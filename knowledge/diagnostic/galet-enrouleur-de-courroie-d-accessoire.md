---
entity_type: gamme
title: Galet enrouleur de courroie d'accessoire
slug: galet-enrouleur-de-courroie-d-accessoire
pg_id: 312
category: distribution
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Guide la courroie d'accessoire
  must_be_true:
    - guider
    - enrouler
    - maintenir
  must_not_contain_concepts:
    - freinage
    - climatisation
    - turbo
    - injection
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_courroie-d-accessoire-visiblement-usee-ou
    then: verifier_piece
  - if: symptome_sifflement-ou-grondement-au-niveau-de
    then: diagnostic_approfondi
  - if: symptome_perceptible-faisant-tourner-galet-main
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Courroie d accessoire visiblement usee ou
    description: courroie d accessoire visiblement usee ou fissuree
    risk_level: confort
    evidence:
      - 'Observation: courroie d accessoire visiblement usee ou'
      - Vérification visuelle ou auditive
  - id: S2
    label: Sifflement ou grondement au niveau de
    description: sifflement ou grondement au niveau de la courroie
    risk_level: confort
    evidence:
      - 'Observation: sifflement ou grondement au niveau de'
      - Vérification visuelle ou auditive
  - id: S3
    label: Perceptible faisant tourner galet main
    description: perceptible faisant tourner galet main
    risk_level: confort
    evidence:
      - 'Observation: perceptible faisant tourner galet main'
      - Vérification visuelle ou auditive
  - id: S4
    label: Perte de tension de la courroie
    description: perte de tension de la courroie
    risk_level: confort
    evidence:
      - 'Observation: perte de tension de la courroie'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de caoutchouc chaud
    description: odeur de caoutchouc chaud
    risk_level: confort
    evidence:
      - 'Observation: odeur de caoutchouc chaud'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 80 000 km depuis
    description: plus de 80 000 km depuis le dernier changement
    risk_level: confort
    evidence:
      - 'Observation: plus de 80 000 km depuis'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Galet enrouleur de courroie d'accessoire - Guide Complet

## Fonction

Guide la courroie d'accessoire

## Symptômes de défaillance

### Courroie d accessoire visiblement usee ou

courroie d accessoire visiblement usee ou fissuree

### Sifflement ou grondement au niveau de

sifflement ou grondement au niveau de la courroie

### Perceptible faisant tourner galet main

perceptible faisant tourner galet main

### Perte de tension de la courroie

perte de tension de la courroie

### Odeur de caoutchouc chaud

odeur de caoutchouc chaud

### Plus de 80 000 km depuis

plus de 80 000 km depuis le dernier changement

## Diagnostic

Pour diagnostiquer un problème de galet enrouleur de courroie d'accessoire:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- alternateur
- compresseur-de-climatisation
- courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- pompe-a-eau

## Compatibilité

Pour commander le bon galet enrouleur de courroie d'accessoire, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
