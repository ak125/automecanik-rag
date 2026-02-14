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
  - transmettre
  - actionner
  - commander
  must_not_contain_concepts:
  - injection
  - papillon electronique
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Transmet la commande d'accélération de la pédale au papillon
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "plus de puissance"
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
    question: Comment choisir Câble d'accélérateur compatible avec mon vehicule ?
  - answer: En cas de pedale d accelerateur dure ou rigide ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Câble d'accélérateur ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Câble d'accélérateur sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Câble d'accélérateur.
  id: 618
  intro:
    role: Transmet la commande d'accélération de la pédale au papillon
    syncParts:
    - transmettre
    - actionner
    - commander
    title: A quoi sert Câble d'accélérateur ?
  pgId: '618'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/cable-d-accelerateur.md
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
    title: Pourquoi remplacer Câble d'accélérateur a temps ?
  symptoms:
  - pedale d accelerateur dure ou rigide
  - reponse moteur retardee a l acceleration
  - point dur lors de l enfoncement de la pedale
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 618
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: cable-d-accelerateur
source_type: gamme
symptoms:
- description: pedale d accelerateur dure ou rigide
  evidence:
  - 'Observation: pedale d accelerateur dure ou rigide'
  - Vérification visuelle ou auditive
  id: S1
  label: Pedale d accelerateur dure ou rigide
  risk_level: confort
- description: reponse moteur retardee a l acceleration
  evidence:
  - 'Observation: reponse moteur retardee a l acceleration'
  - Vérification visuelle ou auditive
  id: S2
  label: Reponse moteur retardee a l acceleration
  risk_level: confort
- description: point dur lors de l enfoncement de la pedale
  evidence:
  - 'Observation: point dur lors de l enfoncement de la pedale'
  - Vérification visuelle ou auditive
  id: S3
  label: Point dur lors de l enfoncement de la pedale
  risk_level: confort
title: Câble d'accélérateur
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Câble d'accélérateur - Guide Diagnostic Complet

## Fonction et Rôle

Transmet la commande d'accélération de la pédale au papillon

**Actions principales:** transmettre, actionner, commander

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- pedale d accelerateur dure ou rigide
- reponse moteur retardee a l acceleration
- point dur lors de l enfoncement de la pedale

## Procédure de Diagnostic

Pour diagnostiquer un problème de câble d'accélérateur:

1. **Inspection visuelle** - Examiner l'état du câble d'accélérateur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- pedale
- papillon

## Critères de Compatibilité

Pour commander le bon câble d'accélérateur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"