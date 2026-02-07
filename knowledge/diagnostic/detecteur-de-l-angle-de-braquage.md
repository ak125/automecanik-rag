---
entity_type: gamme
title: Détecteur de l'angle de braquage
slug: detecteur-de-l-angle-de-braquage
pg_id: 3252
category: direction
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Mesurer l'angle de rotation du volant pour l'ESP
  must_be_true:
    - mesurer
    - detecter
    - transmettre
  must_not_contain_concepts:
    - injection
    - freinage
    - distribution
    - turbo
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_voyant-esp-allume-en-permanence
    then: verifier_piece
  - if: symptome_direction-assistee-desactivee
    then: diagnostic_approfondi
  - if: symptome_comportement-anormal-du-vehicule-en-virage
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Voyant esp allume en permanence
    description: voyant esp allume en permanence
    risk_level: securite
    evidence:
      - 'Observation: voyant esp allume en permanence'
      - Vérification visuelle ou auditive
  - id: S2
    label: Direction assistee desactivee
    description: direction assistee desactivee
    risk_level: securite
    evidence:
      - 'Observation: direction assistee desactivee'
      - Vérification visuelle ou auditive
  - id: S3
    label: Comportement anormal du vehicule en virage
    description: comportement anormal du vehicule en virage
    risk_level: confort
    evidence:
      - 'Observation: comportement anormal du vehicule en virage'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Détecteur de l'angle de braquage - Guide Complet

## Fonction

Mesurer l'angle de rotation du volant pour l'ESP

## Symptômes de défaillance

### Voyant esp allume en permanence

voyant esp allume en permanence

### Direction assistee desactivee

direction assistee desactivee

### Comportement anormal du vehicule en virage

comportement anormal du vehicule en virage

## Diagnostic

Pour diagnostiquer un problème de détecteur de l'angle de braquage:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- calculateur-esp
- capteur-abs

## Compatibilité

Pour commander le bon détecteur de l'angle de braquage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
