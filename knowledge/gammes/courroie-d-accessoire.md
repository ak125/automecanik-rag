---
category: distribution
slug: courroie-d-accessoire
title: Courroie d'accessoire
pg_id: 10
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
  role: Entraîne les accessoires moteur
  must_be_true:
  - entrainer
  - transmettre
  must_not_contain:
  - freinage
  - climatisation
  - turbo
  - injection
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - courroie-de-distribution
  - kit-de-distribution
  - galet-tendeur-de-courroie-de-distribution
  - galet-enrouleur-de-courroie-de-distribution
  - pompe-a-eau
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
  - ❌ "plus de puissance"
  cost_range:
    min: 7
    max: 181
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  brands:
    premium:
    - Gates
    - Continental/Contitech
    standard:
    - Dayco
    - SKF
    - INA
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Sifflement au demarrage ou a l acceleration
    severity: confort
  - id: S2
    label: Courroie fissuree ou effilochee visible
    severity: confort
  - id: S3
    label: Voyant batterie allume alternateur non entraine
    severity: confort
  - id: S4
    label: Perte de direction assistee si sur meme courroie
    severity: securite
  - id: S5
    label: Odeur de caoutchouc brule
    severity: confort
  - id: S6
    label: Plus de 60 000 km ou 5 ans depuis le remplacement
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - remplacement preventif recommande
  quick_checks:
  - 'Observer : sifflement au demarrage ou a l acceleration ?'
  - 'Observer : courroie fissuree ou effilochee visible ?'
  - Voyant batterie allume alternateur non entraine ?
  - 'Observer : perte de direction assistee si sur meme courroie ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Sifflement au demarrage ou a l acceleration
  - Courroie fissuree ou effilochee visible
  - Voyant batterie allume alternateur non entraine
  - Perte de direction assistee si sur meme courroie
  - Odeur de caoutchouc brule
  - Plus de 60 000 km ou 5 ans depuis le remplacement
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '10'
  intro_title: A quoi sert Courroie d'accessoire ?
  risk_title: Pourquoi remplacer Courroie d'accessoire a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: Peut-on rouler sans courroie d'accessoire ?
    answer: Quelques kilomètres seulement. Sans alternateur, la batterie se vide. Sans pompe de direction, le volant devient
      très dur. Dépannage uniquement.
  - question: Comment savoir si elle est usée ?
    answer: 'Visuellement : craquelures, effilochage, brillance (glaçage). Au son : sifflement au démarrage ou quand vous
      braquez à fond.'
  - question: Faut-il changer le galet tendeur ?
    answer: Recommandé si plus de 100 000 km ou si bruit de roulement. Le galet coûte peu et peut bloquer la courroie s'il
      gripe.
  - question: Quelles sont les erreurs fréquentes à éviter ?
    answer: Mettre du produit "anti-sifflement" au lieu de changer la courroie. Trop ou pas assez tendre. Oublier de vérifier
      les galets.
  - question: Comment faire un diagnostic rapide ?
    answer: Sifflement → courroie usée ou mal tendue. Témoin batterie → courroie cassée ou alternateur. Direction dure soudaine
      → courroie à vérifier.
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
doc_id: 30f1197d-61fc-5083-95ac-cc6afe7cee95
content_hash: sha256:880711935f0e0d1b
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
  area: Face laterale du moteur, derriere le carter de distribution
  access: Depose courroie accessoire + carter distribution
  adjacent_parts:
  - courroie
  - galets
  - pompe a eau
  - poulie
installation:
  difficulty: difficile (pro recommande)
  time: 3h a 6h
  tools:
  - kit calage distribution
  - cle dynamometrique
  - extracteur poulie
  prerequisite: Moteur cale au PMH, ne pas tourner le moteur sans courroie
