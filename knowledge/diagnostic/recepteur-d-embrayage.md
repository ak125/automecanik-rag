---
entity_type: gamme
title: Récepteur d'embrayage
slug: recepteur-d-embrayage
pg_id: 620
category: embrayage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Recevoir la pression hydraulique et actionner la butée ou la fourchette
  must_be_true:
    - recevoir la pression
    - actionner la butée
    - pousser la fourchette
  must_not_contain_concepts:
    - disque
    - volant
    - couple
    - câble
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_pedale-d-embrayage-molle-ou-spongieuse
    then: verifier_piece
  - if: symptome_fuite-de-liquide-visible-sous-la
    then: diagnostic_approfondi
  - if: symptome_bruit-de-grincement-au-niveau-de
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Pedale d embrayage molle ou spongieuse
    description: pedale d embrayage molle ou spongieuse
    risk_level: confort
    evidence:
      - 'Observation: pedale d embrayage molle ou spongieuse'
      - Vérification visuelle ou auditive
  - id: S2
    label: Fuite de liquide visible sous la
    description: fuite de liquide visible sous la boite de vitesses
    risk_level: confort
    evidence:
      - 'Observation: fuite de liquide visible sous la'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit de grincement au niveau de
    description: bruit de grincement au niveau de la fourchette
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit de grincement au niveau de'
      - Vérification visuelle ou auditive
  - id: S4
    label: Odeur de liquide de frein brule
    description: odeur de liquide de frein brule sous la voiture
    risk_level: securite
    evidence:
      - 'Observation: odeur de liquide de frein brule'
      - Vérification visuelle ou auditive
  - id: S5
    label: Embrayage qui ne debraye plus piston
    description: embrayage qui ne debraye plus piston bloque
    risk_level: immobilisation
    evidence:
      - 'Observation: embrayage qui ne debraye plus piston'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 150 000 km sans
    description: plus de 150 000 km sans verification du circuit
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
# Récepteur d'embrayage - Guide Complet

## Fonction

Recevoir la pression hydraulique et actionner la butée ou la fourchette

## Symptômes de défaillance

### Pedale d embrayage molle ou spongieuse

pedale d embrayage molle ou spongieuse

### Fuite de liquide visible sous la

fuite de liquide visible sous la boite de vitesses

### Bruit de grincement au niveau de

bruit de grincement au niveau de la fourchette

### Odeur de liquide de frein brule

odeur de liquide de frein brule sous la voiture

### Embrayage qui ne debraye plus piston

embrayage qui ne debraye plus piston bloque

### Plus de 150 000 km sans

plus de 150 000 km sans verification du circuit

## Diagnostic

Pour diagnostiquer un problème de récepteur d'embrayage:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- butee-d-embrayage
- emetteur-d-embrayage
- kit-d-embrayage
- volant-moteur

## Compatibilité

Pour commander le bon récepteur d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
