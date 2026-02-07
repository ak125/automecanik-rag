---
entity_type: gamme
title: Roulement de roue
slug: roulement-de-roue
pg_id: 655
category: direction
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Permettre la rotation libre de la roue sur son axe - Supporte les charges
    radiales et axiales
  must_be_true:
    - permettre la rotation
    - supporter
    - guider
  must_not_contain_concepts:
    - direction
    - cremailliere
    - volant
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_ronronnement-grondement-augmente-vitesse
    then: verifier_piece
  - if: symptome_bruit-qui-change-d-intensite-dans
    then: diagnostic_approfondi
  - if: symptome_jeu-perceptible-en-secouant-la-roue
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Ronronnement grondement augmente vitesse
    description: ronronnement grondement augmente vitesse
    risk_level: confort
    evidence:
      - 'Observation: ronronnement grondement augmente vitesse'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit qui change d intensite dans
    description: bruit qui change d intensite dans les virages
    risk_level: confort
    evidence:
      - 'Observation: bruit qui change d intensite dans'
      - Vérification visuelle ou auditive
  - id: S3
    label: Jeu perceptible en secouant la roue
    description: jeu perceptible en secouant la roue montee
    risk_level: confort
    evidence:
      - 'Observation: jeu perceptible en secouant la roue'
      - Vérification visuelle ou auditive
  - id: S4
    label: Vibrations dans le volant a certaines
    description: vibrations dans le volant a certaines vitesses
    risk_level: confort
    evidence:
      - 'Observation: vibrations dans le volant a certaines'
      - Vérification visuelle ou auditive
  - id: S5
    label: Roue anormalement chaude apres roulage
    description: roue anormalement chaude apres roulage
    risk_level: confort
    evidence:
      - 'Observation: roue anormalement chaude apres roulage'
      - Vérification visuelle ou auditive
  - id: S6
    label: Bruit de frottement ou de craquement
    description: bruit de frottement ou de craquement
    risk_level: confort
    evidence:
      - 'Observation: bruit de frottement ou de craquement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Roulement de roue - Guide Complet

## Fonction

Permettre la rotation libre de la roue sur son axe - Supporte les charges radiales et axiales

## Symptômes de défaillance

### Ronronnement grondement augmente vitesse

ronronnement grondement augmente vitesse

### Bruit qui change d intensite dans

bruit qui change d intensite dans les virages

### Jeu perceptible en secouant la roue

jeu perceptible en secouant la roue montee

### Vibrations dans le volant a certaines

vibrations dans le volant a certaines vitesses

### Roue anormalement chaude apres roulage

roue anormalement chaude apres roulage

### Bruit de frottement ou de craquement

bruit de frottement ou de craquement

## Diagnostic

Pour diagnostiquer un problème de roulement de roue:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- capteur-abs
- disque-de-frein
- plaquette-de-frein

## Compatibilité

Pour commander le bon roulement de roue, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
