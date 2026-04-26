---
category: refroidissement
slug: capteur-niveau-de-liquide-de-refroidissement
title: Capteur niveau de liquide de refroidissement
pg_id: 1288
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
  role: Detecter le niveau de liquide de refroidissement et alerter le conducteur en cas de niveau bas
  must_be_true:
  - detecter le niveau
  - liquide de refroidissement
  - alerter le conducteur
  must_not_contain:
  - universel
  - tous modeles
  - adaptable tous
  confusion_with:
  - term: sonde-de-refroidissement
    difference: La sonde mesure la temperature du liquide, le capteur de niveau detecte si le niveau est suffisant
  - term: bouchon-vase-expansion
    difference: Le bouchon assure la pression du circuit, le capteur mesure le niveau dans le vase
  related_parts:
  - vase-d-expansion
  - bouchon-vase-expansion
  - durite-de-refroidissement
  - sonde-de-refroidissement
selection:
  criteria:
  - Marque de votre vehicule
  - Modele de votre vehicule
  - Motorisation de votre vehicule
  - Annee de votre vehicule
  - Type de capteur (flotteur magnetique, thermistance, ultrason)
  anti_mistakes:
  - universel
  - tous modeles
  - adaptable tous
  brands:
    premium:
    - Behr/Mahle
    - Gates
    standard:
    - Valeo
    - NRF
    - Febi
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Voyant niveau liquide de refroidissement allume alors que le niveau est correct
    severity: confort
  - id: S2
    label: Pas d'alerte malgre un niveau bas reel
    severity: securite
  - id: S3
    label: Alerte intermittente en virage ou sur route bosselee
    severity: confort
  - id: S4
    label: Surchauffe moteur non detectee a temps
    severity: securite
  causes:
  - flotteur bloque par des depots de tartre ou de rouille
  - connecteur oxyde ou fil coupe
  - capteur thermistance defaillant (court-circuit ou circuit ouvert)
  depose_steps:
  - Laisser refroidir le moteur et ouvrir le bouchon du vase d'expansion pour depressuriser
  - Localiser le capteur de niveau sur le vase d'expansion (connecteur electrique visible)
  - Debrancher le connecteur electrique du capteur (languette de verrouillage)
  - Deposer le capteur par rotation (quart de tour) ou devisser selon le modele
  - Installer le nouveau capteur avec son joint neuf, reconnecter le connecteur
  - Completer le niveau de liquide de refroidissement si necessaire, purger le circuit
  quick_checks:
  - Voyant niveau liquide de refroidissement allume alors que le niveau est correct ?
  - 'Observer : pas d''alerte malgre un niveau bas reel ?'
  - 'Observer : alerte intermittente en virage ou sur route bosselee ?'
  - 'Observer : surchauffe moteur non detectee a temps ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Verifier le bon fonctionnement du voyant a chaque vidange de liquide de refroidissement.
  wear_signs:
  - Voyant niveau liquide de refroidissement allume alors que le niveau est correct
  - Pas d'alerte malgre un niveau bas reel
  - Alerte intermittente en virage ou sur route bosselee
  - Surchauffe moteur non detectee a temps
  good_practices:
  - Controle du niveau de liquide de refroidissement a froid chaque mois
  - Remplacement du liquide selon preconisation constructeur (2-5 ans)
  - Verification des durites et colliers a chaque revision
  - Purge du circuit apres toute intervention sur le refroidissement
rendering:
  pgId: '1288'
  faq:
  - question: Comment tester le capteur niveau LDR ?
    answer: Debrancher le connecteur, le voyant doit s'allumer (alerte niveau bas). Si non, verifier le faisceau et le capteur.
  - question: Capteur OE ou adaptable ?
    answer: Privilegier OE pour la fiabilite. Le capteur de niveau est une piece de securite.
  - question: Peut-on rouler avec un capteur defaillant ?
    answer: Oui mais sans alerte en cas de fuite, risque de surchauffe moteur non detectee. Verifier le niveau manuellement.
  - question: Tous les combien changer ?
    answer: Pas de periodicite. Remplacer si le voyant reste allume malgre un niveau correct ou si pas d'alerte malgre niveau
      bas.
  - question: Quelle erreur eviter ?
    answer: Ne pas oublier de purger le circuit de refroidissement apres intervention sur le vase d'expansion.
  quality:
    score: 60
    source: manual:claude-r3-kp
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modeles
  - adaptable tous
  requires_vehicle: true
