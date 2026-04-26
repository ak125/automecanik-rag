---
category: freinage
slug: etrier-de-frein
title: Étrier de frein
pg_id: 78
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
  role: Appliquer la pression hydraulique sur les plaquettes
  must_be_true:
  - appliquer la pression
  - maintenir les plaquettes
  - serrer
  must_not_contain:
  - tambour
  - machoire
  - thermique
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - disque-de-frein
  - plaquette-de-frein
  - flexible-de-frein
  - maitre-cylindre-de-frein
  - liquide-de-frein
  - tambour-de-frein
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
  - ❌ "freinage direct"
  cost_range:
    min: 68
    max: 262
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Pièce OE (Origine Équipement)
    description: Étrier identique à l origine. Matériaux conformes (aluminium recyclé, semi-solid metalforming sur certains
      véhicules récents). Poids optimisé.
  - tier: Équivalent OE (spécialistes freinage)
    description: Fabricants spécialisés en freinage soumettant leurs étriers à des tests de contrainte et simulations avant
      commercialisation.
  - tier: Reconditionné certifié (échange standard)
    description: 'Programme de reconditionnement avec contrôle OE : chaque étrier repris est contrôlé et retraité selon des
      critères précis. Qualité OE contrôlée à prix réduit.'
  - tier: Générique non qualifié
    description: Non recommandé sur un composant de sécurité active. Qualité des matériaux non vérifiable.
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
    label: Usure asymetrique plaquettes plus usee
    severity: confort
  - id: S2
    label: Vehicule qui tire d un cote au freinage
    severity: securite
  - id: S3
    label: Roue anormalement chaude apres roulage
    severity: confort
  - id: S4
    label: Fuite de liquide de frein au niveau de l etrier
    severity: securite
  - id: S5
    label: Pedale de frein dure ou spongieuse
    severity: securite
  - id: S6
    label: Bruit de frottement permanent piston grippe
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - remplacement preventif recommande
  depose_steps: []
  quick_checks:
  - 'Observer : usure asymetrique plaquettes plus usee ?'
  - 'Observer : vehicule qui tire d un cote au freinage ?'
  - 'Observer : roue anormalement chaude apres roulage ?'
  - Fuite de liquide de frein au niveau de l etrier ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Usure asymetrique plaquettes plus usee
  - Vehicule qui tire d un cote au freinage
  - Roue anormalement chaude apres roulage
  - Fuite de liquide de frein au niveau de l etrier
  - Pedale de frein dure ou spongieuse
  - Bruit de frottement permanent piston grippe
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '78'
  intro_title: A quoi sert Étrier de frein ?
  risk_title: Pourquoi remplacer Étrier de frein a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
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
  - question: Étrier neuf ou échange standard ?
    answer: L'échange standard est 30-50% moins cher et de qualité équivalente. Vérifiez la consigne et l'état du noyau à
      retourner.
  - question: Comment savoir si mon étrier est grippé ?
    answer: Usure asymétrique des plaquettes (une seule usée), véhicule qui tire d'un côté au freinage, roue anormalement
      chaude après roulage.
  - question: Faut-il purger après changement d'étrier ?
    answer: Oui obligatoirement. Le circuit a été ouvert, de l'air est entré. Purgez par gravité ou avec un purgeur automatique.
  - question: Peut-on réparer un étrier grippé ?
    answer: Parfois, en changeant le kit de réparation (piston + joints). Mais souvent plus rentable de remplacer l'étrier
      complet.
  - question: Quelle erreur éviter avec les étriers ?
    answer: Ne jamais appuyer sur la pédale de frein étrier déposé (piston éjecté). Ne pas tordre le flexible. Graisser les
      coulisseaux.
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
doc_id: 477ee8f5-6701-511a-8334-cad107e1bfc1
content_hash: sha256:bcf05482404e31d1
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
  _source: aftermarket.zf.com + ate-freinage.fr + bremboparts.com + delphiautoparts.com + ferodo.com + gpa26.com + profauto.fr
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 34
  _has_tech_data: true
  types_variants:
  - type: 'Composite'
    source_ref: corpus RAG web OEM
  - type: 'composite'
    source_ref: corpus RAG web OEM
  - type: 'céramique'
    source_ref: corpus RAG web OEM
  - type: 'hydraulique'
    source_ref: corpus RAG web OEM
  - type: 'pneumatique'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    norme_ece_r90: 'ECE R90'
    norme_sae_j2521: 'SAE J2521'
    val_0_035_mm: '0,035 mm'
    val_0_05_mm: '0,05 mm'
    val_0_1_mm: '0,1 mm'
    val_000_km: '000 km'
    val_1_5_mm: '1,5 mm'
    val_1__v: '1. V'
    val_10__m: '10 µm'
    val_100__: '100 %'
    val_100_a: '100 a'
    val_110_nm: '110 Nm'
    val_115_nm: '115 Nm'
    val_120_nm: '120 Nm'
    val_2_a: '2 a'
    val_2_mm: '2 mm'
    val_200_km: '200 km'
  materials:
  - materiau: 'EPDM'
    source_ref: corpus RAG web OEM
  - materiau: 'HNBR'
    source_ref: corpus RAG web OEM
  - materiau: 'acier inoxydable'
    source_ref: corpus RAG web OEM
  - materiau: 'aluminium'
    source_ref: corpus RAG web OEM
  - materiau: 'céramique'
    source_ref: corpus RAG web OEM
  - materiau: 'fonte grise'
    source_ref: corpus RAG web OEM
  - materiau: 'graphite'
    source_ref: corpus RAG web OEM
  - materiau: 'silicone'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Lesétriers de frein jouent le rôle de support et de guide dans le circuit defreinage également composé des plaquettesde
    frein avant ou arrière et des pistons del''étrier. Les étriers de frein transforment l''huile du circuit hydraulique enénergie
    mécanique, qui permet ensuite aux pistons de pousser les plaquettes de frein gauche ou droite surle disque de frein gauche
    ou droit pour ralentirou de freiner le véhicule. Ilexiste deux types d''étrier de frein : - L''étrier de frein flottant
    (coulissant) : Seule laplaquette intérieure est poussée contre le disque de frein de la voiture par un ou plusieurs pistons.La
    plaquette extérieure subit la pression grâce à un système coulissant reliantles deux plaquettes. L''étrier flottant est
    le système de freinage le plusconnu. - L''étrier de frein fixe : Le pincement des plaquettesde frein de la voiture sur
    le disque de frein se fait à l''aide d''un ou plusieurs pistons qui sontsitués de part et d''autre du disque. Généralement
    l''étrier fixe est utilisé surles voitures performantes. En savoir plus : étrier de frein — définition et rôle mécanique
    🚨 Bruit Étrier de frein : causes et diagnostic'
  S2: 'Ne pas attendre la panne complete pour intervenir. Symptômes d''usure : - Usure asymetrique plaquettes plus usee -
    Vehicule qui tire d un cote au freinage - Roue anormalement chaude apres roulage - Fuite de liquide de frein au niveau
    de l etrier - Pedale de frein dure ou spongieuse - Bruit de frottement permanent piston grippe'
  S2_DIAG: 'SymptômeCause probableActionUsure asymetrique plaquettes plus useelocaliser source et verifier usure mecaniqueObserver
    : usure asymetrique plaquettes plus usee ?Vehicule qui tire d un cote au freinageidentifier origine fuite et verifier
    jointsObserver : vehicule qui tire d un cote au freinage ?Roue anormalement chaude apres roulageremplacement preventif
    recommandeObserver : roue anormalement chaude apres roulage ?Fuite de liquide de frein au niveau de l etrierlocaliser
    source et verifier usure mecaniqueFuite de liquide de frein au niveau de l etrier ?Pedale de frein dure ou spongieuselocaliser
    source et verifier usure mecaniqueObserver : usure asymetrique plaquettes plus usee ?Bruit de frottement permanent piston
    grippelocaliser source et verifier usure mecaniqueObserver : usure asymetrique plaquettes plus usee ?'
  S3: 'Pour choisir les bons etrier de frein pour votre véhicule : - Marque de votre véhicule - Modele de votre véhicule -
    Annee de votre véhicule - Vérifier : usure asymetrique plaquettes plus usee - Vérifier : vehicule qui tire d un cote au
    freinage - Vérifier : roue anormalement chaude apres roulage - Vérifier : fuite de liquide de frein au niveau de l etrier
    - Vérifier : pedale de frein dure ou spongieuse - Vérifier : bruit de frottement permanent piston grippePour aller plus
    loin : consultez notre guide d''achat étrier de frein — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 1. Desserrez les boulons de roue, levez et calez le véhicule sur chandelles. 2. Démontez la roue. 3. Débranchez
    le connecteur du capteur d'usure de plaquettes (si équipé). 4. Débranchez le flexible de frein de l'étrier (préparez un
    bouchon ou pincez le flexible pour limiter la perte de liquide). 5. Dévissez les deux vis de fixation de l'étrier (colonnettes
    ou vis de support). 6. Retirez l'étrier et les plaquettes. 7. Nettoyez le support d'étrier et les glissières au nettoyant
    frein.
  S4_REPOSE: 'Le remontage de l''étrier de frein est une opération de sécurité : une purge incomplète, un piston mal repoussé
    ou un flexible tordu peuvent provoquer un freinage asymétrique ou une perte de pression hydraulique au premier freinage
    d''urgence. Respectez l''ordre des étapes ci-dessous sans improvisation. - Vérifiez que l''étrier neuf (ou reconditionné)
    est identique à celui déposé : position du flexible, sens de montage, diamètre du piston. Ne montez jamais l''étrier gauche
    à droite. - Contrôlez l''état d''usure des disques de frein et des plaquettes : si l''épaisseur résiduelle est inférieure
    aux cotes constructeur, remplacez-les simultanément pour conserver l''équilibre de freinage. - Nettoyez le porte-étrier
    et les glissières avec un nettoyant frein. Appliquez de la graisse haute température spécifique étrier sur les glissières
    et les portées de plaquettes — sans jamais en mettre sur les surfaces de friction. - Repoussez le piston de l''étrier
    complètement dans son logement avec un repousse-piston ou un outil à cames (étriers arrière à vis). Gardez le bouchon
    du maître- cylindre entrebâillé pour éviter la surpression dans le circuit. - Installez les plaquettes de frein neuves
    dans le porte-étrier en vérifiant le bon engagement des ressorts anti-bruit et des cales de plaquettes. - Posez l''étrier
    sur le porte-étrier et serrez les colonnettes de guidage au couple préconisé (typiquement 25 à 35 N·m pour les colonnettes,
    100 à 120 N·m pour les vis de fixation de l''étrier selon le modèle). - Reconnectez le flexible de frein sur l''étrier
    sans le vriller. Serrez le raccord au couple (15 à 17 N·m). Si le flexible est craquelé ou tordu, remplacez-le maintenant.
    - Resserrez le câble de frein à main sur l''étrier arrière si déposé, et ajustez la tension selon les préconisations.
    - Purgez le circuit de freinage par la vis de purge de l''étrier : appuyez lentement sur la pédale, ouvrez la vis, fermez
    avant de relâcher. Répétez jusqu''à un jet de liquide sans bulle. Maintenez le niveau dans le bocal tout au long de la
    purge. - Remontez la roue, descendez le véhicule et serrez les écrous de roue en croix au couple (110 à 130 N·m selon
    véhicule). Effectuez 5 à 6 freinages progressifs depuis 50 km/h avant tout freinage d''urgence pour permettre le rodage
    des plaquettes. ✅ Après remontage, vérifiez les spécifications dans la fiche technique Étrier de frein.'
  S5: '- ❌ "homologué CT" - ❌ "sécurité garantie" - ❌ "zéro panne" - ❌ "garanti à vie" - ❌ "freinage direct"'
  S6: 'Contrôles statiques - Vérifier le serrage de toutes les vis de fixation (colonnettes et support) au couple constructeur
    - Contrôler l''absence de fuite au raccord du flexible de frein et autour du piston - Vérifier le niveau de liquide de
    frein dans le bocal (compléter si nécessaire après purge) - Vérifier que le flexible n''est ni tordu, ni en contact avec
    un élément mobile (disque, roue) - Pomper la pédale de frein : elle doit devenir ferme après 3 à 5 appuis Essai routier
    progressif - Démarrer sur un parking : freinage doux à 10 km/h, vérifier que le véhicule freine droit - Augmenter progressivement
    : 30, 50, puis 70 km/h avec des freinages normaux - Vérifier l''absence de tirage latéral (le véhicule ne doit pas dévier
    au freinage) - Après 2-3 km, s''arrêter et toucher les jantes : les deux côtés doivent être à température similaire ⚠️
    Arrêter immédiatement si : pédale molle ou qui s''enfonce, tirage net d''un côté, fuite de liquide visible, odeur de brûlé
    localisée sur une roue, surchauffe d''une jante. 🚨 Bruit Étrier de frein : causes et diagnostic'
  S_GARAGE: 'Nous vous recommandons de confier cette intervention à un professionnel : - Plusieurs causes possibles de défaillance
    (3 identifiées) nécessitent un diagnostic professionnel Un garagiste qualifié dispose de l''outillage et de l''expérience
    nécessaires pour effectuer cette opération en toute sécurité.'
  S7: Quel est le prix d'un étrier de frein ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur pour trouver
    l'étrier de frein compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment savoir si
    l'étrier de frein est à changer ?Les signes d'usure les plus courants sont détaillés dans la section diagnostic ci- dessus.
    En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un étrier de frein défaillant ?Cela
    dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule. Consultez la section symptômes
    pour évaluer l'urgence du remplacement.- cable de frein a main - capteur abs - disque de frein - flexible de frein - interrupteur
    des feux de freins - maitre cylindre de frein - plaquette de frein - servo frein
  S8: Étrier neuf ou échange standard ?L'échange standard est 30-50% moins cher et de qualité équivalente. Vérifiez la consigne
    et l'état du noyau à retourner. Comment savoir si mon étrier est grippé ?Usure asymétrique des plaquettes (une seule usée),
    véhicule qui tire d'un côté au freinage, roue anormalement chaude après roulage. Faut-il purger après changement d'étrier
    ?Oui obligatoirement. Le circuit a été ouvert, de l'air est entré. Purgez par gravité ou avec un purgeur automatique.
    Peut-on réparer un étrier grippé ?Parfois, en changeant le kit de réparation (piston + joints). Mais souvent plus rentable
    de remplacer l'étrier complet. Quelle erreur éviter avec les étriers ?Ne jamais appuyer sur la pédale de frein étrier
    déposé (piston éjecté). Ne pas tordre le flexible. Graisser les coulisseaux.
  META: 'Guide complet pour remplacer vos étriers de frein : erreurs à éviter, vérification après montage, purge du circuit
    et FAQ pour un freinage sûr.'
