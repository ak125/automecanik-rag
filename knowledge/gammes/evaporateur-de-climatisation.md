---
category: climatisation
slug: evaporateur-de-climatisation
title: Evaporateur de climatisation
pg_id: 471
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
  last_enriched_by: skill:phase5-hella-ngk
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Absorbe la chaleur de l'air habitacle pour produire du froid - Circuit habitacle uniquement
  must_be_true:
  - absorber la chaleur
  must_not_contain:
  - moteur
  - refroidissement
  - radiateur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - compresseur-de-climatisation
  - condenseur-de-climatisation
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
    min: 100
    max: 400
    currency: EUR
    unit: l'unite
    source: estimation categorie
  quality_tiers:
  - tier: Pièce OE (Origine Équipement)
    description: Évaporateur identique à l origine. Surface d échange optimale, traitement anti-corrosion conforme. Compatible
      raccords et boîtier de soufflage d origine.
  - tier: Équivalent OE (spécialistes échangeurs thermiques)
    description: 'Fabricants d échangeurs de rang 1 fournissant les constructeurs. Deux grandes familles techniques : évaporateur
      type MS (ailette intérieure entre plaques, circuit complexe) et tubes multivoies.'
  - tier: Générique compatible
    description: Peut convenir si les dimensions et raccords sont strictement conformes. Vérifier la surface d échange et
      le traitement anti-corrosion.
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
    label: Climatisation inefficace malgre recharge recente
    severity: confort
  - id: S2
    label: Odeur de moisi ou d humidite a la ventilation
    severity: confort
  - id: S3
    label: Buee persistante sur le pare-brise en mode clim
    severity: confort
  - id: S4
    label: Flaque d eau anormale sous le tableau de bord
    severity: confort
  - id: S5
    label: Bruit gargouillement boitier ventilation
    severity: confort
  - id: S6
    label: Mauvaises odeurs des l enclenchement de la clim
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : climatisation inefficace malgre recharge recente'
  depose_steps: []
  quick_checks:
  - 'Observer : climatisation inefficace malgre recharge recente ?'
  - Odeur de moisi ou d humidite a la ventilation ?
  - 'Observer : buee persistante sur le pare-brise en mode clim ?'
  - 'Observer : flaque d eau anormale sous le tableau de bord ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Climatisation inefficace malgre recharge recente
  - Odeur de moisi ou d humidite a la ventilation
  - Buee persistante sur le pare-brise en mode clim
  - Flaque d eau anormale sous le tableau de bord
  - Bruit gargouillement boitier ventilation
  - Mauvaises odeurs des l enclenchement de la clim
  good_practices:
  - Faire tourner la climatisation 10 min par semaine meme en hiver
  - Remplacement du filtre d habitacle chaque annee
  - Recharge de gaz par un professionnel equipe (circuit sous pression)
  - Controle d etancheite si baisse de performance
