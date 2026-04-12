---
category: moteur
slug: soupape-d-admission
title: Soupape d'admission
pg_id: 1269
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-03-29'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:rag-enrich-from-web-corpus
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Ouvrir et fermer le passage des gaz d'admission
  must_be_true:
  - ouvrir
  - fermer
  - admettre
  must_not_contain:
  - echappement
  - carburant
  - injection
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - ouvrir
  - fermer
  - admettre
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
  - ❌ "plus de puissance"
  cost_range:
    min: 15
    max: 50
    currency: EUR
    unit: soupape
    source: catalogue automecanik
  brands:
    premium:
    - Mahle Original
    - TRW Engine Component
    - AE (Federal-Mogul)
    standard:
    - Freccia
    - Intervalves
    - SM (Societe Mecanique)
    budget:
    - Osvat
    - BGA
    - AMP
  quality_tiers:
  - tier: Origine constructeur
    description: Soupapes identiques a celles montees en usine. Specifications exactes de longueur, diametre de tete et de
      queue respectees.
  - tier: Equipementier qualite OE
    description: Fabricants fournissant les constructeurs en premiere monte. Memes tolerances dimensionnelles et metallurgiques.
  - tier: Adaptable qualite reconnue
    description: Soupapes conformes aux cotes constructeur, fabriquees par des equipementiers independants avec controle qualite.
diagnostic:
  symptoms:
  - id: S1
    label: Perte de compression sur un ou plusieurs cylindres
    severity: confort
  - id: S2
    label: Rates d allumage persistants
    severity: confort
  - id: S3
    label: Claquement au niveau de la culasse
    severity: confort
  - id: S4
    label: Consommation d huile anormale guides uses
    severity: confort
  - id: S5
    label: Fumee bleue a l echappement
    severity: confort
  - id: S6
    label: Casse de courroie de distribution controle
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  quick_checks:
  - 'Observer : perte de compression sur un ou plusieurs cylindres ?'
  - 'Observer : rates d allumage persistants ?'
  - 'Observer : claquement au niveau de la culasse ?'
  - 'Observer : consommation d huile anormale guides uses ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Perte de compression sur un ou plusieurs cylindres
  - Rates d allumage persistants
  - Claquement au niveau de la culasse
  - Consommation d huile anormale guides uses
  - Fumee bleue a l echappement
  - Casse de courroie de distribution controle
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '1269'
  intro_title: A quoi sert Soupape d'admission ?
  risk_title: Pourquoi remplacer Soupape d'admission a temps ?
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
  - question: Soupape d'admission OE ou adaptable ?
    answer: Les soupapes OES (AE, Freccia, TRW) sont fiables. Vérifiez les cotes exactes (longueur, diamètre tête et queue).
      Ne pas mélanger les qualités.
  - question: Comment savoir si une soupape d'admission est HS ?
    answer: Perte de compression sur un cylindre, claquement, ratés d'allumage, consommation d'huile excessive (guide usé).
  - question: Tous les combien changer les soupapes d'admission ?
    answer: Pas de périodicité. Durée de vie 200 000+ km. Remplacement lors d'une réfection culasse ou après casse distribution.
  - question: Peut-on changer une soupape soi-même ?
    answer: Non recommandé. Nécessite un lève-soupapes, une rectification des sièges, et un contrôle d'étanchéité. Travail
      de spécialiste.
  - question: Quelle erreur éviter avec les soupapes ?
    answer: Ne jamais rodé une soupape neuve sur un siège usé. Remplacer aussi les guides si jeu excessif. Contrôler la planéité
      de la culasse.
  quality:
    score: 60
    source: script:rag-upgrade-v4
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
doc_id: 0c8f3298-e12a-5181-b7f6-7d345dd0673d
content_hash: sha256:6b580f910bee5e46
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
  area: Sur le vehicule (position variable selon modele)
  access: Consulter la revue technique du vehicule
  adjacent_parts:
  - pieces adjacentes du meme systeme
