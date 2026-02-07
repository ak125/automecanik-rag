---
entity_type: gamme
title: Refroidisseur de carburant
slug: refroidisseur-de-carburant
pg_id: 3640
category: alimentation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Refroidir le carburant de retour pour optimiser l'injection
  must_be_true:
    - refroidir
    - abaisser la temperature
  must_not_contain_concepts:
    - freinage
    - climatisation
    - distribution
    - embrayage
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
    label: Surchauffe du carburant en ete
    description: surchauffe du carburant en ete
    risk_level: confort
    evidence:
      - 'Observation: surchauffe du carburant en ete'
      - Vérification visuelle ou auditive
  - id: S2
    label: Perte de puissance par temps chaud
    description: perte de puissance par temps chaud
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance par temps chaud'
      - Vérification visuelle ou auditive
  - id: S3
    label: Codes defaut temperature carburant
    description: codes defaut temperature carburant
    risk_level: confort
    evidence:
      - 'Observation: codes defaut temperature carburant'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Refroidisseur de carburant - Guide Diagnostic Complet

## Fonction et Rôle

Refroidir le carburant de retour pour optimiser l'injection

**Actions principales:** refroidir, abaisser la temperature

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- surchauffe du carburant en ete
- perte de puissance par temps chaud
- codes defaut temperature carburant

## Procédure de Diagnostic

Pour diagnostiquer un problème de refroidisseur de carburant:

1. **Inspection visuelle** - Examiner l'état du refroidisseur de carburant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- pompe-a-carburant
- filtre-a-carburant

## Critères de Compatibilité

Pour commander le bon refroidisseur de carburant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare l'injection"
