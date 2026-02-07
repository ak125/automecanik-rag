---
entity_type: gamme
title: Colonne de direction
slug: colonne-de-direction
pg_id: 1211
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
    Relier le volant a la cremailliere - Transmet la rotation du conducteur au
    systeme de direction
  must_be_true:
    - relier
    - transmettre
    - connecter
  must_not_contain_concepts:
    - suspension
    - amortissement
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_jeu-important-du-volant-vertical-ou
    then: verifier_piece
  - if: symptome_craquements-ou-bruits-secs-en-tournant
    then: diagnostic_approfondi
  - if: symptome_volant-qui-ne-revient-pas-seul
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Jeu important du volant vertical ou
    description: jeu important du volant vertical ou lateral
    risk_level: confort
    evidence:
      - 'Observation: jeu important du volant vertical ou'
      - Vérification visuelle ou auditive
  - id: S2
    label: Craquements ou bruits secs en tournant
    description: craquements ou bruits secs en tournant le volant
    risk_level: confort
    evidence:
      - 'Observation: craquements ou bruits secs en tournant'
      - Vérification visuelle ou auditive
  - id: S3
    label: Volant qui ne revient pas seul
    description: volant qui ne revient pas seul apres un virage
    risk_level: confort
    evidence:
      - 'Observation: volant qui ne revient pas seul'
      - Vérification visuelle ou auditive
  - id: S4
    label: Bruits de frottement dans la colonne
    description: bruits de frottement dans la colonne
    risk_level: confort
    evidence:
      - 'Observation: bruits de frottement dans la colonne'
      - Vérification visuelle ou auditive
  - id: S5
    label: Voyant direction assistee allume
    description: voyant direction assistee allume
    risk_level: securite
    evidence:
      - 'Observation: voyant direction assistee allume'
      - Vérification visuelle ou auditive
  - id: S6
    label: Sensation de points durs en tournant
    description: sensation de points durs en tournant
    risk_level: confort
    evidence:
      - 'Observation: sensation de points durs en tournant'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Colonne de direction - Guide Complet

## Fonction

Relier le volant a la cremailliere - Transmet la rotation du conducteur au systeme de direction

## Symptômes de défaillance

### Jeu important du volant vertical ou

jeu important du volant vertical ou lateral

### Craquements ou bruits secs en tournant

craquements ou bruits secs en tournant le volant

### Volant qui ne revient pas seul

volant qui ne revient pas seul apres un virage

### Bruits de frottement dans la colonne

bruits de frottement dans la colonne

### Voyant direction assistee allume

voyant direction assistee allume

### Sensation de points durs en tournant

sensation de points durs en tournant

## Diagnostic

Pour diagnostiquer un problème de colonne de direction:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- cremailliere-de-direction
- pompe-de-direction-assistee
- rotule-de-direction

## Compatibilité

Pour commander le bon colonne de direction, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
