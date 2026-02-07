---
entity_type: gamme
title: Bougie d'allumage
slug: bougie-d-allumage
pg_id: 686
category: allumage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Produire l'etincelle qui enflamme le melange air-essence - Fonctionne en
    continu moteur tournant
  must_be_true:
    - produire une etincelle
    - enflammer
    - allumer le melange
  must_not_contain_concepts:
    - diesel
    - prechauffage
    - incandescence
    - chambre de combustion diesel
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Demarrage difficile ou laborieux
    description: demarrage difficile ou laborieux
    risk_level: confort
    evidence:
      - 'Observation: demarrage difficile ou laborieux'
      - Vérification visuelle ou auditive
  - id: S2
    label: Rates moteur a froid ou a l acceleration
    description: rates moteur a froid ou a l acceleration
    risk_level: confort
    evidence:
      - 'Observation: rates moteur a froid ou a l acceleration'
      - Vérification visuelle ou auditive
  - id: S3
    label: Consommation de carburant excessive
    description: consommation de carburant excessive
    risk_level: confort
    evidence:
      - 'Observation: consommation de carburant excessive'
      - Vérification visuelle ou auditive
  - id: S4
    label: Voyant moteur allume code rate d allumage
    description: voyant moteur allume code rate d allumage
    risk_level: confort
    evidence:
      - 'Observation: voyant moteur allume code rate d allumage'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur essence echappement combustion incomplete
    description: odeur essence echappement combustion incomplete
    risk_level: confort
    evidence:
      - 'Observation: odeur essence echappement combustion incomplete'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 40 000 km sans remplacement standard
    description: plus de 40 000 km sans remplacement standard
    risk_level: confort
    evidence:
      - 'Observation: plus de 40 000 km sans remplacement standard'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Bougie d'allumage - Guide Diagnostic Complet

## Fonction et Rôle

Produire l'etincelle qui enflamme le melange air-essence - Fonctionne en continu moteur tournant

**Actions principales:** produire une etincelle, enflammer, allumer le melange, declencher la combustion, generer l'arc electrique

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- demarrage difficile ou laborieux
- rates moteur a froid ou a l acceleration
- consommation de carburant excessive
- voyant moteur allume code rate d allumage
- odeur essence echappement combustion incomplete
- plus de 40 000 km sans remplacement standard

## Procédure de Diagnostic

Pour diagnostiquer un problème de bougie d'allumage:

1. **Inspection visuelle** - Examiner l'état du bougie d'allumage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- bobine-d-allumage
- faisceau-d-allumage
- filtre-a-air
- filtre-a-carburant
- filtre-a-huile
- sonde-lambda

## Critères de Compatibilité

Pour commander le bon bougie d'allumage, vous devez connaître:

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
