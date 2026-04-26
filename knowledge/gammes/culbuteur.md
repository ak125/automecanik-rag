---
category: moteur
slug: culbuteur
title: Culbuteur
pg_id: 432
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
  role: Transmettre le mouvement de l'arbre a cames aux soupapes
  must_be_true:
  - transmettre
  - basculer
  - actionner
  must_not_contain:
  - boite de vitesses
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - transmettre
  - basculer
  - actionner
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
  - ❌ "repare le moteur"
  cost_range:
    min: 1000
    max: 5000
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Equipement d origine (OE)
  - tier: Equivalent OE
  - tier: Piece adaptable
  brands:
    premium:
    - Elring
    - Victor Reinz
    standard:
    - Febi
    - Ajusa
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Claquement moteur regulier
    severity: confort
  - id: S2
    label: Bruit de tic-tic au ralenti
    severity: confort
  - id: S3
    label: Perte de puissance sur un cylindre
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : claquement moteur regulier'
  quick_checks:
  - 'Observer : claquement moteur regulier ?'
  - Bruit de tic-tic au ralenti ?
  - 'Observer : perte de puissance sur un cylindre ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Claquement moteur regulier
  - Bruit de tic-tic au ralenti
  - Perte de puissance sur un cylindre
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '432'
  intro_title: A quoi sert Culbuteur ?
  risk_title: Pourquoi remplacer Culbuteur a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: Comment choisir Culbuteur compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Culbuteur ?
    answer: En cas de claquement moteur regulier ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Culbuteur sans verification atelier ?
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
doc_id: 8787a4aa-4c8e-578f-b611-4bd73b31d412
content_hash: sha256:b35ca1a7a4ec9ec6
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
  _source: fr.wikipedia.org + gpa26.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 2
  _has_tech_data: true
  types_variants:
  - type: 'hydraulique'
    source_ref: corpus RAG web OEM
  - type: 'plein'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_18_a: '18 a'
    val_28_a: '28 a'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le culbuteur équipe lesmoteurs à arbre à cames en tête. Il va transmettre lemouvement de l''arbre à cames aux soupapes
    pour le cycle de combustion dumoteur. Il assurel''ouverture et la fermeture d''une soupape d''admission ou d''une soupape
    d''échappement, enfonction de la rotation de l''arbre à cames. La transmission se fait par pivotement autour d''un axe.
    En générale le culbuteur estarticulé sur une rotule hydraulique à l''une de ses extrémités et l''actionnementest assuré
    par la came via un rouleau ou une platine de friction. L''autreextrémité va appuyer sur la queue de soupape pour son ouverture
    et pour la fermeturec''est le ressort de rappel de la soupape qui va la fermée après qu''elle estlibérée de la pression
    du culbuteur. Sur les anciennes motorisations l''extrémité du culbuteur porte un système de vis etcontre écrou pour le
    réglage du jeu entre culbuteur et soupape (le réglage sefait à l''aide d''une cale d''épaisseur calibrée)... opération
    à réitérer àintervalles réguliers. En savoir plus : culbuteur — définition et rôle mécanique 🚨 Bruit Culbuteur : causes
    et diagnostic'
  S2: 'Un culbuteur défaillant présente plusieurs symptômes : - Surconsommation du carburant. - Fumée d''échappement. - Bruit
    de claquement lors du fonctionnement du moteur. - Manque de puissance du moteur. Un culbuteur usé peut causer de différent
    problème dans le moteur : - Usure de la soupape d''admission. - Usure de la soupape d''échappement. - Usure de l''arbre
    à cames. - Usure des injecteurs. - Usure du catalyseur. - Usure du FAP. Diagnostic complet : identifier une panne de culbuteur'
  S3: '- Référence moteur et code motorisation — Le culbuteur est dimensionné au millimètre près pour chaque architecture
    de culasse. Un culbuteur de 1.6 HDi ne s''adapte pas sur un 2.0 HDi même si les deux moteurs partagent la même plateforme.
    Identifier le code moteur (gravé sur le bloc ou visible sur la carte grise au champ P5) avant toute commande. - Type de
    distribution : arbre à cames en tête ou latéral — Sur les moteurs à arbre à cames en tête (DOHC), le culbuteur présente
    un profil différent de celui des moteurs à arbre latéral (OHV) où la tige de culbuteur est plus longue. Vérifier l''architecture
    de distribution de votre motorisation pour sélectionner le bon type de bascule. - Présence ou absence de poussoir hydraulique
    intégré — Certains culbuteurs intègrent un poussoir hydraulique auto-réglable, éliminant le besoin de réglage du jeu aux
    soupapes. D''autres nécessitent un réglage manuel à la vis et contre-écrou. Ces deux versions ne sont pas interchangeables
    : se fier à la configuration d''origine. - Matériau et traitement de surface de la portée — La portée de came subit une
    usure par abrasion et contact roulant. Les culbuteurs de qualité OEM présentent une portée traitée par nitruration ou
    rechargée à l''alliage dur. Un culbuteur avec portée non traitée s''use prématurément et entraîne l''usure de la came
    en regard. - Remplacement par jeu complet sur un même cylindre — Lorsqu''un culbuteur d''admission est usé sur un cylindre,
    le culbuteur d''échappement du même cylindre présente généralement la même usure. Remplacer les deux simultanément évite
    une seconde intervention rapprochée et garantit un comportement symétrique de la soupape. - Vérification de l''arbre à
    cames associé — Un culbuteur usé interagit avec la came correspondante : la portée de came montre souvent des traces d''usure
    en miroir. Commander un culbuteur neuf sans inspecter l''arbre à cames peut conduire à une dégradation accélérée de la
    pièce neuve dans les premières heures de fonctionnement. - Équipementier de rang 1 ou pièce constructeur — Privilégier
    les fabricants référencés OEM (INA, Febi, Victor Reinz pour les composants moteur) pour garantir la conformité dimensionnelle
    et métallurgique. Une pièce hors filière peut présenter des tolérances insuffisantes et générer des bruits persistants
    même après montage. Pour aller plus loin : consultez notre guide d''achat culbuteur — comparatif marques, critères de
    choix et prix.'
  S4_DEPOSE: '- Déposer le cache-culbuteurs (couvre-culasse) — Débrancher d''abord les connecteurs électriques fixés sur le
    cache (bobines d''allumage, tuyaux de dépression). Dévisser les vis de fixation dans l''ordre inverse de serrage (spirale
    de l''extérieur vers le centre pour éviter toute déformation du joint). Soulever le cache délicatement pour ne pas endommager
    le joint d''étanchéité. - Identifier le cylindre et le culbuteur à remplacer — Repérer visuellement le culbuteur défaillant
    : traces d''usure brillante sur la portée, jeu axial excessif, ou déformation visible. Photographier la disposition avant
    démontage pour faciliter la remise en place. - Amener le cylindre concerné au Point Mort Haut (PMH) compression — Tourner
    le vilebrequin (clé sur la vis centrale ou par le boulon de poulie) jusqu''à aligner les repères de distribution. Au PMH
    compression, les deux soupapes du cylindre sont fermées et le culbuteur n''est soumis à aucune contrainte de came, ce
    qui permet un démontage sans risque. - Déposer l''axe de culbuteur ou le pivot de fixation — Selon la conception (axe
    commun ou pivot individuel), dévisser les vis de fixation de l''axe dans l''ordre préconisé par le constructeur. Sur les
    moteurs à axe commun, noter la position de chaque culbuteur et entretoise : ils ne sont pas interchangeables entre cylindres.
    - Extraire le culbuteur défaillant — Glisser le culbuteur hors de son axe ou déposer le pivot. Conserver toutes les pièces
    dans l''ordre pour le remontage. Ne pas mélanger les culbuteurs de cylindres différents. - Inspecter la portée de came
    et le poussoir hydraulique — Examiner la trace de contact sur l''arbre à cames : si elle est creusée ou présente des rayures,
    l''arbre à cames doit être mesuré au micromètre et potentiellement remplacé. Vérifier le poussoir hydraulique associé
    s''il est présent. - Nettoyer l''axe et le logement avant remontage — Éliminer les résidus d''huile ancienne et de métal
    avec un chiffon non pelucheux. Appliquer une fine couche d''huile moteur neuve sur l''axe et les portées de glissement
    avant d''introduire le nouveau culbuteur. - Monter le culbuteur neuf et régler le jeu aux soupapes si nécessaire — Insérer
    le culbuteur neuf, revisser les vis d''axe au couple constructeur. Si le modèle ne dispose pas de poussoirs hydrauliques,
    régler le jeu aux soupapes à la jauge d''épaisseur selon la valeur constructeur (typiquement 0,10 à 0,30 mm à froid selon
    moteur). - Reposer le cache-culbuteurs avec un joint neuf — Ne jamais réutiliser le joint de cache-culbuteurs écrasé.
    Serrer les vis dans l''ordre préconisé (centre vers extérieur) au couple constructeur (généralement 8 à 12 N.m) pour éviter
    toute déformation du plan de joint. - Démarrer et écouter — Démarrer le moteur et écouter les premières secondes : un
    bruit de tic-tic résiduel pendant 30 secondes est normal le temps que les poussoirs hydrauliques se remplissent d''huile.
    La persistance au-delà indique un problème de jeu résiduel ou un poussoir défaillant.'
  S4_REPOSE: 'Il existe deux types de culbuteur suivant le type de réglage de chaque motorisation : - Sur les anciens moteurs
    : le culbuteur est doté d''un système vis-écrou pour la compensation du jeu. Le réglage du jeu se fait à l''aide d''un
    jeu de cales (moteur froid et l''arbre à cames n''appuie pas sur le culbuteur) . Attention : Il faut obligatoirement consulter
    la revue technique de votre véhicule pour la valeur de jeu nominal ainsi que pour la procédure de réglage. - Sur les nouvelle
    motorisation : les culbuteurs sont équipés d''un système de rattrapage hydraulique qu''est sans maintenance dans ce cas
    vous n''aurez plus besoin de réglage de jeu. Le systèmes hydraulique est constitué d''un poussoir positionné au point
    de pivotement du culbuteur et qui fonctionne avec la pression d''huile. ✅ Après remontage, vérifiez les spécifications
    dans la fiche technique Culbuteur.'
  S5: '- Ne pas atteindre le PMH compression avant démontage — Démonter un culbuteur alors que la came exerce une contrainte
    sur lui force l''extraction et peut entraîner la déformation de l''axe ou l''arrachage du pivot. Systématiquement vérifier
    la position de vilebrequin au PMH du cylindre concerné avant tout démontage. - Mélanger les culbuteurs entre cylindres
    — Les culbuteurs s''adaptent à leur portée de came respective après rodage. Intervertir deux culbuteurs entre cylindres
    réintroduit un rodage croisé : usure accélérée des deux paires came-culbuteur et retour du claquement dans les jours suivants.
    - Omettre l''inspection de l''arbre à cames — Un culbuteur usé est souvent la conséquence d''une came abîmée, et non sa
    cause. Monter un culbuteur neuf sur une came rayée ou creusée le dégrade à nouveau en quelques milliers de kilomètres.
    L''inspection de la came est une étape non négociable avant remontage. - Ne pas remplacer le joint de cache-culbuteurs
    — Un joint de cache-culbuteurs comprimé, réutilisé, provoque une fuite d''huile par le plan de joint. La fuite s''aggrave
    avec la chaleur et contamine le circuit d''allumage (bobines, bougies), générant des ratés d''allumage sans rapport apparent
    avec l''intervention initiale. - Oublier de régler le jeu aux soupapes sur un moteur à réglage manuel — Sur les moteurs
    à culbuteurs sans poussoir hydraulique, négliger le réglage du jeu aux soupapes maintient le bruit de tic-tic malgré le
    remplacement. Le jeu hors tolérance (trop grand : claquement ; trop petit : soupape ne se ferme plus complètement) peut
    conduire à une usure prématurée des soupapes ou à un défaut de compression.'
  S6: '- Écoute au démarrage pendant les 60 premières secondes — Un bruit de tic- tic résiduel à froid pendant 20 à 30 secondes
    est normal : les poussoirs hydrauliques se purgent et se remplissent d''huile. Si le claquement persiste au-delà de 60
    secondes moteur chaud, le jeu aux soupapes doit être vérifié ou le poussoir hydraulique neuf testé. - Contrôle du jeu
    aux soupapes (moteurs à réglage manuel) — Après 500 km de rodage, revérifier le jeu à la jauge d''épaisseur moteur froid.
    La valeur doit correspondre à la tolérance constructeur (admission et échappement ont souvent des valeurs différentes).
    Un jeu hors tolérance après rodage indique un problème de portée ou de pivot. - Vérification de l''absence de fuite d''huile
    au niveau du cache- culbuteurs — Après 15 minutes de fonctionnement moteur, inspecter visuellement le pourtour du cache-culbuteurs.
    Toute trace suintante signale un joint mal posé ou une vis insuffisamment serrée. - Test de compression sur le cylindre
    concerné — Un culbuteur mal monté ou une came endommagée non détectée lors du démontage se traduit par une baisse de compression
    sur le cylindre traité. Un test de compression au compressiomètre (valeur typique : 10 à 14 bars selon motorisation) permet
    de confirmer l''intégrité de la chaîne soupape-culbuteur-came. - Absence de code défaut allumage ou calage — Connecter
    un outil OBD et vérifier l''absence de codes P030X (raté d''allumage cylindre X) ou de codes liés au calage variable (VVT).
    La disparition du claquement moteur et de la perte de puissance valide la réussite de l''intervention.'
  S7: 'Le culbuteur est la pièce intermédiaire entre l''arbre à cames et les soupapes : il bascule sous la poussée du lobe
    de came pour ouvrir la soupape, puis revient en position par le ressort de soupape. Son usure entraîne systématiquement
    la dégradation des pièces en contact direct, qui doivent être contrôlées lors de l''intervention. - Arbre à cames — le
    lobe de came appuie directement sur la pastille ou la surface du culbuteur. Un arbre à cames usé présente des lobes aplatis
    qui réduisent la levée de soupape et causent exactement les mêmes symptômes (claquement, perte de puissance sur un cylindre)
    qu''un culbuteur défectueux. Inspecter les lobes lors de l''accès à la culasse. - Poussoirs de soupape — sur les motorisations
    à poussoirs hydrauliques, ces éléments assurent la compensation automatique du jeu aux soupapes. Un poussoir grippé ou
    vidé de son huile claque au ralenti. Remplacer l''ensemble culbuteur + poussoir sur le cylindre concerné. - Soupapes d''admission
    et d''échappement — une soupape brûlée ou à tige tordue génère un jeu anormal et provoque un claquement identique à celui
    d''un culbuteur usé. La vérification de la rectitude des tiges est obligatoire lors de l''ouverture du cache-culasse.
    - Joint de cache-culbuteurs — la dépose du cache-culasse pour accéder aux culbuteurs requiert le remplacement systématique
    du joint de couvre-culasse. Un joint reposé en l''état compresse de manière inégale et provoque des fuites d''huile rapides.
    - Huile moteur et filtre à huile — le culbuteur est lubrifié par la pression d''huile moteur. Une huile ancienne ou un
    filtre colmaté réduisent cette pression et accélèrent l''usure des culbuteurs. Changer simultanément l''huile et le filtre
    lors de toute intervention sur la distribution haute.'
  S8: 'Comment distinguer un bruit de culbuteur d''un bruit de poussoir hydraulique ? Les deux génèrent un "tic-tic" rythmé
    par le régime moteur, mais leur comportement diffère. Un poussoir hydraulique défaillant produit un bruit souvent présent
    à froid uniquement, qui disparaît après quelques minutes de chauffe (l''huile se redistribue dans le poussoir). Un culbuteur
    usé ou mal réglé produit un claquement présent à froid et à chaud, invariable en température. Pour affiner le diagnostic,
    placer un stéthoscope mécanique (ou un tournevis tenu contre la culasse) sur chaque couvre-culasse pour localiser le cylindre
    concerné avant démontage. Peut-on remplacer un seul culbuteur ou faut-il changer le jeu complet ? Techniquement, remplacer
    un seul culbuteur est possible et acceptable si les autres ne présentent aucun signe d''usure (portée intacte, jeu correct).
    Cependant, si le moteur dépasse 150 000 km ou si plusieurs culbuteurs montrent une usure similaire, le remplacement du
    jeu complet sur la culasse est économiquement pertinent : le coût de la main-d''oeuvre (ouverture du cache-culbuteurs)
    représente l''essentiel du coût de la réparation. Les culbuteurs peuvent-ils être réparés ou rectifiés ? Non dans le cadre
    d''un atelier standard. La portée de came d''un culbuteur usé présente une déformation de quelques dixièmes de millimètre
    qui modifie le profil de contact et la géométrie de levée de soupape. La rectification nécessite une rectifieuse de précision
    et un contrôle dimensionnel post-usinage que seuls les ateliers de mécanique fine peuvent réaliser. Dans la pratique,
    le coût d''un culbuteur neuf d''origine ou équipementier est inférieur à celui d''une rectification, sauf sur des moteurs
    de collection introuvables en pièces neuves. Un culbuteur usé peut- il casser et tomber dans le moteur ? Rarement mais
    possible sur des moteurs très kilométrés non entretenus. Une portée de came fortement usée peut conduire à une perte de
    matière par écaillage : les éclats se retrouvent alors dans le circuit d''huile et peuvent obstruer partiellement un gicleur
    d''huile ou un passage de lubrification. Dans les cas extrêmes, un culbuteur fissuré peut se désolidariser de son axe
    et bloquer mécaniquement une soupape en position ouverte, causant une perte de compression totale sur le cylindre concerné
    — voire une collision piston-soupape.'
  META: '{"meta_title":"Culbuteur : symptômes d''usure et remplacement","meta_description":"Claquements moteur, perte de puissance
    ou fumée d''échappement ? Identifiez un culbuteur défaillant et sélectionnez la pièce compatible avec votre moteur."}'
---

# Culbuteur - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre le mouvement de l'arbre a cames aux soupapes

**Actions principales:** transmettre, basculer, actionner

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement moteur regulier**
  claquement moteur regulier

### 🟢 Autres Symptômes

- bruit de tic-tic au ralenti
- perte de puissance sur un cylindre

## Procédure de Diagnostic

Pour diagnostiquer un problème de culbuteur:

1. **Inspection visuelle** - Examiner l'état du culbuteur
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur
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

- arbre-a-came
- kit-de-poussoir-culbuteur
- poussoir-de-soupape
- soupape-d-admission
- soupape-d-echappement

## Critères de Compatibilité

Pour commander le bon culbuteur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"

## FAQ

**Comment choisir Culbuteur compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Culbuteur ?**
En cas de claquement moteur regulier ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Culbuteur sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
