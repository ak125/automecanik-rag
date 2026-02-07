---
entity_type: gamme
title: Balais d'essuie-glace
slug: balais-d-essuie-glace
pg_id: 298
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Nettoie le pare-brise de l'eau et des impuretés
  must_be_true:
    - essuyer
    - nettoyer
    - balayer
  must_not_contain_concepts:
    - capteur abs
    - freinage
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
    label: Traces ou stries sur le pare-brise apres essuyage
    description: traces ou stries sur le pare-brise apres essuyage
    risk_level: confort
    evidence:
      - 'Observation: traces ou stries sur le pare-brise apres essuyage'
      - Vérification visuelle ou auditive
  - id: S2
    label: Zones non essuyees voile d eau persistant
    description: zones non essuyees voile d eau persistant
    risk_level: confort
    evidence:
      - 'Observation: zones non essuyees voile d eau persistant'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit de frottement ou de crissement
    description: bruit de frottement ou de crissement
    risk_level: confort
    evidence:
      - 'Observation: bruit de frottement ou de crissement'
      - Vérification visuelle ou auditive
  - id: S4
    label: Balai qui sautille sur le pare-brise
    description: balai qui sautille sur le pare-brise
    risk_level: confort
    evidence:
      - 'Observation: balai qui sautille sur le pare-brise'
      - Vérification visuelle ou auditive
  - id: S5
    label: Caoutchouc fissure durci ou decolle
    description: caoutchouc fissure durci ou decolle
    risk_level: confort
    evidence:
      - 'Observation: caoutchouc fissure durci ou decolle'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus d un an depuis le dernier remplacement
    description: plus d un an depuis le dernier remplacement
    risk_level: confort
    evidence:
      - 'Observation: plus d un an depuis le dernier remplacement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Balais d'essuie-glace - Guide Diagnostic Complet

## Fonction et Rôle

Nettoie le pare-brise de l'eau et des impuretés

**Actions principales:** essuyer, nettoyer, balayer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- traces ou stries sur le pare-brise apres essuyage
- zones non essuyees voile d eau persistant
- bruit de frottement ou de crissement
- balai qui sautille sur le pare-brise
- caoutchouc fissure durci ou decolle
- plus d un an depuis le dernier remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de balais d'essuie-glace:

1. **Inspection visuelle** - Examiner l'état du balais d'essuie-glace
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- commande-d-essuie-glace

## Critères de Compatibilité

Pour commander le bon balais d'essuie-glace, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "visibilité parfaite garantie"
