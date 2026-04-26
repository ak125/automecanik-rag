---
category: freinage
slug: maitre-cylindre-de-frein
title: Maître cylindre de frein
pg_id: 258
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
phase5_enrichment:
  _source: ate-freinage.fr + bremboparts.com + delphiautoparts.com + gpa26.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 10
  _has_tech_data: true
  types_variants:
  - type: 'hydraulique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_100_a: '100 a'
    val_15_a: '15 a'
    val_18_mm: '18 mm'
    val_20__: '20 %'
    val_20_mm: '20 mm'
    val_7_a: '7 a'
    val_8_a: '8 a'
    val_9_a: '9 a'
  materials:
  - materiau: 'EPDM'
    source_ref: corpus RAG web OEM
  - materiau: 'aluminium'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: Le maître-cylindre de frein est le cœur du circuit de freinage hydraulique. Fixé sur le servo-frein, il transforme la
    pression mécanique de votre pédale en pression hydraulique transmise aux étriers et cylindres de roue. Il contient deux
    pistons indépendants alimentant deux circuits séparés (diagonal ou avant/arrière selon le véhicule). Ce double circuit
    garantit un freinage résiduel si un circuit fuit — c'est une sécurité obligatoire depuis les années 70. Le réservoir de
    liquide de frein est fixé sur le maître- cylindre. Toute baisse de niveau sans usure de plaquettes indique une fuite au
    maître-cylindre ou dans le circuit. ⚠️ Pièce de sécurité critique. Une défaillance du maître-cylindre entraîne une perte
    partielle ou totale du freinage.
  S2: 'Symptômes d''un maître-cylindre de frein défaillant : Symptômes critiques (sécurité) : - Pédale de frein qui s''enfonce
    lentement à l''arrêt — fuite interne entre les deux circuits. Le joint du piston laisse passer le liquide. Symptôme le
    plus caractéristique. - Pédale molle malgré une purge récente — si la purge est correcte et que la pédale reste spongieuse,
    le maître-cylindre a une fuite interne. - Perte de freinage progressive sur un circuit — un des deux circuits ne monte
    plus en pression. Le véhicule tire d''un côté au freinage. Symptômes visuels : - Niveau de liquide qui baisse sans usure
    de plaquettes — fuite au maître-cylindre, aux raccords ou dans le servo. - Liquide de frein qui fuit dans l''habitacle
    — le maître-cylindre fuit côté servo-frein. Trace de liquide sur la moquette côté conducteur. - Voyant niveau liquide
    allumé — vérifier d''abord l''usure des plaquettes avant de suspecter le maître-cylindre. Test simple : Moteur tournant,
    appuyez fort sur la pédale et maintenez 30 secondes. Si la pédale s''enfonce progressivement sans lâcher → fuite interne
    = maître-cylindre HS.'
  S3: 'Pour choisir les bons maitre cylindre de frein pour votre véhicule : - Marque de votre véhicule - Modele de votre véhicule
    - Annee de votre véhicule - Vérifier : pedale de frein qui s enfonce lentement a l arret - Vérifier : niveau liquide baisse
    fuite visible - Vérifier : pedale de frein molle malgre une purge recente - Vérifier : liquide de frein qui fuit dans
    l habitacle servo - Vérifier : perte de freinage progressive sur un circuit - Vérifier : voyant niveau liquide de frein
    allume'
  S4_DEPOSE: 'Procédure de diagnostic du maître-cylindre : 1. Test de la pédale (moteur tournant) : - Appuyez fort sur la
    pédale de frein et maintenez 30 secondes. - Si la pédale s''enfonce lentement sans lâcher = fuite interne → maître- cylindre
    HS. - Si la pédale reste ferme = le maître-cylindre est probablement bon. 2. Inspection visuelle : - Vérifier le niveau
    de liquide dans le réservoir — une baisse sans usure de plaquettes est suspecte. - Chercher des traces de fuite au raccord
    maître-cylindre/servo-frein (côté cloison pare-feu). - Inspecter la moquette côté conducteur — le liquide de frein coule
    dans l''habitacle en cas de fuite arrière. 3. Contrôle des raccords : - Vérifier l''étanchéité aux deux sorties hydrauliques
    (circuits 1 et 2). - Traces de liquide ou cristallisation blanche = fuite externe. 4. Test différentiel : - Si le véhicule
    tire d''un côté au freinage, un circuit du maître-cylindre ne monte plus en pression. Comparer la pression aux 4 roues
    avec un manomètre.'
  S4_REPOSE: 'Le remontage du maître-cylindre de frein est une intervention de sécurité critique. Une purge incomplète du
    circuit hydraulique laisse de l''air compressible dans les canalisations, ce qui rend la pédale molle et réduit drastiquement
    l''efficacité de freinage. La procédure doit être suivie dans son intégralité avant tout essai routier. - Contrôler la
    conformité du maître-cylindre neuf — Comparer le maître-cylindre neuf avec celui déposé : nombre de sorties hydrauliques,
    diamètre du piston, longueur totale et position du réservoir. Une référence incorrecte peut être non compatible avec la
    pédale ou le servofrein. - Remplacer le joint d''étanchéité — Monter le joint d''étanchéité neuf fourni dans le kit sur
    le maître-cylindre avant pose. Ce joint assure l''étanchéité entre le maître-cylindre et le servofrein. Ne jamais réutiliser
    l''ancien joint. - Pré-remplir le maître- cylindre — Remplir le réservoir du maître-cylindre de liquide de frein neuf
    (DOT4 ou selon préconisation constructeur) avant de le positionner sur le servofrein. Cette étape évite d''introduire
    de l''air en excès dans le circuit primaire. - Positionner et fixer le maître-cylindre — Guider le piston du maître-cylindre
    sur la tige de poussée du servofrein, puis engager la bride sur le tablier. Serrer les écrous de fixation au couple prescrit
    en croix pour assurer un appui uniforme sur le joint. - Reconnecter les canalisations hydrauliques — Brancher les flexibles
    et canalisations de frein sur chacune des sorties du maître-cylindre. Serrer les raccords banjo ou les unions à la clé
    dynamométrique. Un serrage insuffisant provoque une fuite de liquide de frein sous pression. - Remplir le circuit de frein
    — Compléter le niveau dans le réservoir jusqu''au repère MAX avec du liquide de frein neuf. Ne pas mélanger des liquides
    de différentes spécifications DOT. - Purger le circuit hydraulique complet — Purger chaque roue dans l''ordre constructeur
    (généralement roue la plus éloignée en premier : arrière droit, arrière gauche, avant droit, avant gauche). Pomper la
    pédale lentement et maintenir la pression pendant l''ouverture de la vis de purge. Recommencer jusqu''à l''absence de
    bulles dans le liquide. - Vérifier la dureté de la pédale — Après purge, appuyer fermement sur la pédale de frein : elle
    doit être dure immédiatement, sans enfoncement progressif. Un enfoncement lent indique une fuite interne ou une purge
    incomplète — ne pas rouler dans cet état. - Contrôler les fixations et le niveau de liquide — Vérifier l''absence de fuite
    sur les raccords hydrauliques et autour du joint du maître-cylindre. Compléter le niveau si nécessaire et refermer le
    bocal. - Essai routier contrôlé — Effectuer un premier essai à faible allure en zone dégagée pour confirmer l''efficacité
    du freinage. Tester le freinage d''urgence à 40 km/h avant tout usage en circulation normale.'
  S5: 'Erreurs fréquentes avec le maître-cylindre de frein : - ❌ Oublier le bench bleeding — un maître-cylindre neuf contient
    de l''air. Il faut le purger sur l''établi AVANT de le monter. Sans ça, la pédale restera molle. - ❌ Purger dans le mauvais
    ordre — après montage, purger en partant de la roue la plus éloignée du maître-cylindre (généralement arrière droite →
    arrière gauche → avant droite → avant gauche). - ❌ Mélanger les liquides de frein — DOT 3, DOT 4 et DOT 5.1 sont miscibles
    entre eux, mais PAS avec le DOT 5 (base silicone). Vérifier la spécification constructeur. - ❌ Ne pas protéger la peinture
    — le liquide de frein attaque la peinture et le plastique. Couvrir les zones autour du maître-cylindre. - ❌ Réutiliser
    l''ancien liquide — le liquide de frein absorbe l''humidité. Utiliser uniquement du liquide neuf, bidon scellé. - ❌ Ignorer
    le servo-frein — si le servo est percé, le liquide y pénètre. Vérifier l''état du servo lors du remplacement.'
  S6: 'Contrôles statiques - Vérifier l''absence de fuite à tous les raccords hydrauliques et entre le maître-cylindre et
    le servo-frein - Contrôler le niveau de liquide dans le bocal (entre MIN et MAX) - Pomper la pédale : elle doit devenir
    dure et ne pas s''enfoncer progressivement (signe d''air résiduel ou de fuite interne) - Maintenir la pédale enfoncée
    30 secondes : elle ne doit pas descendre (test de fuite interne) Essai routier progressif - Démarrer sur parking : freinages
    doux à 10 km/h, vérifier la progressivité de la pédale - Augmenter à 30, 50, puis 70 km/h avec des freinages normaux -
    Freinage d''urgence à 50 km/h sur route dégagée : la pédale doit rester ferme et le véhicule freiner droit - Après 10
    km, vérifier le niveau du bocal (il ne doit pas avoir baissé) ⚠️ Arrêter immédiatement si : pédale molle ou qui s''enfonce,
    perte de liquide visible, distance de freinage anormale, pédale qui descend lentement pied maintenu. 🚨 Bruit Maître cylindre
    de frein : causes et diagnostic'
  S_GARAGE: 'Nous vous recommandons de confier cette intervention à un professionnel : - Plusieurs causes possibles de défaillance
    (4 identifiées) nécessitent un diagnostic professionnel Un garagiste qualifié dispose de l''outillage et de l''expérience
    nécessaires pour effectuer cette opération en toute sécurité.'
  S7: Quel est le prix d'un maître cylindre de frein ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur
    pour trouver le maître cylindre de frein compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon maître cylindre de frein est à changer ?Les signes d'usure les plus courants sont détaillés dans la section
    diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un maître cylindre
    de frein défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule.
    Consultez la section symptômes pour évaluer l'urgence du remplacement.- agregat de freinage - capteur abs - cylindre de
    roue - disque de frein - etrier de frein - flexible de frein - interrupteur des feux de freins - kit de freins arriere
  S8: Maître-cylindre neuf ou échange standard ?L'échange standard est 30-40% moins cher. Qualité équivalente au neuf si le
    reconditionnement est fait par un spécialiste. Comment savoir si mon maître-cylindre est HS ?Pédale de frein qui s'enfonce
    lentement au feu rouge, niveau de liquide qui baisse sans fuite visible, pédale molle après purge. Tous les combien changer
    le maître-cylindre ?Pas de périodicité fixe. C'est une pièce durable (souvent plus de 200 000 km). À remplacer en cas
    de fuite interne ou défaillance. Peut-on changer le maître-cylindre soi-même ?Oui mais technique. Il faut purger tout
    le circuit après. Réglage de la garde de pédale parfois nécessaire. Comptez 2h. Quelle erreur éviter avec le maître-cylindre
    ?Ne jamais rouler avec une pédale qui s'enfonce (danger). Purger dans le bon ordre (roue la plus éloignée en premier).
    Utiliser du liquide de frein neuf.
  META: '{"og_title": "Maître-cylindre de frein : diagnostic pédale molle", "meta_title": "Maître-cylindre de frein : pédale
    molle, diagnostic et prix | AutoMecanik", "gate_report": "PASS", "schema_type": "HowTo", "og_description": "Pédale de
    frein molle ou qui s''enfonce ? Le maître- cylindre fuit peut-être. Diagnostic, purge et remplacement.", "primary_intent":
    "diagnostic", "meta_description": "Pédale de frein qui s''enfonce ? Fuite de liquide ? Le maître-cylindre est probablement
    HS. Diagnostic, bench bleeding et remplacement."}'
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
## Variantes et types
- hydraulique

## Matériaux
- EPDM
- aluminium

## Valeurs techniques de référence
- 18 mm
- 20 %
- 20 mm
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
