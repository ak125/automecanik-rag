---
category: editorial
created_at: 2026-02-15
doc_family: knowledge
doc_kind: contract
entity_scope: system
id: buying_guide__contract__v1
lang: fr
source_type: canonical
title: BuyingGuideContract v1 — Framework editorial guides d'achat
truth_level: L1
updated_at: 2026-02-15
verification_status: verified
doc_id: c14dd2ce-2c4d-584f-a7fa-b389a8da5a0f
content_hash: sha256:a3bd665667a242a4
---


# BuyingGuideContract v1

Ce document definit le framework editorial que chaque guide d'achat gamme doit respecter.
Table : `__seo_gamme_purchase_guide`, cle : `sgpg_pg_id`.

## Sections obligatoires

### 1. Intro (sgpg_intro_*)

| Champ | Type | Regle |
|-------|------|-------|
| `intro_title` | string | Nom de la gamme au pluriel |
| `intro_role` | string | 1-2 phrases : quoi verifier AVANT d'acheter. Actionnable, pas generique |
| `intro_sync_parts` | string[] | Pieces a changer en meme temps (ex: disques + plaquettes) |

### 2. Risk (sgpg_risk_*)

| Champ | Type | Regle |
|-------|------|-------|
| `risk_title` | string | Question provocante ("Pourquoi ne pas attendre...") |
| `risk_explanation` | string | 2-3 risques concrets et chiffres |
| `risk_consequences` | string[] | Min 3 consequences precises |
| `risk_cost_range` | string | Fourchette prix en EUR |
| `risk_conclusion` | string | 1 phrase de conclusion |

### 3. Timing (sgpg_timing_*)

| Champ | Type | Regle |
|-------|------|-------|
| `timing_title` | string | "Quand changer les [gamme] ?" |
| `timing_years` | string | Frequence temporelle ou visuelle |
| `timing_km` | string | Kilometrage typique |
| `timing_note` | string | Cas de remplacement immediat |

### 4. Trust Arguments (sgpg_arg1-4_*)

4 arguments de confiance, chacun avec :
- `title` : 3-6 mots actionnables
- `content` : 1-2 phrases concretes
- `icon` : identifiant lucide-react (check-circle, shield-check, list-check, clock)

### 5. How To Choose (sgpg_how_to_choose)

Texte structure en etapes numerotees (1 a 5). Chaque etape = action + verification.

### 6. Symptoms (sgpg_symptoms)

`string[]` — Min 3, idealement 5. Symptomes observables par le conducteur.
Format : description sensorielle (bruit, vibration, visuel, sensation).

### 7. FAQ (sgpg_faq)

`jsonb[]` de `{question, answer}` — Min 5.
- `question` : min 10 caracteres, format interrogatif
- `answer` : min 20 caracteres, reponse actionnable

### 8. Anti-Mistakes (sgpg_anti_mistakes)

`string[]` — Min 4, idealement 8. **Format erreur uniquement** :
- Commence par un verbe negatif ou decrit une action incorrecte
- INTERDIT : actions positives ("Remplacement...", "Entretien...")
- CORRECT : "Oublier de nettoyer...", "Monter X sur Y use", "Ne pas respecter..."

### 9. Selection Criteria (sgpg_selection_criteria)

`jsonb[]` de `{key, label, guidance, priority}` — Min 5.
- `key` : snake_case unique
- `label` : nom du critere (3-5 mots)
- `guidance` : **OBLIGATION** explication concrete de COMMENT verifier le critere (min 50 chars, doit etre differente du label)
- `priority` : "required" ou "recommended"

### 10. Decision Tree (sgpg_decision_tree)

`jsonb[]` de `{id, question, options[]}` — Min 1 node.
- Chaque option : `{label, outcome, nextId?, note?}`
- `outcome` : "continue" | "check" | "replace" | "stop"
- Structure arborescente avec liens `nextId` entre nodes

### 11. Use Cases (sgpg_use_cases)

`jsonb[]` de `{id, label, recommendation}` — Min 3.
- **OBLIGATION** : profils conducteur (ville, route, montagne, sport)
- **INTERDIT** : types de produit (perces, rainures, standard)
- `recommendation` : conseil adapte au profil, pas description technique

## Quality Gate

Le guide DOIT passer l'Anti-Wiki Gate pour etre affiche :

| Critere | Seuil | Penalty si echec |
|---------|-------|------------------|
| selection_criteria count | >= 5 | bloquant |
| anti_mistakes count | >= 4 | bloquant |
| decision_tree nodes | >= 1 | bloquant |
| guidance != label | > 50% des criteres | 18 pts (GUIDANCE_COPIES_LABEL) |
| anti_mistakes format | > 50% format erreur | flag (ANTI_MISTAKES_NOT_ERRORS) |
| use_cases = profils | au moins 1 profil identifiable | flag (USE_CASES_NOT_PROFILES) |
| generic sans action | 0 phrase generique sans verbe d'action | bloquant |
| FAQ count | >= 3 | 14 pts |
| symptoms count | >= 3 | 12 pts |
| source_verified | true | 20 pts |

Score qualite = 100 - sum(penalties). Seuil minimum : 70/100.

## Source Provenance

| Champ | Regle |
|-------|-------|
| `source_type` | "rag", "db", "manual", "fallback" |
| `source_uri` | URI traçable (rag://..., pdf://..., oem://...) |
| `source_verified` | true si valide par pipeline ou humain |
| `source_verified_by` | "pipeline:rag-enrich" ou nom humain |

## Prototype de reference

pg_id=82 "Disque de frein" — premier guide enrichi et valide.
12 criteres, 8 anti-mistakes, 4 use_cases, 3 decision_tree, 5 FAQ, 5 symptoms.
