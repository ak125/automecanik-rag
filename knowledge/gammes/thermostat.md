---
category: refroidissement
slug: thermostat
title: Thermostat
pg_id: 316
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
  role: Reguler le flux de liquide de refroidissement selon la temperature moteur
  must_be_true:
  - reguler
  - ouvrir
  - fermer
  must_not_contain:
  - sonde
  - capteur
  - electronique
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - radiateur-de-refroidissement
  - pompe-a-eau
  - durite-de-refroidissement
  - vase-d-expansion
  - ventilateur-de-refroidissement
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
  - ❌ "evite la casse moteur"
  cost_range:
    min: 3
    max: 59
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  brands:
    premium:
    - Wahler
    - Behr (Mahle)
    - Gates
    standard:
    - Calorstat (Vernet)
    - Thermostat (Continental)
    - Dayco
    budget:
    - Febi Bilstein
    - Meyle
    - Topran
  quality_tiers:
  - tier: Origine constructeur
    description: Thermostats d origine avec temperature d ouverture et course calibrees pour le moteur. Joint de boitier inclus
      selon les references.
  - tier: Equipementier qualite OE
    description: Thermostats premiere monte avec temperature d ouverture precise et capsule de cire de qualite. Plage de tolerance
      etroite.
  - tier: Adaptable qualite reconnue
    description: Thermostats compatibles avec verification de la temperature d ouverture nominale et du diametre avant montage.
diagnostic:
  symptoms:
  - id: S1
    label: Aiguille de temperature dans le rouge rapidement
    severity: confort
  - id: S2
    label: Moteur qui ne chauffe jamais aiguille basse
    severity: confort
  - id: S3
    label: Sifflement ou vapeur s echappant du capot
    severity: confort
  - id: S4
    label: Chauffage qui reste froid tres longtemps
    severity: confort
  - id: S5
    label: Odeur de liquide de refroidissement en surchauffe
    severity: confort
  - id: S6
    label: Plus de 100 000 km sans remplacement
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - remplacement preventif recommande
  quick_checks:
  - 'Observer : aiguille de temperature dans le rouge rapidement ?'
  - 'Observer : moteur qui ne chauffe jamais aiguille basse ?'
  - 'Observer : sifflement ou vapeur s echappant du capot ?'
  - 'Observer : chauffage qui reste froid tres longtemps ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Aiguille de temperature dans le rouge rapidement
  - Moteur qui ne chauffe jamais aiguille basse
  - Sifflement ou vapeur s echappant du capot
  - Chauffage qui reste froid tres longtemps
  - Odeur de liquide de refroidissement en surchauffe
  - Plus de 100 000 km sans remplacement
  good_practices:
  - Controle du niveau de liquide de refroidissement a froid chaque mois
  - Remplacement du liquide selon preconisation constructeur (2-5 ans)
  - Verification des durites et colliers a chaque revision
  - Purge du circuit apres toute intervention sur le refroidissement
rendering:
  pgId: '316'
  intro_title: A quoi sert Thermostat ?
  risk_title: Pourquoi remplacer Thermostat a temps ?
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
  - question: Thermostat OE ou adaptable ?
    answer: Les thermostats OES (Wahler, Behr, Gates) garantissent une température d'ouverture précise. Les adaptables peuvent
      avoir une plage d'ouverture moins fiable.
  - question: Comment savoir si mon thermostat est HS ?
    answer: Surchauffe rapide (bloqué fermé), moteur qui ne chauffe pas (bloqué ouvert), chauffage froid, surconsommation
      de carburant.
  - question: Tous les combien changer le thermostat ?
    answer: Remplacement préventif conseillé à 100 000 km. Changez-le systématiquement lors d'une intervention sur le circuit
      de refroidissement.
  - question: Peut-on changer le thermostat soi-même ?
    answer: Oui, opération accessible sur la plupart des véhicules. Vidange partielle, dépose du boîtier, remplacement du
      joint. Purge obligatoire.
  - question: Quelle erreur éviter avec le thermostat ?
    answer: Ne pas oublier le joint de boîtier. Respecter le sens de montage (pointeau vers le moteur). Bien purger le circuit
      après.
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
doc_id: b7fe6110-0f53-5587-bb5d-b32380d0a27a
content_hash: sha256:a5fd9278e32d508b
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
  area: Face avant du vehicule (radiateur) et bloc moteur
  access: Par le dessus (capot) ou face avant
  adjacent_parts:
  - radiateur
  - durites
  - pompe a eau
  - thermostat
