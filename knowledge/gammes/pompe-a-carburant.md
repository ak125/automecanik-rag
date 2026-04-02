---
category: alimentation
slug: pompe-a-carburant
title: Pompe à carburant
pg_id: 458
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
  role: Acheminer le carburant du reservoir vers le systeme d'injection a basse pression
  must_be_true:
  - alimenter
  - acheminer
  - pomper
  must_not_contain:
  - haute pression
  - injection
  - injecteur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - alimenter
  - acheminer
  - pomper
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
  - ❌ "plus de puissance"
  cost_range:
    min: 29
    max: 224
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE (OES)
  - tier: Adaptable qualite
  - tier: Reconditionne
  - tier: Echange standard
  brands:
    premium:
    - Bosch
    - Delphi
    - Denso
    standard:
    - Pierburg
    - VDO
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Moteur qui refuse de demarrer pas d amorcage
    severity: confort
  - id: S2
    label: Calages repetes a chaud ou en cote
    severity: immobilisation
  - id: S3
    label: A-coups a l acceleration
    severity: confort
  - id: S4
    label: Bruit de gemissement dans le reservoir
    severity: confort
  - id: S5
    label: Perte de puissance en montee
    severity: confort
  - id: S6
    label: Plus de 200 000 km ou reservoir souvent vide
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - remplacement preventif recommande
  quick_checks:
  - 'Observer : moteur qui refuse de demarrer pas d amorcage ?'
  - 'Observer : calages repetes a chaud ou en cote ?'
  - 'Observer : a-coups a l acceleration ?'
  - Bruit de gemissement dans le reservoir ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Moteur qui refuse de demarrer pas d amorcage
  - Calages repetes a chaud ou en cote
  - A-coups a l acceleration
  - Bruit de gemissement dans le reservoir
  - Perte de puissance en montee
  - Plus de 200 000 km ou reservoir souvent vide
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '458'
  intro_title: A quoi sert Pompe à carburant ?
  risk_title: Pourquoi remplacer Pompe à carburant a temps ?
  risk_explanation: '**Pièce HS** - Le pompe à carburant peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le pompe à carburant peut être hors service et nécessiter un remplacement'
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
  - question: Pompe à carburant OE ou adaptable ?
    answer: Les pompes OES (Bosch, Delphi, VDO) sont fiables. Sur diesel haute pression, privilégiez l'OE. Les adaptables
      essence de qualité (Pierburg) fonctionnent bien.
  - question: Comment savoir si ma pompe à carburant est HS ?
    answer: Moteur qui cale ou refuse de démarrer, à-coups à l'accélération, perte de puissance en côte, bruit de gémissement
      dans le réservoir.
  - question: Tous les combien changer la pompe à carburant ?
    answer: Pas de périodicité. Durée de vie 150 000 à 250 000 km. Évitez de rouler réservoir quasi vide (la pompe chauffe).
  - question: Peut-on changer la pompe à carburant soi-même ?
    answer: 'Possible mais attention : accès souvent sous la banquette arrière ou par le dessous. Circuit sous pression, risque
      d''incendie.'
  - question: Quelle erreur éviter avec la pompe à carburant ?
    answer: Ne pas rouler réservoir vide (la pompe s'use). Ne pas oublier le joint de module. Vérifier l'état du filtre dans
      le réservoir.
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
doc_id: df813cd6-9940-594e-87a9-a433f8efc709
content_hash: sha256:092935f81d78e868
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
  _source: boschaftermarket.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_10__m: '10 μm'
    val_100__: '100 %'
    val_95__: '95 %'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    La pompe à carburant est immergé dans le réservoir àcarburant du véhicule,
    est composée d'un corps, d'un capteur de niveau àcarburant qui donne
    l'indication du niveau sur le tableau de bord et d'unmoteur électrique, qui
    pompe le carburant du réservoir et l'envoie à un débitconstant vers le
    système d'alimentation ce qui accélère la circulationdu carburant à travers
    le filtre à carburant . Elle est autorégulatriceet génère un débit et non
    une pression. L'excès du carburantretourne au réservoir via le régulateur de
    pression. En savoir plus : pompe à carburant — définition et rôle mécanique
    🚨 Bruit Pompe à carburant : causes et diagnostic
  S2: >-
    - Des ratés de combustion : des trous d'accélération. - Des démarrages
    difficiles. - Des coupures de moteur. Une pompe à carburant défaillante peut
    créer plusieursproblèmes : - Injecteurs peuventtomber en panne puisqu'il n'y
    a pas suffisamment de carburant. - La pompe injection :débit faible.
    Diagnostic complet : identifier une panne de pompe à carburant
  S3: >-
    La pompe à carburant transfère le carburant du réservoir vers le système
    d'injection à une pression et un débit précis (typiquement 3 à 7 bar pour
    une pompe basse pression essence, jusqu'à 10 bar pour certains systèmes).
    Une pompe sous-dimensionnée ou incompatible provoque des calages à chaud,
    des ratés d'allumage sous charge et une incapacité à atteindre le régime
    plein gaz. La sélection doit se baser sur des critères techniques stricts,
    pas uniquement sur la compatibilité véhicule de base. - Type de montage :
    immergée dans le réservoir ou externe — La majorité des véhicules post-1990
    utilisent une pompe immergée dans le réservoir (groupe de jaugeage),
    lubrifiée et refroidie par le carburant. Les moteurs plus anciens peuvent
    avoir une pompe mécanique entraînée par l'arbre à cames. Ces deux types ne
    sont pas interchangeables. - Pression et débit de la pompe — La pression
    nominale de la pompe doit correspondre exactement aux valeurs prescrites par
    le constructeur (consultables dans la documentation technique). Un écart de
    ±0,5 bar peut provoquer une richesse inadaptée et déclencher un code défaut
    sur l'injection. Le débit minimum (en L/h à pression nominale) est également
    à respecter. - Tension d'alimentation et connectique — Les pompes à
    carburant sont alimentées en 12 V continu. Vérifier que le connecteur
    électrique du nouveau groupe est identique à l'original (type de
    verrouillage, nombre de broches, position). Une adaptation par épissure est
    déconseillée dans le réservoir. - Groupe de jaugeage complet vs pompe seule
    — Sur les véhicules récents, la pompe est montée sur un ensemble avec le
    capteur de niveau (flotteur). Selon l'état du flotteur et de la crépine de
    la pompe existante, il peut être plus judicieux de remplacer le groupe
    complet pour éviter un démontage double. - Compatibilité carburant :
    essence, diesel, E10/E85, GNV — La composition du carburant détermine les
    matériaux internes de la pompe (joints, turbine). Une pompe conçue pour
    l'essence conventionnelle peut se dégrader rapidement avec du SP95-E10 ou du
    superéthanol E85. Vérifier explicitement la compatibilité carburant dans la
    fiche technique du fabricant. - Marque de qualité et homologation — Préférer
    les fabricants OEM ou OE-quality (Bosch, Denso, Pierburg, Delphi, Walbro)
    qui garantissent les pressions et débits mesurés sur banc. Une pompe
    générique sans certification de débit peut sembler fonctionner mais créer
    des problèmes intermittents à chaud ou sous charge. - Marque, modèle, année
    et type de carburant — Ces quatre données sont impératives pour filtrer le
    catalogue et accéder aux références exactes. Indiquer également la cylindrée
    et la puissance moteur : un même véhicule peut avoir reçu des groupes de
    jaugeage différents selon l'équipement (version économique vs sportive).
    Pour aller plus loin : consultez notre guide d'achat pompe à carburant —
    comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Pompe à carburant pour
    connaître les spécifications. - Débranchez la batterie. - Déposez la
    banquette de siège arrière. - Détachez les connecteurs du couvercle
    deréservoir. - Déposez le couvercle de réservoir. - Débranchez le connecteur
    de la jauge deniveau de carburant. - Déposez la pompe à carburant.
  S4_REPOSE: >-
    Le remontage d'une pompe à carburant nécessite des précautions liées à la
    présence de vapeurs d'essence : travailler dans un espace ventilé, à l'écart
    de toute flamme ou étincelle, batterie déconnectée. La pompe est immergée
    dans le réservoir ; un joint de module mal positionné ou un câblage
    incorrectement connecté suffisent à provoquer une fuite ou une panne
    immédiate. - Contrôler la conformité de la pompe neuve — Comparer la pompe à
    carburant neuve avec celle déposée : hauteur totale du module, sens de la
    tête de pompe, position des connexions électriques et du retour de
    carburant. Une pompe de hauteur incorrecte ne jauge pas correctement le
    niveau de carburant. - Remplacer le filtre à carburant intégré — Si le
    module est fourni sans filtre de crépine, monter le filtre à carburant neuf
    sur l'entrée de la pompe avant d'insérer le module dans le réservoir. Un
    filtre encrassé dégrade la durée de vie de la nouvelle pompe. - Vérifier le
    capteur de niveau de carburant — Contrôler le bon fonctionnement du capteur
    de niveau (flotteur et rhéostat) intégré au module. Une jauge défaillante
    doit être remplacée en même temps que la pompe, car l'accès nécessite de
    rouvrir le réservoir. - Positionner le joint de module neuf — Installer le
    joint d'étanchéité neuf du couvercle de réservoir dans sa gorge, proprement
    graissé avec un peu de carburant ou de vaseline. Un joint pincé ou mal
    engagé provoque une fuite de carburant et de vapeurs dans l'habitacle. -
    Introduire la pompe dans le réservoir — Insérer délicatement la pompe à
    carburant dans le réservoir en alignant les repères de positionnement
    angulaire de la tête de module sur le repère de la trappe du réservoir. Ne
    pas forcer : un détrompeur empêche une mauvaise orientation. - Remettre le
    couvercle et verrouiller le bouchon — Remettre en place le couvercle du
    réservoir et visser (ou faire tourner jusqu'au déclic) le bouchon de
    verrouillage dans le sens prescrit (généralement dans le sens des aiguilles
    d'une montre). Vérifier que toutes les encoches sont correctement engagées.
    - Reconnecter les raccords électriques et carburant — Brancher le connecteur
    électrique de la jauge et de la pompe (connecteur unique sur la plupart des
    modules modernes). Reconnecter les conduites d'alimentation et de retour de
    carburant en vérifiant le bon clipsage des raccords rapides. - Reposer la
    banquette arrière et rebrancher la batterie — Remettre en place la banquette
    ou le plancher de coffre. Rebrancher la batterie. Mettre le contact sans
    démarrer plusieurs fois pour amorcer la pompe et monter en pression dans le
    circuit carburant. - Contrôler le démarrage et vérifier l'absence de fuite —
    Démarrer le moteur et laisser tourner au ralenti 2 à 3 minutes. Vérifier
    l'absence d'odeur de carburant dans l'habitacle et l'absence de fuite autour
    du couvercle de réservoir. Contrôler l'affichage correct de la jauge de
    carburant au tableau de bord.
  S5: >-
    Erreurs frequentes avec la pompe a carburant : - Ne pas depressuriser le
    circuit avant intervention — le carburant sous pression gicle a l'ouverture
    des raccords, risque d'incendie- Rouler regulierement en reserve — la pompe
    immergee dans le reservoir utilise le carburant comme refroidissement, en
    reserve elle surchauffe et s'use prematurement- Confondre pompe de gavage et
    pompe haute pression (diesel) — ce sont deux pieces distinctes avec des
    emplacements et des prix differents- Ne pas remplacer le filtre a carburant
    en meme temps — un filtre colmate fait forcer la pompe neuve et reduit sa
    duree de vie- Ignorer des a-coups a l'acceleration ou un demarrage difficile
    a chaud — symptomes classiques d'une pompe a carburant fatiguee- Ne pas
    verifier la tension d'alimentation electrique de la pompe avant remplacement
    — un relais ou un fusible defaillant mime une panne de pompe
  S6: >-
    Après le remplacement d'une pompe à carburant (immergée dans le réservoir ou
    mécanique sur moteur), des contrôles d'amorçage, de pression et d'étanchéité
    doivent être effectués avant toute mise en route prolongée. La pompe
    achemine le carburant du réservoir vers le système d'injection à basse
    pression — une fuite ou un défaut d'amorçage peut provoquer une panne sèche
    immédiate. - Amorçage de la pompe avant démarrage : activer le contact
    plusieurs fois sans démarrer (position "contact" pendant 3 à 5 secondes,
    puis coupure, répéter 3 fois) pour permettre à la pompe de remplir la rampe
    d'injection. Écouter un léger bourdonnement depuis le réservoir à chaque
    activation — son absence indique une pompe non alimentée électriquement ou
    un fusible grillé. - Contrôle de la pression carburant : brancher un
    manomètre sur la rampe d'injection (valeur attendue : 2,5 à 4 bar selon
    moteur essence, vérifier spécification constructeur). Une pression
    inférieure de 20 % à la valeur nominale pointe vers une pompe sous-
    performante ou un régulateur de pression défaillant. - Absence de fuite au
    niveau du bouchon et des raccords : après démarrage, inspecter soigneusement
    le pourtour du bouchon de jauge (bride de fermeture du réservoir), les
    raccords de durites d'entrée et de sortie ainsi que la durite de retour.
    L'odeur de carburant à l'intérieur de l'habitacle ou sous le véhicule impose
    un arrêt immédiat. - Comportement moteur à l'accélération : effectuer
    plusieurs accélérations franches de 0 à 80 km/h. L'absence d'à-coups, de
    ratés ou de chute de régime confirme que la pompe délivre un débit suffisant
    en forte demande. Tout à-coup persistant indique un débit insuffisant en
    charge. - Absence de bruit de gémissement dans le réservoir : à bas régime
    et fenêtres ouvertes, écouter le réservoir. Un bourdonnement fort et continu
    signale une pompe qui aspire à sec (niveau carburant trop bas lors du test)
    ou une crépine d'aspiration partiellement obstruée. - Vérification du filtre
    à carburant : si le filtre n'a pas été remplacé simultanément, contrôler
    qu'il ne présente pas un colmatage excessif susceptible de limiter le débit
    de la pompe neuve. Un filtre encrassé réduit la durée de vie de la pompe de
    façon significative.
  S7: >-
    Quel est le prix d'un pompe à carburant ?Le prix varie selon le véhicule et
    la marque. Utilisez notre sélecteur pour trouver le pompe à carburant
    compatible avec votre véhicule et comparer les tarifs des différents
    équipementiers.Comment savoir si mon pompe à carburant est à changer ?Les
    signes d'usure les plus courants sont détaillés dans la section diagnostic
    ci-dessus. En cas de doute, faites contrôler la pièce par un
    professionnel.Peut-on rouler avec un pompe à carburant défaillant ?Cela
    dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la
    sécurité du véhicule. Consultez la section symptômes pour évaluer l'urgence
    du remplacement.- alimenter - acheminer - pomper
  S8: >-
    Comment choisir Pompe à carburant compatible avec mon vehicule ?Renseignez
    marque, modele, type moteur et annee, puis verifiez la reference Quand
    remplacer Pompe à carburant ?En cas de moteur qui refuse de demarrer pas d
    amorcage ou de degradation Puis-je monter Pompe à carburant sans
    verification atelier ?Le montage peut exiger controles de couple, alignement
    et references.
  META: >-
    {"meta_title":"Pompe à carburant : Conseils diagnostic et remplacement |
    AutoMecanik","meta_description":"Moteur qui cale, gémissement réservoir ou
    perte de puissance ? Découvrez quand changer la pompe à carburant et comment
    choisir entre OE et adaptable."}
---

# Pompe à carburant - Guide Diagnostic Complet

## Fonction et Rôle

Acheminer le carburant du reservoir vers le systeme d'injection a basse pression

**Actions principales:** alimenter, acheminer, pomper

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Calages repetes a chaud ou en cote**
  calages repetes a chaud ou en cote

### 🟢 Autres Symptômes

- moteur qui refuse de demarrer pas d amorcage
- a-coups a l acceleration
- bruit de gemissement dans le reservoir
- perte de puissance en montee
- plus de 200 000 km ou reservoir souvent vide

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à carburant:

1. **Inspection visuelle** - Examiner l'état du pompe à carburant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le pompe à carburant peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-pression-de-carburant
- filtre-a-carburant
- injecteur

## Critères de Compatibilité

Pour commander le bon pompe à carburant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"

## FAQ

**Pompe à carburant OE ou adaptable ?**
Les pompes OES (Bosch, Delphi, VDO) sont fiables. Sur diesel haute pression, privilégiez l'OE. Les adaptables essence de qualité (Pierburg) fonctionnent bien.

**Comment savoir si ma pompe à carburant est HS ?**
Moteur qui cale ou refuse de démarrer, à-coups à l'accélération, perte de puissance en côte, bruit de gémissement dans le réservoir.

**Tous les combien changer la pompe à carburant ?**
Pas de périodicité. Durée de vie 150 000 à 250 000 km. Évitez de rouler réservoir quasi vide (la pompe chauffe).

**Peut-on changer la pompe à carburant soi-même ?**
Possible mais attention : accès souvent sous la banquette arrière ou par le dessous. Circuit sous pression, risque d'incendie.

**Quelle erreur éviter avec la pompe à carburant ?**
Ne pas rouler réservoir vide (la pompe s'use). Ne pas oublier le joint de module. Vérifier l'état du filtre dans le réservoir.
