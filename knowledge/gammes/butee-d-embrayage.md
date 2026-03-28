---
category: embrayage
slug: butee-d-embrayage
title: Butée d'embrayage
pg_id: 48
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
  role: Actionner le mécanisme d'embrayage pour permettre le débrayage
  must_be_true:
  - actionner
  - débrayer
  - pousser
  must_not_contain:
  - disque
  - volant
  - couple
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - kit-d-embrayage
  - volant-moteur
  - emetteur-d-embrayage
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
  - ❌ "débrayage parfait"
  cost_range:
    min: 20
    max: 80
    currency: EUR
    unit: butée
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
    description: 'Butée conforme aux spécifications constructeur : diamètre de contact, hauteur de poussée et type (auto-centrante
      ou à guidage). Généralement livrée dans le kit embrayage complet.'
  - tier: Qualité équivalente OE
    description: Butée d'équipementier spécialisé embrayage respectant les côtes fonctionnelles. Souvent vendue seule ou en
      kit partiel avec la fourchette.
  - tier: Adaptable compatible
    description: Butée de remplacement compatible avec plusieurs références proches. Vérifier impérativement le diamètre intérieur,
      extérieur et la hauteur avant commande.
  - tier: Kit embrayage complet
    description: La butée est généralement remplacée en même temps que le disque et le mécanisme. Acheter un kit complet homogène
      évite les incompatibilités d'usure.
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
    label: Bruit roulement quand appuie pedale
    severity: confort
  - id: S2
    label: Sifflement grondement disparait relachant pedale
    severity: confort
  - id: S3
    label: Pedale d embrayage qui vibre sous le pied
    severity: confort
  - id: S4
    label: Embrayage qui accroche par a-coups
    severity: confort
  - id: S5
    label: Difficulte a passer les vitesses butee grippee
    severity: confort
  - id: S6
    label: Plus changement embrayage
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : bruit roulement quand appuie pedale'
  quick_checks:
  - Bruit roulement quand appuie pedale ?
  - 'Observer : sifflement grondement disparait relachant pedale ?'
  - 'Observer : pedale d embrayage qui vibre sous le pied ?'
  - 'Observer : embrayage qui accroche par a-coups ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Bruit roulement quand appuie pedale
  - Sifflement grondement disparait relachant pedale
  - Pedale d embrayage qui vibre sous le pied
  - Embrayage qui accroche par a-coups
  - Difficulte a passer les vitesses butee grippee
  - Plus changement embrayage
  good_practices:
  - Eviter de laisser le pied sur la pedale d embrayage au point mort
  - Remplacement du kit complet (disque + mecanisme + butee)
  - Purge du circuit hydraulique si recepteur/emetteur concerne
  - Verifier le volant moteur lors du remplacement d embrayage
rendering:
  pgId: '48'
  intro_title: A quoi sert Butée d'embrayage ?
  risk_title: Pourquoi remplacer Butée d'embrayage a temps ?
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
  - question: Butée d'embrayage OE ou OES ?
    answer: Les butées OES (Sachs, LuK, Valeo) sont de qualité équivalente à l'OE. Privilégiez un kit embrayage complet de
      la même marque pour garantir la compatibilité.
  - question: Comment savoir si ma butée d'embrayage est HS ?
    answer: Bruit de roulement (grondement ou sifflement) quand on appuie sur la pédale d'embrayage, pédale qui vibre, embrayage
      qui accroche par à-coups.
  - question: Tous les combien changer la butée d'embrayage ?
    answer: À chaque changement du kit embrayage (120 000 à 200 000 km). Ne jamais la réutiliser même si elle semble en bon
      état.
  - question: Peut-on changer la butée d'embrayage seule ?
    answer: 'Techniquement possible mais déconseillé : il faut déposer la boîte de vitesses. Autant changer tout le kit embrayage
      en même temps.'
  - question: Quelle erreur éviter avec la butée d'embrayage ?
    answer: Ne pas laisser le pied sur la pédale d'embrayage en conduisant. Ne pas réutiliser une vieille butée. Vérifier
      le guide-butée et la fourchette.
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
doc_id: 09874db9-d6a5-5c68-bcb9-4370b6c80d06
content_hash: sha256:8a5ad1608d9efd0f
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

# Butée d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Actionner le mécanisme d'embrayage pour permettre le débrayage

**Actions principales:** actionner, débrayer, pousser, libérer le disque, appuyer sur le mécanisme

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- bruit roulement quand appuie pedale
- sifflement grondement disparait relachant pedale
- pedale d embrayage qui vibre sous le pied
- embrayage qui accroche par a-coups
- difficulte a passer les vitesses butee grippee
- plus changement embrayage

## Procédure de Diagnostic

Pour diagnostiquer un problème de butée d'embrayage:

1. **Inspection visuelle** - Examiner l'état du butée d'embrayage
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

- emetteur-d-embrayage
- kit-d-embrayage
- recepteur-d-embrayage
- volant-moteur

## Critères de Compatibilité

Pour commander le bon butée d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "débrayage parfait"

## FAQ

**Butée d'embrayage OE ou OES ?**
Les butées OES (Sachs, LuK, Valeo) sont de qualité équivalente à l'OE. Privilégiez un kit embrayage complet de la même marque pour garantir la compatibilité.

**Comment savoir si ma butée d'embrayage est HS ?**
Bruit de roulement (grondement ou sifflement) quand on appuie sur la pédale d'embrayage, pédale qui vibre, embrayage qui accroche par à-coups.

**Tous les combien changer la butée d'embrayage ?**
À chaque changement du kit embrayage (120 000 à 200 000 km). Ne jamais la réutiliser même si elle semble en bon état.

**Peut-on changer la butée d'embrayage seule ?**
Techniquement possible mais déconseillé : il faut déposer la boîte de vitesses. Autant changer tout le kit embrayage en même temps.

**Quelle erreur éviter avec la butée d'embrayage ?**
Ne pas laisser le pied sur la pédale d'embrayage en conduisant. Ne pas réutiliser une vieille butée. Vérifier le guide-butée et la fourchette.


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
