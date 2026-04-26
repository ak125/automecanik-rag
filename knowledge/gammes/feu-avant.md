---
category: eclairage
slug: feu-avant
title: Feu avant
pg_id: 259
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
  role: Éclaire la route devant le véhicule
  must_be_true:
  - eclairer
  - illuminer
  must_not_contain:
  - injection
  - freinage
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - ampoule-feu-avant
  - ampoule-feu-arriere
  - feu-arriere
  - phares-antibrouillard
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
    min: 80
    max: 400
    currency: EUR
    unit: phare standard
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    description: Phare identique à celui d'usine. Recommandé pour les véhicules premium ou les phares xénon/LED de série.
  - tier: Équivalent OE (OES)
    description: Valeo, Hella et Magneti Marelli fabriquent souvent les phares en première monte. Qualité premium pour un
      prix inférieur à l'OE.
  - tier: Adaptable (aftermarket)
    description: Fabricants spécialisés dans l'éclairage aftermarket. Convient pour l'halogène standard. Pour le xénon ou
      LED, l'OES est recommandé.
  brands:
    premium:
    - Osram
    - Philips
    standard:
    - Bosch
    - Hella
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Eclairage insuffisant nuit malgre ampoules
    severity: confort
  - id: S2
    label: Phare qui ne s allume plus ou par intermittence
    severity: confort
  - id: S3
    label: Condensation ou eau a l interieur du bloc optique
    severity: confort
  - id: S4
    label: Reglage impossible phares faisceau toujours
    severity: confort
  - id: S5
    label: Odeur de plastique brule au niveau du phare
    severity: confort
  - id: S6
    label: Phare opaque couleur jaunie reduisant
    severity: confort
  - id: S7
    label: Grincement ou bruit metallique du reglage de phare
    severity: confort
  - id: S8
    label: Perte luminosite progressive meme ampoules
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : eclairage insuffisant nuit malgre ampoules'
  quick_checks:
  - 'Observer : eclairage insuffisant nuit malgre ampoules ?'
  - 'Observer : phare qui ne s allume plus ou par intermittence ?'
  - 'Observer : condensation ou eau a l interieur du bloc optique ?'
  - 'Observer : reglage impossible phares faisceau toujours ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Eclairage insuffisant nuit malgre ampoules
  - Phare qui ne s allume plus ou par intermittence
  - Condensation ou eau a l interieur du bloc optique
  - Reglage impossible phares faisceau toujours
  - Odeur de plastique brule au niveau du phare
  - Phare opaque couleur jaunie reduisant
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '259'
  intro_title: A quoi sert Feu avant ?
  risk_title: Pourquoi remplacer Feu avant a temps ?
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
  - question: Phare OE, OES ou adaptable ?
    answer: Les phares OES (Valeo, Hella, Magneti Marelli) sont de qualité premium. Les adaptables (TYC, DEPO) conviennent
      pour un usage standard. Pour le xénon/LED, privilégiez l'OE ou OES.
  - question: Comment savoir si mon phare est HS ?
    answer: Glace cassée ou fissurée, phare opaque (rénovation possible), buée permanente à l'intérieur, support de fixation
      cassé, réglage impossible.
  - question: Tous les combien changer le phare avant ?
    answer: Pas de périodicité. Un phare opaque peut être rénové (polissage). Remplacement si cassé ou si la rénovation ne
      suffit plus.
  - question: Peut-on changer un phare soi-même ?
    answer: Oui mais parfois complexe. Certains véhicules nécessitent de déposer le pare-chocs. Prévoir 30 min à 2h selon
      modèle. Réglage des feux conseillé après.
  - question: Quelle erreur éviter avec le phare avant ?
    answer: Ne pas mélanger halogène et xénon. Faire régler les feux après remplacement (éblouissement). Vérifier l'homologation
      E sur le phare neuf.
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
doc_id: 0b526ffc-9fbe-5597-82c7-60795e004829
content_hash: sha256:0896686b447f5ab1
lang: fr
variants:
- name: Ampoule halogene
  aliases:
  - halogene
  - H1
  - H4
  - H7
  functional_differences:
  - Standard, economique
  - Remplacement simple
- name: Ampoule LED
  aliases:
  - LED
  functional_differences:
  - Duree de vie superieure
  - Consommation reduite
  - Verifier homologation
location_on_vehicle:
  area: Face avant, arriere et laterale du vehicule
  access: Par le compartiment moteur (avant) ou coffre (arriere)
  adjacent_parts:
  - optique
  - ampoule
  - connecteur
  - reflecteur
