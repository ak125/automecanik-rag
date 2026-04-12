---
category: embrayage
slug: guide-d-embrayage
title: Guide d'embrayage
pg_id: 4688
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-04-04'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:materialize-db-to-md
  last_enriched_at: '2026-04-04'
  v5_migrated_at: '2026-03-29'
domain:
  role: Guider l'arbre primaire dans le volant moteur
  must_be_true:
  - guider
  - centrer
  - positionner
  must_not_contain:
  - injection
  - freinage
  - climatisation
  - turbo
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - kit-d-embrayage
  - butee-d-embrayage
  - volant-moteur
  - emetteur-d-embrayage
  - recepteur-d-embrayage
  - cable-d-embrayage
  confusion_with:
  - term: piece-d-embrayage-voisine
    difference: Le systeme d embrayage comporte plusieurs pieces (disque, mecanisme, butee, emetteur, recepteur). Verifier
      laquelle est defectueuse.
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
  - ❌ "passage de vitesse parfait"
  cost_range:
    min: 10
    max: 40
    currency: EUR
    unit: l'unite
    source: estimation categorie
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
    label: Embrayage mal centre
    severity: confort
  - id: S2
    label: Vibrations au demarrage
    severity: confort
  - id: S3
    label: Usure prematuree du disque
    severity: confort
  causes:
  - verifier equilibrage et fixations
  - remplacement preventif recommande
  - 'vibrations anormales : verifier equilibrage et fixations'
  - 'kilometrage eleve ou usure visible : remplacement preventif recommande'
  quick_checks:
  - 'Observer : embrayage mal centre ?'
  - Vibrations au demarrage ?
  - 'Observer : usure prematuree du disque ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Embrayage mal centre
  - Vibrations au demarrage
  - Usure prematuree du disque
  good_practices:
  - Eviter de laisser le pied sur la pedale d embrayage au point mort
  - Remplacement du kit complet (disque + mecanisme + butee)
  - Purge du circuit hydraulique si recepteur/emetteur concerne
  - Verifier le volant moteur lors du remplacement d embrayage
rendering:
  pgId: '4688'
  intro_title: A quoi sert Guide d'embrayage ?
  risk_title: Pourquoi remplacer Guide d'embrayage a temps ?
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
  - question: Comment choisir Guide d'embrayage compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Guide d'embrayage ?
    answer: En cas de embrayage mal centre ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Guide d'embrayage sans verification atelier ?
    answer: Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure
      constructeur.
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
doc_id: 375169f9-addb-53d9-a472-99b0c6c125c9
content_hash: sha256:0cee63cbfe97edd5
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
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-04'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: hydraulique
    source_ref: corpus RAG web OEM
  - type: plein
    source_ref: corpus RAG web OEM
  - type: électrique
    source_ref: corpus RAG web OEM
  technical_notes:
    val_11_a: 11 a
    val_12_a: 12 a
    val_13_a: 13 a
    val_15__: 15 %
    val_2__: 2 %
    val_2_a: 2 a
    val_54__: 54 %
    val_6_a: 6 a
    val_8__: 8 %
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Guider l''arbre primaire dans le volant moteur. Pièces liées : vérifier les composants adjacents lors du remplacement.'
  S2: 'Intervalle : selon constructeur. Symptômes de défaillance : - Embrayage mal centre- Vibrations au demarrage- Usure
    prematuree du disque'
  S3: 'Pour choisir le bon guide d''embrayage pour votre véhicule : - Marque de votre véhicule- Modele de votre véhicule-
    Annee de votre véhicule- Marques : LuK, Sachs (premium), Valeo, Exedy (standard), Ridex (budget)- Budget : 10 à 40 EUR'
  S4_DEPOSE: 1. Débrancher la batterie. 2. Localiser la pièce selon la documentation constructeur. 3. Déconnecter les connecteurs
    électriques et raccords. 4. Dévisser les fixations de la pièce. 5. Déposer la pièce en notant l'orientation et la position
    de montage. 6. Nettoyer le logement et vérifier l'état des pièces adjacentes.
  S5: 'Erreurs fréquentes avec le guide d''embrayage : - Ne pas vérifier la référence exacte avant commande — une pièce de
    mauvaise référence ne fonctionne pas correctement même si elle se monte physiquement- Oublier de débrancher la batterie
    avant intervention — risque de court-circuit sur les composants électroniques- Ne pas respecter le couple de serrage constructeur
    au remontage- Ignorer les symptômes d''usure en espérant que ça passe — une défaillance progressive s''aggrave toujours-
    Ne pas effacer les codes défaut après remplacement — le calculateur peut rester en mode dégradé'
  S6: 'Après le remplacement du guide d''embrayage : - Eviter de laisser le pied sur la pedale d embrayage au point mort-
    Remplacement du kit complet (disque + mecanisme + butee)- Purge du circuit hydraulique si recepteur/emetteur concerne-
    Verifier le volant moteur lors du remplacement d embrayage- Effacer les codes défaut éventuels avec l''outil OBD- Effectuer
    un essai route pour confirmer la disparition des symptômes'
