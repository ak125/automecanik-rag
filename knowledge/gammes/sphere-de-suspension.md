---
entity_type: gamme
title: Sphère de suspension
slug: sphere-de-suspension
pg_id: 1718
category: suspension
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Assurer la suspension via pression hydraulique et gaz (systeme Citroen).
    Remplace amortisseur ET ressort. NE FONCTIONNE PAS COMME UN RESSORT
    CLASSIQUE!
  must_be_true:
    - stabiliser hydrauliquement
    - reguler la pression
    - amortir hydrauliquement
  must_not_contain_concepts:
    - ressort helicoidale
    - amortisseur classique
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
    label: Suspension tres dure
    description: suspension tres dure
    risk_level: securite
    evidence:
      - 'Observation: suspension tres dure'
      - Vérification visuelle ou auditive
  - id: S2
    label: Vehicule qui ne monte plus en hauteur
    description: vehicule qui ne monte plus en hauteur
    risk_level: confort
    evidence:
      - 'Observation: vehicule qui ne monte plus en hauteur'
      - Vérification visuelle ou auditive
  - id: S3
    label: Confort de roulement degrade
    description: confort de roulement degrade
    risk_level: confort
    evidence:
      - 'Observation: confort de roulement degrade'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Sphère de suspension - Guide Diagnostic Complet

## Fonction et Rôle

Assurer la suspension via pression hydraulique et gaz (systeme Citroen). Remplace amortisseur ET ressort. NE FONCTIONNE PAS COMME UN RESSORT CLASSIQUE!

**Actions principales:** stabiliser hydrauliquement, reguler la pression, amortir hydrauliquement, maintenir la hauteur

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Suspension tres dure**
  suspension tres dure

### 🟢 Autres Symptômes

- vehicule qui ne monte plus en hauteur
- confort de roulement degrade

## Procédure de Diagnostic

Pour diagnostiquer un problème de sphère de suspension:

1. **Inspection visuelle** - Examiner l'état du sphère de suspension
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- amortisseur
- suspension

## Critères de Compatibilité

Pour commander le bon sphère de suspension, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "tenue de route parfaite"
