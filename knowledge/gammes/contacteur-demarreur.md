---
category: electrique
slug: contacteur-demarreur
title: Contacteur démarreur
pg_id: 682
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
  role: Commuter le circuit electrique du demarreur
  must_be_true:
  - commuter
  - activer
  - alimenter
  must_not_contain:
  - injection
  - climatisation
  - freinage
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
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de electrique
    pour confirmer Contacteur démarreur.
  - Verifier la reference OE ou equivalence constructeur pour le vehicule exact
  - Controler la compatibilite des connecteurs et du voltage (12V, 24V)
  - Choisir un equipementier specialise (Bosch, Valeo, Hella, Denso)
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "demarrage garanti"
  cost_range:
    min: 200
    max: 800
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Equipement d origine (OE)
  - tier: Equivalent OE
  - tier: Piece adaptable
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
    label: Aucune reaction a la cle de contact
    severity: confort
  - id: S2
    label: Demarrage intermittent
    severity: confort
  - id: S3
    label: Tableau de bord qui ne s allume pas
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'Usure ou defaillance causant : aucune reaction a la cle de contact'
  - 'Usure ou defaillance causant : demarrage intermittent'
  quick_checks:
  - 'Observer : aucune reaction a la cle de contact ?'
  - 'Observer : demarrage intermittent ?'
  - 'Observer : tableau de bord qui ne s allume pas ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Aucune reaction a la cle de contact
  - Demarrage intermittent
  - Tableau de bord qui ne s allume pas
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '682'
  intro_title: A quoi sert Contacteur démarreur ?
  risk_title: Pourquoi remplacer Contacteur démarreur a temps ?
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
  - question: Comment choisir Contacteur démarreur compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Contacteur démarreur ?
    answer: En cas de aucune reaction a la cle de contact ou de degradation mesurable, il faut controler rapidement avant
      panne secondaire.
  - question: Puis-je monter Contacteur démarreur sans verification atelier ?
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
doc_id: 29d2dc6c-64df-5637-8169-ae76f3ac2ee1
content_hash: sha256:eb676f800625305a
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
  - type: pneumatique
    source_ref: corpus RAG web OEM
  - type: électrique
    source_ref: corpus RAG web OEM
  technical_notes:
    val_100_a: 100 a
    val_15_km: 15 km
    val_90_km: 90 km
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le contacteur démarreur est le composant électrique qui établit et interrompt le circuit d''alimentation du démarreur
    lorsque le conducteur tourne la clé de contact ou appuie sur le bouton de démarrage. Il joue le rôle d''un relais de puissance
    commandé : il reçoit un signal de faible intensité en provenance du barillet de contact ou du module de démarrage, et
    commute en réponse un circuit de forte intensité vers le moteur de démarrage. Lors d''un démarrage, le démarreur consomme
    entre 80 et 300 ampères selon le type de moteur et les conditions de température. Ce courant élevé ne peut pas transiter
    directement par la clé de contact ou les fils du tableau de bord. Le contacteur démarreur — souvent appelé relais de démarreur
    ou solénoïde — est dimensionné pour commuter ces intensités élevées de façon fiable et répétée. Sur les véhicules modernes,
    la commande du contacteur passe souvent par le BSI (boîtier de servitude intelligent) ou le module anti-démarrage, ce
    qui rend le diagnostic plus complexe qu''un simple test de continuité. Les pièces à contrôler en parallèle lors d''une
    panne de démarrage sont le démarreur lui-même et la batterie, dont les défaillances produisent des symptômes similaires.'
  S2: 'Un contacteur démarreur défaillant produit des symptômes caractéristiques qui diffèrent des pannes de batterie ou de
    démarreur. L''identification précise de ces signaux évite de remplacer des pièces non défaillantes. - Aucune réaction
    à la clé de contact : tourner la clé ou appuyer sur le bouton ne produit aucun son, aucun clic, aucun mouvement. Le moteur
    de démarrage ne reçoit pas l''ordre de s''enclencher. Ce silence complet distingue une panne de contacteur d''une panne
    de démarreur (qui produit généralement un grincement ou un raclement). - Démarrage intermittent aléatoire : le véhicule
    démarre normalement certains jours et refuse de démarrer d''autres jours, sans logique apparente. Ce comportement aléatoire
    est typique d''un contacteur usé dont les contacts internes présentent des points de résistance variable. - Tableau de
    bord qui ne s''allume pas à la mise sur contact : si aucun voyant ne s''allume lors de la mise sur contact, le contacteur
    peut être défaillant au niveau du circuit de commande, empêchant l''alimentation générale du véhicule. - Clic unique sans
    démarrage : un clic fort à la mise sur contact suivi d''un silence indique que le contacteur s''engage mais que le démarreur
    ne suit pas. Ce symptôme peut aussi signaler une batterie trop faible ou un démarreur grippé. - Chaleur excessive au niveau
    du contacteur : un contacteur dont les contacts internes sont oxydés présente une résistance élevée qui génère de la chaleur.
    Un boîtier chaud ou une odeur de brûlé près du relais de démarrage est un signal d''alarme. - Démarrage uniquement après
    plusieurs tentatives rapprochées : le contacteur s''engage seulement après plusieurs sollicitations successives, signe
    que ses contacts ne font plus connexion au premier appel.'
  S3: 'Le contacteur démarreur est une pièce électrique critique dont la mauvaise sélection entraîne soit un non-fonctionnement
    immédiat, soit une destruction rapide par surcharge. Voici les critères indispensables pour choisir la bonne pièce. -
    Marque, modèle et année du véhicule : la référence du contacteur dépend directement du type de démarreur monté sur le
    véhicule, qui varie selon la version moteur et l''année de production. Un même modèle peut avoir reçu plusieurs démarreurs
    différents selon les millésimes. - Référence du démarreur associé : le contacteur est dimensionné pour un démarreur spécifique.
    Pour être certain de la compatibilité, relever la référence inscrite sur le corps du démarreur existant (généralement
    sur une étiquette ou un marquage en relief). - Intensité nominale de commutation : vérifier que le contacteur supporte
    l''intensité maximale appelée par le démarreur. Un contacteur sous-dimensionné en intensité surchauffe et fusionne prématurément.
    - Tension nominale : les véhicules légers fonctionnent en 12V, mais certains poids lourds et engins de chantier utilisent
    du 24V. La tension doit correspondre exactement au réseau de bord du véhicule. - Type de montage : séparé ou intégré au
    démarreur : sur certains démarreurs, le contacteur (solénoïde) est intégré dans le corps du démarreur et ne se remplace
    pas séparément. Dans ce cas, c''est l''ensemble démarreur qui doit être remplacé. Vérifier ce point avant toute commande.
    - Nombre de connexions électriques : compter les bornes du contacteur d''origine (2, 3 ou 4 bornes selon les véhicules)
    et s''assurer que la pièce de remplacement présente le même brochage. - Qualité des contacts internes : privilégier les
    contacteurs avec contacts en cuivre massif plutôt qu''en alliages bas de gamme. Un contact de qualité résiste mieux aux
    arcs électriques répétés du démarrage. Pour aller plus loin : consultez notre guide d''achat contacteur démarreur — comparatif
    marques, critères de choix et prix.'
  S4_DEPOSE: 'Le remplacement d''un contacteur démarreur est une intervention électrique qui nécessite des précautions contre
    les courts-circuits. La procédure varie selon que le contacteur est séparé du démarreur ou intégré sous forme de solénoïde.
    Voici la procédure générale pour un contacteur démarreur séparé. - Déconnexion obligatoire de la batterie : débrancher
    en premier le câble négatif de la batterie. Le démarreur est directement connecté au pôle positif par un câble de forte
    section sans fusible intermédiaire. Travailler sur ce circuit batterie connectée expose à un risque de court-circuit grave.
    - Localisation du contacteur démarreur : selon le véhicule, le contacteur peut se trouver dans le boîtier de fusibles
    ou de relais (habitacle ou compartiment moteur), directement sur le corps du démarreur, ou sur le circuit de démarrage.
    Consulter le schéma électrique du véhicule. - Repérage et débranchement des connecteurs : photographier ou noter la position
    de chaque fil connecté au contacteur avant de les débrancher. Sur les contacteurs à plusieurs bornes, l''ordre de reconnexion
    est critique pour le bon fonctionnement du circuit. - Dépose du contacteur défaillant : dévisser les vis ou déclipser
    les fixations maintenant le contacteur dans son support. Si le contacteur est fixé directement sur le démarreur, il peut
    être nécessaire de déposer d''abord le démarreur pour accéder aux vis du solénoïde. - Comparaison avec la pièce de remplacement
    : avant toute pose, vérifier que le nouveau contacteur est identique en termes de nombre de bornes, d''encombrement et
    de sens de montage. - Pose du nouveau contacteur : fixer mécaniquement le contacteur, puis reconnecter les fils dans l''ordre
    exact d''origine. Vérifier l''absence de fil pincé ou de connecteur mal enfoncé. - Reconnexion de la batterie et test
    fonctionnel : reconnecter le câble négatif de la batterie et tester le démarrage. Le moteur doit démarrer au premier appui
    sans clic parasite ni hésitation. - Lecture des codes défaut : sur les véhicules récents avec BSI, un code défaut peut
    s''être mémorisé lors de la panne. Effacer les codes à l''aide d''un outil de diagnostic après remplacement.'
  S4_REPOSE: 'Après la dépose du contacteur défaillant, la repose du nouveau contacteur démarreur suit un ordre précis pour
    éviter toute erreur de câblage sur ce circuit à courant fort. Voici les étapes de remontage : - Vérifier la conformité
    du nouveau contacteur avant toute pose : comparer physiquement le nouveau contacteur avec l''ancien : nombre de bornes,
    dimensions du corps, type de fixation (clips ou vis), sens d''entrée des fils. Un contacteur avec une borne en moins ou
    en plus ne peut pas être reposé sans risque de court- circuit. - Positionner et fixer mécaniquement le contacteur dans
    son support : engager le contacteur dans son logement (boîtier de relais, support sur démarreur ou support dédié) et serrer
    les vis de fixation sans excès. Le contacteur ne doit pas bouger une fois en place. - Reconnecter les fils dans l''ordre
    exact d''origine : se référer à la photographie prise avant la dépose. Chaque fil doit rejoindre exactement la même borne.
    Sur les contacteurs à solénoïde de démarreur, distinguer la borne petite section (commande, fil fin) de la borne grosse
    section (puissance, câble de batterie). - Vérifier l''absence de fil pincé ou de connecteur mal engagé : inspecter visuellement
    que chaque fil est correctement orienté et que les connecteurs à fiches sont bien verrouillés par leur clip. Un fil pincé
    dans un cache peut provoquer un court-circuit au remontage. - Remonter les caches et protections déposés : replacer le
    couvercle du boîtier de fusibles ou les protections moteur qui avaient été retirés pour accéder au contacteur. Vérifier
    que toutes les vis et clips sont en place. - Si le démarreur avait été déposé, le reposer et le fixer au couple constructeur
    : serrer les boulons de fixation du démarreur sur le carter d''embrayage ou le bloc moteur selon les valeurs de couple
    constructeur (généralement 25 à 45 N.m). - Reconnecter la borne négative de la batterie : rebrancher le câble masse en
    s''assurant que le contact est propre et exempt d''oxydation. Un mauvais contact de masse est une cause courante de dysfonctionnement
    après remplacement. - Tester le démarrage et l''absence de bruit parasite : actionner le contacteur de démarrage et vérifier
    que le démarreur s''engage franchement, tourne sans claquement et se désengage dès que le moteur a démarré. Répéter 3
    fois le test pour confirmer la fiabilité du démarrage. - Effacer les codes défaut avec un outil OBD : sur les véhicules
    récents équipés d''un BSI ou d''un module de gestion du réseau, effacer les codes défaut mémorisés lors de la panne. Vérifier
    qu''aucun nouveau code ne s''enregistre après les tests.'
  S5: 'Le circuit de démarrage est un des rares circuits automobiles alimentés directement depuis la batterie sans fusible
    de protection sur le câble principal. Les erreurs lors du remplacement du contacteur peuvent causer des courts-circuits
    avec dégagement de chaleur important. - Travailler batterie connectée : intervenir sur le circuit de démarrage sans déconnecter
    préalablement le câble négatif de la batterie expose à un court-circuit entre le câble positif de forte section et la
    masse. La déconnexion de la batterie est la première action à réaliser, sans exception. - Inverser les connexions au remontage
    : un contacteur à plusieurs bornes mal rebranché commande le démarreur en permanence ou ne le commande pas du tout. Photographier
    systématiquement le câblage d''origine avant toute dépose. - Commander un contacteur sans vérifier sa compatibilité avec
    le démarreur : un contacteur de dimension similaire mais destiné à un autre démarreur peut ne pas déclencher correctement,
    provoquer un accrochage du pignon ou une destruction rapide par surchauffe. - Remplacer le contacteur sans diagnostiquer
    la cause de la panne : un contacteur défaillant peut être la conséquence d''un problème de batterie (tension insuffisante
    qui surcharge le contacteur) ou d''un démarreur grippé (surintensité permanente qui brûle les contacts). Sans diagnostic
    complet, le nouveau contacteur subira le même sort. - Négliger le contrôle de la résistance des câbles : des câbles de
    démarrage corrodés ou de section insuffisante créent une chute de tension qui force le contacteur à travailler en permanence
    sous tension dégradée, accélérant son usure. Mesurer la résistance des câbles au multimètre avant de conclure à une panne
    de contacteur.'
  S6: 'Après la pose d''un nouveau contacteur démarreur, quelques vérifications électriques permettent de confirmer le bon
    fonctionnement du circuit et d''éviter une récidive rapide par une cause sous-jacente non détectée. - Test de démarrage
    à froid et à chaud : vérifier que le véhicule démarre au premier appui aussi bien moteur froid que moteur chaud. Certains
    contacteurs défectueux passent bien à froid mais présentent des ratés à chaud en raison de la dilatation thermique des
    contacts internes. - Mesure de la tension aux bornes du démarreur lors du démarrage : connecter un multimètre entre la
    borne positive du démarreur et la masse. La tension lors de la mise en route ne doit pas descendre en dessous de 9,5V.
    Une tension plus basse indique une batterie faible ou une résistance élevée dans les câbles ou le contacteur. - Contrôle
    de l''absence d''arc électrique ou de chaleur anormale : après quelques démarrages, palper prudemment le boîtier du contacteur.
    Un contacteur correctement dimensionné et câblé reste froid ou légèrement tiède. Un boîtier chaud signale un problème
    de câblage ou de dimensionnement. - Lecture et effacement des codes défaut BSI : sur les véhicules avec boîtier de servitude,
    vérifier l''absence de codes résiduels liés au circuit de démarrage après 3 à 5 cycles de démarrage normaux. - Vérification
    de l''état de charge de la batterie : tester la batterie au pèse-acide ou avec un testeur de batterie. Une batterie en
    fin de vie surcharge le contacteur à chaque démarrage et provoque son usure prématurée.'
  S7: 'Un contacteur démarreur défaillant est rarement isolé — plusieurs composants du circuit de démarrage doivent être contrôlés
    simultanément pour éviter une récidive ou une panne masquée : - Démarreur — moteur électrique actionné par le contacteur.
    Un démarreur usé (charbons, roue libre) peut provoquer les mêmes symptômes qu''un contacteur défaillant. Tester le démarreur
    sous charge avant de conclure à un contacteur seul. - Batterie — source d''énergie primaire du circuit de démarrage. Une
    batterie en fin de vie provoque des démarrages intermittents identiques à ceux d''un contacteur défaillant. Mesurer la
    tension à vide et sous charge avant de remplacer le contacteur. - Relais de démarrage — commande l''alimentation du contacteur.
    Un relais de démarrage défaillant bloque la commande du contacteur sans que le contacteur lui-même soit en cause. Tester
    le relais par substitution ou à l''ohmmètre. - Câble de masse moteur — le retour de courant du démarreur transite par
    ce câble. Un câble de masse oxydé ou desserré crée une chute de tension qui simule un contacteur défaillant. Contrôler
    la résistance du câble de masse moteur-châssis.'
  S8: 'Comment distinguer une panne de contacteur démarreur d''une panne de batterie ? Les deux pannes peuvent produire un
    symptôme similaire (véhicule qui ne démarre pas), mais se distinguent par des détails. Une batterie déchargée produit
    généralement un démarreur lent qui tourne mais sans élan suffisant, ou une série de clics rapides du relais de démarrage.
    Un contacteur défaillant produit soit un silence complet (aucun clic, aucun mouvement), soit un unique clic suivi d''un
    silence, les phares et le tableau de bord fonctionnant normalement. Mesurer la tension de batterie avec un multimètre
    (valeur cible : 12,4 à 12,7V à vide) permet de trancher rapidement. Peut-on tester un contacteur démarreur sans l''enlever
    du véhicule ? Oui. Avec un multimètre en position ohmmètre, mesurer la résistance des contacts principaux du contacteur
    lorsqu''il est commandé (demander à quelqu''un de tenir la clé sur démarrage pendant la mesure, ou court-circuiter brièvement
    la borne de commande). Un contacteur sain présente une résistance quasi nulle (inférieure à 0,1 ohm) sur ses contacts
    principaux lors de l''activation. Une résistance élevée confirme l''usure des contacts internes. Le contacteur démarreur
    se remplace-t-il toujours seul ? Pas toujours. Sur les démarreurs modernes, le solénoïde (contacteur intégré) fait partie
    intégrante de la mécanique du démarreur — il actionne à la fois le circuit électrique et le pignon de démarrage. Dans
    ce cas, seul l''ensemble démarreur peut être remplacé. Sur les architectures plus anciennes avec contacteur séparé dans
    le circuit de démarrage, la pièce se remplace bien seule. Consulter le catalogue constructeur pour identifier la configuration
    exacte. Un contacteur démarreur peut-il tomber en panne à cause du froid ? Oui. Par temps très froid, la résistance interne
    augmente dans tous les composants électriques, et les contacts internes oxydés d''un contacteur vieillissant peuvent ne
    plus établir la connexion nécessaire. Si le véhicule démarre normalement après réchauffement du moteur, c''est un signe
    que le contacteur ou la batterie est en fin de vie et doit être contrôlé avant l''hiver suivant.'
  META: '{"meta_title":"Contacteur démarreur : diagnostic et remplacement | AutoMecanik","meta_description":"Aucune réaction
    à la clé, démarrage intermittent, tableau de bord muet ? Diagnostiquez votre contacteur démarreur et trouvez la pièce
    compatible avec votre véhicule.","source":"rag://gammes/contacteur-demarreur.md"}'
---

# Contacteur démarreur - Guide Diagnostic Complet

## Fonction et Rôle

Commuter le circuit electrique du demarreur

**Actions principales:** commuter, activer, alimenter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- aucune reaction a la cle de contact
- demarrage intermittent
- tableau de bord qui ne s allume pas

## Procédure de Diagnostic

Pour diagnostiquer un problème de contacteur démarreur:

1. **Inspection visuelle** - Examiner l'état du contacteur démarreur
2. **Test électrique** - Vérifier la tension et les connexions
3. **Lecture codes défaut** - Scanner OBD si voyant allumé


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- demarreur
- batterie

## Critères de Compatibilité

Pour commander le bon contacteur démarreur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "demarrage garanti"

## FAQ

**Comment choisir Contacteur démarreur compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Contacteur démarreur ?**
En cas de aucune reaction a la cle de contact ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Contacteur démarreur sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.


## References supplementaires

<!-- materialized-from-db manual/2e276e4a0c44 2026-04-03 -->
### Données techniques OEM — Contacteur démarreur

# Données techniques OEM — Contacteur démarreur
Source : fr.wikipedia.org (1 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- pneumatique
- électrique
