---
category: refroidissement
slug: radiateur-de-refroidissement
title: Radiateur de refroidissement
pg_id: 470
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
  role: Dissiper la chaleur du liquide de refroidissement vers l'air exterieur
  must_be_true:
  - dissiper
  - echanger
  - refroidir
  must_not_contain:
  - chauffage
  - habitacle
  - huile
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - pompe-a-eau
  - thermostat
  - durite-de-refroidissement
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
    min: 62
    max: 218
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE (OES)
  - tier: Adaptable qualite
  - tier: Reconditionne
  - tier: Echange standard
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
    label: Flaque de liquide colore sous l avant
    severity: confort
  - id: S2
    label: Traces de corrosion sur les tubes du radiateur
    severity: confort
  - id: S3
    label: Sifflement d air ou de vapeur a l avant
    severity: confort
  - id: S4
    label: Surchauffe au ralenti ou en embouteillage
    severity: confort
  - id: S5
    label: Odeur de liquide de refroidissement chaud
    severity: confort
  - id: S6
    label: Radiateur visiblement deforme ou perce
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  depose_steps: []
  quick_checks:
  - 'Observer : flaque de liquide colore sous l avant ?'
  - 'Observer : traces de corrosion sur les tubes du radiateur ?'
  - 'Observer : sifflement d air ou de vapeur a l avant ?'
  - 'Observer : surchauffe au ralenti ou en embouteillage ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Flaque de liquide colore sous l avant
  - Traces de corrosion sur les tubes du radiateur
  - Sifflement d air ou de vapeur a l avant
  - Surchauffe au ralenti ou en embouteillage
  - Odeur de liquide de refroidissement chaud
  - Radiateur visiblement deforme ou perce
  good_practices:
  - Controle du niveau de liquide de refroidissement a froid chaque mois
  - Remplacement du liquide selon preconisation constructeur (2-5 ans)
  - Verification des durites et colliers a chaque revision
  - Purge du circuit apres toute intervention sur le refroidissement
rendering:
  pgId: '470'
  intro_title: A quoi sert Radiateur de refroidissement ?
  risk_title: Pourquoi remplacer Radiateur de refroidissement a temps ?
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
  - question: Radiateur OE ou adaptable ?
    answer: Les radiateurs OES (Valeo, Behr/Mahle, Nissens) garantissent un refroidissement optimal. Les adaptables moins
      chers peuvent avoir un rendement inférieur.
  - question: Comment savoir si mon radiateur fuit ?
    answer: Flaque de liquide sous l'avant du véhicule, niveau qui baisse, traces vertes/roses sur le radiateur, surchauffe
      au ralenti prolongé.
  - question: Tous les combien changer le radiateur ?
    answer: Pas de périodicité. À remplacer si fuite, si bouché (surchauffe) ou si endommagé par un choc.
  - question: Peut-on réparer un radiateur percé ?
    answer: Une réparation provisoire (résine, soudure) est possible mais temporaire. Le remplacement reste la solution fiable.
  - question: Quelle erreur éviter avec le radiateur ?
    answer: Ne pas monter un radiateur sans remplacer le liquide de refroidissement. Vérifier l'état des supports et des durites
      adjacentes.
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
doc_id: 6992b1dd-582f-5d32-86f7-fb08e7ea8f3a
content_hash: sha256:ad6ca200cdbb9f3a
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

# Radiateur de refroidissement - Guide Diagnostic Complet

## Fonction et Rôle

Dissiper la chaleur du liquide de refroidissement vers l'air exterieur

**Actions principales:** dissiper, echanger, refroidir, evacuer la chaleur

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- flaque de liquide colore sous l avant
- traces de corrosion sur les tubes du radiateur
- sifflement d air ou de vapeur a l avant
- surchauffe au ralenti ou en embouteillage
- odeur de liquide de refroidissement chaud
- radiateur visiblement deforme ou perce

## Procédure de Diagnostic

Pour diagnostiquer un problème de radiateur de refroidissement:

