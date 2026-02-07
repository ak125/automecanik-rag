---
entity_type: gamme
title: Moyeu de roue
slug: moyeu-de-roue
pg_id: 653
category: direction
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Supporter la roue et transmettre la rotation - Fixe la roue au roulement
  must_be_true:
    - supporter
    - fixer
    - transmettre
  must_not_contain_concepts:
    - direction
    - cremailliere
    - volant
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: vibrations_anormales
    then: verifier_equilibrage_et_fixations
symptoms:
  - id: S1
    label: Jeu anormal de la roue
    description: jeu anormal de la roue
    risk_level: confort
    evidence:
      - 'Observation: jeu anormal de la roue'
      - Vérification visuelle ou auditive
  - id: S2
    label: Vibrations a vitesse constante
    description: vibrations a vitesse constante
    risk_level: confort
    evidence:
      - 'Observation: vibrations a vitesse constante'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruits sourds en roulant
    description: bruits sourds en roulant
    risk_level: confort
    evidence:
      - 'Observation: bruits sourds en roulant'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Moyeu de roue - Guide Diagnostic Complet

## Fonction et Rôle

Supporter la roue et transmettre la rotation - Fixe la roue au roulement

**Actions principales:** supporter, fixer, transmettre, recevoir la roue

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- jeu anormal de la roue
- vibrations a vitesse constante
- bruits sourds en roulant

## Procédure de Diagnostic

Pour diagnostiquer un problème de moyeu de roue:

1. **Inspection visuelle** - Examiner l'état du moyeu de roue
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- roulement-de-roue
- disque-de-frein

## Critères de Compatibilité

Pour commander le bon moyeu de roue, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"
