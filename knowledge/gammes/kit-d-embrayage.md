---
category: embrayage
slug: kit-d-embrayage
title: Kit d'embrayage
pg_id: 479
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
  role: Transmettre le couple moteur à la boîte de vitesses et permettre la séparation temporaire
  must_be_true:
  - transmettre le couple
  - accoupler
  - désaccoupler
  must_not_contain:
  - sélecteur
  - pommeau
  - levier de vitesses
  - differentiel
  - cardan
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - butee-d-embrayage
  - volant-moteur
  - emetteur-d-embrayage
  - recepteur-d-embrayage
  - cable-d-embrayage
  confusion_with:
  - term: volant-moteur
    difference: Le kit d embrayage (disque+mecanisme+butee) se fixe SUR le volant moteur. Le volant moteur est une piece separee,
      plus lourde et plus chere.
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
  - ❌ "passage parfait"
  cost_range:
    min: 76
    max: 1070
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
    - LuK
    - Sachs
    standard:
    - Valeo
    - Exedy
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Embrayage patine regime monte acceleration
    severity: confort
  - id: S2
    label: Odeur brule apres cote demarrage
    severity: confort
  - id: S3
    label: Pedale d embrayage anormalement haute ou basse
    severity: confort
  - id: S4
    label: Vibrations ou a-coups au demarrage
    severity: confort
  - id: S5
    label: Difficulte a passer les vitesses craquements
    severity: confort
  - id: S6
    label: Plus de 150 000 km ou conduite urbaine intensive
    severity: confort
  causes:
  - verifier equilibrage et fixations
  - remplacement preventif recommande
  - 'vibrations anormales : verifier equilibrage et fixations'
  - 'kilometrage eleve ou usure visible : remplacement preventif recommande'
  quick_checks:
  - 'Observer : embrayage patine regime monte acceleration ?'
  - Odeur brule apres cote demarrage ?
  - 'Observer : pedale d embrayage anormalement haute ou basse ?'
  - Vibrations ou a-coups au demarrage ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Embrayage patine regime monte acceleration
  - Odeur brule apres cote demarrage
  - Pedale d embrayage anormalement haute ou basse
  - Vibrations ou a-coups au demarrage
  - Difficulte a passer les vitesses craquements
  - Plus de 150 000 km ou conduite urbaine intensive
  good_practices:
  - Eviter de laisser le pied sur la pedale d embrayage au point mort
  - Remplacement du kit complet (disque + mecanisme + butee)
  - Purge du circuit hydraulique si recepteur/emetteur concerne
  - Verifier le volant moteur lors du remplacement d embrayage
rendering:
  pgId: '479'
  intro_title: A quoi sert Kit d'embrayage ?
  risk_title: Pourquoi remplacer Kit d'embrayage a temps ?
  risk_explanation: '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
  risk_consequences:
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
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
  - question: 'Kit embrayage OE ou OES : que choisir ?'
    answer: Les kits OES (Sachs, LuK, Valeo) sont de qualité équivalente à l'OE et moins chers. Ces équipementiers fournissent
      les constructeurs. Évitez les kits premiers prix.
  - question: Comment savoir si mon embrayage est usé ?
    answer: Embrayage qui patine (régime monte sans accélération), pédale haute, odeur de brûlé, difficulté à passer les vitesses,
      vibrations au démarrage.
  - question: Tous les combien changer le kit d'embrayage ?
    answer: Entre 120 000 et 200 000 km selon conduite. Usage urbain ou remorquage l'use plus vite. Pas de périodicité fixe,
      c'est l'usure qui décide.
  - question: Peut-on changer le kit d'embrayage soi-même ?
    answer: 'Opération complexe : dépose de la boîte de vitesses obligatoire. Nécessite pont ou fosse, outils spécifiques,
      centrage du disque. Réservé aux bricoleurs expérimentés.'
  - question: Quelle erreur éviter avec le kit d'embrayage ?
    answer: Ne jamais changer une seule pièce. Vérifier le volant moteur et le remplacer si bimasse ou usé. Graisser légèrement
      les cannelures. Ne pas toucher les garnitures.
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
doc_id: 9e658751-c5e5-5985-8e61-ff27e5182f0d
content_hash: sha256:320d70c00474555f
lang: fr
variants:
- name: Kit embrayage complet
  aliases:
  - kit complet
  - 3 pieces
  functional_differences:
  - Disque + mecanisme + butee
  - Remplacement recommande en bloc