installation:
  difficulty: facile
  time: 5 a 15 min
  tools:
  - tournevis
  - gants (ne pas toucher ampoule halogene)
  prerequisite: Moteur eteint, acces par compartiment moteur ou coffre
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'Hall'
    source_ref: corpus RAG web OEM
  - type: 'Nao'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_14_a: '14 a'
    val_2__: '2 %'
    val_2_a: '2 a'
    val_20__: '20 %'
    val_30_a: '30 a'
    val_35__: '35 %'
    val_4_a: '4 a'
    val_6__: '6 %'
    val_78__: '78 %'
    val_80__: '80 %'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Les feux avant sontdes projecteurs de lumière leurs rôle est éclairé la route empruntée par unvéhicule la nuit. Ils
    sont aussi des constituants principaux de l''éclairage standard d''une automobile. Les phares avant servent à rendre la
    voiture plusvisible par les autres (par exemple lorsqu''il ya du brouillard ou de la pluie).Sur les modèles de voiture
    les plus récent il existe des feux de jour pouraccroître la visibilité diurne. Ils assurent les fonctions feu de route,
    feu de croisement et feu de position . Un véhicule compte un nombre impressionnantde dispositifs d''éclairage et de signalisation,qui
    sont placés à l''avant du véhicule, ils changent d''un automobile à un autreselon l''équipement de votre voiture : - Les
    feux de route : ils permettent au conducteurde voir loin lors de la conduite dans une route sans éclairage pendant la
    nuit.Ils peuvent être complétés par les feux de brouillard si la chaussée est vraiment sinueuse. Ce typed''éclairage est
    représenté sur le tableau de bord par une image d''un phare bleuémettant une onde lumineuse qu''est orientée perpendiculairement
    au phare. Lesfeux de routes ont une portée de 100 mètres minimum, et on les utilise sur desroutes sans aucun éclairage
    et si le véhicule est seul sur la chaussée. - Les feux de croisement : ils sont nommés aussipar feu de codes, ils sont
    représentés par l''image d''un phare vert émettantdes rayons lumineux en diagonale, vers le bas à gauche. La portée des
    feux decroisement est de 30 mètres minimum, ils vont permettre aux usagers de laroute de voir le véhicule pendant la nuit
    si le véhicule roule sur une route bienéclairée ou sur une route non éclairée mais comprenant d''autre véhicule. Attention
    : lors de l''utilisation des feux de route etsi vous croisez un autre véhicule, le conducteur doit absolument passer en
    feux de croisement, pour ne pas gênerl''autre voiture. - Les feux de position : ce type d''éclairage estutilisé dans des
    situations de faible visibilité, ils servent pour être vu parles usagers de la route, mais ils ne produisent pas un éclairage
    suffisant pourconduire de nuit ou en cas de mauvaise visibilité. Ils sont représentés sur letableau de bord par un symbole
    d''ampoule vert et ils ont une couleur blanche àl''avant. En savoir plus : feu avant — définition et rôle mécanique 🚨
    Bruit Feu avant : causes et diagnostic'
  S2: 'Un feu avantdéfectueux présente plusieurs symptômes : - Manque d''éclairage lors de l''utilisation des feux avant.
    - Lors d''un contrôle visuel vous remarquez que le feu avant est fissuré. - Lors d''un contrôle visuel vous remarquez
    que le feu avant est sale à l''intérieur. Un feu avant HS etqu''il n''est pas remplacé à temps peut causer des risques
    d''accidents lors del''utilisation de la route et le refus de votre véhicule lors du contrôletechnique. Diagnostic complet
    : identifier une panne de feu avant'
  S3: 'Sélectionner un feu avant (phare) demande une rigueur particulière : ces blocs optiques sont homologués par type de
    véhicule et intègrent des fonctions multiples (code, route, antibrouillard, DRL) qui varient d''une version à l''autre.
    Un phare mal choisi peut altérer la portée du faisceau, éblouir les autres usagers ou déclencher un refus au contrôle
    technique. Voici les paramètres techniques à contrôler avant commande. - Position gauche ou droit et référence OEM — Un
    phare avant gauche et un phare avant droit ont des géométries de lentilles inversées pour répartir le faisceau correctement
    selon le côté de conduite. La référence OEM (Origin Equipment Manufacturer) gravée sur le boîtier d''origine ou renseignée
    dans la documentation constructeur est le seul identifiant fiable. - Marque, modèle, millésime et phase de restylage —
    Un modèle vendu sur 10 ans peut avoir subi 2 à 3 facelifts qui modifient profondément la forme du phare. Renseignez le
    millésime exact (ex. : 09/2018) et non uniquement l''année civile, car la coupure constructeur peut intervenir en milieu
    d''année. - Technologie de source lumineuse — Halogen (H7, H4, H1), Xénon/HID (D1S, D2S, D3S, D4S) ou Full LED sont des
    technologies incompatibles entre elles sans modification électronique lourde. Un phare xénon nécessite un ballast et des
    correcteurs d''assiette spécifiques ; un phare LED intègre son propre driver et ne peut pas recevoir d''ampoule aftermarket.
    - Présence de réglage électrique et correcteur de portée — De nombreux véhicules modernes utilisent un correcteur de portée
    motorisé piloté par la CAN-bus. Vérifiez que le phare de remplacement intègre le même motoréducteur et dispose du même
    connecteur de pilotage, sous peine de code défaut permanent et de faisceau fixe non réglable. - Fonctions intégrées :
    DRL, clignotant, antibrouillard — Selon la version d''équipement du véhicule (entrée de gamme vs version haute), les DRL
    (feux diurnes) et le clignotant peuvent être intégrés dans le bloc principal ou non. Comparez la liste des fonctions du
    phare d''origine avec celle du phare de remplacement avant de valider la commande. - Indice d''étanchéité et qualité du
    joint périmétrique — La condensation à l''intérieur du bloc optique (buée visible) résulte d''un joint d''étanchéité défaillant.
    Lors du remplacement, vérifiez que la pièce inclut le joint de pourtour en état et un indice IP67 minimum. Un phare humide
    dégrade la portée lumineuse de 30 à 50 % en quelques mois. - Certification E-Mark et conformité aux normes ECE — Seules
    les pièces portant le marquage E (cercle + numéro de pays homologateur) sont légalement conformes pour circulation sur
    voie publique en Europe. Évitez toute offre présentant des termes comme "universel", "compatible tous modèles" ou "adaptable"
    : ces qualificatifs signalent une pièce hors référence constructeur. Pour aller plus loin : consultez notre guide d''achat
    feu avant — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 📖 Avant de démonter, consultez la fiche technique Feu avant pour connaître les spécifications. - Débranchez la
    batterie. - Démontez les caches de protection situés dans le feu avant. - Débranchez les connecteurs du feu avant. - Desserrez
    les fixations du pare-choc avant. - Démontez le pare-choc avant. - Localisez les différentes fixations du feu avant. -
    Desserrez les fixations du feu avant. - Démontez le feu avant.
  S4_REPOSE: 'Une fois le feu avant neuf en main, le remontage suit un ordre strict pour garantir l''étanchéité du bloc optique,
    le bon positionnement du faisceau lumineux et l''absence de faux contact. Vérifiez la conformité de la référence avant
    d''engager la première fixation. - Contrôlez que le feu avant neuf porte la même référence et le même type de source lumineuse
    (halogène, xénon ou LED) que le bloc déposé. Un phare xénon ne s''adapte jamais à un circuit halogène sans kit de conversion.
    - Inspectez les ampoules de feu avant : si elles présentent un noircissement ou un filament cassé, remplacez-les avant
    la repose pour éviter un second démontage immédiat. - Vérifiez l''état du joint périphérique du bloc optique. S''il est
    écrasé ou fissuré, enduisez la gorge d''un léger cordon de mastic silicone transparent pour prévenir toute infiltration
    d''humidité. - Positionnez le feu avant dans son logement en engageant d''abord les plots de centrage puis les pattes
    de fixation. Ne forcez pas : toute résistance indique un mauvais alignement. - Serrez les vis ou écrous de fixation du
    feu avant en croix, progressivement, au couple préconisé par la revue technique (généralement entre 5 et 10 N·m selon
    le modèle). - Rebranchez les connecteurs électriques jusqu''au clic de verrouillage. Sur les véhicules équipés de correction
    électronique d''assiette, rebranchez aussi le capteur de niveau. - Remontez le pare-chocs avant ou les caches de protection,
    en commençant par clipser les agrafes latérales avant de revisser les points de fixation inférieurs. - Rebranchez la batterie
    en connectant d''abord la borne positive (+), puis la borne négative (-). - Allumez les feux et vérifiez le fonctionnement
    de chaque fonction : feux de croisement, feux de route, feux de position et, si présent, feu diurne (DRL). Effectuez également
    un test de la correction électrique de site si le véhicule en est équipé. - Faites régler l''orientation du faisceau sur
    banc de réglage de phares (obligatoire après tout remplacement de bloc optique) pour éviter d''éblouir les conducteurs
    venant en sens inverse. ✅ Après remontage, vérifiez les spécifications dans la fiche technique Feu avant.'
  S5: 'Erreurs frequentes avec les feux avant : - Ne pas verifier le cote (gauche/droite) et le type (halogene, xenon, LED)
    avant achat — les references et connectiques different completement- Toucher l''ampoule halogene avec les doigts — la
    graisse cutanee cree un point chaud qui fait eclater l''ampoule. Manipuler avec un chiffon propre- Ne pas regler les feux
    apres remplacement du bloc optique — un feu mal regle eblouit les autres conducteurs la nuit- Confondre un probleme de
    ballast avec un defaut d''ampoule xenon — le ballast est un composant separe qui alimente l''ampoule, tester les deux-
    Ignorer un feu avant opaque ou jauni — la polycarbonate se degrade aux UV, reduit l''eclairage de 40% et c''est un motif
    de contre- visite- Oublier de verifier l''etancheite du joint apres montage — la buee dans le phare corrode le reflecteur
    et reduit l''eclairage'
  S6: 'Le remplacement d''un feu avant (bloc optique ou projecteur) impose des vérifications fonctionnelles et un réglage
    de faisceau avant toute conduite nocturne. Un phare mal réglé éblouit les autres conducteurs et peut entraîner un refus
    au contrôle technique.- Fonctionnement des deux faisceaux — code et route — Testez le feu de croisement (feu de code)
    et le feu de route indépendamment. Chaque faisceau doit s''allumer sans scintillement. Sur les projecteurs bi-xénon ou
    full LED, attendez 10 secondes pour vérifier la stabilité de l''arc.- Réglage de la hauteur de faisceau — Placez le véhicule
    à charge normale devant un mur blanc à 10 mètres. Le bord supérieur du faisceau code doit se trouver entre 0,9 et 1,1
    % de déflexion par rapport à la hauteur du centre du phare (soit environ 10 cm en dessous de la hauteur d''axe à 10 m).
    Ajustez via la vis de réglage vertical.- Absence de condensation intérieure — Après 15 minutes de fonctionnement avec
    les feux allumés, vérifiez l''absence de buée à l''intérieur du bloc. Une condensation persistante indique que le cache
    arrière ou l''évent de décompression n''a pas été correctement reposé.- Symétrie des faisceaux gauche/droit — Observez
    les deux phares depuis l''avant du véhicule : la forme et la hauteur de la coupure de faisceau doivent être identiques
    des deux côtés. Une asymétrie révèle un problème de position du réflecteur ou de la douille d''ampoule.- Correcteur de
    hauteur automatique fonctionnel — Sur les véhicules avec correcteur électrique, changez la charge (passagers à l''arrière
    ou chargement) et vérifiez que le faisceau s''ajuste automatiquement en quelques secondes. Un faisceau fixe malgré la
    charge signale un capteur de hauteur ou un moteur de correcteur défaillant.- Absence d''odeur de plastique brûlé — Après
    30 minutes de fonctionnement en feux de croisement, aucune odeur ne doit être perceptible au niveau du phare. Une odeur
    indique une ampoule incompatible (puissance trop élevée) ou un mauvais positionnement dans le réflecteur.- Connexion électrique
    sécurisée — Vérifiez que le connecteur principal du phare est verrouillé et que le cache arrière du phare est correctement
    fermé. Un cache mal positionné expose l''ampoule à l''humidité et provoque une dégradation prématurée du réflecteur.'
  S7: Quel est le prix d'un feu avant ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur pour trouver
    le feu avant compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment savoir si mon
    feu avant est à changer ?Les signes d'usure les plus courants sont détaillés dans la section diagnostic ci-dessus. En
    cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un feu avant défaillant ?Cela dépend
    de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule. Consultez la section symptômes
    pour évaluer l'urgence du remplacement.- ampoule feu avant - commande d eclairage - feu arriere - feu clignotant
  S8: Comment choisir Feu avant compatible avec mon vehicule ?Renseignez marque, modele, type moteur et annee, puis verifiez
    la reference Quand remplacer Feu avant ?En cas de eclairage insuffisant nuit malgre ampoules ou de degradation Puis-je
    monter Feu avant sans verification atelier ?Le montage peut exiger controles de couple, alignement et references.
  META: '{"meta_title":"Feu avant : Guide Remplacement Phare | AutoMecanik","meta_description":"Phare jauni, condensation,
    éclairage insuffisant : identifiez quand changer votre feu avant, comment choisir le bon bloc optique et le remplacer
    vous-même. Guide AutoMecanik."}'
