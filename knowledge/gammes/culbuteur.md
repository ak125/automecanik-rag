---
entity_type: gamme
title: Culbuteur
slug: culbuteur
pg_id: 432
category: moteur
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmettre le mouvement de l'arbre a cames aux soupapes
  must_be_true:
    - transmettre
    - basculer
    - actionner
  must_not_contain_concepts:
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
    label: Claquement moteur regulier
    description: claquement moteur regulier
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement moteur regulier'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit de tic-tic au ralenti
    description: bruit de tic-tic au ralenti
    risk_level: confort
    evidence:
      - 'Observation: bruit de tic-tic au ralenti'
      - Vérification visuelle ou auditive
  - id: S3
    label: Perte de puissance sur un cylindre
    description: perte de puissance sur un cylindre
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance sur un cylindre'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Culbuteur - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre le mouvement de l'arbre a cames aux soupapes

**Actions principales:** transmettre, basculer, actionner

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement moteur regulier**
  claquement moteur regulier

### 🟢 Autres Symptômes

- bruit de tic-tic au ralenti
- perte de puissance sur un cylindre

## Procédure de Diagnostic

Pour diagnostiquer un problème de culbuteur:

1. **Inspection visuelle** - Examiner l'état du culbuteur
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- arbre-a-came
- kit-de-poussoir-culbuteur
- poussoir-de-soupape
- soupape-d-admission
- soupape-d-echappement

## Critères de Compatibilité

Pour commander le bon culbuteur, vous devez connaître:

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
