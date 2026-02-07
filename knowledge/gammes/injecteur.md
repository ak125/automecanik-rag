---
entity_type: gamme
title: Injecteur
slug: injecteur
pg_id: 3902
category: alimentation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Pulveriser le carburant sous forme de fines gouttelettes dans la chambre de
    combustion
  must_be_true:
    - injecter
    - pulveriser
    - doser
  must_not_contain_concepts:
    - air
    - admission
    - debitmetre
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
    label: Rates d allumage ou rate sur un cylindre
    description: rates d allumage ou rate sur un cylindre
    risk_level: confort
    evidence:
      - 'Observation: rates d allumage ou rate sur un cylindre'
      - Vérification visuelle ou auditive
  - id: S2
    label: Fumee noire ou blanche a l echappement
    description: fumee noire ou blanche a l echappement
    risk_level: confort
    evidence:
      - 'Observation: fumee noire ou blanche a l echappement'
      - Vérification visuelle ou auditive
  - id: S3
    label: Claquement diesel anormal injection
    description: claquement diesel anormal injection
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement diesel anormal injection'
      - Vérification visuelle ou auditive
  - id: S4
    label: Surconsommation de carburant notable
    description: surconsommation de carburant notable
    risk_level: confort
    evidence:
      - 'Observation: surconsommation de carburant notable'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de carburant non brule
    description: odeur de carburant non brule
    risk_level: confort
    evidence:
      - 'Observation: odeur de carburant non brule'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 200 000 km sans controle injecteurs
    description: plus de 200 000 km sans controle injecteurs
    risk_level: confort
    evidence:
      - 'Observation: plus de 200 000 km sans controle injecteurs'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Injecteur - Guide Diagnostic Complet

## Fonction et Rôle

Pulveriser le carburant sous forme de fines gouttelettes dans la chambre de combustion

**Actions principales:** injecter, pulveriser, doser

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement diesel anormal injection**
  claquement diesel anormal injection

### 🟢 Autres Symptômes

- rates d allumage ou rate sur un cylindre
- fumee noire ou blanche a l echappement
- surconsommation de carburant notable
- odeur de carburant non brule
- plus de 200 000 km sans controle injecteurs

## Procédure de Diagnostic

Pour diagnostiquer un problème de injecteur:

1. **Inspection visuelle** - Examiner l'état du injecteur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-de-cognement
- corps-papillon
- joint-d-injecteur
- pompe-a-carburant
- pompe-a-injection
- vanne-egr

## Critères de Compatibilité

Pour commander le bon injecteur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"
