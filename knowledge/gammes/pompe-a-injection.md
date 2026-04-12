---
category: alimentation
slug: pompe-a-injection
title: Pompe à injection
pg_id: 3904
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-04-04'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:materialize-db-to-md
  last_enriched_at: '2026-04-04'
  v5_migrated_at: '2026-03-29'
domain:
  role: Mettre le carburant sous haute pression pour alimenter les injecteurs
  must_be_true:
  - pressuriser
  - alimenter
  - comprimer
  must_not_contain:
  - basse pression
  - reservoir
  - air
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - injecteur
  - pompe-a-haute-pression
  - corps-papillon
  - debitmetre-d-air
  - regulateur-de-pression-carburant
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
    min: 200
    max: 800
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE — equipementiers injection
  - tier: Reconditionne (echange standard)
  brands:
    premium:
    - Bosch
    - Delphi
    - Denso
    standard:
    - Siemens VDO
    - Pierburg
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Demarrage difficile
    severity: confort
  - id: S2
    label: Perte de puissance
    severity: confort
  - id: S3
    label: Fumee
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : demarrage difficile'
  quick_checks:
  - 'Observer : demarrage difficile ?'
  - 'Observer : perte de puissance ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Demarrage difficile
  - Perte de puissance
  good_practices:
  - Utiliser du carburant de qualite pour preserver les injecteurs
  - Remplacement du filtre a carburant selon intervalle constructeur
  - Diagnostic electronique (OBD) en cas de perte de puissance
  - Ne pas rouler en reserve de carburant (pompe immergee non lubrifee)
rendering:
  pgId: '3904'
  intro_title: A quoi sert Pompe à injection ?
  risk_title: Pourquoi remplacer Pompe à injection a temps ?
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
  - question: Comment choisir Pompe à injection compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Pompe à injection ?
    answer: En cas de demarrage difficile ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Pompe à injection sans verification atelier ?
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
doc_id: eb49ed25-1cbc-5ef5-b417-2ae826ca340c
content_hash: sha256:838d98f0e3ac0b3b
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
  area: Sur le moteur (rampe injection, admission)
  access: Par le dessus (capot)
  adjacent_parts:
  - rampe
  - injecteurs
  - calculateur moteur
  - papillon
installation:
  difficulty: moyen a difficile
  time: 30min a 2h
  tools:
  - cle a douille
  - cle dynamometrique
  - diagnostic OBD
  prerequisite: Depressuriser le circuit carburant avant depose
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-04'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: hydraulique
    source_ref: corpus RAG web OEM
  technical_notes:
    val_000_bars: 000 bars
  materials:
  - materiau: aluminium
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Mettre le carburant sous haute pression pour alimenter les injecteurs. Pièces liées : vérifier les composants adjacents
    lors du remplacement.'
  S2: 'Intervalle : selon constructeur. Symptômes de défaillance : - Demarrage difficile- Perte de puissance'
  S3: 'Pour choisir le bon pompe à injection pour votre véhicule : - Marque de votre véhicule- Modele de votre véhicule- Annee
    de votre véhicule- Marques : Bosch, Delphi, Denso (premium), Siemens VDO, Pierburg (standard), Ridex (budget)- Budget
    : 200 à 800 EUR'
  S4_DEPOSE: 1. Débrancher la batterie. 2. Localiser la pièce selon la documentation constructeur. 3. Déconnecter les connecteurs
    électriques et raccords. 4. Dévisser les fixations de la pièce. 5. Déposer la pièce en notant l'orientation et la position
    de montage. 6. Nettoyer le logement et vérifier l'état des pièces adjacentes.
  S5: 'Erreurs fréquentes avec le pompe à injection : - Ne pas vérifier la référence exacte avant commande — une pièce de
    mauvaise référence ne fonctionne pas correctement même si elle se monte physiquement- Oublier de débrancher la batterie
    avant intervention — risque de court-circuit sur les composants électroniques- Ne pas respecter le couple de serrage constructeur
    au remontage- Ignorer les symptômes d''usure en espérant que ça passe — une défaillance progressive s''aggrave toujours-
    Ne pas effacer les codes défaut après remplacement — le calculateur peut rester en mode dégradé'
  S6: 'Après le remplacement du pompe à injection : - Utiliser du carburant de qualite pour preserver les injecteurs- Remplacement
    du filtre a carburant selon intervalle constructeur- Diagnostic electronique (OBD) en cas de perte de puissance- Ne pas
    rouler en reserve de carburant (pompe immergee non lubrifee)- Effacer les codes défaut éventuels avec l''outil OBD- Effectuer
    un essai route pour confirmer la disparition des symptômes'
---

# Pompe à injection - Guide Diagnostic Complet

## Fonction et Rôle

Mettre le carburant sous haute pression pour alimenter les injecteurs

**Actions principales:** pressuriser, alimenter, comprimer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- demarrage difficile
- perte de puissance
- fumee

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à injection:

1. **Inspection visuelle** - Examiner l'état du pompe à injection
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

- capteur-pression-de-carburant
- injecteur

## Critères de Compatibilité

Pour commander le bon pompe à injection, vous devez connaître:

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

**Comment choisir Pompe à injection compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Pompe à injection ?**
En cas de demarrage difficile ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Pompe à injection sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
## Symptomes injecteurs defaillants

