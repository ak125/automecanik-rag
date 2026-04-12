---
category: support_moteur
slug: support-de-boite-vitesse
title: Support de boîte vitesse
pg_id: 249
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
  last_enriched_by: script:rag-enrich-from-web-corpus
  last_enriched_at: '2026-04-03'
  v5_migrated_at: '2026-03-29'
domain:
  role: Supporter et fixer la boite de vitesses au chassis
  must_be_true:
  - supporter
  - fixer
  - amortir
  must_not_contain:
  - injection
  - freinage
  - climatisation
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - amortisseur
  - ressort-de-suspension
  - bras-de-suspension
  - rotule-de-suspension
  - barre-stabilisatrice
  - biellette-de-barre-stabilisatrice
  confusion_with:
  - term: piece-de-suspension-voisine
    difference: Les pieces de suspension travaillent ensemble mais ont des references distinctes. Verifier la position (avant/arriere,
      gauche/droite).
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
  - ❌ "zero vibration"
  cost_range:
    min: 30
    max: 120
    currency: EUR
    unit: pièce
    source: catalogue automecanik
  brands:
    premium:
    - Hutchinson
    - Vibracoustic (Continental)
    - Anvis
    standard:
    - Lemforder (ZF)
    - Corteco
    - Swag
    budget:
    - Febi Bilstein
    - Meyle
    - Sasic
  quality_tiers:
  - tier: Origine constructeur
    description: Supports de boite de vitesses identiques a la premiere monte, avec elastomere calibre pour la frequence de
      vibration du groupe motopropulseur.
  - tier: Equipementier qualite OE
    description: Supports fabriques par des equipementiers premiere monte avec elastomere de qualite equivalente et durete
      Shore conforme.
  - tier: Adaptable qualite reconnue
    description: Supports compatibles avec verification de la durete de l elastomere et des dimensions de fixation avant montage.
diagnostic:
  symptoms:
  - id: S1
    label: Vibrations ressenties sur le levier de vitesses
    severity: confort
  - id: S2
    label: Caoutchouc du support visiblement deteriore
    severity: confort
  - id: S3
    label: Claquement ou bruit sourd au passage des rapports
    severity: confort
  - id: S4
    label: Boite de vitesses qui semble bouger anormalement
    severity: confort
  - id: S5
    label: Sensation d a-coups a l embrayage ou debrayage
    severity: confort
  - id: S6
    label: Plus de 100 000 km ou supports moteur a changer
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - verifier equilibrage et fixations
  - remplacement preventif recommande
  quick_checks:
  - Vibrations ressenties sur le levier de vitesses ?
  - 'Observer : caoutchouc du support visiblement deteriore ?'
  - 'Observer : claquement ou bruit sourd au passage des rapports ?'
  - 'Observer : boite de vitesses qui semble bouger anormalement ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Vibrations ressenties sur le levier de vitesses
  - Caoutchouc du support visiblement deteriore
  - Claquement ou bruit sourd au passage des rapports
  - Boite de vitesses qui semble bouger anormalement
  - Sensation d a-coups a l embrayage ou debrayage
  - Plus de 100 000 km ou supports moteur a changer
  good_practices:
  - Controle visuel des fuites et deformations a chaque revision
  - Remplacement par paire (meme essieu) pour equilibre du vehicule
  - Faire verifier la geometrie apres remplacement
  - Inspection des silent-blocs et des rotules associees
