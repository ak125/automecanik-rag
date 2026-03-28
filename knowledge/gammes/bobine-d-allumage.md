---
category: allumage
slug: bobine-d-allumage
title: Bobine d'allumage
pg_id: 689
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-25'
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
  role: Transformer la basse tension batterie en haute tension (15-40kV) pour creer l'etincelle aux bougies
  must_be_true:
  - transformer la tension
  - amplifier
  - generer la haute tension
  must_not_contain:
  - diesel
  - prechauffage
  - incandescence
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - alternateur
  - batterie
  - demarreur
  - bougie-d-allumage
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
  - ❌ "plus de puissance"
  cost_range:
    min: 25
    max: 245
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Piece d'origine (OE)
    description: Bobine reference constructeur, generalement produite par un equipementier de rang 1. Recommandee sur vehicules
      recents ou si une garantie constructeur est en jeu.
  - tier: Equipementier rang 1 - electricite/allumage
    description: Fabricants specialises en systemes d'allumage, fournissant les constructeurs en premiere monte. Equivalences
      documentees par reference vehicule et motorisation.
  - tier: Marque intermediaire
    description: Bobines de remplacement conformes aux specifications electriques. Verifier la tension nominale, la resistance
      primaire et secondaire avant achat.
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
    label: Rate moteur localise sur un cylindre precis
    severity: confort
  - id: S2
    label: Voyant moteur allume code p030x
    severity: confort
  - id: S3
    label: Perte de puissance brutale ou progressive
    severity: confort
  - id: S4
    label: Surconsommation de carburant
    severity: confort
  - id: S5
    label: Odeur d essence non brulee a l echappement
    severity: confort
  - id: S6
    label: Demarrage difficile par temps humide
    severity: confort
  causes:
  - lecture codes defaut obd et diagnostic electronique
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  - 'Usure ou defaillance causant : rate moteur localise sur un cylindre precis'
  depose_steps: []
  quick_checks:
  - 'Observer : rate moteur localise sur un cylindre precis ?'
  - Voyant moteur allume code p030x ?
  - 'Observer : perte de puissance brutale ou progressive ?'
  - 'Comparer la consommation : surconsommation de carburant ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Rate moteur localise sur un cylindre precis
  - Voyant moteur allume code p030x
  - Perte de puissance brutale ou progressive
  - Surconsommation de carburant
  - Odeur d essence non brulee a l echappement
  - Demarrage difficile par temps humide
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '689'
  intro_title: A quoi sert Bobine d'allumage ?
  risk_title: Pourquoi remplacer Bobine d'allumage a temps ?
  risk_explanation: '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
  risk_consequences:
  - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
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
  - question: Bobine d'allumage OE ou adaptable ?
    answer: Privilégiez l'OE ou OES (Bosch, Denso, NGK). Les bobines bas de gamme ont une durée de vie réduite et peuvent
      griller rapidement.
  - question: Comment savoir si ma bobine d'allumage est HS ?
    answer: Raté moteur localisé sur un cylindre, voyant moteur + code P030x, perte de puissance, test à l'ohmmètre hors tolérance.
  - question: Tous les combien changer les bobines d'allumage ?
    answer: Pas de périodicité fixe. Durée de vie 100 000 à 200 000 km. À remplacer uniquement en cas de défaut avéré (test
      diagnostic).
  - question: Peut-on changer une bobine d'allumage soi-même ?
    answer: Oui, opération simple sur bobines crayon. Débrancher le connecteur, dévisser la vis de fixation, extraire la bobine.
      10 à 20 minutes.
  - question: Quelle erreur éviter avec les bobines d'allumage ?
    answer: Ne pas changer toutes les bobines par précaution (inutile et coûteux). Vérifier l'état des bougies avant de remplacer
      la bobine.
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
doc_id: bdcb2e3a-53f9-59b8-b5f3-46e27c0c9941
content_hash: sha256:0479945fd18601e8
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

# Bobine d'allumage - Guide Diagnostic Complet

## Fonction et Rôle

Transformer la basse tension batterie en haute tension (15-40kV) pour creer l'etincelle aux bougies

