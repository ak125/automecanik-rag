---
entity_type: gamme
title: Vérin de coffre
slug: verin-de-coffre
pg_id: 5032
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Maintient le coffre ou hayon en position ouverte
  must_be_true:
    - maintenir
    - supporter
    - soulever
  must_not_contain_concepts:
    - serrure
    - verrouillage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_general_detecte
    then: inspection_visuelle_et_test_fonctionnel
symptoms:
  - id: S1
    label: Coffre qui retombe lentement
    description: coffre qui retombe lentement
    risk_level: confort
    evidence:
      - 'Observation: coffre qui retombe lentement'
      - Vérification visuelle ou auditive
  - id: S2
    label: Coffre impossible a maintenir ouvert
    description: coffre impossible a maintenir ouvert
    risk_level: confort
    evidence:
      - 'Observation: coffre impossible a maintenir ouvert'
      - Vérification visuelle ou auditive
  - id: S3
    label: Verin qui fuit traces graisseuses
    description: verin qui fuit traces graisseuses
    risk_level: confort
    evidence:
      - 'Observation: verin qui fuit traces graisseuses'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Vérin de coffre - Guide Diagnostic Complet

## Fonction et Rôle

Maintient le coffre ou hayon en position ouverte

**Actions principales:** maintenir, supporter, soulever

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- coffre qui retombe lentement
- coffre impossible a maintenir ouvert
- verin qui fuit traces graisseuses

## Procédure de Diagnostic

Pour diagnostiquer un problème de vérin de coffre:

1. **Inspection visuelle** - Examiner l'état du vérin de coffre
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- hayon
- charniere

## Critères de Compatibilité

Pour commander le bon vérin de coffre, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"
