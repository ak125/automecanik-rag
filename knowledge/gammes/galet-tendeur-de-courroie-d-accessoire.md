---
entity_type: gamme
title: Galet tendeur de courroie d'accessoire
slug: galet-tendeur-de-courroie-d-accessoire
pg_id: 310
category: distribution
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Maintient la tension de la courroie d'accessoire
  must_be_true:
    - tendre
    - maintenir
    - guider
  must_not_contain_concepts:
    - freinage
    - climatisation
    - turbo
    - injection
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
  - if: vibrations_anormales
    then: verifier_equilibrage_et_fixations
symptoms:
  - id: S1
    label: Sifflement de la courroie
    description: sifflement de la courroie
    risk_level: confort
    evidence:
      - 'Observation: sifflement de la courroie'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit de roulement cote accessoires
    description: bruit de roulement cote accessoires
    risk_level: confort
    evidence:
      - 'Observation: bruit de roulement cote accessoires'
      - Vérification visuelle ou auditive
  - id: S3
    label: Courroie qui patine temoin batterie
    description: courroie qui patine temoin batterie
    risk_level: confort
    evidence:
      - 'Observation: courroie qui patine temoin batterie'
      - Vérification visuelle ou auditive
  - id: S4
    label: Galet qui ne bouge plus tendeur bloque
    description: galet qui ne bouge plus tendeur bloque
    risk_level: immobilisation
    evidence:
      - 'Observation: galet qui ne bouge plus tendeur bloque'
      - Vérification visuelle ou auditive
  - id: S5
    label: Vibrations dans le moteur
    description: vibrations dans le moteur
    risk_level: confort
    evidence:
      - 'Observation: vibrations dans le moteur'
      - Vérification visuelle ou auditive
  - id: S6
    label: Bruit de claquement courroie detendue
    description: bruit de claquement courroie detendue
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit de claquement courroie detendue'
      - Vérification visuelle ou auditive
  - id: S7
    label: Courroie qui saute de son logement
    description: courroie qui saute de son logement
    risk_level: confort
    evidence:
      - 'Observation: courroie qui saute de son logement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Galet tendeur de courroie d'accessoire - Guide Diagnostic Complet

## Fonction et Rôle

Maintient la tension de la courroie d'accessoire

**Actions principales:** tendre, maintenir, guider

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Galet qui ne bouge plus tendeur bloque**
  galet qui ne bouge plus tendeur bloque

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de claquement courroie detendue**
  bruit de claquement courroie detendue

### 🟢 Autres Symptômes

- sifflement de la courroie
- bruit de roulement cote accessoires
- courroie qui patine temoin batterie
- vibrations dans le moteur
- courroie qui saute de son logement

## Procédure de Diagnostic

Pour diagnostiquer un problème de galet tendeur de courroie d'accessoire:

1. **Inspection visuelle** - Examiner l'état du galet tendeur de courroie d'accessoire
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le galet tendeur de courroie d'accessoire peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- compresseur-de-climatisation
- courroie-d-accessoire
- galet-enrouleur-de-courroie-d-accessoire
- pompe-de-direction-assistee
- poulie-d-alternateur
- poulie-vilebrequin

## Critères de Compatibilité

Pour commander le bon galet tendeur de courroie d'accessoire, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de durée de vie"
