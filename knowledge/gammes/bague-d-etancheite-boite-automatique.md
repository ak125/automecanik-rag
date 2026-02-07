---
entity_type: gamme
title: Bague d'étanchéité boîte automatique
slug: bague-d-etancheite-boite-automatique
pg_id: 626
category: moteur
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Assurer l'etancheite des arbres de la boite automatique
  must_be_true:
    - assurer l'etancheite
    - isoler
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
    label: Fuites d huile sous la boite
    description: fuites d huile sous la boite
    risk_level: confort
    evidence:
      - 'Observation: fuites d huile sous la boite'
      - Vérification visuelle ou auditive
  - id: S2
    label: Niveau d huile qui baisse
    description: niveau d huile qui baisse
    risk_level: confort
    evidence:
      - 'Observation: niveau d huile qui baisse'
      - Vérification visuelle ou auditive
  - id: S3
    label: Taches au sol au niveau de la transmission
    description: taches au sol au niveau de la transmission
    risk_level: confort
    evidence:
      - 'Observation: taches au sol au niveau de la transmission'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Bague d'étanchéité boîte automatique - Guide Diagnostic Complet

## Fonction et Rôle

Assurer l'etancheite des arbres de la boite automatique

**Actions principales:** assurer l'etancheite, isoler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- fuites d huile sous la boite
- niveau d huile qui baisse
- taches au sol au niveau de la transmission

## Procédure de Diagnostic

Pour diagnostiquer un problème de bague d'étanchéité boîte automatique:

1. **Inspection visuelle** - Examiner l'état du bague d'étanchéité boîte automatique
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- joint-spi
- boite-automatique

## Critères de Compatibilité

Pour commander le bon bague d'étanchéité boîte automatique, vous devez connaître:

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
