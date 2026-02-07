---
entity_type: gamme
title: Filtre à air
slug: filtre-a-air
pg_id: 8
category: filtration
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Filtre l'air d'admission pour protéger le moteur des poussières et
    particules avant la combustion
  must_be_true:
    - filtrer
    - protéger
    - retenir poussières
    - air propre
  must_not_contain_concepts:
    - huile
    - lubrification
    - carter
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
    label: Perte de puissance a l acceleration
    description: perte de puissance a l acceleration
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance a l acceleration'
      - Vérification visuelle ou auditive
  - id: S2
    label: Surconsommation de carburant anormale
    description: surconsommation de carburant anormale
    risk_level: confort
    evidence:
      - 'Observation: surconsommation de carburant anormale'
      - Vérification visuelle ou auditive
  - id: S3
    label: Fumee noire a l echappement
    description: fumee noire a l echappement
    risk_level: confort
    evidence:
      - 'Observation: fumee noire a l echappement'
      - Vérification visuelle ou auditive
  - id: S4
    label: Sifflement anormal a l admission
    description: sifflement anormal a l admission
    risk_level: confort
    evidence:
      - 'Observation: sifflement anormal a l admission'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de carburant non brule
    description: odeur de carburant non brule
    risk_level: confort
    evidence:
      - 'Observation: odeur de carburant non brule'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 30 000 km depuis le dernier changement
    description: plus de 30 000 km depuis le dernier changement
    risk_level: confort
    evidence:
      - 'Observation: plus de 30 000 km depuis le dernier changement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Filtre à air - Guide Diagnostic Complet

## Fonction et Rôle

Filtre l'air d'admission pour protéger le moteur des poussières et particules avant la combustion.

**Actions principales:** filtrer, protéger, retenir poussières, garantir air propre pour combustion

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- perte de puissance a l acceleration
- surconsommation de carburant anormale
- fumee noire a l echappement
- sifflement anormal a l admission
- odeur de carburant non brule
- plus de 30 000 km depuis le dernier changement

## Procédure de Diagnostic

Pour diagnostiquer un problème de filtre à air:

1. **Inspection visuelle** - Examiner l'état du filtre à air
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-position-papillon
- capteur-pression-du-tuyau-d-admission
- capteur-temperature-d-air-admission
- debitmetre-d-air
- filtre-a-carburant
- filtre-a-huile
- filtre-d-habitacle
- valve-de-reglage-du-ralenti

## Critères de Compatibilité

Pour commander le bon filtre à air, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "zero panne"
