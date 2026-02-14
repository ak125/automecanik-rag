#!/usr/bin/env bash
# Charge les variables .env dans l'environnement courant
# Usage: source /opt/automecanik/rag/scripts/load-env.sh
set -a
source <(grep -v '^#' /opt/automecanik/app/backend/.env | grep -v '^\s*$')
set +a
