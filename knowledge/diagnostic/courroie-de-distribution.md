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
  - if: symptome_aucun-symptome-visible-courroie-casse
    then: verifier_piece
  - if: symptome_echeance-kilometrique-ou-temps-depassee
    then: diagnostic_approfondi
  - if: symptome_traces-de-craquelures-sur-la-courroie
    then: remplacement_recommande
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
    label: Traces de craquelures sur la courroie
    description: traces de craquelures sur la courroie si visible
    risk_level: confort
    evidence:
      - 'Observation: traces de craquelures sur la courroie'
      - Vérification visuelle ou auditive
  - id: S4
    label: Bruit de claquement cote distribution
    description: bruit de claquement cote distribution
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit de claquement cote distribution'
      - Vérification visuelle ou auditive
  - id: S5
    label: Fuite de liquide de refroidissement pompe
    description: fuite de liquide de refroidissement pompe a eau
    risk_level: confort
    evidence:
      - 'Observation: fuite de liquide de refroidissement pompe'
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
# Courroie de distribution - Guide Complet

## Fonction

Kit complet pour la synchronisation de la distribution avec tous les composants necessaires

## Symptômes de défaillance

### Aucun symptome visible courroie casse

aucun symptome visible courroie casse

### Echeance kilometrique ou temps depassee

echeance kilometrique ou temps depassee

### Traces de craquelures sur la courroie

traces de craquelures sur la courroie si visible

### Bruit de claquement cote distribution

bruit de claquement cote distribution

### Fuite de liquide de refroidissement pompe

fuite de liquide de refroidissement pompe a eau

### Jeu dans le galet tendeur

jeu dans le galet tendeur

### Courroie effilochee sur les bords

courroie effilochee sur les bords

## Diagnostic

Pour diagnostiquer un problème de courroie de distribution:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- courroie-d-accessoire
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- kit-de-distribution
- pompe-a-eau

## Ne pas confondre avec

| Pièce confondue | Distinction |
|-----------------|-------------|
| courroie-d-accessoire | Courroie distribution = synchronise moteur (CRITIQUE), Courroie accessoire = alternateur/clim (moins critique) |
| chaine-de-distribution | Courroie = caoutchouc à remplacer, Chaîne = métal plus durable |

## Compatibilité

Pour commander le bon courroie de distribution, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Motorisation** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "évite la casse moteur"
- ❌ "sécurité garantie"
- ❌ "garanti CT"
