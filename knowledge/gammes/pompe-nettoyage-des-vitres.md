---
entity_type: gamme
title: Pompe nettoyage des vitres
slug: pompe-nettoyage-des-vitres
pg_id: 794
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Projette le liquide lave-glace sur le pare-brise
  must_be_true:
    - projeter
    - pulveriser
    - alimenter
  must_not_contain_concepts:
    - balai
    - moteur essuie-glace
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
    label: Jet de lave-glace absent
    description: jet de lave-glace absent
    risk_level: securite
    evidence:
      - 'Observation: jet de lave-glace absent'
      - Vérification visuelle ou auditive
  - id: S2
    label: Pompe qui fait du bruit sans projeter
    description: pompe qui fait du bruit sans projeter
    risk_level: confort
    evidence:
      - 'Observation: pompe qui fait du bruit sans projeter'
      - Vérification visuelle ou auditive
  - id: S3
    label: Jet faible malgre reservoir plein
    description: jet faible malgre reservoir plein
    risk_level: confort
    evidence:
      - 'Observation: jet faible malgre reservoir plein'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Pompe nettoyage des vitres - Guide Diagnostic Complet

## Fonction et Rôle

Projette le liquide lave-glace sur le pare-brise

**Actions principales:** projeter, pulveriser, alimenter

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Jet de lave-glace absent**
  jet de lave-glace absent

### 🟢 Autres Symptômes

- pompe qui fait du bruit sans projeter
- jet faible malgre reservoir plein

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe nettoyage des vitres:

1. **Inspection visuelle** - Examiner l'état du pompe nettoyage des vitres
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bras-d-essuie-glace
- commande-d-essuie-glace
- moteur-d-essuie-glace

## Critères de Compatibilité

Pour commander le bon pompe nettoyage des vitres, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "visibilite parfaite"
