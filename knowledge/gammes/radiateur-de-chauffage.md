---
entity_type: gamme
title: Radiateur de chauffage
slug: radiateur-de-chauffage
pg_id: 467
category: refroidissement
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Transferer la chaleur du liquide de refroidissement vers l'habitacle pour le
    confort des passagers. NE REFROIDIT PAS LE MOTEUR!
  must_be_true:
    - chauffer
    - transferer
    - diffuser
  must_not_contain_concepts:
    - refroidissement moteur
    - ventilateur moteur
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
symptoms:
  - id: S1
    label: Buee grasse persistante sur le pare-brise
    description: buee grasse persistante sur le pare-brise
    risk_level: confort
    evidence:
      - 'Observation: buee grasse persistante sur le pare-brise'
      - Vérification visuelle ou auditive
  - id: S2
    label: Odeur sucree de liquide dans l habitacle
    description: odeur sucree de liquide dans l habitacle
    risk_level: confort
    evidence:
      - 'Observation: odeur sucree de liquide dans l habitacle'
      - Vérification visuelle ou auditive
  - id: S3
    label: Moquette humide cote passager avant
    description: moquette humide cote passager avant
    risk_level: confort
    evidence:
      - 'Observation: moquette humide cote passager avant'
      - Vérification visuelle ou auditive
  - id: S4
    label: Chauffage qui ne chauffe plus ou peu
    description: chauffage qui ne chauffe plus ou peu
    risk_level: confort
    evidence:
      - 'Observation: chauffage qui ne chauffe plus ou peu'
      - Vérification visuelle ou auditive
  - id: S5
    label: Gargouillement dans le tableau de bord
    description: gargouillement dans le tableau de bord
    risk_level: confort
    evidence:
      - 'Observation: gargouillement dans le tableau de bord'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 15 ans ou fuite averee
    description: plus de 15 ans ou fuite averee
    risk_level: confort
    evidence:
      - 'Observation: plus de 15 ans ou fuite averee'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Radiateur de chauffage - Guide Diagnostic Complet

## Fonction et Rôle

Transferer la chaleur du liquide de refroidissement vers l'habitacle pour le confort des passagers. NE REFROIDIT PAS LE MOTEUR!

**Actions principales:** chauffer, transferer, diffuser, rechauffer l'habitacle

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- buee grasse persistante sur le pare-brise
- odeur sucree de liquide dans l habitacle
- moquette humide cote passager avant
- chauffage qui ne chauffe plus ou peu
- gargouillement dans le tableau de bord
- plus de 15 ans ou fuite averee

## Procédure de Diagnostic

Pour diagnostiquer un problème de radiateur de chauffage:

1. **Inspection visuelle** - Examiner l'état du radiateur de chauffage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- commande-de-ventilation
- filtre-d-habitacle
- pulseur-d-air-d-habitacle
- radiateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon radiateur de chauffage, vous devez connaître:

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
