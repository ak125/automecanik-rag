---
category: alimentation
slug: corps-papillon
title: Boîtier papillon
pg_id: 158
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
  role: Doser la quantite d'air admise dans le moteur en fonction de la position de l'accelerateur
  must_be_true:
  - doser
  - reguler
  - controler
  must_not_contain:
  - carburant
  - injection
  - injecteur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - injecteur
  - pompe-a-injection
  - pompe-a-haute-pression
  - debitmetre-d-air
  - regulateur-de-pression-carburant
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de compatibilite
    pour confirmer Boîtier papillon.
  - Verifier la reference OE ou equivalence constructeur pour le vehicule exact
  - Controler la compatibilite avec le systeme d injection (common rail, TDI, HDi)
  - Choisir un equipementier specialise (Bosch, Delphi, Denso, Siemens VDO)
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "plus de puissance"
  cost_range:
    min: 150
    max: 400
    currency: EUR
    unit: boîtier complet
    source: catalogue automecanik
  brands:
    premium:
    - Bosch
    - Delphi
    - Denso
    standard:
    - Siemens VDO
    - Pierburg
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Ralenti instable ou irregulier
    severity: confort
  - id: S2
    label: Accelerations saccadees ou a-coups
    severity: confort
  - id: S3
    label: Moteur qui cale au demarrage ou au ralenti
    severity: immobilisation
  - id: S4
    label: Sifflement d air au niveau de l admission
    severity: confort
  - id: S5
    label: Odeur d essence melange trop riche
    severity: confort
  - id: S6
    label: Plus de 100 000 km sans nettoyage
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - remplacement preventif recommande
  quick_checks:
  - 'Observer : ralenti instable ou irregulier ?'
  - 'Observer : accelerations saccadees ou a-coups ?'
  - 'Observer : moteur qui cale au demarrage ou au ralenti ?'
  - 'Observer : sifflement d air au niveau de l admission ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Ralenti instable ou irregulier
  - Accelerations saccadees ou a-coups
  - Moteur qui cale au demarrage ou au ralenti
  - Sifflement d air au niveau de l admission
  - Odeur d essence melange trop riche
  - Plus de 100 000 km sans nettoyage
  good_practices:
  - Utiliser du carburant de qualite pour preserver les injecteurs
  - Remplacement du filtre a carburant selon intervalle constructeur
  - Diagnostic electronique (OBD) en cas de perte de puissance
  - Ne pas rouler en reserve de carburant (pompe immergee non lubrifee)
rendering:
  pgId: '158'
  intro_title: A quoi sert Boîtier papillon ?
  risk_title: Pourquoi remplacer Boîtier papillon a temps ?
  risk_explanation: '**Pièce HS** - Le boîtier papillon peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le boîtier papillon peut être hors service et nécessiter un remplacement'
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
  - question: Boîtier papillon OE ou adaptable ?
    answer: Privilégiez l'OE ou OES (Bosch, VDO, Continental). Le boîtier papillon est calibré avec le calculateur. Un adaptable
      peut nécessiter une réadaptation.
  - question: Comment savoir si mon boîtier papillon est HS ?
    answer: Ralenti instable, accélérations saccadées, voyant moteur allumé, perte de puissance, moteur qui cale au démarrage
      ou au ralenti.
  - question: Tous les combien nettoyer le boîtier papillon ?
    answer: Nettoyage conseillé tous les 30 000 à 50 000 km. Plus souvent si petits trajets urbains. Pas de périodicité de
      remplacement fixe.
  - question: Peut-on nettoyer le boîtier papillon soi-même ?
    answer: Oui, avec un spray nettoyant carburateur. Démonter le conduit d'admission, nettoyer le volet et les parois. Attention
      à ne pas forcer le volet.
  - question: Quelle erreur éviter avec le boîtier papillon ?
    answer: Ne pas forcer le volet manuellement sur les boîtiers motorisés. Après nettoyage ou remplacement, une réadaptation
      par valise peut être nécessaire.
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
doc_id: 94577777-70a8-53ce-9cd7-c10fca2b03f0
content_hash: sha256:ab59f67ca60e0d8c
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
  area: Sur le moteur (rampe injection, admission)
  access: Par le dessus (capot)
  adjacent_parts:
  - rampe
  - injecteurs
  - calculateur moteur
  - papillon
