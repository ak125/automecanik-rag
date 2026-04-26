---
category: distribution
slug: galet-tendeur-de-courroie-de-distribution
title: Galet tendeur de courroie de distribution
pg_id: 308
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-04-03'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:rag-enrich-from-web-corpus
  last_enriched_at: '2026-04-03'
  v5_migrated_at: '2026-03-29'
domain:
  role: Maintenir la tension de la courroie de distribution
  must_be_true:
  - tendre
  - maintenir
  - ajuster
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
  - ❌ "synchronisation parfaite"
  cost_range:
    min: 25
    max: 80
    currency: EUR
    unit: galet seul
    source: catalogue automecanik
  quality_tiers:
  - tier: Qualité Origine (OE)
    description: Galets tendeurs de distribution fournis en première monte. Mécanisme de tension à ressort calibré, roulement
      haute précision résistant aux cycles thermiques.
  - tier: Équivalent Qualité Origine
    description: Galets tendeurs fabriqués selon les mêmes spécifications de charge et de tension que l'OE. Ressort de rappel
      et roulement conformes aux exigences constructeur.
  - tier: Adaptable Économique
    description: Galets tendeurs aux dimensions compatibles pour un usage courant. Vérifier le type de fixation, le diamètre
      et la force de tension avant montage.
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
    label: Sifflement ou couinement cote distribution
    severity: confort
  - id: S2
    label: Bruit de roulement au ralenti
    severity: confort
  - id: S3
    label: Jeu excessif dans le galet controle main
    severity: confort
  - id: S4
    label: Traces de rouille sur le galet
    severity: confort
  - id: S5
    label: Bruit qui varie avec le regime moteur
    severity: confort
  - id: S6
    label: Grincement au demarrage a froid
    severity: confort
  - id: S7
    label: Courroie qui saute cas extreme
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : sifflement ou couinement cote distribution'
  quick_checks:
  - 'Observer : sifflement ou couinement cote distribution ?'
  - Bruit de roulement au ralenti ?
  - 'Observer : jeu excessif dans le galet controle main ?'
  - 'Observer : traces de rouille sur le galet ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Sifflement ou couinement cote distribution
  - Bruit de roulement au ralenti
  - Jeu excessif dans le galet controle main
  - Traces de rouille sur le galet
  - Bruit qui varie avec le regime moteur
  - Grincement au demarrage a froid
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '308'
  intro_title: A quoi sert Galet tendeur de courroie de distribution ?
  risk_title: Pourquoi remplacer Galet tendeur de courroie de distribution a temps ?
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
  - question: Peut-on changer le galet seul ?
    answer: Techniquement oui, mais déconseillé. Si vous accédez au galet, changez tout le kit. La courroie a probablement
      le même âge.
  - question: Comment savoir si le galet est HS ?
    answer: Bruit de roulement, jeu quand on le secoue, traces de rouille ou de surchauffe. En cas de doute, remplacez-le
      avec la courroie.
  - question: Galet tendeur vs galet enrouleur ?
    answer: Le tendeur maintient la tension, l'enrouleur guide la courroie. Les deux sont critiques et se changent ensemble.
  - question: Quelles sont les erreurs fréquentes à éviter ?
    answer: Réutiliser le galet "parce qu'il tourne encore". Mal régler la tension au remontage. Acheter un galet premier
      prix.
  - question: Comment faire un diagnostic rapide ?
    answer: Bruit de roulement côté distribution → galet suspect. Sifflement au ralenti → tension ou galet. Jeu dans le galet
      → remplacement urgent.
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
doc_id: 64a4e6a0-6250-53e7-9a3c-5af7b0d04870
content_hash: sha256:9e87bf8816fa284d
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
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'rainuré'
    source_ref: corpus RAG web OEM
  - type: 'trapézoïdal'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_373_kw: '373 kW'
    val_600_kw: '600 kW'
    val_96__: '96 %'
    val_98__: '98 %'
  materials:
  - materiau: 'Kevlar'
    source_ref: corpus RAG web OEM
  - materiau: 'aramide'
    source_ref: corpus RAG web OEM
  - materiau: 'polyamide '
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le galet tendeur de courroie de distribution assure la tension de la courroieet réduire les vibrations. Le réglage
    de la tension de la courroie dedistribution du moteur se fait manuellement ou automatiquement suivant le type du galettendeur.
    Il existedeux types de galet tendeur : - Galet tendeur mécanique est composé d''un ressort de torsion etd''élément de
    friction. - Galet tendeur hydrauliqueest composé d''un ressort de compression et d''un circuit hydraulique où unfluide
    est forcé par un orifice calibré'
  S2: 'Un galet tendeur de courroie de distribution défectueux présente plusieurs symptômes : - Courroie de distribution qui
    siffle. - Courroie de distribution pas assez tendue. - Un jeu dans le galet tendeur. Un galet tendeur de courroie de distribution
    usé et qu''iln''est pas remplacé à temps peut provoquer plusieurs pannes : - Rupture de la courroie de distribution. -
    Rupture du vilebrequin. - Usure de la roue dentée de vilebrequin. - Casse des arbres à cames. - Casse de la pompe injection
    (pour moteurdiesel).'
  S3: 'Le galet tendeur de courroie de distribution est une pièce dont la défaillance peut entraîner une casse moteur grave.
    La sélection doit donc se faire sur la base de critères techniques stricts, sans compromis sur la référence ou la qualité
    du roulement. Voici les points de contrôle avant commande.- Référence constructeur ou équipementier d''origine — Le galet
    de distribution est dimensionné pour un couple de serrage et une plage de tension précis définis par le constructeur.
    Utilisez la référence OEM (ex. : 06B109243E sur VAG) ou celle de l''équipementier (INA, SKF, DAYCO, Gates) pour garantir
    l''interchangeabilité.- Code moteur exact, pas uniquement la cylindrée — Un moteur 1.9 TDI peut exister en version 90
    ch ou 130 ch avec des géométries de distribution différentes. Le code moteur (ex. : ALH, ARL, ASZ) détermine la tension
    de ressort du galet et son emplacement dans la chaîne de pièces.- Diamètre de la gorge et profil de la piste de roulement
    — La piste doit correspondre exactement au profil de la courroie crantée (pas de largeur en mm). Un galet trop étroit
    ou à profil lisse ne peut pas être utilisé à la place d''un galet à gorge crantée.- Type de galet : tendeur fixe ou oscillant
    — Certains moteurs utilisent un galet tendeur à ressort intégré (dit oscillant ou automatique), d''autres un galet à axe
    fixe réglé manuellement à l''aide d''un outil de mise en tension. Ces deux types ne sont pas interchangeables.- Qualité
    du roulement : étanchéité et jeu radial — Exigez un roulement 2RS (double joint étanche) de classe C3 ou C0. Le jeu radial
    conditionne la précision de rotation sous charge thermique. Les roulements de bas de gamme présentent souvent des jeux
    excessifs visibles à la main.- Kit distribution complet ou galet seul — Si le kilométrage dépasse 100 000 km ou si la
    courroie n''a jamais été changée, remplacer le galet seul est une fausse économie. Comparez le coût d''un kit complet
    (courroie + galet + galet enrouleur + pompe à eau si applicable) par rapport au prix de la main-d''œuvre d''une re-dépose.-
    Couple de serrage de l''axe central — L''axe du galet doit être serré au couple spécifié (généralement entre 20 et 45
    N·m selon le moteur). Vérifiez que la fiche technique du galet acheté précise cette valeur pour valider la conformité
    à la procédure constructeur.Pour aller plus loin : consultez notre guide d''achat galet tendeur de courroie de distribution
    — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: '- Débranchez la batterie. - Démontez la courroie de distribution . - Démontez la fixation du galet tendeur de
    la courroie de distribution. - Retirez le galet tendeur de courroie de distribution.'
  S4_REPOSE: '- Vérifiez que le galet tendeur de courroie de distribution neuf est identique à celui démonté. - Changez le
    kit de distribution . - Remontez le galet tendeur de courroie de distribution. - Serrez la fixation du galet tendeur de
    courroie de distribution. - Remontez la courroie de distribution. - Rebranchez la batterie.'
  S5: '- ❌ "homologué CT - ❌ "sécurité garantie - ❌ "zéro panne - ❌ "garanti à vie - ❌ "synchronisation parfaite'
  S6: 'Le galet tendeur de courroie de distribution est une pièce dont la défaillance peut provoquer une casse moteur sévère.
    Après son remplacement, les contrôles suivants sont indispensables avant toute mise en route prolongée. - Vérification
    du calage distribution : avant de démarrer, confirmer que les repères de calage moteur (pignon vilebrequin, pignon arbre
    à cames) sont correctement alignés selon les marques constructeur. Un calage décalé d''une dent peut provoquer une collision
    pistons-soupapes. - Contrôle du couple de serrage du galet : le boulon du galet tendeur de distribution doit être serré
    au couple spécifié par le constructeur (en général 20 à 45 N·m selon le moteur). Utiliser une clé dynamométrique — un
    serrage insuffisant provoque un jeu progressif sous vibrations. - Contrôle de la tension courroie de distribution : après
    serrage du tendeur, vérifier que la courroie présente la tension conforme : ni trop lâche (risque de saut de dent), ni
    trop tendue (usure prématurée des galets et de la courroie). Utiliser l''outil de mesure de tension préconisé si disponible.
    - Contrôle du jeu radial du galet à la main : avant démarrage, vérifier manuellement qu''il n''existe aucun jeu radial
    ni axial sur le nouveau galet. Un galet qui oscille latéralement est défectueux ou mal monté. - Premier démarrage — écoute
    attentive : démarrer moteur froid et laisser au ralenti 3 minutes. Aucun claquement côté distribution, aucun grincement
    ni sifflement ne doit être perceptible. Arrêter immédiatement si un bruit anormal est détecté. - Contrôle du régime de
    ralenti : le régime de ralenti doit être stable (750 à 850 tr/min selon moteur). Une instabilité ou une chute de régime
    peut indiquer un problème de calage ou une courroie qui saute. - Vérification de la courroie et du galet après montée
    en température : une fois le moteur à température de fonctionnement (environ 90 °C), arrêter et contrôler visuellement
    l''absence de suintement d''huile au niveau du galet, de traces de frottement sur la courroie et de déformation du galet.'
  S7: Quel est le prix d'un galet tendeur de courroie de distribution ?Le prix varie selon le véhicule et la marque. Utilisez
    notre sélecteur pour trouver le galet tendeur de courroie de distribution compatible avec votre véhicule et comparer les
    tarifs des différents équipementiers.Comment savoir si mon galet tendeur de courroie de distribution est à changer ?Les
    signes d'usure les plus courants sont détaillés dans la section diagnostic ci-dessus. En cas de doute, faites contrôler
    la pièce par un professionnel.Peut-on rouler avec un galet tendeur de courroie de distribution défaillant ?Cela dépend
    de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule. Consultez la section symptômes
    pour évaluer l'urgence du remplacement.- courroie de distribution
  S8: Comment choisir Galet tendeur de courroie de distribution compatibleRenseignez marque, modele, type moteur et annee,
    puis verifiez la reference Quand remplacer Galet tendeur de courroie de distribution ?En cas de sifflement ou couinement
    cote distribution ou de degradation Puis-je monter Galet tendeur de courroie de distribution sans verificationLe montage
    peut exiger controles de couple, alignement et references.
  META: '{"meta_title":"Galet tendeur distribution : bruit, usure, remplacement | AutoMecanik","meta_description":"Grincement
    ou bruit de roulement côté distribution ? Un galet tendeur usé peut faire sauter la courroie. Ce guide explique quand
    le changer et pourquoi toujours en kit.","og_title":"Galet tendeur courroie distribution : guide complet","og_description":"Grincement
    ou bruit de roulement côté distribution ? Un galet tendeur usé peut faire sauter la courroie. Ce guide explique quand
    le changer et pourquoi toujours en kit.","schema_type":"Article","primary_intent":"diagnostic","gate_report" :"PASS","char_count_title":60,"char_count_desc":185}'
