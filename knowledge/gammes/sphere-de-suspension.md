---
category: suspension
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
  - stabiliser hydrauliquement
  - reguler la pression
  - amortir hydrauliquement
  must_not_contain_concepts:
  - ressort helicoidale
  - amortisseur classique
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Assurer la suspension via pression hydraulique et gaz (systeme Citroen).
    Remplace amortisseur ET ressort. NE FONCTIONNE PAS COMME UN RESSORT CLASSIQUE!
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "tenue de route parfaite"
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
    question: Comment choisir Sphère de suspension compatible avec mon vehicule ?
  - answer: En cas de suspension tres dure ou de degradation mesurable, il faut controler
      rapidement avant panne secondaire.
    question: Quand remplacer Sphère de suspension ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Sphère de suspension sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de suspension pour confirmer Sphère de suspension.
  id: 1718
  intro:
    role: Assurer la suspension via pression hydraulique et gaz (systeme Citroen).
      Remplace amortisseur ET ressort. NE FONCTIONNE PAS COMME UN RESSORT CLASSIQUE!
    syncParts:
    - stabiliser hydrauliquement
    - reguler la pression
    - amortir hydrauliquement
    title: A quoi sert Sphère de suspension ?
  pgId: '1718'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - MISSING_REQUIRED_TERMS
    - TOO_SHORT
    score: 60
    source: reindex:gammes/sphere-de-suspension.md
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
    title: Pourquoi remplacer Sphère de suspension a temps ?
  symptoms:
  - suspension tres dure
  - vehicule qui ne monte plus en hauteur
  - confort de roulement degrade
  - '**Suspension tres dure**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 1718
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: sphere-de-suspension
source_type: gamme
symptoms:
- description: suspension tres dure
  evidence:
  - 'Observation: suspension tres dure'
  - Vérification visuelle ou auditive
  id: S1
  label: Suspension tres dure
  risk_level: securite
- description: vehicule qui ne monte plus en hauteur
  evidence:
  - 'Observation: vehicule qui ne monte plus en hauteur'
  - Vérification visuelle ou auditive
  id: S2
  label: Vehicule qui ne monte plus en hauteur
  risk_level: confort
- description: confort de roulement degrade
  evidence:
  - 'Observation: confort de roulement degrade'
  - Vérification visuelle ou auditive
  id: S3
  label: Confort de roulement degrade
  risk_level: confort
title: Sphère de suspension
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Sphère de suspension - Guide Diagnostic Complet

## Fonction et Rôle

Assurer la suspension via pression hydraulique et gaz (systeme Citroen). Remplace amortisseur ET ressort. NE FONCTIONNE PAS COMME UN RESSORT CLASSIQUE!

**Actions principales:** stabiliser hydrauliquement, reguler la pression, amortir hydrauliquement, maintenir la hauteur

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Suspension tres dure**
  suspension tres dure

### 🟢 Autres Symptômes

- vehicule qui ne monte plus en hauteur
- confort de roulement degrade

## Procédure de Diagnostic

Pour diagnostiquer un problème de sphère de suspension:

1. **Inspection visuelle** - Examiner l'état du sphère de suspension
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- amortisseur
- suspension

## Critères de Compatibilité

Pour commander le bon sphère de suspension, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "tenue de route parfaite"