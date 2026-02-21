#!/usr/bin/env bash
set -euo pipefail

# Low-memory reindex helper.
# Runs reindex with very small batch + CPU strict mode.
#
# Usage:
#   ./scripts/reindex_low_memory.sh
#   ./scripts/reindex_low_memory.sh /knowledge 1
#   ./scripts/reindex_low_memory.sh /knowledge 1 50
#
# Args:
#   1: path (default /knowledge)
#   2: batch size (default 1)
#   3: max files (default 0 = unlimited)

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
KNOWLEDGE_PATH="${1:-/knowledge}"
BATCH_SIZE="${2:-1}"
MAX_FILES="${3:-0}"

cd "$ROOT_DIR"

docker compose -p rag -f docker-compose.prod.yml run --rm --no-deps rag-api sh -lc "
  set -euo pipefail
  ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 \
  REINDEX_BATCH_SIZE=$BATCH_SIZE \
  MALLOC_ARENA_MAX=2 \
  python scripts/reindex.py \
    --path $KNOWLEDGE_PATH \
    --batch-size $BATCH_SIZE \
    --max-files $MAX_FILES \
    --cpu-strict
"
