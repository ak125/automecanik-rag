---
category: support_moteur
slug: support-moteur
title: Support moteur
pg_id: 247
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-26'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v4_converted
  last_enriched_by: script:materialize-db-to-md
  last_enriched_at: '2026-03-26'
domain:
  role: Fixe et isole le moteur du châssis
  must_be_true:
  - supporter
  - isoler
  - fixer
  must_not_contain:
  - injection
  - freinage
  - climatisation
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  confusion_with:
  - term: support-de-boite-vitesse
    difference: Support moteur = fixe le moteur au chassis. Support de boite = fixe la boite de vitesses. Positions differentes,
      references non interchangeables.
  - term: silent-bloc
    difference: Le silent-bloc est le composant caoutchouc/metal a l'interieur du support. Le support moteur est l'ensemble
      complet (silent-bloc + fixation).
  related_parts:
  - support-de-boite-vitesse
  - silent-bloc
  - berceau-moteur
  - biellette-de-reprise-de-couple
selection:
  criteria:
  - Identifier la position exacte du support (avant droit, avant gauche, arriere, inferieur)
  - Verifier la reference OE sur la piece d'origine ou dans le catalogue constructeur
  - Choisir un support de durete equivalente a l OE (trop souple = vibrations, trop dur = bruit)
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "moins de vibrations garanties"
  cost_range:
    min: 15
    max: 80
    currency: EUR
    unit: l'unite
    note: Support simple 15-30€, support hydraulique 40-80€. Biellette de reprise de couple 20-50€.
    source: catalogue automecanik
  brands:
    premium:
    - Lemforder
    - Hutchinson
    - Corteco
    standard:
    - Febi
    - Meyle
    - Swag
    budget:
    - Ridex
    - Topran
  quality_tiers:
  - tier: OE/OES
    description: Support identique a l'origine (Lemforder, Hutchinson, Corteco). Durete calibree par le constructeur.
    price_range: 40-80€
  - tier: Equipementier
    description: Qualite equivalente (Febi, Meyle). Bon compromis qualite/prix pour vehicule hors garantie.
    price_range: 20-50€
  - tier: Adaptable
    description: Pieces generiques. Durete parfois differente de l'OE, risque de vibrations residuelles.
    price_range: 15-30€
variants:
- name: Support moteur hydraulique
  aliases:
  - support hydro
  - hydrolager
  visual_differences:
  - contient du liquide hydraulique
  - plus lourd
  - corps metallique ferme
  functional_differences:
  - meilleure absorption des vibrations
  - monte sur moteurs diesel et puissants
- name: Support moteur caoutchouc (classique)
  aliases:
  - support silent-bloc
  - silent-bloc moteur
  visual_differences:
  - bloc caoutchouc visible
  - forme simple
  - plus leger
  functional_differences:
  - standard sur petits moteurs essence
  - duree de vie longue
  - remplacement facile
- name: Biellette de reprise de couple
  aliases:
  - biellette anti-couple
  - tirant moteur
  visual_differences:
  - barre avec silent-blocs aux deux extremites
  - fixee entre moteur et berceau
  functional_differences:
  - limite le basculement du moteur en acceleration/deceleration
  - souvent oubliee au diagnostic
location_on_vehicle:
  area: Compartiment moteur, entre le bloc moteur et le berceau/chassis
  access: Par le dessus (capot) ou par le dessous (pont elevateur selon position)
  adjacent_parts:
  - berceau moteur
  - carter huile
  - support de boite
  - faisceau electrique moteur
installation:
  difficulty: moyen
  tools:
  - cle a douille 16/18mm
  - cric hydraulique
  - support moteur ou chandelle
  - cle dynamometrique
  time: 1h a 2h par support
  prerequisite: Soutenir le moteur avant de retirer le support
  steps:
  - Soutenir le moteur avec un cric hydraulique sous le carter (cale bois entre cric et carter)
  - Devisser les fixations du support cote chassis (2 a 4 vis selon vehicule)
  - Devisser la fixation cote moteur
  - Retirer l'ancien support, verifier l'etat des goujons et du chassis
  - Positionner le nouveau support, visser a la main d'abord
  - Serrer au couple preconise (40-60 Nm cote chassis, 60-80 Nm cote moteur selon constructeur)
  - Redescendre le moteur progressivement, verifier alignement et absence de contrainte
