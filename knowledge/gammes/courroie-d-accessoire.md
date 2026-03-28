---
category: distribution
slug: courroie-d-accessoire
title: Courroie d'accessoire
pg_id: 10
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
  role: Entraîne les accessoires moteur
  must_be_true:
  - entrainer
  - transmettre
  must_not_contain:
  - freinage
  - climatisation
  - turbo
  - injection
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - courroie-de-distribution
  - kit-de-distribution
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
  - ❌ "plus de puissance"
  cost_range:
    min: 7
    max: 181
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
    label: Sifflement au demarrage ou a l acceleration
    severity: confort
  - id: S2
    label: Courroie fissuree ou effilochee visible
    severity: confort
  - id: S3
    label: Voyant batterie allume alternateur non entraine
    severity: confort
  - id: S4
    label: Perte de direction assistee si sur meme courroie
    severity: securite
  - id: S5
    label: Odeur de caoutchouc brule
    severity: confort
  - id: S6
    label: Plus de 60 000 km ou 5 ans depuis le remplacement
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - remplacement preventif recommande
  quick_checks:
  - 'Observer : sifflement au demarrage ou a l acceleration ?'
  - 'Observer : courroie fissuree ou effilochee visible ?'
  - Voyant batterie allume alternateur non entraine ?
  - 'Observer : perte de direction assistee si sur meme courroie ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Sifflement au demarrage ou a l acceleration
  - Courroie fissuree ou effilochee visible
  - Voyant batterie allume alternateur non entraine
  - Perte de direction assistee si sur meme courroie
  - Odeur de caoutchouc brule
  - Plus de 60 000 km ou 5 ans depuis le remplacement
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '10'
  intro_title: A quoi sert Courroie d'accessoire ?
  risk_title: Pourquoi remplacer Courroie d'accessoire a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: Peut-on rouler sans courroie d'accessoire ?
    answer: Quelques kilomètres seulement. Sans alternateur, la batterie se vide. Sans pompe de direction, le volant devient
      très dur. Dépannage uniquement.
  - question: Comment savoir si elle est usée ?
    answer: 'Visuellement : craquelures, effilochage, brillance (glaçage). Au son : sifflement au démarrage ou quand vous
      braquez à fond.'
  - question: Faut-il changer le galet tendeur ?
    answer: Recommandé si plus de 100 000 km ou si bruit de roulement. Le galet coûte peu et peut bloquer la courroie s'il
      gripe.
  - question: Quelles sont les erreurs fréquentes à éviter ?
    answer: Mettre du produit "anti-sifflement" au lieu de changer la courroie. Trop ou pas assez tendre. Oublier de vérifier
      les galets.
  - question: Comment faire un diagnostic rapide ?
    answer: Sifflement → courroie usée ou mal tendue. Témoin batterie → courroie cassée ou alternateur. Direction dure soudaine
      → courroie à vérifier.
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
doc_id: 30f1197d-61fc-5083-95ac-cc6afe7cee95
content_hash: sha256:880711935f0e0d1b
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

# Courroie d'accessoire - Guide Diagnostic Complet

## Fonction et Rôle

Entraîne les accessoires moteur

**Actions principales:** entrainer, transmettre

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Perte de direction assistee si sur meme courroie**
  perte de direction assistee si sur meme courroie

### 🟢 Autres Symptômes

- sifflement au demarrage ou a l acceleration
- courroie fissuree ou effilochee visible
- voyant batterie allume alternateur non entraine
- odeur de caoutchouc brule
- plus de 60 000 km ou 5 ans depuis le remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de courroie d'accessoire:

1. **Inspection visuelle** - Examiner l'état du courroie d'accessoire
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- compresseur-de-climatisation
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- pompe-a-eau
- pompe-de-direction-assistee
- poulie-d-alternateur
- poulie-vilebrequin


## References supplementaires

<!-- materialized-from-db manual/9b17456bc379 2026-03-26 -->
### Courroie Stretchy

