---
category: allumage
slug: distributeur-d-allumage
title: Distributeur d'allumage
pg_id: 683
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
  last_enriched_by: script:materialize-db-to-md
  last_enriched_at: '2026-04-03'
  v5_migrated_at: '2026-03-29'
domain:
  role: Distribuer la haute tension aux bougies dans l'ordre d'allumage
  must_be_true:
  - distribuer
  - repartir
  - transmettre
  must_not_contain:
  - freinage
  - climatisation
  - embrayage
  - direction
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - distribuer
  - repartir
  - transmettre
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
  - ❌ "demarrage instantane"
  cost_range:
    min: 100
    max: 400
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Pièce d'origine (OE / neuf)
    description: Distributeur neuf conforme à la spécification constructeur d'origine. Disponibilité variable selon l'âge
      du véhicule. Recommandé pour les restaurations soignées.
  - tier: Équipementier reconnu (allumage)
    description: Produit de fabricants spécialisés en systèmes d'allumage. Compatible avec les kits de distribution (vis platinées,
      condensateur, rotor, chapeau).
  - tier: Pièce adaptable / reconditionné
    description: Option sur véhicules anciens où la pièce neuve n'est plus disponible. Vérifier l'ordre d'allumage, le type
      de déclencheur (platines ou capteur Hall) et les dimensions de l'arbre.
  - tier: Distributeur reconditionné
    description: Reconditionné d'occasion avec remplacement des pièces d'usure internes. Peut convenir pour certains modèles
      dont les pièces neuves ne sont plus disponibles.
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
    label: Rates d allumage
    severity: confort
  - id: S2
    label: Demarrage difficile
    severity: confort
  - id: S3
    label: Manque de puissance
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : rates d allumage'
  quick_checks:
  - 'Observer : rates d allumage ?'
  - 'Observer : demarrage difficile ?'
  - 'Observer : manque de puissance ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Rates d allumage
  - Demarrage difficile
  - Manque de puissance
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '683'
  intro_title: A quoi sert Distributeur d'allumage ?
  risk_title: Pourquoi remplacer Distributeur d'allumage a temps ?
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
  - question: Comment choisir Distributeur d'allumage compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Distributeur d'allumage ?
    answer: En cas de rates d allumage ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Distributeur d'allumage sans verification atelier ?
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
doc_id: ca4bb638-03c0-547f-86b5-c155ff80a94f
content_hash: sha256:d5b9075febe289c7
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
  _has_tech_data: true
  types_variants:
  - type: Hall
    source_ref: corpus RAG web OEM
  - type: hall
    source_ref: corpus RAG web OEM
  - type: organique
    source_ref: corpus RAG web OEM
  - type: piézo
    source_ref: corpus RAG web OEM
  - type: plein
    source_ref: corpus RAG web OEM
  - type: électrique
    source_ref: corpus RAG web OEM
  technical_notes:
    val_000_v: 000 V
    val_12_v: 12 v
    val_15__: 15 %
    val_2_litres: 2 litres
    val_20__: 20 %
    val_20_95__: 20,95 %
    val_28_a: 28 a
    val_3_v: 3 v
    val_30__: 30 %
    val_30_bars: 30 bars
    val_33_9__: 33,9 %
    val_35__: 35 %
    val_380__c: 380 °C
    val_40__: 40 %
    val_40_1__: 40,1 %
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le distributeur d''allumage est le composant central du système d''allumage à haute tension sur les moteurs à essence
    équipés d''un allumage à contact ou à rupture. Sa fonction principale est de distribuer la haute tension produite par
    la bobine d''allumage vers chaque bougie dans l''ordre précis imposé par la séquence d''allumage du moteur. Concrètement,
    le distributeur reçoit l''impulsion électrique de la bobine — une tension pouvant atteindre 20 000 à 40 000 volts — et
    la répartit successivement à chacune des bougies grâce à un rotor tournant à l''intérieur d''un chapeau (tête de distributeur).
    Ce rotor est entraîné mécaniquement par l''arbre à cames, ce qui garantit une synchronisation parfaite avec les pistons.
    Sur les moteurs anciens équipés de rupteurs, le distributeur intègre également le platinoir (rupteur) et le condensateur,
    qui pilotent directement l''alimentation primaire de la bobine. Sur les versions à allumage électronique, le distributeur
    conserve sa fonction de répartition haute tension mais délègue le déclenchement à un module électronique ou à un capteur
    à effet Hall. Le distributeur agit donc comme un chef d''orchestre de la combustion : il transmet l''énergie d''allumage,
    répartit cette énergie dans le bon ordre et au bon moment, et assure la répétabilité de cette séquence à chaque cycle
    moteur. Une défaillance de ce composant perturbe immédiatement la combustion et se traduit par des ratés, une perte de
    puissance ou l''impossibilité de démarrer.'
  S2: 'Un distributeur d''allumage en fin de vie ou défectueux se manifeste par des symptômes moteur caractéristiques. Ces
    signaux apparaissent progressivement et s''aggravent si aucune intervention n''est effectuée. Voici les signes à surveiller
    : - Ratés d''allumage à froid ou à chaud : le moteur hoquette, manque de régularité ou présente des à-coups lors de l''accélération.
    C''est souvent le premier symptôme visible d''un distributeur usé ou d''une tête de distributeur fissurée. - Démarrage
    difficile ou impossible : le moteur tourne sans démarrer, ou démarre laborieusement après plusieurs tentatives, signe
    que la haute tension n''atteint plus correctement les bougies. - Manque de puissance manifeste : le véhicule accélère
    avec difficulté, notamment en charge ou en côte, du fait d''une combustion incomplète liée à un allumage défaillant. -
    Consommation de carburant anormalement élevée : les ratés de combustion obligent le calculateur à enrichir le mélange,
    ce qui augmente la consommation sans gain de performance. - Vibrations et tremblement du moteur au ralenti : un ou plusieurs
    cylindres ne s''allument pas correctement, provoquant un déséquilibre mécanique perceptible sur la carrosserie et le bloc
    moteur. - Odeur de carburant non brûlé à l''échappement : la combustion incomplète entraîne un rejet d''essence crue,
    avec une odeur caractéristique et parfois de la fumée noire. - Fissures visibles sur la tête de distributeur : à l''inspection
    visuelle, des craquelures ou dépôts de corrosion sur le chapeau de distributeur indiquent un composant à remplacer sans
    délai.'
  S3: 'Le distributeur d''allumage est une pièce dont la compatibilité est strictement spécifique au véhicule. Une erreur
    de référence entraîne un allumage incorrect et un moteur qui ne démarre pas. Voici les critères déterminants pour sélectionner
    la bonne référence : - Marque et modèle du véhicule : la première étape indispensable. Chaque constructeur utilise des
    architectures d''allumage spécifiques, et le distributeur doit correspondre exactement au modèle concerné. - Année de
    fabrication : un même modèle peut avoir subi des évolutions de motorisation ou de système d''allumage en cours de carrière.
    L''année de production détermine la génération exacte du composant. - Type de motorisation (cylindrée, nombre de cylindres)
    : le nombre de sorties haute tension sur la tête de distributeur doit correspondre au nombre de cylindres du moteur (4,
    6, 8 cylindres). - Type d''allumage (platinoir ou électronique) : un distributeur avec rupteur mécanique n''est pas interchangeable
    avec un distributeur à allumage électronique. Vérifier le type d''allumage d''origine. - Vérification de la référence
    OEM : l''idéal est de relever le numéro gravé sur l''ancien distributeur et de le croiser avec les références constructeur
    pour s''assurer d''une compatibilité exacte. - État de la tête de distributeur et du rotor : lors du remplacement du distributeur,
    prévoir également le remplacement systématique de la tête de distributeur et du rotor, qui s''usent conjointement. - Origine
    de la pièce (OE ou OES) : pour les systèmes d''allumage, privilégier les fabricants équipementiers reconnus (Bosch, Beru,
    Facet) dont la qualité de fabrication garantit la précision de la répartition de l''étincelle. Pour aller plus loin :
    consultez notre guide d''achat distributeur d''allumage — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 'Le remplacement d''un distributeur d''allumage requiert une grande précision pour respecter le calage de l''allumage.
    Une erreur dans la position du distributeur au remontage entraîne un démarrage impossible ou un allumage décalé. Voici
    la procédure à suivre : - Préparer et sécuriser le véhicule : couper le contact, débrancher la borne négative de la batterie.
    Laisser le moteur refroidir si une intervention récente a eu lieu. - Repérer la position exacte du distributeur : avant
    toute dépose, marquer au feutre ou à la craie la position du rotor par rapport au corps du distributeur, et la position
    du corps par rapport au bloc moteur. Ces repères sont indispensables pour le remontage à l''identique. - Débrancher les
    fils haute tension : noter ou photographier l''ordre de branchement des fils de bougie sur la tête de distributeur avant
    de les déconnecter un par un. Ne jamais les inverser. - Déconnecter le câble d''alimentation basse tension : débrancher
    le connecteur du module électronique ou les fils du platinoir selon le type de distributeur. - Déposer le chapeau (tête)
    de distributeur : retirer les clips ou vis de fixation, puis soulever délicatement la tête de distributeur sans forcer.
    - Dévisser et extraire le corps du distributeur : retirer la vis de serrage du collier ou l''écrou de fixation, puis extraire
    le corps du distributeur en le tirant axialement. Ne pas faire tourner le moteur pendant cette opération. - Poser le nouveau
    distributeur : introduire le nouveau distributeur en alignant les repères préalablement tracés. S''assurer que l''entraînement
    (pignon hélicoïdal ou axe) s''engage correctement dans l''arbre à cames. - Reserrer le collier de fixation, rebrancher
    les connexions : rebrancher le câble basse tension, reposer la tête de distributeur, rebrancher les fils haute tension
    dans l''ordre noté. - Reconnecter la batterie et démarrer : vérifier le calage d''allumage à la lampe stroboscopique si
    nécessaire, puis corriger la position angulaire du distributeur jusqu''à obtenir le bon calage spécifié par le constructeur.'
  S4_REPOSE: 'Le remontage du distributeur d''allumage est l''étape la plus critique de toute l''intervention : un calage
    décalé ne permet pas le démarrage ou provoque une surcharge du circuit d''allumage. Voici les étapes dans l''ordre exact
    à respecter : - Vérifier que le moteur n''a pas bougé depuis la dépose : s''assurer qu''aucune manœuvre n''a fait tourner
    le vilebrequin pendant que le distributeur était déposé. Si le moteur a tourné, il faut retrouver le point mort haut (PMH)
    du cylindre 1 en compressions, puis repositionner le rotor en conséquence avant la pose. - Contrôler l''état du joint
    d''étanchéité de la base du distributeur : remplacer le joint torique ou le joint plat de la base du distributeur si le
    kit de remplacement en fournit un neuf. Un joint usé provoquerait une fuite d''huile à l''emplacement du distributeur.
    - Engager le nouveau distributeur en alignant les repères préalablement tracés : introduire l''axe du distributeur dans
    le corps de l''arbre à cames (ou la pompe à huile selon le moteur) en alignant soigneusement les marques faites avant
    la dépose. L''entraînement à pignon hélicoïdal provoque une rotation du rotor lors de l''enfoncement : anticiper ce décalage
    angulaire tel qu''indiqué dans la documentation constructeur. - Vérifier l''engagement complet de l''entraînement : le
    distributeur doit s''enfoncer jusqu''à la bride d''appui sans forcer. Si le distributeur résiste, l''entraînement est
    mal engagé — ne pas forcer, retirer et repositionner. - Serrer provisoirement le collier de fixation : visser le boulon
    de collier suffisamment pour maintenir le distributeur en place tout en permettant une rotation fine pour le calage d''allumage.
    Ne pas bloquer définitivement avant le calage. - Reposer la tête de distributeur et les fils haute tension : remettre
    le chapeau de distributeur, fixer les clips ou vis de maintien. Reconnecter les fils haute tension sur les bougies dans
    l''ordre exact d''origine (se référer à la photographie prise avant la dépose). L''ordre d''allumage est critique — une
    inversion de deux fils provoque des rates sévères. - Reconnecter le câble basse tension du module électronique : rebrancher
    le connecteur du module ou les fils du platinoir selon le type de distributeur. Reconnecter la borne négative de la batterie.
    - Vérifier et ajuster le calage d''allumage à la lampe stroboscopique : démarrer le moteur et brancher la lampe stroboscopique
    sur le fil de la bougie numéro 1. Pointer la lampe sur le repère de calage du vilebrequin. Faire tourner légèrement le
    distributeur jusqu''à obtenir le calage prescrit par le constructeur (exprimé en degrés avant PMH). Bloquer définitivement
    le collier au couple constructeur. - Effectuer un test routier et contrôler l''absence de rates : réaliser un essai en
    conditions variées (ralenti, accélération franche, régime stabilisé). L''absence totale de rates, la souplesse de la montée
    en régime et la consommation normale confirment un calage correct.'
  S5: 'Le remplacement d''un distributeur d''allumage est une opération délicate où plusieurs erreurs fréquentes peuvent compromettre
    le démarrage ou endommager le moteur. Voici les pièges à éviter absolument : - Oublier de repérer la position du rotor
    avant la dépose : sans marque de référence, il est impossible de replacer le distributeur dans sa position d''origine.
    Conséquence directe : un calage d''allumage erroné, un moteur qui ne démarre pas ou qui cliquète sous charge. - Intervertir
    les fils haute tension au remontage : chaque fil de bougie correspond à un cylindre précis dans l''ordre d''allumage.
    Les inverser provoque des ratés graves, des retours de flamme à l''admission ou des dommages au catalyseur. - Monter un
    distributeur sans vérifier le type d''allumage : confondre un distributeur à platinoir avec un distributeur à allumage
    électronique conduit à une pièce incompatible que le système ne peut pas piloter correctement. - Ne pas remplacer la tête
    de distributeur et le rotor simultanément : ces pièces d''usure s''usent conjointement. Monter un distributeur neuf avec
    une tête usée ou fissurée annule le bénéfice du remplacement et provoque de nouveaux ratés d''allumage. - Faire tourner
    le moteur pendant la dépose du distributeur : si le moteur tourne sans distributeur ou avec une position incorrecte du
    rotor, le repère de calage est perdu et il faut repositionner le moteur au PMH (Point Mort Haut) du cylindre 1 avant de
    poser le nouveau distributeur.'
  S6: 'Après la pose d''un distributeur d''allumage, plusieurs contrôles doivent être effectués pour confirmer que l''allumage
    est correct et que le moteur fonctionne dans les paramètres constructeur. Ces vérifications évitent une remise en route
    prématurée avec un calage erroné : - Contrôle du calage d''allumage à la lampe stroboscopique : avec le moteur au ralenti,
    pointer la lampe stroboscopique sur le repère de vilebrequin et vérifier que l''avance correspond à la valeur spécifiée
    par le constructeur (généralement entre 5° et 15° avant PMH selon le moteur). - Absence de ratés au ralenti et en accélération
    : le moteur doit tourner régulièrement sans à-coups, hoquets ou tremblements. Des ratés résiduels après remplacement indiquent
    un calage insuffisant ou un fil haute tension mal connecté. - Démarrage à froid et à chaud sans anomalie : tester le démarrage
    après une nuit complète (à froid) et après un trajet (à chaud) pour s''assurer de la fiabilité du nouveau distributeur
    dans toutes les conditions thermiques. - Vérification visuelle des connexions haute tension : s''assurer que tous les
    fils de bougies sont fermement enclipsés sur la tête de distributeur et sur chaque bougie. Un fil déboîté provoque un
    raté permanent sur le cylindre concerné. - Contrôle de l''absence de codes défaut : brancher un outil de diagnostic OBD
    pour vérifier qu''aucun code de raté d''allumage (P0300 à P030X) n''est mémorisé après le premier parcours de validation.'
  S7: 'Le distributeur d''allumage distribue la haute tension aux bougies. Son remplacement est l''occasion de vérifier l''ensemble
    du circuit d''allumage : - Bobine d''allumage — génère la haute tension envoyée au distributeur. Une bobine en fin de
    vie (résistance hors spécification) provoque des rates d''allumage même avec un distributeur neuf. Mesurer la résistance
    primaire et secondaire de la bobine à l''ohmmètre avant de conclure à un distributeur défaillant. - Faisceau d''allumage
    — fils haute tension entre la tête de distributeur et les bougies. Les fils se dégradent avec les cycles thermiques :
    fissures d''isolant, résistance interne augmentée. Remplacer l''ensemble fils-bougies lors du remplacement du distributeur.
    - Bougies d''allumage — dernier maillon de la chaîne d''allumage. Des bougies usées (électrodes érodées, écartement hors
    spécification) annulent le bénéfice d''un distributeur neuf. Le remplacement simultané est systématiquement recommandé.
    - Rotor et chapeau de distributeur — s''ils ne sont pas compris dans le kit distributeur, inspecter l''état du rotor (fissures,
    arc électrique) et du chapeau (oxydation des plots de contact, fissures radiales) et les remplacer si nécessaire.'
  S8: Quelle est la durée de vie d'un distributeur d'allumage ? Il n'existe pas de kilométrage fixe pour le remplacement d'un
    distributeur d'allumage, car cela dépend fortement du type de moteur, des conditions d'utilisation et de la qualité de
    la pièce d'origine. Sur la plupart des véhicules équipés de ce système, la tête de distributeur et le rotor se remplacent
    tous les 30 000 à 60 000 km dans le cadre de l'entretien courant. Le corps du distributeur lui-même dure souvent plus
    longtemps, mais doit être remplacé dès apparition de ratés persistants ou de jeu dans l'axe. Peut-on rouler avec un distributeur
    défaillant ? Non, il ne faut pas continuer à rouler avec un distributeur en panne. Les ratés d'allumage envoyent de l'essence
    non brûlée dans le pot catalytique, ce qui peut le détruire en quelques dizaines de kilomètres — une réparation bien plus
    coûteuse que le distributeur lui-même. De plus, un moteur qui rate d'allumage de façon répétée produit des contraintes
    mécaniques anormales et peut endommager les joints et les pistons sur le long terme. Comment choisir le bon distributeur
    d'allumage pour mon véhicule ? Renseignez la marque, le modèle, l'année et le type de motorisation de votre véhicule.
    Vérifiez le nombre de cylindres pour sélectionner une tête de distributeur avec le bon nombre de sorties haute tension.
    Relevez si possible le numéro de référence gravé sur l'ancien distributeur pour croiser la compatibilité avec les références
    équipementiers (Bosch, Beru, Facet). Évitez les pièces présentées comme "universelles" ou "adaptables" — le distributeur
    d'allumage est une pièce strictement spécifique au moteur. Faut-il régler le calage après un remplacement de distributeur
    ? Oui, dans la quasi-totalité des cas. Même en remplaçant le distributeur dans la position exacte de l'ancien, un contrôle
    du calage à la lampe stroboscopique est indispensable. La tolérance mécanique des pièces peut introduire un écart de quelques
    degrés d'avance, suffisant pour dégrader les performances ou provoquer des cliquetis. Le calage correct est indiqué dans
    la documentation technique du véhicule ou sur l'étiquette sous le capot.
  META: '{"meta_title":"Distributeur d''allumage : symptômes et remplacement | AutoMecanik","meta_description":"Ratés d''allumage,
    démarrage difficile, manque de puissance : reconnaître un distributeur défaillant et savoir quand le remplacer sur moteur
    essence.","og_title":"Distributeur d''allumage défaillant : 3 signes clés","og_description":"Ratés moteur ou démarrage
    difficile ? Le distributeur transmet la haute tension aux bougies. Découvrez quand et comment le remplacer sur votre vehicule.","sources":[{"type":"rag","ref":"gammes/distributeur-d-
    allumage.md","field":"diagnostic.symptoms,domain.role,rendering.faq"}]}'
---

# Distributeur d'allumage - Guide Diagnostic Complet

## Fonction et Rôle

Distribuer la haute tension aux bougies dans l'ordre d'allumage

**Actions principales:** distribuer, repartir, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- rates d allumage
- demarrage difficile
- manque de puissance

## Procédure de Diagnostic

Pour diagnostiquer un problème de distributeur d'allumage:

1. **Inspection visuelle** - Examiner l'état du distributeur d'allumage
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

- bobine-d-allumage
- faisceau-d-allumage
- bougie-d-allumage

## Critères de Compatibilité

Pour commander le bon distributeur d'allumage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "demarrage instantane"

## FAQ

**Comment choisir Distributeur d'allumage compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Distributeur d'allumage ?**
En cas de rates d allumage ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Distributeur d'allumage sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
