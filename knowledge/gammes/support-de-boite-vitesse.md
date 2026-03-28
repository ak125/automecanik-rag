---
category: support_moteur
slug: support-de-boite-vitesse
title: Support de boîte vitesse
pg_id: 249
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
  role: Supporter et fixer la boite de vitesses au chassis
  must_be_true:
  - supporter
  - fixer
  - amortir
  must_not_contain:
  - injection
  - freinage
  - climatisation
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - amortisseur
  - ressort-de-suspension
  - bras-de-suspension
  - rotule-de-suspension
  - barre-stabilisatrice
  - biellette-de-barre-stabilisatrice
  confusion_with:
  - term: piece-de-suspension-voisine
    difference: Les pieces de suspension travaillent ensemble mais ont des references distinctes. Verifier la position (avant/arriere,
      gauche/droite).
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
  - ❌ "zero vibration"
  cost_range:
    min: 30
    max: 120
    currency: EUR
    unit: pièce
    source: catalogue automecanik
  brands:
    premium:
    - Hutchinson
    - Vibracoustic (Continental)
    - Anvis
    standard:
    - Lemforder (ZF)
    - Corteco
    - Swag
    budget:
    - Febi Bilstein
    - Meyle
    - Sasic
  quality_tiers:
  - tier: Origine constructeur
    description: Supports de boite de vitesses identiques a la premiere monte, avec elastomere calibre pour la frequence de
      vibration du groupe motopropulseur.
  - tier: Equipementier qualite OE
    description: Supports fabriques par des equipementiers premiere monte avec elastomere de qualite equivalente et durete
      Shore conforme.
  - tier: Adaptable qualite reconnue
    description: Supports compatibles avec verification de la durete de l elastomere et des dimensions de fixation avant montage.
diagnostic:
  symptoms:
  - id: S1
    label: Vibrations ressenties sur le levier de vitesses
    severity: confort
  - id: S2
    label: Caoutchouc du support visiblement deteriore
    severity: confort
  - id: S3
    label: Claquement ou bruit sourd au passage des rapports
    severity: confort
  - id: S4
    label: Boite de vitesses qui semble bouger anormalement
    severity: confort
  - id: S5
    label: Sensation d a-coups a l embrayage ou debrayage
    severity: confort
  - id: S6
    label: Plus de 100 000 km ou supports moteur a changer
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - verifier equilibrage et fixations
  - remplacement preventif recommande
  quick_checks:
  - Vibrations ressenties sur le levier de vitesses ?
  - 'Observer : caoutchouc du support visiblement deteriore ?'
  - 'Observer : claquement ou bruit sourd au passage des rapports ?'
  - 'Observer : boite de vitesses qui semble bouger anormalement ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Vibrations ressenties sur le levier de vitesses
  - Caoutchouc du support visiblement deteriore
  - Claquement ou bruit sourd au passage des rapports
  - Boite de vitesses qui semble bouger anormalement
  - Sensation d a-coups a l embrayage ou debrayage
  - Plus de 100 000 km ou supports moteur a changer
  good_practices:
  - Controle visuel des fuites et deformations a chaque revision
  - Remplacement par paire (meme essieu) pour equilibre du vehicule
  - Faire verifier la geometrie apres remplacement
  - Inspection des silent-blocs et des rotules associees
rendering:
  pgId: '249'
  intro_title: A quoi sert Support de boîte vitesse ?
  risk_title: Pourquoi remplacer Support de boîte vitesse a temps ?
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
  - question: Support de boîte OE, OES ou adaptable ?
    answer: Les supports OES (Lemförder, Corteco) sont de qualité première monte. adaptables (Febi, Meyle) offrent un bon
      rapport qualité/prix. Vérifier la compatibilité boîte manuelle ou automatique.
  - question: Comment savoir si le support de boîte est HS ?
    answer: Vibrations en roulant, bruit de claquement au passage des vitesses, levier de vitesses qui vibre, à-coups à l'embrayage.
  - question: Tous les combien changer le support de boîte ?
    answer: Pas de périodicité fixe. Durée de vie 100 000 à 180 000 km. À remplacer en même temps que les supports moteur
      si usé.
  - question: Peut-on changer le support de boîte soi-même ?
    answer: Oui, souvent plus accessible que les supports moteur. Soutenir la boîte avec un cric. Prévoir 1h environ.
  - question: Quelle erreur éviter avec le support de boîte ?
    answer: Ne pas oublier de vérifier l'état de la biellette de réaction si présente. Serrer au couple recommandé.
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
doc_id: 526fe560-efc4-5819-94a5-29e2b902265f
content_hash: sha256:a7b239b6157af006
lang: fr
variants:
- name: Version gaz
  aliases:
  - gaz
  - gas-a-just
  functional_differences:
  - Meilleure tenue de route
  - Plus ferme que l huile
- name: Version huile
  aliases:
  - huile
  - hydraulique
  functional_differences:
  - Confort de conduite superieur
  - Moins cher que le gaz
location_on_vehicle:
  area: Entre la roue et la carrosserie (avant et/ou arriere)
  access: Par le dessous (pont elevateur) ou demontage roue
  adjacent_parts:
  - amortisseur
  - ressort
  - bras
  - rotule
installation:
  difficulty: moyen a difficile
  time: 1h a 2h par cote
  tools:
  - compresseur de ressort
  - cle a douille
  - cle dynamometrique
  - arrache-rotule
  prerequisite: Pont elevateur recommande, vehicule decharge
---

# Support de boîte vitesse - Guide Diagnostic Complet

## Fonction et Rôle

Supporter et fixer la boite de vitesses au chassis

**Actions principales:** supporter, fixer, amortir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement ou bruit sourd au passage des rapports**
  claquement ou bruit sourd au passage des rapports

### 🟢 Autres Symptômes

- vibrations ressenties sur le levier de vitesses
- caoutchouc du support visiblement deteriore
- boite de vitesses qui semble bouger anormalement
- sensation d a-coups a l embrayage ou debrayage
- plus de 100 000 km ou supports moteur a changer

## Procédure de Diagnostic

Pour diagnostiquer un problème de support de boîte vitesse:

1. **Inspection visuelle** - Examiner l'état du support de boîte vitesse
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- support-moteur
- boite-de-vitesses

## Critères de Compatibilité

Pour commander le bon support de boîte vitesse, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "zero vibration"

## FAQ

**Support de boîte OE, OES ou adaptable ?**
Les supports OES (Lemförder, Corteco) sont de qualité première monte. adaptables (Febi, Meyle) offrent un bon rapport qualité/prix. Vérifier la compatibilité boîte manuelle ou automatique.

**Comment savoir si le support de boîte est HS ?**
Vibrations en roulant, bruit de claquement au passage des vitesses, levier de vitesses qui vibre, à-coups à l'embrayage.

**Tous les combien changer le support de boîte ?**
Pas de périodicité fixe. Durée de vie 100 000 à 180 000 km. À remplacer en même temps que les supports moteur si usé.

**Peut-on changer le support de boîte soi-même ?**
Oui, souvent plus accessible que les supports moteur. Soutenir la boîte avec un cric. Prévoir 1h environ.

**Quelle erreur éviter avec le support de boîte ?**
Ne pas oublier de vérifier l'état de la biellette de réaction si présente. Serrer au couple recommandé.


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
