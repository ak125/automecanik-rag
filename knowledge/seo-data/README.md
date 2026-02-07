# SEO Data - RAG Knowledge

Données SEO pour le corpus RAG AutoMecanik.

## Fichiers

| Fichier | Description | Source |
|---------|-------------|--------|
| `gammes_keywords.csv` | Mots-clés SEO par gamme de pièces | Google Ads / SEMrush |
| `gammes_seo_expert.csv` | Données SEO enrichies (expert) | Analyse interne |
| `gammes_search_volumes.csv` | Volumes de recherche par gamme | Google Ads API |
| `gammes_with_trends.csv` | Tendances de recherche | Google Trends |
| `gammes_editable.csv` | Gammes éditables (meta) | Admin SEO |

## Sous-dossiers

### google-ads/
Exports bruts Google Ads (Keyword Stats).

## Usage RAG

Ces fichiers sont accessibles pour :
- Enrichissement des réponses Claude sur les pièces auto
- Génération de contenu SEO
- Analyse de tendances

## Migration

Migré depuis `backend/*.csv` le 2026-02-02 (Phase P2.3).
Voir [DEC-001-hardening-dev-preprod-prod](../../../governance-vault/02-decisions/DEC-001-hardening-dev-preprod-prod.md)
