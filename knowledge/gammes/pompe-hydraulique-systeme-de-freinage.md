---
schema_version: '5.0'
category: freinage
slug: pompe-hydraulique-systeme-de-freinage
title: Pompe hydraulique système de freinage
pg_id: 1115
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-29'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: skill:phase5-vague6
  last_enriched_at: '2026-03-29'
domain:
  role: >-
    La pompe hydraulique du systeme de freinage (bloc ABS/ESP) est le coeur du systeme de stabilite electronique. Elle gere l''ABS, ASR, EBV et ESP en agissant sur les freins independamment sur chaque roue.
  must_be_true: []
  must_not_contain: []
  related_parts: []
phase5_enrichment:
  _source: contenu LLM — a revalider contre sources OEM
  _validation_status: pending_oem_validation
  _enriched_at: '2026-03-30'
  technical_notes:
    role: 'bloc hydraulique ABS/ESP — pompe de retour pour moduler la pression par roue'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    L'ESP pour Electronic Stability Program est un équipement de sécurité
    automobile. L'ESP permet de corriger la trajectoire en agissant sur le
    système de freinage et sur le couple moteur. Ce système de sécurité comprend
    multiples capteurs situés dans les 4 roues du véhicule qui contrôlent la
    trajectoire 25 fois par seconde. Unité de commande intégrée électronique
    avec le bloc hydraulique, il gère l'ESP, ASR, EBV, ABS, etc... C'est bien
    sûr le cœur du système. Il est chargé, en fonction des signaux reçus des
    différents capteurs, agissant sur les freins.
  S2: >-
    La pompe hydraulique de freinage (aussi appelée groupe hydraulique,
    motopompe de freinage ou pompe ABS/ESP selon les systèmes) génère et
    maintient la pression haute dans le circuit de freinage assisté. Sur les
    véhicules Citroën/Peugeot à technologie hydraulique LHM/LDS, elle alimente
    simultanément le freinage et la suspension. Une pompe défaillante compromet
    directement la sécurité de freinage — son diagnostic doit être rapide. -
    Pompe qui tourne en permanence sans s'arrêter : signe le plus fréquent d'une
    anomalie. Une pompe hydraulique saine tourne 5 à 30 secondes pour charger
    l'accumulateur, puis s'arrête automatiquement. Si elle tourne en continu,
    l'accumulateur de pression est épuisé dans 80 % des cas. Remplacer d'abord
    l'accumulateur : si la pompe continue de tourner avec un accumulateur neuf,
    la pompe est défaillante. - Pédale de frein dure ou sans assistance : une
    pression hydraulique insuffisante dans le circuit produit une pédale qui ne
    s'enfonce pas naturellement et nécessite un effort musculaire excessif. Ce
    symptôme peut aussi indiquer un servofrein défaillant — distinguer les deux
    en vérifiant si le voyant de pression hydraulique s'allume simultanément. -
    Voyant de pression hydraulique allumé de façon permanente : sur les tableaux
    de bord Citroën/Peugeot hydrauliques, ce voyant (rouge, pression
    hydraulique) s'allume quand le circuit est sous la pression minimale de
    sécurité. Après vérification du niveau de liquide et remplacement de
    l'accumulateur, s'il reste allumé, la pompe est défaillante. - Fuite
    hydraulique visible sous le véhicule : une flaque de liquide vert (LHM) ou
    brun/incolore (DOT) sous le groupe hydraulique indique une fuite sur les
    joints de pompe. La pompe doit être déposée pour inspection et remplacement
    des joints ou de l'ensemble. - Bruit de pompe anormal : claquement,
    grincement ou sifflement lors du fonctionnement de la pompe indiquent une
    usure mécanique interne (roulements, pistons, clapets). Une pompe saine est
    silencieuse en dehors d'un léger bourdonnement lors des phases de
    chargement. - Codes défauts OBD persistants liés à la pression de freinage :
    après remplacement de l'accumulateur, des codes C-xxxx liés à la pression du
    circuit de freinage ou à l'alimentation de la pompe qui persistent indiquent
    une pompe hors service. La lecture OBD via un outil multimarque permet de
    confirmer avant dépose. Il n'existe pas d'intervalle kilométrique fixe pour
    la pompe hydraulique. Sa durée de vie dépend du nombre de cycles pompe/arrêt
    cumulés au fil des années. Une pompe bien entretenue (niveau de liquide
    correct, accumulateur remplacé à temps) peut dépasser 200 000 km.
  S3: >-
    Deux grands systèmes se différenciés dans la manière de produire la pression
    par la pompe hydraulique de l'ABS. - Bosch : la pompe hydraulique
    indépendante de l'unité hydraulique de l'ABS.- Continental Teves : Tout est
    formé d'un seul bloc. Elle fournit pour l'ABS, EDS, ASR, ESP. Il faut
    toujours faire un contrôle permanant pour tous les composants de freinage
    pour ne pas avoir des problèmes de freinage lorsque le véhicule est sur la
    route.
  S4_DEPOSE: >-
    Intervention sur circuit haute pression (150 à 200 bar). Dépressurisation
    complète obligatoire avant toute ouverture du circuit. Le liquide
    hydraulique sous pression projette à grande vitesse et les liquides LHM ou
    DOT sont nocifs au contact des muqueuses et des yeux. - Dépressuriser le
    circuit hydraulique : couper le contact. Appuyer sur la pédale de frein à
    fond 25 à 30 fois consécutives, contact coupé, jusqu'à ce que la pédale
    devienne dure et résistante. Sur les systèmes Citroën avec suspension
    hydraulique, baisser également la suspension manuellement si possible pour
    décharger les sphères. Attendre 5 minutes supplémentaires. - Déconnecter la
    batterie : borne négative en premier. Cette précaution évite tout démarrage
    intempestif du moteur électrique de la pompe pendant l'intervention et
    protège les calculateurs des surtensions lors de la reconnexion des
    connecteurs électriques. - Placer des protections sous la pompe : disposer
    plusieurs chiffons absorbants larges et un bac de récupération sous
    l'ensemble hydraulique. Le liquide LHM (vert) est nocif pour les peintures
    carrosserie et les surfaces caoutchouc environnantes. Protéger les zones
    sensibles avec des bâches plastiques. - Repérer et débrancher les
    connecteurs électriques : photographier ou noter la position de chaque
    connecteur avant débranchement (alimentation moteur pompe, capteurs de
    pression, electrovanne de régulation). Les connecteurs sont parfois
    identiques en apparence mais ne sont pas interchangeables. - Déposer les
    raccords hydrauliques haute pression : utiliser des clés plates adaptées
    (doubles) pour dévisser chaque raccord sans tordre les tuyauteries. Obturer
    immédiatement chaque orifice ouvert avec des bouchons plastiques propres
    pour éviter toute introduction de poussières ou d'humidité dans le circuit
    hydraulique. - Déposer les vis ou boulons de fixation de la pompe : la pompe
    est généralement fixée sur un support ou sur le bloc moteur par 3 à 4 vis
    (M8 ou M10 selon le modèle). Accéder à toutes les vis avant de commencer à
    desserrer pour éviter que la pompe ne bascule lors du dernier boulon. -
    Inspecter le support et les tuyauteries avant repose : contrôler l'état des
    tuyaux haute pression (aucune fissure, aucune déformation), des raccords et
    du support de fixation. Un tuyau endommagé doit être remplacé en même temps
    pour éviter une seconde intervention immédiate. - Poser la nouvelle pompe :
    fixer la pompe sur son support, serrer les vis au couple constructeur
    (généralement 20 à 40 N.m selon le modèle). Rebrancher les raccords
    hydrauliques en commençant par ceux de plus grande section. Serrer aux
    couples indiqués dans la documentation technique. - Purger le circuit et
    remettre en service : remplir le réservoir de liquide hydraulique jusqu'au
    repère MAX. Rebrancher la batterie. Démarrer et laisser tourner la pompe
    pendant 2 à 3 minutes pour amorcer le circuit. Vérifier le niveau de liquide
    après pompage — il peut baisser de 10 à 20 % lors de la purge. Compléter si
    nécessaire.
  S5: >-
    - Remplacer la pompe sans avoir d'abord vérifié l'accumulateur : dans 80 %
    des cas de pompe qui tourne en permanence, l'accumulateur de pression est la
    cause primaire. Un accumulateur épuisé sur-sollicite la pompe jusqu'à
    l'usure. Remplacer la pompe sans changer simultanément l'accumulateur
    condamne la pièce neuve aux mêmes cycles excessifs. Toujours remplacer les
    deux en même temps ou tester l'accumulateur au préalable. - Ouvrir le
    circuit sans dépressurisation complète : une pression résiduelle de 150 à
    200 bar dans le circuit hydraulique projette du liquide à très grande
    vitesse lors de l'ouverture d'un raccord. Une projection dans l'œil ou sur
    la peau à haute pression peut causer des blessures graves nécessitant une
    intervention médicale. Les 25 à 30 appuis pédale contact coupé sont non
    négociables. - Mélanger LHM et liquide DOT : les deux types de liquide
    hydraulique sont absolument incompatibles. Le LHM (minéral, vert) est à base
    d'huile minérale. Le DOT (synthétique) est à base de glycol. La moindre
    contamination croisée détruit les joints en caoutchouc du circuit en
    quelques heures et nécessite le rinçage complet du circuit et le
    remplacement de tous les composants à joints. Identifier le type de liquide
    sur l'étiquette du réservoir avant toute intervention. - Démarrer la pompe à
    sec après remplacement : une pompe hydraulique démarrée sans liquide dans le
    circuit se détruit en quelques secondes. Après repose, toujours remplir le
    réservoir au niveau MAX et s'assurer que les raccords sont serrés avant de
    mettre le contact. Laisser amorcer sans accélérer. - Négliger la purge du
    circuit : de l'air introduit dans les tuyauteries haute pression pendant
    l'ouverture des raccords provoque une assistance irrégulière, des coups de
    bélier hydrauliques et une cavitation de la pompe. Une purge complète du
    circuit (mise en pression, purge des freins si nécessaire) est systématique.
    - Omettre le contrôle des tuyauteries avant repose : une tuyauterie haute
    pression fissurée ou dont le raccord est corrodé peut lâcher sous la
    pression quelques jours après l'intervention. Inspecter chaque tuyau et
    chaque raccord avant de refermer le capot.
  S6: >-
    - Comportement de la pompe au démarrage : démarrer le moteur et chronométrer
    la durée de fonctionnement de la pompe. Sur un circuit hydraulique sain avec
    accumulateur neuf, la pompe doit tourner entre 10 et 30 secondes pour
    atteindre la pression nominale du circuit, puis s'arrêter. Un fonctionnement
    continu au-delà de 60 secondes après démarrage indique une fuite hydraulique
    ou un accumulateur de mauvaise précharge. - Test de l'assistance au freinage
    : couper le contact immédiatement après le démarrage, puis appuyer sur la
    pédale 10 fois à fond. Les 8 à 10 premiers appuis doivent rencontrer une
    résistance assistée souple. La pédale doit durcir progressivement à partir
    du 10e appui. Une pédale immédiatement dure dès le premier appui ou un
    durcissement avant le 5e appui indique une pression de circuit insuffisante.
    - Contrôle d'étanchéité de tous les raccords : passer une lingette propre
    sur chaque raccord hydraulique reconstruit pendant l'intervention après 5
    minutes de fonctionnement moteur. Inspecter à nouveau après 15 minutes de
    fonctionnement à chaud. Une trace de liquide LHM (vert) ou DOT impose un
    reserrage immédiat ou un remplacement du joint. - Niveau de liquide
    hydraulique : vérifier le niveau dans le réservoir après la purge initiale.
    Le niveau peut baisser légèrement pendant les premiers cycles de chargement.
    Compléter jusqu'au repère MAX avec le liquide correct (LHM sur les systèmes
    Citroën/Peugeot hydrauliques, DOT 4 ou 5.1 sur les autres). - Lecture OBD
    post-intervention : connecter un scanner OBD et effacer les codes défauts
    résiduels. Sur les véhicules avec ABS/ESP, vérifier que le calculateur ne
    signale pas d'erreur de pression ou d'alimentation liée à la pompe. Sur
    certains modèles (Peugeot 407, Citroën C5), une initialisation de la pompe
    via l'outil de diagnostic constructeur est nécessaire. - Essai routier avec
    freinages successifs : effectuer 10 freinages francs à 50 km/h sur une route
    dégagée. L'assistance doit être présente et régulière du premier au dixième
    freinage. Sur les Citroën/Peugeot hydrauliques, vérifier également que la
    suspension maintient la hauteur de caisse sans affaissement ni oscillations
    anormales pendant les accélérations.
  S7: >-
    La pompe hydraulique de freinage opère en circuit fermé avec plusieurs
    composants hydrauliques interdépendants. Le remplacement d'une pompe est
    systématiquement l'occasion d'inspecter ou de remplacer les pièces qui
    subissent les mêmes contraintes de pression et de cycles. - Accumulateur de
    pression hydraulique — la pièce à remplacer systématiquement en même temps
    que la pompe. Un accumulateur épuisé force la pompe neuve à tourner en
    permanence et l'use prématurément. Si le budget ne permet pas de remplacer
    les deux en même temps, tester l'accumulateur en premier (test des appuis
    pédale contact coupé) pour s'assurer qu'il n'est pas la cause du
    remplacement de la pompe. - Agrégat de freinage ABS/ESP — sur les véhicules
    modernes, la pompe hydraulique et les électrovannes ABS sont intégrées dans
    un même bloc hydraulique. Si le boîtier du groupe présente des fissures, de
    la corrosion ou si les électrovannes sont défaillantes en même temps que la
    pompe, le remplacement du groupe complet est économiquement préférable à la
    réparation pièce par pièce. - Maître-cylindre de frein — si la pédale reste
    molle ou spongieuse malgré une pompe et un accumulateur neufs, le maître-
    cylindre est à examiner. Une fuite interne du maître-cylindre empêche la
    montée en pression du circuit hydraulique et simule une pompe défaillante. -
    Servofrein — sur les systèmes mixtes (assistance mécanique et hydraulique),
    le servofrein à dépression peut être à l'origine d'une pédale dure
    indépendamment de l'état de la pompe hydraulique. Un test au moteur froid
    (pédale qui s'enfonce lors du démarrage = servofrein sain) permet de
    distinguer les deux causes. - Liquide hydraulique LHM ou DOT — lors du
    remplacement de la pompe, vérifier la date du dernier remplacement du
    liquide hydraulique. Un liquide DOT vieilli absorbe l'humidité et fait
    chuter le point d'ébullition. Pour les circuits LHM, vérifier l'absence de
    contamination par du DOT ou de coloration anormale du liquide.
  S8: >-
    La pompe hydraulique tourne en permanence : dois-je changer la pompe ou
    l'accumulateur ? Dans 80 % des cas, c'est l'accumulateur de pression qui est
    épuisé, pas la pompe. Avant de commander la pompe (pièce plus coûteuse et
    plus longue à poser), réaliser le test suivant : couper le contact et
    appuyer sur la pédale de frein à fond 10 fois. Si la pédale devient dure en
    moins de 3 appuis avec un accumulateur neuf, la pompe est défaillante. Si la
    pédale tient 10 appuis ou plus avec le même accumulateur, la pompe est
    saine. Commencer par remplacer l'accumulateur (10 à 80 euros selon le
    modèle) : dans la majorité des cas, le problème est résolu sans toucher à la
    pompe. Peut-on rouler avec une pompe hydraulique de freinage défaillante ?
    Non, en aucun cas. Sur les véhicules dont le freinage est entièrement
    assisté hydrauliquement (Citroën BX, Xantia, XM, C5, Peugeot 405, 406, 407,
    certains 607), une panne de pompe supprime totalement l'assistance. La
    pédale devient une pédale de ciment — le conducteur ne peut pas développer
    une force de freinage suffisante pour arrêter le véhicule dans des distances
    normales. Le véhicule ne doit pas circuler. Sur les véhicules avec double
    assistance (mécanique et hydraulique), une panne pompe réduit fortement mais
    ne supprime pas totalement l'assistance — la conduite est dangereuse mais
    physiquement possible sur courte distance jusqu'à l'atelier. Quel liquide
    hydraulique utiliser pour ce système ? Le type de liquide dépend du
    constructeur et du modèle. Les systèmes Citroën/Peugeot à technologie
    hydraulique (BX, Xantia, XM, C5, 406, 407, Xsara Picasso hydraulique)
    utilisent du LHM (Liquide Hydraulique Minéral, vert) ou du LDS (liquid
    destiné aux systèmes DCS/Hydractive) selon la génération. Ces liquides sont
    minéraux et incompatibles avec le DOT. Tous les autres systèmes ABS/ESP
    (Renault, Volkswagen, Ford, Toyota, BMW, etc.) utilisent du liquide de frein
    synthétique DOT 4 ou DOT 5.1. La mention du type de liquide figure sur
    l'étiquette collée sur le réservoir hydraulique. Ne jamais mélanger sous
    aucun prétexte. Faut-il programmer ou calibrer la pompe après remplacement ?
    Sur la grande majorité des véhicules, non. La pompe hydraulique est un
    composant électromécanique sans calibration spécifique. Toutefois, sur
    certains véhicules équipés de systèmes ABS/ESP évolués avec capteurs de
    pression intégrés (Citroën C5 II, Peugeot 407 avec suspension Hydractive
    3+), une procédure d'initialisation via l'outil de diagnostic constructeur
    ou un outil compatible (Diagbox pour Citroën/Peugeot) peut être nécessaire.
    Une lecture OBD après remplacement permet de détecter les codes résiduels et
    de confirmer que le calculateur reconnaît le bon fonctionnement de la pompe.
    La pompe hydraulique peut-elle être réparée (joints, rotor) plutôt que
    remplacée ? Techniquement oui sur certains modèles anciens où des kits de
    joints sont disponibles (Citroën BX, Xantia). En pratique, la réparation
    d'une pompe hydraulique haute pression nécessite un démontage en atelier
    spécialisé avec presse hydraulique et outillage de mesure. Le coût en main
    d'œuvre dépasse souvent le coût d'une pompe d'échange standard
    reconditionnée. Sur les véhicules récents (post-2000), les pièces de
    réparation ne sont plus disponibles et le remplacement de la pompe complète
    est la seule solution.
---

# Pompe hydraulique système de freinage

<!-- A enrichir : Phase 5 -->
