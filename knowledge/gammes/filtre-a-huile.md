---
category: filtration
slug: filtre-a-huile
title: Filtre à huile
pg_id: 7
source_type: gamme
doc_family: catalog
truth_level: L3
updated_at: '2026-03-25'
verification_status: verified
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
completeness_profile: filtration
lifecycle:
  stage: v4_converted
  last_enriched_by: script:rag-enrich-metier-templates
  last_enriched_at: '2026-03-26'
domain:
  role: Filtre l'huile moteur pour retenir les impuretés métalliques et résidus de combustion, protégeant pistons, bielles
    et arbre à cames
  must_be_true:
  - filtrer
  - retenir impuretés
  - protéger moteur
  - lubrification
  must_not_contain:
  - accessoires
  - alternateur
  - climatisation
  - servitude
  - universel
  - tous moteurs
  confusion_with:
  - term: filtre-a-air
    difference: Filtre à huile = filtre l'huile moteur, Filtre à air = filtre l'air admission
  - term: filtre-a-carburant
    difference: Filtre à huile = huile moteur, Filtre à carburant = essence/diesel
  - term: filtre-a-huile-boite
    difference: Filtre à huile moteur = filtre le circuit de lubrification moteur, Filtre à huile de boîte = filtre l'huile
      de la transmission automatique
  norms:
  - ISO 4548-12 (efficacité de filtration multi-pass)
  - ISO 4548-1 (résistance pression différentielle)
  - Spécifications constructeur (ex: VW 502.00, BMW LL-01 exigent filtre certifié)
  related_parts:
  - huile-moteur
  - joint-de-vidange-carter
  - filtre-a-air
  - filtre-a-carburant
  - filtre-d-habitacle
  - bouchon-de-vidange
variants:
- name: Filtre à visser (spin-on)
  aliases:
  - filtre vissable
  - spin-on
  visual_differences:
  - cylindrique métallique avec filetage visible en bas
  - coque acier peinte (blanc, noir, bleu selon marque)
  functional_differences:
  - remplacement complet filtre + coque
  - joint torique intégré
- name: Filtre à cartouche (insert)
  aliases:
  - cartouche filtrante
  - élément filtrant
  visual_differences:
  - papier plissé sans coque métallique
  - logé dans un boîtier moteur réutilisable
  functional_differences:
  - seul le média filtrant est remplacé
  - boîtier réutilisable avec couvercle à dévisser
- name: Filtre centrifuge
  aliases:
  - filtre centrifuge à huile
  visual_differences:
  - rotor métallique compact
  - principalement utilitaires et poids lourds
  functional_differences:
  - nettoyage possible selon modèle
  - usage poids lourds et industriel
location_on_vehicle:
  area: bloc moteur
  access: par dessous ou par dessus selon motorisation
  adjacent_parts:
  - carter d'huile
  - bouchon de vidange
  - tuyauterie d'huile
  - collecteur d'échappement (proximité)
key_visual_features:
  identifying_shapes:
  - cylindre métallique fileté (spin-on)
  - cartouche papier plissé dans boîtier plastique ou alu (insert)
  identifying_materials:
  - acier peint (spin-on)
  - papier cellulose ou synthétique plissé (cartouche)
  - joint torique caoutchouc (les deux types)
selection:
  criteria:
  - Marque de votre vehicule
  - Modele de votre vehicule
  - Motorisation de votre vehicule
  - Type de filtre monte (vissant spin-on ou cartouche element filtrant)
  - Reference constructeur OEM (si disponible)
  - Diametre du filetage et joint torique
  - Pression differentielle supportee (bar)
  - Presence clapet anti-retour (obligatoire moteurs modernes)
  - Presence clapet by-pass (protection moteur si colmatage)
  - Compatibilite huile longlife (VW 502.00, BMW LL-01)
  criteria_enriched_sources:
  - web-catalog/f693354c7bf0 (MANN-FILTER types et specifications)
  - web-catalog/d2e427d74f38 (SOFIMA filtration types et efficacite)
  - web-catalog/8c1a4aa61267 (DENSO filtres huile catalogue)
  - web/7377bedb9c7e (anatomy spin-on et cartouche filters)
  - web/777af1b0088d (how oil filters work - detailed components)
  anti_mistakes:
  - ❌ "garanti moteur"
  - ❌ "zéro usure"
  - ❌ "sécurité garantie"
  cost_range:
    min: 4
    max: 17
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: OEM
    description: Qualité constructeur ou équivalent direct
    price_range: 15-40€
  - tier: Premium aftermarket
    description: Haute qualité aftermarket, très bonne filtration et tenue
    price_range: 8-25€
  - tier: Standard
    description: Bon compromis usage courant et budget
    price_range: 5-15€
  brands:
    premium:
    - Mann-Filter
    - Mahle
    - Hengst
    standard:
    - Bosch
    - Purflux
    - Filtron
    budget:
    - Ridex
    - Kamoka
