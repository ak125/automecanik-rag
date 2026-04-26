---
category: echappement
slug: fap
title: FAP
pg_id: 1256
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
  role: Filtre et retient les particules fines des gaz d'échappement diesel
  must_be_true:
  - filtrer
  - retenir
  - regenerer
  must_not_contain:
  - catalyseur
  - pot catalytique
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - catalyseur
  - silencieux
  - sonde-lambda
  - vanne-egr
  - tube-d-echappement
  - collecteur-d-echappement
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
  - ❌ "passe le controle technique"
  cost_range:
    min: 150
    max: 800
    currency: EUR
    unit: l'unite
    source: estimation categorie
  quality_tiers:
  - tier: Pièce OE (Origine Équipement)
    description: FAP identique à l origine. Homologation moteur et normes anti-pollution conformes. Capteur de pression différentielle
      compatible.
  - tier: Équivalent OE (spécialistes échappement)
    description: Fabricants d échappement et de filtration reconnus fournissant les constructeurs. Qualité proche de l OE.
  - tier: FAP régénéré / décalaminé
    description: Nettoyage chimique ou thermique du FAP d origine. Efficace si le filtre n est pas trop colmaté ou endommagé.
      Option économique (150 à 300 EUR) avant de passer au remplacement.
  - tier: FAP générique non homologué
    description: Non recommandé. Un FAP non homologué peut affecter la régénération et le comportement du moteur. Risque de
      non-conformité au contrôle technique.
  brands:
    premium:
    - Walker
    - Bosal
    standard:
    - Valeo
    - Febi
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Voyant filtre particules allume tableau
    severity: confort
  - id: S2
    label: Perte de puissance importante mode degrade
    severity: confort
  - id: S3
    label: Regenerations frequentes odeur de brule
    severity: confort
  - id: S4
    label: Fumee noire excessive a l acceleration
    severity: confort
  - id: S5
    label: Surconsommation de carburant anormale
    severity: confort
  - id: S6
    label: Plus de 150 000 km en conduite urbaine
    severity: confort
  causes:
  - lecture codes defaut obd et diagnostic electronique
  - remplacement preventif recommande
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  - 'kilometrage eleve ou usure visible : remplacement preventif recommande'
  quick_checks:
  - Voyant filtre particules allume tableau ?
  - 'Observer : perte de puissance importante mode degrade ?'
  - 'Observer : regenerations frequentes odeur de brule ?'
  - 'Observer : fumee noire excessive a l acceleration ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Voyant filtre particules allume tableau
  - Perte de puissance importante mode degrade
  - Regenerations frequentes odeur de brule
  - Fumee noire excessive a l acceleration
  - Surconsommation de carburant anormale
  - Plus de 150 000 km en conduite urbaine
  good_practices:
  - Controle visuel sous le vehicule a chaque revision
  - Verifier les fixations et silent-blocs de suspension d echappement
  - Remplacement si perforation, rouille traversante ou bruit anormal
  - Ne pas conduire avec un echappement defectueux (gaz toxiques)
rendering:
  pgId: '1256'
  intro_title: A quoi sert FAP ?
  risk_title: Pourquoi remplacer FAP a temps ?
  risk_explanation: '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
  risk_consequences:
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
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
  - question: 'FAP OE ou OES : que choisir ?'
    answer: Les FAP OES (Bosal, Walker) sont de qualité équivalente à l'OE. Vérifiez l'homologation et la compatibilité exacte
      avec votre moteur (numéro de pièce).
  - question: Comment savoir si mon FAP est colmaté ?
    answer: Voyant FAP allumé, mode dégradé (perte de puissance), régénérations fréquentes, fumée noire, code défaut P2002
      ou P2463.
  - question: Tous les combien changer le FAP ?
    answer: Entre 150 000 et 250 000 km selon utilisation. Trajets longs = longue durée de vie. Trajets courts = colmatage
      rapide.
  - question: Peut-on nettoyer le FAP au lieu de le changer ?
    answer: Oui, le décalaminage (nettoyage chimique ou thermique) peut prolonger sa vie si pas trop colmaté. Efficace à 70-80%
      pour 150-300€.
  - question: Quelle erreur éviter avec le FAP ?
    answer: Ne jamais supprimer le FAP (illégal, amende 7500€). Éviter les trajets courts répétés. Ne pas couper le moteur
      pendant une régénération.
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
doc_id: 00b5f905-3b43-5fe3-9779-5554e31b0357
content_hash: sha256:f178e2deea3a2855
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
  area: Sous le vehicule, du collecteur moteur au silencieux arriere
  access: Par le dessous (pont elevateur)
  adjacent_parts:
  - collecteur
  - catalyseur
  - tubes
  - silencieux
