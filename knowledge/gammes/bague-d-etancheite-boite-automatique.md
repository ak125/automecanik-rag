---
category: moteur
slug: bague-d-etancheite-boite-automatique
title: Bague d'étanchéité boîte automatique
pg_id: 626
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
  last_enriched_by: script:materialize-db-to-md
  last_enriched_at: '2026-04-03'
  v5_migrated_at: '2026-03-29'
domain:
  role: Assurer l'etancheite des arbres de la boite automatique
  must_be_true:
  - assurer l'etancheite
  - isoler
  must_not_contain:
  - freinage
  - climatisation
  - direction
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - cardan
  - soufflet-de-cardan
  - roulement-de-roue
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de moteur pour
    confirmer Bague d'étanchéité boîte automatique.
  - Verifier la reference OE ou equivalence constructeur pour le vehicule exact
  - Comparer les dimensions et le type de montage avec la piece d origine
  - Choisir un equipementier reconnu pour garantir qualite et compatibilite
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "repare le moteur"
  cost_range:
    min: 1000
    max: 5000
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    description: Joint spi fourni par l'équipementier d'origine de la boîte automatique. Dimensions et matière conformes aux
      spécifications constructeur.
  - tier: Équivalent OE — équipementiers spécialisés étanchéité
    description: Fabricants reconnus en joints d'étanchéité automobile. Matériaux (FPM/NBR) adaptés aux huiles ATF haute température.
  - tier: Adaptables — kits d'étanchéité
    description: Kits multi-références couvrant plusieurs boîtes automatiques. Vérifier impérativement les cotes (diamètre
      intérieur, extérieur, hauteur) avant montage.
  brands:
    premium:
    - SKF
    - GKN/Spidan
    standard:
    - Febi
    - Meyle
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Fuites d huile sous la boite
    severity: confort
  - id: S2
    label: Niveau d huile qui baisse
    severity: confort
  - id: S3
    label: Taches au sol au niveau de la transmission
    severity: confort
  causes:
  - identifier origine fuite et verifier joints
  - 'Usure ou defaillance causant : fuites d huile sous la boite'
  - 'Usure ou defaillance causant : niveau d huile qui baisse'
  quick_checks:
  - Fuites d huile sous la boite ?
  - 'Observer : niveau d huile qui baisse ?'
  - 'Observer : taches au sol au niveau de la transmission ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Fuites d huile sous la boite
  - Niveau d huile qui baisse
  - Taches au sol au niveau de la transmission
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '626'
  intro_title: A quoi sert Bague d'étanchéité boîte automatique ?
  risk_title: Pourquoi remplacer Bague d'étanchéité boîte automatique a temps ?
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
  - question: Comment choisir Bague d'étanchéité boîte automatique compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Bague d'étanchéité boîte automatique ?
    answer: En cas de fuites d huile sous la boite ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Bague d'étanchéité boîte automatique sans verification atelier ?
    answer: Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure
      constructeur.
  quality:
    score: 60
    source: script:rag-upgrade-v4
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
doc_id: 705ecff9-f37d-53c4-9a9e-064da5b3c5ad
content_hash: sha256:09add9e18b90ec7d
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
  area: Sous le vehicule, relie la boite aux roues
  access: Par le dessous (pont elevateur)
  adjacent_parts:
  - cardan
  - soufflet
  - roulement de roue
  - boite
