---
category: freinage
slug: accumulateur-de-pression
title: Accumulateur de pression
pg_id: 1064
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
  role: Stocker la pression hydraulique pour assister le freinage et maintenir la pression dans le circuit
  must_be_true:
  - stocker la pression
  - assister le freinage
  - maintenir la pression hydraulique
  must_not_contain:
  - universel
  - tous modeles
  - adaptable tous
  confusion_with:
  - term: accumulateur-de-pression-de-carburant
    difference: L'accumulateur de pression freinage stocke la pression hydraulique du circuit de frein, celui de carburant
      maintient la pression dans la rampe d'injection
  - term: maitre-cylindre-de-frein
    difference: Le maitre-cylindre genere la pression, l'accumulateur la stocke
  related_parts:
  - pompe-hydraulique-systeme-de-freinage
  - maitre-cylindre-de-frein
  - agregat-de-freinage
  - flexible-de-frein
selection:
  criteria:
  - Marque de votre vehicule
  - Modele de votre vehicule
  - Motorisation de votre vehicule
  - Annee de votre vehicule
  - Type de systeme de freinage (hydraulique assiste, Citroen hydractive, etc.)
  - Pression de service
  anti_mistakes:
  - universel
  - tous modeles
  - adaptable tous
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
    label: Pedale de frein dure et difficile a enfoncer
    severity: securite
  - id: S2
    label: Pompe hydraulique qui tourne en continu ou trop souvent
    severity: securite
  - id: S3
    label: Freinage assiste defaillant apres quelques coups de frein
    severity: securite
  - id: S4
    label: Voyant de frein allume au tableau de bord
    severity: securite
  - id: S5
    label: Bruit de claquement dans le circuit de freinage
    severity: confort
  causes:
  - membrane interne de l'accumulateur percee
  - perte de pression d'azote dans la sphere
  - usure naturelle apres 100000 km ou 8-10 ans
  quick_checks:
  - 'Observer : pedale de frein dure et difficile a enfoncer ?'
  - 'Observer : pompe hydraulique qui tourne en continu ou trop souvent ?'
  - 'Observer : freinage assiste defaillant apres quelques coups de frein ?'
  - Voyant de frein allume au tableau de bord ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Verifier si la pedale devient dure apres 3-4 freinages moteur eteint. Duree de vie 80000 a 150000 km.
  wear_signs:
  - Pedale de frein dure et difficile a enfoncer
  - Pompe hydraulique qui tourne en continu ou trop souvent
  - Freinage assiste defaillant apres quelques coups de frein
  - Voyant de frein allume au tableau de bord
  - Bruit de claquement dans le circuit de freinage
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '1064'
  faq:
  - question: Comment tester l'accumulateur de pression ?
    answer: Moteur eteint, appuyer 10 fois sur la pedale de frein. Si elle devient dure des le 3eme appui, l'accumulateur
      est HS.
  - question: Peut-on rouler avec un accumulateur defaillant ?
    answer: Oui mais le freinage sera moins assiste. Intervention a prevoir rapidement pour la securite.
  - question: Accumulateur OE ou adaptable ?
    answer: Privilegier l'OE car la pression de service doit correspondre exactement aux specifications constructeur.
  - question: Combien coute un accumulateur de pression ?
    answer: Entre 80 et 400 EUR selon le vehicule. Les systemes Citroen hydractive sont plus couteux.
  - question: Quelle erreur eviter ?
    answer: Ne jamais ouvrir un accumulateur (gaz sous pression). Toujours purger le circuit de frein apres remplacement.
  quality:
    score: 60
    source: manual:claude-r3-kp
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modeles
  - adaptable tous
  requires_vehicle: true
