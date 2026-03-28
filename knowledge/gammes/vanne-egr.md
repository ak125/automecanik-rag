---
category: alimentation
slug: vanne-egr
title: Vanne EGR
pg_id: 1145
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-26'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v4_converted
  last_enriched_by: script:materialize-db-to-md
  last_enriched_at: '2026-03-26'
domain:
  role: Recycler une partie des gaz d'echappement vers l'admission pour reduire les emissions de NOx
  must_be_true:
  - recycler
  - ouvrir
  - fermer
  must_not_contain:
  - carburant
  - injection
  - injecteur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - catalyseur
  - fap
  - silencieux
  - sonde-lambda
  - tube-d-echappement
  - collecteur-d-echappement
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
  - ❌ "nettoie le moteur"
  cost_range:
    min: 63
    max: 469
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    description: Vanne identique au premier montage constructeur. Débit, course du clapet et connectique conformes aux paramètres
      du calculateur moteur.
  - tier: Équivalent OE (OES)
    description: Fabricants comme Valeo, Pierburg ou Delphi fournissent les vannes EGR aux constructeurs en première monte.
      Même qualité, même débit, même connectique.
  - tier: Adaptable (aftermarket)
    description: Vannes aftermarket compatibles. Vérifier le type (pneumatique ou électrique), le connecteur et le nombre
      de broches avant commande.
  brands:
    premium:
    - Walker
    - Bosal
    standard:
    - Valeo
    - Febi
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Perte de puissance a bas et moyen regime
    severity: confort
  - id: S2
    label: Fumee noire a l acceleration
    severity: confort
  - id: S3
    label: Ralenti irregulier ou moteur qui broute
    severity: confort
  - id: S4
    label: Voyant moteur allume codes p0400-p0409
    severity: confort
  - id: S5
    label: A-coups a bas regime
    severity: confort
  - id: S6
    label: Plus de 80 000 km sans nettoyage diesel
    severity: confort
  causes:
  - lecture codes defaut obd et diagnostic electronique
  - remplacement preventif recommande
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  - 'kilometrage eleve ou usure visible : remplacement preventif recommande'
  quick_checks:
  - 'Observer : perte de puissance a bas et moyen regime ?'
  - 'Observer : fumee noire a l acceleration ?'
  - 'Observer : ralenti irregulier ou moteur qui broute ?'
  - Voyant moteur allume codes p0400-p0409 ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Perte de puissance a bas et moyen regime
  - Fumee noire a l acceleration
  - Ralenti irregulier ou moteur qui broute
  - Voyant moteur allume codes p0400-p0409
  - A-coups a bas regime
  - Plus de 80 000 km sans nettoyage diesel
  good_practices:
  - Controle visuel sous le vehicule a chaque revision
  - Verifier les fixations et silent-blocs de suspension d echappement
  - Remplacement si perforation, rouille traversante ou bruit anormal
  - Ne pas conduire avec un echappement defectueux (gaz toxiques)
rendering:
  pgId: '1145'
  intro_title: A quoi sert Vanne EGR ?
  risk_title: Pourquoi remplacer Vanne EGR a temps ?
  risk_explanation: '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
  risk_consequences:
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
  - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
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
  - question: Vanne EGR OE ou adaptable ?
    answer: Les vannes OES (Valeo, Pierburg, Delphi) sont recommandées. Une vanne de qualité inférieure s'encrassera plus
      vite et pourra avoir un débit incorrect.
  - question: Comment savoir si ma vanne EGR est HS ?
    answer: Perte de puissance, fumée noire, voyant moteur allumé, ralenti irrégulier, à-coups à bas régime, mode dégradé
      possible.
  - question: Tous les combien nettoyer la vanne EGR ?
    answer: 'Nettoyage recommandé tous les 60 000 km sur diesel. Plus souvent si petits trajets urbains. Essence : moins critique.'
  - question: Peut-on nettoyer la vanne EGR soi-même ?
    answer: Oui, avec un nettoyant spécifique EGR. Démonter la vanne, tremper ou pulvériser, nettoyer les conduits. Compter
      1 à 2 heures.
  - question: Quelle erreur éviter avec la vanne EGR ?
    answer: Ne pas supprimer l'EGR (illégal et risque de surconsommation). Ne pas oublier de nettoyer aussi le collecteur
      d'admission encrassé.
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
doc_id: b44d8e1b-e7b2-5300-94af-6058ba627a6e
content_hash: sha256:5c21b0da84984d7d
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
  area: Sous le vehicule, du collecteur moteur au silencieux arriere
  access: Par le dessous (pont elevateur)
  adjacent_parts:
  - collecteur
  - catalyseur
  - tubes
  - silencieux
