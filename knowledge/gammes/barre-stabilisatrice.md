---
category: direction
slug: barre-stabilisatrice
title: Barre stabilisatrice
pg_id: 274
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
  role: Limiter le roulis en virage - Relie les deux cotes de la suspension pour transferer les efforts
  must_be_true:
  - limiter le roulis
  - stabiliser
  - relier
  must_not_contain:
  - direction
  - cremailliere
  - volant
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - cremailliere-de-direction
  - rotule-de-direction
  - pompe-de-direction-assistee
  - barre-de-direction
  - soufflet-de-direction
  - colonne-de-direction
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
  - ❌ "securite garantie"
  cost_range:
    min: 3
    max: 147
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Piece d'origine (OE)
    description: Barre reference constructeur. Garantit la correspondance exacte des diametres et points de fixation. Recommandee
      sur vehicules recents.
  - tier: Equipementier specialise suspension
    description: Fabricants specialises en pieces de suspension, fournissant les constructeurs ou proposant des equivalences
      techniques documentees. Pieces generalement fabriquees en acier traite avec les memes caract
  brands:
    premium:
    - Lemforder
    - TRW
    standard:
    - Febi
    - Meyle
    - MOOG
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Roulis excessif en virage
    severity: confort
  - id: S2
    label: Claquements sur route degradee
    severity: confort
  - id: S3
    label: Bruits sourds en compression
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : roulis excessif en virage'
  quick_checks:
  - 'Observer : roulis excessif en virage ?'
  - 'Observer : claquements sur route degradee ?'
  - Bruits sourds en compression ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Roulis excessif en virage
  - Claquements sur route degradee
  - Bruits sourds en compression
  good_practices:
  - Controle du jeu de direction a chaque revision
  - Verifier les soufflets de protection (pas de fuite de graisse)
  - Faire verifier la geometrie apres remplacement
  - Inspecter les biellettes et rotules associees
rendering:
  pgId: '274'
  intro_title: A quoi sert Barre stabilisatrice ?
  risk_title: Pourquoi remplacer Barre stabilisatrice a temps ?
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
  - question: Comment choisir Barre stabilisatrice compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Barre stabilisatrice ?
    answer: En cas de roulis excessif en virage ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Barre stabilisatrice sans verification atelier ?
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
doc_id: a27a623e-f80d-5194-8936-48cb76b973e3
content_hash: sha256:8f03dda616eedb18
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
  area: Sous le vehicule, relie le volant aux roues
  access: Par le dessous (pont elevateur recommande)
  adjacent_parts:
  - cremailliere
  - biellette
  - rotule
  - soufflet
installation:
  difficulty: difficile
  time: 1h a 3h
  tools:
  - cle a douille
  - arrache-rotule
  - cle dynamometrique
  prerequisite: Pont elevateur, geometrie a refaire apres
