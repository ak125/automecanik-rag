---
category: suspension
slug: amortisseur
title: Amortisseur
pg_id: 854
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
  role: Controler les oscillations du ressort et stabiliser la roue. Dissipe l'energie des chocs. NE SUPPORTE PAS LE POIDS
    DU VEHICULE!
  must_be_true:
  - amortir
  - controler
  - dissiper
  must_not_contain:
  - direction
  - freinage
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - ressort-de-suspension
  - bras-de-suspension
  - rotule-de-suspension
  - barre-stabilisatrice
  - biellette-de-barre-stabilisatrice
  - coupelle-d-amortisseur
  confusion_with:
  - term: ressort-de-suspension
    difference: L amortisseur controle le rebond. Le ressort supporte le poids. Pieces distinctes, souvent remplaces ensemble.
  - term: coupelle-d-amortisseur
    difference: La coupelle est le palier superieur qui fixe l amortisseur a la carrosserie. Piece separee.
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
  - ❌ "tenue de route parfaite"
  cost_range:
    min: 46
    max: 651
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Piece d'origine (OE)
    description: Amortisseur code constructeur, identique a la monte usine. Recommande sur vehicules recents sous garantie.
  - tier: Equipementier rang 1 - equivalence OE
    description: Les grands equipementiers fournissent les lignes de montage constructeur. Leur gamme de rechange est techniquement
      equivalente pour l'usage courant.
  - tier: Marque intermediaire
    description: Amortisseurs de remplacement conformes aux cotes OE. Adaptes pour un usage courant avec un budget maitrise.
      Verifier la garantie et les certifications.
  brands:
    premium:
    - Bilstein
    - Sachs
    - KYB
    standard:
    - Monroe
    - Meyle
    - Febi
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Vehicule qui rebondit excessivement sur les bosses
    severity: confort
  - id: S2
    label: Fuite huile visible corps amortisseur
    severity: confort
  - id: S3
    label: Usure asymetrique ou irreguliere des pneus
    severity: securite
  - id: S4
    label: Bruit de cognement sur routes degradees
    severity: confort
  - id: S5
    label: Sensation d instabilite en virage ou au freinage
    severity: securite
  - id: S6
    label: Plus de 80 000 km sans remplacement
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - remplacement preventif recommande
  quick_checks:
  - 'Observer : vehicule qui rebondit excessivement sur les bosses ?'
  - Fuite huile visible corps amortisseur ?
  - 'Observer : usure asymetrique ou irreguliere des pneus ?'
  - Bruit de cognement sur routes degradees ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Vehicule qui rebondit excessivement sur les bosses
  - Fuite huile visible corps amortisseur
  - Usure asymetrique ou irreguliere des pneus
  - Bruit de cognement sur routes degradees
  - Sensation d instabilite en virage ou au freinage
  - Plus de 80 000 km sans remplacement
  good_practices:
  - Controle visuel des fuites et deformations a chaque revision
  - Remplacement par paire (meme essieu) pour equilibre du vehicule
  - Faire verifier la geometrie apres remplacement
  - Inspection des silent-blocs et des rotules associees
