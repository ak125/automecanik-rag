---
category: freinage
slug: machoires-de-frein
title: Mâchoires de frein
pg_id: 70
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-04-02'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:rag-enrich-from-web-corpus
  last_enriched_at: '2026-04-02'
  v5_migrated_at: '2026-03-29'
domain:
  role: Creer la friction a l'interieur du tambour
  must_be_true:
  - frotter
  - exercer une pression interne
  - s'user progressivement
  must_not_contain:
  - disque
  - plaquette
  - etrier
  - ventile
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
  - ❌ "remplacement plaquettes"
  cost_range:
    min: 20
    max: 80
    currency: EUR
    unit: l'unite
    source: estimation categorie
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE (OES)
  - tier: Adaptable qualite
  - tier: Reconditionne
  - tier: Echange standard
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
    label: Frein a main qui ne tient plus ou mal
    severity: securite
  - id: S2
    label: Bruit de frottement metallique a l arriere
    severity: confort
  - id: S3
    label: Tambour raye ou strie a l interieur
    severity: confort
  - id: S4
    label: Epaisseur de garniture inferieure a 2mm
    severity: confort
  - id: S5
    label: Freinage arriere desequilibre tire d un cote
    severity: securite
  - id: S6
    label: Poussiere frein noire excessive jantes
    severity: securite
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : frein a main qui ne tient plus ou mal'
  depose_steps: []
  quick_checks:
  - 'Observer : frein a main qui ne tient plus ou mal ?'
  - Bruit de frottement metallique a l arriere ?
  - 'Observer : tambour raye ou strie a l interieur ?'
  - 'Observer : epaisseur de garniture inferieure a 2mm ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Frein a main qui ne tient plus ou mal
  - Bruit de frottement metallique a l arriere
  - Tambour raye ou strie a l interieur
  - Epaisseur de garniture inferieure a 2mm
  - Freinage arriere desequilibre tire d un cote
  - Poussiere frein noire excessive jantes
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '70'
  intro_title: A quoi sert Mâchoires de frein ?
  risk_title: Pourquoi remplacer Mâchoires de frein a temps ?
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
  - question: 'Mâchoires OE ou adaptables : que choisir ?'
    answer: Les mâchoires OES (TRW, Bosch, Valeo) offrent d excellentes performances. Vérifiez le diamètre du tambour et la
      largeur des garnitures.
  - question: Comment savoir si mes mâchoires sont usées ?
    answer: Frein à main inefficace, bruit de frottement métallique à l arrière, tambour rayé à l intérieur, épaisseur de
      garniture inférieure à 2mm.
  - question: Tous les combien changer les mâchoires ?
    answer: Entre 80 000 et 120 000 km en moyenne. Les mâchoires arrière sont moins sollicitées que le freinage avant, d où
      leur durée de vie supérieure.
  - question: Peut-on changer ses mâchoires soi-même ?
    answer: Oui mais opération technique. Il faut déposer le tambour et les ressorts. Comptez 1h par côté. Attention au remontage
      des ressorts dans le bon ordre.
  - question: Quelle erreur éviter avec les mâchoires ?
    answer: Ne pas toucher les garnitures avec des mains grasses. Vérifier l état des cylindres de roue. Toujours changer
      par paire (essieu).
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
doc_id: 14712c8b-d4f3-5594-96c0-2cf7febf13ff
content_hash: sha256:9b18aa2eb78fe65d
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
  _source: ate-freinage.fr + bremboparts.com + delphiautoparts.com + textar.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 9
  _has_tech_data: true
  types_variants:
  - type: 'composite'
    source_ref: corpus RAG web OEM
  technical_notes:
    norme_ecer90: 'ecer90'
    val_0_5__: '0,5 %'
    val_100__: '100 %'
    val_100_a: '100 a'
    val_115_nm: '115 Nm'
    val_120_nm: '120 Nm'
    val_17_a: '17 a'
    val_18_a: '18 a'
    val_19_a: '19 a'
    val_2_a: '2 a'
    val_3_a: '3 a'
    val_33_a: '33 a'
    val_4_a: '4 a'
    val_5_a: '5 a'
    val_6_a: '6 a'
    val_61_a: '61 a'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Lorsque vous appuyez sur la pédale de frein la pression duliquide de frein va actionner le cylindrede roue de la voiture
    qui va écarter les mâchoires de frein pour créer une friction à l''intérieurdu tambour de frein de la voiture. Les mâchoiresde
    frein sont liées par un système de rattrapage à ressort pour les maintenir au plusprès des parois intérieures du tambour
    de frein et sont reliées au câble de freinde stationnement pour le fonctionnent du freinde stationnement. En savoir plus
    : mâchoires de frein — définition et rôle mécanique 🚨 Bruit Mâchoires de frein : causes et diagnostic'
  S2: 'Ne pas attendre la panne complete pour intervenir. Symptômes d''usure : - Frein a main qui ne tient plus ou mal - Bruit
    de frottement metallique a l arriere - Tambour raye ou strie a l interieur - Epaisseur de garniture inferieure a 2mm -
    Freinage arriere desequilibre tire d un cote - Poussiere frein noire excessive jantes'
  S2_DIAG: 'SymptômeCause probableActionFrein a main qui ne tient plus ou mallocaliser source et verifier usure mecaniqueObserver
    : frein a main qui ne tient plus ou mal ?Bruit de frottement metallique a l arrierebruit anormal detecte : localiser source
    et verifier usure mecaniqueBruit de frottement metallique a l arriere ?Tambour raye ou strie a l interieurUsure ou defaillance
    causant : frein a main qui ne tient plus ou malObserver : tambour raye ou strie a l interieur ?Epaisseur de garniture
    inferieure a 2mmlocaliser source et verifier usure mecaniqueObserver : epaisseur de garniture inferieure a 2mm ?Freinage
    arriere desequilibre tire d un cotelocaliser source et verifier usure mecaniqueObserver : frein a main qui ne tient plus
    ou mal ?Poussiere frein noire excessive janteslocaliser source et verifier usure mecaniqueObserver : frein a main qui
    ne tient plus ou mal ?'
  S3: 'Avant de commander, vérifiez ces caractéristiques : - Diamètre du tambour : les mâchoires doivent correspondre au diamètre
    intérieur du tambour (180, 200, 228 mm, etc.) - Largeur de la garniture : varie selon le modèle (30 à 42 mm), elle détermine
    la surface de friction - Type de fixation : mâchoire à levier de frein à main intégré (côté secondaire) ou sans levier
    - Kit complet ou mâchoires seules : certains kits incluent les ressorts de rappel et le kit de fixation Méthode : mesurer
    le diamètre intérieur du tambour et la largeur de garniture de l''ancienne mâchoire, ou utiliser le sélecteur véhicule.
    ➡️ Trouver les mâchoires compatibles avec votre véhicule Pour aller plus loin : consultez notre guide d''achat mâchoires
    de frein — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: '📖 Avant de démonter, consultez la fiche technique Mâchoires de frein pour connaître les spécifications. - Relâchez
    le freinà main. - Levez et calez le véhicule. - Démontez la roue. - Démontez le cache de protection qu''est fixé aucentre
    du tambour de frein gauche ou droite. - Desserrez l''écrou de fixation du tambour de frein du véhicule. - Démontez le
    tambourde frein. - Démontez les brides de maintien des mâchoires de frein sur le flasque. - A l''aide d''un tournevis
    écarter les mâchoires de frein puis les retirez. Attention : les mâchoires de frein reste solidaires aux ressorts et au
    câble de frein à main de la voiture. - A l''aide d''une pince tendre le câble de frein à main. - Démontez les mâchoiresde
    frein.'
  S4_REPOSE: 'Remontage des mâchoires de frein à tambour — procédure détaillée Changer les mâchoires de frein seules est une
    opération plus délicate qu''un changement de plaquettes : les ressorts sont sous tension, le mécanisme de rattrapage doit
    être réglé et l''orientation des mâchoires est asymétrique. Une photo du montage d''origine avant dépose est fortement
    conseillée. - Préparation des mâchoires neuves — Vérifier que les mâchoires neuves ont exactement la même longueur de
    garniture, le même rayon de courbure et les mêmes trous de fixation que les anciennes. Sur certains véhicules, la mâchoire
    avant (primaire) est légèrement plus courte que la mâchoire arrière (secondaire) — les inverser crée un freinage résiduel
    ou une efficacité réduite. - Nettoyage du flasque et lubrification sélective — Nettoyer le flasque au nettoyant frein.
    Appliquer une fine couche de graisse cuivre uniquement sur les ergots de glissement des mâchoires sur le flasque (4 à
    6 points d''appui). Ne jamais mettre de graisse sur les garnitures ni sur la surface intérieure du tambour. - Mise en
    place de la mâchoire primaire — Positionner la mâchoire primaire (garniture plus courte) en appui sur les ergots du flasque,
    les extrémités engagées dans les pistons du cylindre de roue (ou les encoches du flasque côté bas). Fixer le ressort de
    maintien central à l''aide de la tige de fixation et d''une pince spéciale (rotation à 90°). - Mise en place de la mâchoire
    secondaire — Procéder de la même manière pour la mâchoire secondaire. Avant de l''engager définitivement, connecter l''extrémité
    du câble de frein à main dans la came du levier de frein à main situé sur la mâchoire secondaire. - Montage des ressorts
    de rappel — Accrocher le ressort de rappel supérieur entre les deux têtes de mâchoires, en utilisant un tournevis à ressort
    ou une pince plate. Le ressort de rappel inférieur (si présent) relie les deux extrémités basses des mâchoires. La tension
    de montage est élevée — utiliser les outils dédiés pour éviter de blesser les garnitures ou de déformer les ressorts.
    - Réglage du mécanisme de rattrapage — Tourner la roue étoilée de réglage (accessible par l''orifice de réglage au dos
    du flasque ou en faisant tourner la roue phonique) jusqu''à ce que les mâchoires touchent légèrement le tambour. Reculer
    ensuite de 5 à 8 clics pour obtenir un léger jeu. Ce réglage détermine l''efficacité de freinage et du frein à main. -
    Remontage du tambour — Glisser le tambour sur le moyeu. S''il ne rentre pas facilement, réduire encore le réglage des
    mâchoires de 2 à 3 clics. Serrer la vis de retenue. Tourner le tambour à la main sur 2 tours complets : la résistance
    doit être uniforme. - Ajustement final du câble de frein à main — Régler la tension du câble pour obtenir un blocage de
    roue entre 3 et 5 clics. Plus de 5 clics = câble trop détendu ou mâchoires trop éloignées. Moins de 3 clics = risque de
    freinage résiduel permanent. - Test de rodage — Effectuer 5 freinages modérés depuis 50 km/h (sans bloquer les roues)
    pour roder les garnitures. Observer les 200 premiers km : aucun échauffement anormal (odeur de brûlé) ne doit apparaître,
    ce qui signalerait un réglage trop serré. ✅ Après remontage, vérifiez les spécifications dans la fiche technique Mâchoires
    de frein.'
  S5: '- Mauvais diamètre de mâchoire — Les mâchoires ne s''ajustent pas dans le tambour ou frottent en permanence. → Vérifier
    le diamètre du tambour avant commande. - Confondre mâchoire primaire et secondaire — La mâchoire primaire (garniture courte)
    va côté avant du sens de rotation, la secondaire (garniture longue) côté arrière. → Repérer la position avant démontage.
    - Réutiliser les vieux ressorts de rappel — Des ressorts fatigués empêchent le recul correct des mâchoires, provoquant
    surchauffe et usure prématurée. → Remplacer systématiquement avec le kit de ressorts. - Oublier le mécanisme de rattrapage
    automatique — Les mâchoires neuves sont plus épaisses que les anciennes usées, le réglage du rattrapage doit être repositionné.
    → Régler la came ou la vis de rattrapage. - Ne pas nettoyer le plateau de frein — La poussière de garniture (potentiellement
    nocive) et la rouille empêchent le bon positionnement. → Nettoyer au nettoyant frein, jamais à l''air comprimé. - Monter
    des garnitures contaminées — Toucher la surface de friction avec des mains grasses ou la laisser tremper dans du liquide
    de frein réduit l''adhérence. → Manipuler avec des gants propres. - Forcer le remontage du tambour — Si le tambour ne
    se remet pas, les mâchoires sont trop écartées. → Réduire le réglage du rattrapage avant de remettre le tambour. - Ne
    pas régler le frein à main — La tension du câble doit être ajustée après chaque remplacement de mâchoires. → Régler pour
    un blocage en 3 à 5 clics de levier. 📖 Fiche technique Mâchoires de frein — spécifications à vérifier avant montage.'
  S6: 'Contrôles statiques - Vérifier que le tambour tourne librement avec un léger frottement (pas de blocage) - Contrôler
    le mécanisme de rattrapage : la roue doit se bloquer quand on resserre, puis tourner librement en desserrant d''un cran
    - Vérifier le frein à main : blocage des roues en 3 à 5 clics - Pomper la pédale de frein : elle doit devenir ferme après
    4 à 6 appuis - Vérifier l''absence de fuite au cylindre de roue Essai routier progressif - Freinage doux à 10 km/h sur
    parking, vérifier que le véhicule freine droit - Tester le frein à main sur pente montante et descendante - Augmenter
    à 30, 50 km/h — un léger frottement les 100 premiers km est normal (rodage) ⚠️ Arrêter immédiatement si : pédale molle,
    tirage d''un côté, bruits de raclement métallique, frein à main inopérant, odeur de brûlé sur une roue arrière. 🚨 Bruit
    Mâchoires de frein : causes et diagnostic'
  S_GARAGE: 'Nous vous recommandons de confier cette intervention à un professionnel : - Plusieurs causes possibles de défaillance
    (3 identifiées) nécessitent un diagnostic professionnel Un garagiste qualifié dispose de l''outillage et de l''expérience
    nécessaires pour effectuer cette opération en toute sécurité.'
  S7: Quel est le prix d'un mâchoires de frein ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur pour
    trouver le mâchoires de frein compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon mâchoires de frein est à changer ?Les signes d'usure les plus courants sont détaillés dans la section diagnostic
    ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un mâchoires de frein défaillant
    ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule. Consultez la section
    symptômes pour évaluer l'urgence du remplacement.- Cylindre de roue. - Boulon de roue. - Kit de freins arrière. - Accessoires
    de mâchoire. 📖 Fiche technique Mâchoires de frein — intervalles et spécifications d’entretien.
  S8: 'Mâchoires de frein et plaquettes de frein : quelle différence concrète ? Les plaquettes de frein frottent contre les
    deux faces d''un disque métallique (freins à disque, généralement à l''avant et sur les véhicules récents à l''arrière
    aussi). Les mâchoires de frein s''écartent vers l''extérieur et frottent contre la surface intérieure cylindrique d''un
    tambour. Le principe de friction est le même, mais les contraintes mécaniques diffèrent : les mâchoires travaillent à
    l''expansion (force centrifuge), tandis que les plaquettes travaillent à la compression. Les mâchoires ne peuvent jamais
    remplacer des plaquettes ni l''inverse. Combien de kilomètres durent des mâchoires de frein ? En moyenne 60 000 à 120
    000 km, soit nettement plus que les plaquettes avant, car l''essieu arrière ne supporte que 30 à 40 % de l''effort de
    freinage total. La durée est raccourcie par l''utilisation fréquente du frein à main (qui sollicite le mécanisme de frein
    à tambour indépendamment du circuit hydraulique), les descentes longues sans frein moteur, et les véhicules portant régulièrement
    leur charge maximale. Faut-il remplacer le tambour en même temps que les mâchoires ? Seulement si le diamètre intérieur
    du tambour dépasse la valeur maximale gravée dessus (par exemple « Ø max. 181 mm » pour un tambour neuf de 180 mm), ou
    si la surface présente des rainures profondes de plus de 0,5 mm. Un tambour légèrement rayé peut être repris au tour (rectification)
    si le diamètre après reprise reste dans les tolérances. Un tambour trop large accueille mal les mâchoires neuves et réduit
    la surface de contact. Pourquoi le tambour ne rentre plus après avoir monté les mâchoires neuves ? Les garnitures neuves
    sont plus épaisses que les garnitures usées. Il faut réduire le réglage du mécanisme de rattrapage (tourner la roue étoilée
    dans le sens de réduction) pour rapprocher les mâchoires, puis refaire le réglage une fois le tambour en place. Sur les
    véhicules avec rattrapage automatique, le réglage se fait progressivement lors des premiers freinages en marche arrière.
    Un bruit de claquement apparaît après le montage — que vérifier en premier ? Un claquement à chaque rotation de roue indique
    généralement un ressort de rappel mal positionné ou une mâchoire dont l''extrémité n''est pas correctement engagée dans
    son ergot. Déposer le tambour et vérifier les points d''appui des deux mâchoires, la position de chaque ressort et le
    verrouillage des brides de maintien. Un ressort de rappel détaché est parfois visible sans déposer le tambour en regardant
    par l''orifice de réglage. La poussière de garniture noire sur les jantes est-elle un signe d''usure critique ? Une légère
    poussière noire sur les jantes arrière est normale. Une quantité excessive signale soit un réglage trop serré (mâchoires
    frottant en permanence), soit un cylindre de roue qui fuit (huile contaminerait la garniture et provoquerait à la fois
    une poussière abondante et un freinage asymétrique). Inspecter le cylindre de roue par l''intérieur du tambour : toute
    trace de liquide hydraulique impose le remplacement immédiat du cylindre. 📖 Pour plus de détails techniques : fiche Mâchoires
    de frein'
  META: 'Guide complet pour remplacer vos mâchoires de frein : compatibilité tambour, erreurs de montage, réglage du rattrapage
    et FAQ frein arrière.'
