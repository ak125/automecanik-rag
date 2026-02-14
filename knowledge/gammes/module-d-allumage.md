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
  - piloter
  - commander
  - controler
  must_not_contain_concepts:
  - freinage
  - climatisation
  - embrayage
  - direction
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Commander electroniquement le moment d'allumage
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
    question: Comment choisir Module d'allumage compatible avec mon vehicule ?
  - answer: En cas de rates d allumage intermittents ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Module d'allumage ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Module d'allumage sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Module d'allumage.
  id: 1218
  intro:
    role: Commander electroniquement le moment d'allumage
    syncParts:
    - piloter
    - commander
    - controler
    title: A quoi sert Module d'allumage ?
  pgId: '1218'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/module-d-allumage.md
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
    title: Pourquoi remplacer Module d'allumage a temps ?
  symptoms:
  - rates d allumage intermittents
  - demarrage difficile
  - perte de puissance sur certains cylindres
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 1218
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: module-d-allumage
source_type: gamme
symptoms:
- description: rates d allumage intermittents
  evidence:
  - 'Observation: rates d allumage intermittents'
  - Vérification visuelle ou auditive
  id: S1
  label: Rates d allumage intermittents
  risk_level: confort
- description: demarrage difficile
  evidence:
  - 'Observation: demarrage difficile'
  - Vérification visuelle ou auditive
  id: S2
  label: Demarrage difficile
  risk_level: confort
- description: perte de puissance sur certains cylindres
  evidence:
  - 'Observation: perte de puissance sur certains cylindres'
  - Vérification visuelle ou auditive
  id: S3
  label: Perte de puissance sur certains cylindres
  risk_level: confort
title: Module d'allumage
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Module d'allumage - Guide Diagnostic Complet

## Fonction et Rôle

Commander electroniquement le moment d'allumage

**Actions principales:** piloter, commander, controler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- rates d allumage intermittents
- demarrage difficile
- perte de puissance sur certains cylindres

## Procédure de Diagnostic

Pour diagnostiquer un problème de module d'allumage:

1. **Inspection visuelle** - Examiner l'état du module d'allumage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bobine-d-allumage
- calculateur-moteur

## Critères de Compatibilité

Pour commander le bon module d'allumage, vous devez connaître:

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