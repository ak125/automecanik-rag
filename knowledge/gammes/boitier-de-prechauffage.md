---
entity_type: gamme
title: Boîtier de préchauffage
slug: boitier-de-prechauffage
pg_id: 1750
category: allumage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Alimenter et controler les bougies de prechauffage diesel - Gere le temps et
    l'intensite de chauffe
  must_be_true:
    - alimenter
    - controler
    - commander
  must_not_contain_concepts:
    - essence
    - etincelle
    - haute tension
    - bobine
    - distributeur
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
symptoms:
  - id: S1
    label: Voyant prechauffage qui clignote ou reste allume
    description: voyant prechauffage qui clignote ou reste allume
    risk_level: confort
    evidence:
      - 'Observation: voyant prechauffage qui clignote ou reste allume'
      - Vérification visuelle ou auditive
  - id: S2
    label: Demarrage tres difficile par temps froid
    description: demarrage tres difficile par temps froid
    risk_level: confort
    evidence:
      - 'Observation: demarrage tres difficile par temps froid'
      - Vérification visuelle ou auditive
  - id: S3
    label: Fumee blanche excessive au demarrage a froid
    description: fumee blanche excessive au demarrage a froid
    risk_level: confort
    evidence:
      - 'Observation: fumee blanche excessive au demarrage a froid'
      - Vérification visuelle ou auditive
  - id: S4
    label: Bruit claquement diesel demarrage combustion
    description: bruit claquement diesel demarrage combustion
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit claquement diesel demarrage combustion'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de carburant non brule a l echappement
    description: odeur de carburant non brule a l echappement
    risk_level: confort
    evidence:
      - 'Observation: odeur de carburant non brule a l echappement'
      - Vérification visuelle ou auditive
  - id: S6
    label: Code defaut p0380 ou p0381 a la valise diagnostic
    description: code defaut p0380 ou p0381 a la valise diagnostic
    risk_level: confort
    evidence:
      - 'Observation: code defaut p0380 ou p0381 a la valise diagnostic'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Boîtier de préchauffage - Guide Diagnostic Complet

## Fonction et Rôle

Alimenter et controler les bougies de prechauffage diesel - Gere le temps et l'intensite de chauffe

**Actions principales:** alimenter, controler, commander, reguler, gerer le prechauffage

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit claquement diesel demarrage combustion**
  bruit claquement diesel demarrage combustion

### 🟢 Autres Symptômes

- voyant prechauffage qui clignote ou reste allume
- demarrage tres difficile par temps froid
- fumee blanche excessive au demarrage a froid
- odeur de carburant non brule a l echappement
- code defaut p0380 ou p0381 a la valise diagnostic

## Procédure de Diagnostic

Pour diagnostiquer un problème de boîtier de préchauffage:

1. **Inspection visuelle** - Examiner l'état du boîtier de préchauffage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- bougie-de-prechauffage
- demarreur

## Critères de Compatibilité

Pour commander le bon boîtier de préchauffage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"
