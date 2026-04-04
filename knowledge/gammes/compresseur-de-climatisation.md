---
category: climatisation
slug: compresseur-de-climatisation
title: Compresseur de climatisation
pg_id: 447
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-04-03'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:rag-enrich-from-web-corpus
  last_enriched_at: '2026-04-03'
  v5_migrated_at: '2026-03-29'
domain:
  role: Comprime le fluide frigorigene pour le cycle de climatisation - Ne refroidit PAS le moteur
  must_be_true:
  - comprimer le fluide
  - entrainer le circuit
  must_not_contain:
  - pompe
  - eau
  - moteur
  - refroidissement
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - condenseur-de-climatisation
  - evaporateur-de-climatisation
  - filtre-d-habitacle
  - detendeur-de-climatisation
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
  - ❌ "refroidit le moteur"
  cost_range:
    min: 383
    max: 610
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Pièce OE (Origine Équipement)
    description: Compresseur identique à celui monté en usine. Certains constructeurs (Audi, BMW, Mercedes, Toyota, VW) utilisent
      des fournisseurs spécialistes représentant jusqu à 40 % du marché mondial.
  - tier: Équivalent OE (fournisseurs de rang 1)
    description: Fabricants qui produisent les compresseurs pour les constructeurs. Qualité identique à l OE, prix inférieur.
  - tier: Reconditionné (échange standard)
    description: Compresseur remanufacturé et testé. Option économique valable si le reconditionnement est certifié.
  - tier: Générique non qualifié
    description: Risque de projection de limaille dans le circuit. Peut endommager condenseur, déshydrateur et tout le circuit.
  brands:
    premium:
    - Denso
    - Valeo
    standard:
    - NRF
    - Delphi
    - Hella
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Climatisation qui ne produit plus d air froid
    severity: confort
  - id: S2
    label: Bruit de claquement a l enclenchement de la clim
    severity: confort
  - id: S3
    label: Sifflement ou grincement cote compresseur
    severity: confort
  - id: S4
    label: Embrayage compresseur patine enclenche
    severity: confort
  - id: S5
    label: Traces d huile autour du compresseur
    severity: confort
  - id: S6
    label: Plus de 150 000 km sans controle du circuit
    severity: confort
  - id: S7
    label: Fuite huile visible compresseur raccords
    severity: confort
  - id: S8
    label: Climatisation refroidit puis arrete brutalement
    severity: confort
  - id: S9
    label: Odeur brule caoutchouc chaud cote
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - remplacement preventif recommande
  depose_steps:
  - 'Comment changer un compresseur de climatisation de voiture : guide étape par étape (Source: web/c9b0e275b412-s007.md)'
  quick_checks:
  - 'Observer : climatisation qui ne produit plus d air froid ?'
  - Bruit de claquement a l enclenchement de la clim ?
  - 'Observer : sifflement ou grincement cote compresseur ?'
  - 'Observer : embrayage compresseur patine enclenche ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Climatisation qui ne produit plus d air froid
  - Bruit de claquement a l enclenchement de la clim
  - Sifflement ou grincement cote compresseur
  - Embrayage compresseur patine enclenche
  - Traces d huile autour du compresseur
  - Plus de 150 000 km sans controle du circuit
  good_practices:
  - Faire tourner la climatisation 10 min par semaine meme en hiver
  - Remplacement du filtre d habitacle chaque annee
  - Recharge de gaz par un professionnel equipe (circuit sous pression)
  - Controle d etancheite si baisse de performance
