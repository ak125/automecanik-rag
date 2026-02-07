---
entity_type: gamme
title: Rotule de direction
slug: rotule-de-direction
pg_id: 2066
category: direction
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Articuler la barre de direction et la fusee - Permet le braquage. NE
    SUPPORTE PAS LA CHARGE!
  must_be_true:
    - orienter
    - transmettre le mouvement
    - articuler
  must_not_contain_concepts:
    - suspension
    - bras
    - triangle
    - charge
    - poids
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Jeu perceptible dans le volant
    description: jeu perceptible dans le volant
    risk_level: confort
    evidence:
      - 'Observation: jeu perceptible dans le volant'
      - Vérification visuelle ou auditive
  - id: S2
    label: Claquements en tournant a basse vitesse
    description: claquements en tournant a basse vitesse
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquements en tournant a basse vitesse'
      - Vérification visuelle ou auditive
  - id: S3
    label: Direction imprecise ou floue
    description: direction imprecise ou floue
    risk_level: securite
    evidence:
      - 'Observation: direction imprecise ou floue'
      - Vérification visuelle ou auditive
  - id: S4
    label: Usure asymetrique des pneus avant
    description: usure asymetrique des pneus avant
    risk_level: securite
    evidence:
      - 'Observation: usure asymetrique des pneus avant'
      - Vérification visuelle ou auditive
  - id: S5
    label: Soufflet de rotule dechire ou graisse visible
    description: soufflet de rotule dechire ou graisse visible
    risk_level: confort
    evidence:
      - 'Observation: soufflet de rotule dechire ou graisse visible'
      - Vérification visuelle ou auditive
  - id: S6
    label: Controle technique refuse pour jeu aux trains
    description: controle technique refuse pour jeu aux trains
    risk_level: confort
    evidence:
      - 'Observation: controle technique refuse pour jeu aux trains'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Rotule de direction - Guide Diagnostic Complet

## Fonction et Rôle

Articuler la barre de direction et la fusee - Permet le braquage. NE SUPPORTE PAS LA CHARGE!

**Actions principales:** orienter, transmettre le mouvement, articuler, permettre le braquage, guider

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquements en tournant a basse vitesse**
  claquements en tournant a basse vitesse

### 🟡 Symptômes de Sécurité

- **Direction imprecise ou floue**
  direction imprecise ou floue
- **Usure asymetrique des pneus avant**
  usure asymetrique des pneus avant

### 🟢 Autres Symptômes

- jeu perceptible dans le volant
- soufflet de rotule dechire ou graisse visible
- controle technique refuse pour jeu aux trains

## Procédure de Diagnostic

Pour diagnostiquer un problème de rotule de direction:

1. **Inspection visuelle** - Examiner l'état du rotule de direction
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- amortisseur
- barre-de-direction
- bras-de-suspension
- cremailliere-de-direction
- pompe-de-direction-assistee
- rotule-de-suspension
- soufflet-de-direction

## Critères de Compatibilité

Pour commander le bon rotule de direction, vous devez connaître:

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
