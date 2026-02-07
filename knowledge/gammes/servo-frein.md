---
entity_type: gamme
title: Servo frein
slug: servo-frein
pg_id: 74
category: freinage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Amplifier l'effort de freinage grace a la depression moteur
  must_be_true:
    - amplifier
    - assister
    - demultiplier
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
  - if: vehicule_immobilise_ou_symptome_critique
    then: verification_urgente_piece_et_alimentation
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
symptoms:
  - id: S1
    label: Pedale de frein tres dure a enfoncer
    description: pedale de frein tres dure a enfoncer
    risk_level: securite
    evidence:
      - 'Observation: pedale de frein tres dure a enfoncer'
      - Vérification visuelle ou auditive
  - id: S2
    label: Effort au freinage anormalement eleve
    description: effort au freinage anormalement eleve
    risk_level: securite
    evidence:
      - 'Observation: effort au freinage anormalement eleve'
      - Vérification visuelle ou auditive
  - id: S3
    label: Sifflement au niveau de la pedale
    description: sifflement au niveau de la pedale
    risk_level: confort
    evidence:
      - 'Observation: sifflement au niveau de la pedale'
      - Vérification visuelle ou auditive
  - id: S4
    label: Pedale qui vibre au freinage
    description: pedale qui vibre au freinage
    risk_level: securite
    evidence:
      - 'Observation: pedale qui vibre au freinage'
      - Vérification visuelle ou auditive
  - id: S5
    label: Moteur qui cale au freinage prise d air
    description: moteur qui cale au freinage prise d air
    risk_level: immobilisation
    evidence:
      - 'Observation: moteur qui cale au freinage prise d air'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Servo frein - Guide Diagnostic Complet

## Fonction et Rôle

Amplifier l'effort de freinage grace a la depression moteur

**Actions principales:** amplifier, assister, demultiplier

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Moteur qui cale au freinage prise d air**
  moteur qui cale au freinage prise d air

### 🟡 Symptômes de Sécurité

- **Pedale de frein tres dure a enfoncer**
  pedale de frein tres dure a enfoncer
- **Effort au freinage anormalement eleve**
  effort au freinage anormalement eleve
- **Pedale qui vibre au freinage**
  pedale qui vibre au freinage

### 🟢 Autres Symptômes

- sifflement au niveau de la pedale

## Procédure de Diagnostic

Pour diagnostiquer un problème de servo frein:

1. **Inspection visuelle** - Examiner l'état du servo frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le servo frein peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes

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

Pour commander le bon servo frein, vous devez connaître:

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
