---
entity_type: gamme
title: Kit de poussoir culbuteur
slug: kit-de-poussoir-culbuteur
pg_id: 3320
category: moteur
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmettre le mouvement de l'arbre a cames aux soupapes
  must_be_true:
    - transmettre
    - actionner
    - lever
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
  - if: symptome_claquement-moteur-au-demarrage
    then: verifier_piece
  - if: symptome_bruit-qui-persiste-a-chaud
    then: diagnostic_approfondi
  - if: symptome_perte-de-puissance-legere
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Claquement moteur au demarrage
    description: claquement moteur au demarrage
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement moteur au demarrage'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit qui persiste a chaud
    description: bruit qui persiste a chaud
    risk_level: confort
    evidence:
      - 'Observation: bruit qui persiste a chaud'
      - Vérification visuelle ou auditive
  - id: S3
    label: Perte de puissance legere
    description: perte de puissance legere
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance legere'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Kit de poussoir culbuteur - Guide Complet

## Fonction

Transmettre le mouvement de l'arbre a cames aux soupapes

## Symptômes de défaillance

### Claquement moteur au demarrage

claquement moteur au demarrage

### Bruit qui persiste a chaud

bruit qui persiste a chaud

### Perte de puissance legere

perte de puissance legere

## Diagnostic

Pour diagnostiquer un problème de kit de poussoir culbuteur:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- arbre-a-came
- culbuteur
- poussoir-de-soupape
- soupape-d-admission
- soupape-d-echappement

## Compatibilité

Pour commander le bon kit de poussoir culbuteur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
