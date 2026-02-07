---
entity_type: gamme
title: Capteur de pédale d'accélérateur
slug: capteur-de-pedale-d-accelerateur
pg_id: 3908
category: capteurs
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Mesurer la position de la pedale d'accelerateur et transmettre la demande du
    conducteur au calculateur
  must_be_true:
    - mesurer
    - detecter
    - transmettre
  must_not_contain_concepts:
    - papillon
    - admission
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
symptoms:
  - id: S1
    label: Accelerations irregulieres ou saccadees
    description: accelerations irregulieres ou saccadees
    risk_level: confort
    evidence:
      - 'Observation: accelerations irregulieres ou saccadees'
      - Vérification visuelle ou auditive
  - id: S2
    label: Mode degrade moteur active
    description: mode degrade moteur active
    risk_level: confort
    evidence:
      - 'Observation: mode degrade moteur active'
      - Vérification visuelle ou auditive
  - id: S3
    label: Voyant moteur avec code pedale
    description: voyant moteur avec code pedale
    risk_level: confort
    evidence:
      - 'Observation: voyant moteur avec code pedale'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Capteur de pédale d'accélérateur - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la position de la pedale d'accelerateur et transmettre la demande du conducteur au calculateur

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- accelerations irregulieres ou saccadees
- mode degrade moteur active
- voyant moteur avec code pedale

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur de pédale d'accélérateur:

1. **Inspection visuelle** - Examiner l'état du capteur de pédale d'accélérateur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-position-papillon

## Critères de Compatibilité

Pour commander le bon capteur de pédale d'accélérateur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "corrige la panne"
