---
entity_type: gamme
title: Cylindre de roue
slug: cylindre-de-roue
pg_id: 277
category: freinage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmettre la pression hydraulique aux machoires
  must_be_true:
    - pousser les machoires
    - transmettre la pression
    - actionner le freinage tambour
  must_not_contain_concepts:
    - disque
    - etrier
    - plaquette
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_traces-de-liquide-sur-le-dos
    then: verifier_piece
  - if: symptome_interieur-du-tambour-mouille-ou-gras
    then: diagnostic_approfondi
  - if: symptome_niveau-de-liquide-de-frein-qui
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Traces de liquide sur le dos
    description: traces de liquide sur le dos des machoires
    risk_level: confort
    evidence:
      - 'Observation: traces de liquide sur le dos'
      - Vérification visuelle ou auditive
  - id: S2
    label: Interieur du tambour mouille ou gras
    description: interieur du tambour mouille ou gras
    risk_level: confort
    evidence:
      - 'Observation: interieur du tambour mouille ou gras'
      - Vérification visuelle ou auditive
  - id: S3
    label: Niveau de liquide de frein qui
    description: niveau de liquide de frein qui baisse
    risk_level: securite
    evidence:
      - 'Observation: niveau de liquide de frein qui'
      - Vérification visuelle ou auditive
  - id: S4
    label: Freinage arriere desequilibre
    description: freinage arriere desequilibre
    risk_level: securite
    evidence:
      - 'Observation: freinage arriere desequilibre'
      - Vérification visuelle ou auditive
  - id: S5
    label: Machoires usees de facon asymetrique
    description: machoires usees de facon asymetrique
    risk_level: confort
    evidence:
      - 'Observation: machoires usees de facon asymetrique'
      - Vérification visuelle ou auditive
  - id: S6
    label: Fuite visible au niveau du cylindre
    description: fuite visible au niveau du cylindre
    risk_level: confort
    evidence:
      - 'Observation: fuite visible au niveau du cylindre'
      - Vérification visuelle ou auditive
  - id: S7
    label: Bruit de frottement a l arriere
    description: bruit de frottement a l arriere
    risk_level: confort
    evidence:
      - 'Observation: bruit de frottement a l arriere'
      - Vérification visuelle ou auditive
  - id: S8
    label: Odeur de liquide de frein pres
    description: odeur de liquide de frein pres des roues arriere
    risk_level: securite
    evidence:
      - 'Observation: odeur de liquide de frein pres'
      - Vérification visuelle ou auditive
  - id: S9
    label: Plus de 100 000 km sans
    description: plus de 100 000 km sans controle des cylindres
    risk_level: confort
    evidence:
      - 'Observation: plus de 100 000 km sans'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Cylindre de roue - Guide Complet

## Fonction

Transmettre la pression hydraulique aux machoires

## Symptômes de défaillance

### Traces de liquide sur le dos

traces de liquide sur le dos des machoires

### Interieur du tambour mouille ou gras

interieur du tambour mouille ou gras

### Niveau de liquide de frein qui

niveau de liquide de frein qui baisse

### Freinage arriere desequilibre

freinage arriere desequilibre

### Machoires usees de facon asymetrique

machoires usees de facon asymetrique

### Fuite visible au niveau du cylindre

fuite visible au niveau du cylindre

### Bruit de frottement a l arriere

bruit de frottement a l arriere

### Odeur de liquide de frein pres

odeur de liquide de frein pres des roues arriere

## Diagnostic

Pour diagnostiquer un problème de cylindre de roue:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- cable-de-frein-a-main
- disque-de-frein
- etrier-de-frein
- flexible-de-frein
- kit-de-freins-arriere

## Compatibilité

Pour commander le bon cylindre de roue, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
