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
  - if: symptome_voyant-abs-allume-en-permanence-au
    then: verifier_piece
  - if: symptome_abs-qui-ne-se-declenche-plus
    then: diagnostic_approfondi
  - if: symptome_bruit-de-pompe-abs-anormal-ou
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Voyant abs allume en permanence au
    description: voyant abs allume en permanence au tableau de bord
    risk_level: securite
    evidence:
      - 'Observation: voyant abs allume en permanence au'
      - Vérification visuelle ou auditive
  - id: S2
    label: Abs qui ne se declenche plus
    description: abs qui ne se declenche plus au freinage d urgence
    risk_level: securite
    evidence:
      - 'Observation: abs qui ne se declenche plus'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit de pompe abs anormal ou
    description: bruit de pompe abs anormal ou continu
    risk_level: securite
    evidence:
      - 'Observation: bruit de pompe abs anormal ou'
      - Vérification visuelle ou auditive
  - id: S4
    label: Codes defaut abs stockes p ou
    description: codes defaut abs stockes p ou c
    risk_level: securite
    evidence:
      - 'Observation: codes defaut abs stockes p ou'
      - Vérification visuelle ou auditive
  - id: S5
    label: Pedale de frein qui pulse sans
    description: pedale de frein qui pulse sans raison
    risk_level: securite
    evidence:
      - 'Observation: pedale de frein qui pulse sans'
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
# Agregat de freinage - Guide Complet

## Fonction

Module hydraulique de freinage avec ABS/ESP

## Symptômes de défaillance

### Voyant abs allume en permanence au

voyant abs allume en permanence au tableau de bord

### Abs qui ne se declenche plus

abs qui ne se declenche plus au freinage d urgence

### Bruit de pompe abs anormal ou

bruit de pompe abs anormal ou continu

### Codes defaut abs stockes p ou

codes defaut abs stockes p ou c

### Pedale de frein qui pulse sans

pedale de frein qui pulse sans raison

### Esp ou controle de stabilite desactive

esp ou controle de stabilite desactive

## Diagnostic

Pour diagnostiquer un problème de agregat de freinage:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- agregat-de-freinage
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- etrier-de-frein

## Compatibilité

Pour commander le bon agregat de freinage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
