---
entity_type: gamme
title: Filtre d'habitacle
slug: filtre-d-habitacle
pg_id: 424
category: filtration
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Filtre l'air entrant dans l'habitacle pour protéger les occupants des
    pollens, poussières et polluants
  must_be_true:
    - remplacer
    - changer
  must_not_contain_concepts:
    - huile
    - carburant
    - air moteur
    - injection
    - essence
    - diesel
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
    label: Buee persistante sur le pare-brise
    description: buee persistante sur le pare-brise
    risk_level: confort
    evidence:
      - 'Observation: buee persistante sur le pare-brise'
      - Vérification visuelle ou auditive
  - id: S2
    label: Mauvaises odeurs mise route ventilation
    description: mauvaises odeurs mise route ventilation
    risk_level: confort
    evidence:
      - 'Observation: mauvaises odeurs mise route ventilation'
      - Vérification visuelle ou auditive
  - id: S3
    label: Debit d air faible meme en vitesse maximale
    description: debit d air faible meme en vitesse maximale
    risk_level: confort
    evidence:
      - 'Observation: debit d air faible meme en vitesse maximale'
      - Vérification visuelle ou auditive
  - id: S4
    label: Bruit de ventilation anormal ou sifflement
    description: bruit de ventilation anormal ou sifflement
    risk_level: confort
    evidence:
      - 'Observation: bruit de ventilation anormal ou sifflement'
      - Vérification visuelle ou auditive
  - id: S5
    label: Climatisation moins efficace qu avant
    description: climatisation moins efficace qu avant
    risk_level: confort
    evidence:
      - 'Observation: climatisation moins efficace qu avant'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus depuis dernier changement
    description: plus depuis dernier changement
    risk_level: confort
    evidence:
      - 'Observation: plus depuis dernier changement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Filtre d'habitacle - Guide Diagnostic Complet

## Fonction et Rôle

Filtre l'air entrant dans l'habitacle pour protéger les occupants des pollens, poussières et polluants

**Actions principales:** remplacer, changer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- buee persistante sur le pare-brise
- mauvaises odeurs mise route ventilation
- debit d air faible meme en vitesse maximale
- bruit de ventilation anormal ou sifflement
- climatisation moins efficace qu avant
- plus depuis dernier changement

## Procédure de Diagnostic

Pour diagnostiquer un problème de filtre d'habitacle:

1. **Inspection visuelle** - Examiner l'état du filtre d'habitacle
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- filtre-a-air
- filtre-a-carburant
- filtre-a-huile
- pulseur-d-air-d-habitacle

## Critères de Compatibilité

Pour commander le bon filtre d'habitacle, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "lavable"
