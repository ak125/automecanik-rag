---
category: alimentation
slug: corps-papillon
title: Boîtier papillon
pg_id: 158
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
  role: Doser la quantite d'air admise dans le moteur en fonction de la position de l'accelerateur
  must_be_true:
  - doser
  - reguler
  - controler
  must_not_contain:
  - carburant
  - injection
  - injecteur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - injecteur
  - pompe-a-injection
  - pompe-a-haute-pression
  - debitmetre-d-air
  - regulateur-de-pression-carburant
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de compatibilite
    pour confirmer Boîtier papillon.
  - Verifier la reference OE ou equivalence constructeur pour le vehicule exact
  - Controler la compatibilite avec le systeme d injection (common rail, TDI, HDi)
  - Choisir un equipementier specialise (Bosch, Delphi, Denso, Siemens VDO)
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "plus de puissance"
  cost_range:
    min: 150
    max: 400
    currency: EUR
    unit: boîtier complet
    source: catalogue automecanik
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
    label: Ralenti instable ou irregulier
    severity: confort
  - id: S2
    label: Accelerations saccadees ou a-coups
    severity: confort
  - id: S3
    label: Moteur qui cale au demarrage ou au ralenti
    severity: immobilisation
  - id: S4
    label: Sifflement d air au niveau de l admission
    severity: confort
  - id: S5
    label: Odeur d essence melange trop riche
    severity: confort
  - id: S6
    label: Plus de 100 000 km sans nettoyage
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - remplacement preventif recommande
  quick_checks:
  - 'Observer : ralenti instable ou irregulier ?'
  - 'Observer : accelerations saccadees ou a-coups ?'
  - 'Observer : moteur qui cale au demarrage ou au ralenti ?'
  - 'Observer : sifflement d air au niveau de l admission ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Ralenti instable ou irregulier
  - Accelerations saccadees ou a-coups
  - Moteur qui cale au demarrage ou au ralenti
  - Sifflement d air au niveau de l admission
  - Odeur d essence melange trop riche
  - Plus de 100 000 km sans nettoyage
  good_practices:
  - Utiliser du carburant de qualite pour preserver les injecteurs
  - Remplacement du filtre a carburant selon intervalle constructeur
  - Diagnostic electronique (OBD) en cas de perte de puissance
  - Ne pas rouler en reserve de carburant (pompe immergee non lubrifee)
rendering:
  pgId: '158'
  intro_title: A quoi sert Boîtier papillon ?
  risk_title: Pourquoi remplacer Boîtier papillon a temps ?
  risk_explanation: '**Pièce HS** - Le boîtier papillon peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le boîtier papillon peut être hors service et nécessiter un remplacement'
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
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
  - question: Boîtier papillon OE ou adaptable ?
    answer: Privilégiez l'OE ou OES (Bosch, VDO, Continental). Le boîtier papillon est calibré avec le calculateur. Un adaptable
      peut nécessiter une réadaptation.
  - question: Comment savoir si mon boîtier papillon est HS ?
    answer: Ralenti instable, accélérations saccadées, voyant moteur allumé, perte de puissance, moteur qui cale au démarrage
      ou au ralenti.
  - question: Tous les combien nettoyer le boîtier papillon ?
    answer: Nettoyage conseillé tous les 30 000 à 50 000 km. Plus souvent si petits trajets urbains. Pas de périodicité de
      remplacement fixe.
  - question: Peut-on nettoyer le boîtier papillon soi-même ?
    answer: Oui, avec un spray nettoyant carburateur. Démonter le conduit d'admission, nettoyer le volet et les parois. Attention
      à ne pas forcer le volet.
  - question: Quelle erreur éviter avec le boîtier papillon ?
    answer: Ne pas forcer le volet manuellement sur les boîtiers motorisés. Après nettoyage ou remplacement, une réadaptation
      par valise peut être nécessaire.
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
doc_id: 94577777-70a8-53ce-9cd7-c10fca2b03f0
content_hash: sha256:ab59f67ca60e0d8c
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
---

# Boîtier papillon - Guide Diagnostic Complet

## Fonction et Rôle

Doser la quantite d'air admise dans le moteur en fonction de la position de l'accelerateur

**Actions principales:** doser, reguler, controler

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Moteur qui cale au demarrage ou au ralenti**
  moteur qui cale au demarrage ou au ralenti

### 🟢 Autres Symptômes

- ralenti instable ou irregulier
- accelerations saccadees ou a-coups
- sifflement d air au niveau de l admission
- odeur d essence melange trop riche
- plus de 100 000 km sans nettoyage

## Procédure de Diagnostic

Pour diagnostiquer un problème de boîtier papillon:

1. **Inspection visuelle** - Examiner l'état du boîtier papillon
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le boîtier papillon peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-position-papillon
- capteur-de-cognement
- capteur-temperature-d-air-admission
- corps-papillon
- injecteur
- valve-de-reglage-du-ralenti

## Critères de Compatibilité

Pour commander le bon boîtier papillon, vous devez connaître:

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

**Boîtier papillon OE ou adaptable ?**
Privilégiez l'OE ou OES (Bosch, VDO, Continental). Le boîtier papillon est calibré avec le calculateur. Un adaptable peut nécessiter une réadaptation.

**Comment savoir si mon boîtier papillon est HS ?**
Ralenti instable, accélérations saccadées, voyant moteur allumé, perte de puissance, moteur qui cale au démarrage ou au ralenti.

**Tous les combien nettoyer le boîtier papillon ?**
Nettoyage conseillé tous les 30 000 à 50 000 km. Plus souvent si petits trajets urbains. Pas de périodicité de remplacement fixe.

**Peut-on nettoyer le boîtier papillon soi-même ?**
Oui, avec un spray nettoyant carburateur. Démonter le conduit d'admission, nettoyer le volet et les parois. Attention à ne pas forcer le volet.

**Quelle erreur éviter avec le boîtier papillon ?**
Ne pas forcer le volet manuellement sur les boîtiers motorisés. Après nettoyage ou remplacement, une réadaptation par valise peut être nécessaire.


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
