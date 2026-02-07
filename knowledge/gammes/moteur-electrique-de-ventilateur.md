---
entity_type: gamme
title: Moteur électrique de ventilateur
slug: moteur-electrique-de-ventilateur
pg_id: 792
category: refroidissement
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Entrainer les pales du ventilateur de refroidissement
  must_be_true:
    - entrainer
    - tourner
    - ventiler
  must_not_contain_concepts:
    - injection
    - freinage
    - embrayage
    - distribution
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: vehicule_immobilise_ou_symptome_critique
    then: verification_urgente_piece_et_alimentation
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
symptoms:
  - id: S1
    label: Ventilateur qui ne tourne pas
    description: ventilateur qui ne tourne pas
    risk_level: immobilisation
    evidence:
      - 'Observation: ventilateur qui ne tourne pas'
      - Vérification visuelle ou auditive
  - id: S2
    label: Surchauffe en circulation lente
    description: surchauffe en circulation lente
    risk_level: confort
    evidence:
      - 'Observation: surchauffe en circulation lente'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit de roulement du ventilateur
    description: bruit de roulement du ventilateur
    risk_level: confort
    evidence:
      - 'Observation: bruit de roulement du ventilateur'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Moteur électrique de ventilateur - Guide Diagnostic Complet

## Fonction et Rôle

Entrainer les pales du ventilateur de refroidissement

**Actions principales:** entrainer, tourner, ventiler

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Ventilateur qui ne tourne pas**
  ventilateur qui ne tourne pas

### 🟢 Autres Symptômes

- surchauffe en circulation lente
- bruit de roulement du ventilateur

## Procédure de Diagnostic

Pour diagnostiquer un problème de moteur électrique de ventilateur:

1. **Inspection visuelle** - Examiner l'état du moteur électrique de ventilateur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le moteur électrique de ventilateur peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes

## Pièces Associées

Lors du remplacement, vérifier également:

- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon moteur électrique de ventilateur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidissement optimal"
