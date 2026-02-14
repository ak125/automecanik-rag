#!/usr/bin/env bash
set -euo pipefail

BASE="${1:-/opt/automecanik/rag/ingest}"

DIRS=(
  "$BASE/inbox/pdf"
  "$BASE/inbox/images"
  "$BASE/inbox/videos"
  "$BASE/raw/pdf"
  "$BASE/raw/images"
  "$BASE/raw/videos"
  "$BASE/raw/web"
  "$BASE/raw/db"
  "$BASE/normalized/pdf"
  "$BASE/normalized/images"
  "$BASE/normalized/videos"
  "$BASE/normalized/web"
  "$BASE/normalized/db"
  "$BASE/chunks/KB_Knowledge"
  "$BASE/chunks/KB_Diagnostic"
  "$BASE/chunks/KB_Catalog"
  "$BASE/chunks/KB_Media"
  "$BASE/logs"
  "$BASE/quarantine"
  "$BASE/tmp"
)

for d in "${DIRS[@]}"; do
  mkdir -p "$d"
done

: > "$BASE/inbox/urls.txt"
: > "$BASE/logs/ingest_jobs.jsonl"
: > "$BASE/logs/retrieval_logs.jsonl"

find "$BASE" -type d -exec sh -c 'for d; do [ -f "$d/.keep" ] || : > "$d/.keep"; done' sh {} +

chmod -R 750 "$BASE"
chmod 640 "$BASE/inbox/urls.txt" "$BASE/logs/ingest_jobs.jsonl" "$BASE/logs/retrieval_logs.jsonl"

echo "Ingest tree ready at: $BASE"
