---
entity_type: gamme
title: Maître cylindre de frein
slug: maitre-cylindre-de-frein
pg_id: 258
category: freinage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transformer l'action de la pedale en pression hydraulique
  must_be_true:
    - generer la pression
    - alimenter le circuit
    - commander le freinage
  must_not_contain_concepts:
    - friction
    - thermique
    - ABS
    - electronique
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
symptoms:
  - id: S1
    label: Pedale de frein qui s enfonce lentement a l arret
    description: pedale de frein qui s enfonce lentement a l arret
    risk_level: securite
    evidence:
      - 'Observation: pedale de frein qui s enfonce lentement a l arret'
      - Vérification visuelle ou auditive
  - id: S2
    label: Niveau liquide baisse fuite visible
    description: niveau liquide baisse fuite visible
    risk_level: confort
    evidence:
      - 'Observation: niveau liquide baisse fuite visible'
      - Vérification visuelle ou auditive
  - id: S3
    label: Pedale de frein molle malgre une purge recente
    description: pedale de frein molle malgre une purge recente
    risk_level: securite
    evidence:
      - 'Observation: pedale de frein molle malgre une purge recente'
      - Vérification visuelle ou auditive
  - id: S4
    label: Liquide de frein qui fuit dans l habitacle servo
    description: liquide de frein qui fuit dans l habitacle servo
    risk_level: securite
    evidence:
      - 'Observation: liquide de frein qui fuit dans l habitacle servo'
      - Vérification visuelle ou auditive
  - id: S5
    label: Perte de freinage progressive sur un circuit
    description: perte de freinage progressive sur un circuit
    risk_level: securite
    evidence:
      - 'Observation: perte de freinage progressive sur un circuit'
      - Vérification visuelle ou auditive
  - id: S6
    label: Voyant niveau liquide de frein allume
    description: voyant niveau liquide de frein allume
    risk_level: securite
    evidence:
      - 'Observation: voyant niveau liquide de frein allume'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Maître cylindre de frein - Guide Diagnostic Complet

## Fonction et Rôle

Transformer l'action de la pedale en pression hydraulique

**Actions principales:** generer la pression, alimenter le circuit, commander le freinage, convertir, pousser le liquide

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Pedale de frein qui s enfonce lentement a l arret**
  pedale de frein qui s enfonce lentement a l arret
- **Pedale de frein molle malgre une purge recente**
  pedale de frein molle malgre une purge recente
- **Liquide de frein qui fuit dans l habitacle servo**
  liquide de frein qui fuit dans l habitacle servo
- **Perte de freinage progressive sur un circuit**
  perte de freinage progressive sur un circuit
- **Voyant niveau liquide de frein allume**
  voyant niveau liquide de frein allume

### 🟢 Autres Symptômes

- niveau liquide baisse fuite visible

## Procédure de Diagnostic

Pour diagnostiquer un problème de maître cylindre de frein:

1. **Inspection visuelle** - Examiner l'état du maître cylindre de frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

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

Pour commander le bon maître cylindre de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "efficacite garantie"
