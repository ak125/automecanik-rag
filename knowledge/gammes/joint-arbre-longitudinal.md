---
category: transmission
slug: joint-arbre-longitudinal
title: Joint arbre longitudinal
pg_id: 1427
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
  role: Transmettre le couple entre les elements de transmission
  must_be_true:
  - transmettre
  - articuler
  - relier
  must_not_contain:
  - injection
  - freinage
  - climatisation
  - allumage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - cardan
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
  - ❌ "transmission parfaite"
  cost_range:
    min: 400
    max: 1200
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Qualité Origine (OE)
    description: Joints d'arbre longitudinal fournis en première monte. Croisillons usinés avec précision, coupelles à aiguilles
      graissées, circlips de maintien conformes.
  - tier: Équivalent Qualité Origine
    description: Joints de transmission fabriqués selon les mêmes tolérances que l'OE. Croisillons traités thermiquement,
      coupelles étanches.
  - tier: Adaptable Économique
    description: Joints de cardan aux dimensions compatibles. Conviennent pour un usage courant. Vérifier le diamètre des
      coupelles et l'entraxe avant montage.
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
    label: Vibrations a vitesse constante
    severity: confort
  - id: S2
    label: Claquements en acceleration deceleration
    severity: confort
  - id: S3
    label: Bruits de roulement sous le vehicule
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - verifier equilibrage et fixations
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'vibrations anormales : verifier equilibrage et fixations'
  quick_checks:
  - Vibrations a vitesse constante ?
  - 'Observer : claquements en acceleration deceleration ?'
  - Bruits de roulement sous le vehicule ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Vibrations a vitesse constante
  - Claquements en acceleration deceleration
  - Bruits de roulement sous le vehicule
  good_practices:
  - Verifier le niveau d huile de boite selon preconisation constructeur
  - Controle des soufflets de protection (pas de fuite de graisse)
  - Remplacement de la bague d etancheite en cas de fuite
  - Inspection des cardans et croisillons a chaque revision
