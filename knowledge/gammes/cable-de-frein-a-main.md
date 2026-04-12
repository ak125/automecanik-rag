---
category: freinage
slug: cable-de-frein-a-main
title: Câble de frein à main
pg_id: 124
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
  role: Transmet la commande du frein de stationnement
  must_be_true:
  - transmettre
  - actionner
  - maintenir
  must_not_contain:
  - injection
  - climatisation
  - embrayage
  - distribution
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - disque-de-frein
  - plaquette-de-frein
  - etrier-de-frein
  - flexible-de-frein
  - maitre-cylindre-de-frein
  - liquide-de-frein
  confusion_with:
  - term: piece-de-freinage-voisine
    difference: 'Verifier la reference exacte : les pieces de freinage se ressemblent mais ne sont pas interchangeables entre
      essieux ou types de montage.'
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
  - ❌ "meilleur freinage"
  cost_range:
    min: 24
    max: 49
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Constructeur (OE)
    description: Câble d'origine avec longueur, gaine et embouts conformes au véhicule. Référence de compatibilité absolue.
  - tier: Équivalent OE (OES)
    description: 'Câbles fabriqués par des équipementiers reconnus dans ce segment : TRW, Cofle, Adriauto. Qualité comparable
      à l''OE, référence croisée disponible.'
  - tier: Adaptable
    description: Câble de longueur approximative ou avec embouts universels. Vérifier impérativement la longueur totale et
      le type d'embouts avant commande.
  brands:
    premium:
    - Brembo
    - ATE
    - TRW
    standard:
    - Bosch
    - Ferodo
    - Textar
    budget:
    - Ridex
    - Valeo
diagnostic:
  symptoms:
  - id: S1
    label: Frein a main qui ne tient plus en cote
    severity: securite
  - id: S2
    label: Course du levier excessive plus de 7 clics
    severity: confort
  - id: S3
    label: Vehicule roule alors frein main
    severity: securite
  - id: S4
    label: Cable visible effiloche ou rouille
    severity: confort
  - id: S5
    label: Bruit de frottement a l arriere en roulant
    severity: confort
  - id: S6
    label: Levier de frein a main mou ou sans resistance
    severity: securite
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : frein a main qui ne tient plus en cote'
  quick_checks:
  - 'Observer : frein a main qui ne tient plus en cote ?'
  - 'Observer : course du levier excessive plus de 7 clics ?'
  - 'Observer : vehicule roule alors frein main ?'
  - 'Observer : cable visible effiloche ou rouille ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Frein a main qui ne tient plus en cote
  - Course du levier excessive plus de 7 clics
  - Vehicule roule alors frein main
  - Cable visible effiloche ou rouille
  - Bruit de frottement a l arriere en roulant
  - Levier de frein a main mou ou sans resistance
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '124'
  intro_title: A quoi sert Câble de frein à main ?
  risk_title: Pourquoi remplacer Câble de frein à main a temps ?
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
  - question: 'Câble OE ou adaptable : que choisir ?'
    answer: Les câbOES (TRW) ou adaptables (Cofle) sont fiables et moins chers. Vérifiez la longueur exacte et les embouts
      de fixation.
  - question: Comment savoir si mon câble de frein à main est usé ?
    answer: Frein à main qui ne tient plus en côte, course du levier excessive (plus de 7 clics), véhicule qui roule frein
      à main serré.
  - question: Tous les combien changer le câble de frein à main ?
    answer: Pas de périodicité fixe. À remplacer dès que le frein à main ne tient plus correctement malgré le réglage.
  - question: Peut-on changer le câble de frein à main soi-même ?
    answer: Oui, mais accès parfois difficile sous le véhicule. Comptez 1h à 2h. Pensez à régler la tension après montage.
  - question: Quelle erreur éviter avec le câble de frein à main ?
    answer: Ne pas trop tendre le câble neuf (usure prématurée). Graisser la gaine si elle coulisse mal. Vérifier aussi l'état
      des mâchoires.
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
doc_id: 0a9c7baa-2653-59fb-8260-7288cf94d5b6
content_hash: sha256:bdb3c596d7a1c378
lang: fr
variants:
- name: Piece standard
  aliases:
  - standard
  - OE equivalent
  functional_differences:
  - Qualite equivalente a la monte d origine
  - Compatible avec la majorite des vehicules
