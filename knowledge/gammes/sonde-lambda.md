---
entity_type: gamme
title: Sonde lambda
slug: sonde-lambda
pg_id: 3922
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
    Mesurer le taux d'oxygene dans les gaz d'echappement pour optimiser la
    combustion et le fonctionnement du catalyseur
  must_be_true:
    - mesurer
    - detecter
    - analyser
  must_not_contain_concepts:
    - injecteur
    - pompe
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
    label: Voyant moteur allume avec codes p0130 a p0167
    description: voyant moteur allume avec codes p0130 a p0167
    risk_level: confort
    evidence:
      - 'Observation: voyant moteur allume avec codes p0130 a p0167'
      - Vérification visuelle ou auditive
  - id: S2
    label: Surconsommation de carburant inexpliquee
    description: surconsommation de carburant inexpliquee
    risk_level: confort
    evidence:
      - 'Observation: surconsommation de carburant inexpliquee'
      - Vérification visuelle ou auditive
  - id: S3
    label: Perte de puissance et ralenti instable
    description: perte de puissance et ralenti instable
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance et ralenti instable'
      - Vérification visuelle ou auditive
  - id: S4
    label: Fumee noire excessive a l echappement
    description: fumee noire excessive a l echappement
    risk_level: confort
    evidence:
      - 'Observation: fumee noire excessive a l echappement'
      - Vérification visuelle ou auditive
  - id: S5
    label: Controle technique refuse pour pollution
    description: controle technique refuse pour pollution
    risk_level: confort
    evidence:
      - 'Observation: controle technique refuse pour pollution'
      - Vérification visuelle ou auditive
  - id: S6
    label: Sifflement bruit anormal niveau echappement
    description: sifflement bruit anormal niveau echappement
    risk_level: confort
    evidence:
      - 'Observation: sifflement bruit anormal niveau echappement'
      - Vérification visuelle ou auditive
  - id: S7
    label: Odeur d essence non brulee a l echappement
    description: odeur d essence non brulee a l echappement
    risk_level: confort
    evidence:
      - 'Observation: odeur d essence non brulee a l echappement'
      - Vérification visuelle ou auditive
  - id: S8
    label: Sonde service depuis plus remplacement
    description: sonde service depuis plus remplacement
    risk_level: confort
    evidence:
      - 'Observation: sonde service depuis plus remplacement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Sonde lambda - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer le taux d'oxygene dans les gaz d'echappement pour optimiser la combustion et le fonctionnement du catalyseur

**Actions principales:** mesurer, detecter, analyser, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant moteur allume avec codes p0130 a p0167
- surconsommation de carburant inexpliquee
- perte de puissance et ralenti instable
- fumee noire excessive a l echappement
- controle technique refuse pour pollution
- sifflement bruit anormal niveau echappement

## Procédure de Diagnostic

Pour diagnostiquer un problème de sonde lambda:

1. **Inspection visuelle** - Examiner l'état du sonde lambda
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- bougie-d-allumage
- bougie-de-prechauffage
- catalyseur
- fap

## Critères de Compatibilité

Pour commander le bon sonde lambda, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "corrige la pollution"
