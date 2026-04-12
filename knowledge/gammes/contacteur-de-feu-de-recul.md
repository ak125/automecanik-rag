---
category: eclairage
slug: contacteur-de-feu-de-recul
title: Contacteur feu de recul
pg_id: 807
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
  last_enriched_by: script:materialize-db-to-md
  last_enriched_at: '2026-04-03'
  v5_migrated_at: '2026-03-29'
domain:
  role: Active les feux de recul en marche arrière
  must_be_true:
  - activer
  - signaler
  - commander
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
  - feu-avant
  - feu-arriere
  - phares-antibrouillard
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de compatibilite
    pour confirmer Contacteur feu de recul.
  - Verifier le type d ampoule (H1, H4, H7, LED, xenon) compatible avec le vehicule
  - Respecter la puissance et le culot exact de l ampoule d origine
  - Choisir des ampoules homologuees pour la circulation routiere
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "sécurité maximale"
  cost_range:
    min: 10
    max: 40
    currency: EUR
    unit: contacteur
    source: catalogue automecanik
  quality_tiers:
  - tier: Pièce OE (Origine Équipement)
    description: Contacteur identique à l origine. Filetage et connecteur parfaitement conformes. Option à envisager sur véhicules
      récents sous garantie.
  - tier: Équivalent OE (spécialistes électricité auto)
    description: Fabricants spécialisés en composants électriques automobiles. Qualité proche de l OE à prix accessible.
  - tier: Générique compatible
    description: Peut convenir si le filetage et le connecteur sont strictement identiques. Vérifier avant commande.
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
    label: Feux recul allument plus marche
    severity: confort
  - id: S2
    label: Feux de recul toujours allumes moteur demarre
    severity: confort
  - id: S3
    label: Fuite huile visible niveau contacteur
    severity: confort
  - id: S4
    label: Camera de recul inactive car contacteur defaillant
    severity: confort
  - id: S5
    label: Odeur huile boite vitesses autour
    severity: confort
  - id: S6
    label: Claquement bruit passage marche arriere
    severity: confort
  - id: S7
    label: Difficulte enclencher marche arriere contacteur
    severity: confort
  - id: S8
    label: Contacteur place depuis plus controle
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - 'Usure ou defaillance causant : feux recul allument plus marche'
  quick_checks:
  - 'Observer : feux recul allument plus marche ?'
  - 'Observer : feux de recul toujours allumes moteur demarre ?'
  - Fuite huile visible niveau contacteur ?
  - 'Observer : camera de recul inactive car contacteur defaillant ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Feux recul allument plus marche
  - Feux de recul toujours allumes moteur demarre
  - Fuite huile visible niveau contacteur
  - Camera de recul inactive car contacteur defaillant
  - Odeur huile boite vitesses autour
  - Claquement bruit passage marche arriere
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '807'
  intro_title: A quoi sert Contacteur feu de recul ?
  risk_title: Pourquoi remplacer Contacteur feu de recul a temps ?
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
  - question: Contacteur de feu de recul OE ou adaptable ?
    answer: Les contacteurs OES (Hella, FAE) ou adaptables de qualité conviennent. Vérifiez le type de filetage et le connecteur.
      Pièce peu coûteuse, privilégiez la qualité.
  - question: Comment savoir si mon contacteur de recul est HS ?
    answer: Feux de recul qui ne s'allument jamais, feux qui restent allumés en permanence, feux intermittents. Tester avec
      un multimètre (continuité en marche arrière).
  - question: Tous les combien changer le contacteur de recul ?
    answer: Pas de périodicité fixe. Durée de vie très variable. À remplacer si les feux de recul ne fonctionnent plus après
      vérification ampoule et fusible.
  - question: Peut-on changer le contacteur de recul soi-même ?
    answer: Oui, opération simple. Localiser le contacteur sur la boîte (fil électrique), débrancher, dévisser (attention
      à la fuite d'huile de boîte), revisser le neuf. 15-30 min.
  - question: Quelle erreur éviter avec le contacteur de recul ?
    answer: Prévoir un joint neuf si fourni. Avoir un récipient pour l'huile qui peut couler. Serrer au couple pour éviter
      les fuites. Vérifier le niveau d'huile de boîte après.
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
doc_id: 1295563c-6550-51c4-bb16-b1f833e4fc7b
content_hash: sha256:315afdbb2dd29b17
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
  - type: Hall
    source_ref: corpus RAG web OEM
  - type: hall
    source_ref: corpus RAG web OEM
  - type: plein
    source_ref: corpus RAG web OEM
  technical_notes:
    val_1_v: 1 v
    val_100_a: 100 a
    val_20_a: 20 a
    val_21_a: 21 a
    val_424_a: 424 a
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le contacteur de feu de recul est un interrupteur électromécanique vissé dans le carter de la boîte de vitesses. Son
    rôle est de détecter le passage en marche arrière et d''alimenter électriquement les feux de recul blancs situés à l''arrière
    du véhicule. Ces feux blancs signalent aux autres usagers que le véhicule recule — leur fonctionnement est exigé au contrôle
    technique et imposé par le Code de la Route. Sur les boîtes de vitesses manuelles, le contacteur est actionné mécaniquement
    par la fourchette de marche arrière ou par la tige de sélection : lorsque la marche arrière est engagée, une came ou un
    ergot déplace le piston du contacteur, ferme le circuit électrique et alimente les ampoules ou les LEDs des feux de recul.
    Sur les boîtes automatiques, le signal est généralement fourni par un capteur de position de sélecteur (PRNDL), et le
    contacteur physique est intégré dans le boîtier de levier ou dans le module de transmission. Trois catégories de contacteurs
    coexistent selon les technologies de boîte : - Contacteur mécanique fileté : le plus répandu sur les boîtes manuelles.
    Corps métallique vissé dans le carter de boîte (M16x1.5, M18x1.5 selon les marques), piston interne actionné mécaniquement.
    Pièce peu coûteuse, facilement remplaçable. Son joint d''étanchéité empêche les fuites d''huile de boîte. - Contacteur
    hydraulique : utilisé sur certaines boîtes où la pression hydraulique interne commande le signal électrique lors de l''engagement
    de la marche arrière. Moins courant, plus délicat à remplacer. - Contacteur pneumatique : présent sur certaines transmissions
    lourdes (véhicules utilitaires, boîtes robotisées). La variation de pression d''air commande le signal électrique. Le
    contacteur joue également un rôle secondaire sur les véhicules modernes : sur les voitures équipées d''une caméra de recul,
    le signal du contacteur déclenche l''affichage de l''image sur l''écran central. Sur les véhicules avec radar de stationnement
    arrière (PDC), ce signal active les capteurs ultrasoniques. Une défaillance du contacteur coupe donc simultanément les
    feux de recul, la caméra et les radars.'
  S2: 'Le contacteur de feu de recul n''a pas d''intervalle de remplacement fixe exprimé en kilomètres ou en années. Sa durée
    de vie dépend du nombre de passages en marche arrière (chaque manœuvre = un cycle du contacteur) et des conditions environnementales
    (chaleur, humidité, vibrations). Un conducteur urbain effectue 10 à 30 manœuvres en marche arrière par jour, soit 3 000
    à 10 000 cycles par an — le contacteur peut durer 10 à 20 ans dans de bonnes conditions. Remplacer le contacteur de feu
    de recul dans les cas suivants : - Feux de recul qui ne s''allument plus : premier symptôme. Avant de commander le contacteur,
    éliminer les autres causes possibles dans cet ordre : 1) vérifier les ampoules des deux feux de recul (les sortir et les
    tester), 2) vérifier le fusible correspondant dans le boîtier à fusibles (chercher "reverse light" ou "feux recul" sur
    le couvercle), 3) tester la continuité électrique du contacteur au multimètre. Si les ampoules et le fusible sont bons,
    le contacteur est défaillant. - Feux de recul qui restent allumés en permanence : le contacteur est bloqué en position
    fermée (court- circuit interne ou piston coincé). Ce symptôme décharge la batterie si le véhicule est garé longtemps et
    peut griller les ampoules par surchauffe prolongée. - Feux de recul intermittents : le contacteur s''ouvre et se ferme
    de façon aléatoire lors de vibrations ou de changements de température. Les contacts internes sont oxydés ou le piston
    est en fin de course. Un test multimètre en secouant le faisceau révèle le problème. - Fuite d''huile de boîte au niveau
    du contacteur : le joint d''étanchéité est usé ou le corps du contacteur est fissuré. La fuite doit être traitée sans
    délai pour éviter une baisse de niveau d''huile de boîte. Vérifier le niveau d''huile avant toute autre intervention.
    - Caméra de recul ou radar PDC inactif : si la caméra de recul ou les capteurs de stationnement arrière ne s''activent
    plus lors du passage en marche arrière, et que le diagnostic OBD ne pointe pas vers les capteurs eux-mêmes, tester le
    contacteur en premier — il commande l''alimentation de ces systèmes sur de nombreux modèles. - Contacteur posé depuis
    plus de 15 ans : à titre préventif, lors d''une intervention en sous- caisse ou d''une vidange de boîte, inspecter l''état
    du contacteur et le remplacer si le caoutchouc d''étanchéité est durci ou si des traces de corrosion sont visibles sur
    le corps.'
  S3: 'Le contacteur de feu de recul est un commutateur mécanique ou électronique vissé sur le carter de boîte de vitesses
    : il détecte l''engagement de la marche arrière et envoie le signal d''alimentation aux feux de recul et, sur les véhicules
    récents, à la caméra de recul. Sa défaillance prive le conducteur des feux arrière blancs imposés par le Code de la Route,
    ce qui constitue un motif de non-conformité au contrôle technique. Le choix doit être précis car les caractéristiques
    électriques et mécaniques varient selon la boîte montée sur le véhicule. - Type de boîte de vitesses (manuelle, automatique,
    robotisée) — Le contacteur est spécifique au type de transmission. Une boîte manuelle utilise un contacteur mécanique
    actionné par le levier de vitesse, tandis qu''une boîte automatique peut utiliser un commutateur intégré au module de
    position sélecteur (PRNDL). Les références sont incompatibles entre ces deux familles. - Référence OE ou référence boîte
    de vitesses — La référence du contacteur est liée au code boîte, pas uniquement au modèle de véhicule. Sur un même modèle,
    plusieurs boîtes peuvent coexister selon l''année ou la motorisation. Vérifier le code boîte gravé sur le carter (exemple
    : JH3, ML6, PF6) avant de commander. - Filetage et pas de vis — Le contacteur se visse directement dans le carter de boîte.
    Le diamètre de filetage (M10, M12, M16 selon les constructeurs) et le pas (1,0 ; 1,25 ou 1,5 mm) doivent être identiques
    à l''original. Un filetage différent endommage le carter de boîte irrémédiablement. - Tension de service et courant nominal
    — Le contacteur doit supporter la tension du circuit (12 V) et le courant d''alimentation des feux de recul (1 à 5 A selon
    le nombre d''ampoules ou LEDs). Un contacteur sous-dimensionné en courant chauffe et tombe en défaut en quelques semaines.
    - Connecteur et nombre de broches — Vérifier le nombre de broches (2 broches sur les versions simples, 3 ou 4 broches
    sur les versions avec signal caméra de recul). La forme du connecteur femelle sur le câblage véhicule doit correspondre
    exactement pour éviter l''adaptation par soudure. - Présence d''un joint d''étanchéité — Le contacteur est en contact
    avec l''huile de boîte. Vérifier que la pièce est livrée avec le joint torique adapté (NBR ou FKM selon l''huile de boîte
    utilisée). Un joint absent ou de mauvaise matière entraîne une fuite d''huile lente au niveau du filetage. Pour aller
    plus loin : consultez notre guide d''achat contacteur feu de recul — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 📖 Avant de démonter, consultez la fiche technique Contacteur de feu de recul pour connaître les spécifications.
    - Débranchez la batterie. - Levez et calez le véhicule si nécessaire. - Dans certain véhicule le contacteur de feux de
    recul est accessible parla partie moteur dans ce cas il faudra démontez toutes les pièces pourfaciliter l'accès (le boîtier
    du filtre à air , la batterie, le bac de labatterie ). - Localisez l'emplacement du contacteur des feux de recul. - Débranchez
    le connecteur électrique du contacteur des feux de recul. - A l'aide d'une clé appropriée dévissez le contacteur des feux
    de recul dansle sens antihoraire. - Retirez le contacteur des feux de recul.
  S4_REPOSE: '- Vérifier la compatibilité du contacteur neuf avant la pose : comparer le contacteur neuf avec celui déposé
    — filetage (M16x1.5 ou M18x1.5 le plus courant), longueur totale du corps, nombre de broches du connecteur et type de
    connecteur. Un contacteur de dimension différente ne s''engage pas correctement dans le taraudage de la boîte et ne commande
    pas le circuit correctement. - Contrôler l''état des ampoules de feux de recul : avant de visser le contacteur neuf, tester
    les deux ampoules de feux de recul. Si l''ancien contacteur était en court-circuit (feux restés allumés en permanence),
    les ampoules ont pu être grillées par la surchauffe. Remplacer les deux ampoules simultanément si l''une est grillée.
    - Préparer le joint d''étanchéité neuf : déposer l''ancien joint du taraudage si il est resté en place. Appliquer une
    fine couche de pâte d''étanchéité compatible huile de boîte (cuivre ou silicone) sur le joint neuf si aucun joint n''est
    fourni avec le contacteur. Ne jamais remonter sans joint — une fuite d''huile de boîte au niveau du contacteur peut entraîner
    un niveau d''huile insuffisant et une destruction de la boîte. - Engager le contacteur neuf à la main : visser à la main
    sur les premiers filets pour s''assurer que le filetage s''engage correctement (pas de vissage en force). Serrer progressivement
    avec la clé adaptée (clé à douille ou clé à fourche). Couple de serrage : généralement entre 15 et 25 N.m selon le modèle
    — s''en tenir aux préconisations constructeur. Un serrage excessif sur un carter en aluminium risque de fissurer le logement
    ou d''arracher le filetage. - Rebrancher le connecteur électrique : clipser le connecteur jusqu''au clic de verrouillage
    franc. Tirer légèrement sur le câble après clipsage pour confirmer le verrouillage. Un connecteur mal verrouillé provoque
    des intermittences à chaud ou lors de vibrations. - Remonter les pièces d''accès démontées : protections sous-caisse,
    garde-boue si déposé, cache moteur. Rebrancher la batterie, borne positive en premier. - Mettre le contact et tester immédiatement
    : passer en marche arrière. Les deux feux de recul doivent s''allumer simultanément. Repasser en neutre : les feux doivent
    s''éteindre. Vérifier également que la caméra de recul et les capteurs de stationnement s''activent si le véhicule en
    est équipé.'
  S5: 'Erreurs frequentes avec le contacteur de feu de recul : - Ne pas verifier le fusible et l''ampoule avant de remplacer
    le contacteur — ce sont les causes de panne les plus frequentes et les moins couteuses- Oublier de verifier l''etancheite
    apres montage — le contacteur est visse sur la boite de vitesses, un joint defectueux provoque une fuite d''huile de boite-
    Confondre contacteur de recul et contacteur de point mort (sur boite auto) — les deux sont sur la boite mais n''ont pas
    la meme fonction- Ne pas respecter le couple de serrage — trop serre le contacteur casse, pas assez il fuit- Ignorer un
    feu de recul qui ne s''allume plus — c''est un motif de contre- visite au controle technique'
  S6: 'Le contacteur de feu de recul est une pièce électrique simple à poser mais qui implique une ouverture du carter de
    boîte. Les vérifications post- montage portent sur trois axes : fonctionnement électrique, étanchéité mécanique et validation
    des systèmes associés. - Test immédiat du fonctionnement électrique des feux de recul : mettre le contact, passer la marche
    arrière avec le pied sur la pédale de frein (boîte automatique) ou en manœuvrant la boîte (boîte manuelle). Les deux feux
    de recul doivent s''allumer simultanément, avec la même intensité lumineuse. Un seul feu allumé indique que l''ampoule
    de l''autre côté est défaillante — le contacteur fonctionne correctement mais une ampoule est grillée. Repasser en neutre
    ou point mort : les feux doivent s''éteindre immédiatement. - Test de l''étanchéité au joint d''huile de boîte : démarrer
    le moteur et laisser tourner 5 à 10 minutes pour mettre la boîte à température. Inspecter la zone du contacteur avec une
    lingette propre — toute trace d''huile ATF (rouge) ou d''huile de boîte manuelle (brun/or) indique une fuite au joint.
    Serrer légèrement si la fuite est minime (1/8 de tour maximum), ou déposer et revisser avec un joint neuf si la fuite
    persiste. - Vérification du couple de serrage : si la clé dynamométrique n''a pas été utilisée lors de la pose, contrôler
    que le contacteur n''est pas trop lâche (risque de fuite) ni trop serré (risque de fissure du carter). Le couple correct
    est généralement de 15 à 25 N.m selon le modèle. - Contrôle du connecteur électrique : tirer légèrement sur le câble du
    connecteur pour confirmer que le verrouillage est actif. Faire vibrer le câble manuellement pendant que quelqu''un surveille
    les feux de recul allumés — une intermittence lors de la vibration indique un connecteur mal clipsé ou des contacts oxydés.
    - Vérification des systèmes associés : sur les véhicules équipés d''une caméra de recul, vérifier que l''image apparaît
    sur l''écran central lors du passage en marche arrière. Sur les véhicules avec radar de stationnement arrière (PDC), confirmer
    que les bips sonores et l''affichage s''activent bien. Un contacteur correctement posé déclenche ces deux fonctions automatiquement.
    - Dix cycles de marche arrière consécutifs : passer dix fois consécutivement entre la marche arrière et le point mort
    (boîte manuelle) ou le neutre (boîte automatique) en observant les feux de recul à chaque cycle. Les feux doivent réagir
    instantanément sans délai ni intermittence, ce qui valide le bon positionnement du piston du contacteur dans son logement
    et l''absence d''oxydation sur les contacts.'
  S7: Quel est le prix d'un contacteur feu de recul ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur
    pour trouver le contacteur feu de recul compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon contacteur feu de recul est à changer ?Les signes d'usure les plus courants sont détaillés dans la section
    diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un contacteur
    feu de recul défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule.
    Consultez la section symptômes pour évaluer l'urgence du remplacement.- activer - signaler - commander
  S8: Comment choisir Contacteur feu de recul compatible avec mon vehiculeRenseignez marque, modele, type moteur et annee,
    puis verifiez la reference Quand remplacer Contacteur feu de recul ?En cas de feux recul allument plus marche ou de degradation
    mesurable, Puis-je monter Contacteur feu de recul sans verification atelier ?Le montage peut exiger controles de couple,
    alignement et references.
  META: '{"meta_title":"Contacteur feu de recul : diagnostic et remplacement","meta_description":"Feux de recul éteints ou
    toujours allumés, fuite d''huile au niveau du contacteur ? Identifiez les causes et sachez quand remplacer le contacteur
    de feu de recul."}'
