---
entity_type: gamme
title: Ampoule feu de position
slug: ampoule-feu-de-position
pg_id: 2126
category: eclairage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Produit la lumière pour signaler la présence du véhicule à faible intensité
  must_be_true:
    - produire
    - emettre
    - signaler
  must_not_contain_concepts:
    - feu complet
    - optique
    - relais
    - commande
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
symptoms:
  - id: S1
    label: Feu de position eteint
    description: feu de position eteint
    risk_level: confort
    evidence:
      - 'Observation: feu de position eteint'
      - Vérification visuelle ou auditive
  - id: S2
    label: Eclairage asymetrique
    description: eclairage asymetrique
    risk_level: confort
    evidence:
      - 'Observation: eclairage asymetrique'
      - Vérification visuelle ou auditive
  - id: S3
    label: Voyant au tableau de bord
    description: voyant au tableau de bord
    risk_level: confort
    evidence:
      - 'Observation: voyant au tableau de bord'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Ampoule feu de position - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière pour signaler la présence du véhicule à faible intensité

**Actions principales:** produire, emettre, signaler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- feu de position eteint
- eclairage asymetrique
- voyant au tableau de bord

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule feu de position:

1. **Inspection visuelle** - Examiner l'état du ampoule feu de position
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-arriere
- ampoule-feu-avant
- ampoule-feu-clignotant

## Critères de Compatibilité

Pour commander le bon ampoule feu de position, vous devez connaître:

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