diagnostic:
  symptoms:
  - id: S1
    label: Vibrations excessives ressenties volant habitacle
    severity: confort
  - id: S2
    label: Caoutchouc support visiblement fissure affaisse
    severity: confort
  - id: S3
    label: Bruit sourd ou claquement lors des accelerations
    severity: confort
  - id: S4
    label: Moteur bouge anormalement ouverture capot
    severity: confort
  - id: S5
    label: A-coups au passage des vitesses
    severity: confort
  - id: S6
    label: Plus de 120 000 km ou vibrations au ralenti
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - verifier equilibrage et fixations
  - remplacement preventif recommande
  depose_steps:
  - Soutenir le moteur avec un cric hydraulique sous le carter ou un support moteur dedie
  - Devisser les fixations du support moteur (2 a 4 vis, cle de 16 ou 18 selon vehicule)
  - Retirer l'ancien support en verifiant l'etat du chassis et des goujons de fixation
  - Positionner le nouveau support, serrer au couple preconise (40-60 Nm selon constructeur)
  - Redescendre le moteur progressivement, verifier l'alignement et l'absence de jeu
  quick_checks:
  - Vibrations excessives ressenties volant habitacle ?
  - 'Observer : caoutchouc support visiblement fissure affaisse ?'
  - Bruit sourd ou claquement lors des accelerations ?
  - 'Observer : moteur bouge anormalement ouverture capot ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Vibrations excessives ressenties volant habitacle
  - Caoutchouc support visiblement fissure affaisse
  - Bruit sourd ou claquement lors des accelerations
  - Moteur bouge anormalement ouverture capot
  - A-coups au passage des vitesses
  - Plus de 120 000 km ou vibrations au ralenti
  good_practices:
  - Controle visuel des fuites et deformations a chaque revision
  - Remplacement par paire (meme essieu) pour equilibre du vehicule
  - Faire verifier la geometrie apres remplacement
  - Inspection des silent-blocs et des rotules associees
rendering:
  pgId: '247'
  intro_title: A quoi sert Support moteur ?
  risk_title: Pourquoi remplacer Support moteur a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
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
  - question: Support moteur OE, OES ou adaptable ?
    answer: Les supports OES (Lemförder, Corteco, Hutchinson) sont de qualité équivalente à l'OE. adaptables (Febi, Meyle)
      offrent un bon rapport qualité/prix.
  - question: Comment savoir si mon support moteur est HS ?
    answer: Vibrations excessives au ralenti, à-coups au démarrage ou passage de vitesses, bruit sourd en accélération, moteur
      qui bouge visiblement.
  - question: Tous les combien changer les supports moteur ?
    answer: Pas de périodicité fixe. Durée de vie 100 000 à 200 000 km selon utilisation. À vérifier si vibrations anormales
      au ralenti.
  - question: Peut-on changer un support moteur soi-même ?
    answer: Possible mais nécessite de soutenir le moteur avec un cric. Attention à ne pas endommager le carter. Prévoir 1
      à 2h par support.
  - question: Quelle erreur éviter avec les supports moteur ?
    answer: Ne pas serrer les vis moteur en charge. Serrer au couple moteur soulevé puis reposer. Vérifier l'alignement des
      autres supports.
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
doc_id: 76f9403a-1632-52f8-a964-992defd5aaf9
content_hash: sha256:db35993dbc6523f8
lang: fr
---

## Entretien supplementaire

<!-- materialized-from-db manual/54f200c202e1 2026-03-25 -->
### Comment entretenir les supports moteur

Pièces
Diagnostic
Solutions d'atelier
Masters of Motion
Presse & Actualités
À propos
Accueil
Tutoriels
Comment entretenir les supports moteur
Tutoriels
Comment entretenir les supports moteur
Partage de ressource:
    
Ressources importantes
Dans cet article vous allez découvrir comment fonctionnent les supports moteur, les types de support qui existe et  comment les entretenir. 
How to resource banner
Un support moteur défectueux ou usé est l’une des principales causes de vibrations et de bruit du moteur. Bien que cela puisse être préoccupant pour les propriétaires de véhicules, en comprenant les raisons de leurs défaillances, ce qu'il faut vérifier et comment les remplacer, vous pouvez aider vos clients à maintenir leurs voitures en bon état de marche, pour une conduite silencieuse et confortable. Dans cet article, Delphi Technologies vous conseille pour réaliser au mieux cet entretien.

Comment fonctionnent les supports moteur ?
Comme son nom l’indique, le support moteur fixe le moteur au châssis du véhicule ; une extrémité se visse au bloc moteur et l’autre au châssis de la voiture. En plus du fait de maintenir le moteur fermement en place, le support en caoutchouc vulcanisé sert d'isolant entre le châssis du véhicule et les composants du moteur, contribuant ainsi à réduire le bruit, les vibrations et les secousses pour une conduite confortable et silencieuse. La plupart des véhicules dispose de trois supports moteur, en plus d’un ou deux supports de transmission.

