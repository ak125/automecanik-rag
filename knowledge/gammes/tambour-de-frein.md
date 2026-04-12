---
category: freinage
slug: tambour-de-frein
title: Tambour de frein
pg_id: 123
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-04-03'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:rag-enrich-from-web-corpus
  last_enriched_at: '2026-04-03'
  v5_migrated_at: '2026-03-29'
domain:
  role: Support interne de freinage par expansion des machoires
  must_be_true:
  - recevoir la friction
  - contenir les machoires
  - ralentir la rotation
  must_not_contain:
  - disque
  - plaquette
  - etrier
  - ventile
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - disque-de-frein
  - plaquette-de-frein
  - etrier-de-frein
  - flexible-de-frein
  - maitre-cylindre-de-frein
  - liquide-de-frein
  confusion_with:
  - term: piece-de-freinage-voisine
    difference: 'Verifier la reference exacte : les pieces de freinage se ressemblent mais ne sont pas interchangeables entre
      essieux ou types de montage.'
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
  - ❌ "freinage optimal"
  cost_range:
    min: 63
    max: 152
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  brands:
    premium:
    - Brembo
    - ATE
    - TRW
    standard:
    - Bosch
    - Ferodo
    - Textar
    budget:
    - Ridex
    - Valeo
diagnostic:
  symptoms:
  - id: S1
    label: Rainures profondes visibles interieur tambour
    severity: confort
  - id: S2
    label: Diametre interieur au-dela du maximum grave
    severity: confort
  - id: S3
    label: Bruit de frottement ou crissement a l arriere
    severity: confort
  - id: S4
    label: Tambour ovalise vibrations au freinage arriere
    severity: securite
  - id: S5
    label: Traces de surchauffe bleuissement du metal
    severity: confort
  - id: S6
    label: Frein a main inefficace malgre machoires neuves
    severity: securite
  causes:
  - localiser source et verifier usure mecanique
  - verifier equilibrage et fixations
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'vibrations anormales : verifier equilibrage et fixations'
  quick_checks:
  - 'Observer : rainures profondes visibles interieur tambour ?'
  - 'Observer : diametre interieur au-dela du maximum grave ?'
  - Bruit de frottement ou crissement a l arriere ?
  - 'Observer : tambour ovalise vibrations au freinage arriere ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Rainures profondes visibles interieur tambour
  - Diametre interieur au-dela du maximum grave
  - Bruit de frottement ou crissement a l arriere
  - Tambour ovalise vibrations au freinage arriere
  - Traces de surchauffe bleuissement du metal
  - Frein a main inefficace malgre machoires neuves
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '123'
  intro_title: A quoi sert Tambour de frein ?
  risk_title: Pourquoi remplacer Tambour de frein a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: 'Tambour OE ou adaptable : que choisir ?'
    answer: Les tambours OES (TRW, Brembo) sont fiables et économiques. Vérifiez le diamètre intérieur exact et le nombre
      de trous.
  - question: Comment savoir si mon tambour est usé ?
    answer: Rainures profondes à l intérieur du tambour, diamètre intérieur au-delà du maximum (gravé sur le tambour), freinage
      arrière bruyant.
  - question: Tous les combien changer les tambours ?
    answer: Entre 100 000 et 150 000 km. Les tambours s usent lentement car le freinage arrière est moins sollicité. Vérifiez
      le diamètre à chaque changement de mâchoires.
  - question: Peut-on rectifier un tambour ?
    answer: Oui si le diamètre reste sous le maximum autorisé. Mais la rectification coûte souvent presque autant qu un tambour
      neuf.
  - question: Quelle erreur éviter avec les tambours ?
    answer: Ne pas forcer pour déposer un tambour grippé (utiliser un extracteur). Nettoyer la poussière de frein (nocive).
      Changer par paire.
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
doc_id: c34e0039-b141-5a98-8931-94f2d0eacb30
content_hash: sha256:d649db5a1ec23956
lang: fr
variants:
- name: Piece standard
  aliases:
  - standard
  - OE equivalent
  functional_differences:
  - Qualite equivalente a la monte d origine
  - Compatible avec la majorite des vehicules
