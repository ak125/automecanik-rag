---
category: transmission
slug: cardan
title: Cardan
pg_id: 13
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
  role: Transmet le couple moteur aux roues tout en permettant les mouvements de suspension
  must_be_true:
  - transmettre
  - entrainer
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
  - joint-arbre-longitudinal
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
  - ❌ "plus de puissance"
  cost_range:
    min: 100
    max: 350
    currency: EUR
    unit: cardan complet
    source: catalogue automecanik
  brands:
    premium:
    - SKF
    - GKN/Spidan
    standard:
    - Febi
    - Meyle
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Claquement braquant accelerant marche arriere
    severity: confort
  - id: S2
    label: Vibrations ressenties vitesse constante
    severity: confort
  - id: S3
    label: Graisse noire visible jante passage
    severity: confort
  - id: S4
    label: Soufflet de cardan dechire ou fendu visible
    severity: confort
  - id: S5
    label: Bruit roulement change selon angle
    severity: confort
  - id: S6
    label: Plus de 150 000 km sans verification des soufflets
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - verifier equilibrage et fixations
  - remplacement preventif recommande
  quick_checks:
  - 'Observer : claquement braquant accelerant marche arriere ?'
  - Vibrations ressenties vitesse constante ?
  - 'Observer : graisse noire visible jante passage ?'
  - 'Observer : soufflet de cardan dechire ou fendu visible ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Claquement braquant accelerant marche arriere
  - Vibrations ressenties vitesse constante
  - Graisse noire visible jante passage
  - Soufflet de cardan dechire ou fendu visible
  - Bruit roulement change selon angle
  - Plus de 150 000 km sans verification des soufflets
  good_practices:
  - Verifier le niveau d huile de boite selon preconisation constructeur
  - Controle des soufflets de protection (pas de fuite de graisse)
  - Remplacement de la bague d etancheite en cas de fuite
  - Inspection des cardans et croisillons a chaque revision
rendering:
  pgId: '13'
  intro_title: A quoi sert Cardan ?
  risk_title: Pourquoi remplacer Cardan a temps ?
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
  - question: Cardan OE, OES ou échange standard ?
    answer: Les cardans OES (SKF, GKN, Lobro) sont de qualité équivalente à l'OE. L'échange standard est 30-50% moins cher
      avec une qualité similaire.
  - question: Comment savoir si mon cardan est usé ?
    answer: Claquement en braquant et accélérant (manœuvres), vibrations à vitesse constante, graisse visible sur la jante
      ou sous le passage de roue.
  - question: Tous les combien changer le cardan ?
    answer: Pas de périodicité fixe. Un cardan avec soufflets intacts peut durer 200 000+ km. À remplacer dès qu'un joint
      claque ou vibre.
  - question: Peut-on changer un cardan soi-même ?
    answer: Oui mais technique. Dépose roue, étrier, moyeu. Attention à la vis de moyeu (très serrée, souvent à usage unique).
      Prévoir 2h par côté.
  - question: Quelle erreur éviter avec le cardan ?
    answer: Ne pas réutiliser l'écrou de moyeu usagé. Vérifier les soufflets avant de changer le cardan complet. Ne pas forcer
      sur le joint.
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
doc_id: bc2e108d-c21a-5f6c-b590-75411650de5a
content_hash: sha256:718a4b1bdda0e76f
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

# Cardan - Guide Diagnostic Complet

## Fonction et Rôle

Transmet le couple moteur aux roues tout en permettant les mouvements de suspension

**Actions principales:** transmettre, entrainer

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement braquant accelerant marche arriere**
  claquement braquant accelerant marche arriere

### 🟢 Autres Symptômes

- vibrations ressenties vitesse constante
- graisse noire visible jante passage
- soufflet de cardan dechire ou fendu visible
- bruit roulement change selon angle
- plus de 150 000 km sans verification des soufflets

## Procédure de Diagnostic

Pour diagnostiquer un problème de cardan:

1. **Inspection visuelle** - Examiner l'état du cardan
2. **Test dynamique** - Vérifier les bruits en roulant
3. **Contrôle du jeu** - Examiner l'usure des articulations
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- bague-d-etancheite-cardan
- soufflet-de-cardan

## Critères de Compatibilité

Pour commander le bon cardan, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"

## FAQ

**Cardan OE, OES ou échange standard ?**
Les cardans OES (SKF, GKN, Lobro) sont de qualité équivalente à l'OE. L'échange standard est 30-50% moins cher avec une qualité similaire.

**Comment savoir si mon cardan est usé ?**
Claquement en braquant et accélérant (manœuvres), vibrations à vitesse constante, graisse visible sur la jante ou sous le passage de roue.

**Tous les combien changer le cardan ?**
Pas de périodicité fixe. Un cardan avec soufflets intacts peut durer 200 000+ km. À remplacer dès qu'un joint claque ou vibre.

**Peut-on changer un cardan soi-même ?**
Oui mais technique. Dépose roue, étrier, moyeu. Attention à la vis de moyeu (très serrée, souvent à usage unique). Prévoir 2h par côté.

**Quelle erreur éviter avec le cardan ?**
Ne pas réutiliser l'écrou de moyeu usagé. Vérifier les soufflets avant de changer le cardan complet. Ne pas forcer sur le joint.


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
