---
category: tableau-de-bord
slug: cable-de-compteur-de-vitesse
title: Câble de compteur de vitesse
pg_id: 1150
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
  last_enriched_by: script:rag-fill-remaining-gaps
  last_enriched_at: '2026-03-28'
domain:
  role: Transmettre mecaniquement la rotation des roues au compteur de vitesse du tableau de bord via un cable flexible (courant
    de Foucault)
  must_be_true:
  - transmettre la rotation au compteur
  - relier la transmission au tableau de bord
  - permettre l'affichage de la vitesse
  must_not_contain:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  - capteur electronique
  related_parts:
  - compteur-de-vitesse
  - boite-de-vitesses
  - tableau-de-bord
  confusion_with:
  - piece: capteur-impulsion
    difference: Le capteur d'impulsion est electronique (signal ABS/ESP). Le cable de compteur est mecanique (rotation physique).
      Les vehicules modernes utilisent le capteur, les anciens le cable.
selection:
  criteria:
  - Marque de votre vehicule
  - Modele de votre vehicule
  - Annee de votre vehicule
  - Longueur du cable (variable selon modele)
  - Type d'embout cote transmission (carre, hexagonal)
  - Type d'embout cote compteur
  - Gaine rigide ou souple
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ Ne pas confondre cable de compteur mecanique et capteur de vitesse electronique
  - ❌ Verifier la longueur exacte du cable avant commande
  - ❌ Ne pas forcer l'embout lors du montage (risque de casse)
  cost_range:
    min: 8
    max: 60
    currency: EUR
    unit: l'unite
    source: fourchette constatee equipementiers
  checklist:
  - Verifier si votre vehicule utilise un cable mecanique ou un capteur electronique
  - Mesurer la longueur du cable d'origine
  - Verifier le type d'embout cote transmission
  - Verifier le type d'embout cote compteur
  - Commander la bonne longueur de gaine
  brands:
    premium:
    - Elring
    - Victor Reinz
    standard:
    - Febi
    - Ajusa
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Compteur de vitesse bloque a zero
    severity: securite
  - id: S2
    label: Aiguille du compteur qui saute ou tremble
    severity: confort
  - id: S3
    label: Bruit de grincement derriere le tableau de bord
    severity: confort
  - id: S4
    label: Lecture de vitesse erronee (trop haute ou trop basse)
    severity: securite
  - id: S5
    label: Compteur kilometrique qui ne tourne plus
    severity: confort
  causes:
  - Cable casse ou effiloche a l'interieur de la gaine
  - Embout use ou arrondi (ne s'accroche plus)
  - Gaine pliee ou ecrasee empechant la rotation
  - Manque de lubrification du cable dans la gaine
  depose_steps: []
  quick_checks:
  - 'Observer : compteur de vitesse bloque a zero ?'
  - 'Observer : aiguille du compteur qui saute ou tremble ?'
  - Bruit de grincement derriere le tableau de bord ?
  - 'Observer : lecture de vitesse erronee (trop haute ou trop basse) ?'
maintenance:
  interval:
    value: selon etat
    unit: condition
    note: Pas de periodicite fixe. Remplacer en cas de panne compteur, bruit ou lecture erronee. Piece typique des vehicules
      anciens (avant 2000).
    source: null
  cross_gammes:
  - capteur-impulsion
  brands:
    equivalent:
    - Cofle
    - Valeo
    budget:
    - Febi
    - JP Group
  wear_signs:
  - Compteur de vitesse bloque a zero
  - Aiguille du compteur qui saute ou tremble
  - Bruit de grincement derriere le tableau de bord
  - Lecture de vitesse erronee (trop haute ou trop basse)
  - Compteur kilometrique qui ne tourne plus
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '1150'
  intro_title: A quoi sert le cable de compteur de vitesse ?
  risk_title: Pourquoi remplacer le cable de compteur a temps ?
  risk_explanation: Un cable defaillant empeche l'affichage correct de la vitesse, ce qui compromet la securite routiere et
    peut entrainer un echec au controle technique.
  risk_consequences:
  - Impossibilite de connaitre sa vitesse reelle (risque d'exces de vitesse)
  - Compteur kilometrique bloque (impact revente et CT)
  - Bruit de grincement permanent derriere le tableau de bord
  risk_conclusion: Le remplacement est simple et peu couteux. Ne pas rouler sans compteur fonctionnel.
  arguments:
  - content: Selection guidee par vehicule et longueur de cable.
    icon: check-circle
    title: Compatibilite verifiee
  - content: Un compteur en panne est un motif de refus au controle technique.
    icon: shield-check
    title: Controle technique
  - content: Piece peu couteuse, remplacement rapide.
    icon: clock
    title: Intervention rapide
  - content: Verifiez si votre vehicule utilise un cable ou un capteur electronique.
    icon: list-check
    title: Verification prealable
  faq:
  - question: Mon vehicule a-t-il un cable ou un capteur electronique ?
    answer: Les vehicules avant 1995-2000 utilisent generalement un cable mecanique. Les vehicules modernes utilisent un capteur
      electronique (capteur d'impulsion). Verifiez sous le tableau de bord ou pres de la boite de vitesses.
  - question: Comment savoir si le cable est casse ?
    answer: Compteur bloque a zero, aiguille immobile meme en roulant, bruit de grincement au tableau de bord. Debrancher
      le cable cote compteur et le faire tourner a la main pour verifier.
  - question: Faut-il lubrifier le cable de compteur ?
    answer: Oui, un cable sec grince et s'use plus vite. Utiliser de la graisse legere ou du lubrifiant silicone dans la gaine
      lors du remplacement.
  - question: Quel est le prix d'un cable de compteur ?
    answer: Entre 8 et 60 EUR selon le vehicule. Le remplacement prend generalement 30 minutes a 1 heure.
  quality:
    score: 76
    source: manual-from-db-2026-03-21
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
doc_id: a97b57f0-8a5f-5ede-badb-e235413e3858
content_hash: sha256:25247fd8c9f93202
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
  area: Sur le vehicule (position variable selon modele)
  access: Consulter la revue technique du vehicule
  adjacent_parts:
  - pieces adjacentes du meme systeme
installation:
  difficulty: variable
  time: consulter revue technique
  tools:
  - outillage standard
  prerequisite: Consulter la procedure constructeur
---

# Câble de compteur de vitesse - Guide Diagnostic et Achat

## Fonction et Role

Le cable de compteur de vitesse (ou cable kilometrique) transmet mecaniquement la rotation des roues au compteur du tableau de bord. Il fonctionne par le principe du courant de Foucault : la rotation des roues entraine un plateau aimante via le cable, et la vitesse de rotation est refletee sur le tachymetre.

**Actions principales:** transmettre la rotation, afficher la vitesse, permettre le controle du vehicule

## Symptomes de Defaillance

### 🔴 Symptomes Critiques (Securite)

- **Compteur bloque a zero** — impossible de connaitre sa vitesse reelle
- **Lecture erronee** — vitesse affichee trop haute ou trop basse

### 🟢 Autres Symptomes

- Aiguille qui saute ou tremble
- Bruit de grincement derriere le tableau de bord
- Compteur kilometrique qui ne tourne plus


## Entretien et Intervalles

- **Intervalle** : selon etat
- Pas de periodicite fixe. Remplacer en cas de panne compteur, bruit ou lecture erronee. Piece typique des vehicules anciens (avant 2000).

## Causes Probables

- **Cable casse** — le fil interieur est rompu dans la gaine
- **Embout use** — l'embout carre ou hexagonal est arrondi, ne s'accroche plus
- **Gaine ecrasee** — pliure empechant la libre rotation du cable
- **Manque de lubrification** — cable sec provoquant grincement et usure acceleree

## Pieces Associees

- **capteur-impulsion** — alternative electronique sur vehicules modernes

## Criteres de Compatibilite

- **Marque, modele et annee** de votre vehicule
- **Longueur exacte** du cable (variable selon modele)
- **Type d'embout** cote transmission et cote compteur
- **Cable mecanique ou capteur electronique** (verifier avant commande)

## ❌ Attention aux Erreurs Frequentes

- ❌ Ne pas confondre cable mecanique et capteur electronique
- ❌ Verifier la longueur exacte avant commande
- ❌ Ne pas forcer l'embout lors du montage
- ❌ Lubrifier le cable neuf avant installation

## FAQ

**Mon vehicule a-t-il un cable ou un capteur electronique ?**
Les vehicules avant 1995-2000 utilisent generalement un cable mecanique. Les vehicules modernes utilisent un capteur electronique (capteur d'impulsion). Verifiez sous le tableau de bord ou pres de la boite de vitesses.

**Comment savoir si le cable est casse ?**
Compteur bloque a zero, aiguille immobile meme en roulant, bruit de grincement au tableau de bord. Debrancher le cable cote compteur et le faire tourner a la main pour verifier.

**Faut-il lubrifier le cable de compteur ?**
Oui, un cable sec grince et s'use plus vite. Utiliser de la graisse legere ou du lubrifiant silicone dans la gaine lors du remplacement.

**Quel est le prix d'un cable de compteur ?**
Entre 8 et 60 EUR selon le vehicule. Le remplacement prend generalement 30 minutes a 1 heure.
