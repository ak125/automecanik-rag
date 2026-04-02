---
category: refroidissement
slug: bouchon-de-radiateur
title: Bouchon de radiateur
pg_id: 548
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
  last_enriched_by: skill:phase5-vague6
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Fermer le radiateur et reguler la pression du circuit
  must_be_true:
  - fermer
  - reguler
  - proteger
  must_not_contain:
  - injection
  - freinage
  - embrayage
  - distribution
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - radiateur-de-refroidissement
  - pompe-a-eau
  - thermostat
  - durite-de-refroidissement
  - vase-d-expansion
  - ventilateur-de-refroidissement
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
  - ❌ "refroidissement optimal"
  cost_range:
    min: 1500
    max: 4000
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    description: Bouchon fourni par l'équipementier d'origine du radiateur ou du vase d'expansion. Pression de tarage identique
      aux spécifications constructeur.
  - tier: Équivalent OE — spécialistes refroidissement
    description: Fabricants reconnus en composants de circuit de refroidissement. Soupapes de pression calibrées et joints
      testés en température.
  - tier: Adaptables
    description: Bouchons de radiateur génériques. La valeur de pression de tarage doit impérativement correspondre à celle
      préconisée par le constructeur pour le véhicule concerné.
  brands:
    premium:
    - Behr/Mahle
    - Gates
    standard:
    - Valeo
    - NRF
    - Febi
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Fuite de liquide par le bouchon
    severity: confort
  - id: S2
    label: Surchauffe moteur sans fuite visible
    severity: confort
  - id: S3
    label: Pression excessive dans le circuit
    severity: confort
  causes:
  - identifier origine fuite et verifier joints
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  - 'Usure ou defaillance causant : fuite de liquide par le bouchon'
  quick_checks:
  - Fuite de liquide par le bouchon ?
  - 'Observer : surchauffe moteur sans fuite visible ?'
  - 'Observer : pression excessive dans le circuit ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Fuite de liquide par le bouchon
  - Surchauffe moteur sans fuite visible
  - Pression excessive dans le circuit
  good_practices:
  - Controle du niveau de liquide de refroidissement a froid chaque mois
  - Remplacement du liquide selon preconisation constructeur (2-5 ans)
  - Verification des durites et colliers a chaque revision
  - Purge du circuit apres toute intervention sur le refroidissement
rendering:
  pgId: '548'
  intro_title: A quoi sert Bouchon de radiateur ?
  risk_title: Pourquoi remplacer Bouchon de radiateur a temps ?
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
  - question: Comment choisir Bouchon de radiateur compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Bouchon de radiateur ?
    answer: En cas de fuite de liquide par le bouchon ou de degradation mesurable, il faut controler rapidement avant panne
      secondaire.
  - question: Puis-je monter Bouchon de radiateur sans verification atelier ?
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
doc_id: f61c4e2c-0b41-5b39-85a4-e45675d22360
content_hash: sha256:dc1e94a1beaf168c
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
  area: Face avant du vehicule (radiateur) et bloc moteur
  access: Par le dessus (capot) ou face avant
  adjacent_parts:
  - radiateur
  - durites
  - pompe a eau
  - thermostat
installation:
  difficulty: moyen
  time: 30min a 2h
  tools:
  - tournevis
  - pince de serrage
  - bac de recuperation
  prerequisite: Moteur froid, circuit vidange avant depose
