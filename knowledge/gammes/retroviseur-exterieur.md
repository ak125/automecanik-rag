---
category: accessoires
slug: retroviseur-exterieur
title: Rétroviseur extérieur
pg_id: 50
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-03-29'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:rag-enrich-from-web-corpus
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Permet la vision arrière et latérale
  must_be_true:
  - reflechir
  - montrer
  - permettre la vision
  must_not_contain:
  - injection
  - freinage
  - distribution
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - reflechir
  - montrer
  - permettre la vision
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
  - ❌ "meilleure visibilité garantie"
  cost_range:
    min: 50
    max: 200
    currency: EUR
    unit: coque complète
    source: catalogue automecanik
  brands:
    premium:
    - Magna Mirrors
    - Ficosa
    - SMR
    standard:
    - Hagus/DAPA
    - ALKAR
    - TYC
    budget:
    - VAN WEZEL
    - PRASCO
    - BLIC
  quality_tiers:
  - tier: Origine constructeur (OE/OES)
    description: Retroviseur identique a la premiere monte. Toutes les fonctions d'origine preservees (rabattage electrique,
      chauffant, camera, repetiteur).
  - tier: Equivalent OE (qualite premiere monte)
    description: Retroviseur de qualite equivalente. Fonctions principales conservees (reglage electrique, chauffant). Finition
      correcte.
  - tier: Adaptable (qualite atelier courant)
    description: Retroviseur compatible. Verifier la presence des fonctions requises (chauffant, repetiteur, rabattage) avant
      commande.
diagnostic:
  symptoms:
  - id: S1
    label: Miroir casse fissure ou decolle
    severity: confort
  - id: S2
    label: Coque de retroviseur cassee choc accrochage
    severity: confort
  - id: S3
    label: Reglage electrique inoperant ou lent
    severity: confort
  - id: S4
    label: Degivrage du miroir qui ne fonctionne plus
    severity: confort
  - id: S5
    label: Retroviseur rabattable bloque ou qui vibre
    severity: immobilisation
  - id: S6
    label: Repetiteur de clignotant integre grille
    severity: confort
  - id: S7
    label: Miroir fissure ebreche deformant image
    severity: confort
  - id: S8
    label: Bruit claquement vibration retroviseur vent
    severity: confort
  - id: S9
    label: Odeur plastique brule moteur electrique
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - verifier equilibrage et fixations
  quick_checks:
  - 'Observer : miroir casse fissure ou decolle ?'
  - 'Observer : coque de retroviseur cassee choc accrochage ?'
  - 'Observer : reglage electrique inoperant ou lent ?'
  - 'Observer : degivrage du miroir qui ne fonctionne plus ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Miroir casse fissure ou decolle
  - Coque de retroviseur cassee choc accrochage
  - Reglage electrique inoperant ou lent
  - Degivrage du miroir qui ne fonctionne plus
  - Retroviseur rabattable bloque ou qui vibre
  - Repetiteur de clignotant integre grille
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '50'
  intro_title: A quoi sert Rétroviseur extérieur ?
  risk_title: Pourquoi remplacer Rétroviseur extérieur a temps ?
  risk_explanation: '**Pièce HS** - Le rétroviseur extérieur peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le rétroviseur extérieur peut être hors service et nécessiter un remplacement'
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: Rétroviseur OE ou adaptable ?
    answer: Les rétroviseurs adaptables (Hagus, ALKAR, VAN WEZEL) sont de qualité correcte pour un usage courant. Pour un
      rétro avec nombreuses fonctions (rabattable, chauffant, caméra), l'OE est plus fiable.
  - question: Comment savoir si mon rétroviseur est HS ?
    answer: Miroir cassé ou décollé, coque fissurée, réglage électrique inopérant, dégivrage qui ne fonctionne plus, rabattage
      bloqué, répétiteur grillé.
  - question: Tous les combien changer le rétroviseur ?
    answer: Pas de périodicité. Le rétroviseur se change uniquement si cassé (choc, vandalisme) ou si le mécanisme électrique
      est défaillant.
  - question: Peut-on changer un rétroviseur soi-même ?
    answer: 'Oui. Pour le miroir seul : déclipser l''ancien, clipser le nouveau. Pour la coque complète : déposer le cache
      intérieur de portière, débrancher, dévisser. 15-45 min.'
  - question: Quelle erreur éviter avec le rétroviseur ?
    answer: Forcer sur un rétroviseur rabattable électrique bloqué. Le mécanisme interne est fragile et se casse facilement.
      Vérifiez d'abord le fusible et le connecteur.
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
doc_id: 6ef9fa0a-b808-5455-94f4-2aab050d1292
content_hash: sha256:8dfdef4372d8cc7d
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
  area: Sur le vehicule (position variable selon modele)
  access: Consulter la revue technique du vehicule
  adjacent_parts:
  - pieces adjacentes du meme systeme
