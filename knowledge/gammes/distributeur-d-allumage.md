---
category: allumage
slug: distributeur-d-allumage
title: Distributeur d'allumage
pg_id: 683
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
  role: Distribuer la haute tension aux bougies dans l'ordre d'allumage
  must_be_true:
  - distribuer
  - repartir
  - transmettre
  must_not_contain:
  - freinage
  - climatisation
  - embrayage
  - direction
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - distribuer
  - repartir
  - transmettre
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
  - ❌ "demarrage instantane"
  cost_range:
    min: 100
    max: 400
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Pièce d'origine (OE / neuf)
    description: Distributeur neuf conforme à la spécification constructeur d'origine. Disponibilité variable selon l'âge
      du véhicule. Recommandé pour les restaurations soignées.
  - tier: Équipementier reconnu (allumage)
    description: Produit de fabricants spécialisés en systèmes d'allumage. Compatible avec les kits de distribution (vis platinées,
      condensateur, rotor, chapeau).
  - tier: Pièce adaptable / reconditionné
    description: Option sur véhicules anciens où la pièce neuve n'est plus disponible. Vérifier l'ordre d'allumage, le type
      de déclencheur (platines ou capteur Hall) et les dimensions de l'arbre.
  - tier: Distributeur reconditionné
    description: Reconditionné d'occasion avec remplacement des pièces d'usure internes. Peut convenir pour certains modèles
      dont les pièces neuves ne sont plus disponibles.
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
    label: Rates d allumage
    severity: confort
  - id: S2
    label: Demarrage difficile
    severity: confort
  - id: S3
    label: Manque de puissance
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : rates d allumage'
  quick_checks:
  - 'Observer : rates d allumage ?'
  - 'Observer : demarrage difficile ?'
  - 'Observer : manque de puissance ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Rates d allumage
  - Demarrage difficile
  - Manque de puissance
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '683'
  intro_title: A quoi sert Distributeur d'allumage ?
  risk_title: Pourquoi remplacer Distributeur d'allumage a temps ?
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
  - question: Comment choisir Distributeur d'allumage compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Distributeur d'allumage ?
    answer: En cas de rates d allumage ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Distributeur d'allumage sans verification atelier ?
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
doc_id: ca4bb638-03c0-547f-86b5-c155ff80a94f
content_hash: sha256:d5b9075febe289c7
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

# Distributeur d'allumage - Guide Diagnostic Complet

## Fonction et Rôle

Distribuer la haute tension aux bougies dans l'ordre d'allumage

**Actions principales:** distribuer, repartir, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- rates d allumage
- demarrage difficile
- manque de puissance

## Procédure de Diagnostic

Pour diagnostiquer un problème de distributeur d'allumage:

1. **Inspection visuelle** - Examiner l'état du distributeur d'allumage
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

- bobine-d-allumage
- faisceau-d-allumage
- bougie-d-allumage

## Critères de Compatibilité

Pour commander le bon distributeur d'allumage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "demarrage instantane"

## FAQ

**Comment choisir Distributeur d'allumage compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Distributeur d'allumage ?**
En cas de rates d allumage ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Distributeur d'allumage sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