diagnostic:
  symptoms:
  - id: S1
    label: Voyant huile qui s allume ou clignote
    severity: urgence
  - id: S2
    label: Bruit de claquement ou de cliquetis au ralenti
    severity: urgence
  - id: S3
    label: Huile tres noire avant echeance vidange
    severity: confort
  - id: S4
    label: Baisse du niveau d huile plus rapide
    severity: attention
  - id: S5
    label: Odeur d huile brulee dans l habitacle
    severity: attention
  causes:
  - Filtre colmate par accumulation d impuretes metalliques et residus de combustion
  - Intervalle de vidange depasse ou huile de mauvaise viscosite
  - Joint torique defaillant ou ancien joint reste colle causant une fuite
  - Clapet by-pass bloque en position ouverte laissant passer l huile non filtree
  depose_steps: []
  quick_checks:
  - Voyant huile qui s allume ou clignote ?
  - Bruit de claquement ou de cliquetis au ralenti ?
  - 'Observer : huile tres noire avant echeance vidange ?'
  - 'Observer : baisse du niveau d huile plus rapide ?'
maintenance:
  interval:
    value: 10000-30000 km selon constructeur
    unit: km
    note: Essence classique 10 000-15 000 km (ou 1 an). Diesel moderne 15 000-20 000 km. Longlife (VW/BMW) jusqu'à 30 000
      km. Se change à chaque vidange.
    source: champion-autoparts+revue-technique-auto-2026-03
    timing_years: 1-2 ans (essence 1 an, diesel 1-1.5 ans, longlife 2 ans)
  wear_signs:
  - Voyant huile qui s allume ou clignote
  - Bruit de claquement ou de cliquetis au ralenti
  - Huile tres noire avant echeance vidange
  - Baisse du niveau d huile plus rapide
  - Odeur d huile brulee dans l habitacle
  good_practices:
  - Remplacement systematique selon intervalle constructeur
  - Ne pas souffler a l air comprime (endommage le media filtrant)
  - Controle visuel a chaque vidange ou entretien
  - Verifier l etancheite du boitier apres remplacement
