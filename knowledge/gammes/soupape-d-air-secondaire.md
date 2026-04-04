---
category: alimentation
slug: soupape-d-air-secondaire
title: Soupape d'air secondaire
pg_id: 904
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
  role: Controler l'admission d'air secondaire vers l'echappement
  must_be_true:
  - ouvrir
  - fermer
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
  - ouvrir
  - fermer
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
    description: Soupapes d air secondaire montees en premiere monte, calibrees pour le debit et la temporisation specifiques
      du systeme antipollution.
  - tier: Equipementier qualite OE
    description: Fabricants fournissant les constructeurs. Memes specifications de debit et de resistance thermique.
  - tier: Adaptable qualite reconnue
    description: Soupapes compatibles avec verification du debit d air et de l etancheite. Controler la conformite avant montage.
diagnostic:
  symptoms:
  - id: S1
    label: Voyant moteur avec code p0410
    severity: confort
  - id: S2
    label: Bruit d air au demarrage a froid
    severity: confort
  - id: S3
    label: Perte de puissance a froid
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  quick_checks:
  - Voyant moteur avec code p0410 ?
  - Bruit d air au demarrage a froid ?
  - 'Observer : perte de puissance a froid ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Voyant moteur avec code p0410
  - Bruit d air au demarrage a froid
  - Perte de puissance a froid
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '904'
  intro_title: A quoi sert Soupape d'air secondaire ?
  risk_title: Pourquoi remplacer Soupape d'air secondaire a temps ?
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
  - question: Comment choisir Soupape d'air secondaire compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Soupape d'air secondaire ?
    answer: En cas de voyant moteur avec code p0410 ou de degradation mesurable, il faut controler rapidement avant panne
      secondaire.
  - question: Puis-je monter Soupape d'air secondaire sans verification atelier ?
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
doc_id: 0254b0bf-f17d-5bb6-9151-61350e564ee2
content_hash: sha256:4fae5b0148790f46
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
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  technical_notes:
    val_150__c: '150 °C'
    val_17_a: '17 a'
    val_2_a: '2 a'
    val_25__: '25 %'
    val_6_a: '6 a'
    val_800__c: '800 °C'
    val_97_5__c: '97,5 °C'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    La soupape d'air secondaire est un composant du système de dépollution
    présent sur de nombreux moteurs à essence. Son rôle est de contrôler
    l'admission d'air frais supplémentaire directement dans le collecteur
    d'échappement, en aval des soupapes d'échappement du moteur, lors du
    démarrage à froid. Lors des premiers instants de fonctionnement du moteur
    (les 2 à 3 premières minutes à froid), le catalyseur n'a pas encore atteint
    sa température de fonctionnement optimale (entre 400 et 800°C). Durant cette
    phase, les émissions d'hydrocarbures non brûlés sont importantes. La soupape
    d'air secondaire s'ouvre alors pour injecter de l'air dans les gaz
    d'échappement chauds, provoquant une post-combustion partielle des résidus.
    Cette réaction oxydante réchauffe plus rapidement le catalyseur et réduit
    significativement les émissions polluantes à froid. La soupape est commandée
    électroniquement par le calculateur moteur (ECU) et actionné par une pompe à
    air secondaire qui crée la pression d'air nécessaire. La soupape s'ouvre à
    la commande de l'ECU et se referme automatiquement dès que le catalyseur est
    à température ou que le régime moteur dépasse un certain seuil. Un
    dysfonctionnement de cette soupape génère directement un code défaut P0410
    (système d'air secondaire) au tableau de bord et augmente les émissions
    polluantes, pouvant conduire à un refus au contrôle antipollution du
    contrôle technique.
  S2: >-
    La soupape d'air secondaire peut se boucher progressivement par des dépôts
    carbonés ou subir une défaillance mécanique ou électrique. Les symptômes
    sont caractéristiques et permettent un diagnostic rapide. Voici les signaux
    à surveiller : - Voyant moteur allumé avec code défaut P0410 : c'est le
    symptôme le plus direct — le calculateur moteur détecte une anomalie dans le
    circuit d'air secondaire et stocke ce code spécifique, lisible avec un outil
    de diagnostic OBD. - Bruit d'air anormal au démarrage à froid : un
    sifflement ou un grondement sourd pendant les premières secondes de
    démarrage peut indiquer une soupape qui ne s'ouvre plus correctement ou une
    fuite dans le circuit. - Perte de puissance perceptible à froid : si la
    soupape reste bloquée en position ouverte, elle perturbe la gestion des gaz
    d'échappement et peut dégrader les performances moteur avant montée en
    température. - Odeur d'échappement plus prononcée à froid : une soupape
    défaillante empêche la post-combustion des hydrocarbures non brûlés,
    augmentant les émissions et l'odeur en sortie d'échappement. - Ralenti
    instable dans les premières minutes : le calculateur moteur peut modifier la
    cartographie d'injection pour compenser le dysfonctionnement, créant des
    variations de régime au ralenti. - Refus au contrôle technique antipollution
    : des émissions de CO et d'hydrocarbures hors normes lors du test
    antipollution peuvent résulter d'une soupape d'air secondaire défaillante
    qui n'assure plus la post-combustion à froid.
  S3: >-
    La soupape d'air secondaire est une pièce technique dont la sélection exige
    une identification précise du moteur et de l'architecture du système d'air
    secondaire. Voici les critères déterminants à vérifier avant de commander :
    - Marque, modèle et année du véhicule : la soupape est spécifique à chaque
    motorisation et parfois même à des variantes au sein d'une même gamme moteur
    (versions haute et basse puissance). - Référence du code défaut OBD : noter
    le code exact (P0410, P0411, P0412, etc.) permet de cibler précisément le
    composant défaillant — la soupape elle-même, la pompe à air ou le circuit
    électrique de commande. - Type de moteur (cylindrée et code moteur) : le
    code moteur inscrit sur la plaque constructeur ou dans la documentation
    technique est l'identifiant le plus fiable pour sélectionner la soupape
    correcte. - Vérifier le système complet avant de commander uniquement la
    soupape : si la pompe à air secondaire est également défaillante, remplacer
    la soupape seule ne résoudra pas le problème — diagnostiquer l'ensemble du
    circuit. - Référence constructeur ou OEM : croiser la référence inscrite sur
    l'ancienne soupape avec la référence équipementier pour confirmer
    l'interchangeabilité mécanique et électrique. - Qualité des joints et
    connecteurs électriques : vérifier que la pièce de remplacement inclut les
    joints d'étanchéité et le connecteur électrique adaptés, car les fuites
    d'air sur le circuit secondaire génèrent de faux codes défauts. - Éviter les
    pièces sans numéro de référence traçable : une soupape d'air secondaire de
    mauvaise qualité peut se bloquer rapidement par dépôts carbonés, causant une
    récidive rapide du code défaut P0410. Pour aller plus loin : consultez notre
    guide d'achat soupape d'air secondaire — comparatif marques, critères de
    choix et prix.
  S4_DEPOSE: >-
    Le remplacement de la soupape d'air secondaire nécessite un accès au
    collecteur d'échappement ou à sa zone adjacente selon le modèle. Un outil de
    diagnostic OBD est indispensable pour effacer le code défaut après
    l'intervention. Voici la procédure générale : - Connecter un outil de
    diagnostic OBD et noter tous les codes défauts présents avant intervention —
    le code P0410 doit être présent, et identifier si d'autres codes
    accompagnateurs (pompe à air, capteur) signalent des défaillances associées.
    - Laisser refroidir le moteur complètement — la soupape est positionnée à
    proximité du collecteur d'échappement, une zone qui reste chaude longtemps
    après l'arrêt moteur. - Localiser la soupape d'air secondaire sur le moteur
    : elle est généralement vissée sur le collecteur d'admission ou
    d'échappement et reliée à la pompe à air par un tuyau souple et à l'ECU par
    un connecteur électrique. - Débrancher le connecteur électrique de commande
    de la soupape en appuyant sur la languette de déverrouillage. - Déconnecter
    le tuyau d'air reliant la pompe à air à la soupape — noter le sens de
    connexion et inspecter l'état du tuyau (fissures, durcissement). - Dévisser
    les vis ou écrous de fixation de la soupape sur le collecteur (généralement
    2 à 3 vis), en appliquant du dégrippant si la zone est corrodée. - Extraire
    l'ancienne soupape et nettoyer les portées d'étanchéité sur le collecteur. -
    Installer la nouvelle soupape avec des joints neufs, reconnecter le tuyau
    d'air et le connecteur électrique, puis effacer les codes défauts avec
    l'outil OBD avant de démarrer et vérifier la disparition du voyant moteur.
  S4_REPOSE: >-
    Après avoir fixé la soupape d'air secondaire neuve dans son logement, la
    repose des durites et la vérification électronique sont les deux étapes
    critiques pour garantir le bon fonctionnement du système de dépollution à
    froid. Un effacement des codes défaut OBD est impératif avant la validation.
    - Repositionner la soupape neuve dans son logement sur le collecteur ou le
    bloc selon la configuration du moteur. S'assurer que le joint d'étanchéité
    fourni est en place avant de visser les fixations. - Serrer les vis de
    fixation au couple préconisé (typiquement 10 à 15 N·m sur les brides de
    soupape). Un serrage insuffisant provoque des fuites d'air ; un serrage
    excessif déforme le corps de soupape. - Reconnecter les durites d'air en
    amont et en aval de la soupape. Vérifier que les colliers de serrage sont en
    position correcte et serrés uniformément — aucune vrille du tuyau ne doit
    contraindre les raccords. - Reconnecter le connecteur électrique de la
    soupape électromagnétique. Aligner les ergots de guidage avant d'enfoncer le
    connecteur jusqu'au clic de verrouillage. Tirer légèrement pour confirmer la
    prise. - Rebrancher le tuyau de commande pneumatique si la soupape est à
    commande mixte. Vérifier l'absence de microfissures sur le tuyau remis en
    place. - Reposer les caches et protections déposés lors de l'accès à la
    soupape (cache moteur, gaine d'admission, etc.) dans l'ordre inverse de leur
    dépose. - Effacer les codes défaut OBD à la valise de diagnostic avant le
    démarrage. Le code P0410 (système d'air secondaire) doit être effacé pour
    que l'ECU réévalue le bon fonctionnement de la soupape neuve. - Démarrer le
    moteur à froid et observer pendant les 2 premières minutes : vérifier
    l'absence de bruit d'air anormal et que le voyant moteur ne se rallume pas
    dans les premiers cycles de chauffe.
  S5: >-
    Le diagnostic et le remplacement de la soupape d'air secondaire donnent lieu
    à plusieurs erreurs fréquentes qui peuvent conduire à une récidive rapide du
    code défaut ou à un remplacement inutile. Voici les cinq erreurs à éviter
    absolument : - Remplacer la soupape sans diagnostiquer l'ensemble du circuit
    : le code P0410 peut provenir de la soupape elle-même, de la pompe à air
    secondaire, d'un tuyau fissuré ou du connecteur électrique — un diagnostic
    complet du circuit évite de remplacer la mauvaise pièce. - Ne pas effacer
    les codes défauts après remplacement : après l'installation de la nouvelle
    soupape, le voyant moteur restera allumé tant que les codes ne sont pas
    effacés avec un outil OBD — cette étape est indispensable pour valider la
    réparation. - Négliger les joints d'étanchéité lors de la repose : une fuite
    d'air sur le circuit secondaire génère des faux codes défauts et des
    perturbations dans la lecture des capteurs lambda — toujours remplacer les
    joints lors de chaque démontage. - Oublier de vérifier l'état du tuyau
    souple reliant la pompe à la soupape : ce tuyau en caoutchouc est soumis à
    des températures élevées et devient cassant avec le temps — une fissure sur
    ce tuyau produit exactement les mêmes symptômes qu'une soupape défaillante.
    - Intervenir sur un collecteur d'échappement encore chaud : attendre au
    minimum 2 heures après l'arrêt moteur — les zones proches de l'échappement
    peuvent maintenir des températures dangereuses bien après la coupure du
    moteur.
  S6: >-
    Après l'installation de la nouvelle soupape d'air secondaire, une série de
    contrôles techniques et électroniques doit être réalisée pour valider la
    réparation avant de rendre le véhicule à son usage normal : - Effacer les
    codes défauts avec l'outil OBD et vérifier que le voyant moteur s'éteint
    correctement après effacement — si le voyant se rallume immédiatement, une
    autre cause de défaillance doit être investigée. - Démarrer le moteur à
    froid et écouter attentivement pendant les 2 à 3 premières minutes : aucun
    sifflement ni bruit d'air anormal ne doit être perceptible — cela confirme
    que la soupape s'ouvre et se ferme correctement. - Vérifier l'absence de
    fuite d'air aux jonctions du circuit (raccords du tuyau, joint de la soupape
    sur le collecteur) avec un spray de détection de fuites ou en passant la
    main près des jonctions moteur chaud. - Effectuer un test de diagnostic
    actif avec l'outil OBD si l'outil le permet : activer manuellement la pompe
    à air et la soupape pour confirmer leur fonctionnement synchronisé à la
    demande du calculateur. - Réaliser un trajet de test avec un ou deux
    démarrages à froid complets et vérifier que le voyant moteur reste éteint
    après au moins 2 cycles de conduite — cela confirme que le système est
    validé par les autodiagnostics du calculateur.
  S7: >-
    La soupape d'air secondaire s'inscrit dans un système de dépollution composé
    de plusieurs éléments interdépendants. Une défaillance de l'un d'eux peut
    générer exactement le même code défaut (P0410) que la soupape elle-même.
    Vérifier ces pièces avant de conclure au remplacement. - Pompe à air
    secondaire — génère le débit d'air injecté dans l'échappement à froid. Si la
    pompe est grippée ou hors service, la soupape neuve ne servira à rien car il
    n'y aura aucun flux à contrôler. Tester la pompe à la valise avant toute
    commande. - Soupape d'aspiration d'air secondaire — clapet situé en amont,
    souvent confondu avec la soupape de contrôle principale. Les deux pièces
    peuvent être défaillantes simultanément sur les véhicules à forte
    kilométrage. - Tuyaux et durites du circuit d'air secondaire — microfissures
    fréquentes dues aux cycles thermiques. Une durite fendue génère une fuite
    d'air qui déclenche le code P0410 sans que la soupape soit en cause. -
    Relais et fusible de la pompe à air — à contrôler avant tout remplacement
    mécanique. Un relais claqué bloque l'alimentation de la pompe et simule une
    défaillance de l'ensemble du système d'air secondaire. - Capteur de
    température d'air — sur certains moteurs, une valeur incohérente du capteur
    empêche l'activation du système d'air secondaire à froid et génère un faux
    code de défaut sur la soupape.
  S8: >-
    le rôle de le code défaut P0410 et que signifie-t-il exactement ? Le code
    P0410 signifie "Dysfonctionnement du système d'air secondaire". Il est
    généré par le calculateur moteur lorsqu'il détecte que le débit d'air
    secondaire injecté dans l'échappement est insuffisant ou absent lors de la
    phase de démarrage à froid. Ce code peut pointer vers la soupape d'air
    secondaire elle-même, mais aussi vers la pompe à air, le tuyau de liaison,
    le relais de commande ou le câblage électrique du circuit. Un diagnostic OBD
    complet avec lecture des données en temps réel est nécessaire pour isoler le
    composant précis défaillant. La soupape d'air secondaire est-elle présente
    sur tous les moteurs essence ? Non. Le système d'air secondaire est
    principalement présent sur les moteurs essence soumis à des normes
    antipollution strictes (Euro 3 à Euro 5), surtout sur les véhicules produits
    entre 1997 et 2015 environ. Les moteurs diesel n'en sont pas équipés. Sur
    les véhicules plus récents (post-Euro 6), d'autres technologies de
    dépollution ont remplacé le système d'air secondaire. Vérifiez dans la
    documentation constructeur si votre moteur dispose de ce système avant de
    commander. Peut-on continuer à rouler avec un code P0410 actif sans
    remplacer la soupape ? Techniquement oui sur le court terme — la défaillance
    de la soupape d'air secondaire n'empêche pas le moteur de tourner
    normalement une fois chaud. Cependant, le voyant moteur restera allumé en
    permanence, ce qui masque d'autres défauts potentiels. Les émissions
    polluantes seront supérieures aux normes, ce qui entraîne un refus au
    contrôle technique antipollution. L'intervention doit être planifiée dans
    les semaines qui suivent la détection du code. Comment distinguer une panne
    de soupape d'air secondaire d'une panne de pompe à air ? Les deux composants
    génèrent des codes similaires (P0410, P0411). Pour les distinguer : brancher
    un outil de diagnostic et activer manuellement la pompe à air — si la pompe
    démarre (bruit audible dans le compartiment moteur) mais que le code
    persiste, la soupape est probablement défaillante. Si la pompe ne démarre
    pas du tout, c'est elle qui est en cause. Un test de pression d'air dans le
    circuit avec un manomètre permet de confirmer le diagnostic.
---

# Soupape d'air secondaire - Guide Diagnostic Complet

## Fonction et Rôle

Controler l'admission d'air secondaire vers l'echappement

**Actions principales:** ouvrir, fermer, controler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant moteur avec code p0410
- bruit d air au demarrage a froid
- perte de puissance a froid

## Procédure de Diagnostic

Pour diagnostiquer un problème de soupape d'air secondaire:

1. **Inspection visuelle** - Examiner l'état du soupape d'air secondaire
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
- soupape-d-aspiration-d-air-secondaire

## Critères de Compatibilité

Pour commander le bon soupape d'air secondaire, vous devez connaître:

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

**Comment choisir Soupape d'air secondaire compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Soupape d'air secondaire ?**
En cas de voyant moteur avec code p0410 ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Soupape d'air secondaire sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