Types de support moteur
Il existe trois types de supports moteur et, en fonction de l'application, les constructeurs peuvent choisir d’en utiliser plusieurs parmi ceux-ci :

Supports passifs en caoutchouc : les supports passifs en caoutchouc suivent une conception caoutchouc-métal typique, deux points de fixation en métal liés par un composé de caoutchouc, et sont adaptés à la plupart des véhicules. 
Supports hydrauliques passifs : certaines applications comportent des supports hydrauliques remplis de liquide. Aussi connus sous le nom de supports hydrauliques passifs, ils contiennent une chambre remplie de fluide hydraulique qui aide à absorber des vibrations supplémentaires.
Supports actifs : certains véhicules récents utilisent des supports actifs ou à commande électronique. Dotés d'une chambre à vide supplémentaire, contrôlés par une vanne de commutation à vide, ils peuvent ajuster la rigidité du support afin d'absorber plus ou moins de vibrations en fonction de la vitesse ou de la charge.

[...]

## References supplementaires

<!-- materialized-from-db manual/e1021c922d93 2026-03-26 -->
### Suspension Moteur

Suspension Moteur
Biellette de reprise de couple conventionnel

Notre solution de filtration pour roll restrictor est conçue pour atténuer les vibrations induites par le groupe motopropulseur et la route, assurant des performances NVH optimales et une fiabilité à long terme sur toutes les plateformes de mobilité. Grâce à des options personnalisables en formulations de caoutchouc naturel, métaux et plastiques, elle offre une grande flexibilité en matière de conception et d’intégration, tout en étant entièrement optimisée pour la maîtrise des coûts, sans compromis sur la qualité.

Principaux bénéfices
Optimisation du poids
Optimisation des coûts
Durabilité et comportement ajustable
Caractéristiques techniques
Structures

Fonction :
L’élément principal en caoutchouc (EPC), composé principalement de caoutchouc naturel pour ses propriétés de déformabilité, est lié à au moins deux composants métalliques ou composites.
Nos roll restrictors gèrent le couple moteur et les mouvements de rotation.
Conception sur mesure, de la conception à la fin de vie.

Performances

Résistance mécanique

Conçu pour supporter les charges maximales
Plage de température : de -40°C à +110°C

Filtration

Entre -20 dB et -30 dB, grâce à l’accord dynamique des mélanges

Poids

Optimisé grâce à la conception et à la sélection des matériaux

Respect de l’environnement

Résistant aux liquides : huile, liquide de refroidissement, produits chimiques, eau, humidité, etc.
Protection anticorrosion appliquée selon les besoins
Caractéristiques

Comportement :

Déflexion sous charge
Rigidité

Performances :

Amortissement
Fatigue
Mélange
Bénéfices
Réduction des vibrations
Optimisation des coûts
Longévité

<!-- materialized-from-db manual/2551ca703c08 2026-03-26 -->
### Articulation conventionnelle

Articulation conventionnelle

Nos solutions de filtration cylindrique sont conçues pour atténuer les vibrations générées par le groupe motopropulseur et la route, garantissant des performances optimales ainsi qu'une fiabilité à long terme sur tous types de véhicules. Grâce à l'optimisation de nos formulations caoutchouc, l'utilisation de composants métalliques et plastiques, nos articulations offrent une flexibilité de conception et d’intégration, en assurant la compétitivité des coûts sans compromis sur la qualité.

Principaux bénéfices
Optimisation des coûts
Optimisation fonctionnelle : filtration et endurance
Conception bi-matière en option
Caractéristiques techniques
Structures

Fonction :
L’élément principal composé de caoutchouc naturel pour ses propriétés de déformabilité est adhéré à au moins deux composants, métalliques ou composites.
Nos articulations assurent la liaison entre deux structures du véhicule.
Design sur mesure, de la conception à la fin de vie.

Performances

Résistance mécanique

Conçu pour supporter les charges maximales
Plage de température : de -40°C à +110°C

Filtration

Entre -20 dB et -30 dB, grâce à l’amortissement du mélange

Poids

Optimisé par la conception et le choix des matériaux

Respect de l’environnement

Résistant aux liquides : huile, liquide de refroidissement, produits chimiques, eau, etc.
Protection anticorrosion appliquée selon les besoins
Caractéristiques

Comportement :

Déflexion sous charge
Rigidité

Performances :

Amortissement
Fatigue
Mélange
Bénéfices
Réduction des vibrations
Optimisation des coûts
Longévité

<!-- materialized-from-db manual/b105723c365e 2026-03-26 -->
### Articulation hydraulique