---

# Contacteur feu de recul - Guide Diagnostic Complet

## Fonction et Rôle

Active les feux de recul en marche arrière

**Actions principales:** activer, signaler, commander

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement bruit passage marche arriere**
  claquement bruit passage marche arriere

### 🟢 Autres Symptômes

- feux recul allument plus marche
- feux de recul toujours allumes moteur demarre
- fuite huile visible niveau contacteur
- camera de recul inactive car contacteur defaillant
- odeur huile boite vitesses autour
- difficulte enclencher marche arriere contacteur

## Procédure de Diagnostic

Pour diagnostiquer un problème de contacteur feu de recul:

1. **Inspection visuelle** - Examiner l'état du contacteur feu de recul
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

- ampoule-feu-arriere
- commande-d-eclairage
- feu-arriere
- feu-avant
- feu-clignotant

## Critères de Compatibilité

Pour commander le bon contacteur feu de recul, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "sécurité maximale"

## FAQ

**Contacteur de feu de recul OE ou adaptable ?**
Les contacteurs OES (Hella, FAE) ou adaptables de qualité conviennent. Vérifiez le type de filetage et le connecteur. Pièce peu coûteuse, privilégiez la qualité.

**Comment savoir si mon contacteur de recul est HS ?**
Feux de recul qui ne s'allument jamais, feux qui restent allumés en permanence, feux intermittents. Tester avec un multimètre (continuité en marche arrière).

**Tous les combien changer le contacteur de recul ?**
Pas de périodicité fixe. Durée de vie très variable. À remplacer si les feux de recul ne fonctionnent plus après vérification ampoule et fusible.

**Peut-on changer le contacteur de recul soi-même ?**
Oui, opération simple. Localiser le contacteur sur la boîte (fil électrique), débrancher, dévisser (attention à la fuite d'huile de boîte), revisser le neuf. 15-30 min.

**Quelle erreur éviter avec le contacteur de recul ?**
Prévoir un joint neuf si fourni. Avoir un récipient pour l'huile qui peut couler. Serrer au couple pour éviter les fuites. Vérifier le niveau d'huile de boîte après.
