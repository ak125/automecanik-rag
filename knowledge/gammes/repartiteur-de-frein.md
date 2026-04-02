---
category: freinage
slug: repartiteur-de-frein
title: Répartiteur de frein
pg_id: 73
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
  role: Repartir la pression de freinage entre les essieux
  must_be_true:
  - repartir
  - distribuer
  - equilibrer
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
  - ❌ "freinage garanti"
  cost_range:
    min: 15
    max: 200
    currency: EUR
    unit: l'unite
    source: estimation categorie
  brands:
    premium:
    - Bosch
    - TRW/ZF
    - ATE/Continental
    standard:
    - Ferodo
    - LPR
    - Bendix
    budget:
    - ABE
    - NK
    - sbs
  quality_tiers:
  - tier: Origine constructeur (OE/OES)
    description: Repartiteur identique a la premiere monte. Calibration de pression conforme aux specifications du constructeur
      pour l'equilibre avant/arriere.
  - tier: Equivalent OE (qualite premiere monte)
    description: Repartiteur de qualite equivalente, teste en pression. Calibration verifiee.
  - tier: Adaptable (qualite atelier courant)
    description: Repartiteur compatible. Verifier le type de raccords et la pression de coupure avant commande.
diagnostic:
  symptoms:
  - id: S1
    label: Roues arriere qui bloquent trop tot au freinage
    severity: immobilisation
  - id: S2
    label: Freinage desequilibre avant arriere
    severity: securite
  - id: S3
    label: Fuite au niveau du repartiteur
    severity: confort
  - id: S4
    label: Echec au controle technique desequilibre
    severity: confort
  - id: S5
    label: Desequilibre freinage controle technique valeurs
    severity: securite
  causes:
  - verification urgente piece et alimentation
  - identifier origine fuite et verifier joints
  - 'vehicule immobilise ou symptome critique : verification urgente piece et alimentation'
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  quick_checks:
  - 'Observer : roues arriere qui bloquent trop tot au freinage ?'
  - 'Observer : freinage desequilibre avant arriere ?'
  - Fuite au niveau du repartiteur ?
  - 'Observer : echec au controle technique desequilibre ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Roues arriere qui bloquent trop tot au freinage
  - Freinage desequilibre avant arriere
  - Fuite au niveau du repartiteur
  - Echec au controle technique desequilibre
  - Desequilibre freinage controle technique valeurs
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '73'
  intro_title: A quoi sert Répartiteur de frein ?
  risk_title: Pourquoi remplacer Répartiteur de frein a temps ?
  risk_explanation: '**Pièce HS** - Le répartiteur de frein peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le répartiteur de frein peut être hors service et nécessiter un remplacement'
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
  - question: À quoi sert le répartiteur de frein ?
    answer: Il dose la pression envoyée aux freins arrière pour éviter le blocage. Sur les véhicules modernes avec ABS, cette
      fonction est souvent électronique (EBD).
  - question: Mon véhicule a-t-il un répartiteur mécanique ?
    answer: Les véhicules sans ABS ont généralement un répartiteur mécanique ou compensateur de charge. Avec ABS/EBD, la répartition
      est gérée électroniquement.
  - question: Quels sont les symptômes d'un répartiteur défaillant ?
    answer: Blocage prématuré des roues arrière au freinage, déséquilibre constaté au contrôle technique, ou fuite de liquide
      au niveau du répartiteur.
  - question: Quelles sont les erreurs fréquentes à éviter ?
    answer: Diagnostiquer 'répartiteur HS' sur véhicule ABS alors que la répartition est électronique (EBD). Confondre blocage
      arrière avec pneus/pression/amortisseurs fatigués.
  - question: Comment faire un diagnostic rapide ?
    answer: 'Véhicule sans ABS + arrière qui bloque → répartiteur/correcteur à suspecter. Fuite sous caisse près essieu AR
      → répartiteur possible. Avec ABS : chercher d''abord défaut capteurs/diag.'
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
doc_id: 97318f4a-4b75-5cf3-883d-9403c17cb032
content_hash: sha256:cda5f07f377d2afe
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
  _source: ate-freinage.fr
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'hydraulique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_50__: '50 %'
  materials:
  - materiau: 'acier inoxydable'
    source_ref: corpus RAG web OEM
  - materiau: 'aluminium'
    source_ref: corpus RAG web OEM
  - materiau: 'fonte grise'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: Le répartiteur de frein est un boîtier hydraulique qui va diminuer la pression de freinage sur les rouesarrière et éviter
    leurs blocages. Il est situé dans le circuit de freinage entrel'avant et l'arrière du véhicule. Lors de l'augmentation
    de la pression de freinage vousrisquez un blocage des roues arrière, une soupape limite la pression sur lecircuit de freinage
    arrière. Lorsque leconducteur appuie sur la pédale frein, il va avoir une accumulationdes forces de pression sur l'avant
    et un délestage sur l'arrière, ce qui va provoquer le blocagedes roues arrière lors du freinage, dansce cas vous allez
    avoir une inefficacité des freins arrière ce qui peut amener à la pertede contrôle du véhicule c'est ici ou intervient
    le rôle du répartiteur de frein. Sur les voitures modernes, le système ABS de roues fait disparaîtreles répartiteurs de
    freinage aussi appelés correcteurs defreinage.
  S2: 'Un répartiteur de frein défectueuxprésente plusieurs symptômes : - Rallongementdes distances de freinage. - Blocage
    desroues lors du freinage. - Lors d''uncontrôle visuel vous constatez la présence d''une fuite de liquide de frein. Unrépartiteur
    de frein usé et qu''il n''est pas changé à temps peut causerplusieurs problèmes : - Usure des disques de frein. - Usure
    des plaquettes defrein. - Usure des étriers de frein. - Risque d''accident à causede blocage des roues.'
  S3: 'Avant de commander, vérifiez ces caractéristiques : - Type de répartiteur : à clapet (fixe) ou à correcteur de charge
    (compensateur) — ils ne sont pas interchangeables - Nombre de raccords : généralement 3 (1 entrée depuis le maître-cylindre,
    2 sorties vers les roues arrière) - Filetage des raccords : M10x1 ou M10x1,25 selon l''origine du véhicule - Fixation
    : boulonné sur le longeron ou le train arrière — vérifier l''entraxe des vis de fixation Méthode : relever le nombre de
    raccords et le type (correcteur ou clapet) sur l''ancien, ou utiliser le sélecteur véhicule. ➡️ Trouver les répartiteurs
    compatibles avec votre véhicule Pour aller plus loin : consultez notre guide d''achat répartiteur de frein — comparatif
    marques, critères de choix et prix.'
  S4_DEPOSE: '- Levez et calez le véhicule. - Localisez l''emplacement durépartiteur de frein. - Démontez la roue du cotéconcerné.
    - Démontez les canalisationsdu répartiteur de frein. - Desserrez les fixations durépartiteur de frein. - Désolidarisez
    lerépartiteur de frein. - Retirez le répartiteur de frein de son logement.'
  S4_REPOSE: 'Le remontage du répartiteur de frein exige une attention particulière à l''étanchéité du circuit hydraulique
    et à l''équilibrage du freinage avant- arrière. Sur les véhicules sans ABS disposant d''un correcteur de charge asservi
    à la charge arrière, le réglage mécanique doit être respecté scrupuleusement pour éviter tout blocage prématuré des roues
    arrière. - Vérifiez que le répartiteur de frein neuf est identique à celui démonté : type (proportionnel, correcteur de
    charge), diamètre des raccords hydrauliques, référence constructeur. - Contrôlez l''état des plaquettes de frein avant
    et arrière — un répartiteur remplacé avec des plaquettes usées en fin de vie conduira à un déséquilibre immédiat. - Contrôlez
    l''état des disques de frein arrière : des disques voilés ou sous l''épaisseur minimale amplifient le déséquilibre de
    freinage que le répartiteur doit corriger. - Contrôlez l''état du flexible de frein arrière et des canalisations : remplacez
    tout flexible présentant des craquelures ou des zones durcies qui pourraient restreindre le flux hydraulique. - Remontez
    le répartiteur de frein dans son logement et serrez les fixations au couple spécifié. Si le répartiteur est asservi à
    l''essieu arrière par une biellette, vérifiez que l''axe de liaison est correctement positionné. - Raccordez les canalisations
    hydrauliques en commençant par les raccords d''entrée, puis de sortie. Serrez sans excès pour ne pas fissurer les olives
    de cuivre. - Remplissez le circuit de frein avec du liquide DOT 4 neuf et purgez intégralement la ligne arrière passant
    par le répartiteur jusqu''à l''absence totale de bulles d''air au purgeur de chaque roue arrière. - Remontez la roue du
    côté concerné au couple de serrage prescrit (typiquement 110 à 130 N·m sur véhicule de tourisme). - Effectuez un test
    de freinage progressif à basse vitesse (20 km/h) sur sol sec pour vérifier l''absence de blocage prématuré des roues arrière.
    - Vérifiez le niveau de liquide de frein dans le réservoir du maître-cylindre et complétez si nécessaire avant toute circulation.'
  S5: '- Confondre répartiteur fixe et correcteur de charge — Le correcteur s''adapte à la charge du véhicule, le répartiteur
    fixe non. → Vérifier le type exact sur l''ancien composant. - Inverser les raccords d''entrée et de sortie — Le freinage
    arrière est inversé ou supprimé. → Repérer et étiqueter chaque canalisation avant dépose. - Arrondir les raccords avec
    une clé plate — Les écrous en laiton s''arrondissent facilement. → Utiliser exclusivement une clé à tuyauter (ouverte
    6 pans). - Ne pas purger le circuit après remplacement — De l''air dans les canalisations arrière rend le freinage inefficace.
    → Purger les deux roues arrière après montage. - Oublier de régler le correcteur de charge — Si le répartiteur est un
    correcteur, la tige de liaison avec l''essieu arrière doit être correctement réglée. → Ajuster la longueur de la tige
    selon la spécification constructeur. - Serrer les raccords trop fort — Le filetage en laiton casse ou se déforme, causant
    une fuite. → Serrer fermement à la main puis 1/4 de tour à la clé. - Ne pas vérifier l''état des canalisations — Des canalisations
    rigides rouillées peuvent casser lors du démontage du raccord. → Inspecter les tubes et les remplacer si piqués. - Ne
    pas tester le freinage sur les deux essieux — Le répartiteur dose la répartition AV/AR. → Vérifier que les 4 roues freinent
    correctement après montage.'
  S6: 'Contrôles statiques - Vérifier l''absence de fuite à chaque raccord hydraulique - Contrôler le niveau de liquide de
    frein dans le bocal - Si correcteur de charge : vérifier le réglage de la tige de liaison (jeu conforme au constructeur)
    - Pomper la pédale de frein : fermeté après 3 à 5 appuis Essai routier progressif - Freinage doux à 10 km/h : le véhicule
    doit freiner droit sans blocage arrière - Freinage appuyé à 50 km/h : l''arrière ne doit pas décrocher avant l''avant
    - Freinage d''urgence sur route dégagée : répartition correcte (pas de survirage au freinage) ⚠️ Arrêter immédiatement
    si : blocage des roues arrière avant les avant, pédale molle, fuite de liquide, tirage au freinage.'
  S7: Quel est le prix d'un répartiteur de frein ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur pour
    trouver le répartiteur de frein compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon répartiteur de frein est à changer ?Les signes d'usure les plus courants sont détaillés dans la section
    diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un répartiteur
    de frein défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule.
    Consultez la section symptômes pour évaluer l'urgence du remplacement. - Maître-cylindre de frein — source de pression
    en amont du répartiteur - Cylindre de roue — récepteur de pression en aval (freins à tambour) - Flexible de frein — liaison
    souple entre le répartiteur et les roues - Mâchoires de frein — garnitures de friction dans les tambours arrière - Tambour
    de frein — surface de friction des mâchoires
  S8: 'Répartiteur et correcteur de freinage, est-ce la même chose ? Non. Le répartiteur fixe dose la pression selon un ratio
    prédéfini (ex : 60/40 avant/arrière). Le correcteur de charge (compensateur) ajuste dynamiquement la pression arrière
    selon la charge du véhicule via une tige reliée à l''essieu. Les véhicules modernes avec ABS n''ont souvent plus ni l''un
    ni l''autre : le calculateur ABS gère la répartition électroniquement. Mon véhicule a l''ABS, a-t-il quand même un répartiteur
    ? Les véhicules récents avec ABS n''ont généralement plus de répartiteur mécanique. L''ABS module la pression roue par
    roue. Certains véhicules plus anciens (ABS première génération) conservent un correcteur de charge en complément de l''ABS.
    Comment diagnostiquer un répartiteur défaillant ? Symptômes : l''arrière bloque bien avant l''avant au freinage (répartiteur
    bloqué ouvert) ou l''arrière ne freine plus (répartiteur bloqué fermé). Sur route mouillée, le véhicule part en tête-à-queue
    au freinage. Un contrôle au freinomètre révèle un déséquilibre avant/arrière. Puis-je supprimer le répartiteur ? Non.
    Sans répartiteur, la pression pleine arrive aux roues arrière, qui bloqueraient systématiquement au freinage (poids transféré
    sur l''avant). C''est extrêmement dangereux et interdit par la réglementation. Le correcteur de charge se dérègle-t-il
    avec le temps ? Oui. La tige de liaison se corrode ou se déforme, et les ressorts de suspension s''affaissent. Un correcteur
    mal réglé dose mal la pression arrière. Le réglage doit être vérifié à chaque changement de ressorts ou d''amortisseurs
    arrière.'
  META: 'Guide complet pour remplacer votre répartiteur de frein : compatibilité, réglage du correcteur de charge, purge et
    FAQ répartition freinage.'
