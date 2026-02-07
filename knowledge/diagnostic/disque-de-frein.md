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
  - if: symptome_vibrations-dans-le-volant-au-freinage
    then: verifier_piece
  - if: symptome_sillon-circulaire-visible-sur-la-surface
    then: diagnostic_approfondi
  - if: symptome_bord-du-disque-en-relief-levre
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Vibrations dans le volant au freinage
    description: vibrations dans le volant au freinage
    risk_level: securite
    evidence:
      - 'Observation: vibrations dans le volant au freinage'
      - Vérification visuelle ou auditive
  - id: S2
    label: Sillon circulaire visible sur la surface
    description: sillon circulaire visible sur la surface du disque
    risk_level: confort
    evidence:
      - 'Observation: sillon circulaire visible sur la surface'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bord du disque en relief levre
    description: bord du disque en relief levre d usure
    risk_level: confort
    evidence:
      - 'Observation: bord du disque en relief levre'
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
    label: Epaisseur sous le minimum indique sur
    description: epaisseur sous le minimum indique sur le disque
    risk_level: confort
    evidence:
      - 'Observation: epaisseur sous le minimum indique sur'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Disque de frein - Guide Complet

## Fonction

Support de friction et dissipation thermique lors du freinage

## Symptômes de défaillance

### Vibrations dans le volant au freinage

vibrations dans le volant au freinage

### Sillon circulaire visible sur la surface

sillon circulaire visible sur la surface du disque

### Bord du disque en relief levre

bord du disque en relief levre d usure

### Crissement metallique au freinage

crissement metallique au freinage

### Odeur de brule apres freinages repetes

odeur de brule apres freinages repetes

### Epaisseur sous le minimum indique sur

epaisseur sous le minimum indique sur le disque

## Diagnostic

Pour diagnostiquer un problème de disque de frein:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- cable-de-frein-a-main
- capteur-abs
- etrier-de-frein
- interrupteur-des-feux-de-freins
- plaquette-de-frein

## Compatibilité

Pour commander le bon disque de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