Articulation hydraulique

Conçue pour offrir un confort de conduite premium, nos solutions de filtration hydraulique cylindrique assurent un amortissement important aux fréquences et amplitudes ciblées. Cette technologie permet de réduire efficacement les vibrations induites par le groupe motopropulseur et la route. Grâce à une large gamme de matériaux, incluant des formulations en caoutchouc naturel, des composants métalliques et plastiques, nos articulations garantissent des performances supérieures, une durabilité à long terme, tout en assurant la compétitivité des coûts sans compromis sur la qualité.

Principaux bénéfices
Amortissement renforcé
Optimisation fonctionnelle : filtration et endurance
Caractéristiques techniques
Structures

Fonction :
Ce composant élastomère à fluide intégré est constitué d’un élément principal en caoutchouc (EPC), principalement en caoutchouc naturel pour ses propriétés de déformabilité, lié à au moins deux composants — interne et manchon de fenêtre — métalliques ou composites.

Un liquide de type glycol est encapsulé entre l’EPC et un composant externe. Sa structure est conçue pour offrir un haut niveau d’amortissement à une fréquence spécifique, tout en assurant la conformité entre deux structures du véhicule.
Conception sur mesure, de la conception à la fin de vie.

Performances

Résistance mécanique

Conçu pour supporter les charges maximales
Plage de température : de -40°C à +110°C

Filtration

Amortissement élevé à basse fréquence pour un confort amélioré, grâce à la conception et aux caractéristiques du fluide
Entre -20 dB et -30 dB, grâce à la conception et à l’accord dynamique des mélanges pour les hautes fréquences

Poids

Optimisé grâce à la conception et à la sélection des matériaux

Respect de l’environnement

Résistant aux liquides : huile, liquide de refroidissement, produits chimiques, eau, humidité, etc.
Protection anticorrosion appliquée selon les besoins
Caractéristiques

Comportement :

Déflexion sous charge
Rigidité
Amortissement maximal

Performances :

Viscosité du fluide
Fatigue
Mélange
Bénéfices
Réduction des vibrations
Amélioration des performances
Confort
Optimisation des coûts
Longévité

<!-- materialized-from-db manual/f52fb3d37d68 2026-03-26 -->
### Articulation double isolation

Articulation double isolation

Nos articulations à double filtration, alliant caoutchouc naturel sur mesure à des composants métalliques et plastiques avancés, atténuent efficacement les vibrations du groupe motopropulseur et de la route. Optimisée pour les performances NVH et la fiabilité, elles offrent des matériaux personnalisables et une rentabilité maximale sans compromis sur la qualité.

Principaux bénéfices
Amélioration des performances NVH
Optimisation fonctionnelle : filtration et endurance
Caractéristiques techniques
Structures

Fonction :
L’élément principal en caoutchouc (EPC), composé principalement de caoutchouc naturel pour ses propriétés de déformabilité, est lié à au moins deux composants internes et externes métalliques ou composites, ainsi qu’à un composant additionnel généralement constitué d’un matériau à plus forte densité, intégré à l’EPC pour agir comme masse mobile.

Nos articulations élastiques à double isolation assurent une filtration accrue entre deux structures du véhicule.
Conception sur mesure, de la conception à la fin de vie.

Performances

Résistance mécanique

Conçu pour supporter les charges maximales
Plage de température : de -40°C à +110°C

Filtration

Entre -30 dB et -40 dB, optimisée par la double isolation

Poids

Optimisé grâce à la conception et à la sélection des matériaux

Respect de l’environnement

Résistant aux liquides : huile, liquide de refroidissement, produits chimiques, eau, humidité, etc.
Protection anticorrosion appliquée selon les besoins
Caractéristiques

Comportement :

Déflexion sous charge
Rigidité

Performances :

Amortissement
Fatigue
Mélange
Bénéfices
Réduction des vibrations
Réduction du bruit
Amélioration des performances
Optimisation des coûts
Longévité

<!-- materialized-from-db manual/22931f35d800 2026-03-26 -->
### Biellette de reprise de couple active

Suspension Moteur
Biellette de reprise de couple active

Conçue pour garantir un confort de conduite optimal, notre solution de filtration pour supports intègre des stratégies de contrôle actif permettant de générer des réponses dynamiques locales et précises en temps réel, sur une large plage de conditions de fonctionnement. Grâce à des configurations dédiées, le système s’adapte aux vibrations du groupe motopropulseur. Au-delà de la conception mécanique, nous développons des algorithmes, des composants électroniques et des logiciels embarqués pour permettre un comportement intelligent du système.

