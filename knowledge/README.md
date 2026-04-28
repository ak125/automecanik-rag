---
category: README.md
doc_family: knowledge
source_type: general
---

> ⚠️ **Répertoire généré post-Phase F (ADR-031 §D22).**
>
> La source canonique de ce contenu est `automecanik-wiki/exports/rag/`.
> Le script `nestjs-remix-monorepo/scripts/rag/sync-from-wiki.py --apply`
> régénère ce dossier à chaque sync.
>
> **Toute modification manuelle sera écrasée** à la prochaine sync.
>
> Pour rollback documenté pendant un incident :
>
> 1. Préparer le fix dans `automecanik-wiki/proposals/<slug>.md`
>    (puis promotion vers `wiki/<entity_type>/<slug>.md`).
> 2. Si le fix doit prendre effet immédiat avant la prochaine sync,
>    commit ici avec le message marqueur :
>
>    ```
>    fix(rollback-documented): <one-line subject>
>
>    Why: <incident reference, why this can't wait for the next sync>
>    Linked wiki PR: <ak125/automecanik-wiki PR URL>
>    ```
>
> Les hooks `.githooks/commit-msg` + le workflow CI `d22-protected-paths.yml`
> bloquent toute écriture sous `knowledge/<5 catégories>` qui ne contient
> pas le marqueur `rollback-documented`.

# Corpus Métier AutoMecanik

Ce dossier contient la base de connaissance métier pour le système RAG.

## Structure

```
knowledge/
├── diagnostic/     # Diagnostics véhicule (symptômes, causes, solutions)
├── vehicles/       # Fiches véhicules et marques
├── faq/            # FAQ support client
├── policies/       # Politiques (retours, garantie, livraison)
└── guides/         # Guides pratiques
```

## Format des fichiers

Chaque fichier Markdown doit avoir un frontmatter YAML :

```markdown
---
title: "Titre du document"
source_type: diagnostic|faq|policy|guide|vehicle
category: freinage|moteur|livraison|retours|...
updated_at: 2026-01-01
---

# Contenu...
```

## Indexation

Le contenu est indexé dans Weaviate via le service RAG :
- **prod:chatbot** - Accessible en production (chatbot client)
- **dev:full** - Accessible en développement (agents internes)

## Mise à jour

1. Modifier les fichiers dans ce dossier
2. Créer une PR
3. Après merge sur `main`, le contenu est automatiquement réindexé