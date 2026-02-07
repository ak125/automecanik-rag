---
entity_type: gamme
title: Capteur ABS
slug: capteur-abs
pg_id: 412
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
    Mesurer la vitesse de rotation de chaque roue et transmettre l'information
    au calculateur ABS
  must_be_true:
    - mesurer
    - detecter
    - transmettre
  must_not_contain_concepts:
    - electrovanne
    - modulateur
    - pompe abs
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
    label: Voyant abs allume au tableau de bord
    description: voyant abs allume au tableau de bord
    risk_level: securite
    evidence:
      - 'Observation: voyant abs allume au tableau de bord'
      - Vérification visuelle ou auditive
  - id: S2
    label: Code defaut specifique a une roue
    description: code defaut specifique a une roue
    risk_level: confort
    evidence:
      - 'Observation: code defaut specifique a une roue'
      - Vérification visuelle ou auditive
  - id: S3
    label: Capteur visible endommage ou couvert de crasse
    description: capteur visible endommage ou couvert de crasse
    risk_level: confort
    evidence:
      - 'Observation: capteur visible endommage ou couvert de crasse'
      - Vérification visuelle ou auditive
  - id: S4
    label: Cable du capteur coupe ou denude
    description: cable du capteur coupe ou denude
    risk_level: confort
    evidence:
      - 'Observation: cable du capteur coupe ou denude'
      - Vérification visuelle ou auditive
  - id: S5
    label: Abs qui se declenche a basse vitesse sans raison
    description: abs qui se declenche a basse vitesse sans raison
    risk_level: securite
    evidence:
      - 'Observation: abs qui se declenche a basse vitesse sans raison'
      - Vérification visuelle ou auditive
  - id: S6
    label: Bruit anormal lors du fonctionnement abs
    description: bruit anormal lors du fonctionnement abs
    risk_level: securite
    evidence:
      - 'Observation: bruit anormal lors du fonctionnement abs'
      - Vérification visuelle ou auditive
  - id: S7
    label: Freinage desequilibre avec abs actif
    description: freinage desequilibre avec abs actif
    risk_level: securite
    evidence:
      - 'Observation: freinage desequilibre avec abs actif'
      - Vérification visuelle ou auditive
  - id: S8
    label: Plus de 150 000 km sans verification capteurs
    description: plus de 150 000 km sans verification capteurs
    risk_level: confort
    evidence:
      - 'Observation: plus de 150 000 km sans verification capteurs'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Capteur ABS - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la vitesse de rotation de chaque roue et transmettre l'information au calculateur ABS

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Voyant abs allume au tableau de bord**
  voyant abs allume au tableau de bord
- **Abs qui se declenche a basse vitesse sans raison**
  abs qui se declenche a basse vitesse sans raison
- **Bruit anormal lors du fonctionnement abs**
  bruit anormal lors du fonctionnement abs
- **Freinage desequilibre avec abs actif**
  freinage desequilibre avec abs actif

### 🟢 Autres Symptômes

- code defaut specifique a une roue
- capteur visible endommage ou couvert de crasse
- cable du capteur coupe ou denude
- plus de 150 000 km sans verification capteurs

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur abs:

1. **Inspection visuelle** - Examiner l'état du capteur abs
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- agregat-de-freinage
- cable-de-frein-a-main
- disque-de-frein
- etrier-de-frein
- kit-de-freins-arriere
- machoires-de-frein
- plaquette-de-frein
- roulement-de-roue

## Critères de Compatibilité

Pour commander le bon capteur abs, vous devez connaître:

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
