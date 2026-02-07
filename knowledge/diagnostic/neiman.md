---
entity_type: gamme
title: Neiman
slug: neiman
pg_id: 1367
category: electrique
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Verrouiller la direction et alimenter les circuits electriques
  must_be_true:
    - verrouiller
    - alimenter
    - securiser
  must_not_contain_concepts:
    - injection
    - climatisation
    - freinage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_tableau-de-bord-qui-ne-s
    then: verifier_piece
  - if: symptome_cle-qui-tourne-dans-le-vide
    then: diagnostic_approfondi
  - if: symptome_direction-bloquee-impossible-a-debloquer
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Tableau de bord qui ne s
    description: tableau de bord qui ne s allume pas au contact
    risk_level: confort
    evidence:
      - 'Observation: tableau de bord qui ne s'
      - Vérification visuelle ou auditive
  - id: S2
    label: Cle qui tourne dans le vide
    description: cle qui tourne dans le vide sans effet
    risk_level: confort
    evidence:
      - 'Observation: cle qui tourne dans le vide'
      - Vérification visuelle ou auditive
  - id: S3
    label: Direction bloquee impossible a debloquer
    description: direction bloquee impossible a debloquer
    risk_level: immobilisation
    evidence:
      - 'Observation: direction bloquee impossible a debloquer'
      - Vérification visuelle ou auditive
  - id: S4
    label: Contact electrique intermittent coupures
    description: contact electrique intermittent coupures
    risk_level: confort
    evidence:
      - 'Observation: contact electrique intermittent coupures'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de plastique brule court-circuit interne
    description: odeur de plastique brule court-circuit interne
    risk_level: confort
    evidence:
      - 'Observation: odeur de plastique brule court-circuit interne'
      - Vérification visuelle ou auditive
  - id: S6
    label: Difficulte recurrente a tourner la cle
    description: difficulte recurrente a tourner la cle
    risk_level: confort
    evidence:
      - 'Observation: difficulte recurrente a tourner la cle'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Neiman - Guide Complet

## Fonction

Verrouiller la direction et alimenter les circuits electriques

## Symptômes de défaillance

### Tableau de bord qui ne s

tableau de bord qui ne s allume pas au contact

### Cle qui tourne dans le vide

cle qui tourne dans le vide sans effet

### Direction bloquee impossible a debloquer

direction bloquee impossible a debloquer

### Contact electrique intermittent coupures

contact electrique intermittent coupures

### Odeur de plastique brule court-circuit interne

odeur de plastique brule court-circuit interne

### Difficulte recurrente a tourner la cle

difficulte recurrente a tourner la cle

## Diagnostic

Pour diagnostiquer un problème de neiman:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- alternateur
- colonne-de-direction
- demarreur

## Compatibilité

Pour commander le bon neiman, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
