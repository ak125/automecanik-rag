---
category: distribution
slug: galet-enrouleur-de-courroie-d-accessoire
title: Galet enrouleur de courroie d'accessoire
pg_id: 312
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
  role: Guide la courroie d'accessoire
  must_be_true:
  - guider
  - enrouler
  - maintenir
  must_not_contain:
  - freinage
  - climatisation
  - turbo
  - injection
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - courroie-de-distribution
  - kit-de-distribution
  - galet-tendeur-de-courroie-de-distribution
  - galet-enrouleur-de-courroie-de-distribution
  - pompe-a-eau
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
  - ❌ "plus de durée de vie"
  cost_range:
    min: 15
    max: 45
    currency: EUR
    unit: galet
    source: catalogue automecanik
  quality_tiers:
  - tier: Qualité Origine (OE)
    description: Galets enrouleurs fournis en première monte par les équipementiers des constructeurs. Roulement à billes
      haute précision, surface de contact lisse et traitée.
  - tier: Équivalent Qualité Origine
    description: Galets de qualité comparable à l'OE, fabriqués selon les mêmes normes dimensionnelles. Roulement de précision
      et revêtement de guidage conformes.
  - tier: Adaptable Économique
    description: Galets enrouleurs aux dimensions compatibles pour un usage standard. Vérifier le diamètre intérieur, extérieur
      et la largeur avant commande.
  brands:
    premium:
    - Gates
    - Continental/Contitech
    standard:
    - Dayco
    - SKF
    - INA
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Courroie d accessoire visiblement usee ou fissuree
    severity: confort
  - id: S2
    label: Sifflement ou grondement au niveau de la courroie
    severity: confort
  - id: S3
    label: Perceptible faisant tourner galet main
    severity: confort
  - id: S4
    label: Perte de tension de la courroie
    severity: confort
  - id: S5
    label: Odeur de caoutchouc chaud
    severity: confort
  - id: S6
    label: Plus de 80 000 km depuis le dernier changement
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - remplacement preventif recommande
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'kilometrage eleve ou usure visible : remplacement preventif recommande'
  quick_checks:
  - 'Observer : courroie d accessoire visiblement usee ou fissuree ?'
  - 'Observer : sifflement ou grondement au niveau de la courroie ?'
  - 'Observer : perceptible faisant tourner galet main ?'
  - 'Observer : perte de tension de la courroie ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Courroie d accessoire visiblement usee ou fissuree
  - Sifflement ou grondement au niveau de la courroie
  - Perceptible faisant tourner galet main
  - Perte de tension de la courroie
  - Odeur de caoutchouc chaud
  - Plus de 80 000 km depuis le dernier changement
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '312'
  intro_title: A quoi sert Galet enrouleur de courroie d'accessoire ?
  risk_title: Pourquoi remplacer Galet enrouleur de courroie d'accessoire a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
  - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
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
  - question: Galet enrouleur OE ou adaptable ?
    answer: Les galets OES (SKF, INA, Gates) sont fiables. Vérifiez le diamètre et le type de roulement.
  - question: Comment savoir si mon galet enrouleur est HS ?
    answer: Sifflement ou grondement au niveau de la courroie, jeu perceptible à la main, roulement rugueux.
  - question: Tous les combien changer le galet enrouleur ?
    answer: À chaque changement de courroie d'accessoire (60 000 à 100 000 km). Ne jamais réutiliser un ancien galet.
  - question: Peut-on changer le galet enrouleur soi-même ?
    answer: Oui, opération accessible. Détendre la courroie, dévisser le galet, monter le neuf. 30 min à 1h.
  - question: Quelle erreur éviter avec le galet enrouleur ?
    answer: Ne pas oublier de vérifier le tendeur aussi. Respecter le cheminement de la courroie. Vérifier l'alignement.
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
doc_id: 316d28e0-3d97-57fa-b485-f8861c4f40fb
content_hash: sha256:6f4ca5630fe6c6ef
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
  area: Face laterale du moteur, derriere le carter de distribution
  access: Depose courroie accessoire + carter distribution
  adjacent_parts:
  - courroie
  - galets
  - pompe a eau
  - poulie
installation:
  difficulty: difficile (pro recommande)
  time: 3h a 6h
  tools:
  - kit calage distribution
  - cle dynamometrique
  - extracteur poulie
  prerequisite: Moteur cale au PMH, ne pas tourner le moteur sans courroie
---

# Galet enrouleur de courroie d'accessoire - Guide Diagnostic Complet

## Fonction et Rôle

Guide la courroie d'accessoire

**Actions principales:** guider, enrouler, maintenir

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- courroie d accessoire visiblement usee ou fissuree
- sifflement ou grondement au niveau de la courroie
- perceptible faisant tourner galet main
- perte de tension de la courroie
- odeur de caoutchouc chaud
- plus de 80 000 km depuis le dernier changement

## Procédure de Diagnostic

Pour diagnostiquer un problème de galet enrouleur de courroie d'accessoire:

1. **Inspection visuelle** - Examiner l'état du galet enrouleur de courroie d'accessoire
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- compresseur-de-climatisation
- courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- pompe-a-eau
- pompe-de-direction-assistee

## Critères de Compatibilité

Pour commander le bon galet enrouleur de courroie d'accessoire, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de durée de vie"

## FAQ

**Galet enrouleur OE ou adaptable ?**
Les galets OES (SKF, INA, Gates) sont fiables. Vérifiez le diamètre et le type de roulement.

**Comment savoir si mon galet enrouleur est HS ?**
Sifflement ou grondement au niveau de la courroie, jeu perceptible à la main, roulement rugueux.

**Tous les combien changer le galet enrouleur ?**
À chaque changement de courroie d'accessoire (60 000 à 100 000 km). Ne jamais réutiliser un ancien galet.

**Peut-on changer le galet enrouleur soi-même ?**
Oui, opération accessible. Détendre la courroie, dévisser le galet, monter le neuf. 30 min à 1h.

**Quelle erreur éviter avec le galet enrouleur ?**
Ne pas oublier de vérifier le tendeur aussi. Respecter le cheminement de la courroie. Vérifier l'alignement.
