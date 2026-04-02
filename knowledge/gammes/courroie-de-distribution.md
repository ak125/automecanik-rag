---
category: distribution
slug: courroie-de-distribution
title: Courroie de distribution
pg_id: 306
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
  role: Kit complet pour la synchronisation de la distribution avec tous les composants necessaires
  must_be_true:
  - synchroniser
  - entrainer
  - maintenir
  must_not_contain:
  - chaine
  - universel
  - tous moteurs
  - adaptable
  confusion_with:
  - term: chaine-de-distribution
    difference: Courroie = caoutchouc à remplacer, Chaîne = métal plus durable
  - term: courroie-d-accessoire
    difference: Courroie distribution = synchronise moteur (CRITIQUE), Courroie accessoire = alternateur/clim (moins critique)
  related_parts:
  - kit-de-distribution
  - galet-tendeur-de-courroie-de-distribution
  - galet-enrouleur-de-courroie-de-distribution
  - pompe-a-eau
selection:
  criteria:
  - Marque de votre véhicule
  - Modele de votre véhicule
  - Motorisation de votre véhicule
  - Annee de votre véhicule
  anti_mistakes:
  - ❌ "évite la casse moteur"
  - ❌ "sécurité garantie"
  - ❌ "garanti CT"
  cost_range:
    min: 19
    max: 38
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Pièce OE (Origine Équipement)
    description: Courroie identique à l origine, fabriquée selon les spécifications exactes du constructeur. Option recommandée
      sur moteurs fragiles (moteurs interférents).
  - tier: Kit distribution complet (équivalent OE)
    description: Kit incluant courroie, galets tendeurs et galet enrouleur. Les fabricants de rang 1 fournissent les constructeurs
      automobiles.
  - tier: Courroie seule sans galets
    description: Remplacer la courroie sans les galets n est pas recommandé. Les galets usés peuvent casser une courroie neuve
      rapidement.
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
    label: Aucun symptome visible courroie casse
    severity: confort
  - id: S2
    label: Echeance kilometrique ou temps depassee
    severity: confort
  - id: S3
    label: Traces de craquelures sur la courroie si visible
    severity: confort
  - id: S4
    label: Bruit de claquement cote distribution
    severity: confort
  - id: S5
    label: Fuite de liquide de refroidissement pompe a eau
    severity: confort
  - id: S6
    label: Jeu dans le galet tendeur
    severity: confort
  - id: S7
    label: Courroie effilochee sur les bords
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  quick_checks:
  - 'Observer : aucun symptome visible courroie casse ?'
  - 'Observer : echeance kilometrique ou temps depassee ?'
  - 'Observer : traces de craquelures sur la courroie si visible ?'
  - Bruit de claquement cote distribution ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Aucun symptome visible courroie casse
  - Echeance kilometrique ou temps depassee
  - Traces de craquelures sur la courroie si visible
  - Bruit de claquement cote distribution
  - Fuite de liquide de refroidissement pompe a eau
  - Jeu dans le galet tendeur
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '306'
  intro_title: A quoi sert Courroie de distribution ?
  risk_title: Pourquoi remplacer Courroie de distribution a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Défaillance progressive** - Usure normale due à l''utilisation'
  - '**Conditions d''utilisation** - Sollicitations excessives ou environnement défavorable'
  - ❌ "évite la casse moteur"
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
  - question: Comment choisir Courroie de distribution compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Courroie de distribution ?
    answer: En cas de aucun symptome visible courroie casse ou de degradation mesurable, il faut controler rapidement avant
      panne secondaire.
  - question: Puis-je monter Courroie de distribution sans verification atelier ?
    answer: Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure
      constructeur.
  quality:
    score: 76
    source: script:rag-upgrade-v4
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous moteurs
  - adaptable
  requires_vehicle: true
