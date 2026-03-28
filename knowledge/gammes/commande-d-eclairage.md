---
category: eclairage
slug: commande-d-eclairage
title: Commande d'éclairage
pg_id: 809
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
  last_enriched_by: script:rag-enrich-metier-templates
  last_enriched_at: '2026-03-26'
domain:
  role: Commande les différents feux du véhicule
  must_be_true:
  - commander
  - activer
  - regler
  must_not_contain:
  - injection
  - freinage
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - ampoule-feu-avant
  - ampoule-feu-arriere
  - feu-avant
  - feu-arriere
  - phares-antibrouillard
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
  - ❌ "meilleur éclairage"
  cost_range:
    min: 40
    max: 200
    currency: EUR
    unit: commodo
    source: catalogue automecanik
  quality_tiers:
  - tier: Constructeur (OE)
    description: 'Commodo d''origine : connecteurs, fonctions (veille, croisement, route, antibrouillard, correcteur) et codage
      calculateur conformes au véhicule.'
  - tier: Équivalent OE (OES)
    description: 'Équipementiers reconnus dans ce segment : Valeo, Hella, TRW. Commodos avec connecteurs conformes et fonctions
      vérifiées par correspondance de référence.'
  - tier: Adaptable
    description: Commodos génériques avec risque de fonctions manquantes ou de connecteurs légèrement différents. Peut nécessiter
      adaptation.
  brands:
    premium:
    - Osram
    - Philips
    standard:
    - Bosch
    - Hella
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Feux croisement route allument plus
    severity: confort
  - id: S2
    label: Commodo bloque ou difficile a tourner
    severity: immobilisation
  - id: S3
    label: Fonctions aleatoires s allument puis s eteignent
    severity: confort
  - id: S4
    label: Clignotants fonctionnent plus depuis commodo
    severity: confort
  - id: S5
    label: Bruit de craquement en actionnant l interrupteur
    severity: confort
  - id: S6
    label: Fusibles ok mais feux inoperants
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - 'vehicule immobilise ou symptome critique : verification urgente piece et alimentation'
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  quick_checks:
  - 'Observer : feux croisement route allument plus ?'
  - 'Observer : commodo bloque ou difficile a tourner ?'
  - 'Observer : fonctions aleatoires s allument puis s eteignent ?'
  - 'Observer : clignotants fonctionnent plus depuis commodo ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Feux croisement route allument plus
  - Commodo bloque ou difficile a tourner
  - Fonctions aleatoires s allument puis s eteignent
  - Clignotants fonctionnent plus depuis commodo
  - Bruit de craquement en actionnant l interrupteur
  - Fusibles ok mais feux inoperants
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '809'
  intro_title: A quoi sert Commande d'éclairage ?
  risk_title: Pourquoi remplacer Commande d'éclairage a temps ?
  risk_explanation: '**Pièce HS** - Le commande d''éclairage peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le commande d''éclairage peut être hors service et nécessiter un remplacement'
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
  - question: Commande d'éclairage OE ou adaptable ?
    answer: Privilégiez l'OE ou OES (Valeo, Hella). Le commodo doit être parfaitement compatible avec votre véhicule (connecteurs,
      fonctions). Les adaptables peuvent avoir des incompatibilités.
  - question: Comment savoir si ma commande d'éclairage est HS ?
    answer: Feux qui ne s'allument plus ou par intermittence, commodo qui reste bloqué, fonctions aléatoires, bruit de craquement
      en tournant le commutateur.
  - question: Tous les combien changer la commande d'éclairage ?
    answer: Pas de périodicité fixe. Durée de vie variable selon usage. À remplacer si dysfonctionnement avéré après vérification
      des fusibles et ampoules.
  - question: Peut-on changer la commande d'éclairage soi-même ?
    answer: Oui, opération accessible. Débrancher la batterie, déposer le cache colonne de direction, débrancher les connecteurs,
      dévisser le commodo. 30 min à 1h.
  - question: Quelle erreur éviter avec la commande d'éclairage ?
    answer: Toujours vérifier les fusibles et ampoules avant de remplacer le commodo. Débrancher la batterie pour éviter les
      courts-circuits. Ne pas forcer sur les connecteurs.
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
doc_id: 271e3dbc-55df-5f6f-b12a-21d0223b3fb3
content_hash: sha256:50ece7f502310d3e
lang: fr
variants:
- name: Ampoule halogene
  aliases:
  - halogene
  - H1
  - H4
  - H7
  functional_differences:
  - Standard, economique
  - Remplacement simple
- name: Ampoule LED
  aliases:
  - LED
  functional_differences:
  - Duree de vie superieure
  - Consommation reduite
  - Verifier homologation
location_on_vehicle:
  area: Face avant, arriere et laterale du vehicule
  access: Par le compartiment moteur (avant) ou coffre (arriere)
  adjacent_parts:
  - optique
  - ampoule
  - connecteur
  - reflecteur
installation:
  difficulty: facile
  time: 5 a 15 min
  tools:
  - tournevis
  - gants (ne pas toucher ampoule halogene)
  prerequisite: Moteur eteint, acces par compartiment moteur ou coffre
---

# Commande d'éclairage - Guide Diagnostic Complet

## Fonction et Rôle

Commande les différents feux du véhicule

**Actions principales:** commander, activer, regler

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Commodo bloque ou difficile a tourner**
  commodo bloque ou difficile a tourner

### 🟢 Autres Symptômes

- feux croisement route allument plus
- fonctions aleatoires s allument puis s eteignent
- clignotants fonctionnent plus depuis commodo
- bruit de craquement en actionnant l interrupteur
- fusibles ok mais feux inoperants

## Procédure de Diagnostic

Pour diagnostiquer un problème de commande d'éclairage:

1. **Inspection visuelle** - Examiner l'état du commande d'éclairage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le commande d'éclairage peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes

## Pièces Associées

Lors du remplacement, vérifier également:

- commande-d-essuie-glace
- feu-arriere
- feu-avant
- feu-clignotant

## Critères de Compatibilité

Pour commander le bon commande d'éclairage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleur éclairage"

## FAQ

**Commande d'éclairage OE ou adaptable ?**
Privilégiez l'OE ou OES (Valeo, Hella). Le commodo doit être parfaitement compatible avec votre véhicule (connecteurs, fonctions). Les adaptables peuvent avoir des incompatibilités.

**Comment savoir si ma commande d'éclairage est HS ?**
Feux qui ne s'allument plus ou par intermittence, commodo qui reste bloqué, fonctions aléatoires, bruit de craquement en tournant le commutateur.

**Tous les combien changer la commande d'éclairage ?**
Pas de périodicité fixe. Durée de vie variable selon usage. À remplacer si dysfonctionnement avéré après vérification des fusibles et ampoules.

**Peut-on changer la commande d'éclairage soi-même ?**
Oui, opération accessible. Débrancher la batterie, déposer le cache colonne de direction, débrancher les connecteurs, dévisser le commodo. 30 min à 1h.

**Quelle erreur éviter avec la commande d'éclairage ?**
Toujours vérifier les fusibles et ampoules avant de remplacer le commodo. Débrancher la batterie pour éviter les courts-circuits. Ne pas forcer sur les connecteurs.
