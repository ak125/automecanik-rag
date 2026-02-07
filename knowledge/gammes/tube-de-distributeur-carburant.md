---
entity_type: gamme
title: Tube de distributeur carburant
slug: tube-de-distributeur-carburant
pg_id: 3964
category: alimentation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Repartir le carburant de la rampe vers chaque injecteur
  must_be_true:
    - distribuer
    - repartir
    - alimenter
  must_not_contain_concepts:
    - freinage
    - climatisation
    - distribution
    - embrayage
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
    label: Fuite de carburant sur la rampe
    description: fuite de carburant sur la rampe
    risk_level: confort
    evidence:
      - 'Observation: fuite de carburant sur la rampe'
      - Vérification visuelle ou auditive
  - id: S2
    label: Odeur de gasoil ou essence
    description: odeur de gasoil ou essence
    risk_level: confort
    evidence:
      - 'Observation: odeur de gasoil ou essence'
      - Vérification visuelle ou auditive
  - id: S3
    label: Pression d injection instable
    description: pression d injection instable
    risk_level: confort
    evidence:
      - 'Observation: pression d injection instable'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Tube de distributeur carburant - Guide Diagnostic Complet

## Fonction et Rôle

Repartir le carburant de la rampe vers chaque injecteur

**Actions principales:** distribuer, repartir, alimenter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- fuite de carburant sur la rampe
- odeur de gasoil ou essence
- pression d injection instable

## Procédure de Diagnostic

Pour diagnostiquer un problème de tube de distributeur carburant:

1. **Inspection visuelle** - Examiner l'état du tube de distributeur carburant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- rampe-d-injection
- injecteur

## Critères de Compatibilité

Pour commander le bon tube de distributeur carburant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare l'injection"
