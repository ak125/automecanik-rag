---
entity_type: gamme
title: Joint tige de soupape
slug: joint-tige-de-soupape
pg_id: 322
category: moteur
subcategory: joints
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Empecher l'huile de descendre dans la chambre de combustion
  must_be_true:
    - assurer l'etancheite
    - empecher
  must_not_contain_concepts:
    - freinage
    - climatisation
    - direction
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
symptoms:
  - id: S1
    label: Fumee bleue au demarrage
    description: fumee bleue au demarrage
    risk_level: confort
    evidence:
      - 'Observation: fumee bleue au demarrage'
      - Vérification visuelle ou auditive
  - id: S2
    label: Consommation d huile excessive
    description: consommation d huile excessive
    risk_level: confort
    evidence:
      - 'Observation: consommation d huile excessive'
      - Vérification visuelle ou auditive
  - id: S3
    label: Depots sur les bougies
    description: depots sur les bougies
    risk_level: confort
    evidence:
      - 'Observation: depots sur les bougies'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Joint tige de soupape - Guide Diagnostic Complet

## Fonction et Rôle

Empecher l'huile de descendre dans la chambre de combustion

**Actions principales:** assurer l'etancheite, empecher

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- fumee bleue au demarrage
- consommation d huile excessive
- depots sur les bougies

## Procédure de Diagnostic

Pour diagnostiquer un problème de joint tige de soupape:

1. **Inspection visuelle** - Examiner l'état du joint tige de soupape
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bagues-d-etancheite-moteur
- joint-de-cache-culbuteurs
- joint-de-carter-d-huile
- joint-de-collecteur
- joint-de-culasse
- pochette-joints-moteur
- vis-de-culasse

## Critères de Compatibilité

Pour commander le bon joint tige de soupape, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"
