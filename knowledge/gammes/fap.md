---
category: echappement
slug: fap
title: FAP
pg_id: 1256
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
  last_enriched_by: script:rag-fill-remaining-gaps
  last_enriched_at: '2026-03-28'
domain:
  role: Filtre et retient les particules fines des gaz d'échappement diesel
  must_be_true:
  - filtrer
  - retenir
  - regenerer
  must_not_contain:
  - catalyseur
  - pot catalytique
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - catalyseur
  - silencieux
  - sonde-lambda
  - vanne-egr
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
  - ❌ "passe le controle technique"
  cost_range:
    min: 150
    max: 800
    currency: EUR
    unit: l'unite
    source: estimation categorie
  quality_tiers:
  - tier: Pièce OE (Origine Équipement)
    description: FAP identique à l origine. Homologation moteur et normes anti-pollution conformes. Capteur de pression différentielle
      compatible.
  - tier: Équivalent OE (spécialistes échappement)
    description: Fabricants d échappement et de filtration reconnus fournissant les constructeurs. Qualité proche de l OE.
  - tier: FAP régénéré / décalaminé
    description: Nettoyage chimique ou thermique du FAP d origine. Efficace si le filtre n est pas trop colmaté ou endommagé.
      Option économique (150 à 300 EUR) avant de passer au remplacement.
  - tier: FAP générique non homologué
    description: Non recommandé. Un FAP non homologué peut affecter la régénération et le comportement du moteur. Risque de
      non-conformité au contrôle technique.
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
    label: Voyant filtre particules allume tableau
    severity: confort
  - id: S2
    label: Perte de puissance importante mode degrade
    severity: confort
  - id: S3
    label: Regenerations frequentes odeur de brule
    severity: confort
  - id: S4
    label: Fumee noire excessive a l acceleration
    severity: confort
  - id: S5
    label: Surconsommation de carburant anormale
    severity: confort
  - id: S6
    label: Plus de 150 000 km en conduite urbaine
    severity: confort
  causes:
  - lecture codes defaut obd et diagnostic electronique
  - remplacement preventif recommande
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  - 'kilometrage eleve ou usure visible : remplacement preventif recommande'
  quick_checks:
  - Voyant filtre particules allume tableau ?
  - 'Observer : perte de puissance importante mode degrade ?'
  - 'Observer : regenerations frequentes odeur de brule ?'
  - 'Observer : fumee noire excessive a l acceleration ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Voyant filtre particules allume tableau
  - Perte de puissance importante mode degrade
  - Regenerations frequentes odeur de brule
  - Fumee noire excessive a l acceleration
  - Surconsommation de carburant anormale
  - Plus de 150 000 km en conduite urbaine
  good_practices:
  - Controle visuel sous le vehicule a chaque revision
  - Verifier les fixations et silent-blocs de suspension d echappement
  - Remplacement si perforation, rouille traversante ou bruit anormal
  - Ne pas conduire avec un echappement defectueux (gaz toxiques)
rendering:
  pgId: '1256'
  intro_title: A quoi sert FAP ?
  risk_title: Pourquoi remplacer FAP a temps ?
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
  - question: 'FAP OE ou OES : que choisir ?'
    answer: Les FAP OES (Bosal, Walker) sont de qualité équivalente à l'OE. Vérifiez l'homologation et la compatibilité exacte
      avec votre moteur (numéro de pièce).
  - question: Comment savoir si mon FAP est colmaté ?
    answer: Voyant FAP allumé, mode dégradé (perte de puissance), régénérations fréquentes, fumée noire, code défaut P2002
      ou P2463.
  - question: Tous les combien changer le FAP ?
    answer: Entre 150 000 et 250 000 km selon utilisation. Trajets longs = longue durée de vie. Trajets courts = colmatage
      rapide.
  - question: Peut-on nettoyer le FAP au lieu de le changer ?
    answer: Oui, le décalaminage (nettoyage chimique ou thermique) peut prolonger sa vie si pas trop colmaté. Efficace à 70-80%
      pour 150-300€.
  - question: Quelle erreur éviter avec le FAP ?
    answer: Ne jamais supprimer le FAP (illégal, amende 7500€). Éviter les trajets courts répétés. Ne pas couper le moteur
      pendant une régénération.
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
doc_id: 00b5f905-3b43-5fe3-9779-5554e31b0357
content_hash: sha256:f178e2deea3a2855
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

# FAP - Guide Diagnostic Complet

## Fonction et Rôle

Filtre et retient les particules fines des gaz d'échappement diesel

**Actions principales:** filtrer, retenir, regenerer, stocker

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant filtre particules allume tableau
- perte de puissance importante mode degrade
- regenerations frequentes odeur de brule
- fumee noire excessive a l acceleration
- surconsommation de carburant anormale
- plus de 150 000 km en conduite urbaine

## Procédure de Diagnostic

Pour diagnostiquer un problème de fap:

1. **Inspection visuelle** - Examiner l'état du fap
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

- capteur-temperature-d-air-admission
- catalyseur
- sonde-lambda
- tube-d-echappement
- vanne-egr

## Critères de Compatibilité

Pour commander le bon fap, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "passe le controle technique"

## FAQ

**FAP OE ou OES : que choisir ?**
Les FAP OES (Bosal, Walker) sont de qualité équivalente à l'OE. Vérifiez l'homologation et la compatibilité exacte avec votre moteur (numéro de pièce).

**Comment savoir si mon FAP est colmaté ?**
Voyant FAP allumé, mode dégradé (perte de puissance), régénérations fréquentes, fumée noire, code défaut P2002 ou P2463.

**Tous les combien changer le FAP ?**
Entre 150 000 et 250 000 km selon utilisation. Trajets longs = longue durée de vie. Trajets courts = colmatage rapide.

**Peut-on nettoyer le FAP au lieu de le changer ?**
Oui, le décalaminage (nettoyage chimique ou thermique) peut prolonger sa vie si pas trop colmaté. Efficace à 70-80% pour 150-300€.

**Quelle erreur éviter avec le FAP ?**
Ne jamais supprimer le FAP (illégal, amende 7500€). Éviter les trajets courts répétés. Ne pas couper le moteur pendant une régénération.
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

<!-- materialized-from-db manual/4137ea3e8a09 2026-03-26 -->
### Dépollution

Filtres à particules diesel/essence

Notre système relie un capteur de pression à la ligne d'échappement pour informer le calculateur des besoins en dépollution.

Principaux bénéfices
Résistance chimique et thermique
Mélange de caoutchouc réalisé en interne
Ensemble complet de gaines de protection
Caractéristiques techniques
Description

Assemblage de tuyaux en caoutchouc et en métal, avec capteurs.

Informations fonctionnelles
Résistance à 220 °C
Résistance chimique aux gaz d'échappement
Bénéfices
Amélioration des performances
Résistance aux hautes pressions
Fiabilité

## Symptomes supplementaires

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