rendering:
  pgId: '447'
  intro_title: A quoi sert Compresseur de climatisation ?
  risk_title: Pourquoi remplacer Compresseur de climatisation a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
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
  - question: Compresseur clim OE ou adaptable ?
    answer: Privilégiez l'OE ou OES (Denso, Sanden, Valeo). Un compresseur de mauvaise qualité peut endommager tout le circuit
      par projection de limaille.
  - question: Comment savoir si mon compresseur est HS ?
    answer: Clim qui ne refroidit plus, bruit de claquement ou sifflement, embrayage qui ne s'enclenche pas, traces d'huile
      sur le compresseur.
  - question: Tous les combien changer le compresseur ?
    answer: Pas de périodicité. Durée de vie 100 000 à 200 000 km. Faire une recharge tous les 2 ans préserve le compresseur.
  - question: Peut-on changer le compresseur soi-même ?
    answer: Déconseillé. Nécessite un équipement de récupération de gaz (obligatoire légalement) et une station de recharge
      professionnelle.
  - question: Quelle erreur éviter avec le compresseur ?
    answer: Ne jamais ajouter de gaz dans un circuit vide (air + humidité = dégâts). Toujours remplacer le déshydrateur avec
      le compresseur.
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
doc_id: 253d689b-3b70-5777-b80b-58ab21d0b552
content_hash: sha256:8beddd37bb872c77
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
  area: Face avant (condenseur), habitacle (evaporateur), moteur (compresseur)
  access: Variable selon composant (capot, tableau de bord, face avant)
  adjacent_parts:
  - compresseur
  - condenseur
  - detendeur
  - evaporateur
installation:
  difficulty: difficile (pro obligatoire)
  time: 1h a 4h
  tools:
  - station de recharge
  - detecteur de fuites
  - cle a douille
  prerequisite: Recuperation du gaz obligatoire par professionnel agree
