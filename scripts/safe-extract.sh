#!/bin/bash
# =============================================================================
# safe-extract.sh - Extraction securisee fichier par fichier depuis MinIO
# =============================================================================
# Usage: ./safe-extract.sh <pattern> [callback_script]
# Exemple: ./safe-extract.sh "100.*.sql" ./process-sql.sh
#
# IMPORTANT: Ne JAMAIS extraire l'archive complete (113 GB > 102 GB dispo)
# =============================================================================

set -euo pipefail

MINIO_CONTAINER="automecanik-minio"
BUCKET="catalog-raw"
ARCHIVE="SQL-CONVERTED.7z"
WORK_DIR="/tmp/taf24-current"
MIN_FREE_DISK_MB=20000  # 20 GB minimum
MIN_FREE_RAM_MB=2000    # 2 GB minimum

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# =============================================================================
# Verification ressources AVANT chaque operation
# =============================================================================
check_resources() {
  local free_mem=$(free -m | awk '/Mem:/ {print $7}')
  local free_disk=$(df -m /tmp | awk 'NR==2 {print $4}')

  if [ "$free_mem" -lt "$MIN_FREE_RAM_MB" ]; then
    log_error "RAM insuffisante: ${free_mem}MB < ${MIN_FREE_RAM_MB}MB"
    return 1
  fi

  if [ "$free_disk" -lt "$MIN_FREE_DISK_MB" ]; then
    log_error "Disque insuffisant: ${free_disk}MB < ${MIN_FREE_DISK_MB}MB"
    return 1
  fi

  log_info "Ressources OK: ${free_mem}MB RAM, ${free_disk}MB disque"
  return 0
}

# =============================================================================
# Telecharger archive depuis MinIO (si pas en cache local)
# =============================================================================
ensure_archive_local() {
  local local_archive="/tmp/${ARCHIVE}"

  if [ -f "$local_archive" ]; then
    log_info "Archive deja en cache: $local_archive"
    echo "$local_archive"
    return 0
  fi

  log_info "Telechargement archive depuis MinIO..."
  docker run --rm --network rag_rag-network \
    --entrypoint /bin/sh \
    -v /tmp:/data \
    minio/mc -c "
      mc alias set myminio http://${MINIO_CONTAINER}:9000 automecanik \$MINIO_ROOT_PASSWORD >/dev/null 2>&1
      mc cp myminio/${BUCKET}/${ARCHIVE} /data/${ARCHIVE}
    "

  echo "$local_archive"
}

# =============================================================================
# Lister fichiers dans l'archive correspondant au pattern
# =============================================================================
list_files() {
  local archive="$1"
  local pattern="${2:-*}"

  7z l "$archive" | grep -E "^[0-9]{4}-" | awk '{print $NF}' | grep -E "$pattern" || true
}

# =============================================================================
# Extraire UN fichier, traiter, supprimer
# =============================================================================
extract_and_process() {
  local archive="$1"
  local filename="$2"
  local callback="${3:-}"

  # Verifier ressources avant extraction
  if ! check_resources; then
    log_error "Ressources insuffisantes, arret"
    return 1
  fi

  # Creer dossier de travail
  mkdir -p "$WORK_DIR"

  # Extraire UN SEUL fichier
  log_info "Extraction: $filename"
  7z e -mmt1 "$archive" "$filename" -o"$WORK_DIR" -y >/dev/null

  local extracted_file="$WORK_DIR/$filename"

  if [ ! -f "$extracted_file" ]; then
    log_warn "Fichier non trouve apres extraction: $filename"
    return 1
  fi

  local file_size=$(du -h "$extracted_file" | cut -f1)
  log_info "Extrait: $filename ($file_size)"

  # Appeler callback si fourni
  if [ -n "$callback" ] && [ -x "$callback" ]; then
    log_info "Traitement: $callback $extracted_file"
    "$callback" "$extracted_file"
  fi

  # TOUJOURS supprimer apres traitement
  rm -f "$extracted_file"
  log_info "Nettoyage: $filename supprime"

  return 0
}

# =============================================================================
# Traitement batch avec pattern
# =============================================================================
process_pattern() {
  local pattern="$1"
  local callback="${2:-}"

  log_info "=== Extraction securisee: pattern '$pattern' ==="

  # Verifier ressources initiales
  if ! check_resources; then
    log_error "Ressources insuffisantes pour demarrer"
    exit 1
  fi

  # Obtenir archive locale
  local archive=$(ensure_archive_local)

  # Lister fichiers correspondants
  local files=$(list_files "$archive" "$pattern")
  local count=$(echo "$files" | grep -c . || echo 0)

  log_info "Fichiers trouves: $count"

  if [ "$count" -eq 0 ]; then
    log_warn "Aucun fichier correspondant au pattern: $pattern"
    return 0
  fi

  # Traiter fichier par fichier
  local processed=0
  local failed=0

  echo "$files" | while read -r filename; do
    if [ -z "$filename" ]; then continue; fi

    if extract_and_process "$archive" "$filename" "$callback"; then
      ((processed++)) || true
    else
      ((failed++)) || true
    fi

    # Pause entre fichiers pour eviter surcharge
    sleep 1
  done

  log_info "=== Termine: $processed traites, $failed echecs ==="
}

# =============================================================================
# Main
# =============================================================================
main() {
  local pattern="${1:-}"
  local callback="${2:-}"

  if [ -z "$pattern" ]; then
    echo "Usage: $0 <pattern> [callback_script]"
    echo ""
    echo "Exemples:"
    echo "  $0 '100\\..*\\.sql'           # Fabricants"
    echo "  $0 '030\\..*\\.sql'           # Langues"
    echo "  $0 '120\\.0001\\.sql' ./process.sh  # Un seul fichier avec callback"
    echo ""
    echo "Tables prioritaires (petites):"
    echo "  100.* - Fabricants (~100 KB)"
    echo "  030.* - Langues (~500 KB)"
    echo "  110.* - Modeles (~5 MB)"
    echo "  120.* - Types vehicules (~50 MB)"
    echo ""
    echo "Tables volumineuses (ATTENTION):"
    echo "  200.* - Articles (~10 GB)"
    echo "  400.* - Liaisons (~50 GB)"
    exit 1
  fi

  process_pattern "$pattern" "$callback"
}

main "$@"
