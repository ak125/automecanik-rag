---
category: accessoires
slug: pompe-nettoyage-des-vitres
title: Pompe nettoyage des vitres
pg_id: 794
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-04-04'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:materialize-db-to-md
  last_enriched_at: '2026-04-04'
  v5_migrated_at: '2026-03-29'
domain:
  role: Projette le liquide lave-glace sur le pare-brise
  must_be_true:
  - projeter
  - pulveriser
  - alimenter
  must_not_contain:
  - balai
  - moteur essuie-glace
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - projeter
  - pulveriser
  - alimenter
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
  - ❌ "visibilite parfaite"
  cost_range:
    min: 50
    max: 300
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE
  - tier: Adaptable — entree de gamme
  brands:
    premium:
    - Bosch
    - Valeo
    standard:
    - SWF
    - Hella
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Jet de lave-glace absent
    severity: securite
  - id: S2
    label: Pompe qui fait du bruit sans projeter
    severity: confort
  - id: S3
    label: Jet faible malgre reservoir plein
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : jet de lave-glace absent'
  quick_checks:
  - 'Observer : jet de lave-glace absent ?'
  - 'Observer : pompe qui fait du bruit sans projeter ?'
  - 'Observer : jet faible malgre reservoir plein ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Jet de lave-glace absent
  - Pompe qui fait du bruit sans projeter
  - Jet faible malgre reservoir plein
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '794'
  intro_title: A quoi sert Pompe nettoyage des vitres ?
  risk_title: Pourquoi remplacer Pompe nettoyage des vitres a temps ?
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
  - question: Comment choisir Pompe nettoyage des vitres compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Pompe nettoyage des vitres ?
    answer: En cas de jet de lave-glace absent ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Pompe nettoyage des vitres sans verification atelier ?
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
doc_id: c7cdf102-78e7-54cd-a261-e9d37325412a
content_hash: sha256:fb3601f9429d3283
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
  _enriched_at: '2026-04-04'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: Hydraulique
    source_ref: corpus RAG web OEM
  - type: hydraulique
    source_ref: corpus RAG web OEM
  - type: organique
    source_ref: corpus RAG web OEM
  technical_notes:
    val_10_mm: 10 mm
    val_100_bar: 100 bar
    val_100__c: 100 °C
    val_14_a: 14 a
    val_15_a: 15 a
    val_2_a: 2 a
    val_300_bars: 300 bars
    val_320_bar: 320 bar
    val_800_mm: 800 mm
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'La pompe de nettoyage des vitres est le composant motorisé qui projette le liquide lave-glace sous pression vers le
    pare-brise et, selon l''équipement du véhicule, vers la lunette arrière. Elle est immergée dans le réservoir de liquide
    lave-glace et entraîne le fluide jusqu''aux gicleurs par l''intermédiaire de durites dédiées. Son activation est commandée
    par le levier multifonctions du conducteur ou automatiquement par certains systèmes de détection de pluie couplés à la
    vitesse d''essuie-glace. La pompe remplit trois fonctions mécaniques essentielles : aspirer le liquide depuis le fond
    du réservoir, le mettre sous pression pour lui donner un débit suffisant à travers les gicleurs et finalement le pulvériser
    de manière régulière sur la surface vitrée. Sur les véhicules modernes, la pompe gère souvent deux circuits distincts
    (avant et arrière) par deux moteurs électriques séparés ou par un moteur unique à deux sorties. Un pare-brise propre est
    directement lié à la sécurité active : selon les études de visibilité routière, un pare- brise encrassé réduit de 20 à
    30 % la visibilité effective en conduite de nuit et par temps de pluie. La pompe lave-glace est donc un composant de sécurité
    à ne pas négliger, même si sa défaillance n''allume aucun voyant d''alarme sur la plupart des véhicules. Les pièces associées
    à inspecter lors d''un remplacement incluent le bras d''essuie-glace, la commande d''essuie- glace et le moteur d''essuie-glace,
    qui collaborent avec la pompe dans le système de nettoyage global.'
  S2: 'La pompe lave-glace se dégrade progressivement ou tombe en panne sèche. Dans les deux cas, des signaux avant-coureurs
    permettent d''anticiper le remplacement. Le symptôme le plus grave — l''absence totale de jet — constitue un problème
    de sécurité directe puisqu''il empêche de nettoyer le pare-brise en roulant. - Jet de lave-glace totalement absent (symptôme
    de sécurité) : aucun liquide ne jaillit des gicleurs lors de l''activation ; la pompe est soit grillée, soit alimentée
    en courant mais le moteur interne est bloqué. - Pompe qui fait du bruit sans projeter : le bourdonnement caractéristique
    de la pompe est audible mais aucun jet n''apparaît ; cela indique un moteur qui tourne dans le vide, signe d''une membrane
    déchirée ou d''une durite débranchée. - Jet faible malgré un réservoir plein : la pression de sortie est insuffisante
    pour décoller les salissures du pare- brise ; cause probable : usure des joints internes de la pompe ou obstruction partielle
    d''un gicleur. - Jet uniquement en avant ou uniquement en arrière : sur les pompes bi-circuits, la défaillance d''un moteur
    laisse fonctionner l''autre ; distinguer ainsi une panne partielle d''une panne totale. - Fuites au bas du réservoir :
    des traces de liquide bleu ou vert sous le véhicule côté avant signalent un joint de pompe percé ou une durite desserrée
    à la sortie de la pompe. - Activation intermittente et aléatoire : la pompe fonctionne seulement par intermittence, souvent
    révélateur d''un connecteur électrique dont les broches sont oxydées ou d''un câblage partiellement coupé. - Gel de la
    pompe en hiver : si du liquide non antigel a été utilisé, la pompe peut se bloquer définitivement après un gel ; elle
    se débloque rarement spontanément et nécessite un remplacement.'
  S3: 'Toutes les pompes lave-glace ne sont pas interchangeables. Le diamètre du puit dans le réservoir, le nombre de sorties,
    le brochage électrique et la pression nominale varient selon les constructeurs et même selon les générations d''un même
    modèle. Voici comment sélectionner la bonne pièce. - Identifier marque, modèle et année de production : ce triptyque est
    le point de départ indispensable ; une erreur sur l''année peut conduire à commander une pompe avec un connecteur incompatible.
    - Déterminer le type de circuit : votre véhicule dispose-t-il d''un lave-glace arrière ? Si oui, la pompe doit avoir deux
    sorties (avant + arrière) ; une pompe à sortie unique ne peut pas être adaptée sans modifier le câblage. - Vérifier les
    symptômes avant de commander : si le jet est faible, vérifier d''abord les gicleurs (souvent bouchés par le calcaire)
    avant de conclure à une pompe défaillante ; si la pompe fait du bruit sans projeter, la pompe est à remplacer. - Privilégier
    les équipementiers référencés : des marques comme Valeo, Bosch, Hella ou Febi proposent des pompes conformes aux spécifications
    OEM avec des connecteurs identiques à l''origine. - Contrôler le nombre de broches du connecteur : 2 broches pour une
    pompe simple, 3 ou 4 broches pour les pompes avec circuit double ou capteur de niveau intégré. - Vérifier si la pompe
    inclut le joint torique : le joint d''étanchéité entre la pompe et le réservoir doit être remplacé systématiquement ;
    certaines pompes aftermarket le fournissent, d''autres non. - Inspecter les pièces adjacentes : lors de la commande, vérifier
    l''état du bras d''essuie-glace et de la commande d''essuie- glace pour n''avoir qu''une seule intervention sur le circuit
    de nettoyage. Pour aller plus loin : consultez notre guide d''achat pompe nettoyage des vitres — comparatif marques, critères
    de choix et prix.'
  S4_DEPOSE: 'Le remplacement d''une pompe lave-glace est une opération accessible à un bricoleur averti disposant de l''outillage
    de base. L''accès au réservoir peut nécessiter le démontage partiel d''un passage de roue avant selon les modèles. Prévoir
    environ 30 à 60 minutes pour l''ensemble de l''opération. - Déconnecter la batterie : débrancher le câble négatif de la
    batterie avant toute intervention électrique pour protéger le circuit de commande de la pompe. - Localiser le réservoir
    lave-glace : généralement visible dans le compartiment moteur côté conducteur ou passager ; sur certains véhicules, le
    réservoir est partiellement caché derrière un cache de passage de roue avant. - Vider partiellement le réservoir : aspirer
    le liquide jusqu''à ce que le niveau soit inférieur à la hauteur de la pompe ; évite les écoulements lors de l''extraction.
    - Repérer les durites et connecteurs : photographier avant démontage la disposition des durites (avant, arrière, capteur
    de niveau) pour retrouver la configuration exacte lors du remontage. - Débrancher le connecteur électrique : appuyer sur
    le clip de verrouillage et dégager le connecteur ; vérifier visuellement l''état des broches. - Débrancher les durites
    : noter leur couleur ou position, puis retirer les durites en tirant sans forcer ; obturer les extrémités avec des doigts
    de gant ou des bouchons plastique pour contenir le liquide résiduel. - Extraire la pompe : selon les véhicules, tourner
    d''un quart de tour et tirer (système baïonnette) ou dégager les clips de rétention puis tirer perpendiculairement au
    réservoir ; récupérer le joint torique usagé. - Monter la nouvelle pompe : lubrifier légèrement le joint torique neuf
    avec du liquide lave-glace, insérer la pompe, reconnecter les durites dans l''ordre noté, puis encliquer le connecteur
    électrique. - Remplir le réservoir et tester : rebrancher la batterie, remplir le réservoir, et déclencher plusieurs cycles
    avant/arrière pour purger l''air et vérifier la projection.'
  S4_REPOSE: 'Après remplacement de la pompe lave-vitre, le remontage doit rétablir un circuit hydraulique totalement étanche
    avec des gicleurs correctement orientés. Une mauvaise installation se traduit par un jet absent, faible ou mal dirigé.
    - Inspection du réservoir de lave-glace — Avant de poser la nouvelle pompe, nettoyez l''intérieur du réservoir pour éliminer
    les dépôts de calcaire ou de produit vieux. Un réservoir encrassé colmate rapidement la nouvelle pompe. - Insertion de
    la pompe dans le réservoir — La pompe lave- vitre est généralement clipsée dans un orifice dédié du réservoir avec un
    joint torique. Lubrifiez légèrement le joint avec de l''eau pour faciliter l''insertion sans déformation. Enfoncez jusqu''au
    déclic de verrouillage. - Reconnexion de la durite de sortie — Branchez la durite principale allant vers les gicleurs
    de pare-brise. Vérifiez que la durite n''est pas pincée sous le capot ou dans les passages de carrosserie. Un étranglement
    partiel réduit le débit. - Reconnexion du connecteur électrique — Branchez le connecteur de la pompe jusqu''au clic. Vérifiez
    que le câblage n''est pas tendu ou en contact avec des arêtes tranchantes de tôle. - Remplissage du réservoir — Remplissez
    avec un liquide lave-glace dilué adapté à la saison (antigel concentré dilué selon température). La quantité typique est
    de 2 à 5 litres selon le réservoir. Ne pas utiliser d''eau pure : corrosion de la pompe et risque de gel. - Test de projection
    avant et arrière — Activez le lave-glace avant, puis arrière si votre véhicule en dispose. Le jet doit atteindre le bas
    du pare-brise dans la zone de balayage des essuie-glaces. Un jet qui ne monte pas assez ou qui projette trop loin est
    à régler. - Réglage des gicleurs — Utilisez une aiguille fine pour orienter délicatement les embouts des gicleurs. Position
    idéale : jet atteignant le centre du pare-brise, légèrement vers le haut pour couvrir la zone de balayage complète à 100
    km/h. - Contrôle d''absence de fuite — Après 3 à 4 cycles d''activation, vérifiez l''absence de fuite au niveau de la
    pompe dans le réservoir et sur tous les raccords de durite. Remarque : si le véhicule dispose d''un chauffage de gicleur
    (résistance intégrée dans le gicleur), assurez-vous que les connecteurs de chauffage sont branchés pour éviter le gel
    des gicleurs en hiver.'
  S5: 'Le remplacement d''une pompe lave-glace peut sembler simple, mais plusieurs erreurs fréquentes aboutissent à une reprise
    d''intervention ou à une panne persistante. Les voici avec leurs conséquences concrètes. - Intervertir les durites avant
    et arrière : sur une pompe bi-circuits, rebrancher les durites à l''envers envoie le jet vers l''arrière quand on commande
    l''avant et inversement ; une inspection visuelle avec le schéma constructeur suffit à éviter cela. - Oublier de vider
    le réservoir avant démontage : extraire la pompe avec le réservoir plein déclenche un flot de liquide dans le compartiment
    moteur, pouvant atteindre des connecteurs électriques sensibles et provoquer des courts-circuits. - Utiliser de l''eau
    du robinet pour remplir après l''intervention : l''eau calcaire colmate les gicleurs en quelques semaines et détériore
    les joints de la pompe neuve ; toujours utiliser du liquide lave-glace concentré dilué selon les préconisations. - Réutiliser
    le joint torique d''origine : un joint déformé ne garantit plus l''étanchéité ; il faut absolument le remplacer avec la
    nouvelle pompe, même si le joint semble en bon état visuel. - Ne pas tester les deux circuits après montage : sur une
    pompe double, tester uniquement le circuit avant et négliger l''arrière peut masquer une durite arrière mal reconnectée
    qui fuira ensuite dans le coffre ou sous le véhicule.'
  S6: 'Le remplacement de la pompe lave-glace doit être suivi d''une série de contrôles fonctionnels et visuels pour valider
    l''intervention et s''assurer qu''aucune fuite ou dysfonctionnement ne subsiste. - Activer le lave-glace avant plusieurs
    fois de suite : les premiers cycles purgent l''air emprisonné dans les durites ; un jet irrégulier ou hésitant lors des
    premiers déclenchements est normal et disparaît après 3 à 5 cycles. - Tester le circuit arrière si équipé : déclencher
    séparément le lave-glace arrière et vérifier que le jet atteint correctement la lunette. - Contrôler l''étanchéité de
    la base de pompe : après 10 cycles de fonctionnement, inspecter le réservoir et le puit de pompe pour détecter toute fuite
    de liquide sur le joint torique. - Vérifier l''orientation des gicleurs : les gicleurs peuvent avoir été déplacés lors
    du remontage ; s''assurer qu''ils arrosent le centre du pare-brise dans la zone balayée par les essuie-glaces. - Contrôler
    le niveau du réservoir : compléter si nécessaire ; noter que les durites contiennent du liquide résiduel qui peut temporairement
    réduire le niveau apparent dans le réservoir. - Vérifier la solidité du connecteur électrique : tirer doucement sur le
    câble pour confirmer que le clip de verrouillage est bien enclenché.'
  S7: La pompe lave-vitre agit en lien direct avec les éléments du système d'essuyage. Un dysfonctionnement d'un composant
    adjacent peut simuler ou aggraver une défaillance de pompe. Inspectez ces pièces lors de l'intervention. - Moteur d'essuie-glace
    — Le moteur des essuie-glaces est souvent actionné simultanément au jet de lave-glace. Si le moteur ne fonctionne pas,
    le liquide projeté reste sur le pare-brise sans être essuyé. Vérifiez son état si l'essuie-glace est inactif ou grippé.
    - Bras d'essuie- glace — Un bras desserré ou tordu déplace le balai hors de sa zone normale d'essuyage. La pression insuffisante
    du bras sur le pare-brise rend l'essuyage inefficace même avec un jet de liquide correct. - Commande d'essuie-glace —
    La commande (combiné au volant) pilote simultanément le moteur et la pompe. Si le jet fonctionne mais sans essuie-glace,
    la panne peut venir du contacteur de commande ou de son câblage. - Gicleurs de lave- glace — Les gicleurs (buses) se bouchent
    régulièrement par le calcaire ou les impuretés du liquide. Un gicleur bouché sur un côté crée un jet asymétrique sans
    que la pompe soit défaillante. Nettoyez à l'aiguille fine ou remplacez. - Durites de distribution de liquide — Relient
    la pompe aux gicleurs avant et arrière. Une durite coupée, pincée ou décrochée d'un raccord provoque un jet absent sur
    l'un des côtés uniquement. Si votre véhicule dispose d'un système lave-phares utilisant le même réservoir, assurez-vous
    que la pompe commandée correspond au bon orifice (lave-vitre ou lave-phares, souvent distingués par un nombre de broches
    différent sur le connecteur).
  S8: 'Pourquoi ma pompe lave-glace fait-elle du bruit mais ne projette rien ? Ce symptôme indique que le moteur électrique
    de la pompe tourne mais que le fluide ne circule pas. Les causes les plus fréquentes sont : une membrane interne déchirée
    (la pompe ne crée plus de dépression), une durite débranchée ou percée entre la pompe et les gicleurs, ou encore le réservoir
    vide que la pompe aspire à sec. Vérifier d''abord le niveau du réservoir, puis inspecter les durites, et si aucune de
    ces causes n''est identifiée, la pompe est à remplacer. Puis-je utiliser de l''eau claire à la place du liquide lave-glace
    dans le réservoir ? L''eau claire peut dépanner ponctuellement par temps chaud, mais elle est déconseillée à l''usage
    régulier pour plusieurs raisons : elle ne contient pas de dégraissants efficaces pour les insectes et résidus routiers,
    elle gèle en dessous de 0 °C et peut éclater le réservoir ou bloquer définitivement la pompe, et son calcaire colmate
    progressivement les gicleurs et détériore les joints internes de la pompe. Utiliser exclusivement du liquide lave-glace
    formulé, dilué selon les températures locales. Comment savoir si c''est la pompe ou les gicleurs qui sont défaillants
    ? Pour distinguer les deux composants : débrancher une durite directement à la sortie de la pompe (avant le premier raccord),
    déclencher la pompe et vérifier si du liquide sort sous pression. Si oui, la pompe fonctionne et le problème se situe
    en aval (durite bouchée ou gicleur colmaté, à nettoyer à l''aiguille ou au compresseur). Si aucun débit ne sort même après
    avoir débranché la durite, la pompe est défaillante. La pompe lave-glace peut-elle être réparée ou faut-il systématiquement
    la remplacer ? Ces pompes ne sont généralement pas réparables, car les pièces internes (membrane, rotor, joints) ne sont
    pas commercialisées séparément et leur remplacement nécessiterait un démontage complet de la pompe et un outillage spécialisé.
    Le coût du remplacement d''une pompe complète est suffisamment faible pour que la réparation ne soit économiquement pas
    justifiable dans la grande majorité des cas. La pompe lave-glace fonctionne-t-elle avec n''importe quel liquide lave-glace
    ? Oui, pour autant que le liquide soit adapté à un usage automobile et utilisé à la bonne concentration. Éviter les produits
    ménagers (liquide vaisselle) qui moussent excessivement, bouchent les gicleurs et détériorent les joints de pompe. En
    été, une dilution à 30 % de concentré est suffisante ; en hiver dans les régions froides, monter jusqu''à 50 % pour une
    protection jusqu''à -20 °C.'
  META: '{"meta_title":"Pompe lave-glace : jet absent ou faible ? Guide | AutoMecanik","meta_description":"Jet de lave-glace
    absent ou pompe qui fait du bruit sans projeter ? Ce guide explique quand remplacer la pompe nettoyage des vitres et comment
    choisir la bonne pièce.","meta_title_length" :57,"meta_description_length":154,"primary_intent":"diagnostic","target_symp
    toms":["jet de lave-glace absent","pompe qui fait du bruit sans projeter","jet faible malgre reservoir plein"],"category":"accessoires"}'
---

# Pompe nettoyage des vitres - Guide Diagnostic Complet

## Fonction et Rôle

Projette le liquide lave-glace sur le pare-brise

**Actions principales:** projeter, pulveriser, alimenter

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Jet de lave-glace absent**
  jet de lave-glace absent

### 🟢 Autres Symptômes

- pompe qui fait du bruit sans projeter
- jet faible malgre reservoir plein

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe nettoyage des vitres:

1. **Inspection visuelle** - Examiner l'état du pompe nettoyage des vitres
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

- bras-d-essuie-glace
- commande-d-essuie-glace
- moteur-d-essuie-glace

## Critères de Compatibilité

Pour commander le bon pompe nettoyage des vitres, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "visibilite parfaite"

## FAQ

**Comment choisir Pompe nettoyage des vitres compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Pompe nettoyage des vitres ?**
En cas de jet de lave-glace absent ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Pompe nettoyage des vitres sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
