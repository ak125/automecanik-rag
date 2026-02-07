---
entity_type: gamme
title: Servo frein
slug: servo-frein
pg_id: 74
category: freinage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Amplifier l'effort de freinage grace a la depression moteur
  must_be_true:
    - amplifier
    - assister
    - demultiplier
  must_not_contain_concepts:
    - injection
    - climatisation
    - embrayage
    - distribution
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_pedale-de-frein-tres-dure-a
    then: verifier_piece
  - if: symptome_effort-au-freinage-anormalement-eleve
    then: diagnostic_approfondi
  - if: symptome_sifflement-au-niveau-de-la-pedale
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Pedale de frein tres dure a
    description: pedale de frein tres dure a enfoncer
    risk_level: securite
    evidence:
      - 'Observation: pedale de frein tres dure a'
      - Vérification visuelle ou auditive
  - id: S2
    label: Effort au freinage anormalement eleve
    description: effort au freinage anormalement eleve
    risk_level: securite
    evidence:
      - 'Observation: effort au freinage anormalement eleve'
      - Vérification visuelle ou auditive
  - id: S3
    label: Sifflement au niveau de la pedale
    description: sifflement au niveau de la pedale
    risk_level: confort
    evidence:
      - 'Observation: sifflement au niveau de la pedale'
      - Vérification visuelle ou auditive
  - id: S4
    label: Pedale qui vibre au freinage
    description: pedale qui vibre au freinage
    risk_level: securite
    evidence:
      - 'Observation: pedale qui vibre au freinage'
      - Vérification visuelle ou auditive
  - id: S5
    label: Moteur qui cale au freinage prise
    description: moteur qui cale au freinage prise d air
    risk_level: immobilisation
    evidence:
      - 'Observation: moteur qui cale au freinage prise'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Servo frein - Guide Complet

## Fonction

Amplifier l'effort de freinage grace a la depression moteur

## Symptômes de défaillance

### Pedale de frein tres dure a

pedale de frein tres dure a enfoncer

### Effort au freinage anormalement eleve

effort au freinage anormalement eleve

### Sifflement au niveau de la pedale

sifflement au niveau de la pedale

### Pedale qui vibre au freinage

pedale qui vibre au freinage

### Moteur qui cale au freinage prise

moteur qui cale au freinage prise d air

## Diagnostic

Pour diagnostiquer un problème de servo frein:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- agregat-de-freinage
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- etrier-de-frein

## Compatibilité

Pour commander le bon servo frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
