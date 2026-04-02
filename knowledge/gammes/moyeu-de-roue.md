---
category: direction
slug: moyeu-de-roue
title: Moyeu de roue
pg_id: 653
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
  role: Supporter la roue et transmettre la rotation - Fixe la roue au roulement
  must_be_true:
  - supporter
  - fixer
  - transmettre
  must_not_contain:
  - direction
  - cremailliere
  - volant
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - cremailliere-de-direction
  - rotule-de-direction
  - pompe-de-direction-assistee
  - barre-de-direction
  - soufflet-de-direction
  - colonne-de-direction
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
  - ❌ "securite garantie"
  cost_range:
    min: 200
    max: 600
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    price_range: Prix élevé — justifié par les certifications de sécurité
  - tier: Équivalent OE (OES)
    price_range: Prix intermédiaire — recommandé pour les applications courantes
  - tier: Aftermarket standard
    price_range: Prix bas — vigilance accrue sur les certifications sécurité
  brands:
    premium:
    - Lemforder
    - TRW
    standard:
    - Febi
    - Meyle
    - MOOG
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Jeu anormal de la roue
    severity: confort
  - id: S2
    label: Vibrations a vitesse constante
    severity: confort
  - id: S3
    label: Bruits sourds en roulant
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - verifier equilibrage et fixations
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'vibrations anormales : verifier equilibrage et fixations'
  quick_checks:
  - 'Observer : jeu anormal de la roue ?'
  - Vibrations a vitesse constante ?
  - Bruits sourds en roulant ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Jeu anormal de la roue
  - Vibrations a vitesse constante
  - Bruits sourds en roulant
  good_practices:
  - Controle du jeu de direction a chaque revision
  - Verifier les soufflets de protection (pas de fuite de graisse)
  - Faire verifier la geometrie apres remplacement
  - Inspecter les biellettes et rotules associees
rendering:
  pgId: '653'
  intro_title: A quoi sert Moyeu de roue ?
  risk_title: Pourquoi remplacer Moyeu de roue a temps ?
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
  - question: Comment choisir Moyeu de roue compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Moyeu de roue ?
    answer: En cas de jeu anormal de la roue ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Moyeu de roue sans verification atelier ?
    answer: Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure
      constructeur.
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
doc_id: 410e21f6-db4d-5ed2-9f60-136bbcc39025
content_hash: sha256:e51d4e7adca4cae1
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
  area: Sous le vehicule, relie le volant aux roues
  access: Par le dessous (pont elevateur recommande)
  adjacent_parts:
  - cremailliere
  - biellette
  - rotule
  - soufflet
installation:
  difficulty: difficile
  time: 1h a 3h
  tools:
  - cle a douille
  - arrache-rotule
  - cle dynamometrique
  prerequisite: Pont elevateur, geometrie a refaire apres
