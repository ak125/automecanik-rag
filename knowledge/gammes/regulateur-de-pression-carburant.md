---
entity_type: gamme
title: Régulateur de pression carburant
slug: regulateur-de-pression-carburant
pg_id: 168
category: alimentation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Maintenir une pression constante dans le circuit carburant
  must_be_true:
    - reguler
    - maintenir
    - stabiliser
  must_not_contain_concepts:
    - freinage
    - climatisation
    - distribution
    - embrayage
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
    label: Ralenti instable
    description: ralenti instable
    risk_level: confort
    evidence:
      - 'Observation: ralenti instable'
      - Vérification visuelle ou auditive
  - id: S2
    label: Demarrage a chaud difficile
    description: demarrage a chaud difficile
    risk_level: confort
    evidence:
      - 'Observation: demarrage a chaud difficile'
      - Vérification visuelle ou auditive
  - id: S3
    label: Odeur de carburant dans le compartiment moteur
    description: odeur de carburant dans le compartiment moteur
    risk_level: confort
    evidence:
      - 'Observation: odeur de carburant dans le compartiment moteur'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Régulateur de pression carburant - Guide Diagnostic Complet

## Fonction et Rôle

Maintenir une pression constante dans le circuit carburant

**Actions principales:** reguler, maintenir, stabiliser

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- ralenti instable
- demarrage a chaud difficile
- odeur de carburant dans le compartiment moteur

## Procédure de Diagnostic

Pour diagnostiquer un problème de régulateur de pression carburant:

1. **Inspection visuelle** - Examiner l'état du régulateur de pression carburant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- accumulateur-de-pression-de-carburant
- pompe-d-amorcage
- soupape-de-rampe-commune-d-injection

## Critères de Compatibilité

Pour commander le bon régulateur de pression carburant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare l'injection"
