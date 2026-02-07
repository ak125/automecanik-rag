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
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
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
# Radiateur d'huile - Guide Diagnostic Complet

## Fonction et Rôle

Refroidir l'huile moteur

**Actions principales:** refroidir, echanger, maintenir la temperature

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- huile surchauffee
- melange eau-huile
- fuites externes au niveau du radiateur

## Procédure de Diagnostic

Pour diagnostiquer un problème de radiateur d'huile:

1. **Inspection visuelle** - Examiner l'état du radiateur d'huile
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- filtre-a-huile
- pompe-a-huile

## Critères de Compatibilité

Pour commander le bon radiateur d'huile, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"
