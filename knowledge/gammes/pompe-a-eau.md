---
category: distribution
slug: pompe-a-eau
title: Pompe à eau
pg_id: 1260
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
  role: Faire circuler le liquide de refroidissement dans le circuit moteur
  must_be_true:
  - faire circuler
  - pomper
  - alimenter
  must_not_contain:
  - huile
  - carburant
  - direction
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - courroie-de-distribution
  - kit-de-distribution
  - galet-tendeur-de-courroie-de-distribution
  - galet-enrouleur-de-courroie-de-distribution
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
  - ❌ "evite la casse moteur"
  cost_range:
    min: 20
    max: 130
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
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
    label: Fuite de liquide au niveau de la pompe
    severity: confort
  - id: S2
    label: Bruit de roulement cote distribution
    severity: confort
  - id: S3
    label: Jeu perceptible dans la poulie de pompe
    severity: confort
  - id: S4
    label: Surchauffe moteur malgre niveau correct
    severity: confort
  - id: S5
    label: Odeur de liquide de refroidissement chaud
    severity: confort
  - id: S6
    label: Echeance distribution approche preventif
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  quick_checks:
  - Fuite de liquide au niveau de la pompe ?
  - Bruit de roulement cote distribution ?
  - 'Observer : jeu perceptible dans la poulie de pompe ?'
  - 'Observer : surchauffe moteur malgre niveau correct ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Fuite de liquide au niveau de la pompe
  - Bruit de roulement cote distribution
  - Jeu perceptible dans la poulie de pompe
  - Surchauffe moteur malgre niveau correct
  - Odeur de liquide de refroidissement chaud
  - Echeance distribution approche preventif
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '1260'
  intro_title: A quoi sert Pompe à eau ?
  risk_title: Pourquoi remplacer Pompe à eau a temps ?
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
  - question: Pompe à eau OE ou adaptable ?
    answer: Privilégiez l'OES (SKF, FAG, INA, Gates) pour une durée de vie garantie jusqu'à la prochaine distribution. Les
      adaptables sont risqués sur cette pièce critique.
  - question: Comment savoir si ma pompe à eau fuit ?
    answer: Fuite visible sous la pompe, bruit de roulement (grognement), jeu dans l'axe, traces de calcaire autour de la
      pompe, surchauffe moteur.
  - question: Tous les combien changer la pompe à eau ?
    answer: 'Avec la distribution : 80 000 à 120 000 km. Sinon, pas de périodicité fixe mais contrôle à chaque distribution.'
  - question: Peut-on changer la pompe à eau soi-même ?
    answer: Possible si accessible, mais souvent liée à la distribution. Nécessite vidange du circuit et purge soignée après
      montage.
  - question: Quelle erreur éviter avec la pompe à eau ?
    answer: Ne pas monter une pompe sans changer le joint. Vérifier le sens de rotation de la turbine. Purger correctement
      le circuit après.
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
doc_id: bf27168c-fddd-558d-96a2-f2363970e213
content_hash: sha256:6087d334eb8d426c
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
  _source: automotive.hutchinson.com + fr.wikipedia.org + hella.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 4
  _has_tech_data: true
  types_variants:
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    norme_iso_9981: 'ISO 9981'
    val_000_km: '000 km'
    val_1_5_bars: '1,5 bars'
    val_120__c: '120 °C'
    val_135__c: '135 °C'
    val_3_bars: '3 bars'
    val_360_v: '360 V'
    val_95__c: '95 °C'
  materials:
  - materiau: 'aluminium'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'La pompe à eau fait circulerle liquide derefroidissement au sein dumoteur par la rotation de sa poulie si elle est
    entraînée par lacourroie d''accessoires. Et si la pompe à eau à une roue dentée, elles sera entraînée par la courroie
    de distribution . La combustion du moteur produit de très fortes chaleurs quifait augmenter la température des pièces
    mécanique, qu''ils seront refroidis grâceau circuit de refroidissement moteur. Le circuit de refroidissement est composé
    d''un radiateurde refroidissement, d''une pompe à eau, d''un thermostat etd''un ventilateur de refroidissement à travers
    lesquels circule le liquide de refroidissement.La pompe à eau fait circuler le liquide de refroidissement dans cesystème.
    En savoir plus : pompe à eau — définition et rôle mécanique 🚨 Voyant pompe à eau allum'
  S2: 'La pompe à eau n''a pas de période de remplacement, mais elledoit être remplacée dès que vous constatez les symptômes
    suivants : - Fuites de liquide derefroidissement au niveau de la pompe à eau. - Bruits au niveau de la pompeà eau. - Poulie
    grippé, remplacementuniquement de la poulie si il n''y a pas de fuite de la pompe à eau. Si la pompe à eau défaillante
    n''est pas remplacée, lerefroidissement du moteur ne sera plus assurée ce qui va produire unesurchauffe du moteur (joint
    de culasse à long terme casse moteur). Lorsque lapompe à eau est entraînée par la courroie de distribution , la casse
    de la pompeà eau peut entraîner la rupture de la courroie de distribution ce qui vaprovoquer une casse moteur c''est pour
    cela qu''il faut toujours remplacerla pompe à eau avec le kit de distribution et vis versa. Diagnostic complet : identifier
    une panne de pompe à eau'
  S2_DIAG: SymptômeCause probableActionUn bruit anormal au niveau du pompe à eau peut se manifester lors de la phase "acceleration"Pour
    identifier ce probleme de bruit du pompe à eau:Verification visuelle du pompe à eauDes vibrations provenant du pompe à
    eau sont souvent perceptibles a haute vitessePour identifier ce probleme de vibration du pompe à eau:Verification visuelle
    du pompe à eau
  S3: 'La pompe à eau entraîne la circulation du liquide de refroidissement dans le circuit moteur, maintenant la température
    dans la plage de fonctionnement normale (85 à 95 °C). Sur la majorité des véhicules modernes, la pompe à eau est entraînée
    par la courroie de distribution et doit être remplacée systématiquement lors de chaque révision de la distribution, tous
    les 120 000 à 200 000 km selon le constructeur. Choisir une pompe dimensionnellement et hydrauliquement correcte est indispensable
    pour éviter une surchauffe entraînant la déformation de la culasse. - Entraînement : courroie de distribution, courroie
    accessoire ou chaîne — La pompe à eau peut être entraînée par la courroie de distribution (remplacement simultané obligatoire),
    par la courroie d''accessoires (remplacement indépendant possible) ou par la chaîne de distribution (durée de vie moteur,
    remplacement rare). Identifier le type d''entraînement avant de commander. - Matériau de la turbine : métal ou plastique
    — Les pompes récentes utilisent des turbines en plastique renforcé pour réduire le poids et le bruit. Si la turbine d''origine
    est en métal, ne pas la remplacer par une pompe à turbine plastique générique : le plastique peut se désolidariser de
    l''axe à haute température, stoppant net la circulation sans bruit d''alerte. - Débit hydraulique et dimension de la turbine
    — Le débit de la pompe (en L/min) doit correspondre au circuit du constructeur. Une pompe sous-débitante ne compense pas
    la chaleur à régime élevé ou avec la climatisation en fonctionnement. Vérifier que le diamètre de la turbine et le nombre
    d''ailettes correspondent à la référence d''origine. - Joint d''étanchéité inclus — La pompe à eau est livrée avec ou
    sans joint de carter. Vérifier si le joint de logement de la pompe est inclus dans la livraison. Monter une pompe neuve
    sans remplacer le joint de carter est une source de fuite dès la mise en service. - Kit complet distribution + pompe —
    Les fabricants (SKF, INA, Dayco, Continental, Gates) proposent des kits intégrant courroie de distribution, galets tendeurs
    et pompe à eau. Opter pour un kit d''un seul fournisseur garantit la cohérence des cotes et un seul interlocuteur en cas
    de réclamation. - Pièces liées à contrôler — Lors du remplacement, inspecter systématiquement les durites de refroidissement
    (durcissement, fissures), le thermostat (jeu de l''obturateur) et le bouchon du vase d''expansion (pression de tarage
    entre 1,0 et 1,4 bar). Ces pièces sont accessibles lors du démontage de la distribution. - Marque, modèle, année et code
    moteur — Indispensable : le code moteur détermine la référence exacte de la pompe, sa bride de fixation et le type d''entraînement.
    Un même modèle de voiture peut avoir reçu plusieurs motorisations avec des pompes totalement différentes selon la cylindrée
    ou la puissance.'
  S4_DEPOSE: '📖 Avant de démonter, consultez la fiche technique Pompe à eau pour connaître les spécifications. - Débranchez
    la batterie. - Levez et calez le véhicule. - Démontez la roue avant droite. - Démontez le pare-boue avant droit. - Vidangez
    le circuit derefroidissement à travers la ou les vis de vidange du moteur. Note : une vis de vidange du liquide derefroidissement
    se trouve sur le côté du bloc moteur et/ou en bas du radiateur.S''il n''y a pas de vis de vidange sur votre moteur démontez
    la durite inférieuredu radiateur de refroidissement en positionnant le bac à vidange en dessous pour récupérer leliquide
    de refroidissement. - Repérez le cheminement de la courroie d''accessoires. - Démontez la courroie d''accessoires. - Démontez
    la courroie de distribution (si entraînée par ladistribution). - Démontez les durites de liquide de refroidissement de
    la pompe à eau. - Desserrez les fixations de la pompe à eau. - Démontez la pompe à eau.'
  S4_REPOSE: '- Vérifier que la pompe à eau neuve estidentique à celle démontée. - Contrôler l''état de la courroied''accessoires,
    remplacée si nécessaire. - Remplacez obligatoirement lekit de distribution si la courroie de distribution entraîne la
    pompe à eau. - Remplacez les joints d''étanchéité de la pompe à eau. - Graissez la nouvelle pompe à eau. - Remontez la
    pompe à eau. - Serrez les fixations de la pompe à eau. - Remontez les canalisations sur la pompe à eau. - Remontez la
    courroie de distribution (si entraînée par ladistribution). - Remontez la courroie d''accessoires. - Remontez l''écran
    pare-boue et la roue. - Remplissez et purgez le liquide de refroidissement. - Desserrez la vis de purge du circuit de
    refroidissementpour chasser l''air du circuit. - Refermez la vis de purge. - Démarrez le moteur. - Laissez tourner le
    moteur au ralenti. - Contrôlez la température sur le tableau de bord. - Arrêtez le moteur. - Laissez refroidir le moteur.
    - Contrôlez le niveau du liquide de refroidissement. - Complétez le niveau du liquide de refroidissement sinécessaire.
    ✅ Après remontage, vérifiez les spécifications dans la fiche technique Pompe à eau.'
  S5: 'Erreurs frequentes avec la pompe a eau : - Ignorer une fuite de liquide de refroidissement au niveau de la pompe —
    meme legere, elle s''aggrave et provoque une surchauffe moteur- Ne pas remplacer la pompe a eau lors du changement du
    kit de distribution — si la pompe est entrainee par la courroie de distribution, elle sera inaccessible jusqu''au prochain
    remplacement (60 000 a 120 000 km)- Negliger un bruit de roulement cote pompe a eau — signe que le roulement interne est
    use, la rupture est imminente- Reutiliser l''ancien joint de pompe — le joint d''etancheite doit etre neuf a chaque remplacement
    pour eviter les fuites- Ne pas purger correctement le circuit de refroidissement apres remplacement — une bulle d''air
    provoque des points chauds et un chauffage habitacle defaillant- Oublier de verifier l''etat de la courroie et des galets
    lors du remplacement de la pompe — une courroie usee endommage la pompe neuve'
  S6: 'La pompe à eau assure la circulation du liquide de refroidissement dans l''ensemble du circuit moteur. Après son remplacement
    — souvent effectué conjointement avec la courroie ou la chaîne de distribution — des contrôles d''étanchéité et de température
    sont indispensables avant de valider l''intervention. - Purge complète du circuit de refroidissement : après remplissage
    du vase d''expansion, démarrer le moteur avec le bouchon de purge ouvert (si présent) ou le couvercle du vase légèrement
    desserré. Laisser le moteur tourner jusqu''à ouverture du thermostat (70 à 85 °C selon véhicule) et compléter le niveau
    en éliminant toutes les poches d''air. Un circuit mal purgé provoque une surchauffe localisée malgré un niveau correct.
    - Absence de fuite au joint de bride de pompe : à température de fonctionnement stabilisée, inspecter la bride de la pompe
    sous tous les angles avec une lampe. Toute suintement de liquide rose, bleu ou vert au niveau des vis de fixation ou du
    joint d''étanchéité indique un serrage insuffisant (couple standard : 8 à 12 N·m sur la plupart des moteurs) ou un joint
    mal positionné. - Température moteur stable entre 88 et 95 °C : surveiller le témoin de température ou le capteur sur
    outil de diagnostic pendant les 10 premières minutes de chauffe. Une montée au-delà de 100 °C alors que le niveau est
    correct pointe vers une pompe dont les ailettes tournent dans le mauvais sens (erreur d''installation sur pompe à entraînement
    électrique) ou un air résiduel dans le circuit. - Absence de jeu axial ou radial dans la poulie de pompe : moteur éteint
    et refroidi, saisir la poulie et tenter un mouvement latéral puis axial. Le jeu tolérable est nul — tout jeu perceptible
    indique un roulement de pompe mal serré ou un défaut de fabrication de la pièce neuve. - Absence de bruit de roulement
    côté distribution : au démarrage à froid, écouter la zone pompe à eau pendant 60 secondes. Un bruit de grincement ou de
    roulement bruité qui disparaît avec la chauffe pointe vers un roulement de qualité insuffisante ou un alignement incorrect
    de la poulie. - Niveau du liquide de refroidissement stable après 48 h : contrôler le niveau dans le vase d''expansion
    après refroidissement complet du moteur (lendemain de l''intervention). Une baisse significative trahit une micro-fuite
    non détectée à chaud ou une fuite interne vers le circuit d''huile (joint de culasse à vérifier).'
  S_GARAGE: 'Nous vous recommandons de confier cette intervention à un professionnel : - Plusieurs causes possibles de défaillance
    (4 identifiées) nécessitent un diagnostic professionnel Un garagiste qualifié dispose de l''outillage et de l''expérience
    nécessaires pour effectuer cette opération en toute sécurité.'
  S7: Quel est le prix d'un pompe à eau ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur pour trouver
    le pompe à eau compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment savoir si mon
    pompe à eau est à changer ?Les signes d'usure les plus courants sont détaillés dans la section diagnostic ci-dessus. En
    cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un pompe à eau défaillant ?Cela dépend
    de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule. Consultez la section symptômes
    pour évaluer l'urgence du remplacement.- faire circuler - pomper - alimenter
  S8: Comment choisir Pompe à eau compatible avec mon vehicule ?Renseignez marque, modele, type moteur et annee, puis verifiez
    la reference Quand remplacer Pompe à eau ?En cas de fuite de liquide au niveau de la pompe ou de degradation mesurable,
    Puis-je monter Pompe à eau sans verification atelier ?Le montage peut exiger controles de couple, alignement et references.
  META: '{"meta_title":"Pompe à eau : Conseils Remplacement et Guide | AutoMecanik","meta_description":"Surchauffe, fuite
    de liquide de refroidissement : découvrez quand changer la pompe à eau, comment la remplacer avec la courroie de distribution
    et éviter la casse moteur. AutoMecanik."}'
