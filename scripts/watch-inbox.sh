#!/usr/bin/env bash
# =============================================================================
# watch-inbox.sh — Watcher inotifywait pour le pipeline RAG
# =============================================================================
# Surveille /opt/automecanik/rag/pdfs/inbox/ et lance le pipeline
# automatiquement quand un PDF arrive (close_write).
#
# Geré par systemd: rag-watcher.service
# Manuel: ./watch-inbox.sh
# =============================================================================
set -euo pipefail

# Charger variables d'environnement
source /opt/automecanik/rag/scripts/load-env.sh

INBOX="/opt/automecanik/rag/pdfs/inbox"
LOG="/opt/automecanik/rag/logs/watcher.log"

mkdir -p "$(dirname "$LOG")"

log() { echo "[$(date -Is)] $*" | tee -a "$LOG"; }

log "Watcher started — monitoring $INBOX for new PDFs"

# inotifywait: surveille les fichiers ecrits completement (close_write)
# --include filtre sur .pdf/.PDF uniquement
inotifywait -m -e close_write --include '\.[pP][dD][fF]$' "$INBOX" |
while read -r dir event file; do
  log "Detected: $file ($event)"
  # Petit delai pour s'assurer que le fichier est complet (rsync, scp...)
  sleep 5
  log "Launching pipeline for $file"
  /opt/automecanik/rag/scripts/pipeline/auto-enrich-pipeline.sh 2>&1 | tee -a "$LOG" || true
  log "Pipeline finished for $file"
done
