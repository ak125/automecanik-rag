---
category: embrayage
slug: cable-d-embrayage
title: Câble d'embrayage
pg_id: 478
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
  role: Transmettre l'effort mécanique de la pédale vers la fourchette
  must_be_true:
  - transmettre l'effort
  - tirer
  - pousser
  must_not_contain:
  - disque
  - volant
  - couple
  - hydraulique
  - liquide
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - kit-d-embrayage
  - butee-d-embrayage
  - volant-moteur
  - emetteur-d-embrayage
  - recepteur-d-embrayage
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
  - ❌ "effort parfait"
  cost_range:
    min: 8
    max: 102
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
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
    label: Pedale d embrayage dure ou difficile a enfoncer
    severity: confort
  - id: S2
    label: Point de patinage tres haut ou tres bas
    severity: confort
  - id: S3
    label: Craquement ou grincement en appuyant sur la pedale
    severity: confort
  - id: S4
    label: Cable visible effiloche ou rouille
    severity: confort
  - id: S5
    label: Embrayage qui ne debraye pas completement
    severity: confort
  - id: S6
    label: Pedale qui reste enfoncee cable casse
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : pedale d embrayage dure ou difficile a enfoncer'
  quick_checks:
  - 'Observer : pedale d embrayage dure ou difficile a enfoncer ?'
  - 'Observer : point de patinage tres haut ou tres bas ?'
  - 'Observer : craquement ou grincement en appuyant sur la pedale ?'
  - 'Observer : cable visible effiloche ou rouille ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Pedale d embrayage dure ou difficile a enfoncer
  - Point de patinage tres haut ou tres bas
  - Craquement ou grincement en appuyant sur la pedale
  - Cable visible effiloche ou rouille
  - Embrayage qui ne debraye pas completement
  - Pedale qui reste enfoncee cable casse
  good_practices:
  - Eviter de laisser le pied sur la pedale d embrayage au point mort
  - Remplacement du kit complet (disque + mecanisme + butee)
  - Purge du circuit hydraulique si recepteur/emetteur concerne
  - Verifier le volant moteur lors du remplacement d embrayage
