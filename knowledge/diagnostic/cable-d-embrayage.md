---
entity_type: gamme
title: Câble d'embrayage
slug: cable-d-embrayage
pg_id: 478
category: embrayage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmettre l'effort mécanique de la pédale vers la fourchette
  must_be_true:
    - transmettre l'effort
    - tirer
    - pousser
  must_not_contain_concepts:
    - disque
    - volant
    - couple
    - hydraulique
    - liquide
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_pedale-d-embrayage-dure-ou-difficile
    then: verifier_piece
  - if: symptome_point-de-patinage-tres-haut-ou
    then: diagnostic_approfondi
  - if: symptome_craquement-ou-grincement-en-appuyant-sur
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Pedale d embrayage dure ou difficile
    description: pedale d embrayage dure ou difficile a enfoncer
    risk_level: confort
    evidence:
      - 'Observation: pedale d embrayage dure ou difficile'
      - Vérification visuelle ou auditive
  - id: S2
    label: Point de patinage tres haut ou
    description: point de patinage tres haut ou tres bas
    risk_level: confort
    evidence:
      - 'Observation: point de patinage tres haut ou'
      - Vérification visuelle ou auditive
  - id: S3
    label: Craquement ou grincement en appuyant sur
    description: craquement ou grincement en appuyant sur la pedale
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: craquement ou grincement en appuyant sur'
      - Vérification visuelle ou auditive
  - id: S4
    label: Cable visible effiloche ou rouille
    description: cable visible effiloche ou rouille
    risk_level: confort
    evidence:
      - 'Observation: cable visible effiloche ou rouille'
      - Vérification visuelle ou auditive
  - id: S5
    label: Embrayage qui ne debraye pas completement
    description: embrayage qui ne debraye pas completement
    risk_level: confort
    evidence:
      - 'Observation: embrayage qui ne debraye pas completement'
      - Vérification visuelle ou auditive
  - id: S6
    label: Pedale qui reste enfoncee cable casse
    description: pedale qui reste enfoncee cable casse
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: pedale qui reste enfoncee cable casse'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Câble d'embrayage - Guide Complet

## Fonction

Transmettre l'effort mécanique de la pédale vers la fourchette

## Symptômes de défaillance

### Pedale d embrayage dure ou difficile

pedale d embrayage dure ou difficile a enfoncer

### Point de patinage tres haut ou

point de patinage tres haut ou tres bas

### Craquement ou grincement en appuyant sur

craquement ou grincement en appuyant sur la pedale

### Cable visible effiloche ou rouille

cable visible effiloche ou rouille

### Embrayage qui ne debraye pas completement

embrayage qui ne debraye pas completement

### Pedale qui reste enfoncee cable casse

pedale qui reste enfoncee cable casse

## Diagnostic

Pour diagnostiquer un problème de câble d'embrayage:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- butee-d-embrayage
- kit-d-embrayage
- volant-moteur

## Compatibilité

Pour commander le bon câble d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
