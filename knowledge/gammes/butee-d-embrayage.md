---
category: embrayage
slug: butee-d-embrayage
title: Butée d'embrayage
pg_id: 48
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
  last_enriched_by: skill:phase5-gates-skf-trw
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Actionner le mécanisme d'embrayage pour permettre le débrayage
  must_be_true:
  - actionner
  - débrayer
  - pousser
  must_not_contain:
  - disque
  - volant
  - couple
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - kit-d-embrayage
  - volant-moteur
  - emetteur-d-embrayage
  - recepteur-d-embrayage
  - cable-d-embrayage
  confusion_with:
  - term: piece-d-embrayage-voisine
    difference: Le systeme d embrayage comporte plusieurs pieces (disque, mecanisme, butee, emetteur, recepteur). Verifier
      laquelle est defectueuse.
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
  - ❌ "débrayage parfait"
  cost_range:
    min: 20
    max: 80
    currency: EUR
    unit: butée
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
    description: 'Butée conforme aux spécifications constructeur : diamètre de contact, hauteur de poussée et type (auto-centrante
      ou à guidage). Généralement livrée dans le kit embrayage complet.'
  - tier: Qualité équivalente OE
    description: Butée d'équipementier spécialisé embrayage respectant les côtes fonctionnelles. Souvent vendue seule ou en
      kit partiel avec la fourchette.
  - tier: Adaptable compatible
    description: Butée de remplacement compatible avec plusieurs références proches. Vérifier impérativement le diamètre intérieur,
      extérieur et la hauteur avant commande.
  - tier: Kit embrayage complet
    description: La butée est généralement remplacée en même temps que le disque et le mécanisme. Acheter un kit complet homogène
      évite les incompatibilités d'usure.
  brands:
    premium:
    - LuK
    - Sachs
    standard:
    - Valeo
    - Exedy
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Bruit roulement quand appuie pedale
    severity: confort
  - id: S2
    label: Sifflement grondement disparait relachant pedale
    severity: confort
  - id: S3
    label: Pedale d embrayage qui vibre sous le pied
    severity: confort
  - id: S4
    label: Embrayage qui accroche par a-coups
    severity: confort
  - id: S5
    label: Difficulte a passer les vitesses butee grippee
    severity: confort
  - id: S6
    label: Plus changement embrayage
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : bruit roulement quand appuie pedale'
  quick_checks:
  - Bruit roulement quand appuie pedale ?
  - 'Observer : sifflement grondement disparait relachant pedale ?'
  - 'Observer : pedale d embrayage qui vibre sous le pied ?'
  - 'Observer : embrayage qui accroche par a-coups ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Bruit roulement quand appuie pedale
  - Sifflement grondement disparait relachant pedale
  - Pedale d embrayage qui vibre sous le pied
  - Embrayage qui accroche par a-coups
  - Difficulte a passer les vitesses butee grippee
  - Plus changement embrayage
  good_practices:
  - Eviter de laisser le pied sur la pedale d embrayage au point mort
  - Remplacement du kit complet (disque + mecanisme + butee)
  - Purge du circuit hydraulique si recepteur/emetteur concerne
  - Verifier le volant moteur lors du remplacement d embrayage
