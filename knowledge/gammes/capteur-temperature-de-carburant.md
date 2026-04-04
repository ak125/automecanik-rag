---
schema_version: '5.0'
category: gestion-moteur
slug: capteur-temperature-de-carburant
title: Capteur température de carburant
pg_id: 3943
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-04-03'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:materialize-db-to-md
  last_enriched_at: '2026-04-03'
domain:
  role: Le capteur de temperature de carburant (type CTN) est fixe sur la rampe haute pression ou le circuit de retour au
    reservoir. Il permet au calculateur d''ajuster le debit de carburant injecte en fonction de la variation de viscosite
    du carburant.
  must_be_true: []
  must_not_contain: []
  related_parts: []
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: Hall
    source_ref: corpus RAG web OEM
  - type: inductif
    source_ref: corpus RAG web OEM
  - type: pneumatique
    source_ref: corpus RAG web OEM
  - type: électrique
    source_ref: corpus RAG web OEM
  technical_notes:
    val_0_v: 0 V
    val_0_1__: 0,1 %
    val_1_5__: 1,5 %
    val_14__: 14 %
    val_4_5__: 4,5 %
    val_400__c: 400 °C
    val_5_v: 5 V
  materials:
  - materiau: aluminium
    source_ref: corpus RAG web OEM
  - materiau: platine
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le capteur de température de carburant est du type CTN (Coefficient de Température Négatif) sa résistance diminue lorsque
    la température augmente. Il est fixé soit sur la rampe haute pression soit sur le circuit de retour au réservoir. Il permet
    au calculateur d''apporter des corrections sur le débit de carburant injecté (variation de viscosité du carburant). Rôle
    du calculateur d''injection en fonction de l''information reçue : ajuster le débit carburant et calculer la densité du
    carburant.'
  S2: 'Le capteur de température de carburant mesure la température du gazole ou de l''essence dans le circuit d''alimentation
    et transmet cette donnée au calculateur d''injection. Cette information permet d''adapter la quantité de carburant injectée
    : le carburant chaud est moins dense, donc moins énergétique au volume — le calculateur compense en augmentant légèrement
    la durée d''injection. Une mesure erronée entraîne un dosage inexact et des conséquences directes sur la combustion. Symptômes
    indiquant une défaillance du capteur - Démarrage difficile à froid : Le calculateur reçoit une valeur de température erronée
    et ne parvient pas à calculer correctement l''enrichissement du mélange nécessaire au démarrage. Le moteur peine à s''amorcer,
    surtout sous 0 °C, ou nécessite plusieurs tentatives. - Consommation de carburant anormalement élevée : Si le capteur
    envoie une valeur de température basse alors que le carburant est chaud (ou l''inverse), le calculateur sur-injecte ou
    sous-injecte. Une surconsommation inexpliquée de 10 à 20 % par rapport aux valeurs habituelles peut pointer ce capteur.
    - À-coups ou hésitations à l''accélération : Le moteur répond de manière irrégulière aux sollicitations de l''accélérateur,
    particulièrement lors des reprises. Ces à-coups sont liés à une composition du mélange air/carburant instable due à une
    valeur de température erronée. - Voyant moteur allumé avec code défaut capteur température carburant : La lecture des
    codes défaut à l''outil OBD2 révèle un code de type P0180 à P0184 (capteur température carburant — circuit, plage ou performance
    hors limite). Ce code confirme la piste sans pour autant exclure un problème de câblage ou de connecteur. - Émissions
    polluantes élevées à la mesure CO/HC : Un mélange trop riche (trop de carburant) ou trop pauvre provoque une augmentation
    des émissions. Si le véhicule est recalé au contrôle technique sur les émissions, le capteur de température de carburant
    figure parmi les suspects avec la sonde lambda et les injecteurs. Facteurs déclenchant le remplacement - Usure du capteur
    NTC (thermistance) : Le capteur fonctionne sur le principe d''une thermistance à coefficient de température négatif (NTC)
    : sa résistance diminue quand la température augmente. Avec le temps, la courbe de résistance dérive et la valeur envoyée
    au calculateur ne correspond plus à la température réelle. Ce phénomène s''amplifie sur les véhicules à fort kilométrage
    (au-delà de 150 000 km). - Corrosion et infiltration de carburant : Le capteur est en contact permanent avec le carburant.
    Une légère fuite au niveau du joint d''étanchéité du capteur (joint torique) peut permettre une infiltration d''impuretés
    ou d''eau, surtout sur les véhicules diesel équipés de filtres à carburant avec séparateur d''eau. Remplacer le joint
    d''étanchéité lors de chaque intervention. - Connecteur oxydé ou câblage endommagé : Avant de remplacer le capteur, effectuer
    un test de résistance entre les bornes du capteur à froid et à température moteur atteinte. Comparer les valeurs à la
    courbe NTC constructeur. Un câblage sectionné ou un connecteur corrodé peut simuler une panne capteur — ne pas commander
    de pièce avant ce diagnostic.'
  S3: 'Le capteur de température de carburant mesure en temps réel la chaleur du carburant dans le circuit d''injection. Cette
    donnée est utilisée par le calculateur moteur pour corriger le dosage d''injection car la densité et la viscosité du carburant
    varient avec la température : un diesel chaud est moins dense et contient moins d''énergie au litre qu''un diesel froid.
    Le choix d''un capteur inadapté génère des corrections d''injection erronées et peut déclencher des codes défauts persistants.
    - Technologie NTC obligatoire : les capteurs de température carburant sont des résistances NTC (coefficient de température
    négatif). La résistance diminue quand la température augmente. Les plages types sont 2 000 à 3 000 ohms à 20°C et 200
    à 300 ohms à 80°C. Vérifier que le nouveau capteur correspond aux valeurs de la documentation constructeur. - Position
    dans le circuit : distinguer le capteur sur la rampe d''injection haute pression (jusqu''à 2 500 bar), le capteur sur
    la pompe haute pression, et le capteur sur le retour basse pression (10 à 60 bar). Chaque position impose des spécifications
    de tenue en pression différentes. Un capteur basse pression ne peut jamais équiper un circuit haute pression. - Compatibilité
    moteur précise : moteur diesel common rail (HDi, TDCi, CDI, CRDI, dCi), diesel pompe-injecteur (PDI, TDI ancienne génération),
    ou essence injection directe haute pression (TSI, TFSI, GDI). Les plages de température mesurées et les valeurs de résistance
    NTC diffèrent entre ces architectures. - Type de raccordement : filetage M14x1.5 ou M12x1.5 le plus fréquent sur common
    rail. Certains circuits utilisent des raccords rapides (push-to-connect) qui ne peuvent pas être remplacés par des raccords
    filetés sans adaptateur homologué. Vérifier le pas de vis et le type de joint : joint torique ou joint conique. - Connecteur
    électrique : le nombre de broches (2 ou 3 fils), le type de connecteur (Bosch Compact, Delphi Metri-Pack, AMP Junior Timer)
    et le sens de verrouillage varient selon le constructeur. Un connecteur inadapté contraint le câblage et génère des intermittences.
    - Marques de référence : Bosch, Continental/VDO, Delphi et Denso pour les circuits common rail. Pour les véhicules sous
    garantie ou récents, privilégier la référence OEM du constructeur ou la référence équipementier OES correspondante.'
  S4_DEPOSE: 'Intervention sur circuit carburant haute pression. La dépressurisation complète est impérative avant toute ouverture
    du circuit : le carburant sous pression dans un common rail est inflammable et s''échappe à grande vitesse en cas d''ouverture
    intempestive. - Dépressuriser le circuit carburant : deux méthodes selon le véhicule. Méthode 1 — retirer le fusible de
    la pompe à carburant (repérer sur le boîtier à fusibles) puis démarrer le moteur et le laisser caler par manque de carburant.
    Méthode 2 — sur certains common rail, actionner la valve de décharge manuelle sur la rampe haute pression. Attendre 10
    minutes après extinction pour laisser la pression résiduelle se dissiper dans la rampe. - Préparer la zone d''intervention
    : placer plusieurs chiffons absorbants autour du capteur pour récupérer le carburant résiduel. Travailler en espace ventilé
    — les vapeurs de gazole sont inflammables au- dessus de 55°C. Interdire toute flamme, cigarette ou outil générant des
    étincelles dans le périmètre immédiat. - Débrancher le connecteur électrique : appuyer sur le clip de déverrouillage et
    tirer dans l''axe du connecteur. Ne pas tirer sur les fils. Noter l''orientation du connecteur pour la repose. - Dévisser
    le capteur défaillant : utiliser une douille ou une clé de bonne taille (dimensions selon modèle, généralement 19 à 27
    mm). Desserrer lentement et progressivement — un léger suintement de carburant résiduel est normal et attendu. Récupérer
    le carburant avec les chiffons. Ne pas forcer si le capteur résiste : un capteur grippé dans l''aluminium de la rampe
    peut arracher le filetage. Utiliser un dégrippant pénétrant et attendre 15 minutes avant de retenter. - Inspecter le logement
    : nettoyer le taraudage avec un écouvillon. Vérifier visuellement l''état des filets : un filet endommagé dans la rampe
    haute pression nécessite un retaraudage ou le remplacement de la rampe. Contrôler l''état du joint d''étanchéité dans
    le logement : le retirer s''il est resté en place. - Préparer le nouveau capteur : vérifier que le joint torique neuf
    est en place. Ne pas lubrifier le joint avec du gasoil ni avec de la graisse minérale — utiliser uniquement de la graisse
    compatible carburant (Vaseline technique) sur le joint seul. - Visser le capteur neuf : engager à la main sur les premiers
    filets pour éviter le coincement. Serrer au couple constructeur indiqué (généralement 15 à 25 N.m selon le modèle). Ne
    pas dépasser ce couple sur une rampe aluminium. - Reconnecter et remettre en service : remettre le fusible de pompe, mettre
    le contact en position II pendant 3 à 5 secondes pour amorcer la pompe avant de démarrer. Démarrer et contrôler l''absence
    de fuite pendant 10 minutes.'
  S5: '- Intervenir sans dépressurisation préalable : ouvrir un raccord sur circuit common rail sous pression (jusqu''à 2
    500 bar) projette du carburant à très grande vitesse. Une projection de gazole chaud au contact d''une surface à plus
    de 55°C peut s''enflammer. La dépressurisation n''est pas optionnelle. - Confondre capteur haute pression et capteur basse
    pression : sur les moteurs common rail, il existe souvent deux capteurs de température carburant : l''un sur la rampe
    haute pression (jusqu''à 2 500 bar) et l''autre sur le retour basse pression. Les deux pièces se ressemblent mais ne sont
    pas interchangeables. Vérifier la position dans le circuit sur le schéma hydraulique avant commande. - Réutiliser le joint
    torique d''origine : un joint torique comprimé lors du premier montage perd son élasticité. Remonter un joint usagé produit
    une micro-fuite de carburant qui s''amplifie à chaud et sous pression. Toujours installer le joint neuf fourni avec le
    capteur ou acheter un joint de même section et de même matière (Viton recommandé pour les circuits carburant haute pression).
    - Forcer sur un filetage grippé : le corps du capteur est souvent en acier inoxydable vissé dans une rampe en aluminium.
    La différence de dilatation thermique entre les deux métaux peut gripper le filetage après des années de service. Forcer
    provoque l''arrachage des filets dans la rampe aluminium, une réparation complexe. Utiliser un dégrippant pénétrant et
    attendre 15 minutes, ou chauffer prudemment la rampe à la chaleur douce (pistolet à air chaud, jamais de chalumeau). -
    Omettre le test de fuite à chaud : une installation peut sembler étanche à froid mais fuir légèrement à chaud sous pression
    maximale. Faire tourner le moteur 10 à 15 minutes jusqu''à température de fonctionnement et inspecter le raccord avec
    une lingette blanche. Toute trace de carburant impose un reserrage ou un remplacement du joint. - Commander sur la seule
    référence OBD sans vérifier la position : les codes P0180 à P0189 peuvent être déclenchés par plusieurs capteurs sur le
    même moteur. Identifier avec précision le capteur défaillant (mesure de résistance au multimètre sur chaque capteur) avant
    de commander.'
  S6: '- Test d''étanchéité à froid puis à chaud : démarrer le moteur et laisser tourner 15 minutes. Inspecter le raccord
    du capteur avec une lingette blanche propre à froid (après 2 minutes) puis à chaud (après 15 minutes de fonctionnement).
    Toute trace de carburant, même infime, indique une micro- fuite à traiter immédiatement. - Vérification de la disparition
    des codes défauts OBD : connecter un scanner OBD après la remise en service. Effacer les codes P0180–P0189 et surveiller
    leur ré-apparition sur les 20 premiers kilomètres. Si le code revient, mesurer la résistance du capteur à température
    stabilisée et la comparer aux valeurs constructeur. - Lecture de la valeur en temps réel : avec un scanner ou un outil
    multimarque (VCDS, Autel, Launch), afficher la valeur de température carburant en données en direct. À froid (5 à 10°C),
    la valeur doit être cohérente avec la température ambiante. À chaud (60 à 80°C), la valeur doit évoluer progressivement.
    Une valeur figée ou incohérente indique un capteur défaillant ou un problème de connecteur. - Observation de la consommation
    sur les 50 premiers kilomètres : une consommation anormalement haute (hausse de 1 à 3 L/100 km sans cause apparente) suggère
    que le calculateur corrige le dosage d''injection sur la base d''une valeur de température incorrecte. Vérifier la valeur
    OBD en temps réel. - Contrôle de l''absence de fumées à l''échappement : des fumées noires indiquent un enrichissement
    du mélange (capteur envoyant une température trop basse). Des fumées blanches peuvent signaler une temperature perçue
    trop haute et un mélange appauvri. Un premier essai sur route avec observation de l''échappement confirme le bon fonctionnement.'
  S7: 'Le capteur de température de carburant fait partie du circuit d''injection haute pression. Son remplacement est l''occasion
    d''inspecter les composants du même circuit qui subissent les mêmes conditions de pression et de température. - Capteur
    de pression common rail — situé sur la même rampe haute pression, il mesure la pression d''injection (jusqu''à 2 500 bar).
    Si des codes défauts injection multiples sont présents simultanément, les deux capteurs sont à contrôler ensemble. Un
    test de résistance électrique et une vérification de la valeur OBD en temps réel permettent de cibler le capteur défaillant.
    - Pompe à haute pression carburant — si la pression réelle dans la rampe est faible malgré un capteur de pression sain,
    la pompe haute pression est en cause. Une pression de rampe inférieure à 250 bar au ralenti sur un moteur common rail
    indique une pompe usée ou des régulateurs de débit défaillants. - Régulateur de pression carburant — il maintient la pression
    de rampe à la valeur demandée par le calculateur. Un régulateur défaillant entraîne des fluctuations de pression que le
    capteur de température peut détecter indirectement via des corrections d''injection erratiques. - Filtre à carburant —
    un filtre colmaté réduit le débit vers la pompe haute pression et provoque des chutes de pression. À remplacer lors de
    l''intervention pour éviter toute contamination du circuit neuf. Intervalle recommandé : tous les 30 000 km sur diesel
    common rail. - Injecteurs — les injecteurs sont alimentés depuis la rampe haute pression. Une mauvaise lecture de la température
    carburant peut masquer des corrections d''injection incorrectes liées à des injecteurs usés ou encrassés. Si la consommation
    reste élevée malgré un capteur neuf, tester les injecteurs au banc ou via un test de contribution cylndre par cylindre.'
  S8: 'Quels codes défauts OBD sont liés au capteur de température de carburant ? Les codes les plus fréquents sont P0180
    (circuit défaillant), P0181 (plage ou performance hors valeurs), P0182 (signal bas — tension inférieure à 0,2 V) et P0183
    (signal haut — tension supérieure à 4,8 V). Ces codes sont également déclenchés par un connecteur corrodé, un câble sectionné
    ou un mauvais contact. Avant de commander le capteur, débrancher le connecteur et mesurer la résistance entre les broches
    avec un multimètre : à 20°C la résistance doit être de 2 000 à 3 000 ohms sur la grande majorité des capteurs NTC. Une
    résistance infinie ou nulle confirme le capteur défaillant. La surconsommation de carburant peut-elle venir de ce capteur
    ? Oui. Le calculateur moteur utilise la valeur de température carburant pour corriger la masse injectée : un carburant
    froid est plus dense et l''injection est légèrement augmentée. Si le capteur envoie en permanence une valeur de température
    basse (capteur bloqué sur valeur froide), le calculateur enrichit le mélange en permanence et la consommation augmente
    de 1 à 3 L/100 km. Un scanner OBD permet de comparer la valeur transmise par le capteur à la température de liquide de
    refroidissement après chauffe complète — les deux valeurs doivent être proches une fois le moteur stabilisé. Ce capteur
    est-il présent sur les moteurs essence ? Il est principalement répandu sur les moteurs diesel à injection common rail
    (HDi, TDCi, CDI, CRDI, dCi) car la viscosité du gazole varie significativement avec la température. On le retrouve également
    sur certains moteurs essence à injection directe haute pression (TSI, TFSI 1.8 et 2.0 TFSI EA888, GDI Hyundai/Kia) où
    la pression d''injection dépasse 200 bar et où la température carburant influence les corrections d''injection. Sur les
    anciens moteurs essence à injection indirecte (MPI), ce capteur est généralement absent ou remplacé par un capteur de
    température d''air admission. Peut-on tester le capteur sans le démonter ? Oui, en deux étapes. Premièrement, mesurer
    la résistance électrique entre les broches du connecteur débranché avec un multimètre : à 20°C la valeur attendue est
    de 2 000 à 3 000 ohms sur un capteur NTC standard ; une résistance infinie indique un circuit ouvert, une résistance nulle
    un court-circuit. Deuxièmement, si le capteur est accessible sur circuit froid, démarrer le moteur et observer l''évolution
    de la valeur sur scanner en temps réel : la valeur doit augmenter progressivement de la température ambiante vers 60–80°C
    pendant la chauffe. Une valeur figée confirme un capteur hors service. Faut-il remplacer le joint d''étanchéité en même
    temps que le capteur ? Systématiquement. Le joint torique ou le joint conique du capteur est comprimé lors du premier
    montage et perd son élasticité. Remonter le capteur avec l''ancien joint produit une micro-fuite de carburant à haute
    pression qui s''amplifie à chaud. Les kits capteur incluent généralement un joint neuf. Si le capteur est vendu seul,
    commander le joint correspondant (numéro de section et matière Viton pour les circuits haute pression).'
---

# Capteur température de carburant

<!-- A enrichir : Phase 5 -->


## References supplementaires

<!-- materialized-from-db manual/3473873e08ac 2026-04-03 -->
### Données techniques OEM — Capteur température de carburant

# Données techniques OEM — Capteur température de carburant
Source : fr.wikipedia.org (1 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- Hall
- inductif
- pneumatique
- électrique

## Matériaux
- aluminium
- platine

## Valeurs techniques de référence
- 0,1 %
- 1,5 %
- 14 %
- 4,5 %
- 400 °C
