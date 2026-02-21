#!/usr/bin/env bash
set -euo pipefail

# Starter pack for common auto-parts schemas.
# It runs a set of fact queries and skips the ones that don't match your DB.
#
# Usage:
#   DB_URL='postgresql://user:pass@host:5432/db' ./scripts/import_and_index_db_starter.sh
#   DB_URL='postgresql://...' ./scripts/import_and_index_db_starter.sh supabase 300

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROVIDER="${1:-supabase}"
LIMIT="${2:-200}"

if [[ -z "${DB_URL:-}" ]]; then
  echo "ERROR: DB_URL env var is required"
  exit 1
fi

cd "$ROOT_DIR"

./scripts/importers/import_and_index_db.sh \
  --provider "$PROVIDER" \
  --schema-truth-level L2 \
  --facts-truth-level L3 \
  --skip-query-errors \
  --fact-query "pieces::id::SELECT id, sku, reference, marque, prix, gamme_id FROM pieces LIMIT $LIMIT" \
  --fact-query "products::id::SELECT id, sku, brand, price, category_id FROM products LIMIT $LIMIT" \
  --fact-query "compatibilites::id::SELECT id, piece_id, vehicule_id, moteur, annee_debut, annee_fin FROM compatibilites LIMIT $LIMIT" \
  --fact-query "compatibility::id::SELECT id, product_id, vehicle_id, engine, year_from, year_to FROM compatibility LIMIT $LIMIT" \
  --fact-query "gammes::id::SELECT id, code, nom, description FROM gammes LIMIT $LIMIT" \
  --fact-query "ranges::id::SELECT id, code, name, description FROM ranges LIMIT $LIMIT" \
  --fact-query "piece_attributs::id::SELECT id, piece_id, attr_key, attr_value FROM piece_attributs LIMIT $LIMIT" \
  --fact-query "product_attributes::id::SELECT id, product_id, attr_key, attr_value FROM product_attributes LIMIT $LIMIT" \
  --fact-query "fitment::id::SELECT id, product_id, vehicle_id, engine_code FROM fitment LIMIT $LIMIT"

echo "Starter pack completed."
