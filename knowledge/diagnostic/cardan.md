---
entity_type: gamme
title: Cardan
slug: cardan
pg_id: 13
category: transmission
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Transmet le couple moteur aux roues tout en permettant les mouvements de
    suspension
  must_be_true:
    - transmettre
    - entrainer
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
  - if: symptome_claquement-braquant-accelerant-marche-arriere
    then: verifier_piece
  - if: symptome_vibrations-ressenties-vitesse-constante
    then: diagnostic_approfondi
  - if: symptome_graisse-noire-visible-jante-passage
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Claquement braquant accelerant marche arriere
    description: claquement braquant accelerant marche arriere
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement braquant accelerant marche arriere'
      - Vérification visuelle ou auditive
  - id: S2
    label: Vibrations ressenties vitesse constante
    description: vibrations ressenties vitesse constante
    risk_level: confort
    evidence:
      - 'Observation: vibrations ressenties vitesse constante'
      - Vérification visuelle ou auditive
  - id: S3
    label: Graisse noire visible jante passage
    description: graisse noire visible jante passage
    risk_level: confort
    evidence:
      - 'Observation: graisse noire visible jante passage'
      - Vérification visuelle ou auditive
  - id: S4
    label: Soufflet de cardan dechire ou fendu
    description: soufflet de cardan dechire ou fendu visible
    risk_level: confort
    evidence:
      - 'Observation: soufflet de cardan dechire ou fendu'
      - Vérification visuelle ou auditive
  - id: S5
    label: Bruit roulement change selon angle
    description: bruit roulement change selon angle
    risk_level: confort
    evidence:
      - 'Observation: bruit roulement change selon angle'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 150 000 km sans
    description: plus de 150 000 km sans verification des soufflets
    risk_level: confort
    evidence:
      - 'Observation: plus de 150 000 km sans'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Cardan - Guide Complet

## Fonction

Transmet le couple moteur aux roues tout en permettant les mouvements de suspension

## Symptômes de défaillance

### Claquement braquant accelerant marche arriere

claquement braquant accelerant marche arriere

### Vibrations ressenties vitesse constante

vibrations ressenties vitesse constante

### Graisse noire visible jante passage

graisse noire visible jante passage

### Soufflet de cardan dechire ou fendu

soufflet de cardan dechire ou fendu visible

### Bruit roulement change selon angle

bruit roulement change selon angle

### Plus de 150 000 km sans

plus de 150 000 km sans verification des soufflets

## Diagnostic

Pour diagnostiquer un problème de cardan:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- bague-d-etancheite-cardan
- soufflet-de-cardan

## Compatibilité

Pour commander le bon cardan, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
