---
category: electrique
slug: neiman
title: Neiman
pg_id: 1367
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
  role: Verrouiller la direction et alimenter les circuits electriques
  must_be_true:
  - verrouiller
  - alimenter
  - securiser
  must_not_contain:
  - injection
  - climatisation
  - freinage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - alternateur
  - batterie
  - demarreur
  - bougie-d-allumage
  - bobine-d-allumage
  - poulie-d-alternateur
  confusion_with:
  - term: piece-electrique-voisine
    difference: Les pieces electriques ont des connecteurs specifiques. Verifier le nombre de broches et le voltage.
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
  - ❌ "demarrage garanti"
  cost_range:
    min: 80
    max: 250
    currency: EUR
    unit: neuf
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    price_range: Prix élevé — évite les frais de reprogrammation antidémarrage
  - tier: Équivalent OE (OES)
    price_range: Prix intermédiaire — vérifier les exigences de reprogrammation
  - tier: Aftermarket standard
    price_range: Prix bas — risque de reprogrammation à prévoir sur certains véhicules
  brands:
    premium:
    - Bosch
    - Valeo
    - Denso
    standard:
    - Hella
    - NGK
    - Delphi
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Tableau de bord qui ne s allume pas au contact
    severity: confort
  - id: S2
    label: Cle qui tourne dans le vide sans effet
    severity: confort
  - id: S3
    label: Direction bloquee impossible a debloquer
    severity: immobilisation
  - id: S4
    label: Contact electrique intermittent coupures
    severity: confort
  - id: S5
    label: Odeur de plastique brule court-circuit interne
    severity: confort
  - id: S6
    label: Difficulte recurrente a tourner la cle
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - 'vehicule immobilise ou symptome critique : verification urgente piece et alimentation'
  - 'Usure ou defaillance causant : tableau de bord qui ne s allume pas au contact'
  quick_checks:
  - 'Observer : tableau de bord qui ne s allume pas au contact ?'
  - 'Observer : cle qui tourne dans le vide sans effet ?'
  - 'Observer : direction bloquee impossible a debloquer ?'
  - 'Observer : contact electrique intermittent coupures ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Tableau de bord qui ne s allume pas au contact
  - Cle qui tourne dans le vide sans effet
  - Direction bloquee impossible a debloquer
  - Contact electrique intermittent coupures
  - Odeur de plastique brule court-circuit interne
  - Difficulte recurrente a tourner la cle
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '1367'
  intro_title: A quoi sert Neiman ?
  risk_title: Pourquoi remplacer Neiman a temps ?
  risk_explanation: '**Pièce HS** - Le neiman peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le neiman peut être hors service et nécessiter un remplacement'
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
  - question: Neiman OE ou adaptable ?
    answer: Privilégiez l'OE ou OES (Valeo, Hella) pour garantir la compatibilité avec l'immobiliseur. Les adaptables peuvent
      nécessiter une reprogrammation coûteuse.
  - question: Comment savoir si mon neiman est HS ?
    answer: Clé qui tourne dans le vide, direction bloquée en permanence, tableau de bord qui ne s'allume pas, contact intermittent,
      impossibilité de démarrer.
  - question: Quand faut-il changer le neiman ?
    answer: Pas de périodicité. À remplacer si usé mécaniquement (clé qui force), si les contacts sont oxydés, ou si la direction
      reste bloquée.
  - question: Peut-on changer le neiman soi-même ?
    answer: Difficile. Nécessite de démonter le carénage de colonne et souvent des vis de sécurité. Risque de bloquer l'antidémarrage.
      Prévoir reprogrammation.
  - question: Quelle erreur éviter avec le neiman ?
    answer: Ne pas forcer sur la clé (risque de casser). Vérifier la compatibilité immobiliseur avant achat. Prévoir le coût
      de reprogrammation si nécessaire.
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
doc_id: 24b47372-a822-5b06-9266-d6204849ac46
content_hash: sha256:5528ddc3f7b11b75
lang: fr
variants:
- name: Piece neuve OE/OES
  aliases:
  - neuf
  - OE
  - OES
  functional_differences:
  - Garantie constructeur ou equipementier
  - Calibration d usine
- name: Piece echange standard
  aliases:
  - echange standard
  - reconditionne
  functional_differences:
  - Moins cher
  - Piece d origine reconditionnee
location_on_vehicle:
  area: Compartiment moteur (alternateur, demarreur) ou peripherie
  access: Par le dessus (capot) ou par le dessous selon modele
  adjacent_parts:
  - faisceau electrique
  - batterie
  - fusibles
installation:
  difficulty: facile a moyen
  time: 15min a 1h
  tools:
  - cle a douille
  - multimetre
  - tournevis
  prerequisite: Debrancher la batterie avant intervention
---

# Neiman - Guide Diagnostic Complet

## Fonction et Rôle

Verrouiller la direction et alimenter les circuits electriques

**Actions principales:** verrouiller, alimenter, securiser

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Direction bloquee impossible a debloquer**
  direction bloquee impossible a debloquer

### 🟢 Autres Symptômes

- tableau de bord qui ne s allume pas au contact
- cle qui tourne dans le vide sans effet
- contact electrique intermittent coupures
- odeur de plastique brule court-circuit interne
- difficulte recurrente a tourner la cle

## Procédure de Diagnostic

Pour diagnostiquer un problème de neiman:

1. **Inspection visuelle** - Examiner l'état du neiman
2. **Test électrique** - Vérifier la tension et les connexions
3. **Lecture codes défaut** - Scanner OBD si voyant allumé


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le neiman peut être hors service et nécessiter un remplacement
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- colonne-de-direction
- demarreur

## Critères de Compatibilité

Pour commander le bon neiman, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "demarrage garanti"

## FAQ

**Neiman OE ou adaptable ?**
Privilégiez l'OE ou OES (Valeo, Hella) pour garantir la compatibilité avec l'immobiliseur. Les adaptables peuvent nécessiter une reprogrammation coûteuse.

**Comment savoir si mon neiman est HS ?**
Clé qui tourne dans le vide, direction bloquée en permanence, tableau de bord qui ne s'allume pas, contact intermittent, impossibilité de démarrer.

**Quand faut-il changer le neiman ?**
Pas de périodicité. À remplacer si usé mécaniquement (clé qui force), si les contacts sont oxydés, ou si la direction reste bloquée.

**Peut-on changer le neiman soi-même ?**
Difficile. Nécessite de démonter le carénage de colonne et souvent des vis de sécurité. Risque de bloquer l'antidémarrage. Prévoir reprogrammation.

**Quelle erreur éviter avec le neiman ?**
Ne pas forcer sur la clé (risque de casser). Vérifier la compatibilité immobiliseur avant achat. Prévoir le coût de reprogrammation si nécessaire.
