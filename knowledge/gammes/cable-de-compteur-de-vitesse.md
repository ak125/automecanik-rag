---
category: tableau-de-bord
slug: cable-de-compteur-de-vitesse
title: Câble de compteur de vitesse
pg_id: 1150
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
business_priority: low
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:rag-enrich-from-web-corpus
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Transmettre mecaniquement la rotation des roues au compteur de vitesse du tableau de bord via un cable flexible (courant
    de Foucault)
  must_be_true:
  - transmettre la rotation au compteur
  - relier la transmission au tableau de bord
  - permettre l'affichage de la vitesse
  must_not_contain:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  - capteur electronique
  related_parts:
  - compteur-de-vitesse
  - boite-de-vitesses
  - tableau-de-bord
  confusion_with:
  - piece: capteur-impulsion
    difference: Le capteur d'impulsion est electronique (signal ABS/ESP). Le cable de compteur est mecanique (rotation physique).
      Les vehicules modernes utilisent le capteur, les anciens le cable.
selection:
  criteria:
  - Marque de votre vehicule
  - Modele de votre vehicule
  - Annee de votre vehicule
  - Longueur du cable (variable selon modele)
  - Type d'embout cote transmission (carre, hexagonal)
  - Type d'embout cote compteur
  - Gaine rigide ou souple
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ Ne pas confondre cable de compteur mecanique et capteur de vitesse electronique
  - ❌ Verifier la longueur exacte du cable avant commande
  - ❌ Ne pas forcer l'embout lors du montage (risque de casse)
  cost_range:
    min: 8
    max: 60
    currency: EUR
    unit: l'unite
    source: fourchette constatee equipementiers
  checklist:
  - Verifier si votre vehicule utilise un cable mecanique ou un capteur electronique
  - Mesurer la longueur du cable d'origine
  - Verifier le type d'embout cote transmission
  - Verifier le type d'embout cote compteur
  - Commander la bonne longueur de gaine
  brands:
    premium:
    - Elring
    - Victor Reinz
    standard:
    - Febi
    - Ajusa
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Compteur de vitesse bloque a zero
    severity: securite
  - id: S2
    label: Aiguille du compteur qui saute ou tremble
    severity: confort
  - id: S3
    label: Bruit de grincement derriere le tableau de bord
    severity: confort
  - id: S4
    label: Lecture de vitesse erronee (trop haute ou trop basse)
    severity: securite
  - id: S5
    label: Compteur kilometrique qui ne tourne plus
    severity: confort
  causes:
  - Cable casse ou effiloche a l'interieur de la gaine
  - Embout use ou arrondi (ne s'accroche plus)
  - Gaine pliee ou ecrasee empechant la rotation
  - Manque de lubrification du cable dans la gaine
  depose_steps: []
  quick_checks:
  - 'Observer : compteur de vitesse bloque a zero ?'
  - 'Observer : aiguille du compteur qui saute ou tremble ?'
  - Bruit de grincement derriere le tableau de bord ?
  - 'Observer : lecture de vitesse erronee (trop haute ou trop basse) ?'
maintenance:
  interval:
    value: selon etat
    unit: condition
    note: Pas de periodicite fixe. Remplacer en cas de panne compteur, bruit ou lecture erronee. Piece typique des vehicules
      anciens (avant 2000).
    source: null
  cross_gammes:
  - capteur-impulsion
  brands:
    equivalent:
    - Cofle
    - Valeo
    budget:
    - Febi
    - JP Group
  wear_signs:
  - Compteur de vitesse bloque a zero
  - Aiguille du compteur qui saute ou tremble
  - Bruit de grincement derriere le tableau de bord
  - Lecture de vitesse erronee (trop haute ou trop basse)
  - Compteur kilometrique qui ne tourne plus
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '1150'
  intro_title: A quoi sert le cable de compteur de vitesse ?
  risk_title: Pourquoi remplacer le cable de compteur a temps ?
  risk_explanation: Un cable defaillant empeche l'affichage correct de la vitesse, ce qui compromet la securite routiere et
    peut entrainer un echec au controle technique.
  risk_consequences:
  - Impossibilite de connaitre sa vitesse reelle (risque d'exces de vitesse)
  - Compteur kilometrique bloque (impact revente et CT)
  - Bruit de grincement permanent derriere le tableau de bord
  risk_conclusion: Le remplacement est simple et peu couteux. Ne pas rouler sans compteur fonctionnel.
  arguments:
  - content: Selection guidee par vehicule et longueur de cable.
    icon: check-circle
    title: Compatibilite verifiee
  - content: Un compteur en panne est un motif de refus au controle technique.
    icon: shield-check
    title: Controle technique
  - content: Piece peu couteuse, remplacement rapide.
    icon: clock
    title: Intervention rapide
  - content: Verifiez si votre vehicule utilise un cable ou un capteur electronique.
    icon: list-check
    title: Verification prealable
  faq:
  - question: Mon vehicule a-t-il un cable ou un capteur electronique ?
    answer: Les vehicules avant 1995-2000 utilisent generalement un cable mecanique. Les vehicules modernes utilisent un capteur
      electronique (capteur d'impulsion). Verifiez sous le tableau de bord ou pres de la boite de vitesses.
  - question: Comment savoir si le cable est casse ?
    answer: Compteur bloque a zero, aiguille immobile meme en roulant, bruit de grincement au tableau de bord. Debrancher
      le cable cote compteur et le faire tourner a la main pour verifier.
  - question: Faut-il lubrifier le cable de compteur ?
    answer: Oui, un cable sec grince et s'use plus vite. Utiliser de la graisse legere ou du lubrifiant silicone dans la gaine
      lors du remplacement.
  - question: Quel est le prix d'un cable de compteur ?
    answer: Entre 8 et 60 EUR selon le vehicule. Le remplacement prend generalement 30 minutes a 1 heure.
  quality:
    score: 76
    source: manual-from-db-2026-03-21
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
doc_id: a97b57f0-8a5f-5ede-badb-e235413e3858
content_hash: sha256:25247fd8c9f93202
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
  technical_notes:
    val_0_2_bar: '0,2 bar'
    val_10__: '10 %'
    val_10_km: '10 km'
    val_120_km: '120 km'
    val_150_km: '150 km'
    val_19_a: '19 a'
    val_2__a: '2, A'
    val_20_km: '20 km'
    val_200_km: '200 km'
    val_23__c: '23 °C'
    val_30_km: '30 km'
    val_40_km: '40 km'
    val_45_km: '45 km'
    val_5__c: '5 °C'
    val_50_a: '50 a'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le c&acirc;ble de compteur de vitesses ou kilométrique est une pièce très
    importante pour le véhicule. Il permet d'indiquer au conducteur par
    l'intermédiaire du compteur à quelle vitesse on est en train de rouler. Le
    c&acirc;ble fonctionne avec le courant de Foucault. Le c&acirc;ble relie la
    roue ou la transmission du véhicule à un plateau aimanté.La rotation des
    roues entra&icirc;ne le plateau aimanté et la vitesse de rotation est
    reflétée sur le tachymètre qui s'affiche sur le compteur. En permettant
    l'affichage de la vitesse, le c&acirc;ble permet au conducteur de mieux
    ma&icirc;triser le véhicule, de savoir quand engager un nouveau rapport et
    de respecter les limitations de vitesse.
  S2: >-
    Le c&acirc;ble de compteur de vitesse n'a pas une période de remplacement.
    Le c&acirc;ble est une pièce qui s'use avec le temps suivant plusieurs
    facteurs par exemple le style de conduite et des conditions dans lesquelles
    le véhicule roule habituellement. Si on constate une panne de compteur, il
    faut diagnostiquer pour savoir si le c&acirc;ble est l'origine du problème
    et le remplacer si nécessaire. Un c&acirc;ble défectueux ne va pas afficher
    la bonne vitesse dans ce cas on risque à faire des accidents puisqu'on va
    rouler à des grandes vitesses, problème au niveau de la bo&icirc;te de
    vitesses puisqu'on ne va pas savoir quand on change les vitesses.
  S3: >-
    - Longueur totale exacte : Le câble de compteur est dimensionné pour
    correspondre au parcours depuis la boîte de vitesses jusqu'au tableau de
    bord. Un câble trop court crée une tension permanente qui génère des
    vibrations et accélère l'usure. Trop long, il forme des boucles qui frottent
    sur les pièces chaudes. Mesurez l'original ou relevez la référence
    constructeur. - Type et dimension des embouts : L'embout côté boîte de
    vitesses (carré, hexagonal ou à baïonnette selon le constructeur) et
    l'embout côté compteur doivent correspondre exactement à l'original. Les
    carrés les plus courants sont de 5 mm et 6,35 mm (1/4 de pouce) — confondre
    les deux rend le câble inutilisable. - Diamètre de la gaine extérieure : La
    gaine conditionne le passage dans les grommets et supports de carrosserie.
    Un diamètre incorrect ne rentre pas dans les guides et force sur les œillets
    de passage, créant des angles qui brisent le câble interne. - Compatibilité
    avec la boîte de vitesses : Le câble prend son mouvement rotatif sur la
    boîte de vitesses ou le pont arrière (traction ou propulsion). Les boîtes
    manuelles, automatiques et les ponts arrière ont des sorties de câble
    différentes — spécifiez le type de transmission lors de la commande. -
    Présence ou absence de butée de gaine intermédiaire : Certains modèles
    utilisent un câble en deux sections avec un raccord intermédiaire (pour
    faciliter le passage autour du moteur). Vérifiez si le vôtre est en une ou
    deux sections avant de commander. - Marque, modèle, année et type de boîte :
    Ces quatre informations sont indispensables. Un même véhicule peut recevoir
    des câbles différents selon la motorisation et le type de boîte (manuelle 5
    rapports vs automatique 4 rapports).
  S4_DEPOSE: >-
    - Préparer le véhicule : Coupez le contact, appliquez le frein à main et
    callez les roues. Le câble de compteur passe généralement sous le véhicule
    et dans le compartiment moteur — travaillez si possible sur une fosse ou
    avec le véhicule surélevé sur chandelles. - Photographier le tracé du câble
    : Avant tout démontage, photographiez le parcours complet du câble depuis la
    boîte de vitesses jusqu'à l'entrée du tableau de bord. Notez chaque collier,
    agrafe et guide de carrosserie — la repose doit reproduire exactement ce
    tracé. - Déconnexion côté tableau de bord : Depuis l'habitacle, accédez à
    l'arrière du compteur (généralement accessible sous la planche de bord ou
    après démontage du panneau de compteur). Dévissez le raccord fileté (sens
    antihoraire) qui fixe le câble dans le compteur. Si le compteur doit être
    déposé, consultez la procédure spécifique au modèle. - Dégager le câble au
    passage de cloison : Le câble traverse la cloison pare-feu via un grommets
    en caoutchouc. Dégagez doucement ce grommets pour libérer le passage sans le
    déchirer — un grommets abîmé laisse entrer l'eau et les gaz d'échappement
    dans l'habitacle. - Déconnexion côté boîte de vitesses : Sous le véhicule,
    localisez la sortie de câble sur la boîte (généralement sur le côté de la
    cloche d'embrayage ou sur le pont). Dévissez le raccord de fixation et
    retirez l'embout du pignon de compteur. - Retirer les colliers sur le
    parcours : Dégagez le câble de tous ses points de fixation intermédiaires
    (colliers en plastique ou agrafes métalliques) en notant chaque emplacement.
    - Extraire le câble usagé : Tirez progressivement le câble depuis la boîte
    de vitesses vers le tableau de bord (ou inversement). Si la gaine est rigide
    par temps froid, réchauffez-la légèrement avec un sèche-cheveux pour
    faciliter le passage dans les courbes. - Installer le nouveau câble : Guidez
    le nouveau câble en suivant exactement le tracé photographié. Engagez
    d'abord l'embout côté boîte de vitesses, puis progressez vers le tableau de
    bord en reposant chaque collier. Repassez le grommets de cloison en le
    regraisssant légèrement. - Connecter côté tableau de bord et vérifier :
    Vissez le raccord du câble dans le compteur (serrage à la main puis un quart
    de tour à la clé). Ne pas serrer excessivement — le raccord en laiton se
    détériore rapidement si sur-serré.
  S5: >-
    - Forcer l'extraction du câble intérieur sans retirer la gaine complète :
    Certains tentent de tirer uniquement le câble intérieur en laissant la gaine
    en place. Si la gaine est cintrée ou corrodée intérieurement, le câble neuf
    s'usera en quelques semaines contre les aspérités. Remplacez toujours gaine
    et câble ensemble comme un ensemble monobloc. - Négliger le grommets de
    cloison pare-feu : Un grommets craquelé ou mal reposé après le passage du
    câble laisse entrer l'eau de pluie directement dans l'habitacle et les gaz
    d'échappement en cas d'aspiration moteur. Inspectez-le systématiquement et
    remplacez-le si la gomme est durcie ou fissurée. - Tordre le câble en angle
    vif lors du passage : Le câble de compteur transmet un mouvement rotatif —
    tout coude inférieur à 150° crée un point de friction intense qui fait
    vibrer l'aiguille du compteur et brise les fils internes en 3 à 6 mois.
    Respectez les rayons de courbure minimum indiqués par le constructeur
    (généralement 100 mm minimum). - Monter un câble sans lubrifier l'embout
    intérieur : L'extrémité carrée ou hexagonale du câble doit être légèrement
    graissée à la graisse graphitée avant insertion dans le pignon de boîte. Un
    embout monté à sec grince, s'oxyde et devient impossible à démonter lors du
    prochain entretien. - Commander sans vérifier si le véhicule a un compteur
    analogique câblé : Les véhicules fabriqués après 2000 utilisent quasi-
    universellement un capteur de vitesse électronique sur la boîte, sans câble
    mécanique. Si votre véhicule a un compteur numérique ou digital, il n'y a
    pas de câble — cherchez plutôt un capteur de vitesse sur boîte (VSS).
  S6: >-
    - Test de l'affichage au démarrage : Démarrez le moteur et engagez une
    vitesse en maintenant l'embrayage. Observez l'aiguille du compteur : elle
    doit rester à zéro stable. Une aiguille qui oscille sans avancer signale un
    câble mal connecté côté boîte ou un pignon de compteur endommagé. - Test de
    progression à faible vitesse : Roulez à 30 km/h sur une route droite et
    observez l'aiguille — elle doit monter progressivement et tenir stable. Des
    saccades ou une aiguille qui "danse" indiquent un coude trop serré sur le
    parcours du câble ou un câble intérieur non graissé. - Vérification de
    cohérence à 90 km/h : Comparez la vitesse affichée avec un GPS ou
    l'affichage d'un téléphone (application compteur GPS). L'écart acceptable
    est de ±5 % selon la norme européenne. Un compteur qui sous-évalue la
    vitesse signale un câble de mauvais rapport de démultiplication. - Contrôle
    de l'étanchéité du grommets de pare-feu : Par temps de pluie ou après un
    lavage à haute pression, vérifiez l'absence d'humidité sous la planche de
    bord au niveau du passage de câble. - Inspection à 1 000 km : Après rodage,
    vérifiez que les colliers de fixation du câble sont toujours en place et que
    la gaine ne présente pas de traces de frottement contre des pièces mobiles
    ou chaudes.
  S7: >-
    - Capteur d'impulsion (capteur de vitesse) — Sur les véhicules qui ont migré
    vers un comptage électronique, le câble de compteur mécanique est remplacé
    par un capteur d'impulsion monté sur la boîte de vitesses ou le moyeu de
    roue. Si le compteur reste à zéro sur un véhicule hybride
    câble/électronique, le capteur d'impulsion peut avoir pris le relais et être
    défaillant alors que le câble est intact. Vérifier si le système est câble
    seul, électronique seul, ou hybride avant de commander. - Boîtier compteur /
    tableau de bord — Si le câble est intact (tourne librement, pas de casse
    visible) mais que l'aiguille du compteur reste à zéro ou tremble, le boîtier
    d'instruments lui-même peut être en cause : pignon de compteur usé dans le
    tableau de bord, ou liaison électrique défaillante (sur tableaux
    numériques). Tester le câble en le connectant à un boîtier de remplacement
    avant de déposer le tableau de bord. - Joint d'étanchéité de boîte de
    vitesses (côté prise de mouvement) — Le câble de compteur se branche sur la
    boîte de vitesses à travers un passe-câble étanche. Si une fuite d'huile de
    boîte est constatée au niveau du raccord du câble, le joint d'étanchéité du
    passe-câble est percé. Remplacer ce joint lors du changement du câble pour
    éviter une vidange involontaire de la boîte. - Pignons de prise de mouvement
    compteur (galet de boîte) — Le câble entraîne un petit pignon plastique dans
    la boîte de vitesses (le « galet compteur »). Ce pignon s'use indépendamment
    du câble. Si le câble est neuf mais ne tourne pas, le galet dans la boîte
    peut être cassé ou manquant. Vérifier la rotation de l'extrémité du câble
    côté boîte avant de conclure à un câble défaillant. - Gaine de câble de
    compteur — Certains câbles de compteur sont vendus avec ou sans gaine de
    protection. Si la gaine est craquelée, le câble frotte à l'intérieur et
    produit des bruits de grattement ou de ronronnement en proportion de la
    vitesse. Vérifier l'état de la gaine avant de remplacer uniquement le câble
    intérieur.
  S8: >-
    Mon compteur de vitesse est bloqué à zéro : câble ou capteur électronique ?
    Avant de commander un câble, vérifiez si votre véhicule est équipé d'un
    compteur analogique câblé ou d'un capteur de vitesse électronique (VSS). Les
    véhicules avec compteur à câble ont généralement été produits avant
    1995-2000 selon le constructeur. Si votre compteur est numérique ou si votre
    véhicule a une ABS, il est presque certain qu'il utilise un capteur VSS
    électronique — il n'y a pas de câble à remplacer dans ce cas, c'est le
    capteur de vitesse sur boîte qu'il faut diagnostiquer. Pourquoi mon compteur
    oscille-t-il ou saccade-t-il après remplacement du câble ? L'oscillation de
    l'aiguille après remplacement provient de trois causes principales : un
    coude trop serré sur le tracé du câble (angle inférieur à 150°), un manque
    de graisse sur l'embout intérieur du pignon, ou un câble intérieur de
    mauvaise qualité dont les torons ne sont pas uniformes. Commencez par
    vérifier le tracé sous le capot et vous assurer qu'aucune section ne forme
    un coude brutal. Si le problème persiste, le compteur lui-même peut être usé
    (engrenages internes). Peut-on graisser soi-même le câble de compteur sans
    le démonter ? Oui, si le câble est accessible côté tableau de bord. Dévissez
    le raccord du câble sur le compteur et tirez légèrement le câble intérieur
    de sa gaine sur 20-30 cm. Appliquez de la graisse graphitée ou de la graisse
    de câble spéciale sur toute la partie sortie, puis faites rentrer et sortir
    le câble plusieurs fois pour répartir la graisse vers le bas. Cette
    opération prolonge la durée de vie du câble de 1 à 2 ans, surtout sur les
    véhicules qui roulent par temps froid. Le kilométrage du compteur est-il
    affecté par le remplacement du câble ? Non. Le câble de compteur transmet la
    rotation du pignon de boîte de vitesses mais le totalisation du kilométrage
    est effectuée par le mécanisme interne du compteur (totalisateur mécanique
    sur les anciens compteurs, mémoire électronique sur les plus récents). Le
    remplacement du câble n'affecte ni ne réinitialise l'odomètre.
  META: >-
    {"meta_title":"Câble de compteur de vitesse : diagnostic et
    remplacement","meta_description":"Compteur bloqué, aiguille qui saute ou
    lecture erronée ? Identifiez les symptômes d'un câble de compteur de vitesse
    défaillant et sachez quand le remplacer sur votre voiture."}
---

# Câble de compteur de vitesse - Guide Diagnostic et Achat

## Fonction et Role

Le cable de compteur de vitesse (ou cable kilometrique) transmet mecaniquement la rotation des roues au compteur du tableau de bord. Il fonctionne par le principe du courant de Foucault : la rotation des roues entraine un plateau aimante via le cable, et la vitesse de rotation est refletee sur le tachymetre.

**Actions principales:** transmettre la rotation, afficher la vitesse, permettre le controle du vehicule

## Symptomes de Defaillance

### 🔴 Symptomes Critiques (Securite)

- **Compteur bloque a zero** — impossible de connaitre sa vitesse reelle
- **Lecture erronee** — vitesse affichee trop haute ou trop basse

### 🟢 Autres Symptomes

- Aiguille qui saute ou tremble
- Bruit de grincement derriere le tableau de bord
- Compteur kilometrique qui ne tourne plus


## Entretien et Intervalles

- **Intervalle** : selon etat
- Pas de periodicite fixe. Remplacer en cas de panne compteur, bruit ou lecture erronee. Piece typique des vehicules anciens (avant 2000).

## Causes Probables

- **Cable casse** — le fil interieur est rompu dans la gaine
- **Embout use** — l'embout carre ou hexagonal est arrondi, ne s'accroche plus
- **Gaine ecrasee** — pliure empechant la libre rotation du cable
- **Manque de lubrification** — cable sec provoquant grincement et usure acceleree

## Pieces Associees

- **capteur-impulsion** — alternative electronique sur vehicules modernes

## Criteres de Compatibilite

- **Marque, modele et annee** de votre vehicule
- **Longueur exacte** du cable (variable selon modele)
- **Type d'embout** cote transmission et cote compteur
- **Cable mecanique ou capteur electronique** (verifier avant commande)

## ❌ Attention aux Erreurs Frequentes

- ❌ Ne pas confondre cable mecanique et capteur electronique
- ❌ Verifier la longueur exacte avant commande
- ❌ Ne pas forcer l'embout lors du montage
- ❌ Lubrifier le cable neuf avant installation

## FAQ

**Mon vehicule a-t-il un cable ou un capteur electronique ?**
Les vehicules avant 1995-2000 utilisent generalement un cable mecanique. Les vehicules modernes utilisent un capteur electronique (capteur d'impulsion). Verifiez sous le tableau de bord ou pres de la boite de vitesses.

**Comment savoir si le cable est casse ?**
Compteur bloque a zero, aiguille immobile meme en roulant, bruit de grincement au tableau de bord. Debrancher le cable cote compteur et le faire tourner a la main pour verifier.

**Faut-il lubrifier le cable de compteur ?**
Oui, un cable sec grince et s'use plus vite. Utiliser de la graisse legere ou du lubrifiant silicone dans la gaine lors du remplacement.

**Quel est le prix d'un cable de compteur ?**
Entre 8 et 60 EUR selon le vehicule. Le remplacement prend generalement 30 minutes a 1 heure.
