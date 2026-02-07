---
entity_type: gamme
title: Joint tige de soupape
slug: joint-tige-de-soupape
pg_id: 322
category: moteur
subcategory: joints
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Empecher l'huile de descendre dans la chambre de combustion
  must_be_true:
    - assurer l'etancheite
    - empecher
  must_not_contain_concepts:
    - freinage
    - climatisation
    - direction
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_fumee-bleue-au-demarrage
    then: verifier_piece
  - if: symptome_consommation-d-huile-excessive
    then: diagnostic_approfondi
  - if: symptome_depots-sur-les-bougies
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Fumee bleue au demarrage
    description: fumee bleue au demarrage
    risk_level: confort
    evidence:
      - 'Observation: fumee bleue au demarrage'
      - Vérification visuelle ou auditive
  - id: S2
    label: Consommation d huile excessive
    description: consommation d huile excessive
    risk_level: confort
    evidence:
      - 'Observation: consommation d huile excessive'
      - Vérification visuelle ou auditive
  - id: S3
    label: Depots sur les bougies
    description: depots sur les bougies
    risk_level: confort
    evidence:
      - 'Observation: depots sur les bougies'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Joint tige de soupape - Guide Complet

## Fonction

Empecher l'huile de descendre dans la chambre de combustion

## Symptômes de défaillance

### Fumee bleue au demarrage

fumee bleue au demarrage

### Consommation d huile excessive

consommation d huile excessive

### Depots sur les bougies

depots sur les bougies

## Diagnostic

Pour diagnostiquer un problème de joint tige de soupape:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- bagues-d-etancheite-moteur
- joint-de-cache-culbuteurs
- joint-de-carter-d-huile
- joint-de-collecteur
- joint-de-culasse

## Compatibilité

Pour commander le bon joint tige de soupape, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
