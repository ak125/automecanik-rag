---
entity_type: gamme
title: Pompe d'amorcage
slug: pompe-d-amorcage
pg_id: 862
category: alimentation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Amorcer le circuit carburant lors du demarrage a froid
  must_be_true:
    - amorcer
    - aspirer
    - preparer
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
    label: Demarrage difficile apres coupure moteur
    description: demarrage difficile apres coupure moteur
    risk_level: confort
    evidence:
      - 'Observation: demarrage difficile apres coupure moteur'
      - Vérification visuelle ou auditive
  - id: S2
    label: Poire molle sans resistance
    description: poire molle sans resistance
    risk_level: confort
    evidence:
      - 'Observation: poire molle sans resistance'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bulles d air dans le circuit
    description: bulles d air dans le circuit
    risk_level: confort
    evidence:
      - 'Observation: bulles d air dans le circuit'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Pompe d'amorcage - Guide Diagnostic Complet

## Fonction et Rôle

Amorcer le circuit carburant lors du demarrage a froid

**Actions principales:** amorcer, aspirer, preparer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- demarrage difficile apres coupure moteur
- poire molle sans resistance
- bulles d air dans le circuit

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe d'amorcage:

1. **Inspection visuelle** - Examiner l'état du pompe d'amorcage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- accumulateur-de-pression-de-carburant
- regulateur-de-pression-carburant
- soupape-de-rampe-commune-d-injection

## Critères de Compatibilité

Pour commander le bon pompe d'amorcage, vous devez connaître:

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
