---
entity_type: gamme
title: Témoin d'usure
slug: temoin-d-usure
pg_id: 407
category: freinage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Signale l'usure des plaquettes de frein
  must_be_true:
    - signaler
    - alerter
    - indiquer
  must_not_contain_concepts:
    - injection
    - climatisation
    - embrayage
    - distribution
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Voyant usure frein allume au tableau de bord
    description: voyant usure frein allume au tableau de bord
    risk_level: securite
    evidence:
      - 'Observation: voyant usure frein allume au tableau de bord'
      - Vérification visuelle ou auditive
  - id: S2
    label: Sifflement metallique freinage temoin acoustique
    description: sifflement metallique freinage temoin acoustique
    risk_level: securite
    evidence:
      - 'Observation: sifflement metallique freinage temoin acoustique'
      - Vérification visuelle ou auditive
  - id: S3
    label: Voyant allume en permanence meme plaquettes neuves
    description: voyant allume en permanence meme plaquettes neuves
    risk_level: confort
    evidence:
      - 'Observation: voyant allume en permanence meme plaquettes neuves'
      - Vérification visuelle ou auditive
  - id: S4
    label: Connecteur du temoin debranche ou coupe
    description: connecteur du temoin debranche ou coupe
    risk_level: confort
    evidence:
      - 'Observation: connecteur du temoin debranche ou coupe'
      - Vérification visuelle ou auditive
  - id: S5
    label: Fil du temoin fondu par frottement sur disque
    description: fil du temoin fondu par frottement sur disque
    risk_level: confort
    evidence:
      - 'Observation: fil du temoin fondu par frottement sur disque'
      - Vérification visuelle ou auditive
  - id: S6
    label: Freinage degrade malgre absence de voyant
    description: freinage degrade malgre absence de voyant
    risk_level: securite
    evidence:
      - 'Observation: freinage degrade malgre absence de voyant'
      - Vérification visuelle ou auditive
  - id: S7
    label: Odeur de brule si frottement du fil
    description: odeur de brule si frottement du fil
    risk_level: confort
    evidence:
      - 'Observation: odeur de brule si frottement du fil'
      - Vérification visuelle ou auditive
  - id: S8
    label: Plus de 30 000 km avec temoin non verifie
    description: plus de 30 000 km avec temoin non verifie
    risk_level: confort
    evidence:
      - 'Observation: plus de 30 000 km avec temoin non verifie'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Témoin d'usure - Guide Diagnostic Complet

## Fonction et Rôle

Signale l'usure des plaquettes de frein

**Actions principales:** signaler, alerter, indiquer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Voyant usure frein allume au tableau de bord**
  voyant usure frein allume au tableau de bord
- **Sifflement metallique freinage temoin acoustique**
  sifflement metallique freinage temoin acoustique
- **Freinage degrade malgre absence de voyant**
  freinage degrade malgre absence de voyant

### 🟢 Autres Symptômes

- voyant allume en permanence meme plaquettes neuves
- connecteur du temoin debranche ou coupe
- fil du temoin fondu par frottement sur disque
- odeur de brule si frottement du fil
- plus de 30 000 km avec temoin non verifie

## Procédure de Diagnostic

Pour diagnostiquer un problème de témoin d'usure:

1. **Inspection visuelle** - Examiner l'état du témoin d'usure
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
- plaquette-de-frein
- servo-frein

## Critères de Compatibilité

Pour commander le bon témoin d'usure, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "améliore le freinage"