installation:
  difficulty: variable
  time: consulter revue technique
  tools:
  - outillage standard
  prerequisite: Consulter la procedure constructeur
phase5_enrichment:
  _source: gpa26.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 2
  technical_notes:
    val_4_a: '4 a'
    val_503_a: '503 a'
    val_59_a: '59 a'
    val_6_a: '6 a'
    val_70_a: '70 a'
    val_988_a: '988 a'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le rôle du rétroviseur extérieur est donner à l'utilisateur duvéhicule
    d'apercevoir l'environnement extérieur (ce qui passe à coté etderrière la
    voiture). Sur un véhicule en dispose de deux rétroviseur extérieurgauche et
    droite, mais sur certains anciens modèles en n'ont qu'un. Seulementle
    rétroviseur extérieur gauche est obligatoire. Généralement un
    rétroviseurextérieur se compose en d'une glace rétroviseur, d'un boîtier de
    rétroviseur etd'un support de fixation à la carrosserie. Il existe plusieurs
    types de rétroviseurs extérieurs selonle type de réglage de ce dernier : -
    Rétroviseur extérieur manuel qui serègle directement à la main à l'extérieur
    du véhicule. - Rétroviseur extérieur mécanique quise règle de l'intérieur du
    véhicule grâce à un système d'articulation. - Rétroviseur extérieur
    électrique quise règle de l'intérieur du véhicule par l'intermédiaire d'un
    bouton électrique. En savoir plus : rétroviseur extérieur — définition et
    rôle mécanique 🚨 Bruit Rétroviseur extérieur : causes et diagnostic
  S2: >-
    Un rétroviseur extérieur doit être remplacé si vous remarquez qu'il estbrisé
    ou détérioré à cause d'un accident ou si le rétroviseur de votre
    voiturepercute celui du véhicule croisé dans la route. Si vous roulez avec
    unrétroviseur extérieur cassé cela provoque un manque de visibilité
    important puisque vousn'aller rien voir des deux côtés du véhicule.
    Diagnostic complet : identifier une panne de rétroviseur extérieur
  S3: >-
    Le rétroviseur extérieur est une pièce de carrosserie dont les variantes se
    multiplient avec les équipements électriques embarqués : un même modèle de
    véhicule peut exister en version miroir fixe, réglage électrique, dégivrage,
    rabattement électrique, caméra intégrée ou répétiteur de clignotant.
    Sélectionner un rétroviseur incomplet par rapport à la version d'origine
    prive le conducteur de fonctions de sécurité homologuées. - Côté conducteur
    (gauche) ou passager (droit) et marché — La conception optique du miroir
    (plan ou légèrement convexe) diffère selon le côté et la réglementation du
    marché. Un rétroviseur passager européen est convexe pour élargir le champ
    visuel ; un modèle destiné au marché américain peut être plan. Ne pas
    substituer un côté à l'autre. - Type de commande : manuelle, électrique ou
    électrique à mémoire — Le commutateur intérieur doit correspondre au type de
    réglage : mécanique à câble Bowden (2 axes, traction directe) ou électrique
    à moteur (2 ou 4 fils de commande + masse). Les modèles à mémoire de
    position ajoutent un capteur angulaire et un connecteur supplémentaire. -
    Fonction de dégivrage et câblage chauffant — Le miroir dégivrant intègre un
    réseau de fils résistifs collés sur le verre. Un miroir sans dégivrage monté
    à la place d'un miroir chauffant d'origine rend le dégivrage inopérant en
    hiver, ce qui peut constituer un manquement aux règles du code de la route
    en conditions givrantes. - Rabattement électrique : moteur de repliage
    intégré — Les rétroviseurs à rabattement électrique contiennent un
    motoréducteur et une came de déverrouillage. Ce sous-ensemble n'est pas
    présent sur les modèles à rabattement manuel. La connexion requiert un
    câblage supplémentaire de 2 à 4 fils selon la marque. - Répétiteur de
    clignotant intégré — La présence d'un répétiteur LED ou ampoule dans la
    coque est obligatoire sur tous les véhicules homologués après 2007 dans de
    nombreux pays européens. Commander un rétroviseur sans répétiteur sur un
    véhicule qui en est équipé d'origine crée une non-conformité au contrôle
    technique. - Angle de la base et point de fixation sur la porte — La forme
    de la base (triangulaire, ronde, avec ou sans cache-montant) et l'entraxe
    des vis de fixation (généralement 3 vis) doivent correspondre exactement à
    la platine de porte. Une base légèrement différente crée un jeu qui génère
    des vibrations à haute vitesse. - Teinte de la glace : neutre, athermique
    (bleutée) ou grand angle inférieur — Certains modèles haut de gamme
    intègrent une zone grand angle en bas du miroir passager et une glace
    athermique antiéblouissement côté conducteur. Ces variantes optiques sont
    identifiables par la teinte de la glace et ne sont pas substituables entre
    elles sans modification du champ de vision. Pour aller plus loin : consultez
    notre guide d'achat rétroviseur extérieur — comparatif marques, critères de
    choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Rétroviseur extérieur pour
    connaître les spécifications. Note : leremplacement d'un rétroviseur
    extérieur change d'un véhicule à un autre selonla spécificité de ce dernier
    (le mode de réglage). - Débranchez la batterie. - Démontez la garniture de
    porte ou le cache situé à l'intérieur dans le coinde la vitre suivant la
    position de la molette de réglage du rétroviseurextérieur. - Si le système
    de réglage du rétroviseur extérieur est mécanique : séparerla molette de
    réglage soit en la dévissant, soit en la déclipsant. - Si le système de
    réglage du rétroviseur extérieur est électrique :débrancher le connecteur de
    la commande de réglage. - Desserrer les vis de fixation du rétroviseur
    extérieure à la porte duvéhicule. - Démontez avec précaution le rétroviseur
    extérieur de son logement.
  S4_REPOSE: >-
    Remontage du rétroviseur extérieur — procédure selon type de fixation Le
    rétroviseur extérieur peut être remplacé en totalité (coque + mécanisme) ou
    partiellement (miroir seul ou coque seule). Chaque niveau d'intervention a
    sa propre procédure. Remplacement du miroir seul (sans démontage de la
    portière) - Déclipser l'ancien miroir — Glisser un tissu épais (chiffon
    plié) entre le miroir et la coque pour protéger les surfaces. Appuyer le
    miroir vers le bas et l'extérieur pour déclipser les 2 à 4 clips plastiques
    de maintien. Sur certains modèles avec dégivrage, déconnecter le connecteur
    chauffant avant de retirer le miroir. - Mise en place du miroir neuf —
    Vérifier que la référence du miroir correspond bien au modèle (côté
    gauche/droit, présence ou absence de dégivrage). Engager d'abord le bord
    inférieur du miroir, puis appuyer progressivement sur les clips supérieurs
    jusqu'à l'enclenchement complet. Chaque clip doit produire un clic franc. -
    Test de réglage et du dégivrage — Tester le réglage électrique dans les 4
    directions. Si le rétroviseur est équipé du dégivrage, vérifier son
    fonctionnement avec la touche lunette arrière. Remplacement de l'ensemble
    rétroviseur (coque + mécanisme) - Protection de la vitre et dépose du cache
    intérieur — Mettre le véhicule en position vitre levée. Insérer un cale-
    vitre en mousse dans la fente de porte pour éviter que la vitre ne tombe.
    Déposer le cache plastique intérieur situé dans le coin de la vitre
    (généralement 1 vis cachée sous un enjoliveur, puis clips). - Déconnexion
    électrique — Débrancher le faisceau électrique du rétroviseur (connecteur
    multi-broches pour réglage électrique, chauffage et répétiteur de
    clignotant). Repérer la position des fils si le connecteur n'est pas
    détrompé. - Dépose des vis de fixation — Les vis de fixation du pied de
    rétroviseur (généralement 2 à 3 vis Torx ou hexagonales, M6 ou M8) sont
    accessibles derrière le cache intérieur retiré. Les retirer et maintenir le
    rétroviseur d'une main pour éviter qu'il ne tombe. - Vérification du
    rétroviseur neuf — Contrôler que le rétroviseur neuf présente la même
    configuration de connexion, les mêmes trous de fixation et le bon côté
    (G/D). Sur les rétroviseurs avec clignotant intégré, vérifier le câblage de
    la LED de répétiteur (couleur des fils ou schéma du connecteur). - Remontage
    et serrage — Positionner le rétroviseur neuf dans son logement, aligner les
    trous de fixation, visser les fixations à la main puis au couple (8-12 Nm).
    Sur-serrer les vis de rétroviseur fragilise le pied de fixation plastique de
    la portière. - Reconnexion et remontage du cache — Reconnecter le faisceau
    électrique (clips enclenchés). Remettre le cache intérieur en positionnant
    d'abord les clips du bas, puis appuyer jusqu'au cliquetis des clips du haut.
    Serrer la vis de fixation. - Tests électriques et mécaniques — Rebrancher la
    batterie. Tester : réglage électrique (4 directions), dégivrage, répétiteur
    de clignotant, et rabattage si présent. Effectuer un trajet à 80 km/h pour
    confirmer l'absence de vibration ou de claquement. ✅ Après remontage,
    vérifiez les spécifications dans la fiche technique Rétroviseur extérieur.
  S5: >-
    Erreurs frequentes avec le retroviseur exterieur : - Ne pas verifier le cote
    (gauche/droite) et les options (degivrant, rabattable electrique, clignotant
    integre) avant achat — les references different selon l'equipement du
    vehicule- Forcer le demontage du cache interieur de portiere — les clips
    plastique sont fragiles et cassent facilement, utiliser un outil de
    demontage adapte- Oublier de debrancher le connecteur electrique avant de
    retirer le retroviseur — le fil se tend et arrache le connecteur de la
    portiere- Confondre un probleme de miroir avec un defaut de moteur de
    reglage — le miroir seul est remplacable sans changer l'ensemble du
    retroviseur- Ignorer un retroviseur casse ou manquant — c'est un motif de
    contre-visite au controle technique (cote conducteur obligatoire)
  S6: >-
    Après le montage d'un rétroviseur extérieur, plusieurs vérifications
    s'imposent pour garantir la sécurité de conduite. Elles portent sur la
    fixation mécanique, le réglage optique, les fonctions électriques et
    l'étanchéité du passage de câbles. Un rétroviseur mal fixé ou mal orienté
    constitue un risque direct : angle mort non couvert, vibrations à haute
    vitesse ou perte du rétroviseur sur autoroute. - Contrôle de la fixation sur
    la portière : vérifier que les 2 à 3 vis du pied de rétroviseur (M6 ou M8
    selon modèle) sont serrées au couple constructeur, généralement 8 à 12 N.m.
    Un sous-serrage provoque des vibrations rendant le miroir inexploitable dès
    80 km/h. Contrôler également que le joint d'étanchéité entre le pied et la
    portière est correctement positionné pour éviter les infiltrations d'eau
    dans la portière. - Vérification de l'étanchéité du connecteur : s'assurer
    que le passe-câbles traversant la portière est correctement repositionné
    avec son joint torique ou son passe-fil en caoutchouc. Une étanchéité
    défaillante entraîne à terme la corrosion du connecteur et des
    dysfonctionnements électriques intermittents, notamment en période
    hivernale. - Réglage de l'angle du miroir : depuis la position de conduite
    normale, régler le miroir pour voir le flanc arrière du véhicule sur 10 à 15
    % de la largeur du miroir, avec le sol visible à partir de 10 m derrière le
    véhicule. Pour les modèles à réglage électrique, tester les 4 directions
    (haut, bas, gauche, droite) — le moteur doit fonctionner sans à-coups ni
    blocage en fin de course. - Test du dégivrage du miroir : activer la lunette
    arrière dégivrante (souvent couplée au dégivrage des rétroviseurs). Après 2
    à 3 minutes de fonctionnement, le miroir doit être tiède au toucher (40 à 50
    °C en surface). L'absence de montée en température indique un fil chauffant
    coupé ou un connecteur mal encliqueté. Mesurer la résistance de l'élément
    chauffant au multimètre : valeur typique entre 10 et 30 ohms selon modèle. -
    Vérification du répétiteur de clignotant intégré : si le rétroviseur
    comporte un répétiteur latéral LED ou à ampoule, activer les clignotants
    gauche et droit pour vérifier le clignotement synchrone avec les clignotants
    de carrosserie. Un clignotement absent ou désynchronisé signale un
    connecteur mal encliqueté ou une LED défectueuse. Vérifier aussi l'absence
    de code défaut au diagnostic (ampoule grillée détectée par le BCM). - Test
    du rabattement électrique : pour les modèles avec rabattement motorisé,
    actionner la commande depuis l'habitacle. Le rétroviseur doit se rabattre et
    se déployer sans blocage ni bruit mécanique anormal, et s'immobiliser à 90°
    en position déployée. Un arrêt en position intermédiaire signale un obstacle
    mécanique ou un pignon endommagé dans le réducteur. Vérifier également la
    fonction de rabattement automatique au verrouillage si le véhicule en est
    équipé. - Test anti-éblouissement automatique : sur les rétroviseurs à
    miroir électrochrome, vérifier que la fonction anti-éblouissement fonctionne
    en obscurcissant le miroir lorsqu'une source lumineuse intense est détectée
    par le capteur arrière. Le miroir doit revenir à sa teinte normale en 5 à 10
    secondes après suppression de la source lumineuse. - Essai routier de
    validation : lors du premier trajet, rouler jusqu'à 100-110 km/h. Aucun
    claquement, sifflement ni vibration parasite ne doit provenir du
    rétroviseur. Un bruit aérodynamique anormal indique un jeu excessif dans les
    clips de fixation de la coque ou un mauvais plaquage du joint de pied.
    Vérifier aussi la stabilité de l'image dans le miroir sur route dégradée.
  S7: >-
    Le rétroviseur extérieur est un ensemble complexe intégrant plusieurs sous-
    composants indépendants. Selon la panne identifiée (miroir cassé,
    motorisation défaillante, dégivrage hors service, répétiteur de clignotant
    grillé), certains éléments peuvent être remplacés individuellement sans
    changer tout le rétroviseur. Voici les pièces associées à contrôler
    systématiquement. - Glace de rétroviseur (miroir seul) — Si seul le miroir
    est fissuré, cassé ou décollé sans dommage sur la coque ni le mécanisme
    électrique, la glace peut être remplacée seule. Elle se déclipse ou se colle
    selon le modèle. Nettement moins coûteux qu'un rétroviseur complet, vérifier
    la disponibilité de la glace seule pour votre véhicule. - Coque de
    rétroviseur (couvercle extérieur) — En cas de choc avec dommage esthétique
    uniquement sur la coque (le mécanisme et le miroir sont intacts), la coque
    se remplace indépendamment sur la plupart des modèles. Elle se clipse sur le
    châssis du rétroviseur. Vérifier la correspondance de couleur (coque prête à
    peindre ou peinte en teinte d'origine). - Moteur électrique de réglage du
    miroir — Si le réglage électrique du miroir est inopérant (miroir figé ou se
    déplace saccadé), le moteur de réglage peut être défaillant. Tester d'abord
    le fusible correspondant et le connecteur électrique. Si le moteur est hors
    service, son remplacement seul est possible sur certains modèles mais
    nécessite souvent le démontage complet du rétroviseur. - Mécanisme de
    rabattage électrique — Le module de rabattage (moteur + engrenage) peut
    tomber en panne indépendamment du miroir. Symptôme typique : rétroviseur qui
    ne se replie plus, ou qui se replie partiellement et reste bloqué. Vérifier
    d'abord le fusible et contrôler que l'axe de pivot n'est pas cassé. -
    Répétiteur de clignotant intégré — La plupart des rétroviseurs modernes
    intègrent un répétiteur LED ou à ampoule. Un répétiteur grillé constitue un
    défaut signalé au contrôle technique. Il peut être remplacé seul (ampoule ou
    module LED) sans changer le rétroviseur complet. Vérifier le type de
    connecteur. - Élément dégivrant — La résistance de dégivrage intégrée dans
    le miroir peut brûler. Si le dégivrage ne fonctionne plus, vérifier d'abord
    le fusible dédié (souvent partagé avec la lunette arrière) avant d'envisager
    un remplacement. Sur certains modèles, le dégivrage est intégré dans la
    glace de rétroviseur et non remplaçable séparément. - Connecteur et faisceau
    électrique — Un connecteur oxydé ou un fil rompu dans le faisceau du
    rétroviseur peut simuler une panne de motorisation ou de dégivrage. Avant
    tout remplacement coûteux, vérifier la continuité électrique du connecteur
    avec un multimètre.
  S8: >-
    Comment choisir Rétroviseur extérieur compatible avec mon vehicule
    ?Renseignez marque, modele, type moteur et annee, puis verifiez la reference
    Quand remplacer Rétroviseur extérieur ?En cas de miroir casse fissure ou
    decolle ou de degradation mesurable, Puis-je monter Rétroviseur extérieur
    sans verification atelier ?Le montage peut exiger controles de couple,
    alignement et references.
  META: >-
    {"meta_title":"Rétroviseur Extérieur : Guide Remplacement |
    AutoMecanik","meta_description":"Miroir cassé, coque fissurée ou réglage
    électrique défaillant ? Découvrez quand et comment remplacer votre
    rétroviseur extérieur sur AutoMecanik."}
---

# Rétroviseur extérieur - Guide Diagnostic Complet

## Fonction et Rôle

Permet la vision arrière et latérale

**Actions principales:** reflechir, montrer, permettre la vision

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Retroviseur rabattable bloque ou qui vibre**
  retroviseur rabattable bloque ou qui vibre

### 🟠 Symptômes de Dégâts Potentiels

- **Miroir casse fissure ou decolle**
  miroir casse fissure ou decolle
- **Coque de retroviseur cassee choc accrochage**
  coque de retroviseur cassee choc accrochage
- **Bruit claquement vibration retroviseur vent**
  bruit claquement vibration retroviseur vent

### 🟢 Autres Symptômes

- reglage electrique inoperant ou lent
- degivrage du miroir qui ne fonctionne plus
- repetiteur de clignotant integre grille
- miroir fissure ebreche deformant image
- odeur plastique brule moteur electrique

## Procédure de Diagnostic

Pour diagnostiquer un problème de rétroviseur extérieur:

1. **Inspection visuelle** - Examiner l'état du rétroviseur extérieur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le rétroviseur extérieur peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- bouton-de-retroviseur

## Critères de Compatibilité

Pour commander le bon rétroviseur extérieur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleure visibilité garantie"

## FAQ

**Rétroviseur OE ou adaptable ?**
Les rétroviseurs adaptables (Hagus, ALKAR, VAN WEZEL) sont de qualité correcte pour un usage courant. Pour un rétro avec nombreuses fonctions (rabattable, chauffant, caméra), l'OE est plus fiable.

**Comment savoir si mon rétroviseur est HS ?**
Miroir cassé ou décollé, coque fissurée, réglage électrique inopérant, dégivrage qui ne fonctionne plus, rabattage bloqué, répétiteur grillé.

**Tous les combien changer le rétroviseur ?**
Pas de périodicité. Le rétroviseur se change uniquement si cassé (choc, vandalisme) ou si le mécanisme électrique est défaillant.

**Peut-on changer un rétroviseur soi-même ?**
Oui. Pour le miroir seul : déclipser l'ancien, clipser le nouveau. Pour la coque complète : déposer le cache intérieur de portière, débrancher, dévisser. 15-45 min.

**Quelle erreur éviter avec le rétroviseur ?**
Forcer sur un rétroviseur rabattable électrique bloqué. Le mécanisme interne est fragile et se casse facilement. Vérifiez d'abord le fusible et le connecteur.
