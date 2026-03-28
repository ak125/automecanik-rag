---
category: alimentation
slug: pompe-d-amorcage
title: Pompe d'amorcage
pg_id: 862
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
  role: Amorcer le circuit carburant lors du demarrage a froid
  must_be_true:
  - amorcer
  - aspirer
  - preparer
  must_not_contain:
  - freinage
  - climatisation
  - distribution
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - amorcer
  - aspirer
  - preparer
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
  - ❌ "repare l'injection"
  cost_range:
    min: 200
    max: 800
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE
  - tier: Adaptable
  brands:
    premium:
    - Bosch
    - Delphi
    - Denso
    standard:
    - Pierburg
    - VDO
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Demarrage difficile apres coupure moteur
    severity: confort
  - id: S2
    label: Poire molle sans resistance
    severity: confort
  - id: S3
    label: Bulles d air dans le circuit
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : demarrage difficile apres coupure moteur'
  quick_checks:
  - 'Observer : demarrage difficile apres coupure moteur ?'
  - 'Observer : poire molle sans resistance ?'
  - 'Observer : bulles d air dans le circuit ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Demarrage difficile apres coupure moteur
  - Poire molle sans resistance
  - Bulles d air dans le circuit
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '862'
  intro_title: A quoi sert Pompe d'amorcage ?
  risk_title: Pourquoi remplacer Pompe d'amorcage a temps ?
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
  - question: Comment choisir Pompe d'amorcage compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Pompe d'amorcage ?
    answer: En cas de demarrage difficile apres coupure moteur ou de degradation mesurable, il faut controler rapidement avant
      panne secondaire.
  - question: Puis-je monter Pompe d'amorcage sans verification atelier ?
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
doc_id: af4accc2-a048-50f2-901a-2de489e1ed13
content_hash: sha256:5eb27dfec1aaac21
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

# Pompe d'amorcage - Guide Diagnostic Complet

## Fonction et Rôle

Amorcer le circuit carburant lors du demarrage a froid

**Actions principales:** amorcer, aspirer, preparer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- demarrage difficile apres coupure moteur
- poire molle sans resistance
- bulles d air dans le circuit

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe d'amorcage:

1. **Inspection visuelle** - Examiner l'état du pompe d'amorcage
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

- accumulateur-de-pression-de-carburant
- regulateur-de-pression-carburant
- soupape-de-rampe-commune-d-injection

## Critères de Compatibilité

Pour commander le bon pompe d'amorcage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare l'injection"

## FAQ

**Comment choisir Pompe d'amorcage compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Pompe d'amorcage ?**
En cas de demarrage difficile apres coupure moteur ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Pompe d'amorcage sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
