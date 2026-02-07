---
entity_type: gamme
title: Galet enrouleur de courroie de distribution
slug: galet-enrouleur-de-courroie-de-distribution
pg_id: 313
category: distribution
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Guider la courroie de distribution dans son parcours
  must_be_true:
    - guider
    - enrouler
    - positionner
  must_not_contain_concepts:
    - freinage
    - climatisation
    - turbo
    - injection
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
    label: Bruit de roulement au ralenti
    description: bruit de roulement au ralenti
    risk_level: confort
    evidence:
      - 'Observation: bruit de roulement au ralenti'
      - Vérification visuelle ou auditive
  - id: S2
    label: Sifflement cote distribution
    description: sifflement cote distribution
    risk_level: confort
    evidence:
      - 'Observation: sifflement cote distribution'
      - Vérification visuelle ou auditive
  - id: S3
    label: Traces d usure anormale sur la courroie
    description: traces d usure anormale sur la courroie
    risk_level: confort
    evidence:
      - 'Observation: traces d usure anormale sur la courroie'
      - Vérification visuelle ou auditive
  - id: S4
    label: Galet qui tourne difficilement a la main
    description: galet qui tourne difficilement a la main
    risk_level: confort
    evidence:
      - 'Observation: galet qui tourne difficilement a la main'
      - Vérification visuelle ou auditive
  - id: S5
    label: Jeu radial ou axial dans le galet
    description: jeu radial ou axial dans le galet
    risk_level: confort
    evidence:
      - 'Observation: jeu radial ou axial dans le galet'
      - Vérification visuelle ou auditive
  - id: S6
    label: Bruit metallique leger
    description: bruit metallique leger
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit metallique leger'
      - Vérification visuelle ou auditive
  - id: S7
    label: Courroie qui se deporte sur le cote
    description: courroie qui se deporte sur le cote
    risk_level: confort
    evidence:
      - 'Observation: courroie qui se deporte sur le cote'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Galet enrouleur de courroie de distribution - Guide Diagnostic Complet

## Fonction et Rôle

Guider la courroie de distribution dans son parcours

**Actions principales:** guider, enrouler, positionner

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit metallique leger**
  bruit metallique leger

### 🟢 Autres Symptômes

- bruit de roulement au ralenti
- sifflement cote distribution
- traces d usure anormale sur la courroie
- galet qui tourne difficilement a la main
- jeu radial ou axial dans le galet
- courroie qui se deporte sur le cote

## Procédure de Diagnostic

Pour diagnostiquer un problème de galet enrouleur de courroie de distribution:

1. **Inspection visuelle** - Examiner l'état du galet enrouleur de courroie de distribution
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-de-distribution

## Critères de Compatibilité

Pour commander le bon galet enrouleur de courroie de distribution, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "synchronisation parfaite"