- name: Piece performance/sport
  aliases:
  - sport
  - haute performance
  functional_differences:
  - Materiaux haute temperature
  - Pour usage intensif ou sportif
location_on_vehicle:
  area: Au niveau des roues (avant et/ou arriere)
  access: Demontage de la roue necessaire (cric + chandelle)
  adjacent_parts:
  - disque
  - plaquette
  - etrier
  - flexible
installation:
  difficulty: moyen
  time: 30min a 1h par essieu
  tools:
  - cle a douille
  - cle Allen
  - pied a coulisse
  - cle dynamometrique
  prerequisite: Vehicule sur chandelles, roue demontee
phase5_enrichment:
  _source: ate-freinage.fr + bremboparts.com + delphiautoparts.com + textar.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 6
  _has_tech_data: true
  types_variants:
  - type: 'hydraulique'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    norme_ece_r90: 'ECE R90'
    norme_ecer90: 'ecer90'
    val_100_a: '100 a'
    val_17_a: '17 a'
    val_50_a: '50 a'
    val_7_a: '7 a'
    val_8_a: '8 a'
    val_882_a: '882 a'
    val_921_a: '921 a'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'En appuyant sur la pédale de frein la pression du liquide defrein va actionner le cylindre deroue de la voiture qui
    va écarter les mâchoires de frein arrière pour créer une friction à l''intérieurdu tambour de frein. Il existe plusieurs
    types de tambours de frein : - Tambour de frein avec moyeu de roulement (roulementconique ou cylindrique). - Tambour de
    frein sans moyeu de roulement : leroulement est monté sur la fusée arrière. En savoir plus : tambour de frein — définition
    et rôle mécanique 🚨 Bruit Tambour de frein : causes et diagnostic'
  S2: 'Un tambour de frein défectueux présent plusieurs symptômes : - Bruit de frottement dansle tambour de frein lors du
    freinage. - Rallongement desdistances de freinage. - Le câble de frein à main de la voiture même serré neretient plus
    le véhicule en stationnement. Tous les tambours de frein sont homologuées par les constructeurs automobile et par les
    équipementiers des pièces détachées automobile. Diagnostic complet : identifier une panne de tambour de frein'
  S2_DIAG: 'SymptômeCause probableActionRainures profondes visibles interieur tambourlocaliser source et verifier usure mecaniqueObserver
    : rainures profondes visibles interieur tambour ?Diametre interieur au-dela du maximum graveverifier equilibrage et fixationsObserver
    : diametre interieur au-dela du maximum grave ?Bruit de frottement ou crissement a l arrierebruit anormal detecte : localiser
    source et verifier usure mecaniqueBruit de frottement ou crissement a l arriere ?Tambour ovalise vibrations au freinage
    arrierevibrations anormales : verifier equilibrage et fixationsObserver : tambour ovalise vibrations au freinage arriere
    ?Traces de surchauffe bleuissement du metallocaliser source et verifier usure mecaniqueObserver : rainures profondes visibles
    interieur tambour ?Frein a main inefficace malgre machoires neuveslocaliser source et verifier usure mecaniqueObserver
    : rainures profondes visibles interieur tambour ?'
  S3: 'Avant de commander, vérifiez ces caractéristiques sur votre ancien tambour ou dans votre carnet d''entretien : - Diamètre
    intérieur : varie selon le modèle (ex : 180 mm, 200 mm ou 228 mm sur la même gamme de véhicules) - Nombre de trous de
    fixation et entraxe des goujons de roue - Roulement intégré : certains tambours intègrent le roulement de roue arrière
    (véhicules sans moyeu séparé) - Bague ABS : si votre véhicule a l''ABS arrière, le tambour doit inclure la bague magnétique
    pour le capteur - Type de fixation : tambour à vis de centrage ou à simple emboîtement sur les goujons Méthode : mesurer
    le diamètre intérieur de l''ancien tambour au pied à coulisse, ou utiliser le sélecteur véhicule pour trouver la référence
    exacte. ➡️ Trouver les tambours compatibles avec votre véhicule'
  S4_DEPOSE: 📖 Avant de démonter, consultez la fiche technique Tambour de frein pour connaître les spécifications. - Relâchez
    le frein à main. - Levez et calez le véhicule. - Démontez la roue. - Démontez le cache de protection qu'est fixé aucentre
    du tambour de frein. - Desserrez l'écrou de fixation du tambourde frein. - Démontez le tambour de frein.
  S4_REPOSE: 'Le remontage du tambour de frein exige une vérification dimensionnelle préalable et un réglage du jeu entre
    mâchoires et tambour. Un jeu trop faible provoque une friction permanente qui surchauffe le tambour et détruit les mâchoires
    en quelques centaines de kilomètres ; un jeu trop important rend le frein à main inefficace. - Vérifiez que le tambour
    de frein neuf est identique à celui démonté : diamètre intérieur exact (gravé sur le tambour et à vérifier au pied à coulisse),
    nombre de trous de fixation, présence éventuelle de cannelures ABS. - Contrôlez l''état du kit de freins arrière complet
    (mâchoires, ressorts, tendeurs) et remplacez l''ensemble si les mâchoires montrent moins de 2 mm de garniture ou si les
    ressorts sont déformés. - Contrôlez l''état du câble de frein à main : un câble étiré ou gainé fissuré ne permettra pas
    au frein à main d''être efficace même avec un tambour neuf. - Contrôlez l''état du cylindre de roue : une fuite de liquide
    de frein à l''arrière du plateau de frein indique un cylindre à remplacer impérativement avant repose du tambour. - Graissez
    à la graisse cuivre les points d''appui des mâchoires sur le plateau de frein — uniquement sur les portées métalliques,
    jamais sur la garniture ni sur la surface de friction interne du tambour. - Réglez le diamètre des mâchoires via le tendeur
    de réglage automatique ou le réglage manuel pour que le tambour glisse avec une légère résistance sur les mâchoires :
    tournez d''un cran à la fois jusqu''à ce que le tambour frôle sans coincer. - Montez le tambour de frein neuf et fixez
    les vis de centrage si présentes. Assurez-vous que le tambour est parfaitement centré sur le moyeu avant de monter la
    roue. - Effectuez 5 à 8 actionnements lents de la pédale de frein pour que les mâchoires s''auto- positionnent dans le
    tambour neuf et que le réglage automatique se mette à jour. - Actionnez le frein à main pour vérifier qu''il bloque correctement
    les roues arrière en 3 à 5 crans de garde — réajustez la tension du câble si nécessaire. - Remontez la roue au couple
    de serrage prescrit, reposez le véhicule et effectuez un test de freinage progressif à 30 km/h pour vérifier l''absence
    de crissement et l''absence de déséquilibre latéral.'
  S5: '- Mauvais diamètre de tambour (180 vs 200 vs 228 mm) — Le tambour ne se monte pas ou les mâchoires frottent en permanence.
    → Vérifier la référence exacte via le sélecteur véhicule. - Réutiliser des ressorts de rappel fatigués — Les mâchoires
    ne reculent plus correctement, freinage résiduel et surchauffe. → Remplacer systématiquement les ressorts et le kit de
    fixation. - Ne pas régler le mécanisme de rattrapage — Course de pédale excessive ou frein à main inefficace. → Régler
    la came de rattrapage pour obtenir un jeu de 0,3-0,5 mm entre mâchoires et tambour. - Oublier de nettoyer l''intérieur
    du tambour neuf — Poussière de fonderie et huile de protection réduisent l''adhérence. → Nettoyer au nettoyant frein avant
    montage. - Forcer le démontage du tambour grippé — Risque de casser les goujons ou d''endommager le roulement. → Utiliser
    les trous de chasse filetés (M8) prévus sur le tambour, ou un extracteur. - Confondre mâchoire primaire et secondaire
    — Freinage déséquilibré, la mâchoire primaire (garniture courte) doit être côté avant du sens de rotation. → Repérer le
    sens avant démontage. - Ne pas contrôler le cylindre de roue — Un cylindre qui fuit souille les garnitures neuves et réduit
    le freinage. → Vérifier l''absence de fuite et la souplesse des pistons. - Oublier de régler le frein à main — Le frein
    de stationnement ne bloque plus suffisamment. → Ajuster le câble de frein à main après montage du tambour neuf. 📖 Fiche
    technique Tambour de frein — spécifications à vérifier avant montage.'
  S6: 'Contrôles statiques - Vérifier que le tambour tourne librement à la main (léger frottement acceptable, pas de blocage)
    - Contrôler le réglage du rattrapage : la roue doit se bloquer légèrement quand on resserre la came, puis être relâchée
    d''un cran - Vérifier l''absence de fuite au cylindre de roue - Tester le frein à main : il doit bloquer les roues arrière
    en 3 à 5 clics de levier - Pomper la pédale de frein : elle doit devenir ferme après 4 à 6 appuis (rattrapage du jeu des
    mâchoires) Essai routier progressif - Démarrer sur un parking plat : freinage doux à 10 km/h, vérifier que le véhicule
    freine droit - Tester le frein à main sur une pente douce : le véhicule doit rester immobile - Augmenter progressivement
    : 30, 50 km/h avec des freinages normaux - Un léger frottement les premiers kilomètres est normal pendant le rodage des
    garnitures ⚠️ Arrêter immédiatement si : pédale molle, bruits de raclement métallique, frein à main inopérant, odeur de
    brûlé sur une roue arrière, surchauffe anormale d''un tambour. 🚨 Bruit Tambour de frein : causes et diagnostic'
  S_GARAGE: 'Nous vous recommandons de confier cette intervention à un professionnel : - Plusieurs causes possibles de défaillance
    (4 identifiées) nécessitent un diagnostic professionnel Un garagiste qualifié dispose de l''outillage et de l''expérience
    nécessaires pour effectuer cette opération en toute sécurité.'
  S7: Quel est le prix d'un tambour de frein ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur pour
    trouver le tambour de frein compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon tambour de frein est à changer ?Les signes d'usure les plus courants sont détaillés dans la section diagnostic
    ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un tambour de frein défaillant
    ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule. Consultez la section
    symptômes pour évaluer l'urgence du remplacement.- Mâchoires de frein. - Kit de freins arrière. 📖 Fiche technique Tambour
    de frein — intervalles et spécifications d’entretien.
  S8: 'Faut-il remplacer les tambours par paire ? Oui, les tambours se remplacent toujours par paire (les deux de l''essieu
    arrière) pour garantir un freinage équilibré. Un tambour neuf et un tambour usé ont des diamètres intérieurs différents,
    ce qui provoque un déséquilibre au freinage. Mon tambour est grippé et ne se démonte pas, que faire ? Ne jamais forcer
    au marteau directement sur le tambour. Utiliser d''abord les trous de chasse filetés (M8) présents sur la plupart des
    tambours : visser des boulons qui poussent le tambour hors du moyeu. Si le tambour est rouillé sur le moyeu, appliquer
    du dégrippant et laisser agir 15 minutes avant de réessayer. Peut-on rectifier un tambour au lieu de le remplacer ? La
    rectification est possible si le diamètre intérieur après usinage reste inférieur au diamètre maximal gravé sur le tambour
    (ex : Ø max 181 mm). Au-delà, le tambour est trop fin et risque de se fissurer sous l''échauffement. En pratique, le coût
    de rectification est souvent proche du prix d''un tambour neuf. Faut-il changer les mâchoires en même temps que les tambours
    ? Si les garnitures des mâchoires sont encore épaisses (> 2 mm) et sans traces de contamination (huile, liquide de frein),
    elles peuvent être conservées. Sinon, les remplacer en même temps avec le kit de ressorts pour un résultat optimal. Pourquoi
    le frein à main ne tient plus après le changement ? Le mécanisme de rattrapage automatique doit être repositionné pour
    compenser le diamètre du tambour neuf (plus petit que l''ancien usé). Régler la came de rattrapage et ajuster la tension
    du câble de frein à main jusqu''à obtenir un blocage en 3 à 5 clics de levier. 📖 Pour plus de détails techniques : fiche
    Tambour de frein'
  META: '- Rôle des tambours de frein et les types de pannes sur la Clio II 1.2.'
