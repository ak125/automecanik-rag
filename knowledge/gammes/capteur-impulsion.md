---
entity_type: gamme
title: Capteur impulsion
slug: capteur-impulsion
pg_id: 4813
category: capteurs
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Detecter les impulsions du vilebrequin ou de l'arbre a cames
  must_be_true:
    - detecter
    - compter
    - transmettre
  must_not_contain_concepts:
    - reparation
    - regeneration
    - nettoyage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: vehicule_immobilise_ou_symptome_critique
    then: verification_urgente_piece_et_alimentation
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
symptoms:
  - id: S1
    label: Moteur qui ne demarre pas du tout
    description: moteur qui ne demarre pas du tout
    risk_level: immobilisation
    evidence:
      - 'Observation: moteur qui ne demarre pas du tout'
      - Vérification visuelle ou auditive
  - id: S2
    label: Calages repetes au ralenti ou en roulant
    description: calages repetes au ralenti ou en roulant
    risk_level: immobilisation
    evidence:
      - 'Observation: calages repetes au ralenti ou en roulant'
      - Vérification visuelle ou auditive
  - id: S3
    label: Claquement ou rate d allumage
    description: claquement ou rate d allumage
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement ou rate d allumage'
      - Vérification visuelle ou auditive
  - id: S4
    label: Voyant moteur avec codes p0335 p0336
    description: voyant moteur avec codes p0335 p0336
    risk_level: confort
    evidence:
      - 'Observation: voyant moteur avec codes p0335 p0336'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur d essence injection non synchronisee
    description: odeur d essence injection non synchronisee
    risk_level: confort
    evidence:
      - 'Observation: odeur d essence injection non synchronisee'
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
    - compatible tout véhicule
    - adaptable
---
# Capteur impulsion - Guide Diagnostic Complet

## Fonction et Rôle

Detecter les impulsions du vilebrequin ou de l'arbre a cames

**Actions principales:** detecter, compter, transmettre

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Moteur qui ne demarre pas du tout**
  moteur qui ne demarre pas du tout
- **Calages repetes au ralenti ou en roulant**
  calages repetes au ralenti ou en roulant

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement ou rate d allumage**
  claquement ou rate d allumage

### 🟢 Autres Symptômes

- voyant moteur avec codes p0335 p0336
- odeur d essence injection non synchronisee
- plus demarrages difficiles recurrents

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur impulsion:

1. **Inspection visuelle** - Examiner l'état du capteur impulsion
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Pièce HS** - Le capteur impulsion peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-de-cognement
- capteur-impulsion
- poulie-d-arbre-a-came
- poulie-vilebrequin
- volant-moteur

## Critères de Compatibilité

Pour commander le bon capteur impulsion, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "mesure parfaite"