rendering:
  pgId: '249'
  intro_title: A quoi sert Support de boîte vitesse ?
  risk_title: Pourquoi remplacer Support de boîte vitesse a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
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
  - question: Support de boîte OE, OES ou adaptable ?
    answer: Les supports OES (Lemförder, Corteco) sont de qualité première monte. adaptables (Febi, Meyle) offrent un bon
      rapport qualité/prix. Vérifier la compatibilité boîte manuelle ou automatique.
  - question: Comment savoir si le support de boîte est HS ?
    answer: Vibrations en roulant, bruit de claquement au passage des vitesses, levier de vitesses qui vibre, à-coups à l'embrayage.
  - question: Tous les combien changer le support de boîte ?
    answer: Pas de périodicité fixe. Durée de vie 100 000 à 180 000 km. À remplacer en même temps que les supports moteur
      si usé.
  - question: Peut-on changer le support de boîte soi-même ?
    answer: Oui, souvent plus accessible que les supports moteur. Soutenir la boîte avec un cric. Prévoir 1h environ.
  - question: Quelle erreur éviter avec le support de boîte ?
    answer: Ne pas oublier de vérifier l'état de la biellette de réaction si présente. Serrer au couple recommandé.
  quality:
    score: 60
    source: script:rag-upgrade-v4
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
doc_id: 526fe560-efc4-5819-94a5-29e2b902265f
content_hash: sha256:a7b239b6157af006
lang: fr
variants:
- name: Version gaz
  aliases:
  - gaz
  - gas-a-just
  functional_differences:
  - Meilleure tenue de route
  - Plus ferme que l huile
- name: Version huile
  aliases:
  - huile
  - hydraulique
  functional_differences:
  - Confort de conduite superieur
  - Moins cher que le gaz
location_on_vehicle:
  area: Entre la roue et la carrosserie (avant et/ou arriere)
  access: Par le dessous (pont elevateur) ou demontage roue
  adjacent_parts:
  - amortisseur
  - ressort
  - bras
  - rotule
