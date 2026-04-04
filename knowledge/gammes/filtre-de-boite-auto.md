---
category: filtration
slug: filtre-de-boite-auto
title: Filtre de boîte auto
pg_id: 416
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
  last_enriched_by: skill:phase5-vague4
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Filtrer l'huile de la boite automatique
  must_be_true:
  - filtrer
  - retenir
  - purifier
  must_not_contain:
  - injection
  - freinage
  - direction
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - filtre-a-air
  - filtre-a-huile
  - filtre-d-habitacle
  - filtre-a-carburant
  confusion_with:
  - term: autre-filtre
    difference: Chaque filtre a un role specifique (air, huile, habitacle, carburant, boite). Verifier le type exact avant
      commande.
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
  - ❌ "filtration parfaite"
  cost_range:
    min: 20
    max: 80
    currency: EUR
    unit: filtre
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
    description: Filtre conforme aux spécifications du fabricant de la boîte automatique. Finesse de filtration, capacité
      de débit et dimensions conformes. Fortement recommandé pour les boîtes à double embrayage (DSG,
  - tier: Équipementier reconnu (transmission)
    description: Fabricants spécialisés en composants de boîtes automatiques. Kit complet généralement disponible avec filtre,
      joint de carter et parfois la vis de vidange.
  - tier: Kit filtre adaptable
    description: Option économique pour les boîtes standards à convertisseur de couple. Vérifier impérativement la référence
      de la boîte (pas seulement le modèle de véhicule), la compatibilité avec l'huile ATF utilisé
  brands:
    premium:
    - Mann Filter
    - Mahle/Knecht
    - Hengst
    standard:
    - Bosch
    - Purflux
    - WIX
    budget:
    - Ridex
    - Valeo
diagnostic:
  symptoms:
  - id: S1
    label: Passages de vitesses brutaux ou tardifs
    severity: confort
  - id: S2
    label: Vibrations lors des changements de rapport
    severity: confort
  - id: S3
    label: Boite qui patine sous charge
    severity: confort
  - id: S4
    label: Huile atf brune ou odeur brule
    severity: confort
  - id: S5
    label: Voyant temperature boite
    severity: confort
  causes:
  - lecture codes defaut obd et diagnostic electronique
  - identifier origine fuite et verifier joints
  - verifier equilibrage et fixations
  quick_checks:
  - 'Observer : passages de vitesses brutaux ou tardifs ?'
  - Vibrations lors des changements de rapport ?
  - 'Observer : boite qui patine sous charge ?'
  - 'Observer : huile atf brune ou odeur brule ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Passages de vitesses brutaux ou tardifs
  - Vibrations lors des changements de rapport
  - Boite qui patine sous charge
  - Huile atf brune ou odeur brule
  - Voyant temperature boite
  good_practices:
  - Remplacement systematique selon intervalle constructeur
  - Ne pas souffler a l air comprime (endommage le media filtrant)
  - Controle visuel a chaque vidange ou entretien
  - Verifier l etancheite du boitier apres remplacement
rendering:
  pgId: '416'
  intro_title: A quoi sert Filtre de boîte auto ?
  risk_title: Pourquoi remplacer Filtre de boîte auto a temps ?
  risk_explanation: '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
  risk_consequences:
  - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
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
  - question: Filtre boîte auto OE ou adaptable ?
    answer: Privilégiez l'OE ou OES (ZF, Valeo). La boîte auto est sensible, un filtre de qualité inférieure peut causer des
      dégâts coûteux.
  - question: Comment savoir si le filtre de boîte auto est HS ?
    answer: Passages de vitesses brutaux ou tardifs, patinage de la boîte, voyant boîte auto allumé, huile ATF foncée ou odeur
      de brûlé.
  - question: Tous les combien changer le filtre de boîte auto ?
    answer: Entre 60 000 et 100 000 km selon constructeur. Toujours le changer lors de la vidange de boîte. Certaines boîtes
      scellées n'ont pas de filtre accessible.
  - question: Peut-on changer le filtre de boîte auto soi-même ?
    answer: Déconseillé aux débutants. Nécessite de vidanger l'huile ATF, déposer le carter, remplacer le joint. Procédure
      de remplissage stricte.
  - question: Quelle erreur éviter avec le filtre de boîte auto ?
    answer: Ne jamais mélanger différentes huiles ATF. Respecter le niveau exact. Ne pas oublier le joint de carter. Éviter
      les vidanges par gravité seule.
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
doc_id: 0f91a914-79f1-5a52-bb45-b2d6a87fa87d
content_hash: sha256:e20e153509fb7475
lang: fr
variants:
- name: Filtre standard papier
  aliases:
  - papier
  - standard
  functional_differences:
  - Usage normal
  - Remplacement a chaque entretien
- name: Filtre performance lavable
  aliases:
  - sport
  - K&N
  - BMC
  - lavable
  functional_differences:
  - Reutilisable apres nettoyage
  - Pour usage sportif
location_on_vehicle:
  area: Compartiment moteur (air, huile) ou habitacle (pollen)
  access: Par le dessus (capot) ou depuis la boite a gants
  adjacent_parts:
  - boitier filtre
  - durite admission
  - collecteur
installation:
  difficulty: facile
  time: 10 a 30 min
  tools:
  - tournevis
  - cle a filtre (huile)
  - chiffon
  prerequisite: Moteur froid pour filtre a huile
phase5_enrichment:
  _source: contenu LLM — a revalider contre sources OEM
  _validation_status: pending_oem_validation
  _enriched_at: '2026-03-30'
  types_variants:
  - type: Filtre a tamis (interne)
    description: Tamis metallique ou synthetique dans le carter de boite, remplacable lors d'une vidange de BVA
    era: standard
  - type: Filtre externe (en ligne)
    description: Filtre sur la conduite de retour du radiateur de BVA, plus accessible
    era: certaines BVA
  technical_notes:
    intervalle: "60 000 a 80 000 km ou selon constructeur (certains disent 'a vie' = faux)"
    huile_bva: 'huile ATF specifique a la boite (DEXRON, MATIC, LT71141...) — ne PAS melanger les types'
    quantite_vidange: 'vidange partielle = 3-5L, vidange complete par rincage = 8-12L selon boite'
    temperature_huile: 'fonctionnement normal 80-100°C, max 150°C (au-dela = degradation acceleree)'
  materials:
  - composant: media
    materiau: feutre synthetique ou tamis metallique (inox ou laiton)
  - composant: joint
    materiau: caoutchouc ou liege (joint de carter BVA)
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le filtre de boîte automatique a pour fonction de filtrer l'huile ATF
    (Automatic Transmission Fluid) qui circule dans le circuit hydraulique de la
    boîte de vitesses automatique. Cette huile est à la fois un lubrifiant, un
    fluide de transmission de puissance et un vecteur de commande hydraulique
    pour les solénoïdes et les embrayages multidisques. Au fil du temps, l'huile
    ATF se charge en particules métalliques issues de l'usure des disques
    d'embrayage, des planétaires et des pignons. Le filtre retient ces
    particules en suspension avant qu'elles ne circulent vers les électrovannes
    de la boîte, dont les orifices sont de très faible dimension (quelques
    centièmes de millimètre). Un filtre colmaté réduit le débit d'huile vers ces
    composants et entraîne des dysfonctionnements de passage de vitesses. Le
    filtre de boîte automatique est généralement situé à l'intérieur du carter
    inférieur de la boîte, immergé dans l'huile ATF. Il peut prendre la forme :
    - D'un filtre à mailles métalliques (réutilisable après nettoyage sur
    certaines boîtes) - D'un filtre en papier ou en feutre (à usage unique, non
    nettoyable) - D'un filtre intégré au carter (inséparable, nécessite le
    remplacement du carter complet) La fonction de purification de l'huile
    assurée par le filtre protège directement les solénoïdes hydrauliques
    (électrovannes) et le corps de valve de la boîte, dont la réparation ou le
    remplacement représente un coût très élevé. Le remplacement du filtre se
    fait systématiquement lors de chaque vidange de la boîte automatique, entre
    60 000 et 100 000 km selon le constructeur.
  S2: >-
    Un filtre de boîte automatique colmaté ou une huile ATF dégradée génèrent
    des symptômes de passage de vitesses caractéristiques, qui s'aggravent
    progressivement si l'entretien n'est pas réalisé à temps. Ces signaux
    méritent une attention immédiate car la boîte automatique est un ensemble
    coûteux à réparer. Voici les symptômes à surveiller : - Passages de vitesses
    brutaux ou tardifs : la boîte passe les rapports avec un choc perceptible,
    ou attend trop longtemps avant de monter ou descendre un rapport. C'est le
    signe le plus fréquent d'une huile ATF dégradée ou d'un filtre colmaté
    réduisant la pression hydraulique vers les solénoïdes. - Vibrations lors des
    changements de rapport : un à-coup mécanique se produit lors de chaque
    changement de vitesse. Les disques d'embrayage de la boîte ne s'engagent pas
    progressivement, ce qui indique un manque de pression hydraulique ou une
    huile chargée en particules. - Boîte qui patine sous charge : à
    l'accélération en montée ou lors d'un dépassement, le moteur monte en régime
    sans que la vitesse du véhicule suive. La boîte "glisse", signe d'un
    embrayage multidisque qui ne parvient pas à transmettre la puissance moteur
    faute de pression hydraulique suffisante. - Huile ATF brune ou avec odeur de
    brûlé : une huile ATF saine est rouge et transparente. Une couleur brune ou
    noire avec une odeur de brûlé indique une dégradation thermique avancée,
    souvent causée par des passages de vitesses répétés avec une pression
    insuffisante ayant surchauffé les disques. - Voyant de température de boîte
    allumé : un filtre obstrué réduit le refroidissement de l'huile et provoque
    une surchauffe de la boîte. Ce voyant est un signal d'alarme qui exige un
    arrêt immédiat pour protéger la boîte de dommages irréversibles.
  S3: >-
    Le filtre de boîte automatique est une pièce strictement spécifique à chaque
    boîte et à chaque véhicule. Les boîtes automatiques sont conçues par des
    fabricants spécialisés (ZF, Aisin, Jatco, GM) et chaque référence de filtre
    est adaptée à un modèle précis de boîte. Voici les critères de sélection
    indispensables : - Marque et modèle du véhicule : premier critère
    obligatoire. La même motorisation peut être couplée à différentes boîtes
    automatiques selon les années ou les marchés, ce qui implique des filtres
    différents. - Année de production et code boîte : le code de la boîte
    automatique (gravé sur le carter ou lisible dans la documentation technique)
    permet d'identifier avec certitude le filtre exact à commander. Un même
    modèle de véhicule peut avoir reçu plusieurs boîtes différentes au fil des
    millésimes. - Type de filtre adapté à la boîte (mailles métalliques ou
    papier) : certaines boîtes anciennes utilisent un filtre à mailles
    nettoyable. Les boîtes modernes utilisent un filtre papier ou feutre à usage
    unique. Ne jamais monter un filtre nettoyable à la place d'un filtre papier
    si le constructeur spécifie un filtre jetable. - Joint de carter : lors du
    remplacement du filtre, le joint du carter de boîte doit impérativement être
    remplacé simultanément. Ne pas commander de filtre sans le joint
    correspondant. - Qualité OE ou OES (ZF, Valeo, Bosch) : la boîte automatique
    est extrêmement sensible à la qualité du filtrage. Un filtre de qualité
    inférieure avec une porosité non conforme peut laisser passer des particules
    qui endommagent les solénoïdes. Toujours choisir une marque équipementier
    reconnue. - Compatibilité avec l'huile ATF spécifiée : vérifier que le
    filtre est compatible avec le grade d'huile ATF spécifié par le constructeur
    de la boîte (Dexron, Mercon, ZF Lifeguard, Esso ATF, etc.). Certains filtres
    sont conçus pour des huiles synthétiques spécifiques. - Boîtes "sealed" sans
    filtre accessible : certaines boîtes automatiques modernes (dites "scellées
    à vie") n'ont pas de filtre accessible depuis l'extérieur. Vérifier ce point
    dans la documentation technique avant de commander. Pour aller plus loin :
    consultez notre guide d'achat filtre de boîte auto — comparatif marques,
    critères de choix et prix.
  S4_DEPOSE: >-
    Le remplacement du filtre de boîte automatique est une opération d'entretien
    délicate qui exige de respecter scrupuleusement les procédures de vidange et
    de remplissage de l'huile ATF. Une erreur de niveau d'huile ou un mauvais
    joint de carter peut provoquer une panne grave de la boîte. Voici la
    procédure générale : - Vérifier la documentation technique : avant
    d'intervenir, s'assurer que la boîte automatique du véhicule dispose d'un
    filtre accessible et d'une procédure de vidange standard. Certaines boîtes
    "scellées à vie" nécessitent un outillage spécial et une procédure de
    remplissage assistée par calculateur. - Préparer le matériel : bac de
    vidange de capacité suffisante (la boîte peut contenir 4 à 8 litres d'huile
    ATF selon le modèle), joint de carter neuf, filtre neuf, huile ATF du grade
    exact spécifié. Ne jamais utiliser une huile ATF différente de celle
    prescrite. - Mettre le véhicule en température : effectuer un court trajet
    de 5 à 10 minutes pour chauffer l'huile ATF à 60-80°C, ce qui améliore
    l'écoulement lors de la vidange. Couper le moteur et sécuriser le véhicule
    sur chandelles. - Placer le bac de vidange et retirer le bouchon de vidange
    : si un bouchon de vidange est présent sur le carter, le retirer. Sinon,
    dévisser progressivement les vis du carter en commençant par les coins pour
    faire basculer le carter et laisser l'huile s'écouler progressivement. -
    Déposer le carter de boîte : retirer les vis de fixation du carter en
    alternant le dévissage pour éviter de déformer le carter. Nettoyer
    soigneusement les surfaces d'appui du carter et du plan de joint de la
    boîte. - Retirer et remplacer le filtre : déclipser ou dévisser l'ancien
    filtre selon son mode de fixation. Installer le nouveau filtre dans le même
    sens, en s'assurant que la bague d'étanchéité (si présente) est correctement
    engagée sur le corps de valve. - Poser le joint de carter neuf et revisser
    le carter : ne jamais réutiliser un joint de carter usagé. Serrer les vis de
    carter au couple spécifié (généralement 6 à 10 N.m selon les modèles) en
    croix. - Remplir avec l'huile ATF spécifiée : la procédure de remplissage
    est critique. Sur la plupart des boîtes, le niveau se contrôle par un
    bouchon de niveau sur le côté du carter, avec le moteur en marche et la
    boîte à température. Respecter exactement la procédure constructeur. -
    Vérifier l'étanchéité et le niveau après premier trajet : inspecter le
    carter pour tout suintement d'huile après le premier trajet de validation.
    Contrôler à nouveau le niveau d'huile selon la procédure constructeur.
  S4_REPOSE: >-
    Après la dépose du filtre usagé et le nettoyage du carter, le remontage du
    filtre de boîte automatique exige une rigueur absolue sur les couples de
    serrage et la procédure de remplissage en huile ATF. Une erreur à ce stade
    peut provoquer une panne de boîte immédiate ou différée. - Inspecter et
    nettoyer soigneusement le fond du carter et les aimants : les aimants
    permanents fixés dans le fond du carter récupèrent les particules ferriques
    en suspension dans l'huile. Nettoyer les aimants avec un chiffon propre et
    les repositionner. Inspecter les dépôts au fond du carter : des copeaux
    métalliques importants signalent une usure grave de la boîte nécessitant un
    diagnostic approfondi. - Installer le nouveau filtre dans le corps de valve
    en respectant le sens et l'engagement de la bague : le filtre doit s'engager
    correctement dans le corps de valve ou le conduit d'aspiration de la pompe.
    La bague d'étanchéité du filtre doit être correctement positionnée et ne pas
    être en appui sur un angle ou une arête. Un mauvais engagement du filtre
    crée une aspiration d'air dans la pompe. - Poser un joint de carter
    strictement neuf : ne jamais réutiliser le joint de carter même s'il semble
    intact. Certains joints de boîte auto utilisent de la pâte à joint (silicone
    RTV) plutôt qu'un joint solide — respecter le type et la quantité préconisés
    par le constructeur. - Remettre le carter en place et serrer les vis en
    croix au couple constructeur : serrer progressivement et en croix pour
    comprimer uniformément le joint. Le couple de serrage est généralement de 6
    à 10 N.m selon le modèle — ne jamais utiliser une clé à choc sur les vis de
    carter de boîte. - Revisser le bouchon de vidange s'il est séparé du carter
    : monter un joint cuivre neuf sur le bouchon de vidange et serrer au couple
    prescrit (généralement 30 à 40 N.m). Une rondelle cuivre réutilisée provoque
    un suintement d'huile difficile à stopper sans dépose du carter. - Procéder
    au remplissage de l'huile ATF en respectant strictement la procédure
    constructeur : la procédure de remplissage d'une boîte automatique est
    spécifique à chaque modèle. Elle implique généralement : verser une quantité
    de base définie, démarrer le moteur, passer les rapports, puis ajuster le
    niveau avec le moteur chaud à la bonne température (entre 35°C et 45°C selon
    le constructeur) via le bouchon de niveau latéral. - Ne jamais mélanger deux
    spécifications d'huile ATF différentes : chaque boîte automatique est conçue
    pour une huile ATF précise (Dexron VI, Shell ATF M-1375.4, Toyota T-IV,
    etc.). Un mélange même partiel peut provoquer la perte de friction des
    embrayages internes et rendre la boîte inutilisable. - Vérifier l'étanchéité
    après le premier trajet : effectuer un trajet de 15 à 20 minutes incluant
    plusieurs passages de rapports et des arrêts. Garer le véhicule sur une
    surface propre et inspecter le dessous pour tout suintement d'huile ATF au
    niveau du carter. Contrôler à nouveau le niveau d'huile selon la procédure
    constructeur. - Effacer les codes défaut éventuels avec un outil OBD : si
    des codes défaut liés à la boîte automatique (glissement, rapport manquant,
    température) s'étaient enregistrés avant l'intervention, les effacer après
    la repose. Confirmer l'absence de nouveaux codes après le trajet de
    validation.
  S5: >-
    La vidange de boîte automatique avec remplacement de filtre est une
    opération où les erreurs sont fréquentes et souvent coûteuses. La boîte
    automatique ne tolère pas les approximations. Voici les pièges à éviter
    absolument : - Mélanger différentes huiles ATF : c'est l'erreur la plus
    grave et la plus fréquente. Chaque fabricant de boîte spécifie une huile ATF
    avec une formulation chimique précise. Mélanger du Dexron III avec du Mercon
    V, ou une huile ZF Lifeguard avec une huile générique, provoque une
    dégradation chimique de l'huile et des dommages aux joints toriques et aux
    disques d'embrayage. Toujours vidanger complètement avant de remplir avec la
    nouvelle huile. - Ne pas remplacer le joint de carter lors du remplacement
    du filtre : un joint de carter usagé recomprimé avec un nouveau serrage ne
    garantit pas l'étanchéité. Une fuite d'huile ATF même minime peut vider la
    boîte en quelques centaines de kilomètres et provoquer une destruction
    complète de la boîte par manque de lubrification. - Effectuer une vidange
    par gravité seule sans rinçage : la vidange par gravité ne récupère que 40 à
    60 % de l'huile ATF contenue dans la boîte (une partie reste dans le
    convertisseur de couple et le circuit hydraulique). Sur les boîtes très
    encrassées, une simple vidange partielle laisse en place l'ancienne huile
    dégradée qui contaminera la nouvelle. - Se tromper sur le niveau d'huile ATF
    : un niveau trop bas ou trop haut est également néfaste. Un niveau
    insuffisant provoque une cavitation de la pompe hydraulique et un patinage
    des embrayages. Un niveau trop haut provoque un moussage de l'huile, qui
    perd ses propriétés hydrauliques et cause des passages de vitesses
    irréguliers. - Ignorer les boîtes "sealed" sans procédure de vidange
    standard : tenter de vidanger une boîte scellée sans outillage spécifique
    (pompe de remplissage et adaptateur) aboutit à un niveau d'huile incorrect
    après remplissage, souvent trop bas, avec risque de casse.
  S6: >-
    Après le remplacement du filtre de boîte automatique et la
    vidange/remplissage d'huile ATF, une série de contrôles est indispensable
    avant de rendre le véhicule opérationnel. Ces vérifications permettent de
    détecter une erreur de niveau, une fuite ou un dysfonctionnement résiduel :
    - Contrôle du niveau d'huile ATF à température de service : avec le moteur
    au ralenti, la boîte en position N ou P et l'huile à la bonne température
    (60 à 80°C selon le constructeur), vérifier le niveau par la vis de niveau
    sur le carter ou la jauge selon le système. La procédure exacte de contrôle
    est spécifique à chaque boîte. - Inspection visuelle du carter pour fuite :
    après le premier démarrage, inspecter attentivement le tour du carter de
    boîte et le bouchon de vidange. Aucune trace d'huile ATF ne doit être
    visible. Une fuite, même minime, doit être corrigée immédiatement. - Test
    des passages de vitesses sur route : effectuer un trajet d'essai en
    sollicitant la boîte sur tous les rapports, y compris les passages manuels
    si disponibles. Les changements de vitesse doivent être progressifs et sans
    choc. Des passages brutaux résiduels peuvent indiquer un niveau d'huile
    incorrect ou la présence d'air dans le circuit. - Lecture OBD pour
    vérification des codes de boîte : certains calculateurs de boîte automatique
    mémorisent des codes défaut liés à des pressions hydrauliques hors plage.
    Effectuer une lecture OBD après le trajet d'essai pour s'assurer qu'aucun
    code de type P07XX ou P08XX n'est apparu. - Vérification après 500 km :
    contrôler à nouveau le niveau d'huile ATF et inspecter le carter après 500
    km d'utilisation normale pour confirmer l'absence de fuite et la stabilité
    du niveau.
  S7: >-
    Le filtre de boîte automatique s'intègre dans un ensemble d'entretien
    complet de la boîte. Ces composants doivent être vérifiés ou remplacés
    simultanément : - Boîte automatique — un filtre colmaté est souvent le
    symptôme d'une usure interne avancée de la boîte. Si les dépôts au fond du
    carter sont importants (lamelles d'embrayage, copeaux), un remplacement de
    filtre seul ne résoudra pas le problème — faire diagnostiquer la boîte par
    un spécialiste. - Huile ATF (huile de boîte automatique) — le filtre et
    l'huile ATF se remplacent ensemble systématiquement lors d'une vidange de
    boîte. Utiliser exclusivement la spécification d'huile ATF préconisée par le
    constructeur (ne jamais mélanger des spécifications différentes). - Joint de
    carter de boîte automatique — le joint de carter doit être remplacé à chaque
    dépose du carter. Un joint de carter réutilisé provoque systématiquement un
    suintement d'huile. Prévoir le joint dans la commande de pièces avant
    l'intervention. - Radiateur d'huile de boîte automatique — refroidit l'huile
    ATF lors des trajets intensifs (remorquage, circulation urbaine). Un
    radiateur colmaté provoque une surchauffe de la boîte identique à celle
    causée par un filtre encrassé. Contrôler le circuit de refroidissement de
    boîte lors de la vidange.
  S8: >-
    Tous les combien faut-il changer le filtre de boîte automatique ?
    L'intervalle de remplacement varie entre 60 000 et 100 000 km selon le
    constructeur de la boîte. Certains constructeurs ne préconisent pas de
    vidange (boîtes dites "sealed à vie"), mais la pratique démontre qu'une
    vidange à 80 000-100 000 km prolonge significativement la durée de vie de la
    boîte. Le filtre se remplace systématiquement lors de chaque vidange d'huile
    ATF, jamais seul. Peut-on changer le filtre de boîte auto soi-même ?
    L'opération est déconseillée aux débutants en mécanique. La difficulté
    principale réside dans la procédure de remplissage de l'huile ATF, qui doit
    se faire avec le moteur en marche et l'huile à température. Un niveau
    incorrect peut provoquer des dommages graves à la boîte. De plus, certaines
    boîtes nécessitent un outil de diagnostic pour réinitialiser les paramètres
    d'adaptation après vidange. Pour les boîtes récentes, l'intervention en
    atelier spécialisé est fortement recommandée. Quelle huile ATF utiliser lors
    du remplacement du filtre ? Utiliser exclusivement l'huile ATF spécifiée par
    le constructeur de la boîte (ZF Lifeguard, Aisin ATF, Dexron VI, Mercon LV,
    etc.). Cette information figure dans le carnet d'entretien du véhicule ou
    sur l'étiquette apposée sur la boîte. Ne jamais utiliser une huile ATF
    "universelle" ou un grade différent de celui prescrit — les formulations
    chimiques sont incompatibles et peuvent dégrader les joints et les disques
    d'embrayage en quelques milliers de kilomètres. Quelles erreurs éviter
    absolument lors de cette opération ? Ne jamais mélanger deux marques ou deux
    grades d'huile ATF différents dans la boîte. Ne jamais oublier de remplacer
    le joint de carter en même temps que le filtre. Ne pas se fier uniquement à
    la vidange par gravité sur les boîtes à convertisseur de couple — une partie
    de l'ancienne huile reste piégée dans le convertisseur. Respecter
    scrupuleusement le couple de serrage des vis de carter pour ne pas déformer
    le carter ni créer de fuite.
  META: >-
    {"og_title": "Filtre boîte automatique : symptômes et remplacement",
    "meta_title": "Filtre boîte auto : quand changer ? Signes et vidange |
    AutoMecanik", "gate_report": "PASS", "schema_type": "HowTo",
    "og_description": "Passages brutaux, patinage, ATF brûlée : guide diagnostic
    et remplacement du filtre de boîte auto.", "primary_intent": "diagnostic",
    "char_count_desc": 127, "char_count_title": 57, "meta_description":
    "Passages brutaux, boîte qui patine ou huile ATF brunâtre ? Guide pour
    diagnostiquer et remplacer le filtre de boîte automatique."}
---

# Filtre de boîte auto - Guide Diagnostic Complet

## Fonction et Rôle

Filtrer l'huile de la boite automatique

**Actions principales:** filtrer, retenir, purifier

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- passages de vitesses brutaux ou tardifs
- vibrations lors des changements de rapport
- boite qui patine sous charge
- huile atf brune ou odeur brule
- voyant temperature boite

## Procédure de Diagnostic

Pour diagnostiquer un problème de filtre de boîte auto:

1. **Inspection visuelle** - Examiner l'état du filtre de boîte auto
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- boite-automatique
- huile-bva

## Critères de Compatibilité

Pour commander le bon filtre de boîte auto, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "filtration parfaite"

## FAQ

**Filtre boîte auto OE ou adaptable ?**
Privilégiez l'OE ou OES (ZF, Valeo). La boîte auto est sensible, un filtre de qualité inférieure peut causer des dégâts coûteux.

**Comment savoir si le filtre de boîte auto est HS ?**
Passages de vitesses brutaux ou tardifs, patinage de la boîte, voyant boîte auto allumé, huile ATF foncée ou odeur de brûlé.

**Tous les combien changer le filtre de boîte auto ?**
Entre 60 000 et 100 000 km selon constructeur. Toujours le changer lors de la vidange de boîte. Certaines boîtes scellées n'ont pas de filtre accessible.

**Peut-on changer le filtre de boîte auto soi-même ?**
Déconseillé aux débutants. Nécessite de vidanger l'huile ATF, déposer le carter, remplacer le joint. Procédure de remplissage stricte.

**Quelle erreur éviter avec le filtre de boîte auto ?**
Ne jamais mélanger différentes huiles ATF. Respecter le niveau exact. Ne pas oublier le joint de carter. Éviter les vidanges par gravité seule.


## Symptomes supplementaires

<!-- materialized-from-db diagnostic/transmission-boite.md 2026-02-15 -->
### Diagnostic - Transmission et boîte de vitesses

# Transmission et boîte de vitesses - Diagnostic complet

## Boîte manuelle

### Craquement au passage de vitesse
- **Synchroniseurs usés** : Craquement surtout sur un rapport précis (souvent 2ème ou 3ème). Pire à froid, s'améliore à chaud.
- **Huile de boîte inadaptée ou usée** : Vidange de boîte à effectuer (75W-80 ou 75W-90 selon constructeur).
- **Câble ou timonerie de commande usé** : Passage imprécis, sensation de flou dans le levier.

### Vitesse qui saute
- **Fourchette de sélection usée** : La vitesse se désengage spontanément sous charge.
- **Ressort de verrouillage cassé** : Le rapport ne tient plus en position.

### Bruit de roulement en boîte
- **Roulement d'arbre primaire usé** : Sifflement continu qui disparaît quand on appuie sur l'embrayage.
- **Roulement de sortie** : Bruit proportionnel à la vitesse du véhicule.

## Boîte automatique

### À-coups ou patinage
- **Niveau d'huile ATF incorrect** : Vérifier le niveau à chaud, moteur tournant au point mort.
- **Huile ATF usée** : Couleur marron foncé au lieu de rouge. Vidange recommandée.
- **Convertisseur de couple usé** : Patinage au démarrage, surchauffe de l'huile.

### Passage de rapports brutal
- **Calculateur de boîte** : Réinitialisation des adaptations parfois nécessaire.
- **Électrovannes de commande** : Corps de vannes encrassé ou électrovanne bloquée.

## Cardans et transmission

### Claquement en virage
- **Soufflet de cardan déchiré** : Graisse projetée visible sur la roue intérieure. Le cardan tourne sans lubrification.
- **Croisillon de cardan usé** : Claquement sec en accélération ou décélération dans les virages.

### Vibration à l'accélération
- **Cardan voilé** : Vibration proportionnelle à la vitesse.
- **Silent-bloc de transmission usé** : Vibrations transmises dans l'habitacle.

## Quand consulter un professionnel

- Boîte automatique en mode dégradé (bloquée sur un rapport)
- Fuite d'huile de boîte importante
- Craquement systématique sur tous les rapports
- Cardan cassé (roue qui ne tourne plus)
