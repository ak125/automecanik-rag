---
entity_type: gamme
title: Kit de distribution
slug: kit-de-distribution
pg_id: 307
category: distribution
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Kit complet pour la distribution a chaine avec tous les composants (tendeur,
    patins, glissieres)
  must_be_true:
    - synchroniser
    - entrainer
    - guider
  must_not_contain_concepts:
    - courroie
    - caoutchouc
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Echeance kilometrique ou temps atteinte
    description: echeance kilometrique ou temps atteinte
    risk_level: confort
    evidence:
      - 'Observation: echeance kilometrique ou temps atteinte'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit de roulement cote distribution galet
    description: bruit de roulement cote distribution galet
    risk_level: confort
    evidence:
      - 'Observation: bruit de roulement cote distribution galet'
      - Vérification visuelle ou auditive
  - id: S3
    label: Fuite de liquide de refroidissement pompe a eau
    description: fuite de liquide de refroidissement pompe a eau
    risk_level: confort
    evidence:
      - 'Observation: fuite de liquide de refroidissement pompe a eau'
      - Vérification visuelle ou auditive
  - id: S4
    label: Sifflement au ralenti cote courroie
    description: sifflement au ralenti cote courroie
    risk_level: confort
    evidence:
      - 'Observation: sifflement au ralenti cote courroie'
      - Vérification visuelle ou auditive
  - id: S5
    label: Jeu dans les galets controle visuel
    description: jeu dans les galets controle visuel
    risk_level: confort
    evidence:
      - 'Observation: jeu dans les galets controle visuel'
      - Vérification visuelle ou auditive
  - id: S6
    label: Traces d usure sur la courroie
    description: traces d usure sur la courroie
    risk_level: confort
    evidence:
      - 'Observation: traces d usure sur la courroie'
      - Vérification visuelle ou auditive
  - id: S7
    label: Grincement au demarrage a froid
    description: grincement au demarrage a froid
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: grincement au demarrage a froid'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Kit de distribution - Guide Diagnostic Complet

## Fonction et Rôle

Kit complet pour la distribution a chaine avec tous les composants (tendeur, patins, glissieres)

**Actions principales:** synchroniser, entrainer, guider

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Grincement au demarrage a froid**
  grincement au demarrage a froid

### 🟢 Autres Symptômes

- echeance kilometrique ou temps atteinte
- bruit de roulement cote distribution galet
- fuite de liquide de refroidissement pompe a eau
- sifflement au ralenti cote courroie
- jeu dans les galets controle visuel
- traces d usure sur la courroie

## Procédure de Diagnostic

Pour diagnostiquer un problème de kit de distribution:

1. **Inspection visuelle** - Examiner l'état du kit de distribution
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-d-accessoire
- pompe-a-eau
- poulie-d-arbre-a-came
- poulie-vilebrequin

## Critères de Compatibilité

Pour commander le bon kit de distribution, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"