installation:
  difficulty: moyen a difficile
  time: 1h a 2h par cote
  tools:
  - compresseur de ressort
  - cle a douille
  - cle dynamometrique
  - arrache-rotule
  prerequisite: Pont elevateur recommande, vehicule decharge
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'hydraulique'
    source_ref: corpus RAG web OEM
  - type: 'plein'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_11_a: '11 a'
    val_12_a: '12 a'
    val_13_a: '13 a'
    val_15__: '15 %'
    val_2__: '2 %'
    val_2_a: '2 a'
    val_54__: '54 %'
    val_6_a: '6 a'
    val_8__: '8 %'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le support de boîte vitesse est une pièce de liaison mécanique chargée de fixer la boîte de vitesses au châssis ou
    au berceau du véhicule tout en amortissant les vibrations générées par la transmission. Il se compose généralement d''une
    armature métallique encapsulant un bloc en caoutchouc ou en élastomère vulcanisé, qui fait office d''absorbeur de vibrations.
    Son rôle est triple : supporter le poids de la boîte de vitesses et de la transmission dans le compartiment moteur, fixer
    ces organes de manière rigide au châssis pour éviter tout déplacement intempestif lors des changements de rapports ou
    des à-coups moteur, et amortir les vibrations et les chocs issus du mouvement de rotation de la transmission avant qu''ils
    ne se propagent dans l''habitacle. Le support de boîte travaille en permanence sous des contraintes mécaniques importantes
    : couple de réaction lors du passage des vitesses, vibrations à haute fréquence, contraintes thermiques dues à la proximité
    du moteur. L''élément caoutchouc se détériore progressivement sous l''effet de l''huile, de la chaleur et des cycles de
    compression/détente répétés. Il est souvent remplacé en même temps que les supports moteur lors d''une révision de la
    chaîne cinématique.'
  S2: 'Le vieillissement du support de boîte vitesse est progressif et les symptômes s''accentuent au fil des kilomètres.
    Après 100 000 km ou en cas de contamination par l''huile moteur, les signaux suivants doivent alerter : - Vibrations ressenties
    sur le levier de vitesses : le caoutchouc durci ou fissuré ne filtre plus les vibrations de la transmission. Ces vibrations
    se transmettent directement jusqu''au levier de vitesses, perceptibles en conduite à vitesse stabilisée. - Caoutchouc
    du support visiblement détérioré : à l''inspection visuelle sous le véhicule, le bloc caoutchouc présente des fissures,
    des déchirures ou un écrasement permanent. Signe d''usure avancée nécessitant un remplacement immédiat. - Claquement ou
    bruit sourd au passage des rapports : quand la boîte de vitesses se déplace légèrement à chaque changement de rapport
    faute de maintien rigide, un bruit de choc sourd se produit — symptôme de sévérité intermédiaire. - Boîte de vitesses
    qui semble bouger anormalement : observable en regardant sous le capot lors d''une accélération brusque. Le bloc boîte
    doit rester quasi immobile. Un mouvement perceptible indique un support défaillant. - Sensation d''à-coups à l''embrayage
    ou au débrayage : les mouvements parasites de la boîte perturbent l''engagement de l''embrayage et créent des à-coups
    lors des démarrages ou des manœuvres. - Plus de 100 000 km ou supports moteur déjà changés : le remplacement préventif
    du support de boîte lors d''une révision des supports moteur est conseillé pour éviter une récidive rapide.'
  S3: 'Le support de boîte vitesse est une pièce spécifique au couple véhicule/boîte de vitesses. La géométrie, la rigidité
    et les points de fixation varient selon que la boîte est manuelle, robotisée ou automatique. Voici les critères à valider
    avant commande : - Marque, modèle et année du véhicule : les références varient même sur un même modèle selon les millésimes
    de production. Toujours indiquer ces trois informations. - Type de boîte de vitesses : manuelle, automatique ou robotisée.
    Le point de fixation et la rigidité du support diffèrent selon le type de boîte, qui a une masse et un centre de gravité
    différents. - Motorisation et puissance : une version sportive ou à forte puissance peut nécessiter un support de boîte
    avec une rigidité accrue par rapport à la version de base. - Qualité OES ou OEM : les fabricants comme Lemförder, Corteco,
    Febi ou Meyle produisent des supports de boîte conformes aux spécifications constructeur. Vérifier systématiquement la
    compatibilité boîte manuelle ou automatique dans la description article. - Présence d''une biellette de réaction : sur
    certains véhicules, un support avant et une biellette de réaction travaillent en tandem. Si la biellette est usée, la
    remplacer simultanément au support. - État du support actuel avant commande : inspecter visuellement le caoutchouc et
    vérifier les fixations pour confirmer que le support est bien la pièce défaillante et non la biellette ou une vis de fixation
    desserrée. - Référence constructeur ou OEM à croiser : comparer la référence de la pièce proposée avec la référence constructeur
    du véhicule ou la référence de la pièce d''origine déposée. Pour aller plus loin : consultez notre guide d''achat support
    de boîte vitesse — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 'Le remplacement du support de boîte vitesse est une intervention généralement plus accessible que le remplacement
    des supports moteur, car la boîte de vitesses est souvent moins encombrée. Prévoir environ 1 heure de travail avec un
    équipement de levage adapté. Voici la procédure générale : - Lever le véhicule et le placer sur chandelles rigides aux
    points de levage constructeur. Ne jamais travailler sous un véhicule soutenu uniquement par un cric hydraulique. - Repérer
    le support de boîte sur le berceau ou le châssis. Il est situé sous la boîte de vitesses, souvent visible en regardant
    sous le véhicule depuis l''avant ou le côté. - Positionner un cric avec une planche de bois sous le carter de la boîte
    de vitesses pour soutenir son poids avant de démonter le support. Ne pas placer le cric sous un point de drainage ou une
    prise d''huile. - Dévisser les vis de fixation du support sur le berceau/châssis d''une part, et les vis de fixation sur
    la boîte de vitesses d''autre part. Utiliser les douilles adaptées et noter le couple de serrage constructeur. - Abaisser
    légèrement la boîte avec le cric pour dégager le support, puis extraire le support usé. - Inspecter les filetages du berceau
    et de la boîte — si les filetages sont endommagés, les retravailler avec un taraud avant montage. - Positionner le nouveau
    support en alignant les trous de fixation, puis serrer les vis au couple constructeur (généralement 40 à 80 Nm selon le
    véhicule). - Remonter le cric, repositionner la boîte à sa hauteur initiale et vérifier que toutes les fixations sont
    serrées uniformément. - Effectuer un test de roulage en réalisant des passages de vitesses et des accélérations pour confirmer
    la disparition des bruits et vibrations.'
  S4_REPOSE: 'La repose du support de boîte vitesse est l''étape décisive pour retrouver un fonctionnement silencieux et des
    passages de vitesses fluides. Une fixation insuffisante ou un support mal aligné transmettra des vibrations résiduelles
    malgré la pièce neuve. - Préparer le support neuf : comparer visuellement le support neuf avec l''ancien avant montage
    — vérifier que les points de fixation et la géométrie de l''inserts caoutchouc correspondent exactement. Un support légèrement
    différent peut provoquer des contraintes sur la boîte. - Positionner le support sous la boîte : avec le cric maintenant
    la boîte en position, glisser le support neuf sur les goujons ou les trous de fixation du berceau. Ne pas forcer si l''alignement
    n''est pas naturel. - Visser les fixations côté berceau/châssis en premier : engager toutes les vis à la main sans les
    serrer. Vérifier que toutes les vis sont bien engagées dans leurs filetages avant de commencer le serrage. - Descendre
    le cric progressivement pour que la boîte de vitesses repose naturellement sur le support. Le poids de la boîte aide à
    centrer le support sur ses points d''appui. - Serrer toutes les fixations au couple constructeur avec la clé dynamométrique
    (généralement 40 à 80 Nm selon le véhicule). Commencer par les vis côté boîte, puis les vis côté berceau. Ne jamais estimer
    le couple au ressenti sur des fixations antivibratoires. - Contrôler le jeu de la biellette de réaction si votre véhicule
    en est équipé : la biellette (aussi appelée bras de reprise de couple) limite les mouvements de la boîte sous accélération.
    Vérifier ses silentblocs et l''état de ses fixations. - Remonter les caches et protections déposés lors de l''accès et
    retirer les chandelles avec précaution. - Effectuer un test de roulage complet : réaliser des accélérations progressives,
    des passages de vitesses et des décélérations pour confirmer la disparition des claquements, vibrations sur le levier
    et à-coups à l''embrayage. Un léger bruit de rodage peut être présent pendant les 50 premiers kilomètres.'
  S5: 'Le remplacement du support de boîte vitesse concentre quelques erreurs récurrentes qui peuvent compromettre la durabilité
    de l''intervention ou endommager des composants adjacents. Voici les principales à éviter : - Oublier de soutenir la boîte
    avant démontage : retirer les vis de fixation sans soutenir le poids de la boîte provoque une chute brusque qui peut endommager
    les durites, le câblage ou la pédale d''embrayage. Conséquence : dégâts collatéraux sur d''autres composants. - Ne pas
    serrer au couple constructeur : un serrage insuffisant laisse le support se désolidariser progressivement, recréant les
    vibrations et risquant un arrachement. Un surserrage détériore les filetages ou crée des contraintes excessives dans le
    caoutchouc. Conséquence : retour en atelier dans les 10 000 km. - Ignorer l''état de la biellette de réaction : sur les
    véhicules équipés d''une biellette de réaction avant, négliger son remplacement simultané conduit à une récidive des à-coups
    malgré un support neuf. Conséquence : deuxième intervention rapide à prévoir. - Choisir un support sans vérifier le type
    de boîte : un support prévu pour une boîte manuelle n''a pas la rigidité ni la géométrie d''un support pour boîte automatique.
    Conséquence : mauvaise tenue de la boîte et transmission de vibrations différentes. - Travailler sans levage sécurisé
    : utiliser un cric seul sans chandelles rigides pour travailler sous le véhicule est dangereux. Conséquence : risque d''accident
    grave en cas de chute du véhicule.'
  S6: 'Après montage du nouveau support de boîte vitesse, les contrôles suivants permettent de valider la qualité de l''intervention
    avant de rendre le véhicule à la route : - Contrôle du serrage de toutes les vis : passer systématiquement sur chaque
    point de fixation avec une clé dynamométrique pour confirmer que les couples constructeur sont atteints et uniformes.
    - Inspection visuelle du positionnement : le support doit être parfaitement centré et le bloc caoutchouc ne doit présenter
    aucune contrainte angulaire — un appui oblique réduirait prématurément la durée de vie du caoutchouc. - Test moteur à
    l''arrêt : démarrer le moteur et observer la boîte de vitesses depuis le dessous du véhicule (avec le véhicule en sécurité
    sur chandelles) — aucun mouvement anormal ne doit être visible. - Test de passage des vitesses : passer tous les rapports
    successivement à l''arrêt, puis vérifier l''absence de bruit sourd ou de claquement lors du passage en marche arrière.
    - Test routier avec accélérations et décélérations : confirmer la disparition des vibrations sur le levier de vitesses
    et des à-coups à l''embrayage sur un trajet de 5 à 10 km.'
  S7: 'Quel est le prix d''un support de boîte vitesse ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur
    pour trouver le support de boîte vitesse compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon support de boîte vitesse est à changer ?Les signes d''usure les plus courants sont détaillés dans la section
    diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un support de
    boîte vitesse défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule.
    Consultez la section symptômes pour évaluer l''urgence du remplacement.Le support de boîte vitesse travaille en synergie
    avec les autres silentblocs et supports du groupe motopropulseur. Un remplacement isolé peut s''avérer insuffisant si
    les pièces adjacentes sont également usées. - Support moteur — Les supports moteur et le support de boîte s''usent souvent
    simultanément, car ils partagent les mêmes sollicitations vibratoires. Si le support de boîte est à changer, inspecter
    systématiquement les supports moteur : si leur caoutchouc est fendu ou déformé, les remplacer en même temps pour éviter
    une double intervention. - Boîte de vitesses — Si le support de boîte était très dégradé depuis longtemps, vérifier l''état
    des joints de boîte et du carter : un support HS peut provoquer des micro-déplacements qui accélèrent l''usure des joints
    latéraux.'
  S8: 'Quelle est la durée de vie d''un support de boîte vitesse ? Il n''existe pas de périodicité de remplacement fixe définie
    par les constructeurs. En pratique, la durée de vie se situe entre 100 000 et 180 000 km selon la qualité de la pièce
    d''origine, le type de boîte (automatique plus lourde = contraintes plus élevées) et les conditions d''utilisation (conduite
    sportive ou urbaine intensive accélère l''usure). Un support contaminé par de l''huile moteur peut se dégrader beaucoup
    plus rapidement. Comment distinguer un support de boîte HS d''un support moteur défaillant ? Les symptômes sont similaires.
    La localisation du bruit est le premier indicateur : un bruit qui varie uniquement lors du passage des vitesses pointe
    vers le support de boîte, tandis qu''un bruit présent à toutes les sollicitations moteur suggère un support moteur. L''inspection
    visuelle sous le véhicule, moteur tournant, reste le moyen le plus fiable : faire tractionner légèrement le véhicule (roues
    calées, embrayage relâché progressivement) et observer quel support se déforme. Peut-on changer le support de boîte soi-même
    ? Oui, à condition de disposer d''un pont de levage ou d''un jeu de chandelles rigides et d''un cric hydraulique de plancher.
    L''opération reste accessible à un mécanicien amateur expérimenté car la boîte de vitesses est souvent moins encombrée
    que le moteur. Compter environ 1 heure sur une voiture de milieu de gamme. Le point critique est de soutenir la boîte
    correctement avant de démonter les vis. Faut-il remplacer le support de boîte et le support moteur ensemble ? C''est fortement
    conseillé si les deux ont le même kilométrage et des symptômes similaires. L''élastomère vieillit de la même façon sur
    les deux supports. Remplacer uniquement le support le plus dégradé sans traiter l''autre conduit souvent à revenir en
    atelier 20 000 à 30 000 km plus tard pour le second. Le surcoût est marginal par rapport à la main-d''œuvre double.'
  META: '{"meta_title":"Support de boîte vitesse : vibrations, causes | AutoMecanik","meta_description":"Vibrations sur le
    levier, claquement au passage des rapports ou boîte qui bouge ? Le support de boîte est peut-être HS. Guide diagnostic
    et compatibilité.","og_title":"Support de boîte vitesse : diagnostic vibrations","og_description":"Caoutchouc détérioré,
    à-coups à l''embrayage ou claquement sourd : les signes d''un support de boîte de vitesses usé. Durée de vie, remplacement
    et pièces liées.","canonical_intent ":"diagnostic","schema_type":"HowTo","sources":[{"type":"rag","ref":"gammes/ support-de-boite-vitesse.md","field":"domain.role
    + diagnostic.symptoms + rendering.faq"}]}'
