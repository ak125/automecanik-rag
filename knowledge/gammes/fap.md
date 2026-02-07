---
entity_type: gamme
title: FAP
slug: fap
pg_id: 1256
category: echappement
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Filtre et retient les particules fines des gaz d'échappement diesel
  must_be_true:
    - filtrer
    - retenir
    - regenerer
  must_not_contain_concepts:
    - catalyseur
    - pot catalytique
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Voyant filtre particules allume tableau
    description: voyant filtre particules allume tableau
    risk_level: confort
    evidence:
      - 'Observation: voyant filtre particules allume tableau'
      - Vérification visuelle ou auditive
  - id: S2
    label: Perte de puissance importante mode degrade
    description: perte de puissance importante mode degrade
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance importante mode degrade'
      - Vérification visuelle ou auditive
  - id: S3
    label: Regenerations frequentes odeur de brule
    description: regenerations frequentes odeur de brule
    risk_level: confort
    evidence:
      - 'Observation: regenerations frequentes odeur de brule'
      - Vérification visuelle ou auditive
  - id: S4
    label: Fumee noire excessive a l acceleration
    description: fumee noire excessive a l acceleration
    risk_level: confort
    evidence:
      - 'Observation: fumee noire excessive a l acceleration'
      - Vérification visuelle ou auditive
  - id: S5
    label: Surconsommation de carburant anormale
    description: surconsommation de carburant anormale
    risk_level: confort
    evidence:
      - 'Observation: surconsommation de carburant anormale'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 150 000 km en conduite urbaine
    description: plus de 150 000 km en conduite urbaine
    risk_level: confort
    evidence:
      - 'Observation: plus de 150 000 km en conduite urbaine'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# FAP - Guide Diagnostic Complet

## Fonction et Rôle

Filtre et retient les particules fines des gaz d'échappement diesel

**Actions principales:** filtrer, retenir, regenerer, stocker

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant filtre particules allume tableau
- perte de puissance importante mode degrade
- regenerations frequentes odeur de brule
- fumee noire excessive a l acceleration
- surconsommation de carburant anormale
- plus de 150 000 km en conduite urbaine

## Procédure de Diagnostic

Pour diagnostiquer un problème de fap:

1. **Inspection visuelle** - Examiner l'état du fap
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-temperature-d-air-admission
- catalyseur
- sonde-lambda
- tube-d-echappement
- vanne-egr

## Critères de Compatibilité

Pour commander le bon fap, vous devez connaître:

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