rendering:
  pgId: '48'
  intro_title: A quoi sert Butée d'embrayage ?
  risk_title: Pourquoi remplacer Butée d'embrayage a temps ?
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
  - question: Butée d'embrayage OE ou OES ?
    answer: Les butées OES (Sachs, LuK, Valeo) sont de qualité équivalente à l'OE. Privilégiez un kit embrayage complet de
      la même marque pour garantir la compatibilité.
  - question: Comment savoir si ma butée d'embrayage est HS ?
    answer: Bruit de roulement (grondement ou sifflement) quand on appuie sur la pédale d'embrayage, pédale qui vibre, embrayage
      qui accroche par à-coups.
  - question: Tous les combien changer la butée d'embrayage ?
    answer: À chaque changement du kit embrayage (120 000 à 200 000 km). Ne jamais la réutiliser même si elle semble en bon
      état.
  - question: Peut-on changer la butée d'embrayage seule ?
    answer: 'Techniquement possible mais déconseillé : il faut déposer la boîte de vitesses. Autant changer tout le kit embrayage
      en même temps.'
  - question: Quelle erreur éviter avec la butée d'embrayage ?
    answer: Ne pas laisser le pied sur la pédale d'embrayage en conduisant. Ne pas réutiliser une vieille butée. Vérifier
      le guide-butée et la fourchette.
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
doc_id: 09874db9-d6a5-5c68-bcb9-4370b6c80d06
content_hash: sha256:8a5ad1608d9efd0f
lang: fr
variants:
- name: Kit embrayage complet
  aliases:
  - kit complet
  - 3 pieces
  functional_differences:
  - Disque + mecanisme + butee
  - Remplacement recommande en bloc
- name: Kit avec volant moteur
  aliases:
  - kit 4 pieces
  - kit + volant
  functional_differences:
  - Inclut le volant moteur bimasse
  - Pour vehicules diesel modernes
location_on_vehicle:
  area: Entre le moteur et la boite de vitesses
  access: Depose de la boite de vitesses necessaire (pont elevateur)
  adjacent_parts:
  - volant moteur
  - boite de vitesses
  - arbre primaire
installation:
  difficulty: difficile (pro recommande)
  time: 4h a 8h
  tools:
  - pont elevateur
  - cric de boite
  - centreur d embrayage
  - cle dynamometrique
  prerequisite: Depose complete de la boite de vitesses