- name: Kit avec volant moteur
  aliases:
  - kit 4 pieces
  - kit + volant
  functional_differences:
  - Inclut le volant moteur bimasse
  - Pour vehicules diesel modernes
location_on_vehicle:
  area: Entre le moteur et la boite de vitesses
  access: Depose de la boite de vitesses necessaire (pont elevateur)
  adjacent_parts:
  - volant moteur
  - boite de vitesses
  - arbre primaire
installation:
  difficulty: difficile (pro recommande)
  time: 4h a 8h
  tools:
  - pont elevateur
  - cric de boite
  - centreur d embrayage
  - cle dynamometrique
  prerequisite: Depose complete de la boite de vitesses
phase5_enrichment:
  _source: ate-freinage.fr + automotive.hutchinson.com + bremboparts.com + hella.com + textar.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 11
  _has_tech_data: true
  types_variants:
  - type: 'hydraulique'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    norme_dot5.1: 'DOT5.1'
    val_100__: '100 %'
    val_2_a: '2 a'
    val_3_a: '3 a'
    val_465_a: '465 a'
    val_8_a: '8 a'
    val_86_a: '86 a'
    val_9_a: '9 a'
  materials:
  - materiau: 'EPDM'
    source_ref: corpus RAG web OEM
  - materiau: 'silicone'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le kit d''embrayage transmet le couple moteur a la boite de vitesses et permet la separation temporaire lors des changements
    de rapport. Il se compose de trois pieces principales : le disque d''embrayage (garniture de friction), le mecanisme (plateau
    de pression + diaphragme) et la butee d''embrayage. Niveau de difficulte : Avance — impose la depose de la boite de vitesses,
    qui represente l''essentiel du temps de travail. Comptez 4 a 8 h selon le vehicule (traction avant = plus complexe que
    propulsion). Outils necessaires : - Cric de boite de vitesses ou cric hydraulique rouleur- Chandelles de securite- Jeu
    de cles/douilles 10-19 mm + Torx selon vehicule- Mandrin de centrage d''embrayage (outil d''alignement du disque)- Repousse-
    piston ou outil de reglage de la butee hydraulique Pieces liees : butee d''embrayage, volant moteur, emetteur d''embrayage,
    recepteur d''embrayage, cable d''embrayage.'
  S2: 'Ne pas attendre la panne complete pour intervenir. Symptômes d''usure : - Embrayage patine regime monte acceleration
    - Odeur brule apres cote demarrage - Pedale d embrayage anormalement haute ou basse - Vibrations ou a-coups au demarrage
    - Difficulte a passer les vitesses craquements - Plus de 150 000 km ou conduite urbaine intensive'
  S2_DIAG: 'SymptômeCause probableActionEmbrayage patine regime monte accelerationverifier equilibrage et fixationsObserver
    : embrayage patine regime monte acceleration ?Odeur brule apres cote demarrageremplacement preventif recommandeOdeur brule
    apres cote demarrage ?Pedale d embrayage anormalement haute ou bassevibrations anormales : verifier equilibrage et fixationsObserver
    : pedale d embrayage anormalement haute ou basse ?Vibrations ou a-coups au demarragekilometrage eleve ou usure visible
    : remplacement preventif recommandeVibrations ou a-coups au demarrage ?Difficulte a passer les vitesses craquementsverifier
    equilibrage et fixationsObserver : embrayage patine regime monte acceleration ?Plus de 150 000 km ou conduite urbaine
    intensiveverifier equilibrage et fixationsObserver : embrayage patine regime monte acceleration ?'
  S3: 'Pour choisir le bon kit d''embrayage pour votre vehicule : - Motorisation exacte : le couple moteur determine le type
    de mecanisme et la garniture du disque — un kit sous-dimensionne patine, un kit surdimensionne durcit la pedale- Kit complet
    vs pieces separees : privilegier le kit complet (disque + mecanisme + butee) pour garantir la compatibilite des pieces
    entre elles- Volant moteur : verifier si le vehicule a un volant bimasse — s''il est use (jeu excessif, bruit de claquement
    a froid), le remplacer en meme temps sinon l''embrayage neuf s''use prematurement- Marques equipementieres : LuK, Valeo,
    Sachs fabriquent en premiere monte — les kits generiques sont moins fiables sur les vehicules a fort couple (diesel)-
    Boite de vitesses : verifier le type (manuelle, robotisee) — les boites robotisees ont des kits specifiques'
  S4_DEPOSE: '📖 Avant de démonter, consultez la fiche technique Kit d''embrayage pour connaître les spécifications. - Débranchez
    la batterie. - Levez et calez le véhicule. - Vidangez la boîte devitesses. - Démontez la tringle de vitesses. - Démontez
    la commande d''embrayage. Note : la commande peut être mécaniquepar câble d''embrayage ou hydraulique suivant le niveau
    d''équipement du véhicule. Dans lemontage hydraulique seulement le récepteur d''embrayage doit être démontez. - Démontez
    le démarreur . - Démontez les cardans. - Débranchez les capteurs de boîte de vitesse (capteur de feu de recule, capteur
    de vitesses, capteur point mort haut...). - Soutenez le moteur avec crique ou un palan ou unechèvre ou barre de fer et
    un crochet avant de démontez les supports de la boîtede vitesses. - Démontez les supports de la boîte de vitesse. - Démontez
    les fixations de la boîte de vitesses. - Immobilisez le volant moteur à l''aide d''un outilapproprié. - Démontez les vis
    de fixation du kit d''embrayage sur levolant moteur. - Démontez le mécanisme d''embrayage et le disque d''embrayage. -
    Démontez la butée d''embrayage .'
  S4_REPOSE: '- Vérifier que le kit d''embrayage neuf est identique àcelui démonté (diamètre de disque d''embrayage, le type
    de la butée et lesfixations du mécanisme). - Contrôlez le joint d''étanchéité de la boîte de vitesseset le remplacée si
    nécessaire. - Contrôlez la bague d''étanchéité de cardan et la remplacéesi nécessaire. - Contrôlez le volant moteur et
    le remplacée si volantbi-masse. - Graissez la butée d''embrayage et l''arbre primaire. - Mettre en place la butée d''embrayage.
    - Remontez le disque d''embrayage en utilisant un centreurd''embrayage. - Remontez le mécanisme d''embrayage. - Serrez
    dans l''ordre préconisé les vis de fixation dumécanisme d''embrayage. - Remontez la boîte de vitesses. - Serrez les vis
    de fixation de la boîte de vitesses sur lemoteur. - Remontez les supports de la boîte de vitesse. - Rebranchez les capteurs
    de la boîte de vitesse. - Remontez les cardans. - Remontez le démarreur . - Remontez la commande d''embrayage (câble d''embrayage
    ou récepteur d''embrayage). - Remontez la tringle de vitesses. - Rebranchez la batterie. - Faire l''appoint d''huile de
    la boîte de vitesses. - Purgez l''embrayage si le système d''embrayage est hydraulique. - Contrôlez le passage des rapports
    de vitesses en appuyant sur la pédaled''embrayage. - Démarrez le moteur. - Vérifiez le bonfonctionnement de l''embrayage.
    ✅ Après remontage, vérifiez les spécifications dans la fiche technique Kit d''embrayage.'
  S5: 'Erreurs frequentes avec le kit d''embrayage : - Ne pas centrer le disque avec le mandrin d''alignement — l''arbre primaire
    de la boite ne s''engage pas dans le disque et la boite est impossible a remonter- Monter le disque a l''envers — la garniture
    cote mecanisme et cote volant ne sont pas symetriques, verifier le marquage "cote boite" / "cote volant"- Toucher les
    garnitures du disque avec les doigts — la graisse cutanee provoque un patinage premature- Ne pas remplacer le volant bimasse
    use en meme temps — un volant avec du jeu excessif ou qui claque a froid detruit l''embrayage neuf en quelques milliers
    de km- Oublier de purger le circuit hydraulique d''embrayage apres remplacement de la butee — la pedale reste molle et
    l''embrayage ne debraye plus completement- Reutiliser les vis du mecanisme sans verifier leur etat — des vis fatiguees
    se desserrent et provoquent un balourd'
  S6: '- Eviter de laisser le pied sur la pedale d embrayage au point mort - Remplacement du kit complet (disque + mecanisme
    + butee) - Purge du circuit hydraulique si recepteur/emetteur concerne - Verifier le volant moteur lors du remplacement
    d embrayage'
  S_GARAGE: 'Nous vous recommandons de confier cette intervention à un professionnel : - Plusieurs causes possibles de défaillance
    (4 identifiées) nécessitent un diagnostic professionnel Un garagiste qualifié dispose de l''outillage et de l''expérience
    nécessaires pour effectuer cette opération en toute sécurité.'
  S7: '- butee d embrayage - cable d embrayage - emetteur d embrayage - recepteur d embrayage - volant moteur'
  S8: 'Kit embrayage OE ou OES : que choisir ?Les kits OES (Sachs, LuK, Valeo) sont de qualité équivalente à l''OE et moins
    chers. Ces équipementiers fournissent les constructeurs. Évitez les kits premiers prix. Comment savoir si mon embrayage
    est usé ?Embrayage qui patine (régime monte sans accélération), pédale haute, odeur de brûlé, difficulté à passer les
    vitesses, vibrations au démarrage. Tous les combien changer le kit d''embrayage ?Entre 120 000 et 200 000 km selon conduite.
    Usage urbain ou remorquage l''use plus vite. Pas de périodicité fixe, c''est l''usure qui décide. Peut-on changer le kit
    d''embrayage soi-même ?Opération complexe : dépose de la boîte de vitesses obligatoire. Nécessite pont ou fosse, outils
    spécifiques, centrage du disque. Réservé aux bricoleurs expérimentés. Quelle erreur éviter avec le kit d''embrayage ?Ne
    jamais changer une seule pièce. Vérifier le volant moteur et le remplacer si bimasse ou usé. Graisser légèrement les cannelures.
    Ne pas toucher les garnitures.'
  META: '{"meta_title":"Kit Embrayage : Guide Remplacement et Conseils | AutoMecanik","meta_description":"Embrayage qui patine,
    odeur de brûlé ? Découvrez quand changer le kit d''embrayage, comment le remplacer et vérifier la compatibilité sur AutoMecanik."}'