rendering:
  pgId: '854'
  intro_title: A quoi sert Amortisseur ?
  risk_title: Pourquoi remplacer Amortisseur a temps ?
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
  - question: 'Amortisseur OE ou adaptable : que choisir ?'
    answer: Les amortisseurs OES (Sachs) ou premium (Monroe, KYB, Bilstein) offrent un excellent rapport qualité/prix. L'OE
      est recommandé pour véhicules premium ou sportifs.
  - question: Comment savoir si mes amortisseurs sont HS ?
    answer: Rebonds excessifs sur dos d'âne, aquaplaning précoce, usure asymétrique des pneus, fuite d'huile visible sur le
      corps de l'amortisseur.
  - question: Tous les combien changer les amortisseurs ?
    answer: Entre 80 000 et 120 000 km en moyenne. Contrôle visuel recommandé à 60 000 km. Plus tôt sur routes dégradées.
  - question: Peut-on changer les amortisseurs soi-même ?
    answer: Possible mais nécessite compresseur de ressorts (dangereux). Géométrie obligatoire après. Prévoir 2h par essieu.
  - question: Quelle erreur éviter avec les amortisseurs ?
    answer: Ne jamais changer un seul amortisseur. Toujours par paire sur le même essieu. Vérifier coupelles et butées en
      même temps.
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
doc_id: 7cf61614-e134-5ce1-afc4-8b6f06c62f33
content_hash: sha256:00bc4ad510335826
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
  _source: aftermarket.zf.com + ate-freinage.fr + bremboparts.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 3
  _has_tech_data: true
  types_variants:
  - type: 'Composite'
    source_ref: corpus RAG web OEM
  - type: 'bi-matière'
    source_ref: corpus RAG web OEM
  - type: 'composite'
    source_ref: corpus RAG web OEM
  - type: 'céramique'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    norme_ece_r90: 'ECE R90'
    norme_sae_j2521: 'SAE J2521'
    val_000_km: '000 km'
    val_1_5_mm: '1,5 mm'
    val_10__m: '10 µm'
    val_100__: '100 %'
    val_100_a: '100 a'
    val_30__m: '30 µm'
    val_45__: '45 %'
    val_50000_km: '50000 km'
    val_700__c: '700 °C'
    val_80__: '80 %'
    val_85__: '85 %'
    val_97__: '97 %'
  materials:
  - materiau: 'aluminium'
    source_ref: corpus RAG web OEM
  - materiau: 'céramique'
    source_ref: corpus RAG web OEM
  - materiau: 'fonte grise'
    source_ref: corpus RAG web OEM
  - materiau: 'graphite'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    L'amortisseurest une jambe de suspension à système de compression qui
    fonctionne à l'huile ou au gaz. L'huile ou le gaz est comprimée dans le
    cylindre de l'amortisseurgrâce à un piston qui ne cesse de monter et
    descendre à chaque déformation dela route parcouru par le véhicule. Ce
    mouvement permanent a pour fonctiond'amortir les chocs.
    L'amortisseurfonctionne en duo avec le ressortde suspension. La combinaison
    entre eux assure le confort à bord du véhicule etla bonne tenue de route. En
    savoir plus : amortisseur — définition et rôle mécanique 🚨 Bruit de
    amortisseur : que faire ?
  S2: >-
    Ne pas attendre la panne complete pour intervenir. Symptômes d'usure : -
    Vehicule qui rebondit excessivement sur les bosses - Fuite huile visible
    corps amortisseur - Usure asymetrique ou irreguliere des pneus - Bruit de
    cognement sur routes degradees - Sensation d instabilite en virage ou au
    freinage - Plus de 80 000 km sans remplacement
  S2_DIAG: >-
    SymptômeCause probableActionUn bruit anormal au niveau du amortisseur peut
    se manifester lors de la phase "acceleration"Pour identifier ce probleme de
    bruit du amortisseur:Verification visuelle du amortisseurDes vibrations
    provenant du amortisseur sont souvent perceptibles a haute vitessePour
    identifier ce probleme de vibration du amortisseur:Verification visuelle du
    amortisseur
  S3: >-
    L'amortisseur contrôle les oscillations du ressort de suspension. Un modèle
    incompatible modifie dangereusement le comportement routier du
    véhicule.Vérifications indispensables- Essieu : avant ou arrière — les
    amortisseurs avant et arrière ont des caractéristiques très différentes-
    Type de fixation : œillet/œillet, tige/œillet, ou tige/coupelle — doit
    correspondre exactement aux points d'ancrage du véhicule- Longueur comprimé
    et déployé : mesurer l'amortisseur déposé dans les deux positions (tolérance
    ± 5 mm)- Technologie : hydraulique, à gaz monotube ou à gaz bitube — le type
    d'origine est recommandé pour un remplacement standard- Diamètre de tige :
    12, 14 ou 16 mm selon le modèle — conditionne la coupelle et l'écrou
    supérieurMéthode de vérificationRelever la référence OE sur l'amortisseur
    déposé ou via le VIN. Comparer les cotes et le type de fixation haute et
    basse.Pour aller plus loin : consultez notre guide d'achat amortisseur —
    comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Amortisseur pour connaître
    les spécifications. - Levez le véhicule. - Démontez le tapis du coffre (si
    nécessaire pour accéder àla fixation supérieure de l'amortisseur). -
    Démontez les fixations supérieures de l'amortisseur. - Démontez la roue. -
    Démontez la fixation inférieure de l'amortisseur. - Démontez l'amortisseur.
  S4_REPOSE: >-
    - Vérifier que l'amortisseur neuf est identique à celuidémonté. - Contrôlez
    la butée élastique d?amortisseur et remplacéessi nécessaire. - Remontez
    l'amortisseur. - Serrez les fixations inférieure et supérieure de
    l'amortisseur. - Reposez la roue. - Redescendre le véhicule. - Resserrez la
    roue. - Faire un essai routier. ✅ Après remontage, vérifiez les
    spécifications dans la fiche technique Amortisseur.
  S5: >-
    - Ne changer qu'un seul amortisseur sur un essieu — Un amortisseur neuf d'un
    côté et un amortisseur usé de l'autre créent une dissymétrie de comportement
    : le côté neuf rebondit moins que le côté usé, le véhicule se déporte au
    freinage et la tenue de route devient imprévisible. Remplacer toujours les
    amortisseurs par paire sur le même essieu, les deux avant ou les deux
    arrière. - Oublier coupelle, butée et soufflet lors du remplacement — La
    coupelle supérieure (palier de pivot avant), la butée de suspension et le
    soufflet de protection de la tige s'usent au même rythme que l'amortisseur.
    Remonter un amortisseur neuf avec une butée fissurée ou une coupelle à
    roulement grippé recréera des bruits de claquement à froid dans les 6 mois.
    Ces pièces sont vendues en kit et représentent un faible surcoût pour une
    intervention durable. - Utiliser un compresseur de ressorts non homologué ou
    mal engagé — Le ressort de suspension comprimé stocke une énergie
    équivalente à plusieurs centaines de joules. Un compresseur endommagé, des
    crochets mal engagés sur les spires ou une compression asymétrique
    provoquent une libération violente du ressort pouvant causer des fractures.
    Utiliser des compresseurs homologués dont les crochets couvrent entièrement
    les spires. - Serrer l'écrou de tige sans maintenir la tige en rotation —
    Sur la plupart des amortisseurs, la tige de piston tourne librement sans une
    clé de maintien. Vissez l'écrou sans immobiliser la tige revient à ne rien
    serrer : l'écrou tourne dans le vide. Engager une clé Allen (hexagonale
    femelle) ou un plat de maintien dans l'extrémité de la tige pendant le
    serrage de l'écrou. - Monter l'amortisseur tête en bas — La tige chromée
    doit toujours pointer vers le haut. Un amortisseur monotube inversé provoque
    une fuite d'huile immédiate (la chambre à gaz se retrouve en bas). Vérifier
    l'orientation avant montage : la tige polie (chromée ou dorée) = partie
    haute, le corps plus large = partie basse. - Négliger l'amorçage de
    l'amortisseur neuf — Un amortisseur livré en position comprimée (piston à
    mi-course) peut contenir une poche d'air résiduelle. Avant montage,
    comprimer et étendre la tige 5 à 10 fois tige vers le haut (position
    verticale). Ce geste chasse l'air piégé et garantit une amortissement
    optimal dès la première sollicitation. - Serrer les silentblocs inférieurs
    véhicule suspendu — Les silentblocs de la fixation basse de l'amortisseur
    doivent être serrés au couple en position de charge normale (véhicule posé
    sur ses roues). Serrer en position levée précontraint le caoutchouc du
    silentbloc, ce qui provoque des bruits de claquement à froid et réduit la
    durée de vie du silentbloc à quelques mois. - Omettre le contrôle de
    géométrie après remplacement avant — Le remplacement des amortisseurs avant
    modifie parfois légèrement le carrossage et le parallélisme selon le type de
    suspension. Un train avant mal géométré use les pneus de façon asymétrique
    (usure latérale d'un flanc) et dévie la trajectoire au freinage. Faire
    contrôler la géométrie dans les 500 km suivant le remplacement des
    amortisseurs avant. 📖 Fiche technique Amortisseur — couples de serrage et
    spécifications constructeur.
  S6: >-
    Contrôles statiques (véhicule au sol)- Vérifier que le véhicule est à la
    même hauteur des deux côtés (mesurer l'écart aile/sol)- Contrôler le serrage
    de l'écrou de tige supérieur et des fixations inférieures au couple
    constructeur- Inspecter que le soufflet de protection est en place et non
    pincé- Appuyer fermement sur chaque coin du véhicule et relâcher : la caisse
    doit revenir en position et se stabiliser en 1-2 oscillations maximumTest
    routier progressif- Rouler à 30 km/h sur route plane : pas de bruit de
    cognement ni de grincement- Passer sur un ralentisseur à 30 km/h : la caisse
    absorbe le choc sans rebond excessif- Rouler à 90 km/h : stabilité en ligne
    droite, pas de flottement ni de louvoiement- Freiner d'urgence : le véhicule
    doit rester stable et en ligne, sans plongée excessive de l'avant⚠️
    Important : Si le véhicule penche d'un côté après remplacement, vérifiez que
    les ressorts de suspension sont identiques des deux côtés. Un ressort cassé
    ou affaissé annule l'efficacité de l'amortisseur neuf.
  S_GARAGE: >-
    Nous vous recommandons de confier cette intervention à un professionnel : -
    Plusieurs causes possibles de défaillance (3 identifiées) nécessitent un
    diagnostic professionnel Un garagiste qualifié dispose de l'outillage et de
    l'expérience nécessaires pour effectuer cette opération en toute sécurité.
  S7: >-
    Quel est le prix d'un amortisseur ?Le prix varie selon le véhicule et la
    marque. Utilisez notre sélecteur pour trouver l'amortisseur compatible avec
    votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si l'amortisseur est à changer ?Les signes d'usure les plus courants
    sont détaillés dans la section diagnostic ci-dessus. En cas de doute, faites
    contrôler la pièce par un professionnel.Peut-on rouler avec un amortisseur
    défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la
    pièce dans la sécurité du véhicule. Consultez la section symptômes pour
    évaluer l'urgence du remplacement.Lors du remplacement des amortisseurs,
    inspectez systématiquement ces pièces connexes :- Coupelle d'amortisseur —
    le roulement de coupelle s'use et provoque des craquements en braquant,
    remplacer avec l'amortisseur- Butée de suspension — absorbe les fins de
    course, se désagrège avec le temps, remplacer systématiquement- Soufflet de
    protection — protège la tige chromée de la corrosion, inclus dans les kits
    de protection- Ressort de suspension — vérifier l'absence de spire cassée et
    la hauteur (comparer les deux côtés)- Biellette de barre stabilisatrice —
    souvent accessible lors de la dépose, vérifier le jeu des rotules- Silent-
    blocs de bras — un silent-bloc usé transmet les chocs malgré un amortisseur
    neuf- Roulement de roue — un jeu de roulement peut être confondu avec un
    bruit d'amortisseur
  S8: >-
    Comment savoir si mes amortisseurs sont usés ?Les signes principaux : le
    véhicule rebondit excessivement sur les bosses, la tenue de route se dégrade
    en virage, les distances de freinage augmentent, et les pneus s'usent de
    manière irrégulière. Le test simple : appuyez fermement sur un coin du
    véhicule et relâchez — s'il rebondit plus d'une fois, l'amortisseur est
    fatigué. Une fuite d'huile visible sur le corps est un signe évident.Tous
    les combien faut-il changer les amortisseurs ?La recommandation générale est
    entre 60 000 et 100 000 km, mais cela dépend fortement des conditions
    d'utilisation. Sur routes dégradées ou avec un véhicule lourdement chargé,
    l'usure est plus rapide. Après 80 000 km, faites contrôler leur efficacité
    même sans symptôme apparent.Amortisseurs à gaz ou hydrauliques, que choisir
    ?Les amortisseurs à gaz (monotube ou bitube pressurisé) offrent une
    meilleure tenue de route et résistent mieux à l'échauffement. Les
    hydrauliques sont plus confortables mais moins performants en usage sportif.
    Pour un remplacement standard, choisissez le même type que l'origine. Pour
    améliorer le comportement, passez au gaz monotube.Pourquoi faut-il les
    changer par paire ?Un amortisseur neuf et un usé créent un déséquilibre
    dangereux : le côté usé rebondit davantage, réduisant l'adhérence de cette
    roue au sol. En freinage d'urgence ou en évitement, le véhicule peut devenir
    instable. Toujours remplacer les deux amortisseurs du même essieu.Les
    amortisseurs influencent-ils le freinage ?Oui, significativement. Des
    amortisseurs usés augmentent les distances de freinage de 10 à 20 % car les
    roues perdent le contact avec le sol lors des rebonds. L'ABS fonctionne
    moins efficacement quand les roues décollent entre les oscillations.
  META: >-
    Guide remplacement amortisseurs : compatibilité, erreurs courantes, pièces
    liées et vérifications après montage. Toujours changer par paire.
---

# Amortisseur - Guide Diagnostic Complet

## Fonction et Rôle

Controler les oscillations du ressort et stabiliser la roue. Dissipe l'energie des chocs. NE SUPPORTE PAS LE POIDS DU VEHICULE!

**Actions principales:** amortir, controler, dissiper, stabiliser, absorber les oscillations

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Usure asymetrique ou irreguliere des pneus**
  usure asymetrique ou irreguliere des pneus
- **Sensation d instabilite en virage ou au freinage**
  sensation d instabilite en virage ou au freinage

### 🟢 Autres Symptômes

- vehicule qui rebondit excessivement sur les bosses
- fuite huile visible corps amortisseur
- bruit de cognement sur routes degradees
- plus de 80 000 km sans remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de amortisseur:

1. **Inspection visuelle** - Examiner l'état du amortisseur
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

- bras-de-suspension
- kit-de-butee-de-suspension
- ressort-de-suspension
- rotule-de-suspension

## Critères de Compatibilité

Pour commander le bon amortisseur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "tenue de route parfaite"

## FAQ

**Amortisseur OE ou adaptable : que choisir ?**
Les amortisseurs OES (Sachs) ou premium (Monroe, KYB, Bilstein) offrent un excellent rapport qualité/prix. L'OE est recommandé pour véhicules premium ou sportifs.

**Comment savoir si mes amortisseurs sont HS ?**
Rebonds excessifs sur dos d'âne, aquaplaning précoce, usure asymétrique des pneus, fuite d'huile visible sur le corps de l'amortisseur.

**Tous les combien changer les amortisseurs ?**
Entre 80 000 et 120 000 km en moyenne. Contrôle visuel recommandé à 60 000 km. Plus tôt sur routes dégradées.

**Peut-on changer les amortisseurs soi-même ?**
Possible mais nécessite compresseur de ressorts (dangereux). Géométrie obligatoire après. Prévoir 2h par essieu.

**Quelle erreur éviter avec les amortisseurs ?**
Ne jamais changer un seul amortisseur. Toujours par paire sur le même essieu. Vérifier coupelles et butées en même temps.


## References supplementaires

<!-- materialized-from-db guides/identifier-panne-auto.md 2026-02-21 -->
### Guide - Comment identifier une panne auto : methodes, signes et urgences

# Comment identifier une panne auto : guide complet

## Pourquoi identifier soi-meme sa panne ?

Un diagnostic precoce permet d'eviter une panne totale, de reduire le cout de reparation et d'arriver chez le garagiste avec une hypothese claire. 80% des pannes presentent des signes avant-coureurs pendant plusieurs semaines avant l'immobilisation.

## Les 3 methodes pour identifier une panne auto

### 1. Observer les symptomes sensoriels (sans outil)

Chaque organe du vehicule communique par un canal sensoriel distinct :

| Canal | Exemples | Zone probable |
|-------|----------|---------------|
| Auditif | Sifflement, claquement, grincement | Freinage, suspension, moteur |
| Visuel | Fumee, voyant, fuite | Moteur, circuit de refroidissement, freins |
| Tactile | Vibration, a-coup, pedale molle | Suspension, embrayage, freinage |
| Olfactif | Odeur de brule, de caoutchouc | Embrayage, freins, circuit electrique |

### 2. Lire les voyants du tableau de bord

Les voyants sont le premier niveau de diagnostic embarque. Leur couleur indique l'urgence :
- Rouge : arret immediat obligatoire (huile, temperature, frein)
- Orange : attention requise rapidement (moteur, ABS, FAP)
- Jaune/vert : information (entretien, assistance parking)

Un voyant orange moteur (check engine) indique une anomalie enregistree dans le calculateur. La lecture des codes OBD avec un scanner (protocole OBD2 depuis 2001) permet d'identifier le defaut exact.

### 3. Scanner le code OBD (P, C, B, U)

Les codes OBD se lisent avec un scanner OBD2 (disponibles a partir de 30 EUR) :
- P0xxx : moteur et transmission
- C0xxx : chassis (ABS, ESP)
- B0xxx : carrosserie (airbags, sieges)
- U0xxx : reseau de communication

## Les 10 signes avant-coureurs d'une panne

1. **Bruit inhabituel au freinage** — sifflement aigu = plaquettes usees, grincement = disques ou etrier
2. **Voyant moteur allume** — code OBD a lire dans les 48h
3. **Vibration au volant** — a vitesse constante : pneumatiques ; au freinage : disques voiles
4. **Demarrage difficile** — lent, bruyant ou manque = batterie, demarreur ou alternateur
5. **Surconsommation soudaine** — injecteurs, bougie, fuite circuit d'alimentation
6. **Fumee a l'echappement** — blanche = liquide de refroidissement ; noire = richesse essence ; bleue = huile
7. **Perte de puissance** — turbo, FAP obstrue, injecteurs defaillants
8. **Odeur de brule** — embrayage en patinage, frein grippe, court-circuit electrique
9. **Pedale de frein molle** — fuite liquide de frein, plaquettes usees extremes
10. **Voyant ABS ou ESP** — capteur de roue, bloc hydraulique

## Panne mecanique vs electrique : comment distinguer

| Critere | Mecanique | Electrique |
|---------|-----------|------------|
| Manifestation | Progressive, sonore, vibratoire | Soudaine, voyant allume |
| Temperature | Souvent liee a la montee en temperature | Independante |
| Diagnostic | Inspection visuelle, ecoute | Scanner OBD indispensable |
| Exemples | Usure plaquettes, joint HS, courroie | Capteur O2, calculateur, alternateur |

## Que faire en cas de panne sur autoroute ?

**Priorite absolue : securiser le vehicule et les occupants.**

1. Allumer les feux de detresse immediatement
2. Se garer sur la bande d'arret d'urgence (BAU), le plus a droite possible
3. Couper le moteur et serrer le frein a main
4. Sortir du vehicule par la droite et s'eloigner de la glissiere
5. Revetir le gilet de securite (obligatoire)
6. Poser le triangle de signalisation a 150m minimum (si possible sans danger)
7. Appeler le 3477 (societe d'autoroute) depuis une borne d'appel orange ou votre telephone

**Ne jamais tenter de reparer sur la BAU.** Appelez le prestataire agree de l'autoroute.

## FAQ : Identifier sa panne auto

### Comment savoir quel est le probleme de ma voiture ?
Commencez par observer les symptomes : voyants allumes, bruits, vibrations, odeurs. Si un voyant moteur est allume, lisez le code OBD avec un scanner. Pour les pannes sans voyant, decrivez le symptome (canal sensoriel + moment d'apparition) dans notre outil de diagnostic.

### Comment identifier une panne de demarreur ?
Un demarreur defaillant se manifeste par un clic unique sans demarrage (relais de demarrage), un grincement de courte duree, ou une absence totale de reaction moteur alors que la batterie est chargee. Le diagnostic se confirme en mesurant la tension aux bornes du demarreur lors de la sollicitation.

### Qu'est-ce qu'une panne voyant ABS ?
Le voyant ABS orange indique une defaillance du systeme antiblocage. Le freinage normal reste fonctionnel mais l'assistance ABS est desactivee. Cause la plus frequente : capteur ABS de roue defaillant (50-80 EUR la piece). Ne pas ignorer : rouler sans ABS est legalement autorise mais deconseille.

### Comment lire un code panne voiture ?
Branchez un scanner OBD2 sur le port OBD situe sous le tableau de bord (cote conducteur, generalement sous la colonne de direction). Selectionnez "Lire les codes defaut". Le code P0xxx s'interprete via notre outil ou des bases specialisees. Effacez le code seulement apres reparation.

### Voiture en panne qui ne demarre pas : par ou commencer ?
Verifiez dans cet ordre : 1) Batterie (tension > 12.4V), 2) Demarreur (bruit de clic = OK cote relais), 3) Bobines et bougies (si moteur tourne mais cale), 4) Circuit d'alimentation (pompe a carburant). Un diagnostic OBD indique souvent la piste exacte.

