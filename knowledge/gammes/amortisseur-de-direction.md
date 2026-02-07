---
entity_type: gamme
title: Amortisseur de direction
slug: amortisseur-de-direction
pg_id: 130
category: direction
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Amortir les vibrations et chocs transmis au volant
  must_be_true:
    - amortir
    - stabiliser
    - filtrer
  must_not_contain_concepts:
    - injection
    - freinage
    - distribution
    - turbo
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: vibrations_anormales
    then: verifier_equilibrage_et_fixations
symptoms:
  - id: S1
    label: Shimmy vibration du volant a certaines vitesses
    description: shimmy vibration du volant a certaines vitesses
    risk_level: confort
    evidence:
      - 'Observation: shimmy vibration du volant a certaines vitesses'
      - Vérification visuelle ou auditive
  - id: S2
    label: Direction qui tire d un cote
    description: direction qui tire d un cote
    risk_level: securite
    evidence:
      - 'Observation: direction qui tire d un cote'
      - Vérification visuelle ou auditive
  - id: S3
    label: Sensation de flottement dans la direction
    description: sensation de flottement dans la direction
    risk_level: securite
    evidence:
      - 'Observation: sensation de flottement dans la direction'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Amortisseur de direction - Guide Diagnostic Complet

## Fonction et Rôle

Amortir les vibrations et chocs transmis au volant

**Actions principales:** amortir, stabiliser, filtrer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Direction qui tire d un cote**
  direction qui tire d un cote
- **Sensation de flottement dans la direction**
  sensation de flottement dans la direction

### 🟢 Autres Symptômes

- shimmy vibration du volant a certaines vitesses

## Procédure de Diagnostic

Pour diagnostiquer un problème de amortisseur de direction:

1. **Inspection visuelle** - Examiner l'état du amortisseur de direction
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- cremaillere-de-direction
- colonne-de-direction

## Critères de Compatibilité

Pour commander le bon amortisseur de direction, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "direction parfaite"
