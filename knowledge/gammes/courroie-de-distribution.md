---
category: distribution
slug: courroie-de-distribution
title: Courroie de distribution
pg_id: 306
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
  role: Kit complet pour la synchronisation de la distribution avec tous les composants necessaires
  must_be_true:
  - synchroniser
  - entrainer
  - maintenir
  must_not_contain:
  - chaine
  - universel
  - tous moteurs
  - adaptable
  confusion_with:
  - term: chaine-de-distribution
    difference: Courroie = caoutchouc à remplacer, Chaîne = métal plus durable
  - term: courroie-d-accessoire
    difference: Courroie distribution = synchronise moteur (CRITIQUE), Courroie accessoire = alternateur/clim (moins critique)
  related_parts:
  - kit-de-distribution
  - galet-tendeur-de-courroie-de-distribution
  - galet-enrouleur-de-courroie-de-distribution
  - pompe-a-eau
selection:
  criteria:
  - Marque de votre véhicule
  - Modele de votre véhicule
  - Motorisation de votre véhicule
  - Annee de votre véhicule
  anti_mistakes:
  - ❌ "évite la casse moteur"
  - ❌ "sécurité garantie"
  - ❌ "garanti CT"
  cost_range:
    min: 19
    max: 38
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Pièce OE (Origine Équipement)
    description: Courroie identique à l origine, fabriquée selon les spécifications exactes du constructeur. Option recommandée
      sur moteurs fragiles (moteurs interférents).
  - tier: Kit distribution complet (équivalent OE)
    description: Kit incluant courroie, galets tendeurs et galet enrouleur. Les fabricants de rang 1 fournissent les constructeurs
      automobiles.
  - tier: Courroie seule sans galets
    description: Remplacer la courroie sans les galets n est pas recommandé. Les galets usés peuvent casser une courroie neuve
      rapidement.
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
    label: Aucun symptome visible courroie casse
    severity: confort
  - id: S2
    label: Echeance kilometrique ou temps depassee
    severity: confort
  - id: S3
    label: Traces de craquelures sur la courroie si visible
    severity: confort
  - id: S4
    label: Bruit de claquement cote distribution
    severity: confort
  - id: S5
    label: Fuite de liquide de refroidissement pompe a eau
    severity: confort
  - id: S6
    label: Jeu dans le galet tendeur
    severity: confort
  - id: S7
    label: Courroie effilochee sur les bords
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  quick_checks:
  - 'Observer : aucun symptome visible courroie casse ?'
  - 'Observer : echeance kilometrique ou temps depassee ?'
  - 'Observer : traces de craquelures sur la courroie si visible ?'
  - Bruit de claquement cote distribution ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Aucun symptome visible courroie casse
  - Echeance kilometrique ou temps depassee
  - Traces de craquelures sur la courroie si visible
  - Bruit de claquement cote distribution
  - Fuite de liquide de refroidissement pompe a eau
  - Jeu dans le galet tendeur
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '306'
  intro_title: A quoi sert Courroie de distribution ?
  risk_title: Pourquoi remplacer Courroie de distribution a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Défaillance progressive** - Usure normale due à l''utilisation'
  - '**Conditions d''utilisation** - Sollicitations excessives ou environnement défavorable'
  - ❌ "évite la casse moteur"
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
  - question: Comment choisir Courroie de distribution compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Courroie de distribution ?
    answer: En cas de aucun symptome visible courroie casse ou de degradation mesurable, il faut controler rapidement avant
      panne secondaire.
  - question: Puis-je monter Courroie de distribution sans verification atelier ?
    answer: Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure
      constructeur.
  quality:
    score: 76
    source: script:rag-upgrade-v4
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous moteurs
  - adaptable
  requires_vehicle: true
doc_id: e616e207-a589-5a29-83a5-70701bebe187
content_hash: sha256:3bb2b16c0b2283ce
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

# Courroie de distribution - Guide Diagnostic Complet

## Fonction et Rôle

Kit complet pour la synchronisation de la distribution avec tous les composants necessaires

**Actions principales:** synchroniser, entrainer, maintenir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Aucun symptome visible courroie casse**
  aucun symptome visible courroie casse
- **Bruit de claquement cote distribution**
  bruit de claquement cote distribution

### 🟢 Autres Symptômes

- echeance kilometrique ou temps depassee
- traces de craquelures sur la courroie si visible
- fuite de liquide de refroidissement pompe a eau
- jeu dans le galet tendeur
- courroie effilochee sur les bords

## Procédure de Diagnostic

Pour diagnostiquer un problème de courroie de distribution:

1. **Inspection visuelle** - Examiner l'état du courroie de distribution
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-d-accessoire
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- kit-de-distribution
- pompe-a-eau
- poulie-d-arbre-a-came
- poulie-vilebrequin

## ⚠️ Ne Pas Confondre Avec

### courroie-d-accessoire
**Distinction:** Courroie distribution = synchronise moteur (CRITIQUE), Courroie accessoire = alternateur/clim (moins critique)

### chaine-de-distribution
**Distinction:** Courroie = caoutchouc à remplacer, Chaîne = métal plus durable

## Critères de Compatibilité

Pour commander le bon courroie de distribution, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Motorisation** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "évite la casse moteur"
- ❌ "sécurité garantie"
- ❌ "garanti CT"

## FAQ

**Comment choisir Courroie de distribution compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Courroie de distribution ?**
En cas de aucun symptome visible courroie casse ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Courroie de distribution sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.


## References supplementaires

<!-- materialized-from-db guides/choisir-courroie-distribution.md 2026-01-08 -->
### Guide - Choisir son kit distribution

# Comment choisir son kit de distribution