---

# Mâchoires de frein - Guide Diagnostic Complet

## Fonction et Rôle

Creer la friction a l'interieur du tambour

**Actions principales:** frotter, exercer une pression interne, s'user progressivement, s'ecarter, plaquer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Frein a main qui ne tient plus ou mal**
  frein a main qui ne tient plus ou mal
- **Freinage arriere desequilibre tire d un cote**
  freinage arriere desequilibre tire d un cote
- **Poussiere frein noire excessive jantes**
  poussiere frein noire excessive jantes

### 🟢 Autres Symptômes

- bruit de frottement metallique a l arriere
- tambour raye ou strie a l interieur
- epaisseur de garniture inferieure a 2mm

## Procédure de Diagnostic

Pour diagnostiquer un problème de mâchoires de frein:

1. **Inspection visuelle** - Examiner l'état du mâchoires de frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
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

- cable-de-frein-a-main
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- flexible-de-frein
- interrupteur-des-feux-de-freins
- kit-de-freins-arriere
- maitre-cylindre-de-frein

## Critères de Compatibilité

Pour commander le bon mâchoires de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "remplacement plaquettes"

## FAQ

**Mâchoires OE ou adaptables : que choisir ?**
Les mâchoires OES (TRW, Bosch, Valeo) offrent d excellentes performances. Vérifiez le diamètre du tambour et la largeur des garnitures.

