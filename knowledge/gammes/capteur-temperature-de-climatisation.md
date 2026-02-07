---
entity_type: gamme
title: Capteur température de climatisation
slug: capteur-temperature-de-climatisation
pg_id: 2054
category: climatisation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Mesurer la temperature de l'air dans l'habitacle
  must_be_true:
    - mesurer
    - detecter
    - transmettre
  must_not_contain_concepts:
    - injection
    - freinage
    - allumage
    - embrayage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
symptoms:
  - id: S1
    label: Compresseur qui refuse de s enclencher
    description: compresseur qui refuse de s enclencher
    risk_level: confort
    evidence:
      - 'Observation: compresseur qui refuse de s enclencher'
      - Vérification visuelle ou auditive
  - id: S2
    label: Climatisation qui givre l evaporateur
    description: climatisation qui givre l evaporateur
    risk_level: confort
    evidence:
      - 'Observation: climatisation qui givre l evaporateur'
      - Vérification visuelle ou auditive
  - id: S3
    label: Regulation automatique de temperature defaillante
    description: regulation automatique de temperature defaillante
    risk_level: confort
    evidence:
      - 'Observation: regulation automatique de temperature defaillante'
      - Vérification visuelle ou auditive
  - id: S4
    label: Voyant de climatisation qui clignote
    description: voyant de climatisation qui clignote
    risk_level: confort
    evidence:
      - 'Observation: voyant de climatisation qui clignote'
      - Vérification visuelle ou auditive
  - id: S5
    label: Code defaut capteur au diagnostic
    description: code defaut capteur au diagnostic
    risk_level: confort
    evidence:
      - 'Observation: code defaut capteur au diagnostic'
      - Vérification visuelle ou auditive
  - id: S6
    label: Temperature affichee incoherente
    description: temperature affichee incoherente
    risk_level: confort
    evidence:
      - 'Observation: temperature affichee incoherente'
      - Vérification visuelle ou auditive
  - id: S7
    label: Compresseur climatisation enclenche coupe boucle
    description: compresseur climatisation enclenche coupe boucle
    risk_level: confort
    evidence:
      - 'Observation: compresseur climatisation enclenche coupe boucle'
      - Vérification visuelle ou auditive
  - id: S8
    label: Temperature consigne jamais atteinte habitacle
    description: temperature consigne jamais atteinte habitacle
    risk_level: confort
    evidence:
      - 'Observation: temperature consigne jamais atteinte habitacle'
      - Vérification visuelle ou auditive
  - id: S9
    label: Givrage excessif evaporateur provoquant odeur
    description: givrage excessif evaporateur provoquant odeur
    risk_level: confort
    evidence:
      - 'Observation: givrage excessif evaporateur provoquant odeur'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Capteur température de climatisation - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la temperature de l'air dans l'habitacle

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- compresseur qui refuse de s enclencher
- climatisation qui givre l evaporateur
- regulation automatique de temperature defaillante
- voyant de climatisation qui clignote
- code defaut capteur au diagnostic
- temperature affichee incoherente

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur température de climatisation:

1. **Inspection visuelle** - Examiner l'état du capteur température de climatisation
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- evaporateur-de-climatisation
- compresseur-de-climatisation

## Critères de Compatibilité

Pour commander le bon capteur température de climatisation, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidit instantanement"