---

# Kit d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre le couple moteur à la boîte de vitesses et permettre la séparation temporaire

**Actions principales:** transmettre le couple, accoupler, désaccoupler, permettre le passage des rapports, relier

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- embrayage patine regime monte acceleration
- odeur brule apres cote demarrage
- pedale d embrayage anormalement haute ou basse
- vibrations ou a-coups au demarrage
- difficulte a passer les vitesses craquements
- plus de 150 000 km ou conduite urbaine intensive

## Procédure de Diagnostic

Pour diagnostiquer un problème de kit d'embrayage:

1. **Inspection visuelle** - Examiner l'état du kit d'embrayage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- butee-d-embrayage
- cable-d-embrayage
- emetteur-d-embrayage
- recepteur-d-embrayage
- volant-moteur

## Critères de Compatibilité

Pour commander le bon kit d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "passage parfait"

## FAQ

**Kit embrayage OE ou OES : que choisir ?**
Les kits OES (Sachs, LuK, Valeo) sont de qualité équivalente à l'OE et moins chers. Ces équipementiers fournissent les constructeurs. Évitez les kits premiers prix.

**Comment savoir si mon embrayage est usé ?**
Embrayage qui patine (régime monte sans accélération), pédale haute, odeur de brûlé, difficulté à passer les vitesses, vibrations au démarrage.

