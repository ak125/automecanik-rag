---
category: distribution
slug: galet-tendeur-de-courroie-d-accessoire
title: Galet tendeur de courroie d'accessoire
pg_id: 310
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
  role: Maintient la tension de la courroie d'accessoire
  must_be_true:
  - tendre
  - maintenir
  - guider
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
    max: 84
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
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
    label: Sifflement de la courroie
    severity: confort
  - id: S2
    label: Bruit de roulement cote accessoires
    severity: confort
  - id: S3
    label: Courroie qui patine temoin batterie
    severity: confort
  - id: S4
    label: Galet qui ne bouge plus tendeur bloque
    severity: immobilisation
  - id: S5
    label: Vibrations dans le moteur
    severity: confort
  - id: S6
    label: Bruit de claquement courroie detendue
    severity: confort
  - id: S7
    label: Courroie qui saute de son logement
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - verifier equilibrage et fixations
  quick_checks:
  - 'Observer : sifflement de la courroie ?'
  - Bruit de roulement cote accessoires ?
  - 'Observer : courroie qui patine temoin batterie ?'
  - 'Observer : galet qui ne bouge plus tendeur bloque ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Sifflement de la courroie
  - Bruit de roulement cote accessoires
  - Courroie qui patine temoin batterie
  - Galet qui ne bouge plus tendeur bloque
  - Vibrations dans le moteur
  - Bruit de claquement courroie detendue
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '310'
  intro_title: A quoi sert Galet tendeur de courroie d'accessoire ?
  risk_title: Pourquoi remplacer Galet tendeur de courroie d'accessoire a temps ?
  risk_explanation: '**Pièce HS** - Le galet tendeur de courroie d''accessoire peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le galet tendeur de courroie d''accessoire peut être hors service et nécessiter un remplacement'
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
  - question: Comment savoir si le tendeur est HS ?
    answer: Vérifiez s'il bouge librement (ressort interne). Un tendeur bloqué ne compense plus l'usure de la courroie. Bruit
      de roulement = roulement HS.
  - question: Peut-on changer le galet sans la courroie ?
    answer: Oui si la courroie est récente. Mais généralement, on change les deux ensemble car l'accès est le même.
  - question: Tendeur manuel ou automatique ?
    answer: La plupart des véhicules modernes ont un tendeur automatique à ressort. Les anciens ont un tendeur manuel à régler.
  - question: Quelles sont les erreurs fréquentes à éviter ?
    answer: Forcer sur un tendeur automatique. Mal positionner le tendeur au remontage. Ignorer le bruit de roulement.
  - question: Comment faire un diagnostic rapide ?
    answer: Tendeur qui ne bouge pas → ressort cassé ou galet grippé. Bruit de roulement → galet à changer. Courroie détendue
      → vérifier tendeur en premier.
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
doc_id: df592e24-cc02-5e3c-9198-a7b9601c2485
content_hash: sha256:7324a68d44a7080c
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

# Galet tendeur de courroie d'accessoire - Guide Diagnostic Complet

## Fonction et Rôle

Maintient la tension de la courroie d'accessoire

**Actions principales:** tendre, maintenir, guider

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Galet qui ne bouge plus tendeur bloque**
  galet qui ne bouge plus tendeur bloque

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de claquement courroie detendue**
  bruit de claquement courroie detendue

### 🟢 Autres Symptômes

- sifflement de la courroie
- bruit de roulement cote accessoires
- courroie qui patine temoin batterie
- vibrations dans le moteur
- courroie qui saute de son logement

## Procédure de Diagnostic

Pour diagnostiquer un problème de galet tendeur de courroie d'accessoire:

1. **Inspection visuelle** - Examiner l'état du galet tendeur de courroie d'accessoire
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le galet tendeur de courroie d'accessoire peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- compresseur-de-climatisation
- courroie-d-accessoire
- galet-enrouleur-de-courroie-d-accessoire
- pompe-de-direction-assistee
- poulie-d-alternateur
- poulie-vilebrequin

## Critères de Compatibilité

Pour commander le bon galet tendeur de courroie d'accessoire, vous devez connaître:

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

**Comment savoir si le tendeur est HS ?**
Vérifiez s'il bouge librement (ressort interne). Un tendeur bloqué ne compense plus l'usure de la courroie. Bruit de roulement = roulement HS.

**Peut-on changer le galet sans la courroie ?**
Oui si la courroie est récente. Mais généralement, on change les deux ensemble car l'accès est le même.

**Tendeur manuel ou automatique ?**
La plupart des véhicules modernes ont un tendeur automatique à ressort. Les anciens ont un tendeur manuel à régler.

**Quelles sont les erreurs fréquentes à éviter ?**
Forcer sur un tendeur automatique. Mal positionner le tendeur au remontage. Ignorer le bruit de roulement.

**Comment faire un diagnostic rapide ?**
Tendeur qui ne bouge pas → ressort cassé ou galet grippé. Bruit de roulement → galet à changer. Courroie détendue → vérifier tendeur en premier.
