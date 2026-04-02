---
category: eclairage
slug: relais-de-clignotant
title: Relais de clignotant
pg_id: 61
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
  last_enriched_by: skill:phase5-vague6
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Commande le clignotement intermittent des feux de direction
  must_be_true:
  - commander
  - activer
  - cadencer
  must_not_contain:
  - ampoule
  - feu
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
  brands:
    premium:
    - Hella
    - Bosch
    - Continental/VDO
    standard:
    - Febi Bilstein
    - SWAG
    - Valeo
    budget:
    - Meat & Doria
    - ERA
    - Herth+Buss
  quality_tiers:
  - tier: Origine constructeur (OE/OES)
    description: Relais identique a celui monte en usine. Cadence de clignotement conforme, compatible avec le systeme de
      signalisation d'origine.
  - tier: Equivalent OE (qualite premiere monte)
    description: Relais de qualite equivalente. Cadence et brochage conformes aux specifications constructeur.
  - tier: Adaptable (qualite atelier courant)
    description: Relais compatible. Verifier le nombre de broches et la cadence de clignotement avant montage.
diagnostic:
  symptoms:
  - id: S1
    label: Clignotants ne fonctionnent pas
    severity: confort
  - id: S2
    label: Clignotement trop rapide
    severity: confort
  - id: S3
    label: Clignotement irregulier
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : clignotants ne fonctionnent pas'
  quick_checks:
  - 'Observer : clignotants ne fonctionnent pas ?'
  - 'Observer : clignotement trop rapide ?'
  - 'Observer : clignotement irregulier ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Clignotants ne fonctionnent pas
  - Clignotement trop rapide
  - Clignotement irregulier
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '61'
  intro_title: A quoi sert Relais de clignotant ?
  risk_title: Pourquoi remplacer Relais de clignotant a temps ?
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
  - question: Comment choisir Relais de clignotant compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Relais de clignotant ?
    answer: En cas de clignotants ne fonctionnent pas ou de degradation mesurable, il faut controler rapidement avant panne
      secondaire.
  - question: Puis-je monter Relais de clignotant sans verification atelier ?
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
doc_id: 67fe4426-2646-529b-a086-d904c8ae938e
content_hash: sha256:9358072a14c379c4
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
  _source: contenu LLM — a revalider contre sources OEM
  _validation_status: pending_oem_validation
  _enriched_at: '2026-03-30'
  technical_notes:
    clignotement_rapide: 'ampoule grillee sur le circuit = la resistance baisse = le relais accelere'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le relais de clignotant est un composant électrique central du système de
    signalisation lumineuse. Sa mission est de cadencer le clignotement
    intermittent des feux de direction — feux avant, arrière et latéraux — à une
    fréquence réglementaire, généralement comprise entre 60 et 120 clignotements
    par minute selon les normes constructeur. Concrètement, le relais reçoit
    l'ordre électrique provenant du commodo de direction (la manette de
    clignotant sur la colonne de direction) et active ou désactive le circuit
    des feux de direction de façon rythmée. Il intègre un mécanisme temporisé —
    électronique sur les véhicules modernes, thermobimétallique sur les anciens
    — qui découpe le courant pour produire ce clignotement caractéristique. Sur
    les architectures électroniques récentes, le relais est souvent intégré au
    boîtier de signalisation (BSI/BCM) et communique via le réseau CAN. Sur les
    véhicules plus anciens, il s'agit d'un composant autonome, facilement
    accessible, généralement positionné dans le tableau de bord ou le boîtier de
    fusibles. Un relais de clignotant défaillant perturbe directement la
    signalisation des changements de direction, ce qui constitue une anomalie
    détectable au contrôle technique et représente un risque pour les autres
    usagers de la route. Sa surveillance et son remplacement dès les premiers
    signes de défaillance sont des actes de maintenance indispensables.
  S2: >-
    Un relais de clignotant qui commence à défaillir manifeste des signes
    spécifiques à identifier rapidement. Ces anomalies apparaissent
    progressivement, souvent aggravées par les cycles de chaud/froid ou
    l'humidité. Voici les principaux signaux d'alerte à surveiller : -
    Clignotants qui ne fonctionnent plus du tout : le feu de direction reste
    fixe ou éteint lors de l'activation de la manette — symptôme le plus grave,
    à corriger immédiatement. - Clignotement anormalement rapide (hyperflash) :
    la fréquence double ou triple par rapport à la normale, souvent accompagné
    d'un claquement accéléré dans l'habitacle — signe classique d'un relais
    défaillant ou d'une ampoule grillée sur le circuit. - Clignotement
    irrégulier ou saccadé : la cadence oscille de façon imprévisible, parfois
    lente, parfois rapide, sans cohérence — indique une résistance interne
    instable dans le relais. - Feux de direction qui restent allumés en fixe :
    le relais ne parvient plus à interrompre le circuit, maintenant le courant
    en permanence. - Absence de signal sonore de clignotant dans l'habitacle
    alors que le mécanisme est activé — le tic-tac électronique ou thermique ne
    se produit plus. - Voyant d'alerte au tableau de bord : sur les véhicules
    récents, le BSI détecte l'incohérence et allume un témoin de défaut circuit
    éclairage. - Fonctionnement aléatoire selon la température : le relais
    fonctionne normalement à froid mais se dérègle dès que l'habitacle chauffe,
    ou inversement — caractéristique d'un composant en fin de vie.
  S3: >-
    La sélection d'un relais de clignotant doit être conduite avec rigueur, car
    une pièce inadaptée peut créer des dysfonctionnements électroniques ou des
    incompatibilités avec le réseau CAN du véhicule. Voici les critères
    déterminants à vérifier avant toute commande : - Marque et modèle du
    véhicule : le relais est spécifique à chaque plateforme constructeur — un
    relais Renault Clio ne s'adapte pas à une Peugeot 208, même de génération
    identique. - Année de mise en circulation : un même modèle peut avoir subi
    des révisions électroniques en cours de série, modifiant la référence du
    relais à utiliser. - Type de motorisation et niveau de finition : certains
    équipements (feux de direction LED, régulateur de vitesse) modifient les
    exigences électriques du circuit clignotant. - Référence constructeur ou
    équipementier : toujours croiser la référence OEM (d'origine) avec la
    référence équipementier pour confirmer l'interchangeabilité exacte. -
    Symptôme constaté avant commande : si le clignotement est trop rapide
    (hyperflash), vérifier d'abord l'ensemble des ampoules avant de remplacer le
    relais — une ampoule grillée produit exactement le même symptôme. - Type de
    technologie d'éclairage : sur les véhicules post-2010 avec éclairage LED
    intégré de série, un relais spécifique LED est requis pour maintenir la
    bonne fréquence de clignotement réglementaire. - Éviter les produits sans
    référence précise : un relais vendu comme adaptable présente un risque de
    dysfonctionnement élevé sur les architectures électroniques modernes avec
    réseau CAN multiplexé. Pour aller plus loin : consultez notre guide d'achat
    relais de clignotant — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    Le remplacement d'un relais de clignotant est généralement accessible sans
    outillage spécialisé sur les véhicules anciens. Sur les architectures
    modernes avec BSI intégré, l'intervention nécessite de ne pas perturber le
    réseau électronique. Voici la procédure générale à suivre : - Couper le
    contact et attendre 2 à 3 minutes pour laisser se décharger les
    condensateurs du réseau CAN du véhicule. - Déconnecter la borne négative de
    la batterie pour éviter tout court-circuit lors de la manipulation des
    connecteurs électriques. - Localiser le relais de clignotant : consulter le
    schéma électrique du véhicule ou le couvercle du boîtier de fusibles, qui
    indique l'emplacement de chaque relais avec un pictogramme codifié. -
    Accéder au boîtier de fusibles (sous tableau de bord côté conducteur, dans
    l'habitacle ou dans le compartiment moteur selon le modèle) en retirant le
    cache protecteur. - Extraire le relais défaillant en le tirant fermement à
    la verticale — sur certains modèles, un outil extracteur de relais est
    nécessaire pour éviter de déformer les connecteurs du socket. - Vérifier
    l'état du support : contrôler les broches du socket, l'absence d'oxydation
    ou de traces de brûlures sur les contacts avant d'insérer le nouveau relais.
    - Insérer le nouveau relais en alignant les broches avec le socket et en
    poussant jusqu'au clic d'enclenchement — ne jamais forcer si l'orientation
    ne semble pas correcte. - Reconnecter la batterie et tester le
    fonctionnement des clignotants avant/arrière gauche et droit, ainsi que les
    feux de détresse (warning).
  S4_REPOSE: >-
    Repose du relais de clignotant Le remontage du relais de clignotant est une
    opération rapide, mais quelques vérifications préalables évitent une
    récidive de panne ou un clignotement irrégulier après remplacement.
    Préparation avant repose - Comparez le nouveau relais avec l'ancien : le
    nombre de broches, la disposition et la référence doivent correspondre
    exactement à ce que préconise le schéma électrique du véhicule - Vérifiez
    l'état du connecteur : broches non oxydées, aucun fil coupé ou denudé, clip
    de verrouillage intact - Si un nettoyant contact électrique a été utilisé
    lors de la dépose, attendez que le produit soit totalement évaporé avant de
    remonter - Contrôlez que la cavité du boîtier relais ou du porte-fusibles
    est propre et sèche Étapes de remontage - Orientation du relais — repérez le
    chanfrein ou la forme détrompeur sur le relais et alignez-le avec la cavité
    correspondante dans le boîtier ; ne forcez jamais si le relais résiste à
    l'insertion - Enclenchement — poussez fermement le relais jusqu'au fond de
    sa cavité, un léger clic doit se faire entendre ou sentir - Vérification de
    la fixation — sur certains véhicules, le relais est maintenu par une vis ou
    un clip supplémentaire ; remettez-le en place - Reconnexion de la batterie —
    reconnectez la borne négative en dernier, serrez le collier de borne sans
    excès (6 à 8 Nm) Contrôles fonctionnels après repose - Activez les
    clignotants gauche et droit : chaque côté doit clignoter au rythme standard
    (environ 60 à 120 clignotements par minute selon norme) - Vérifiez le
    clignotant de détresse (warning) : les quatre feux doivent clignoter de
    façon synchronisée - Si le clignotement reste trop rapide d'un côté, cela
    indique une ampoule grillée ou une LED de remplacement non adaptée —
    vérifiez chaque feu de direction sur ce côté - Contrôlez le témoin de
    clignotant au tableau de bord : il doit être synchronisé avec les feux
    extérieurs
  S5: >-
    Certaines erreurs récurrentes lors du diagnostic ou du remplacement du
    relais de clignotant peuvent conduire à des interventions inutiles ou à une
    récidive rapide de la panne. Voici les cinq erreurs à éviter absolument : -
    Remplacer le relais sans vérifier les ampoules au préalable : un
    clignotement trop rapide est dans la majorité des cas dû à une ampoule
    grillée sur le circuit, et non au relais lui-même — contrôler toutes les
    ampoules (avant, arrière, répétiteurs latéraux) avant toute dépose du
    relais. - Monter un relais sans vérification de référence sur un véhicule
    récent : les architectures BSI modernes nécessitent un relais exactement
    conforme à la référence constructeur, sous peine de générer des codes
    défauts électroniques ou un fonctionnement erratique du circuit de
    signalisation. - Travailler sur le circuit électrique sans couper la
    batterie : manipuler les connecteurs du relais sous tension peut provoquer
    un court-circuit et endommager le BSI, représentant un coût de réparation
    nettement supérieur au relais lui-même. - Négliger l'état des contacts du
    socket : un socket oxydé ou légèrement déformé ne garantit pas un contact
    électrique fiable avec le nouveau relais — nettoyer les contacts au spray
    désoxydant ou remplacer le support si nécessaire. - Confondre le relais de
    clignotant avec un fusible : les deux composants se ressemblent visuellement
    dans certains boîtiers, mais leur fonction est radicalement différente —
    toujours consulter le schéma de repérage sur le couvercle du boîtier avant
    toute extraction.
  S6: >-
    Après le montage du nouveau relais de clignotant, une série de contrôles
    doit être effectuée pour confirmer le bon fonctionnement de l'ensemble du
    circuit de signalisation avant de reprendre la route : - Tester les
    clignotants gauche et droit : activer successivement chaque côté et vérifier
    que la fréquence de clignotement est normale (1 à 2 fois par seconde) tant à
    l'avant qu'à l'arrière, y compris les répétiteurs latéraux si présents. -
    Tester les feux de détresse (warning) : activer le bouton de détresse et
    contrôler que les 4 feux clignotent simultanément et de façon parfaitement
    synchronisée. - Vérifier le signal sonore dans l'habitacle : le tic-tac doit
    être audible et régulier, à cadence identique pour les deux côtés gauche et
    droit. - Contrôler l'absence de voyant d'alerte au tableau de bord : sur les
    véhicules avec surveillance électronique du circuit, aucun témoin de défaut
    éclairage ne doit rester allumé après l'intervention. - Inspecter
    visuellement l'ensemble des feux de direction : confirmer que toutes les
    ampoules fonctionnent, y compris les feux latéraux (répétiteurs d'aile) si
    le véhicule en est équipé.
  S7: >-
    Pièces à vérifier lors du remplacement du relais de clignotant Le relais de
    clignotant cadence l'alimentation électrique des feux de direction. Sa
    défaillance est souvent liée à des composants en aval. Vérifiez ces pièces
    pour un diagnostic complet. - Feux clignotants (avant et arrière) Un
    clignotant grillé modifie la résistance du circuit et peut provoquer un
    clignotement accéléré ou irrégulier que l'on attribue à tort au relais.
    Contrôlez chaque ampoule avant de remplacer le relais, en particulier sur
    les véhicules équipés d'ampoules conventionnelles (pas de LED). Sur les
    véhicules récents avec feux LED intégrés, un bloc optique défaillant peut
    simuler une panne de relais. Voir les feux clignotants - Ampoules feux
    clignotants Le remplacement d'une ampoule incandescente par une ampoule LED
    sans résistance de charge peut causer un hyperclignotement (clignotement
    trop rapide). Si vous montez des LED, assurez-vous qu'elles intègrent une
    résistance adaptée ou que le relais est compatible LED. Une ampoule de
    mauvaise puissance (wattage incorrect) perturbe également le cadencement.
    Voir les ampoules feux clignotants
  S8: >-
    Pourquoi mes clignotants clignotent-ils deux fois plus vite que d'habitude ?
    Ce phénomène, appelé hyperflash, se produit lorsque la résistance totale du
    circuit de direction est réduite de façon anormale. La cause la plus
    fréquente est une ampoule grillée d'un côté : le relais détecte une
    consommation électrique insuffisante et accélère sa cadence pour signaler le
    défaut. Commencez toujours par vérifier l'ensemble des ampoules (avant,
    arrière, répétiteur latéral) avant d'envisager le remplacement du relais
    lui-même. Comment savoir si c'est le relais ou le commodo qui est en cause ?
    Si le dysfonctionnement concerne les deux côtés (clignotant gauche ET droit
    simultanément défaillants), le relais est la cause la plus probable. Si un
    seul côté est affecté, la panne provient plutôt d'une ampoule grillée, d'un
    fil coupé ou d'un contact oxydé côté commodo. Un test avec un multimètre sur
    les broches du relais permet de confirmer le diagnostic en quelques minutes.
    Peut-on rouler avec un relais de clignotant défaillant ? Techniquement le
    véhicule roule, mais des clignotants non fonctionnels constituent une
    infraction au code de la route et un risque d'accident grave, notamment lors
    des changements de voie ou des manoeuvres. Un feu de direction inopérant est
    également un motif de refus au contrôle technique. L'intervention doit être
    réalisée sans délai. Comment choisir le bon relais de clignotant pour mon
    véhicule ? Renseignez impérativement la marque, le modèle exact, l'année de
    mise en circulation et le type de motorisation. Sur les véhicules équipés de
    feux LED de série, un relais spécifique LED est obligatoire pour maintenir
    la fréquence de clignotement conforme. Croisez toujours la référence du
    relais d'origine (étiquetée sur l'ancien relais ou dans la documentation
    technique) avec la référence de la pièce de remplacement.
---

# Relais de clignotant - Guide Diagnostic Complet

## Fonction et Rôle

Commande le clignotement intermittent des feux de direction

**Actions principales:** commander, activer, cadencer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- clignotants ne fonctionnent pas
- clignotement trop rapide
- clignotement irregulier

## Procédure de Diagnostic

Pour diagnostiquer un problème de relais de clignotant:

1. **Inspection visuelle** - Examiner l'état du relais de clignotant
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

- feu-clignotant
- ampoule-feu-clignotant

## Critères de Compatibilité

Pour commander le bon relais de clignotant, vous devez connaître:

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

**Comment choisir Relais de clignotant compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Relais de clignotant ?**
En cas de clignotants ne fonctionnent pas ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Relais de clignotant sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
