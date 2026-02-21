#!/usr/bin/env bash
set -euo pipefail

# Ingest DB "knowledge views" then index:
# - schema docs -> KB_Knowledge
# - entity snapshots -> KB_Catalog
#
# Usage:
#   DB_URL='postgresql://...' ./scripts/import_and_index_db.sh \
#     --provider supabase \
#     --fact-query "pieces::id::SELECT id, sku, brand, price FROM pieces LIMIT 100"

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROVIDER="supabase"
SCHEMA_TRUTH_LEVEL="L2"
FACTS_TRUTH_LEVEL="L3"
LOW_MEMORY="${LOW_MEMORY:-1}"
REINDEX_BATCH_SIZE="${REINDEX_BATCH_SIZE:-1}"
REINDEX_MAX_FILES="${REINDEX_MAX_FILES:-0}"
FACT_ARGS=()
INGEST_FLAGS=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --provider)
      PROVIDER="${2:-supabase}"
      shift 2
      ;;
    --schema-truth-level)
      SCHEMA_TRUTH_LEVEL="${2:-L2}"
      shift 2
      ;;
    --facts-truth-level)
      FACTS_TRUTH_LEVEL="${2:-L3}"
      shift 2
      ;;
    --fact-query)
      FACT_ARGS+=("--fact-query" "${2:-}")
      shift 2
      ;;
    --skip-query-errors)
      INGEST_FLAGS+=("--skip-query-errors")
      shift 1
      ;;
    *)
      echo "Unknown argument: $1"
      exit 1
      ;;
  esac
done

if [[ -z "${DB_URL:-}" ]]; then
  echo "ERROR: DB_URL env var is required"
  exit 1
fi

cd "$ROOT_DIR"

docker compose -p rag -f docker-compose.prod.yml run --rm \
  -e DB_URL="$DB_URL" \
  -v "$ROOT_DIR/knowledge:/knowledge-import:rw" \
  rag-api sh -lc "
    set -euo pipefail
    ENV=dev KNOWLEDGE_PATH=/knowledge-import python scripts/ingestors/ingest_db.py \
      --db-url \"\$DB_URL\" \
      --provider \"$PROVIDER\" \
      --schema-truth-level \"$SCHEMA_TRUTH_LEVEL\" \
      --facts-truth-level \"$FACTS_TRUTH_LEVEL\" \
      ${INGEST_FLAGS[*]} \
      ${FACT_ARGS[*]}
    if [ -d /knowledge-import/db/schema ]; then
      if [ \"$LOW_MEMORY\" = \"1\" ]; then
        ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 REINDEX_BATCH_SIZE=$REINDEX_BATCH_SIZE \
        python scripts/reindex.py --path /knowledge-import/db/schema --collection KB_Knowledge --batch-size $REINDEX_BATCH_SIZE --max-files $REINDEX_MAX_FILES --cpu-strict
      else
        ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 python scripts/reindex.py --path /knowledge-import/db/schema --collection KB_Knowledge
      fi
    fi
    if [ -d /knowledge-import/db/entity_snapshots ]; then
      if [ \"$LOW_MEMORY\" = \"1\" ]; then
        ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 REINDEX_BATCH_SIZE=$REINDEX_BATCH_SIZE \
        python scripts/reindex.py --path /knowledge-import/db/entity_snapshots --collection KB_Catalog --batch-size $REINDEX_BATCH_SIZE --max-files $REINDEX_MAX_FILES --cpu-strict
      else
        ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 python scripts/reindex.py --path /knowledge-import/db/entity_snapshots --collection KB_Catalog
      fi
    fi
  "

echo "Done."
