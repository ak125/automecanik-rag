---
entity_type: gamme
title: Cardan
slug: cardan
pg_id: 13
category: transmission
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Transmet le couple moteur aux roues tout en permettant les mouvements de
    suspension
  must_be_true:
    - transmettre
    - entrainer
  must_not_contain_concepts:
    - injection
    - freinage
    - climatisation
    - allumage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: vibrations_anormales
    then: verifier_equilibrage_et_fixations
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Claquement braquant accelerant marche arriere
    description: claquement braquant accelerant marche arriere
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement braquant accelerant marche arriere'
      - Vérification visuelle ou auditive
  - id: S2
    label: Vibrations ressenties vitesse constante
    description: vibrations ressenties vitesse constante
    risk_level: confort
    evidence:
      - 'Observation: vibrations ressenties vitesse constante'
      - Vérification visuelle ou auditive
  - id: S3
    label: Graisse noire visible jante passage
    description: graisse noire visible jante passage
    risk_level: confort
    evidence:
      - 'Observation: graisse noire visible jante passage'
      - Vérification visuelle ou auditive
  - id: S4
    label: Soufflet de cardan dechire ou fendu visible
    description: soufflet de cardan dechire ou fendu visible
    risk_level: confort
    evidence:
      - 'Observation: soufflet de cardan dechire ou fendu visible'
      - Vérification visuelle ou auditive
  - id: S5
    label: Bruit roulement change selon angle
    description: bruit roulement change selon angle
    risk_level: confort
    evidence:
      - 'Observation: bruit roulement change selon angle'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 150 000 km sans verification des soufflets
    description: plus de 150 000 km sans verification des soufflets
    risk_level: confort
    evidence:
      - 'Observation: plus de 150 000 km sans verification des soufflets'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Cardan - Guide Diagnostic Complet

## Fonction et Rôle

Transmet le couple moteur aux roues tout en permettant les mouvements de suspension

**Actions principales:** transmettre, entrainer

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement braquant accelerant marche arriere**
  claquement braquant accelerant marche arriere

### 🟢 Autres Symptômes

- vibrations ressenties vitesse constante
- graisse noire visible jante passage
- soufflet de cardan dechire ou fendu visible
- bruit roulement change selon angle
- plus de 150 000 km sans verification des soufflets

## Procédure de Diagnostic

Pour diagnostiquer un problème de cardan:

1. **Inspection visuelle** - Examiner l'état du cardan
2. **Test dynamique** - Vérifier les bruits en roulant
3. **Contrôle du jeu** - Examiner l'usure des articulations
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- bague-d-etancheite-cardan
- soufflet-de-cardan

## Critères de Compatibilité

Pour commander le bon cardan, vous devez connaître:

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
