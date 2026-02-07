---
entity_type: gamme
title: Joint de collecteur
slug: joint-de-collecteur
pg_id: 40
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
  role_summary: Assurer l'etancheite entre le collecteur et la culasse
  must_be_true:
    - assurer l'etancheite
    - empecher les fuites
    - separer les fluides
  must_not_contain_concepts:
    - boite de vitesses
    - electronique
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_sifflement-ou-souffle-a-l-echappement
    then: verifier_piece
  - if: symptome_bruit-de-claquement-a-froid-qui
    then: diagnostic_approfondi
  - if: symptome_ralenti-instable-prise-d-air-admission
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Sifflement ou souffle a l echappement
    description: sifflement ou souffle a l echappement
    risk_level: confort
    evidence:
      - 'Observation: sifflement ou souffle a l echappement'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit de claquement a froid qui
    description: bruit de claquement a froid qui disparait a chaud
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit de claquement a froid qui'
      - Vérification visuelle ou auditive
  - id: S3
    label: Ralenti instable prise d air admission
    description: ralenti instable prise d air admission
    risk_level: confort
    evidence:
      - 'Observation: ralenti instable prise d air admission'
      - Vérification visuelle ou auditive
  - id: S4
    label: Suie noire visible autour du joint
    description: suie noire visible autour du joint d echappement
    risk_level: confort
    evidence:
      - 'Observation: suie noire visible autour du joint'
      - Vérification visuelle ou auditive
  - id: S5
    label: Voyant moteur allume melange perturbe
    description: voyant moteur allume melange perturbe
    risk_level: confort
    evidence:
      - 'Observation: voyant moteur allume melange perturbe'
      - Vérification visuelle ou auditive
  - id: S6
    label: Odeur d echappement dans l habitacle
    description: odeur d echappement dans l habitacle
    risk_level: confort
    evidence:
      - 'Observation: odeur d echappement dans l habitacle'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Joint de collecteur - Guide Complet

## Fonction

Assurer l'etancheite entre le collecteur et la culasse

## Symptômes de défaillance

### Sifflement ou souffle a l echappement

sifflement ou souffle a l echappement

### Bruit de claquement a froid qui

bruit de claquement a froid qui disparait a chaud

### Ralenti instable prise d air admission

ralenti instable prise d air admission

### Suie noire visible autour du joint

suie noire visible autour du joint d echappement

### Voyant moteur allume melange perturbe

voyant moteur allume melange perturbe

### Odeur d echappement dans l habitacle

odeur d echappement dans l habitacle

## Diagnostic

Pour diagnostiquer un problème de joint de collecteur:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- bagues-d-etancheite-moteur
- joint-de-cache-culbuteurs
- joint-de-culasse
- soupape-d-admission
- soupape-d-echappement

## Compatibilité

Pour commander le bon joint de collecteur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
