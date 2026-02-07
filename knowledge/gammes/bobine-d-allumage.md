---
entity_type: gamme
title: Bobine d'allumage
slug: bobine-d-allumage
pg_id: 689
category: allumage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Transformer la basse tension batterie en haute tension (15-40kV) pour creer
    l'etincelle aux bougies
  must_be_true:
    - transformer la tension
    - amplifier
    - generer la haute tension
  must_not_contain_concepts:
    - diesel
    - prechauffage
    - incandescence
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
symptoms:
  - id: S1
    label: Rate moteur localise sur un cylindre precis
    description: rate moteur localise sur un cylindre precis
    risk_level: confort
    evidence:
      - 'Observation: rate moteur localise sur un cylindre precis'
      - Vérification visuelle ou auditive
  - id: S2
    label: Voyant moteur allume code p030x
    description: voyant moteur allume code p030x
    risk_level: confort
    evidence:
      - 'Observation: voyant moteur allume code p030x'
      - Vérification visuelle ou auditive
  - id: S3
    label: Perte de puissance brutale ou progressive
    description: perte de puissance brutale ou progressive
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance brutale ou progressive'
      - Vérification visuelle ou auditive
  - id: S4
    label: Surconsommation de carburant
    description: surconsommation de carburant
    risk_level: confort
    evidence:
      - 'Observation: surconsommation de carburant'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur d essence non brulee a l echappement
    description: odeur d essence non brulee a l echappement
    risk_level: confort
    evidence:
      - 'Observation: odeur d essence non brulee a l echappement'
      - Vérification visuelle ou auditive
  - id: S6
    label: Demarrage difficile par temps humide
    description: demarrage difficile par temps humide
    risk_level: confort
    evidence:
      - 'Observation: demarrage difficile par temps humide'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Bobine d'allumage - Guide Diagnostic Complet

## Fonction et Rôle

Transformer la basse tension batterie en haute tension (15-40kV) pour creer l'etincelle aux bougies

**Actions principales:** transformer la tension, amplifier, generer la haute tension, alimenter les bougies, creer l'arc

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- rate moteur localise sur un cylindre precis
- voyant moteur allume code p030x
- perte de puissance brutale ou progressive
- surconsommation de carburant
- odeur d essence non brulee a l echappement
- demarrage difficile par temps humide

## Procédure de Diagnostic

Pour diagnostiquer un problème de bobine d'allumage:

1. **Inspection visuelle** - Examiner l'état du bobine d'allumage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- bougie-d-allumage
- faisceau-d-allumage

## Critères de Compatibilité

Pour commander le bon bobine d'allumage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"
