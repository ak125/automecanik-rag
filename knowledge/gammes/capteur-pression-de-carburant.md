---
category: capteurs
slug: capteur-pression-de-carburant
title: Capteur pression de carburant
pg_id: 817
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
  role: Mesurer la pression du carburant dans la rampe d'injection et transmettre l'information au calculateur
  must_be_true:
  - mesurer
  - detecter
  - transmettre
  must_not_contain:
  - pompe
  - injecteur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - alternateur
  - batterie
  - demarreur
  - bougie-d-allumage
  - bobine-d-allumage
  - poulie-d-alternateur
  confusion_with:
  - term: piece-electrique-voisine
    difference: Les pieces electriques ont des connecteurs specifiques. Verifier le nombre de broches et le voltage.
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
  - ❌ "corrige la panne"
  cost_range:
    min: 40
    max: 150
    currency: EUR
    unit: capteur
    source: catalogue automecanik
  brands:
    premium:
    - Bosch
    - Valeo
    - Denso
    standard:
    - Hella
    - NGK
    - Delphi
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Perte de puissance a l acceleration
    severity: confort
  - id: S2
    label: A-coups ou hesitations du moteur
    severity: confort
  - id: S3
    label: Cliquetis cognement moteur injection defaillante
    severity: confort
  - id: S4
    label: Voyant moteur avec codes p0190-p0194
    severity: confort
  - id: S5
    label: Odeur carburant anormale fuite mauvaise
    severity: confort
  - id: S6
    label: Plus de 150 000 km sur moteur diesel hdi tdi
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - identifier origine fuite et verifier joints
  - remplacement preventif recommande
  quick_checks:
  - 'Observer : perte de puissance a l acceleration ?'
  - 'Observer : a-coups ou hesitations du moteur ?'
  - 'Observer : cliquetis cognement moteur injection defaillante ?'
  - Voyant moteur avec codes p0190-p0194 ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Perte de puissance a l acceleration
  - A-coups ou hesitations du moteur
  - Cliquetis cognement moteur injection defaillante
  - Voyant moteur avec codes p0190-p0194
  - Odeur carburant anormale fuite mauvaise
  - Plus de 150 000 km sur moteur diesel hdi tdi
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '817'
  intro_title: A quoi sert Capteur pression de carburant ?
  risk_title: Pourquoi remplacer Capteur pression de carburant a temps ?
  risk_explanation: '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
  risk_consequences:
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
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
  - question: Capteur pression carburant OE ou adaptable ?
    answer: Privilégiez l'OE ou OES (Bosch, Delphi, Denso) pour les systèmes haute pression diesel. Les adaptables sont risqués
      sur rampe common rail.
  - question: Comment savoir si mon capteur de pression carburant est HS ?
    answer: Perte de puissance, à-coups, démarrage difficile, voyant moteur avec codes P0190 à P0194, fumée noire ou blanche.
  - question: Tous les combien changer le capteur de pression carburant ?
    answer: Pas de périodicité. Durée de vie variable selon qualité du carburant. Peut durer 200 000+ km ou moins si carburant
      de mauvaise qualité.
  - question: Peut-on changer le capteur de pression carburant soi-même ?
    answer: 'Possible mais attention : système sous haute pression (diesel). Dépressuriser avant intervention. Joint neuf
      obligatoire.'
  - question: Quelle erreur éviter avec le capteur de pression carburant ?
    answer: Ne jamais réutiliser le joint. Respecter le couple de serrage. Ne pas confondre avec le régulateur de pression.
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
doc_id: 0ff788ec-f3b9-5277-9fc0-831d0193c308
content_hash: sha256:67409cc68aca2a70
lang: fr
variants:
- name: Piece neuve OE/OES
  aliases:
  - neuf
  - OE
  - OES
  functional_differences:
  - Garantie constructeur ou equipementier
  - Calibration d usine
- name: Piece echange standard
  aliases:
  - echange standard
  - reconditionne
  functional_differences:
  - Moins cher
  - Piece d origine reconditionnee
