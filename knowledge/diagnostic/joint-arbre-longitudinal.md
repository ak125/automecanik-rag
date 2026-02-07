---
entity_type: gamme
title: Joint arbre longitudinal
slug: joint-arbre-longitudinal
pg_id: 1427
category: transmission
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmettre le couple entre les elements de transmission
  must_be_true:
    - transmettre
    - articuler
    - relier
  must_not_contain_concepts:
    - injection
    - freinage
    - climatisation
    - allumage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_vibrations-a-vitesse-constante
    then: verifier_piece
  - if: symptome_claquements-en-acceleration-deceleration
    then: diagnostic_approfondi
  - if: symptome_bruits-de-roulement-sous-le-vehicule
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Vibrations a vitesse constante
    description: vibrations a vitesse constante
    risk_level: confort
    evidence:
      - 'Observation: vibrations a vitesse constante'
      - Vérification visuelle ou auditive
  - id: S2
    label: Claquements en acceleration deceleration
    description: claquements en acceleration deceleration
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquements en acceleration deceleration'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruits de roulement sous le vehicule
    description: bruits de roulement sous le vehicule
    risk_level: confort
    evidence:
      - 'Observation: bruits de roulement sous le vehicule'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Joint arbre longitudinal - Guide Complet

## Fonction

Transmettre le couple entre les elements de transmission

## Symptômes de défaillance

### Vibrations a vitesse constante

vibrations a vitesse constante

### Claquements en acceleration deceleration

claquements en acceleration deceleration

### Bruits de roulement sous le vehicule

bruits de roulement sous le vehicule

## Diagnostic

Pour diagnostiquer un problème de joint arbre longitudinal:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- cardan
- soufflet-de-cardan

## Compatibilité

Pour commander le bon joint arbre longitudinal, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
