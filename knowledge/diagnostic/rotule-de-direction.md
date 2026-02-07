---
entity_type: gamme
title: Rotule de direction
slug: rotule-de-direction
pg_id: 2066
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
    Articuler la barre de direction et la fusee - Permet le braquage. NE
    SUPPORTE PAS LA CHARGE!
  must_be_true:
    - orienter
    - transmettre le mouvement
    - articuler
  must_not_contain_concepts:
    - suspension
    - bras
    - triangle
    - charge
    - poids
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_jeu-perceptible-dans-le-volant
    then: verifier_piece
  - if: symptome_claquements-en-tournant-a-basse-vitesse
    then: diagnostic_approfondi
  - if: symptome_direction-imprecise-ou-floue
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Jeu perceptible dans le volant
    description: jeu perceptible dans le volant
    risk_level: confort
    evidence:
      - 'Observation: jeu perceptible dans le volant'
      - Vérification visuelle ou auditive
  - id: S2
    label: Claquements en tournant a basse vitesse
    description: claquements en tournant a basse vitesse
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquements en tournant a basse vitesse'
      - Vérification visuelle ou auditive
  - id: S3
    label: Direction imprecise ou floue
    description: direction imprecise ou floue
    risk_level: securite
    evidence:
      - 'Observation: direction imprecise ou floue'
      - Vérification visuelle ou auditive
  - id: S4
    label: Usure asymetrique des pneus avant
    description: usure asymetrique des pneus avant
    risk_level: securite
    evidence:
      - 'Observation: usure asymetrique des pneus avant'
      - Vérification visuelle ou auditive
  - id: S5
    label: Soufflet de rotule dechire ou graisse
    description: soufflet de rotule dechire ou graisse visible
    risk_level: confort
    evidence:
      - 'Observation: soufflet de rotule dechire ou graisse'
      - Vérification visuelle ou auditive
  - id: S6
    label: Controle technique refuse pour jeu aux
    description: controle technique refuse pour jeu aux trains
    risk_level: confort
    evidence:
      - 'Observation: controle technique refuse pour jeu aux'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Rotule de direction - Guide Complet

## Fonction

Articuler la barre de direction et la fusee - Permet le braquage. NE SUPPORTE PAS LA CHARGE!

## Symptômes de défaillance

### Jeu perceptible dans le volant

jeu perceptible dans le volant

### Claquements en tournant a basse vitesse

claquements en tournant a basse vitesse

### Direction imprecise ou floue

direction imprecise ou floue

### Usure asymetrique des pneus avant

usure asymetrique des pneus avant

### Soufflet de rotule dechire ou graisse

soufflet de rotule dechire ou graisse visible

### Controle technique refuse pour jeu aux

controle technique refuse pour jeu aux trains

## Diagnostic

Pour diagnostiquer un problème de rotule de direction:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- amortisseur
- barre-de-direction
- bras-de-suspension
- cremailliere-de-direction
- pompe-de-direction-assistee

## Compatibilité

Pour commander le bon rotule de direction, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
