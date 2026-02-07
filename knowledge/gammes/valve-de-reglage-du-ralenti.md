---
entity_type: gamme
title: Valve de réglage du ralenti
slug: valve-de-reglage-du-ralenti
pg_id: 1298
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
    Reguler le debit d'air au ralenti pour maintenir un regime stable moteur
    chaud ou froid
  must_be_true:
    - reguler
    - ouvrir
    - fermer
  must_not_contain_concepts:
    - capteur
    - sonde
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
symptoms:
  - id: S1
    label: Ralenti instable ou irregulier
    description: ralenti instable ou irregulier
    risk_level: confort
    evidence:
      - 'Observation: ralenti instable ou irregulier'
      - Vérification visuelle ou auditive
  - id: S2
    label: Regime ralenti trop haut ou trop bas
    description: regime ralenti trop haut ou trop bas
    risk_level: confort
    evidence:
      - 'Observation: regime ralenti trop haut ou trop bas'
      - Vérification visuelle ou auditive
  - id: S3
    label: Moteur qui cale au ralenti ou au feu rouge
    description: moteur qui cale au ralenti ou au feu rouge
    risk_level: immobilisation
    evidence:
      - 'Observation: moteur qui cale au ralenti ou au feu rouge'
      - Vérification visuelle ou auditive
  - id: S4
    label: Sifflement ou bruit d aspirtion d air anormal
    description: sifflement ou bruit d aspirtion d air anormal
    risk_level: confort
    evidence:
      - 'Observation: sifflement ou bruit d aspirtion d air anormal'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur d essence au ralenti melange trop riche
    description: odeur d essence au ralenti melange trop riche
    risk_level: confort
    evidence:
      - 'Observation: odeur d essence au ralenti melange trop riche'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus nettoyage boitier papillon
    description: plus nettoyage boitier papillon
    risk_level: confort
    evidence:
      - 'Observation: plus nettoyage boitier papillon'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Valve de réglage du ralenti - Guide Diagnostic Complet

## Fonction et Rôle

Reguler le debit d'air au ralenti pour maintenir un regime stable moteur chaud ou froid

**Actions principales:** reguler, ouvrir, fermer, doser

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Moteur qui cale au ralenti ou au feu rouge**
  moteur qui cale au ralenti ou au feu rouge

### 🟢 Autres Symptômes

- ralenti instable ou irregulier
- regime ralenti trop haut ou trop bas
- sifflement ou bruit d aspirtion d air anormal
- odeur d essence au ralenti melange trop riche
- plus nettoyage boitier papillon

## Procédure de Diagnostic

Pour diagnostiquer un problème de valve de réglage du ralenti:

1. **Inspection visuelle** - Examiner l'état du valve de réglage du ralenti
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le valve de réglage du ralenti peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes

## Pièces Associées

Lors du remplacement, vérifier également:

- corps-papillon
- filtre-a-air

## Critères de Compatibilité

Pour commander le bon valve de réglage du ralenti, vous devez connaître:

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
