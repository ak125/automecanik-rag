---
category: suspension
slug: kit-de-butee-de-suspension
title: Kit de butée de suspension
pg_id: 1632
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
  role: Ensemble de fixation supérieure de l'amortisseur
  must_be_true:
  - supporter
  - amortir
  - guider
  must_not_contain:
  - injection
  - freinage
  - climatisation
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - amortisseur
  - ressort-de-suspension
  - bras-de-suspension
  - rotule-de-suspension
  - barre-stabilisatrice
  - biellette-de-barre-stabilisatrice
  confusion_with:
  - term: piece-de-suspension-voisine
    difference: Les pieces de suspension travaillent ensemble mais ont des references distinctes. Verifier la position (avant/arriere,
      gauche/droite).
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
  - ❌ "meilleur confort"
  cost_range:
    min: 30
    max: 100
    currency: EUR
    unit: kit
    source: catalogue automecanik
  quality_tiers:
  - tier: Equipement d'origine (OE)
    description: Kit complet agréé par le constructeur du véhicule. Inclut coupelle, roulement de butée et joint. Dimensions
      et rigidité identiques à la première monte.
  - tier: Equivalent OE (OES)
    description: Fabricants spécialisés en roulements et pièces de suspension. Le corpus RAG cite SKF, SNR et FAG pour cette
      gamme.
  - tier: Kit adaptable multi-véhicules
    description: Kits couvrant plusieurs modèles proches. Vérifier la liste de correspondance précise et que le roulement
      inclus est de qualité acceptable.
  brands:
    premium:
    - Bilstein
    - Sachs
    - KYB
    standard:
    - Monroe
    - Meyle
    - Febi
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Craquement en tournant le volant a l arret
    severity: confort
  - id: S2
    label: Coupelle amortisseur visiblement fissuree deformee
    severity: confort
  - id: S3
    label: Perceptible secouant haut jambe force
    severity: confort
  - id: S4
    label: Tenue de route degradee sur chaussee deformee
    severity: confort
  - id: S5
    label: Odeur de caoutchouc si roulement grippe
    severity: confort
  - id: S6
    label: Amortisseurs remplacer changer meme temps
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : craquement en tournant le volant a l arret'
  quick_checks:
  - 'Observer : craquement en tournant le volant a l arret ?'
  - 'Observer : coupelle amortisseur visiblement fissuree deformee ?'
  - 'Observer : perceptible secouant haut jambe force ?'
  - 'Observer : tenue de route degradee sur chaussee deformee ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Craquement en tournant le volant a l arret
  - Coupelle amortisseur visiblement fissuree deformee
  - Perceptible secouant haut jambe force
  - Tenue de route degradee sur chaussee deformee
  - Odeur de caoutchouc si roulement grippe
  - Amortisseurs remplacer changer meme temps
  good_practices:
  - Controle visuel des fuites et deformations a chaque revision
  - Remplacement par paire (meme essieu) pour equilibre du vehicule
  - Faire verifier la geometrie apres remplacement
  - Inspection des silent-blocs et des rotules associees
rendering:
  pgId: '1632'
  intro_title: A quoi sert Kit de butée de suspension ?
  risk_title: Pourquoi remplacer Kit de butée de suspension a temps ?
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
  - question: Kit butée OE ou adaptable ?
    answer: 'Les kits OES (SKF, SNR, FAG) sont de bonne qualité. Vérifier que le kit contient toutes les pièces : coupelle,
      roulement, butée.'
  - question: Comment savoir si mon kit de butée est HS ?
    answer: Bruit de craquement en tournant le volant à l'arrêt, claquement sur bosses, jeu perceptible au niveau de la coupelle.
  - question: Tous les combien changer le kit de butée ?
    answer: À chaque changement d'amortisseur. Le roulement et la coupelle s'usent ensemble. Durée 80 000 à 150 000 km.
  - question: Peut-on changer le kit de butée soi-même ?
    answer: Oui mais il faut déposer la jambe de force complète. Nécessite compresseur de ressorts. Prévoir 1h30 par côté.
  - question: Quelle erreur éviter avec le kit de butée ?
    answer: Ne pas oublier le roulement de butée. Respecter le couple de serrage de l'écrou central. Vérifier l'état du soufflet.
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
doc_id: bac1ba58-ced3-5f96-96b9-8dd4d8e80931
content_hash: sha256:1d7387dad5485c94
lang: fr
variants:
- name: Version gaz
  aliases:
  - gaz
  - gas-a-just
  functional_differences:
  - Meilleure tenue de route
  - Plus ferme que l huile
- name: Version huile
  aliases:
  - huile
  - hydraulique
  functional_differences:
  - Confort de conduite superieur
  - Moins cher que le gaz
location_on_vehicle:
  area: Entre la roue et la carrosserie (avant et/ou arriere)
  access: Par le dessous (pont elevateur) ou demontage roue
  adjacent_parts:
  - amortisseur
  - ressort
  - bras
  - rotule
