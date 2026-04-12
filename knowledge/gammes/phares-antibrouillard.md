---
category: eclairage
slug: phares-antibrouillard
title: Phares antibrouillard
pg_id: 289
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-04-04'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:materialize-db-to-md
  last_enriched_at: '2026-04-04'
  v5_migrated_at: '2026-03-29'
domain:
  role: Dirige la lumière pour améliorer la visibilité par temps de brouillard ou mauvaise visibilité
  must_be_true:
  - diriger
  - diffuser
  - eclairer
  must_not_contain:
  - ampoule seule
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - ampoule-feu-avant
  - ampoule-feu-arriere
  - feu-avant
  - feu-arriere
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
  - ❌ "visibilite parfaite"
  cost_range:
    min: 30
    max: 200
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    price_range: Prix élevé — qualité optique et étanchéité conformes à l'origine
  - tier: Équivalent OE (OES)
    price_range: Prix intermédiaire — recommandé dans la majorité des cas
  - tier: Aftermarket standard
    price_range: Prix bas — homologation ECE obligatoire sur route ouverte
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
    label: Antibrouillard inactif
    severity: confort
  - id: S2
    label: Eclairage faible ou jauni
    severity: confort
  - id: S3
    label: Optique fissuree ou embuee
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : antibrouillard inactif'
  quick_checks:
  - 'Observer : antibrouillard inactif ?'
  - 'Observer : eclairage faible ou jauni ?'
  - 'Observer : optique fissuree ou embuee ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Antibrouillard inactif
  - Eclairage faible ou jauni
  - Optique fissuree ou embuee
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '289'
  intro_title: A quoi sert Phares antibrouillard ?
  risk_title: Pourquoi remplacer Phares antibrouillard a temps ?
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
  - question: Comment choisir Phares antibrouillard compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Phares antibrouillard ?
    answer: En cas de antibrouillard inactif ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Phares antibrouillard sans verification atelier ?
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
doc_id: e24db93b-1629-5fd4-925e-1b0f77ea7d7f
content_hash: sha256:258c91d8edd55032
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
  _enriched_at: '2026-04-04'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: hall
    source_ref: corpus RAG web OEM
  - type: monotube
    source_ref: corpus RAG web OEM
  - type: perforé
    source_ref: corpus RAG web OEM
  - type: plein
    source_ref: corpus RAG web OEM
  - type: ventilé
    source_ref: corpus RAG web OEM
  - type: électrique
    source_ref: corpus RAG web OEM
  technical_notes:
    val_000_kg: 000 kg
    val_1_5_litre: 1,5 litre
    val_1_8_litre: 1.8 litre
    val_10_a: 10 A
    val_100_kg: 100 kg
    val_100_km: 100 km
    val_15_mm: 15 mm
    val_150_a: 150 a
    val_17_a: 17 a
    val_173_kg: 173 kg
    val_196_km: 196 km
    val_2_litres: 2 litres
    val_2_0_litre: 2,0 litre
    val_2_0_litres: 2,0 litres
  materials:
  - materiau: Aluminium
    source_ref: corpus RAG web OEM
  - materiau: acier inoxydable
    source_ref: corpus RAG web OEM
  - materiau: aluminium
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le phare antibrouillard est un projecteur spécialisé conçu pour diriger la lumière horizontalement, ras du sol, afin
    de diffuser un faisceau large et court qui éclaire la chaussée sans réfléchir sur le voile de brouillard ou de précipitations.
    Contrairement aux phares de croisement qui projettent un cône lumineux vers l''avant, le phare antibrouillard éclaire
    la zone immédiatement devant le véhicule avec un angle rasant, en dessous du niveau du brouillard.La technologie utilisée
    repose sur une optique à coupure nette qui délimite précisément la zone éclairée. Cette coupure empêche la lumière de
    monter dans le brouillard et de créer l''effet d''éblouissement par rétrodiffusion. Les phares antibrouillard sont montés
    en position basse sur le bouclier avant, typiquement à moins de 40 cm du sol, pour rester sous la couche de brouillard.Selon
    la technologie embarquée, on distingue plusieurs types : les phares à ampoule halogène H1, H3 ou H7 (technologie classique),
    les phares à ampoule HID (décharge haute intensité) et les phares à LED (diodes électroluminescentes) qui offrent une
    durée de vie supérieure et une consommation réduite. Les pièces associées comme l''ampoule-feu-avant et le relais-phare
    participent au circuit d''alimentation de l''ensemble du système d''éclairage avant.'
  S2: 'Un phare antibrouillard défaillant se manifeste par plusieurs signes reconnaissables. Intervenir dès les premiers symptômes
    évite de rouler sans protection optique par mauvaise visibilité et prévient les complications électriques secondaires.-
    Antibrouillard inactif : Le phare ne s''allume pas malgré l''activation de la commande. Cela peut indiquer une ampoule
    grillée, un relais défectueux, un fusible sauté ou une rupture dans le câblage d''alimentation.- Éclairage faible ou jauni
    : Le faisceau lumineux est nettement moins intense qu''à l''état neuf ou présente une teinte jaune- orangée prononcée.
    Ce phénomène révèle une ampoule en fin de vie, un dépôt de condensation interne sur l''optique ou un verre opacifié par
    l''oxydation UV.- Optique fissurée ou embuée : Le verre de protection présente des craquelures, des impacts ou une condensation
    persistante à l''intérieur du boîtier. Une optique fissurée laisse entrer l''eau, ce qui détériore l''ampoule et les connecteurs
    électriques rapidement.- Faisceau désaxé ou diffus : Le phare éclaire dans une direction incorrecte ou produit un halo
    diffus sans coupure nette. Cela indique un support de fixation cassé ou une optique déréglée suite à un choc.- Intermittences
    à l''allumage : Le phare clignote ou s''éteint aléatoirement pendant le roulage, signe d''un contact électrique défaillant
    ou d''une ampoule dont le filament est en cours de rupture.- Boîtier fissuré ou déformé : Le boîtier plastique présente
    des fissures suite à un impact de caillou ou de grêle, compromettant l''étanchéité de l''ensemble.'
  S3: 'Choisir le bon phare antibrouillard nécessite de croiser plusieurs critères techniques pour garantir la compatibilité
    mécanique, électrique et réglementaire avec votre véhicule.- Marque et modèle du véhicule : La référence constructeur
    est le point de départ obligatoire. Un phare antibrouillard est spécifique à un modèle, un millésime et parfois une version
    de finition. Utiliser le sélecteur de véhicule avec la marque, le modèle et l''année de mise en circulation.- Côté de
    montage : Les phares antibrouillard gauche et droit ne sont généralement pas interchangeables. Vérifier impérativement
    le côté (D ou G, ou Droit/Gauche) avant la commande.- Type de technologie lumineuse : Identifier la technologie d''origine
    (halogène, HID, LED) et choisir une pièce utilisant la même technologie ou une technologie compatible. Un remplacement
    halogène par LED peut nécessiter un adaptateur ou un kit de conversion.- Référence OEM ou équivalent homologué : Privilégier
    une référence correspondant à la référence d''origine (OEM) ou une pièce d''équipementier certifiée ECE pour garantir
    l''homologation au contrôle technique.- Vérification de l''état du verre avant commande : Si seule l''ampoule est défaillante
    et que l''optique est intacte, remplacer uniquement l''ampoule plutôt que l''ensemble du bloc optique.- Compatibilité
    avec le système d''aide à la conduite : Sur les véhicules récents équipés de caméras ou capteurs frontaux, vérifier que
    le remplacement du phare n''interfère pas avec le calibrage des systèmes ADAS.- Conditionnement et contenu : Certains
    phares sont vendus avec ampoule incluse, d''autres non. Vérifier le contenu de la boîte pour éviter un achat complémentaire
    non anticipé.Pour aller plus loin : consultez notre guide d''achat phares antibrouillard — comparatif marques, critères
    de choix et prix.'
  S4_DEPOSE: 'Le remplacement d''un phare antibrouillard est une opération accessible à un mécanicien amateur équipé des bons
    outils. La procédure varie selon les modèles, mais les grandes étapes restent similaires.- Préparer le poste de travail
    : Garer le véhicule sur surface plane, couper le contact et débrancher la borne négative de la batterie pour supprimer
    toute alimentation électrique avant intervention.- Accéder au phare antibrouillard : Selon le véhicule, l''accès se fait
    par le dessous du pare-chocs (en dévissant une trappe ou un écrou de fixation), depuis l''intérieur du passage de roue
    (en retirant le carter de protection) ou directement par le dessus du bouclier.- Déposer le connecteur électrique : Pincer
    les loquets du connecteur enfichable et tirer perpendiculairement au phare pour débrancher l''alimentation. Ne jamais
    tirer sur les câbles.- Dévisser les fixations du boîtier : Localiser les vis ou clips de maintien (généralement 2 à 3
    points de fixation) et les retirer avec une clé appropriée (souvent Torx T20 ou T25, ou 10 mm). Conserver les fixations.-
    Extraire le phare défectueux : Dégager le phare en le faisant glisser ou en le pivotant selon le système d''encliquetage
    propre au véhicule.- Positionner le phare neuf : Insérer le nouveau phare dans son logement en alignant les ergots de
    positionnement, puis serrer les fixations sans forcer pour ne pas fissurer la monture plastique.- Rebrancher le connecteur
    électrique : Encliqueter le connecteur jusqu''au clic de verrouillage. Reconnecter la borne négative de la batterie.-
    Tester le fonctionnement : Allumer les phares antibrouillard et vérifier l''allumage, l''intensité et l''orientation du
    faisceau avant de reposer les carters.'
  S4_REPOSE: 'Après vérification que le nouveau phare antibrouillard correspond exactement à votre véhicule (côté, référence,
    type de fixation), procédez au remontage méthodique. Un mauvais montage peut compromettre l''étanchéité de l''optique
    et la qualité du faisceau lumineux. - Positionnement de l''optique dans son logement — Guidez le phare antibrouillard
    dans sa cavité en respectant les ergots de centrage. Ne forcez pas : un mauvais alignement crée des contraintes sur le
    boîtier plastique qui peut se fissurer. - Fixation des vis ou clips de maintien — Serrez les vis dans l''ordre diagonal
    (croix) pour répartir uniformément la pression sur le joint périphérique. Couple de serrage typique : 4 à 6 Nm selon le
    constructeur. Ne pas dépasser sous peine de casser les picots de fixation. - Reconnexion du connecteur électrique — Branchez
    le connecteur en orientant la languette de verrouillage correctement jusqu''au clic de fermeture. Tirez légèrement pour
    confirmer le verrouillage. Un connecteur mal engagé provoque une coupure intermittente. - Vérification de l''étanchéité
    — Contrôlez visuellement que le joint périphérique est bien en appui sur toute la périphérie du logement. Toute zone non
    jointée laissera entrer l''humidité et ternira l''optique en quelques semaines. - Remontage du bouclier ou de la jupe
    — Replacez les agrafes, clips ou vis de fixation du bouclier avant selon la procédure de dépose. Vérifiez l''alignement
    des lignes de caisse avec les autres éléments de carrosserie adjacents. - Test d''allumage — Mettez le contact et activez
    les antibrouillards avant depuis la commande habituelle. L''optique doit s''allumer immédiatement avec une lumière homogène.
    Un scintillement indique un défaut de connexion. - Contrôle de l''orientation du faisceau — Le faisceau antibrouillard
    doit éclairer la route à courte portée sans aveugler les conducteurs venant en face. Un réglage de portée est possible
    sur certains véhicules via les vis de réglage dédiées. Point de vigilance : si l''antibrouillard ne s''allume pas après
    montage correct, vérifiez le fusible correspondant dans le boîtier à fusibles (consulter le manuel du véhicule pour la
    localisation).'
  S5: 'Plusieurs erreurs fréquentes peuvent compromettre la réussite du remplacement d''un phare antibrouillard ou réduire
    la durée de vie de la pièce neuve.- Commander sans vérifier le côté : Confondre le phare gauche et le phare droit est
    l''erreur la plus répandue. Conséquence : retour et délai d''immobilisation supplémentaire. Toujours noter le côté défaillant
    avant la commande.- Toucher l''ampoule halogène à mains nues : La graisse de la peau dépose des traces sur l''ampoule
    qui créent des points chauds lors de l''allumage, provoquant une fissuration prématurée du verre. Manipuler l''ampoule
    avec un chiffon propre ou des gants.- Oublier de débrancher la batterie : Travailler sous tension électrique expose à
    un risque de court- circuit sur le circuit d''éclairage. Toujours débrancher la borne négative avant toute intervention
    sur un circuit électrique.- Serrer excessivement les vis de fixation : Le boîtier du phare et sa monture sont en plastique.
    Un couple de serrage excessif fissure les points d''ancrage et compromet l''étanchéité à long terme. Serrer fermement
    sans forcer.- Négliger le réglage du faisceau : Un phare mal orienté éblouit les conducteurs en face et diminue l''efficacité
    de l''éclairage. Après remplacement, vérifier l''orientation du faisceau sur un mur ou faire régler le phare en atelier.'
  S6: 'Une fois le phare antibrouillard remplacé, une série de contrôles permet de valider la qualité du montage avant de
    reprendre la route.- Test d''allumage immédiat : Allumer les phares antibrouillard avec le contact. Le phare neuf doit
    s''allumer instantanément, sans clignotement ni délai.- Vérification de l''intensité lumineuse : Comparer la luminosité
    du phare neuf avec le phare du côté opposé (si non remplacé). Les deux doivent présenter une intensité similaire.- Contrôle
    de l''étanchéité du boîtier : Vérifier visuellement l''absence de jeu ou d''espace entre le boîtier et le bouclier. En
    cas de doute, projeter de l''eau sur le phare et vérifier l''absence d''infiltration.- Orientation du faisceau : Projeter
    le faisceau sur un mur à 5 mètres et vérifier que la coupure lumineuse est bien horizontale, ras du sol, sans déviation
    latérale excessive.- Absence de témoin de défaut : S''assurer qu''aucun témoin de défaut d''éclairage ne s''allume au
    tableau de bord après remise en route du véhicule.- Contrôle du connecteur électrique : Tirer légèrement sur le faisceau
    au niveau du connecteur pour confirmer qu''il est correctement verrouillé et qu''il ne se débranche pas sous vibration.'
  S7: Le phare antibrouillard fait partie d'un ensemble d'éléments d'éclairage avant. Lors d'un remplacement, vérifiez l'état
    des pièces adjacentes pour éviter de devoir réparer à nouveau dans un délai court. - Ampoule de phare avant — Si l'optique
    antibrouillard est remplacée à cause d'une casse, vérifiez que l'ampoule interne n'a pas subi de choc. Un filament brisé
    ou une ampoule noircie doit être substituée simultanément. - Relais de phare — Le relais commande l'alimentation électrique
    de l'antibrouillard. Un relais défaillant coupe l'alimentation de manière aléatoire. À tester si le phare fonctionne par
    intermittence malgré les connexions correctes. - Fusible du circuit antibrouillard — Première vérification à effectuer
    avant tout remplacement de phare. Un fusible grillé coupe l'alimentation de l'optique entière. Remplacez par un fusible
    de même ampérage. - Grille ou protection avant de carrosserie — Si le phare antibrouillard a été endommagé par un choc,
    le support de fixation dans le bouclier peut être fissuré. Un support cassé rend le remontage impossible sans réparation
    préalable. Confirmez systématiquement que le phare de remplacement est conçu pour le bon côté du véhicule (avant gauche
    ou avant droit) et correspond à la version d'équipement d'origine de votre modèle.
  S8: Comment choisir un phare antibrouillard compatible avec mon véhicule ?Renseignez la marque, le modèle, l'année de mise
    en circulation et le type de motorisation dans le sélecteur de véhicule. La référence exacte du phare (OEM) figure sur
    l'étiquette collée à l'arrière du boîtier d'origine. Notez également le côté de montage (gauche ou droit) et la technologie
    d'ampoule (H1, H3, H7, HID ou LED) avant de comparer les références disponibles.Mon phare antibrouillard s'est fissuré
    suite à un impact, puis-je continuer à rouler ?Un phare antibrouillard fissuré doit être remplacé rapidement. La fissure
    crée une entrée d'humidité qui détériore l'ampoule et les connecteurs électriques en quelques semaines. De plus, un boîtier
    fissuré peut être signalé lors d'un contrôle technique si le phare est actif au moment du contrôle. L'intervention reste
    accessible et peu coûteuse si réalisée tôt.Puis-je remplacer uniquement l'ampoule plutôt que tout le phare antibrouillard
    ?Oui, si l'optique et le boîtier sont en bon état, le remplacement de la seule ampoule est possible et suffit dans la
    grande majorité des cas de panne. Identifier le type d'ampoule (H1, H3, H7) depuis la documentation du véhicule ou l'étiquette
    sur le boîtier. Utiliser des gants pour la manipulation et veiller à ne pas toucher le verre de l'ampoule halogène avec
    les doigts.Le contrôle technique vérifie-t-il les phares antibrouillard ?Oui. Le contrôle technique vérifie l'allumage,
    l'intensité et l'orientation des phares antibrouillard avant. Un phare inactif, fissuré ou mal orienté constitue une défaillance
    qui entraîne une contre-visite. L'homologation ECE de la pièce de remplacement est vérifiée si la pièce est présentée
    lors d'un contrôle de conformité.
  META: '{"meta_title":"Phare antibrouillard : inactif, jauni, optique embuée ? | AutoMecanik","meta_description":"Antibrouillard
    inactif, éclairage jauni ou optique embuée ? Ce guide explique comment diagnostiquer et trouver le phare antibrouillard
    compatible avec votre véhicule.","og_title":"Phares antibrouillard : diagnostic et compatibilité","og_description":"Antibrouillard
    inactif, éclairage jauni ou optique embuée ? Ce guide explique comment diagnostiquer et trouver le phare antibrouillard
    compatible avec votre véhicule.","schema_type":"Article","pri mary_intent":"diagnostic","gate_report":"PASS","char_count_title":58,"char_c
    ount_desc":178}'
