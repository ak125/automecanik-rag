---
entity_type: gamme
title: Sonde de refroidissement
slug: sonde-de-refroidissement
pg_id: 830
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
    Mesurer la temperature du liquide de refroidissement et informer le
    calculateur pour le pilotage moteur
  must_be_true:
    - mesurer
    - detecter
    - transmettre
  must_not_contain_concepts:
    - calorstat
    - thermostat
    - pompe a eau
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: vehicule_immobilise_ou_symptome_critique
    then: verification_urgente_piece_et_alimentation
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Indicateur temperature bloque froid maximum
    description: indicateur temperature bloque froid maximum
    risk_level: immobilisation
    evidence:
      - 'Observation: indicateur temperature bloque froid maximum'
      - Vérification visuelle ou auditive
  - id: S2
    label: Ventilateur qui tourne en permanence ou jamais
    description: ventilateur qui tourne en permanence ou jamais
    risk_level: confort
    evidence:
      - 'Observation: ventilateur qui tourne en permanence ou jamais'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit de ventilateur qui s emballe au demarrage
    description: bruit de ventilateur qui s emballe au demarrage
    risk_level: confort
    evidence:
      - 'Observation: bruit de ventilateur qui s emballe au demarrage'
      - Vérification visuelle ou auditive
  - id: S4
    label: Surconsommation et demarrage difficile a froid
    description: surconsommation et demarrage difficile a froid
    risk_level: confort
    evidence:
      - 'Observation: surconsommation et demarrage difficile a froid'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de liquide de refroidissement surchauffe
    description: odeur de liquide de refroidissement surchauffe
    risk_level: confort
    evidence:
      - 'Observation: odeur de liquide de refroidissement surchauffe'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 200 000 km sans controle du circuit
    description: plus de 200 000 km sans controle du circuit
    risk_level: confort
    evidence:
      - 'Observation: plus de 200 000 km sans controle du circuit'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Sonde de refroidissement - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la temperature du liquide de refroidissement et informer le calculateur pour le pilotage moteur

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Indicateur temperature bloque froid maximum**
  indicateur temperature bloque froid maximum

### 🟢 Autres Symptômes

- ventilateur qui tourne en permanence ou jamais
- bruit de ventilateur qui s emballe au demarrage
- surconsommation et demarrage difficile a froid
- odeur de liquide de refroidissement surchauffe
- plus de 200 000 km sans controle du circuit

## Procédure de Diagnostic

Pour diagnostiquer un problème de sonde de refroidissement:

1. **Inspection visuelle** - Examiner l'état du sonde de refroidissement
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le sonde de refroidissement peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- pompe-a-eau
- radiateur-de-refroidissement
- thermostat
- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon sonde de refroidissement, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "corrige la surchauffe"
