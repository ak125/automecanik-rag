#!/usr/bin/env bash
# =============================================================================
# auto-enrich-pipeline.sh — Pipeline RAG Auto-Enrichissement
# =============================================================================
# Drop PDF → Ingestion → Indexation → Détection catégorie → Enrichissement
#
# Usage:
#   ./auto-enrich-pipeline.sh              # Production (dryRun=false)
#   DRY_RUN=true ./auto-enrich-pipeline.sh # Preview mode
#
# Cron (every 30 min):
#   */30 * * * * /opt/automecanik/rag/scripts/auto-enrich-pipeline.sh
# =============================================================================
set -euo pipefail

# --- Config ---
RAG_URL="${RAG_SERVICE_URL:-http://localhost:8000}"
RAG_API_KEY="${RAG_API_KEY:-}"
NESTJS_URL="${NESTJS_URL:-http://localhost:3000}"
INTERNAL_KEY="${INTERNAL_API_KEY:-}"
DRY_RUN="${DRY_RUN:-false}"

BASE_DIR="/opt/automecanik/rag"
INBOX_DIR="$BASE_DIR/pdfs/inbox"
PROCESSED_DIR="$BASE_DIR/pdfs/processed"
FAILED_DIR="$BASE_DIR/pdfs/failed"
KNOWLEDGE_DIR="$BASE_DIR/knowledge"
CATEGORY_MAP="$BASE_DIR/config/category-gamme-map.json"
LOG_FILE="$BASE_DIR/logs/auto-enrich.log"
LOCK_FILE="/tmp/auto-enrich-pipeline.lock"
MANIFEST="$PROCESSED_DIR/.manifest"

# Max poll time for ingestion (30 min = 60 iterations * 30s)
MAX_POLL_ITERATIONS=120
POLL_INTERVAL=30

# --- Ensure dirs exist ---
mkdir -p "$INBOX_DIR" "$PROCESSED_DIR" "$FAILED_DIR" "$BASE_DIR/logs"

# --- Global lock (prevent concurrent RAG operations) ---
GLOBAL_LOCK="/tmp/rag-global.lock"
exec 8>"$GLOBAL_LOCK"
if ! flock -n 8; then
  echo "[$(date -Is)] Another RAG operation active (global lock), skipping" >> "$LOG_FILE"
  exit 0
fi

# --- Local lock (prevent concurrent pipeline runs) ---
exec 9>"$LOCK_FILE"
if ! flock -n 9; then
  echo "[$(date -Is)] Another pipeline run active, skipping" >> "$LOG_FILE"
  exit 0
fi

# --- Logging ---
log() {
  echo "[$(date -Is)] $*" | tee -a "$LOG_FILE"
}

# --- Utilities ---
sha256() {
  sha256sum "$1" | cut -d' ' -f1
}

# --- Health checks ---
check_health() {
  local rag_ok nestjs_ok
  rag_ok=$(curl -sf -o /dev/null -w "%{http_code}" "$RAG_URL/health" 2>/dev/null || echo "000")
  nestjs_ok=$(curl -sf -o /dev/null -w "%{http_code}" "$NESTJS_URL/health" 2>/dev/null || echo "000")

  if [ "$rag_ok" != "200" ]; then
    log "ERROR: RAG service not responding ($RAG_URL/health → $rag_ok)"
    return 1
  fi
  if [ "$nestjs_ok" != "200" ]; then
    log "ERROR: NestJS not responding ($NESTJS_URL/health → $nestjs_ok)"
    return 1
  fi
  return 0
}

# --- Step 1: Ingest PDF ---
LAST_JOB_ID=""
RAG_CONTAINER="${RAG_CONTAINER_NAME:-rag-api-prod}"