rendering:
  pgId: '471'
  intro_title: A quoi sert Evaporateur de climatisation ?
  risk_title: Pourquoi remplacer Evaporateur de climatisation a temps ?
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
  - question: Evaporateur clim OE ou adaptable ?
    answer: Les évaporateurs OES (Valeo, Denso, Nissens) garantissent une surface d'échange optimale. Les adaptables moins
      chers peuvent être moins efficaces.
  - question: Comment savoir si mon évaporateur fuit ?
    answer: Clim qui ne refroidit plus, buée sur le pare-brise en mode clim, odeur d'humidité ou de moisi, flaque d'eau sous
      le tableau de bord.
  - question: Tous les combien changer l'évaporateur ?
    answer: Pas de périodicité. Durée de vie 10 à 15 ans. Nettoyage antibactérien annuel recommandé pour éviter l'encrassement.
  - question: Peut-on nettoyer l'évaporateur sans le démonter ?
    answer: Oui, avec un nettoyant mousse via les conduits de ventilation. Efficace pour les mauvaises odeurs mais pas pour
      les fuites.
  - question: Quelle erreur éviter avec l'évaporateur ?
    answer: Ne pas négliger les mauvaises odeurs (moisissures sur l'évaporateur). Remplacer aussi le filtre d'habitacle encrassé.
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
doc_id: 190aa91d-7f5a-5adb-af09-ec5e39aae00d
content_hash: sha256:a54b85a18dcd4fbe
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
  _source: HELLA TechWorld
  _validation_status: oem_verified
  _enriched_at: '2026-03-29'
  technical_notes:
    position_circuit: 'cote basse pression (entre detendeur et compresseur)'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    L'évaporateur de climatisation est un échangeur de chaleur fabriqué en
    aluminium qui absorbe l'énergie provenant du médium à refroidir par le biais
    d'unliquide s'évaporant après avoir été détendu. Il est le dernier
    composantdans le système de climatisation, il se situe dans le bloc de
    chauffage. Il estcomposé d'ailettes (multitude d'ailettesdestinées à
    augmenter la surface d'échange thermique) qui permettentd'enlever toute
    l'humidité de l'air pulsée dans l'habitacle. Au cours du passage dans
    l'évaporateur de climatisation, le fluidefrigorigène passe de l'état liquide
    à l'état gazeux (évaporation).L'eau déposée sur lesailettes, est évacuée
    sous le véhicule. En savoir plus : evaporateur de climatisation — définition
    et rôle mécanique 🚨 Bruit Evaporateur de climatisation : causes et
    diagnostic
  S2: >-
    Un évaporateur de climatisation défectueuxprésente plusieurs symptômes : -
    Humidité élevée dansl'habitacle. - Embuage important lorsquele véhicule est
    en mouvement. - Vous sentez de la mauvaiseodeur lors du fonctionnement de
    climatisation. - Manque de contrôle sur latempérature de l'air en
    circulation. Diagnostic complet : identifier une panne de evaporateur de
    climatisation
  S3: >-
    L'évaporateur de climatisation absorbe la chaleur de l'air de l'habitacle
    pour produire du froid : le fluide frigorigène se vaporise à l'intérieur de
    ses tubes, captant l'énergie thermique de l'air soufflé par le pulseur. Il
    est intégré dans le boîtier de ventilation, derrière le tableau de bord —
    son accès implique souvent un démontage partiel ou complet de la planche de
    bord. Un évaporateur mal sélectionné ou de cotes différentes ne se loge pas
    dans le boîtier et impose une reprise d'intervention coûteuse. Voici les
    critères à maîtriser avant commande. - Référence véhicule et cotes hors-tout
    précises — L'évaporateur est dimensionné pour s'insérer dans un emplacement
    fixe du boîtier de ventilation. Une différence de 3 mm en hauteur ou en
    largeur empêche physiquement le montage ou génère des vibrations et des
    bruits de frottement. Vérifier les cotes sur la documentation technique ou
    mesurer la pièce d'origine avant démontage. - Compatibilité fluide R134a ou
    R1234yf — Comme pour les autres composants du circuit frigorifique,
    l'évaporateur est formulé pour un fluide donné. Les alliages d'aluminium,
    les joints de raccord et les pressions de service sont différents entre
    R134a et R1234yf. Un évaporateur R134a monté sur circuit R1234yf présente un
    risque de corrosion galvanique accélérée. - Nombre de rangées de tubes et
    surface d'échange — La surface d'échange de l'évaporateur (exprimée
    indirectement par le nombre de rangées et l'espacement des ailettes)
    conditionne l'efficacité frigorifique. Un évaporateur de remplacement avec
    moins de rangées que l'original délivrera moins de froid et fera cycler le
    compresseur plus fréquemment. - Position et type de raccords frigorifiques —
    Les raccords d'entrée (liquide haute pression après détendeur) et de sortie
    (vapeur basse pression vers compresseur) doivent être positionnés à
    l'identique. Certains évaporateurs utilisent des raccords à emboîtement
    rapide (push-lock), d'autres des raccords à filetage. Vérifier le type avant
    commande pour s'assurer de la compatibilité avec les durites en place. -
    Traitement anti-corrosion des ailettes — L'évaporateur est en contact avec
    de l'eau condensée et l'air extérieur humide. Un évaporateur avec des
    ailettes en aluminium traité (revêtement époxyde ou céramique) résiste mieux
    à la corrosion et aux moisissures responsables des mauvaises odeurs. Ce
    critère est important sur les véhicules utilisés en environnement côtier ou
    humide. - Pièces à remplacer lors de l'ouverture du circuit — L'ouverture du
    circuit pour remplacer l'évaporateur impose le changement systématique de la
    bouteille déshydratante et la vérification du détendeur. Toujours remettre
    le circuit sous vide pendant au moins 45 minutes avec une pompe à vide à
    deux étages avant recharge : une présence d'humidité résiduelle dans le
    circuit provoque une corrosion interne accélérée des aluminium. Pour aller
    plus loin : consultez notre guide d'achat evaporateur de climatisation —
    comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Evaporateur de
    climatisation pour connaître les spécifications. Note : pour leremplacement
    de l'évaporateur de climatisation il doit être fait par un professionnel si
    non ilfaut se référé à la revue technique de vote voiture. - Videz le
    circuit de climatisation. - Débranchez la batterie. - Libérez l'accès pour
    le démontage du détendeur de climatisation . - Démontez le détendeur de
    climatisation. - Dépressuriser le circuit derefroidissement. - Pincer les
    durites de liquide de refroidissement à l'aide des pinces à durites. -
    Démontez les clips deverrouillage des durites de liquide de refroidissement.
    - Désaccoupler les durites de liquide de refroidissement. Note : Évacuer un
    maximum de liquide de refroidissement del'aérotherme à l'aide d'une
    soufflette placée en entrée, placer un récipientpour récupérer le liquide de
    refroidissement. - Desserrez la vis defixation de la plaque de maintien des
    durites de liquide de refroidissement. - Démontez la plaque demaintien des
    durites de liquide de refroidissement et le joint d'étanchéité. - Démontez
    tous le tableau de bord. - Désaccouplez les conduits d'airdes places
    arrière. - Déconnectez les connecteursdu groupe de chauffage. - Démontez le
    groupe dechauffage. - Démontez l'évaporateur declimatisation.
  S4_REPOSE: >-
    Le remontage d'un évaporateur de climatisation est une intervention lourde
    qui mobilise le tableau de bord en quasi-totalité. Une fois l'évaporateur en
    place, ne bâclez pas les étapes de vérification : un raccord frigorigène mal
    serré ou une durite de chauffage mal clipsée génèrent des avaries coûteuses
    dès la première mise en route. - Vérifiez que l'évaporateur neuf est
    identique à celui déposé : forme, dimensions, positions des raccords
    frigorigènes et des durites de chauffage. Un modèle non conforme ne peut pas
    être raccordé sans forcer. - Contrôlez simultanément l'état du détendeur de
    climatisation : si le circuit a été ouvert pour remplacer l'évaporateur,
    c'est le moment de remplacer aussi le détendeur si son état est douteux. -
    Positionnez l'évaporateur dans le boîtier de chauffage-ventilation. Assurez-
    vous que les joints de boîtier sont correctement en place avant de refermer
    le boîtier. - Remontez le groupe de chauffage complet dans le boîtier et
    rebranchez les connecteurs électriques du moto-ventilateur et des volets de
    distribution d'air. - Raccordez les durites de liquide de refroidissement du
    radiateur de chauffage sur leurs raccords. Posez les clips de verrouillage
    jusqu'au déclic. Vérifiez l'absence de pliure. - Accouplez les conduits
    d'air des places arrière si votre véhicule en est équipé. Remontez
    l'ensemble du tableau de bord en inversant l'ordre de dépose. - Reconnectez
    tous les connecteurs électriques du tableau de bord (climatisation,
    chauffage, éclairage, airbag). Vérifiez le verrouillage de chaque
    connecteur. - Remontez les pièces déposées dans le compartiment moteur pour
    accéder aux raccords frigorigènes. Rebranchez la batterie (borne positive en
    premier). - Faites recharger le circuit de climatisation par un technicien
    habilité : récupération des éventuels résidus, mise sous vide 30 minutes
    minimum, puis charge en réfrigérant et huile PAG aux quantités constructeur.
    - Contrôlez le niveau de liquide de refroidissement et purgez le circuit de
    chauffage si nécessaire. Vérifiez le bon fonctionnement de la climatisation
    et du chauffage en mode automatique. ✅ Après remontage, vérifiez les
    spécifications dans la fiche technique Evaporateur de climatisation.
  S5: >-
    Erreurs frequentes avec l'evaporateur de climatisation : - Ne pas faire le
    vide du circuit avant recharge — l'air et l'humidite residuels degradent le
    compresseur et provoquent des surpressions- Oublier de remplacer le
    detendeur et la bouteille deshydratante en meme temps — un detendeur
    encrasse ou une bouteille saturee reduisent l'efficacite de l'evaporateur
    neuf- Ne pas nettoyer le boitier de ventilation lors du remplacement — les
    moisissures et debris accumules contaminent l'evaporateur neuf et provoquent
    des odeurs- Ignorer une odeur de moisi persistante a la mise en route de la
    ventilation — signe d'evaporateur colonise par des bacteries, un traitement
    antibacterien est necessaire- Ne pas verifier l'etancheite du circuit apres
    remontage — une micro-fuite vide le circuit en quelques semaines
  S6: >-
    L'évaporateur de climatisation absorbe la chaleur de l'air habitacle en
    faisant circuler le fluide frigorigène à basse pression. Son remplacement
    est une intervention majeure qui nécessite le démontage du tableau de bord
    sur la plupart des véhicules. Les vérifications post-remplacement couvrent à
    la fois l'étanchéité du circuit frigorigène et la propreté du boîtier de
    ventilation. - Vérifier l'étanchéité du circuit frigorigène après recharge :
    utiliser un détecteur de fuite électronique pour contrôler les raccords de
    l'évaporateur dans le boîtier de ventilation. Ces raccords sont difficiles
    d'accès — inspecter avec une sonde flexible ou un traceur fluorescent UV
    visible à la lampe. - Contrôler la pression basse en régime stabilisé :
    après 10 minutes de fonctionnement à régime moteur stabilisé, la pression
    côté basse pression doit être entre 1,5 et 2,5 bar. Une pression inférieure
    à 1 bar indique un givrage de l'évaporateur — vérifier le détendeur associé
    et la quantité de fluide. - Vérifier l'absence de fuites d'eau sous le
    tableau de bord : l'évaporateur produit des condensats qui s'évacuent par un
    tuyau de drainage. Contrôler que ce tuyau est correctement reconnecté et non
    obstrué. Une flaque d'eau sous le tableau de bord après 10 minutes de
    climatisation indique un drainage bouché ou mal raccordé. - Contrôler le
    débit d'air par les bouches de ventilation : après le remontage du tableau
    de bord, tester chaque vitesse de ventilateur. Un débit insuffisant sur une
    ou plusieurs vitesses peut indiquer un boîtier de ventilation mal remonté ou
    un joint de boîtier absent qui crée une fuite d'air interne. - Tester
    l'absence de mauvaises odeurs après le premier démarrage de la clim : un
    évaporateur neuf peut émettre une légère odeur de plastique lors des
    premières utilisations. En revanche, une odeur de moisi persistante dès les
    premières minutes signale que la canalisation de drainage est obstruée ou
    que de l'humidité résiduelle reste dans le boîtier. - Vérifier l'efficacité
    de refroidissement sur 10 minutes : fenêtres fermées, ventilateur à
    puissance maximale, la température aux bouches doit descendre sous 10 °C en
    5 minutes à 20-25 °C ambiants. Un évaporateur neuf correctement installé
    restaure les performances d'origine du système de climatisation. - Contrôler
    l'absence de bruits de gargouillement dans le boîtier : des bruits de
    gargouillement pendant les 5 premières minutes sont normaux (fluide
    frigorigène qui circule à nouveau). Des bruits persistants après 10 minutes
    de fonctionnement signalent un problème de niveau de fluide ou de drainage
    des condensats.
  S7: >-
    Quel est le prix d'un evaporateur de climatisation ?Le prix varie selon le
    véhicule et la marque. Utilisez notre sélecteur pour trouver l'evaporateur
    de climatisation compatible avec votre véhicule et comparer les tarifs des
    différents équipementiers.Comment savoir si l'evaporateur de climatisation
    est à changer ?Les signes d'usure les plus courants sont détaillés dans la
    section diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par
    un professionnel.Peut-on rouler avec un evaporateur de climatisation
    défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la
    pièce dans la sécurité du véhicule. Consultez la section symptômes pour
    évaluer l'urgence du remplacement.- compresseur de climatisation -
    condenseur de climatisation - detendeur de climatisation - filtre d
    habitacle - pulseur d air d habitacle
  S8: >-
    Comment choisir Evaporateur de climatisation compatible avec mon
    vehiculeRenseignez marque, modele, type moteur et annee, puis verifiez la
    reference Quand remplacer Evaporateur de climatisation ?En cas de
    climatisation inefficace malgre recharge recente ou de degradation Puis-je
    monter Evaporateur de climatisation sans verification atelierLe montage peut
    exiger controles de couple, alignement et references.
  META: >-
    {"meta_title":"Évaporateur clim : odeurs et remplacement |
    AutoMecanik","meta_description":"Odeur de moisi, buée persistante sur le
    pare-brise ou clim inefficace malgré recharge ? Découvrez comment
    diagnostiquer un évaporateur de climatisation défaillant et choisir la bonne
    pièce.","robots":"index,follow","og_type":"article","schema_type":"HowTo"}
---

# Evaporateur de climatisation - Guide Diagnostic Complet

## Fonction et Rôle

Absorbe la chaleur de l'air habitacle pour produire du froid - Circuit habitacle uniquement

**Actions principales:** absorber la chaleur

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- climatisation inefficace malgre recharge recente
- odeur de moisi ou d humidite a la ventilation
- buee persistante sur le pare-brise en mode clim
- flaque d eau anormale sous le tableau de bord
- bruit gargouillement boitier ventilation
- mauvaises odeurs des l enclenchement de la clim

## Procédure de Diagnostic

Pour diagnostiquer un problème de evaporateur de climatisation:

1. **Inspection visuelle** - Examiner l'état du evaporateur de climatisation
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

- compresseur-de-climatisation
- condenseur-de-climatisation
- detendeur-de-climatisation
- filtre-d-habitacle
- pulseur-d-air-d-habitacle

## Critères de Compatibilité

Pour commander le bon evaporateur de climatisation, vous devez connaître:

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

**Evaporateur clim OE ou adaptable ?**
Les évaporateurs OES (Valeo, Denso, Nissens) garantissent une surface d'échange optimale. Les adaptables moins chers peuvent être moins efficaces.

**Comment savoir si mon évaporateur fuit ?**
Clim qui ne refroidit plus, buée sur le pare-brise en mode clim, odeur d'humidité ou de moisi, flaque d'eau sous le tableau de bord.

**Tous les combien changer l'évaporateur ?**
Pas de périodicité. Durée de vie 10 à 15 ans. Nettoyage antibactérien annuel recommandé pour éviter l'encrassement.

**Peut-on nettoyer l'évaporateur sans le démonter ?**
Oui, avec un nettoyant mousse via les conduits de ventilation. Efficace pour les mauvaises odeurs mais pas pour les fuites.

**Quelle erreur éviter avec l'évaporateur ?**
Ne pas négliger les mauvaises odeurs (moisissures sur l'évaporateur). Remplacer aussi le filtre d'habitacle encrassé.


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
