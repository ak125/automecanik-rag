---
entity_type: gamme
title: Mâchoires de frein
slug: machoires-de-frein
pg_id: 70
category: freinage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Creer la friction a l'interieur du tambour
  must_be_true:
    - frotter
    - exercer une pression interne
    - s'user progressivement
  must_not_contain_concepts:
    - disque
    - plaquette
    - etrier
    - ventile
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_frein-a-main-qui-ne-tient
    then: verifier_piece
  - if: symptome_bruit-de-frottement-metallique-a-l
    then: diagnostic_approfondi
  - if: symptome_tambour-raye-ou-strie-a-l
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Frein a main qui ne tient
    description: frein a main qui ne tient plus ou mal
    risk_level: securite
    evidence:
      - 'Observation: frein a main qui ne tient'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit de frottement metallique a l
    description: bruit de frottement metallique a l arriere
    risk_level: confort
    evidence:
      - 'Observation: bruit de frottement metallique a l'
      - Vérification visuelle ou auditive
  - id: S3
    label: Tambour raye ou strie a l
    description: tambour raye ou strie a l interieur
    risk_level: confort
    evidence:
      - 'Observation: tambour raye ou strie a l'
      - Vérification visuelle ou auditive
  - id: S4
    label: Epaisseur de garniture inferieure a 2mm
    description: epaisseur de garniture inferieure a 2mm
    risk_level: confort
    evidence:
      - 'Observation: epaisseur de garniture inferieure a 2mm'
      - Vérification visuelle ou auditive
  - id: S5
    label: Freinage arriere desequilibre tire d un
    description: freinage arriere desequilibre tire d un cote
    risk_level: securite
    evidence:
      - 'Observation: freinage arriere desequilibre tire d un'
      - Vérification visuelle ou auditive
  - id: S6
    label: Poussiere frein noire excessive jantes
    description: poussiere frein noire excessive jantes
    risk_level: securite
    evidence:
      - 'Observation: poussiere frein noire excessive jantes'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Mâchoires de frein - Guide Complet

## Fonction

Creer la friction a l'interieur du tambour

## Symptômes de défaillance

### Frein a main qui ne tient

frein a main qui ne tient plus ou mal

### Bruit de frottement metallique a l

bruit de frottement metallique a l arriere

### Tambour raye ou strie a l

tambour raye ou strie a l interieur

### Epaisseur de garniture inferieure a 2mm

epaisseur de garniture inferieure a 2mm

### Freinage arriere desequilibre tire d un

freinage arriere desequilibre tire d un cote

### Poussiere frein noire excessive jantes

poussiere frein noire excessive jantes

## Diagnostic

Pour diagnostiquer un problème de mâchoires de frein:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- cable-de-frein-a-main
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- flexible-de-frein

## Compatibilité

Pour commander le bon mâchoires de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
