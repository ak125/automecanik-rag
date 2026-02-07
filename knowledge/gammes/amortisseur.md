---
entity_type: gamme
title: Amortisseur
slug: amortisseur
pg_id: 854
category: suspension
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Controler les oscillations du ressort et stabiliser la roue. Dissipe
    l'energie des chocs. NE SUPPORTE PAS LE POIDS DU VEHICULE!
  must_be_true:
    - amortir
    - controler
    - dissiper
  must_not_contain_concepts:
    - direction
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
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Vehicule qui rebondit excessivement sur les bosses
    description: vehicule qui rebondit excessivement sur les bosses
    risk_level: confort
    evidence:
      - 'Observation: vehicule qui rebondit excessivement sur les bosses'
      - Vérification visuelle ou auditive
  - id: S2
    label: Fuite huile visible corps amortisseur
    description: fuite huile visible corps amortisseur
    risk_level: confort
    evidence:
      - 'Observation: fuite huile visible corps amortisseur'
      - Vérification visuelle ou auditive
  - id: S3
    label: Usure asymetrique ou irreguliere des pneus
    description: usure asymetrique ou irreguliere des pneus
    risk_level: securite
    evidence:
      - 'Observation: usure asymetrique ou irreguliere des pneus'
      - Vérification visuelle ou auditive
  - id: S4
    label: Bruit de cognement sur routes degradees
    description: bruit de cognement sur routes degradees
    risk_level: confort
    evidence:
      - 'Observation: bruit de cognement sur routes degradees'
      - Vérification visuelle ou auditive
  - id: S5
    label: Sensation d instabilite en virage ou au freinage
    description: sensation d instabilite en virage ou au freinage
    risk_level: securite
    evidence:
      - 'Observation: sensation d instabilite en virage ou au freinage'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 80 000 km sans remplacement
    description: plus de 80 000 km sans remplacement
    risk_level: confort
    evidence:
      - 'Observation: plus de 80 000 km sans remplacement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Amortisseur - Guide Diagnostic Complet

## Fonction et Rôle

Controler les oscillations du ressort et stabiliser la roue. Dissipe l'energie des chocs. NE SUPPORTE PAS LE POIDS DU VEHICULE!

**Actions principales:** amortir, controler, dissiper, stabiliser, absorber les oscillations

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Usure asymetrique ou irreguliere des pneus**
  usure asymetrique ou irreguliere des pneus
- **Sensation d instabilite en virage ou au freinage**
  sensation d instabilite en virage ou au freinage

### 🟢 Autres Symptômes

- vehicule qui rebondit excessivement sur les bosses
- fuite huile visible corps amortisseur
- bruit de cognement sur routes degradees
- plus de 80 000 km sans remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de amortisseur:

1. **Inspection visuelle** - Examiner l'état du amortisseur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- bras-de-suspension
- kit-de-butee-de-suspension
- ressort-de-suspension
- rotule-de-suspension

## Critères de Compatibilité

Pour commander le bon amortisseur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "tenue de route parfaite"
