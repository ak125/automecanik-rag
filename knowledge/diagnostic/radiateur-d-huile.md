---
entity_type: gamme
title: Radiateur d'huile
slug: radiateur-d-huile
pg_id: 469
category: moteur
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Refroidir l'huile moteur
  must_be_true:
    - refroidir
    - echanger
    - maintenir la temperature
  must_not_contain_concepts:
    - eau
    - liquide refroidissement
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_huile-surchauffee
    then: verifier_piece
  - if: symptome_melange-eau-huile
    then: diagnostic_approfondi
  - if: symptome_fuites-externes-au-niveau-du-radiateur
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Huile surchauffee
    description: huile surchauffee
    risk_level: confort
    evidence:
      - 'Observation: huile surchauffee'
      - Vérification visuelle ou auditive
  - id: S2
    label: Melange eau-huile
    description: melange eau-huile
    risk_level: confort
    evidence:
      - 'Observation: melange eau-huile'
      - Vérification visuelle ou auditive
  - id: S3
    label: Fuites externes au niveau du radiateur
    description: fuites externes au niveau du radiateur
    risk_level: confort
    evidence:
      - 'Observation: fuites externes au niveau du radiateur'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Radiateur d'huile - Guide Complet

## Fonction

Refroidir l'huile moteur

## Symptômes de défaillance

### Huile surchauffee

huile surchauffee

### Melange eau-huile

melange eau-huile

### Fuites externes au niveau du radiateur

fuites externes au niveau du radiateur

## Diagnostic

Pour diagnostiquer un problème de radiateur d'huile:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- filtre-a-huile
- pompe-a-huile

## Compatibilité

Pour commander le bon radiateur d'huile, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
