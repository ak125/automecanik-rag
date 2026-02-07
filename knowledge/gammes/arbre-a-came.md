---
entity_type: gamme
title: Arbre à came
slug: arbre-a-came
pg_id: 566
category: moteur
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Commander l'ouverture et la fermeture des soupapes
  must_be_true:
    - commander
    - synchroniser
    - actionner les soupapes
  must_not_contain_concepts:
    - vilebrequin
    - boite de vitesses
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
    label: Bruit moteur
    description: bruit moteur
    risk_level: confort
    evidence:
      - 'Observation: bruit moteur'
      - Vérification visuelle ou auditive
  - id: S2
    label: Claquement
    description: claquement
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement'
      - Vérification visuelle ou auditive
  - id: S3
    label: Perte puissance
    description: perte puissance
    risk_level: confort
    evidence:
      - 'Observation: perte puissance'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Arbre à came - Guide Diagnostic Complet

## Fonction et Rôle

Commander l'ouverture et la fermeture des soupapes

**Actions principales:** commander, synchroniser, actionner les soupapes

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement**
  claquement

### 🟢 Autres Symptômes

- bruit moteur
- perte puissance

## Procédure de Diagnostic

Pour diagnostiquer un problème de arbre à came:

1. **Inspection visuelle** - Examiner l'état du arbre à came
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-de-distribution
- culbuteur
- kit-de-poussoir-culbuteur
- poulie-d-arbre-a-came
- poussoir-de-soupape

## Critères de Compatibilité

Pour commander le bon arbre à came, vous devez connaître:

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
