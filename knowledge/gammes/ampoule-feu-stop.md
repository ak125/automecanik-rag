---
category: eclairage
slug: ampoule-feu-stop
title: Ampoule feu stop
pg_id: 111
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
  role: Produit la lumière pour signaler le freinage du véhicule
  must_be_true:
  - produire
  - emettre
  - signaler
  must_not_contain:
  - feu complet
  - optique
  - relais
  - commande
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - ampoule-feu-avant
  - ampoule-feu-arriere
  - feu-avant
  - feu-arriere
  - phares-antibrouillard
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
  - ❌ "visibilite parfaite"
  cost_range:
    min: 2
    max: 15
    currency: EUR
    unit: ampoule
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
  - tier: Équivalent OE / équipementier éclairage reconnu
  - tier: Ampoule LED stop compatible
  brands:
    premium:
    - Osram
    - Philips
    standard:
    - Bosch
    - Hella
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Un seul feu stop ne s allume pas
    severity: confort
  - id: S2
    label: Feu stop qui clignote ou s allume faiblement
    severity: confort
  - id: S3
    label: Ampoule noircie visible a travers le feu
    severity: confort
  - id: S4
    label: Message defaut feux au tableau de bord
    severity: confort
  - id: S5
    label: Feux stop grillent souvent verifier
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : un seul feu stop ne s allume pas'
  quick_checks:
  - 'Observer : un seul feu stop ne s allume pas ?'
  - 'Observer : feu stop qui clignote ou s allume faiblement ?'
  - 'Observer : ampoule noircie visible a travers le feu ?'
  - 'Observer : message defaut feux au tableau de bord ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Seul feu stop ne s allume pas
  - Feu stop qui clignote ou s allume faiblement
  - Ampoule noircie visible a travers le feu
  - Message defaut feux au tableau de bord
  - Feux stop grillent souvent verifier
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '111'
  intro_title: A quoi sert Ampoule feu stop ?
  risk_title: Pourquoi remplacer Ampoule feu stop a temps ?
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
  - question: Quelle ampoule pour mes feux stop ?
    answer: La plus courante est la P21W (simple filament) ou P21/5W (double filament si combinée avec le feu de position).
      Vérifiez dans votre carnet d'entretien ou sur l'ampoule d'origine.
  - question: Puis-je mettre des LED ?
    answer: Oui, mais attention à la compatibilité. Certains véhicules détectent les LED comme défaillantes (consommation
      trop faible). Il peut falloir ajouter une résistance.
  - question: Comment accéder aux ampoules ?
    answer: 'Généralement par l''intérieur du coffre : déclipsez le cache ou dévissez le bloc feu. Sur certains modèles, il
      faut retirer le bloc complet depuis l''extérieur.'
  - question: Quelles sont les erreurs fréquentes à éviter ?
    answer: Toucher le verre de l'ampoule avec les doigts (graisse = point chaud = grillage). Forcer sur la douille. Ne pas
      vérifier le fusible si les deux feux sont HS.
  - question: Comment faire un diagnostic rapide ?
    answer: Un seul feu HS → ampoule. Les deux HS → fusible ou contacteur. Feu faible → mauvais contact ou ampoule fatiguée.
      Clignote → contact intermittent.
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
doc_id: 30194bb1-c54b-540c-804d-8ea1736201e6
content_hash: sha256:3e22c4aa5b15daf8
lang: fr
variants:
- name: Ampoule halogene
  aliases:
  - halogene
  - H1
  - H4
  - H7
  functional_differences:
  - Standard, economique
  - Remplacement simple
- name: Ampoule LED
  aliases:
  - LED
  functional_differences:
  - Duree de vie superieure
  - Consommation reduite
  - Verifier homologation
location_on_vehicle:
  area: Face avant, arriere et laterale du vehicule
  access: Par le compartiment moteur (avant) ou coffre (arriere)
  adjacent_parts:
  - optique
  - ampoule
  - connecteur
  - reflecteur