### Panne mecanique ou electrique : comment savoir ?
Une panne mecanique est generalement progressive et s'accompagne de bruits ou vibrations. Une panne electrique est souvent soudaine avec voyant allume. L'outil de diagnostic OBD lit les defauts electroniques ; une inspection physique confirme les pannes mecaniques.

### Que faire si un voyant rouge s'allume en conduisant ?
Un voyant rouge impose l'arret immediat securise du vehicule (huile moteur, temperature moteur, frein). Garez-vous des que possible en securite, coupez le moteur, et n'attendez pas que la situation empire. Relancer un moteur surchauffe ou en manque de pression d'huile cause des dommages irreversibles.

<!-- materialized-from-db guides/selecteur-vehicule-pieces-auto.md 2026-02-17 -->
### Guide - Sélecteur de véhicule pièces auto : 4 méthodes

# Sélecteur de véhicule pièces auto : 4 méthodes pour trouver la bonne pièce

Chaque véhicule a des spécifications techniques uniques : dimensions de disques, type de fixation, connecteurs électriques. Commander une pièce incompatible peut entraîner un montage impossible, un dysfonctionnement ou un danger. Le sélecteur de véhicule pièces auto garantit que seules les pièces compatibles avec votre véhicule vous sont proposées parmi les 4 millions de références du catalogue Automecanik.

