---
entity_type: gamme
title: Intercooler
slug: intercooler
pg_id: 468
category: turbo
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Refroidit l'air comprimé par le turbo
  must_be_true:
    - refroidir
    - echanger
    - densifier
  must_not_contain_concepts:
    - climatisation
    - freinage
    - distribution
    - embrayage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
symptoms:
  - id: S1
    label: Perte de puissance a l acceleration
    description: perte de puissance a l acceleration
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance a l acceleration'
      - Vérification visuelle ou auditive
  - id: S2
    label: Fumee a l acceleration huile dans admission
    description: fumee a l acceleration huile dans admission
    risk_level: confort
    evidence:
      - 'Observation: fumee a l acceleration huile dans admission'
      - Vérification visuelle ou auditive
  - id: S3
    label: Fuite d air audible sifflement
    description: fuite d air audible sifflement
    risk_level: confort
    evidence:
      - 'Observation: fuite d air audible sifflement'
      - Vérification visuelle ou auditive
  - id: S4
    label: Intercooler gras ou huileux a l exterieur
    description: intercooler gras ou huileux a l exterieur
    risk_level: confort
    evidence:
      - 'Observation: intercooler gras ou huileux a l exterieur'
      - Vérification visuelle ou auditive
  - id: S5
    label: Ailettes ecrasees ou deformees choc
    description: ailettes ecrasees ou deformees choc
    risk_level: confort
    evidence:
      - 'Observation: ailettes ecrasees ou deformees choc'
      - Vérification visuelle ou auditive
  - id: S6
    label: Surconsommation apres casse turbo
    description: surconsommation apres casse turbo
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: surconsommation apres casse turbo'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Intercooler - Guide Diagnostic Complet

## Fonction et Rôle

Refroidit l'air comprimé par le turbo

**Actions principales:** refroidir, echanger, densifier

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Surconsommation apres casse turbo**
  surconsommation apres casse turbo

### 🟢 Autres Symptômes

- perte de puissance a l acceleration
- fumee a l acceleration huile dans admission
- fuite d air audible sifflement
- intercooler gras ou huileux a l exterieur
- ailettes ecrasees ou deformees choc

## Procédure de Diagnostic

Pour diagnostiquer un problème de intercooler:

1. **Inspection visuelle** - Examiner l'état du intercooler
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- turbo

## Critères de Compatibilité

Pour commander le bon intercooler, vous devez connaître:

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
