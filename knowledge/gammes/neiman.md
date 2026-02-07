---
entity_type: gamme
title: Neiman
slug: neiman
pg_id: 1367
category: electrique
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Verrouiller la direction et alimenter les circuits electriques
  must_be_true:
    - verrouiller
    - alimenter
    - securiser
  must_not_contain_concepts:
    - injection
    - climatisation
    - freinage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: vehicule_immobilise_ou_symptome_critique
    then: verification_urgente_piece_et_alimentation
symptoms:
  - id: S1
    label: Tableau de bord qui ne s allume pas au contact
    description: tableau de bord qui ne s allume pas au contact
    risk_level: confort
    evidence:
      - 'Observation: tableau de bord qui ne s allume pas au contact'
      - Vérification visuelle ou auditive
  - id: S2
    label: Cle qui tourne dans le vide sans effet
    description: cle qui tourne dans le vide sans effet
    risk_level: confort
    evidence:
      - 'Observation: cle qui tourne dans le vide sans effet'
      - Vérification visuelle ou auditive
  - id: S3
    label: Direction bloquee impossible a debloquer
    description: direction bloquee impossible a debloquer
    risk_level: immobilisation
    evidence:
      - 'Observation: direction bloquee impossible a debloquer'
      - Vérification visuelle ou auditive
  - id: S4
    label: Contact electrique intermittent coupures
    description: contact electrique intermittent coupures
    risk_level: confort
    evidence:
      - 'Observation: contact electrique intermittent coupures'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de plastique brule court-circuit interne
    description: odeur de plastique brule court-circuit interne
    risk_level: confort
    evidence:
      - 'Observation: odeur de plastique brule court-circuit interne'
      - Vérification visuelle ou auditive
  - id: S6
    label: Difficulte recurrente a tourner la cle
    description: difficulte recurrente a tourner la cle
    risk_level: confort
    evidence:
      - 'Observation: difficulte recurrente a tourner la cle'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Neiman - Guide Diagnostic Complet

## Fonction et Rôle

Verrouiller la direction et alimenter les circuits electriques

**Actions principales:** verrouiller, alimenter, securiser

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Direction bloquee impossible a debloquer**
  direction bloquee impossible a debloquer

### 🟢 Autres Symptômes

- tableau de bord qui ne s allume pas au contact
- cle qui tourne dans le vide sans effet
- contact electrique intermittent coupures
- odeur de plastique brule court-circuit interne
- difficulte recurrente a tourner la cle

## Procédure de Diagnostic

Pour diagnostiquer un problème de neiman:

1. **Inspection visuelle** - Examiner l'état du neiman
2. **Test électrique** - Vérifier la tension et les connexions
3. **Lecture codes défaut** - Scanner OBD si voyant allumé

## Causes Probables

- **Pièce HS** - Le neiman peut être hors service et nécessiter un remplacement
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- colonne-de-direction
- demarreur

## Critères de Compatibilité

Pour commander le bon neiman, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "demarrage garanti"
