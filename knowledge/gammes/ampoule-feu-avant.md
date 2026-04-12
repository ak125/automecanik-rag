---
category: eclairage
slug: ampoule-feu-avant
title: Ampoule feu avant
pg_id: 107
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-04-03'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:rag-enrich-from-web-corpus
  last_enriched_at: '2026-04-03'
  v5_migrated_at: '2026-03-29'
domain:
  role: Produit la lumière pour éclairer la route devant le véhicule
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
    min: 30
    max: 200
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
  - tier: Équivalent OE / équipementier éclairage reconnu
  - tier: Kit LED ou HID compatible
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
    label: Phare ne fonctionne pas
    severity: confort
  - id: S2
    label: Ampoule grillée
    severity: confort
  - id: S3
    label: Eclairage faible
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : phare ne fonctionne pas'
  quick_checks:
  - 'Observer : phare ne fonctionne pas ?'
  - 'Observer : ampoule grillée ?'
  - 'Observer : eclairage faible ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Phare ne fonctionne pas
  - Ampoule grillée
  - Eclairage faible
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '107'
  intro_title: A quoi sert Ampoule feu avant ?
  risk_title: Pourquoi remplacer Ampoule feu avant a temps ?
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
  - question: Comment choisir Ampoule feu avant compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Ampoule feu avant ?
    answer: En cas de phare ne fonctionne pas ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Ampoule feu avant sans verification atelier ?
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
doc_id: ad4bf824-7326-5f65-a087-0c307a441d16
content_hash: sha256:6e9656b3229594df
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
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_10__: '10 %'
    val_12_v: '12 v'
    val_2_v: '2 v'
    val_2__a: '2, a'
    val_20_a: '20 a'
    val_21_a: '21 a'
    val_230_v: '230 V'
    val_3__a: '3, A'
    val_30__: '30 %'
    val_4_v: '4 v'
    val_5__: '5 %'
    val_50_v: '50 v'
    val_7__: '7 %'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'L''ampoule de feu avant est le composant lumineux installé dans le bloc optique avant du véhicule. Sa mission est de
    produire et émettre la lumière nécessaire pour éclairer la route devant le véhicule et pour signaler sa présence aux autres
    usagers. Elle se décline en plusieurs fonctions au sein d''un même bloc optique : feux de croisement (code), feux de route
    (plein phare) et feux de position avant.Les feux de croisement sont les feux utilisés en conduite normale de nuit et dans
    les tunnels. Ils éclairent la route à une distance de 40 à 60 mètres sans éblouir les conducteurs venant en sens inverse,
    grâce à un faisceau asymétrique et dévié vers le bas. Les feux de route fournissent un éclairage puissant jusqu''à 100
    mètres, utilisé uniquement en l''absence de circulation venant en face. Les feux de position avant (ou veilleuses) sont
    de faible puissance — ils signalent la présence du véhicule sans éclairer la route.Techniquement, les ampoules de feux
    avant se déclinent en plusieurs technologies. Les ampoules halogènes (H1, H4, H7, H11, HB3, HB4) représentent le standard
    sur la majorité du parc automobile actuel — elles fonctionnent à une tension de 12 V et consomment de 35 à 100 W selon
    la fonction. Les xénons (HID, D1S, D2S, D3S, D4S) produisent une lumière plus blanche et plus puissante avec une consommation
    réduite. Les LED et les lasers équipent les véhicules haut de gamme récents sous forme de modules intégrés non remplaçables
    unitairement.Les pièces associées à vérifier lors d''une intervention sur les feux avant sont l''ampoule feu arrière,
    l''ampoule feu clignotant et l''ampoule feu de position.'
  S2: 'Les ampoules de feux avant présentent des signes de défaillance que le conducteur peut détecter de l''intérieur du
    véhicule ou lors d''un contrôle extérieur. Agir dès l''apparition des premiers symptômes évite les contraventions et les
    situations dangereuses de nuit. Voici les indicateurs à surveiller :- Phare qui ne fonctionne plus : un bloc optique entier
    reste éteint ou l''une des fonctions (croisement ou route) est inopérante d''un côté. Vérifiez depuis l''extérieur avec
    le véhicule face à un mur — la zone éteinte est immédiatement visible. Avant de conclure à une ampoule grillée, vérifiez
    le fusible correspondant.- Ampoule grillée visible : le filament de l''ampoule est visuellement cassé ou l''enveloppe
    en verre est noircie à l''intérieur. Ce noircissement indique la volatilisation du filament de tungstène — l''ampoule
    est définitivement hors service.- Éclairage faible ou jaunissant : l''ampoule produit une lumière nettement moins puissante
    que l''ampoule du côté opposé, ou la teinte est devenue jaune/orangée au lieu de blanc-jaune. Ce symptôme caractérise
    une ampoule en fin de vie dont le filament s''est aminci — la puissance lumineuse chute avant le claquage définitif.-
    Voyant ampoule allumé au tableau de bord : les véhicules équipés d''un contrôle électronique des feux (présent sur la
    majorité des véhicules depuis 2010) allument un pictogramme ampoule accompagné d''un point d''exclamation pour signaler
    une défaillance sur le circuit des feux extérieurs.- Refus au contrôle technique : une ampoule de phare défaillante est
    un motif de contre-visite immédiate. Le phare éteint ou trop faible est relevé systématiquement lors de la vérification
    de l''éclairage.- Faisceau déréglé ou éblouissant : si le faisceau de croisement éclaire anormalement haut et éblouit
    les conducteurs en face, la cause peut être une ampoule mal positionnée après une intervention précédente ou un support
    de lampe tordu.'
  S3: 'Le choix d''une ampoule de feu avant est déterminé par le type de culot d''origine, la technologie du phare et les
    réglementations en vigueur. Une erreur de référence rend l''ampoule inutilisable ou provoque un faisceau non conforme.
    Voici les critères à respecter pour une commande précise :- Marque, modèle et année de circulation du véhicule : le catalogue
    pièces détachées utilise ces données pour identifier la référence exacte. Sur un même modèle, les blocs optiques peuvent
    changer selon la finition (phares simples vs phares bi-xénon ou LED selon les versions).- Type de culot d''ampoule : identifiez
    le culot en retirant l''ampoule en place ou en consultant le manuel du véhicule. Les plus courants sont H1 (culot P14.5S,
    croisement monofilament), H4 (culot P43T, croisement + route double filament), H7 (culot PX26D, croisement ou route),
    H11 (anti-brouillard, croisement), D1S/D2S/D3S/D4S (xénon). Un culot incorrect ne peut pas s''installer mécaniquement
    dans le support.- Technologie d''origine : si votre véhicule est équipé d''origine de xénon (HID), remplacez par des xénon
    de même référence D-series — les ampoules halogènes ne sont pas interchangeables et l''installation de LED dans un optique
    conçu pour xénon produit un faisceau non conforme et éblouissant.- Teinte et flux lumineux : les ampoules halogènes homologuées
    doivent émettre une lumière jaune-blanc (entre 3 200 K et 4 100 K) avec un flux conforme aux réglementations CE. Les ampoules
    bleues ou ultra-blanches (6 000 K+) ne sont pas homologuées pour les feux de croisement sur route ouverte.- Marquage d''homologation
    : vérifiez la présence du marquage ECE (cercle E suivi d''un numéro) sur l''ampoule ou son emballage. Ce marquage atteste
    de la conformité aux normes européennes. Sans ce marquage, l''ampoule peut être refusée au contrôle technique ou lors
    d''un contrôle routier.- Remplacement par paires : les deux ampoules de croisement (gauche et droite) s''usent à rythme
    similaire. Remplacez les deux simultanément pour garantir un éclairage symétrique et éviter une deuxième intervention
    à court terme.Pour aller plus loin : consultez notre guide d''achat ampoule feu avant — comparatif marques, critères de
    choix et prix.'
  S4_DEPOSE: 'L''accès aux ampoules de feux avant varie considérablement selon le véhicule. Sur les modèles compacts, l''espace
    derrière le bloc optique est souvent très réduit et l''opération peut nécessiter de déposer le boîtier à air ou un cache
    moteur. Sur les véhicules où l''espace est suffisant, l''opération se réalise en quelques minutes. Voici la procédure
    générale :- Coupez le contact et attendez 5 à 10 minutes : laissez refroidir les ampoules halogènes en fonctionnement.
    Une ampoule H7 en fonctionnement peut atteindre 300 °C — un contact direct avec les doigts cause une brûlure sévère.-
    Ouvrez le capot moteur : localisez le bloc optique à remplacer. Vérifiez depuis l''arrière du bloc optique si un cache
    en caoutchouc ou en plastique ferme l''accès au porte-ampoule — c''est le cas sur la grande majorité des véhicules modernes.-
    Retirez le cache de protection : dévissez le cache (quart de tour antihoraire) ou retirez-le en le tirant si c''est un
    cache à bouchon souple. Ce cache assure l''étanchéité du bloc optique — il doit être remis en place soigneusement après
    l''opération.- Déconnectez le connecteur électrique : avant de toucher au porte-ampoule, débranchez le connecteur électrique
    en appuyant sur l''ergot de déverrouillage et en tirant perpendiculairement. Ne jamais tirer sur les fils.- Déverrouillez
    le porte-ampoule : le porte- ampoule est maintenu par une agrafe métallique à ressort (la plus courante) ou par une bague
    de verrouillage à baïonnette. Pour l''agrafe, soulevez-la et basculez-la sur le côté — l''ampoule se dégage alors vers
    l''avant. Pour la bague, tournez d''un quart de tour dans le sens antihoraire et extrayez.- Retirez l''ampoule défaillante
    : saisissez l''ampoule par son culot (jamais par le verre) et extrayez-la. Inspectez le filament cassé ou le noircissement
    pour confirmer la défaillance.- Installez la nouvelle ampoule : saisissez la nouvelle ampoule avec un chiffon propre.
    Pour une H7 ou H1, alignez les détrompeurs du culot avec les encoches du porte-lampe avant d''insérer — un seul sens est
    possible. Vérifiez que l''ampoule est fermement en butée.- Sécurisez le porte-ampoule : rabattez l''agrafe à ressort jusqu''au
    clic de verrouillage ou revissez la bague d''un quart de tour dans le sens horaire. Une ampoule mal verrouillée vibre
    et grille prématurément.- Reconnectez le connecteur et remettez le cache : branchez le connecteur jusqu''au clic d''enclenchement,
    puis remontez le cache en le tournant dans le sens horaire jusqu''au verrouillage.- Testez le fonctionnement et vérifiez
    la direction du faisceau : avec le véhicule face à un mur, allumez les feux de croisement et vérifiez que le faisceau
    est symétrique et pointé correctement (la coupure du faisceau doit être à hauteur de phare ou légèrement en dessous).'
  S4_REPOSE: 'Une fois la nouvelle ampoule feu avant prête, la repose s''effectue dans l''ordre inverse de la dépose. L''étape
    critique est d''éviter tout contact direct avec le verre de l''ampoule halogène — les traces de graisse provoquent un
    point chaud et réduisent drastiquement la durée de vie de l''ampoule. Utilisez un chiffon propre ou des gants fins. -
    Vérifier l''orientation de l''ampoule : l''ampoule halogène H4, H7, H1 ou autre présente un détrompeur physique (picot,
    oreille ou encoche). Positionnez l''ampoule en alignant ce détrompeur avec son logement dans le réflecteur. Ne forcez
    pas — si l''ampoule résiste, vérifiez l''orientation avant tout effort. - Engager l''ampoule dans son logement : poussez
    doucement jusqu''à sentir ou entendre le déclic de verrouillage. Sur les ampoules à baïonnette, un quart de tour suffit
    pour verrouiller. Sur les ampoules à pince, vérifiez que la pince métallique est bien refermée sur le culot. - Reconnecter
    le connecteur électrique : réenficher le connecteur jusqu''au déclic. Un connecteur mal enfoncé provoque un faux contact
    et génère une détection de panne par le calculateur sur les véhicules récents. Tirez légèrement sur le connecteur pour
    confirmer qu''il est verrouillé. - Repositionner le cache de protection : revissez ou reclipsez le cache caoutchouc à
    l''arrière du bloc optique. Ce cache assure l''étanchéité du boîtier — un cache mal positionné laisse entrer l''humidité
    et embue le phare. - Remettre en place les éléments déposés : si le boîtier de filtre à air, un cache moteur ou un bouclier
    ont été déposés pour accéder au bloc, remontez-les dans l''ordre inverse. Vérifiez que les clips et vis sont correctement
    repositionnés. - Test avant fermeture : reconnectez la batterie si elle a été débranchée. Allumez les phares (codes, puis
    longue portée) et demandez à quelqu''un de se placer devant le véhicule pour confirmer que le phare concerné fonctionne.
    - Vérifier le faisceau lumineux : le phare doit éclairer dans le même axe que son homologue. Un faisceau décentré peut
    incommoder les autres conducteurs et nécessite un réglage de la portée (vis de réglage accessible depuis le compartiment
    moteur ou via la commande au tableau de bord selon le véhicule). - Remise sur route : effectuez un court trajet de nuit
    ou en tunnel pour valider l''uniformité de l''éclairage. Sur les véhicules équipés d''un correcteur de portée électronique,
    aucun réglage manuel n''est nécessaire.'
  S5: 'Le remplacement d''une ampoule de feu avant semble simple mais plusieurs erreurs techniques ou de sécurité peuvent
    compliquer l''opération ou rendre la pièce défaillante rapidement. Voici les cinq erreurs les plus fréquentes :- Toucher
    le verre de l''ampoule halogène avec les doigts : les traces de graisse cutanée créent des points de surchauffe sur l''enveloppe
    en verre de quartz des ampoules halogènes (H1, H4, H7, etc.). Ces points atteignent des températures anormalement élevées
    lors du fonctionnement et provoquent une fissure ou une explosion de l''ampoule en quelques heures à quelques jours. Manipulez
    toujours avec un chiffon propre ou les gants fournis dans le kit.- Monter une ampoule non homologuée : les ampoules "ultra-blanches"
    ou "xénon look" à base halogène avec teinte bleue ne sont pas conformes à la réglementation CE pour les feux de croisement.
    Elles produisent un flux lumineux inférieur aux homologuées, éblouissent les autres usagers et peuvent entraîner un refus
    au contrôle technique.- Ne remplacer qu''un phare : les ampoules des deux phares s''usent en parallèle. En remplacer une
    seule crée une dissymétrie lumineuse immédiate (l''ampoule neuve est nettement plus brillante) et impose une deuxième
    intervention à très court terme. Remplacez toujours les deux ampoules de croisement simultanément.- Mal sécuriser l''ampoule
    dans son support : une ampoule mal verrouillée dans le porte- ampoule vibre en roulant, ce qui fatigue rapidement le filament
    et provoque un claquage prématuré. Vérifiez toujours que l''agrafe à ressort est bien encliquetée ou que la bague est
    verrouillée avant de fermer le cache.- Oublier de remettre le cache d''étanchéité : le cache caoutchouc ou plastique à
    l''arrière du bloc optique assure l''étanchéité de l''optique contre l''humidité et la poussière. Oublier de le remettre
    en place entraîne une condensation dans l''optique, un noircissement progressif du réflecteur et une dégradation rapide
    de la prochaine ampoule.'
  S6: 'Après remplacement d''une ampoule de feu avant, les vérifications suivantes confirment que l''installation est conforme
    et que le faisceau est correctement orienté :- Test d''allumage de chaque fonction : vérifiez successivement les feux
    de position, les feux de croisement et les feux de route sur le côté intervenu. Toutes les fonctions doivent s''allumer
    avec une intensité similaire au côté opposé.- Vérification du faisceau face à un mur : placez le véhicule à 5 mètres d''un
    mur blanc et allumez les feux de croisement. La coupure du faisceau (ligne horizontale entre la zone éclairée et la zone
    sombre) doit être à hauteur du bas des phares ou légèrement en dessous. Si le faisceau est trop haut, les autres conducteurs
    sont éblouis — effectuez un réglage du correcteur de phare.- Contrôle de l''absence de condensation dans l''optique :
    après quelques minutes de fonctionnement, inspectez l''intérieur du bloc optique. Une légère buée qui disparaît est normale
    en temps froid. Une condensation persistante ou des gouttes d''eau indiquent un cache d''étanchéité mal positionné ou
    un joint de bloc optique défaillant.- Extinction du voyant ampoule tableau de bord : sur les véhicules avec contrôle électronique
    des feux, démarrez le moteur et attendez quelques secondes — le voyant ampoule doit s''éteindre et ne pas revenir lors
    du trajet de vérification.- Contrôle de la symétrie des faisceaux côté gauche et droit : comparez visuellement la luminosité
    et la zone éclairée des deux phares. Une dissymétrie notable indique soit une ampoule de référence incorrecte, soit une
    ampoule mal positionnée dans son support.'
  S7: 'Lors du remplacement d''une ampoule feu avant, plusieurs pièces du système d''éclairage méritent un contrôle simultané.
    Le démontage partiel du bloc optique ou du boîtier moteur offre un accès facilité à des composants qui partagent le même
    circuit électrique ou le même espace de travail. - Ampoule feu avant côté opposé : les ampoules vieillissent en parallèle.
    Si une ampoule grille, l''autre n''est souvent qu''à quelques centaines d''heures de son terme. Remplacer les deux simultanément
    garantit une homogénéité de l''éclairage et évite une seconde intervention rapprochée. - Ampoule feu de position : intégrée
    dans le même boîtier sur la majorité des véhicules. Elle s''allume avec les feux de croisement et partage le même connecteur
    ou le même cache d''accès. Un contrôle de son état lors de l''intervention est économique en temps. - Ampoule feu clignotant
    avant : logée dans le même bloc optique ou un bloc adjacent. Son câblage passe par la même zone de travail. Un clignotant
    en hyperfrequence est le premier signe d''une ampoule défaillante à surveiller. - Connecteur électrique et faisceau :
    inspectez l''état du connecteur alimentant l''ampoule — oxydation, brûlures, broches rétractées sont fréquentes sur les
    véhicules de plus de 8 ans. Un connecteur dégradé génère des micro-coupures et fait griller les ampoules prématurément.
    - Cache de protection arrière du bloc optique : en caoutchouc ou plastique rigide, il assure l''étanchéité du boîtier.
    S''il est craquelé ou déformé, l''humidité pénètre et embue le phare. Son remplacement préventif lors du changement d''ampoule
    est une bonne pratique. - Réglage de la portée : après tout remplacement d''ampoule ou de bloc optique, vérifiez la portée
    des feux de croisement. Un phare mal orienté éblouit les autres conducteurs et constitue un motif de contre-visite au
    contrôle technique.'
  S8: 'Puis-je remplacer mes ampoules halogènes par des LED sur mes phares avant ?Techniquement possible dans certains cas,
    mais pas pour les feux de croisement sur route ouverte sans homologation spécifique. En France et dans l''Union européenne,
    les ampoules LED plug-and-play pour feux de croisement ne sont pas homologuées pour remplacer les halogènes dans les optiques
    prévus pour halogène — le faisceau produit n''est pas conforme (pas de coupure nette, risque d''éblouissement). Pour les
    feux de position ou les feux de route, certaines LED homologuées existent. Pour avoir des phares LED conformes sur un
    véhicule halogène d''origine, il faut remplacer les blocs optiques complets par des optiques LED homologués.Mon phare
    s''est mis à clignoter quelques semaines après l''installation d''une ampoule neuve — que faire ?Un phare qui clignote
    ou s''éteint par intermittence sur une ampoule récemment installée indique généralement une connexion électrique défaillante
    : connecteur d''alimentation oxydé ou mal encliqueté, contact insuffisant dans le porte-ampoule, ou ampoule mal verrouillée
    dans son support. Déposez l''ampoule, nettoyez les contacts du porte-ampoule avec un spray contact électrique et vérifiez
    que l''ampoule est bien en butée et sécurisée par son agrafe ou sa bague avant de la remonter.Faut-il régler les phares
    après un remplacement d''ampoule ?Normalement non, si l''ampoule est montée dans le même porte-lampe dans le même optique
    — le réglage de l''optique ne change pas. Cependant, si vous avez dû démonter le bloc optique entier pour accéder à l''ampoule,
    un contrôle du réglage est recommandé : placez le véhicule face à un mur à 5 mètres et vérifiez que la coupure du faisceau
    de croisement est à la bonne hauteur. Si non, ajustez via la vis de réglage de l''optique accessible depuis le compartiment
    moteur.Quelle durée de vie espérer d''une ampoule de phare halogène ?Une ampoule halogène H7 ou H4 de qualité standard
    dure en moyenne de 450 à 1 000 heures de fonctionnement, soit 2 à 5 ans selon le kilométrage annuel et les habitudes de
    conduite nocturne. Les ampoules "longue durée" ou "extended life" peuvent atteindre 1 500 heures. Une ampoule xénon HID
    dure 2 500 à 3 000 heures. Les modules LED d''origine constructeur durent généralement toute la vie du véhicule. La durée
    de vie est réduite par les vibrations (mauvaise route), les cycles thermiques fréquents et la manipulation du verre à
    mains nues.'
  META: '{"meta_title":"Ampoule feu avant : quand changer ? | AutoMecanik","meta_description":"Phare qui ne fonctionne plus
    ou éclairage faible ? Ce guide explique quand changer l''ampoule feu avant, comment la choisir par véhicule et éviter
    les erreurs de montage.","meta_title_length": 49,"meta_description_length":155,"primary_intent":"diagnostic","target_sympt
    oms":["phare ne fonctionne pas","ampoule grillée","eclairage faible"],"category":"eclairage"}'
