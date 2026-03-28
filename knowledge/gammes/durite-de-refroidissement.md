---
category: refroidissement
slug: durite-de-refroidissement
title: Durite de refroidissement
pg_id: 475
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
  role: Acheminer le liquide de refroidissement entre les elements du circuit
  must_be_true:
  - acheminer
  - conduire
  - relier
  must_not_contain:
  - huile
  - carburant
  - frein
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - radiateur-de-refroidissement
  - pompe-a-eau
  - thermostat
  - vase-d-expansion
  - ventilateur-de-refroidissement
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
    min: 15
    max: 80
    currency: EUR
    unit: durite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
    description: 'Durite conforme aux spécifications constructeur : même matière, mêmes dimensions et mêmes raccords. Recommandé
      pour les véhicules récents ou à forte valeur.'
  - tier: Équipementier reconnu (refroidissement)
    description: Produit de fabricants spécialisés en circuit de refroidissement. Résistance thermique et pression de service
      équivalentes à la pièce d'origine.
  - tier: Durite silicone renforcée (aftermarket)
    description: Offre une résistance thermique et chimique supérieure à l'EPDM standard. Convient particulièrement pour les
      véhicules utilisés intensivement ou en conditions extrêmes. Vérifier la compatibilité des di
  brands:
    premium:
    - Behr/Mahle
    - Gates
    standard:
    - Valeo
    - NRF
    - Febi
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Traces de liquide colore sous le vehicule
    severity: confort
  - id: S2
    label: Durite visiblement gonflee ou craquelee
    severity: confort
  - id: S3
    label: Sifflement ou gargouillement dans le circuit
    severity: confort
  - id: S4
    label: Niveau de liquide qui baisse regulierement
    severity: confort
  - id: S5
    label: Odeur sucree de liquide de refroidissement
    severity: confort
  - id: S6
    label: Plus de 100 000 km ou 8 ans sans remplacement
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - remplacement preventif recommande
  quick_checks:
  - 'Observer : traces de liquide colore sous le vehicule ?'
  - 'Observer : durite visiblement gonflee ou craquelee ?'
  - 'Observer : sifflement ou gargouillement dans le circuit ?'
  - 'Observer : niveau de liquide qui baisse regulierement ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Traces de liquide colore sous le vehicule
  - Durite visiblement gonflee ou craquelee
  - Sifflement ou gargouillement dans le circuit
  - Niveau de liquide qui baisse regulierement
  - Odeur sucree de liquide de refroidissement
  - Plus de 100 000 km ou 8 ans sans remplacement
  good_practices:
  - Controle du niveau de liquide de refroidissement a froid chaque mois
  - Remplacement du liquide selon preconisation constructeur (2-5 ans)
  - Verification des durites et colliers a chaque revision
  - Purge du circuit apres toute intervention sur le refroidissement
rendering:
  pgId: '475'
  intro_title: A quoi sert Durite de refroidissement ?
  risk_title: Pourquoi remplacer Durite de refroidissement a temps ?
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
  - question: Durite OE ou adaptable ?
    answer: Les durites OES (Gates, Contitech) offrent une résistance optimale à la chaleur et à la pression. Les adaptables
      (Febi, Meyle) conviennent pour un usage courant.
  - question: Comment savoir si une durite est à changer ?
    answer: Durite gonflée, craquelée, suintement au niveau des colliers, traces blanches de calcaire séché, durite dure au
      toucher.
  - question: Tous les combien changer les durites ?
    answer: Contrôle visuel tous les 2 ans. Remplacement préventif à 100 000 km ou 8 ans. Plus tôt si traces de fissures.
  - question: Peut-on changer une durite soi-même ?
    answer: Oui, opération accessible. Vidanger le circuit, desserrer les colliers, remplacer par une durite identique. Purger
      le circuit après.
  - question: Quelle erreur éviter avec les durites ?
    answer: Ne pas réutiliser les vieux colliers. Utiliser des colliers neufs adaptés. Vérifier l'absence de pliure après
      montage.
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
doc_id: 1e5d946e-8a92-5fb5-83f2-c49719db56e5
content_hash: sha256:c672b28c18460299
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
  area: Face avant du vehicule (radiateur) et bloc moteur
  access: Par le dessus (capot) ou face avant
  adjacent_parts:
  - radiateur
  - durites
  - pompe a eau
  - thermostat
installation:
  difficulty: moyen
  time: 30min a 2h
  tools:
  - tournevis
  - pince de serrage
  - bac de recuperation
  prerequisite: Moteur froid, circuit vidange avant depose
---

# Durite de refroidissement - Guide Diagnostic Complet

## Fonction et Rôle

Acheminer le liquide de refroidissement entre les elements du circuit

**Actions principales:** acheminer, conduire, relier, transporter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- traces de liquide colore sous le vehicule
- durite visiblement gonflee ou craquelee
- sifflement ou gargouillement dans le circuit
- niveau de liquide qui baisse regulierement
- odeur sucree de liquide de refroidissement
- plus de 100 000 km ou 8 ans sans remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de durite de refroidissement:

1. **Inspection visuelle** - Examiner l'état du durite de refroidissement
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

- pompe-a-eau
- radiateur-de-refroidissement
- sonde-de-refroidissement
- thermostat
- vase-d-expansion
- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon durite de refroidissement, vous devez connaître:

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

**Durite OE ou adaptable ?**
Les durites OES (Gates, Contitech) offrent une résistance optimale à la chaleur et à la pression. Les adaptables (Febi, Meyle) conviennent pour un usage courant.

**Comment savoir si une durite est à changer ?**
Durite gonflée, craquelée, suintement au niveau des colliers, traces blanches de calcaire séché, durite dure au toucher.

**Tous les combien changer les durites ?**
Contrôle visuel tous les 2 ans. Remplacement préventif à 100 000 km ou 8 ans. Plus tôt si traces de fissures.

**Peut-on changer une durite soi-même ?**
Oui, opération accessible. Vidanger le circuit, desserrer les colliers, remplacer par une durite identique. Purger le circuit après.

**Quelle erreur éviter avec les durites ?**
Ne pas réutiliser les vieux colliers. Utiliser des colliers neufs adaptés. Vérifier l'absence de pliure après montage.


## Symptomes supplementaires

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
