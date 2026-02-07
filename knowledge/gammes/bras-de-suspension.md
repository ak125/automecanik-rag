---
entity_type: gamme
title: Bras de suspension
slug: bras-de-suspension
pg_id: 273
category: direction
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Maintenir la geometrie de la roue et supporter les efforts verticaux -
    Element structurel de la suspension
  must_be_true:
    - maintenir
    - supporter
    - guider
  must_not_contain_concepts:
    - direction
    - cremailliere
    - volant
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: vibrations_anormales
    then: verifier_equilibrage_et_fixations
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Claquements ou cognements sur routes degradees
    description: claquements ou cognements sur routes degradees
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquements ou cognements sur routes degradees'
      - Vérification visuelle ou auditive
  - id: S2
    label: Vehicule qui tire a droite ou a gauche au freinage
    description: vehicule qui tire a droite ou a gauche au freinage
    risk_level: securite
    evidence:
      - 'Observation: vehicule qui tire a droite ou a gauche au freinage'
      - Vérification visuelle ou auditive
  - id: S3
    label: Usure irreguliere pneus epaules interieures
    description: usure irreguliere pneus epaules interieures
    risk_level: securite
    evidence:
      - 'Observation: usure irreguliere pneus epaules interieures'
      - Vérification visuelle ou auditive
  - id: S4
    label: Vibrations dans le volant a certaines vitesses
    description: vibrations dans le volant a certaines vitesses
    risk_level: confort
    evidence:
      - 'Observation: vibrations dans le volant a certaines vitesses'
      - Vérification visuelle ou auditive
  - id: S5
    label: Silentblocs fissures ou decolles visibles
    description: silentblocs fissures ou decolles visibles
    risk_level: confort
    evidence:
      - 'Observation: silentblocs fissures ou decolles visibles'
      - Vérification visuelle ou auditive
  - id: S6
    label: Tenue de route degradee en virage
    description: tenue de route degradee en virage
    risk_level: confort
    evidence:
      - 'Observation: tenue de route degradee en virage'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Bras de suspension - Guide Diagnostic Complet

## Fonction et Rôle

Maintenir la geometrie de la roue et supporter les efforts verticaux - Element structurel de la suspension

**Actions principales:** maintenir, supporter, guider, articuler, positionner la roue

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquements ou cognements sur routes degradees**
  claquements ou cognements sur routes degradees

### 🟡 Symptômes de Sécurité

- **Vehicule qui tire a droite ou a gauche au freinage**
  vehicule qui tire a droite ou a gauche au freinage
- **Usure irreguliere pneus epaules interieures**
  usure irreguliere pneus epaules interieures

### 🟢 Autres Symptômes

- vibrations dans le volant a certaines vitesses
- silentblocs fissures ou decolles visibles
- tenue de route degradee en virage

## Procédure de Diagnostic

Pour diagnostiquer un problème de bras de suspension:

1. **Inspection visuelle** - Examiner l'état du bras de suspension
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- amortisseur
- barre-de-direction
- biellette-de-barre-stabilisatrice
- rotule-de-direction
- rotule-de-suspension

## Critères de Compatibilité

Pour commander le bon bras de suspension, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"
