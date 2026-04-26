---
category: allumage
slug: bougie-d-allumage
title: Bougie d'allumage
pg_id: 686
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
  role: Produire l'etincelle qui enflamme le melange air-essence - Fonctionne en continu moteur tournant
  must_be_true:
  - produire une etincelle
  - enflammer
  - allumer le melange
  must_not_contain:
  - diesel
  - prechauffage
  - incandescence
  - chambre de combustion diesel
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - alternateur
  - batterie
  - demarreur
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
  - ❌ "plus de puissance"
  cost_range:
    min: 8
    max: 15
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Bougie d'origine (OE)
    description: Reference constructeur, avec le type d'electrode, l'indice thermique et l'ecartement precis pour le moteur.
      Recommandee pour respecter les intervalles de remplacement constructeur.
  - tier: Equipementier specialise allumage - nickel/cuivre
    description: Bougie d'entree de gamme, equivalente a l'OE standard. Intervalle de remplacement generalement autour de
      30 000 a 60 000 km selon le vehicule. Rapport qualite/prix adapte pour usage courant.
  - tier: Equipementier specialise - iridium / platine
    description: Electrodes en iridium ou platine. Duree de vie superieure (jusqu'a 100 000 km selon certains fabricants).
      Recommandee si le constructeur preconise ce type ou si l'intervalle de revision est long.
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
    label: Demarrage difficile ou laborieux
    severity: confort
  - id: S2
    label: Rates moteur a froid ou a l acceleration
    severity: confort
  - id: S3
    label: Consommation de carburant excessive
    severity: confort
  - id: S4
    label: Voyant moteur allume code rate d allumage
    severity: confort
  - id: S5
    label: Odeur essence echappement combustion incomplete
    severity: confort
  - id: S6
    label: Plus de 40 000 km sans remplacement standard
    severity: confort
  causes:
  - lecture codes defaut obd et diagnostic electronique
  - remplacement preventif recommande
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  - 'kilometrage eleve ou usure visible : remplacement preventif recommande'
  quick_checks:
  - 'Observer : demarrage difficile ou laborieux ?'
  - 'Observer : rates moteur a froid ou a l acceleration ?'
  - 'Observer : consommation de carburant excessive ?'
  - Voyant moteur allume code rate d allumage ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Demarrage difficile ou laborieux
  - Rates moteur a froid ou a l acceleration
  - Consommation de carburant excessive
  - Voyant moteur allume code rate d allumage
  - Odeur essence echappement combustion incomplete
  - Plus de 40 000 km sans remplacement standard
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '686'
  intro_title: A quoi sert Bougie d'allumage ?
  risk_title: Pourquoi remplacer Bougie d'allumage a temps ?
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
  - question: Bougie d'allumage standard ou iridium ?
    answer: L'iridium dure 2x plus longtemps et offre une meilleure étincelle. Plus chère mais rentable sur la durée. Respectez
      les préconisations constructeur.
  - question: Comment savoir si mes bougies d'allumage sont usées ?
    answer: Démarrage difficile, ratés moteur, surconsommation, électrode usée ou encrassée visible au démontage, écartement
      hors tolérance.
  - question: Tous les combien changer les bougies d'allumage ?
    answer: 'Standard : 30 000 à 45 000 km. Iridium/Platine : 60 000 à 100 000 km. Vérifier l''écartement tous les 20 000
      km.'
  - question: Peut-on changer les bougies d'allumage soi-même ?
    answer: Oui, avec une clé à bougie adaptée. Visser à la main d'abord pour éviter de foirer le filetage. Serrage au couple
      ou 1/4 de tour après contact.
  - question: Quelle erreur éviter avec les bougies d'allumage ?
    answer: Ne pas serrer trop fort (casse la porcelaine). Vérifier l'écartement avant montage. Ne pas mettre de graisse sur
      le filetage.
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
doc_id: d87c8dc0-57a3-5f9d-875f-6bbed7f09915
content_hash: sha256:a3cb7b08f8e41706
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
  _source: delphiautoparts.com + fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 3
  _has_tech_data: true
  types_variants:
  - type: 'céramique'
    source_ref: corpus RAG web OEM
  - type: 'plein'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_000_v: '000 V'
    val_000_v: '000 v'
    val_000__c: '000 °C'
    val_100_a: '100 a'
    val_105_a: '105 a'
    val_15_a: '15 a'
    val_16_a: '16 a'
    val_19_a: '19 a'
    val_20_a: '20 a'
    val_400__c: '400 °C'
    val_450__c: '450 °C'
    val_60_a: '60 a'
    val_7_a: '7 a'
    val_75__: '75 %'
    val_770__c: '770 °C'
  materials:
  - materiau: 'céramique'
    source_ref: corpus RAG web OEM
  - materiau: 'platine'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'La bougie d''allumage estimplantée au cœur de chaque cylindre et délivre l''étincelle qui déclenche la combustion du
    mélange air/essence.Dans les moteurs essence,l''air et le carburant sont aspirés dans le cylindre à travers l''injecteur
    ou lecarburateur. Le mélange forme un combustible qui va s''enflammer grâce àl''étincelle crée par la bougie d''allumage.
    La bougie d''allumage comprend deux parties : - La partie supérieure est connectée par un faisceau d''allumage haute-tensionà
    la bobine d''allumage. - La partie inférieure est vissée dans la culasse, elle comporte l''électrode quiva générer l''étincelle.
    La qualité de l''étincelle fournie par la bougie d''allumage détermine laforce de la combustion et donc la puissance et
    la souplesse de votre moteur. Généralement, il y a unebougie d''allumage par cylindre mais afin d''optimiser la combustion,
    certainsmoteurs sont pourvus de deux bougies par cylindre En savoir plus : bougie d''allumage — définition et rôle mécanique
    🚨 Bruit Bougie d''allumage : causes et diagnostic'
  S2: 'Une bougie d''allumage défectueuse présente plusieurs symptômes : - Manque de puissance du moteur. - Surconsommation
    de carburant. - Moteur qui pollue, dans ce cas il fautfaire attention au catalyseur. Diagnostic complet : identifier une
    panne de bougie d''allumage'
  S3: 'La bougie d''allumage déclenche l''étincelle qui enflamme le mélange air- essence dans chaque cylindre, en continu
    et à chaque cycle moteur. La durée de vie et la fréquence de remplacement varient du simple au quadruple selon le type
    de bougie : 40 000 km pour une bougie standard nickel, jusqu''à 160 000 km pour une bougie iridium. Un mauvais choix de
    résistance thermique ou de diamètre crée des ratés immédiats ou un pré-allumage qui détruit les pistons. - Indice thermique
    (chaleur) — critique pour éviter le pré-allumage — L''indice thermique (noté de 2 à 12 selon les fabricants : NGK, Bosch,
    Denso) définit la capacité de la bougie à évacuer la chaleur vers la culasse. Une bougie trop froide s''encrasse ; une
    bougie trop chaude provoque un pré-allumage (combustion avant l''étincelle) qui percute les pistons. Utiliser strictement
    l''indice prescrit par le constructeur. - Diamètre et pas de filetage : M10, M12 ou M14 x 1,25 — Le filetage doit correspondre
    au logement dans la culasse. Un mauvais diamètre abîme le filetage de culasse lors du montage. Les moteurs modernes 4
    soupapes utilisent majoritairement du M12x1,25 ; les anciens moteurs 2 soupapes du M14x1,25. - Longueur de filetage (reach)
    : courte (12 mm), longue (19 mm) ou extra-longue (26,5 mm) — Une bougie trop longue pénètre dans la chambre de combustion
    et risque de heurter les soupapes ou le piston. Une bougie trop courte crée une zone morte non allumée qui génère des
    ratés et des dépôts de calamine sur les électrodes. - Matériau de l''électrode centrale : nickel, platine ou iridium —
    Nickel : durée de vie 30 000 à 40 000 km, économique, convient aux véhicules anciens ou à forte consommation d''huile.
    Platine : 60 000 à 80 000 km, bonne tenue en température. Iridium : 100 000 à 160 000 km, électrode ultra-fine (0,4 mm)
    qui réduit la tension d''amorçage et améliore la régularité de la combustion. - Écartement inter-électrodes (gap) : mesure
    obligatoire avant montage — Le gap (espacement entre électrode centrale et masse) est généralement entre 0,7 et 1,3 mm
    selon le moteur. Les bougies iridium et platine ne se règlent pas (électrode fragile). Les bougies nickel doivent être
    vérifiées avec un calibre et ajustées si nécessaire au gap constructeur. - Résistance intégrée (R) : obligatoire sur les
    véhicules modernes — Les bougies avec résistance intégrée (suffixe R chez NGK, ex : BKR6E au lieu de BK6E) limitent les
    interférences électromagnétiques avec les calculateurs. Sur les véhicules post-2000, utiliser uniquement des bougies avec
    résistance. - Intervalle de remplacement préventif : respecter le carnet d''entretien — Au-delà de 40 000 km sans remplacement
    sur bougie standard, l''électrode s''érode, le gap augmente, et la tension nécessaire à l''étincelle dépasse la capacité
    de la bobine, ce qui la fatigue prématurément. Remplacer toutes les bougies simultanément pour maintenir une combustion
    équilibrée entre cylindres. Pour aller plus loin : consultez notre guide d''achat bougie d''allumage — comparatif marques,
    critères de choix et prix.'
  S4_DEPOSE: '📖 Avant de démonter, consultez la fiche technique Bougie d''allumage pour connaître les spécifications. - Arrêtez
    le moteur et le laissez refroidir. - Débranchez la batterie. - Localisez l''emplacement des bougiesd''allumage. - Libérez
    l''accès aux bougies d''allumage suivant l''équipement devotre véhicule : cache moteur, collecteur d''admission, boîtier
    de filtre àair... - Si vos bougies d''allumage sont avecfaisceau d''allumage dans ce cas débranchez les faisceaux des
    bougies d''allumage, il ne faut surtout pas tirer sur les faisceaux. Marquezles faisceaux des bougies d''allumage avant
    de les débranchés pour savoir surquel cylindre il était branché. - Si vos bougies d''allumage sont avecrampe dans ce cas
    débrancher le connecteur de la rampe, desserrez lesfixations de la rampe et retirez la rampe. - Si vos bougies d''allumage
    sont avec bobinepar bougie dans ce cas débranchez les connecteurs des bobines d''allumage etretirer les bobines d''allumage
    une par une. - Après avoir libérer l''accès aux bougiesd''allumage utilisez une clé à bougie et une rallonge pour les
    retirer. - Desserrez les bougies d''allumage une parune'
  S4_REPOSE: 'Le remontage des bougies d''allumage est une opération délicate car le filetage dans la culasse est fragile.
    Un serrage trop fort casse la porcelaine ou écrase le filetage ; un serrage trop faible provoque des fuites de compression.
    Vérifiez systématiquement l''écartement de l''électrode avant montage — un écartement hors tolérance génère des ratés
    d''allumage même sur une bougie neuve. - Vérifiez que les bougies d''allumage neuves sont identiques à celles déposées
    (référence, type d''électrode standard, iridium ou platine, longueur du filetage). Contrôlez l''écartement de l''électrode
    au calibre à lame — valeur typique entre 0,7 et 1,1 mm selon constructeur. - Contrôlez l''état des bobines d''allumage
    ou des faisceaux d''allumage : craquelures, humidité, connecteur oxydé. Remplacez tout élément douteux avant de remonter
    les bougies. - Nettoyez le puits de bougie avec un chiffon propre pour éliminer toute trace de crasse ou d''huile pouvant
    tomber dans la chambre de combustion. - Vissez chaque bougie d''allumage à la main jusqu''à la butée du joint conique
    ou plat. Ne jamais forcer avec une clé dès le début — le risque de foirer le filetage est maximal à cette étape. - Serrez
    au couple prescrit à l''aide de la clé à bougie et d''un compte-tours : pour les bougies avec joint plat, serrez d''un
    quart de tour (90°) après contact ; pour les bougies avec joint conique, serrez de 1/16 de tour (environ 15 à 20 Nm).
    Consultez la valeur exacte dans la fiche technique de votre moteur. - Reconnectez les faisceaux d''allumage ou les bobines
    d''allumage sur chaque bougie dans l''ordre des cylindres (respectez les repères effectués au démontage). Vérifiez le
    clic de verrouillage de chaque connecteur. - Remontez les éléments déposés pour l''accès (rampe de bobines, cache moteur,
    boîtier de filtre à air) dans l''ordre inverse du démontage. - Rebranchez la batterie. - Démarrez le moteur à froid et
    maintenez le ralenti 2 minutes. Vérifiez l''absence de raté d''allumage et de voyant moteur allumé. - Effacez les codes
    défaut OBD éventuellement mémorisés (notamment les codes de raté d''allumage P030x) si le voyant était allumé avant l''intervention.'
  S5: 'Erreurs frequentes avec les bougies d''allumage : - Ne pas respecter l''ecartement des electrodes (0,7 a 1,1 mm selon
    constructeur) — un ecartement incorrect provoque des rates ou une surconsommation- Trop serrer la bougie au montage —
    la culasse en aluminium se deforme et le filetage s''arrache. Respecter le couple constructeur (20-30 Nm selon reference)-
    Confondre bougies standard et bougies iridium/platine — les bougies longue duree ont une periodicite differente, ne pas
    les remplacer trop tot ni trop tard- Ne pas remplacer les bougies par jeu complet — des bougies d''age different provoquent
    un fonctionnement irregulier du moteur- Visser la bougie de travers dans le puits — le filetage en aluminium de la culasse
    se detruit et la reparation est couteuse (insert helicoil)- Ne pas anti- graisser le filetage (si preconise) — la bougie
    grippe dans la culasse et casse au demontage suivant'
  S6: 'Après le remplacement de vos bougies d''allumage, effectuez ces vérifications dans l''ordre. - Vérifier le couple de
    serrage de chaque bougie selon les préconisations constructeur (généralement 20 à 30 N·m) pour éviter fuite de compression
    ou casse au filetage - Effacer tout code de raté d''allumage stocké (type P0301 à P0308) et réaliser un essai de 15 km
    incluant des accélérations franches - Contrôler le démarrage à froid : le moteur doit démarrer en moins de 2 secondes
    sans rates les premières secondes - Vérifier l''absence d''odeur d''essence non brûlée à l''échappement moteur chaud -
    Surveiller la consommation sur les 500 premiers km : une normalisation vers la consommation constructeur est attendue
    après remplacement des bougies usées (seuil 40 000 km) - Contrôler simultanément les bobines d''allumage et le faisceau
    haute tension si le remplacement est effectué à plus de 60 000 km Retrouvez les spécifications techniques sur la fiche
    référence bougie d''allumage.'
  S7: Quel est le prix d'un bougie d'allumage ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur pour
    trouver le bougie d'allumage compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon bougie d'allumage est à changer ?Les signes d'usure les plus courants sont détaillés dans la section diagnostic
    ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un bougie d'allumage défaillant
    ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule. Consultez la section
    symptômes pour évaluer l'urgence du remplacement.- Faisceau d'allumage. - Bobine d'allumage. 📖 Fiche technique Bougie
    d'allumage — intervalles et spécifications d’entretien.
  S8: Comment choisir Bougie d'allumage compatible avec mon vehicule ?Renseignez marque, modele, type moteur et annee, puis
    verifiez la reference Quand remplacer Bougie d'allumage ?En cas de demarrage difficile ou laborieux ou de degradation
    mesurable, Puis-je monter Bougie d'allumage sans verification atelier ?Le montage peut exiger controles de couple, alignement
    et references.
  META: '{"meta_title":"Bougie d''allumage : quand changer ? | AutoMecanik","meta_description":"Démarrage difficile, ratés
    moteur, surconsommation : reconnaître des bougies d''allumage usées et savoir à quel kilométrage les remplacer sur moteur
    essence.","og_title":"Bougies d''allumage usées : ratés moteur et surconsommation","og_description":"Ratés au démarrage,
    voyant moteur allumé ou surconsommation ? Des bougies usées en sont la cause. Standard : 30-45 000 km. Iridium/Platine
    : 60-100 000 km.","sources":[{"type":"rag","ref":"gammes/bougie-d- allumage.md","field":"diagnostic.symptoms,domain.role,rendering.faq"}]}'