**Comment savoir si mes mâchoires sont usées ?**
Frein à main inefficace, bruit de frottement métallique à l arrière, tambour rayé à l intérieur, épaisseur de garniture inférieure à 2mm.

**Tous les combien changer les mâchoires ?**
Entre 80 000 et 120 000 km en moyenne. Les mâchoires arrière sont moins sollicitées que le freinage avant, d où leur durée de vie supérieure.

**Peut-on changer ses mâchoires soi-même ?**
Oui mais opération technique. Il faut déposer le tambour et les ressorts. Comptez 1h par côté. Attention au remontage des ressorts dans le bon ordre.

**Quelle erreur éviter avec les mâchoires ?**
Ne pas toucher les garnitures avec des mains grasses. Vérifier l état des cylindres de roue. Toujours changer par paire (essieu).
## Definition

La norme ECE R90 encadre la conformite des pieces de freinage de remplacement (ex: plaquettes, disques) avec des exigences de performance proches de l'equipement d'origine.

## Pourquoi c'est important

- meilleure coherence de freinage
- reduction du risque de pieces non conformes
- reference utile pour le choix de pieces sur vehicule de tourisme

## Points a verifier

- mention ECE R90 sur le produit/emballage
- correspondance avec la reference vehicule
- provenance et tracabilite
## Types de vibrations

