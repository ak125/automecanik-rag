---
entity_type: gamme
title: Faisceau d'allumage
slug: faisceau-d-allumage
pg_id: 685
category: allumage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmettre la haute tension de la bobine aux bougies d'allumage sans perte
  must_be_true:
    - transmettre
    - conduire
    - acheminer
  must_not_contain_concepts:
    - diesel
    - prechauffage
    - incandescence
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
    label: Rates moteur a l acceleration ou au ralenti
    description: rates moteur a l acceleration ou au ralenti
    risk_level: confort
    evidence:
      - 'Observation: rates moteur a l acceleration ou au ralenti'
      - Vérification visuelle ou auditive
  - id: S2
    label: Demarrage difficile surtout par temps humide
    description: demarrage difficile surtout par temps humide
    risk_level: confort
    evidence:
      - 'Observation: demarrage difficile surtout par temps humide'
      - Vérification visuelle ou auditive
  - id: S3
    label: Consommation de carburant anormalement elevee
    description: consommation de carburant anormalement elevee
    risk_level: confort
    evidence:
      - 'Observation: consommation de carburant anormalement elevee'
      - Vérification visuelle ou auditive
  - id: S4
    label: Arc electrique visible sur les cables dans le noir
    description: arc electrique visible sur les cables dans le noir
    risk_level: confort
    evidence:
      - 'Observation: arc electrique visible sur les cables dans le noir'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur d essence au pot d echappement
    description: odeur d essence au pot d echappement
    risk_level: confort
    evidence:
      - 'Observation: odeur d essence au pot d echappement'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 80 000 km sans remplacement
    description: plus de 80 000 km sans remplacement
    risk_level: confort
    evidence:
      - 'Observation: plus de 80 000 km sans remplacement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Faisceau d'allumage - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre la haute tension de la bobine aux bougies d'allumage sans perte

**Actions principales:** transmettre, conduire, acheminer, vehiculer la haute tension, relier bobine et bougies

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- rates moteur a l acceleration ou au ralenti
- demarrage difficile surtout par temps humide
- consommation de carburant anormalement elevee
- arc electrique visible sur les cables dans le noir
- odeur d essence au pot d echappement
- plus de 80 000 km sans remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de faisceau d'allumage:

1. **Inspection visuelle** - Examiner l'état du faisceau d'allumage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- bobine-d-allumage
- bougie-d-allumage

## Critères de Compatibilité

Pour commander le bon faisceau d'allumage, vous devez connaître:

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