installation:
  difficulty: facile
  time: 5 a 15 min
  tools:
  - tournevis
  - gants (ne pas toucher ampoule halogene)
  prerequisite: Moteur eteint, acces par compartiment moteur ou coffre
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'plein'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    L'ampoule feu stop est le composant électrique qui produit la lumière rouge
    signalant le freinage du véhicule aux conducteurs qui le suivent. Elle
    s'allume automatiquement dès que le conducteur appuie sur la pédale de
    frein, via le contacteur de feux stop fixé sur le maître-cylindre ou sur la
    pédale elle-même. Son rôle est fondamentalement sécuritaire : avertir le
    conducteur suivant d'une décélération ou d'un arrêt imminent, lui permettant
    d'adapter sa propre vitesse et d'éviter une collision arrière. C'est l'un
    des éclairages les plus sollicités d'un véhicule — en circulation urbaine,
    une ampoule feu stop peut être activée des centaines de fois par jour.
    Techniquement, l'ampoule feu stop est alimentée par le circuit 12 V du
    véhicule à travers le contacteur de frein. Les types d'ampoules les plus
    courants sont la P21W (filament simple, 21 W, culot BA15s) pour les feux
    stop indépendants, et la P21/5W (double filament, culot BAY15d) lorsque le
    feu stop est combiné avec le feu de position arrière. Ce double filament
    permet à une seule ampoule d'assumer les deux fonctions : 5 W en permanence
    pour le feu de position, 21 W lors du freinage pour le feu stop. Sur les
    véhicules récents, des ampoules LED de remplacement sont disponibles. Elles
    offrent une réponse lumineuse quasi instantanée (temps de réaction de
    l'ordre de 200 microsecondes contre 200 millisecondes pour l'halogène), ce
    qui représente une distance de freinage évitable de plusieurs mètres à 130
    km/h pour le conducteur suivant.
  S2: >-
    L'ampoule feu stop présente des symptômes de défaillance caractéristiques
    qui doivent conduire à une intervention immédiate. Un feu stop défaillant
    constitue un danger sécuritaire grave et une infraction au code de la route.
    - Un seul feu stop ne s'allume pas : lors du freinage, un seul côté
    s'éclaire. Ce symptôme direct indique la rupture du filament de l'ampoule du
    côté défaillant. Sur les véhicules à double feu stop, ce cas pointe
    clairement vers l'ampoule. - Feu stop qui clignote ou s'allume faiblement
    lors du freinage : la lumière produite par le feu stop est instable — elle
    vacille, clignote ou présente une intensité nettement inférieure à la
    normale. Ce comportement signale un filament fragilisé en fin de vie ou un
    mauvais contact électrique dans la douille. - Ampoule noircie visible à
    travers la glace du feu : une tache sombre, brune ou noire visible à
    l'intérieur du verre de l'ampoule halogène indique que le filament a
    surchauffé ou brûlé. L'ampoule peut encore fonctionner quelques heures, mais
    la panne totale est imminente. - Message de défaut feux au tableau de bord :
    sur les véhicules récents équipés d'un système de surveillance des ampoules
    (BCI — Bulb Control Interface), un pictogramme ou un message texte s'affiche
    dès qu'une défaillance est détectée dans le circuit feu stop. - Feux stop
    grillent souvent et répétitivement : si les ampoules feu stop doivent être
    remplacées plus d'une fois par an, c'est le signe d'un problème électrique
    sous-jacent — tension trop élevée, contacteur de frein défectueux envoyant
    un signal continu, ou mauvaise qualité de la douille. Ce symptôme justifie
    un diagnostic électrique complet. Méthode de diagnostic rapide : un seul feu
    HS pointe vers l'ampoule. Les deux feux HS simultanément orientent vers le
    fusible ou le contacteur de frein. Un feu faible indique un mauvais contact
    ou un filament en fin de vie. Un clignotement signale un contact
    intermittent.
  S3: >-
    Choisir la bonne ampoule feu stop exige de distinguer plusieurs paramètres
    techniques précis, notamment entre les ampoules à simple et double filament.
    Une erreur de référence peut conduire à un feu stop inactif ou à un feu de
    position permanent parasite. - Identifier si le feu stop est indépendant ou
    combiné avec le feu de position : les feux stop indépendants utilisent une
    ampoule P21W (simple filament, 21 W, culot BA15s). Les feux stop combinés
    avec le feu de position utilisent une P21/5W (double filament, culot BAY15d,
    21 W + 5 W). Ces deux types ne sont pas interchangeables — vérifiez la
    configuration de votre bloc feu avant de commander. - Vérifier le culot : le
    culot BA15s de la P21W et le culot BAY15d de la P21/5W ont des détrompeurs
    différents. Monter un mauvais culot force dans la douille, risquant de la
    briser. - Confirmer la puissance de 21 W : le circuit du feu stop est
    dimensionné pour 21 W. Ne pas augmenter cette valeur — risque de surcharge
    du câblage et de fusion de la douille. - Envisager le passage aux LED : les
    LED feu stop offrent une réactivité quasi instantanée, améliorant la
    sécurité du conducteur suivant. Vérifiez la compatibilité avec le contrôle
    électronique de votre véhicule. Sur les modèles avec surveillance des
    ampoules, une résistance de compensation peut être nécessaire. - Vérifier
    l'état de la douille et du contacteur : si les ampoules feu stop grillent
    fréquemment, une tension excessive ou un contacteur de frein défectueux peut
    en être la cause. Diagnostiquer ces éléments avant d'investir dans une
    ampoule de remplacement. - Remplacer par paire : remplacez les deux ampoules
    feu stop (gauche et droite) simultanément si elles ont le même kilométrage,
    pour éviter une seconde panne rapide de l'autre côté. Pour aller plus loin :
    consultez notre guide d'achat ampoule feu stop — comparatif marques,
    critères de choix et prix.
  S4_DEPOSE: >-
    Le remplacement d'une ampoule feu stop est accessible à tout conducteur
    attentif. L'accès se fait généralement par l'intérieur du coffre, parfois
    par l'extérieur selon le modèle. La procédure dure de 10 à 30 minutes selon
    l'accessibilité du bloc feu. - Couper le contact et laisser refroidir :
    éteignez le véhicule et attendez au moins 5 minutes. L'ampoule feu stop est
    fortement sollicitée en conduite urbaine — elle peut atteindre des
    températures élevées. - Accéder au bloc feu arrière : ouvrez le coffre. Sur
    la majorité des véhicules, un cache en plastique intérieur (déclipsable ou
    fixé par des vis à main) donne accès aux porte-ampoules. Sur certains
    modèles, le bloc feu complet doit être retiré depuis l'extérieur après
    dépose de 2 à 4 vis. - Identifier le porte-ampoule du feu stop : repérez le
    porte-ampoule correspondant au feu stop — généralement identifié par un
    marquage sur le cache intérieur ou dans le manuel du véhicule. Sur les blocs
    avec P21/5W combinée, le même porte-ampoule gère le stop et le feu de
    position. - Débrancher le connecteur électrique : appuyez sur le clip de
    verrouillage et retirez le connecteur sans tirer sur les fils. - Extraire le
    porte-ampoule : tournez d'un quart de tour dans le sens antihoraire et
    sortez le porte-ampoule du bloc feu. - Retirer l'ampoule défaillante :
    appuyez légèrement et tournez d'un quart de tour dans le sens antihoraire
    (baïonnette). Ne pas toucher le verre de la nouvelle ampoule halogène avec
    les doigts nus. - Insérer la nouvelle ampoule : alignez les tenons de la
    nouvelle ampoule avec les rainures de la douille, insérez et tournez d'un
    quart de tour dans le sens horaire pour verrouiller. - Tester avant de
    refermer : reconnectez le connecteur, demandez à un tiers de confirmer le
    fonctionnement du feu stop pendant que vous appuyez sur la pédale de frein —
    vérifiez avant de refermer le cache intérieur. - Remonter dans l'ordre
    inverse : réinsérez le porte-ampoule, refixez le cache intérieur ou le bloc
    feu extérieur.
  S4_REPOSE: >-
    Le remontage d'une ampoule feu stop s'effectue dans l'ordre inverse de la
    dépose. La procédure dure entre 5 et 20 minutes selon l'accessibilité du
    bloc feu. Points critiques à respecter : ne pas toucher le verre de
    l'ampoule halogène avec les doigts nus, et s'assurer que le porte-ampoule
    est correctement verrouillé avant de refermer. - Préparer la nouvelle
    ampoule : l'ampoule feu stop standard est une P21W (21 W, culot BA15s, un
    ergot) pour les feux stop simples, ou une P21/5W (21/5 W, culot BAY15d, deux
    ergots décalés) lorsque le feu stop est combiné avec le feu de position
    arrière. Vérifiez absolument la référence sur l'ampoule retirée. Une P21W
    montée en lieu et place d'une P21/5W provoque un défaut de circuit
    détectable par le calculateur. - Manipuler l'ampoule avec précaution : pour
    les ampoules halogènes, ne touchez jamais le verre — la graisse des doigts
    crée un point chaud à haute température et réduit dramatiquement la durée de
    vie. Utilisez un morceau de tissu propre ou des gants fins sans poudre.
    Cette précaution est inutile pour les ampoules LED. - Engager l'ampoule dans
    la douille : alignez les ergots du culot baïonnette avec les rainures
    correspondantes de la douille. Pour une P21W à un ergot : le culot est
    symétrique, toute orientation est correcte. Pour une P21/5W à deux ergots
    décalés : le détrompeur physique empêche une insertion incorrecte — si
    l'ampoule ne s'engage pas, elle est en mauvaise position ou de mauvaise
    référence. - Effectuer le quart de tour de verrouillage : une fois l'ampoule
    engagée et le ressort de fond de douille comprimé, tournez d'un quart de
    tour dans le sens horaire jusqu'au verrouillage. L'ampoule ne doit pas se
    rétracter sous la pression du ressort. Un léger tirage en sens inverse
    confirme le verrouillage. - Réinsérer le porte-ampoule dans le bloc feu :
    réintroduisez l'ensemble porte-ampoule dans son logement dans le bloc feu
    arrière. Effectuez le quart de tour de verrouillage ou clipsez selon le
    système du véhicule. Assurez-vous que les plots d'étanchéité du porte-
    ampoule sont bien positionnés pour éviter les infiltrations d'eau. -
    Reconnecter le faisceau si débranché : réenficher le connecteur
    d'alimentation jusqu'au déclic. Si le bloc feu intègre plusieurs fonctions
    (stop, clignotant, recul, position), un seul connecteur multibroche est
    généralement utilisé — vérifiez qu'il est correctement enfoncé sur toute sa
    longueur. - Refermer l'accès : si vous avez accédé par l'intérieur du
    coffre, reclipsez le cache de garniture en commençant par les clips du bord
    supérieur. Si le bloc feu a été déposé depuis l'extérieur, repositionnez-le
    sur son cadre et revissez les vis de fixation sans trop forcer pour ne pas
    fissurer le plastique. - Test fonctionnel impératif : demandez à un tiers
    d'appuyer sur la pédale de frein pendant que vous observez depuis l'arrière.
    Les deux feux stop doivent s'allumer avec la même intensité. Un stop
    asymétrique (un fort, un faible) indique une mauvaise référence d'ampoule ou
    un mauvais contact. Si le feu reste éteint malgré l'ampoule neuve, testez le
    fusible et le contacteur de stop avant toute autre vérification.
  S5: >-
    Plusieurs erreurs fréquentes surviennent lors du diagnostic ou du
    remplacement d'une ampoule feu stop. Certaines sont des erreurs de
    diagnostic qui conduisent à remplacer la mauvaise pièce, d'autres sont des
    erreurs de montage qui réduisent la durée de vie de la nouvelle ampoule. -
    Toucher le verre de l'ampoule halogène avec les doigts : les traces de
    graisse et de sel de la transpiration créent un point de faiblesse thermique
    sur le verre lors de l'allumage. Ce point surchauffe et provoque la rupture
    prématurée du filament — parfois en quelques heures. Saisir l'ampoule par
    son culot ou utiliser un chiffon propre sans peluchage. - Remplacer
    l'ampoule quand les deux feux stop sont éteints : si les deux feux stop sont
    inactifs simultanément, la cause n'est presque jamais une double panne
    d'ampoule — vérifiez d'abord le fusible du circuit feux stop, puis le
    contacteur de frein fixé sur la pédale ou le maître-cylindre. - Confondre
    P21W et P21/5W : monter une P21W (simple filament) à la place d'une P21/5W
    (double filament) résulte en un feu stop qui ne s'allume que lors du
    freinage, sans feu de position permanent — ou l'inverse. De plus, les culots
    BA15s et BAY15d ont des détrompeurs différents qui peuvent endommager la
    douille si on force. - Forcer lors de l'insertion ou du retrait de la
    baïonnette : les douilles de feux stop sont en plastique. Forcer lors de
    l'opération de baïonnette (pression + rotation) peut casser la douille,
    nécessitant le remplacement du bloc feu complet. - Ne pas diagnostiquer la
    cause d'une usure anormalement rapide : si l'ampoule feu stop grille plus
    d'une fois tous les 2 ans, une tension excessive (alternateur défectueux),
    un contacteur de frein bloqué en position fermée ou une mauvaise qualité de
    la douille sont en cause. Remplacer uniquement l'ampoule sans traiter la
    cause conduit à une récidive rapide.
  S6: >-
    Après le remplacement d'une ampoule feu stop, plusieurs vérifications
    confirment le bon fonctionnement et la sécurité du montage. - Test de
    freinage avec observateur : demandez à un tiers de se positionner derrière
    le véhicule, démarrez le moteur et appuyez sur la pédale de frein. Vérifiez
    que le feu stop s'allume immédiatement et avec une intensité lumineuse
    identique des deux côtés. - Vérification de l'extinction sans freinage :
    relâchez la pédale de frein et confirmez que le feu stop s'éteint
    immédiatement. Un feu stop qui reste allumé en permanence indique un
    contacteur de frein bloqué — à corriger rapidement car cela épuise la
    batterie et provoque une usure prématurée de l'ampoule. - Contrôle de la
    disparition du voyant tableau de bord : si un voyant de défaut feux stop
    s'affichait, il doit s'éteindre dans les secondes suivant le remplacement et
    le premier test de freinage. - Vérification du feu de position si P21/5W :
    si l'ampoule remplacée est une P21/5W double filament, vérifiez également
    que le feu de position (lumière de faible intensité permanente) fonctionne
    correctement lorsque les feux de position sont allumés. - Contrôle de
    l'étanchéité du cache : assurez-vous que le cache intérieur du coffre est
    correctement replacé et que le joint du bloc feu est en place pour prévenir
    toute infiltration d'humidité dans le bloc optique.
  S7: >-
    Le feu stop appartient au circuit de freinage électrique et partage son
    environnement avec plusieurs composants critiques pour la sécurité. Un feu
    stop défaillant expose à un risque d'accident par l'arrière — son
    remplacement est l'occasion de contrôler l'ensemble du circuit de
    signalisation de freinage. - Contacteur de feu stop (contacteur de pédale de
    frein) : si les deux feux stop sont inactifs simultanément alors que les
    ampoules sont neuves, le contacteur est le coupable le plus probable. Il est
    vissé sur le support de pédale de frein dans l'habitacle. Testez-le
    facilement avec un multimètre en appuyant sur la pédale — il doit fermer le
    circuit. - Troisième feu stop (feu stop central haut) : situé en haut du
    haïon ou dans la lunette arrière, il utilise une technologie LED sur les
    véhicules récents ou une ampoule C5W/W21W sur les plus anciens. Un troisième
    stop défaillant constitue un défaut au contrôle technique — vérifiez son
    état dans la même session. - Ampoule feu stop côté opposé : remplacez les
    deux feux stop simultanément. Une différence d'intensité entre les deux feux
    (un neuf, un vieillissant) est visuellement détectable et peut générer une
    confusion pour les conducteurs suiveurs lors d'un freinage d'urgence. - Feu
    arrière complet : le feu stop est logé dans le bloc feu arrière avec le feu
    de position, le clignotant et parfois le feu de recul. Un bloc fissures,
    oxydé ou présentant un embuage chronique devrait être remplacé pour garantir
    une étanchéité durable. - Fusible de circuit stop : si les deux feux stop ne
    s'allumaient plus, le fusible dédié est à vérifier avant tout. Il est
    localisé dans le boîtier à fusibles habitacle ou moteur (référencer dans le
    manuel du véhicule). Un fusible qui grille de façon répétée indique un
    court-circuit dans le circuit. - Câblage de feu stop : sur les véhicules à
    haïon ou break, le câblage passe par une charnière soumise à des flexions
    répétées à chaque ouverture. Inspectez l'état des câbles au niveau de la
    charnière — une gaine craquelée révèle souvent un fil cassé en interne qui
    provoque des coupures intermittentes.
  S8: >-
    Quelle ampoule pour les feux stop : P21W ou P21/5W ? La P21W (simple
    filament, 21 W, culot BA15s) équipe les véhicules dont le feu stop est
    séparé du feu de position — deux ampoules distinctes dans le même bloc feu.
    La P21/5W (double filament, 21 W + 5 W, culot BAY15d) est utilisée quand une
    seule ampoule assure à la fois le feu de position (5 W en continu) et le feu
    stop (21 W lors du freinage). Vérifiez le type exact sur l'ampoule d'origine
    ou dans le carnet d'entretien — les culots des deux types ont des
    détrompeurs différents qui empêchent tout montage incorrect si vous ne
    forcez pas. Peut-on mettre des LED pour les feux stop ? Oui, sous conditions
    de compatibilité. Les LED feu stop réagissent environ 1 000 fois plus vite
    que les ampoules halogène (0,2 ms contre 200 ms), ce qui permet au
    conducteur suivant de gagner plusieurs mètres de distance de freinage à
    haute vitesse. Cependant, sur les véhicules avec contrôle électronique des
    ampoules, une LED de faible consommation peut être interprétée comme une
    panne. Dans ce cas, il faut installer une résistance de compensation en
    parallèle sur le circuit, ou choisir des LED avec résistance intégrée.
    Comment faire un diagnostic rapide des feux stop ? La règle est simple : un
    seul feu HS → l'ampoule de ce côté est grillée (vérifiez visuellement le
    noircissement). Les deux feux HS simultanément → vérifiez le fusible du
    circuit feux stop dans le boîtier à fusibles, puis le contacteur de frein.
    Feu faible → mauvais contact dans la douille ou filament en fin de vie. Feu
    qui clignote → contact intermittent entre l'ampoule et la douille, ou
    douille corrodée. Pourquoi mes ampoules feu stop grillent-elles souvent ?
    Une usure anormalement rapide des ampoules feu stop signale un problème
    électrique. Les causes les plus fréquentes sont : un alternateur délivrant
    une tension supérieure à 14,4 V (surveiller avec un voltmètre), un
    contacteur de frein bloqué en position fermée (feu stop allumé en
    permanence), une douille de mauvaise qualité créant des arcs électriques, ou
    des vibrations excessives fragilisant le filament. Un diagnostic électrique
    du circuit s'impose avant de continuer à remplacer les ampoules.
