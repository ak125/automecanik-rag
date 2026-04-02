---
category: alimentation
slug: pompe-a-haute-pression
title: Pompe à haute pression
pg_id: 3918
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-03-29'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: skill:phase5-hella-ngk
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Mettre le carburant sous tres haute pression pour l'injection directe
  must_be_true:
  - pressuriser
  - comprimer
  - alimenter
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
  - injecteur
  - pompe-a-injection
  - corps-papillon
  - debitmetre-d-air
  - regulateur-de-pression-carburant
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Marque et modele du vehicule
  - Motorisation exacte (diesel injection directe, essence injection directe)
  - Reference constructeur ou equipementier (Bosch, Delphi, Continental, Denso)
  - Type de carburant (diesel common rail, essence GDI/TSI/TFSI)
  - Pression de service (bar) compatible avec le systeme d'injection
  - Nombre de pistons et debit (litres/heure)
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
    source: estimation categorie
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
    label: Demarrage impossible ou tres long
    severity: confort
  - id: S2
    label: Perte de puissance brutale
    severity: confort
  - id: S3
    label: Limaille dans le filtre a gasoil
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'Usure ou defaillance causant : demarrage impossible ou tres long'
  - 'Usure ou defaillance causant : perte de puissance brutale'
  quick_checks:
  - 'Observer : demarrage impossible ou tres long ?'
  - 'Observer : perte de puissance brutale ?'
  - 'Observer : limaille dans le filtre a gasoil ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Demarrage impossible ou tres long
  - Perte de puissance brutale
  - Limaille dans le filtre a gasoil
  good_practices:
  - Utiliser du carburant de qualite pour preserver les injecteurs
  - Remplacement du filtre a carburant selon intervalle constructeur
  - Diagnostic electronique (OBD) en cas de perte de puissance
  - Ne pas rouler en reserve de carburant (pompe immergee non lubrifee)
