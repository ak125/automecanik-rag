---
entity_type: gamme
title: Palier d'arbre de transmission
slug: palier-d-arbre-de-transmission
pg_id: 2109
category: transmission
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Supporter et guider l'arbre de transmission en rotation
  must_be_true:
    - supporter
    - guider
    - centrer
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
  - if: symptome_bruit-de-roulement-sous-le-vehicule
    then: diagnostic_approfondi
  - if: symptome_jeu-perceptible-au-palier
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
    label: Bruit de roulement sous le vehicule
    description: bruit de roulement sous le vehicule
    risk_level: confort
    evidence:
      - 'Observation: bruit de roulement sous le vehicule'
      - Vérification visuelle ou auditive
  - id: S3
    label: Jeu perceptible au palier
    description: jeu perceptible au palier
    risk_level: confort
    evidence:
      - 'Observation: jeu perceptible au palier'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Palier d'arbre de transmission - Guide Complet

## Fonction

Supporter et guider l'arbre de transmission en rotation

## Symptômes de défaillance

### Vibrations a vitesse constante

vibrations a vitesse constante

### Bruit de roulement sous le vehicule

bruit de roulement sous le vehicule

### Jeu perceptible au palier

jeu perceptible au palier

## Diagnostic

Pour diagnostiquer un problème de palier d'arbre de transmission:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- cardan
- roulement

## Compatibilité

Pour commander le bon palier d'arbre de transmission, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