4 méthodes disponibles : plaque d'immatriculation, numéro VIN, sélection manuelle (marque/modèle/motorisation), ou référence OEM.

## Mots-clés et expressions SEO

### Intention informationnelle
- comment trouver pièce auto compatible avec mon véhicule
- comment être sûr de commander la bonne pièce auto
- comment savoir le type de motorisation de ma voiture
- c'est quoi F1 F2 F3 sur une carte grise
- quelle est la différence entre type mine et code moteur
- où trouver le numéro VIN de mon véhicule
- quelle est la différence entre pièce d'origine et pièce équipementier
- où trouver un logiciel de vue éclatée automobile gratuit
- comment trouver la référence d'une pièce auto
- mon véhicule a des variantes de montage : comment choisir la bonne pièce

### Intention commerciale
- sélecteur de véhicule pièces auto
- configurateur de pièces auto en ligne
- pièce auto avec carte grise
- numéro VIN 17 caractères pièces auto
- guide pratique choisir pièces auto
- sélection des pièces détachées par modèle de voiture
- information voiture avec plaque d'immatriculation gratuit

### Intention transactionnelle
- recherche pièces auto par plaque d'immatriculation
- trouver pièce auto avec numéro de châssis
- chercher pièce détachée par référence OEM
- trouver code moteur avec VIN gratuit
- trouver numéro OEM avec VIN gratuit

