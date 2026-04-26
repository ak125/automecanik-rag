---
category: eclairage
slug: ampoule-feu-arriere
title: Ampoule feu arrière
pg_id: 115
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
  role: Produit la lumière pour signaler la présence du véhicule à l'arrière
  must_be_true:
  - produire
  - emettre
  - signaler
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
    pour confirmer Ampoule feu arrière.
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
  - tier: Équivalent OE / équipementier éclairage reconnu
  - tier: Ampoule LED compatible feu arrière
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
    label: Feu arriere eteint
    severity: confort
  - id: S2
    label: Clignotant rapide si combine
    severity: confort
  - id: S3
    label: Refus au controle technique
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'Usure ou defaillance causant : feu arriere eteint'
  - 'Usure ou defaillance causant : clignotant rapide si combine'
  quick_checks:
  - 'Observer : feu arriere eteint ?'
  - 'Observer : clignotant rapide si combine ?'
  - 'Observer : refus au controle technique ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Feu arriere eteint
  - Clignotant rapide si combine
  - Refus au controle technique
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '115'
  intro_title: A quoi sert Ampoule feu arrière ?
  risk_title: Pourquoi remplacer Ampoule feu arrière a temps ?
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
  - question: Comment choisir Ampoule feu arrière compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Ampoule feu arrière ?
    answer: En cas de feu arriere eteint ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Ampoule feu arrière sans verification atelier ?
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
doc_id: a3082e5b-3035-5a08-9898-50f873e31460
content_hash: sha256:932f86fe39132057
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
  - type: 'plein'
    source_ref: corpus RAG web OEM
  - type: 'pneumatique'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_000_v: '000 v'
    val_15_a: '15 a'
    val_21_a: '21 a'
    val_3__: '3 %'
    val_30__: '30 %'
    val_45__: '45 %'
    val_8_v: '8 v'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'L''ampoule de feu arrière est le composant lumineux placé dans les blocs optiques arrière du véhicule. Sa fonction
    principale est de signaler la présence du véhicule aux autres usagers de la route, que ce soit le jour ou la nuit. Elle
    remplit plusieurs rôles distincts selon la fonction de l''optique dans laquelle elle est installée : feu de position arrière
    (feu de gabarit), feu de stop (freinage), feu de recul (marche arrière) ou feu de brouillard arrière.Le feu de position
    arrière émet en continu lorsque les feux de stationnement ou de croisement sont activés. Il avertit les véhicules suiveurs
    de la présence du véhicule, particulièrement dans des conditions de faible visibilité. Le feu de stop, lui, émet une lumière
    de forte intensité lors de l''appui sur la pédale de frein — il est alimenté via le circuit de freinage et son fonctionnement
    est contrôlé par l''interrupteur des feux de freins. Le feu de recul, blanc, s''allume en marche arrière pour signaler
    la manoeuvre et éclairer derrière le véhicule.Techniquement, ces ampoules sont des ampoules 12 V à culot standard : BA15S
    (simple contact) pour les feux de position, BAY15D ou P21/5W (double contact, double filament) pour les feux combinés
    stop/position, P21W pour les feux de stop et de recul. Le passage aux technologies LED est courant sur les véhicules récents,
    où les ampoules sont remplacées par des modules LED intégrés dans l''optique.Les pièces à vérifier simultanément lors
    d''une intervention sur le feu arrière sont l''ampoule de feu avant, l''ampoule de clignotant, l''ampoule de feu de position
    et l''interrupteur des feux de freins.'
  S2: 'Une ampoule de feu arrière défaillante expose le conducteur à une amende forfaitaire lors d''un contrôle routier et
    à un refus de contrôle technique. La plupart des défaillances sont immédiates (filament cassé), mais certains signes précurseurs
    permettent de les anticiper. Voici les symptômes caractéristiques à identifier :- Feu arrière éteint : le bloc optique
    arrière ne s''allume plus lorsque les feux sont activés. Ce symptôme est facilement visible depuis l''extérieur du véhicule
    — demandez à quelqu''un de vérifier derrière pendant que vous actionnez les différentes commandes d''éclairage.- Clignotant
    en hyperfrequence lorsqu''une ampoule est combinée : sur les véhicules où le clignotant et le feu de stop partagent une
    même ampoule double filament (ex. P21/5W), la grille d''un filament modifie la résistance électrique du circuit et provoque
    un clignotement accéléré (hyperfrequence) perceptible au tableau de bord via le voyant de clignotant.- Refus au contrôle
    technique : un feu arrière défaillant est un motif de contre-visite obligatoire. Si votre véhicule revient du contrôle
    technique avec une mention défaillance feux arrière, vérifiez chacune des fonctions du bloc optique arrière (position,
    stop, recul, brouillard).- Voyant tableau de bord allumé : les véhicules modernes (à partir d''environ 2010) disposent
    d''un contrôle des feux extérieurs via le bus CAN. Un voyant en forme d''ampoule avec un point d''exclamation peut s''allumer
    pour signaler une ampoule défaillante à l''arrière.- Éclairage dissymétrique à l''arrière : observé de l''extérieur, un
    côté du bloc optique arrière est moins lumineux ou présente une zone éteinte alors que l''autre côté fonctionne normalement.'
  S3: 'Le choix d''une ampoule de feu arrière dépend de la fonction de l''ampoule dans le bloc optique et de la technologie
    d''origine du véhicule. Une erreur de culot ou de technologie rend l''ampoule incompatible ou peut endommager l''optique.
    Voici les critères à respecter pour commander la bonne pièce :- Marque, modèle et année de mise en circulation : ces trois
    paramètres définissent la référence exacte de l''ampoule. Même sur un modèle identique, la référence peut changer selon
    l''année de production et la finition (blocs optiques facelift vs pré-facelift).- Identifier la fonction précise de l''ampoule
    : distinguez le feu de position arrière (allumé en permanence quand les feux sont activés), le feu de stop (allumé lors
    du freinage), le feu de recul (blanc, marche arrière) et le feu de brouillard arrière (rouge intense). Chaque fonction
    utilise une ampoule aux caractéristiques différentes.- Type de culot : les culots les plus courants pour les feux arrière
    sont BA15S (monofilament, simple contact), BAY15D / P21/5W (bifilament, double contact) et P21W. Le culot est identifiable
    sur l''ampoule d''origine ou dans le manuel du propriétaire.- Technologie (incandescence, halogène, LED) : si le bloc
    optique d''origine utilise des LED intégrées (module LED non remplaçable), il faut remplacer le module complet ou l''optique
    entière. Si l''ampoule est de type conventionnel, le remplacement LED plug-and-play est possible sous réserve de vérifier
    la compatibilité avec le contrôleur du véhicule.- Conformité réglementaire : les feux de stop et de position doivent être
    homologués R65 (stop) et R7 (position). Pour les LED, vérifiez la présence du marquage d''homologation sur l''emballage
    — une LED non homologuée peut entraîner un refus au contrôle technique.- Remplacement par paires : remplacez les ampoules
    de même fonction côté gauche et côté droit simultanément pour garantir une luminosité uniforme et éviter une nouvelle
    intervention rapide.Pour aller plus loin : consultez notre guide d''achat ampoule feu arrière — comparatif marques, critères
    de choix et prix.'
  S4_DEPOSE: 'L''accès aux ampoules des feux arrière varie considérablement d''un véhicule à l''autre. Sur la majorité des
    berlines et breaks, l''accès se fait depuis le coffre (intérieur) en retirant un cache en plastique. Sur les véhicules
    à hayon, l''accès peut nécessiter le démontage du bloc optique entier depuis l''extérieur. Voici la procédure générale
    :- Coupez le contact et attendez 2 minutes : laissez refroidir les ampoules halogènes de stop avant de les toucher, notamment
    si elles ont été allumées récemment. Un contact avec une ampoule chaude provoque une brûlure.- Identifiez le mode d''accès
    au bloc optique arrière : ouvrez le coffre et cherchez la trappe d''accès aux ampoules (souvent un cache oval ou rectangulaire
    en plastique, fixé par un quart de tour ou des clips). Sur certains véhicules, l''ensemble du bloc optique se dépose depuis
    l''extérieur après retrait de vis accessibles dans le coffre ou sous la carrosserie.- Retirez la trappe d''accès : tournez
    le quart de tour ou déclipsez la trappe. Le porte-ampoule est maintenant accessible — c''est un support plastique avec
    plusieurs douilles de culots.- Identifiez l''ampoule défaillante : avant de démonter quoi que ce soit, activez les différentes
    fonctions (feux de position, freinage, marche arrière) depuis l''intérieur pour confirmer quelle ampoule est hors service.-
    Déverrouillez le porte-ampoule : selon le design, le porte-ampoule se déverrouille par une rotation d''un quart de tour
    dans le sens antihoraire ou par un dégagement de clips latéraux. Tirez-le vers vous une fois déverrouillé.- Retirez l''ampoule
    défaillante : pour une ampoule à baïonnette, appuyez légèrement, tournez d''un quart de tour dans le sens antihoraire
    et tirez. Pour une ampoule à ergots (P21/5W), tirez directement en veillant à ne pas la tordre.- Installez la nouvelle
    ampoule : pour les ampoules halogènes, évitez tout contact du verre avec les doigts nus. Insérez la nouvelle ampoule,
    appuyez et tournez dans le sens horaire jusqu''au blocage.- Testez avant de remonter la trappe : avec le porte- ampoule
    en place mais la trappe ouverte, activez chaque fonction lumineuse pour confirmer le fonctionnement avant de tout refermer.-
    Remontez la trappe et le cache : repositionnez la trappe, effectuez le quart de tour de fermeture ou réenclenchez les
    clips. Vérifiez l''étanchéité — une trappe mal fermée laisse entrer l''humidité dans l''optique.'
  S4_REPOSE: 'La repose d''une ampoule de feu arrière prolonge la procédure de dépose en quelques étapes précises. L''enjeu
    principal est de s''assurer que l''ampoule est correctement engagée dans sa douille et que le bloc optique est étanche
    à l''humidité — une fuite d''eau dans un feu arrière accélère la corrosion des contacts et provoque des pannes récurrentes.
    - Vérifier le type et la puissance de la nouvelle ampoule : comparez l''ampoule neuve à l''ancienne : même culot (P21W,
    P21/5W, P27/7W, W16W selon la fonction du feu), même puissance. Pour les feux combinant plusieurs fonctions (stop + recul,
    stop + position), l''ampoule double filament P21/5W est la plus fréquente. Un culot mal adapté empêche la mise en place
    ou provoque une mauvaise connexion électrique. - Insérer l''ampoule à baïonnette correctement : la plupart des ampoules
    de feux arrière utilisent un culot à baïonnette (deux ergots latéraux). Pour les insérer : enfoncez l''ampoule dans la
    douille, tournez d''un quart de tour dans le sens des aiguilles d''une montre jusqu''au déclic. Ne forcez pas — si l''ampoule
    résiste, c''est qu''elle est mal alignée. Recommencez l''insertion en partant de zéro. - Contrôler l''étanchéité du joint
    de bloc optique : si vous avez déposé le bloc optique entier, remplacez le joint périmétrique s''il est aplati, fissuré
    ou manquant. Un bloc optique non étanche laisse entrer l''humidité, condense sur l''optique et corrode les contacts en
    quelques mois. Ce joint coûte peu et s''emboîte simplement dans sa gorge. - Tester l''ampoule avant de refermer : avant
    de reposer le cache d''accès ou de reviser le bloc optique, reconnectez le faisceau électrique temporairement et faites
    un test : demandez à un tiers d''actionner les feux de position, les stops et les clignotants. Vérifiez que chaque fonction
    s''allume correctement. Cette vérification à découvert est infiniment plus simple qu''un test après remontage complet.
    - Reposer le cache d''accès ou le bloc optique : pour les accès par le coffre, remettez le cache plastique en place en
    engageant d''abord les ergots côté charnière, puis en pressant côté clip. Pour les blocs optiques déposés depuis l''extérieur,
    réengagez d''abord les deux broches de positionnement dans leurs trous de caisse, puis serrez les vis ou écrous aux couples
    d''origine (généralement 5 à 8 N·m pour les vis de plastique sur carrosserie). - Vérifier le câblage et reconnecteur :
    rebranchez le connecteur de faisceau en vous assurant qu''il s''encliquète parfaitement. Un connecteur mal engagé peut
    fonctionner par intermittence et déclencher un message d''anomalie feux au tableau de bord. Sur certains véhicules récents,
    le calculateur BCM (Body Control Module) surveille la consommation de chaque feu et signale toute anomalie. - Effectuer
    le test final de conformité : avec un aide ou en vous déplaçant autour du véhicule, vérifiez successivement : feux de
    position allumés (feu arrière à puissance réduite), freinage (feux stop), clignotant droit et gauche. Pour les feux combinés,
    chaque fonction doit s''activer sans interférence avec les autres.'
  S5: 'Plusieurs erreurs fréquentes compliquent le remplacement des ampoules de feux arrière ou génèrent des pannes récurrentes.
    Voici les principales à éviter :- Confondre les fonctions des ampoules dans le bloc optique : un bloc optique arrière
    contient plusieurs ampoules de types différents (position, stop, recul, brouillard). Retirer et tester la mauvaise ampoule
    fait perdre du temps et peut conduire à commander la mauvaise pièce. Identifiez toujours la fonction défaillante avant
    tout démontage en testant chaque commande séparément.- Toucher l''ampoule halogène à mains nues : les traces de graisse
    des doigts créent des points de surchauffe qui fissurent l''enveloppe en verre et réduisent la durée de vie de quelques
    mois à quelques jours. Utilisez systématiquement un chiffon propre ou les gants fournis dans l''emballage de la pièce.-
    Ne remplacer qu''un côté : les ampoules du même type (gauche et droite) ont la même durée de vie. Si une ampoule de feu
    de stop a grillé d''un côté, l''ampoule du côté opposé est en fin de vie. Remplacez les deux pour éviter une deuxième
    intervention dans les semaines suivantes.- Forcer le porte-ampoule sans connaître la direction de déverrouillage : certains
    porte-ampoules se déverrouillent en tirant, d''autres en tournant. Forcer dans le mauvais sens casse le mécanisme de verrouillage
    et peut nécessiter le remplacement du bloc optique entier.- Ignorer un clignotant en hyperfrequence après remplacement
    : si le clignotant bat trop vite après remplacement d''une ampoule double filament par une LED, c''est que le relais de
    clignotant n''est pas adapté aux LED. Remplacez le relais de clignotant par un relais compatible LED ou installez une
    résistance d''équilibrage.'
  S6: 'Après remplacement d''une ampoule de feu arrière, les vérifications suivantes garantissent la conformité de l''installation
    et la sécurité du véhicule sur la route :- Test des trois fonctions principales depuis l''extérieur du véhicule : avec
    l''aide d''une seconde personne ou en utilisant un miroir, vérifiez successivement l''allumage du feu de position (feux
    allumés), le feu de stop (appui sur la pédale de frein) et le feu de recul (passage en marche arrière). Toutes les zones
    du bloc optique concernées doivent s''allumer uniformément.- Contrôle de l''hyperfrequence des clignotants : activez le
    clignotant du côté intervenu et comptez la fréquence de clignotement. Elle doit correspondre à l''autre côté (environ
    60 à 120 éclairs par minute). Un clignotement plus rapide signale un problème d''impédance lié à l''ampoule ou au relais.-
    Vérification de l''étanchéité de la trappe d''accès : assurez-vous que la trappe d''accès aux ampoules est correctement
    refermée et verrouillée. Une trappe mal ajustée laisse pénétrer l''humidité dans le bloc optique, ce qui entraîne des
    condensations et une dégradation prématurée des ampoules et des contacts.- Extinction du voyant tableau de bord : sur
    les véhicules équipés d''un contrôle électronique des feux, vérifiez que le voyant d''alerte ampoule (picto ampoule avec
    point d''exclamation) s''est éteint après le démarrage et quelques secondes de fonctionnement.'
  S7: 'Lors du remplacement d''une ampoule de feu arrière, plusieurs éléments complémentaires méritent une inspection simultanée.
    Les feux arrière concentrent plusieurs fonctions (stop, position, clignotant, recul, brouillard) et leurs composants vieillissent
    ensemble — une panne isolée annonce souvent la fatigue prochaine des éléments adjacents. - Ampoule feu avant (côté opposé)
    : les ampoules d''éclairage vieillissent à des rythmes similaires. Lorsqu''une ampoule arrière grille, l''ampoule symétrique
    du côté opposé est souvent en fin de vie. Remplacer les ampoules par paire garantit un éclairage homogène et évite un
    second arrêt à court terme. - Ampoule feu clignotant arrière : le clignotant arrière partage souvent le même bloc optique
    que le feu arrière. Un remplacement de l''un sans vérifier l''autre laisse une ampoule fatiguée en place. Contrôlez systématiquement
    le clignotant arrière lors de l''accès au bloc optique. - Ampoule feu de position : dans les feux combinés (fréquents
    sur les feux arrière), l''ampoule double filament assure à la fois la fonction stop (filament fort) et position (filament
    faible). Si seule la fonction stop fonctionne mais pas la position (ou inversement), c''est le filament interne qui est
    claqué — remplacez l''ampoule complète. - Interrupteur des feux de freins (contacteur de stop) : si les deux feux stop
    sont simultanément défaillants après remplacement des ampoules, le contacteur de stop (situé sur la pédale de frein) est
    la cause la plus probable. Ce contacteur signale au calculateur que la pédale est enfoncée — un contacteur HS laisse les
    feux stop constamment éteints ou constamment allumés. - Douilles et supports d''ampoule : les douilles de feux arrière
    s''oxydent progressivement, notamment dans les zones exposées aux projections de boue. Des douilles oxydées créent un
    mauvais contact électrique qui fait griller les ampoules prématurément. Inspectez l''état des contacts cuivrés dans chaque
    douille — un contact noirci ou vert-de-grisé se nettoie avec du papier de verre fin ou se remplace. - Faisceau électrique
    arrière et connecteurs : sur les breaks et les hayon, le faisceau arrière passe par une gaine souple entre le plancher
    et le coffre. Ce faisceau supporte des flexions répétées à chaque ouverture et peut se rompre intérieurement à long terme.
    En cas de coupure intermittente des feux arrière, inspectez ce point de passage avant de remplacer d''autres composants.'
  S8: 'Comment savoir quelle ampoule du bloc optique arrière est défaillante ?Avec l''aide d''une seconde personne, activez
    successivement chaque commande lumineuse depuis le poste de conduite : feux de position (ou feux de stationnement), freinage
    (pied sur le frein), marche arrière (sélecteur en position R) et antibrouillard arrière (bouton dédié). La zone éteinte
    ou moins lumineuse dans le bloc optique identifie l''ampoule défaillante. Si vous êtes seul, posez le véhicule face à
    un mur blanc ou un rideau sombre pour observer le reflet des feux lors de chaque activation.Mon clignotant clignote trop
    vite depuis que j''ai remplacé une ampoule — pourquoi ?Ce phénomène d''hyperfrequence (ou hyperflash) est lié à la résistance
    électrique de l''ampoule dans le circuit de clignotant. Le relais de clignotant mesure la consommation du circuit pour
    déterminer si une ampoule est défaillante : une résistance trop élevée (filament grillé) ou trop faible (LED basse consommation)
    déclenche l''hyperfrequence. Si vous avez remplacé une ampoule à incandescence par une LED, installez une résistance d''équilibrage
    de 6 à 8 ohms en parallèle sur le circuit, ou remplacez le relais de clignotant par un relais spécifique LED.Peut-on conduire
    avec un feu arrière éteint ?Non. Un feu arrière éteint (feu de position ou feu de stop) expose le conducteur à une verbalisation
    immédiate lors d''un contrôle routier, et surtout à un risque d''accident par l''arrière en conditions de faible visibilité.
    Le remplacement est simple, rapide et peu coûteux — il doit être effectué dès la détection du défaut, sans attendre.Faut-il
    déposer tout le bloc optique pour changer une ampoule arrière ?Dans la majorité des cas, non. L''accès se fait depuis
    le coffre en retirant une trappe en plastique sur le bloc optique, sans déposer l''ensemble du feu. Cependant, sur certains
    véhicules (notamment des berlines à hayon ou des monospaces), le bloc optique doit être entièrement déposé — il est maintenu
    par 2 ou 3 vis accessibles dans le coffre, et se retire en tirant latéralement après extraction des vis. Consultez le
    forum dédié à votre modèle pour confirmer la procédure exacte.'
---

# Ampoule feu arrière - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière pour signaler la présence du véhicule à l'arrière

**Actions principales:** produire, emettre, signaler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- feu arriere eteint
- clignotant rapide si combine
- refus au controle technique

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule feu arrière:

1. **Inspection visuelle** - Examiner l'état du ampoule feu arrière
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

- ampoule-feu-avant
- ampoule-feu-clignotant
- ampoule-feu-de-position
- interrupteur-des-feux-de-freins

## Critères de Compatibilité

Pour commander le bon ampoule feu arrière, vous devez connaître:

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

**Comment choisir Ampoule feu arrière compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Ampoule feu arrière ?**
En cas de feu arriere eteint ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Ampoule feu arrière sans verification atelier ?**
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
