---
category: alimentation
slug: soupape-reaspiration-des-gaz-d-echappement
title: Soupape réaspiration des gaz d'échappement
pg_id: 1137
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
  role: Readmettre une partie des gaz d'echappement dans l'admission
  must_be_true:
  - recycler
  - readmettre
  - doser
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
  - injecteur
  - pompe-a-injection
  - corps-papillon
  - debitmetre-d-air
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de compatibilite
    pour confirmer Soupape réaspiration des gaz d'échappement.
  - Verifier la reference OE ou equivalence constructeur pour le vehicule exact
  - Comparer les dimensions et le type de montage avec la piece d origine
  - Choisir un equipementier reconnu pour garantir qualite et compatibilite
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "repare l'injection"
  cost_range:
    min: 20
    max: 300
    currency: EUR
    unit: l'unite
    source: estimation categorie
  brands:
    premium:
    - Pierburg
    - Delphi
    - BorgWarner
    standard:
    - Valeo
    - Wahler
    - Hella
    budget:
    - Meat & Doria
    - ERA
    - Hoffer
  quality_tiers:
  - tier: Origine constructeur
    description: Vanne EGR identique a la premiere monte, avec moteur electrique et capteur de position calibres pour le calculateur
      du vehicule.
  - tier: Equipementier qualite OE
    description: Fabricants premiere monte avec meme qualite de moteur electrique et de capteur. Cartographie compatible avec
      le calculateur.
  - tier: Adaptable qualite reconnue
    description: Vannes EGR compatibles avec verification de la course du papillon et du signal electrique. Tester le fonctionnement
      apres montage.
diagnostic:
  symptoms:
  - id: S1
    label: Voyant moteur allume avec codes p040x visuel
    severity: confort
  - id: S2
    label: Perte de puissance a l acceleration comportement
    severity: confort
  - id: S3
    label: Fumee noire excessive a l acceleration visuel
    severity: confort
  - id: S4
    label: Ralenti instable calages frequents comportement
    severity: immobilisation
  - id: S5
    label: Odeur d echappement plus prononcee olfactif
    severity: confort
  - id: S6
    label: Plus de 100 000 km sans decalaminage preventif
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - lecture codes defaut obd et diagnostic electronique
  - remplacement preventif recommande
  quick_checks:
  - Voyant moteur allume avec codes p040x visuel ?
  - 'Observer : perte de puissance a l acceleration comportement ?'
  - 'Observer : fumee noire excessive a l acceleration visuel ?'
  - 'Observer : ralenti instable calages frequents comportement ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Voyant moteur allume avec codes p040x visuel
  - Perte de puissance a l acceleration comportement
  - Fumee noire excessive a l acceleration visuel
  - Ralenti instable calages frequents comportement
  - Odeur d echappement plus prononcee olfactif
  - Plus de 100 000 km sans decalaminage preventif
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '1137'
  intro_title: A quoi sert Soupape réaspiration des gaz d'échappement ?
  risk_title: Pourquoi remplacer Soupape réaspiration des gaz d'échappement a temps ?
  risk_explanation: '**Pièce HS** - Le soupape réaspiration des gaz d''échappement peut être hors service et nécessiter un
    remplacement'
  risk_consequences:
  - '**Pièce HS** - Le soupape réaspiration des gaz d''échappement peut être hors service et nécessiter un remplacement'
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
  - question: Vanne EGR OE ou adaptable ?
    answer: Les EGR OES (Pierburg, Valeo, Delphi) sont fiables. Les adaptables génériques sont déconseillées car la qualité
      du moteur électrique varie beaucoup.
  - question: Comment savoir si ma vanne EGR est HS ?
    answer: Voyant moteur allumé, perte de puissance, fumée noire, à-coups au ralenti, codes défaut P0400-P0409.
  - question: Peut-on nettoyer l'EGR soi-même ?
    answer: Oui si elle est accessible. Démontez-la, trempez-la dans du dégraissant, brossez les dépôts. Vérifiez que le papillon
      bouge librement avant remontage.
  - question: Peut-on rouler sans EGR ?
    answer: Oui le moteur fonctionne, mais c'est interdit (contrôle technique) et polluant (NOx). De plus, le calculateur
      peut passer en mode dégradé.
  - question: Quelle erreur éviter avec l'EGR ?
    answer: Supprimer l'EGR ou la faire reprogrammer. C'est illégal, polluant, et détectable au contrôle technique OBD depuis
      2019.
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
doc_id: 3b35bcc9-9df3-5bf1-8861-6412bd694b00
content_hash: sha256:ddab50931bbbf5d2
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
  area: Sur le moteur (rampe injection, admission)
  access: Par le dessus (capot)
  adjacent_parts:
  - rampe
  - injecteurs
  - calculateur moteur
  - papillon
