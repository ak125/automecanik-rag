---
category: freinage
slug: servo-frein
title: Servo frein
pg_id: 74
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-03-29'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:rag-enrich-from-web-corpus
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Amplifier l'effort de freinage grace a la depression moteur
  must_be_true:
  - amplifier
  - assister
  - demultiplier
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
  - Le choix du servo-frein dépend de votre véhicule.
  - En sélectionnant votre voiture sur Automecanik, nous affichons uniquement les servo-freins compatibles.
  - Le servo-frein amplifie votre effort sur la pédale. Sans lui, freiner demande une force considérable.
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "freinage garanti"
  cost_range:
    min: 150
    max: 450
    currency: EUR
    unit: pièce
    source: catalogue automecanik
  brands:
    premium:
    - ATE
    - TRW
    - Bosch
    standard:
    - FTE Automotive
    - Brembo
    - LPR
    budget:
    - NK
    - Maxgear
    - Febi Bilstein
  quality_tiers:
  - tier: Origine (OE)
    description: Servo-freins fabriques par l'equipementier d'origine. Membrane, diametre et rapport d'amplification identiques
      a la piece constructeur.
  - tier: Qualite equivalente OE (OES)
    description: Equipementiers reconnus en freinage. Performances d'amplification equivalentes a l'OE, tarif inferieur.
  - tier: Adaptable de qualite
    description: Marques fiables en entree de gamme. Verifier le diametre de membrane et le nombre de membranes (simple ou
      tandem).
