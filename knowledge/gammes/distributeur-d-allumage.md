---
entity_type: gamme
title: Distributeur d'allumage
slug: distributeur-d-allumage
pg_id: 683
category: allumage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Distribuer la haute tension aux bougies dans l'ordre d'allumage
  must_be_true:
    - distribuer
    - repartir
    - transmettre
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
    label: Rates d allumage
    description: rates d allumage
    risk_level: confort
    evidence:
      - 'Observation: rates d allumage'
      - Vérification visuelle ou auditive
  - id: S2
    label: Demarrage difficile
    description: demarrage difficile
    risk_level: confort
    evidence:
      - 'Observation: demarrage difficile'
      - Vérification visuelle ou auditive
  - id: S3
    label: Manque de puissance
    description: manque de puissance
    risk_level: confort
    evidence:
      - 'Observation: manque de puissance'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Distributeur d'allumage - Guide Diagnostic Complet

## Fonction et Rôle

Distribuer la haute tension aux bougies dans l'ordre d'allumage

**Actions principales:** distribuer, repartir, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- rates d allumage
- demarrage difficile
- manque de puissance

## Procédure de Diagnostic

Pour diagnostiquer un problème de distributeur d'allumage:

1. **Inspection visuelle** - Examiner l'état du distributeur d'allumage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bobine-d-allumage
- faisceau-d-allumage
- bougie-d-allumage

## Critères de Compatibilité

Pour commander le bon distributeur d'allumage, vous devez connaître:

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
