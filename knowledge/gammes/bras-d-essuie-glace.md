---
category: accessoires
slug: bras-d-essuie-glace
title: Bras d'essuie-glace
pg_id: 301
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
  role: Supporte et maintient le balai contre le pare-brise
  must_be_true:
  - supporter
  - maintenir
  - plaquer
  must_not_contain:
  - caoutchouc
  - lame
  - capteur abs
  - freinage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - supporter
  - maintenir
  - plaquer
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
    min: 50
    max: 300
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
    description: 'Bras identique à l''origine : angle d''attaque, longueur et type d''attache (écrou, clip baïonnette) conformes
      aux plans constructeur.'
  - tier: Qualité équivalente OE
    description: Bras fabriqué par un équipementier spécialisé avec les mêmes côtes fonctionnelles. Souvent livré avec les
      fixations.
  - tier: Adaptable compatible
    description: Bras compatible avec plusieurs références proches. Vérifier la longueur totale, l'offset et le type d'attache
      avant commande.
  brands:
    premium:
    - Bosch
    - Valeo
    standard:
    - SWF
    - Hella
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Balai qui ne touche plus le pare-brise
    severity: confort
  - id: S2
    label: Traces ou zones non balayees
    severity: confort
  - id: S3
    label: Bras tordu ou rouille
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : balai qui ne touche plus le pare-brise'
  quick_checks:
  - 'Observer : balai qui ne touche plus le pare-brise ?'
  - 'Observer : traces ou zones non balayees ?'
  - 'Observer : bras tordu ou rouille ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Balai qui ne touche plus le pare-brise
  - Traces ou zones non balayees
  - Bras tordu ou rouille
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '301'
  intro_title: A quoi sert Bras d'essuie-glace ?
  risk_title: Pourquoi remplacer Bras d'essuie-glace a temps ?
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
  - question: Comment choisir Bras d'essuie-glace compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Bras d'essuie-glace ?
    answer: En cas de balai qui ne touche plus le pare-brise ou de degradation mesurable, il faut controler rapidement avant
      panne secondaire.
  - question: Puis-je monter Bras d'essuie-glace sans verification atelier ?
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
doc_id: d6a4c79f-9803-55db-890f-10dd6dded3e9
content_hash: sha256:d6184bcc3663f27d
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
  _source: denso-am.eu + fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 2
  _has_tech_data: true
  types_variants:
  - type: 'électrique'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le bras d'essuie-glace est la tige métallique articulée qui relie le
    mécanisme d'entraînement (moteur d'essuie-glace) au balai essuyant la
    surface du pare-brise. Sa mission est de supporter, maintenir et plaquer le
    balai contre le verre avec une pression constante sur toute la largeur du
    balayage, quelle que soit la vitesse du véhicule ou l'angle de la vitre.Fixé
    sur l'axe de pivot par un écrou et un cône d'entraînement, le bras transmet
    le mouvement oscillant du mécanisme tout en conservant la pression mécanique
    exercée par un ressort interne intégré. Cette pression, typiquement comprise
    entre 1 et 3 N selon les constructeurs, garantit un contact permanent entre
    le caoutchouc du balai et le verre. Sans cette force d'appui constante, le
    balai rebondit à haute vitesse ou décolle dans les virages à grande vitesse,
    laissant des zones non essuyées.Le bras d'essuie-glace travaille dans des
    conditions sévères : exposition aux UV, aux variations de température (de
    -30 °C à +80 °C sous le capot moteur en zone de fixation), aux projections
    de gravillons et au sel de dégivrage. Au fil des cycles d'utilisation, le
    ressort interne fatigue, l'articulation de tête s'use et la surface du bras
    peut se corroder, réduisant progressivement la qualité d'essuyage.Les pièces
    directement associées à vérifier lors d'un remplacement sont le moteur
    d'essuie-glace, la commande d'essuie-glace et la pompe de nettoyage des
    vitres.
  S2: >-
    Un bras d'essuie-glace défaillant se manifeste par des signes visuels et
    fonctionnels facilement identifiables. Ne pas les ignorer : une mauvaise
    visibilité par temps de pluie présente un risque direct pour la sécurité de
    conduite.- Balai qui ne touche plus le pare-brise : le bras a perdu sa
    tension de ressort ou est déformé. Le balai claque, rebondit et ne nettoie
    plus la surface correctement. Se remarque à vitesse élevée ou par grand
    vent.- Traces ou zones non balayées : des bandes horizontales de pluie
    persistent sur le pare-brise après chaque passage du balai. Indique une
    pression insuffisante due à un ressort interne affaibli.- Bras tordu ou
    rouillé : visible à l'oeil nu. La déformation peut résulter d'un choc
    (branche, congère grattée), la corrosion avancée fragilise la structure et
    peut provoquer une rupture soudaine.- Bruit de claquement ou de frottement :
    si le bras oscille librement sur son axe ou si la tête de fixation du balai
    est desserrée, un claquement rythmique apparaît à chaque mouvement.- Bras
    désolidarisé après gel : une tentative de dégivrage par la force (tirer sur
    le balai gelé au pare-brise) peut arracher la tête de fixation ou déformer
    le bras.- Angle de balayage réduit ou asymétrique : le bras ne revient plus
    à sa position de repos ou ne suit plus la courbe prévue par le constructeur,
    laissant des zones vives non protégées.
  S3: >-
    Le bras d'essuie-glace est une pièce spécifique au véhicule : la longueur,
    l'angle de courbure, la fixation sur l'axe et le type de tête (crochet,
    baïonnette, côté latéral) varient selon chaque modèle. Un bras non adapté
    peut toucher le montant du pare-brise, endommager la carrosserie ou ne pas
    s'accoupler correctement au balai.- Renseigner la marque, le modèle et
    l'année du véhicule : c'est le prérequis absolu. Un même modèle peut
    recevoir deux types de bras différents selon l'année de fabrication (face-
    lift, changement de génération).- Identifier le côté (conducteur / passager)
    : les deux bras d'un véhicule sont souvent de longueurs et de géométries
    différentes. Commander le bon côté est impératif.- Vérifier le type de
    fixation sur l'axe : les fixations standard sont de type pince conique (le
    plus répandu), pivot fileté ou boulon latéral. Mesurer le diamètre et la
    longueur du pivot si le bras d'origine n'est plus disponible.- Contrôler le
    type de tête de balai : crochet standard, connecteur latéral, baïonnette ou
    pinch-tab. Le nouveau bras doit être compatible avec le balai en place ou
    être commandé avec un balai assorti.- Privilégier une référence OEM ou
    équivalent qualité : les fabricants de premier montage (Bosch, Valeo, SWF,
    Trico) garantissent les dimensions et la pression de ressort conformes aux
    spécifications constructeur.- Inspecter l'axe de pivot avant montage : si
    l'axe est corrodé ou strié, le bras neuf ne tiendra pas. Un nettoyage à la
    brosse métallique et une légère lubrification au cuivre-métal est
    nécessaire.Pour aller plus loin : consultez notre guide d'achat bras
    d'essuie-glace — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    Le remplacement d'un bras d'essuie-glace est une intervention accessible
    sans outillage spécialisé, mais qui demande des précautions pour éviter
    d'endommager le pare-brise ou le mécanisme de pivotement.- Positionner les
    bras à mi-course : démarrer le véhicule, activer les essuie-glaces, puis les
    arrêter en position haute (mi-course). Couper le contact. Cela facilite la
    manipulation et évite que le bras ne revienne en percussion sur le capot
    moteur.- Soulever et bloquer le bras : soulever le bras perpendiculairement
    au pare-brise. Intercaler un chiffon épais ou un carton plié entre le bras
    soulevé et la vitre pour éviter que le bras nu (sans balai) ne vienne
    percuter et fissurer le pare-brise si vous le lâchez par inadvertance.-
    Déposer le balai : actionner le mécanisme de libération de la tête (pression
    sur le clip ou rotation selon le type) et retirer le balai. Le conserver si
    vous réutilisez le balai avec le nouveau bras.- Retirer le cache de la
    fixation : soulever le petit cache plastique situé à la base du bras pour
    accéder à l'écrou ou à la vis de fixation sur l'axe de pivot.- Dévisser et
    extraire le bras : desserrer l'écrou central (en général 13 mm hexagonal).
    Le bras est monté à friction conique : utiliser un extracteur de bras ou
    exercer des pressions alternées latérales pour le désolidariser sans abîmer
    l'axe.- Nettoyer l'axe de pivot : éliminer la corrosion à la brosse
    métallique, dépoussiérer, appliquer une légère couche de graisse cuivre sur
    les cannelures.- Monter le nouveau bras : positionner le bras dans l'angle
    de repos exact (repère gravé ou marquage de la peinture d'origine). Engager
    sur l'axe, serrer l'écrou au couple préconisé (généralement 8 à 12 Nm).
    Remonter le cache et fixer le balai.- Tester le balayage : activer les
    essuie-glaces et vérifier la course complète, la position de repos et
    l'absence de bruit anormal.
  S4_REPOSE: >-
    La repose du bras d'essuie-glace conditionne directement la qualité du
    balayage et la durée de vie du balai. Un angle de repos incorrect ou un
    serrage insuffisant sur l'axe cannelé provoquent un bruit de choc lors de
    l'arrêt et une usure prématurée du mécanisme.- Nettoyer l'axe de pivot :
    éliminer les résidus de corrosion à l'aide d'une brosse métallique fine.
    Souffler les cannelures pour les débarrasser de toute poussière. Appliquer
    une fine couche de graisse cuivre sur les cannelures uniquement — ne pas en
    mettre sur la portée conique pour ne pas réduire le frottement de maintien.-
    Positionner le nouveau bras à l'angle de repos exact : aligner le bras selon
    le repère d'origine (trait de marqueur ou repère gravé laissé lors de la
    dépose, ou position de repos constructeur inscrite dans le manuel). Sur les
    essuie-glaces avant, l'angle de repos doit ramener le bras sous le bord
    inférieur du capot ou dans la gorge de la carrosserie, selon la géométrie du
    véhicule.- Engager le bras sur l'axe cannelé sans frapper : glisser le bras
    à la main sur l'axe en respectant l'orientation de la cannelure (détrompeur
    ou méplat). Ne jamais frapper au marteau sur la tête du bras — les chocs
    transmis à l'arbre du moteur peuvent endommager les engrenages ou le joint
    d'étanchéité.- Serrer l'écrou de fixation au couple constructeur : visser
    l'écrou central (en général 8 à 12 Nm pour un bras d'essuie-glace avant).
    Utiliser une clé dynamométrique — un serrage excessif écrase les cannelures
    et un serrage insuffisant laisse le bras patiner sur l'axe lors des
    à-coups.- Remonter le cache de protection : clipser le cache plastique sur
    la base du bras pour protéger l'écrou de l'humidité et des projections.
    S'assurer qu'il est correctement enclipé sur tous ses points de fixation.-
    Installer ou réinstaller le balai : engager le balai dans la tête du bras
    jusqu'au clic de verrouillage. Tirer légèrement sur le balai pour confirmer
    la fixation.- Tester le balayage complet : activer les essuie-glaces en mode
    intermittent, puis à vitesse 1 et vitesse 2. Vérifier que le bras balaie
    toute la surface prévue, que le balai revient en position de repos sans choc
    contre le capot ou la carrosserie, et qu'aucun bruit de frottement anormal
    n'est présent.- Vérifier la pression du balai sur le verre : soulever le
    bras relevé avec deux doigts et le laisser revenir lentement. Il doit
    s'appliquer progressivement sur le verre sans rebond. Une pression
    insuffisante signale un ressort de bras fatigué à remplacer.
  S5: >-
    Plusieurs erreurs fréquentes surviennent lors du remplacement d'un bras
    d'essuie-glace. Les connaître à l'avance évite les casses coûteuses et les
    retours atelier.- Laisser retomber le bras nu sur le pare-brise : sans le
    balai, la tige métallique percute directement la vitre et peut la fissurer.
    Toujours intercaler un chiffon ou maintenir fermement le bras. Conséquence :
    remplacement du pare-brise.- Forcer l'extraction sans extracteur dédié :
    tirer brutalement sur le bras sans outil approprié déforme l'axe de pivot ou
    arrache les cannelures. Conséquence : axe inutilisable, remplacement du
    mécanisme complet.- Monter sans respecter l'angle de repos : positionner le
    bras trop haut ou trop bas décale la zone de balayage. En position trop
    haute, le bras peut percuter le montant du pare-brise et se déformer.
    Conséquence : zone non couverte, bras re-déformé.- Négliger le nettoyage de
    l'axe : monter le nouveau bras sur un axe corrodé empêche le serrage correct
    et le bras peut se desserrer en roulage. Conséquence : bras projeté sur la
    chaussée ou sur la voiture.- Commander la mauvaise longueur ou le mauvais
    côté : un bras trop long frôle le montant du pare-brise, un bras trop court
    laisse une zone morte centrale. Toujours vérifier côté et longueur avant de
    déposer l'ancien bras. Conséquence : mauvais essuyage, retour pièce.
  S6: >-
    Une fois le nouveau bras monté, effectuer ces contrôles avant de reprendre
    la route pour s'assurer que le montage est correct et que la visibilité est
    restaurée.- Position de repos conforme : vérifier que le bras revient
    exactement à la position basse marquée par le constructeur (repère sur la
    carrosserie ou le cache de pivot). Un décalage de plus de 1 cm signale un
    angle de montage incorrect.- Course complète sans accrochage : activer les
    essuie-glaces à vitesse rapide (mode 2 ou position de pluie battante) et
    observer que le bras effectue sa course complète des deux côtés sans toucher
    le montant du pare-brise ni le joint de carrosserie.- Absence de bruit de
    claquement : un claquement en fin de course indique soit un couple de
    serrage insuffisant sur l'axe, soit une tête de balai mal clipsée. Arrêter
    immédiatement et vérifier.- Pression du balai homogène : lors d'un arrosage
    simulé (gicleurs), vérifier visuellement que la bande essuyée est uniforme
    sur toute la largeur du pare-brise, sans laisser de bandes verticales non
    essuyées au centre ou aux extrémités.- Serrage de l'écrou : re-contrôler le
    couple de l'écrou de pivot après un premier cycle de fonctionnement à froid,
    car la fixation conique peut légèrement se tasquer.
  S7: >-
    Le bras d'essuie-glace est la tige métallique qui relie le mécanisme
    d'entraînement au balai. Lorsqu'il est tordu, corrodé ou que sa tension de
    rappel est insuffisante, les balais neufs n'effacent pas correctement même
    en parfait état. En cas de remplacement du bras, ou si l'essuyage reste
    insatisfaisant après changement des balais, les pièces suivantes doivent
    être vérifiées. - Balais d'essuie-glace (lames caoutchouc) : Le bras
    supporte et plaque le balai contre le pare-brise. Si le bras est déformé ou
    si sa fixation sur l'axe a joué, les balais sautillent ou laissent des zones
    non essuyées même en étant neufs. Remplacer les balais en même temps que le
    bras pour garantir un résultat immédiat et éviter un second démontage à
    court terme. - Moteur d'essuie-glace : Le moteur électrique entraîne le bras
    via un mécanisme de tringlerie. Si le bras d'essuie-glace présente une
    résistance anormale au mouvement (corrosion de l'axe, point dur mécanique),
    le moteur peut être mis en surcharge et finir par rendre l'âme. À l'inverse,
    si le bras ne suit plus la course complète du mécanisme, vérifier que le
    pignon de sortie moteur n'est pas usé ou que l'écrou de fixation du bras sur
    l'axe n'est pas desserré. - Mécanisme de tringlerie d'essuie-glace : La
    tringlerie relie le moteur aux deux bras via des biellettes et des rotules.
    Des rotules usées ou une biellette déformée provoquent un décalage de course
    ou un bras qui ne revient pas en position de repos. Si un bras a un
    comportement erratique indépendamment de l'autre, inspecter la tringlerie. -
    Commande d'essuie-glace (commodo) : Si les essuie-glaces ne fonctionnent
    plus sur certaines vitesses ou ne s'arrêtent pas en position de repos, le
    problème vient de la commande au volant (commodo de colonne de direction),
    pas des bras. Ce cas de figure se rencontre souvent lorsque les symptômes
    sont électriques (intermittent, vitesse unique) plutôt que mécaniques
    (frottement, sautillement). - Pompe de lave-glace et buses de projection :
    Lors d'une intervention sur les bras d'essuie-glace, c'est le bon moment
    pour contrôler les buses de lave-glace (orientées vers le pare-brise). Les
    buses bouchées par le calcaire réduisent l'efficacité de nettoyage et
    forcent les balais à travailler à sec — ce qui accélère l'usure du
    caoutchouc.
  S8: >-
    Peut-on changer uniquement le balai sans remplacer le bras ?Oui, dans la
    majorité des cas. Si le bras n'est pas tordu, corrodé ou si son ressort est
    toujours fonctionnel (pression correcte), seul le balai doit être remplacé.
    Inspecter le bras à chaque remplacement de balai pour détecter un début de
    corrosion ou une perte de tension. Un bras détérioré finit par abîmer le
    balai neuf prématurément.Comment choisir le bras d'essuie-glace compatible
    avec mon véhicule ?Renseigner la marque, le modèle, le type de carrosserie
    et l'année de fabrication. Un même modèle peut évoluer en cours de
    production et recevoir des bras de géométrie différente. Vérifier également
    le côté (conducteur ou passager), la longueur en millimètres et le type de
    tête de fixation du balai (crochet standard, connecteur latéral ou
    baïonnette). Le numéro de référence OEM gravé sur le bras d'origine est la
    méthode la plus fiable.Quand remplacer le bras d'essuie-glace ?Le
    remplacement s'impose dès qu'un bras est visible tordu ou rouillé, dès que
    le balai ne plaque plus correctement le pare-brise malgré un balai neuf, ou
    après un choc (congère, branche). De façon préventive, inspecter les bras
    tous les 2 ans ou à chaque contrôle technique. Un bras avec ressort affaibli
    ne se répare pas : le remplacer complet.Peut-on monter le bras d'essuie-
    glace soi-même ?Oui, l'intervention est accessible à tout bricoleur
    automobile. Elle ne nécessite qu'une clé à oeil de 13 mm et, idéalement, un
    extracteur de bras pour désolidariser la fixation conique sans abîmer l'axe.
    La précaution principale est de protéger le pare-brise pendant la dépose
    pour éviter qu'un bras nu ne le percute.Quel est le risque de rouler avec un
    bras d'essuie-glace défaillant ?Un bras qui ne plaque plus le balai
    correctement réduit drastiquement la visibilité par temps de pluie. À 100
    km/h, le risque d'accident sans visibilité suffisante est direct. De plus,
    un bras corrodé peut se rompre subitement et projecter le balai sur la
    chaussée ou sur le véhicule suivant. Ne pas différer le remplacement.
  META: >-
    {"meta_title":"Bras d'essuie-glace : balai décollé ou tordu ? |
    AutoMecanik","meta_description":"Balai qui ne touche plus le pare-brise ou
    zones non balayées ? Ce guide détaille quand changer le bras d'essuie-glace
    et comment sélectionner le bon modèle pour votre véhicule.","meta_title_leng
    th":55,"meta_description_length":158,"primary_intent":"diagnostic","target_s
    ymptoms":["balai qui ne touche plus le pare-brise","traces ou zones non
    balayees","bras tordu ou rouille"],"category":"accessoires"}
---

# Bras d'essuie-glace - Guide Diagnostic Complet

## Fonction et Rôle

Supporte et maintient le balai contre le pare-brise

**Actions principales:** supporter, maintenir, plaquer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- balai qui ne touche plus le pare-brise
- traces ou zones non balayees
- bras tordu ou rouille

## Procédure de Diagnostic

Pour diagnostiquer un problème de bras d'essuie-glace:

1. **Inspection visuelle** - Examiner l'état du bras d'essuie-glace
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

- commande-d-essuie-glace
- moteur-d-essuie-glace
- pompe-nettoyage-des-vitres

## Critères de Compatibilité

Pour commander le bon bras d'essuie-glace, vous devez connaître:

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

**Comment choisir Bras d'essuie-glace compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Bras d'essuie-glace ?**
En cas de balai qui ne touche plus le pare-brise ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Bras d'essuie-glace sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
