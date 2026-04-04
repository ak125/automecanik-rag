---
category: accessoires
slug: attelage
title: Attelage
pg_id: 39
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
  role: Permet de tracter une remorque ou une caravane
  must_be_true:
  - tracter
  - remorquer
  - accrocher
  must_not_contain:
  - freinage
  - suspension
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - tracter
  - remorquer
  - accrocher
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
  - ❌ "securite garantie"
  cost_range:
    min: 150
    max: 500
    currency: EUR
    unit: attelage complet
    source: catalogue automecanik
  quality_tiers:
  - tier: Attelage origine constructeur
    description: Fourni par le reseau constructeur, cote pour le vehicule exact. Garantit la compatibilite avec le faisceau
      electrique d'origine et les points de fixation chassis.
  - tier: Equipementier specialise homologue
    description: Fabricants specialises dans l'attelage automobile, proposant des produits homologues par vehicule. Compatibilite
      validee par reference vehicule (marque, modele, annee, carrosserie).
  - tier: Attelage demontable ou escamotable
    description: Variante permettant de masquer la boule quand elle n'est pas utilisee. Disponible chez plusieurs equipementiers
      specialises. Verifier la compatibilite et l'homologation specifique a ce type.
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
    label: Boule attelage usee tete attelage
    severity: confort
  - id: S2
    label: Corrosion importante sur la traverse ou la boule
    severity: confort
  - id: S3
    label: Fissures visibles sur les soudures
    severity: confort
  - id: S4
    label: Faisceau electrique defaillant feux remorque
    severity: confort
  - id: S5
    label: Bruits de claquement lors du tractage
    severity: confort
  - id: S6
    label: Attelage non homologue controle technique
    severity: confort
  - id: S7
    label: Remorque oscille anormalement route signe
    severity: confort
  - id: S8
    label: Odeur caoutchouc brule provenant pneus
    severity: securite
  - id: S9
    label: Plus utilisation forte utilisation controle
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : boule attelage usee tete attelage'
  quick_checks:
  - 'Observer : boule attelage usee tete attelage ?'
  - 'Observer : corrosion importante sur la traverse ou la boule ?'
  - 'Observer : fissures visibles sur les soudures ?'
  - 'Observer : faisceau electrique defaillant feux remorque ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Boule attelage usee tete attelage
  - Corrosion importante sur la traverse ou la boule
  - Fissures visibles sur les soudures
  - Faisceau electrique defaillant feux remorque
  - Bruits de claquement lors du tractage
  - Attelage non homologue controle technique
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '39'
  intro_title: A quoi sert Attelage ?
  risk_title: Pourquoi remplacer Attelage a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
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
  - question: Attelage OE ou adaptable ?
    answer: Les attelages OES (Westfalia, Brink, Bosal) sont homologués et de qualité équivalente à l'OE. Vérifiez la charge
      tractable et la masse sur flèche compatibles avec votre véhicule.
  - question: Comment savoir si mon attelage est usé ?
    answer: Boule d'attelage usée (diamètre inférieur à 49mm), jeu dans la rotule, corrosion importante sur la traverse, fissures
      visibles, faisceau électrique défaillant.
  - question: Tous les combien contrôler l'attelage ?
    answer: Contrôle visuel annuel recommandé. Vérifiez l'usure de la boule (calibre 49-50mm), l'état des soudures, la corrosion
      et le fonctionnement du faisceau électrique.
  - question: Peut-on monter un attelage soi-même ?
    answer: Oui mais nécessite parfois de percer le pare-chocs ou déposer des éléments. Le faisceau électrique doit être correctement
      branché. Prévoir 2 à 4h selon modèle.
  - question: Quelle erreur éviter avec l'attelage ?
    answer: Dépasser le PTAC ou le poids sur flèche maximal. Vérifiez toujours les capacités indiquées sur la plaque signalétique
      de l'attelage avant de tracter.
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
doc_id: 082d5626-cbb8-5aeb-ac0e-846fafe570b2
content_hash: sha256:41af83a352c9cebb
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
  _has_tech_data: false
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Un attelage réalise la liaison entre deux véhicules. En général, l'un des
    véhicules est tractant et l'autre est remorqué. Un attelage doit avoir des
    propriétés particulières : - résistance mécanique à la traction pour
    transmettre l'effort de remorquage et éviter une rupture d'attelage. -
    souplesse pour s'adapter facilement aux positions relatives de la remorque
    par rapport au véhicule tracteur. - rigidité pour transmettre les variations
    de vitesse aux différents véhicules et éviter les mouvements intempestifs de
    la remorque qui entra&icirc;nent des collisions entre tracteur et remorque.
    Le crochet d'attelage est situé à l'arrière de véhicule au niveau du pare-
    choc arrière on peut utiliser le crochet d'attelage pour remorquer un
    véhicule une caravane etc. En savoir plus : attelage — définition et rôle
    mécanique 🚨 Bruit Attelage : causes et diagnostic
  S2: >-
    Le dispositif d'attelage n'a pas une période de remplacement puisque c'est
    une pièce conçue à vivre le plus longtemps possible. Mais il faut faire un
    contrôle de temps en temps pour vérifier la fixation du crochet d'attelage
    pour ne pas courir de risque on remorquant un engin sur la route. Diagnostic
    complet : identifier une panne de attelage
  S3: >-
    Un attelage est une pièce d'accrochage soumise à des charges importantes et
    à la réglementation du contrôle technique. Le choix doit s'appuyer sur des
    données techniques précises, pas sur une estimation approximative. - Marque,
    modèle, motorisation et année : l'attelage est conçu pour les points de
    fixation spécifiques du châssis de votre véhicule. Une mauvaise référence
    rend le montage impossible ou crée un défaut à la prise du contrôle
    technique. - Masse remorquable autorisée (MMA) : vérifiez dans la carte
    grise du véhicule la masse remorquable avec et sans freinage. Le col de
    cygne doit être homologué pour une charge au minimum égale à la MMA inscrite
    sur la carte grise. - Charge verticale (masse sur boule D) : la charge
    verticale maximale sur la boule est généralement de 75 à 100 kg selon les
    constructeurs. Vérifiez que ce paramètre correspond aux besoins de votre
    caravane ou remorque. - Type d'attelage — amovible ou fixe : l'attelage
    amovible (col de cygne débrochable) se retire en quelques secondes pour ne
    pas gêner l'accès au coffre et éviter les dommages en stationnement.
    L'attelage fixe est plus robuste mais encombre en permanence. - Conformité
    CE et homologation : exigez un attelage portant le marquage CE avec le
    numéro d'homologation européen (directive 94/20/CE). Sans homologation, le
    véhicule sera refusé au contrôle technique. - Faisceau électrique compatible
    : vérifiez si le véhicule nécessite un faisceau 7 broches (norme NF ISO
    1724) ou 13 broches (norme NF ISO 11446) selon le type de remorque. Le
    faisceau doit être commandé en même temps que l'attelage pour assurer la
    compatibilité électrique. - Boule de remorquage : la boule est souvent
    vendue séparément. Vérifiez le diamètre (50 mm est la norme européenne) et
    le type de fixation (boule à serrage par écrou ou boule intégrée). Pour
    aller plus loin : consultez notre guide d'achat attelage — comparatif
    marques, critères de choix et prix.
  S4_DEPOSE: >-
    La dépose d'un attelage implique de travailler sous le véhicule sur des
    fixations souvent corrodées. Prévoyez un dégrippant, une clé dynamométrique,
    un cric et des chandelles. Comptez 1 h 30 à 3 heures selon l'état des
    fixations et le type d'attelage. - Sécurité et mise en position : stationnez
    sur sol plat, serrez le frein à main, coupez le contact. Déconnectez la
    borne négative de la batterie avant de manipuler le faisceau électrique pour
    éviter tout court-circuit sur la prise remorque. - Déconnexion du faisceau
    électrique : repérez le connecteur du faisceau attelage sous le pare-choc
    arrière ou dans la roue de secours. Débranchez le connecteur et notez le
    cheminement du câble pour faciliter le remontage ou le remplacement. -
    Dépose du pare-choc arrière si nécessaire : sur certains modèles, l'accès
    aux boulons de fixation de la traverse d'attelage requiert de retirer
    partiellement ou totalement le pare-choc. Consultez la procédure
    constructeur spécifique à votre modèle. - Application du dégrippant :
    pulvérisez un dégrippant pénétrant sur tous les boulons de fixation de la
    traverse et laissez agir 15 à 20 minutes. Les fixations d'attelage sont
    exposées aux intempéries et à la corrosion de la route ; un écrou grippé
    peut exiger une perceuse ou une scie si le dégrippant ne suffit pas. -
    Desserrage des boulons de traverse : l'attelage est fixé à la caisse ou au
    longeron par 4 à 8 boulons selon le modèle (diamètre M10 à M14, couples de
    serrage de 40 à 100 Nm). Desserrez progressivement en alternant les côtés
    pour éviter de déformer la traverse. - Extraction de la traverse : faites-
    vous assister pour tenir la traverse pendant l'extraction des derniers
    boulons — la traverse peut peser de 5 à 15 kg selon le modèle. Posez-la sur
    un établi pour inspecter l'état des soudures et la corrosion avant toute
    décision de réutilisation. - Diagnostic des points de fixation caisse :
    inspectez les renforts de caisse ou longerons après dépose. Si des traces de
    rouille perforante sont visibles, faites traiter les zones avant de poser le
    nouvel attelage. - Dépose de la boule si réutilisée : si la boule est en bon
    état (pas d'usure plate, pas de corrosion profonde), dévissez l'écrou de
    boule (couple élevé, souvent 200 Nm ou plus) et réutilisez-la sur le nouvel
    attelage après vérification du filetage.
  S4_REPOSE: >-
    Une fois la traverse neuve ou vérifiée, la repose doit être réalisée avec
    méthode pour garantir la tenue mécanique et la conformité réglementaire. Le
    non-respect des couples de serrage est la première cause de défaillance
    après remontage. Comptez 1 h à 2 h selon le modèle. - Contrôle des renforts
    de caisse avant repose : Inspectez les points d'ancrage sur le longeron ou
    la caisse. Toute zone de rouille perforante doit être traitée (apprêt
    antirouille) avant de reposer l'attelage. Une fixation sur métal corrodé ne
    tient pas au couple prescrit. - Positionnement de la traverse : Avec l'aide
    d'un assistant, positionnez la traverse en alignant les trous de fixation
    avec les inserts de caisse. Engagez les boulons à la main sur au moins 3 pas
    de vis avant de commencer le serrage — évitez de forcer dès le premier tour
    pour ne pas croiser les filetages. - Serrage progressif et alterné des
    boulons : Serrez les boulons en alternance côté gauche / côté droit, en deux
    passes. Première passe à 50 % du couple, deuxième passe à la clé
    dynamométrique au couple constructeur — généralement 40 à 100 Nm selon
    diamètre (M10 : 45–55 Nm, M12 : 75–85 Nm, M14 : 90–100 Nm). - Repose de la
    boule d'attelage : Vissez la boule à la main jusqu'au contact avec la
    plaque, puis serrez à la clé dynamométrique au couple prescrit (souvent 200
    à 250 Nm). Vérifiez qu'il n'y a aucun jeu radial une fois serrée — un jeu
    résiduel indique un filetage usé ou un couple insuffisant. - Cheminement et
    connexion du faisceau électrique : Repassez le câble selon le tracé
    d'origine, à l'abri des parties chaudes et des zones de frottement. Fixez
    avec des colliers aux points d'attache prévus. Branchez le connecteur
    remorque jusqu'au verrouillage audible du clip. - Test électrique du
    faisceau : Connectez une remorque ou une fiche de test 7/13 broches et
    vérifiez le fonctionnement de chaque feu : feux de position, stop,
    clignotants gauche et droit, feux de recul, anti-brouillard arrière. Testez
    la masse remorque pour détecter tout problème de masse flottante. - Repose
    du pare-choc si déposé : Remontez le pare-choc avec ses clips, vis et
    agrafes dans l'ordre inverse de la dépose. Vérifiez l'alignement et
    l'absence de jeu latéral. Assurez-vous que la boule dépasse correctement à
    travers l'ouverture prévue. - Contrôle réglementaire final : Vérifiez la
    plaque d'homologation de l'attelage (charge tractable, masse sur flèche) et
    comparez avec les valeurs inscrites dans la carte grise du véhicule. Un
    attelage dont la charge tractable est inférieure à celle du véhicule doit
    être remplacé par un modèle homologué correspondant.
  S5: >-
    Le montage d'un attelage engage la sécurité du conducteur, des passagers et
    des autres usagers de la route. Ces cinq erreurs, très courantes lors d'une
    pose en autonomie, peuvent entraîner des conséquences graves. - Monter un
    attelage sans vérifier la MMA autorisée par le constructeur : chaque
    véhicule a une masse remorquable maximale inscrite dans sa carte grise.
    Tracter une remorque dépassant ce seuil surcharge le châssis, dégrade les
    amortisseurs et peut entraîner un refus au contrôle technique, voire un
    accident en cas de perte de contrôle de la remorque en descente. - Ne pas
    serrer les boulons au couple prescrit : un serrage insuffisant (<40 Nm sur
    des boulons M12) provoque un mouvement de la traverse dès les premières
    sollicitations en traction. Un serrage excessif déforme les renforts de
    caisse et peut rendre le démontage impossible. Utilisez toujours une clé
    dynamométrique avec le couple constructeur. - Omettre de brancher le
    faisceau électrique ou brancher incorrectement : rouler sans feux de
    remorque (stop, clignotants) est une infraction routière passible d'amende.
    De plus, une connexion inversée grille le module de gestion des feux sur les
    véhicules récents. Vérifiez le câblage sur la base du schéma fourni avec le
    faisceau. - Réutiliser un attelage corrodé présentant des fissures aux
    soudures : des fissures sur les cordons de soudure sont un signe de fatigue
    structurelle. Une soudure fissurée peut céder brutalement en charge,
    entraînant le découplage de la remorque à pleine vitesse. La réparation par
    soudure d'un attelage structurel n'est pas admissible — le remplacement
    s'impose. - Ne pas tester le faisceau électrique avant le premier tractage :
    branchez la prise remorque et testez les feux stop, clignotants et feux de
    position avec un second vérificateur derrière le véhicule (ou une douille de
    test). Un faisceau mal connecté se détecte en 2 minutes mais peut coûter une
    amende ou causer un accident si non détecté.
  S6: >-
    Avant le premier tractage, un ensemble de vérifications structurées s'impose
    pour s'assurer que l'attelage est correctement installé, homologué et
    électriquement fonctionnel. Ce protocole s'applique aussi bien après une
    pose neuve qu'après une repose suite à dépose temporaire. - Contrôle des
    couples de serrage : revérifiez tous les boulons de la traverse avec une clé
    dynamométrique selon les valeurs prescrites par le fabricant de l'attelage
    (généralement 40 à 100 Nm selon le diamètre). Ne contrôlez pas au toucher —
    la dynamométrie est le seul indicateur fiable. - Test des feux de remorque :
    branchez une remorque ou un testeur de prise 7 ou 13 broches et vérifiez le
    fonctionnement des feux stop (pédale frein), des clignotants gauche et
    droit, des feux de position arrière et du feu de marche arrière si présent.
    Un voyant absent indique une connexion défaillante ou un fusible grillé. -
    Inspection visuelle de la boule : vérifiez que la boule est correctement
    serrée (couple d'écrou de boule souvent entre 150 et 250 Nm selon le
    modèle), sans jeu en rotation ni en basculement axial. Une boule mal serrée
    peut se dévisser sous la charge dynamique. - Contrôle de l'absence de
    contact avec le pare-choc ou les feux : simulez un braquage complet avec et
    sans remorque pour vérifier qu'aucun élément ne frotte sur la traverse ou la
    boule. Un frottement abîme la carrosserie et peut bloquer la direction. -
    Vérification du comportement à l'essai statique : accrochez une charge
    représentative (ou la remorque habituelle) et tirez manuellement le crochet
    d'attelage vers le bas avec une force progressive. Aucun mouvement de la
    traverse ni bruit de claquement ne doit se produire. - Premier trajet court
    avec charge : effectuez un premier trajet chargé de 5 à 10 km à vitesse
    modérée. Après le retour, revérifiez les boulons de traverse (possibilité de
    tassement au premier chargement) et l'absence de fuites ou de déformations
    visibles. - Vérification de l'homologation pour le contrôle technique :
    assurez-vous que la plaque d'homologation de l'attelage est visible et
    lisible. Photographiez-la avec la masse remorquable et le numéro de
    réception pour vos archives.
  S7: >-
    L'attelage fonctionne rarement seul : lors d'une intervention sur la
    traverse ou la boule, plusieurs pièces adjacentes méritent d'être inspectées
    ou remplacées simultanément pour éviter une seconde intervention rapprochée.
    - Faisceau électrique d'attelage (7 ou 13 broches) — Le câblage du faisceau
    vieillit avec l'attelage : connecteurs oxydés, gaine craquelée, masse
    défaillante. Un attelage neuf avec un faisceau usé engendre des pannes
    électriques intermittentes sur les feux de remorque. - Boule d'attelage et
    collerette de serrage — La boule s'use par frottement avec la tête
    d'attelage de la remorque. Un diamètre inférieur à 49 mm (standard 50 mm)
    crée un jeu dangereux. À inspecter au calibre lors de chaque contrôle
    annuel. - Platine de tête d'attelage — La platine reçoit les contraintes
    mécaniques lors du tractage. Des fissures ou une déformation de la platine
    compromettent la rigidité de l'assemblage même avec une traverse saine. -
    Silentblocs de traverse — Sur les attelages avec amortissement caoutchouc,
    les silentblocs absorbent les vibrations de traction. Des silentblocs fendus
    transmettent les chocs à la caisse et créent des bruits sourds au démarrage
    traction. - Boulons et écrous de fixation (classe 8.8 minimum) — Les boulons
    d'attelage sont des pièces de sécurité. Ne jamais réutiliser des boulons
    corrodés ou ayant subi un couple excessif. Remplacer systématiquement lors
    d'une repose. - Stabilisateur de couple (antiroulis de remorque) —
    Accessoire recommandé pour les remorques de plus de 1 000 kg, il réduit les
    oscillations pendulaires lors du tractage sur autoroute.
  S8: >-
    Un attelage usagé peut-il être réutilisé après dépose pour vente du véhicule
    ? Oui, à condition que la traverse ne présente ni corrosion perforante, ni
    fissures aux cordons de soudure, ni déformation visible de la boule (usure
    plate sur la sphère). La boule est mesurable : un diamètre inférieur à 49,6
    mm (norme tolérant -0,4 mm sur les 50 mm nominaux) impose le remplacement de
    la boule seule. La traverse peut être reposée sur un autre véhicule
    uniquement si elle est homologuée pour ce modèle — une traverse n'est pas
    interchangeable entre modèles différents. Quelle différence entre faisceau 7
    broches et 13 broches ? Le faisceau 7 broches (norme ISO 1724) gère les
    fonctions de base : feux stop, clignotants, feux de position, feu de recul
    et alimentation 12 V accessoire. Le faisceau 13 broches (norme ISO 11446)
    ajoute la gestion de l'alimentation de la batterie de la remorque et des
    fonctions avancées (ABS remorque, stabilisateur). Les caravanes modernes et
    les remorques frigorifiques nécessitent 13 broches. Vérifiez les
    spécifications de votre remorque avant commande du faisceau. Mon véhicule
    peut-il passer le contrôle technique avec un attelage amovible en position
    retirée ? Oui. Un attelage amovible n'est pas contrôlé à proprement parler
    lors du contrôle technique lorsqu'il est en position débrochée. Cependant,
    si le col de cygne est présent pendant le contrôle, l'homologation et l'état
    de la boule seront vérifiés. Une boule usée ou un attelage sans plaque
    d'homologation lisible entraîne un défaut. Peut-on tracter une remorque avec
    un véhicule dont la carte grise indique 0 kg de masse remorquable ? Non. Si
    la carte grise mentionne 0 kg ou si la masse remorquable n'est pas
    renseignée, le tractage est juridiquement interdit même avec un attelage
    homologué installé. Certains constructeurs peuvent fournir une attestation
    de modification permettant d'inscrire une masse remorquable sur la carte
    grise, sous réserve que le châssis supporte la modification — renseignez-
    vous auprès du constructeur. Le bruit de claquement à l'arrière lors du
    tractage signifie-t-il que l'attelage est défaillant ? Un claquement au
    démarrage ou lors des à-coups peut indiquer un jeu excessif dans
    l'accouplement remorque-boule (crochet de remorque mal serré), un boulon de
    traverse desserré, ou une usure avancée de la boule. Commencez par vérifier
    le serrage du crochet de remorque sur la boule. Si le claquement persiste,
    contrôlez les boulons de traverse et l'état de la boule avant de continuer à
    tracter.
  META: >-
    {"meta_title":"Attelage voiture : boule usée ou corrosion ? |
    AutoMecanik","meta_description":"Boule d'attelage usée, corrosion sur la
    traverse ou faisceau défaillant ? Vérifiez l'homologation et trouvez
    l'attelage compatible (Westfalia, Brink, Bosal).","og_title":"Attelage :
    diagnostic usure et remplacement","og_description":"Claquement lors du
    tractage, remorque qui oscille ou corrosion visible : les signes d'un
    attelage à remplacer. Guide homologation, PTAC et compatibilité véhicule.","
    canonical_intent":"diagnostic","schema_type":"HowTo","sources":[{"type":"rag
    ","ref":"gammes/attelage.md","field":"domain.role + diagnostic.symptoms +
    rendering.faq"}]}
---

# Attelage - Guide Diagnostic Complet

## Fonction et Rôle

Permet de tracter une remorque ou une caravane

**Actions principales:** tracter, remorquer, accrocher

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruits de claquement lors du tractage**
  bruits de claquement lors du tractage

### 🟡 Symptômes de Sécurité

- **Odeur caoutchouc brule provenant pneus**
  odeur caoutchouc brule provenant pneus

### 🟢 Autres Symptômes

- boule attelage usee tete attelage
- corrosion importante sur la traverse ou la boule
- fissures visibles sur les soudures
- faisceau electrique defaillant feux remorque
- attelage non homologue controle technique
- remorque oscille anormalement route signe

## Procédure de Diagnostic

Pour diagnostiquer un problème de attelage:

1. **Inspection visuelle** - Examiner l'état du attelage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- faisceau attelage
- boule

## Critères de Compatibilité

Pour commander le bon attelage, vous devez connaître:

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

**Attelage OE ou adaptable ?**
Les attelages OES (Westfalia, Brink, Bosal) sont homologués et de qualité équivalente à l'OE. Vérifiez la charge tractable et la masse sur flèche compatibles avec votre véhicule.

**Comment savoir si mon attelage est usé ?**
Boule d'attelage usée (diamètre inférieur à 49mm), jeu dans la rotule, corrosion importante sur la traverse, fissures visibles, faisceau électrique défaillant.

**Tous les combien contrôler l'attelage ?**
Contrôle visuel annuel recommandé. Vérifiez l'usure de la boule (calibre 49-50mm), l'état des soudures, la corrosion et le fonctionnement du faisceau électrique.

**Peut-on monter un attelage soi-même ?**
Oui mais nécessite parfois de percer le pare-chocs ou déposer des éléments. Le faisceau électrique doit être correctement branché. Prévoir 2 à 4h selon modèle.

**Quelle erreur éviter avec l'attelage ?**
Dépasser le PTAC ou le poids sur flèche maximal. Vérifiez toujours les capacités indiquées sur la plaque signalétique de l'attelage avant de tracter.
