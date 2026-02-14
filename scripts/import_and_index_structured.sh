#!/usr/bin/env bash
set -euo pipefail

# Ingest JSON/XML -> structure profile + controlled snapshots, then index:
# - structured/profiles -> KB_Knowledge
# - structured/entity_snapshots -> KB_Catalog
#
# Usage:
#   ./scripts/import_and_index_structured.sh /opt/automecanik/rag/data/export.json
#   ./scripts/import_and_index_structured.sh /opt/automecanik/rag/data/export.xml sku

INPUT_PATH="${1:-}"
SNAPSHOT_KEY="${2:-}"
PROFILE_TRUTH_LEVEL="${PROFILE_TRUTH_LEVEL:-L3}"
SNAPSHOT_TRUTH_LEVEL="${SNAPSHOT_TRUTH_LEVEL:-L3}"
SNAPSHOT_TOP_N="${SNAPSHOT_TOP_N:-200}"
REINDEX_BATCH_SIZE="${REINDEX_BATCH_SIZE:-20}"
REINDEX_MAX_FILES="${REINDEX_MAX_FILES:-0}"
LOW_MEMORY="${LOW_MEMORY:-0}"

if [ -z "$INPUT_PATH" ]; then
  echo "Usage: $0 /abs/path/to/file.json|xml [snapshot_key]"
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
INPUT_ABS="$(cd "$(dirname "$INPUT_PATH")" && pwd)/$(basename "$INPUT_PATH")"

if [ ! -f "$INPUT_ABS" ]; then
  echo "Input file not found: $INPUT_ABS"
  exit 1
fi

echo "Running structured import + index"
echo "Input: $INPUT_ABS"

docker run --rm \
  --network rag_default \
  -v "$ROOT_DIR:/app:rw" \
  -v "$ROOT_DIR/knowledge:/knowledge-import:rw" \
  -w /app \
  rag-api:latest \
  /bin/bash -lc "
    set -euo pipefail
    ENV=dev KNOWLEDGE_PATH=/knowledge-import python scripts/ingest_structured.py \
      --input \"$INPUT_ABS\" \
      --profile-truth-level \"$PROFILE_TRUTH_LEVEL\" \
      --snapshot-truth-level \"$SNAPSHOT_TRUTH_LEVEL\" \
      --snapshot-top-n \"$SNAPSHOT_TOP_N\" \
      ${SNAPSHOT_KEY:+--snapshot-key \"$SNAPSHOT_KEY\"}

    if [ -d /knowledge-import/structured/profiles ]; then
      if [ \"$LOW_MEMORY\" = \"1\" ]; then
        ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 REINDEX_BATCH_SIZE=$REINDEX_BATCH_SIZE \
        python scripts/reindex.py --path /knowledge-import/structured/profiles --collection KB_Knowledge --batch-size $REINDEX_BATCH_SIZE --max-files $REINDEX_MAX_FILES --cpu-strict
      else
        ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 python scripts/reindex.py --path /knowledge-import/structured/profiles --collection KB_Knowledge
      fi
    fi

    if [ -d /knowledge-import/structured/entity_snapshots ]; then
      if [ \"$LOW_MEMORY\" = \"1\" ]; then
        ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 REINDEX_BATCH_SIZE=$REINDEX_BATCH_SIZE \
        python scripts/reindex.py --path /knowledge-import/structured/entity_snapshots --collection KB_Catalog --batch-size $REINDEX_BATCH_SIZE --max-files $REINDEX_MAX_FILES --cpu-strict
      else
        ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 python scripts/reindex.py --path /knowledge-import/structured/entity_snapshots --collection KB_Catalog
      fi
    fi
  "

echo "Done."
