---
category: alimentation
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
  - amorcer
  - aspirer
  - preparer
  must_not_contain_concepts:
  - freinage
  - climatisation
  - distribution
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Amorcer le circuit carburant lors du demarrage a froid
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "repare l'injection"
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
    question: Comment choisir Pompe d'amorcage compatible avec mon vehicule ?
  - answer: En cas de demarrage difficile apres coupure moteur ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Pompe d'amorcage ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Pompe d'amorcage sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Pompe d'amorcage.
  id: 862
  intro:
    role: Amorcer le circuit carburant lors du demarrage a froid
    syncParts:
    - amorcer
    - aspirer
    - preparer
    title: A quoi sert Pompe d'amorcage ?
  pgId: '862'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/pompe-d-amorcage.md
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
    title: Pourquoi remplacer Pompe d'amorcage a temps ?
  symptoms:
  - demarrage difficile apres coupure moteur
  - poire molle sans resistance
  - bulles d air dans le circuit
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 862
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: pompe-d-amorcage
source_type: gamme
symptoms:
- description: demarrage difficile apres coupure moteur
  evidence:
  - 'Observation: demarrage difficile apres coupure moteur'
  - Vérification visuelle ou auditive
  id: S1
  label: Demarrage difficile apres coupure moteur
  risk_level: confort
- description: poire molle sans resistance
  evidence:
  - 'Observation: poire molle sans resistance'
  - Vérification visuelle ou auditive
  id: S2
  label: Poire molle sans resistance
  risk_level: confort
- description: bulles d air dans le circuit
  evidence:
  - 'Observation: bulles d air dans le circuit'
  - Vérification visuelle ou auditive
  id: S3
  label: Bulles d air dans le circuit
  risk_level: confort
title: Pompe d'amorcage
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Pompe d'amorcage - Guide Diagnostic Complet

## Fonction et Rôle

Amorcer le circuit carburant lors du demarrage a froid

**Actions principales:** amorcer, aspirer, preparer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- demarrage difficile apres coupure moteur
- poire molle sans resistance
- bulles d air dans le circuit

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe d'amorcage:

1. **Inspection visuelle** - Examiner l'état du pompe d'amorcage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- accumulateur-de-pression-de-carburant
- regulateur-de-pression-carburant
- soupape-de-rampe-commune-d-injection

## Critères de Compatibilité

Pour commander le bon pompe d'amorcage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare l'injection"