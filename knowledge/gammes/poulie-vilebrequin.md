---
entity_type: gamme
title: Poulie vilebrequin
slug: poulie-vilebrequin
pg_id: 3213
category: distribution
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmet le mouvement du vilebrequin aux accessoires
  must_be_true:
    - entrainer
    - transmettre
    - amortir
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
    label: Vibrations moteur importantes au ralenti
    description: vibrations moteur importantes au ralenti
    risk_level: confort
    evidence:
      - 'Observation: vibrations moteur importantes au ralenti'
      - Vérification visuelle ou auditive
  - id: S2
    label: Caoutchouc de la poulie fissure ou decolle
    description: caoutchouc de la poulie fissure ou decolle
    risk_level: confort
    evidence:
      - 'Observation: caoutchouc de la poulie fissure ou decolle'
      - Vérification visuelle ou auditive
  - id: S3
    label: Courroie d accessoire qui deraille
    description: courroie d accessoire qui deraille
    risk_level: confort
    evidence:
      - 'Observation: courroie d accessoire qui deraille'
      - Vérification visuelle ou auditive
  - id: S4
    label: Bruit sourd au niveau du bas moteur
    description: bruit sourd au niveau du bas moteur
    risk_level: confort
    evidence:
      - 'Observation: bruit sourd au niveau du bas moteur'
      - Vérification visuelle ou auditive
  - id: S5
    label: Reperes de calage impossibles a aligner
    description: reperes de calage impossibles a aligner
    risk_level: immobilisation
    evidence:
      - 'Observation: reperes de calage impossibles a aligner'
      - Vérification visuelle ou auditive
  - id: S6
    label: Voyant moteur codes vibrations vilebrequin
    description: voyant moteur codes vibrations vilebrequin
    risk_level: confort
    evidence:
      - 'Observation: voyant moteur codes vibrations vilebrequin'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Poulie vilebrequin - Guide Diagnostic Complet

## Fonction et Rôle

Transmet le mouvement du vilebrequin aux accessoires

**Actions principales:** entrainer, transmettre, amortir

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Reperes de calage impossibles a aligner**
  reperes de calage impossibles a aligner

### 🟢 Autres Symptômes

- vibrations moteur importantes au ralenti
- caoutchouc de la poulie fissure ou decolle
- courroie d accessoire qui deraille
- bruit sourd au niveau du bas moteur
- voyant moteur codes vibrations vilebrequin

## Procédure de Diagnostic

Pour diagnostiquer un problème de poulie vilebrequin:

1. **Inspection visuelle** - Examiner l'état du poulie vilebrequin
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le poulie vilebrequin peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- capteur-impulsion
- compresseur-de-climatisation
- courroie-d-accessoire
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- pompe-de-direction-assistee
- poulie-d-alternateur

## Critères de Compatibilité

Pour commander le bon poulie vilebrequin, vous devez connaître:

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
