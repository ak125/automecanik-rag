---
category: freinage
slug: kit-de-freins-arriere
title: Kit de freins arrière
pg_id: 3859
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
  last_enriched_by: skill:phase5-gates-skf-trw
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Ensemble complet de freinage arrière
  must_be_true:
  - freiner
  - ralentir
  - immobiliser
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
  - ❌ "meilleur freinage"
  cost_range:
    min: 40
    max: 150
    currency: EUR
    unit: l'unite
    source: estimation categorie
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
    label: Frein a main qui ne tient plus correctement
    severity: securite
  - id: S2
    label: Freinage arriere bruyant ou qui grince
    severity: securite
  - id: S3
    label: Fuite de liquide au niveau des roues arriere
    severity: confort
  - id: S4
    label: Ressorts de rappel casses ou detendus
    severity: confort
  - id: S5
    label: Freinage arriere desequilibre
    severity: securite
  - id: S6
    label: Crissement metallique a l arriere
    severity: confort
  - id: S7
    label: Odeur de brule apres freinages repetes
    severity: securite
  - id: S8
    label: Plus de 80 000 km depuis le dernier changement
    severity: confort
  causes:
  - identifier origine fuite et verifier joints
  - remplacement preventif recommande
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  - 'kilometrage eleve ou usure visible : remplacement preventif recommande'
  depose_steps: []
  quick_checks:
  - 'Observer : frein a main qui ne tient plus correctement ?'
  - 'Observer : freinage arriere bruyant ou qui grince ?'
  - Fuite de liquide au niveau des roues arriere ?
  - 'Observer : ressorts de rappel casses ou detendus ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Frein a main qui ne tient plus correctement
  - Freinage arriere bruyant ou qui grince
  - Fuite de liquide au niveau des roues arriere
  - Ressorts de rappel casses ou detendus
  - Freinage arriere desequilibre
  - Crissement metallique a l arriere
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '3859'
  intro_title: A quoi sert Kit de freins arrière ?
  risk_title: Pourquoi remplacer Kit de freins arrière a temps ?
  risk_explanation: '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
  risk_consequences:
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
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
  - question: 'Kit complet ou pièces séparées : que choisir ?'
    answer: Le kit complet est souvent 15-20% moins cher que les pièces séparées. Il garantit la compatibilité entre mâchoires,
      cylindres et ressorts.
  - question: Comment savoir si je dois changer tout le kit arrière ?
    answer: Frein à main inefficace, freinage arrière bruyant, fuite de cylindre de roue, ressorts cassés ou détendus visibles.
  - question: Tous les combien changer le kit de frein arrière ?
    answer: Entre 80 000 et 120 000 km. Profitez du changement de mâchoires pour inspecter cylindres et ressorts. Changez
      le kit si douteux.
  - question: Peut-on changer le kit de frein arrière soi-même ?
    answer: Oui mais technique. Dépose du tambour, des ressorts, des mâchoires et cylindres. Comptez 2h par côté. Photos avant
      démontage conseillées.
  - question: Quelle erreur éviter avec le kit de frein arrière ?
    answer: Ne pas mélanger pièces de différents kits. Respecter le sens de montage des mâchoires (primaire/secondaire). Purger
      après si cylindres changés.
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
doc_id: 0929134e-a273-51c7-9d06-2849f902f321
content_hash: sha256:9e7eb822c4d4dedc
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
  _source: Gates / SKF / TRW-ZF (donnees techniques constructeur)
  _validation_status: oem_verified
  _enriched_at: '2026-03-30'
  technical_notes:
    diametre_tambour: '180, 200, 203, 228 mm selon vehicule — mesurer avant commande'
    garnitures_machoires: 'organique (standard) ou semi-metallique (utilitaire charge)'
    ressorts: 'raideur calibree constructeur — NE PAS reutiliser les anciens'
    rodage: '200 km freinages progressifs, ne pas freiner fort'
  materials:
  - composant: machoires
    materiau: support acier + garniture organique collee ou rivetee
  - composant: cylindre de roue
    materiau: corps fonte d'aluminium + pistons acier + joints EPDM
  - composant: ressorts
    materiau: acier ressort traite thermiquement
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le kit de freins arrière regroupe l''ensemble des pièces nécessaires au
    remplacement complet du système de freinage arrière à tambour : mâchoires de
    frein, cylindres de roue, ressorts de rappel, accessoires de fixation et
    parfois les tambours. Le kit garantit la compatibilité entre toutes les
    pièces. Niveau de difficulté : Intermédiaire — plus complexe que les freins
    à disque car le mécanisme à tambour comporte de nombreux ressorts et clips.
    Comptez 1h30 à 2h30 par côté. Outils : jeu de pinces à ressorts de frein,
    repousse-piston de cylindre, clé à tuyauter (raccord hydraulique), clé
    dynamométrique. Pièces liées : tambour de frein, câble de frein à main,
    liquide de frein (purge obligatoire).
  S2: >-
    Intervalle : environ 80 000 km ou selon usure. Les freins arrière s''usent
    moins vite que les freins avant (30% de l''effort de freinage seulement).
    Symptômes de défaillance : - Frein à main qui ne tient plus correctement —
    garnitures usées ou câble détendu- Freinage arrière bruyant ou qui grince —
    garniture au métal, contact métal/métal sur le tambour- Fuite de liquide au
    niveau des roues arrière — cylindre de roue percé, joints internes HS-
    Ressorts de rappel cassés ou détendus — les mâchoires ne reviennent plus en
    position, frottement permanent- Freinage arrière déséquilibré — le véhicule
    dévie au freinage, un côté freine plus que l''autre- Odeur de brûlé après
    freinages répétés — surchauffe par frottement permanent (ressort cassé ou
    cylindre grippé)
  S3: >-
    Pour choisir le bon kit de freins arrière : - Kit complet vs pièces séparées
    : le kit complet est souvent 15-20% moins cher que les pièces séparées et
    garantit la compatibilité mâchoires + cylindres + ressorts- Diamètre du
    tambour : vérifier le diamètre exact (180, 200, 203, 228 mm selon véhicule)
    — un kit de mauvais diamètre ne se monte pas- Avec ou sans cylindres :
    certains kits incluent les cylindres de roue, d''autres non — si les
    cylindres fuient, prendre le kit avec cylindres- Marques : Brembo, ATE, TRW
    (premium), Bosch, Ferodo, Textar (standard) — les pièces de freinage sont
    des organes de sécurité, privilégier la qualité- Budget : 40 à 150 EUR le
    kit — le surcoût d''un kit premium est marginal face au coût de main
    d''oeuvre
  S4_DEPOSE: >-
    1. Lever le véhicule, déposer les roues arrière, sécuriser sur chandelles.
    2. Desserrer le frein à main. 3. Retirer le tambour de frein (frapper
    légèrement si collé par la corrosion). 4. Photographier le montage des
    ressorts et clips AVANT démontage — le remontage est complexe sans repère.
    5. Déposer les ressorts de rappel et de maintien avec la pince spécifique.
    6. Décrocher le câble de frein à main de la mâchoire. 7. Débrancher le
    raccord hydraulique du cylindre de roue (clé à tuyauter, obturer pour
    limiter la perte de liquide). 8. Déposer les mâchoires et le cylindre de
    roue.
  S5: >-
    Erreurs fréquentes avec le kit de freins arrière : - Ne pas photographier le
    montage des ressorts avant démontage — le remontage d''un mécanisme à
    tambour est un puzzle sans repère visuel- Oublier de purger le circuit de
    frein après remplacement des cylindres — l''air dans le circuit rend la
    pédale molle et le freinage arrière inefficace- Ne pas remplacer les
    ressorts et clips avec les mâchoires — des ressorts fatigués sur des
    mâchoires neuves provoquent un frottement permanent et une surchauffe-
    Monter le kit sans régler le frein à main — le rattrapage de jeu
    mâchoires/tambour est indispensable pour que le frein de parking tienne-
    Remplacer un seul côté — toujours remplacer les deux côtés (gauche + droite)
    pour un freinage équilibré- Ne pas vérifier l''état du tambour — un tambour
    ovalisé ou rainuré use les mâchoires neuves prématurément. Mesurer au pied à
    coulisse
  S6: >-
    Après le remplacement du kit de freins arrière : - Purge : purger le circuit
    hydraulique arrière (commencer par la roue la plus éloignée du maître-
    cylindre)- Frein à main : régler le câble et vérifier que le frein de
    parking tient le véhicule en pente (3 à 5 clics)- Rodage : 200 km de
    freinages progressifs — ne pas freiner brusquement pendant le rodage des
    garnitures- Test freinage : à 30 km/h, freiner progressivement — le véhicule
    ne doit pas dévier. Si déviation = purge incomplète ou montage asymétrique-
    Vérification étanchéité : après 50 km, vérifier l''absence de fuite au
    niveau des raccords hydrauliques et des cylindres
