---
category: distribution
slug: kit-de-distribution
title: Kit de distribution
pg_id: 307
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
  role: Kit complet pour la distribution a chaine avec tous les composants (tendeur, patins, glissieres)
  must_be_true:
  - synchroniser
  - entrainer
  - guider
  must_not_contain:
  - courroie
  - caoutchouc
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - courroie-de-distribution
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
    min: 100
    max: 350
    currency: EUR
    unit: kit avec pompe
    source: catalogue automecanik
  quality_tiers:
  - tier: Equipement d'origine (OE)
    description: Kit complet fourni ou homologué par le constructeur du moteur. Courroie, galets et pompe à eau issus des
      mêmes fournisseurs que la première monte.
  - tier: Equivalent OE (OES) — kit complet recommandé
    description: Fabricants reconnus en systèmes de distribution (courroies et transmissions). L'important est de choisir
      un kit de marque reconnue et de ne jamais mélanger des pièces de provenances différentes.
  - tier: Kit partiel ou composants séparés
    description: 'Remplacement de la courroie seule ou des galets seuls. Approche déconseillée : si un composant est usé,
      les autres le sont probablement aussi.'
  - tier: Kit sans pompe à eau (budget minimum)
    description: Kits qui n'incluent pas la pompe à eau. Acceptable uniquement si la pompe a été récemment remplacée avec
      documentation.
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
    label: Echeance kilometrique ou temps atteinte
    severity: confort
  - id: S2
    label: Bruit de roulement cote distribution galet
    severity: confort
  - id: S3
    label: Fuite de liquide de refroidissement pompe a eau
    severity: confort
  - id: S4
    label: Sifflement au ralenti cote courroie
    severity: confort
  - id: S5
    label: Jeu dans les galets controle visuel
    severity: confort
  - id: S6
    label: Traces d usure sur la courroie
    severity: confort
  - id: S7
    label: Grincement au demarrage a froid
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - remplacement preventif recommande
  quick_checks:
  - 'Observer : echeance kilometrique ou temps atteinte ?'
  - Bruit de roulement cote distribution galet ?
  - Fuite de liquide de refroidissement pompe a eau ?
  - 'Observer : sifflement au ralenti cote courroie ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Echeance kilometrique ou temps atteinte
  - Bruit de roulement cote distribution galet
  - Fuite de liquide de refroidissement pompe a eau
  - Sifflement au ralenti cote courroie
  - Jeu dans les galets controle visuel
  - Traces d usure sur la courroie
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '307'
  intro_title: A quoi sert Kit de distribution ?
  risk_title: Pourquoi remplacer Kit de distribution a temps ?
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
  - question: Que contient un kit de distribution ?
    answer: Courroie + galet tendeur + galet(s) enrouleur(s) + pompe à eau (selon kit). Certains kits incluent aussi les joints
      et vis.
  - question: Kit avec ou sans pompe à eau ?
    answer: Avec pompe recommandé. La pompe est entraînée par la courroie. Si elle grippe, elle peut bloquer la courroie et
      la faire casser.
  - question: Peut-on monter un kit soi-même ?
    answer: Déconseillé sans expérience. Le calage de la distribution est critique. Une dent de décalage peut endommager le
      moteur au démarrage.
  - question: Quelles sont les erreurs fréquentes à éviter ?
    answer: Acheter un kit sans pompe à eau pour économiser. Mal caler le moteur au remontage. Ne pas contrôler le jeu des
      galets avant achat.
  - question: Comment faire un diagnostic rapide ?
    answer: Kilométrage proche de l'échéance → kit complet. Bruit de roulement → galet suspect. Fuite liquide → pompe à eau.
      Les 3 → kit urgent.
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
doc_id: b202e9cc-2f8c-53a5-b3ff-7802be06373e
content_hash: sha256:417ae47e9cffe6d3
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
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  technical_notes:
    val_155_nm: '155 Nm'
    val_16_v: '16 V'
    val_160_nm: '160 Nm'
  materials:
  - materiau: 'aluminium'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    La distribution estle système mécanique qui synchronise par la courroie de
    distribution le cyclede combustion du moteur. Chaquepièce du kit de
    distribution à un rôle bien précis : - La courroie dedistribution : c'est
    une courroie crantée entraînée par la roue dentée de vilebrequin, qui àson
    tour entraîne la roue dentée d'arbre à came , la roue dentée de pompe
    àinjection (pour les moteurs diesel) et la pompe à eau (si elle est
    entraînéepar la courroie de distribution). - Le galettendeur (manuel ou
    automatique) de la courroie de distribution à pour rôled'assurer la tension
    de la courroie. - Le galet enrouleur à pour rôle d'orienteret de guider la
    courroie de distribution pour faire fonctionner les autresorganes du moteur
    (arbre à cames, pompe injection).- Pompe à eau fait circuler le liquide de
    refroidissement dans le moteur. En savoir plus : kit de distribution —
    définition et rôle mécanique 🚨 Bruit Kit de distribution : causes et
    diagnostic
  S2: >-
    Pour savoir si le kit de distribution est àremplacer : -
    Contrôlervisuellement l'état de la courroie de distribution . - Des
    dentscreusées ou usée. - Descraquelures au dos de la courroie. - Une
    usureexcessive entre les dents. - Undécollement des dents. - Unecourroie
    huilée. - Unsifflement au niveau de la courroie de distribution. - Un
    bruitde roulement au niveau des galets. Si le kit dedistribution n'est pas
    remplacé à temps et que la courroie crantée se rompe ilrisque d'avoir une
    casse moteur avec des effets irréversible avec de grave détériorationdes
    arbres à cames et du vilebrequin avec des frais de réparation élevée. C'est
    pour cela que nous vous conseillons qu'il seraplus convenable de ne pas
    dépassé les 120 000 km pour remplacer le kit dedistribution. Diagnostic
    complet : identifier une panne de kit de distribution
  S3: >-
    Le kit de distribution regroupe courroie crantée, galets tendeurs, galets
    enrouleurs et, selon les motorisations, la pompe à eau entraînée par la
    courroie. La défaillance d'un seul élément du kit peut provoquer une casse
    moteur par contact pistons-soupapes. Un choix rigoureux en amont réduit ce
    risque à zéro. - Code moteur comme référence primaire : la fiche technique
    constructeur indique le pas de courroie (pas en millimètres entre deux
    dents), la largeur et le nombre de dents. Ces trois paramètres sont liés au
    code moteur, pas uniquement au modèle du véhicule. Deux versions du même
    modèle peuvent avoir des kits incompatibles si les codes moteur diffèrent. -
    Kit avec ou sans pompe à eau : sur les motorisations où la pompe à eau est
    entraînée par la courroie de distribution (Renault, Peugeot, Volkswagen,
    Toyota — selon versions), elle doit être remplacée lors de chaque
    intervention distribution. Un kit sans pompe oblige à déposer à nouveau
    l'ensemble de la distribution pour remplacer la pompe séparément —
    doublement du coût main-d'œuvre. - Matière de la courroie — EPDM vs néoprène
    : les courroies en EPDM (éthylène propylène diène monomère) résistent mieux
    aux températures extrêmes (moteurs turbo : jusqu'à 120 °C en zone
    distribution) et aux projections d'huile. Le néoprène convient aux
    motorisations atmosphériques en usage normal. Vérifier la préconisation
    constructeur : certains moteurs exigent explicitement une courroie EPDM. -
    Galets : roulement intégré vs externe : les galets modernes intègrent un
    roulement scellé à vie, graissé à la fabrication. Vérifier que les galets du
    kit ne nécessitent pas de lubrification à l'installation (certains kits
    génériques fournissent des galets à graissage manuel, source d'erreur de
    montage). La présence d'un joint d'étanchéité côté courroie est un critère
    de qualité supplémentaire. - Respecter l'intervalle constructeur — km ET
    années : la courroie de distribution se dégrade par hydrolyse indépendamment
    du kilométrage. Un véhicule peu roulant mais âgé de 5 à 8 ans (selon
    constructeur) doit impérativement remplacer son kit même si l'intervalle
    kilométrique n'est pas atteint. Les échéances typiques s'échelonnent entre
    60 000 et 150 000 km ou 4 à 8 ans. - Contrôle du joint de vilebrequin et du
    joint de l'arbre à cames : profiter de la dépose de la distribution pour
    vérifier l'état des joints d'étanchéité d'arbre. Une fuite d'huile sur ces
    joints contamine la courroie et réduit sa durée de vie de 30 à 50 %. Les
    remplacer préventivement coûte moins que de refaire une distribution en
    urgence. - Traçabilité du kit : date de fabrication et conditionnement : les
    courroies vieillissent disponible. Vérifier la date de fabrication inscrite
    sur le conditionnement ou le flanc de courroie. Un kit stocké plus de 3 ans
    dans des conditions inadaptées (humidité, chaleur, lumière UV) peut être
    fragile même neuf à l'ouverture. Pour aller plus loin : consultez notre
    guide d'achat kit de distribution — comparatif marques, critères de choix et
    prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Kit de distribution pour
    connaître les spécifications. - Débranchez la batterie. - Levez et calez le
    véhicule. - Démontez la roue avant droite. - Démontez l'écran pare-boue
    avant droit. - Démontez les vis de fixation de la protection sousmoteur. -
    Démontez la protection sous moteur. - Repérez le cheminement de la courroie
    d'accessoires. - Démontez la courroie d'accessoires. - Démontez la poulie de
    vilebrequin. - Soutenez le moteur à l'aide d'un cric et une cale debois. -
    Démontez le support moteur et la >biellette desuspension moteur-boîte (si
    nécessaire). - Démontez les carters de la courroie de distribution . -
    Repérez le cheminement de la courroie de distribution. - Tournez le moteur à
    la main dans le sens horaire (côtédistribution), pour positionner le trou de
    l'arbre à cames quasiment en face dutrou de la culasse. - Déposez le bouchon
    de la pige du point mort haut. - Vissez la pige à fond dans le trou du point
    mort haut. - Tournez le moteur à la main dans le sens horaire
    (côtédistribution), jusqu'au blocage du moteur sur la pige. - Immobilisez la
    roue dentée d'arbre à cames avec unepige appropriée. - Vérifiez la position
    de calage du moteur. - Desserrez la fixation du galet tendeur de
    distribution. - Démontez la courroie de distribution. - Démontez le galet
    tendeur de distribution. - Démontez le galet enrouleur de distribution. -
    Démontez les fixations de la pompe à eau , suivant le niveau d'équipement. -
    Démontez la pompe à eau.
  S4_REPOSE: >-
    - Vérifier que lacourroie de distribution neuve au même nombre de dents que
    la courroie démonté. - Contrôler que lesgalets neufs sont identiques aux
    galets démontés. - Contrôler que lapompe à eau est identique à la pompe
    démontée. - Remontez lesgalets tendeurs et enrouleurs. - Remontez la pompeà
    eau. - Serrez lesfixations de la pompe à eau. - Contrôlez la position
    desrepères du galet tendeur de distribution par rapport à la culasse. -
    Contrôlez laposition des repères de la roue dentée de l'arbre à cames et de
    la roue dentéede vilebrequin. - Remettre en placela courroie de distribution
    en tenant compte de son cheminement. - Réglez la tension de la courroiede
    distribution avec le galet tendeur. - Si le galet tendeur de distribution
    estautomatique : il peut être équipé d'une bride de maintient qui facilite
    la posede la courroie. Dans le cas d'un galet tendeur automatique sans bride
    de maintient,il faut détendre le système de poussé du galet en même temps
    qu'on repositionnela courroie. - Si le galettendeur de distribution est
    manuel : en général une courroie correctement tendue doit pouvoirfaire un
    quart de tour dans son épaisseur en la prenant par le bout des doigts(entre
    l'index et le pouce). Faire le test au milieu de la portion la pluslongue
    entre deux équipements (arbre à cames ou vilebrequin ou tendeurs). -
    Tournezle galet tendeur de distribution dans le sens inverse des aiguilles
    d'une montre. - Amenez lerepère mobile à côté du repère fixe du galet
    tendeur de distribution. - Serrezl'écrou du galet tendeur de distribution. -
    Tournezsix fois le vilebrequin. - Immobilisezle volant moteur . -
    Contrôlezla position des repères de vilebrequin et de l'arbre à cames. -
    Démontez lesoutils de blocage de la roue dentée d'arbre à cames et du
    vilebrequin. - Remontez lescarters de la courroie de distribution. -
    Remontez lesupport moteur et la biellette de suspension moteur-boîte. -
    Remontez la pouliede vilebrequin. - Remontez lacourroie d'accessoires. -
    Remontez laprotection sous moteur. - Remontez lepare-boue. - Remontez la
    roue. - Descendre le véhicule. - Resserrez la roue. - Contrôler le
    bonfonctionnement de la distribution. - Vérifiez que lacourroie de
    distribution présente une tension correcte en accélérant par à coups : - Si
    la courroien'est pas assez tendue, elle n'accroche pas suffisamment aux
    poulies lors del'accélération et donc patine, créant ainsi un sifflement. -
    Si la courroie esttrop tendue, elle exerce une tension trop importante sur
    les roulements qui sefont entendre (sorte de ronflement) à la décélération.
    ✅ Après remontage, vérifiez les spécifications dans la fiche technique Kit
    de distribution.
  S5: >-
    Erreurs frequentes avec le kit de distribution : - Depasser les 120 000 km
    sans remplacement — risque de casse moteur par rupture de la courroie de
    distribution- Remplacer uniquement la courroie sans changer les galets
    tendeurs et la pompe a eau — un galet gripe ou une pompe qui fuit entraine
    la rupture de la courroie neuve- Ne pas verifier le calage de la
    distribution au remontage — un decalage meme d'une dent provoque des ratés
    moteur, perte de puissance ou casse des soupapes- Reutiliser les vis de
    fixation des galets sans verifier leur couple — risque de desserrage en
    fonctionnement- Ignorer un bruit de claquement ou de sifflement cote
    distribution — signe de galet use ou de courroie detendue- Ne pas bloquer le
    vilebrequin et l'arbre a cames avant depose — le moteur perd son calage et
    le remontage devient impossible sans outils specifiques
  S6: >-
    Le kit de distribution regroupe courroie, tendeur, galets et pompe à eau sur
    de nombreux moteurs. Après pose, une série de contrôles précis garantit que
    la distribution est correctement synchronisée et que le moteur peut être
    remis en service sans risque. - Calage de la distribution aux repères
    constructeur : vérifier l'alignement des marques sur la poulie de
    vilebrequin, le pignon d'arbre à cames et le galet tendeur. Faire tourner le
    moteur à la main de deux tours complets (720 °) et reconfirmer les repères —
    aucune déviation acceptable. - Tension de courroie mesurée : contrôler la
    tension à l'aide d'un tensiomètre si disponible ou selon la méthode
    constructeur (pression au doigt, deflexion de 10 à 15 mm au milieu du brin
    tendu). Un galet tendeur neuf doit être positionné selon le couple de
    serrage prescrit (valeur courante : 20 à 25 N·m selon moteur). - Galets et
    tendeurs tournant librement : avant pose de la courroie, vérifier à la main
    que les galets neufs tournent sans jeu axial ni résistance. Un galet dur ou
    rugueux en neuf indique un défaut de fabrication à traiter sous garantie. -
    Absence de fuite pompe à eau (si remplacée) : après démarrage et montée en
    température à 90 °C, inspecter visuellement la pompe sous tous les angles.
    Toute trace de liquide de refroidissement autour de la bride ou du joint
    d'étanchéité impose un démontage immédiat. - Sifflement ou grincement au
    démarrage à froid absent : au premier démarrage, écouter spécifiquement la
    zone distribution pendant 60 secondes. Un grincement persistant signale une
    courroie mal tendue ou un galet en contact frottant avec le carter. - Niveau
    de liquide de refroidissement vérifié : si la pompe à eau fait partie du
    kit, purger le circuit de refroidissement après remplissage et attendre que
    la température se stabilise avant de valider l'absence de bulle d'air
    (voyant température stable, chauffage fonctionnel). - Scan OBD sans code de
    calage : vérifier l'absence de codes P0016, P0017, P0340, P0345 après le
    premier cycle de chauffe. Ces codes confirment un problème de
    synchronisation nécessitant une repose immédiate.
  S7: >-
    Quel est le prix d'un kit de distribution ?Le prix varie selon le véhicule
    et la marque. Utilisez notre sélecteur pour trouver le kit de distribution
    compatible avec votre véhicule et comparer les tarifs des différents
    équipementiers.Comment savoir si mon kit de distribution est à changer ?Les
    signes d'usure les plus courants sont détaillés dans la section diagnostic
    ci-dessus. En cas de doute, faites contrôler la pièce par un
    professionnel.Peut-on rouler avec un kit de distribution défaillant ?Cela
    dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la
    sécurité du véhicule. Consultez la section symptômes pour évaluer l'urgence
    du remplacement.- synchroniser - entrainer - guider
  S8: >-
    Comment choisir Kit de distribution compatible avec mon vehicule ?Renseignez
    marque, modele, type moteur et annee, puis verifiez la reference Quand
    remplacer Kit de distribution ?En cas de echeance kilometrique ou temps
    atteinte ou de degradation mesurable, Puis-je monter Kit de distribution
    sans verification atelier ?Le montage peut exiger controles de couple,
    alignement et references.
  META: >-
    {"meta_title":"Kit de distribution : guide entretien
    complet","meta_description":"Quand changer le kit de distribution ?
    Symptômes (bruit, grincement au démarrage), intervalle préventif, critères
    de choix et erreurs à éviter."}
---

# Kit de distribution - Guide Diagnostic Complet

## Fonction et Rôle

Kit complet pour la distribution a chaine avec tous les composants (tendeur, patins, glissieres)

**Actions principales:** synchroniser, entrainer, guider

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Grincement au demarrage a froid**
  grincement au demarrage a froid

### 🟢 Autres Symptômes

- echeance kilometrique ou temps atteinte
- bruit de roulement cote distribution galet
- fuite de liquide de refroidissement pompe a eau
- sifflement au ralenti cote courroie
- jeu dans les galets controle visuel
- traces d usure sur la courroie

## Procédure de Diagnostic

Pour diagnostiquer un problème de kit de distribution:

1. **Inspection visuelle** - Examiner l'état du kit de distribution
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

- courroie-d-accessoire
- pompe-a-eau
- poulie-d-arbre-a-came
- poulie-vilebrequin

## Critères de Compatibilité

Pour commander le bon kit de distribution, vous devez connaître:

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

**Que contient un kit de distribution ?**
Courroie + galet tendeur + galet(s) enrouleur(s) + pompe à eau (selon kit). Certains kits incluent aussi les joints et vis.

**Kit avec ou sans pompe à eau ?**
Avec pompe recommandé. La pompe est entraînée par la courroie. Si elle grippe, elle peut bloquer la courroie et la faire casser.

**Peut-on monter un kit soi-même ?**
Déconseillé sans expérience. Le calage de la distribution est critique. Une dent de décalage peut endommager le moteur au démarrage.

**Quelles sont les erreurs fréquentes à éviter ?**
Acheter un kit sans pompe à eau pour économiser. Mal caler le moteur au remontage. Ne pas contrôler le jeu des galets avant achat.

**Comment faire un diagnostic rapide ?**
Kilométrage proche de l'échéance → kit complet. Bruit de roulement → galet suspect. Fuite liquide → pompe à eau. Les 3 → kit urgent.


## References supplementaires

<!-- materialized-from-db guides/choisir-courroie-distribution.md 2026-01-08 -->
### Guide - Choisir son kit distribution

# Comment choisir son kit de distribution

## Composition d'un kit complet

### Kit standard
- Courroie de distribution
- Galet tendeur
- Galet(s) enrouleur(s)

### Kit complet (recommande)
- Kit standard +
- Pompe a eau
- Courroie accessoires (option)

## Criteres de choix

### 1. Reference exacte
- **OEM** : Reference constructeur (ex: 0831V4 PSA)
- **Equivalence** : Cross-reference equipementier
- **Verification** : Nombre de dents, largeur, profil

### 2. Qualite courroie
| Materiau | Avantage | Duree vie |
|----------|----------|-----------|
| HNBR | Standard, fiable | 120 000 km |
| EPDM | Resistant chaleur | 160 000 km |
| HSN | Haute performance | 180 000 km |

### 3. Pompe a eau incluse?
- **Recommande** : Toujours remplacer avec
- **Raison** : Meme niveau d'usure, cout main d'oeuvre
- **Exception** : Pompe a eau entrainee par courroie accessoires

## Marques de reference

### Premiere monte
| Marque | Constructeurs |
|--------|---------------|
| **Gates** | PSA, Renault, VAG |
| **Contitech** | VAG, BMW, Mercedes |
| **Dayco** | Fiat, Alfa, Lancia |
| **INA** | VAG, BMW |

### Alternative qualite
| Marque | Commentaire |
|--------|-------------|
| **SKF** | Kits complets haute qualite |
| **Febi** | Bonne alternative |
| **Quinton Hazell** | Budget, garantie 2 ans |

## Intervalles par constructeur

### PSA (Peugeot/Citroen)
| Moteur | Intervalle |
|--------|------------|
| TU (1.0-1.6) | 80 000 km / 5 ans |
| DV4/DV6 HDi | 100 000 km / 10 ans |
| DW10 HDi | 120 000 km / 6 ans |
| EB PureTech | 100 000 km / 10 ans |

### Renault
| Moteur | Intervalle |
|--------|------------|
| K4M/K7M | 120 000 km / 6 ans |
| K9K dCi | 90-120 000 km selon version |
| F9Q | 120 000 km |
| M9R | 120 000 km / 6 ans |

### VAG (VW/Audi/Seat/Skoda)
| Moteur | Intervalle |
|--------|------------|
| 1.6 TDI CAYC | 120 000 km / 5 ans |
| 2.0 TDI CR | 120 000 km / 5 ans |
| TSI | Chaine (pas d'entretien) |

## Signes de remplacement urgent

### Visuels
- Craquelures sur courroie
- Usure laterale (desalignement)
- Traces de poudre noire

### Sonores
- Couinement au demarrage
- Claquement periodique
- Bruit de galet

### Preventif
- Kilometrage atteint
- Age depasse (meme faible km)
- Apres fuite pompe a eau/joint SPI

## Conseils pratiques

1. **Ne jamais depasser l'intervalle** : Casse = moteur HS
2. **Kit complet** : Economise la main d'oeuvre future
3. **Pompe a eau** : Inclure systematiquement
4. **Courroie accessoires** : Profiter de l'intervention
5. **Liquide refroidissement** : Vidanger lors du remplacement
6. **Carnet entretien** : Tamponner avec date et km

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