---

# Tambour de frein - Guide Diagnostic Complet

## Fonction et Rôle

Support interne de freinage par expansion des machoires

**Actions principales:** recevoir la friction, contenir les machoires, ralentir la rotation, tourner, enfermer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Tambour ovalise vibrations au freinage arriere**
  tambour ovalise vibrations au freinage arriere
- **Frein a main inefficace malgre machoires neuves**
  frein a main inefficace malgre machoires neuves

### 🟢 Autres Symptômes

- rainures profondes visibles interieur tambour
- diametre interieur au-dela du maximum grave
- bruit de frottement ou crissement a l arriere
- traces de surchauffe bleuissement du metal

## Procédure de Diagnostic

Pour diagnostiquer un problème de tambour de frein:

1. **Inspection visuelle** - Examiner l'état du tambour de frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- cable-de-frein-a-main
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- etrier-de-frein
- interrupteur-des-feux-de-freins
- kit-de-freins-arriere
- machoires-de-frein

## Critères de Compatibilité

Pour commander le bon tambour de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "freinage optimal"

## FAQ

**Tambour OE ou adaptable : que choisir ?**
Les tambours OES (TRW, Brembo) sont fiables et économiques. Vérifiez le diamètre intérieur exact et le nombre de trous.

**Comment savoir si mon tambour est usé ?**
Rainures profondes à l intérieur du tambour, diamètre intérieur au-delà du maximum (gravé sur le tambour), freinage arrière bruyant.

