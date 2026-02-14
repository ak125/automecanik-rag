---
category: capteurs
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: voyant_tableau_bord_allume
  then: lecture_codes_defaut_obd_et_diagnostic_electronique
- if: kilometrage_eleve_ou_usure_visible
  then: remplacement_preventif_recommande
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - mesurer
  - detecter
  - transmettre
  must_not_contain_concepts:
  - electrovanne
  - modulateur
  - pompe abs
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Mesurer la vitesse de rotation de chaque roue et transmettre l'information
    au calculateur ABS
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "corrige la panne"
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
  - answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference
      exacte avant montage.
    question: Comment choisir Capteur ABS compatible avec mon vehicule ?
  - answer: En cas de voyant abs allume au tableau de bord ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Capteur ABS ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Capteur ABS sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Capteur ABS.
  id: 412
  intro:
    role: Mesurer la vitesse de rotation de chaque roue et transmettre l'information
      au calculateur ABS
    syncParts:
    - mesurer
    - detecter
    - transmettre
    title: A quoi sert Capteur ABS ?
  pgId: '412'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/capteur-abs.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Usure normale** - Après un certain kilométrage, le remplacement préventif
      est recommandé'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Capteur ABS a temps ?
  symptoms:
  - voyant abs allume au tableau de bord
  - code defaut specifique a une roue
  - capteur visible endommage ou couvert de crasse
  - cable du capteur coupe ou denude
  - abs qui se declenche a basse vitesse sans raison
  - bruit anormal lors du fonctionnement abs
  - freinage desequilibre avec abs actif
  - plus de 150 000 km sans verification capteurs
  - '**Voyant abs allume au tableau de bord**'
  - '**Abs qui se declenche a basse vitesse sans raison**'
  - '**Bruit anormal lors du fonctionnement abs**'
  - '**Freinage desequilibre avec abs actif**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 412
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: capteur-abs
source_type: gamme
symptoms:
- description: voyant abs allume au tableau de bord
  evidence:
  - 'Observation: voyant abs allume au tableau de bord'
  - Vérification visuelle ou auditive
  id: S1
  label: Voyant abs allume au tableau de bord
  risk_level: securite
- description: code defaut specifique a une roue
  evidence:
  - 'Observation: code defaut specifique a une roue'
  - Vérification visuelle ou auditive
  id: S2
  label: Code defaut specifique a une roue
  risk_level: confort
- description: capteur visible endommage ou couvert de crasse
  evidence:
  - 'Observation: capteur visible endommage ou couvert de crasse'
  - Vérification visuelle ou auditive
  id: S3
  label: Capteur visible endommage ou couvert de crasse
  risk_level: confort
- description: cable du capteur coupe ou denude
  evidence:
  - 'Observation: cable du capteur coupe ou denude'
  - Vérification visuelle ou auditive
  id: S4
  label: Cable du capteur coupe ou denude
  risk_level: confort
- description: abs qui se declenche a basse vitesse sans raison
  evidence:
  - 'Observation: abs qui se declenche a basse vitesse sans raison'
  - Vérification visuelle ou auditive
  id: S5
  label: Abs qui se declenche a basse vitesse sans raison
  risk_level: securite
- description: bruit anormal lors du fonctionnement abs
  evidence:
  - 'Observation: bruit anormal lors du fonctionnement abs'
  - Vérification visuelle ou auditive
  id: S6
  label: Bruit anormal lors du fonctionnement abs
  risk_level: securite
- description: freinage desequilibre avec abs actif
  evidence:
  - 'Observation: freinage desequilibre avec abs actif'
  - Vérification visuelle ou auditive
  id: S7
  label: Freinage desequilibre avec abs actif
  risk_level: securite
- description: plus de 150 000 km sans verification capteurs
  evidence:
  - 'Observation: plus de 150 000 km sans verification capteurs'
  - Vérification visuelle ou auditive
  id: S8
  label: Plus de 150 000 km sans verification capteurs
  risk_level: confort
title: Capteur ABS
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Capteur ABS - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la vitesse de rotation de chaque roue et transmettre l'information au calculateur ABS

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Voyant abs allume au tableau de bord**
  voyant abs allume au tableau de bord
- **Abs qui se declenche a basse vitesse sans raison**
  abs qui se declenche a basse vitesse sans raison
- **Bruit anormal lors du fonctionnement abs**
  bruit anormal lors du fonctionnement abs
- **Freinage desequilibre avec abs actif**
  freinage desequilibre avec abs actif

### 🟢 Autres Symptômes

- code defaut specifique a une roue
- capteur visible endommage ou couvert de crasse
- cable du capteur coupe ou denude
- plus de 150 000 km sans verification capteurs

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur abs:

1. **Inspection visuelle** - Examiner l'état du capteur abs
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- agregat-de-freinage
- cable-de-frein-a-main
- disque-de-frein
- etrier-de-frein
- kit-de-freins-arriere
- machoires-de-frein
- plaquette-de-frein
- roulement-de-roue

## Critères de Compatibilité

Pour commander le bon capteur abs, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "corrige la panne"