---

# Étrier de frein - Guide Diagnostic Complet

## Fonction et Rôle

Appliquer la pression hydraulique sur les plaquettes

**Actions principales:** appliquer la pression, maintenir les plaquettes, serrer, relacher, pincer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Vehicule qui tire d un cote au freinage**
  vehicule qui tire d un cote au freinage
- **Fuite de liquide de frein au niveau de l etrier**
  fuite de liquide de frein au niveau de l etrier
- **Pedale de frein dure ou spongieuse**
  pedale de frein dure ou spongieuse

### 🟢 Autres Symptômes

- usure asymetrique plaquettes plus usee
- roue anormalement chaude apres roulage
- bruit de frottement permanent piston grippe

## Procédure de Diagnostic

Pour diagnostiquer un problème de étrier de frein:

1. **Inspection visuelle** - Examiner l'état du étrier de frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- cable-de-frein-a-main
- capteur-abs
- disque-de-frein
- flexible-de-frein
- interrupteur-des-feux-de-freins
- maitre-cylindre-de-frein
- plaquette-de-frein
- servo-frein

## Critères de Compatibilité

Pour commander le bon étrier de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "freinage direct"

## FAQ

**Étrier neuf ou échange standard ?**
L'échange standard est 30-50% moins cher et de qualité équivalente. Vérifiez la consigne et l'état du noyau à retourner.

**Comment savoir si mon étrier est grippé ?**
Usure asymétrique des plaquettes (une seule usée), véhicule qui tire d'un côté au freinage, roue anormalement chaude après roulage.

**Faut-il purger après changement d'étrier ?**
Oui obligatoirement. Le circuit a été ouvert, de l'air est entré. Purgez par gravité ou avec un purgeur automatique.

**Peut-on réparer un étrier grippé ?**
Parfois, en changeant le kit de réparation (piston + joints). Mais souvent plus rentable de remplacer l'étrier complet.

**Quelle erreur éviter avec les étriers ?**
Ne jamais appuyer sur la pédale de frein étrier déposé (piston éjecté). Ne pas tordre le flexible. Graisser les coulisseaux.
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
