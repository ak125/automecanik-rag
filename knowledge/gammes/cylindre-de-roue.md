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
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Traces de liquide sur le dos des machoires
    description: traces de liquide sur le dos des machoires
    risk_level: confort
    evidence:
      - 'Observation: traces de liquide sur le dos des machoires'
      - Vérification visuelle ou auditive
  - id: S2
    label: Interieur du tambour mouille ou gras
    description: interieur du tambour mouille ou gras
    risk_level: confort
    evidence:
      - 'Observation: interieur du tambour mouille ou gras'
      - Vérification visuelle ou auditive
  - id: S3
    label: Niveau de liquide de frein qui baisse
    description: niveau de liquide de frein qui baisse
    risk_level: securite
    evidence:
      - 'Observation: niveau de liquide de frein qui baisse'
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
    label: Odeur de liquide de frein pres des roues arriere
    description: odeur de liquide de frein pres des roues arriere
    risk_level: securite
    evidence:
      - 'Observation: odeur de liquide de frein pres des roues arriere'
      - Vérification visuelle ou auditive
  - id: S9
    label: Plus de 100 000 km sans controle des cylindres
    description: plus de 100 000 km sans controle des cylindres
    risk_level: confort
    evidence:
      - 'Observation: plus de 100 000 km sans controle des cylindres'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Cylindre de roue - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre la pression hydraulique aux machoires

**Actions principales:** pousser les machoires, transmettre la pression, actionner le freinage tambour, ecarter, commander

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Niveau de liquide de frein qui baisse**
  niveau de liquide de frein qui baisse
- **Freinage arriere desequilibre**
  freinage arriere desequilibre
- **Odeur de liquide de frein pres des roues arriere**
  odeur de liquide de frein pres des roues arriere

### 🟢 Autres Symptômes

- traces de liquide sur le dos des machoires
- interieur du tambour mouille ou gras
- machoires usees de facon asymetrique
- fuite visible au niveau du cylindre
- bruit de frottement a l arriere
- plus de 100 000 km sans controle des cylindres

## Procédure de Diagnostic

Pour diagnostiquer un problème de cylindre de roue:

1. **Inspection visuelle** - Examiner l'état du cylindre de roue
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- cable-de-frein-a-main
- disque-de-frein
- etrier-de-frein
- flexible-de-frein
- kit-de-freins-arriere
- machoires-de-frein
- plaquette-de-frein
- tambour-de-frein

## Critères de Compatibilité

Pour commander le bon cylindre de roue, vous devez connaître:

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