### Moteur qui broute
- **Quand** : Acceleration, montee en regime
- **Caracteristique** : A-coups, rates d'allumage
- **Distinction** : Un cylindre vs plusieurs

### Fumee noire echappement (diesel)
- **Quand** : Acceleration franche
- **Caracteristique** : Fumee noire epaisse
- **Cause** : Injecteur qui fuit, mauvaise pulverisation

### Surconsommation carburant
- **Quand** : Usage normal
- **Caracteristique** : +20% consommation sans raison
- **Indication** : Injecteur coule ou mauvais dosage

### Ralenti instable
- **Quand** : Moteur au ralenti
- **Caracteristique** : Variations RPM, vibrations
- **Test** : Debranchement successif injecteurs

### Difficulte demarrage
- **Quand** : A froid principalement
- **Caracteristique** : Plusieurs tentatives necessaires
- **Diesel** : Souvent lie au circuit basse pression

## Symptomes pompe injection/HP

### Moteur ne demarre pas
- **Quand** : Tentative demarrage
- **Caracteristique** : Moteur tourne mais ne part pas
- **Diesel** : Pression rampe commune insuffisante

### Perte de puissance brutale
- **Quand** : En roulant
- **Caracteristique** : Moteur passe en mode degrade
- **Voyant** : Check engine allume

### Claquement moteur diesel
- **Quand** : A froid ou constant
- **Caracteristique** : Claquement metallique prononce
- **Cause** : Calage injection decale, injecteur defaillant

## Causes et solutions - Injecteurs essence

### 1. Injecteurs encrasses
- **Probabilite** : 50%
- **Verification** : Lecture defauts, test debit
- **Solution** : Nettoyage ultrasons ou additif
- **Pieces** : Nettoyant injecteurs, injecteurs neufs si necessaire
- **Urgence** : Moyenne

### 2. Bobine d'allumage HS
- **Probabilite** : 30%
- **Verification** : Code defaut Pxxxx (rate allumage)
- **Solution** : Remplacement bobine concernee
- **Pieces** : Bobine allumage
- **Urgence** : Moyenne

### 3. Injecteur fuyant
- **Probabilite** : 15%
- **Verification** : Test etancheite, odeur essence
- **Solution** : Remplacement injecteur
- **Pieces** : Injecteur + joints
- **Urgence** : Haute (risque incendie)

### 4. Regulateur pression carburant
- **Probabilite** : 5%
- **Verification** : Pression rampe (3-4 bar essence)
- **Solution** : Remplacement regulateur
- **Pieces** : Regulateur pression
- **Urgence** : Moyenne

## Causes et solutions - Injecteurs diesel (HDi, dCi, TDI)

### 1. Injecteurs uses
- **Probabilite** : 40%
- **Verification** : Test retour injecteurs, valise diag
- **Solution** : Echange standard ou reparation
- **Pieces** : Injecteurs (Bosch, Delphi, Siemens)
- **Urgence** : Haute
- **Cout** : 150-400€/injecteur selon type

### 2. Pompe haute pression fatiguee
- **Probabilite** : 25%
- **Verification** : Pression rampe < spec (1600-2000 bar)
- **Solution** : Echange standard pompe HP
- **Pieces** : Pompe HP
- **Urgence** : Haute

### 3. Capteur pression rampe HS
- **Probabilite** : 15%
- **Verification** : Code defaut P0190-P0194
- **Solution** : Remplacement capteur
- **Pieces** : Capteur pression rail
- **Urgence** : Moyenne

### 4. Filtre a gasoil colmate
- **Probabilite** : 15%
- **Verification** : Historique entretien, eau dans filtre
- **Solution** : Remplacement filtre + purge
- **Pieces** : Filtre a gasoil
- **Urgence** : Basse

### 5. Pompe de gavage faible
- **Probabilite** : 5%
- **Verification** : Pression basse pression (0.3-0.5 bar)
- **Solution** : Remplacement pompe gavage
- **Pieces** : Pompe immergee reservoir
- **Urgence** : Moyenne

## Codes defaut frequents

| Code | Description | Cause probable |
|------|-------------|----------------|
| P0201-P0204 | Circuit injecteur cyl 1-4 | Injecteur ou cablage |
| P0300 | Rates multiples detectes | Plusieurs injecteurs |
| P0190 | Capteur pression rail | Capteur ou rampe |
| P0087 | Pression rail trop basse | Pompe HP, fuite |
| P0088 | Pression rail trop haute | Regulateur |
| P2146 | Alimentation injecteurs | Fusible, relais, ECU |

## Entretien preventif

### Essence
- Additif nettoyant : Tous les 20 000 km
- Remplacement injecteurs : Rarement necessaire (>200 000 km)

### Diesel
- Filtre a gasoil : 60 000 km (30 000 km si gazole de qualite variable)
- Additif : A chaque plein en hiver (antigel)
- Nettoyage injecteurs : Tous les 80 000 km

## Recommandations

- **Qualite carburant** : SP95-E10 ou SP98 essence, gasoil premium diesel
- **Diagnostic** : Toujours lire les codes defaut avant intervention
- **Echange standard** : Solution economique pour injecteurs diesel
- **Marques** : Bosch, Delphi, Siemens VDO, Denso
- **Calibration** : Obligatoire apres remplacement injecteurs diesel (code IMA)
