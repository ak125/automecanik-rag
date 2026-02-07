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
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
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
# Vase d'expansion - Guide Diagnostic Complet

## Fonction et Rôle

Compenser les variations de volume du liquide de refroidissement

**Actions principales:** compenser, stocker, indiquer, reguler la pression

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- fuite
- fissure
- niveau bas

## Procédure de Diagnostic

Pour diagnostiquer un problème de vase d'expansion:

1. **Inspection visuelle** - Examiner l'état du vase d'expansion
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bouchon-vase-d-expansion

## Critères de Compatibilité

Pour commander le bon vase d'expansion, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "evite la casse moteur"
