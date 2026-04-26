---
category: moteur
slug: capteur-temperature-d-huile
title: Capteur temperature d'huile
pg_id: 829
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-04-04'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: low
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:materialize-db-to-md
  last_enriched_at: '2026-04-04'
  v5_migrated_at: '2026-03-29'
domain:
  role: Mesurer la temperature de l'huile moteur pour adapter la lubrification et informer le conducteur
  must_be_true:
  - mesurer la temperature
  - huile moteur
  - information au calculateur
  must_not_contain:
  - universel
  - tous modeles
  - adaptable tous
  confusion_with:
  - term: capteur-pression-d-huile
    difference: Le capteur temperature mesure la chaleur de l'huile, le capteur pression mesure la pression dans le circuit
      de lubrification
  - term: sonde-de-refroidissement
    difference: La sonde de refroidissement mesure la temperature du liquide de refroidissement, pas de l'huile
  related_parts:
  - capteur-pression-d-huile
  - carter-d-huile
  - filtre-a-huile
  - radiateur-d-huile
selection:
  criteria:
  - Marque de votre vehicule
  - Modele de votre vehicule
  - Motorisation de votre vehicule
  - Annee de votre vehicule
  - Type de filetage et longueur de sonde
  - Nombre de broches du connecteur
  anti_mistakes:
  - universel
  - tous modeles
  - adaptable tous
  brands:
    premium:
    - Bosch
    - Valeo
    - Denso
    standard:
    - Hella
    - NGK
    - Delphi
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Indication de temperature d'huile incorrecte au tableau de bord
    severity: confort
  - id: S2
    label: Voyant huile allume sans raison apparente
    severity: securite
  - id: S3
    label: Surconsommation de carburant (mauvaise gestion moteur)
    severity: confort
  causes:
  - sonde thermistance defaillante (circuit ouvert ou court-circuit)
  - connecteur oxyde ou fil endommage
  - encrassement de la sonde par les depots d'huile
  quick_checks:
  - 'Observer : indication de temperature d''huile incorrecte au tableau de bord ?'
  - Voyant huile allume sans raison apparente ?
  - 'Comparer la consommation : surconsommation de carburant (mauvaise gestion moteur) ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Pas de periodicite. Verifier en cas d'indication anormale au tableau de bord.
  wear_signs:
  - Indication de temperature d'huile incorrecte au tableau de bord
  - Voyant huile allume sans raison apparente
  - Surconsommation de carburant (mauvaise gestion moteur)
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '829'
  faq:
  - question: Comment tester le capteur temperature d'huile ?
    answer: Mesurer la resistance a froid et a chaud avec un multimetre. La valeur doit correspondre a la courbe constructeur
      (NTC generalement).
  - question: Capteur OE ou adaptable ?
    answer: Privilegier OE pour la precision de la courbe de resistance. Un capteur imprecis fausse la gestion moteur.
  - question: Peut-on rouler avec un capteur defaillant ?
    answer: Oui mais le calculateur n'aura pas l'information correcte, ce qui peut affecter la lubrification et la consommation.
  - question: Ne pas confondre avec le capteur pression d'huile ?
    answer: Ce sont deux capteurs distincts. Le capteur temperature est une thermistance, le capteur pression est un manocontact.
  - question: Quelle erreur eviter ?
    answer: Ne pas serrer excessivement (filetage delicat). Appliquer du teflon sur le filetage si specifie par le constructeur.
  quality:
    score: 60
    source: manual:claude-r3-kp
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modeles
  - adaptable tous
  requires_vehicle: true
doc_id: c51d0acc-4275-5159-a625-e85e1489da47
content_hash: sha256:0b285b8df177e8f1
lang: fr
variants:
- name: Piece neuve OE/OES
  aliases:
  - neuf
  - OE
  - OES
  functional_differences:
  - Garantie constructeur ou equipementier
  - Calibration d usine
- name: Piece echange standard
  aliases:
  - echange standard
  - reconditionne
  functional_differences:
  - Moins cher
  - Piece d origine reconditionnee