**Tous les combien changer le kit d'embrayage ?**
Entre 120 000 et 200 000 km selon conduite. Usage urbain ou remorquage l'use plus vite. Pas de périodicité fixe, c'est l'usure qui décide.

**Peut-on changer le kit d'embrayage soi-même ?**
Opération complexe : dépose de la boîte de vitesses obligatoire. Nécessite pont ou fosse, outils spécifiques, centrage du disque. Réservé aux bricoleurs expérimentés.

**Quelle erreur éviter avec le kit d'embrayage ?**
Ne jamais changer une seule pièce. Vérifier le volant moteur et le remplacer si bimasse ou usé. Graisser légèrement les cannelures. Ne pas toucher les garnitures.
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
## Mots-clés et expressions SEO

### Intention informationnelle
- comment trouver pièce auto compatible avec mon véhicule
- comment être sûr de commander la bonne pièce auto
- comment savoir le type de motorisation de ma voiture
- c'est quoi F1 F2 F3 sur une carte grise
- quelle est la différence entre type mine et code moteur
- où trouver le numéro VIN de mon véhicule
- quelle est la différence entre pièce d'origine et pièce équipementier
- où trouver un logiciel de vue éclatée automobile gratuit
- comment trouver la référence d'une pièce auto
- mon véhicule a des variantes de montage : comment choisir la bonne pièce

