---
category: freinage
slug: machoires-de-frein
title: Mâchoires de frein
pg_id: 70
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-25'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v4_converted
  last_enriched_by: script:rag-fill-remaining-gaps
  last_enriched_at: '2026-03-28'
domain:
  role: Creer la friction a l'interieur du tambour
  must_be_true:
  - frotter
  - exercer une pression interne
  - s'user progressivement
  must_not_contain:
  - disque
  - plaquette
  - etrier
  - ventile
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
  - ❌ "remplacement plaquettes"
  cost_range:
    min: 20
    max: 80
    currency: EUR
    unit: l'unite
    source: estimation categorie
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE (OES)
  - tier: Adaptable qualite
  - tier: Reconditionne
  - tier: Echange standard
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
    label: Frein a main qui ne tient plus ou mal
    severity: securite
  - id: S2
    label: Bruit de frottement metallique a l arriere
    severity: confort
  - id: S3
    label: Tambour raye ou strie a l interieur
    severity: confort
  - id: S4
    label: Epaisseur de garniture inferieure a 2mm
    severity: confort
  - id: S5
    label: Freinage arriere desequilibre tire d un cote
    severity: securite
  - id: S6
    label: Poussiere frein noire excessive jantes
    severity: securite
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : frein a main qui ne tient plus ou mal'
  depose_steps: []
  quick_checks:
  - 'Observer : frein a main qui ne tient plus ou mal ?'
  - Bruit de frottement metallique a l arriere ?
  - 'Observer : tambour raye ou strie a l interieur ?'
  - 'Observer : epaisseur de garniture inferieure a 2mm ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Frein a main qui ne tient plus ou mal
  - Bruit de frottement metallique a l arriere
  - Tambour raye ou strie a l interieur
  - Epaisseur de garniture inferieure a 2mm
  - Freinage arriere desequilibre tire d un cote
  - Poussiere frein noire excessive jantes
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '70'
  intro_title: A quoi sert Mâchoires de frein ?
  risk_title: Pourquoi remplacer Mâchoires de frein a temps ?
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
  - question: 'Mâchoires OE ou adaptables : que choisir ?'
    answer: Les mâchoires OES (TRW, Bosch, Valeo) offrent d excellentes performances. Vérifiez le diamètre du tambour et la
      largeur des garnitures.
  - question: Comment savoir si mes mâchoires sont usées ?
    answer: Frein à main inefficace, bruit de frottement métallique à l arrière, tambour rayé à l intérieur, épaisseur de
      garniture inférieure à 2mm.
  - question: Tous les combien changer les mâchoires ?
    answer: Entre 80 000 et 120 000 km en moyenne. Les mâchoires arrière sont moins sollicitées que le freinage avant, d où
      leur durée de vie supérieure.
  - question: Peut-on changer ses mâchoires soi-même ?
    answer: Oui mais opération technique. Il faut déposer le tambour et les ressorts. Comptez 1h par côté. Attention au remontage
      des ressorts dans le bon ordre.
  - question: Quelle erreur éviter avec les mâchoires ?
    answer: Ne pas toucher les garnitures avec des mains grasses. Vérifier l état des cylindres de roue. Toujours changer
      par paire (essieu).
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
doc_id: 14712c8b-d4f3-5594-96c0-2cf7febf13ff
content_hash: sha256:9b18aa2eb78fe65d
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
---

# Mâchoires de frein - Guide Diagnostic Complet

## Fonction et Rôle

Creer la friction a l'interieur du tambour

**Actions principales:** frotter, exercer une pression interne, s'user progressivement, s'ecarter, plaquer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Frein a main qui ne tient plus ou mal**
  frein a main qui ne tient plus ou mal
- **Freinage arriere desequilibre tire d un cote**
  freinage arriere desequilibre tire d un cote
- **Poussiere frein noire excessive jantes**
  poussiere frein noire excessive jantes

### 🟢 Autres Symptômes

- bruit de frottement metallique a l arriere
- tambour raye ou strie a l interieur
- epaisseur de garniture inferieure a 2mm

## Procédure de Diagnostic

Pour diagnostiquer un problème de mâchoires de frein:

1. **Inspection visuelle** - Examiner l'état du mâchoires de frein
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

- cable-de-frein-a-main
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- flexible-de-frein
- interrupteur-des-feux-de-freins
- kit-de-freins-arriere
- maitre-cylindre-de-frein

## Critères de Compatibilité

Pour commander le bon mâchoires de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "remplacement plaquettes"

## FAQ

**Mâchoires OE ou adaptables : que choisir ?**
Les mâchoires OES (TRW, Bosch, Valeo) offrent d excellentes performances. Vérifiez le diamètre du tambour et la largeur des garnitures.

**Comment savoir si mes mâchoires sont usées ?**
Frein à main inefficace, bruit de frottement métallique à l arrière, tambour rayé à l intérieur, épaisseur de garniture inférieure à 2mm.

**Tous les combien changer les mâchoires ?**
Entre 80 000 et 120 000 km en moyenne. Les mâchoires arrière sont moins sollicitées que le freinage avant, d où leur durée de vie supérieure.

**Peut-on changer ses mâchoires soi-même ?**
Oui mais opération technique. Il faut déposer le tambour et les ressorts. Comptez 1h par côté. Attention au remontage des ressorts dans le bon ordre.

**Quelle erreur éviter avec les mâchoires ?**
Ne pas toucher les garnitures avec des mains grasses. Vérifier l état des cylindres de roue. Toujours changer par paire (essieu).


## References supplementaires

<!-- materialized-from-db reference/freinage__ece-r90.md 2026-03-03 -->
### ECE R90 - definition

## Definition

La norme ECE R90 encadre la conformite des pieces de freinage de remplacement (ex: plaquettes, disques) avec des exigences de performance proches de l'equipement d'origine.

## Pourquoi c'est important

- meilleure coherence de freinage
- reduction du risque de pieces non conformes
- reference utile pour le choix de pieces sur vehicule de tourisme

## Points a verifier

- mention ECE R90 sur le produit/emballage
- correspondance avec la reference vehicule
- provenance et tracabilite

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