### Intention navigationnelle
- Automecanik sélecteur véhicule
- Automecanik recherche par immatriculation
- Automecanik recherche par VIN

## Les 4 méthodes d'identification

### 1. Par immatriculation (la plus rapide)

Saisissez votre numéro de plaque au format SIV (AA-123-BB) ou ancien format FNI. Le système identifie automatiquement votre véhicule en quelques secondes. C'est la recherche de pièces auto par plaque d'immatriculation la plus rapide pour les plaques françaises.

**Ce qu'il faut** : plaque française (SIV ou FNI)
**Fiabilité** : bonne (si la base est à jour)
**Limitation** : les plaques étrangères ne sont pas reconnues
**Recommandé si** : vous êtes sur le véhicule ou vous avez la plaque sous les yeux. Fonctionne aussi avec la carte grise (pièce auto par carte grise).

### 2. Par numéro VIN (la plus fiable)

Saisissez les 17 caractères du VIN (visible sur la carte grise au champ E ou sur le pare-brise côté conducteur). Cette méthode offre 99%+ de fiabilité et identifie la configuration exacte sortie d'usine, y compris pour les véhicules importés.

**Ce qu'il faut** : VIN de 17 caractères (carte grise champ E)
**Fiabilité** : excellente (99%+)
**Limitation** : le VIN n'est pas toujours sous la main
**Recommandé si** : pièces de sécurité (freins, suspension), véhicule importé, ou variantes de montage. Permet aussi de trouver le code moteur avec le VIN gratuitement.

