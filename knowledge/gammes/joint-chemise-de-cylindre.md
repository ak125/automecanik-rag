---
entity_type: gamme
title: Joint chemise de cylindre
slug: joint-chemise-de-cylindre
pg_id: 128
category: moteur
subcategory: joints
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Assurer l'etancheite entre la chemise et le bloc moteur
  must_be_true:
    - assurer l'etancheite
    - isoler
  must_not_contain_concepts:
    - freinage
    - climatisation
    - direction
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
symptoms:
  - id: S1
    label: Melange eau-huile mayonnaise
    description: melange eau-huile mayonnaise
    risk_level: confort
    evidence:
      - 'Observation: melange eau-huile mayonnaise'
      - Vérification visuelle ou auditive
  - id: S2
    label: Surchauffe moteur sans fuite visible
    description: surchauffe moteur sans fuite visible
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: surchauffe moteur sans fuite visible'
      - Vérification visuelle ou auditive
  - id: S3
    label: Perte de compression sur un cylindre
    description: perte de compression sur un cylindre
    risk_level: confort
    evidence:
      - 'Observation: perte de compression sur un cylindre'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Joint chemise de cylindre - Guide Diagnostic Complet

## Fonction et Rôle

Assurer l'etancheite entre la chemise et le bloc moteur

**Actions principales:** assurer l'etancheite, isoler

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Surchauffe moteur sans fuite visible**
  surchauffe moteur sans fuite visible

### 🟢 Autres Symptômes

- melange eau-huile mayonnaise
- perte de compression sur un cylindre

## Procédure de Diagnostic

Pour diagnostiquer un problème de joint chemise de cylindre:

1. **Inspection visuelle** - Examiner l'état du joint chemise de cylindre
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- chemise-de-cylindre
- joint-de-culasse

## Critères de Compatibilité

Pour commander le bon joint chemise de cylindre, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"
