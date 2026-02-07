---
entity_type: gamme
title: Crémaillière de direction
slug: cremailliere-de-direction
pg_id: 286
category: direction
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transforme la rotation du volant en déplacement des roues
  must_be_true:
    - diriger
    - guider
    - transmettre
  must_not_contain_concepts:
    - injection
    - freinage
    - distribution
    - turbo
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
    label: Fuite liquide direction visible sous
    description: fuite liquide direction visible sous
    risk_level: securite
    evidence:
      - 'Observation: fuite liquide direction visible sous'
      - Vérification visuelle ou auditive
  - id: S2
    label: Direction dure ou assistance intermittente
    description: direction dure ou assistance intermittente
    risk_level: securite
    evidence:
      - 'Observation: direction dure ou assistance intermittente'
      - Vérification visuelle ou auditive
  - id: S3
    label: Jeu excessif dans le volant
    description: jeu excessif dans le volant
    risk_level: confort
    evidence:
      - 'Observation: jeu excessif dans le volant'
      - Vérification visuelle ou auditive
  - id: S4
    label: Bruit de grincement ou de couinement en tournant
    description: bruit de grincement ou de couinement en tournant
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit de grincement ou de couinement en tournant'
      - Vérification visuelle ou auditive
  - id: S5
    label: Soufflets de cremaillere fissures ou dechires
    description: soufflets de cremaillere fissures ou dechires
    risk_level: confort
    evidence:
      - 'Observation: soufflets de cremaillere fissures ou dechires'
      - Vérification visuelle ou auditive
  - id: S6
    label: Niveau de liquide de direction qui baisse
    description: niveau de liquide de direction qui baisse
    risk_level: securite
    evidence:
      - 'Observation: niveau de liquide de direction qui baisse'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Crémaillière de direction - Guide Diagnostic Complet

## Fonction et Rôle

Transforme la rotation du volant en déplacement des roues

**Actions principales:** diriger, guider, transmettre

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de grincement ou de couinement en tournant**
  bruit de grincement ou de couinement en tournant

### 🟡 Symptômes de Sécurité

- **Fuite liquide direction visible sous**
  fuite liquide direction visible sous
- **Direction dure ou assistance intermittente**
  direction dure ou assistance intermittente
- **Niveau de liquide de direction qui baisse**
  niveau de liquide de direction qui baisse

### 🟢 Autres Symptômes

- jeu excessif dans le volant
- soufflets de cremaillere fissures ou dechires

## Procédure de Diagnostic

Pour diagnostiquer un problème de crémaillière de direction:

1. **Inspection visuelle** - Examiner l'état du crémaillière de direction
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- barre-de-direction
- bras-de-suspension
- colonne-de-direction
- pompe-de-direction-assistee
- rotule-de-direction
- rotule-de-suspension
- soufflet-de-direction

## Critères de Compatibilité

Pour commander le bon crémaillière de direction, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleure tenue de route"
