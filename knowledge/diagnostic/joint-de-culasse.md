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
  - if: symptome_mayonnaise-sous-le-bouchon-d-huile
    then: verifier_piece
  - if: symptome_fumee-blanche-epaisse-a-l-echappement
    then: diagnostic_approfondi
  - if: symptome_bulles-d-air-dans-le-vase
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Mayonnaise sous le bouchon d huile
    description: mayonnaise sous le bouchon d huile ou de ldr
    risk_level: confort
    evidence:
      - 'Observation: mayonnaise sous le bouchon d huile'
      - Vérification visuelle ou auditive
  - id: S2
    label: Fumee blanche epaisse a l echappement
    description: fumee blanche epaisse a l echappement
    risk_level: confort
    evidence:
      - 'Observation: fumee blanche epaisse a l echappement'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bulles d air dans le vase
    description: bulles d air dans le vase d expansion
    risk_level: confort
    evidence:
      - 'Observation: bulles d air dans le vase'
      - Vérification visuelle ou auditive
  - id: S4
    label: Surchauffe repetee du moteur
    description: surchauffe repetee du moteur
    risk_level: confort
    evidence:
      - 'Observation: surchauffe repetee du moteur'
      - Vérification visuelle ou auditive
  - id: S5
    label: Niveau de ldr qui baisse sans
    description: niveau de ldr qui baisse sans fuite visible
    risk_level: confort
    evidence:
      - 'Observation: niveau de ldr qui baisse sans'
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
# Joint de culasse - Guide Complet

## Fonction

Assurer l'etancheite entre le bloc moteur et la culasse, maintenir la pression de compression

## Symptômes de défaillance

### Mayonnaise sous le bouchon d huile

mayonnaise sous le bouchon d huile ou de ldr

### Fumee blanche epaisse a l echappement

fumee blanche epaisse a l echappement

### Bulles d air dans le vase

bulles d air dans le vase d expansion

### Surchauffe repetee du moteur

surchauffe repetee du moteur

### Niveau de ldr qui baisse sans

niveau de ldr qui baisse sans fuite visible

### Huile dans le liquide de refroidissement

huile dans le liquide de refroidissement

## Diagnostic

Pour diagnostiquer un problème de joint de culasse:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- bagues-d-etancheite-moteur
- filtre-a-huile
- joint-de-cache-culbuteurs
- joint-de-collecteur
- vis-de-culasse

## Compatibilité

Pour commander le bon joint de culasse, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