---

# Pompe à eau - Guide Diagnostic Complet

## Fonction et Rôle

Faire circuler le liquide de refroidissement dans le circuit moteur

**Actions principales:** faire circuler, pomper, alimenter, assurer la circulation

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Surchauffe moteur malgre niveau correct**
  surchauffe moteur malgre niveau correct

### 🟢 Autres Symptômes

- fuite de liquide au niveau de la pompe
- bruit de roulement cote distribution
- jeu perceptible dans la poulie de pompe
- odeur de liquide de refroidissement chaud
- echeance distribution approche preventif

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à eau:

1. **Inspection visuelle** - Examiner l'état du pompe à eau
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

- chaine-de-distribution
- courroie-d-accessoire
- courroie-de-distribution
- durite-de-refroidissement
- kit-de-chaine-de-distribution
- kit-de-distribution
- radiateur-de-refroidissement
- sonde-de-refroidissement

## Critères de Compatibilité

Pour commander le bon pompe à eau, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "evite la casse moteur"

## FAQ

**Pompe à eau OE ou adaptable ?**
Privilégiez l'OES (SKF, FAG, INA, Gates) pour une durée de vie garantie jusqu'à la prochaine distribution. Les adaptables sont risqués sur cette pièce critique.

**Comment savoir si ma pompe à eau fuit ?**
Fuite visible sous la pompe, bruit de roulement (grognement), jeu dans l'axe, traces de calcaire autour de la pompe, surchauffe moteur.

