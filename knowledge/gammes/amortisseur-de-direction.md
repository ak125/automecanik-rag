---
category: direction
diagnostic_tree:
- if: vibrations_anormales
  then: verifier_equilibrage_et_fixations
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - amortir
  - stabiliser
  - filtrer
  must_not_contain_concepts:
  - injection
  - freinage
  - distribution
  - turbo
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Amortir les vibrations et chocs transmis au volant
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "direction parfaite"
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
    question: Comment choisir Amortisseur de direction compatible avec mon vehicule
      ?
  - answer: En cas de shimmy vibration du volant a certaines vitesses ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Amortisseur de direction ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Amortisseur de direction sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Amortisseur de
    direction.
  id: 130
  intro:
    role: Amortir les vibrations et chocs transmis au volant
    syncParts:
    - amortir
    - stabiliser
    - filtrer
    title: A quoi sert Amortisseur de direction ?
  pgId: '130'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/amortisseur-de-direction.md
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
    title: Pourquoi remplacer Amortisseur de direction a temps ?
  symptoms:
  - shimmy vibration du volant a certaines vitesses
  - direction qui tire d un cote
  - sensation de flottement dans la direction
  - '**Direction qui tire d un cote**'
  - '**Sensation de flottement dans la direction**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 130
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: amortisseur-de-direction
source_type: gamme
symptoms:
- description: shimmy vibration du volant a certaines vitesses
  evidence:
  - 'Observation: shimmy vibration du volant a certaines vitesses'
  - Vérification visuelle ou auditive
  id: S1
  label: Shimmy vibration du volant a certaines vitesses
  risk_level: confort
- description: direction qui tire d un cote
  evidence:
  - 'Observation: direction qui tire d un cote'
  - Vérification visuelle ou auditive
  id: S2
  label: Direction qui tire d un cote
  risk_level: securite
- description: sensation de flottement dans la direction
  evidence:
  - 'Observation: sensation de flottement dans la direction'
  - Vérification visuelle ou auditive
  id: S3
  label: Sensation de flottement dans la direction
  risk_level: securite
title: Amortisseur de direction
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Amortisseur de direction - Guide Diagnostic Complet

## Fonction et Rôle

Amortir les vibrations et chocs transmis au volant

**Actions principales:** amortir, stabiliser, filtrer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Direction qui tire d un cote**
  direction qui tire d un cote
- **Sensation de flottement dans la direction**
  sensation de flottement dans la direction

### 🟢 Autres Symptômes

- shimmy vibration du volant a certaines vitesses

## Procédure de Diagnostic

Pour diagnostiquer un problème de amortisseur de direction:

1. **Inspection visuelle** - Examiner l'état du amortisseur de direction
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- cremaillere-de-direction
- colonne-de-direction

## Critères de Compatibilité

Pour commander le bon amortisseur de direction, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "direction parfaite"