rendering:
  pgId: '7'
  intro_title: A quoi sert Filtre à huile ?
  risk_title: Pourquoi remplacer Filtre à huile a temps ?
  risk_explanation: '**Colmatage progressif** - Le filtre retient de plus en plus de particules jusqu au seuil critique ou
    le clapet by-pass s ouvre'
  risk_consequences:
  - '**Colmatage du filtre** - L huile non filtree circule via le clapet by-pass, accelerant l usure des organes moteur'
  - '**Perte de pression d huile** - Le voyant s allume, risque de casse moteur si ignore'
  - '**Usure prematuree** - Les impuretes metalliques abrasent pistons, bielles et arbre a cames'
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
  - question: 'Filtre à huile OE ou adaptable : que choisir ?'
    answer: Les filtres OES (Bosch) ou adaptables (Mann, Mahle) offrent une qualité équivalente à l'OE pour moins cher. Vérifiez
      le filetage et le diamètre du joint.
  - question: Comment savoir si mon filtre à huile est bouché ?
    answer: Voyant huile allumé, bruit de cliquetis moteur, huile noire et épaisse à la jauge, consommation d'huile excessive.
  - question: Tous les combien changer le filtre à huile ?
    answer: À chaque vidange, soit entre 15 000 et 30 000 km ou 1 an. Ne jamais réutiliser un ancien filtre même récent.
  - question: Peut-on changer le filtre à huile soi-même ?
    answer: Oui, opération simple lors de la vidange. Clé à filtre nécessaire. Graisser le joint neuf avec de l'huile. Serrage
      à la main + 3/4 de tour.
  - question: Quelle erreur éviter avec le filtre à huile ?
    answer: Ne pas trop serrer (écrase le joint). Ne pas oublier de retirer l'ancien joint collé sur le bloc. Toujours pré-remplir
      le filtre si possible.
  - question: Peut-on changer le filtre à huile sans faire la vidange ?
    answer: Techniquement possible mais déconseillé. Retirer le filtre entraîne une perte d'huile. Le filtre neuf dans de
      l'huile usagée ne remplit pas pleinement son rôle.
  - question: Le joint torique se change-t-il en même temps que le filtre ?
    answer: Oui, systématiquement. Sur filtre cartouche, le joint torique est souvent fourni. Erreur fréquente — toujours
      vérifier que l'ancien joint n'est pas resté collé sur le bloc.
  quality:
    score: 88
    source: manual-research-2026-03-03
    version: GammeContentContract.v4
seo_cluster:
  source: keyword-dataset
  updated_at: '2026-02-23'
  schema_version: '1.0'
  primary_keyword:
    text: filtre a huile
    volume: 5000
    traffic_range: 2500-12500/mo
    intent: informationnelle
  keyword_variants:
  - keyword: filtre huile
    volume: 5000
    traffic_range: 2500-12500/mo
    intent: informationnelle
    competition: forte
  - keyword: filtre a huile citroen c3
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
    competition: moyenne
  - keyword: filtre a huile scenic 3
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
    competition: moyenne
  - keyword: filtre a huile ds3
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
    competition: moyenne
  - keyword: filtre a huile golf 7
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
    competition: moyenne
  - keyword: filtre huile purflux
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
    competition: moyenne
  - keyword: filtre a huile 206
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
    competition: moyenne
  - keyword: filtre huile clio 3
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
    competition: moyenne
  - keyword: filtre a huile twingo 1
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
    competition: moyenne
  - keyword: filtres à huile purflux
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
    competition: moyenne
  paa_questions:
  - Comment savoir quel filtre à huile prendre ?
  - Comment savoir quelle taille de filtre il me faut ?
  - Quels sont les différents types de filtres à huile ?
  - Comment choisir un filtre à huile de qualité ?
  - Comment savoir si le filtre à huile est à changer ?
  - Quelle est la durée de vie d'un filtre à huile ?
  - Un filtre à huile peut-il durer 16 000 kilomètres ?
  - Quand changer les 3 filtres ?
  - Quelles sont les meilleures marques de filtres à huile ?
  - Est-ce important de choisir la marque du filtre à huile ?
  - Est-ce que MANN-FILTER est une bonne marque ?
  - Qui fabrique les filtres à huile Norauto ?
  - Quel est le prix d'un filtre à huile ?
  - Quel est le prix d'un changement de filtre à huile ?
  - Puis-je utiliser n'importe quel filtre à huile compatible ?
  - Que se passe-t-il si j'utilise le mauvais filtre à huile ?
  - La plupart des filtres à huile sont-ils universels ?
  - Quelles sont les conséquences d'un mauvais filtre à huile ?
  - Est-ce possible de changer un filtre à huile sans faire la vidange ?
  - Le joint torique doit-il être remplacé à chaque vidange d'huile ?
  role_mapping:
    R1: prix filtre a huile citroen c3
    R3_guide: filtre a huile
    R3_conseils: quand changer filtre a huile
    R4: filtre a huile definition
    R5: symptome filtre a huile use
    R6: guide achat filtre a huile
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous moteurs
  requires_vehicle: true
doc_id: 9f4ada19-1a13-5d86-96e2-0e4541b3f643
content_hash: sha256:18baf863684a01f4
lang: fr
installation:
  difficulty: facile
  time: 10 a 30 min
  tools:
  - tournevis
  - cle a filtre (huile)
  - chiffon
  prerequisite: Moteur froid pour filtre a huile