---

# Feu avant - Guide Diagnostic Complet

## Fonction et Rôle

Éclaire la route devant le véhicule

**Actions principales:** eclairer, illuminer

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Grincement ou bruit metallique du reglage de phare**
  grincement ou bruit metallique du reglage de phare

### 🟢 Autres Symptômes

- eclairage insuffisant nuit malgre ampoules
- phare qui ne s allume plus ou par intermittence
- condensation ou eau a l interieur du bloc optique
- reglage impossible phares faisceau toujours
- odeur de plastique brule au niveau du phare
- phare opaque couleur jaunie reduisant

## Procédure de Diagnostic

Pour diagnostiquer un problème de feu avant:

1. **Inspection visuelle** - Examiner l'état du feu avant
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

- ampoule-feu-avant
- commande-d-eclairage
- feu-arriere
- feu-clignotant

## Critères de Compatibilité

Pour commander le bon feu avant, vous devez connaître:

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

**Phare OE, OES ou adaptable ?**
Les phares OES (Valeo, Hella, Magneti Marelli) sont de qualité premium. Les adaptables (TYC, DEPO) conviennent pour un usage standard. Pour le xénon/LED, privilégiez l'OE ou OES.

**Comment savoir si mon phare est HS ?**
Glace cassée ou fissurée, phare opaque (rénovation possible), buée permanente à l'intérieur, support de fixation cassé, réglage impossible.

