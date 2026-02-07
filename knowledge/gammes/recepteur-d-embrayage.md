---
entity_type: gamme
title: Récepteur d'embrayage
slug: recepteur-d-embrayage
pg_id: 620
category: embrayage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Recevoir la pression hydraulique et actionner la butée ou la fourchette
  must_be_true:
    - recevoir la pression
    - actionner la butée
    - pousser la fourchette
  must_not_contain_concepts:
    - disque
    - volant
    - couple
    - câble
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
    label: Pedale d embrayage molle ou spongieuse
    description: pedale d embrayage molle ou spongieuse
    risk_level: confort
    evidence:
      - 'Observation: pedale d embrayage molle ou spongieuse'
      - Vérification visuelle ou auditive
  - id: S2
    label: Fuite de liquide visible sous la boite de vitesses
    description: fuite de liquide visible sous la boite de vitesses
    risk_level: confort
    evidence:
      - 'Observation: fuite de liquide visible sous la boite de vitesses'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit de grincement au niveau de la fourchette
    description: bruit de grincement au niveau de la fourchette
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit de grincement au niveau de la fourchette'
      - Vérification visuelle ou auditive
  - id: S4
    label: Odeur de liquide de frein brule sous la voiture
    description: odeur de liquide de frein brule sous la voiture
    risk_level: securite
    evidence:
      - 'Observation: odeur de liquide de frein brule sous la voiture'
      - Vérification visuelle ou auditive
  - id: S5
    label: Embrayage qui ne debraye plus piston bloque
    description: embrayage qui ne debraye plus piston bloque
    risk_level: immobilisation
    evidence:
      - 'Observation: embrayage qui ne debraye plus piston bloque'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 150 000 km sans verification du circuit
    description: plus de 150 000 km sans verification du circuit
    risk_level: confort
    evidence:
      - 'Observation: plus de 150 000 km sans verification du circuit'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Récepteur d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Recevoir la pression hydraulique et actionner la butée ou la fourchette

**Actions principales:** recevoir la pression, actionner la butée, pousser la fourchette, convertir

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Embrayage qui ne debraye plus piston bloque**
  embrayage qui ne debraye plus piston bloque

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de grincement au niveau de la fourchette**
  bruit de grincement au niveau de la fourchette

### 🟡 Symptômes de Sécurité

- **Odeur de liquide de frein brule sous la voiture**
  odeur de liquide de frein brule sous la voiture

### 🟢 Autres Symptômes

- pedale d embrayage molle ou spongieuse
- fuite de liquide visible sous la boite de vitesses
- plus de 150 000 km sans verification du circuit

## Procédure de Diagnostic

Pour diagnostiquer un problème de récepteur d'embrayage:

1. **Inspection visuelle** - Examiner l'état du récepteur d'embrayage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le récepteur d'embrayage peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- butee-d-embrayage
- emetteur-d-embrayage
- kit-d-embrayage
- volant-moteur

## Critères de Compatibilité

Pour commander le bon récepteur d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "action parfaite"
