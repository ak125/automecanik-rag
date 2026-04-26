---
category: electrique
slug: demarreur
title: Démarreur
pg_id: 2
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
  role: Appliquer une rotation initiale au moteur pour declencher le demarrage
  must_be_true:
  - lancer le moteur
  - entrainer
  - demarrer
  must_not_contain:
  - charge
  - recharge
  - alimentation electrique
  - alternateur
  - universel
  - tous modèles
  - adaptable tous
  confusion_with:
  - term: alternateur
    difference: Démarreur = lance le moteur (au démarrage), Alternateur = recharge batterie (moteur tournant)
  - term: batterie
    difference: Batterie faible peut simuler un démarreur HS - toujours tester la batterie d'abord
  related_parts:
  - alternateur
  - batterie
  - bougie-d-allumage
  - bobine-d-allumage
  - poulie-d-alternateur
selection:
  criteria:
  - Marque de votre véhicule
  - Modele de votre véhicule
  - Motorisation de votre véhicule
  - Annee de votre véhicule
  anti_mistakes:
  - ❌ "démarrage garanti"
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  cost_range:
    min: 85
    max: 334
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
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
    label: Claquement contact demarrage solenoide
    severity: confort
  - id: S2
    label: Demarreur tourne mais moteur lance
    severity: confort
  - id: S3
    label: Aucune reaction au contact moteur electrique hs
    severity: immobilisation
  - id: S4
    label: Grincement ou bruit anormal au demarrage
    severity: confort
  - id: S5
    label: Odeur de brule electrique au demarrage
    severity: confort
  - id: S6
    label: Plus demarrages difficiles recurrents
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - 'vehicule immobilise ou symptome critique : verification urgente piece et alimentation'
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  quick_checks:
  - 'Observer : claquement contact demarrage solenoide ?'
  - 'Observer : demarreur tourne mais moteur lance ?'
  - 'Observer : aucune reaction au contact moteur electrique hs ?'
  - 'Observer : grincement ou bruit anormal au demarrage ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Claquement contact demarrage solenoide
  - Demarreur tourne mais moteur lance
  - Aucune reaction au contact moteur electrique hs
  - Grincement ou bruit anormal au demarrage
  - Odeur de brule electrique au demarrage
  - Plus demarrages difficiles recurrents
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '2'
  intro_title: A quoi sert Démarreur ?
  risk_title: Pourquoi remplacer Démarreur a temps ?
  risk_explanation: '**Pièce HS** - Le démarreur peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le démarreur peut être hors service et nécessiter un remplacement'
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
  - ❌ "démarrage garanti"
  - ❌ "homologué CT"
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
  - question: Démarreur OE, OES ou échange standard ?
    answer: 'Les démarreurs OES (Bosch, Valeo, Denso) sont de qualité première monte. L''échange standard est économique et
      fiable : pièce reconditionnée avec garantie.'
  - question: Comment savoir si mon démarreur est HS ?
    answer: Claquement sans démarrage (solénoïde), démarreur qui tourne dans le vide (lanceur usé), pas de réaction au contact
      (moteur électrique grillé).
  - question: Tous les combien changer le démarreur ?
    answer: Pas de périodicité fixe. Durée de vie 150 000 à 250 000 km selon utilisation. Les démarrages fréquents (ville)
      usent plus vite.
  - question: Peut-on changer le démarreur soi-même ?
    answer: Oui, opération accessible. Débrancher la batterie, dévisser les 2-3 vis de fixation, débrancher les fils. Compter
      1h à 2h selon l'accès.
  - question: Quelle erreur éviter avec le démarreur ?
    answer: Ne pas insister si le démarreur ne répond pas (risque de griller le solénoïde). Vérifier la batterie et les câbles
      avant de changer le démarreur.
  quality:
    score: 60
    source: script:rag-upgrade-v4
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - adaptable tous
  requires_vehicle: true
