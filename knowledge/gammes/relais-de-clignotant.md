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
  - commander
  - activer
  - cadencer
  must_not_contain_concepts:
  - ampoule
  - feu
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Commande le clignotement intermittent des feux de direction
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "visibilite parfaite"
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
    question: Comment choisir Relais de clignotant compatible avec mon vehicule ?
  - answer: En cas de clignotants ne fonctionnent pas ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Relais de clignotant ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Relais de clignotant sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Relais de clignotant.
  id: 61
  intro:
    role: Commande le clignotement intermittent des feux de direction
    syncParts:
    - commander
    - activer
    - cadencer
    title: A quoi sert Relais de clignotant ?
  pgId: '61'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/relais-de-clignotant.md
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
    title: Pourquoi remplacer Relais de clignotant a temps ?
  symptoms:
  - clignotants ne fonctionnent pas
  - clignotement trop rapide
  - clignotement irregulier
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 61
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: relais-de-clignotant
source_type: gamme
symptoms:
- description: clignotants ne fonctionnent pas
  evidence:
  - 'Observation: clignotants ne fonctionnent pas'
  - Vérification visuelle ou auditive
  id: S1
  label: Clignotants ne fonctionnent pas
  risk_level: confort
- description: clignotement trop rapide
  evidence:
  - 'Observation: clignotement trop rapide'
  - Vérification visuelle ou auditive
  id: S2
  label: Clignotement trop rapide
  risk_level: confort
- description: clignotement irregulier
  evidence:
  - 'Observation: clignotement irregulier'
  - Vérification visuelle ou auditive
  id: S3
  label: Clignotement irregulier
  risk_level: confort
title: Relais de clignotant
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Relais de clignotant - Guide Diagnostic Complet

## Fonction et Rôle

Commande le clignotement intermittent des feux de direction

**Actions principales:** commander, activer, cadencer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- clignotants ne fonctionnent pas
- clignotement trop rapide
- clignotement irregulier

## Procédure de Diagnostic

Pour diagnostiquer un problème de relais de clignotant:

1. **Inspection visuelle** - Examiner l'état du relais de clignotant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- feu-clignotant
- ampoule-feu-clignotant

## Critères de Compatibilité

Pour commander le bon relais de clignotant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "visibilite parfaite"