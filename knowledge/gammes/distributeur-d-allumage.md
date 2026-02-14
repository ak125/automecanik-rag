---
category: allumage
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
  - distribuer
  - repartir
  - transmettre
  must_not_contain_concepts:
  - freinage
  - climatisation
  - embrayage
  - direction
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Distribuer la haute tension aux bougies dans l'ordre d'allumage
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "demarrage instantane"
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
    question: Comment choisir Distributeur d'allumage compatible avec mon vehicule
      ?
  - answer: En cas de rates d allumage ou de degradation mesurable, il faut controler
      rapidement avant panne secondaire.
    question: Quand remplacer Distributeur d'allumage ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Distributeur d'allumage sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Distributeur d'allumage.
  id: 683
  intro:
    role: Distribuer la haute tension aux bougies dans l'ordre d'allumage
    syncParts:
    - distribuer
    - repartir
    - transmettre
    title: A quoi sert Distributeur d'allumage ?
  pgId: '683'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/distributeur-d-allumage.md
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
    title: Pourquoi remplacer Distributeur d'allumage a temps ?
  symptoms:
  - rates d allumage
  - demarrage difficile
  - manque de puissance
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 683
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: distributeur-d-allumage
source_type: gamme
symptoms:
- description: rates d allumage
  evidence:
  - 'Observation: rates d allumage'
  - Vérification visuelle ou auditive
  id: S1
  label: Rates d allumage
  risk_level: confort
- description: demarrage difficile
  evidence:
  - 'Observation: demarrage difficile'
  - Vérification visuelle ou auditive
  id: S2
  label: Demarrage difficile
  risk_level: confort
- description: manque de puissance
  evidence:
  - 'Observation: manque de puissance'
  - Vérification visuelle ou auditive
  id: S3
  label: Manque de puissance
  risk_level: confort
title: Distributeur d'allumage
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Distributeur d'allumage - Guide Diagnostic Complet

## Fonction et Rôle

Distribuer la haute tension aux bougies dans l'ordre d'allumage

**Actions principales:** distribuer, repartir, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- rates d allumage
- demarrage difficile
- manque de puissance

## Procédure de Diagnostic

Pour diagnostiquer un problème de distributeur d'allumage:

1. **Inspection visuelle** - Examiner l'état du distributeur d'allumage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bobine-d-allumage
- faisceau-d-allumage
- bougie-d-allumage

## Critères de Compatibilité

Pour commander le bon distributeur d'allumage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "demarrage instantane"