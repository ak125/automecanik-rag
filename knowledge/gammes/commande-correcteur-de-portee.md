---
category: eclairage
slug: commande-correcteur-de-portee
title: Commande correcteur de portée
pg_id: 1432
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
  role: Interface permettant au conducteur de régler la hauteur des phares depuis l'habitacle
  must_be_true:
  - commander
  - activer
  - regler
  must_not_contain:
  - ampoule
  - feu
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - ampoule-feu-avant
  - ampoule-feu-arriere
  - feu-avant
  - feu-arriere
  - phares-antibrouillard
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de compatibilite
    pour confirmer Commande correcteur de portée.
  - Verifier le type d ampoule (H1, H4, H7, LED, xenon) compatible avec le vehicule
  - Respecter la puissance et le culot exact de l ampoule d origine
  - Choisir des ampoules homologuees pour la circulation routiere
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "visibilite parfaite"
  cost_range:
    min: 30
    max: 200
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Equipement d origine (OE)
  - tier: Equivalent OE
  - tier: Piece adaptable
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
    label: Molette de reglage inactive
    severity: confort
  - id: S2
    label: Phares bloques en position haute basse
    severity: immobilisation
  - id: S3
    label: Voyant defaut eclairage
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - lecture codes defaut obd et diagnostic electronique
  - 'Usure ou defaillance causant : molette de reglage inactive'
  quick_checks:
  - 'Observer : molette de reglage inactive ?'
  - 'Observer : phares bloques en position haute basse ?'
  - Voyant defaut eclairage ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Molette de reglage inactive
  - Phares bloques en position haute basse
  - Voyant defaut eclairage
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '1432'
  intro_title: A quoi sert Commande correcteur de portée ?
  risk_title: Pourquoi remplacer Commande correcteur de portée a temps ?
  risk_explanation: '**Pièce HS** - Le commande correcteur de portée peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le commande correcteur de portée peut être hors service et nécessiter un remplacement'
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
  - question: Comment choisir Commande correcteur de portée compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Commande correcteur de portée ?
    answer: En cas de molette de reglage inactive ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Commande correcteur de portée sans verification atelier ?
    answer: Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure
      constructeur.
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
doc_id: 48639c94-931a-5602-991c-13530413b995
content_hash: sha256:7e657d03744c4854
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
  - type: 'Organique'
    source_ref: corpus RAG web OEM
  - type: 'organique'
    source_ref: corpus RAG web OEM
  technical_notes:
    norme_iso_13666: 'ISO 13666'
    val_100__: '100 %'
    val_13_a: '13 a'
    val_16_a: '16 a'
    val_18_a: '18 a'
    val_3_a: '3 a'
    val_30__: '30 %'
    val_335_nm: '335 nm'
    val_355_nm: '355 nm'
    val_380_nm: '380 nm'
    val_400_nm: '400 nm'
    val_42_a: '42 a'
    val_5__: '5 %'
    val_5_a: '5 a'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: La commande de correcteur de portée est l'interface conducteur qui permet de régler la hauteur d'orientation des faisceaux
    lumineux des phares depuis l'intérieur de l'habitacle, sans intervention manuelle sur les phares. Elle se présente sous
    forme d'une molette rotative ou d'un potentiomètre généralement situé sur la planche de bord, à gauche du volant ou dans
    le combiné de commandes d'éclairage. En tournant cette molette sur les positions graduées (0, 1, 2, 3 ou plus selon le
    véhicule), le conducteur commande et active les correcteurs de portée électriques — des servomoteurs ou des actionneurs
    hydrauliques fixés à l'arrière de chaque phare. Ces actionneurs modifient l'inclinaison du réflecteur ou du projecteur
    pour adapter l'angle du faisceau lumineux à la charge du véhicule. Cette correction est nécessaire car un véhicule chargé
    à l'arrière (coffre plein, passagers) voit sa garde au sol arrière s'abaisser et son avant se soulever, ce qui oriente
    les phares vers le haut et éblouit les conducteurs en sens inverse. La molette permet de corriger cette orientation en
    abaissant le faisceau selon la charge. Les pièces directement associées à cette commande sont le correcteur de portée
    (actionneur sur le phare) et le feu avant (phare) lui-même.
  S2: 'Une commande de correcteur de portée défaillante se traduit par une perte de contrôle de l''orientation des phares
    depuis l''habitacle. Les conséquences vont d''une gêne de confort à une situation dangereuse selon le degré de défaillance
    et la position de blocage. - Molette de réglage inactive : tourner la molette n''a aucun effet visible sur les phares
    — les faisceaux restent dans la même position quelle que soit la graduation sélectionnée. Ce symptôme peut provenir de
    la commande elle-même (potentiomètre HS) ou du connecteur électrique en défaut. - Phares bloqués en position haute : les
    faisceaux restent orientés vers le haut en permanence, éblouissant systématiquement les conducteurs en face. Cette situation
    est particulièrement dangereuse de nuit et peut conduire à un refus au contrôle technique. - Phares bloqués en position
    basse : les faisceaux pointent vers le sol à quelques mètres devant le véhicule, réduisant drastiquement la portée d''éclairage
    de nuit. La visibilité est réduite à moins de 20 mètres au lieu des 60 à 100 mètres normaux — situation à risque sur route.
    - Voyant de défaut éclairage au tableau de bord : sur les véhicules équipés d''un système de correction de portée automatique
    ou d''un calculateur d''éclairage, un défaut de circuit de la commande peut allumer un voyant dédié ou un message d''alerte
    dans le combiné. - Position 0 différente de la position d''origine : si les phares ne reviennent pas à leur position d''équilibre
    standard lorsque la molette est sur 0, le potentiomètre de la commande est usé et envoie une valeur de tension décalée
    au correcteur de portée.'
  S3: 'La commande de correcteur de portée est une pièce spécifique à un modèle de véhicule. Sa compatibilité dépend non seulement
    du modèle commercial mais aussi de la version d''équipement et de l''année de production, car les constructeurs modifient
    les combinés de commandes au fil des millésimes. - Renseigner marque, modèle, type et année de production exacte : une
    commande compatible doit correspondre à la référence OEM du véhicule. Une différence de millésime peut suffire à rendre
    une pièce incompatible (connecteur différent, loi de résistance du potentiomètre modifiée). - Vérifier la référence d''origine
    sur la pièce défaillante : la référence constructeur est généralement imprimée ou gravée sur le corps de la commande.
    Cette référence permet d''identifier la pièce de remplacement exacte chez un équipementier ou chez le constructeur. -
    Contrôler le connecteur et le nombre de broches : les connecteurs de commandes de tableau de bord varient (4, 6 ou 8 broches
    selon les véhicules). Un connecteur incompatible rend le montage impossible sans modification du faisceau. - Vérifier
    si la commande est intégrée à un combiné multifonctions : sur de nombreux véhicules, la commande de correcteur de portée
    est intégrée dans le même boîtier que les commandes d''éclairage, de brouillards ou du rétroviseur électrique. Dans ce
    cas, il faut remplacer le combiné complet, ce qui change la nature de la pièce à commander. - Diagnostiquer le correcteur
    de portée avant de remplacer la commande : si les actionneurs sur les phares sont défaillants, remplacer la commande ne
    résoudra pas le problème. Vérifier d''abord que les correcteurs de portée répondent lorsqu''on leur applique directement
    une tension (test court-circuit maîtrisé) avant de conclure à une commande HS. Pour aller plus loin : consultez notre
    guide d''achat commande correcteur de portée — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 'Le remplacement d''une commande de correcteur de portée est une opération accessible au particulier bricoleur.
    Elle implique la dépose d''un élément du tableau de bord et nécessite de débrancher la batterie pour éviter tout risque
    électrique. - Débrancher la batterie : déconnecter la borne négative (-) de la batterie avant toute intervention électronique
    sur le tableau de bord. Attendre 2 minutes après déconnexion pour permettre la décharge des condensateurs des airbags.
    - Localiser la commande à remplacer : elle est généralement intégrée dans le combiné de commandes d''éclairage à gauche
    du volant, ou sur la planche de bord centrale selon le modèle. Photographier la position et le câblage avant de toucher
    quoi que ce soit. - Déposer le cache ou le panneau entourant la commande : utiliser des outils de démontage plastique
    pour lever les clips et retirer le panneau sans abîmer les garnitures. La plupart des panneaux de tableau de bord sont
    maintenus par des clips plastiques sans vis apparentes. - Débrancher le connecteur de la commande : appuyer sur le clip
    de rétention du connecteur et le retirer doucement. Note : certains véhicules utilisent un connecteur verrouillé qui nécessite
    d''appuyer sur un loquet secondaire avant de pouvoir extraire le connecteur. - Déposer la commande : elle est généralement
    maintenue par 2 à 4 vis Torx ou par des clips de rétention. Retirer les vis ou dégager les clips, puis extraire la commande.
    - Monter la commande neuve : placer la commande neuve dans son logement, la fixer avec les vis ou enclencher les clips.
    Rebrancher le connecteur jusqu''au clic. - Remonter les panneaux et reconnecter la batterie : remettre en place dans l''ordre
    inverse. Reconnecter la borne négative de la batterie. - Tester le fonctionnement : allumer les phares, tester chaque
    position de la molette et vérifier visuellement que les faisceaux bougent effectivement. Effacer les codes défaut OBD
    si un voyant était présent.'
  S4_REPOSE: 'Le remontage de la commande de correcteur de portée est la séquence inverse de la dépose, réalisée en intégralité
    avant de reconnecter la batterie. Le point de validation critique est la vérification du mouvement effectif des faisceaux
    lors du test fonctionnel de la molette. - Présenter la commande neuve dans son logement : orienter correctement la commande
    en respectant la position d''origine photographiée lors de la dépose. Sur les véhicules où la commande est intégrée au
    combiné de commandes d''éclairage, s''assurer que les autres fonctions du combiné (clignotants, feux de route) sont en
    position neutre avant l''insertion. - Fixer la commande avec ses vis ou ses clips : revisser les vis (généralement Torx
    T20 ou T25) au couple normal sans forcer — les vis de tableau de bord tiennent dans du plastique. Si la commande est maintenue
    par des clips, les enclencher méthodiquement en commençant par les clips de positionnement, puis les clips de verrouillage.
    - Rebrancher le connecteur de la commande : enclencher le connecteur dans son logement jusqu''au clic de verrouillage.
    Sur les connecteurs à loquet secondaire (commun sur les commandes électroniques de tableau de bord), verrouiller ce loquet
    secondaire après avoir encliqueté le connecteur principal. Un connecteur mal verrouillé se débranche aux vibrations et
    provoque une défaillance intermittente. - Remettre en place le panneau de tableau de bord : repositionner le panneau ou
    le cache en commençant par les clips les plus difficiles d''accès. Appuyer ferme et régulièrement le long du bord du panneau
    pour enclencher les clips plastique sans les casser. Vérifier que le panneau est parfaitement affleurant sans jeu ni craquement.
    - Reconnecter la borne négative de la batterie : après reconnexion, attendre 30 secondes avant d''allumer le contact pour
    permettre aux modules électroniques de s''initialiser. - Allumer les phares et tester immédiatement la molette : avec
    les phares allumés, faire tourner la molette de la position 0 à la position maximale et observer les faisceaux. Les faisceaux
    doivent se déplacer visiblement et sans à-coup. Sur les véhicules avec correcteur électrique (motorisé), le mouvement
    est plus fluide que sur un correcteur mécanique. - Effacer les codes défaut OBD si un voyant d''éclairage était allumé
    avant l''intervention, et vérifier l''absence de nouveau code après test. - Vérifier le réglage de base des phares : si
    le correcteur de portée avait été en panne depuis un certain temps, les phares peuvent être restés dans une position incorrecte
    (trop haute ou trop basse). Régler la position de base (position 0 de la molette) selon les préconisations constructeur
    et le type de chargement du véhicule.'
  S5: 'Plusieurs erreurs de diagnostic ou de montage peuvent compliquer l''intervention sur une commande de correcteur de
    portée ou conduire à remplacer la mauvaise pièce. - Ne pas débrancher la batterie avant l''intervention : travailler sur
    le tableau de bord sans couper l''alimentation expose à des court-circuits sur les nappes de câbles denses du tableau
    de bord, ou dans le pire cas à un déclenchement accidentel des airbags si un connecteur est perturbé. Le débranchement
    de la batterie est obligatoire. - Remplacer la commande sans vérifier les correcteurs de portée sur les phares : si les
    actionneurs de correction sur les phares sont gripés ou en court-circuit, la commande neuve enverra des signaux qui ne
    seront pas exécutés. Vérifier le fonctionnement électrique des actionneurs avec un multimètre avant de conclure à une
    commande HS. - Commander une pièce sans vérifier l''intégration dans un combiné multifonctions : sur de nombreux véhicules,
    la commande de correcteur de portée est intégrée dans un bloc qui gère aussi les brouillards ou l''éclairage ambiant.
    Commander une pièce isolée alors que seul le bloc complet existe en pièce de rechange entraîne une perte de temps. - Forcer
    les clips plastiques du tableau de bord : les clips des panneaux de tableau de bord en plastique sont fragiles. Les forcer
    sans outil adapté casse les clips et oblige à remplacer le panneau. Utiliser systématiquement des démonte-panneaux plastique.
    - Oublier de coder la pièce si nécessaire : sur certains véhicules récents, un remplacement de composant du tableau de
    bord nécessite un codage via l''outil de diagnostic constructeur. Sans ce codage, la pièce neuve peut être reconnue en
    défaut par le calculateur.'
  S6: 'Après le montage d''une commande de correcteur de portée neuve, les vérifications portent sur la conformité du réglage
    des phares et l''absence de codes défaut résiduels. - Test de toutes les positions de la molette : allumer les phares
    et tourner la molette de la position 0 à la position maximale (3 ou 4 selon le véhicule) en observant le mouvement des
    faisceaux projetés sur un mur ou le sol. Chaque position doit produire un déplacement visible et progressif du faisceau
    vers le bas. - Vérification de la position 0 comme position haute : en position 0 (sans charge), les phares doivent être
    orientés à la hauteur maximale autorisée — celle qui correspond au réglage d''usine pour un véhicule vide. Si les phares
    pointent trop haut même en position 0, un réglage des correcteurs de portée est nécessaire. - Lecture des codes défaut
    OBD : effacer les codes mémorisés liés au circuit d''éclairage et vérifier après 5 minutes de fonctionnement qu''aucun
    nouveau code n''apparaît. - Contrôle de l''absence de voyant tableau de bord : s''assurer que tous les voyants liés à
    l''éclairage sont éteints après le test de fonctionnement des phares. - Vérification du réglage réglementaire des phares
    : si les phares n''ont pas été réglés depuis longtemps ou si le correcteur avait été bloqué en position haute, un passage
    chez un carrossier ou un centre de contrôle technique pour le réglage optique des phares est conseillé avant le prochain
    contrôle technique.'
  S7: 'La commande de correcteur de portée fait partie d''un système qui va de la molette habitacle jusqu''aux actionneurs
    sur les phares. Plusieurs composants de cette chaîne peuvent être défaillants indépendamment de la commande elle- même.
    - Correcteur de portée (actionneur sur le phare) : le correcteur est le composant qui pivote physiquement le réflecteur
    à l''intérieur du phare. Si la molette de commande est neuve mais que les faisceaux ne bougent toujours pas, l''actionneur
    sur le phare lui-même est défaillant. Il est spécifique à chaque phare. - Phare avant complet : sur certains véhicules
    modernes, le correcteur de portée est intégré au bloc optique et non remplaçable séparément. Si l''actionneur est défaillant
    et non disponible en pièce détachée, le phare complet doit être remplacé. - Harnais de câblage du correcteur : le câblage
    entre la commande et les actionneurs peut se frotter, se couper ou présenter de l''oxydation aux connecteurs. Un câblage
    endommagé donne les mêmes symptômes qu''une commande HS avec une commande neuve. - Capteur de hauteur d''assiette (pour
    correcteurs automatiques) : les véhicules équipés de correcteurs automatiques (xenon, LED) utilisent un capteur de hauteur
    d''assiette sur l''essieu arrière pour calculer le réglage en temps réel. Ce capteur peut tomber en panne et bloquer le
    système correcteur indépendamment de la commande manuelle.'
  S8: Comment savoir si c'est la commande ou le correcteur de portée qui est défaillant ? Le test le plus simple est de déposer
    le connecteur du correcteur de portée sur le phare et d'appliquer directement la tension d'alimentation (12V DC) selon
    le schéma électrique du véhicule. Si l'actionneur bouge, le correcteur de portée fonctionne et la panne vient de la commande
    ou du câblage. Si l'actionneur ne bouge pas même avec une tension directe, c'est le correcteur de portée qui est défaillant.
    Un multimètre sur les bornes de la commande permet également de vérifier si elle envoie bien une variation de tension
    lors du réglage de la molette. Quand doit-on remplacer la commande de correcteur de portée ? La commande est à remplacer
    lorsque la molette devient inactive, que les phares se bloquent dans une position fixe, ou qu'un code défaut de circuit
    de correcteur de portée est confirmé après vérification du câblage et des actionneurs. La pièce n'a pas de périodicité
    d'entretien — elle dure généralement toute la vie du véhicule dans des conditions normales d'utilisation. Peut-on monter
    cette commande sans aller en atelier ? Oui pour la grande majorité des véhicules — la dépose d'un panneau de tableau de
    bord et l'échange du composant sont accessibles avec les bons outils de démontage plastique et en prenant soin de débrancher
    la batterie. Toutefois, si le véhicule nécessite un codage du composant après remplacement (certains modèles récents Volkswagen,
    BMW ou Mercedes), un outil de diagnostic compatible est nécessaire — ce qui peut justifier un passage en atelier pour
    cette étape. Le correcteur de portée est-il obligatoire au contrôle technique ? Oui. Le système de correction de portée
    des phares est contrôlé lors du contrôle technique. Des phares bloqués en position haute (éblouissant les autres conducteurs)
    ou un système de correction inopérant constitue une défaillance majeure qui peut entraîner un refus. Le réglage et le
    bon fonctionnement du correcteur sont des points de contrôle obligatoires depuis 2018 en France.
---

# Commande correcteur de portée - Guide Diagnostic Complet

## Fonction et Rôle

Interface permettant au conducteur de régler la hauteur des phares depuis l'habitacle

**Actions principales:** commander, activer, regler

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Phares bloques en position haute basse**
  phares bloques en position haute basse

### 🟢 Autres Symptômes

- molette de reglage inactive
- voyant defaut eclairage

## Procédure de Diagnostic

Pour diagnostiquer un problème de commande correcteur de portée:

1. **Inspection visuelle** - Examiner l'état du commande correcteur de portée
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le commande correcteur de portée peut être hors service et nécessiter un remplacement
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- correcteur-de-portee
- feu-avant

## Critères de Compatibilité

Pour commander le bon commande correcteur de portée, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "visibilite parfaite"

## FAQ

**Comment choisir Commande correcteur de portée compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Commande correcteur de portée ?**
En cas de molette de reglage inactive ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Commande correcteur de portée sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
