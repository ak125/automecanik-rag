---
entity_type: gamme
title: Capteur de pression Common Rail
slug: capteur-de-pression-common-rail
pg_id: 3996
category: capteurs
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Mesurer la pression dans le circuit haute pression Common Rail et informer
    le calculateur
  must_be_true:
    - mesurer
    - detecter
    - transmettre
  must_not_contain_concepts:
    - pompe hp
    - injecteur
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
symptoms:
  - id: S1
    label: Demarrage difficile a froid
    description: demarrage difficile a froid
    risk_level: confort
    evidence:
      - 'Observation: demarrage difficile a froid'
      - Vérification visuelle ou auditive
  - id: S2
    label: Perte de puissance progressive
    description: perte de puissance progressive
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance progressive'
      - Vérification visuelle ou auditive
  - id: S3
    label: Voyant moteur avec code pression rail
    description: voyant moteur avec code pression rail
    risk_level: confort
    evidence:
      - 'Observation: voyant moteur avec code pression rail'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Capteur de pression Common Rail - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la pression dans le circuit haute pression Common Rail et informer le calculateur

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- demarrage difficile a froid
- perte de puissance progressive
- voyant moteur avec code pression rail

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur de pression common rail:

1. **Inspection visuelle** - Examiner l'état du capteur de pression common rail
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- pompe-a-haute-pression
- rampe-d-injection

## Critères de Compatibilité

Pour commander le bon capteur de pression common rail, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "corrige la panne"
