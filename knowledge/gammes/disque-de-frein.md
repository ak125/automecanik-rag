---
category: freinage
slug: disque-de-frein
title: Disque de frein
pg_id: 82
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-04-04'
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
  last_enriched_by: script:materialize-db-to-md
  last_enriched_at: '2026-04-04'
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
  _source: aftermarket.zf.com + ate-freinage.fr + bremboparts.com + delphiautoparts.com + ferodo.com + gpa26.com + hella.com
    + profauto.fr + textar.com + valeoservice.fr
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 89
  _has_tech_data: true
  types_variants:
  - type: Composite
    source_ref: corpus RAG web OEM
  - type: bi-matière
    source_ref: corpus RAG web OEM
  - type: composite
    source_ref: corpus RAG web OEM
  - type: céramique
    source_ref: corpus RAG web OEM
  - type: perforé
    source_ref: corpus RAG web OEM
  - type: plein
    source_ref: corpus RAG web OEM
  - type: rainuré
    source_ref: corpus RAG web OEM
  - type: ventilé
    source_ref: corpus RAG web OEM
  technical_notes:
    norme_ece_r90: ECE R90
    norme_sae_j2521: SAE J2521
    val_0_035_mm: 0,035 mm
    val_0_05_mm: 0,05 mm
    val_0_050_mm: 0,050 mm
    val_0_1_mm: 0,1 mm
    val_0_10_mm: 0,10 mm
    val_0_12_mm: 0,12 mm
    val_000_km: 000 km
    val_1_5_mm: 1,5 mm
    val_10__m: 10 µm
    val_10__v: 10. V
    val_100__: 100 %
    val_100_a: 100 a
    val_11_a: 11 a
    val_110_nm: 110 Nm
    val_115_nm: 115 Nm
  materials:
  - materiau: ALUMINIUM
    source_ref: corpus RAG web OEM
  - materiau: acier inox
    source_ref: corpus RAG web OEM
  - materiau: aluminium
    source_ref: corpus RAG web OEM
  - materiau: carbone-céramique
    source_ref: corpus RAG web OEM
  - materiau: céramique
    source_ref: corpus RAG web OEM
  - materiau: fonte grise
    source_ref: corpus RAG web OEM
  - materiau: graphite
    source_ref: corpus RAG web OEM
  - materiau: silicone
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
