---
category: accessoires
slug: pompe-nettoyage-des-phares
title: Pompe nettoyage des phares
pg_id: 795
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
  last_enriched_by: skill:phase5-hella-ngk
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Projette le liquide de nettoyage sur les optiques de phares
  must_be_true:
  - projeter
  - pulveriser
  - alimenter
  must_not_contain:
  - balai
  - essuie-glace
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
    min: 50
    max: 300
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE
  - tier: Adaptable
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
    label: Jets de phares inactifs
    severity: confort
  - id: S2
    label: Phares sales malgre l activation
    severity: confort
  - id: S3
    label: Bruit de pompe sans projection
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : jets de phares inactifs'
  quick_checks:
  - 'Observer : jets de phares inactifs ?'
  - 'Observer : phares sales malgre l activation ?'
  - Bruit de pompe sans projection ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Jets de phares inactifs
  - Phares sales malgre l activation
  - Bruit de pompe sans projection
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '795'
  intro_title: A quoi sert Pompe nettoyage des phares ?
  risk_title: Pourquoi remplacer Pompe nettoyage des phares a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: Comment choisir Pompe nettoyage des phares compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Pompe nettoyage des phares ?
    answer: En cas de jets de phares inactifs ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Pompe nettoyage des phares sans verification atelier ?
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
doc_id: 65433234-f0e5-572e-a8ec-3efa5bcd80a7
content_hash: sha256:a923fe88182cb046
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
  _source: HELLA TechWorld
  _validation_status: oem_verified
  _enriched_at: '2026-03-29'
  types_variants:
  - type: Gicleur telescopique
    description: Piston extensible, cycle ~0,8s
    era: standard
  - type: Gicleur fixe
    description: Stationnaire, cycle ~0,5s
    era: economique
  technical_notes:
    plage_temperature: '-10 a +35 degC'
    vitesse_max: '130 km/h'
    efficacite_nettoyage: '> 70% (reglementation CEE R45)'
    reserve_cycles: '25 ou 50 cycles selon classification'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    La pompe de nettoyage des phares est un composant hydraulique dont la
    mission est de projeter le liquide de nettoyage directement sur les optiques
    de phares pour en éliminer les salissures accumulées : insectes, boue, sel
    de dégivrage et pellicules graisseuses. Intégrée au circuit lave-glace ou
    dotée d'un réservoir dédié selon les modèles, elle fonctionne via un moteur
    électrique qui crée une dépression pour aspirer le liquide et le refouler
    sous pression vers des gicleurs orientables fixés sous les optiques ou dans
    les pare-chocs avant. Le déclenchement est automatique sur la plupart des
    véhicules modernes : la pompe s'active lorsque le conducteur utilise les
    essuie-glaces ou le lave-glace frontal, généralement après un délai de
    quelques cycles. Sur certaines motorisations diesel et sur les véhicules
    équipés de projecteurs xénon ou à LED, la réglementation impose ce
    dispositif, car ces optiques sont plus sensibles aux dépôts et plus
    coûteuses à endommager. Les actions techniques de la pièce se déclinent
    ainsi : pulvériser le liquide sous une pression adaptée pour décrocher les
    dépôts tenaces, alimenter les gicleurs de manière continue sans perte de
    charge, et projeter uniformément sur toute la surface de l'optique pour
    garantir une visibilité nocturne maximale. Un défaut de pompe se traduit
    directement par une dégradation de l'éclairage effectif, puisqu'un phare
    encrassé peut perdre jusqu'à 40 % de son flux lumineux.
  S2: >-
    Plusieurs signaux permettent de suspecter une défaillance de la pompe de
    nettoyage des phares avant d'en arriver à une panne totale. Intervenir dès
    les premiers signes évite de dégrader les optiques et de compromettre la
    visibilité nocturne. - Jets de phares totalement inactifs : aucun liquide ne
    sort des gicleurs malgré l'activation du système ; c'est le signe le plus
    direct d'une pompe défaillante ou d'une alimentation coupée. - Phares sales
    malgré l'activation répétée : le système se déclenche (bruit ou voyant
    actif) mais les optiques restent encrassées, indiquant une pression
    insuffisante ou des gicleurs bouchés en aval de la pompe. - Bruit de pompe
    sans projection visible : on entend le moteur électrique tourner mais aucun
    jet ne sort ; cela pointe vers une membrane interne usée, un clapet anti-
    retour défaillant ou une fuite de durite. - Pression de jet nettement
    réduite : les jets atteignent les optiques mais avec si peu de force qu'ils
    ne nettoient pas ; cause probable : usure des joints internes de la pompe. -
    Fuites de liquide sous le pare-chocs avant : des traces de liquide lave-
    glace sous le bouclier avant signalent une durite percée ou un raccord
    desserré côté pompe de phares. - Activation aléatoire ou intermittente : la
    pompe fonctionne une fois sur deux, souvent liée à une connexion électrique
    oxydée sur le connecteur de la pompe. - Consommation excessive de liquide
    lave-glace : si le réservoir se vide anormalement vite sans trace visible de
    jet, une fuite interne au circuit de nettoyage des phares est à envisager.
  S3: >-
    La pompe de nettoyage des phares est une pièce spécifique au modèle de
    véhicule. Une référence inadaptée peut entraîner une incompatibilité de
    connecteur, une pression insuffisante ou un montage impossible. Voici les
    critères à vérifier impérativement avant de commander. - Marque et modèle
    exact du véhicule : la référence constructeur varie non seulement selon la
    marque, mais aussi selon la version de carrosserie (berline, break, SUV) et
    le millésime de production. - Année de fabrication précise : un même modèle
    peut avoir reçu deux générations de système de nettoyage phares au cours de
    sa production ; l'année de mise en circulation est déterminante. - Type
    d'optiques installées : phares halogènes, xénon (bi-xénon) ou LED/matriciels
    n'utilisent pas forcément la même pompe ni la même pression de projection. -
    Vérifier les symptômes actifs : si les jets sont inactifs, contrôler d'abord
    si le fusible de la pompe est intact ; si la pompe fait du bruit sans
    projeter, la pièce est à remplacer ; si les jets sont faibles, vérifier
    aussi les gicleurs avant de remplacer la pompe. - Référence OEM ou
    équivalent certifié : privilégier une référence d'équipementier (Valeo,
    Hella, Bosch) ou la référence d'origine constructeur pour garantir la
    pression de sortie conforme aux spécifications du fabricant de phares. -
    Compatibilité du connecteur électrique : le nombre de broches et le type de
    verrouillage du connecteur doivent correspondre à l'existant ; une
    adaptation de connecteur fragilise la connexion dans un environnement
    humide. - Vérifier les pièces associées : lors du remplacement, inspecter
    également les gicleurs (susceptibles d'être bouchés ou cassés) et les
    durites de liaison pour éviter un second démontage rapide. Pour aller plus
    loin : consultez notre guide d'achat pompe nettoyage des phares — comparatif
    marques, critères de choix et prix.
  S4_DEPOSE: >-
    Le remplacement d'une pompe de nettoyage des phares nécessite généralement
    d'accéder au réservoir de liquide lave-glace, qui loge souvent la pompe en
    position immergée. La procédure varie selon les véhicules mais suit dans les
    grandes lignes les étapes ci-dessous. - Vider partiellement le réservoir :
    avant toute intervention, pomper ou vider suffisamment de liquide lave-glace
    pour que le niveau descende en dessous de la pompe ; évite les écoulements
    lors du démontage. - Débrancher la batterie : déconnecter le câble négatif
    de la batterie pour mettre le circuit électrique de la pompe hors tension
    avant de toucher au connecteur. - Localiser la pompe de phares : dans la
    plupart des véhicules, elle est vissée ou clipsée dans un puit latéral du
    réservoir lave-glace, distincte de la pompe principale du lave-glace avant.
    - Déconnecter le connecteur électrique : appuyer sur le clip de verrouillage
    et tirer le connecteur ; noter l'état des broches (oxydation = nettoyage
    avec spray contact). - Déconnecter les durites : noter la position des
    durites (parfois deux sorties sur une pompe double) ; obturer provisoirement
    les durites avec des bouchons pour éviter de vider le réservoir. - Extraire
    la pompe : selon la fixation (vissée, clipsée ou à baïonnette), dévisser ou
    appuyer sur les clips de rétention et tirer la pompe vers l'extérieur du
    réservoir ; changer le joint torique si la nouvelle pompe en est fournie. -
    Installer la nouvelle pompe : insérer la pompe neuve avec son joint,
    reconnecter les durites dans le bon ordre, puis rebrancher le connecteur
    électrique. - Remplir le réservoir et tester : remettre le niveau de liquide
    lave-glace, rebrancher la batterie et déclencher plusieurs cycles de
    nettoyage phares pour valider la pression et l'orientation des jets.
  S4_REPOSE: >-
    Après remplacement de la pompe de nettoyage des phares, le remontage doit
    garantir l'étanchéité du circuit hydraulique et la bonne orientation des
    gicleurs. Une installation incorrecte se traduit par des projections
    inefficaces ou des fuites de liquide dans le compartiment avant. -
    Positionnement de la pompe dans le réservoir ou le support — Selon le type
    de circuit, la pompe est soit immergée dans le réservoir de lave-glace (avec
    le gicleur phare intégré sur un second orifice), soit montée en ligne sur le
    circuit dédié. Respectez l'orientation prévue par les ergots de fixation. -
    Connexion de la durite de départ vers les gicleurs — Branchez la durite
    d'alimentation vers les gicleurs télescopiques des phares. Vérifiez qu'elle
    n'est pas vrillée ou pincée sous les pièces de carrosserie adjacentes. -
    Fixation de la pompe dans son support — Insérez la pompe dans son logement
    en caoutchouc (filtre et joint d'étanchéité inclus). Une pompe mal centrée
    vibre et décroche sa durite sous pression. - Reconnexion du connecteur
    électrique — Branchez le connecteur jusqu'au clic de verrouillage. La pompe
    de nettoyage des phares est généralement alimentée par un circuit distinct
    de la pompe lave-glace (relais ou circuit dédié dans le boîtier de bord). -
    Remplissage du réservoir — Remplissez le réservoir de liquide lave-phares
    dilué selon la saison. Ne pas utiliser d'eau du robinet seule : elle
    favorise le calcaire dans les gicleurs et la corrosion interne de la pompe.
    - Test de projection — Activez le nettoyage des phares depuis la commande
    habituelle (levier ou touche dédiée). Les gicleurs télescopiques doivent se
    déployer, projeter le liquide sur l'optique et se rétracter. Un gicleur qui
    ne se déploie pas peut être bouché ou mécaniquement bloqué. - Réglage des
    gicleurs si nécessaire — Si le jet n'atteint pas le centre de l'optique,
    orientez délicatement l'embout du gicleur avec une aiguille fine. Le point
    d'impact idéal est le centre de l'optique du phare. Vérification finale :
    après 2 à 3 cycles de nettoyage, contrôlez visuellement l'absence de fuite
    sur les raccords de durite et autour de la pompe dans le réservoir.
  S5: >-
    Certaines erreurs lors du diagnostic ou du remplacement de la pompe de
    nettoyage des phares sont fréquentes et peuvent conduire à un mauvais
    diagnostic, un montage raté ou une panne récurrente. Les voici accompagnées
    de leurs conséquences directes. - Confondre la pompe de phares avec la pompe
    lave-glace principale : sur la plupart des véhicules, les deux pompes sont
    distinctes, logées dans le même réservoir mais sur des puits différents.
    Commander la mauvaise pièce entraîne un renvoi et un délai supplémentaire. -
    Négliger de vérifier le fusible avant remplacement : un fusible grillé peut
    provoquer exactement les mêmes symptômes qu'une pompe défaillante. Remplacer
    la pompe sans vérifier le fusible revient à dépenser inutilement si c'est le
    fusible la cause. - Omettre de changer le joint torique lors du remplacement
    : le joint entre la pompe et le réservoir se déforme et durcit avec le
    temps. Le réutiliser entraîne une fuite de liquide dans le bas du
    compartiment moteur dès les premières semaines. - Négliger les gicleurs
    bouchés après remplacement de pompe : une pompe neuve qui projette contre
    des gicleurs colmatés par du calcaire ou des insectes ne netttoiera pas
    mieux qu'une pompe usée. Toujours nettoyer ou remplacer les gicleurs en même
    temps. - Monter une pompe sans vérifier la compatibilité du connecteur : une
    pompe d'une autre génération ou d'un autre modèle peut présenter un
    connecteur visuellement similaire mais avec un brochage différent, causant
    un court-circuit ou une pompe qui ne démarre pas.
  S6: >-
    Une fois la pompe de nettoyage des phares remplacée, une série de
    vérifications fonctionnelles s'impose avant de valider l'intervention et de
    remettre le véhicule en circulation nocturne. - Tester l'activation des jets
    sur les deux optiques : déclencher le nettoyage phares et vérifier que les
    deux optiques reçoivent bien un jet uniforme ; une optique sans jet signale
    une durite mal reconnectée ou un gicleur toujours bouché. - Vérifier
    l'orientation des gicleurs : les jets doivent couvrir la surface des
    optiques de façon homogène ; si les gicleurs sont réglables, les orienter
    selon les préconisations constructeur (généralement précisées dans le manuel
    d'atelier). - Contrôler l'étanchéité au niveau du réservoir : après
    plusieurs cycles de nettoyage, inspecter la base du réservoir et le puit de
    pompe pour détecter toute fuite de liquide liée à un joint torique mal posé.
    - Vérifier le niveau du réservoir lave-glace : compléter le niveau si
    nécessaire et s'assurer que la jauge (si présente) indique correctement. -
    Contrôler le connecteur électrique : tirer légèrement sur le câble pour
    s'assurer que le connecteur est correctement verrouillé ; un connecteur
    insuffisamment encliqueté peut se déboîter sur les premières vibrations. -
    Test visuel nocturne des optiques : allumer les phares après le test de
    nettoyage et vérifier que les optiques propres améliorent bien la portée
    lumineuse.
  S7: >-
    La pompe de nettoyage des phares fait partie d'un sous-système hydraulique
    dédié à l'éclairage avant. En cas de défaillance de la pompe, les composants
    suivants doivent être inspectés simultanément. - Gicleur de phare
    télescopique — Le gicleur est la partie visible du système de nettoyage. Son
    mécanisme télescopique peut se gripper sous l'effet du gel ou du calcaire.
    Un gicleur bloqué force la pompe et peut provoquer sa surchauffe. À nettoyer
    ou remplacer si le déploiement est irrégulier. - Phare avant — Si l'optique
    est déjà embuée ou fissurée, le nettoyage des phares aggrave le problème en
    forçant du liquide dans des zones non étanches. Vérifiez l'état des joints
    de phare avant de remettre en service le système de nettoyage. - Durites de
    circuit de nettoyage — Les durites en plastique rigide ou en caoutchouc
    souple reliant la pompe aux gicleurs peuvent se fissurer aux points de
    flexion. Une fuite sur ce circuit vide le réservoir sans projection visible
    sur les phares. - Relais et fusible du circuit — Un fusible grillé ou un
    relais défaillant prive la pompe d'alimentation. Vérifiez ces éléments en
    premier si la pompe ne démarre pas malgré une connexion électrique correcte.
    La pompe de nettoyage des phares est distincte de la pompe lave-vitre, même
    si elles partagent parfois le même réservoir. Précisez si votre véhicule
    dispose du système de nettoyage des phares (optionnel sur certaines
    versions) avant de commander.
  S8: >-
    La pompe de nettoyage des phares est-elle obligatoire sur tous les véhicules
    ? Non, ce dispositif n'est pas universel. La réglementation européenne
    impose le nettoyage des phares uniquement sur les véhicules équipés de
    projecteurs à décharge (xénon, bi-xénon) et sur certains projecteurs à LED
    de forte puissance. Sur ces modèles, la pompe est un équipement de sécurité
    obligatoire lié à l'homologation des optiques. Sur les véhicules à phares
    halogènes, il s'agit d'un équipement de confort optionnel, présent sur les
    niveaux de finition hauts de gamme. Peut-on continuer à rouler avec une
    pompe de nettoyage des phares défaillante ? Sur un véhicule à phares
    halogènes, la défaillance n'est qu'un inconfort. Sur un véhicule xénon ou
    LED homologué avec ce système, rouler sans nettoyage efficace des phares
    peut constituer une non-conformité au contrôle technique et dégrader
    progressivement les optiques, car les dépôts tenaces peuvent attaquer les
    traitements de surface des verres. Une intervention dès que possible est à
    privilégier. Comment distinguer une pompe de phares défaillante d'un gicleur
    simplement bouché ? Si la pompe fait du bruit lors de l'activation mais
    qu'aucun jet ne sort, débrancher une durite de gicleur et déclencher la
    pompe : si le liquide sort sous pression par la durite débranchée, la pompe
    fonctionne et c'est le gicleur qui est bouché (nettoyage à l'aiguille ou
    remplacement du gicleur). Si aucun débit ne sort même durite débranchée, la
    pompe est effectivement défaillante. Quelle est la durée de vie typique
    d'une pompe de nettoyage des phares ? Ces pompes sont conçues pour durer la
    vie du véhicule dans des conditions normales d'utilisation. Les défaillances
    prématurées surviennent généralement après 5 à 10 ans sur des véhicules
    exposés à des cycles gel/dégel répétés, ou lorsque le réservoir a été
    alimenté avec de l'eau non traitée qui favorise le tartre et corrode la
    membrane interne de la pompe. Utiliser exclusivement du liquide lave-glace
    concentré dilué selon les préconisations constructeur prolonge la durée de
    vie de la pompe. Comment choisir le bon liquide lave-glace pour préserver la
    pompe ? Utiliser un liquide lave-glace avec des agents anticalcaire et
    antigivre adapté à la saison. Éviter de diluer avec de l'eau du robinet très
    calcaire, car le tartre détériore rapidement les joints internes et les
    gicleurs. En hiver, vérifier que le liquide est protégé jusqu'à la
    température minimale attendue dans votre région pour éviter que le gel dans
    les durites n'endommage la pompe au démarrage.
  META: >-
    {"meta_title":"Pompe nettoyage phares : jets inactifs ? Guide |
    AutoMecanik","meta_description":"Jets de phares inactifs ou phares sales
    malgré l'activation ? Ce guide explique quand remplacer la pompe nettoyage
    des phares et comment choisir la pièce compatible avec votre véhicule.","met
    a_title_length":54,"meta_description_length":155,"primary_intent":"diagnosti
    c","target_symptoms":["jets de phares inactifs","phares sales malgre l
    activation","bruit de pompe sans projection"],"category":"accessoires"}
---

# Pompe nettoyage des phares - Guide Diagnostic Complet

## Fonction et Rôle

Projette le liquide de nettoyage sur les optiques de phares

**Actions principales:** projeter, pulveriser, alimenter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- jets de phares inactifs
- phares sales malgre l activation
- bruit de pompe sans projection

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe nettoyage des phares:

1. **Inspection visuelle** - Examiner l'état du pompe nettoyage des phares
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- gicleur
- phare

## Critères de Compatibilité

Pour commander le bon pompe nettoyage des phares, vous devez connaître:

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

**Comment choisir Pompe nettoyage des phares compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Pompe nettoyage des phares ?**
En cas de jets de phares inactifs ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Pompe nettoyage des phares sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
