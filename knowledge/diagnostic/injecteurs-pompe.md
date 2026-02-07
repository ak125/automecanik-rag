---
title: "Diagnostic - Injecteurs et systeme injection"
source_type: diagnostic
category: injection
truth_level: L2
verification_status: verified
updated_at: 2026-01-08
---

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
