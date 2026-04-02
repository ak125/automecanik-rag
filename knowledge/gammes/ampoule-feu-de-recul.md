---
category: eclairage
slug: ampoule-feu-de-recul
title: Ampoule feu de recul
pg_id: 114
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
  role: Produit la lumière pour signaler la marche arrière et éclairer derrière le véhicule
  must_be_true:
  - produire
  - emettre
  - eclairer
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
  - tier: Ampoule LED recul compatible
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
    label: Feu de recul inactif
    severity: confort
  - id: S2
    label: Camera de recul sans eclairage
    severity: confort
  - id: S3
    label: Stationnement nocturne difficile
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : feu de recul inactif'
  quick_checks:
  - 'Observer : feu de recul inactif ?'
  - 'Observer : camera de recul sans eclairage ?'
  - 'Observer : stationnement nocturne difficile ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Feu de recul inactif
  - Camera de recul sans eclairage
  - Stationnement nocturne difficile
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '114'
  intro_title: A quoi sert Ampoule feu de recul ?
  risk_title: Pourquoi remplacer Ampoule feu de recul a temps ?
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
  - question: Comment choisir Ampoule feu de recul compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Ampoule feu de recul ?
    answer: En cas de feu de recul inactif ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Ampoule feu de recul sans verification atelier ?
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
doc_id: 9b072dc5-82e8-51df-8dd0-a37f6bc1a917
content_hash: sha256:c559d4b4c206dcaa
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
    type: 'P21W ou W16W selon vehicule, lumiere blanche'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    L'ampoule feu de recul est le composant électrique qui produit la lumière
    blanche signalant l'engagement de la marche arrière et éclairant la zone
    derrière le véhicule. Elle est montée dans le bloc feu arrière et s'allume
    automatiquement dès que le conducteur engage la marche arrière, via le
    contacteur de boîte de vitesses. Son rôle est double : avertir les usagers
    situés derrière le véhicule d'une manœuvre de recul imminente ou en cours,
    et éclairer la zone arrière pour faciliter la manœuvre du conducteur,
    notamment de nuit ou dans un espace étroit. La lumière émise est
    obligatoirement blanche selon la réglementation européenne et nord-
    américaine. Techniquement, l'ampoule feu de recul est alimentée par le
    circuit électrique de marche arrière. Un contacteur mécanique fixé sur la
    boîte de vitesses — ou un signal électronique issu du calculateur de boîte
    sur les transmissions automatiques — ferme le circuit dès que la marche
    arrière est sélectionnée. L'ampoule fonctionne sur le circuit 12 V du
    véhicule et est protégée par un fusible dédié. Les types d'ampoules feu de
    recul les plus courants sont la P21W (culot BA15s, 21 W) et, sur certains
    modèles, des versions LED de remplacement. La compatibilité doit être
    vérifiée par référence constructeur — marque, modèle et année — car les
    culots et les supports varient significativement selon les constructeurs et
    les générations de véhicules.
  S2: >-
    La défaillance d'une ampoule feu de recul se manifeste par plusieurs signes
    caractéristiques. Ces symptômes doivent conduire à une intervention rapide,
    car un feu de recul non fonctionnel constitue une infraction au code de la
    route et réduit la sécurité des manœuvres de recul. - Feu de recul inactif
    en marche arrière : l'ampoule ne s'allume pas lorsque la marche arrière est
    engagée. Ce symptôme direct indique soit la rupture du filament de
    l'ampoule, soit une panne du contacteur de boîte ou un fusible grillé. -
    Caméra de recul sans éclairage : sur les véhicules équipés d'une caméra de
    recul positionnée à proximité du feu de recul, l'absence d'éclairage du feu
    peut dégrader fortement la qualité de l'image de la caméra de nuit, rendant
    les manœuvres dangereuses. - Stationnement nocturne difficile : sans
    l'éclairage du feu de recul, le conducteur perd un repère lumineux précieux
    lors des manœuvres en marche arrière dans un environnement peu éclairé,
    augmentant le risque de collision. - Scintillement du feu lors des manœuvres
    : le feu s'allume de manière instable ou intermittente lorsque la marche
    arrière est engagée, signe d'un mauvais contact entre l'ampoule et sa
    douille, ou d'un filament fragilisé en voie de rupture. - Ampoule noircie
    visible dans le bloc feu : un dépôt noir à l'intérieur du verre de l'ampoule
    halogène indique que le filament a surchauffé ou brûlé — signe de fin de vie
    imminent même si l'ampoule produit encore de la lumière. - Voyant ou message
    de défaut feux au tableau de bord : les véhicules récents disposent d'un
    système de surveillance des ampoules qui génère un message ou un pictogramme
    dès qu'une défaillance électrique est détectée dans le circuit feu de recul.
  S3: >-
    Le choix d'une ampoule feu de recul doit s'appuyer sur la référence exacte
    préconisée par le constructeur. Une ampoule non conforme peut endommager la
    douille, déclencher un voyant de défaut ou ne pas s'activer correctement au
    passage de la marche arrière. - Identifier la référence par le triptyque
    véhicule : renseignez la marque, le modèle et l'année du véhicule dans un
    catalogue de référence automobile. La référence figure également sur
    l'ampoule d'origine une fois retirée. - Vérifier le type de culot : le culot
    BA15s (ampoule P21W) est le plus répandu pour les feux de recul, mais
    certains véhicules utilisent d'autres standards. Monter un culot
    incompatible empêche le montage ou crée un contact défectueux. - Respecter
    la puissance de 21 W : la puissance standard pour un feu de recul est de 21
    W. Ne pas augmenter cette valeur — le câblage, le fusible et la douille sont
    dimensionnés pour cette charge spécifique. - Contrôler le contacteur de
    marche arrière avant remplacement : si le feu ne fonctionnait pas et que le
    fusible est intact, le contacteur de boîte de vitesses peut être en cause.
    Vérifier ce point avant de monter une ampoule neuve. - Choisir une LED
    compatible si souhaité : une LED feu de recul offre une meilleure luminosité
    et une durée de vie plus longue. Vérifiez la compatibilité avec votre modèle
    — certains véhicules nécessitent une résistance de compensation pour éviter
    le déclenchement d'un voyant de défaut. - Vérifier l'état de la douille :
    une douille corrodée ou brûlée doit être nettoyée ou remplacée avant le
    montage d'une ampoule neuve, sous peine de réduire sa durée de vie et de
    créer des intermittences. Pour aller plus loin : consultez notre guide
    d'achat ampoule feu de recul — comparatif marques, critères de choix et
    prix.
  S4_DEPOSE: >-
    Le remplacement d'une ampoule feu de recul est généralement accessible sans
    outillage spécialisé. L'accès se fait le plus souvent par l'intérieur du
    coffre. Sur certains véhicules, le bloc feu doit être retiré depuis
    l'extérieur. - Couper le contact et engager la marche arrière : éteignez
    complètement le véhicule. Laissez l'ampoule refroidir au moins 5 minutes si
    les feux étaient allumés. Ne jamais manipuler une ampoule chaude. - Accéder
    au bloc feu arrière : ouvrez le coffre. Sur la plupart des véhicules, un
    cache en plastique intérieur (déclipsable ou vissé) donne accès aux porte-
    ampoules du bloc feu arrière. Sur d'autres modèles, le bloc se retire par
    l'extérieur après dépose de 2 à 4 vis. - Identifier le porte-ampoule du feu
    de recul : localisez le porte-ampoule correspondant au feu de recul — il est
    généralement identifié par une étiquette sur le cache ou dans le manuel
    d'utilisation du véhicule. - Débrancher le connecteur électrique : appuyez
    sur le verrou du connecteur et tirez délicatement. Ne pas tirer sur les fils
    eux-mêmes. - Extraire le porte-ampoule : tournez le porte-ampoule d'un quart
    de tour dans le sens antihoraire pour le déverrouiller, puis extrayez-le du
    bloc optique. - Remplacer l'ampoule : retirez l'ampoule usagée du porte-
    ampoule (pression + rotation selon les modèles). Insérez la nouvelle ampoule
    sans toucher le verre avec les doigts nus — utilisez un chiffon propre ou
    saisissez par le culot. - Remonter dans l'ordre inverse : réinsérez le
    porte-ampoule dans le bloc optique, reconnectez le connecteur électrique,
    refixez le cache intérieur ou le bloc feu extérieur. - Tester le
    fonctionnement : démarrez le véhicule, engagez la marche arrière et vérifiez
    que le feu de recul s'allume correctement des deux côtés si le véhicule en
    est équipé.
  S4_REPOSE: >-
    La repose d'une ampoule feu de recul suit l'ordre inverse de la dépose.
    L'opération est rapide — moins de 10 minutes dans la majorité des cas — mais
    nécessite de respecter quelques points précis pour éviter un faux contact ou
    un défaut détecté par le calculateur de bord. L'ampoule de recul est
    généralement une P21W (21 watts, culot baïonnette à un ergot) ou une R10W
    selon le véhicule. - Identifier la bonne référence : avant d'insérer la
    nouvelle ampoule, vérifiez qu'elle correspond exactement à l'ampoule
    d'origine. Pour un feu de recul, la puissance nominale est 21 W (P21W). Une
    ampoule de 5 W ou 10 W dans ce logement produira un éclairage insuffisant et
    peut provoquer une détection de défaut sur les véhicules récents. - Engager
    l'ampoule dans la douille : alignez les ergots latéraux du culot baïonnette
    avec les rainures de la douille. Enfoncez légèrement l'ampoule en comprimant
    le ressort de fond de douille, puis effectuez un quart de tour dans le sens
    horaire jusqu'au blocage. La résistance doit être nette — l'ampoule ne doit
    pas pouvoir se rétracter seule. - Vérifier l'orientation de l'ergot de
    détrompeur : la P21W possède un ergot unique qui empêche de monter une
    ampoule double filament à la place. Si l'ampoule ne s'engage pas, c'est que
    la référence est incorrecte. Ne forcez jamais. - Réinsérer le porte-ampoule
    dans le feu : réintroduisez l'ensemble porte-ampoule dans le logement du
    bloc feu arrière. Effectuez le quart de tour de verrouillage ou clipsez
    selon le système de fixation du véhicule. - Reconnecter le faisceau si
    déconnecté : si le faisceau a été débranché, réenficher le connecteur
    jusqu'au déclic audible. Sur certains feux arrière, le connecteur est
    multifil (feu stop, clignotant, recul, position) — attention à ne pas
    inverser les connecteurs s'il y en a plusieurs. - Remettre le bloc feu en
    place si déposé : si vous avez dû retirer le bloc feu depuis l'extérieur,
    repositionnez-le sur son cadre. Revissez les vis ou boulons de fixation sans
    trop forcer (risque de fissure du plastique). Vérifiez que le joint
    d'étanchéité entre le feu et la carrosserie est bien positionné. - Refermer
    le cache intérieur de coffre : si un cache en tissu ou en plastique rigide a
    été déposé depuis l'intérieur du coffre, reclipsez-le en vérifiant que tous
    les clips sont engagés. Un cache mal fixé génère des bruits parasites en
    roulant. - Test fonctionnel : reconnectez la batterie si elle a été
    débranchée. Démarrez le véhicule, engagez la marche arrière et vérifiez
    depuis l'arrière que le feu de recul s'allume. Si le véhicule est équipé
    d'une caméra de recul, vérifiez également que l'image s'affiche correctement
    — la caméra exploite souvent l'éclairage du feu de recul pour fonctionner la
    nuit.
  S5: >-
    Le remplacement d'une ampoule feu de recul est simple mais expose à
    plusieurs erreurs fréquentes qui peuvent réduire la durée de vie de la
    nouvelle pièce ou laisser le défaut en place. - Ne pas vérifier le fusible
    avant de changer l'ampoule : si le feu de recul ne fonctionne pas, la
    première vérification doit porter sur le fusible dédié. Remplacer l'ampoule
    sans contrôler le fusible conduit à monter une pièce neuve qui ne
    fonctionnera pas non plus si le fusible est grillé. - Confondre le
    contacteur de boîte et l'ampoule : si les deux feux de recul sont éteints
    simultanément, le problème vient presque toujours du contacteur de marche
    arrière ou du fusible, pas des ampoules — deux ampoules ne grillent pas en
    même temps dans des circonstances normales. - Toucher le verre de l'ampoule
    halogène avec les doigts : les traces de graisse créent un point chaud lors
    de l'allumage qui fragmente le verre ou brûle le filament prématurément.
    Saisir l'ampoule par le culot ou utiliser un chiffon propre. - Monter une
    LED sans vérifier la compatibilité électronique : sur les véhicules avec
    surveillance des ampoules, une LED de trop faible consommation est
    interprétée comme une panne par le calculateur, qui peut afficher un voyant
    ou couper le circuit. - Négliger de contrôler la douille et le connecteur :
    une douille oxydée ou un connecteur avec des contacts brûlés entraîne un
    mauvais contact électrique qui réduit la durée de vie de la nouvelle ampoule
    et provoque des intermittences.
  S6: >-
    Après le remplacement de l'ampoule feu de recul, réalisez les contrôles
    suivants pour confirmer le bon fonctionnement du circuit et la qualité du
    montage. - Test d'activation en marche arrière : démarrez le véhicule,
    engagez la marche arrière et vérifiez que le ou les feux de recul s'allument
    immédiatement, avec une lumière blanche stable et intense. - Vérification de
    l'extinction hors marche arrière : confirmez que le feu s'éteint
    complètement dès que vous quittez la marche arrière. Un feu qui reste allumé
    signale un contacteur de boîte bloqué ou un court-circuit dans le circuit. -
    Contrôle de la disparition du voyant tableau de bord : si un voyant de
    défaut feux était présent avant l'intervention, il doit s'éteindre
    automatiquement après quelques secondes de fonctionnement normal. -
    Vérification de l'étanchéité du cache ou du bloc feu : assurez-vous que le
    cache intérieur du coffre est bien replacé et que le joint du bloc feu est
    en place pour éviter toute infiltration d'humidité dans le bloc optique. -
    Contrôle visuel à distance : demandez à un tiers de se positionner derrière
    le véhicule pendant que vous engagez la marche arrière, pour confirmer que
    le feu est bien visible et actif.
  S7: >-
    Le feu de recul est un élément du circuit électrique arrière qui partage ses
    connexions avec d'autres fonctions du véhicule. Son remplacement offre un
    accès simplifié à plusieurs composants qui peuvent nécessiter un contrôle ou
    un remplacement simultané. - Contacteur de feu de recul : le contacteur est
    le commutateur mécanique ou électronique qui envoie le signal d'alimentation
    à l'ampoule lorsque la marche arrière est engagée. Si l'ampoule est neuve
    mais que le feu ne s'allume pas, le contacteur est la première cause à
    investiguer. Il est vissé sur le carter de boîte de vitesses (manuelle) ou
    piloté électroniquement (boîte automatique). - Feu arrière complet : si le
    bloc feu arrière présente une lentille fissurée, jaunie ou décolorée, le
    remplacement du bloc entier garantit une étanchéité optimale et une
    visibilité conforme. Les ampoules logées dans un bloc dégradé sont exposées
    à l'humidité, ce qui accélère leur vieillissement. - Ampoule feu stop :
    logée dans le même bloc feu arrière, elle partage l'accès par le coffre. Si
    un stop était faible ou irrégulier, profitez de l'ouverture du bloc pour le
    remplacer simultanément. - Ampoule feu clignotant arrière : dans le même
    bloc optique, partageant le même accès et souvent le même porte-ampoule
    tournant. Un contrôle rapide lors du démontage ne prend que quelques
    secondes. - Caméra de recul : sur les véhicules équipés, la caméra de recul
    exploite souvent l'éclairage du feu de recul pour fournir une image nette la
    nuit. Si la caméra présentait une image sombre ou inexploitable, vérifiez
    d'abord l'état de l'ampoule avant de suspecter la caméra elle-même. - Joint
    d'étanchéité du bloc feu : le joint en caoutchouc placé entre le feu et la
    carrosserie peut se dégrader et laisser pénétrer l'eau dans le coffre. Son
    inspection et son remplacement éventuel lors du démontage du bloc feu est
    une précaution utile sur les véhicules de plus de 8 ans.
  S8: >-
    Comment distinguer une panne d'ampoule feu de recul d'une panne du
    contacteur de boîte ? La méthode la plus simple : si un seul feu de recul
    est éteint, l'ampoule de ce côté est grillée. Si les deux feux de recul sont
    inactifs simultanément, vérifiez d'abord le fusible du circuit feu de recul
    (consultez le schéma du boîtier à fusibles). Si le fusible est intact, la
    cause probable est le contacteur de marche arrière fixé sur la boîte de
    vitesses — une pièce mécanique qui s'use et doit parfois être remplacée.
    Peut-on rouler avec un feu de recul défaillant ? Le feu de recul n'est pas
    obligatoire pour circuler sur la voie publique au sens strict — il ne fait
    pas partie des feux dont l'absence constitue une infraction immédiate à
    l'arrêt. Cependant, il est obligatoire pour le contrôle technique et sa
    défaillance constitue un risque sécuritaire lors des manœuvres nocturnes,
    notamment pour les piétons et les cyclistes qui se trouvent derrière le
    véhicule. Quel type d'ampoule pour le feu de recul ? L'ampoule feu de recul
    la plus répandue est la P21W (culot BA15s, 21 W, lumière blanche). Sur
    certains modèles récents, des variantes comme la P21/5W ou des LED de
    remplacement sont utilisées. La référence exacte doit toujours être vérifiée
    par rapport au modèle du véhicule. Les feux de recul émettent
    obligatoirement de la lumière blanche — aucune autre couleur n'est
    autorisée. La caméra de recul est-elle affectée par l'ampoule feu de recul ?
    Indirectement, oui. La caméra de recul est souvent positionnée dans le même
    bloc feu arrière ou à proximité immédiate du feu de recul. Elle utilise la
    lumière émise par l'ampoule pour éclairer la scène derrière le véhicule de
    nuit. Une ampoule défaillante réduit significativement la qualité de l'image
    de la caméra dans l'obscurité, augmentant le risque de ne pas détecter un
    obstacle ou un piéton.
---

# Ampoule feu de recul - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière pour signaler la marche arrière et éclairer derrière le véhicule

**Actions principales:** produire, emettre, eclairer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- feu de recul inactif
- camera de recul sans eclairage
- stationnement nocturne difficile

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule feu de recul:

1. **Inspection visuelle** - Examiner l'état du ampoule feu de recul
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

- contacteur-feu-de-recul
- feu-arriere

## Critères de Compatibilité

Pour commander le bon ampoule feu de recul, vous devez connaître:

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

**Comment choisir Ampoule feu de recul compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Ampoule feu de recul ?**
En cas de feu de recul inactif ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Ampoule feu de recul sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