**Tous les combien changer la pompe à eau ?**
Avec la distribution : 80 000 à 120 000 km. Sinon, pas de périodicité fixe mais contrôle à chaque distribution.

**Peut-on changer la pompe à eau soi-même ?**
Possible si accessible, mais souvent liée à la distribution. Nécessite vidange du circuit et purge soignée après montage.

**Quelle erreur éviter avec la pompe à eau ?**
Ne pas monter une pompe sans changer le joint. Vérifier le sens de rotation de la turbine. Purger correctement le circuit après.
## Rôle de la pompe à eau

- Fait circuler le liquide de refroidissement dans le circuit moteur
- Assure le refroidissement du moteur en toutes conditions
- Entraînée par la courroie de distribution ou la courroie accessoire selon les moteurs

## Types de pompes

### Pompe mécanique (standard)
- Entraînée par courroie. Turbine en métal ou plastique renforcé.
- La plus courante, remplacement lors du kit de distribution recommandé.

### Pompe électrique
- Présente sur certains véhicules récents (BMW, certains VW/Audi)
- Fonctionnement indépendant du régime moteur, meilleure gestion thermique
- Remplacement spécifique, plus coûteux

## Signes de défaillance

- **Fuite au joint** : Goutte visible sous le véhicule, trace de rouille ou de calcaire sur la pompe
- **Roulement bruyant** : Sifflement ou grondement provenant de la pompe, jeu sur l'axe
- **Surchauffe moteur** : La pompe ne fait plus circuler assez de liquide
- **Turbine dégradée** : Pales cassées ou érodées (plastique), circulation insuffisante

