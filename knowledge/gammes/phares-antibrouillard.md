---
entity_type: gamme
title: Phares antibrouillard
slug: phares-antibrouillard
pg_id: 289
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
    Dirige la lumière pour améliorer la visibilité par temps de brouillard ou
    mauvaise visibilité
  must_be_true:
    - diriger
    - diffuser
    - eclairer
  must_not_contain_concepts:
    - ampoule seule
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
    label: Antibrouillard inactif
    description: antibrouillard inactif
    risk_level: confort
    evidence:
      - 'Observation: antibrouillard inactif'
      - Vérification visuelle ou auditive
  - id: S2
    label: Eclairage faible ou jauni
    description: eclairage faible ou jauni
    risk_level: confort
    evidence:
      - 'Observation: eclairage faible ou jauni'
      - Vérification visuelle ou auditive
  - id: S3
    label: Optique fissuree ou embuee
    description: optique fissuree ou embuee
    risk_level: confort
    evidence:
      - 'Observation: optique fissuree ou embuee'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Phares antibrouillard - Guide Diagnostic Complet

## Fonction et Rôle

Dirige la lumière pour améliorer la visibilité par temps de brouillard ou mauvaise visibilité

**Actions principales:** diriger, diffuser, eclairer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- antibrouillard inactif
- eclairage faible ou jauni
- optique fissuree ou embuee

## Procédure de Diagnostic

Pour diagnostiquer un problème de phares antibrouillard:

1. **Inspection visuelle** - Examiner l'état du phares antibrouillard
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-avant
- relais-phare

## Critères de Compatibilité

Pour commander le bon phares antibrouillard, vous devez connaître:

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
