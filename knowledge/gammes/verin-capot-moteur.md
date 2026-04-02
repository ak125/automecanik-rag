---
category: accessoires
slug: verin-capot-moteur
title: Vérin capot moteur
pg_id: 514
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
  role: Maintient le capot moteur en position ouverte
  must_be_true:
  - maintenir
  - supporter
  - soulever
  must_not_contain:
  - moteur
  - refroidissement
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - verin-de-coffre
  - poignee-de-porte
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de compatibilite
    pour confirmer Vérin capot moteur.
  - Verifier la reference OE ou equivalence constructeur pour le vehicule exact
  - Comparer les dimensions et le type de montage avec la piece d origine
  - Choisir un equipementier reconnu pour garantir qualite et compatibilite
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "securite garantie"
  cost_range:
    min: 50
    max: 300
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  brands:
    premium:
    - Stabilus
    - Magneti Marelli
    - Valeo
    standard:
    - Lesjöfors
    - Triscan
    - Maxgear
    - Febi Bilstein
    budget:
    - Mapco
    - Metzger
    - Polcar
  quality_tiers:
  - tier: Origine (OE/OES)
    description: Vérins fabriqués par les équipementiers d'origine. Force de poussée, longueur et fixations identiques à la
      pièce montée en usine.
  - tier: Équivalent OE
    description: Fabricants aftermarket spécialisés en vérins à gaz. Conformes aux spécifications constructeur, bon rapport
      qualité/prix.
  - tier: Adaptable
    description: Vérins économiques. Vérifier impérativement la force (en Newton), la longueur dépliée et le type de rotule/embout
      avant commande.
diagnostic:
  symptoms:
  - id: S1
    label: Capot qui retombe lentement
    severity: confort
  - id: S2
    label: Capot qui ne reste plus ouvert
    severity: confort
  - id: S3
    label: Verin qui fuit traces de graisse
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'Usure ou defaillance causant : capot qui retombe lentement'
  - 'Usure ou defaillance causant : capot qui ne reste plus ouvert'
  quick_checks:
  - 'Observer : capot qui retombe lentement ?'
  - 'Observer : capot qui ne reste plus ouvert ?'
  - 'Observer : verin qui fuit traces de graisse ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Capot qui retombe lentement
  - Capot qui ne reste plus ouvert
  - Verin qui fuit traces de graisse
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '514'
  intro_title: A quoi sert Vérin capot moteur ?
  risk_title: Pourquoi remplacer Vérin capot moteur a temps ?
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
  - question: Comment choisir Vérin capot moteur compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Vérin capot moteur ?
    answer: En cas de capot qui retombe lentement ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Vérin capot moteur sans verification atelier ?
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
doc_id: e30048f8-a94c-5a4c-bff7-ba330cc24125
content_hash: sha256:86911cef48e55c2d
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
  area: Sur la carrosserie (capot, coffre, portes)
  access: Accessible directement sans outil special
  adjacent_parts:
  - charniere
  - serrure
  - cable
  - joint
installation:
  difficulty: facile
  time: 10 a 30 min
  tools:
  - tournevis
  - cle plate
  - clip de fixation
  prerequisite: Aucun prerequis special
