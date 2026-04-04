---
category: refroidissement
slug: radiateur-de-chauffage
title: Radiateur de chauffage
pg_id: 467
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
  role: Transferer la chaleur du liquide de refroidissement vers l'habitacle pour le confort des passagers. NE REFROIDIT PAS
    LE MOTEUR!
  must_be_true:
  - chauffer
  - transferer
  - diffuser
  must_not_contain:
  - refroidissement moteur
  - ventilateur moteur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - radiateur-de-refroidissement
  - pompe-a-eau
  - thermostat
  - durite-de-refroidissement
  - vase-d-expansion
  - ventilateur-de-refroidissement
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
  - ❌ "refroidit le moteur"
  cost_range:
    min: 50
    max: 200
    currency: EUR
    unit: radiateur
    source: catalogue automecanik
  brands:
    premium:
    - Valeo
    - Behr/Mahle
    - Denso
    standard:
    - Nissens
    - NRF
    - Hella
    budget:
    - Thermotec
    - Frigair
    - AVA
  quality_tiers:
  - tier: Origine constructeur (OE/OES)
    description: Radiateur de chauffage identique a la premiere monte. Echange thermique optimal, dimensions et raccords conformes.
  - tier: Equivalent OE (qualite premiere monte)
    description: Radiateur de chauffage de qualite equivalente, teste en pression. Dimensions et raccords verifies.
  - tier: Adaptable (qualite atelier courant)
    description: Radiateur compatible. Verifier les dimensions exactes et le type de raccords avant commande.
diagnostic:
  symptoms:
  - id: S1
    label: Buee grasse persistante sur le pare-brise
    severity: confort
  - id: S2
    label: Odeur sucree de liquide dans l habitacle
    severity: confort
  - id: S3
    label: Moquette humide cote passager avant
    severity: confort
  - id: S4
    label: Chauffage qui ne chauffe plus ou peu
    severity: confort
  - id: S5
    label: Gargouillement dans le tableau de bord
    severity: confort
  - id: S6
    label: Plus de 15 ans ou fuite averee
    severity: confort
  causes:
  - identifier origine fuite et verifier joints
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  - 'Usure ou defaillance causant : buee grasse persistante sur le pare-brise'
  quick_checks:
  - 'Observer : buee grasse persistante sur le pare-brise ?'
  - Odeur sucree de liquide dans l habitacle ?
  - 'Observer : moquette humide cote passager avant ?'
  - 'Observer : chauffage qui ne chauffe plus ou peu ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Buee grasse persistante sur le pare-brise
  - Odeur sucree de liquide dans l habitacle
  - Moquette humide cote passager avant
  - Chauffage qui ne chauffe plus ou peu
  - Gargouillement dans le tableau de bord
  - Plus de 15 ans ou fuite averee
  good_practices:
  - Controle du niveau de liquide de refroidissement a froid chaque mois
  - Remplacement du liquide selon preconisation constructeur (2-5 ans)
  - Verification des durites et colliers a chaque revision
  - Purge du circuit apres toute intervention sur le refroidissement