doc_id: 58c757e2-3740-5935-976f-3eb4b9219f1e
content_hash: sha256:4f1849d5ca7ecc25
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
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: Hall
    source_ref: corpus RAG web OEM
  - type: inductif
    source_ref: corpus RAG web OEM
  - type: pneumatique
    source_ref: corpus RAG web OEM
  - type: électrique
    source_ref: corpus RAG web OEM
  technical_notes:
    val_0_v: 0 V
    val_0_1__: 0,1 %
    val_1_5__: 1,5 %
    val_14__: 14 %
    val_4_5__: 4,5 %
    val_400__c: 400 °C
    val_5_v: 5 V
  materials:
  - materiau: aluminium
    source_ref: corpus RAG web OEM
  - materiau: platine
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: Le capteur niveau de liquide de refroidissement est situé auniveau du vase d'expansion, il va mesurer le niveau de liquide
    derefroidissement dans le vase et cette information va être envoyée aucalculateur. Le calculateur moteur va afficher la
    mesure sur le tableau bordpour informer le conducteur du niveau de liquide de refroidissement. En cas debaisse de niveau
    de liquide de refroidissement un message d'alerte va être affiché ou l'allumage le témoinde niveau (suivant le niveau
    d'équipement duvéhicule) sur le tableau de bord (couleur rouge). En cas d'alerte de baisse de niveau il faut obligatoirement
    contrôlerle liquide de refroidissement et le corrigé si nécessaire.
  S2: 'Verifier le bon fonctionnement du voyant a chaque vidange de liquide de refroidissement. Symptômes d''usure : - Voyant
    niveau liquide de refroidissement allume alors que le niveau est correct - Pas d''alerte malgre un niveau bas reel - Alerte
    intermittente en virage ou sur route bosselee - Surchauffe moteur non detectee a temps'
  S3: 'Pour choisir les bons capteur niveau de liquide de refroidissement pour votre véhicule : - Marque de votre vehicule
    - Modele de votre vehicule - Motorisation de votre vehicule - Annee de votre vehicule - Type de capteur (flotteur magnetique,
    thermistance, ultrason)'
  S4_DEPOSE: 1. Laisser refroidir le moteur et ouvrir le bouchon du vase d'expansion pour depressuriser 2. Localiser le capteur
    de niveau sur le vase d'expansion (connecteur electrique visible) 3. Debrancher le connecteur electrique du capteur (languette
    de verrouillage) 4. Deposer le capteur par rotation (quart de tour) ou devisser selon le modele 5. Installer le nouveau
    capteur avec son joint neuf, reconnecter le connecteur 6. Completer le niveau de liquide de refroidissement si necessaire,
    purger le circuit
  S4_REPOSE: '- Vérifiez que le capteur niveau de liquide de refroidissement neuf est identique à celui démonté. - Contrôlez
    l''état defonctionnement de la pompe à eau. - Contrôlez l''état de fonctionnement du thermostat. - Contrôlez l''état d''usure
    duradiateur de refroidissement. - Contrôlez l''état d''usuredes durites de liquide de refroidissement. - Contrôlez l''état
    d''usure duvase d''expansion. - On vous conseils de purgezet remplissez le liquide de refroidissement. - Mettre en place
    le capteurniveau de liquide de refroidissement. - Reconnectez le connecteurdu capteur niveau de liquide de refroidissement.
    - Rebranchez la batterie. - Contrôlez le bonfonctionnement du capteur niveau de liquide de refroidissement.'
  S6: 'Après la pose du capteur de niveau de liquide de refroidissement, plusieurs vérifications confirment l''étanchéité
    du montage et le bon fonctionnement de l''alerte avant que le véhicule ne reprenne la route. - Contrôle du niveau dans
    le vase d''expansion : vérifier que le liquide de refroidissement se situe entre les repères MIN et MAX du vase d''expansion,
    à froid. Un niveau correct est la condition préalable à tout test de fonctionnement du capteur. - Vérification de l''étanchéité
    à froid : immédiatement après la pose, inspecter visuellement le filetage ou le joint du capteur. Aucune trace humide
    ne doit être visible. Serrer si nécessaire, sans dépasser le couple préconisé (typiquement 4 à 8 N·m pour un capteur M12
    en plastique). - Test fonctionnel du circuit d''alerte : avec un outil de diagnostic, vérifier que la valeur lue par le
    calculateur correspond à « niveau correct » et non à une alerte. Sur les véhicules sans outil dédié, démarrer le moteur
    et observer que le témoin de niveau (rouge) s''éteint bien après quelques secondes si le niveau est correct. - Vérification
    après montée en température : laisser le moteur atteindre sa température normale de fonctionnement (environ 90°C). La
    pression dans le circuit augmente et peut révéler une fuite autour du capteur invisible à froid. Inspecter à nouveau le
    pourtour du capteur à chaud. - Contrôle de l''absence de codes défaut OBD : lire les DTC avec un outil de diagnostic.
    Les codes liés au capteur de niveau de liquide de refroidissement (P0117, P0118, P2183 selon constructeur) doivent être
    absents après effacement et cycle de conduite. - Vérification de la concentration en antigel : si du liquide a été ajouté
    pour compenser la perte, contrôler la concentration du mélange avec un réfractomètre. La teneur en glycol doit être entre
    40 et 60 % pour une protection entre -25°C et -40°C.'
  S_GARAGE: 'Nous vous recommandons de confier cette intervention à un professionnel : - Plusieurs causes possibles de défaillance
    (3 identifiées) nécessitent un diagnostic professionnel Un garagiste qualifié dispose de l''outillage et de l''expérience
    nécessaires pour effectuer cette opération en toute sécurité.'
  S7: '- vase d expansion - bouchon vase expansion - durite de refroidissement - sonde de refroidissement'
  S8: Comment tester le capteur niveau LDR ?Debrancher le connecteur, le voyant doit s'allumer (alerte niveau bas). Si non,
    verifier le faisceau et le capteur. Capteur OE ou adaptable ?Privilegier OE pour la fiabilite. Le capteur de niveau est
    une piece de securite. Peut-on rouler avec un capteur defaillant ?Oui mais sans alerte en cas de fuite, risque de surchauffe
    moteur non detectee. Verifier le niveau manuellement. Tous les combien changer ?Pas de periodicite. Remplacer si le voyant
    reste allume malgre un niveau correct ou si pas d'alerte malgre niveau bas. Quelle erreur eviter ?Ne pas oublier de purger
    le circuit de refroidissement apres intervention sur le vase d'expansion.