doc_id: 49ecb965-df48-5669-a85d-22d90aaec1c3
content_hash: sha256:8da30191f5b1f212
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
phase5_enrichment:
  _source: boschaftermarket.com + delphiautoparts.com + fr.wikipedia.org + hella.com + mann-filter.com + textar.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 11
  _has_tech_data: true
  types_variants:
  - type: 'pneumatique'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_0_1_mm: '0,1 mm'
    val_0_9_mm: '0,9 mm'
    val_000_v: '000 V'
    val_10_5_v: '10,5 V'
    val_100_a: '100 a'
    val_11_93_v: '11,93 V'
    val_12_v: '12 V'
    val_15_km: '15 km'
    val_2_a: '2 a'
    val_24_v: '24 V'
    val_3_0_ohms: '3,0 ohms'
    val_31_a: '31 a'
    val_4__v: '4. V'
    val_45_a: '45 A'
    val_59_a: '59 a'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: '- Niveau de difficulté : facile à intermédiaire (accessibilité variable selon véhicule). - Temps estimé : 30 min à
    2 h. - Outils : clés à œil/douilles 10-13 mm, rallonge + cliquet, lampe. - Précaution : débranchez impérativement la borne
    négative de la batterie — le câble B+ du démarreur est sous tension permanente. - Accès : par le dessus (véhicules compacts)
    ou par le dessous (cric + chandelles nécessaires).'
  S2: 'Ne pas attendre la panne complete pour intervenir. Symptômes d''usure : - Claquement contact demarrage solenoide -
    Demarreur tourne mais moteur lance - Aucune reaction au contact moteur electrique hs - Grincement ou bruit anormal au
    demarrage - Odeur de brule electrique au demarrage - Plus demarrages difficiles recurrents'
  S2_DIAG: 'SymptômeCause probableActionClaquement contact demarrage solenoideverification urgente piece et alimentationObserver
    : claquement contact demarrage solenoide ?Demarreur tourne mais moteur lancelocaliser source et verifier usure mecaniqueObserver
    : demarreur tourne mais moteur lance ?Aucune reaction au contact moteur electrique hsvehicule immobilise ou symptome critique
    : verification urgente piece et alimentationObserver : aucune reaction au contact moteur electrique hs ?Grincement ou
    bruit anormal au demarragebruit anormal detecte : localiser source et verifier usure mecaniqueObserver : grincement ou
    bruit anormal au demarrage ?Odeur de brule electrique au demarrageverification urgente piece et alimentationObserver :
    claquement contact demarrage solenoide ?Plus demarrages difficiles recurrentsverification urgente piece et alimentationObserver
    : claquement contact demarrage solenoide ?'
  S3: 'Pour choisir le bon demarreur pour votre vehicule : - Puissance (kW) : doit correspondre a la cylindree et au type
    de moteur — un demarreur sous- puissant ne lancera pas le moteur, surtout a froid- Nombre de dents du pignon lanceur :
    doit correspondre exactement a la couronne du volant moteur (9, 10, 11 ou 13 dents selon vehicule)- Sens de rotation :
    horaire ou anti- horaire selon le moteur — un demarreur inversé tourne dans le vide- Fixation : verifier le nombre de
    vis (2 ou 3), le diametre et l''entraxe — l''accessibilite varie fortement d''un vehicule a l''autre- Connectique : borne
    B+ (gros cable batterie) et connecteur du solenoide doivent correspondre au faisceau existant'
  S4_DEPOSE: '📖 Avant de démonter, consultez la fiche technique Démarreur pour connaître les spécifications. - Démonterun
    démarreur. - Débranchez la batterie. - Levez et calez le véhiculesi nécessaire. - Identifiez la position du démarreur.
    - Repérez les branchements etles positions des connexions du démarreur. - Débranchez les connexionsdu démarreur. - Analyser
    les points de fixation. - Identifier les différentesfixations du démarreur. Note : le démarreur peut être fixé soit à
    : - la boîte de vitesse. - la boîte de vitesse et l''arrièredu démarreur au moteur. - la boîte de vitesse par desdifférentes
    vis, et ces derniers servent à maintenir en place le groupemotopropulseur par exemple Volkswagen,Audi, Seat et Skoda.
    Dans ce type de fixations il faut placer un cric sous le moteur afinpour le soutenir. - la boîte de vitesse, dansde nombreux
    autres cas ces mêmes vis sont reliées à des organes (supportde filtre à air, support de canalisation etc.). - Déposer
    votre démarreur. - Après la dépose du démarreur,Il faut récupérer le guide qui sert pour le centrer sur la boite de vitessepuisqu''il
    peut rester accroché sur la tête du démarreur. - Récupérez le support defixation à l''arrière du démarreur car il ne sera
    pas livré sur lanouvelle pièce.'
  S4_REPOSE: '- Comparer le nouveau démarreur avec celui monté sur le véhicule avant de le remonté, s''assurez que les pointsde
    fixations et le nombre de dents soient identiques. - Mettre en place le supportde fixation arrière du démarreur. - Remontez
    le démarreuret vérifiez qu''il soit bien positionné sur son guide. - Serrer les différentesfixations du démarreur. - Nettoyez
    à l''aide d''unebrosse métallique les cosses qui pourraient être oxydées. - Rebranchez les connexionsdu démarreur. - Rebranchez
    la bornenégative de la batterie. - Vérifiez le bonfonctionnement du démarreur. ✅ Après remontage, vérifiez les spécifications
    dans la fiche technique Démarreur.'
  S5: 'Erreurs frequentes lors du remplacement d''un demarreur : - Oublier de debrancher la batterie — le cable B+ du demarreur
    est sous tension permanente, risque de court-circuit et d''etincelle- Ne pas verifier la couronne du volant moteur — des
    dents cassees empechent le lanceur d''engrener correctement et usent le demarreur neuf prematurement- Inverser les connexions
    electriques — le cable B+ (gros cable batterie) et le fil de commande du solenoide ne sont pas interchangeables- Forcer
    les vis de fixation si le demarreur ne s''aligne pas — signe que la reference est incorrecte ou qu''un element gene le
    positionnement- Ne pas tester le circuit electrique avant de remplacer le demarreur — une batterie faible, un cable oxyde
    ou un contacteur defaillant peuvent mimer une panne de demarreur- Oublier de verifier le serrage de la borne B+ apres
    montage — un mauvais contact provoque des chutes de tension et un demarrage lent'
  S6: 'Verifications apres remplacement du demarreur : - Test de demarrage : le moteur doit demarrer sans bruit anormal —
    un claquement metallique indique un mauvais engrainement du lanceur sur la couronne- Tension batterie : mesurer avec un
    multimetre (12,6 V moteur arret, 13,5-14,5 V moteur tournant) — une tension basse apres demarrage signale un probleme
    d''alternateur, pas du demarreur- Connexions electriques : verifier que la borne B+ est bien serree et sans oxydation
    — un mauvais contact provoque un demarrage lent qui mime un demarreur defaillant- Couple de serrage : verifier les vis
    de fixation du demarreur sur la cloche de boite — un demarreur mal fixe vibre et use le pignon lanceur- Absence de fumee
    ou d''odeur : une odeur de brule apres demarrage indique un probleme de cablage ou un demarreur bloque en position engrenee'
  S_GARAGE: 'Nous vous recommandons de confier cette intervention à un professionnel : - Plusieurs causes possibles de défaillance
    (4 identifiées) nécessitent un diagnostic professionnel Un garagiste qualifié dispose de l''outillage et de l''expérience
    nécessaires pour effectuer cette opération en toute sécurité.'
  S7: '- neiman - contacteur demarreur'
  S8: 'Démarreur OE, OES ou échange standard ?Les démarreurs OES (Bosch, Valeo, Denso) sont de qualité première monte. L''échange
    standard est économique et fiable : pièce reconditionnée avec garantie. Comment savoir si mon démarreur est HS ?Claquement
    sans démarrage (solénoïde), démarreur qui tourne dans le vide (lanceur usé), pas de réaction au contact (moteur électrique
    grillé). Tous les combien changer le démarreur ?Pas de périodicité fixe. Durée de vie 150 000 à 250 000 km selon utilisation.
    Les démarrages fréquents (ville) usent plus vite. Peut-on changer le démarreur soi-même ?Oui, opération accessible. Débrancher
    la batterie, dévisser les 2-3 vis de fixation, débrancher les fils. Compter 1h à 2h selon l''accès. Quelle erreur éviter
    avec le démarreur ?Ne pas insister si le démarreur ne répond pas (risque de griller le solénoïde). Vérifier la batterie
    et les câbles avant de changer le démarreur.'
  META: '{"meta_title":"Démarreur : Guide Remplacement et Diagnostic | AutoMecanik","meta_description":"Claquement au démarrage,
    moteur qui ne se lance pas ? Découvrez quand changer le démarreur, comment le remplacer et choisir la pièce compatible
    sur AutoMecanik."}'