1. **Inspection visuelle** - Examiner l'état du radiateur de refroidissement
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

- bouchon-de-radiateur
- durite-de-refroidissement
- pompe-a-eau
- radiateur-de-chauffage
- sonde-de-refroidissement
- thermostat
- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon radiateur de refroidissement, vous devez connaître:

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

**Radiateur OE ou adaptable ?**
Les radiateurs OES (Valeo, Behr/Mahle, Nissens) garantissent un refroidissement optimal. Les adaptables moins chers peuvent avoir un rendement inférieur.

**Comment savoir si mon radiateur fuit ?**
Flaque de liquide sous l'avant du véhicule, niveau qui baisse, traces vertes/roses sur le radiateur, surchauffe au ralenti prolongé.

**Tous les combien changer le radiateur ?**
Pas de périodicité. À remplacer si fuite, si bouché (surchauffe) ou si endommagé par un choc.

**Peut-on réparer un radiateur percé ?**
Une réparation provisoire (résine, soudure) est possible mais temporaire. Le remplacement reste la solution fiable.

**Quelle erreur éviter avec le radiateur ?**
Ne pas monter un radiateur sans remplacer le liquide de refroidissement. Vérifier l'état des supports et des durites adjacentes.


## References supplementaires

<!-- materialized-from-db guides/identifier-panne-auto.md 2026-02-21 -->
### Guide - Comment identifier une panne auto : methodes, signes et urgences

# Comment identifier une panne auto : guide complet

## Pourquoi identifier soi-meme sa panne ?

Un diagnostic precoce permet d'eviter une panne totale, de reduire le cout de reparation et d'arriver chez le garagiste avec une hypothese claire. 80% des pannes presentent des signes avant-coureurs pendant plusieurs semaines avant l'immobilisation.

## Les 3 methodes pour identifier une panne auto

### 1. Observer les symptomes sensoriels (sans outil)

Chaque organe du vehicule communique par un canal sensoriel distinct :

| Canal | Exemples | Zone probable |
|-------|----------|---------------|
| Auditif | Sifflement, claquement, grincement | Freinage, suspension, moteur |
| Visuel | Fumee, voyant, fuite | Moteur, circuit de refroidissement, freins |
| Tactile | Vibration, a-coup, pedale molle | Suspension, embrayage, freinage |
| Olfactif | Odeur de brule, de caoutchouc | Embrayage, freins, circuit electrique |

### 2. Lire les voyants du tableau de bord

Les voyants sont le premier niveau de diagnostic embarque. Leur couleur indique l'urgence :
- Rouge : arret immediat obligatoire (huile, temperature, frein)
- Orange : attention requise rapidement (moteur, ABS, FAP)
- Jaune/vert : information (entretien, assistance parking)

Un voyant orange moteur (check engine) indique une anomalie enregistree dans le calculateur. La lecture des codes OBD avec un scanner (protocole OBD2 depuis 2001) permet d'identifier le defaut exact.

### 3. Scanner le code OBD (P, C, B, U)

Les codes OBD se lisent avec un scanner OBD2 (disponibles a partir de 30 EUR) :
- P0xxx : moteur et transmission
- C0xxx : chassis (ABS, ESP)
- B0xxx : carrosserie (airbags, sieges)
- U0xxx : reseau de communication

## Les 10 signes avant-coureurs d'une panne

1. **Bruit inhabituel au freinage** — sifflement aigu = plaquettes usees, grincement = disques ou etrier
2. **Voyant moteur allume** — code OBD a lire dans les 48h
3. **Vibration au volant** — a vitesse constante : pneumatiques ; au freinage : disques voiles
4. **Demarrage difficile** — lent, bruyant ou manque = batterie, demarreur ou alternateur
5. **Surconsommation soudaine** — injecteurs, bougie, fuite circuit d'alimentation
6. **Fumee a l'echappement** — blanche = liquide de refroidissement ; noire = richesse essence ; bleue = huile
7. **Perte de puissance** — turbo, FAP obstrue, injecteurs defaillants
8. **Odeur de brule** — embrayage en patinage, frein grippe, court-circuit electrique
9. **Pedale de frein molle** — fuite liquide de frein, plaquettes usees extremes
10. **Voyant ABS ou ESP** — capteur de roue, bloc hydraulique