---

# Galet tendeur de courroie de distribution - Guide Diagnostic Complet

## Fonction et Rôle

Maintenir la tension de la courroie de distribution

**Actions principales:** tendre, maintenir, ajuster

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Grincement au demarrage a froid**
  grincement au demarrage a froid

### 🟢 Autres Symptômes

- sifflement ou couinement cote distribution
- bruit de roulement au ralenti
- jeu excessif dans le galet controle main
- traces de rouille sur le galet
- bruit qui varie avec le regime moteur
- courroie qui saute cas extreme

## Procédure de Diagnostic

Pour diagnostiquer un problème de galet tendeur de courroie de distribution:

1. **Inspection visuelle** - Examiner l'état du galet tendeur de courroie de distribution
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

- courroie-de-distribution

## Critères de Compatibilité

Pour commander le bon galet tendeur de courroie de distribution, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "synchronisation parfaite"

## FAQ

**Peut-on changer le galet seul ?**
Techniquement oui, mais déconseillé. Si vous accédez au galet, changez tout le kit. La courroie a probablement le même âge.

**Comment savoir si le galet est HS ?**
Bruit de roulement, jeu quand on le secoue, traces de rouille ou de surchauffe. En cas de doute, remplacez-le avec la courroie.

**Galet tendeur vs galet enrouleur ?**
Le tendeur maintient la tension, l'enrouleur guide la courroie. Les deux sont critiques et se changent ensemble.

**Quelles sont les erreurs fréquentes à éviter ?**
Réutiliser le galet "parce qu'il tourne encore". Mal régler la tension au remontage. Acheter un galet premier prix.

**Comment faire un diagnostic rapide ?**
Bruit de roulement côté distribution → galet suspect. Sifflement au ralenti → tension ou galet. Jeu dans le galet → remplacement urgent.
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
