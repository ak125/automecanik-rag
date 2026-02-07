---
entity_type: gamme
title: Conduite de climatisation
slug: conduite-de-climatisation
pg_id: 2094
category: climatisation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Acheminer le fluide frigorigene entre les composants
  must_be_true:
    - vehiculer
    - transporter
    - acheminer
  must_not_contain_concepts:
    - injection
    - freinage
    - allumage
    - embrayage
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
    label: Climatisation inefficace
    description: climatisation inefficace
    risk_level: confort
    evidence:
      - 'Observation: climatisation inefficace'
      - Vérification visuelle ou auditive
  - id: S2
    label: Traces de gras sur les raccords
    description: traces de gras sur les raccords
    risk_level: confort
    evidence:
      - 'Observation: traces de gras sur les raccords'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit de sifflement dans le circuit
    description: bruit de sifflement dans le circuit
    risk_level: confort
    evidence:
      - 'Observation: bruit de sifflement dans le circuit'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Conduite de climatisation - Guide Diagnostic Complet

## Fonction et Rôle

Acheminer le fluide frigorigene entre les composants

**Actions principales:** vehiculer, transporter, acheminer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- climatisation inefficace
- traces de gras sur les raccords
- bruit de sifflement dans le circuit

## Procédure de Diagnostic

Pour diagnostiquer un problème de conduite de climatisation:

1. **Inspection visuelle** - Examiner l'état du conduite de climatisation
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- compresseur-de-climatisation
- condenseur-de-climatisation
- evaporateur-de-climatisation

## Critères de Compatibilité

Pour commander le bon conduite de climatisation, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidit instantanement"
