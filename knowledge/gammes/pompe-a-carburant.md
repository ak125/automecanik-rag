---
category: alimentation
slug: pompe-a-carburant
title: Pompe à carburant
pg_id: 458
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-06'
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
  role: Acheminer le carburant du reservoir vers le systeme d'injection a basse pression
  must_be_true:
  - alimenter
  - acheminer
  - pomper
  must_not_contain:
  - haute pression
  - injection
  - injecteur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - alimenter
  - acheminer
  - pomper
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
  - ❌ "plus de puissance"
  cost_range:
    min: 29
    max: 224
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE (OES)
  - tier: Adaptable qualite
  - tier: Reconditionne
  - tier: Echange standard
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
    label: Moteur qui refuse de demarrer pas d amorcage
    severity: confort
  - id: S2
    label: Calages repetes a chaud ou en cote
    severity: immobilisation
  - id: S3
    label: A-coups a l acceleration
    severity: confort
  - id: S4
    label: Bruit de gemissement dans le reservoir
    severity: confort
  - id: S5
    label: Perte de puissance en montee
    severity: confort
  - id: S6
    label: Plus de 200 000 km ou reservoir souvent vide
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - remplacement preventif recommande
  quick_checks:
  - 'Observer : moteur qui refuse de demarrer pas d amorcage ?'
  - 'Observer : calages repetes a chaud ou en cote ?'
  - 'Observer : a-coups a l acceleration ?'
  - Bruit de gemissement dans le reservoir ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Moteur qui refuse de demarrer pas d amorcage
  - Calages repetes a chaud ou en cote
  - A-coups a l acceleration
  - Bruit de gemissement dans le reservoir
  - Perte de puissance en montee
  - Plus de 200 000 km ou reservoir souvent vide
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '458'
  intro_title: A quoi sert Pompe à carburant ?
  risk_title: Pourquoi remplacer Pompe à carburant a temps ?
  risk_explanation: '**Pièce HS** - Le pompe à carburant peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le pompe à carburant peut être hors service et nécessiter un remplacement'
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
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
  - question: Pompe à carburant OE ou adaptable ?
    answer: Les pompes OES (Bosch, Delphi, VDO) sont fiables. Sur diesel haute pression, privilégiez l'OE. Les adaptables
      essence de qualité (Pierburg) fonctionnent bien.
  - question: Comment savoir si ma pompe à carburant est HS ?
    answer: Moteur qui cale ou refuse de démarrer, à-coups à l'accélération, perte de puissance en côte, bruit de gémissement
      dans le réservoir.
  - question: Tous les combien changer la pompe à carburant ?
    answer: Pas de périodicité. Durée de vie 150 000 à 250 000 km. Évitez de rouler réservoir quasi vide (la pompe chauffe).
  - question: Peut-on changer la pompe à carburant soi-même ?
    answer: 'Possible mais attention : accès souvent sous la banquette arrière ou par le dessous. Circuit sous pression, risque
      d''incendie.'
  - question: Quelle erreur éviter avec la pompe à carburant ?
    answer: Ne pas rouler réservoir vide (la pompe s'use). Ne pas oublier le joint de module. Vérifier l'état du filtre dans
      le réservoir.
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
doc_id: df813cd6-9940-594e-87a9-a433f8efc709
content_hash: sha256:092935f81d78e868
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

# Pompe à carburant - Guide Diagnostic Complet

## Fonction et Rôle

Acheminer le carburant du reservoir vers le systeme d'injection a basse pression

**Actions principales:** alimenter, acheminer, pomper

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Calages repetes a chaud ou en cote**
  calages repetes a chaud ou en cote

### 🟢 Autres Symptômes

- moteur qui refuse de demarrer pas d amorcage
- a-coups a l acceleration
- bruit de gemissement dans le reservoir
- perte de puissance en montee
- plus de 200 000 km ou reservoir souvent vide

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à carburant:

1. **Inspection visuelle** - Examiner l'état du pompe à carburant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le pompe à carburant peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-pression-de-carburant
- filtre-a-carburant
- injecteur

## Critères de Compatibilité

Pour commander le bon pompe à carburant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"

## FAQ

**Pompe à carburant OE ou adaptable ?**
Les pompes OES (Bosch, Delphi, VDO) sont fiables. Sur diesel haute pression, privilégiez l'OE. Les adaptables essence de qualité (Pierburg) fonctionnent bien.

**Comment savoir si ma pompe à carburant est HS ?**
Moteur qui cale ou refuse de démarrer, à-coups à l'accélération, perte de puissance en côte, bruit de gémissement dans le réservoir.

**Tous les combien changer la pompe à carburant ?**
Pas de périodicité. Durée de vie 150 000 à 250 000 km. Évitez de rouler réservoir quasi vide (la pompe chauffe).

**Peut-on changer la pompe à carburant soi-même ?**
Possible mais attention : accès souvent sous la banquette arrière ou par le dessous. Circuit sous pression, risque d'incendie.

**Quelle erreur éviter avec la pompe à carburant ?**
Ne pas rouler réservoir vide (la pompe s'use). Ne pas oublier le joint de module. Vérifier l'état du filtre dans le réservoir.
