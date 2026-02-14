---
category: eclairage
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
  - produire
  - emettre
  - signaler
  must_not_contain_concepts:
  - feu complet
  - optique
  - relais
  - commande
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Produit la lumière pour signaler la présence du véhicule à faible
    intensité
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
    question: Comment choisir Ampoule feu de position compatible avec mon vehicule
      ?
  - answer: En cas de feu de position eteint ou de degradation mesurable, il faut
      controler rapidement avant panne secondaire.
    question: Quand remplacer Ampoule feu de position ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Ampoule feu de position sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Ampoule feu de
    position.
  id: 2126
  intro:
    role: Produit la lumière pour signaler la présence du véhicule à faible intensité
    syncParts:
    - produire
    - emettre
    - signaler
    title: A quoi sert Ampoule feu de position ?
  pgId: '2126'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/ampoule-feu-de-position.md
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
    title: Pourquoi remplacer Ampoule feu de position a temps ?
  symptoms:
  - feu de position eteint
  - eclairage asymetrique
  - voyant au tableau de bord
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 2126
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: ampoule-feu-de-position
source_type: gamme
symptoms:
- description: feu de position eteint
  evidence:
  - 'Observation: feu de position eteint'
  - Vérification visuelle ou auditive
  id: S1
  label: Feu de position eteint
  risk_level: confort
- description: eclairage asymetrique
  evidence:
  - 'Observation: eclairage asymetrique'
  - Vérification visuelle ou auditive
  id: S2
  label: Eclairage asymetrique
  risk_level: confort
- description: voyant au tableau de bord
  evidence:
  - 'Observation: voyant au tableau de bord'
  - Vérification visuelle ou auditive
  id: S3
  label: Voyant au tableau de bord
  risk_level: confort
title: Ampoule feu de position
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Ampoule feu de position - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière pour signaler la présence du véhicule à faible intensité

**Actions principales:** produire, emettre, signaler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- feu de position eteint
- eclairage asymetrique
- voyant au tableau de bord

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule feu de position:

1. **Inspection visuelle** - Examiner l'état du ampoule feu de position
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-arriere
- ampoule-feu-avant
- ampoule-feu-clignotant

## Critères de Compatibilité

Pour commander le bon ampoule feu de position, vous devez connaître:

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