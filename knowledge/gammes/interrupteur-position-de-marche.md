---
category: capteurs
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
  - activer
  - commuter
  must_not_contain_concepts:
  - capteur
  - sonde
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Signaler la position de la boite de vitesses pour autoriser le demarrage
    ou activer les feux de recul
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "corrige la panne"
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
    question: Comment choisir Interrupteur position de marche compatible avec mon
      vehicule ?
  - answer: En cas de feux de recul qui ne s allument pas ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Interrupteur position de marche ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Interrupteur position de marche sans verification atelier
      ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Interrupteur position
    de marche.
  id: 2197
  intro:
    role: Signaler la position de la boite de vitesses pour autoriser le demarrage
      ou activer les feux de recul
    syncParts:
    - signaler
    - activer
    - commuter
    title: A quoi sert Interrupteur position de marche ?
  pgId: '2197'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/interrupteur-position-de-marche.md
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
    title: Pourquoi remplacer Interrupteur position de marche a temps ?
  symptoms:
  - feux de recul qui ne s allument pas
  - marche arriere non detectee par le calculateur
  - camera de recul inactive
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 2197
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: interrupteur-position-de-marche
source_type: gamme
symptoms:
- description: feux de recul qui ne s allument pas
  evidence:
  - 'Observation: feux de recul qui ne s allument pas'
  - Vérification visuelle ou auditive
  id: S1
  label: Feux de recul qui ne s allument pas
  risk_level: confort
- description: marche arriere non detectee par le calculateur
  evidence:
  - 'Observation: marche arriere non detectee par le calculateur'
  - Vérification visuelle ou auditive
  id: S2
  label: Marche arriere non detectee par le calculateur
  risk_level: confort
- description: camera de recul inactive
  evidence:
  - 'Observation: camera de recul inactive'
  - Vérification visuelle ou auditive
  id: S3
  label: Camera de recul inactive
  risk_level: confort
title: Interrupteur position de marche
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Interrupteur position de marche - Guide Diagnostic Complet

## Fonction et Rôle

Signaler la position de la boite de vitesses pour autoriser le demarrage ou activer les feux de recul

**Actions principales:** signaler, activer, commuter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- feux de recul qui ne s allument pas
- marche arriere non detectee par le calculateur
- camera de recul inactive

## Procédure de Diagnostic

Pour diagnostiquer un problème de interrupteur position de marche:

1. **Inspection visuelle** - Examiner l'état du interrupteur position de marche
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- contacteur-demarreur
- neiman

## Critères de Compatibilité

Pour commander le bon interrupteur position de marche, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "corrige la panne"