### Vibrations au volant
- **À basse vitesse (< 50 km/h)** : Problème de pneus ou jantes
- **À haute vitesse (> 80 km/h)** : Équilibrage ou géométrie
- **Au freinage** : Disques voilés

### Vibrations dans l'habitacle
- **Moteur au ralenti** : Supports moteur
- **En accélération** : Transmission, cardans
- **À vitesse constante** : Pneus, roulements

### Vibrations dans la pédale de frein
- **Au freinage** : Disques voilés, plaquettes usées

## Causes et solutions

### 1. Pneus déséquilibrés
- **Symptôme** : Vibration volant à partir de 80-100 km/h
- **Vérification** : Visuel sur les masses d'équilibrage
- **Solution** : Équilibrage des 4 pneus
- **Coût** : 40-60€
- **Urgence** : Moyenne

### 2. Pneus usés irrégulièrement
- **Symptôme** : Vibration + bruit de roulement
- **Vérification** : Usure en "dents de scie"
- **Solution** : Remplacement pneus + géométrie
- **Urgence** : Haute

### 3. Roulement de roue défaillant
- **Symptôme** : Grondement augmentant avec la vitesse
- **Vérification** : Jeu dans la roue, bruit en virage
- **Solution** : Remplacement roulement
- **Pièces** : Kit roulement de roue
- **Urgence** : Haute - Sécurité

