---
entity_type: gamme
title: Butée d'embrayage
slug: butee-d-embrayage
pg_id: 48
category: embrayage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Actionner le mécanisme d'embrayage pour permettre le débrayage
  must_be_true:
    - actionner
    - débrayer
    - pousser
  must_not_contain_concepts:
    - disque
    - volant
    - couple
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_bruit-roulement-quand-appuie-pedale
    then: verifier_piece
  - if: symptome_sifflement-grondement-disparait-relachant-pedale
    then: diagnostic_approfondi
  - if: symptome_pedale-d-embrayage-qui-vibre-sous
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Bruit roulement quand appuie pedale
    description: bruit roulement quand appuie pedale
    risk_level: confort
    evidence:
      - 'Observation: bruit roulement quand appuie pedale'
      - Vérification visuelle ou auditive
  - id: S2
    label: Sifflement grondement disparait relachant pedale
    description: sifflement grondement disparait relachant pedale
    risk_level: confort
    evidence:
      - 'Observation: sifflement grondement disparait relachant pedale'
      - Vérification visuelle ou auditive
  - id: S3
    label: Pedale d embrayage qui vibre sous
    description: pedale d embrayage qui vibre sous le pied
    risk_level: confort
    evidence:
      - 'Observation: pedale d embrayage qui vibre sous'
      - Vérification visuelle ou auditive
  - id: S4
    label: Embrayage qui accroche par a-coups
    description: embrayage qui accroche par a-coups
    risk_level: confort
    evidence:
      - 'Observation: embrayage qui accroche par a-coups'
      - Vérification visuelle ou auditive
  - id: S5
    label: Difficulte a passer les vitesses butee
    description: difficulte a passer les vitesses butee grippee
    risk_level: confort
    evidence:
      - 'Observation: difficulte a passer les vitesses butee'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus changement embrayage
    description: plus changement embrayage
    risk_level: confort
    evidence:
      - 'Observation: plus changement embrayage'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Butée d'embrayage - Guide Complet

## Fonction

Actionner le mécanisme d'embrayage pour permettre le débrayage

## Symptômes de défaillance

### Bruit roulement quand appuie pedale

bruit roulement quand appuie pedale

### Sifflement grondement disparait relachant pedale

sifflement grondement disparait relachant pedale

### Pedale d embrayage qui vibre sous

pedale d embrayage qui vibre sous le pied

### Embrayage qui accroche par a-coups

embrayage qui accroche par a-coups

### Difficulte a passer les vitesses butee

difficulte a passer les vitesses butee grippee

### Plus changement embrayage

plus changement embrayage

## Diagnostic

Pour diagnostiquer un problème de butée d'embrayage:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- emetteur-d-embrayage
- kit-d-embrayage
- recepteur-d-embrayage
- volant-moteur

## Compatibilité

Pour commander le bon butée d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
