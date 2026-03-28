---
category: capteurs
slug: interrupteur-des-feux-de-freins
title: Interrupteur des feux de freins
pg_id: 806
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
  role: Detecte l'appui sur la pedale de frein pour activer les feux stop
  must_be_true:
  - detecter
  - signaler
  - activer
  must_not_contain:
  - reparation
  - regeneration
  - nettoyage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - disque-de-frein
  - plaquette-de-frein
  - etrier-de-frein
  - flexible-de-frein
  - maitre-cylindre-de-frein
  - liquide-de-frein
  confusion_with:
  - term: piece-de-freinage-voisine
    difference: 'Verifier la reference exacte : les pieces de freinage se ressemblent mais ne sont pas interchangeables entre
      essieux ou types de montage.'
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
  - ❌ "meilleur freinage"
  cost_range:
    min: 10
    max: 35
    currency: EUR
    unit: pièce
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    description: Interrupteur identique à l'origine. Recommandé sur véhicules récents avec fonctions multiples (ESP, régulateur
      adaptatif, boîte automatique).
  - tier: Équivalent OE (OES)
    description: Fabricants comme Bosch, TRW ou Febi proposent des interrupteurs équivalents OE. Compatibilité électrique
      et mécanique vérifiée sur les principaux modèles.
  - tier: Adaptable (aftermarket)
    description: Le marché aftermarket couvre bien ce segment pour un usage standard. Vérifier que le nombre de circuits correspond
      (certains interrupteurs ont 2 ou 3 circuits).
  brands:
    premium:
    - Brembo
    - ATE
    - TRW
    standard:
    - Bosch
    - Ferodo
    - Textar
    budget:
    - Ridex
    - Valeo
