---
category: direction
slug: cremailliere-de-direction
title: Crémaillère de direction
pg_id: 286
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-25'
verification_status: reviewed
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v4_enriched
  last_enriched_by: script:rag-enrich-metier-templates
  last_enriched_at: '2026-03-26'
domain:
  role: 'La crémaillère de direction est le composant central du train avant qui convertit la rotation du volant en translation
    latérale (mouvement linéaire) via un mécanisme pignon-crémaillère dentée. Elle assure la liaison entre la colonne de direction
    et les roues directrices, conditionnant la précision de trajectoire et la sécurité du véhicule. Elle s''insère dans un
    ensemble comprenant les rotules axiales, les biellettes et les soufflets protecteurs. On distingue trois familles : crémaillère
    non assistée (rare, sur voitures légères anciennes), crémaillère assistée hydrauliquement (pompe + circuits huile) et
    crémaillère à assistance électrique (moteur électromécanique intégré, EPS). La durée de vie moyenne est de 150 000 km,
    conditionnée à l''intégrité des soufflets et joints.'
  components:
  - Corps en alliage aluminium/acier
  - Pignon d'entrée (lié à la colonne de direction)
  - Tige dentée (la crémaillère elle-même)
  - Joints d'étanchéité hydrauliques (sur version hydraulique)
  - Soufflets en caoutchouc (protection contre poussière/eau)
  - Rotules de direction / biellettes (transmission aux roues)
  - Silent-blocs de fixation au berceau
  must_be_true:
  - diriger
  - guider
  - transmettre
  - pignon-crémaillère
  - translation latérale
  must_not_contain:
  - injection
  - freinage
  - distribution
  - turbo
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - barre-de-direction
  - colonne-de-direction
  - pompe-de-direction-assistee
  - rotule-de-direction
  - soufflet-de-direction
  - biellette-de-direction
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - 'Type d''assistance : Identifier si le véhicule est équipé d''une direction sans assistance (rare), hydraulique (DA/HPS)
    ou électrique (EPS/EPAS). Les pièces ne sont pas interchangeables. Présence d''une pompe = hydraulique ; absence de pompe
    + moteur sur crémaillère ou colonne = électrique.'
  - 'Référence OEM constructeur : Vérifier la référence constructeur sur l''ancienne pièce ou dans le catalogue technique.
    Les crémaillères sont fortement spécifiques au modèle, à l''année et à la motorisation. Correspondance par immatriculation
    (TecDoc, ETAI) recommandée.'
  - 'Cotes de fixation et filetage des rotules : Contrôler le taraudage des rotules (ex. M14x1,50), la longueur totale de
    la tige de crémaillère (en mm) et les points de fixation au berceau. Une erreur sur ces cotes rend la pièce inutilisable.'
  - 'Pièce OE / Équivalent OE / Adaptable / Reconditionnée : OE (TRW/ZF, Lemförder, Bosch, JTEKT, Delphi) = qualité garantie,
    prix élevé. Équivalent OE (RIDEX, NTY, LIZARTE, Febi Bilstein) = mêmes specs, prix intermédiaire. Reconditionnée (échange
    standard GPA26, Cevam) = prix bas, garantie réduite.'
  - 'Compatibilité ABS/ESP : Sur certaines crémaillères électriques, le capteur de couple ou d''angle de braquage est intégré.
    La nouvelle pièce doit être compatible avec le système ESP/ABS et peut nécessiter une reprogrammation par valise diagnostic.'
  - 'Type et longueur des soufflets : Vérifier si les soufflets sont fournis avec la crémaillère ou à commander séparément.
    Les dimensions (diamètre d''entrée/sortie, longueur comprimée) varient selon le véhicule.'
  anti_mistakes:
  - 'Oublier la purge du circuit hydraulique après remplacement : toute poche d''air résiduelle génère des bruits (gémissements),
    une assistance irrégulière et une usure prématurée de la pompe. Purger en braquant de butée en butée moteur tournant.'
  - 'Ne pas refaire la géométrie du train avant : c''est l''erreur la plus fréquente. Un remplacement de crémaillère modifie
    systématiquement le parallélisme. Sans correction géométrique, les pneus s''usent anormalement (usure en biseau) et la
    voiture dérive à haute vitesse.'
  - 'Forcer sur les rotules avec un marteau : utiliser un marteau pour déposer les rotules endommage le filetage et le cône.
    Toujours utiliser un extracteur de rotule (chasse-rotule) adapté.'
  - 'Confondre crémaillère mécanique et assistée : les pièces ne sont pas interchangeables. Vérifier impérativement le type
    d''assistance avant commande.'
  - 'Ne pas vérifier les flexibles de servo-direction avant montage : la détérioration interne des flexibles libère des particules
    de caoutchouc dans le circuit, cause principale de panne des crémaillères et pompes neuves (Source: BT-110 Da Silva).'
  - 'Laisser tourner la pompe à sec lors de la purge : maintenir le niveau de liquide dans le réservoir en permanence pendant
    toute la procédure. Une pompe tournant à sec s''endommage immédiatement (Source: BT-110 Da Silva).'
  - 'Ne pas remplacer les deux flexibles quand un seul est défectueux : si un flexible est rigide, dur ou spongieux, l''autre
    est certainement détérioré aussi. Toujours remplacer la paire (Source: BT-110 Da Silva).'
  cost_range:
    min: 7
    max: 2087
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Pièce OE (Origine Équipement)
    description: 'Crémaillère identique à l origine. Fabricants de rang 1 reconnus : TRW/ZF, Lemförder, Bosch, JTEKT, Delphi.
      Compatibilité ESP/ABS garantie.'
  - tier: Équivalent OE (qualité documentée)
    description: Fournisseurs alternatifs respectant les mêmes spécifications techniques. Prix intermédiaire entre OE et reconditionné.
  - tier: Reconditionnée (échange standard)
    description: Crémaillère remanufacturée et testée. Prix bas, garantie généralement réduite (6 à 12 mois). Attention aux
      conditions de reprise du noyau (core return).
  - tier: Générique non qualifié
    description: Non recommandé sur un composant de sécurité actif. Absence de documentation technique fiable.
  brands:
    premium:
    - Lemforder
    - TRW
    standard:
    - Febi
    - Meyle
    - MOOG
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Fuite liquide direction visible sous le véhicule
    severity: securite
  - id: S2
    label: Direction dure ou assistance intermittente
    severity: securite
  - id: S3
    label: Jeu excessif dans le volant
    severity: confort
  - id: S4
    label: Bruit de grincement ou de couinement en tournant
    severity: confort
  - id: S5
    label: Soufflets de crémaillère fissurés ou déchirés
    severity: confort
  - id: S6
    label: Niveau de liquide de direction qui baisse régulièrement
    severity: securite
  causes:
  - 'Usure mécanique : usure des pignons, de la tige dentée ou des joints internes (durée de vie ~150 000 km)'
  - 'Fuite hydraulique : joints d''étanchéité détériorés, soufflets fissurés laissant entrer eau/poussière'
  - 'Défaillance capteur de couple (EPS) : panne électronique sur crémaillère électrique, direction dure intermittente'
  - 'Sollicitations excessives : braquage en butée répété, chocs sur trottoirs, conduite sur pistes dégradées'
  depose_steps:
  - 'Mise en sécurité et préparation : Garer sur surface plane et stable. Serrer le frein de parking. Placer le véhicule sur
    cric hydraulique puis poser les chandelles aux longerons. Ne jamais travailler sous un véhicule tenu seulement par un
    cric.'
  - 'Démontage des roues et déconnexion des rotules : Retirer les roues avant. Déconnecter les rotules de direction aux deux
    extrémités de la crémaillère à l''aide d''un extracteur de rotule (ne jamais frapper à la masse sur la rotule). Déconnecter
    le joint de colonne liant la colonne de direction à la crémaillère.'
  - 'Déconnexion hydraulique (uniquement direction hydraulique) : Démonter les raccords hydrauliques (tuyaux aller et retour
    de la pompe). Récupérer l''intégralité du liquide de direction dans un bac propre. Boucher immédiatement les raccords.
    Vérifier le liquide récupéré sur un chiffon blanc — si des particules métalliques sont visibles, la pompe d''assistance
    doit être remplacée (Source: BT-110 Da Silva).'
  - 'Dépose de la crémaillère : Retirer les boulons de fixation sur le berceau moteur (généralement 2 à 4 points de fixation).
    Faire coulisser la crémaillère hors du berceau en manoeuvrant les roues si nécessaire.'
  - 'Inspection avant remontage : Contrôler l''état des silent-blocs de berceau et des biellettes. Remplacer systématiquement
    les soufflets. Vérifier l''état des rotules axiales. Nettoyer le conduit de retour à l''air comprimé — c''est le seul
    conduit non nettoyé lors de la purge (Source: BT-110 Da Silva).'
  - 'Remontage et serrage au couple : Positionner la nouvelle crémaillère. Serrer les boulons de fixation au couple prescrit
    par le constructeur (clé dynamométrique obligatoire). Reconnecter les durits hydrauliques avec joints neufs. Reconnecter
    les rotules et la colonne. Vérifier et remettre le clapet anti-retour situé dans l''orifice d''alimentation sur certains
    modèles — Ford, Espace V6 notamment (Source: BT-110 Da Silva).'
  - 'Purge du circuit hydraulique (direction hydraulique) : Remplir le réservoir de liquide de direction. Démarrer le moteur.
    Braquer de butée gauche à butée droite lentement et à plusieurs reprises (environ 5 à 10 allers-retours). Recompléter
    le niveau.'
  - 'Géométrie obligatoire : Après tout remplacement de crémaillère, un contrôle et réglage de la géométrie du train avant
    (parallélisme, carrossage) est impératif. À réaliser en atelier équipé.'
  tools_required:
  - Cric hydraulique + chandelles homologuées
  - Extracteur de rotule (chasse-rotule)
  - Jeu de clés à douilles (13, 17, 19, 21 mm selon véhicule)
  - Clé dynamométrique (réglage 20 à 120 N.m selon point)
  - Adaptateurs raccords hydrauliques (direction hydraulique)
  - Bac de récupération liquide
  - Outil de diagnostic OBD (direction électrique EPS uniquement)
  - Flexible d'air comprimé (nettoyage conduit retour)
  quick_checks:
  - Fuite liquide direction visible sous le véhicule ?
  - 'Observer : direction dure ou assistance intermittente ?'
  - 'Observer : jeu excessif dans le volant ?'
  - Bruit de grincement ou de couinement en tournant ?
