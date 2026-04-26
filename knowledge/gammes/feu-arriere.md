---
category: eclairage
slug: feu-arriere
title: Feu arrière
pg_id: 290
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
  role: Signale la présence et les actions du véhicule
  must_be_true:
  - signaler
  - indiquer
  - eclairer
  must_not_contain:
  - injection
  - freinage
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - ampoule-feu-avant
  - ampoule-feu-arriere
  - feu-avant
  - phares-antibrouillard
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
  - ❌ "sécurité maximale"
  cost_range:
    min: 50
    max: 250
    currency: EUR
    unit: bloc complet
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    description: Pièce identique à celle montée en usine. Fit parfait, homologation E garantie.
  - tier: Équivalent OE (OES)
    description: Fabricants comme Valeo, Hella ou Magneti Marelli fournissent souvent les constructeurs en premier montage.
      Qualité identique à l'OE.
  - tier: Adaptable (aftermarket)
    description: Fabricants spécialisés dans l'éclairage aftermarket. Rapport qualité/prix acceptable pour usage standard.
  brands:
    premium:
    - Osram
    - Philips
    standard:
    - Bosch
    - Hella
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Arriere allume plus cote stop
    severity: confort
  - id: S2
    label: Buee visible interieur bloc optique
    severity: confort
  - id: S3
    label: Ampoule qui grille frequemment probleme de masse
    severity: confort
  - id: S4
    label: Controle technique refuse pour feux defaillants
    severity: confort
  - id: S5
    label: Plus de 10 ans sans verification des connecteurs
    severity: confort
  - id: S6
    label: Bruit crissement electrique niveau arriere
    severity: confort
  - id: S7
    label: Feux inefficaces car tres faibles a l allumage
    severity: confort
  - id: S8
    label: Odeur plastique surchauffe niveau feux
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : arriere allume plus cote stop'
  quick_checks:
  - 'Observer : arriere allume plus cote stop ?'
  - 'Observer : buee visible interieur bloc optique ?'
  - 'Observer : ampoule qui grille frequemment probleme de masse ?'
  - 'Observer : controle technique refuse pour feux defaillants ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Arriere allume plus cote stop
  - Buee visible interieur bloc optique
  - Ampoule qui grille frequemment probleme de masse
  - Controle technique refuse pour feux defaillants
  - Plus de 10 ans sans verification des connecteurs
  - Bruit crissement electrique niveau arriere
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '290'
  intro_title: A quoi sert Feu arrière ?
  risk_title: Pourquoi remplacer Feu arrière a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
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
  - question: Feu arrière OE, OES ou adaptable ?
    answer: Les feux OES (Valeo, Hella, Magneti Marelli) sont de qualité équivalente à l'OE. Les adaptables (TYC) offrent
      un bon rapport qualité/prix. Vérifiez l'homologation E.
  - question: Comment savoir si mon feu arrière est HS ?
    answer: Fissure ou casse visible, buée à l'intérieur, ampoules qui grillent souvent, plastique jauni ou opaque, contrôle
      technique refusé.
  - question: Tous les combien changer le feu arrière ?
    answer: Pas de périodicité. Le feu arrière se change uniquement si cassé, fissuré ou défaillant. Durée de vie normale
      = vie du véhicule.
  - question: Peut-on changer un feu arrière soi-même ?
    answer: Oui, opération simple. Ouvrir le coffre, accéder par l'intérieur, dévisser les fixations, débrancher le connecteur,
      retirer le bloc. 15-30 min par côté.
  - question: Quelle erreur éviter avec le feu arrière ?
    answer: Vérifier que le joint d'étanchéité est bien en place. Ne pas serrer excessivement (risque de casse). Tester toutes
      les fonctions après montage.
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
doc_id: b734bd5d-6191-5c78-ada6-25d7f722ff16
content_hash: sha256:f172d301e4a4c2d4
lang: fr
variants:
- name: Ampoule halogene
  aliases:
  - halogene
  - H1
  - H4
  - H7
  functional_differences:
  - Standard, economique
  - Remplacement simple
