---
entity_type: gamme
title: Faisceau d'attelage
slug: faisceau-d-attelage
pg_id: 179
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Assure la connexion électrique entre le véhicule et la remorque
  must_be_true:
    - connecter
    - alimenter
    - transmettre
  must_not_contain_concepts:
    - freinage
    - abs
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
    label: Feux de remorque inactifs
    description: feux de remorque inactifs
    risk_level: confort
    evidence:
      - 'Observation: feux de remorque inactifs'
      - Vérification visuelle ou auditive
  - id: S2
    label: Clignotants non synchronises
    description: clignotants non synchronises
    risk_level: confort
    evidence:
      - 'Observation: clignotants non synchronises'
      - Vérification visuelle ou auditive
  - id: S3
    label: Court-circuit au branchement
    description: court-circuit au branchement
    risk_level: confort
    evidence:
      - 'Observation: court-circuit au branchement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Faisceau d'attelage - Guide Diagnostic Complet

## Fonction et Rôle

Assure la connexion électrique entre le véhicule et la remorque

**Actions principales:** connecter, alimenter, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- feux de remorque inactifs
- clignotants non synchronises
- court-circuit au branchement

## Procédure de Diagnostic

Pour diagnostiquer un problème de faisceau d'attelage:

1. **Inspection visuelle** - Examiner l'état du faisceau d'attelage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- attelage
- prise

## Critères de Compatibilité

Pour commander le bon faisceau d'attelage, vous devez connaître:

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
