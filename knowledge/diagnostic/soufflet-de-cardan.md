---
entity_type: gamme
title: Soufflet de Cardan
slug: soufflet-de-cardan
pg_id: 193
category: transmission
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Protege le joint de cardan et retient la graisse de lubrification
  must_be_true:
    - proteger
    - etancher
    - contenir
  must_not_contain_concepts:
    - injection
    - freinage
    - climatisation
    - allumage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_graisse-noire-visible-sur-la-jante
    then: verifier_piece
  - if: symptome_soufflet-fendu-dechire-ou-decolle-visible
    then: diagnostic_approfondi
  - if: symptome_claquement-en-braquant-joint-deja-endommage
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Graisse noire visible sur la jante
    description: graisse noire visible sur la jante interieure
    risk_level: confort
    evidence:
      - 'Observation: graisse noire visible sur la jante'
      - Vérification visuelle ou auditive
  - id: S2
    label: Soufflet fendu dechire ou decolle visible
    description: soufflet fendu dechire ou decolle visible
    risk_level: confort
    evidence:
      - 'Observation: soufflet fendu dechire ou decolle visible'
      - Vérification visuelle ou auditive
  - id: S3
    label: Claquement en braquant joint deja endommage
    description: claquement en braquant joint deja endommage
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement en braquant joint deja endommage'
      - Vérification visuelle ou auditive
  - id: S4
    label: Odeur de graisse brulee pres de
    description: odeur de graisse brulee pres de la roue
    risk_level: confort
    evidence:
      - 'Observation: odeur de graisse brulee pres de'
      - Vérification visuelle ou auditive
  - id: S5
    label: Vibrations au volant a vitesse constante
    description: vibrations au volant a vitesse constante
    risk_level: confort
    evidence:
      - 'Observation: vibrations au volant a vitesse constante'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus controle visuel soufflets
    description: plus controle visuel soufflets
    risk_level: confort
    evidence:
      - 'Observation: plus controle visuel soufflets'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Soufflet de Cardan - Guide Complet

## Fonction

Protege le joint de cardan et retient la graisse de lubrification

## Symptômes de défaillance

### Graisse noire visible sur la jante

graisse noire visible sur la jante interieure

### Soufflet fendu dechire ou decolle visible

soufflet fendu dechire ou decolle visible

### Claquement en braquant joint deja endommage

claquement en braquant joint deja endommage

### Odeur de graisse brulee pres de

odeur de graisse brulee pres de la roue

### Vibrations au volant a vitesse constante

vibrations au volant a vitesse constante

### Plus controle visuel soufflets

plus controle visuel soufflets

## Diagnostic

Pour diagnostiquer un problème de soufflet de cardan:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- cardan

## Compatibilité

Pour commander le bon soufflet de cardan, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
