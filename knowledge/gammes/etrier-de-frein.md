---
entity_type: gamme
title: Étrier de frein
slug: etrier-de-frein
pg_id: 78
category: freinage
subcategory: etriers
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Appliquer la pression hydraulique sur les plaquettes
  must_be_true:
    - appliquer la pression
    - maintenir les plaquettes
    - serrer
  must_not_contain_concepts:
    - tambour
    - machoire
    - thermique
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
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Usure asymetrique plaquettes plus usee
    description: usure asymetrique plaquettes plus usee
    risk_level: confort
    evidence:
      - 'Observation: usure asymetrique plaquettes plus usee'
      - Vérification visuelle ou auditive
  - id: S2
    label: Vehicule qui tire d un cote au freinage
    description: vehicule qui tire d un cote au freinage
    risk_level: securite
    evidence:
      - 'Observation: vehicule qui tire d un cote au freinage'
      - Vérification visuelle ou auditive
  - id: S3
    label: Roue anormalement chaude apres roulage
    description: roue anormalement chaude apres roulage
    risk_level: confort
    evidence:
      - 'Observation: roue anormalement chaude apres roulage'
      - Vérification visuelle ou auditive
  - id: S4
    label: Fuite de liquide de frein au niveau de l etrier
    description: fuite de liquide de frein au niveau de l etrier
    risk_level: securite
    evidence:
      - 'Observation: fuite de liquide de frein au niveau de l etrier'
      - Vérification visuelle ou auditive
  - id: S5
    label: Pedale de frein dure ou spongieuse
    description: pedale de frein dure ou spongieuse
    risk_level: securite
    evidence:
      - 'Observation: pedale de frein dure ou spongieuse'
      - Vérification visuelle ou auditive
  - id: S6
    label: Bruit de frottement permanent piston grippe
    description: bruit de frottement permanent piston grippe
    risk_level: confort
    evidence:
      - 'Observation: bruit de frottement permanent piston grippe'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Étrier de frein - Guide Diagnostic Complet

## Fonction et Rôle

Appliquer la pression hydraulique sur les plaquettes

**Actions principales:** appliquer la pression, maintenir les plaquettes, serrer, relacher, pincer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Vehicule qui tire d un cote au freinage**
  vehicule qui tire d un cote au freinage
- **Fuite de liquide de frein au niveau de l etrier**
  fuite de liquide de frein au niveau de l etrier
- **Pedale de frein dure ou spongieuse**
  pedale de frein dure ou spongieuse

### 🟢 Autres Symptômes

- usure asymetrique plaquettes plus usee
- roue anormalement chaude apres roulage
- bruit de frottement permanent piston grippe

## Procédure de Diagnostic

Pour diagnostiquer un problème de étrier de frein:

1. **Inspection visuelle** - Examiner l'état du étrier de frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- cable-de-frein-a-main
- capteur-abs
- disque-de-frein
- flexible-de-frein
- interrupteur-des-feux-de-freins
- maitre-cylindre-de-frein
- plaquette-de-frein
- servo-frein

## Critères de Compatibilité

Pour commander le bon étrier de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "freinage direct"
