---
entity_type: gamme
title: Joint de culasse
slug: joint-de-culasse
pg_id: 318
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
  role_summary: >-
    Assurer l'etancheite entre le bloc moteur et la culasse, maintenir la
    pression de compression
  must_be_true:
    - assurer l'etancheite
    - empecher les fuites
    - separer les fluides
  must_not_contain_concepts:
    - boite de vitesses
    - electronique
    - reparation
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
    label: Mayonnaise sous le bouchon d huile ou de ldr
    description: mayonnaise sous le bouchon d huile ou de ldr
    risk_level: confort
    evidence:
      - 'Observation: mayonnaise sous le bouchon d huile ou de ldr'
      - Vérification visuelle ou auditive
  - id: S2
    label: Fumee blanche epaisse a l echappement
    description: fumee blanche epaisse a l echappement
    risk_level: confort
    evidence:
      - 'Observation: fumee blanche epaisse a l echappement'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bulles d air dans le vase d expansion
    description: bulles d air dans le vase d expansion
    risk_level: confort
    evidence:
      - 'Observation: bulles d air dans le vase d expansion'
      - Vérification visuelle ou auditive
  - id: S4
    label: Surchauffe repetee du moteur
    description: surchauffe repetee du moteur
    risk_level: confort
    evidence:
      - 'Observation: surchauffe repetee du moteur'
      - Vérification visuelle ou auditive
  - id: S5
    label: Niveau de ldr qui baisse sans fuite visible
    description: niveau de ldr qui baisse sans fuite visible
    risk_level: confort
    evidence:
      - 'Observation: niveau de ldr qui baisse sans fuite visible'
      - Vérification visuelle ou auditive
  - id: S6
    label: Huile dans le liquide de refroidissement
    description: huile dans le liquide de refroidissement
    risk_level: confort
    evidence:
      - 'Observation: huile dans le liquide de refroidissement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Joint de culasse - Guide Diagnostic Complet

## Fonction et Rôle

Assurer l'etancheite entre le bloc moteur et la culasse, maintenir la pression de compression

**Actions principales:** assurer l'etancheite, empecher les fuites, separer les fluides

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- mayonnaise sous le bouchon d huile ou de ldr
- fumee blanche epaisse a l echappement
- bulles d air dans le vase d expansion
- surchauffe repetee du moteur
- niveau de ldr qui baisse sans fuite visible
- huile dans le liquide de refroidissement

## Procédure de Diagnostic

Pour diagnostiquer un problème de joint de culasse:

1. **Inspection visuelle** - Examiner l'état du joint de culasse
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bagues-d-etancheite-moteur
- filtre-a-huile
- joint-de-cache-culbuteurs
- joint-de-collecteur
- vis-de-culasse

## Critères de Compatibilité

Pour commander le bon joint de culasse, vous devez connaître:

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
