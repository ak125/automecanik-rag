#!/usr/bin/env bash
set -euo pipefail

# One-command workflow:
# 1) ingest local PDFs into /knowledge as cleaned/auto-classified markdown
# 2) index resulting corpus into Weaviate
#
# Usage:
#   ./scripts/import_and_index_pdfs.sh /opt/automecanik/rag/pdfs
#   ./scripts/import_and_index_pdfs.sh /opt/automecanik/rag/pdfs L2

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PDF_DIR="${1:-$ROOT_DIR/pdfs}"
TRUTH_LEVEL="${2:-L3}"
LOW_MEMORY="${LOW_MEMORY:-1}"
REINDEX_BATCH_SIZE="${REINDEX_BATCH_SIZE:-1}"
REINDEX_MAX_FILES="${REINDEX_MAX_FILES:-0}"

if [[ ! -d "$PDF_DIR" ]]; then
  echo "ERROR: PDF directory not found: $PDF_DIR"
  exit 1
fi

PDF_COUNT="$(find "$PDF_DIR" -type f -iname '*.pdf' | wc -l | tr -d ' ')"
if [[ "$PDF_COUNT" -eq 0 ]]; then
  echo "ERROR: no PDF files found in $PDF_DIR"
  exit 1
fi

echo "PDF directory: $PDF_DIR"
echo "PDF files: $PDF_COUNT"
echo "Truth level: $TRUTH_LEVEL"
echo "Low memory mode: $LOW_MEMORY"
echo "Running import + index in one-shot container..."

cd "$ROOT_DIR"

docker compose -p rag -f docker-compose.prod.yml run --rm \
  -v "$ROOT_DIR/knowledge:/knowledge-import:rw" \
  -v "$PDF_DIR:/app/pdfs:ro" \
  rag-api sh -lc "
    set -euo pipefail
    ENV=dev KNOWLEDGE_PATH=/knowledge-import python scripts/ingestors/ingest_pdfs.py --input /app/pdfs --truth-level $TRUTH_LEVEL
    if [ \"$LOW_MEMORY\" = \"1\" ]; then
      ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 REINDEX_BATCH_SIZE=$REINDEX_BATCH_SIZE \
      python scripts/reindex.py --path /knowledge-import --batch-size $REINDEX_BATCH_SIZE --max-files $REINDEX_MAX_FILES --cpu-strict
    else
      ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 python scripts/reindex.py --path /knowledge-import
    fi
  "

echo "Done."
