---
category: distribution
slug: chaine-de-distribution
title: Chaîne de distribution
pg_id: 1123
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
  role: Synchroniser la rotation de l'arbre a cames avec le vilebrequin de maniere durable
  must_be_true:
  - synchroniser
  - entrainer
  - transmettre
  must_not_contain:
  - courroie
  - caoutchouc
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - courroie-de-distribution
  - kit-de-distribution
  - galet-tendeur-de-courroie-de-distribution
  - galet-enrouleur-de-courroie-de-distribution
  - pompe-a-eau
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
  - ❌ "repare le moteur"
  cost_range:
    min: 150
    max: 400
    currency: EUR
    unit: chaîne seule
    source: catalogue automecanik
  quality_tiers:
  - tier: Equipement d origine (OE)
  - tier: Equivalent OE / kit complet
  - tier: Piece adaptable
  brands:
    premium:
    - Gates
    - Continental/Contitech
    standard:
    - Dayco
    - SKF
    - INA
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Bruit de cliquetis metallique au demarrage a froid
    severity: confort
  - id: S2
    label: Claquement qui disparait apres quelques secondes
    severity: confort
  - id: S3
    label: Voyant moteur allume codes calage
    severity: immobilisation
  - id: S4
    label: Moteur qui manque de puissance
    severity: confort
  - id: S5
    label: Bruit de ferraille permanent cote distribution
    severity: confort
  - id: S6
    label: Difficultes de demarrage
    severity: confort
  - id: S7
    label: Consommation huile anormale tendeur hydraulique
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - identifier origine fuite et verifier joints
  quick_checks:
  - Bruit de cliquetis metallique au demarrage a froid ?
  - 'Observer : claquement qui disparait apres quelques secondes ?'
  - Voyant moteur allume codes calage ?
  - 'Observer : moteur qui manque de puissance ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Bruit de cliquetis metallique au demarrage a froid
  - Claquement qui disparait apres quelques secondes
  - Voyant moteur allume codes calage
  - Moteur qui manque de puissance
  - Bruit de ferraille permanent cote distribution
  - Difficultes de demarrage
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '1123'
  intro_title: A quoi sert Chaîne de distribution ?
  risk_title: Pourquoi remplacer Chaîne de distribution a temps ?
  risk_explanation: '**Pièce HS** - Le chaîne de distribution peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le chaîne de distribution peut être hors service et nécessiter un remplacement'
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: La chaîne de distribution doit-elle être changée ?
    answer: Oui, contrairement aux idées reçues, la chaîne s'use et s'allonge. Sur certains moteurs (VAG TSI/TDI, BMW N47),
      le remplacement préventif est recommandé.
  - question: Quand remplacer la chaîne ?
    answer: Pas de kilométrage fixe, mais contrôle recommandé vers 150 000-200 000 km. Si bruit métallique au démarrage ou
      codes défaut calage, contrôle urgent.
  - question: Peut-on rouler avec une chaîne usée ?
    answer: Risqué. Une chaîne allongée décale le calage, ce qui peut endommager le moteur. En cas de rupture, les dégâts
      sont les mêmes qu'une courroie cassée.
  - question: Quelles sont les erreurs fréquentes à éviter ?
    answer: Ignorer le bruit de cliquetis au démarrage (signe d'usure). Ne pas remplacer les tendeurs et guides avec la chaîne.
      Utiliser de l'huile non conforme (tendeur hydraulique).
  - question: Comment faire un diagnostic rapide ?
    answer: Bruit métallique au démarrage à froid qui disparaît → chaîne allongée / tendeur faible. Bruit permanent → chaîne
      ou guide très usé. Codes P0016/P0017 → calage décalé.
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
doc_id: 96b56d73-0206-5e1f-94f9-d24b57ce9f60
content_hash: sha256:0fa05a7974fa1f05
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
  area: Face laterale du moteur, derriere le carter de distribution
  access: Depose courroie accessoire + carter distribution
  adjacent_parts:
  - courroie
  - galets
  - pompe a eau
  - poulie
installation:
  difficulty: difficile (pro recommande)
  time: 3h a 6h
  tools:
  - kit calage distribution
  - cle dynamometrique
  - extracteur poulie
  prerequisite: Moteur cale au PMH, ne pas tourner le moteur sans courroie
phase5_enrichment:
  _source: bremboparts.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 3
  types_variants:
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_10_nm: '10 Nm'
    val_115_nm: '115 Nm'
    val_125_nm: '125 Nm'
    val_16_nm: '16 Nm'
    val_16_a: '16 a'
    val_180_nm: '180 Nm'
    val_20_nm: '20 Nm'
    val_210_nm: '210 Nm'
    val_22_nm: '22 Nm'
    val_3_a: '3 a'
    val_304_a: '304 a'
    val_32_a: '32 a'
    val_36_nm: '36 Nm'
    val_4_a: '4 a'
    val_437_a: '437 a'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    La chaîne de distribution est fabriquée en acier et elle se compose de
    plusieurs maillons métalliques. Elle permet la synchronisation du
    vilebrequin avec l'arbre à cames. Une chaîne de distribution peut être
    double. Le graissage de la chaîne de distribution est assuré par l'huile
    moteur à travers un pulvérisateur d'huile. La tension de la chaîne est
    assurée par un tendeur hydraulique qu'est alimenté par l'huile moteur et le
    guidage est assuré par des patins caoutchouc (glissière de chaîne). Une
    chaîne de distribution est très résistante et elle est presque inusable. La
    chaîne de distribution a un gros avantage, elle se casse difficilement dans
    ce cas elle se remplace presque jamais sauf dans des cas bien précis. Les
    désavantages d'une chaîne de distribution qu'elle est trop lourde, d'être
    énergivore (son fonctionnement consomme de l'énergie du moteur) et elle fait
    trop de bruit. En savoir plus : chaîne de distribution — définition et rôle
    mécanique 🚨 Bruit Chaîne de distribution : causes et diagnostic
  S2: >-
    Unechaîne de distribution défectueuse présente plusieurs symptômes : - Bruit
    de chaîne quand votre le doit fournir un effort à bas régime. - Lors d'un
    contrôle visuel vous remarquez la présenced'un jeu dans le tendeur de chaîne
    ou les glissières.Une chaîne de distribution HS et qu'elle n'est pas
    remplacée à temps peut causer plusieurs dégâts dans le moteur qui peuvent
    amener au changement de ce dernier par exemple rupture de l'arbre à cames,
    rupture de vilebrequin Diagnostic complet : identifier une panne de chaîne
    de distribution
  S3: >-
    La chaîne de distribution est la pièce maîtresse de la synchronisation
    moteur : elle relie le vilebrequin aux arbres à cames avec une tolérance de
    calage de quelques degrés. Contrairement à la courroie de distribution en
    caoutchouc, la chaîne est en acier et peut durer la vie du moteur si la
    lubrification est correcte — mais elle s'allonge et claque quand l'huile
    n'est pas changée à temps. Un mauvais choix de kit (tendeur, patin
    d'amortisseur, pompe à huile) est la principale cause de réintervention dans
    l'année suivant le remplacement. - Ne pas confondre chaîne de distribution
    et courroie de distribution : la chaîne est en acier multimaillons, baigne
    dans l'huile moteur, et est visible dans le carter de distribution côté
    moteur (pas de cache extérieur en caoutchouc). La courroie est en
    élastomère, à sec, avec un cache plastique latéral. Commander l'une à la
    place de l'autre est une erreur immédiatement détectable au montage. - Kit
    complet ou chaîne seule : toujours préférer le kit : le kit de chaîne de
    distribution comprend chaîne(s), tendeur hydraulique, patins
    d'amortissement, pignons (vilebrequin et arbres à cames), et parfois la
    pompe à huile. Remplacer la chaîne seule sans les patins usés ou le tendeur
    fatigué aboutit dans 60 % des cas à un bruit résiduel ou une nouvelle casse
    dans les 20 000 km. - Nombre de maillons et pas de chaîne : les chaînes de
    distribution existent en pas 8 mm (chaînes simples) ou 9,525 mm (chaînes à
    rouleaux) avec un nombre de maillons précis selon la distance vilebrequin /
    arbre à cames. Un maillon de trop ou de moins empêche le montage ou crée un
    mauvais calage. - Tendeur hydraulique : type à rochet ou à rappel par
    ressort : les tendeurs hydrauliques à rochet (non réinitialisables) doivent
    être remplacés à chaque intervention — ils ne peuvent pas être réutilisés
    une fois déposés. Les tendeurs à ressort peuvent être réinitialisés mais
    sont à vérifier. Identifier votre type avant commande. - Calage moteur via
    kit de calage (outils de blocage) : la chaîne de distribution n'est pas une
    pièce isolée — son remplacement nécessite de bloquer le vilebrequin et les
    arbres à cames avec des outils de calage spécifiques au moteur (broches de
    calage, verrous de PMH). Sans ces outils, le risque de heurte de soupapes
    est élevé sur les moteurs à zone de sécurité réduite. - Compatibilité avec
    le système de calage variable (VVT/VTC) : les moteurs équipés d'un calage
    variable des soupapes (Valvetronic BMW, VTEC Honda, MultiAir Fiat) intègrent
    des pignons à déphasage hydraulique. Le kit de chaîne doit être
    spécifiquement compatib avec ces pignons — les kits génériques ne
    comprennent pas les bagues d'étanchéité internes des déphaseurs. - Qualité
    d'huile moteur et intervalles de vidange comme critère indirect : une chaîne
    de distribution présentant un allongement prématuré (moins de 80 000 km)
    signale souvent une huile trop ancienne ou de mauvaise spécification. Avant
    de choisir une référence renforcée (chaîne double rangée), vérifier
    l'historique de maintenance huile du moteur. Pour aller plus loin :
    consultez notre guide d'achat chaîne de distribution — comparatif marques,
    critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Chaîne de distribution
    pour connaître les spécifications. Note : la méthode de démontage remontage
    d'un kit chaîne de distribution change d'un moteur à un autre dans ce cas il
    faut se référer à la revue technique de votre véhicule. - Débranchez la
    batterie. - Vidanger l'huile moteur et le liquide de refroidissement. -
    Démontez toutes les pièces nécessaires pour faciliter l'accès à la chaîne de
    distribution (filtre à air , turbo?). - Levez et calez le véhicule. -
    Démontez la roue. - Démontez le pare-boue. - Démontez la courroie
    d'accessoires. - Démontez le galet tendeur de la courroie d'accessoires. -
    Démontez la pompe à eau . - Démontez la poulie de vilebrequin. - Redescendre
    le véhicule. - Immobilisez l'arbre à cames à l'aide d'une pige de blocage
    appropriée. - Levez le véhicule. - Immobilisez le vilebrequin à l'aide d'une
    pige de blocage appropriée. - Redescendre le véhicule. - Desserrez les
    fixations du carter de kit chaîne de distribution. - Démontez le carter de
    kit chaîne de distribution. - Poussez et verrouillez le tendeur de chaîne de
    distribution. - Démontez le tendeur de chaîne de distribution. - Immobilisez
    la poulie d'arbre à cames avec un outil approprié. - Desserrez la fixation
    de la poulie d'arbre à cames. - Démontez l'outil de blocage de la poulie
    d'arbre à cames. - Desserrez la fixation de la roue dentée de vilebrequin. -
    Démontez la chaîne de distribution avec la poulie d'arbre à cames et la roue
    dentée de vilebrequin.
  S4_REPOSE: >-
    Le remontage d'une chaîne de distribution est une opération de haute
    précision qui conditionne le calage moteur. Une erreur de repère d'un seul
    maillon provoque un décalage d'allumage et d'injection qui peut, sur les
    moteurs à pistons interférents, entraîner une collision soupapes-pistons dès
    le premier démarrage. Travaillez avec le schéma de calage du constructeur
    sous les yeux. - Vérifiez que la chaîne de distribution neuve est identique
    à celle démontée : nombre de maillons, pas de chaîne, largeur. Une chaîne
    avec un pas différent refuse de s'engrener correctement sur les pignons. -
    Contrôlez le bon fonctionnement des glissières de chaîne et remplacez-les si
    elles présentent une usure visible (rainures profondes, craquelures). Des
    glissières usées détruisent une chaîne neuve en moins de 20 000 km. -
    Contrôlez le bon fonctionnement du pulvérisateur d'huile (gicleur de
    lubrification de chaîne). Dégorgez le gicleur à l'air comprimé si
    nécessaire. Sans lubrification, la chaîne s'allonge prématurément. -
    Remontez la chaîne de distribution avec la poulie d'arbre à cames et la roue
    dentée de vilebrequin en respectant scrupuleusement les repères de calage
    constructeur. Ne serrez pas encore les fixations des pignons. - Remontez le
    tendeur de chaîne et serrez ses fixations au couple prescrit. Vérifiez que
    la goupille de blocage est encore en place pour maintenir le tendeur
    comprimé pendant le montage. - Immobilisez la poulie d'arbre à cames avec
    l'outil de blocage approprié. Serrez la fixation de la poulie au couple
    prescrit, puis démontez l'outil de blocage. Serrez ensuite la fixation de la
    roue dentée de vilebrequin. - Retirez la goupille d'immobilisation du
    tendeur de chaîne pour libérer la tension automatique. Le tendeur doit
    prendre appui progressivement sur la chaîne — un claquement sec indique un
    tendeur défaillant à remplacer immédiatement. - Changez le joint
    d'étanchéité du carter de distribution. Nettoyez les faces de joint à la
    pierre plate. Appliquez de la pâte à joint si prescrit par le constructeur,
    en cordon continu sans interruption. - Remontez le carter de distribution,
    puis la poulie de vilebrequin, la pompe à eau, le galet tendeur de courroie
    d'accessoires et la courroie d'accessoires dans l'ordre inverse de la
    dépose. Serrez chaque fixation au couple prescrit. - Remontez la roue et
    toutes les pièces déposées pour accéder à la distribution. Rebranchez la
    batterie. Remplissez l'huile moteur avec le grade et la norme prescrits,
    puis remplissez et purgez le liquide de refroidissement. Démarrez et
    vérifiez l'absence de bruit de cliquetis et de voyant calage (codes P0016,
    P0017).
  S5: >-
    - ❌ "homologué CT - ❌ "sécurité garantie - ❌ "zéro panne - ❌ "garanti à vie
    - ❌ "repare le moteur
  S6: >-
    Après le remplacement de votre chaîne de distribution, effectuez ces
    vérifications dans l'ordre. - Vérifiez le calage de la distribution en
    positionnant le moteur au PMH (point mort haut) du cylindre 1 et confirmez
    l'alignement des repères sur les pignons d'arbre à cames et vilebrequin. -
    Contrôlez la tension du tendeur hydraulique : après le premier démarrage, la
    pression d'huile doit tendre automatiquement la chaîne — aucun jeu excessif
    visible. - Vérifiez le niveau d'huile moteur avant démarrage : le tendeur
    hydraulique de chaîne fonctionne à la pression d'huile, un niveau trop bas
    perturbe son fonctionnement. - Démarrez le moteur et écoutez pendant 10
    secondes à froid : aucun cliquetis métallique côté distribution ne doit
    persister au-delà des 3 premières secondes. - Effacez les codes défaut OBD
    liés au calage (codes arbre à cames et vilebrequin) et vérifiez qu'ils ne
    reviennent pas après 5 minutes de fonctionnement. - Contrôlez l'absence de
    fuite d'huile autour du carter de distribution et des joints de culasse
    latéraux après 15 minutes de chauffe. - Effectuez un trajet de 30 minutes
    incluant des phases à régime moteur varié : le moteur doit répondre sans
    à-coup ni manque de puissance. Consultez également la page références chaîne
    de distribution pour identifier la pièce compatible avec votre véhicule.
  S7: >-
    Quel est le prix d'un chaîne de distribution ?Le prix varie selon le
    véhicule et la marque. Utilisez notre sélecteur pour trouver le chaîne de
    distribution compatible avec votre véhicule et comparer les tarifs des
    différents équipementiers.Comment savoir si mon chaîne de distribution est à
    changer ?Les signes d'usure les plus courants sont détaillés dans la section
    diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par un
    professionnel.Peut-on rouler avec un chaîne de distribution défaillant ?Cela
    dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la
    sécurité du véhicule. Consultez la section symptômes pour évaluer l'urgence
    du remplacement.- courroie d accessoire - kit de chaine de distribution -
    pompe a eau - pompe a injection - poulie d arbre a came
  S8: >-
    Comment choisir Chaîne de distribution compatible avec mon
    vehiculeRenseignez marque, modele, type moteur et annee, puis verifiez la
    reference Quand remplacer Chaîne de distribution ?En cas de bruit de
    cliquetis metallique au demarrage a froid ou de degradation Puis-je monter
    Chaîne de distribution sans verification atelier ?Le montage peut exiger
    controles de couple, alignement et references.
  META: >-
    {"meta_title":"Chaîne de distribution : cliquetis ou calage ? |
    AutoMecanik","meta_description":"Bruit métallique au démarrage à froid ou
    voyant moteur codes calage ? Ce guide explique quand changer la chaîne de
    distribution et les erreurs à éviter pour protéger le moteur.","meta_title_l
    ength":56,"meta_description_length":159,"primary_intent":"diagnostic","targe
    t_symptoms":["bruit de cliquetis metallique au demarrage a froid","voyant
    moteur allume codes calage","claquement qui disparait apres quelques seconde
    s"],"category":"distribution","severity_note":"symptome_immobilisation_prese
    nt"}
---

# Chaîne de distribution - Guide Diagnostic Complet

## Fonction et Rôle

Synchroniser la rotation de l'arbre a cames avec le vilebrequin de maniere durable

**Actions principales:** synchroniser, entrainer, transmettre

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Voyant moteur allume codes calage**
  voyant moteur allume codes calage

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement qui disparait apres quelques secondes**
  claquement qui disparait apres quelques secondes

### 🟢 Autres Symptômes

- bruit de cliquetis metallique au demarrage a froid
- moteur qui manque de puissance
- bruit de ferraille permanent cote distribution
- difficultes de demarrage
- consommation huile anormale tendeur hydraulique

## Procédure de Diagnostic

Pour diagnostiquer un problème de chaîne de distribution:

1. **Inspection visuelle** - Examiner l'état du chaîne de distribution
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le chaîne de distribution peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-d-accessoire
- kit-de-chaine-de-distribution
- pompe-a-eau
- pompe-a-injection
- poulie-d-arbre-a-came

## Critères de Compatibilité

Pour commander le bon chaîne de distribution, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"

## FAQ

**La chaîne de distribution doit-elle être changée ?**
Oui, contrairement aux idées reçues, la chaîne s'use et s'allonge. Sur certains moteurs (VAG TSI/TDI, BMW N47), le remplacement préventif est recommandé.

**Quand remplacer la chaîne ?**
Pas de kilométrage fixe, mais contrôle recommandé vers 150 000-200 000 km. Si bruit métallique au démarrage ou codes défaut calage, contrôle urgent.

**Peut-on rouler avec une chaîne usée ?**
Risqué. Une chaîne allongée décale le calage, ce qui peut endommager le moteur. En cas de rupture, les dégâts sont les mêmes qu'une courroie cassée.

**Quelles sont les erreurs fréquentes à éviter ?**
Ignorer le bruit de cliquetis au démarrage (signe d'usure). Ne pas remplacer les tendeurs et guides avec la chaîne. Utiliser de l'huile non conforme (tendeur hydraulique).

**Comment faire un diagnostic rapide ?**
Bruit métallique au démarrage à froid qui disparaît → chaîne allongée / tendeur faible. Bruit permanent → chaîne ou guide très usé. Codes P0016/P0017 → calage décalé.


## Symptomes supplementaires

<!-- materialized-from-db diagnostic/distribution-courroie.md 2026-01-08 -->
### Diagnostic - Distribution et courroie

# Distribution et courroie - Diagnostic complet

## Symptomes courants

### Bruit de claquement moteur
- **Quand** : Au ralenti ou a l'acceleration
- **Caracteristique** : Claquement rythmique, lie au regime moteur

### Sifflement au demarrage
- **Quand** : A froid, disparait a chaud
- **Caracteristique** : Son aigu type courroie patinante

### Perte de puissance
- **Quand** : En acceleration
- **Caracteristique** : Moteur qui "tire" moins

### Temoin moteur allume
- **Quand** : Aleatoire
- **Caracteristique** : Voyant orange fixe

## Causes possibles et solutions

### 1. Courroie de distribution usee
- **Probabilite** : 40%
- **Verification** : Age/kilometrage, aspect visuel (fissures, effilochage)
- **Solution** : Remplacement kit distribution complet
- **Pieces** : Kit distribution (courroie, galets, pompe a eau)
- **Urgence** : CRITIQUE - Risque casse moteur

### 2. Galet tendeur defaillant
- **Probabilite** : 25%
- **Verification** : Jeu excessif, bruit de roulement
- **Solution** : Remplacement galet(s)
- **Pieces** : Galet tendeur, galet enrouleur
- **Urgence** : Haute

### 3. Pompe a eau HS
- **Probabilite** : 20%
- **Verification** : Fuite liquide de refroidissement, jeu axial
- **Solution** : Remplacement pompe a eau
- **Pieces** : Pompe a eau
- **Urgence** : Haute

### 4. Courroie accessoires usee
- **Probabilite** : 15%
- **Verification** : Fissures, patinage
- **Solution** : Remplacement courroie accessoires
- **Pieces** : Courroie poly-V, galet tendeur accessoires
- **Urgence** : Moyenne

## Intervalles de remplacement

| Type moteur | Intervalle | Kilometrage |
|-------------|------------|-------------|
| Essence | 5 ans | 100 000 km |
| Diesel | 5 ans | 120 000 km |
| HDI/TDI | 4 ans | 160 000 km |

## Recommandations

- **Remplacement preventif** : Respecter les preconisations constructeur
- **Kit complet** : Toujours remplacer courroie + galets + pompe a eau ensemble
- **Marques** : Privilegier Gates, Continental, SKF
- **Huile** : Verifier absence de fuites d'huile sur la courroie
