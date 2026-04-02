---
category: alimentation
slug: soupape-d-aspiration-d-air-secondaire
title: Soupape d'aspiration d'air secondaire
pg_id: 1136
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
  last_enriched_by: skill:phase5-vague6
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Admettre l'air secondaire pour la depollution a froid
  must_be_true:
  - aspirer
  - admettre
  - controler
  must_not_contain:
  - freinage
  - climatisation
  - distribution
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - aspirer
  - admettre
  - controler
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
  - ❌ "repare l'injection"
  cost_range:
    min: 200
    max: 800
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  brands:
    premium:
    - Pierburg
    - Continental
    - Bosch
    standard:
    - Wahler
    - Valeo
    - Hella
    budget:
    - Meat & Doria
    - ERA
    - Hoffer
  quality_tiers:
  - tier: Origine constructeur
    description: Soupape d aspiration d air secondaire identique a la premiere monte, calibree pour le systeme de depollution
      a froid du vehicule.
  - tier: Equipementier qualite OE
    description: Equipementiers fournisseurs des constructeurs avec memes specifications de debit et d etancheite.
  - tier: Adaptable qualite reconnue
    description: Soupapes compatibles necessitant une verification de debit et d etancheite apres montage.
diagnostic:
  symptoms:
  - id: S1
    label: Voyant moteur avec code air secondaire
    severity: confort
  - id: S2
    label: Bruit anormal au demarrage a froid
    severity: confort
  - id: S3
    label: Ralenti irregulier a froid
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  quick_checks:
  - Voyant moteur avec code air secondaire ?
  - Bruit anormal au demarrage a froid ?
  - 'Observer : ralenti irregulier a froid ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Voyant moteur avec code air secondaire
  - Bruit anormal au demarrage a froid
  - Ralenti irregulier a froid
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '1136'
  intro_title: A quoi sert Soupape d'aspiration d'air secondaire ?
  risk_title: Pourquoi remplacer Soupape d'aspiration d'air secondaire a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
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
  - question: Comment choisir Soupape d'aspiration d'air secondaire compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Soupape d'aspiration d'air secondaire ?
    answer: En cas de voyant moteur avec code air secondaire ou de degradation mesurable, il faut controler rapidement avant
      panne secondaire.
  - question: Puis-je monter Soupape d'aspiration d'air secondaire sans verification atelier ?
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
doc_id: 08b4c76e-3d0a-515e-ab1f-964883737e9c
content_hash: sha256:9fa06064180ce875
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
  _source: contenu LLM — a revalider contre sources OEM
  _validation_status: pending_oem_validation
  _enriched_at: '2026-03-30'
  technical_notes:
    role: 'aspire l''air frais dans l''echappement par depression naturelle (systeme passif, sans pompe)'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    La soupape d'aspiration d'air secondaire est un composant du circuit de
    dépollution à froid des moteurs à essence. Son rôle est d'admettre l'air
    frais secondaire dans le système d'échappement pour favoriser la post-
    combustion des polluants lors des premières minutes de fonctionnement
    moteur, avant que le catalyseur n'atteigne sa température d'activation.
    Contrairement à la soupape d'air secondaire classique (qui contrôle le flux
    d'air depuis la pompe à air vers l'échappement), la soupape d'aspiration
    d'air secondaire est positionnée en amont du circuit et aspire l'air frais
    nécessaire à l'alimentation de ce système. Elle joue un rôle de clapet
    d'admission anti-retour qui s'ouvre à la commande de l'ECU moteur pour
    laisser entrer l'air, et se referme pour éviter tout reflux de gaz chauds
    vers la pompe ou le filtre à air. Le fonctionnement est coordonné avec la
    pompe à air secondaire et la soupape d'air secondaire de sortie : lors du
    démarrage à froid, l'ECU active la pompe, qui crée une dépression ouvrant la
    soupape d'aspiration, permettant ainsi l'aspiration d'air frais qui est
    ensuite poussé vers l'échappement pour la post-combustion des hydrocarbures
    non brûlés. Une soupape d'aspiration d'air secondaire défaillante — bloquée
    fermée ou présentant une fuite — perturbe l'ensemble du circuit d'air
    secondaire et génère des codes défauts liés au système antipollution (codes
    P04xx selon la nomenclature OBD). Elle peut conduire à un refus au contrôle
    technique antipollution si les émissions dépassent les seuils
    réglementaires.
  S2: >-
    La soupape d'aspiration d'air secondaire peut être victime de colmatage par
    dépôts carbonés, de rupture du clapet interne ou d'une défaillance
    électrique du circuit de commande. Les symptômes sont proches de ceux de la
    soupape d'air secondaire, mais présentent quelques spécificités. Voici les
    signaux à surveiller : - Voyant moteur allumé avec code défaut lié au
    système d'air secondaire : le calculateur moteur (ECU) détecte une anomalie
    dans le circuit et stocke un code P04xx lisible avec un outil de diagnostic
    OBD. - Bruit anormal au démarrage à froid : un sifflement, un clapotement ou
    un grondement sourd pendant les 2 à 3 premières minutes de fonctionnement
    peut signaler que la soupape ne s'ouvre ou ne se ferme pas correctement. -
    Ralenti irrégulier à froid : une soupape d'aspiration qui reste ouverte
    après la phase de chauffe perturbe le bilan d'air du moteur et crée des
    oscillations de régime au ralenti. - Odeur d'échappement plus marquée à
    froid : l'absence de post-combustion des hydrocarbures non brûlés due à un
    défaut d'aspiration d'air entraîne des émissions plus importantes et une
    odeur caractéristique en sortie d'échappement. - Performances réduites lors
    des premières minutes : si la soupape reste bloquée en position ouverte,
    elle crée une dépression parasite dans le circuit d'admission et peut
    déstabiliser la gestion moteur. - Refus au contrôle technique antipollution
    : un système d'air secondaire inopérant empêche le préchauffage rapide du
    catalyseur, augmentant les émissions de CO et d'HC au-delà des seuils légaux
    lors des mesures à froid.
  S3: >-
    La soupape d'aspiration d'air secondaire est une pièce technique dont la
    sélection doit être menée avec une identification précise du moteur et du
    circuit d'air secondaire. Voici les critères essentiels avant de commander :
    - Marque, modèle et code moteur : le code moteur (indiqué sur la plaque
    constructeur dans le compartiment moteur ou dans la documentation technique)
    est l'identifiant le plus fiable pour sélectionner la soupape exacte adaptée
    au circuit d'aspiration de votre motorisation. - Année de production du
    véhicule : le circuit d'air secondaire peut avoir été modifié en cours de
    production pour répondre aux évolutions des normes antipollution — vérifier
    les éventuelles variantes selon le millésime. - Code défaut OBD exact :
    noter le code P04xx précis permet de cibler le composant spécifique
    défaillant dans le circuit (soupape d'aspiration, soupape de sortie, pompe à
    air) et d'éviter de commander la mauvaise pièce. - Vérifier l'ensemble du
    circuit avant de commander : si le tuyau d'aspiration est fissuré ou si la
    pompe à air est défaillante, remplacer la soupape seule ne résoudra pas le
    code défaut. - Qualité des joints et du clapet interne : la soupape
    d'aspiration intègre un clapet anti-retour dont la souplesse et l'étanchéité
    sont critiques — une pièce de mauvaise qualité se colmate ou se déforme
    rapidement sous l'effet des cycles thermiques. - Référence OEM ou
    équipementier traçable : croiser la référence constructeur avec la référence
    de l'équipementier pour confirmer l'interchangeabilité mécanique et la
    compatibilité des raccords d'air. - Éviter les pièces sans référence
    identifiable : une soupape d'aspiration non conforme peut générer des fuites
    d'air perturbant le circuit et créant des codes défauts persistants après
    remplacement. Pour aller plus loin : consultez notre guide d'achat soupape
    d'aspiration d'air secondaire — comparatif marques, critères de choix et
    prix.
  S4_DEPOSE: >-
    Le remplacement de la soupape d'aspiration d'air secondaire nécessite un
    accès au compartiment moteur et un outil de diagnostic OBD pour valider la
    réparation. La procédure est accessible pour un mécanicien expérimenté.
    Voici les étapes générales : - Connecter un outil de diagnostic OBD et
    relever tous les codes défauts présents — noter particulièrement les codes
    P04xx du circuit d'air secondaire pour les effacer après l'intervention. -
    Laisser refroidir le moteur complètement — la soupape est positionnée à
    proximité du collecteur d'échappement, qui reste chaud longtemps après
    l'arrêt moteur. - Localiser la soupape d'aspiration d'air secondaire sur le
    moteur : elle est généralement positionnée sur le côté du moteur, reliée à
    la pompe à air par un tuyau souple et connectée électriquement au circuit de
    commande de l'ECU. - Déconnecter le connecteur électrique de la soupape si
    elle est commandée électroniquement, en appuyant sur la languette de
    déverrouillage sans tirer sur les fils. - Déconnecter le ou les tuyaux d'air
    reliant la soupape à la pompe à air et au circuit d'échappement — noter les
    sens de connexion et inspecter l'état des tuyaux (fissures, durcissement,
    colmatage). - Retirer les vis ou colliers de fixation de la soupape sur son
    support — appliquer du dégrippant si les fixations sont corrodées. -
    Extraire l'ancienne soupape et nettoyer les portées de raccordement des
    tuyaux et les surfaces de joint. - Installer la nouvelle soupape avec des
    joints neufs, reconnecter les tuyaux dans le bon sens, brancher le
    connecteur électrique, puis effacer les codes défauts et effectuer un test à
    froid pour vérifier la disparition du voyant moteur.
  S4_REPOSE: >-
    Après avoir fixé la soupape d'aspiration d'air secondaire neuve, la repose
    des connexions pneumatiques et électriques doit être réalisée avec soin.
    L'effacement des codes défaut OBD et un test à froid du démarrage sont
    indispensables pour valider la réparation. - Positionner la soupape neuve
    dans son logement en orientant les raccords d'entrée et de sortie d'air dans
    le bon sens. Un montage inversé bloque le flux et génère immédiatement un
    code défaut. - Fixer les vis ou le collier de maintien au couple spécifié.
    La soupape d'aspiration est souvent montée sur un support caoutchouc anti-
    vibratoire — vérifier l'état de ce support avant la repose. - Brancher la
    durite d'aspiration côté amont (depuis le filtre à air ou la boîte à air)
    avec le collier serré à fond mais sans coincer la paroi du tuyau. - Brancher
    la durite de refoulement côté aval vers la pompe à air ou le clapet de non-
    retour. Contrôler l'absence de pliure ou de vrille susceptible de réduire le
    débit d'air. - Reconnecter le connecteur électrique si la soupape est à
    commande électromagnétique. Enfoncer fermement jusqu'au clic et tirer
    légèrement pour vérifier le verrouillage. - Reposer les caches et habillages
    moteur déposés pour accéder à la soupape, dans l'ordre inverse du démontage.
    - Effacer les codes défaut à la valise OBD — les codes liés au système d'air
    secondaire (P0410, P0411, P0413, P0414) doivent disparaître et ne pas
    revenir après 2 cycles de conduite à froid. - Effectuer un premier démarrage
    à froid complet : surveiller le comportement au ralenti pendant la phase de
    chauffe et confirmer l'absence de bruit aspiratif anormal ou de voyant
    moteur.
  S5: >-
    Le diagnostic et le remplacement de la soupape d'aspiration d'air secondaire
    présentent plusieurs pièges techniques récurrents. Voici les cinq erreurs à
    éviter pour garantir une réparation durable : - Confondre la soupape
    d'aspiration avec la soupape d'air secondaire de sortie : ces deux
    composants font partie du même circuit mais sont positionnés différemment
    sur le moteur — identifier précisément le composant défaillant via le code
    défaut moteur avant de commander la pièce de remplacement. - Négliger
    l'inspection du tuyau d'aspiration : le tuyau reliant la pompe à air à la
    soupape d'aspiration est en caoutchouc et se fissure avec les cycles
    thermiques — une fuite sur ce tuyau génère exactement les mêmes codes
    défauts qu'une soupape défaillante et doit être remplacé en même temps. - Ne
    pas effacer les codes défauts après l'intervention : le voyant moteur
    restera allumé tant que les codes ne sont pas effacés avec l'outil OBD —
    cette étape est obligatoire pour valider la réparation et permettre au
    calculateur de re-tester le circuit. - Inverser le sens de montage de la
    soupape : la soupape d'aspiration intègre un clapet anti-retour qui doit
    être orienté dans le bon sens du flux d'air — un montage inversé bloque
    complètement le circuit ou crée des reflux de gaz chauds vers la pompe. -
    Intervenir sans diagnostiquer l'ensemble du système d'air secondaire :
    remplacer uniquement la soupape d'aspiration alors que la pompe à air ou la
    soupape de sortie sont également défaillantes conduira à une récidive
    immédiate du code défaut et à une deuxième intervention inutile.
  S6: >-
    Après l'installation de la nouvelle soupape d'aspiration d'air secondaire,
    une série de contrôles fonctionnels et électroniques doit être réalisée pour
    valider la réparation et confirmer le retour à la normale du système
    antipollution : - Effacer les codes défauts avec l'outil OBD et vérifier que
    le voyant moteur s'éteint correctement — si le voyant se rallume dans les
    minutes qui suivent, une autre cause est à investiguer dans le circuit d'air
    secondaire. - Effectuer un démarrage à froid complet et écouter
    attentivement pendant les 2 à 3 premières minutes : aucun sifflement, aucun
    claquement ni bruit d'air anormal ne doit être perceptible depuis le circuit
    d'aspiration. - Vérifier l'étanchéité des raccords de tuyaux en passant la
    main près des jonctions moteur chaud (à distance de sécurité) pour détecter
    tout courant d'air chaud caractéristique d'une fuite résiduelle. - Contrôler
    le sens du clapet anti-retour en vérifiant que l'air circule bien dans le
    sens pompe vers échappement et non dans le sens inverse — si le circuit est
    accessible, un test de souffle à la main peut confirmer l'orientation. -
    Réaliser deux à trois cycles de démarrage à froid sur plusieurs jours et
    vérifier que le voyant moteur reste éteint — le calculateur lance ses
    autodiagnostics du circuit d'air secondaire uniquement lors des démarrages à
    froid, la validation peut prendre 2 à 3 cycles complets.
  S7: >-
    La soupape d'aspiration d'air secondaire fait partie d'un circuit de
    dépollution complet. Plusieurs pièces de ce circuit peuvent générer des
    symptômes identiques (voyant moteur, code air secondaire, bruit au démarrage
    à froid). Vérifier l'ensemble du circuit avant de cibler uniquement cette
    soupape. - Soupape d'air secondaire (clapet de contrôle) — clapet situé côté
    échappement qui travaille en tandem avec la soupape d'aspiration. Les deux
    pièces vieillissent simultanément et un test d'activation individuelle à la
    valise permet de distinguer laquelle est défaillante. - Pompe à air
    secondaire — génère la pression d'air envoyée dans le circuit. Si la pompe
    est grippée ou ne s'active pas à froid, aucune des deux soupapes ne peut
    fonctionner correctement malgré leur remplacement. - Durites du circuit
    d'air secondaire — tuyaux en caoutchouc ou plastique soumis aux cycles
    thermiques. Microfissures ou déboîtements spontanés créent des fuites d'air
    à l'origine de codes défaut intermittents. - Relais de pompe à air —
    commande l'alimentation électrique de la pompe. Un relais défaillant simule
    exactement une panne de soupape d'aspiration : vérifier en priorité avec un
    multimètre avant de commander les pièces mécaniques. - Filtre à air — un
    filtre colmaté réduit le débit d'aspiration disponible pour le système d'air
    secondaire et peut provoquer un ralenti irrégulier à froid sans que la
    soupape soit en cause. À contrôler lors de tout diagnostic du circuit.
  S8: >-
    Quelle est la différence entre la soupape d'aspiration d'air secondaire et
    la soupape d'air secondaire ? Ces deux pièces font partie du même circuit
    mais ont des rôles distincts. La soupape d'aspiration (cette gamme) est
    positionnée en entrée du circuit et admet l'air frais extérieur vers la
    pompe à air. La soupape d'air secondaire (gamme soupape-d-air-secondaire)
    est positionnée en sortie et injecte cet air dans le collecteur
    d'échappement. En cas de panne, il est important de diagnostiquer
    précisément laquelle est défaillante avant de commander, car elles ont des
    références et des positions différentes sur le moteur. Le code défaut peut-
    il être causé par un simple tuyau fissuré plutôt que par la soupape elle-
    même ? Oui, et c'est une cause fréquemment sous-estimée. Le tuyau souple
    reliant la pompe à air à la soupape d'aspiration est en caoutchouc qui
    durcit et se fissure avec les cycles thermiques. Une micro-fissure sur ce
    tuyau crée une fuite d'air qui perturbe le débit mesuré par le calculateur,
    générant un code défaut identique à celui d'une soupape défaillante.
    Inspecter systématiquement l'état de tous les tuyaux du circuit avant de
    remplacer la soupape. Ce système d'air secondaire est-il obligatoire pour le
    contrôle technique ? Un véhicule équipé d'origine de ce système doit le
    maintenir fonctionnel pour passer le contrôle technique. Si le voyant moteur
    est allumé à cause d'un code défaut du circuit d'air secondaire, cela
    constitue un motif de refus. De plus, les émissions à froid peuvent dépasser
    les seuils réglementaires si le catalyseur ne préchauffe pas assez vite,
    entraînant également un refus au test antipollution. Comment choisir entre
    remplacer la soupape d'aspiration ou l'ensemble du kit d'air secondaire
    complet ? Si seule la soupape d'aspiration est défaillante et que la pompe à
    air et les tuyaux sont en bon état, le remplacement de la soupape seule
    suffit. En revanche, si le véhicule dépasse 150 000 km ou si la pompe à air
    montre des signes de fatigue (bruit de roulement, débit insuffisant),
    remplacer l'ensemble du kit d'un coup est souvent plus économique à long
    terme que d'intervenir en plusieurs fois sur chaque composant séparément.
---

# Soupape d'aspiration d'air secondaire - Guide Diagnostic Complet

## Fonction et Rôle

Admettre l'air secondaire pour la depollution a froid

**Actions principales:** aspirer, admettre, controler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant moteur avec code air secondaire
- bruit anormal au demarrage a froid
- ralenti irregulier a froid

## Procédure de Diagnostic

Pour diagnostiquer un problème de soupape d'aspiration d'air secondaire:

1. **Inspection visuelle** - Examiner l'état du soupape d'aspiration d'air secondaire
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- intercooler
- pompe-a-air
- soupape-d-air-secondaire

## Critères de Compatibilité

Pour commander le bon soupape d'aspiration d'air secondaire, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare l'injection"

## FAQ

**Comment choisir Soupape d'aspiration d'air secondaire compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Soupape d'aspiration d'air secondaire ?**
En cas de voyant moteur avec code air secondaire ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Soupape d'aspiration d'air secondaire sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
