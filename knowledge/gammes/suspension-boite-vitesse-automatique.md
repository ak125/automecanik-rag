---
category: transmission
slug: suspension-boite-vitesse-automatique
title: Suspension boite vitesse automatique
pg_id: 248
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
business_priority: low
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:materialize-db-to-md
  last_enriched_at: '2026-04-03'
  v5_migrated_at: '2026-03-29'
domain:
  role: Absorber les vibrations et mouvements de la boite de vitesses automatique pour reduire les a-coups transmis a la caisse
  must_be_true:
  - absorber les vibrations
  - maintenir la boite en position
  - reduire les a-coups
  must_not_contain:
  - universel
  - tous modeles
  - adaptable tous
  confusion_with:
  - term: support-moteur
    difference: Le support moteur maintient le moteur, la suspension BVA maintient specifiquement la boite de vitesses automatique
  - term: suspension-boite-vitesse
    difference: La version manuelle peut avoir un support different, verifier la reference selon le type de boite
  related_parts:
  - support-moteur
  - cardan
  - joint-d-arbre-de-transmission
  - mecatronique-boite-automatique
selection:
  criteria:
  - Marque de votre vehicule
  - Modele de votre vehicule
  - Motorisation de votre vehicule
  - Annee de votre vehicule
  - Type de boite automatique (conventionnelle, DSG, CVT)
  - Position du support (superieur, inferieur, lateral)
  anti_mistakes:
  - universel
  - tous modeles
  - adaptable tous
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
    label: Vibrations excessives au ralenti en position D ou R
    severity: confort
  - id: S2
    label: A-coups lors des passages de rapport
    severity: confort
  - id: S3
    label: Bruit sourd ou cognement en passant de P a D ou R
    severity: confort
  - id: S4
    label: Mouvement excessif du groupe motopropulseur a l'acceleration
    severity: securite
  - id: S5
    label: Caoutchouc du silent-bloc fissure ou affaisse
    severity: confort
  causes:
  - usure naturelle du caoutchouc (chaleur, vibrations, age)
  - fuite d'huile sur le support hydraulique
  - contraintes mecaniques excessives (conduite sportive)
  quick_checks:
  - Vibrations excessives au ralenti en position D ou R ?
  - 'Observer : a-coups lors des passages de rapport ?'
  - Bruit sourd ou cognement en passant de P a D ou R ?
  - 'Observer : mouvement excessif du groupe motopropulseur a l''acceleration ?'
maintenance:
  interval:
    value: selon etat
    unit: condition
    note: Verifier visuellement tous les 80000 km. Remplacer si caoutchouc fissure, affaisse ou decole.
  wear_signs:
  - Vibrations excessives au ralenti en position D ou R
  - A-coups lors des passages de rapport
  - Bruit sourd ou cognement en passant de P a D ou R
  - Mouvement excessif du groupe motopropulseur a l'acceleration
  - Caoutchouc du silent-bloc fissure ou affaisse
  good_practices:
  - Verifier le niveau d huile de boite selon preconisation constructeur
  - Controle des soufflets de protection (pas de fuite de graisse)
  - Remplacement de la bague d etancheite en cas de fuite
  - Inspection des cardans et croisillons a chaque revision
rendering:
  pgId: '248'
  faq:
  - question: Comment savoir si la suspension de BVA est HS ?
    answer: Vibrations au ralenti en D/R, bruit sourd au passage P vers D, mouvement excessif du moteur a l'acceleration.
      Inspection visuelle du silent-bloc (fissures, affaissement).
  - question: Peut-on rouler avec une suspension de BVA usee ?
    answer: Oui mais les vibrations s'aggravent et peuvent endommager les canalisations hydrauliques ou les cardans a terme.
  - question: Suspension BVA OE ou adaptable ?
    answer: Privilegier l'OE pour la duree de vie et la compatibilite exacte. Les generiques peuvent avoir une durete differente.
  - question: Combien coute le remplacement ?
    answer: La piece coute entre 30 et 200 EUR. La main d'oeuvre peut etre elevee si l'acces est difficile (1h a 3h).
  - question: Quelle erreur eviter ?
    answer: Ne pas confondre support moteur et support BVA (references differentes). Toujours verifier les 2 ou 3 supports
      du vehicule en meme temps.
  quality:
    score: 60
    source: manual:claude-r3-kp
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modeles
  - adaptable tous
  requires_vehicle: true