installation:
  difficulty: moyen a difficile
  time: 30min a 2h
  tools:
  - cle a douille
  - cle dynamometrique
  - diagnostic OBD
  prerequisite: Depressuriser le circuit carburant avant depose
phase5_enrichment:
  _source: delphiautoparts.com + fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 2
  _has_tech_data: true
  technical_notes:
    val_17_a: '17 a'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le corps papillon estinstallé entre le filtre à air et le collecteur
    d'admission du moteur, sonobjectif est de réguler le flux d'air qui va
    rentrer dans le moteur à traversun clapet d'air mobile pour obtenir un
    rapport air-carburant optimal pour lacombustion du carburant. Le principe de
    fonctionnement est celui d'un voletpivotant qui s'ouvre (plus ou moins) pour
    laisser passer l'air.Selon l'équipement du moteur un corps papillon peut
    être reliémécaniquement à la pédale d'accélérateur via un simple câble ou
    piloté par un mécanismeélectrique qu'est contrôlé par le calculateur
    d'injection, il utilise des capteurs de position de la pédale d'accélérateur
    pour faire fonctionnerle boîtier papillon. En savoir plus : boîtier papillon
    — définition et rôle mécanique 🚨 Bruit Boîtier papillon : causes et
    diagnostic
  S2: >-
    Un corps papillon défectueux présenteplusieurs symptômes : - Surconsommation
    ducarburant. - Allumage du témoin degestion moteur sur le tableau de bord. -
    Des secousses ressentieslors de l'accélération. - Perte de puissance lors
    del'accélération. - Calage du moteur. Un corps papillon HS et qu'il n'est
    pas changé à temps peutendommager plusieurs autres pièces : - Usure des
    injecteurs. - Usure de la vanne EGR . - Usure du FAP. - Usure du catalyseur.
    Diagnostic complet : identifier une panne de boîtier papillon Symptômes
    détaillés et vérifications Un boîtier papillon encrassé ou défaillant
    (parfois appelé corps papillon HS) peut se manifester de plusieurs façons.
    Voici les signaux à surveiller, du plus discret au plus bloquant : - Ralenti
    instable ou irrégulier : le régime moteur oscille au point mort, peut
    indiquer un volet de dosage encrassé ou une valve de ralenti défectueuse. -
    Accélérations saccadées : des à-coups répétés à l'accélération sont souvent
    liés à un capteur de position papillon (TPS) hors tolérance ou à une prise
    d'air parasite sur le conduit d'admission. - Calage moteur au démarrage ou
    au ralenti : symptôme plus sévère indiquant un défaut de dosage
    air/carburant — à traiter en priorité. - Sifflement au niveau de l'admission
    : peut indiquer une fuite d'air en amont ou en aval du boîtier papillon,
    souvent lié à un joint d'étanchéité usé. - Odeur d'essence prononcée : un
    mélange trop riche consécutif à une information erronée du capteur TPS peut
    générer ce symptôme. - Kilométrage élevé sans nettoyage : au-delà de 100 000
    km, un encrassement progressif du volet est probable même sans symptôme
    apparent. Hypothèses à explorer Ces symptômes peuvent indiquer : un
    encrassement du volet papillon, une usure du capteur TPS, un défaut de la
    valve de ralenti, ou une prise d'air sur le circuit d'admission. Un
    diagnostic électronique permet de confirmer l'origine exacte. Vérifications
    non-invasives (à faire soi-même) - Observer le compte-tours au ralenti : une
    oscillation régulière entre 600 et 1 000 tr/min est un indicateur fiable
    d'un problème de corps papillon. - Vérifier la présence d'un voyant moteur
    (codes P0120–P0124 typiquement associés au capteur TPS). - Écouter le
    conduit d'admission moteur tournant : un sifflement ou un chuintement trahit
    une fuite d'air. - Observer la couleur des fumées d'échappement : une fumée
    noire soutenue peut confirmer un mélange trop riche. - Inspecter
    visuellement le boîtier papillon après dépose du conduit d'air : un dépôt
    noir épais sur les parois est le signe d'un encrassement à traiter. Pour un
    diagnostic personnalisé adapté à votre véhicule, utilisez notre outil de
    diagnostic gratuit.
  S3: >-
    Le boîtier papillon (ou corps papillon) régule la quantité d'air admise dans
    le moteur en modulant l'ouverture d'un volet en fonction de la position de
    la pédale d'accélérateur. Sur les moteurs modernes, ce volet est commandé
    électroniquement par un motoréducteur intégré au corps papillon, piloté par
    le calculateur moteur (contrôle-moteur). Un boîtier inadapté — mauvais
    diamètre d'alésage, motoréducteur incompatible, ou capteur de position (TPS)
    non conforme — génère des codes défaut et des à-coups non corrigeables par
    recalibration. Voici les critères déterminants avant toute commande. -
    Diamètre d'alésage du volet papillon — Ce diamètre (exprimé en mm, courant
    entre 50 et 82 mm selon la cylindrée moteur) conditionne le débit d'air
    maximal admissible. Un boîtier avec un alésage de 5 mm de trop génère un
    mélange trop riche à bas régime et perturbe le ralenti. Vérifier ce diamètre
    dans la documentation technique ou le mesurer sur la pièce d'origine. -
    Compatibilité du capteur de position papillon (TPS) — Le capteur de position
    transmet l'angle d'ouverture du volet au calculateur. Certains véhicules
    utilisent un capteur potentiométrique (signal analogique 0–5 V), d'autres un
    capteur Hall (signal numérique). Un boîtier avec un TPS de technologie
    différente sera refusé par le calculateur et génèrera un code P0120 ou
    similaire. - Référence du motoréducteur intégré — Le motoréducteur
    électrique commande le volet. Sa tension nominale (12 V) et son rapport de
    réduction doivent correspondre aux paramètres attendus par le calculateur
    (temps de réponse, couple, angle max). Un motoréducteur trop lent provoque
    des à-coups à l'accélération ; trop rapide, il dépasse les butées mécaniques
    et déclenche le mode dégradé. - Configuration des raccords air (entrée,
    sortie, by-pass) — Comparer le nombre et le positionnement des raccords de
    vide sur le boîtier (recyclage vapeurs d'huile, servos de ralenti, by-pass
    de ralenti). Un raccord obturé ou mal connecté introduit une fuite d'air non
    mesurée par le débitmètre, ce qui dérègle le mélange air-carburant. -
    Procédure de recalibration obligatoire après montage — Tout boîtier papillon
    électronique neuf nécessite une procédure d'initialisation à l'outil de
    diagnostic (apprentissage position neutre, butées ouvert/fermé). Sans cette
    étape, le calculateur conserve les valeurs de l'ancien boîtier et le ralenti
    reste instable. Vérifier que votre atelier ou outillage permet cette
    procédure. - Nettoyage ou remplacement : savoir distinguer — Sur certains
    moteurs, le corps papillon encrassé de dépôts de carbone peut être nettoyé
    avec un produit dégraissant spécifique (sans démonter le capteur TPS pour
    éviter le déréglage). Le remplacement complet s'impose en cas de volet
    grippé, de TPS hors-plage, ou de motoréducteur défaillant détecté à
    l'oscilloscope. Pour aller plus loin : consultez notre guide d'achat boîtier
    papillon — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Corps papillon pour
    connaître les spécifications. - >Débranchez la batterie. - Démontez le
    filtre à air si nécessaire pour faciliter l'accès au corps papillon. -
    Localisez l'emplacement du corps papillon. - Desserrez les vis de fixations
    du corps papillon. - Débranchez le connecteur du corps papillon. - Démontez
    le corps papillon.
  S4_REPOSE: >-
    Le remontage du boîtier papillon requiert une attention particulière sur les
    modèles à commande électronique (drive-by-wire) : toute modification de la
    position de repos du volet papillon nécessite une procédure de réadaptation
    par valise de diagnostic. Sans cette procédure, le calculateur applique une
    cartographie incorrecte qui provoque un ralenti instable ou des à-coups à
    l'accélération. - Vérifiez que le corps papillon neuf est identique à celui
    démonté : diamètre d'alésage, position du capteur de position (TPS intégré
    ou séparé), type de connecteur. Sur les boîtiers motorisés, la résistance
    électrique du moteur doit correspondre aux valeurs d'origine. - Remplacez le
    filtre à air si son état le justifie. Un filtre encrassé augmente la
    dépression dans le conduit et accélère l'encrassement du volet papillon
    neuf, en particulier sur les trajets urbains courts. - Contrôlez l'état des
    injecteurs (encrassement des bouts) si le moteur présentait un ralenti
    instable prononcé avant la dépose. Un injecteur qui goutte contamine le
    nouveau boîtier par les retours de carburant vapeur. - Nettoyez
    soigneusement la face de joint du collecteur d'admission où vient s'appuyer
    le boîtier papillon. Éliminez les résidus de l'ancien joint avec un grattoir
    plastique sans rayer l'aluminium. - Posez un joint de corps papillon neuf
    (fourni avec la pièce ou commandé séparément). N'utilisez pas de pâte à
    joint silicone en remplacement : elle s'infiltre dans le conduit d'air et
    obstrue le capteur MAF. - Remontez le corps papillon neuf sur le collecteur.
    Engagez les vis à la main sans forcer. Serrez les vis de fixation au couple
    prescrit (généralement 8 à 12 N·m) en croix pour un appui uniforme sur le
    joint. - Reconnectez le connecteur du corps papillon. Le clip de
    verrouillage doit s'enclencher distinctement. Reconnectez également le tuyau
    de recirculation de vapeurs d'essence (reniflard) s'il était débranché. -
    Remontez le boîtier de filtre à air et les conduits d'admission dans l'ordre
    inverse de la dépose. Vérifiez l'étanchéité de tous les raccords et colliers
    — tout faux air fausse la mesure du débitmètre. - Rebranchez la batterie.
    Démarrez le moteur sans accélérer et laissez-le tourner 5 minutes au
    ralenti. Vérifiez la stabilité du ralenti (doit être stable entre 700 et 850
    tr/min selon moteur). Si le ralenti est instable, effectuez la procédure de
    réadaptation du papillon avec une valise de diagnostic (apprentissage
    position zéro, plage d'ouverture, inactivité électrique 15 minutes puis
    démarrage progressif selon constructeur).
  S5: >-
    Erreurs frequentes avec le boitier papillon : - Ne pas nettoyer le corps
    papillon avant de le remplacer — dans 80% des cas un nettoyage au produit
    dedie suffit a resoudre les problemes de ralenti instable- Oublier de faire
    un reapprentissage du papillon apres remplacement — le calculateur moteur
    doit reapprendre les positions min/max du volet, sinon le ralenti est
    instable- Confondre un probleme de capteur de position avec un defaut
    mecanique du papillon — lire les codes defaut avant de remplacer la piece-
    Ne pas verifier l'etat du filtre a air — un filtre colmate laisse passer des
    poussieres qui encrassent le papillon- Debrancher le connecteur electrique
    moteur tournant — risque de destruction du capteur de position par
    surtension
  S6: >-
    Le boîtier papillon électronique nécessite une procédure de réinitialisation
    après son remplacement. Sans cette étape, le calculateur moteur conserve les
    valeurs d'apprentissage de l'ancien boîtier et le ralenti reste instable ou
    le moteur peut caler. Voici les contrôles à effectuer dans l'ordre. -
    Réinitialiser les valeurs d'adaptation du calculateur : avec un outil de
    diagnostic OBD, effacer les codes défaut mémorisés et lancer la procédure de
    réinitialisation du papillon (throttle body reset). Sur certains véhicules,
    couper le contact 30 secondes suffit ; sur d'autres, une procédure
    spécifique par outil est requise. - Effectuer la procédure d'apprentissage
    du ralenti : démarrer le moteur à froid et le laisser monter en température
    au ralenti sans actionner l'accélérateur pendant au moins 3 minutes. Le
    calculateur apprend la position zéro du papillon et calibre le ralenti cible
    (généralement 750 à 900 tr/min selon le moteur). - Vérifier la stabilité du
    ralenti à chaud : le ralenti ne doit pas osciller de plus de ±50 tr/min une
    fois le moteur à température. Des oscillations continues indiquent que
    l'apprentissage est incomplet ou que le joint d'entrée d'air du boîtier
    fuit. - Contrôler l'absence de sifflement d'air : inspecter les colliers de
    serrage et le joint torique du boîtier papillon. Toute fuite d'air entre le
    boîtier et la tubulure d'admission fausse la mesure du débitmètre et génère
    un mélange air/carburant incorrect. - Tester les accélérations progressives
    : augmenter progressivement le régime moteur de 800 à 3 000 tr/min. La
    réponse doit être linéaire et sans à-coups. Des saccades persistent
    signalent soit un mauvais apprentissage, soit un capteur de position
    papillon (TPS) défectueux sur la pièce neuve. - Vérifier l'absence de code
    défaut résiduel : après 15 minutes de conduite incluant plusieurs
    accélérations franches, brancher l'outil OBD et confirmer qu'aucun code
    P0120 à P0124 (capteur position papillon) ni P0506/P0507 (ralenti hors
    plage) n'est présent. - Contrôler la consommation de carburant : un boîtier
    papillon neuf mal calibré produit un mélange trop riche (odeur d'essence) ou
    trop pauvre (claquements). Comparer la consommation sur les 100 premiers km
    avec les valeurs habituelles du véhicule.
  S7: >-
    Quel est le prix d'un boîtier papillon ?Le prix varie selon le véhicule et
    la marque. Utilisez notre sélecteur pour trouver le boîtier papillon
    compatible avec votre véhicule et comparer les tarifs des différents
    équipementiers.Comment savoir si mon boîtier papillon est à changer ?Les
    signes d'usure les plus courants sont détaillés dans la section diagnostic
    ci-dessus. En cas de doute, faites contrôler la pièce par un
    professionnel.Peut-on rouler avec un boîtier papillon défaillant ?Cela
    dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la
    sécurité du véhicule. Consultez la section symptômes pour évaluer l'urgence
    du remplacement.- capteur position papillon - capteur de cognement - capteur
    temperature d air admission - corps papillon - injecteur - valve de reglage
    du ralenti
  S8: >-
    Comment choisir Boîtier papillon compatible avec mon vehicule ?Renseignez
    marque, modele, type moteur et annee, puis verifiez la reference Quand
    remplacer Boîtier papillon ?En cas de ralenti instable ou irregulier ou de
    degradation mesurable, Puis-je monter Boîtier papillon sans verification
    atelier ?Le montage peut exiger controles de couple, alignement et
    references.
  META: >-
    {"meta_title":"Boîtier papillon : ralenti instable et nettoyage |
    AutoMecanik","meta_description":"Ralenti irrégulier, accélérations
    saccadées, moteur qui cale : diagnostiquer un boîtier papillon encrassé ou
    HS et savoir quand nettoyer ou le remplacer.","og_title":"Boîtier papillon
    encrassé : ralenti instable et à-coups","og_description":"Ralenti instable,
    moteur qui cale ou accélérations saccadées ? Le boîtier papillon dose l'air
    moteur. Guide pour nettoyer ou remplacer la
    pièce.","sources":[{"type":"rag","ref":"gammes/corps-
    papillon.md","field":"diagnostic.symptoms,domain.role,rendering.faq"}]}
---

# Boîtier papillon - Guide Diagnostic Complet

## Fonction et Rôle

Doser la quantite d'air admise dans le moteur en fonction de la position de l'accelerateur

**Actions principales:** doser, reguler, controler

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Moteur qui cale au demarrage ou au ralenti**
  moteur qui cale au demarrage ou au ralenti

### 🟢 Autres Symptômes

- ralenti instable ou irregulier
- accelerations saccadees ou a-coups
- sifflement d air au niveau de l admission
- odeur d essence melange trop riche
- plus de 100 000 km sans nettoyage

## Procédure de Diagnostic

Pour diagnostiquer un problème de boîtier papillon:

1. **Inspection visuelle** - Examiner l'état du boîtier papillon
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le boîtier papillon peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-position-papillon
- capteur-de-cognement
- capteur-temperature-d-air-admission
- corps-papillon
- injecteur
- valve-de-reglage-du-ralenti

## Critères de Compatibilité

Pour commander le bon boîtier papillon, vous devez connaître:

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

**Boîtier papillon OE ou adaptable ?**
Privilégiez l'OE ou OES (Bosch, VDO, Continental). Le boîtier papillon est calibré avec le calculateur. Un adaptable peut nécessiter une réadaptation.

**Comment savoir si mon boîtier papillon est HS ?**
Ralenti instable, accélérations saccadées, voyant moteur allumé, perte de puissance, moteur qui cale au démarrage ou au ralenti.

**Tous les combien nettoyer le boîtier papillon ?**
Nettoyage conseillé tous les 30 000 à 50 000 km. Plus souvent si petits trajets urbains. Pas de périodicité de remplacement fixe.

**Peut-on nettoyer le boîtier papillon soi-même ?**
Oui, avec un spray nettoyant carburateur. Démonter le conduit d'admission, nettoyer le volet et les parois. Attention à ne pas forcer le volet.

**Quelle erreur éviter avec le boîtier papillon ?**
Ne pas forcer le volet manuellement sur les boîtiers motorisés. Après nettoyage ou remplacement, une réadaptation par valise peut être nécessaire.
