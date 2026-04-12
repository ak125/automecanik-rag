---
category: eclairage
slug: correcteur-de-portee
title: Correcteur de portée
pg_id: 700
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
  role: Règle la hauteur du faisceau lumineux en fonction de la charge du véhicule
  must_be_true:
  - regler
  - ajuster
  - adapter
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
    pour confirmer Correcteur de portée.
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
    label: Phares mal orientés
    severity: confort
  - id: S2
    label: Eblouissement
    severity: confort
  - id: S3
    label: Reglage impossible
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'Usure ou defaillance causant : phares mal orientés'
  - 'Usure ou defaillance causant : eblouissement'
  quick_checks:
  - 'Observer : phares mal orientés ?'
  - 'Observer : eblouissement ?'
  - 'Observer : reglage impossible ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Phares mal orientés
  - Eblouissement
  - Reglage impossible
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '700'
  intro_title: A quoi sert Correcteur de portée ?
  risk_title: Pourquoi remplacer Correcteur de portée a temps ?
  risk_explanation: '**Défaillance progressive** - Usure normale due à l''utilisation'
  risk_consequences:
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
  - question: Comment choisir Correcteur de portée compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Correcteur de portée ?
    answer: En cas de phares mal orientés ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Correcteur de portée sans verification atelier ?
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
doc_id: 463dda70-8518-50ff-bbcd-6302e7184af2
content_hash: sha256:6b8347359fe4e7bc
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
  S1: 'Le correcteur de portée est le mécanisme électrique ou électromécanique qui ajuste automatiquement ou manuellement
    l''inclinaison verticale des projecteurs avant en fonction de la charge transportée par le véhicule. Son rôle est de maintenir
    le faisceau lumineux parallèle à la route quelle que soit la charge à bord, garantissant ainsi une visibilité nocturne
    optimale sans éblouir les autres usagers. Lorsque le véhicule est chargé à l''arrière (passagers supplémentaires, chargement
    de coffre, remorque), la suspension arrière s''affaisse et la proue se soulève légèrement, ce qui relève mécaniquement
    le faisceau des phares vers le haut. Sans correction, ce basculement éblouit les conducteurs venant en sens inverse à
    partir d''une certaine distance. Le correcteur de portée compense cet effet en abaissant l''angle d''émission du phare
    d''une valeur proportionnelle à l''enfoncement de la suspension. Il existe deux grandes familles : le correcteur manuel
    (actionné par une molette dans l''habitacle avec plusieurs positions de 0 à 3 ou 4) et le correcteur automatique (piloté
    par des capteurs de hauteur de caisse). Sur les véhicules récents avec feux à technologie LED ou Xénon, le correcteur
    automatique est obligatoire et fait partie intégrante du calculateur d''éclairage. Les pièces associées à vérifier en
    cas de dysfonctionnement sont le feu avant et la commande correcteur de portée.'
  S2: 'Un correcteur de portée défaillant compromet directement la sécurité routière nocturne et expose le conducteur à une
    verbalisation lors du contrôle technique, les phares mal orientés étant un motif de refus. Voici les signaux à surveiller.
    - Phares mal orientés en permanence vers le haut : le faisceau éclaire trop haut et éblouit systématiquement les véhicules
    venant en sens inverse, même véhicule à vide. C''est le symptôme le plus visible d''un correcteur bloqué en position haute
    ou d''un moteur de correcteur défaillant. - Phares orientés trop bas réduisant la visibilité : le correcteur bloqué en
    position maximale d''abaissement réduit la portée utile du faisceau à quelques mètres, rendant la conduite nocturne dangereuse
    sur route. - Réglage impossible depuis la commande habitacle : tourner la molette ou agir sur le réglage électronique
    ne produit aucun changement de l''orientation du phare. Le moteur du correcteur ne répond plus aux commandes. - Bruit
    de craquement ou de grincement dans le phare : le mécanisme d''actionnement du correcteur produit des bruits anormaux
    lors des tentatives de réglage, signe d''un engrenage usé ou d''un moteur électrique en fin de vie. - Mouvement saccadé
    ou tremblant du faisceau : le faisceau lumineux tremble ou se déplace par à-coups lors du passage de dos d''âne ou de
    changement de charge, indiquant un correcteur automatique dont le moteur présente une résistance variable. - Voyant de
    défaut d''éclairage au tableau de bord : sur les véhicules avec correcteur automatique piloté, le calculateur détecte
    la défaillance du moteur ou du capteur et allume un témoin d''anomalie lumière.'
  S3: 'Le choix d''un correcteur de portée de remplacement doit tenir compte non seulement du véhicule mais aussi du type
    de projecteur équipé, car les moteurs de correcteur sont conçus pour des débattements angulaires et des charges spécifiques.
    Voici les critères à vérifier. - Marque, modèle, année et version de finition : un même modèle de véhicule peut être équipé
    de projecteurs différents selon la finition (projecteur halogène sur la base, Xénon ou LED sur les finitions supérieures),
    chacun nécessitant un correcteur spécifique. - Type de technologie d''éclairage : les projecteurs Xénon (HID) et LED imposent
    réglementairement un correcteur automatique avec capteurs de hauteur de caisse. Les phares halogène peuvent être équipés
    d''un correcteur manuel. Un correcteur manuel ne peut pas remplacer un correcteur automatique. - Côté du projecteur :
    gauche ou droit : les correcteurs sont généralement miroirs l''un de l''autre, ou parfois identiques selon la conception
    du projecteur. Identifier précisément le côté défaillant avant de commander. - Débattement et course du moteur : le moteur
    doit avoir exactement la même course que l''original pour permettre les mêmes amplitudes de réglage. Une course trop longue
    ou trop courte fausse le réglage final du phare. - Tension d''alimentation et type de commande : vérifier que le correcteur
    fonctionne en 12V et que la commande (résistance variable, PWM ou bus LIN selon les véhicules récents) est compatible
    avec le boîtier de commande du véhicule. - Référence du projecteur d''origine : relever le numéro de référence inscrit
    sur le bloc optique du phare (souvent visible en ouvrant le capot). Cette référence est le meilleur moyen d''identifier
    le correcteur compatible. - Certification et qualité du moteur électrique interne : les correcteurs de bas de gamme utilisent
    des moteurs en plastique qui se fissure à basse température. Privilégier des pièces avec boîtier en matériau résistant
    aux variations thermiques importantes. Pour aller plus loin : consultez notre guide d''achat correcteur de portée — comparatif
    marques, critères de choix et prix.'
  S4_DEPOSE: 'Le remplacement d''un moteur de correcteur de portée est une intervention accessible sur la plupart des véhicules
    une fois le bloc optique accessible. La procédure varie légèrement selon que le correcteur est intégré au boîtier du phare
    ou accessible par l''arrière du projecteur. - Déconnexion de la batterie : couper l''alimentation électrique avant d''intervenir
    sur les projecteurs pour éviter tout arc électrique sur les connexions de faible intensité du correcteur. - Accès au correcteur
    par l''arrière du phare : selon le véhicule, l''accès se fait par le compartiment moteur (sans démontage du phare) ou
    nécessite la dépose complète du bloc optique. Identifier la meilleure voie d''accès en consultant les données constructeur.
    - Dépose du bloc optique si nécessaire : déconnecter le faisceau électrique et dévisser les fixations du projecteur (généralement
    3 à 4 vis). Dégager le bloc optique avec précaution en évitant de contraindre les câbles. - Localisation du moteur de
    correcteur sur le bloc optique : le moteur est un petit cylindre de 2 à 4 cm monté sur un axe fileté qui agit directement
    sur la glace ou le réflecteur du phare. Il est généralement accessible sur la face arrière du bloc optique. - Déconnexion
    du connecteur électrique : débrancher le connecteur du moteur de correcteur en appuyant sur le clip de verrouillage. Ne
    pas tirer sur les fils. - Dépose du moteur défaillant : tourner le moteur d''un quart de tour dans le sens antihoraire
    pour le déverrouiller de son logement (baïonnette), puis l''extraire. Sur certains modèles, deux vis maintiennent le moteur.
    - Pose du nouveau moteur : engager le nouveau moteur dans le logement et le verrouiller par rotation d''un quart de tour
    dans le sens horaire (ou visser). Reconnecter le connecteur électrique jusqu''au clic de verrouillage. - Remontage du
    bloc optique et réglage : remonter le phare, reconnecter la batterie, puis effectuer le réglage de la portée des phares
    sur un mur à 5 mètres ou sur une fosse de réglage. Le réglage final sur un banc de réglage homologué est recommandé pour
    la conformité au contrôle technique.'
  S4_REPOSE: 'Après la dépose du moteur de correcteur de portée défaillant, la repose du composant neuf et le réglage final
    de la portée des phares constituent les étapes critiques pour garantir la conformité au contrôle technique et la sécurité
    routière : - Vérifier la position de l''axe fileté avant la pose du nouveau moteur : le nouvel actionneur doit être positionné
    avec son axe fileté en position identique à l''ancien pour que la glace du phare soit dans la bonne position initiale.
    Si la documentation indique une position de référence (généralement milieu de course), y placer l''axe avant d''enficher
    le moteur. - Engager le moteur dans son logement par rotation : introduire le nouveau moteur dans le logement à baïonnette
    et tourner d''un quart de tour dans le sens horaire jusqu''au blocage. Ou visser les deux vis de fixation si le modèle
    est à vis. Vérifier que le moteur est fermement maintenu sans jeu. - Reconnecter le connecteur électrique jusqu''au clic
    de verrouillage : enficher le connecteur du moteur de correcteur en veillant à ne pas inverser le sens (détrompeur présent
    sur la plupart des connecteurs). Le clic de verrouillage confirme l''engagement correct. - Remonter le bloc optique sur
    le véhicule : si le phare avait été déposé, le repositionner soigneusement dans ses logements et serrer les 3 à 4 vis
    de fixation au couple normal. Reconnecter le faisceau électrique du phare (ampoule, feux de position, direction). - Remonter
    les protections de carrosserie déposées : replacer les caches moteur, protections d''aile ou bouclier avant dans leurs
    emplacements d''origine. Vérifier que chaque agrafe, clip et vis est correctement positionné. - Reconnecter la batterie
    et allumer les phares : rebrancher la borne négative de la batterie. Mettre le contact et allumer les phares. Vérifier
    que le voyant de correcteur de portée au tableau de bord (si présent) ne reste pas allumé en permanence. - Tester la commande
    de correcteur depuis l''habitacle : actionner le commutateur de correcteur de portée entre les positions 0, 1, 2 et 3
    (selon le véhicule) et vérifier que le faisceau se déplace visuellement vers le bas pour chaque cran. - Effectuer le réglage
    de la portée des phares : placer le véhicule à vide devant un mur blanc à 5 mètres, allumer les feux de croisement et
    marquer la hauteur du faisceau au centre. Ajuster avec la vis de réglage du phare jusqu''à la hauteur réglementaire. Un
    réglage sur banc de réglage homologué est recommandé pour la conformité au contrôle technique.'
  S5: 'Le remplacement d''un correcteur de portée est une intervention en apparence simple mais qui concentre plusieurs erreurs
    récurrentes pouvant compromettre l''éclairage ou endommager le nouveau moteur. - Remplacer le moteur sans régler la portée
    après la pose : la pose d''un nouveau correcteur remet la glace du phare à une position mécanique qui ne correspond pas
    forcément à l''orientation correcte. Ne pas effectuer le réglage de portée après remplacement revient à rouler avec des
    phares mal orientés, et expose à un refus au contrôle technique. - Commander le correcteur sans identifier le côté défaillant
    : les correcteurs sont parfois asymétriques (gauche / droit). Commander le mauvais côté oblige à retourner la commande
    et à payer deux fois les frais de port. - Forcer le moteur lors de la dépose en rotation : le système de baïonnette requiert
    un quart de tour précis. Forcer en rotation avec un outil inadapté brise l''ergot de verrouillage du logement dans le
    boîtier du phare, rendant le remplacement plus difficile et pouvant nécessiter le remplacement du bloc optique entier.
    - Ignorer le voyant de défaut après remplacement : sur les véhicules avec correcteur automatique piloté, un code défaut
    peut persister après le remplacement si le capteur de hauteur de caisse n''a pas été étalonné. Ne pas effacer ce code
    et ne pas réaliser la procédure d''initialisation laisse le système en mode dégradé. - Utiliser un correcteur non compatible
    avec le type de phare : installer un correcteur prévu pour phare halogène sur un bloc optique Xénon ne déclenchera pas
    la commande électronique et peut endommager le calculateur d''éclairage sur les systèmes à bus LIN.'
  S6: 'Après la pose d''un nouveau correcteur de portée, le réglage de la portée des phares et quelques contrôles fonctionnels
    sont indispensables pour valider l''intervention et assurer la conformité du véhicule. - Réglage de la portée sur mur
    ou fosse homologuée : placer le véhicule à 5 mètres d''un mur vertical blanc dans un endroit sombre, charge à vide, pression
    de pneumatiques nominale. Le centre du faisceau coupé doit être à la hauteur prescrite (généralement 1 à 2 cm en dessous
    du centre du phare). Un réglage sur banc optique homologué est la méthode de référence. - Test de toutes les positions
    de réglage : actionner la commande de réglage (molette ou bouton) sur toutes les positions disponibles et vérifier que
    le faisceau se déplace de façon régulière et proportionnelle sans à-coups. - Vérification de l''absence de bruit pendant
    le fonctionnement : lors des réglages, le moteur doit fonctionner silencieusement ou avec un léger bourdonnement. Tout
    grincement, craquement ou bruit sec indique un problème de montage ou un mauvais engagement dans le logement. - Lecture
    et effacement des codes défaut : sur les véhicules avec correcteur automatique, connecter un outil de diagnostic et vérifier
    l''absence de codes actifs liés au circuit d''éclairage après remontage et réglage. - Contrôle du fonctionnement en charge
    : charger le véhicule avec du poids à l''arrière (passagers ou charge équivalente) et vérifier que le correcteur automatique
    abaisse effectivement le faisceau en conséquence, ou que la position manuelle sélectionnée correspond au faisceau observé
    sur le mur.'
  S7: 'Un correcteur de portée défaillant s''inscrit dans un système d''éclairage où plusieurs composants travaillent ensemble.
    Vérifier ces pièces associées lors de l''intervention : - Bloc optique avant (phare) — le moteur de correcteur est intégré
    au bloc optique. Si le phare est fissuré, brûlé intérieurement ou très encrassé, envisager le remplacement du bloc optique
    complet plutôt que du seul correcteur. - Commande de correcteur de portée — molette ou commutateur en habitacle qui envoie
    le signal au moteur. Un correcteur neuf qui ne répond pas peut indiquer une commande défaillante plutôt qu''un problème
    de moteur. Tester la commande avant la pose. - Câblage et connecteur du correcteur — le connecteur du moteur correcteur
    est exposé dans le compartiment moteur et peut s''oxyder ou se fissurer. Inspecter le connecteur et le câblage lors du
    remplacement du moteur. - Vis de réglage du phare — permettent l''ajustement de l''orientation verticale et horizontale
    du faisceau. Si la vis de réglage est grippée ou cassée, elle doit être remplacée pour permettre le réglage après la pose
    du correcteur neuf.'
  S8: Peut-on passer le contrôle technique avec un correcteur de portée défaillant ? Non. L'orientation des phares est un
    point de contrôle obligatoire au contrôle technique. Des phares mal orientés (trop hauts, trop bas, ou orientation non
    ajustable) constituent un motif de refus entraînant une contre-visite dans les 2 mois. Le remplacement du correcteur défaillant
    suivi d'un réglage de portée conforme est obligatoire pour obtenir le quitus. Comment savoir si c'est le moteur du correcteur
    ou le câblage qui est en cause ? Mesurer la tension d'alimentation aux bornes du connecteur du correcteur (moteur déconnecté)
    avec un multimètre lors de l'activation de la commande. Si la tension est présente mais que le moteur ne tourne pas, le
    moteur est défaillant. Si aucune tension n'est mesurée, le problème vient du câblage ou de la commande habitacle. Un test
    de continuité sur le faisceau entre la commande et le connecteur du correcteur permet d'isoler le problème. Faut-il remplacer
    les deux correcteurs en même temps ? Ce n'est pas obligatoire si le deuxième fonctionne correctement. Cependant, si les
    deux correcteurs sont du même âge et que l'un tombe en panne, il est souvent préférable de remplacer les deux simultanément
    pour éviter une deuxième intervention prochaine. Le coût de la main-d'oeuvre représente la majeure partie du coût de l'intervention
    une fois le phare déposé. Un correcteur de portée manuel peut-il être remplacé par un correcteur automatique ? Non, sans
    modification supplémentaire du véhicule. Le correcteur automatique nécessite des capteurs de hauteur de caisse, un calculateur
    dédié et un câblage spécifique. Installer uniquement le moteur de correcteur automatique sans le reste du système ne permet
    pas son fonctionnement. En revanche, remplacer un correcteur automatique défaillant par un autre correcteur automatique
    identique est la procédure standard.
  META: '{"meta_title":"Correcteur de portée : diagnostic et remplacement","meta_description":"Phares mal orientés, éblouissement
    ou réglage impossible ? Découvrez comment diagnostiquer un correcteur de portée défaillant et le remplacer selon votre
    véhicule."}'
---

# Correcteur de portée - Guide Diagnostic Complet

## Fonction et Rôle

Règle la hauteur du faisceau lumineux en fonction de la charge du véhicule

**Actions principales:** regler, ajuster, adapter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- phares mal orientés
- eblouissement
- reglage impossible

## Procédure de Diagnostic

Pour diagnostiquer un problème de correcteur de portée:

1. **Inspection visuelle** - Examiner l'état du correcteur de portée
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- feu-avant
- commande-correcteur-de-portee

## Critères de Compatibilité

Pour commander le bon correcteur de portée, vous devez connaître:

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

**Comment choisir Correcteur de portée compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Correcteur de portée ?**
En cas de phares mal orientés ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Correcteur de portée sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
