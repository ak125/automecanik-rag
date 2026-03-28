---
category: capteurs
slug: sonde-de-refroidissement
title: Sonde de refroidissement
pg_id: 830
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
  role: Mesurer la temperature du liquide de refroidissement et informer le calculateur pour le pilotage moteur
  must_be_true:
  - mesurer
  - detecter
  - transmettre
  must_not_contain:
  - calorstat
  - thermostat
  - pompe a eau
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - alternateur
  - batterie
  - demarreur
  - bougie-d-allumage
  - bobine-d-allumage
  - poulie-d-alternateur
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
  - ❌ "corrige la surchauffe"
  cost_range:
    min: 6
    max: 31
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  brands:
    premium:
    - Bosch
    - Hella
    - Continental VDO
    standard:
    - NTK (NGK)
    - FAE
    - Meat & Doria
    budget:
    - Febi Bilstein
    - Topran
    - Calorstat by Vernet
  quality_tiers:
  - tier: Origine (OE)
    description: Sondes fabriquees par l'equipementier d'origine. Courbe de resistance (CTN) et connecteur identiques a la
      piece constructeur.
  - tier: Qualite equivalente OE (OES)
    description: Equipementiers reconnus en capteurs moteur. Memes specifications electriques, fiabilite comparable.
  - tier: Adaptable de qualite
    description: Marques fiables en entree de gamme. Bien verifier le nombre de broches (2 ou 4) et la forme du connecteur
      avant commande.
diagnostic:
  symptoms:
  - id: S1
    label: Indicateur temperature bloque froid maximum
    severity: immobilisation
  - id: S2
    label: Ventilateur qui tourne en permanence ou jamais
    severity: confort
  - id: S3
    label: Bruit de ventilateur qui s emballe au demarrage
    severity: confort
  - id: S4
    label: Surconsommation et demarrage difficile a froid
    severity: confort
  - id: S5
    label: Odeur de liquide de refroidissement surchauffe
    severity: confort
  - id: S6
    label: Plus de 200 000 km sans controle du circuit
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - remplacement preventif recommande
  depose_steps: []
  quick_checks:
  - 'Observer : indicateur temperature bloque froid maximum ?'
  - 'Observer : ventilateur qui tourne en permanence ou jamais ?'
  - Bruit de ventilateur qui s emballe au demarrage ?
  - 'Comparer la consommation : surconsommation et demarrage difficile a froid ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Indicateur temperature bloque froid maximum
  - Ventilateur qui tourne en permanence ou jamais
  - Bruit de ventilateur qui s emballe au demarrage
  - Surconsommation et demarrage difficile a froid
  - Odeur de liquide de refroidissement surchauffe
  - Plus de 200 000 km sans controle du circuit
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '830'
  intro_title: A quoi sert Sonde de refroidissement ?
  risk_title: Pourquoi remplacer Sonde de refroidissement a temps ?
  risk_explanation: '**Pièce HS** - Le sonde de refroidissement peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le sonde de refroidissement peut être hors service et nécessiter un remplacement'
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
  - question: Sonde de température OE ou adaptable ?
    answer: Les adaptables (Febi, FAE, NTK) fonctionnent bien. Vérifiez la courbe de résistance (CTN) et le nombre de broches
      (2 ou 4).
  - question: Comment savoir si ma sonde de température est HS ?
    answer: Indicateur bloqué à froid ou à chaud, ventilateur qui tourne en permanence, surconsommation, difficultés de démarrage
      à froid.
  - question: Tous les combien changer la sonde de température ?
    answer: Pas de périodicité. Pièce simple qui dure généralement 200 000+ km. À remplacer si valeurs incohérentes.
  - question: Peut-on changer la sonde de température soi-même ?
    answer: Oui, mais attention à la perte de liquide de refroidissement. Prévoir de compléter et purger le circuit après.
  - question: Quelle erreur éviter avec la sonde de température ?
    answer: Ne pas confondre sonde calculateur et sonde indicateur. Identifier laquelle est défaillante (diagnostic OBD).
      Purger le circuit après.
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
doc_id: 88def317-322d-56bf-96dd-63594c701dd0
content_hash: sha256:89476c9aed24f8f9
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

# Sonde de refroidissement - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la temperature du liquide de refroidissement et informer le calculateur pour le pilotage moteur

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Indicateur temperature bloque froid maximum**
  indicateur temperature bloque froid maximum

### 🟢 Autres Symptômes

- ventilateur qui tourne en permanence ou jamais
- bruit de ventilateur qui s emballe au demarrage
- surconsommation et demarrage difficile a froid
- odeur de liquide de refroidissement surchauffe
- plus de 200 000 km sans controle du circuit

## Procédure de Diagnostic

Pour diagnostiquer un problème de sonde de refroidissement:

