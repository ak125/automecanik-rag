---
entity_type: gamme
title: Rétroviseur extérieur
slug: retroviseur-exterieur
pg_id: 50
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Permet la vision arrière et latérale
  must_be_true:
    - reflechir
    - montrer
    - permettre la vision
  must_not_contain_concepts:
    - injection
    - freinage
    - distribution
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
  - if: vibrations_anormales
    then: verifier_equilibrage_et_fixations
symptoms:
  - id: S1
    label: Miroir casse fissure ou decolle
    description: miroir casse fissure ou decolle
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: miroir casse fissure ou decolle'
      - Vérification visuelle ou auditive
  - id: S2
    label: Coque de retroviseur cassee choc accrochage
    description: coque de retroviseur cassee choc accrochage
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: coque de retroviseur cassee choc accrochage'
      - Vérification visuelle ou auditive
  - id: S3
    label: Reglage electrique inoperant ou lent
    description: reglage electrique inoperant ou lent
    risk_level: confort
    evidence:
      - 'Observation: reglage electrique inoperant ou lent'
      - Vérification visuelle ou auditive
  - id: S4
    label: Degivrage du miroir qui ne fonctionne plus
    description: degivrage du miroir qui ne fonctionne plus
    risk_level: confort
    evidence:
      - 'Observation: degivrage du miroir qui ne fonctionne plus'
      - Vérification visuelle ou auditive
  - id: S5
    label: Retroviseur rabattable bloque ou qui vibre
    description: retroviseur rabattable bloque ou qui vibre
    risk_level: immobilisation
    evidence:
      - 'Observation: retroviseur rabattable bloque ou qui vibre'
      - Vérification visuelle ou auditive
  - id: S6
    label: Repetiteur de clignotant integre grille
    description: repetiteur de clignotant integre grille
    risk_level: confort
    evidence:
      - 'Observation: repetiteur de clignotant integre grille'
      - Vérification visuelle ou auditive
  - id: S7
    label: Miroir fissure ebreche deformant image
    description: miroir fissure ebreche deformant image
    risk_level: confort
    evidence:
      - 'Observation: miroir fissure ebreche deformant image'
      - Vérification visuelle ou auditive
  - id: S8
    label: Bruit claquement vibration retroviseur vent
    description: bruit claquement vibration retroviseur vent
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit claquement vibration retroviseur vent'
      - Vérification visuelle ou auditive
  - id: S9
    label: Odeur plastique brule moteur electrique
    description: odeur plastique brule moteur electrique
    risk_level: confort
    evidence:
      - 'Observation: odeur plastique brule moteur electrique'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Rétroviseur extérieur - Guide Diagnostic Complet

## Fonction et Rôle

Permet la vision arrière et latérale

**Actions principales:** reflechir, montrer, permettre la vision

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Retroviseur rabattable bloque ou qui vibre**
  retroviseur rabattable bloque ou qui vibre

### 🟠 Symptômes de Dégâts Potentiels

- **Miroir casse fissure ou decolle**
  miroir casse fissure ou decolle
- **Coque de retroviseur cassee choc accrochage**
  coque de retroviseur cassee choc accrochage
- **Bruit claquement vibration retroviseur vent**
  bruit claquement vibration retroviseur vent

### 🟢 Autres Symptômes

- reglage electrique inoperant ou lent
- degivrage du miroir qui ne fonctionne plus
- repetiteur de clignotant integre grille
- miroir fissure ebreche deformant image
- odeur plastique brule moteur electrique

## Procédure de Diagnostic

Pour diagnostiquer un problème de rétroviseur extérieur:

1. **Inspection visuelle** - Examiner l'état du rétroviseur extérieur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le rétroviseur extérieur peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- bouton-de-retroviseur

## Critères de Compatibilité

Pour commander le bon rétroviseur extérieur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleure visibilité garantie"
