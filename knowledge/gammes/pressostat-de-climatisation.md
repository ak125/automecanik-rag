---
category: climatisation
slug: pressostat-de-climatisation
title: Pressostat de climatisation
pg_id: 1360
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
  role: Mesurer la pression du fluide et proteger le compresseur
  must_be_true:
  - detecter
  - mesurer
  - proteger
  must_not_contain:
  - injection
  - freinage
  - allumage
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - compresseur-de-climatisation
  - condenseur-de-climatisation
  - evaporateur-de-climatisation
  - filtre-d-habitacle
  - detendeur-de-climatisation
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
  - ❌ "refroidit instantanement"
  cost_range:
    min: 200
    max: 800
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  brands:
    premium:
    - Delphi
    - Hella
    - Sanden
    - Denso
    standard:
    - NRF
    - Nissens
    - Valeo
    budget:
    - Thermotec
    - Frigair
    - Meat & Doria
  quality_tiers:
  - tier: Origine constructeur (OE/OES)
    description: Pressostat identique a celui monte en usine, fabrique par l'equipementier d'origine.
  - tier: Equivalent OE (qualite premiere monte)
    description: Pressostat de qualite identique a l'OE, fabrique par un equipementier reconnu mais sous sa propre marque.
  - tier: Adaptable (qualite atelier courant)
    description: Pressostat compatible de fabrication independante. Fonctionnement correct pour un usage courant.
diagnostic:
  symptoms:
  - id: S1
    label: Climatisation qui s arrete brutalement
    severity: confort
  - id: S2
    label: Compresseur qui ne demarre pas
    severity: immobilisation
  - id: S3
    label: Voyant de climatisation clignotant
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - lecture codes defaut obd et diagnostic electronique
  - 'vehicule immobilise ou symptome critique : verification urgente piece et alimentation'
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  quick_checks:
  - 'Observer : climatisation qui s arrete brutalement ?'
  - 'Observer : compresseur qui ne demarre pas ?'
  - Voyant de climatisation clignotant ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Climatisation qui s arrete brutalement
  - Compresseur qui ne demarre pas
  - Voyant de climatisation clignotant
  good_practices:
  - Faire tourner la climatisation 10 min par semaine meme en hiver
  - Remplacement du filtre d habitacle chaque annee
  - Recharge de gaz par un professionnel equipe (circuit sous pression)
  - Controle d etancheite si baisse de performance
rendering:
  pgId: '1360'
  intro_title: A quoi sert Pressostat de climatisation ?
  risk_title: Pourquoi remplacer Pressostat de climatisation a temps ?
  risk_explanation: '**Pièce HS** - Le pressostat de climatisation peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le pressostat de climatisation peut être hors service et nécessiter un remplacement'
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
  - question: Comment choisir Pressostat de climatisation compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Pressostat de climatisation ?
    answer: En cas de climatisation qui s arrete brutalement ou de degradation mesurable, il faut controler rapidement avant
      panne secondaire.
  - question: Puis-je monter Pressostat de climatisation sans verification atelier ?
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
doc_id: 6cfd6fde-ffb4-5f4b-a9a1-c10945044e83
content_hash: sha256:ad13da242766435d
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
  area: Face avant (condenseur), habitacle (evaporateur), moteur (compresseur)
  access: Variable selon composant (capot, tableau de bord, face avant)
  adjacent_parts:
  - compresseur
  - condenseur
  - detendeur
  - evaporateur
