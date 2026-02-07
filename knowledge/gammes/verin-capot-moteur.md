---
entity_type: gamme
title: Vérin capot moteur
slug: verin-capot-moteur
pg_id: 514
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Maintient le capot moteur en position ouverte
  must_be_true:
    - maintenir
    - supporter
    - soulever
  must_not_contain_concepts:
    - moteur
    - refroidissement
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
    label: Capot qui retombe lentement
    description: capot qui retombe lentement
    risk_level: confort
    evidence:
      - 'Observation: capot qui retombe lentement'
      - Vérification visuelle ou auditive
  - id: S2
    label: Capot qui ne reste plus ouvert
    description: capot qui ne reste plus ouvert
    risk_level: confort
    evidence:
      - 'Observation: capot qui ne reste plus ouvert'
      - Vérification visuelle ou auditive
  - id: S3
    label: Verin qui fuit traces de graisse
    description: verin qui fuit traces de graisse
    risk_level: confort
    evidence:
      - 'Observation: verin qui fuit traces de graisse'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Vérin capot moteur - Guide Diagnostic Complet

## Fonction et Rôle

Maintient le capot moteur en position ouverte

**Actions principales:** maintenir, supporter, soulever

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- capot qui retombe lentement
- capot qui ne reste plus ouvert
- verin qui fuit traces de graisse

## Procédure de Diagnostic

Pour diagnostiquer un problème de vérin capot moteur:

1. **Inspection visuelle** - Examiner l'état du vérin capot moteur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- capot
- charniere

## Critères de Compatibilité

Pour commander le bon vérin capot moteur, vous devez connaître:

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