doc_id: e616e207-a589-5a29-83a5-70701bebe187
content_hash: sha256:3bb2b16c0b2283ce
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
  _source: bremboparts.com + denso-am.eu + textar.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 13
  types_variants:
  - type: 'hall'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_10_nm: '10 Nm'
    val_115_nm: '115 Nm'
    val_125_nm: '125 Nm'
    val_15_a: '15 a'
    val_16_nm: '16 Nm'
    val_16_a: '16 a'
    val_18_mm: '18 mm'
    val_180_nm: '180 Nm'
    val_20_nm: '20 Nm'
    val_20_mm: '20 mm'
    val_210_nm: '210 Nm'
    val_22_nm: '22 Nm'
    val_26_a: '26 A'
    val_29_a: '29 a'
    val_3_a: '3 a'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'La courroie de distributionest une courroie crantée, entraînée par la roue dentée de vilebrequin. Lacourroie de distribution
    fait le lien entre la pompe injection (pour lesmoteurs diesels), le vilebrequin, la pompeà eau (suivant le niveau d''équipement
    de votre motorisation) et les arbres àcames qui commandent les soupapes d''admission et les soupapesd''échappement. La
    courroie de distribution est donc très sollicitée,notamment aux démarrages.On démarrant le moteur la courroie de distribution
    estentraînée en mouvement depuis le vilebrequin par l''intermédiaire de la rouedentée et le mouvement arrivera à la poulie
    d''arbre à cames en fonction de la courroie dedistribution et du galet tendeur. - Le galet tendeur de distribution, safonction
    est de mettre sous tension la courroie et de préserver son alignement.Le réglage du galet est indiqué par le constructeur.
    - La pompe à eau , elle apour fonction de faire circuler le liquide de refroidissement. Sans elle, lemoteur chauffe et
    casse. En savoir plus : courroie de distribution — définition et rôle mécanique 🚨 Bruit Courroie de distribution : causes
    et diagnostic'
  S2: 'Pour savoir si la courroie dedistribution est à remplacer : - Contrôler visuellement l''état de la courroiede distribution.
    - Des dents creusées ou usée. - Des craquelures au dos de la courroie crantée. - Une usure excessive entre les dents.
    - Un décollement des dents. - Une courroie crantée huilée. - Un sifflement au niveau de la courroiede distribution. -
    Un bruit de roulement au niveau des galets. Si la courroie de distribution est HS et qu''elle n''estpas remplacée à temps
    et elle se rompe, il risque d''avoir une casse moteur avecdes effets irréversible avec de grave détérioration des arbres
    à cames etdu vilebrequin avec des frais de réparation élevée.C''est pour cela que nous vous conseillons qu''ilsera plus
    convenable de ne pas dépassé les 120 000 km pour remplacer le kit de distribution . Diagnostic complet : identifier une
    panne de courroie de distribution'
  S3: 'La courroie de distribution synchronise la rotation du vilebrequin et des arbres à cames : elle garantit que les soupapes
    s''ouvrent et se ferment au bon moment par rapport aux pistons. Une casse de courroie de distribution provoque, sur la
    quasi-totalité des moteurs interférents, un choc pistons- soupapes entraînant une destruction moteur dont le coût dépasse
    souvent 3 000 à 5 000 €. À ne pas confondre avec la courroie d''accessoire (alternateur/clim), ni avec la chaîne de distribution
    (métal, pas de remplacement périodique). Les intervalles constructeurs vont de 60 000 à 150 000 km selon le moteur. Voici
    les critères à maîtriser avant de commander. - Référence moteur et code motorisation obligatoires — Contrairement à la
    courroie d''accessoire, la courroie de distribution est spécifique au code moteur (exemple : 1.6 TDI code CAYB ≠ 1.6 TDI
    code CAYA). Sur un même modèle de véhicule, deux codes moteurs peuvent nécessiter des courroies de longueur ou de pas
    différent. Ne commander qu''avec le code moteur gravé sur le bloc, pas uniquement avec la cylindrée. - Pas de la courroie
    (nombre de dents) — Le pas (exprimé en mm ou en nombre de dents sur le pourtour) détermine la synchronisation exacte.
    Une courroie avec un dent de trop ou de moins décale le calage de distribution de plusieurs degrés : pertes de puissance
    mesurables et risque de casse à haute charge. - Kit complet ou courroie seule — Le remplacement par kit complet (courroie
    + galet tendeur + galet enrouleur + pompe à eau sur les moteurs dont la pompe est entraînée par la courroie) est systématiquement
    préférable à la courroie seule. Le coût de main-d''œuvre représente 70 à 80 % du total : remplacer uniquement la courroie
    et laisser en place un galet à roulement usé reviendra à refaire l''opération quelques milliers de km plus tard. - Largeur
    de la courroie (en mm) — La largeur conditionne la résistance à la traction. Un moteur 2.0 TDI exige une courroie plus
    large (25 à 30 mm) qu''un moteur 1.0 essence (15 à 19 mm). Une courroie de largeur insuffisante amorce une fissuration
    par fatigue des flancs dès les premières accélérations à pleine charge. - Compatibilité avec la pompe à eau — Sur les
    moteurs à pompe à eau entraînée par la courroie de distribution, le débit de la pompe neuve doit correspondre exactement
    aux spécifications d''origine. Une pompe à eau de remplacement avec un rotor de diamètre différent modifie la tension
    de courroie lors des montées en température. - Procédure de calage moteur avant dépose — Avant de retirer l''ancienne
    courroie, poser les outils de calage constructeur (broches de blocage arbres à cames et vilebrequin) pour mémoriser la
    position de distribution. Sans cet outillage, le risque de décalage d''un ou plusieurs dents lors du remontage est élevé,
    même pour un technicien expérimenté. Pour aller plus loin : consultez notre guide d''achat courroie de distribution —
    comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 📖 Avant de démonter, consultez la fiche technique Courroie de distribution pour connaître les spécifications.
    - Débranchez la batterie. - Levez et calez le véhicule. - Démontez la roue avant droite. - Démontez l'écran pare- boue
    avant droit. - Démontez les vis de fixation de la protectionsous moteur. - Démontez la protection sous moteur. - Repérez
    le cheminement de la courroied'accessoires. - Démontez la courroie d'accessoires. - Démontez la poulie devilebrequin.
    - Soutenez le moteur à l'aide d'un cric et unecale de bois. - Démontez le supportmoteur et la biellette desuspension moteur-boîte
    (sinécessaire). - Démontez les carters de la courroie dedistribution. - Repérez le cheminement de la courroiede distribution.
    - Tournez le moteur à la main dans le senshoraire (côté distribution), pour positionner le trou de l'arbre à cames quasimenten
    face du trou de la culasse. - Déposez le bouchon de la pige du point morthaut. - Vissez la pige à fond dans le trou du
    pointmort haut. - Tournez le moteur à la main dans le senshoraire (côté distribution), jusqu'au blocage du moteur sur
    la pige. - Immobilisez la poulie d'arbre à cames avecune pige appropriée. - Vérifiez la position de calage du moteur.
    - Desserrez la fixation du galet tendeurde distribution. - Démontez la courroie de distribution. - Démontez le galet tendeurde
    distribution. - Démontez le galetenrouleur de distribution.
  S4_REPOSE: 'Le remontage de la courroie de distribution est l''opération de précision la plus critique sur un moteur à courroie.
    Un écart d''une dent sur les pignons de calage provoque un désynchronisation de l''allumage et de l''injection. Sur les
    moteurs à pistons interférents (majorité des diesels et de nombreux essences), une dent de décalage suffit à provoquer
    un contact soupapes- pistons au premier démarrage. - Vérifiez que la courroie de distribution neuve a le même nombre de
    dents que celle démontée. Comptez les dents sur les deux courroies avant de procéder au montage. Un écart annule la garantie
    constructeur sur le moteur. - Changez systématiquement le galet tendeur de distribution et le galet enrouleur de distribution
    en même temps que la courroie. Des galets neufs sur une courroie usée, ou des galets usés sur une courroie neuve, sont
    tous deux sources de défaillance précoce. - Contrôlez le bon fonctionnement de la pompe à eau : tournez-la à la main —
    elle doit tourner sans jeu ni résistance anormale. Si la pompe présente un roulement rugueux ou une fuite de l''axe, remplacez-la
    maintenant (l''accès est libre et le coût marginal). - Remontez les galets tendeur et enrouleur et contrôlez la position
    des repères du galet tendeur par rapport à la culasse (selon constructeur, flèche ou trait de référence aligné). - Contrôlez
    la position des repères de la poulie d''arbre à cames et de la roue dentée de vilebrequin avec les piges de calage constructeur.
    Ne procédez au montage de la courroie que si le moteur est en position point mort haut cylindre 1 confirmée. - Remettez
    en place la courroie de distribution neuve en respectant scrupuleusement le cheminement et le sens de montage (flèche
    imprimée sur la courroie indique le sens de rotation). Commencez par le pignon de vilebrequin, puis l''enrouleur, puis
    l''arbre à cames, puis le tendeur. - Réglez la tension de la courroie avec le galet tendeur selon la méthode constructeur.
    Sur les tendeurs automatiques : relâchez la bride de blocage et laissez le tendeur prendre sa position libre. Sur les
    tendeurs manuels : amenez le repère mobile jusqu''au repère fixe puis serrez l''écrou au couple prescrit. - Tournez le
    vilebrequin 6 tours à la main dans le sens horaire (côté distribution). Vérifiez que les piges de calage se réengagent
    sans forcer dans les trous constructeur. Si les piges refusent de s''engager, le calage est incorrect — recommencez depuis
    l''étape 5. - Démontez les piges et outils de calage. Remontez les carters de distribution, le support moteur, la poulie
    de vilebrequin (au couple prescrit, souvent 100 à 150 N·m + angle), la courroie d''accessoires, le pare-boue et la roue.
    - Descendez le véhicule. Rebranchez la batterie. Démarrez et vérifiez l''absence de bruit anormal (claquement, sifflement).
    Après 500 km, vérifiez la tension de la courroie si le galet est manuel. Contrôlez l''absence de code défaut de calage
    (P0016, P0017, P0018, P0019) à la valise OBD.'
  S5: 'La courroie de distribution est la pièce mécanique la plus critique du moteur : sa rupture provoque une casse moteur
    immédiate sur les moteurs dits "interférents". Les erreurs de remplacement sont malheureusement fréquentes et souvent
    coûteuses. Voici les cinq erreurs les plus graves à éviter. - Remplacer uniquement la courroie sans changer les galets
    et la pompe à eau — La courroie, les galets tendeur et enrouleur, et la pompe à eau (si entraînée par la courroie) vieillissent
    ensemble. Changer uniquement la courroie en conservant des galets usés, c''est courir le risque d''une casse dans les
    mois suivants. Le coût d''un kit complet (courroie + galets + pompe) représente 20 à 30% du coût d''une casse moteur.
    Conséquence : moteur cassé sur des galets neufs à 50 000 km. - Ne pas respecter le calage distribution — La courroie synchronise
    précisément le vilebrequin et l''arbre à cames. Un décalage d''une seule dent provoque une perte de puissance, des ratés,
    voire une casse moteur immédiate sur les moteurs interférents (pistons percutent les soupapes). Toujours se référer aux
    marques de calage constructeur et utiliser les outils de calage spécifiques au moteur. - Monter la courroie sans respecter
    le sens de montage — Les courroies crantées ont un sens de rotation défini. Un montage à l''envers (même si la courroie
    "rentre") désynchronise les crans et provoque immédiatement un calage incorrect. Vérifier systématiquement la flèche de
    direction gravée sur la courroie. - Ne pas respecter la tension prescrite — Une courroie trop lâche glisse et saute de
    dents. Trop tendue, elle usure prématurément les roulements des galets et de la pompe à eau, et peut se rompre sous contrainte
    thermique. Utiliser un outil de mesure de tension homologué (comparateur vibratoire) pour atteindre la tension constructeur.
    Ne pas se fier à l''impression tactile. - Négliger le couple de serrage des boulons — Les boulons de poulie de vilebrequin
    et d''arbre à cames sont souvent à serrage angulaire (plastique) et doivent être remplacés. Les serrer sans clé dynamométrique
    ou réutiliser des boulons usagés expose à un desserrage pendant la marche, avec destruction immédiate de la distribution.
    Utiliser systématiquement la clé dynamométrique et des boulons neufs si prescrit.'
  S6: 'Le remplacement de la courroie de distribution est l''intervention la plus critique en termes de conséquences en cas
    d''erreur. Une courroie mal calée de quelques dents suffit à provoquer une collision soupapes/pistons et détruire le moteur
    au premier démarrage. Les vérifications suivantes sont non négociables. - Contrôler le calage de la distribution avant
    le premier démarrage : avec le moteur en position PMH (point mort haut), vérifier que tous les repères de calage sont
    alignés simultanément — repère du vilebrequin sur le carter inférieur et repères des arbres à cames sur le cache-culasse.
    Toute discordance d''un seul cran impose de recommencer le calage. - Vérifier le couple de serrage des galets : le galet
    tendeur et le galet enrouleur doivent être serrés aux couples préconisés par le constructeur (généralement 20 à 45 Nm
    selon le moteur). Un galet sous-serré se desserre en fonctionnement et fait perdre la tension de courroie. - Contrôler
    la tension de la courroie après le premier démarrage : sur les systèmes à tendeur hydraulique, vérifier que le témoin
    de position du tendeur est dans la plage verte. Sur les tendeurs mécaniques, la courroie ne doit pas vibrer ni claquer
    entre les galets. - Écouter les premiers tours moteur : les 30 premières secondes de fonctionnement sont déterminantes.
    Tout claquement sec ou bruit métallique à froid impose un arrêt immédiat et un contrôle du calage. Ne pas dépasser 1 000
    tr/min lors de ce premier démarrage. - Vérifier l''absence de fuite de liquide de refroidissement : si la pompe à eau
    a été remplacée simultanément (ce qui est fortement conseillé), inspecter la bride de pompe et les durites adjacentes
    après 5 minutes de chauffe. Toute fuite sur la pompe neuve impose un arrêt avant que le moteur ne surchauffe. - Contrôler
    le niveau d''huile moteur : lors du démontage de la distribution, des projections d''huile peuvent réduire le niveau.
    Vérifier la jauge avant le premier démarrage et compléter si nécessaire. Un moteur insuffisamment lubrifié après une distribution
    neuve est une cause fréquente de casse précoce. - Effectuer un premier trajet court à régime modéré : les 50 premiers
    km, maintenir le régime sous 3 000 tr/min et éviter les fortes accélérations. Après ce trajet, contrôler visuellement
    la courroie depuis les trappes d''accès pour détecter tout déplacement latéral ou usure de bord.'
  S7: Quel est le prix d'un courroie de distribution ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur
    pour trouver le courroie de distribution compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon courroie de distribution est à changer ?Les signes d'usure les plus courants sont détaillés dans la section
    diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un courroie
    de distribution défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du
    véhicule. Consultez la section symptômes pour évaluer l'urgence du remplacement.- courroie d accessoire - galet enrouleur
    de courroie d accessoire - galet tendeur de courroie d accessoire - kit de distribution - pompe a eau - poulie d arbre
    a came - poulie vilebrequin
  S8: Comment choisir Courroie de distribution compatible avec mon vehiculeRenseignez marque, modele, type moteur et annee,
    puis verifiez la reference Quand remplacer Courroie de distribution ?En cas de aucun symptome visible courroie casse ou
    de degradation mesurable, Puis-je monter Courroie de distribution sans verification atelier ?Le montage peut exiger controles
    de couple, alignement et references.
  META: '{"meta_title":"Courroie de distribution : quand changer ? | AutoMecanik","meta_description":"Kilométrage dépassé,
    craquelures ou bruit côté distribution ? Ne pas attendre la casse moteur. Guide symptômes, intervalles et compatibilité
    par motorisation."}'