- name: Piece performance/sport
  aliases:
  - sport
  - haute performance
  functional_differences:
  - Materiaux haute temperature
  - Pour usage intensif ou sportif
location_on_vehicle:
  area: Au niveau des roues (avant et/ou arriere)
  access: Demontage de la roue necessaire (cric + chandelle)
  adjacent_parts:
  - disque
  - plaquette
  - etrier
  - flexible
installation:
  difficulty: moyen
  time: 30min a 1h par essieu
  tools:
  - cle a douille
  - cle Allen
  - pied a coulisse
  - cle dynamometrique
  prerequisite: Vehicule sur chandelles, roue demontee
phase5_enrichment:
  _source: ate-freinage.fr + bremboparts.com + delphiautoparts.com + fr.wikipedia.org + gpa26.com + textar.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 13
  _has_tech_data: true
  types_variants:
  - type: 'hydraulique'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_0_10_mm: '0,10 mm'
    val_0_12_mm: '0,12 mm'
    val_1__v: '1. V'
    val_10_nm: '10 Nm'
    val_10__v: '10. V'
    val_100_a: '100 a'
    val_115_nm: '115 Nm'
    val_125_nm: '125 Nm'
    val_16_nm: '16 Nm'
    val_16_a: '16 a'
    val_18_a: '18 a'
    val_180_nm: '180 Nm'
    val_19_a: '19 a'
    val_2_a: '2 a'
    val_2_mm: '2 mm'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le rôle du câble de frein à main estd''activer ou désactiver le frein de stationnement pour immobiliser le véhiculelorsqu''elle
    est en stationnement. Il bloque une ou plusieurs roues sur un mêmeessieu. Le système du frein destationnement (frein à
    main) à commande mécanique a la fonction d''agir surles mécanismes de frein des roues arrière. Il comprend le levier de
    commande,les câbles de commande, la tringle de commande, le palonnier de frein, lesleviers de commande des segments de
    frein, et aussi le mécanisme de réglageautomatique de l''écartement entre le tambour de frein gauche et droite et le jeu
    de mâchoires de frein. Le frein à main utilise les pièces habituellement utilisées pour lefreinage, disques de frein de
    la voiture ou tambour de frein de la voiture. C''est un simple câble qui permet d''actionner ledispositif situé dans les
    roues arrière. La commande est généralement activéepar une poignée située entre les sièges avant. Il existe aujourd''hui
    denouvelles générations de frein à main à commande au pied ou automatiques. Quelque doit le type de freinage utilisé à
    frein à disque ou frein à tambour, un dispositif automatique est monté sur les roues arrière pourpermettre de maintenir
    une course constante du levier ou de la pédale de freinde stationnement quelque soit l''usure du câble de frein à main.
    En savoir plus : câble de frein à main — définition et rôle mécanique 🚨 Bruit Câble de frein à main : causes et diagnostic'
  S2: 'Uncâble de frein à main défectueux présente plusieurs symptômes : - Le levier de frein à main doit être tiré très fort
    sinon la voiturebouge. - Le levier de frein à main monte tellement qu''il gène lors de ladescente du véhicule. - Une seule
    roue ne bloque pas. Tous les câbles de frein à main sont homologuées par les constructeurs automobile et par les équipementiers
    des pièces détachées automobile. Diagnostic complet : identifier une panne de câble de frein à main'
  S3: 'Avant de commander, vérifiez ces caractéristiques : - Côté concerné : câble gauche, droit ou central (câble principal
    reliant le levier aux deux câbles secondaires) - Longueur totale : varie selon l''empattement du véhicule et le type de
    frein arrière (tambour ou disque) - Type d''embout : embout à clipser, à visser ou à crochet selon le mécanisme de rattrapage
    - Frein de parking intégré à l''étrier : sur les véhicules avec freins arrière à disque, le câble actionne un mécanisme
    dans l''étrier (pas un tambour) Méthode : comparer la longueur et les embouts avec l''ancien câble, ou utiliser le sélecteur
    véhicule pour la référence exacte. ➡️ Trouver les câbles compatibles avec votre véhicule Pour aller plus loin : consultez
    notre guide d''achat câble de frein à main — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: '📖 Avant de démonter, consultez la fiche technique Câble de frein à main pour connaître les spécifications. -
    Dans l''habitacle : démontez le cache du levier de frein à main,Desserrez l''écrou de fixation du câble de frein à main
    et le retirez dusupport. - Levez et calez le véhicule. - Démontez la roue arrière. - Démontez l''étrier de frein gauche
    ou droit ou les mâchoires de frein gauche ou droite suivant l''équipement de votre véhicule. - Retirez le câble de frein
    à main de l''étrier de frein arrière ou des mâchoires de frein arrière. - Démontez toutes les fixations du câble de frein
    à main en dessous duvéhicule. - Retirez le câble de frein à main.'
  S4_REPOSE: 'Remontage du câble de frein à main — procédure complète Avant toute repose, vérifiez que le câble neuf présente
    les mêmes dimensions (longueur, embouts, type de gaine) que le câble déposé. Un câble de longueur incorrecte ne peut pas
    se régler correctement. - Contrôle des pièces associées — Profitez de l''accès pour inspecter l''état des mâchoires de
    frein : une épaisseur de garniture inférieure à 2 mm impose leur remplacement avant le remontage du câble. Vérifiez également
    l''état du tambour de frein (absence de rayures profondes) et de l''étrier de frein arrière (piston non grippé). - Lubrification
    des points de passage — Appliquez une légère couche de graisse silicone (non grasse sur les garnitures) sur chaque guide
    de câble et chaque œillet de passage sous le plancher. Ne jamais graisser la gaine plastique — le câble intérieur doit
    coulisser librement sans lubrifiant sur les garnitures. - Passage du câble sous le véhicule — Engagez le câble dans ses
    guides plastiques et ses colliers de maintien de l''arrière vers l''avant, en vous assurant que chaque clip s''enclenche
    avec un clic franc. Un câble mal guidé frotte contre l''échappement ou le plancher et s''use en quelques semaines. - Connexion
    côté roue — Clipser l''embout du câble dans la came de rattrapage du mécanisme de frein (tambour) ou dans le levier de
    l''étrier (disque avec frein à main mécanique). L''embout doit être parfaitement logé dans son logement ; forcer provoque
    une déformation de la came. - Remontage des mâchoires — Si les mâchoires ont été déposées, les remonter en respectant
    l''orientation primaire/secondaire (la mâchoire primaire, plus courte, est côté avant du tambour). Accrocher les ressorts
    de rappel en s''aidant d''un tournevis à ressort de frein pour éviter toute déformation. - Remontage du tambour — Remettre
    le tambour en place. S''il bloque, vérifier que le réglage du mécanisme de rattrapage est au minimum (mâchoires rapprochées).
    Serrer les vis de retenue du tambour au couple (environ 8 Nm selon véhicule). - Connexion côté habitacle — Passer le câble
    dans son passage étanche sous le plancher, engager l''extrémité dans la chape du levier de frein à main et serrer l''écrou
    de tension à la main dans un premier temps. - Réglage de la tension — Serrer l''écrou de réglage progressivement. Le frein
    à main doit bloquer la roue en tirant le levier entre 3 et 5 clics. Plus de 7 clics indique un câble trop détendu ou des
    mâchoires trop usées. Moins de 2 clics indique un câble surtensionné, risque de freinage résiduel. - Test de fonctionnement
    final — Reposer la roue, descendre le véhicule, serrer les écrous de roue au couple constructeur. Tirer le levier à fond,
    vérifier que la roue est bloquée. Relâcher, vérifier que la roue tourne librement sans frottement résiduel. Effectuer
    un essai routier avec test d''arrêt en côte. ✅ Après remontage, vérifiez les spécifications dans la fiche technique Câble
    de frein à main.'
  S5: '- Confondre câble gauche et câble droit — Sur la plupart des véhicules, le câble de frein à main comprend deux câbles
    secondaires (un par roue) différents en longueur et en courbure selon le côté. Repérer le côté avant démontage (marquage
    gauche/droit ou photo de référence) et commander la bonne référence constructeur. - Ne pas détendre le câble avant dépose
    — Desserrer à fond l''écrou de réglage du levier ou du compensateur avant de déconnecter quoi que ce soit. Un câble sous
    tension libéré brusquement peut endommager la came de rattrapage du mécanisme de tambour ou tordre le levier. Déposer
    d''abord le cache du levier, puis détendre. - Forcer le câble dans les guides de passage — Un câble trop tendu dans son
    guide se déformera, craquera la gaine plastique et grippera après quelques semaines. Lubrifier chaque point de passage
    à la graisse silicone et guider le câble sans forcer, en spiralant légèrement si nécessaire. - Oublier de régler la tension
    après montage — Un câble non réglé peut être trop lâche (frein à main inefficace en côte, levier à plus de 7 clics) ou
    trop tendu (freinage résiduel permanent, surchauffe des tambours, usure prématurée des garnitures). La tension cible est
    un blocage de roue entre 3 et 5 clics. - Réutiliser des clips de maintien de câble cassés — Si les clips plastiques retenant
    le câble sous le plancher sont fissurés ou manquants, le câble vibrera contre la caisse ou frôlera l''échappement, s''usant
    en quelques mois. Remplacer tous les clips de maintien endommagés lors de chaque intervention. - Ne pas contrôler le mécanisme
    de rattrapage dans le tambour — Un rattrapage automatique grippé ou corrodé annule l''efficacité du câble neuf. Avant
    remontage, actionner le mécanisme à la main et vérifier qu''il se déplace sans accroc ; le nettoyer à l''aérosol dégrippant
    si nécessaire. - Ne pas tester le frein à main sur pente réelle — Un réglage sur terrain plat ne garantit pas l''efficacité
    sur une côte à 15-20 %. Effectuer systématiquement un test en côte après montage, moteur coupé, et vérifier que le véhicule
    ne bouge pas. - Ignorer l''état du câble opposé — Les deux câbles travaillent dans les mêmes conditions thermiques et
    mécaniques. Si l''un est usé ou effiloché, l''autre est souvent proche de la rupture. Inspecter les deux câbles et remplacer
    par paire lorsque l''un est défaillant. - Ne pas respecter le couple de serrage de l''écrou de réglage — Un écrou insuffisamment
    serré se desserre par vibrations et fait perdre le réglage. Un écrou sur-serré plastifie le filetage et rend le prochain
    réglage difficile. Serrer au couple constructeur (généralement 8-12 Nm) avec frein- filet si nécessaire. 📖 Fiche technique
    Câble de frein à main — spécifications de réglage constructeur.'
  S6: 'Contrôles statiques - Vérifier la course du levier de frein à main : blocage des roues arrière en 3 à 5 clics - Contrôler
    que le câble ne frotte contre aucun élément mobile (échappement, cardan, bras de suspension) - Vérifier le bon encliquetage
    des embouts aux deux extrémités (levier et mécanisme de frein) - Avec le frein desserré, vérifier que les roues arrière
    tournent librement (aucun freinage résiduel) Essai routier - Rouler à 30 km/h et tirer légèrement le frein à main : le
    véhicule doit ralentir progressivement et droit - Stationner sur une pente montante puis descendante : le véhicule doit
    rester parfaitement immobile - Contrôler après 50 km que les réglages n''ont pas bougé (câble neuf qui s''allonge légèrement)
    ⚠️ Arrêter immédiatement si : le frein à main ne bloque pas les roues, freinage résiduel permanent (roue chaude frein
    desserré), bruit de frottement métallique, câble qui se détend d''un coup. 🚨 Bruit Câble de frein à main : causes et diagnostic'
  S7: Quel est le prix d'un câble de frein à main ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur
    pour trouver le câble de frein à main compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon câble de frein à main est à changer ?Les signes d'usure les plus courants sont détaillés dans la section
    diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un câble de
    frein à main défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule.
    Consultez la section symptômes pour évaluer l'urgence du remplacement.- Étrier de frein. - Kit de freins arrière. 📖 Fiche
    technique Câble de frein à main — intervalles et spécifications d’entretien.
  S8: 'Mon frein à main ne tient plus en côte, est-ce le câble ? Pas nécessairement. Vérifier d''abord le réglage (tension
    du câble). Si le réglage est en butée et que le frein ne tient toujours pas, le câble est probablement étiré ou grippé
    dans sa gaine. Les garnitures de frein usées peuvent aussi être en cause. Faut-il remplacer les deux câbles en même temps
    ? Ce n''est pas obligatoire, mais recommandé. Si un câble a cédé ou est fortement grippé, l''autre a le même âge et la
    même usure. Remplacer les deux garantit un freinage de parking équilibré. Le câble central et les câbles latéraux, quelle
    différence ? Le câble central relie le levier à un répartiteur sous le véhicule. Les câbles latéraux (gauche et droit)
    relient le répartiteur à chaque roue arrière. Certains véhicules n''ont qu''un câble par côté sans répartiteur central.
    Mon frein à main grince quand je le serre, est-ce normal ? Un léger bruit du mécanisme à cliquet est normal. Un grincement
    métallique fort indique un câble grippé dans sa gaine ou un mécanisme de rattrapage corrodé. Lubrifier la gaine ou remplacer
    le câble. Puis-je rouler avec un câble de frein à main cassé ? Techniquement oui, car le frein à main est indépendant
    du circuit hydraulique principal. Mais c''est une infraction au contrôle technique et un danger en stationnement. Le remplacement
    est impératif. 📖 Pour plus de détails techniques : fiche Câble de frein à main'
  META: 'Guide complet pour remplacer votre câble de frein à main : compatibilité, erreurs fréquentes, réglage de la tension
    et FAQ pour un stationnement sûr.'
