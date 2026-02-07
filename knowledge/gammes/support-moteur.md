---
entity_type: gamme
title: Support moteur
slug: support-moteur
pg_id: 247
category: support_moteur
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Fixe et isole le moteur du châssis
  must_be_true:
    - supporter
    - isoler
    - fixer
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
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Vibrations excessives ressenties volant habitacle
    description: vibrations excessives ressenties volant habitacle
    risk_level: confort
    evidence:
      - 'Observation: vibrations excessives ressenties volant habitacle'
      - Vérification visuelle ou auditive
  - id: S2
    label: Caoutchouc support visiblement fissure affaisse
    description: caoutchouc support visiblement fissure affaisse
    risk_level: confort
    evidence:
      - 'Observation: caoutchouc support visiblement fissure affaisse'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit sourd ou claquement lors des accelerations
    description: bruit sourd ou claquement lors des accelerations
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit sourd ou claquement lors des accelerations'
      - Vérification visuelle ou auditive
  - id: S4
    label: Moteur bouge anormalement ouverture capot
    description: moteur bouge anormalement ouverture capot
    risk_level: confort
    evidence:
      - 'Observation: moteur bouge anormalement ouverture capot'
      - Vérification visuelle ou auditive
  - id: S5
    label: A-coups au passage des vitesses
    description: a-coups au passage des vitesses
    risk_level: confort
    evidence:
      - 'Observation: a-coups au passage des vitesses'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 120 000 km ou vibrations au ralenti
    description: plus de 120 000 km ou vibrations au ralenti
    risk_level: confort
    evidence:
      - 'Observation: plus de 120 000 km ou vibrations au ralenti'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Support moteur - Guide Diagnostic Complet

## Fonction et Rôle

Fixe et isole le moteur du châssis

**Actions principales:** supporter, isoler, fixer, absorber

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit sourd ou claquement lors des accelerations**
  bruit sourd ou claquement lors des accelerations

### 🟢 Autres Symptômes

- vibrations excessives ressenties volant habitacle
- caoutchouc support visiblement fissure affaisse
- moteur bouge anormalement ouverture capot
- a-coups au passage des vitesses
- plus de 120 000 km ou vibrations au ralenti

## Procédure de Diagnostic

Pour diagnostiquer un problème de support moteur:

1. **Inspection visuelle** - Examiner l'état du support moteur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-d-accessoire
- courroie-de-distribution
- kit-de-chaine-de-distribution
- kit-de-distribution

## Critères de Compatibilité

Pour commander le bon support moteur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "moins de vibrations garanties"
