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
  - diriger
  - diffuser
  - eclairer
  must_not_contain_concepts:
  - ampoule seule
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Dirige la lumière pour améliorer la visibilité par temps de brouillard
    ou mauvaise visibilité
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
    question: Comment choisir Phares antibrouillard compatible avec mon vehicule ?
  - answer: En cas de antibrouillard inactif ou de degradation mesurable, il faut
      controler rapidement avant panne secondaire.
    question: Quand remplacer Phares antibrouillard ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Phares antibrouillard sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Phares antibrouillard.
  id: 289
  intro:
    role: Dirige la lumière pour améliorer la visibilité par temps de brouillard ou
      mauvaise visibilité
    syncParts:
    - diriger
    - diffuser
    - eclairer
    title: A quoi sert Phares antibrouillard ?
  pgId: '289'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/phares-antibrouillard.md
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
    title: Pourquoi remplacer Phares antibrouillard a temps ?
  symptoms:
  - antibrouillard inactif
  - eclairage faible ou jauni
  - optique fissuree ou embuee
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 289
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: phares-antibrouillard
source_type: gamme
symptoms:
- description: antibrouillard inactif
  evidence:
  - 'Observation: antibrouillard inactif'
  - Vérification visuelle ou auditive
  id: S1
  label: Antibrouillard inactif
  risk_level: confort
- description: eclairage faible ou jauni
  evidence:
  - 'Observation: eclairage faible ou jauni'
  - Vérification visuelle ou auditive
  id: S2
  label: Eclairage faible ou jauni
  risk_level: confort
- description: optique fissuree ou embuee
  evidence:
  - 'Observation: optique fissuree ou embuee'
  - Vérification visuelle ou auditive
  id: S3
  label: Optique fissuree ou embuee
  risk_level: confort
title: Phares antibrouillard
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Phares antibrouillard - Guide Diagnostic Complet

## Fonction et Rôle

Dirige la lumière pour améliorer la visibilité par temps de brouillard ou mauvaise visibilité

**Actions principales:** diriger, diffuser, eclairer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- antibrouillard inactif
- eclairage faible ou jauni
- optique fissuree ou embuee

## Procédure de Diagnostic

Pour diagnostiquer un problème de phares antibrouillard:

1. **Inspection visuelle** - Examiner l'état du phares antibrouillard
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-avant
- relais-phare

## Critères de Compatibilité

Pour commander le bon phares antibrouillard, vous devez connaître:

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