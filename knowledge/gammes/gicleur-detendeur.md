---
entity_type: gamme
title: Gicleur détendeur
slug: gicleur-detendeur
pg_id: 2408
category: climatisation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Detendre le fluide frigorigene avant l'evaporateur
  must_be_true:
    - detendre
    - abaisser la pression
  must_not_contain_concepts:
    - injection
    - freinage
    - allumage
    - embrayage
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
    label: Clim qui refroidit mal
    description: clim qui refroidit mal
    risk_level: confort
    evidence:
      - 'Observation: clim qui refroidit mal'
      - Vérification visuelle ou auditive
  - id: S2
    label: Givre visible sur les conduites
    description: givre visible sur les conduites
    risk_level: confort
    evidence:
      - 'Observation: givre visible sur les conduites'
      - Vérification visuelle ou auditive
  - id: S3
    label: Clim qui fonctionne par a-coups
    description: clim qui fonctionne par a-coups
    risk_level: confort
    evidence:
      - 'Observation: clim qui fonctionne par a-coups'
      - Vérification visuelle ou auditive
  - id: S4
    label: Compresseur qui s emballe
    description: compresseur qui s emballe
    risk_level: confort
    evidence:
      - 'Observation: compresseur qui s emballe'
      - Vérification visuelle ou auditive
  - id: S5
    label: Bruits de glouglou dans le circuit
    description: bruits de glouglou dans le circuit
    risk_level: confort
    evidence:
      - 'Observation: bruits de glouglou dans le circuit'
      - Vérification visuelle ou auditive
  - id: S6
    label: Clim qui marche puis s arrete
    description: clim qui marche puis s arrete
    risk_level: confort
    evidence:
      - 'Observation: clim qui marche puis s arrete'
      - Vérification visuelle ou auditive
  - id: S7
    label: Pressions instables au diagnostic
    description: pressions instables au diagnostic
    risk_level: confort
    evidence:
      - 'Observation: pressions instables au diagnostic'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Gicleur détendeur - Guide Diagnostic Complet

## Fonction et Rôle

Detendre le fluide frigorigene avant l'evaporateur

**Actions principales:** detendre, abaisser la pression

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- clim qui refroidit mal
- givre visible sur les conduites
- clim qui fonctionne par a-coups
- compresseur qui s emballe
- bruits de glouglou dans le circuit
- clim qui marche puis s arrete

## Procédure de Diagnostic

Pour diagnostiquer un problème de gicleur détendeur:

1. **Inspection visuelle** - Examiner l'état du gicleur détendeur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- evaporateur-de-climatisation
- conduite-de-climatisation

## Critères de Compatibilité

Pour commander le bon gicleur détendeur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidit instantanement"