ingest_pdf() {
  local pdf="$1"
  local run_id response job_id status
  LAST_JOB_ID=""

  run_id="$(date +%s)-$(head -c4 /dev/urandom | xxd -p)"

  # Stage PDF in a temp directory for the RAG service
  local staging_dir="$BASE_DIR/pdfs/_staging/$run_id"
  mkdir -p "$staging_dir"
  cp "$pdf" "$staging_dir/"

  # Trigger ingestion via RAG API
  response=$(curl -sf -X POST "$RAG_URL/admin/ingest/pdf/run" \
    -H "Content-Type: application/json" \
    -H "X-RAG-API-Key: $RAG_API_KEY" \
    -d "{\"input_dir\":\"/app/pdfs/_staging/$run_id\",\"truth_level\":\"L2\"}" 2>/dev/null) || {
    log "  WARN: Ingestion API call failed"
    rm -rf "$staging_dir"
    return 1
  }

  job_id=$(echo "$response" | jq -r '.job_id // empty' 2>/dev/null)
  if [ -z "$job_id" ]; then
    log "  WARN: No job_id returned from ingestion"
    rm -rf "$staging_dir"
    return 1
  fi

  log "  Ingestion job started: $job_id"

  # Poll until done
  for i in $(seq 1 "$MAX_POLL_ITERATIONS"); do
    sleep "$POLL_INTERVAL"
    status=$(curl -sf "$RAG_URL/admin/ingest/pdf/jobs/$job_id" \
      -H "X-RAG-API-Key: $RAG_API_KEY" 2>/dev/null | jq -r '.status // "unknown"' 2>/dev/null) || status="error"

    case "$status" in
      completed|done)
        log "  Ingestion completed (poll #$i)"
        LAST_JOB_ID="$job_id"
        rm -rf "$staging_dir"
        return 0
        ;;
      failed|error)
        log "  Ingestion failed at poll #$i (status=$status)"
        rm -rf "$staging_dir"
        return 1
        ;;
      *)
        # still running (processing, queued, etc.)
        ;;
    esac
  done

  log "  Ingestion timed out after $((MAX_POLL_ITERATIONS * POLL_INTERVAL))s"
  rm -rf "$staging_dir"
  return 1
}

# --- Step 2: Detect category from ingested content ---
detect_category() {
  local pdf="$1"
  local category

  # Strategy 1: Read frontmatter from Docker container (most reliable)
  # The RAG service writes markdown to /tmp/knowledge-import/{job_id}/ inside the container
  if [ -n "$LAST_JOB_ID" ]; then
    category=$(docker exec "$RAG_CONTAINER" find "/tmp/knowledge-import/$LAST_JOB_ID" \
      -name '*.md' -type f -exec grep -m1 '^category:' {} \; 2>/dev/null \
      | head -1 \
      | sed 's/category:\s*//' | tr -d '"' | tr -d "'" \
      | tr '[:upper:]' '[:lower:]' | tr ' ' '_')

    if [ -n "$category" ]; then
      echo "$category"
      return
    fi
  fi

  # Strategy 2: Fallback — keyword detection from PDF filename
  local filename
  filename=$(basename "$pdf" .pdf | tr '[:upper:]' '[:lower:]')

  declare -A keyword_map=(
    ["brake|frein|disque|plaquette|etrier"]="freinage"
    ["filtre|filter|filtration"]="filtres"
    ["courroie|galet|poulie|chaine|distribution"]="courroie_galet_poulie_chaine"
    ["bougie|allumage|prechauffage"]="prechauffage_allumage"
    ["direction|rotule|bras.*suspension|biellette"]="direction_liaison_sol"
    ["amortisseur|ressort.*suspension"]="amortisseur_suspension"
    ["support.*moteur"]="support_moteur"
    ["embrayage|clutch"]="embrayage"
    ["transmission|cardan|roulement"]="transmission"
    ["alternateur|demarreur|batterie"]="systeme_electrique"
    ["capteur|sensor|sonde"]="capteurs"
    ["injection|injecteur|pompe.*carburant|egr"]="systeme_alimentation"
    ["joint.*culasse|carter|soupape|culbuteur"]="moteur"
    ["refroidissement|radiateur|thermostat"]="refroidissement"
    ["climatisation|compresseur.*clim|condenseur"]="climatisation"
    ["echappement|silencieux|catalyseur|fap"]="echappement"
    ["phare|feu|clignotant|eclairage"]="eclairage"
    ["turbo|suralimentation|intercooler"]="turbo"
  )

  for pattern in "${!keyword_map[@]}"; do
    if echo "$filename" | grep -qEi "$pattern"; then
      echo "${keyword_map[$pattern]}"
      return
    fi
  done

  echo "unknown"
}