---

# Ampoule feu avant - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière pour éclairer la route devant le véhicule

**Actions principales:** produire, emettre, eclairer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- phare ne fonctionne pas
- ampoule grillée
- eclairage faible

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule feu avant:

1. **Inspection visuelle** - Examiner l'état du ampoule feu avant
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

- ampoule-feu-arriere
- ampoule-feu-clignotant
- ampoule-feu-de-position

## Critères de Compatibilité

Pour commander le bon ampoule feu avant, vous devez connaître:

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

**Comment choisir Ampoule feu avant compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Ampoule feu avant ?**
En cas de phare ne fonctionne pas ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Ampoule feu avant sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
## Phares et feux

### Phares faibles
- **Ampoules vieillissantes** : Les ampoules halogènes perdent 20-30% de luminosité après 2-3 ans. Remplacement par paire recommandé.
- **Optiques ternies** : Le polycarbonate des phares jaunit et devient opaque avec le temps. Kit de rénovation ou polissage.
- **Réglage incorrect** : Phares trop bas après un chargement ou un remplacement. Réglage avec les vis dédiées.

### Ampoules grillées fréquemment
- **Surtension** : Régulateur d'alternateur défaillant (tension > 14.8V). Mesurer la tension de charge.
- **Vibrations excessives** : Ampoule mal fixée dans son support, vibrations transmises au filament.
- **Mauvaise qualité** : Préférer des ampoules de marque (Philips, Osram, Bosch).

