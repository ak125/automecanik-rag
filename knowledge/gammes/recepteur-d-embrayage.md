---
category: embrayage
slug: recepteur-d-embrayage
title: Récepteur d'embrayage
pg_id: 620
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
  role: Recevoir la pression hydraulique et actionner la butée ou la fourchette
  must_be_true:
  - recevoir la pression
  - actionner la butée
  - pousser la fourchette
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
  - emetteur-d-embrayage
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
  - ❌ "action parfaite"
  cost_range:
    min: 26
    max: 165
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
    label: Fuite de liquide visible sous la boite de vitesses
    severity: confort
  - id: S3
    label: Bruit de grincement au niveau de la fourchette
    severity: confort
  - id: S4
    label: Odeur de liquide de frein brule sous la voiture
    severity: securite
  - id: S5
    label: Embrayage qui ne debraye plus piston bloque
    severity: immobilisation
  - id: S6
    label: Plus de 150 000 km sans verification du circuit
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - remplacement preventif recommande
  depose_steps: []
  quick_checks:
  - 'Observer : pedale d embrayage molle ou spongieuse ?'
  - Fuite de liquide visible sous la boite de vitesses ?
  - Bruit de grincement au niveau de la fourchette ?
  - Odeur de liquide de frein brule sous la voiture ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Pedale d embrayage molle ou spongieuse
  - Fuite de liquide visible sous la boite de vitesses
  - Bruit de grincement au niveau de la fourchette
  - Odeur de liquide de frein brule sous la voiture
  - Embrayage qui ne debraye plus piston bloque
  - Plus de 150 000 km sans verification du circuit
  good_practices:
  - Eviter de laisser le pied sur la pedale d embrayage au point mort
  - Remplacement du kit complet (disque + mecanisme + butee)
  - Purge du circuit hydraulique si recepteur/emetteur concerne
  - Verifier le volant moteur lors du remplacement d embrayage
rendering:
  pgId: '620'
  intro_title: A quoi sert Récepteur d'embrayage ?
  risk_title: Pourquoi remplacer Récepteur d'embrayage a temps ?
  risk_explanation: '**Pièce HS** - Le récepteur d''embrayage peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le récepteur d''embrayage peut être hors service et nécessiter un remplacement'
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
  - question: Récepteur d'embrayage OE ou OES ?
    answer: Les récepteurs OES (Sachs, LuK, Valeo) sont fiables. Pour un récepteur concentrique (CSC), privilégiez l'OE ou
      un kit embrayage complet incluant le CSC.
  - question: Comment savoir si mon récepteur d'embrayage fuit ?
    answer: Pédale molle ou qui s'enfonce, fuite de liquide sous la boîte de vitesses, niveau de liquide de frein qui baisse,
      embrayage qui ne débraye plus.
  - question: Faut-il purger après changement de récepteur ?
    answer: Oui obligatoirement. Purge par le purgeur situé sur le récepteur. Utiliser du liquide DOT4 neuf. Vérifier l'absence
      de bulles d'air.
  - question: Peut-on changer le récepteur d'embrayage soi-même ?
    answer: 'Le récepteur externe oui (sous la voiture). Le récepteur concentrique nécessite de déposer la boîte : autant
      changer l''embrayage en même temps.'
  - question: Quelle erreur éviter avec le récepteur d'embrayage ?
    answer: Ne pas forcer sur le piston. Bien purger pour éliminer tout l'air. Vérifier l'émetteur si le récepteur fuyait.
      Remplacer le CSC avec l'embrayage.
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
doc_id: 564a76d1-b7a3-5481-813d-fb1c8d4391df
content_hash: sha256:e6faf6048dd44e73
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

# Récepteur d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Recevoir la pression hydraulique et actionner la butée ou la fourchette

**Actions principales:** recevoir la pression, actionner la butée, pousser la fourchette, convertir

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Embrayage qui ne debraye plus piston bloque**
  embrayage qui ne debraye plus piston bloque

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de grincement au niveau de la fourchette**
  bruit de grincement au niveau de la fourchette

### 🟡 Symptômes de Sécurité

- **Odeur de liquide de frein brule sous la voiture**
  odeur de liquide de frein brule sous la voiture

### 🟢 Autres Symptômes

- pedale d embrayage molle ou spongieuse
- fuite de liquide visible sous la boite de vitesses
- plus de 150 000 km sans verification du circuit

## Procédure de Diagnostic

Pour diagnostiquer un problème de récepteur d'embrayage:

1. **Inspection visuelle** - Examiner l'état du récepteur d'embrayage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le récepteur d'embrayage peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- butee-d-embrayage
- emetteur-d-embrayage
- kit-d-embrayage
- volant-moteur

## Critères de Compatibilité

Pour commander le bon récepteur d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "action parfaite"

## FAQ

**Récepteur d'embrayage OE ou OES ?**
Les récepteurs OES (Sachs, LuK, Valeo) sont fiables. Pour un récepteur concentrique (CSC), privilégiez l'OE ou un kit embrayage complet incluant le CSC.

**Comment savoir si mon récepteur d'embrayage fuit ?**
Pédale molle ou qui s'enfonce, fuite de liquide sous la boîte de vitesses, niveau de liquide de frein qui baisse, embrayage qui ne débraye plus.

**Faut-il purger après changement de récepteur ?**
Oui obligatoirement. Purge par le purgeur situé sur le récepteur. Utiliser du liquide DOT4 neuf. Vérifier l'absence de bulles d'air.

**Peut-on changer le récepteur d'embrayage soi-même ?**
Le récepteur externe oui (sous la voiture). Le récepteur concentrique nécessite de déposer la boîte : autant changer l'embrayage en même temps.

**Quelle erreur éviter avec le récepteur d'embrayage ?**
Ne pas forcer sur le piston. Bien purger pour éliminer tout l'air. Vérifier l'émetteur si le récepteur fuyait. Remplacer le CSC avec l'embrayage.


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
