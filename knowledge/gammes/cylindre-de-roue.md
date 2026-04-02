---
category: freinage
slug: cylindre-de-roue
title: Cylindre de roue
pg_id: 277
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
  role: Transmettre la pression hydraulique aux machoires
  must_be_true:
  - pousser les machoires
  - transmettre la pression
  - actionner le freinage tambour
  must_not_contain:
  - disque
  - etrier
  - plaquette
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
  - ❌ "freinage direct"
  cost_range:
    min: 31
    max: 41
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Pièce OE (Origine Équipement)
    description: Cylindre conforme aux spécifications constructeur. Étanchéité haute et basse pression testée. Matériaux résistant
      à la chaleur et aux fluides de frein.
  - tier: Équivalent OE (spécialistes freinage)
    description: Fabricants de freinage reconnus appliquant des normes de résistance plus sévères que les prescriptions légales.
      Longévité exceptionnelle documentée.
  - tier: Kit réparation (pistons + joints)
    description: Option économique si le corps du cylindre n est pas rayé ni corrodé. Le cylindre neuf reste plus fiable.
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
    label: Traces de liquide sur le dos des machoires
    severity: confort
  - id: S2
    label: Interieur du tambour mouille ou gras
    severity: confort
  - id: S3
    label: Niveau de liquide de frein qui baisse
    severity: securite
  - id: S4
    label: Freinage arriere desequilibre
    severity: securite
  - id: S5
    label: Machoires usees de facon asymetrique
    severity: confort
  - id: S6
    label: Fuite visible au niveau du cylindre
    severity: confort
  - id: S7
    label: Bruit de frottement a l arriere
    severity: confort
  - id: S8
    label: Odeur de liquide de frein pres des roues arriere
    severity: securite
  - id: S9
    label: Plus de 100 000 km sans controle des cylindres
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - remplacement preventif recommande
  depose_steps: []
  quick_checks:
  - 'Observer : traces de liquide sur le dos des machoires ?'
  - 'Observer : interieur du tambour mouille ou gras ?'
  - 'Observer : niveau de liquide de frein qui baisse ?'
  - 'Observer : freinage arriere desequilibre ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Traces de liquide sur le dos des machoires
  - Interieur du tambour mouille ou gras
  - Niveau de liquide de frein qui baisse
  - Freinage arriere desequilibre
  - Machoires usees de facon asymetrique
  - Fuite visible au niveau du cylindre
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '277'
  intro_title: A quoi sert Cylindre de roue ?
  risk_title: Pourquoi remplacer Cylindre de roue a temps ?
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
  - question: Cylindre de roue neuf ou kit réparation ?
    answer: Le cylindre neuf est plus fiable. Le kit réparation (pistons + joints) convient si le corps du cylindre n'est
      pas rayé ou corrodé.
  - question: Comment savoir si mon cylindre de roue fuit ?
    answer: Traces de liquide sur le dos des mâchoires, intérieur du tambour mouillé, niveau de liquide qui baisse, mâchoire
      d'un côté plus usée.
  - question: Tous les combien changer les cylindres de roue ?
    answer: Pas de périodicité fixe. À remplacer dès qu'une fuite apparaît. Contrôle visuel à chaque changement de mâchoires.
  - question: Peut-on changer un cylindre de roue soi-même ?
    answer: Oui. Dépose du tambour et des mâchoires nécessaire. Purge obligatoire après. Comptez 1h par côté.
  - question: Quelle erreur éviter avec les cylindres de roue ?
    answer: Ne pas rouler avec un cylindre qui fuit (liquide sur garnitures = perte de freinage). Changer par paire recommandé.
      Purger correctement.
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
doc_id: 72f1447f-0444-5ead-bca4-0180a01ca8f6
content_hash: sha256:20a9288c7215cbec
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
  _source: ate-freinage.fr + delphiautoparts.com + textar.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 7
  _has_tech_data: true
  types_variants:
  - type: 'hydraulique'
    source_ref: corpus RAG web OEM
  technical_notes:
    norme_dot_5.1: 'DOT 5.1'
    norme_fmvss_§571.116_(dot_3: 'FMVSS §571.116 (DOT 3'
    norme_sae_j1703: 'SAE J1703'
    val_0_5__: '0,5 %'
    val_100__: '100 %'
    val_100_a: '100 a'
    val_6__a: '6. A'
    val_68_a: '68 a'
    val_7_a: '7 a'
    val_882_a: '882 a'
  materials:
  - materiau: 'EPDM'
    source_ref: corpus RAG web OEM
  - materiau: 'aluminium'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le cylindre de roue est constitué d''un cylindrequi comporte deux pistons, un de chaque côté. Chaque piston a un jointd''étanchéité
    en caoutchouc et un tuyau qui relie le piston à la mâchoire defrein de la voiture. Le cylindre de roue écarte le jeu de
    mâchoires de frein qui frottent alors sur le tambour solidaire àla roue, ce qui provoque le ralentissement de la voiture.
    Les cylindres de rouesont reliés directement au circuit hydraulique de freinage par les flexibles defrein de la voiture.
    Certains cylindres de roue ont un système de rattrapage automatiqueincorporé appelé aussi « à compensateur intégré ».
    En savoir plus : cylindre de roue — définition et rôle mécanique 🚨 Bruit Cylindre de roue : causes et diagnostic'
  S2: 'Ne pas attendre la panne complete pour intervenir. Symptômes d''usure : - Traces de liquide sur le dos des machoires
    - Interieur du tambour mouille ou gras - Niveau de liquide de frein qui baisse - Freinage arriere desequilibre - Machoires
    usees de facon asymetrique - Fuite visible au niveau du cylindre - Bruit de frottement a l arriere - Odeur de liquide
    de frein pres des roues arriere - Plus de 100 000 km sans controle des cylindres - Sécurité maximale Contrôles complets
    : - Étanchéité à basse et haute pression - Résistance à l’usure - Norme N plus sévère que les prescriptions légales -
    Fabrication conforme aux normes environnementales ISO1400'
  S3: 'Pour choisir les bons cylindre de roue pour votre véhicule : - Marque de votre véhicule - Modele de votre véhicule
    - Annee de votre véhicule - Vérifier : traces de liquide sur le dos des machoires - Vérifier : interieur du tambour mouille
    ou gras - Vérifier : niveau de liquide de frein qui baisse - Vérifier : freinage arriere desequilibre - Vérifier : machoires
    usees de facon asymetrique - Vérifier : fuite visible au niveau du cylindre - Vérifier : bruit de frottement a l arriere
    - Vérifier : odeur de liquide de frein pres des roues arrierePour aller plus loin : consultez notre guide d''achat cylindre
    de roue — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: '1. # Maîtres-cylindres, cylindres de roue et cylindres récepteurs - Accueil Pièces Freinage Freinage Maîtres-cylindres,
    cylindres de roue et cylindres récepteurs Maîtres-cylindres, cylindres de roue et cylindres récepteurs En termes simples,
    le maître-cylindre génère une pression hydraulique qui est... 2. Comment changer un compresseur de climatisation de voiture
    : guide étape par étape'
  S4_REPOSE: '- Vérifier que le cylindre de roue neufest identique à celui démonté. - Contrôlez si le câble de frein à main
    est grippé et le remplacé sinécessaire. - Contrôlez l''état d''usure du tambour de frein gauche ou droit et le remplacé
    si nécessaire. - Nettoyer le flasque de frein à l''aide d''un nettoyant defrein. - Graissez tous le cylindre de roue.
    - Mettre en place le cylindre de roue. - Remontez la fixation du cylindre de roue. - Appuyez à plusieurs reprise sur la
    pédale de frein jusqu''à elle devient dure. - Accouplez la canalisation du cylindre de roue. - Remontez les mâchoires
    de frein du véhicule. - Remontez la roue. ✅ Après remontage, vérifiez les spécifications dans la fiche technique Cylindre
    de roue.'
  S5: 'Erreurs frequentes avec le cylindre de roue : - Ne pas purger le circuit de frein apres remplacement — l''air dans
    le circuit rend la pedale molle et le freinage arriere inefficace- Oublier de verifier l''etat des machoires de frein
    — des machoires usees endommagent le cylindre neuf par frottement anormal- Ne pas nettoyer le flasque de frein avant montage
    — la rouille et les debris empechent le cylindre de coulisser correctement- Ignorer une fuite de liquide de frein derriere
    la roue arriere — signe de joints de cylindre uses, le freinage arriere se degrade progressivement- Remplacer un seul
    cylindre au lieu des deux (essieu arriere) — l''effort de freinage devient asymetrique et le vehicule tire d''un cote-
    Ne pas regler le frein a main apres remplacement — le rattrapage de jeu des machoires doit etre fait pour que le frein
    de parking soit efficace'
  S6: 'Contrôles statiques - Vérifier l''absence de fuite au raccord hydraulique et autour des soufflets de piston - Contrôler
    le niveau de liquide de frein dans le bocal (compléter après purge) - Vérifier que le tambour tourne librement (pas de
    freinage résiduel) - Tester le frein à main : blocage en 3 à 5 clics - Pomper la pédale : elle doit devenir ferme après
    4 à 6 appuis Essai routier progressif - Freinage doux à 10 km/h sur parking, vérifier que le véhicule freine droit - Augmenter
    à 30 puis 50 km/h avec des freinages normaux - Après 5 km, s''arrêter et vérifier l''absence de fuite au niveau du cylindre
    neuf ⚠️ Arrêter immédiatement si : pédale molle ou qui s''enfonce, fuite de liquide visible, tirage d''un côté, frein
    à main inopérant. 🚨 Bruit Cylindre de roue : causes et diagnostic'
  S_GARAGE: 'Nous vous recommandons de confier cette intervention à un professionnel : - Plusieurs causes possibles de défaillance
    (3 identifiées) nécessitent un diagnostic professionnel Un garagiste qualifié dispose de l''outillage et de l''expérience
    nécessaires pour effectuer cette opération en toute sécurité.'
  S7: Quel est le prix d'un cylindre de roue ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur pour
    trouver le cylindre de roue compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon cylindre de roue est à changer ?Les signes d'usure les plus courants sont détaillés dans la section diagnostic
    ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un cylindre de roue défaillant
    ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule. Consultez la section
    symptômes pour évaluer l'urgence du remplacement.- cable de frein a main - disque de frein - etrier de frein - flexible
    de frein - kit de freins arriere - machoires de frein - plaquette de frein - tambour de frein
  S8: Cylindre de roue neuf ou kit réparation ?Le cylindre neuf est plus fiable. Le kit réparation (pistons + joints) convient
    si le corps du cylindre n'est pas rayé ou corrodé. Comment savoir si mon cylindre de roue fuit ?Traces de liquide sur
    le dos des mâchoires, intérieur du tambour mouillé, niveau de liquide qui baisse, mâchoire d'un côté plus usée. Tous les
    combien changer les cylindres de roue ?Pas de périodicité fixe. À remplacer dès qu'une fuite apparaît. Contrôle visuel
    à chaque changement de mâchoires. Peut-on changer un cylindre de roue soi-même ?Oui. Dépose du tambour et des mâchoires
    nécessaire. Purge obligatoire après. Comptez 1h par côté. Quelle erreur éviter avec les cylindres de roue ?Ne pas rouler
    avec un cylindre qui fuit (liquide sur garnitures = perte de freinage). Changer par paire recommandé. Purger correctement.
  META: 'Guide complet pour remplacer votre cylindre de roue : compatibilité, purge du circuit, erreurs à éviter et FAQ pour
    un freinage arrière fiable.'
---

# Cylindre de roue - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre la pression hydraulique aux machoires

**Actions principales:** pousser les machoires, transmettre la pression, actionner le freinage tambour, ecarter, commander

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Niveau de liquide de frein qui baisse**
  niveau de liquide de frein qui baisse
- **Freinage arriere desequilibre**
  freinage arriere desequilibre
- **Odeur de liquide de frein pres des roues arriere**
  odeur de liquide de frein pres des roues arriere

### 🟢 Autres Symptômes

- traces de liquide sur le dos des machoires
- interieur du tambour mouille ou gras
- machoires usees de facon asymetrique
- fuite visible au niveau du cylindre
- bruit de frottement a l arriere
- plus de 100 000 km sans controle des cylindres

## Procédure de Diagnostic

Pour diagnostiquer un problème de cylindre de roue:

1. **Inspection visuelle** - Examiner l'état du cylindre de roue
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
- disque-de-frein
- etrier-de-frein
- flexible-de-frein
- kit-de-freins-arriere
- machoires-de-frein
- plaquette-de-frein
- tambour-de-frein

## Critères de Compatibilité

Pour commander le bon cylindre de roue, vous devez connaître:

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

**Cylindre de roue neuf ou kit réparation ?**
Le cylindre neuf est plus fiable. Le kit réparation (pistons + joints) convient si le corps du cylindre n'est pas rayé ou corrodé.

**Comment savoir si mon cylindre de roue fuit ?**
Traces de liquide sur le dos des mâchoires, intérieur du tambour mouillé, niveau de liquide qui baisse, mâchoire d'un côté plus usée.

**Tous les combien changer les cylindres de roue ?**
Pas de périodicité fixe. À remplacer dès qu'une fuite apparaît. Contrôle visuel à chaque changement de mâchoires.

**Peut-on changer un cylindre de roue soi-même ?**
Oui. Dépose du tambour et des mâchoires nécessaire. Purge obligatoire après. Comptez 1h par côté.

**Quelle erreur éviter avec les cylindres de roue ?**
Ne pas rouler avec un cylindre qui fuit (liquide sur garnitures = perte de freinage). Changer par paire recommandé. Purger correctement.
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


## References supplementaires

<!-- materialized-from-db manual/447c92041150 2026-04-02 -->
### Données techniques OEM — Montage maitrise

# Données techniques OEM — Montage maitrise
Source : ate-freinage.fr + delphiautoparts.com (6 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- hydraulique

## Normes applicables
- DOT 5.1
- FMVSS §571.116 (DOT 3
- SAE J1703

## Matériaux
- EPDM
- aluminium

## Valeurs techniques de référence
- 0,5 %
- 100 %

## Symptomes supplementaires

<!-- materialized-from-db diagnostic/freinage/vibration-au-freinage.md 2026-01-01 -->
### Diagnostic - Vibrations véhicule

# Vibrations véhicule - Diagnostic complet

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

## Arbre de décision

```
Vibration ?
├── Au volant ?
│   ├── À haute vitesse → Équilibrage / Géométrie
│   ├── Au freinage → Disques voilés
│   └── En virage → Roulement / Cardan
├── Dans l'habitacle ?
│   ├── Au ralenti → Supports moteur
│   ├── En accélération → Cardan / Transmission
│   └── Constant → Pneus / Roulements
└── Pédale de frein ?
    └── Au freinage → Disques voilés
```

<!-- materialized-from-db diagnostic/bruits-freinage.md 2026-01-01 -->
### Diagnostic - Bruits de freinage

# Bruits de freinage - Diagnostic complet

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