### 3. Sélection manuelle — marque, modèle, motorisation (toujours disponible)

Sélectionnez successivement la marque (champ D.1 de la carte grise), le modèle/génération, l'année (champ B) et la motorisation (champ P.3). En cas de doute entre 2 motorisations proches, utilisez la recherche par VIN.

**Ce qu'il faut** : marque, modèle, année, motorisation
**Fiabilité** : bonne (si la motorisation exacte est sélectionnée)
**Limitation** : doute possible entre motorisations proches
**Recommandé si** : vous connaissez votre véhicule. Fonctionne sans carte grise. Sélection des pièces détachées par modèle de voiture.

### 4. Par référence OEM (la plus précise)

Saisissez le numéro OEM (Origine Équipementier) gravé sur la pièce d'origine pour trouver l'équivalent exact ou les alternatives compatibles chez d'autres fabricants. C'est la méthode pour chercher une pièce détachée par sa référence OEM avec 100% de précision.

**Ce qu'il faut** : numéro OE gravé sur la pièce usagée
**Fiabilité** : maximale (100%)
**Limitation** : nécessite d'avoir la pièce usagée sous les yeux
**Recommandé si** : vous avez le numéro OE de l'ancienne pièce. Permet un remplacement à l'identique garanti et de trouver les équivalences équipementiers.

