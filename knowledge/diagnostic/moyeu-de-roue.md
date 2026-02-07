---
entity_type: gamme
title: Moyeu de roue
slug: moyeu-de-roue
pg_id: 653
category: direction
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Supporter la roue et transmettre la rotation - Fixe la roue au roulement
  must_be_true:
    - supporter
    - fixer
    - transmettre
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
  - if: symptome_jeu-anormal-de-la-roue
    then: verifier_piece
  - if: symptome_vibrations-a-vitesse-constante
    then: diagnostic_approfondi
  - if: symptome_bruits-sourds-en-roulant
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Jeu anormal de la roue
    description: jeu anormal de la roue
    risk_level: confort
    evidence:
      - 'Observation: jeu anormal de la roue'
      - Vérification visuelle ou auditive
  - id: S2
    label: Vibrations a vitesse constante
    description: vibrations a vitesse constante
    risk_level: confort
    evidence:
      - 'Observation: vibrations a vitesse constante'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruits sourds en roulant
    description: bruits sourds en roulant
    risk_level: confort
    evidence:
      - 'Observation: bruits sourds en roulant'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Moyeu de roue - Guide Complet

## Fonction

Supporter la roue et transmettre la rotation - Fixe la roue au roulement

## Symptômes de défaillance

### Jeu anormal de la roue

jeu anormal de la roue

### Vibrations a vitesse constante

vibrations a vitesse constante

### Bruits sourds en roulant

bruits sourds en roulant

## Diagnostic

Pour diagnostiquer un problème de moyeu de roue:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- roulement-de-roue
- disque-de-frein

## Compatibilité

Pour commander le bon moyeu de roue, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
