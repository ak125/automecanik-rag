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
  role_summary: Produit la lumière pour éclairer la route devant le véhicule
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
    question: Comment choisir Ampoule feu avant compatible avec mon vehicule ?
  - answer: En cas de phare ne fonctionne pas ou de degradation mesurable, il faut
      controler rapidement avant panne secondaire.
    question: Quand remplacer Ampoule feu avant ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Ampoule feu avant sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Ampoule feu avant.
  id: 107
  intro:
    role: Produit la lumière pour éclairer la route devant le véhicule
    syncParts:
    - produire
    - emettre
    - eclairer
    title: A quoi sert Ampoule feu avant ?
  pgId: '107'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/ampoule-feu-avant.md
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
    title: Pourquoi remplacer Ampoule feu avant a temps ?
  symptoms:
  - phare ne fonctionne pas
  - ampoule grillée
  - eclairage faible
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 107
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: ampoule-feu-avant
source_type: gamme
symptoms:
- description: phare ne fonctionne pas
  evidence:
  - 'Observation: phare ne fonctionne pas'
  - Vérification visuelle ou auditive
  id: S1
  label: Phare ne fonctionne pas
  risk_level: confort
- description: ampoule grillée
  evidence:
  - 'Observation: ampoule grillée'
  - Vérification visuelle ou auditive
  id: S2
  label: Ampoule grillée
  risk_level: confort
- description: eclairage faible
  evidence:
  - 'Observation: eclairage faible'
  - Vérification visuelle ou auditive
  id: S3
  label: Eclairage faible
  risk_level: confort
title: Ampoule feu avant
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Ampoule feu avant - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière pour éclairer la route devant le véhicule

**Actions principales:** produire, emettre, eclairer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- phare ne fonctionne pas
- ampoule grillée
- eclairage faible

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule feu avant:

1. **Inspection visuelle** - Examiner l'état du ampoule feu avant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-arriere
- ampoule-feu-clignotant
- ampoule-feu-de-position

## Critères de Compatibilité

Pour commander le bon ampoule feu avant, vous devez connaître:

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