rendering:
  pgId: '478'
  intro_title: A quoi sert Câble d'embrayage ?
  risk_title: Pourquoi remplacer Câble d'embrayage a temps ?
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
  - question: Câble d'embrayage OE ou adaptable ?
    answer: Les câbles OES (Cofle, TRW) sont fiables. Vérifiez la longueur exacte et le type d'embouts (rotule, chape). Un
      câble mal adapté cassera rapidement.
  - question: Comment savoir si mon câble d'embrayage est usé ?
    answer: Pédale dure ou point de patinage très haut, craquement en appuyant sur la pédale, câble effiloché visible, embrayage
      qui accroche.
  - question: Tous les combien régler le câble d'embrayage ?
    answer: Contrôle du jeu tous les 30 000 km. Le câble s'étire naturellement. Quand le réglage est en butée, il faut le
      remplacer.
  - question: Peut-on changer le câble d'embrayage soi-même ?
    answer: Oui, opération accessible. Déconnecter côté pédale et côté fourchette, passer le nouveau câble, régler le jeu.
      Compter 30 min à 1h.
  - question: Quelle erreur éviter avec le câble d'embrayage ?
    answer: Ne pas forcer si le câble est coincé. Graisser les gaines. Vérifier l'état de la fourchette et de la rotule. Bien
      régler le jeu après montage.
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
doc_id: a73c7466-9e71-5920-a608-84e4abd8725f
content_hash: sha256:e02812f21d71c997
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
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'composite'
    source_ref: corpus RAG web OEM
  - type: 'céramique'
    source_ref: corpus RAG web OEM
  - type: 'hydraulique'
    source_ref: corpus RAG web OEM
  - type: 'pneumatique'
    source_ref: corpus RAG web OEM
  - type: 'rainuré'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_20_a: '20 a'
    val_5_a: '5 a'
  materials:
  - materiau: 'céramique'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le câble d''embrayage relie la pédale d''embrayage à la fourchette. Il est composé d''un câble métallique àl''intérieur
    d''une gaine. Lorsqu''on appui sur lapédale d''embrayage le câble qui est fixé à la fourchette actionne (appuie outire)
    la butée d''embrayage qui va à son tour permettre le passage du rapport devitesses en appuyant sur le diaphragme du mécanisme
    d''embrayage pour le séparerdu disque d''embrayage . Il y a deux types de câbles d''embrayage : - Câble d''embrayage à
    réglage automatique. - Câble d''embrayage à réglage manuel. En savoir plus : câble d''embrayage — définition et rôle mécanique
    🚨 Bruit Câble d''embrayage : causes et diagnostic'
  S2: 'Un câble d''embrayage usé présente plusieurs symptômes : - Passage de vitesses difficile. - Pédale d''embrayage dur
    à cause du grippage du câble. Un câble d''embrayage défaillant et qu''il n''est remplacé à temps peutentraîner plusieurs
    pannes : - Usure de la butée d''embrayage et de la fourchetted''embrayage. - Usure du kit d''embrayage . Diagnostic complet
    : identifier une panne de câble d''embrayage Symptômes détaillés et vérifications Un câble d''embrayage cassé ou en fin
    de vie envoie des signaux de plus en plus nets avant de lâcher complètement. Voici les symptômes caractéristiques à ne
    pas négliger : - Pédale d''embrayage dure ou difficile à enfoncer : signe typique d''un câble qui se grippe dans sa gaine,
    souvent dû à la corrosion ou à l''usure des fils internes. - Point de patinage très haut ou très bas : un câble détendu
    ou partiellement cassé modifie le point d''engagement, rendant les départs hésitants. - Craquement ou grincement à la
    pédale : peut indiquer un câble effiloché en frottement dans la gaine, ou une gaine elle-même détériorée. - Câble visible
    effiloché ou rouillé : une inspection sous capot ou sous véhicule permet parfois de constater directement l''usure des
    fils. - Embrayage qui ne débraye pas complètement : le câble ne tire plus suffisamment la fourchette, entraînant des difficultés
    à passer les vitesses. - Pédale qui reste enfoncée au plancher : signe d''une rupture franche du câble — le véhicule est
    immobilisé. Hypothèses à explorer Ces symptômes peuvent indiquer : un câble effiloché progressivement, une gaine fendue
    laissant entrer l''humidité, un réglage de tension inadapté, ou une rupture complète. Un câble usé peut également accélérer
    l''usure de la butée d''embrayage et de la fourchette. Vérifications non-invasives (à faire soi-même) - Évaluer la résistance
    à la pédale : une résistance irrégulière ou une pédale qui accroche en cours de course signale un câble à inspecter. -
    Inspecter le câble visible (côté pédale et côté boîte) à la recherche de fils dénudés, de rouille ou d''effilochage. -
    Vérifier le réglage de la tension du câble : un jeu excessif ou une tension trop forte peut être rectifié avant remplacement
    si le câble est encore sain. - Contrôler l''état de la gaine : une gaine fendue ou écrasée compromet la lubrification
    du câble et accélère son usure. Pour un diagnostic personnalisé adapté à votre véhicule, utilisez notre outil de diagnostic
    gratuit.'
  S3: 'Le câble d''embrayage transmet mécaniquement l''effort de la pédale vers la fourchette d''embrayage sur les véhicules
    à commande mécanique (par opposition aux systèmes hydrauliques). Ce composant est soumis à des milliers de cycles de traction
    par an, et son usure se manifeste progressivement avant la rupture. Un câble mal dimensionné en longueur ou en diamètre
    fausse le réglage du jeu de pédale et peut rendre le débrayage incomplet. - Longueur totale du câble (gaine + toron) —
    mesure sur l''original — La longueur du câble est spécifique au véhicule et au positionnement du point de fixation sur
    le mécanisme. Un câble trop court impose une tension permanente sur la fourchette et use prématurément la butée d''embrayage
    ; un câble trop long dépasse les possibilités de réglage de la patte de tension. - Diamètre du toron acier et charge de
    rupture minimale — Le toron est l''âme métallique tressée qui supporte la charge. Les câbles d''embrayage courants ont
    un toron de 3 à 5 mm de diamètre avec une charge de rupture entre 8 et 15 kN. Utiliser un câble de diamètre inférieur
    à l''origine réduit la marge de sécurité avant rupture, particulièrement sur les véhicules à moteur puissant ou avec embrayage
    renforcé. - Type de terminal (olive) aux deux extrémités : rotule, tige filetée ou embout cylindrique — L''extrémité côté
    pédale et l''extrémité côté fourchette utilisent des terminaux différents selon le constructeur. Un mauvais type d''embout
    côté fourchette empêche l''encliquetage ou crée un jeu axial qui génère un retour d''effort sous le pied et une course
    de pédale instable. - Matériau de la gaine et revêtement intérieur — La gaine externe protège le toron et guide sa course.
    Les gaines modernes sont tressées acier avec revêtement intérieur PTFE (polytétrafluoroéthylène) qui supprime la nécessité
    de lubrification. Les gaines sans PTFE (câbles d''origine ancienne génération) nécessitent un graissage au montage avec
    une graisse câble spécifique. - Compatibilité avec le système de réglage : réglage automatique ou manuel — Certains véhicules
    équipent un réglage automatique du câble (tendeur à cliquet intégré à la gaine). Ce système absorbe l''allongement progressif
    du câble neuf au rodage. Ces câbles ont un embout de gaine spécifique et ne peuvent pas être remplacés par un câble à
    réglage manuel sans modifier la fixation côté carrosserie. - État de la gaine de guidage au passage de carrosserie — vérifier
    avant montage — Le câble passe dans un passe-cloison en caoutchouc qui le protège de l''humidité et de la chaleur. Si
    ce passe-cloison est craquelé ou absent, l''humidité pénètre dans la gaine, corrode le toron depuis l''intérieur et provoque
    une rupture sur le câble neuf dans les 12 à 24 mois. - Câble avec ou sans gaine pré-montée — vérifier ce qui est fourni
    — Certains câbles sont vendus toron seul (pour réutiliser la gaine d''origine en bon état) ; d''autres sont livrés avec
    gaine complète. Si la gaine d''origine est froissée, coudée ou corrodée, il faut impérativement commander un câble avec
    gaine neuve intégrée.'
  S4_DEPOSE: 📖 Avant de démonter, consultez la fiche technique Câble d'embrayage pour connaître les spécifications. - Débranchez
    la batterie. - Dégagez l'accès à la boîte de vitesses si nécessairepour faciliter le travail et pour avoir un accès facile
    au câble d'embrayagecôté moteur. - Démontez le boîtier du filtre à air , si nécessaire. - Démontez la batterie. - Démontez
    le bac de batterie. - Libérez le câble d'embrayage de la biellette de lafourchette. - Déboîtez l'arrêt de gaine du câble
    d'embrayage. - Sortez le câble d'embrayage par l'encoche. - Dans l'habitacle au niveau du pédalier, poussez lagaine du
    câble d'embrayage vers le compartiment moteur. - Retirez le câble d'embrayage.
  S4_REPOSE: '- Vérifiez que le câble d''embrayage neuf est de la mêmelongueur que celui démonté. - Contrôlez l''état d''usure
    de la butée d''embrayage et laremplacée si nécessaire. - Contrôlez l''état d''usure du kit d''embrayage et le remplacési
    nécessaire. - Faire passer le câble d''embrayage dans l''orificeallant côté pédalier. - Accrochez le câble à la pédale
    d''embrayage. - Mettre en place l''arrêt de gaine de câble dansl''orifice. - Remontez l''arrêt de gaine côté boîte de
    vitesses. - Mettre en place le câble d''embrayage sur la biellettede la fourchette d''embrayage . - Contrôlez que le câble
    d''embrayage est bien mis enplace. - Remontez le bac de la batterie. - Remontez la batterie. - Remontez le filtre à air
    . - Rebranchez la batterie. - Contrôlez le bon fonction du système d''embrayage. ✅ Après remontage, vérifiez les spécifications
    dans la fiche technique Câble d''embrayage.'
  S5: 'Erreurs fréquentes avec le câble d''embrayage : - ❌ Ne pas graisser la gaine — un câble neuf dans une gaine sèche durcira
    rapidement. Graisser les deux extrémités au montage. - ❌ Mal régler le jeu de garde — trop de jeu = embrayage qui patine.
    Pas assez = embrayage qui ne débraye pas complètement. Le jeu typique à la pédale est de 10 à 20 mm. - ❌ Plier le câble
    lors du passage — un rayon de courbure trop serré provoque un effort excessif et une usure prématurée. - ❌ Oublier de
    vérifier la fourchette d''embrayage — si la fourchette est usée ou fissurée, le câble neuf cassera rapidement. Vérifier
    aussi la rotule d''appui. - ❌ Monter un câble de longueur incorrecte — vérifier la longueur totale et le type d''embouts
    (rotule, chape, clip). Les câbles OES Cofle ou TRW sont les plus fiables.'
  S6: 'Après le remplacement de votre câble d''embrayage, effectuez ces vérifications dans l''ordre. - Contrôler la tension
    du câble à froid : la pédale ne doit pas être dure ni présenter de jeu excessif supérieur à 20 mm en début de course -
    Vérifier le point de patinage : il doit se trouver à mi-course de la pédale, ni en tout début ni en fin de course - Lubrifier
    les extrémités du câble et la gaine selon les préconisations constructeur pour éviter le grippage prématuré - Effectuer
    10 manœuvres complètes pédale enfoncée/relâchée pour confirmer l''absence de craquement ou grincement - Inspecter visuellement
    le cheminement du câble : aucun coude brutal, aucun frottement sur une pièce mobile - Contrôler la fixation aux deux extrémités
    (côté pédale et côté fourchette) : les goupilles ou clips doivent être correctement engagés Retrouvez les spécifications
    techniques sur la fiche référence câble d''embrayage.'
  S7: 'Comment régler un câble d''embrayage ? Le réglage se fait via l''écrou de réglage situé sur la fourchette d''embrayage
    (côté boîte de vitesses) ou au niveau de la pédale. Tournez l''écrou pour obtenir un jeu de 1 à 2 cm en haut de course
    de pédale. Sur les câbles à rattrapage automatique, appuyez à fond sur la pédale 10 fois puis vérifiez le point de patinage
    — il doit être au tiers inférieur de la course. Câble ou commande hydraulique : quelle différence ? Le câble est mécanique
    (gaine + câble acier) — simple, léger, pas de purge. La commande hydraulique utilise un émetteur + récepteur + liquide
    de frein — plus douce mais nécessite une purge en cas d''intervention. Les véhicules récents (post-2005) utilisent majoritairement
    l''hydraulique. Le câble reste courant sur les utilitaires et les citadines d''entrée de gamme. Quel est le prix d''un
    câble d''embrayage ? Un câble d''embrayage coûte entre 15 € et 60 € selon le véhicule. La main-d''œuvre est de 30 minutes
    à 1h30 selon l''accessibilité. Au total, comptez 50 à 150 € tout compris. C''est l''une des réparations d''embrayage les
    moins chères. Quels sont les signes d''un câble d''embrayage à remplacer ? Les signes typiques : pédale dure ou qui accroche,
    point de patinage très haut, pédale qui ne revient pas seule, bruits de frottement. Un câble effiloché peut lâcher sans
    prévenir — si vous sentez des à-coups à la pédale ou des brins visibles sur la gaine, remplacez sans attendre. Pièces
    à contrôler lors du remplacement du câble d''embrayage : - Butée d''embrayage — si le câble était dur, la butée a pu être
    sollicitée en excès. Vérifier l''état et le jeu axial. - Kit d''embrayage — si le câble a cassé en roulant, le disque
    et le mécanisme ont subi un choc. Inspecter l''usure. - Volant moteur — sur les véhicules à volant bi-masse, un à-coup
    d''embrayage peut révéler un volant fatigué. - Fourchette d''embrayage — vérifier l''usure de la rotule d''appui et l''absence
    de fissure. Pièce souvent oubliée. - Pédalier et axe — vérifier que l''axe de pédale n''est pas grippé (cause fréquente
    de pédale dure attribuée à tort au câble).'
  S8: 'Câble d''embrayage OE ou adaptable ?Les câbles OES (Cofle, TRW) sont fiables. Vérifiez la longueur exacte et le type
    d''embouts (rotule, chape). Un câble mal adapté cassera rapidement ou donnera une course de pédale incorrecte. Comment
    savoir si mon câble d''embrayage est usé ?Pédale dure ou point de patinage très haut, craquement en appuyant sur la pédale,
    câble effiloché visible sous le capot, embrayage qui accroche ou ne débraye pas complètement. Tous les combien régler
    le câble d''embrayage ?Contrôle du jeu de garde tous les 30 000 km. Le câble s''étire naturellement avec l''usage. Quand
    le réglage est en butée (plus de marge), il faut le remplacer. Peut-on changer le câble d''embrayage soi-même ?Oui, opération
    accessible. Déconnecter côté pédale et côté fourchette, passer le nouveau câble dans la gaine, graisser, régler le jeu.
    Compter 30 min à 1h selon l''accès. Quel est le prix d''un câble d''embrayage ?Entre 15 € et 80 € pour la pièce. Main-d''œuvre
    : 30 min à 1h en atelier. Vérifier aussi l''état de la fourchette et de la butée pour éviter de démonter deux fois.'
  META: '{"og_title": "Câble d''embrayage : diagnostic et réglage du jeu", "meta_title": "Câble d''embrayage dur : réglage,
    changement et prix | AutoMecanik", "gate_report": "PASS", "schema_type": "Article", "og_description": "Pédale dure, patinage
    haut ou câble effiloché ? Diagnostic, réglage et remplacement du câble d''embrayage.", "primary_intent": "diagnostic",
    "char_count_desc": 143, "char_count_title": 53, "meta_description": "Pédale d''embrayage dure ou point de patinage trop
    haut ? Diagnostiquez le câble d''embrayage : réglage du jeu, signes d''usure et remplacement."}'
