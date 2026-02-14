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
  - maintenir
  - supporter
  - soulever
  must_not_contain_concepts:
  - serrure
  - verrouillage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Maintient le coffre ou hayon en position ouverte
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
    question: Comment choisir Vérin de coffre compatible avec mon vehicule ?
  - answer: En cas de coffre qui retombe lentement ou de degradation mesurable, il
      faut controler rapidement avant panne secondaire.
    question: Quand remplacer Vérin de coffre ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Vérin de coffre sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Vérin de coffre.
  id: 5032
  intro:
    role: Maintient le coffre ou hayon en position ouverte
    syncParts:
    - maintenir
    - supporter
    - soulever
    title: A quoi sert Vérin de coffre ?
  pgId: '5032'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/verin-de-coffre.md
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
    title: Pourquoi remplacer Vérin de coffre a temps ?
  symptoms:
  - coffre qui retombe lentement
  - coffre impossible a maintenir ouvert
  - verin qui fuit traces graisseuses
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 5032
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: verin-de-coffre
source_type: gamme
symptoms:
- description: coffre qui retombe lentement
  evidence:
  - 'Observation: coffre qui retombe lentement'
  - Vérification visuelle ou auditive
  id: S1
  label: Coffre qui retombe lentement
  risk_level: confort
- description: coffre impossible a maintenir ouvert
  evidence:
  - 'Observation: coffre impossible a maintenir ouvert'
  - Vérification visuelle ou auditive
  id: S2
  label: Coffre impossible a maintenir ouvert
  risk_level: confort
- description: verin qui fuit traces graisseuses
  evidence:
  - 'Observation: verin qui fuit traces graisseuses'
  - Vérification visuelle ou auditive
  id: S3
  label: Verin qui fuit traces graisseuses
  risk_level: confort
title: Vérin de coffre
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Vérin de coffre - Guide Diagnostic Complet

## Fonction et Rôle

Maintient le coffre ou hayon en position ouverte

**Actions principales:** maintenir, supporter, soulever

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- coffre qui retombe lentement
- coffre impossible a maintenir ouvert
- verin qui fuit traces graisseuses

## Procédure de Diagnostic

Pour diagnostiquer un problème de vérin de coffre:

1. **Inspection visuelle** - Examiner l'état du vérin de coffre
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- hayon
- charniere

## Critères de Compatibilité

Pour commander le bon vérin de coffre, vous devez connaître:

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