---

# Filtre à huile - Guide Diagnostic Complet

## Fonction et Rôle

Filtre l'huile moteur pour retenir les impuretés métalliques et résidus de combustion, protégeant pistons, bielles et arbre à cames.

**Actions principales:** filtrer, protéger, retenir les particules, maintenir huile propre


## Types et Variantes

### Filtre à visser (spin-on)
Aussi appelé : filtre vissable, spin-on.
- cylindrique métallique avec filetage visible en bas
- coque acier peinte (blanc, noir, bleu selon marque)
- remplacement complet filtre + coque
- joint torique intégré

### Filtre à cartouche (insert)
Aussi appelé : cartouche filtrante, élément filtrant.
- papier plissé sans coque métallique
- logé dans un boîtier moteur réutilisable
- seul le média filtrant est remplacé
- boîtier réutilisable avec couvercle à dévisser

### Filtre centrifuge
Aussi appelé : filtre centrifuge à huile.
- rotor métallique compact
- principalement utilitaires et poids lourds
- nettoyage possible selon modèle
- usage poids lourds et industriel

## Symptômes de Défaillance

### 🔴 Urgence

- **Voyant huile qui s allume ou clignote** — pression insuffisante, risque casse moteur
- **Bruit de claquement ou de cliquetis au ralenti** — lubrification degradee

### 🟠 Attention

- **Baisse du niveau d huile plus rapide** — fuite possible ou consommation excessive
- **Odeur d huile brulee dans l habitacle** — fuite sur collecteur ou filtre defaillant

### 🟢 Confort

- **Huile tres noire avant echeance vidange** — filtre sature, vidange a prevoir

## Procédure de Diagnostic

Pour diagnostiquer un problème de filtre à huile:

1. **Inspection visuelle** - Examiner l'état du filtre à huile
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : 10000-30000 km selon constructeur
- Essence classique 10 000-15 000 km (ou 1 an). Diesel moderne 15 000-20 000 km. Longlife (VW/BMW) jusqu'à 30 000 km. Se change à chaque vidange.
- **Timing** : 1-2 ans (essence 1 an, diesel 1-1.5 ans, longlife 2 ans)

## Causes Probables

- **Filtre colmate** - Accumulation d impuretes metalliques et residus de combustion au-dela de la capacite du filtre
- **Vidange en retard** - Intervalle depasse ou huile de mauvaise viscosite accelerant le colmatage
- **Joint torique defaillant** - Ancien joint reste colle sur le bloc moteur causant une fuite
- **Clapet by-pass bloque** - En position ouverte, l huile non filtree circule dans le moteur

## Pièces Associées

Lors du remplacement, verifier egalement:

- huile-moteur
- joint-de-vidange-carter
- filtre-a-air
- filtre-a-carburant
- filtre-d-habitacle
- bouchon-de-vidange

## ⚠️ Ne Pas Confondre Avec

### filtre-a-air
**Distinction:** Filtre à huile = filtre l'huile moteur, Filtre à air = filtre l'air admission

### filtre-a-carburant
**Distinction:** Filtre à huile = huile moteur, Filtre à carburant = essence/diesel

### filtre-a-huile-boite
**Distinction:** Filtre à huile moteur = filtre le circuit de lubrification moteur, Filtre à huile de boîte = filtre l'huile de la transmission automatique

## Critères de Compatibilité

Pour commander le bon filtre à huile, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Motorisation** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "garanti moteur"
- ❌ "zéro usure"
- ❌ "sécurité garantie"

## FAQ

**Filtre à huile OE ou adaptable : que choisir ?**
Les filtres OES (Bosch) ou adaptables (Mann, Mahle) offrent une qualité équivalente à l'OE pour moins cher. Vérifiez le filetage et le diamètre du joint.

**Comment savoir si mon filtre à huile est bouché ?**
Voyant huile allumé, bruit de cliquetis moteur, huile noire et épaisse à la jauge, consommation d'huile excessive.

