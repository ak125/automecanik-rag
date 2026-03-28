---
category: distribution
slug: poulie-vilebrequin
title: Poulie vilebrequin
pg_id: 3213
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
  role: Transmet le mouvement du vilebrequin aux accessoires
  must_be_true:
  - entrainer
  - transmettre
  - amortir
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
  - ❌ "plus de puissance"
  cost_range:
    min: 50
    max: 200
    currency: EUR
    unit: poulie
    source: catalogue automecanik
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE
  - tier: Adaptable
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
    label: Vibrations moteur importantes au ralenti
    severity: confort
  - id: S2
    label: Caoutchouc de la poulie fissure ou decolle
    severity: confort
  - id: S3
    label: Courroie d accessoire qui deraille
    severity: confort
  - id: S4
    label: Bruit sourd au niveau du bas moteur
    severity: confort
  - id: S5
    label: Reperes de calage impossibles a aligner
    severity: immobilisation
  - id: S6
    label: Voyant moteur codes vibrations vilebrequin
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - verifier equilibrage et fixations
  quick_checks:
  - Vibrations moteur importantes au ralenti ?
  - 'Observer : caoutchouc de la poulie fissure ou decolle ?'
  - 'Observer : courroie d accessoire qui deraille ?'
  - Bruit sourd au niveau du bas moteur ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Vibrations moteur importantes au ralenti
  - Caoutchouc de la poulie fissure ou decolle
  - Courroie d accessoire qui deraille
  - Bruit sourd au niveau du bas moteur
  - Reperes de calage impossibles a aligner
  - Voyant moteur codes vibrations vilebrequin
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '3213'
  intro_title: A quoi sert Poulie vilebrequin ?
  risk_title: Pourquoi remplacer Poulie vilebrequin a temps ?
  risk_explanation: '**Pièce HS** - Le poulie vilebrequin peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le poulie vilebrequin peut être hors service et nécessiter un remplacement'
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: Poulie vilebrequin OE ou adaptable ?
    answer: Privilégiez l'OE. C'est une pièce critique pour l'équilibrage moteur. Les copies peuvent vibrer.
  - question: Comment savoir si ma poulie vilebrequin est HS ?
    answer: Vibrations importantes moteur, caoutchouc de la poulie fissuré ou décollé, courroie qui saute.
  - question: Tous les combien changer la poulie vilebrequin ?
    answer: Pas de périodicité fixe. À remplacer si fissurée ou si le caoutchouc est détérioré. Souvent 150 000+ km.
  - question: Peut-on changer la poulie vilebrequin soi-même ?
    answer: Difficile. Nécessite de bloquer le volant moteur et un extracteur. Vis centrale très serrée.
  - question: Quelle erreur éviter avec la poulie vilebrequin ?
    answer: Ne pas frapper pour démonter. Utiliser un extracteur adapté. Vérifier le repère de calage. Serrer au couple.
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
doc_id: 32f52546-4115-532e-a9eb-b621edd1a6a9
content_hash: sha256:4f67a48a7475f924
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

# Poulie vilebrequin - Guide Diagnostic Complet

## Fonction et Rôle

Transmet le mouvement du vilebrequin aux accessoires

**Actions principales:** entrainer, transmettre, amortir

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Reperes de calage impossibles a aligner**
  reperes de calage impossibles a aligner

### 🟢 Autres Symptômes

- vibrations moteur importantes au ralenti
- caoutchouc de la poulie fissure ou decolle
- courroie d accessoire qui deraille
- bruit sourd au niveau du bas moteur
- voyant moteur codes vibrations vilebrequin

## Procédure de Diagnostic

Pour diagnostiquer un problème de poulie vilebrequin:

1. **Inspection visuelle** - Examiner l'état du poulie vilebrequin
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le poulie vilebrequin peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- capteur-impulsion
- compresseur-de-climatisation
- courroie-d-accessoire
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- pompe-de-direction-assistee
- poulie-d-alternateur

## Critères de Compatibilité

Pour commander le bon poulie vilebrequin, vous devez connaître:

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

**Poulie vilebrequin OE ou adaptable ?**
Privilégiez l'OE. C'est une pièce critique pour l'équilibrage moteur. Les copies peuvent vibrer.

**Comment savoir si ma poulie vilebrequin est HS ?**
Vibrations importantes moteur, caoutchouc de la poulie fissuré ou décollé, courroie qui saute.

**Tous les combien changer la poulie vilebrequin ?**
Pas de périodicité fixe. À remplacer si fissurée ou si le caoutchouc est détérioré. Souvent 150 000+ km.

**Peut-on changer la poulie vilebrequin soi-même ?**
Difficile. Nécessite de bloquer le volant moteur et un extracteur. Vis centrale très serrée.

**Quelle erreur éviter avec la poulie vilebrequin ?**
Ne pas frapper pour démonter. Utiliser un extracteur adapté. Vérifier le repère de calage. Serrer au couple.
