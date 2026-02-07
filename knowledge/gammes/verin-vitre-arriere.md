---
entity_type: gamme
title: Vérin vitre arrière
slug: verin-vitre-arriere
pg_id: 2454
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Maintient la vitre arrière ou le hayon en position ouverte
  must_be_true:
    - maintenir
    - supporter
    - soulever
  must_not_contain_concepts:
    - leve-vitre
    - electrique
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
    label: Vitre arriere qui retombe seule
    description: vitre arriere qui retombe seule
    risk_level: confort
    evidence:
      - 'Observation: vitre arriere qui retombe seule'
      - Vérification visuelle ou auditive
  - id: S2
    label: Ouverture difficile de la vitre
    description: ouverture difficile de la vitre
    risk_level: confort
    evidence:
      - 'Observation: ouverture difficile de la vitre'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruits lors de l ouverture fermeture
    description: bruits lors de l ouverture fermeture
    risk_level: confort
    evidence:
      - 'Observation: bruits lors de l ouverture fermeture'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Vérin vitre arrière - Guide Diagnostic Complet

## Fonction et Rôle

Maintient la vitre arrière ou le hayon en position ouverte

**Actions principales:** maintenir, supporter, soulever

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- vitre arriere qui retombe seule
- ouverture difficile de la vitre
- bruits lors de l ouverture fermeture

## Procédure de Diagnostic

Pour diagnostiquer un problème de vérin vitre arrière:

1. **Inspection visuelle** - Examiner l'état du vérin vitre arrière
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- hayon
- charniere

## Critères de Compatibilité

Pour commander le bon vérin vitre arrière, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"
