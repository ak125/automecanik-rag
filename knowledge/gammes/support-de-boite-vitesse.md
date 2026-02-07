---
entity_type: gamme
title: Support de boîte vitesse
slug: support-de-boite-vitesse
pg_id: 249
category: support_moteur
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Supporter et fixer la boite de vitesses au chassis
  must_be_true:
    - supporter
    - fixer
    - amortir
  must_not_contain_concepts:
    - injection
    - freinage
    - climatisation
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
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Vibrations ressenties sur le levier de vitesses
    description: vibrations ressenties sur le levier de vitesses
    risk_level: confort
    evidence:
      - 'Observation: vibrations ressenties sur le levier de vitesses'
      - Vérification visuelle ou auditive
  - id: S2
    label: Caoutchouc du support visiblement deteriore
    description: caoutchouc du support visiblement deteriore
    risk_level: confort
    evidence:
      - 'Observation: caoutchouc du support visiblement deteriore'
      - Vérification visuelle ou auditive
  - id: S3
    label: Claquement ou bruit sourd au passage des rapports
    description: claquement ou bruit sourd au passage des rapports
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement ou bruit sourd au passage des rapports'
      - Vérification visuelle ou auditive
  - id: S4
    label: Boite de vitesses qui semble bouger anormalement
    description: boite de vitesses qui semble bouger anormalement
    risk_level: confort
    evidence:
      - 'Observation: boite de vitesses qui semble bouger anormalement'
      - Vérification visuelle ou auditive
  - id: S5
    label: Sensation d a-coups a l embrayage ou debrayage
    description: sensation d a-coups a l embrayage ou debrayage
    risk_level: confort
    evidence:
      - 'Observation: sensation d a-coups a l embrayage ou debrayage'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 100 000 km ou supports moteur a changer
    description: plus de 100 000 km ou supports moteur a changer
    risk_level: confort
    evidence:
      - 'Observation: plus de 100 000 km ou supports moteur a changer'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Support de boîte vitesse - Guide Diagnostic Complet

## Fonction et Rôle

Supporter et fixer la boite de vitesses au chassis

**Actions principales:** supporter, fixer, amortir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement ou bruit sourd au passage des rapports**
  claquement ou bruit sourd au passage des rapports

### 🟢 Autres Symptômes

- vibrations ressenties sur le levier de vitesses
- caoutchouc du support visiblement deteriore
- boite de vitesses qui semble bouger anormalement
- sensation d a-coups a l embrayage ou debrayage
- plus de 100 000 km ou supports moteur a changer

## Procédure de Diagnostic

Pour diagnostiquer un problème de support de boîte vitesse:

1. **Inspection visuelle** - Examiner l'état du support de boîte vitesse
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- support-moteur
- boite-de-vitesses

## Critères de Compatibilité

Pour commander le bon support de boîte vitesse, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "zero vibration"
