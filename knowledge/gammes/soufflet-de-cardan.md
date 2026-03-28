---
category: transmission
slug: soufflet-de-cardan
title: Soufflet de Cardan
pg_id: 193
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
  role: Protege le joint de cardan et retient la graisse de lubrification
  must_be_true:
  - proteger
  - etancher
  - contenir
  must_not_contain:
  - injection
  - freinage
  - climatisation
  - allumage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - cardan
  - roulement-de-roue
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
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
  - ❌ "transmission parfaite"
  cost_range:
    min: 15
    max: 50
    currency: EUR
    unit: soufflet
    source: catalogue automecanik
  brands:
    premium:
    - GKN (Loebro)
    - SKF
    - NTN-SNR
    standard:
    - Spidan
    - Febi Bilstein
    - Meyle
    budget:
    - Sasic
    - Topran
    - Maxgear
  quality_tiers:
  - tier: Origine (OE)
    description: Soufflets fabriques par l'equipementier d'origine. Caoutchouc haute resistance, diametre et longueur identiques
      a la piece constructeur. Graisse specifique incluse.
  - tier: Qualite equivalente OE (OES)
    description: Equipementiers reconnus en transmission. Soufflets en caoutchouc ou thermoplastique de qualite equivalente,
      kit avec colliers et graisse.
  - tier: Adaptable de qualite
    description: Marques fiables en entree de gamme. Verifier le diametre exact et le type (cote roue ou cote boite). Kit
      complet avec colliers et graisse recommande.
diagnostic:
  symptoms:
  - id: S1
    label: Graisse noire visible sur la jante interieure
    severity: confort
  - id: S2
    label: Soufflet fendu dechire ou decolle visible
    severity: confort
  - id: S3
    label: Claquement en braquant joint deja endommage
    severity: confort
  - id: S4
    label: Odeur de graisse brulee pres de la roue
    severity: confort
  - id: S5
    label: Vibrations au volant a vitesse constante
    severity: confort
  - id: S6
    label: Plus controle visuel soufflets
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - verifier equilibrage et fixations
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'vibrations anormales : verifier equilibrage et fixations'
  quick_checks:
  - 'Observer : graisse noire visible sur la jante interieure ?'
  - 'Observer : soufflet fendu dechire ou decolle visible ?'
  - 'Observer : claquement en braquant joint deja endommage ?'
  - Odeur de graisse brulee pres de la roue ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Graisse noire visible sur la jante interieure
  - Soufflet fendu dechire ou decolle visible
  - Claquement en braquant joint deja endommage
  - Odeur de graisse brulee pres de la roue
  - Vibrations au volant a vitesse constante
  - Plus controle visuel soufflets
  good_practices:
  - Verifier le niveau d huile de boite selon preconisation constructeur
  - Controle des soufflets de protection (pas de fuite de graisse)
  - Remplacement de la bague d etancheite en cas de fuite
  - Inspection des cardans et croisillons a chaque revision
rendering:
  pgId: '193'
  intro_title: A quoi sert Soufflet de Cardan ?
  risk_title: Pourquoi remplacer Soufflet de Cardan a temps ?
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
  - question: Soufflet de cardan OE ou adaptable ?
    answer: 'Les soufflets OES (GKN, SKF) ou adaptables (Spidan, Febi) sont fiables. Vérifiez le diamètre exact et le type
      : côté roue ou côté boîte.'
  - question: Comment savoir si mon soufflet est percé ?
    answer: Graisse noire sur la jante ou le passage de roue, soufflet visiblement fendu ou déchiré, fuite de graisse sous
      le véhicule.
  - question: Tous les combien vérifier les soufflets ?
    answer: Contrôle visuel à chaque révision ou passage au contrôle technique. Un soufflet peut se fendre sans prévenir suite
      à un choc.
  - question: Peut-on changer un soufflet de cardan seul ?
    answer: 'Oui si le joint n''est pas usé. Opération technique : dépose du cardan, nettoyage du joint, regraissage, montage
      du soufflet neuf.'
  - question: Quelle erreur éviter avec le soufflet ?
    answer: Ne pas attendre si le soufflet est percé. Utiliser la graisse spécifique fournie. Vérifier les deux soufflets
      (côté roue et côté boîte).
  quality:
    score: 60
    source: script:rag-upgrade-v4
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
doc_id: 50d7977f-f03f-5a93-89f5-2fd2270058a3
content_hash: sha256:63493ca7589a6996
lang: fr
variants:
- name: Version OE (origine)
  aliases:
  - OE
  - constructeur
  functional_differences:
  - Reference constructeur exacte
  - Garantie et compatibilite maximales
- name: Version equivalente OES
  aliases:
  - OES
  - equipementier
  functional_differences:
  - Qualite equivalente, prix aftermarket
  - Equipementier de premier monte
location_on_vehicle:
  area: Sous le vehicule, relie la boite aux roues
  access: Par le dessous (pont elevateur)
  adjacent_parts:
  - cardan
  - soufflet
  - roulement de roue
  - boite
installation:
  difficulty: difficile
  time: 1h a 3h
  tools:
  - pont elevateur
  - cle a douille
  - arrache-cardan
  prerequisite: Vidange huile de boite si cardan depose
---

# Soufflet de Cardan - Guide Diagnostic Complet

## Fonction et Rôle

Protege le joint de cardan et retient la graisse de lubrification

**Actions principales:** proteger, etancher, contenir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement en braquant joint deja endommage**
  claquement en braquant joint deja endommage

### 🟢 Autres Symptômes

- graisse noire visible sur la jante interieure
- soufflet fendu dechire ou decolle visible
- odeur de graisse brulee pres de la roue
- vibrations au volant a vitesse constante
- plus controle visuel soufflets

## Procédure de Diagnostic

Pour diagnostiquer un problème de soufflet de cardan:

1. **Inspection visuelle** - Examiner l'état du soufflet de cardan
2. **Test dynamique** - Vérifier les bruits en roulant
3. **Contrôle du jeu** - Examiner l'usure des articulations


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- cardan

## Critères de Compatibilité

Pour commander le bon soufflet de cardan, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "transmission parfaite"

## FAQ

**Soufflet de cardan OE ou adaptable ?**
Les soufflets OES (GKN, SKF) ou adaptables (Spidan, Febi) sont fiables. Vérifiez le diamètre exact et le type : côté roue ou côté boîte.

**Comment savoir si mon soufflet est percé ?**
Graisse noire sur la jante ou le passage de roue, soufflet visiblement fendu ou déchiré, fuite de graisse sous le véhicule.

**Tous les combien vérifier les soufflets ?**
Contrôle visuel à chaque révision ou passage au contrôle technique. Un soufflet peut se fendre sans prévenir suite à un choc.

**Peut-on changer un soufflet de cardan seul ?**
Oui si le joint n'est pas usé. Opération technique : dépose du cardan, nettoyage du joint, regraissage, montage du soufflet neuf.

**Quelle erreur éviter avec le soufflet ?**
Ne pas attendre si le soufflet est percé. Utiliser la graisse spécifique fournie. Vérifier les deux soufflets (côté roue et côté boîte).


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