---

# Phares antibrouillard - Guide Diagnostic Complet

## Fonction et Rôle

Dirige la lumière pour améliorer la visibilité par temps de brouillard ou mauvaise visibilité

**Actions principales:** diriger, diffuser, eclairer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- antibrouillard inactif
- eclairage faible ou jauni
- optique fissuree ou embuee

## Procédure de Diagnostic

Pour diagnostiquer un problème de phares antibrouillard:

1. **Inspection visuelle** - Examiner l'état du phares antibrouillard
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

- ampoule-feu-avant
- relais-phare

## Critères de Compatibilité

Pour commander le bon phares antibrouillard, vous devez connaître:

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

**Comment choisir Phares antibrouillard compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Phares antibrouillard ?**
En cas de antibrouillard inactif ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Phares antibrouillard sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
## Phares et feux

### Phares faibles
- **Ampoules vieillissantes** : Les ampoules halogènes perdent 20-30% de luminosité après 2-3 ans. Remplacement par paire recommandé.
- **Optiques ternies** : Le polycarbonate des phares jaunit et devient opaque avec le temps. Kit de rénovation ou polissage.
- **Réglage incorrect** : Phares trop bas après un chargement ou un remplacement. Réglage avec les vis dédiées.

### Ampoules grillées fréquemment
- **Surtension** : Régulateur d'alternateur défaillant (tension > 14.8V). Mesurer la tension de charge.
- **Vibrations excessives** : Ampoule mal fixée dans son support, vibrations transmises au filament.
- **Mauvaise qualité** : Préférer des ampoules de marque (Philips, Osram, Bosch).