1. **Inspection visuelle** - Examiner l'état du sonde de refroidissement
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le sonde de refroidissement peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- pompe-a-eau
- radiateur-de-refroidissement
- thermostat
- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon sonde de refroidissement, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "corrige la surchauffe"

## FAQ

**Sonde de température OE ou adaptable ?**
Les adaptables (Febi, FAE, NTK) fonctionnent bien. Vérifiez la courbe de résistance (CTN) et le nombre de broches (2 ou 4).

**Comment savoir si ma sonde de température est HS ?**
Indicateur bloqué à froid ou à chaud, ventilateur qui tourne en permanence, surconsommation, difficultés de démarrage à froid.

**Tous les combien changer la sonde de température ?**
Pas de périodicité. Pièce simple qui dure généralement 200 000+ km. À remplacer si valeurs incohérentes.

**Peut-on changer la sonde de température soi-même ?**
Oui, mais attention à la perte de liquide de refroidissement. Prévoir de compléter et purger le circuit après.

**Quelle erreur éviter avec la sonde de température ?**
Ne pas confondre sonde calculateur et sonde indicateur. Identifier laquelle est défaillante (diagnostic OBD). Purger le circuit après.


## Symptomes supplementaires

<!-- materialized-from-db diagnostic/temoins-tableau-bord.md 2026-01-01 -->
### Diagnostic - Témoins tableau de bord

# Témoins tableau de bord - Guide complet

## Témoins critiques (ARRÊT IMMÉDIAT)

### Témoin huile moteur (rouge)
- **Signification** : Pression d'huile insuffisante
- **Action** : ARRÊT IMMÉDIAT du véhicule
- **Causes** : Niveau bas, pompe à huile, fuite
- **Risque** : Casse moteur
- **Vérification** : Niveau d'huile à la jauge

### Témoin température moteur (rouge)
- **Signification** : Surchauffe moteur
- **Action** : ARRÊT IMMÉDIAT, laisser refroidir
- **Causes** : Liquide refroidissement, thermostat, ventilateur
- **Risque** : Joint de culasse, casse moteur

### Témoin frein (rouge)
- **Signification** : Niveau liquide frein bas ou frein à main
- **Action** : Vérifier frein à main, puis niveau liquide
- **Causes** : Fuite, usure plaquettes extrême
- **Risque** : Perte de freinage

### Témoin batterie (rouge)
- **Signification** : Charge batterie insuffisante
- **Action** : Rejoindre un garage rapidement
- **Causes** : Alternateur, courroie, batterie HS
- **Risque** : Panne complète

## Témoins importants (attention requise)

### Témoin ABS (orange)
- **Signification** : Système ABS désactivé
- **Action** : Contrôle recommandé
- **Causes** : Capteur ABS, bloc hydraulique
- **Impact** : Freinage normal mais sans assistance ABS
- **Pièces** : Capteur ABS, bloc ABS

### Témoin ESP/ASR (orange)
- **Signification** : Antipatinage/stabilité désactivé
- **Action** : Conduire prudemment
- **Causes** : Capteur, calculateur

### Témoin airbag (orange)
- **Signification** : Système airbag défaillant
- **Action** : Contrôle obligatoire
- **Risque** : Non-déclenchement en cas d'accident
- **Pièces** : Contacteur tournant, capteur airbag

### Témoin moteur (orange - check engine)
- **Signification** : Anomalie gestion moteur
- **Action** : Diagnostic OBD recommandé
- **Causes multiples** : Capteur O2, catalyseur, allumage
- **Impact** : Surconsommation, pollution

### Témoin FAP/DPF (orange - diesel)
- **Signification** : Filtre à particules saturé
- **Action** : Rouler 20min sur autoroute (régénération)
- **Causes** : Trajets courts répétés
- **Pièces** : FAP, nettoyage, additif

## Témoins d'information

### Témoin préchauffage (diesel)
- **Signification** : Préchauffage des bougies en cours
- **Action** : Attendre extinction avant démarrage
- **Normal** : S'éteint après quelques secondes

### Témoin clignotant
- **Signification** : Clignotant actif
- **Anomalie si** : Clignote rapidement = ampoule grillée

### Témoin feux de route
- **Signification** : Pleins phares activés

### Témoin antibrouillard
- **Signification** : Feux de brouillard actifs

## Codes couleur

| Couleur | Signification | Action |
|---------|---------------|--------|
| **Rouge** | Danger immédiat | Arrêt véhicule |
| **Orange** | Attention | Contrôle rapide |
| **Vert/Bleu** | Information | Aucune |

## Diagnostic OBD-II

Pour les témoins moteur, un diagnostic OBD permet de lire les codes défaut :
- **P0xxx** : Groupe motopropulseur
- **B0xxx** : Carrosserie
- **C0xxx** : Châssis
- **U0xxx** : Réseau/Communication

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