**Tous les combien changer le filtre à huile ?**
À chaque vidange, soit entre 15 000 et 30 000 km ou 1 an. Ne jamais réutiliser un ancien filtre même récent.

**Peut-on changer le filtre à huile soi-même ?**
Oui, opération simple lors de la vidange. Clé à filtre nécessaire. Graisser le joint neuf avec de l'huile. Serrage à la main + 3/4 de tour.

**Quelle erreur éviter avec le filtre à huile ?**
Ne pas trop serrer (écrase le joint). Ne pas oublier de retirer l'ancien joint collé sur le bloc. Toujours pré-remplir le filtre si possible.

**Peut-on changer le filtre à huile sans faire la vidange ?**
Techniquement possible mais déconseillé. Retirer le filtre entraîne une perte d'huile. Le filtre neuf dans de l'huile usagée ne remplit pas pleinement son rôle.

**Le joint torique se change-t-il en même temps que le filtre ?**
Oui, systématiquement. Sur filtre cartouche, le joint torique est souvent fourni. Erreur fréquente — toujours vérifier que l'ancien joint n'est pas resté collé sur le bloc.


## References supplementaires

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

**Cause probable** : le modèle existe avec plusieurs cylindrées ou puissances similaires (ex : 1.5 dCi 90ch vs 110ch).
**Solution** : utilisez le VIN pour identifier la configuration exacte. Sinon, vérifiez le champ P.3 (carburant) et D.2 (type mine) sur votre carte grise.

### Le sélecteur propose plusieurs variantes pour une même pièce

**Cause probable** : le constructeur a utilisé plusieurs fournisseurs ou modifié les spécifications en cours de production.
**Solution** : mesurez la pièce actuelle (diamètre, nombre de trous) ou relevez le numéro OE gravé dessus. Ce numéro est la confirmation la plus fiable.

### La pièce affichée est marquée "compatible" mais je ne suis pas sûr

**Cause probable** : doute sur la variante de montage ou les options du véhicule.
**Solution** : comparez le numéro OE de votre pièce actuelle avec les références proposées. Si le doute persiste, contactez notre service client avec votre carte grise.

## FAQ — 14 questions-réponses

### Q : Pourquoi dois-je sélectionner mon véhicule avant de commander des pièces auto ?

Chaque véhicule a des spécifications techniques uniques : dimensions de disques, type de fixation, connecteurs électriques. Commander une pièce incompatible peut entraîner un montage impossible, un dysfonctionnement ou un danger. Le sélecteur de véhicule pièces auto garantit que seules les pièces compatibles avec votre véhicule vous sont proposées. Sans sélection, vous verriez les 4 millions de références du catalogue — le sélecteur réduit ce choix aux pièces vérifiées pour votre montage exact.

### Q : Comment trouver la référence d'une pièce auto ?

Il existe 3 méthodes pour trouver la référence d'une pièce auto : 1) Relevez le numéro OEM (Origine Équipementier) gravé ou imprimé directement sur la pièce usagée (ex : 8200 123 456 pour Renault). 2) Consultez le catalogue constructeur avec votre numéro VIN pour obtenir les références d'origine. 3) Utilisez notre sélecteur de véhicule par immatriculation ou VIN : il identifie automatiquement les références compatibles avec votre montage exact.

### Q : Où trouver le numéro VIN de mon véhicule ?