installation:
  difficulty: moyen
  time: 1h a 2h
  tools:
  - cle a douille
  - degripant
  - chandelles
  prerequisite: Pont elevateur, fixations souvent grippees par la rouille
---

# Vanne EGR - Guide Diagnostic Complet

## Fonction et Rôle

Recycler une partie des gaz d'echappement vers l'admission pour reduire les emissions de NOx

**Actions principales:** recycler, ouvrir, fermer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- perte de puissance a bas et moyen regime
- fumee noire a l acceleration
- ralenti irregulier ou moteur qui broute
- voyant moteur allume codes p0400-p0409
- a-coups a bas regime
- plus de 80 000 km sans nettoyage diesel

## Procédure de Diagnostic

Pour diagnostiquer un problème de vanne egr:

1. **Inspection visuelle** - Examiner l'état du vanne egr
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- catalyseur
- fap
- injecteur
- turbo

## Critères de Compatibilité

Pour commander le bon vanne egr, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "nettoie le moteur"

## FAQ

**Vanne EGR OE ou adaptable ?**
Les vannes OES (Valeo, Pierburg, Delphi) sont recommandées. Une vanne de qualité inférieure s'encrassera plus vite et pourra avoir un débit incorrect.

**Comment savoir si ma vanne EGR est HS ?**
Perte de puissance, fumée noire, voyant moteur allumé, ralenti irrégulier, à-coups à bas régime, mode dégradé possible.

**Tous les combien nettoyer la vanne EGR ?**
Nettoyage recommandé tous les 60 000 km sur diesel. Plus souvent si petits trajets urbains. Essence : moins critique.

**Peut-on nettoyer la vanne EGR soi-même ?**
Oui, avec un nettoyant spécifique EGR. Démonter la vanne, tremper ou pulvériser, nettoyer les conduits. Compter 1 à 2 heures.

**Quelle erreur éviter avec la vanne EGR ?**
Ne pas supprimer l'EGR (illégal et risque de surconsommation). Ne pas oublier de nettoyer aussi le collecteur d'admission encrassé.
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
## Bruits d'échappement

### Bruit métallique sous la voiture
- **Catalyseur décollé** : Le substrat céramique interne s'est fragmenté et vibre dans le boîtier. Bruit de ferraille au ralenti.
- **Silencieux percé** : Corrosion ayant percé le pot d'échappement. Bruit de souffle ou grondement.
- **Flexible d'échappement fissuré** : Joint de raccord entre le collecteur et la ligne d'échappement. Bruit de fuite.
- **Collier ou bride desserré** : Claquement rythmique, plus audible au ralenti.

### Sifflement
- **Fuite au collecteur** : Joint de collecteur d'échappement brûlé. Sifflement aigu surtout à froid, qui peut s'atténuer à chaud.
- **Fissure sur le tube** : Soudure fatiguée ou corrosion localisée.

## Fumées anormales

### Fumée blanche épaisse
- **Joint de culasse défaillant** : Liquide de refroidissement entre dans la chambre de combustion. Fumée blanche sucrée, persistante même moteur chaud. Vérifier le niveau de liquide de refroidissement.

### Fumée noire
- **Mélange trop riche** : Injecteurs qui fuient, capteur MAP/MAF défaillant, filtre à air colmaté.
- **Turbo défaillant** : Fuite d'huile dans l'admission via les joints du turbo.

### Fumée bleue
- **Consommation d'huile** : Segments usés, guides de soupapes usés, ou joint de queue de soupape. L'huile brûle dans la chambre de combustion.

