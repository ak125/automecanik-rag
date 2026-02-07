---
entity_type: gamme
title: Serrure de porte
slug: serrure-de-porte
pg_id: 1361
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Verrouille et déverrouille la porte du véhicule
  must_be_true:
    - verrouiller
    - deverrouiller
    - bloquer
  must_not_contain_concepts:
    - alarme
    - antivol
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
    label: Porte qui ne se verrouille plus
    description: porte qui ne se verrouille plus
    risk_level: confort
    evidence:
      - 'Observation: porte qui ne se verrouille plus'
      - Vérification visuelle ou auditive
  - id: S2
    label: Centralisation inoperante sur une porte
    description: centralisation inoperante sur une porte
    risk_level: confort
    evidence:
      - 'Observation: centralisation inoperante sur une porte'
      - Vérification visuelle ou auditive
  - id: S3
    label: Cle qui tourne dans le vide
    description: cle qui tourne dans le vide
    risk_level: confort
    evidence:
      - 'Observation: cle qui tourne dans le vide'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Serrure de porte - Guide Diagnostic Complet

## Fonction et Rôle

Verrouille et déverrouille la porte du véhicule

**Actions principales:** verrouiller, deverrouiller, bloquer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- porte qui ne se verrouille plus
- centralisation inoperante sur une porte
- cle qui tourne dans le vide

## Procédure de Diagnostic

Pour diagnostiquer un problème de serrure de porte:

1. **Inspection visuelle** - Examiner l'état du serrure de porte
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- poignee
- cle
- barillet

## Critères de Compatibilité

Pour commander le bon serrure de porte, vous devez connaître:

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