**Tous les combien changer les tambours ?**
Entre 100 000 et 150 000 km. Les tambours s usent lentement car le freinage arrière est moins sollicité. Vérifiez le diamètre à chaque changement de mâchoires.

**Peut-on rectifier un tambour ?**
Oui si le diamètre reste sous le maximum autorisé. Mais la rectification coûte souvent presque autant qu un tambour neuf.

**Quelle erreur éviter avec les tambours ?**
Ne pas forcer pour déposer un tambour grippé (utiliser un extracteur). Nettoyer la poussière de frein (nocive). Changer par paire.
## Definition

La norme ECE R90 encadre la conformite des pieces de freinage de remplacement (ex: plaquettes, disques) avec des exigences de performance proches de l'equipement d'origine.

## Pourquoi c'est important

- meilleure coherence de freinage
- reduction du risque de pieces non conformes
- reference utile pour le choix de pieces sur vehicule de tourisme

## Points a verifier

- mention ECE R90 sur le produit/emballage
- correspondance avec la reference vehicule
- provenance et tracabilite
## Types de vibrations

### Vibrations au volant
- **À basse vitesse (< 50 km/h)** : Problème de pneus ou jantes
- **À haute vitesse (> 80 km/h)** : Équilibrage ou géométrie
- **Au freinage** : Disques voilés

