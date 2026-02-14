---
category: refroidissement
diagnostic_tree:
- if: fuite_detectee_ou_niveau_bas
  then: identifier_origine_fuite_et_verifier_joints
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - fermer
  - reguler
  - proteger
  must_not_contain_concepts:
  - injection
  - freinage
  - embrayage
  - distribution
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Fermer le radiateur et reguler la pression du circuit
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "refroidissement optimal"
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
    question: Comment choisir Bouchon de radiateur compatible avec mon vehicule ?
  - answer: En cas de fuite de liquide par le bouchon ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Bouchon de radiateur ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Bouchon de radiateur sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Bouchon de radiateur.
  id: 548
  intro:
    role: Fermer le radiateur et reguler la pression du circuit
    syncParts:
    - fermer
    - reguler
    - proteger
    title: A quoi sert Bouchon de radiateur ?
  pgId: '548'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/bouchon-de-radiateur.md
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
    title: Pourquoi remplacer Bouchon de radiateur a temps ?
  symptoms:
  - fuite de liquide par le bouchon
  - surchauffe moteur sans fuite visible
  - pression excessive dans le circuit
  - '**Surchauffe moteur sans fuite visible**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 548
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: bouchon-de-radiateur
source_type: gamme
symptoms:
- description: fuite de liquide par le bouchon
  evidence:
  - 'Observation: fuite de liquide par le bouchon'
  - Vérification visuelle ou auditive
  id: S1
  label: Fuite de liquide par le bouchon
  risk_level: confort
- description: surchauffe moteur sans fuite visible
  evidence:
  - 'Observation: surchauffe moteur sans fuite visible'
  - Vérification visuelle ou auditive
  id: S2
  label: Surchauffe moteur sans fuite visible
  risk_level: degats_volant_moteur
- description: pression excessive dans le circuit
  evidence:
  - 'Observation: pression excessive dans le circuit'
  - Vérification visuelle ou auditive
  id: S3
  label: Pression excessive dans le circuit
  risk_level: confort
title: Bouchon de radiateur
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Bouchon de radiateur - Guide Diagnostic Complet

## Fonction et Rôle

Fermer le radiateur et reguler la pression du circuit

**Actions principales:** fermer, reguler, proteger

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Surchauffe moteur sans fuite visible**
  surchauffe moteur sans fuite visible

### 🟢 Autres Symptômes

- fuite de liquide par le bouchon
- pression excessive dans le circuit

## Procédure de Diagnostic

Pour diagnostiquer un problème de bouchon de radiateur:

1. **Inspection visuelle** - Examiner l'état du bouchon de radiateur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- radiateur
- durite-de-refroidissement

## Critères de Compatibilité

Pour commander le bon bouchon de radiateur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidissement optimal"