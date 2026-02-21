---
category: freinage
doc_family: catalog
source_type: gamme
pg_id: 82
slug: disque-de-frein
title: Disque de frein
truth_level: L2
updated_at: 2026-02-17
verification_status: draft
intent_targets:
  - diagnostic
  - achat
  - reference
  - entretien
mechanical_rules:
  must_be_true:
    - friction
    - plaquettes
    - chaleur
    - essieu
    - paire
  must_not_contain_concepts:
    - tambour de frein
    - frein à main
  confusion_with:
    - term: tambour de frein
      difference: Le tambour utilise des mâchoires internes, le disque utilise des plaquettes externes pressées par un étrier
    - term: plaquette de frein
      difference: La plaquette est la garniture qui frotte contre le disque. Le disque est le plateau métallique fixé au moyeu
page_contract:
  pgId: '82'
  intro:
    title: À quoi sert le disque de frein ?
    role: Le disque de frein transforme l'énergie cinétique en chaleur par friction avec les plaquettes afin de ralentir le véhicule de manière stable et répétable.
    syncParts:
      - Vérifier les plaquettes au démontage.
      - Contrôler l'état de l'étrier et des guidages.
  symptoms:
    - Vibrations au volant au freinage
    - Pulsation dans la pédale de frein
    - Bruit de grincement ou frottement métallique
    - Distance de freinage allongée
    - Traces bleutées ou rainures profondes sur la piste
  timing:
    title: Quand intervenir ?
    km: Contrôle à chaque révision, remplacement entre 60 000 et 80 000 km en usage mixte
    years: Contrôle annuel recommandé
    note: Épaisseur sous minimum constructeur = remplacement immédiat
  risk:
    title: Pourquoi remplacer le disque de frein à temps ?
    explanation: Un disque usé ou voilé réduit l'efficacité de freinage et peut endommager les plaquettes neuves.
    consequences:
      - Distance de freinage allongée (risque d'accident)
      - Destruction prématurée des plaquettes neuves
      - Vibrations transmises au volant et à la pédale
      - Surchauffe pouvant fissurer le disque
    costRange: 80 à 300 EUR par essieu (pièces), 100 à 200 EUR de main d'œuvre
    conclusion: Un contrôle visuel régulier et un remplacement par paire évitent la majorité des problèmes.
  arguments:
    - title: Compatibilité vérifiée
      content: Sélection guidée par véhicule, motorisation et essieu.
      icon: check-circle
    - title: Priorité sécurité
      content: Le freinage est le premier organe de sécurité du véhicule.
      icon: shield-check
    - title: Décision rapide
      content: Le guide structure les contrôles avant commande.
      icon: clock
    - title: Montage maîtrisé
      content: Toujours remplacer par paire avec vérification des plaquettes.
      icon: list-check
  howToChoose: Renseignez marque, modèle, motorisation et essieu (avant/arrière). Vérifiez le type (plein ou ventilé) et le diamètre. Notre sélecteur affiche uniquement les références compatibles.
  antiMistakes:
    - Ne remplacer qu'un seul disque au lieu des deux sur le même essieu
    - Monter des plaquettes neuves sur des disques usés
    - Ne pas respecter le couple de serrage des boulons de roue
    - Utiliser de la graisse en zone de friction (piste du disque)
    - Ignorer l'état des étriers et guidages au remontage
  faq:
    - question: Faut-il changer les disques et les plaquettes ensemble ?
      answer: Oui dans la plupart des cas. Des plaquettes neuves sur des disques usés ne freinent pas de manière optimale. Prévoyez le remplacement conjoint.
    - question: Plein ou ventilé, lequel choisir ?
      answer: Pour l'avant, ventilé (standard). Pour l'arrière, respectez le type d'origine. Notre sélecteur indique le bon type.
    - question: Combien de temps durent les disques de frein ?
      answer: En moyenne 60 000 à 80 000 km en usage mixte. En conduite urbaine intensive, l'usure peut être plus rapide.
    - question: Quelle différence entre un disque à 20 EUR et un à 60 EUR ?
      answer: Le prix reflète la qualité des matériaux et la précision de fabrication. Un disque de marque reconnue offre un freinage plus constant et une meilleure durée de vie.
    - question: Peut-on changer ses disques soi-même ?
      answer: Le remplacement est possible pour un bricoleur équipé, mais le freinage est un élément de sécurité critique. En cas de doute, confiez le montage à un professionnel. Prévoyez 200 km de rodage.
    - question: Faut-il changer les 2 côtés en même temps ?
      answer: Oui, toujours par paire sur le même essieu. Un disque neuf d'un côté et un disque usé de l'autre crée un déséquilibre de freinage dangereux.
  quality:
    score: 92
    source: manual:template-v3
    version: GammeContentContract.v3
seo_cluster:
  updated_at: 2026-02-17
  primary_keyword:
    text: "comment choisir ses disques de frein"
    seo_difficulty: 41
    traffic_range: "220-1400/mo"
    intent: informationnelle
  keyword_variants:
    - keyword: "guide achat disque de frein"
      sd: 31
      results: "11.7M"
      intent: "informationnelle + transactionnelle"
      competition: faible
    - keyword: "achat disque de frein"
      sd: 31
      results: "8.4M"
      intent: transactionnelle
      competition: moyenne
    - keyword: "comment choisir disque de frein"
      sd: 42
      results: "6.3M"
      intent: informationnelle
      competition: forte
    - keyword: "quel disque de frein choisir"
      sd: 36
      results: "3.8M"
      intent: informationnelle
      competition: moyenne
    - keyword: "meilleur disque de frein"
      sd: 48
      results: "3.6M"
      intent: "informationnelle + comparatif"
      competition: forte
    - keyword: "comment choisir ses disques de frein voiture"
      sd: 38
      intent: informationnelle
      competition: forte
  paa_questions:
    - "Comment savoir quel disque de frein acheter ?"
    - "Comment savoir quels disques de frein il me faut ?"
    - "Comment connaître la taille de ses disques de frein ?"
    - "Comment savoir si on doit changer les disques de frein ?"
    - "Quelle est la meilleure marque pour les disques de frein ?"
    - "Quelle est la limite d'usure pour les disques de frein ?"
    - "Comment savoir si mon disque est mort ?"
  cluster_informationnelle:
    - keyword: "comment choisir ses disques de frein"
      sd: 41
      potential: 5
    - keyword: "comment choisir ses disques de frein voiture"
      sd: 38
      potential: 4
    - keyword: "comment bien choisir ses disques de frein"
      sd: 35
      potential: 4
    - keyword: "comment connaitre taille disque de frein voiture"
      sd: 40
      potential: 4
    - keyword: "disque de frein ventilé ou plein"
      sd: 48
      potential: 3
    - keyword: "comment trouver la référence de ses disques de frein"
      sd: 30
      potential: 3
    - keyword: "quand changer disque de frein"
      sd: 37
      potential: 4
    - keyword: "disque de frein usé symptôme"
      sd: 35
      potential: 3
    - keyword: "quelle épaisseur de disque de frein choisir"
      sd: 30
      potential: 3
  cluster_commerciale:
    - keyword: "meilleure marque disque de frein voiture"
      sd: 40
      potential: 5
    - keyword: "comparatif disque de frein"
      sd: 42
      potential: 5
    - keyword: "classement marque disque de frein"
      sd: 35
      potential: 4
    - keyword: "top 10 disque de frein"
      sd: 30
      potential: 4
    - keyword: "quel disque de frein choisir"
      sd: 36
      potential: 5
    - keyword: "quels disques de frein choisir"
      sd: 38
      potential: 4
    - keyword: "disque de frein ATE ou Brembo"
      sd: 25
      potential: 3
    - keyword: "disque de frein ATE avis"
      sd: 25
      potential: 3
    - keyword: "quelle marque de disque et plaquettes de frein choisir"
      sd: 35
      potential: 4
    - keyword: "quel type de disques de frein est le meilleur"
      sd: 33
      potential: 3
    - keyword: "meilleur marque disque de frein BMW"
      sd: 20
      potential: 3
  cluster_transactionnelle:
    - keyword: "achat disque de frein"
      sd: 31
      potential: 4
    - keyword: "disque de frein pas cher"
      sd: 35
      potential: 4
    - keyword: "disques de freins prix"
      sd: 38
      potential: 4
    - keyword: "plaquette et disque de frein prix"
      sd: 33
      potential: 4
    - keyword: "disque de frein prix moyen"
      sd: 28
      potential: 3
    - keyword: "disques de frein avant"
      sd: 45
      potential: 3
    - keyword: "disques de frein arrière"
      sd: 43
      potential: 3
    - keyword: "kit disque et plaquette de frein"
      sd: 35
      potential: 4
    - keyword: "remplacement plaquettes de frein et disques avant"
      sd: 30
      potential: 3
  cluster_pratique:
    - keyword: "comment choisir ses plaquettes de frein"
      potential: 4
      note: "complémentaire cross-gamme"
    - keyword: "comment choisir plaquette de frein voiture"
      potential: 4
      note: "complémentaire cross-gamme"
    - keyword: "comment choisir disque de frein vélo"
      potential: 3
      note: "niche vélo - hors scope"
    - keyword: "comment choisir ses disques de frein VTT"
      potential: 3
      note: "niche VTT - hors scope"
  competitors:
    - name: Oscaro
      traffic: "1400/mo"
      keywords_ranked: 304
    - name: Mister-auto
      traffic: "980/mo"
      keywords_ranked: 283
    - name: Garages AD
      note: "DA modéré, forte présence"
    - name: Autodoc
      note: "concurrent transactionnel"
    - name: Trodo
      note: "concurrent transactionnel"
  priority_top5:
    - "comment choisir ses disques de frein"
    - "quel disque de frein choisir"
    - "meilleure marque disque de frein voiture"
    - "comparatif disque de frein"
    - "quand changer disque de frein"
  target_reach: "300+ requêtes via guide complet"
---

# Disque de frein

## Référence technique

Le disque de frein est un composant de sécurité du système de freinage. Il transforme l'énergie cinétique du véhicule en chaleur par friction avec les plaquettes de frein.

### Types de disques

| Type | Usage | Caractéristiques |
|------|-------|-----------------|
| **Plein** | Arrière (véhicules légers) | Moins cher, suffisant pour faible sollicitation |
| **Ventilé** | Avant (standard) | Deux pistes séparées par des ailettes, meilleure évacuation de la chaleur |
| **Perforé** | Sport / circuit | Trous pour évacuer gaz et eau, mordant à chaud |
| **Rainuré** | Sport / utilitaire chargé | Rainures pour évacuer poussières de garniture, mordant constant |

### Normes et spécifications

- **ECE R90** : Norme européenne imposant des performances de freinage proches de l'équipement d'origine pour toute pièce de remplacement
- **Cote minimale** : Épaisseur minimale gravée sur le disque (ex : MIN TH 22.0 mm). En dessous = remplacement obligatoire
- **Voile maximal** : Tolérance de faux-rond, généralement 0.05 à 0.07 mm. Au-delà = vibrations au freinage

### Pièces associées

- **Plaquettes de frein** : S'usent avec le disque, à contrôler systématiquement
- **Étrier de frein** : Presse les plaquettes contre le disque
- **Flexible de frein** : Transmet la pression hydraulique à l'étrier
- **Capteur ABS** : Mesure la vitesse de rotation de la roue via la cible ABS du disque
- **Liquide de frein** : À purger si le circuit a été ouvert

## Diagnostic

### Symptômes spécifiques au disque de frein

| Symptôme | Description | Urgence |
|----------|-------------|---------|
| **Vibrations au volant au freinage** | Le volant tremble quand on freine, surtout à vitesse élevée | Moyenne - faire contrôler |
| **Pulsation dans la pédale** | La pédale de frein pulse sous le pied au freinage | Moyenne |
| **Grincement métallique** | Bruit de métal contre métal : les plaquettes sont usées jusqu'à l'âme | Haute - sécurité |
| **Distance de freinage allongée** | Le véhicule met plus de distance à s'arrêter | Haute - sécurité |
| **Traces bleutées sur la piste** | Surchauffe du disque, points chauds visibles | Haute - remplacement |
| **Rainures profondes** | Sillons creusés dans la piste de freinage | Moyenne - mesurer épaisseur |
| **Tire d'un côté au freinage** | Un étrier grippé ou un disque plus usé que l'autre | Haute - sécurité |

### Causes probables (du plus fréquent au plus rare)

1. **Usure normale** (60%) : Le disque s'amincit avec les kilomètres. Remplacement entre 60 000 et 80 000 km en usage mixte.
2. **Disque voilé** (20%) : Déformation due à un échauffement excessif (descente de col, freinage appuyé répété). Provoque vibrations au volant.
3. **Montage non conforme** (10%) : Moyeu sale, couple de serrage incorrect, boulons de roue serrés à la visseuse sans couple.
4. **Étrier grippé** (5%) : L'étrier ne relâche pas la plaquette, le disque chauffe en permanence d'un côté.
5. **Mauvaise association disque/plaquette** (5%) : Garniture trop abrasive ou incompatible qui raye le disque.

### Tests simples (sans outil)

- **Inspection visuelle** : Regarder le disque à travers les jantes. Traces bleues, fissures, rainures profondes ?
- **Essai route** : Freiner progressivement à 80 km/h. Vibrations dans le volant ? Pulsation dans la pédale ?
- **Écoute** : Bruit de frottement ou grincement métallique au freinage ?
- **Comparaison** : La distance de freinage semble-t-elle plus longue qu'avant ?

### Tests atelier

- **Mesure d'épaisseur** au pied à coulisse en plusieurs points (comparer à la cote mini gravée sur le disque)
- **Mesure du voile** au comparateur (tolérance : 0.05-0.07 mm)
- **Contrôle du faux-rond du moyeu** avant montage du disque neuf
- **Vérification état de surface** : pas de fissures, pas de points chauds, pas de corrosion excessive sur la piste

### Quand remplacer immédiatement

- Épaisseur sous le minimum constructeur (cote gravée sur le disque)
- Fissure visible sur la piste de freinage
- Déformation importante (voile > 0.1 mm)
- Traces de surchauffe sévère (coloration bleu-violet sur toute la piste)
- Freinage instable ou perte d'efficacité ressentie

## Guide d'achat

### Critères de choix

**1. Position : avant ou arrière**

| Position | Rôle | Type standard |
|----------|------|--------------|
| **Avant** | 70% de l'effort de freinage | Ventilé |
| **Arrière** | Stabilité au freinage | Plein ou ventilé selon véhicule |

Toujours remplacer par essieu (les 2 côtés ensemble).

**2. Type selon l'usage**

| Conduite | Disque recommandé | Budget par paire |
|----------|-------------------|-----------------|
| Urbaine / calme | Ventilé standard | 40-80 EUR |
| Mixte route/ville | Ventilé standard | 40-80 EUR |
| Montagne / véhicule chargé | Ventilé haute capacité | 80-150 EUR |
| Sportive / circuit | Perforé ou rainuré | 150-400 EUR |

**3. Compatibilité**

- Vérifier l'essieu (avant ≠ arrière)
- Vérifier le type (plein ≠ ventilé)
- Vérifier le diamètre et l'épaisseur
- Vérifier si bague ABS intégrée au disque
- Utiliser le sélecteur de véhicule pour éviter les erreurs

### Marques recommandées

**Premium (équipementiers d'origine)**
- **Brembo** : Référence en performance et durabilité
- **ATE** : Spécialiste freinage, qualité d'origine
- **Bosch** : Excellent rapport qualité/prix
- **TRW** : Équipementier majeur, large couverture

**Qualité équivalente**
- **Valeo** : Bon rapport qualité/prix
- **Ferodo** : Fiabilité éprouvée
- **Textar** : Qualité d'origine

**Économique**
- **NK** : Budget maîtrisé, qualité correcte
- **Delphi** : Entrée de gamme fiable

### Check-list avant commande

1. Vérifier l'essieu concerné (avant ≠ arrière)
2. Confirmer le type (plein ou ventilé)
3. Commander par paire (2 disques même essieu)
4. Vérifier si bague ABS intégrée nécessaire
5. Choisir selon l'usage (standard, haute capacité, sport)
6. Penser aux plaquettes (les changer en même temps si usées)
7. Privilégier une marque reconnue
8. Si stationnement extérieur fréquent, préférer un traitement anti-corrosion

### Erreurs à éviter

- Commander sans vérifier l'essieu (avant ≠ arrière)
- Remplacer un seul disque au lieu des deux sur le même essieu
- Choisir uniquement sur le prix sans vérifier marque et qualité
- Oublier de vérifier l'état des plaquettes au changement de disques
- Commander des disques percés pour un usage urbain (inutile et plus cher)
- Ignorer les vibrations au freinage en espérant que ça passe
- Confondre plein et ventilé
- Ne pas vérifier si le véhicule nécessite une bague ABS intégrée

## Entretien

### Intervalles de contrôle

| Contrôle | Fréquence |
|----------|-----------|
| Inspection visuelle (à travers jantes) | À chaque révision ou tous les 15 000 km |
| Mesure d'épaisseur | À chaque changement de plaquettes |
| Contrôle du voile | Si vibrations au freinage |

### Durée de vie moyenne

| Type de conduite | Durée de vie estimée |
|------------------|---------------------|
| Urbaine intensive | 40 000 - 60 000 km |
| Mixte | 60 000 - 80 000 km |
| Autoroute | 80 000 - 100 000 km |

### Signes d'usure à surveiller

- Rainures profondes visibles sur la piste
- Bord du disque en relief (la piste s'est creusée)
- Traces de rouille sur la piste de freinage (stationnement prolongé)
- Vibrations au freinage qui apparaissent progressivement

### Remplacement : les règles

- **Toujours par paire** : Les 2 disques du même essieu en même temps
- **Avec les plaquettes** : Des plaquettes neuves sur des disques usés ne freinent pas correctement
- **Rodage** : 200 km de conduite modérée après montage (éviter les freinages brusques)
- **Purge** : Si le circuit hydraulique a été ouvert, purger le liquide de frein
- **Couples de serrage** : Respecter le couple des boulons de roue (clé dynamométrique obligatoire)
