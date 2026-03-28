---
category: eclairage
slug: correcteur-de-portee
title: Correcteur de portée
pg_id: 700
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
  role: Règle la hauteur du faisceau lumineux en fonction de la charge du véhicule
  must_be_true:
  - regler
  - ajuster
  - adapter
  must_not_contain:
  - ampoule
  - feu
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - ampoule-feu-avant
  - ampoule-feu-arriere
  - feu-avant
  - feu-arriere
  - phares-antibrouillard
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de compatibilite
    pour confirmer Correcteur de portée.
  - Verifier le type d ampoule (H1, H4, H7, LED, xenon) compatible avec le vehicule
  - Respecter la puissance et le culot exact de l ampoule d origine
  - Choisir des ampoules homologuees pour la circulation routiere
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "visibilite parfaite"
  cost_range:
    min: 30
    max: 200
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Equipement d origine (OE)
  - tier: Equivalent OE
  - tier: Piece adaptable
  brands:
    premium:
    - Osram
    - Philips
    standard:
    - Bosch
    - Hella
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Phares mal orientés
    severity: confort
  - id: S2
    label: Eblouissement
    severity: confort
  - id: S3
    label: Reglage impossible
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'Usure ou defaillance causant : phares mal orientés'
  - 'Usure ou defaillance causant : eblouissement'
  quick_checks:
  - 'Observer : phares mal orientés ?'
  - 'Observer : eblouissement ?'
  - 'Observer : reglage impossible ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Phares mal orientés
  - Eblouissement
  - Reglage impossible
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '700'
  intro_title: A quoi sert Correcteur de portée ?
  risk_title: Pourquoi remplacer Correcteur de portée a temps ?
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
  - question: Comment choisir Correcteur de portée compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Correcteur de portée ?
    answer: En cas de phares mal orientés ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Correcteur de portée sans verification atelier ?
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
doc_id: 463dda70-8518-50ff-bbcd-6302e7184af2
content_hash: sha256:6b8347359fe4e7bc
lang: fr
variants:
- name: Ampoule halogene
  aliases:
  - halogene
  - H1
  - H4
  - H7
  functional_differences:
  - Standard, economique
  - Remplacement simple
- name: Ampoule LED
  aliases:
  - LED
  functional_differences:
  - Duree de vie superieure
  - Consommation reduite
  - Verifier homologation
location_on_vehicle:
  area: Face avant, arriere et laterale du vehicule
  access: Par le compartiment moteur (avant) ou coffre (arriere)
  adjacent_parts:
  - optique
  - ampoule
  - connecteur
  - reflecteur
installation:
  difficulty: facile
  time: 5 a 15 min
  tools:
  - tournevis
  - gants (ne pas toucher ampoule halogene)
  prerequisite: Moteur eteint, acces par compartiment moteur ou coffre
---

# Correcteur de portée - Guide Diagnostic Complet

## Fonction et Rôle

Règle la hauteur du faisceau lumineux en fonction de la charge du véhicule

**Actions principales:** regler, ajuster, adapter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- phares mal orientés
- eblouissement
- reglage impossible

## Procédure de Diagnostic

Pour diagnostiquer un problème de correcteur de portée:

1. **Inspection visuelle** - Examiner l'état du correcteur de portée
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

- feu-avant
- commande-correcteur-de-portee

## Critères de Compatibilité

Pour commander le bon correcteur de portée, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "visibilite parfaite"

## FAQ

**Comment choisir Correcteur de portée compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Correcteur de portée ?**
En cas de phares mal orientés ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Correcteur de portée sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
