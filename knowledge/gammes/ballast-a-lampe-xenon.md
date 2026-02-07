---
entity_type: gamme
title: Ballast à lampe xénon
slug: ballast-a-lampe-xenon
pg_id: 1431
category: eclairage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Convertit et stabilise la tension électrique pour alimenter les ampoules
    xénon
  must_be_true:
    - alimenter
    - convertir
    - stabiliser
  must_not_contain_concepts:
    - ampoule
    - lampe
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_general_detecte
    then: inspection_visuelle_et_test_fonctionnel
symptoms:
  - id: S1
    label: Phare xenon ne s'allume pas
    description: phare xenon ne s'allume pas
    risk_level: confort
    evidence:
      - 'Observation: phare xenon ne s''allume pas'
      - Vérification visuelle ou auditive
  - id: S2
    label: Eclairage instable
    description: eclairage instable
    risk_level: confort
    evidence:
      - 'Observation: eclairage instable'
      - Vérification visuelle ou auditive
  - id: S3
    label: Phare qui clignote
    description: phare qui clignote
    risk_level: confort
    evidence:
      - 'Observation: phare qui clignote'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Ballast à lampe xénon - Guide Diagnostic Complet

## Fonction et Rôle

Convertit et stabilise la tension électrique pour alimenter les ampoules xénon

**Actions principales:** alimenter, convertir, stabiliser

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- phare xenon ne s'allume pas
- eclairage instable
- phare qui clignote

## Procédure de Diagnostic

Pour diagnostiquer un problème de ballast à lampe xénon:

1. **Inspection visuelle** - Examiner l'état du ballast à lampe xénon
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-avant
- feu-avant

## Critères de Compatibilité

Pour commander le bon ballast à lampe xénon, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "visibilite parfaite"
