---
category: moteur
slug: radiateur-d-huile
title: Radiateur d'huile
pg_id: 469
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
  role: Refroidir l'huile moteur via un echangeur thermique huile-eau ou huile-air pour maintenir la viscosite optimale et
    proteger le moteur
  must_be_true:
  - refroidir l'huile moteur
  - echanger la chaleur (huile vers eau ou air)
  - maintenir la viscosite de l'huile dans la plage optimale
  - proteger les paliers et organes internes du moteur
  must_not_contain:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  - refroidit le moteur
  related_parts:
  - filtre-a-huile
  - pompe-a-huile
  - joint-de-carter-d-huile
  - durite-de-refroidissement
  - thermostat
  confusion_with:
  - piece: radiateur-de-refroidissement
    difference: Le radiateur de refroidissement evacue la chaleur du liquide de refroidissement moteur. Le radiateur d'huile
      refroidit uniquement l'huile moteur ou boite via un echangeur separe.
  - piece: intercooler
    difference: L'intercooler refroidit l'air de suralimentation (turbo). Le radiateur d'huile refroidit l'huile.
selection:
  criteria:
  - Marque de votre vehicule
  - Modele de votre vehicule
  - Annee de votre vehicule
  - Type de motorisation (diesel souvent equipe, essence sur modeles sportifs)
  - Type d'echangeur (huile-eau integre au bloc ou huile-air externe)
  - Nombre de raccords et diametre des durites
  - Presence de thermostat integre ou non
  - Dimensions et position de montage (bride, vis, support)
  - Compatibilite joints et raccords (joints toriques inclus ou non)
  - Pression de service (selon motorisation)
  - Materiau du corps (aluminium, acier, composite)
  - Reference OE constructeur
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "repare le moteur"
  - ❌ Ne pas confondre radiateur d'huile moteur et radiateur d'huile boite automatique
  - ❌ Verifier que les joints toriques sont inclus ou a commander separement
  - ❌ Ne pas reutiliser les anciens joints lors du remplacement
  cost_range:
    min: 25
    max: 350
    currency: EUR
    unit: l'unite
    source: fourchette constatee equipementiers 2024-2025
  checklist:
  - Verifier le type (huile-eau ou huile-air)
  - Verifier le nombre de raccords (2 huile + 2 eau pour huile-eau)
  - Verifier les dimensions de la bride de fixation
  - Verifier si joints toriques inclus
  - Verifier la pression de service compatible
  - Commander les joints neufs si non inclus
  brands:
    premium:
    - Behr/Mahle
    - Modine
    - Nissens
    standard:
    - NRF
    - Valeo
    - Hella
    budget:
    - Thermotec
    - Frigair
    - Meat & Doria
  quality_tiers:
  - tier: Origine constructeur (OE/OES)
    description: Echangeur huile/eau identique a la premiere monte. Etancheite et echange thermique garantis aux specifications
      constructeur.
  - tier: Equivalent OE (qualite premiere monte)
    description: Radiateur d'huile de qualite equivalente, teste en pression et temperature. Joints fournis.
  - tier: Adaptable (qualite atelier courant)
    description: Echangeur compatible. Verifier la presence des joints et la conformite des raccords hydrauliques.
