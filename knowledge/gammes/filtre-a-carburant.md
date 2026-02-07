---
entity_type: gamme
title: Filtre à carburant
slug: filtre-a-carburant
pg_id: 9
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
    Retient l'eau et les impuretés du carburant pour protéger les injecteurs et
    la pompe
  must_be_true:
    - remplacer
    - changer
    - purger
  must_not_contain_concepts:
    - huile
    - air
    - habitacle
    - climatisation
    - pollen
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Perte de puissance progressive
    description: perte de puissance progressive
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance progressive'
      - Vérification visuelle ou auditive
  - id: S2
    label: A-coups a l acceleration
    description: a-coups a l acceleration
    risk_level: confort
    evidence:
      - 'Observation: a-coups a l acceleration'
      - Vérification visuelle ou auditive
  - id: S3
    label: Demarrage difficile ou laborieux
    description: demarrage difficile ou laborieux
    risk_level: confort
    evidence:
      - 'Observation: demarrage difficile ou laborieux'
      - Vérification visuelle ou auditive
  - id: S4
    label: Cliquetis ou rates moteur
    description: cliquetis ou rates moteur
    risk_level: confort
    evidence:
      - 'Observation: cliquetis ou rates moteur'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de carburant autour du vehicule
    description: odeur de carburant autour du vehicule
    risk_level: confort
    evidence:
      - 'Observation: odeur de carburant autour du vehicule'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 60 000 km ou 4 ans depuis le remplacement
    description: plus de 60 000 km ou 4 ans depuis le remplacement
    risk_level: confort
    evidence:
      - 'Observation: plus de 60 000 km ou 4 ans depuis le remplacement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Filtre à carburant - Guide Diagnostic Complet

## Fonction et Rôle

Retient l'eau et les impuretés du carburant pour protéger les injecteurs et la pompe

**Actions principales:** remplacer, changer, purger

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- perte de puissance progressive
- a-coups a l acceleration
- demarrage difficile ou laborieux
- cliquetis ou rates moteur
- odeur de carburant autour du vehicule
- plus de 60 000 km ou 4 ans depuis le remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de filtre à carburant:

1. **Inspection visuelle** - Examiner l'état du filtre à carburant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bougie-d-allumage
- bougie-de-prechauffage
- filtre-a-air
- filtre-a-huile
- filtre-d-habitacle
- pompe-a-carburant

## Critères de Compatibilité

Pour commander le bon filtre à carburant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "lavable"
