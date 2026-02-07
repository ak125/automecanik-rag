---
entity_type: gamme
title: Contacteur démarreur
slug: contacteur-demarreur
pg_id: 682
category: electrique
subcategory: demarrage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Commuter le circuit electrique du demarreur
  must_be_true:
    - commuter
    - activer
    - alimenter
  must_not_contain_concepts:
    - injection
    - climatisation
    - freinage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_aucune-reaction-a-la-cle-de
    then: verifier_piece
  - if: symptome_demarrage-intermittent
    then: diagnostic_approfondi
  - if: symptome_tableau-de-bord-qui-ne-s
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Aucune reaction a la cle de
    description: aucune reaction a la cle de contact
    risk_level: confort
    evidence:
      - 'Observation: aucune reaction a la cle de'
      - Vérification visuelle ou auditive
  - id: S2
    label: Demarrage intermittent
    description: demarrage intermittent
    risk_level: confort
    evidence:
      - 'Observation: demarrage intermittent'
      - Vérification visuelle ou auditive
  - id: S3
    label: Tableau de bord qui ne s
    description: tableau de bord qui ne s allume pas
    risk_level: confort
    evidence:
      - 'Observation: tableau de bord qui ne s'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Contacteur démarreur - Guide Complet

## Fonction

Commuter le circuit electrique du demarreur

## Symptômes de défaillance

### Aucune reaction a la cle de

aucune reaction a la cle de contact

### Demarrage intermittent

demarrage intermittent

### Tableau de bord qui ne s

tableau de bord qui ne s allume pas

## Diagnostic

Pour diagnostiquer un problème de contacteur démarreur:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- demarreur
- batterie

## Compatibilité

Pour commander le bon contacteur démarreur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
