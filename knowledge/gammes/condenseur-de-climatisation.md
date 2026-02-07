---
entity_type: gamme
title: Condenseur de climatisation
slug: condenseur-de-climatisation
pg_id: 448
category: climatisation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Dissipe la chaleur du fluide frigorigene comprime - Distinct du radiateur
    moteur
  must_be_true:
    - dissiper la chaleur
  must_not_contain_concepts:
    - radiateur moteur
    - refroidissement
    - eau
    - liquide
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
symptoms:
  - id: S1
    label: Climatisation moins efficace qu avant
    description: climatisation moins efficace qu avant
    risk_level: confort
    evidence:
      - 'Observation: climatisation moins efficace qu avant'
      - Vérification visuelle ou auditive
  - id: S2
    label: Recharges de gaz frequentes necessaires
    description: recharges de gaz frequentes necessaires
    risk_level: confort
    evidence:
      - 'Observation: recharges de gaz frequentes necessaires'
      - Vérification visuelle ou auditive
  - id: S3
    label: Traces d huile verdatre sur le condenseur
    description: traces d huile verdatre sur le condenseur
    risk_level: confort
    evidence:
      - 'Observation: traces d huile verdatre sur le condenseur'
      - Vérification visuelle ou auditive
  - id: S4
    label: Condenseur visiblement deforme ou perce
    description: condenseur visiblement deforme ou perce
    risk_level: confort
    evidence:
      - 'Observation: condenseur visiblement deforme ou perce'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de gaz refrigerant a l avant
    description: odeur de gaz refrigerant a l avant
    risk_level: confort
    evidence:
      - 'Observation: odeur de gaz refrigerant a l avant'
      - Vérification visuelle ou auditive
  - id: S6
    label: Choc frontal recent meme leger
    description: choc frontal recent meme leger
    risk_level: confort
    evidence:
      - 'Observation: choc frontal recent meme leger'
      - Vérification visuelle ou auditive
  - id: S7
    label: Bruit ventilateur condenseur tourne permanence
    description: bruit ventilateur condenseur tourne permanence
    risk_level: confort
    evidence:
      - 'Observation: bruit ventilateur condenseur tourne permanence'
      - Vérification visuelle ou auditive
  - id: S8
    label: Climatisation inefficace temps chaud embouteillages
    description: climatisation inefficace temps chaud embouteillages
    risk_level: confort
    evidence:
      - 'Observation: climatisation inefficace temps chaud embouteillages'
      - Vérification visuelle ou auditive
  - id: S9
    label: Plus controle circuit climatisation preventif
    description: plus controle circuit climatisation preventif
    risk_level: confort
    evidence:
      - 'Observation: plus controle circuit climatisation preventif'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Condenseur de climatisation - Guide Diagnostic Complet

## Fonction et Rôle

Dissipe la chaleur du fluide frigorigene comprime - Distinct du radiateur moteur

**Actions principales:** dissiper la chaleur

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- climatisation moins efficace qu avant
- recharges de gaz frequentes necessaires
- traces d huile verdatre sur le condenseur
- condenseur visiblement deforme ou perce
- odeur de gaz refrigerant a l avant
- choc frontal recent meme leger

## Procédure de Diagnostic

Pour diagnostiquer un problème de condenseur de climatisation:

1. **Inspection visuelle** - Examiner l'état du condenseur de climatisation
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
- detendeur-de-climatisation
- evaporateur-de-climatisation
- filtre-d-habitacle
- pulseur-d-air-d-habitacle

## Critères de Compatibilité

Pour commander le bon condenseur de climatisation, vous devez connaître:

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
