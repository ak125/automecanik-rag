---
entity_type: gamme
title: Disque de frein
slug: disque-de-frein
pg_id: 82
category: freinage
subcategory: disques
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Support de friction et dissipation thermique lors du freinage
  must_be_true:
    - dissiper la chaleur
    - recevoir la friction
    - ralentir la rotation
  must_not_contain_concepts:
    - tambour
    - machoire
    - hydraulique
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: vibrations_anormales
    then: verifier_equilibrage_et_fixations
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Vibrations dans le volant au freinage
    description: vibrations dans le volant au freinage
    risk_level: securite
    evidence:
      - 'Observation: vibrations dans le volant au freinage'
      - Vérification visuelle ou auditive
  - id: S2
    label: Sillon circulaire visible sur la surface du disque
    description: sillon circulaire visible sur la surface du disque
    risk_level: confort
    evidence:
      - 'Observation: sillon circulaire visible sur la surface du disque'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bord du disque en relief levre d usure
    description: bord du disque en relief levre d usure
    risk_level: confort
    evidence:
      - 'Observation: bord du disque en relief levre d usure'
      - Vérification visuelle ou auditive
  - id: S4
    label: Crissement metallique au freinage
    description: crissement metallique au freinage
    risk_level: securite
    evidence:
      - 'Observation: crissement metallique au freinage'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de brule apres freinages repetes
    description: odeur de brule apres freinages repetes
    risk_level: securite
    evidence:
      - 'Observation: odeur de brule apres freinages repetes'
      - Vérification visuelle ou auditive
  - id: S6
    label: Epaisseur sous le minimum indique sur le disque
    description: epaisseur sous le minimum indique sur le disque
    risk_level: confort
    evidence:
      - 'Observation: epaisseur sous le minimum indique sur le disque'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Disque de frein - Guide Diagnostic Complet

## Fonction et Rôle

Support de friction et dissipation thermique lors du freinage

**Actions principales:** dissiper la chaleur, recevoir la friction, ralentir la rotation, resister a l'echauffement, evacuer la chaleur

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Vibrations dans le volant au freinage**
  vibrations dans le volant au freinage
- **Crissement metallique au freinage**
  crissement metallique au freinage
- **Odeur de brule apres freinages repetes**
  odeur de brule apres freinages repetes

### 🟢 Autres Symptômes

- sillon circulaire visible sur la surface du disque
- bord du disque en relief levre d usure
- epaisseur sous le minimum indique sur le disque

## Procédure de Diagnostic

Pour diagnostiquer un problème de disque de frein:

1. **Inspection visuelle** - Examiner l'état du disque de frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- cable-de-frein-a-main
- capteur-abs
- etrier-de-frein
- interrupteur-des-feux-de-freins
- plaquette-de-frein
- roulement-de-roue
- servo-frein

## Critères de Compatibilité

Pour commander le bon disque de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "freinage garanti"
