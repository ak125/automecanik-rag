---
entity_type: gamme
title: Poignée de porte
slug: poignee-de-porte
pg_id: 1373
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Permet l'ouverture de la porte depuis l'extérieur ou l'intérieur
  must_be_true:
    - actionner
    - tirer
    - ouvrir
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
    label: Poignee molle ou sans ressort
    description: poignee molle ou sans ressort
    risk_level: confort
    evidence:
      - 'Observation: poignee molle ou sans ressort'
      - Vérification visuelle ou auditive
  - id: S2
    label: Porte qui ne s ouvre plus de l exterieur
    description: porte qui ne s ouvre plus de l exterieur
    risk_level: confort
    evidence:
      - 'Observation: porte qui ne s ouvre plus de l exterieur'
      - Vérification visuelle ou auditive
  - id: S3
    label: Poignee cassee physiquement
    description: poignee cassee physiquement
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: poignee cassee physiquement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Poignée de porte - Guide Diagnostic Complet

## Fonction et Rôle

Permet l'ouverture de la porte depuis l'extérieur ou l'intérieur

**Actions principales:** actionner, tirer, ouvrir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Poignee cassee physiquement**
  poignee cassee physiquement

### 🟢 Autres Symptômes

- poignee molle ou sans ressort
- porte qui ne s ouvre plus de l exterieur

## Procédure de Diagnostic

Pour diagnostiquer un problème de poignée de porte:

1. **Inspection visuelle** - Examiner l'état du poignée de porte
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- serrure
- cable

## Critères de Compatibilité

Pour commander le bon poignée de porte, vous devez connaître:

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
