---
category: capteurs
slug: interrupteur-des-feux-de-freins
title: Interrupteur des feux de freins
pg_id: 806
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
  role: Detecte l'appui sur la pedale de frein pour activer les feux stop
  must_be_true:
  - detecter
  - signaler
  - activer
  must_not_contain:
  - reparation
  - regeneration
  - nettoyage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - disque-de-frein
  - plaquette-de-frein
  - etrier-de-frein
  - flexible-de-frein
  - maitre-cylindre-de-frein
  - liquide-de-frein
  confusion_with:
  - term: piece-de-freinage-voisine
    difference: 'Verifier la reference exacte : les pieces de freinage se ressemblent mais ne sont pas interchangeables entre
      essieux ou types de montage.'
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
  - ❌ "meilleur freinage"
  cost_range:
    min: 10
    max: 35
    currency: EUR
    unit: pièce
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    description: Interrupteur identique à l'origine. Recommandé sur véhicules récents avec fonctions multiples (ESP, régulateur
      adaptatif, boîte automatique).
  - tier: Équivalent OE (OES)
    description: Fabricants comme Bosch, TRW ou Febi proposent des interrupteurs équivalents OE. Compatibilité électrique
      et mécanique vérifiée sur les principaux modèles.
  - tier: Adaptable (aftermarket)
    description: Le marché aftermarket couvre bien ce segment pour un usage standard. Vérifier que le nombre de circuits correspond
      (certains interrupteurs ont 2 ou 3 circuits).
  brands:
    premium:
    - Brembo
    - ATE
    - TRW
    standard:
    - Bosch
    - Ferodo
    - Textar
    budget:
    - Ridex
    - Valeo
