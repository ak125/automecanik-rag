---
category: capteurs
slug: interrupteur-position-de-marche
title: Interrupteur position de marche
pg_id: 2197
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
  role: Signaler la position de la boite de vitesses pour autoriser le demarrage ou activer les feux de recul
  must_be_true:
  - signaler
  - activer
  - commuter
  must_not_contain:
  - capteur
  - sonde
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - signaler
  - activer
  - commuter
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Marque de votre véhicule
  - Modele de votre véhicule
  - Annee de votre véhicule
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "corrige la panne"
  cost_range:
    min: 1000
    max: 5000
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Qualité Origine (OE)
    description: Interrupteurs de position fournis en première monte par les équipementiers des constructeurs. Contact électrique
      fiable, boîtier étanche adapté à l'environnement boîte de vitesses.
  - tier: Équivalent Qualité Origine
    description: Interrupteurs fabriqués selon les mêmes spécifications électriques et dimensionnelles que l'OE. Connecteur
      et brochage identiques.
  - tier: Adaptable Économique
    description: Interrupteurs de remplacement aux dimensions et brochage compatibles. Vérifier le type de filetage et le
      nombre de broches avant commande.
  brands:
    premium:
    - Stabilus
    - Valeo
    standard:
    - Febi
    - Meyle
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Feux de recul qui ne s allument pas
    severity: confort
  - id: S2
    label: Marche arriere non detectee par le calculateur
    severity: confort
  - id: S3
    label: Camera de recul inactive
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : feux de recul qui ne s allument pas'
  quick_checks:
  - 'Observer : feux de recul qui ne s allument pas ?'
  - 'Observer : marche arriere non detectee par le calculateur ?'
  - 'Observer : camera de recul inactive ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Feux de recul qui ne s allument pas
  - Marche arriere non detectee par le calculateur
  - Camera de recul inactive
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '2197'
  intro_title: A quoi sert Interrupteur position de marche ?
  risk_title: Pourquoi remplacer Interrupteur position de marche a temps ?
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
  - question: Comment choisir Interrupteur position de marche compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Interrupteur position de marche ?
    answer: En cas de feux de recul qui ne s allument pas ou de degradation mesurable, il faut controler rapidement avant
      panne secondaire.
  - question: Puis-je monter Interrupteur position de marche sans verification atelier ?
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
doc_id: b11dccef-5a95-5fc3-9571-683c088cf1b6
content_hash: sha256:b809af197e47d9bf
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
  area: Sur le vehicule (position variable selon modele)
  access: Consulter la revue technique du vehicule
  adjacent_parts:
  - pieces adjacentes du meme systeme
installation:
  difficulty: variable
  time: consulter revue technique
  tools:
  - outillage standard
  prerequisite: Consulter la procedure constructeur
---

# Interrupteur position de marche - Guide Diagnostic Complet

## Fonction et Rôle

Signaler la position de la boite de vitesses pour autoriser le demarrage ou activer les feux de recul

**Actions principales:** signaler, activer, commuter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- feux de recul qui ne s allument pas
- marche arriere non detectee par le calculateur
- camera de recul inactive

## Procédure de Diagnostic

Pour diagnostiquer un problème de interrupteur position de marche:

1. **Inspection visuelle** - Examiner l'état du interrupteur position de marche
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

- contacteur-demarreur
- neiman

## Critères de Compatibilité

Pour commander le bon interrupteur position de marche, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "corrige la panne"

## FAQ

**Comment choisir Interrupteur position de marche compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Interrupteur position de marche ?**
En cas de feux de recul qui ne s allument pas ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Interrupteur position de marche sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
