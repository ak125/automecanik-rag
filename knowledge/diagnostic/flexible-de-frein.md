---
entity_type: gamme
title: Flexible de frein
slug: flexible-de-frein
pg_id: 83
category: freinage
subcategory: flexibles
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmettre la pression hydraulique entre les elements mobiles
  must_be_true:
    - transmettre la pression
    - acheminer le liquide
    - resister a la pression
  must_not_contain_concepts:
    - friction
    - thermique
    - electronique
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_craquelures-ou-fissures-visibles-sur-le
    then: verifier_piece
  - if: symptome_gonflement-flexible-lors-appui-pedale
    then: diagnostic_approfondi
  - if: symptome_fuite-de-liquide-de-frein-au
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Craquelures ou fissures visibles sur le
    description: craquelures ou fissures visibles sur le flexible
    risk_level: confort
    evidence:
      - 'Observation: craquelures ou fissures visibles sur le'
      - Vérification visuelle ou auditive
  - id: S2
    label: Gonflement flexible lors appui pedale
    description: gonflement flexible lors appui pedale
    risk_level: confort
    evidence:
      - 'Observation: gonflement flexible lors appui pedale'
      - Vérification visuelle ou auditive
  - id: S3
    label: Fuite de liquide de frein au
    description: fuite de liquide de frein au niveau du flexible
    risk_level: securite
    evidence:
      - 'Observation: fuite de liquide de frein au'
      - Vérification visuelle ou auditive
  - id: S4
    label: Pedale de frein spongieuse ou molle
    description: pedale de frein spongieuse ou molle
    risk_level: securite
    evidence:
      - 'Observation: pedale de frein spongieuse ou molle'
      - Vérification visuelle ou auditive
  - id: S5
    label: Freinage qui tire d un cote
    description: freinage qui tire d un cote flexible bouche
    risk_level: securite
    evidence:
      - 'Observation: freinage qui tire d un cote'
      - Vérification visuelle ou auditive
  - id: S6
    label: Sifflement bruit niveau flexible sous
    description: sifflement bruit niveau flexible sous
    risk_level: confort
    evidence:
      - 'Observation: sifflement bruit niveau flexible sous'
      - Vérification visuelle ou auditive
  - id: S7
    label: Odeur de liquide de frein fuite
    description: odeur de liquide de frein fuite
    risk_level: securite
    evidence:
      - 'Observation: odeur de liquide de frein fuite'
      - Vérification visuelle ou auditive
  - id: S8
    label: Plus depuis dernier changement flexibles
    description: plus depuis dernier changement flexibles
    risk_level: confort
    evidence:
      - 'Observation: plus depuis dernier changement flexibles'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Flexible de frein - Guide Complet

## Fonction

Transmettre la pression hydraulique entre les elements mobiles

## Symptômes de défaillance

### Craquelures ou fissures visibles sur le

craquelures ou fissures visibles sur le flexible

### Gonflement flexible lors appui pedale

gonflement flexible lors appui pedale

### Fuite de liquide de frein au

fuite de liquide de frein au niveau du flexible

### Pedale de frein spongieuse ou molle

pedale de frein spongieuse ou molle

### Freinage qui tire d un cote

freinage qui tire d un cote flexible bouche

### Sifflement bruit niveau flexible sous

sifflement bruit niveau flexible sous

### Odeur de liquide de frein fuite

odeur de liquide de frein fuite

### Plus depuis dernier changement flexibles

plus depuis dernier changement flexibles

## Diagnostic

Pour diagnostiquer un problème de flexible de frein:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- capteur-abs
- cylindre-de-roue
- disque-de-frein
- etrier-de-frein
- interrupteur-des-feux-de-freins

## Compatibilité

Pour commander le bon flexible de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