---

# Câble d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre l'effort mécanique de la pédale vers la fourchette

**Actions principales:** transmettre l'effort, tirer, pousser, relier, actionner

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Craquement ou grincement en appuyant sur la pedale**
  craquement ou grincement en appuyant sur la pedale
- **Pedale qui reste enfoncee cable casse**
  pedale qui reste enfoncee cable casse

### 🟢 Autres Symptômes

- pedale d embrayage dure ou difficile a enfoncer
- point de patinage tres haut ou tres bas
- cable visible effiloche ou rouille
- embrayage qui ne debraye pas completement

## Procédure de Diagnostic

Pour diagnostiquer un problème de câble d'embrayage:

1. **Inspection visuelle** - Examiner l'état du câble d'embrayage
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

- butee-d-embrayage
- kit-d-embrayage
- volant-moteur

## Critères de Compatibilité

Pour commander le bon câble d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "effort parfait"

## FAQ

**Câble d'embrayage OE ou adaptable ?**
Les câbles OES (Cofle, TRW) sont fiables. Vérifiez la longueur exacte et le type d'embouts (rotule, chape). Un câble mal adapté cassera rapidement.

**Comment savoir si mon câble d'embrayage est usé ?**
Pédale dure ou point de patinage très haut, craquement en appuyant sur la pédale, câble effiloché visible, embrayage qui accroche.

