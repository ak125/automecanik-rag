---
category: allumage
slug: module-d-allumage
title: Module d'allumage
pg_id: 1218
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
  role: Commander electroniquement le moment d'allumage
  must_be_true:
  - piloter
  - commander
  - controler
  must_not_contain:
  - freinage
  - climatisation
  - embrayage
  - direction
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - piloter
  - commander
  - controler
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
  - ❌ "demarrage instantane"
  cost_range:
    min: 100
    max: 400
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    price_range: Prix élevé — justifié par la traçabilité et la certification
  - tier: Équivalent OE (OES)
    price_range: Prix intermédiaire — recommandé pour la majorité des cas
  - tier: Aftermarket standard
    price_range: Prix bas — vérifier les certifications avant achat
  brands:
    premium:
    - Bosch
    - Valeo
    standard:
    - Febi
    - Meyle
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Rates d allumage intermittents
    severity: confort
  - id: S2
    label: Demarrage difficile
    severity: confort
  - id: S3
    label: Perte de puissance sur certains cylindres
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : rates d allumage intermittents'
  quick_checks:
  - 'Observer : rates d allumage intermittents ?'
  - 'Observer : demarrage difficile ?'
  - 'Observer : perte de puissance sur certains cylindres ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Rates d allumage intermittents
  - Demarrage difficile
  - Perte de puissance sur certains cylindres
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '1218'
  intro_title: A quoi sert Module d'allumage ?
  risk_title: Pourquoi remplacer Module d'allumage a temps ?
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
  - question: Comment choisir Module d'allumage compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Module d'allumage ?
    answer: En cas de rates d allumage intermittents ou de degradation mesurable, il faut controler rapidement avant panne
      secondaire.
  - question: Puis-je monter Module d'allumage sans verification atelier ?
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
doc_id: 7d43cf22-a028-578a-b078-cb51421e2e34
content_hash: sha256:9e3b299bb0937bf3
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
  area: Sur le vehicule (position variable selon modele)
  access: Consulter la revue technique du vehicule
  adjacent_parts:
  - pieces adjacentes du meme systeme
