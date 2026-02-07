---
entity_type: gamme
title: Filtre de boîte auto
slug: filtre-de-boite-auto
pg_id: 416
category: filtration
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Filtrer l'huile de la boite automatique
  must_be_true:
    - filtrer
    - retenir
    - purifier
  must_not_contain_concepts:
    - injection
    - freinage
    - direction
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
  - if: vibrations_anormales
    then: verifier_equilibrage_et_fixations
symptoms:
  - id: S1
    label: Passages de vitesses brutaux ou tardifs
    description: passages de vitesses brutaux ou tardifs
    risk_level: confort
    evidence:
      - 'Observation: passages de vitesses brutaux ou tardifs'
      - Vérification visuelle ou auditive
  - id: S2
    label: Vibrations lors des changements de rapport
    description: vibrations lors des changements de rapport
    risk_level: confort
    evidence:
      - 'Observation: vibrations lors des changements de rapport'
      - Vérification visuelle ou auditive
  - id: S3
    label: Boite qui patine sous charge
    description: boite qui patine sous charge
    risk_level: confort
    evidence:
      - 'Observation: boite qui patine sous charge'
      - Vérification visuelle ou auditive
  - id: S4
    label: Huile atf brune ou odeur brule
    description: huile atf brune ou odeur brule
    risk_level: confort
    evidence:
      - 'Observation: huile atf brune ou odeur brule'
      - Vérification visuelle ou auditive
  - id: S5
    label: Voyant temperature boite
    description: voyant temperature boite
    risk_level: confort
    evidence:
      - 'Observation: voyant temperature boite'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Filtre de boîte auto - Guide Diagnostic Complet

## Fonction et Rôle

Filtrer l'huile de la boite automatique

**Actions principales:** filtrer, retenir, purifier

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- passages de vitesses brutaux ou tardifs
- vibrations lors des changements de rapport
- boite qui patine sous charge
- huile atf brune ou odeur brule
- voyant temperature boite

## Procédure de Diagnostic

Pour diagnostiquer un problème de filtre de boîte auto:

1. **Inspection visuelle** - Examiner l'état du filtre de boîte auto
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- boite-automatique
- huile-bva

## Critères de Compatibilité

Pour commander le bon filtre de boîte auto, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "filtration parfaite"
