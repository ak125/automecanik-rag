#!/usr/bin/env bash
set -euo pipefail

# One-command workflow:
# 1) ingest local videos into /knowledge as media markdown docs (transcript + keyframes)
# 2) index media docs to KB_Media
# 3) index promoted canonical docs to KB_Knowledge
#
# Usage:
#   ./scripts/import_and_index_videos.sh /opt/automecanik/rag/videos
#   ./scripts/import_and_index_videos.sh /opt/automecanik/rag/videos L3

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VID_DIR="${1:-$ROOT_DIR/videos}"
TRUTH_LEVEL="${2:-L3}"
LOW_MEMORY="${LOW_MEMORY:-1}"
REINDEX_BATCH_SIZE="${REINDEX_BATCH_SIZE:-1}"
REINDEX_MAX_FILES="${REINDEX_MAX_FILES:-0}"
MEDIA_PATH="${MEDIA_PATH:-/knowledge-import/video}"
CANONICAL_PATH="${CANONICAL_PATH:-/knowledge-import/canonical}"

if [[ ! -d "$VID_DIR" ]]; then
  echo "ERROR: video directory not found: $VID_DIR"
  exit 1
fi

VID_COUNT="$(find "$VID_DIR" -type f \( -iname '*.mp4' -o -iname '*.mov' -o -iname '*.mkv' -o -iname '*.webm' -o -iname '*.m4v' -o -iname '*.avi' \) | wc -l | tr -d ' ')"
if [[ "$VID_COUNT" -eq 0 ]]; then
  echo "ERROR: no video files found in $VID_DIR"
  exit 1
fi

echo "Video directory: $VID_DIR"
echo "Video files: $VID_COUNT"
echo "Truth level: $TRUTH_LEVEL"
echo "Target collections: KB_Media (+ KB_Knowledge for canonical promotions)"

cd "$ROOT_DIR"

docker compose -p rag -f docker-compose.prod.yml run --rm \
  -v "$ROOT_DIR/knowledge:/knowledge-import:rw" \
  -v "$VID_DIR:/app/videos:ro" \
  rag-api sh -lc "
    set -euo pipefail
    ENV=dev KNOWLEDGE_PATH=/knowledge-import python scripts/ingest_videos.py --input /app/videos --truth-level $TRUTH_LEVEL
    test -d \"$MEDIA_PATH\"
    if [ \"$LOW_MEMORY\" = \"1\" ]; then
      ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 REINDEX_BATCH_SIZE=$REINDEX_BATCH_SIZE \
      python scripts/reindex.py --path \"$MEDIA_PATH\" --collection KB_Media --batch-size $REINDEX_BATCH_SIZE --max-files $REINDEX_MAX_FILES --cpu-strict
    else
      ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 python scripts/reindex.py --path \"$MEDIA_PATH\" --collection KB_Media
    fi
    if [ -d \"$CANONICAL_PATH\" ]; then
      if [ \"$LOW_MEMORY\" = \"1\" ]; then
        ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 REINDEX_BATCH_SIZE=$REINDEX_BATCH_SIZE \
        python scripts/reindex.py --path \"$CANONICAL_PATH\" --collection KB_Knowledge --batch-size $REINDEX_BATCH_SIZE --max-files $REINDEX_MAX_FILES --cpu-strict
      else
        ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 python scripts/reindex.py --path \"$CANONICAL_PATH\" --collection KB_Knowledge
      fi
    fi
  "

echo "Done."
