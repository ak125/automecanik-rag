---
category: climatisation
slug: pressostat-de-climatisation
title: Pressostat de climatisation
pg_id: 1360
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-25'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v4_converted
  last_enriched_by: script:rag-enrich-metier-templates
  last_enriched_at: '2026-03-26'
domain:
  role: Mesurer la pression du fluide et proteger le compresseur
  must_be_true:
  - detecter
  - mesurer
  - proteger
  must_not_contain:
  - injection
  - freinage
  - allumage
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - compresseur-de-climatisation
  - condenseur-de-climatisation
  - evaporateur-de-climatisation
  - filtre-d-habitacle
  - detendeur-de-climatisation
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
  - ❌ "refroidit instantanement"
  cost_range:
    min: 200
    max: 800
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  brands:
    premium:
    - Delphi
    - Hella
    - Sanden
    - Denso
    standard:
    - NRF
    - Nissens
    - Valeo
    budget:
    - Thermotec
    - Frigair
    - Meat & Doria
  quality_tiers:
  - tier: Origine constructeur (OE/OES)
    description: Pressostat identique a celui monte en usine, fabrique par l'equipementier d'origine.
  - tier: Equivalent OE (qualite premiere monte)
    description: Pressostat de qualite identique a l'OE, fabrique par un equipementier reconnu mais sous sa propre marque.
  - tier: Adaptable (qualite atelier courant)
    description: Pressostat compatible de fabrication independante. Fonctionnement correct pour un usage courant.
diagnostic:
  symptoms:
  - id: S1
    label: Climatisation qui s arrete brutalement
    severity: confort
  - id: S2
    label: Compresseur qui ne demarre pas
    severity: immobilisation
  - id: S3
    label: Voyant de climatisation clignotant
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - lecture codes defaut obd et diagnostic electronique
  - 'vehicule immobilise ou symptome critique : verification urgente piece et alimentation'
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  quick_checks:
  - 'Observer : climatisation qui s arrete brutalement ?'
  - 'Observer : compresseur qui ne demarre pas ?'
  - Voyant de climatisation clignotant ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Climatisation qui s arrete brutalement
  - Compresseur qui ne demarre pas
  - Voyant de climatisation clignotant
  good_practices:
  - Faire tourner la climatisation 10 min par semaine meme en hiver
  - Remplacement du filtre d habitacle chaque annee
  - Recharge de gaz par un professionnel equipe (circuit sous pression)
  - Controle d etancheite si baisse de performance
rendering:
  pgId: '1360'
  intro_title: A quoi sert Pressostat de climatisation ?
  risk_title: Pourquoi remplacer Pressostat de climatisation a temps ?
  risk_explanation: '**Pièce HS** - Le pressostat de climatisation peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le pressostat de climatisation peut être hors service et nécessiter un remplacement'
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
  - question: Comment choisir Pressostat de climatisation compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Pressostat de climatisation ?
    answer: En cas de climatisation qui s arrete brutalement ou de degradation mesurable, il faut controler rapidement avant
      panne secondaire.
  - question: Puis-je monter Pressostat de climatisation sans verification atelier ?
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
doc_id: 6cfd6fde-ffb4-5f4b-a9a1-c10945044e83
content_hash: sha256:ad13da242766435d
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
  area: Face avant (condenseur), habitacle (evaporateur), moteur (compresseur)
  access: Variable selon composant (capot, tableau de bord, face avant)
  adjacent_parts:
  - compresseur
  - condenseur
  - detendeur
  - evaporateur
installation:
  difficulty: difficile (pro obligatoire)
  time: 1h a 4h
  tools:
  - station de recharge
  - detecteur de fuites
  - cle a douille
  prerequisite: Recuperation du gaz obligatoire par professionnel agree
---

# Pressostat de climatisation - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la pression du fluide et proteger le compresseur

**Actions principales:** detecter, mesurer, proteger

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Compresseur qui ne demarre pas**
  compresseur qui ne demarre pas

### 🟢 Autres Symptômes

- climatisation qui s arrete brutalement
- voyant de climatisation clignotant

## Procédure de Diagnostic

Pour diagnostiquer un problème de pressostat de climatisation:

1. **Inspection visuelle** - Examiner l'état du pressostat de climatisation
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le pressostat de climatisation peut être hors service et nécessiter un remplacement
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- conduite-de-climatisation

## Critères de Compatibilité

Pour commander le bon pressostat de climatisation, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidit instantanement"

## FAQ

**Comment choisir Pressostat de climatisation compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Pressostat de climatisation ?**
En cas de climatisation qui s arrete brutalement ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Pressostat de climatisation sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.


## Symptomes supplementaires

<!-- materialized-from-db diagnostic/climatisation.md 2026-02-15 -->
### Diagnostic - Climatisation et chauffage

# Climatisation et chauffage - Diagnostic complet

## Climatisation sans effet

### Pas de froid
- **Manque de gaz réfrigérant** : Fuite dans le circuit. Le compresseur ne s'enclenche pas ou tourne en continu sans refroidir. Recharge + recherche de fuite nécessaire.
- **Compresseur bloqué** : Embrayage de compresseur HS, bruit métallique, courroie qui patine.
- **Condenseur obstrué** : Débris, feuilles ou insectes devant le condenseur (devant le radiateur). Nettoyage au jet doux.
- **Détendeur bloqué** : Le gaz ne se détend plus correctement, givrage possible sur les tuyaux.

### Odeurs dans l'habitacle
- **Filtre habitacle encrassé** : Odeur de moisi à la mise en route de la ventilation. Remplacement tous les 15 000-20 000 km.
- **Évaporateur contaminé** : Bactéries et moisissures sur l'évaporateur. Traitement antibactérien recommandé.

## Chauffage défaillant

### Pas de chaleur
- **Niveau de liquide de refroidissement bas** : Le radiateur de chauffage n'est pas alimenté. Vérifier le niveau et faire l'appoint.
- **Thermostat bloqué ouvert** : Le moteur ne monte pas en température. L'aiguille reste basse même après 10 minutes de conduite.
- **Radiateur de chauffage bouché** : Les deux durites d'entrée/sortie doivent être chaudes moteur à température. Si une seule est chaude, le radiateur est obstrué.

### Ventilation faible
- **Résistance de ventilateur grillée** : Seule la vitesse maximale fonctionne, les autres vitesses sont inactives.
- **Moteur de ventilateur fatigué** : Bruit de frottement, débit d'air réduit.

## Quand consulter un professionnel

- Compresseur bruyant (risque de blocage et casse courroie)
- Fuite de gaz réfrigérant visible (traces d'huile sur les raccords)
- Odeur sucrée dans l'habitacle (fuite de liquide de refroidissement dans le radiateur de chauffage)
- Surchauffe moteur associée à un problème de chauffage