Courroie
Courroie Stretchy

La courroie élastique HUTCHINSON® (auto-tension) entraîne les systèmes d'accessoires et d'entraînement par courroie des véhicules. Elle est utilisée avec une distance fixe entre les centres des poulies et maintient automatiquement la tension du système sans nécessiter de tendeur supplémentaire.

Principaux bénéfices
Optimisation du système FEAD
Réduction des coûts et du poids
Tension stable
Caractéristiques
Structure de la courroie

Haute qualité de fabrication :

Formées par moulage, les dents de la courroie entraînent la poulie par pression de contact dans les gorges
Elles sont composées d’une base en caoutchouc EPDM, très résistante aux contraintes mécaniques et aux agressions extérieures
Selon l’application, la gamme de revêtements (flock PA / composite / film PE) offre la solution adaptée à chaque niveau sonore requis
Le câblage constitue la partie structurelle de la courroie et est composé de polyamide
Le dos de la courroie assure le contact avec les galets tendeurs et peut également transmettre la puissance sur des poulies plates
Il protège le câblage et garantit la stabilité radiale de la structure
Performances
Processus de moulage réduisant les pertes de matière et garantissant le contrôle dimensionnel
Profil conforme à la norme ISO9981
Large gamme de longueurs et de largeurs de courroies
Plage de température de fonctionnement de -40 à +135°C
Optimisée pour minimiser les pertes par friction et les charges sur les roulements
Excellente résistance à l’ozone
Résistance aux huiles et aux fluides
Durée de vie prolongée (240 000 km)
Capacité à entraîner plusieurs accessoires simultanément (alternateurs, compresseurs de climatisation, ventilateurs)
Bénéfices
Compacité
Optimisation des coûts
Légèreté
Fiabilité
Industries

<!-- materialized-from-db manual/36e9537e2c77 2026-03-26 -->
### Courroie Hybroad®

Courroie
Courroie Hybroad®

La courroie HUTCHINSON® Hybroad® est spécialement conçue et optimisée pour répondre aux exigences de l’électrification des véhicules.

Principaux bénéfices
Capacité de transmission de couple élevé
Excellentes performances acoustiques
Résistance à des sollicitations intenses
Caractéristiques
Structure de la courroie

Haute qualité de fabrication :

Face arrière en EPDM renforcé de fibres pour assurer la stabilité de la ligne de câblage
Câblage en aramide, capable de fonctionner sous très haute tension
EPDM optimisé, renforcé de fibres, permettant de transmettre des charges lourdes (couple)
Bonne adhérence en conditions sèches et humides, tout au long de la durée de vie de la courroie
Revêtement tricot, spécialement conçu pour offrir les coefficients de friction requis
Performances

Capacité de transmission de couple élevé

Tests de performance spécifiques :

Coefficients de friction à sec et en conditions humides, à l’état neuf et âgé
Test de glissement en conditions humides
Test lors des phases Stop & Start

Excellentes performances acoustiques

Tests spécifiques :

En conditions sèches et humides
À l’état neuf et âgé
Lors de redémarrage en conditions humides
En cas de désalignement

Durabilité

Tests spécifiques :

Évaluation de la fatigue des dents de la courroie en conditions chaudes et froides
Évaluation de la résistance à l’usure du câblage
Bénéfices
Amélioration des performances
Longévité
Réduction du bruit
Industries
Automobile
Camions & Bus

Voici aussi la version ultra épurée :

Courroie Hybroad®

Cette courroie est spécialement conçue pour répondre aux exigences de l’électrification des véhicules.

Principaux bénéfices
Transmission de couple élevé
Excellentes performances acoustiques
Résistance à des sollicitations intenses
Caractéristiques techniques

Structure :

Face arrière en EPDM renforcé de fibres
Câblage en aramide pour très haute tension
EPDM renforcé de fibres pour charges lourdes
Bonne adhérence à sec et en conditions humides
Revêtement tricot adapté aux coefficients de friction requis

Performances et validation :