---

# Bougie d'allumage - Guide Diagnostic Complet

## Fonction et Rôle

Produire l'etincelle qui enflamme le melange air-essence - Fonctionne en continu moteur tournant

**Actions principales:** produire une etincelle, enflammer, allumer le melange, declencher la combustion, generer l'arc electrique

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- demarrage difficile ou laborieux
- rates moteur a froid ou a l acceleration
- consommation de carburant excessive
- voyant moteur allume code rate d allumage
- odeur essence echappement combustion incomplete
- plus de 40 000 km sans remplacement standard

## Procédure de Diagnostic

Pour diagnostiquer un problème de bougie d'allumage:

1. **Inspection visuelle** - Examiner l'état du bougie d'allumage
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

- alternateur
- bobine-d-allumage
- faisceau-d-allumage
- filtre-a-air
- filtre-a-carburant
- filtre-a-huile
- sonde-lambda

## Critères de Compatibilité

Pour commander le bon bougie d'allumage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"

## FAQ

**Bougie d'allumage standard ou iridium ?**
L'iridium dure 2x plus longtemps et offre une meilleure étincelle. Plus chère mais rentable sur la durée. Respectez les préconisations constructeur.

**Comment savoir si mes bougies d'allumage sont usées ?**
Démarrage difficile, ratés moteur, surconsommation, électrode usée ou encrassée visible au démontage, écartement hors tolérance.

