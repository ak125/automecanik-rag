---
entity_type: gamme
title: Feu arrière
slug: feu-arriere
pg_id: 290
category: eclairage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Signale la présence et les actions du véhicule
  must_be_true:
    - signaler
    - indiquer
    - eclairer
  must_not_contain_concepts:
    - injection
    - freinage
    - embrayage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
symptoms:
  - id: S1
    label: Arriere allume plus cote stop
    description: arriere allume plus cote stop
    risk_level: confort
    evidence:
      - 'Observation: arriere allume plus cote stop'
      - Vérification visuelle ou auditive
  - id: S2
    label: Buee visible interieur bloc optique
    description: buee visible interieur bloc optique
    risk_level: confort
    evidence:
      - 'Observation: buee visible interieur bloc optique'
      - Vérification visuelle ou auditive
  - id: S3
    label: Ampoule qui grille frequemment probleme de masse
    description: ampoule qui grille frequemment probleme de masse
    risk_level: confort
    evidence:
      - 'Observation: ampoule qui grille frequemment probleme de masse'
      - Vérification visuelle ou auditive
  - id: S4
    label: Controle technique refuse pour feux defaillants
    description: controle technique refuse pour feux defaillants
    risk_level: confort
    evidence:
      - 'Observation: controle technique refuse pour feux defaillants'
      - Vérification visuelle ou auditive
  - id: S5
    label: Plus de 10 ans sans verification des connecteurs
    description: plus de 10 ans sans verification des connecteurs
    risk_level: confort
    evidence:
      - 'Observation: plus de 10 ans sans verification des connecteurs'
      - Vérification visuelle ou auditive
  - id: S6
    label: Bruit crissement electrique niveau arriere
    description: bruit crissement electrique niveau arriere
    risk_level: confort
    evidence:
      - 'Observation: bruit crissement electrique niveau arriere'
      - Vérification visuelle ou auditive
  - id: S7
    label: Feux inefficaces car tres faibles a l allumage
    description: feux inefficaces car tres faibles a l allumage
    risk_level: confort
    evidence:
      - 'Observation: feux inefficaces car tres faibles a l allumage'
      - Vérification visuelle ou auditive
  - id: S8
    label: Odeur plastique surchauffe niveau feux
    description: odeur plastique surchauffe niveau feux
    risk_level: confort
    evidence:
      - 'Observation: odeur plastique surchauffe niveau feux'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Feu arrière - Guide Diagnostic Complet

## Fonction et Rôle

Signale la présence et les actions du véhicule

**Actions principales:** signaler, indiquer, eclairer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- arriere allume plus cote stop
- buee visible interieur bloc optique
- ampoule qui grille frequemment probleme de masse
- controle technique refuse pour feux defaillants
- plus de 10 ans sans verification des connecteurs
- bruit crissement electrique niveau arriere

## Procédure de Diagnostic

Pour diagnostiquer un problème de feu arrière:

1. **Inspection visuelle** - Examiner l'état du feu arrière
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-arriere
- commande-d-eclairage
- contacteur-de-feu-de-recul
- feu-avant
- feu-clignotant
- interrupteur-des-feux-de-freins

## Critères de Compatibilité

Pour commander le bon feu arrière, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "sécurité maximale"
