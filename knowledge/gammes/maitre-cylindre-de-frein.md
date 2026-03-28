---
category: freinage
slug: maitre-cylindre-de-frein
title: Maître cylindre de frein
pg_id: 258
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
  last_enriched_by: script:rag-enrich-metier-templates
  last_enriched_at: '2026-03-26'
domain:
  role: Transformer l'action de la pedale en pression hydraulique
  must_be_true:
  - generer la pression
  - alimenter le circuit
  - commander le freinage
  must_not_contain:
  - friction
  - thermique
  - ABS
  - electronique
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - disque-de-frein
  - plaquette-de-frein
  - etrier-de-frein
  - flexible-de-frein
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
  - ❌ "efficacite garantie"
  cost_range:
    min: 79
    max: 424
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
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
    label: Pedale de frein qui s enfonce lentement a l arret
    severity: securite
  - id: S2
    label: Niveau liquide baisse fuite visible
    severity: confort
  - id: S3
    label: Pedale de frein molle malgre une purge recente
    severity: securite
  - id: S4
    label: Liquide de frein qui fuit dans l habitacle servo
    severity: securite
  - id: S5
    label: Perte de freinage progressive sur un circuit
    severity: securite
  - id: S6
    label: Voyant niveau liquide de frein allume
    severity: securite
  causes:
  - lecture codes defaut obd et diagnostic electronique
  - identifier origine fuite et verifier joints
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  depose_steps: []
  quick_checks:
  - 'Observer : pedale de frein qui s enfonce lentement a l arret ?'
  - 'Observer : niveau liquide baisse fuite visible ?'
  - 'Observer : pedale de frein molle malgre une purge recente ?'
  - 'Observer : liquide de frein qui fuit dans l habitacle servo ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Pedale de frein qui s enfonce lentement a l arret
  - Niveau liquide baisse fuite visible
  - Pedale de frein molle malgre une purge recente
  - Liquide de frein qui fuit dans l habitacle servo
  - Perte de freinage progressive sur un circuit
  - Voyant niveau liquide de frein allume
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '258'
  intro_title: A quoi sert Maître cylindre de frein ?
  risk_title: Pourquoi remplacer Maître cylindre de frein a temps ?
  risk_explanation: '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
  risk_consequences:
  - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
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
  - question: Maître-cylindre neuf ou échange standard ?
    answer: L'échange standard est 30-40% moins cher. Qualité équivalente au neuf si le reconditionnement est fait par un
      spécialiste.
  - question: Comment savoir si mon maître-cylindre est HS ?
    answer: Pédale de frein qui s'enfonce lentement au feu rouge, niveau de liquide qui baisse sans fuite visible, pédale
      molle après purge.
  - question: Tous les combien changer le maître-cylindre ?
    answer: Pas de périodicité fixe. C'est une pièce durable (souvent plus de 200 000 km). À remplacer en cas de fuite interne
      ou défaillance.
  - question: Peut-on changer le maître-cylindre soi-même ?
    answer: Oui mais technique. Il faut purger tout le circuit après. Réglage de la garde de pédale parfois nécessaire. Comptez
      2h.
  - question: Quelle erreur éviter avec le maître-cylindre ?
    answer: Ne jamais rouler avec une pédale qui s'enfonce (danger). Purger dans le bon ordre (roue la plus éloignée en premier).
      Utiliser du liquide de frein neuf.
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
doc_id: 58eb73ad-e394-57b3-8205-6de7a26ff435
content_hash: sha256:aa9234eeabec4a37
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

# Maître cylindre de frein - Guide Diagnostic Complet

## Fonction et Rôle

Transformer l'action de la pedale en pression hydraulique

**Actions principales:** generer la pression, alimenter le circuit, commander le freinage, convertir, pousser le liquide

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Pedale de frein qui s enfonce lentement a l arret**
  pedale de frein qui s enfonce lentement a l arret
- **Pedale de frein molle malgre une purge recente**
  pedale de frein molle malgre une purge recente
- **Liquide de frein qui fuit dans l habitacle servo**
  liquide de frein qui fuit dans l habitacle servo
- **Perte de freinage progressive sur un circuit**
  perte de freinage progressive sur un circuit
- **Voyant niveau liquide de frein allume**
  voyant niveau liquide de frein allume

### 🟢 Autres Symptômes

- niveau liquide baisse fuite visible

## Procédure de Diagnostic

Pour diagnostiquer un problème de maître cylindre de frein:

1. **Inspection visuelle** - Examiner l'état du maître cylindre de frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- agregat-de-freinage
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- etrier-de-frein
- flexible-de-frein
- interrupteur-des-feux-de-freins
- kit-de-freins-arriere

## Critères de Compatibilité

Pour commander le bon maître cylindre de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "efficacite garantie"

## FAQ

**Maître-cylindre neuf ou échange standard ?**
L'échange standard est 30-40% moins cher. Qualité équivalente au neuf si le reconditionnement est fait par un spécialiste.

**Comment savoir si mon maître-cylindre est HS ?**
Pédale de frein qui s'enfonce lentement au feu rouge, niveau de liquide qui baisse sans fuite visible, pédale molle après purge.

**Tous les combien changer le maître-cylindre ?**
Pas de périodicité fixe. C'est une pièce durable (souvent plus de 200 000 km). À remplacer en cas de fuite interne ou défaillance.

**Peut-on changer le maître-cylindre soi-même ?**
Oui mais technique. Il faut purger tout le circuit après. Réglage de la garde de pédale parfois nécessaire. Comptez 2h.

**Quelle erreur éviter avec le maître-cylindre ?**
Ne jamais rouler avec une pédale qui s'enfonce (danger). Purger dans le bon ordre (roue la plus éloignée en premier). Utiliser du liquide de frein neuf.


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