# --- Step 3: Get pg_ids for a category ---
get_pg_ids() {
  local category="$1"
  # Read from mapping JSON, skip _meta key
  jq -r ".[\"$category\"] // [] | .[] | tostring" "$CATEGORY_MAP" 2>/dev/null
}

# --- Step 4: Enrich gammes via NestJS internal API ---
enrich_gammes() {
  local pg_ids_json="$1"
  local dry_flag="$DRY_RUN"

  local response http_code
  response=$(curl -sf -w "\n%{http_code}" -X POST "$NESTJS_URL/api/internal/buying-guides/enrich" \
    -H "Content-Type: application/json" \
    -H "X-Internal-Key: $INTERNAL_KEY" \
    -d "{\"pgIds\":$pg_ids_json,\"dryRun\":$dry_flag}" 2>/dev/null) || {
    log "  WARN: Enrichment API call failed"
    return 1
  }

  http_code=$(echo "$response" | tail -1)
  local body
  body=$(echo "$response" | sed '$d')

  if [ "$http_code" = "200" ] || [ "$http_code" = "201" ]; then
    local enriched_count
    enriched_count=$(echo "$body" | jq '.results | length' 2>/dev/null || echo "?")
    log "  Enrichment OK: $enriched_count gammes processed (dryRun=$dry_flag)"
    return 0
  else
    log "  WARN: Enrichment returned HTTP $http_code"
    return 1
  fi
}

# =============================================================================
# MAIN
# =============================================================================
log "========================================="
log "Pipeline start (DRY_RUN=$DRY_RUN)"

# Validate config
if [ -z "$INTERNAL_KEY" ]; then
  log "ERROR: INTERNAL_API_KEY not set"
  exit 1
fi

if [ ! -f "$CATEGORY_MAP" ]; then
  log "ERROR: Category map not found: $CATEGORY_MAP"
  exit 1
fi

# Health check
check_health || { log "Aborting: services unavailable"; exit 1; }

# Scan inbox
shopt -s nullglob
pdfs=("$INBOX_DIR"/*.pdf "$INBOX_DIR"/*.PDF)
shopt -u nullglob

if [ ${#pdfs[@]} -eq 0 ]; then
  log "No PDFs in inbox"
  exit 0
fi

log "Found ${#pdfs[@]} PDF(s) in inbox"

# Create manifest if missing
touch "$MANIFEST"

# Process each PDF
success_count=0
fail_count=0

for pdf in "${pdfs[@]}"; do
  filename=$(basename "$pdf")
  hash=$(sha256 "$pdf")
  stamp=$(date +%Y%m%d_%H%M%S)

  # Idempotency: skip already-processed files
  if grep -q "$hash" "$MANIFEST" 2>/dev/null; then
    log "SKIP $filename (already processed: $hash)"
    rm -f "$pdf"
    continue
  fi

  log "PROCESSING $filename ($hash)"

  # Step 1: Ingest
  if ingest_pdf "$pdf"; then
    log "  [1/3] Ingestion OK"

    # Step 2: Detect category
    category=$(detect_category "$pdf")
    log "  [2/3] Category detected: $category"

    # Step 3: Get pg_ids and enrich
    pg_ids=$(get_pg_ids "$category")
    if [ -n "$pg_ids" ]; then
      pg_ids_json=$(echo "$pg_ids" | jq -R . | jq -s .)
      pg_count=$(echo "$pg_ids_json" | jq 'length')
      log "  [3/3] Enriching $pg_count gammes: $(echo "$pg_ids_json" | jq -c .)"

      if enrich_gammes "$pg_ids_json"; then
        log "  SUCCESS"
      else
        log "  PARTIAL: ingestion OK but enrichment failed"
      fi
    else
      log "  WARN: no gammes mapped for category '$category' — skipping enrichment"
    fi

    # Archive to processed
    mv "$pdf" "$PROCESSED_DIR/${stamp}_${filename}"
    echo "$hash $stamp $filename $category" >> "$MANIFEST"
    ((success_count++)) || true
    log "  Archived → processed/${stamp}_${filename}"
  else
    log "  FAILED: ingestion error"
    mv "$pdf" "$FAILED_DIR/${stamp}_${filename}"
    ((fail_count++)) || true
  fi

  log "---"
done

log "Pipeline complete: ${#pdfs[@]} scanned, $success_count OK, $fail_count failed"
log "========================================="