phase5_enrichment:
  _source: automotive.hutchinson.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 1
  types_variants:
  - type: 'Poly V'
    source_ref: corpus RAG web OEM
  - type: 'polyv'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_2_a: '2 a'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'La courroie d''accessoire (aussi appelee courroie d''alternateur ou courroie trapezoidale) entraine les accessoires
    moteur a partir de la poulie de vilebrequin : alternateur, pompe de direction assistee, pompe a eau (selon equipement)
    et compresseur de climatisation. Types de courroies : - Courroie trapezoidale : section en forme de trapeze, utilisee
    sur les anciens vehicules- Courroie poly-V : la plus repandue, plus efficace et plus silencieuse grace a ses nervures
    multiples La courroie est guidee par des galets tendeurs (reglage de tension) et des galets enrouleurs (cheminement).
    Le nombre de galets varie selon la longueur de la courroie et les equipements entraines. Attention : sans courroie d''accessoires,
    la batterie ne se recharge plus et aucun composant electrique du vehicule ne fonctionne. Sur certains vehicules, la rupture
    de la courroie peut entrainer la surchauffe moteur si elle entraine la pompe a eau. Pieces liees : courroie de distribution,
    kit de distribution, galet tendeur de courroie de distribution, galet enrouleur de courroie de distribution, pompe a eau.'
  S2: 'Ne pas attendre la panne complete pour intervenir. Symptômes d''usure : - Sifflement au demarrage ou a l acceleration
    - Courroie fissuree ou effilochee visible - Voyant batterie allume alternateur non entraine - Perte de direction assistee
    si sur meme courroie - Odeur de caoutchouc brule - Plus de 60 000 km ou 5 ans depuis le remplacement'
  S2_DIAG: 'SymptômeCause probableActionSifflement au demarrage ou a l accelerationlocaliser source et verifier usure mecaniqueObserver
    : sifflement au demarrage ou a l acceleration ?Courroie fissuree ou effilochee visiblelecture codes defaut obd et diagnostic
    electroniqueObserver : courroie fissuree ou effilochee visible ?Voyant batterie allume alternateur non entraineremplacement
    preventif recommandeVoyant batterie allume alternateur non entraine ?Perte de direction assistee si sur meme courroielocaliser
    source et verifier usure mecaniqueObserver : perte de direction assistee si sur meme courroie ?Odeur de caoutchouc brulelocaliser
    source et verifier usure mecaniqueObserver : sifflement au demarrage ou a l acceleration ?Plus de 60 000 km ou 5 ans depuis
    le remplacementlocaliser source et verifier usure mecaniqueObserver : sifflement au demarrage ou a l acceleration ?'
  S3: 'Pour choisir la bonne courroie d''accessoire pour votre vehicule : - Type de courroie : trapezoidale (anciens vehicules)
    ou poly-V (la plupart des vehicules recents) — ne pas interchanger- Longueur et nombre de nervures : varient selon les
    options du vehicule (avec ou sans direction assistee, avec ou sans climatisation) — verifier la reference exacte- Etat
    visuel avant achat : si l''ancienne courroie presente des craquelures, dechirures ou irregularites, le remplacement est
    urgent- Galets a remplacer en meme temps : un galet tendeur fatigue fait patiner la courroie neuve — prevoir le kit complet
    (courroie + galets)- Compatibilite vehicule : marque, modele, motorisation et annee — une courroie trop courte ou trop
    longue ne se monte pas correctement'
  S4_DEPOSE: '📖 Avant de démonter, consultez la fiche technique Courroie d''accessoire pour connaître les spécifications.
    - Débranchez la batterie. - Levez et calez le véhicule. - Démontez la roue avant droite. - Démontez l''écran pare-boue
    avant droit. - Démontez les vis de fixation de la protection sousmoteur. - Démontez la protection sous moteur. - Identifiez
    le type de galet tendeur (manuel ouautomatique). Note : Les galets tendeurs peuvent avoirdifférents systèmes de réglage
    de la tension. Certains sont à tensionautomatique via un ressort ou un vérin hydraulique. D''autres nécessitent unetension
    manuelle. - Repérez le cheminement de la courroie d''accessoires. - Relâchez la tension de la courroie d''accessoires.
    Note : La tension peut être réalisée soit par lesgalets tendeurs, ou par les différents équipements entraînés par la courroie
    d''accessoires (alternateurs ou pompe de direction assistée ). Dans ce cas il est indispensablede consulter la revue technique,
    car chaque cas est différent. - Démontez la courroie d''accessoires. - Déposer le galet tendeur et le galet enrouleur.'
  S4_REPOSE: '- Vérifier que la longueurde la courroie d''accessoires neuve est identique à la courroie démontée. - Contrôlez
    l''étatde la poulie d''alternateur , de la poulie de vilebrequin et de la poulie decompresseur de climatisation , s''il
    y a présence de jeu dans les poulies. - Contrôlez l''étatde la pompe à eau si elle entraînée par la courroie d''accessoires
    et laremplacée en cas de présence de fuite de liquide de refroidissement. - Remontez le galet tendeur et le galet enrouleur.
    - Mettre en place lacourroie d''accessoires en tenant compte de son cheminement. - Réamorcer le galettendeur pour retendre
    la courroie d''accessoires. - Ajuster la tensionsuivant le type de tendeur. - Si le galet tendeur estautomatique : il
    peut être équipé d''une bride de maintient qui facilite la posede la courroie. Dans le cas d''un galet tendeur automatique
    sans bride de maintient,il faut détendre le système de poussé du galet en même temps qu''on repositionnela courroie. -
    Si le galettendeur est manuel : en général une courroie correctement tendue doit pouvoirfaire un quart de tour dans son
    épaisseur en la prenant par le bout des doigts(entre l''index et le pouce). Faire le test au milieu de la portion la pluslongue
    (entre deux équipements ou tendeurs). - Rebrancher la batterie. - Démarrez lavoiture. - Vérifiez que lacourroie d''accessoires
    présente une tension correcte en accélérant par à coups : - Si la courroien''est pas assez tendue, elle n''accroche pas
    suffisamment aux poulies lors del''accélération et donc patine, créant ainsi un sifflement. - Si la courroie esttrop tendue,
    elle exerce une tension trop importante sur les roulements qui sefont entendre (sorte de ronflement) à la décélération.
    - Remontez laprotection sous moteur. - Remontez lepare-boue. - Remontez la roue. - Redescendre levéhicule. - Resserrez
    la roue. ✅ Après remontage, vérifiez les spécifications dans la fiche technique Courroie d''accessoire.'
  S5: 'Erreurs frequentes avec la courroie d''accessoire : - Ne pas remplacer les galets tendeurs et enrouleurs en meme temps
    que la courroie — un galet fatigue fait patiner ou deporter la courroie neuve- Ignorer un sifflement au demarrage ou a
    l''acceleration — signe de courroie detendue ou de galet tendeur use- Ne pas verifier le cheminement de la courroie avant
    demontage — sans schema, le remontage sera incorrect et la courroie va sauter- Confondre courroie d''accessoire et courroie
    de distribution — elles n''ont pas le meme role ni le meme emplacement- Negliger le voyant batterie allume — il peut signaler
    une courroie cassee ou detendue (l''alternateur n''entraine plus)- Oublier de verifier la tension apres montage — une
    courroie trop tendue use les roulements des galets, trop lache elle patine et siffle'
  S6: 'Une courroie d''accessoire mal posée ou mal tendue peut lâcher en quelques dizaines de kilomètres, entraînant la perte
    simultanée de l''alternateur, de la direction assistée hydraulique et du compresseur de climatisation. Les contrôles post-montage
    prennent moins de 5 minutes et évitent une panne en route. - Vérifier le guidage de la courroie sur toutes les poulies
    : avant le démarrage, s''assurer que la courroie est centrée sur chaque gorge de poulie (vilebrequin, alternateur, compresseur,
    pompe de direction assistée). Une courroie décalée de 2 mm frotte sur le flanc et s''effiloche rapidement. - Contrôler
    la tension après montage à froid : sur les systèmes à galet tendeur automatique, vérifier que le galet est en butée correcte
    et que la flèche de courroie est nulle. Sur les systèmes à réglage manuel, la flèche admissible est généralement de 10
    à 15 mm sous une force de 10 N appliquée au milieu du brin le plus long. - Démarrer le moteur et écouter les premières
    secondes : au démarrage, aucun sifflement ni couinement ne doit apparaître. Un sifflement persistant après 30 secondes
    signale une courroie mal tendue ou un galet tendeur défectueux. - Vérifier la tension à chaud après 10 minutes : sur les
    systèmes à galet automatique, contrôler que le galet tendeur se repositionne correctement une fois le moteur à température.
    La courroie se détend légèrement à chaud — c''est normal — mais ne doit pas claquer. - Contrôler l''état de charge de
    la batterie : après 10 minutes de fonctionnement, la tension aux bornes de la batterie doit être entre 13,8 V et 14,4
    V, confirmant que l''alternateur est bien entraîné. En dessous de 13,5 V, la courroie patine sur la poulie d''alternateur.
    - Tester la direction assistée hydraulique si présente : braquer à fond dans les deux sens à l''arrêt. La direction doit
    rester légère sans bruit de pompe. Un grincement ou une résistance accrue indique que la courroie de la pompe de direction
    patine. - Inspecter visuellement la courroie après 500 km : contrôler l''absence de fissures transversales, de bords effilochés
    ou de brillance anormale sur la face intérieure, signes d''une mauvaise tension ou d''un galet défectueux.'
  S_GARAGE: 'Nous vous recommandons de confier cette intervention à un professionnel : - Plusieurs causes possibles de défaillance
    (3 identifiées) nécessitent un diagnostic professionnel Un garagiste qualifié dispose de l''outillage et de l''expérience
    nécessaires pour effectuer cette opération en toute sécurité.'
  S7: '- alternateur - compresseur de climatisation - galet enrouleur de courroie d accessoire - galet tendeur de courroie
    d accessoire - pompe a eau - pompe de direction assistée - poulie d alternateur - poulie vilebrequin'
  S8: 'Peut-on rouler sans courroie d''accessoire ?Quelques kilomètres seulement. Sans alternateur, la batterie se vide. Sans
    pompe de direction, le volant devient très dur. Dépannage uniquement. Comment savoir si elle est usée ?Visuellement :
    craquelures, effilochage, brillance (glaçage). Au son : sifflement au démarrage ou quand vous braquez à fond. Faut-il
    changer le galet tendeur ?Recommandé si plus de 100 000 km ou si bruit de roulement. Le galet coûte peu et peut bloquer
    la courroie s''il gripe. Quelles sont les erreurs fréquentes à éviter ?Mettre du produit "anti-sifflement" au lieu de
    changer la courroie. Trop ou pas assez tendre. Oublier de vérifier les galets. Comment faire un diagnostic rapide ?Sifflement
    → courroie usée ou mal tendue. Témoin batterie → courroie cassée ou alternateur. Direction dure soudaine → courroie à
    vérifier.'
  META: '{"meta_title":"Courroie Accessoire : Guide Remplacement | AutoMecanik","meta_description":"Sifflement moteur ou courroie
    fissurée ? Découvrez quand changer la courroie d''accessoire, comment la remplacer et choisir le bon modèle sur AutoMecanik."}'
