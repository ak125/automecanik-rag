---
entity_type: gamme
title: Témoin d'usure
slug: temoin-d-usure
pg_id: 407
category: freinage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Signale l'usure des plaquettes de frein
  must_be_true:
    - signaler
    - alerter
    - indiquer
  must_not_contain_concepts:
    - injection
    - climatisation
    - embrayage
    - distribution
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_voyant-usure-frein-allume-au-tableau
    then: verifier_piece
  - if: symptome_sifflement-metallique-freinage-temoin-acoustique
    then: diagnostic_approfondi
  - if: symptome_voyant-allume-en-permanence-meme-plaquettes
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Voyant usure frein allume au tableau
    description: voyant usure frein allume au tableau de bord
    risk_level: securite
    evidence:
      - 'Observation: voyant usure frein allume au tableau'
      - Vérification visuelle ou auditive
  - id: S2
    label: Sifflement metallique freinage temoin acoustique
    description: sifflement metallique freinage temoin acoustique
    risk_level: securite
    evidence:
      - 'Observation: sifflement metallique freinage temoin acoustique'
      - Vérification visuelle ou auditive
  - id: S3
    label: Voyant allume en permanence meme plaquettes
    description: voyant allume en permanence meme plaquettes neuves
    risk_level: confort
    evidence:
      - 'Observation: voyant allume en permanence meme plaquettes'
      - Vérification visuelle ou auditive
  - id: S4
    label: Connecteur du temoin debranche ou coupe
    description: connecteur du temoin debranche ou coupe
    risk_level: confort
    evidence:
      - 'Observation: connecteur du temoin debranche ou coupe'
      - Vérification visuelle ou auditive
  - id: S5
    label: Fil du temoin fondu par frottement
    description: fil du temoin fondu par frottement sur disque
    risk_level: confort
    evidence:
      - 'Observation: fil du temoin fondu par frottement'
      - Vérification visuelle ou auditive
  - id: S6
    label: Freinage degrade malgre absence de voyant
    description: freinage degrade malgre absence de voyant
    risk_level: securite
    evidence:
      - 'Observation: freinage degrade malgre absence de voyant'
      - Vérification visuelle ou auditive
  - id: S7
    label: Odeur de brule si frottement du
    description: odeur de brule si frottement du fil
    risk_level: confort
    evidence:
      - 'Observation: odeur de brule si frottement du'
      - Vérification visuelle ou auditive
  - id: S8
    label: Plus de 30 000 km avec
    description: plus de 30 000 km avec temoin non verifie
    risk_level: confort
    evidence:
      - 'Observation: plus de 30 000 km avec'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Témoin d'usure - Guide Complet

## Fonction

Signale l'usure des plaquettes de frein

## Symptômes de défaillance

### Voyant usure frein allume au tableau

voyant usure frein allume au tableau de bord

### Sifflement metallique freinage temoin acoustique

sifflement metallique freinage temoin acoustique

### Voyant allume en permanence meme plaquettes

voyant allume en permanence meme plaquettes neuves

### Connecteur du temoin debranche ou coupe

connecteur du temoin debranche ou coupe

### Fil du temoin fondu par frottement

fil du temoin fondu par frottement sur disque

### Freinage degrade malgre absence de voyant

freinage degrade malgre absence de voyant

### Odeur de brule si frottement du

odeur de brule si frottement du fil

### Plus de 30 000 km avec

plus de 30 000 km avec temoin non verifie

## Diagnostic

Pour diagnostiquer un problème de témoin d'usure:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- cable-de-frein-a-main
- capteur-abs
- disque-de-frein
- etrier-de-frein
- interrupteur-des-feux-de-freins

## Compatibilité

Pour commander le bon témoin d'usure, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
