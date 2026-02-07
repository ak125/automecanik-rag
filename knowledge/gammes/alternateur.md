---
entity_type: gamme
title: Alternateur
slug: alternateur
pg_id: 4
category: electrique
subcategory: charge
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Recharger la batterie et alimenter les equipements electriques du vehicule
    moteur tournant
  must_be_true:
    - recharger
    - alimenter
    - fournir du courant
  must_not_contain_concepts:
    - demarrage
    - demarreur
    - lancer le moteur
    - rotation initiale
    - neiman
    - universel
    - tous modèles
    - adaptable tous
  confusion_with:
    demarreur:
      key_difference: >-
        Alternateur = recharge batterie (moteur tournant), Démarreur = lance le
        moteur (au démarrage)
    batterie:
      key_difference: >-
        Alternateur recharge la batterie, si batterie HS l'alternateur ne peut
        compenser
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Voyant batterie allume moteur tournant
    description: voyant batterie allume moteur tournant
    risk_level: confort
    evidence:
      - 'Observation: voyant batterie allume moteur tournant'
      - Vérification visuelle ou auditive
  - id: S2
    label: Batterie qui se decharge malgre les trajets
    description: batterie qui se decharge malgre les trajets
    risk_level: confort
    evidence:
      - 'Observation: batterie qui se decharge malgre les trajets'
      - Vérification visuelle ou auditive
  - id: S3
    label: Phares qui faiblissent ou clignotent
    description: phares qui faiblissent ou clignotent
    risk_level: confort
    evidence:
      - 'Observation: phares qui faiblissent ou clignotent'
      - Vérification visuelle ou auditive
  - id: S4
    label: Sifflement de la courroie d accessoire
    description: sifflement de la courroie d accessoire
    risk_level: confort
    evidence:
      - 'Observation: sifflement de la courroie d accessoire'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de courroie brulee ou d electrique
    description: odeur de courroie brulee ou d electrique
    risk_level: confort
    evidence:
      - 'Observation: odeur de courroie brulee ou d electrique'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 150 000 km ou tension de charge basse
    description: plus de 150 000 km ou tension de charge basse
    risk_level: confort
    evidence:
      - 'Observation: plus de 150 000 km ou tension de charge basse'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - adaptable tous
---
# Alternateur - Guide Diagnostic Complet

## Fonction et Rôle

Recharger la batterie et alimenter les equipements electriques du vehicule moteur tournant

**Actions principales:** recharger, alimenter, fournir du courant, maintenir la charge, produire de lelectricite

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant batterie allume moteur tournant
- batterie qui se decharge malgre les trajets
- phares qui faiblissent ou clignotent
- sifflement de la courroie d accessoire
- odeur de courroie brulee ou d electrique
- plus de 150 000 km ou tension de charge basse

## Procédure de Diagnostic

Pour diagnostiquer un problème de alternateur:

1. **Inspection visuelle** - Examiner l'état du alternateur
2. **Test électrique** - Vérifier la tension et les connexions
3. **Lecture codes défaut** - Scanner OBD si voyant allumé
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-d-accessoire
- demarreur
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- poulie-d-alternateur
- poulie-vilebrequin

## ⚠️ Ne Pas Confondre Avec

### demarreur
**Distinction:** Alternateur = recharge batterie (moteur tournant), Démarreur = lance le moteur (au démarrage)

### batterie
**Distinction:** Alternateur recharge la batterie, si batterie HS l'alternateur ne peut compenser

## Critères de Compatibilité

Pour commander le bon alternateur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Motorisation** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "zéro panne électrique"
- ❌ "homologué CT"
- ❌ "sécurité garantie"
