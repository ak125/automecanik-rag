---
category: eclairage
slug: contacteur-de-feu-de-recul
title: Contacteur feu de recul
pg_id: 807
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
  role: Active les feux de recul en marche arrière
  must_be_true:
  - activer
  - signaler
  - commander
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
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de compatibilite
    pour confirmer Contacteur feu de recul.
  - Verifier le type d ampoule (H1, H4, H7, LED, xenon) compatible avec le vehicule
  - Respecter la puissance et le culot exact de l ampoule d origine
  - Choisir des ampoules homologuees pour la circulation routiere
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "sécurité maximale"
  cost_range:
    min: 10
    max: 40
    currency: EUR
    unit: contacteur
    source: catalogue automecanik
  quality_tiers:
  - tier: Pièce OE (Origine Équipement)
    description: Contacteur identique à l origine. Filetage et connecteur parfaitement conformes. Option à envisager sur véhicules
      récents sous garantie.
  - tier: Équivalent OE (spécialistes électricité auto)
    description: Fabricants spécialisés en composants électriques automobiles. Qualité proche de l OE à prix accessible.
  - tier: Générique compatible
    description: Peut convenir si le filetage et le connecteur sont strictement identiques. Vérifier avant commande.
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
    label: Feux recul allument plus marche
    severity: confort
  - id: S2
    label: Feux de recul toujours allumes moteur demarre
    severity: confort
  - id: S3
    label: Fuite huile visible niveau contacteur
    severity: confort
  - id: S4
    label: Camera de recul inactive car contacteur defaillant
    severity: confort
  - id: S5
    label: Odeur huile boite vitesses autour
    severity: confort
  - id: S6
    label: Claquement bruit passage marche arriere
    severity: confort
  - id: S7
    label: Difficulte enclencher marche arriere contacteur
    severity: confort
  - id: S8
    label: Contacteur place depuis plus controle
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - 'Usure ou defaillance causant : feux recul allument plus marche'
  quick_checks:
  - 'Observer : feux recul allument plus marche ?'
  - 'Observer : feux de recul toujours allumes moteur demarre ?'
  - Fuite huile visible niveau contacteur ?
  - 'Observer : camera de recul inactive car contacteur defaillant ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Feux recul allument plus marche
  - Feux de recul toujours allumes moteur demarre
  - Fuite huile visible niveau contacteur
  - Camera de recul inactive car contacteur defaillant
  - Odeur huile boite vitesses autour
  - Claquement bruit passage marche arriere
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '807'
  intro_title: A quoi sert Contacteur feu de recul ?
  risk_title: Pourquoi remplacer Contacteur feu de recul a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: Contacteur de feu de recul OE ou adaptable ?
    answer: Les contacteurs OES (Hella, FAE) ou adaptables de qualité conviennent. Vérifiez le type de filetage et le connecteur.
      Pièce peu coûteuse, privilégiez la qualité.
  - question: Comment savoir si mon contacteur de recul est HS ?
    answer: Feux de recul qui ne s'allument jamais, feux qui restent allumés en permanence, feux intermittents. Tester avec
      un multimètre (continuité en marche arrière).
  - question: Tous les combien changer le contacteur de recul ?
    answer: Pas de périodicité fixe. Durée de vie très variable. À remplacer si les feux de recul ne fonctionnent plus après
      vérification ampoule et fusible.
  - question: Peut-on changer le contacteur de recul soi-même ?
    answer: Oui, opération simple. Localiser le contacteur sur la boîte (fil électrique), débrancher, dévisser (attention
      à la fuite d'huile de boîte), revisser le neuf. 15-30 min.
  - question: Quelle erreur éviter avec le contacteur de recul ?
    answer: Prévoir un joint neuf si fourni. Avoir un récipient pour l'huile qui peut couler. Serrer au couple pour éviter
      les fuites. Vérifier le niveau d'huile de boîte après.
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
doc_id: 1295563c-6550-51c4-bb16-b1f833e4fc7b
content_hash: sha256:315afdbb2dd29b17
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

# Contacteur feu de recul - Guide Diagnostic Complet

## Fonction et Rôle

Active les feux de recul en marche arrière

**Actions principales:** activer, signaler, commander

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement bruit passage marche arriere**
  claquement bruit passage marche arriere

### 🟢 Autres Symptômes

- feux recul allument plus marche
- feux de recul toujours allumes moteur demarre
- fuite huile visible niveau contacteur
- camera de recul inactive car contacteur defaillant
- odeur huile boite vitesses autour
- difficulte enclencher marche arriere contacteur

## Procédure de Diagnostic

Pour diagnostiquer un problème de contacteur feu de recul:

1. **Inspection visuelle** - Examiner l'état du contacteur feu de recul
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-arriere
- commande-d-eclairage
- feu-arriere
- feu-avant
- feu-clignotant

## Critères de Compatibilité

Pour commander le bon contacteur feu de recul, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "sécurité maximale"

## FAQ

**Contacteur de feu de recul OE ou adaptable ?**
Les contacteurs OES (Hella, FAE) ou adaptables de qualité conviennent. Vérifiez le type de filetage et le connecteur. Pièce peu coûteuse, privilégiez la qualité.

**Comment savoir si mon contacteur de recul est HS ?**
Feux de recul qui ne s'allument jamais, feux qui restent allumés en permanence, feux intermittents. Tester avec un multimètre (continuité en marche arrière).

**Tous les combien changer le contacteur de recul ?**
Pas de périodicité fixe. Durée de vie très variable. À remplacer si les feux de recul ne fonctionnent plus après vérification ampoule et fusible.

**Peut-on changer le contacteur de recul soi-même ?**
Oui, opération simple. Localiser le contacteur sur la boîte (fil électrique), débrancher, dévisser (attention à la fuite d'huile de boîte), revisser le neuf. 15-30 min.

**Quelle erreur éviter avec le contacteur de recul ?**
Prévoir un joint neuf si fourni. Avoir un récipient pour l'huile qui peut couler. Serrer au couple pour éviter les fuites. Vérifier le niveau d'huile de boîte après.