installation:
  difficulty: variable
  time: consulter revue technique
  tools:
  - outillage standard
  prerequisite: Consulter la procedure constructeur
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-04'
  _web_files_count: 1
  _has_tech_data: true
  technical_notes:
    val_150__c: '150 °C'
    val_17_a: '17 a'
    val_2_a: '2 a'
    val_25__: '25 %'
    val_6_a: '6 a'
    val_800__c: '800 °C'
    val_97_5__c: '97,5 °C'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    La soupape d'admission ce met en mouvement dés la miseen marche du moteur
    par l'intermédiaire de l'arbre à cames et elle est situéedans la culasse,
    son rôle est de permettre l'aspiration d'une quantité demélange frais
    air/carburant dans le cylindre. Les soupapes d'admission sontouvertes
    pendant le temps d'admission. Généralement une soupape se compose d'une tête
    etd'une tige : - La tête va assurerl'obturation du cylindre en combinaison
    avec le siège de soupape. - La tige sera guidée dans laculasse par un guide
    de soupape. Pour éviter l'infiltration d'huile du moteur dans lachambre de
    combustion un joint est monté sur le haut de la tige de soupape. Lafermeture
    de la soupape est assurée par un ressort de soupape. Généralement dans les
    nouvelles motorisations il y adeux soupapes d'admission dans chaque
    cylindre. Il existe trois types de soupapes : - Soupapes à chemise
    louvoyante. - Soupapes rotatives. - Soupapes à tige nommées aussi soupapes à
    tulipe. Les soupapes sont des pièces fortement sollicités auplan thermique,
    une soupape d'admission peut atteindre une température de 500°C En savoir
    plus : soupape d'admission — définition et rôle mécanique 🚨 Bruit Soupape
    d'admission : causes et diagnostic
  S2: >-
    Une soupape d'admission défaillante présente plusieurs symptômes : - Bruit
    au niveau du moteur. - Surconsommation ducarburant. - Fumée noir à la sortie
    del'échappement. Une soupape d'admission usée et qu'elle n'est pas remplacée
    à temps peut amener à la casse du moteur. Diagnostic complet : identifier
    une panne de soupape d'admission
  S3: >-
    - Marque, modèle et motorisation : la soupape d'admission est dimensionnée
    au dixième de millimètre près pour chaque moteur. Un écart de diamètre de
    tête, de longueur ou de diamètre de queue rend la pièce inutilisable.
    Renseigner systématiquement le code moteur lors de la commande. - Fabricants
    OES de référence : privilégier AE, Freccia ou TRW — ces équipementiers
    produisent pour les constructeurs. Vérifier que les cotes (longueur totale,
    diamètre de tête, diamètre de queue, angle d'assise) correspondent
    exactement à la référence d'origine. - Diagnostic de compression préalable :
    avant de commander, effectuer un test de compression. Si la compression est
    faible sur un cylindre (typiquement moins de 10 bars sur un moteur à essence
    en bon état), confirmer l'origine soupape par un test à la bougie
    dépressurisation. Cela évite un remplacement inutile si la culasse est
    déformée. - Vérifier l'état des guides de soupape : une consommation d'huile
    anormale associée à une fumée bleue à l'échappement signale souvent des
    guides usés plutôt que la soupape elle-même. Si le jeu radial de la queue de
    soupape dans son guide dépasse 0,1 mm, remplacer les guides simultanément —
    sinon la nouvelle soupape s'use prématurément. - Contrôle de la planéité de
    la culasse : une culasse gauchie (plus de 0,05 mm de voile selon les
    constructeurs) provoque une fuite de gaz même avec une soupape neuve. Faire
    rectifier la culasse si nécessaire avant montage. - Remplacement par paire
    admission/échappement lors d'une réfection culasse : si la culasse est
    déposée pour casse de distribution ou surchauffe, remplacer l'ensemble des
    soupapes des deux côtés — le coût de la pièce est marginal par rapport au
    coût de main-d'œuvre d'une deuxième intervention. - Rodage obligatoire après
    montage : ne jamais roder une soupape neuve sur un siège usé — rectifier les
    sièges avant le montage pour garantir une étanchéité parfaite. Le rodage
    seul sur siège endommagé ne restaure pas l'étanchéité. Pour aller plus loin
    : consultez notre guide d'achat soupape d'admission — comparatif marques,
    critères de choix et prix.
  S4_DEPOSE: >-
    - Déposer la culasse : la dépose des soupapes d'admission nécessite
    impérativement de déposer la culasse du moteur. Commencer par vidanger le
    liquide de refroidissement, déconnecter le faisceau et les durites, puis
    desserrer les vis de culasse dans l'ordre inverse du serrage (schéma en
    spirale de l'extérieur vers le centre). - Contrôler la planéité de la
    culasse : avant toute intervention sur les soupapes, poser une règle d'ébat
    sur la surface de joint et mesurer au jaugeage. Une déformation supérieure à
    0,05 mm impose une rectification chez un motoriste — monter une soupape
    neuve sur une culasse voilée est une perte d'argent. - Compresser le ressort
    de soupape : utiliser un compresseur de ressort de soupape adapté au type de
    culasse. Comprimer jusqu'à dégager les demi-lunes (clavettes) de la queue de
    soupape. Récupérer les clavettes dans un contenant — leur perte nécessite un
    achat de remplacement. - Extraire la soupape : retirer le ressort, la
    coupelle supérieure, puis extraire délicatement la soupape par le bas de la
    culasse. Étiqueter ou organiser les soupapes par cylindre et par position
    (admission 1, 2, 3…) pour pouvoir les réinstaller dans leur logement
    d'origine si elles ne sont pas remplacées. - Contrôler le guide de soupape :
    mesurer le jeu radial entre la queue de soupape et son guide. Au-delà de 0,1
    mm, le guide est usé et doit être remplacé ou chemisé. Un guide usé provoque
    une consommation d'huile persistante malgré la soupape neuve. - Rectifier
    les sièges avant le montage : faire usiner les sièges de soupape par un
    motoriste si la soupape ancienne présentait des traces de brûlure ou
    d'écaillage. Un siège non rectifié empêche l'étanchéité de la nouvelle
    soupape. - Monter la nouvelle soupape avec ses joints de queue : remplacer
    systématiquement les joints de queue de soupape (bagues d'étanchéité) lors
    du remplacement des soupapes — ils empêchent l'huile de descendre dans les
    guides et dans le cylindre. - Reposer dans l'ordre inverse : remonter les
    ressorts, coupelles et clavettes. Vérifier que chaque paire de clavettes est
    correctement engagée dans la gorge de la queue. Reposer la culasse avec un
    joint de culasse neuf, serrer les vis au couple constructeur en plusieurs
    passes.
  S4_REPOSE: >-
    Le remontage des soupapes d'admission sur la culasse exige une extrême
    rigueur : les cotes d'assemblage, l'ordre de serrage des vis de culasse et
    le rodage des portées conditionneront directement l'étanchéité combustion et
    la durée de vie de la réparation. Cette étape est réservée à un mécanicien
    outillé pour la rectification moteur. - Contrôler la planéité de la culasse
    au comparateur sur règle de précision avant tout remontage. Un voilage
    supérieur à 0,05 mm impose une rectification par un atelier spécialisé —
    toute soupape neuve montée sur culasse voilée sera perdue. - Vérifier les
    guides de soupapes au comparateur : le jeu radial acceptable est
    généralement de 0,02 à 0,06 mm selon constructeur. Un guide trop usé doit
    être chassé et remplacé avant la pose des nouvelles soupapes. - Roder les
    soupapes d'admission neuves sur leurs sièges à la pâte à roder fine (grain
    400 minimum) en rotation alternée jusqu'à obtenir un filet d'appui continu
    et mat sur toute la circonférence de la portée. - Nettoyer intégralement la
    pâte à roder au solvant puis au chiffon non pelucheux. La moindre trace de
    pâte abrasive dans le conduit d'admission ou sur le siège dégradera
    rapidement la nouvelle soupape. - Lubrifier légèrement la queue de soupape à
    l'huile moteur propre avant l'introduction dans le guide. Ne jamais monter
    une soupape à sec. - Reposer les rondelles coupelles, ressorts et clavettes
    avec le lève-soupapes. Comprimer le ressort sans dépasser la hauteur de
    compression libre constructeur pour ne pas fatiguer les spires. - Vérifier
    le montage de chaque clavette au marteau plastique : un coup sec sur la
    queue de soupape en libérant la compression du ressort doit confirmer la
    prise correcte des clavettes dans la gorge. - Reposer la culasse avec un
    joint neuf positionné à sec (côté feu côté bloc). Serrer les vis dans
    l'ordre constructeur en plusieurs passes angulaires selon le protocole
    (généralement 20 N·m + 90° + 90°). - Refaire la mise à l'heure de la
    distribution après remontage complet de la culasse avant de démarrer le
    moteur.
  S5: >-
    - Roder une soupape neuve sur un siège usé : le rodage est un ajustement de
    finition, non une correction de siège endommagé. Monter directement sans
    rectification préalable conduit à une mauvaise étanchéité, des ratés
    d'allumage persistants, et un remplacement prématuré de la soupape. -
    Omettre le remplacement des guides de soupape usés : si le jeu dans le guide
    dépasse 0,1 mm, la nouvelle soupape battra latéralement dans son logement,
    usera le siège de manière inégale, et génèrera une consommation d'huile
    persistante. Le coût des guides est marginal au regard d'une deuxième
    intervention complète. - Ne pas contrôler la planéité de la culasse avant le
    montage : une culasse gauchie après surchauffe ne garantit pas l'étanchéité
    même avec une soupape neuve et un joint de culasse neuf. Le résultat :
    reprise des ratés d'allumage et perte de compression dès la remise en route.
    - Réutiliser les vieux joints de queue de soupape : les bagues d'étanchéité
    de queue de soupape durcissent avec la chaleur et ne redeviennent jamais
    étanches une fois démontées. Les omettre provoque une descente d'huile dans
    les guides, une fumée bleue à l'échappement et une sur-consommation d'huile.
    - Mélanger des soupapes de qualités différentes dans la même culasse :
    installer une soupape OES sur des cylindres avec d'anciennes soupapes usées
    crée un déséquilibre de compression entre cylindres — le moteur tourne
    irrégulier et les anciens sièges continuent de se dégrader au contact des
    vieilles soupapes.
  S6: >-
    - Test de compression cylindre par cylindre : avant de remonter la culasse
    et de démarrer, effectuer un test d'étanchéité pneumatique ou au
    compressiomètre sur chaque cylindre. La compression doit être homogène
    (écart maximum 1 bar entre cylindres) et conforme aux valeurs constructeur.
    - Contrôle d'étanchéité au bleu de Prusse : avant le montage final,
    badigeonner le siège de soupape avec du bleu de Prusse, reposer la soupape
    et effectuer une légère rotation — la trace de contact doit être continue et
    centrée sur toute la largeur du siège. Un contact incomplet signale un
    rodage ou une rectification insuffisante. - Vérification du niveau d'huile
    et de la consommation : après les 500 premiers kilomètres, vérifier
    l'absence de consommation d'huile anormale et de fumée bleue — signes d'une
    bague de queue de soupape défaillante ou d'un guide encore usé. - Absence de
    ratés d'allumage : effectuer un diagnostic OBD après 50 km pour s'assurer
    qu'aucun code défaut P030x (raté d'allumage cylindre x) n'est mémorisé. Des
    ratés résiduels signalent un problème d'étanchéité sur un cylindre. -
    Contrôle visuel des joints d'étanchéité : après les premières minutes de
    fonctionnement, inspecter le plan de joint de culasse et le joint de cache-
    culbuteurs pour détecter toute trace de fuite d'huile ou de liquide de
    refroidissement.
  S7: >-
    Les soupapes d'admission font partie d'un ensemble mécanique complexe dont
    plusieurs composants sont directement impliqués dans leur fonctionnement.
    Lors d'une réfection de culasse, il est pratique d'inspecter et de remplacer
    les pièces suivantes pour éviter une seconde intervention. - Soupape
    d'échappement — lors de toute réfection de culasse, il est recommandé de
    remplacer simultanément les soupapes d'admission et d'échappement pour
    repartir avec un ensemble homogène en termes d'usure et de portée de siège.
    - Poussoir de soupape (ou linguet / culbuteur selon architecture) — transmet
    la commande de l'arbre à cames vers la soupape. Un poussoir usé à plateau
    plat produit un claquement caractéristique et accélère l'usure de la came et
    de la soupape neuves. - Joint de queue de soupape (bague d'étanchéité) —
    évite les remontées d'huile dans le conduit d'admission. Un guide usé avec
    joint HS provoque une consommation d'huile et de la fumée bleue à
    l'échappement malgré des soupapes neuves. - Joint de culasse — pièce
    d'étanchéité combustion à remplacer systématiquement lors de toute dépose de
    culasse. Réutiliser un joint de culasse est une source certaine de panne
    secondaire. - Joint de collecteur d'admission — assure l'étanchéité entre le
    collecteur et la culasse. À inspecter lors du démontage : une fuite d'air
    parasite perturbe la richesse et génère des ratés d'allumage malgré les
    soupapes neuves. - Poulie d'arbre à cames — à inspecter si la courroie de
    distribution a sauté (cause fréquente de casse de soupapes). Une poulie de
    came voilée ou à clavette abîmée doit être remplacée pour sécuriser la
    nouvelle distribution.
  S8: >-
    Peut-on changer une soupape d'admission sans démonter la culasse ? Non. La
    dépose des soupapes d'admission nécessite impérativement de retirer la
    culasse du moteur pour accéder aux ressorts et aux clavettes de queue de
    soupape. Il existe des techniques de maintien pneumatique du ressort en
    compression moteur tourné sur le PMH, mais elles ne sont viables que sur des
    moteurs très accessibles et toujours risquées (chute de clavette dans le
    cylindre). La dépose complète de la culasse reste la seule approche fiable.
    Quelle est la durée de vie d'une soupape d'admission ? Dans des conditions
    normales, une soupape d'admission dure 200 000 km et plus. Elle est rarement
    remplacée à titre préventif — le remplacement survient après une casse de
    courroie de distribution (contact piston-soupape), une surchauffe moteur
    ayant causé une déformation thermique, ou lors d'une réfection culasse de
    principe. Une soupape d'admission travaille à des températures inférieures à
    la soupape d'échappement (150-200°C contre 600-800°C), ce qui lui confère
    une plus grande longévité. Comment distinguer un problème de soupape
    d'admission d'un problème d'injecteur ? Un problème de soupape d'admission
    affecte toujours un cylindre précis et se manifeste par une chute de
    compression mesurable (compressiomètre). Un problème d'injecteur crée des
    ratés d'allumage également localisés sur un cylindre, mais sans chute de
    compression — le test de compression suffit à distinguer les deux causes. Un
    diagnostic OBD peut affiner le cylindre concerné via les codes P030x. Faut-
    il remplacer aussi les soupapes d'échappement en même temps ? Lors d'une
    réfection culasse complète (après casse de distribution ou surchauffe), oui
    : le coût de la pièce est négligeable par rapport au coût de main-d'œuvre.
    Si l'intervention est ciblée (soupape d'admission cassée sur un seul
    cylindre, culasse par ailleurs saine), les soupapes d'échappement peuvent
    être conservées si leur contrôle dimensional est satisfaisant et si les
    sièges sont rectifiés.
  META: >-
    {"meta_title":"Soupape d'admission : perte compression, causes |
    AutoMecanik","meta_description":"Perte de compression sur un cylindre, ratés
    d'allumage ou fumée bleue ? La soupape d'admission contrôle l'entrée des
    gaz. Diagnostic et compatibilité moteur.","og_title":"Soupape d'admission :
    diagnostic et remplacement","og_description":"Claquement culasse, casse de
    distribution ou consommation d'huile anormale : la soupape d'admission est
    peut-être en cause. Guide complet et sélection par moteur.","canonical_inten
    t":"diagnostic","schema_type":"HowTo","sources":[{"type":"rag","ref":"gammes
    /soupape-d-admission.md","field":"domain.role + diagnostic.symptoms +
    rendering.faq"}]}
---

# Soupape d'admission - Guide Diagnostic Complet

## Fonction et Rôle

Ouvrir et fermer le passage des gaz d'admission

**Actions principales:** ouvrir, fermer, admettre

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement au niveau de la culasse**
  claquement au niveau de la culasse
- **Casse de courroie de distribution controle**
  casse de courroie de distribution controle

### 🟢 Autres Symptômes

- perte de compression sur un ou plusieurs cylindres
- rates d allumage persistants
- consommation d huile anormale guides uses
- fumee bleue a l echappement

## Procédure de Diagnostic

Pour diagnostiquer un problème de soupape d'admission:

1. **Inspection visuelle** - Examiner l'état du soupape d'admission
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bagues-d-etancheite-moteur
- joint-de-cache-culbuteurs
- joint-de-collecteur
- joint-de-culasse
- poulie-d-arbre-a-came
- poussoir-de-soupape
- soupape-d-echappement

## Critères de Compatibilité

Pour commander le bon soupape d'admission, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"

## FAQ

**Soupape d'admission OE ou adaptable ?**
Les soupapes OES (AE, Freccia, TRW) sont fiables. Vérifiez les cotes exactes (longueur, diamètre tête et queue). Ne pas mélanger les qualités.

**Comment savoir si une soupape d'admission est HS ?**
Perte de compression sur un cylindre, claquement, ratés d'allumage, consommation d'huile excessive (guide usé).

**Tous les combien changer les soupapes d'admission ?**
Pas de périodicité. Durée de vie 200 000+ km. Remplacement lors d'une réfection culasse ou après casse distribution.

**Peut-on changer une soupape soi-même ?**
Non recommandé. Nécessite un lève-soupapes, une rectification des sièges, et un contrôle d'étanchéité. Travail de spécialiste.

**Quelle erreur éviter avec les soupapes ?**
Ne jamais rodé une soupape neuve sur un siège usé. Remplacer aussi les guides si jeu excessif. Contrôler la planéité de la culasse.