**Tous les combien changer les bougies d'allumage ?**
Standard : 30 000 à 45 000 km. Iridium/Platine : 60 000 à 100 000 km. Vérifier l'écartement tous les 20 000 km.

**Peut-on changer les bougies d'allumage soi-même ?**
Oui, avec une clé à bougie adaptée. Visser à la main d'abord pour éviter de foirer le filetage. Serrage au couple ou 1/4 de tour après contact.

**Quelle erreur éviter avec les bougies d'allumage ?**
Ne pas serrer trop fort (casse la porcelaine). Vérifier l'écartement avant montage. Ne pas mettre de graisse sur le filetage.
## Les critères essentiels

### Types de bougies
- **Cuivre/Nickel** : Standard, durée de vie 20 000-30 000 km. Économiques.
- **Platine** : Électrode en platine, durée de vie 60 000-80 000 km. Étincelle plus stable.
- **Iridium** : Électrode ultra-fine en iridium, durée 80 000-120 000 km. Meilleur allumage, plus chères.
- **Double iridium/platine** : Les deux électrodes sont renforcées. Durée maximale.

### Indice thermique
- L'indice thermique détermine la capacité de la bougie à évacuer la chaleur
- Un indice trop chaud = risque d'auto-allumage. Un indice trop froid = encrassement
- Toujours respecter l'indice préconisé par le constructeur

