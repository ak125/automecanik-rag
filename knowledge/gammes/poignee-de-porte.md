---
category: accessoires
slug: poignee-de-porte
title: Poignée de porte
pg_id: 1373
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-01'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v4_converted
  last_enriched_by: script:rag-fill-remaining-gaps
  last_enriched_at: '2026-03-28'
domain:
  role: Permet l'ouverture de la porte depuis l'extérieur ou l'intérieur
  must_be_true:
  - actionner
  - tirer
  - ouvrir
  must_not_contain:
  - serrure
  - verrouillage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - verin-capot-moteur
  - verin-de-coffre
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de compatibilite
    pour confirmer Poignée de porte.
  - Verifier la reference OE ou equivalence constructeur pour le vehicule exact
  - Comparer les dimensions et le type de montage avec la piece d origine
  - Choisir un equipementier reconnu pour garantir qualite et compatibilite
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "securite garantie"
  cost_range:
    min: 15
    max: 80
    currency: EUR
    unit: l'unite
    source: estimation categorie
  brands:
    premium:
    - Stabilus
    standard:
    - Febi
    - Meyle
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Poignee molle ou sans ressort
    severity: confort
  - id: S2
    label: Porte qui ne s ouvre plus de l exterieur
    severity: confort
  - id: S3
    label: Poignee cassee physiquement
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'Usure ou defaillance causant : poignee molle ou sans ressort'
  - 'Usure ou defaillance causant : porte qui ne s ouvre plus de l exterieur'
  quick_checks:
  - 'Observer : poignee molle ou sans ressort ?'
  - 'Observer : porte qui ne s ouvre plus de l exterieur ?'
  - 'Observer : poignee cassee physiquement ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Poignee molle ou sans ressort
  - Porte qui ne s ouvre plus de l exterieur
  - Poignee cassee physiquement
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '1373'
  intro_title: A quoi sert Poignée de porte ?
  risk_title: Pourquoi remplacer Poignée de porte a temps ?
  risk_explanation: '**Défaillance progressive** - Usure normale due à l''utilisation'
  risk_consequences:
  - '**Défaillance progressive** - Usure normale due à l''utilisation'
  - '**Conditions d''utilisation** - Sollicitations excessives ou environnement défavorable'
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  risk_conclusion: Un diagnostic precoce reduit le risque technique et financier.
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
  - question: Comment choisir Poignée de porte compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Poignée de porte ?
    answer: En cas de poignee molle ou sans ressort ou de degradation mesurable, il faut controler rapidement avant panne
      secondaire.
  - question: Puis-je monter Poignée de porte sans verification atelier ?
    answer: Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure
      constructeur.
  quality:
    score: 76
    source: script:rag-upgrade-v4
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
doc_id: 260cfb18-f40b-57f4-a89d-2116031bfd7d
content_hash: sha256:ecf306cde62544fc
lang: fr
variants:
- name: Version OE (origine)
  aliases:
  - OE
  - constructeur
  functional_differences:
  - Reference constructeur exacte
  - Garantie et compatibilite maximales
- name: Version equivalente OES
  aliases:
  - OES
  - equipementier
  functional_differences:
  - Qualite equivalente, prix aftermarket
  - Equipementier de premier monte
location_on_vehicle:
  area: Sur la carrosserie (capot, coffre, portes)
  access: Accessible directement sans outil special
  adjacent_parts:
  - charniere
  - serrure
  - cable
  - joint
installation:
  difficulty: facile
  time: 10 a 30 min
  tools:
  - tournevis
  - cle plate
  - clip de fixation
  prerequisite: Aucun prerequis special
---

# Poignée de porte - Guide Diagnostic Complet

## Fonction et Rôle

Permet l'ouverture de la porte depuis l'extérieur ou l'intérieur

**Actions principales:** actionner, tirer, ouvrir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Poignee cassee physiquement**
  poignee cassee physiquement

### 🟢 Autres Symptômes

- poignee molle ou sans ressort
- porte qui ne s ouvre plus de l exterieur

## Procédure de Diagnostic

Pour diagnostiquer un problème de poignée de porte:

1. **Inspection visuelle** - Examiner l'état du poignée de porte
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- serrure
- cable

## Critères de Compatibilité

Pour commander le bon poignée de porte, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"

## FAQ

**Comment choisir Poignée de porte compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Poignée de porte ?**
En cas de poignee molle ou sans ressort ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Poignée de porte sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
