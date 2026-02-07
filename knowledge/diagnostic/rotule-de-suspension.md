---
entity_type: gamme
title: Rotule de suspension
slug: rotule-de-suspension
pg_id: 2462
category: direction
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Articuler le bras de suspension et la fusee - Supporte la charge verticale.
    NE DIRIGE PAS!
  must_be_true:
    - supporter la charge
    - articuler
    - maintenir
  must_not_contain_concepts:
    - direction
    - cremailliere
    - volant
    - braquage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_claquements-sourds-sur-dos-d-ane
    then: verifier_piece
  - if: symptome_vehicule-qui-tire-d-un-cote
    then: diagnostic_approfondi
  - if: symptome_jeu-visible-en-soulevant-la-roue
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Claquements sourds sur dos d ane
    description: claquements sourds sur dos d ane ou nids de poule
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquements sourds sur dos d ane'
      - Vérification visuelle ou auditive
  - id: S2
    label: Vehicule qui tire d un cote
    description: vehicule qui tire d un cote
    risk_level: confort
    evidence:
      - 'Observation: vehicule qui tire d un cote'
      - Vérification visuelle ou auditive
  - id: S3
    label: Jeu visible en soulevant la roue
    description: jeu visible en soulevant la roue a la main
    risk_level: confort
    evidence:
      - 'Observation: jeu visible en soulevant la roue'
      - Vérification visuelle ou auditive
  - id: S4
    label: Craquements en braquant a fond
    description: craquements en braquant a fond
    risk_level: confort
    evidence:
      - 'Observation: craquements en braquant a fond'
      - Vérification visuelle ou auditive
  - id: S5
    label: Soufflet de rotule dechire ou absent
    description: soufflet de rotule dechire ou absent
    risk_level: securite
    evidence:
      - 'Observation: soufflet de rotule dechire ou absent'
      - Vérification visuelle ou auditive
  - id: S6
    label: Usure anormale des pneus avant
    description: usure anormale des pneus avant
    risk_level: securite
    evidence:
      - 'Observation: usure anormale des pneus avant'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Rotule de suspension - Guide Complet

## Fonction

Articuler le bras de suspension et la fusee - Supporte la charge verticale. NE DIRIGE PAS!

## Symptômes de défaillance

### Claquements sourds sur dos d ane

claquements sourds sur dos d ane ou nids de poule

### Vehicule qui tire d un cote

vehicule qui tire d un cote

### Jeu visible en soulevant la roue

jeu visible en soulevant la roue a la main

### Craquements en braquant a fond

craquements en braquant a fond

### Soufflet de rotule dechire ou absent

soufflet de rotule dechire ou absent

### Usure anormale des pneus avant

usure anormale des pneus avant

## Diagnostic

Pour diagnostiquer un problème de rotule de suspension:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- amortisseur
- barre-stabilisatrice
- bras-de-suspension
- ressort-de-suspension
- rotule-de-direction

## Compatibilité

Pour commander le bon rotule de suspension, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
