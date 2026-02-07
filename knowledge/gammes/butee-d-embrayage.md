---
entity_type: gamme
title: Butée d'embrayage
slug: butee-d-embrayage
pg_id: 48
category: embrayage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Actionner le mécanisme d'embrayage pour permettre le débrayage
  must_be_true:
    - actionner
    - débrayer
    - pousser
  must_not_contain_concepts:
    - disque
    - volant
    - couple
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
    label: Bruit roulement quand appuie pedale
    description: bruit roulement quand appuie pedale
    risk_level: confort
    evidence:
      - 'Observation: bruit roulement quand appuie pedale'
      - Vérification visuelle ou auditive
  - id: S2
    label: Sifflement grondement disparait relachant pedale
    description: sifflement grondement disparait relachant pedale
    risk_level: confort
    evidence:
      - 'Observation: sifflement grondement disparait relachant pedale'
      - Vérification visuelle ou auditive
  - id: S3
    label: Pedale d embrayage qui vibre sous le pied
    description: pedale d embrayage qui vibre sous le pied
    risk_level: confort
    evidence:
      - 'Observation: pedale d embrayage qui vibre sous le pied'
      - Vérification visuelle ou auditive
  - id: S4
    label: Embrayage qui accroche par a-coups
    description: embrayage qui accroche par a-coups
    risk_level: confort
    evidence:
      - 'Observation: embrayage qui accroche par a-coups'
      - Vérification visuelle ou auditive
  - id: S5
    label: Difficulte a passer les vitesses butee grippee
    description: difficulte a passer les vitesses butee grippee
    risk_level: confort
    evidence:
      - 'Observation: difficulte a passer les vitesses butee grippee'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus changement embrayage
    description: plus changement embrayage
    risk_level: confort
    evidence:
      - 'Observation: plus changement embrayage'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Butée d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Actionner le mécanisme d'embrayage pour permettre le débrayage

**Actions principales:** actionner, débrayer, pousser, libérer le disque, appuyer sur le mécanisme

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- bruit roulement quand appuie pedale
- sifflement grondement disparait relachant pedale
- pedale d embrayage qui vibre sous le pied
- embrayage qui accroche par a-coups
- difficulte a passer les vitesses butee grippee
- plus changement embrayage

## Procédure de Diagnostic

Pour diagnostiquer un problème de butée d'embrayage:

1. **Inspection visuelle** - Examiner l'état du butée d'embrayage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- emetteur-d-embrayage
- kit-d-embrayage
- recepteur-d-embrayage
- volant-moteur

## Critères de Compatibilité

Pour commander le bon butée d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "débrayage parfait"
