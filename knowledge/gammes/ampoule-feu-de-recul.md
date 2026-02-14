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
  - produire
  - emettre
  - eclairer
  must_not_contain_concepts:
  - feu complet
  - optique
  - relais
  - commande
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Produit la lumière pour signaler la marche arrière et éclairer derrière
    le véhicule
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
    question: Comment choisir Ampoule feu de recul compatible avec mon vehicule ?
  - answer: En cas de feu de recul inactif ou de degradation mesurable, il faut controler
      rapidement avant panne secondaire.
    question: Quand remplacer Ampoule feu de recul ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Ampoule feu de recul sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Ampoule feu de
    recul.
  id: 114
  intro:
    role: Produit la lumière pour signaler la marche arrière et éclairer derrière
      le véhicule
    syncParts:
    - produire
    - emettre
    - eclairer
    title: A quoi sert Ampoule feu de recul ?
  pgId: '114'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/ampoule-feu-de-recul.md
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
    title: Pourquoi remplacer Ampoule feu de recul a temps ?
  symptoms:
  - feu de recul inactif
  - camera de recul sans eclairage
  - stationnement nocturne difficile
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 114
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: ampoule-feu-de-recul
source_type: gamme
symptoms:
- description: feu de recul inactif
  evidence:
  - 'Observation: feu de recul inactif'
  - Vérification visuelle ou auditive
  id: S1
  label: Feu de recul inactif
  risk_level: confort
- description: camera de recul sans eclairage
  evidence:
  - 'Observation: camera de recul sans eclairage'
  - Vérification visuelle ou auditive
  id: S2
  label: Camera de recul sans eclairage
  risk_level: confort
- description: stationnement nocturne difficile
  evidence:
  - 'Observation: stationnement nocturne difficile'
  - Vérification visuelle ou auditive
  id: S3
  label: Stationnement nocturne difficile
  risk_level: confort
title: Ampoule feu de recul
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Ampoule feu de recul - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière pour signaler la marche arrière et éclairer derrière le véhicule

**Actions principales:** produire, emettre, eclairer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- feu de recul inactif
- camera de recul sans eclairage
- stationnement nocturne difficile

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule feu de recul:

1. **Inspection visuelle** - Examiner l'état du ampoule feu de recul
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- contacteur-feu-de-recul
- feu-arriere

## Critères de Compatibilité

Pour commander le bon ampoule feu de recul, vous devez connaître:

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