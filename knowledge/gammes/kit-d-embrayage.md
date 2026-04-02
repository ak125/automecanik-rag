---
category: embrayage
slug: kit-d-embrayage
title: Kit d'embrayage
pg_id: 479
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-04-02'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:rag-enrich-from-web-corpus
  last_enriched_at: '2026-04-02'
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
  _source: ate-freinage.fr + automotive.hutchinson.com + bremboparts.com + textar.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 10
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

## Dépannage

### Mon véhicule n'apparaît pas dans le sélecteur

**Cause probable** : véhicule importé, très récent, ou plaque étrangère non reconnue.
**Solution** : passez en recherche par VIN (champ E de la carte grise). Les véhicules importés depuis l'Allemagne ou la Belgique sont généralement reconnus par VIN même si la plaque ne fonctionne pas.

### J'hésite entre deux motorisations proches

**Cause probable** : le modèle existe avec plusieurs cylindrées ou puissances similaires (ex : 1.5 dCi 90ch vs 110ch).
**Solution** : utilisez le VIN pour identifier la configuration exacte. Sinon, vérifiez le champ P.3 (carburant) et D.2 (type mine) sur votre carte grise.

### Le sélecteur propose plusieurs variantes pour une même pièce

**Cause probable** : le constructeur a utilisé plusieurs fournisseurs ou modifié les spécifications en cours de production.
**Solution** : mesurez la pièce actuelle (diamètre, nombre de trous) ou relevez le numéro OE gravé dessus. Ce numéro est la confirmation la plus fiable.

### La pièce affichée est marquée "compatible" mais je ne suis pas sûr

**Cause probable** : doute sur la variante de montage ou les options du véhicule.
**Solution** : comparez le numéro OE de votre pièce actuelle avec les références propo

[...]


## Conseils supplementaires

<!-- materialized-from-db web/7e4c02e012b4 2026-03-28 -->
### Instructions pour remplacer le... - Montage auto - section-1

# Instructions pour remplacer le... - Montage auto

- Skip to main content Skip to menu Skip to footer Partager sur Instructions pour remplacer le cylindre émetteur d'embrayage avec butée d’embrayage intégrée (CCSC) Nous vous conseillons de lire et de suivre attentivement les instructions fournies. Vous trouverez les mêmes instructions dans l’emballage des étriers de frein. N’oubliez pas de les conserver pendant toute la durée de vie du produit. En cas de passage de propriété, elles devront être remises au nouveau propriétaire du véhicule. Nous conseillons de n’effectuer que les opérations nécessaires pour le remplacement de la pièce de rechange ou des pièces de rechange souhaitées. Procédure de montage/indications initiales 1. Ne pas enfoncer la pédale plusieurs fois l’une après l’autre pour la purge, mais l’enfoncer une seule fois et attendre que le système hydraulique se stabilise (risque de surpression à l'intérieur de CCSC). 2. Ne pas utiliser de lubrifiant ou de produits de nettoyage parce qu’ils risquent d’endommager les joints du CCSC. 3. Toujours faire attention au niveau de propreté. 4. Utiliser uniquement le liquide de frein approuvé par le constructeur du véhicule. 5. Nettoyer les anciens joints ou les déposer (s’ils sont fournis avec le CCSC) et éliminer la poussière de la surface d’union. 6. Nettoyer la partie initiale de l'arbre de transmission et vérifier que l’usure n'est pas excessive sur la surface d'étanchéité. 7. Veiller à ce que le CCSC soit installé à plat par rapport à la surface de montage. 8. S’assurer que l'adaptateur est enclenché, avant de serrer complètement les vis de fixation du CCSC. 9. Placer les boulons de fixation du dispositif et les serrer selon les prescriptions du constructeur du véhicule. 10. Ne jamais purger le CCSC si l’embrayage et le volant n’ont pas encore été montés (il doit toujours y avoir une charge de réaction opposée à la course du CCSC). 11. S’assurer que le dispositif n’est pas incliné pendant l’installation parce que l’inclinaison provoque des dommages aux supports ou un désalignement angulaire qui compromet le fonctionnement du dispositif. 12. À la fin de la purge, resserrer la vis (si présente) de façon à garantir sa tenue. Toujours remplacer le mécanisme d'embrayage avec systèmes de rattrapage de l’usure. Toujours remplacer le volant d’embrayage et le diaphragme. Procédure correcte de montage La méthode de fixation du couvercle au volant a une forte répercussion sur les caractéristiques fonctionnelles du système d’embrayage (spécialement pour les embrayages avec réglage automatique) et donc sur les performances du CCSC et sur sa durée (charge/hauteur). Afin de respecter et de maintenir la conformité de l’embrayage en ce qui concerne ces caractéristiques, il faut monter l’embrayage en utilisant l’outil spécifique avant de procéder à l’insertion du volant. Voir le schéma ci-contre. Lors du montage du système d’embrayage, il faut faire très attention aux possibles erreurs susceptibles de se produire et qui risqueraient d’endommager le CCSC, en entraînant la perte de validité de la garantie du fabricant. When fitting the clutch system, take the utmost care to avoid possible errors which may occur and thus damage the CCSC, thereby nullifying the manufacturer’s warranty . Ci-dessous nous en citons quelques-unes: 1. Erreur de montage du volant côté contraire Le volant mal assemblé endommage le CCSC parce que la bague de sécurité est déformée et que le CCSC perd. 2. Erreur d’assemblage : surcourse En cas d’erreur de montage ou de purge du système, il est possible que le CCSC fonctionne en surcourse. Une course excessive comporte l’endommagement de la bague d'étanchéité et/ou du joint primaire, ce qui provoque le glissement de la bague hors du guide. 3. Désalignement axial et angulaire boîte de vitesses/moteur Un erreur de montage axial et/ou angulaire du CCSC par rapport à l’arbre de boîte de vitesses, compromet le fonctionnement du dispositif en réduisant la durée de la bague d’étanchéité de l’arbre côté boîte de vitesses. 4. Liquide incorrect Le circuit hydraulique de l’embrayage ne doit être rempli qu’avec le liquide approprié. Ne jamais utiliser d’huile minérale et toujours utiliser le liquide d'embrayage indiqué par le constructeur dans la notice d'entretien du véhicule. 5. Erreur lors de la purge - surpression L’opération de purge manuelle doit être effectuée en suivant les étapes ci-dessous :