phase5_enrichment:
  _source: delphiautoparts.com + fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 3
  _has_tech_data: true
  types_variants:
  - type: 'plein'
    source_ref: corpus RAG web OEM
  - type: 'pneumatique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_000_nm: '000 Nm'
    val_10_a: '10 a'
    val_100_a: '100 a'
    val_22_a: '22 a'
    val_30_a: '30 a'
    val_7_a: '7 a'
    val_800_nm: '800 Nm'
  materials:
  - materiau: 'aluminium'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Une barre stabilisatriceest un composant très important pour le véhicule, il est en forme de U aplati,forgée en métal.
    La barre stabilisatrice sert àassurer la stabilité de la voiture dans les virages, sur les routesirrégulières et sur les
    chaussées déformées pour conserver une bonne tenue deroute. Surun véhicule il ya une barre stabilisatrice à l''avant et
    une à l''arrière(suivant le niveau d''équipement de votre véhicule). La barre stabilisatrice vapermettre d''équilibrer
    la pression des roues parce que dans un virage,la pression est plus forte sur les roues intérieur ce qui a pour conséquenced''entraîner
    les deux roues extérieur. Sans labarre stabilisatrice les roues entraînées par le poids du véhiculepeuvent quitter la
    chaussée jusqu''au renversement complet de l''automobile. Elleva limiter lesinclinaisons de la voiture dans les virages,
    d''où le nom de barres anti- dévers.La barre stabilisatrice exerce une action anti-roulis grâceà ses ressorts et ses barres
    qui contribuent à augmenter l''adhérence au sol dela voiture. La barre stabilisatrice créeune solidarité entre les roues,
    le tangage est moindre, la voiture reste stablesur ces quatre roues. La barre stabilisatrice absorbe les chocs et les
    vibrations pour soulager lesroues et le reste de la mécanique. En savoir plus : barre stabilisatrice — définition et rôle
    mécanique 🚨 Bruit Barre stabilisatrice : causes et diagnostic'
  S2: 'Une barre stabilisatrice défectueuse présente plusieurssymptômes : - Des à coups dans le volantde direction. - Bruit
    de claquement ouvibration lors des virages. - Le véhicule tire plus d''uncôté que d''un autre. - Mauvaise tenue de route
    duvéhicule. Diagnostic complet : identifier une panne de barre stabilisatrice'
  S3: 'La barre stabilisatrice (ou barre antiroulis) limite le roulis en virage. Son remplacement nécessite une pièce strictement
    identique à l''originale.Vérifications indispensables- Diamètre de la barre : mesuré au pied à coulisse (18, 20, 22, 24
    mm selon le modèle) — un mauvais diamètre modifie le comportement dynamique- Longueur et forme : droite ou coudée, la
    géométrie doit correspondre exactement au châssis- Points de fixation : écartement des paliers et diamètre des silentblocs
    de fixation- Type d''attache : biellettes à rotule ou à silentbloc — vérifier la compatibilité avec les biellettes existantesMéthode
    de vérificationComparer la référence OE de la barre déposée. Mesurer le diamètre avec un pied à coulisse et la longueur
    totale. Vérifier le nombre et la position des points de fixation.Pour aller plus loin : consultez notre guide d''achat
    barre stabilisatrice — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 📖 Avant de démonter, consultez la fiche technique Barre stabilisatrice pour connaître les spécifications. - Levez
    et calez le véhicule. - Démontez les roues. - Démontez la rotule desuspension pour faciliter la manipulation sur la barre
    stabilisatrice. - Desserrez les écrous defixations supérieure et inférieure de la biellette de la barre stabilisatrice.
    - Desserrez les fixations du berceau si nécessaire. - Descendre un peut le berceau pour faciliter le démontage de la barre
    stabilisatrice. - Desserrez les fixations dela barre stabilisatrice sur le berceau. - Démontez la barrestabilisatrice.
  S4_REPOSE: '- Vérifier que la barre stabilisatrice neuve est identique à celle démontée. - Changer les silentblocs de la
    barre stabilisatrice. - Vérifiez l''état d''usure du bras de suspension et remplacé si nécessaire. - Mettre en place la
    barre stabilisatrice. - Serrer les fixations de la barre stabilisatrice. - Remontez le berceau et serrer ces fixations.
    - Mettre en place les biellettes de la barre stabilisatrice. - Serrez les fixation des biellettes de la barre stabilisatrice.
    - Remontez la rotule de suspension. - Remontez les roues. - Descendre de véhicule. - Contrôlez les valeurs de réglage
    de la géométrie des trains et les réglées si nécessaire. ✅ Après remontage, vérifiez les spécifications dans la fiche
    technique Barre stabilisatrice.'
  S5: '- Confondre barre stabilisatrice et biellette — la biellette est la pièce d''usure courante, la barre elle-même casse
    rarement → diagnostiquer correctement avant de commander- Monter une barre de mauvais diamètre — le comportement en virage
    sera déséquilibré, risque de sur-virage ou sous- virage → vérifier le diamètre au pied à coulisse avant montage- Réutiliser
    des silentblocs de palier usés — la barre claquera dans ses supports dès les premiers nids-de-poule → remplacer systématiquement
    les silentblocs de palier avec la barre- Serrer les fixations véhicule en l''air — les silentblocs seront précontraints
    en torsion permanente, usure accélérée → effectuer le serrage final au couple, véhicule au sol à hauteur de roulage- Oublier
    de graisser les silentblocs neufs — grincements et usure prématurée au contact barre/silentbloc → appliquer une fine couche
    de graisse silicone sur la portée de la barre- Ne pas vérifier l''état des biellettes — une biellette avec du jeu transmet
    les chocs à la barre et à la caisse → contrôler et remplacer les biellettes si elles présentent du jeu axial ou radial-
    Forcer le positionnement de la barre — si la barre ne se positionne pas naturellement, la référence est incorrecte → ne
    jamais modifier ou plier une barre stabilisatrice- Négliger le couple de serrage des paliers — un serrage excessif écrase
    le silentbloc, insuffisant provoque du jeu → respecter le couple constructeur (25-45 Nm selon modèle) 📖 Fiche technique
    Barre stabilisatrice — spécifications à vérifier avant montage.'
  S6: 'Contrôles statiques (véhicule au sol)- Vérifier le serrage des paliers de barre au couple constructeur- Contrôler que
    les biellettes sont correctement fixées aux deux extrémités- Inspecter l''absence de contact entre la barre et les durites
    de frein ou les câbles ABS- Vérifier que les silentblocs sont bien centrés et non pincésTest routier progressif- Rouler
    sur route plane à 50 km/h : pas de bruit de claquement ni de grincement- Passer sur un ralentisseur à 30 km/h : absence
    de cognement sourd provenant du train avant- Effectuer des virages à vitesse modérée : le véhicule ne doit pas rouler
    excessivement (sensation de flottement)- Enchaîner des changements de direction rapides : la barre doit stabiliser le
    châssis sans délai⚠️ Important : Si des claquements persistent après remplacement, vérifiez en priorité les biellettes
    de barre stabilisatrice et les silentblocs de palier — ce sont les causes les plus fréquentes de bruit résiduel. 🚨 Bruit
    Barre stabilisatrice : causes et diagnostic'
  S7: Quel est le prix d'un barre stabilisatrice ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur pour
    trouver le barre stabilisatrice compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon barre stabilisatrice est à changer ?Les signes d'usure les plus courants sont détaillés dans la section
    diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un barre stabilisatrice
    défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule. Consultez
    la section symptômes pour évaluer l'urgence du remplacement.- Bras de suspension. - Silentbloc de barre stabilisatrice.
    📖 Fiche technique Barre stabilisatrice — intervalles et spécifications d’entretien.
  S8: 'Quels sont les symptômes d''une barre stabilisatrice défaillante ?Les signes principaux sont des claquements sourds
    en passant sur des irrégularités, un roulis excessif en virage (la caisse penche davantage), et parfois un bruit de grincement
    au passage de dos-d''âne. Attention : ces symptômes sont souvent causés par les biellettes ou les silentblocs de palier,
    pas par la barre elle-même.Faut-il remplacer les biellettes en même temps que la barre ?Pas obligatoirement, mais c''est
    fortement recommandé. Les biellettes de barre stabilisatrice s''usent plus vite que la barre. Si vous remplacez la barre,
    profitez-en pour inspecter les biellettes : tout jeu axial ou rotule fissurée justifie leur remplacement simultané.Peut-on
    rouler sans barre stabilisatrice ?Techniquement oui, mais c''est déconseillé et interdit au contrôle technique. Sans barre
    stabilisatrice, le roulis en virage augmente considérablement, réduisant la tenue de route et la sécurité, surtout en
    cas d''évitement d''urgence.Quelle différence entre barre stabilisatrice avant et arrière ?La barre avant est plus épaisse
    (20-24 mm) et gère l''essentiel du roulis. La barre arrière (16-20 mm), quand elle existe, affine l''équilibre dynamique.
    Tous les véhicules n''ont pas de barre arrière. Ne jamais intervertir avant et arrière.Combien de temps dure une barre
    stabilisatrice ?La barre en acier dure généralement toute la vie du véhicule sauf corrosion sévère. Ce sont les silentblocs
    de palier (50 000-80 000 km) et les biellettes (60 000-100 000 km) qui s''usent et nécessitent un remplacement périodique.
    📖 Pour plus de détails techniques : fiche Barre stabilisatrice'
  META: 'Guide remplacement barre stabilisatrice : vérifier le diamètre, éviter les erreurs courantes, contrôles après montage
    et FAQ. Conseils techniques.'