diagnostic:
  symptoms:
  - id: S1
    label: Pedale de frein tres dure a enfoncer
    severity: securite
  - id: S2
    label: Effort au freinage anormalement eleve
    severity: securite
  - id: S3
    label: Sifflement au niveau de la pedale
    severity: confort
  - id: S4
    label: Pedale qui vibre au freinage
    severity: securite
  - id: S5
    label: Moteur qui cale au freinage prise d air
    severity: immobilisation
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - 'Usure ou defaillance causant : pedale de frein tres dure a enfoncer'
  quick_checks:
  - 'Observer : pedale de frein tres dure a enfoncer ?'
  - 'Observer : effort au freinage anormalement eleve ?'
  - 'Observer : sifflement au niveau de la pedale ?'
  - 'Observer : pedale qui vibre au freinage ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Pedale de frein tres dure a enfoncer
  - Effort au freinage anormalement eleve
  - Sifflement au niveau de la pedale
  - Pedale qui vibre au freinage
  - Moteur qui cale au freinage prise d air
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '74'
  intro_title: A quoi sert Servo frein ?
  risk_title: Pourquoi remplacer Servo frein a temps ?
  risk_explanation: '**Pièce HS** - Le servo frein peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le servo frein peut être hors service et nécessiter un remplacement'
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: À quoi sert le servo-frein ?
    answer: Il amplifie la force de votre pied sur la pédale grâce à la dépression moteur. Sans lui, il faudrait appuyer très
      fort pour freiner correctement.
  - question: Comment savoir si mon servo-frein est HS ?
    answer: 'Pédale de frein très dure à enfoncer, surtout moteur tournant. Sifflement au freinage. Test : moteur arrêté,
      appuyez plusieurs fois sur la pédale puis démarrez. La pédale doit s''enfoncer légèrement.'
  - question: Le servo-frein peut-il fuir ?
    answer: La membrane interne peut se perforer avec l'âge, causant une perte d'assistance. Pas de fuite de liquide mais
      perte de dépression.
  - question: Quelles sont les erreurs fréquentes à éviter ?
    answer: Accuser le servo-frein alors que c'est la pompe à vide (diesel) ou une durite de dépression fissurée. Ne pas vérifier
      le clapet anti-retour. Oublier de contrôler le maître-cylindre fixé dessus.
  - question: Comment faire un diagnostic rapide ?
    answer: 'Pédale dure moteur tournant → servo ou dépression. Sifflement → fuite membrane/durite. Test dépression OK mais
      pédale dure → membrane HS. Sur diesel : vérifier pompe à vide en premier.'
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
doc_id: be42e06c-98f2-5a8f-856c-8ae5a1180390
content_hash: sha256:284b1955ea07a4cf
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
  _source: ate-freinage.fr + hella.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 3
  _has_tech_data: true
  materials:
  - materiau: 'aluminium'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    - Niveau de difficulté : avancé — intervention sur le circuit de freinage. -
    Temps estimé : 2 à 4 h selon l'accessibilité. - Outils : cric + chandelles,
    clés à œil 10-17 mm, clés à tuyauter, pince à durites, kit de purge. -
    Consommables : liquide de frein DOT 4 neuf (1 L minimum), clapet anti-retour
    neuf. - Sécurité : pièce safety-critical. Ne jamais démarrer sans purge
    complète du circuit. En cas de doute, confiez l'intervention à un
    professionnel. 🚨 Bruit Servo frein : causes et diagnostic
  S2: >-
    Unservofrein n'a pas de période de remplacement fixe, l'état de la pédale
    defrein c'est elle qu'informe sur l'état d'usure du servofrein. Diagnostic
    complet : identifier une panne de servo frein
  S3: >-
    - Diamètre du maître-cylindre : le servo doit correspondre au diamètre du MC
    monté sur le véhicule. - Type d'assistance : dépression moteur (majorité) ou
    pompe à vide (diesel récents, électriques). Le servo à dépression ne
    fonctionne pas sur un véhicule équipé d'une pompe à vide sans adaptation. -
    Entraxe de fixation : 4 goujons au tablier — vérifiez l'entraxe et le
    diamètre des goujons. - Longueur de tige de poussée : elle détermine la
    garde de pédale. Certains servos neufs sont livrés avec une tige réglable. -
    Raccord de dépression : diamètre et orientation du raccord doivent
    correspondre à la durite d'origine. Pour aller plus loin : consultez notre
    guide d'achat servo frein — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Servo frein pour connaître
    les spécifications. - Vidangez leliquide de frein. - Démontez lemaître-
    cylindre de la voiture. - Désaccouplez lescanalisations d'air. - Démontez le
    cachederrière la pédale de frein. - Appuyez et gardezl'appui sur la pédale
    de frein. - Démontez lapédale de frein de la tige de poussée en utilisant un
    outil de démontageapproprié. - Retirez l'outilde démontage de la tige sans
    bouger la pédale de frein. - Démontez la tigede poussée. - Desserrez les
    fixationsdu servofrein. - Démontez leservofrein.
  S4_REPOSE: >-
    - Vérifiez que le servofrein neuf est identiqueà celui démonté. - Contrôlez
    le fonctionnement du maître-cylindreet le remplacé si nécessaire. - Mettreen
    place le servofrein. - Serrez les fixations du servofrein. - Mettre en place
    la tige de poussée sur lapédale de frein. - Remontez le cache derrière la
    pédale de frein. - Accouplez les canalisations d'air. - Remontez le maître-
    cylindre. - Remplir le circuit de frein avec l'huilepréconisé. - Appuyez
    plusieurs fois sur la pédale de frein. - Faire un essai routier pour
    contrôlez le bonfonctionnement du système de freinage. ✅ Après remontage,
    vérifiez les spécifications dans la fiche technique Servo frein.
  S5: >-
    - Oublier la purge des freins — le démontage du maître-cylindre introduit de
    l'air. Sans purge complète 4 roues, le freinage est dangereux. - Ne pas
    remplacer le clapet anti-retour — un clapet fatigué laisse entrer l'air et
    annule l'assistance du servo neuf. - Forcer la tige de poussée — une tige
    trop longue maintient le maître-cylindre sous pression et provoque un
    freinage résiduel permanent. - Serrage inégal des écrous du tablier — serrez
    en étoile pour éviter de déformer la collerette du servo. - Négliger le
    joint de tablier — le joint entre le servo et la cloison empêche
    infiltrations d'eau et de bruit. Remplacez-le s'il est écrasé. - Déconnecter
    les conduites de frein sans nécessité — le maître-cylindre peut souvent être
    écarté sans débrancher les conduites, ce qui limite la purge. 📖 Fiche
    technique Servo frein — spécifications à vérifier avant montage.
  S6: >-
    - Test de dépression : moteur éteint, appuyez 5 fois sur la pédale,
    maintenez, démarrez → la pédale doit s'enfoncer légèrement = servo
    fonctionnel. - Étanchéité : aucun sifflement au freinage, aucune fuite de
    liquide au maître-cylindre après 10 min moteur tournant. - Garde de pédale :
    la course libre avant résistance doit correspondre à la préconisation
    constructeur (3-8 mm). - Essai routier progressif : freinez doucement puis
    augmentez l'effort. Vérifiez que le véhicule freine droit et que l'ABS
    intervient normalement. - Passage au banc recommandé : un essai de freinage
    sur banc valide la conformité de l'effort de freinage avant de reprendre la
    route. 🚨 Bruit Servo frein : causes et diagnostic
  S7: >-
    Quel est le prix d'un servo frein ?Le prix varie selon le véhicule et la
    marque. Utilisez notre sélecteur pour trouver le servo frein compatible avec
    votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon servo frein est à changer ?Les signes d'usure les plus
    courants sont détaillés dans la section diagnostic ci-dessus. En cas de
    doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un
    servo frein défaillant ?Cela dépend de la gravité du dysfonctionnement et du
    rôle de la pièce dans la sécurité du véhicule. Consultez la section
    symptômes pour évaluer l'urgence du remplacement. - Clapet anti-retour de
    dépression — à remplacer systématiquement (usure invisible, pièce
    économique). - Durite de dépression — remplacez si craquelée ou ramollie. -
    Maître-cylindre de frein — inspectez les joints internes si le véhicule
    dépasse 200 000 km. - Liquide de frein DOT 4 — 1 L minimum pour la purge 4
    roues. - Joint de tablier — joint d'étanchéité entre le servo et la cloison
    pare-feu. 📖 Fiche technique Servo frein — intervalles et spécifications
    d’entretien.
  S8: >-
    - Peut-on rouler sans servo-frein ? Le freinage reste possible mais exige
    une force considérable. C'est dangereux en situation d'urgence et non
    conforme au contrôle technique. - Servo-frein neuf ou échange standard ?
    L'échange standard est courant et fiable. Vérifiez que le reconditionneur
    remplace la membrane et le clapet interne. - Le servo fonctionne-t-il sans
    moteur ? Il stocke une réserve de 2-3 freinages après l'arrêt moteur. Au-
    delà, la pédale devient dure. - Servo ou maître-cylindre : comment
    distinguer la panne ? Le servo rend la pédale dure (pas d'assistance). Le
    maître-cylindre rend la pédale molle (fuite interne). Les deux peuvent
    coexister. - Faut-il un passage au contrôle technique après remplacement ?
    Non, mais un essai sur banc de freinage est recommandé pour valider la
    conformité. 📖 Pour plus de détails techniques : fiche Servo frein
---

# Servo frein - Guide Diagnostic Complet

## Fonction et Rôle

Amplifier l'effort de freinage grace a la depression moteur

**Actions principales:** amplifier, assister, demultiplier

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Moteur qui cale au freinage prise d air**
  moteur qui cale au freinage prise d air

### 🟡 Symptômes de Sécurité

- **Pedale de frein tres dure a enfoncer**
  pedale de frein tres dure a enfoncer
- **Effort au freinage anormalement eleve**
  effort au freinage anormalement eleve
- **Pedale qui vibre au freinage**
  pedale qui vibre au freinage

### 🟢 Autres Symptômes

- sifflement au niveau de la pedale

## Procédure de Diagnostic

Pour diagnostiquer un problème de servo frein:

1. **Inspection visuelle** - Examiner l'état du servo frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le servo frein peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes

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

Pour commander le bon servo frein, vous devez connaître:

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

**À quoi sert le servo-frein ?**
Il amplifie la force de votre pied sur la pédale grâce à la dépression moteur. Sans lui, il faudrait appuyer très fort pour freiner correctement.

**Comment savoir si mon servo-frein est HS ?**
Pédale de frein très dure à enfoncer, surtout moteur tournant. Sifflement au freinage. Test : moteur arrêté, appuyez plusieurs fois sur la pédale puis démarrez. La pédale doit s'enfoncer légèrement.

**Le servo-frein peut-il fuir ?**
La membrane interne peut se perforer avec l'âge, causant une perte d'assistance. Pas de fuite de liquide mais perte de dépression.

**Quelles sont les erreurs fréquentes à éviter ?**
Accuser le servo-frein alors que c'est la pompe à vide (diesel) ou une durite de dépression fissurée. Ne pas vérifier le clapet anti-retour. Oublier de contrôler le maître-cylindre fixé dessus.

**Comment faire un diagnostic rapide ?**
Pédale dure moteur tournant → servo ou dépression. Sifflement → fuite membrane/durite. Test dépression OK mais pédale dure → membrane HS. Sur diesel : vérifier pompe à vide en premier.


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
