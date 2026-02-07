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
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: vibrations_anormales
    then: verifier_equilibrage_et_fixations
symptoms:
  - id: S1
    label: Bruit de claquement ou cognement au ralenti
    description: bruit de claquement ou cognement au ralenti
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit de claquement ou cognement au ralenti'
      - Vérification visuelle ou auditive
  - id: S2
    label: Vibrations anormales transmises a l habitacle
    description: vibrations anormales transmises a l habitacle
    risk_level: confort
    evidence:
      - 'Observation: vibrations anormales transmises a l habitacle'
      - Vérification visuelle ou auditive
  - id: S3
    label: Craquement au demarrage ou a l arret du moteur
    description: craquement au demarrage ou a l arret du moteur
    risk_level: confort
    evidence:
      - 'Observation: craquement au demarrage ou a l arret du moteur'
      - Vérification visuelle ou auditive
  - id: S4
    label: Angulaire perceptible main volant depose
    description: angulaire perceptible main volant depose
    risk_level: confort
    evidence:
      - 'Observation: angulaire perceptible main volant depose'
      - Vérification visuelle ou auditive
  - id: S5
    label: Embrayage qui vibre ou accroche au demarrage
    description: embrayage qui vibre ou accroche au demarrage
    risk_level: confort
    evidence:
      - 'Observation: embrayage qui vibre ou accroche au demarrage'
      - Vérification visuelle ou auditive
  - id: S6
    label: Changement d embrayage prevu verifier le volant
    description: changement d embrayage prevu verifier le volant
    risk_level: confort
    evidence:
      - 'Observation: changement d embrayage prevu verifier le volant'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Volant moteur - Guide Diagnostic Complet

## Fonction et Rôle

Lisser les vibrations du moteur, supporter le disque d'embrayage et transmettre l'inertie

**Actions principales:** lisser, supporter, transmettre l'inertie, amortir les à-coups, stocker l'énergie

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de claquement ou cognement au ralenti**
  bruit de claquement ou cognement au ralenti

### 🟢 Autres Symptômes

- vibrations anormales transmises a l habitacle
- craquement au demarrage ou a l arret du moteur
- angulaire perceptible main volant depose
- embrayage qui vibre ou accroche au demarrage
- changement d embrayage prevu verifier le volant

## Procédure de Diagnostic

Pour diagnostiquer un problème de volant moteur:

1. **Inspection visuelle** - Examiner l'état du volant moteur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- butee-d-embrayage
- cable-d-embrayage
- capteur-impulsion
- demarreur
- emetteur-d-embrayage
- kit-d-embrayage
- recepteur-d-embrayage

## Critères de Compatibilité

Pour commander le bon volant moteur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "embraye mieux"