phase5_enrichment:
  _source: Gates / SKF / TRW-ZF (donnees techniques constructeur)
  _validation_status: oem_verified
  _enriched_at: '2026-03-30'
  types_variants:
  - type: Butee mecanique a roulement
    description: Roulement a billes + guide, actionnee par fourchette mecanique
    era: standard vehicules a cable
  - type: Butee hydraulique concentrique (CSC)
    description: Verin hydraulique + roulement integre, remplace fourchette + emetteur/recepteur
    era: 2005+, standard actuel
  technical_notes:
    graisse_guide: 'graisse haute temperature sur la portee de centrage, indispensable'
    purge_csc: 'obligatoire apres remplacement butee hydraulique — air = pedale molle'
    course_csc: 'verifier course residuelle au diagnostic — course < 3 mm = butee en fin de vie'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le rôle de la butée d'embrayage est comprimé le centre de diaphragme
    dumécanisme d'embrayage pour libérer le disque. Lorsque vous appuyez sur
    lapédale d'embrayage, la fourchette exerce une force sur la butée qui va
    appuyersur le mécanisme d'embrayage. Ce dernier va libérer le disque
    d'embrayage pourfaire la liaison entre le volant moteur et la boîte de
    vitesses. Cette liaisonest interrompue lorsqu'on relâche la pédale
    d'embrayage. La butée d'embrayage est constituée d'un plateau d'appui et
    d'unroulement intégré pour limiter la friction sur le centre de diaphragme.
    Il existe deux types de butée d'embrayage : - Butée d'embrayage mécanique. -
    Butée d'embrayage hydraulique. Unenouvelle technologie avec butée intégré
    appelé cylindre récepteur concentrique(CSC) permet d'obtenir un système plus
    léger et plus rapide. En savoir plus : butée d'embrayage — définition et
    rôle mécanique 🚨 Bruit Butée d'embrayage : causes et diagnostic
  S2: >-
    Une butée d'embrayage défaillante présente plusieurssymptômes : - Bruit
    sourde lorsque lemoteur tourne et il s'arrête dés que vous appuyez sur la
    pédale d'embrayage. - Pédale d'embrayage dur. - Passage difficile
    desvitesses. Une butée d'embrayage défectueuse et qu'elle n'est pasremplacée
    peut causer plusieurs problèmes : - Usure du kit d'embrayage . - Usure du
    volant moteur . Diagnostic complet : identifier une panne de butée
    d'embrayage
  S3: >-
    La butée d'embrayage (ou butée de débrayage) est le point de contact entre
    la fourchette commandée par la pédale et le plateau de pression du mécanisme
    d'embrayage. Elle tourne en permanence sur les transmissions à commande
    hydraulique (butée auto-réglante en contact constant), ou seulement lors de
    l'appui pédale sur les commandes mécaniques. Un mauvais choix de butée
    provoque des bruits persistants ou une incompatibilité de cote qui empêche
    le débrayage complet. - Type de commande : hydraulique (butée auto-réglante)
    ou mécanique (câble/fourchette) — La butée hydraulique (cylindre récepteur
    concentrique, ou CSC) est intégrée dans la cloche d'embrayage et ne se règle
    pas. La butée mécanique se monte sur la fourchette et son débattement se
    règle par câble ou tringle. Ces deux types ne sont pas interchangeables et
    exigent des mécanismes d'embrayage adaptés. - Diamètre intérieur et
    extérieur de la bague de contact (mm) — La face de contact de la butée doit
    correspondre exactement à la face du mécanisme d'embrayage. Un diamètre
    intérieur trop grand crée un contact excentré qui fait travailler les doigts
    du mécanisme de manière inégale et accélère l'usure du plateau. - Course et
    hauteur hors-tout — cote critique sur les butées mécaniques — La hauteur de
    la butée détermine la position de point de patinage à la pédale. Une butée
    trop haute ou trop basse déplace le point de coupure hors de la plage de
    réglage du câble, rendant le réglage du jeu de pédale impossible ou
    extrêmement court. - Compatibilité avec le kit d'embrayage complet —
    référence du kit — Les fabricants de kits d'embrayage (Sachs, LuK, Valeo,
    Exedy) incluent souvent la butée adaptée dans leur kit complet. Acheter une
    butée séparément exige de vérifier sa compatibilité avec le mécanisme et le
    disque en place — qui peuvent être d'un fabricant différent de celui
    d'origine. - Type de palier : roulement à billes ou butée à aiguilles — Le
    roulement à billes (le plus courant) supporte les charges axiales lors du
    débrayage. La butée à aiguilles supporte des charges radiales et axiales
    combinées sur certaines boîtes de vitesses à fort couple. Vérifier le type
    monté sur le véhicule d'origine pour maintenir la compatibilité de charge. -
    Matériau de la bague de contact : acier ou composite plastique — Les butées
    modernes à bague de contact composite (plastique chargé PTFE) fonctionnent à
    sec sans graissage et tolèrent un contact permanent avec le mécanisme
    (butées auto-réglantes). Les bagues acier nécessitent une légère application
    de graisse haute température au montage. - Remplacement systématique avec le
    kit d'embrayage complet — La butée d'embrayage partage la durée de vie du
    disque et du mécanisme. La remplacer seule sans changer le kit complet
    laisse le reste du système en fin de vie et expose à une récidive dans les
    10 000 à 20 000 km. Pour aller plus loin : consultez notre guide d'achat
    butée d'embrayage — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Butée d'embrayage pour
    connaître les spécifications. - Levez et calez le véhicule. - Démontez le
    kit d'embrayage . - Démontez le mécanisme d'embrayage . - Démontez le disque
    d'embrayage . - Désaccouplez la canalisation hydraulique de la butée
    d'embrayage (si le système est hydraulique). - Desserrez les fixations de la
    butée d'embrayage. - Retirez la butée d'embrayage.
  S4_REPOSE: >-
    Le remontage de la butée d'embrayage s'effectue dans le cadre du
    remplacement complet du kit embrayage, la boîte de vitesses étant abaissée.
    C'est l'occasion de contrôler tous les composants accessibles (guide-butée,
    fourchette, guide-boîte) avant de tout refermer — une vérification manquée
    ici coûte une nouvelle intervention complète. - Vérifiez que la butée
    d'embrayage neuve est identique à celle déposée : diamètre intérieur, profil
    de glissière et type de fixation sur la fourchette (clip ou rondelle-
    ressort). Ne jamais réutiliser l'ancienne butée même si elle semble en état.
    - Contrôlez l'état du guide-butée sur l'arbre primaire de la boîte : absence
    d'oxydation, de rainure d'usure ou d'ovalisage. En cas de doute, remplacez-
    le — il est généralement inclus dans le kit embrayage. - Vérifiez l'état de
    la fourchette de débrayage : absence de fissure, de déformation ou d'usure
    sur l'axe de pivotement. Graissez légèrement l'axe de fourchette avec une
    graisse haute température. - Appliquez une fine couche de graisse spéciale
    embrayage sur les rainures de glissière du guide-butée (pas sur la surface
    de contact de la butée avec le mécanisme, qui doit rester sèche). - Montez
    la butée d'embrayage sur le guide-butée en engageant les griffes sur la
    fourchette. Vérifiez qu'elle coulisse librement sur toute la course sans
    point dur. - Remontez le disque d'embrayage en veillant au sens de montage
    (face amortisseur côté boîte sur la plupart des modèles). Centrez le disque
    à l'aide d'un mandrin de centrage correspondant au diamètre de l'arbre
    primaire. - Remontez le mécanisme d'embrayage en engageant les goupilles de
    centrage sur le volant moteur. Serrez les vis du mécanisme progressivement
    en étoile au couple constructeur (généralement 18 à 25 Nm). - Si la butée
    est à commande hydraulique, reconnectez la canalisation hydraulique et
    purgez le circuit : appuyez et relâchez lentement la pédale d'embrayage
    plusieurs fois avec le bouchon de purge ouvert jusqu'à absence de bulles
    d'air. - Remontez la boîte de vitesses en guidant l'arbre primaire dans le
    disque centré. Ne pas forcer — si l'arbre résiste, recentrez le disque.
    Serrez les vis de fixation de la boîte au couple constructeur. - Reposez le
    véhicule au sol. Vérifiez la course et la dureté de la pédale d'embrayage.
    Passez toutes les vitesses moteur tournant pour confirmer le bon
    fonctionnement avant de rouler.
  S5: >-
    Erreurs frequentes avec la butee d'embrayage : - Ne pas remplacer la butee
    lors du changement du kit d'embrayage — la butee a le meme age que le disque
    et le mecanisme, elle lachera peu apres et il faudra tout redemonter-
    Oublier de graisser la portee de centrage de la butee sur le guide — sans
    graisse, la butee grippe et l'embrayage ne debraye plus completement-
    Confondre butee mecanique et butee hydraulique — les deux ne sont pas
    interchangeables et les fixations different- Ne pas purger le circuit
    hydraulique apres remplacement d'une butee hydraulique — air dans le circuit
    = pedale molle et debrayage incomplet- Ignorer un bruit de sifflement ou de
    grondement pedale enfoncee — signe typique de roulement de butee use-
    Reutiliser les clips ou ressorts de maintien de la butee — ces pieces se
    deforment au demontage et ne tiennent plus
  S6: >-
    Après le remplacement de votre butée d'embrayage, effectuez ces
    vérifications dans l'ordre. - Appuyer lentement sur la pédale d'embrayage en
    cabine, moteur arrêté : aucun bruit de roulement ni sifflement ne doit être
    audible - Démarrer le moteur et appuyer plusieurs fois sur la pédale pour
    confirmer l'absence de bruit caractéristique disparaissant au relâché -
    Vérifier le point de patinage de l'embrayage : il doit se situer à mi-course
    de la pédale, ni trop haut ni trop bas - Effectuer plusieurs passages de
    vitesse en roulant à basse vitesse (1re, 2e, marche arrière) pour confirmer
    l'absence d'accrochage - Contrôler l'absence de vibration sous le pied lors
    de l'appui sur la pédale - Si la butée a été changée avec le kit d'embrayage
    complet, vérifier le récepteur et l'émetteur d'embrayage pour toute fuite de
    liquide hydraulique Retrouvez les spécifications techniques sur la fiche
    référence butée d'embrayage.
  S7: >-
    Quel est le prix d'un butée d'embrayage ?Le prix varie selon le véhicule et
    la marque. Utilisez notre sélecteur pour trouver le butée d'embrayage
    compatible avec votre véhicule et comparer les tarifs des différents
    équipementiers.Comment savoir si mon butée d'embrayage est à changer ?Les
    signes d'usure les plus courants sont détaillés dans la section diagnostic
    ci-dessus. En cas de doute, faites contrôler la pièce par un
    professionnel.Peut-on rouler avec un butée d'embrayage défaillant ?Cela
    dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la
    sécurité du véhicule. Consultez la section symptômes pour évaluer l'urgence
    du remplacement.- emetteur d embrayage - kit d embrayage - recepteur d
    embrayage - volant moteur
  S8: >-
    Comment choisir Butée d'embrayage compatible avec mon vehicule ?Renseignez
    marque, modele, type moteur et annee, puis verifiez la reference Quand
    remplacer Butée d'embrayage ?En cas de bruit roulement quand appuie pedale
    ou de degradation mesurable, Puis-je monter Butée d'embrayage sans
    verification atelier ?Le montage peut exiger controles de couple, alignement
    et references.
  META: >-
    {"meta_title":"Butée d'embrayage : bruit, diagnostic et remplacement |
    AutoMecanik","meta_description":"Grondement ou sifflement quand vous appuyez
    sur la pédale d'embrayage ? La butée est usée. Ce guide explique quand la
    changer, toujours avec le kit embrayage complet.","og_title":"Butée
    d'embrayage : diagnostic bruit et remplacement
    kit","og_description":"Grondement ou sifflement quand vous appuyez sur la
    pédale d'embrayage ? La butée est usée. Ce guide explique quand la changer,
    toujours avec le kit embrayage complet.","schema_type":"Article","primary_in
    tent":"diagnostic","gate_report":"PASS","char_count_title":55,"char_count_de
    sc":181}
---

# Butée d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Actionner le mécanisme d'embrayage pour permettre le débrayage

**Actions principales:** actionner, débrayer, pousser, libérer le disque, appuyer sur le mécanisme

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- bruit roulement quand appuie pedale
- sifflement grondement disparait relachant pedale
- pedale d embrayage qui vibre sous le pied
- embrayage qui accroche par a-coups
- difficulte a passer les vitesses butee grippee
- plus changement embrayage

## Procédure de Diagnostic

Pour diagnostiquer un problème de butée d'embrayage:

1. **Inspection visuelle** - Examiner l'état du butée d'embrayage
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

- emetteur-d-embrayage
- kit-d-embrayage
- recepteur-d-embrayage
- volant-moteur

## Critères de Compatibilité

Pour commander le bon butée d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "débrayage parfait"

## FAQ

**Butée d'embrayage OE ou OES ?**
Les butées OES (Sachs, LuK, Valeo) sont de qualité équivalente à l'OE. Privilégiez un kit embrayage complet de la même marque pour garantir la compatibilité.

**Comment savoir si ma butée d'embrayage est HS ?**
Bruit de roulement (grondement ou sifflement) quand on appuie sur la pédale d'embrayage, pédale qui vibre, embrayage qui accroche par à-coups.

**Tous les combien changer la butée d'embrayage ?**
À chaque changement du kit embrayage (120 000 à 200 000 km). Ne jamais la réutiliser même si elle semble en bon état.

**Peut-on changer la butée d'embrayage seule ?**
Techniquement possible mais déconseillé : il faut déposer la boîte de vitesses. Autant changer tout le kit embrayage en même temps.

**Quelle erreur éviter avec la butée d'embrayage ?**
Ne pas laisser le pied sur la pédale d'embrayage en conduisant. Ne pas réutiliser une vieille butée. Vérifier le guide-butée et la fourchette.