diagnostic:
  symptoms:
  - id: S1
    label: Temperature d'huile anormalement elevee (voyant ou jauge)
    severity: securite
  - id: S2
    label: Melange eau-huile (mayonnaise sous le bouchon d'huile)
    severity: securite
  - id: S3
    label: Fuite d'huile au niveau de l'echangeur
    severity: confort
  - id: S4
    label: Niveau d'huile qui baisse sans fuite visible (fuite interne vers le circuit d'eau)
    severity: securite
  - id: S5
    label: Liquide de refroidissement qui prend une teinte brunâtre (huile dans l'eau)
    severity: securite
  - id: S6
    label: Surchauffe moteur repetee malgre circuit de refroidissement OK
    severity: securite
  causes:
  - Fuite interne de l'echangeur (joints toriques uses ou corps fissure)
  - Fuite externe au niveau des raccords
  - Encrassement interne reduisant l'efficacite d'echange thermique
  - Corrosion du corps en aluminium (liquide de refroidissement non adapte)
  - Choc thermique (surchauffe moteur repetee)
  depose_steps: []
  quick_checks:
  - 'Observer : temperature d''huile anormalement elevee (voyant ou jauge) ?'
  - 'Observer : melange eau-huile (mayonnaise sous le bouchon d''huile) ?'
  - Fuite d'huile au niveau de l'echangeur ?
  - 'Observer : niveau d''huile qui baisse sans fuite visible (fuite interne vers le circuit d''eau) ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Pas de periodicite fixe. Remplacer en cas de fuite, melange eau-huile ou surchauffe. Verifier les joints a chaque
      vidange.
    source: null
  norms:
  - Les joints toriques doivent etre remplaces a chaque depose
  - Utiliser le couple de serrage constructeur pour les vis de bride
  cross_gammes:
  - filtre-a-huile
  - pompe-a-huile
  - joint-de-carter-d-huile
  - durite-de-refroidissement
  - thermostat
  brands:
    premium:
    - Mahle/Behr (equipementier OE BMW, Mercedes, VW)
    - Nissens (specialiste echangeurs thermiques)
    equivalent:
    - Valeo
    - NRF
    budget:
    - Febi
    - Meyle
  compatibility_notes:
  - Sur moteurs diesel modernes (TDI, HDI, dCi), le radiateur d'huile est souvent integre au bloc filtre a huile
  - Sur moteurs essence sportifs, il peut etre un echangeur externe huile-air avec durites
  - Le remplacement seul prend 1 a 3h selon l'accessibilite
  - Sur certains modeles (VW/Audi TSI, BMW N47/N57), le boitier filtre complet inclut l'echangeur
  wear_signs:
  - Temperature d'huile anormalement elevee (voyant ou jauge)
  - Melange eau-huile (mayonnaise sous le bouchon d'huile)
  - Fuite d'huile au niveau de l'echangeur
  - Niveau d'huile qui baisse sans fuite visible (fuite interne vers le circuit d'eau)
  - Liquide de refroidissement qui prend une teinte brunâtre (huile dans l'eau)
  - Surchauffe moteur repetee malgre circuit de refroidissement OK
  good_practices:
  - Controle du niveau de liquide de refroidissement a froid chaque mois
  - Remplacement du liquide selon preconisation constructeur (2-5 ans)
  - Verification des durites et colliers a chaque revision
  - Purge du circuit apres toute intervention sur le refroidissement
rendering:
  pgId: '469'
  intro_title: A quoi sert le radiateur d'huile ?
  risk_title: Pourquoi remplacer le radiateur d'huile a temps ?
  risk_explanation: Un radiateur d'huile defaillant provoque une surchauffe de l'huile, reduisant sa viscosite et accelerant
    l'usure des paliers et organes internes du moteur.
  risk_consequences:
  - Surchauffe de l'huile moteur entrainant une usure acceleree des composants internes
  - Melange eau-huile (mayonnaise) pouvant provoquer une casse moteur
  - Fuite d'huile externe au niveau de l'echangeur
  - Contamination du liquide de refroidissement par l'huile
  risk_conclusion: Un diagnostic precoce evite la casse moteur. Le melange eau-huile est une urgence.
  arguments:
  - content: Selection guidee par vehicule, type de motorisation et reference OE.
    icon: check-circle
    title: Compatibilite verifiee
  - content: Un echangeur defaillant peut provoquer la casse moteur par surchauffe d'huile.
    icon: shield-check
    title: Piece critique moteur
  - content: Verifiez si les joints sont inclus avant de commander.
    icon: clock
    title: Decision rapide
  - content: Pensez a commander le filtre a huile et les joints en meme temps.
    icon: list-check
    title: Pieces associees
  faq:
  - question: Radiateur d'huile OE ou adaptable ?
    answer: Les echangeurs OES (Mahle/Behr, Nissens, NRF) sont de qualite equivalente a l'OE. Sur moteurs turbo diesel, privilegiez
      l'OE ou OES pour la resistance aux pressions elevees.
  - question: Huile-eau ou huile-air, quelle difference ?
    answer: L'echangeur huile-eau est integre au bloc moteur et utilise le circuit de refroidissement. L'echangeur huile-air
      est externe avec ses propres durites. Le type depend de votre motorisation.
  - question: Faut-il changer les joints avec le radiateur d'huile ?
    answer: Oui obligatoirement. Les joints toriques entre l'echangeur et le bloc moteur doivent etre remplaces a chaque depose.
      Reutiliser les anciens joints provoque des fuites.
  - question: Comment detecter un radiateur d'huile HS ?
    answer: Mayonnaise sous le bouchon d'huile (melange eau-huile), liquide de refroidissement brunâtre, fuite d'huile au
      niveau de l'echangeur, temperature d'huile elevee.
  - question: Peut-on rouler avec un radiateur d'huile qui fuit ?
    answer: Si fuite externe legere, controler le niveau d'huile regulierement. Si melange eau-huile (mayonnaise), arreter
      le moteur immediatement pour eviter la casse.
  quality:
    score: 82
    source: manual-enrichment-2026-03-21
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
doc_id: 3bbc5f70-c5d8-52c4-9596-5231d5bed3b9
content_hash: sha256:6edf4800706dca31
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
  _source: gpa26.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 1
  _has_tech_data: false
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Danscertains véhicules, le radiateur de refroidissement est accompagné d'un
    radiateurd'huile pour refroidir l'huile moteur. Dans certaine motorisation,
    l'huilemoteur est soumise à des contraintes thermiques très élevées dés la
    mise enmarche du moteur dans ce que cas elle doit être refroidit pour que
    lesdifférentes pièces moteur soient bien lubrifier parce que l'huile joue le
    rôlede protection entre les pièces mobile interne du moteur. La température
    dumoteur peut atteindre les 100°C (voire 120°C) à cause des frictions entre
    lespièces du moteur ce qui provoque un échauffement des métaux et par
    conséquentl'huile maintien la température des pièces dans ce cas ildoit être
    refroidit pour lubrification optimale. Le radiateur d'huile se situe à
    l'avant du véhicule soit sous le pare-chocs,soit il est recouvert d'une
    grille. Il refroidit l'huile moteur grâce au fluxd'air qui le traverse. Pour
    bien contrôler latempérature vous pouvez installer un manomètre de
    température d'huile. En savoir plus : radiateur d'huile — définition et rôle
    mécanique 🚨 Bruit Radiateur d'huile : causes et diagnostic
  S2: >-
    Un radiateur d'huile défectueux présente plusieurs symptômes : - Fuite au
    niveau duradiateur d'huile. - Déformation du radiateurd'huile à cause d'un
    choc frontal. Un radiateur d'huileHS et qu'il n'est pas remplacé à temps
    peut amener à la casse dumoteur à cause du manque d'huile moteur et du
    surchauffe de ce dernier. Diagnostic complet : identifier une panne de
    radiateur d'huile
  S3: >-
    Le radiateur d'huile maintient la température de l'huile moteur dans la
    plage de viscosité optimale, typiquement entre 80 °C et 120 °C selon le
    constructeur. Un radiateur de capacité inadaptée — trop petit pour une
    utilisation intensive ou trop grand pour un moteur atmosphérique — perturbe
    la thermique moteur et accélère le vieillissement de l'huile. La sélection
    par référence véhicule est impérative. - Type de raccordement : eau-huile ou
    air-huile — Les radiateurs d'huile eau-huile sont intégrés au circuit de
    refroidissement moteur (thermosiphon) et logés dans le filtre à huile ou sur
    le carter. Les radiateurs air-huile, généralement additionnels, sont
    positionnés devant le radiateur principal. Ces deux technologies ont des
    configurations de raccordement radicalement différentes. - Filetage des
    raccords d'huile — Les filetages courants sur les radiateurs d'huile vissés
    sont M20x1,5, M22x1,5 ou M26x1,5. Un adaptateur mal choisi provoque une
    fuite d'huile sous pression. Mesurer le pas et le diamètre de l'embase sur
    le bloc moteur avant toute commande. - Nombre de rangées et capacité
    d'échange thermique — La capacité d'échange est proportionnelle au nombre de
    rangées (de 2 à 8 rangées sur les modèles standards). Sur les moteurs diesel
    à forte charge (traction ou utilitaire), ne pas descendre en dessous de la
    capacité d'origine, au risque d'une surchauffe d'huile en côte prolongée. -
    Présence d'un bypass thermostatique — Certains radiateurs d'huile intègrent
    une vanne thermostatique qui court-circuite le radiateur quand l'huile est
    froide (typiquement sous 60 °C). Cette fonction protège les coussinets au
    démarrage hivernal. Vérifier si l'original en était équipé avant de
    commander un modèle nu. - Matériau : aluminium ou acier — Les radiateurs
    aluminium sont plus légers et offrent un meilleur échange thermique, mais
    sont sensibles aux chocs mécaniques et à la corrosion galvanique si le
    liquide de refroidissement est mal entretenu. L'acier est plus robuste mais
    plus lourd. - Position et orientation des entrées/sorties — La position des
    raccords (haut/bas, latéral/frontal) doit correspondre exactement au schéma
    de tuyauterie du véhicule. Un radiateur d'aspect identique mais avec
    raccords inversés impose une modification des durites non prévue. - Contrôle
    simultané des joints et durites — Remplacer systématiquement les joints
    toriques ou les colliers de serrage des durites d'huile lors du remplacement
    du radiateur. Ces joints sont souvent détériorés lors du démontage et leur
    réutilisation provoque des fuites. Pour aller plus loin : consultez notre
    guide d'achat radiateur d'huile — comparatif marques, critères de choix et
    prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Radiateur d'huile pour
    connaître les spécifications. - Débranchez la batterie. - Levez et calez le
    véhicule. - Vidanger l'huile moteur. - Localisez l'emplacement du
    radiateurd'huile. - Démontez le pare-choc avant. - Démontez les fixations du
    radiateurd'huile. - Désaccouplez les canalisations d'entrée etde sortie du
    radiateur d'huile. - Démontez le radiateur d'huile.
  S4_REPOSE: >-
    - Vérifiez que le radiateurd'huile neuf est identique à celui démonté. -
    Contrôlez l'état de fonctionnement duradiateur de refroidissement et le
    remplacé si nécessaire. - Remontez le radiateur d'huile. - Accouplez les
    canalisationsd'entrée et de sortie du radiateur d'huile. - Serrez les
    fixations duradiateur d'huile. - Remontez lepare-choc avant. - Redescendre
    le véhicule. - Rebranchez labatterie. - Remplissez l'huile moteur. -
    Remontez un filtre à huileneuf. - Contrôler le bonfonctionnement du circuit
    de lubrification. ✅ Après remontage, vérifiez les spécifications dans la
    fiche technique Radiateur d'huile.
  S5: >-
    - ❌ "homologué CT - ❌ "sécurité garantie - ❌ "zéro panne - ❌ "garanti à vie
    - ❌ "repare le moteur
  S6: >-
    Le radiateur d'huile est en interface directe entre le circuit huile moteur
    et le circuit eau de refroidissement (ou l'air extérieur sur les modèles à
    refroidissement par air). Son remplacement impose un protocole de
    vérification rigoureux centré sur l'étanchéité des deux circuits et
    l'absence de contamination croisée huile-eau. - Purge complète du circuit de
    refroidissement : si le radiateur d'huile est du type eau-huile (le plus
    courant), purger intégralement le circuit de refroidissement après remontage
    pour éliminer toute bulle d'air. Remplir avec un mélange eau déminéralisée /
    antigel à 50 % jusqu'au repère MAX du vase d'expansion. Une bulle d'air
    persistante génère des points chauds locaux. - Contrôle d'absence de mélange
    eau-huile : après le premier démarrage, observer la couleur de l'huile sur
    la jauge : une couleur chocolat au lait ou des petites bulles blanches sur
    le bouchon de vidange signalent une contamination eau-huile — signe d'un
    joint interne défaillant ou d'un raccordement incorrect. Couper le moteur
    immédiatement. - Vérification de la température d'huile : après 15 minutes
    de chauffe en cycle mixte, la température d'huile doit se stabiliser entre
    90 et 110 °C (lisible sur un outil de diagnostic OBD si le véhicule dispose
    d'un capteur de température d'huile). Une température d'huile supérieure à
    130 °C indique que l'échangeur ne fonctionne pas correctement. - Inspection
    des raccords et colliers : contrôler visuellement les durites de connexion
    au radiateur d'huile et les colliers de serrage. Aucun suintement d'huile ni
    de liquide de refroidissement ne doit apparaître après montée en
    température. Resserrer les colliers à la main après refroidissement si
    nécessaire. - Contrôle du niveau d'huile moteur : le remplacement du
    radiateur d'huile entraîne une perte d'huile. Vérifier le niveau sur jauge
    froide avant le premier démarrage et après le premier cycle thermique.
    Compléter jusqu'au repère MAX avec l'huile conforme aux préconisations
    constructeur (viscosité 5W30, 5W40 ou autre selon moteur). - Absence de
    fuites externes après 48h : inspecter le dessous du véhicule après une ou
    deux journées de fonctionnement normal. Aucune trace d'huile ni de liquide
    coloré ne doit apparaître sous le carter moteur à la verticale du radiateur
    d'huile.
  S7: >-
    Quel est le prix d'un radiateur d'huile ?Le prix varie selon le véhicule et
    la marque. Utilisez notre sélecteur pour trouver le radiateur d'huile
    compatible avec votre véhicule et comparer les tarifs des différents
    équipementiers.Comment savoir si mon radiateur d'huile est à changer ?Les
    signes d'usure les plus courants sont détaillés dans la section diagnostic
    ci-dessus. En cas de doute, faites contrôler la pièce par un
    professionnel.Peut-on rouler avec un radiateur d'huile défaillant ?Cela
    dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la
    sécurité du véhicule. Consultez la section symptômes pour évaluer l'urgence
    du remplacement.- filtre a huile - pompe a huile
  S8: >-
    Comment choisir Radiateur d'huile compatible avec mon vehicule ?Renseignez
    marque, modele, type moteur et annee, puis verifiez la reference Quand
    remplacer Radiateur d'huile ?En cas de huile surchauffee ou de degradation
    mesurable, il faut controler Puis-je monter Radiateur d'huile sans
    verification atelier ?Le montage peut exiger controles de couple, alignement
    et references.
  META: >-
    {"meta_title":"Radiateur d'huile : fuites et surchauffe moteur |
    AutoMecanik","meta_description":"Huile surchauffée, mélange eau-huile, fuite
    au niveau du radiateur ? Identifiez les causes d'un radiateur d'huile
    défaillant et choisissez la bonne pièce pour votre
    moteur.","source":"rag://gammes/radiateur-d-huile.md"}
---

# Radiateur d'huile - Guide Diagnostic et Achat

## Fonction et Role

Le radiateur d'huile (echangeur thermique) refroidit l'huile moteur en transferant la chaleur vers le circuit de refroidissement (echangeur huile-eau) ou directement vers l'air ambiant (echangeur huile-air). Il maintient la viscosite optimale de l'huile pour proteger les paliers, segments et organes internes du moteur.

**Actions principales:** refroidir l'huile, echanger la chaleur, maintenir la viscosite optimale, proteger le moteur

## Types de radiateurs d'huile

### Echangeur huile-eau (le plus courant)
- Integre au bloc moteur, souvent solidaire du support de filtre a huile
- Utilise le circuit de refroidissement pour evacuer la chaleur
- Compact, efficace, pas de durites externes
- Frequent sur moteurs diesel modernes (TDI, HDI, dCi)

### Echangeur huile-air (externe)
- Monte separement avec ses propres durites et raccords
- Refroidissement par flux d'air (place devant le radiateur principal)
- Utilise sur moteurs sportifs ou vehicules a forte sollicitation
- Necessite plus d'espace et des durites specifiques

## Symptomes de Defaillance

### 🔴 Symptomes Critiques (Securite)

- **Melange eau-huile** — mayonnaise blanchatre sous le bouchon d'huile ou dans le vase d'expansion
- **Niveau d'huile qui baisse** sans fuite visible (fuite interne vers le circuit d'eau)
- **Liquide de refroidissement brunâtre** (contamination par l'huile)
- **Surchauffe moteur repetee** malgre circuit de refroidissement fonctionnel

### 🟡 Symptomes de Confort

- **Fuite d'huile** au niveau de l'echangeur ou de ses raccords
- **Temperature d'huile elevee** sur la jauge ou le voyant


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Pas de periodicite fixe. Remplacer en cas de fuite, melange eau-huile ou surchauffe. Verifier les joints a chaque vidange.

## Causes Probables

- **Joints toriques uses** — cause la plus frequente de fuite interne ou externe
- **Corps fissure** — corrosion ou choc thermique
- **Encrassement interne** — depot reduisant l'efficacite d'echange
- **Liquide de refroidissement non adapte** — corrosion acceleree de l'aluminium

## Pieces Associees

Lors du remplacement, verifier et commander si necessaire :

- **filtre-a-huile** — a remplacer systematiquement avec l'echangeur
- **joint-de-carter-d-huile** — si vidange necessaire
- **pompe-a-huile** — verifier l'etat si surchauffe repetee
- **durite-de-refroidissement** — si echangeur externe
- **thermostat** — si surchauffe moteur associee

## Criteres de Compatibilite

Pour commander le bon radiateur d'huile :

- **Marque, modele et annee** de votre vehicule
- **Type de motorisation** (diesel, essence, cylindree)
- **Type d'echangeur** (huile-eau integre ou huile-air externe)
- **Nombre et diametre des raccords**
- **Presence de thermostat integre**
- **Reference OE constructeur** (indispensable sur modeles recents)

## Marques reconnues

| Segment | Marques | Note |
|---------|---------|------|
| Premium OE | Mahle/Behr, Nissens | Equipementiers premiere monte BMW, Mercedes, VW |
| Equivalent OES | Valeo, NRF | Bon rapport qualite/prix |
| Budget | Febi, Meyle | Acceptable sur modeles courants, verifier les joints inclus |

## ❌ Attention aux Erreurs Frequentes

- ❌ Ne pas confondre radiateur d'huile **moteur** et radiateur d'huile **boite automatique**
- ❌ Ne pas reutiliser les anciens joints toriques
- ❌ Ne pas oublier de commander les joints si non inclus avec la piece
- ❌ Verifier le type exact (huile-eau vs huile-air) avant de commander
- ❌ Sur VW/Audi/BMW, le boitier filtre complet peut inclure l'echangeur

## FAQ

**Radiateur d'huile OE ou adaptable ?**
Les echangeurs OES (Mahle/Behr, Nissens, NRF) sont de qualite equivalente a l'OE. Sur moteurs turbo diesel, privilegiez l'OE ou OES pour la resistance aux pressions elevees.

**Huile-eau ou huile-air, quelle difference ?**
L'echangeur huile-eau est integre au bloc moteur et utilise le circuit de refroidissement. L'echangeur huile-air est externe avec ses propres durites. Le type depend de votre motorisation.

**Faut-il changer les joints avec le radiateur d'huile ?**
Oui obligatoirement. Les joints toriques entre l'echangeur et le bloc moteur doivent etre remplaces a chaque depose. Reutiliser les anciens joints provoque des fuites.

**Comment detecter un radiateur d'huile HS ?**
Mayonnaise sous le bouchon d'huile (melange eau-huile), liquide de refroidissement brunâtre, fuite d'huile au niveau de l'echangeur, temperature d'huile elevee.

**Peut-on rouler avec un radiateur d'huile qui fuit ?**
Si fuite externe legere, controler le niveau d'huile regulierement. Si melange eau-huile (mayonnaise), arreter le moteur immediatement pour eviter la casse.