---

# Câble de frein à main - Guide Diagnostic Complet

## Fonction et Rôle

Transmet la commande du frein de stationnement

**Actions principales:** transmettre, actionner, maintenir

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Frein a main qui ne tient plus en cote**
  frein a main qui ne tient plus en cote
- **Vehicule roule alors frein main**
  vehicule roule alors frein main
- **Levier de frein a main mou ou sans resistance**
  levier de frein a main mou ou sans resistance

### 🟢 Autres Symptômes

- course du levier excessive plus de 7 clics
- cable visible effiloche ou rouille
- bruit de frottement a l arriere en roulant

## Procédure de Diagnostic

Pour diagnostiquer un problème de câble de frein à main:

1. **Inspection visuelle** - Examiner l'état du câble de frein à main
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
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

- capteur-abs
- disque-de-frein
- etrier-de-frein
- interrupteur-des-feux-de-freins
- kit-de-freins-arriere
- machoires-de-frein
- plaquette-de-frein
- tambour-de-frein

## Critères de Compatibilité

Pour commander le bon câble de frein à main, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleur freinage"

## FAQ

**Câble OE ou adaptable : que choisir ?**
Les câbOES (TRW) ou adaptables (Cofle) sont fiables et moins chers. Vérifiez la longueur exacte et les embouts de fixation.