---

# Courroie d'accessoire - Guide Diagnostic Complet

## Fonction et Rôle

Entraîne les accessoires moteur

**Actions principales:** entrainer, transmettre

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Perte de direction assistee si sur meme courroie**
  perte de direction assistee si sur meme courroie

### 🟢 Autres Symptômes

- sifflement au demarrage ou a l acceleration
- courroie fissuree ou effilochee visible
- voyant batterie allume alternateur non entraine
- odeur de caoutchouc brule
- plus de 60 000 km ou 5 ans depuis le remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de courroie d'accessoire:

1. **Inspection visuelle** - Examiner l'état du courroie d'accessoire
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## References supplementaires

<!-- materialized-from-db manual/36e9537e2c77 2026-03-28 -->
### Courroie Hybroad®

Courroie
Courroie Hybroad®

La courroie HUTCHINSON® Hybroad® est spécialement conçue et optimisée pour répondre aux exigences de l’électrification des véhicules.

Principaux bénéfices
Capacité de transmission de couple élevé
Excellentes performances acoustiques
Résistance à des sollicitations intenses
Caractéristiques
Structure de la courroie

Haute qualité de fabrication :

Face arrière en EPDM renforcé de fibres pour assurer la stabilité de la ligne de câblage
Câblage en aramide, capable de fonctionner sous très haute tension
EPDM optimisé, renforcé de fibres, permettant de transmettre des charges lourdes (couple)
Bonne adhérence en conditions sèches et humides, tout au long de la durée de vie de la courroie
Revêtement tricot, spécialement conçu pour offrir les coefficients de friction requis
Performances

