---
entity_type: gamme
title: Amortisseur de direction
slug: amortisseur-de-direction
pg_id: 130
category: direction
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Amortir les vibrations et chocs transmis au volant
  must_be_true:
    - amortir
    - stabiliser
    - filtrer
  must_not_contain_concepts:
    - injection
    - freinage
    - distribution
    - turbo
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_shimmy-vibration-du-volant-a-certaines
    then: verifier_piece
  - if: symptome_direction-qui-tire-d-un-cote
    then: diagnostic_approfondi
  - if: symptome_sensation-de-flottement-dans-la-direction
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Shimmy vibration du volant a certaines
    description: shimmy vibration du volant a certaines vitesses
    risk_level: confort
    evidence:
      - 'Observation: shimmy vibration du volant a certaines'
      - Vérification visuelle ou auditive
  - id: S2
    label: Direction qui tire d un cote
    description: direction qui tire d un cote
    risk_level: securite
    evidence:
      - 'Observation: direction qui tire d un cote'
      - Vérification visuelle ou auditive
  - id: S3
    label: Sensation de flottement dans la direction
    description: sensation de flottement dans la direction
    risk_level: securite
    evidence:
      - 'Observation: sensation de flottement dans la direction'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Amortisseur de direction - Guide Complet

## Fonction

Amortir les vibrations et chocs transmis au volant

## Symptômes de défaillance

### Shimmy vibration du volant a certaines

shimmy vibration du volant a certaines vitesses

### Direction qui tire d un cote

direction qui tire d un cote

### Sensation de flottement dans la direction

sensation de flottement dans la direction

## Diagnostic

Pour diagnostiquer un problème de amortisseur de direction:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- cremaillere-de-direction
- colonne-de-direction

## Compatibilité

Pour commander le bon amortisseur de direction, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
