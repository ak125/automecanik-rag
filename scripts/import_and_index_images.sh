#!/usr/bin/env bash
set -euo pipefail

# One-command workflow:
# 1) ingest local images into /knowledge as media markdown docs (caption + ocr blocks)
# 2) index resulting corpus into Weaviate KB_Media
#
# Usage:
#   ./scripts/import_and_index_images.sh /opt/automecanik/rag/pdf-images
#   ./scripts/import_and_index_images.sh /opt/automecanik/rag/pdf-images L3

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMG_DIR="${1:-$ROOT_DIR/pdf-images}"
TRUTH_LEVEL="${2:-L3}"
LOW_MEMORY="${LOW_MEMORY:-1}"
REINDEX_BATCH_SIZE="${REINDEX_BATCH_SIZE:-1}"
REINDEX_MAX_FILES="${REINDEX_MAX_FILES:-0}"
MEDIA_KNOWLEDGE_PATH="${MEDIA_KNOWLEDGE_PATH:-/knowledge-import/media}"

if [[ ! -d "$IMG_DIR" ]]; then
  echo "ERROR: image directory not found: $IMG_DIR"
  exit 1
fi

IMG_COUNT="$(find "$IMG_DIR" -type f \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.webp' -o -iname '*.bmp' -o -iname '*.tif' -o -iname '*.tiff' \) | wc -l | tr -d ' ')"
if [[ "$IMG_COUNT" -eq 0 ]]; then
  echo "ERROR: no image files found in $IMG_DIR"
  exit 1
fi

echo "Image directory: $IMG_DIR"
echo "Image files: $IMG_COUNT"
echo "Truth level: $TRUTH_LEVEL"
echo "Target collection: KB_Media"
echo "Low memory mode: $LOW_MEMORY"
echo "Running import + index in one-shot container..."

cd "$ROOT_DIR"

docker compose -p rag -f docker-compose.prod.yml run --rm \
  -v "$ROOT_DIR/knowledge:/knowledge-import:rw" \
  -v "$IMG_DIR:/app/images:ro" \
  rag-api sh -lc "
    set -euo pipefail
    ENV=dev KNOWLEDGE_PATH=/knowledge-import python scripts/ingest_images.py --input /app/images --truth-level $TRUTH_LEVEL
    test -d \"$MEDIA_KNOWLEDGE_PATH\"
    if [ \"$LOW_MEMORY\" = \"1\" ]; then
      ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 REINDEX_BATCH_SIZE=$REINDEX_BATCH_SIZE \
      python scripts/reindex.py --path \"$MEDIA_KNOWLEDGE_PATH\" --collection KB_Media --batch-size $REINDEX_BATCH_SIZE --max-files $REINDEX_MAX_FILES --cpu-strict
    else
      ENV=dev WEAVIATE_URL=http://weaviate-prod:8080 python scripts/reindex.py --path \"$MEDIA_KNOWLEDGE_PATH\" --collection KB_Media
    fi
  "

echo "Done."
