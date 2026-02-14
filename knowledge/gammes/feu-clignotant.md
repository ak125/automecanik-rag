---
category: eclairage
diagnostic_tree:
- if: symptome_general_detecte
  then: inspection_visuelle_et_test_fonctionnel
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - signaler
  - indiquer
  - clignoter
  must_not_contain_concepts:
  - injection
  - freinage
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Signale les changements de direction
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "meilleure visibilité"
  arguments:
  - content: Selection guidee par vehicule et references techniques.
    icon: check-circle
    title: Compatibilite verifiee
  - content: Un remplacement a temps limite les risques de panne secondaire.
    icon: shield-check
    title: Priorite securite
  - content: Le guide structure les controles avant commande.
    icon: clock
    title: Decision rapide
  - content: La verification des pieces associees reduit les retours atelier.
    icon: list-check
    title: Montage maitrise
  faq:
  - answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference
      exacte avant montage.
    question: Comment choisir Feu clignotant compatible avec mon vehicule ?
  - answer: En cas de clignotant lateral qui ne s allume plus ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Feu clignotant ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Feu clignotant sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Feu clignotant.
  id: 62
  intro:
    role: Feu clignotant intervient directement sur compatibilite du vehicule. Un
      choix conforme protege la securite et limite les pannes secondaires.
    syncParts:
    - signaler
    - indiquer
    - clignoter
    title: A quoi sert Feu clignotant ?
  pgId: '62'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/feu-clignotant.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Défaillance progressive** - Usure normale due à l''utilisation'
    - '**Conditions d''utilisation** - Sollicitations excessives ou environnement
      défavorable'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Défaillance progressive** - Usure normale due à l''utilisation'
    title: Pourquoi remplacer Feu clignotant a temps ?
  symptoms:
  - clignotant lateral qui ne s allume plus
  - clignotement rapide tableau bord ampoule
  - repetiteur casse ou fissure choc
  - eau ou buee visible dans le repetiteur
  - controle technique refuse signalisation defaillante
  - ampoule qui grille frequemment infiltration
  - clignotement plus rapide normale hyper
  - clignotant fonctionne intermittence maniere aleatoire
  - odeur plastique fondu court circuit
  - '**Repetiteur casse ou fissure choc**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 62
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: feu-clignotant
source_type: gamme
symptoms:
- description: clignotant lateral qui ne s allume plus
  evidence:
  - 'Observation: clignotant lateral qui ne s allume plus'
  - Vérification visuelle ou auditive
  id: S1
  label: Clignotant lateral qui ne s allume plus
  risk_level: confort
- description: clignotement rapide tableau bord ampoule
  evidence:
  - 'Observation: clignotement rapide tableau bord ampoule'
  - Vérification visuelle ou auditive
  id: S2
  label: Clignotement rapide tableau bord ampoule
  risk_level: confort
- description: repetiteur casse ou fissure choc
  evidence:
  - 'Observation: repetiteur casse ou fissure choc'
  - Vérification visuelle ou auditive
  id: S3
  label: Repetiteur casse ou fissure choc
  risk_level: degats_volant_moteur
- description: eau ou buee visible dans le repetiteur
  evidence:
  - 'Observation: eau ou buee visible dans le repetiteur'
  - Vérification visuelle ou auditive
  id: S4
  label: Eau ou buee visible dans le repetiteur
  risk_level: confort
- description: controle technique refuse signalisation defaillante
  evidence:
  - 'Observation: controle technique refuse signalisation defaillante'
  - Vérification visuelle ou auditive
  id: S5
  label: Controle technique refuse signalisation defaillante
  risk_level: confort
- description: ampoule qui grille frequemment infiltration
  evidence:
  - 'Observation: ampoule qui grille frequemment infiltration'
  - Vérification visuelle ou auditive
  id: S6
  label: Ampoule qui grille frequemment infiltration
  risk_level: confort
- description: clignotement plus rapide normale hyper
  evidence:
  - 'Observation: clignotement plus rapide normale hyper'
  - Vérification visuelle ou auditive
  id: S7
  label: Clignotement plus rapide normale hyper
  risk_level: confort
- description: clignotant fonctionne intermittence maniere aleatoire
  evidence:
  - 'Observation: clignotant fonctionne intermittence maniere aleatoire'
  - Vérification visuelle ou auditive
  id: S8
  label: Clignotant fonctionne intermittence maniere aleatoire
  risk_level: confort
- description: odeur plastique fondu court circuit
  evidence:
  - 'Observation: odeur plastique fondu court circuit'
  - Vérification visuelle ou auditive
  id: S9
  label: Odeur plastique fondu court circuit
  risk_level: confort
title: Feu clignotant
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Feu clignotant - Guide Diagnostic Complet

## Fonction et Rôle

Signale les changements de direction

**Actions principales:** signaler, indiquer, clignoter

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Repetiteur casse ou fissure choc**
  repetiteur casse ou fissure choc

### 🟢 Autres Symptômes

- clignotant lateral qui ne s allume plus
- clignotement rapide tableau bord ampoule
- eau ou buee visible dans le repetiteur
- controle technique refuse signalisation defaillante
- ampoule qui grille frequemment infiltration
- clignotement plus rapide normale hyper

## Procédure de Diagnostic

Pour diagnostiquer un problème de feu clignotant:

1. **Inspection visuelle** - Examiner l'état du feu clignotant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-clignotant
- commande-d-eclairage
- feu-arriere
- feu-avant

## Critères de Compatibilité

Pour commander le bon feu clignotant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleure visibilité"