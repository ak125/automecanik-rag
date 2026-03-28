---
category: distribution
slug: pompe-a-eau
title: Pompe à eau
pg_id: 1260
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
  role: Faire circuler le liquide de refroidissement dans le circuit moteur
  must_be_true:
  - faire circuler
  - pomper
  - alimenter
  must_not_contain:
  - huile
  - carburant
  - direction
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - courroie-de-distribution
  - kit-de-distribution
  - galet-tendeur-de-courroie-de-distribution
  - galet-enrouleur-de-courroie-de-distribution
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
  - ❌ "evite la casse moteur"
  cost_range:
    min: 20
    max: 130
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
    label: Fuite de liquide au niveau de la pompe
    severity: confort
  - id: S2
    label: Bruit de roulement cote distribution
    severity: confort
  - id: S3
    label: Jeu perceptible dans la poulie de pompe
    severity: confort
  - id: S4
    label: Surchauffe moteur malgre niveau correct
    severity: confort
  - id: S5
    label: Odeur de liquide de refroidissement chaud
    severity: confort
  - id: S6
    label: Echeance distribution approche preventif
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  quick_checks:
  - Fuite de liquide au niveau de la pompe ?
  - Bruit de roulement cote distribution ?
  - 'Observer : jeu perceptible dans la poulie de pompe ?'
  - 'Observer : surchauffe moteur malgre niveau correct ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Fuite de liquide au niveau de la pompe
  - Bruit de roulement cote distribution
  - Jeu perceptible dans la poulie de pompe
  - Surchauffe moteur malgre niveau correct
  - Odeur de liquide de refroidissement chaud
  - Echeance distribution approche preventif
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '1260'
  intro_title: A quoi sert Pompe à eau ?
  risk_title: Pourquoi remplacer Pompe à eau a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: Pompe à eau OE ou adaptable ?
    answer: Privilégiez l'OES (SKF, FAG, INA, Gates) pour une durée de vie garantie jusqu'à la prochaine distribution. Les
      adaptables sont risqués sur cette pièce critique.
  - question: Comment savoir si ma pompe à eau fuit ?
    answer: Fuite visible sous la pompe, bruit de roulement (grognement), jeu dans l'axe, traces de calcaire autour de la
      pompe, surchauffe moteur.
  - question: Tous les combien changer la pompe à eau ?
    answer: 'Avec la distribution : 80 000 à 120 000 km. Sinon, pas de périodicité fixe mais contrôle à chaque distribution.'
  - question: Peut-on changer la pompe à eau soi-même ?
    answer: Possible si accessible, mais souvent liée à la distribution. Nécessite vidange du circuit et purge soignée après
      montage.
  - question: Quelle erreur éviter avec la pompe à eau ?
    answer: Ne pas monter une pompe sans changer le joint. Vérifier le sens de rotation de la turbine. Purger correctement
      le circuit après.
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
doc_id: bf27168c-fddd-558d-96a2-f2363970e213
content_hash: sha256:6087d334eb8d426c
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

# Pompe à eau - Guide Diagnostic Complet

## Fonction et Rôle

Faire circuler le liquide de refroidissement dans le circuit moteur

**Actions principales:** faire circuler, pomper, alimenter, assurer la circulation

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Surchauffe moteur malgre niveau correct**
  surchauffe moteur malgre niveau correct

### 🟢 Autres Symptômes

- fuite de liquide au niveau de la pompe
- bruit de roulement cote distribution
- jeu perceptible dans la poulie de pompe
- odeur de liquide de refroidissement chaud
- echeance distribution approche preventif

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à eau:

1. **Inspection visuelle** - Examiner l'état du pompe à eau
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

- chaine-de-distribution
- courroie-d-accessoire
- courroie-de-distribution
- durite-de-refroidissement
- kit-de-chaine-de-distribution
- kit-de-distribution
- radiateur-de-refroidissement
- sonde-de-refroidissement

## Critères de Compatibilité

Pour commander le bon pompe à eau, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "evite la casse moteur"

## FAQ

**Pompe à eau OE ou adaptable ?**
Privilégiez l'OES (SKF, FAG, INA, Gates) pour une durée de vie garantie jusqu'à la prochaine distribution. Les adaptables sont risqués sur cette pièce critique.

