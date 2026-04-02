---
category: moteur
slug: joint-de-boite-vitesse
title: Joint de boîte vitesse
pg_id: 146
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
  role: Assurer l'etancheite de la boite de vitesses contre les fuites d'huile
  must_be_true:
  - assurer l'etancheite
  - proteger
  must_not_contain:
  - freinage
  - climatisation
  - direction
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - cardan
  - soufflet-de-cardan
  - roulement-de-roue
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de moteur pour
    confirmer Joint de boîte vitesse.
  - Verifier la reference OE ou equivalence constructeur pour le vehicule exact
  - Comparer les dimensions et le type de montage avec la piece d origine
  - Choisir un equipementier reconnu pour garantir qualite et compatibilite
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "repare le moteur"
  cost_range:
    min: 1000
    max: 5000
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Equipement d'origine (OE)
    description: Joint agréé par le constructeur de la boîte. Dimensions et matériau identiques à la première monte.
  - tier: Equivalent OE (OES)
    description: Fabricants spécialisés en étanchéité automobile, approvisionnant les équipementiers de première monte.
  - tier: Adaptable multi-référence
    description: Joints compatibles plusieurs types de boîtes. Nécessite vérification des cotes extérieures, intérieures et
      de la lèvre d'étanchéité.
  brands:
    premium:
    - SKF
    - GKN/Spidan
    standard:
    - Febi
    - Meyle
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Fuite d huile au niveau de la boite
    severity: confort
  - id: S2
    label: Traces d huile sur le sol de garage
    severity: confort
  - id: S3
    label: Niveau d huile de boite insuffisant
    severity: confort
  causes:
  - identifier origine fuite et verifier joints
  - 'Usure ou defaillance causant : fuite d huile au niveau de la boite'
  - 'Usure ou defaillance causant : traces d huile sur le sol de garage'
  quick_checks:
  - Fuite d huile au niveau de la boite ?
  - 'Observer : traces d huile sur le sol de garage ?'
  - 'Observer : niveau d huile de boite insuffisant ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Fuite d huile au niveau de la boite
  - Traces d huile sur le sol de garage
  - Niveau d huile de boite insuffisant
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '146'
  intro_title: A quoi sert Joint de boîte vitesse ?
  risk_title: Pourquoi remplacer Joint de boîte vitesse a temps ?
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
  - question: Comment choisir Joint de boîte vitesse compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Joint de boîte vitesse ?
    answer: En cas de fuite d huile au niveau de la boite ou de degradation mesurable, il faut controler rapidement avant
      panne secondaire.
  - question: Puis-je monter Joint de boîte vitesse sans verification atelier ?
    answer: Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure
      constructeur.
  quality:
    score: 60
    source: script:rag-upgrade-v4
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
doc_id: 175a0fc0-05d2-5b43-807f-f5fe0798b438
content_hash: sha256:b0b390fd92706d05
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
  area: Sous le vehicule, relie la boite aux roues
  access: Par le dessous (pont elevateur)
  adjacent_parts:
  - cardan
  - soufflet
  - roulement de roue
  - boite
installation:
  difficulty: difficile
  time: 1h a 3h
  tools:
  - pont elevateur
  - cle a douille
  - arrache-cardan
  prerequisite: Vidange huile de boite si cardan depose
