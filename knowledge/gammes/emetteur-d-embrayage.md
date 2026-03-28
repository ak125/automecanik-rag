---
category: embrayage
slug: emetteur-d-embrayage
title: Emetteur d'embrayage
pg_id: 234
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-25'
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
  role: Transmettre la pression hydraulique de la pédale vers le récepteur
  must_be_true:
  - transmettre la pression
  - pousser le liquide
  - convertir l'effort
  must_not_contain:
  - disque
  - volant
  - couple
  - câble
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - kit-d-embrayage
  - butee-d-embrayage
  - volant-moteur
  - recepteur-d-embrayage
  - cable-d-embrayage
  confusion_with:
  - term: piece-d-embrayage-voisine
    difference: Le systeme d embrayage comporte plusieurs pieces (disque, mecanisme, butee, emetteur, recepteur). Verifier
      laquelle est defectueuse.
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
  - ❌ "pression parfaite"
  cost_range:
    min: 40
    max: 150
    currency: EUR
    unit: émetteur
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
    description: Pièce conforme aux préconisations constructeur. Diamètre de piston et course identiques, joints inclus. Recommandé
      sur les véhicules récents ou lorsque la fidélité de la pédale est prioritaire.
  - tier: Équipementier reconnu (embrayage / freinage)
    description: Fabricants spécialisés en composants hydrauliques. Matières des joints compatibles avec les liquides de frein
      DOT 4/DOT 5.1, diamètres conformes aux spécifications.
  - tier: Pièce adaptable
    description: Option économique pour les véhicules anciens. Vérifier impérativement le diamètre de piston (en mm), la longueur
      hors tout et la compatibilité du filetage de raccordement.
  brands:
    premium:
    - LuK
    - Sachs
    standard:
    - Valeo
    - Exedy
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Pedale d embrayage molle ou spongieuse
    severity: confort
  - id: S2
    label: Pedale qui s enfonce jusqu au plancher
    severity: confort
  - id: S3
    label: Niveau liquide frein baisse fuite
    severity: securite
  - id: S4
    label: Fuite liquide sous tableau bord
    severity: confort
  - id: S5
    label: Embrayage qui patine par intermittence
    severity: confort
  - id: S6
    label: Difficulte a debrayer completement
    severity: confort
  causes:
  - identifier origine fuite et verifier joints
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  - 'Usure ou defaillance causant : pedale d embrayage molle ou spongieuse'
  quick_checks:
  - 'Observer : pedale d embrayage molle ou spongieuse ?'
  - 'Observer : pedale qui s enfonce jusqu au plancher ?'
  - 'Observer : niveau liquide frein baisse fuite ?'
  - Fuite liquide sous tableau bord ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Pedale d embrayage molle ou spongieuse
  - Pedale qui s enfonce jusqu au plancher
  - Niveau liquide frein baisse fuite
  - Fuite liquide sous tableau bord
  - Embrayage qui patine par intermittence
  - Difficulte a debrayer completement
  good_practices:
  - Eviter de laisser le pied sur la pedale d embrayage au point mort
  - Remplacement du kit complet (disque + mecanisme + butee)
  - Purge du circuit hydraulique si recepteur/emetteur concerne
  - Verifier le volant moteur lors du remplacement d embrayage
rendering:
  pgId: '234'
  intro_title: A quoi sert Emetteur d'embrayage ?
  risk_title: Pourquoi remplacer Emetteur d'embrayage a temps ?
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
  - question: Émetteur d'embrayage OE ou OES ?
    answer: Les émetteurs OES (Sachs, LuK, Valeo) sont fiables. Certains véhicules ont un émetteur concentrique plus complexe.
      Vérifiez le type exact pour votre véhicule.
  - question: Comment savoir si mon émetteur d'embrayage fuit ?
    answer: Pédale d'embrayage molle ou qui s'enfonce, niveau de liquide de frein qui baisse, tache de liquide sous le tableau
      de bord, embrayage qui patine.
  - question: Faut-il purger après changement d'émetteur ?
    answer: Oui obligatoirement. Le circuit a été ouvert et de l'air est entré. Purge par gravité ou avec purgeur. Utiliser
      du liquide de frein DOT4 neuf.
  - question: Peut-on changer l'émetteur d'embrayage soi-même ?
    answer: Oui, opération accessible. L'émetteur est généralement sous le tableau de bord. La purge demande un assistant
      ou un purgeur automatique.
  - question: Quelle erreur éviter avec l'émetteur d'embrayage ?
    answer: Ne pas mélanger les liquides de frein. Bien purger pour éliminer l'air. Vérifier aussi le récepteur si l'émetteur
      était défaillant.
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
doc_id: 7ac8a510-b4a8-521b-a220-782770fcb54c
content_hash: sha256:29694840b0ab4ed1
lang: fr
variants:
- name: Kit embrayage complet
  aliases:
  - kit complet
  - 3 pieces
  functional_differences:
  - Disque + mecanisme + butee
  - Remplacement recommande en bloc
- name: Kit avec volant moteur
  aliases:
  - kit 4 pieces
  - kit + volant
  functional_differences:
  - Inclut le volant moteur bimasse
  - Pour vehicules diesel modernes
