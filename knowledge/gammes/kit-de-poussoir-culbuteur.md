---
entity_type: gamme
title: Kit de poussoir culbuteur
slug: kit-de-poussoir-culbuteur
pg_id: 3320
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
    - actionner
    - lever
  must_not_contain_concepts:
    - freinage
    - climatisation
    - direction
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
    label: Claquement moteur au demarrage
    description: claquement moteur au demarrage
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement moteur au demarrage'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit qui persiste a chaud
    description: bruit qui persiste a chaud
    risk_level: confort
    evidence:
      - 'Observation: bruit qui persiste a chaud'
      - Vérification visuelle ou auditive
  - id: S3
    label: Perte de puissance legere
    description: perte de puissance legere
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance legere'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Kit de poussoir culbuteur - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre le mouvement de l'arbre a cames aux soupapes

**Actions principales:** transmettre, actionner, lever

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement moteur au demarrage**
  claquement moteur au demarrage

### 🟢 Autres Symptômes

- bruit qui persiste a chaud
- perte de puissance legere

## Procédure de Diagnostic

Pour diagnostiquer un problème de kit de poussoir culbuteur:

1. **Inspection visuelle** - Examiner l'état du kit de poussoir culbuteur
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
- culbuteur
- poussoir-de-soupape
- soupape-d-admission
- soupape-d-echappement

## Critères de Compatibilité

Pour commander le bon kit de poussoir culbuteur, vous devez connaître:

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
