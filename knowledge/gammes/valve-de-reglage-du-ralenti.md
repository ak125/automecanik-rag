---
category: capteurs
slug: valve-de-reglage-du-ralenti
title: Valve de réglage du ralenti
pg_id: 1298
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
  last_enriched_by: skill:phase5-vague6
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Reguler le debit d'air au ralenti pour maintenir un regime stable moteur chaud ou froid
  must_be_true:
  - reguler
  - ouvrir
  - fermer
  must_not_contain:
  - capteur
  - sonde
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - reguler
  - ouvrir
  - fermer
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
  - ❌ "corrige la panne"
  cost_range:
    min: 30
    max: 100
    currency: EUR
    unit: vanne
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    description: Valve identique au premier montage. Calibration du moteur pas-à-pas et débit d'air conformes aux paramètres
      du calculateur d'origine.
  - tier: Équivalent OE (OES)
    description: Fabricants comme Bosch, Pierburg ou VDO fournissent ces valves aux constructeurs en première monte. Même
      calibration et même connectique.
  - tier: Adaptable (aftermarket)
    description: Valves aftermarket compatibles. Vérifier le type de connecteur, le nombre de broches et le diamètre du corps
      avant commande.
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
    label: Ralenti instable ou irregulier
    severity: confort
  - id: S2
    label: Regime ralenti trop haut ou trop bas
    severity: confort
  - id: S3
    label: Moteur qui cale au ralenti ou au feu rouge
    severity: immobilisation
  - id: S4
    label: Sifflement ou bruit d aspirtion d air anormal
    severity: confort
  - id: S5
    label: Odeur d essence au ralenti melange trop riche
    severity: confort
  - id: S6
    label: Plus nettoyage boitier papillon
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - 'vehicule immobilise ou symptome critique : verification urgente piece et alimentation'
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  quick_checks:
  - 'Observer : ralenti instable ou irregulier ?'
  - 'Observer : regime ralenti trop haut ou trop bas ?'
  - 'Observer : moteur qui cale au ralenti ou au feu rouge ?'
  - 'Observer : sifflement ou bruit d aspirtion d air anormal ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Ralenti instable ou irregulier
  - Regime ralenti trop haut ou trop bas
  - Moteur qui cale au ralenti ou au feu rouge
  - Sifflement ou bruit d aspirtion d air anormal
  - Odeur d essence au ralenti melange trop riche
  - Plus nettoyage boitier papillon
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '1298'
  intro_title: A quoi sert Valve de réglage du ralenti ?
  risk_title: Pourquoi remplacer Valve de réglage du ralenti a temps ?
  risk_explanation: '**Pièce HS** - Le valve de réglage du ralenti peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le valve de réglage du ralenti peut être hors service et nécessiter un remplacement'
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: Vanne de ralenti OE ou adaptable ?
    answer: Les vannes OES (Bosch, Valeo) sont recommandées. Les adaptables peuvent avoir un débit différent causant des problèmes
      de ralenti.
  - question: Comment savoir si ma vanne de ralenti est HS ?
    answer: Ralenti instable ou trop haut, moteur qui cale au ralenti, régime qui monte et descend seul, voyant moteur avec
      codes P0505-P0509.
  - question: Tous les combien changer la vanne de ralenti ?
    answer: Pas de périodicité. Durée de vie variable selon encrassement. Un nettoyage tous les 50 000 km prolonge sa durée
      de vie.
  - question: Peut-on changer la vanne de ralenti soi-même ?
    answer: Oui, généralement accessible sur le boîtier papillon. Quelques vis, un connecteur. Nettoyage du boîtier recommandé
      en même temps.
  - question: Quelle erreur éviter avec la vanne de ralenti ?
    answer: Essayer le nettoyage avant le remplacement. Vérifier aussi le boîtier papillon et le capteur de position papillon.
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
doc_id: 70e66768-fdc2-57d8-bcb8-8db45dd0bb3f
content_hash: sha256:da9066d2aa5c39a1
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
  _source: contenu LLM — a revalider contre sources OEM
  _validation_status: pending_oem_validation
  _enriched_at: '2026-03-30'
  technical_notes:
    reapprentissage: 'obligatoire apres remplacement — le calculateur doit reapprendre la position de repos'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    La valve de réglage du ralentie peut être soit une électrovanne ou soit un
    moteur pas àpas, elle est située sur le corps papillon ou en parallèle sur
    la tubulure d'admission. Commeson nom l'indique elle permet de réguler
    l'admission d'air dans le moteur lorsquece dernier est au ralenti, pour
    qu'il ne s'étouffe ou ne cale pas. Généralementle régulateur de ralenti
    équipe les moteurs essences. Le régulateur deralenti est commandé par le
    calculateur moteur, qui va permettre l'ajustage dudébit d'air au ralenti.
    Lerégulateur de ralenti fait passer un flux d'air variable selon que le
    ralentis'écarte ou s'approche de sa valeur de référence et il gère aussi le
    débitd'air complémentaire lors des démarrages à froid ou de décélération. En
    savoir plus : valve de réglage du ralenti — définition et rôle mécanique 🚨
    Bruit Valve de réglage du ralenti : causes et diagnostic
  S2: >-
    Une valve de réglage de ralenti défaillante présente plusieurs symptômes : -
    Ralenti moteur instable surtout si le véhicule en arrêtavec un calage du
    moteur. - Le régime ralenti monte dans les tours sans que l'appui sur la
    pédale d'accélérateur. - Le moteur broute lors de la décélération. - Une
    surconsommation decarburant. - Fumée d'échappement. Nous vous conseillons de
    faite un diagnostic approfondisi vous constatez un de ces symptômes par ce
    que d'autres composants peuventêtre à la source d'un régime de ralenti
    instable par exemple l'usure du capteur de position du papillon, une sonde
    lambda usée, un injecteur grippé, un des capteurs d'impulsionest défaillant
    . Un régulateur de ralenti défectueux peut causer plusieurs autres pannes
    dans lemoteur : - Usure du corps papillon. - Usure des injecteurs.
    Diagnostic complet : identifier une panne de valve de réglage du ralenti
  S3: >-
    La valve de réglage du ralenti (aussi appelée vanne IAC ou by-pass d'air)
    dose le débit d'air contournant le papillon fermé pour maintenir un régime
    stable à chaud et à froid, entre 650 et 900 tr/min selon le constructeur.
    Sur les motorisations injection monopoint ou multipoint pré-2005, c'est un
    composant mécatronique critique : une pièce incompatible provoque un calage
    immédiat au feu rouge ou un régime erratique impossible à corriger par
    apprentissage calculateur. - Code moteur et type d'injection — La valve IAC
    est spécifique au type d'injection (monopoint, multipoint, injection
    directe) et au code motorisation (ex. XU10J4RS, N13B16, F4R). Deux moteurs
    de 1,4 L de marques différentes utilisent des valves incompatibles. - Nombre
    de fils du connecteur électrique — Les valves rotatives (type stepper motor)
    utilisent 4 fils ; les valves à obturateur solénoïde utilisent 2 fils. Un
    mauvais nombre de fils rend le remplacement impossible sans modification du
    câblage. - Diamètre du by-pass d'air — L'orifice de by-pass a un diamètre de
    4 à 8 mm selon les applications. Ce diamètre conditionne le débit maximal
    autorisé et ne peut pas être compensé par le calibrage du calculateur. -
    Type de fixation sur le corps papillon — Certaines valves se vissent
    directement sur le corps papillon (2 ou 3 vis) ; d'autres se connectent via
    un tuyau en caoutchouc. Vérifiez l'emplacement exact sur votre boîtier
    papillon avant de commander. - Version nettoyée ou neuve — Les valves IAC
    s'encrassent progressivement en dépôts de calamine et de gomme d'essence.
    Sur les véhicules de plus de 100 000 km, préférez une pièce neuve plutôt
    qu'une pièce reconditionnée dont l'historique de nettoyage est inconnu. -
    Procédure d'apprentissage après montage — La plupart des calculateurs
    nécessitent une procédure d'initialisation du ralenti après remplacement
    (déconnexion batterie 15 min ou procédure OBD). Vérifiez que cette étape est
    réalisable avant de fermer le capot. Pour aller plus loin : consultez notre
    guide d'achat valve de réglage du ralenti — comparatif marques, critères de
    choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Valve de réglage du
    ralenti pour connaître les spécifications. - Débranchez la batterie. -
    Démontez le filtre à air . - Démontez le boîtier dufiltre à air. - Démontez
    la canalisation d'airdu corps papillon. - Déconnectez les connecteursdu
    capteur position papillon et de la valve de réglage du ralenti. - Démontez
    le corps papillons'il le faut pour faciliter l'accès au vis de fixation de
    la valve de réglage du ralenti. Note : si vous n'allez pas déposez le corps
    papillondans ce cas desserrez ces vis de fixation et le tourné légèrement
    jusqu'à avoiraccès aux fixations de la valve de réglage du ralenti. -
    Desserrez les fixations de la valve de réglage du ralenti. - Démontez la
    valve de réglage du ralenti.
  S4_REPOSE: >-
    La repose de la valve de réglage du ralenti nécessite de vérifier
    simultanément l'état du boîtier papillon et du capteur de position papillon,
    car ces trois composants travaillent en synergie directe. Monter une valve
    neuve sur un boîtier encrassé ou un capteur défaillant ne résoudra pas le
    problème de ralenti. - Vérifiez que la valve de réglage du ralenti neuve est
    strictement identique à celle démontée : nombre de voies, diamètre
    d'alésage, type de connecteur électrique (2 ou 3 fils selon le modèle). -
    Profitez de l'accès au boîtier papillon pour le nettoyer intérieurement avec
    un nettoyant papillon en aérosol. Un boîtier encrassé perturbe le débit
    d'air de base et rend le ralenti instable même avec une valve neuve. -
    Inspectez l'état du capteur de position papillon : un capteur usé (codes
    P0120 à P0124) cause des symptômes identiques à une valve défaillante.
    Remplacez-le si des hésitations sont présentes. - Vérifiez l'état du filtre
    à air : un filtre colmaté réduit le débit d'air d'admission et sollicite
    excessivement la valve de ralenti. Remplacez-le si nécessaire. - Nettoyez le
    logement de la valve sur le boîtier papillon avec un chiffon non pelucheux.
    Assurez-vous que le joint torique ou le plan de joint est exempt de résidus
    de l'ancien joint. - Mettez en place la valve de réglage du ralenti neuve en
    orientant correctement le connecteur. N'exercez aucune contrainte de torsion
    sur le corps de la valve lors de la mise en position. - Serrez les vis de
    fixation de la valve uniformément, en étoile si elles sont au nombre de 3 ou
    4, pour éviter de déformer le plan de joint. Le couple de serrage est
    typiquement faible (2 à 4 Nm) : ne pas serrer au choc. - Si le boîtier
    papillon a été déposé, remontez-le en remplaçant son joint d'étanchéité et
    en serrant les fixations au couple préconisé. - Reconnectez les connecteurs
    électriques du corps papillon et de la valve de réglage du ralenti jusqu'au
    déclic caractéristique d'encliquetage. - Remontez la canalisation d'air, le
    boîtier du filtre à air et le filtre à air. Vérifiez l'étanchéité de la
    gaine entre le boîtier filtre et le papillon : une aspiration d'air parasite
    génère un code P0507 (régime ralenti trop élevé). - Rebranchez la batterie.
    Démarrez le moteur à froid et laissez-le atteindre la température de
    fonctionnement normale. Observez la stabilité du ralenti : il doit se
    stabiliser entre 700 et 900 tr/min selon le moteur. Un régime oscillant en
    phase de chauffe peut nécessiter une réinitialisation de l'apprentissage
    papillon via outil de diagnostic.
  S5: >-
    - ❌ "homologué CT - ❌ "sécurité garantie - ❌ "zéro panne - ❌ "garanti à vie
    - ❌ "corrige la panne
  S6: >-
    Après le remplacement ou le nettoyage d'une valve de réglage du ralenti
    (également appelée IAC — Idle Air Control), les vérifications portent sur la
    stabilité du régime moteur dans différentes conditions thermiques et de
    charge. Le calculateur moteur doit aussi être mis en conditions de
    réapprentissage. - Réinitialisation de la mémoire adaptative du calculateur
    : débrancher la borne négative de la batterie pendant 10 minutes après le
    remplacement. Cette opération efface les valeurs d'adaptation apprises avec
    l'ancienne valve et force le calculateur à recalculer les paramètres de
    ralenti avec la pièce neuve. - Vérification du régime au ralenti à froid :
    au premier démarrage après remplacement, le régime moteur froid doit se
    situer entre 900 et 1 200 tr/min selon le moteur (régime de fast-idle pour
    la montée en température). Un régime inférieur à 700 tr/min à froid indique
    que la valve ne s'ouvre pas suffisamment. - Stabilisation du ralenti à chaud
    : moteur à température normale (aiguille stabilisée), le régime de ralenti
    doit se tenir entre 700 et 850 tr/min sans oscillations. Des fluctuations de
    ±150 tr/min ou plus signalent une pollution résiduelle du boîtier papillon à
    nettoyer ou une fuite d'air parasite. - Test de reprise au ralenti après
    coupure charge électrique : allumer climatisation, feux de route et
    chauffage simultanément puis les éteindre. Le régime doit se stabiliser dans
    un délai inférieur à 2 secondes sans chute sous 600 tr/min, qui provoquerait
    un calage. - Contrôle de l'absence de codes défaut : connecter un outil OBD
    et vérifier l'absence de codes P0505 (circuit de commande ralenti) ou
    P0506/P0507 (régime ralenti hors plage). Ces codes persistent parfois dans
    la mémoire de l'ancienne valve et doivent être effacés manuellement. -
    Inspection de l'étanchéité du boîtier papillon : vérifier que le joint
    d'interface entre la valve et le boîtier papillon est correctement
    positionné et qu'aucun sifflement d'air n'est audible au niveau du
    raccordement à chaud, signe d'une fuite d'admission perturbant le mélange
    air/carburant. - Test de coupure moteur et redémarrage : couper et
    redémarrer le moteur 3 fois de suite — le démarrage doit être immédiat à
    chaque fois sans nécessiter d'accélération forcée, confirmant que la valve
    est pleinement opérationnelle.
  S7: >-
    Quel est le prix d'un valve de réglage du ralenti ?Le prix varie selon le
    véhicule et la marque. Utilisez notre sélecteur pour trouver le valve de
    réglage du ralenti compatible avec votre véhicule et comparer les tarifs des
    différents équipementiers.Comment savoir si mon valve de réglage du ralenti
    est à changer ?Les signes d'usure les plus courants sont détaillés dans la
    section diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par
    un professionnel.Peut-on rouler avec un valve de réglage du ralenti
    défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la
    pièce dans la sécurité du véhicule. Consultez la section symptômes pour
    évaluer l'urgence du remplacement.- corps papillon - filtre a air
  S8: >-
    Comment choisir Valve de réglage du ralenti compatible avec mon
    vehiculeRenseignez marque, modele, type moteur et annee, puis verifiez la
    reference Quand remplacer Valve de réglage du ralenti ?En cas de ralenti
    instable ou irregulier ou de degradation mesurable, Puis-je monter Valve de
    réglage du ralenti sans verification atelierLe montage peut exiger controles
    de couple, alignement et references.
  META: >-
    {"meta_title":"Valve de réglage du ralenti : symptômes et
    remplacement","meta_description":"Ralenti instable, moteur qui cale au feu
    rouge ou régime erratique ? Apprenez à diagnostiquer et remplacer la valve
    de réglage du ralenti avant une panne secondaire."}
---

# Valve de réglage du ralenti - Guide Diagnostic Complet

## Fonction et Rôle

Reguler le debit d'air au ralenti pour maintenir un regime stable moteur chaud ou froid

**Actions principales:** reguler, ouvrir, fermer, doser

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Moteur qui cale au ralenti ou au feu rouge**
  moteur qui cale au ralenti ou au feu rouge

### 🟢 Autres Symptômes

- ralenti instable ou irregulier
- regime ralenti trop haut ou trop bas
- sifflement ou bruit d aspirtion d air anormal
- odeur d essence au ralenti melange trop riche
- plus nettoyage boitier papillon

## Procédure de Diagnostic

Pour diagnostiquer un problème de valve de réglage du ralenti:

1. **Inspection visuelle** - Examiner l'état du valve de réglage du ralenti
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le valve de réglage du ralenti peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes

## Pièces Associées

Lors du remplacement, vérifier également:

- corps-papillon
- filtre-a-air

## Critères de Compatibilité

Pour commander le bon valve de réglage du ralenti, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "corrige la panne"

## FAQ

**Vanne de ralenti OE ou adaptable ?**
Les vannes OES (Bosch, Valeo) sont recommandées. Les adaptables peuvent avoir un débit différent causant des problèmes de ralenti.

**Comment savoir si ma vanne de ralenti est HS ?**
Ralenti instable ou trop haut, moteur qui cale au ralenti, régime qui monte et descend seul, voyant moteur avec codes P0505-P0509.

**Tous les combien changer la vanne de ralenti ?**
Pas de périodicité. Durée de vie variable selon encrassement. Un nettoyage tous les 50 000 km prolonge sa durée de vie.

**Peut-on changer la vanne de ralenti soi-même ?**
Oui, généralement accessible sur le boîtier papillon. Quelques vis, un connecteur. Nettoyage du boîtier recommandé en même temps.

**Quelle erreur éviter avec la vanne de ralenti ?**
Essayer le nettoyage avant le remplacement. Vérifier aussi le boîtier papillon et le capteur de position papillon.
