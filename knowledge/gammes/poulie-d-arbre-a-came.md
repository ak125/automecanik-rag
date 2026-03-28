---
category: distribution
slug: poulie-d-arbre-a-came
title: Poulie d'arbre à came
pg_id: 1067
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
  role: Entrainer l'arbre a cames en synchronisation avec le vilebrequin
  must_be_true:
  - entrainer
  - synchroniser
  - transmettre
  must_not_contain:
  - vilebrequin
  - accessoire
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
  - ❌ "repare le moteur"
  cost_range:
    min: 40
    max: 150
    currency: EUR
    unit: poulie
    source: catalogue automecanik
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE — equipementiers distribution
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
    label: Bruit de claquement au niveau de la culasse
    severity: confort
  - id: S2
    label: Perte de puissance progressive
    severity: confort
  - id: S3
    label: Moteur qui cale au ralenti
    severity: immobilisation
  - id: S4
    label: Fumee anormale a l echappement
    severity: confort
  - id: S5
    label: Voyant moteur allume codes calage
    severity: immobilisation
  - id: S6
    label: Distribution a remplacer selon carnet d entretien
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  quick_checks:
  - Bruit de claquement au niveau de la culasse ?
  - 'Observer : perte de puissance progressive ?'
  - 'Observer : moteur qui cale au ralenti ?'
  - 'Observer : fumee anormale a l echappement ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Bruit de claquement au niveau de la culasse
  - Perte de puissance progressive
  - Moteur qui cale au ralenti
  - Fumee anormale a l echappement
  - Voyant moteur allume codes calage
  - Distribution a remplacer selon carnet d entretien
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '1067'
  intro_title: A quoi sert Poulie d'arbre à came ?
  risk_title: Pourquoi remplacer Poulie d'arbre à came a temps ?
  risk_explanation: '**Pièce HS** - Le poulie d''arbre à came peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le poulie d''arbre à came peut être hors service et nécessiter un remplacement'
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
  - question: Poulie d'arbre à came OE ou adaptable ?
    answer: Privilégiez l'OE ou le kit distribution complet. C'est une pièce critique pour le calage moteur.
  - question: Comment savoir si ma poulie d'arbre à came est HS ?
    answer: Bruit de claquement moteur, calage distribution décalé, perte de puissance, moteur qui cale.
  - question: Tous les combien changer la poulie d'arbre à came ?
    answer: À chaque remplacement du kit de distribution (80 000 à 120 000 km selon véhicule). Jamais seule.
  - question: Peut-on changer la poulie d'arbre à came soi-même ?
    answer: Déconseillé sans expérience. Nécessite de caler la distribution. Erreur = destruction moteur.
  - question: Quelle erreur éviter avec la poulie d'arbre à came ?
    answer: Ne jamais réutiliser une poulie usée. Respecter les repères de calage. Serrer au couple exact.
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
doc_id: 3d6efecb-2f0a-58ca-9791-bbdbd6561d53
content_hash: sha256:9d6cc5f8a6607b99
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

# Poulie d'arbre à came - Guide Diagnostic Complet

## Fonction et Rôle

Entrainer l'arbre a cames en synchronisation avec le vilebrequin

**Actions principales:** entrainer, synchroniser, transmettre

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Moteur qui cale au ralenti**
  moteur qui cale au ralenti
- **Voyant moteur allume codes calage**
  voyant moteur allume codes calage

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de claquement au niveau de la culasse**
  bruit de claquement au niveau de la culasse

### 🟢 Autres Symptômes

- perte de puissance progressive
- fumee anormale a l echappement
- distribution a remplacer selon carnet d entretien

## Procédure de Diagnostic

Pour diagnostiquer un problème de poulie d'arbre à came:

1. **Inspection visuelle** - Examiner l'état du poulie d'arbre à came
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le poulie d'arbre à came peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- arbre-a-came
- capteur-impulsion
- chaine-de-distribution
- courroie-de-distribution
- kit-de-chaine-de-distribution
- kit-de-distribution

## Critères de Compatibilité

Pour commander le bon poulie d'arbre à came, vous devez connaître:

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

**Poulie d'arbre à came OE ou adaptable ?**
Privilégiez l'OE ou le kit distribution complet. C'est une pièce critique pour le calage moteur.

**Comment savoir si ma poulie d'arbre à came est HS ?**
Bruit de claquement moteur, calage distribution décalé, perte de puissance, moteur qui cale.

**Tous les combien changer la poulie d'arbre à came ?**
À chaque remplacement du kit de distribution (80 000 à 120 000 km selon véhicule). Jamais seule.

**Peut-on changer la poulie d'arbre à came soi-même ?**
Déconseillé sans expérience. Nécessite de caler la distribution. Erreur = destruction moteur.

**Quelle erreur éviter avec la poulie d'arbre à came ?**
Ne jamais réutiliser une poulie usée. Respecter les repères de calage. Serrer au couple exact.