**Tous les combien régler le câble d'embrayage ?**
Contrôle du jeu tous les 30 000 km. Le câble s'étire naturellement. Quand le réglage est en butée, il faut le remplacer.

**Peut-on changer le câble d'embrayage soi-même ?**
Oui, opération accessible. Déconnecter côté pédale et côté fourchette, passer le nouveau câble, régler le jeu. Compter 30 min à 1h.

**Quelle erreur éviter avec le câble d'embrayage ?**
Ne pas forcer si le câble est coincé. Graisser les gaines. Vérifier l'état de la fourchette et de la rotule. Bien régler le jeu après montage.
## Symptomes courants

### Pedale d'embrayage dure
- **Quand** : A chaque actionnement
- **Caracteristique** : Resistance excessive, fatigue musculaire

### Pedale molle ou spongieuse
- **Quand** : Constant
- **Caracteristique** : Course excessive, point de patinage haut

### Patinage embrayage
- **Quand** : En acceleration forte, en cote
- **Caracteristique** : Regime moteur monte sans acceleration proportionnelle

### Bruit au debrayage
- **Quand** : Appui sur la pedale
- **Caracteristique** : Grincement, sifflement, claquement

### Difficulte passage vitesses
- **Quand** : A froid ou constant
- **Caracteristique** : Craquements, resistance

