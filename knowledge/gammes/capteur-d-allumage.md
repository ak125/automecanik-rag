---
schema_version: '5.0'
category: allumage
slug: capteur-d-allumage
title: Capteur d''allumage
pg_id: 834
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
    Le capteur d''allumage determine les moments de commutation du module d''allumage. Il utilise un capteur a induction ou a effet de Hall pour transmettre la position du vilebrequin au systeme d''allumage.
  must_be_true: []
  must_not_contain: []
  related_parts: []
phase5_enrichment:
  _source: contenu LLM — a revalider contre sources OEM
  _validation_status: pending_oem_validation
  _enriched_at: '2026-03-30'
  technical_notes:
    role: 'determine le moment de commutation du module d''allumage (anciens moteurs)'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le fonctionnement du module d'allumage est assuré par la présence d'un
    capteur d'allumage qui lui détermine les moments de commutation. Ici entrent
    en actions les capteurs à induction ou capteurs à effet de Hall. Le capteur
    d'allumage fait partie du système d'allumage des anciens moteurs.Certains
    constructeurs abandonnent complètement l'utilisation du commutateur
    d'allumage en confiant cette fonction directement au contrôleur de moteur
    électronique. L'instant de l'allumage est déterminé par le module de
    l'allumage. La panne du module d'allumage peut &ecirc;tre la cause d'un
    fonctionnement irrégulier et m&ecirc;me d'une défaillance complète du
    système d'allumage. Dans ce cas il est recommandé d'effectuer une
    vérification précise de tout le système d'allumage.
  S2: >-
    Le capteur d'allumage (capteur de position vilebrequin ou arbre à cames
    selon l'application) n'a pas d'intervalle de remplacement préventif défini
    en km. Sa durée de vie typique se situe entre 150 000 et 300 000 km, mais la
    chaleur excessive, les vibrations et les projections d'huile accélèrent sa
    défaillance. Le remplacement s'impose dès l'apparition des symptômes
    suivants : - Voyant moteur allumé avec codes OBD P0335 à P0344 (capteur
    vilebrequin) ou P0340 à P0349 (capteur arbre à cames) : le calculateur a
    détecté une absence ou une irrégularité du signal. Diagnostic immédiat
    requis — ne pas attendre. - Démarrage difficile ou refus de démarrage : sans
    le signal de position du vilebrequin, le calculateur ne peut ni synchroniser
    l'injection ni déclencher l'allumage. Le moteur tourne au démarreur sans
    jamais partir. - Coupures moteur aléatoires en roulage, souvent après montée
    en température, avec reprise spontanée après refroidissement de 10 à 20
    minutes : signe caractéristique d'une défaillance thermique du capteur. -
    Calage au ralenti ou ralenti très instable avec oscillations supérieures à
    200 tr/min : le signal de position est irrégulier, la gestion du ralenti
    perd sa référence. - Perte de puissance marquée couplée à une consommation
    en hausse : l'avance à l'allumage est calculée sur une position
    approximative, dégradant le rendement de combustion. - Ratés de combustion
    (code P0300 à P030X) sans anomalie bougies ni bobines : un signal capteur
    bruité peut simuler des ratés alors que le circuit d'allumage est sain. Si
    le moteur cale uniquement à chaud et redémarre après refroidissement, tester
    impérativement la résistance du capteur inductif à chaud au multimètre : une
    résistance dépassant 2 000 ohms à chaud (contre 500 à 1 000 ohms à froid)
    confirme une défaillance thermique.
  S3: >-
    Le capteur d'allumage est une pièce de précision électronique dont un
    mauvais choix peut conduire à un non-démarrage immédiat ou à des
    dysfonctionnements intermittents difficiles à diagnostiquer. Voici les
    critères à respecter sans exception : - Identifier le type de capteur avant
    tout achat : deux familles coexistent sur les moteurs modernes. Le capteur à
    induction (magnétique) produit un signal sinusoïdal proportionnel à la
    vitesse de rotation — résistance mesurable au multimètre (200 à 1 000 ohms).
    Le capteur à effet Hall produit un signal carré alimenté par une tension de
    référence (5 V) — il ne se mesure pas au multimètre de la même façon. Ces
    deux types ne sont pas interchangeables, même si l'aspect physique semble
    similaire. - Référence OEM ou équivalent certifié : le capteur doit
    reproduire exactement le même nombre de dents détectées sur la couronne ou
    le disque de déclenchement, la même longueur d'entrefer (0,3 à 1,5 mm selon
    application), la même amplitude de signal de sortie et la même plage de
    température de fonctionnement (-40°C à +130°C minimum). - Résistance
    nominale (capteur inductif) : vérifier les valeurs dans la documentation
    technique du moteur. Des capteurs hors-spécification génèrent des impulsions
    de mauvaise amplitude que le calculateur ne reconnaît pas ou interprète de
    manière erratique. - Longueur de câble et type de connecteur : le câble doit
    atteindre le faisceau moteur sans tension ni coude serré. Les connecteurs
    sont véhicule-spécifiques ; un mauvais connecteur impose un adaptateur
    susceptible de s'oxyder et de générer des micro-coupures. - Compatibilité
    avec la couronne phonique : sur les moteurs avec roue phonique 60-2 ou 36-1
    dents, le capteur doit être étalonné pour ce nombre. Un capteur prévu pour
    une couronne différente génère des codes défauts dès le premier démarrage. -
    Marques avec certification OEM : Bosch, Delphi, Hella, Febi Bilstein, FAE
    proposent des capteurs fabriqués aux spécifications des équipementiers
    d'origine. Éviter les capteurs génériques sans référence technique
    vérifiable. En cas de doute entre capteur vilebrequin et capteur arbre à
    cames, lire les codes défauts OBD avant commande : P0335-P0338 =
    vilebrequin, P0340-P0349 = arbre à cames.
  S4_DEPOSE: >-
    La difficulté d'accès varie fortement selon l'emplacement du capteur : le
    capteur de vilebrequin se trouve généralement sur le carter inférieur au
    niveau du volant moteur ou de la couronne phonique, parfois dissimulé sous
    le turbo ou le cache moteur. Le capteur d'arbre à cames est positionné sur
    le cache-distribution ou la culasse. Comptez 30 minutes à 2 heures selon le
    véhicule. - Couper le contact et déconnecter la borne négative de la
    batterie : opération indispensable avant toute manipulation électronique. Un
    court-circuit sur le circuit du capteur peut endommager le calculateur
    moteur. - Localiser précisément le capteur à remplacer : identifier grâce au
    code défaut OBD si c'est le capteur vilebrequin ou arbre à cames. Consulter
    un éclaté moteur si nécessaire pour éviter de déposer le mauvais capteur. -
    Désassembler les éléments masquant l'accès : selon le moteur, déposer le
    cache moteur supérieur, une protection thermique, voire partiellement le
    turbo ou le collecteur d'admission pour accéder au capteur de vilebrequin. -
    Débrancher le connecteur électrique : appuyer sur le clip de déverrouillage
    avant de tirer. Photographier la position du câble et son chemin dans le
    faisceau pour faciliter la repose. - Dévisser la vis de fixation :
    généralement une vis M6 ou M8 unique. Utiliser une douille magnétique pour
    ne pas perdre la vis dans le moteur. Appliquer un peu de lubrifiant
    dégrippant si la vis est coincée — laisser agir 5 minutes. - Extraire le
    capteur délicatement : tirer en ligne droite dans l'axe. Si le capteur est
    collé par la rouille ou un dépôt, une légère rotation de 30° à droite et à
    gauche le libère progressivement. Ne jamais forcer perpendiculairement au
    risque de casser le corps dans le logement. - Nettoyer le logement avec soin
    : éliminer les copeaux de métal attirés magnétiquement sur la face active du
    capteur. Inspecter le joint torique d'étanchéité du logement (le remplacer
    si aplati). Vérifier l'absence de corrosion dans le filetage si le capteur
    est vissé. - Installer le nouveau capteur : insérer dans l'axe, visser à la
    main d'abord, puis serrer au couple prescrit (généralement 8 à 10 N.m).
    Rebrancher le connecteur jusqu'au clic de verrouillage. Reconnecter la
    batterie. Après pose, démarrer et effectuer immédiatement une lecture OBD
    pour confirmer l'absence de codes défauts actifs liés au capteur.
  S5: >-
    Ces erreurs sont récurrentes lors du remplacement du capteur d'allumage et
    peuvent conduire à une réparation inefficace ou à de nouveaux dommages : -
    Confondre capteur de vilebrequin et capteur d'arbre à cames sans lire les
    codes défauts : les deux capteurs ont parfois une apparence identique. Le
    capteur vilebrequin mesure la rotation du moteur (référence absolue),
    l'arbre à cames détermine la phase d'injection (admission ou échappement).
    Remplacer le mauvais capteur ne résout rien et laisse le problème d'origine
    intact. - Installer un capteur d'un type incompatible (inductif contre effet
    Hall) : le calculateur est câblé pour un type précis. Un capteur effet Hall
    monté à la place d'un inductif produit un signal de 5 V carré là où le
    calculateur attend un signal sinusoïdal — résultat : démarrage impossible ou
    codes défauts persistants. - Laisser des copeaux de métal dans le logement :
    les capteurs inductifs sont magnétiques. Les copeaux de métal présents dans
    le compartiment moteur s'accumulent sur la face active du capteur lors du
    retrait. Si ces copeaux restent dans le logement, le nouveau capteur se
    retrouve immédiatement encrassé et son signal est dégradé dès le premier
    démarrage. - Ne pas respecter l'entrefer sur les capteurs sans joint intégré
    : sur certaines applications, l'entrefer entre la face du capteur et la
    couronne phonique est fixé par une cale de calage fournie avec le capteur
    neuf. Un entrefer trop faible (moins de 0,3 mm) entraîne un contact rotor-
    capteur à chaud par dilatation ; trop important (plus de 1,5 mm), le signal
    est trop faible pour être lu. - Ne pas effacer les codes défauts après
    remplacement : un code P0335 mémorisé reste actif dans la mémoire du
    calculateur même après correction. Sans effacement OBD, le moteur peut
    rester en mode dégradé (avance fixe, limitation de régime) et masquer
    d'éventuels nouveaux défauts. - Sur-serrer la vis de fixation : le corps du
    capteur en plastique ou en aluminium se fissure facilement sous une
    contrainte excessive. Le couple de serrage est généralement limité à 8-10
    N.m — toujours utiliser une clé dynamométrique. - Ne pas vérifier le
    connecteur et le faisceau : le problème peut venir d'un connecteur oxydé ou
    d'un câble rompu à l'intérieur de sa gaine (rupture invisible). Mesurer la
    continuité du câble et nettoyer les contacts du connecteur avant de conclure
    à un capteur défectueux.
  S6: >-
    Ces contrôles permettent de confirmer que le remplacement a résolu la panne
    et que le capteur neuf fonctionne dans ses paramètres nominaux : -
    Reconnecter la batterie et démarrer : le moteur doit démarrer sans
    hésitation ni calage immédiat. Un refus de démarrage après pose d'un capteur
    neuf indique soit un problème de connecteur, soit un capteur incompatible. -
    Lecture OBD immédiate : effectuer un cycle de démarrage complet puis
    brancher un scanner OBD. Aucun code défaut P0335-P0349 ne doit être actif ou
    en attente. Les codes mémorisés du défaut précédent doivent avoir été
    effacés avant ou être effacés à ce stade. - Vérifier le ralenti à froid puis
    à chaud : le ralenti doit se stabiliser entre 700 et 900 tr/min sans
    oscillations supérieures à ±100 tr/min. Un ralenti instable persistant
    suggère soit un défaut de connecteur (micro-coupures), soit un autre capteur
    en cause. - Test de conduite à chaud pendant 20 minutes : les défaillances
    thermiques du capteur se manifestent uniquement à chaud. Si le moteur tient
    à chaud sans coupure ni perte de puissance, la réparation est confirmée. Un
    moteur qui recale uniquement après montée en température indique une autre
    pièce défaillante ou un faux contact sur le connecteur. - Vérifier les
    données en temps réel sur scanner : observer le signal de position
    vilebrequin en tr/min via les données temps réel du scanner OBD. Le signal
    doit être continu et proportionnel à la vitesse moteur, sans interruptions
    ni valeurs incohérentes. - Contrôle final de la vis de fixation : après 10
    minutes de fonctionnement, vérifier par le toucher (moteur froid, contact
    coupé) que la vis de fixation du capteur n'a pas vibré et desserré — une vis
    desserrée crée un jeu qui se traduit par un signal irrégulier.
  S7: >-
    Lors d'une panne liée au capteur d'allumage, plusieurs composants du système
    d'allumage et de gestion moteur doivent être contrôlés en parallèle. Un
    diagnostic incomplet peut masquer une panne secondaire persistante après le
    remplacement du capteur : - Bobine d'allumage — à contrôler en priorité si
    des ratés de combustion sur des cylindres spécifiques (codes P0301 à P030X)
    persistent après remplacement du capteur. La bobine utilise le signal du
    capteur d'allumage pour déclencher l'étincelle ; une bobine défaillante peut
    imiter un symptôme de capteur. - Bougies d'allumage — à inspecter et
    remplacer si un fonctionnement en mode dégradé (avance fixe, enrichissement)
    prolongé a provoqué une usure prématurée ou un encrassement des électrodes.
    Une bougie encrassée empêche la confirmation que le moteur tourne
    correctement après réparation du capteur. - Faisceau d'allumage — les câbles
    haute tension passent parfois près du capteur et peuvent parasiter son
    signal par induction électromagnétique. Un faisceau vieilli avec isolation
    détériorée génère des interférences qui simulent un capteur défaillant. -
    Capteur d'impulsion — sur certaines architectures (notamment Bosch Motronic
    ancienne génération), le capteur d'impulsion joue un rôle similaire au
    capteur d'arbre à cames. Sur les moteurs bi-arbres, un capteur défaillant
    sur le second arbre génère des codes de phase même avec le capteur
    vilebrequin sain. - Calculateur moteur (ECU) — si le capteur neuf ne
    supprime pas les codes défauts après plusieurs cycles de conduite, vérifier
    les alimentations et masses du calculateur. Rarement, une surtension sur le
    circuit capteur endommage l'entrée du calculateur.
  S8: >-
    Comment différencier une panne de capteur d'allumage d'une panne de bobine ?
    Le capteur d'allumage défaillant impacte l'ensemble du moteur simultanément
    : démarrage impossible, coupure moteur totale, codes P0335 à P0349. Une
    bobine défaillante provoque des ratés ciblés sur un ou plusieurs cylindres
    spécifiques (codes P0301 à P0308), le moteur tournant de façon irrégulière
    mais sans couper complètement. Confirmer avec un scanner OBD en mode données
    temps réel : observer le signal de position vilebrequin (continu pour un
    capteur sain) et les ratés par cylindre (localisés pour une bobine
    défaillante). Le moteur cale uniquement à chaud : comment confirmer que
    c'est le capteur ? La défaillance thermique du capteur inductif est un
    défaut classique : la résistance de la bobine interne augmente avec la
    chaleur jusqu'à produire un signal trop faible. Pour confirmer : mesurer la
    résistance du capteur à froid (500 à 1 000 ohms selon spécification) puis
    immédiatement après une coupure à chaud. Si la résistance dépasse 2 000 ohms
    à chaud, la défaillance thermique est confirmée. Alternativement, surveiller
    le signal capteur en données temps réel sur scanner : une disparition du
    signal uniquement à chaud est diagnostique. Peut-on rouler avec un code
    défaut capteur d'allumage actif ? Avec un code P0335 ou P0340 actif, le
    calculateur fonctionne en stratégie de sécurité : avance à l'allumage figée
    à une valeur conservative, injection légèrement enrichie pour compenser. La
    conduite est possible en mode dégradé si le signal est encore partiellement
    présent, mais la consommation augmente de 15 à 25 %, le catalyseur et les
    bougies se dégradent prématurément. Une panne totale du capteur de
    vilebrequin rend le démarrage strictement impossible. Faut-il recalibrer le
    calculateur après remplacement du capteur ? Sur la grande majorité des
    véhicules, non : le calculateur recalibrer son apprentissage automatiquement
    après 2 à 3 cycles de conduite complets. Sur certains modèles BMW, Mercedes
    ou VAG avec gestion d'allumage adaptative, une procédure de base adaption
    via outil de diagnostic constructeur (ISTA, XENTRY, ODIS) peut être
    prescrite. Consulter la documentation technique du modèle spécifique. Peut-
    on tester un capteur d'allumage sans scanner OBD ? Partiellement. Pour un
    capteur inductif : mesurer la résistance au multimètre en mode ohmmètre (200
    à 1 000 ohms = correct, infini ou zéro = défaillant). Vérifier également
    l'isolement entre les broches et la masse du véhicule (infini = correct).
    Pour un capteur effet Hall, ce test n'est pas applicable sans alimentation
    de référence 5 V — un oscilloscope branché directement sur le connecteur
    permet de visualiser le signal pendant le démarrage. Quelle est la
    différence entre capteur d'allumage et capteur d'impulsion ? Les deux
    capteurs mesurent la position des éléments rotatifs du moteur, mais leur
    rôle dans le calculateur diffère. Le capteur d'allumage (vilebrequin) est la
    référence principale de synchronisation moteur — sans lui, pas d'injection
    ni d'allumage. Le capteur d'impulsion est une dénomination ancienne souvent
    utilisée pour le capteur arbre à cames sur les moteurs Bosch L-Jetronic ou
    Motronic première génération. Sur les moteurs récents, les deux fonctions
    sont assurées par des capteurs distincts nommément désignés.
---

# Capteur d'allumage

<!-- A enrichir : Phase 5 -->
