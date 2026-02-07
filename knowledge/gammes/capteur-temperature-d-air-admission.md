---
entity_type: gamme
title: Capteur température d'air admission
slug: capteur-temperature-d-air-admission
pg_id: 3939
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
    Mesurer la temperature de l'air entrant dans le moteur pour optimiser le
    melange air-carburant
  must_be_true:
    - mesurer
    - detecter
    - transmettre
  must_not_contain_concepts:
    - echappement
    - refroidissement
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Surconsommation de carburant anormale
    description: surconsommation de carburant anormale
    risk_level: confort
    evidence:
      - 'Observation: surconsommation de carburant anormale'
      - Vérification visuelle ou auditive
  - id: S2
    label: Ralenti instable surtout a froid
    description: ralenti instable surtout a froid
    risk_level: confort
    evidence:
      - 'Observation: ralenti instable surtout a froid'
      - Vérification visuelle ou auditive
  - id: S3
    label: Sifflement anormal a l admission
    description: sifflement anormal a l admission
    risk_level: confort
    evidence:
      - 'Observation: sifflement anormal a l admission'
      - Vérification visuelle ou auditive
  - id: S4
    label: Fumee noire a l echappement
    description: fumee noire a l echappement
    risk_level: confort
    evidence:
      - 'Observation: fumee noire a l echappement'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de carburant non brule
    description: odeur de carburant non brule
    risk_level: confort
    evidence:
      - 'Observation: odeur de carburant non brule'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 150 000 km sans verification
    description: plus de 150 000 km sans verification
    risk_level: confort
    evidence:
      - 'Observation: plus de 150 000 km sans verification'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Capteur température d'air admission - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la temperature de l'air entrant dans le moteur pour optimiser le melange air-carburant

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- surconsommation de carburant anormale
- ralenti instable surtout a froid
- sifflement anormal a l admission
- fumee noire a l echappement
- odeur de carburant non brule
- plus de 150 000 km sans verification

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur température d'air admission:

1. **Inspection visuelle** - Examiner l'état du capteur température d'air admission
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- catalyseur
- corps-papillon
- debitmetre-d-air
- fap
- filtre-a-air

## Critères de Compatibilité

Pour commander le bon capteur température d'air admission, vous devez connaître:

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
