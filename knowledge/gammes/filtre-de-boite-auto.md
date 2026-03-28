---
category: filtration
slug: filtre-de-boite-auto
title: Filtre de boîte auto
pg_id: 416
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
  role: Filtrer l'huile de la boite automatique
  must_be_true:
  - filtrer
  - retenir
  - purifier
  must_not_contain:
  - injection
  - freinage
  - direction
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - filtre-a-air
  - filtre-a-huile
  - filtre-d-habitacle
  - filtre-a-carburant
  confusion_with:
  - term: autre-filtre
    difference: Chaque filtre a un role specifique (air, huile, habitacle, carburant, boite). Verifier le type exact avant
      commande.
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
  - ❌ "filtration parfaite"
  cost_range:
    min: 20
    max: 80
    currency: EUR
    unit: filtre
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
    description: Filtre conforme aux spécifications du fabricant de la boîte automatique. Finesse de filtration, capacité
      de débit et dimensions conformes. Fortement recommandé pour les boîtes à double embrayage (DSG,
  - tier: Équipementier reconnu (transmission)
    description: Fabricants spécialisés en composants de boîtes automatiques. Kit complet généralement disponible avec filtre,
      joint de carter et parfois la vis de vidange.
  - tier: Kit filtre adaptable
    description: Option économique pour les boîtes standards à convertisseur de couple. Vérifier impérativement la référence
      de la boîte (pas seulement le modèle de véhicule), la compatibilité avec l'huile ATF utilisé
  brands:
    premium:
    - Mann Filter
    - Mahle/Knecht
    - Hengst
    standard:
    - Bosch
    - Purflux
    - WIX
    budget:
    - Ridex
    - Valeo
diagnostic:
  symptoms:
  - id: S1
    label: Passages de vitesses brutaux ou tardifs
    severity: confort
  - id: S2
    label: Vibrations lors des changements de rapport
    severity: confort
  - id: S3
    label: Boite qui patine sous charge
    severity: confort
  - id: S4
    label: Huile atf brune ou odeur brule
    severity: confort
  - id: S5
    label: Voyant temperature boite
    severity: confort
  causes:
  - lecture codes defaut obd et diagnostic electronique
  - identifier origine fuite et verifier joints
  - verifier equilibrage et fixations
  quick_checks:
  - 'Observer : passages de vitesses brutaux ou tardifs ?'
  - Vibrations lors des changements de rapport ?
  - 'Observer : boite qui patine sous charge ?'
  - 'Observer : huile atf brune ou odeur brule ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Passages de vitesses brutaux ou tardifs
  - Vibrations lors des changements de rapport
  - Boite qui patine sous charge
  - Huile atf brune ou odeur brule
  - Voyant temperature boite
  good_practices:
  - Remplacement systematique selon intervalle constructeur
  - Ne pas souffler a l air comprime (endommage le media filtrant)
  - Controle visuel a chaque vidange ou entretien
  - Verifier l etancheite du boitier apres remplacement
rendering:
  pgId: '416'
  intro_title: A quoi sert Filtre de boîte auto ?
  risk_title: Pourquoi remplacer Filtre de boîte auto a temps ?
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
  - question: Filtre boîte auto OE ou adaptable ?
    answer: Privilégiez l'OE ou OES (ZF, Valeo). La boîte auto est sensible, un filtre de qualité inférieure peut causer des
      dégâts coûteux.
  - question: Comment savoir si le filtre de boîte auto est HS ?
    answer: Passages de vitesses brutaux ou tardifs, patinage de la boîte, voyant boîte auto allumé, huile ATF foncée ou odeur
      de brûlé.
  - question: Tous les combien changer le filtre de boîte auto ?
    answer: Entre 60 000 et 100 000 km selon constructeur. Toujours le changer lors de la vidange de boîte. Certaines boîtes
      scellées n'ont pas de filtre accessible.
  - question: Peut-on changer le filtre de boîte auto soi-même ?
    answer: Déconseillé aux débutants. Nécessite de vidanger l'huile ATF, déposer le carter, remplacer le joint. Procédure
      de remplissage stricte.
  - question: Quelle erreur éviter avec le filtre de boîte auto ?
    answer: Ne jamais mélanger différentes huiles ATF. Respecter le niveau exact. Ne pas oublier le joint de carter. Éviter
      les vidanges par gravité seule.
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
doc_id: 0f91a914-79f1-5a52-bb45-b2d6a87fa87d
content_hash: sha256:e20e153509fb7475
lang: fr
variants:
- name: Filtre standard papier
  aliases:
  - papier
  - standard
  functional_differences:
  - Usage normal
  - Remplacement a chaque entretien
- name: Filtre performance lavable
  aliases:
  - sport
  - K&N
  - BMC
  - lavable
  functional_differences:
  - Reutilisable apres nettoyage
  - Pour usage sportif
location_on_vehicle:
  area: Compartiment moteur (air, huile) ou habitacle (pollen)
  access: Par le dessus (capot) ou depuis la boite a gants
  adjacent_parts:
  - boitier filtre
  - durite admission
  - collecteur
installation:
  difficulty: facile
  time: 10 a 30 min
  tools:
  - tournevis
  - cle a filtre (huile)
  - chiffon
  prerequisite: Moteur froid pour filtre a huile
---

# Filtre de boîte auto - Guide Diagnostic Complet

## Fonction et Rôle

Filtrer l'huile de la boite automatique

**Actions principales:** filtrer, retenir, purifier

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- passages de vitesses brutaux ou tardifs
- vibrations lors des changements de rapport
- boite qui patine sous charge
- huile atf brune ou odeur brule
- voyant temperature boite

## Procédure de Diagnostic

Pour diagnostiquer un problème de filtre de boîte auto:

1. **Inspection visuelle** - Examiner l'état du filtre de boîte auto
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- boite-automatique
- huile-bva

## Critères de Compatibilité

Pour commander le bon filtre de boîte auto, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "filtration parfaite"

## FAQ

**Filtre boîte auto OE ou adaptable ?**
Privilégiez l'OE ou OES (ZF, Valeo). La boîte auto est sensible, un filtre de qualité inférieure peut causer des dégâts coûteux.

**Comment savoir si le filtre de boîte auto est HS ?**
Passages de vitesses brutaux ou tardifs, patinage de la boîte, voyant boîte auto allumé, huile ATF foncée ou odeur de brûlé.

**Tous les combien changer le filtre de boîte auto ?**
Entre 60 000 et 100 000 km selon constructeur. Toujours le changer lors de la vidange de boîte. Certaines boîtes scellées n'ont pas de filtre accessible.

**Peut-on changer le filtre de boîte auto soi-même ?**
Déconseillé aux débutants. Nécessite de vidanger l'huile ATF, déposer le carter, remplacer le joint. Procédure de remplissage stricte.

**Quelle erreur éviter avec le filtre de boîte auto ?**
Ne jamais mélanger différentes huiles ATF. Respecter le niveau exact. Ne pas oublier le joint de carter. Éviter les vidanges par gravité seule.


## Symptomes supplementaires

<!-- materialized-from-db diagnostic/transmission-boite.md 2026-02-15 -->
### Diagnostic - Transmission et boîte de vitesses

# Transmission et boîte de vitesses - Diagnostic complet

## Boîte manuelle

### Craquement au passage de vitesse
- **Synchroniseurs usés** : Craquement surtout sur un rapport précis (souvent 2ème ou 3ème). Pire à froid, s'améliore à chaud.
- **Huile de boîte inadaptée ou usée** : Vidange de boîte à effectuer (75W-80 ou 75W-90 selon constructeur).
- **Câble ou timonerie de commande usé** : Passage imprécis, sensation de flou dans le levier.

### Vitesse qui saute
- **Fourchette de sélection usée** : La vitesse se désengage spontanément sous charge.
- **Ressort de verrouillage cassé** : Le rapport ne tient plus en position.

### Bruit de roulement en boîte
- **Roulement d'arbre primaire usé** : Sifflement continu qui disparaît quand on appuie sur l'embrayage.
- **Roulement de sortie** : Bruit proportionnel à la vitesse du véhicule.

## Boîte automatique

### À-coups ou patinage
- **Niveau d'huile ATF incorrect** : Vérifier le niveau à chaud, moteur tournant au point mort.
- **Huile ATF usée** : Couleur marron foncé au lieu de rouge. Vidange recommandée.
- **Convertisseur de couple usé** : Patinage au démarrage, surchauffe de l'huile.

### Passage de rapports brutal
- **Calculateur de boîte** : Réinitialisation des adaptations parfois nécessaire.
- **Électrovannes de commande** : Corps de vannes encrassé ou électrovanne bloquée.

## Cardans et transmission

### Claquement en virage
- **Soufflet de cardan déchiré** : Graisse projetée visible sur la roue intérieure. Le cardan tourne sans lubrification.
- **Croisillon de cardan usé** : Claquement sec en accélération ou décélération dans les virages.

### Vibration à l'accélération
- **Cardan voilé** : Vibration proportionnelle à la vitesse.
- **Silent-bloc de transmission usé** : Vibrations transmises dans l'habitacle.

## Quand consulter un professionnel

- Boîte automatique en mode dégradé (bloquée sur un rapport)
- Fuite d'huile de boîte importante
- Craquement systématique sur tous les rapports
- Cardan cassé (roue qui ne tourne plus)
