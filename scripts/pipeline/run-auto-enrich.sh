#!/usr/bin/env bash
# Wrapper cron — charge les clés depuis le .env NestJS et lance le pipeline
set -euo pipefail

ENV_FILE="/opt/automecanik/app/backend/.env"

if [ ! -f "$ENV_FILE" ]; then
  echo "[$(date -Is)] ERROR: .env not found at $ENV_FILE" >&2
  exit 1
fi

export RAG_API_KEY=$(grep '^RAG_API_KEY=' "$ENV_FILE" | cut -d'=' -f2)
export INTERNAL_API_KEY=$(grep '^INTERNAL_API_KEY=' "$ENV_FILE" | cut -d'=' -f2)
export RAG_SERVICE_URL="http://localhost:8000"
export NESTJS_URL="http://localhost:3000"

exec /opt/automecanik/rag/scripts/pipeline/auto-enrich-pipeline.sh "$@"