installation:
  difficulty: moyen
  time: 30min a 2h
  tools:
  - tournevis
  - pince de serrage
  - bac de recuperation
  prerequisite: Moteur froid, circuit vidange avant depose
phase5_enrichment:
  _source: denso-am.eu + fr.wikipedia.org + hella.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 6
  _has_tech_data: true
  types_variants:
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_1_5_bars: '1,5 bars'
    val_2_a: '2 a'
    val_3_a: '3 a'
    val_4_a: '4 a'
    val_868_a: '868 a'
    val_9_a: '9 a'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le thermostat est une vanne thermostatique, il s'actionne(ouverture et
    fermeture) en fonction de la température du liquide derefroidissement pour
    permettre la régulation de la température dans le circuit.Le thermostat ne
    laisse pas passer le liquide de refroidissement lorsque lemoteur est froid
    jusqu'à il atteint sa température optimale de fonctionnement.Le thermostat
    s'ouvre et fait circuler le liquide de refroidissement chaud auradiateur de
    refroidissement pour le refroidir dés que le moteur atteint latempérature de
    fonctionnement.Les nouveaux thermostats sont actionnésautomatiquement par le
    calculateur de gestion moteur. En savoir plus : thermostat — définition et
    rôle mécanique 🚨 Bruit Thermostat : causes et diagnostic
  S2: >-
    Un thermostat usé présente plusieurs symptômes : - Le moteur atteint
    lentement la température defonctionnement. - Après un contrôle visuel vous
    remarquez que lethermostat est grippé (reste fermé ou reste ouvert). Un
    thermostat défaillant et qu'il n'est pas remplacé à temps peut entraînerla
    surchauffe du moteur et qui amène à un joint de culasse . Diagnostic complet
    : identifier une panne de thermostat
  S3: >-
    Le thermostat régule le flux de liquide de refroidissement en maintenant le
    moteur dans sa plage de température optimale, généralement entre 85 °C et
    105 °C selon la conception constructeur. Un thermostat bloqué en position
    fermée provoque la surchauffe en quelques kilomètres ; bloqué en position
    ouverte, il fait tourner le moteur trop froid, augmentant la consommation et
    l'usure des segments. La sélection doit être précise sur trois paramètres
    clés. - Température d'ouverture gravée sur la cloche — Chaque thermostat
    porte une valeur en °C (ex. 82 °C, 87 °C, 92 °C). Cette valeur doit
    correspondre exactement à la préconisation constructeur ; un thermostat à 82
    °C sur un moteur préconisant 92 °C maintient le moteur trop froid en
    permanence. - Référence moteur et code motorisation — Renseignez le code
    moteur complet (ex. N47D20, K9K, DV6) et non seulement la cylindrée : deux
    moteurs de 1,6 L de la même marque peuvent utiliser des thermostats de
    diamètres différents. - Diamètre de la cloche et type de joint — Le logement
    du thermostat dans la culasse ou le boîtier de sortie d'eau a un diamètre
    précis (57 mm, 61 mm, 68 mm sont les plus répandus). Vérifiez si le joint
    torique est fourni avec la pièce ou s'il doit être commandé séparément. -
    Version avec ou sans sonde de température intégrée — Certains thermostats
    modernes intègrent une sonde NTC directement dans la cloche. Remplacer cette
    version par un thermostat sans sonde laisse un emplacement vide dans le
    circuit électronique et déclenche un code défaut P0118 ou P0128. -
    Thermostat à commande électrique (e-thermostat) — Sur les motorisations
    récentes (post-2010, particulièrement BMW, Volkswagen, PSA), le thermostat
    est commandé par le calculateur moteur. Ces versions ne sont pas
    interchangeables avec les thermostats mécaniques traditionnels. - Matériau
    du boîtier et résistance chimique — Les boîtiers en aluminium sont plus
    durables mais plus chers ; les versions plastique (polyamide) suffisent pour
    la plupart des applications. Vérifiez la compatibilité avec le liquide de
    refroidissement utilisé (G11, G12, G13) car certains antigels attaquent les
    joints d'origine. Pour aller plus loin : consultez notre guide d'achat
    thermostat — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Thermostat pour connaître
    les spécifications. - Arrêtez le moteur et le laisser refroidir. -
    Débranchez la batterie. - Repérez l'emplacement du thermostat survotre
    moteur. - Ouvrir le bouchon du vase d'expansion . - Levez et calez le
    véhicule. - Désaccouplez la durite inférieure duradiateur de refroidissement
    . - Vidangez le liquide de refroidissement. - Accouplez la durite inférieure
    duradiateur de refroidissement. - Désaccouplez la canalisation duthermostat.
    - Démontez les fixations du thermostat. - Démontez le thermostat.
  S4_REPOSE: >-
    Le remontage du thermostat impose le respect de deux contraintes techniques
    absolues : le sens d'orientation du pointeau (vers le moteur, jamais vers le
    radiateur) et l'utilisation d'un joint de boîtier neuf. Un thermostat monté
    à l'envers reste bloqué en position ouverte et produit exactement les mêmes
    symptômes qu'un thermostat défaillant. La purge complète du circuit clôt
    systématiquement l'intervention. - Vérifiez que le thermostat neuf est
    identique à celui démonté : température d'ouverture (gravée sur le pointeau,
    typiquement 82 °C, 87 °C ou 92 °C selon le moteur), diamètre du boîtier,
    présence d'un by-pass. - Remplacez le joint de boîtier systématiquement — ne
    jamais réutiliser l'ancien joint même en apparence intact : un joint
    thermostat coûte moins d'un euro et une fuite sous pression peut noyer le
    compartiment moteur. - Nettoyez les surfaces d'appui du boîtier et du bloc
    moteur à la lame de rasoir ou au papier abrasif fin pour éliminer tout
    résidu du joint ancien, puis essuyez avec un chiffon propre et sec. -
    Positionnez le nouveau thermostat avec le pointeau thermosensible orienté
    vers le moteur (côté chaud) — vérifiez la direction indiquée sur le boîtier
    ou dans la documentation constructeur si le sens n'est pas évident. - Posez
    le joint neuf sur le boîtier thermostat ou dans la gorge du bloc, en
    vérifiant qu'il est bien centré sans être tordu ni plié. - Remontez le
    boîtier thermostat et serrez les vis de fixation progressivement en croix au
    couple prescrit (typiquement 8 à 12 N·m) pour ne pas déformer le boîtier
    plastique ou aluminium. - Reconnectez le connecteur électrique du capteur de
    température ou de l'éventuel thermostat électronique, jusqu'au déclic de
    verrouillage. - Remplissez le circuit de refroidissement avec un mélange
    liquide de refroidissement et eau déminéralisée conforme aux préconisations
    constructeur, par le vase d'expansion. - Purgez le circuit en faisant
    tourner le moteur à froid avec le bouchon du vase d'expansion entrebâillé —
    attendez l'ouverture du thermostat (aiguille au milieu de cadran, environ 5
    à 8 minutes de chauffe) et maintenez le niveau jusqu'à stabilisation sans
    bulles. - Effectuez un contrôle de fonctionnement sur route courte :
    l'aiguille de température doit se stabiliser en position médiane en moins de
    5 minutes, le chauffage doit délivrer de l'air chaud, et aucune fuite ne
    doit apparaître au boîtier thermostat après refroidissement complet.
  S5: >-
    Erreurs frequentes avec le thermostat : - Confondre thermostat bloque ouvert
    et bloque ferme — ouvert = le moteur ne monte jamais en temperature
    (surconsommation, chauffage faible). Ferme = surchauffe rapide, destruction
    du joint de culasse- Ne pas remplacer le joint du thermostat — un joint
    reutilise fuit systematiquement, meme si le boitier semble etanche au
    montage- Oublier de purger le circuit de refroidissement apres remplacement
    — une bulle d'air bloque la circulation et le moteur surchauffe malgre le
    thermostat neuf- Monter un thermostat avec une temperature d'ouverture
    differente de l'origine — un thermostat a 82°C sur un moteur prevu pour 89°C
    provoque un fonctionnement a froid permanent- Ignorer un chauffage habitacle
    faible par temps froid — premier symptome d'un thermostat bloque ouvert,
    avant la surconsommation
  S6: >-
    Le remplacement du thermostat implique une ouverture du circuit de
    refroidissement. Les vérifications post-montage sont donc doubles :
    s'assurer de l'étanchéité du circuit et confirmer que le thermostat neuf
    s'ouvre et se ferme correctement aux bonnes températures. - Purge complète
    du circuit de refroidissement : après le remontage, ouvrir le ou les vis de
    purge présents sur le circuit (généralement sur le radiateur ou la durite
    haute) et faire tourner le moteur jusqu'à ce que le liquide s'écoule sans
    bulles d'air. Une poche d'air résiduelle provoque une surchauffe localisée
    même avec un thermostat neuf. - Vérification du niveau de liquide de
    refroidissement : contrôler que le niveau dans le vase d'expansion se situe
    entre les repères MIN et MAX à froid, puis vérifier à nouveau après la
    première montée en température. Le volume peut baisser légèrement lors du
    premier cycle thermique. - Surveillance de l'aiguille de température : au
    premier démarrage après remplacement, observer la montée en température du
    moteur. L'aiguille doit atteindre la zone normale (entre 80°C et 95°C selon
    le moteur) en 5 à 10 minutes de ralenti, puis se stabiliser. Une aiguille
    qui reste en dessous de 60°C indique un thermostat bloqué ouvert. - Test
    d'ouverture du thermostat : lorsque l'aiguille atteint la température
    d'ouverture du thermostat (généralement 87°C à 92°C), vérifier que la durite
    radiateur haute commence à chauffer rapidement au toucher — signe que le
    liquide circule dans le radiateur principal. - Contrôle de l'absence de
    fuite : moteur chaud et circuit en pression, inspecter visuellement le
    boîtier du thermostat, les colliers de serrage des durites raccordées et le
    joint de boîtier pour détecter toute trace de liquide de refroidissement
    suintant. - Vérification de la chauffe habitacle : mettre le chauffage au
    maximum — l'air chaud doit arriver dans l'habitacle dans un délai normal (2
    à 4 minutes), confirmant que la circulation dans l'échangeur de chauffage
    est rétablie. - Test sous charge modérée : effectuer un trajet de 15 à 20 km
    incluant de la route et de la ville. L'aiguille de température ne doit pas
    dépasser la zone rouge ni présenter d'oscillations, ce qui signalerait une
    purge incomplète ou un thermostat défectueux.
  S7: >-
    Quel est le prix d'un thermostat ?Le prix varie selon le véhicule et la
    marque. Utilisez notre sélecteur pour trouver le thermostat compatible avec
    votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon thermostat est à changer ?Les signes d'usure les plus courants
    sont détaillés dans la section diagnostic ci-dessus. En cas de doute, faites
    contrôler la pièce par un professionnel.Peut-on rouler avec un thermostat
    défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la
    pièce dans la sécurité du véhicule. Consultez la section symptômes pour
    évaluer l'urgence du remplacement.- reguler - ouvrir - fermer
  S8: >-
    Comment choisir Thermostat compatible avec mon vehicule ?Renseignez marque,
    modele, type moteur et annee, puis verifiez la reference Quand remplacer
    Thermostat ?En cas de aiguille de temperature dans le rouge rapidement ou de
    degradation Puis-je monter Thermostat sans verification atelier ?Le montage
    peut exiger controles de couple, alignement et references.
  META: >-
    {"meta_title":"Thermostat moteur : symptômes et
    remplacement","meta_description":"Moteur qui surchauffe ou qui ne monte pas
    en température ? Quand changer le thermostat, le choisir selon votre
    véhicule et éviter les erreurs."}
---

# Thermostat - Guide Diagnostic Complet

## Fonction et Rôle

Reguler le flux de liquide de refroidissement selon la temperature moteur

**Actions principales:** reguler, ouvrir, fermer, controler le flux

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- aiguille de temperature dans le rouge rapidement
- moteur qui ne chauffe jamais aiguille basse
- sifflement ou vapeur s echappant du capot
- chauffage qui reste froid tres longtemps
- odeur de liquide de refroidissement en surchauffe
- plus de 100 000 km sans remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de thermostat:

1. **Inspection visuelle** - Examiner l'état du thermostat
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

- durite-de-refroidissement
- pompe-a-eau
- radiateur-de-refroidissement
- sonde-de-refroidissement
- vase-d-expansion
- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon thermostat, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "evite la casse moteur"

## FAQ

**Thermostat OE ou adaptable ?**
Les thermostats OES (Wahler, Behr, Gates) garantissent une température d'ouverture précise. Les adaptables peuvent avoir une plage d'ouverture moins fiable.

**Comment savoir si mon thermostat est HS ?**
Surchauffe rapide (bloqué fermé), moteur qui ne chauffe pas (bloqué ouvert), chauffage froid, surconsommation de carburant.

**Tous les combien changer le thermostat ?**
Remplacement préventif conseillé à 100 000 km. Changez-le systématiquement lors d'une intervention sur le circuit de refroidissement.

**Peut-on changer le thermostat soi-même ?**
Oui, opération accessible sur la plupart des véhicules. Vidange partielle, dépose du boîtier, remplacement du joint. Purge obligatoire.

**Quelle erreur éviter avec le thermostat ?**
Ne pas oublier le joint de boîtier. Respecter le sens de montage (pointeau vers le moteur). Bien purger le circuit après.
