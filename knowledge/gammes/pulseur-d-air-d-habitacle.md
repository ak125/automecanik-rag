---
entity_type: gamme
title: Pulseur d'air d'habitacle
slug: pulseur-d-air-d-habitacle
pg_id: 2669
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
    Souffler l'air dans l'habitacle pour le chauffage ou la climatisation. NE
    REFROIDIT PAS LE MOTEUR!
  must_be_true:
    - souffler
    - pulser
    - ventiler
  must_not_contain_concepts:
    - refroidissement moteur
    - radiateur moteur
    - motoventilateur
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
    label: Aucune ventilation soit vitesse selectionnee
    description: aucune ventilation soit vitesse selectionnee
    risk_level: confort
    evidence:
      - 'Observation: aucune ventilation soit vitesse selectionnee'
      - Vérification visuelle ou auditive
  - id: S2
    label: Seulement certaines vitesses ventilation fonctionnent
    description: seulement certaines vitesses ventilation fonctionnent
    risk_level: confort
    evidence:
      - 'Observation: seulement certaines vitesses ventilation fonctionnent'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit grincement frottement mise marche
    description: bruit grincement frottement mise marche
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit grincement frottement mise marche'
      - Vérification visuelle ou auditive
  - id: S4
    label: Ventilation demarre puis arrete facon
    description: ventilation demarre puis arrete facon
    risk_level: confort
    evidence:
      - 'Observation: ventilation demarre puis arrete facon'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de brule a l enclenchement du chauffage
    description: odeur de brule a l enclenchement du chauffage
    risk_level: confort
    evidence:
      - 'Observation: odeur de brule a l enclenchement du chauffage'
      - Vérification visuelle ou auditive
  - id: S6
    label: Fusible pulseur grille visible boite
    description: fusible pulseur grille visible boite
    risk_level: confort
    evidence:
      - 'Observation: fusible pulseur grille visible boite'
      - Vérification visuelle ou auditive
  - id: S7
    label: Ventilation inefficace malgre reglage vitesse
    description: ventilation inefficace malgre reglage vitesse
    risk_level: confort
    evidence:
      - 'Observation: ventilation inefficace malgre reglage vitesse'
      - Vérification visuelle ou auditive
  - id: S8
    label: Pulseur service depuis plus controle
    description: pulseur service depuis plus controle
    risk_level: confort
    evidence:
      - 'Observation: pulseur service depuis plus controle'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Pulseur d'air d'habitacle - Guide Diagnostic Complet

## Fonction et Rôle

Souffler l'air dans l'habitacle pour le chauffage ou la climatisation. NE REFROIDIT PAS LE MOTEUR!

**Actions principales:** souffler, pulser, ventiler, diffuser l'air

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit grincement frottement mise marche**
  bruit grincement frottement mise marche

### 🟢 Autres Symptômes

- aucune ventilation soit vitesse selectionnee
- seulement certaines vitesses ventilation fonctionnent
- ventilation demarre puis arrete facon
- odeur de brule a l enclenchement du chauffage
- fusible pulseur grille visible boite
- ventilation inefficace malgre reglage vitesse

## Procédure de Diagnostic

Pour diagnostiquer un problème de pulseur d'air d'habitacle:

1. **Inspection visuelle** - Examiner l'état du pulseur d'air d'habitacle
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- commande-de-ventilation
- compresseur-de-climatisation
- condenseur-de-climatisation
- detendeur-de-climatisation
- evaporateur-de-climatisation
- filtre-d-habitacle
- radiateur-de-chauffage

## Critères de Compatibilité

Pour commander le bon pulseur d'air d'habitacle, vous devez connaître:

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
