---
entity_type: gamme
title: Boulon de roue
slug: boulon-de-roue
pg_id: 657
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Fixe la roue sur le moyeu du véhicule
  must_be_true:
    - fixer
    - serrer
    - maintenir
  must_not_contain_concepts:
    - frein
    - moyeu
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: vibrations_anormales
    then: verifier_equilibrage_et_fixations
symptoms:
  - id: S1
    label: Vibrations lors du freinage
    description: vibrations lors du freinage
    risk_level: securite
    evidence:
      - 'Observation: vibrations lors du freinage'
      - Vérification visuelle ou auditive
  - id: S2
    label: Roue qui emet des claquements
    description: roue qui emet des claquements
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: roue qui emet des claquements'
      - Vérification visuelle ou auditive
  - id: S3
    label: Serrage impossible boulon tourne vide
    description: serrage impossible boulon tourne vide
    risk_level: confort
    evidence:
      - 'Observation: serrage impossible boulon tourne vide'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Boulon de roue - Guide Diagnostic Complet

## Fonction et Rôle

Fixe la roue sur le moyeu du véhicule

**Actions principales:** fixer, serrer, maintenir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Roue qui emet des claquements**
  roue qui emet des claquements

### 🟡 Symptômes de Sécurité

- **Vibrations lors du freinage**
  vibrations lors du freinage

### 🟢 Autres Symptômes

- serrage impossible boulon tourne vide

## Procédure de Diagnostic

Pour diagnostiquer un problème de boulon de roue:

1. **Inspection visuelle** - Examiner l'état du boulon de roue
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- jante
- moyeu

## Critères de Compatibilité

Pour commander le bon boulon de roue, vous devez connaître:

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