## Panne mecanique vs electrique : comment distinguer

| Critere | Mecanique | Electrique |
|---------|-----------|------------|
| Manifestation | Progressive, sonore, vibratoire | Soudaine, voyant allume |
| Temperature | Souvent liee a la montee en temperature | Independante |
| Diagnostic | Inspection visuelle, ecoute | Scanner OBD indispensable |
| Exemples | Usure plaquettes, joint HS, courroie | Capteur O2, calculateur, alternateur |

## Que faire en cas de panne sur autoroute ?

**Priorite absolue : securiser le vehicule et les occupants.**

1. Allumer les feux de detresse immediatement
2. Se garer sur la bande d'arret d'urgence (BAU), le plus a droite possible
3. Couper le moteur et serrer le frein a main
4. Sortir du vehicule par la droite et s'eloigner de la glissiere
5. Revetir le gilet de securite (obligatoire)
6. Poser le triangle de signalisation a 150m minimum (si possible sans danger)
7. Appeler le 3477 (societe d'autoroute) depuis une borne d'appel orange ou votre telephone

**Ne jamais tenter de reparer sur la BAU.** Appelez le prestataire agree de l'autoroute.

## FAQ : Identifier sa panne auto

### Comment savoir quel est le probleme de ma voiture ?
Commencez par observer les symptomes : voyants allumes, bruits, vibrations, odeurs. Si un voyant moteur est allume, lisez le code OBD avec un scanner. Pour les pannes sans voyant, decrivez le symptome (canal sensoriel + moment d'apparition) dans notre outil de diagnostic.

### Comment identifier une panne de demarreur ?
Un demarreur defaillant se manifeste par un clic unique sans demarrage (relais de demarrage), un grincement de courte duree, ou une absence totale de reaction moteur alors que la batterie est chargee. Le diagnostic se confirme en mesurant la tension aux bornes du demarreur lors de la sollicitation.

### Qu'est-ce qu'une panne voyant ABS ?
Le voyant ABS orange indique une defaillance du systeme antiblocage. Le freinage normal reste fonctionnel mais l'assistance ABS est desactivee. Cause la plus frequente : capteur ABS de roue defaillant (50-80 EUR la piece). Ne pas ignorer : rouler sans ABS est legalement autorise mais deconseille.

### Comment lire un code panne voiture ?
Branchez un scanner OBD2 sur le port OBD situe sous le tableau de bord (cote conducteur, generalement sous la colonne de direction). Selectionnez "Lire les codes defaut". Le code P0xxx s'interprete via notre outil ou des bases specialisees. Effacez le code seulement apres reparation.

### Voiture en panne qui ne demarre pas : par ou commencer ?
Verifiez dans cet ordre : 1) Batterie (tension > 12.4V), 2) Demarreur (bruit de clic = OK cote relais), 3) Bobines et bougies (si moteur tourne mais cale), 4) Circuit d'alimentation (pompe a carburant). Un diagnostic OBD indique souvent la piste exacte.

### Panne mecanique ou electrique : comment savoir ?
Une panne mecanique est generalement progressive et s'accompagne de bruits ou vibrations. Une panne electrique est souvent soudaine avec voyant allume. L'outil de diagnostic OBD lit les defauts electroniques ; une inspection physique confirme les pannes mecaniques.

### Que faire si un voyant rouge s'allume en conduisant ?
Un voyant rouge impose l'arret immediat securise du vehicule (huile moteur, temperature moteur, frein). Garez-vous des que possible en securite, coupez le moteur, et n'attendez pas que la situation empire. Relancer un moteur surchauffe ou en manque de pression d'huile cause des dommages irreversibles.

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
