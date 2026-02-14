---
category: moteur
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
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
  - transmettre
  - actionner
  - amortir
  must_not_contain_concepts:
  - culbuteur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Transmettre le mouvement de l'arbre a cames aux soupapes
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "repare le moteur"
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
    question: Comment choisir Poussoir de soupape compatible avec mon vehicule ?
  - answer: En cas de claquement metallique au ralenti a froid ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Poussoir de soupape ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Poussoir de soupape sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de moteur pour confirmer Poussoir de soupape.
  id: 1216
  intro:
    role: Poussoir de soupape intervient directement sur moteur du vehicule. Un choix
      conforme protege la combustion et limite les pannes secondaires.
    syncParts:
    - transmettre
    - actionner
    - amortir
    title: A quoi sert Poussoir de soupape ?
  pgId: '1216'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - MISSING_REQUIRED_TERMS
    - TOO_SHORT
    score: 60
    source: reindex:gammes/poussoir-de-soupape.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Usure normale** - Après un certain kilométrage, le remplacement préventif
      est recommandé'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Poussoir de soupape a temps ?
  symptoms:
  - claquement metallique au ralenti a froid
  - bruit de tac-tac au niveau de la culasse
  - claquement qui persiste meme a chaud
  - bruit qui s amplifie avec le regime moteur
  - perte de puissance legere jeu excessif
  - plus de 150 000 km et claquement recurrent
  - '**Claquement metallique au ralenti a froid**'
  - '**Claquement qui persiste meme a chaud**'
  - '**Plus de 150 000 km et claquement recurrent**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 1216
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: poussoir-de-soupape
source_type: gamme
symptoms:
- description: claquement metallique au ralenti a froid
  evidence:
  - 'Observation: claquement metallique au ralenti a froid'
  - Vérification visuelle ou auditive
  id: S1
  label: Claquement metallique au ralenti a froid
  risk_level: degats_volant_moteur
- description: bruit de tac-tac au niveau de la culasse
  evidence:
  - 'Observation: bruit de tac-tac au niveau de la culasse'
  - Vérification visuelle ou auditive
  id: S2
  label: Bruit de tac-tac au niveau de la culasse
  risk_level: confort
- description: claquement qui persiste meme a chaud
  evidence:
  - 'Observation: claquement qui persiste meme a chaud'
  - Vérification visuelle ou auditive
  id: S3
  label: Claquement qui persiste meme a chaud
  risk_level: degats_volant_moteur
- description: bruit qui s amplifie avec le regime moteur
  evidence:
  - 'Observation: bruit qui s amplifie avec le regime moteur'
  - Vérification visuelle ou auditive
  id: S4
  label: Bruit qui s amplifie avec le regime moteur
  risk_level: confort
- description: perte de puissance legere jeu excessif
  evidence:
  - 'Observation: perte de puissance legere jeu excessif'
  - Vérification visuelle ou auditive
  id: S5
  label: Perte de puissance legere jeu excessif
  risk_level: confort
- description: plus de 150 000 km et claquement recurrent
  evidence:
  - 'Observation: plus de 150 000 km et claquement recurrent'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 150 000 km et claquement recurrent
  risk_level: degats_volant_moteur
title: Poussoir de soupape
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Poussoir de soupape - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre le mouvement de l'arbre a cames aux soupapes

**Actions principales:** transmettre, actionner, amortir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement metallique au ralenti a froid**
  claquement metallique au ralenti a froid
- **Claquement qui persiste meme a chaud**
  claquement qui persiste meme a chaud
- **Plus de 150 000 km et claquement recurrent**
  plus de 150 000 km et claquement recurrent

### 🟢 Autres Symptômes

- bruit de tac-tac au niveau de la culasse
- bruit qui s amplifie avec le regime moteur
- perte de puissance legere jeu excessif

## Procédure de Diagnostic

Pour diagnostiquer un problème de poussoir de soupape:

1. **Inspection visuelle** - Examiner l'état du poussoir de soupape
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- joint-de-cache-culbuteurs
- joint-de-collecteur
- joint-de-culasse
- soupape-d-admission
- soupape-d-echappement

## Critères de Compatibilité

Pour commander le bon poussoir de soupape, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"