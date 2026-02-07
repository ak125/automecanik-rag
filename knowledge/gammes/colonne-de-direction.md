---
entity_type: gamme
title: Colonne de direction
slug: colonne-de-direction
pg_id: 1211
category: direction
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Relier le volant a la cremailliere - Transmet la rotation du conducteur au
    systeme de direction
  must_be_true:
    - relier
    - transmettre
    - connecter
  must_not_contain_concepts:
    - suspension
    - amortissement
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
symptoms:
  - id: S1
    label: Jeu important du volant vertical ou lateral
    description: jeu important du volant vertical ou lateral
    risk_level: confort
    evidence:
      - 'Observation: jeu important du volant vertical ou lateral'
      - Vérification visuelle ou auditive
  - id: S2
    label: Craquements ou bruits secs en tournant le volant
    description: craquements ou bruits secs en tournant le volant
    risk_level: confort
    evidence:
      - 'Observation: craquements ou bruits secs en tournant le volant'
      - Vérification visuelle ou auditive
  - id: S3
    label: Volant qui ne revient pas seul apres un virage
    description: volant qui ne revient pas seul apres un virage
    risk_level: confort
    evidence:
      - 'Observation: volant qui ne revient pas seul apres un virage'
      - Vérification visuelle ou auditive
  - id: S4
    label: Bruits de frottement dans la colonne
    description: bruits de frottement dans la colonne
    risk_level: confort
    evidence:
      - 'Observation: bruits de frottement dans la colonne'
      - Vérification visuelle ou auditive
  - id: S5
    label: Voyant direction assistee allume
    description: voyant direction assistee allume
    risk_level: securite
    evidence:
      - 'Observation: voyant direction assistee allume'
      - Vérification visuelle ou auditive
  - id: S6
    label: Sensation de points durs en tournant
    description: sensation de points durs en tournant
    risk_level: confort
    evidence:
      - 'Observation: sensation de points durs en tournant'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Colonne de direction - Guide Diagnostic Complet

## Fonction et Rôle

Relier le volant a la cremailliere - Transmet la rotation du conducteur au systeme de direction

**Actions principales:** relier, transmettre, connecter, vehiculer la rotation

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Voyant direction assistee allume**
  voyant direction assistee allume

### 🟢 Autres Symptômes

- jeu important du volant vertical ou lateral
- craquements ou bruits secs en tournant le volant
- volant qui ne revient pas seul apres un virage
- bruits de frottement dans la colonne
- sensation de points durs en tournant

## Procédure de Diagnostic

Pour diagnostiquer un problème de colonne de direction:

1. **Inspection visuelle** - Examiner l'état du colonne de direction
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- cremailliere-de-direction
- pompe-de-direction-assistee
- rotule-de-direction

## Critères de Compatibilité

Pour commander le bon colonne de direction, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"
