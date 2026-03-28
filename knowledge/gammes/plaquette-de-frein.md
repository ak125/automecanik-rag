---
category: freinage
slug: plaquette-de-frein
title: Plaquette de frein
pg_id: 402
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-25'
verification_status: draft
intent_targets:
- diagnostic
- achat
- reference
- entretien
business_priority: high
priority_signals:
  avg_basket: 120
  monthly_searches: 8000
  margin_tier: high
lifecycle:
  stage: auto_generated
  last_enriched_by: script:rag-enrich-metier-templates
  last_enriched_at: '2026-03-26'
_sources:
  ece-r90:
    type: norm
    doc: null
    note: Norme europeenne performances freinage remplacement
  experience-atelier:
    type: field-expertise
    note: Retours atelier partenaire, donnees constructeurs
domain:
  role: La plaquette de frein est la garniture de friction pressee contre le disque par l'etrier hydraulique pour ralentir
    le vehicule de maniere progressive et repetable
  must_be_true:
  - friction
  - etrier
  - disque
  - garniture
  - paire
  must_not_contain:
  - tambour de frein
  - frein a main
  confusion_with:
  - term: disque de frein
    difference: Le disque est le plateau metallique fixe au moyeu; la plaquette est la garniture qui frotte contre le disque
  - term: machoire de frein
    difference: La machoire est utilisee dans un systeme a tambour; la plaquette est specifique au systeme a disque
  related_parts:
  - Disques de frein (a controler systematiquement au changement de plaquettes)
  - Etrier de frein (presse les plaquettes contre le disque)
  - Flexible de frein (transmet la pression hydraulique a l'etrier)
  - Capteur d'usure (alerte quand la garniture atteint l'epaisseur minimale)
  - Liquide de frein (a purger si le circuit a ete ouvert)
  norms:
  - ECE R90 — performances de freinage proches de l'equipement d'origine
  cross_gammes:
  - slug: disque-de-frein
    relation: always_together
    context: Des plaquettes neuves sur des disques uses ne freinent pas correctement. Remplacer conjointement.
  - slug: etrier-de-frein
    relation: check_on_replace
    context: Controler l'etat de l'etrier et des guidages au demontage des plaquettes
  - slug: flexible-de-frein
    relation: check_on_replace
    context: Verifier l'etat du flexible si le circuit hydraulique est ouvert
  - slug: liquide-de-frein
    relation: check_on_replace
    context: Purger le liquide de frein si le circuit hydraulique a ete ouvert