installation:
  difficulty: moyen a difficile
  time: 1h a 2h par cote
  tools:
  - compresseur de ressort
  - cle a douille
  - cle dynamometrique
  - arrache-rotule
  prerequisite: Pont elevateur recommande, vehicule decharge
---

# Kit de butée de suspension - Guide Diagnostic Complet

## Fonction et Rôle

Ensemble de fixation supérieure de l'amortisseur

**Actions principales:** supporter, amortir, guider

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- craquement en tournant le volant a l arret
- coupelle amortisseur visiblement fissuree deformee
- perceptible secouant haut jambe force
- tenue de route degradee sur chaussee deformee
- odeur de caoutchouc si roulement grippe
- amortisseurs remplacer changer meme temps

## Procédure de Diagnostic

Pour diagnostiquer un problème de kit de butée de suspension:

1. **Inspection visuelle** - Examiner l'état du kit de butée de suspension
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

- amortisseur
- ressort-de-suspension

## Critères de Compatibilité

Pour commander le bon kit de butée de suspension, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleur confort"

## FAQ

**Kit butée OE ou adaptable ?**
Les kits OES (SKF, SNR, FAG) sont de bonne qualité. Vérifier que le kit contient toutes les pièces : coupelle, roulement, butée.

**Comment savoir si mon kit de butée est HS ?**
Bruit de craquement en tournant le volant à l'arrêt, claquement sur bosses, jeu perceptible au niveau de la coupelle.

**Tous les combien changer le kit de butée ?**
À chaque changement d'amortisseur. Le roulement et la coupelle s'usent ensemble. Durée 80 000 à 150 000 km.

**Peut-on changer le kit de butée soi-même ?**
Oui mais il faut déposer la jambe de force complète. Nécessite compresseur de ressorts. Prévoir 1h30 par côté.

**Quelle erreur éviter avec le kit de butée ?**
Ne pas oublier le roulement de butée. Respecter le couple de serrage de l'écrou central. Vérifier l'état du soufflet.


## References supplementaires

<!-- materialized-from-db guides/choisir-amortisseurs.md 2026-01-08 -->
### Guide - Choisir ses amortisseurs

# Comment choisir ses amortisseurs

## Criteres de choix

### 1. Compatibilite vehicule
- **Marque/Modele/Annee** : Indispensable
- **Motorisation** : Certains moteurs ont des trains differents
- **Type de suspension** : Jambe de force McPherson, multibras, essieu rigide
- **Avec/sans correcteur assiette** : Impacte le choix arriere

### 2. Type de conduite
| Usage | Type recommande |
|-------|-----------------|
| Conduite souple, confort | Gaz standard |
| Conduite mixte | Gaz pression |
| Conduite sportive | Sport/Renforce |
| Tout-terrain/charge | Heavy duty |

### 3. Technologies disponibles

#### Amortisseurs a gaz
- **Pression basse** : Confort, usage standard
- **Pression haute** : Meilleur controle, routes degradees
- **Avantage** : Pas de phenomene de mousse a chaud

#### Amortisseurs a huile
- **Usage** : Vehicules anciens, piece d'origine
- **Inconvenient** : Peut mousser sur long trajet

#### Amortisseurs pilotes
- **Technologie** : Valves electroniques
- **Avantage** : Adaptation automatique
- **Inconvenient** : Cout de remplacement eleve

## Marques de reference

### Premium
| Marque | Specialite |
|--------|------------|
| **Bilstein** | Sport, qualite OEM premium |
| **KYB** | Qualite origine, rapport qualite/prix |
| **Sachs** | Premiere monte VW/BMW/Mercedes |

### Milieu de gamme
| Marque | Specialite |
|--------|------------|
| **Monroe** | Large gamme, bon rapport qualite/prix |
| **Boge** | Qualite allemande |
| **Record** | Budget, garantie 2 ans |

## Regles de remplacement

### Toujours par paire
- **AV gauche + AV droit** ensemble
- **AR gauche + AR droit** ensemble
- **Raison** : Equilibre vehicule, usure uniforme

### Pieces associees
| A remplacer avec | Raison |
|------------------|--------|
| Coupelles/butees | Usure simultanee |
| Soufflets protection | Protection amortisseur |
| Ressorts (si fatigues) | Geometrie correcte |

### Geometrie
- **Obligatoire** : Apres remplacement AV
- **Recommandee** : Apres remplacement AR

## Signes de remplacement necessaire

- Plus de 2 rebonds au test manuel
- Fuite d'huile visible sur corps
- Kilometrage > 80-100 000 km
- Usure pneus irreguliere (facettes)
- Tenue de route degradee

## Conseils pratiques

1. **Ne pas melanger les marques** sur un meme essieu
2. **Commander le kit complet** (amortisseur + butee + soufflet)
3. **Verifier les ressorts** lors du remplacement
4. **Rodage** : 500 km de conduite souple apres montage
5. **Garantie** : Conserver facture (2 ans minimum)

## Symptomes supplementaires

