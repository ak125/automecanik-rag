---
category: direction
diagnostic_tree:
- if: voyant_tableau_bord_allume
  then: lecture_codes_defaut_obd_et_diagnostic_electronique
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - mesurer
  - detecter
  - transmettre
  must_not_contain_concepts:
  - injection
  - freinage
  - distribution
  - turbo
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Mesurer l'angle de rotation du volant pour l'ESP
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
    question: Comment choisir Détecteur de l'angle de braquage compatible avec mon
      vehicule ?
  - answer: En cas de voyant esp allume en permanence ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Détecteur de l'angle de braquage ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Détecteur de l'angle de braquage sans verification atelier
      ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Détecteur de l'angle
    de braquage.
  id: 3252
  intro:
    role: Mesurer l'angle de rotation du volant pour l'ESP
    syncParts:
    - mesurer
    - detecter
    - transmettre
    title: A quoi sert Détecteur de l'angle de braquage ?
  pgId: '3252'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/detecteur-de-l-angle-de-braquage.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - '**Défaillance progressive** - Usure normale due à l''utilisation'
    - '**Conditions d''utilisation** - Sollicitations excessives ou environnement
      défavorable'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Défaillance électrique** - Problème de connexion, de câblage ou
      de composant électronique'
    title: Pourquoi remplacer Détecteur de l'angle de braquage a temps ?
  symptoms:
  - voyant esp allume en permanence
  - direction assistee desactivee
  - comportement anormal du vehicule en virage
  - '**Voyant esp allume en permanence**'
  - '**Direction assistee desactivee**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 3252
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: detecteur-de-l-angle-de-braquage
source_type: gamme
symptoms:
- description: voyant esp allume en permanence
  evidence:
  - 'Observation: voyant esp allume en permanence'
  - Vérification visuelle ou auditive
  id: S1
  label: Voyant esp allume en permanence
  risk_level: securite
- description: direction assistee desactivee
  evidence:
  - 'Observation: direction assistee desactivee'
  - Vérification visuelle ou auditive
  id: S2
  label: Direction assistee desactivee
  risk_level: securite
- description: comportement anormal du vehicule en virage
  evidence:
  - 'Observation: comportement anormal du vehicule en virage'
  - Vérification visuelle ou auditive
  id: S3
  label: Comportement anormal du vehicule en virage
  risk_level: confort
title: Détecteur de l'angle de braquage
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Détecteur de l'angle de braquage - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer l'angle de rotation du volant pour l'ESP

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Voyant esp allume en permanence**
  voyant esp allume en permanence
- **Direction assistee desactivee**
  direction assistee desactivee

### 🟢 Autres Symptômes

- comportement anormal du vehicule en virage

## Procédure de Diagnostic

Pour diagnostiquer un problème de détecteur de l'angle de braquage:

1. **Inspection visuelle** - Examiner l'état du détecteur de l'angle de braquage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- calculateur-esp
- capteur-abs

## Critères de Compatibilité

Pour commander le bon détecteur de l'angle de braquage, vous devez connaître:

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