---

# Courroie de distribution - Guide Diagnostic Complet

## Fonction et Rôle

Kit complet pour la synchronisation de la distribution avec tous les composants necessaires

**Actions principales:** synchroniser, entrainer, maintenir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Aucun symptome visible courroie casse**
  aucun symptome visible courroie casse
- **Bruit de claquement cote distribution**
  bruit de claquement cote distribution

### 🟢 Autres Symptômes

- echeance kilometrique ou temps depassee
- traces de craquelures sur la courroie si visible
- fuite de liquide de refroidissement pompe a eau
- jeu dans le galet tendeur
- courroie effilochee sur les bords

## Procédure de Diagnostic

Pour diagnostiquer un problème de courroie de distribution:

1. **Inspection visuelle** - Examiner l'état du courroie de distribution
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-d-accessoire
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- kit-de-distribution
- pompe-a-eau
- poulie-d-arbre-a-came
- poulie-vilebrequin

## ⚠️ Ne Pas Confondre Avec

### courroie-d-accessoire
**Distinction:** Courroie distribution = synchronise moteur (CRITIQUE), Courroie accessoire = alternateur/clim (moins critique)

### chaine-de-distribution
**Distinction:** Courroie = caoutchouc à remplacer, Chaîne = métal plus durable

## Critères de Compatibilité

