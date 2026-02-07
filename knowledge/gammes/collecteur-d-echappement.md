---
entity_type: gamme
title: Collecteur d'échappement
slug: collecteur-d-echappement
pg_id: 1543
category: echappement
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Collecte les gaz d'échappement sortant des cylindres et les achemine vers le
    catalyseur
  must_be_true:
    - collecter
    - acheminer
    - rassembler
  must_not_contain_concepts:
    - fap
    - sonde lambda
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
symptoms:
  - id: S1
    label: Bruit metallique demarrage diminue chaud
    description: bruit metallique demarrage diminue chaud
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit metallique demarrage diminue chaud'
      - Vérification visuelle ou auditive
  - id: S2
    label: Odeur echappement habitacle sous capot
    description: odeur echappement habitacle sous capot
    risk_level: confort
    evidence:
      - 'Observation: odeur echappement habitacle sous capot'
      - Vérification visuelle ou auditive
  - id: S3
    label: Traces de suie noire autour du collecteur visuel
    description: traces de suie noire autour du collecteur visuel
    risk_level: confort
    evidence:
      - 'Observation: traces de suie noire autour du collecteur visuel'
      - Vérification visuelle ou auditive
  - id: S4
    label: Perte puissance mauvais rendement moteur
    description: perte puissance mauvais rendement moteur
    risk_level: confort
    evidence:
      - 'Observation: perte puissance mauvais rendement moteur'
      - Vérification visuelle ou auditive
  - id: S5
    label: Voyant moteur allume - codes sonde lambda visuel
    description: voyant moteur allume - codes sonde lambda visuel
    risk_level: confort
    evidence:
      - 'Observation: voyant moteur allume - codes sonde lambda visuel'
      - Vérification visuelle ou auditive
  - id: S6
    label: Controle technique refuse pollution excessive
    description: controle technique refuse pollution excessive
    risk_level: confort
    evidence:
      - 'Observation: controle technique refuse pollution excessive'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Collecteur d'échappement - Guide Diagnostic Complet

## Fonction et Rôle

Collecte les gaz d'échappement sortant des cylindres et les achemine vers le catalyseur

**Actions principales:** collecter, acheminer, rassembler

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit metallique demarrage diminue chaud**
  bruit metallique demarrage diminue chaud

### 🟢 Autres Symptômes

- odeur echappement habitacle sous capot
- traces de suie noire autour du collecteur visuel
- perte puissance mauvais rendement moteur
- voyant moteur allume - codes sonde lambda visuel
- controle technique refuse pollution excessive

## Procédure de Diagnostic

Pour diagnostiquer un problème de collecteur d'échappement:

1. **Inspection visuelle** - Examiner l'état du collecteur d'échappement
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- joint-d-echappement
- catalyseur

## Critères de Compatibilité

Pour commander le bon collecteur d'échappement, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "passe le controle technique"