installation:
  difficulty: variable
  time: consulter revue technique
  tools:
  - outillage standard
  prerequisite: Consulter la procedure constructeur
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'Hall'
    source_ref: corpus RAG web OEM
  - type: 'hall'
    source_ref: corpus RAG web OEM
  - type: 'organique'
    source_ref: corpus RAG web OEM
  - type: 'piézo'
    source_ref: corpus RAG web OEM
  - type: 'plein'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_000_v: '000 V'
    val_12_v: '12 v'
    val_15__: '15 %'
    val_2_litres: '2 litres'
    val_20__: '20 %'
    val_20_95__: '20,95 %'
    val_28_a: '28 a'
    val_3_v: '3 v'
    val_30__: '30 %'
    val_30_bars: '30 bars'
    val_33_9__: '33,9 %'
    val_35__: '35 %'
    val_380__c: '380 °C'
    val_40__: '40 %'
    val_40_1__: '40,1 %'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: Le module d'allumage est le composant électronique qui commande, pilote et contrôle le moment précis de la délivrance
    de l'étincelle aux bougies d'allumage. Sur les moteurs à allumage commandé (essence, GPL, éthanol), la combustion du mélange
    air-carburant dépend entièrement de l'étincelle électrique produite par la bougie au moment exact calculé par ce module.
    En pratique, le module d'allumage reçoit des signaux provenant du capteur de position de vilebrequin (PMH) et du capteur
    d'arbre à cames. Il traite ces informations pour calculer l'avance à l'allumage optimale selon le régime moteur, la charge,
    la température et les informations de cliquetis transmises par le capteur anticliquetis. Il délivre ensuite un signal
    de commande aux bobines d'allumage qui génèrent la haute tension envoyée aux bougies. Sur les moteurs anciens, le module
    d'allumage était une unité distincte du calculateur moteur (allumage transistorisé ou CDI). Sur les motorisations modernes,
    sa fonction est intégrée directement dans le calculateur moteur (ECU) qui gère simultanément l'injection et l'allumage.
    Dans les deux cas, un défaut de module d'allumage supprime ou perturbe l'étincelle sur un ou plusieurs cylindres, entraînant
    des rates de combustion immédiates. Les pièces directement associées lors d'une intervention sont la bobine d'allumage
    (qui amplifie le signal du module en haute tension) et le calculateur moteur. La défaillance du module d'allumage se distingue
    de la défaillance de la bobine par le fait qu'elle touche généralement plusieurs cylindres simultanément, alors qu'une
    bobine défaillante n'affecte qu'un ou deux cylindres.
  S2: 'Un module d''allumage défaillant produit des symptômes qui affectent directement les performances du moteur et peuvent
    déclencher le voyant de diagnostic. Ces signes apparaissent souvent progressivement, parfois de façon intermittente au
    début. Voici les principaux : - Rates d''allumage intermittentes : le moteur ``trébuche`` à certaines plages de régime
    ou de charge — sensation de perte de puissance soudaine et brève, parfois accompagnée d''une secousse du véhicule. Les
    rates peuvent générer un code défaut P030x (rate cylindre X) ou P0300 (rate aléatoire). - Démarrage difficile : le moteur
    met plus de temps que d''habitude à démarrer, nécessite plusieurs tentatives de démarreur, ou démarre puis cale immédiatement.
    Le module ne délivre plus le signal d''allumage correctement dans les premières secondes. - Perte de puissance sur certains
    cylindres : le moteur tourne ``sur trois pattes`` — perte de puissance notable, consommation accrue, bruit de fonctionnement
    irrégulier. Sur les moteurs 4 cylindres, la perte d''un cylindre représente 25 % de la puissance disponible. - Consommation
    de carburant en hausse : le carburant non enflammé par les rates est éjecté à l''échappement. Sur un cycle de conduite
    mixte, les rates augmentent visiblement la consommation et peuvent dégrader le catalyseur à moyen terme. - Moteur chaud
    difficile à redémarrer : certains modules d''allumage thermosensibles tombent en panne lorsque la température monte (dilatation
    des composants internes) et retrouvent leur fonctionnement au refroidissement. Le symptôme caractéristique est un démarrage
    impossible après un arrêt moteur chaud (arrêt au feu rouge, ravitaillement), mais un redémarrage normal après refroidissement.
    - Voyant ``check engine`` allumé : la plupart des calculateurs modernes détectent les rates d''allumage et allument le
    voyant MIL (malfunction indicator lamp). La lecture des codes avec un outil OBD identifie les cylindres en défaut et oriente
    vers le module ou les bobines. Le diagnostic différentiel entre un module d''allumage et des bougies ou bobines défaillantes
    nécessite un test d''inversion des composants (intervertir les bobines entre cylindres) ou une mesure oscilloscopique
    du signal d''allumage.'
  S3: 'Le module d''allumage doit correspondre exactement à l''architecture électronique du système d''allumage du véhicule.
    Un module incorrect peut endommager les bobines ou ne pas communiquer correctement avec le calculateur moteur. Voici les
    critères à vérifier : - Marque, modèle et année du véhicule : le système d''allumage évolue selon les générations. Indiquer
    l''année exacte de mise en circulation est indispensable pour éviter de commander un module d''une génération précédente
    ou suivante. - Code moteur : deux motorisations de cylindrée identique mais de code moteur différent peuvent utiliser
    des modules d''allumage différents. Le code moteur est la référence la plus précise pour identifier la pièce exacte. -
    Vérifier la présence de rates d''allumage intermittentes : avant de commander le module, confirmer que les rates sont
    présentes sur plusieurs cylindres et non sur un seul — une rate sur un seul cylindre oriente plus vers une bougie ou une
    bobine défaillante que vers le module. - Vérifier si le démarrage est difficile : un démarrage difficile combiné à des
    rates généralisées est plus caractéristique d''une défaillance de module que d''une défaillance de bougie isolée. - Vérifier
    la perte de puissance par cylindre : noter si la perte affecte plusieurs cylindres simultanément — cela renforce l''hypothèse
    d''un module central plutôt que de plusieurs bougies ou bobines défaillantes en même temps. - Type de module (externe
    ou intégré) : sur les véhicules anciens (avant 2000 environ), le module d''allumage est une boîte électronique séparée.
    Sur les véhicules récents, la fonction est intégrée au calculateur moteur et non remplaçable seule — vérifier que la pièce
    commandée correspond bien au type externe présent sur le véhicule. - Préférer les équipementiers reconnus : Bosch, Delphi,
    Bremi, Beru et NGK sont des fournisseurs fiables pour les composants d''allumage. Éviter les modules sans marque identifiable
    dont la conformité aux spécifications électriques n''est pas garantie. Pour aller plus loin : consultez notre guide d''achat
    module d''allumage — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 'Le remplacement d''un module d''allumage externe (boîte électronique distincte) est une opération d''accessibilité
    variable selon l''emplacement du module sur le véhicule (parfois fixé sur le bloc moteur, parfois sur le compartiment
    moteur ou sur la culasse). Voici la procédure générale : - Confirmer le diagnostic : lire les codes de défaut OBD, noter
    les codes de rates par cylindre. Effectuer si possible un test d''inversion des bobines pour éliminer une défaillance
    de bobine isolée avant de remplacer le module. - Couper le contact et débrancher la batterie : déconnecter la borne négative
    de la batterie. Le module d''allumage travaille avec des tensions pouvant atteindre 40 000 V côté secondaire des bobines
    — toute intervention sur un circuit d''allumage sous tension présente un risque d''électrocution. - Localiser le module
    d''allumage : consulter le schéma électrique du véhicule pour identifier l''emplacement exact du module. Il est souvent
    fixé près des bobines, sur le côté du bloc moteur ou sur un support dédié dans le compartiment moteur. - Déconnecter les
    connecteurs électriques : identifier et déconnecter les connecteurs du module — généralement un connecteur de commande
    (signal du capteur PMH, alimentation, masse) et un ou plusieurs connecteurs de sortie vers les bobines. Repérer ou photographier
    le câblage avant dépose. - Déposer le module : dévisser les vis ou boulons de fixation du module sur son support. Certains
    modules sont fixés avec un produit frein-filet — appliquer une légère pression de torsion si résistance. - Nettoyer le
    support de montage : si le module est fixé sur le bloc moteur avec une pâte thermoconductrice (dissipation thermique),
    nettoyer la surface d''appui et appliquer une couche fraîche de pâte thermique sur la face arrière du nouveau module avant
    montage. - Monter le nouveau module : positionner le nouveau module sur son support, fixer les vis au couple normal. Reconnecter
    les connecteurs dans leur ordre de dépose en s''assurant du verrouillage de chaque clip. - Rebrancher la batterie et effacer
    les codes : reconnecter la borne négative de la batterie. Connecter l''outil OBD et effacer tous les codes de défaut mémorisés.
    - Test de démarrage et essai roulant : démarrer le moteur et observer le fonctionnement au ralenti. Effectuer un essai
    roulant de 15 à 20 km incluant des phases d''accélération franche pour vérifier l''absence de rates à toutes les plages
    de régime. - Contrôle final des codes : après l''essai roulant, relire les codes de défaut pour confirmer qu''aucun nouveau
    code n''est apparu et que les anciens codes ne sont pas revenus.'
  S4_REPOSE: 'Après le remplacement du module d''allumage, la phase de vérification post- montage est essentielle pour confirmer
    l''absence de rates d''allumage et valider que le nouveau module communique correctement avec le reste du système d''allumage.
    Ne pas négliger l''étape d''effacement de codes et de test roulant étendu. - Vérifier le serrage et la connexion thermique
    du module : si le module d''allumage est monté sur le bloc moteur avec une pâte thermoconductrice, confirmer que la face
    arrière du module est correctement enduite et en contact plan avec le support métallique. Un mauvais contact thermique
    entraîne une surchauffe du module à haute charge et une défaillance prématurée. Le serrage des vis de fixation doit permettre
    un contact uniforme sans jeu. - Reconnecter les connecteurs dans l''ordre correct : vérifier que chaque connecteur est
    verrouillé jusqu''au clic audible. Sur les modules multi-connecteurs (connecteur de commande + connecteurs de sorties
    bobines), confondre les connecteurs produit un allumage sur le mauvais cylindre ou une absence totale d''allumage. Consulter
    le schéma électrique ou les photos prises lors de la dépose. - Reconnecter la batterie et effectuer un autodiagnostic
    : reconnecter la borne négative de la batterie. Connecter l''outil OBD et vérifier l''absence de codes actifs avant le
    démarrage. Si des codes de rates par cylindre étaient présents avant l''intervention, les effacer. Note : ne pas effacer
    les codes avant de les avoir notés — ils constituent un historique utile en cas de récidive. - Effectuer le démarrage
    et contrôler le régime de ralenti : démarrer le moteur et laisser monter en température au ralenti. Le régime de ralenti
    doit se stabiliser rapidement (sous 30 secondes) à la valeur nominale constructeur. Une instabilité de ralenti persistante
    après 2 minutes de chauffe peut indiquer une mauvaise connexion sur un des connecteurs de bobine. - Test de rates par
    cylindre avec l''outil OBD : avec le moteur chaud au ralenti, activer la lecture des rates d''allumage en temps réel sur
    l''outil OBD. Vérifier que le compteur de rates de chaque cylindre reste à zéro ou extrêmement faible (moins de 5 rates
    en 1 000 révolutions moteur). Une persistance de rates sur un cylindre spécifique après remplacement du module indique
    une bobine défaillante ou une bougie usée sur ce cylindre. - Essai roulant de validation — 20 à 30 km : effectuer un essai
    roulant incluant des accélérations franches de 0 à 100 km/h et des phases de régime élevé (au-delà de 4 000 tr/min si
    le constructeur autorise ce régime). Les rates d''allumage liées à une défaillance de module se manifestent souvent en
    charge haute et régime élevé — le test en ville à faible régime ne suffit pas à valider la réparation. - Relecture des
    codes après essai : après l''essai roulant, relire les codes de défaut. Confirmer l''absence de codes de rates ou de codes
    de module d''allumage. Un test de conduite de 300 km supplémentaires sans récidive de codes valide définitivement le remplacement.'
  S5: 'Le remplacement d''un module d''allumage comporte plusieurs pièges techniques. Voici les erreurs les plus fréquentes
    et leurs conséquences : - Remplacer le module sans avoir éliminé les bougies ou bobines défaillantes : les rates d''allumage
    peuvent être causées par des bougies usées ou des bobines défaillantes — des causes bien moins coûteuses. Remplacer directement
    le module sans diagnostic différentiel préalable conduit à une dépense inutile si la cause réelle était une bougie à 8
    euros. Conséquence : panne persistante et coût de réparation doublé. - Toucher les câbles haute tension du secondaire
    des bobines avec le moteur en marche : tester l''allumage moteur tournant en touchant les fils de bougie expose à des
    décharges électriques de plusieurs milliers de volts. Conséquence : risque de choc électrique grave, parfois mortel sur
    les systèmes à bobine unique à haute énergie. - Négliger la pâte thermique sur les modules fixés sur le bloc moteur :
    certains modules d''allumage sont montés sur le bloc et dissipent leur chaleur par contact métallique. Sans pâte thermique,
    la température du module monte en flèche et la durée de vie est réduite. Conséquence : nouvelle défaillance prématurée
    du module dans les 20 000 à 50 000 km. - Commander un module pour une mauvaise génération moteur : deux modules d''allumage
    d''aspect similaire peuvent avoir des caractéristiques d''amplification et de timing différentes. Un module inadapté perturbe
    l''avance à l''allumage. Conséquence : performances dégradées, risque de cliquetis, voire dommages pistons sur les moteurs
    à fort taux de compression. - Ne pas effacer les codes OBD après remplacement : les codes de rates mémorisés peuvent maintenir
    le voyant allumé même avec le module neuf. Conséquence : le client croit que la panne persiste alors que le système fonctionne
    normalement — perte de confiance et retour inutile en atelier.'
  S6: 'Après le remplacement du module d''allumage, plusieurs contrôles permettent de confirmer que l''allumage fonctionne
    correctement sur tous les cylindres : - Effacement des codes OBD et contrôle post-démarrage : effacer tous les codes de
    défaut mémorisés, démarrer le moteur et laisser tourner 3 minutes au ralenti. Relire immédiatement les codes — aucun code
    de rate ne doit apparaître dès la première lecture. - Contrôle du ralenti : le ralenti doit être stable et régulier dans
    la plage nominale (700 à 900 tr/min selon le moteur). Un ralenti instable indique une rate persistante sur un cylindre
    — le module n''était peut-être pas la seule cause du problème. - Test de montée en régime : effectuer une accélération
    progressive de 1 000 à 4 000 tr/min en stationnaire. Le moteur doit répondre linéairement sans à-coup ni tremblement caractéristique
    des rates à charge partielle. - Essai roulant avec monitoring OBD : si un outil de diagnostic permet de visualiser les
    rates en temps réel, effectuer un essai roulant de 20 km avec surveillance du compteur de rates par cylindre. Ce compteur
    doit rester à zéro sur l''ensemble du parcours. - Vérification de la consommation de carburant : après 200 à 300 km de
    conduite normale post-remplacement, comparer la consommation avec les valeurs relevées avant la panne — une réduction
    significative confirme que les rates qui surconsommaient le carburant ont disparu.'
  S7: 'Le module d''allumage est souvent remplacé après un diagnostic d''élimination : bobines testées, bougies vérifiées.
    Avant de commander le module, et lors du remplacement, plusieurs composants périphériques méritent un contrôle ou un remplacement
    préventif. - Bobine d''allumage — Module d''allumage et bobines d''allumage travaillent en tandem. Avant de conclure à
    une défaillance de module, tester les bobines (résistance primaire et secondaire à l''ohmmètre ou par permutation entre
    cylindres). Un module neuf sur des bobines défaillantes ne résoudra pas le problème. Si une bobine est défectueuse, évaluer
    le remplacement en kit (toutes les bobines d''un même allumeur). - Calculateur moteur (ECU) — Le module d''allumage reçoit
    ses ordres du calculateur moteur. Des codes de rates persistants après remplacement du module peuvent indiquer un signal
    de commande incorrect en sortie de calculateur. Un diagnostic oscilloscope sur le signal d''allumage permet de trancher
    avant d''engager un remplacement de calculateur. - Bougies d''allumage — Le remplacement du module d''allumage est l''occasion
    idéale de vérifier ou remplacer les bougies. Des bougies usées augmentent la tension nécessaire à l''allumage et sollicitent
    excessivement le module. Un jeu de bougies neuf associé au module neuf garantit un allumage nominal dès la remise en route.
    - Capteur de position vilebrequin (PMH) — Le module d''allumage reçoit le signal de position du vilebrequin pour synchroniser
    l''allumage. Un capteur PMH défaillant génère des rates intermittentes et une instabilité de ralenti identiques aux symptômes
    d''un module défaillant. Vérifier la cohérence des codes de défaut pour distinguer les deux pannes.'
  S8: 'Comment distinguer une panne de module d''allumage d''une panne de bobine ? La méthode la plus simple est le test d''inversion
    : intervertir les bobines entre deux cylindres (par exemple cylindre 1 et cylindre 3) et observer si la rate migre avec
    la bobine ou reste sur le même cylindre. Si la rate migre, la bobine est en cause. Si la rate reste sur le même cylindre
    ou si elle s''étend à plusieurs cylindres sans logique d''inversion, le module d''allumage ou le calculateur est suspect.
    Un oscilloscope sur les signaux de commande du module permet une confirmation définitive. Un module d''allumage externe
    peut-il être remonté en état (reconditionné) ? Techniquement oui, mais rarement de façon économiquement pertinente. Les
    défaillances internes du module (transistors de puissance, circuits de commande) nécessitent un équipement de microsoudure
    et un accès aux schémas internes. Quelques spécialistes en électronique automobile proposent ce service pour des modules
    rares ou de véhicules anciens. Pour les véhicules courants, le remplacement par une pièce neuve ou reconditionnée est
    plus fiable et souvent moins cher. Le module d''allumage nécessite-t-il une adaptation après montage ? Sur les véhicules
    récents où la fonction allumage est intégrée au calculateur moteur, il n''y a pas de module externe à remplacer séparément.
    Sur les véhicules équipés d''un module externe distinct (architectures antérieures à 2005 environ), le module est généralement
    plug-and-play : il n''y a pas de codage ni d''apprentissage nécessaire après montage, contrairement à un calculateur moteur.
    Il suffit d''effacer les codes OBD et de vérifier l''absence de rates sur essai roulant. Les rates d''allumage peuvent-elles
    endommager le catalyseur ? Oui, c''est l''une des conséquences les plus sérieuses d''une panne de module d''allumage prolongée.
    Le carburant non brûlé par les rates passe dans l''échappement et arrive cru sur le catalyseur, où il brûle à des températures
    très élevées (supérieures à 1 000 °C). Ces surchauffes répétées fondent la structure en céramique du catalyseur. Un catalyseur
    détruit par des rates d''allumage est bien plus coûteux à remplacer que le module d''allumage lui-même — raison supplémentaire
    d''intervenir sans délai dès l''apparition des premiers symptômes.'
  META: '{"meta_title":"Module d''allumage : guide diagnostic et remplacement","meta_description":"Rates d''allumage, démarrage
    difficile, perte de puissance ? Découvrez quand changer le module d''allumage, comment le choisir et les erreurs à éviter
    selon votre véhicule."}'
---

# Module d'allumage - Guide Diagnostic Complet

## Fonction et Rôle

Commander electroniquement le moment d'allumage

**Actions principales:** piloter, commander, controler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- rates d allumage intermittents
- demarrage difficile
- perte de puissance sur certains cylindres

## Procédure de Diagnostic

Pour diagnostiquer un problème de module d'allumage:

1. **Inspection visuelle** - Examiner l'état du module d'allumage
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

- bobine-d-allumage
- calculateur-moteur

## Critères de Compatibilité

Pour commander le bon module d'allumage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "demarrage instantane"

## FAQ

**Comment choisir Module d'allumage compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Module d'allumage ?**
En cas de rates d allumage intermittents ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Module d'allumage sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
