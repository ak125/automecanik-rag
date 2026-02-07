---
entity_type: gamme
title: Barre de direction
slug: barre-de-direction
pg_id: 285
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
    Relier la cremailliere aux rotules de direction - Transmet le mouvement
    lateral aux roues
  must_be_true:
    - relier
    - transmettre
    - connecter
  must_not_contain_concepts:
    - suspension
    - amortisseur
    - ressort
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_perceptible-volant-mouvement-reaction-roues
    then: verifier_piece
  - if: symptome_claquements-ou-cognements-en-tournant-le
    then: diagnostic_approfondi
  - if: symptome_direction-floue-ou-imprecise-a-haute
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Perceptible volant mouvement reaction roues
    description: perceptible volant mouvement reaction roues
    risk_level: confort
    evidence:
      - 'Observation: perceptible volant mouvement reaction roues'
      - Vérification visuelle ou auditive
  - id: S2
    label: Claquements ou cognements en tournant le
    description: claquements ou cognements en tournant le volant
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquements ou cognements en tournant le'
      - Vérification visuelle ou auditive
  - id: S3
    label: Direction floue ou imprecise a haute
    description: direction floue ou imprecise a haute vitesse
    risk_level: securite
    evidence:
      - 'Observation: direction floue ou imprecise a haute'
      - Vérification visuelle ou auditive
  - id: S4
    label: Usure asymetrique pneus avant interieur
    description: usure asymetrique pneus avant interieur
    risk_level: securite
    evidence:
      - 'Observation: usure asymetrique pneus avant interieur'
      - Vérification visuelle ou auditive
  - id: S5
    label: Vibrations dans le volant en ligne
    description: vibrations dans le volant en ligne droite
    risk_level: confort
    evidence:
      - 'Observation: vibrations dans le volant en ligne'
      - Vérification visuelle ou auditive
  - id: S6
    label: Controle technique refuse direction
    description: controle technique refuse direction
    risk_level: securite
    evidence:
      - 'Observation: controle technique refuse direction'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Barre de direction - Guide Complet

## Fonction

Relier la cremailliere aux rotules de direction - Transmet le mouvement lateral aux roues

## Symptômes de défaillance

### Perceptible volant mouvement reaction roues

perceptible volant mouvement reaction roues

### Claquements ou cognements en tournant le

claquements ou cognements en tournant le volant

### Direction floue ou imprecise a haute

direction floue ou imprecise a haute vitesse

### Usure asymetrique pneus avant interieur

usure asymetrique pneus avant interieur

### Vibrations dans le volant en ligne

vibrations dans le volant en ligne droite

### Controle technique refuse direction

controle technique refuse direction

## Diagnostic

Pour diagnostiquer un problème de barre de direction:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- bras-de-suspension
- cremailliere-de-direction
- rotule-de-direction
- soufflet-de-direction

## Compatibilité

Pour commander le bon barre de direction, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