Principaux bénéfices
Amélioration des performances NVH en temps réel
Caractéristiques techniques
Structures

Fonction :
L’élément principal en caoutchouc (EPC), composé principalement de caoutchouc naturel pour ses propriétés de déformabilité, est lié à au moins deux composants internes et externes, métalliques ou composites.

Cet EPC est associé à un support principalement en métal ou en composite pour ses faibles propriétés de déformabilité et sa haute résistance. Sa structure est conçue pour annuler la raideur dynamique jusqu’à un certain niveau d’excitation. Dans ce cas, aucune vibration ni charge n’est transmise.

Ce produit gère le couple moteur et les mouvements de rotation tout en assurant le meilleur niveau de filtration.
Conception sur mesure, de la conception à la fin de vie.

Performances

Résistance mécanique

Conçu pour supporter les charges maximales
Plage de température : de -40°C à +110°C

Filtration

Amortissement élevé à basse fréquence pour un confort amélioré sur route dégradée, grâce à la conception et aux caractéristiques du fluide
Raideur dynamique nulle à haute fréquence pour un confort optimal au ralenti et sur route lisse, grâce à la conception et aux caractéristiques du fluide

Poids

Optimisé grâce à la conception et à la sélection des matériaux

Respect de l’environnement

Résistant aux liquides : huile, liquide de refroidissement, produits chimiques, eau, humidité, etc.
Protection anticorrosion appliquée selon les besoins
Caractéristiques

Comportement :

Déflexion sous charge
Rigidité
Annulation de la raideur dynamique

Performances :

Viscosité du fluide
Fatigue
Mélange
Activation en temps réel
Faible consommation
Bénéfices
Réduction des vibrations
Amélioration des performances
Confort
Réduction du bruit
Efficacité énergétique
Industries
Automobile
Produits associés
Toutes nos solutions Groupe motopropulseur

Voici aussi la version ultra épurée, centrée uniquement sur le contenu utile :

Biellette de reprise de couple active

Conçue pour améliorer le confort de conduite, cette solution de support moteur intègre un contrôle actif permettant de générer en temps réel des réponses dynamiques locales et précises sur une large plage de fonctionnement. Le système s’adapte aux vibrations du groupe motopropulseur et combine conception mécanique, algorithmes, électronique et logiciel embarqué pour assurer un comportement intelligent.

Principal bénéfice
Amélioration des performances NVH en temps réel
Caractéristiques techniques

Structure :
L’élément principal en caoutchouc naturel est lié à plusieurs composants métalliques ou composites. Il est associé à un support rigide conçu pour annuler la raideur dynamique jusqu’à un certain niveau d’excitation, afin de limiter la transmission des vibrations et des charges.
Le système gère le couple moteur et les mouvements de rotation tout en assurant un haut niveau de filtration.

Performances mécaniques :

Supporte les charges maximales
Température de fonctionnement : -40°C à +110°C

Filtration vibratoire :

Amortissement élevé à basse fréquence
Raideur dynamique nulle à haute fréquence

Autres points :

Poids optimisé
Résistance aux liquides et à l’humidité
Protection anticorrosion
Activation en temps réel
Faible consommation
Bénéfices
Réduction des vibrations
Amélioration des performances
Confort
Réduction du bruit
Efficacité énergétique

<!-- materialized-from-db manual/69487d02dcd6 2026-03-26 -->
### Suspension Moteur

Suspension Moteur
Support conventionnel

Notre solution de filtration pour supports est conçue pour atténuer les vibrations induites par le groupe motopropulseur et la route, garantissant des performances NVH optimales et une fiabilité à long terme sur toutes les plateformes de mobilité. Grâce à des options personnalisables en formulations de caoutchouc naturel, métaux et plastiques, elle offre une flexibilité inégalée en matière de conception et d’intégration, tout en étant entièrement optimisée pour l’efficacité économique sans compromis sur la qualité.

Principaux bénéfices
Optimisation des coûts
Durabilité et comportement ajustable
Conception bi-matière
Caractéristiques techniques
Structures

Fonction :
L’Élément Principal en Caoutchouc (EPC), composé principalement de caoutchouc naturel pour ses propriétés de déformabilité, est lié à au moins deux composants métalliques ou composites. Nos supports assurent la conformité entre deux structures du véhicule.
Conception sur mesure, de la conception jusqu'à la fin de vie.

Performances

Comportement :

Déflexion sous charge
Rigidité

Performances :

Amortissement
Fatigue
Mélange

Caractéristiques

Comportement :

Déflexion sous charge
Rigidité

Performances :

Amortissement
Fatigue
Bénéfices
Réduction des vibrations
Optimisation des coûts
Longévité