---

# Barre stabilisatrice - Guide Diagnostic Complet

## Fonction et Rôle

Limiter le roulis en virage - Relie les deux cotes de la suspension pour transferer les efforts

**Actions principales:** limiter le roulis, stabiliser, relier, equilibrer

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquements sur route degradee**
  claquements sur route degradee

### 🟢 Autres Symptômes

- roulis excessif en virage
- bruits sourds en compression

## Procédure de Diagnostic

Pour diagnostiquer un problème de barre stabilisatrice:

1. **Inspection visuelle** - Examiner l'état du barre stabilisatrice
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

- bras-de-suspension

## Critères de Compatibilité

Pour commander le bon barre stabilisatrice, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"

## FAQ

**Comment choisir Barre stabilisatrice compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Barre stabilisatrice ?**
En cas de roulis excessif en virage ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Barre stabilisatrice sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
## Symptomes amortisseurs uses

### Rebonds excessifs
- **Quand** : Passage dos d'ane, ralentisseurs
- **Caracteristique** : Vehicule continue de rebondir
- **Test** : Appuyer sur aile, plus de 2 rebonds = use

### Tenue de route degradee
- **Quand** : Virage, freinage, autoroute
- **Caracteristique** : Vehicule flottant, instable
- **Urgence** : Securite - A remplacer rapidement

