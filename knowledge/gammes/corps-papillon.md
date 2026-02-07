---
entity_type: gamme
title: Boîtier papillon
slug: corps-papillon
pg_id: 158
category: alimentation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Doser la quantite d'air admise dans le moteur en fonction de la position de
    l'accelerateur
  must_be_true:
    - doser
    - reguler
    - controler
  must_not_contain_concepts:
    - carburant
    - injection
    - injecteur
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
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Ralenti instable ou irregulier
    description: ralenti instable ou irregulier
    risk_level: confort
    evidence:
      - 'Observation: ralenti instable ou irregulier'
      - Vérification visuelle ou auditive
  - id: S2
    label: Accelerations saccadees ou a-coups
    description: accelerations saccadees ou a-coups
    risk_level: confort
    evidence:
      - 'Observation: accelerations saccadees ou a-coups'
      - Vérification visuelle ou auditive
  - id: S3
    label: Moteur qui cale au demarrage ou au ralenti
    description: moteur qui cale au demarrage ou au ralenti
    risk_level: immobilisation
    evidence:
      - 'Observation: moteur qui cale au demarrage ou au ralenti'
      - Vérification visuelle ou auditive
  - id: S4
    label: Sifflement d air au niveau de l admission
    description: sifflement d air au niveau de l admission
    risk_level: confort
    evidence:
      - 'Observation: sifflement d air au niveau de l admission'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur d essence melange trop riche
    description: odeur d essence melange trop riche
    risk_level: confort
    evidence:
      - 'Observation: odeur d essence melange trop riche'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 100 000 km sans nettoyage
    description: plus de 100 000 km sans nettoyage
    risk_level: confort
    evidence:
      - 'Observation: plus de 100 000 km sans nettoyage'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Boîtier papillon - Guide Diagnostic Complet

## Fonction et Rôle

Doser la quantite d'air admise dans le moteur en fonction de la position de l'accelerateur

**Actions principales:** doser, reguler, controler

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Moteur qui cale au demarrage ou au ralenti**
  moteur qui cale au demarrage ou au ralenti

### 🟢 Autres Symptômes

- ralenti instable ou irregulier
- accelerations saccadees ou a-coups
- sifflement d air au niveau de l admission
- odeur d essence melange trop riche
- plus de 100 000 km sans nettoyage

## Procédure de Diagnostic

Pour diagnostiquer un problème de boîtier papillon:

1. **Inspection visuelle** - Examiner l'état du boîtier papillon
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le boîtier papillon peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-position-papillon
- capteur-de-cognement
- capteur-temperature-d-air-admission
- corps-papillon
- injecteur
- valve-de-reglage-du-ralenti

## Critères de Compatibilité

Pour commander le bon boîtier papillon, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"