Capacité de transmission de couple élevé

Tests de performance spécifiques :

Coefficients de friction à sec et en conditions humides, à l’état neuf et âgé
Test de glissement en conditions humides
Test lors des phases Stop & Start

Excellentes performances acoustiques

Tests spécifiques :

En conditions sèches et humides
À l’état neuf et âgé
Lors de redémarrage en conditions humides
En cas de désalignement

Durabilité

Tests spécifiques :

Évaluation de la fatigue des dents de la courroie en conditions chaudes et froides
Évaluation de la résistance à l’usure du câblage
Bénéfices
Amélioration des performances
Longévité
Réduction du bruit
Industries
Automobile
Camions & Bus

Voici aussi la version ultra épurée :

Courroie Hybroad®

Cette courroie est spécialement conçue pour répondre aux exigences de l’électrification des véhicules.

Principaux bénéfices
Transmission de couple élevé
Excellentes performances acoustiques
Résistance à des sollicitations intenses
Caractéristiques techniques

Structure :

Face arrière en EPDM renforcé de fibres
Câblage en aramide pour très haute tension
EPDM renforcé de fibres pour charges lourdes
Bonne adhérence à sec et en conditions humides
Revêtement tricot adapté aux coefficients de friction requis

Performances et validation :

Tests de friction à sec et en conditions humides
Tests de glissement en conditions humides
Validation en phases Stop & Start
Tests acoustiques en conditions sèches et humides
Validation au redémarrage humide et en cas de désalignement
Tests de fatigue des dents en conditions chaudes et froides
Tests de résistance à l’usure du câblage
Bénéfices
Amélioration des performances
Longévité
Réduction du bruit

