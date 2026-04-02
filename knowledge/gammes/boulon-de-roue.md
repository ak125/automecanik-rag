---
category: accessoires
slug: boulon-de-roue
title: Boulon de roue
pg_id: 657
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
  role: Fixe la roue sur le moyeu du véhicule
  must_be_true:
  - fixer
  - serrer
  - maintenir
  must_not_contain:
  - frein
  - moyeu
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - fixer
  - serrer
  - maintenir
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
  - ❌ "securite garantie"
  cost_range:
    min: 50
    max: 300
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
    description: 'Boulon certifié conforme aux spécifications constructeur : pas de vis, longueur de filet, côte de serrage
      et revêtement anticorrosion d''origine.'
  - tier: Qualité équivalente OE
    description: Pièce d'un équipementier de rang 1 répondant aux normes de résistance mécanique (classe 10.9 ou 12.9 selon
      application). Données techniques vérifiables.
  - tier: Adaptable compatible
    description: Boulons de remplacement compatibles avec plusieurs gammes de véhicules. Vérifier impérativement le pas de
      vis, la longueur et le type de siège (conique, sphérique, plat).
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
    label: Vibrations lors du freinage
    severity: securite
  - id: S2
    label: Roue qui emet des claquements
    severity: confort
  - id: S3
    label: Serrage impossible boulon tourne vide
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - verifier equilibrage et fixations
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'vibrations anormales : verifier equilibrage et fixations'
  quick_checks:
  - Vibrations lors du freinage ?
  - 'Observer : roue qui emet des claquements ?'
  - 'Observer : serrage impossible boulon tourne vide ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Vibrations lors du freinage
  - Roue qui emet des claquements
  - Serrage impossible boulon tourne vide
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '657'
  intro_title: A quoi sert Boulon de roue ?
  risk_title: Pourquoi remplacer Boulon de roue a temps ?
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
  - question: Comment choisir Boulon de roue compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Boulon de roue ?
    answer: En cas de vibrations lors du freinage ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Boulon de roue sans verification atelier ?
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
doc_id: 8fc6c24b-bccf-5ae8-9178-59a0347494ff
content_hash: sha256:f08b6a9962c01d83
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
  _source: contenu LLM — a revalider contre sources OEM
  _validation_status: pending_oem_validation
  _enriched_at: '2026-03-30'
  technical_notes:
    couple: '80-130 Nm selon vehicule — TOUJOURS cle dynamometrique'
    type_assise: 'conique (60°), spherique ou plate selon la jante — ne pas interchanger'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Les boulons de roue sont des pièces essentielles pour les roues avant et
    arrière du véhicule. Leur rôle est de garantir la bonne fixation et le
    centrage de l'assemblage de la jante ou la roue (suivant le niveau
    d'équipement du véhicule) sur le moyeu. Pour démonter une jante ou une roue
    du moyeu, il faut dans dévisser les boulons en premier lieu après les
    démonter, puis démonter la roue à l'aide du cric que le trouve avec les
    équipements du véhicule au niveau du coffre arrière.
  S2: >-
    Le boulon de roue n'a pas de période de remplacement puisque ce n'est pas
    une pièce d'usure. Mais il faut faire un contrôle des boulons de roue si on
    constate qu'il y a un problème de fixation par exemple une t&ecirc;te de
    boulon érodée ou d'un filetage ab&icirc;mé. Des boulons défectueux impacte
    sur l'efficacité du serrage et donc à la solidité de la fixation de la jante
    sur le moyeu. Lors de démontage des boulons pour le changement d'une roue ou
    d'une jante veiller à mettre le cric de soutien du véhicule dans sa bonne
    position. Il faut bien contrôler le serrage des boulons après le remontage
    de la roue ou de la jante si non on risque à avoir plusieurs problèmes si la
    fixation n'est pas bien faite surtout les risques d'accident.
  S3: >-
    - Pas de vis et diamètre : Le pas de vis est la donnée la plus critique —
    une erreur ici rend le boulon inutilisable et endommage les goujons. Les pas
    courants sont M12x1,25 (Renault, Citroën, Peugeot), M12x1,5 (Ford, Opel,
    Toyota) et M14x1,5 (Mercedes, BMW). Mesurez toujours sur un boulon d'origine
    avant de commander. - Longueur de la tige filetée : Trop courte, la roue
    n'est pas maintenue correctement. Trop longue, le boulon frotte sur le frein
    ou l'étrier. La longueur s'exprime en millimètres et doit correspondre
    exactement à l'épaisseur de la jante et du moyeu. - Forme du siège conique
    ou sphérique : Le siège du boulon (la partie qui s'appuie sur la jante) est
    soit conique à 60°, soit sphérique (R12 ou R14). Un siège conique monté sur
    une jante à siège sphérique concentre l'effort sur un anneau étroit et
    provoque un desserrage progressif à l'usage — vérifiez le type de jante
    avant de choisir. - Matériau : acier chromé ou traité : Les boulons
    d'origine sont traités contre la corrosion. Évitez les boulons chromés
    décoratifs bas de gamme sur les roues actives — le chrome peut masquer une
    qualité d'acier insuffisante qui risque de cisaillement sous couple. -
    Hauteur de tête (clé hex ou multipoints) : Vérifiez que la tête du boulon
    (17 mm, 19 mm ou 21 mm selon les modèles) est compatible avec votre clé de
    roue. Sur certaines jantes en alliage avec des trous de petite section, une
    tête trop haute ne rentre pas dans le puits. - Compatibilité jante d'origine
    vs jante après-marché : Les jantes après-marché ont souvent des épaisseurs
    et des types de sièges différents des jantes d'origine. Si vous montez des
    jantes sport ou tuning, reconfirmez la longueur et le type de siège avec le
    fabricant de jantes. - Marque, modèle et année de fabrication :
    Indispensables pour filtrer les références. Sur plusieurs modèles, un même
    constructeur a utilisé des filetages différents selon l'année ou la
    motorisation. Pour aller plus loin : consultez notre guide d'achat boulon de
    roue — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    - Préparer l'outillage : Réunissez une clé dynamométrique (réglable jusqu'à
    130 Nm minimum), une douille adaptée à votre boulon (17, 19 ou 21 mm selon
    le modèle), un cric hydraulique et des chandelles de sécurité homologuées.
    Ne travaillez jamais sous un véhicule maintenu uniquement par un cric. -
    Desserrer les boulons à mi-hauteur avant de lever le véhicule : Avec la roue
    encore au sol (véhicule stable), desserrez chaque boulon d'un quart de tour
    maximum. Cette étape évite de faire tourner la roue dans le vide lors du
    desserrage complet. - Lever et caler le véhicule : Placez le cric sous le
    point de levage prévu par le constructeur (généralement indiqué dans le
    manuel ou marqué sous le seuil de porte). Montez le véhicule puis installez
    les chandelles avant de retirer le cric. - Déposer les boulons et la roue :
    Dévissez complètement les boulons en commençant par ceux opposés en
    diagonale (pour éviter de déformer le moyeu). Posez la roue à plat sur le
    sol. - Inspecter le filetage des goujons : Si des goujons sont présents
    (certains modèles), vérifiez qu'ils ne sont pas déformés ou corrodés. Un
    goujon endommagé doit être remplacé avant de monter les nouveaux boulons. -
    Nettoyer les surfaces de contact : Brossez les portées de la jante et du
    moyeu pour éliminer la corrosion. Une portée propre garantit un serrage
    homogène et évite le desserrage progressif. - Monter les nouveaux boulons à
    la main : Vissez chaque boulon à la main jusqu'à résistance pour s'assurer
    qu'il prend bien dans le filetage sans forcer. Un boulon qui croise ne doit
    jamais être serré à la clé. - Serrer en étoile à la clé dynamométrique :
    Serrez progressivement en croix (ou en étoile pour 5 boulons) en trois
    passes : d'abord à la main, puis à 50 % du couple, enfin au couple prescrit
    par le constructeur (généralement 90 à 130 Nm selon le véhicule — vérifiez
    le manuel). - Contrôle de couple après 50 km : Après le premier trajet,
    repassez sur chaque boulon à la clé dynamométrique pour confirmer le
    maintien du couple. Les nouveaux boulons ont tendance à se tasser légèrement
    lors des premiers serrage-desserrage.
  S4_REPOSE: >-
    La repose des boulons de roue est une étape critique de sécurité. Un serrage
    insuffisant entraîne un desserrage progressif et une perte de roue ; un
    serrage excessif déforme les goujons et complique les futures interventions.
    Le respect de l'ordre d'étoile et du couple constructeur est non
    négociable.- Nettoyer les surfaces de contact avant remontage : brosser la
    portée de la jante et la face du moyeu pour éliminer toute trace de rouille,
    gravier ou corps étranger. Une surface propre garantit un appui homogène et
    évite que les boulons ne se desserrent par tassement.- Vérifier les
    filetages des goujons et des boulons neufs : passer le doigt dans chaque
    filetage de goujon pour détecter un écrasement ou un dommage. Un goujon dont
    le filetage est déformé doit être remplacé — ne pas monter un boulon neuf
    sur un goujon dégradé.- Monter chaque boulon à la main jusqu'à résistance :
    pour les jantes à goujons, engager la jante sur les goujons et visser les
    boulons à la main en les croisant. Ne jamais engager un boulon oblique et ne
    jamais utiliser la clé pour rattraper un croisement de filets.- Pré-serrer
    en étoile à 30 % du couple final : avec la roue encore en l'air, pré-serrer
    les boulons en suivant un ordre en étoile (boulons opposés en diagonale pour
    4 ou 6 boulons, en pentagramme pour 5 boulons). Cette première passe centre
    la jante sur le moyeu.- Descendre le véhicule et poser le poids sur la roue
    : retirer les chandelles, descendre le cric lentement jusqu'à ce que la roue
    porte le poids du véhicule. Cette étape est obligatoire avant le serrage
    final pour éviter que la roue ne tourne lors du serrage dynamométrique.-
    Serrer au couple prescrit par le constructeur en deux passes : première
    passe à 60 % du couple cible, en étoile. Deuxième passe au couple final
    prescrit (généralement 90 à 130 Nm selon les véhicules — consulter le
    manuel). Ne pas dépasser le couple sous peine d'étirer le goujon.- Marquer
    les boulons au marqueur après serrage : tracer un trait de marqueur sur
    chaque boulon en continuité avec la jante. Si un boulon se desserre, le
    décalage du trait sera visible au contrôle suivant.- Contrôler le couple
    après 50 à 100 km : les boulons neufs se tassent légèrement lors des
    premières sollicitations thermiques et mécaniques. Re-serrer chaque boulon
    au couple prescrit après le premier trajet pour confirmer la stabilité du
    serrage.
  S5: >-
    - Serrer au choc pneumatique sans contrôle dynamométrique : La clé à choc
    peut dépasser 300 Nm sur un boulon calibré à 110 Nm. La sur-contrainte étire
    irrémédiablement la tige filetée, rend le boulon fragile et peut fissurer le
    moyeu. Après un serrage au choc (garage ou changement de pneus), repassez
    toujours à la clé dynamométrique. - Utiliser des boulons avec un mauvais
    type de siège : Un siège conique sur une jante à siège sphérique (ou
    inversement) ne répartit pas correctement la charge. La roue semble fixée
    mais le boulon se desserre progressivement à l'usage — situation
    particulièrement dangereuse en virage ou au freinage. - Lubrifier les
    filetages avec de la graisse : La graisse réduit le coefficient de
    frottement et fausse la lecture dynamométrique : pour un couple cible de 110
    Nm, vous obtenez en réalité un serrage de 70-80 Nm seulement. Les boulons de
    roue se serrent toujours à sec sur un filetage propre, sauf indication
    contraire explicite du constructeur. - Monter des boulons de mauvaise
    longueur : Un boulon trop court n'engage pas suffisamment de filets dans le
    moyeu (minimum 6 filets complets requis). Un boulon trop long peut heurter
    le tambour de frein ou l'étrier à pleine butée. Mesurer la longueur filetée
    de l'origine est obligatoire. - Ne pas resserrer après 50 km : Les boulons
    neufs, surtout après remplacement de la jante, ont besoin d'un contrôle de
    couple après rodage. Le tassement des surfaces de contact peut réduire le
    couple de 5 à 15 % lors des premiers kilomètres. Oublier ce contrôle
    transforme un remplacement correct en incident de sécurité potentiel.
  S6: >-
    - Contrôle dynamométrique immédiat : Avant de descendre le véhicule,
    vérifiez chaque boulon à la clé dynamométrique au couple prescrit (90 à 130
    Nm selon le constructeur — vérifiez le manuel de votre véhicule). Procédez
    en étoile ou en croix. - Inspection visuelle de l'affleurement : Chaque
    boulon doit dépasser du moyeu ou de la jante du même nombre de filets que
    les boulons d'origine. Un boulon qui rase la surface extérieure de la jante
    est trop court. - Test de vibrations à faible vitesse : Après remontage,
    roulez à 30-50 km/h en ligne droite puis effectuez un freinage doux. Toute
    vibration au volant ou au plancher indique un serrage inégal — revenez
    immédiatement en atelier. - Contrôle de couple à 50 km : Retournez au
    véhicule immobilisé après le premier trajet significatif et repassez sur
    chaque boulon à la dynamométrique. Si un boulon se déplace lors de ce
    contrôle, c'est un signe de non-conformité du siège ou du filetage. -
    Vérification à 1 000 km : Lors du prochain entretien ou passage en garage,
    demandez un contrôle systématique du couple des boulons de roue, notamment
    si vous avez monté des jantes après-marché.
  S7: >-
    Lors du remplacement des boulons de roue, contrôlez également les composants
    de la fixation de roue et du moyeu qui peuvent être sollicités simultanément
    ou révéler une usure associée :- Jante — inspecter les trous de passage des
    boulons pour détecter un ovalisation ou une corrosion galvanique qui
    compromettrait le maintien du serrage- Moyeu de roue — vérifier l'état des
    goujons (déformation, corrosion) ; un goujon endommagé doit être remplacé
    avant de monter les nouveaux boulons- Écrou de roue — selon le modèle,
    certains véhicules utilisent des écrous plutôt que des boulons ; contrôler
    l'état des filetages et remplacer en kit- Roulement de roue — un jeu
    excessif dans le moyeu signale un roulement usé, qui peut provoquer des
    vibrations similaires à un boulon mal serré
  S8: >-
    Peut-on réutiliser les boulons de roue après démontage ? Dans la majorité
    des cas oui, à condition qu'ils n'aient pas été serrés au-delà de leur
    couple limite ni dévissés plus de 5 fois. Inspectez visuellement le filetage
    — tout filet écrasé, oxydé en profondeur ou tige légèrement allongée visible
    à l'œil nu signale un boulon à remplacer. Les boulons en acier traité
    supportent plusieurs démontages contrairement aux boulons chromés décoratifs
    bas de gamme. Vibrations au volant après changement de roue : quel est le
    lien avec les boulons ? Les vibrations ressenties après un changement de
    roue peuvent provenir d'un serrage inégal des boulons (une roue excentrée
    vibre), d'un mauvais centrage de la jante sur le moyeu, ou d'un déséquilibre
    de la roue elle-même. Commencez par vérifier le couple de chaque boulon à la
    clé dynamométrique : si un boulon est nettement moins serré que les autres,
    la roue est montée hors axe. Si tous les couples sont corrects, faites
    équilibrer les roues. Quel couple de serrage pour mes boulons de roue ? Le
    couple varie selon le constructeur et la taille du boulon : de 80 Nm pour
    les petits véhicules (Citroën C1, Renault Twingo) à 130 Nm pour les berlines
    et SUV (Peugeot 508, Renault Koleos). Ce couple est indiqué dans le manuel
    d'utilisation du véhicule, sur une étiquette sous le capot ou dans la
    documentation technique. Ne jamais estimer "au feeling" — une clé
    dynamométrique est indispensable. Combien de filets minimum pour un boulon
    de roue ? Le minimum absolu est de 6 filets complets engagés dans le moyeu
    pour garantir la résistance au cisaillement sous charge. Un boulon trop
    court qui n'engage que 3 ou 4 filets peut tenir lors d'un serrage statique
    mais se désolidariser sous les contraintes dynamiques du freinage ou d'un
    choc. Mesurez toujours la longueur filetée de l'origine avant de commander.
---

# Boulon de roue - Guide Diagnostic Complet

## Fonction et Rôle

Fixe la roue sur le moyeu du véhicule

**Actions principales:** fixer, serrer, maintenir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Roue qui emet des claquements**
  roue qui emet des claquements

### 🟡 Symptômes de Sécurité

- **Vibrations lors du freinage**
  vibrations lors du freinage

### 🟢 Autres Symptômes

- serrage impossible boulon tourne vide

## Procédure de Diagnostic

Pour diagnostiquer un problème de boulon de roue:

1. **Inspection visuelle** - Examiner l'état du boulon de roue
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- jante
- moyeu

## Critères de Compatibilité

Pour commander le bon boulon de roue, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"

## FAQ

**Comment choisir Boulon de roue compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Boulon de roue ?**
En cas de vibrations lors du freinage ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Boulon de roue sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