---

# Répartiteur de frein - Guide Diagnostic Complet

## Fonction et Rôle

Repartir la pression de freinage entre les essieux

**Actions principales:** repartir, distribuer, equilibrer

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Roues arriere qui bloquent trop tot au freinage**
  roues arriere qui bloquent trop tot au freinage

### 🟡 Symptômes de Sécurité

- **Freinage desequilibre avant arriere**
  freinage desequilibre avant arriere
- **Desequilibre freinage controle technique valeurs**
  desequilibre freinage controle technique valeurs

### 🟢 Autres Symptômes

- fuite au niveau du repartiteur
- echec au controle technique desequilibre

## Procédure de Diagnostic

Pour diagnostiquer un problème de répartiteur de frein:

1. **Inspection visuelle** - Examiner l'état du répartiteur de frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le répartiteur de frein peut être hors service et nécessiter un remplacement
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- maitre-cylindre-de-frein
- flexible-de-frein

## Critères de Compatibilité

Pour commander le bon répartiteur de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "freinage garanti"

## FAQ

**À quoi sert le répartiteur de frein ?**
Il dose la pression envoyée aux freins arrière pour éviter le blocage. Sur les véhicules modernes avec ABS, cette fonction est souvent électronique (EBD).

**Mon véhicule a-t-il un répartiteur mécanique ?**
Les véhicules sans ABS ont généralement un répartiteur mécanique ou compensateur de charge. Avec ABS/EBD, la répartition est gérée électroniquement.

**Quels sont les symptômes d'un répartiteur défaillant ?**
Blocage prématuré des roues arrière au freinage, déséquilibre constaté au contrôle technique, ou fuite de liquide au niveau du répartiteur.

**Quelles sont les erreurs fréquentes à éviter ?**
Diagnostiquer 'répartiteur HS' sur véhicule ABS alors que la répartition est électronique (EBD). Confondre blocage arrière avec pneus/pression/amortisseurs fatigués.

**Comment faire un diagnostic rapide ?**
Véhicule sans ABS + arrière qui bloque → répartiteur/correcteur à suspecter. Fuite sous caisse près essieu AR → répartiteur possible. Avec ABS : chercher d'abord défaut capteurs/diag.


## References supplementaires

<!-- materialized-from-db manual/b45db7af3e98 2026-04-02 -->
### Données techniques OEM — Montage maitrise

# Données techniques OEM — Montage maitrise
Source : ate-freinage.fr (1 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- hydraulique

## Matériaux
- acier inoxydable
- aluminium
- fonte grise

## Valeurs techniques de référence
- 50 %