phase5_enrichment:
  _source: contenu LLM — a revalider contre sources OEM
  _validation_status: pending_oem_validation
  _enriched_at: '2026-03-30'
  technical_notes:
    huile_bvm: '75W-80 ou 75W-90 GL4 selon constructeur — NE PAS utiliser GL5 sur boites synchronisees'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le joint de boîte vitesse est un composant d'étanchéité positionné aux
    interfaces de la boîte de vitesses — en particulier autour des arbres
    d'entrée et de sortie, ainsi qu'au niveau du carter. Sa mission technique
    consiste à assurer l'étanchéité de la boîte de vitesses contre les fuites
    d'huile, en maintenant l'huile de transmission à l'intérieur du carter tout
    en empêchant l'eau, la poussière et les contaminants extérieurs de pénétrer
    dans le mécanisme. La boîte de vitesses baigne dans de l'huile de
    transmission dont le rôle est de lubrifier les engrenages, les roulements et
    les synchroniseurs. Sans étanchéité correcte, cette huile s'échappe
    progressivement et les pièces internes se retrouvent en contact métal contre
    métal. Le joint de boîte vitesse protège donc l'ensemble de la transmission
    d'une dégradation accélérée. Fabriqués en caoutchouc synthétique ou en
    matériau composite résistant aux hydrocarbures et aux températures élevées
    (jusqu'à 150 °C en régime continu), ces joints vieillissent avec le temps :
    les cycles thermiques successifs, le contact permanent avec l'huile de boîte
    et les contraintes mécaniques les font durcir et perdre leur souplesse. Un
    joint durci ne peut plus s'adapter aux microdéformations de l'arbre et
    laisse filtrer l'huile. Les pièces directement associées lors d'une
    intervention sont la boîte de vitesses, le joint d'étanchéité de carter,
    ainsi que les roulements d'arbres. Intervenir sur le joint de boîte vitesse
    sans vérifier l'état du niveau d'huile et des pièces adjacentes est une
    erreur fréquente qui conduit à des pannes secondaires coûteuses.
  S2: >-
    Un joint de boîte vitesse défaillant se manifeste par des signes progressifs
    qu'il convient d'identifier tôt pour éviter la détérioration des pièces
    internes. Voici les symptômes les plus fréquents : - Fuite d'huile au niveau
    de la boîte de vitesses : tache d'huile noire ou marron sous le véhicule,
    côté transmission, visible après stationnement prolongé. C'est le signe le
    plus direct d'un joint percé ou durci. - Traces d'huile sur le sol de garage
    : flaque ou trainée d'huile de transmission sous la zone moteur-boîte.
    L'huile de boîte est généralement plus épaisse et plus sombre que l'huile
    moteur. - Niveau d'huile de boîte insuffisant : contrôle du niveau révélant
    une perte anormale sans autre cause identifiable. Un niveau bas entraîne une
    lubrification insuffisante des engrenages et des synchroniseurs. - Odeur de
    brûlé autour de la boîte : l'huile qui fuit peut entrer en contact avec des
    pièces chaudes (pot d'échappement, carter) et produire une odeur
    caractéristique de caoutchouc ou d'huile chauffée. - Difficultés de passage
    de vitesses : si le niveau d'huile a baissé de façon significative, la
    lubrification des synchroniseurs se dégrade, rendant les passages de
    rapports moins fluides, notamment à froid. - Vibrations ou bruit de
    grondement en mouvement : une boîte mal lubrifiée suite à une fuite
    prolongée peut développer des bruits d'engrenages caractéristiques, signe
    d'usure avancée des pièces internes. Ne pas attendre la panne complète pour
    intervenir. Un joint de boîte vitesse fuyant détecté tôt se remplace à coût
    modéré ; une boîte de vitesses abîmée par manque d'huile peut nécessiter une
    révision complète ou un échange standard.
  S3: >-
    Le choix d'un joint de boîte vitesse repose sur des critères de
    compatibilité stricts. Un joint de mauvaise cote ou de matériau inadapté ne
    garantira pas l'étanchéité attendue. Voici les points à valider avant toute
    commande : - Marque, modèle et année du véhicule : la référence constructeur
    est l'identifiant le plus sûr. Renseignez précisément votre marque, modèle,
    variante de carrosserie et année de mise en circulation pour accéder aux
    références compatibles. - Type de motorisation et code moteur : un même
    modèle de véhicule peut recevoir plusieurs boîtes de vitesses selon la
    motorisation (essence, diesel, hybride) et la puissance. Le code moteur
    (visible sur la carte grise ou sur le bloc moteur) permet de lever toute
    ambiguïté. - Type de boîte de vitesses : boîte mécanique à 5 ou 6 rapports,
    boîte robotisée, transmission intégrale — chaque configuration implique des
    joints spécifiques en termes de dimensions (diamètre intérieur, diamètre
    extérieur, épaisseur) et de matériaux. - Position du joint sur la boîte : le
    joint d'arbre primaire (côté moteur), le joint d'arbre secondaire (côté
    roue) et le joint de sélecteur n'ont pas les mêmes cotes. Identifiez
    précisément le joint à remplacer avant de commander. - Matériau de l'élément
    d'étanchéité : préférez les joints en NBR (nitrile) ou FKM (Viton) pour leur
    résistance à l'huile de transmission et aux températures élevées. Les joints
    en caoutchouc standard vieillissent prématurément dans cet environnement. -
    Vérification des pièces associées : lors du remplacement, vérifiez l'état de
    la portée d'arbre (strie d'usure pouvant imposer un joint à lèvre double) et
    le niveau d'huile de boîte à corriger après montage. - Comparer la référence
    OEM avec les références alternatives : utilisez la référence d'origine
    constructeur comme base de comparaison pour valider toute référence
    aftermarket proposée. Pour aller plus loin : consultez notre guide d'achat
    joint de boîte vitesse — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    Le remplacement d'un joint de boîte vitesse nécessite d'accéder à l'arbre
    concerné après démontage partiel de la transmission. L'intervention varie
    selon la position du joint (arbre primaire, secondaire, sélecteur) et le
    type de boîte. Voici la procédure générale : - Préparer le véhicule : placer
    le véhicule sur un pont ou des chandelles stables. Déposer la roue et le
    passage de roue si nécessaire pour accéder côté arbre de transmission.
    Prévoir un bac de récupération pour l'huile de boîte. - Vidanger
    partiellement l'huile de boîte : déboulonner le bouchon de vidange de la
    boîte et laisser s'écouler l'huile dans le bac de récupération. Cela évite
    un déversement lors de la dépose de l'arbre de transmission. - Déposer
    l'arbre de transmission : désaccoupler le joint homocinétique côté boîte en
    déposant la vis de fixation ou en extrayant l'arbre à la barre à mine (selon
    le type d'accouplement). Protéger la soufflet de joint homocinétique pendant
    cette opération. - Extraire l'ancien joint : utiliser un extracteur de joint
    lèvre ou un tournevis à lame émoussée pour déloger délicatement le joint
    usé. Ne pas rayer la portée de l'arbre ni le logement dans le carter de
    boîte. - Préparer la portée : nettoyer soigneusement le logement du joint et
    inspecter l'arbre : une strie d'usure profonde sur l'arbre (trace de
    frottement du joint) impose l'utilisation d'un joint à lèvre décalée ou
    d'une bague de réparation. - Monter le nouveau joint : enduire légèrement la
    lèvre du nouveau joint d'huile de boîte propre. Positionner le joint dans
    son logement en veillant au sens de montage (la lèvre d'étanchéité doit être
    orientée vers l'intérieur de la boîte). Enfoncer le joint à l'aide d'une
    douille de montage de diamètre adapté — jamais avec un tournevis. - Reposer
    l'arbre de transmission : réintroduire l'arbre proprement, vérifier
    l'enclenchement correct de la circlip ou du dispositif de verrouillage.
    Contrôler le couple de serrage de la vis de fixation selon les
    préconisations constructeur. - Remplir l'huile de boîte : ajouter la
    quantité et le grade d'huile de boîte spécifiés par le constructeur.
    Revisser le bouchon de remplissage au couple. - Vérifier l'absence de fuite
    : démarrer le moteur, passer les vitesses, effectuer un essai roulant de 10
    à 15 minutes puis contrôler visuellement la zone du joint remplacé.
  S4_REPOSE: >-
    Après la repose du nouveau joint de boîte vitesse, une série de contrôles
    permet de valider l'étanchéité et le bon fonctionnement de la transmission
    avant de remettre le véhicule en circulation. - Vérifier le niveau d'huile
    de boîte après remplissage : avec le véhicule sur terrain plat et le moteur
    à l'arrêt, contrôler que le niveau d'huile atteint le bas du filetage du
    bouchon de niveau (méthode de trop-plein). Certaines boîtes modernes
    requièrent un contrôle de niveau à chaud, moteur tournant — consulter la
    procédure constructeur spécifique au modèle. - Contrôler visuellement le
    joint en place : avant de remonter l'arbre de transmission, vérifier que le
    joint est positionné perpendiculairement à l'axe de l'arbre, sans
    déformation ni pincement de la lèvre d'étanchéité. La lèvre doit reposer
    uniformément sur la portée de l'arbre sur tout son pourtour. - Effectuer un
    premier démarrage moteur à l'arrêt : démarrer le véhicule et passer
    successivement les rapports de boîte en restant immobile (sur pont ou
    chandelles). Observer la zone du joint pendant 2 à 3 minutes à la recherche
    de toute trace de suintement ou de fuite active. Un suintement superficiel
    résiduel d'huile de montage est acceptable ; une fuite active impose une
    dépose immédiate. - Tester les passages de vitesses : vérifier l'absence de
    craquements, de résistance anormale ou de vibrations lors des changements de
    rapport. Un bruit de frottement à la sélection peut indiquer une
    réintroduction incorrecte de l'arbre de transmission ou un arbre mal calé
    dans son logement. - Effectuer un essai roulant progressif : rouler 10 à 15
    minutes en variant les régimes (départ, montée en vitesse, décélération).
    Inclure des phases de marche arrière. Éviter les accélérations brutales lors
    des 50 premiers kilomètres pour permettre la mise en place thermique du
    joint. - Contrôle final à chaud : après l'essai roulant, inspecter à nouveau
    la zone du joint avec le moteur chaud. Un joint de boîte se dilate
    légèrement à chaud — c'est à chaud que les fuites réelles se révèlent.
    Vérifier également le sol de garage après stationnement d'une heure pour
    détecter toute goutte d'huile. - Vérifier le couple de serrage de l'arbre de
    transmission : si l'intervention a nécessité de déposer la vis de fixation
    de l'arbre, confirmer que le serrage au couple constructeur a été respecté
    (typiquement 40 à 80 Nm selon les boîtes). Une vis insuffisamment serrée
    peut entraîner une extraction de l'arbre lors des phases de traction.
  S5: >-
    Certaines erreurs lors du remplacement d'un joint de boîte vitesse
    conduisent à une fuite persistante ou à une nouvelle panne rapide. En voici
    les principales, avec leur conséquence directe : - Utiliser un joint aux
    cotes incorrectes : un joint légèrement trop petit ne garantit pas
    l'étanchéité ; un joint trop grand se déchire au montage. Conséquence :
    fuite immédiate ou dans les premières centaines de kilomètres. - Monter le
    joint sans lubrifier la lèvre : la lèvre sèche se déchire lors de la remise
    en rotation de l'arbre. Conséquence : le joint neuf est détruit dès le
    premier démarrage. - Ne pas inspecter la portée de l'arbre : une gorge
    d'usure sur l'arbre empêche le nouveau joint de faire une étanchéité
    correcte. Conséquence : fuite persistante malgré le remplacement du joint. -
    Enfoncer le joint avec un tournevis ou un burin : le joint s'incline et
    n'est pas positionné perpendiculairement à l'arbre. Conséquence : étanchéité
    asymétrique, fuite rapide sur un côté. - Oublier de refaire le niveau
    d'huile de boîte après intervention : la vidange partielle effectuée pour la
    dépose de l'arbre entraîne une perte de volume. Conséquence : boîte en sous-
    remplissage, usure accélérée des pièces internes.
  S6: >-
    Après le montage d'un joint de boîte vitesse neuf, plusieurs contrôles
    permettent de valider l'intervention avant de reprendre la route normalement
    : - Contrôle visuel immédiat du joint : avant de remettre la roue, vérifier
    que le joint est bien positionné à fleur du carter, sans inclinaison ni
    déformation visible sur le pourtour. - Vérification du niveau d'huile de
    boîte : contrôler et ajuster le niveau selon les préconisations constructeur
    (mesure au bouchon de jauge ou par le bouchon de remplissage selon le type
    de boîte). - Essai moteur au ralenti : démarrer le véhicule et laisser
    tourner 2 à 3 minutes en observant la zone du joint — aucune trace d'huile
    ne doit apparaître. - Test de passage des vitesses : passer tous les
    rapports disponibles pour vérifier le fonctionnement correct de la boîte et
    l'absence de bruit anormal lié à la dépose-repose de l'arbre. - Essai
    roulant de 15 à 20 km : effectuer un parcours incluant accélérations et
    décélérations franches. À l'issue, laisser le véhicule stationner 10 minutes
    puis inspecter le sol sous la boîte. - Contrôle définitif du niveau d'huile
    à froid : après l'essai roulant et refroidissement complet, vérifier une
    dernière fois le niveau d'huile de boîte pour s'assurer de l'absence de
    perte.
  S7: >-
    Le remplacement d'un joint de boîte vitesse s'accompagne souvent de la
    vérification ou du remplacement simultané de plusieurs composants de la
    transmission. Anticiper ces besoins lors de la commande réduit les allers-
    retours en atelier. - Boîte de vitesses — Si le joint est défaillant depuis
    longtemps et que le niveau d'huile a été très bas pendant une période
    prolongée, vérifier l'état général de la boîte (bruits de synchroniseurs,
    difficulté de passage des rapports) avant de conclure à un simple
    remplacement de joint. - Joint d'étanchéité (set complet) — Il est courant
    de remplacer l'ensemble des joints d'étanchéité accessibles lors de
    l'ouverture de la transmission : joint de sélecteur, joint d'arbre
    secondaire et joint de reniflard si applicable. Le coût en pièces est faible
    comparé au temps de main-d'œuvre économisé. - Huile de boîte de vitesses —
    Lors d'une dépose de joint, la boîte est partiellement ou totalement
    vidangée. C'est l'occasion idéale de renouveler l'huile de boîte avec la
    référence exacte préconisée par le constructeur (MTF, GL-4, GL-5 ou huile
    spécifique DSG/CVT selon le type de boîte). - Soufflet de joint
    homocinétique — Si l'arbre de transmission a été déposé pour accéder au
    joint de boîte, vérifier l'état du soufflet de joint homocinétique. Un
    soufflet fissuré projette la graisse et expose le joint homocinétique à la
    corrosion et à l'usure prématurée. - Circlip de fixation d'arbre — La
    circlip de retenue de l'arbre dans la boîte se déforme légèrement à chaque
    dépose. Sur de nombreuses boîtes modernes, la dépose impose le remplacement
    de la circlip pour garantir un enclenchement fiable.
  S8: >-
    Quelle est la différence entre un joint de boîte vitesse et un joint
    homocinétique ? Le joint de boîte vitesse est un joint lèvre statique (ou
    quasi-statique) qui assure l'étanchéité entre le carter de boîte et un arbre
    tournant. Le joint homocinétique (ou soufflet de cardan) est une enveloppe
    flexible qui protège le cardan lui-même, en conservant la graisse à
    l'intérieur et en empêchant l'eau et la boue d'y pénétrer. Les deux assurent
    une forme d'étanchéité mais sur des pièces et avec des mécanismes
    différents. Peut-on continuer à rouler avec une fuite de joint de boîte
    vitesse ? Une fuite légère peut permettre de rouler quelques centaines de
    kilomètres, mais uniquement si le niveau d'huile de boîte est surveillé et
    maintenu. En cas de fuite importante, rouler sans appoint d'huile conduit à
    l'assèchement de la boîte et à une destruction rapide des engrenages, des
    roulements et des synchroniseurs — une réparation bien plus coûteuse qu'un
    simple joint. L'intervention doit être programmée sans délai. Comment
    choisir le bon joint de boîte vitesse pour mon véhicule ? Renseignez la
    marque, le modèle, la motorisation (code moteur) et l'année de mise en
    circulation de votre véhicule, puis vérifiez la référence constructeur.
    Identifiez la position exacte du joint à remplacer (arbre primaire,
    secondaire, sélecteur) car les cotes varient d'un emplacement à l'autre sur
    une même boîte. Comparez ensuite la référence OEM avec les alternatives
    aftermarket disponibles. Faut-il obligatoirement changer l'huile de boîte en
    même temps que le joint ? La dépose partielle de l'arbre impose généralement
    une vidange partielle de la boîte. C'est l'occasion idéale de vérifier
    l'état de l'huile de boîte : une huile de couleur noire, à l'odeur de brûlé
    ou chargée en particules métalliques doit être remplacée. Si l'huile est
    encore conforme, un simple appoint au niveau correct suffit après le
    remplacement du joint. Le remplacement d'un joint de boîte vitesse est-il
    accessible à un mécanicien amateur ? L'opération demande un outillage de
    base (pont ou chandelles, bac de récupération, douille de montage) et une
    connaissance du montage des joints lèvre. Elle reste accessible à un
    bricoleur méthodique sur des véhicules courants. En revanche, sur les
    transmissions intégrales, les boîtes double embrayage ou lorsque la portée
    de l'arbre est usée, l'intervention est mieux confiée à un atelier
    spécialisé.
  META: >-
    {"meta_title":"Joint de boîte de vitesses : fuites et
    remplacement","meta_description":"Fuite d'huile sous la voiture, traces sur
    le sol ou niveau insuffisant ? Apprenez à localiser un joint de boîte de
    vitesses défaillant et à le remplacer au bon moment."}
---

# Joint de boîte vitesse - Guide Diagnostic Complet

## Fonction et Rôle

Assurer l'etancheite de la boite de vitesses contre les fuites d'huile

**Actions principales:** assurer l'etancheite, proteger

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- fuite d huile au niveau de la boite
- traces d huile sur le sol de garage
- niveau d huile de boite insuffisant

## Procédure de Diagnostic

Pour diagnostiquer un problème de joint de boîte vitesse:

1. **Inspection visuelle** - Examiner l'état du joint de boîte vitesse
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- boite-de-vitesses
- joint-d-etancheite

## Critères de Compatibilité

Pour commander le bon joint de boîte vitesse, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"

## FAQ

**Comment choisir Joint de boîte vitesse compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Joint de boîte vitesse ?**
En cas de fuite d huile au niveau de la boite ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Joint de boîte vitesse sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