## Remplacement avec la distribution

- Sur les moteurs où la pompe est entraînée par la courroie de distribution, **toujours la remplacer en même temps**
- Le coût supplémentaire de la pompe est négligeable face au coût de la main d'œuvre
- Un kit distribution complet inclut souvent la pompe (vérifier le contenu)

## Marques recommandées

- **SKF** : Spécialiste roulements, pompes de qualité OE
- **Saleri** : Fabricant italien spécialisé, OE pour de nombreux constructeurs
- **Dolz** : Bon rapport qualité-prix, large couverture
- **Gates** : Souvent vendu en kit avec la distribution

## Erreurs à éviter

- Ne jamais réutiliser le joint d'étanchéité de la pompe
- Vérifier la compatibilité de la turbine (métal vs plastique) avec le type de liquide de refroidissement
- Ne pas oublier de purger le circuit après remplacement
- Toujours utiliser du liquide de refroidissement neuf compatible
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
## Symptomes surchauffe

### Temoin temperature allume
- **Quand** : En roulant ou a l'arret
- **Caracteristique** : Voyant rouge fixe ou clignotant
- **Urgence** : Critique - Arreter immediatement le moteur

### Temperature monte rapidement
- **Quand** : Apres quelques kilometres
- **Caracteristique** : Aiguille dans le rouge en moins de 10 min
- **Urgence** : Haute - Risque joint de culasse