---

# Ampoule feu stop - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière pour signaler le freinage du véhicule

**Actions principales:** produire, emettre, signaler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- un seul feu stop ne s allume pas
- feu stop qui clignote ou s allume faiblement
- ampoule noircie visible a travers le feu
- message defaut feux au tableau de bord
- feux stop grillent souvent verifier

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule feu stop:

1. **Inspection visuelle** - Examiner l'état du ampoule feu stop
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

- feu-arriere
- contacteur-feu-stop

## Critères de Compatibilité

Pour commander le bon ampoule feu stop, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "visibilite parfaite"

## FAQ

**Quelle ampoule pour mes feux stop ?**
La plus courante est la P21W (simple filament) ou P21/5W (double filament si combinée avec le feu de position). Vérifiez dans votre carnet d'entretien ou sur l'ampoule d'origine.

**Puis-je mettre des LED ?**
Oui, mais attention à la compatibilité. Certains véhicules détectent les LED comme défaillantes (consommation trop faible). Il peut falloir ajouter une résistance.

**Comment accéder aux ampoules ?**
Généralement par l'intérieur du coffre : déclipsez le cache ou dévissez le bloc feu. Sur certains modèles, il faut retirer le bloc complet depuis l'extérieur.

**Quelles sont les erreurs fréquentes à éviter ?**
Toucher le verre de l'ampoule avec les doigts (graisse = point chaud = grillage). Forcer sur la douille. Ne pas vérifier le fusible si les deux feux sont HS.

**Comment faire un diagnostic rapide ?**
Un seul feu HS → ampoule. Les deux HS → fusible ou contacteur. Feu faible → mauvais contact ou ampoule fatiguée. Clignote → contact intermittent.