### 4. Cardans usés
- **Symptôme** : Claquement en braquant, vibration en accélération
- **Vérification** : Soufflets déchirés, jeu
- **Solution** : Remplacement cardan
- **Pièces** : Cardan complet ou transmission
- **Urgence** : Haute

### 5. Disques de frein voilés
- **Symptôme** : Vibration pédale au freinage
- **Vérification** : Mesure au comparateur
- **Solution** : Rectification ou remplacement
- **Pièces** : Disques de frein
- **Urgence** : Moyenne

### 6. Supports moteur fatigués
- **Symptôme** : Vibration au ralenti dans l'habitacle
- **Vérification** : Visuel sur silent-blocs
- **Solution** : Remplacement supports
- **Pièces** : Support moteur, silent-bloc
- **Urgence** : Basse
## Symptômes courants

### Grincement aigu au freinage
- **Quand** : Au moment du freinage léger ou modéré
- **Caractéristique** : Son métallique aigu, type "crissement"

### Sifflement continu
- **Quand** : Pendant tout le freinage
- **Caractéristique** : Son aigu constant

### Bruit sourd / grondement
- **Quand** : Freinage appuyé
- **Caractéristique** : Vibration ressentie dans la pédale

### Claquement
- **Quand** : Début ou fin de freinage
- **Caractéristique** : Bruit sec, ponctuel

## Causes possibles et solutions

### 1. Plaquettes de frein usées
- **Probabilité** : 70%
- **Vérification** : Témoin usure allumé, épaisseur < 3mm
- **Solution** : Remplacement des plaquettes
- **Pièces** : Plaquettes de frein avant/arrière
- **Urgence** : Haute - Sécurité

### 2. Disques de frein voilés
- **Probabilité** : 15%
- **Vérification** : Vibration pédale, usure inégale visible
- **Solution** : Rectification ou remplacement des disques
- **Pièces** : Disques de frein
- **Urgence** : Moyenne

### 3. Étrier grippé
- **Probabilité** : 10%
- **Vérification** : Usure asymétrique des plaquettes
- **Solution** : Nettoyage/graissage ou remplacement étrier
- **Pièces** : Kit réparation étrier, étrier complet
- **Urgence** : Haute

### 4. Absence de graisse sur glissières
- **Probabilité** : 5%
- **Vérification** : Plaquettes difficiles à bouger
- **Solution** : Nettoyage et graissage
- **Pièces** : Graisse haute température
- **Urgence** : Basse

## Questions complémentaires pour affiner le diagnostic

1. Le bruit apparaît-il à froid ou à chaud ?
2. Le bruit est-il présent sur les 4 roues ou localisé ?
3. Y a-t-il une vibration dans le volant ?
4. Quand avez-vous changé vos plaquettes pour la dernière fois ?
5. Avez-vous un témoin d'usure allumé au tableau de bord ?

## Recommandations

- **Contrôle visuel** : Vérifier l'épaisseur des plaquettes (minimum 3mm)
- **Kilométrage** : Remplacement préventif tous les 30 000 - 50 000 km
- **Qualité** : Privilégier les marques équipementier (Bosch, Brembo, TRW)


## Conseils supplementaires