### Écartement des électrodes
- L'écartement (gap) est calibré en usine selon la référence
- Ne pas modifier l'écartement sur les bougies iridium/platine (risque de casser l'électrode fine)

## Compatibilité moteur

- **Essence uniquement** : Les moteurs diesel n'ont pas de bougies d'allumage (ils utilisent des bougies de préchauffage)
- Respecter la référence constructeur (exemple : NGK BKR6E, Bosch FR7DC+)
- Utiliser le cross-reference des fabricants pour trouver l'équivalence

## Marques recommandées

- **NGK** : Leader mondial, équipementier OE pour de nombreux constructeurs
- **Denso** : Spécialiste iridium, OE pour constructeurs japonais
- **Bosch** : Large gamme, fiable
- **Champion** : Bonne couverture, rapport qualité-prix

## Erreurs à éviter

- Ne jamais mélanger des types de bougies différents sur le même moteur
- Respecter le couple de serrage (risque de casse de culasse si trop serré)
- Ne pas négliger le joint d'étanchéité (neuf à chaque montage)
## Qu'est-ce qu'une référence OEM ?

**OEM** = Original Equipment Manufacturer (Fabricant d'Équipement d'Origine)

La référence OEM est le numéro de pièce attribué par le constructeur automobile.

### Exemple
- **Renault** : 7701207242 (filtre à huile Clio)
- **Peugeot** : 1109AY (filtre à huile 206/207)
- **Volkswagen** : 03L115561 (filtre à huile Golf)

