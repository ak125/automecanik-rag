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
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
symptoms:
  - id: S1
    label: Frein a main qui ne tient plus ou mal
    description: frein a main qui ne tient plus ou mal
    risk_level: securite
    evidence:
      - 'Observation: frein a main qui ne tient plus ou mal'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit de frottement metallique a l arriere
    description: bruit de frottement metallique a l arriere
    risk_level: confort
    evidence:
      - 'Observation: bruit de frottement metallique a l arriere'
      - Vérification visuelle ou auditive
  - id: S3
    label: Tambour raye ou strie a l interieur
    description: tambour raye ou strie a l interieur
    risk_level: confort
    evidence:
      - 'Observation: tambour raye ou strie a l interieur'
      - Vérification visuelle ou auditive
  - id: S4
    label: Epaisseur de garniture inferieure a 2mm
    description: epaisseur de garniture inferieure a 2mm
    risk_level: confort
    evidence:
      - 'Observation: epaisseur de garniture inferieure a 2mm'
      - Vérification visuelle ou auditive
  - id: S5
    label: Freinage arriere desequilibre tire d un cote
    description: freinage arriere desequilibre tire d un cote
    risk_level: securite
    evidence:
      - 'Observation: freinage arriere desequilibre tire d un cote'
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
# Mâchoires de frein - Guide Diagnostic Complet

## Fonction et Rôle

Creer la friction a l'interieur du tambour

**Actions principales:** frotter, exercer une pression interne, s'user progressivement, s'ecarter, plaquer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Frein a main qui ne tient plus ou mal**
  frein a main qui ne tient plus ou mal
- **Freinage arriere desequilibre tire d un cote**
  freinage arriere desequilibre tire d un cote
- **Poussiere frein noire excessive jantes**
  poussiere frein noire excessive jantes

### 🟢 Autres Symptômes

- bruit de frottement metallique a l arriere
- tambour raye ou strie a l interieur
- epaisseur de garniture inferieure a 2mm

## Procédure de Diagnostic

Pour diagnostiquer un problème de mâchoires de frein:

1. **Inspection visuelle** - Examiner l'état du mâchoires de frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- cable-de-frein-a-main
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- flexible-de-frein
- interrupteur-des-feux-de-freins
- kit-de-freins-arriere
- maitre-cylindre-de-frein

## Critères de Compatibilité

Pour commander le bon mâchoires de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "remplacement plaquettes"