<!-- materialized-from-db web/19c4896f8fc0 2026-03-28 -->
### Instructions pour remplacer... - Montage auto - section-1

# Instructions pour remplacer... - Montage auto

- Skip to main content Skip to menu Skip to footer Partager sur Instructions pour remplacer les mâchoires de frein Nous vous conseillons de lire et de suivre attentivement les instructions fournies. Vous trouverez les mêmes instructions dans l’emballage des mâchoires de frein. N’oubliez pas de les conserver pendant toute la durée de vie du produit. En cas de passage de propriété, elles devront être remises au nouveau propriétaire du véhicule. Ces instructions de montage sont un guide générique sur les réparations, qui peuvent varier d’un système de freinage à l’autre. Les instructions spécifiques émises par le constructeur du véhicule ou du système de freinage doivent impérativement être respectées. Identifier soigneusement la référence correcte de la série de mâchoires pour le véhicule en question, en fonction aussi de l’année de production et du système de freinage. Les mâchoires doivent être remplacées pour l’ensemble de l’essieu. Procédure de remplacement Avant de remplacer les mâchoires de frein, nous vous conseillons de faire attention aux indications suivantes: 1. Veiller à ce que le véhicule ne puisse pas se déplacer pendant la réparation, le soulever et s’assurer de sa stabilité. ATTENTION! Pour garantir la sécurité, toujours utiliser des outils adaptés et fiables. 2. Démonter une roue à la fois, en gardant l’autre roue comme référence pour le montage . ATTENTION ! Ne pas agir sur la pédale de frein après avoir démonté le tambour. 3. Démonter les ressorts qui fixent les mâchoires au plateau . 4. Décrocher le câble du frein à main. ATTENTION! Contrôler que le câble n’est pas usé. Dans le cas contraire, le remplacer. 5. Déposer les mâchoires et démonter le petit cylindre. ​​​ 6. Nettoyer le plateau et le tambour en utilisant un chiffon imbibé de détergent (ne pas utiliser de détergents à base d’huile minérale). ATTENTION! Lors de la phase de nettoyage, ne pas soulever de poussières. Si elles sont inhalées, elles risquent de nuire à la santé. Pour travailler dans des milieux fermés, utiliser un masque. ATTENTION! Le liquide de frein contenu dans les petits cylindres peut provoquer des dommages, le manipuler avec soin, ne pas jeter le liquide dans l’environnement. Procédure de montage 1. Remonter le nouveau petit cylindre sur le plateau et visser le tuyau du liquide de frein. Reassemble the new cylinder on the back plate and screw on the brake fluid tube. 2. Seulement pour les KITS PRÉ-ASSEMBLÉS: Déposer le support inférieur. 3. Appliquer de la graisse à point de fusion élevé sur les pièces du plateau en contact avec les mâchoires. 4. ATTENTION! La graisse de lubrification de ne doit pas être appliquée sur le matériau de freinage ou sur la partie intérieure de travail du tambour, cela risquerait de compromettre le fonctionnement du système de freinage. 5. Accrocher le câble du frein à main et loger les mâchoires sur le plateau. 6. Fixer les mâchoires au plateau en utilisant les ressorts spécifiques. 6. Centrer les mâchoires dans leur logement en les replaçant comme à l’origine. ATTENTION! Ne pas manipuler les dispositifs de réglage automatique pour garantir leur fonctionnement correct. 7. Actionner légèrement le frein à main et vérifier le fonctionnement correct de tous les mécanismes et tringleries. Après quoi, tout remettre dans la position initiale. 8. Remonter le tambour et régler le dispositif de réglage automatique en agissant plusieurs fois sur la pédale de frein. Purger le circuit de freinage. IMPORTANT! Les pièces de rechange contenues dans cet emballage ne doivent pas être montées par l’automobiliste (Interdiction aux termes de la Loi 122/92), toujours s’adresser à des ateliers et des mécaniciens spécialisés. 9. Les mâchoires de frein doivent être remplacées pour l’ensemble de l’essieu. Informations générales et de sécurité Le produit Brembo a été conçu pour respecter les meilleurs standards de sécurité . Les Produits ne doivent pas être destinés à une utilisation différente de celle pour laquelle ils ont été conçus et fabriqués. L’ utilisation à d’autres fins , la modification ou la manipulation du produit risquent d’altérer son fonctionnement et de compromettre sa sécurité. Toute modification éventuelle ou toute utilisation impropre rendent nulles les Limitations de garantie et peuvent rendre la personne utilisant le Produit dans ces conditions responsable quant aux dommages physiques ou matériels éventuellement causés à des tiers. Les plaquettes de frein s’usent et elles doivent, donc, être contrôlées à intervalles réguliers. Lorsque le matériau de friction atteint 2 mm d’épaisseur ou lorsque le témoin de l’indicateur d’usure s’allume, il faut impérativement remplacer les plaquettes . Les disques Brembo Kit EV et les plaquettes Brembo Kit EV doivent toujours être montés ensemble. Leur association avec d’autres produits compromet le bon fonctionnement du KIT. Dans ces instructions, lorsqu’il est indiqué « DANGER! », cela signifie que le non-respect de la procédure indiquée a de fortes probabilités de provoquer de graves dommages physiques ou même la mort . La mention « ATTENTION! » indique une procédure dont le non-respect peut provoquer des dommages physiques , alors que la mention « AVERTISSEMENT! » indique une procédure dont le non-respect peut provoquer des dommages au véhicule. DANGER! Avant de commencer la procédure de remplacement, s’assurer que la pièce de rechange est adaptée à la marque et au modèle du véhicule. Le Produit revêt une importance fondamentale pour la sécurité du véhicule sur lequel il est installé et il doit, donc, être installé par du personnel qualifié ayant reçu une formation adéquate ou possédant suffisamment d’expérience dans l’installation et dans l’utilisation prévue du Produit. L’installateur doit avoir à sa disposition l’ outillage adéquat à l’installation et posséder des connaissances et une expérience appropriées pour s’occuper de l ’entretien du véhicule. Une installation inadéquate ou erronée, due au non-respect de ces instructions ou autres, rendra nulles les Limitations de garantie et pourrait rendre l’installateur responsable quant aux dommages physiques ou matériels éventuellement provoqués. Brembo décline toute responsabilité en cas de dommage matériel ou physique provoqué à ou par une personne conduisant un véhicule sur lequel le produit aurait été installé de façon inappropriée. ATTENTION! Les pièces remplacées doivent être éliminées selon les dispositions prescrites par la loi. Il est important d’éviter de frapper violemment ou d’endommager le Produit et ses composants, parce que cela risquerait de réduire son efficacité et de provoquer des dysfonctionnements. Si nécessaire, remplacer les composants endommagés. Pour éviter tout dommage physique, nous conseillons de: Toujours porter des gants lors des opérations de démontage et de remontage des composants présentant des arêtes coupantes.