Pour commander le bon courroie de distribution, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Motorisation** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "évite la casse moteur"
- ❌ "sécurité garantie"
- ❌ "garanti CT"

## FAQ

**Comment choisir Courroie de distribution compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Courroie de distribution ?**
En cas de aucun symptome visible courroie casse ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Courroie de distribution sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
## Composition d'un kit complet

### Kit standard
- Courroie de distribution
- Galet tendeur
- Galet(s) enrouleur(s)

### Kit complet (recommande)
- Kit standard +
- Pompe a eau
- Courroie accessoires (option)

## Criteres de choix

### 1. Reference exacte
- **OEM** : Reference constructeur (ex: 0831V4 PSA)
- **Equivalence** : Cross-reference equipementier
- **Verification** : Nombre de dents, largeur, profil

### 2. Qualite courroie
| Materiau | Avantage | Duree vie |
|----------|----------|-----------|
| HNBR | Standard, fiable | 120 000 km |
| EPDM | Resistant chaleur | 160 000 km |
| HSN | Haute performance | 180 000 km |

### 3. Pompe a eau incluse?
- **Recommande** : Toujours remplacer avec
- **Raison** : Meme niveau d'usure, cout main d'oeuvre
- **Exception** : Pompe a eau entrainee par courroie accessoires

## Marques de reference

### Premiere monte
| Marque | Constructeurs |
|--------|---------------|
| **Gates** | PSA, Renault, VAG |
| **Contitech** | VAG, BMW, Mercedes |
| **Dayco** | Fiat, Alfa, Lancia |
| **INA** | VAG, BMW |

### Alternative qualite
| Marque | Commentaire |
|--------|-------------|
| **SKF** | Kits complets haute qualite |
| **Febi** | Bonne alternative |
| **Quinton Hazell** | Budget, garantie 2 ans |

## Intervalles par constructeur

### PSA (Peugeot/Citroen)
| Moteur | Intervalle |
|--------|------------|
| TU (1.0-1.6) | 80 000 km / 5 ans |
| DV4/DV6 HDi | 100 000 km / 10 ans |
| DW10 HDi | 120 000 km / 6 ans |
| EB PureTech | 100 000 km / 10 ans |

