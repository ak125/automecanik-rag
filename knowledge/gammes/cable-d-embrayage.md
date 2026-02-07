---
entity_type: gamme
title: Câble d'embrayage
slug: cable-d-embrayage
pg_id: 478
category: embrayage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmettre l'effort mécanique de la pédale vers la fourchette
  must_be_true:
    - transmettre l'effort
    - tirer
    - pousser
  must_not_contain_concepts:
    - disque
    - volant
    - couple
    - hydraulique
    - liquide
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
    label: Pedale d embrayage dure ou difficile a enfoncer
    description: pedale d embrayage dure ou difficile a enfoncer
    risk_level: confort
    evidence:
      - 'Observation: pedale d embrayage dure ou difficile a enfoncer'
      - Vérification visuelle ou auditive
  - id: S2
    label: Point de patinage tres haut ou tres bas
    description: point de patinage tres haut ou tres bas
    risk_level: confort
    evidence:
      - 'Observation: point de patinage tres haut ou tres bas'
      - Vérification visuelle ou auditive
  - id: S3
    label: Craquement ou grincement en appuyant sur la pedale
    description: craquement ou grincement en appuyant sur la pedale
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: craquement ou grincement en appuyant sur la pedale'
      - Vérification visuelle ou auditive
  - id: S4
    label: Cable visible effiloche ou rouille
    description: cable visible effiloche ou rouille
    risk_level: confort
    evidence:
      - 'Observation: cable visible effiloche ou rouille'
      - Vérification visuelle ou auditive
  - id: S5
    label: Embrayage qui ne debraye pas completement
    description: embrayage qui ne debraye pas completement
    risk_level: confort
    evidence:
      - 'Observation: embrayage qui ne debraye pas completement'
      - Vérification visuelle ou auditive
  - id: S6
    label: Pedale qui reste enfoncee cable casse
    description: pedale qui reste enfoncee cable casse
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: pedale qui reste enfoncee cable casse'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Câble d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre l'effort mécanique de la pédale vers la fourchette

**Actions principales:** transmettre l'effort, tirer, pousser, relier, actionner

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Craquement ou grincement en appuyant sur la pedale**
  craquement ou grincement en appuyant sur la pedale
- **Pedale qui reste enfoncee cable casse**
  pedale qui reste enfoncee cable casse

### 🟢 Autres Symptômes

- pedale d embrayage dure ou difficile a enfoncer
- point de patinage tres haut ou tres bas
- cable visible effiloche ou rouille
- embrayage qui ne debraye pas completement

## Procédure de Diagnostic

Pour diagnostiquer un problème de câble d'embrayage:

1. **Inspection visuelle** - Examiner l'état du câble d'embrayage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- butee-d-embrayage
- kit-d-embrayage
- volant-moteur

## Critères de Compatibilité

Pour commander le bon câble d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "effort parfait"