### Feux qui ne fonctionnent pas
- **Fusible grillé** : Vérifier le fusible correspondant dans la boîte à fusibles.
- **Connecteur oxydé** : Humidité dans le porte-ampoule, nettoyage et graisse contact.
- **Problème de masse** : Fil de masse corrodé au niveau du feu. Fréquent sur les feux arrière.

## Contrôle technique - Points éclairage

- Tous les feux doivent fonctionner : croisement, route, position, stop, recul, clignotants, antibrouillard arrière
- Hauteur de faisceau correcte (réglage)
- Pas de fissure laissant entrer l'eau dans les optiques
- Couleur conforme : blanc devant, rouge derrière, orange pour les clignotants

## LED vs Halogène vs Xénon

- **Halogène (H7, H4, H1)** : Standard, remplacement facile, coût faible
- **Xénon (D1S, D2S, D3S)** : Puissant, durée de vie longue, remplacement coûteux, nécessite un ballast
- **LED** : Très longue durée de vie, faible consommation, remplacement du bloc optique entier en cas de panne

## Quand consulter un professionnel

- Phare xénon qui clignote ou change de couleur (ballast ou ampoule)
- Feux LED intégrés défaillants (remplacement du bloc complet)
- Court-circuit récurrent (fusible qui saute à chaque remplacement)
- Défaut de réglage persistant malgré les ajustements
