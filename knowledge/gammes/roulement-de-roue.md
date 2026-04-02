---
category: direction
slug: roulement-de-roue
title: Roulement de roue
pg_id: 655
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-04-02'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:rag-enrich-from-web-corpus
  last_enriched_at: '2026-04-02'
  v5_migrated_at: '2026-03-29'
domain:
  role: Permettre la rotation libre de la roue sur son axe - Supporte les charges radiales et axiales
  must_be_true:
  - permettre la rotation
  - supporter
  - guider
  must_not_contain:
  - direction
  - cremailliere
  - volant
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - cremailliere-de-direction
  - rotule-de-direction
  - pompe-de-direction-assistee
  - barre-de-direction
  - soufflet-de-direction
  - colonne-de-direction
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
  - ❌ "securite garantie"
  cost_range:
    min: 40
    max: 150
    currency: EUR
    unit: pièce
    source: catalogue automecanik
  brands:
    premium:
    - SKF
    - FAG (Schaeffler)
    - NTN-SNR
    standard:
    - SNR
    - INA (Schaeffler)
    - Timken
    budget:
    - Febi Bilstein
    - Optimal
    - GSP
  quality_tiers:
  - tier: Origine (OE)
    description: Roulements fabriques par l'equipementier d'origine. Tolerances micrometriques, etancheite et precharge identiques
      a la piece usine.
  - tier: Qualite equivalente OE (OES)
    description: Grands roulementiers mondiaux qui equipent aussi les constructeurs. Qualite tres proche de l'OE.
  - tier: Adaptable de qualite
    description: Marques fiables en entree de gamme. Verifier si le kit inclut l'ecrou de moyeu (souvent a usage unique).
diagnostic:
  symptoms:
  - id: S1
    label: Ronronnement grondement augmente vitesse
    severity: confort
  - id: S2
    label: Bruit qui change d intensite dans les virages
    severity: confort
  - id: S3
    label: Jeu perceptible en secouant la roue montee
    severity: confort
  - id: S4
    label: Vibrations dans le volant a certaines vitesses
    severity: confort
  - id: S5
    label: Roue anormalement chaude apres roulage
    severity: confort
  - id: S6
    label: Bruit de frottement ou de craquement
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - verifier equilibrage et fixations
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'vibrations anormales : verifier equilibrage et fixations'
  quick_checks:
  - 'Observer : ronronnement grondement augmente vitesse ?'
  - Bruit qui change d intensite dans les virages ?
  - 'Observer : jeu perceptible en secouant la roue montee ?'
  - Vibrations dans le volant a certaines vitesses ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Ronronnement grondement augmente vitesse
  - Bruit qui change d intensite dans les virages
  - Jeu perceptible en secouant la roue montee
  - Vibrations dans le volant a certaines vitesses
  - Roue anormalement chaude apres roulage
  - Bruit de frottement ou de craquement
  good_practices:
  - Controle du jeu de direction a chaque revision
  - Verifier les soufflets de protection (pas de fuite de graisse)
  - Faire verifier la geometrie apres remplacement
  - Inspecter les biellettes et rotules associees
rendering:
  pgId: '655'
  intro_title: A quoi sert Roulement de roue ?
  risk_title: Pourquoi remplacer Roulement de roue a temps ?
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
  - question: Roulement de roue OE ou adaptable ?
    answer: 'OES (SKF, FAG, SNR) sont excellents. Vérifiez le type : roulement seul, avec moyeu intégré ou kit complet.'
  - question: Comment savoir si mon roulement de roue est usé ?
    answer: Ronronnement qui varie avec la vitesse, bruit qui change en virage, jeu en secouant la roue, vibrations au volant.
  - question: Tous les combien changer le roulement de roue ?
    answer: Entre 120 000 et 200 000 km. Durée de vie variable. Un roulement peut lâcher avant l'autre.
  - question: Peut-on changer le roulement de roue soi-même ?
    answer: 'Dépend du type. Roulement-moyeu intégré : facile. Roulement à presser : nécessite presse hydraulique.'
  - question: Quelle erreur éviter avec le roulement de roue ?
    answer: Ne pas serrer l'écrou de moyeu au couple exact (trop serré = destruction). Ne pas réutiliser l'écrou si à usage
      unique.
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
doc_id: 32acb057-3062-513a-984e-98ec764ffa5d
content_hash: sha256:f1c9f4271fdb1786
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
  area: Sous le vehicule, relie le volant aux roues
  access: Par le dessous (pont elevateur recommande)
  adjacent_parts:
  - cremailliere
  - biellette
  - rotule
  - soufflet
