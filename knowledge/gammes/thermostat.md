---
category: refroidissement
slug: thermostat
title: Thermostat
pg_id: 316
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
  role: Reguler le flux de liquide de refroidissement selon la temperature moteur
  must_be_true:
  - reguler
  - ouvrir
  - fermer
  must_not_contain:
  - sonde
  - capteur
  - electronique
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - radiateur-de-refroidissement
  - pompe-a-eau
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
    min: 3
    max: 59
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  brands:
    premium:
    - Wahler
    - Behr (Mahle)
    - Gates
    standard:
    - Calorstat (Vernet)
    - Thermostat (Continental)
    - Dayco
    budget:
    - Febi Bilstein
    - Meyle
    - Topran
  quality_tiers:
  - tier: Origine constructeur
    description: Thermostats d origine avec temperature d ouverture et course calibrees pour le moteur. Joint de boitier inclus
      selon les references.
  - tier: Equipementier qualite OE
    description: Thermostats premiere monte avec temperature d ouverture precise et capsule de cire de qualite. Plage de tolerance
      etroite.
  - tier: Adaptable qualite reconnue
    description: Thermostats compatibles avec verification de la temperature d ouverture nominale et du diametre avant montage.
diagnostic:
  symptoms:
  - id: S1
    label: Aiguille de temperature dans le rouge rapidement
    severity: confort
  - id: S2
    label: Moteur qui ne chauffe jamais aiguille basse
    severity: confort
  - id: S3
    label: Sifflement ou vapeur s echappant du capot
    severity: confort
  - id: S4
    label: Chauffage qui reste froid tres longtemps
    severity: confort
  - id: S5
    label: Odeur de liquide de refroidissement en surchauffe
    severity: confort
  - id: S6
    label: Plus de 100 000 km sans remplacement
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - remplacement preventif recommande
  quick_checks:
  - 'Observer : aiguille de temperature dans le rouge rapidement ?'
  - 'Observer : moteur qui ne chauffe jamais aiguille basse ?'
  - 'Observer : sifflement ou vapeur s echappant du capot ?'
  - 'Observer : chauffage qui reste froid tres longtemps ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Aiguille de temperature dans le rouge rapidement
  - Moteur qui ne chauffe jamais aiguille basse
  - Sifflement ou vapeur s echappant du capot
  - Chauffage qui reste froid tres longtemps
  - Odeur de liquide de refroidissement en surchauffe
  - Plus de 100 000 km sans remplacement
  good_practices:
  - Controle du niveau de liquide de refroidissement a froid chaque mois
  - Remplacement du liquide selon preconisation constructeur (2-5 ans)
  - Verification des durites et colliers a chaque revision
  - Purge du circuit apres toute intervention sur le refroidissement
rendering:
  pgId: '316'
  intro_title: A quoi sert Thermostat ?
  risk_title: Pourquoi remplacer Thermostat a temps ?
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
  - question: Thermostat OE ou adaptable ?
    answer: Les thermostats OES (Wahler, Behr, Gates) garantissent une température d'ouverture précise. Les adaptables peuvent
      avoir une plage d'ouverture moins fiable.
  - question: Comment savoir si mon thermostat est HS ?
    answer: Surchauffe rapide (bloqué fermé), moteur qui ne chauffe pas (bloqué ouvert), chauffage froid, surconsommation
      de carburant.
  - question: Tous les combien changer le thermostat ?
    answer: Remplacement préventif conseillé à 100 000 km. Changez-le systématiquement lors d'une intervention sur le circuit
      de refroidissement.
  - question: Peut-on changer le thermostat soi-même ?
    answer: Oui, opération accessible sur la plupart des véhicules. Vidange partielle, dépose du boîtier, remplacement du
      joint. Purge obligatoire.
  - question: Quelle erreur éviter avec le thermostat ?
    answer: Ne pas oublier le joint de boîtier. Respecter le sens de montage (pointeau vers le moteur). Bien purger le circuit
      après.
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
doc_id: b7fe6110-0f53-5587-bb5d-b32380d0a27a
content_hash: sha256:a5fd9278e32d508b
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

# Thermostat - Guide Diagnostic Complet

## Fonction et Rôle

Reguler le flux de liquide de refroidissement selon la temperature moteur

**Actions principales:** reguler, ouvrir, fermer, controler le flux

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- aiguille de temperature dans le rouge rapidement
- moteur qui ne chauffe jamais aiguille basse
- sifflement ou vapeur s echappant du capot
- chauffage qui reste froid tres longtemps
- odeur de liquide de refroidissement en surchauffe
- plus de 100 000 km sans remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de thermostat:

1. **Inspection visuelle** - Examiner l'état du thermostat
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

- durite-de-refroidissement
- pompe-a-eau
- radiateur-de-refroidissement
- sonde-de-refroidissement
- vase-d-expansion
- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon thermostat, vous devez connaître:

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

**Thermostat OE ou adaptable ?**
Les thermostats OES (Wahler, Behr, Gates) garantissent une température d'ouverture précise. Les adaptables peuvent avoir une plage d'ouverture moins fiable.

**Comment savoir si mon thermostat est HS ?**
Surchauffe rapide (bloqué fermé), moteur qui ne chauffe pas (bloqué ouvert), chauffage froid, surconsommation de carburant.

**Tous les combien changer le thermostat ?**
Remplacement préventif conseillé à 100 000 km. Changez-le systématiquement lors d'une intervention sur le circuit de refroidissement.

**Peut-on changer le thermostat soi-même ?**
Oui, opération accessible sur la plupart des véhicules. Vidange partielle, dépose du boîtier, remplacement du joint. Purge obligatoire.

**Quelle erreur éviter avec le thermostat ?**
Ne pas oublier le joint de boîtier. Respecter le sens de montage (pointeau vers le moteur). Bien purger le circuit après.


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