phase5_enrichment:
  _source: ate-freinage.fr + bremboparts.com + delphiautoparts.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 6
  _has_tech_data: true
  types_variants:
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_0_050_mm: '0,050 mm'
    val_0_10_mm: '0,10 mm'
    val_0_12_mm: '0,12 mm'
    val_0_15_mm: '0,15 mm'
    val_10__v: '10. V'
    val_2_a: '2 a'
    val_200_km: '200 km'
    val_300_km: '300 km'
    val_5_mm: '5 mm'
    val_7_a: '7 a'
    val_8_a: '8 a'
    val_86_a: '86 a'
    val_98__: '98 %'
    val_98_61__: '98,61 %'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le moyeu de roue est la pièce structurelle centrale qui supporte la roue et
    assure la liaison entre celle-ci et le roulement de roue. Il remplit trois
    fonctions simultanées : supporter le poids du véhicule qui s'exerce sur la
    roue, fixer la roue par l'intermédiaire de ses goujons filetés et de ses
    écrous de roue, et transmettre la rotation depuis l'arbre de transmission
    (sur les essieux moteurs) jusqu'à la roue. Le moyeu est monté sur le
    roulement de roue, qui lui permet de tourner librement par rapport au porte-
    fusée. Sur les essieux moteurs, le moyeu présente un alésage cannelé central
    dans lequel s'engage la tête de l'arbre de transmission. Sur les essieux non
    moteurs (essieu arrière de véhicules à traction), le moyeu est simplement
    monté sur le roulement sans entraînement en rotation propre. En complément
    de ces fonctions dynamiques, le moyeu supporte également le disque de frein
    (fixé sur la face avant du moyeu par des vis de centrage) et fournit la
    piste de mesure pour le capteur ABS (via une couronne dentée intégrée ou
    rapportée). Un moyeu fissuré, oxydé ou présentant un jeu excessif compromet
    la stabilité directionnelle du véhicule et peut provoquer un déjantage en
    cas de rupture.
  S2: >-
    Le moyeu de roue est une pièce de sécurité primaire. Ses symptômes de
    défaillance doivent être pris au sérieux et traités rapidement, car un moyeu
    défaillant peut compromettre la tenue de route et le freinage du véhicule. -
    Jeu anormal de la roue : en soulevant le véhicule sur chandelles, agiter la
    roue dans le plan transversal (2h-8h ou midi-18h). Un mouvement perceptible,
    même faible, signale une usure du roulement solidaire du moyeu ou du moyeu
    lui-même. - Vibrations à vitesse constante : des vibrations ressenties dans
    le volant, le plancher ou le siège à des vitesses comprises entre 80 et 130
    km/h peuvent provenir d'un moyeu déformé, fissuré ou dont le roulement
    intégré est détérioré. - Bruits sourds en roulant : un roulement de roue usé
    intégré au moyeu produit un bruit sourd ou ronronnant qui s'amplifie avec la
    vitesse. Ce bruit peut s'atténuer lors des changements de direction
    (transfert de charge). - Bruit différent lors des virages : si le bruit
    augmente lors d'un virage à gauche (charge transférée sur la roue droite),
    le roulement droit est suspect, et inversement pour un bruit amplifié en
    virage à droite. - Dysfonctionnement de l'ABS : un moyeu fissuré ou déformé
    peut désaligner la couronne dentée du capteur ABS, provoquant des alertes
    ABS erratiques ou un déclenchement intempestif du système lors du freinage.
    - Résistance à la rotation de la roue : en soulevant le véhicule, une roue
    qui offre une résistance anormale à la rotation à la main peut signaler un
    roulement intégré au moyeu grippé.
  S3: >-
    Le moyeu de roue est une pièce de sécurité dont les dimensions et la
    géométrie doivent correspondre exactement au véhicule. Un moyeu incompatible
    peut rendre le montage impossible ou générer des jeux dangereux. - Marque,
    modèle et année du véhicule : paramètres fondamentaux pour identifier la
    référence exacte. Un même modèle peut avoir été produit avec des
    configurations de moyeu différentes selon les options (4x4 ou traction,
    frein à disque ou tambour). - Essieu avant ou arrière : les moyeux avant et
    arrière sont distincts. Sur les essieux avant moteurs, le moyeu dispose d'un
    alésage cannelé pour l'arbre de transmission. À l'arrière des véhicules à
    traction, le moyeu est souvent plein (sans cannelure). - Configuration de
    freinage : disque ou tambour. Les moyeux pour freins à disque ont une face
    plane servant d'appui au disque, ceux pour tambour ont une forme différente
    adaptée au montage du tambour. - Présence d'un anneau ABS intégré : les
    véhicules équipés d'ABS nécessitent un moyeu avec une couronne phonique
    (dentée) intégrée ou compatible avec le capteur ABS existant. Vérifier cette
    caractéristique lors de la commande. - Entraxe et diamètre de centrage : ces
    dimensions sont fixes pour un modèle donné, mais il est prudent de les
    vérifier en cas de doute (notamment lors d'un changement de génération de
    véhicule). - Qualité des roulements intégrés : sur les moyeux à roulement
    intégré (Hub Unit), la qualité du roulement est déterminante pour la durée
    de vie. Préférer les équipementiers reconnus (SKF, FAG, Timken, NTN) pour un
    moyeu avec roulement intégré. - Vérifier simultanément l'état du disque de
    frein : lors d'un remplacement de moyeu, inspecter systématiquement le
    disque de frein associé. Les deux pièces travaillent en liaison directe et
    leur remplacement simultané optimise la durée de vie du montage. Pour aller
    plus loin : consultez notre guide d'achat moyeu de roue — comparatif
    marques, critères de choix et prix.
  S4_DEPOSE: >-
    Le remplacement du moyeu de roue est une intervention de carrosserie
    mécanique qui nécessite de l'outillage spécifique, notamment un extracteur
    de moyeu et une douille de grand diamètre pour l'écrou de moyeu (type Torx
    ou hexagonal selon le véhicule). Prévoir également une presse d'atelier pour
    séparer et remonter les roulements si ceux-ci ne sont pas intégrés au moyeu.
    - Soulever et sécuriser le véhicule : utiliser un cric et deux chandelles
    robustes sous les points d'appui carrosserie. Ne jamais travailler sous un
    véhicule uniquement maintenu par un cric hydraulique. - Déposer la roue :
    dévisser les 4 ou 5 écrous de roue et retirer la roue. Conserver les écrous
    en lieu sûr. - Desserrer l'écrou de moyeu : avant de déposer l'étrier de
    frein, desserrer l'écrou central du moyeu (souvent entre 200 et 300 Nm,
    parfois freiné à la matière). Utiliser la douille adaptée et un
    démultiplicateur de couple. - Déposer l'étrier de frein et le disque :
    retirer les 2 vis de l'étrier, le suspendre sans étirer le flexible de
    frein, puis dévisser les vis de centrage du disque et extraire le disque. -
    Débrancher le câble de capteur ABS : déconnecter soigneusement le capteur
    ABS de son support avant de tirer sur le moyeu, pour ne pas endommager le
    câble. - Déposer les fixations du porte-fusée : sur les essieux à triangle,
    dévisser les axes de rotule de direction et de rotule de triangle pour
    libérer le porte-fusée autour du moyeu. - Extraire le moyeu : utiliser un
    extracteur de moyeu pour dégager l'arbre de transmission du cannelage
    central. Frapper légèrement sur l'extracteur si nécessaire, sans choquer
    l'arbre de transmission. - Monter le nouveau moyeu : positionner le nouveau
    moyeu, engager l'arbre de transmission dans le cannelage et monter l'écrou
    neuf (toujours remplacer l'écrou de moyeu, il est souvent à usage unique). -
    Serrer l'écrou de moyeu au couple constructeur : respecter impérativement le
    couple de serrage spécifié (typiquement 200 à 320 Nm selon le véhicule),
    puis freiner à la matière si requis. - Reposer le disque, l'étrier, le
    capteur ABS et la roue : remonter dans l'ordre inverse, serrer les écrous de
    roue au couple constructeur (généralement 110 à 130 Nm).
  S4_REPOSE: >-
    La repose du moyeu de roue exige une attention particulière sur les couples
    de serrage et le respect des procédures constructeur. Il s'agit d'un
    composant de sécurité active : une erreur de montage peut provoquer la perte
    de contrôle du véhicule à haute vitesse. - Serrer l'écrou de moyeu au couple
    constructeur avec frein à la matière : l'écrou de moyeu est une pièce à
    usage unique sur la majorité des véhicules modernes (écrou auto-freinant ou
    écrou à freiner après serrage). Utiliser une clé dynamométrique calibrée et
    respecter impérativement le couple constructeur (typiquement entre 200 et
    320 Nm selon le modèle). Après serrage, réaliser le frein à la matière en
    déformant la collerette de l'écrou dans l'encoche de l'arbre. Ne jamais
    réutiliser un écrou de moyeu déjà freiné. - Vérifier l'engagement du capteur
    ABS dans son logement : reconnecter le câble du capteur ABS et s'assurer que
    le capteur est correctement positionné dans son siège sur le porte-fusée. Un
    capteur ABS mal positionné génère un signal de vitesse de roue absent ou
    erratique, déclenchant le voyant ABS et mettant le système en mode dégradé.
    Vérifier l'entrefer capteur-couronne phonique selon les spécifications
    constructeur si applicable. - Remonter le disque de frein et l'étrier au
    couple : repositionner le disque de frein centré sur le moyeu, visser les
    vis de centrage (généralement 8 à 12 Nm). Remonter l'étrier de frein et
    serrer les deux vis d'étrier au couple constructeur (généralement 30 à 60 Nm
    selon le modèle). Vérifier que le flexible de frein n'est ni vrillé ni tendu
    après remplacement du moyeu. - Remonter la roue et serrer les écrous au
    couple : poser la roue, visser les écrous à la main dans un ordre en étoile,
    puis serrer au couple avec la roue au sol (généralement entre 110 et 130
    Nm). Ne jamais serrer avec la roue en l'air — le couple appliqué ne serre
    que l'axe, pas la roue. - Test de jeu de roue au sol avant premier roulage :
    avec le véhicule posé au sol, saisir la roue à 3 heures et 9 heures (jeu
    horizontal) puis à 12 heures et 6 heures (jeu vertical). L'absence totale de
    jeu perceptible confirme le bon montage du moyeu. Un jeu résiduel horizontal
    indique un problème de roulement ou une rotule de direction défaillante ; un
    jeu vertical indique un problème de triangle de suspension ou de rotule de
    triangle. - Test roulant progressif avec attention aux vibrations :
    effectuer un test roulant progressif : 30 km/h, 50 km/h, 80 km/h, 120 km/h.
    Observer l'absence de vibration de volant ou de véhicule à chaque palier.
    Des vibrations dès 60 km/h peuvent indiquer un balourd de la roue (à
    équilibrer) ou un moyeu mal centré. Des vibrations progressives avec la
    vitesse signalent généralement un défaut d'équilibrage. - Contrôle du voyant
    ABS et vérification des codes de défaut : après le test roulant, vérifier
    que le voyant ABS est éteint et que le voyant de frein reste éteint.
    Connecter un outil OBD pour confirmer l'absence de codes liés aux capteurs
    de vitesse de roue. Un code de capteur ABS persistant après remplacement du
    moyeu signale une incompatibilité de capteur ou un écart d'entrefer à
    corriger.
  S5: >-
    Le remplacement du moyeu de roue est une intervention sur un organe de
    sécurité. Certaines erreurs, même commises de bonne foi, peuvent
    compromettre la sécurité du véhicule et de ses occupants. - Réutiliser
    l'ancien écrou de moyeu : l'écrou de moyeu est souvent un écrou à
    déformation plastique (auto-freiné à la matière), conçu pour un usage
    unique. Réutiliser un écrou déjà serré ne garantit pas le maintien du couple
    de serrage, ce qui peut entraîner un desserrement progressif du moyeu en
    roulage. - Ne pas serrer l'écrou au couple constructeur : un couple
    insuffisant laisse un jeu axial sur le moyeu qui accélérera la destruction
    du roulement. Un couple excessif peut fracturer le moyeu ou endommager le
    roulement. Un couple-mètre est obligatoire pour cette intervention. -
    Confondre les côtés gauche et droit : les moyeux gauche et droit ne sont pas
    interchangeables sur de nombreux véhicules. L'orientation de l'anneau ABS et
    la position des fixations de l'étrier imposent un moyeu spécifique à chaque
    côté. Toujours vérifier la référence côté lors de la commande. - Négliger de
    contrôler l'état du roulement sur un moyeu sans roulement intégré : lors
    d'un remplacement de moyeu nu (sans roulement intégré), le roulement doit
    être systématiquement inspecté et remplacé si nécessaire. Monter un moyeu
    neuf sur un roulement usé conduit à une défaillance prématurée. - Endommager
    le capteur ABS lors de la dépose : le câble du capteur ABS est fragile et le
    capteur lui-même peut se bloquer dans son logement par l'oxydation. Forcer
    sans désoxyder provoque une rupture du capteur ou de son câble, ajoutant une
    réparation supplémentaire non prévue.
  S6: >-
    Après remplacement du moyeu de roue, la validation du montage doit être
    méthodique. Un contrôle insuffisant sur cet organe de sécurité peut avoir
    des conséquences graves en roulage. - Contrôle du jeu de roue à la main :
    avec le véhicule sur chandelles, agiter chaque roue remplacée en tous sens.
    Aucun jeu perceptible ne doit être détecté, confirmant le serrage correct de
    l'écrou de moyeu et l'absence de jeu dans le nouveau roulement. - Rotation
    libre de la roue : faire tourner la roue à la main. Elle doit tourner
    librement et régulièrement sans résistance anormale ni points durs, signe
    que le nouveau moyeu et son roulement sont correctement montés. -
    Vérification du voyant ABS : démarrer le véhicule et vérifier que le voyant
    ABS ne s'allume pas. Si le voyant reste allumé, le capteur ABS est peut-être
    mal repositionné dans son logement ou son entrefond ne respecte pas les
    tolérances constructeur. - Test à basse vitesse dans un espace dégagé :
    effectuer un premier roulage à 20-30 km/h sur 500 m pour vérifier l'absence
    de bruit, de vibration ou de résistance anormale avant de reprendre une
    conduite normale. - Vérification du freinage : effectuer plusieurs freinages
    progressifs depuis 50 km/h pour confirmer l'absence de vibrations dans la
    pédale de frein et l'efficacité symétrique des deux côtés de l'essieu
    traité. - Contrôle visuel des fixations : vérifier que les vis de l'étrier,
    les écrous de roue et les axes de rotule sont correctement serrés et
    qu'aucun accessoire n'a été oublié lors du remontage.
  S7: >-
    Le moyeu de roue est un composant central du train roulant qui interagit
    avec plusieurs systèmes de sécurité. Lors de son remplacement, plusieurs
    pièces adjacentes méritent une inspection ou un remplacement simultané. -
    Roulement de roue — Sur de nombreux véhicules, le roulement est intégré au
    moyeu (cartouche de roulement non démontable). Dans ce cas, roulement et
    moyeu ne forment qu'une pièce. Sur les véhicules à roulement séparé,
    remplacer le roulement en même temps que le moyeu permet d'éviter une
    deuxième intervention à courte échéance : les deux pièces ont la même durée
    de vie et sont sollicitées identiquement. - Disque de frein — Lors de toute
    dépose de moyeu, le disque de frein est également retiré. C'est l'occasion
    d'évaluer son état (épaisseur résiduelle, voile, traces de pitting). Un
    disque dépassant la limite d'usure doit être remplacé pendant que le train
    roulant est démonté. - Capteur ABS de roue — Le capteur ABS est monté sur ou
    à proximité immédiate du moyeu. Un câble de capteur fissuré ou un capteur
    endommagé par la corrosion génère un voyant ABS et désactive le système.
    Inspecter le câble sur toute sa longueur lors du remplacement du moyeu. -
    Écrou de moyeu — L'écrou de moyeu est à usage unique sur la quasi-totalité
    des véhicules modernes. Prévoir un écrou neuf lors de toute commande de
    moyeu — le réutiliser constitue un risque de sécurité, l'écrou usagé pouvant
    se desserrer spontanément en roulage. - Rotule de direction — Si le porte-
    fusée a été déposé pour accéder au moyeu, vérifier l'état des rotules de
    direction et de triangle. Des rotules présentant un jeu ou un claquement
    doivent être remplacées pendant que la suspension est démontée.
  S8: >-
    Comment distinguer une usure de roulement d'une usure de moyeu ? Les deux
    composants produisent des symptômes similaires (bruit sourd, vibrations, jeu
    de roue). La distinction se fait par l'inspection directe lors de la dépose.
    Un roulement usé présente des billes ou des pistes marquées (pitting),
    tandis qu'un moyeu défaillant peut présenter des fissures visibles, une
    déformation de la bride de fixation des goujons ou une usure du cannelage
    central. Sur les moyeux à roulement intégré (Hub Unit), les deux composants
    forment un seul ensemble et sont remplacés simultanément. Peut-on rouler
    avec un léger jeu sur le moyeu de roue ? Non. Tout jeu mesurable sur un
    moyeu de roue doit être traité sans délai. Un jeu même faible s'aggrave
    rapidement avec la distance parcourue, exerce des contraintes anormales sur
    les fixations de roue et peut provoquer une rupture du moyeu ou du roulement
    en roulage. Sur les véhicules équipés d'ABS, un jeu de moyeu génère des
    signaux erratiques du capteur, pouvant désactiver le système de freinage
    d'urgence. La pièce gauche et droite sont-elles interchangeables ? Dans la
    majorité des cas, non. Même si les dimensions extérieures paraissent
    identiques, l'orientation de la couronne ABS, la position du logement de
    capteur ou les points d'ancrage des triangles de suspension diffèrent entre
    côté gauche et côté droit sur de nombreux modèles. Toujours vérifier la
    référence spécifique au côté lors de la commande. Faut-il obligatoirement
    remplacer le disque de frein lors d'un changement de moyeu ? Ce n'est pas
    systématiquement obligatoire, mais fortement recommandé si le disque
    présente une épaisseur inférieure au seuil minimum constructeur ou des
    traces de chauffe localisées. Le remplacement du moyeu implique une dépose
    complète du disque, ce qui représente l'occasion idéale pour inspecter et
    remplacer le disque si son état le justifie, sans coût de main-d'oeuvre
    supplémentaire.
  META: >-
    {"meta_title":"Moyeu de roue : jeu, vibrations et remplacement |
    AutoMecanik","meta_description":"Jeu anormal de la roue, vibrations à
    vitesse constante, bruits sourds en roulant : reconnaître un moyeu de roue
    usé et agir avant la casse du roulement.","og_title":"Moyeu de roue
    défaillant : jeu de roue et bruits sourds","og_description":"Bruit sourd en
    roulant ou roue qui vibre à vitesse constante ? Un moyeu de roue usé met la
    sécurité en jeu. Guide de diagnostic et
    remplacement.","sources":[{"type":"rag","ref":"gammes/moyeu-de-
    roue.md","field":"diagnostic.symptoms,domain.role,rendering.faq"}]}
---

# Moyeu de roue - Guide Diagnostic Complet

## Fonction et Rôle

Supporter la roue et transmettre la rotation - Fixe la roue au roulement

**Actions principales:** supporter, fixer, transmettre, recevoir la roue

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- jeu anormal de la roue
- vibrations a vitesse constante
- bruits sourds en roulant

## Procédure de Diagnostic

Pour diagnostiquer un problème de moyeu de roue:

1. **Inspection visuelle** - Examiner l'état du moyeu de roue
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

- roulement-de-roue
- disque-de-frein

## Critères de Compatibilité

Pour commander le bon moyeu de roue, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"

## FAQ

**Comment choisir Moyeu de roue compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Moyeu de roue ?**
En cas de jeu anormal de la roue ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Moyeu de roue sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