### Intention commerciale
- sélecteur de véhicule pièces auto
- configurateur de pièces auto en ligne
- pièce auto avec carte grise
- numéro VIN 17 caractères pièces auto
- guide pratique choisir pièces auto
- sélection des pièces détachées par modèle de voiture
- information voiture avec plaque d'immatriculation gratuit

### Intention transactionnelle
- recherche pièces auto par plaque d'immatriculation
- trouver pièce auto avec numéro de châssis
- chercher pièce détachée par référence OEM
- trouver code moteur avec VIN gratuit
- trouver numéro OEM avec VIN gratuit

### Intention navigationnelle
- Automecanik sélecteur véhicule
- Automecanik recherche par immatriculation
- Automecanik recherche par VIN

## Les 4 méthodes d'identification

### 1. Par immatriculation (la plus rapide)

Saisissez votre numéro de plaque au format SIV (AA-123-BB) ou ancien format FNI. Le système identifie automatiquement votre véhicule en quelques secondes. C'est la recherche de pièces auto par plaque d'immatriculation la plus rapide pour les plaques françaises.

**Ce qu'il faut** : plaque française (SIV ou FNI)
**Fiabilité** : bonne (si la base est à jour)
**Limitation** : les plaques étrangères ne sont pas reconnues
**Recommandé si** : vous êtes sur le véhicule ou vous avez la plaque sous les yeux. Fonctionne aussi avec la carte grise (pièce auto par carte grise).

### 2. Par numéro VIN (la plus fiable)

Saisissez les 17 caractères du VIN (visible sur la carte grise au champ E ou sur le pare-brise côté conducteur). Cette méthode offre 99%+ de fiabilité et identifie la configuration exacte sortie d'usine, y compris pour les véhicules importés.

**Ce qu'il faut** : VIN de 17 caractères (carte grise champ E)
**Fiabilité** : excellente (99%+)
**Limitation** : le VIN n'est pas toujours sous la main
**Recommandé si** : pièces de sécurité (freins, suspension), véhicule importé, ou variantes de montage. Permet aussi de trouver le code moteur avec le VIN gratuitement.

### 3. Sélection manuelle — marque, modèle, motorisation (toujours disponible)

Sélectionnez successivement la marque (champ D.1 de la carte grise), le modèle/génération, l'année (champ B) et la motorisation (champ P.3). En cas de doute entre 2 motorisations proches, utilisez la recherche par VIN.

**Ce qu'il faut** : marque, modèle, année, motorisation
**Fiabilité** : bonne (si la motorisation exacte est sélectionnée)
**Limitation** : doute possible entre motorisations proches
**Recommandé si** : vous connaissez votre véhicule. Fonctionne sans carte grise. Sélection des pièces détachées par modèle de voiture.

### 4. Par référence OEM (la plus précise)