rendering:
  pgId: '467'
  intro_title: A quoi sert Radiateur de chauffage ?
  risk_title: Pourquoi remplacer Radiateur de chauffage a temps ?
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
  - question: Radiateur chauffage OE ou adaptable ?
    answer: Les radiateurs OES (Valeo, Behr, Nissens) garantissent un échange thermique optimal. Les adaptables peuvent convenir
      mais vérifiez les dimensions exactes.
  - question: Comment savoir si mon radiateur de chauffage fuit ?
    answer: Buée grasse sur le pare-brise, odeur sucrée dans l'habitacle, moquette humide côté passager, niveau de liquide
      qui baisse.
  - question: Tous les combien changer le radiateur de chauffage ?
    answer: Pas de périodicité. Durée de vie 10 à 15 ans. À remplacer uniquement en cas de fuite ou d'obstruction.
  - question: Peut-on changer le radiateur de chauffage soi-même ?
    answer: Difficile. Accès complexe nécessitant souvent la dépose du tableau de bord. Intervention réservée aux bricoleurs
      expérimentés.
  - question: Quelle erreur éviter avec le radiateur de chauffage ?
    answer: Ne pas négliger une petite fuite qui s'aggravera. Rincer le circuit avant montage pour éviter d'obstruer le nouveau
      radiateur.
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
doc_id: 9b8b5373-18bb-5759-ba64-8786d636438a
content_hash: sha256:b2f969a6f5990300
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
  _source: denso-am.eu + fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 2
  _has_tech_data: true
  types_variants:
  - type: 'hall'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_110__c: '110 °C'
    val_43_a: '43 a'
    val_70__: '70 %'
    val_80__: '80 %'
  materials:
  - materiau: 'aluminium'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le radiateur de chauffage est relié au système deventilation de l''habitacle. Son rôle est d''apporter de la chaleur
    en utilisantle liquide de refroidissement comme source de chauffage. Le radiateur de chauffage est couplé au circuit derefroidissement
    du moteur, est traversé par l''air provenant du système deventilation qui se réchauffe à son contact. La puissance du
    radiateur de chauffage se règlesuivant deux façons : - Par un robinet modérant ledébit de liquide de refroidissement à
    l''intérieur du radiateur de chauffage(les anciens modèles). - Par la modération, par unvolet, du débit d''air traversant
    le radiateur (les modèles récents). Le radiateur de chauffage est situé habituellementsitué derrière La boîte à gants
    directement sous le tableau de bord. En savoir plus : radiateur de chauffage — définition et rôle mécanique 🚨 Bruit Radiateur
    de chauffage : causes et diagnostic'
  S2: 'Ne pas attendre la panne complete pour intervenir. Symptômes d''usure : - buee grasse persistante sur le pare-brise
    - odeur sucree de liquide dans l habitacle - moquette humide cote passager avant - chauffage qui ne chauffe plus ou peu
    - gargouillement dans le tableau de bord - plus de 15 ans ou fuite averee'
  S3: 'Le radiateur de chauffage transfère la chaleur du liquide de refroidissement moteur vers l''air soufflé dans l''habitacle
    par le pulseur. Contrairement au radiateur moteur, il fonctionne à basse pression (0,5 à 1,2 bar) mais avec un débit réduit
    et des canaux de faible diamètre : une tubulure légèrement encrassée ou des dimensions légèrement différentes suffisent
    à diviser par deux la puissance de chauffage. La précision dimensionnelle est déterminante. - Dimensions hors-tout (longueur
    × largeur × épaisseur) — Le radiateur de chauffage est logé dans un boîtier plastique sous le tableau de bord dont les
    dimensions sont fixes. Une variation de ±5 mm sur l''épaisseur (généralement 26 à 45 mm) peut empêcher la fermeture du
    boîtier ou générer des fuites par contrainte mécanique. - Diamètre et orientation des tubulures de raccordement — Les
    tubulures sont de diamètre 16, 19 ou 22 mm selon le véhicule. Leur orientation (parallèles, perpendiculaires, décalées)
    doit correspondre exactement au trajet des durites dans la cloison pare-feu. Un mauvais sens des tubulures impose une
    modification non prévue. - Nombre de rangées et capacité d''échange thermique — Un radiateur à 2 rangées de tubes aluminium
    offre une puissance de chauffe inférieure à un modèle 3 ou 4 rangées. Sur les véhicules de grande taille (monospace, SUV),
    ne pas substituer un modèle moins performant que l''origine, au risque d''un chauffage insuffisant par temps froid (−10
    °C ou moins). - Matériau : aluminium/plastique ou cuivre/laiton — Les radiateurs modernes sont en aluminium avec boîtes
    collectrices plastique. Les véhicules anciens (avant 1995 environ) utilisent du cuivre-laiton. Ces deux matériaux ne sont
    pas interchangeables en raison des différences de soudure et de fixation. Vérifier le matériau d''origine. - Sens de circulation
    du liquide (entrée/sortie) — L''entrée du liquide chaud doit correspondre à la tubulure connectée à la sortie de culasse.
    Une inversion entrée/sortie réduit l''efficacité thermique de 15 à 25 % sans autre symptôme apparent qu''un chauffage
    moins puissant. - Type de joint d''étanchéité périmétrique — Le joint mousse ou caoutchouc qui assure l''étanchéité entre
    le radiateur et le boîtier doit être intact. Certains fabricants livrent ce joint avec la pièce neuve ; d''autres non.
    Vérifier avant montage pour éviter de remontages à cause de fuites d''air froid qui contournent le radiateur. - Pièces
    à contrôler lors du remplacement — Purger intégralement le circuit de refroidissement et contrôler l''état des durites
    de chauffage (durcissement, fissures) et des colliers de serrage. Remplacer le liquide de refroidissement si la dernière
    vidange dépasse 5 ans. Pour aller plus loin : consultez notre guide d''achat radiateur de chauffage — comparatif marques,
    critères de choix et prix.'
  S4_DEPOSE: 📖 Avant de démonter, consultez la fiche technique Radiateur de chauffage pour connaître les spécifications. -
    Débranchez la batterie. - Vidanger le liquide de refroidissement. - Démontez le volant de direction. - Démontez tous le
    tableau de bord. - Débranchez tous les connecteurs au niveaudu tableau de bord. - Retirez le tableau de bord. - Démontez
    les canalisations du radiateur dechauffage situé dans le compartiment moteur. - Démontez le boîtier de chauffage. - Reculez
    le boîtier de chauffage puisdémontez le radiateur de chauffage.
  S4_REPOSE: '- Vérifiez que le radiateurde chauffage neuf est identique à celui démonté. - Contrôlez l''état duradiateur
    de refroidissement et le remplacé si nécessaire. - Remontez le radiateur de chauffage. - Remontez le boîtier dechauffage.
    - Serrez les vis du boîtier dechauffage. - Remontez lescanalisations du radiateur de chauffage situé dans le compartiment
    moteur. - Remontez le tableaude bord. - Remontez le volantde direction. - Remplissez le liquidede refroidissement. - Rebranchez
    labatterie. - Contrôler le bonfonctionnement du circuit de chauffage. ✅ Après remontage, vérifiez les spécifications dans
    la fiche technique Radiateur de chauffage.'
  S5: 'Erreurs frequentes avec le radiateur de chauffage : - Ne pas verifier l''etat du liquide de refroidissement avant de
    remplacer le radiateur — un liquide non entretenu corrode le radiateur neuf de l''interieur- Oublier de purger le circuit
    de refroidissement apres remplacement — une bulle d''air bloque la circulation du liquide et le chauffage ne fonctionne
    plus- Confondre un probleme de vanne de chauffage avec un radiateur defaillant — tester d''abord la commande de temperature
    et le cable de commande- Ignorer une odeur sucree dans l''habitacle — signe de micro-fuite du radiateur de chauffage,
    le liquide de refroidissement s''evapore dans l''habitacle- Ne pas proteger le tableau de bord et la moquette lors du
    demontage — le liquide de refroidissement tache et corrode les revetements- Sous-estimer le temps d''intervention — le
    radiateur de chauffage est souvent derriere le tableau de bord, comptez 3 a 6 heures'
  S6: 'Le radiateur de chauffage est positionné dans le boîtier de chauffage, derrière la planche de bord. Son remplacement
    est une intervention lourde qui impose une purge complète du circuit de refroidissement et une vérification systématique
    avant de reposer l''intégralité des habillages intérieurs. Ce radiateur transfère la chaleur du liquide de refroidissement
    vers l''habitacle — il ne refroidit pas le moteur. - Purge du circuit de refroidissement : après remontage des durites
    de chauffage, purger le circuit en ouvrant les vis de purge (souvent situées sur le boîtier de thermostat ou sur la durite
    haute) jusqu''à obtention d''un flux de liquide sans bulles. Un circuit non purgé produit des gargouillements dans le
    tableau de bord et une inefficacité du chauffage. - Absence de buée grasse sur le pare-brise : démarrer le moteur, chauffer
    l''habitacle au maximum, désembuer le pare-brise. Si une buée translucide à odeur sucrée de glycol se dépose sur la vitre
    intérieure, le radiateur présente une micro-fuite interne. Ce symptôme impose le démontage et le remplacement sans délai.
    - Contrôle de l''absence d''humidité sous la planche de bord : après 10 à 15 minutes de chauffage à plein régime, inspecter
    la moquette côté passager avant et sous la planche de bord. Aucune trace d''humidité ni de liquide de refroidissement
    ne doit être présente. Une moquette humide signale une fuite du radiateur ou d''une durite de connexion. - Test de la
    montée en température du chauffage : à partir d''un moteur froid, le chauffage doit produire de l''air chaud au niveau
    des buses (température supérieure à 40 °C mesurée à l''aérateur) dans les 5 à 7 minutes suivant le démarrage. Une montée
    lente indique une bulle d''air résiduelle dans le radiateur de chauffage. - Vérification du niveau de liquide de refroidissement
    : contrôler le niveau dans le vase d''expansion après le premier cycle thermique complet (moteur chaud puis refroidi).
    Un niveau qui baisse sans fuite visible extérieure indique une absorption interne — potentiellement une micro-fuite du
    radiateur de chauffage vers la moquette. - Contrôle des attaches et des durites : s''assurer que les deux durites de connexion
    au radiateur de chauffage sont bien fixées avec les colliers d''origine ou des colliers neufs, et qu''elles ne frottent
    pas contre des éléments de structure lors des mouvements moteur. Un frottement prolongé peut provoquer une usure prématurée
    de la durite.'
  S7: Quel est le prix d'un radiateur de chauffage ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur
    pour trouver le radiateur de chauffage compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon radiateur de chauffage est à changer ?Les signes d'usure les plus courants sont détaillés dans la section
    diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un radiateur
    de chauffage défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule.
    Consultez la section symptômes pour évaluer l'urgence du remplacement.Filtre d'habitacle . 📖 Fiche technique Radiateur
    de chauffage — intervalles et spécifications d’entretien.
  S8: Comment choisir Radiateur de chauffage compatible avec mon vehiculeRenseignez marque, modele, type moteur et annee,
    puis verifiez la reference Quand remplacer Radiateur de chauffage ?En cas de buee grasse persistante sur le pare-brise
    ou de degradation Puis-je monter Radiateur de chauffage sans verification atelier ?Le montage peut exiger controles de
    couple, alignement et references.
  META: '{"meta_title":"Radiateur de chauffage : fuite et remplacement | AutoMecanik","meta_description":"Buée grasse sur
    le pare-brise, odeur sucrée dans l''habitacle, moquette humide : détecter une fuite de radiateur de chauffage et savoir
    quand intervenir.","og_title":"Radiateur de chauffage qui fuit : buée et odeur sucrée","og_description":"Buée persistante
    sur le pare-brise ou odeur sucrée dans l''habitacle ? Une fuite du radiateur de chauffage en est souvent la cause. Guide
    diagnostic et remplacement.","sources":[{"type":"rag","ref":"gammes/radiateur-de- chauffage.md","field":"diagnostic.symptoms,domain.role,rendering.faq"}]}'
