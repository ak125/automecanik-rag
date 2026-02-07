---
entity_type: gamme
title: Détendeur de climatisation
slug: detendeur-de-climatisation
pg_id: 183
category: climatisation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Détend le fluide frigorigène avant l'évaporateur
  must_be_true:
    - detendre
    - reguler
    - abaisser la pression
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
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
symptoms:
  - id: S1
    label: Evaporateur qui givre anormalement
    description: evaporateur qui givre anormalement
    risk_level: confort
    evidence:
      - 'Observation: evaporateur qui givre anormalement'
      - Vérification visuelle ou auditive
  - id: S2
    label: Refroidissement irregulier chaud puis froid
    description: refroidissement irregulier chaud puis froid
    risk_level: confort
    evidence:
      - 'Observation: refroidissement irregulier chaud puis froid'
      - Vérification visuelle ou auditive
  - id: S3
    label: Sifflement ou bruit de detente audible
    description: sifflement ou bruit de detente audible
    risk_level: confort
    evidence:
      - 'Observation: sifflement ou bruit de detente audible'
      - Vérification visuelle ou auditive
  - id: S4
    label: Compresseur qui cycle en permanence
    description: compresseur qui cycle en permanence
    risk_level: confort
    evidence:
      - 'Observation: compresseur qui cycle en permanence'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de gaz refrigerant dans l habitacle
    description: odeur de gaz refrigerant dans l habitacle
    risk_level: confort
    evidence:
      - 'Observation: odeur de gaz refrigerant dans l habitacle'
      - Vérification visuelle ou auditive
  - id: S6
    label: Clim qui fonctionne puis s arrete brusquement
    description: clim qui fonctionne puis s arrete brusquement
    risk_level: confort
    evidence:
      - 'Observation: clim qui fonctionne puis s arrete brusquement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Détendeur de climatisation - Guide Diagnostic Complet

## Fonction et Rôle

Détend le fluide frigorigène avant l'évaporateur

**Actions principales:** detendre, reguler, abaisser la pression

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- evaporateur qui givre anormalement
- refroidissement irregulier chaud puis froid
- sifflement ou bruit de detente audible
- compresseur qui cycle en permanence
- odeur de gaz refrigerant dans l habitacle
- clim qui fonctionne puis s arrete brusquement

## Procédure de Diagnostic

Pour diagnostiquer un problème de détendeur de climatisation:

1. **Inspection visuelle** - Examiner l'état du détendeur de climatisation
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bouteille-deshydratante
- commande-de-ventilation
- compresseur-de-climatisation
- condenseur-de-climatisation
- evaporateur-de-climatisation
- filtre-d-habitacle

## Critères de Compatibilité

Pour commander le bon détendeur de climatisation, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidit le moteur"
