---
entity_type: gamme
title: Volant moteur
slug: volant-moteur
pg_id: 577
category: embrayage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Lisser les vibrations du moteur, supporter le disque d'embrayage et
    transmettre l'inertie
  must_be_true:
    - lisser
    - supporter
    - transmettre l'inertie
  must_not_contain_concepts:
    - butée
    - pédale
    - commande
    - differentiel
    - cardan
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_bruit-de-claquement-ou-cognement-au
    then: verifier_piece
  - if: symptome_vibrations-anormales-transmises-a-l-habitacle
    then: diagnostic_approfondi
  - if: symptome_craquement-au-demarrage-ou-a-l
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Bruit de claquement ou cognement au
    description: bruit de claquement ou cognement au ralenti
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit de claquement ou cognement au'
      - Vérification visuelle ou auditive
  - id: S2
    label: Vibrations anormales transmises a l habitacle
    description: vibrations anormales transmises a l habitacle
    risk_level: confort
    evidence:
      - 'Observation: vibrations anormales transmises a l habitacle'
      - Vérification visuelle ou auditive
  - id: S3
    label: Craquement au demarrage ou a l
    description: craquement au demarrage ou a l arret du moteur
    risk_level: confort
    evidence:
      - 'Observation: craquement au demarrage ou a l'
      - Vérification visuelle ou auditive
  - id: S4
    label: Angulaire perceptible main volant depose
    description: angulaire perceptible main volant depose
    risk_level: confort
    evidence:
      - 'Observation: angulaire perceptible main volant depose'
      - Vérification visuelle ou auditive
  - id: S5
    label: Embrayage qui vibre ou accroche au
    description: embrayage qui vibre ou accroche au demarrage
    risk_level: confort
    evidence:
      - 'Observation: embrayage qui vibre ou accroche au'
      - Vérification visuelle ou auditive
  - id: S6
    label: Changement d embrayage prevu verifier le
    description: changement d embrayage prevu verifier le volant
    risk_level: confort
    evidence:
      - 'Observation: changement d embrayage prevu verifier le'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Volant moteur - Guide Complet

## Fonction

Lisser les vibrations du moteur, supporter le disque d'embrayage et transmettre l'inertie

## Symptômes de défaillance

### Bruit de claquement ou cognement au

bruit de claquement ou cognement au ralenti

### Vibrations anormales transmises a l habitacle

vibrations anormales transmises a l habitacle

### Craquement au demarrage ou a l

craquement au demarrage ou a l arret du moteur

### Angulaire perceptible main volant depose

angulaire perceptible main volant depose

### Embrayage qui vibre ou accroche au

embrayage qui vibre ou accroche au demarrage

### Changement d embrayage prevu verifier le

changement d embrayage prevu verifier le volant

## Diagnostic

Pour diagnostiquer un problème de volant moteur:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- butee-d-embrayage
- cable-d-embrayage
- capteur-impulsion
- demarreur
- emetteur-d-embrayage

## Compatibilité

Pour commander le bon volant moteur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
