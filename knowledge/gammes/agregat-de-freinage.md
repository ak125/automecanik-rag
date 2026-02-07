---
entity_type: gamme
title: Agregat de freinage
slug: agregat-de-freinage
pg_id: 415
category: freinage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Module hydraulique de freinage avec ABS/ESP
  must_be_true:
    - moduler
    - réguler
    - distribuer
  must_not_contain_concepts:
    - injection
    - climatisation
    - embrayage
    - distribution
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
symptoms:
  - id: S1
    label: Voyant abs allume en permanence au tableau de bord
    description: voyant abs allume en permanence au tableau de bord
    risk_level: securite
    evidence:
      - 'Observation: voyant abs allume en permanence au tableau de bord'
      - Vérification visuelle ou auditive
  - id: S2
    label: Abs qui ne se declenche plus au freinage d urgence
    description: abs qui ne se declenche plus au freinage d urgence
    risk_level: securite
    evidence:
      - 'Observation: abs qui ne se declenche plus au freinage d urgence'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit de pompe abs anormal ou continu
    description: bruit de pompe abs anormal ou continu
    risk_level: securite
    evidence:
      - 'Observation: bruit de pompe abs anormal ou continu'
      - Vérification visuelle ou auditive
  - id: S4
    label: Codes defaut abs stockes p ou c
    description: codes defaut abs stockes p ou c
    risk_level: securite
    evidence:
      - 'Observation: codes defaut abs stockes p ou c'
      - Vérification visuelle ou auditive
  - id: S5
    label: Pedale de frein qui pulse sans raison
    description: pedale de frein qui pulse sans raison
    risk_level: securite
    evidence:
      - 'Observation: pedale de frein qui pulse sans raison'
      - Vérification visuelle ou auditive
  - id: S6
    label: Esp ou controle de stabilite desactive
    description: esp ou controle de stabilite desactive
    risk_level: securite
    evidence:
      - 'Observation: esp ou controle de stabilite desactive'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Agregat de freinage - Guide Diagnostic Complet

## Fonction et Rôle

Module hydraulique de freinage avec ABS/ESP

**Actions principales:** moduler, réguler, distribuer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Voyant abs allume en permanence au tableau de bord**
  voyant abs allume en permanence au tableau de bord
- **Abs qui ne se declenche plus au freinage d urgence**
  abs qui ne se declenche plus au freinage d urgence
- **Bruit de pompe abs anormal ou continu**
  bruit de pompe abs anormal ou continu
- **Codes defaut abs stockes p ou c**
  codes defaut abs stockes p ou c
- **Pedale de frein qui pulse sans raison**
  pedale de frein qui pulse sans raison
- **Esp ou controle de stabilite desactive**
  esp ou controle de stabilite desactive

## Procédure de Diagnostic

Pour diagnostiquer un problème de agregat de freinage:

1. **Inspection visuelle** - Examiner l'état du agregat de freinage
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- agregat-de-freinage
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- etrier-de-frein
- flexible-de-frein
- interrupteur-des-feux-de-freins
- kit-de-freins-arriere

## Critères de Compatibilité

Pour commander le bon agregat de freinage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleur freinage"