![La méthode de fixation du couvercle au volant a une forte répercussion sur les caractéristiques fonctionnelles du système d’embrayage (spécialement pour les embrayages avec réglage automatique) et donc sur les performances du CCSC et sur sa durée (charge/hauteur).  Afin de respecter et de maintenir la conformité de l’embrayage en ce qui concerne ces caractéristiques, il faut monter l’embrayage en utilisant l’outil spécifique avant de procéder à l’insertion du volant. Voir le schéma ci-contre.  Lors du montage du système d’embrayage, il faut faire très attention aux possibles erreurs susceptibles de se produire et qui risqueraient d’endommager le CCSC, en entraînant la perte de validité de la garantie du fabricant.](_raw/web-images/71b0410dd99fa919.jpg)

- Enfoncer la pédale d’embrayage

- Ouvrir le purgeur

- Maintenir la pédale d'embrayage enfoncée jusqu’à ce que le liquide apparaisse - Ne pas la relâcher !

- Fermer le purgeur

- Relâcher lentement la pédale d'embrayage

- Sous peine de perdre la garantie, de les communiquer par écrit au fabricant et au distributeur dans les soixante jours suivant leur découverte ; l’utilisateur devra aussi fournir une description du défaut rencontré sur le Produit ou sur les pièces restituées ainsi qu’une preuve d’achat de l’utilisateur d’origine identifiant tant le Produit que la date d’achat (qu’il ait été acheté au détail ou vendu par un distributeur comme partie de l’installation du Produit) ;

- D’expédier le Produit considéré défectueux à la société Brembo S.p.A. à son siège sis à via Brembo 25 -24035 Curno (BG) - Italie, par le biais de la chaîne de distribution.

- Les dommages au Produit causés, en partie ou totalement, par une mauvaise utilisation, un accident, un incendie, de la corrosion chimique, une utilisation à des fins autres que celles prévues, une utilisation illicite, un emploi sur un modèle différent de celui prévu, une installation erronée, une installation contraire aux indications du Fabricant ou un manque d’entretien du Produit selon les prescriptions du Fabricant indiquées dans les instructions fournies ;