**Comment savoir si ma pompe à eau fuit ?**
Fuite visible sous la pompe, bruit de roulement (grognement), jeu dans l'axe, traces de calcaire autour de la pompe, surchauffe moteur.

**Tous les combien changer la pompe à eau ?**
Avec la distribution : 80 000 à 120 000 km. Sinon, pas de périodicité fixe mais contrôle à chaque distribution.

**Peut-on changer la pompe à eau soi-même ?**
Possible si accessible, mais souvent liée à la distribution. Nécessite vidange du circuit et purge soignée après montage.

**Quelle erreur éviter avec la pompe à eau ?**
Ne pas monter une pompe sans changer le joint. Vérifier le sens de rotation de la turbine. Purger correctement le circuit après.


## References supplementaires

<!-- materialized-from-db guides/choisir-pompe-eau.md 2026-02-15 -->
### Guide - Comment choisir sa pompe à eau

# Comment choisir sa pompe à eau

## Rôle de la pompe à eau

- Fait circuler le liquide de refroidissement dans le circuit moteur
- Assure le refroidissement du moteur en toutes conditions
- Entraînée par la courroie de distribution ou la courroie accessoire selon les moteurs

## Types de pompes

### Pompe mécanique (standard)
- Entraînée par courroie. Turbine en métal ou plastique renforcé.
- La plus courante, remplacement lors du kit de distribution recommandé.

### Pompe électrique
- Présente sur certains véhicules récents (BMW, certains VW/Audi)
- Fonctionnement indépendant du régime moteur, meilleure gestion thermique
- Remplacement spécifique, plus coûteux

## Signes de défaillance

- **Fuite au joint** : Goutte visible sous le véhicule, trace de rouille ou de calcaire sur la pompe
- **Roulement bruyant** : Sifflement ou grondement provenant de la pompe, jeu sur l'axe
- **Surchauffe moteur** : La pompe ne fait plus circuler assez de liquide
- **Turbine dégradée** : Pales cassées ou érodées (plastique), circulation insuffisante

## Remplacement avec la distribution

- Sur les moteurs où la pompe est entraînée par la courroie de distribution, **toujours la remplacer en même temps**
- Le coût supplémentaire de la pompe est négligeable face au coût de la main d'œuvre
- Un kit distribution complet inclut souvent la pompe (vérifier le contenu)

## Marques recommandées

- **SKF** : Spécialiste roulements, pompes de qualité OE
- **Saleri** : Fabricant italien spécialisé, OE pour de nombreux constructeurs
- **Dolz** : Bon rapport qualité-prix, large couverture
- **Gates** : Souvent vendu en kit avec la distribution

## Erreurs à éviter

- Ne jamais réutiliser le joint d'étanchéité de la pompe
- Vérifier la compatibilité de la turbine (métal vs plastique) avec le type de liquide de refroidissement
- Ne pas oublier de purger le circuit après remplacement
- Toujours utiliser du liquide de refroidissement neuf compatible

## FAQ

**Faut-il changer la pompe à eau à chaque distribution ?** Oui, c'est fortement recommandé si elle est entraînée par la courroie de distribution. Le surcoût est faible par rapport au risque.

**Quelle durée de vie ?** Environ 100 000-150 000 km. Souvent alignée sur le remplacement de la distribution.

**Pompe OE ou aftermarket ?** Les deux sont acceptables si la marque est reconnue. Les pompes discount avec turbine en plastique de mauvaise qualité sont à éviter.

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

<!-- materialized-from-db diagnostic/refroidissement.md 2026-01-08 -->
### Diagnostic - Systeme de refroidissement

# Systeme de refroidissement - Diagnostic complet

## Symptomes surchauffe

### Temoin temperature allume
- **Quand** : En roulant ou a l'arret
- **Caracteristique** : Voyant rouge fixe ou clignotant
- **Urgence** : Critique - Arreter immediatement le moteur

### Temperature monte rapidement
- **Quand** : Apres quelques kilometres
- **Caracteristique** : Aiguille dans le rouge en moins de 10 min
- **Urgence** : Haute - Risque joint de culasse