**Comment savoir si mon câble de frein à main est usé ?**
Frein à main qui ne tient plus en côte, course du levier excessive (plus de 7 clics), véhicule qui roule frein à main serré.

**Tous les combien changer le câble de frein à main ?**
Pas de périodicité fixe. À remplacer dès que le frein à main ne tient plus correctement malgré le réglage.

**Peut-on changer le câble de frein à main soi-même ?**
Oui, mais accès parfois difficile sous le véhicule. Comptez 1h à 2h. Pensez à régler la tension après montage.

**Quelle erreur éviter avec le câble de frein à main ?**
Ne pas trop tendre le câble neuf (usure prématurée). Graisser la gaine si elle coulisse mal. Vérifier aussi l'état des mâchoires.
## Types de vibrations

### Vibrations au volant
- **À basse vitesse (< 50 km/h)** : Problème de pneus ou jantes
- **À haute vitesse (> 80 km/h)** : Équilibrage ou géométrie
- **Au freinage** : Disques voilés

### Vibrations dans l'habitacle
- **Moteur au ralenti** : Supports moteur
- **En accélération** : Transmission, cardans
- **À vitesse constante** : Pneus, roulements

### Vibrations dans la pédale de frein
- **Au freinage** : Disques voilés, plaquettes usées

## Causes et solutions

