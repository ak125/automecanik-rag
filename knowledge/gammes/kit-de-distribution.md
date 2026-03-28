---
category: distribution
slug: kit-de-distribution
title: Kit de distribution
pg_id: 307
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
  role: Kit complet pour la distribution a chaine avec tous les composants (tendeur, patins, glissieres)
  must_be_true:
  - synchroniser
  - entrainer
  - guider
  must_not_contain:
  - courroie
  - caoutchouc
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - courroie-de-distribution
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
    min: 100
    max: 350
    currency: EUR
    unit: kit avec pompe
    source: catalogue automecanik
  quality_tiers:
  - tier: Equipement d'origine (OE)
    description: Kit complet fourni ou homologué par le constructeur du moteur. Courroie, galets et pompe à eau issus des
      mêmes fournisseurs que la première monte.
  - tier: Equivalent OE (OES) — kit complet recommandé
    description: Fabricants reconnus en systèmes de distribution (courroies et transmissions). L'important est de choisir
      un kit de marque reconnue et de ne jamais mélanger des pièces de provenances différentes.
  - tier: Kit partiel ou composants séparés
    description: 'Remplacement de la courroie seule ou des galets seuls. Approche déconseillée : si un composant est usé,
      les autres le sont probablement aussi.'
  - tier: Kit sans pompe à eau (budget minimum)
    description: Kits qui n'incluent pas la pompe à eau. Acceptable uniquement si la pompe a été récemment remplacée avec
      documentation.
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
    label: Echeance kilometrique ou temps atteinte
    severity: confort
  - id: S2
    label: Bruit de roulement cote distribution galet
    severity: confort
  - id: S3
    label: Fuite de liquide de refroidissement pompe a eau
    severity: confort
  - id: S4
    label: Sifflement au ralenti cote courroie
    severity: confort
  - id: S5
    label: Jeu dans les galets controle visuel
    severity: confort
  - id: S6
    label: Traces d usure sur la courroie
    severity: confort
  - id: S7
    label: Grincement au demarrage a froid
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - remplacement preventif recommande
  quick_checks:
  - 'Observer : echeance kilometrique ou temps atteinte ?'
  - Bruit de roulement cote distribution galet ?
  - Fuite de liquide de refroidissement pompe a eau ?
  - 'Observer : sifflement au ralenti cote courroie ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Echeance kilometrique ou temps atteinte
  - Bruit de roulement cote distribution galet
  - Fuite de liquide de refroidissement pompe a eau
  - Sifflement au ralenti cote courroie
  - Jeu dans les galets controle visuel
  - Traces d usure sur la courroie
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '307'
  intro_title: A quoi sert Kit de distribution ?
  risk_title: Pourquoi remplacer Kit de distribution a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
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
  - question: Que contient un kit de distribution ?
    answer: Courroie + galet tendeur + galet(s) enrouleur(s) + pompe à eau (selon kit). Certains kits incluent aussi les joints
      et vis.
  - question: Kit avec ou sans pompe à eau ?
    answer: Avec pompe recommandé. La pompe est entraînée par la courroie. Si elle grippe, elle peut bloquer la courroie et
      la faire casser.
  - question: Peut-on monter un kit soi-même ?
    answer: Déconseillé sans expérience. Le calage de la distribution est critique. Une dent de décalage peut endommager le
      moteur au démarrage.
  - question: Quelles sont les erreurs fréquentes à éviter ?
    answer: Acheter un kit sans pompe à eau pour économiser. Mal caler le moteur au remontage. Ne pas contrôler le jeu des
      galets avant achat.
  - question: Comment faire un diagnostic rapide ?
    answer: Kilométrage proche de l'échéance → kit complet. Bruit de roulement → galet suspect. Fuite liquide → pompe à eau.
      Les 3 → kit urgent.
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
doc_id: b202e9cc-2f8c-53a5-b3ff-7802be06373e
content_hash: sha256:417ae47e9cffe6d3
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

# Kit de distribution - Guide Diagnostic Complet

## Fonction et Rôle

Kit complet pour la distribution a chaine avec tous les composants (tendeur, patins, glissieres)

**Actions principales:** synchroniser, entrainer, guider

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Grincement au demarrage a froid**
  grincement au demarrage a froid

### 🟢 Autres Symptômes

- echeance kilometrique ou temps atteinte
- bruit de roulement cote distribution galet
- fuite de liquide de refroidissement pompe a eau
- sifflement au ralenti cote courroie
- jeu dans les galets controle visuel
- traces d usure sur la courroie

## Procédure de Diagnostic

Pour diagnostiquer un problème de kit de distribution:

1. **Inspection visuelle** - Examiner l'état du kit de distribution
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-d-accessoire
- pompe-a-eau
- poulie-d-arbre-a-came
- poulie-vilebrequin

## Critères de Compatibilité

Pour commander le bon kit de distribution, vous devez connaître:

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

**Que contient un kit de distribution ?**
Courroie + galet tendeur + galet(s) enrouleur(s) + pompe à eau (selon kit). Certains kits incluent aussi les joints et vis.

**Kit avec ou sans pompe à eau ?**
Avec pompe recommandé. La pompe est entraînée par la courroie. Si elle grippe, elle peut bloquer la courroie et la faire casser.

**Peut-on monter un kit soi-même ?**
Déconseillé sans expérience. Le calage de la distribution est critique. Une dent de décalage peut endommager le moteur au démarrage.

**Quelles sont les erreurs fréquentes à éviter ?**
Acheter un kit sans pompe à eau pour économiser. Mal caler le moteur au remontage. Ne pas contrôler le jeu des galets avant achat.

**Comment faire un diagnostic rapide ?**
Kilométrage proche de l'échéance → kit complet. Bruit de roulement → galet suspect. Fuite liquide → pompe à eau. Les 3 → kit urgent.


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