### Chauffage habitacle faible
- **Quand** : Moteur chaud
- **Caracteristique** : Air tiede au lieu de chaud
- **Indication** : Niveau liquide bas ou thermostat bloque

### Fuite liquide de refroidissement
- **Quand** : Vehicule a l'arret
- **Caracteristique** : Flaque verte/orange sous le vehicule
- **Localisation** : Durites, radiateur, pompe a eau

## Symptomes thermostat

### Moteur long a chauffer
- **Quand** : Par temps froid
- **Caracteristique** : Temperature ne monte pas apres 10 km
- **Cause probable** : Thermostat bloque ouvert

### Temperature instable
- **Quand** : En roulant
- **Caracteristique** : Aiguille qui oscille
- **Cause probable** : Thermostat defaillant

## Causes et solutions - Surchauffe

### 1. Niveau liquide insuffisant
- **Probabilite** : 40%
- **Verification** : Niveau vase expansion (moteur froid)
- **Solution** : Completer et chercher la fuite
- **Pieces** : Liquide refroidissement G12/G13
- **Urgence** : Moyenne

### 2. Pompe a eau defaillante
- **Probabilite** : 25%
- **Verification** : Jeu sur axe, fuite par trou temoin
- **Solution** : Remplacement (souvent avec distribution)
- **Pieces** : Pompe a eau
- **Urgence** : Haute

### 3. Thermostat bloque ferme
- **Probabilite** : 20%
- **Verification** : Durite superieure radiateur froide moteur chaud
- **Solution** : Remplacement thermostat
- **Pieces** : Calorstat/thermostat
- **Urgence** : Haute

### 4. Ventilateur HS
- **Probabilite** : 10%
- **Verification** : Ne se declenche pas a 100°C
- **Solution** : Test motoventilateur, fusible, relais
- **Pieces** : Motoventilateur, relais
- **Urgence** : Moyenne

### 5. Radiateur bouche/fuyant
- **Probabilite** : 5%
- **Verification** : Zones froides sur radiateur, traces calcaire
- **Solution** : Rinçage ou remplacement
- **Pieces** : Radiateur
- **Urgence** : Moyenne

## Causes et solutions - Fuites

### 1. Durites percees/craquelees
- **Probabilite** : 35%
- **Verification** : Inspection visuelle, traces blanches
- **Solution** : Remplacement durite
- **Pieces** : Durites refroidissement
- **Urgence** : Moyenne

### 2. Joint de pompe a eau
- **Probabilite** : 25%
- **Verification** : Fuite par trou temoin pompe
- **Solution** : Remplacement pompe complete
- **Pieces** : Pompe a eau
- **Urgence** : Haute

### 3. Bouchon vase expansion
- **Probabilite** : 20%
- **Verification** : Pression circuit (tarage bouchon)
- **Solution** : Remplacement bouchon
- **Pieces** : Bouchon vase expansion
- **Urgence** : Basse

### 4. Joint de culasse
- **Probabilite** : 10%
- **Verification** : Mayonnaise sous bouchon huile, fumee blanche echappement
- **Solution** : Remplacement joint (intervention lourde)
- **Pieces** : Joint de culasse, kit vis
- **Urgence** : Critique

### 5. Radiateur de chauffage
- **Probabilite** : 10%
- **Verification** : Odeur sucree habitacle, buee pare-brise
- **Solution** : Remplacement radiateur chauffage
- **Pieces** : Radiateur de chauffage
- **Urgence** : Moyenne

## Diagnostics complementaires

### Test de pression circuit
- Outil : Pompe de mise en pression
- Pression : 1.2 à 1.5 bar selon vehicule
- But : Detecter fuites non visibles

### Test CO2 dans liquide
- Outil : Testeur de fuite joint culasse
- Indicateur : Changement couleur (bleu → jaune)
- But : Confirmer fuite joint de culasse

## Recommandations

- **Liquide** : Respecter specifications constructeur (G12, G13, type D)
- **Melange** : Ne jamais melanger differents types
- **Vidange** : Tous les 4-5 ans ou 100 000 km
- **Purge** : Obligatoire apres intervention (bulles d'air = surchauffe)
- **Marques** : Valeo, Gates, SKF (pompes), Behr (radiateurs)
