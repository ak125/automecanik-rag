---
entity_type: gamme
title: Arbre à came
slug: arbre-a-came
pg_id: 566
category: moteur
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Commander l'ouverture et la fermeture des soupapes
  must_be_true:
    - commander
    - synchroniser
    - actionner les soupapes
  must_not_contain_concepts:
    - vilebrequin
    - boite de vitesses
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_bruit-moteur
    then: verifier_piece
  - if: symptome_claquement
    then: diagnostic_approfondi
  - if: symptome_perte-puissance
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Bruit moteur
    description: bruit moteur
    risk_level: confort
    evidence:
      - 'Observation: bruit moteur'
      - Vérification visuelle ou auditive
  - id: S2
    label: Claquement
    description: claquement
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement'
      - Vérification visuelle ou auditive
  - id: S3
    label: Perte puissance
    description: perte puissance
    risk_level: confort
    evidence:
      - 'Observation: perte puissance'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Arbre à came - Guide Complet

## Fonction

Commander l'ouverture et la fermeture des soupapes

## Symptômes de défaillance

### Bruit moteur

bruit moteur

### Claquement

claquement

### Perte puissance

perte puissance

## Diagnostic

Pour diagnostiquer un problème de arbre à came:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- courroie-de-distribution
- culbuteur
- kit-de-poussoir-culbuteur
- poulie-d-arbre-a-came
- poussoir-de-soupape

## Compatibilité

Pour commander le bon arbre à came, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
