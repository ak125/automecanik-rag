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
  - if: symptome_voyant-batterie-allume-moteur-tournant
    then: verifier_piece
  - if: symptome_batterie-qui-se-decharge-malgre-les
    then: diagnostic_approfondi
  - if: symptome_phares-qui-faiblissent-ou-clignotent
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Voyant batterie allume moteur tournant
    description: voyant batterie allume moteur tournant
    risk_level: confort
    evidence:
      - 'Observation: voyant batterie allume moteur tournant'
      - Vérification visuelle ou auditive
  - id: S2
    label: Batterie qui se decharge malgre les
    description: batterie qui se decharge malgre les trajets
    risk_level: confort
    evidence:
      - 'Observation: batterie qui se decharge malgre les'
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
    label: Odeur de courroie brulee ou d
    description: odeur de courroie brulee ou d electrique
    risk_level: confort
    evidence:
      - 'Observation: odeur de courroie brulee ou d'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 150 000 km ou
    description: plus de 150 000 km ou tension de charge basse
    risk_level: confort
    evidence:
      - 'Observation: plus de 150 000 km ou'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - adaptable tous
---
# Alternateur - Guide Complet

## Fonction

Recharger la batterie et alimenter les equipements electriques du vehicule moteur tournant

## Symptômes de défaillance

### Voyant batterie allume moteur tournant

voyant batterie allume moteur tournant

### Batterie qui se decharge malgre les

batterie qui se decharge malgre les trajets

### Phares qui faiblissent ou clignotent

phares qui faiblissent ou clignotent

### Sifflement de la courroie d accessoire

sifflement de la courroie d accessoire

### Odeur de courroie brulee ou d

odeur de courroie brulee ou d electrique

### Plus de 150 000 km ou

plus de 150 000 km ou tension de charge basse

## Diagnostic

Pour diagnostiquer un problème de alternateur:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- courroie-d-accessoire
- demarreur
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- poulie-d-alternateur

## Ne pas confondre avec

| Pièce confondue | Distinction |
|-----------------|-------------|
| demarreur | Alternateur = recharge batterie (moteur tournant), Démarreur = lance le moteur (au démarrage) |
| batterie | Alternateur recharge la batterie, si batterie HS l'alternateur ne peut compenser |

## Compatibilité

Pour commander le bon alternateur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Motorisation** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "zéro panne électrique"
- ❌ "homologué CT"
- ❌ "sécurité garantie"
