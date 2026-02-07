---
entity_type: gamme
title: Avertisseur sonore
slug: avertisseur-sonore
pg_id: 297
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Émet un signal sonore pour avertir les autres usagers
  must_be_true:
    - avertir
    - signaler
    - emettre
  must_not_contain_concepts:
    - alarme
    - antivol
    - freins
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_general_detecte
    then: inspection_visuelle_et_test_fonctionnel
symptoms:
  - id: S1
    label: Klaxon silencieux ou tres faible
    description: klaxon silencieux ou tres faible
    risk_level: confort
    evidence:
      - 'Observation: klaxon silencieux ou tres faible'
      - Vérification visuelle ou auditive
  - id: S2
    label: Son intermittent ou coupe
    description: son intermittent ou coupe
    risk_level: confort
    evidence:
      - 'Observation: son intermittent ou coupe'
      - Vérification visuelle ou auditive
  - id: S3
    label: Klaxon qui fonctionne une fois sur deux
    description: klaxon qui fonctionne une fois sur deux
    risk_level: confort
    evidence:
      - 'Observation: klaxon qui fonctionne une fois sur deux'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Avertisseur sonore - Guide Diagnostic Complet

## Fonction et Rôle

Émet un signal sonore pour avertir les autres usagers

**Actions principales:** avertir, signaler, emettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- klaxon silencieux ou tres faible
- son intermittent ou coupe
- klaxon qui fonctionne une fois sur deux

## Procédure de Diagnostic

Pour diagnostiquer un problème de avertisseur sonore:

1. **Inspection visuelle** - Examiner l'état du avertisseur sonore
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- moteur-d-essuie-glace
- tringlerie-d-essuie-glace
- bras-d-essuie-glace

## Critères de Compatibilité

Pour commander le bon avertisseur sonore, vous devez connaître:

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