---

# Radiateur de chauffage - Guide Diagnostic Complet

## Fonction et Rôle

Transferer la chaleur du liquide de refroidissement vers l'habitacle pour le confort des passagers. NE REFROIDIT PAS LE MOTEUR!

**Actions principales:** chauffer, transferer, diffuser, rechauffer l'habitacle

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- buee grasse persistante sur le pare-brise
- odeur sucree de liquide dans l habitacle
- moquette humide cote passager avant
- chauffage qui ne chauffe plus ou peu
- gargouillement dans le tableau de bord
- plus de 15 ans ou fuite averee

## Procédure de Diagnostic

Pour diagnostiquer un problème de radiateur de chauffage:

1. **Inspection visuelle** - Examiner l'état du radiateur de chauffage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- commande-de-ventilation
- filtre-d-habitacle
- pulseur-d-air-d-habitacle
- radiateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon radiateur de chauffage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidit le moteur"

## FAQ

**Radiateur chauffage OE ou adaptable ?**
Les radiateurs OES (Valeo, Behr, Nissens) garantissent un échange thermique optimal. Les adaptables peuvent convenir mais vérifiez les dimensions exactes.

**Comment savoir si mon radiateur de chauffage fuit ?**
Buée grasse sur le pare-brise, odeur sucrée dans l'habitacle, moquette humide côté passager, niveau de liquide qui baisse.