### 1. Pneus déséquilibrés
- **Symptôme** : Vibration volant à partir de 80-100 km/h
- **Vérification** : Visuel sur les masses d'équilibrage
- **Solution** : Équilibrage des 4 pneus
- **Coût** : 40-60€
- **Urgence** : Moyenne

### 2. Pneus usés irrégulièrement
- **Symptôme** : Vibration + bruit de roulement
- **Vérification** : Usure en "dents de scie"
- **Solution** : Remplacement pneus + géométrie
- **Urgence** : Haute

### 3. Roulement de roue défaillant
- **Symptôme** : Grondement augmentant avec la vitesse
- **Vérification** : Jeu dans la roue, bruit en virage
- **Solution** : Remplacement roulement
- **Pièces** : Kit roulement de roue
- **Urgence** : Haute - Sécurité

### 4. Cardans usés
- **Symptôme** : Claquement en braquant, vibration en accélération
- **Vérification** : Soufflets déchirés, jeu
- **Solution** : Remplacement cardan
- **Pièces** : Cardan complet ou transmission
- **Urgence** : Haute

### 5. Disques de frein voilés
- **Symptôme** : Vibration pédale au freinage
- **Vérification** : Mesure au comparateur
- **Solution** : Rectification ou remplacement
- **Pièces** : Disques de frein
- **Urgence** : Moyenne