rendering:
  pgId: '1427'
  intro_title: A quoi sert Joint arbre longitudinal ?
  risk_title: Pourquoi remplacer Joint arbre longitudinal a temps ?
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
  - question: Comment choisir Joint arbre longitudinal compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Joint arbre longitudinal ?
    answer: En cas de vibrations a vitesse constante ou de degradation mesurable, il faut controler rapidement avant panne
      secondaire.
  - question: Puis-je monter Joint arbre longitudinal sans verification atelier ?
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
doc_id: c5f695cf-1c75-5b04-85a2-3cae5b6378a6
content_hash: sha256:6923c75263a05ec4
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
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-04'
  _web_files_count: 1
  _has_tech_data: false
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le joint d'arbre longitudinal (aussi appelé joint de transmission
    longitudinal) est un composant d'étanchéité situé à l'interface entre
    l'arbre de transmission longitudinal et les boîtiers de renvoi d'angle, le
    pont arrière ou la boîte de transfert selon la configuration du véhicule. Sa
    fonction est double : transmettre le couple moteur sans fuite de lubrifiant
    et articuler les mouvements relatifs entre les organes de transmission. Dans
    les véhicules à propulsion ou à transmission intégrale, l'arbre longitudinal
    (aussi nommé arbre de cardan ou arbre propulseur) relie la boîte de vitesses
    au pont arrière. Le joint d'arbre assure l'étanchéité aux deux extrémités de
    cet arbre, là où il pénètre dans le carter du différentiel ou de la boîte de
    transfert. Sans ce joint, le lubrifiant interne s'écoule, réduisant la
    lubrification des pignons et conduisant à une usure rapide ou à une casse
    des organes internes. Mécaniquement, ces joints sont le plus souvent des
    simples lèvres en élastomère (joints spi) ou des joints à double lèvre pour
    les environnements plus agressifs. Ils travaillent en rotation continue et
    sont soumis à des contraintes de température, de pression interne et de
    vibrations. Les pièces associées à surveiller lors du remplacement incluent
    le cardan et le soufflet de cardan.
  S2: >-
    La détérioration d'un joint d'arbre longitudinal suit une progression
    caractéristique. Reconnaître les signes précoces permet d'intervenir avant
    que la panne ne se propage aux organes de transmission adjacents : -
    Vibrations à vitesse constante : des vibrations ressenties dans le plancher
    ou la colonne de direction lors d'un maintien de vitesse (80-120 km/h)
    signalent souvent un déséquilibre de l'arbre lié à un jeu excessif au niveau
    du joint usé. - Claquements en accélération et en décélération : des bruits
    secs ou claquements lors des phases de reprise ou de relâchement de
    l'accélérateur indiquent un jeu dans la liaison joint/arbre ou joint/pont,
    caractéristique d'un joint très usé. - Bruits de roulement sous le véhicule
    : un bruit continu de type roulement ou sifflement sourd localisé sous le
    plancher, variant avec la vitesse mais pas avec les virages, pointe vers
    l'arbre longitudinal ou ses joints. - Tache d'huile sous le véhicule à
    l'arrière : une fuite de lubrifiant sous la zone centrale ou arrière du
    véhicule indique une défaillance du joint d'étanchéité. L'huile de pont est
    généralement plus foncée et plus visqueuse que l'huile moteur. - Niveau
    d'huile de pont en baisse : une perte progressive de lubrifiant dans le
    différentiel arrière ou la boîte de transfert est souvent due à un joint
    d'arbre défaillant. - Odeur de lubrifiant chaud : le lubrifiant de pont qui
    s'échappe sur des organes chauds produit une odeur caractéristique
    différente de l'huile moteur.
  S3: >-
    Le joint d'arbre longitudinal est une pièce d'étanchéité dont les dimensions
    et le matériau doivent correspondre exactement à la spécification
    constructeur. Une erreur de sélection entraîne une fuite immédiate ou une
    durée de vie réduite : - Marque et modèle exact du véhicule : les dimensions
    du logement (diamètre intérieur, diamètre extérieur, hauteur) varient selon
    le constructeur et la configuration de transmission. - Motorisation et type
    de transmission : propulsion, traction, 4x4 permanent ou 4x4 à la demande —
    chaque architecture utilise des arbres de diamètres différents et donc des
    joints différents. - Côté concerné : identifier précisément si le joint est
    celui du côté boîte de vitesses, boîte de transfert ou pont arrière, car les
    dimensions peuvent différer d'un côté à l'autre. - Matériau du joint :
    joints en NBR (nitrile) pour les applications standard, joints en FKM
    (Viton) pour les environnements à haute température ou produits chimiques
    agressifs — choisir selon les spécifications constructeur. - Présence d'une
    lèvre anti-poussière : certains joints comportent une double lèvre dont une
    dédiée à repousser la boue et l'eau. Nécessaire pour les véhicules 4x4 ou
    utilitaires roulant hors route. - Référence OEM ou équipementier reconnu :
    privilégier des marques comme Corteco, Elring, Victor Reinz dont les joints
    respectent les tolérances d'origine. Vérifier la compatibilité avec votre
    référence constructeur. - Vérifier l'état du logement : avant de commander
    un joint, s'assurer que le logement dans le carter n'est pas rayé ou corrodé
    — un logement abîmé ne garantit plus l'étanchéité même avec un joint neuf.
    Pour aller plus loin : consultez notre guide d'achat joint arbre
    longitudinal — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    Le remplacement d'un joint d'arbre longitudinal nécessite la dépose
    partielle de la transmission. Cette opération requiert un équipement adapté
    et une méthode rigoureuse pour éviter d'endommager le logement ou l'arbre :
    - Mise en sécurité : élever le véhicule sur chandelles, débrancher la
    batterie. Placer un bac de récupération sous la zone de travail car du
    lubrifiant va s'écouler. - Vidange du lubrifiant concerné : vidanger l'huile
    de pont ou de la boîte de transfert avant dépose pour éviter de polluer le
    sol et faciliter le travail. Conserver le volume pour remplir à l'identique.
    - Dépose de l'arbre longitudinal : démarquer la position angulaire des
    flasques de cardan (marqueur ou pointeau) avant démontage pour respecter
    l'équilibrage d'origine. Dévisser les vis de flasque, soutenir l'arbre et le
    dégager. - Extraction de l'ancien joint : utiliser un extracteur de joint
    adapté ou un tournevis à lame plate protégée pour déloger le joint sans
    rayer le logement. Ne jamais utiliser un tournevis directement sur
    l'alésage. - Nettoyage et inspection du logement : nettoyer soigneusement le
    logement avec un chiffon non fibreux. Inspecter la piste de frottement sur
    l'arbre pour détecter toute strie ou corrosion. Un arbre strié devra être
    remplacé ou réparé. - Mise en place du nouveau joint : lubrifier légèrement
    le joint neuf avec la même huile que celle du carter. Monter le joint à
    l'aide d'un poussoir cylindrique de diamètre adapté (ou d'une douille de
    remplacement) pour l'enfoncer uniformément et perpendiculairement, jusqu'à
    affleurement du logement. - Repose de l'arbre et remplissage : reposer
    l'arbre en respectant les repères angulaires. Remplir le carter au niveau
    prescrit avec le lubrifiant homologué constructeur. Vérifier l'absence de
    fuite après mise en route.
  S4_REPOSE: >-
    Après avoir remplacé le joint d'arbre longitudinal, la repose de la
    transmission doit être rigoureuse. Un joint mal posé ou un arbre mal orienté
    peut provoquer une fuite immédiate ou des vibrations dès la remise en
    circulation. - Lubrification du lèvre du joint neuf : avant d'introduire
    l'arbre, appliquer une fine couche d'huile de boîte ou d'huile de pont
    (selon le type de joint) sur la lèvre d'étanchéité du joint. Ne jamais
    introduire un arbre dans un joint à sec — le lèvre se déchire à l'insertion
    et la fuite est immédiate. - Introduction de l'arbre dans le joint : aligner
    l'arbre dans l'axe exact du joint avant d'insérer. Toute inclinaison roule
    ou rétrograde la lèvre du joint. Introduire doucement en effectuant une
    légère rotation — ne jamais frapper l'arbre à la masse directement sur le
    joint. - Vérification du positionnement axial de l'arbre : une fois l'arbre
    en position, contrôler le jeu axial selon la préconisation constructeur. Un
    jeu excessif indique un épaulement d'arbre usé — le joint seul ne résoudra
    pas le problème dans ce cas. - Remontage des paliers ou des brides de
    fixation : sur les arbres longitudinaux de véhicules 4x4 ou à propulsion,
    des paliers intermédiaires ou des brides boulonnées maintiennent l'arbre.
    Remonter ces éléments en respectant les couples de serrage constructeur
    (généralement 40 à 80 N·m selon la taille). - Remontage des cardans et
    joints de cardan : reconnecter les joints de cardan en respectant les
    marquages de position (flèches ou traits de marquage effectués avant
    dépose). Une inversion de phase peut créer des vibrations à vitesse
    constante, symptôme difficile à diagnostiquer par la suite. - Vérification
    du niveau d'huile de pont ou de boîte de transfert : après toute
    intervention sur un joint d'arbre longitudinal, contrôler et si nécessaire
    compléter le niveau d'huile du pont ou de la boîte de transfert avec le
    lubrifiant préconisé (huile 75W90, 75W140 selon l'application). - Test
    dynamique prudent : effectuer quelques kilomètres à vitesse modérée avant de
    passer sur route rapide. Revenir inspecter visuellement la zone du joint
    après ce premier trajet pour confirmer l'absence de fuite et de suintement.
  S5: >-
    Le remplacement d'un joint d'arbre longitudinal est une opération de
    transmission qui, mal exécutée, peut provoquer une fuite persistante ou
    endommager des pièces coûteuses : - Monter le joint sans lubrification :
    insérer un joint à sec crée des contraintes excessives lors de la première
    rotation et provoque une usure prématurée de la lèvre en quelques centaines
    de kilomètres. Lubrifier toujours la lèvre avec le lubrifiant du carter. -
    Ne pas marquer la position angulaire de l'arbre : omettre de repérer la
    position du cardan avant dépose désorganise l'équilibrage d'usine de
    l'arbre. Cela génère des vibrations à haute vitesse qui n'existaient pas
    avant l'intervention. - Enfoncer le joint de travers : un joint monté de
    biais ne scelle pas correctement le logement et fuit immédiatement. Utiliser
    impérativement un outil cylindrique adapté, jamais un marteau directement
    sur le joint. - Rayer le logement lors de l'extraction : utiliser un
    tournevis directement en levier sur l'alésage crée des stries qui empêchent
    tout joint neuf d'assurer l'étanchéité. Toujours utiliser un extracteur de
    joint ou protéger le logement. - Omettre de contrôler le niveau de
    lubrifiant après montage : ne pas vérifier le niveau d'huile de pont après
    remplacement du joint laisse le risque d'une marche à sec si le carter était
    déjà bas. Toujours contrôler et ajuster le niveau avant le premier départ.
  S6: >-
    Après la pose d'un joint d'arbre longitudinal neuf, plusieurs points de
    contrôle s'imposent pour valider l'étanchéité et le comportement dynamique
    du véhicule : - Contrôle visuel immédiat à froid : avant de remettre le
    véhicule en circulation, inspecter la zone du joint pour détecter toute
    fuite résiduelle due à un mauvais centrage ou un oubli de lubrification. -
    Vérification du niveau de lubrifiant du carter : contrôler que le niveau
    d'huile de pont ou de boîte de transfert est au niveau correct selon les
    spécifications constructeur. Un niveau insuffisant endommage les engrenages
    dès les premiers kilomètres. - Test dynamique progressif : effectuer un
    premier trajet court (5-10 km) à vitesse modérée, en variant les
    accélérations. Écouter l'absence de claquements ou de vibrations qui
    indiqueraient un mauvais remontage de l'arbre. - Inspection sous le véhicule
    après le premier trajet : après le test routier, placer le véhicule sur sol
    propre et inspecter la zone du joint. Aucune goutte d'huile ne doit
    apparaître. Un léger suintement dans les 10 premières minutes peut venir du
    lubrifiant résiduel sur l'arbre — il doit cesser rapidement. - Contrôle des
    vibrations à 110 km/h : si l'arbre a été déposé et reposé, effectuer un test
    à vitesse autoroutière pour confirmer l'absence de vibrations liées à un
    décalage angulaire de remontage.
  S7: >-
    La transmission longitudinale est un ensemble de composants solidaires. Lors
    du remplacement d'un joint d'arbre longitudinal, plusieurs éléments doivent
    être inspectés dans la même zone pour prévenir une nouvelle intervention
    rapprochée. - Cardan : le cardan est directement adjacent au joint d'arbre
    longitudinal sur la plupart des configurations 4x4 et propulsion. Vérifier
    le jeu dans les croisillons de cardan lors de la dépose. Un cardan avec du
    jeu ou grippé doit être remplacé en même temps. - Soufflet de cardan : si le
    soufflet de cardan est fissuré ou qu'il manque de la graisse, le remplacer
    dès que la zone est accessible. Un soufflet déchiré laisse entrer l'eau et
    les particules dans le cardan, qui s'use rapidement. - Palier intermédiaire
    d'arbre de transmission : sur les véhicules avec arbre longitudinal long, un
    palier à roulement maintient l'arbre en position médiane. Si ce palier est
    usé (bruit de roulement), le remplacer lors de la même intervention —
    l'arbre est déjà déposé. - Huile de pont / huile de boîte de transfert :
    chaque intervention sur les joints d'arbre longitudinal implique de vérifier
    les niveaux de lubrification du pont arrière et de la boîte de transfert si
    présente. Une huile dégradée (noire, avec particules métalliques) signale
    une usure interne à investiguer. - Autres joints SPI de pont : si un joint
    fuit, les autres joints du même boîtier (joints de sortie de pont côté
    roues) peuvent être dans le même état de vieillissement. Profiter de la
    dépose pour les inspecter visuellement.
  S8: >-
    Comment distinguer une fuite de joint d'arbre longitudinal d'une fuite de
    joint de cardan ? La fuite de joint d'arbre longitudinal se situe à
    l'interface entre l'arbre et le carter du pont ou de la boîte de transfert :
    la tache d'huile apparaît à l'arrière central du véhicule, juste devant ou
    derrière le pont. Le joint de cardan (soufflet) se situe à l'extrémité de
    l'arbre — sa rupture est souvent visible à l'oeil nu (soufflet déchiré avec
    graisse projetée). Les deux défauts peuvent coexister. Peut-on continuer à
    rouler avec un joint d'arbre longitudinal qui fuit ? Un faible suintement
    peut être temporairement toléré en surveillant le niveau d'huile de pont
    tous les 500 km. Cependant, une fuite franche vide le carter en quelques
    centaines de kilomètres et provoque une casse du pont arrière ou de la boîte
    de transfert, dont le coût de remplacement est très élevé. L'intervention
    doit être réalisée rapidement. Faut-il remplacer les deux joints (côté boîte
    et côté pont) en même temps ? Si le véhicule totalise plus de 150 000 km et
    que l'arbre a été déposé, remplacer les deux joints est une pratique
    professionnelle avisée. Le coût de la pièce est faible par rapport au coût
    de main-d'oeuvre d'une nouvelle dépose. Si le second joint n'est pas encore
    usé, la décision reste à l'appréciation du mécanicien après inspection. Quel
    lubrifiant utiliser pour remplir le carter après remplacement du joint ?
    Utiliser exclusivement le lubrifiant homologué par le constructeur pour le
    composant concerné (pont, boîte de transfert, boîte de vitesses). Pour un
    pont arrière classique, il s'agit généralement d'une huile de pont SAE
    75W-90 ou 80W-90 — mais vérifiez la notice du véhicule car certains ponts
    modernes utilisent des lubrifiants synthétiques spécifiques. Les vibrations
    ont-elles disparu après le remplacement du joint — est-ce normal si elles
    persistent légèrement ? Si les vibrations persistent après remplacement du
    joint, vérifiez d'abord que l'arbre a été remis dans sa position angulaire
    d'origine (repères marqués avant dépose). Si les repères n'ont pas été
    faits, un rééquilibrage de l'arbre par un spécialiste peut être nécessaire.
    Des vibrations persistantes peuvent aussi indiquer une usure des paliers
    intermédiaires de l'arbre.
  META: >-
    {"meta_title":"Joint arbre longitudinal : quand changer |
    AutoMecanik","meta_description":"Vibrations à vitesse constante ou
    claquements en accélération ? Apprenez à diagnostiquer un joint d'arbre
    longitudinal défaillant, choisir la bonne pièce et éviter les pannes seconda
    ires.","robots":"index,follow","og_type":"article","schema_type":"HowTo"}
---

# Joint arbre longitudinal - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre le couple entre les elements de transmission

**Actions principales:** transmettre, articuler, relier

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquements en acceleration deceleration**
  claquements en acceleration deceleration

### 🟢 Autres Symptômes

- vibrations a vitesse constante
- bruits de roulement sous le vehicule

## Procédure de Diagnostic

Pour diagnostiquer un problème de joint arbre longitudinal:

1. **Inspection visuelle** - Examiner l'état du joint arbre longitudinal
2. **Test dynamique** - Vérifier les bruits en roulant
3. **Contrôle du jeu** - Examiner l'usure des articulations
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

- cardan
- soufflet-de-cardan

## Critères de Compatibilité

Pour commander le bon joint arbre longitudinal, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "transmission parfaite"

## FAQ

**Comment choisir Joint arbre longitudinal compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Joint arbre longitudinal ?**
En cas de vibrations a vitesse constante ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Joint arbre longitudinal sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
