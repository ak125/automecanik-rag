---
entity_type: gamme
title: Emetteur d'embrayage
slug: emetteur-d-embrayage
pg_id: 234
category: embrayage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmettre la pression hydraulique de la pédale vers le récepteur
  must_be_true:
    - transmettre la pression
    - pousser le liquide
    - convertir l'effort
  must_not_contain_concepts:
    - disque
    - volant
    - couple
    - câble
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
symptoms:
  - id: S1
    label: Pedale d embrayage molle ou spongieuse
    description: pedale d embrayage molle ou spongieuse
    risk_level: confort
    evidence:
      - 'Observation: pedale d embrayage molle ou spongieuse'
      - Vérification visuelle ou auditive
  - id: S2
    label: Pedale qui s enfonce jusqu au plancher
    description: pedale qui s enfonce jusqu au plancher
    risk_level: confort
    evidence:
      - 'Observation: pedale qui s enfonce jusqu au plancher'
      - Vérification visuelle ou auditive
  - id: S3
    label: Niveau liquide frein baisse fuite
    description: niveau liquide frein baisse fuite
    risk_level: securite
    evidence:
      - 'Observation: niveau liquide frein baisse fuite'
      - Vérification visuelle ou auditive
  - id: S4
    label: Fuite liquide sous tableau bord
    description: fuite liquide sous tableau bord
    risk_level: confort
    evidence:
      - 'Observation: fuite liquide sous tableau bord'
      - Vérification visuelle ou auditive
  - id: S5
    label: Embrayage qui patine par intermittence
    description: embrayage qui patine par intermittence
    risk_level: confort
    evidence:
      - 'Observation: embrayage qui patine par intermittence'
      - Vérification visuelle ou auditive
  - id: S6
    label: Difficulte a debrayer completement
    description: difficulte a debrayer completement
    risk_level: confort
    evidence:
      - 'Observation: difficulte a debrayer completement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Emetteur d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre la pression hydraulique de la pédale vers le récepteur

**Actions principales:** transmettre la pression, pousser le liquide, convertir l'effort, envoyer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Niveau liquide frein baisse fuite**
  niveau liquide frein baisse fuite

### 🟢 Autres Symptômes

- pedale d embrayage molle ou spongieuse
- pedale qui s enfonce jusqu au plancher
- fuite liquide sous tableau bord
- embrayage qui patine par intermittence
- difficulte a debrayer completement

## Procédure de Diagnostic

Pour diagnostiquer un problème de emetteur d'embrayage:

1. **Inspection visuelle** - Examiner l'état du emetteur d'embrayage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- butee-d-embrayage
- kit-d-embrayage
- recepteur-d-embrayage

## Critères de Compatibilité

Pour commander le bon emetteur d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "pression parfaite"
