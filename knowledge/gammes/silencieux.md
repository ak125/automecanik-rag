---
entity_type: gamme
title: Silencieux
slug: silencieux
pg_id: 26
category: echappement
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Atténue le bruit des gaz d'échappement avant évacuation
  must_be_true:
    - attenuer
    - evacuer
    - reduire le bruit
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
symptoms:
  - id: S1
    label: Bruit excessif
    description: bruit excessif
    risk_level: confort
    evidence:
      - 'Observation: bruit excessif'
      - Vérification visuelle ou auditive
  - id: S2
    label: Vibrations
    description: vibrations
    risk_level: confort
    evidence:
      - 'Observation: vibrations'
      - Vérification visuelle ou auditive
  - id: S3
    label: Corrosion
    description: corrosion
    risk_level: confort
    evidence:
      - 'Observation: corrosion'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Silencieux - Guide Diagnostic Complet

## Fonction et Rôle

Atténue le bruit des gaz d'échappement avant évacuation

**Actions principales:** attenuer, evacuer, reduire le bruit

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- bruit excessif
- vibrations
- corrosion

## Procédure de Diagnostic

Pour diagnostiquer un problème de silencieux:

1. **Inspection visuelle** - Examiner l'état du silencieux
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- tube-d-echappement
- support-d-echappement

## Critères de Compatibilité

Pour commander le bon silencieux, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "passe le controle technique"
