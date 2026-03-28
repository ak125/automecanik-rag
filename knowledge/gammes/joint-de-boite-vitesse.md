---
category: moteur
slug: joint-de-boite-vitesse
title: Joint de boîte vitesse
pg_id: 146
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
  role: Assurer l'etancheite de la boite de vitesses contre les fuites d'huile
  must_be_true:
  - assurer l'etancheite
  - proteger
  must_not_contain:
  - freinage
  - climatisation
  - direction
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - cardan
  - soufflet-de-cardan
  - roulement-de-roue
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de moteur pour
    confirmer Joint de boîte vitesse.
  - Verifier la reference OE ou equivalence constructeur pour le vehicule exact
  - Comparer les dimensions et le type de montage avec la piece d origine
  - Choisir un equipementier reconnu pour garantir qualite et compatibilite
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "repare le moteur"
  cost_range:
    min: 1000
    max: 5000
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Equipement d'origine (OE)
    description: Joint agréé par le constructeur de la boîte. Dimensions et matériau identiques à la première monte.
  - tier: Equivalent OE (OES)
    description: Fabricants spécialisés en étanchéité automobile, approvisionnant les équipementiers de première monte.
  - tier: Adaptable multi-référence
    description: Joints compatibles plusieurs types de boîtes. Nécessite vérification des cotes extérieures, intérieures et
      de la lèvre d'étanchéité.
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
    label: Fuite d huile au niveau de la boite
    severity: confort
  - id: S2
    label: Traces d huile sur le sol de garage
    severity: confort
  - id: S3
    label: Niveau d huile de boite insuffisant
    severity: confort
  causes:
  - identifier origine fuite et verifier joints
  - 'Usure ou defaillance causant : fuite d huile au niveau de la boite'
  - 'Usure ou defaillance causant : traces d huile sur le sol de garage'
  quick_checks:
  - Fuite d huile au niveau de la boite ?
  - 'Observer : traces d huile sur le sol de garage ?'
  - 'Observer : niveau d huile de boite insuffisant ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Fuite d huile au niveau de la boite
  - Traces d huile sur le sol de garage
  - Niveau d huile de boite insuffisant
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '146'
  intro_title: A quoi sert Joint de boîte vitesse ?
  risk_title: Pourquoi remplacer Joint de boîte vitesse a temps ?
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
  - question: Comment choisir Joint de boîte vitesse compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Joint de boîte vitesse ?
    answer: En cas de fuite d huile au niveau de la boite ou de degradation mesurable, il faut controler rapidement avant
      panne secondaire.
  - question: Puis-je monter Joint de boîte vitesse sans verification atelier ?
    answer: Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure
      constructeur.
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
doc_id: 175a0fc0-05d2-5b43-807f-f5fe0798b438
content_hash: sha256:b0b390fd92706d05
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

# Joint de boîte vitesse - Guide Diagnostic Complet

## Fonction et Rôle

Assurer l'etancheite de la boite de vitesses contre les fuites d'huile

**Actions principales:** assurer l'etancheite, proteger

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- fuite d huile au niveau de la boite
- traces d huile sur le sol de garage
- niveau d huile de boite insuffisant

## Procédure de Diagnostic

Pour diagnostiquer un problème de joint de boîte vitesse:

1. **Inspection visuelle** - Examiner l'état du joint de boîte vitesse
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- boite-de-vitesses
- joint-d-etancheite

## Critères de Compatibilité

Pour commander le bon joint de boîte vitesse, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"

## FAQ

**Comment choisir Joint de boîte vitesse compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Joint de boîte vitesse ?**
En cas de fuite d huile au niveau de la boite ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Joint de boîte vitesse sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
