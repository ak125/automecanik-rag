---
entity_type: gamme
title: Fourchette d'embrayage
slug: fourchette-d-embrayage
pg_id: 3419
category: embrayage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Actionner la butee d'embrayage via la commande
  must_be_true:
    - actionner
    - pousser
    - deplacer
  must_not_contain_concepts:
    - injection
    - freinage
    - climatisation
    - turbo
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
symptoms:
  - id: S1
    label: Pedale d embrayage dure
    description: pedale d embrayage dure
    risk_level: confort
    evidence:
      - 'Observation: pedale d embrayage dure'
      - Vérification visuelle ou auditive
  - id: S2
    label: Difficulte a passer les vitesses
    description: difficulte a passer les vitesses
    risk_level: confort
    evidence:
      - 'Observation: difficulte a passer les vitesses'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit de claquement a l embrayage
    description: bruit de claquement a l embrayage
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit de claquement a l embrayage'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Fourchette d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Actionner la butee d'embrayage via la commande

**Actions principales:** actionner, pousser, deplacer

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de claquement a l embrayage**
  bruit de claquement a l embrayage

### 🟢 Autres Symptômes

- pedale d embrayage dure
- difficulte a passer les vitesses

## Procédure de Diagnostic

Pour diagnostiquer un problème de fourchette d'embrayage:

1. **Inspection visuelle** - Examiner l'état du fourchette d'embrayage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- guide-d-embrayage
- tringle-de-vitesses

## Critères de Compatibilité

Pour commander le bon fourchette d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "passage de vitesse parfait"
