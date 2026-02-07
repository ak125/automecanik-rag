---
entity_type: gamme
title: Interrupteur position de marche
slug: interrupteur-position-de-marche
pg_id: 2197
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
    Signaler la position de la boite de vitesses pour autoriser le demarrage ou
    activer les feux de recul
  must_be_true:
    - signaler
    - activer
    - commuter
  must_not_contain_concepts:
    - capteur
    - sonde
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
    label: Feux de recul qui ne s allument pas
    description: feux de recul qui ne s allument pas
    risk_level: confort
    evidence:
      - 'Observation: feux de recul qui ne s allument pas'
      - Vérification visuelle ou auditive
  - id: S2
    label: Marche arriere non detectee par le calculateur
    description: marche arriere non detectee par le calculateur
    risk_level: confort
    evidence:
      - 'Observation: marche arriere non detectee par le calculateur'
      - Vérification visuelle ou auditive
  - id: S3
    label: Camera de recul inactive
    description: camera de recul inactive
    risk_level: confort
    evidence:
      - 'Observation: camera de recul inactive'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Interrupteur position de marche - Guide Diagnostic Complet

## Fonction et Rôle

Signaler la position de la boite de vitesses pour autoriser le demarrage ou activer les feux de recul

**Actions principales:** signaler, activer, commuter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- feux de recul qui ne s allument pas
- marche arriere non detectee par le calculateur
- camera de recul inactive

## Procédure de Diagnostic

Pour diagnostiquer un problème de interrupteur position de marche:

1. **Inspection visuelle** - Examiner l'état du interrupteur position de marche
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- contacteur-demarreur
- neiman

## Critères de Compatibilité

Pour commander le bon interrupteur position de marche, vous devez connaître:

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