---

# Support de boîte vitesse - Guide Diagnostic Complet

## Fonction et Rôle

Supporter et fixer la boite de vitesses au chassis

**Actions principales:** supporter, fixer, amortir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement ou bruit sourd au passage des rapports**
  claquement ou bruit sourd au passage des rapports

### 🟢 Autres Symptômes

- vibrations ressenties sur le levier de vitesses
- caoutchouc du support visiblement deteriore
- boite de vitesses qui semble bouger anormalement
- sensation d a-coups a l embrayage ou debrayage
- plus de 100 000 km ou supports moteur a changer

## Procédure de Diagnostic

Pour diagnostiquer un problème de support de boîte vitesse:

1. **Inspection visuelle** - Examiner l'état du support de boîte vitesse
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- support-moteur
- boite-de-vitesses

## Critères de Compatibilité

Pour commander le bon support de boîte vitesse, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "zero vibration"

## FAQ

**Support de boîte OE, OES ou adaptable ?**
Les supports OES (Lemförder, Corteco) sont de qualité première monte. adaptables (Febi, Meyle) offrent un bon rapport qualité/prix. Vérifier la compatibilité boîte manuelle ou automatique.

**Comment savoir si le support de boîte est HS ?**
Vibrations en roulant, bruit de claquement au passage des vitesses, levier de vitesses qui vibre, à-coups à l'embrayage.