---

# Guide d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Guider l'arbre primaire dans le volant moteur

**Actions principales:** guider, centrer, positionner

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- embrayage mal centre
- vibrations au demarrage
- usure prematuree du disque

## Procédure de Diagnostic

Pour diagnostiquer un problème de guide d'embrayage:

1. **Inspection visuelle** - Examiner l'état du guide d'embrayage
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

- fourchette-d-embrayage
- tringle-de-vitesses

## Critères de Compatibilité

Pour commander le bon guide d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "passage de vitesse parfait"

## FAQ

**Comment choisir Guide d'embrayage compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Guide d'embrayage ?**
En cas de embrayage mal centre ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Guide d'embrayage sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
## Composants du kit

### Kit standard (3 pièces)
- **Disque d'embrayage** : La pièce d'usure principale, avec les garnitures de friction
- **Mécanisme (plateau de pression)** : Le diaphragme qui presse le disque contre le volant moteur
- **Butée de débrayage** : Le roulement qui actionne le mécanisme via la pédale

### Kit complet (4 pièces)
- Les 3 pièces du kit standard + **volant moteur** (bi-masse ou mono-masse)
- Recommandé si le volant moteur présente des signes d'usure (vibrations au ralenti, bruit de claquement)

## Signes d'usure

- **Patinage** : Le moteur monte en régime mais la voiture n'accélère pas proportionnellement. Le disque est usé.
- **Point de pédale haut** : La pédale d'embrayage mord très haut, signe d'usure avancée.
- **Vibrations en première** : Volant moteur bi-masse usé ou disque déformé.
- **Bruit de frottement** : Butée de débrayage usée (bruit quand on appuie sur la pédale).

## Bi-masse vs mono-masse

- **Volant bi-masse** : D'origine sur la plupart des voitures récentes (diesel surtout). Absorbe les vibrations du moteur. Plus cher au remplacement.
- **Volant mono-masse** : Conversion possible (kit Valeo, Sachs). Moins cher mais vibrations plus perceptibles au ralenti.
- **Conseil** : Rester en bi-masse si le véhicule est récent et confortable. Passer en mono-masse si le budget est serré.

## Marques recommandées

- **Valeo** : N°1 mondial de l'embrayage, OE pour PSA, Renault, et autres
- **Sachs (ZF)** : OE pour BMW, VW, Mercedes. Qualité premium.
- **LuK (Schaeffler)** : OE pour de nombreux constructeurs, inventeur du volant bi-masse

## Erreurs à éviter

- Ne jamais remplacer uniquement le disque sans le mécanisme (usure croisée)
- Toujours remplacer la butée avec le kit
- Vérifier l'état du volant moteur au démontage (jeu, rayures, points chauds)
- Ne pas oublier le guide de centrage pour l'alignement du disque

## FAQ

**Combien coûte un remplacement d'embrayage ?** Comptez 400-800€ en pièces + 300-600€ de main d'œuvre (4-8h selon le véhicule).

**Quelle durée de vie ?** 120 000-200 000 km selon la conduite. La conduite urbaine avec beaucoup de pédale réduit la durée de vie.

**Faut-il changer le volant moteur à chaque embrayage ?** Non, seulement s'il présente des signes d'usure (vibrations, jeu excessif, bruit). Vérifier systématiquement au démontage.
