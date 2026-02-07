---
entity_type: gamme
title: Plaquette de frein
slug: plaquette-de-frein
pg_id: 402
category: freinage
subcategory: plaquettes
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Creer la friction contre le disque pour ralentir le vehicule
  must_be_true:
    - freiner
    - creer la friction
    - ralentir le vehicule
  must_not_contain_concepts:
    - tambour
    - machoire
    - hydraulique
    - pression
    - universel
    - tous véhicules
    - adaptable tous
  confusion_with:
    disque-de-frein:
      key_difference: >-
        Plaquettes = garnitures qui s'usent, Disques = surfaces de friction à
        contrôler
    machoire-de-frein:
      key_difference: 'Plaquettes = freins à disque, Mâchoires = freins à tambour'
diagnostic_tree:
  - if: symptome_sifflement-metallique-au-freinage-temoin-d
    then: verifier_piece
  - if: symptome_voyant-frein-allume-au-tableau-de
    then: diagnostic_approfondi
  - if: symptome_epaisseur-visible-inferieure-travers-jante
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Sifflement metallique au freinage temoin d
    description: sifflement metallique au freinage temoin d usure
    risk_level: securite
    evidence:
      - 'Observation: sifflement metallique au freinage temoin d'
      - Vérification visuelle ou auditive
  - id: S2
    label: Voyant frein allume au tableau de
    description: voyant frein allume au tableau de bord
    risk_level: securite
    evidence:
      - 'Observation: voyant frein allume au tableau de'
      - Vérification visuelle ou auditive
  - id: S3
    label: Epaisseur visible inferieure travers jante
    description: epaisseur visible inferieure travers jante
    risk_level: confort
    evidence:
      - 'Observation: epaisseur visible inferieure travers jante'
      - Vérification visuelle ou auditive
  - id: S4
    label: Distances de freinage allongees
    description: distances de freinage allongees
    risk_level: securite
    evidence:
      - 'Observation: distances de freinage allongees'
      - Vérification visuelle ou auditive
  - id: S5
    label: Pedale de frein qui s enfonce
    description: pedale de frein qui s enfonce plus que d habitude
    risk_level: securite
    evidence:
      - 'Observation: pedale de frein qui s enfonce'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 30 000 km depuis
    description: plus de 30 000 km depuis le dernier changement
    risk_level: confort
    evidence:
      - 'Observation: plus de 30 000 km depuis'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous véhicules
    - adaptable tous
---
# Plaquette de frein - Guide Complet

## Fonction

Creer la friction contre le disque pour ralentir le vehicule

## Symptômes de défaillance

### Sifflement metallique au freinage temoin d

sifflement metallique au freinage temoin d usure

### Voyant frein allume au tableau de

voyant frein allume au tableau de bord

### Epaisseur visible inferieure travers jante

epaisseur visible inferieure travers jante

### Distances de freinage allongees

distances de freinage allongees

### Pedale de frein qui s enfonce

pedale de frein qui s enfonce plus que d habitude

### Plus de 30 000 km depuis

plus de 30 000 km depuis le dernier changement

## Diagnostic

Pour diagnostiquer un problème de plaquette de frein:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- cable-de-frein-a-main
- capteur-abs
- disque-de-frein
- etrier-de-frein
- interrupteur-des-feux-de-freins

## Ne pas confondre avec

| Pièce confondue | Distinction |
|-----------------|-------------|
| disque-de-frein | Plaquettes = garnitures qui s'usent, Disques = surfaces de friction à contrôler |
| machoire-de-frein | Plaquettes = freins à disque, Mâchoires = freins à tambour |

## Compatibilité

Pour commander le bon plaquette de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule
- **Position** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "sécurité garantie"
- ❌ "arrêt immédiat"
- ❌ "zéro accident"
- ❌ "garanti CT"