location_on_vehicle:
  area: Compartiment moteur (alternateur, demarreur) ou peripherie
  access: Par le dessus (capot) ou par le dessous selon modele
  adjacent_parts:
  - faisceau electrique
  - batterie
  - fusibles
installation:
  difficulty: facile a moyen
  time: 15min a 1h
  tools:
  - cle a douille
  - multimetre
  - tournevis
  prerequisite: Debrancher la batterie avant intervention
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-04'
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
  S1: Le capteur de température est un dispositif permettant de transformer l'effet du réchauffement ou du refroidissement
    sur leurs composants en signal électrique.Le capteur de température est un capteur de lecture. Le calculateur moteur l'utilise
    pour déterminer la température du moteur.Le capteur contient une résistance de type spécial. La valeur de cette résistance
    baisse quand la température du liquide de refroidissement monte.
  S2: Le capteur de température fournis des données importantes au calculateur de gestion du moteur. Un mauvais fonctionnement
    du capteur peut causer plusieurs problèmes par exemple un capteur de température défectueux va emp&ecirc;cher le moteur
    de fonctionner à une température adéquate, pouvant ainsi entra&icirc;ner une surchauffe. Il peut aussi entra&icirc;ner
    un mauvais rendement du moteur. Le capteur de température n'a pas de période de remplacement mais on doit faire un contrôle
    lorsqu'on constate qu'il y a un problème au niveau de la température du moteur.
  S3: 'Le capteur de température d''huile transmet en temps réel la valeur thermique du lubrifiant au calculateur moteur.
    Cette donnée pilote l''injection, la gestion de la ventilation et les seuils d''alerte. Un capteur avec une courbe de
    résistance inadaptée fausse toutes ces régulations sans générer de code défaut immédiat. Les critères de sélection sont
    les suivants : - Référence constructeur exacte ou référence OEM croisée : c''est le critère prioritaire. La courbe de
    résistance NTC (coefficient de température négatif) ou PTC (coefficient positif) est propre à chaque application. Un capteur
    avec une courbe décalée de 10% affiche une température d''huile erronée à toutes les plages de fonctionnement. Ne pas
    se fier uniquement aux dimensions mécaniques pour établir la compatibilité. - Nombre de broches et type de connecteur
    : les configurations courantes sont 1 broche (masse par corps du capteur), 2 broches (signal + masse séparée) et 3 broches
    (capteur combiné pression/température sur certains moteurs diesel modernes). Le brochage du connecteur de faisceau d''origine
    est le critère déterminant. - Filetage et pas de vis : M12x1,5 (le plus courant), M14x1,5 sur les blocs diesels plus anciens.
    Un mauvais filetage ne peut pas être forcé sans risquer de détériorer le logement taraudé dans le bloc ou le carter d''huile
    — une réparation qui peut nécessiter une dépose du carter. - Plage de mesure opérationnelle : la plage standard est -40°C
    à +150°C pour la plupart des moteurs. Sur les moteurs sport, turbo haute performance ou véhicules industriels, vérifier
    que le capteur est homologué pour une plage étendue pouvant atteindre +160°C ou +180°C. - Certification et équipementier
    : FAE, Hella, Bosch et Beru proposent des capteurs avec courbes NTC documentées et certifiées ISO. Exiger que la fiche
    produit mentionne les valeurs de résistance à 20°C, 80°C et 120°C pour vérification croisée avec les valeurs constructeur.
    - Ne pas confondre avec le capteur de pression d''huile : les deux capteurs sont souvent implantés côte à côte dans le
    bloc moteur. Leurs connecteurs peuvent être similaires. Se référer au schéma d''implantation du manuel constructeur pour
    identifier sans ambiguïté chaque capteur avant la dépose.'
  S4_DEPOSE: 'Le remplacement du capteur de température d''huile est accessible sur la plupart des motorisations sans outillage
    spécifique. Comptez 30 à 60 minutes selon l''accessibilité. La dépose entraîne une légère fuite d''huile — prévoir des
    chiffons absorbants et un récipient de récupération. Respecter impérativement les conditions de sécurité suivantes avant
    toute intervention : - Couper le contact et attendre le refroidissement complet : ne jamais intervenir moteur chaud. Attendre
    au minimum 2 heures après l''arrêt du véhicule. L''huile à 90–110°C sous pression résiduelle peut projeter du lubrifiant
    bouillant lors de la dépose du capteur, provoquant des brûlures graves. Confirmer le refroidissement en posant la main
    sur le carter — il doit être tiède, pas chaud. - Débrancher le câble négatif de la batterie : déconnecter la cosse négative
    (-) de la batterie avant toute intervention sur un composant électrique du moteur. Cela évite tout court-circuit accidentel
    lors de la manipulation du connecteur du capteur et protège le calculateur moteur. - Localiser le capteur à l''aide du
    schéma d''implantation : selon la motorisation, le capteur est implanté dans le bloc moteur (côté distribution ou côté
    volant moteur), dans le carter d''huile, ou dans la galerie d''huile de culasse. Sur les moteurs à double capteur combiné
    (pression + température), identifier précisément le capteur de température en comptant ses broches — 2 broches pour la
    température, 1 broche pour le pressostat simple. - Débrancher le connecteur électrique : appuyer fermement sur la languette
    de déverrouillage et extraire le connecteur en tenant son boîtier plastique, jamais en tirant sur les fils. Si le connecteur
    est oxydé ou figé, vaporiser un dégrippant électronique et attendre 3 à 5 minutes avant d''insister doucement. Inspecter
    l''état des broches (oxydation verte, écrasement) et noter leur condition pour évaluer si le câblage nécessite une réparation.
    - Positionner un chiffon absorbant sous le capteur : avant de dévisser, protéger les surfaces environnantes (courroies
    d''accessoires, durites en caoutchouc) contre les projections d''huile. Placer le chiffon directement sous le corps du
    capteur pour récupérer les 0,1 à 0,5 litre d''huile qui s''écoule lors du dévissage. - Dévisser le capteur avec la douille
    adaptée : utiliser une douille 6 pans de 19 mm ou 22 mm selon l''application (mesurer avec un pied à coulisse si incertain).
    Dévisser dans le sens antihoraire. Le capteur peut être légèrement collé par le joint torique comprimé lors du premier
    montage — une rotation initiale de 15° dans les deux sens aide à briser l''adhérence sans forcer en torsion sur le filetage.
    - Récupérer et inspecter le joint torique : noter l''état du joint — aplati, fissuré ou manquant. Ce joint ne se réutilise
    jamais. Si le nouveau capteur n''est pas livré avec un joint, commander un joint torique de dimensions exactes (mesurer
    le diamètre intérieur et la section du joint d''origine). Sur les capteurs à étanchéité par pâte, nettoyer le filetage
    du logement des résidus d''ancienne pâte avant remontage. - Vérifier l''état du filetage dans le bloc moteur : inspecter
    les filets taraudés avec une lampe torche. Si les filets présentent des résidus d''huile solidifiée ou de dépôts, les
    nettoyer avec un taraud de nettoyage (sans enlèvement de matière). Un filetage endommagé doit être réparé avec un insert
    hélicoïdal (hélicoïl) avant le remontage du nouveau capteur — forcer sur un filetage abîmé arrachera définitivement les
    filets dans le bloc.'
  S5: 'Ces erreurs lors du remplacement du capteur de température d''huile entraînent des fuites d''huile persistantes, des
    dommages structurels sur le moteur ou des mesures incorrectes qui compromettent la protection du circuit de lubrification
    : - Serrage excessif qui fissure le carter ou le bloc moteur : le filetage taraudé dans le carter d''huile en aluminium
    est particulièrement vulnérable. Un serrage au-delà de 15 N.m sur un logement M12 en aluminium peut provoquer des microfissures
    dans le métal environnant qui s''élargissent progressivement sous l''effet des cycles thermiques. La fuite d''huile apparaît
    2 à 6 semaines après l''intervention, au moment où les fissures traversent l''épaisseur de la paroi. Utiliser obligatoirement
    une clé dynamométrique et ne pas dépasser le couple constructeur (généralement 12 à 25 N.m selon le matériau du logement).
    - Remonter sans joint cuivre ou joint torique neuf : certains capteurs utilisent un joint cuivre plat (écrasement contrôlé)
    plutôt qu''un joint torique. Le joint cuivre ne se réutilise jamais — après le premier serrage, il est déformé de manière
    permanente et ne peut plus assurer l''étanchéité. Le négliger provoque une fuite d''huile invisible à froid qui devient
    visible à chaud, lorsque l''huile sous pression (3 à 5 bar en régime) trouve la voie de passage créée par le joint aplati.
    - Ne pas purger l''air du circuit d''huile après dépose : lors de la dépose du capteur, une poche d''air peut s''introduire
    dans le logement. Si le nouveau capteur est monté sans précaution, cette poche reste piégée dans le circuit et peut créer
    un manque de pression momentané au démarrage (cavitation) — perceptible par un bruit de claquement bref à la mise en route.
    Le remontage doit se faire capteur partiellement engagé pour laisser l''huile remplir le logement avant le serrage final.
    - Commande sans vérification du référencement exact : utiliser une référence approximative ou une référence croisée non
    validée conduit à recevoir un capteur dont le filetage, le nombre de broches ou la courbe NTC ne correspond pas à l''application.
    Un capteur avec un filetage M14×1,5 commandé pour une application M12×1,5 est impossible à monter sans forcer — le risque
    de faux- filet est immédiat. Toujours saisir la référence constructeur complète ou fournir la référence de la pièce déposée
    pour validation. - Connecteur mal verrouillé après remontage : le connecteur du capteur de température d''huile est soumis
    à des vibrations moteur permanentes et à des chocs thermiques répétés. Un connecteur partiellement engagé, sans clic de
    verrouillage confirmé, se dégage progressivement. La valeur de résistance transmise au calculateur devient instable :
    la température affichée oscille, le calculateur enregistre des codes défauts intermittents difficiles à reproduire en
    atelier. Vérifier le verrouillage en tirant sur le connecteur sans appuyer sur la languette — il ne doit pas bouger. -
    Confondre le signal capteur avec le circuit de masse : sur les câblages modifiés ou les faisceaux réparés, un inversement
    des fils signal et masse génère une valeur de résistance calculée incorrecte. Le calculateur interprète cette résistance
    comme une température hors plage et génère immédiatement un code défaut P019x. Avant de conclure à un capteur défectueux,
    vérifier la polarité du câblage avec le schéma électrique constructeur du véhicule.'
  S6: 'Ces contrôles permettent de confirmer que le capteur est correctement posé, étanche, et que sa mesure est cohérente
    avec la réalité thermique du moteur. Les effectuer séquentiellement pour isoler tout défaut résiduel avant de reprendre
    la route : - Contrôle d''étanchéité au démarrage : après avoir rebranché la batterie, démarrer le moteur et laisser tourner
    au ralenti pendant 5 minutes. Inspecter immédiatement la base du capteur avec une lampe torche et un chiffon propre. Toute
    trace d''huile, même en film mince, autour du filetage indique un joint insuffisamment comprimé ou un couple de serrage
    insuffisant. Couper le moteur, laisser refroidir 30 minutes, puis re-serrer de 2 à 3 N.m supplémentaires. Si la fuite
    persiste, déposer et remplacer le joint. - Lecture OBD de la température d''huile après 5 minutes de chauffe : connecter
    un scanner OBD et surveiller la valeur de température d''huile en temps réel. Après 5 minutes de fonctionnement au ralenti,
    la valeur doit être comprise entre 40°C et 60°C selon la température extérieure. Une valeur bloquée à la température ambiante
    indique un mauvais contact au niveau du connecteur. Une valeur immédiatement à 100°C ou plus indique un court- circuit
    interne au capteur. - Vérification du voyant huile éteint et absence de voyant moteur : après un cycle de chauffe complet
    (température stabilisée entre 80°C et 110°C), tous les voyants de contrôle du circuit d''huile doivent être éteints. La
    présence d''un voyant moteur allumé avec un code P019x actif après remplacement indique une incompatibilité de courbe
    NTC entre le capteur monté et l''application, ou un problème résiduel de câblage. - Absence de code défaut après cycle
    de conduite : effectuer un trajet de 10 à 15 minutes incluant phases de montée en régime. Un code défaut intermittent
    sur le circuit de température d''huile qui réapparaît après effacement indique soit un connecteur mal verrouillé (vibrations),
    soit un capteur dont la courbe NTC dérive légèrement de la valeur attendue. Dans ce cas, mesurer la résistance du capteur
    à chaud et la comparer aux valeurs de référence constructeur. - Test cohérence température huile / température liquide
    de refroidissement : à moteur stabilisé en conduite, la température d''huile moteur est généralement 5 à 20°C supérieure
    à la température du liquide de refroidissement. Un écart inférieur à 5°C ou supérieur à 30°C entre les deux valeurs suggère
    une mesure erronée du capteur d''huile (courbe NTC incompatible) ou un problème sur l''échangeur huile/eau (thermostat
    d''huile bloqué sur les moteurs qui en disposent).'
  S7: 'Le capteur de température d''huile surveille l''état thermique du lubrifiant moteur et interagit avec plusieurs composants
    du circuit de lubrification. Lors d''une intervention, contrôler ces pièces associées permet de valider que la défaillance
    est bien isolée au capteur et d''éviter une seconde intervention rapprochée : - Capteur de pression d''huile (pressostat
    d''huile) — implanté à proximité immédiate sur la quasi-totalité des architectures moteurs. Mesure la pression hydraulique
    du lubrifiant en complément de la température. Les deux capteurs assurent ensemble la supervision complète du circuit
    de lubrification. Un remplacement du capteur de température est l''occasion de contrôler le pressostat (état du joint,
    absence de fuite, résistance électrique conforme). Sur les moteurs diesel modernes, un capteur combiné pression/température
    regroupe les deux fonctions en un seul boîtier — s''assurer que la référence commandée correspond bien à la version combinée
    si c''est le cas. - Joint de carter d''huile — à contrôler visuellement lors de la dépose du capteur. Si des traces d''huile
    anciennes (dépôts carbonisés noirs) sont visibles sur le carter ou sur les boulons de fixation, le joint de carter est
    en fin de vie. Le remplacer lors de la même intervention permet de profiter de la vidange partielle déjà effectuée et
    d''éviter un nouveau rendez-vous atelier. - Filtre à huile — à remplacer lors de la même vidange si l''intervalle constructeur
    est atteint ou dépassé. Un filtre colmaté réduit le débit d''huile dans le circuit, ce qui augmente la température du
    lubrifiant à débit réduit et génère des valeurs thermiques anormalement élevées que le nouveau capteur restitue fidèlement
    — sans que cela soit un défaut capteur. - Thermostat d''huile — présent sur les moteurs avec échangeur thermique huile/eau
    (fréquent sur les moteurs diesel récents et certains moteurs essence suralimentés). Un thermostat d''huile bloqué en position
    fermée empêche la régulation thermique du lubrifiant et peut provoquer une surchauffe lente et progressive du circuit.
    Un thermostat bloqué en position ouverte maintient l''huile froide trop longtemps, dégradant la lubrification en phase
    de démarrage. - Câblage moteur — connecteur du capteur — à inspecter sur les véhicules de plus de 10 ans ou avec historique
    d''exposition à l''humidité. La corrosion des broches du connecteur génère une résistance de contact parasite qui s''ajoute
    à la résistance du capteur. Le calculateur interprète cette résistance additionnelle comme une température plus basse
    que réelle. Un nettoyage des broches avec un spray contact ou un remplacement du connecteur résout le problème sans remplacer
    le capteur lui-même. - Calculateur moteur (ECU) — à suspecter uniquement en dernier recours, après vérification complète
    du capteur, du connecteur et du câblage. Un calculateur avec défaut interne sur le canal de lecture de la température
    d''huile génère des codes P019x même avec un capteur et un câblage parfaitement conformes. Ce diagnostic doit être réalisé
    par un technicien spécialisé avec un outil de diagnostic constructeur.'
  S8: 'Le voyant de température d''huile s''allume mais le niveau est normal : est-ce le capteur ? Un voyant allumé avec un
    niveau d''huile correct est un signe typique d''un capteur défaillant ou d''un circuit ouvert. Effectuer d''abord une
    lecture OBD (codes P0195 à P0199). Vérifier la résistance du capteur avec un multimètre : à 20°C, un capteur NTC sain
    présente entre 2 000 et 4 000 ohms. Une résistance infinie (circuit ouvert) ou nulle (court-circuit) confirme le défaut
    capteur. Contrôler aussi le connecteur : une broche oxydée génère le même code qu''un capteur HS. Écarter le câblage avant
    de conclure au remplacement. Peut-on rouler avec un capteur de température d''huile défaillant ? Le véhicule reste opérationnel
    à court terme. Cependant, sans signal valide, le calculateur adopte une stratégie dégradée : injection enrichie persistante,
    régimes bridés, ventilation forcée. Ces adaptations augmentent la consommation et encrassent les injecteurs. À moyen terme,
    l''absence de surveillance thermique du lubrifiant expose le moteur à une surchauffe silencieuse lors de conduite en charge
    soutenue. Le remplacement doit intervenir dans les plus brefs délais. Comment distinguer le capteur de température d''huile
    du capteur de pression d''huile ? Les deux capteurs sont souvent voisins sur le bloc moteur. Le capteur de température
    mesure la chaleur via une résistance variable (NTC) — 2 broches, résistance mesurable de quelques centaines à quelques
    milliers d''ohms. Le capteur de pression (pressostat) mesure la force exercée par l''huile — 1 ou 2 broches, comportement
    binaire (ouverture/fermeture). Un test multimètre permet de distinguer les deux. Se référer également au schéma d''implantation
    constructeur avant dépose. Le remplacement du capteur efface-t-il les codes défauts ? Non. Les codes DTC mémorisés restent
    dans le calculateur jusqu''à effacement explicite via scanner OBD. Certaines gestions moteur effacent automatiquement
    les codes après 40 à 80 cycles de conduite sans récurrence. Pour éviter d''attendre, effacer manuellement les DTC après
    confirmation du bon fonctionnement du capteur neuf lors d''un cycle de chauffe complet. Le voyant moteur s''éteint immédiatement
    si aucune nouvelle anomalie n''est détectée. Peut-on utiliser un capteur universel sans référence constructeur ? Non pour
    cette application. Le calculateur est calibré pour une courbe NTC précise, propre à chaque motorisation. Un capteur universel
    avec une courbe différente affiche des valeurs vraisemblables mais erronées de 10 à 20°C sans générer de code défaut.
    Cette erreur systématique fausse les stratégies d''injection, de ventilation et les seuils d''alerte thermique sur toute
    la durée d''utilisation. Pour un composant de supervision de lubrification, la conformité de la courbe NTC est une exigence
    non négociable.'