<!-- materialized-from-db diagnostic/amortisseurs.md 2026-01-08 -->
### Diagnostic - Amortisseurs et suspension

# Amortisseurs et suspension - Diagnostic complet

## Symptomes amortisseurs uses

### Rebonds excessifs
- **Quand** : Passage dos d'ane, ralentisseurs
- **Caracteristique** : Vehicule continue de rebondir
- **Test** : Appuyer sur aile, plus de 2 rebonds = use

### Tenue de route degradee
- **Quand** : Virage, freinage, autoroute
- **Caracteristique** : Vehicule flottant, instable
- **Urgence** : Securite - A remplacer rapidement

### Usure pneus anormale
- **Quand** : Controle visuel
- **Caracteristique** : Usure en vagues, facettes
- **Indication** : Amortisseurs HS depuis longtemps

### Bruits de suspension
- **Quand** : Routes degradees
- **Caracteristique** : Claquements, cognements
- **Distinction** : Amortisseur vs silent-bloc vs rotule

## Symptomes ressorts

### Vehicule affaisse
- **Quand** : A l'arret
- **Caracteristique** : Un cote plus bas que l'autre
- **Cause** : Ressort casse ou fatigue

### Bruits metalliques
- **Quand** : Compression suspension
- **Caracteristique** : Claquement sec, grincement
- **Verification** : Coupelle superieure, butee

## Symptomes rotules et silent-blocs

### Jeu dans la direction
- **Quand** : Manoeuvres parking
- **Caracteristique** : Direction floue, impreise
- **Test** : Roue levee, jeu lateral

### Claquements sourds
- **Quand** : Depart, freinage, dos d'ane
- **Caracteristique** : Bruit sourd cote roue
- **Cause probable** : Silent-bloc triangle use

## Causes et solutions - Amortisseurs

### 1. Amortisseurs uses (fuite huile)
- **Probabilite** : 60%
- **Verification** : Traces huile sur corps amortisseur
- **Solution** : Remplacement par paire (essieu)
- **Pieces** : Amortisseurs avant/arriere
- **Urgence** : Haute (securite)

### 2. Coupelles/butees HS
- **Probabilite** : 25%
- **Verification** : Bruit rotation volant a l'arret
- **Solution** : Remplacement kit complet
- **Pieces** : Kit butee + roulement
- **Urgence** : Moyenne

### 3. Ressort casse
- **Probabilite** : 10%
- **Verification** : Inspection visuelle, hauteur caisse
- **Solution** : Remplacement par paire
- **Pieces** : Ressorts de suspension
- **Urgence** : Haute

### 4. Soufflet dechire
- **Probabilite** : 5%
- **Verification** : Poussiere/eau dans amortisseur
- **Solution** : Remplacement amortisseur (soufflet non vendu seul)
- **Pieces** : Amortisseur complet
- **Urgence** : Moyenne

## Causes et solutions - Train roulant

### 1. Silent-blocs triangle uses
- **Probabilite** : 40%
- **Verification** : Jeu visible, caoutchouc craquele
- **Solution** : Remplacement triangle complet ou silent-bloc seul
- **Pieces** : Triangle de suspension, silent-bloc
- **Urgence** : Moyenne

### 2. Rotule de direction usee
- **Probabilite** : 25%
- **Verification** : Jeu rotule (roue levee)
- **Solution** : Remplacement + geometrie
- **Pieces** : Rotule de direction
- **Urgence** : Haute (securite)

### 3. Biellette de barre stabilisatrice
- **Probabilite** : 20%
- **Verification** : Claquement dans virages
- **Solution** : Remplacement biellettes
- **Pieces** : Biellettes stabilisateur
- **Urgence** : Moyenne

### 4. Roulement de roue
- **Probabilite** : 15%
- **Verification** : Ronronnement proportionnel vitesse
- **Solution** : Remplacement roulement
- **Pieces** : Roulement moyeu
- **Urgence** : Haute

## Intervalles de remplacement

| Piece | Kilometrage indicatif |
|-------|----------------------|
| Amortisseurs | 80 000 - 100 000 km |
| Ressorts | Controle apres 120 000 km |
| Silent-blocs | 100 000 - 150 000 km |
| Rotules | 100 000 - 150 000 km |
| Biellettes | 80 000 - 120 000 km |

## Recommandations

- **Remplacement par paire** : Toujours remplacer par essieu (AV gauche + AV droit)
- **Geometrie** : Obligatoire apres remplacement rotules, triangles
- **Kit complet** : Preferer kits avec butee et soufflet
- **Marques** : Bilstein, Monroe, Sachs, KYB (amortisseurs), Lemforder, TRW (train roulant)
- **Controle** : A chaque revision, au CT tous les 2 ans

## Test rapide amortisseurs

1. Stationner sur sol plat
2. Appuyer fortement sur chaque aile
3. Relacher et compter les rebonds
4. **OK** : 1-2 rebonds max
5. **Use** : Plus de 2 rebonds