---

# Capteur niveau de liquide de refroidissement - Guide Diagnostic

## Fonction et Role

Detecter le niveau de liquide de refroidissement et alerter en cas de niveau bas.

## Symptomes de Defaillance

- Voyant allume malgre niveau correct
- Pas d'alerte malgre niveau bas reel
- Alerte intermittente en virage
- Surchauffe non detectee

## Pieces Associees

- vase-d-expansion
- bouchon-vase-expansion
- durite-de-refroidissement
- sonde-de-refroidissement

## FAQ

**Comment tester le capteur niveau LDR ?**
Debrancher le connecteur, le voyant doit s'allumer (alerte niveau bas). Si non, verifier le faisceau et le capteur.

**Capteur OE ou adaptable ?**
Privilegier OE pour la fiabilite. Le capteur de niveau est une piece de securite.

**Peut-on rouler avec un capteur defaillant ?**
Oui mais sans alerte en cas de fuite, risque de surchauffe moteur non detectee. Verifier le niveau manuellement.

**Tous les combien changer ?**
Pas de periodicite. Remplacer si le voyant reste allume malgre un niveau correct ou si pas d'alerte malgre niveau bas.

**Quelle erreur eviter ?**
Ne pas oublier de purger le circuit de refroidissement apres intervention sur le vase d'expansion.

## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Verifier le bon fonctionnement du voyant a chaque vidange de liquide de refroidissement.
