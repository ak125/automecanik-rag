---
entity_type: gamme
title: Tube d'échappement
slug: tube-d-echappement
pg_id: 17
category: echappement
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Achemine et évacue les gaz d'échappement traités vers l'extérieur
  must_be_true:
    - evacuer
    - acheminer
    - conduire
  must_not_contain_concepts:
    - injection
    - freinage
    - climatisation
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
    label: Bruit echappement anormalement fort metallique
    description: bruit echappement anormalement fort metallique
    risk_level: confort
    evidence:
      - 'Observation: bruit echappement anormalement fort metallique'
      - Vérification visuelle ou auditive
  - id: S2
    label: Trou ou rouille visible sous le vehicule visuel
    description: trou ou rouille visible sous le vehicule visuel
    risk_level: confort
    evidence:
      - 'Observation: trou ou rouille visible sous le vehicule visuel'
      - Vérification visuelle ou auditive
  - id: S3
    label: Odeur echappement habitacle olfactif
    description: odeur echappement habitacle olfactif
    risk_level: confort
    evidence:
      - 'Observation: odeur echappement habitacle olfactif'
      - Vérification visuelle ou auditive
  - id: S4
    label: Vibrations excessives ressenties plancher comportement
    description: vibrations excessives ressenties plancher comportement
    risk_level: confort
    evidence:
      - 'Observation: vibrations excessives ressenties plancher comportement'
      - Vérification visuelle ou auditive
  - id: S5
    label: Fumee vapeur echappant sous vehicule
    description: fumee vapeur echappant sous vehicule
    risk_level: confort
    evidence:
      - 'Observation: fumee vapeur echappant sous vehicule'
      - Vérification visuelle ou auditive
  - id: S6
    label: Vehicule plus roulant preventif
    description: vehicule plus roulant preventif
    risk_level: confort
    evidence:
      - 'Observation: vehicule plus roulant preventif'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Tube d'échappement - Guide Diagnostic Complet

## Fonction et Rôle

Achemine et évacue les gaz d'échappement traités vers l'extérieur

**Actions principales:** evacuer, acheminer, conduire

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- bruit echappement anormalement fort metallique
- trou ou rouille visible sous le vehicule visuel
- odeur echappement habitacle olfactif
- vibrations excessives ressenties plancher comportement
- fumee vapeur echappant sous vehicule
- vehicule plus roulant preventif

## Procédure de Diagnostic

Pour diagnostiquer un problème de tube d'échappement:

1. **Inspection visuelle** - Examiner l'état du tube d'échappement
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- catalyseur
- fap

## Critères de Compatibilité

Pour commander le bon tube d'échappement, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "passe le controle technique"
