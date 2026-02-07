---
entity_type: gamme
title: Courroie de distribution
slug: courroie-de-distribution
pg_id: 306
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
    Kit complet pour la synchronisation de la distribution avec tous les
    composants necessaires
  must_be_true:
    - synchroniser
    - entrainer
    - maintenir
  must_not_contain_concepts:
    - chaine
    - universel
    - tous moteurs
    - adaptable
  confusion_with:
    courroie-d-accessoire:
      key_difference: >-
        Courroie distribution = synchronise moteur (CRITIQUE), Courroie
        accessoire = alternateur/clim (moins critique)
    chaine-de-distribution:
      key_difference: 'Courroie = caoutchouc à remplacer, Chaîne = métal plus durable'
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
symptoms:
  - id: S1
    label: Aucun symptome visible courroie casse
    description: aucun symptome visible courroie casse
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: aucun symptome visible courroie casse'
      - Vérification visuelle ou auditive
  - id: S2
    label: Echeance kilometrique ou temps depassee
    description: echeance kilometrique ou temps depassee
    risk_level: confort
    evidence:
      - 'Observation: echeance kilometrique ou temps depassee'
      - Vérification visuelle ou auditive
  - id: S3
    label: Traces de craquelures sur la courroie si visible
    description: traces de craquelures sur la courroie si visible
    risk_level: confort
    evidence:
      - 'Observation: traces de craquelures sur la courroie si visible'
      - Vérification visuelle ou auditive
  - id: S4
    label: Bruit de claquement cote distribution
    description: bruit de claquement cote distribution
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit de claquement cote distribution'
      - Vérification visuelle ou auditive
  - id: S5
    label: Fuite de liquide de refroidissement pompe a eau
    description: fuite de liquide de refroidissement pompe a eau
    risk_level: confort
    evidence:
      - 'Observation: fuite de liquide de refroidissement pompe a eau'
      - Vérification visuelle ou auditive
  - id: S6
    label: Jeu dans le galet tendeur
    description: jeu dans le galet tendeur
    risk_level: confort
    evidence:
      - 'Observation: jeu dans le galet tendeur'
      - Vérification visuelle ou auditive
  - id: S7
    label: Courroie effilochee sur les bords
    description: courroie effilochee sur les bords
    risk_level: confort
    evidence:
      - 'Observation: courroie effilochee sur les bords'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous moteurs
    - adaptable
---
# Courroie de distribution - Guide Diagnostic Complet

## Fonction et Rôle

Kit complet pour la synchronisation de la distribution avec tous les composants necessaires

**Actions principales:** synchroniser, entrainer, maintenir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Aucun symptome visible courroie casse**
  aucun symptome visible courroie casse
- **Bruit de claquement cote distribution**
  bruit de claquement cote distribution

### 🟢 Autres Symptômes

- echeance kilometrique ou temps depassee
- traces de craquelures sur la courroie si visible
- fuite de liquide de refroidissement pompe a eau
- jeu dans le galet tendeur
- courroie effilochee sur les bords

## Procédure de Diagnostic

Pour diagnostiquer un problème de courroie de distribution:

1. **Inspection visuelle** - Examiner l'état du courroie de distribution
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-d-accessoire
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- kit-de-distribution
- pompe-a-eau
- poulie-d-arbre-a-came
- poulie-vilebrequin

## ⚠️ Ne Pas Confondre Avec

### courroie-d-accessoire
**Distinction:** Courroie distribution = synchronise moteur (CRITIQUE), Courroie accessoire = alternateur/clim (moins critique)

### chaine-de-distribution
**Distinction:** Courroie = caoutchouc à remplacer, Chaîne = métal plus durable

## Critères de Compatibilité

Pour commander le bon courroie de distribution, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Motorisation** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "évite la casse moteur"
- ❌ "sécurité garantie"
- ❌ "garanti CT"