installation:
  difficulty: difficile (pro obligatoire)
  time: 1h a 4h
  tools:
  - station de recharge
  - detecteur de fuites
  - cle a douille
  prerequisite: Recuperation du gaz obligatoire par professionnel agree
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-04'
  _web_files_count: 1
  _has_tech_data: true
  technical_notes:
    val_000__c: '000 °C'
    val_100__: '100 %'
    val_14_a: '14 a'
    val_20__c: '20 °C'
    val_200_bar: '200 bar'
    val_25_a: '25 a'
    val_25__c: '25 °C'
    val_70__: '70 %'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le pressostat de climatisation est un capteur de pression intégré dans le
    circuit frigorifique du système de climatisation. Sa mission est double :
    mesurer en permanence la pression du fluide frigorigène circulant dans le
    circuit haute pression et protéger le compresseur contre les conditions de
    fonctionnement anormales qui l'endommagent irréversiblement. Concrètement,
    le pressostat détecte trois états critiques : une pression trop basse
    (manque de fluide frigorigène par fuite), une pression trop haute
    (condenseur encrassé ou ventilateur en panne) et une pression nominale
    correspondant au fonctionnement normal. En cas de pression hors plage
    acceptable, il envoie un signal électrique à l'unité de contrôle de la
    climatisation qui coupe immédiatement le compresseur pour éviter une casse
    mécanique. Le compresseur de climatisation coûte plusieurs centaines d'euros
    ; le pressostat, qui vaut une fraction de ce prix, est donc le gardien
    électronique de cet organe coûteux. Sur les véhicules modernes, le
    pressostat est souvent un capteur analogique à trois fils qui transmet une
    valeur de pression continue (et non plus seulement un simple contact
    ouvert/fermé comme les anciens modèles bi-états). La conduite de
    climatisation qui le reçoit, ainsi que le compresseur, sont les pièces
    directement liées à son fonctionnement. Un pressostat défaillant peut
    provoquer une coupure intempestive du compresseur même à pression normale,
    ou au contraire ne pas couper lors d'une surpression dangereuse.
  S2: >-
    Le pressostat de climatisation peut tomber en panne de deux manières
    opposées : rester fermé en permanence (climatisation coupée tout le temps)
    ou rester ouvert en permanence (compresseur non protégé). Les symptômes
    suivants orientent vers un diagnostic avant de procéder au remplacement. -
    Climatisation qui s'arrête brutalement et aléatoirement : le système se
    coupe sans raison apparente puis repart quelques minutes plus tard ; le
    pressostat détecte de fausses pressions basses et interrompt le compresseur
    de manière intempestive. - Compresseur qui ne démarre pas (symptôme
    critique) : le compresseur ne s'enclenche jamais, même avec la climatisation
    activée à la commande ; si le niveau de fluide frigorigène est correct, un
    pressostat bloqué en position ouverte est la cause la plus fréquente. -
    Voyant de climatisation clignotant : sur les véhicules à affichage digital
    du système de climatisation, un voyant ou un code d'erreur lié à la pression
    s'allume ; lire les codes défaut OBD pour distinguer un défaut de capteur
    d'une pression réellement anormale. - Climatisation inefficace par temps
    chaud : si le compresseur s'enclenche puis se désengage trop rapidement, la
    cabine ne se refroidit pas correctement ; une lecture des pressions avec une
    station de diagnostic confirme si la pression est normale et si le
    pressostat est à mettre en cause. - Codes défaut liés à la pression du
    circuit : un diagnostic OBD révèle des codes P0530 (circuit défaut
    pressostat), P0531 (plage/performance), P0532 (signal bas) ou P0533 (signal
    haut) ; ces codes pointent directement le capteur. - Absence de froid
    uniquement en conditions extrêmes : le compresseur fonctionne normalement en
    température ambiante modérée mais se coupe dès que la charge thermique
    augmente (forte chaleur, embouteillage) ; un pressostat vieillissant perd sa
    précision de mesure à haute pression.
  S3: >-
    Le pressostat de climatisation est un composant dont la plage de pression et
    le type de signal électrique sont spécifiques au système de climatisation du
    véhicule. Un pressostat inadapté peut couper le compresseur à la mauvaise
    pression ou ne pas le protéger du tout. Voici les critères de sélection à
    respecter. - Marque, modèle et année de production : la référence varie
    selon le constructeur et la génération de système de climatisation équipant
    le véhicule ; une erreur d'un millésime peut mener à commander un capteur
    avec un signal électrique incompatible. - Type de fluide frigorigène du
    circuit : vérifier si votre véhicule utilise du R134a (la grande majorité
    des véhicules jusqu'aux années 2015-2018) ou du R1234yf (véhicules plus
    récents conformes à la réglementation européenne) ; certains pressostats
    sont calibrés différemment selon le fluide. - Type de capteur : binaire ou
    analogique : les anciens pressostats sont des contacts simples
    (ouvert/fermé) ; les pressostats modernes sont des capteurs analogiques qui
    transmettent une valeur de pression continue ; ces deux types ne sont pas
    interchangeables. - Vérifier le symptôme avant de commander : si le
    compresseur ne démarre pas, faire d'abord un contrôle du niveau de fluide
    par un professionnel équipé d'une station de charge ; un circuit vide simule
    les mêmes symptômes qu'un pressostat défaillant. - Lire les codes défaut OBD
    : un diagnostic électronique préalable confirme si le code pointe bien le
    pressostat (codes P053x) et évite de remplacer une pièce saine. -
    Privilégier les équipementiers spécialisés : des marques comme NRF, Hella,
    Delphi ou Denso proposent des pressostats homologués avec les seuils de
    pression conformes aux spécifications constructeur. - Vérifier les pièces
    associées : lors du remplacement, inspecter l'état de la conduite de
    climatisation au niveau du raccord du pressostat pour détecter une fuite de
    fluide frigorigène potentielle. Pour aller plus loin : consultez notre guide
    d'achat pressostat de climatisation — comparatif marques, critères de choix
    et prix.
  S4_DEPOSE: >-
    Le remplacement du pressostat de climatisation nécessite idéalement une
    récupération préalable du fluide frigorigène par une station de
    climatisation, sauf si le modèle de pressostat du véhicule dispose d'un
    raccord à valve Schrader permettant un remplacement sans dépressuriser le
    circuit. Dans le cas général, voici la procédure à suivre. - Faire récupérer
    le fluide frigorigène : avant toute intervention sur le circuit, faire
    dépressuriser et récupérer le fluide R134a ou R1234yf par un professionnel
    équipé d'une station agréée ; le rejet de fluide frigorigène dans
    l'atmosphère est interdit par la réglementation européenne. - Localiser le
    pressostat : il se trouve sur la conduite haute pression du circuit de
    climatisation, généralement accessible depuis le compartiment moteur ; il
    est vissé dans un raccord fileté sur la conduite ou le condenseur. -
    Débrancher la batterie : couper l'alimentation électrique avant de manipuler
    le connecteur du capteur pour protéger l'unité de contrôle climatisation. -
    Débrancher le connecteur électrique : appuyer sur le clip de verrouillage et
    retirer le connecteur ; noter le nombre de broches pour commander la pièce
    de remplacement identique. - Dévisser le pressostat défaillant : utiliser
    une clé plate de la taille adaptée (généralement 19 ou 22 mm selon les
    modèles) ; dévisser doucement en maintenant la conduite stable pour ne pas
    la plier. - Installer le nouveau pressostat : enduire le filetage d'un léger
    film de lubrifiant frigorigène ou huile polyol-ester, visser à la main puis
    serrer au couple préconisé (généralement 8 à 12 Nm) sans forcer. -
    Reconnecter le connecteur électrique : encliquer le connecteur jusqu'au clic
    de verrouillage. - Faire recharger le circuit : faire recharger le circuit
    en fluide frigorigène avec la quantité exacte préconisée par le constructeur
    par un technicien agréé ; tester ensuite la climatisation pour confirmer le
    bon fonctionnement.
  S4_REPOSE: >-
    Repose du pressostat de climatisation Après avoir installé le nouveau
    pressostat, respectez cette séquence pour garantir l'étanchéité du circuit
    et la protection du compresseur. Préparation avant repose - Vérifiez que le
    nouveau pressostat correspond à la référence d'origine (pression d'ouverture
    et de fermeture identiques) - Inspectez le filetage du raccord sur le
    circuit : aucun fil endommagé ne doit subsister - Remplacez systématiquement
    le joint torique (O-ring) fourni avec la nouvelle pièce — ne jamais
    réutiliser l'ancien - Lubrifiez légèrement le joint torique avec quelques
    gouttes d'huile PAG compatible avec votre fluide frigorigène (R134a ou
    R1234yf selon véhicule) Étapes de remontage - Mise en place du pressostat —
    vissez à la main jusqu'au contact, sans forcer, pour éviter de coincer le
    joint - Serrage au couple — serrez à la clé selon la préconisation
    constructeur (généralement 8 à 12 Nm selon le type de raccord) ; évitez le
    serrage excessif qui écrase le joint - Branchement du connecteur électrique
    — enclenchez fermement jusqu'au clic de verrouillage ; vérifiez l'absence de
    corrosion sur les broches avant connexion - Recharge du circuit
    climatisation — uniquement par un professionnel habilité avec station de
    charge homologuée ; ne jamais charger soi-même le fluide frigorigène
    (réglementation F-Gaz) - Mise sous pression et contrôle d'étanchéité — après
    recharge, vérifiez l'absence de fuite au niveau du raccord avec détecteur
    électronique ou UV Contrôles fonctionnels après repose - Démarrez le moteur
    et activez la climatisation — le compresseur doit s'enclencher normalement -
    Vérifiez que le voyant de climatisation ne clignote plus au tableau de bord
    - Contrôlez la température de soufflage en sortie d'aérateur (doit descendre
    sous 10°C en conditions normales) - Effectuez un test de 10 à 15 minutes en
    roulage pour valider le cycle de coupure/enclenchement du pressostat
  S5: >-
    Le diagnostic et le remplacement du pressostat de climatisation donnent lieu
    à plusieurs erreurs fréquentes qui peuvent aggraver la panne ou nécessiter
    une seconde intervention. Les voici avec leurs conséquences. - Remplacer le
    pressostat sans vérifier le niveau de fluide frigorigène : un circuit vide
    ou sous-chargé coupe le compresseur exactement comme un pressostat
    défaillant ; si le circuit est vide, un pressostat neuf ne changera rien et
    la véritable cause (fuite) devra être traitée séparément. - Ouvrir le
    circuit sans récupérer le fluide : dévisser le pressostat sur un circuit
    encore sous pression libère le fluide frigorigène dans l'atmosphère, ce qui
    est illégal et peut provoquer des brûlures par contact avec le fluide sous
    pression. - Confondre le pressostat avec le capteur de température de
    climatisation : ces deux capteurs sont souvent proches l'un de l'autre sur
    le circuit ; commander et monter le mauvais capteur est une erreur fréquente
    sur certaines marques où les deux capteurs se ressemblent. - Sous-serrer ou
    sur-serrer le pressostat : un sous-serrage entraîne une fuite de fluide
    frigorigène au niveau du filetage dès la remise en charge du circuit ; un
    sur-serrage peut fracturer le raccord fileté de la conduite ou déformer le
    capteur. - Négliger de lire les codes défaut après remplacement : effacer
    les codes sans vérifier qu'ils ne reviennent pas après un test de
    climatisation de 15 minutes laisse passer une panne intermittente ; toujours
    relire les codes après un cycle complet de fonctionnement.
  S6: >-
    Après le remplacement du pressostat et la recharge du circuit frigorigène,
    plusieurs vérifications permettent de valider l'intervention et de s'assurer
    que le système de climatisation fonctionne dans ses paramètres normaux. -
    Tester l'enclenchement du compresseur : activer la climatisation à froid et
    vérifier que le compresseur s'enclenche dans les premières secondes ; un
    embrayage magnétique qui se connecte et reste connecté confirme que le
    pressostat détecte une pression normale. - Vérifier les températures de
    soufflage : après 5 minutes de fonctionnement à régime stabilisé, la
    température de soufflage des bouches doit être nettement fraîche
    (typiquement entre 5 et 12 °C selon la température ambiante et la puissance
    du système). - Contrôler l'absence de codes défaut : effectuer un scan OBD
    après 15 minutes de fonctionnement en climatisation pour s'assurer qu'aucun
    code lié au pressostat (P053x) ne s'est régénéré. - Inspecter l'étanchéité
    du raccord pressostat : appliquer un produit détecteur de fuite UV ou
    utiliser une lampe UV après quelques heures de fonctionnement pour s'assurer
    qu'aucune fuite de fluide ne se produit au niveau du filetage du nouveau
    pressostat. - Vérifier le comportement sous forte charge thermique : tester
    la climatisation par temps chaud (ou en simulant la charge par le chauffage
    de l'habitacle) pour confirmer que le compresseur reste enclenché sans
    coupure intempestive.
  S7: >-
    Pièces à vérifier lors du remplacement du pressostat de climatisation Le
    pressostat de climatisation travaille en liaison directe avec plusieurs
    composants du circuit frigorifique. Un remplacement isolé sans vérifier ces
    pièces peut conduire à une nouvelle panne rapide. - Conduite de
    climatisation Les conduites haute et basse pression acheminent le fluide
    frigorigène vers le pressostat. Une conduite fissurée ou dont les raccords
    sont poreux provoque une fuite de fluide qui déclenche à nouveau le
    pressostat de protection. Inspectez visuellement l'ensemble du circuit lors
    de chaque intervention. Voir les conduites de climatisation - Compresseur de
    climatisation Le pressostat protège directement le compresseur contre les
    sur-pressions et sous-pressions. Si le compresseur est usé ou présente des
    jeux internes excessifs, les pressions de fonctionnement sortent des plages
    normales et le pressostat coupe prématurément. Un pressostat neuf ne résout
    pas un compresseur défaillant. Voir les compresseurs de climatisation -
    Condenseur de climatisation Un condenseur encrassé ou partiellement bouché
    élève la pression haute du circuit. Le pressostat détecte alors une pression
    anormalement haute et déclenche la coupure du compresseur. Nettoyez ou
    remplacez le condenseur si la pression haute est systématiquement excessive.
    Voir les condenseurs de climatisation
  S8: >-
    Peut-on remplacer soi-même le pressostat de climatisation ? Le remplacement
    du pressostat est techniquement possible pour un bricoleur averti si le
    véhicule dispose d'un pressostat à valve Schrader intégrée permettant le
    remplacement sans dépressurisation du circuit. Dans le cas général,
    l'intervention nécessite de faire récupérer le fluide frigorigène par un
    professionnel équipé d'une station agréée, puis de faire recharger le
    circuit après remplacement. Intervenir sur un circuit frigorigène sous
    pression sans équipement adapté est dangereux et illégal. Comment savoir si
    c'est le pressostat ou une fuite de fluide qui coupe le compresseur ? Un
    technicien connecte une station de charge avec des manomètres haute et basse
    pression. Si les pressions mesurées sont dans la plage normale et que le
    compresseur ne démarre quand même pas, le pressostat est très probablement
    en cause. Si les pressions sont anormalement basses, il y a une fuite de
    fluide frigorigène à localiser et corriger avant de remplacer quoi que ce
    soit. Quels codes défaut OBD sont associés au pressostat de climatisation ?
    Les codes défaut les plus courants liés au pressostat sont : P0530 (circuit
    ouvert ou signal absent), P0531 (signal hors plage de fonctionnement), P0532
    (signal trop bas, pressostat bloqué en pression basse) et P0533 (signal trop
    haut, pressostat bloqué en pression haute). Ces codes sont génériques ;
    certains constructeurs ajoutent des codes propriétaires plus précis. La
    lecture des codes doit toujours être combinée à une mesure physique des
    pressions pour confirmer le diagnostic. Combien de temps dure un pressostat
    de climatisation ? Un pressostat de climatisation a normalement une durée de
    vie de 10 à 15 ans. La défaillance prématurée est souvent liée à la
    corrosion du connecteur électrique dans un environnement humide, à des
    vibrations excessives sur les véhicules roulant fréquemment sur revêtements
    dégradés, ou à une contamination du fluide frigorigène par de l'humidité qui
    accélère la corrosion interne des composants électroniques du capteur. Le
    remplacement du pressostat nécessite-t-il de recharger la climatisation ?
    Dans la plupart des cas, oui. Sauf si votre véhicule dispose d'un raccord à
    valve Schrader qui permet de retirer le pressostat sans ouvrir le circuit
    pressurisé, il faut dépressuriser le circuit pour le remontage, puis faire
    recharger avec la quantité exacte de fluide spécifiée par le constructeur.
    Une surcharge ou une sous-charge de fluide après remplacement provoque les
    mêmes symptômes que le pressostat défaillant d'origine.
---

# Pressostat de climatisation - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la pression du fluide et proteger le compresseur

**Actions principales:** detecter, mesurer, proteger

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Compresseur qui ne demarre pas**
  compresseur qui ne demarre pas

### 🟢 Autres Symptômes

- climatisation qui s arrete brutalement
- voyant de climatisation clignotant

## Procédure de Diagnostic

Pour diagnostiquer un problème de pressostat de climatisation:

1. **Inspection visuelle** - Examiner l'état du pressostat de climatisation
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le pressostat de climatisation peut être hors service et nécessiter un remplacement
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- conduite-de-climatisation

## Critères de Compatibilité

Pour commander le bon pressostat de climatisation, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidit instantanement"

## FAQ

**Comment choisir Pressostat de climatisation compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Pressostat de climatisation ?**
En cas de climatisation qui s arrete brutalement ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Pressostat de climatisation sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