**Tous les combien changer le phare avant ?**
Pas de périodicité. Un phare opaque peut être rénové (polissage). Remplacement si cassé ou si la rénovation ne suffit plus.

**Peut-on changer un phare soi-même ?**
Oui mais parfois complexe. Certains véhicules nécessitent de déposer le pare-chocs. Prévoir 30 min à 2h selon modèle. Réglage des feux conseillé après.

**Quelle erreur éviter avec le phare avant ?**
Ne pas mélanger halogène et xénon. Faire régler les feux après remplacement (éblouissement). Vérifier l'homologation E sur le phare neuf.
## Phares et feux

### Phares faibles
- **Ampoules vieillissantes** : Les ampoules halogènes perdent 20-30% de luminosité après 2-3 ans. Remplacement par paire recommandé.
- **Optiques ternies** : Le polycarbonate des phares jaunit et devient opaque avec le temps. Kit de rénovation ou polissage.
- **Réglage incorrect** : Phares trop bas après un chargement ou un remplacement. Réglage avec les vis dédiées.

### Ampoules grillées fréquemment
- **Surtension** : Régulateur d'alternateur défaillant (tension > 14.8V). Mesurer la tension de charge.
- **Vibrations excessives** : Ampoule mal fixée dans son support, vibrations transmises au filament.
- **Mauvaise qualité** : Préférer des ampoules de marque (Philips, Osram, Bosch).

