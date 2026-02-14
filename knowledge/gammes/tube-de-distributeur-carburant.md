---
category: alimentation
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
  - distribuer
  - repartir
  - alimenter
  must_not_contain_concepts:
  - freinage
  - climatisation
  - distribution
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Repartir le carburant de la rampe vers chaque injecteur
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
    question: Comment choisir Tube de distributeur carburant compatible avec mon vehicule
      ?
  - answer: En cas de fuite de carburant sur la rampe ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Tube de distributeur carburant ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Tube de distributeur carburant sans verification atelier
      ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Tube de distributeur
    carburant.
  id: 3964
  intro:
    role: Repartir le carburant de la rampe vers chaque injecteur
    syncParts:
    - distribuer
    - repartir
    - alimenter
    title: A quoi sert Tube de distributeur carburant ?
  pgId: '3964'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/tube-de-distributeur-carburant.md
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
    title: Pourquoi remplacer Tube de distributeur carburant a temps ?
  symptoms:
  - fuite de carburant sur la rampe
  - odeur de gasoil ou essence
  - pression d injection instable
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 3964
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: tube-de-distributeur-carburant
source_type: gamme
symptoms:
- description: fuite de carburant sur la rampe
  evidence:
  - 'Observation: fuite de carburant sur la rampe'
  - Vérification visuelle ou auditive
  id: S1
  label: Fuite de carburant sur la rampe
  risk_level: confort
- description: odeur de gasoil ou essence
  evidence:
  - 'Observation: odeur de gasoil ou essence'
  - Vérification visuelle ou auditive
  id: S2
  label: Odeur de gasoil ou essence
  risk_level: confort
- description: pression d injection instable
  evidence:
  - 'Observation: pression d injection instable'
  - Vérification visuelle ou auditive
  id: S3
  label: Pression d injection instable
  risk_level: confort
title: Tube de distributeur carburant
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Tube de distributeur carburant - Guide Diagnostic Complet

## Fonction et Rôle

Repartir le carburant de la rampe vers chaque injecteur

**Actions principales:** distribuer, repartir, alimenter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- fuite de carburant sur la rampe
- odeur de gasoil ou essence
- pression d injection instable

## Procédure de Diagnostic

Pour diagnostiquer un problème de tube de distributeur carburant:

1. **Inspection visuelle** - Examiner l'état du tube de distributeur carburant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- rampe-d-injection
- injecteur

## Critères de Compatibilité

Pour commander le bon tube de distributeur carburant, vous devez connaître:

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