### Usure pneus anormale
- **Quand** : Controle visuel
- **Caracteristique** : Usure en vagues, facettes
- **Indication** : Amortisseurs HS depuis longtemps

### Bruits de suspension
- **Quand** : Routes degradees
- **Caracteristique** : Claquements, cognements
- **Distinction** : Amortisseur vs silent-bloc vs rotule

## Symptomes ressorts

### Vehicule affaisse
- **Quand** : A l'arret
- **Caracteristique** : Un cote plus bas que l'autre
- **Cause** : Ressort casse ou fatigue

### Bruits metalliques
- **Quand** : Compression suspension
- **Caracteristique** : Claquement sec, grincement
- **Verification** : Coupelle superieure, butee

## Symptomes rotules et silent-blocs

### Jeu dans la direction
- **Quand** : Manoeuvres parking
- **Caracteristique** : Direction floue, impreise
- **Test** : Roue levee, jeu lateral

### Claquements sourds
- **Quand** : Depart, freinage, dos d'ane
- **Caracteristique** : Bruit sourd cote roue
- **Cause probable** : Silent-bloc triangle use

## Causes et solutions - Amortisseurs

### 1. Amortisseurs uses (fuite huile)
- **Probabilite** : 60%
- **Verification** : Traces huile sur corps amortisseur
- **Solution** : Remplacement par paire (essieu)
- **Pieces** : Amortisseurs avant/arriere
- **Urgence** : Haute (securite)

### 2. Coupelles/butees HS
- **Probabilite** : 25%
- **Verification** : Bruit rotation volant a l'arret
- **Solution** : Remplacement kit complet
- **Pieces** : Kit butee + roulement
- **Urgence** : Moyenne

### 3. Ressort casse
- **Probabilite** : 10%
- **Verification** : Inspection visuelle, hauteur caisse
- **Solution** : Remplacement par paire
- **Pieces** : Ressorts de suspension
- **Urgence** : Haute

