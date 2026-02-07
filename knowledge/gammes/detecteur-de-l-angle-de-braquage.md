---
entity_type: gamme
title: Détecteur de l'angle de braquage
slug: detecteur-de-l-angle-de-braquage
pg_id: 3252
category: direction
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Mesurer l'angle de rotation du volant pour l'ESP
  must_be_true:
    - mesurer
    - detecter
    - transmettre
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
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
symptoms:
  - id: S1
    label: Voyant esp allume en permanence
    description: voyant esp allume en permanence
    risk_level: securite
    evidence:
      - 'Observation: voyant esp allume en permanence'
      - Vérification visuelle ou auditive
  - id: S2
    label: Direction assistee desactivee
    description: direction assistee desactivee
    risk_level: securite
    evidence:
      - 'Observation: direction assistee desactivee'
      - Vérification visuelle ou auditive
  - id: S3
    label: Comportement anormal du vehicule en virage
    description: comportement anormal du vehicule en virage
    risk_level: confort
    evidence:
      - 'Observation: comportement anormal du vehicule en virage'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Détecteur de l'angle de braquage - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer l'angle de rotation du volant pour l'ESP

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Voyant esp allume en permanence**
  voyant esp allume en permanence
- **Direction assistee desactivee**
  direction assistee desactivee

### 🟢 Autres Symptômes

- comportement anormal du vehicule en virage

## Procédure de Diagnostic

Pour diagnostiquer un problème de détecteur de l'angle de braquage:

1. **Inspection visuelle** - Examiner l'état du détecteur de l'angle de braquage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- calculateur-esp
- capteur-abs

## Critères de Compatibilité

Pour commander le bon détecteur de l'angle de braquage, vous devez connaître:

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
