---
entity_type: gamme
title: Poulie d'arbre à came
slug: poulie-d-arbre-a-came
pg_id: 1067
category: distribution
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Entrainer l'arbre a cames en synchronisation avec le vilebrequin
  must_be_true:
    - entrainer
    - synchroniser
    - transmettre
  must_not_contain_concepts:
    - vilebrequin
    - accessoire
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
    label: Bruit de claquement au niveau de la culasse
    description: bruit de claquement au niveau de la culasse
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit de claquement au niveau de la culasse'
      - Vérification visuelle ou auditive
  - id: S2
    label: Perte de puissance progressive
    description: perte de puissance progressive
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance progressive'
      - Vérification visuelle ou auditive
  - id: S3
    label: Moteur qui cale au ralenti
    description: moteur qui cale au ralenti
    risk_level: immobilisation
    evidence:
      - 'Observation: moteur qui cale au ralenti'
      - Vérification visuelle ou auditive
  - id: S4
    label: Fumee anormale a l echappement
    description: fumee anormale a l echappement
    risk_level: confort
    evidence:
      - 'Observation: fumee anormale a l echappement'
      - Vérification visuelle ou auditive
  - id: S5
    label: Voyant moteur allume codes calage
    description: voyant moteur allume codes calage
    risk_level: immobilisation
    evidence:
      - 'Observation: voyant moteur allume codes calage'
      - Vérification visuelle ou auditive
  - id: S6
    label: Distribution a remplacer selon carnet d entretien
    description: distribution a remplacer selon carnet d entretien
    risk_level: confort
    evidence:
      - 'Observation: distribution a remplacer selon carnet d entretien'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Poulie d'arbre à came - Guide Diagnostic Complet

## Fonction et Rôle

Entrainer l'arbre a cames en synchronisation avec le vilebrequin

**Actions principales:** entrainer, synchroniser, transmettre

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Moteur qui cale au ralenti**
  moteur qui cale au ralenti
- **Voyant moteur allume codes calage**
  voyant moteur allume codes calage

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de claquement au niveau de la culasse**
  bruit de claquement au niveau de la culasse

### 🟢 Autres Symptômes

- perte de puissance progressive
- fumee anormale a l echappement
- distribution a remplacer selon carnet d entretien

## Procédure de Diagnostic

Pour diagnostiquer un problème de poulie d'arbre à came:

1. **Inspection visuelle** - Examiner l'état du poulie d'arbre à came
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le poulie d'arbre à came peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- arbre-a-came
- capteur-impulsion
- chaine-de-distribution
- courroie-de-distribution
- kit-de-chaine-de-distribution
- kit-de-distribution

## Critères de Compatibilité

Pour commander le bon poulie d'arbre à came, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"
