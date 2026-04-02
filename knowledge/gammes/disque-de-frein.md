---
category: freinage
slug: disque-de-frein
title: Disque de frein
pg_id: 82
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-04-02'
verification_status: draft
intent_targets:
- diagnostic
- achat
- reference
- entretien
business_priority: high
priority_signals:
  avg_basket: 180
  monthly_searches: 12000
  margin_tier: high
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:rag-enrich-from-web-corpus
  last_enriched_at: '2026-04-02'
  v5_migrated_at: '2026-03-29'
_sources:
  ece-r90:
    type: norm
    doc: null
    note: Norme europeenne performances freinage remplacement
  experience-atelier:
    type: field-expertise
    note: Retours atelier partenaire, donnees constructeurs
domain:
  role: Le disque de frein transforme l'energie cinetique du vehicule en chaleur par friction avec les plaquettes, afin de
    ralentir le vehicule de maniere stable et repetable sur chaque essieu
  must_be_true:
  - friction
  - plaquettes
  - chaleur
  - essieu
  - paire
  must_not_contain:
  - tambour de frein
  - frein a main
  confusion_with:
  - term: tambour de frein
    difference: Le tambour utilise des machoires internes, le disque utilise des plaquettes externes pressees par un etrier
  - term: plaquette de frein
    difference: La plaquette est la garniture qui frotte contre le disque. Le disque est le plateau metallique fixe au moyeu
  related_parts:
  - Plaquettes de frein (s'usent avec le disque, a controler systematiquement)
  - Etrier de frein (presse les plaquettes contre le disque)
  - Flexible de frein (transmet la pression hydraulique a l'etrier)
  - Capteur ABS (mesure la vitesse de rotation via la cible ABS du disque)
  - Liquide de frein (a purger si le circuit a ete ouvert)
  norms:
  - ECE R90 — performances de freinage proches de l'equipement d'origine
  cross_gammes:
  - slug: plaquette-de-frein
    relation: always_together
    context: Des plaquettes neuves sur des disques uses ne freinent pas correctement. Remplacer conjointement.
  - slug: etrier-de-frein
    relation: check_on_replace
    context: Controler l'etat de l'etrier et des guidages au demontage du disque
  - slug: flexible-de-frein
    relation: check_on_replace
    context: Verifier l'etat du flexible si le circuit hydraulique est ouvert
  - slug: liquide-de-frein
    relation: check_on_replace
    context: Purger le liquide de frein si le circuit hydraulique a ete ouvert
selection:
  criteria:
  - 'Essieu : avant (70% de l''effort de freinage, ventile standard) ou arriere (stabilite, plein ou ventile selon vehicule)'
  - 'Type : plein, ventile, perfore (sport/circuit), rainure (sport/utilitaire charge)'
  - Diametre et epaisseur (specifiques au vehicule)
  - Bague ABS integree ou non (selon modele)
  - 'Usage : standard (urbain/mixte 40-80 EUR/paire), haute capacite (montagne 80-150 EUR), sport (150-400 EUR)'
  checklist:
  - Verifier l'essieu concerne (avant ≠ arriere)
  - Confirmer le type (plein ou ventile)
  - Commander par paire (2 disques meme essieu)
  - Verifier si bague ABS integree necessaire
  - Choisir selon l'usage (standard, haute capacite, sport)
  - Penser aux plaquettes (les changer en meme temps si usees)
  - Privilegier une marque reconnue
  - Si stationnement exterieur frequent, preferer un traitement anti-corrosion
  anti_mistakes:
  - Commander sans verifier l'essieu (avant ≠ arriere)
  - Remplacer un seul disque au lieu des deux sur le meme essieu
  - Choisir uniquement sur le prix sans verifier marque et qualite
  - Oublier de verifier l'etat des plaquettes au changement de disques
  - Commander des disques perces pour un usage urbain (inutile et plus cher)
  - Confondre plein et ventile
  - Ne pas verifier si le vehicule necessite une bague ABS integree
  cost_range:
    min: 31
    max: 145
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  compatibility_notes: 'Main d''oeuvre supplementaire : 100 a 200 EUR selon vehicule'
  brands:
    premium:
    - Brembo
    - ATE
    - Bosch
    - TRW
    equivalent:
    - Valeo
    - Ferodo
    - Textar
    budget:
    - NK
    - Delphi
  quality_tiers:
  - tier: Equipementiers premium
  - tier: Equipementiers reconnus
  - tier: Economique certifie ECE R90
diagnostic:
  symptoms:
  - id: S1
    label: Vibrations au volant au freinage (surtout a vitesse elevee)
    severity: securite
  - id: S2
    label: Pulsation dans la pedale de frein
    severity: securite
  - id: S3
    label: Grincement ou frottement metallique au freinage
    severity: securite
  - id: S4
    label: Distance de freinage allongee
    severity: securite
  - id: S5
    label: Traces bleutees ou rainures profondes sur la piste du disque
    severity: securite
  - id: S6
    label: Rainures profondes creusees dans la piste de freinage
    severity: securite
  - id: S7
    label: Vehicule qui tire d'un cote au freinage
    severity: securite
  causes:
  - Usure normale (60%) — le disque s'amincit avec les kilometres, remplacement entre 60 000 et 80 000 km en usage mixte
  - Disque voile (20%) — deformation due a un echauffement excessif (descente de col, freinage appuye repete)
  - Montage non conforme (10%) — moyeu sale, couple de serrage incorrect, boulons serres a la visseuse sans couple
  - Etrier grippe (5%) — l'etrier ne relache pas la plaquette, le disque chauffe en permanence d'un cote
  - Mauvaise association disque/plaquette (5%) — garniture trop abrasive ou incompatible qui raye le disque
  quick_checks:
  - 'Inspection visuelle a travers les jantes : traces bleues, fissures, rainures profondes ?'
  - 'Essai route : freiner progressivement a 80 km/h, vibrations dans le volant ? pulsation dans la pedale ?'
  - 'Ecoute : bruit de frottement ou grincement metallique au freinage ?'
  - 'Comparaison : la distance de freinage semble-t-elle plus longue qu''avant ?'
  workshop_checks:
  - Mesure d'epaisseur au pied a coulisse en plusieurs points (comparer a la cote mini gravee sur le disque)
  - 'Mesure du voile au comparateur (tolerance : 0.05-0.07 mm)'
  - Controle du faux-rond du moyeu avant montage du disque neuf
  - 'Verification etat de surface : pas de fissures, pas de points chauds, pas de corrosion excessive sur la piste'
  immediate_replace:
  - Epaisseur sous le minimum constructeur (cote gravee sur le disque)
  - Fissure visible sur la piste de freinage
  - Deformation importante (voile > 0.1 mm)
  - Traces de surchauffe severe (coloration bleu-violet sur toute la piste)
  - Freinage instable ou perte d'efficacite ressentie
  depose_steps: []
maintenance:
  interval:
    value: 60000-80000
    unit: km
    note: Epaisseur sous minimum constructeur = remplacement immediat
    source: experience-atelier
  good_practices:
  - Inspection visuelle a travers les jantes a chaque revision ou tous les 15 000 km
  - Mesure d'epaisseur a chaque changement de plaquettes
  - Controle du voile si vibrations au freinage
  do_not:
  - Ignorer les vibrations au freinage en esperant que ca passe
  - Utiliser de la graisse en zone de friction (piste du disque)
  wear_signs:
  - Rainures profondes visibles sur la piste
  - Bord du disque en relief (la piste s'est creusee)
  - Traces de rouille sur la piste de freinage (stationnement prolonge)
  - Vibrations au freinage qui apparaissent progressivement
installation:
  difficulty: moyen
  time: 1-2h
  tools:
  - Cle dynamometrique
  - Pied a coulisse
  - Cric et chandelles
  - Cle a douille (taille selon vehicule)
  prerequisite: Vehicule sur chandelles, roue demontee
  steps:
  - Demonter la roue et securiser le vehicule sur chandelles
  - Demonter l'etrier de frein et le suspendre (ne pas laisser pendre par le flexible)
  - Retirer l'ancien disque du moyeu
  - Nettoyer la surface du moyeu (eliminer rouille et debris)
  - Monter le disque neuf sur le moyeu (verifier l'absence de jeu)
  - Remonter l'etrier et les plaquettes (neuves si usees)
  - Serrer les boulons de roue a la cle dynamometrique au couple prescrit
  - Repeter de l'autre cote (toujours par paire sur le meme essieu)
  - Pomper la pedale de frein plusieurs fois avant de demarrer (rattraper le jeu)
  - 'Rodage : 200 km de conduite moderee, eviter les freinages brusques'
  post_checks:
  - Pedale de frein ferme apres pompage ?
  - Pas de bruit anormal au freinage ?
  - Pas de vibration au volant ?
  - 'Verification apres 50 km : resserrer les boulons au couple si necessaire'
  common_errors:
  - Ne pas nettoyer le moyeu avant montage (provoque un faux-rond)
  - Serrer les boulons a la visseuse sans cle dynamometrique
  - Laisser l'etrier pendre par le flexible (risque de rupture)
  - Oublier de pomper la pedale avant de demarrer
  - Ne pas respecter la periode de rodage (200 km)
  pro_only: false
rendering:
  pgId: '82'
  intro_title: A quoi sert le disque de frein ?
  risk_title: Pourquoi remplacer le disque de frein a temps ?
  risk_explanation: Un disque use ou voile reduit l'efficacite de freinage et peut endommager les plaquettes neuves.
  risk_consequences:
  - Distance de freinage allongee (risque d'accident)
  - Destruction prematuree des plaquettes neuves
  - Vibrations transmises au volant et a la pedale
  - Surchauffe pouvant fissurer le disque
  risk_conclusion: Un controle visuel regulier et un remplacement par paire evitent la majorite des problemes.
  arguments:
  - title: Compatibilite verifiee
    icon: check-circle
    source_ref: null
  - title: Priorite securite
    icon: shield-check
    source_ref: null
  - title: Decision rapide
    icon: clock
    source_ref: null
  - title: Montage maitrise
    icon: list-check
    source_ref: null
  faq:
  - question: Faut-il changer les disques et les plaquettes ensemble ?
    answer: Oui dans la plupart des cas. Des plaquettes neuves sur des disques uses ne freinent pas de maniere optimale. Prevoyez
      le remplacement conjoint.
  - question: Plein ou ventile, lequel choisir ?
    answer: Pour l'avant, ventile (standard). Pour l'arriere, respectez le type d'origine. Notre selecteur indique le bon
      type.
  - question: Combien de temps durent les disques de frein ?
    answer: En moyenne 60 000 a 80 000 km en usage mixte. En conduite urbaine intensive, l'usure peut etre plus rapide.
  - question: Quelle difference entre un disque a 20 EUR et un a 60 EUR ?
    answer: Le prix reflete la qualite des materiaux et la precision de fabrication. Un disque de marque reconnue offre un
      freinage plus constant et une meilleure duree de vie.
  - question: Peut-on changer ses disques soi-meme ?
    answer: Le remplacement est possible pour un bricoleur equipe, mais le freinage est un element de securite critique. En
      cas de doute, confiez le montage a un professionnel. Prevoyez 200 km de rodage.
  - question: Faut-il changer les 2 cotes en meme temps ?
    answer: Oui, toujours par paire sur le meme essieu. Un disque neuf d'un cote et un disque use de l'autre cree un desequilibre
      de freinage dangereux.
  schema_org:
  - type: FAQPage
    source_bloc: rendering
  - type: HowTo
    source_bloc: E
  - type: Product
    source_bloc: B
  quality:
    score: 92
    source: manual:template-v4
    version: GammeContentContract.v4
seo_cluster:
  source: keyword-dataset
  updated_at: '2026-02-23'
  schema_version: '1.0'
  primary_keyword:
    text: disque de frein
    volume: 50000
    traffic_range: 25000-125000/mo
    intent: informationnelle
  keyword_variants:
  - keyword: disque de frein arriere
    volume: 5000
    traffic_range: 2500-12500/mo
    intent: informationnelle
    competition: forte
  - keyword: disque frein
    volume: 5000
    traffic_range: 2500-12500/mo
    intent: informationnelle
    competition: forte
  - keyword: disque de frein brembo
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
    competition: moyenne
  - keyword: disque de frein ate
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
    competition: moyenne
  - keyword: prix disque et plaquette de frein peugeot 208
    volume: 500
    traffic_range: 250-1250/mo
    intent: transactionnelle
    competition: moyenne
  - keyword: prix plaquette et disque de frein clio 4
    volume: 500
    traffic_range: 250-1250/mo
    intent: transactionnelle
    competition: moyenne
  - keyword: disque de frein clio 2
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
    competition: moyenne
  - keyword: disque de frein bosch
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
    competition: moyenne
  - keyword: disque de frein 207
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
    competition: moyenne
  - keyword: bosch disque de frein
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
    competition: moyenne
  paa_questions: []
  role_mapping:
    R1: prix disque et plaquette de frein peugeot 208
    R3_guide: disque de frein
    R3_conseils: quand changer disque de frein
    R4: disque de frein definition
    R5: symptome disque de frein use
doc_id: c2ffc7ca-9e43-5b1f-8a92-349e1da6abe6
content_hash: sha256:53c1d39d80ff4aba
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
phase5_enrichment:
  _source: ate-freinage.fr + bremboparts.com + delphiautoparts.com + ferodo.com + gpa26.com + profauto.fr + textar.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 85
  types_variants:
  - type: 'bi-matière'
    source_ref: corpus RAG web OEM
  - type: 'composite'
    source_ref: corpus RAG web OEM
  - type: 'céramique'
    source_ref: corpus RAG web OEM
  - type: 'perforé'
    source_ref: corpus RAG web OEM
  - type: 'plein'
    source_ref: corpus RAG web OEM
  - type: 'rainuré'
    source_ref: corpus RAG web OEM
  - type: 'ventilé'
    source_ref: corpus RAG web OEM
  technical_notes:
    norme_ece_r90: 'ECE R90'
    val_0_035_mm: '0,035 mm'
    val_0_05_mm: '0,05 mm'
    val_0_050_mm: '0,050 mm'
    val_0_1_mm: '0,1 mm'
    val_0_10_mm: '0,10 mm'
    val_0_12_mm: '0,12 mm'
    val_10__v: '10. V'
    val_100__: '100 %'
    val_100_a: '100 a'
    val_11_a: '11 a'
    val_110_nm: '110 Nm'
    val_115_nm: '115 Nm'
    val_120_nm: '120 Nm'
    val_2_a: '2 a'
    val_20__: '20 %'
  materials:
  - materiau: 'ALUMINIUM'
    source_ref: corpus RAG web OEM
  - materiau: 'acier inox'
    source_ref: corpus RAG web OEM
  - materiau: 'aluminium'
    source_ref: corpus RAG web OEM
  - materiau: 'carbone-céramique'
    source_ref: corpus RAG web OEM
  - materiau: 'fonte grise'
    source_ref: corpus RAG web OEM
  - materiau: 'graphite'
    source_ref: corpus RAG web OEM
  - materiau: 'silicone'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le disque de frein transforme l''energie cinetique du vehicule en chaleur par friction avec les plaquettes, afin de
    ralentir le vehicule de maniere stable et repetable sur chaque essieu. Niveau de difficulte : Moyen — le disque de frein
    est un organe de securite. Travail sous le vehicule obligatoire. Temps estime : 45 min a 1h30 par essieu selon l''experience
    et l''etat de la boulonnerie. Outils necessaires : - Cric hydraulique + chandelles de securite- Cle dynamometrique (pour
    le couple de serrage des boulons de roue et vis de colonnettes)- Repousse-piston (pour reculer le piston de l''etrier)-
    Nettoyant frein (pour degraisser le disque neuf)- Brosse metallique (pour nettoyer le moyeu)- Cle Torx ou 6 pans (selon
    le vehicule, pour la vis de guidage du disque) Pieces liees : Plaquettes de frein (s''usent avec le disque, a controler
    systematiquement), Etrier de frein (presse les plaquettes contre le disque), Flexible de frein (transmet la pression hydraulique
    a l''etrier), Capteur ABS (mesure la vitesse de rotation via la cible ABS du disque), Liquide de frein (a purger si le
    circuit a ete ouvert).'
  S2: 'Les disque de frein sont à remplacer tous les 60 000 à 80 000 km environ. Epaisseur sous minimum constructeur = remplacement
    immediat Symptômes d''usure : - Vibrations au volant au freinage (surtout a vitesse elevee) - Pulsation dans la pedale
    de frein - Grincement ou frottement metallique au freinage - Distance de freinage allongee - Traces bleutees ou rainures
    profondes sur la piste du disque - Rainures profondes creusees dans la piste de freinage - Vehicule qui tire d''un cote
    au freinage'
  S2_DIAG: 'SymptômeCause probableActionVibrations au volant au freinage (surtout a vitesse elevee)Usure normale (60%) — le
    disque s''amincit avec les kilometres, remplacement entre 60 000 et 80 000 km en usage mixteInspection visuelle a travers
    les jantes : traces bleues, fissures, rainures profondes ?Pulsation dans la pedale de freinDisque voile (20%) — deformation
    due a un echauffement excessif (descente de col, freinage appuye repete)Essai route : freiner progressivement a 80 km/h,
    vibrations dans le volant ? pulsation dans la pedale ?Grincement ou frottement metallique au freinageMontage non conforme
    (10%) — moyeu sale, couple de serrage incorrect, boulons serres a la visseuse sans coupleEcoute : bruit de frottement
    ou grincement metallique au freinage ?Distance de freinage allongeeEtrier grippe (5%) — l''etrier ne relache pas la plaquette,
    le disque chauffe en permanence d''un coteComparaison : la distance de freinage semble-t-elle plus longue qu''avant ?Traces
    bleutees ou rainures profondes sur la piste du disqueMauvaise association disque/plaquette (5%) — garniture trop abrasive
    ou incompatible qui raye le disqueInspection visuelle a travers les jantes : traces bleues, fissures, rainures profondes
    ?Rainures profondes creusees dans la piste de freinageUsure normale (60%) — le disque s''amincit avec les kilometres,
    remplacement entre 60 000 et 80 000 km en usage mixteInspection visuelle a travers les jantes : traces bleues, fissures,
    rainures profondes ?'
  S3: 'Pour choisir les bons disque de frein pour votre véhicule : - Essieu : avant (70% de l''effort de freinage, ventile
    standard) ou arriere (stabilite, plein ou ventile selon vehicule) - Type : plein, ventile, perfore (sport/circuit), rainure
    (sport/utilitaire charge) - Diametre et epaisseur (specifiques au vehicule) - Bague ABS integree ou non (selon modele)
    - Usage : standard (urbain/mixte 40-80 EUR/paire), haute capacite (montagne 80-150 EUR), sport (150-400 EUR)'
  S4_DEPOSE: 1. Lever le véhicule, déposer la roue, sécuriser sur chandelles 2. Dévisser la vis de guidage du disque (Torx
    ou 6 pans) 3. Déposer l'étrier (2 vis de coulisse) — ne PAS laisser pendre par le flexible 4. Suspendre l'étrier avec
    un fil de fer ou crochet 5. Retirer le disque usé (frapper légèrement si collé par la corrosion)
  S4_REPOSE: '- Nettoyer le moyeu de roue à la brosse métallique — éliminer toute trace de rouille (ceci évite les vibrations
    au freinage) - Comparer le disque neuf avec l''ancien : diamètre, épaisseur, type (plein ou ventilé), centrage - Pour
    les disques arrière avec ABS : vérifier que le roulement et la bague ABS sont intégrés si le modèle l''exige - Dégraisser
    le disque neuf au nettoyant frein (retirer la paraffine de protection de stockage) - Poser le disque sur le moyeu, visser
    les vis de guidage - Installer les plaquettes neuves (disque neuf = plaquettes neuves obligatoires) - Repousser le piston
    de l''étrier avec un repousse-piston adapté - Remonter l''étrier, serrer les vis de colonnettes au couple constructeur
    - Reposer la roue, serrer les boulons au couple (ex : 110 Nm, vérifier la valeur constructeur) - Descendre le véhicule
    des chandelles - Pomper la pédale de frein plusieurs fois jusqu''à obtenir une pédale dure — ne jamais démarrer sans cette
    étape Rodage : 200 à 300 km avec des freinages progressifs. Éviter tout freinage brusque pendant cette période. ✅ Après
    remontage, vérifiez les spécifications dans la fiche technique Disque de frein.'
  S5: '- Commander sans verifier l''essieu (avant ≠ arriere) - Remplacer un seul disque au lieu des deux sur le meme essieu
    - Choisir uniquement sur le prix sans verifier marque et qualite - Oublier de verifier l''etat des plaquettes au changement
    de disques - Commander des disques perces pour un usage urbain (inutile et plus cher) - Confondre plein et ventile - Ne
    pas verifier si le vehicule necessite une bague ABS integree'
  S6: 'Après le montage de disques de frein neufs, plusieurs vérifications sont indispensables avant de reprendre la route
    normalement. Le freinage est un système de sécurité : une erreur de montage peut avoir des conséquences graves. Voici
    les points de contrôle à effectuer dans l''ordre. Vérifications immédiates avant de démarrer - Pomper la pédale de frein
    : Avant tout démarrage, appuyez sur la pédale plusieurs fois de suite jusqu''à ce qu''elle devienne ferme et résistante.
    Les étriers ont besoin de rattraper le jeu avec les plaquettes neuves. Une pédale molle au premier appui est normale —
    elle ne doit pas rester molle. - Niveau de liquide de frein : Vérifier que le niveau dans le bocal est entre MIN et MAX.
    Si le circuit a été ouvert (étrier démonté), purger les éventuelles bulles d''air, car une bulle dans le circuit entraîne
    une pédale spongieuse. - Absence de fuite hydraulique : Inspecter visuellement le flexible de frein , les raccords d''étrier
    et les canalisations. Aucune trace de liquide de frein ne doit être visible sur les pièces ou sur le sol sous le véhicule.
    - Fixation des boulons de roue : Contrôler le serrage au couple prescrit par le constructeur à la clé dynamométrique.
    Un boulon insuffisamment serré peut provoquer un voile du disque en cours de route. Vérifications après le premier déplacement
    à basse vitesse - Essai de freinage progressif à 30 km/h : Freiner doucement depuis 30 km/h jusqu''à l''arrêt. La pédale
    doit être ferme et la décélération linéaire. Aucune vibration ni déviation de trajectoire ne doit être ressentie. - Absence
    de bruit anormal : Un léger bruit de frottement pendant les premiers kilomètres est acceptable (rodage de la surface du
    disque). Un grincement métallique persistant ou un crissement aigu signale un problème (plaquette mal positionnée, corps
    étranger entre disque et plaquette). - Absence de vibrations au volant : Si des vibrations apparaissent dès le premier
    freinage, vérifier immédiatement le couple de serrage des boulons de roue et la propreté de la surface du moyeu. Un moyeu
    sale ou une rondelle oubliée crée un faux-rond immédiat. Période de rodage : 200 km obligatoires - Conduite modérée pendant
    200 km : Éviter les freinages brusques et les montées en température brutales. Le rodage permet à la surface du disque
    et à la garniture des plaquettes de se polir mutuellement pour une surface de contact uniforme. - Pas de freinages répétés
    depuis haute vitesse : Descentes de col, autoroute avec décélération d''urgence répétée — à éviter pendant la phase de
    rodage. Un disque neuf non rodé peut se voiler sous l''effet de la chaleur. Vérification à 50 km - Resserrage des boulons
    de roue au couple : Après 50 km, démonter les roues et re-serrer les boulons à la clé dynamométrique au couple prescrit.
    Les boulons neufs ou réinstallés peuvent légèrement se desserrer au premier usage. C''est une précaution standard pour
    tout remplacement de disques. - Contrôle visuel des disques : Observer l''état de surface des disques à travers les jantes.
    La piste de freinage doit présenter une couleur homogène sans traces bleues localisées (points chauds). Des traces bleues
    signalent une surchauffe liée à un étrier grippé ou à un rodage trop agressif.'
  S_GARAGE: 'Nous vous recommandons de confier cette intervention à un professionnel : - Plusieurs causes possibles de défaillance
    (5 identifiées) nécessitent un diagnostic professionnel - Erreurs fréquentes en atelier amateur : Ne pas nettoyer le moyeu
    avant montage (provoque un faux-rond) ; Serrer les boulons a la visseuse sans cle dynamometrique ; Laisser l''etrier pendre
    par le flexible (risque de rupture) Un garagiste qualifié dispose de l''outillage et de l''expérience nécessaires pour
    effectuer cette opération en toute sécurité.'
  S7: Quel est le prix d'un disque de frein ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur pour trouver
    le disque de frein compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment savoir
    si mon disque de frein est à changer ?Les signes d'usure les plus courants sont détaillés dans la section diagnostic ci-dessus.
    En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un disque de frein défaillant ?Cela
    dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule. Consultez la section symptômes
    pour évaluer l'urgence du remplacement.- Plaquettes de frein (s'usent avec le disque, a controler systematiquement) -
    Etrier de frein (presse les plaquettes contre le disque) - Flexible de frein (transmet la pression hydraulique a l'etrier)
    - Capteur ABS (mesure la vitesse de rotation via la cible ABS du disque) - Liquide de frein (a purger si le circuit a
    ete ouvert)
  S8: Faut-il changer les disques et les plaquettes ensemble ?Oui dans la plupart des cas. Des plaquettes neuves sur des disques
    uses ne freinent pas de maniere optimale. Prevoyez le remplacement conjoint. Plein ou ventile, lequel choisir ?Pour l'avant,
    ventile (standard). Pour l'arriere, respectez le type d'origine. Notre selecteur indique le bon type. Combien de temps
    durent les disques de frein ?En moyenne 60 000 a 80 000 km en usage mixte. En conduite urbaine intensive, l'usure peut
    etre plus rapide. Quelle difference entre un disque a 20 EUR et un a 60 EUR ?Le prix reflete la qualite des materiaux
    et la precision de fabrication. Un disque de marque reconnue offre un freinage plus constant et une meilleure duree de
    vie. Peut-on changer ses disques soi-meme ?Le remplacement est possible pour un bricoleur equipe, mais le freinage est
    un element de securite critique. En cas de doute, confiez le montage a un professionnel. Prevoyez 200 km de rodage. Faut-il
    changer les 2 cotes en meme temps ?Oui, toujours par paire sur le meme essieu. Un disque neuf d'un cote et un disque use
    de l'autre cree un desequilibre de freinage dangereux.
  META: '- Quand remplacer disques de frein sur Golf 4 1.9 TDI.'
---

# Disque de frein

## Reference technique

Le disque de frein est un composant de securite du systeme de freinage. Il transforme l'energie cinetique du vehicule en chaleur par friction avec les plaquettes de frein.

### Types de disques

| Type | Usage | Caracteristiques |
|------|-------|-----------------|
| **Plein** | Arriere (vehicules legers) | Moins cher, suffisant pour faible sollicitation |
| **Ventile** | Avant (standard) | Deux pistes separees par des ailettes, meilleure evacuation de la chaleur |
| **Perfore** | Sport / circuit | Trous pour evacuer gaz et eau, mordant a chaud |
| **Rainure** | Sport / utilitaire charge | Rainures pour evacuer poussieres de garniture, mordant constant |

### Normes et specifications

- **ECE R90** : Norme europeenne imposant des performances de freinage proches de l'equipement d'origine pour toute piece de remplacement
- **Cote minimale** : Epaisseur minimale gravee sur le disque (ex : MIN TH 22.0 mm). En dessous = remplacement obligatoire
- **Voile maximal** : Tolerance de faux-rond, generalement 0.05 a 0.07 mm. Au-dela = vibrations au freinage

### Pieces associees

- **Plaquettes de frein** : S'usent avec le disque, a controler systematiquement
- **Etrier de frein** : Presse les plaquettes contre le disque
- **Flexible de frein** : Transmet la pression hydraulique a l'etrier
- **Capteur ABS** : Mesure la vitesse de rotation de la roue via la cible ABS du disque
- **Liquide de frein** : A purger si le circuit a ete ouvert

## Diagnostic

### Symptomes specifiques au disque de frein

| Symptome | Description | Urgence |
|----------|-------------|---------|
| **Vibrations au volant au freinage** | Le volant tremble quand on freine, surtout a vitesse elevee | Moyenne - faire controler |
| **Pulsation dans la pedale** | La pedale de frein pulse sous le pied au freinage | Moyenne |
| **Grincement metallique** | Bruit de metal contre metal : les plaquettes sont usees jusqu'a l'ame | Haute - securite |
| **Distance de freinage allongee** | Le vehicule met plus de distance a s'arreter | Haute - securite |
| **Traces bleutees sur la piste** | Surchauffe du disque, points chauds visibles | Haute - remplacement |
| **Rainures profondes** | Sillons creuses dans la piste de freinage | Moyenne - mesurer epaisseur |
| **Tire d'un cote au freinage** | Un etrier grippe ou un disque plus use que l'autre | Haute - securite |

### Causes probables (du plus frequent au plus rare)

1. **Usure normale** (60%) : Le disque s'amincit avec les kilometres. Remplacement entre 60 000 et 80 000 km en usage mixte.
2. **Disque voile** (20%) : Deformation due a un echauffement excessif (descente de col, freinage appuye repete). Provoque vibrations au volant.
3. **Montage non conforme** (10%) : Moyeu sale, couple de serrage incorrect, boulons de roue serres a la visseuse sans couple.
4. **Etrier grippe** (5%) : L'etrier ne relache pas la plaquette, le disque chauffe en permanence d'un cote.
5. **Mauvaise association disque/plaquette** (5%) : Garniture trop abrasive ou incompatible qui raye le disque.

### Tests simples (sans outil)

- **Inspection visuelle** : Regarder le disque a travers les jantes. Traces bleues, fissures, rainures profondes ?
- **Essai route** : Freiner progressivement a 80 km/h. Vibrations dans le volant ? Pulsation dans la pedale ?
- **Ecoute** : Bruit de frottement ou grincement metallique au freinage ?
- **Comparaison** : La distance de freinage semble-t-elle plus longue qu'avant ?

### Tests atelier

- **Mesure d'epaisseur** au pied a coulisse en plusieurs points (comparer a la cote mini gravee sur le disque)
- **Mesure du voile** au comparateur (tolerance : 0.05-0.07 mm)
- **Controle du faux-rond du moyeu** avant montage du disque neuf
- **Verification etat de surface** : pas de fissures, pas de points chauds, pas de corrosion excessive sur la piste

### Quand remplacer immediatement

- Epaisseur sous le minimum constructeur (cote gravee sur le disque)
- Fissure visible sur la piste de freinage
- Deformation importante (voile > 0.1 mm)
- Traces de surchauffe severe (coloration bleu-violet sur toute la piste)
- Freinage instable ou perte d'efficacite ressentie

## Guide d'achat

### Criteres de choix

**1. Position : avant ou arriere**

| Position | Role | Type standard |
|----------|------|--------------|
| **Avant** | 70% de l'effort de freinage | Ventile |
| **Arriere** | Stabilite au freinage | Plein ou ventile selon vehicule |

Toujours remplacer par essieu (les 2 cotes ensemble).

**2. Type selon l'usage**

| Conduite | Disque recommande | Budget par paire |
|----------|-------------------|-----------------|
| Urbaine / calme | Ventile standard | 40-80 EUR |
| Mixte route/ville | Ventile standard | 40-80 EUR |
| Montagne / vehicule charge | Ventile haute capacite | 80-150 EUR |
| Sportive / circuit | Perfore ou rainure | 150-400 EUR |

**3. Compatibilite**

- Verifier l'essieu (avant ≠ arriere)
- Verifier le type (plein ≠ ventile)
- Verifier le diametre et l'epaisseur
- Verifier si bague ABS integree au disque
- Utiliser le selecteur de vehicule pour eviter les erreurs

### Marques recommandees

**Premium (equipementiers d'origine)**
- **Brembo** : Reference en performance et durabilite
- **ATE** : Specialiste freinage, qualite d'origine
- **Bosch** : Excellent rapport qualite/prix
- **TRW** : Equipementier majeur, large couverture

**Qualite equivalente**
- **Valeo** : Bon rapport qualite/prix
- **Ferodo** : Fiabilite eprouvee
- **Textar** : Qualite d'origine

**Economique**
- **NK** : Budget maitrise, qualite correcte
- **Delphi** : Entree de gamme fiable

### Check-list avant commande

1. Verifier l'essieu concerne (avant ≠ arriere)
2. Confirmer le type (plein ou ventile)
3. Commander par paire (2 disques meme essieu)
4. Verifier si bague ABS integree necessaire
5. Choisir selon l'usage (standard, haute capacite, sport)
6. Penser aux plaquettes (les changer en meme temps si usees)
7. Privilegier une marque reconnue
8. Si stationnement exterieur frequent, preferer un traitement anti-corrosion

### Erreurs a eviter

- Commander sans verifier l'essieu (avant ≠ arriere)
- Remplacer un seul disque au lieu des deux sur le meme essieu
- Choisir uniquement sur le prix sans verifier marque et qualite
- Oublier de verifier l'etat des plaquettes au changement de disques
- Commander des disques perces pour un usage urbain (inutile et plus cher)
- Ignorer les vibrations au freinage en esperant que ca passe
- Confondre plein et ventile
- Ne pas verifier si le vehicule necessite une bague ABS integree

## Entretien

### Intervalles de controle

| Controle | Frequence |
|----------|-----------|
| Inspection visuelle (a travers jantes) | A chaque revision ou tous les 15 000 km |
| Mesure d'epaisseur | A chaque changement de plaquettes |
| Controle du voile | Si vibrations au freinage |

### Duree de vie moyenne

| Type de conduite | Duree de vie estimee |
|------------------|---------------------|
| Urbaine intensive | 40 000 - 60 000 km |
| Mixte | 60 000 - 80 000 km |
| Autoroute | 80 000 - 100 000 km |

### Signes d'usure a surveiller

- Rainures profondes visibles sur la piste
- Bord du disque en relief (la piste s'est creusee)
- Traces de rouille sur la piste de freinage (stationnement prolonge)
- Vibrations au freinage qui apparaissent progressivement

### Remplacement : les regles

- **Toujours par paire** : Les 2 disques du meme essieu en meme temps
- **Avec les plaquettes** : Des plaquettes neuves sur des disques uses ne freinent pas correctement
- **Rodage** : 200 km de conduite moderee apres montage (eviter les freinages brusques)
- **Purge** : Si le circuit hydraulique a ete ouvert, purger le liquide de frein
- **Couples de serrage** : Respecter le couple des boulons de roue (cle dynamometrique obligatoire)

## Installation

### Prerequis et outils

- Vehicule sur chandelles, roue demontee
- Cle dynamometrique, pied a coulisse, cric et chandelles

### Procedure

1. Demonter la roue et securiser le vehicule sur chandelles
2. Demonter l'etrier de frein et le suspendre (ne pas laisser pendre par le flexible)
3. Retirer l'ancien disque du moyeu
4. Nettoyer la surface du moyeu (eliminer rouille et debris)
5. Monter le disque neuf sur le moyeu (verifier l'absence de jeu)
6. Remonter l'etrier et les plaquettes (neuves si usees)
7. Serrer les boulons de roue a la cle dynamometrique au couple prescrit
8. Repeter de l'autre cote (toujours par paire)
9. Pomper la pedale de frein plusieurs fois avant de demarrer
10. Rodage : 200 km de conduite moderee

### Verifications post-montage

- Pedale de frein ferme apres pompage
- Pas de bruit anormal au freinage
- Pas de vibration au volant
- Resserrage boulons au couple apres 50 km

### Erreurs de montage

- Ne pas nettoyer le moyeu avant montage (provoque un faux-rond)
- Serrer les boulons a la visseuse sans cle dynamometrique
- Laisser l'etrier pendre par le flexible (risque de rupture)
- Oublier de pomper la pedale avant de demarrer
- Ne pas respecter la periode de rodage (200 km)

## FAQ

**Faut-il changer les disques et les plaquettes ensemble ?**
Oui dans la plupart des cas. Des plaquettes neuves sur des disques uses ne freinent pas de maniere optimale. Prevoyez le remplacement conjoint.

**Plein ou ventile, lequel choisir ?**
Pour l'avant, ventile (standard). Pour l'arriere, respectez le type d'origine. Notre selecteur indique le bon type.

**Combien de temps durent les disques de frein ?**
En moyenne 60 000 a 80 000 km en usage mixte. En conduite urbaine intensive, l'usure peut etre plus rapide.

**Quelle difference entre un disque a 20 EUR et un a 60 EUR ?**
Le prix reflete la qualite des materiaux et la precision de fabrication. Un disque de marque reconnue offre un freinage plus constant et une meilleure duree de vie.

**Peut-on changer ses disques soi-meme ?**
Le remplacement est possible pour un bricoleur equipe, mais le freinage est un element de securite critique. En cas de doute, confiez le montage a un professionnel. Prevoyez 200 km de rodage.

**Faut-il changer les 2 cotes en meme temps ?**
Oui, toujours par paire sur le meme essieu. Un disque neuf d'un cote et un disque use de l'autre cree un desequilibre de freinage dangereux.
## Definition

La norme ECE R90 encadre la conformite des pieces de freinage de remplacement (ex: plaquettes, disques) avec des exigences de performance proches de l'equipement d'origine.

## Pourquoi c'est important

- meilleure coherence de freinage
- reduction du risque de pieces non conformes
- reference utile pour le choix de pieces sur vehicule de tourisme
## Les criteres essentiels

### 1. Compatibilite vehicule

**Obligatoire** : Les disques doivent etre compatibles avec votre vehicule exact.

Pour trouver les bons disques :
1. Utilisez notre selecteur de vehicule
2. Entrez votre plaque d'immatriculation
3. Ou selectionnez marque/modele/motorisation

Notre systeme affiche uniquement les disques compatibles avec votre vehicule.

### 2. Position : Avant ou Arriere

| Position | Role | Remarque |
|----------|------|----------|
| **Avant** | Freinage principal (70% de l'effort) | Toujours ventile |
| **Arriere** | Stabilite au freinage | Plein ou ventile selon vehicule |

**Conseil** : Remplacez toujours par essieu (les 2 cotes ensemble).

### 3. Type de conduite

| Conduite | Disque recommande | Budget |
|----------|-------------------|--------|
| Urbaine / Calme | Ventile standard | Economique |
| Mixte route/ville | Ventile standard | Economique |
| Montagne / Vehicule charge | Ventile haute capacite | Moyen |
| Sportive / Circuit | Perce ou rainure | Eleve |

## Check-list compatibilite

- Verifiez l'essieu concerne : les disques avant et arriere sont differents, ne les confondez pas
- Confirmez le type de disque : plein ou ventile (notre selecteur vous indique le bon type)
- Commandez toujours par paire : 2 disques pour le meme essieu, jamais un seul
- Verifiez si votre vehicule necessite une bague ABS integree au disque (le selecteur le precise)
- Choisissez selon votre usage : standard pour la ville, haute capacite pour la montagne ou le remorquage
- Pensez a vos plaquettes : si elles sont usees, changez-les en meme temps que les disques
- Privilegiez une marque reconnue : Brembo, ATE, Bosch, TRW ou Valeo pour la fiabilite
- En cas d'hesitation entre deux references, contactez notre service client pour confirmation
- Si votre vehicule stationne souvent dehors, preferez un disque avec traitement anti-corrosion

## Les marques recommandees

### Premium (Equipementiers d'origine)
- **Brembo** : Reference en performance et durabilite
- **ATE** : Specialiste freinage, qualite d'origine
- **Bosch** : Excellent rapport qualite/prix
- **TRW** : Equipementier majeur, large couverture

### Qualite equivalente
- **Valeo** : Bon rapport qualite/prix
- **Ferodo** : Fiabilite eprouvee
- **Textar** : Qualite d'origine

### Economique
- **NK** : Budget maitrise, qualite correcte
- **Delphi** : Entree de gamme fiable

## Conduite urbaine

Freinages frequents mais a basse vitesse. La montee en temperature reste moderee.

### Avantages
Disques ventiles standard suffisent amplement. Budget maitrise, duree de vie longue en usage calme.

### Inconvenients
Si le vehicule stationne souvent dehors, la surface des disques peut rouiller entre deux trajets. Privilegiez un traitement anti-corrosion.

## Route et autoroute

Freinages moins frequents mais a vitesse plus elevee.

### Avantages
Disques ventiles standard avec bonne capacite de refroidissement. Budget raisonnable, securite assuree sur longs trajets.

### Inconvenients
L'usure est moins visible car le kilometrage est eleve entre les controles. Pensez a verifier vos disques a chaque revision.

## Montagne et charge

Descentes prolongees, vehicule charge ou avec remorque. Forte sollicitation des freins.

### Avantages
Disques ventiles haute capacite pour une meilleure evacuation de la chaleur. Freinage stable meme en descente longue.

### Inconvenients
Prix plus eleve que les disques standard. Associez avec des plaquettes adaptees a l'usage intensif pour un resultat optimal.

## Conduite sportive

Freinages appuyes et repetes. Temperatures tres elevees.

### Avantages
Disques perces ou rainures pour un freinage mordant et constant a haute temperature.

### Inconvenients
Usure des plaquettes acceleree. Budget eleve. Bruit de freinage possible. A reserver a un usage reellement sportif.

## Tests simples (sans outil)

- Regardez vos disques a travers les jantes : traces bleues, rainures profondes ou fissures visibles
- Roulez et freinez : vibrations dans le volant ou pulsations dans la pedale
- Ecoutez au freinage : bruit metallique, grincement ou sifflement inhabituel
- Comparez la distance de freinage : si elle vous semble plus longue qu'avant, faites controler

## Tests atelier

- Votre garagiste mesure l'epaisseur restante et la compare au minimum autorise
- Il verifie l'etat de surface : rainures, fissures, traces de surchauffe

## Erreurs a eviter

- Commander des disques sans verifier l'essieu : les disques avant et arriere sont differents
- Remplacer un seul disque au lieu des deux sur le meme essieu
- Choisir uniquement sur le prix sans verifier la marque et la qualite
- Oublier de verifier l'etat des plaquettes quand on change les disques
- Commander des disques perces pour un usage urbain : c'est inutile et plus cher
- Ignorer les vibrations au freinage en esperant que ca passe tout seul
- Confondre plein et ventile en se disant que c'est pareil
- Ne pas verifier si votre vehicule necessite une bague ABS integree au disque

### Faut-il changer les disques et les plaquettes ensemble ?

Oui dans la plupart des cas. Des plaquettes neuves sur des disques uses ne freinent pas de maniere optimale. Prevoyez le remplacement conjoint pour un resultat de freinage homogene.

### Faut-il changer les 2 cotes en meme temps ?

Oui, toujours par paire sur le meme essieu. Un disque neuf d'un cote et un disque use de l'autre cree un desequilibre de freinage dangereux.

### Plein ou ventile : lequel choisir ?

Pour l'avant, choisissez ventile (c'est le standard). Pour l'arriere, respectez le type d'origine de votre vehicule. Notre selecteur vous indique le bon type automatiquement.

### Combien de temps durent les disques de frein ?

En moyenne 60 000 a 80 000 km en usage mixte. En conduite urbaine intensive, l'usure peut etre plus rapide. Faites-les controler a chaque changement de plaquettes.

### Quelle difference entre un disque a 20 EUR et un a 60 EUR ?

Le prix reflete la qualite des materiaux et la precision de fabrication. Un disque de marque reconnue (Brembo, ATE, Bosch) offre un freinage plus constant, une meilleure duree de vie et moins de bruit.

### Peut-on changer ses disques soi-meme ?

Le remplacement est possible pour un bricoleur equipe, mais le freinage est un element de securite critique. En cas de doute, confiez le montage a un professionnel. Prevoyez 200 km de rodage apres le montage.
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

## Recommandations

- **Contrôle visuel** : Vérifier l'épaisseur des plaquettes (minimum 3mm)
- **Kilométrage** : Remplacement préventif tous les 30 000 - 50 000 km
- **Qualité** : Privilégier les marques équipementier (Bosch, Brembo, TRW)


## Conseils supplementaires

<!-- materialized-from-db web/3cb342907fc5 2026-03-28 -->
### Instructions pour remplacer... - Montage auto - section-1

# Instructions pour remplacer... - Montage auto

- Skip to main content Skip to menu Skip to footer Partager sur Instructions pour remplacer les maîtres-cylindres de frein ou les cylindres des maîtres-cylindres de frein Nous vous conseillons de lire et de suivre attentivement les instructions fournies. Vous trouverez les mêmes instructions dans l’emballage des maîtres-cylindres. N’oubliez pas de les conserver pendant toute la durée de vie du produit. En cas de passage de propriété, elles devront être remises au nouveau propriétaire du véhicule. Indications générales 1. Utiliser uniquement du liquide de frein DOT3 ou DOT4, à l’exception des véhicules qui requièrent du liquide de frein DOTS (à base de silicium). 2. Le liquide de frein doit être complètement remplacé après que le réservoir a été soigneusement lavé avec de l'alcool dénaturé. 3. À cause de la nature technique du produit, les maîtres-cylindres de frein doivent être remplacés par un technicien qualifié et, en cas de réclamation, il faudra le démontrer à l’aide d'une facture. Procédure de remplacement 1. Si le cylindre est équipé de vis de purge, brancher la vis de purge du cylindre à un tuyau en caoutchouc et placer l'extrémité libre du tuyau dans un récipient transparent. 2. Déposer les couvertures, supports, branchements électriques ou autres pièces éventuelles, qui gêneront la dépose du cylindre une fois desserré. 3. Desserrer légèrement les vis des tuyaux en retenant les tuyaux de sortie. 4. Déposer les vis ou les boulons qui retiennent le cylindre sur le servofrein ou sur le pare-feu. 5. Desserrer complètement les vis du tuyau de sortie et éloigner les tuyaux du cylindre, en faisant attention à ne pas les plier ni les déformer. Placer un chiffon sous le cylindre pour capturer la sortie de liquide et déposer le cylindre. 6. Si le liquide de frein se renverse sur la peinture, laver immédiatement avec de l'eau. Procédure de montage 1. Retirer les capuchons de protection du nouveau cylindre. 2. Contrôler que le joint de sortie de l’unité servo, si présente, est monté correctement et est en bon état. 3. Placer le cylindre (si possible, avec le réservoir déjà inséré) et contrôler attentivement que la tige de poussée du servo soit positionnée correctement ou que la tige de poussée reliée à la pédale de frein puisse se déplacer librement. 4. Remettre en place les boulons ou les vis de montage du cylindre, en les remplaçant s’ils sont endommagés. Le couple de serrage des boulons doit correspondre à celui recommandé par le constructeur du véhicule. 5. Brancher les connecteurs du tuyau de frein, en veillant à ce que le filetage sur les connecteurs du tuyau et le cylindre correspondent. Serrer les connecteurs selon les couples de serrage recommandé par le constructeur du véhicule. 6. Monter le réservoir et remplir avec le liquide de frein comme spécifié par le constructeur du véhicule. 7. Si le système ABS est installé, suivre scrupuleusement toutes les instructions du constructeur du véhicule. 8. Purger le système de freinage en suivant les instructions du constructeur du véhicule. 9. Vérifier la présence de fuites sur le système de freinage. 10. Contrôler le niveau du liquide de frein. 11. Effectuer un essai sur route. Informations générales et de sécurité Le produit Brembo a été conçu pour respecter les meilleurs standards de sécurité . Les Produits ne doivent pas être destinés à une utilisation différente de celle pour laquelle ils ont été conçus et fabriqués. L’ utilisation à d’autres fins , la modification ou la manipulation du produit risquent d’ altérer son fonctionnement et de compromettre sa sécurité . Toute modification éventuelle ou toute utilisation impropre rendent nulles les Limitations de garantie et peuvent rendre la personne utilisant le Produit dans ces conditions responsable quant aux dommages physiques ou matériels éventuellement causés à des tiers. Dans ces instructions, lorsqu’il est indiqué « DANGER! », cela signifie que le non-respect de la procédure indiquée a de fortes probabilités de provoquer de graves dommages physiques ou même la mort . La mention « ATTENTION! » indique une procédure dont le non-respect peut provoquer des dommages physiques, alors que la mention « AVERTISSEMENT! » indique une procédure dont le non-respect peut provoquer des dommages au véhicule. DANGER! Avant de commencer la procédure de remplacement, s’assurer que la pièce de rechange est adaptée à la marque et au modèle du véhicule. Le Produit revêt une importance fondamentale pour la sécurité du véhicule sur lequel il est installé et il doit, donc, être installé par du personnel qualifié ayant reçu une formation adéquate ou possédant suffisamment d’expérience dans l’installation et dans l’utilisation prévue du Produit. L’installateur doit avoir à sa disposition l’ outillage adéquat à l’installation et posséder des connaissances et une expérience appropriées pour s’occuper de l’entretien du véhicule. Une installation inadéquate ou erronée, due au non-respect de ces instructions ou autres, rendra nulles les Limitations de garantie et pourrait rendre l’installateur responsable quant aux dommages physiques ou matériels éventuellement provoqués. Il est fondamental de r emplacer les disques de frein pour chaque essieu , en les prélevant de leur emballage. À chaque remplacement des disques, remplacer aussi leurs plaquettes. Éviter le contact de graisse et autres lubrifiants avec les surfaces de freinage du disque et des plaquettes parce que cela risque de rendre le système de freinage inefficace. Brembo décline toute responsabilité en cas de dommage matériel ou physique provoqué à ou par une personne conduisant un véhicule sur lequel le produit aurait été installé de façon inappropriée. ATTENTION! Les pièces remplacées doivent être éliminées selon les dispositions prescrites par la loi. Il est important d’éviter de frapper violemment ou d’endommager le Produit et ses composants, parce que cela risquerait de réduire son efficacité et de provoquer des dysfonctionnements. Si nécessaire, remplacer les composants endommagés. Pour éviter tout dommage physique, nous conseillons de: Toujours porter des gants lors de l’opération de démontage et de remontage des composants présentant des arêtes coupantes.

![Approfondissements](_raw/web-images/2d2507a39e7ef6eb.jpg)

![Comment choisir le bon produit](_raw/web-images/554e6f769f52f78a.jpg)

![Montage auto](_raw/web-images/d8bc5a5c2c667779.jpg)

![Montage moto](_raw/web-images/8f8c2ca53665bfa9.jpg)

![Entretien](_raw/web-images/e936dadf5dced240.jpg)

- Éviter le contact direct de la peau avec le matériau de friction des plaquettes et mâchoires parce que cela risque de provoquer des abrasions.

![Service après-vente](_raw/web-images/c8ff08f5cb503a6a.jpg)

![Limites de garantie](_raw/web-images/3f780074f3f64f27.jpg)

![Contacter le support Brembo](_raw/web-images/1e8d4f4c405ed310.webp)

![WeChat](_raw/web-images/dec8ad591b7cebf6.jpg)

<!-- materialized-from-db web/cf6140b58cea 2026-03-28 -->
### Comment installer correctement les plaquettes de frein - section-1

# Comment installer correctement les plaquettes de frein

- Comment installer correctement les plaquettes de frein Skip Navigation Sélectionner la langue Comment installer correctement les plaquettes de frein Comment installer correctement les plaquettes de frein Travaillez malin lorsque vous remplacez les composants les plus sollicités d'un véhicule. Évitez les bruits de frein, le cliquetis des étriers et le mouvement des plaquettes en suivant ces étapes simples INTRODUCTION La plupart des conducteurs n'accordent pas assez d'importance à leurs freins, considérant qu'ils fonctionneront parfaitement tout le temps. Cependant, après des milliers d'heures de conduite, y compris d'innombrables trajets courts et longs dans tous types de conditions, les freins commencent inévitablement à montrer des signes d'usure tels qu'une réduction de la puissance de freinage, des bruits parasites ou d'autres problèmes. Bien que le remplacement des plaquettes de frein - la réparation la plus courante - soit un travail de routine pour un mécanicien expérimenté, l'importance des plaquettes pour la sécurité de fonctionnement d'un véhicule signifie qu'il y a peu de place pour l'erreur. Que vous soyez novice en matière d'installation de plaquettes de frein ou que vous ayez besoin d'une remise à niveau sur la manière de procéder, voici un aperçu de Ferodo® des quatre étapes fondamentales nécessaires au remplacement réussi des composants les plus sollicités d'un véhicule. Sélectionnez les bonnes plaquettes de rechange. S'il existe d'innombrables marques et variétés de plaquettes de frein, toutes ne se valent pas. Les meilleures marques, telles que Ferodo, bénéficient d'une expérience impressionnante en matière de performances et de fiabilité. En fait, Ferodo a récemment célébré son 125e anniversaire de leadership en matière de freinage. De plus, les plaquettes de frein de meilleure qualité sont livrées avec tout le matériel nécessaire pour effectuer le travail complet. Un autre conseil important est d'utiliser la même marque de disques et de plaquettes de frein pour garantir une compatibilité, des performances, une longévité et une facilité d'installation optimales.

- Préparez-vous correctement. Remplacer les plaquettes de frein n'est pas aussi simple que d'enlever les plaquettes usées et d'en installer de nouvelles. Avant l'installation, les étriers doivent être soigneusement inspectés et débarrassés de la saleté accumulée au cours de l'utilisation quotidienne. De plus, l'application d'une graisse de haute qualité et résistante à la température sur la butée des plaquettes de frein, les supports d'étriers et les plaques d'appui des nouvelles plaquettes peut contribuer à éliminer les bruits de freinage.

- Comprendre et prendre en compte les variations des différentes plaquettes. Comme c'est le cas pour de nombreux composants automobiles, différents véhicules nécessiteront différentes variétés de plaquettes de frein dotées de leur propre conception. Vous devez être conscient de ces variations lorsque vous choisissez les bonnes plaquettes de rechange.

- Comme c'est le cas pour de nombreux composants automobiles, différents véhicules nécessiteront différentes variétés de plaquettes de frein dotées de leur propre conception. Vous devez être conscient de ces variations lorsque vous choisissez les bonnes plaquettes de rechange.

Après le démontage, vérifiez et nettoyez les surfaces de montage des étriers de frein pour garantir un effort de glissement maximal de 3 à 4 kg.

![Cleaning 600x400](_raw/web-images/3be683d2192a491a.jpg)

Une petite quantité de graisse de frein spéciale résistante à la température peut être appliquée sur les composants suivants sur les composants suivants :

![pad disc caliper](_raw/web-images/53c4af651d491c0c.jpg)

Cela permet d'éliminer les bruits lors du freinage.

N'utilisez JAMAIS de graisse à base de cuivre pour les pièces du système de freinage, car elle pourrait provoquer une corrosion électrochimique et un collage à haute température.

![pad 600x331 transp](_raw/web-images/d337a742a9c0b29f.png)

Nous recommandons l'utilisation d'une pâte de montage sans cuivre à base de silicone à haute viscosité, contenant du graphite naturel pur (référence FGB068).

3a. Plaquettes de frein directionnelles

Certains systèmes de freinage utilisent désormais des plaquettes de frein asymétriques, qui appliquent la plaquette de frein sur le disque selon un angle, afin de réduire de manière significative les vibrations et le bruit.

Ce type de plaquette peut présenter un chanfrein sur la surface de frottement ou une découpe dans la cale de réduction du bruit sur la plaque d'appui. Ces deux éléments doivent être positionnés sur l'étrier d'une manière spécifique pour garantir un montage correct.

Il est important que le marquage de la flèche sur la plaque arrière de la plaquette corresponde au sens de rotation du disque de frein. Si ces instructions ne sont pas respectées, des bruits peuvent apparaître.

![Installation directional brake pads](_raw/web-images/f9ee15b357c46dbf.jpg)

3b. Plaquettes de frein avec rivets sur la plaque arrière

Certaines plaquettes contiennent des rivets sur la plaque arrière. Dans ce cas, ceux-ci doivent être montés dans la bonne position pour éviter un désalignement des plaquettes, ce qui peut générer des vibrations et du bruit.

![backplate rivets](_raw/web-images/3745b4e1faca929c.jpg)

La plaquette illustrée à gauche doit être montée du côté de la réaction du véhicule, identifié par les rivets (3) à angle droit avec les languettes de verrouillage (4). La plaquette illustrée à droite doit être monté du côté du piston. Cette plaquette est identifiée par les rivets (1) parallèles aux languettes de verrouillage (2).

3c. Comment retirer correctement le papier protecteur 3M

Si les plaquettes de frein sont fournies avec une feuille adhésive, seul le papier doit être retiré. Veuillez laisser la feuille adhésive sur la plaque arrière, car elle fixe la plaquette de frein à l'étrier et évite tout mouvement.

![backplate adhesive 600x355](_raw/web-images/1d81cb3950fc1be3.jpg)

Les ressorts limitent les mouvements et les vibrations si un mastic de blocage est appliqué sur les boulons de l'étrier, ce qui protège le boulon contre le desserrage et vous aide à éviter de serrer les boulons avec un couple excessif. Cela permet un maintien sûr, réduisant le risque de bruit et de vibration des freins.

Vérifiez l'aspect des accessoires de montage supplémentaires (tels que les dispositifs de retenue, les cales anti-bruit, etc.) - s'il y a des signes de déformation, de corrosion ou de dommage, il faut les remplacer.

![bolts and springs](_raw/web-images/03ca04a9cdd1822e.jpg)

Fixez les boulons de l'étrier et de la roue avec le couple de serrage recommandé par le constructeur du véhicule (le couple de serrage du boulon de l'étrier est souvent de 30 Nm, et celui des boulons/écrous de la roue d'environ 110 Nm). Respectez toujours les spécifications du constructeur automobile en ce qui concerne le couple de serrage recommandé.

N'utilisez JAMAIS de clé à chocs pneumatique ni de lubrifiant pour filetage lorsque vous serrez des boulons/écrous. Nous recommandons d'utiliser un outil à air comprimé doux, puis une clé dynamométrique pour serrer les boulons/écrous de roue.

![Tools](_raw/web-images/6c2261eeb971c7eb.jpg)

- par mesure de sécurité avant de prendre la route, vérifier la course de la pédale de frein et sa dureté lorsqu'elle est enfoncée.

- premier rodage : en respectant toutes les mesures de sécurité nécessaires, effectuer 20 freinages de 80 à 30 km/h avec une pression légère ou modérée sur la pédale. IMPORTANT : l'intervalle entre les freinages doit être d'au moins 30 secondes, afin de ne pas surchauffer les freins !

- Pendant les 200-300 premiers kilomètres, évitez les freinages brusques, les freinages à grande vitesse, ainsi que sur une voiture surchargée.

Nous recommandons vivement d'utiliser des plaquettes et des disques de frein de la même marque afin de garantir une compatibilité totale.

Vérifiez l

[...]