doc_id: 7c50d9b0-38e5-599d-bc2e-5203882fa706
content_hash: sha256:051ba7072c928e86
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
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: hydraulique
    source_ref: corpus RAG web OEM
  - type: pneumatique
    source_ref: corpus RAG web OEM
  - type: électrique
    source_ref: corpus RAG web OEM
  technical_notes:
    val_10_a: 10 a
    val_5_a: 5 a
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: Le support de bo&icirc;te de vitesses est un élément essentiel qui sert à supporter la bo&icirc;te de votre véhicule.
    Le support bo&icirc;te de vitesses est différent d'un véhicule à un autre, suivant les types des bo&icirc;tes de vitesses
    et la fixation de la bo&icirc;te par rapport au moteur. On peut avoir des supports en bas de la bo&icirc;te de vitesses
    (billette anti couple) et on peut avoir des supports en haut de la bo&icirc;te de vitesses avec le support moteur.
  S2: Le support de bo&icirc;te de vitesses n'a pas de période de remplacement d'après les constructeurs mais il faut faire
    un contrôle des fixations et de l'état du support à chaque fois o&ugrave; on constate qu'il y a un turc bizarre surtout
    les bruits et vibration au niveau de la bo&icirc;te de vitesses.En cas de défectuosité du support, on sent des bruits
    de grincements importants dans l'habitacle, le cardan risque très vite de s'ab&icirc;mer et de faire des bruits de claquement.
    Dans les cas extr&ecirc;mes, le risque peut &ecirc;tre de voir les éléments supportés tomber. Lors du remplacement du
    support bo&icirc;te de vitesses il faut bien soutenir le moteur pour ne pas avoir le risque que le moteur tombe.
  S3: 'La suspension de boîte de vitesses automatique (également appelée support de boîte, silent-bloc de boîte ou coussinet
    de boîte) remplit un double rôle : maintenir la boîte de vitesses dans sa position géométrique exacte et absorber les
    vibrations et les chocs transmis entre la boîte et la caisse du véhicule. Un support usé ou mal choisi génère des bruits,
    des vibrations et accélère l''usure des transmissions et des joints de boîte. Le choix doit prendre en compte plusieurs
    paramètres précis. - Identifier la position exacte sur le véhicule : les boîtes automatiques sont généralement maintenues
    par 2 à 4 supports selon le modèle (support avant, arrière, latéral gauche, latéral droit, et parfois un support central
    sur les boîtes lourdes). Chaque position a une géométrie spécifique, une orientation différente et une dureté d''insert
    élastomère adaptée aux efforts de cette position. Commander sur la désignation exacte de la position, pas uniquement sur
    la référence boîte. - Matériau de l''insert élastomère : trois types existent selon les constructeurs et les applications
    : - Caoutchouc standard : insert naturel ou synthétique, bon isolant vibratoire, adapté aux conditions normales. Se dégrade
    progressivement sous l''effet de la chaleur et des huiles. - Hydro-élastique (rempli de liquide) : chambre interne remplie
    de glycol qui dissipe l''énergie vibratoire par effet d''amortissement hydraulique. Meilleur confort que le caoutchouc
    standard, particulièrement adapté aux boîtes automatiques qui génèrent des à-coups au changement de rapport. Reconnaissable
    à son corps plus épais. - Polyuréthane sport : insert plus dur, meilleure tenue géométrique, utilisé en préparation ou
    sur les châssis rigides. Transmet davantage de vibrations dans l''habitacle — ne pas utiliser sur une voiture de route
    classique. - Résistance au couple : les boîtes automatiques modernes (ZF 8HP, Aisin 6 vitesses, DSG 7, CVT) génèrent des
    couples de torsion importants et des à-coups lors des changements de rapport en mode manuel ou sportif. Le support doit
    être homologué pour le couple maxi de la boîte (information dans la documentation technique véhicule). Un support sous-dimensionné
    cède ou se déchire prématurément. - Compatibilité véhicule complète : marque, modèle, motorisation, année ET type de boîte
    (AT classique, CVT, DSG double embrayage). Un support de boîte manuelle ne convient jamais à une boîte automatique même
    sur le même modèle de véhicule, car les dimensions et les propriétés mécaniques sont différentes. Vérifier la compatibilité
    sur la liste du fabricant ou via la référence OEM. - Marques recommandées : Febi Bilstein, Hutchinson, Lemförder, Tedgum,
    Corteco pour les équipementiers OES. SWAG, Meyle pour les alternatives économiques. Eviter les pièces sans marque ni référence
    d''origine.'
  S4_DEPOSE: 'L''opération nécessite un pont élévateur ou un fosset de travail. Prévoir 1 à 3 heures selon le modèle, la position
    du support et l''état de corrosion des boulons. Une boîte automatique pèse 60 à 120 kg — le soutien de la boîte pendant
    l''intervention est obligatoire. - Lever et caler le véhicule en sécurité : monter sur pont à bras réglables ou sur chandelles
    stables placées sous les points de levage constructeur (renforts de caisse). Ne jamais travailler sous un véhicule soutenu
    uniquement par un cric hydraulique — le risque d''effondrement est mortel. Retirer la roue du côté de la transmission
    si l''accès au support nécessite de déposer le cardan. - Soutenir la boîte de vitesses avant toute dépose : placer un
    cric de transmission (cric à fourche ou cric à selle universelle) sous le carter de boîte, légèrement en charge (le cric
    soutient le poids mais ne soulève pas). Cette étape est impérative — sans ce soutien, lors du desserrage du dernier boulon
    de support, la boîte bascule et transfère 60 à 120 kg de charge sur les demi-arbres de transmission, risquant de déchirer
    les soufflets de cardan ou de plier les demi-arbres. - Identifier et photographier les points de fixation : avant de commencer
    à dévisser, photographier la position exacte de chaque boulon et l''orientation du support. Certains supports ont une
    position de montage imposée (marques de repérage sur le caoutchouc ou flèche indiquant le sens de charge). - Traiter les
    boulons corrodés : les boulons de support de boîte sont souvent en acier de haute résistance (classe 10.9) et peuvent
    être fortement corrodés après 10 à 20 ans. Appliquer un produit dégrippant (WD-40 Specialist, Penetrating Oil) 30 minutes
    avant le début de l''intervention. Si les boulons résistent, utiliser un rallonge de clé à choc plutôt que de forcer avec
    une clé plate qui risque de glisser et d''abîmer l''hexagone. - Déposer le support usagé : une fois tous les boulons retirés,
    descendre progressivement le cric de boîte de 2 à 3 cm pour libérer le support. Inspecter la traverse ou le berceau sur
    lequel le support se fixe : toute déformation, fissure ou corrosion avancée du berceau doit être traitée avant la repose
    du support neuf. - Contrôler l''état des pièces connexes : profiter de l''accès à la transmission pour inspecter les soufflets
    de cardan, les roulements de transmission et les joints d''étanchéité de boîte (joint de sortie d''arbre). Un soufflet
    fissuré ou un joint qui fuit est à remplacer maintenant pour éviter une seconde intervention à court terme. - Poser le
    nouveau support : engager les boulons à la main sur les premiers filets. Aligner la boîte dans sa position nominale (vérifier
    l''absence de contrainte sur les demi-arbres) puis remonter le cric de boîte si nécessaire. Serrer les boulons au couple
    constructeur indiqué (généralement 50 à 100 N.m selon le modèle et la classe des boulons). Utiliser une clé dynamométrique
    — un sous-serrage provoque un desserrage en roulage, un sur-serrage risque de fissurer l''insert élastomère du support
    neuf. - Relâcher le cric de boîte progressivement : une fois tous les boulons serrés, descendre le cric lentement. Observer
    que la boîte repose correctement sur le support neuf sans contrainte ni bascule. Retirer le cric.'
  S5: '- Travailler sans soutenir la boîte : c''est l''erreur la plus dangereuse et la plus coûteuse. Une boîte automatique
    pèse 60 à 120 kg. Sans cric de transmission, le poids lors du dernier boulon dévissé se reporte brutalement sur les demi-arbres
    de transmission. Les conséquences : soufflets de cardan déchirés, demi-arbre plié, joint de boîte arraché. Le coût de
    ces dégâts secondaires dépasse largement celui du support. Le cric de boîte (cric à fourche ou selle de transmission)
    est l''outil indispensable. - Installer un support de dureté inadaptée : un insert élastomère trop souple laisse la boîte
    se déplacer lors des changements de rapport et des accélérations. Les symptômes : chocs en mode D/R, vibrations dans le
    plancher, usure rapide des cardans. A l''inverse, un insert trop dur (polyuréthane sport monté sur route) transmet toutes
    les vibrations moteur et boîte à l''habitacle, rendant la conduite inconfortable. Toujours choisir l''insert de dureté
    d''origine ou hydro-élastique si disponible. - Remplacer un seul support quand les autres sont usés : si un support cède,
    les autres on généralement la même ancienneté et le même niveau d''usure. Remplacer un seul support déséquilibre les efforts
    et accélère la dégradation des supports adjacents. Inspecter tous les supports lors de l''accès (visuel : caoutchouc craquelé,
    décollé de l''armature, déformé) et les remplacer par lot si nécessaire. - Confondre support de boîte automatique et support
    moteur : sur les motorisations transversales, le support de boîte et le support moteur sont côte à côte et peuvent se
    ressembler. La désignation sur la facture ou la commande doit préciser explicitement "support boîte automatique" (ou "support
    boîte de vitesses") avec la position (avant/arrière/gauche/droit). Monter un support moteur à la place d''un support boîte
    fonctionne souvent pendant quelques semaines, puis génère des contraintes anormales et des bruits. - Ne pas respecter
    le couple de serrage : les boulons de support de boîte sont en général de classe 10.9 (haute résistance, marqués sur la
    tête). Un sous- serrage laisse le boulon se desserrer en roulage — risque de perte du support. Un sur-serrage fissure
    l''insert élastomère du support neuf immédiatement. Toujours utiliser une clé dynamométrique avec le couple indiqué dans
    la documentation constructeur. - Omettre de vérifier l''alignement de la boîte après montage : après pose du support neuf,
    vérifier que les demi-arbres de transmission ne présentent pas d''angle anormal ou de contrainte axiale. Un demi-arbre
    sous tension permanente s''use prématurément et peut se casser.'
  S6: '- Test des passages de rapport D/R au ralenti : démarrer le moteur au ralenti et passer successivement de N (neutre)
    à D (drive) puis de D à R (reverse) plusieurs fois. La boîte doit s''engager sans choc sourd ni bruit de claquement. Un
    bruit de choc lors de l''engagement indique que le support neuf n''est pas correctement positionné ou que son couple de
    serrage est insuffisant — la boîte se déplace encore en se solidarisant au rapport. - Essai de conduite avec accélérations
    progressives et franches : effectuer un trajet court avec accélérations progressives puis quelques accélérations franches
    depuis l''arrêt. Observer l''absence de vibrations dans le plancher, le siège conducteur et la colonne de direction. Des
    vibrations perceptibles à mi-régime (1 500 à 2 500 tr/min) indiquent un support de dureté inadaptée ou un support adjacent
    usé non remplacé. - Contrôle visuel de tous les points de fixation : après 5 à 10 minutes de roulage, lever le véhicule
    ou l''inspecter en sous-caisse. Contrôler visuellement que chaque boulon est en place et qu''aucun ne présente de signe
    de desserrage (trace de rotation, surface brillante autour de la tête). Si un boulon montre un mouvement, le resserrer
    au couple. - Vérification de l''alignement des demi-arbres de transmission : inspecter les deux demi-arbres et leurs joints
    de cardan (soufflets). Les soufflets ne doivent pas être plissés anormalement ni montrer de tension axiale excessive.
    Un demi-arbre sous contrainte produit un claquement caractéristique à la reprise d''accélération ou lors des virages serrés.
    - Vérification de l''absence de fuite d''huile de boîte : lors du remontage, le joint de sortie d''arbre (joint spy de
    boîte) peut avoir été légèrement déplacé. Inspecter les joints d''étanchéité de chaque côté de la boîte avec une lingette
    propre après 15 minutes de conduite. Toute trace d''huile ATF (rouge, rosé) impose une intervention immédiate avant que
    le niveau de boîte baisse trop bas.'
  S7: La suspension de boîte automatique s'inscrit dans un ensemble de pièces qui maintiennent le groupe moto-propulseur dans
    sa position géométrique. Une usure de support génère des contraintes sur toutes les pièces voisines, créant un phénomène
    d'usure en cascade. - Support moteur — le support moteur et le support de boîte travaillent en équipe pour maintenir l'ensemble
    moteur-boîte. Si le support de boîte est usé, le support moteur est généralement dans un état similaire (même ancienneté,
    mêmes conditions thermiques). Les inspecter simultanément — un ensemble de supports à remplacer réduit les coûts de main
    d'œuvre en réalisant l'opération en une seule fois. - Cardan (demi-arbre de transmission) — l'usure du support de boîte
    laisse la boîte se déplacer de son axe nominal. Ce déplacement crée un angle de travail excessif sur les joints de cardan
    qui génère une usure prématurée des roulements et des soufflets. Si des vibrations ou des claquements au cardan étaient
    présents avant le remplacement du support, inspecter les cardans après la pose. - Joint de cardan (soufflet) — profiter
    de l'accès en sous-caisse pour inspecter les soufflets de cardan des deux côtés. Un soufflet fissuré ou déchiré doit être
    remplacé avant que la graisse ne s'échappe et que le joint universel ne s'abîme. Un soufflet neuf coûte 15 à 30 euros
    — un cardan complet coûte 80 à 200 euros. - Huile de boîte automatique (ATF) — lors de l'accès en sous-caisse, vérifier
    le niveau d'huile ATF. Si la boîte a vibré pendant une longue période avec un support usé, les contraintes internes peuvent
    avoir dégradé le fluid ATF. Une vidange est recommandée si le kilométrage le justifie (généralement tous les 60 000 à
    120 000 km selon le constructeur). - Joint d'étanchéité de boîte automatique — les vibrations d'une boîte mal supportée
    sollicitent les joints de sortie d'arbre et peuvent créer de légères fuites. Inspecter les deux joints de sortie lors
    de l'accès et les remplacer si une suintement est visible.
  S8: 'Quels symptômes indiquent qu''un support de boîte automatique est usé ? Les symptômes les plus caractéristiques sont
    : un choc sourd ou un claquement lors de l''engagement du rapport D (drive) ou R (reverse) depuis le neutre, des vibrations
    dans le plancher et le siège à l''accélération, un bruit de ferraille lors des à-coups moteur ou lors du changement de
    mode de conduite (éco, sport). En sous-caisse, l''inspection visuelle révèle généralement un insert élastomère craquelé,
    déchiré, ou décollé de son armature métallique — parfois avec une déformation visible en compression ou en cisaillement.
    Sur les supports hydro-élastiques, une fuite de liquide interne (tache sombre sur le support) confirme la défaillance.
    Faut-il faire un alignement des roues après remplacement du support de boîte ? En règle générale, non. Le support de boîte
    agit sur la position du groupe moto-propulseur mais pas directement sur la géométrie des trains roulants. Cependant, si
    la boîte est restée longtemps hors position avec un support effondré, des contraintes ont pu se transmettre aux demi-arbres
    de transmission et aux joints de cardan. Il est prudent de faire contrôler le train avant et d''inspecter les cardans
    si des irrégularités d''usure des pneus sont constatées, mais un alignement des roues n''est pas systématiquement nécessaire.
    Peut-on rouler avec un support de boîte automatique défaillant ? La conduite reste techniquement possible sur courte distance,
    mais des dégâts secondaires s''accumulent rapidement. La boîte mal maintenue exerce des contraintes permanentes sur les
    soufflets de cardan, les demi-arbres et les joints d''étanchéité de sortie de boîte. Sur les véhicules à traction ou à
    transmission intégrale, le risque de rupture d''un demi-arbre ou de déchirure d''un soufflet est réel si l''on continue
    à conduire de façon sportive. Traiter le problème dans les semaines qui suivent l''apparition des symptômes — ne pas attendre
    la casse. Le remplacement du support de boîte nécessite-t-il une vidange de la boîte ? Non, sauf si une fuite d''huile
    a été constatée lors de l''accès. Le remplacement du support élastomère externe ne touche pas au circuit hydraulique interne
    de la boîte automatique. C''est cependant une occasion pratique de planifier une vidange de boîte si le kilométrage le
    justifie — les intervalles varient selon les constructeurs de 60 000 km (Toyota, Honda) à 120 000 km (Volkswagen, BMW)
    pour les boîtes dites "remplissage à vie". Certains constructeurs ne prévoient pas de vidange mais une vidange préventive
    reste recommandée après 100 000 km. Combien de supports de boîte faut-il remplacer en une fois ? Il est fortement recommandé
    de remplacer l''ensemble des supports de boîte en une seule intervention. Les boîtes automatiques sont généralement maintenues
    par 2 à 4 supports qui vieillissent simultanément (mêmes conditions thermiques, même ancienneté). Si un support cède en
    premier, les autres sont souvent à un stade d''usure avancé. Remplacer un seul support reporte la charge sur les autres
    et provoque une défaillance rapide avec une seconde intervention et une seconde facture de main d''œuvre. Le coût des
    supports élastomères supplémentaires est marginal par rapport au coût de la dépose.'
---

# Suspension boite vitesse automatique - Guide Diagnostic

## Fonction et Role

Absorber les vibrations et mouvements de la boite de vitesses automatique.

## Symptomes de Defaillance

- Vibrations excessives au ralenti en position D ou R
- A-coups lors des passages de rapport
- Bruit sourd en passant de P a D ou R
- Mouvement excessif du groupe motopropulseur
- Caoutchouc du silent-bloc fissure ou affaisse

## Pieces Associees

- support-moteur
- cardan
- joint-d-arbre-de-transmission
- mecatronique-boite-automatique

## FAQ

**Comment savoir si la suspension de BVA est HS ?**
Vibrations au ralenti en D/R, bruit sourd au passage P vers D, mouvement excessif du moteur a l'acceleration. Inspection visuelle du silent-bloc (fissures, affaissement).

**Peut-on rouler avec une suspension de BVA usee ?**
Oui mais les vibrations s'aggravent et peuvent endommager les canalisations hydrauliques ou les cardans a terme.

**Suspension BVA OE ou adaptable ?**
Privilegier l'OE pour la duree de vie et la compatibilite exacte. Les generiques peuvent avoir une durete differente.

**Combien coute le remplacement ?**
La piece coute entre 30 et 200 EUR. La main d'oeuvre peut etre elevee si l'acces est difficile (1h a 3h).

**Quelle erreur eviter ?**
Ne pas confondre support moteur et support BVA (references differentes). Toujours verifier les 2 ou 3 supports du vehicule en meme temps.

## Entretien et Intervalles

- **Intervalle** : selon etat
- Verifier visuellement tous les 80000 km. Remplacer si caoutchouc fissure, affaisse ou decole.


## References supplementaires

<!-- materialized-from-db manual/eeb86ff10147 2026-04-03 -->
### Données techniques OEM — Suspension boite vitesse automatique

# Données techniques OEM — Suspension boite vitesse automatique
Source : fr.wikipedia.org (1 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- hydraulique
- pneumatique
- électrique
