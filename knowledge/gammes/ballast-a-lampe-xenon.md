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
  - alimenter
  - convertir
  - stabiliser
  must_not_contain_concepts:
  - ampoule
  - lampe
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Convertit et stabilise la tension électrique pour alimenter les ampoules
    xénon
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
    question: Comment choisir Ballast à lampe xénon compatible avec mon vehicule ?
  - answer: En cas de phare xenon ne s'allume pas ou de degradation mesurable, il
      faut controler rapidement avant panne secondaire.
    question: Quand remplacer Ballast à lampe xénon ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Ballast à lampe xénon sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Ballast à lampe
    xénon.
  id: 1431
  intro:
    role: Convertit et stabilise la tension électrique pour alimenter les ampoules
      xénon
    syncParts:
    - alimenter
    - convertir
    - stabiliser
    title: A quoi sert Ballast à lampe xénon ?
  pgId: '1431'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/ballast-a-lampe-xenon.md
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
    title: Pourquoi remplacer Ballast à lampe xénon a temps ?
  symptoms:
  - phare xenon ne s'allume pas
  - eclairage instable
  - phare qui clignote
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 1431
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: ballast-a-lampe-xenon
source_type: gamme
symptoms:
- description: phare xenon ne s'allume pas
  evidence:
  - 'Observation: phare xenon ne s''allume pas'
  - Vérification visuelle ou auditive
  id: S1
  label: Phare xenon ne s'allume pas
  risk_level: confort
- description: eclairage instable
  evidence:
  - 'Observation: eclairage instable'
  - Vérification visuelle ou auditive
  id: S2
  label: Eclairage instable
  risk_level: confort
- description: phare qui clignote
  evidence:
  - 'Observation: phare qui clignote'
  - Vérification visuelle ou auditive
  id: S3
  label: Phare qui clignote
  risk_level: confort
title: Ballast à lampe xénon
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Ballast à lampe xénon - Guide Diagnostic Complet

## Fonction et Rôle

Convertit et stabilise la tension électrique pour alimenter les ampoules xénon

**Actions principales:** alimenter, convertir, stabiliser

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- phare xenon ne s'allume pas
- eclairage instable
- phare qui clignote

## Procédure de Diagnostic

Pour diagnostiquer un problème de ballast à lampe xénon:

1. **Inspection visuelle** - Examiner l'état du ballast à lampe xénon
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-avant
- feu-avant

## Critères de Compatibilité

Pour commander le bon ballast à lampe xénon, vous devez connaître:

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