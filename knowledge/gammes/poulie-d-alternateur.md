---
entity_type: gamme
title: Poulie d'alternateur
slug: poulie-d-alternateur
pg_id: 1108
category: distribution
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmet le mouvement à l'alternateur
  must_be_true:
    - entrainer
    - transmettre
  must_not_contain_concepts:
    - freinage
    - climatisation
    - turbo
    - injection
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
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Sifflement aigu au demarrage a froid
    description: sifflement aigu au demarrage a froid
    risk_level: confort
    evidence:
      - 'Observation: sifflement aigu au demarrage a froid'
      - Vérification visuelle ou auditive
  - id: S2
    label: Courroie d accessoire qui saute ou patine
    description: courroie d accessoire qui saute ou patine
    risk_level: confort
    evidence:
      - 'Observation: courroie d accessoire qui saute ou patine'
      - Vérification visuelle ou auditive
  - id: S3
    label: Vibrations moteur au ralenti
    description: vibrations moteur au ralenti
    risk_level: confort
    evidence:
      - 'Observation: vibrations moteur au ralenti'
      - Vérification visuelle ou auditive
  - id: S4
    label: Bruit de roulement au niveau de l alternateur
    description: bruit de roulement au niveau de l alternateur
    risk_level: confort
    evidence:
      - 'Observation: bruit de roulement au niveau de l alternateur'
      - Vérification visuelle ou auditive
  - id: S5
    label: Alternateur qui charge mal par intermittence
    description: alternateur qui charge mal par intermittence
    risk_level: confort
    evidence:
      - 'Observation: alternateur qui charge mal par intermittence'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 120 000 km sans remplacement
    description: plus de 120 000 km sans remplacement
    risk_level: confort
    evidence:
      - 'Observation: plus de 120 000 km sans remplacement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Poulie d'alternateur - Guide Diagnostic Complet

## Fonction et Rôle

Transmet le mouvement à l'alternateur

**Actions principales:** entrainer, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- sifflement aigu au demarrage a froid
- courroie d accessoire qui saute ou patine
- vibrations moteur au ralenti
- bruit de roulement au niveau de l alternateur
- alternateur qui charge mal par intermittence
- plus de 120 000 km sans remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de poulie d'alternateur:

1. **Inspection visuelle** - Examiner l'état du poulie d'alternateur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- courroie-d-accessoire
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- poulie-vilebrequin

## Critères de Compatibilité

Pour commander le bon poulie d'alternateur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleure charge"