phase5_enrichment:
  _source: contenu LLM — a revalider contre sources OEM
  _validation_status: pending_oem_validation
  _enriched_at: '2026-03-30'
  technical_notes:
    force_N: 'verifier la force en Newtons avant commande — trop faible = capot ne tient pas'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le vérin capot moteur est un amortisseur à gaz comprimé chargé de maintenir
    le capot en position haute lors de chaque ouverture. Monté par paire sur la
    plupart des véhicules, il convertit la pression interne du gaz — typiquement
    entre 6 et 12 bar selon le fabricant — en une force de poussée qui compense
    le poids du capot et le maintient stable sans effort de la part du
    conducteur. Son principe de fonctionnement repose sur un corps cylindrique
    rempli de gaz azote et d'huile, dans lequel un piston coulissant se déplace
    avec friction contrôlée. À l'ouverture, le gaz en expansion pousse la tige
    et soulève le capot. À la fermeture, la compression progressive du gaz
    ralentit le mouvement et absorbe les chocs. Les points d'ancrage — rotules
    ou embouts à billes — transmettent les efforts entre le carrosserie, la
    charnière et le capot. La durée de vie dépend directement de la fréquence
    d'utilisation, des écarts de température (gel hivernal, chaleur moteur) et
    de la qualité des joints d'étanchéité. Un vérin qui perd de sa pression au
    fil du temps ne maintient plus le capot en hauteur suffisante, exposant
    l'intervenant à un risque de blessure au niveau de la tête ou des bras si le
    capot descend inopinément.
  S2: >-
    Un vérin capot moteur défaillant se détecte rapidement à l'usage.
    Contrairement à d'autres pièces dont l'usure est graduelle et silencieuse,
    la perte de pression d'un vérin se manifeste par des signes comportementaux
    clairs dès les premières ouvertures de capot. Identifier ces symptômes tôt
    permet d'éviter une chute du capot lors d'une intervention moteur. - Le
    capot retombe lentement au lieu de rester en position haute : le vérin n'a
    plus la force de poussée suffisante pour compenser le poids du panneau —
    premier signe d'une perte de gaz progressive. - Le capot ne se maintient
    plus ouvert sans support manuel : à un stade avancé, le vérin ne développe
    plus aucune résistance et le capot redescend dès qu'on le lâche, même
    légèrement. - Traces de graisse ou d'huile le long de la tige : une fuite au
    niveau du joint torique se trahit par un film graisseux sur la tige chromée
    — signe que la pression interne chute irrémédiablement. - Résistance
    irrégulière à l'ouverture : le capot monte par à-coups ou nécessite un
    effort accru en début de course — signe d'un joint ou d'un piston usé à
    l'intérieur du corps du vérin. - Bruit de claquement à la fermeture : un
    vérin qui ne freine plus correctement en fin de course laisse le capot
    claquer sur ses butées — les joints absorbeurs internes sont hors service. -
    Corrosion visible sur le corps ou la tige : la rouille fragilise le corps
    métallique et attaque les joints, accélérant la perte de pression. Visible à
    travers le passage de roue ou sous capot.
  S3: >-
    Le vérin capot moteur est une pièce d'accès direct : la référence
    constructeur doit correspondre exactement au modèle du véhicule. Un vérin de
    longueur ou de force de poussée incorrecte ne maintiendra pas le capot dans
    la bonne position angulaire, rendant l'ouverture dangereuse. Voici les
    critères à vérifier avant de commander. - Marque, modèle et année de mise en
    circulation : le premier filtre. Des versions différentes d'un même modèle
    (restylage, phase 2) peuvent avoir des points d'ancrage distincts. -
    Longueur à vide et longueur déployée : les deux cotes déterminantes. La
    longueur repliée conditionne l'encombrement, la longueur déployée fixe
    l'angle d'ouverture du capot. - Force de poussée en Newton : trop faible, le
    capot ne se maintient pas ; trop élevée, il ouvre violemment et force les
    charnières. Respecter la valeur d'origine. - Type d'embouts de fixation :
    rotule, embout à billes ou clip plastique — le système d'attache doit
    correspondre aux ergots présents sur la carrosserie et sur le capot. -
    Remplacement par paire : même si un seul vérin est défaillant, remplacer les
    deux garantit un effort équilibré et évite un déséquilibre de soutien
    latéral. - Indice de qualité du gaz de remplissage : préférer un vérin
    rechargé à l'azote pur (non hygroscopique) pour une durée de vie maximale,
    surtout en environnement humide ou salin. - Compatibilité validée par
    référence croisée : comparer la référence OEM d'origine avec la référence du
    fournisseur tiers avant achat pour éviter tout risque de retour. Pour aller
    plus loin : consultez notre guide d'achat vérin capot moteur — comparatif
    marques, critères de choix et prix.
  S4_DEPOSE: >-
    Le remplacement d'un vérin capot moteur ne nécessite pas d'outillage
    spécialisé, mais impose de sécuriser le capot avant toute manipulation. Il
    faut impérativement caler le capot avec un support rigide (manche à balai,
    cale bois) avant de déposer l'ancien vérin, au risque de recevoir le capot
    sur la tête ou les mains. - Sécuriser le capot en position haute : placer un
    support rigide sous le capot, à mi-hauteur, pour le maintenir ouvert pendant
    toute la durée de l'intervention. Ne jamais se fier à un vérin dégradé comme
    seul support. - Identifier les points de fixation : localiser les embouts
    inférieur (côté carrosserie) et supérieur (côté capot). Selon le véhicule,
    il s'agit de clips à dégager avec un tournevis plat ou de rotules à
    déclipser. - Déposer l'embout inférieur en premier : lever l'ergot de
    verrouillage ou insérer un tournevis plat dans la gorge de l'embout et faire
    levier pour déclipper. Tenir le vérin pour éviter qu'il tombe. - Déposer
    l'embout supérieur : même procédure sur l'attache côté capot. Le vérin est
    maintenant libre — le poser de côté sans le plier ni le percer. - Nettoyer
    les ergots de fixation : éliminer corrosion et saleté des deux points
    d'ancrage avec une brosse métallique et du dégrippant. Vérifier l'état des
    ergots — les remplacer s'ils sont déformés. - Clipser le nouveau vérin côté
    capot d'abord : positionner l'embout supérieur sur l'ergot capot et appuyer
    jusqu'au clic de verrouillage. - Clipser l'embout inférieur côté carrosserie
    : aligner et pousser fermement jusqu'au clic. Tirer légèrement pour vérifier
    la fixation. - Retirer le support de sécurité et tester : laisser le capot
    descendre doucement, puis rouvrir pour vérifier que le vérin maintient le
    capot en position haute sans assistance manuelle.
  S4_REPOSE: >-
    Une fois le vérin capot moteur neuf déposé de son emballage, la repose
    s'effectue en moins de dix minutes. Le capot doit rester calé pendant toute
    la durée de l'opération — ne retirer la cale de sécurité qu'après avoir
    vérifié que les deux vérins sont correctement fixés.- Inspecter les rotules
    et embouts du vérin neuf avant la pose : comparer les rotules du vérin neuf
    avec celles de l'ancien. Le diamètre de rotule et le type de clip (à
    ressort, à baïonnette, plastique ou métal) doivent correspondre aux points
    d'ancrage du véhicule. Un embout inadapté forcé à la main peut se déclipser
    en cours d'utilisation.- Clipser d'abord l'embout côté carrosserie (point
    fixe supérieur) : positionner l'embout supérieur du vérin sur le pivot de
    carrosserie en orientant correctement le corps du vérin. Appuyer fermement
    jusqu'au clic de verrouillage — vérifier en tirant légèrement sur le corps
    du vérin après clippage.- Comprimer le vérin pour atteindre le point
    d'ancrage inférieur : le vérin neuf est en pression maximale — il faut le
    comprimer manuellement pour aligner l'embout inférieur sur le pivot du
    capot. Cette compression demande un effort de 50 à 150 N selon la force de
    poussée de la référence ; utiliser les deux mains ou un outil de compression
    adapté.- Clipser l'embout côté capot (point inférieur) : placer l'embout
    inférieur sur le pivot du capot et appuyer jusqu'au clic. Tirer sur le vérin
    pour confirmer le verrouillage — le vérin ne doit pas se déclipser sous
    traction.- Répéter l'opération pour le second vérin : les vérins capot
    travaillent en binôme — remplacer impérativement les deux en même temps. Un
    seul vérin neuf face à un vérin fatigué crée un déséquilibre qui fausse le
    maintien du capot.- Retirer la cale de sécurité et tester le maintien : une
    fois les deux vérins fixés, enlever le support de calage et lâcher le capot
    en position haute. Il doit s'immobiliser sans dériver. Réaliser 5 cycles
    d'ouverture/fermeture complète pour vérifier la constance du maintien.-
    Contrôler l'alignement du capot après fermeture : refermer le capot
    délicatement et vérifier que les jeux de carrosserie de part et d'autre sont
    uniformes. Si le capot est décentré, contrôler que les deux vérins sont bien
    positionnés sur leurs pivots respectifs.
  S5: >-
    Le remplacement d'un vérin capot est une opération en apparence simple, mais
    plusieurs erreurs techniques peuvent compromettre la sécurité de
    l'intervention ou réduire la durée de vie de la pièce neuve. Ces erreurs
    sont récurrentes chez les non-initiés. - Travailler sans caler le capot :
    déposer l'ancien vérin sans avoir sécurisé le capot avec un support rigide
    expose l'intervenant à une chute brutale du capot. Conséquence : blessure
    grave à la tête, aux épaules ou aux mains. - Commander un vérin avec une
    force de poussée incorrecte : un vérin trop puissant ouvre violemment le
    capot et force les charnières ; trop faible, il ne maintient pas.
    Conséquence : détérioration des charnières ou capot instable persistant. -
    Remplacer un seul vérin sur deux : si un seul est changé, le déséquilibre de
    force entre les deux côtés provoque un maintien asymétrique et fatigue
    prématurément le vérin neuf. Conséquence : nouveau remplacement dans les 6 à
    12 mois. - Forcer les embouts sans vérifier leur orientation : un embout mal
    orienté (roule qui ne fait pas face à l'ergot) ne se verrouille pas
    correctement. Forcer provoque la casse de l'embout plastique. Conséquence :
    vérin non fixé, chute du capot. - Percer ou flamber le vieux vérin pour
    l'éliminer : le corps est sous pression de gaz. Percer ou exposer le vérin à
    une flamme peut provoquer une projection violente de gaz et d'huile.
    Conséquence : accident grave. Déposer les vieux vérins en déchetterie ou
    chez le distributeur.
  S6: >-
    Une fois les nouveaux vérins posés, quelques vérifications rapides
    permettent de confirmer que le montage est correct et que la sécurité de
    l'utilisateur est assurée lors des prochaines ouvertures de capot. - Test de
    maintien statique : ouvrir le capot complètement et lâcher — il doit se
    maintenir en position haute sans dériver vers le bas pendant au moins 30
    secondes. Sinon, vérifier la force de poussée de la référence commandée. -
    Contrôle des deux embouts de fixation : tirer fermement sur chaque extrémité
    du vérin pour s'assurer que les clips sont verrouillés. Un embout qui se
    décroche à la traction manuelle n'est pas correctement fixé. - Inspection
    des ergots de carrosserie et de capot : vérifier l'absence de déformation ou
    de fissure sur les points d'ancrage. Un ergot fissuré lâchera sous
    vibrations. - Test de fermeture progressive : refermer le capot lentement
    depuis la position haute — les vérins doivent offrir une résistance
    progressive sans à-coup jusqu'au verrouillage du loquet. - Contrôle visuel
    de la tige pour fuite : après 2 à 3 cycles d'ouverture/fermeture, vérifier
    qu'aucun film huileux n'apparaît sur la tige chromée des vérins neufs. -
    Vérification des pièces associées : profiter du capot ouvert pour inspecter
    l'état des charnières et du loquet de capot. Une charnière voilée compromet
    l'alignement même avec un vérin neuf.
  S7: >-
    Le vérin de capot moteur est un amortisseur à gaz qui maintient le capot en
    position ouverte sans appui manuel. Quand il se vide ou se corrodé, le capot
    retombe sans avertissement — risque de blessure lors d'une intervention
    moteur. Lors du remplacement, vérifier les éléments structurels et de
    maintien voisins. - Charnières de capot — le vérin s'appuie sur le capot via
    ses rotules d'accrochage, mais la charnière porte la charge principale. Des
    charnières grippées ou déformées génèrent un effort supplémentaire sur le
    vérin neuf et l'usent prématurément. Lubrifier les axes de charnières à la
    graisse lithium lors du remplacement du vérin. - Câble de déverrouillage du
    capot — si l'ouverture du capot était devenue difficile avant la défaillance
    du vérin, le câble de déverrouillage ou sa gaine peut être grippé. Un câble
    rigide fatigue les mécanismes d'ouverture et indique une intervention
    prochaine. Lubrifier ou remplacer le câble si la résistance est notable. -
    Serrure de capot — le mécanisme de verrouillage double sécurité (loquet
    principal + sécurité anti-ouverture accidentelle) doit fermer et ouvrir
    librement. Un loquet grippé ou désaxé force la charnière et le vérin lors
    des ouvertures répétées. - Joints de capot — les bourrelets de caoutchouc
    périmétriques qui assurent l'étanchéité du capot vieillissent et se
    détachent. Des joints décollés laissent entrer l'eau dans le compartiment
    moteur et accélèrent la corrosion des fixations du vérin. Coller ou
    remplacer les portions décollées lors de l'accès au capot.
  S8: >-
    Peut-on rouler avec un vérin capot moteur défaillant ? Oui, techniquement la
    voiture reste opérationnelle sur route. Mais dès que vous ouvrez le capot
    pour une vérification de niveaux ou une intervention, le risque de chute du
    capot est réel. Un capot qui descend brutalement peut blesser grièvement au
    niveau de la tête ou des bras. Bloquer le capot avec un cale provisoire est
    une mesure d'urgence acceptable, mais pas une solution à conserver dans la
    durée. Comment savoir si le vérin est à plat ou si le problème vient des
    charnières ? Ouvrir le capot et mesurer l'effort nécessaire pour le pousser
    vers le haut à mi-hauteur : si le capot est lourd mais se maintient une fois
    poussé à fond, les vérins manquent de pression. Si le capot part librement
    mais revient immédiatement, les charnières sont voilées ou les butées sont
    usées. Dans le doute, tester en retirant un vérin et en le comprimant à la
    main : un vérin sain résiste fortement à la compression. Faut-il toujours
    remplacer les deux vérins en même temps ? Oui, dans la grande majorité des
    cas. Les vérins d'un même véhicule ont le même kilométrage et subissent les
    mêmes contraintes thermiques. Si l'un cède, l'autre est en fin de vie.
    Remplacer un seul crée un déséquilibre de poussée entre les deux côtés du
    capot, ce qui fatigue anormalement le vérin neuf et déforme progressivement
    les points d'ancrage. Peut-on recharger en pression un vérin capot usé
    plutôt que de le remplacer ? Non, dans les conditions courantes. Les vérins
    de capot sont des pièces scellées non rechargeables en atelier standard.
    Certains spécialistes proposent la recharge sous pression, mais le coût est
    souvent supérieur au prix d'une paire de vérins neufs d'entrée de gamme. Le
    remplacement direct est la solution technique et économique retenue par
    l'ensemble de la profession.
  META: >-
    {"meta_title":"Vérin capot moteur : quand et comment changer |
    AutoMecanik","meta_description":"Capot qui retombe seul, qui ne reste plus
    ouvert ou vérin qui fuit ? Guide diagnostic et remplacement du vérin capot
    moteur selon votre véhicule.","og_title":"Vérin capot moteur défaillant :
    diagnostic et remplacement | AutoMecanik","og_description":"Capot retombe
    lentement, ne reste plus ouvert ou traces de graisse sur le vérin :
    identifiez la panne et remplacez selon votre
    modèle.","schema_type":"HowTo","canonical_hint":"/pieces/verin-capot-
    moteur"}
---

# Vérin capot moteur - Guide Diagnostic Complet

## Fonction et Rôle

Maintient le capot moteur en position ouverte

**Actions principales:** maintenir, supporter, soulever

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- capot qui retombe lentement
- capot qui ne reste plus ouvert
- verin qui fuit traces de graisse

## Procédure de Diagnostic

Pour diagnostiquer un problème de vérin capot moteur:

1. **Inspection visuelle** - Examiner l'état du vérin capot moteur
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

- capot
- charniere

## Critères de Compatibilité

Pour commander le bon vérin capot moteur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"

## FAQ

**Comment choisir Vérin capot moteur compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Vérin capot moteur ?**
En cas de capot qui retombe lentement ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Vérin capot moteur sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