doc_id: 3069ccff-bc79-55a0-8519-4c12a236cd2d
content_hash: sha256:d02c488259e517ac
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
phase5_enrichment:
  _source: bremboparts.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: false
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    L'accumulateur de pression est une sorte de sphère qui sert à stocker une
    réserve de pression de liquide hydraulique afin de garantir un freinage
    suffisant m&ecirc;me si une chute brutale de pression devait se produire sur
    votre véhicule. La pression de liquide hydraulique est ensuite distribuée à
    l'ensemble des sphères accumulatrices. Pour vérifier le fonctionnement de
    votre accumulateur, mettez votre voiture en route quelques minutes, le temps
    que l'accumulateur soit bien sous pression. Coupez le moteur. Il est
    normalement alors de faire une vingtaine de freinages avant que le voyant ne
    se déclenche. Il existe plusieurs modèles d'accumulateurs pour une
    m&ecirc;me auto. Vérifiez bien dans la fiche produit la compatibilité des
    accumulateurs avec votre véhicule.
  S2: >-
    L'accumulateur ne possède pas une période de remplacement mais c'est une
    pièce usable vu les conditions d'utilisation de véhicule, dans ce cas il
    faut faire un contrôle chaque fois ou en constate un problème au niveau de
    cette pièce et la remplacer si nécessaire parce qu'on risque à avoir
    plusieurs problèmes en cas de dysfonctionnement.
  S3: >-
    L'accumulateur de pression hydraulique (également appelé sphère hydraulique
    ou accumulateur de sphère sur certains Citroën) stocke l'énergie hydraulique
    sous forme de gaz comprimé (azote) séparé du liquide hydraulique par une
    membrane en caoutchouc. Lorsque le circuit hydraulique est sous pression, il
    se charge. Lorsque la pression chute, il la compense instantanément. Un
    mauvais choix de pièce dégrade les performances ou endommage le circuit
    haute pression. - Identifier l'application précise : l'accumulateur de
    pression n'est pas universel. Trois applications distinctes existent sur les
    véhicules : - Freinage assisté hydraulique (servofrein hydraulique
    Citroën/Peugeot LDS, ex-BX, Xantia, XM, C5, 407, Xsara Picasso) :
    accumulateur cylindrique vissé sur le groupe hydraulique ou le boîtier de
    freinage. - Suspension hydraulique active (Citroën Hydractive, Xantia
    Activa) : sphères de suspension sphériques situées sur chaque train. -
    Direction assistée hydraulique : accumulateur de pression sur certaines
    crémaillères hydrauliques haute pression. Ces pièces se ressemblent parfois
    mais ne sont jamais interchangeables entre applications. - Pression de
    précharge à l'azote : la précharge usine varie entre 40 et 100 bar selon
    l'application et le constructeur. Elle détermine la plage de stockage
    d'énergie utile. Un accumulateur avec une précharge incorrecte (trop haute
    ou trop basse) dégrade les performances dès l'installation et ne se répare
    pas à froid. Vérifier la valeur de précharge indiquée sur l'étiquette de
    l'accumulateur d'origine ou dans la documentation technique. - Volume de la
    chambre à gaz : exprimé en centilitres ou décilitres, le volume détermine la
    quantité d'énergie stockable et la durée d'autonomie de l'assistance.
    Respecter scrupuleusement le volume d'origine — un volume plus petit réduit
    l'autonomie de freinage et fatigue la pompe hydraulique. - Type de
    raccordement hydraulique : filetage (BSP, JIC, SAE) et diamètre du port de
    raccordement. Vérifier le pas de vis (généralement M22x1.5 ou M24x1.5 sur
    freinage Citroën/Peugeot) et le type de joint d'étanchéité (joint plat ou
    joint torique). - Marques de référence : LPR, ATE, Febi Bilstein, Mando pour
    le freinage ; pièces d'origine Citroën/Stellantis pour les suspensions
    Hydractive (la sphère de suspension est une pièce très spécifique). Les
    équipementiers OES garantissent la précharge azote correcte contrairement
    aux copies génériques.
  S4_DEPOSE: >-
    Intervention sur circuit haute pression (jusqu'à 200 bar). La
    dépressurisation complète est impérative avant toute ouverture d'un raccord
    hydraulique. Un circuit sous pression ouvert sans précaution projette du
    liquide hydraulique LHM ou DOT à très grande vitesse, pouvant causer des
    blessures graves. - Dépressuriser le circuit hydraulique : couper le contact
    et appuyer sur la pédale de frein 25 à 30 fois d'affilée, à fond, contact
    coupé. La pédale doit progressivement devenir dure et résistante — c'est la
    preuve que la pression de l'accumulateur est dissipée. Sur les Citroën avec
    suspension hydraulique, appuyer également sur le bouton de
    relevage/abaissement de la suspension pour vider les sphères de suspension.
    - Préparer la zone d'intervention : placer plusieurs chiffons absorbants
    larges sous et autour du groupe hydraulique ou de la zone d'accumulateur. Le
    LHM (liquide hydraulique minéral vert) et le LDS sont nocifs pour les
    peintures et les surfaces caoutchoucs environnantes. Travailler avec des
    gants. Récupérer le liquide écoulé dans un bac pour élimination conforme. -
    Localiser l'accumulateur : selon le modèle et l'application, l'accumulateur
    se trouve sur le groupe hydraulique (boîtier métallique situé généralement
    derrière le moteur côté passager sur Citroën/Peugeot), ou directement sur la
    rampe de freinage ABS/ESP. Sur certains modèles, déposer un cache plastique
    ou un support pour y accéder. - Déposer l'accumulateur : utiliser une clé
    adaptée à la taille du corps (souvent 30, 32 ou 36 mm selon le modèle).
    Desserrer lentement — un léger suintement hydraulique est attendu et normal,
    signe que la dépressurisation n'est pas totale. Continuer à dévisser
    progressivement en laissant le liquide s'écouler. Récupérer le joint plat ou
    torique qui se détache souvent avec l'accumulateur. - Inspecter le port de
    raccordement : nettoyer l'alésage du port avec une lingette propre. Vérifier
    l'état du filetage interne — un filet endommagé sur le groupe hydraulique
    oblige au remplacement du groupe complet. Contrôler l'absence de résidus de
    l'ancien joint dans le logement. - Préparer le nouvel accumulateur :
    vérifier que la précharge azote correspond (voir étiquette ou
    documentation). Le nouvel accumulateur ne doit jamais être comprimé, tordu
    ou percé. Installer le joint neuf fourni sans le graisser — le LHM lui-même
    assure la lubrification à la mise en pression. - Visser le nouvel
    accumulateur : engager à la main sur les premiers filets pour éviter le
    croisement. Serrer progressivement à la clé au couple constructeur indiqué
    dans la documentation (généralement 30 à 50 N.m selon l'application). Ne
    jamais sur-serrer : le corps en aluminium du groupe hydraulique se déforme
    facilement. - Purger et remettre en service : vérifier le niveau de liquide
    hydraulique dans le réservoir. Démarrer le moteur et laisser la pompe monter
    en pression. Sur les systèmes Citroën, la suspension doit se relever à la
    hauteur normale en moins de 30 secondes. Appuyer plusieurs fois sur la
    pédale de frein pour valider la pression.
  S5: >-
    - Ouvrir le circuit sans dépressurisation complète : le circuit de freinage
    hydraulique Citroën/Peugeot peut maintenir une pression résiduelle de 150 à
    200 bar plusieurs minutes après l'arrêt du moteur. À cette pression, du
    liquide projeté traverse la peau et provoque des embolies graisseuses
    potentiellement mortelles. Toujours effectuer les 25 à 30 appuis sur pédale
    contact coupé et attendre que la pédale soit dure avant d'ouvrir un raccord.
    - Confondre accumulateur de freinage et sphère de suspension : les
    accumulateurs de freinage (cylindriques, filetés sur le groupe hydraulique)
    et les sphères de suspension (sphériques ou en forme de champignon sur les
    trains) ont des précharges azote totalement différentes. Monter une sphère
    de suspension à la place d'un accumulateur de freinage provoque une perte
    d'assistance au freinage immédiate. - Réutiliser le joint d'étanchéité
    d'origine : le joint plat ou torique comprimé lors du premier montage ne
    garantit plus l'étanchéité haute pression à la repose. Toujours utiliser le
    joint neuf fourni avec la pièce ou acheter le joint correspondant (matière
    Viton pour LHM, EPDM pour DOT). - Omettre la purge après montage : si de
    l'air a été introduit dans le circuit de freinage hydraulique pendant
    l'ouverture du raccord, l'assistance ne fonctionne pas correctement. Sur les
    systèmes Citroën LDS/LHM, la pompe hydraulique doit pouvoir évacuer l'air en
    quelques cycles. Si la pédale reste spongieuse après 5 minutes de
    fonctionnement, une purge complète du circuit de freinage s'impose. - Sur-
    serrer l'accumulateur sur un groupe hydraulique aluminium : la tête de
    fixation est souvent en aluminium sur les groupes modernes. Un sur-serrage
    au-delà du couple constructeur (30 à 50 N.m selon modèle) écrase le filetage
    et rend l'étanchéité impossible sans remplacement du groupe. Utiliser une
    clé dynamométrique. - Remplacer l'accumulateur sans vérifier la pompe
    hydraulique : si la pompe tourne en permanence avec un accumulateur neuf, la
    pompe elle-même est défaillante. Diagnostiquer les deux pièces avant
    commande. Tester en coupant le moteur et en comptant les appuis pédale avant
    durcissement : 10 à 20 appuis = accumulateur sain ; moins de 5 appuis avec
    accumulateur neuf = pompe défaillante.
  S6: >-
    - Montée en pression du circuit : démarrer le moteur et observer le
    comportement de la pompe hydraulique. Sur un système Citroën/Peugeot
    LHM/LDS, la pompe doit tourner entre 10 et 30 secondes pour monter le
    circuit à la pression nominale (généralement 150 à 200 bar), puis se mettre
    en sécurité ou ralentir. Une pompe qui tourne en permanence sans s'arrêter
    après 60 secondes indique soit une fuite hydraulique soit un accumulateur de
    mauvaise qualité ou de mauvaise précharge. - Test de l'assistance au
    freinage : couper le moteur et appuyer sur la pédale de frein à fond 10 fois
    de suite. Compter le nombre d'appuis avant que la pédale devienne dure et
    résistante. Un accumulateur neuf et correctement préchargé doit tenir 10 à
    20 appuis. Moins de 5 appuis avec une pièce neuve indique une précharge
    azote incorrecte ou une membrane interne défaillante — retourner la pièce. -
    Contrôle d'étanchéité au raccord : après 5 minutes de fonctionnement sous
    pression, inspecter visuellement la zone du raccord avec une lingette
    propre. Toute trace de liquide LHM (vert) ou LDS (jaune/vert) impose un
    reserrage ou un remplacement du joint. Laisser tourner le moteur 15 minutes
    supplémentaires et refaire l'inspection — les fuites à chaud apparaissent
    souvent en second contrôle. - Vérification du niveau de liquide hydraulique
    : compléter le réservoir si le niveau a baissé pendant l'opération. Sur les
    systèmes Citroën, le réservoir de liquide LHM/LDS se situe généralement dans
    le compartiment moteur. Ne jamais mélanger LHM (minéral, vert) avec du DOT
    (synthétique, incolore/brun) — incompatibilité totale qui détruit les joints
    en quelques heures. - Essai sur route avec freinages successifs : effectuer
    5 à 10 freinages francs à vitesse modérée. L'assistance doit être présente
    et constante du premier au dixième freinage. Sur les Citroën avec suspension
    hydraulique, vérifier également le maintien de hauteur de caisse en virage
    et sur obstacles — un accumulateur de freinage neuf ne doit pas modifier le
    comportement de la suspension.
  S7: >-
    L'accumulateur de pression fait partie d'un circuit hydraulique haute
    pression dans lequel plusieurs composants travaillent en interdépendance.
    Une défaillance de l'accumulateur sollicite excessivement la pompe
    hydraulique et peut masquer une défaillance adjacente. - Pompe hydraulique
    de freinage — si la pompe tourne en permanence, l'accumulateur de pression
    est la cause primaire dans 80 % des cas. Toutefois, si la pompe continue de
    tourner en continu avec un accumulateur neuf et correctement préchargé, la
    pompe hydraulique elle-même est défaillante (rotor usé, clapets de décharge
    grippés). Le diagnostic doit toujours vérifier les deux pièces avant de
    conclure. - Agrégat de freinage ABS/ESP — le groupe hydraulique complet
    intègre parfois l'accumulateur, la pompe et les électrovannes ABS dans un
    seul bloc. Si plusieurs composants sont usés simultanément ou si le boîtier
    présente des fissures, le remplacement du bloc complet peut s'avérer plus
    économique que la réparation pièce par pièce. Un test de pression avec
    manomètre permet de localiser la défaillance. - Maître-cylindre de frein —
    si la pédale reste molle ou spongieuse malgré un accumulateur et une pompe
    neufs et en bon état, le maître-cylindre est à examiner. Un maître-cylindre
    usé laisse le liquide passer en interne et empêche la montée en pression du
    circuit, même avec un accumulateur chargé. - Servofrein — sur les véhicules
    avec assistance mécanique (à dépression moteur) en complément de
    l'assistance hydraulique, le servofrein peut masquer une perte d'assistance
    hydraulique partielle. Tester les deux systèmes séparément si l'assistance
    semble faible sans code défaut hydraulique. - Liquide hydraulique LHM ou
    liquide de frein DOT — à contrôler et compléter après l'intervention. Sur
    circuits LHM (Citroën/Peugeot hydraulique), un liquide dégradé ou contaminé
    par de l'eau accélère l'usure de la membrane de l'accumulateur. Vidanger le
    circuit tous les 2 ans ou tous les 60 000 km.
  S8: >-
    Pourquoi la pompe hydraulique tourne-t-elle en permanence sur ma Citroën ou
    Peugeot ? C'est le signe classique d'un accumulateur de pression à membrane
    percée ou à azote épuisé. La membrane interne en caoutchouc se dégrade avec
    le temps (chaleur, cycles de pression répétés) et finit par se perforer.
    L'azote de précharge s'échappe alors dans le liquide hydraulique, et
    l'accumulateur ne peut plus stocker d'énergie. La pompe doit maintenir la
    pression en permanence pour compenser. Tester en coupant le moteur et en
    appuyant sur la pédale : moins de 5 appuis avant durcissement confirme
    l'accumulateur à plat. Un accumulateur neuf résout ce problème dans 80 % des
    cas ; si la pompe continue de tourner avec une pièce neuve, la pompe elle-
    même est défaillante. Comment tester un accumulateur de pression sans le
    démonter ? Le test de base ne nécessite aucun outil spécial. Couper le
    contact (moteur froid ou chaud peu importe). Appuyer sur la pédale de frein
    à fond et compter le nombre d'appuis avant que la pédale devienne dure. Un
    accumulateur sain produit 10 à 20 appuis. Entre 5 et 10 appuis :
    accumulateur en fin de vie mais encore fonctionnel. Moins de 5 appuis :
    accumulateur épuisé à remplacer immédiatement. Sur les véhicules Citroën
    avec suspension hydraulique, un autre indicateur est la hauteur de caisse
    après arrêt prolongé — un véhicule qui s'affaisse sur un ou plusieurs trains
    indique des sphères de suspension à plat. Peut-on recharger l'azote d'un
    accumulateur usagé plutôt que le remplacer ? La recharge d'azote est
    techniquement possible sur les accumulateurs équipés d'une valve Schrader
    accessible, à condition que la membrane interne soit intacte. Elle nécessite
    un équipement spécialisé (manomètre haute pression, bouteille d'azote pur)
    et la connaissance de la pression de précharge exacte. En pratique, la
    membrane se dégrade en même temps que la précharge se perd — une recharge
    sur une membrane percée est inutile. Compte tenu du coût modéré d'un
    accumulateur neuf d'équipementier (20 à 80 euros selon l'application), le
    remplacement est généralement plus économique et plus fiable que la
    tentative de recharge. Quel liquide hydraulique utiliser après remplacement
    de l'accumulateur ? Le type de liquide dépend strictement du système. Les
    circuits Citroën/Peugeot à technologie hydraulique LHM/LDS utilisent un
    liquide hydraulique minéral (LHM, vert, ou LDS selon les générations). Les
    circuits de freinage ABS/ESP classiques (Volkswagen, Renault, Toyota, Ford,
    BMW, etc.) utilisent du liquide de frein synthétique DOT 4 ou DOT 5.1. Ces
    deux familles sont totalement incompatibles : une contamination croisée
    détruit les joints en caoutchouc en quelques heures et nécessite un rinçage
    complet du circuit avec remplacement de tous les composants à joints. Lire
    l'étiquette sur le réservoir hydraulique avant de compléter. L'accumulateur
    de pression peut-il être à l'origine d'un refus au contrôle technique ?
    Directement, non — il n'existe pas de test spécifique à l'accumulateur au
    contrôle technique. Cependant, les défaillances induites peuvent être
    sanctionnées : efficacité de freinage insuffisante (si l'accumulateur est à
    plat et que l'assistance est réduite), voyant de pression hydraulique allumé
    (point de contrôle obligatoire), ou bruits anormaux liés à la pompe. Sur les
    véhicules Citroën avec suspension hydraulique, une hauteur de caisse
    incorrecte ou une suspension qui s'affaisse peut également générer une
    contre-visite.
---

# Accumulateur de pression - Guide Diagnostic

## Fonction et Role

Stocker la pression hydraulique pour assister le freinage et maintenir la pression dans le circuit.

## Symptomes de Defaillance

- Pedale de frein dure et difficile a enfoncer
- Pompe hydraulique qui tourne en continu
- Freinage assiste defaillant apres quelques coups de frein
- Voyant de frein allume
- Bruit de claquement dans le circuit

## Pieces Associees

- pompe-hydraulique-systeme-de-freinage
- maitre-cylindre-de-frein
- agregat-de-freinage
- flexible-de-frein

## FAQ

**Comment tester l'accumulateur de pression ?**
Moteur eteint, appuyer 10 fois sur la pedale de frein. Si elle devient dure des le 3eme appui, l'accumulateur est HS.

**Peut-on rouler avec un accumulateur defaillant ?**
Oui mais le freinage sera moins assiste. Intervention a prevoir rapidement pour la securite.

**Accumulateur OE ou adaptable ?**
Privilegier l'OE car la pression de service doit correspondre exactement aux specifications constructeur.

**Combien coute un accumulateur de pression ?**
Entre 80 et 400 EUR selon le vehicule. Les systemes Citroen hydractive sont plus couteux.

**Quelle erreur eviter ?**
Ne jamais ouvrir un accumulateur (gaz sous pression). Toujours purger le circuit de frein apres remplacement.

## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Verifier si la pedale devient dure apres 3-4 freinages moteur eteint. Duree de vie 80000 a 150000 km.