**Tous les combien changer le support de boîte ?**
Pas de périodicité fixe. Durée de vie 100 000 à 180 000 km. À remplacer en même temps que les supports moteur si usé.

**Peut-on changer le support de boîte soi-même ?**
Oui, souvent plus accessible que les supports moteur. Soutenir la boîte avec un cric. Prévoir 1h environ.

**Quelle erreur éviter avec le support de boîte ?**
Ne pas oublier de vérifier l'état de la biellette de réaction si présente. Serrer au couple recommandé.
## Boîte manuelle

### Craquement au passage de vitesse
- **Synchroniseurs usés** : Craquement surtout sur un rapport précis (souvent 2ème ou 3ème). Pire à froid, s'améliore à chaud.
- **Huile de boîte inadaptée ou usée** : Vidange de boîte à effectuer (75W-80 ou 75W-90 selon constructeur).
- **Câble ou timonerie de commande usé** : Passage imprécis, sensation de flou dans le levier.

### Vitesse qui saute
- **Fourchette de sélection usée** : La vitesse se désengage spontanément sous charge.
- **Ressort de verrouillage cassé** : Le rapport ne tient plus en position.

### Bruit de roulement en boîte
- **Roulement d'arbre primaire usé** : Sifflement continu qui disparaît quand on appuie sur l'embrayage.
- **Roulement de sortie** : Bruit proportionnel à la vitesse du véhicule.

## Boîte automatique

### À-coups ou patinage
- **Niveau d'huile ATF incorrect** : Vérifier le niveau à chaud, moteur tournant au point mort.
- **Huile ATF usée** : Couleur marron foncé au lieu de rouge. Vidange recommandée.
- **Convertisseur de couple usé** : Patinage au démarrage, surchauffe de l'huile.

### Passage de rapports brutal
- **Calculateur de boîte** : Réinitialisation des adaptations parfois nécessaire.
- **Électrovannes de commande** : Corps de vannes encrassé ou électrovanne bloquée.

## Cardans et transmission

### Claquement en virage
- **Soufflet de cardan déchiré** : Graisse projetée visible sur la roue intérieure. Le cardan tourne sans lubrification.
- **Croisillon de cardan usé** : Claquement sec en accélération ou décélération dans les virages.

### Vibration à l'accélération
- **Cardan voilé** : Vibration proportionnelle à la vitesse.
- **Silent-bloc de transmission usé** : Vibrations transmises dans l'habitacle.

## Quand consulter un professionnel

- Boîte automatique en mode dégradé (bloquée sur un rapport)
- Fuite d'huile de boîte importante
- Craquement systématique sur tous les rapports
- Cardan cassé (roue qui ne tourne plus)