## Composition d'un kit complet

### Kit standard
- Courroie de distribution
- Galet tendeur
- Galet(s) enrouleur(s)

### Kit complet (recommande)
- Kit standard +
- Pompe a eau
- Courroie accessoires (option)

## Criteres de choix

### 1. Reference exacte
- **OEM** : Reference constructeur (ex: 0831V4 PSA)
- **Equivalence** : Cross-reference equipementier
- **Verification** : Nombre de dents, largeur, profil

### 2. Qualite courroie
| Materiau | Avantage | Duree vie |
|----------|----------|-----------|
| HNBR | Standard, fiable | 120 000 km |
| EPDM | Resistant chaleur | 160 000 km |
| HSN | Haute performance | 180 000 km |

### 3. Pompe a eau incluse?
- **Recommande** : Toujours remplacer avec
- **Raison** : Meme niveau d'usure, cout main d'oeuvre
- **Exception** : Pompe a eau entrainee par courroie accessoires

## Marques de reference

### Premiere monte
| Marque | Constructeurs |
|--------|---------------|
| **Gates** | PSA, Renault, VAG |
| **Contitech** | VAG, BMW, Mercedes |
| **Dayco** | Fiat, Alfa, Lancia |
| **INA** | VAG, BMW |

### Alternative qualite
| Marque | Commentaire |
|--------|-------------|
| **SKF** | Kits complets haute qualite |
| **Febi** | Bonne alternative |
| **Quinton Hazell** | Budget, garantie 2 ans |

## Intervalles par constructeur

### PSA (Peugeot/Citroen)
| Moteur | Intervalle |
|--------|------------|
| TU (1.0-1.6) | 80 000 km / 5 ans |
| DV4/DV6 HDi | 100 000 km / 10 ans |
| DW10 HDi | 120 000 km / 6 ans |
| EB PureTech | 100 000 km / 10 ans |

### Renault
| Moteur | Intervalle |
|--------|------------|
| K4M/K7M | 120 000 km / 6 ans |
| K9K dCi | 90-120 000 km selon version |
| F9Q | 120 000 km |
| M9R | 120 000 km / 6 ans |

### VAG (VW/Audi/Seat/Skoda)
| Moteur | Intervalle |
|--------|------------|
| 1.6 TDI CAYC | 120 000 km / 5 ans |
| 2.0 TDI CR | 120 000 km / 5 ans |
| TSI | Chaine (pas d'entretien) |

## Signes de remplacement urgent

### Visuels
- Craquelures sur courroie
- Usure laterale (desalignement)
- Traces de poudre noire

### Sonores
- Couinement au demarrage
- Claquement periodique
- Bruit de galet

### Preventif
- Kilometrage atteint
- Age depasse (meme faible km)
- Apres fuite pompe a eau/joint SPI

## Conseils pratiques

1. **Ne jamais depasser l'intervalle** : Casse = moteur HS
2. **Kit complet** : Economise la main d'oeuvre future
3. **Pompe a eau** : Inclure systematiquement
4. **Courroie accessoires** : Profiter de l'intervention
5. **Liquide refroidissement** : Vidanger lors du remplacement
6. **Carnet entretien** : Tamponner avec date et km

## Symptomes supplementaires

<!-- materialized-from-db diagnostic/distribution-courroie.md 2026-01-08 -->
### Diagnostic - Distribution et courroie

# Distribution et courroie - Diagnostic complet

## Symptomes courants

### Bruit de claquement moteur
- **Quand** : Au ralenti ou a l'acceleration
- **Caracteristique** : Claquement rythmique, lie au regime moteur

### Sifflement au demarrage
- **Quand** : A froid, disparait a chaud
- **Caracteristique** : Son aigu type courroie patinante

### Perte de puissance
- **Quand** : En acceleration
- **Caracteristique** : Moteur qui "tire" moins

### Temoin moteur allume
- **Quand** : Aleatoire
- **Caracteristique** : Voyant orange fixe

## Causes possibles et solutions

### 1. Courroie de distribution usee
- **Probabilite** : 40%
- **Verification** : Age/kilometrage, aspect visuel (fissures, effilochage)
- **Solution** : Remplacement kit distribution complet
- **Pieces** : Kit distribution (courroie, galets, pompe a eau)
- **Urgence** : CRITIQUE - Risque casse moteur

### 2. Galet tendeur defaillant
- **Probabilite** : 25%
- **Verification** : Jeu excessif, bruit de roulement
- **Solution** : Remplacement galet(s)
- **Pieces** : Galet tendeur, galet enrouleur
- **Urgence** : Haute

### 3. Pompe a eau HS
- **Probabilite** : 20%
- **Verification** : Fuite liquide de refroidissement, jeu axial
- **Solution** : Remplacement pompe a eau
- **Pieces** : Pompe a eau
- **Urgence** : Haute

### 4. Courroie accessoires usee
- **Probabilite** : 15%
- **Verification** : Fissures, patinage
- **Solution** : Remplacement courroie accessoires
- **Pieces** : Courroie poly-V, galet tendeur accessoires
- **Urgence** : Moyenne

## Intervalles de remplacement

| Type moteur | Intervalle | Kilometrage |
|-------------|------------|-------------|
| Essence | 5 ans | 100 000 km |
| Diesel | 5 ans | 120 000 km |
| HDI/TDI | 4 ans | 160 000 km |

## Recommandations

- **Remplacement preventif** : Respecter les preconisations constructeur
- **Kit complet** : Toujours remplacer courroie + galets + pompe a eau ensemble
- **Marques** : Privilegier Gates, Continental, SKF
- **Huile** : Verifier absence de fuites d'huile sur la courroie