maintenance:
  interval:
    value: 150000
    unit: km
    note: Durée de vie moyenne de 150 000 km, conditionnée à l'intégrité des soufflets et joints. Contrôler à chaque révision
      les soufflets et le niveau de liquide.
    source: Featured Snippet Oscaro SERP 2026-03
  good_practices:
  - Réaliser la géométrie du train avant (parallélisme, carrossage) après tout remplacement de crémaillère ou de rotule de
    direction.
  - Purger intégralement le circuit hydraulique après remplacement (braquer de butée en butée 5-10 fois moteur tournant, recompléter
    le niveau).
  - Contrôler le niveau de liquide de direction assistée à chaque révision ou tous les 20 000 km.
  - 'Inspecter visuellement les soufflets de crémaillère à chaque contrôle technique ou révision : fissures = remplacement
    immédiat.'
  - 'Sur direction électrique (EPS) : effectuer un reset du capteur d''angle de braquage via valise OBD après remplacement.'
  - 'Vérifier l''état des flexibles de servo-direction lors de chaque remplacement : un flexible rigide, dur ou spongieux
    libère des micro-particules de caoutchouc qui endommagent la crémaillère et le bloc de soupapes. Utiliser uniquement le
    fluide recommandé par le constructeur (Source: BT-110 Da Silva).'
  wear_signs:
  - Fuite de liquide rougeâtre ou brun sous le véhicule (côté train avant)
  - Direction dure par intermittence, surtout à froid
  - Jeu au volant (mouvement sans effet sur les roues)
  - Grincements ou cliquetis lors du braquage
  - Soufflets gonflés, fissurés ou déchirés
  - Voyant direction assistée allumé (EPS)
