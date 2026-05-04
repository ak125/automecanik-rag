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
  log "ERROR: $ENV_FILE not found"; exit 1
fi
set -a
# shellcheck disable=SC1090
source "$ENV_FILE"
set +a

# Vérifier les secrets requis
if [ -z "${INTERNAL_API_KEY:-}" ]; then
  log "ERROR: INTERNAL_API_KEY not set"; exit 1
fi

# Nom du conteneur RAG (configurable)
RAG_CONTAINER="${RAG_CONTAINER_NAME:-rag-api-prod}"
if ! docker ps --format '{{.Names}}' | grep -q "^${RAG_CONTAINER}$"; then
  log "ERROR: container $RAG_CONTAINER not running"; exit 1
fi

# Global lock (ne pas tourner en même temps que le pipeline PDF)
GLOBAL_LOCK="/tmp/rag-global.lock"
exec 8>"$GLOBAL_LOCK"
if ! flock -n 8; then
  log "Another RAG operation active, skipping Phase F"; exit 0
fi

DRY_RUN_FLAG=""
[ "$DRY_RUN" = "true" ] && DRY_RUN_FLAG="--dry-run"

log "=== Phase F start (DRY_RUN=$DRY_RUN) ==="

# ── Étape 1 : Download corpus OEM (warning possible, non bloquant) ────────────
# Refactor placement (PR monorepo #270) : scripts/rag/ → scripts/raw-downloaders/
log "[1/4] download-oem-corpus.py"
python3 "$APP_DIR/scripts/raw-downloaders/download-oem-corpus.py" $DRY_RUN_FLAG 2>&1 | tee -a "$LOG"
STEP1_CODE=${PIPESTATUS[0]}
[ $STEP1_CODE -ne 0 ] && log "WARN: step 1 exited $STEP1_CODE (non-blocking)"

# ── Étape 2 : Générer les gammes .md depuis corpus web (bloquant si échec) ───
# Refactor placement (PR monorepo #270) + redirection OUTPUT (PR #275) :
# scripts/rag/rag-enrich-from-web-corpus.py → scripts/wiki-generators/gamme-from-web-corpus-generator.py
# OUTPUT path passe désormais à automecanik-wiki/exports/rag/gammes/ (ADR-031 §D20).
log "[2/4] gamme-from-web-corpus-generator.py"
python3 "$APP_DIR/scripts/wiki-generators/gamme-from-web-corpus-generator.py" $DRY_RUN_FLAG 2>&1 | tee -a "$LOG"
STEP2_CODE=${PIPESTATUS[0]}
if [ $STEP2_CODE -ne 0 ]; then
  log "ERROR: step 2 (enrich) exited $STEP2_CODE — aborting"; exit $STEP2_CODE
fi

if [ "$DRY_RUN" = "true" ]; then
  log "DRY_RUN=true — skipping reindex and ingest"
  log "=== Phase F dry-run complete ==="
  exit 0
fi

# ── Étape 3 : Reindex via pipeline API + polling (bloquant si échec) ─────────
log "[3/4] pipeline launch reindex (scope=all)"

# Capturer body + code HTTP séparément pour diagnostic précis
REINDEX_BODY=$(curl -s -o /tmp/phase-f-launch-body.txt -w "%{http_code}" \
  -X POST \
  -H "Content-Type: application/json" \
  -H "X-Internal-Key: $INTERNAL_API_KEY" \
  -d '{"step":"reindex","scope":"all"}' \
  "http://localhost:3000/api/rag/admin/pipeline/launch" 2>/dev/null || echo "000")
HTTP_CODE="$REINDEX_BODY"
REINDEX_RESP=$(cat /tmp/phase-f-launch-body.txt 2>/dev/null || echo '{}')

case "$HTTP_CODE" in
  201|200) ;;  # OK
  409) log "ERROR: launch failed: http=409 lock_active — pipeline already running"; exit 1 ;;
  401) log "ERROR: launch failed: http=401 unauthorized — check INTERNAL_API_KEY"; exit 1 ;;
  403) log "ERROR: launch failed: http=403 forbidden"; exit 1 ;;
  000) log "ERROR: launch failed: http=000 network/timeout — NestJS reachable?"; exit 1 ;;
  *)   log "ERROR: launch failed: http=$HTTP_CODE — $REINDEX_RESP"; exit 1 ;;
esac

RUN_ID=$(echo "$REINDEX_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('run_id',''))" 2>/dev/null || true)

if [ -z "$RUN_ID" ]; then
  log "ERROR: launch returned $HTTP_CODE but no run_id — $REINDEX_RESP"; exit 1
fi
log "  → reindex queued (run_id=$RUN_ID)"

# Polling jusqu'à done ou failed (max 90 min = 180 × 30s)
POLL_MAX=180
POLL_INTERVAL=30
for i in $(seq 1 $POLL_MAX); do
  sleep $POLL_INTERVAL
  RUN_DETAIL=$(curl -sf \
    -H "X-Internal-Key: $INTERNAL_API_KEY" \
    "http://localhost:3000/api/rag/admin/pipeline/runs/$RUN_ID" 2>/dev/null || echo '{"status":"error"}')
  STATUS=$(echo "$RUN_DETAIL" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('status','unknown'))" 2>/dev/null || echo "error")

  log "  poll #$i → $STATUS"

  case "$STATUS" in
    done|completed)
      # Lire le détail du run pour détecter faux succès (blocked_docs/chunks > 0)
      echo "$RUN_DETAIL" | python3 - <<'PYEOF' 2>/dev/null | while IFS= read -r line; do log "  $line"; done
import sys, json
d = json.load(sys.stdin)
summary = d.get('summary') or {}
errors = summary.get('errors') or []
blocked_docs = summary.get('blocked_docs', 0)
blocked_chunks = summary.get('blocked_chunks', 0)
if errors:
    print(f"WARN: summary.errors = {errors}")
if blocked_docs:
    print(f"WARN: blocked_docs = {blocked_docs}")
if blocked_chunks:
    print(f"WARN: blocked_chunks = {blocked_chunks}")
if not errors and not blocked_docs and not blocked_chunks:
    print("reindex completed cleanly (no errors, no blocked docs)")
PYEOF
      log "  reindex done ✓"
      break ;;
    failed|cancelled|abandoned|error)
      log "ERROR: reindex $STATUS — aborting"; exit 1 ;;
  esac

  if [ $i -eq $POLL_MAX ]; then
    log "ERROR: reindex timed out after $((POLL_MAX * POLL_INTERVAL / 60)) min"; exit 1
  fi
done

# ── Étape 4 : Ingest phase5_enrichment → __rag_knowledge (bloquant si échec) ─
log "[4/4] ingest-oem-enriched-gammes.py"
python3 "$APP_DIR/scripts/rag/ingest-oem-enriched-gammes.py" 2>&1 | tee -a "$LOG"
STEP4_CODE=${PIPESTATUS[0]}
if [ $STEP4_CODE -ne 0 ]; then
  log "ERROR: step 4 (ingest) exited $STEP4_CODE"; exit $STEP4_CODE
fi

log "=== Phase F done ==="
