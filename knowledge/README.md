# Corpus Métier AutoMecanik

Ce dossier contient la base de connaissance métier pour le système RAG.

## Structure

```
knowledge/
├── diagnostic/     # Diagnostics véhicule (symptômes, causes, solutions)
├── vehicle/        # Compatibilité véhicule/pièces
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
