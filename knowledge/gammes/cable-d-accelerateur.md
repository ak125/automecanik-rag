---
category: accessoires
slug: cable-d-accelerateur
title: Câble d'accélérateur
pg_id: 618
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
  last_enriched_by: script:rag-fill-remaining-gaps
  last_enriched_at: '2026-03-28'
domain:
  role: Transmet la commande d'accélération de la pédale au papillon
  must_be_true:
  - transmettre
  - actionner
  - commander
  must_not_contain:
  - injection
  - papillon electronique
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - transmettre
  - actionner
  - commander
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de compatibilite
    pour confirmer Câble d'accélérateur.
  - Verifier la reference OE ou equivalence constructeur pour le vehicule exact
  - Comparer les dimensions et le type de montage avec la piece d origine
  - Choisir un equipementier reconnu pour garantir qualite et compatibilite
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "plus de puissance"
  cost_range:
    min: 50
    max: 300
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
    description: 'Câble conforme aux plans constructeur : longueur totale, longueur de gaine, embouts et course libre identiques
      à l''origine. Garantit la réponse accélérateur sans jeu excessif.'
  - tier: Qualité équivalente OE
    description: Câble fabriqué par un équipementier spécialisé respectant les longueurs et la résistance à la traction d'origine.
      Gaine traitée contre la corrosion.
  - tier: Adaptable compatible
    description: Câble universel à ajustement possible. Vérifier la longueur totale, la longueur de gaine et la compatibilité
      des embouts avant montage.
  brands:
    premium:
    - Bosch
    - Valeo
    standard:
    - Febi
    - Meyle
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Pedale d accelerateur dure ou rigide
    severity: confort
  - id: S2
    label: Reponse moteur retardee a l acceleration
    severity: confort
  - id: S3
    label: Point dur lors de l enfoncement de la pedale
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'Usure ou defaillance causant : pedale d accelerateur dure ou rigide'
  - 'Usure ou defaillance causant : reponse moteur retardee a l acceleration'
  quick_checks:
  - 'Observer : pedale d accelerateur dure ou rigide ?'
  - 'Observer : reponse moteur retardee a l acceleration ?'
  - 'Observer : point dur lors de l enfoncement de la pedale ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Pedale d accelerateur dure ou rigide
  - Reponse moteur retardee a l acceleration
  - Point dur lors de l enfoncement de la pedale
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '618'
  intro_title: A quoi sert Câble d'accélérateur ?
  risk_title: Pourquoi remplacer Câble d'accélérateur a temps ?
  risk_explanation: '**Défaillance progressive** - Usure normale due à l''utilisation'
  risk_consequences:
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
  - question: Comment choisir Câble d'accélérateur compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Câble d'accélérateur ?
    answer: En cas de pedale d accelerateur dure ou rigide ou de degradation mesurable, il faut controler rapidement avant
      panne secondaire.
  - question: Puis-je monter Câble d'accélérateur sans verification atelier ?
    answer: Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure
      constructeur.
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
doc_id: f11935af-cfbe-5036-954a-f8ac5eaf673e
content_hash: sha256:5cc918f39dbe6cca
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

# Câble d'accélérateur - Guide Diagnostic Complet

## Fonction et Rôle

Transmet la commande d'accélération de la pédale au papillon

**Actions principales:** transmettre, actionner, commander

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- pedale d accelerateur dure ou rigide
- reponse moteur retardee a l acceleration
- point dur lors de l enfoncement de la pedale

## Procédure de Diagnostic

Pour diagnostiquer un problème de câble d'accélérateur:

1. **Inspection visuelle** - Examiner l'état du câble d'accélérateur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- pedale
- papillon

## Critères de Compatibilité

Pour commander le bon câble d'accélérateur, vous devez connaître:

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

**Comment choisir Câble d'accélérateur compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Câble d'accélérateur ?**
En cas de pedale d accelerateur dure ou rigide ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Câble d'accélérateur sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
