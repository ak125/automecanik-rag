---
entity_type: gamme
title: Étrier de frein
slug: etrier-de-frein
pg_id: 78
category: freinage
subcategory: etriers
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Appliquer la pression hydraulique sur les plaquettes
  must_be_true:
    - appliquer la pression
    - maintenir les plaquettes
    - serrer
  must_not_contain_concepts:
    - tambour
    - machoire
    - thermique
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_usure-asymetrique-plaquettes-plus-usee
    then: verifier_piece
  - if: symptome_vehicule-qui-tire-d-un-cote
    then: diagnostic_approfondi
  - if: symptome_roue-anormalement-chaude-apres-roulage
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Usure asymetrique plaquettes plus usee
    description: usure asymetrique plaquettes plus usee
    risk_level: confort
    evidence:
      - 'Observation: usure asymetrique plaquettes plus usee'
      - Vérification visuelle ou auditive
  - id: S2
    label: Vehicule qui tire d un cote
    description: vehicule qui tire d un cote au freinage
    risk_level: securite
    evidence:
      - 'Observation: vehicule qui tire d un cote'
      - Vérification visuelle ou auditive
  - id: S3
    label: Roue anormalement chaude apres roulage
    description: roue anormalement chaude apres roulage
    risk_level: confort
    evidence:
      - 'Observation: roue anormalement chaude apres roulage'
      - Vérification visuelle ou auditive
  - id: S4
    label: Fuite de liquide de frein au
    description: fuite de liquide de frein au niveau de l etrier
    risk_level: securite
    evidence:
      - 'Observation: fuite de liquide de frein au'
      - Vérification visuelle ou auditive
  - id: S5
    label: Pedale de frein dure ou spongieuse
    description: pedale de frein dure ou spongieuse
    risk_level: securite
    evidence:
      - 'Observation: pedale de frein dure ou spongieuse'
      - Vérification visuelle ou auditive
  - id: S6
    label: Bruit de frottement permanent piston grippe
    description: bruit de frottement permanent piston grippe
    risk_level: confort
    evidence:
      - 'Observation: bruit de frottement permanent piston grippe'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Étrier de frein - Guide Complet

## Fonction

Appliquer la pression hydraulique sur les plaquettes

## Symptômes de défaillance

### Usure asymetrique plaquettes plus usee

usure asymetrique plaquettes plus usee

### Vehicule qui tire d un cote

vehicule qui tire d un cote au freinage

### Roue anormalement chaude apres roulage

roue anormalement chaude apres roulage

### Fuite de liquide de frein au

fuite de liquide de frein au niveau de l etrier

### Pedale de frein dure ou spongieuse

pedale de frein dure ou spongieuse

### Bruit de frottement permanent piston grippe

bruit de frottement permanent piston grippe

## Diagnostic

Pour diagnostiquer un problème de étrier de frein:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- cable-de-frein-a-main
- capteur-abs
- disque-de-frein
- flexible-de-frein
- interrupteur-des-feux-de-freins

## Compatibilité

Pour commander le bon étrier de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