### 4. Soufflet dechire
- **Probabilite** : 5%
- **Verification** : Poussiere/eau dans amortisseur
- **Solution** : Remplacement amortisseur (soufflet non vendu seul)
- **Pieces** : Amortisseur complet
- **Urgence** : Moyenne

## Causes et solutions - Train roulant

### 1. Silent-blocs triangle uses
- **Probabilite** : 40%
- **Verification** : Jeu visible, caoutchouc craquele
- **Solution** : Remplacement triangle complet ou silent-bloc seul
- **Pieces** : Triangle de suspension, silent-bloc
- **Urgence** : Moyenne

### 2. Rotule de direction usee
- **Probabilite** : 25%
- **Verification** : Jeu rotule (roue levee)
- **Solution** : Remplacement + geometrie
- **Pieces** : Rotule de direction
- **Urgence** : Haute (securite)

### 3. Biellette de barre stabilisatrice
- **Probabilite** : 20%
- **Verification** : Claquement dans virages
- **Solution** : Remplacement biellettes
- **Pieces** : Biellettes stabilisateur
- **Urgence** : Moyenne

### 4. Roulement de roue
- **Probabilite** : 15%
- **Verification** : Ronronnement proportionnel vitesse
- **Solution** : Remplacement roulement
- **Pieces** : Roulement moyeu
- **Urgence** : Haute

## Intervalles de remplacement

| Piece | Kilometrage indicatif |
|-------|----------------------|
| Amortisseurs | 80 000 - 100 000 km |
| Ressorts | Controle apres 120 000 km |
| Silent-blocs | 100 000 - 150 000 km |
| Rotules | 100 000 - 150 000 km |
| Biellettes | 80 000 - 120 000 km |

## Recommandations

- **Remplacement par paire** : Toujours remplacer par essieu (AV gauche + AV droit)
- **Geometrie** : Obligatoire apres remplacement rotules, triangles
- **Kit complet** : Preferer kits avec butee et soufflet
- **Marques** : Bilstein, Monroe, Sachs, KYB (amortisseurs), Lemforder, TRW (train roulant)
- **Controle** : A chaque revision, au CT tous les 2 ans

## Test rapide amortisseurs

1. Stationner sur sol plat
2. Appuyer fortement sur chaque aile
3. Relacher et compter les rebonds
4. **OK** : 1-2 rebonds max
5. **Use** : Plus de 2 rebonds


## References supplementaires

<!-- materialized-from-db manual/8b352d0eb2ce 2026-04-03 -->
### Données techniques OEM — Barre stabilisatrice

