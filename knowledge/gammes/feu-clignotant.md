---
entity_type: gamme
title: Feu clignotant
slug: feu-clignotant
pg_id: 62
category: eclairage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Signale les changements de direction
  must_be_true:
    - signaler
    - indiquer
    - clignoter
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
  - if: symptome_general_detecte
    then: inspection_visuelle_et_test_fonctionnel
symptoms:
  - id: S1
    label: Clignotant lateral qui ne s allume plus
    description: clignotant lateral qui ne s allume plus
    risk_level: confort
    evidence:
      - 'Observation: clignotant lateral qui ne s allume plus'
      - Vérification visuelle ou auditive
  - id: S2
    label: Clignotement rapide tableau bord ampoule
    description: clignotement rapide tableau bord ampoule
    risk_level: confort
    evidence:
      - 'Observation: clignotement rapide tableau bord ampoule'
      - Vérification visuelle ou auditive
  - id: S3
    label: Repetiteur casse ou fissure choc
    description: repetiteur casse ou fissure choc
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: repetiteur casse ou fissure choc'
      - Vérification visuelle ou auditive
  - id: S4
    label: Eau ou buee visible dans le repetiteur
    description: eau ou buee visible dans le repetiteur
    risk_level: confort
    evidence:
      - 'Observation: eau ou buee visible dans le repetiteur'
      - Vérification visuelle ou auditive
  - id: S5
    label: Controle technique refuse signalisation defaillante
    description: controle technique refuse signalisation defaillante
    risk_level: confort
    evidence:
      - 'Observation: controle technique refuse signalisation defaillante'
      - Vérification visuelle ou auditive
  - id: S6
    label: Ampoule qui grille frequemment infiltration
    description: ampoule qui grille frequemment infiltration
    risk_level: confort
    evidence:
      - 'Observation: ampoule qui grille frequemment infiltration'
      - Vérification visuelle ou auditive
  - id: S7
    label: Clignotement plus rapide normale hyper
    description: clignotement plus rapide normale hyper
    risk_level: confort
    evidence:
      - 'Observation: clignotement plus rapide normale hyper'
      - Vérification visuelle ou auditive
  - id: S8
    label: Clignotant fonctionne intermittence maniere aleatoire
    description: clignotant fonctionne intermittence maniere aleatoire
    risk_level: confort
    evidence:
      - 'Observation: clignotant fonctionne intermittence maniere aleatoire'
      - Vérification visuelle ou auditive
  - id: S9
    label: Odeur plastique fondu court circuit
    description: odeur plastique fondu court circuit
    risk_level: confort
    evidence:
      - 'Observation: odeur plastique fondu court circuit'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Feu clignotant - Guide Diagnostic Complet

## Fonction et Rôle

Signale les changements de direction

**Actions principales:** signaler, indiquer, clignoter

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Repetiteur casse ou fissure choc**
  repetiteur casse ou fissure choc

### 🟢 Autres Symptômes

- clignotant lateral qui ne s allume plus
- clignotement rapide tableau bord ampoule
- eau ou buee visible dans le repetiteur
- controle technique refuse signalisation defaillante
- ampoule qui grille frequemment infiltration
- clignotement plus rapide normale hyper

## Procédure de Diagnostic

Pour diagnostiquer un problème de feu clignotant:

1. **Inspection visuelle** - Examiner l'état du feu clignotant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-clignotant
- commande-d-eclairage
- feu-arriere
- feu-avant

## Critères de Compatibilité

Pour commander le bon feu clignotant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleure visibilité"
