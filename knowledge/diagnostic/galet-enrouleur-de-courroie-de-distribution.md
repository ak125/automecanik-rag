---
entity_type: gamme
title: Galet enrouleur de courroie de distribution
slug: galet-enrouleur-de-courroie-de-distribution
pg_id: 313
category: distribution
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Guider la courroie de distribution dans son parcours
  must_be_true:
    - guider
    - enrouler
    - positionner
  must_not_contain_concepts:
    - freinage
    - climatisation
    - turbo
    - injection
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_bruit-de-roulement-au-ralenti
    then: verifier_piece
  - if: symptome_sifflement-cote-distribution
    then: diagnostic_approfondi
  - if: symptome_traces-d-usure-anormale-sur-la
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Bruit de roulement au ralenti
    description: bruit de roulement au ralenti
    risk_level: confort
    evidence:
      - 'Observation: bruit de roulement au ralenti'
      - Vérification visuelle ou auditive
  - id: S2
    label: Sifflement cote distribution
    description: sifflement cote distribution
    risk_level: confort
    evidence:
      - 'Observation: sifflement cote distribution'
      - Vérification visuelle ou auditive
  - id: S3
    label: Traces d usure anormale sur la
    description: traces d usure anormale sur la courroie
    risk_level: confort
    evidence:
      - 'Observation: traces d usure anormale sur la'
      - Vérification visuelle ou auditive
  - id: S4
    label: Galet qui tourne difficilement a la
    description: galet qui tourne difficilement a la main
    risk_level: confort
    evidence:
      - 'Observation: galet qui tourne difficilement a la'
      - Vérification visuelle ou auditive
  - id: S5
    label: Jeu radial ou axial dans le
    description: jeu radial ou axial dans le galet
    risk_level: confort
    evidence:
      - 'Observation: jeu radial ou axial dans le'
      - Vérification visuelle ou auditive
  - id: S6
    label: Bruit metallique leger
    description: bruit metallique leger
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit metallique leger'
      - Vérification visuelle ou auditive
  - id: S7
    label: Courroie qui se deporte sur le
    description: courroie qui se deporte sur le cote
    risk_level: confort
    evidence:
      - 'Observation: courroie qui se deporte sur le'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Galet enrouleur de courroie de distribution - Guide Complet

## Fonction

Guider la courroie de distribution dans son parcours

## Symptômes de défaillance

### Bruit de roulement au ralenti

bruit de roulement au ralenti

### Sifflement cote distribution

sifflement cote distribution

### Traces d usure anormale sur la

traces d usure anormale sur la courroie

### Galet qui tourne difficilement a la

galet qui tourne difficilement a la main

### Jeu radial ou axial dans le

jeu radial ou axial dans le galet

### Bruit metallique leger

bruit metallique leger

### Courroie qui se deporte sur le

courroie qui se deporte sur le cote

## Diagnostic

Pour diagnostiquer un problème de galet enrouleur de courroie de distribution:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- courroie-de-distribution

## Compatibilité

Pour commander le bon galet enrouleur de courroie de distribution, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
