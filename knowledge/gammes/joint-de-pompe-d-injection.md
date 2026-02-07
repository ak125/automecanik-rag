---
entity_type: gamme
title: Joint de pompe d'injection
slug: joint-de-pompe-d-injection
pg_id: 3893
category: alimentation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Assurer l'etancheite entre la pompe d'injection et le moteur
  must_be_true:
    - assurer l'etancheite
    - isoler
  must_not_contain_concepts:
    - freinage
    - climatisation
    - distribution
    - embrayage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
symptoms:
  - id: S1
    label: Fuite de gasoil sur la pompe
    description: fuite de gasoil sur la pompe
    risk_level: confort
    evidence:
      - 'Observation: fuite de gasoil sur la pompe'
      - Vérification visuelle ou auditive
  - id: S2
    label: Odeur de carburant au capot
    description: odeur de carburant au capot
    risk_level: confort
    evidence:
      - 'Observation: odeur de carburant au capot'
      - Vérification visuelle ou auditive
  - id: S3
    label: Baisse de pression d injection
    description: baisse de pression d injection
    risk_level: confort
    evidence:
      - 'Observation: baisse de pression d injection'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Joint de pompe d'injection - Guide Diagnostic Complet

## Fonction et Rôle

Assurer l'etancheite entre la pompe d'injection et le moteur

**Actions principales:** assurer l'etancheite, isoler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- fuite de gasoil sur la pompe
- odeur de carburant au capot
- baisse de pression d injection

## Procédure de Diagnostic

Pour diagnostiquer un problème de joint de pompe d'injection:

1. **Inspection visuelle** - Examiner l'état du joint de pompe d'injection
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- pompe-d-injection
- joint-d-etancheite

## Critères de Compatibilité

Pour commander le bon joint de pompe d'injection, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare l'injection"
