---
entity_type: gamme
title: Flexible de frein
slug: flexible-de-frein
pg_id: 83
category: freinage
subcategory: flexibles
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmettre la pression hydraulique entre les elements mobiles
  must_be_true:
    - transmettre la pression
    - acheminer le liquide
    - resister a la pression
  must_not_contain_concepts:
    - friction
    - thermique
    - electronique
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
symptoms:
  - id: S1
    label: Craquelures ou fissures visibles sur le flexible
    description: craquelures ou fissures visibles sur le flexible
    risk_level: confort
    evidence:
      - 'Observation: craquelures ou fissures visibles sur le flexible'
      - Vérification visuelle ou auditive
  - id: S2
    label: Gonflement flexible lors appui pedale
    description: gonflement flexible lors appui pedale
    risk_level: confort
    evidence:
      - 'Observation: gonflement flexible lors appui pedale'
      - Vérification visuelle ou auditive
  - id: S3
    label: Fuite de liquide de frein au niveau du flexible
    description: fuite de liquide de frein au niveau du flexible
    risk_level: securite
    evidence:
      - 'Observation: fuite de liquide de frein au niveau du flexible'
      - Vérification visuelle ou auditive
  - id: S4
    label: Pedale de frein spongieuse ou molle
    description: pedale de frein spongieuse ou molle
    risk_level: securite
    evidence:
      - 'Observation: pedale de frein spongieuse ou molle'
      - Vérification visuelle ou auditive
  - id: S5
    label: Freinage qui tire d un cote flexible bouche
    description: freinage qui tire d un cote flexible bouche
    risk_level: securite
    evidence:
      - 'Observation: freinage qui tire d un cote flexible bouche'
      - Vérification visuelle ou auditive
  - id: S6
    label: Sifflement bruit niveau flexible sous
    description: sifflement bruit niveau flexible sous
    risk_level: confort
    evidence:
      - 'Observation: sifflement bruit niveau flexible sous'
      - Vérification visuelle ou auditive
  - id: S7
    label: Odeur de liquide de frein fuite
    description: odeur de liquide de frein fuite
    risk_level: securite
    evidence:
      - 'Observation: odeur de liquide de frein fuite'
      - Vérification visuelle ou auditive
  - id: S8
    label: Plus depuis dernier changement flexibles
    description: plus depuis dernier changement flexibles
    risk_level: confort
    evidence:
      - 'Observation: plus depuis dernier changement flexibles'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Flexible de frein - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre la pression hydraulique entre les elements mobiles

**Actions principales:** transmettre la pression, acheminer le liquide, resister a la pression, conduire le fluide, relier

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Fuite de liquide de frein au niveau du flexible**
  fuite de liquide de frein au niveau du flexible
- **Pedale de frein spongieuse ou molle**
  pedale de frein spongieuse ou molle
- **Freinage qui tire d un cote flexible bouche**
  freinage qui tire d un cote flexible bouche
- **Odeur de liquide de frein fuite**
  odeur de liquide de frein fuite

### 🟢 Autres Symptômes

- craquelures ou fissures visibles sur le flexible
- gonflement flexible lors appui pedale
- sifflement bruit niveau flexible sous
- plus depuis dernier changement flexibles

## Procédure de Diagnostic

Pour diagnostiquer un problème de flexible de frein:

1. **Inspection visuelle** - Examiner l'état du flexible de frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-abs
- cylindre-de-roue
- disque-de-frein
- etrier-de-frein
- interrupteur-des-feux-de-freins
- kit-de-freins-arriere
- machoires-de-frein
- maitre-cylindre-de-frein

## Critères de Compatibilité

Pour commander le bon flexible de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "freinage ameliore"