Le VIN (Vehicle Identification Number) est un code unique de 17 caractères. Vous le trouverez : sur la plaque constructeur (montant de porte conducteur), sur le pare-brise côté conducteur (visible de l'extérieur), et sur votre carte grise au champ E. Le numéro VIN 17 caractères permet de trouver des pièces auto avec une précision de 99%+.

### Q : C'est quoi F1, F2 et F3 sur une carte grise ?

Les champs F de la carte grise concernent les masses du véhicule : F.1 = masse en charge maximale techniquement admissible (PTAC), F.2 = PTAC de l'ensemble (véhicule + remorque), F.3 = masse en charge maximale de l'ensemble en service (PTRA). Ces informations sont utiles pour dimensionner correctement les pièces de freinage (disques, plaquettes) et de suspension (amortisseurs, ressorts) de votre véhicule.

### Q : Comment savoir le type de motorisation de ma voiture ?

Pour connaître le type de motorisation, consultez le champ P.3 de votre carte grise (type de carburant : essence, diesel, hybride, électrique, GPL) et le champ D.2 (type mine / variante / version). Vous pouvez aussi décoder votre VIN : les positions 4 à 8 identifient généralement le moteur. Notre sélecteur par VIN extrait automatiquement ces informations.

### Q : Que faire si mon véhicule n'apparaît pas dans le sélecteur ?

Essayez la recherche par VIN qui est la plus précise. Pour les véhicules rares, importés ou très récents, contactez notre service client avec votre carte grise : nous identifierons les pièces compatibles manuellement. Astuce : les véhicules importés depuis l'Allemagne ou la Belgique sont généralement reconnus par VIN même si la plaque étrangère ne fonctionne pas.

### Q : Quelle est la différence entre type mine et code moteur ?

Le type mine (champ D.2 de la carte grise) identifie la version exacte du véhicule auprès du constructeur. Le code moteur, gravé sur le bloc moteur, identifie uniquement la motorisation. Les deux informations sont complémentaires pour une identification précise. Vous pouvez trouver le code moteur avec le VIN gratuitement via notre sélecteur.

### Q : Mon véhicule a des variantes de montage : comment choisir la bonne pièce ?

Les variantes existent car les constructeurs changent de fournisseurs en cours de production. Pour identifier la bonne variante : mesurez les pièces actuelles (diamètre des disques, nombre de trous), consultez la plaque constructeur (codes PR/option), ou utilisez la recherche par VIN qui identifie automatiquement la bonne configuration. Conseil rapide : prenez une photo du numéro OE gravé sur votre pièce actuelle. Ce numéro est votre meilleure référence pour retrouver l'équivalent exact.

### Q : Comment être sûr de commander la bonne pièce auto en ligne ?

Pour être sûr de commander la bonne pièce auto : 1) Sélectionnez votre véhicule via notre configurateur (immatriculation, VIN ou sélection manuelle). 2) Vérifiez que la fiche produit indique "Compatible" avec votre véhicule. 3) Lisez les alertes de variantes (diamètre, Start & Stop, capteur). 4) En cas de doute, comparez le numéro OEM de votre ancienne pièce. 5) Pour les pièces de sécurité (freins, suspension), privilégiez toujours la recherche par VIN.

### Q : Les pièces premier prix sont-elles fiables pour le freinage ?

Pour les organes de sécurité (freinage, direction, suspension), nous recommandons les équipementiers de première monte (Bosch, TRW, Valeo, Brembo). Ces fabricants respectent les cahiers des charges constructeur et leurs pièces sont testées aux mêmes normes que les pièces d'origine. La différence entre une pièce d'origine et un équipementier ? Souvent la même usine, sans le logo constructeur, avec un prix réduit de 20 à 40%.

### Q : Puis-je enregistrer plusieurs véhicules dans le sélecteur ?

Le sélecteur enregistre le dernier véhicule sélectionné pour accélérer vos prochaines visites. Si vous possédez plusieurs véhicules, vous pouvez changer de véhicule à tout moment en cliquant sur "Changer de véhicule". L'historique de vos commandes conserve la référence de chaque véhicule.

### Q : Le sélecteur fonctionne-t-il pour les véhicules importés ?

Les véhicules importés depuis l'Europe (Allemagne, Belgique, Espagne, Italie) sont généralement reconnus par la recherche VIN, même si la plaque d'immatriculation étrangère ne fonctionne pas avec la recherche par immatriculation. Le VIN est un standard international qui identifie le véhicule indépendamment du pays d'immatriculation.

### Q : Où trouver un logiciel de vue éclatée automobile gratuit ?

Les catalogues en ligne comme TecDoc et 7zap proposent des vues éclatées gratuites pour identifier les pièces par position sur le véhicule. Automecanik intègre ces données TecDoc directement dans son catalogue : en sélectionnant votre véhicule, vous accédez aux schémas de montage e

[...]
