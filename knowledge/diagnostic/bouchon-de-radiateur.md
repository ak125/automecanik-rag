---
entity_type: gamme
title: Bouchon de radiateur
slug: bouchon-de-radiateur
pg_id: 548
category: refroidissement
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Fermer le radiateur et reguler la pression du circuit
  must_be_true:
    - fermer
    - reguler
    - proteger
  must_not_contain_concepts:
    - injection
    - freinage
    - embrayage
    - distribution
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_fuite-de-liquide-par-le-bouchon
    then: verifier_piece
  - if: symptome_surchauffe-moteur-sans-fuite-visible
    then: diagnostic_approfondi
  - if: symptome_pression-excessive-dans-le-circuit
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Fuite de liquide par le bouchon
    description: fuite de liquide par le bouchon
    risk_level: confort
    evidence:
      - 'Observation: fuite de liquide par le bouchon'
      - Vérification visuelle ou auditive
  - id: S2
    label: Surchauffe moteur sans fuite visible
    description: surchauffe moteur sans fuite visible
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: surchauffe moteur sans fuite visible'
      - Vérification visuelle ou auditive
  - id: S3
    label: Pression excessive dans le circuit
    description: pression excessive dans le circuit
    risk_level: confort
    evidence:
      - 'Observation: pression excessive dans le circuit'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Bouchon de radiateur - Guide Complet

## Fonction

Fermer le radiateur et reguler la pression du circuit

## Symptômes de défaillance

### Fuite de liquide par le bouchon

fuite de liquide par le bouchon

### Surchauffe moteur sans fuite visible

surchauffe moteur sans fuite visible

### Pression excessive dans le circuit

pression excessive dans le circuit

## Diagnostic

Pour diagnostiquer un problème de bouchon de radiateur:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- radiateur
- durite-de-refroidissement

## Compatibilité

Pour commander le bon bouchon de radiateur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
