---
entity_type: gamme
title: Interrupteur des feux de freins
slug: interrupteur-des-feux-de-freins
pg_id: 806
category: capteurs
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Detecte l'appui sur la pedale de frein pour activer les feux stop
  must_be_true:
    - detecter
    - signaler
    - activer
  must_not_contain_concepts:
    - reparation
    - regeneration
    - nettoyage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Feux stop qui restent allumes moteur eteint
    description: feux stop qui restent allumes moteur eteint
    risk_level: confort
    evidence:
      - 'Observation: feux stop qui restent allumes moteur eteint'
      - Vérification visuelle ou auditive
  - id: S2
    label: Feux stop qui ne s allument plus du tout
    description: feux stop qui ne s allument plus du tout
    risk_level: confort
    evidence:
      - 'Observation: feux stop qui ne s allument plus du tout'
      - Vérification visuelle ou auditive
  - id: S3
    label: Regulateur de vitesse qui ne fonctionne plus
    description: regulateur de vitesse qui ne fonctionne plus
    risk_level: confort
    evidence:
      - 'Observation: regulateur de vitesse qui ne fonctionne plus'
      - Vérification visuelle ou auditive
  - id: S4
    label: Message d erreur systeme esp au tableau de bord
    description: message d erreur systeme esp au tableau de bord
    risk_level: securite
    evidence:
      - 'Observation: message d erreur systeme esp au tableau de bord'
      - Vérification visuelle ou auditive
  - id: S5
    label: Batterie decharge feux stop restes
    description: batterie decharge feux stop restes
    risk_level: confort
    evidence:
      - 'Observation: batterie decharge feux stop restes'
      - Vérification visuelle ou auditive
  - id: S6
    label: Clic audible absent quand on appuie sur la pedale
    description: clic audible absent quand on appuie sur la pedale
    risk_level: securite
    evidence:
      - 'Observation: clic audible absent quand on appuie sur la pedale'
      - Vérification visuelle ou auditive
  - id: S7
    label: Odeur de plastique brule court-circuit
    description: odeur de plastique brule court-circuit
    risk_level: confort
    evidence:
      - 'Observation: odeur de plastique brule court-circuit'
      - Vérification visuelle ou auditive
  - id: S8
    label: Plus de 150 000 km sans verification
    description: plus de 150 000 km sans verification
    risk_level: confort
    evidence:
      - 'Observation: plus de 150 000 km sans verification'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Interrupteur des feux de freins - Guide Diagnostic Complet

## Fonction et Rôle

Detecte l'appui sur la pedale de frein pour activer les feux stop

**Actions principales:** detecter, signaler, activer, commander

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Message d erreur systeme esp au tableau de bord**
  message d erreur systeme esp au tableau de bord
- **Clic audible absent quand on appuie sur la pedale**
  clic audible absent quand on appuie sur la pedale

### 🟢 Autres Symptômes

- feux stop qui restent allumes moteur eteint
- feux stop qui ne s allument plus du tout
- regulateur de vitesse qui ne fonctionne plus
- batterie decharge feux stop restes
- odeur de plastique brule court-circuit
- plus de 150 000 km sans verification

## Procédure de Diagnostic

Pour diagnostiquer un problème de interrupteur des feux de freins:

1. **Inspection visuelle** - Examiner l'état du interrupteur des feux de freins
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- cable-de-frein-a-main
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- etrier-de-frein
- feu-arriere
- kit-de-freins-arriere
- machoires-de-frein

## Critères de Compatibilité

Pour commander le bon interrupteur des feux de freins, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleur freinage"
