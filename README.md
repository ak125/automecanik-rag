# AutoMecanik RAG Service

Service RAG (Retrieval-Augmented Generation) pour le support client AutoMecanik.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    RAG Service (FastAPI)                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │
│  │ POST /chat  │  │ POST /search│  │ GET /health │          │
│  └──────┬──────┘  └──────┬──────┘  └─────────────┘          │
│         │                │                                   │
│  ┌──────▼────────────────▼──────┐                           │
│  │        RAG Service            │                           │
│  │  Search → Format → Generate   │                           │
│  └──────┬────────────────┬──────┘                           │
│         │                │                                   │
│  ┌──────▼──────┐  ┌──────▼──────┐                           │
│  │  Weaviate   │  │   Claude    │                           │
│  │ (Hybrid DB) │  │   (LLM)     │                           │
│  └─────────────┘  └─────────────┘                           │
└─────────────────────────────────────────────────────────────┘
```

## Quick Start

### 1. Configuration

```bash
cp .env.example .env
# Edit .env with your API keys
```

### 2. Start Services

```bash
docker-compose up -d
```

### 3. Initialize Schema

```bash
docker-compose exec rag-api python scripts/init_schema.py
```

### 4. Index Knowledge Base

```bash
docker-compose exec rag-api python scripts/build_index.py /path/to/knowledge
```

### 5. Test API

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -H "X-RAG-API-Key: your-api-key" \
  -d '{"message": "Quels sont les délais de livraison?"}'
```

## API Endpoints

### POST /chat

Chat with the RAG system.

**Request:**
```json
{
  "message": "Quels sont les délais de livraison?",
  "session_id": "optional-session-id"
}
```

**Response:**
```json
{
  "answer": "Les délais de livraison sont...",
  "sources": ["faq/livraison.md"],
  "session_id": "generated-or-provided-id",
  "confidence": 0.85
}
```

### POST /search

Semantic search without generation.

**Request:**
```json
{
  "query": "livraison express",
  "limit": 5
}
```

### GET /health

Health check.

## Development

### Local Development

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run with hot reload
uvicorn app.main:app --reload --port 8000
```

### Running Tests

```bash
pytest tests/ -v
```

## Knowledge Base Structure

The service indexes markdown files from the `/knowledge` directory:

```
knowledge/
├── faq/
│   ├── livraison.md
│   ├── retours.md
│   └── paiement.md
├── policies/
│   ├── retours.md
│   ├── garantie.md
│   └── livraison.md
└── README.md
```

Each markdown file should have frontmatter:

```markdown
---
id: faq.livraison.delais
category: livraison
priority: high
---

# Quels sont les délais de livraison?

Content here...
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `ENV` | Environment (dev/staging/prod) | dev |
| `WEAVIATE_URL` | Weaviate server URL | http://weaviate:8080 |
| `ANTHROPIC_API_KEY` | Claude API key | Required |
| `OPENAI_API_KEY` | OpenAI API key (embeddings) | Required |
| `RAG_API_KEY` | API authentication key | Required |

## License

Proprietary - AutoMecanik