rendering:
  pgId: '286'
  intro_title: A quoi sert la crémaillère de direction ?
  risk_title: Pourquoi remplacer la crémaillère de direction à temps ?
  risk_explanation: '**Usure mécanique** - Les bruits et fuites indiquent souvent une usure des composants internes (pignons,
    joints, tige dentée). Une crémaillère défectueuse compromet directement la sécurité : perte de contrôle possible en cas
    de blocage ou de jeu excessif.'
  risk_consequences:
  - '**Perte de contrôle de trajectoire** - Un jeu excessif ou un blocage peut rendre le véhicule imprévisible en virage ou
    en évitement d''urgence'
  - '**Défaillance progressive** - La fuite de liquide hydraulique entraîne une perte d''assistance qui s''aggrave, rendant
    la direction de plus en plus dure'
  - '**Dégradation en cascade** - Une crémaillère qui fuit abîme la pompe de direction assistée (fonctionnement à sec) et
    accélère l''usure des pneus (géométrie décalée)'
  - '**Refus au contrôle technique** - Jeu excessif, soufflets déchirés ou fuite visible = contre-visite'
  risk_conclusion: Un diagnostic précoce réduit le risque technique et financier. Ne pas attendre la panne complète.
  arguments:
  - content: Sélection guidée par véhicule, type d'assistance et références OEM.
    icon: check-circle
    title: Compatibilité vérifiée
  - content: Un remplacement à temps évite la casse de la pompe DA et l'usure prématurée des pneus.
    icon: shield-check
    title: Priorité sécurité
  - content: Le guide structure les 6 critères à vérifier avant commande.
    icon: clock
    title: Décision rapide
  - content: La vérification des pièces associées (rotules, soufflets, biellettes) réduit les retours atelier.
    icon: list-check
    title: Montage maîtrisé
  faq:
  - question: Comment choisir la crémaillère de direction compatible avec mon véhicule ?
    answer: Vérifiez d'abord le type d'assistance (hydraulique, électrique ou mécanique), puis la référence OEM constructeur.
      Croisez avec l'immatriculation via TecDoc ou ETAI. Contrôlez les cotes de fixation et le filetage des rotules.
  - question: Quand remplacer la crémaillère de direction ?
    answer: 'Durée de vie moyenne : 150 000 km. Remplacer dès l''apparition de fuites de liquide, de direction dure intermittente,
      de jeu excessif au volant ou de soufflets fissurés.'
  - question: Faut-il refaire la géométrie après remplacement de la crémaillère ?
    answer: Oui, c'est obligatoire. Un remplacement de crémaillère modifie systématiquement le parallélisme. Sans réglage
      géométrique, les pneus s'usent anormalement et la voiture dérive.
  - question: Quelle différence entre crémaillère hydraulique et électrique ?
    answer: La crémaillère hydraulique utilise une pompe et du liquide sous pression. La crémaillère électrique intègre un
      moteur électromécanique (EPS), sans liquide. Les pièces ne sont pas interchangeables.
  - question: Peut-on rouler avec une crémaillère de direction défectueuse ?
    answer: 'C''est dangereux. Une crémaillère défectueuse compromet la direction du véhicule : perte d''assistance, jeu au
      volant, risque de blocage. Intervention rapide recommandée.'
  quality:
    score: 95
    source: manual-serp-research + BT-110 Da Silva
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
warranty_notes:
  source: BT-110 Da Silva (garantie 24 mois)
  exclusions:
  - Montage sur véhicule inadapté
  - Unité démontée totalement ou partiellement
  - Unité renvoyée incomplète
  - Soufflets endommagés
  - Filetage croisé ou serrage excessif des biellettes
  core_return_refusals:
  - Fonderie du corps ou tube endommagé
  - Pattes de fixation ou trous de fixation endommagés
  - Composants internes grippés ou rouillés
  - Unité incomplète ou composants manquants
  - Pignon ou flèche du pignon endommagé
  - Biellettes pliées ou filetage endommagé
  - Ports d'entrée ou de sortie endommagés
  - Dégâts par procédure de dépose incorrecte (flamme, outil coupant)
