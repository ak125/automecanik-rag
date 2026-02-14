---
category: accessoires
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
  - actionner
  - tirer
  - ouvrir
  must_not_contain_concepts:
  - serrure
  - verrouillage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Permet l'ouverture de la porte depuis l'extérieur ou l'intérieur
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "securite garantie"
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
    question: Comment choisir Poignée de porte compatible avec mon vehicule ?
  - answer: En cas de poignee molle ou sans ressort ou de degradation mesurable, il
      faut controler rapidement avant panne secondaire.
    question: Quand remplacer Poignée de porte ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Poignée de porte sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Poignée de porte.
  id: 1373
  intro:
    role: Permet l'ouverture de la porte depuis l'extérieur ou l'intérieur
    syncParts:
    - actionner
    - tirer
    - ouvrir
    title: A quoi sert Poignée de porte ?
  pgId: '1373'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/poignee-de-porte.md
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
    title: Pourquoi remplacer Poignée de porte a temps ?
  symptoms:
  - poignee molle ou sans ressort
  - porte qui ne s ouvre plus de l exterieur
  - poignee cassee physiquement
  - '**Poignee cassee physiquement**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 1373
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: poignee-de-porte
source_type: gamme
symptoms:
- description: poignee molle ou sans ressort
  evidence:
  - 'Observation: poignee molle ou sans ressort'
  - Vérification visuelle ou auditive
  id: S1
  label: Poignee molle ou sans ressort
  risk_level: confort
- description: porte qui ne s ouvre plus de l exterieur
  evidence:
  - 'Observation: porte qui ne s ouvre plus de l exterieur'
  - Vérification visuelle ou auditive
  id: S2
  label: Porte qui ne s ouvre plus de l exterieur
  risk_level: confort
- description: poignee cassee physiquement
  evidence:
  - 'Observation: poignee cassee physiquement'
  - Vérification visuelle ou auditive
  id: S3
  label: Poignee cassee physiquement
  risk_level: degats_volant_moteur
title: Poignée de porte
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Poignée de porte - Guide Diagnostic Complet

## Fonction et Rôle

Permet l'ouverture de la porte depuis l'extérieur ou l'intérieur

**Actions principales:** actionner, tirer, ouvrir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Poignee cassee physiquement**
  poignee cassee physiquement

### 🟢 Autres Symptômes

- poignee molle ou sans ressort
- porte qui ne s ouvre plus de l exterieur

## Procédure de Diagnostic

Pour diagnostiquer un problème de poignée de porte:

1. **Inspection visuelle** - Examiner l'état du poignée de porte
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- serrure
- cable

## Critères de Compatibilité

Pour commander le bon poignée de porte, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"