installation:
  difficulty: moyen
  time: 1h a 2h
  tools:
  - cle a douille
  - degripant
  - chandelles
  prerequisite: Pont elevateur, fixations souvent grippees par la rouille
phase5_enrichment:
  _source: delphiautoparts.com + fr.wikipedia.org + hella.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 6
  _has_tech_data: true
  types_variants:
  - type: 'polyv'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_0_ohm: '0 ohm'
    val_000_km: '000 km'
    val_15_a: '15 a'
    val_15_ohms: '15 ohms'
    val_20_a: '20 a'
    val_25_a: '25 a'
    val_27_a: '27 a'
    val_5_5_litres: '5,5 litres'
    val_9_a: '9 A'
    val_908_v: '908 V'
    val_908_a: '908 a'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    L'accumulation de cendres dans le FAP, associée à lamultiplication de
    parcours urbains, vont conduire à la saturation du FAP. Lorsquele FAP est
    plein, le calculateur va déclencher une action de combustion quipermet de
    régénérer le filtre. Un FAP fonctionne selon 2 cycles, le premier consiste
    en lacollecte de particules et le second est leur élimination. - 1er cycle
    (Filtration) : Le filtre capture lesparticules en suspension dans les gaz
    d'échappement. Cela conduit à laformation d'une couche de suie sur les
    parois du filtre. A terme, cette coucheprovoque une diminution des
    performances du moteur. Il est donc nécessaire denettoyer régulièrement le
    FAP. C'est à ce moment qu'intervient le cycle derégénération. - 2eme cycle
    (régénération) : Le nettoyage du FAPs'effectue sous la forme de cycles
    automatiques durant lesquels la températuredes gaz d'échappements va être
    fortement augmentée afin de brûler le dépôt desuie. Pour augmenter la
    température, du gasoil non brûlé est injectée dans uncatalyseur intégré au
    FAP. Ce carburant va s'enflammer et ainsi faire augmenterla température dans
    la pièce, provoquant la combustion des suies piégées dansle filtre. En
    savoir plus : fap — définition et rôle mécanique 🚨 Bruit FAP : causes et
    diagnostic
  S2: >-
    Un FAP défectueux présente plusieurs symptômes : - Manque de puissance dans
    levéhicule. - Témoin du filtre àparticule s'allume si équipé. - Témoin de
    gestion moteurs'allume mais il faut faire un test diagnostic. Le
    dysfonctionnement du FAP peut avoir desconséquences irrémédiables sur
    certains organes périphériques comme le turbo,le catalyseur, la ligne
    d'échappement... Diagnostic complet : identifier une panne de fap
  S3: >-
    Le filtre à particules (FAP ou DPF — Diesel Particulate Filter) est un
    composant exclusif aux moteurs diesel qui retient les suies et particules
    fines (PM2.5 et PM10) avant leur rejet à l'atmosphère. Un FAP colmaté
    déclenche le mode dégradé (puissance réduite à 60-70 %), puis une
    régénération forcée qui, si elle échoue, conduit au remplacement. Compte
    tenu du coût élevé du composant (600 à 2 500 EUR selon le véhicule), la
    sélection doit être rigoureuse. Voici les critères à vérifier. - Référence
    constructeur et code moteur diesel obligatoires — Le FAP est homologué pour
    une motorisation spécifique : cylindrée, norme Euro (Euro 4, Euro 5, Euro
    6), et parfois version de calibration calculateur. Un FAP Euro 5 monté sur
    un véhicule Euro 6 peut générer des codes défaut de contre-pression et
    empêcher les régénérations. Renseignez le code moteur précis (ex. : 2.0 TDI
    CUNA, 1.6 BlueHDi BHZ) avant toute commande. - Présence ou absence d'additif
    de régénération (Eolys/FAP+) — Certains systèmes FAP (Peugeot, Citroën,
    Volvo avec système SiC) utilisent un additif cérine (Eolys) injecté dans le
    carburant pour abaisser la température de régénération. Ces FAP (en carbure
    de silicium SiC) ne sont pas interchangeables avec les FAP sans additif (en
    cordiérite). Vérifiez si votre véhicule dispose d'un réservoir d'additif
    Eolys distinct avant de choisir le type de substrat. - Substrat : cordiérite
    ou carbure de silicium (SiC) — Le substrat cordiérite (moins cher,
    légèrement moins performant thermiquement) convient aux véhicules sans
    additif dont la régénération est assurée uniquement par montée en
    température. Le substrat SiC résiste à des températures de régénération de
    600 à 650°C et s'impose sur les véhicules à forte sollicitation (longues
    distances, motorisations puissantes). - Cellules par pouce carré (cpsi) :
    densité de filtration — La densité de cellules (généralement 200 à 300 cpsi
    pour les FAP automobiles) détermine la surface filtrante et la contre-
    pression en fonctionnement. Un FAP de densité inférieure à l'origine génère
    moins de contre-pression mais filtre moins efficacement, ce qui peut
    entraîner un refus au contrôle technique sur les mesures d'opacité. -
    Capteurs associés : sonde de pression différentielle et sondes de
    température — Le calculateur moteur mesure le colmatage du FAP par la
    différence de pression entre l'entrée et la sortie du filtre (capteur de
    pression différentielle). Lors du remplacement, vérifiez que les orifices de
    connexion de ce capteur sont positionnés aux mêmes emplacements sur la pièce
    de remplacement, sous peine de mesures erronées et de régénérations
    anarchiques. - Régénération active ou passive : impact sur le choix — Un FAP
    de remplacement doit être compatible avec le mode de régénération de votre
    véhicule. La régénération passive se produit naturellement en roulage
    autoroutier au-dessus de 60-70 km/h. La régénération active est déclenchée
    par le calculateur via une post-injection de gazole. Si votre usage est
    principalement urbain (courts trajets), choisissez un FAP adapté à ce profil
    d'usage ou envisagez une consultation pour réinitialisation du compteur de
    suies après remplacement. - Durée de vie et garantie constructeur — Un FAP
    neuf de qualité OEM ou équivalent doit présenter une durée de vie de 150 000
    à 200 000 km en conduite mixte. Évitez les offres sans mention de durée de
    vie garantie. La mention "passe le contrôle technique" n'est pas une
    garantie technique : elle ne dit rien sur la durée de vie du substrat ni sur
    la compatibilité avec votre système de régénération. Pour aller plus loin :
    consultez notre guide d'achat fap — comparatif marques, critères de choix et
    prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique FAP pour connaître les
    spécifications. - Débranchez la batterie. - Démontez les vis de fixation
    supérieure etcentrale de l'écran thermique. - Démonter le tuyau de prise de
    pressionavant. - Levez et calez le véhicule. - Démontez la protection sous
    moteur. - Démontez les vis de fixation inférieuresde l'écran thermique. -
    Démontez le tuyau de prise de pressionarrière. - Démontez le collier
    d'échappement. - Démontez l'écran thermique. - Démontez le collier de
    serrage del'ensemble catalyseur/FAP. - Démontez le FAP.
  S4_REPOSE: >-
    Le remontage du FAP exige de soigner les joints de bride et l'écran
    thermique : un joint de FAP qui fuit laisse passer des gaz chauds, ce qui
    peut déclencher un incendie dans l'habitacle du soubassement. Changez
    systématiquement les joints et les colliers de serrage, même si les anciens
    semblent en bon état. - Vérifiez que le FAP neuf est identique à celui
    déposé : référence constructeur, position des capteurs de pression
    différentielle, orientation du corps sur la ligne d'échappement. - Contrôlez
    l'état du tube d'échappement amont et aval : vérifiez l'absence de corrosion
    perforante sur les tronçons adjacents. Contrôlez aussi le capteur de
    pression différentielle (sonde amont/aval) et ses tubes de prise de
    pression. - Posez des joints de bride neufs sur les emboîtements amont et
    aval. N'utilisez jamais de pâte d'étanchéité haute température en
    remplacement d'un joint métallique ou fibré prévu d'origine. - Mettez en
    place le FAP sur la ligne d'échappement en engageant d'abord le côté amont,
    puis en alignant le flanc aval. - Remontez et serrez le collier de serrage
    catalyseur/FAP au couple préconisé. Serrez en alternant les vis opposées
    pour répartir la pression uniformément sur le joint. - Remontez l'écran
    thermique et serrez ses vis de fixation supérieure et centrale, puis
    inférieures. L'écran protège les composants voisins des températures de
    régénération (600 à 900 °C). - Reconnectez le tube de prise de pression
    avant sur le capteur de pression différentielle, puis le tube arrière.
    Vérifiez que les clips de fixation des tubes sont clipsés. - Remontez la
    protection sous moteur, puis descendez le véhicule. Rebranchez la batterie
    (borne positive en premier). - Démarrez le moteur et effectuez une lecture
    avec un outil de diagnostic OBD pour effacer les codes défaut résiduels
    (P2002, P2463) et vérifier l'absence de nouveaux codes d'échappement. -
    Effectuez un trajet routier d'au moins 20 km à allure soutenue (voie rapide
    ou nationale) pour permettre une première régénération passive et confirmer
    le bon fonctionnement du FAP. ✅ Après remontage, vérifiez les spécifications
    dans la fiche technique FAP.
  S5: >-
    Erreurs frequentes avec le filtre a particules (FAP) : - Rouler
    exclusivement en ville sur de courts trajets — le FAP a besoin de phases de
    regeneration a haute temperature (autoroute) pour bruler les suies
    accumulees- Ignorer le voyant FAP allume — la regeneration active est en
    cours ou le FAP est sature. Rouler 20 min a 3000 tr/min sur voie rapide peut
    suffire, sinon intervention garage- Supprimer ou debrider le FAP — c'est
    illegal et provoque un echec au controle technique (sonde de particules
    depuis 2019)- Utiliser une huile moteur non compatible FAP — les huiles non
    "low SAPS" contiennent des cendres metalliques qui colmatent definitivement
    le FAP- Confondre FAP bouche et FAP casse — un diagnostic pression
    differentielle est necessaire avant remplacement pour confirmer le
    colmatage- Ne pas verifier l'etat de l'additif cerine (si equipe) — sur les
    vehicules PSA avec additif, le reservoir de cerine vide empeche la
    regeneration
  S6: >-
    Le remplacement d'un filtre à particules diesel (FAP) exige des
    vérifications précises après la pose : le calculateur moteur doit
    reconnaître le nouveau filtre et la première régénération doit pouvoir
    s'effectuer dans les conditions thermiques correctes.- Effacement des codes
    défaut OBD — Connectez un outil de diagnostic et effacez les codes P2002,
    P2003 ou P244x liés au FAP. Sans effacement, le voyant reste allumé même
    avec un filtre neuf et le moteur peut rester bloqué en mode dégradé.-
    Extinction définitive du voyant FAP au tableau de bord — Après effacement et
    redémarrage, le voyant filtre à particules doit s'éteindre. S'il se rallume
    dans les premiers kilomètres, contrôlez l'étanchéité des joints et des
    brides de raccordement.- Pression différentielle FAP proche de 0 mbar à
    froid — Le capteur de pression différentielle amont/aval doit afficher une
    valeur proche de 0 mbar sur un filtre propre et froid. Une valeur déjà
    élevée à la pose indique une mauvaise étanchéité ou un problème de montage.-
    Premier trajet de régénération passive — Effectuez un trajet d'au moins 20
    km à vitesse soutenue (80-110 km/h) pour initier la première régénération
    passive. La température des gaz en aval du FAP doit atteindre 550 à 600°C
    lors de cette phase.- Disparition des fumées noires à l'accélération — Les
    fumées noires caractéristiques du FAP saturé doivent disparaître
    immédiatement après le remplacement. Des fumées persistantes après 50 km
    signalent un problème résiduel : injecteurs encrassés ou vanne EGR
    défaillante.- Contrôle de l'état de la vanne EGR — Un FAP neuf monté avec
    une EGR encrassée se colmatera de nouveau en 20 000 à 30 000 km. Contrôlez
    visuellement la vanne et nettoyez-la si nécessaire avant de refermer le
    circuit d'échappement.- Retour à une consommation normale — La
    surconsommation liée au FAP colmaté disparaît progressivement sur les 500
    premiers km. Une consommation toujours anormalement élevée après cette
    distance justifie un contrôle des injecteurs et de la sonde lambda amont.
  S7: >-
    Quel est le prix d'un fap ?Le prix varie selon le véhicule et la marque.
    Utilisez notre sélecteur pour trouver le fap compatible avec votre véhicule
    et comparer les tarifs des différents équipementiers.Comment savoir si mon
    fap est à changer ?Les signes d'usure les plus courants sont détaillés dans
    la section diagnostic ci-dessus. En cas de doute, faites contrôler la pièce
    par un professionnel.Peut-on rouler avec un fap défaillant ?Cela dépend de
    la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du
    véhicule. Consultez la section symptômes pour évaluer l'urgence du
    remplacement.- filtrer - retenir - regenerer
  S8: >-
    Comment choisir FAP compatible avec mon vehicule ?Renseignez marque, modele,
    type moteur et annee, puis verifiez la reference Quand remplacer FAP ?En cas
    de voyant filtre particules allume tableau ou de degradation mesurable,
    Puis-je monter FAP sans verification atelier ?Le montage peut exiger
    controles de couple, alignement et references.
  META: >-
    {"meta_title":"FAP diesel : voyant allumé, que faire ? |
    AutoMecanik","meta_description":"Voyant FAP allumé, mode dégradé ou fumée
    noire à l'accélération ? Diagnostiquez votre filtre à particules diesel et
    trouvez le bon FAP pour votre véhicule.","og_title":"FAP : diagnostic et
    remplacement filtre à particules","og_description":"Perte de puissance,
    régénérations fréquentes, surconsommation : les signes d'un FAP colmaté.
    Guide complet diesel, compatibilité par immatriculation.","canonical_intent"
    :"diagnostic","schema_type":"HowTo","sources":[{"type":"rag","ref":"gammes/f
    ap.md","field":"domain.role + diagnostic.symptoms + rendering.faq"}]}
---

# FAP - Guide Diagnostic Complet

## Fonction et Rôle

Filtre et retient les particules fines des gaz d'échappement diesel

**Actions principales:** filtrer, retenir, regenerer, stocker

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant filtre particules allume tableau
- perte de puissance importante mode degrade
- regenerations frequentes odeur de brule
- fumee noire excessive a l acceleration
- surconsommation de carburant anormale
- plus de 150 000 km en conduite urbaine

## Procédure de Diagnostic

Pour diagnostiquer un problème de fap:

1. **Inspection visuelle** - Examiner l'état du fap
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-temperature-d-air-admission
- catalyseur
- sonde-lambda
- tube-d-echappement
- vanne-egr

## Critères de Compatibilité

Pour commander le bon fap, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "passe le controle technique"

## FAQ

**FAP OE ou OES : que choisir ?**
Les FAP OES (Bosal, Walker) sont de qualité équivalente à l'OE. Vérifiez l'homologation et la compatibilité exacte avec votre moteur (numéro de pièce).

**Comment savoir si mon FAP est colmaté ?**
Voyant FAP allumé, mode dégradé (perte de puissance), régénérations fréquentes, fumée noire, code défaut P2002 ou P2463.

**Tous les combien changer le FAP ?**
Entre 150 000 et 250 000 km selon utilisation. Trajets longs = longue durée de vie. Trajets courts = colmatage rapide.

**Peut-on nettoyer le FAP au lieu de le changer ?**
Oui, le décalaminage (nettoyage chimique ou thermique) peut prolonger sa vie si pas trop colmaté. Efficace à 70-80% pour 150-300€.

**Quelle erreur éviter avec le FAP ?**
Ne jamais supprimer le FAP (illégal, amende 7500€). Éviter les trajets courts répétés. Ne pas couper le moteur pendant une régénération.
## Bruits d'échappement

### Bruit métallique sous la voiture
- **Catalyseur décollé** : Le substrat céramique interne s'est fragmenté et vibre dans le boîtier. Bruit de ferraille au ralenti.
- **Silencieux percé** : Corrosion ayant percé le pot d'échappement. Bruit de souffle ou grondement.
- **Flexible d'échappement fissuré** : Joint de raccord entre le collecteur et la ligne d'échappement. Bruit de fuite.
- **Collier ou bride desserré** : Claquement rythmique, plus audible au ralenti.

### Sifflement
- **Fuite au collecteur** : Joint de collecteur d'échappement brûlé. Sifflement aigu surtout à froid, qui peut s'atténuer à chaud.
- **Fissure sur le tube** : Soudure fatiguée ou corrosion localisée.

## Fumées anormales

### Fumée blanche épaisse
- **Joint de culasse défaillant** : Liquide de refroidissement entre dans la chambre de combustion. Fumée blanche sucrée, persistante même moteur chaud. Vérifier le niveau de liquide de refroidissement.

### Fumée noire
- **Mélange trop riche** : Injecteurs qui fuient, capteur MAP/MAF défaillant, filtre à air colmaté.
- **Turbo défaillant** : Fuite d'huile dans l'admission via les joints du turbo.

### Fumée bleue
- **Consommation d'huile** : Segments usés, guides de soupapes usés, ou joint de queue de soupape. L'huile brûle dans la chambre de combustion.

## Catalyseur et FAP

- **Catalyseur colmaté** : Perte de puissance, moteur qui étouffe à l'accélération, voyant moteur allumé (codes P0420/P0430).
- **Filtre à particules bouché** : Voyant FAP allumé, régénérations trop fréquentes, perte de puissance. Fréquent sur les trajets courts en ville.
- **Sonde lambda défaillante** : Consommation en hausse, voyant moteur, mélange air/carburant mal régulé.

## Quand consulter un professionnel

- Fumée blanche persistante moteur chaud (risque joint de culasse)
- Voyant moteur + perte de puissance (catalyseur/FAP)
- Odeur d'œuf pourri (catalyseur en surchauffe)
- Bruit d'échappement fort + odeur de gaz dans l'habitacle