diagnostic:
  symptoms:
  - id: S1
    label: Feux stop qui restent allumes moteur eteint
    severity: confort
  - id: S2
    label: Feux stop qui ne s allument plus du tout
    severity: confort
  - id: S3
    label: Regulateur de vitesse qui ne fonctionne plus
    severity: confort
  - id: S4
    label: Message d erreur systeme esp au tableau de bord
    severity: securite
  - id: S5
    label: Batterie decharge feux stop restes
    severity: confort
  - id: S6
    label: Clic audible absent quand on appuie sur la pedale
    severity: securite
  - id: S7
    label: Odeur de plastique brule court-circuit
    severity: confort
  - id: S8
    label: Plus de 150 000 km sans verification
    severity: confort
  causes:
  - remplacement preventif recommande
  - 'kilometrage eleve ou usure visible : remplacement preventif recommande'
  - 'Usure ou defaillance causant : feux stop qui restent allumes moteur eteint'
  quick_checks:
  - 'Observer : feux stop qui restent allumes moteur eteint ?'
  - 'Observer : feux stop qui ne s allument plus du tout ?'
  - 'Observer : regulateur de vitesse qui ne fonctionne plus ?'
  - 'Observer : message d erreur systeme esp au tableau de bord ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Feux stop qui restent allumes moteur eteint
  - Feux stop qui ne s allument plus du tout
  - Regulateur de vitesse qui ne fonctionne plus
  - Message d erreur systeme esp au tableau de bord
  - Batterie decharge feux stop restes
  - Clic audible absent quand on appuie sur la pedale
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '806'
  intro_title: A quoi sert Interrupteur des feux de freins ?
  risk_title: Pourquoi remplacer Interrupteur des feux de freins a temps ?
  risk_explanation: '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
  risk_consequences:
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
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
  - question: Interrupteur feux stop OE ou adaptable ?
    answer: Les interrupteurs adaptables fonctionnent bien pour un usage standard. L'OE est recommandé sur véhicules récents
      avec fonctions multiples (ESP, régulateur).
  - question: Comment savoir si mon interrupteur de feux stop est HS ?
    answer: Feux stop qui restent allumés en permanence, ou qui ne s'allument plus du tout. Le régulateur de vitesse peut
      aussi ne plus fonctionner.
  - question: Peut-on tester l'interrupteur de feux stop ?
    answer: Oui avec un multimètre. Vérifiez la continuité quand la pédale est enfoncée. Ou observez les feux stop pendant
      qu'un assistant appuie sur la pédale.
  - question: Peut-on changer l'interrupteur de feux stop soi-même ?
    answer: Oui, très simple. Accès sous le tableau de bord, derrière la pédale de frein. Quart de tour pour déverrouiller.
      10 minutes suffisent.
  - question: Quelle erreur éviter avec l'interrupteur de feux stop ?
    answer: Vérifier le réglage après montage (feux doivent s'allumer dès le début de course pédale). Attention au sens de
      montage sur certains modèles.
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
doc_id: cd3ee0a9-5be2-50e5-943c-3204d0c35403
content_hash: sha256:6b254fc188500a63
lang: fr
variants:
- name: Piece standard
  aliases:
  - standard
  - OE equivalent
  functional_differences:
  - Qualite equivalente a la monte d origine
  - Compatible avec la majorite des vehicules
- name: Piece performance/sport
  aliases:
  - sport
  - haute performance
  functional_differences:
  - Materiaux haute temperature
  - Pour usage intensif ou sportif
location_on_vehicle:
  area: Au niveau des roues (avant et/ou arriere)
  access: Demontage de la roue necessaire (cric + chandelle)
  adjacent_parts:
  - disque
  - plaquette
  - etrier
  - flexible
installation:
  difficulty: moyen
  time: 30min a 1h par essieu
  tools:
  - cle a douille
  - cle Allen
  - pied a coulisse
  - cle dynamometrique
  prerequisite: Vehicule sur chandelles, roue demontee
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-04'
  _web_files_count: 1
  _has_tech_data: true
  materials:
  - materiau: 'aluminium'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    L'interrupteur des feux de frein est placé derrière la pédale de freinqui
    appuie directement sur son bouton poussoir. Il s'agit la plupart du temps
    d'un bouton-poussoir, équipéd'un ressort de rappel en contact avec la pédale
    de frein. L'interrupteur des feux de frein est nommé aussi contacteur de feu
    destop parce qu'il ouvre ou ferme un circuit électrique. Dés que le
    conducteur appuiesur la pédale de frein, l'interrupteur des feux de frein va
    actionner le boutonpoussoir qui établit un contact entre deux voies
    électriques, pour alimenter lecircuit des feux stop. Le bouton poussoir du
    contacteur des feux de stop estamené par un ressort en position repos et
    coupe le circuit des feux stop désque le conducteur relâche la pédale de
    frein. Il existe trois typesd'interrupteur des feux de frein selon le type
    de commande du contacteur : - Interrupteur des feux de frein mécaniques. -
    Interrupteur des feux de frein hydrauliques. - Interrupteur des feux de
    frein pneumatiques. En savoir plus : interrupteur des feux de freins —
    définition et rôle mécanique 🚨 Bruit Interrupteur des feux de freins :
    causes et diagnostic
  S2: >-
    Ne pas attendre la panne complete pour intervenir. Symptômes d'usure : -
    feux stop qui restent allumes moteur eteint - feux stop qui ne s allument
    plus du tout - regulateur de vitesse qui ne fonctionne plus - message d
    erreur systeme esp au tableau de bord - batterie decharge feux stop restes -
    clic audible absent quand on appuie sur la pedale - odeur de plastique brule
    court-circuit - plus de 150 000 km sans verification - **Message d erreur
    systeme esp au tableau de bord** - **Clic audible absent quand on appuie sur
    la pedale**
  S3: >-
    L'interrupteur des feux de freins est une pièce électrique dont la
    compatibilité dépend à la fois du connecteur, de la plage de tension de
    commutation et de la géométrie de fixation sur la pédale. Un interrupteur
    inadapté peut laisser les feux stop allumés en permanence ou les rendre
    totalement inactifs, deux situations qui génèrent un risque routier immédiat
    et peuvent déclencher des codes défaut sur les systèmes ESP et régulateur de
    vitesse.- Référence constructeur ou équivalence OEM vérifiée —
    L'interrupteur est souvent vendu sous plusieurs références croisées.
    Identifiez la référence d'origine (ex. : 6Q0945511 sur Volkswagen, 4545.G9
    sur Peugeot) et vérifiez la liste des équivalences de l'équipementier
    (Hella, Bosch, Febi) pour confirmer la compatibilité.- Type de connecteur et
    nombre de broches — Les interrupteurs se déclinent en version 2, 3 ou 4
    broches selon que le circuit commande uniquement les feux stop ou pilote
    également le régulateur de vitesse et le système ESP. Comptez les broches
    sur l'ancien interrupteur avant de commander.- Tension de commutation : 12 V
    DC — La quasi-totalité des véhicules de tourisme fonctionnent en 12 V, mais
    vérifiez que l'interrupteur supporte une intensité suffisante pour le
    circuit concerné (généralement 10 A minimum). Les interrupteurs sous-
    dimensionnés brûlent rapidement leurs contacts internes.- Mécanisme
    d'activation : pression ou dépression — Certains interrupteurs s'activent à
    l'enfoncement de la pédale (contact normalement ouvert, NO), d'autres
    s'activent au relâchement (contact normalement fermé, NC). L'inversion de
    ces deux types rend les feux stop systématiquement allumés au repos.-
    Réglage de la longueur d'activation (plongeur) — De nombreux interrupteurs
    modernes disposent d'un plongeur réglable permettant d'ajuster la course
    d'activation après montage. Vérifiez que la pièce choisie offre ce réglage
    si le véhicule requiert une calibration après pose (nécessite souvent un
    déplacement de 2 à 5 mm).- Compatibilité avec les systèmes électroniques
    associés — Sur les véhicules récents, l'interrupteur des feux de freins est
    intégré dans la stratégie du BSI / UCH. Une pièce sans la bonne résistance
    interne peut déclencher des alertes résiduelles même après montage. Vérifiez
    la compatibilité avec le calculateur via la documentation technique du
    véhicule.- Au-delà de 150 000 km — L'interrupteur effectue plusieurs
    milliers d'actionnements par an. Au-delà de 150 000 km sans contrôle, un
    remplacement préventif est cohérent même sans symptôme déclaré, notamment
    lors d'une révision complète du circuit de freinage.Pour aller plus loin :
    consultez notre guide d'achat interrupteur des feux de freins — comparatif
    marques, critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Interrupteur des feux de
    freins pour connaître les spécifications. - Débranchez la batterie. -
    Localisez l'emplacement de l'interrupteur des feux de frein. - Débranchez le
    connecteur électrique de l'interrupteur des feux de frein. - Tournez
    l'interrupteur des feux de frein vers la gauche (à peut prêt 45degrés). -
    Retirez l'interrupteur des feux de frein.
  S4_REPOSE: >-
    La repose de l'interrupteur des feux de frein est une opération courte mais
    qui conditionne la sécurité de plusieurs systèmes en cascade : feux stop,
    régulateur de vitesse, ESP et même le déverrouillage de la sélectrice
    automatique sur certains modèles. Un réglage précis de la garde de pédale
    est obligatoire après montage. - Vérifiez que le nouvel interrupteur des
    feux de frein correspond à la référence constructeur du véhicule. Sur les
    véhicules modernes, l'interrupteur pilote simultanément les feux stop, le
    régulateur de vitesse et le calculateur ESP : une référence inadaptée peut
    désactiver ces fonctions sans déclencher de voyant explicite. - Assurez-vous
    que la pédale de frein est en position repos (non enfoncée) avant d'insérer
    l'interrupteur. La plupart des interrupteurs se règlent automatiquement lors
    du premier appui sur la pédale : introduire l'interrupteur pédale enfoncée
    fausse ce réglage. - Engagez le corps de l'interrupteur dans son support de
    pédalier en poussant le tire-poussoir contre la butée de la pédale de frein,
    puis tournez l'interrupteur de 45 degrés dans le sens horaire pour le
    verrouiller dans son logement. - Tirez doucement l'interrupteur vers
    l'arrière pour vérifier qu'il est correctement verrouillé dans son support.
    Un interrupteur mal encliqueté peut se déloger lors d'un freinage brusque et
    rendre les feux stop inopérants. - Rebranchez le connecteur électrique
    jusqu'au clic de verrouillage. Sur les modèles à deux connecteurs (signal
    stop + signal ESP/régulateur), branchez les deux connecteurs sans les
    inverser — un repérage couleur ou une forme différente vous guide. -
    Rebranchez la batterie (borne + en premier), puis mettez le contact sans
    démarrer le moteur. - Demandez à un assistant de surveiller les feux stop
    arrière depuis l'extérieur du véhicule pendant que vous appuyez
    progressivement sur la pédale de frein. Les feux doivent s'allumer dès le
    début de la course de pédale, sans délai. - Vérifiez que les feux stop
    s'éteignent immédiatement au relâchement de la pédale, sans rester allumés.
    Un interrupteur trop avancé dans son logement maintient les feux allumés en
    permanence et décharge la batterie à l'arrêt. - Si le véhicule est équipé
    d'un régulateur de vitesse, testez-le sur route pour confirmer son
    fonctionnement correct. Contrôlez également l'absence de message d'erreur
    ESP ou ABS dans l'instrumentation de bord. ✅ Après remontage, vérifiez les
    spécifications dans la fiche technique Interrupteur des feux de freins.
  S5: >-
    Erreurs frequentes avec l'interrupteur des feux de freins : - Ne pas
    verifier le reglage de la course du contacteur apres montage — un contacteur
    mal positionne laisse les feux de stop allumes en permanence ou ne les
    allume plus du tout- Oublier de debrancher la batterie avant intervention —
    le circuit des feux est sous tension permanente- Confondre un probleme
    d'ampoule avec un defaut de contacteur — tester d'abord les ampoules et
    fusibles avant de remplacer le contacteur- Ne pas verifier l'etat du
    connecteur electrique — l'oxydation des cosses est la premiere cause de faux
    contact sur ce composant- Ignorer des feux de stop qui restent allumes
    moteur arrete — decharge la batterie et signale un contacteur colle ou mal
    regle
  S6: >-
    L'interrupteur des feux de freins commande à la fois les feux stop, le
    régulateur de vitesse, le système ESP et parfois la gestion de la boîte
    automatique. Après le remplacement, les vérifications suivantes garantissent
    que tous ces systèmes fonctionnent correctement avant de reprendre la route.
    - Réglage de la position de l'interrupteur : l'interrupteur doit être
    positionné de façon à s'activer dès le premier millimètre d'enfoncement de
    la pédale de frein. Trop éloigné, les feux stop ne s'allument pas ; trop
    proche, les feux restent allumés en permanence. Ajuster jusqu'à entendre le
    clic caractéristique à chaque appui. - Test des feux stop à deux personnes :
    demander à quelqu'un d'observer les feux arrière pendant que vous appuyez
    sur la pédale de frein. Les deux feux stop doivent s'allumer simultanément
    dès le premier contact sur la pédale, et s'éteindre immédiatement à son
    relâchement. - Vérification avec le moteur coupé : contact mis (sans
    démarrer), appuyer et relâcher la pédale plusieurs fois. Les feux doivent
    s'allumer et s'éteindre sans délai. S'assurer qu'ils ne restent pas allumés
    moteur coupé — risque de décharge de batterie (confirmé symptôme RAG). -
    Test du régulateur de vitesse : sur route, activer le régulateur de vitesse
    et vérifier qu'il se désactive immédiatement lors de l'appui sur la pédale
    de frein. Si le régulateur reste actif lors du freinage, l'interrupteur est
    mal réglé ou défectueux. - Contrôle du tableau de bord : vérifier l'absence
    de message d'erreur ESP ou d'ABS au tableau de bord après démarrage. Ces
    systèmes interrogent l'interrupteur de frein et un défaut de signal peut
    déclencher un voyant (symptôme RAG confirmé). - Vérification du connecteur
    électrique : inspecter que le connecteur est correctement verrouillé sur
    l'interrupteur. Un connecteur mal clipsé provoque des contacts intermittents
    et des dysfonctionnements aléatoires — particulièrement sensible aux
    vibrations moteur. - Test sur 50 km de conduite variée : effectuer un trajet
    incluant freinages doux, freinages d'urgence et arrêts complets. Vérifier
    l'absence de comportement erratique du régulateur de vitesse et l'absence de
    voyant ESP qui s'allumerait de façon intempestive.
  S7: >-
    Quel est le prix d'un interrupteur des feux de freins ?Le prix varie selon
    le véhicule et la marque. Utilisez notre sélecteur pour trouver
    l'interrupteur des feux de freins compatible avec votre véhicule et comparer
    les tarifs des différents équipementiers.Comment savoir si l'interrupteur
    des feux de freins est à changer ?Les signes d'usure les plus courants sont
    détaillés dans la section diagnostic ci-dessus. En cas de doute, faites
    contrôler la pièce par un professionnel.Peut-on rouler avec un interrupteur
    des feux de freins défaillant ?Cela dépend de la gravité du
    dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule.
    Consultez la section symptômes pour évaluer l'urgence du remplacement.-
    detecter - signaler - activer
  S8: >-
    Comment choisir Interrupteur des feux de freins compatible avec
    monRenseignez marque, modele, type moteur et annee, puis verifiez la
    reference Quand remplacer Interrupteur des feux de freins ?En cas de feux
    stop qui restent allumes moteur eteint ou de degradation Puis-je monter
    Interrupteur des feux de freins sans verification atelierLe montage peut
    exiger controles de couple, alignement et references.
  META: >-
    {"meta_title":"Interrupteur feux de frein : stop bloqués ou HS ? |
    AutoMecanik","meta_description":"Feux stop restés allumés ou qui ne
    s'allument plus ? Ce guide explique quand changer l'interrupteur des feux de
    freins et comment tester et remplacer la pièce soi-même en 10 min.","meta_ti
    tle_length":58,"meta_description_length":157,"primary_intent":"diagnostic","
    target_symptoms":["feux stop qui restent allumes moteur eteint","feux stop
    qui ne s allument plus du tout","message d erreur systeme esp au tableau de
    bord"],"category":"capteurs","severity_note":"symptome_securite_present"}
---

# Interrupteur des feux de freins - Guide Diagnostic Complet

## Fonction et Rôle

Detecte l'appui sur la pedale de frein pour activer les feux stop

**Actions principales:** detecter, signaler, activer, commander

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Message d erreur systeme esp au tableau de bord**
  message d erreur systeme esp au tableau de bord
- **Clic audible absent quand on appuie sur la pedale**
  clic audible absent quand on appuie sur la pedale

### 🟢 Autres Symptômes

- feux stop qui restent allumes moteur eteint
- feux stop qui ne s allument plus du tout
- regulateur de vitesse qui ne fonctionne plus
- batterie decharge feux stop restes
- odeur de plastique brule court-circuit
- plus de 150 000 km sans verification

## Procédure de Diagnostic

Pour diagnostiquer un problème de interrupteur des feux de freins:

1. **Inspection visuelle** - Examiner l'état du interrupteur des feux de freins
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- cable-de-frein-a-main
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- etrier-de-frein
- feu-arriere
- kit-de-freins-arriere
- machoires-de-frein

## Critères de Compatibilité

Pour commander le bon interrupteur des feux de freins, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleur freinage"

## FAQ

**Interrupteur feux stop OE ou adaptable ?**
Les interrupteurs adaptables fonctionnent bien pour un usage standard. L'OE est recommandé sur véhicules récents avec fonctions multiples (ESP, régulateur).

**Comment savoir si mon interrupteur de feux stop est HS ?**
Feux stop qui restent allumés en permanence, ou qui ne s'allument plus du tout. Le régulateur de vitesse peut aussi ne plus fonctionner.

**Peut-on tester l'interrupteur de feux stop ?**
Oui avec un multimètre. Vérifiez la continuité quand la pédale est enfoncée. Ou observez les feux stop pendant qu'un assistant appuie sur la pédale.

**Peut-on changer l'interrupteur de feux stop soi-même ?**
Oui, très simple. Accès sous le tableau de bord, derrière la pédale de frein. Quart de tour pour déverrouiller. 10 minutes suffisent.

**Quelle erreur éviter avec l'interrupteur de feux stop ?**
Vérifier le réglage après montage (feux doivent s'allumer dès le début de course pédale). Attention au sens de montage sur certains modèles.