<!-- materialized-from-db manual/587e2a0702ad 2026-03-28 -->
### Courroie Poly V

Courroie
Courroie Poly V

HUTCHINSON® Poly V est une courroie de transmission de puissance destinée aux systèmes d'accessoires et d'entraînement par courroie des véhicules.
Grâce à ses dents longitudinales, la courroie Poly V transmet le couple par contact entre les dents de la courroie et les gorges de la poulie.

Principaux bénéfices
Durabilité accrue
Structure optimisée
Performances testées et prouvées
Caractéristiques
Structure de la courroie

Haute qualité de fabrication :

Les dents sont formées par moulage et entraînent la poulie par pression de contact dans les gorges. Elles sont composées d’un caoutchouc EPDM à haute résistance aux contraintes mécaniques et aux agressions environnementales.

Selon l’application, notre gamme de revêtement de dents offre la solution adaptée à chaque niveau sonore requis.

Le câblage en polyester (PET) convient à la plupart des applications, tandis que le câblage en aramide est la norme pour les applications les plus exigeantes. Son module élevé permet de gérer les comportements NVH (bruit, vibrations, dureté) au-delà des critères habituels.

Le dos de la courroie entre en contact avec les galets tendeurs et peut également transmettre la puissance sur des poulies plates. Il protège le câblage et assure la stabilité radiale de la structure.

