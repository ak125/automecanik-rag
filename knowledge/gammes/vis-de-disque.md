---
entity_type: gamme
title: Vis de disque
slug: vis-de-disque
pg_id: 54
category: freinage
subcategory: disques
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Fixer le disque de frein sur le moyeu de roue
  must_be_true:
    - fixer
    - maintenir
    - bloquer
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
symptoms:
  - id: S1
    label: Vis grippee impossible a devisser
    description: vis grippee impossible a devisser
    risk_level: confort
    evidence:
      - 'Observation: vis grippee impossible a devisser'
      - Vérification visuelle ou auditive
  - id: S2
    label: Tete de vis arrondie ou endommagee
    description: tete de vis arrondie ou endommagee
    risk_level: confort
    evidence:
      - 'Observation: tete de vis arrondie ou endommagee'
      - Vérification visuelle ou auditive
  - id: S3
    label: Vis rouillee visible a travers la jante
    description: vis rouillee visible a travers la jante
    risk_level: confort
    evidence:
      - 'Observation: vis rouillee visible a travers la jante'
      - Vérification visuelle ou auditive
  - id: S4
    label: Disque qui bouge legerement vis desserree
    description: disque qui bouge legerement vis desserree
    risk_level: confort
    evidence:
      - 'Observation: disque qui bouge legerement vis desserree'
      - Vérification visuelle ou auditive
  - id: S5
    label: Bruit claquement freinage cassee absente
    description: bruit claquement freinage cassee absente
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit claquement freinage cassee absente'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Vis de disque - Guide Diagnostic Complet

## Fonction et Rôle

Fixer le disque de frein sur le moyeu de roue

**Actions principales:** fixer, maintenir, bloquer

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit claquement freinage cassee absente**
  bruit claquement freinage cassee absente

### 🟢 Autres Symptômes

- vis grippee impossible a devisser
- tete de vis arrondie ou endommagee
- vis rouillee visible a travers la jante
- disque qui bouge legerement vis desserree

## Procédure de Diagnostic

Pour diagnostiquer un problème de vis de disque:

1. **Inspection visuelle** - Examiner l'état du vis de disque
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- disque-de-frein

## Critères de Compatibilité

Pour commander le bon vis de disque, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "freinage garanti"
