---
entity_type: gamme
title: Emetteur d'embrayage
slug: emetteur-d-embrayage
pg_id: 234
category: embrayage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmettre la pression hydraulique de la pédale vers le récepteur
  must_be_true:
    - transmettre la pression
    - pousser le liquide
    - convertir l'effort
  must_not_contain_concepts:
    - disque
    - volant
    - couple
    - câble
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_pedale-d-embrayage-molle-ou-spongieuse
    then: verifier_piece
  - if: symptome_pedale-qui-s-enfonce-jusqu-au
    then: diagnostic_approfondi
  - if: symptome_niveau-liquide-frein-baisse-fuite
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Pedale d embrayage molle ou spongieuse
    description: pedale d embrayage molle ou spongieuse
    risk_level: confort
    evidence:
      - 'Observation: pedale d embrayage molle ou spongieuse'
      - Vérification visuelle ou auditive
  - id: S2
    label: Pedale qui s enfonce jusqu au
    description: pedale qui s enfonce jusqu au plancher
    risk_level: confort
    evidence:
      - 'Observation: pedale qui s enfonce jusqu au'
      - Vérification visuelle ou auditive
  - id: S3
    label: Niveau liquide frein baisse fuite
    description: niveau liquide frein baisse fuite
    risk_level: securite
    evidence:
      - 'Observation: niveau liquide frein baisse fuite'
      - Vérification visuelle ou auditive
  - id: S4
    label: Fuite liquide sous tableau bord
    description: fuite liquide sous tableau bord
    risk_level: confort
    evidence:
      - 'Observation: fuite liquide sous tableau bord'
      - Vérification visuelle ou auditive
  - id: S5
    label: Embrayage qui patine par intermittence
    description: embrayage qui patine par intermittence
    risk_level: confort
    evidence:
      - 'Observation: embrayage qui patine par intermittence'
      - Vérification visuelle ou auditive
  - id: S6
    label: Difficulte a debrayer completement
    description: difficulte a debrayer completement
    risk_level: confort
    evidence:
      - 'Observation: difficulte a debrayer completement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Emetteur d'embrayage - Guide Complet

## Fonction

Transmettre la pression hydraulique de la pédale vers le récepteur

## Symptômes de défaillance

### Pedale d embrayage molle ou spongieuse

pedale d embrayage molle ou spongieuse

### Pedale qui s enfonce jusqu au

pedale qui s enfonce jusqu au plancher

### Niveau liquide frein baisse fuite

niveau liquide frein baisse fuite

### Fuite liquide sous tableau bord

fuite liquide sous tableau bord

### Embrayage qui patine par intermittence

embrayage qui patine par intermittence

### Difficulte a debrayer completement

difficulte a debrayer completement

## Diagnostic

Pour diagnostiquer un problème de emetteur d'embrayage:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- butee-d-embrayage
- kit-d-embrayage
- recepteur-d-embrayage

## Compatibilité

Pour commander le bon emetteur d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
