---
entity_type: gamme
title: Moteur électrique de ventilateur
slug: moteur-electrique-de-ventilateur
pg_id: 792
category: refroidissement
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Entrainer les pales du ventilateur de refroidissement
  must_be_true:
    - entrainer
    - tourner
    - ventiler
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
  - if: symptome_ventilateur-qui-ne-tourne-pas
    then: verifier_piece
  - if: symptome_surchauffe-en-circulation-lente
    then: diagnostic_approfondi
  - if: symptome_bruit-de-roulement-du-ventilateur
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Ventilateur qui ne tourne pas
    description: ventilateur qui ne tourne pas
    risk_level: immobilisation
    evidence:
      - 'Observation: ventilateur qui ne tourne pas'
      - Vérification visuelle ou auditive
  - id: S2
    label: Surchauffe en circulation lente
    description: surchauffe en circulation lente
    risk_level: confort
    evidence:
      - 'Observation: surchauffe en circulation lente'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit de roulement du ventilateur
    description: bruit de roulement du ventilateur
    risk_level: confort
    evidence:
      - 'Observation: bruit de roulement du ventilateur'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Moteur électrique de ventilateur - Guide Complet

## Fonction

Entrainer les pales du ventilateur de refroidissement

## Symptômes de défaillance

### Ventilateur qui ne tourne pas

ventilateur qui ne tourne pas

### Surchauffe en circulation lente

surchauffe en circulation lente

### Bruit de roulement du ventilateur

bruit de roulement du ventilateur

## Diagnostic

Pour diagnostiquer un problème de moteur électrique de ventilateur:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- ventilateur-de-refroidissement

## Compatibilité

Pour commander le bon moteur électrique de ventilateur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