location_on_vehicle:
  area: Compartiment moteur (alternateur, demarreur) ou peripherie
  access: Par le dessus (capot) ou par le dessous selon modele
  adjacent_parts:
  - faisceau electrique
  - batterie
  - fusibles
installation:
  difficulty: facile a moyen
  time: 15min a 1h
  tools:
  - cle a douille
  - multimetre
  - tournevis
  prerequisite: Debrancher la batterie avant intervention
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'plein'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_0__: '0 %'
    val_000_v: '000 v'
    val_10__: '10 %'
    val_100__: '100 %'
    val_11__: '11 %'
    val_14_a: '14 a'
    val_15__: '15 %'
    val_18_a: '18 a'
    val_2_a: '2 a'
    val_20__: '20 %'
    val_23__: '23 %'
    val_23_a: '23 a'
    val_25__: '25 %'
    val_26_a: '26 a'
    val_30__: '30 %'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le capteur de pression de carburant est un composant d''instrumentation monté directement sur la rampe d''injection.
    Sa fonction est de mesurer en temps réel la pression du carburant dans la rampe et de transmettre cette valeur au calculateur
    moteur, qui ajuste en permanence la durée d''injection et le débit de la pompe haute pression en conséquence. Sur les
    moteurs diesel à injection directe Common Rail, la pression dans la rampe varie typiquement entre 200 et 2 000 bars selon
    le régime moteur et la charge. Le capteur doit détecter ces variations avec une précision de l''ordre de 1 à 2 % sur toute
    la plage de fonctionnement. Un capteur qui dérive de cette précision provoque une gestion moteur incorrecte : trop peu
    de pression entraîne une combustion incomplète (fumée noire), trop de pression risque d''endommager les injecteurs. Sur
    les moteurs essence à injection directe (GDI, FSI, TSI), le principe est identique avec des niveaux de pression inférieurs
    (50 à 350 bars). Le capteur transmet une tension proportionnelle à la pression mesurée — généralement entre 0,5 V et 4,5
    V. Le calculateur utilise cette valeur pour détecter toute anomalie dans le circuit carburant : fuite, pompe défaillante,
    injecteur qui ne se ferme pas correctement. Les pièces associées à vérifier lors du remplacement sont la pompe à carburant
    haute pression et la pompe à injection, car une pression anormale peut être causée par l''une ou l''autre plutôt que par
    le capteur lui-même.'
  S2: 'La défaillance du capteur de pression de carburant se traduit par des symptômes moteur caractéristiques, car le calculateur
    ne dispose plus d''une référence fiable pour piloter l''injection. Les symptômes peuvent être progressifs (dérive de mesure)
    ou brutaux (rupture du circuit électrique). Sur les moteurs diesel HDi, TDi et CDTi, ce composant est particulièrement
    sollicité au-delà de 150 000 km. - Perte de puissance à l''accélération : le calculateur réduit l''injection faute d''information
    fiable sur la pression dans la rampe, provoquant une accélération molle et un manque de couple dès les régimes moyens.
    - À-coups ou hésitations du moteur : le moteur tressaille ou hésite lors des accélérations, signe que la pression mesurée
    oscille autour d''une valeur incohérente, perturbant la durée d''injection à chaque cycle. - Cliquetis ou cognement moteur
    par injection défaillante : une pression mal mesurée peut entraîner une injection trop précoce ou trop tardive, générant
    des cliquetis caractéristiques dans le bloc moteur. - Voyant moteur allumé avec codes P0190 à P0194 : ces codes OBD indiquent
    directement un défaut sur le circuit du capteur de pression carburant ou une pression hors plage admissible. - Odeur de
    carburant anormale ou fuite : un capteur dont le joint est dégradé peut laisser fuir du carburant au niveau de son filetage
    sur la rampe d''injection, situation à traiter en urgence. - Au-delà de 150 000 km sur moteur diesel HDi ou TDi : le remplacement
    préventif du capteur est recommandé lors de révisions majeures sur ces motorisations, car la haute pression accélère l''usure
    de l''élément sensible.'
  S3: 'Le capteur de pression de carburant est une pièce de haute précision dont la compatibilité est critique. Une référence
    inadaptée peut délivrer des mesures erronées qui conduisent le calculateur à piloter l''injection hors des paramètres
    optimaux, sans déclencher de code défaut immédiat. Voici les critères à valider avant de commander. - Marque, modèle et
    motorisation exacte : la plage de pression mesurée varie selon le type d''injection (Common Rail diesel 200–2000 bar,
    injection directe essence 50–350 bar). Un capteur diesel monté sur un moteur essence ou inversement est incompatible.
    - Année de mise en circulation : les motorisations Diesel HDi et TDi ont évolué entre les générations avec des pressions
    nominales différentes nécessitant des capteurs spécifiques. - Vérifier les codes P0190 à P0194 : un diagnostic OBD avant
    commande confirme que c''est bien le capteur qui est en cause et non la pompe haute pression ou un injecteur défaillant.
    - Préférer les marques OE ou OES : Bosch, Delphi et Denso fabriquent ces capteurs pour les constructeurs. Sur les systèmes
    Common Rail haute pression, les capteurs génériques présentent des risques de dérive de mesure qui peuvent conduire à
    une sur-injection endommageant les injecteurs. - Vérifier l''état du joint de montage : le joint du capteur sur la rampe
    haute pression ne doit jamais être réutilisé. La pièce neuve doit impérativement être montée avec un joint neuf pour assurer
    l''étanchéité sous haute pression. - Ne pas confondre avec le régulateur de pression : le capteur mesure la pression mais
    ne la régule pas. Ces deux composants sont souvent proches sur la rampe et peuvent se confondre à l''œil. Vérifier la
    référence exacte de chaque pièce avant d''intervenir. Pour aller plus loin : consultez notre guide d''achat capteur pression
    de carburant — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 'Le remplacement du capteur de pression de carburant requiert une précaution majeure : le circuit d''injection
    est sous très haute pression (jusqu''à 2 000 bars sur les Common Rail diesel). Une dépressurisation impérative du système
    avant toute intervention est nécessaire. Cette opération est accessible à un mécanicien expérimenté mais déconseillée
    aux novices sur les moteurs haute pression diesel. - Lire les codes défaut OBD (P0190–P0194) et noter les données live
    de pression carburant pour confirmer la défaillance du capteur avant d''intervenir. - Dépressuriser le système d''injection
    : couper le contact et attendre au minimum 2 minutes pour que la pression chute. Sur certains véhicules, retirer le fusible
    de la pompe à carburant et faire tourner le démarreur 3 secondes sans carburant accélère la dépressurisation. - Laisser
    refroidir le moteur : attendre 30 minutes minimum. Le compartiment moteur et la rampe d''injection sont très chauds après
    utilisation et le carburant chaud augmente les risques de projection. - Protéger la zone de travail : placer des chiffons
    absorbants sous et autour de la rampe d''injection pour récupérer le carburant résiduel qui s''écoulera lors du démontage
    du capteur. - Débrancher le connecteur électrique du capteur en appuyant sur le clip de déverrouillage. Ne jamais tirer
    sur les fils. - Dévisser le capteur avec la clé adaptée (généralement une clé de 22 à 27 mm). Desserrer lentement pour
    laisser le carburant résiduel s''écouler progressivement. Mettre un chiffon autour pour absorber. - Inspecter le siège
    de montage sur la rampe : vérifier l''absence de dépôts ou de trace de fuite au niveau du filetage. - Monter le nouveau
    capteur avec un joint neuf : ne jamais réutiliser l''ancien joint. Respecter le couple de serrage constructeur (typiquement
    20 à 35 Nm selon le modèle). - Rebrancher le connecteur, rétablir le fusible si retiré, démarrer le moteur et inspecter
    immédiatement l''étanchéité du montage. Effacer les codes défaut OBD.'
  S4_REPOSE: 'Le remontage du capteur de pression de carburant est aussi exigeant que sa dépose. Le respect du couple de serrage
    et l''étanchéité du joint neuf sont les deux points critiques qui conditionnent la fiabilité du montage sur une rampe
    Common Rail pouvant atteindre 2 000 bars. - Inspecter le siège de montage sur la rampe : avant de monter le nouveau capteur,
    vérifier l''état du filetage femelle sur la rampe d''injection. Nettoyer délicatement tout dépôt carboné ou résidu d''ancien
    joint avec un chiffon propre. Ne pas utiliser d''outil métallique qui risque d''endommager le filetage. - Préparer le
    joint neuf : ne jamais réutiliser l''ancien joint, même s''il semble en bon état. Le joint neuf doit être celui fourni
    avec le nouveau capteur ou correspondre exactement à la référence constructeur. Appliquer une légère couche d''huile moteur
    sur le joint pour faciliter le montage. - Visser le capteur à la main en premier lieu : engager le filetage à la main
    pour éviter tout risque de faux-filetage, qui serait catastrophique sur une rampe d''injection. Tourner sans outil jusqu''à
    sentir la résistance du joint. - Serrer au couple constructeur avec une clé dynamométrique : respecter impérativement
    la valeur de serrage constructeur, généralement comprise entre 20 et 35 N·m selon le véhicule. Sous-serrer provoque une
    fuite, sur- serrer détériore le filetage de la rampe. - Rebrancher le connecteur électrique : enclencher le connecteur
    jusqu''au clic de verrouillage. S''assurer que le câble n''est pas en tension ni au contact de pièces chaudes ou mobiles.
    - Rétablir le fusible de la pompe à carburant si celui-ci avait été retiré pour la procédure de dépressurisation. - Remettre
    en pression progressivement : rebrancher la batterie, mettre le contact sans démarrer pendant 10 secondes (la pompe de
    gavage remonte la pression), puis répéter 2 fois. Ce cycle progressif permet à la rampe de monter en pression sans à-coup.
    - Démarrer et inspecter immédiatement l''étanchéité : avec un miroir ou une lampe, vérifier l''absence de toute trace
    de carburant autour du capteur et de la rampe. Même une micro-fuite sur un circuit haute pression est inacceptable en
    raison du risque incendie. - Effacer les codes défaut OBD (P0190–P0194) et effectuer une montée en charge progressive
    pour valider les données live de pression retournées par le nouveau capteur. La valeur de pression doit correspondre aux
    spécifications constructeur à régime stabilisé.'
  S5: 'Le remplacement du capteur de pression de carburant sur un moteur à injection haute pression concentre plusieurs erreurs
    techniques aux conséquences potentiellement graves. Ces erreurs sont documentées par les techniciens et peuvent être évitées
    avec une méthode rigoureuse. - Réutiliser l''ancien joint de montage : le joint du capteur sur la rampe haute pression
    est soumis à des pressions extrêmes. Un joint comprimé une première fois perd son élasticité et ne garantit plus l''étanchéité
    après remontage. Une fuite de carburant sur une rampe Common Rail à 2 000 bars est un risque d''incendie immédiat. - Ne
    pas respecter le couple de serrage : un serrage insuffisant provoque une fuite de carburant sous pression, un serrage
    excessif abîme le filetage de la rampe d''injection. Le remplacement d''une rampe Common Rail endommagée coûte plusieurs
    centaines d''euros. - Confondre le capteur de pression avec le régulateur de pression : ces deux pièces sont physiquement
    proches sur la rampe et peuvent se ressembler. Démonter le mauvais composant sans avoir vérifié la référence exacte conduit
    à une panne non résolue et à une dépense inutile. - Intervenir sans dépressuriser le circuit : travailler sur un circuit
    encore sous pression expose à une projection de carburant à haute vitesse lors du desserrage du capteur, avec risque de
    brûlures et d''incendie. - Ne pas vérifier l''état de la pompe haute pression : si le capteur signalait une pression insuffisante,
    la pompe peut être la cause réelle du problème. Changer le capteur sans diagnostiquer la pompe ne résout pas une pression
    chroniquement basse dans la rampe.'
  S6: 'Après le montage du nouveau capteur de pression de carburant, les vérifications sont critiques en raison des pressions
    en jeu. Une fuite de carburant non détectée immédiatement représente un risque sérieux. - Contrôle d''étanchéité immédiat
    au démarrage : dès le premier démarrage, inspecter visuellement et olfactivement la zone du capteur. La moindre odeur
    de carburant ou trace d''humidité autour du capteur impose l''arrêt immédiat du moteur. - Lecture des données live avec
    un outil OBD : vérifier que la pression mesurée correspond aux valeurs constructeur à différents régimes moteur (ralenti,
    mi-charge, pleine charge). La pression au ralenti doit être stable sans oscillations. - Effacement des codes P0190–P0194
    et vérification que le voyant moteur s''éteint définitivement après un cycle de conduite complet (moteur chaud, différents
    régimes). - Test en conditions réelles : effectuer un trajet d''au moins 15 km incluant des accélérations franches pour
    solliciter le système à haute pression et confirmer l''absence de à-coups ou de perte de puissance. - Vérification du
    couple de serrage après refroidissement : sur les moteurs très sollicités thermiquement, un contrôle du couple du capteur
    après le premier cycle thermique garantit que le serrage est resté conforme.'
  S7: 'Le capteur de pression de carburant s''inscrit dans un circuit d''injection haute pression dont plusieurs composants
    méritent vérification lors de la même intervention pour limiter les risques de repanne rapide. - Pompe à carburant (basse
    pression) : la pompe de gavage dans le réservoir alimente la pompe haute pression. Si sa pression de refoulement est insuffisante,
    le capteur de pression rampe enregistrera des valeurs basses même après son remplacement. Vérifier la pression d''alimentation
    basse pression avant de conclure à un défaut capteur. - Pompe à injection haute pression : la pompe HP est en amont du
    capteur. Une pompe usée ne maintient pas la pression correcte et donne des codes défaut similaires à un capteur HS. À
    contrôler si le capteur neuf ne résout pas les codes P0190–P0194. - Rampe d''injection (rail common rail) : le rail stocke
    le carburant sous haute pression. Des micro-fissures ou un régulateur de pression défaillant intégré au rail peuvent provoquer
    les mêmes symptômes qu''un capteur défaillant. - Régulateur de pression de carburant : ce composant distinct du capteur
    régule la pression dans la rampe. Si le régulateur est encrassé ou HS, la pression varie de façon erratique indépendamment
    du capteur. - Joints de raccords et O-rings : lors d''une intervention sur la rampe d''injection, remplacer systématiquement
    tous les joints de raccords démontés. Aucun joint haute pression ne doit être réutilisé après dépose.'
  S8: 'Capteur pression carburant OE ou adaptable : lequel choisir ? Sur les systèmes Common Rail haute pression diesel (HDi,
    TDi, CDTi), privilégier impérativement les marques OE ou OES comme Bosch, Delphi ou Denso. Ces capteurs sont étalonnés
    avec une précision de mesure conforme aux exigences constructeur. Les capteurs génériques présentent des risques de dérive
    de mesure qui peuvent conduire le calculateur à piloter l''injection en dehors des paramètres optimaux, sans déclencher
    immédiatement de code défaut — un problème difficile à diagnostiquer par la suite. Sur les moteurs essence injection directe,
    la tolérance est légèrement plus grande mais le principe reste identique. Comment confirmer que c''est le capteur et non
    la pompe haute pression ? Un outil de diagnostic avec lecture des données live est indispensable. Si la pression cible
    demandée par l''ECU est atteinte (ex : 1 500 bars demandés, 1 500 bars mesurés) mais que des codes P0190–P0194 sont présents,
    le capteur est suspect. Si la pression mesurée est chroniquement inférieure à la pression cible quelle que soit la charge
    moteur, la pompe haute pression ou le régulateur de débit est en cause. Un technicien peut également mesurer la tension
    de sortie du capteur au multimètre pour confirmer sa cohérence. Faut-il une périodicité d''entretien pour le capteur de
    pression carburant ? Pas de périodicité fixe. Le capteur peut dépasser 200 000 km sur un moteur bien entretenu et alimenté
    en carburant de qualité. En revanche, un carburant contaminé ou de mauvaise qualité accélère l''usure de l''élément sensible.
    Le remplacement préventif est recommandé sur les moteurs diesel HDi et TDi lors des grandes révisions au-delà de 150 000
    km, en même temps que les injecteurs si ceux-ci sont remplacés. Peut-on changer le capteur de pression carburant soi-même
    ? Possible sur les moteurs essence à injection directe avec précautions standard. Sur les moteurs diesel Common Rail,
    l''opération est déconseillée aux novices en raison des pressions extrêmes. Il faut obligatoirement dépressuriser le système
    avant tout démontage. Un joint neuf est impératif. Le couple de serrage doit être respecté à la clé dynamométrique. En
    cas de doute sur la procédure de dépressurisation de votre moteur, préférer l''atelier. Que faire si une fuite apparaît
    après remplacement du capteur ? Arrêter immédiatement le moteur — toute fuite de carburant sur un circuit sous haute pression
    est un risque d''incendie. Desserrer le capteur à froid, remplacer le joint (même s''il était neuf, un mauvais serrage
    peut l''avoir écrasé de façon incorrecte), et remonter en respectant scrupuleusement le couple constructeur à la clé dynamométrique.
    Ne jamais tenter de resserrer un capteur sur moteur chaud ou circuit sous pression.'