confusion_pairs:
- piece_a: cremaillere-de-direction
  piece_b: colonne-de-direction
  differentiation: La crémaillère convertit la rotation en translation latérale (au niveau du train avant). La colonne de
    direction transmet la rotation du volant à la crémaillère (entre le volant et la crémaillère).
- piece_a: cremaillere-de-direction
  piece_b: pompe-de-direction-assistee
  differentiation: La crémaillère effectue le mouvement mécanique de braquage. La pompe DA fournit la pression hydraulique
    qui assiste ce mouvement. Les deux sont liées mais distinctes.
- piece_a: cremaillere-de-direction
  piece_b: rotule-de-direction
  differentiation: La crémaillère est le mécanisme central. Les rotules sont les articulations aux extrémités qui relient
    la crémaillère aux biellettes puis aux fusées de roue.
doc_id: 1d2d62f3-1253-5db9-849b-b32a10a665a1
content_hash: sha256:0c49128229f4c146
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
  area: Sous le vehicule, relie le volant aux roues
  access: Par le dessous (pont elevateur recommande)
  adjacent_parts:
  - cremailliere
  - biellette
  - rotule
  - soufflet
installation:
  difficulty: difficile
  time: 1h a 3h
  tools:
  - cle a douille
  - arrache-rotule
  - cle dynamometrique
  prerequisite: Pont elevateur, geometrie a refaire apres