Performances
Processus de moulage réduisant les pertes de matière et garantissant un contrôle dimensionnel
Profil conforme à la norme ISO 9981
Rigidité et longueur de la courroie stables dans le temps
Large gamme de longueurs et de largeurs de courroies
Plage de température de fonctionnement de -40 à +135 °C
Optimisée pour minimiser les pertes par friction
Excellente résistance à l’ozone
Résistance aux huiles et aux fluides
Durée de vie prolongée (240 000 km)
Capacité à supporter les contraintes mécaniques : flexion / contre-flexion, cisaillement
Tensions dynamiques
Capacité à entraîner plusieurs accessoires simultanément (alternateur, compresseur de climatisation, pompe de direction assistée, pompe à eau, ventilateur)
Bénéfices
Longévité
Optimisation des coûts
Fiabilité

<!-- materialized-from-db manual/1fde80c127aa 2026-03-28 -->
### Courroie Hybroad® avec tendeur hydraulique et galet

Systèmes d'entraînement par courroie
Courroie Hybroad® avec tendeur hydraulique et galet

La solution complète HUTCHINSON® courroie Hybroad® avec tendeur hydraulique et galet est le système idéal pour répondre aux exigences de l’électrification des véhicules.
Cette solution optimisée permet de réduire le poids et les coûts en supprimant l’isolation du vilebrequin.

Principaux bénéfices
Réduction du poids et des coûts
Système optimisé
Applications sévères y compris sur les véhicules mild-hybrid
Bénéfices
Optimisation des coûts
Amélioration des performances
Conception robuste
Industries
Automobile
Micro-mobilité
Camions & Bus
Véhicules tout terrain & Agriculture
Machines industrielles

Voici aussi la version ultra épurée :

Courroie Hybroad® avec tendeur hydraulique et galet

Cette solution complète de courroie avec tendeur hydraulique et galet est conçue pour répondre aux exigences de l’électrification des véhicules. Elle permet de réduire le poids et les coûts en supprimant l’isolation du vilebrequin.

Principaux bénéfices
Réduction du poids et des coûts
Système optimisé
Compatible avec des applications sévères, y compris les véhicules mild-hybrid
Bénéfices
Optimisation des coûts
Amélioration des performances
Conception robuste

<!-- materialized-from-db manual/9b17456bc379 2026-03-28 -->
### Courroie Stretchy

Courroie
Courroie Stretchy

La courroie élastique HUTCHINSON® (auto-tension) entraîne les systèmes d'accessoires et d'entraînement par courroie des véhicules. Elle est utilisée avec une distance fixe entre les centres des poulies et maintient automatiquement la tension du système sans nécessiter de tendeur supplémentaire.

Principaux bénéfices
Optimisation du système FEAD
Réduction des coûts et du poids
Tension stable
Caractéristiques
Structure de la courroie

Haute qualité de fabrication :

Formées par moulage, les dents de la courroie entraînent la poulie par pression de contact dans les gorges
Elles sont composées d’une base en caoutchouc EPDM, très résistante aux contraintes mécaniques et aux agressions extérieures
Selon l’application, la gamme de revêtements (flock PA / composite / film PE) offre la solution adaptée à chaque niveau sonore requis
Le câblage constitue la partie structurelle de la courroie et est composé de polyamide
Le dos de la courroie assure le contact avec les galets tendeurs et peut également transmettre la puissance sur des poulies plates
Il protège le câblage et garantit la stabilité radiale de la structure
Performances
Processus de moulage réduisant les pertes de matière et garantissant le contrôle dimensionnel
Profil conforme à la norme ISO9981
Large gamme de longueurs et de largeurs de courroies
Plage de température de fonctionnement de -40 à +135°C
Optimisée pour minimiser les pertes par friction et les charges sur les roulements
Excellente résistance à l’ozone
Résistance aux huiles et aux fluides
Durée de vie prolongée (240 000 km)
Capacité à entraîner plusieurs accessoires simultanément (alternateurs, compresseurs de climatisation, ventilateurs)
Bénéfices
Compacité
Optimisation des coûts
Légèreté
Fiabilité
Industries

