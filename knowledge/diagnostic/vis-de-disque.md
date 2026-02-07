---
entity_type: gamme
title: Vis de disque
slug: vis-de-disque
pg_id: 54
category: freinage
subcategory: disques
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Fixer le disque de frein sur le moyeu de roue
  must_be_true:
    - fixer
    - maintenir
    - bloquer
  must_not_contain_concepts:
    - injection
    - climatisation
    - embrayage
    - distribution
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_vis-grippee-impossible-a-devisser
    then: verifier_piece
  - if: symptome_tete-de-vis-arrondie-ou-endommagee
    then: diagnostic_approfondi
  - if: symptome_vis-rouillee-visible-a-travers-la
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Vis grippee impossible a devisser
    description: vis grippee impossible a devisser
    risk_level: confort
    evidence:
      - 'Observation: vis grippee impossible a devisser'
      - Vérification visuelle ou auditive
  - id: S2
    label: Tete de vis arrondie ou endommagee
    description: tete de vis arrondie ou endommagee
    risk_level: confort
    evidence:
      - 'Observation: tete de vis arrondie ou endommagee'
      - Vérification visuelle ou auditive
  - id: S3
    label: Vis rouillee visible a travers la
    description: vis rouillee visible a travers la jante
    risk_level: confort
    evidence:
      - 'Observation: vis rouillee visible a travers la'
      - Vérification visuelle ou auditive
  - id: S4
    label: Disque qui bouge legerement vis desserree
    description: disque qui bouge legerement vis desserree
    risk_level: confort
    evidence:
      - 'Observation: disque qui bouge legerement vis desserree'
      - Vérification visuelle ou auditive
  - id: S5
    label: Bruit claquement freinage cassee absente
    description: bruit claquement freinage cassee absente
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit claquement freinage cassee absente'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Vis de disque - Guide Complet

## Fonction

Fixer le disque de frein sur le moyeu de roue

## Symptômes de défaillance

### Vis grippee impossible a devisser

vis grippee impossible a devisser

### Tete de vis arrondie ou endommagee

tete de vis arrondie ou endommagee

### Vis rouillee visible a travers la

vis rouillee visible a travers la jante

### Disque qui bouge legerement vis desserree

disque qui bouge legerement vis desserree

### Bruit claquement freinage cassee absente

bruit claquement freinage cassee absente

## Diagnostic

Pour diagnostiquer un problème de vis de disque:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- disque-de-frein

## Compatibilité

Pour commander le bon vis de disque, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
