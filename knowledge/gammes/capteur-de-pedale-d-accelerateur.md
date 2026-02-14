---
category: capteurs
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
  - papillon
  - admission
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Mesurer la position de la pedale d'accelerateur et transmettre la
    demande du conducteur au calculateur
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
    question: Comment choisir Capteur de pédale d'accélérateur compatible avec mon
      vehicule ?
  - answer: En cas de accelerations irregulieres ou saccadees ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Capteur de pédale d'accélérateur ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Capteur de pédale d'accélérateur sans verification atelier
      ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Capteur de pédale
    d'accélérateur.
  id: 3908
  intro:
    role: Mesurer la position de la pedale d'accelerateur et transmettre la demande
      du conducteur au calculateur
    syncParts:
    - mesurer
    - detecter
    - transmettre
    title: A quoi sert Capteur de pédale d'accélérateur ?
  pgId: '3908'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/capteur-de-pedale-d-accelerateur.md
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
    title: Pourquoi remplacer Capteur de pédale d'accélérateur a temps ?
  symptoms:
  - accelerations irregulieres ou saccadees
  - mode degrade moteur active
  - voyant moteur avec code pedale
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 3908
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: capteur-de-pedale-d-accelerateur
source_type: gamme
symptoms:
- description: accelerations irregulieres ou saccadees
  evidence:
  - 'Observation: accelerations irregulieres ou saccadees'
  - Vérification visuelle ou auditive
  id: S1
  label: Accelerations irregulieres ou saccadees
  risk_level: confort
- description: mode degrade moteur active
  evidence:
  - 'Observation: mode degrade moteur active'
  - Vérification visuelle ou auditive
  id: S2
  label: Mode degrade moteur active
  risk_level: confort
- description: voyant moteur avec code pedale
  evidence:
  - 'Observation: voyant moteur avec code pedale'
  - Vérification visuelle ou auditive
  id: S3
  label: Voyant moteur avec code pedale
  risk_level: confort
title: Capteur de pédale d'accélérateur
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Capteur de pédale d'accélérateur - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la position de la pedale d'accelerateur et transmettre la demande du conducteur au calculateur

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- accelerations irregulieres ou saccadees
- mode degrade moteur active
- voyant moteur avec code pedale

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur de pédale d'accélérateur:

1. **Inspection visuelle** - Examiner l'état du capteur de pédale d'accélérateur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-position-papillon

## Critères de Compatibilité

Pour commander le bon capteur de pédale d'accélérateur, vous devez connaître:

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