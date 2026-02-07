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
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: vibrations_anormales
    then: verifier_equilibrage_et_fixations
symptoms:
  - id: S1
    label: Ronronnement grondement augmente vitesse
    description: ronronnement grondement augmente vitesse
    risk_level: confort
    evidence:
      - 'Observation: ronronnement grondement augmente vitesse'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit qui change d intensite dans les virages
    description: bruit qui change d intensite dans les virages
    risk_level: confort
    evidence:
      - 'Observation: bruit qui change d intensite dans les virages'
      - Vérification visuelle ou auditive
  - id: S3
    label: Jeu perceptible en secouant la roue montee
    description: jeu perceptible en secouant la roue montee
    risk_level: confort
    evidence:
      - 'Observation: jeu perceptible en secouant la roue montee'
      - Vérification visuelle ou auditive
  - id: S4
    label: Vibrations dans le volant a certaines vitesses
    description: vibrations dans le volant a certaines vitesses
    risk_level: confort
    evidence:
      - 'Observation: vibrations dans le volant a certaines vitesses'
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
# Roulement de roue - Guide Diagnostic Complet

## Fonction et Rôle

Permettre la rotation libre de la roue sur son axe - Supporte les charges radiales et axiales

**Actions principales:** permettre la rotation, supporter, guider, rouler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- ronronnement grondement augmente vitesse
- bruit qui change d intensite dans les virages
- jeu perceptible en secouant la roue montee
- vibrations dans le volant a certaines vitesses
- roue anormalement chaude apres roulage
- bruit de frottement ou de craquement

## Procédure de Diagnostic

Pour diagnostiquer un problème de roulement de roue:

1. **Inspection visuelle** - Examiner l'état du roulement de roue
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-abs
- disque-de-frein
- plaquette-de-frein

## Critères de Compatibilité

Pour commander le bon roulement de roue, vous devez connaître:

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