- Les réclamations liées au confort, à la présence de bruits, de vibrations ou de fluidité limitée dans la conduite.

- Utiliser des moyens appropriés pour éviter d’inhaler les poussières soulevées pendant le nettoyage des pièces.

- Toujours porter des gants lors de l’opération de démontage et de remontage des composants présentant des arêtes coupantes.

- Éviter le contact direct de la peau avec le matériau de friction des plaquettes et mâchoires parce que cela risque de provoquer des abrasions.

- Ne pas introduire les mains dans le logement des plaquettes lorsque les pistons de l’étrier sont déposés en utilisant de l’air comprimé, parce que cela comporte un risque de d’écrasement des mains.

- Éviter tout contact direct avec le liquide de frein parce que cela peut irriter la peau et les yeux. En cas de contact accidentel, nettoyer soigneusement selon les indications fournies par le constructeur du véhicule ou le fabricant du liquide de frein.

- Ne pas soumettre les composants électriques à des charges électrostatiques et à des chocs susceptibles d’endommager les pièces en plastique .

- Protéger les composants électriques démontés contre l’humidité.

- S’assurer que tous les contacts électriques sont branchés correctement , en vérifiant que les témoins de signalisation s’allument. Si ce n'est pas le cas, le dysfonctionnement des témoins de signalisation peut provoquer une efficacité réduite du système de freinage ou le dysfonctionnement des indicateurs de freinage.

- Éviter le contact de graisse et autres lubrifiants avec les surfaces de freinage du disque, du tambour, des plaquettes et des mâchoires parce que cela risque de rendre le système de freinage inefficace et de provoquer de graves dommages physiques.

- Ne pas utiliser d'outils tranchants pour poser les composants en caoutchouc, car cela pourrait les endommager. Veiller à remplacer toutes les pièces endommagées

<!-- materialized-from-db web/e598f5f6d678 2026-03-28 -->
### Instructions pour remplacer le... - Montage auto - section-1

# Instructions pour remplacer le... - Montage auto

