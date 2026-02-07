---
entity_type: gamme
title: Module d'allumage
slug: module-d-allumage
pg_id: 1218
category: allumage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Commander electroniquement le moment d'allumage
  must_be_true:
    - piloter
    - commander
    - controler
  must_not_contain_concepts:
    - freinage
    - climatisation
    - embrayage
    - direction
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
    label: Rates d allumage intermittents
    description: rates d allumage intermittents
    risk_level: confort
    evidence:
      - 'Observation: rates d allumage intermittents'
      - Vérification visuelle ou auditive
  - id: S2
    label: Demarrage difficile
    description: demarrage difficile
    risk_level: confort
    evidence:
      - 'Observation: demarrage difficile'
      - Vérification visuelle ou auditive
  - id: S3
    label: Perte de puissance sur certains cylindres
    description: perte de puissance sur certains cylindres
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance sur certains cylindres'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Module d'allumage - Guide Diagnostic Complet

## Fonction et Rôle

Commander electroniquement le moment d'allumage

**Actions principales:** piloter, commander, controler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- rates d allumage intermittents
- demarrage difficile
- perte de puissance sur certains cylindres

## Procédure de Diagnostic

Pour diagnostiquer un problème de module d'allumage:

1. **Inspection visuelle** - Examiner l'état du module d'allumage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bobine-d-allumage
- calculateur-moteur

## Critères de Compatibilité

Pour commander le bon module d'allumage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "demarrage instantane"
