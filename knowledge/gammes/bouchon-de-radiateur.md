---
entity_type: gamme
title: Bouchon de radiateur
slug: bouchon-de-radiateur
pg_id: 548
category: refroidissement
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Fermer le radiateur et reguler la pression du circuit
  must_be_true:
    - fermer
    - reguler
    - proteger
  must_not_contain_concepts:
    - injection
    - freinage
    - embrayage
    - distribution
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
    label: Fuite de liquide par le bouchon
    description: fuite de liquide par le bouchon
    risk_level: confort
    evidence:
      - 'Observation: fuite de liquide par le bouchon'
      - Vérification visuelle ou auditive
  - id: S2
    label: Surchauffe moteur sans fuite visible
    description: surchauffe moteur sans fuite visible
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: surchauffe moteur sans fuite visible'
      - Vérification visuelle ou auditive
  - id: S3
    label: Pression excessive dans le circuit
    description: pression excessive dans le circuit
    risk_level: confort
    evidence:
      - 'Observation: pression excessive dans le circuit'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Bouchon de radiateur - Guide Diagnostic Complet

## Fonction et Rôle

Fermer le radiateur et reguler la pression du circuit

**Actions principales:** fermer, reguler, proteger

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Surchauffe moteur sans fuite visible**
  surchauffe moteur sans fuite visible

### 🟢 Autres Symptômes

- fuite de liquide par le bouchon
- pression excessive dans le circuit

## Procédure de Diagnostic

Pour diagnostiquer un problème de bouchon de radiateur:

1. **Inspection visuelle** - Examiner l'état du bouchon de radiateur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- radiateur
- durite-de-refroidissement

## Critères de Compatibilité

Pour commander le bon bouchon de radiateur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidissement optimal"
