---
category: eclairage
slug: ampoule-feu-clignotant
title: Ampoule feu clignotant
pg_id: 105
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
  role: Produit la lumière intermittente pour signaler les changements de direction
  must_be_true:
  - produire
  - emettre
  - clignoter
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
    min: 30
    max: 200
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
  - tier: Équivalent OE / équipementier éclairage reconnu
  - tier: Ampoule LED clignotant compatible
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
    label: Clignotant qui clignote vite hyperfrequence
    severity: confort
  - id: S2
    label: Clignotant inactif d un cote
    severity: confort
  - id: S3
    label: Voyant tableau bord clignote anormalement
    severity: confort
  causes:
  - lecture codes defaut obd et diagnostic electronique
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  - 'Usure ou defaillance causant : clignotant qui clignote vite hyperfrequence'
  quick_checks:
  - 'Observer : clignotant qui clignote vite hyperfrequence ?'
  - 'Observer : clignotant inactif d un cote ?'
  - Voyant tableau bord clignote anormalement ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Clignotant qui clignote vite hyperfrequence
  - Clignotant inactif d un cote
  - Voyant tableau bord clignote anormalement
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '105'
  intro_title: A quoi sert Ampoule feu clignotant ?
  risk_title: Pourquoi remplacer Ampoule feu clignotant a temps ?
  risk_explanation: '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
  risk_consequences:
  - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
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
  - question: Comment choisir Ampoule feu clignotant compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Ampoule feu clignotant ?
    answer: En cas de clignotant qui clignote vite hyperfrequence ou de degradation mesurable, il faut controler rapidement
      avant panne secondaire.
  - question: Puis-je monter Ampoule feu clignotant sans verification atelier ?
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
doc_id: 91b376ba-55a5-594e-9c4c-4ba2c46171a2
content_hash: sha256:23b4f41fae040041
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
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    L'ampoule de feu clignotant est le composant lumineux qui produit la lumière
    intermittente utilisée pour signaler les changements de direction du
    véhicule aux autres usagers de la route. Elle est présente à l'avant (dans
    le bloc optique avant ou en position latérale sur le rétroviseur extérieur),
    à l'arrière (dans le bloc optique arrière) et parfois sur les côtés du
    véhicule (clignotants latéraux de répétition).Le fonctionnement du
    clignotant repose sur un relais électronique ou électromécanique qui
    interrompt et rétablit l'alimentation électrique à une fréquence régulière,
    comprise entre 60 et 120 impulsions par minute selon la norme ECE R6. Ce
    relais surveille également la résistance électrique du circuit : si une
    ampoule grille, la résistance totale du circuit change, et le relais
    interprète cette variation comme un défaut — il accélère alors la fréquence
    de clignotement (phénomène d'hyperfrequence) pour alerter le conducteur.Les
    ampoules de clignotant les plus courantes sont des ampoules à culot BA15S ou
    PY21W (ambre/orange), émettant une lumière de couleur orangée conforme à la
    réglementation. Sur les véhicules récents, les clignotants LED intégrés aux
    blocs optiques remplacent les ampoules conventionnelles — dans ce cas, la
    défaillance concerne le module LED ou sa carte de contrôle, et non une
    ampoule isolée.Les pièces associées à vérifier lors d'une intervention sur
    un clignotant défaillant sont l'ampoule feu arrière, l'ampoule feu avant et
    l'ampoule feu de position du même côté, ainsi que le relais de clignotant si
    l'hyperfrequence persiste après remplacement de l'ampoule.
  S2: >-
    Les défaillances des ampoules de clignotant sont facilement détectables
    depuis le poste de conduite grâce au voyant de clignotant au tableau de
    bord, dont le comportement change lorsqu'une ampoule est hors service. Voici
    les symptômes à identifier :- Clignotant en hyperfrequence (clignotement
    trop rapide) : c'est le signe le plus caractéristique d'une ampoule de
    clignotant grillée sur les systèmes à relais électromécanique. Le voyant de
    clignotant au tableau de bord clignote deux fois plus vite que la normale
    sur un des côtés. Ce phénomène est dû à la variation de résistance dans le
    circuit lorsqu'une ampoule est absente.- Clignotant inactif d'un côté :
    l'activation du clignotant (levier de direction) n'allume aucune ampoule
    d'un côté du véhicule. Le voyant au tableau de bord peut clignoter seul sans
    signal extérieur visible. Ce symptôme peut indiquer une ampoule grillée mais
    aussi un fusible défaillant ou un fil coupé.- Voyant tableau de bord qui
    clignote anormalement : sur les véhicules à gestion électronique des
    clignotants (module BSI ou BCM), un clignotement irrégulier ou continu du
    voyant de direction peut signaler une défaillance d'ampoule détectée par le
    calculateur, parfois accompagné d'un message d'alerte sur l'écran de bord.-
    Ampoule de clignotant restant allumée en fixe : dans de rares cas, un
    contact électrique permanent provoque l'allumage fixe du clignotant — la
    cause est alors un court-circuit dans le faisceau électrique ou un relais de
    clignotant défaillant, et non l'ampoule elle-même.- Clignotant visible d'un
    seul côté lors de la vérification extérieure : en demandant à quelqu'un de
    vérifier depuis l'extérieur pendant que vous activez le clignotant,
    l'absence d'une ampoule (avant, arrière ou latérale) sur un côté est
    immédiatement visible.
  S3: >-
    Le choix d'une ampoule de clignotant doit impérativement correspondre aux
    spécifications d'origine en termes de culot, de puissance et de couleur. Un
    mauvais choix peut générer un clignotement en hyperfrequence, un refus au
    contrôle technique ou une incompatibilité électronique avec le système de
    gestion des clignotants. Voici les critères à respecter :- Marque, modèle et
    année de mise en circulation : le catalogue pièces détachées filtre les
    ampoules compatibles sur ces données. Un même modèle de véhicule peut
    utiliser des références différentes selon l'année de production ou la
    finition (blocs optiques standard vs bi-xénon ou LED).- Type de culot : les
    culots les plus courants pour les clignotants sont BA15S (monofilament,
    simple contact), BAY15D (bifilament), PY21W (culot ambre-décalé, obligatoire
    sur les clignotants ambre pour éviter un montage dans le mauvais logement)
    et T20 / W21W. Le décalage du culot PY21W est une sécurité anti-confusion —
    une ampoule blanche W21W ne peut physiquement pas entrer dans un support
    PY21W.- Puissance nominale : les clignotants utilisent des ampoules de 21 W
    (feux avant et arrière) ou de 5 W (feux de répétition latéraux). Monter une
    ampoule de puissance inférieure modifie la résistance du circuit et génère
    un clignotement en hyperfrequence sur les systèmes à relais
    électromécanique.- Couleur amber/orange conforme : les ampoules de
    clignotant doivent émettre une lumière orangée (amber) ou la couleur est
    produite par le diffuseur orange du bloc optique (dans ce cas, l'ampoule est
    blanche à l'intérieur). Vérifiez la couleur d'origine avant de commander —
    monter une ampoule orange dans un logement à diffuseur clair produit une
    double teinte non conforme.- Compatibilité LED avec le relais de clignotant
    : si vous souhaitez passer aux LED sur les clignotants, vérifiez que le
    relais de clignotant d'origine est compatible LED. La très grande majorité
    des relais électromécaniques d'origine ne l'est pas et génèrera de
    l'hyperfrequence avec des LED basse consommation.- Remplacement par paires :
    remplacez les ampoules de clignotant avant et arrière du même côté
    simultanément pour maintenir la symétrie du circuit électrique et garantir
    un clignotement à la même fréquence des deux côtés.Pour aller plus loin :
    consultez notre guide d'achat ampoule feu clignotant — comparatif marques,
    critères de choix et prix.
  S4_DEPOSE: >-
    Le remplacement d'une ampoule de clignotant varie selon qu'il s'agit d'un
    clignotant avant, arrière ou latéral (répétiteur sur rétroviseur). La
    procédure est généralement accessible sans outillage spécialisé. Voici les
    étapes à suivre pour chaque cas :- Identifiez l'emplacement de l'ampoule
    défaillante : activez le clignotant depuis le poste de conduite et observez
    depuis l'extérieur du véhicule (avant, arrière, côtés) quelle ampoule ne
    clignote pas. Sur certains véhicules, le répétiteur latéral sur le
    rétroviseur est la seule ampoule défaillante — ne l'omettez pas dans votre
    inspection.- Coupez le contact : éteignez toutes les commandes électriques
    et retirez la clé du contact ou attendez que le système de veille soit
    inactif. Pour les clignotants, la mise hors tension est importante pour
    éviter tout arc électrique lors de la manipulation.- Pour un clignotant
    avant : ouvrez le capot et cherchez l'accès depuis l'arrière du bloc
    optique. Sur la plupart des véhicules, le porte-ampoule du clignotant se
    déverrouille par un quart de tour antihoraire (sens de la flèche gravée sur
    le support) et se tire vers l'arrière. Retirez l'ampoule à baïonnette (appui
    + quart de tour antihoraire).- Pour un clignotant arrière : ouvrez le coffre
    et accédez au porte-ampoule par la trappe de service en plastique à
    l'arrière du bloc optique. Déverrouillez le porte-ampoule d'un quart de tour
    et extrayez l'ampoule défaillante.- Pour un répétiteur latéral sur
    rétroviseur : le boîtier du répétiteur se déclipse généralement vers
    l'arrière ou se glisse vers l'avant — consultez la documentation de votre
    véhicule car la manipulation incorrecte peut casser les clips. L'ampoule
    interne est souvent de type baïonnette ou T10.- Installez la nouvelle
    ampoule : vérifiez que le culot de la nouvelle ampoule correspond exactement
    à l'original avant de l'insérer. Pour une ampoule à baïonnette, insérez en
    alignant les ergots avec les rainures du porte-ampoule, appuyez et tournez
    d'un quart de tour dans le sens horaire jusqu'au blocage.- Testez avant de
    refermer : avec le porte-ampoule en place mais le cache ouvert ou le
    répétiteur non reclipsé, activez le clignotant depuis l'intérieur du
    véhicule pour confirmer que la nouvelle ampoule s'allume et que la fréquence
    de clignotement est normale.- Remontez le cache ou clipsez le répétiteur :
    réenclenchez les éléments démontés et vérifiez l'absence de jeu. Refermez le
    coffre ou le capot selon le côté intervenu.
  S4_REPOSE: >-
    Le remontage d'une ampoule de clignotant s'effectue dans l'ordre inverse de
    la dépose. La procédure diffère selon que l'ampoule est montée en baïonnette
    (clignotant arrière classique), en clip plastique (répétiteur de
    rétroviseur) ou à pression dans un douille souple (clignotant avant intégré
    au bloc). La clé du succès est de ne jamais forcer : chaque ampoule dispose
    d'un détrompeur qui guide son insertion correcte. - Préparer la nouvelle
    ampoule : vérifiez le culot et le type avant d'engager (PY21W pour
    clignotant ambre standard, WY5W pour répétiteur). Ne touchez pas le verre
    avec les doigts — les dépôts de graisse créent un point chaud qui réduit la
    durée de vie. Utilisez un tissu propre ou des gants fins. - Engager
    l'ampoule dans la douille : pour les culots à baïonnette, alignez les ergots
    latéraux de l'ampoule avec les rainures de la douille, puis effectuez un
    quart de tour dans le sens horaire jusqu'au blocage. Pour les douilles à
    friction, poussez simplement jusqu'au fond du logement. - Vérifier l'ambre
    de l'ampoule : les clignotants nécessitent impérativement une ampoule de
    teinte ambre (orange). Une ampoule transparente dans un feu clignotant non
    teinté est interdite par le code de la route. Sur les blocs optiques à verre
    clair, l'ampoule elle-même doit être orange. - Remettre le porte-ampoule en
    place : réinsérez l'ensemble porte-ampoule dans le bloc feu. Vérifiez le
    sens (détrompeur ou encoche de positionnement) et effectuez un quart de tour
    pour verrouiller, ou clipsez selon le système. - Reconnecter le faisceau si
    déconnecté : certains clignotants arrière demandent de déconnecter le
    faisceau pour déposer le bloc. Réemboîtez le connecteur jusqu'au déclic et
    tirez légèrement pour confirmer le verrouillage. - Remise en place du cache
    ou du bloc : si le bloc feu a été démonté, revissez les écrous papillon ou
    les vis de fixation. Si un cache intérieur de coffre a été déposé,
    reclipsez-le en partant du centre vers les extrémités pour éviter les
    déformations. - Test de fonctionnement immédiat : activez le clignotant
    depuis le poste de conduite et observez depuis l'extérieur. Le clignotant
    doit flasher au rythme normal (environ 1 à 1,5 Hz). Une hyperfrequence
    (clignotement trop rapide) indique une ampoule défaillante, une ampoule de
    mauvaise puissance ou un problème de contact. - Vérification du voyant
    tableau de bord : sur les véhicules récents, un défaut de circuit clignotant
    peut allumer un voyant. Si le voyant persiste après le remplacement et le
    test fonctionnel, vérifiez la résistance de la prise — les ampoules LED
    peuvent nécessiter une résistance additionnelle pour éviter le défaut de
    circuit.
  S5: >-
    Plusieurs erreurs répétitives conduisent à un remplacement inefficace ou à
    une persistance du dysfonctionnement après intervention. Voici les cinq
    erreurs les plus fréquentes lors du remplacement d'une ampoule de clignotant
    :- Ne pas identifier toutes les ampoules de clignotant du côté défaillant :
    un côté du véhicule comporte généralement 2 à 3 ampoules de clignotant
    (avant, arrière, et répétiteur latéral sur rétroviseur). Remplacer
    uniquement l'ampoule avant sans vérifier les autres laisse le circuit en
    défaut partiel, ce qui peut maintenir l'hyperfrequence si la résistance
    totale du circuit reste modifiée.- Monter une ampoule de puissance
    incorrecte : une ampoule de 10 W à la place d'une ampoule de 21 W change la
    résistance du circuit et provoque un clignotement en hyperfrequence
    persistent. Vérifiez toujours la puissance nominale marquée sur l'ampoule
    d'origine ou dans le manuel du véhicule.- Confondre ampoule amber et ampoule
    blanche dans un logement clear : certains blocs optiques modernes ont un
    diffuseur transparent (clair) et utilisent des ampoules ambre PY21W pour
    produire la couleur orangée. Monter une ampoule blanche W21W dans ce
    logement produit une lumière blanche non conforme à la réglementation.
    L'ampoule PY21W a un culot décalé exprès pour éviter cette confusion — si
    l'ampoule blanche entre dans le support, c'est que le culot n'est pas le
    bon.- Ignorer l'hyperfrequence persistante après remplacement : si
    l'hyperfrequence persiste après le remplacement de l'ampoule, ne concluez
    pas que l'ampoule neuve est défaillante. Vérifiez le répétiteur latéral du
    même côté (souvent oublié) et, si le problème persiste, testez le relais de
    clignotant qui peut être défaillant indépendamment des ampoules.- Oublier de
    lire les codes défaut OBD sur les véhicules récents : les véhicules équipés
    d'un calculateur de gestion des clignotants (BSI, BCM) peuvent conserver un
    code défaut en mémoire même après remplacement de l'ampoule. Ce code
    mémorisé peut provoquer des alertes persistantes au tableau de bord. Effacez
    les codes défaut avec un scanner OBD2 après l'intervention pour valider le
    retour à la normale.
  S6: >-
    Après remplacement d'une ampoule de clignotant, les vérifications suivantes
    confirment que l'intervention est complète et que le circuit fonctionne à la
    bonne fréquence :- Contrôle de la fréquence de clignotement : activez le
    clignotant du côté intervenu et comptez les impulsions visuelles depuis
    l'extérieur. La fréquence doit être comprise entre 60 et 120 éclairs par
    minute (environ 1 clignotement par seconde), identique à l'autre côté du
    véhicule. Un clignotement plus rapide indique un problème persistant dans le
    circuit.- Vérification de toutes les ampoules de clignotant du même côté :
    observez simultanément le clignotant avant, le clignotant arrière et le
    répétiteur latéral (sur rétroviseur si présent) du même côté. Toutes doivent
    clignoter à la même fréquence et avec la même intensité lumineuse.- Contrôle
    du voyant de clignotant au tableau de bord : le voyant de direction (flèche
    verte) doit clignoter à la même fréquence que les feux extérieurs et avoir
    la même cadence des deux côtés. Un voyant en hyperfrequence d'un côté
    confirme un défaut résiduel dans le circuit.- Lecture des codes défaut OBD :
    sur les véhicules post-2010 avec gestion électronique des clignotants,
    connectez un scanner OBD2 et vérifiez l'absence de code défaut actif ou
    mémorisé lié au circuit de clignotant. Effacez les codes mémorisés si la
    réparation est confirmée.- Vérification lors d'un trajet de test : effectuez
    quelques kilomètres incluant des créneaux et des changements de voie pour
    confirmer que les clignotants répondent normalement à chaque sollicitation
    du levier de direction, y compris les clignotements automatiques "lane
    change" (simple pression du levier) si votre véhicule en est équipé.
  S7: >-
    Le remplacement d'un clignotant défaillant est l'occasion de contrôler
    d'autres composants du circuit de signalisation. Plusieurs pièces partagent
    le même circuit électrique ou le même emplacement physique et méritent un
    examen simultané pour éviter une deuxième intervention à court terme. -
    Ampoule clignotant côté opposé : les ampoules de clignotant droite et gauche
    s'usent au même rythme car elles fonctionnent alternativement. Remplacer les
    deux simultanément garantit une durée de vie homogène et supprime le risque
    de panne côté opposé dans les semaines suivantes. - Relais de clignotant (ou
    module de clignotant électronique) : le relais est le composant qui génère
    le battement du clignotant. S'il vieillit, le rythme devient irrégulier ou
    le clignotant reste fixe. Sur les véhicules modernes, cette fonction est
    gérée par un module électronique — un code défaut OBD peut pointer vers ce
    composant. - Répétiteur de clignotant sur rétroviseur : situé sur le
    rétroviseur extérieur, il partage le même circuit que le clignotant
    principal. Vérifiez son état lors de chaque intervention sur la
    signalisation latérale. Il peut être remplacé indépendamment ou avec le bloc
    rétroviseur selon le véhicule. - Contacteur de clignotant (levier de
    colonne) : si le clignotant grille fréquemment ou ne fonctionne
    qu'intermittemment malgré une ampoule neuve, le contacteur peut envoyer un
    signal défaillant. Un test rapide avec un multimètre entre les deux bornes
    du connecteur ampoule suffit à diagnostiquer. - Câblage et connecteur de feu
    : les connecteurs des clignotants sont exposés aux vibrations et aux écarts
    de température. Sur les véhicules de plus de 10 ans, inspectez les broches
    du connecteur (oxydation, brûlures, fissures du plastique). Un connecteur
    dégradé provoque le clignotement en hyperfrequence par augmentation de
    résistance. - Feu arrière complet : si l'ampoule de clignotant est logée
    dans un bloc feu arrière présentant une fissure ou un jaunissement prononcé,
    le bloc entier peut nécessiter un remplacement pour éviter tout problème
    lors du contrôle technique.
  S8: >-
    le rôle de le clignotant en hyperfrequence et comment le corriger
    ?L'hyperfrequence (ou hyperflash) est le clignotement anormalement rapide du
    voyant de direction et des feux de clignotant lorsqu'une ampoule du circuit
    est grillée ou absente. Le relais de clignotant électromécanique détecte la
    variation de résistance dans le circuit (résistance plus haute = filament
    absent) et interprète ce changement comme un défaut en accélérant la
    cadence. Pour corriger le problème, remplacez toutes les ampoules de
    clignotant défaillantes du côté concerné (avant, arrière, répétiteur
    latéral). Si l'hyperfrequence persiste après remplacement de toutes les
    ampoules, le relais de clignotant lui-même est probablement défaillant.Peut-
    on remplacer les ampoules de clignotant par des LED ?Oui, à condition
    d'adapter le relais de clignotant. Les ampoules LED consomment 3 à 5 fois
    moins qu'une ampoule à incandescence de 21 W — cette faible consommation est
    interprétée par le relais électromécanique d'origine comme une ampoule
    grillée, ce qui provoque l'hyperfrequence en permanence. La solution est de
    remplacer le relais de clignotant d'origine par un relais compatible LED
    (électronique, insensible à la résistance de charge) ou d'installer des
    résistances d'équilibrage de 6 à 8 ohms en parallèle sur chaque ampoule LED.
    Sur les véhicules récents avec gestion électronique, la compatibilité LED
    est à vérifier modèle par modèle.Mon clignotant clignote mais un voyant
    d'alerte reste allumé — que faire ?Un voyant d'alerte persistant après
    remplacement d'une ampoule de clignotant sur un véhicule avec gestion
    électronique (BSI, BCM) est souvent dû à un code défaut mémorisé dans le
    calculateur. Le calculateur a enregistré la défaillance et conserve l'alerte
    même après la réparation. Branchez un scanner OBD2 compatible avec votre
    marque de véhicule, lisez les codes défaut actifs et mémorisés, et effacez-
    les après avoir confirmé que l'ampoule fonctionne. Si le code revient
    immédiatement, un autre composant du circuit est défaillant (faisceau,
    connecteur, calculateur).Le répétiteur de clignotant sur rétroviseur est-il
    obligatoire au contrôle technique ?Oui. Le répétiteur latéral de clignotant
    est contrôlé lors de la visite technique — son absence ou sa défaillance
    peut constituer un motif de contre-visite selon l'équipement d'origine du
    véhicule. S'il était présent à l'origine sur votre véhicule, il doit être
    fonctionnel. Lors du remplacement d'une ampoule de clignotant, vérifiez donc
    systématiquement l'état du répétiteur latéral sur rétroviseur du même côté.
---

# Ampoule feu clignotant - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière intermittente pour signaler les changements de direction

**Actions principales:** produire, emettre, clignoter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- clignotant qui clignote vite hyperfrequence
- clignotant inactif d un cote
- voyant tableau bord clignote anormalement

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule feu clignotant:

1. **Inspection visuelle** - Examiner l'état du ampoule feu clignotant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-arriere
- ampoule-feu-avant
- ampoule-feu-de-position

## Critères de Compatibilité

Pour commander le bon ampoule feu clignotant, vous devez connaître:

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

**Comment choisir Ampoule feu clignotant compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Ampoule feu clignotant ?**
En cas de clignotant qui clignote vite hyperfrequence ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Ampoule feu clignotant sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