phase5_enrichment:
  _source: automotive.hutchinson.com + denso-am.eu + fr.wikipedia.org + hella.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 4
  _has_tech_data: true
  types_variants:
  - type: 'composite'
    source_ref: corpus RAG web OEM
  - type: 'hydraulique'
    source_ref: corpus RAG web OEM
  - type: 'plein'
    source_ref: corpus RAG web OEM
  - type: 'pneumatique'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    norme_iso_9981: 'ISO 9981'
    val_000_km: '000 km'
    val_10_bars: '10 bars'
    val_100__c: '100 °C'
    val_12_a: '12 a'
    val_134_a: '134 a'
    val_135__c: '135 °C'
    val_15_bar: '15 bar'
    val_19_a: '19 a'
    val_2_a: '2 a'
    val_2_bars: '2 bars'
    val_300_bars: '300 bars'
    val_36_a: '36 a'
    val_40_bars: '40 bars'
    val_42_a: '42 a'
    val_7_a: '7 a'
  materials:
  - materiau: 'graphite'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le système de climatisation se met enroute dés que vous actionnez la commande de climatisation située dans l''habitacle.La
    poulie du compresseur entraînée par lacourroie d''accessoires est munie d''un embrayage magnétique qui va mettre en action
    lecompresseur de climatisation pour envoyé le liquide frigorigène à hautepression dans le condenseur de climatisation
    pour le refroidir, le gaz vasortir du condenseur sous forme de liquide vers la bouteille déshydratante qui va filtrerle
    gaz liquéfié et qui va se détendre dans le détendeur de climatisation pourfaire chuter la pression et générer du froid.
    Le gaz refroidit passe dansl''évaporateur de climatisation pour l''évacuer de l''humidité sous forme liquide (eau qui
    coulesous le véhicule), l''air froid arrive dans l''habitacle. Le rôle du compresseur de climatisationest de compresser
    le gaz basse pression de manière à l''échauffer et de letransformer en gaz haute pression. Le fonctionnement de la climatisation
    consomme une grande quantité d''énergie surtout quand le moteur tourne au ralentie. En savoir plus : compresseur de climatisation
    — définition et rôle mécanique 🚨 Bruit Compresseur de climatisation : causes et diagnostic'
  S2: 'Ne pas attendre la panne complete pour intervenir. Symptômes d''usure : - Climatisation qui ne produit plus d air froid
    - Bruit de claquement a l enclenchement de la clim - Sifflement ou grincement cote compresseur - Embrayage compresseur
    patine enclenche - Traces d huile autour du compresseur - Plus de 150 000 km sans controle du circuit - Fuite huile visible
    compresseur raccords - Climatisation refroidit puis arrete brutalement - Odeur brule caoutchouc chaud cote'
  S3: 'Pour choisir les bons compresseur de climatisation pour votre véhicule : - Marque de votre véhicule - Modele de votre
    véhicule - Annee de votre véhicule - Vérifier : climatisation qui ne produit plus d air froid - Vérifier : bruit de claquement
    a l enclenchement de la clim - Vérifier : sifflement ou grincement cote compresseur - Vérifier : embrayage compresseur
    patine enclenche - Vérifier : traces d huile autour du compresseur - Vérifier : plus de 150 000 km sans controle du circuit
    - Vérifier : fuite huile visible compresseur raccords - Vérifier : climatisation refroidit puis arrete brutalement - Vérifier
    : odeur brule caoutchouc chaud cote - Vérifier : Bruit de claquement a l enclenchement de la clim - Vérifier : Sifflement
    ou grincement cote compresseur - ### Caractéristiques La formulation unique de l’huile de base de , signifie qu’ils offrent
    les propriétés physiques exactes dont notre compresseur AC, a besoin pour continuer à fonctionner sans heurts et efficacement.
    (Source: web-catalog/12908517def6-s001.md, web- catalog/12908517def6-s002.md, web-catalog/12908517def6-s003.md, web- catalog/12908517def6-s004.md)
    - ## Safety Data Sheets If you work with air conditioning oils, please follow the safety instructions. - ND Oil 8 Version
    3.1 Safety Datasheet Austria ND-oil-8 - ND Oil 11 Version 1.2 Safety Datasheet... (Source: web-catalog/12908517def6-s001.md,
    web- catalog/12908517def6-s002.md, web-catalog/12908517def6-s003.md, web- catalog/12908517def6-s004.md)Pour aller plus
    loin : consultez notre guide d''achat compresseur de climatisation — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: '1. Comment changer un compresseur de climatisation de voiture : guide étape par étape 2. ## Les fabricants choisissent
    Détenant 40 % du marché mondial des compresseurs A/C d’origine, est le leader mondial sur ce marché. Les pièces sont sélectionnées
    par les principaux constructeurs automobiles tels que Audi, BMW, Fiat, Mercedes, Porsche, Toyota et VW. Design compact
    et léger de haute...'
  S4_REPOSE: 'Le remontage d''un compresseur de climatisation nécessite un équipement de station de recharge professionnelle
    (obligatoire légalement pour la manipulation du fluide frigorigène R134a ou R1234yf). Ne remontez jamais un compresseur
    dans un circuit non purgé : l''air et l''humidité résiduels forment des acides qui détruisent le compresseur neuf en quelques
    heures. - Vérifiez que le compresseur de climatisation neuf est rigoureusement identique à celui démonté : numéro d''identification,
    capacité en huile, type de poulie (diamètre, nombre de gorges), type d''embrayage et position de la valve. Un compresseur
    avec une capacité en huile différente nécessite une vidange du circuit entier. - Contrôlez l''état de la courroie d''accessoires
    : si elle présente des craquelures, des effilochures ou une usure latérale, remplacez-la simultanément. Une courroie défaillante
    peut casser le compresseur neuf par patinage ou blocage. - Contrôlez l''état des conduites de climatisation : flexibilité
    des flexibles, absence de corrosion sur les raccords rigides, état des joints toriques. Remplacez tous les joints toriques
    d''interface compresseur — ils ne peuvent pas être réutilisés. - Remplissez le compresseur neuf avec la quantité d''huile
    réfrigérante prescrite par le constructeur (PAG ou POE selon le fluide frigorigène). Un compresseur trop peu huilé gripe
    dès la première mise en route. - Remontez le compresseur de climatisation sur ses supports. Démarrez le serrage à la main
    sur tous les points de fixation avant d''utiliser la clé. Serrez les vis de fixation au couple prescrit (généralement
    20 à 35 N·m). - Remontez les conduites de climatisation avec des joints toriques neufs légèrement enduits d''huile réfrigérante.
    Serrez les raccords au couple prescrit — un raccord trop serré coupe le joint, trop lâche il fuit. - Rebranchez le connecteur
    électrique du compresseur. Remontez la courroie d''accessoires en respectant le cheminement constructeur et la tension
    correcte. Rebranchez la batterie. - Ouvrez les valves de service basse et haute pression. Faites réaliser par un professionnel
    agréé la mise sous vide du circuit (minimum 30 minutes à –1 bar) pour éliminer l''air et l''humidité résiduels, puis la
    charge en fluide frigorigène à la quantité et au type prescrits (R134a ou R1234yf). - Contrôlez la pression du circuit
    en basse et haute pression avec les manomètres de station (valeurs constructeur à température ambiante stable). Vérifiez
    l''absence de fuite aux raccords avec un détecteur ou du spray traceur UV. - Enclenchez la climatisation et contrôlez
    la montée en froid : la température en sortie d''aérateur doit descendre en dessous de 10 °C en 5 minutes par temps chaud.
    Vérifiez l''absence de bruit de sifflement ou de claquement à l''embrayage du compresseur.'
  S5: '- ❌ "homologué CT" - ❌ "sécurité garantie" - ❌ "zéro panne" - ❌ "garanti à vie" - ❌ "refroidit le moteur" - - Climatisation
    et système thermique moteur - Huile de compresseur A/C Huile de compresseur A/C Il est essentiel de lubrifier le compresseur
    A/C avec de l’huile de haute qualité, pour garantir son...'
  S6: 'Après la pose d''un compresseur de climatisation neuf, plusieurs contrôles sont nécessaires avant de considérer l''intervention
    terminée. Le circuit frigorigène est sous pression et toute anomalie doit être détectée immédiatement. - Vérifier l''absence
    de fuite aux raccords : utiliser un détecteur de gaz réfrigérant électronique ou des lunettes UV avec traceur fluorescent.
    Contrôler chaque raccord du compresseur — entrée basse pression, sortie haute pression, et zone d''embrayage. - Contrôler
    les pressions du circuit après recharge : côté basse pression entre 1,5 et 2,5 bar au ralenti, côté haute pression entre
    14 et 20 bar selon la température extérieure. Se référer aux préconisations constructeur pour les valeurs précises du
    véhicule. - Tester l''embrayage compresseur : enclencher la climatisation et observer le plateau d''entraînement. L''embrayage
    doit s''accrocher sans claquement sec ni patinage visible. Un clic franc unique à l''enclenchement est normal. - Vérifier
    la quantité d''huile frigorigène : le compresseur neuf contient une dose d''huile prédéfinie (généralement 80 à 140 ml
    de PAG selon le modèle). En cas de remplacement de plusieurs composants, ajuster la quantité totale d''huile dans le circuit
    pour éviter une surdose. - Contrôler la tension et l''état de la courroie d''accessoire : une courroie détendue ou usée
    provoque des sifflements et accélère l''usure de l''embrayage. Vérifier également le galet tendeur et la poulie de compresseur.
    - Tester l''efficacité de refroidissement sur 10 minutes : fenêtres fermées, ventilateur à fond, la température de soufflage
    des bouches doit descendre sous 10 °C en 5 minutes à 20-25 °C ambiants. Au- dessus de cette valeur, suspecter une charge
    de fluide insuffisante. - Contrôler l''absence de vibrations anormales : au ralenti avec la climatisation enclenchée,
    les supports du compresseur ne doivent transmettre aucune vibration excessive. Des vibrations persistantes signalent un
    balourd de plateau ou un mauvais alignement de courroie.'
  S_GARAGE: 'Nous vous recommandons de confier cette intervention à un professionnel : - Plusieurs causes possibles de défaillance
    (3 identifiées) nécessitent un diagnostic professionnel Un garagiste qualifié dispose de l''outillage et de l''expérience
    nécessaires pour effectuer cette opération en toute sécurité.'
  S7: Quel est le prix d'un compresseur de climatisation ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur
    pour trouver le compresseur de climatisation compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon compresseur de climatisation est à changer ?Les signes d'usure les plus courants sont détaillés dans la
    section diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un compresseur
    de climatisation défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du
    véhicule. Consultez la section symptômes pour évaluer l'urgence du remplacement.- bouteille deshydratante - condenseur
    de climatisation - courroie d accessoire - detendeur de climatisation - evaporateur de climatisation - filtre d habitacle
  S8: Compresseur clim OE ou adaptable ?Privilégiez l'OE ou OES (Denso, Sanden, Valeo). Un compresseur de mauvaise qualité
    peut endommager tout le circuit par projection de limaille. Comment savoir si mon compresseur est HS ?Clim qui ne refroidit
    plus, bruit de claquement ou sifflement, embrayage qui ne s'enclenche pas, traces d'huile sur le compresseur. Tous les
    combien changer le compresseur ?Pas de périodicité. Durée de vie 100 000 à 200 000 km. Faire une recharge tous les 2 ans
    préserve le compresseur. Peut-on changer le compresseur soi-même ?Déconseillé. Nécessite un équipement de récupération
    de gaz (obligatoire légalement) et une station de recharge professionnelle. Quelle erreur éviter avec le compresseur ?Ne
    jamais ajouter de gaz dans un circuit vide (air + humidité = dégâts). Toujours remplacer le déshydrateur avec le compresseur.
  META: '{"meta_title":"Compresseur de clim : Conseils remplacement | AutoMecanik","meta_description":"Compresseur de climatisation
    en panne ? Découvrez quand changer cette pièce, les symptômes à surveiller (bruit, plus d''air froid) et comment choisir
    le bon modèle."}'
