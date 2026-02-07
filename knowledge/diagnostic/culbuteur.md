---
entity_type: gamme
title: Culbuteur
slug: culbuteur
pg_id: 432
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
    - basculer
    - actionner
  must_not_contain_concepts:
    - boite de vitesses
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_claquement-moteur-regulier
    then: verifier_piece
  - if: symptome_bruit-de-tic-tic-au-ralenti
    then: diagnostic_approfondi
  - if: symptome_perte-de-puissance-sur-un-cylindre
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Claquement moteur regulier
    description: claquement moteur regulier
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement moteur regulier'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit de tic-tic au ralenti
    description: bruit de tic-tic au ralenti
    risk_level: confort
    evidence:
      - 'Observation: bruit de tic-tic au ralenti'
      - Vérification visuelle ou auditive
  - id: S3
    label: Perte de puissance sur un cylindre
    description: perte de puissance sur un cylindre
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance sur un cylindre'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Culbuteur - Guide Complet

## Fonction

Transmettre le mouvement de l'arbre a cames aux soupapes

## Symptômes de défaillance

### Claquement moteur regulier

claquement moteur regulier

### Bruit de tic-tic au ralenti

bruit de tic-tic au ralenti

### Perte de puissance sur un cylindre

perte de puissance sur un cylindre

## Diagnostic

Pour diagnostiquer un problème de culbuteur:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- arbre-a-came
- kit-de-poussoir-culbuteur
- poussoir-de-soupape
- soupape-d-admission
- soupape-d-echappement

## Compatibilité

Pour commander le bon culbuteur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
