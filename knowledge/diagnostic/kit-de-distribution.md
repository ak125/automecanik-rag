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
  - if: symptome_echeance-kilometrique-ou-temps-atteinte
    then: verifier_piece
  - if: symptome_bruit-de-roulement-cote-distribution-galet
    then: diagnostic_approfondi
  - if: symptome_fuite-de-liquide-de-refroidissement-pompe
    then: remplacement_recommande
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
    label: Fuite de liquide de refroidissement pompe
    description: fuite de liquide de refroidissement pompe a eau
    risk_level: confort
    evidence:
      - 'Observation: fuite de liquide de refroidissement pompe'
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
# Kit de distribution - Guide Complet

## Fonction

Kit complet pour la distribution a chaine avec tous les composants (tendeur, patins, glissieres)

## Symptômes de défaillance

### Echeance kilometrique ou temps atteinte

echeance kilometrique ou temps atteinte

### Bruit de roulement cote distribution galet

bruit de roulement cote distribution galet

### Fuite de liquide de refroidissement pompe

fuite de liquide de refroidissement pompe a eau

### Sifflement au ralenti cote courroie

sifflement au ralenti cote courroie

### Jeu dans les galets controle visuel

jeu dans les galets controle visuel

### Traces d usure sur la courroie

traces d usure sur la courroie

### Grincement au demarrage a froid

grincement au demarrage a froid

## Diagnostic

Pour diagnostiquer un problème de kit de distribution:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- courroie-d-accessoire
- pompe-a-eau
- poulie-d-arbre-a-came
- poulie-vilebrequin

## Compatibilité

Pour commander le bon kit de distribution, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