- Skip to main content Skip to menu Skip to footer Partager sur Instructions pour remplacer le cylindre émetteur d'embrayage et le maître-cylindre Nous vous conseillons de lire et de suivre attentivement les instructions fournies. Vous trouverez les mêmes instructions dans l’emballage des maîtres-cylindres. N’oubliez pas de les conserver pendant toute la durée de vie du produit. En cas de passage de propriété, elles devront être remises au nouveau propriétaire du véhicule. Indications générales 1. Utiliser le liquide de frein recommandé par le constructeur. 2. Le liquide de frein doit être complètement remplacé après que le réservoir a été soigneusement lavé avec de l'alcool isopropylique ou dénaturé. 3. À cause de la nature technique du produit, les cylindres émetteurs d'embrayage et le maître-cylindre doivent être remplacés par un technicien qualifié et, en cas de réclamation, il faudra le démontrer à l’aide d'une facture. 4. De nombreux véhicules plus récents sont équipés d’un cylindre esclave concentrique qui est monté à l'intérieur du logement de la cloche de boîte de vitesses. Afin de remplacer cette unité, la boîte de vitesses doit être déposée. 5. Certains de ces cylindres esclaves concentriques ont un tuyau d’alimentation et un tuyau de purge et purger ces systèmes est normalement simple. D’autres ont un seul tuyau d'alimentation avec des branchements de tuyaux extérieurs où le système est purgé. Ceux-ci peuvent être difficiles à purger, nous vous conseillons de suivre attentivement les procédures du fabricant. 6. Sur certains des nouveaux systèmes, le tuyau qui relie le cylindre émetteur d’embrayage au maître-cylindre est maintenu en place dans les cylindres à l’aide d’un clip et il est scellé avec un petit joint torique. Veiller à ce que ces tuyaux soient correctement montés pour éviter les fuites. 7. À présent, sur certains véhicules, les cylindres émetteurs d’embrayage sont montés à l’intérieur du véhicule et il est important de suivre les procédures correctes pour les déposer parce qu’il pourrait être nécessaire de déposer ou de desserrer des éléments critiques comme la colonne de direction. Procédure de remplacement 1. Soulever le véhicule et le soutenir en utilisant des supports spécifiques. 2. Déposer la moulure du compartiment de pieds en suivant les lignes directrices du constructeur du véhicule. 3. Débrancher le tuyau du cylindre, sceller le trou avec un bouchon en caoutchouc pour éviter que le fluide ne sorte. 4. Déposer le maître-cylindre ou le cylindre émetteur d'embrayage en suivant les lignes directrices du constructeur du véhicule. 5. Faire attention au diamètre/dimension du piston lors du remplacement du cylindre. Procédure de montage 1. Remplacer en même temps le cylindre émetteur d'embrayage et le maître-cylindre. 2. Installer les cylindres conformément aux instructions du constructeur du véhicule. 3. S’assurer que le maître-cylindre d’embrayage est parfaitement aligné et sûr pour empêcher de pousser la tige de poussée dans le cylindre coudé. 4. Brancher le tuyau. 5. Serrer les vis et les écrous à un couple approprié. 6. Vidanger le liquide de frein. 7. Purger l'embrayage. 8. Actionner plusieurs fois la pédale d'embrayage. 9. Vérifier le niveau du liquide de frein et si nécessaire, faire l’appoint, puis fermer le bouchon. 10. Vérifier s’il y a des fuites dans le système. 11. Contrôler la position de la pédale et la régler si nécessaire. 12. Assembler à nouveau la moulure du compartiment de pieds en suivant les lignes directrices du constructeur du véhicule. 13. Effectuer un essai sur route et contrôler la fonction de frein et d’embrayage. Informations générales et de sécurité Le produit Brembo a été conçu pour respecter les meilleurs standards de sécurité. Les Produits ne doivent pas être destinés à une utilisation différente de celle pour laquelle ils ont été conçus et fabriqués. L’utilisation à d’autres fins, la modification ou la manipulation du produit risquent d’altérer son fonctionnement et de compromettre sa sécurité. Toute modification éventuelle ou toute utilisation impropre rendent nulles les Limitations de garantie et peuvent rendre la personne utilisant le Produit dans ces conditions responsable quant aux dommages physiques ou matériels éventuellement causés à des tiers. Dans ces instructions, lorsqu’il est indiqué « DANGER! », cela signifie que le non-respect de la procédure indiquée a de fortes probabilités de provoquer de graves dommages physiques ou même la mort. La mention « ATTENTION! » indique une procédure dont le non-respect peut provoquer des dommages physiques , alors que la mention « AVERTISSEMENT! » indique une procédure dont le non-respect peut provoquer des dommages au véhicule. DANGER! Avant de commencer la procédure de remplacement, s’assurer que la pièce de rechange est adaptée à la marque et au modèle du véhicule . Le Produit revêt une importance fondamentale pour la sécurité du véhicule sur lequel il est installé et il doit, donc, être installé par du personnel qualifié ayant reçu une formation adéquate ou possédant suffisamment d’expérience dans l’installation et dans l’utilisation prévue du Produit. L’installateur doit avoir à sa disposition l’ outillage adéquat à l’installation et posséder des connaissances et une expérience appropriées pour s’occuper de l’entretien du véhicule. Une installation inadéquate ou erronée, due au non-respect de ces instructions ou autres, rendra nulles les Limitations de garantie et pourrait rendre l’installateur responsable quant aux dommages physiques ou matériels éventuellement provoqués. Il est fondamental de remplacer les disques de frein pour chaque essieu, en les prélevant de leur emballage. À chaque remplacement des disques, remplacer aussi leurs plaquettes. Éviter le contact de graisse et autres lubrifiants avec les surfaces de freinage du disque et des plaquettes parce que cela risque de rendre le système de freinage inefficace. Brembo décline toute responsabilité en cas de dommage matériel ou physique provoqué à ou par une personne conduisant un véhicule sur lequel le produit aurait été installé de façon inappropriée. ATTENTION! Les pièces remplacées doivent être éliminées selon les dispositions prescrites par la loi. Il est important d’éviter de frapper violemment ou d’endommager le Produit et ses composants, parce que cela risquerait de réduire son efficacité et de provoquer des dysfonctionnements. Si nécessaire, remplacer les composants endommagés. Pour éviter tout dommage

[...]
