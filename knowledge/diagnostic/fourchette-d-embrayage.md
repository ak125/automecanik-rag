---
entity_type: gamme
title: Fourchette d'embrayage
slug: fourchette-d-embrayage
pg_id: 3419
category: embrayage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Actionner la butee d'embrayage via la commande
  must_be_true:
    - actionner
    - pousser
    - deplacer
  must_not_contain_concepts:
    - injection
    - freinage
    - climatisation
    - turbo
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_pedale-d-embrayage-dure
    then: verifier_piece
  - if: symptome_difficulte-a-passer-les-vitesses
    then: diagnostic_approfondi
  - if: symptome_bruit-de-claquement-a-l-embrayage
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Pedale d embrayage dure
    description: pedale d embrayage dure
    risk_level: confort
    evidence:
      - 'Observation: pedale d embrayage dure'
      - Vérification visuelle ou auditive
  - id: S2
    label: Difficulte a passer les vitesses
    description: difficulte a passer les vitesses
    risk_level: confort
    evidence:
      - 'Observation: difficulte a passer les vitesses'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit de claquement a l embrayage
    description: bruit de claquement a l embrayage
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit de claquement a l embrayage'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Fourchette d'embrayage - Guide Complet

## Fonction

Actionner la butee d'embrayage via la commande

## Symptômes de défaillance

### Pedale d embrayage dure

pedale d embrayage dure

### Difficulte a passer les vitesses

difficulte a passer les vitesses

### Bruit de claquement a l embrayage

bruit de claquement a l embrayage

## Diagnostic

Pour diagnostiquer un problème de fourchette d'embrayage:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- guide-d-embrayage
- tringle-de-vitesses

## Compatibilité

Pour commander le bon fourchette d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