### Chauffage habitacle faible
- **Quand** : Moteur chaud
- **Caracteristique** : Air tiede au lieu de chaud
- **Indication** : Niveau liquide bas ou thermostat bloque

### Fuite liquide de refroidissement
- **Quand** : Vehicule a l'arret
- **Caracteristique** : Flaque verte/orange sous le vehicule
- **Localisation** : Durites, radiateur, pompe a eau

## Symptomes thermostat

### Moteur long a chauffer
- **Quand** : Par temps froid
- **Caracteristique** : Temperature ne monte pas apres 10 km
- **Cause probable** : Thermostat bloque ouvert

### Temperature instable
- **Quand** : En roulant
- **Caracteristique** : Aiguille qui oscille
- **Cause probable** : Thermostat defaillant

## Causes et solutions - Surchauffe

### 1. Niveau liquide insuffisant
- **Probabilite** : 40%
- **Verification** : Niveau vase expansion (moteur froid)
- **Solution** : Completer et chercher la fuite
- **Pieces** : Liquide refroidissement G12/G13
- **Urgence** : Moyenne

### 2. Pompe a eau defaillante
- **Probabilite** : 25%
- **Verification** : Jeu sur axe, fuite par trou temoin
- **Solution** : Remplacement (souvent avec distribution)
- **Pieces** : Pompe a eau
- **Urgence** : Haute

### 3. Thermostat bloque ferme
- **Probabilite** : 20%
- **Verification** : Durite superieure radiateur froide moteur chaud
- **Solution** : Remplacement thermostat
- **Pieces** : Calorstat/thermostat
- **Urgence** : Haute