installation:
  difficulty: moyen a difficile
  time: 30min a 2h
  tools:
  - cle a douille
  - cle dynamometrique
  - diagnostic OBD
  prerequisite: Depressuriser le circuit carburant avant depose
phase5_enrichment:
  _source: contenu LLM — a revalider contre sources OEM
  _validation_status: pending_oem_validation
  _enriched_at: '2026-03-30'
  technical_notes:
    role: 'synonyme vanne EGR — recirculation des gaz d''echappement vers l''admission'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    La soupape de réaspiration des gaz d'échappement, communément appelée vanne
    EGR (Exhaust Gas Recirculation), est un composant du système de dépollution
    du moteur. Sa fonction principale est de réadmettre une fraction des gaz
    d'échappement dans le collecteur d'admission, afin de les mélanger à l'air
    frais entrant avant la combustion. Ce recyclage remplit deux objectifs
    distincts. D'abord, les gaz d'échappement recirculés, pauvres en oxygène,
    abaissent la température de combustion dans les cylindres. Or, la formation
    des oxydes d'azote (NOx) — polluants réglementés par les normes Euro — est
    directement proportionnelle à la température de flamme. Ensuite, ce
    mécanisme permet de doser précisément la proportion de gaz recyclés en
    fonction du régime moteur et de la charge, grâce à une commande électronique
    pilotée par le calculateur moteur. La vanne EGR peut être de type
    pneumatique (commandée par dépression) ou électronique (motoréducteur
    intégré). Les versions modernes combinent une vanne EGR et un refroidisseur
    EGR qui refroidit les gaz avant leur réintroduction, améliorant encore
    l'efficacité de la réduction des NOx. Elle travaille en lien direct avec le
    collecteur d'admission et peut être associée à une vanne papillon
    d'admission sur certains moteurs diesel.
  S2: >-
    Une vanne EGR défaillante ou encrassée génère des symptômes variés selon
    qu'elle reste coincée en position ouverte ou fermée. L'encrassement
    progressif par les suies est la cause la plus fréquente, surtout après 100
    000 km. Voici les signaux à surveiller : - Voyant moteur allumé avec codes
    défaut P040x : les codes P0400 à P0409 indiquent une anomalie dans le
    circuit EGR, détectée par le calculateur moteur via le capteur de débit
    d'air massique (MAF). - Perte de puissance à l'accélération : une vanne EGR
    bloquée en position ouverte introduit trop de gaz brûlés dans l'admission,
    appauvrissant le mélange en oxygène et réduisant la puissance disponible. -
    Fumée noire excessive à l'accélération : signe d'un mélange air/carburant
    déséquilibré, souvent lié à un flux EGR non contrôlé. - Ralenti instable et
    calages fréquents : quand la vanne reste ouverte au ralenti, les gaz
    d'échappement perturbent le mélange à bas régime et peuvent provoquer des
    calages — symptôme de sévérité élevée nécessitant une intervention rapide. -
    Odeur d'échappement plus prononcée dans l'habitacle : signe de gaz mal
    réacheminés, parfois perceptible à l'arrêt ou en conduite lente. - Plus de
    100 000 km sans décalaminage préventif : au-delà de ce kilométrage, la vanne
    EGR et le collecteur d'admission accumulent des dépôts de suies qui
    réduisent le débit et la précision de régulation.
  S3: >-
    Le choix d'une vanne EGR de remplacement exige de la rigueur. La qualité du
    motoréducteur intégré varie considérablement selon l'origine de la pièce, et
    un choix inadapté se traduit par une récidive rapide ou un mauvais
    fonctionnement. Voici les critères essentiels : - Marque et modèle exacts du
    véhicule : la référence EGR est spécifique à la motorisation, à la cylindrée
    et à la norme d'émissions applicable (Euro 4, 5 ou 6). Saisir marque,
    modèle, type de motorisation et année de mise en circulation. - Code moteur
    : sur un même modèle, les différentes puissances ou variantes de
    motorisation peuvent utiliser des vannes EGR avec des débits et des plages
    de régulation différents. - Qualité OES plutôt que générique : les
    fabricants OES (Pierburg, Valeo, Delphi, Wahler) fabriquent les vannes EGR
    pour les constructeurs. La qualité du motoréducteur et des joints
    d'étanchéité est nettement supérieure aux adaptables génériques de bas de
    gamme. - Type de vanne : pneumatique ou électrique : ne pas substituer un
    type par l'autre. La compatibilité mécanique et électronique doit être
    vérifiée. - Présence ou non d'un refroidisseur EGR intégré : certaines
    configurations combinent la vanne et le refroidisseur en un seul bloc.
    Vérifier si le kit comprend les joints de raccordement nécessaires. -
    Vérifier l'état du collecteur d'admission avant montage : un collecteur
    encrassé réduira immédiatement l'efficacité de la nouvelle vanne. Le
    décalaminage préventif du collecteur est fortement conseillé lors du
    remplacement. Pour aller plus loin : consultez notre guide d'achat soupape
    réaspiration des gaz d'échappement — comparatif marques, critères de choix
    et prix.
  S4_DEPOSE: >-
    Le remplacement d'une vanne EGR varie en complexité selon sa localisation
    (en haut de moteur ou sous la tubulure d'échappement) et le type de moteur.
    Prévoir en moyenne 1 à 3 heures selon l'accessibilité. Voici la procédure
    générale : - Déconnecter la batterie avant toute intervention électrique
    pour éviter un démarrage accidentel du motoréducteur. - Laisser refroidir le
    moteur complètement (minimum 2 heures après le dernier fonctionnement) : la
    vanne EGR est raccordée au circuit d'échappement qui peut atteindre plus de
    500 °C. - Débrancher le connecteur électrique de la vanne EGR (clip de
    verrouillage à presser avant d'extraire). - Dévisser les vis ou écrous de
    fixation de la vanne sur le collecteur d'admission ou le corps EGR. Sur
    moteurs diesel, les vis sont souvent oxydées — utiliser un dégrippant et
    laisser agir 15 minutes. - Déconnecter les durites de refroidissement si la
    vanne intègre un refroidisseur (vider préalablement le liquide de
    refroidissement pour éviter les projections). - Nettoyer soigneusement le
    logement de la vanne et le conduit d'admission avec un spray de décalaminage
    avant de monter la pièce neuve. - Positionner les joints neufs (fournis avec
    la vanne ou à commander séparément) et fixer la nouvelle vanne au couple
    constructeur. - Reconnecter le connecteur, la batterie et remplir le liquide
    de refroidissement si nécessaire. - Démarrer et effacer les codes défaut
    avec la valise OBD pour permettre au calculateur de réinitialiser les
    valeurs d'adaptation EGR.
  S4_REPOSE: >-
    La repose de la vanne EGR est une étape critique : un joint mal positionné
    ou un connecteur mal rebranché peut provoquer une fuite de gaz chauds ou
    générer immédiatement un nouveau code défaut. Suivre cette procédure dans
    l'ordre strict. - Préparer les joints neufs : ne jamais réutiliser les
    joints d'origine après dépose. Les joints EGR sont soumis à des températures
    dépassant 500 °C et à des cycles thermiques répétés. Utiliser exclusivement
    les joints fournis avec la vanne ou ceux préconisés par le constructeur. -
    Nettoyer le logement de la vanne : avant pose, éliminer les résidus de
    calamine et d'anciens joints sur le collecteur d'admission avec un spray
    décalaminant et une spatule plastique. Ne pas rayer les surfaces d'appui
    métalliques. - Positionner la vanne et les joints : aligner la vanne sur les
    guides ou les fixations sans forcer. Si la vanne est munie d'un
    refroidisseur intégré, s'assurer que les raccords de liquide sont
    correctement orientés vers les durites de refroidissement. - Serrer les vis
    de fixation au couple constructeur : utiliser une clé dynamométrique — le
    couple est généralement de 10 à 25 Nm selon le moteur. Serrer en croix pour
    une répartition homogène de la charge sur le joint. Un sur-serrage écrase le
    joint et provoque une fuite. - Reconnecter les durites de refroidissement
    (si présentes) avec des colliers neufs ou en vérifiant l'état des colliers
    d'origine. Remplir le liquide de refroidissement si la vidange avait été
    nécessaire à la dépose. - Rebrancher le connecteur électrique : insérer
    fermement jusqu'au clic du clip de verrouillage. Un connecteur partiellement
    engagé génère un faux contact et un code défaut intermittent difficile à
    diagnostiquer. - Reconnecter la batterie et démarrer le moteur. Maintenir le
    ralenti 5 minutes pour permettre la montée en température et vérifier
    l'absence de fuite de gaz chauds autour de la vanne. - Effacer les codes
    défaut OBD avec la valise et réaliser un cycle d'adaptation : rouler en
    incluant des phases de décélération pied levé (phase active du recyclage
    EGR). Vérifier l'absence de retour des codes P040x après 20 à 30 km.
  S5: >-
    Le remplacement ou la désactivation de la vanne EGR concentre plusieurs
    erreurs fréquentes qui peuvent entraîner des problèmes techniques,
    réglementaires ou financiers. Voici les principales à éviter : - Supprimer
    ou faire reprogrammer la vanne EGR : la suppression électronique de l'EGR
    (via reprogrammation du calculateur ou kit de suppression) est illégale en
    France depuis la directive 2014/45/EU. Elle est détectable au contrôle
    technique OBD depuis 2019 et entraîne un refus de visite. Conséquence :
    contravention et contre-visite obligatoire. - Monter une vanne EGR générique
    de mauvaise qualité : le motoréducteur interne d'une vanne low-cost peut
    tomber en panne dans les 20 000 à 30 000 km. Conséquence : retour atelier
    rapide et coût total supérieur à l'option OES. - Négliger le décalaminage du
    collecteur d'admission : une nouvelle vanne montée sur un collecteur
    encrassé voit ses performances dégradées immédiatement. Conséquence :
    persistance des symptômes malgré le remplacement. - Oublier d'effacer les
    codes défaut après montage : le calculateur garde en mémoire les valeurs
    d'adaptation antérieures. Sans effacement, il peut rester en mode dégradé.
    Conséquence : voyant moteur qui reste allumé et performances réduites. - Ne
    pas vérifier l'état du capteur MAF (débitmètre d'air) : un débitmètre
    encrassé peut simuler un dysfonctionnement EGR. Remplacer la vanne sans
    diagnostiquer le MAF conduit à une mauvaise identification de la panne.
    Conséquence : dépense inutile.
  S6: >-
    Après installation de la nouvelle vanne EGR, une série de contrôles est
    nécessaire pour confirmer le retour à un fonctionnement normal du moteur : -
    Effacement des codes défaut à la valise OBD : indispensable pour
    réinitialiser les valeurs d'adaptation EGR du calculateur. Sans cette étape,
    le moteur peut rester en mode dégradé. - Vérification de l'étanchéité des
    raccordements : inspecter visuellement les joints et les durites de
    refroidissement (si applicable) moteur chaud — aucune trace de fuite liquide
    ou gazeuse ne doit être présente. - Test du ralenti : le ralenti doit être
    stable à la valeur constructeur (généralement 700 à 850 tr/min sur diesel).
    Un ralenti qui chasse ou qui s'effondre indique un problème persistant. -
    Lecture des données en temps réel (live data) : surveiller la position de la
    vanne EGR via la valise OBD en accélération progressive. La vanne doit
    s'ouvrir et se fermer de façon progressive et régulière. - Test routier de
    20 km minimum : réaliser un parcours mixte (ville + route) pour permettre au
    calculateur de recalibrer les adaptations EGR et confirmer l'absence de
    retour des codes défaut.
  S7: >-
    Le remplacement de la vanne EGR s'accompagne souvent d'interventions
    complémentaires sur les composants du circuit d'admission et d'échappement,
    particulièrement encrassés par la réaspiration de gaz chauds chargés de
    suies. - Vanne EGR complète — Sur certaines architectures, la soupape de
    réaspiration est intégrée à la vanne EGR et ne peut être remplacée
    séparément. Vérifier si votre moteur dispose d'une soupape indépendante ou
    d'une vanne EGR avec soupape intégrée avant commande. - Collecteur
    d'admission — Le collecteur est systématiquement encrassé quand la vanne EGR
    dysfonctionne. Un nettoyage ou un remplacement du collecteur est recommandé
    simultanément pour restaurer les sections de passage d'air nominales. -
    Refroidisseur de gaz EGR — Présent sur les moteurs diesel modernes, il
    refroidit les gaz avant réinjection. Un refroidisseur percé contaminerait le
    liquide de refroidissement avec des suies ou des hydrocarbures.
  S8: >-
    Vanne EGR d'origine (OES) ou adaptable : quelle différence concrète ? Les
    vannes EGR OES (Pierburg, Valeo, Delphi) sont fabriquées sur les mêmes
    lignes que les pièces montées en première monte. La qualité du motoréducteur
    interne, des joints et du câblage est significativement supérieure aux
    adaptables génériques. Les vannes génériques présentent un risque accru de
    défaillance prématurée du motoréducteur, souvent entre 20 000 et 40 000 km.
    L'écart de prix initial est généralement récupéré en termes de durabilité.
    Peut-on nettoyer la vanne EGR soi-même plutôt que la remplacer ? Oui, si la
    vanne est accessible et que l'encrassement est la seule cause. Démonter la
    vanne, la tremper dans un solvant de décalaminage adapté, brosser les dépôts
    de suie avec une brosse à poils métalliques fins. Vérifier que le papillon
    interne se déplace librement sur toute sa course avant remontage. Cette
    opération est efficace sur les vannes pneumatiques simples, moins sur les
    vannes électroniques dont le motoréducteur peut être dégradé par les
    solvants. Peut-on rouler avec une vanne EGR défectueuse sans risque immédiat
    ? Techniquement, le moteur continue de fonctionner, souvent en mode dégradé
    (puissance réduite, régime plafonné). Mais il est illégal de circuler avec
    un véhicule en mode dégradé émettant des taux de NOx excessifs. Le contrôle
    technique refusera le véhicule si la vanne EGR est désactivée ou HS. À moyen
    terme, une vanne bloquée ouverte peut encnrasser le collecteur d'admission
    au point de nécessiter un décalaminage complet. Quelle est la durée de vie
    moyenne d'une vanne EGR ? En usage normal avec du carburant de qualité, une
    vanne EGR OES a une durée de vie de 150 000 à 200 000 km. Le kilométrage de
    remplacement courant se situe autour de 120 000 à 150 000 km sur véhicules à
    usage urbain intensif, où les cycles de fonctionnement à basse température
    favorisent l'encrassement par condensation des suies.
---

# Soupape réaspiration des gaz d'échappement - Guide Diagnostic Complet

## Fonction et Rôle

Readmettre une partie des gaz d'echappement dans l'admission

**Actions principales:** recycler, readmettre, doser

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Ralenti instable calages frequents comportement**
  ralenti instable calages frequents comportement

### 🟢 Autres Symptômes

- voyant moteur allume avec codes p040x visuel
- perte de puissance a l acceleration comportement
- fumee noire excessive a l acceleration visuel
- odeur d echappement plus prononcee olfactif
- plus de 100 000 km sans decalaminage preventif

## Procédure de Diagnostic

Pour diagnostiquer un problème de soupape réaspiration des gaz d'échappement:

1. **Inspection visuelle** - Examiner l'état du soupape réaspiration des gaz d'échappement
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le soupape réaspiration des gaz d'échappement peut être hors service et nécessiter un remplacement
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- vanne-egr
- collecteur-d-admission

## Critères de Compatibilité

Pour commander le bon soupape réaspiration des gaz d'échappement, vous devez connaître:

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

**Vanne EGR OE ou adaptable ?**
Les EGR OES (Pierburg, Valeo, Delphi) sont fiables. Les adaptables génériques sont déconseillées car la qualité du moteur électrique varie beaucoup.

**Comment savoir si ma vanne EGR est HS ?**
Voyant moteur allumé, perte de puissance, fumée noire, à-coups au ralenti, codes défaut P0400-P0409.

**Peut-on nettoyer l'EGR soi-même ?**
Oui si elle est accessible. Démontez-la, trempez-la dans du dégraissant, brossez les dépôts. Vérifiez que le papillon bouge librement avant remontage.

**Peut-on rouler sans EGR ?**
Oui le moteur fonctionne, mais c'est interdit (contrôle technique) et polluant (NOx). De plus, le calculateur peut passer en mode dégradé.

**Quelle erreur éviter avec l'EGR ?**
Supprimer l'EGR ou la faire reprogrammer. C'est illégal, polluant, et détectable au contrôle technique OBD depuis 2019.