## Tableau comparatif des méthodes

| Critère | Immatriculation | VIN | Manuelle | OEM |
|---------|-----------------|-----|----------|-----|
| **Fiabilité** | Bonne (si base à jour) | Excellente (99%+) | Bonne (si motorisation exacte) | Maximale (100%) |
| **Vitesse** | Quelques secondes | Quelques secondes | 1-2 minutes | Instantané |
| **Ce qu'il faut** | Plaque française (SIV/FNI) | 17 caractères (carte grise champ E) | Marque, modèle, année, motorisation | Numéro OE (gravé sur la pièce) |
| **Quand l'utiliser** | Commandes courantes | Pièces sécurité, variantes, import | Sans carte grise, véhicule connu | Remplacement à l'identique |
| **Limitation** | Plaques étrangères non reconnues | VIN pas toujours sous la main | Doute entre motorisations proches | Pièce usagée nécessaire |

## Carte grise — champs utiles pour identifier son véhicule

| Champ | Contenu | Utilité pour le sélecteur |
|-------|---------|---------------------------|
| **B** | Date de première immatriculation | Année du véhicule (étape 3 sélection manuelle) |
| **D.1** | Marque du véhicule | Étape 1 sélection manuelle |
| **D.2** | Type mine / variante / version | Identification précise de la version |
| **E** | Numéro VIN (17 caractères) | Méthode VIN — 99%+ de fiabilité |
| **P.3** | Type de carburant (essence, diesel, hybride, électrique, GPL) | Motorisation — étape 4 sélection manuelle |
| **F.1** | Masse en charge maximale techniquement admissible (PTAC) | Dimensionner freinage et suspension |
| **F.2** | PTAC de l'ensemble (véhicule + remorque) | Dimensionner freinage |
| **F.3** | Masse en charge maximale de l'ensemble en service (PTRA) | Dimensionner suspension (amortisseurs, ressorts) |

