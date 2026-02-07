---
entity_type: gamme
title: Pompe de direction assistée
slug: pompe-de-direction-assistee
pg_id: 12
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
    Fournir la pression hydraulique pour assister l'effort de braquage - Reduit
    l'effort au volant
  must_be_true:
    - assister
    - fournir la pression
    - alimenter
  must_not_contain_concepts:
    - suspension
    - amortisseur
    - electrique
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_bruit-grognement-gemissement-tournant-volant
    then: verifier_piece
  - if: symptome_direction-dure-en-man-uvre-a
    then: diagnostic_approfondi
  - if: symptome_sifflement-aigu-au-demarrage-qui-s
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Bruit grognement gemissement tournant volant
    description: bruit grognement gemissement tournant volant
    risk_level: confort
    evidence:
      - 'Observation: bruit grognement gemissement tournant volant'
      - Vérification visuelle ou auditive
  - id: S2
    label: Direction dure en man uvre a
    description: direction dure en man uvre a basse vitesse
    risk_level: securite
    evidence:
      - 'Observation: direction dure en man uvre a'
      - Vérification visuelle ou auditive
  - id: S3
    label: Sifflement aigu au demarrage qui s
    description: sifflement aigu au demarrage qui s attenue
    risk_level: confort
    evidence:
      - 'Observation: sifflement aigu au demarrage qui s'
      - Vérification visuelle ou auditive
  - id: S4
    label: Mousse ou bulles dans le bocal
    description: mousse ou bulles dans le bocal de liquide
    risk_level: confort
    evidence:
      - 'Observation: mousse ou bulles dans le bocal'
      - Vérification visuelle ou auditive
  - id: S5
    label: Fuite de liquide au niveau de
    description: fuite de liquide au niveau de la pompe
    risk_level: confort
    evidence:
      - 'Observation: fuite de liquide au niveau de'
      - Vérification visuelle ou auditive
  - id: S6
    label: Niveau de liquide qui baisse regulierement
    description: niveau de liquide qui baisse regulierement
    risk_level: confort
    evidence:
      - 'Observation: niveau de liquide qui baisse regulierement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Pompe de direction assistée - Guide Complet

## Fonction

Fournir la pression hydraulique pour assister l'effort de braquage - Reduit l'effort au volant

## Symptômes de défaillance

### Bruit grognement gemissement tournant volant

bruit grognement gemissement tournant volant

### Direction dure en man uvre a

direction dure en man uvre a basse vitesse

### Sifflement aigu au demarrage qui s

sifflement aigu au demarrage qui s attenue

### Mousse ou bulles dans le bocal

mousse ou bulles dans le bocal de liquide

### Fuite de liquide au niveau de

fuite de liquide au niveau de la pompe

### Niveau de liquide qui baisse regulierement

niveau de liquide qui baisse regulierement

## Diagnostic

Pour diagnostiquer un problème de pompe de direction assistée:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- colonne-de-direction
- courroie-d-accessoire
- cremailliere-de-direction
- poulie-vilebrequin
- rotule-de-direction

## Compatibilité

Pour commander le bon pompe de direction assistée, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