---

# Capteur pression de carburant - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la pression du carburant dans la rampe d'injection et transmettre l'information au calculateur

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- perte de puissance a l acceleration
- a-coups ou hesitations du moteur
- cliquetis cognement moteur injection defaillante
- voyant moteur avec codes p0190-p0194
- odeur carburant anormale fuite mauvaise
- plus de 150 000 km sur moteur diesel hdi tdi

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur pression de carburant:

1. **Inspection visuelle** - Examiner l'état du capteur pression de carburant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- pompe-a-carburant
- pompe-a-injection

## Critères de Compatibilité

Pour commander le bon capteur pression de carburant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "corrige la panne"

## FAQ

**Capteur pression carburant OE ou adaptable ?**
Privilégiez l'OE ou OES (Bosch, Delphi, Denso) pour les systèmes haute pression diesel. Les adaptables sont risqués sur rampe common rail.

**Comment savoir si mon capteur de pression carburant est HS ?**
Perte de puissance, à-coups, démarrage difficile, voyant moteur avec codes P0190 à P0194, fumée noire ou blanche.

**Tous les combien changer le capteur de pression carburant ?**
Pas de périodicité. Durée de vie variable selon qualité du carburant. Peut durer 200 000+ km ou moins si carburant de mauvaise qualité.

**Peut-on changer le capteur de pression carburant soi-même ?**
Possible mais attention : système sous haute pression (diesel). Dépressuriser avant intervention. Joint neuf obligatoire.

**Quelle erreur éviter avec le capteur de pression carburant ?**
Ne jamais réutiliser le joint. Respecter le couple de serrage. Ne pas confondre avec le régulateur de pression.


## References supplementaires

<!-- materialized-from-db manual/ec88a4276f29 2026-04-03 -->
### Données techniques OEM — Capteur pression de carburant

# Données techniques OEM — Capteur pression de carburant
Source : fr.wikipedia.org (1 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- plein
- électrique

## Valeurs techniques de référence
- 0 %
- 10 %
- 100 %
- 11 %
- 15 %
- 20 %
- 23 %
- 25 %
- 30 %