**Astuce** : prenez votre carte grise en photo avec votre téléphone. Vous aurez toutes les infos sous la main la prochaine fois, même loin du véhicule.

## Variantes de montage

Les constructeurs automobiles utilisent plusieurs fournisseurs pour une même pièce. En cours de production, ils peuvent changer de fournisseur, modifier des spécifications ou ajouter des options.

### Pourquoi les variantes existent

- **Multi-fournisseurs** : un même modèle peut être équipé en première monte par différents équipementiers selon la date et le lieu de fabrication.
- **Évolutions en série** : les constructeurs améliorent les pièces en continu. Un véhicule de début de série peut avoir des spécifications différentes d'un véhicule de fin de série.
- **Options d'usine** : les packs sport, suspensions pilotées ou systèmes Start & Stop modifient les pièces requises.

### Exemples courants de variantes (même véhicule)

| Catégorie | Variante |
|-----------|----------|
| **Freinage** | Diamètre disque 280 vs 288 vs 312 mm, ventilé vs plein |
| **Batterie** | Start & Stop → AGM/EFB obligatoire |
| **Filtration** | Cartouche vs vissé selon moteur |
| **Suspension** | Standard vs sport / pilotée |

### Comment éviter l'erreur

1. Vérifiez les critères clés sur la fiche produit (diamètre, capteur, type de fixation).
2. Privilégiez le VIN quand c'est disponible — 99% de compatibilité.
3. En cas de doute : comparez le numéro OE de l'ancienne pièce avec les références proposées. Le numéro OE = la meilleure confirmation.

## Dépannage

### Mon véhicule n'apparaît pas dans le sélecteur

**Cause probable** : véhicule importé, très récent, ou plaque étrangère non reconnue.
**Solution** : passez en recherche par VIN (champ E de la carte grise). Les véhicules importés depuis l'Allemagne ou la Belgique sont généralement reconnus par VIN même si la plaque ne fonctionne pas.

### J'hésite entre deux motorisations proches

**Cause probable** : le modèle existe avec plusieurs cylindrées ou puissances similaires (ex : 1.5 dCi 90ch vs 110ch).
**Solution** : utilisez le VIN pour identifier la configuration exacte. Sinon, vérifiez le champ P.3 (carburant) et D.2 (type mine) sur votre carte grise.

### Le sélecteur propose plusieurs variantes pour une même pièce

**Cause probable** : le constructeur a utilisé plusieurs fournisseurs ou modifié les spécifications en cours de production.
**Solution** : mesurez la pièce actuelle (diamètre, nombre de trous) ou relevez le numéro OE gravé dessus. Ce numéro est la confirmation la plus fiable.

### La pièce affichée est marquée "compatible" mais je ne suis pas sûr

**Cause probable** : doute sur la variante de montage ou les options du véhicule.
**Solution** : comparez le numéro OE de votre pièce actuelle avec les références propo

[...]
