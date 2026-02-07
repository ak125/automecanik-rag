---
entity_type: gamme
title: Ampoule feu avant
slug: ampoule-feu-avant
pg_id: 107
category: eclairage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Produit la lumière pour éclairer la route devant le véhicule
  must_be_true:
    - produire
    - emettre
    - eclairer
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
  - if: symptome_general_detecte
    then: inspection_visuelle_et_test_fonctionnel
symptoms:
  - id: S1
    label: Phare ne fonctionne pas
    description: phare ne fonctionne pas
    risk_level: confort
    evidence:
      - 'Observation: phare ne fonctionne pas'
      - Vérification visuelle ou auditive
  - id: S2
    label: Ampoule grillée
    description: ampoule grillée
    risk_level: confort
    evidence:
      - 'Observation: ampoule grillée'
      - Vérification visuelle ou auditive
  - id: S3
    label: Eclairage faible
    description: eclairage faible
    risk_level: confort
    evidence:
      - 'Observation: eclairage faible'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Ampoule feu avant - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière pour éclairer la route devant le véhicule

**Actions principales:** produire, emettre, eclairer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- phare ne fonctionne pas
- ampoule grillée
- eclairage faible

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule feu avant:

1. **Inspection visuelle** - Examiner l'état du ampoule feu avant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-arriere
- ampoule-feu-clignotant
- ampoule-feu-de-position

## Critères de Compatibilité

Pour commander le bon ampoule feu avant, vous devez connaître:

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
