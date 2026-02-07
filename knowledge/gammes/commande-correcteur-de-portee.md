---
entity_type: gamme
title: Commande correcteur de portée
slug: commande-correcteur-de-portee
pg_id: 1432
category: eclairage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Interface permettant au conducteur de régler la hauteur des phares depuis
    l'habitacle
  must_be_true:
    - commander
    - activer
    - regler
  must_not_contain_concepts:
    - ampoule
    - feu
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: vehicule_immobilise_ou_symptome_critique
    then: verification_urgente_piece_et_alimentation
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
symptoms:
  - id: S1
    label: Molette de reglage inactive
    description: molette de reglage inactive
    risk_level: confort
    evidence:
      - 'Observation: molette de reglage inactive'
      - Vérification visuelle ou auditive
  - id: S2
    label: Phares bloques en position haute basse
    description: phares bloques en position haute basse
    risk_level: immobilisation
    evidence:
      - 'Observation: phares bloques en position haute basse'
      - Vérification visuelle ou auditive
  - id: S3
    label: Voyant defaut eclairage
    description: voyant defaut eclairage
    risk_level: confort
    evidence:
      - 'Observation: voyant defaut eclairage'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Commande correcteur de portée - Guide Diagnostic Complet

## Fonction et Rôle

Interface permettant au conducteur de régler la hauteur des phares depuis l'habitacle

**Actions principales:** commander, activer, regler

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Phares bloques en position haute basse**
  phares bloques en position haute basse

### 🟢 Autres Symptômes

- molette de reglage inactive
- voyant defaut eclairage

## Procédure de Diagnostic

Pour diagnostiquer un problème de commande correcteur de portée:

1. **Inspection visuelle** - Examiner l'état du commande correcteur de portée
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Pièce HS** - Le commande correcteur de portée peut être hors service et nécessiter un remplacement
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- correcteur-de-portee
- feu-avant

## Critères de Compatibilité

Pour commander le bon commande correcteur de portée, vous devez connaître:

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