location_on_vehicle:
  area: Entre le moteur et la boite de vitesses
  access: Depose de la boite de vitesses necessaire (pont elevateur)
  adjacent_parts:
  - volant moteur
  - boite de vitesses
  - arbre primaire
installation:
  difficulty: difficile (pro recommande)
  time: 4h a 8h
  tools:
  - pont elevateur
  - cric de boite
  - centreur d embrayage
  - cle dynamometrique
  prerequisite: Depose complete de la boite de vitesses
---

# Emetteur d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre la pression hydraulique de la pédale vers le récepteur

**Actions principales:** transmettre la pression, pousser le liquide, convertir l'effort, envoyer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Niveau liquide frein baisse fuite**
  niveau liquide frein baisse fuite

### 🟢 Autres Symptômes

- pedale d embrayage molle ou spongieuse
- pedale qui s enfonce jusqu au plancher
- fuite liquide sous tableau bord
- embrayage qui patine par intermittence
- difficulte a debrayer completement

## Procédure de Diagnostic

Pour diagnostiquer un problème de emetteur d'embrayage:

1. **Inspection visuelle** - Examiner l'état du emetteur d'embrayage
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

- butee-d-embrayage
- kit-d-embrayage
- recepteur-d-embrayage

## Critères de Compatibilité

Pour commander le bon emetteur d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "pression parfaite"

## FAQ

**Émetteur d'embrayage OE ou OES ?**
Les émetteurs OES (Sachs, LuK, Valeo) sont fiables. Certains véhicules ont un émetteur concentrique plus complexe. Vérifiez le type exact pour votre véhicule.

**Comment savoir si mon émetteur d'embrayage fuit ?**
Pédale d'embrayage molle ou qui s'enfonce, niveau de liquide de frein qui baisse, tache de liquide sous le tableau de bord, embrayage qui patine.

**Faut-il purger après changement d'émetteur ?**
Oui obligatoirement. Le circuit a été ouvert et de l'air est entré. Purge par gravité ou avec purgeur. Utiliser du liquide de frein DOT4 neuf.

**Peut-on changer l'émetteur d'embrayage soi-même ?**
Oui, opération accessible. L'émetteur est généralement sous le tableau de bord. La purge demande un assistant ou un purgeur automatique.

**Quelle erreur éviter avec l'émetteur d'embrayage ?**
Ne pas mélanger les liquides de frein. Bien purger pour éliminer l'air. Vérifier aussi le récepteur si l'émetteur était défaillant.


## Symptomes supplementaires

<!-- materialized-from-db diagnostic/embrayage.md 2026-01-08 -->
### Diagnostic - Embrayage

# Embrayage - Diagnostic complet

## Symptomes courants

### Pedale d'embrayage dure
- **Quand** : A chaque actionnement
- **Caracteristique** : Resistance excessive, fatigue musculaire

### Pedale molle ou spongieuse
- **Quand** : Constant
- **Caracteristique** : Course excessive, point de patinage haut

### Patinage embrayage
- **Quand** : En acceleration forte, en cote
- **Caracteristique** : Regime moteur monte sans acceleration proportionnelle

### Bruit au debrayage
- **Quand** : Appui sur la pedale
- **Caracteristique** : Grincement, sifflement, claquement

### Difficulte passage vitesses
- **Quand** : A froid ou constant
- **Caracteristique** : Craquements, resistance

## Causes possibles et solutions

### 1. Disque d'embrayage use
- **Probabilite** : 50%
- **Verification** : Patinage, kilometrage eleve
- **Solution** : Remplacement kit embrayage complet
- **Pieces** : Kit embrayage (disque, mecanisme, butee)
- **Urgence** : Moyenne a haute

### 2. Butee hydraulique/mecanique HS
- **Probabilite** : 25%
- **Verification** : Bruit a l'appui pedale, fuite liquide
- **Solution** : Remplacement butee
- **Pieces** : Butee d'embrayage
- **Urgence** : Moyenne

### 3. Volant moteur bimasse HS
- **Probabilite** : 15%
- **Verification** : Vibrations excessives, claquements au ralenti
- **Solution** : Remplacement volant moteur
- **Pieces** : Volant moteur bimasse ou conversion simple masse
- **Urgence** : Moyenne

### 4. Emetteur/recepteur d'embrayage defaillant
- **Probabilite** : 10%
- **Verification** : Pedale molle, fuite liquide
- **Solution** : Remplacement cylindre emetteur ou recepteur
- **Pieces** : Emetteur, recepteur, liquide de frein
- **Urgence** : Moyenne

## Duree de vie embrayage

| Utilisation | Duree de vie |
|-------------|--------------|
| Autoroute | 150 000 - 200 000 km |
| Mixte | 100 000 - 150 000 km |
| Urbaine | 80 000 - 120 000 km |
| Agressive | 50 000 - 80 000 km |

## Recommandations

- **Kit complet** : Toujours remplacer disque + mecanisme + butee ensemble
- **Volant moteur** : Controler systematiquement le volant lors du changement
- **Marques** : Privilegier Valeo, LuK, Sachs
- **Conduite** : Eviter de garder le pied sur la pedale d'embrayage
