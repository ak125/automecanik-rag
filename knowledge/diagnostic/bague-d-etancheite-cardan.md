---
entity_type: gamme
title: Bague d'étanchéité cardan
slug: bague-d-etancheite-cardan
pg_id: 624
category: transmission
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Assurer l'etancheite de la transmission au niveau du cardan
  must_be_true:
    - assurer l'etancheite
    - empecher les fuites
  must_not_contain_concepts:
    - moteur
    - culasse
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_graisse-projetee-sur-la-roue
    then: verifier_piece
  - if: symptome_claquements-en-braquage
    then: diagnostic_approfondi
  - if: symptome_joint-homocinetique-bruyant
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Graisse projetee sur la roue
    description: graisse projetee sur la roue
    risk_level: confort
    evidence:
      - 'Observation: graisse projetee sur la roue'
      - Vérification visuelle ou auditive
  - id: S2
    label: Claquements en braquage
    description: claquements en braquage
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquements en braquage'
      - Vérification visuelle ou auditive
  - id: S3
    label: Joint homocinetique bruyant
    description: joint homocinetique bruyant
    risk_level: confort
    evidence:
      - 'Observation: joint homocinetique bruyant'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Bague d'étanchéité cardan - Guide Complet

## Fonction

Assurer l'etancheite de la transmission au niveau du cardan

## Symptômes de défaillance

### Graisse projetee sur la roue

graisse projetee sur la roue

### Claquements en braquage

claquements en braquage

### Joint homocinetique bruyant

joint homocinetique bruyant

## Diagnostic

Pour diagnostiquer un problème de bague d'étanchéité cardan:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- cardan

## Compatibilité

Pour commander le bon bague d'étanchéité cardan, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
