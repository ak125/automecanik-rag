---
category: embrayage
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
  - guider
  - relier
  must_not_contain_concepts:
  - injection
  - freinage
  - climatisation
  - turbo
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Transmettre le mouvement du levier vers la boite
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "passage de vitesse parfait"
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
    question: Comment choisir Tringle de vitesses compatible avec mon vehicule ?
  - answer: En cas de vitesses dures a passer ou de degradation mesurable, il faut
      controler rapidement avant panne secondaire.
    question: Quand remplacer Tringle de vitesses ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Tringle de vitesses sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Tringle de vitesses.
  id: 1650
  intro:
    role: Transmettre le mouvement du levier vers la boite
    syncParts:
    - transmettre
    - guider
    - relier
    title: A quoi sert Tringle de vitesses ?
  pgId: '1650'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/tringle-de-vitesses.md
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
    title: Pourquoi remplacer Tringle de vitesses a temps ?
  symptoms:
  - vitesses dures a passer
  - levier de vitesses flottant
  - craquements au passage des rapports
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 1650
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: tringle-de-vitesses
source_type: gamme
symptoms:
- description: vitesses dures a passer
  evidence:
  - 'Observation: vitesses dures a passer'
  - Vérification visuelle ou auditive
  id: S1
  label: Vitesses dures a passer
  risk_level: confort
- description: levier de vitesses flottant
  evidence:
  - 'Observation: levier de vitesses flottant'
  - Vérification visuelle ou auditive
  id: S2
  label: Levier de vitesses flottant
  risk_level: confort
- description: craquements au passage des rapports
  evidence:
  - 'Observation: craquements au passage des rapports'
  - Vérification visuelle ou auditive
  id: S3
  label: Craquements au passage des rapports
  risk_level: confort
title: Tringle de vitesses
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Tringle de vitesses - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre le mouvement du levier vers la boite

**Actions principales:** transmettre, guider, relier

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- vitesses dures a passer
- levier de vitesses flottant
- craquements au passage des rapports

## Procédure de Diagnostic

Pour diagnostiquer un problème de tringle de vitesses:

1. **Inspection visuelle** - Examiner l'état du tringle de vitesses
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- fourchette-d-embrayage
- guide-d-embrayage

## Critères de Compatibilité

Pour commander le bon tringle de vitesses, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "passage de vitesse parfait"