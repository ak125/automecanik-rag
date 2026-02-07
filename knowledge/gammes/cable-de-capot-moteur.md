---
entity_type: gamme
title: Câble de capot moteur
slug: cable-de-capot-moteur
pg_id: 1238
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmet la commande d'ouverture du capot depuis l'habitacle
  must_be_true:
    - transmettre
    - actionner
    - liberer
  must_not_contain_concepts:
    - moteur
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
    label: Capot impossible a ouvrir
    description: capot impossible a ouvrir
    risk_level: confort
    evidence:
      - 'Observation: capot impossible a ouvrir'
      - Vérification visuelle ou auditive
  - id: S2
    label: Tirette molle sans resistance
    description: tirette molle sans resistance
    risk_level: confort
    evidence:
      - 'Observation: tirette molle sans resistance'
      - Vérification visuelle ou auditive
  - id: S3
    label: Cable casse ou grippe
    description: cable casse ou grippe
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: cable casse ou grippe'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Câble de capot moteur - Guide Diagnostic Complet

## Fonction et Rôle

Transmet la commande d'ouverture du capot depuis l'habitacle

**Actions principales:** transmettre, actionner, liberer

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Cable casse ou grippe**
  cable casse ou grippe

### 🟢 Autres Symptômes

- capot impossible a ouvrir
- tirette molle sans resistance

## Procédure de Diagnostic

Pour diagnostiquer un problème de câble de capot moteur:

1. **Inspection visuelle** - Examiner l'état du câble de capot moteur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- serrure capot
- levier

## Critères de Compatibilité

Pour commander le bon câble de capot moteur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"
