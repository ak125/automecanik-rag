---
entity_type: gamme
title: Plaquette de frein
slug: plaquette-de-frein
pg_id: 402
category: freinage
subcategory: plaquettes
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Creer la friction contre le disque pour ralentir le vehicule
  must_be_true:
    - freiner
    - creer la friction
    - ralentir le vehicule
  must_not_contain_concepts:
    - tambour
    - machoire
    - hydraulique
    - pression
    - universel
    - tous véhicules
    - adaptable tous
  confusion_with:
    disque-de-frein:
      key_difference: >-
        Plaquettes = garnitures qui s'usent, Disques = surfaces de friction à
        contrôler
    machoire-de-frein:
      key_difference: 'Plaquettes = freins à disque, Mâchoires = freins à tambour'
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Sifflement metallique au freinage temoin d usure
    description: sifflement metallique au freinage temoin d usure
    risk_level: securite
    evidence:
      - 'Observation: sifflement metallique au freinage temoin d usure'
      - Vérification visuelle ou auditive
  - id: S2
    label: Voyant frein allume au tableau de bord
    description: voyant frein allume au tableau de bord
    risk_level: securite
    evidence:
      - 'Observation: voyant frein allume au tableau de bord'
      - Vérification visuelle ou auditive
  - id: S3
    label: Epaisseur visible inferieure travers jante
    description: epaisseur visible inferieure travers jante
    risk_level: confort
    evidence:
      - 'Observation: epaisseur visible inferieure travers jante'
      - Vérification visuelle ou auditive
  - id: S4
    label: Distances de freinage allongees
    description: distances de freinage allongees
    risk_level: securite
    evidence:
      - 'Observation: distances de freinage allongees'
      - Vérification visuelle ou auditive
  - id: S5
    label: Pedale de frein qui s enfonce plus que d habitude
    description: pedale de frein qui s enfonce plus que d habitude
    risk_level: securite
    evidence:
      - 'Observation: pedale de frein qui s enfonce plus que d habitude'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 30 000 km depuis le dernier changement
    description: plus de 30 000 km depuis le dernier changement
    risk_level: confort
    evidence:
      - 'Observation: plus de 30 000 km depuis le dernier changement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous véhicules
    - adaptable tous
---
# Plaquette de frein - Guide Diagnostic Complet

## Fonction et Rôle

Creer la friction contre le disque pour ralentir le vehicule

**Actions principales:** freiner, creer la friction, ralentir le vehicule, presser le disque, s'user progressivement

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Sifflement metallique au freinage temoin d usure**
  sifflement metallique au freinage temoin d usure
- **Voyant frein allume au tableau de bord**
  voyant frein allume au tableau de bord
- **Distances de freinage allongees**
  distances de freinage allongees
- **Pedale de frein qui s enfonce plus que d habitude**
  pedale de frein qui s enfonce plus que d habitude

### 🟢 Autres Symptômes

- epaisseur visible inferieure travers jante
- plus de 30 000 km depuis le dernier changement

## Procédure de Diagnostic

Pour diagnostiquer un problème de plaquette de frein:

1. **Inspection visuelle** - Examiner l'état du plaquette de frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- cable-de-frein-a-main
- capteur-abs
- disque-de-frein
- etrier-de-frein
- interrupteur-des-feux-de-freins
- servo-frein
- temoin-d-usure

## ⚠️ Ne Pas Confondre Avec

### disque-de-frein
**Distinction:** Plaquettes = garnitures qui s'usent, Disques = surfaces de friction à contrôler

### machoire-de-frein
**Distinction:** Plaquettes = freins à disque, Mâchoires = freins à tambour

## Critères de Compatibilité

Pour commander le bon plaquette de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule
- **Position** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "sécurité garantie"
- ❌ "arrêt immédiat"
- ❌ "zéro accident"
- ❌ "garanti CT"
