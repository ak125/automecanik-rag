---
entity_type: gamme
title: Pressostat de climatisation
slug: pressostat-de-climatisation
pg_id: 1360
category: climatisation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Mesurer la pression du fluide et proteger le compresseur
  must_be_true:
    - detecter
    - mesurer
    - proteger
  must_not_contain_concepts:
    - injection
    - freinage
    - allumage
    - embrayage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: vehicule_immobilise_ou_symptome_critique
    then: verification_urgente_piece_et_alimentation
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
symptoms:
  - id: S1
    label: Climatisation qui s arrete brutalement
    description: climatisation qui s arrete brutalement
    risk_level: confort
    evidence:
      - 'Observation: climatisation qui s arrete brutalement'
      - Vérification visuelle ou auditive
  - id: S2
    label: Compresseur qui ne demarre pas
    description: compresseur qui ne demarre pas
    risk_level: immobilisation
    evidence:
      - 'Observation: compresseur qui ne demarre pas'
      - Vérification visuelle ou auditive
  - id: S3
    label: Voyant de climatisation clignotant
    description: voyant de climatisation clignotant
    risk_level: confort
    evidence:
      - 'Observation: voyant de climatisation clignotant'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Pressostat de climatisation - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la pression du fluide et proteger le compresseur

**Actions principales:** detecter, mesurer, proteger

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Compresseur qui ne demarre pas**
  compresseur qui ne demarre pas

### 🟢 Autres Symptômes

- climatisation qui s arrete brutalement
- voyant de climatisation clignotant

## Procédure de Diagnostic

Pour diagnostiquer un problème de pressostat de climatisation:

1. **Inspection visuelle** - Examiner l'état du pressostat de climatisation
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Pièce HS** - Le pressostat de climatisation peut être hors service et nécessiter un remplacement
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- conduite-de-climatisation

## Critères de Compatibilité

Pour commander le bon pressostat de climatisation, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidit instantanement"
