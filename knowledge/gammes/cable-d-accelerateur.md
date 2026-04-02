---
category: accessoires
slug: cable-d-accelerateur
title: Câble d'accélérateur
pg_id: 618
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
  role: Transmet la commande d'accélération de la pédale au papillon
  must_be_true:
  - transmettre
  - actionner
  - commander
  must_not_contain:
  - injection
  - papillon electronique
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - transmettre
  - actionner
  - commander
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de compatibilite
    pour confirmer Câble d'accélérateur.
  - Verifier la reference OE ou equivalence constructeur pour le vehicule exact
  - Comparer les dimensions et le type de montage avec la piece d origine
  - Choisir un equipementier reconnu pour garantir qualite et compatibilite
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "plus de puissance"
  cost_range:
    min: 50
    max: 300
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
    description: 'Câble conforme aux plans constructeur : longueur totale, longueur de gaine, embouts et course libre identiques
      à l''origine. Garantit la réponse accélérateur sans jeu excessif.'
  - tier: Qualité équivalente OE
    description: Câble fabriqué par un équipementier spécialisé respectant les longueurs et la résistance à la traction d'origine.
      Gaine traitée contre la corrosion.
  - tier: Adaptable compatible
    description: Câble universel à ajustement possible. Vérifier la longueur totale, la longueur de gaine et la compatibilité
      des embouts avant montage.
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
    label: Pedale d accelerateur dure ou rigide
    severity: confort
  - id: S2
    label: Reponse moteur retardee a l acceleration
    severity: confort
  - id: S3
    label: Point dur lors de l enfoncement de la pedale
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'Usure ou defaillance causant : pedale d accelerateur dure ou rigide'
  - 'Usure ou defaillance causant : reponse moteur retardee a l acceleration'
  quick_checks:
  - 'Observer : pedale d accelerateur dure ou rigide ?'
  - 'Observer : reponse moteur retardee a l acceleration ?'
  - 'Observer : point dur lors de l enfoncement de la pedale ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Pedale d accelerateur dure ou rigide
  - Reponse moteur retardee a l acceleration
  - Point dur lors de l enfoncement de la pedale
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '618'
  intro_title: A quoi sert Câble d'accélérateur ?
  risk_title: Pourquoi remplacer Câble d'accélérateur a temps ?
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
  - question: Comment choisir Câble d'accélérateur compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Câble d'accélérateur ?
    answer: En cas de pedale d accelerateur dure ou rigide ou de degradation mesurable, il faut controler rapidement avant
      panne secondaire.
  - question: Puis-je monter Câble d'accélérateur sans verification atelier ?
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
doc_id: f11935af-cfbe-5036-954a-f8ac5eaf673e
content_hash: sha256:5cc918f39dbe6cca
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
  _source: contenu LLM — a revalider contre sources OEM
  _validation_status: pending_oem_validation
  _enriched_at: '2026-03-30'
  technical_notes:
    reglage_garde: '5-10 mm de jeu en position repos (vehicules a cable, rares aujourd''hui — remplace par pedale electronique)'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le c&acirc;ble d'accélérateur d'un véhicule a pour fonction de transmettre
    au mécanisme d'accélération/décélération la pression ou le rel&acirc;chement
    du pied de conducteur sur la pédale d'accélérateur, pour contrôler avec
    précision le régime du moteur. Le montage du c&acirc;ble d'accélération se
    varie beaucoup d'un véhicule à un autre, mais le principe de base reste le
    m&ecirc;me. Il s'agit d'un c&acirc;ble métallique, généralement enfilé dans
    une gaine souple après graissage, fixé à la pédale et au levier
    d'accélérateur via un jeu d'ergots et de butées, le tout étant tributaire
    d'un dispositif de ressorts de rappel.
  S2: >-
    Le c&acirc;ble d'accélération n'a pas de période de remplacement mais tout
    comportement bizarre de la pédale d'accélérateur et tout retard de réaction
    du moteur en cas d'accélération/décélération, on doit vérifier l'état du
    c&acirc;ble d'accélérateur si on constate qu'il est à l'origine du problème
    et le remplacer si nécessaire. Les signes d'usure d'un c&acirc;ble
    d'accélérateur sont plusieurs par exemple une pédale trop molle ou trop
    dure, avec des plages d'inertie ou un moteur avec un ralenti irrégulier ou
    trop rapide.
  S3: >-
    - Longueur totale et longueur de gaine : Le câble d'accélérateur est
    dimensionné au millimètre pour que la pédale atteigne sa butée exactement
    quand le papillon est en pleine ouverture. Mesurez la longueur totale et la
    longueur de gaine de l'original avant de commander — une différence de 5 mm
    suffit à créer un point dur ou une pédale molle. - Diamètre et type de câble
    intérieur : Le câble acier intérieur varie de 1,2 à 2,5 mm selon la
    puissance moteur et la résistance au papillon. Un câble trop fin se rompt
    prématurément sous la sollicitation répétée des cycles d'accélération. -
    Forme et dimensions des embouts : L'embout côté pédale (souvent en nylon ou
    métal) et l'embout côté papillon (cylindre fileté ou rotule) doivent être
    identiques à l'origine. Un embout approximatif peut se décrocher en pleine
    accélération. - Type de gaine extérieure : La gaine doit être compatible
    avec les températures sous capot (jusqu'à 120°C dans le compartiment
    moteur). Vérifiez que la gaine est revêtue téflon intérieurement pour
    réduire le frottement — un câble dans une gaine non lubrifiée se rigidifie
    par temps froid. - Compatibilité avec le moteur (carburateur vs injection
    mécanique) : Les véhicules à carburateur et ceux à injection mécanique
    (corps d'injection sans papillon électronique) ont des câbles différents. Ce
    type de câble est réservé aux véhicules sans commande électronique des gaz.
    - Marque, modèle, année et type moteur : Ces quatre données sont
    indispensables pour identifier la référence exacte. Une même carrosserie
    peut recevoir plusieurs types de câbles selon la motorisation (essence 1.4
    vs 1.6, par exemple). Pour aller plus loin : consultez notre guide d'achat
    câble d'accélérateur — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    - Couper le contact et laisser refroidir le moteur : Travaillez moteur
    froid. Le câble passe à proximité du collecteur d'échappement sur certains
    modèles — le risque de brûlure est réel sur moteur chaud. Débranchez la
    batterie si le papillon est assisté électroniquement (pour éviter toute
    activation involontaire). - Repérer le tracé du câble existant : Avant tout
    démontage, photographiez le parcours complet du câble depuis la pédale
    jusqu'au papillon, y compris les colliers, agrafes et guides de gaine. Cette
    référence est indispensable pour reproduire le tracé à l'identique. -
    Déconnexion côté pédale : Sous le tableau de bord, localisez la pédale
    d'accélérateur. Appuyez sur la pédale à la main pour détendre le câble et
    dégagez l'embout du logement dans la pédale (généralement par rotation de
    90°). Retirez ensuite la gaine de son support sur la pédalier. - Déconnexion
    côté papillon : Dans le compartiment moteur, localisez le corps de papillon.
    Détendez le câble en poussant légèrement le secteur du papillon vers
    l'ouverture, puis sortez l'embout de son logement. Dévissez l'écrou de
    réglage de la gaine si présent. - Retirer les colliers et agrafes sur le
    parcours : Dégagez le câble de tous ses points de fixation intermédiaires
    (colliers sur le moteur, agrafes sur le support de batterie ou le berceau)
    en notant leur position exacte. - Extraire le câble complet : Tirez
    délicatement le câble depuis le compartiment moteur vers l'habitacle (ou
    inversement selon le modèle). Si la gaine est rigide par endroits, vérifiez
    qu'aucun collier n'a été oublié. - Installer le nouveau câble : Guidez le
    nouveau câble exactement selon le tracé photographié. Engagez d'abord
    l'embout côté pédale, puis progressez vers le papillon en reposant chaque
    collier à son emplacement d'origine. - Réglage de la tension : La pédale
    doit avoir 2 à 5 mm de jeu avant que le câble ne commence à tirer sur le
    papillon. Trop tendu : le papillon ne revient pas au ralenti. Trop détendu :
    réponse molle à l'accélération. Ajustez via l'écrou de réglage sur la gaine
    côté papillon. - Test de fonctionnement : Démarrez le moteur au ralenti.
    Actionnez la pédale d'accélérateur lentement jusqu'en butée, puis relâchez
    brusquement. Le ralenti doit reprendre immédiatement sans rebond. Répétez 5
    fois pour confirmer.
  S4_REPOSE: >-
    La repose du câble d'accélérateur est indissociable d'un réglage précis de
    la tension. Un câble trop tendu empêche le papillon de revenir au ralenti —
    condition dangereuse en conduite. Un câble trop détendu génère une réponse
    molle et un retard à l'accélération préjudiciable à la sécurité en
    dépassement.- Engager d'abord l'embout côté loquet du papillon : insérer
    l'embout du câble (noisette ou rotule) dans le logement du secteur du
    papillon en commençant par ce côté car c'est le plus contraint en terme
    d'accès sur la plupart des moteurs. Vérifier que l'embout est bien en butée
    dans son logement et ne peut pas s'extraire par un simple tirage.- Faire
    cheminer le câble exactement selon le tracé d'origine : en s'aidant des
    photos prises lors de la dépose, guider le câble le long de son trajet en
    évitant tout coude brusque, tout contact avec les pièces chaudes
    (collecteur, catalyseur) et tout croisement avec d'autres câbles ou durites.
    Respecter scrupuleusement chaque point de guidage intermédiaire.- Fixer
    toutes les agrafes et colliers de maintien : remettre en place chaque agrafe
    plastique et chaque collier sur leur support d'origine. Ne pas en oublier :
    un câble mal maintenu vibre et se fatigue prématurément aux points de
    friction, ou peut entrer en contact avec une pièce en mouvement.- Connecter
    l'embout côté pédale d'accélérateur : accrocher l'embout dans le logement de
    la pédale (rotation à 90° ou enclipsage selon le modèle). S'assurer que la
    gaine est correctement ancrée dans son support sur le tablier.- Effectuer le
    réglage de la tension par l'écrou de réglage sur la gaine : avec le papillon
    en position fermée (ralenti), la pédale d'accélérateur doit présenter un jeu
    de 2 à 5 mm avant que le câble ne commence à tirer sur le secteur. Tourner
    l'écrou de réglage de gaine pour ajuster : vissez pour tendre, dévissez pour
    détendre. Vérifier que le papillon s'ouvre en butée complète quand la pédale
    est enfoncée à fond.- Contrôler le retour au ralenti sans résistance :
    appuyer sur la pédale jusqu'en butée, relâcher brusquement — le papillon
    doit revenir immédiatement en position de fermeture complète sans
    accrochage. Si le retour est lent ou incomplet, réduire la tension du câble
    ou vérifier le ressort de rappel du papillon.- Démarrer le moteur et valider
    le ralenti : le régime de ralenti doit être stable (généralement 700 à 900
    tr/min selon le moteur). Toute augmentation du ralenti au-dessus de 1 200
    tr/min sans actionnement de la pédale indique un câble trop tendu à re-
    ajuster immédiatement.- Tester l'accélération progressive et les pleins gaz
    : depuis le ralenti, accélérer progressivement jusqu'à pleine charge et
    vérifier que la réponse du moteur est linéaire, sans à-coups. Appuyer
    franchement sur la pédale et relâcher 5 fois pour confirmer la répétabilité
    du retour au ralenti.
  S5: >-
    - Ne pas photographier le tracé avant démontage : Le câble d'accélérateur
    suit un tracé précis pour éviter les frottements sur les arêtes du moteur et
    les pièces mobiles. Un mauvais repassage crée des points durs, accélère
    l'usure et peut provoquer un accrochage du câble en pleine accélération — le
    moteur s'emballe sans que la pédale puisse revenir au ralenti. - Monter un
    câble légèrement trop long en "adaptant" avec l'écrou de réglage au maximum
    : L'écrou de réglage de tension est conçu pour de micro-ajustements (±5 mm).
    En l'utilisant pour compenser une mauvaise longueur, vous déplacez le point
    de fixation de la gaine et créez une angulation qui génère un frottement
    excessif et rompt prématurément le câble. - Ignorer le jeu de la pédale
    après réglage : Un câble trop tendu (jeu inférieur à 1 mm) maintient le
    papillon légèrement ouvert en permanence. Le résultat : ralenti instable,
    surconsommation de carburant et usure prématurée du papillon. Vérifiez
    toujours 2 à 5 mm de jeu libre en tête de pédale. - Ne pas lubrifier la
    gaine avant installation : La gaine intérieure doit être légèrement graissée
    à la graisse téflon (ou à la graisse silicone) avant d'insérer le câble. Une
    gaine sèche génère une résistance croissante par temps froid, rendant la
    pédale progressivement plus rigide jusqu'à la rupture du câble par fatigue.
    - Commander sans vérifier la compatibilité avec le type de motorisation : Ce
    composant est exclusivement destiné aux véhicules à commande mécanique des
    gaz. Sur un véhicule avec drive-by-wire (accélérateur électronique), il n'y
    a pas de câble mécanique — si vous cherchez ce composant pour un tel
    véhicule, c'est le capteur de position pédale ou l'actionneur de papillon
    qu'il faut diagnostiquer.
  S6: >-
    - Contrôle du jeu de pédale : Moteur froid avant démarrage, appuyez
    doucement sur la pédale — vous devez sentir 2 à 5 mm de course libre avant
    que la résistance du câble ne commence. Aucun point dur ne doit être
    perceptible sur toute la course. - Test de retour au ralenti : Démarrez et
    laissez le moteur atteindre sa température normale. Accélérez brièvement à
    mi-régime puis relâchez la pédale d'un coup. Le ralenti doit reprendre
    immédiatement (moins de 1 seconde). Un retour lent signale un câble trop
    tendu ou mal guidé. - Vérification du papillon en butée : Avec l'aide d'un
    assistant, appuyez à fond sur la pédale et observez le secteur du papillon
    sous capot : il doit atteindre sa butée mécanique d'ouverture maximale. S'il
    reste à mi-course, le câble est trop long ou mal réglé. - Inspection
    visuelle du tracé : Moteur tournant, vérifiez visuellement que le câble ne
    frotte pas sur les parties mobiles (poulies d'alternateur, ventilateur), les
    pièces chaudes (collecteur) ou les arêtes métalliques du berceau moteur. -
    Test par temps froid : Si vous effectuez l'intervention en été, refaites un
    test de souplesse de pédale lors de la première matinée froide (en dessous
    de 5°C). Une gaine mal lubrifiée révèle sa rigidité uniquement par temps
    froid.
  S7: >-
    Le câble d'accélérateur transmet mécaniquement la commande de la pédale au
    papillon des gaz. Sa défaillance — rigidité, point dur, rupture — est
    rarement isolée : les éléments en contact direct avec lui s'usent en même
    temps et doivent être inspectés lors du remplacement. - Gaine de câble — le
    câble coulisse dans une gaine souple qui se rigidifie, se fissure ou se
    déplie avec l'âge. Une gaine abîmée crée un point dur sur le câble même si
    le câble lui-même est sain. Remplacer la gaine systématiquement avec le
    câble si le kit le permet. - Papillon des gaz — le câble s'accroche sur un
    secteur denté du papillon. Un papillon encrassé de dépôts carbonés augmente
    l'effort de rappel et accélère l'usure du câble. Nettoyer le papillon avec
    un nettoyant dédié lors du remplacement du câble. - Pédale d'accélérateur —
    le point d'attache du câble sur la pédale (clip ou goujette) peut se
    déformer ou se rompre, générant un jeu excessif. Contrôler l'état du clip de
    pédale et le lubrifier légèrement à la graisse silicone. - Ressort de rappel
    du papillon — assure le retour en position fermée lorsque le pied quitte la
    pédale. Un ressort fatigué ou cassé empêche la fermeture complète du
    papillon — situation dangereuse. Tester le rappel avant et après
    remplacement du câble. - Supports et clips de cheminement — le câble est
    maintenu par des clips plastiques le long du moteur. Des clips cassés
    laissent le câble frotter sur des surfaces chaudes ou des pièces mobiles,
    entraînant une usure rapide. Remplacer tous les clips déficients lors de la
    pose du câble neuf.
  S8: >-
    Comment savoir si mon véhicule a un câble d'accélérateur ou un accélérateur
    électronique ? Les véhicules équipés d'un câble mécanique ont été fabriqués
    en majorité avant 2005-2010 selon les constructeurs. Pour vérifier, ouvrez
    le capot et cherchez un câble gainé reliant la pédale au corps de papillon :
    si vous le voyez, votre véhicule est à commande mécanique. Les véhicules à
    drive-by-wire (commande électronique) n'ont qu'un faisceau électrique sur la
    pédale et un motoréducteur sur le papillon — aucun câble visible. Pédale
    d'accélérateur dure : câble à changer ou simple lubrification ? Commencez
    par la lubrification. Injectez un dégrippant téflon ou silicone en spray
    dans la gaine depuis l'embout côté pédale. Actionnez la pédale plusieurs
    fois pour répartir le lubrifiant sur toute la longueur du câble. Si la
    rigidité persiste après 2-3 essais ou si des fils du câble sont apparents,
    le remplacement complet s'impose. Un câble dont les fils internes sont
    partiellement rompus peut se bloquer en position ouverte — situation
    dangereuse. Peut-on rouler avec un câble d'accélérateur partiellement rompu
    ? Non. Un câble dont seulement une partie des fils acier est intacte peut se
    rompre sans préavis. La rupture complète en conduite bloque le papillon en
    position fermée (moteur coupe) ou, pire, en position entrouverte (ralenti
    élevé incontrôlable). Dès la détection d'un câble endommagé — point dur,
    effilement visible, fils rompus — immobilisez le véhicule et remplacez le
    câble avant tout déplacement. Quel jeu de pédale est normal sur un câble
    d'accélérateur ? Le jeu libre acceptable est de 2 à 5 mm mesuré en tête de
    pédale avant que la résistance du câble ne commence. En dessous de 1 mm, le
    papillon est maintenu légèrement ouvert en permanence : ralenti instable et
    surconsommation. Au-delà de 8-10 mm, la réponse à l'accélération est molle
    avec un temps de latence perceptible. Le réglage s'effectue via l'écrou de
    tension sur la gaine côté papillon, par demi-tours successifs.
  META: >-
    {"meta_title":"Câble d'accélérateur : diagnostic et remplacement |
    AutoMecanik","meta_description":"Pédale d'accélérateur dure, réponse moteur
    retardée ou point dur à l'enfoncement ? Guide de diagnostic et remplacement
    du câble d'accélérateur.","og_title":"Câble d'accélérateur défaillant :
    causes et remplacement | AutoMecanik","og_description":"Pédale rigide,
    réponse retardée, point dur : diagnostiquer et remplacer le câble
    d'accélérateur selon marque, modèle et
    année.","schema_type":"HowTo","canonical_hint":"/pieces/cable-d-
    accelerateur"}
---

# Câble d'accélérateur - Guide Diagnostic Complet

## Fonction et Rôle

Transmet la commande d'accélération de la pédale au papillon

**Actions principales:** transmettre, actionner, commander

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- pedale d accelerateur dure ou rigide
- reponse moteur retardee a l acceleration
- point dur lors de l enfoncement de la pedale

## Procédure de Diagnostic

Pour diagnostiquer un problème de câble d'accélérateur:

1. **Inspection visuelle** - Examiner l'état du câble d'accélérateur
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

- pedale
- papillon

## Critères de Compatibilité

Pour commander le bon câble d'accélérateur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"

## FAQ

**Comment choisir Câble d'accélérateur compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Câble d'accélérateur ?**
En cas de pedale d accelerateur dure ou rigide ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Câble d'accélérateur sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