### 4. Ventilateur HS
- **Probabilite** : 10%
- **Verification** : Ne se declenche pas a 100°C
- **Solution** : Test motoventilateur, fusible, relais
- **Pieces** : Motoventilateur, relais
- **Urgence** : Moyenne

### 5. Radiateur bouche/fuyant
- **Probabilite** : 5%
- **Verification** : Zones froides sur radiateur, traces calcaire
- **Solution** : Rinçage ou remplacement
- **Pieces** : Radiateur
- **Urgence** : Moyenne

## Causes et solutions - Fuites

### 1. Durites percees/craquelees
- **Probabilite** : 35%
- **Verification** : Inspection visuelle, traces blanches
- **Solution** : Remplacement durite
- **Pieces** : Durites refroidissement
- **Urgence** : Moyenne

### 2. Joint de pompe a eau
- **Probabilite** : 25%
- **Verification** : Fuite par trou temoin pompe
- **Solution** : Remplacement pompe complete
- **Pieces** : Pompe a eau
- **Urgence** : Haute

### 3. Bouchon vase expansion
- **Probabilite** : 20%
- **Verification** : Pression circuit (tarage bouchon)
- **Solution** : Remplacement bouchon
- **Pieces** : Bouchon vase expansion
- **Urgence** : Basse

### 4. Joint de culasse
- **Probabilite** : 10%
- **Verification** : Mayonnaise sous bouchon huile, fumee blanche echappement
- **Solution** : Remplacement joint (intervention lourde)
- **Pieces** : Joint de culasse, kit vis
- **Urgence** : Critique

### 5. Radiateur de chauffage
- **Probabilite** : 10%
- **Verification** : Odeur sucree habitacle, buee pare-brise
- **Solution** : Remplacement radiateur chauffage
- **Pieces** : Radiateur de chauffage
- **Urgence** : Moyenne

## Diagnostics complementaires

### Test de pression circuit
- Outil : Pompe de mise en pression
- Pression : 1.2 à 1.5 bar selon vehicule
- But : Detecter fuites non visibles

### Test CO2 dans liquide
- Outil : Testeur de fuite joint culasse
- Indicateur : Changement couleur (bleu → jaune)
- But : Confirmer fuite joint de culasse

## Recommandations