---

# Démarreur - Guide Diagnostic Complet

## Fonction et Rôle

Appliquer une rotation initiale au moteur pour declencher le demarrage

**Actions principales:** lancer le moteur, entrainer, demarrer, mettre en rotation, entrainer le vilebrequin

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Aucune reaction au contact moteur electrique hs**
  aucune reaction au contact moteur electrique hs

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement contact demarrage solenoide**
  claquement contact demarrage solenoide
- **Grincement ou bruit anormal au demarrage**
  grincement ou bruit anormal au demarrage

### 🟢 Autres Symptômes

- demarreur tourne mais moteur lance
- odeur de brule electrique au demarrage
- plus demarrages difficiles recurrents

## Procédure de Diagnostic

Pour diagnostiquer un problème de démarreur:

1. **Inspection visuelle** - Examiner l'état du démarreur
2. **Test électrique** - Vérifier la tension et les connexions
3. **Lecture codes défaut** - Scanner OBD si voyant allumé
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le démarreur peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- neiman
- contacteur-demarreur

## ⚠️ Ne Pas Confondre Avec

### alternateur
**Distinction:** Démarreur = lance le moteur (au démarrage), Alternateur = recharge batterie (moteur tournant)

### batterie
**Distinction:** Batterie faible peut simuler un démarreur HS - toujours tester la batterie d'abord

## Critères de Compatibilité

Pour commander le bon démarreur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Motorisation** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "démarrage garanti"
- ❌ "homologué CT"
- ❌ "sécurité garantie"

## FAQ

**Démarreur OE, OES ou échange standard ?**
Les démarreurs OES (Bosch, Valeo, Denso) sont de qualité première monte. L'échange standard est économique et fiable : pièce reconditionnée avec garantie.

**Comment savoir si mon démarreur est HS ?**
Claquement sans démarrage (solénoïde), démarreur qui tourne dans le vide (lanceur usé), pas de réaction au contact (moteur électrique grillé).

**Tous les combien changer le démarreur ?**
Pas de périodicité fixe. Durée de vie 150 000 à 250 000 km selon utilisation. Les démarrages fréquents (ville) usent plus vite.

**Peut-on changer le démarreur soi-même ?**
Oui, opération accessible. Débrancher la batterie, dévisser les 2-3 vis de fixation, débrancher les fils. Compter 1h à 2h selon l'accès.

**Quelle erreur éviter avec le démarreur ?**
Ne pas insister si le démarreur ne répond pas (risque de griller le solénoïde). Vérifier la batterie et les câbles avant de changer le démarreur.
