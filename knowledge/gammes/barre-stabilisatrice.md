---
entity_type: gamme
title: Barre stabilisatrice
slug: barre-stabilisatrice
pg_id: 274
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
    Limiter le roulis en virage - Relie les deux cotes de la suspension pour
    transferer les efforts
  must_be_true:
    - limiter le roulis
    - stabiliser
    - relier
  must_not_contain_concepts:
    - direction
    - cremailliere
    - volant
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
    label: Roulis excessif en virage
    description: roulis excessif en virage
    risk_level: confort
    evidence:
      - 'Observation: roulis excessif en virage'
      - Vérification visuelle ou auditive
  - id: S2
    label: Claquements sur route degradee
    description: claquements sur route degradee
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquements sur route degradee'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruits sourds en compression
    description: bruits sourds en compression
    risk_level: confort
    evidence:
      - 'Observation: bruits sourds en compression'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Barre stabilisatrice - Guide Diagnostic Complet

## Fonction et Rôle

Limiter le roulis en virage - Relie les deux cotes de la suspension pour transferer les efforts

**Actions principales:** limiter le roulis, stabiliser, relier, equilibrer

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquements sur route degradee**
  claquements sur route degradee

### 🟢 Autres Symptômes

- roulis excessif en virage
- bruits sourds en compression

## Procédure de Diagnostic

Pour diagnostiquer un problème de barre stabilisatrice:

1. **Inspection visuelle** - Examiner l'état du barre stabilisatrice
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bras-de-suspension

## Critères de Compatibilité

Pour commander le bon barre stabilisatrice, vous devez connaître:

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