<!-- materialized-from-db web-catalog/61ad952b2bd6 2026-03-28 -->
### Alternateurs haute performance | DENSO - Installation et détection des pannes

# Alternateurs haute performance | DENSO

- Alternateurs haute performance | DENSO

- Produits

- Machines tournantes

- Alternateurs

Alternateurs Un alternateur fiable peut soutenir la performance de l’ensemble du système électrique d’un véhicule. Recherche Produit Comment installer Informations générales Caractéristiques et avantages Types et caractéristiques Catalogues et brochures Installation et détection des pannes Recherche Produit Retourner Alternateurs Recherche Produit Comment ils fonctionnent Entraîné par le moteur, l’alternateur (avec la courroie et le régulateur) convertit l’énergie mécanique en énergie électrique qui fournit diverses charges dans le système du véhicule. Dans des conditions de conduite normales, cette énergie électrique sera utilisée pour recharger la batterie de la voiture. Lorsque la charge électrique requise ne correspond pas à la puissance produite par l’alternateur, la batterie fournit toute énergie supplémentaire nécessaire à l’équipement électrique.

Lorsque le régime du moteur change en fonction des conditions de conduite, la vitesse de l’alternateur et la tension générée changent également. Le régulateur contrôle cette tension générée, et s’assure que les différentes charges électriques sont alimentées avec la tension appropriée, y compris la batterie de la voiture.

Caractéristiques et avantages Fabriqué selon des normes de qualité supérieure Rigoureusement testé pour répondre aux exigences de haute performance Les technologies avancées permettent des performances optimales dans toutes les conditions Gamme de pièces intelligente et facile à comprendre avec une forte couverture Rendement élevé Petit et léger, le design des alternateurs DENSO, offre des performances élevées dans un produit compact et facile à installer. Qualité supérieure Un produit de choix pour Toyota et un large éventail de constructeurs automobiles européens, nos alternateurs sont fabriqués selon des normes haut de gamme. Technologies de pointe Compatibles avec des systèmes électroniques sophistiqués, nos alternateurs sont conçus pour fonctionner dans toutes les conditions météorologiques, et sous des charges électriques extrêmes. Types et caractéristiques Nous combinons notre ingénierie experte avec des matériaux de qualité supérieure, pour créer des alternateurs fiables et performants, qui peuvent être utilisés au fil des trajets. Alternateurs les types Alternateur avec petit ventilateur interne Conçu pour fournir des performances optimales dans un petit design léger, le ventilateur a deux pales qui sont intégrées dans le rotor, réduisant le poids, la taille et le bruit du ventilateur. De plus, les tailles optimisées du stator et du rotor, ainsi qu’un plus petit diamètre de poulie aident à augmenter la puissance.

Alternateur SC En 2000, DENSO a introduit le premier alternateur SC (Segment Conductor) au monde, en utilisant un conducteur de segment rectangulaire (fils de cuivre angulaires) pour sa bobine de stator. L’alternateur SC réduit la résistance de la bobine et les pertes thermiques de 50 pour cent, le tout dans un facteur de forme plus petit et plus dense. Le résultat est un alternateur compact, et léger avec un rendement et une puissance élevés.

Caractéristiques Nos technologies avancées permettent, un rendement optimal dans un design léger et de petite taille. Cela permet une efficacité maximale dans une pièce facile à monter, et ayant une longue durée de vie.

