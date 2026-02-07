---
entity_type: gamme
title: Turbo
slug: turbo
pg_id: 2234
category: turbo
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Comprime l'air d'admission grâce aux gaz d'échappement
  must_be_true:
    - comprimer
    - suralimenter
    - pressuriser
  must_not_contain_concepts:
    - climatisation
    - freinage
    - distribution
    - embrayage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Fumee bleue ou noire excessive a l echappement
    description: fumee bleue ou noire excessive a l echappement
    risk_level: confort
    evidence:
      - 'Observation: fumee bleue ou noire excessive a l echappement'
      - Vérification visuelle ou auditive
  - id: S2
    label: Sifflement ou bruit metallique du turbo
    description: sifflement ou bruit metallique du turbo
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: sifflement ou bruit metallique du turbo'
      - Vérification visuelle ou auditive
  - id: S3
    label: Perte de puissance importante a l acceleration
    description: perte de puissance importante a l acceleration
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance importante a l acceleration'
      - Vérification visuelle ou auditive
  - id: S4
    label: Consommation d huile anormale 1l 1000km
    description: consommation d huile anormale 1l 1000km
    risk_level: confort
    evidence:
      - 'Observation: consommation d huile anormale 1l 1000km'
      - Vérification visuelle ou auditive
  - id: S5
    label: Voyant moteur allume codes p0234 p0299
    description: voyant moteur allume codes p0234 p0299
    risk_level: confort
    evidence:
      - 'Observation: voyant moteur allume codes p0234 p0299'
      - Vérification visuelle ou auditive
  - id: S6
    label: Jeu perceptible dans l axe du turbo
    description: jeu perceptible dans l axe du turbo
    risk_level: confort
    evidence:
      - 'Observation: jeu perceptible dans l axe du turbo'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Turbo - Guide Diagnostic Complet

## Fonction et Rôle

Comprime l'air d'admission grâce aux gaz d'échappement

**Actions principales:** comprimer, suralimenter, pressuriser

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Sifflement ou bruit metallique du turbo**
  sifflement ou bruit metallique du turbo

### 🟢 Autres Symptômes

- fumee bleue ou noire excessive a l echappement
- perte de puissance importante a l acceleration
- consommation d huile anormale 1l 1000km
- voyant moteur allume codes p0234 p0299
- jeu perceptible dans l axe du turbo

## Procédure de Diagnostic

Pour diagnostiquer un problème de turbo:

1. **Inspection visuelle** - Examiner l'état du turbo
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-de-pression-turbo
- filtre-a-air
- filtre-a-huile
- gaine-de-turbo
- intercooler
- valve-de-turbo
- vanne-egr

## Critères de Compatibilité

Pour commander le bon turbo, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"
