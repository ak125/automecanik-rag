---
category: capteurs
slug: valve-de-reglage-du-ralenti
title: Valve de réglage du ralenti
pg_id: 1298
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
  role: Reguler le debit d'air au ralenti pour maintenir un regime stable moteur chaud ou froid
  must_be_true:
  - reguler
  - ouvrir
  - fermer
  must_not_contain:
  - capteur
  - sonde
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - reguler
  - ouvrir
  - fermer
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
    min: 30
    max: 100
    currency: EUR
    unit: vanne
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    description: Valve identique au premier montage. Calibration du moteur pas-à-pas et débit d'air conformes aux paramètres
      du calculateur d'origine.
  - tier: Équivalent OE (OES)
    description: Fabricants comme Bosch, Pierburg ou VDO fournissent ces valves aux constructeurs en première monte. Même
      calibration et même connectique.
  - tier: Adaptable (aftermarket)
    description: Valves aftermarket compatibles. Vérifier le type de connecteur, le nombre de broches et le diamètre du corps
      avant commande.
  brands:
    premium:
    - Bosch
    - Delphi
    - Denso
    standard:
    - Pierburg
    - VDO
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Ralenti instable ou irregulier
    severity: confort
  - id: S2
    label: Regime ralenti trop haut ou trop bas
    severity: confort
  - id: S3
    label: Moteur qui cale au ralenti ou au feu rouge
    severity: immobilisation
  - id: S4
    label: Sifflement ou bruit d aspirtion d air anormal
    severity: confort
  - id: S5
    label: Odeur d essence au ralenti melange trop riche
    severity: confort
  - id: S6
    label: Plus nettoyage boitier papillon
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - 'vehicule immobilise ou symptome critique : verification urgente piece et alimentation'
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  quick_checks:
  - 'Observer : ralenti instable ou irregulier ?'
  - 'Observer : regime ralenti trop haut ou trop bas ?'
  - 'Observer : moteur qui cale au ralenti ou au feu rouge ?'
  - 'Observer : sifflement ou bruit d aspirtion d air anormal ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Ralenti instable ou irregulier
  - Regime ralenti trop haut ou trop bas
  - Moteur qui cale au ralenti ou au feu rouge
  - Sifflement ou bruit d aspirtion d air anormal
  - Odeur d essence au ralenti melange trop riche
  - Plus nettoyage boitier papillon
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '1298'
  intro_title: A quoi sert Valve de réglage du ralenti ?
  risk_title: Pourquoi remplacer Valve de réglage du ralenti a temps ?
  risk_explanation: '**Pièce HS** - Le valve de réglage du ralenti peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le valve de réglage du ralenti peut être hors service et nécessiter un remplacement'
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: Vanne de ralenti OE ou adaptable ?
    answer: Les vannes OES (Bosch, Valeo) sont recommandées. Les adaptables peuvent avoir un débit différent causant des problèmes
      de ralenti.
  - question: Comment savoir si ma vanne de ralenti est HS ?
    answer: Ralenti instable ou trop haut, moteur qui cale au ralenti, régime qui monte et descend seul, voyant moteur avec
      codes P0505-P0509.
  - question: Tous les combien changer la vanne de ralenti ?
    answer: Pas de périodicité. Durée de vie variable selon encrassement. Un nettoyage tous les 50 000 km prolonge sa durée
      de vie.
  - question: Peut-on changer la vanne de ralenti soi-même ?
    answer: Oui, généralement accessible sur le boîtier papillon. Quelques vis, un connecteur. Nettoyage du boîtier recommandé
      en même temps.
  - question: Quelle erreur éviter avec la vanne de ralenti ?
    answer: Essayer le nettoyage avant le remplacement. Vérifier aussi le boîtier papillon et le capteur de position papillon.
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
doc_id: 70e66768-fdc2-57d8-bcb8-8db45dd0bb3f
content_hash: sha256:da9066d2aa5c39a1
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

# Valve de réglage du ralenti - Guide Diagnostic Complet

## Fonction et Rôle

Reguler le debit d'air au ralenti pour maintenir un regime stable moteur chaud ou froid

**Actions principales:** reguler, ouvrir, fermer, doser

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Moteur qui cale au ralenti ou au feu rouge**
  moteur qui cale au ralenti ou au feu rouge

### 🟢 Autres Symptômes

- ralenti instable ou irregulier
- regime ralenti trop haut ou trop bas
- sifflement ou bruit d aspirtion d air anormal
- odeur d essence au ralenti melange trop riche
- plus nettoyage boitier papillon

## Procédure de Diagnostic

Pour diagnostiquer un problème de valve de réglage du ralenti:

1. **Inspection visuelle** - Examiner l'état du valve de réglage du ralenti
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le valve de réglage du ralenti peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes

## Pièces Associées

Lors du remplacement, vérifier également:

- corps-papillon
- filtre-a-air

## Critères de Compatibilité

Pour commander le bon valve de réglage du ralenti, vous devez connaître:

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

**Vanne de ralenti OE ou adaptable ?**
Les vannes OES (Bosch, Valeo) sont recommandées. Les adaptables peuvent avoir un débit différent causant des problèmes de ralenti.

**Comment savoir si ma vanne de ralenti est HS ?**
Ralenti instable ou trop haut, moteur qui cale au ralenti, régime qui monte et descend seul, voyant moteur avec codes P0505-P0509.

**Tous les combien changer la vanne de ralenti ?**
Pas de périodicité. Durée de vie variable selon encrassement. Un nettoyage tous les 50 000 km prolonge sa durée de vie.

**Peut-on changer la vanne de ralenti soi-même ?**
Oui, généralement accessible sur le boîtier papillon. Quelques vis, un connecteur. Nettoyage du boîtier recommandé en même temps.

**Quelle erreur éviter avec la vanne de ralenti ?**
Essayer le nettoyage avant le remplacement. Vérifier aussi le boîtier papillon et le capteur de position papillon.