![Centrer les mâchoires dans leur logement en les replaçant comme à l’origine.   ATTENTION ! Ne pas manipuler les dispositifs de réglage automatique pour garantir leur fonctionnement correct.](_raw/web-images/80e8b633f7c39434.jpg)

![Remonter le tambour et régler le dispositif de réglage automatique en agissant plusieurs fois sur la pédale de frein. Purger le circuit de freinage.   IMPORTANT ! Les pièces de rechange contenues dans cet emballage ne doivent pas être montées par l’automobiliste (Interdiction aux termes de la Loi 122/92), toujours s’adresser à des ateliers et des mécaniciens spécialisés.   9. Les mâchoires de frein doivent être remplacées pour l’ensemble de l’essieu.](_raw/web-images/ca4547da691947f9.jpg)

![Le produit Brembo a été conçu pour respecter les meilleurs standards de sécurité. Les Produits ne doivent pas être destinés à une utilisation différente de celle pour laquelle ils ont été conçus et fabriqués. L’utilisation à d’autres fins, la modification ou la manipulation du produit risquent d’altérer son fonctionnement et de compromettre sa sécurité.](_raw/web-images/5ca2bd43c39fe577.jpg)

- Éviter le contact direct de la peau avec le matériau de friction des plaquettes et mâchoires parce que cela risque de provoquer des abrasions.

- Ne pas mettre en contact le matériau de friction des plaquettes, les disques, les étriers ou les tuyaux de frein avec des graisses, huiles, autres lubrifiants ou produits dégraissants à base d’huile minérale parce que cela peut endommager le frein. Remplacer ces pièces en cas de contamination, si nécessaire. Les plaquettes de frein doivent être remplacées par essieu.

- Ne pas utiliser d'outils pointus parce qu’une utilisation impropre risque de provoquer des dommages. Utiliser exclusivement l’outillage spécifique (clé dynamométrique, outil à expansion, extracteurs, etc.)

- Si l’on remarque des dommages lors de l’intervention sur le système de freinage, il faut les réparer.

<!-- materialized-from-db web/624cbc1f42da 2026-03-28 -->
### Instructions pour remplacer... - Montage auto - section-1

# Instructions pour remplacer... - Montage auto