**Tous les combien changer le radiateur de chauffage ?**
Pas de périodicité. Durée de vie 10 à 15 ans. À remplacer uniquement en cas de fuite ou d'obstruction.

**Peut-on changer le radiateur de chauffage soi-même ?**
Difficile. Accès complexe nécessitant souvent la dépose du tableau de bord. Intervention réservée aux bricoleurs expérimentés.

**Quelle erreur éviter avec le radiateur de chauffage ?**
Ne pas négliger une petite fuite qui s'aggravera. Rincer le circuit avant montage pour éviter d'obstruer le nouveau radiateur.
## Climatisation sans effet

### Pas de froid
- **Manque de gaz réfrigérant** : Fuite dans le circuit. Le compresseur ne s'enclenche pas ou tourne en continu sans refroidir. Recharge + recherche de fuite nécessaire.
- **Compresseur bloqué** : Embrayage de compresseur HS, bruit métallique, courroie qui patine.
- **Condenseur obstrué** : Débris, feuilles ou insectes devant le condenseur (devant le radiateur). Nettoyage au jet doux.
- **Détendeur bloqué** : Le gaz ne se détend plus correctement, givrage possible sur les tuyaux.

### Odeurs dans l'habitacle
- **Filtre habitacle encrassé** : Odeur de moisi à la mise en route de la ventilation. Remplacement tous les 15 000-20 000 km.
- **Évaporateur contaminé** : Bactéries et moisissures sur l'évaporateur. Traitement antibactérien recommandé.

