---
entity_type: gamme
title: Chaîne de distribution
slug: chaine-de-distribution
pg_id: 1123
category: distribution
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Synchroniser la rotation de l'arbre a cames avec le vilebrequin de maniere
    durable
  must_be_true:
    - synchroniser
    - entrainer
    - transmettre
  must_not_contain_concepts:
    - courroie
    - caoutchouc
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
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
symptoms:
  - id: S1
    label: Bruit de cliquetis metallique au demarrage a froid
    description: bruit de cliquetis metallique au demarrage a froid
    risk_level: confort
    evidence:
      - 'Observation: bruit de cliquetis metallique au demarrage a froid'
      - Vérification visuelle ou auditive
  - id: S2
    label: Claquement qui disparait apres quelques secondes
    description: claquement qui disparait apres quelques secondes
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement qui disparait apres quelques secondes'
      - Vérification visuelle ou auditive
  - id: S3
    label: Voyant moteur allume codes calage
    description: voyant moteur allume codes calage
    risk_level: immobilisation
    evidence:
      - 'Observation: voyant moteur allume codes calage'
      - Vérification visuelle ou auditive
  - id: S4
    label: Moteur qui manque de puissance
    description: moteur qui manque de puissance
    risk_level: confort
    evidence:
      - 'Observation: moteur qui manque de puissance'
      - Vérification visuelle ou auditive
  - id: S5
    label: Bruit de ferraille permanent cote distribution
    description: bruit de ferraille permanent cote distribution
    risk_level: confort
    evidence:
      - 'Observation: bruit de ferraille permanent cote distribution'
      - Vérification visuelle ou auditive
  - id: S6
    label: Difficultes de demarrage
    description: difficultes de demarrage
    risk_level: confort
    evidence:
      - 'Observation: difficultes de demarrage'
      - Vérification visuelle ou auditive
  - id: S7
    label: Consommation huile anormale tendeur hydraulique
    description: consommation huile anormale tendeur hydraulique
    risk_level: confort
    evidence:
      - 'Observation: consommation huile anormale tendeur hydraulique'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Chaîne de distribution - Guide Diagnostic Complet

## Fonction et Rôle

Synchroniser la rotation de l'arbre a cames avec le vilebrequin de maniere durable

**Actions principales:** synchroniser, entrainer, transmettre

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Voyant moteur allume codes calage**
  voyant moteur allume codes calage

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement qui disparait apres quelques secondes**
  claquement qui disparait apres quelques secondes

### 🟢 Autres Symptômes

- bruit de cliquetis metallique au demarrage a froid
- moteur qui manque de puissance
- bruit de ferraille permanent cote distribution
- difficultes de demarrage
- consommation huile anormale tendeur hydraulique

## Procédure de Diagnostic

Pour diagnostiquer un problème de chaîne de distribution:

1. **Inspection visuelle** - Examiner l'état du chaîne de distribution
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le chaîne de distribution peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-d-accessoire
- kit-de-chaine-de-distribution
- pompe-a-eau
- pompe-a-injection
- poulie-d-arbre-a-came

## Critères de Compatibilité

Pour commander le bon chaîne de distribution, vous devez connaître:

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
