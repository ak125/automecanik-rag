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
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: vibrations_anormales
    then: verifier_equilibrage_et_fixations
symptoms:
  - id: S1
    label: Graisse noire visible sur la jante interieure
    description: graisse noire visible sur la jante interieure
    risk_level: confort
    evidence:
      - 'Observation: graisse noire visible sur la jante interieure'
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
    label: Odeur de graisse brulee pres de la roue
    description: odeur de graisse brulee pres de la roue
    risk_level: confort
    evidence:
      - 'Observation: odeur de graisse brulee pres de la roue'
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
# Soufflet de Cardan - Guide Diagnostic Complet

## Fonction et Rôle

Protege le joint de cardan et retient la graisse de lubrification

**Actions principales:** proteger, etancher, contenir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement en braquant joint deja endommage**
  claquement en braquant joint deja endommage

### 🟢 Autres Symptômes

- graisse noire visible sur la jante interieure
- soufflet fendu dechire ou decolle visible
- odeur de graisse brulee pres de la roue
- vibrations au volant a vitesse constante
- plus controle visuel soufflets

## Procédure de Diagnostic

Pour diagnostiquer un problème de soufflet de cardan:

1. **Inspection visuelle** - Examiner l'état du soufflet de cardan
2. **Test dynamique** - Vérifier les bruits en roulant
3. **Contrôle du jeu** - Examiner l'usure des articulations

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- cardan

## Critères de Compatibilité

Pour commander le bon soufflet de cardan, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "transmission parfaite"
