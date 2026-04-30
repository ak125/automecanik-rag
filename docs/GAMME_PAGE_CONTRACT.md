# Gamme Page Contract (RAG)

> **Version** : `GammeContentContract.v2.0`
> **Statut** : `accepted` (canon ADR-033, vault PR #108 commit `77085ef`)
> **Source canon frontmatter wiki** : [`automecanik-wiki/_meta/schema/frontmatter.schema.json`](https://github.com/ak125/automecanik-wiki/blob/main/_meta/schema/frontmatter.schema.json)

Contrat strict pour la fabrication data des pages `/pieces/:slug` (R1 Router), sans modifier l UI frontend.

## Objectif

Chaque document `source_type=gamme` produit un objet `GammeContentContract.v2.0`
structure et versionne, sans H1 (le H1 reste pilote par la page frontend).

Ce contrat est construit et valide dans le repo RAG, pas dans le proxy/widget frontend.

## Ou c est implemente

- Generation + validation:
  - `app/services/gamme_page_contract.py`
- Injection pendant ingestion/reindex:
  - `scripts/reindex.py`
  - champs ajoutes: `gamme_page_contract`, `gamme_contract_errors`, `gamme_contract_warnings`, `gamme_contract_score`, `gamme_contract_flags`
- Materialisation optionnelle en frontmatter (local):
  - `scripts/ensure_gamme_contracts.py`

## Shape cible (v2.0)

```yaml
id: <string>
pgId: <int>
intro:
  role: <string>           # phrase d'introduction principale
risk: <string>             # niveau de risque associé à la pièce (low/medium/high/critical)
timing: <string>           # quand intervenir (intervalle entretien)
arguments: [<string>]      # arguments d'achat (≥ 1 élément)
howToChoose: <string>      # guide de choix par véhicule

diagnostic_relations:      # NOUVEAU v2.0 (canon ADR-033 §D1) — optionnel mais recommandé
  - symptom_slug: <string>           # FK __diag_symptom.slug (ex: brake_noise_metallic)
    system_slug: <string>            # FK __diag_system.slug (ex: freinage)
    relation_to_part: <enum>         # possible_cause | symptom_amplifier | secondary_effect
    part_role: <string>              # 1 phrase, comment la pièce intervient sur le symptôme
    evidence:
      confidence: <enum>             # low | medium | high
      source_policy: <enum>          # 1_high | 2_medium_concordant | manual_review
      reviewed: <bool>               # défaut false
      diagnostic_safe: <bool>        # défaut false ; flip true uniquement après revue humaine
    sources: [<slug>]                # slugs stables _meta/source-catalog.yaml (≥ 1)

diagnostic:                # CONSERVÉ v2.0 — observations propres à la pièce
  causes: [<string>]                 # causes possibles non couvertes par __diag_symptom
  quick_checks: [<string>]           # vérifications rapides terrain
  # symptoms[] : INTERDIT v2.0 — déplacé vers diagnostic_relations[] top-level

entity_data:               # bloc canon ADR-032 (cohabite avec diagnostic_relations[])
  maintenance:
    educational_advice: <string>     # 1-2 lignes ; obligatoire si gamme liée à kg_nodes.MaintenanceInterval
    related_pages: [<slug>]          # slugs pages liées (gamme | vehicle)

antiMistakes: [<string>]   # erreurs courantes à éviter (≥ 3)
faq:                       # ≥ 3 entrées
  - question: <string>
    answer: <string>

quality:
  score: <number>          # 0-1
  flags: [<string>]
  version: GammeContentContract.v2.0
  source: <string>
```

## Rupture v1 → v2.0 (breaking)

| Champ | v1 | v2.0 | Migration |
|---|---|---|---|
| `symptoms[]` (top-level) | obligatoire ≥ 3 | **interdit** | déplacé vers `diagnostic_relations[]` (canon ADR-033 §D1) |
| `diagnostic_relations[]` | absent | **ajouté** (optionnel mais recommandé) | nouvelle structure FK stricte vers `__diag_symptom.slug` / `__diag_system.slug` |
| `entity_data.maintenance.{educational_advice, related_pages}` | absent | **ajouté** (canon ADR-032 §D1) | obligatoire si gamme matche un `kg_nodes.MaintenanceInterval` |
| `diagnostic.causes[]` + `diagnostic.quick_checks[]` | optionnel | **conservé** | observations propres à la pièce, non couvertes par `__diag_symptom` |
| `quality.version` | `GammeContentContract.v1` | `GammeContentContract.v2.0` | bump explicite |

**Cohabitation runtime** : pendant la migration progressive (Phase 4 ADR-033), les fiches `v1` restent valides en lecture par `app/services/gamme_page_contract.py`. Le validateur strict v2.0 s'applique uniquement aux fiches qui déclarent `quality.version: GammeContentContract.v2.0`. Les fiches non encore migrées conservent `quality.version: GammeContentContract.v1` et peuvent contenir `symptoms[]` jusqu'à leur migration unitaire (script `scripts/wiki/migrate-symptoms-to-relations.ts` côté monorepo, batch `--per-system`).

**Big-bang du flip v2** : quand `grep -rn "symptoms:" wiki/gammes/*.md` retourne 0, le code Python `gamme_page_contract.py` peut être bumpé strict v2 et le bloc `symptoms[]` peut être retiré du shape (PR séparée Partie 3).

## Anti-patterns figés (canon ADR-033 §D3)

1. ❌ Création de `wiki/systemes/<slug>.md` ou de tout `entity_type: system` — la DB `__diag_system` est SoT.
2. ❌ Création d'un fichier-par-symptôme `wiki/diagnostic/<symptom>-*.md` — frontend Remix sert `/diagnostic-auto/symptome/$slug`.
3. ❌ Réécriture du moteur diagnostic (DB `__diag_*`, RPCs, backend, frontend) — hors scope ADR-033.

## Regles QA

- Version obligatoire (par fiche) : `GammeContentContract.v1` OU `GammeContentContract.v2.0` (cohabitation jusqu'à migration complète Phase 4 ADR-033).
- Seuil minimum :
  - `intro.role` non vide et exploitable
  - `antiMistakes >= 3`
  - `faq >= 3`
  - **v1 seul** : `symptoms >= 3` (legacy, deprecated)
  - **v2.0** : `diagnostic_relations` non requis (optionnel mais recommandé). Si présent, chaque entrée doit pointer un `symptom_slug` existant dans `__diag_symptom.slug` (validé par export JSON nightly `exports/diag-canon-slugs.json` côté wiki).
  - **v2.0** : `sources[]` de chaque `diagnostic_relations[]` doit pointer un slug présent dans `_meta/source-catalog.yaml` côté wiki.
- Fallback automatique par section (jamais global) : seules les sections KO sont remplacees.
- Flags QA standard :
  - `GENERIC_PHRASES`
  - `MISSING_REQUIRED_TERMS`
  - `TOO_SHORT`
  - `TOO_LONG`
  - `FAQ_TOO_SMALL`
  - `SYMPTOMS_TOO_SMALL` (legacy v1)
  - `DIAGNOSTIC_RELATIONS_FK_BROKEN` (NEW v2.0)
  - `LEGACY_SYMPTOMS_BLOCK` (NEW v2.0 — fiche déclare `quality.version: v2.0` mais contient encore `symptoms[]`)
  - `MAINTENANCE_ADVICE_MISSING` (NEW v2.0 — gamme matche `kg_nodes.MaintenanceInterval` sans `entity_data.maintenance.educational_advice`)
  - `DUPLICATE_ITEMS`

## Sources canon downstream

Le shape v2.0 est dérivé du frontmatter wiki canon :

- `automecanik-wiki/_meta/schema/frontmatter.schema.json` v2.0.0 (Draft 2020-12) — schema strict, validateur Python `_scripts/quality-gates.py` 9 gates ADR-033/032 actifs (PR wiki #8 mergée 2026-04-30 commit `989cb0cc`).
- `automecanik-wiki/_meta/templates/gamme.md` — template canonique v2.0.0 avec exemple `diagnostic_relations[]` complet.
- `automecanik-wiki/_meta/source-catalog.yaml` — registre slugs sources stables (PR wiki #9 mergée 2026-04-30 commit `ee5ee3c4`).

## Commandes utiles

Verifier le contrat (sans ecriture, mode cohabitation v1+v2.0):

```bash
python3 scripts/ensure_gamme_contracts.py --path knowledge --strict-exit
```

Appliquer dans les frontmatters (optionnel, volumineux):

```bash
python3 scripts/ensure_gamme_contracts.py --path knowledge --strict-exit --apply
```

Migrer une fiche v1 → v2.0 (côté monorepo, scope `automecanik-wiki/wiki/gammes/`):

```bash
# Depuis le repo nestjs-remix-monorepo (script à livrer Phase 4 ADR-033 PR-E)
npm run wiki:migrate -- --status                          # dashboard
npm run wiki:migrate -- --dry-run --per-system freinage   # diff sans écriture
npm run wiki:migrate -- --apply --per-system freinage     # batch unitaire par système
```

Verification syntaxe:

```bash
python3 -m py_compile app/services/gamme_page_contract.py scripts/reindex.py scripts/ensure_gamme_contracts.py tests/test_gamme_page_contract.py
```

## Note d architecture

- `proxy` et `widget` restent cote monorepo applicatif.
- La fabrication des donnees SEO reste cote RAG (contrat versionne + QA).
- Ne pas toucher l UI tant que le contrat data n est pas valide.
- Le validateur frontmatter wiki (Python `quality-gates.py` côté wiki, TypeScript `validate-gamme-diagnostic-relations.ts` côté monorepo PR-C ADR-033) vérifie strictement v2.0 sur les fiches qui le déclarent. Les fiches v1 passent en mode permissif jusqu'à leur migration.

## References

- ADR-033 (vault, status `accepted` 2026-04-29, PR #108 commit `77085ef`) : `governance-vault/ledger/decisions/adr/ADR-033-wiki-gamme-diagnostic-relations-contract.md`
- ADR-032 (vault) : maintenance/safety/DTC canon kg_*, blocs `entity_data.maintenance{}` cohabitent avec `diagnostic_relations[]`
- ADR-031 (vault) : 4-layer raw/wiki/exports/consumers — ce contrat = layer `exports/` (consommateurs Partie 3 ADR-031)
- canon frontmatter wiki : `automecanik-wiki/_meta/schema/frontmatter.schema.json` v2.0.0 (PR wiki #8/#9)