---

# Crémaillère de direction - Guide Diagnostic et Achat Complet

## Fonction et Rôle

La crémaillère de direction est le composant central du train avant qui convertit la rotation du volant en translation latérale (mouvement linéaire) via un mécanisme pignon-crémaillère dentée. Elle assure la liaison entre la colonne de direction et les roues directrices, conditionnant la précision de trajectoire et la sécurité du véhicule.

**Trois familles :**
- **Crémaillère non assistée** (rare, voitures légères anciennes)
- **Crémaillère assistée hydrauliquement** (pompe DA + circuits huile)
- **Crémaillère à assistance électrique (EPS)** (moteur électromécanique intégré)

**Composants clés :** corps en alliage, pignon d'entrée, tige dentée, joints d'étanchéité, soufflets en caoutchouc, rotules/biellettes, silent-blocs de fixation.

**Durée de vie moyenne :** 150 000 km (conditionnée à l'intégrité des soufflets et joints).

## Symptômes de Défaillance

### Sécurité (intervention urgente)

- **Fuite liquide direction visible sous le véhicule** — liquide rougeâtre ou brun côté train avant
- **Direction dure ou assistance intermittente** — surtout à froid, peut indiquer un défaut de capteur de couple (EPS) ou une fuite hydraulique
- **Niveau de liquide de direction qui baisse régulièrement** — signe de fuite active sur joints ou raccords

### Confort (surveillance)

- **Jeu excessif dans le volant** — mouvement du volant sans effet sur les roues, usure de la tige dentée
- **Bruit de grincement ou de couinement en tournant** — manque de lubrification interne, usure des pignons ou fuite hydraulique interne
- **Soufflets de crémaillère fissurés ou déchirés** — entrée d'eau et de poussière, usure accélérée

## Procédure de Diagnostic

1. **Inspection visuelle** — Examiner l'état des soufflets, rechercher les fuites de liquide sous le véhicule
2. **Test fonctionnel** — Braquer de butée en butée moteur tournant, vérifier la fluidité de l'assistance
3. **Contrôle du jeu** — Faire bouger le volant moteur arrêté, vérifier l'absence de jeu mécanique
4. **Diagnostic sonore** — Localiser la source des bruits anormaux (grincement, cliquetis, gémissement)
5. **Contrôle du niveau de liquide** — Vérifier le réservoir de liquide DA (direction hydraulique)


## Entretien et Intervalles

- **Intervalle** : 150000
- Durée de vie moyenne de 150 000 km, conditionnée à l'intégrité des soufflets et joints. Contrôler à chaque révision les soufflets et le niveau de liquide.

## Causes Probables

- **Usure mécanique** — Usure des pignons, de la tige dentée ou des joints internes (~150 000 km)
- **Fuite hydraulique** — Joints d'étanchéité détériorés, soufflets fissurés laissant entrer eau/poussière
- **Défaillance capteur de couple (EPS)** — Panne électronique sur crémaillère électrique
- **Sollicitations excessives** — Braquage en butée répété, chocs sur trottoirs

## Procédure de Remplacement (Dépose)

1. **Mise en sécurité** — Surface plane, frein de parking, cric + chandelles aux longerons
2. **Démontage roues et rotules** — Retirer les roues avant, déconnecter les rotules avec extracteur (pas de marteau)
3. **Déconnexion hydraulique** (si DA) — Démonter les raccords, récupérer le liquide, boucher les raccords
4. **Dépose crémaillère** — Retirer les boulons de fixation sur le berceau (2 à 4 points)
5. **Inspection** — Contrôler silent-blocs, biellettes, soufflets, rotules axiales
6. **Remontage au couple** — Serrer au couple prescrit (clé dynamométrique obligatoire)
7. **Purge hydraulique** — Remplir, braquer butée-à-butée 5-10 fois, recompléter
8. **Géométrie obligatoire** — Parallélisme et carrossage en atelier équipé

**Outils requis :** cric hydraulique + chandelles, extracteur de rotule, clés à douilles (13-21 mm), clé dynamométrique, bac de récupération, outil OBD (EPS), flexible d'air comprimé.

## Procédure de Rinçage du Circuit Hydraulique (Source: BT-110 Da Silva)

**Prérequis :** Ce rinçage est obligatoire pour bénéficier de la garantie 24 mois sur les crémaillères et pompes Da Silva. Il complète les BT-171 (précautions montage pompes) et BT-174 (rinçage circuit hydraulique).

1. **Vérifier tous les flexibles de servo-direction** — La détérioration interne des flexibles est la cause n°1 de panne. Les flexibles se morcèlent de l'intérieur, libérant des particules de caoutchouc dans la crémaillère et le bloc de soupapes.
2. **Si un flexible est rigide, dur ou spongieux → remplacer LES DEUX flexibles du circuit.** Si l'un est détérioré, l'autre l'est certainement aussi.
3. **Utiliser UNIQUEMENT le fluide recommandé par le constructeur.** Se référer au manuel utilisateur ou aux spécifications constructeur.
4. **Flexibles déconnectés, pomper du nouveau liquide** — Placer le flexible de sortie de la pompe dans un bac. Remplir le réservoir de nouveau liquide. Démarrer le moteur au ralenti. Continuer à verser jusqu'à ce que le fluide sortant soit propre.
5. **NE PAS LAISSER TOURNER LA POMPE À SEC** — S'assurer que le réservoir reste rempli pendant toute la procédure.
6. **Vérifier les particules métalliques** — Renverser un peu de liquide récupéré sur un chiffon blanc. Si des particules métalliques sont visibles, la pompe d'assistance doit être remplacée.
7. **Comparer la nouvelle unité avec l'ancienne** avant fixation.
8. **Nettoyer le conduit de retour à l'air comprimé** — C'est le seul conduit non nettoyé lors de l'étape précédente.
9. **Déposer les capuchons de protection** et brancher les conduits d'alimentation. **Remettre le clapet anti-retour** situé au fond de l'orifice d'alimentation sur certains modèles (Ford, Espace V6). Remplacer les joints toriques des raccords si nécessaire.
10. **Remplir le réservoir au niveau maxi.** Braquer de butée en butée lentement, moteur tournant, à plusieurs reprises.
11. **Recompléter le niveau**, vérifier l'absence de fuites sur tous les raccords.
12. **Essai routier** — Confirmer l'absence de bruit anormal et le fonctionnement correct de l'assistance.

## Guide de Sélection : 6 Critères

1. **Type d'assistance** — Mécanique / Hydraulique (DA/HPS) / Électrique (EPS/EPAS) — non interchangeables
2. **Référence OEM** — Vérifier via TecDoc, ETAI ou immatriculation
3. **Cotes de fixation** — Taraudage rotules, longueur tige, points de fixation berceau
4. **Qualité pièce** — OE (TRW, Lemförder, Bosch) / Équivalent OE (RIDEX, Febi) / Reconditionnée
5. **Compatibilité ABS/ESP** — Capteur de couple intégré sur certaines EPS
6. **Soufflets** — Fournis ou à commander séparément, vérifier dimensions

## Erreurs Fréquentes à Éviter

- Oublier la purge du circuit hydraulique après remplacement
- Ne pas refaire la géométrie du train avant (erreur la plus fréquente)
- Forcer sur les rotules au marteau au lieu d'utiliser un extracteur
- Confondre crémaillère mécanique et assistée (pièces non interchangeables)
- Ne pas vérifier les flexibles de servo-direction avant montage — cause n°1 de panne (Source: BT-110 Da Silva)
- Laisser tourner la pompe à sec lors de la purge (Source: BT-110 Da Silva)
- Ne pas remplacer les deux flexibles quand un seul est défectueux (Source: BT-110 Da Silva)

## Bonnes Pratiques d'Entretien

- Géométrie après tout remplacement de crémaillère ou de rotule
- Purge intégrale du circuit hydraulique après remplacement
- Contrôle du niveau de liquide DA tous les 20 000 km
- Inspection visuelle des soufflets à chaque révision
- Reset capteur d'angle de braquage via OBD sur direction électrique (EPS)
- Vérifier l'état des flexibles de servo-direction lors de chaque remplacement (Source: BT-110 Da Silva)

## Pièces Associées

Lors du remplacement, vérifier également :

- barre-de-direction
- colonne-de-direction
- pompe-de-direction-assistee
- rotule-de-direction
- soufflet-de-direction
- biellette-de-direction
- bras-de-suspension
- rotule-de-suspension

## Confusions Fréquentes

| Pièce confondue | Différence |
|---|---|
| **Colonne de direction** | Transmet la rotation du volant à la crémaillère (entre volant et crémaillère). La crémaillère convertit cette rotation en mouvement latéral. |
| **Pompe de direction assistée** | Fournit la pression hydraulique. La crémaillère effectue le mouvement mécanique. |
| **Rotule de direction** | Articulation aux extrémités de la crémaillère, relie aux biellettes puis fusées de roue. |

## Fourchette de Prix (2026)

| Type | Prix pièce |
|------|------------|
| Manuelle | 50 – 150 EUR |
| Hydraulique | 125 – 550 EUR |
| Électrique | 130 – 670 EUR |
| Reconditionnée | 150 – 350 EUR |

*Sources : Shopping Google, Oscaro, Mister-Auto, Ovoko (mars 2026), BT-110 Da Silva (Rev. 02, 04/2013)*

## FAQ

**Comment choisir la crémaillère de direction compatible avec mon véhicule ?**
Vérifiez d'abord le type d'assistance (hydraulique, électrique ou mécanique), puis la référence OEM constructeur. Croisez avec l'immatriculation via TecDoc ou ETAI. Contrôlez les cotes de fixation et le filetage des rotules.

**Quand remplacer la crémaillère de direction ?**
Durée de vie moyenne : 150 000 km. Remplacer dès l'apparition de fuites de liquide, de direction dure intermittente, de jeu excessif au volant ou de soufflets fissurés.

**Faut-il refaire la géométrie après remplacement de la crémaillère ?**
Oui, c'est obligatoire. Un remplacement de crémaillère modifie systématiquement le parallélisme. Sans réglage géométrique, les pneus s'usent anormalement et la voiture dérive.

**Quelle différence entre crémaillère hydraulique et électrique ?**
La crémaillère hydraulique utilise une pompe et du liquide sous pression. La crémaillère électrique intègre un moteur électromécanique (EPS), sans liquide. Les pièces ne sont pas interchangeables.

**Peut-on rouler avec une crémaillère de direction défectueuse ?**
C'est dangereux. Une crémaillère défectueuse compromet la direction du véhicule : perte d'assistance, jeu au volant, risque de blocage. Intervention rapide recommandée.


## Symptomes supplementaires

<!-- materialized-from-db diagnostic/direction-cremaillere.md 2026-02-15 -->
### Diagnostic - Direction et crémaillère

# Direction et crémaillère - Diagnostic complet

## Symptômes au volant

### Volant dur
- **Direction assistée défaillante** : Pompe DA qui siffle ou ne fournit plus assez de pression. Vérifier le niveau de liquide DA et l'état de la courroie.
- **Crémaillère grippée** : Corrosion interne ou manque de lubrification. Le volant est dur dans les deux sens, surtout à froid.
- **Colonne de direction usée** : Cardan de direction grippé, surtout après un long stationnement.

### Jeu dans le volant
- **Rotules de direction usées** : Jeu perceptible en tournant le volant sans que les roues bougent. Contrôler visuellement le jeu en secouant la roue.
- **Biellettes de direction desserrées** : Claquement en manœuvrant, jeu latéral au volant.
- **Crémaillère avec jeu interne** : Usure des pignons ou des bagues de guidage.

### Bruits en braquant
- **Craquement dans les virages** : Soufflet de cardan déchiré, graisse partie, croisillon usé.
- **Grincement à basse vitesse** : Roulements de butée d'amortisseur ou coupelles supérieures usées.
- **Sifflement continu** : Pompe de direction assistée en fin de vie ou niveau de liquide bas.

## Fuites de direction

### Fuite de liquide DA
- **Au niveau du bocal** : Joint de bouchon ou bocal fissuré.
- **Sur les raccords** : Durites de pression ou retour qui fuient aux colliers.
- **Sur la crémaillère** : Joints spy de crémaillère usés, fuite visible aux soufflets.

## Vérifications simples

- Contrôler le niveau de liquide de direction assistée (bocal sous le capot)
- Inspecter les soufflets de crémaillère (pas de déchirure, pas de fuite)
- Secouer la roue à 9h-15h pour détecter le jeu dans les rotules
- Tourner le volant moteur allumé : le mouvement doit être fluide et silencieux

## Quand consulter un professionnel

- Volant qui vibre ou tire d'un côté en ligne droite
- Bruit métallique constant dans la direction
- Fuite importante de liquide DA (risque de blocage)
- Jeu excessif au volant détecté au contrôle technique
