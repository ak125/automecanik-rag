---
category: electrique
slug: batterie
title: Batterie
pg_id: 1
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-21'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: high
lifecycle:
  stage: v4_converted
  last_enriched_by: script:rag-enrich-metier-templates
  last_enriched_at: '2026-03-26'
domain:
  role: Stocker et fournir l'energie electrique pour demarrer le moteur et alimenter les equipements du vehicule
  must_be_true:
  - stocker l'energie
  - fournir du courant
  - demarrer le moteur
  - alimenter les equipements
  must_not_contain:
  - recharger (role de l'alternateur)
  - produire de l'electricite
  - universel
  - tous modeles
  - adaptable tous
  confusion_with:
  - term: alternateur
    difference: La batterie stocke l'energie, l'alternateur la produit et recharge la batterie moteur tournant
  - term: demarreur
    difference: La batterie fournit le courant, le demarreur convertit ce courant en rotation mecanique pour lancer le moteur
  related_parts:
  - alternateur
  - demarreur
  - cosses-de-batterie
  - cables-de-batterie
  - coupe-circuit-batterie
selection:
  criteria:
  - Marque de votre vehicule
  - Modele de votre vehicule
  - Motorisation de votre vehicule
  - Annee de votre vehicule
  - Tension nominale (12V pour vehicules legers, 24V pour poids lourds)
  - Capacite en Ah (amperes-heures) adaptee a la motorisation
  - Courant de demarrage a froid CCA (Cold Cranking Amps)
  - Technologie (SLI standard, EFB pour Start-Stop basique, AGM pour Start-Stop avance)
  - Dimensions et polarite (borne positive a droite ou a gauche)
  anti_mistakes:
  - universel
  - tous modeles
  - adaptable tous
  - pas cher
  - premier prix
  cost_range:
    min: 60
    max: 350
    currency: EUR
    unit: l'unite
    source: Bosch aftermarket 2026
  brands:
    premium:
    - Bosch
    - Valeo
    - Denso
    standard:
    - Hella
    - NGK
    - Delphi
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Demarrage lent ou laborieux surtout a froid
    severity: securite
  - id: S2
    label: Voyant batterie allume sur le tableau de bord
    severity: securite
  - id: S3
    label: Perte de memoire autoradio et horloge apres arret prolonge
    severity: confort
  - id: S4
    label: Phares et eclairage interieur faibles moteur eteint
    severity: confort
  - id: S5
    label: Batterie gonflée ou deformee (surcharge ou gel)
    severity: securite
  - id: S6
    label: Odeur de soufre ou d'oeuf pourri pres de la batterie
    severity: securite
  causes:
  - usure naturelle des plaques de plomb (4-5 ans en moyenne)
  - decharges profondes repetees (courts trajets, oubli phares)
  - alternateur defaillant ne rechargeant plus correctement
  - temperatures extremes (gel hivernal, canicule estivale)
  depose_steps:
  - Couper le contact et retirer la cle
  - Debrancher la borne negative (-) en premier
  - Debrancher la borne positive (+)
  - Retirer la fixation de maintien de la batterie
  - Extraire la batterie (attention au poids 15-25 kg)
  - Nettoyer le bac et les cosses si necessaire
  - Poser la batterie neuve, fixer le maintien
  - Rebrancher la borne positive (+) en premier puis la negative (-)
  quick_checks:
  - 'Observer : demarrage lent ou laborieux surtout a froid ?'
  - Voyant batterie allume sur le tableau de bord ?
  - 'Observer : perte de memoire autoradio et horloge apres arret prolonge ?'
  - 'Observer : phares et eclairage interieur faibles moteur eteint ?'
maintenance:
  interval:
    value: 4 a 5 ans
    unit: duree
    note: Verifier la tension avant chaque hiver (12.6V minimum au repos). Les batteries EFB/AGM peuvent durer 6-7 ans.
    source: Bosch aftermarket
  good_practices:
  - Verifier la tension au repos avec un multimetre (12.4V minimum)
  - Nettoyer les cosses si presence d'oxydation (sulfate blanc)
  - Eviter les decharges profondes repetees
  - Recharger avec un chargeur intelligent si vehicule immobilise plus de 3 semaines
  - Controler le bon serrage des cosses
  wear_signs:
  - Demarrage lent ou laborieux surtout a froid
  - Voyant batterie allume sur le tableau de bord
  - Perte de memoire autoradio et horloge apres arret prolonge
  - Phares et eclairage interieur faibles moteur eteint
  - Batterie gonflée ou deformee (surcharge ou gel)
  - Odeur de soufre ou d'oeuf pourri pres de la batterie
rendering:
  pgId: '1'
  intro_title: A quoi sert la batterie auto ?
  risk_title: Pourquoi remplacer la batterie a temps ?
  risk_explanation: '**Panne de demarrage** - Une batterie faible peut vous immobiliser sans prevenir'
  risk_consequences:
  - '**Panne de demarrage** - Immobilisation soudaine, surtout par temps froid'
  - '**Decharge profonde** - Endommage definitivement les plaques internes'
  - '**Surcharge** - Batterie gonflee = risque de fuite acide'
  risk_conclusion: Un controle preventif avant l'hiver evite la panne au pire moment.
  arguments:
  - content: Selection guidee par vehicule, Ah, CCA et technologie.
    icon: check-circle
    title: Compatibilite verifiee
  - content: Un remplacement preventif evite l'immobilisation.
    icon: shield-check
    title: Priorite securite
  - content: Le guide aide a choisir entre SLI, EFB et AGM.
    icon: clock
    title: Decision rapide
  - content: Verifier cosses et fixation reduit les retours.
    icon: list-check
    title: Montage maitrise
  faq:
  - question: Batterie OE ou adaptable, comment choisir ?
    answer: Privilegier une batterie de marque reconnue (Bosch, Varta, Exide) avec les memes Ah et CCA que l'origine. Les
      batteries AGM sont obligatoires pour les vehicules Start-Stop avances.
  - question: Comment savoir si ma batterie est HS ?
    answer: Tension au repos inferieure a 12.4V, demarrage lent, voyant batterie allume, perte des memoires electroniques
      apres une nuit. Un test de charge chez un professionnel confirme le diagnostic.
  - question: Tous les combien changer la batterie ?
    answer: En moyenne 4 a 5 ans pour une batterie SLI, 5 a 7 ans pour EFB/AGM. Verifier la tension avant chaque hiver et
      apres une periode d'immobilisation.
  - question: Peut-on changer la batterie soi-meme ?
    answer: 'Oui, operation simple (15-30 min). Toujours debrancher le negatif en premier et rebrancher le positif en premier.
      Attention : sur certains vehicules recents, un recalibrage calculateur est necessaire apres remplacement.'
  - question: Quelle erreur eviter avec la batterie ?
    answer: Ne jamais inverser les polarites (risque de court-circuit et destruction du calculateur). Ne pas monter une batterie
      SLI sur un vehicule Start-Stop (exige EFB ou AGM). Eviter les batteries sans marque ou sous-dimensionnees en CCA.
  quality:
    score: 76
    source: manual:claude-r3-kp
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modeles
  - adaptable tous
  requires_vehicle: true
doc_id: 5572827b-068e-5f80-bb39-6d7a4d2515ad
content_hash: sha256:5e8b7e6664e2584e
lang: fr
variants:
- name: Piece neuve OE/OES
  aliases:
  - neuf
  - OE
  - OES
  functional_differences:
  - Garantie constructeur ou equipementier
  - Calibration d usine
- name: Piece echange standard
  aliases:
  - echange standard
  - reconditionne
  functional_differences:
  - Moins cher
  - Piece d origine reconditionnee
location_on_vehicle:
  area: Compartiment moteur (alternateur, demarreur) ou peripherie
  access: Par le dessus (capot) ou par le dessous selon modele
  adjacent_parts:
  - faisceau electrique
  - batterie
  - fusibles
installation:
  difficulty: facile a moyen
  time: 15min a 1h
  tools:
  - cle a douille
  - multimetre
  - tournevis
  prerequisite: Debrancher la batterie avant intervention
---

# Batterie - Guide Diagnostic Complet

## Fonction et Role

Stocker et fournir l'energie electrique pour demarrer le moteur et alimenter les equipements du vehicule a l'arret et au demarrage.

**Actions principales:** stocker l'energie, fournir du courant, demarrer le moteur, alimenter les equipements, maintenir la tension

## Symptomes de Defaillance

### 🔴 Symptomes Securite

- Demarrage lent ou laborieux surtout a froid
- Voyant batterie allume sur le tableau de bord
- Batterie gonflee ou deformee (surcharge ou gel)
- Odeur de soufre ou d'oeuf pourri pres de la batterie

### 🟢 Autres Symptomes

- Perte de memoire autoradio et horloge apres arret prolonge
- Phares et eclairage interieur faibles moteur eteint

## Procedure de Diagnostic

Pour diagnostiquer un probleme de batterie:

1. **Mesure de tension au repos** - Multimetre sur les bornes, moteur eteint (12.6V = 100%, 12.4V = 75%, 12.2V = 50%)
2. **Test de charge** - Tension moteur tournant entre 13.5V et 14.5V (alternateur OK)
3. **Inspection visuelle** - Verifier gonflement, fissures, oxydation cosses, niveau electrolyte si accessible
4. **Test de demarrage** - Tension ne doit pas descendre sous 10V au demarrage


## Entretien et Intervalles

- **Intervalle** : 4 a 5 ans
- Verifier la tension avant chaque hiver (12.6V minimum au repos). Les batteries EFB/AGM peuvent durer 6-7 ans.

## Causes Probables

- **Usure naturelle** - Degradation des plaques de plomb apres 4-5 ans
- **Decharges profondes** - Courts trajets repetes, oubli phares ou equipements
- **Alternateur defaillant** - Ne recharge plus correctement la batterie
- **Temperatures extremes** - Gel hivernal ou canicule estivale accelerent le vieillissement

## Pieces Associees

Lors du remplacement, verifier egalement:

- alternateur
- demarreur
- cosses-de-batterie
- cables-de-batterie
- coupe-circuit-batterie

## Ne Pas Confondre Avec

### alternateur
**Distinction:** La batterie stocke l'energie electrique, l'alternateur la produit et recharge la batterie moteur tournant

### demarreur
**Distinction:** La batterie fournit le courant electrique, le demarreur le convertit en rotation mecanique pour lancer le moteur

## Criteres de Compatibilite

Pour commander la bonne batterie, vous devez connaitre:

- **Marque** de votre vehicule
- **Modele** de votre vehicule
- **Motorisation** de votre vehicule
- **Annee** de votre vehicule
- **Tension** nominale (12V ou 24V)
- **Capacite** en Ah (amperes-heures)
- **CCA** courant de demarrage a froid
- **Technologie** SLI, EFB ou AGM selon equipement Start-Stop
- **Dimensions et polarite** de la borne positive

## Attention aux Fausses Promesses

Mefiez-vous des vendeurs qui utilisent ces termes interdits:

- "universel"
- "tous modeles"
- "adaptable tous"
- "pas cher"
- "premier prix"

## FAQ

**Batterie OE ou adaptable, comment choisir ?**
Privilegier une batterie de marque reconnue (Bosch, Varta, Exide) avec les memes Ah et CCA que l'origine. Les batteries AGM sont obligatoires pour les vehicules Start-Stop avances.

**Comment savoir si ma batterie est HS ?**
Tension au repos inferieure a 12.4V, demarrage lent, voyant batterie allume, perte des memoires electroniques apres une nuit. Un test de charge chez un professionnel confirme le diagnostic.

**Tous les combien changer la batterie ?**
En moyenne 4 a 5 ans pour une batterie SLI, 5 a 7 ans pour EFB/AGM. Verifier la tension avant chaque hiver et apres une periode d'immobilisation.

**Peut-on changer la batterie soi-meme ?**
Oui, operation simple (15-30 min). Toujours debrancher le negatif en premier et rebrancher le positif en premier. Attention : sur certains vehicules recents, un recalibrage calculateur est necessaire apres remplacement.

**Quelle erreur eviter avec la batterie ?**
Ne jamais inverser les polarites (risque de court-circuit et destruction du calculateur). Ne pas monter une batterie SLI sur un vehicule Start-Stop (exige EFB ou AGM). Eviter les batteries sans marque ou sous-dimensionnees en CCA.