### Vibrations dans l'habitacle
- **Moteur au ralenti** : Supports moteur
- **En accélération** : Transmission, cardans
- **À vitesse constante** : Pneus, roulements

### Vibrations dans la pédale de frein
- **Au freinage** : Disques voilés, plaquettes usées

## Causes et solutions

### 1. Pneus déséquilibrés
- **Symptôme** : Vibration volant à partir de 80-100 km/h
- **Vérification** : Visuel sur les masses d'équilibrage
- **Solution** : Équilibrage des 4 pneus
- **Coût** : 40-60€
- **Urgence** : Moyenne

### 2. Pneus usés irrégulièrement
- **Symptôme** : Vibration + bruit de roulement
- **Vérification** : Usure en "dents de scie"
- **Solution** : Remplacement pneus + géométrie
- **Urgence** : Haute

### 3. Roulement de roue défaillant
- **Symptôme** : Grondement augmentant avec la vitesse
- **Vérification** : Jeu dans la roue, bruit en virage
- **Solution** : Remplacement roulement
- **Pièces** : Kit roulement de roue
- **Urgence** : Haute - Sécurité

### 4. Cardans usés
- **Symptôme** : Claquement en braquant, vibration en accélération
- **Vérification** : Soufflets déchirés, jeu
- **Solution** : Remplacement cardan
- **Pièces** : Cardan complet ou transmission
- **Urgence** : Haute