### Feux qui ne fonctionnent pas
- **Fusible grillé** : Vérifier le fusible correspondant dans la boîte à fusibles.
- **Connecteur oxydé** : Humidité dans le porte-ampoule, nettoyage et graisse contact.
- **Problème de masse** : Fil de masse corrodé au niveau du feu. Fréquent sur les feux arrière.

## Contrôle technique - Points éclairage

- Tous les feux doivent fonctionner : croisement, route, position, stop, recul, clignotants, antibrouillard arrière
- Hauteur de faisceau correcte (réglage)
- Pas de fissure laissant entrer l'eau dans les optiques
- Couleur conforme : blanc devant, rouge derrière, orange pour les clignotants

## LED vs Halogène vs Xénon

- **Halogène (H7, H4, H1)** : Standard, remplacement facile, coût faible
- **Xénon (D1S, D2S, D3S)** : Puissant, durée de vie longue, remplacement coûteux, nécessite un ballast
- **LED** : Très longue durée de vie, faible consommation, remplacement du bloc optique entier en cas de panne

## Quand consulter un professionnel

- Phare xénon qui clignote ou change de couleur (ballast ou ampoule)
- Feux LED intégrés défaillants (remplacement du bloc complet)
- Court-circuit récurrent (fusible qui saute à chaque remplacement)
- Défaut de réglage persistant malgré les ajustements