Tests de friction à sec et en conditions humides
Tests de glissement en conditions humides
Validation en phases Stop & Start
Tests acoustiques en conditions sèches et humides
Validation au redémarrage humide et en cas de désalignement
Tests de fatigue des dents en conditions chaudes et froides
Tests de résistance à l’usure du câblage
Bénéfices
Amélioration des performances
Longévité
Réduction du bruit

<!-- materialized-from-db manual/1fde80c127aa 2026-03-26 -->
### Courroie Hybroad® avec tendeur hydraulique et galet

Systèmes d'entraînement par courroie
Courroie Hybroad® avec tendeur hydraulique et galet

La solution complète HUTCHINSON® courroie Hybroad® avec tendeur hydraulique et galet est le système idéal pour répondre aux exigences de l’électrification des véhicules.
Cette solution optimisée permet de réduire le poids et les coûts en supprimant l’isolation du vilebrequin.

Principaux bénéfices
Réduction du poids et des coûts
Système optimisé
Applications sévères y compris sur les véhicules mild-hybrid
Bénéfices
Optimisation des coûts
Amélioration des performances
Conception robuste
Industries
Automobile
Micro-mobilité
Camions & Bus
Véhicules tout terrain & Agriculture
Machines industrielles

Voici aussi la version ultra épurée :

Courroie Hybroad® avec tendeur hydraulique et galet

Cette solution complète de courroie avec tendeur hydraulique et galet est conçue pour répondre aux exigences de l’électrification des véhicules. Elle permet de réduire le poids et les coûts en supprimant l’isolation du vilebrequin.

Principaux bénéfices
Réduction du poids et des coûts
Système optimisé
Compatible avec des applications sévères, y compris les véhicules mild-hybrid
Bénéfices
Optimisation des coûts
Amélioration des performances
Conception robuste

<!-- materialized-from-db manual/587e2a0702ad 2026-03-26 -->
### Courroie Poly V

Courroie
Courroie Poly V

HUTCHINSON® Poly V est une courroie de transmission de puissance destinée aux systèmes d'accessoires et d'entraînement par courroie des véhicules.
Grâce à ses dents longitudinales, la courroie Poly V transmet le couple par contact entre les dents de la courroie et les gorges de la poulie.

Principaux bénéfices
Durabilité accrue
Structure optimisée
Performances testées et prouvées
Caractéristiques
Structure de la courroie

Haute qualité de fabrication :

Les dents sont formées par moulage et entraînent la poulie par pression de contact dans les gorges. Elles sont composées d’un caoutchouc EPDM à haute résistance aux contraintes mécaniques et aux agressions environnementales.

Selon l’application, notre gamme de revêtement de dents offre la solution adaptée à chaque niveau sonore requis.

Le câblage en polyester (PET) convient à la plupart des applications, tandis que le câblage en aramide est la norme pour les applications les plus exigeantes. Son module élevé permet de gérer les comportements NVH (bruit, vibrations, dureté) au-delà des critères habituels.

Le dos de la courroie entre en contact avec les galets tendeurs et peut également transmettre la puissance sur des poulies plates. Il protège le câblage et assure la stabilité radiale de la structure.

Performances
Processus de moulage réduisant les pertes de matière et garantissant un contrôle dimensionnel
Profil conforme à la norme ISO 9981
Rigidité et longueur de la courroie stables dans le temps
Large gamme de longueurs et de largeurs de courroies
Plage de température de fonctionnement de -40 à +135 °C
Optimisée pour minimiser les pertes par friction
Excellente résistance à l’ozone
Résistance aux huiles et aux fluides
Durée de vie prolongée (240 000 km)
Capacité à supporter les contraintes mécaniques : flexion / contre-flexion, cisaillement
Tensions dynamiques
Capacité à entraîner plusieurs accessoires simultanément (alternateur, compresseur de climatisation, pompe de direction assistée, pompe à eau, ventilateur)
Bénéfices
Longévité
Optimisation des coûts
Fiabilité