### Feux qui ne fonctionnent pas
- **Fusible grillé** : Vérifier le fusible correspondant dans la boîte à fusibles.
- **Connecteur oxydé** : Humidité dans le porte-ampoule, nettoyage et graisse contact.
- **Problème de masse** : Fil de masse corrodé au niveau du feu. Fréquent sur les feux arrière.

## Contrôle technique - Points éclairage

- Tous les feux doivent fonctionner : croisement, route, position, stop, recul, clignotants, antibrouillard arrière
- Hauteur de faisceau correcte (réglage)
- Pas de fissure laissant entrer l'eau dans les optiques
- Couleur conforme : blanc devant, rouge derrière, orange pour les clignotants

## LED vs Halogène vs Xénon

- **Halogène (H7, H4, H1)** : Standard, remplacement facile, coût faible
- **Xénon (D1S, D2S, D3S)** : Puissant, durée de vie longue, remplacement coûteux, nécessite un ballast
- **LED** : Très longue durée de vie, faible consommation, remplacement du bloc optique entier en cas de panne

## Quand consulter un professionnel

- Phare xénon qui clignote ou change de couleur (ballast ou ampoule)
- Feux LED intégrés défaillants (remplacement du bloc complet)
- Court-circuit récurrent (fusible qui saute à chaque remplacement)
- Défaut de réglage persistant malgré les ajustements
