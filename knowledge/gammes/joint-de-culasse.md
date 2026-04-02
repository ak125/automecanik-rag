---
category: moteur
slug: joint-de-culasse
title: Joint de culasse
pg_id: 318
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
  role: Assurer l'etancheite entre le bloc moteur et la culasse, maintenir la pression de compression
  must_be_true:
  - assurer l'etancheite
  - empecher les fuites
  - separer les fluides
  must_not_contain:
  - boite de vitesses
  - electronique
  - reparation
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - assurer l'etancheite
  - empecher les fuites
  - separer les fluides
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
    min: 50
    max: 200
    currency: EUR
    unit: joint
    source: catalogue automecanik
  quality_tiers:
  - tier: Equipement d'origine (OE)
    description: Joint fourni ou agréé par le constructeur du moteur. Pour les moteurs modernes, il s'agit souvent d'un joint
      multicouches acier (MLS) avec revêtement précis. La référence exacte est indispensable.
  - tier: Equivalent OE (OES) — recommandé
    description: Fabricants reconnus en joints de culasse. Le corpus RAG cite Elring, Victor Reinz et Goetze comme références
      fiables pour cette gamme.
  - tier: Non recommandé pour ce type de pièce
    description: Un joint de culasse de qualité inconnue expose au risque de casse moteur. La pièce doit toujours être OE
      ou OES reconnu.
  brands:
    premium:
    - Elring
    - Victor Reinz
    standard:
    - Febi
    - Ajusa
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Mayonnaise sous le bouchon d huile ou de ldr
    severity: confort
  - id: S2
    label: Fumee blanche epaisse a l echappement
    severity: confort
  - id: S3
    label: Bulles d air dans le vase d expansion
    severity: confort
  - id: S4
    label: Surchauffe repetee du moteur
    severity: confort
  - id: S5
    label: Niveau de ldr qui baisse sans fuite visible
    severity: confort
  - id: S6
    label: Huile dans le liquide de refroidissement
    severity: confort
  causes:
  - identifier origine fuite et verifier joints
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  - 'Usure ou defaillance causant : mayonnaise sous le bouchon d huile ou de ldr'
  quick_checks:
  - 'Observer : mayonnaise sous le bouchon d huile ou de ldr ?'
  - 'Observer : fumee blanche epaisse a l echappement ?'
  - 'Observer : bulles d air dans le vase d expansion ?'
  - 'Observer : surchauffe repetee du moteur ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Mayonnaise sous le bouchon d huile ou de ldr
  - Fumee blanche epaisse a l echappement
  - Bulles d air dans le vase d expansion
  - Surchauffe repetee du moteur
  - Niveau de ldr qui baisse sans fuite visible
  - Huile dans le liquide de refroidissement
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '318'
  intro_title: A quoi sert Joint de culasse ?
  risk_title: Pourquoi remplacer Joint de culasse a temps ?
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
  - question: Joint de culasse OE ou adaptable ?
    answer: Privilégiez TOUJOURS l'OE ou OES (Elring, Victor Reinz, Goetze). Un joint de culasse de mauvaise qualité = casse
      moteur garantie.
  - question: Comment savoir si le joint de culasse est HS ?
    answer: Mayonnaise sous le bouchon d'huile, fumée blanche à l'échappement, bulles dans le vase d'expansion, surchauffe
      répétée.
  - question: Tous les combien changer le joint de culasse ?
    answer: Pas de périodicité. Le joint de culasse dure normalement toute la vie du moteur sauf surchauffe ou défaut de fabrication.
  - question: Peut-on changer le joint de culasse soi-même ?
    answer: Déconseillé sans expérience. Nécessite dépose culasse, contrôle planéité, calage distribution. Erreur = destruction
      moteur.
  - question: Quelle erreur éviter avec le joint de culasse ?
    answer: Ne JAMAIS réutiliser les vis de culasse. Respecter scrupuleusement l'ordre et les passes de serrage. Faire contrôler
      la culasse.
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
doc_id: d5d0d5fa-28db-5cd1-8376-f2285ad1dff4
content_hash: sha256:592e2adb5c8e69d9
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
  _source: gpa26.com + hella.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 5
  _has_tech_data: true
  technical_notes:
    val_23_a: '23 a'
    val_3_bars: '3 bars'
    val_360_v: '360 V'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Comme son nom l'indique un joint de culasse va faire lajointure entre la
    culasse et le bloc-moteur. Le moteur fonctionne grâce à des explosions quise
    produisent dans la chambre de combustion dans ce cas la chambre doitêtre
    bien étanche pour que les gaz chauds issus de l'explosion n'endommagentpas
    le moteur, c'est ici ou on constate l'utilité d'un joint de culasse, qui
    vagarantir l'étanchéité à l'intérieur de la chambre de combustion qui va
    éviterun mélange du liquide de refroidissement et de l'huile moteur. Un
    joint de culasse doit résister àd'importantes contraintes thermiques,
    mécaniques et chimiques. En savoir plus : joint de culasse — définition et
    rôle mécanique 🚨 Bruit Joint de culasse : causes et diagnostic
  S2: >-
    Un joint deculasse n'a pas de période de remplacement mais il est à
    contrôler si vousconstatez un des signes de défaillance suivant : - Fumée
    blanche qui s'échappede l'échappement. - Surchauffe du moteur. - Une baisse
    du niveau duliquide de refroidissement dans le vase d'expansion . - Une
    baisse du niveau d'huile moteur. - Lors de l'ouverture du bouchon du vase
    d'expansion vous remarquez que sa surface est huileuse (ça ressemble à
    lamayonnaise), cela signifie que le liquide de refroidissement estmélangé
    avec l'huile du moteur ce qui est très grave. Un joint de culasse défectueux
    et qu'il n'est pas remplacépeut amener à une révisioncomplète du moteur.Lors
    du changement du joint de culasse il fautobligatoirement vidanger le liquide
    de refroidissement, l'huile du moteur etremplacer le filtre à huile .
    Diagnostic complet : identifier une panne de joint de culasse
  S3: >-
    Le joint de culasse est la pièce d'étanchéité la plus sollicitée du moteur :
    positionné entre le bloc moteur et la culasse, il sépare simultanément les
    chambres de combustion, les galeries d'huile et les galeries de liquide de
    refroidissement. Une défaillance expose immédiatement le moteur à une
    contamination croisée (huile dans le liquide de refroidissement, eau dans
    l'huile) et à une surchauffe rapide pouvant déformer la culasse. Le choix du
    joint de culasse correct est donc une décision technique qui n'autorise
    aucun compromis. - Type de joint : MLS, cuivre ou composite — Les moteurs
    modernes (post-2000) utilisent presque exclusivement des joints MLS (Multi-
    Layer Steel) en acier inoxydable multicouches avec revêtement élastomère.
    Les anciens moteurs peuvent recevoir des joints en cuivre recuit ou en
    composite amiante-libre (graphite/métal). Utiliser impérativement le type
    prescrit par le constructeur. - Épaisseur nominale et cotes de dépassement
    piston — Les joints de culasse existent en plusieurs épaisseurs (par exemple
    1,20 mm, 1,40 mm, 1,60 mm selon le dépassement des pistons au point mort
    haut). L'épaisseur correcte se détermine en mesurant le dépassement des
    pistons avec un comparateur. Monter un joint trop fin augmente le taux de
    compression au-delà des limites, monter un joint trop épais provoque une
    sous-compression. - Nombre de perçages de compression — Sur les joints MLS,
    chaque chambre de combustion possède une ou plusieurs rangées d'agrafes de
    compression (« stoppers »). Ces agrafes définissent l'épaisseur comprimée
    finale. Vérifier que le joint commandé comporte le même nombre de perçages
    et les mêmes agrafes que l'original. - État de la surface de la culasse —
    Avant de commander le joint, faire rectifier ou au minimum contrôler la
    planéité de la culasse (voile toléré : 0,03 à 0,05 mm selon le
    constructeur). Un joint neuf sur une culasse voilée percera de nouveau dans
    les 10 000 km. - Kit avec vis de culasse neuves — Les vis de culasse à
    serrage angulaire (TTY — Torque-To-Yield) ne peuvent JAMAIS être réutilisées
    après desserrage : elles s'allongent plastiquement lors du serrage et
    perdent leur élasticité. Toujours prévoir un jeu de vis neuves. Certains
    kits (Elring, Payen) les incluent. - Pièces à remplacer simultanément — Lors
    d'un remplacement de joint de culasse, remplacer systématiquement : joint de
    cache-culbuteurs, joints de vis de culasse, joints de soupapes si l'âge du
    moteur le justifie. Ces pièces sont démontées lors de l'intervention et leur
    réutilisation présente un risque de fuite résiduelle. - Code moteur
    obligatoire — Le joint de culasse est la pièce pour laquelle le code moteur
    (P.5 carte grise ou gravé sur le bloc) est le plus déterminant. Deux
    variantes du même moteur peuvent avoir des hauteurs de chambre et des
    dépassements de piston différents, imposant des épaisseurs de joint
    distinctes. Pour aller plus loin : consultez notre guide d'achat joint de
    culasse — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Joint de culasse pour
    connaître les spécifications. Note : avant deprocéder au démontage il faut
    consultez la revue technique spécifique à votrevéhicule. - Débranchez la
    batterie. - Levez le véhicule. - Vidangez l'huile du moteur. - Vider le
    liquide de refroidissement du moteur. - Redescendre le véhicule. - Soutenir
    le moteur à l'aide d'un cric d'atelier. - Démontez le cache moteur. -
    Démontez le boîtier du filtre à air si nécessaire. - Démontez les durites du
    liquide de refroidissement du moteur. - Débranchez tous les connecteurs et
    les capteurs du moteur. - Démontez les canalisations de l'alimentation en
    carburant. - Démontez le collecteur d'échappement . - Démontez le support
    moteur avant droit. - Démontez la courroie de distribution . - Démontez le
    couve-culasse. - Repérez la position des vis de culasse avant de les
    démontés. - Démontez les vis de la culasse. - Démontez la culasse. -
    Démontez le joint de culasse.
  S4_REPOSE: >-
    Le remontage d'un joint de culasse est l'opération moteur la plus exigeante
    en matière de rigueur. Chaque étape conditionne la durabilité de
    l'intervention : un défaut de serrage ou de planéité détruit le joint neuf
    dès les premières heures de fonctionnement. Les vis de culasse usagées ne se
    réutilisent jamais — c'est une règle absolue. - Avant toute repose, faites
    contrôler la planéité de la culasse par un rectifieur moteur à l'aide d'une
    règle rectifiée et de cales. Une déformation supérieure à 0,05 mm impose un
    surfaçage. Un surfaçage modifie le taux de compression : certains
    constructeurs imposent alors un joint de culasse plus épais (cotes A, B, C).
    - Sélectionnez le joint de culasse de l'épaisseur correcte (marquages
    encoches sur le bord du joint) en fonction des cotes de dépassement des
    pistons si votre moteur l'exige. Vérifiez la correspondance dans la revue
    technique avant de desceller l'emballage. - Posez le joint de culasse neuf
    sur le bloc moteur propre et sec, en orientant le marquage "OBEN/TOP/HAUT"
    vers le haut. Tout contact avec de l'huile ou de la graisse avant le serrage
    compromet l'étanchéité initiale. - Présentez la culasse verticalement et
    descendez-la sur les goujons de centrage en un seul mouvement, sans la faire
    glisser sur le joint. Un glissement décale le joint et déchire son
    revêtement. - Installez obligatoirement des vis de culasse neuves. Les vis à
    serrage angulaire (torx ou 12 pans) se déforment plastiquement lors du
    premier serrage et ne peuvent pas être réutilisées sans risque de rupture
    sous couple. - Serrez les vis de culasse selon la procédure en plusieurs
    passes prescrite par la revue technique : typiquement une pré-charge à 20
    N·m, puis une deuxième passe à 40-60 N·m, puis un ou deux serrages
    angulaires successifs (par exemple 90° + 90°). Ne substituez jamais un
    serrage angulaire par un couple en N·m. - Remontez le couvre-culasse avec un
    joint neuf si le précédent présentait un suintement, en serrant les vis au
    couple de 8-10 N·m en croix depuis le centre. - Remontez la courroie ou la
    chaîne de distribution en respectant scrupuleusement les repères de calage
    sur l'arbre à cames, le vilebrequin et la pompe à injection (diesel). Un
    décalage d'une dent détruit le moteur au démarrage sur les moteurs
    interférents. - Remplissez le circuit de refroidissement avec le liquide
    préconisé (OAT, HOAT ou IAT selon le constructeur), puis effectuez la mise à
    l'air (purge d'air) via les vis de purge en amenant le moteur
    progressivement en température. Surveillez en permanence le niveau dans le
    vase d'expansion. - Démarrez le moteur et laissez-le atteindre la
    température de fonctionnement normale (85-90°C). Contrôlez l'absence de
    fumée blanche à l'échappement, l'absence de bulles dans le vase d'expansion
    et la stabilité du niveau de liquide de refroidissement. Après
    refroidissement complet, vérifiez le niveau d'huile : une contamination
    huile/eau indique une fuite résiduelle. ✅ Après remontage, vérifiez les
    spécifications dans la fiche technique Joint de culasse.
  S5: >-
    Erreurs frequentes avec le joint de culasse : - Ne pas verifier la planeite
    de la culasse avant remontage — une culasse voilee ne porte pas uniformement
    sur le joint et la fuite revient rapidement- Reutiliser les vis de culasse —
    ces vis sont a usage unique (etirement controle), les reutiliser provoque un
    serrage inegal et des fuites- Ne pas respecter l'ordre et les passes de
    serrage — les vis de culasse se serrent en spirale du centre vers
    l'exterieur, en 3 a 4 passes + angle selon constructeur- Confondre
    surchauffe et joint de culasse — faire un test de CO2 dans le vase
    d'expansion avant de se lancer dans un remplacement couteux- Ne pas purger
    correctement le circuit de refroidissement apres remontage — des bulles
    d'air provoquent des points chauds et un nouveau joint claque- Ignorer la
    cause de la casse (surchauffe, calaminage) — si la cause n'est pas traitee,
    le nouveau joint casse a nouveau
  S6: >-
    Le remplacement d'un joint de culasse est l'une des interventions moteur les
    plus exigeantes. Le joint doit assurer simultanément l'étanchéité aux gaz de
    combustion, à l'huile moteur et au liquide de refroidissement. Les contrôles
    post-remplacement sont rigoureux et s'étalent sur plusieurs jours et
    plusieurs centaines de kilomètres. - Vérification du couple et de la
    séquence de serrage des vis de culasse : les vis de culasse doivent
    impérativement être serrées en respectant l'ordre en croix prescrit par le
    constructeur, en plusieurs passes. Pour la majorité des moteurs modernes, la
    séquence est : pré-serrage à 20-30 N·m, puis angulaire de 90° deux fois (ou
    valeurs spécifiques constructeur). Un serrage incorrect provoque une fuite
    immédiate. - Contrôle du liquide de refroidissement avant démarrage :
    remplir le circuit de refroidissement avec le liquide préconisé (GLSF-48,
    OAT ou HOAT selon constructeur) mélangé à 50 % d'eau déminéralisée. Purger
    l'air du circuit en ouvrant les purgeurs si présents. Un circuit non purgé
    provoque une surchauffe même avec un joint neuf. - Premier démarrage —
    surveillance de la température : démarrer le moteur et surveiller en continu
    la température du liquide de refroidissement. La montée en température doit
    être progressive et s'arrêter à environ 90 °C. Tout dépassement de 100 °C ou
    toute montée rapide sans stabilisation indique un problème d'étanchéité
    résiduel. - Contrôle de l'absence de bulles dans le vase d'expansion :
    moteur à température, observer le vase d'expansion ouvert. L'absence totale
    de bulles d'air confirme que le joint est étanche aux gaz de combustion. Des
    bulles persistantes signalent une fuite de gaz côté circuit de
    refroidissement (symptôme RAG critique). - Contrôle de l'huile moteur :
    après 15 minutes de fonctionnement, vérifier la couleur de l'huile sur la
    jauge et sous le bouchon de remplissage. Aucune émulsion (aspect crémeux ou
    brun-blanc, dit "mayonnaise") ne doit être visible. Une émulsion indique que
    le liquide de refroidissement contamine toujours l'huile. - Contrôle de la
    fumée blanche à l'échappement : observer l'échappement pendant 5 minutes à
    chaud. Une légère fumée blanche est normale à froid. Une fumée blanche
    épaisse et persistante à chaud signale que le liquide de refroidissement est
    toujours aspiré dans la chambre de combustion. - Contrôle du niveau de
    liquide de refroidissement sur 500 km : vérifier le niveau du vase
    d'expansion toutes les 100 km pendant les 500 premiers kilomètres. Le niveau
    ne doit pas baisser. Une baisse régulière sans fuite visible extérieure
    (symptôme RAG confirmé) indique une fuite interne résiduelle vers la chambre
    ou vers l'huile.
  S7: >-
    Quel est le prix d'un joint de culasse ?Le prix varie selon le véhicule et
    la marque. Utilisez notre sélecteur pour trouver le joint de culasse
    compatible avec votre véhicule et comparer les tarifs des différents
    équipementiers.Comment savoir si mon joint de culasse est à changer ?Les
    signes d'usure les plus courants sont détaillés dans la section diagnostic
    ci-dessus. En cas de doute, faites contrôler la pièce par un
    professionnel.Peut-on rouler avec un joint de culasse défaillant ?Cela
    dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la
    sécurité du véhicule. Consultez la section symptômes pour évaluer l'urgence
    du remplacement.- assurer l'etancheite - empecher les fuites - separer les
    fluides
  S8: >-
    Comment choisir Joint de culasse compatible avec mon vehicule ?Renseignez
    marque, modele, type moteur et annee, puis verifiez la reference Quand
    remplacer Joint de culasse ?En cas de mayonnaise sous le bouchon d huile ou
    de ldr ou de degradation Puis-je monter Joint de culasse sans verification
    atelier ?Le montage peut exiger controles de couple, alignement et
    references.
  META: >-
    {"meta_title":"Joint de culasse : symptômes et
    remplacement","meta_description":"Fumée blanche, mayonnaise sous le bouchon
    d'huile, surchauffe : quand changer le joint de culasse ? Causes, signes de
    claquage et guide de remplacement complet."}
---

# Joint de culasse - Guide Diagnostic Complet

## Fonction et Rôle

Assurer l'etancheite entre le bloc moteur et la culasse, maintenir la pression de compression

**Actions principales:** assurer l'etancheite, empecher les fuites, separer les fluides

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- mayonnaise sous le bouchon d huile ou de ldr
- fumee blanche epaisse a l echappement
- bulles d air dans le vase d expansion
- surchauffe repetee du moteur
- niveau de ldr qui baisse sans fuite visible
- huile dans le liquide de refroidissement

## Procédure de Diagnostic

Pour diagnostiquer un problème de joint de culasse:

1. **Inspection visuelle** - Examiner l'état du joint de culasse
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bagues-d-etancheite-moteur
- filtre-a-huile
- joint-de-cache-culbuteurs
- joint-de-collecteur
- vis-de-culasse

## Critères de Compatibilité

Pour commander le bon joint de culasse, vous devez connaître:

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

**Joint de culasse OE ou adaptable ?**
Privilégiez TOUJOURS l'OE ou OES (Elring, Victor Reinz, Goetze). Un joint de culasse de mauvaise qualité = casse moteur garantie.

**Comment savoir si le joint de culasse est HS ?**
Mayonnaise sous le bouchon d'huile, fumée blanche à l'échappement, bulles dans le vase d'expansion, surchauffe répétée.

**Tous les combien changer le joint de culasse ?**
Pas de périodicité. Le joint de culasse dure normalement toute la vie du moteur sauf surchauffe ou défaut de fabrication.

**Peut-on changer le joint de culasse soi-même ?**
Déconseillé sans expérience. Nécessite dépose culasse, contrôle planéité, calage distribution. Erreur = destruction moteur.

**Quelle erreur éviter avec le joint de culasse ?**
Ne JAMAIS réutiliser les vis de culasse. Respecter scrupuleusement l'ordre et les passes de serrage. Faire contrôler la culasse.