### Renault
| Moteur | Intervalle |
|--------|------------|
| K4M/K7M | 120 000 km / 6 ans |
| K9K dCi | 90-120 000 km selon version |
| F9Q | 120 000 km |
| M9R | 120 000 km / 6 ans |

### VAG (VW/Audi/Seat/Skoda)
| Moteur | Intervalle |
|--------|------------|
| 1.6 TDI CAYC | 120 000 km / 5 ans |
| 2.0 TDI CR | 120 000 km / 5 ans |
| TSI | Chaine (pas d'entretien) |

## Signes de remplacement urgent

### Visuels
- Craquelures sur courroie
- Usure laterale (desalignement)
- Traces de poudre noire

### Sonores
- Couinement au demarrage
- Claquement periodique
- Bruit de galet

### Preventif
- Kilometrage atteint
- Age depasse (meme faible km)
- Apres fuite pompe a eau/joint SPI

## Conseils pratiques

1. **Ne jamais depasser l'intervalle** : Casse = moteur HS
2. **Kit complet** : Economise la main d'oeuvre future
3. **Pompe a eau** : Inclure systematiquement
4. **Courroie accessoires** : Profiter de l'intervention
5. **Liquide refroidissement** : Vidanger lors du remplacement
6. **Carnet entretien** : Tamponner avec date et km
## Symptomes courants

### Bruit de claquement moteur
- **Quand** : Au ralenti ou a l'acceleration
- **Caracteristique** : Claquement rythmique, lie au regime moteur

### Sifflement au demarrage
- **Quand** : A froid, disparait a chaud
- **Caracteristique** : Son aigu type courroie patinante

### Perte de puissance
- **Quand** : En acceleration
- **Caracteristique** : Moteur qui "tire" moins

### Temoin moteur allume
- **Quand** : Aleatoire
- **Caracteristique** : Voyant orange fixe

## Causes possibles et solutions

### 1. Courroie de distribution usee
- **Probabilite** : 40%
- **Verification** : Age/kilometrage, aspect visuel (fissures, effilochage)
- **Solution** : Remplacement kit distribution complet
- **Pieces** : Kit distribution (courroie, galets, pompe a eau)
- **Urgence** : CRITIQUE - Risque casse moteur

### 2. Galet tendeur defaillant
- **Probabilite** : 25%
- **Verification** : Jeu excessif, bruit de roulement
- **Solution** : Remplacement galet(s)
- **Pieces** : Galet tendeur, galet enrouleur
- **Urgence** : Haute

### 3. Pompe a eau HS
- **Probabilite** : 20%
- **Verification** : Fuite liquide de refroidissement, jeu axial
- **Solution** : Remplacement pompe a eau
- **Pieces** : Pompe a eau
- **Urgence** : Haute

### 4. Courroie accessoires usee
- **Probabilite** : 15%
- **Verification** : Fissures, patinage
- **Solution** : Remplacement courroie accessoires
- **Pieces** : Courroie poly-V, galet tendeur accessoires
- **Urgence** : Moyenne

## Intervalles de remplacement

| Type moteur | Intervalle | Kilometrage |
|-------------|------------|-------------|
| Essence | 5 ans | 100 000 km |
| Diesel | 5 ans | 120 000 km |
| HDI/TDI | 4 ans | 160 000 km |

## Recommandations

- **Remplacement preventif** : Respecter les preconisations constructeur
- **Kit complet** : Toujours remplacer courroie + galets + pompe a eau ensemble
- **Marques** : Privilegier Gates, Continental, SKF
- **Huile** : Verifier absence de fuites d'huile sur la courroie


## References supplementaires

<!-- materialized-from-db vehicles/renault-megane-3.md 2026-01-08 -->
### Fiche vehicule - Renault Megane 3

# Renault Megane 3 (2008-2016)

## Identification

- **Generation** : III
- **Production** : 2008 - 2016
- **Segment** : C (compacte)
- **Carrosseries** : 3 portes, 5 portes, Estate (break), Coupe, CC (cabriolet), RS

## Motorisations principales

### Essence
| Moteur | Puissance | Code moteur |
|--------|-----------|-------------|
| 1.6 16v | 110 ch | K4M |
| 1.4 TCe | 130 ch | H4J |
| 2.0 TCe | 180 ch | F4R |
| 2.0 RS | 250/265 ch | F4R |

### Diesel
| Moteur | Puissance | Code moteur |
|--------|-----------|-------------|
| 1.5 dCi | 90/110 ch | K9K |
| 1.6 dCi | 130 ch | R9M |
| 1.9 dCi | 130 ch | F9Q |
| 2.0 dCi | 150/160 ch | M9R |

## Pieces d'usure courantes

### Freinage
- **Plaquettes avant** : 30-40 000 km
- **Disques avant** : 60-80 000 km
- **Freins arriere** : Disques ou tambours selon version

### Filtration
- **Filtre a huile** : A chaque vidange
- **Filtre a air** : 30 000 km
- **Filtre habitacle** : 15 000 km
- **Filtre a gasoil** (dCi) : 60 000 km

### Distribution
- **1.5 dCi (K9K)** : Courroie, 90 000 km ou 6 ans
- **1.6 dCi (R9M)** : Chaine (sans entretien)
- **2.0 dCi (M9R)** : Courroie, 120 000 km ou 6 ans
- **1.6 16v (K4M)** : Courroie, 120 000 km ou 6 ans
- **TCe** : Chaine (sans entretien)

## Problemes connus

### Moteur 1.5 dCi (K9K)
- Injecteurs : Defaillance frequente (claquement, fumee)
- Vanne EGR : Encrassement rapide
- Turbo : Controle huile regulier, geometrie variable

### Moteur 1.6 dCi (R9M)
- Injecteurs piezo : Couteux a remplacer
- Courroie accessoires : Galet tendeur a surveiller

### Moteur 2.0 dCi (M9R)
- Volant moteur bimasse : Bruit au ralenti
- Pompe HP : Copeaux metalliques possibles

### Electricite
- Carte main libre : Problemes de detection
- Tableau de bord : Pixels defaillants
- Feux arriere LED : Bandeaux LED HS

### Chassis
- Roulements avant : Usure normale 80-100k km
- Silent-blocs berceau : Claquements
- Cardans : Soufflets a surveiller

## Intervalles d'entretien

### Vidange
- **Essence** : 20 000 km ou 1 an
- **Diesel** : 20 000 km ou 1 an

### Liquide de frein
- Tous les 2 ans ou 60 000 km

## References OEM courantes

| Piece | Reference Renault |
|-------|-------------------|
| Filtre a huile 1.5 dCi | 8200768913 |
| Filtre a air 1.5 dCi | 8200431051 |
| Plaquettes avant | 410607115R |
| Disques avant | 402069518R |
| Kit distribution 1.5 dCi | 130C17529R |

## Conseils d'entretien

1. **Huile moteur** : 5W-30 C3 ou C4 selon version
2. **Liquide refroidissement** : Type D (jaune/vert)
3. **Direction assistee** : Electrique (pas de fluide)
4. **Boite EDC** : Vidange huile 60 000 km

## Specificites par version

### Megane RS (250/265 ch)
- Freinage Brembo 4 pistons
- Chassis Cup disponible (sport)
- Differentiel autobloquant (option Trophy)
- Entretien plus frequent recommande

### Megane CC
- Toit rigide retractable : Verifier joints et verins
- Hydraulique toit : Controle niveau

<!-- materialized-from-db vehicles/volkswagen-golf-6.md 2026-01-08 -->
### Fiche vehicule - Volkswagen Golf 6

# Volkswagen Golf 6 (2008-2012)

## Identification

- **Generation** : VI (5K)
- **Production** : 2008 - 2012
- **Segment** : C (compacte)
- **Carrosseries** : 3 portes, 5 portes, Variant (break), Cabriolet
- **Versions sport** : GTI, GTD, R

## Motorisations principales

### Essence
| Moteur | Puissance | Code moteur |
|--------|-----------|-------------|
| 1.4 TSI | 122 ch | CAXA |
| 1.4 TSI | 160 ch | CAVD |
| 1.8 TSI | 160 ch | CDAA |
| 2.0 TSI GTI | 210 ch | CCZB |
| 2.0 TSI R | 270 ch | CDLF |

### Diesel
| Moteur | Puissance | Code moteur |
|--------|-----------|-------------|
| 1.6 TDI | 90/105 ch | CAYC |
| 2.0 TDI | 110 ch | CBDB |
| 2.0 TDI | 140 ch | CBAB |
| 2.0 TDI GTD | 170 ch | CFGB |

## Pieces d'usure courantes

### Freinage
- **Plaquettes avant** : 30-50 000 km
- **Disques avant** : 60-80 000 km
- **Freins arriere** : Disques sur toutes versions

### Filtration
- **Filtre a huile** : A chaque vidange
- **Filtre a air** : 40 000 km
- **Filtre habitacle** : 20 000 km
- **Filtre a gasoil** (TDI) : 60 000 km

### Distribution
- **1.4 TSI** : Chaine (attention etirement)
- **1.6 TDI** : Courroie, 120 000 km ou 5 ans
- **2.0 TDI** : Courroie, 120 000 km ou 5 ans
- **2.0 TSI** : Chaine (sans entretien normal)

## Problemes connus

### Moteur 1.4 TSI (CAXA/CAVD)
- Chaine distribution : Etirement premature (symptome: bruit au demarrage froid)
- Tendeur chaine : Defaillant, a remplacer preventivement
- Solution : Kit chaine complet (tendeur + guides + chaine)

### Moteur 2.0 TDI (CR)
- Injecteurs piezo : Defaillance possible apres 150k km
- Vanne EGR : Encrassement, nettoyage ou suppression
- FAP : Regenerations frequentes en ville

### Boite DSG
- Mecatronique : Defaillances possibles (a-coups, passage neutre)
- Embrayages : Usure si conduite urbaine
- Vidange huile : Tous les 60 000 km obligatoire

### Electricite
- Module confort : Problemes vitres, centralisation
- Pompe a eau electrique (TSI) : Defaillante apres 100k km

## Intervalles d'entretien

### Vidange (selon service VAG)
- **Service flexible** : 15-30 000 km selon usage
- **Recommande** : 15 000 km ou 1 an

### Liquide de frein
- Tous les 2 ans

## References OEM courantes

| Piece | Reference VAG |
|-------|---------------|
| Filtre a huile 2.0 TDI | 03L115562 |
| Filtre a air 2.0 TDI | 1K0129620D |
| Plaquettes avant | 5K0698151 |
| Disques avant | 5K0615301 |
| Kit distribution 2.0 TDI | Gates/Contitech |

## Conseils d'entretien

1. **Huile moteur** : 5W-30 504.00/507.00 (Long Life)
2. **Alternative recommandee** : 5W-40 non Long Life + vidanges 15k km
3. **Liquide refroidissement** : G12++ (rose/violet)
4. **Boite DSG** : Vidange stricte 60 000 km

## Specificites par version

### Golf GTI
- Freinage plus gros (312mm)
- Differentiel XDS (freinage selectif)
- Mode sport selectable
- Huile 5W-40 recommandee

### Golf R
- Transmission 4Motion
- Freinage 345mm avant
- Entretien renforce recommande

### Golf GTD
- Performances diesel
- FAP et AdBlue selon annee
- Huile specifique FAP

<!-- materialized-from-db vehicles/citroen-c3.md 2026-01-08 -->
### Fiche vehicule - Citroen C3

# Citroen C3 (2002-2024)

## Identification

### C3 I (2002-2009)
- **Code** : FC
- **Segment** : B (citadine)
- **Carrosseries** : 5 portes, Pluriel (decouvrable)

### C3 II (2009-2016)
- **Code** : A51
- **Segment** : B
- **Carrosseries** : 5 portes

### C3 III (2016-2024)
- **Code** : SX
- **Segment** : B
- **Carrosseries** : 5 portes
- **Design** : Airbumps, bi-ton

## Motorisations principales

### Essence
| Moteur | Puissance | Code moteur | Generation |
|--------|-----------|-------------|------------|
| 1.1i | 60 ch | HFZ (TU1JP) | C3 I |
| 1.4i | 75 ch | KFV (TU3JP) | C3 I/II |
| 1.6 VTi | 120 ch | EP6 | C3 II |
| 1.2 PureTech | 82 ch | EB2 | C3 II/III |
| 1.2 PureTech | 110 ch | EB2DT turbo | C3 III |

### Diesel
| Moteur | Puissance | Code moteur | Generation |
|--------|-----------|-------------|------------|
| 1.4 HDi | 68 ch | 8HZ (DV4TD) | C3 I/II |
| 1.6 HDi | 90/92 ch | 9HX (DV6) | C3 I/II |
| 1.5 BlueHDi | 100 ch | DV5 | C3 III |

## Pieces d'usure courantes

### Freinage
- **Plaquettes avant** : 30-40 000 km
- **Disques avant** : 60-80 000 km
- **Arriere** : Tambours (I/II), disques (certaines III)

### Filtration
- **Filtre a huile** : A chaque vidange
- **Filtre a air** : 30 000 km
- **Filtre habitacle** : 15 000 km
- **Filtre a gasoil** : 60 000 km

### Distribution
- **Moteurs TU (1.1/1.4)** : Courroie, 80 000 km ou 5 ans
- **1.4/1.6 HDi** : Courroie, 100 000 km ou 10 ans
- **PureTech EB2** : Courroie, 100 000 km ou 10 ans
- **1.6 VTi (EP6)** : Chaine

## Problemes connus

### Moteur PureTech EB2 (1.2 turbo)
- **Courroie** : Etirement premature, controle frequent
- **Poulie damper** : Eclatement possible
- **Consommation huile** : A surveiller

### Moteur EP6 (1.6 VTi/THP)
- **Chaine distribution** : Etirement (bruit demarrage)
- **Capteur arbre a cames** : Defaillant
- **Bobines allumage** : A remplacer par kit renforce

### Moteur 1.4/1.6 HDi (DV4/DV6)
- **Vanne EGR** : Encrassement frequent
- **Injecteurs** : Fuite retour, demarrage difficile
- **Poulie damper** : Controle visuel regulier

### Electricite
- **BSI** : Dysfonctionnements (essuie-glaces, centralisation)
- **Combine** : Affichage defaillant
- **Antidemarrage** : Problemes cle/transpondeur

### Chassis
- **Roulements avant** : Remplacement frequent
- **Silent-blocs** : Claquements suspension
- **Cardans** : Soufflets fragiles

## Intervalles d'entretien

### Vidange
- **Essence** : 15 000 km ou 1 an
- **Diesel** : 20 000 km ou 1 an

### Liquide de frein
- Tous les 2 ans

## References OEM courantes

| Piece | Reference PSA |
|-------|---------------|
| Filtre a huile 1.4 HDi | 1109AY |
| Filtre a air 1.4 HDi | 1444VJ |
| Plaquettes avant | 4254.22 |
| Disques avant 266mm | 4249.34 |
| Kit distribution PureTech | 1611841580 |

## Conseils d'entretien

1. **Huile moteur essence** : 5W-30 ou 0W-30
2. **Huile moteur diesel** : 5W-30 C2 (FAP)
3. **Liquide refroidissement** : Revkogel 2000
4. **Direction** : Electrique (pas de fluide)

## Specificites par version

### C3 Pluriel (2003-2010)
- Toit amovible modulable
- Arceaux retractables : Maintenance specifique
- Joints toit : Controle annuel

### C3 Aircross (2017+)
- SUV urbain derive C3
- Garde au sol rehaussee
- Memes motorisations PureTech/BlueHDi

<!-- materialized-from-db vehicles/peugeot-206.md 2026-01-01 -->
### Fiche véhicule - Peugeot 206

# Peugeot 206 (1998-2012)

## Identification

- **Génération** : Unique (T1/T3)
- **Production** : 1998 - 2012
- **Segment** : B (citadine)
- **Carrosseries** : 3 portes, 5 portes, CC (cabriolet), SW (break), RC/GTI

## Motorisations principales

### Essence
| Moteur | Puissance | Code moteur |
|--------|-----------|-------------|
| 1.1i | 60 ch | HFX (TU1JP) |
| 1.4i | 75 ch | KFW (TU3JP) |
| 1.6i | 88/110 ch | NFU (TU5JP4) |
| 2.0 GTI | 137 ch | RFK (EW10J4) |
| 2.0 RC | 177 ch | RFK (EW10J4S) |

### Diesel
| Moteur | Puissance | Code moteur |
|--------|-----------|-------------|
| 1.4 HDi | 68 ch | 8HX (DV4TD) |
| 1.6 HDi | 90/110 ch | 9HY/9HZ (DV6) |
| 2.0 HDi | 90 ch | RHY (DW10TD) |

## Pièces d'usure courantes

### Freinage
- **Plaquettes avant** : 30-40 000 km
- **Disques avant** : 60-80 000 km
- **Tambours arrière** : Standard sur la plupart des versions
- **Kit frein arrière** : Mâchoires + cylindres

### Filtration
- **Filtre à huile** : À chaque vidange
- **Filtre à air** : 30 000 km
- **Filtre habitacle** : 15 000 km
- **Filtre à gasoil** (HDi) : 60 000 km

### Distribution
- **Essence TU** : Courroie, 80 000 km ou 5 ans
- **HDi DV4/DV6** : Courroie, 100 000 km ou 10 ans
- **HDi DW10** : Courroie, 120 000 km

## Problèmes connus

### Moteur 1.4 HDi (DV4)
- Injecteurs : Encrassement, démarrage difficile
- Vanne EGR : Colmatage fréquent
- Poulie damper : Éclatement (bruit moteur)

### Moteur 1.6 HDi (DV6)
- Volant moteur bimasse : Usure prématurée (bruit au ralenti)
- Turbo : Contrôle régulier huile

### Électricité
- BSI (Boîtier de Servitude Intelligent) : Dysfonctionnements
- Antidémarrage : Problèmes transpondeur clé

### Train roulant
- Cardans : Soufflets à surveiller
- Roulements avant : Usure normale
- Triangles de suspension : Silent-blocs

## Intervalles d'entretien

### Vidange
- **Essence** : 15 000 km ou 1 an
- **Diesel** : 20 000 km ou 1 an

### Liquide de frein
- Tous les 2 ans

## Références OEM courantes

| Pièce | Référence Peugeot |
|-------|-------------------|
| Filtre à huile 1.4 HDi | 1109AY |
| Filtre à air 1.4 HDi | 1444VJ |
| Plaquettes avant | 4254.22 |
| Disques avant | 4249.G5 |
| Kit distribution 1.4 HDi | 0831V4 |

## Conseils d'entretien

1. **Huile moteur diesel** : 5W-30 spéciale FAP si équipé
2. **Essence** : 10W-40 ou 5W-40 selon préconisation
3. **Liquide refroidissement** : Type Revkogel 2000 (vert)
4. **LHM** : Si direction assistée hydraulique (citadines anciennes)

## Spécificités par version

### 206 RC
- Freinage renforcé (disques ventilés 4 pistons)
- Distribution renforcée
- Entretien plus fréquent recommandé

### 206 CC
- Vérins de capote : Contrôle annuel
- Joints de capote : Entretien spécifique

<!-- materialized-from-db manual/cc6a270d3e4e 2026-04-02 -->
### Données techniques OEM — Montage maitrise

# Données techniques OEM — Montage maitrise
Source : bremboparts.com + denso-am.eu + textar.com (13 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- hall
- électrique

## Valeurs techniques de référence
- 10 Nm
- 115 Nm
- 125 Nm
- 16 Nm
- 18 mm
- 180 Nm
- 20 Nm
- 20 mm
- 210 Nm
- 22 Nm

<!-- materialized-from-db vehicles/renault-clio-3 2026-03-16 -->
### Fiche véhicule - Renault Clio 3

# Renault Clio 3 (2005-2014)

## Identification

- **Génération** : III (BR/CR)
- **Production** : 2005 - 2014
- **Segment** : B (citadine)
- **Carrosseries** : 3 portes, 5 portes, Estate (break)

## Motorisations principales

### Essence
| Moteur | Puissance | Code moteur |
|--------|-----------|-------------|
| 1.2 16V | 75 ch | D4F |
| 1.2 TCE | 100 ch | D4F |
| 1.4 16V | 98 ch | K4J |
| 1.6 16V | 110 ch | K4M |
| 2.0 RS | 197/200 ch | F4R |

### Diesel
| Moteur | Puissance | Code moteur |
|--------|-----------|-------------|
| 1.5 dCi | 65/68 ch | K9K |
| 1.5 dCi | 85/86 ch | K9K |
| 1.5 dCi | 105/106 ch | K9K |

## Pièces d'usure courantes

### Freinage
- **Plaquettes avant** : Remplacement 30-40 000 km
- **Disques avant** : Remplacement 60-80 000 km
- **Plaquettes arrière** : 50-70 000 km (si disques)
- **Tambours** : Contrôle à 100 000 km

### Filtration
- **Filtre à huile** : À chaque vidange
- **Filtre à air** : 30 000 km ou 2 ans
- **Filtre habitacle** : 15 000 km ou 1 an
- **Filtre à carburant** (diesel) : 60 000 km

### Distribution
- **Type** : Courroie
- **Intervalle** : 90 000 km ou 5 ans (selon motorisation)
- **Kit complet** : Courroie + galets + pompe à eau recommandé

## Problèmes connus

### Moteur 1.5 dCi (K9K)
- Vanne EGR : Encrassement fréquent
- Injecteurs : Fuite de carburant (rappel)
- Turbo : Usure prématurée (huile de qualité importante)

### Électricité
- Platine fusibles : Problèmes de contacts
- Capteur pédale accélérateur : Défaillance

### Train roulant
- Rotules de direction : Usure normale
- Silent-blocs bras : À contrôler à 100 000 km

## Rappels constructeur

| Rappel | Motorisation | Période | Détail |
|--------|-------------|---------|--------|
| Injecteurs Delphi — fuite carburant | 1.5 dCi (K9K) | 2005-2010 | Fuite au raccord haute pression des injecteurs. Risque incendie. Remplacement gratuit des joints et clips de fixation. Concerne ~500 000 véhicules en Europe. |
| Platine fusibles — court-circuit | Toutes motorisations | 2006-2009 (certaines séries) | Défaut de soudure sur la platine fusibles habitacle pouvant provoquer un dysfonctionnement électrique. Remplacement platine en concession. |
| Pédale accélérateur — signal erratique | 1.5 dCi | 2007-2009 | Capteur de position pédale accélérateur défaillant pouvant causer des à-coups ou une perte de puissance. Remplacement du capteur. |

> **Vérification** : le numéro de rappel est consultable sur rappel.renault.fr avec le VIN du véhicule.

## Intervalles d'entretien

### Vidange
- **Essence** : 15 000 km ou 1 an
- **Diesel** : 20 000 km ou 1 an

### Contrôle général
- Tous les 20 000 km ou 1 an

## Références OEM courantes

| Pièce | Référence Renault |
|-------|-------------------|
| Filtre à huile 1.5 dCi | 8200768927 |
| Filtre à air 1.5 dCi | 8200431051 |
| Plaquettes avant | 410602192R |
| Dis

[...]