selection:
  criteria:
  - 'Essieu : avant (supporte 70% de l''effort de freinage) ou arriere (stabilite)'
  - 'Materiau : semi-metallique (polyvalent), ceramique (silencieux, peu de poussiere), organique (souple, confort)'
  - Dimensions et reference OE (specifiques au vehicule et a l'etrier)
  - 'Usage : standard (urbain/mixte 20-50 EUR/jeu), haute capacite (montagne 50-80 EUR), sport (80-120 EUR)'
  checklist:
  - Verifier l'essieu concerne (avant ≠ arriere)
  - Commander par jeu de 4 plaquettes (1 essieu complet)
  - Controler l'etat des disques (les changer si uses)
  - Verifier la compatibilite avec le capteur d'usure si present
  - Choisir le materiau adapte a l'usage (urbain, montagne, sport)
  - Privilegier une marque reconnue (Bosch, TRW, Brembo, Ferodo)
  anti_mistakes:
  - Commander pour le mauvais essieu (avant ≠ arriere)
  - Melanger des garnitures de materiaux differents sur un meme essieu
  - Oublier de controler l'etat des disques au changement de plaquettes
  - Choisir uniquement sur le prix sans verifier marque et qualite
  - Ne pas respecter la periode de rodage (200 km de freinage progressif)
  cost_range:
    min: 20
    max: 120
    currency: EUR
    unit: le jeu (4 plaquettes, 1 essieu
    source: catalogue automecanik
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE (OES)
  - tier: Adaptable qualite
  - tier: Reconditionne
  - tier: Echange standard
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
    label: Grincement metallique au freinage
    severity: securite
  - id: S2
    label: Temoin d'usure allume au tableau de bord
    severity: securite
  - id: S3
    label: Distance de freinage allongee
    severity: securite
  causes:
  - Usure normale de la garniture (kilometrage)
  - Freinage intensif repete (conduite urbaine, descentes prolongees)
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  - 'kilometrage eleve ou usure visible : remplacement preventif recommande'
  quick_checks:
  - Inspection visuelle a travers la jante (epaisseur de garniture visible)
  - Ecouter un grincement metallique au freinage leger
  depose_steps: []
maintenance:
  interval:
    value: 30000-50000
    unit: km
    note: Variable selon style de conduite, type de garniture et conduite urbaine vs route
    source: null
  good_practices:
  - Controle visuel a chaque revision
  - Mesure d'epaisseur au pied a coulisse (minimum 3 mm)
  wear_signs:
  - Temoin d'usure qui touche le disque (grincement metallique)
  - Epaisseur de garniture inferieure a 3 mm
rendering:
  pgId: '402'
  intro_title: A quoi sert la plaquette de frein ?
  risk_title: Pourquoi remplacer les plaquettes de frein a temps ?
  risk_explanation: Des plaquettes usees reduisent l'efficacite de freinage et endommagent les disques.
  risk_consequences:
  - Distance de freinage allongee
  - Destruction des disques de frein
  - Grincement metallique permanent
  risk_conclusion: Un controle regulier et un remplacement par essieu complet sont indispensables.
  arguments:
  - title: Compatibilite verifiee
    icon: check-circle
    source_ref: null
  - title: Priorite securite
    icon: shield-check
    source_ref: null
  - title: Decision rapide
    icon: clock
    source_ref: null
  - title: Montage maitrise
    icon: list-check
    source_ref: null
  faq:
  - question: Faut-il changer les 4 plaquettes en meme temps ?
    answer: On remplace les plaquettes par essieu (les 4 d'un meme essieu). Il n'est pas necessaire de changer avant et arriere
      simultanement sauf si les deux sont uses.
  - question: Plaquettes ceramiques ou semi-metalliques ?
    answer: Les ceramiques sont plus silencieuses et generent moins de poussiere. Les semi-metalliques offrent un meilleur
      freinage a haute temperature. Pour un usage urbain standard, les deux conviennent.
  - question: Combien de temps durent les plaquettes ?
    answer: Entre 30 000 et 50 000 km en usage mixte. En conduite urbaine intensive, l'usure peut etre plus rapide.
  - question: Peut-on changer ses plaquettes soi-meme ?
    answer: Le remplacement est accessible a un bricoleur equipe, mais le freinage est un element de securite critique. En
      cas de doute, confiez le montage a un professionnel.
  quality:
    score: 76
    source: stub-manual
    version: GammeContentContract.v4
seo_cluster:
  source: keyword-dataset
  updated_at: '2026-02-23'
  schema_version: '1.0'
  primary_keyword:
    text: plaquettes de freins bosch
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
  keyword_variants:
  - keyword: disque et plaquette de frein clio 4
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
    competition: moyenne
  - keyword: prix disque et plaquette de frein peugeot 308
    volume: 500
    traffic_range: 250-1250/mo
    intent: transactionnelle
    competition: moyenne
  - keyword: prix plaquette et disque de frein clio 4
    volume: 500
    traffic_range: 250-1250/mo
    intent: transactionnelle
    competition: moyenne
  - keyword: prix disque et plaquette de frein peugeot 3008
    volume: 500
    traffic_range: 250-1250/mo
    intent: transactionnelle
    competition: moyenne
  - keyword: plaquettes de frein bmw serie 1
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
    competition: moyenne
  - keyword: prix disque et plaquette de frein peugeot 208
    volume: 500
    traffic_range: 250-1250/mo
    intent: transactionnelle
    competition: moyenne
  - keyword: disque et plaquette de frein 207 prix
    volume: 50
    traffic_range: 25-125/mo
    intent: transactionnelle
    competition: faible
  - keyword: disque et plaquette de frein citroën c3
    volume: 50
    traffic_range: 25-125/mo
    intent: informationnelle
    competition: faible
  - keyword: disque et plaquette de frein c4 picasso prix
    volume: 50
    traffic_range: 25-125/mo
    intent: transactionnelle
    competition: faible
  - keyword: prix disque et plaquette de frein c3
    volume: 50
    traffic_range: 25-125/mo
    intent: transactionnelle
    competition: faible
  paa_questions: []
  role_mapping:
    R1: prix disque et plaquette de frein peugeot 308
    R3_guide: plaquettes de freins bosch
    R3_conseils: quand changer plaquette de frein
    R4: plaquette de frein definition
    R5: symptome plaquette de frein use
doc_id: 06dbeae8-79b3-5241-9d4c-a1157becc7a5
content_hash: sha256:114f27b86d0c95b7
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

# Plaquette de frein

## FAQ

**Faut-il changer les 4 plaquettes en meme temps ?**
On remplace les plaquettes par essieu (les 4 d'un meme essieu). Il n'est pas necessaire de changer avant et arriere simultanement sauf si les deux sont uses.

**Plaquettes ceramiques ou semi-metalliques ?**
Les ceramiques sont plus silencieuses et generent moins de poussiere. Les semi-metalliques offrent un meilleur freinage a haute temperature. Pour un usage urbain standard, les deux conviennent.

**Combien de temps durent les plaquettes ?**
Entre 30 000 et 50 000 km en usage mixte. En conduite urbaine intensive, l'usure peut etre plus rapide.

**Peut-on changer ses plaquettes soi-meme ?**
Le remplacement est accessible a un bricoleur equipe, mais le freinage est un element de securite critique. En cas de doute, confiez le montage a un professionnel.

## Entretien et Intervalles

- **Intervalle** : 30000-50000
- Variable selon style de conduite, type de garniture et conduite urbaine vs route


## References supplementaires

<!-- materialized-from-db canonical/freinage__choisir-plaquettes.md 2026-02-22 -->
### Freinage - choisir ses plaquettes

## Choix rapide

Choisir des plaquettes compatibles vehicule (VIN/immat), privilegier des references conformes (ex ECE R90), et adapter la gamme a l'usage (urbain, charge, conduite soutenue). Verifier aussi l'etat des disques avant remplacement.

<!-- materialized-from-db reference/freinage__ece-r90.md 2026-03-03 -->
### ECE R90 - definition

## Definition

La norme ECE R90 encadre la conformite des pieces de freinage de remplacement (ex: plaquettes, disques) avec des exigences de performance proches de l'equipement d'origine.

## Pourquoi c'est important

- meilleure coherence de freinage
- reduction du risque de pieces non conformes
- reference utile pour le choix de pieces sur vehicule de tourisme

## Points a verifier

- mention ECE R90 sur le produit/emballage
- correspondance avec la reference vehicule
- provenance et tracabilite

<!-- materialized-from-db guides/identifier-panne-auto.md 2026-02-21 -->
### Guide - Comment identifier une panne auto : methodes, signes et urgences

# Comment identifier une panne auto : guide complet

## Pourquoi identifier soi-meme sa panne ?

Un diagnostic precoce permet d'eviter une panne totale, de reduire le cout de reparation et d'arriver chez le garagiste avec une hypothese claire. 80% des pannes presentent des signes avant-coureurs pendant plusieurs semaines avant l'immobilisation.

## Les 3 methodes pour identifier une panne auto

### 1. Observer les symptomes sensoriels (sans outil)

Chaque organe du vehicule communique par un canal sensoriel distinct :

| Canal | Exemples | Zone probable |
|-------|----------|---------------|
| Auditif | Sifflement, claquement, grincement | Freinage, suspension, moteur |
| Visuel | Fumee, voyant, fuite | Moteur, circuit de refroidissement, freins |
| Tactile | Vibration, a-coup, pedale molle | Suspension, embrayage, freinage |
| Olfactif | Odeur de brule, de caoutchouc | Embrayage, freins, circuit electrique |

### 2. Lire les voyants du tableau de bord

Les voyants sont le premier niveau de diagnostic embarque. Leur couleur indique l'urgence :
- Rouge : arret immediat obligatoire (huile, temperature, frein)
- Orange : attention requise rapidement (moteur, ABS, FAP)
- Jaune/vert : information (entretien, assistance parking)

Un voyant orange moteur (check engine) indique une anomalie enregistree dans le calculateur. La lecture des codes OBD avec un scanner (protocole OBD2 depuis 2001) permet d'identifier le defaut exact.

### 3. Scanner le code OBD (P, C, B, U)

Les codes OBD se lisent avec un scanner OBD2 (disponibles a partir de 30 EUR) :
- P0xxx : moteur et transmission
- C0xxx : chassis (ABS, ESP)
- B0xxx : carrosserie (airbags, sieges)
- U0xxx : reseau de communication

## Les 10 signes avant-coureurs d'une panne

1. **Bruit inhabituel au freinage** — sifflement aigu = plaquettes usees, grincement = disques ou etrier
2. **Voyant moteur allume** — code OBD a lire dans les 48h
3. **Vibration au volant** — a vitesse constante : pneumatiques ; au freinage : disques voiles
4. **Demarrage difficile** — lent, bruyant ou manque = batterie, demarreur ou alternateur
5. **Surconsommation soudaine** — injecteurs, bougie, fuite circuit d'alimentation
6. **Fumee a l'echappement** — blanche = liquide de refroidissement ; noire = richesse essence ; bleue = huile
7. **Perte de puissance** — turbo, FAP obstrue, injecteurs defaillants
8. **Odeur de brule** — embrayage en patinage, frein grippe, court-circuit electrique
9. **Pedale de frein molle** — fuite liquide de frein, plaquettes usees extremes
10. **Voyant ABS ou ESP** — capteur de roue, bloc hydraulique

## Panne mecanique vs electrique : comment distinguer

| Critere | Mecanique | Electrique |
|---------|-----------|------------|
| Manifestation | Progressive, sonore, vibratoire | Soudaine, voyant allume |
| Temperature | Souvent liee a la montee en temperature | Independante |
| Diagnostic | Inspection visuelle, ecoute | Scanner OBD indispensable |
| Exemples | Usure plaquettes, joint HS, courroie | Capteur O2, calculateur, alternateur |

## Que faire en cas de panne sur autoroute ?

**Priorite absolue : securiser le vehicule et les occupants.**

1. Allumer les feux de detresse immediatement
2. Se garer sur la bande d'arret d'urgence (BAU), le plus a droite possible
3. Couper le moteur et serrer le frein a main
4. Sortir du vehicule par la droite et s'eloigner de la glissiere
5. Revetir le gilet de securite (obligatoire)
6. Poser le triangle de signalisation a 150m minimum (si possible sans danger)
7. Appeler le 3477 (societe d'autoroute) depuis une borne d'appel orange ou votre telephone

**Ne jamais tenter de reparer sur la BAU.** Appelez le prestataire agree de l'autoroute.

## FAQ : Identifier sa panne auto

### Comment savoir quel est le probleme de ma voiture ?
Commencez par observer les symptomes : voyants allumes, bruits, vibrations, odeurs. Si un voyant moteur est allume, lisez le code OBD avec un scanner. Pour les pannes sans voyant, decrivez le symptome (canal sensoriel + moment d'apparition) dans notre outil de diagnostic.

### Comment identifier une panne de demarreur ?
Un demarreur defaillant se manifeste par un clic unique sans demarrage (relais de demarrage), un grincement de courte duree, ou une absence totale de reaction moteur alors que la batterie est chargee. Le diagnostic se confirme en mesurant la tension aux bornes du demarreur lors de la sollicitation.

### Qu'est-ce qu'une panne voyant ABS ?
Le voyant ABS orange indique une defaillance du systeme antiblocage. Le freinage normal reste fonctionnel mais l'assistance ABS est desactivee. Cause la plus frequente : capteur ABS de roue defaillant (50-80 EUR la piece). Ne pas ignorer : rouler sans ABS est legalement autorise mais deconseille.

### Comment lire un code panne voiture ?
Branchez un scanner OBD2 sur le port OBD situe sous le tableau de bord (cote conducteur, generalement sous la colonne de direction). Selectionnez "Lire les codes defaut". Le code P0xxx s'interprete via notre outil ou des bases specialisees. Effacez le code seulement apres reparation.

### Voiture en panne qui ne demarre pas : par ou commencer ?
Verifiez dans cet ordre : 1) Batterie (tension > 12.4V), 2) Demarreur (bruit de clic = OK cote relais), 3) Bobines et bougies (si moteur tourne mais cale), 4) Circuit d'alimentation (pompe a carburant). Un diagnostic OBD indique souvent la piste exacte.

### Panne mecanique ou electrique : comment savoir ?
Une panne mecanique est generalement progressive et s'accompagne de bruits ou vibrations. Une panne electrique est souvent soudaine avec voyant allume. L'outil de diagnostic OBD lit les defauts electroniques ; une inspection physique confirme les pannes mecaniques.

### Que faire si un voyant rouge s'allume en conduisant ?
Un voyant rouge impose l'arret immediat securise du vehicule (huile moteur, temperature moteur, frein). Garez-vous des que possible en securite, coupez le moteur, et n'attendez pas que la situation empire. Relancer un moteur surchauffe ou en manque de pression d'huile cause des dommages irreversibles.

<!-- materialized-from-db guides/selecteur-vehicule-pieces-auto.md 2026-02-17 -->
### Guide - Sélecteur de véhicule pièces auto : 4 méthodes

# Sélecteur de véhicule pièces auto : 4 méthodes pour trouver la bonne pièce

Chaque véhicule a des spécifications techniques uniques : dimensions de disques, type de fixation, connecteurs électriques. Commander une pièce incompatible peut entraîner un montage impossible, un dysfonctionnement ou un danger. Le sélecteur de véhicule pièces auto garantit que seules les pièces compatibles avec votre véhicule vous sont proposées parmi les 4 millions de références du catalogue Automecanik.

4 méthodes disponibles : plaque d'immatriculation, numéro VIN, sélection manuelle (marque/modèle/motorisation), ou référence OEM.

## Mots-clés et expressions SEO

### Intention informationnelle
- comment trouver pièce auto compatible avec mon véhicule
- comment être sûr de commander la bonne pièce auto
- comment savoir le type de motorisation de ma voiture
- c'est quoi F1 F2 F3 sur une carte grise
- quelle est la différence entre type mine et code moteur
- où trouver le numéro VIN de mon véhicule
- quelle est la différence entre pièce d'origine et pièce équipementier
- où trouver un logiciel de vue éclatée automobile gratuit
- comment trouver la référence d'une pièce auto
- mon véhicule a des variantes de montage : comment choisir la bonne pièce

### Intention commerciale
- sélecteur de véhicule pièces auto
- configurateur de pièces auto en ligne
- pièce auto avec carte grise
- numéro VIN 17 caractères pièces auto
- guide pratique choisir pièces auto
- sélection des pièces détachées par modèle de voiture
- information voiture avec plaque d'immatriculation gratuit

### Intention transactionnelle
- recherche pièces auto par plaque d'immatriculation
- trouver pièce auto avec numéro de châssis
- chercher pièce détachée par référence OEM
- trouver code moteur avec VIN gratuit
- trouver numéro OEM avec VIN gratuit

### Intention navigationnelle
- Automecanik sélecteur véhicule
- Automecanik recherche par immatriculation
- Automecanik recherche par VIN

## Les 4 méthodes d'identification

### 1. Par immatriculation (la plus rapide)

Saisissez votre numéro de plaque au format SIV (AA-123-BB) ou ancien format FNI. Le système identifie automatiquement votre véhicule en quelques secondes. C'est la recherche de pièces auto par plaque d'immatriculation la plus rapide pour les plaques françaises.

**Ce qu'il faut** : plaque française (SIV ou FNI)
**Fiabilité** : bonne (si la base est à jour)
**Limitation** : les plaques étrangères ne sont pas reconnues
**Recommandé si** : vous êtes sur le véhicule ou vous avez la plaque sous les yeux. Fonctionne aussi avec la carte grise (pièce auto par carte grise).

### 2. Par numéro VIN (la plus fiable)

Saisissez les 17 caractères du VIN (visible sur la carte grise au champ E ou sur le pare-brise côté conducteur). Cette méthode offre 99%+ de fiabilité et identifie la configuration exacte sortie d'usine, y compris pour les véhicules importés.

**Ce qu'il faut** : VIN de 17 caractères (carte grise champ E)
**Fiabilité** : excellente (99%+)
**Limitation** : le VIN n'est pas toujours sous la main
**Recommandé si** : pièces de sécurité (freins, suspension), véhicule importé, ou variantes de montage. Permet aussi de trouver le code moteur avec le VIN gratuitement.

### 3. Sélection manuelle — marque, modèle, motorisation (toujours disponible)

Sélectionnez successivement la marque (champ D.1 de la carte grise), le modèle/génération, l'année (champ B) et la motorisation (champ P.3). En cas de doute entre 2 motorisations proches, utilisez la recherche par VIN.

**Ce qu'il faut** : marque, modèle, année, motorisation
**Fiabilité** : bonne (si la motorisation exacte est sélectionnée)
**Limitation** : doute possible entre motorisations proches
**Recommandé si** : vous connaissez votre véhicule. Fonctionne sans carte grise. Sélection des pièces détachées par modèle de voiture.

### 4. Par référence OEM (la plus précise)

Saisissez le numéro OEM (Origine Équipementier) gravé sur la pièce d'origine pour trouver l'équivalent exact ou les alternatives compatibles chez d'autres fabricants. C'est la méthode pour chercher une pièce détachée par sa référence OEM avec 100% de précision.

**Ce qu'il faut** : numéro OE gravé sur la pièce usagée
**Fiabilité** : maximale (100%)
**Limitation** : nécessite d'avoir la pièce usagée sous les yeux
**Recommandé si** : vous avez le numéro OE de l'ancienne pièce. Permet un remplacement à l'identique garanti et de trouver les équivalences équipementiers.

## Tableau comparatif des méthodes

| Critère | Immatriculation | VIN | Manuelle | OEM |
|---------|-----------------|-----|----------|-----|
| **Fiabilité** | Bonne (si base à jour) | Excellente (99%+) | Bonne (si motorisation exacte) | Maximale (100%) |
| **Vitesse** | Quelques secondes | Quelques secondes | 1-2 minutes | Instantané |
| **Ce qu'il faut** | Plaque française (SIV/FNI) | 17 caractères (carte grise champ E) | Marque, modèle, année, motorisation | Numéro OE (gravé sur la pièce) |
| **Quand l'utiliser** | Commandes courantes | Pièces sécurité, variantes, import | Sans carte grise, véhicule connu | Remplacement à l'identique |
| **Limitation** | Plaques étrangères non reconnues | VIN pas toujours sous la main | Doute entre motorisations proches | Pièce usagée nécessaire |

## Carte grise — champs utiles pour identifier son véhicule

| Champ | Contenu | Utilité pour le sélecteur |
|-------|---------|---------------------------|
| **B** | Date de première immatriculation | Année du véhicule (étape 3 sélection manuelle) |
| **D.1** | Marque du véhicule | Étape 1 sélection manuelle |
| **D.2** | Type mine / variante / version | Identification précise de la version |
| **E** | Numéro VIN (17 caractères) | Méthode VIN — 99%+ de fiabilité |
| **P.3** | Type de carburant (essence, diesel, hybride, électrique, GPL) | Motorisation — étape 4 sélection manuelle |
| **F.1** | Masse en charge maximale techniquement admissible (PTAC) | Dimensionner freinage et suspension |
| **F.2** | PTAC de l'ensemble (véhicule + remorque) | Dimensionner freinage |
| **F.3** | Masse en charge maximale de l'ensemble en service (PTRA) | Dimensionner suspension (amortisseurs, ressorts) |

**Astuce** : prenez votre carte grise en photo avec votre téléphone. Vous aurez toutes les infos sous la main la prochaine fois, même loin du véhicule.

## Variantes de montage

Les constructeurs automobiles utilisent plusieurs fournisseurs pour une même pièce. En cours de production, ils peuvent changer de fournisseur, modifier des spécifications ou ajouter des options.

### Pourquoi les variantes existent

- **Multi-fournisseurs** : un même modèle peut être équipé en première monte par différents équipementiers selon la date et le lieu de fabrication.
- **Évolutions en série** : les constructeurs améliorent les pièces en continu. Un véhicule de début de série peut avoir des spécifications différentes d'un véhicule de fin de série.
- **Options d'usine** : les packs sport, suspensions pilotées ou systèmes Start & Stop modifient les pièces requises.

### Exemples courants de variantes (même véhicule)

| Catégorie | Variante |
|-----------|----------|
| **Freinage** | Diamètre disque 280 vs 288 vs 312 mm, ventilé vs plein |
| **Batterie** | Start & Stop → AGM/EFB obligatoire |
| **Filtration** | Cartouche vs vissé selon moteur |
| **Suspension** | Standard vs sport / pilotée |

### Comment éviter l'erreur

1. Vérifiez les critères clés sur la fiche produit (diamètre, capteur, type de fixation).
2. Privilégiez le VIN quand c'est disponible — 99% de compatibilité.
3. En cas de doute : comparez le numéro OE de l'ancienne pièce avec les références proposées. Le numéro OE = la meilleure confirmation.

## Dépannage

### Mon véhicule n'apparaît pas dans le sélecteur

**Cause probable** : véhicule importé, très récent, ou plaque étrangère non reconnue.
**Solution** : passez en recherche par VIN (champ E de la carte grise). Les véhicules importés depuis l'Allemagne ou la Belgique sont généralement reconnus par VIN même si la plaque ne fonctionne pas.

### J'hésite entre deux motorisations proches

**Cause probable** : le modèle existe avec plusieurs cylindrées ou puissances similaires (ex : 1.5 dCi 90ch vs 1

[...]
