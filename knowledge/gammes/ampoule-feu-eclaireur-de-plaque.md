---
category: eclairage
slug: ampoule-feu-eclaireur-de-plaque
title: Ampoule feu éclaireur de plaque
pg_id: 112
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
  role: Produit la lumière pour éclairer la plaque d'immatriculation
  must_be_true:
  - produire
  - emettre
  - eclairer
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
  - 'Type d''ampoule : Navette C5W ou capsule W5W selon véhicule'
  - 'Longueur navette : 36 mm, 39 mm ou 41 mm — mesurer l''existante'
  - 'Puissance : 5W standard (10W interdit — surchauffe du support)'
  - 'Culot : SV8.5-8 (navette) ou W2.1x9.5d (capsule)'
  - 'Technologie : Halogène classique ou LED blanc homologué ECE R7'
  - 'Quantité : Généralement 2 ampoules par véhicule — remplacer par paire'
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "visibilite parfaite"
  cost_range:
    min: 30
    max: 200
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Piece d'origine (OE)
    description: Ampoule reference constructeur. Utile si le vehicule est recent et sous garantie. Pour ce type de piece,
      la reference standard suffit dans la majorite des cas.
  - tier: Equipementier reconnu - ampoule standard
    description: Ampoule navette repondant aux specifications du vehicule. Les equipementiers d'eclairage reconnus proposent
      des produits homologues CE et adaptes aux normes en vigueur.
  - tier: Equivalent LED homologue
    description: Certains vehicules acceptent une ampoule LED en remplacement de la navette halogene. Verifier la compatibilite
      avec le vehicule et s'assurer que la LED est homologuee route (marquage E).
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
    label: Plaque d immatriculation non eclairee
    severity: confort
  - id: S2
    label: Eclairage faible ou clignotant
    severity: confort
  - id: S3
    label: Refus au controle technique
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'Usure ou defaillance causant : plaque d immatriculation non eclairee'
  - 'Usure ou defaillance causant : eclairage faible ou clignotant'
  quick_checks:
  - 'Observer : plaque d immatriculation non eclairee ?'
  - 'Observer : eclairage faible ou clignotant ?'
  - 'Observer : refus au controle technique ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Plaque d immatriculation non eclairee
  - Eclairage faible ou clignotant
  - Refus au controle technique
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '112'
  intro_title: A quoi sert Ampoule feu éclaireur de plaque ?
  risk_title: Pourquoi remplacer Ampoule feu éclaireur de plaque a temps ?
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
  - question: Comment choisir Ampoule feu éclaireur de plaque compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Ampoule feu éclaireur de plaque ?
    answer: En cas de plaque d immatriculation non eclairee ou de degradation mesurable, il faut controler rapidement avant
      panne secondaire.
  - question: Puis-je monter Ampoule feu éclaireur de plaque sans verification atelier ?
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
doc_id: 3030447c-cf13-5a2d-b84c-f8d29a6ab7fe
content_hash: sha256:59553f93cb8e703f
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
    L'ampoule feu éclaireur de plaque est le composant électrique chargé de
    produire la lumière nécessaire à l'éclairage de la plaque d'immatriculation
    arrière. Elle est montée dans un petit logement intégré au pare-chocs
    arrière, au coffre ou au hayon, à proximité directe de la plaque. Elle
    s'allume automatiquement en même temps que les feux de position et les feux
    de route. Son rôle est réglementaire : la plaque d'immatriculation doit être
    lisible de nuit à une distance minimale de 20 mètres selon la réglementation
    européenne. Sans un éclairage correct, la plaque devient illisible dans
    l'obscurité, ce qui constitue une infraction au code de la route et un motif
    de refus au contrôle technique. Techniquement, l'ampoule éclaireur de plaque
    fonctionne sur le circuit basse tension (12 V) du véhicule, couplé au
    circuit des feux de position. Elle est protégée par un fusible partagé avec
    les autres feux de signalisation. Les technologies disponibles incluent
    l'halogène classique et le LED, ce dernier étant de plus en plus courant sur
    les véhicules récents. Les types d'ampoules éclaireurs de plaque les plus
    fréquents sont la navette C5W (longueurs 36 mm, 39 mm ou 41 mm, culot
    SV8.5-8) et la capsule W5W (culot W2.1×9.5d). Ces deux types ne sont pas
    interchangeables et la longueur de la navette doit être mesurée avec
    précision sur l'ampoule d'origine avant de commander. La puissance standard
    est de 5 W — monter une ampoule de 10 W est formellement déconseillé car le
    support en plastique ne supporte pas cette charge thermique.
  S2: >-
    La défaillance d'une ampoule feu éclaireur de plaque se détecte par des
    signes visuels directs. Bien que cette panne ne compromette pas la conduite,
    elle entraîne une infraction réglementaire et peut conduire à un refus au
    contrôle technique. - Plaque d'immatriculation non éclairée : la plaque
    arrière est illisible de nuit alors que les feux de position sont allumés.
    C'est le symptôme le plus évident d'une ampoule grillée. Sur certains
    véhicules équipés de deux ampoules éclaireurs de plaque, une seule peut
    tomber en panne, rendant l'éclairage partiel. - Éclairage faible ou jaunâtre
    : l'ampoule produit encore de la lumière mais avec une intensité nettement
    réduite et une teinte jaunâtre prononcée. Ce symptôme signale une ampoule en
    fin de vie avec un filament fragilisé, à remplacer avant la panne totale. -
    Éclairage clignotant : l'ampoule s'allume et s'éteint de manière
    intermittente, signe d'un mauvais contact entre l'ampoule et son support, ou
    d'un filament en voie de rupture créant des micro-interruptions. - Refus au
    contrôle technique : le contrôleur signale l'absence ou l'insuffisance
    d'éclairage de la plaque comme défaillance. Ce point est systématiquement
    vérifié lors de l'inspection des éclairages réglementaires. - Condensation
    dans le logement de l'ampoule : si de la buée ou de l'eau s'est infiltrée
    dans le compartiment de l'ampoule éclaireur de plaque, l'humidité accélère
    la corrosion des contacts et la dégradation du filament. Une inspection
    visuelle directe depuis l'arrière du véhicule, feux de position allumés,
    permet de détecter immédiatement l'état de l'éclairage de la plaque.
  S3: >-
    Le choix d'une ampoule feu éclaireur de plaque est plus précis que pour
    d'autres ampoules de signalisation, car plusieurs dimensions et technologies
    spécifiques entrent en jeu. Une ampoule de mauvaise taille ne rentrera pas
    dans le logement ou ne fera pas contact correctement. - Identifier le type
    d'ampoule : navette C5W ou capsule W5W : la navette C5W (culot SV8.5-8) est
    cylindrique avec deux culots aux extrémités. La capsule W5W (culot
    W2.1×9.5d) est plus petite avec un seul culot. Ces deux formats ne sont pas
    interchangeables — consultez la référence de votre véhicule pour identifier
    le type correct. - Mesurer la longueur de la navette avec précision : les
    navettes C5W existent en 36 mm, 39 mm et 41 mm. Une navette de mauvaise
    longueur ne fera pas contact aux deux extrémités du support. Mesurez
    l'ampoule d'origine avant de commander ou vérifiez la référence
    constructeur. - Respecter la puissance de 5 W : la puissance standard est de
    5 W. Monter une ampoule de 10 W est formellement déconseillé — le support
    plastique de l'éclaireur de plaque n'est pas conçu pour cette charge
    thermique et peut fondre ou se déformer. - Vérifier le culot (SV8.5-8 pour
    navette, W2.1×9.5d pour capsule) : un culot incompatible peut forcer dans le
    logement et endommager le support de façon irréparable. - Choisir entre
    halogène classique et LED homologuée ECE R7 : une LED éclaireur de plaque
    offre une durée de vie de 20 000 à 30 000 heures contre 2 000 à 5 000 heures
    pour l'halogène. Vérifiez que la LED est homologuée pour cet usage — toutes
    les LED ne sont pas conformes pour les feux de signalisation réglementaires.
    - Remplacer par paire : la plupart des véhicules sont équipés de deux
    ampoules éclaireurs de plaque (une de chaque côté). Remplacez les deux
    simultanément — elles ont le même âge et la seconde grillera rapidement
    après la première. Pour aller plus loin : consultez notre guide d'achat
    ampoule feu éclaireur de plaque — comparatif marques, critères de choix et
    prix.
  S4_DEPOSE: >-
    Le remplacement d'une ampoule feu éclaireur de plaque est l'une des
    opérations les plus accessibles sur un véhicule, ne nécessitant généralement
    aucun outillage spécialisé. L'accès se fait directement depuis l'arrière du
    véhicule. - Couper le contact : éteignez le véhicule. Les ampoules
    éclaireurs de plaque s'allument avec les feux de position — attendez
    qu'elles refroidissent si elles étaient récemment allumées (1 à 2 minutes
    suffisent, leur puissance est faible). - Localiser le logement de l'ampoule
    : les éclaireurs de plaque sont généralement situés en haut ou sur les côtés
    de la zone de la plaque d'immatriculation. Ils sont souvent visibles
    directement depuis l'arrière du véhicule. Sur certains modèles intégrés dans
    le hayon, l'accès peut se faire depuis l'intérieur du coffre. - Ouvrir le
    logement de l'ampoule : selon le modèle, le logement s'ouvre par pression
    sur une languette, par rotation d'un quart de tour, ou par dépose d'une
    petite vis. Sur certains véhicules, un petit tournevis plat suffit pour
    déclipser le cache. - Extraire l'ampoule défaillante : pour une navette C5W,
    pincez légèrement et faites glisser l'ampoule hors de ses contacts à
    ressort. Pour une capsule W5W, effectuez une légère pression et rotation. Ne
    forcez pas — les supports en plastique sont fragiles. - Mesurer l'ampoule
    retirée si nécessaire : vérifiez la longueur de la navette (36, 39 ou 41 mm)
    avant d'aller acheter la pièce de remplacement si vous n'avez pas la
    référence constructeur. - Insérer la nouvelle ampoule : enclipsez ou faites
    glisser la nouvelle ampoule dans le support sans la toucher sur le verre
    avec les doigts (même précaution qu'avec les halogènes). Vérifiez que les
    deux extrémités de la navette sont bien en contact avec les broches du
    support. - Refermer le logement et tester : refermez le cache, allumez les
    feux de position et vérifiez que la plaque est correctement éclairée des
    deux côtés.
  S4_REPOSE: >-
    Le remontage d'une ampoule feu éclaireur de plaque est rapide et ne
    nécessite aucun outillage. La difficulté principale réside dans la fragilité
    du support plastique et de la petite taille des composants. Un remplacement
    par paire est vivement conseillé : les deux ampoules partagent le même
    circuit et le même niveau d'usure. - Préparer les nouvelles ampoules : les
    ampoules éclaireurs de plaque sont des navettes C5W (longueur 36, 39 ou 41
    mm selon le logement) ou des capsules W5W. Vérifiez la longueur exacte en
    mesurant l'ampoule retirée. Une navette trop courte ne fait pas contact ;
    une navette trop longue ne rentre pas dans le logement. - Insérer la navette
    dans le logement : la navette se place en comprimant légèrement les deux
    contacts métalliques aux extrémités pour la faire entrer dans son logement.
    Elle doit rester maintenue par la tension de ses contacts sur les bornes du
    support. Ne pas courber la navette lors de l'insertion — cela crée un
    mauvais contact permanent. - Vérifier le contact électrique : une fois en
    place, la navette doit être légèrement tendue dans son logement, sans jeu.
    Si elle bouge librement, les contacts aux extrémités sont trop courts ou
    usés — remplacer le support de lampe si nécessaire. - Remettre le diffuseur
    en place : repositionnez le diffuseur transparent en l'alignant sur son
    logement. Appuyez uniformément des deux côtés jusqu'au déclic ou revissez la
    vis de fixation si le système est vissé. Un diffuseur mal emboîté laisse
    pénétrer l'eau et génère un embuage de l'éclaireur. - Répéter pour le
    deuxième éclaireur : la grande majorité des véhicules dispose de deux
    éclaireurs de plaque. Remplacez les deux ampoules dans la même session pour
    homogénéiser l'éclairage et éviter une nouvelle intervention dans les
    semaines suivantes. - Test immédiat : allumez les feux de position (première
    position de la molette). Les deux éclaireurs doivent s'allumer simultanément
    avec une intensité identique. Une plaque non éclairée ou partiellement
    éclairée constitue un défaut au contrôle technique. - Vérification de la
    teinte : si des LED blanc homologuées ECE R7 ont été installées à la place
    des ampoules halogènes, comparez la couleur des deux éclaireurs. Une
    différence de teinte blanche (blanc chaud vs blanc froid) est visuellement
    inesthétique et potentiellement non conforme selon la réglementation locale.
  S5: >-
    Malgré la simplicité apparente de l'opération, plusieurs erreurs courantes
    surviennent lors du remplacement d'une ampoule feu éclaireur de plaque,
    pouvant conduire à une panne immédiate ou à un endommagement du support. -
    Commander une navette de mauvaise longueur : les navettes C5W existent en 36
    mm, 39 mm et 41 mm. Une navette trop courte ne contacte pas les deux broches
    et ne s'allume pas. Une navette trop longue force dans le logement et peut
    casser le support plastique. Mesurer l'ampoule d'origine ou vérifier la
    référence constructeur avant toute commande. - Monter une ampoule de 10 W :
    certains conducteurs pensent qu'une puissance supérieure améliore la
    visibilité de la plaque. C'est une erreur — le support plastique de
    l'éclaireur de plaque n'est pas dimensionné pour dissiper la chaleur d'une
    ampoule de 10 W. Il peut se déformer, fondre ou prendre feu. - Forcer lors
    de l'extraction ou du montage : les supports éclaireurs de plaque sont en
    plastique fin et fragile. Forcer l'extraction d'une ampoule coincée ou le
    montage d'une ampoule de mauvaise longueur casse facilement les broches de
    contact ou le corps du support, entraînant un remplacement du support lui-
    même. - Ne remplacer qu'une seule ampoule sur deux : les véhicules équipés
    de deux ampoules éclaireurs de plaque voient généralement les deux vieillir
    au même rythme. Ne remplacer que l'ampoule grillée conduit à une seconde
    intervention dans les semaines suivantes. Remplacez systématiquement par
    paire. - Ignorer la corrosion des contacts : si les contacts à ressort du
    support sont oxydés, la nouvelle ampoule ne fonctionnera pas de manière
    fiable. Nettoyez les contacts avec un papier de verre fin ou un spray
    nettoyant contacts avant le montage.
  S6: >-
    Après le remplacement de l'ampoule feu éclaireur de plaque, quelques
    contrôles simples permettent de confirmer que l'installation est conforme et
    que la plaque sera lisible de nuit. - Test d'allumage immédiat : allumez les
    feux de position et vérifiez que la plaque arrière est uniformément
    éclairée. Si le véhicule dispose de deux ampoules éclaireurs de plaque, les
    deux doivent fonctionner et offrir un éclairage homogène. - Contrôle de la
    lisibilité à distance : reculez d'environ 5 mètres derrière le véhicule et
    vérifiez que les caractères de la plaque d'immatriculation sont clairement
    lisibles. L'éclairage doit être blanc, stable et sans zones d'ombre. -
    Vérification de l'étanchéité du logement : assurez-vous que le cache de
    l'ampoule est correctement refermé et que le joint d'étanchéité (si présent)
    est en place. Une infiltration d'humidité dans le logement corrode les
    contacts et réduit la durée de vie de la nouvelle ampoule. - Contrôle de la
    fixation du cache : le cache de l'éclaireur de plaque doit être fermement
    verrouillé. Un cache mal fixé peut s'ouvrir lors d'un lavage haute pression
    ou par vibration, exposant l'ampoule aux intempéries. - Test d'extinction :
    éteignez les feux de position et vérifiez que l'éclaireur de plaque s'éteint
    immédiatement. Un éclaireur qui reste allumé signale un problème dans le
    circuit d'alimentation.
  S7: >-
    L'ampoule éclaireur de plaque fait partie d'un sous-ensemble de
    signalisation arrière. Son remplacement est l'occasion de contrôler les
    composants voisins qui participent à la visibilité réglementaire et à
    l'étanchéité du système d'éclairage arrière. - Support de lampe (porte-
    ampoule d'éclaireur) : le support plastique maintient la navette et assure
    le contact électrique via ses deux bornes métalliques. S'il est jauni,
    fissuré ou si ses bornes sont oxydées et ne font plus pression sur la
    navette, le support doit être remplacé. Un support défaillant fait griller
    les ampoules en quelques heures par arc électrique. - Feu arrière complet :
    le feu arrière intègre souvent l'éclaireur de plaque, le stop, le clignotant
    et le feu de recul dans un même boîtier. Si le feu présente une lentille
    jaunie, fissurée ou oxydée en profondeur, le remplacement du bloc entier est
    une solution plus durable que de changer uniquement l'ampoule. - Ampoule feu
    arrière (feu de position arrière) : s'allume simultanément avec l'éclaireur
    de plaque lors de l'allumage des feux de position. Si l'un des feux arrière
    est défaillant, le contrôle technique signalera un défaut de signalisation.
    Profitez de l'accès au circuit arrière pour vérifier les feux de position
    arrière. - Câblage et connecteur d'éclaireur : le câblage alimentant les
    éclaireurs de plaque est fin et court. Sur les haïons et portes de coffre
    avec charnière, le passage du câble peut être soumis à des flexions répétées
    qui causent des ruptures de fil internes invisibles à l'oeil nu. Un câble
    avec gaine craquelée ou une connectique brûlée doivent être remplacés. -
    Joint d'étanchéité du feu ou de l'éclaireur : l'éclaireur de plaque est en
    bas du véhicule, exposé aux projections d'eau. Son joint d'étanchéité doit
    être intact pour éviter les infiltrations dans le bloc feu. Un embuage
    régulier du feu est souvent dû à un joint d'éclaireur défaillant. - Vis de
    fixation de la plaque d'immatriculation : lors de l'accès à l'éclaireur de
    plaque, vérifiez l'état des vis et des supports de plaque. Des vis rouillées
    ou des supports cassés peuvent nécessiter un remplacement préventif pour
    éviter de perdre la plaque en roulant.
  S8: >-
    Quelle est la différence entre une navette C5W et une capsule W5W pour
    éclaireur de plaque ? La navette C5W est une ampoule cylindrique avec deux
    culots aux extrémités (culot SV8.5-8) qui s'insère dans un support à deux
    contacts à ressort. Elle existe en 36 mm, 39 mm et 41 mm de longueur. La
    capsule W5W est plus petite, avec un seul culot à une extrémité (culot
    W2.1×9.5d). Ces deux formats correspondent à des supports différents et ne
    sont pas interchangeables. Pour identifier le bon format, retirez l'ampoule
    d'origine et mesurez-la, ou consultez la référence constructeur. Peut-on
    mettre une LED à la place d'une ampoule halogène éclaireur de plaque ? Oui,
    à condition de choisir une LED homologuée ECE R7 pour les éclaireurs de
    plaque. Les LED offrent une durée de vie bien supérieure (20 000 à 30 000
    heures) et une luminosité plus froide et plus blanche. Vérifiez que la LED a
    les mêmes dimensions que l'ampoule d'origine (longueur de navette notamment)
    et que le culot est compatible. Sur les véhicules avec contrôle électronique
    des ampoules, une LED peut déclencher un faux voyant de défaut si sa
    consommation est trop faible. L'éclaireur de plaque est-il vérifié au
    contrôle technique ? Oui, systématiquement. Le contrôleur technique vérifie
    que la plaque d'immatriculation arrière est correctement éclairée de nuit.
    Une ampoule éclaireur de plaque défaillante entraîne une défaillance notée à
    l'inspection, pouvant conduire à une contre-visite selon la sévérité du
    défaut détecté. Il est nécessaire de remplacer toute ampoule défaillante
    avant de présenter le véhicule au contrôle technique. Pourquoi ma nouvelle
    ampoule éclaireur de plaque ne fonctionne-t-elle pas après remplacement ?
    Les causes les plus fréquentes sont : une navette de mauvaise longueur (ne
    fait pas contact), des contacts à ressort du support corrodés (nettoyer avec
    un vaporisateur contacts), un fusible grillé du circuit feux de position (à
    vérifier en boîtier à fusibles), ou un connecteur mal emboîté. Vérifiez ces
    points dans l'ordre avant de conclure à un défaut de la nouvelle ampoule.
  META: >-
    Plaque d'immatriculation non éclairée, éclairage clignotant ou refus au
    contrôle technique ? Identifiez et remplacez l'ampoule feu éclaireur de
    plaque.
---

# Ampoule feu éclaireur de plaque - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière pour éclairer la plaque d'immatriculation

**Actions principales:** produire, emettre, eclairer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- plaque d immatriculation non eclairee
- eclairage faible ou clignotant
- refus au controle technique

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule feu éclaireur de plaque:

1. **Inspection visuelle** - Examiner l'état du ampoule feu éclaireur de plaque
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
- ampoule-feu-arriere

## Critères de Compatibilité

Pour commander le bon ampoule feu éclaireur de plaque, vous devez connaître:

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

**Comment choisir Ampoule feu éclaireur de plaque compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Ampoule feu éclaireur de plaque ?**
En cas de plaque d immatriculation non eclairee ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Ampoule feu éclaireur de plaque sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