## Causes possibles et solutions

### 1. Disque d'embrayage use
- **Probabilite** : 50%
- **Verification** : Patinage, kilometrage eleve
- **Solution** : Remplacement kit embrayage complet
- **Pieces** : Kit embrayage (disque, mecanisme, butee)
- **Urgence** : Moyenne a haute

### 2. Butee hydraulique/mecanique HS
- **Probabilite** : 25%
- **Verification** : Bruit a l'appui pedale, fuite liquide
- **Solution** : Remplacement butee
- **Pieces** : Butee d'embrayage
- **Urgence** : Moyenne

### 3. Volant moteur bimasse HS
- **Probabilite** : 15%
- **Verification** : Vibrations excessives, claquements au ralenti
- **Solution** : Remplacement volant moteur
- **Pieces** : Volant moteur bimasse ou conversion simple masse
- **Urgence** : Moyenne

### 4. Emetteur/recepteur d'embrayage defaillant
- **Probabilite** : 10%
- **Verification** : Pedale molle, fuite liquide
- **Solution** : Remplacement cylindre emetteur ou recepteur
- **Pieces** : Emetteur, recepteur, liquide de frein
- **Urgence** : Moyenne

## Duree de vie embrayage

| Utilisation | Duree de vie |
|-------------|--------------|
| Autoroute | 150 000 - 200 000 km |
| Mixte | 100 000 - 150 000 km |
| Urbaine | 80 000 - 120 000 km |
| Agressive | 50 000 - 80 000 km |

