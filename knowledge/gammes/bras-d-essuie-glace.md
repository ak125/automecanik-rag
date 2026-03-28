---
category: accessoires
slug: bras-d-essuie-glace
title: Bras d'essuie-glace
pg_id: 301
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
  role: Supporte et maintient le balai contre le pare-brise
  must_be_true:
  - supporter
  - maintenir
  - plaquer
  must_not_contain:
  - caoutchouc
  - lame
  - capteur abs
  - freinage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - supporter
  - maintenir
  - plaquer
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
  - ❌ "visibilite parfaite"
  cost_range:
    min: 50
    max: 300
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
    description: 'Bras identique à l''origine : angle d''attaque, longueur et type d''attache (écrou, clip baïonnette) conformes
      aux plans constructeur.'
  - tier: Qualité équivalente OE
    description: Bras fabriqué par un équipementier spécialisé avec les mêmes côtes fonctionnelles. Souvent livré avec les
      fixations.
  - tier: Adaptable compatible
    description: Bras compatible avec plusieurs références proches. Vérifier la longueur totale, l'offset et le type d'attache
      avant commande.
  brands:
    premium:
    - Bosch
    - Valeo
    standard:
    - SWF
    - Hella
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Balai qui ne touche plus le pare-brise
    severity: confort
  - id: S2
    label: Traces ou zones non balayees
    severity: confort
  - id: S3
    label: Bras tordu ou rouille
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : balai qui ne touche plus le pare-brise'
  quick_checks:
  - 'Observer : balai qui ne touche plus le pare-brise ?'
  - 'Observer : traces ou zones non balayees ?'
  - 'Observer : bras tordu ou rouille ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Balai qui ne touche plus le pare-brise
  - Traces ou zones non balayees
  - Bras tordu ou rouille
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '301'
  intro_title: A quoi sert Bras d'essuie-glace ?
  risk_title: Pourquoi remplacer Bras d'essuie-glace a temps ?
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
  - question: Comment choisir Bras d'essuie-glace compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Bras d'essuie-glace ?
    answer: En cas de balai qui ne touche plus le pare-brise ou de degradation mesurable, il faut controler rapidement avant
      panne secondaire.
  - question: Puis-je monter Bras d'essuie-glace sans verification atelier ?
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
doc_id: d6a4c79f-9803-55db-890f-10dd6dded3e9
content_hash: sha256:d6184bcc3663f27d
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

# Bras d'essuie-glace - Guide Diagnostic Complet

## Fonction et Rôle

Supporte et maintient le balai contre le pare-brise

**Actions principales:** supporter, maintenir, plaquer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- balai qui ne touche plus le pare-brise
- traces ou zones non balayees
- bras tordu ou rouille

## Procédure de Diagnostic

Pour diagnostiquer un problème de bras d'essuie-glace:

1. **Inspection visuelle** - Examiner l'état du bras d'essuie-glace
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

- commande-d-essuie-glace
- moteur-d-essuie-glace
- pompe-nettoyage-des-vitres

## Critères de Compatibilité

Pour commander le bon bras d'essuie-glace, vous devez connaître:

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

**Comment choisir Bras d'essuie-glace compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Bras d'essuie-glace ?**
En cas de balai qui ne touche plus le pare-brise ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Bras d'essuie-glace sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