installation:
  difficulty: difficile
  time: 1h a 3h
  tools:
  - cle a douille
  - arrache-rotule
  - cle dynamometrique
  prerequisite: Pont elevateur, geometrie a refaire apres
phase5_enrichment:
  _source: aftermarket.zf.com + ate-freinage.fr + bremboparts.com + delphiautoparts.com + ferodo.com + hella.com + textar.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 37
  _has_tech_data: true
  types_variants:
  - type: 'Composite'
    source_ref: corpus RAG web OEM
  - type: 'Hall'
    source_ref: corpus RAG web OEM
  - type: 'bi-matière'
    source_ref: corpus RAG web OEM
  - type: 'composite'
    source_ref: corpus RAG web OEM
  - type: 'céramique'
    source_ref: corpus RAG web OEM
  - type: 'hydraulique'
    source_ref: corpus RAG web OEM
  - type: 'inductif'
    source_ref: corpus RAG web OEM
  - type: 'plein'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    norme_ece_r90: 'ECE R90'
    norme_sae_j2521: 'SAE J2521'
    val_0_001_mm: '0,001 mm'
    val_0_015_mm: '0,015 mm'
    val_0_03_mm: '0,03 mm'
    val_0_035_mm: '0,035 mm'
    val_0_05_mm: '0,05 mm'
    val_0_050_mm: '0,050 mm'
    val_0_070_mm: '0,070 mm'
    val_0_1_km: '0,1 km'
    val_0_1_mm: '0,1 mm'
    val_0_10_mm: '0,10 mm'
    val_0_12_mm: '0,12 mm'
    val_0_15_mm: '0,15 mm'
    val_000_km: '000 km'
    val_1_5_mm: '1,5 mm'
    val_1__v: '1. V'
  materials:
  - materiau: 'EPDM'
    source_ref: corpus RAG web OEM
  - materiau: 'HNBR'
    source_ref: corpus RAG web OEM
  - materiau: 'acier inoxydable'
    source_ref: corpus RAG web OEM
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
  S1: 'Le roulement de roue est un élément essentielassurant la rotation de la roue, par rapport au châssis de lavoiture,
    toute en supportant les charges appliquées sur la roue. Fonctions principales : - La transmission desefforts de la roue.
    - La rotation des piècestournantes roue, disque de frein et moyeu de roue. - Le fonctionnement descomposants du demi-train
    selon les circonstances d''utilisation duvéhicule : vibrations, corrosion, température. Les roulements de roues ont une
    influence directesur le roulis et la mobilité du véhicule. Le roulement de roue se compose d''unebague extérieure et une
    bague intérieure, qui maintiennent et sépare les piècesde roulement. La bague intérieure et la bague extérieure, forment
    le chemin deroulement. En savoir plus : roulement de roue — définition et rôle mécanique 🚨 Bruit Roulement de roue : causes
    et diagnostic'
  S2: 'Un roulement de roue défaillant présente plusieurs symptômes : - Des bruits de frottement lorsquela roue est en rotation.
    - Des vibrations et un bruitsourd dans l''ensemble de votre habitacle. Un roulement de roue défectueux va endommager le
    moyeu deroue et l''axe de la roue s''il n''est pas remplacé rapidement et il aura unimpact sur la mobilité de votre roue
    et sur la qualité du freinage. Diagnostic complet : identifier une panne de roulement de roue'
  S3: 'Le roulement de roue permet la rotation libre de la roue sur le porte-moyeu. Un roulement inadapté provoquera du jeu,
    du bruit et une usure prématurée du moyeu.Vérifications indispensables- Génération du roulement : 1ère génération (conique
    à régler), 2ème génération (roulement seul pré-assemblé) ou 3ème génération (intégré au moyeu avec capteur ABS)- Dimensions
    : diamètre intérieur, diamètre extérieur et largeur — mesurer avec un pied à coulisse sur le roulement déposé- Essieu
    : avant ou arrière — les dimensions et le type diffèrent souvent- Présence du capteur ABS : certains roulements 3ème génération
    intègrent la bague ABS magnétique, vérifier la compatibilitéMéthode de vérificationIdentifier la génération de roulement.
    Comparer la référence OE. Pour les roulements 1ère génération, noter le couple conique intérieur + extérieur.Pour aller
    plus loin : consultez notre guide d''achat roulement de roue — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 📖 Avant de démonter, consultez la fiche technique Roulement de roue pour connaître les spécifications. - Levez
    et calez le véhicule. - Démontez la roue. - Démontez la rotule de suspension. - Démontez l'étrier de frein etle disque
    de frein. - Démontez la rotule dedirection. - Démontez la fusée d'essieu. - Calez la fusée d'essieudans une presse. -
    Extraire le moyeu de roue. - Retirez le clip de maintiendu roulement de roue. - Extraire le roulement de roue de lafusée
    à l'aide d'une presse.
  S4_REPOSE: 'Le remontage d''un roulement de roue requiert une précision mécanique rigoureuse : le serrage de l''écrou de
    moyeu au couple exact conditionne directement la durée de vie du roulement. Un couple insuffisant crée du jeu ; un couple
    excessif détruit les billes dès les premiers kilomètres. Si votre véhicule dispose d''un ABS, vérifiez l''intégrité de
    la bague de déclenchement avant de refermer. - Vérifiez que le roulement de roue neuf est identique à celui démonté :
    diamètre intérieur et extérieur, type (roulement seul, avec moyeu intégré, ou kit complet), présence de la bague ABS encodeur.
    - Pour les roulements de roue arrière sur véhicules ABS, vérifiez que la bague ABS est intégrée au nouveau roulement ou
    au disque de frein arrière — ne pas confondre les deux configurations selon le modèle. - Contrôlez l''état du capteur
    ABS : nettoyez la face de lecture ou remplacez le capteur si le jeu entre bague et capteur dépasse 1,2 mm, pour éviter
    un défaut de lecture après remontage. - Nettoyez soigneusement le logement du roulement dans le moyeu ou le porte-fusée
    avec un chiffon propre — toute poussière ou particule métallique abimera le nouveau roulement lors de la mise en service.
    - Pressez ou vissez le nouveau roulement de roue dans son logement en poussant uniquement sur la bague extérieure (jamais
    sur la bague intérieure pour un roulement à presser), jusqu''à venue en butée franche. - Contrôlez l''état de la rotule
    de suspension et du demi-arbre de transmission accessibles lors de la dépose : remplacez toute rotule avec jeu ou tout
    soufflet de transmission fendu. - Remontez l''étrier de frein et les disques de frein — si la roue était anormalement
    chaude avant la défaillance du roulement, inspectez le disque pour toute déformation thermique. - Montez un écrou de moyeu
    neuf (à usage unique sur la plupart des véhicules modernes) et serrez au couple constructeur exact — typiquement entre
    180 et 280 N·m selon le véhicule. Utilisez une clé dynamométrique, pas d''estimation au ressenti. - Fraisez ou inservez
    la goupille de freinage de l''écrou si le système en dispose, pour bloquer tout desserrage en service. - Remontez la roue,
    reposez le véhicule au sol, puis effectuez un roulage de contrôle en variant la vitesse entre 40 et 90 km/h pour vérifier
    l''absence de ronronnement résiduel et de vibrations au volant.'
  S5: '- Frapper directement sur le roulement au marteau — les billes ou rouleaux s''endommagent, le roulement neuf sera bruyant
    dès le montage → utiliser un tube d''appui sur la bague extérieure et une presse hydraulique- Confondre les générations
    de roulement — un roulement 2ème génération ne remplace pas un 3ème génération (moyeu intégré) → identifier la génération
    avant commande- Oublier le capteur ou la bague ABS — le voyant ABS restera allumé et le système de freinage d''urgence
    sera inopérant → vérifier la présence et l''orientation correcte de la bague magnétique- Ne pas remplacer l''écrou de
    moyeu — l''écrou perd son pouvoir de freinage après le premier serrage → utiliser systématiquement un écrou neuf, serrer
    au couple (175-280 Nm)- Oublier d''enduire le logement — le roulement suivant sera impossible à extraire → appliquer une
    fine couche de graisse cuivrée sur le logement du porte-moyeu avant insertion- Monter le roulement de travers — le roulement
    forcé de biais se détruira en quelques centaines de km → aligner parfaitement avant de presser, vérifier la perpendicularité-
    Négliger l''état du porte-moyeu — un logement ovalisé ou rayé ne retiendra pas le roulement neuf → vérifier l''état du
    logement, remplacer le porte-moyeu si nécessaire- Régler un jeu incorrect sur roulement conique — trop serré il chauffe
    et grille, trop lâche il crée du jeu → respecter la procédure : serrer, relâcher d''un quart de tour, vérifier le jeu
    axial (0.02-0.05 mm)'
  S6: 'Contrôles statiques (véhicule au sol)- Serrer l''écrou de moyeu au couple constructeur (175-280 Nm selon modèle)- Soulever
    la roue et la faire tourner à la main : rotation libre et silencieuse, sans point dur- Secouer la roue à 12h-6h puis 9h-3h
    : aucun jeu ne doit être perceptible- Vérifier que le voyant ABS s''éteint après démarrage (si roulement avec capteur
    intégré)Test routier progressif- Rouler à 30 km/h : pas de grondement sourd ni de ronronnement cyclique- Rouler à 60 km/h
    et incliner légèrement le volant à gauche puis à droite : un roulement défaillant change de tonalité selon la charge-
    Accélérer à 90 km/h : absence de vibration dans le plancher ou le volant- Freiner fermement : pas de pulsation ni de tirage
    latéral⚠️ Important : Si un grondement persiste après remplacement, vérifiez que le roulement est correctement pressé
    (pas de biais) et que l''écrou de moyeu est au bon couple. Un bruit de roulement peut aussi provenir du côté opposé —
    toujours confirmer le côté défaillant avant intervention.'
  S7: Quel est le prix d'un roulement de roue ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur pour
    trouver le roulement de roue compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon roulement de roue est à changer ?Les signes d'usure les plus courants sont détaillés dans la section diagnostic
    ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un roulement de roue défaillant
    ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule. Consultez la section
    symptômes pour évaluer l'urgence du remplacement.Lors du remplacement d'un roulement de roue, inspectez ces pièces connexes
    :- Écrou de moyeu — toujours remplacer par un écrou neuf (auto-freiné ou à créneaux + goupille)- Capteur ABS — vérifier
    le câble et le connecteur, nettoyer la portée magnétique si capteur séparé- Disque de frein — un voilage de disque peut
    être causé par un roulement usé, vérifier le faux-rond- Cardan — le joint homocinétique côté roue est accessible, vérifier
    l'état du soufflet- Rotule de suspension — vérifier l'absence de jeu car l'accès est dégagé- Porte-moyeu — vérifier l'état
    du logement (pas d'ovalisation ni de rayures profondes)
  S8: 'Comment reconnaître un roulement de roue usé ?Le symptôme le plus courant est un grondement sourd qui augmente avec
    la vitesse et change de tonalité en virage. Pour identifier le côté : si le bruit diminue en tournant à gauche, c''est
    le roulement droit qui est en cause (et inversement). Un jeu perceptible en secouant la roue confirme le diagnostic.Faut-il
    changer les deux roulements en même temps ?Non, contrairement aux amortisseurs ou aux plaquettes, les roulements s''usent
    indépendamment. Remplacez uniquement le roulement défaillant. Cependant, si le véhicule a plus de 150 000 km et que l''un
    est usé, surveillez l''autre de près.Quelle est la durée de vie d''un roulement de roue ?Un roulement de qualité dure
    entre 100 000 et 200 000 km. Les facteurs d''usure accélérée sont les nids-de-poule, le passage de gué (eau), le chargement
    excessif et un montage incorrect (biais, couple inadapté). Les roulements bas de gamme peuvent ne durer que 30 000 km.Peut-
    on rouler avec un roulement qui gronde ?Un roulement qui commence à gronder peut encore fonctionner quelques milliers
    de km, mais le risque augmente avec le temps. Un roulement très usé peut se bloquer brutalement ou se désintégrer, entraînant
    la perte de la roue. Ne tardez pas à le remplacer, surtout si du jeu est détectable.Roulement de marque constructeur ou
    adaptable ?Les roulements de marques reconnues (SKF, SNR, FAG, NTN) offrent une qualité équivalente à l''origine pour
    un prix inférieur de 20-40 %. Évitez les roulements sans marque ou très bon marché : leur durée de vie est souvent 3 à
    5 fois plus courte, ce qui annule l''économie initiale.'
  META: 'Remplacement roulement de roue : identifier la génération, erreurs de montage, vérifications et FAQ. Guide technique
    pour un montage sans bruit.'
---

# Roulement de roue - Guide Diagnostic Complet

## Fonction et Rôle

Permettre la rotation libre de la roue sur son axe - Supporte les charges radiales et axiales

**Actions principales:** permettre la rotation, supporter, guider, rouler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- ronronnement grondement augmente vitesse
- bruit qui change d intensite dans les virages
- jeu perceptible en secouant la roue montee
- vibrations dans le volant a certaines vitesses
- roue anormalement chaude apres roulage
- bruit de frottement ou de craquement

## Procédure de Diagnostic

Pour diagnostiquer un problème de roulement de roue:

1. **Inspection visuelle** - Examiner l'état du roulement de roue
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
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

- capteur-abs
- disque-de-frein
- plaquette-de-frein

## Critères de Compatibilité

Pour commander le bon roulement de roue, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"

## FAQ

**Roulement de roue OE ou adaptable ?**
OES (SKF, FAG, SNR) sont excellents. Vérifiez le type : roulement seul, avec moyeu intégré ou kit complet.

**Comment savoir si mon roulement de roue est usé ?**
Ronronnement qui varie avec la vitesse, bruit qui change en virage, jeu en secouant la roue, vibrations au volant.

**Tous les combien changer le roulement de roue ?**
Entre 120 000 et 200 000 km. Durée de vie variable. Un roulement peut lâcher avant l'autre.

**Peut-on changer le roulement de roue soi-même ?**
Dépend du type. Roulement-moyeu intégré : facile. Roulement à presser : nécessite presse hydraulique.

**Quelle erreur éviter avec le roulement de roue ?**
Ne pas serrer l'écrou de moyeu au couple exact (trop serré = destruction). Ne pas réutiliser l'écrou si à usage unique.


## References supplementaires

<!-- materialized-from-db manual/850f2d8bdc0c 2026-04-02 -->
### Données techniques OEM — Montage maitrise

# Données techniques OEM — Montage maitrise
Source : ate-freinage.fr + bremboparts.com + delphiautoparts.com + ferodo.com + textar.com (33 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- bi-matière
- composite
- hydraulique
- électrique

## Normes applicables
- ECE R90

## Matériaux
- EPDM
- HNBR
- acier inoxydable
- fonte grise

## Valeurs techniques de référence
- 0,035 mm
- 0,05 mm
- 0,050 mm
- 0,1 mm
- 0,10 mm
- 0,12 mm
- 0,15 mm
- 10 Nm
- 100 Nm
- 115 Nm
- 120 Nm