### 5. Disques de frein voilés
- **Symptôme** : Vibration pédale au freinage
- **Vérification** : Mesure au comparateur
- **Solution** : Rectification ou remplacement
- **Pièces** : Disques de frein
- **Urgence** : Moyenne

### 6. Supports moteur fatigués
- **Symptôme** : Vibration au ralenti dans l'habitacle
- **Vérification** : Visuel sur silent-blocs
- **Solution** : Remplacement supports
- **Pièces** : Support moteur, silent-bloc
- **Urgence** : Basse
## Symptômes courants

### Grincement aigu au freinage
- **Quand** : Au moment du freinage léger ou modéré
- **Caractéristique** : Son métallique aigu, type "crissement"

### Sifflement continu
- **Quand** : Pendant tout le freinage
- **Caractéristique** : Son aigu constant

### Bruit sourd / grondement
- **Quand** : Freinage appuyé
- **Caractéristique** : Vibration ressentie dans la pédale

### Claquement
- **Quand** : Début ou fin de freinage
- **Caractéristique** : Bruit sec, ponctuel

## Causes possibles et solutions

### 1. Plaquettes de frein usées
- **Probabilité** : 70%
- **Vérification** : Témoin usure allumé, épaisseur < 3mm
- **Solution** : Remplacement des plaquettes
- **Pièces** : Plaquettes de frein avant/arrière
- **Urgence** : Haute - Sécurité

### 2. Disques de frein voilés
- **Probabilité** : 15%
- **Vérification** : Vibration pédale, usure inégale visible
- **Solution** : Rectification ou remplacement des disques
- **Pièces** : Disques de frein
- **Urgence** : Moyenne

### 3. Étrier grippé
- **Probabilité** : 10%
- **Vérification** : Usure asymétrique des plaquettes
- **Solution** : Nettoyage/graissage ou remplacement étrier
- **Pièces** : Kit réparation étrier, étrier complet
- **Urgence** : Haute

### 4. Absence de graisse sur glissières
- **Probabilité** : 5%
- **Vérification** : Plaquettes difficiles à bouger
- **Solution** : Nettoyage et graissage
- **Pièces** : Graisse haute température
- **Urgence** : Basse

## Questions complémentaires pour affiner le diagnostic

1. Le bruit apparaît-il à froid ou à chaud ?
2. Le bruit est-il présent sur les 4 roues ou localisé ?
3. Y a-t-il une vibration dans le volant ?
4. Quand avez-vous changé vos plaquettes pour la dernière fois ?
5. Avez-vous un témoin d'usure allumé au tableau de bord ?
