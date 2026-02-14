# Gamme Page Contract (RAG)

Contrat strict pour la fabrication data des pages `/pieces/:slug` (R1 Router), sans modifier l UI frontend.

## Objectif

Chaque document `source_type=gamme` produit un objet `GammeContentContract.v1`
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

## Shape cible

- `id`
- `pgId`
- `intro`
- `risk`
- `timing`
- `arguments[]`
- `howToChoose`
- `symptoms[]`
- `antiMistakes[]`
- `faq[]`
- `quality`:
  - `score`
  - `flags`
  - `version` (`GammeContentContract.v1`)
  - `source`

## Regles QA

- Version obligatoire: `GammeContentContract.v1`
- Seuil minimum:
  - `intro.role` non vide et exploitable
  - `symptoms >= 3`
  - `antiMistakes >= 3`
  - `faq >= 3`
- Fallback automatique par section (jamais global): seules les sections KO sont remplacees
- Flags QA standard:
  - `GENERIC_PHRASES`
  - `MISSING_REQUIRED_TERMS`
  - `TOO_SHORT`
  - `TOO_LONG`
  - `FAQ_TOO_SMALL`
  - `SYMPTOMS_TOO_SMALL`
  - `DUPLICATE_ITEMS`

## Commandes utiles

Verifier le contrat (sans ecriture):

```bash
python3 scripts/ensure_gamme_contracts.py --path knowledge --strict-exit
```

Appliquer dans les frontmatters (optionnel, volumineux):

```bash
python3 scripts/ensure_gamme_contracts.py --path knowledge --strict-exit --apply
```

Verification syntaxe:

```bash
python3 -m py_compile app/services/gamme_page_contract.py scripts/reindex.py scripts/ensure_gamme_contracts.py tests/test_gamme_page_contract.py
```

## Note d architecture

- `proxy` et `widget` restent cote monorepo applicatif.
- La fabrication des donnees SEO reste cote RAG (contrat versionne + QA).
- Ne pas toucher l UI tant que le contrat data n est pas valide.