## Pourquoi utiliser la référence OEM ?

### Avantages
1. **Identification exacte** : Aucune confusion possible
2. **Compatibilité garantie** : Pièce identique à l'origine
3. **Recherche facilitée** : Trouve toutes les équivalences

### Comment trouver sa référence OEM ?
1. Sur la pièce d'origine (étiquette, gravure)
2. Dans le carnet d'entretien
3. Chez le concessionnaire avec le numéro de châssis (VIN)
4. Sur notre site via le sélecteur véhicule

## OEM vs Équipementier vs Adaptable

| Type | Qualité | Prix | Exemple |
|------|---------|------|---------|
| **OEM (Origine)** | Constructeur | €€€ | Renault, Peugeot |
| **Équipementier** | Identique OEM | €€ | Bosch, Valeo, TRW |
| **Adaptable** | Compatible | € | Pièces génériques |

### Le saviez-vous ?
Les équipementiers (Bosch, Valeo, etc.) fabriquent les pièces pour les constructeurs. Une pièce Bosch est souvent identique à la pièce "origine" Renault, mais moins chère car sans la marque constructeur.

## Références croisées

Une même pièce peut avoir plusieurs références :

| Constructeur | Référence |
|--------------|-----------|
| Renault | 7701207242 |
| Bosch | F 026 407 136 |
| Mann-Filter | HU 611/1 X |
| Purflux | L330 |

