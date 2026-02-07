---
entity_type: gamme
title: Evaporateur de climatisation
slug: evaporateur-de-climatisation
pg_id: 471
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
    Absorbe la chaleur de l'air habitacle pour produire du froid - Circuit
    habitacle uniquement
  must_be_true:
    - absorber la chaleur
  must_not_contain_concepts:
    - moteur
    - refroidissement
    - radiateur
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
    label: Climatisation inefficace malgre recharge recente
    description: climatisation inefficace malgre recharge recente
    risk_level: confort
    evidence:
      - 'Observation: climatisation inefficace malgre recharge recente'
      - Vérification visuelle ou auditive
  - id: S2
    label: Odeur de moisi ou d humidite a la ventilation
    description: odeur de moisi ou d humidite a la ventilation
    risk_level: confort
    evidence:
      - 'Observation: odeur de moisi ou d humidite a la ventilation'
      - Vérification visuelle ou auditive
  - id: S3
    label: Buee persistante sur le pare-brise en mode clim
    description: buee persistante sur le pare-brise en mode clim
    risk_level: confort
    evidence:
      - 'Observation: buee persistante sur le pare-brise en mode clim'
      - Vérification visuelle ou auditive
  - id: S4
    label: Flaque d eau anormale sous le tableau de bord
    description: flaque d eau anormale sous le tableau de bord
    risk_level: confort
    evidence:
      - 'Observation: flaque d eau anormale sous le tableau de bord'
      - Vérification visuelle ou auditive
  - id: S5
    label: Bruit gargouillement boitier ventilation
    description: bruit gargouillement boitier ventilation
    risk_level: confort
    evidence:
      - 'Observation: bruit gargouillement boitier ventilation'
      - Vérification visuelle ou auditive
  - id: S6
    label: Mauvaises odeurs des l enclenchement de la clim
    description: mauvaises odeurs des l enclenchement de la clim
    risk_level: confort
    evidence:
      - 'Observation: mauvaises odeurs des l enclenchement de la clim'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Evaporateur de climatisation - Guide Diagnostic Complet

## Fonction et Rôle

Absorbe la chaleur de l'air habitacle pour produire du froid - Circuit habitacle uniquement

**Actions principales:** absorber la chaleur

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- climatisation inefficace malgre recharge recente
- odeur de moisi ou d humidite a la ventilation
- buee persistante sur le pare-brise en mode clim
- flaque d eau anormale sous le tableau de bord
- bruit gargouillement boitier ventilation
- mauvaises odeurs des l enclenchement de la clim

## Procédure de Diagnostic

Pour diagnostiquer un problème de evaporateur de climatisation:

1. **Inspection visuelle** - Examiner l'état du evaporateur de climatisation
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- compresseur-de-climatisation
- condenseur-de-climatisation
- detendeur-de-climatisation
- filtre-d-habitacle
- pulseur-d-air-d-habitacle

## Critères de Compatibilité

Pour commander le bon evaporateur de climatisation, vous devez connaître:

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
