---
entity_type: gamme
title: Barre stabilisatrice
slug: barre-stabilisatrice
pg_id: 274
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
    Limiter le roulis en virage - Relie les deux cotes de la suspension pour
    transferer les efforts
  must_be_true:
    - limiter le roulis
    - stabiliser
    - relier
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
  - if: symptome_roulis-excessif-en-virage
    then: verifier_piece
  - if: symptome_claquements-sur-route-degradee
    then: diagnostic_approfondi
  - if: symptome_bruits-sourds-en-compression
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Roulis excessif en virage
    description: roulis excessif en virage
    risk_level: confort
    evidence:
      - 'Observation: roulis excessif en virage'
      - Vérification visuelle ou auditive
  - id: S2
    label: Claquements sur route degradee
    description: claquements sur route degradee
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquements sur route degradee'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruits sourds en compression
    description: bruits sourds en compression
    risk_level: confort
    evidence:
      - 'Observation: bruits sourds en compression'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Barre stabilisatrice - Guide Complet

## Fonction

Limiter le roulis en virage - Relie les deux cotes de la suspension pour transferer les efforts

## Symptômes de défaillance

### Roulis excessif en virage

roulis excessif en virage

### Claquements sur route degradee

claquements sur route degradee

### Bruits sourds en compression

bruits sourds en compression

## Diagnostic

Pour diagnostiquer un problème de barre stabilisatrice:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- bras-de-suspension

## Compatibilité

Pour commander le bon barre stabilisatrice, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