**Toutes ces références désignent le même filtre à huile.**

## Comment utiliser les références sur notre site

### Recherche par référence
1. Entrez la référence OEM ou équipementier
2. Le système trouve la pièce correspondante
3. Toutes les équivalences sont affichées

### Sélecteur véhicule
1. Entrez votre plaque ou VIN
2. Choisissez le type de pièce
3. Les références compatibles s'affichent

## Pièges à éviter

### Références similaires
Attention aux références proches qui désignent des pièces différentes :
- 1109AY ≠ 1109AZ (modèles différents)
- Vérifiez toujours avec votre véhicule exact

### Évolutions de pièces
Le constructeur peut modifier une pièce en cours de production :
- Ancienne réf : 1234A
- Nouvelle réf : 1234B (remplace 1234A)

Notre système prend en compte ces évolutions.

## Conseils pratiques

1. **Notez vos références** : Gardez une liste des pièces de votre véhicule
2. **Photographiez** : L'étiquette de vos pièces d'origine
3. **Utilisez le VIN** : Pour une identification précise
4. **Comparez** : Les équipementiers pour le meilleur rapport qualité/prix
## Le véhicule ne démarre pas

### Rien ne se passe (pas de bruit)
- **Batterie complètement déchargée** : Vérifier la tension aux bornes (< 11.5V = batterie HS ou déchargée). Tester avec un chargeur ou des câbles de démarrage.
- **Bornes de batterie oxydées** : Dépôt blanc-verdâtre sur les cosses. Nettoyer avec une brosse métallique et de la graisse diélectrique.
- **Fusible principal grillé** : Vérifier le fusible de démarreur dans la boîte à fusibles moteur.

### Le démarreur claque sans tourner
- **Solénoïde de démarreur usé** : Le contacteur magnétique fonctionne mais ne peut plus engager le pignon. Remplacement du démarreur nécessaire.
- **Batterie faible** : Assez de courant pour le solénoïde mais pas pour le moteur électrique. Tension entre 11.5V et 12.2V.
- **Mauvaise masse moteur** : Câble de masse entre batterie et bloc moteur corrodé ou desserré.

### Le démarreur tourne mais le moteur ne part pas
- **Problème d'alimentation carburant** : Pompe à carburant HS, filtre à carburant bouché, ou relais de pompe défaillant.
- **Problème d'allumage (essence)** : Bougies encrassées, bobine d'allumage défaillante, capteur vilebrequin HS.
- **Problème d'injection (diesel)** : Injecteurs grippés, préchauffage défaillant (surtout par temps froid), capteur PMH.

## Voyant batterie allumé

- **Alternateur défaillant** : L'alternateur ne charge plus. La batterie se vide progressivement. Vérifier la tension moteur tournant (doit être entre 13.5V et 14.5V).
- **Courroie d'alternateur lâche ou cassée** : Sifflement au démarrage, voyant batterie intermittent.
- **Régulateur de tension HS** : Surcharge ou sous-charge de la batterie.

## Chute de tension intermittente

- **Consommateur parasite** : Un équipement reste sous tension moteur coupé (autoradio, éclairage coffre, etc.). Mesurer le courant de repos (< 50mA normal).
- **Batterie en fin de vie** : Plus de 4-5 ans, la batterie perd sa capacité. Tester avec un testeur de charge.

## Quand consulter un professionnel

- Démarreur qui tourne au ralenti (bruit anormal)
- Fumée ou odeur de brûlé au niveau du démarreur
- Batterie neuve qui se décharge en moins de 48h
- Voyant batterie qui s'allume en roulant