phase5_enrichment:
  _source: contenu LLM — a revalider contre sources OEM
  _validation_status: pending_oem_validation
  _enriched_at: '2026-03-30'
  technical_notes:
    pression: 'bouchon tare 1,0-1,5 bars — remplacer par un bouchon de meme pression'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le bouchon de radiateur ferme l'orifice de remplissage du radiateur et joue
    un rôle actif dans la régulation de la pression du circuit de
    refroidissement. Ce composant en apparence simple est en réalité une soupape
    de pression calibrée, indispensable à l'efficacité thermique du moteur. Le
    circuit de refroidissement fonctionne en système fermé sous pression
    positive. Cette surpression, généralement calibrée entre 0,9 et 1,3 bar
    selon les constructeurs, élève le point d'ébullition du liquide de
    refroidissement au-delà de 100 °C : à 1,2 bar, le liquide ne bout plus à 100
    °C mais à environ 120 °C, ce qui permet au moteur de fonctionner à des
    températures plus élevées sans risque de vaporisation. Le bouchon contient
    deux soupapes intégrées pour assurer cette régulation. La soupape de
    surpression s'ouvre lorsque la pression dans le circuit dépasse la valeur
    calibrée : elle laisse s'échapper du liquide vers le vase d'expansion pour
    éviter toute rupture de durite ou de joint. La soupape de dépression
    fonctionne en sens inverse : lorsque le moteur refroidit après l'arrêt, la
    contraction thermique du liquide crée une dépression ; la soupape s'ouvre
    alors pour permettre au liquide de refluer depuis le vase d'expansion vers
    le radiateur et maintenir le circuit plein. Sans ce mécanisme, de l'air
    pourrait s'introduire dans le circuit et créer des poches de vapeur
    responsables de surchauffes localisées.
  S2: >-
    Un bouchon de radiateur défaillant perturbe la régulation thermique du
    moteur. Ses symptômes peuvent être discrets ou soudains selon le mode de
    défaillance (soupape bloquée ouverte ou fermée). Voici les signes à
    identifier. - Fuite de liquide de refroidissement par le bouchon : des
    traces de liquide coloré (vert, rose ou orange) autour du bouchon ou sur le
    radiateur indiquent que le joint d'étanchéité du bouchon est défectueux ou
    que la soupape s'ouvre à une pression trop basse. La pression du circuit est
    insuffisante et le moteur risque une surchauffe par bouillonnement
    prématuré. - Surchauffe moteur sans fuite visible : si la soupape de
    surpression est bloquée fermée, la pression monte anormalement dans le
    circuit. Les durits se gonflent sous la pression excessive et le liquide
    peut atteindre des températures critiques. Le voyant de température s'affole
    malgré un niveau de liquide correct. - Pression excessive dans le circuit
    après refroidissement : si les durits restent dures et gonflées après
    l'arrêt du moteur et son refroidissement complet, la soupape de dépression
    ne fonctionne plus et le circuit est sur-pressurisé en permanence. - Niveau
    de liquide qui baisse sans trace de fuite extérieure visible : une soupape
    de surpression qui s'ouvre trop tôt laisse fuir du liquide vers le vase
    d'expansion à une pression inférieure à la valeur calibrée. Le liquide
    déborde mais s'évapore ensuite, laissant croire à une perte inexpliquée. -
    Vase d'expansion qui déborde régulièrement : si le bouchon libère le liquide
    à une pression trop basse, le vase se remplit trop souvent. Ce symptôme est
    souvent confondu avec une fuite de joint de culasse, mais un bouchon
    défaillant est bien plus fréquent et doit être vérifié en premier.
  S3: >-
    Le bouchon de radiateur doit correspondre exactement à la pression calibrée
    du circuit de votre véhicule. Un bouchon de mauvaise pression d'ouverture
    modifie les conditions thermiques du moteur. Voici les points à vérifier. -
    Pression d'ouverture de la soupape : c'est le critère technique le plus
    important. Cette valeur en bar est gravée ou imprimée sur le bouchon
    d'origine (exemple : 1,1 bar). Ne jamais monter un bouchon de pression
    supérieure à la préconisation constructeur car les durits et le radiateur ne
    sont pas conçus pour des pressions plus élevées. - Diamètre et pas du
    filetage ou de la baïonnette : les bouchons se fixent par vissage ou par
    quart de tour (baïonnette). Le diamètre et la longueur du filetage ou de la
    baïonnette sont spécifiques à chaque modèle de radiateur. Un bouchon de
    mauvais diamètre ne ferme pas correctement et crée une fuite. - Marque,
    modèle et année du véhicule : utiliser le sélecteur de véhicule pour
    identifier la référence exacte. Deux versions du même modèle avec
    motorisations différentes peuvent utiliser des bouchons de pression
    différente. - État du col de remplissage du radiateur : avant de monter un
    bouchon neuf, inspecter l'état du col de remplissage. Des entailles ou des
    déformations sur le col empêchent le bouchon de créer une étanchéité
    correcte, quelle que soit la qualité du bouchon neuf. - Marque de
    remplacement : les bouchons Stant, Wahler, Behr, Magneti Marelli ou Gates
    correspondent aux spécifications OEM. Évitez les bouchons sans marque
    identifiable dont la pression d'ouverture réelle n'est pas garantie. -
    Présence d'un manomètre de test : si vous souhaitez tester la pression
    d'ouverture du bouchon déposé avant remplacement, des adaptateurs de test à
    pression sont disponibles chez les équipementiers. Cette vérification prend
    moins de 5 minutes et confirme le diagnostic. Pour aller plus loin :
    consultez notre guide d'achat bouchon de radiateur — comparatif marques,
    critères de choix et prix.
  S4_DEPOSE: >-
    Le remplacement du bouchon de radiateur est l'une des opérations les plus
    simples de l'entretien automobile, mais elle comporte un risque de brûlure
    grave si elle est effectuée sur un moteur chaud. Respectez impérativement
    les consignes de sécurité thermique. - Attendre le refroidissement complet
    du moteur : ne jamais ouvrir le bouchon de radiateur ou le bouchon du vase
    d'expansion sur un moteur chaud ou tiède. Le liquide est sous pression entre
    90 °C et 110 °C ; l'ouverture brutale provoque une projection de vapeur et
    de liquide bouillant. Attendre au minimum 2 heures après l'arrêt du moteur,
    ou jusqu'à ce que le radiateur soit froid au toucher. - Placer un chiffon
    épais sur le bouchon avant ouverture : même sur un moteur froid, placer un
    chiffon épais par-dessus le bouchon avant de le desserrer. Tourner le
    bouchon d'un quart de tour uniquement pour libérer la pression résiduelle
    éventuelle, puis attendre avant de retirer complètement le bouchon. -
    Déposer le bouchon usé : desserrer le bouchon d'un quart de tour
    supplémentaire (ou dévisser selon le type de fixation) et l'extraire.
    Observer l'état du joint d'étanchéité : s'il est fissuré, aplati ou durci,
    cela confirme la nécessité du remplacement. - Inspecter le col de
    remplissage : examiner l'état du col en aluminium ou en plastique du
    radiateur. Vérifier l'absence de déformation, de fissure ou d'ébréchure sur
    les bords du col. Un col endommagé nécessite le remplacement du radiateur,
    pas uniquement du bouchon. - Vérifier le niveau de liquide de
    refroidissement : profiter de l'opération pour compléter le niveau si
    nécessaire avec le liquide de refroidissement adapté (couleur et formulation
    correspondant au liquide d'origine : G11, G12, G13 selon le constructeur).
    Ne jamais mélanger des liquides de formulations différentes. - Mise en place
    du bouchon neuf : poser le bouchon neuf en le tournant dans le sens horaire
    jusqu'au clic d'encliquetage (baïonnette) ou jusqu'au couple de serrage
    manuel recommandé (vissage). Ne pas forcer : un bouchon sur-serré déforme le
    col en plastique. - Test de pression à froid puis en chauffe : démarrer le
    moteur et laisser monter en température. Observer le bouchon depuis une
    distance de sécurité pour détecter toute fuite active dès la mise en
    pression du circuit. Contrôler également l'état du vase d'expansion.
  S4_REPOSE: >-
    Après vidange ou remplacement du circuit de refroidissement, la repose du
    bouchon de radiateur est l'étape finale qui conditionne l'étanchéité et la
    régulation de pression de l'ensemble du circuit. Une repose mal effectuée
    peut provoquer des fuites ou une surchauffe moteur à la première mise en
    chauffe. - Vérifier l'état du col de remplissage avant repose : avant de
    visser le nouveau bouchon, inspecter minutieusement le col en plastique ou
    en aluminium du radiateur. Les bords doivent être nets, sans ébréchure ni
    déformation. Passer un chiffon propre pour éliminer tout résidu de liquide
    de refroidissement séché ou dépôt calcaire sur la portée d'étanchéité. -
    Contrôler le niveau de liquide de refroidissement : si le circuit a été
    ouvert pour d'autres travaux, vérifier que le niveau est à la bonne hauteur
    dans le radiateur avant de fermer. Ajouter du liquide adapté (G11, G12 ou
    G13 selon la couleur d'origine) si nécessaire. Ne jamais mélanger des
    formulations différentes. - Positionner le bouchon neuf sur le col : aligner
    les encoches du bouchon avec les ergots du col (système à baïonnette) ou
    engager les premiers filets à la main (système vissé). S'assurer que le
    joint d'étanchéité du bouchon est en place et qu'il repose bien à plat sur
    la portée du col. - Verrouiller le bouchon jusqu'au clic : tourner dans le
    sens horaire jusqu'à l'encliquetage audible et tactile (baïonnette) ou
    jusqu'au contact ferme sans forcer (vissé). Un bouchon correctement posé ne
    doit plus pouvoir être retiré par une simple traction vers le haut sans
    manœuvre de déverrouillage. - Vérifier la pression de tarage du bouchon neuf
    : le bouchon de radiateur est calibré pour une pression d'ouverture précise
    (généralement entre 0,8 et 1,5 bar selon le constructeur). S'assurer que la
    pression gravée ou indiquée sur le bouchon correspond à la valeur
    constructeur du véhicule. Un bouchon sous-calibré laisse s'échapper le
    liquide avant la température nominale. - Faire tourner le moteur jusqu'à la
    température normale : démarrer le moteur et laisser monter en température
    jusqu'à ce que le thermostat s'ouvre (généralement 85-95 °C). Surveiller le
    bouchon depuis une distance de sécurité. Aucune fuite ni vapeur ne doit
    apparaître autour du bouchon sous pression. - Contrôler le niveau à froid
    après refroidissement : une fois le moteur revenu à froid (minimum 1 heure),
    vérifier à nouveau le niveau dans le radiateur et dans le vase d'expansion.
    Une légère baisse à froid après la première chauffe est normale (air dans le
    circuit) ; compléter si nécessaire. Si le niveau chute de façon
    significative, rechercher une fuite dans le circuit.
  S5: >-
    Bien que le remplacement du bouchon de radiateur soit simple, certaines
    erreurs entraînent des dommages graves sur le circuit de refroidissement ou
    mettent en danger la sécurité de l'intervenant. - Ouvrir le bouchon sur un
    moteur chaud : c'est l'erreur la plus dangereuse. Le liquide sous pression
    est projeté violemment lors de l'ouverture du bouchon sur un moteur à
    température de fonctionnement. Conséquence : brûlures graves au visage et
    aux mains, dommages aux éléments sous le capot exposés à la projection de
    liquide bouillant. - Monter un bouchon de pression incorrecte : un bouchon
    dont la pression d'ouverture est inférieure à la préconisation laisse le
    circuit travailler à basse pression, abaissant le point d'ébullition du
    liquide. Conséquence : surchauffe prématurée à régime élevé, bullage dans le
    circuit et risque de joint de culasse détérioré à terme. - Ne pas inspecter
    l'état du col de remplissage : poser un bouchon neuf sur un col fissuré ou
    déformé ne résout pas le problème d'étanchéité. Conséquence : fuite
    persistante et remplacement du bouchon inutile. - Mélanger des liquides de
    refroidissement incompatibles lors du complément : profiter du changement de
    bouchon pour compléter le niveau avec un liquide de couleur différente ou de
    formulation incompatible dégrade les propriétés anticorrosion. Conséquence :
    formation de dépôts, colmatage du radiateur et réduction de l'efficacité
    thermique. - Sous-serrer le bouchon neuf : un bouchon non correctement
    verrouillé sur la baïonnette peut être éjecté lors de la mise en pression du
    circuit. Conséquence : perte de liquide de refroidissement en roulage et
    risque de surchauffe rapide.
  S6: >-
    Après la pose du bouchon de radiateur neuf, les contrôles suivants
    permettent de confirmer l'étanchéité et la bonne régulation de pression du
    circuit de refroidissement. - Contrôle visuel du verrouillage du bouchon :
    s'assurer que le bouchon est correctement engagé dans sa position
    verrouillée (clic audible pour les systèmes à baïonnette, ou résistance
    manuelle confirme le serrage pour les systèmes vissés). - Vérification du
    niveau de liquide à froid : contrôler le niveau dans le vase d'expansion
    (repères MIN et MAX) avant de démarrer. Compléter si nécessaire avec le
    liquide de refroidissement adapté. - Test de montée en température avec le
    chauffage ouvert : démarrer le moteur et laisser monter en température
    jusqu'à l'ouverture du thermostat (environ 85-90 °C sur la jauge). Ouvrir le
    chauffage de l'habitacle à plein régime pour purger les éventuelles bulles
    d'air dans le circuit. - Contrôle de l'absence de fuite après chauffe : une
    fois le moteur à température normale, inspecter visuellement le bouchon et
    le col de remplissage. Aucune trace de liquide ne doit être visible sur ou
    autour du bouchon. - Vérification des durits sous pression : palper
    doucement (avec protection) les durits supérieure et inférieure du radiateur
    pendant la chauffe. Les durits correctement gonflées mais sans être
    excessivement rigides confirment que la pression est dans la plage normale.
  S7: >-
    Le bouchon de radiateur travaille en interaction directe avec l'ensemble du
    circuit de refroidissement. Un bouchon défaillant ou inadapté peut
    solliciter en cascade plusieurs autres composants. Lors du remplacement du
    bouchon, il convient de vérifier l'état des éléments suivants pour éviter
    une récidive rapide. - Radiateur : le bouchon ferme le col du radiateur et
    régule la pression du circuit. Un col de radiateur endommagé (ébréché,
    fissuré, déformé) empêche le nouveau bouchon de faire étanchéité. Si le col
    est abîmé, le radiateur doit être remplacé en même temps que le bouchon. -
    Vase d'expansion : le circuit de refroidissement est communicant entre le
    radiateur et le vase d'expansion. Un vase fissuré ou un bouchon de vase
    défaillant génèrent les mêmes symptômes qu'un bouchon de radiateur HS
    (fuite, niveau fluctuant). Contrôler l'étanchéité du vase lors de toute
    intervention sur le bouchon de radiateur. - Bouchon de vase d'expansion : il
    possède sa propre soupape et son propre calibrage de pression. Sur de
    nombreux véhicules modernes, c'est le bouchon du vase d'expansion qui assume
    la fonction de régulation de pression — le radiateur n'ayant alors qu'un
    bouchon de fermeture simple. Vérifier lequel des deux est le bouchon de
    pression sur votre véhicule. - Durite de radiateur supérieure et inférieure
    : les durites acheminent le liquide entre le moteur et le radiateur. Une
    durite durcie, fissurée ou dont les colliers sont corrodés peut provoquer
    des fuites indépendantes du bouchon. À inspecter au même moment,
    particulièrement aux jonctions avec le radiateur. - Thermostat : un
    thermostat bloqué ouvert ou fermé perturbe la régulation thermique et peut
    générer des surpressions ponctuelles dans le circuit, accélérant l'usure du
    bouchon. Si le moteur chauffe anormalement, contrôler le thermostat avant de
    conclure à un bouchon seul. - Liquide de refroidissement : profiter du
    remplacement du bouchon pour contrôler la date de la dernière vidange du
    circuit. Un liquide dégradé (pH acide, perte d'inhibiteurs) attaque les
    joints et les composants en aluminium. Renouveler le liquide selon la
    périodicité constructeur (généralement tous les 2-4 ans selon la
    formulation).
  S8: >-
    Comment savoir si mon bouchon de radiateur est défaillant ? Les signes les
    plus courants sont : une surchauffe moteur sans fuite visible, des durits
    qui restent gonflées après refroidissement, un vase d'expansion qui déborde
    régulièrement, ou des traces de liquide de refroidissement coloré autour du
    bouchon. Un test de pression avec un manomètre d'atelier (30 à 50 euros
    l'outil ou location chez un équipementier) permet de vérifier précisément la
    pression d'ouverture de la soupape. Peut-on ouvrir le bouchon de radiateur
    avec le moteur chaud ? Non, jamais. Le liquide de refroidissement est sous
    pression et à haute température lorsque le moteur est chaud (110 à 120 °C).
    Ouvrir le bouchon dans cet état provoque une éruption de vapeur et de
    liquide bouillant qui peut causer des brûlures graves. Attendez
    impérativement le refroidissement complet du moteur (au moins 2 heures)
    avant d'intervenir. Quelle pression doit avoir un bouchon de radiateur ? La
    pression d'ouverture est gravée sur le bouchon d'origine et varie de 0,9 à
    1,4 bar selon les constructeurs et les modèles. Cette valeur est choisie
    pour élever le point d'ébullition du liquide de refroidissement au-dessus de
    110 °C. Un bouchon de pression inférieure abaisse ce seuil et favorise la
    surchauffe. Utilisez toujours la valeur prescrite par le constructeur. À
    quelle fréquence remplacer le bouchon de radiateur ? Le bouchon de radiateur
    n'a pas de durée de vie fixe en kilomètres. Son joint d'étanchéité durcit et
    sa soupape perd sa précision de calibration après 5 à 8 ans en moyenne. Un
    remplacement préventif est conseillé lors de chaque vidange de circuit de
    refroidissement (tous les 2 à 5 ans selon les constructeurs). Le coût du
    bouchon est marginal comparé à celui d'une surchauffe.
---

# Bouchon de radiateur - Guide Diagnostic Complet

## Fonction et Rôle

Fermer le radiateur et reguler la pression du circuit

**Actions principales:** fermer, reguler, proteger

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Surchauffe moteur sans fuite visible**
  surchauffe moteur sans fuite visible

### 🟢 Autres Symptômes

- fuite de liquide par le bouchon
- pression excessive dans le circuit

## Procédure de Diagnostic

Pour diagnostiquer un problème de bouchon de radiateur:

1. **Inspection visuelle** - Examiner l'état du bouchon de radiateur
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

- radiateur
- durite-de-refroidissement

## Critères de Compatibilité

Pour commander le bon bouchon de radiateur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidissement optimal"

## FAQ

**Comment choisir Bouchon de radiateur compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Bouchon de radiateur ?**
En cas de fuite de liquide par le bouchon ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Bouchon de radiateur sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