---

# Compresseur de climatisation - Guide Diagnostic Complet

## Fonction et Rôle

Comprime le fluide frigorigene pour le cycle de climatisation - Ne refroidit PAS le moteur

**Actions principales:** comprimer le fluide, entrainer le circuit

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de claquement a l enclenchement de la clim**
  bruit de claquement a l enclenchement de la clim
- **Sifflement ou grincement cote compresseur**
  sifflement ou grincement cote compresseur

### 🟢 Autres Symptômes

- climatisation qui ne produit plus d air froid
- embrayage compresseur patine enclenche
- traces d huile autour du compresseur
- plus de 150 000 km sans controle du circuit
- fuite huile visible compresseur raccords
- climatisation refroidit puis arrete brutalement

## Procédure de Diagnostic

Pour diagnostiquer un problème de compresseur de climatisation:

1. **Inspection visuelle** - Examiner l'état du compresseur de climatisation
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- bouteille-deshydratante
- condenseur-de-climatisation
- courroie-d-accessoire
- detendeur-de-climatisation
- evaporateur-de-climatisation
- filtre-d-habitacle

## Critères de Compatibilité

Pour commander le bon compresseur de climatisation, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidit le moteur"

## FAQ

**Compresseur clim OE ou adaptable ?**
Privilégiez l'OE ou OES (Denso, Sanden, Valeo). Un compresseur de mauvaise qualité peut endommager tout le circuit par projection de limaille.