rendering:
  pgId: '3918'
  intro_title: A quoi sert Pompe à haute pression ?
  risk_title: Pourquoi remplacer Pompe à haute pression a temps ?
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
  - question: Comment choisir Pompe à haute pression compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Pompe à haute pression ?
    answer: En cas de demarrage impossible ou tres long ou de degradation mesurable, il faut controler rapidement avant panne
      secondaire.
  - question: Puis-je monter Pompe à haute pression sans verification atelier ?
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
doc_id: e63ef18e-3dae-58a4-b348-41cb59f303f0
content_hash: sha256:66427798dca7b4e0
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
  _source: HELLA TechWorld + NGK/NTK
  _validation_status: oem_verified
  _enriched_at: '2026-03-29'
  types_variants:
  - type: Pompe a piston radial monocylindre
    description: Avec poussoir a galet, la plus courante (Bosch CP1/CP3/CP4)
    era: standard common rail
  - type: Pompe axiale / en serie
    description: Un ou plusieurs elements de pompage
    era: anciens systemes
  technical_notes:
    pression_service: '50-350 bars selon configuration'
    pression_basse_normale: '~4,0 bars'
    pression_demarrage: '~7,0 bars'
    pression_residuelle_10min: '>= 3,0 bars'
    pression_haute: '40-120 bars selon regime'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    La pompe à haute pression met le carburant sous très haute pression pour
    l''injection directe dans les cylindres. Sur les moteurs diesel common rail,
    elle comprime le carburant de 200 bars au ralenti à 1800-2200 bars à pleine
    charge. Sur les moteurs essence injection directe (GDI/TSI/TFSI), la
    pression varie de 50 à 350 bars. Niveau de difficulté : Avancé —
    intervention sur le circuit haute pression, nécessite des précautions de
    sécurité strictes. Comptez 2 à 4 heures. Outils : clé dynamométrique, clés à
    tuyauter (raccords haute pression), outil OBD pour purge et calibration.
    Pièces liées : injecteurs, rampe d''injection (common rail), filtre à
    carburant, pompe de gavage (basse pression, dans le réservoir).
  S2: >-
    Pas de périodicité fixe. Durée de vie : 200 000+ km si le filtre à carburant
    est remplacé régulièrement. Symptômes de défaillance : - Démarrage
    impossible ou très long — la pompe ne monte plus en pression suffisante pour
    ouvrir les injecteurs- Perte de puissance brutale — le calculateur limite la
    pression d''injection en mode dégradé- Limaille métallique dans le filtre à
    gasoil — usure interne des pistons ou des clapets de la pompe, débris
    envoyés dans tout le circuit- Voyant moteur allumé avec codes pression de
    rampe (P0087 : pression trop basse, P0088 : pression trop haute)- Broutement
    ou à-coups à l''accélération — pression d''injection instable
  S3: >-
    Pour choisir la bonne pompe haute pression : - Motorisation exacte : diesel
    common rail ou essence injection directe — les pompes ne sont pas
    interchangeables même entre variantes du même moteur- Référence constructeur
    : vérifier la référence Bosch CP1/CP3/CP4, Delphi DFP, Continental/Siemens —
    chaque variante a un débit et une pression max différents- Nombre de pistons
    et débit : les pompes CP4.1 (1 piston) et CP4.2 (2 pistons) ne sont pas
    interchangeables- Pression de service : vérifier la compatibilité avec le
    système d''injection du véhicule (1350, 1600, 1800 ou 2200 bars selon
    génération)- Marques : Bosch, Delphi, Denso, Continental — pas d''adaptable
    recommandé sur ce composant critique- Budget : 200 à 800 EUR — les pompes
    reconditionnées échange standard offrent un bon rapport qualité/prix
  S4_DEPOSE: >-
    1. Débrancher la batterie et attendre 10 minutes (dépressurisation du
    circuit haute pression). 2. Nettoyer soigneusement la zone autour de la
    pompe pour éviter l''entrée de contaminants dans le circuit. 3. Débrancher
    les conduites haute pression (clé à tuyauter) — obturer immédiatement chaque
    raccord. 4. Débrancher la conduite d''alimentation basse pression (arrivée
    du filtre à carburant). 5. Débrancher le connecteur électrique du régulateur
    de débit. 6. Dévisser les vis de fixation de la pompe sur le bloc moteur (2
    à 3 vis). 7. Extraire la pompe en la tirant droit — ne pas forcer
    latéralement (arbre d''entraînement fragile). 8. Vérifier l''état du joint
    torique et de l''arbre d''entraînement côté moteur.
  S5: >-
    Erreurs fréquentes avec la pompe haute pression : - Ne pas remplacer le
    filtre à carburant avant de monter la pompe neuve — les impuretés et la
    limaille de l''ancienne pompe détruisent la pompe neuve en quelques milliers
    de km- Ne pas rincer la rampe d''injection et les conduites haute pression —
    les débris métalliques piégés dans le circuit contaminent la pompe neuve et
    les injecteurs- Oublier de remplir la pompe de carburant avant le premier
    démarrage — un démarrage à sec provoque un grippage immédiat des pistons-
    Forcer l''extraction de la pompe latéralement — l''arbre d''entraînement se
    tord et endommage l''entraînement côté moteur- Monter une pompe de mauvaise
    pression de service — une pompe CP4.1 à la place d''une CP4.2 ne fournit pas
    le débit suffisant à pleine charge- Ignorer la limaille dans le filtre à
    gasoil — c''est le signe que la pompe a distribué des débris métalliques
    dans tout le circuit (injecteurs, rampe, conduites). Un remplacement de
    pompe seul ne suffit pas
  S6: >-
    Après le remplacement de la pompe haute pression : - Purge d''air :
    actionner la pompe d''amorçage manuelle (diesel) ou lancer une purge via
    l''outil OBD — un circuit non purgé empêche le démarrage- Pression de rampe
    : vérifier avec l''outil OBD que la pression de rampe au ralenti correspond
    à la valeur constructeur (250-350 bars diesel, 50-120 bars essence GDI)-
    Test de démarrage : le moteur doit démarrer en moins de 5 secondes. Un
    démarrage trop long indique une purge incomplète ou un problème de clapet-
    Étanchéité : vérifier l''absence de fuite sur les raccords haute pression
    après 5 minutes de fonctionnement — la moindre fuite haute pression est
    dangereuse- Effacer les codes : supprimer les codes P0087/P0088 pour que le
    calculateur quitte le mode dégradé
---

# Pompe à haute pression - Guide Diagnostic Complet

## Fonction et Rôle

Mettre le carburant sous tres haute pression pour l'injection directe

**Actions principales:** pressuriser, comprimer, alimenter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- demarrage impossible ou tres long
- perte de puissance brutale
- limaille dans le filtre a gasoil

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à haute pression:

1. **Inspection visuelle** - Examiner l'état du pompe à haute pression
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

- rampe-d-injection
- injecteur
- regulateur-de-pression-carburant

## Critères de Compatibilité

Pour commander le bon pompe à haute pression, vous devez connaître:

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

**Comment choisir Pompe à haute pression compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Pompe à haute pression ?**
En cas de demarrage impossible ou tres long ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Pompe à haute pression sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.


## Symptomes supplementaires

<!-- materialized-from-db diagnostic/injecteurs-pompe.md 2026-01-08 -->
### Diagnostic - Injecteurs et systeme injection

# Injecteurs et systeme injection - Diagnostic complet

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