**Actions principales:** transformer la tension, amplifier, generer la haute tension, alimenter les bougies, creer l'arc

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- rate moteur localise sur un cylindre precis
- voyant moteur allume code p030x
- perte de puissance brutale ou progressive
- surconsommation de carburant
- odeur d essence non brulee a l echappement
- demarrage difficile par temps humide

## Procédure de Diagnostic

Pour diagnostiquer un problème de bobine d'allumage:

1. **Inspection visuelle** - Examiner l'état du bobine d'allumage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- bougie-d-allumage
- faisceau-d-allumage

## Critères de Compatibilité

Pour commander le bon bobine d'allumage, vous devez connaître:

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

**Bobine d'allumage OE ou adaptable ?**
Privilégiez l'OE ou OES (Bosch, Denso, NGK). Les bobines bas de gamme ont une durée de vie réduite et peuvent griller rapidement.

**Comment savoir si ma bobine d'allumage est HS ?**
Raté moteur localisé sur un cylindre, voyant moteur + code P030x, perte de puissance, test à l'ohmmètre hors tolérance.

**Tous les combien changer les bobines d'allumage ?**
Pas de périodicité fixe. Durée de vie 100 000 à 200 000 km. À remplacer uniquement en cas de défaut avéré (test diagnostic).

**Peut-on changer une bobine d'allumage soi-même ?**
Oui, opération simple sur bobines crayon. Débrancher le connecteur, dévisser la vis de fixation, extraire la bobine. 10 à 20 minutes.

**Quelle erreur éviter avec les bobines d'allumage ?**
Ne pas changer toutes les bobines par précaution (inutile et coûteux). Vérifier l'état des bougies avant de remplacer la bobine.


## Symptomes supplementaires

<!-- materialized-from-db diagnostic/demarrage-batterie.md 2026-02-15 -->
### Diagnostic - Démarrage et circuit électrique

# Démarrage et circuit électrique - Diagnostic complet

## Le véhicule ne démarre pas

### Rien ne se passe (pas de bruit)
- **Batterie complètement déchargée** : Vérifier la tension aux bornes (< 11.5V = batterie HS ou déchargée). Tester avec un chargeur ou des câbles de démarrage.
- **Bornes de batterie oxydées** : Dépôt blanc-verdâtre sur les cosses. Nettoyer avec une brosse métallique et de la graisse diélectrique.
- **Fusible principal grillé** : Vérifier le fusible de démarreur dans la boîte à fusibles moteur.

### Le démarreur claque sans tourner
- **Solénoïde de démarreur usé** : Le contacteur magnétique fonctionne mais ne peut plus engager le pignon. Remplacement du démarreur nécessaire.
- **Batterie faible** : Assez de courant pour le solénoïde mais pas pour le moteur électrique. Tension entre 11.5V et 12.2V.
- **Mauvaise masse moteur** : Câble de masse entre batterie et bloc moteur corrodé ou desserré.

### Le démarreur tourne mais le moteur ne part pas
- **Problème d'alimentation carburant** : Pompe à carburant HS, filtre à carburant bouché, ou relais de pompe défaillant.
- **Problème d'allumage (essence)** : Bougies encrassées, bobine d'allumage défaillante, capteur vilebrequin HS.
- **Problème d'injection (diesel)** : Injecteurs grippés, préchauffage défaillant (surtout par temps froid), capteur PMH.

## Voyant batterie allumé

- **Alternateur défaillant** : L'alternateur ne charge plus. La batterie se vide progressivement. Vérifier la tension moteur tournant (doit être entre 13.5V et 14.5V).
- **Courroie d'alternateur lâche ou cassée** : Sifflement au démarrage, voyant batterie intermittent.
- **Régulateur de tension HS** : Surcharge ou sous-charge de la batterie.

## Chute de tension intermittente

- **Consommateur parasite** : Un équipement reste sous tension moteur coupé (autoradio, éclairage coffre, etc.). Mesurer le courant de repos (< 50mA normal).
- **Batterie en fin de vie** : Plus de 4-5 ans, la batterie perd sa capacité. Tester avec un testeur de charge.

## Quand consulter un professionnel

- Démarreur qui tourne au ralenti (bruit anormal)
- Fumée ou odeur de brûlé au niveau du démarreur
- Batterie neuve qui se décharge en moins de 48h
- Voyant batterie qui s'allume en roulant
