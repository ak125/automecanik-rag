---
category: freinage
slug: pompe-a-vide-de-freinage
title: Pompe à vide de freinage
pg_id: 387
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-12'
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
  role: Assister l'effort du conducteur sur la pedale de frein
  must_be_true:
  - assister le freinage
  - reduire l'effort
  - fournir une depression
  must_not_contain:
  - friction
  - hydraulique directe
  - ABS
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - disque-de-frein
  - plaquette-de-frein
  - etrier-de-frein
  - flexible-de-frein
  - maitre-cylindre-de-frein
  - liquide-de-frein
  confusion_with:
  - term: piece-de-freinage-voisine
    difference: 'Verifier la reference exacte : les pieces de freinage se ressemblent mais ne sont pas interchangeables entre
      essieux ou types de montage.'
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
  - ❌ "freinage direct"
  cost_range:
    min: 15
    max: 200
    currency: EUR
    unit: l'unite
    source: estimation categorie
  brands:
    premium:
    - Brembo
    - ATE
    - TRW
    standard:
    - Bosch
    - Ferodo
    - Textar
    budget:
    - Ridex
    - Valeo
diagnostic:
  symptoms:
  - id: S1
    label: Pedale de frein tres dure
    severity: securite
  - id: S2
    label: Assistance au freinage defaillante
    severity: securite
  - id: S3
    label: Sifflement au niveau du moteur
    severity: confort
  - id: S4
    label: Voyant defaut frein allume
    severity: securite
  - id: S5
    label: Pedale dure surtout freinage depression
    severity: securite
  causes:
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  quick_checks:
  - 'Observer : pedale de frein tres dure ?'
  - 'Observer : assistance au freinage defaillante ?'
  - 'Observer : sifflement au niveau du moteur ?'
  - Voyant defaut frein allume ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Pedale de frein tres dure
  - Assistance au freinage defaillante
  - Sifflement au niveau du moteur
  - Voyant defaut frein allume
  - Pedale dure surtout freinage depression
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '387'
  intro_title: A quoi sert Pompe à vide de freinage ?
  risk_title: Pourquoi remplacer Pompe à vide de freinage a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: Tous les véhicules ont-ils une pompe à vide ?
    answer: Principalement les diesel et certains essence turbo. Les moteurs essence atmosphériques utilisent la dépression
      du collecteur d'admission.
  - question: Comment savoir si la pompe à vide est HS ?
    answer: Pédale de frein très dure, surtout après 2-3 freinages successifs. Un sifflement peut indiquer une fuite. Mesure
      au vacuomètre pour confirmer.
  - question: La pompe à vide est-elle critique pour la sécurité ?
    answer: Oui, sans elle le freinage nécessite beaucoup plus de force sur la pédale. Le freinage reste possible mais très
      pénible, surtout en urgence.
  - question: Quelles sont les erreurs fréquentes à éviter ?
    answer: Accuser la pompe alors que c'est une durite de dépression fissurée ou un clapet anti-retour du servo-frein. Ignorer
      la fuite d'huile qui contamine la dépression.
  - question: Comment faire un diagnostic rapide ?
    answer: Pédale dure + sifflement → fuite dépression/durite/clapet. Mesure vacuomètre < -0,6 bar au ralenti → pompe faible.
      Fuite d'huile autour pompe → joint/pompe à traiter rapidement.
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
doc_id: 898a4c30-a6a5-5bb3-961b-2430c4d537f0
content_hash: sha256:66875b662797be93
lang: fr
variants:
- name: Piece standard
  aliases:
  - standard
  - OE equivalent
  functional_differences:
  - Qualite equivalente a la monte d origine
  - Compatible avec la majorite des vehicules
- name: Piece performance/sport
  aliases:
  - sport
  - haute performance
  functional_differences:
  - Materiaux haute temperature
  - Pour usage intensif ou sportif
location_on_vehicle:
  area: Au niveau des roues (avant et/ou arriere)
  access: Demontage de la roue necessaire (cric + chandelle)
  adjacent_parts:
  - disque
  - plaquette
  - etrier
  - flexible
installation:
  difficulty: moyen
  time: 30min a 1h par essieu
  tools:
  - cle a douille
  - cle Allen
  - pied a coulisse
  - cle dynamometrique
  prerequisite: Vehicule sur chandelles, roue demontee
---

# Pompe à vide de freinage - Guide Diagnostic Complet

## Fonction et Rôle

Assister l'effort du conducteur sur la pedale de frein

**Actions principales:** assister le freinage, reduire l'effort, fournir une depression, creer le vide, alimenter le servofrein

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Pedale de frein tres dure**
  pedale de frein tres dure
- **Assistance au freinage defaillante**
  assistance au freinage defaillante
- **Voyant defaut frein allume**
  voyant defaut frein allume
- **Pedale dure surtout freinage depression**
  pedale dure surtout freinage depression

### 🟢 Autres Symptômes

- sifflement au niveau du moteur

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à vide de freinage:

1. **Inspection visuelle** - Examiner l'état du pompe à vide de freinage
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- maitre-cylindre-de-frein
- servo-frein

## Critères de Compatibilité

Pour commander le bon pompe à vide de freinage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "freinage direct"

## FAQ

**Tous les véhicules ont-ils une pompe à vide ?**
Principalement les diesel et certains essence turbo. Les moteurs essence atmosphériques utilisent la dépression du collecteur d'admission.

**Comment savoir si la pompe à vide est HS ?**
Pédale de frein très dure, surtout après 2-3 freinages successifs. Un sifflement peut indiquer une fuite. Mesure au vacuomètre pour confirmer.

**La pompe à vide est-elle critique pour la sécurité ?**
Oui, sans elle le freinage nécessite beaucoup plus de force sur la pédale. Le freinage reste possible mais très pénible, surtout en urgence.

**Quelles sont les erreurs fréquentes à éviter ?**
Accuser la pompe alors que c'est une durite de dépression fissurée ou un clapet anti-retour du servo-frein. Ignorer la fuite d'huile qui contamine la dépression.

**Comment faire un diagnostic rapide ?**
Pédale dure + sifflement → fuite dépression/durite/clapet. Mesure vacuomètre < -0,6 bar au ralenti → pompe faible. Fuite d'huile autour pompe → joint/pompe à traiter rapidement.