- name: Ampoule LED
  aliases:
  - LED
  functional_differences:
  - Duree de vie superieure
  - Consommation reduite
  - Verifier homologation
location_on_vehicle:
  area: Face avant, arriere et laterale du vehicule
  access: Par le compartiment moteur (avant) ou coffre (arriere)
  adjacent_parts:
  - optique
  - ampoule
  - connecteur
  - reflecteur
installation:
  difficulty: facile
  time: 5 a 15 min
  tools:
  - tournevis
  - gants (ne pas toucher ampoule halogene)
  prerequisite: Moteur eteint, acces par compartiment moteur ou coffre
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'plein'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_110_mm: '110 mm'
    val_120_mm: '120 mm'
    val_13_a: '13 a'
    val_187_v: '187 v'
    val_2_a: '2 a'
    val_20_km: '20 km'
    val_24_a: '24 a'
    val_29_a: '29 a'
    val_3_a: '3 a'
    val_30_km: '30 km'
    val_365_a: '365 a'
    val_365_v: '365 v'
    val_45_km: '45 km'
    val_5_km: '5 km'
    val_90_mm: '90 mm'
  materials:
  - materiau: 'aluminium'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Les feux arrièreappartiennent à l'équipement d'éclairage de l'automobile.
    Ils sont situés à lapartie arrière de la voiture sur la partie postérieure
    de la carrosserie. Leursrôle est de permettre de signaler la présence d'un
    véhicule pour les usagers dela route qui sont derrière votre véhicule. Ils
    signalent aussi les intentionsaux autres conducteurs par exemple si vous
    allez freinez ou changez dedirection. Chaque véhicule est équipé de deux
    feux arrière, qui se composent deplusieurs ampoules, chacune est destinée à
    illuminer un des miroirs et desréflecteurs associés par exemple aux
    veilleuses, aux clignotants, auxindicateurs de recul et aux stops de votre
    voiture selon l'équipement de chaquevéhicule. Les feux de stop : La plupart
    des véhicule sont équipés de3 feux de stop 2 de ces feux se retrouvent
    généralement sous les feux deposition situé dans les feux arrière, et le
    3éme prend la forme d'une barrelumineuse rouge située en haut ou en bas du
    pare-brise arrière (suivant leniveau d'équipement du véhicule).Lorsque le
    conducteurappuie sur sa pédale de frein, l'interrupteur des feux de frein se
    ferme et allume lesfeux de stop pour signaler donc aux autres conducteurs
    son intention deralentir ou d'arrêter le véhicule. Les feux de recul :
    Chaque véhicule est équipéde deux feux de recul qui sont placés dans les
    feux arrière (à gauche et àdroite). Ils s'allument lors véhicule d'une
    manœuvre de recul. Ils vont signalés auxautres conducteurs que la voiture
    d'avant va reculer, et éclaire la zone dans laquelleil s'apprête à reculer.
    Note : Si le véhicule ne compte qu'un seul feu derecul, celui-ci sera situé
    du côté droit de la voiture. Les catadioptres rouges : ce sont 2
    dispositifsréfléchissants rouges, leurs rôle est de refléter au conducteur
    lalumière des feux avant de la voiture, ce qui va permettre de signaler
    àl'usager de l'autre automobile la présence d'un autre véhicule devant lui
    mêmesi les feux de position de celle de devant ne sont pas allumés. Les feux
    de position : cetype d'éclairage est utilisé dans des situations de faible
    visibilité, ilsservent pour être vu par les usagers de la route, mais ils ne
    produisent pas unéclairage suffisant pour conduire de nuit ou en cas de
    mauvaise visibilité. Ilssont représentés sur le tableau de bord par un
    symbole d'ampoule vert et ilsont une couleur rouge à l'arrière. En savoir
    plus : feu arrière — définition et rôle mécanique 🚨 Bruit Feu arrière :
    causes et diagnostic
  S2: >-
    Un feu arrièredéfectueux présente plusieurs symptômes : - Manque d'éclairage
    lors de l'utilisation des feux arrière. - Lors d'un contrôle visuel vous
    remarquez que le feu arrière est fissuré. - Lors d'un contrôle visuel vous
    remarquez que le feu arrière est opaque. Un feu arrière HS etqu'il n'est pas
    remplacé à temps peut causer des risques d'accidents lors del'utilisation de
    la route et le refus de votre véhicule lors du contrôletechnique. Diagnostic
    complet : identifier une panne de feu arrière
  S3: >-
    Choisir un feu arrière adapté à son véhicule demande de vérifier plusieurs
    paramètres techniques avant de passer commande. Un bloc optique mal
    référencé peut refuser de se connecter aux connecteurs d'origine, provoquer
    des erreurs électriques ou être refusé au contrôle technique pour non-
    conformité au Code de la route. Les critères ci-dessous permettent
    d'identifier la pièce correcte dès le premier achat. - Référence
    constructeur et position (gauche/droit) — Les feux arrière sont spécifiques
    au côté du véhicule : un feu gauche n'est jamais interchangeable avec un feu
    droit. Relevez la référence OEM inscrite sur le bloc optique d'origine ou
    dans la documentation technique du véhicule pour garantir une correspondance
    exacte. - Marque, modèle, année de fabrication et type de carrosserie — Un
    même modèle peut exister en berline, break ou monospace avec des géométries
    de blocs optiques différentes. L'année de fabrication est déterminante car
    les constructeurs appliquent fréquemment des restylages en milieu de cycle
    qui modifient la forme du feu sans changer le modèle commercial. - Type de
    technologie d'éclairage — Vérifiez si le véhicule d'origine est équipé de
    feux à ampoules classiques (W16W, P21W, P21/5W), à LED ou à technologie
    OLED. Le remplacement doit respecter la même technologie : monter un kit LED
    à la place d'une ampoule conventionnelle peut déclencher des codes défaut
    sur les véhicules dotés d'un contrôle de circuit d'éclairage. - Connecteur
    et nombre de broches — Les connecteurs arrière varient selon les générations
    : 7 broches, 13 broches ou connecteurs spécifiques avec pilotage CAN-bus. Un
    connecteur non compatible rend le montage impossible sans modification du
    faisceau d'origine, ce qui engage la responsabilité lors d'un contrôle
    technique. - Présence ou absence de fonctions intégrées — Certains blocs
    optiques intègrent plusieurs fonctions dans un seul boîtier : stop, recul,
    antibrouillard et clignotant. Vérifiez le schéma de câblage d'origine pour
    ne pas omettre une fonction au remplacement, notamment l'antibrouillard
    arrière et le feu de recul. - Étanchéité et indice IP — Un bloc optique
    défaillant peut présenter une buée intérieure persistante, signe d'un joint
    périmétrique détérioré. Lors du remplacement, privilégiez les pièces avec
    joint d'étanchéité prémonté et un indice IP67 minimum pour les véhicules
    exposés à des conditions humides. - Origine de la pièce : OEM, équipementier
    première monte, adaptable — Évitez les termes "universel", "tous modèles" ou
    "adaptable" : ils indiquent que la pièce ne reprend pas les cotes exactes du
    constructeur. Privilégiez les références d'équipementiers homologués E-Mark
    (marque CE spécifique éclairage) pour garantir la conformité au contrôle
    technique. Pour aller plus loin : consultez notre guide d'achat feu arrière
    — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Feu arrière pour connaître
    les spécifications. Note : la méthodede remplacement d'un feu arrière change
    d'un véhicule à un autre selon laposition de votre feu arrière. - Débranchez
    la batterie. - Retirez le tapis de la malle arrière pour faciliter le
    travail (sinécessaire). - Démontez le cache de protection du feu arrière si
    équipé. - Débranchez les connecteurs du feu arrière. - Localisez les
    différentes fixations du feu arrière. - Desserrez les fixations du feu
    arrière. - Démontez le feu arrière avec précaution.
  S4_REPOSE: >-
    Le remontage d'un feu arrière ne prend que 15 à 30 minutes, mais deux
    erreurs sabotent le résultat : un joint d'étanchéité mal reposé qui laisse
    entrer l'humidité (buée dans l'optique sous 6 mois) et des fixations serrées
    trop fort qui cassent les pattes de la coque. Procédez méthodiquement. -
    Vérifiez que le feu arrière neuf est identique à celui déposé : référence,
    côté (gauche ou droit), type de technologie (ampoule classique ou LED).
    Testez les ampoules existantes ou montez des ampoules neuves avant de poser
    le bloc. - Contrôlez l'état du joint d'étanchéité périphérique : s'il est
    collé, écrasé ou craquelé, remplacez-le. Un joint défaillant laisse entrer
    l'eau dans la carrosserie et provoque de la corrosion. - Nettoyez le
    logement de feu dans la carrosserie : retirez les éventuelles traces de
    rouille superficielle, les débris de phares cassés et séchez le logement si
    humide. - Reconnectez le connecteur électrique du feu arrière avant la mise
    en place du bloc optique. Vérifiez le verrouillage au déclic. Sur certains
    modèles, le connecteur est inaccessible une fois le feu posé. - Engagez le
    feu arrière dans son logement en commençant par les ergots ou les goujons de
    positionnement. Appuyez uniformément pour ne pas déformer la coque. - Serrez
    les vis ou écrous de fixation à la main en premier lieu, puis au couple
    modéré (généralement 5 à 8 N·m) — ne serrez jamais à l'impact sur un feu
    arrière en matière plastique. - Remontez le cache de protection ou de coffre
    (garniture intérieure) en repositionnant les clips. Tirez légèrement sur la
    garniture pour confirmer que tous les clips sont encliquez. - Rebranchez la
    batterie (borne positive en premier) et testez toutes les fonctions : feux
    de position, stop, clignotant, feu de recul et feu de brouillard arrière le
    cas échéant. - Vérifiez la continuité de masse si une ampoule reste faible
    ou clignote anormalement : nettoyez le plot de masse avec du papier de verre
    fin et reserrez la vis de masse. ✅ Après remontage, vérifiez les
    spécifications dans la fiche technique Feu arrière.
  S5: >-
    Erreurs frequentes avec les feux arriere : - Ne pas verifier le cote
    d'assemblage (gauche/droite) avant achat — les feux arriere ne sont pas
    symetriques sur la plupart des vehicules- Forcer le clip ou les vis de
    fixation — le plastique du feu ou de la carrosserie casse et l'etancheite
    est perdue- Oublier de verifier l'etat des joints d'etancheite — un joint
    use laisse entrer l'humidite qui provoque de la buee et corrode les
    contacts- Ne pas tester toutes les fonctions apres montage (stop, position,
    clignotant, recul, antibrouillard) — un mauvais contact est frequent sur les
    connecteurs multi-broches- Confondre feu arriere interieur (hayon) et
    exterieur (aile) — les references et connectiques different- Ignorer un feu
    casse apres un choc arriere — la structure interne peut etre endommagee meme
    si le verre semble intact, et c'est un motif de contre-visite
  S6: >-
    Après le montage du nouveau feu arrière, vérifiez chaque fonction lumineuse
    individuellement et contrôlez l'absence de défauts électriques avant de
    reprendre la route.- Activation de toutes les fonctions du feu — Testez
    successivement : feu de position (contacteur sur 1), feu de stop (appui
    pédale de frein), feu de recul (marche arrière engagée), clignotant (levier
    de direction). Chacune doit s'allumer sans retard ni scintillement.-
    Symétrie droite/gauche — Comparez l'intensité lumineuse du feu remplacé avec
    son homologue de l'autre côté. Une différence notable de luminosité indique
    un problème de contact de masse ou une ampoule de mauvaise référence.-
    Absence de buée à l'intérieur du bloc optique — Après 10 à 15 minutes de
    fonctionnement avec les feux allumés, aucune condensation ne doit apparaître
    à l'intérieur du bloc. De la buée révèle un joint périphérique mal
    positionné ou endommagé lors du montage.- Contrôle du témoin d'ampoule
    grillée au tableau de bord — Sur les véhicules équipés d'un système de
    surveillance des ampoules, aucun avertissement ne doit s'allumer. Si le
    témoin s'allume avec toutes les ampoules fonctionnelles, contrôlez la
    résistance de ligne du connecteur (doit être inférieure à 0,5 ohm).-
    Étanchéité du connecteur électrique — Vérifiez que le connecteur est
    correctement enfoncé et que le clip de verrouillage est enclenché. Appliquez
    de la graisse diélectrique sur les broches pour prévenir l'oxydation,
    surtout sur les feux exposés aux projections d'eau.- Fixation mécanique du
    bloc — Serrez les vis de fixation au couple constructeur (généralement 5 à 8
    N.m selon le véhicule). Un bloc mal serré génère des vibrations en roulage
    qui fatiguent les connecteurs et peuvent provoquer des coupures
    intermittentes.- Pas d'odeur de plastique surchauffé — Après 20 minutes de
    fonctionnement, aucune odeur de plastique brûlé ne doit être perceptible.
    Cette odeur signale une ampoule de puissance incorrecte ou un court-circuit
    dans le faisceau interne du bloc.
  S7: >-
    Quel est le prix d'un feu arrière ?Le prix varie selon le véhicule et la
    marque. Utilisez notre sélecteur pour trouver le feu arrière compatible avec
    votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon feu arrière est à changer ?Les signes d'usure les plus
    courants sont détaillés dans la section diagnostic ci-dessus. En cas de
    doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un
    feu arrière défaillant ?Cela dépend de la gravité du dysfonctionnement et du
    rôle de la pièce dans la sécurité du véhicule. Consultez la section
    symptômes pour évaluer l'urgence du remplacement.- signaler - indiquer -
    eclairer
  S8: >-
    Comment choisir Feu arrière compatible avec mon vehicule ?Renseignez marque,
    modele, type moteur et annee, puis verifiez la reference Quand remplacer Feu
    arrière ?En cas de arriere allume plus cote stop ou de degradation
    mesurable, il Puis-je monter Feu arrière sans verification atelier ?Le
    montage peut exiger controles de couple, alignement et references.
  META: >-
    {"meta_title":"Feu arrière : Conseils remplacement et compatibilité |
    AutoMecanik","meta_description":"Stop éteint, buée dans le bloc optique ou
    contrôle technique refusé ? Apprenez quand changer votre feu arrière et
    comment choisir la bonne référence."}
---

# Feu arrière - Guide Diagnostic Complet

## Fonction et Rôle

Signale la présence et les actions du véhicule

**Actions principales:** signaler, indiquer, eclairer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- arriere allume plus cote stop
- buee visible interieur bloc optique
- ampoule qui grille frequemment probleme de masse
- controle technique refuse pour feux defaillants
- plus de 10 ans sans verification des connecteurs
- bruit crissement electrique niveau arriere

## Procédure de Diagnostic

Pour diagnostiquer un problème de feu arrière:

1. **Inspection visuelle** - Examiner l'état du feu arrière
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-arriere
- commande-d-eclairage
- contacteur-de-feu-de-recul
- feu-avant
- feu-clignotant
- interrupteur-des-feux-de-freins

## Critères de Compatibilité

Pour commander le bon feu arrière, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "sécurité maximale"

## FAQ

**Feu arrière OE, OES ou adaptable ?**
Les feux OES (Valeo, Hella, Magneti Marelli) sont de qualité équivalente à l'OE. Les adaptables (TYC) offrent un bon rapport qualité/prix. Vérifiez l'homologation E.

**Comment savoir si mon feu arrière est HS ?**
Fissure ou casse visible, buée à l'intérieur, ampoules qui grillent souvent, plastique jauni ou opaque, contrôle technique refusé.

**Tous les combien changer le feu arrière ?**
Pas de périodicité. Le feu arrière se change uniquement si cassé, fissuré ou défaillant. Durée de vie normale = vie du véhicule.

**Peut-on changer un feu arrière soi-même ?**
Oui, opération simple. Ouvrir le coffre, accéder par l'intérieur, dévisser les fixations, débrancher le connecteur, retirer le bloc. 15-30 min par côté.

**Quelle erreur éviter avec le feu arrière ?**
Vérifier que le joint d'étanchéité est bien en place. Ne pas serrer excessivement (risque de casse). Tester toutes les fonctions après montage.
