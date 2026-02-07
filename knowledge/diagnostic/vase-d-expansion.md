---
entity_type: gamme
title: Vase d'expansion
slug: vase-d-expansion
pg_id: 397
category: refroidissement
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Compenser les variations de volume du liquide de refroidissement
  must_be_true:
    - compenser
    - stocker
    - indiquer
  must_not_contain_concepts:
    - radiateur
    - pompe
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_fuite
    then: verifier_piece
  - if: symptome_fissure
    then: diagnostic_approfondi
  - if: symptome_niveau-bas
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Fuite
    description: fuite
    risk_level: confort
    evidence:
      - 'Observation: fuite'
      - Vérification visuelle ou auditive
  - id: S2
    label: Fissure
    description: fissure
    risk_level: confort
    evidence:
      - 'Observation: fissure'
      - Vérification visuelle ou auditive
  - id: S3
    label: Niveau bas
    description: niveau bas
    risk_level: confort
    evidence:
      - 'Observation: niveau bas'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Vase d'expansion - Guide Complet

## Fonction

Compenser les variations de volume du liquide de refroidissement

## Symptômes de défaillance

### Fuite

fuite

### Fissure

fissure

### Niveau bas

niveau bas

## Diagnostic

Pour diagnostiquer un problème de vase d'expansion:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- bouchon-vase-d-expansion

## Compatibilité

Pour commander le bon vase d'expansion, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