# Données techniques OEM — Barre stabilisatrice
Source : delphiautoparts.com + fr.wikipedia.org (3 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- plein
- pneumatique

## Matériaux
- aluminium

## Valeurs techniques de référence
- 000 Nm
- 800 Nm

## Symptomes supplementaires

<!-- materialized-from-db diagnostic/amortisseurs.md 2026-01-08 -->
### Diagnostic - Amortisseurs et suspension

# Amortisseurs et suspension - Diagnostic complet

## Symptomes amortisseurs uses

### Rebonds excessifs
- **Quand** : Passage dos d'ane, ralentisseurs
- **Caracteristique** : Vehicule continue de rebondir
- **Test** : Appuyer sur aile, plus de 2 rebonds = use

### Tenue de route degradee
- **Quand** : Virage, freinage, autoroute
- **Caracteristique** : Vehicule flottant, instable
- **Urgence** : Securite - A remplacer rapidement

### Usure pneus anormale
- **Quand** : Controle visuel
- **Caracteristique** : Usure en vagues, facettes
- **Indication** : Amortisseurs HS depuis longtemps

### Bruits de suspension
- **Quand** : Routes degradees
- **Caracteristique** : Claquements, cognements
- **Distinction** : Amortisseur vs silent-bloc vs rotule

## Symptomes ressorts

### Vehicule affaisse
- **Quand** : A l'arret
- **Caracteristique** : Un cote plus bas que l'autre
- **Cause** : Ressort casse ou fatigue

### Bruits metalliques
- **Quand** : Compression suspension
- **Caracteristique** : Claquement sec, grincement
- **Verification** : Coupelle superieure, butee

## Symptomes rotules et silent-blocs

### Jeu dans la direction
- **Quand** : Manoeuvres parking
- **Caracteristique** : Direction floue, impreise
- **Test** : Roue levee, jeu lateral

### Claquements sourds
- **Quand** : Depart, freinage, dos d'ane
- **Caracteristique** : Bruit sourd cote roue
- **Cause probable** : Silent-bloc triangle use

## Causes et solutions - Amortisseurs

### 1. Amortisseurs uses (fuite huile)
- **Probabilite** : 60%
- **Verification** : Traces huile sur corps amortisseur
- **Solution** : Remplacement par paire (essieu)
- **Pieces** : Amortisseurs avant/arriere
- **Urgence** : Haute (securite)

### 2. Coupelles/butees HS
- **Probabilite** : 25%
- **Verification** : Bruit rotation volant a l'arret
- **Solution** : Remplacement kit complet
- **Pieces** : Kit butee + roulement
- **Urgence** : Moyenne

### 3. Ressort casse
- **Probabilite** : 10%
- **Verification** : Inspection visuelle, hauteur caisse
- **Solution** : Remplacement par paire
- **Pieces** : Ressorts de suspension
- **Urgence** : Haute

### 4. Soufflet dechire
- **Probabilite** : 5%
- **Verification** : Poussiere/eau dans amortisseur
- **Solution** : Remplacement amortisseur (soufflet non vendu seul)
- **Pieces** : Amortisseur complet
- **Urgence** : Moyenne

## Causes et solutions - Train roulant

### 1. Silent-blocs triangle uses
- **Probabilite** : 40%
- **Verification** : Jeu visible, caoutchouc craquele
- **Solution** : Remplacement triangle complet ou silent-bloc seul
- **Pieces** : Triangle de suspension, silent-bloc
- **Urgence** : Moyenne

### 2. Rotule de direction usee
- **Probabilite** : 25%
- **Verification** : Jeu rotule (roue levee)
- **Solution** : Remplacement + geometrie
- **Pieces** : Rotule de direction
- **Urgence** : Haute (securite)

### 3. Biellette de barre stabilisatrice
- **Probabilite** : 20%
- **Verification** : Claquement dans virages
- **Solution** : Remplacement biellettes
- **Pieces** : Biellettes stabilisateur
- **Urgence** : Moyenne

### 4. Roulement de roue
- **Probabilite** : 15%
- **Verification** : Ronronnement proportionnel vitesse
- **Solution** : Remplacement roulement
- **Pieces** : Roulement moyeu
- **Urgence** : Haute

## Intervalles de remplacement

| Piece | Kilometrage indicatif |
|-------|----------------------|
| Amortisseurs | 80 000 - 100 000 km |
| Ressorts | Controle apres 120 000 km |
| Silent-blocs | 100 000 - 150 000 km |
| Rotules | 100 000 - 150 000 km |
| Biellettes | 80 000 - 120 000 km |

## Recommandations

- **Remplacement par paire** : Toujours remplacer par essieu (AV gauche + AV droit)
- **Geometrie** : Obligatoire apres remplacement rotules, triangles
- **Kit complet** : Preferer kits avec butee et soufflet
- **Marques** : Bilstein, Monroe, Sachs, KYB (amortisseurs), Lemforder, TRW (train roulant)
- **Controle** : A chaque revision, au CT tous les 2 ans

## Test rapide amortisseurs

1. Stationner sur sol plat
2. Appuyer fortement sur chaque aile
3. Relacher et compter les rebonds
4. **OK** : 1-2 rebonds max
5. **Use** : Plus de 2 rebonds
