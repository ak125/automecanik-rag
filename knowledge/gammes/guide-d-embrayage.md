---
category: embrayage
diagnostic_tree:
- if: vibrations_anormales
  then: verifier_equilibrage_et_fixations
- if: kilometrage_eleve_ou_usure_visible
  then: remplacement_preventif_recommande
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - guider
  - centrer
  - positionner
  must_not_contain_concepts:
  - injection
  - freinage
  - climatisation
  - turbo
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Guider l'arbre primaire dans le volant moteur
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
    question: Comment choisir Guide d'embrayage compatible avec mon vehicule ?
  - answer: En cas de embrayage mal centre ou de degradation mesurable, il faut controler
      rapidement avant panne secondaire.
    question: Quand remplacer Guide d'embrayage ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Guide d'embrayage sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Guide d'embrayage.
  id: 4688
  intro:
    role: Guider l'arbre primaire dans le volant moteur
    syncParts:
    - guider
    - centrer
    - positionner
    title: A quoi sert Guide d'embrayage ?
  pgId: '4688'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/guide-d-embrayage.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure normale** - Après un certain kilométrage, le remplacement préventif
      est recommandé'
    - '**Défaillance progressive** - Usure normale due à l''utilisation'
    - '**Conditions d''utilisation** - Sollicitations excessives ou environnement
      défavorable'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure normale** - Après un certain kilométrage, le remplacement
      préventif est recommandé'
    title: Pourquoi remplacer Guide d'embrayage a temps ?
  symptoms:
  - embrayage mal centre
  - vibrations au demarrage
  - usure prematuree du disque
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 4688
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: guide-d-embrayage
source_type: gamme
symptoms:
- description: embrayage mal centre
  evidence:
  - 'Observation: embrayage mal centre'
  - Vérification visuelle ou auditive
  id: S1
  label: Embrayage mal centre
  risk_level: confort
- description: vibrations au demarrage
  evidence:
  - 'Observation: vibrations au demarrage'
  - Vérification visuelle ou auditive
  id: S2
  label: Vibrations au demarrage
  risk_level: confort
- description: usure prematuree du disque
  evidence:
  - 'Observation: usure prematuree du disque'
  - Vérification visuelle ou auditive
  id: S3
  label: Usure prematuree du disque
  risk_level: confort
title: Guide d'embrayage
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Guide d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Guider l'arbre primaire dans le volant moteur

**Actions principales:** guider, centrer, positionner

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- embrayage mal centre
- vibrations au demarrage
- usure prematuree du disque

## Procédure de Diagnostic

Pour diagnostiquer un problème de guide d'embrayage:

1. **Inspection visuelle** - Examiner l'état du guide d'embrayage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- fourchette-d-embrayage
- tringle-de-vitesses

## Critères de Compatibilité

Pour commander le bon guide d'embrayage, vous devez connaître:

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