## Catalyseur et FAP

- **Catalyseur colmaté** : Perte de puissance, moteur qui étouffe à l'accélération, voyant moteur allumé (codes P0420/P0430).
- **Filtre à particules bouché** : Voyant FAP allumé, régénérations trop fréquentes, perte de puissance. Fréquent sur les trajets courts en ville.
- **Sonde lambda défaillante** : Consommation en hausse, voyant moteur, mélange air/carburant mal régulé.

## Quand consulter un professionnel

- Fumée blanche persistante moteur chaud (risque joint de culasse)
- Voyant moteur + perte de puissance (catalyseur/FAP)
- Odeur d'œuf pourri (catalyseur en surchauffe)
- Bruit d'échappement fort + odeur de gaz dans l'habitacle


## References supplementaires

<!-- materialized-from-db manual/02f258d16d9c 2026-03-26 -->
### Conduit de recirculation des gaz d'échappement (EGR)

Dépollution
Conduit de recirculation des gaz d'échappement (EGR)

Notre conduit transfère les gaz d'échappement après le turbocompresseur vers l'admission d'air avant le turbocompresseur.

Principaux bénéfices
Résistance chimique et thermique
Mélange de caoutchouc réalisé en interne
Caractéristiques techniques
Description

Assemblage de tuyaux en caoutchouc avec ou sans renforts annulaires, avant et après le refroidisseur EGR.

Informations fonctionnelles
Résistance à 230 °C
Résistance chimique aux gaz d'échappement
Technologies
Technologie enveloppée
Tuyaux ondulés
Bénéfices
Amélioration des performances
Résistance aux fortes pressions
Fiabilité

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

<!-- materialized-from-db diagnostic/echappement-catalyseur.md 2026-02-15 -->
### Diagnostic - Échappement et catalyseur

# Échappement et catalyseur - Diagnostic complet

## Bruits d'échappement

### Bruit métallique sous la voiture
- **Catalyseur décollé** : Le substrat céramique interne s'est fragmenté et vibre dans le boîtier. Bruit de ferraille au ralenti.
- **Silencieux percé** : Corrosion ayant percé le pot d'échappement. Bruit de souffle ou grondement.
- **Flexible d'échappement fissuré** : Joint de raccord entre le collecteur et la ligne d'échappement. Bruit de fuite.
- **Collier ou bride desserré** : Claquement rythmique, plus audible au ralenti.

### Sifflement
- **Fuite au collecteur** : Joint de collecteur d'échappement brûlé. Sifflement aigu surtout à froid, qui peut s'atténuer à chaud.
- **Fissure sur le tube** : Soudure fatiguée ou corrosion localisée.

## Fumées anormales

### Fumée blanche épaisse
- **Joint de culasse défaillant** : Liquide de refroidissement entre dans la chambre de combustion. Fumée blanche sucrée, persistante même moteur chaud. Vérifier le niveau de liquide de refroidissement.

### Fumée noire
- **Mélange trop riche** : Injecteurs qui fuient, capteur MAP/MAF défaillant, filtre à air colmaté.
- **Turbo défaillant** : Fuite d'huile dans l'admission via les joints du turbo.

### Fumée bleue
- **Consommation d'huile** : Segments usés, guides de soupapes usés, ou joint de queue de soupape. L'huile brûle dans la chambre de combustion.

## Catalyseur et FAP

- **Catalyseur colmaté** : Perte de puissance, moteur qui étouffe à l'accélération, voyant moteur allumé (codes P0420/P0430).
- **Filtre à particules bouché** : Voyant FAP allumé, régénérations trop fréquentes, perte de puissance. Fréquent sur les trajets courts en ville.
- **Sonde lambda défaillante** : Consommation en hausse, voyant moteur, mélange air/carburant mal régulé.

## Quand consulter un professionnel

- Fumée blanche persistante moteur chaud (risque joint de culasse)
- Voyant moteur + perte de puissance (catalyseur/FAP)
- Odeur d'œuf pourri (catalyseur en surchauffe)
- Bruit d'échappement fort + odeur de gaz dans l'habitacle
