---
category: eclairage
slug: ampoule-feu-eclaireur-de-plaque
title: Ampoule feu éclaireur de plaque
pg_id: 112
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
  role: Produit la lumière pour éclairer la plaque d'immatriculation
  must_be_true:
  - produire
  - emettre
  - eclairer
  must_not_contain:
  - feu complet
  - optique
  - relais
  - commande
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
  - 'Type d''ampoule : Navette C5W ou capsule W5W selon véhicule'
  - 'Longueur navette : 36 mm, 39 mm ou 41 mm — mesurer l''existante'
  - 'Puissance : 5W standard (10W interdit — surchauffe du support)'
  - 'Culot : SV8.5-8 (navette) ou W2.1x9.5d (capsule)'
  - 'Technologie : Halogène classique ou LED blanc homologué ECE R7'
  - 'Quantité : Généralement 2 ampoules par véhicule — remplacer par paire'
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
  - tier: Piece d'origine (OE)
    description: Ampoule reference constructeur. Utile si le vehicule est recent et sous garantie. Pour ce type de piece,
      la reference standard suffit dans la majorite des cas.
  - tier: Equipementier reconnu - ampoule standard
    description: Ampoule navette repondant aux specifications du vehicule. Les equipementiers d'eclairage reconnus proposent
      des produits homologues CE et adaptes aux normes en vigueur.
  - tier: Equivalent LED homologue
    description: Certains vehicules acceptent une ampoule LED en remplacement de la navette halogene. Verifier la compatibilite
      avec le vehicule et s'assurer que la LED est homologuee route (marquage E).
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
    label: Plaque d immatriculation non eclairee
    severity: confort
  - id: S2
    label: Eclairage faible ou clignotant
    severity: confort
  - id: S3
    label: Refus au controle technique
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'Usure ou defaillance causant : plaque d immatriculation non eclairee'
  - 'Usure ou defaillance causant : eclairage faible ou clignotant'
  quick_checks:
  - 'Observer : plaque d immatriculation non eclairee ?'
  - 'Observer : eclairage faible ou clignotant ?'
  - 'Observer : refus au controle technique ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Plaque d immatriculation non eclairee
  - Eclairage faible ou clignotant
  - Refus au controle technique
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '112'
  intro_title: A quoi sert Ampoule feu éclaireur de plaque ?
  risk_title: Pourquoi remplacer Ampoule feu éclaireur de plaque a temps ?
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
  - question: Comment choisir Ampoule feu éclaireur de plaque compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Ampoule feu éclaireur de plaque ?
    answer: En cas de plaque d immatriculation non eclairee ou de degradation mesurable, il faut controler rapidement avant
      panne secondaire.
  - question: Puis-je monter Ampoule feu éclaireur de plaque sans verification atelier ?
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
doc_id: 3030447c-cf13-5a2d-b84c-f8d29a6ab7fe
content_hash: sha256:59553f93cb8e703f
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

# Ampoule feu éclaireur de plaque - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière pour éclairer la plaque d'immatriculation

**Actions principales:** produire, emettre, eclairer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- plaque d immatriculation non eclairee
- eclairage faible ou clignotant
- refus au controle technique

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule feu éclaireur de plaque:

1. **Inspection visuelle** - Examiner l'état du ampoule feu éclaireur de plaque
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

- feu-arriere
- ampoule-feu-arriere

## Critères de Compatibilité

Pour commander le bon ampoule feu éclaireur de plaque, vous devez connaître:

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

**Comment choisir Ampoule feu éclaireur de plaque compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Ampoule feu éclaireur de plaque ?**
En cas de plaque d immatriculation non eclairee ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Ampoule feu éclaireur de plaque sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