---

# Capteur temperature d'huile - Guide Diagnostic

## Fonction et Role

Mesurer la temperature de l'huile moteur pour adapter la lubrification.

## Symptomes de Defaillance

- Indication temperature incorrecte
- Voyant huile allume sans raison
- Surconsommation de carburant

## Pieces Associees

- capteur-pression-d-huile
- carter-d-huile
- filtre-a-huile
- radiateur-d-huile

## FAQ

**Comment tester le capteur temperature d'huile ?**
Mesurer la resistance a froid et a chaud avec un multimetre. La valeur doit correspondre a la courbe constructeur (NTC generalement).

**Capteur OE ou adaptable ?**
Privilegier OE pour la precision de la courbe de resistance. Un capteur imprecis fausse la gestion moteur.

**Peut-on rouler avec un capteur defaillant ?**
Oui mais le calculateur n'aura pas l'information correcte, ce qui peut affecter la lubrification et la consommation.

**Ne pas confondre avec le capteur pression d'huile ?**
Ce sont deux capteurs distincts. Le capteur temperature est une thermistance, le capteur pression est un manocontact.

**Quelle erreur eviter ?**
Ne pas serrer excessivement (filetage delicat). Appliquer du teflon sur le filetage si specifie par le constructeur.

## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Pas de periodicite. Verifier en cas d'indication anormale au tableau de bord.
