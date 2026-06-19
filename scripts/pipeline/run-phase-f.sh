#!/usr/bin/env bash
# Phase F — OEM corpus download + enrich + reindex + ingest (weekly Sunday 02:00)
# DRY_RUN=true → steps 1-2 en simulation, steps 3-4 non exécutés
set -euo pipefail

APP_DIR="/opt/automecanik/app"
RAG_DIR="/opt/automecanik/rag"
ENV_FILE="$APP_DIR/backend/.env"
LOG="$RAG_DIR/logs/phase-f.log"
DRY_RUN="${DRY_RUN:-false}"

mkdir -p "$(dirname "$LOG")"
log() { echo "[$(date -Is)] $*" | tee -a "$LOG"; }

# Précondition : .env doit contenir uniquement des affectations shell simples
if [ ! -f "$ENV_FILE" ]; then
  log "[FAILED] $ENV_FILE not found"; exit 1
fi
set -a
# shellcheck disable=SC1090
source "$ENV_FILE"
set +a

# Vérifier les secrets requis
if [ -z "${INTERNAL_API_KEY:-}" ]; then
  log "[FAILED] INTERNAL_API_KEY not set"; exit 1
fi

# Nom du conteneur RAG (configurable)
RAG_CONTAINER="${RAG_CONTAINER_NAME:-rag-api-prod}"
if ! docker ps --format '{{.Names}}' | grep -q "^${RAG_CONTAINER}$"; then
  log "[FAILED] container $RAG_CONTAINER not running"; exit 1
fi

# Phase F lock dédié (séparation du /tmp/rag-global.lock détenu en permanence
# par auto-enrich-pipeline.sh cron */30 ; collision permanente observée 3 dimanches
# consécutifs 2026-05-10/17/24, runs skip silently). Le lock dédié permet à Phase F
# et auto-enrich de tourner en parallèle — leurs étapes 3-4 hitting le NestJS API
# sont déjà sérialisées côté serveur (HTTP 409 lock_active si conflit réel).
PHASE_F_LOCK="/tmp/rag-phase-f.lock"
exec 8>"$PHASE_F_LOCK"
if ! flock -n 8; then
  log "[SKIP] Phase F déjà en cours (lock $PHASE_F_LOCK détenu) — exit 0"
  exit 0
fi

DRY_RUN_FLAG=""
[ "$DRY_RUN" = "true" ] && DRY_RUN_FLAG="--dry-run"

log "[START] Phase F (DRY_RUN=$DRY_RUN)"

# ── Étape 1 : Download corpus OEM (warning possible, non bloquant) ────────────
# Refactor placement (PR monorepo #270) : scripts/rag/ → scripts/raw-downloaders/
log "[1/4] download-oem-corpus.py"
python3 "$APP_DIR/scripts/raw-downloaders/download-oem-corpus.py" $DRY_RUN_FLAG 2>&1 | tee -a "$LOG"
STEP1_CODE=${PIPESTATUS[0]}
[ $STEP1_CODE -ne 0 ] && log "[WARN] step 1 exited $STEP1_CODE (non-blocking)"

# ── Étape 2 : Générer les gammes .md depuis corpus web (bloquant si échec) ───
# Refactor placement (PR monorepo #270) + redirection OUTPUT (PR #275) :
# scripts/rag/rag-enrich-from-web-corpus.py → scripts/wiki-generators/gamme-from-web-corpus-generator.py
# OUTPUT path passe désormais à automecanik-wiki/exports/rag/gammes/ (ADR-031 §D20).
log "[2/4] gamme-from-web-corpus-generator.py"
python3 "$APP_DIR/scripts/wiki-generators/gamme-from-web-corpus-generator.py" $DRY_RUN_FLAG 2>&1 | tee -a "$LOG"
STEP2_CODE=${PIPESTATUS[0]}
if [ $STEP2_CODE -ne 0 ]; then
  log "[FAILED] step 2 (enrich) exited $STEP2_CODE — aborting"; exit $STEP2_CODE
fi

if [ "$DRY_RUN" = "true" ]; then
  log "[DONE] Phase F dry-run complete (skipped reindex + ingest)"
  exit 0
fi

# ── Étape 3 : Reindex Weaviate — appel DIRECT reindex.py dans le conteneur RAG ─
# Repoint 2026-06-19 : l'ancien wrapper NestJS `POST /api/rag/admin/pipeline/launch`
# a été RETIRÉ (rag-purge B8, monorepo #1028 — RAG ≠ source de contenu, ADR-031/046),
# d'où des 403 récurrents quand ce cron l'appelait encore. On invoque désormais
# reindex.py exactement comme le faisait RagPipelineService.executeReindex :
#   docker exec -e ENV=dev <rag-api> python3 /app/scripts/reindex.py --path /knowledge --cpu-strict
# ENV=dev = kill-switch enforce_build_plane() ; /knowledge = mapping conteneur de
# /opt/automecanik/rag/knowledge ; scope=all → tout /knowledge. Synchrone (plus de polling
# ni de dépendance au NestJS ; la sérialisation Phase F est assurée par PHASE_F_LOCK ci-dessus).
log "[3/4] reindex Weaviate (docker exec reindex.py --path /knowledge, scope=all)"

QUARANTINE_LOG="/tmp/rag_quarantine_phase-f.jsonl"
REINDEX_TIMEOUT_S="${RAG_REINDEX_TIMEOUT_S:-5400}"  # 90 min (parité avec l'ancien polling max)
REINDEX_OUT="$(mktemp)"

set +e
timeout "$REINDEX_TIMEOUT_S" docker exec -e ENV=dev "$RAG_CONTAINER" \
  python3 /app/scripts/reindex.py \
  --path /knowledge \
  --cpu-strict \
  --quarantine-log "$QUARANTINE_LOG" >"$REINDEX_OUT" 2>&1
REINDEX_CODE=$?
set -e
cat "$REINDEX_OUT" >> "$LOG"

if [ "$REINDEX_CODE" -eq 124 ]; then
  rm -f "$REINDEX_OUT"
  log "[FAILED] reindex timed out after $((REINDEX_TIMEOUT_S / 60)) min"; exit 1
fi
if [ "$REINDEX_CODE" -ne 0 ]; then
  rm -f "$REINDEX_OUT"
  log "[FAILED] reindex exited $REINDEX_CODE — aborting"; exit 1
fi

# Détection faux-succès : reindex.py logge "Blocked docs: N" / "Blocked chunks: N"
BLOCKED=$(grep -E "Blocked (docs|chunks): [1-9]" "$REINDEX_OUT" || true)
rm -f "$REINDEX_OUT"
if [ -n "$BLOCKED" ]; then
  log "[WARN] reindex — éléments bloqués détectés :"
  echo "$BLOCKED" | while IFS= read -r l; do log "  $l"; done
else
  log "  reindex completed cleanly (no blocked docs/chunks)"
fi
log "  reindex done ✓"

# ── Étape 4 : Ingest phase5_enrichment → __rag_knowledge (bloquant si échec) ─
log "[4/4] ingest-oem-enriched-gammes.py"
python3 "$APP_DIR/scripts/rag/ingest-oem-enriched-gammes.py" 2>&1 | tee -a "$LOG"
STEP4_CODE=${PIPESTATUS[0]}
if [ $STEP4_CODE -ne 0 ]; then
  log "[FAILED] step 4 (ingest) exited $STEP4_CODE"; exit $STEP4_CODE
fi

log "[DONE] Phase F complete"
