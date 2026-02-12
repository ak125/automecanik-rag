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

### 4a. Init Ingest Tree (Prod-Ready)

```bash
./scripts/init_ingest_tree.sh
```

Optional custom base path:

```bash
./scripts/init_ingest_tree.sh /opt/automecanik/rag/ingest
```

Created structure:

```text
ingest/
  inbox/{pdf,images,videos,urls.txt}
  raw/{pdf,images,videos,web,db}
  normalized/{pdf,images,videos,web,db}
  chunks/{KB_Knowledge,KB_Diagnostic,KB_Catalog,KB_Media}
  logs/{ingest_jobs.jsonl,retrieval_logs.jsonl}
  quarantine/
  tmp/
```

### 4b. Ingest PDF Files (Local Folder)

```bash
# Build plane only (ENV=dev/ci/staging)
ENV=dev python scripts/ingest_pdfs.py --input /opt/automecanik/rag/pdfs

# Preview auto classification without writing files
ENV=dev python scripts/ingest_pdfs.py --input /opt/automecanik/rag/pdfs --dry-run
```

### 4c. One Command: Batch Import + Batch Index

```bash
./scripts/import_and_index_pdfs.sh /opt/automecanik/rag/pdfs
```

Low-memory mode is enabled by default in this script (`batch-size=1`, `cpu-strict`).

```bash
# Optional tuning
LOW_MEMORY=1 REINDEX_BATCH_SIZE=1 REINDEX_MAX_FILES=0 ./scripts/import_and_index_pdfs.sh /opt/automecanik/rag/pdfs
```

### 4d. Translate Imported Markdown EN -> FR

```bash
# Dry-run preview
ANTHROPIC_API_KEY=... python scripts/translate_md_en_to_fr.py --input /opt/automecanik/rag/knowledge --dry-run

# Real translation
ANTHROPIC_API_KEY=... python scripts/translate_md_en_to_fr.py --input /opt/automecanik/rag/knowledge
```

### 4e. Dedicated Low-Memory Reindex Helper

```bash
# path, batch-size, max-files
./scripts/reindex_low_memory.sh /knowledge 1 0
```

### 4e-bis. Ingest Tabular Data (CSV/XLSX) - ULTRA Rule

```bash
# Profile + controlled snapshots (no raw indexing by default)
./scripts/import_and_index_tabular.sh /opt/automecanik/rag/data/products.csv
```

Optional entity key:

```bash
./scripts/import_and_index_tabular.sh /opt/automecanik/rag/data/products.xlsx sku
```

Behavior:
- always generates `tabular/profiles/*_dataset_profile.md` (KB_Knowledge)
- optionally generates `tabular/entity_snapshots/*` (KB_Catalog)
- never indexes raw rows by default
- appends ingest decision to `ingest/logs/ingest_jobs.jsonl`

### 4e-ter. Ingest Structured Exports (JSON/XML) - ULTRA Rule

```bash
# Structure profile + controlled snapshots (no raw indexing by default)
./scripts/import_and_index_structured.sh /opt/automecanik/rag/data/export.json
```

Optional entity key:

```bash
./scripts/import_and_index_structured.sh /opt/automecanik/rag/data/export.xml id
```

Behavior:
- always generates `structured/profiles/*_structure_profile.md` (KB_Knowledge)
- optionally generates `structured/entity_snapshots/*` (KB_Catalog)
- never indexes raw records by default
- appends ingest decision to `ingest/logs/ingest_jobs.jsonl`

### 4f. Extract Images from PDF (for video content)

```bash
# Extract embedded images from all PDFs in /app/pdfs
docker exec rag-api-prod sh -lc "python scripts/extract_pdf_images.py --input /app/pdfs --output /app/pdf-images"
```

Each PDF gets its own output folder with a `manifest.json`:
- image file path
- page number
- image size in bytes
- dimensions when available

### 4g. Build Storyboard (CSV + JSON)

```bash
python scripts/build_video_storyboard.py \
  --input /opt/automecanik/rag/pdf-images \
  --output /opt/automecanik/rag/pdf-images/storyboard
```

### 4h. Normalize Binary Image Files (.bin -> real format)

```bash
python scripts/normalize_pdf_images.py --input /opt/automecanik/rag/pdf-images
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

### Eval Gate

Run eval + thresholds gate locally:

```bash
RAG_API_KEY="your-key" make eval-gate
```

Optional overrides:

```bash
RAG_API_KEY="your-key" make eval-gate RAG_URL="http://127.0.0.1:8000" EVAL_OUT="tests/eval_report.json"
```

CI workflow:
- `.github/workflows/rag-eval-gate.yml` (manual dispatch)
- requires repository secret `RAG_API_KEY`

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