**Comment savoir si mon compresseur est HS ?**
Clim qui ne refroidit plus, bruit de claquement ou sifflement, embrayage qui ne s'enclenche pas, traces d'huile sur le compresseur.

**Tous les combien changer le compresseur ?**
Pas de périodicité. Durée de vie 100 000 à 200 000 km. Faire une recharge tous les 2 ans préserve le compresseur.

**Peut-on changer le compresseur soi-même ?**
Déconseillé. Nécessite un équipement de récupération de gaz (obligatoire légalement) et une station de recharge professionnelle.

**Quelle erreur éviter avec le compresseur ?**
Ne jamais ajouter de gaz dans un circuit vide (air + humidité = dégâts). Toujours remplacer le déshydrateur avec le compresseur.
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
## Climatisation sans effet

### Pas de froid
- **Manque de gaz réfrigérant** : Fuite dans le circuit. Le compresseur ne s'enclenche pas ou tourne en continu sans refroidir. Recharge + recherche de fuite nécessaire.
- **Compresseur bloqué** : Embrayage de compresseur HS, bruit métallique, courroie qui patine.
- **Condenseur obstrué** : Débris, feuilles ou insectes devant le condenseur (devant le radiateur). Nettoyage au jet doux.
- **Détendeur bloqué** : Le gaz ne se détend plus correctement, givrage possible sur les tuyaux.

