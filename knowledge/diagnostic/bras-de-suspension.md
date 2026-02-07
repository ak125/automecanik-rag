---
entity_type: gamme
title: Bras de suspension
slug: bras-de-suspension
pg_id: 273
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
    Maintenir la geometrie de la roue et supporter les efforts verticaux -
    Element structurel de la suspension
  must_be_true:
    - maintenir
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
  - if: symptome_claquements-ou-cognements-sur-routes-degradees
    then: verifier_piece
  - if: symptome_vehicule-qui-tire-a-droite-ou
    then: diagnostic_approfondi
  - if: symptome_usure-irreguliere-pneus-epaules-interieures
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Claquements ou cognements sur routes degradees
    description: claquements ou cognements sur routes degradees
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquements ou cognements sur routes degradees'
      - Vérification visuelle ou auditive
  - id: S2
    label: Vehicule qui tire a droite ou
    description: vehicule qui tire a droite ou a gauche au freinage
    risk_level: securite
    evidence:
      - 'Observation: vehicule qui tire a droite ou'
      - Vérification visuelle ou auditive
  - id: S3
    label: Usure irreguliere pneus epaules interieures
    description: usure irreguliere pneus epaules interieures
    risk_level: securite
    evidence:
      - 'Observation: usure irreguliere pneus epaules interieures'
      - Vérification visuelle ou auditive
  - id: S4
    label: Vibrations dans le volant a certaines
    description: vibrations dans le volant a certaines vitesses
    risk_level: confort
    evidence:
      - 'Observation: vibrations dans le volant a certaines'
      - Vérification visuelle ou auditive
  - id: S5
    label: Silentblocs fissures ou decolles visibles
    description: silentblocs fissures ou decolles visibles
    risk_level: confort
    evidence:
      - 'Observation: silentblocs fissures ou decolles visibles'
      - Vérification visuelle ou auditive
  - id: S6
    label: Tenue de route degradee en virage
    description: tenue de route degradee en virage
    risk_level: confort
    evidence:
      - 'Observation: tenue de route degradee en virage'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Bras de suspension - Guide Complet

## Fonction

Maintenir la geometrie de la roue et supporter les efforts verticaux - Element structurel de la suspension

## Symptômes de défaillance

### Claquements ou cognements sur routes degradees

claquements ou cognements sur routes degradees

### Vehicule qui tire a droite ou

vehicule qui tire a droite ou a gauche au freinage

### Usure irreguliere pneus epaules interieures

usure irreguliere pneus epaules interieures

### Vibrations dans le volant a certaines

vibrations dans le volant a certaines vitesses

### Silentblocs fissures ou decolles visibles

silentblocs fissures ou decolles visibles

### Tenue de route degradee en virage

tenue de route degradee en virage

## Diagnostic

Pour diagnostiquer un problème de bras de suspension:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- amortisseur
- barre-de-direction
- biellette-de-barre-stabilisatrice
- rotule-de-direction
- rotule-de-suspension

## Compatibilité

Pour commander le bon bras de suspension, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
