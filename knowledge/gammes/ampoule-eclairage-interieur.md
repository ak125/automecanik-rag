---
category: eclairage
slug: ampoule-eclairage-interieur
title: Ampoule éclairage intérieur
pg_id: 117
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
  role: Produit la lumière pour éclairer l'intérieur de l'habitacle
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
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de compatibilite
    pour confirmer Ampoule éclairage intérieur.
  - Verifier le type d ampoule (H1, H4, H7, LED, xenon) compatible avec le vehicule
  - Respecter la puissance et le culot exact de l ampoule d origine
  - Choisir des ampoules homologuees pour la circulation routiere
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
  - tier: Équivalent OE / marque reconnue
  - tier: Ampoule LED compatible
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
    label: Plafonnier qui ne s allume plus
    severity: confort
  - id: S2
    label: Lumiere qui clignote ou vacille
    severity: confort
  - id: S3
    label: Eclairage tres faible
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'Usure ou defaillance causant : plafonnier qui ne s allume plus'
  - 'Usure ou defaillance causant : lumiere qui clignote ou vacille'
  quick_checks:
  - 'Observer : plafonnier qui ne s allume plus ?'
  - 'Observer : lumiere qui clignote ou vacille ?'
  - 'Observer : eclairage tres faible ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Plafonnier qui ne s allume plus
  - Lumiere qui clignote ou vacille
  - Eclairage tres faible
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '117'
  intro_title: A quoi sert Ampoule éclairage intérieur ?
  risk_title: Pourquoi remplacer Ampoule éclairage intérieur a temps ?
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
  - question: Comment choisir Ampoule éclairage intérieur compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Ampoule éclairage intérieur ?
    answer: En cas de plafonnier qui ne s allume plus ou de degradation mesurable, il faut controler rapidement avant panne
      secondaire.
  - question: Puis-je monter Ampoule éclairage intérieur sans verification atelier ?
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
doc_id: 6fba7b71-c942-51ba-bc1d-fc87c81670fc
content_hash: sha256:bbbecf9b044854bc
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
  - type: 'composite'
    source_ref: corpus RAG web OEM
  - type: 'hall'
    source_ref: corpus RAG web OEM
  - type: 'organique'
    source_ref: corpus RAG web OEM
  - type: 'plein'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_000__v: '000, v'
    val_1_5_a: '1,5 A'
    val_10__: '10 %'
    val_10_mm: '10 mm'
    val_100__: '100 %'
    val_13_6__: '13,6 %'
    val_1304_5469_v: '1304.5469 v'
    val_2__a: '2, a'
    val_20__: '20 %'
    val_200_a: '200 A'
    val_25_a: '25 a'
    val_28_a: '28 a'
    val_300__m: '300 µm'
    val_40_nm: '40 nm'
    val_400_nm: '400 nm'
  materials:
  - materiau: 'aluminium'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: L'ampoule d'éclairage intérieur est le composant lumineux qui produit la lumière nécessaire pour éclairer l'habitacle
    du véhicule. Elle équipe les plafonniers, les éclairages de coffre, de boîte à gants, de seuils de portes et de miroirs
    de courtoisie. Sa fonction est d'émettre un flux lumineux suffisant pour permettre aux occupants de se repérer, de lire
    ou d'identifier des objets dans l'habitacle, notamment en conditions de faible luminosité ambiante.Techniquement, les
    ampoules d'éclairage intérieur se déclinent en plusieurs technologies selon l'âge et la gamme du véhicule. Les modèles
    anciens utilisent des ampoules à incandescence classiques (filament de tungstène, culots festoon ou W5W), consommatrices
    d'énergie et sensibles aux vibrations. Les véhicules plus récents sont équipés de diodes électroluminescentes (LED) intégrées
    dans des modules spécifiques, offrant une durée de vie nettement supérieure et une consommation réduite. Entre ces deux
    technologies, les ampoules halogènes et les lampes T10 constituent une solution intermédiaire.L'ampoule est activée par
    un interrupteur mécanique placé dans le joint de porte ou par un interrupteur manuel sur le plafonnier. Certains véhicules
    disposent d'une gestion électronique des éclairages intérieurs avec extinction progressive (gradual extinction) pour le
    confort à bord. La tension nominale est de 12 V (ou 24 V sur poids lourds), avec des puissances variant de 3 W à 21 W
    selon la fonction.Les pièces associées à vérifier lors d'une intervention sont le plafonnier complet et l'interrupteur
    d'éclairage de porte, qui peuvent causer les mêmes symptômes qu'une ampoule défaillante.
  S2: 'La défaillance d''une ampoule d''éclairage intérieur est généralement immédiate (claquage du filament) plutôt que progressive.
    Cependant, des symptômes intermédiaires peuvent précéder la panne complète, notamment sur les ampoules en fin de vie ou
    sur des installations avec des problèmes de contact ou d''alimentation. Voici les signes à surveiller :- Plafonnier qui
    ne s''allume plus : c''est le symptôme le plus évident. Le plafonnier reste éteint lors de l''ouverture d''une porte ou
    lorsqu''on appuie sur le bouton d''éclairage manuel. Avant de conclure à une ampoule grillée, vérifiez le fusible correspondant
    dans le boîtier de fusibles (généralement libellé "plafonnier" ou "interior lights").- Lumière qui clignote ou vacille
    : une ampoule dont le filament est partiellement rompu ou dont le contact est intermittent produit un éclairage instable.
    Ce vacillement peut aussi indiquer un contact oxydé dans le porte-ampoule ou une connexion électrique desserrée sur l''interrupteur
    de porte.- Éclairage très faible : l''ampoule s''allume mais produit une lumière nettement insuffisante, sans rapport
    avec sa puissance nominale. Ce symptôme caractérise souvent une ampoule en fin de vie dont le filament s''est aminci,
    ou une connexion électrique dégradée qui limite l''intensité.- Éclairage intérieur qui reste allumé en permanence : si
    le plafonnier reste allumé portières fermées, la cause est généralement un interrupteur de porte défaillant ou collé,
    et non l''ampoule elle-même. Ce défaut peut vider la batterie en quelques heures.- Ampoule qui noircit à l''intérieur
    : le dépôt de tungstène sur la paroi interne de l''ampoule à incandescence indique un filament qui s''est volatilisé —
    l''ampoule est en fin de vie et doit être remplacée avant claquage complet.'
  S3: 'Choisir une ampoule d''éclairage intérieur paraît simple, mais une erreur de culot, de dimensions ou de technologie
    rend la pièce inutilisable. La multiplication des formats (festoon, T10, T4W, navette, LED plug-and-play) impose de vérifier
    plusieurs paramètres avant la commande. Voici les critères à respecter :- Marque, modèle et année du véhicule : les catalogues
    de pièces détachées sont indexés sur cette combinaison. Un même modèle de véhicule peut utiliser des formats d''ampoule
    différents selon l''année de production ou la finition (exemple : plafonnier simple vs plafonnier avec lecture individuelle).-
    Type de culot et dimensions de l''ampoule : mesurez la longueur de l''ampoule en place si vous devez la remplacer à l''identique
    (les festoon existent en 28 mm, 36 mm, 41 mm, 44 mm). Un culot inadapté n''entre pas dans le porte-lampe ou ne fait pas
    contact électrique.- Tension et puissance : les ampoules intérieures automobiles sont en 12 V. La puissance (3 W, 5 W,
    10 W, 21 W) doit correspondre à celle d''origine pour ne pas surcharger le circuit ou sous-éclairer l''habitacle.- Technologie
    (incandescence, halogène, LED) : si le véhicule d''origine est équipé d''ampoules à incandescence, un remplacement par
    des LED plug-and-play est généralement possible à condition de vérifier la compatibilité du culot et l''absence de résistance
    ballast nécessaire. Les LED consomment moins et durent plus longtemps.- Teinte de lumière : pour l''éclairage intérieur,
    une teinte blanche chaude (3000 K à 4000 K) offre le meilleur confort visuel. Une teinte trop froide (6000 K) peut fatiguer
    les yeux lors d''une utilisation nocturne prolongée.- Conformité aux pièces associées : si le plafonnier intègre plusieurs
    sources lumineuses, remplacez toutes les ampoules défaillantes lors de la même intervention pour éviter un éclairage inégal.Pour
    aller plus loin : consultez notre guide d''achat ampoule éclairage intérieur — comparatif marques, critères de choix et
    prix.'
  S4_DEPOSE: 'Le remplacement d''une ampoule d''éclairage intérieur est une opération accessible à un non-professionnel, mais
    qui demande de la délicatesse pour ne pas endommager les clips et les garnitures intérieures. Voici la procédure générale
    applicable à la grande majorité des véhicules :- Identifiez le plafonnier ou le logement à intervenir : localisez l''éclairage
    défaillant (plafonnier central, éclairage de lecture, coffre, boîte à gants). L''emplacement exact du porte-ampoule varie
    selon le type d''éclairage et le véhicule.- Coupez le contact et ouvrez les portes : pour travailler avec un éclairage
    d''ambiance allumé si besoin, gardez une porte ouverte. Le contact coupé évite tout court-circuit lors de la manipulation.-
    Démontez le diffuseur ou le cache du plafonnier : la plupart des plafonniers sont maintenus par des clips en plastique.
    Utilisez un outil de décoffrage (ou un tournevis à lame plate enveloppé d''un chiffon pour protéger la garniture) et glissez-le
    dans la jointure pour faire levier doucement. N''utilisez jamais une lame métallique nue qui rayerait la garniture.- Accédez
    au porte-ampoule : une fois le diffuseur retiré, le porte-ampoule est visible. Il peut s''agir d''un support à ressort
    (pour les ampoules festoon) ou d''un support à baïonnette ou à friction (pour les ampoules T10).- Retirez l''ampoule défaillante
    : pour une ampoule festoon, pincez les deux extrémités et sortez-la des contacts en la faisant légèrement pivoter. Pour
    une ampoule à baïonnette, appuyez, tournez d''un quart de tour dans le sens antihoraire et tirez. Pour une T10, tirez
    simplement en ligne droite.- Installez la nouvelle ampoule : ne touchez pas la partie en verre à mains nues pour les ampoules
    halogènes (les traces de doigts créent des points chauds qui réduisent la durée de vie). Utilisez un chiffon propre ou
    les gants fournis. Insérez la nouvelle ampoule dans le porte-lampe jusqu''au clic ou à la mise en contact ferme.- Testez
    l''éclairage avant de remonter le diffuseur : mettez le contact ou ouvrez la porte pour vérifier que l''ampoule s''allume
    correctement. Ce test évite de remonter le plafonnier pour découvrir ensuite qu''il faut recommencer.- Remontez le diffuseur
    : positionnez les clips en face de leurs logements et appuyez fermement jusqu''aux clics d''enclenchement. Vérifiez que
    le diffuseur est aligné avec la garniture et qu''il n''y a pas de jeu visible.'
  S4_REPOSE: 'La repose d''une ampoule d''éclairage intérieur demande autant de précaution que la dépose, notamment pour ne
    pas abîmer les clips et les garnitures en plastique. La principale règle : ne jamais toucher le verre de l''ampoule halogène
    avec les doigts nus. Une trace de graisse sur le verre crée un point chaud qui provoque l''éclatement de l''ampoule en
    quelques heures de fonctionnement. - Vérifier la compatibilité de la nouvelle ampoule : avant de procéder au remontage,
    comparez la nouvelle ampoule avec l''ancienne : même type (festoon, W5W, T10, BA9s selon le logement), même longueur pour
    les navettes, même puissance (5W ou 10W selon le plafonnier). Une ampoule de mauvais format ne peut pas s''engager dans
    le support et risque de le forcer. - Manipuler l''ampoule avec un chiffon propre ou des gants : saisissez la nouvelle
    ampoule par son culot métallique ou avec un chiffon sans peluche. Évitez tout contact du verre avec les doigts — l''acidité
    de la peau dépose une couche invisible qui génère un point de chauffe fatal pour l''ampoule halogène. - Engager l''ampoule
    dans le support : selon le type de support, l''ampoule s''insère par pression (W5W, T10), par rotation d''un quart de
    tour (type baïonnette) ou par pincement des ergots latéraux (navette festoon). Sentez le déclic ou l''arrêt de course
    — l''ampoule est en place lorsqu''elle ne bouge plus sous une légère traction. - Repositionner le diffuseur ou le cache
    transparent : inclinez le diffuseur en commençant par le côté opposé aux clips de sécurité, puis appuyez jusqu''au clipsage.
    Sur les plafonniers équipés de vis, revissez sans forcer — le plastique est fragile et une vis trop serrée fend le logement.
    Vérifiez que le diffuseur est plan et symétrique. - Contrôler le fonctionnement avant de remonter les garnitures : avant
    de réassembler les éléments de garniture intérieure (panneau de pavillon, cache coffre, etc.), ouvrez la porte concernée
    pour déclencher l''allumage automatique ou actionnez l''interrupteur manuel. L''ampoule doit s''allumer sans scintillement
    ni retard. Un défaut à ce stade est plus facile à corriger avant remontage complet. - Repositionner les garnitures et
    clips : remettez en place les éléments déposés lors de l''accès au porte-ampoule. Pour les clips en plastique, alignez-les
    dans leur logement et exercez une pression franche et uniforme jusqu''au clipsage — une pression en biais fend la patte
    de fixation. Si un clip est cassé, remplacez-le (clips universels disponibles en accessoires auto). - Test final toutes
    portes : ouvrez et fermez chaque porte successivement pour vérifier que l''éclairage s''allume et s''éteint correctement.
    Sur les véhicules avec gestion électronique des éclairages, le calculateur peut mettre quelques secondes à reconnaître
    le changement d''ampoule — c''est normal si aucun voyant d''anomalie ne s''allume au tableau de bord.'
  S5: 'Le remplacement d''une ampoule d''éclairage intérieur semble anodin, mais plusieurs erreurs peuvent compliquer l''opération
    ou entraîner une panne récurrente. Voici les cinq erreurs les plus fréquemment commises :- Forcer sur le diffuseur sans
    outil adapté : tenter de retirer le cache du plafonnier à mains nues ou avec un outil trop large casse les clips en plastique.
    Des clips cassés rendent le diffuseur instable et créent un bruit de vibration en roulant. Utilisez systématiquement un
    outil de décoffrage plastique ou un tournevis protégé par un chiffon.- Ne pas vérifier le fusible avant de remplacer l''ampoule
    : si l''éclairage intérieur est totalement absent sur plusieurs zones simultanément, la cause est probablement un fusible
    grillé et non les ampoules elles-mêmes. Vérifiez le fusible correspondant dans la boîte à fusibles avant d''acheter des
    ampoules.- Toucher le verre d''une ampoule halogène à mains nues : les traces de doigts sur le verre d''une ampoule halogène
    créent des points de surchauffe qui provoquent une rupture prématurée du filament en quelques heures à quelques jours.
    Manipulez toujours les ampoules halogènes avec un chiffon propre ou des gants.- Monter une ampoule de puissance supérieure
    : une ampoule plus puissante que la spécification d''origine peut surchauffer le porte-ampoule en plastique et les câbles
    environnants, voire provoquer un incendie dans le cas extrême. Respectez la puissance d''origine indiquée dans le manuel
    du véhicule.- Ignorer un interrupteur de porte défaillant : si l''ampoule neuve grille à nouveau rapidement ou si l''éclairage
    reste allumé portes fermées, l''interrupteur de porte (souvent un poussoir dans le montant de porte) est collé ou grippé
    en position active. Ne pas traiter ce défaut vide la batterie et réduit la durée de vie des ampoules.'
  S6: 'Après avoir remplacé une ampoule d''éclairage intérieur, les vérifications suivantes permettent de confirmer que l''intervention
    est complète et que l''installation électrique est en bon ordre :- Test d''allumage avec la porte ouverte et avec l''interrupteur
    manuel : vérifiez les deux modes d''activation (automatique par contact de porte et manuel par le bouton du plafonnier)
    pour confirmer que les deux fonctionnent indépendamment.- Contrôle de l''extinction automatique portières fermées : fermez
    toutes les portières et vérifiez que l''éclairage s''éteint correctement. Un éclairage qui reste allumé indique un interrupteur
    de porte défaillant à corriger immédiatement pour préserver la batterie.- Inspection visuelle du diffuseur remonté : vérifiez
    que le cache du plafonnier est correctement encastré, sans jeu ni bord soulevé. Un mauvais enclenchement des clips provoque
    des bruits de vibration sur route.- Vérification de l''uniformité de l''éclairage : si plusieurs ampoules équipent le
    même plafonnier, comparez l''intensité lumineuse de chaque source. Une ampoule nettement moins lumineuse que les autres
    indique une connexion insuffisante dans son porte-ampoule.- Test de durée d''extinction différée : sur les véhicules équipés
    d''une extinction progressive (fade-out), vérifiez que l''éclairage diminue progressivement lors de la fermeture de la
    porte et ne s''éteint pas brusquement, signe que l''alimentation et la gestion électronique fonctionnent normalement.'
  S7: 'Le remplacement d''une ampoule d''éclairage intérieur est l''occasion de contrôler les composants qui conditionnent
    son fonctionnement. Une ampoule qui grille rapidement ou à répétition signale souvent un problème en amont — sur le plafonnier,
    l''interrupteur ou le circuit électrique. - Plafonnier (bloc éclairage) : le plafonnier est l''ensemble qui accueille
    l''ampoule, son support et les interrupteurs de déclenchement. Si le support est fendu, oxydé ou si les contacts sont
    noircis, la nouvelle ampoule souffrira de mauvais contact et grillera prématurément. Contrôlez l''état des contacts cuivrés
    dans le logement : ils doivent être brillants et souples. - Interrupteur d''éclairage de porte : l''allumage du plafonnier
    lors de l''ouverture d''une porte est commandé par un contacteur situé sur le montant de la porte (petit bouton-poussoir
    que la porte comprime quand elle est fermée). Si un seul plafonnier ne s''allume pas malgré une ampoule neuve, vérifiez
    le contacteur de la porte correspondante : il peut être collé en position fermée. - Fusible de circuit éclairage intérieur
    : chaque circuit d''éclairage intérieur est protégé par un fusible dédié. Si tous les éclairages d''un même groupe sont
    HS simultanément, vérifiez le fusible correspondant dans le boîtier fusibles habitacle avant de suspecter les ampoules.
    Un fusible grillé à répétition indique un court-circuit dans le circuit. - Éclairage de coffre : l''ampoule d''éclairage
    du coffre fonctionne souvent sur le même circuit que les plafonniers. Si vous remplacez une ampoule plafonnier, vérifiez
    simultanément le fonctionnement de l''éclairage coffre. Le contacteur de coffre (sur le loquet ou le bord de l''ouverture)
    peut également être encrassé ou défaillant. - Éclairages de lecture et de courtoisie : les véhicules modernes disposent
    de plusieurs points d''éclairage intérieur (lecture avant, lecture arrière, pieds de portière, vide-poches). Ces ampoules
    vieillissent à des rythmes différents selon leur usage. Profitez de l''accès au circuit pour vérifier l''ensemble des
    ampoules intérieures et remplacer toutes celles qui sont fatiguées. - Câblage et connecteurs : sur les véhicules anciens,
    les fils alimentant les plafonniers peuvent se fragiliser au niveau des charnières de porte (câbles sollicités mécaniquement
    à chaque ouverture). En cas d''éclairage intermittent persistant après changement d''ampoule, inspectez le faisceau à
    hauteur des charnières et recherchez un fil rompu ou dénudé.'
  S8: 'Pourquoi mon plafonnier ne s''allume plus alors que l''ampoule semble intacte ?Plusieurs causes sont possibles en dehors
    de l''ampoule elle-même : un fusible grillé (consultez la liste des fusibles dans le manuel du véhicule et cherchez "plafonnier"
    ou "interior lights"), un interrupteur de porte oxydé ou collé qui ne ferme plus le circuit électrique, ou une connexion
    desserrée dans le porte-ampoule. Commencez par vérifier le fusible avec un testeur de continuité avant de démonter quoi
    que ce soit.Peut-on remplacer les ampoules d''origine par des LED dans l''habitacle ?Oui, dans la grande majorité des
    cas, des ampoules LED plug-and-play au même culot que les ampoules d''origine peuvent être installées sans modification.
    Les LED consomment 3 à 5 fois moins et durent 10 fois plus longtemps. Vérifiez que le culot correspond (festoon 36 mm,
    T10, etc.) et que la LED est disponible en 12 V. Certains véhicules récents avec gestion électronique des éclairages peuvent
    détecter la faible consommation des LED comme un défaut — dans ce cas, un kit avec résistance d''équilibrage est nécessaire.L''ampoule
    du coffre est difficile à atteindre — comment procéder ?L''ampoule du coffre est souvent intégrée dans le plafonnier de
    coffre, accessible depuis l''intérieur en retirant le cache en plastique par simple pression sur des clips. Dans certains
    cas, la garniture latérale du coffre doit être partiellement décollée. Consultez un forum dédié à votre modèle de véhicule
    pour identifier la procédure exacte — les démontages de garniture diffèrent fortement d''un véhicule à l''autre et un
    guide illustré évite de casser des clips fragiles.Combien de temps dure une ampoule d''éclairage intérieur ?Une ampoule
    à incandescence classique dure en moyenne 1 000 à 2 000 heures de fonctionnement, soit plusieurs années pour un usage
    normal (quelques minutes par jour). Une ampoule halogène atteint 2 000 à 3 000 heures. Une LED dure 30 000 à 50 000 heures,
    soit une durée de vie équivalente à celle du véhicule dans la plupart des cas. La durée réelle dépend de la qualité de
    la pièce et des conditions d''utilisation (température, vibrations).'
  META: Plafonnier éteint, lumière vacillante ou éclairage trop faible ? Trouvez la bonne ampoule d'éclairage intérieur selon
    la référence de votre véhicule.
---

# Ampoule éclairage intérieur - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière pour éclairer l'intérieur de l'habitacle

**Actions principales:** produire, emettre, eclairer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- plafonnier qui ne s allume plus
- lumiere qui clignote ou vacille
- eclairage tres faible

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule éclairage intérieur:

1. **Inspection visuelle** - Examiner l'état du ampoule éclairage intérieur
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

- plafonnier
- interrupteur-eclairage

## Critères de Compatibilité

Pour commander le bon ampoule éclairage intérieur, vous devez connaître:

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

**Comment choisir Ampoule éclairage intérieur compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Ampoule éclairage intérieur ?**
En cas de plafonnier qui ne s allume plus ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Ampoule éclairage intérieur sans verification atelier ?**
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
