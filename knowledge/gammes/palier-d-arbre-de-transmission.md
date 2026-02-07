---
entity_type: gamme
title: Palier d'arbre de transmission
slug: palier-d-arbre-de-transmission
pg_id: 2109
category: transmission
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Supporter et guider l'arbre de transmission en rotation
  must_be_true:
    - supporter
    - guider
    - centrer
  must_not_contain_concepts:
    - injection
    - freinage
    - climatisation
    - allumage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: vibrations_anormales
    then: verifier_equilibrage_et_fixations
symptoms:
  - id: S1
    label: Vibrations a vitesse constante
    description: vibrations a vitesse constante
    risk_level: confort
    evidence:
      - 'Observation: vibrations a vitesse constante'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit de roulement sous le vehicule
    description: bruit de roulement sous le vehicule
    risk_level: confort
    evidence:
      - 'Observation: bruit de roulement sous le vehicule'
      - Vérification visuelle ou auditive
  - id: S3
    label: Jeu perceptible au palier
    description: jeu perceptible au palier
    risk_level: confort
    evidence:
      - 'Observation: jeu perceptible au palier'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Palier d'arbre de transmission - Guide Diagnostic Complet

## Fonction et Rôle

Supporter et guider l'arbre de transmission en rotation

**Actions principales:** supporter, guider, centrer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- vibrations a vitesse constante
- bruit de roulement sous le vehicule
- jeu perceptible au palier

## Procédure de Diagnostic

Pour diagnostiquer un problème de palier d'arbre de transmission:

1. **Inspection visuelle** - Examiner l'état du palier d'arbre de transmission
2. **Test dynamique** - Vérifier les bruits en roulant
3. **Contrôle du jeu** - Examiner l'usure des articulations
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- cardan
- roulement

## Critères de Compatibilité

Pour commander le bon palier d'arbre de transmission, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "transmission parfaite"
