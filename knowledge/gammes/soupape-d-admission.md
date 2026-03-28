---
category: moteur
slug: soupape-d-admission
title: Soupape d'admission
pg_id: 1269
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-01'
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
  role: Ouvrir et fermer le passage des gaz d'admission
  must_be_true:
  - ouvrir
  - fermer
  - admettre
  must_not_contain:
  - echappement
  - carburant
  - injection
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - ouvrir
  - fermer
  - admettre
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
    min: 15
    max: 50
    currency: EUR
    unit: soupape
    source: catalogue automecanik
  brands:
    premium:
    - Mahle Original
    - TRW Engine Component
    - AE (Federal-Mogul)
    standard:
    - Freccia
    - Intervalves
    - SM (Societe Mecanique)
    budget:
    - Osvat
    - BGA
    - AMP
  quality_tiers:
  - tier: Origine constructeur
    description: Soupapes identiques a celles montees en usine. Specifications exactes de longueur, diametre de tete et de
      queue respectees.
  - tier: Equipementier qualite OE
    description: Fabricants fournissant les constructeurs en premiere monte. Memes tolerances dimensionnelles et metallurgiques.
  - tier: Adaptable qualite reconnue
    description: Soupapes conformes aux cotes constructeur, fabriquees par des equipementiers independants avec controle qualite.
diagnostic:
  symptoms:
  - id: S1
    label: Perte de compression sur un ou plusieurs cylindres
    severity: confort
  - id: S2
    label: Rates d allumage persistants
    severity: confort
  - id: S3
    label: Claquement au niveau de la culasse
    severity: confort
  - id: S4
    label: Consommation d huile anormale guides uses
    severity: confort
  - id: S5
    label: Fumee bleue a l echappement
    severity: confort
  - id: S6
    label: Casse de courroie de distribution controle
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  quick_checks:
  - 'Observer : perte de compression sur un ou plusieurs cylindres ?'
  - 'Observer : rates d allumage persistants ?'
  - 'Observer : claquement au niveau de la culasse ?'
  - 'Observer : consommation d huile anormale guides uses ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Perte de compression sur un ou plusieurs cylindres
  - Rates d allumage persistants
  - Claquement au niveau de la culasse
  - Consommation d huile anormale guides uses
  - Fumee bleue a l echappement
  - Casse de courroie de distribution controle
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '1269'
  intro_title: A quoi sert Soupape d'admission ?
  risk_title: Pourquoi remplacer Soupape d'admission a temps ?
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
  - question: Soupape d'admission OE ou adaptable ?
    answer: Les soupapes OES (AE, Freccia, TRW) sont fiables. Vérifiez les cotes exactes (longueur, diamètre tête et queue).
      Ne pas mélanger les qualités.
  - question: Comment savoir si une soupape d'admission est HS ?
    answer: Perte de compression sur un cylindre, claquement, ratés d'allumage, consommation d'huile excessive (guide usé).
  - question: Tous les combien changer les soupapes d'admission ?
    answer: Pas de périodicité. Durée de vie 200 000+ km. Remplacement lors d'une réfection culasse ou après casse distribution.
  - question: Peut-on changer une soupape soi-même ?
    answer: Non recommandé. Nécessite un lève-soupapes, une rectification des sièges, et un contrôle d'étanchéité. Travail
      de spécialiste.
  - question: Quelle erreur éviter avec les soupapes ?
    answer: Ne jamais rodé une soupape neuve sur un siège usé. Remplacer aussi les guides si jeu excessif. Contrôler la planéité
      de la culasse.
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
doc_id: 0c8f3298-e12a-5181-b7f6-7d345dd0673d
content_hash: sha256:6b580f910bee5e46
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
  area: Sur le vehicule (position variable selon modele)
  access: Consulter la revue technique du vehicule
  adjacent_parts:
  - pieces adjacentes du meme systeme
installation:
  difficulty: variable
  time: consulter revue technique
  tools:
  - outillage standard
  prerequisite: Consulter la procedure constructeur
---

# Soupape d'admission - Guide Diagnostic Complet

## Fonction et Rôle

Ouvrir et fermer le passage des gaz d'admission

**Actions principales:** ouvrir, fermer, admettre

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement au niveau de la culasse**
  claquement au niveau de la culasse
- **Casse de courroie de distribution controle**
  casse de courroie de distribution controle

### 🟢 Autres Symptômes

- perte de compression sur un ou plusieurs cylindres
- rates d allumage persistants
- consommation d huile anormale guides uses
- fumee bleue a l echappement

## Procédure de Diagnostic

Pour diagnostiquer un problème de soupape d'admission:

1. **Inspection visuelle** - Examiner l'état du soupape d'admission
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bagues-d-etancheite-moteur
- joint-de-cache-culbuteurs
- joint-de-collecteur
- joint-de-culasse
- poulie-d-arbre-a-came
- poussoir-de-soupape
- soupape-d-echappement

## Critères de Compatibilité

Pour commander le bon soupape d'admission, vous devez connaître:

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

**Soupape d'admission OE ou adaptable ?**
Les soupapes OES (AE, Freccia, TRW) sont fiables. Vérifiez les cotes exactes (longueur, diamètre tête et queue). Ne pas mélanger les qualités.

**Comment savoir si une soupape d'admission est HS ?**
Perte de compression sur un cylindre, claquement, ratés d'allumage, consommation d'huile excessive (guide usé).

**Tous les combien changer les soupapes d'admission ?**
Pas de périodicité. Durée de vie 200 000+ km. Remplacement lors d'une réfection culasse ou après casse distribution.

**Peut-on changer une soupape soi-même ?**
Non recommandé. Nécessite un lève-soupapes, une rectification des sièges, et un contrôle d'étanchéité. Travail de spécialiste.

**Quelle erreur éviter avec les soupapes ?**
Ne jamais rodé une soupape neuve sur un siège usé. Remplacer aussi les guides si jeu excessif. Contrôler la planéité de la culasse.