### Odeurs dans l'habitacle
- **Filtre habitacle encrassé** : Odeur de moisi à la mise en route de la ventilation. Remplacement tous les 15 000-20 000 km.
- **Évaporateur contaminé** : Bactéries et moisissures sur l'évaporateur. Traitement antibactérien recommandé.

## Chauffage défaillant

### Pas de chaleur
- **Niveau de liquide de refroidissement bas** : Le radiateur de chauffage n'est pas alimenté. Vérifier le niveau et faire l'appoint.
- **Thermostat bloqué ouvert** : Le moteur ne monte pas en température. L'aiguille reste basse même après 10 minutes de conduite.
- **Radiateur de chauffage bouché** : Les deux durites d'entrée/sortie doivent être chaudes moteur à température. Si une seule est chaude, le radiateur est obstrué.

### Ventilation faible
- **Résistance de ventilateur grillée** : Seule la vitesse maximale fonctionne, les autres vitesses sont inactives.
- **Moteur de ventilateur fatigué** : Bruit de frottement, débit d'air réduit.

## Quand consulter un professionnel

- Compresseur bruyant (risque de blocage et casse courroie)
- Fuite de gaz réfrigérant visible (traces d'huile sur les raccords)
- Odeur sucrée dans l'habitacle (fuite de liquide de refroidissement dans le radiateur de chauffage)
- Surchauffe moteur associée à un problème de chauffage


## References supplementaires

<!-- materialized-from-db manual/5bd56cff0d3c 2026-04-03 -->
### Données techniques OEM — Compresseur de climatisation

# Données techniques OEM — Compresseur de climatisation
Source : automotive.hutchinson.com + denso-am.eu + fr.wikipedia.org + hella.com (4 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- composite
- hydraulique
- plein
- pneumatique
- électrique

## Normes applicables
- ISO 9981

## Matériaux
- graphite

## Valeurs techniques de référence
- 10 bars
- 100 °C
- 135 °C
- 15 bar
- 2 bars
- 300 bars
- 40 bars

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

## Symptomes supplementaires

<!-- materialized-from-db diagnostic/climatisation.md 2026-02-15 -->
### Diagnostic - Climatisation et chauffage

# Climatisation et chauffage - Diagnostic complet

## Climatisation sans effet

### Pas de froid
- **Manque de gaz réfrigérant** : Fuite dans le circuit. Le compresseur ne s'enclenche pas ou tourne en continu sans refroidir. Recharge + recherche de fuite nécessaire.
- **Compresseur bloqué** : Embrayage de compresseur HS, bruit métallique, courroie qui patine.
- **Condenseur obstrué** : Débris, feuilles ou insectes devant le condenseur (devant le radiateur). Nettoyage au jet doux.
- **Détendeur bloqué** : Le gaz ne se détend plus correctement, givrage possible sur les tuyaux.

### Odeurs dans l'habitacle
- **Filtre habitacle encrassé** : Odeur de moisi à la mise en route de la ventilation. Remplacement tous les 15 000-20 000 km.
- **Évaporateur contaminé** : Bactéries et moisissures sur l'évaporateur. Traitement antibactérien recommandé.

## Chauffage défaillant

### Pas de chaleur
- **Niveau de liquide de refroidissement bas** : Le radiateur de chauffage n'est pas alimenté. Vérifier le niveau et faire l'appoint.
- **Thermostat bloqué ouvert** : Le moteur ne monte pas en température. L'aiguille reste basse même après 10 minutes de conduite.
- **Radiateur de chauffage bouché** : Les deux durites d'entrée/sortie doivent être chaudes moteur à température. Si une seule est chaude, le radiateur est obstrué.

### Ventilation faible
- **Résistance de ventilateur grillée** : Seule la vitesse maximale fonctionne, les autres vitesses sont inactives.
- **Moteur de ventilateur fatigué** : Bruit de frottement, débit d'air réduit.

## Quand consulter un professionnel

- Compresseur bruyant (risque de blocage et casse courroie)
- Fuite de gaz réfrigérant visible (traces d'huile sur les raccords)
- Odeur sucrée dans l'habitacle (fuite de liquide de refroidissement dans le radiateur de chauffage)
- Surchauffe moteur associée à un problème de chauffage
