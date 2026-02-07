---
entity_type: gamme
title: Contacteur feu de recul
slug: contacteur-de-feu-de-recul
pg_id: 807
category: eclairage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Active les feux de recul en marche arrière
  must_be_true:
    - activer
    - signaler
    - commander
  must_not_contain_concepts:
    - injection
    - freinage
    - embrayage
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
    label: Feux recul allument plus marche
    description: feux recul allument plus marche
    risk_level: confort
    evidence:
      - 'Observation: feux recul allument plus marche'
      - Vérification visuelle ou auditive
  - id: S2
    label: Feux de recul toujours allumes moteur demarre
    description: feux de recul toujours allumes moteur demarre
    risk_level: confort
    evidence:
      - 'Observation: feux de recul toujours allumes moteur demarre'
      - Vérification visuelle ou auditive
  - id: S3
    label: Fuite huile visible niveau contacteur
    description: fuite huile visible niveau contacteur
    risk_level: confort
    evidence:
      - 'Observation: fuite huile visible niveau contacteur'
      - Vérification visuelle ou auditive
  - id: S4
    label: Camera de recul inactive car contacteur defaillant
    description: camera de recul inactive car contacteur defaillant
    risk_level: confort
    evidence:
      - 'Observation: camera de recul inactive car contacteur defaillant'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur huile boite vitesses autour
    description: odeur huile boite vitesses autour
    risk_level: confort
    evidence:
      - 'Observation: odeur huile boite vitesses autour'
      - Vérification visuelle ou auditive
  - id: S6
    label: Claquement bruit passage marche arriere
    description: claquement bruit passage marche arriere
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement bruit passage marche arriere'
      - Vérification visuelle ou auditive
  - id: S7
    label: Difficulte enclencher marche arriere contacteur
    description: difficulte enclencher marche arriere contacteur
    risk_level: confort
    evidence:
      - 'Observation: difficulte enclencher marche arriere contacteur'
      - Vérification visuelle ou auditive
  - id: S8
    label: Contacteur place depuis plus controle
    description: contacteur place depuis plus controle
    risk_level: confort
    evidence:
      - 'Observation: contacteur place depuis plus controle'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Contacteur feu de recul - Guide Diagnostic Complet

## Fonction et Rôle

Active les feux de recul en marche arrière

**Actions principales:** activer, signaler, commander

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement bruit passage marche arriere**
  claquement bruit passage marche arriere

### 🟢 Autres Symptômes

- feux recul allument plus marche
- feux de recul toujours allumes moteur demarre
- fuite huile visible niveau contacteur
- camera de recul inactive car contacteur defaillant
- odeur huile boite vitesses autour
- difficulte enclencher marche arriere contacteur

## Procédure de Diagnostic

Pour diagnostiquer un problème de contacteur feu de recul:

1. **Inspection visuelle** - Examiner l'état du contacteur feu de recul
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-arriere
- commande-d-eclairage
- feu-arriere
- feu-avant
- feu-clignotant

## Critères de Compatibilité

Pour commander le bon contacteur feu de recul, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "sécurité maximale"