---

# Kit de freins arrière - Guide Diagnostic Complet

## Fonction et Rôle

Ensemble complet de freinage arrière

**Actions principales:** freiner, ralentir, immobiliser

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Ressorts de rappel casses ou detendus**
  ressorts de rappel casses ou detendus

### 🟡 Symptômes de Sécurité

- **Frein a main qui ne tient plus correctement**
  frein a main qui ne tient plus correctement
- **Freinage arriere bruyant ou qui grince**
  freinage arriere bruyant ou qui grince
- **Freinage arriere desequilibre**
  freinage arriere desequilibre
- **Odeur de brule apres freinages repetes**
  odeur de brule apres freinages repetes

### 🟢 Autres Symptômes

- fuite de liquide au niveau des roues arriere
- crissement metallique a l arriere
- plus de 80 000 km depuis le dernier changement

## Procédure de Diagnostic

Pour diagnostiquer un problème de kit de freins arrière:

1. **Inspection visuelle** - Examiner l'état du kit de freins arrière
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- cable-de-frein-a-main
- capteur-abs
- cylindre-de-roue
- flexible-de-frein
- interrupteur-des-feux-de-freins
- machoires-de-frein
- tambour-de-frein

## Critères de Compatibilité

Pour commander le bon kit de freins arrière, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleur freinage"

## FAQ

**Kit complet ou pièces séparées : que choisir ?**
Le kit complet est souvent 15-20% moins cher que les pièces séparées. Il garantit la compatibilité entre mâchoires, cylindres et ressorts.

**Comment savoir si je dois changer tout le kit arrière ?**
Frein à main inefficace, freinage arrière bruyant, fuite de cylindre de roue, ressorts cassés ou détendus visibles.

**Tous les combien changer le kit de frein arrière ?**
Entre 80 000 et 120 000 km. Profitez du changement de mâchoires pour inspecter cylindres et ressorts. Changez le kit si douteux.

**Peut-on changer le kit de frein arrière soi-même ?**
Oui mais technique. Dépose du tambour, des ressorts, des mâchoires et cylindres. Comptez 2h par côté. Photos avant démontage conseillées.

**Quelle erreur éviter avec le kit de frein arrière ?**
Ne pas mélanger pièces de différents kits. Respecter le sens de montage des mâchoires (primaire/secondaire). Purger après si cylindres changés.


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
