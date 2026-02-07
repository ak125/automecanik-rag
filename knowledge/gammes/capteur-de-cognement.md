---
entity_type: gamme
title: Capteur de cognement
slug: capteur-de-cognement
pg_id: 3921
category: capteurs
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Detecter les vibrations anormales du moteur liees au cliquetis et informer
    le calculateur pour ajuster l'avance
  must_be_true:
    - detecter
    - mesurer
    - transmettre
  must_not_contain_concepts:
    - allumage
    - bougie
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
symptoms:
  - id: S1
    label: Voyant moteur allume avec code p0325 ou p0327
    description: voyant moteur allume avec code p0325 ou p0327
    risk_level: confort
    evidence:
      - 'Observation: voyant moteur allume avec code p0325 ou p0327'
      - Vérification visuelle ou auditive
  - id: S2
    label: Cliquetis metallique a l acceleration detonation
    description: cliquetis metallique a l acceleration detonation
    risk_level: confort
    evidence:
      - 'Observation: cliquetis metallique a l acceleration detonation'
      - Vérification visuelle ou auditive
  - id: S3
    label: Perte de puissance notable allumage retarde
    description: perte de puissance notable allumage retarde
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance notable allumage retarde'
      - Vérification visuelle ou auditive
  - id: S4
    label: Surconsommation de carburant anormale
    description: surconsommation de carburant anormale
    risk_level: confort
    evidence:
      - 'Observation: surconsommation de carburant anormale'
      - Vérification visuelle ou auditive
  - id: S5
    label: Fumee noire a l echappement
    description: fumee noire a l echappement
    risk_level: confort
    evidence:
      - 'Observation: fumee noire a l echappement'
      - Vérification visuelle ou auditive
  - id: S6
    label: Moteur qui chauffe plus que d habitude
    description: moteur qui chauffe plus que d habitude
    risk_level: confort
    evidence:
      - 'Observation: moteur qui chauffe plus que d habitude'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Capteur de cognement - Guide Diagnostic Complet

## Fonction et Rôle

Detecter les vibrations anormales du moteur liees au cliquetis et informer le calculateur pour ajuster l'avance

**Actions principales:** detecter, mesurer, transmettre, analyser

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant moteur allume avec code p0325 ou p0327
- cliquetis metallique a l acceleration detonation
- perte de puissance notable allumage retarde
- surconsommation de carburant anormale
- fumee noire a l echappement
- moteur qui chauffe plus que d habitude

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur de cognement:

1. **Inspection visuelle** - Examiner l'état du capteur de cognement
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-impulsion
- corps-papillon
- debitmetre-d-air
- injecteur

## Critères de Compatibilité

Pour commander le bon capteur de cognement, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "corrige la panne"
