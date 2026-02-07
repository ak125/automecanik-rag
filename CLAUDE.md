# CLAUDE.md

## Project Overview

AutoMecanik RAG Service -- a Retrieval-Augmented Generation system for customer support on an automotive parts e-commerce platform. Built with FastAPI + Weaviate + Claude, it provides semantic search across a knowledge base with truth-level metadata (L1-L4) and guardrailed LLM responses.

The project philosophy is "100% gratuite" -- free/local embeddings (FastEmbed), open-source vector DB (Weaviate), with Claude as the only paid component for generation.

## Tech Stack

- **Language:** Python 3.11
- **Framework:** FastAPI + Uvicorn
- **Vector DB:** Weaviate (hybrid search: BM25 + vector)
- **Embeddings:** FastEmbed with `all-MiniLM-L6-v2` (384 dimensions, local/free)
- **LLM:** Anthropic Claude (`claude-3-5-sonnet-20241022`)
- **Orchestration:** LangGraph + LangChain Core
- **Cache:** Redis
- **Config:** Pydantic Settings + `rag_config.yml` (YAML is source of truth, env vars can override)
- **Infrastructure:** Docker Compose (rag-api, weaviate, redis)

## Key Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v

# Run golden tests (regression suite)
python tests/run_golden_tests.py

# Start dev server (requires Weaviate + Redis running)
uvicorn app.main:app --reload --port 8000

# Start full stack
docker-compose up -d

# Start dev stack with relaxed thresholds
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d

# Initialize Weaviate schema
python scripts/init_schema.py

# Build knowledge index
python scripts/build_index.py /knowledge

# Reindex all documents
python scripts/reindex.py
```

## Architecture

```
app/
  main.py              # FastAPI app, middleware setup, startup validation
  config.py            # Pydantic settings, kill switch logic, env/YAML config
  api/
    chat.py            # POST /chat (context-only) and POST /chat/v2 (LangGraph)
    search.py          # POST /search (semantic search)
    health.py          # GET /health
    knowledge.py       # Knowledge admin CRUD
  services/
    rag_service.py     # Core search + truth-level analysis
    weaviate_client.py # Weaviate vector DB client
    claude_client.py   # Claude LLM client
    langgraph_flow.py  # LangGraph pipeline: classify -> retrieve -> guardrails -> generate/refuse
    embeddings.py      # FastEmbed integration
    security_validator.py  # Prompt injection + PII detection
    startup_validator.py   # Quarantine mode startup checks
    namespace_guard.py     # Namespace access control (HARDCODED prod namespaces)
    index_version_manager.py
  middleware/
    rate_limiter.py    # Sliding window rate limiter (60 req/min)
  prompts/
    templates.py       # System prompts with truth-level guidelines
  admin/               # Admin web UI (Jinja2 templates)
orchestrator/          # BUILD-plane only (never runs in prod)
  kill_switch.py       # CRITICAL: prevents writes in prod environments
  pipeline.py          # Indexing pipeline (extract -> chunk -> embed -> upsert)
  extractors/          # MinIO, Wiki extractors
  processors/          # Chunking, embedding processors
knowledge/             # Markdown knowledge corpus with YAML frontmatter
scripts/               # Utility scripts (indexing, schema init, wiki export)
tests/                 # pytest suite + golden tests
```

## Critical Safety Mechanisms

### Kill Switch (BUILD vs RUNTIME planes)
- **BUILD plane** (dev, ci, staging): write operations allowed
- **RUNTIME plane** (prod, production): read-only ALWAYS
- Enforced in `app/config.py` (`can_write()`), `orchestrator/kill_switch.py` (`enforce_build_plane()`), and `app/main.py` (startup)
- `AI_PROD_WRITE` env var is blocked in prod regardless of value

### Quarantine Mode
- Validates startup conditions before serving: Weaviate connection, embedding dimension match, corpus not empty
- Configured in `rag_config.yml` under `quarantine:`
- `fail_fast: true` exits on failure by default

### Namespace Guard
- PROD namespaces are HARDCODED in `app/services/namespace_guard.py` (not configurable via env)
- Default namespace: `knowledge:faq`

## Truth Level System (L1-L4)

| Level | Name | Weight | Meaning |
|-------|------|--------|---------|
| L1 | Faits verifies | 1.0 | Verified facts, official docs |
| L2 | Regles metier | 0.9 | Business rules, established procedures |
| L3 | Hypotheses | 0.6 | Reasoned inferences |
| L4 | Heuristiques | 0.4 | Rules of thumb, approximations |

**Mixing rules:** L1+L2 allowed, L1+L3 warning, L1+L4 forbidden, L3+L4 forbidden.

## API Modes

1. **POST /chat** -- Context-only mode. Returns formatted context with sources, no LLM generation.
2. **POST /chat/v2** -- Full LangGraph pipeline: classify -> retrieve -> guardrails -> generate/refuse. Returns generated response with citations.
3. **POST /search** -- Direct semantic search with truth-level metadata.

All endpoints require `X-API-Key` header.

## Configuration Precedence

Environment variables override `rag_config.yml` values. Key env vars:
- `ENV` (dev/staging/prod), `WEAVIATE_URL`, `REDIS_URL`, `RAG_API_KEY`
- `RETRIEVAL_TOP_K`, `RETRIEVAL_ALPHA`, `KNOWLEDGE_PATH`
- See `.env.example` and `.env.prod.example` for templates

## Knowledge Base

Markdown files in `knowledge/` with YAML frontmatter (title, source_type, category, truth_level). Organized into: `diagnostic/`, `vehicle/`, `faq/`, `guide/`, `policies/`. Auto-reindexed via GitHub Actions on PR merge to main when `knowledge/**` changes.

## Development Notes

- The project is bilingual (French/English). Comments and config are often in French.
- Security is layered: CORS hardening, API key auth, rate limiting, prompt injection detection, PII detection, namespace guards, kill switch.
- Tests use mocked services (RAG, Weaviate). Golden tests in `tests/golden_queries.json` provide regression coverage.
- Docker health checks hit `GET /health` every 30s. The API runs as non-root user `appuser`.
