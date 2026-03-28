---
category: accessoires
slug: verin-de-coffre
title: Vérin de coffre
pg_id: 5032
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
  role: Maintient le coffre ou hayon en position ouverte
  must_be_true:
  - maintenir
  - supporter
  - soulever
  must_not_contain:
  - serrure
  - verrouillage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - verin-capot-moteur
  - poignee-de-porte
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de compatibilite
    pour confirmer Vérin de coffre.
  - Verifier la reference OE ou equivalence constructeur pour le vehicule exact
  - Comparer les dimensions et le type de montage avec la piece d origine
  - Choisir un equipementier reconnu pour garantir qualite et compatibilite
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "securite garantie"
  cost_range:
    min: 50
    max: 300
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  brands:
    premium:
    - Stabilus
    - Magneti Marelli
    - Valeo
    standard:
    - Lesjöfors
    - Triscan
    - Maxgear
    - Febi Bilstein
    budget:
    - Mapco
    - Metzger
    - Polcar
  quality_tiers:
  - tier: Origine (OE/OES)
    description: Vérins fabriqués par les équipementiers d'origine. Force, longueur et fixations strictement identiques à
      la pièce d'usine.
  - tier: Équivalent OE
    description: Fabricants aftermarket reconnus. Conformes aux spécifications constructeur avec une durée de vie éprouvée.
  - tier: Adaptable
    description: Vérins économiques. Vérifier la force (en Newton), la longueur totale dépliée et le type d'embout/rotule
      avant commande.
diagnostic:
  symptoms:
  - id: S1
    label: Coffre qui retombe lentement
    severity: confort
  - id: S2
    label: Coffre impossible a maintenir ouvert
    severity: confort
  - id: S3
    label: Verin qui fuit traces graisseuses
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'Usure ou defaillance causant : coffre qui retombe lentement'
  - 'Usure ou defaillance causant : coffre impossible a maintenir ouvert'
  quick_checks:
  - 'Observer : coffre qui retombe lentement ?'
  - 'Observer : coffre impossible a maintenir ouvert ?'
  - 'Observer : verin qui fuit traces graisseuses ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Coffre qui retombe lentement
  - Coffre impossible a maintenir ouvert
  - Verin qui fuit traces graisseuses
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '5032'
  intro_title: A quoi sert Vérin de coffre ?
  risk_title: Pourquoi remplacer Vérin de coffre a temps ?
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
  - question: Comment choisir Vérin de coffre compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Vérin de coffre ?
    answer: En cas de coffre qui retombe lentement ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Vérin de coffre sans verification atelier ?
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
doc_id: 381e642b-bcc2-50df-a2ca-9c87f3d6da61
content_hash: sha256:252f385e5a653818
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
  area: Sur la carrosserie (capot, coffre, portes)
  access: Accessible directement sans outil special
  adjacent_parts:
  - charniere
  - serrure
  - cable
  - joint
installation:
  difficulty: facile
  time: 10 a 30 min
  tools:
  - tournevis
  - cle plate
  - clip de fixation
  prerequisite: Aucun prerequis special
---

# Vérin de coffre - Guide Diagnostic Complet

## Fonction et Rôle

Maintient le coffre ou hayon en position ouverte

**Actions principales:** maintenir, supporter, soulever

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- coffre qui retombe lentement
- coffre impossible a maintenir ouvert
- verin qui fuit traces graisseuses

## Procédure de Diagnostic

Pour diagnostiquer un problème de vérin de coffre:

1. **Inspection visuelle** - Examiner l'état du vérin de coffre
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

- hayon
- charniere

## Critères de Compatibilité

Pour commander le bon vérin de coffre, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"

## FAQ

**Comment choisir Vérin de coffre compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Vérin de coffre ?**
En cas de coffre qui retombe lentement ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Vérin de coffre sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
