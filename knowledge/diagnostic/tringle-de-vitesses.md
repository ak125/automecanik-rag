---
entity_type: gamme
title: Tringle de vitesses
slug: tringle-de-vitesses
pg_id: 1650
category: embrayage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmettre le mouvement du levier vers la boite
  must_be_true:
    - transmettre
    - guider
    - relier
  must_not_contain_concepts:
    - injection
    - freinage
    - climatisation
    - turbo
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_vitesses-dures-a-passer
    then: verifier_piece
  - if: symptome_levier-de-vitesses-flottant
    then: diagnostic_approfondi
  - if: symptome_craquements-au-passage-des-rapports
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Vitesses dures a passer
    description: vitesses dures a passer
    risk_level: confort
    evidence:
      - 'Observation: vitesses dures a passer'
      - Vérification visuelle ou auditive
  - id: S2
    label: Levier de vitesses flottant
    description: levier de vitesses flottant
    risk_level: confort
    evidence:
      - 'Observation: levier de vitesses flottant'
      - Vérification visuelle ou auditive
  - id: S3
    label: Craquements au passage des rapports
    description: craquements au passage des rapports
    risk_level: confort
    evidence:
      - 'Observation: craquements au passage des rapports'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Tringle de vitesses - Guide Complet

## Fonction

Transmettre le mouvement du levier vers la boite

## Symptômes de défaillance

### Vitesses dures a passer

vitesses dures a passer

### Levier de vitesses flottant

levier de vitesses flottant

### Craquements au passage des rapports

craquements au passage des rapports

## Diagnostic

Pour diagnostiquer un problème de tringle de vitesses:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- fourchette-d-embrayage
- guide-d-embrayage

## Compatibilité

Pour commander le bon tringle de vitesses, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
