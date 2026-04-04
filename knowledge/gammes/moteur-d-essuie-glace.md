---
category: accessoires
slug: moteur-d-essuie-glace
title: Moteur d'essuie-glace
pg_id: 295
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
  role: Entraîne le mécanisme d'essuyage via la tringlerie
  must_be_true:
  - entrainer
  - actionner
  - alimenter
  must_not_contain:
  - balai
  - caoutchouc
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - entrainer
  - actionner
  - alimenter
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
    min: 50
    max: 300
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    price_range: Prix élevé — pièce strictement identique à l'origine
  - tier: Équivalent OE (OES)
    price_range: Prix intermédiaire — recommandé dans la majorité des cas
  - tier: Aftermarket standard
    price_range: Prix bas — vérifier impérativement la compatibilité connectique
  brands:
    premium:
    - Bosch
    - Valeo
    standard:
    - SWF
    - Hella
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Essuie-glaces totalement inactifs
    severity: confort
  - id: S2
    label: Mouvement tres lent
    severity: confort
  - id: S3
    label: Arret en position aleatoire
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : essuie-glaces totalement inactifs'
  quick_checks:
  - 'Observer : essuie-glaces totalement inactifs ?'
  - 'Observer : mouvement tres lent ?'
  - 'Observer : arret en position aleatoire ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Essuie-glaces totalement inactifs
  - Mouvement tres lent
  - Arret en position aleatoire
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '295'
  intro_title: A quoi sert Moteur d'essuie-glace ?
  risk_title: Pourquoi remplacer Moteur d'essuie-glace a temps ?
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
  - question: Comment choisir Moteur d'essuie-glace compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Moteur d'essuie-glace ?
    answer: En cas de essuie-glaces totalement inactifs ou de degradation mesurable, il faut controler rapidement avant panne
      secondaire.
  - question: Puis-je monter Moteur d'essuie-glace sans verification atelier ?
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
doc_id: 6c30109f-eb26-530f-8a5e-2e4649cd8111
content_hash: sha256:275bd32a164a143c
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
  - type: 'électrique'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le moteur d'essuie-glace est le composant électromécanique chargé
    d'entraîner le mécanisme d'essuyage via la tringlerie. Lorsque vous activez
    les essuie-glaces, le moteur convertit l'énergie électrique fournie par le
    circuit de bord en mouvement rotatif, lequel est ensuite transmis aux bras
    d'essuie-glace par un système de biellettes articulées. Le moteur comporte
    généralement deux vitesses d'actionnement (lente et rapide) contrôlées par
    un commutateur sur la colonne de direction. Sur les véhicules modernes, un
    troisième niveau intermittent — parfois réglable — est géré
    électroniquement, voire automatiquement via un capteur de pluie. Un
    dispositif de fin de course intégré au moteur assure que les balais
    reviennent systématiquement en position basse après l'arrêt, quelle que soit
    la position du commutateur. Le moteur d'essuie-glace actionne la tringlerie
    qui relie les deux bras via des rotules. Toute défaillance du moteur prive
    instantanément le conducteur de visibilité par temps de pluie, ce qui en
    fait une pièce directement liée à la sécurité active du véhicule. Il
    convient de l'alimenter correctement (12V continu) et de vérifier la
    continuité du relais associé avant de conclure à un remplacement.
  S2: >-
    Un moteur d'essuie-glace défaillant se manifeste le plus souvent
    progressivement. Plusieurs signaux doivent alerter le conducteur avant la
    panne totale, car intervenir tôt évite une dégradation en chaîne sur la
    tringlerie et les bras. - Essuie-glaces totalement inactifs : aucun
    mouvement lors de l'activation du commutateur, quelle que soit la vitesse
    sélectionnée. Cause probable : moteur hors service ou fusible grillé. -
    Mouvement très lent : les balais se déplacent à vitesse anormalement réduite
    même en position rapide, traduisant un moteur en fin de vie dont les
    charbons ou l'enroulement sont usés. - Arrêt en position aléatoire : les
    balais s'immobilisent en milieu de course au lieu de revenir en position
    basse, signe d'une défaillance du dispositif de fin de course interne. -
    Vibrations ou à-coups : le mouvement saccadé lors de l'essuyage peut
    signaler un moteur dont les roulements internes sont détériorés. - Bruit de
    frottement ou grincement anormal : un moteur en mauvais état produit un
    bruit caractéristique distinct du frottement normal des balais sur le pare-
    brise. - Surchauffe du moteur : un moteur grippé ou surchargé par une
    tringlerie déformée chauffe excessivement, ce qui peut provoquer l'ouverture
    du fusible de protection de façon répétée. - Panne intermittente : le
    système fonctionne par intermittence, souvent liée à un défaut de contact
    dans les charbons ou à un problème de relais associé.
  S3: >-
    Le moteur d'essuie-glace est une pièce strictement spécifique au véhicule.
    Les dimensions mécaniques, les connecteurs électriques et la position de la
    sortie d'arbre varient d'un modèle à l'autre. Un moteur non conforme ne peut
    pas être monté ou entraînera un dysfonctionnement de la tringlerie. - Marque
    et modèle du véhicule : le premier filtre indispensable. Des véhicules
    d'apparence similaire peuvent utiliser des motorisations d'essuyage
    entièrement différentes selon la génération. - Année de mise en circulation
    : un même modèle peut avoir été équipé de moteurs différents selon le
    millésime, en particulier lors d'un facelift ou d'un changement de
    fournisseur en cours de production. - Type de motorisation : essence, diesel
    ou hybride peuvent influer sur la configuration électrique du véhicule et
    donc sur les spécifications du moteur d'essuyage. - Vérifier le symptôme
    avant de commander : s'assurer que le moteur est bien en cause et non le
    fusible, le relais ou un câblage défectueux, afin d'éviter une commande
    inutile. - Référence constructeur ou OEM : privilégier un moteur portant la
    référence d'origine ou une référence équivalent certifiée par
    l'équipementier (Valeo, Bosch, Denso, etc.). - Motorisation avant ou arrière
    : les véhicules break ou SUV disposent d'un essuie-glace arrière avec son
    propre moteur, distinct de celui de l'avant. Préciser l'emplacement lors de
    la commande. - Connexion électrique : vérifier le nombre de broches du
    connecteur (2, 3 ou 5 fils selon les véhicules) pour s'assurer de la
    compatibilité directe avec le faisceau existant. Pour aller plus loin :
    consultez notre guide d'achat moteur d'essuie-glace — comparatif marques,
    critères de choix et prix.
  S4_DEPOSE: >-
    Le remplacement du moteur d'essuie-glace nécessite de travailler sous le
    capot, dans le caisson de ventilation ou derrière la planche de bord selon
    les modèles. Débrancher la batterie avant toute intervention sur le circuit
    électrique. - Mettre les essuie-glaces en position de service : activer
    brièvement les essuie-glaces, puis les arrêter en position haute (en milieu
    de course) pour faciliter l'accès aux bras. - Déposer les bras d'essuie-
    glace : soulever le capuchon plastique au pied de chaque bras, dévisser
    l'écrou central et extraire le bras de son cannelage à l'aide d'un levier ou
    d'un arrache-bras. - Déposer le cache de la glissière de pare-brise :
    retirer les clips ou vis qui maintiennent la grille en plastique devant le
    pare-brise pour accéder à la tringlerie. - Débrancher le connecteur
    électrique du moteur : presser le verrou et tirer le connecteur
    perpendiculairement sans forcer pour ne pas casser les languettes de
    verrouillage. - Déposer les fixations de la tringlerie : dévisser les écrous
    ou boulons reliant la tringlerie au châssis et libérer l'ensemble
    tringlerie-moteur. - Dévisser le moteur de son support : retirer les 3 à 4
    boulons de fixation du moteur et le dégager de la tringlerie en notant
    l'orientation de l'arbre de sortie. - Monter le nouveau moteur : positionner
    le nouveau moteur en respectant l'orientation d'origine, serrer les boulons
    au couple constructeur (généralement 8 à 12 Nm). - Rebrancher le connecteur
    : s'assurer du clic de verrouillage avant de reconnecter la batterie. -
    Repositionner les bras d'essuie-glace : replacer les bras en position basse
    (repos), serrer l'écrou central et remettre le capuchon en place. - Tester
    le fonctionnement : vérifier les deux vitesses et le retour automatique en
    position basse après arrêt.
  S4_REPOSE: >-
    Après le remplacement du moteur d'essuie-glace, le réglage correct des bras
    d'essuie-glace et la validation du fonctionnement en conditions réelles sont
    indispensables. Un bras mal positionné en angle peut rayer le pare-brise ou
    décrocher en marche arrière. - Vérifier la position de repos des bras avant
    de reconnecter la batterie : avant de remettre le contact, s'assurer que les
    bras d'essuie-glace sont en position basse (position de repos) et que la
    commande d'arbre de sortie du nouveau moteur est en position correspondante.
    Un décalage angulaire de l'arbre de sortie par rapport à la tringlerie
    entraîne un arc de balayage incorrect et un arrêt hors de la zone de repos.
    - Replacer et serrer les bras au couple correct : engager chaque bras sur
    son cannelage en position basse. Serrer l'écrou de fixation du bras au
    couple constructeur (généralement 15 à 20 Nm). Un bras insuffisamment serré
    glisse sur le cannelage progressivement et modifie l'angle de balayage au
    fil des utilisations. Remettre les capuchons de protection des écrous en
    place. - Tester le fonctionnement en deux vitesses : avec la batterie
    reconnectée, activer les essuie-glaces en vitesse lente puis en vitesse
    rapide. Observer la fluidité du mouvement — une hésitation ou un à-coup en
    début de cycle indique un mauvais engagement de la tringlerie sur l'arbre de
    sortie du moteur. Vérifier que les deux bras bougent de manière synchrone. -
    Vérifier l'arrêt automatique en position basse : arrêter les essuie-glaces
    en position intermédiaire (bras relevés), puis couper le commutateur. Le
    moteur d'essuie-glace doit ramener automatiquement les bras en position de
    repos (basse). Si les bras s'arrêtent en position haute, vérifier le câblage
    du contact de fin de course dans le connecteur du moteur. - Tester la
    fonction intermittente et la temporisation : activer le mode intermittent et
    vérifier que le délai entre deux cycles correspond au réglage de la molette
    de temporisation. Un moteur dont la fonction intermittente est absente ou
    non réglable peut indiquer un connecteur mal embroché ou un branchement
    inverse des fils de commande. - Contrôle visuel du joint de capot et de
    l'absence de bruits parasites : refermer le capot et activer les essuie-
    glaces depuis l'habitacle. Écouter l'absence de bruits de frottement contre
    le capot ou la carrosserie. Un bras trop haut peut toucher le capot lors du
    cycle — ajuster la position angulaire du bras sur son cannelage si
    nécessaire. - Test en conditions pluvieuses réelles (ou simulation) :
    humecter le pare-brise et activer les essuie-glaces. Vérifier que les balais
    assurent un essuyage propre sur toute la zone de balayage sans sauter ni
    rebondir. Si les balais étaient usés avant l'intervention, les remplacer
    pour ne pas imputer leurs défauts de balayage au nouveau moteur.
  S5: >-
    Plusieurs erreurs récurrentes sont constatées lors du diagnostic ou du
    remplacement du moteur d'essuie-glace. Les éviter permet de garantir un
    montage fiable et d'éviter une récidive de panne. - Négliger le contrôle du
    fusible et du relais avant de déposer le moteur : un fusible grillé ou un
    relais défectueux provoquent exactement les mêmes symptômes qu'un moteur HS.
    Tester d'abord ces éléments, bien moins coûteux à remplacer, permet d'éviter
    une dépose inutile. - Repositionner les bras d'essuie-glace sans vérifier la
    position de repos du moteur : le moteur doit être en position de fin de
    course basse avant de remonter les bras. Ignorer ce point entraîne un
    décalage de la position de repos, les balais s'arrêtant en milieu de pare-
    brise. - Forcer sur le connecteur électrique : les connecteurs du moteur
    d'essuie-glace sont fragiles. Tirer sans appuyer sur le verrou casse les
    languettes et oblige à remplacer le faisceau partiel, augmentant
    significativement le coût de la réparation. - Commander un moteur universel
    sans vérifier les références : un moteur présenté comme "universel" ou "tous
    modèles" n'est pas adapté à votre véhicule. L'arbre de sortie, les fixations
    et le connecteur doivent correspondre exactement à la référence d'origine. -
    Omettre de vérifier l'état de la tringlerie lors du remplacement : un moteur
    neuf monté sur une tringlerie déformée ou à rotules usées sera soumis à un
    couple de résistance excessif et tombera prématurément en panne. Contrôler
    systématiquement les articulations de la tringlerie lors de chaque
    intervention.
  S6: >-
    Une fois le moteur d'essuie-glace changé et les bras repositionnés, une
    série de contrôles s'impose avant de remettre le véhicule en service. -
    Position de repos des balais : mettre le contact, activer puis arrêter les
    essuie-glaces et vérifier que les balais reviennent bien en position basse
    (en butée contre le joint de pare-brise), sans s'arrêter en milieu de
    course. - Fonctionnement aux deux vitesses : tester la vitesse lente
    (position 1) et la vitesse rapide (position 2) en s'assurant que le moteur
    atteint la cadence nominale sans bruit anormal ni à-coup. - Fonctionnement
    intermittent : vérifier la temporisation en mode intermittent (si
    disponible), le moteur devant s'activer et s'arrêter régulièrement sans
    à-coup. - Absence de bruit de frottement de tringlerie : écouter
    attentivement lors du premier cycle pour détecter tout bruit de frottement
    indiquant une rotule mal positionnée ou un bras mal fixé. - Contrôle du
    fusible associé : vérifier que le fusible du circuit d'essuyage est de la
    valeur préconisée (généralement 20A à 30A) et qu'il ne saute pas lors des
    premiers essais. - Étanchéité du cache de glissière : s'assurer que la
    grille plastique devant le pare-brise est correctement reclipsée, sans jour
    qui laisserait pénétrer l'eau vers le moteur ou le faisceau électrique. -
    Test sous pluie ou avec jet d'eau : valider le fonctionnement en conditions
    humides pour confirmer que le remplacement a bien résolu le problème
    initial.
  S7: >-
    Le moteur d'essuie-glace entraîne l'ensemble du mécanisme d'essuyage via la
    tringlerie. Sa défaillance ou son remplacement impose d'inspecter les
    composants directement liés dans la même chaîne cinématique. Remplacer le
    moteur sans vérifier ces pièces expose à une récidive rapide ou à une panne
    résiduelle non résolue. - Tringlerie d'essuie-glace — La tringlerie transmet
    le mouvement du moteur aux bras. Un axe grippé ou une rotule usée provoque
    le même symptôme qu'un moteur défaillant (mouvement lent, arrêt aléatoire).
    À contrôler systématiquement avant de conclure à un moteur HS. - Bras
    d'essuie-glace — Le bras est solidaire de la tringlerie. Un bras corrodé ou
    dont l'axe de fixation est usé peut bloquer mécaniquement le moteur ou
    générer un mouvement saccadé. Vérifier le serrage et l'état de l'axe
    cannelé. - Balai d'essuie-glace — Un balai cassé, gelé ou trop résistant
    peut surcharger le moteur jusqu'à griller le mécanisme de protection
    thermique interne. À remplacer dès l'apparition de traces ou de claquements
    sur le pare-brise. - Relais d'essuie-glace — Le relais commande
    l'alimentation électrique du moteur. Un relais défaillant coupe
    l'alimentation intermittente ou bloque le moteur sur une vitesse. À tester
    au multimètre avant de remplacer le moteur. - Commutateur / manette
    d'essuie-glace — La manette envoie le signal de vitesse et d'intervalle. Un
    contact interne défaillant peut simuler une panne moteur. À vérifier si le
    moteur fonctionne lors d'un test direct sous tension mais pas depuis la
    manette. - Joint de caisson d'essuie-glace — Le caisson abritant le moteur
    et la tringlerie peut accumuler de l'eau si ses joints sont percés.
    L'humidité accélère la corrosion du moteur et des connecteurs. À inspecter
    et sceller lors de chaque intervention dans cette zone.
  S8: >-
    Quelle est la durée de vie moyenne d'un moteur d'essuie-glace ? Un moteur
    d'essuie-glace est conçu pour durer toute la vie du véhicule dans des
    conditions normales d'utilisation. La panne survient le plus souvent après
    150 000 à 250 000 km, ou en cas de sollicitation excessive (essuie-glaces
    actionnés sur vitre sèche ou sur neige durcie), ce qui use prématurément les
    charbons et les roulements internes du moteur. Mon moteur d'essuie-glace est
    en panne : est-ce forcément le moteur qui est défaillant ? Pas
    nécessairement. Avant de conclure à un moteur défaillant, vérifier dans
    l'ordre : le fusible dédié au circuit d'essuyage (souvent de 20A à 30A dans
    le boîtier fusibles habitacle ou moteur), le relais d'essuie-glace, la
    continuité du câblage entre le commutateur et le moteur, et enfin l'état des
    broches du connecteur du moteur. Ces vérifications évitent de remplacer un
    moteur encore fonctionnel. Puis-je commander un moteur d'essuie-glace sans
    connaître la référence constructeur ? Il est possible de trouver la pièce
    compatible en renseignant la marque, le modèle, l'année de mise en
    circulation et le type de motorisation du véhicule dans le sélecteur de
    compatibilité. Cela permet d'identifier la référence exacte correspondant à
    votre véhicule. Eviter de commander uniquement par le numéro visible sur
    l'ancien moteur, car ce numéro peut être celui de l'équipementier et
    différer de la référence catalogue. Le remplacement du moteur d'essuie-glace
    est-il accessible à un non-professionnel ? Sur la majorité des véhicules
    courants, l'intervention est accessible à un mécanicien amateur disposant
    des outils de base (clés à douille, arrache-bras). La difficulté principale
    est l'accès au moteur, parfois situé dans un caisson profond sous la
    glissière de pare-brise. Sur certains véhicules haut de gamme ou à
    architecture compacte, le démontage partiel du tableau de bord peut être
    nécessaire, auquel cas une intervention en atelier s'impose.
  META: >-
    {"meta_title":"Moteur d'essuie-glace : quand changer ? |
    AutoMecanik","meta_description":"Essuie-glaces inactifs, mouvement lent ou
    arrêt en position aléatoire ? Diagnostic et guide de remplacement du moteur
    d'essuie-glace selon votre véhicule.","og_title":"Moteur d'essuie-glace :
    symptômes et remplacement | AutoMecanik","og_description":"Identifiez les
    signes de défaillance du moteur d'essuie-glace : inactifs, lents, position
    aléatoire. Guide technique par
    véhicule.","schema_type":"HowTo","canonical_hint":"/pieces/moteur-d-essuie-
    glace"}
---

# Moteur d'essuie-glace - Guide Diagnostic Complet

## Fonction et Rôle

Entraîne le mécanisme d'essuyage via la tringlerie

**Actions principales:** entrainer, actionner, alimenter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- essuie-glaces totalement inactifs
- mouvement tres lent
- arret en position aleatoire

## Procédure de Diagnostic

Pour diagnostiquer un problème de moteur d'essuie-glace:

1. **Inspection visuelle** - Examiner l'état du moteur d'essuie-glace
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

- tringlerie
- bras
- balai

## Critères de Compatibilité

Pour commander le bon moteur d'essuie-glace, vous devez connaître:

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

**Comment choisir Moteur d'essuie-glace compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Moteur d'essuie-glace ?**
En cas de essuie-glaces totalement inactifs ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Moteur d'essuie-glace sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
