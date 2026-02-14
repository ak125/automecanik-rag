#!/usr/bin/env bash
set -euo pipefail

# One-command workflow:
# 1) ingest web URLs to clean markdown corpus
# 2) index web knowledge into KB_Knowledge
# 3) index web catalog into KB_Catalog
#
# Usage:
#   ./scripts/import_and_index_web.sh --url https://example.com
#   ./scripts/import_and_index_web.sh --urls-file ./urls.txt --truth-level L3

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TRUTH_LEVEL="L3"
LOW_MEMORY="${LOW_MEMORY:-1}"
REINDEX_BATCH_SIZE="${REINDEX_BATCH_SIZE:-1}"
REINDEX_MAX_FILES="${REINDEX_MAX_FILES:-0}"
URL_ARGS=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --url)
      URL_ARGS+=("--url" "${2:-}")
      shift 2
      ;;
    --urls-file)
      URL_ARGS+=("--urls-file" "${2:-}")
      shift 2
      ;;
    --truth-level)
      TRUTH_LEVEL="${2:-L3}"
      shift 2
      ;;
    *)
      echo "Unknown argument: $1"
      exit 1
      ;;
  esac
done

if [[ ${#URL_ARGS[@]} -eq 0 ]]; then
  echo "ERROR: provide --url ... or --urls-file ..."
  exit 1
fi

cd "$ROOT_DIR"

docker compose -p rag -f docker-compose.prod.yml run --rm \
  -v "$ROOT_DIR/knowledge:/knowledge-import:rw" \
  rag-api sh -lc "
    set -euo pipefail
    ENV=dev KNOWLEDGE_PATH=/knowledge-import python scripts/ingest_web.py ${URL_ARGS[*]} --truth-level $TRUTH_LEVEL
    if [ -d /knowledge-import/web ]; then
      if [ \"$LOW_MEMORY\" = \"1\" ]; then
        ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 REINDEX_BATCH_SIZE=$REINDEX_BATCH_SIZE \
        python scripts/reindex.py --path /knowledge-import/web --collection KB_Knowledge --batch-size $REINDEX_BATCH_SIZE --max-files $REINDEX_MAX_FILES --cpu-strict
      else
        ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 python scripts/reindex.py --path /knowledge-import/web --collection KB_Knowledge
      fi
    fi
    if [ -d /knowledge-import/web-catalog ]; then
      if [ \"$LOW_MEMORY\" = \"1\" ]; then
        ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 REINDEX_BATCH_SIZE=$REINDEX_BATCH_SIZE \
        python scripts/reindex.py --path /knowledge-import/web-catalog --collection KB_Catalog --batch-size $REINDEX_BATCH_SIZE --max-files $REINDEX_MAX_FILES --cpu-strict
      else
        ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 python scripts/reindex.py --path /knowledge-import/web-catalog --collection KB_Catalog
      fi
    fi
  "

echo "Done."