installation:
  difficulty: difficile
  time: 1h a 3h
  tools:
  - pont elevateur
  - cle a douille
  - arrache-cardan
  prerequisite: Vidange huile de boite si cardan depose
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: céramique
    source_ref: corpus RAG web OEM
  - type: hydraulique
    source_ref: corpus RAG web OEM
  - type: pneumatique
    source_ref: corpus RAG web OEM
  technical_notes:
    norme_iso_5598: ISO 5598
    val_1_5_mm: 1,5 mm
  materials:
  - materiau: céramique
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'La bague d''étanchéité boîte automatique est un joint à lèvre circulaire en élastomère chargé d''assurer l''étanchéité
    dynamique des arbres tournants de la transmission automatique. Elle est positionnée autour des arbres de sortie de la
    boîte (arbres de transmission), ainsi qu''autour de l''arbre d''entrée du convertisseur de couple côté moteur. Son rôle
    est d''isoler l''huile ATF (Automatic Transmission Fluid) contenue dans la boîte automatique de l''extérieur, tout en
    permettant la rotation continue des arbres. La lèvre de la bague s''appuie sur la surface de l''arbre avec une légère
    précontrainte, créant une zone d''étanchéité dynamique qui empêche les fuites sans générer de friction excessive. Techniquement,
    une bague d''étanchéité boîte automatique se compose d''un corps métallique (emmanchement dans le carter) et d''une lèvre
    en caoutchouc fluoré (FKM/Viton) ou en acrylate, maintenue plaquée sur l''arbre par un ressort hélicoïdal intégré. La
    qualité du matériau est déterminante : l''huile ATF est agressive chimiquement et la bague doit résister à des températures
    allant de -40 °C à +150 °C en fonctionnement. Chaque boîte automatique comporte généralement plusieurs bagues d''étanchéité
    : une sur chaque arbre de transmission (2 ou 4 selon le type de transmission — avant, arrière, intégrale), une sur le
    convertisseur de couple, et parfois une sur l''arbre du sélecteur. La défaillance de l''une d''elles entraîne une fuite
    d''huile ATF, qui doit être traitée rapidement pour éviter un endommagement de la boîte automatique par manque de lubrification.'
  S2: 'La défaillance d''une bague d''étanchéité boîte automatique se manifeste essentiellement par des fuites d''huile ATF.
    Ces fuites doivent être traitées rapidement : l''huile ATF est à la fois le fluide de lubrification et le fluide hydraulique
    de commande de la boîte automatique. Un niveau insuffisant entraîne des passages de vitesses perturbés, puis des dommages
    irréversibles sur la boîte. - Fuites d''huile visibles sous la boîte : taches rougeâtres ou brunâtres au sol, sous le
    véhicule, dans la zone de la boîte de vitesses. L''huile ATF est généralement de couleur rouge ou rose en neuf, devenant
    brune avec l''usure. Une tache rouge sous le véhicule est un signe quasi certain de fuite ATF. - Niveau d''huile ATF qui
    baisse : lors des contrôles périodiques du niveau de la boîte automatique (sur les véhicules équipés d''une jauge de niveau),
    un niveau inférieur à la marque minimum sans remplacement récent indique une fuite active. - Taches au sol au niveau de
    la transmission : les taches apparaissent typiquement à l''emplacement de stationnement habituel du véhicule. La localisation
    des taches (avant ou arrière du véhicule, côté gauche ou droit) aide à identifier quelle bague d''étanchéité est en cause.
    - Odeur de brûlé lors de la conduite : si l''huile ATF fuit sur des composants chauds du système d''échappement, une odeur
    caractéristique de brûlé peut se dégager dans l''habitacle ou sous le capot. Ce symptôme impose un arrêt immédiat. - Passages
    de vitesses heurtés ou retardés : un niveau d''huile ATF insuffisant perturbe la commande hydraulique de la boîte automatique.
    Les changements de rapports deviennent brusques, tardifs ou accompagnés de vibrations — symptôme qui indique que la fuite
    est avancée. - Traces d''huile visibles sur le carter de boîte ou les arbres : une inspection visuelle sous le véhicule
    (sur pont ou avec une lampe) peut révéler des traces d''huile sur les arbres de transmission à leur point de sortie du
    carter, directement autour de la bague d''étanchéité.'
  S3: 'Le choix d''une bague d''étanchéité boîte automatique doit reposer sur des critères dimensionnels et matériaux précis.
    Une bague de mauvaises dimensions ou d''un matériau inadapté fuira rapidement ou endommager le carter. - Identifier la
    bague par référence constructeur : renseignez la marque, le modèle, l''année et le type de motorisation. La référence
    constructeur garantit des dimensions exactes (diamètre intérieur, diamètre extérieur, hauteur) et un matériau compatible
    avec l''huile ATF de votre boîte. - Vérifier les trois dimensions de la bague : diamètre intérieur (doit correspondre
    exactement au diamètre de l''arbre), diamètre extérieur (doit correspondre au logement dans le carter), et hauteur. Une
    bague trop grande en diamètre intérieur fuira immédiatement. Une bague trop petite ne rentrera pas dans le logement. -
    Choisir un matériau compatible avec l''huile ATF : privilégiez les bagues en FKM (fluoroélastomère, aussi appelé Viton)
    pour une résistance maximale à la chaleur et aux huiles ATF modernes. Les bagues en acrylate (ACM) conviennent également
    mais avec des limites thermiques inférieures. - Identifier quelle bague est défaillante : localiser la source exacte de
    la fuite (arbre de transmission gauche, droit, convertisseur de couple) avant de commander. Les dimensions varient selon
    la position sur la boîte. - Préférer les bagues d''origine ou équivalent OEM : les bagues génériques bon marché présentent
    souvent des tolérances dimensionnelles moins précises et des matériaux de moindre qualité. Sur une boîte automatique dont
    le remplacement coûte plusieurs milliers d''euros, économiser sur la bague d''étanchéité est une erreur de calcul. - Vérifier
    l''état de l''arbre au remplacement : un arbre rayé ou corrodé à l''emplacement de la bague ne permettra pas à une nouvelle
    bague de tenir. Si l''arbre est endommagé, une bague surdimensionnée ou une réparation de surface de l''arbre peut être
    nécessaire. Pour aller plus loin : consultez notre guide d''achat bague d''étanchéité boîte automatique — comparatif marques,
    critères de choix et prix.'
  S4_DEPOSE: 'Le remplacement d''une bague d''étanchéité boîte automatique est une opération qui nécessite de déposer les
    arbres de transmission, ce qui classe cette intervention dans la catégorie des travaux d''atelier. Un outillage adapté
    est indispensable : extracteur de bague, emmancheur de bague, support de boîte. - Identifier la source de fuite avec précision
    : nettoyez le carter de boîte avec un dégraissant, laissez le véhicule tourner 10 minutes, puis repérez l''origine exacte
    de la fuite pour ne déposer que l''arbre concerné. - Vidanger l''huile ATF : avant toute intervention sur la boîte automatique,
    vidangez l''huile ATF pour éviter de la répandre lors de la dépose de l''arbre de transmission. Récupérez l''huile dans
    un bac de récupération. - Déposer l''arbre de transmission concerné : débloquez l''écrou de moyeu (si accessible), débranchez
    l''arbre de transmission côté boîte. Sur certains modèles, il faut déposer le porte-fusée complet pour accéder à l''arbre
    de boîte. - Extraire l''ancienne bague : utilisez un extracteur de bague adapté ou un tournevis plat inséré délicatement
    dans le logement pour faire levier — en veillant à ne pas rayer le logement dans le carter. La bague se retire par traction.
    - Inspecter l''arbre et le logement : vérifiez que la surface de l''arbre (zone de contact avec la lèvre de la bague)
    est lisse et sans rayures. Examinez le logement dans le carter pour détecter toute déformation. - Lubrifier et emmanchement
    de la nouvelle bague : enduisez légèrement la lèvre de la nouvelle bague d''huile ATF propre. Positionnez la bague en
    face de son logement, lèvre orientée vers l''intérieur de la boîte, et emmancez-la à l''aide d''un emmancheur de bague
    ou d''une douille de même diamètre. La bague doit être emboîtée jusqu''à affleurement avec le carter — ne pas la faire
    rentrer de travers. - Reposer l''arbre de transmission et refaire le niveau ATF : réinsérez l''arbre de transmission,
    vérifiez le couple de serrage de l''écrou de moyeu selon les préconisations constructeur, refaites le niveau d''huile
    ATF avec le fluide spécifié. - Tester l''étanchéité : démarrez le véhicule, laissez-le fonctionner 10 à 15 minutes avec
    plusieurs passages en marche avant, marche arrière et vitesses différentes, puis inspectez visuellement la bague remplacée
    pour confirmer l''absence de fuite.'
  S4_REPOSE: 'La repose d''une bague d''étanchéité boîte automatique est l''étape la plus délicate de l''intervention : un
    emmanchement incorrect — trop incliné, trop enfoncé ou insuffisamment enfoncé — conduit à une reprise de fuite immédiate
    ou différée. L''outil d''emmanchement adapté (emmancheur tubulaire de diamètre correspondant à la bague) est indispensable
    pour garantir une repose propre. - Préparer les surfaces de contact : nettoyez le logement de la bague dans le carter
    avec un chiffon propre. Retirez toute trace d''huile ou de solvant — une surface grasse empêche la bague de s''emmancer
    correctement et peut la faire tourner dans son logement. La surface doit être propre et sèche. - Lubrifier légèrement
    le lèvre de la nouvelle bague : passez un film très fin d''huile de boîte automatique (ATF) sur la lèvre intérieure de
    la bague. Cette lubrification initiale empêche la lèvre de se déchirer lors du premier contact avec l''arbre en rotation.
    Ne lubrifiez pas le diamètre extérieur — il doit rester sec pour une adhérence maximale dans le logement. - Positionner
    la bague en face du logement : placez la bague perpendiculairement à l''axe du logement, lèvre orientée vers l''intérieur
    de la boîte. Toute inclinaison lors de l''emmanchement génère une déformation qui causera une fuite ultérieure. - Emmancer
    la bague avec l''outil adapté : utilisez un emmancheur tubulaire dont le diamètre extérieur correspond exactement au diamètre
    extérieur de la bague. Frappez l''emmancheur à coups de marteau légers et réguliers jusqu''à ce que la bague soit affleurante
    avec le bord du logement ou positionnée à la profondeur spécifiée par le constructeur. Vérifiez à l''aide d''une jauge
    de profondeur si une cote précise est requise. - Contrôler la mise à niveau : une fois emmancée, la bague doit être parfaitement
    perpendiculaire à l''axe de rotation. Passez le doigt sur son pourtour pour détecter toute asymétrie. Un côté plus enfoncé
    que l''autre indique un emmanchement défectueux. - Lubrifier légèrement l''arbre avant la repose : appliquez un film d''ATF
    propre sur la portion de l''arbre de transmission qui sera en contact avec la lèvre de la bague. Cela facilite le glissement
    initial et protège la lèvre lors de la réintroduction de l''arbre. - Réintroduire l''arbre de transmission : réinsérez
    l''arbre dans le boîtier en guidant son extrémité dans la bague neuve. Procédez lentement et en ligne droite pour éviter
    que le bord de l''arbre n''accroche et ne retourne la lèvre de la bague. Si l''arbre présente un chanfrein d''entrée,
    l''opération est facilitée. - Remonter les fixations de la transmission : remontez l''écrou de moyeu, les boulons de cardan
    ou les écrous de fixation selon la configuration du véhicule. Respectez impérativement les couples de serrage constructeur
    (l''écrou de moyeu atteint souvent 200 à 280 Nm selon les modèles — il doit être serré avec le véhicule au sol ou la roue
    bloquée en rotation). - Refaire le niveau d''huile ATF : une partie de l''huile de boîte s''est écoulée lors de la dépose.
    Refaites le niveau selon la procédure constructeur (souvent par l''orifice de remplissage sur le carter latéral, niveau
    à chaud moteur tournant) et utilisez uniquement le grade ATF spécifié pour la boîte concernée. - Test d''étanchéité :
    démarrez le véhicule, laissez la boîte monter en température, effectuez quelques passages de vitesses, puis inspectez
    visuellement la zone de la bague après 10 minutes de fonctionnement. Aucune trace d''huile fraîche ne doit être visible.'
  S5: 'Le remplacement d''une bague d''étanchéité boîte automatique expose à plusieurs erreurs techniques qui peuvent aggraver
    la situation et entraîner une fuite persistante ou un endommagement de la boîte. - Utiliser un additif anti-fuite à la
    place de la bague : les produits chimiques "anti-fuite" pour boîte automatique gonflent temporairement les bagues en élastomère
    pour réduire les fuites. Ce traitement palliatif peut masquer le problème quelques semaines mais ne répare pas la bague
    — et peut aggraver son état si elle est déjà trop dégradée. La bague défaillante doit être physiquement remplacée. - Emmanchement
    de travers de la nouvelle bague : si la bague n''est pas emmanchée parfaitement perpendiculairement à l''axe de l''arbre,
    elle fuira immédiatement. Utiliser un emmancheur de bague de bonne taille garantit un emmanchement droit et homogène.
    - Rayer l''arbre lors de l''extraction de l''ancienne bague : utiliser un tournevis sans précaution pour extraire l''ancienne
    bague peut rayer la surface de contact de l''arbre. Un arbre rayé dans la zone de contact avec la lèvre provoque une fuite
    continue même avec une bague neuve. - Ne pas vider l''huile ATF avant intervention : ouvrir le logement de la boîte sans
    avoir vidangé l''huile ATF entraîne un déversement de fluide lors de la dépose de l''arbre. L''huile ATF est difficile
    à nettoyer et peut endommager certains composants si elle se répand sur des pièces non prévues. - Commander une bague
    générique sans vérifier les dimensions exactes : les bagues d''étanchéité de dimensions légèrement incorrectes (quelques
    dixièmes de millimètre) fuient dès la remise en service. La référence constructeur ou les dimensions précises (diamètre
    intérieur x diamètre extérieur x hauteur) sont indispensables.'
  S6: 'Après le remplacement d''une bague d''étanchéité boîte automatique, un protocole de vérification rigoureux est nécessaire
    pour confirmer l''étanchéité et le bon fonctionnement de la transmission avant de remettre le véhicule en circulation.
    - Contrôle du niveau d''huile ATF après remplissage : vérifiez le niveau d''huile ATF conformément à la procédure constructeur
    (moteur chaud ou froid selon les modèles, parfois via un bouchon de niveau plutôt qu''une jauge). Un niveau incorrect
    perturbe les passages de vitesses et peut endommager la boîte. - Test de fonctionnement à chaud : laissez le véhicule
    tourner 10 à 15 minutes avec des passages manuels dans tous les rapports (P, R, N, D et les rapports manuels si disponibles).
    Les passages de vitesses doivent être doux et sans à-coups — signe que la pression hydraulique est correcte. - Inspection
    visuelle de la bague remplacée après test : après le test à chaud, éteignez le véhicule et inspectez visuellement la zone
    de la bague remplacée avec une lampe. Aucune trace d''huile fraîche ne doit être présente sur le carter ou l''arbre à
    l''emplacement de la bague. - Vérification des arbres de transmission reposés : confirmez que les arbres de transmission
    sont correctement positionnés dans leurs supports et que les soufflets de protection ne présentent pas de déchirure suite
    à l''intervention. - Vérification de l''absence de code défaut : sur les boîtes automatiques gérées par un calculateur,
    connectez un outil de diagnostic et vérifiez l''absence de code défaut en mémoire relatif à la transmission (pression
    hydraulique, capteurs de vitesse d''arbre, etc.).'
  S7: 'La bague d''étanchéité de boîte automatique fait partie d''un système de transmission complet. Son remplacement mobilise
    une partie significative de la transmission, ce qui justifie un contrôle systématique des composants voisins pour éviter
    un retour en atelier à court terme. - Joint SPI d''arbre de transmission (côté opposé) : si la bague d''un côté est usée,
    la bague du côté opposé présente généralement le même niveau d''usure, car elle a subi les mêmes contraintes depuis la
    même date. Remplacer les deux joints lors du même démontage est économique en temps de main-d''oeuvre. - Huile ATF de
    boîte automatique : lors de la dépose des arbres, une partie du fluide ATF s''écoule. Cette intervention est l''occasion
    idéale pour effectuer une vidange du fluide ATF, surtout si le kilométrage est élevé ou si le fluide présente une coloration
    sombre ou une odeur de brûlé. Un ATF dégradé accélère l''usure des joints et des embrayages. - Filtre à huile ATF : sur
    les boîtes automatiques équipées d''un filtre interne ou externe, le changement du filtre accompagne idéalement la vidange
    d''ATF. Un filtre colmaté génère une pression insuffisante et perturbe les changements de vitesse. - Cardan complet ou
    arbre de transmission : lors de la dépose de l''arbre pour accéder à la bague, inspectez l''état du cardan intérieur (soufflet,
    graisse, jeu) et de l''arbre lui-même (traces de rouille, déformation). Un arbre de transmission présentant du jeu ou
    un soufflet percé doit être remplacé simultanément. - Roulement de moyeu : l''écrou de moyeu doit souvent être déserré
    pour déposer l''arbre. Cette ouverture est l''occasion de vérifier l''état du roulement de moyeu — jeu axial, bruit de
    roulement, chauffage. Un roulement en fin de vie sera plus accessible à remplacer maintenant qu''après remontage complet.
    - Joint de carter de boîte : si une fuite secondaire est détectée sur le carter lui-même (au niveau du plan de joint avec
    le carter d''embrayage ou le carter convertisseur), le joint de carter devra être remplacé en même temps pour éviter deux
    interventions séparées.'
  S8: 'Comment localiser quelle bague d''étanchéité fuit sur ma boîte automatique ? Commencez par nettoyer soigneusement le
    carter de boîte automatique avec un dégraissant pour éliminer les traces d''huile existantes. Laissez ensuite le véhicule
    tourner 10 à 15 minutes avec plusieurs passages en marche avant et arrière, puis inspectez sous le véhicule avec une lampe.
    Les traces d''huile fraîche apparaissent à l''emplacement de la bague défaillante : sur les arbres de transmission latéraux,
    sur l''arbre d''entrée côté convertisseur, ou à l''emplacement du sélecteur. La couleur rougeâtre de l''huile ATF facilite
    l''identification. Peut-on continuer à rouler avec une bague d''étanchéité boîte automatique qui fuit ? Non, pas à long
    terme. La fuite d''huile ATF entraîne une baisse progressive du niveau de fluide dans la boîte automatique. L''huile ATF
    assure simultanément la lubrification des engrenages et la commande hydraulique des passages de vitesses. Un niveau insuffisant
    provoque d''abord des passages de vitesses heurtés et des à-coups, puis des endommagements irréversibles des composants
    internes de la boîte. Le coût d''une bague d''étanchéité est sans commune mesure avec celui d''une boîte automatique de
    remplacement. Dès l''apparition d''une fuite, l''intervention doit être planifiée dans les plus brefs délais. Quelle huile
    ATF utiliser pour refaire le niveau après remplacement de la bague ? L''huile ATF est strictement spécifique au constructeur
    et parfois au modèle de boîte automatique. Utiliser un fluide ATF incorrect peut endommager les joints internes de la
    boîte, perturber les passages de vitesses et réduire la durée de vie de la transmission. Consultez le carnet d''entretien
    du véhicule ou la documentation constructeur pour identifier la spécification ATF exacte (ex : ATF Dexron VI, ATF MB 236.15,
    ATF Matic-S, etc.) et n''utilisez jamais un fluide universel sans vérification préalable. La bague d''étanchéité boîte
    automatique peut-elle être remplacée à domicile ? Techniquement, oui — à condition de disposer d''un pont élévateur ou
    d''un fossé de visite, d''un extracteur de bague, d''un emmancheur adapté et de savoir déposer les arbres de transmission.
    Dans la pratique, cette intervention est hors de portée d''un amateur non équipé. L''emmanchement incorrect de la bague
    est la cause principale de fuite persistante après remplacement. Pour une boîte automatique représentant souvent 3 000
    à 8 000 euros de remplacement, cette opération est préférable à confier à un professionnel équipé.'
---

# Bague d'étanchéité boîte automatique - Guide Diagnostic Complet

## Fonction et Rôle

Assurer l'etancheite des arbres de la boite automatique

**Actions principales:** assurer l'etancheite, isoler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- fuites d huile sous la boite
- niveau d huile qui baisse
- taches au sol au niveau de la transmission

## Procédure de Diagnostic

Pour diagnostiquer un problème de bague d'étanchéité boîte automatique:

1. **Inspection visuelle** - Examiner l'état du bague d'étanchéité boîte automatique
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- joint-spi
- boite-automatique

## Critères de Compatibilité

Pour commander le bon bague d'étanchéité boîte automatique, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"

## FAQ

**Comment choisir Bague d'étanchéité boîte automatique compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Bague d'étanchéité boîte automatique ?**
En cas de fuites d huile sous la boite ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Bague d'étanchéité boîte automatique sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
