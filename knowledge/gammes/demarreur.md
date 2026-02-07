---
entity_type: gamme
title: Démarreur
slug: demarreur
pg_id: 2
category: electrique
subcategory: demarrage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Appliquer une rotation initiale au moteur pour declencher le demarrage
  must_be_true:
    - lancer le moteur
    - entrainer
    - demarrer
  must_not_contain_concepts:
    - charge
    - recharge
    - alimentation electrique
    - alternateur
    - universel
    - tous modèles
    - adaptable tous
  confusion_with:
    alternateur:
      key_difference: >-
        Démarreur = lance le moteur (au démarrage), Alternateur = recharge
        batterie (moteur tournant)
    batterie:
      key_difference: >-
        Batterie faible peut simuler un démarreur HS - toujours tester la
        batterie d'abord
diagnostic_tree:
  - if: vehicule_immobilise_ou_symptome_critique
    then: verification_urgente_piece_et_alimentation
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
symptoms:
  - id: S1
    label: Claquement contact demarrage solenoide
    description: claquement contact demarrage solenoide
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement contact demarrage solenoide'
      - Vérification visuelle ou auditive
  - id: S2
    label: Demarreur tourne mais moteur lance
    description: demarreur tourne mais moteur lance
    risk_level: confort
    evidence:
      - 'Observation: demarreur tourne mais moteur lance'
      - Vérification visuelle ou auditive
  - id: S3
    label: Aucune reaction au contact moteur electrique hs
    description: aucune reaction au contact moteur electrique hs
    risk_level: immobilisation
    evidence:
      - 'Observation: aucune reaction au contact moteur electrique hs'
      - Vérification visuelle ou auditive
  - id: S4
    label: Grincement ou bruit anormal au demarrage
    description: grincement ou bruit anormal au demarrage
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: grincement ou bruit anormal au demarrage'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de brule electrique au demarrage
    description: odeur de brule electrique au demarrage
    risk_level: confort
    evidence:
      - 'Observation: odeur de brule electrique au demarrage'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus demarrages difficiles recurrents
    description: plus demarrages difficiles recurrents
    risk_level: confort
    evidence:
      - 'Observation: plus demarrages difficiles recurrents'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - adaptable tous
---
# Démarreur - Guide Diagnostic Complet

## Fonction et Rôle

Appliquer une rotation initiale au moteur pour declencher le demarrage

**Actions principales:** lancer le moteur, entrainer, demarrer, mettre en rotation, entrainer le vilebrequin

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Aucune reaction au contact moteur electrique hs**
  aucune reaction au contact moteur electrique hs

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement contact demarrage solenoide**
  claquement contact demarrage solenoide
- **Grincement ou bruit anormal au demarrage**
  grincement ou bruit anormal au demarrage

### 🟢 Autres Symptômes

- demarreur tourne mais moteur lance
- odeur de brule electrique au demarrage
- plus demarrages difficiles recurrents

## Procédure de Diagnostic

Pour diagnostiquer un problème de démarreur:

1. **Inspection visuelle** - Examiner l'état du démarreur
2. **Test électrique** - Vérifier la tension et les connexions
3. **Lecture codes défaut** - Scanner OBD si voyant allumé
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le démarreur peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- neiman
- contacteur-demarreur

## ⚠️ Ne Pas Confondre Avec

### alternateur
**Distinction:** Démarreur = lance le moteur (au démarrage), Alternateur = recharge batterie (moteur tournant)

### batterie
**Distinction:** Batterie faible peut simuler un démarreur HS - toujours tester la batterie d'abord

## Critères de Compatibilité

Pour commander le bon démarreur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Motorisation** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "démarrage garanti"
- ❌ "homologué CT"
- ❌ "sécurité garantie"