diagnostic:
  symptoms:
  - id: S1
    label: Feux stop qui restent allumes moteur eteint
    severity: confort
  - id: S2
    label: Feux stop qui ne s allument plus du tout
    severity: confort
  - id: S3
    label: Regulateur de vitesse qui ne fonctionne plus
    severity: confort
  - id: S4
    label: Message d erreur systeme esp au tableau de bord
    severity: securite
  - id: S5
    label: Batterie decharge feux stop restes
    severity: confort
  - id: S6
    label: Clic audible absent quand on appuie sur la pedale
    severity: securite
  - id: S7
    label: Odeur de plastique brule court-circuit
    severity: confort
  - id: S8
    label: Plus de 150 000 km sans verification
    severity: confort
  causes:
  - remplacement preventif recommande
  - 'kilometrage eleve ou usure visible : remplacement preventif recommande'
  - 'Usure ou defaillance causant : feux stop qui restent allumes moteur eteint'
  quick_checks:
  - 'Observer : feux stop qui restent allumes moteur eteint ?'
  - 'Observer : feux stop qui ne s allument plus du tout ?'
  - 'Observer : regulateur de vitesse qui ne fonctionne plus ?'
  - 'Observer : message d erreur systeme esp au tableau de bord ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Feux stop qui restent allumes moteur eteint
  - Feux stop qui ne s allument plus du tout
  - Regulateur de vitesse qui ne fonctionne plus
  - Message d erreur systeme esp au tableau de bord
  - Batterie decharge feux stop restes
  - Clic audible absent quand on appuie sur la pedale
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '806'
  intro_title: A quoi sert Interrupteur des feux de freins ?
  risk_title: Pourquoi remplacer Interrupteur des feux de freins a temps ?
  risk_explanation: '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
  risk_consequences:
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
  - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
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
  - question: Interrupteur feux stop OE ou adaptable ?
    answer: Les interrupteurs adaptables fonctionnent bien pour un usage standard. L'OE est recommandé sur véhicules récents
      avec fonctions multiples (ESP, régulateur).
  - question: Comment savoir si mon interrupteur de feux stop est HS ?
    answer: Feux stop qui restent allumés en permanence, ou qui ne s'allument plus du tout. Le régulateur de vitesse peut
      aussi ne plus fonctionner.
  - question: Peut-on tester l'interrupteur de feux stop ?
    answer: Oui avec un multimètre. Vérifiez la continuité quand la pédale est enfoncée. Ou observez les feux stop pendant
      qu'un assistant appuie sur la pédale.
  - question: Peut-on changer l'interrupteur de feux stop soi-même ?
    answer: Oui, très simple. Accès sous le tableau de bord, derrière la pédale de frein. Quart de tour pour déverrouiller.
      10 minutes suffisent.
  - question: Quelle erreur éviter avec l'interrupteur de feux stop ?
    answer: Vérifier le réglage après montage (feux doivent s'allumer dès le début de course pédale). Attention au sens de
      montage sur certains modèles.
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
doc_id: cd3ee0a9-5be2-50e5-943c-3204d0c35403
content_hash: sha256:6b254fc188500a63
lang: fr
variants:
- name: Piece standard
  aliases:
  - standard
  - OE equivalent
  functional_differences:
  - Qualite equivalente a la monte d origine
  - Compatible avec la majorite des vehicules
- name: Piece performance/sport
  aliases:
  - sport
  - haute performance
  functional_differences:
  - Materiaux haute temperature
  - Pour usage intensif ou sportif
location_on_vehicle:
  area: Au niveau des roues (avant et/ou arriere)
  access: Demontage de la roue necessaire (cric + chandelle)
  adjacent_parts:
  - disque
  - plaquette
  - etrier
  - flexible
installation:
  difficulty: moyen
  time: 30min a 1h par essieu
  tools:
  - cle a douille
  - cle Allen
  - pied a coulisse
  - cle dynamometrique
  prerequisite: Vehicule sur chandelles, roue demontee
---

# Interrupteur des feux de freins - Guide Diagnostic Complet

## Fonction et Rôle

Detecte l'appui sur la pedale de frein pour activer les feux stop

**Actions principales:** detecter, signaler, activer, commander

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Message d erreur systeme esp au tableau de bord**
  message d erreur systeme esp au tableau de bord
- **Clic audible absent quand on appuie sur la pedale**
  clic audible absent quand on appuie sur la pedale

### 🟢 Autres Symptômes

- feux stop qui restent allumes moteur eteint
- feux stop qui ne s allument plus du tout
- regulateur de vitesse qui ne fonctionne plus
- batterie decharge feux stop restes
- odeur de plastique brule court-circuit
- plus de 150 000 km sans verification

## Procédure de Diagnostic

Pour diagnostiquer un problème de interrupteur des feux de freins:

1. **Inspection visuelle** - Examiner l'état du interrupteur des feux de freins
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- cable-de-frein-a-main
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- etrier-de-frein
- feu-arriere
- kit-de-freins-arriere
- machoires-de-frein

## Critères de Compatibilité

Pour commander le bon interrupteur des feux de freins, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleur freinage"

## FAQ

**Interrupteur feux stop OE ou adaptable ?**
Les interrupteurs adaptables fonctionnent bien pour un usage standard. L'OE est recommandé sur véhicules récents avec fonctions multiples (ESP, régulateur).

**Comment savoir si mon interrupteur de feux stop est HS ?**
Feux stop qui restent allumés en permanence, ou qui ne s'allument plus du tout. Le régulateur de vitesse peut aussi ne plus fonctionner.

**Peut-on tester l'interrupteur de feux stop ?**
Oui avec un multimètre. Vérifiez la continuité quand la pédale est enfoncée. Ou observez les feux stop pendant qu'un assistant appuie sur la pédale.

**Peut-on changer l'interrupteur de feux stop soi-même ?**
Oui, très simple. Accès sous le tableau de bord, derrière la pédale de frein. Quart de tour pour déverrouiller. 10 minutes suffisent.

**Quelle erreur éviter avec l'interrupteur de feux stop ?**
Vérifier le réglage après montage (feux doivent s'allumer dès le début de course pédale). Attention au sens de montage sur certains modèles.
