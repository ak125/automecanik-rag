---
entity_type: gamme
title: Bague d'étanchéité cardan
slug: bague-d-etancheite-cardan
pg_id: 624
category: transmission
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Assurer l'etancheite de la transmission au niveau du cardan
  must_be_true:
    - assurer l'etancheite
    - empecher les fuites
  must_not_contain_concepts:
    - moteur
    - culasse
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
    label: Graisse projetee sur la roue
    description: graisse projetee sur la roue
    risk_level: confort
    evidence:
      - 'Observation: graisse projetee sur la roue'
      - Vérification visuelle ou auditive
  - id: S2
    label: Claquements en braquage
    description: claquements en braquage
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquements en braquage'
      - Vérification visuelle ou auditive
  - id: S3
    label: Joint homocinetique bruyant
    description: joint homocinetique bruyant
    risk_level: confort
    evidence:
      - 'Observation: joint homocinetique bruyant'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Bague d'étanchéité cardan - Guide Diagnostic Complet

## Fonction et Rôle

Assurer l'etancheite de la transmission au niveau du cardan

**Actions principales:** assurer l'etancheite, empecher les fuites

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquements en braquage**
  claquements en braquage

### 🟢 Autres Symptômes

- graisse projetee sur la roue
- joint homocinetique bruyant

## Procédure de Diagnostic

Pour diagnostiquer un problème de bague d'étanchéité cardan:

1. **Inspection visuelle** - Examiner l'état du bague d'étanchéité cardan
2. **Test dynamique** - Vérifier les bruits en roulant
3. **Contrôle du jeu** - Examiner l'usure des articulations

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- cardan

## Critères de Compatibilité

Pour commander le bon bague d'étanchéité cardan, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare la transmission"