### 6. Supports moteur fatigués
- **Symptôme** : Vibration au ralenti dans l'habitacle
- **Vérification** : Visuel sur silent-blocs
- **Solution** : Remplacement supports
- **Pièces** : Support moteur, silent-bloc
- **Urgence** : Basse
## Symptômes courants

### Grincement aigu au freinage
- **Quand** : Au moment du freinage léger ou modéré
- **Caractéristique** : Son métallique aigu, type "crissement"

### Sifflement continu
- **Quand** : Pendant tout le freinage
- **Caractéristique** : Son aigu constant

### Bruit sourd / grondement
- **Quand** : Freinage appuyé
- **Caractéristique** : Vibration ressentie dans la pédale

### Claquement
- **Quand** : Début ou fin de freinage
- **Caractéristique** : Bruit sec, ponctuel

## Causes possibles et solutions

### 1. Plaquettes de frein usées
- **Probabilité** : 70%
- **Vérification** : Témoin usure allumé, épaisseur < 3mm
- **Solution** : Remplacement des plaquettes
- **Pièces** : Plaquettes de frein avant/arrière
- **Urgence** : Haute - Sécurité

### 2. Disques de frein voilés
- **Probabilité** : 15%
- **Vérification** : Vibration pédale, usure inégale visible
- **Solution** : Rectification ou remplacement des disques
- **Pièces** : Disques de frein
- **Urgence** : Moyenne

### 3. Étrier grippé
- **Probabilité** : 10%
- **Vérification** : Usure asymétrique des plaquettes
- **Solution** : Nettoyage/graissage ou remplacement étrier
- **Pièces** : Kit réparation étrier, étrier complet
- **Urgence** : Haute

### 4. Absence de graisse sur glissières
- **Probabilité** : 5%
- **Vérification** : Plaquettes difficiles à bouger
- **Solution** : Nettoyage et graissage
- **Pièces** : Graisse haute température
- **Urgence** : Basse

## Questions complémentaires pour affiner le diagnostic

1. Le bruit apparaît-il à froid ou à chaud ?
2. Le bruit est-il présent sur les 4 roues ou localisé ?
3. Y a-t-il une vibration dans le volant ?
4. Quand avez-vous changé vos plaquettes pour la dernière fois ?
5. Avez-vous un témoin d'usure allumé au tableau de bord ?

## Recommandations

- **Contrôle visuel** : Vérifier l'épaisseur des plaquettes (minimum 3mm)
- **Kilométrage** : Remplacement préventif tous les 30 000 - 50 000 km
- **Qualité** : Privilégier les marques équipementier (Bosch, Brembo, TRW)
