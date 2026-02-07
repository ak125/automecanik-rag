---
entity_type: gamme
title: Joint arbre longitudinal
slug: joint-arbre-longitudinal
pg_id: 1427
category: transmission
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmettre le couple entre les elements de transmission
  must_be_true:
    - transmettre
    - articuler
    - relier
  must_not_contain_concepts:
    - injection
    - freinage
    - climatisation
    - allumage
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
    label: Vibrations a vitesse constante
    description: vibrations a vitesse constante
    risk_level: confort
    evidence:
      - 'Observation: vibrations a vitesse constante'
      - Vérification visuelle ou auditive
  - id: S2
    label: Claquements en acceleration deceleration
    description: claquements en acceleration deceleration
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquements en acceleration deceleration'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruits de roulement sous le vehicule
    description: bruits de roulement sous le vehicule
    risk_level: confort
    evidence:
      - 'Observation: bruits de roulement sous le vehicule'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Joint arbre longitudinal - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre le couple entre les elements de transmission

**Actions principales:** transmettre, articuler, relier

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquements en acceleration deceleration**
  claquements en acceleration deceleration

### 🟢 Autres Symptômes

- vibrations a vitesse constante
- bruits de roulement sous le vehicule

## Procédure de Diagnostic

Pour diagnostiquer un problème de joint arbre longitudinal:

1. **Inspection visuelle** - Examiner l'état du joint arbre longitudinal
2. **Test dynamique** - Vérifier les bruits en roulant
3. **Contrôle du jeu** - Examiner l'usure des articulations
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- cardan
- soufflet-de-cardan

## Critères de Compatibilité

Pour commander le bon joint arbre longitudinal, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "transmission parfaite"
