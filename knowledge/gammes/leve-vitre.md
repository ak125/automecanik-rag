---
entity_type: gamme
title: Lève-vitre
slug: leve-vitre
pg_id: 1561
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Monte et descend la vitre de la portière
  must_be_true:
    - lever
    - descendre
    - actionner
  must_not_contain_concepts:
    - injection
    - freinage
    - distribution
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
    label: Vitre qui ne monte ou ne descend plus
    description: vitre qui ne monte ou ne descend plus
    risk_level: confort
    evidence:
      - 'Observation: vitre qui ne monte ou ne descend plus'
      - Vérification visuelle ou auditive
  - id: S2
    label: Vitre tres lente arrete cours
    description: vitre tres lente arrete cours
    risk_level: confort
    evidence:
      - 'Observation: vitre tres lente arrete cours'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit de moteur mais vitre immobile cable casse
    description: bruit de moteur mais vitre immobile cable casse
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit de moteur mais vitre immobile cable casse'
      - Vérification visuelle ou auditive
  - id: S4
    label: Vitre qui descend toute seule mecanisme use
    description: vitre qui descend toute seule mecanisme use
    risk_level: confort
    evidence:
      - 'Observation: vitre qui descend toute seule mecanisme use'
      - Vérification visuelle ou auditive
  - id: S5
    label: Grincement ou bruit anormal a la montee descente
    description: grincement ou bruit anormal a la montee descente
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: grincement ou bruit anormal a la montee descente'
      - Vérification visuelle ou auditive
  - id: S6
    label: Vitre de travers ou mal guidee dans le rail
    description: vitre de travers ou mal guidee dans le rail
    risk_level: confort
    evidence:
      - 'Observation: vitre de travers ou mal guidee dans le rail'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Lève-vitre - Guide Diagnostic Complet

## Fonction et Rôle

Monte et descend la vitre de la portière

**Actions principales:** lever, descendre, actionner

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de moteur mais vitre immobile cable casse**
  bruit de moteur mais vitre immobile cable casse
- **Grincement ou bruit anormal a la montee descente**
  grincement ou bruit anormal a la montee descente

### 🟢 Autres Symptômes

- vitre qui ne monte ou ne descend plus
- vitre tres lente arrete cours
- vitre qui descend toute seule mecanisme use
- vitre de travers ou mal guidee dans le rail

## Procédure de Diagnostic

Pour diagnostiquer un problème de lève-vitre:

1. **Inspection visuelle** - Examiner l'état du lève-vitre
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- moteur-leve-vitre
- interrupteur-leve-vitre

## Critères de Compatibilité

Pour commander le bon lève-vitre, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "fonctionnement garanti"
