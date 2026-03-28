---
category: transmission
slug: suspension-boite-vitesse-automatique
title: Suspension boite vitesse automatique
pg_id: 248
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-21'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: low
lifecycle:
  stage: v4_converted
  last_enriched_by: script:rag-enrich-metier-templates
  last_enriched_at: '2026-03-26'
domain:
  role: Absorber les vibrations et mouvements de la boite de vitesses automatique pour reduire les a-coups transmis a la caisse
  must_be_true:
  - absorber les vibrations
  - maintenir la boite en position
  - reduire les a-coups
  must_not_contain:
  - universel
  - tous modeles
  - adaptable tous
  confusion_with:
  - term: support-moteur
    difference: Le support moteur maintient le moteur, la suspension BVA maintient specifiquement la boite de vitesses automatique
  - term: suspension-boite-vitesse
    difference: La version manuelle peut avoir un support different, verifier la reference selon le type de boite
  related_parts:
  - support-moteur
  - cardan
  - joint-d-arbre-de-transmission
  - mecatronique-boite-automatique
selection:
  criteria:
  - Marque de votre vehicule
  - Modele de votre vehicule
  - Motorisation de votre vehicule
  - Annee de votre vehicule
  - Type de boite automatique (conventionnelle, DSG, CVT)
  - Position du support (superieur, inferieur, lateral)
  anti_mistakes:
  - universel
  - tous modeles
  - adaptable tous
  brands:
    premium:
    - SKF
    - GKN/Spidan
    standard:
    - Febi
    - Meyle
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Vibrations excessives au ralenti en position D ou R
    severity: confort
  - id: S2
    label: A-coups lors des passages de rapport
    severity: confort
  - id: S3
    label: Bruit sourd ou cognement en passant de P a D ou R
    severity: confort
  - id: S4
    label: Mouvement excessif du groupe motopropulseur a l'acceleration
    severity: securite
  - id: S5
    label: Caoutchouc du silent-bloc fissure ou affaisse
    severity: confort
  causes:
  - usure naturelle du caoutchouc (chaleur, vibrations, age)
  - fuite d'huile sur le support hydraulique
  - contraintes mecaniques excessives (conduite sportive)
  quick_checks:
  - Vibrations excessives au ralenti en position D ou R ?
  - 'Observer : a-coups lors des passages de rapport ?'
  - Bruit sourd ou cognement en passant de P a D ou R ?
  - 'Observer : mouvement excessif du groupe motopropulseur a l''acceleration ?'
maintenance:
  interval:
    value: selon etat
    unit: condition
    note: Verifier visuellement tous les 80000 km. Remplacer si caoutchouc fissure, affaisse ou decole.
  wear_signs:
  - Vibrations excessives au ralenti en position D ou R
  - A-coups lors des passages de rapport
  - Bruit sourd ou cognement en passant de P a D ou R
  - Mouvement excessif du groupe motopropulseur a l'acceleration
  - Caoutchouc du silent-bloc fissure ou affaisse
  good_practices:
  - Verifier le niveau d huile de boite selon preconisation constructeur
  - Controle des soufflets de protection (pas de fuite de graisse)
  - Remplacement de la bague d etancheite en cas de fuite
  - Inspection des cardans et croisillons a chaque revision
rendering:
  pgId: '248'
  faq:
  - question: Comment savoir si la suspension de BVA est HS ?
    answer: Vibrations au ralenti en D/R, bruit sourd au passage P vers D, mouvement excessif du moteur a l'acceleration.
      Inspection visuelle du silent-bloc (fissures, affaissement).
  - question: Peut-on rouler avec une suspension de BVA usee ?
    answer: Oui mais les vibrations s'aggravent et peuvent endommager les canalisations hydrauliques ou les cardans a terme.
  - question: Suspension BVA OE ou adaptable ?
    answer: Privilegier l'OE pour la duree de vie et la compatibilite exacte. Les generiques peuvent avoir une durete differente.
  - question: Combien coute le remplacement ?
    answer: La piece coute entre 30 et 200 EUR. La main d'oeuvre peut etre elevee si l'acces est difficile (1h a 3h).
  - question: Quelle erreur eviter ?
    answer: Ne pas confondre support moteur et support BVA (references differentes). Toujours verifier les 2 ou 3 supports
      du vehicule en meme temps.
  quality:
    score: 60
    source: manual:claude-r3-kp
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modeles
  - adaptable tous
  requires_vehicle: true
doc_id: 7c50d9b0-38e5-599d-bc2e-5203882fa706
content_hash: sha256:051ba7072c928e86
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
  area: Sous le vehicule, relie la boite aux roues
  access: Par le dessous (pont elevateur)
  adjacent_parts:
  - cardan
  - soufflet
  - roulement de roue
  - boite
installation:
  difficulty: difficile
  time: 1h a 3h
  tools:
  - pont elevateur
  - cle a douille
  - arrache-cardan
  prerequisite: Vidange huile de boite si cardan depose
---

# Suspension boite vitesse automatique - Guide Diagnostic

## Fonction et Role

Absorber les vibrations et mouvements de la boite de vitesses automatique.

## Symptomes de Defaillance

- Vibrations excessives au ralenti en position D ou R
- A-coups lors des passages de rapport
- Bruit sourd en passant de P a D ou R
- Mouvement excessif du groupe motopropulseur
- Caoutchouc du silent-bloc fissure ou affaisse

## Pieces Associees

- support-moteur
- cardan
- joint-d-arbre-de-transmission
- mecatronique-boite-automatique

## FAQ

**Comment savoir si la suspension de BVA est HS ?**
Vibrations au ralenti en D/R, bruit sourd au passage P vers D, mouvement excessif du moteur a l'acceleration. Inspection visuelle du silent-bloc (fissures, affaissement).

**Peut-on rouler avec une suspension de BVA usee ?**
Oui mais les vibrations s'aggravent et peuvent endommager les canalisations hydrauliques ou les cardans a terme.

**Suspension BVA OE ou adaptable ?**
Privilegier l'OE pour la duree de vie et la compatibilite exacte. Les generiques peuvent avoir une durete differente.

**Combien coute le remplacement ?**
La piece coute entre 30 et 200 EUR. La main d'oeuvre peut etre elevee si l'acces est difficile (1h a 3h).

**Quelle erreur eviter ?**
Ne pas confondre support moteur et support BVA (references differentes). Toujours verifier les 2 ou 3 supports du vehicule en meme temps.

## Entretien et Intervalles

- **Intervalle** : selon etat
- Verifier visuellement tous les 80000 km. Remplacer si caoutchouc fissure, affaisse ou decole.