- **Liquide** : Respecter specifications constructeur (G12, G13, type D)
- **Melange** : Ne jamais melanger differents types
- **Vidange** : Tous les 4-5 ans ou 100 000 km
- **Purge** : Obligatoire apres intervention (bulles d'air = surchauffe)
- **Marques** : Valeo, Gates, SKF (pompes), Behr (radiateurs)


## Conseils supplementaires

<!-- materialized-from-db web/41593e6acbd2 2026-03-28 -->
### Filtres à carburant pour automobiles – Automobile – WIX Filters - section-1

# Filtres à carburant pour automobiles – Automobile – WIX Filters

- FILTRES À CARBURANT La propreté du carburant arrivant au moteur est très importante, parce qu'elle impacte l’usure des pièces du moteur tels que les pompes, les injecteurs, les soupapes qui régulent la pression de carburant. Une bonne filtration du carburant est nécessaire pour un fonctionnement fiable du moteur.</p>\r\n","repo:modifyDate":"2025-09-22T11:24:17Z","@type":"mannhummel-base/components/whitelabel/teaser-media-object","dc:title":"OFFRANT DES PERFORMANCES INÉGALÉES DE PURIFICATION DU CARBURANT"}}"> OFFRANT DES PERFORMANCES INÉGALÉES DE PURIFICATION DU CARBURANT La propreté du carburant arrivant au moteur est très importante, parce qu'elle impacte l’usure des pièces du moteur tels que les pompes, les injecteurs, les soupapes qui régulent la pression de carburant. Une bonne filtration du carburant est nécessaire pour un fonctionnement fiable du moteur. POURQUOI CHOISIR LES FILTRES À CARBURANT WIX FILTERS? Les filtres à carburant WIX Filters arrêtent tout aussi bien les impuretés qui proviennent du réservoir de l’automobile ou du carburant telles que les particules de rouille, les limailles provenant des éléments du système d’injection ainsi que l’eau (dans le cas des moteurs diesel). Grâce à notre expérience et notre compétence, nous produisons des filtres à carburant qui répondent aux normes exigeantes des fabricants automobiles.</p>\r\n","repo:modifyDate":"2025-09-22T11:25:22Z","@type":"mannhummel-base/components/whitelabel/teaser-content","dc:title":"EFFICACITÉ DE LA FILTRATION"}}"> EFFICACITÉ DE LA FILTRATION Les filtres à carburant WIX Filters arrêtent tout aussi bien les impuretés qui proviennent du réservoir de l’automobile ou du carburant telles que les particules de rouille, les limailles provenant des éléments du système d’injection ainsi que l’eau (dans le cas des moteurs diesel). Grâce à notre expérience et notre compétence, nous produisons des filtres à carburant qui répondent aux normes exigeantes des fabricants automobiles. Chaque moteur a ses exigences propres. Pour les filtres WIX Filters, nous utilisons des matériaux filtrants adaptés aux exigences définies par les fabricants de moteur ou de véhicules. Les propriétés des médias filtrants testés en laboratoire permettent d’atteindre l’efficacité souhaitée. Nous effectuons annuellement environ 4000 tests en laboratoire en Europe.</p>\r\n","repo:modifyDate":"2025-09-22T11:26:16Z","@type":"mannhummel-base/components/whitelabel/teaser-content","dc:title":"ADAPTATION DES MATÉRIAUX FILTRANTS AU MOTEUR"}}"> ADAPTATION DES MATÉRIAUX FILTRANTS AU MOTEUR Chaque moteur a ses exigences propres. Pour les filtres WIX Filters, nous utilisons des matériaux filtrants adaptés aux exigences définies par les fabricants de moteur ou de véhicules. Les propriétés des médias filtrants testés en laboratoire permettent d’atteindre l’efficacité souhaitée. Nous effectuons annuellement environ 4000 tests en laboratoire en Europe. En plus de l’élimination des particules, notamment celles de 4 à 6 microns, soit celles qui sont les plus dangereuses pour tous les éléments du système d’injection, les filtres à carburant doivent être très étanches. Chaque fuite de carburant est un risque d’incendie pour une automobile. C’est pourquoi tous nos filtres sont soumis aux tests d’étanchéité.</p>\r\n","repo:modifyDate":"2025-09-22T11:26:54Z","@type":"mannhummel-base/components/whitelabel/teaser-content","dc:title":"ÉTANCHÉITÉ PARFAITE"}}"> ÉTANCHÉITÉ PARFAITE En plus de l’élimination des particules, notamment celles de 4 à 6 microns, soit celles qui sont les plus dangereuses pour tous les éléments du système d’injection, les filtres à carburant doivent être très étanches. Chaque fuite de carburant est un risque d’incendie pour une automobile. C’est pourquoi tous nos filtres sont soumis aux tests d’étanchéité. Les systèmes d’injection des moteurs diesel exigent une efficacité remarquable de filtration et une séparation de l’eau. WIX Filters propose un large assortiment de filtres à carburant pour les véhicules équipés de systèmes d’injection moderne. Des procédés tels que la séparation de l’eau en plusieurs étapes répond aux exigences techniques les plus élevées.</p>\r\n","repo:modifyDate":"2025-09-22T11:27:24Z","@type":"mannhummel-base/components/whitelabel/teaser-content","dc:title":"PROTECTION DES SYSTÈMES D'INJECTION MODERNES"}}"> PROTECTION DES SYSTÈMES D'INJECTION MODERNES Les systèmes d’injection des moteurs diesel exigent une efficacité remarquable de filtration et une séparation de l’eau. WIX Filters propose un large assortiment de filtres à carburant pour les véhicules équipés de systèmes d’injection moderne. Des procédés tels que la séparation de l’eau en plusieurs étapes répond aux exigences techniques les plus élevées. LA QUALITÉ DES FILTRES WIX PROVIENT DE NOTRE COMPÉTENCE EN TANT QUE FOURNISSEUR D’ÉQUIPEMENTS D’ORIGINE La haute qualité des produits WIX Filters résulte de l’expertise approfondie de MANN+HUMMEL – notre société et principal fournisseur de filtres d’origine pour les plus grands constructeurs automobiles au monde. MANN+HUMMEL est le leader mondial de la technologie de filtration. Notre savoir-faire et nos standards de qualité garantissent que chaque filtre WIX offre une protection fiable pendant toute la durée de service recommandée. REGARDE COMMENT FONCTIONNE UN FILTRE A CARBURANT</h4>\r\n","repo:modifyDate":"2025-09-22T11:28:34Z","@type":"mannhummel-base/components/whitelabel/teaser-block"}}"> REGARDE COMMENT FONCTIONNE UN FILTRE A CARBURANT REGARDEZ LA VIDÉO Le corps en métal ou en plastique hermétiquement fermé dispose de connexions adaptées aux durites. Ces filtres sont utilisés tout aussi bien pour les moteurs à essence que diesel. Certains modèles prévus pour les moteurs diesel disposent de systèmes de filtration à plusieurs étapes qui permettent d’augmenter l’efficacité ainsi que la durée d’utilisation du filtre.</p>\r\n","repo:modifyDate":"2025-09-22T11:33:48Z","@type":"mannhummel-base/components/whitelabel/teaser-media-object","dc:title":"FILTRES AVEC CONNEXIONS"}}"> FILTRES AVEC CONNEXIONS Le corps en métal ou en plastique hermétiquement fermé dispose de connexions adaptées aux durites. Ces filtres sont utilisés tout aussi bien pour les moteurs à essence que diesel. Certains modèles prévus pour les moteurs diesel disposent de systèmes de filtration à plusieurs étapes qui permettent d’augmenter l’efficacité ainsi que la durée d’utilisation du filtre. L’aspect ressemble aux filtres à huile spin-on, cependant ils sont dépourvus de soupape interne. Cette solution permet au moteur de s’arrêter avant l’arrivée du carburant contaminé. Le filtre obturé agit comme un fusible et permet d’éviter une panne grave du moteur. Grâce à cela, uniquement le carburant propre entre dans la chambre à combustion. La probabilité d'introduction accidentelle de polluants dans le système de carburant lors du remplacement du filtre à vis est quasi nulle.</p>\r\n","repo:modifyDate":"2025-09-22T11:34:25Z","@type":"mannhummel-base/components/whitelabel/teaser-media-object","dc:title":"CARTOUCHES DE FILTRE À CARBURANT"}}"> CARTOUCHES DE FILTRE À CARBURANT L’aspect ressemble aux filtres à huile spin-on, cependant ils sont dépourvus de soupape interne. Cette solution permet au moteur de s’arrêter avant l’arrivée du carburant contaminé. Le filtre obturé agit comme un fusible et permet d’éviter une panne grave du moteur. Grâce à cela, uniquement le carburant propre entre dans la chambre à combustion. La probabilité d'introduction accidentelle de polluants dans le système de carburant lors du remplacement du filtre à vis est quasi nulle. L’aspect ressemble aux filtres à huile spin-on, cependant ils sont dépourvus de soupape interne. Cette solution permet au moteur de s’arrêter avant l’arrivée du carburant contaminé. Le filtre obturé agit comme un fusible et permet d’éviter une panne grave du moteur. Grâce à cela, uniquement le carburant propre entre dans la chambre à combustion. La probabilité d'introduction accidentelle de polluants dans le système de carburant lors du remplacement du filtre à vis est quasi nulle.</p>\r\n","repo:modifyDate":"2025-09-22T11:35:11Z","@type":"mannhummel-base/components/whitelabel/teaser-media-object","dc:title":"FILTRES À VIS"}}"> FILTRES À VIS L’aspect ressemble aux filtres à huile spin-on, cependant ils sont dépourvus de soupape interne. Cette solution permet au moteur de s’arrêter avant l’arrivée du carburant contaminé. Le filtre obturé agit comme un fusible et permet d’éviter une panne grave du moteur. Grâce à cela, uniquement le carburant propre entre dans la chambre à combustion. La probabilité d'introduction accidentelle de polluants dans le système de carburant lors du remplacement du filtre à vis est quasi nulle. TROUVEZ UN FILTRE

![](_raw/web-images/ff36149084c9b09c.jpg)

![](_raw/web-images/d41ac56feae4b5a8.jpg)

![](_raw/web-images/8d971be07dcf7360.jpg)

![](_raw/web-images/67a6a2f64f9e0fb9.jpg)

![](_raw/web-images/1f0ef3d7dc72fc7c.jpg)

![](_raw/web-images/5cee958255b1a9f3.jpg)

- OÙ ACHETER

- YOUTUBE

- CONTACTEZ-NOUS

ACCÈS RAPIDE

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
- Performances

[...]