## Chauffage défaillant

### Pas de chaleur
- **Niveau de liquide de refroidissement bas** : Le radiateur de chauffage n'est pas alimenté. Vérifier le niveau et faire l'appoint.
- **Thermostat bloqué ouvert** : Le moteur ne monte pas en température. L'aiguille reste basse même après 10 minutes de conduite.
- **Radiateur de chauffage bouché** : Les deux durites d'entrée/sortie doivent être chaudes moteur à température. Si une seule est chaude, le radiateur est obstrué.

### Ventilation faible
- **Résistance de ventilateur grillée** : Seule la vitesse maximale fonctionne, les autres vitesses sont inactives.
- **Moteur de ventilateur fatigué** : Bruit de frottement, débit d'air réduit.

## Quand consulter un professionnel

- Compresseur bruyant (risque de blocage et casse courroie)
- Fuite de gaz réfrigérant visible (traces d'huile sur les raccords)
- Odeur sucrée dans l'habitacle (fuite de liquide de refroidissement dans le radiateur de chauffage)
- Surchauffe moteur associée à un problème de chauffage


## References supplementaires

<!-- materialized-from-db manual/cc5f4e879fe9 2026-04-03 -->
### Données techniques OEM — Radiateur de chauffage

# Données techniques OEM — Radiateur de chauffage
Source : denso-am.eu + fr.wikipedia.org (2 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- hall
- électrique

## Matériaux
- aluminium

## Valeurs techniques de référence
- 110 °C
- 70 %
- 80 %

## Symptomes supplementaires

<!-- materialized-from-db diagnostic/climatisation.md 2026-02-15 -->
### Diagnostic - Climatisation et chauffage

# Climatisation et chauffage - Diagnostic complet

## Climatisation sans effet

### Pas de froid
- **Manque de gaz réfrigérant** : Fuite dans le circuit. Le compresseur ne s'enclenche pas ou tourne en continu sans refroidir. Recharge + recherche de fuite nécessaire.
- **Compresseur bloqué** : Embrayage de compresseur HS, bruit métallique, courroie qui patine.
- **Condenseur obstrué** : Débris, feuilles ou insectes devant le condenseur (devant le radiateur). Nettoyage au jet doux.
- **Détendeur bloqué** : Le gaz ne se détend plus correctement, givrage possible sur les tuyaux.

### Odeurs dans l'habitacle
- **Filtre habitacle encrassé** : Odeur de moisi à la mise en route de la ventilation. Remplacement tous les 15 000-20 000 km.
- **Évaporateur contaminé** : Bactéries et moisissures sur l'évaporateur. Traitement antibactérien recommandé.

## Chauffage défaillant

### Pas de chaleur
- **Niveau de liquide de refroidissement bas** : Le radiateur de chauffage n'est pas alimenté. Vérifier le niveau et faire l'appoint.
- **Thermostat bloqué ouvert** : Le moteur ne monte pas en température. L'aiguille reste basse même après 10 minutes de conduite.
- **Radiateur de chauffage bouché** : Les deux durites d'entrée/sortie doivent être chaudes moteur à température. Si une seule est chaude, le radiateur est obstrué.

### Ventilation faible
- **Résistance de ventilateur grillée** : Seule la vitesse maximale fonctionne, les autres vitesses sont inactives.
- **Moteur de ventilateur fatigué** : Bruit de frottement, débit d'air réduit.

## Quand consulter un professionnel

- Compresseur bruyant (risque de blocage et casse courroie)
- Fuite de gaz réfrigérant visible (traces d'huile sur les raccords)
- Odeur sucrée dans l'habitacle (fuite de liquide de refroidissement dans le radiateur de chauffage)
- Surchauffe moteur associée à un problème de chauffage