## Recommandations

- **Kit complet** : Toujours remplacer disque + mecanisme + butee ensemble
- **Volant moteur** : Controler systematiquement le volant lors du changement
- **Marques** : Privilegier Valeo, LuK, Sachs
- **Conduite** : Eviter de garder le pied sur la pedale d'embrayage


## References supplementaires

<!-- materialized-from-db manual/305b057993b9 2026-04-03 -->
### Données techniques OEM — Câble d'embrayage

# Données techniques OEM — Câble d'embrayage
Source : fr.wikipedia.org (1 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- composite
- céramique
- hydraulique
- pneumatique
- rainuré
- électrique

## Matériaux
- céramique

## Symptomes supplementaires

<!-- materialized-from-db diagnostic/embrayage.md 2026-01-08 -->
### Diagnostic - Embrayage

# Embrayage - Diagnostic complet

## Symptomes courants

### Pedale d'embrayage dure
- **Quand** : A chaque actionnement
- **Caracteristique** : Resistance excessive, fatigue musculaire

### Pedale molle ou spongieuse
- **Quand** : Constant
- **Caracteristique** : Course excessive, point de patinage haut

### Patinage embrayage
- **Quand** : En acceleration forte, en cote
- **Caracteristique** : Regime moteur monte sans acceleration proportionnelle

### Bruit au debrayage
- **Quand** : Appui sur la pedale
- **Caracteristique** : Grincement, sifflement, claquement

### Difficulte passage vitesses
- **Quand** : A froid ou constant
- **Caracteristique** : Craquements, resistance

## Causes possibles et solutions

### 1. Disque d'embrayage use
- **Probabilite** : 50%
- **Verification** : Patinage, kilometrage eleve
- **Solution** : Remplacement kit embrayage complet
- **Pieces** : Kit embrayage (disque, mecanisme, butee)
- **Urgence** : Moyenne a haute

### 2. Butee hydraulique/mecanique HS
- **Probabilite** : 25%
- **Verification** : Bruit a l'appui pedale, fuite liquide
- **Solution** : Remplacement butee
- **Pieces** : Butee d'embrayage
- **Urgence** : Moyenne

### 3. Volant moteur bimasse HS
- **Probabilite** : 15%
- **Verification** : Vibrations excessives, claquements au ralenti
- **Solution** : Remplacement volant moteur
- **Pieces** : Volant moteur bimasse ou conversion simple masse
- **Urgence** : Moyenne

### 4. Emetteur/recepteur d'embrayage defaillant
- **Probabilite** : 10%
- **Verification** : Pedale molle, fuite liquide
- **Solution** : Remplacement cylindre emetteur ou recepteur
- **Pieces** : Emetteur, recepteur, liquide de frein
- **Urgence** : Moyenne

## Duree de vie embrayage

| Utilisation | Duree de vie |
|-------------|--------------|
| Autoroute | 150 000 - 200 000 km |
| Mixte | 100 000 - 150 000 km |
| Urbaine | 80 000 - 120 000 km |
| Agressive | 50 000 - 80 000 km |

## Recommandations

- **Kit complet** : Toujours remplacer disque + mecanisme + butee ensemble
- **Volant moteur** : Controler systematiquement le volant lors du changement
- **Marques** : Privilegier Valeo, LuK, Sachs
- **Conduite** : Eviter de garder le pied sur la pedale d'embrayage