Saisissez le numéro OEM (Origine Équipementier) gravé sur la pièce d'origine pour trouver l'équivalent exact ou les alternatives compatibles chez d'autres fabricants. C'est la méthode pour chercher une pièce détachée par sa référence OEM avec 100% de précision.

**Ce qu'il faut** : numéro OE gravé sur la pièce usagée
**Fiabilité** : maximale (100%)
**Limitation** : nécessite d'avoir la pièce usagée sous les yeux
**Recommandé si** : vous avez le numéro OE de l'ancienne pièce. Permet un remplacement à l'identique garanti et de trouver les équivalences équipementiers.

## Tableau comparatif des méthodes

| Critère | Immatriculation | VIN | Manuelle | OEM |
|---------|-----------------|-----|----------|-----|
| **Fiabilité** | Bonne (si base à jour) | Excellente (99%+) | Bonne (si motorisation exacte) | Maximale (100%) |
| **Vitesse** | Quelques secondes | Quelques secondes | 1-2 minutes | Instantané |
| **Ce qu'il faut** | Plaque française (SIV/FNI) | 17 caractères (carte grise champ E) | Marque, modèle, année, motorisation | Numéro OE (gravé sur la pièce) |
| **Quand l'utiliser** | Commandes courantes | Pièces sécurité, variantes, import | Sans carte grise, véhicule connu | Remplacement à l'identique |
| **Limitation** | Plaques étrangères non reconnues | VIN pas toujours sous la main | Doute entre motorisations proches | Pièce usagée nécessaire |

## Carte grise — champs utiles pour identifier son véhicule

| Champ | Contenu | Utilité pour le sélecteur |
|-------|---------|---------------------------|
| **B** | Date de première immatriculation | Année du véhicule (étape 3 sélection manuelle) |
| **D.1** | Marque du véhicule | Étape 1 sélection manuelle |
| **D.2** | Type mine / variante / version | Identification précise de la version |
| **E** | Numéro VIN (17 caractères) | Méthode VIN — 99%+ de fiabilité |
| **P.3** | Type de carburant (essence, diesel, hybride, électrique, GPL) | Motorisation — étape 4 sélection manuelle |
| **F.1** | Masse en charge maximale techniquement admissible (PTAC) | Dimensionner freinage et suspension |
| **F.2** | PTAC de l'ensemble (véhicule + remorque) | Dimensionner freinage |
| **F.3** | Masse en charge maximale de l'ensemble en service (PTRA) | Dimensionner suspension (amortisseurs, ressorts) |

**Astuce** : prenez votre carte grise en photo avec votre téléphone. Vous aurez toutes les infos sous la main la prochaine fois, même loin du véhicule.

## Variantes de montage

Les constructeurs automobiles utilisent plusieurs fournisseurs pour une même pièce. En cours de production, ils peuvent changer de fournisseur, modifier des spécifications ou ajouter des options.

### Pourquoi les variantes existent

- **Multi-fournisseurs** : un même modèle peut être équipé en première monte par différents équipementiers selon la date et le lieu de fabrication.
- **Évolutions en série** : les constructeurs améliorent les pièces en continu. Un véhicule de début de série peut avoir des spécifications différentes d'un véhicule de fin de série.
- **Options d'usine** : les packs sport, suspensions pilotées ou systèmes Start & Stop modifient les pièces requises.

### Exemples courants de variantes (même véhicule)

| Catégorie | Variante |
|-----------|----------|
| **Freinage** | Diamètre disque 280 vs 288 vs 312 mm, ventilé vs plein |
| **Batterie** | Start & Stop → AGM/EFB obligatoire |
| **Filtration** | Cartouche vs vissé selon moteur |
| **Suspension** | Standard vs sport / pilotée |

### Comment éviter l'erreur

1. Vérifiez les critères clés sur la fiche produit (diamètre, capteur, type de fixation).
2. Privilégiez le VIN quand c'est disponible — 99% de compatibilité.
3. En cas de doute : comparez le numéro OE de l'ancienne pièce avec les références proposées. Le numéro OE = la meilleure confirmation.
