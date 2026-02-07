---
entity_type: gamme
title: Ampoule feu stop
slug: ampoule-feu-stop
pg_id: 111
category: eclairage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Produit la lumière pour signaler le freinage du véhicule
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
  - if: symptome_general_detecte
    then: inspection_visuelle_et_test_fonctionnel
symptoms:
  - id: S1
    label: Un seul feu stop ne s allume pas
    description: un seul feu stop ne s allume pas
    risk_level: confort
    evidence:
      - 'Observation: un seul feu stop ne s allume pas'
      - Vérification visuelle ou auditive
  - id: S2
    label: Feu stop qui clignote ou s allume faiblement
    description: feu stop qui clignote ou s allume faiblement
    risk_level: confort
    evidence:
      - 'Observation: feu stop qui clignote ou s allume faiblement'
      - Vérification visuelle ou auditive
  - id: S3
    label: Ampoule noircie visible a travers le feu
    description: ampoule noircie visible a travers le feu
    risk_level: confort
    evidence:
      - 'Observation: ampoule noircie visible a travers le feu'
      - Vérification visuelle ou auditive
  - id: S4
    label: Message defaut feux au tableau de bord
    description: message defaut feux au tableau de bord
    risk_level: confort
    evidence:
      - 'Observation: message defaut feux au tableau de bord'
      - Vérification visuelle ou auditive
  - id: S5
    label: Feux stop grillent souvent verifier
    description: feux stop grillent souvent verifier
    risk_level: confort
    evidence:
      - 'Observation: feux stop grillent souvent verifier'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Ampoule feu stop - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière pour signaler le freinage du véhicule

**Actions principales:** produire, emettre, signaler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- un seul feu stop ne s allume pas
- feu stop qui clignote ou s allume faiblement
- ampoule noircie visible a travers le feu
- message defaut feux au tableau de bord
- feux stop grillent souvent verifier

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule feu stop:

1. **Inspection visuelle** - Examiner l'état du ampoule feu stop
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- feu-arriere
- contacteur-feu-stop

## Critères de Compatibilité

Pour commander le bon ampoule feu stop, vous devez connaître:

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
