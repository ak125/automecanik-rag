#!/bin/bash
# rag-query.sh - Wrapper Claude CLI + RAG AutoMecanik
# Usage: ./rag-query.sh "Votre question"

set -e

# Configuration
RAG_URL="${RAG_URL:-http://localhost:8000}"
RAG_API_KEY="${RAG_API_KEY:-automecanik-rag-dev-2026}"
LIMIT="${RAG_LIMIT:-5}"

# Couleurs pour l'affichage
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Fonction d'aide
show_help() {
    echo "Usage: $0 [OPTIONS] \"Votre question\""
    echo ""
    echo "Options:"
    echo "  -l, --limit N     Nombre de sources (défaut: 5)"
    echo "  -r, --raw         Afficher le JSON brut du RAG"
    echo "  -c, --context     Afficher uniquement le contexte (sans Claude)"
    echo "  -h, --help        Afficher cette aide"
    echo ""
    echo "Exemples:"
    echo "  $0 \"Diagnostic bruit de freinage\""
    echo "  $0 -l 3 \"Politique de retour\""
    echo "  $0 --context \"Comment choisir des plaquettes\""
}

# Parse arguments
RAW_MODE=false
CONTEXT_ONLY=false
QUERY=""

while [[ $# -gt 0 ]]; do
    case $1 in
        -l|--limit)
            LIMIT="$2"
            shift 2
            ;;
        -r|--raw)
            RAW_MODE=true
            shift
            ;;
        -c|--context)
            CONTEXT_ONLY=true
            shift
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            QUERY="$1"
            shift
            ;;
    esac
done

# Vérifier que la question est fournie
if [ -z "$QUERY" ]; then
    echo -e "${RED}Erreur: Question manquante${NC}"
    show_help
    exit 1
fi

# Vérifier que le RAG est accessible
if ! curl -s "$RAG_URL/health" > /dev/null 2>&1; then
    echo -e "${RED}Erreur: RAG non accessible sur $RAG_URL${NC}"
    echo "Vérifiez que le service RAG est démarré:"
    echo "  cd /opt/automecanik/rag && docker compose up -d"
    exit 1
fi

echo -e "${BLUE}=== RAG AutoMecanik ===${NC}"
echo -e "${YELLOW}Question:${NC} $QUERY"
echo ""

# 1. Recherche dans le RAG
echo -e "${BLUE}Recherche dans le corpus...${NC}"
RAG_RESPONSE=$(curl -s -X POST "$RAG_URL/chat" \
    -H "Content-Type: application/json" \
    -H "X-RAG-API-Key: $RAG_API_KEY" \
    -d "{\"message\": \"$QUERY\", \"limit\": $LIMIT}")

# Vérifier si la réponse est valide
if [ -z "$RAG_RESPONSE" ] || echo "$RAG_RESPONSE" | grep -q "detail"; then
    echo -e "${RED}Erreur RAG:${NC} $RAG_RESPONSE"
    exit 1
fi

# Mode raw: afficher le JSON brut
if [ "$RAW_MODE" = true ]; then
    echo "$RAG_RESPONSE" | python3 -m json.tool
    exit 0
fi

# Extraire les informations
CONTEXT=$(echo "$RAG_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('context', ''))" 2>/dev/null)
SOURCES=$(echo "$RAG_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print('\n'.join(data.get('sources', [])))" 2>/dev/null)
TOTAL=$(echo "$RAG_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('total_sources', 0))" 2>/dev/null)
CONFIDENCE=$(echo "$RAG_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(int(data.get('truth_metadata', {}).get('composite_confidence', 0.5) * 100))" 2>/dev/null)
DOMINANT=$(echo "$RAG_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('truth_metadata', {}).get('dominant_level', 'L3'))" 2>/dev/null)

echo -e "${GREEN}Sources trouvées:${NC} $TOTAL (Confiance: ${CONFIDENCE}%, Niveau: $DOMINANT)"
echo ""

# Mode context-only: afficher le contexte sans appeler Claude
if [ "$CONTEXT_ONLY" = true ]; then
    echo -e "${YELLOW}=== CONTEXTE RAG ===${NC}"
    echo "$CONTEXT"
    echo ""
    echo -e "${YELLOW}=== SOURCES ===${NC}"
    echo "$SOURCES"
    exit 0
fi

# 2. Passer le contexte à Claude CLI
echo -e "${BLUE}Interrogation de Claude CLI...${NC}"
echo ""

# Construire le prompt pour Claude
CLAUDE_PROMPT="Tu es un assistant spécialisé en pièces automobiles pour AutoMecanik.

CONTEXTE (provenant de notre base de connaissances RAG):
$CONTEXT

QUESTION DU CLIENT:
$QUERY

INSTRUCTIONS:
- Réponds de manière claire et concise
- Utilise les informations du contexte RAG
- Si le contexte ne contient pas la réponse, dis-le clairement
- Niveau de confiance des sources: ${CONFIDENCE}% (${DOMINANT})"

# Appeler Claude CLI
echo "$CLAUDE_PROMPT" | claude --dangerously-skip-permissions -p "Réponds à la question du client en utilisant le contexte fourni."

echo ""
echo -e "${YELLOW}Sources utilisées:${NC}"
echo "$SOURCES" | while read -r source; do
    [ -n "$source" ] && echo "  - $source"
done
