---
entity_type: gamme
title: Ampoule feu clignotant
slug: ampoule-feu-clignotant
pg_id: 105
category: eclairage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Produit la lumière intermittente pour signaler les changements de direction
  must_be_true:
    - produire
    - emettre
    - clignoter
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
    label: Clignotant qui clignote vite hyperfrequence
    description: clignotant qui clignote vite hyperfrequence
    risk_level: confort
    evidence:
      - 'Observation: clignotant qui clignote vite hyperfrequence'
      - Vérification visuelle ou auditive
  - id: S2
    label: Clignotant inactif d un cote
    description: clignotant inactif d un cote
    risk_level: confort
    evidence:
      - 'Observation: clignotant inactif d un cote'
      - Vérification visuelle ou auditive
  - id: S3
    label: Voyant tableau bord clignote anormalement
    description: voyant tableau bord clignote anormalement
    risk_level: confort
    evidence:
      - 'Observation: voyant tableau bord clignote anormalement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Ampoule feu clignotant - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière intermittente pour signaler les changements de direction

**Actions principales:** produire, emettre, clignoter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- clignotant qui clignote vite hyperfrequence
- clignotant inactif d un cote
- voyant tableau bord clignote anormalement

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule feu clignotant:

1. **Inspection visuelle** - Examiner l'état du ampoule feu clignotant
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
- ampoule-feu-de-position

## Critères de Compatibilité

Pour commander le bon ampoule feu clignotant, vous devez connaître:

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