- Skip to main content Skip to menu Skip to footer Partager sur Instructions pour remplacer les freins à tambour Nous vous conseillons de lire et de suivre attentivement les instructions fournies. Vous trouverez les mêmes instructions dans l’emballage des freins à tambour. N’oubliez pas de les conserver pendant toute la durée de vie du produit. En cas de passage de propriété, elles devront être remises au nouveau propriétaire du véhicule. Ces instructions de montage sont un guide générique sur les réparations, qui peuvent varier d’un système de freinage à l’autre. Les instructions spécifiques émises par le constructeur du véhicule ou du système de freinage doivent impérativement être respectées. Avant de commencer la procédure de remplacement, s’assurer que la pièce de rechange utilisée pour le remplacement est adaptée à la marque et au modèle du véhicule. Procédure de remplacement La procédure décrite concerne une roue, elle doit être répétée sur l’autre roue de l’essieu. 1. Démonter les roues. 2. Le frein à main doit être complètement relâché. 3. Mettre complètement 4. Démonter le tambour du frein. AVERTISSEMENT ! N’appliquer aucune force pour éviter d’endommager les moyeux et les roulements des roues, les capteurs et les bagues dentées. AVERTISSEMENT! Utiliser les outils spéciaux prévus. 5. Dans le cas de tambours de freins avec roulements des roues et bagues dentées intégrées, démonter ces pièces pour leur réutilisation postérieure (uniquement si les pièces ne présentent de dommages ou de défauts). Avant de passer aux autres phases de remplacement, nous vous conseillons de suivre ces étapes pour le nettoyage et le contrôle du Produit qui favorisent un meilleur montage. Nettoyage/contrôle/montage préalable 1. Nettoyer la surface de la bride/rehausse de centrage dans le moyeu de la roue. Celui-ci doit être parfaitement propre, exempt de toute trace de rouille et d’ébarbure, lisse. Surface de la bride brillante (ne pas utiliser de ponceuses d’angle !). 2. Dans le cas de tambours de freins avec roulements des roues intégrés, monter les pièces neuves ou démontées ne présentant pas de dommages ou de défauts, en suivant les prescriptions. Appliquer le lubrifiant prescrit. 3. Monter les nouveaux éléments d’étanchéité pour les roulements des roues. 4. Si présente, monter la bague dentée (neuve ou sans dommages ni défauts). ​​​​​​ DANGER! Tous les composants du frein à tambour, comme cylindres de la roue, mâchoires de frein, ressorts, leviers, supports, languettes, etc. doivent être contrôlés avant leur réutilisation pour vérifier leur parfait état et fonctionnement ou bien procéder au remplacement des pièces. 5. Sauf indication contraire, éliminer complètement le traitement anticorrosion du nouveau tambour de frein uniquement au niveau de la surface de la bride et de la surface de travail. Vérifier que la surface de la bride est propre, sans ébarbure et intacte. Procédure de montage 1. En cas d’utilisation de nouvelles mâchoires de frein, mettre complètement à zéro leur réglage. 2. Dans le cas d’un moyeu de la roue séparé, appliquer uniformément une très fine couche d’huile anticorrosion (pas en pâte) sur la bride. 3. Centrer le tambour de frein. En fonction du type de construction, fixer avec la vis ou avec le dispositif de sécurité et/ou avec la roue. 4. Serrer uniformément en croix ou (procéder dans le sens des aiguilles d'une montre) en deux phases en utilisant le moment de torsion prescrit. 5. Sur les tambours de frein avec moyeu de la roue intégré, centrer le tambour de frein, régler/fixer le roulement de la roue selon les prescriptions, fermer avec une calotte neuve ou ne présentant pas de dommages ni défauts. 6. Régler selon les prescriptions le jeu des mâchoires du frein de service/frein à main. 7. Dans le cas d’un moyeu de la roue séparé, appliquer uniformément une très fine couche d’huile anticorrosion (pas en pâte) sur la bride. 8. Si le système hydraulique avait été ouvert, remplir/purger le système de freinage avec le liquide prescrit. Contrôle du fonctionnement ATTENTION! Contrôler que les parties en caoutchouc ne sont pas endommagées. Si nécessaire, les remplacer. 1. Actionner la pédale pour rapprocher les mâchoires du tambour. Répéter l’opération jusqu’à ce que la course de la pédale soit correcte. 2. Contrôler le niveau du liquide de frein dans le réservoir et faire l’appoint, si nécessaire. 3. Effectuer l'équilibrage de la roue. 4. Remonter la roue et serrer les vis de roue de la façon indiquée par le constructeur du véhicule ou dans le catalogue Brembo. Essai et rodage Effectuer un essai sur route. Durant cet essai, éviter de freiner brusquement et pendant plus de 3 secondes. L’essai sert à vérifier l’absence de bruits et de vibrations provenant des freins. Le rodage à conseiller à l’utilisateur final consiste à parcourir 200 km, en effectuant des freinages doux et courts, sans faire intervenir l’ABS. DANGER! Un mauvais rodage risque de compromettre l’efficacité du système de freinage . Informations générales et de sécurité Le produit Brembo a été conçu pour respecter les meilleurs standards de sécurité . Les Produits ne doivent pas être destinés à une utilisation différente de celle pour laquelle ils ont été conçus et fabriqués. L’ utilisation à d’autres fins , la modification ou la manipulation du produit risquent d’altérer son fonctionnement et de compromettre sa sécurité. Toute modification éventuelle ou toute utilisation impropre rendent nulles les Limitations de garantie et peuvent rendre la personne utilisant le Produit dans ces conditions responsable quant aux dommages physiques ou matériels éventuellement causés à des tiers. Dans ces instructions, lorsqu’il est indiqué « DANGER! », cela signifie que le non-respect de la procédure indiquée a de fortes probabilités de provoquer de graves dommages physiques ou même la mort. La mention « ATTENTION! » indique une procédure dont le non-respect peut provoquer des dommages physiques , alors que la mention « AVERTISSEMENT! » indique une procédure dont le non-respect peut provoquer des d

[...]