---

## Catalogues et brochures

Pour plus d'information Alternateurs visitez notre zone de téléchargement Click here.

---

## Installation et détection des pannes

Les pannes d’alternateurs peuvent causer des dommages importants aux systèmes électriques d’un véhicule. Pour éviter cela, il est important d’installer les alternateurs correctement, et de résoudre les problèmes rapidement.

---

### Remplacement

- Identifier chaque connexion de fil, et noter son emplacement sur l’alternateur.

- Débrancher les fils de l’alternateur.

- Desserrer le boulon du bras horizontal de l’alternateur, mais ne pas encore le retirer.

- Desserrer le contre-écrou ou le boulon de l’ensemble de tension, et tourner le boulon de réglage de sorte que la tension de la courroie d’entraînement soit suffisamment. Réduite pour permettre le retrait de la courroie. Certains véhicules peuvent être équipés d’un tendeur automatique à ressort. Faire tourner le tendeur à ressort à l’aide de l’outil approprié suffisamment loin, pour permettre le retrait de la courroie d’entraînement.

- Retirer la courroie d’entraînement de l’alternateur.

- Soutenir l’alternateur et retirer les boulons, maintenant l’alternateur en place. Mettre les boulons et l’alternateur de côté. Veiller à noter l’orientation du support et la longueur/l’emplacement de la fixation avant de retirer l’alternateur.

- Inspecter l’état du câblage et des connecteurs. Inspecter les extrémités des fils usées, la continuité, les connecteurs desserrés ou cassés, la corrosion et la souplesse. Réparer ou remplacer au besoin.

Comparer physiquement le nouvel alternateur à l’original. Comparer les décalages du boîtier et de la poulie, la taille et le type de la poulie, les emplacements des trous de pivotement et de réglage, les emplacements des connecteurs de fil et les configurations des bornes avec l’alternateur d’origine. Installer le ou les supports de montage, mais ne pas encore serrer complètement les boulons. Soutenir l’alternateur et le fixer en position, mais ne pas encore serrer complètement les boulons. Installer la courroie d’entraînement. Si la courroie d’entraînement est usée, étirée, fissurée, huileuse ou vitrée, elle doit être remplacée. Régler la tension de la courroie tout en serrant les boulons de montage et de réglage. Assurez-vous de régler la tension de la courroie et de serrer les boulons de montage selon les spécifications recommandées par le constructeur du véhicule. ATTENTION : Ne pas forcer ni heurter le boîtier de l’alternateur pour régler la tension de la courroie. Vérifier l’alignement de la courroie d’entraînement entre la poulie de l’alternateur et les autres poulies d’entraînement. S’assurer qu’il n’y a aucune interférence entre la courroie d’entraînement, et les autres composants. Rebrancher le connecteur de fil à son emplacement approprié sur l’alternateur. S’assurer qu’il n’y a aucune interférence entre le faisceau de câbles, et les autres composants. Réinstaller tous les composants. S’assurer que les fixations filetées sont correctement serrées, et qu’il n’y a aucune interférence entre les composants. Rebrancher le câble négatif de la batterie. Démarrez le moteur. Laissez pendant 5 minutes pour habituer la courroie d’entraînement. Réajuster la courroie d’entraînement en utilisant la spécification de tension « utilisée ». Éteignez le moteur et faites une nouvelle inspection. Tester à nouveau le système de charge pour vérifier qu’il fonctionne conformément aux spécifications du constructeur du véhicule. Recherche de défaut Trouvez et corrigez rapidement les défauts de l’alternateur. Le voyant d’avertissement de la batterie s’allume sur le tableau de bord. Les phares peuvent clignoter ou s’éteindre. Les accessoires électriques fonctionneront lentement ou pas du tout. Le conducteur remarquera un décrochage et un mauvais fonctionnement du moteur. La batterie s’écoule plus vite que prévu. Le moteur ne démarre pas ou

[...]
