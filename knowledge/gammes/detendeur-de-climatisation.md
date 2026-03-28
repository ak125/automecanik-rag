---
category: climatisation
slug: detendeur-de-climatisation
title: Détendeur de climatisation
pg_id: 183
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
  role: Détend le fluide frigorigène avant l'évaporateur
  must_be_true:
  - detendre
  - reguler
  - abaisser la pression
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
  - ❌ "refroidit le moteur"
  cost_range:
    min: 50
    max: 150
    currency: EUR
    unit: détendeur
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
    description: Pièce identique à celle montée en usine, avec la même plage de régulation et les mêmes raccords. Recommandé
      pour les véhicules récents ou les climatisations sous garantie.
  - tier: Équivalent OE (équipementiers climatisation)
    description: Produit de fabricants spécialisés en composants de climatisation automobile. Tolérances identiques, compatible
      avec les fluides R134a et R1234yf selon modèle.
  - tier: Pièce adaptable
    description: Peut convenir sur des véhicules plus anciens. La compatibilité avec le type de fluide, la position de montage
      et le débit nominal doit être vérifiée avant commande.
  brands:
    premium:
    - Denso
    - Valeo
    standard:
    - NRF
    - Delphi
    - Hella
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Evaporateur qui givre anormalement
    severity: confort
  - id: S2
    label: Refroidissement irregulier chaud puis froid
    severity: confort
  - id: S3
    label: Sifflement ou bruit de detente audible
    severity: confort
  - id: S4
    label: Compresseur qui cycle en permanence
    severity: confort
  - id: S5
    label: Odeur de gaz refrigerant dans l habitacle
    severity: confort
  - id: S6
    label: Clim qui fonctionne puis s arrete brusquement
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : evaporateur qui givre anormalement'
  quick_checks:
  - 'Observer : evaporateur qui givre anormalement ?'
  - 'Observer : refroidissement irregulier chaud puis froid ?'
  - 'Observer : sifflement ou bruit de detente audible ?'
  - 'Observer : compresseur qui cycle en permanence ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Evaporateur qui givre anormalement
  - Refroidissement irregulier chaud puis froid
  - Sifflement ou bruit de detente audible
  - Compresseur qui cycle en permanence
  - Odeur de gaz refrigerant dans l habitacle
  - Clim qui fonctionne puis s arrete brusquement
  good_practices:
  - Faire tourner la climatisation 10 min par semaine meme en hiver
  - Remplacement du filtre d habitacle chaque annee
  - Recharge de gaz par un professionnel equipe (circuit sous pression)
  - Controle d etancheite si baisse de performance
rendering:
  pgId: '183'
  intro_title: A quoi sert Détendeur de climatisation ?
  risk_title: Pourquoi remplacer Détendeur de climatisation a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: Détendeur clim OE ou adaptable ?
    answer: Les détendeurs OES (Valeo, Denso) garantissent un débit calibré. Un détendeur mal calibré peut provoquer un givrage
      de l'évaporateur.
  - question: Comment savoir si le détendeur est HS ?
    answer: Clim qui givre puis s'arrête, refroidissement irrégulier (chaud/froid), sifflement au niveau du détendeur, évaporateur
      partiellement givré.
  - question: Tous les combien changer le détendeur ?
    answer: Pas de périodicité. Pièce rarement en panne sauf obstruction par impuretés. Changez-le si diagnostic confirmé.
  - question: Peut-on changer le détendeur soi-même ?
    answer: Possible mais nécessite la récupération du gaz et une recharge. L'accès est souvent difficile (boîtier de ventilation).
  - question: Quelle erreur éviter avec le détendeur ?
    answer: Ne pas confondre un détendeur bouché avec un manque de gaz. Vérifier la pression HP et BP avant remplacement.
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
doc_id: ec1fed8c-3160-574f-af9d-559487c84df9
content_hash: sha256:81fad23642f8f8fa
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

# Détendeur de climatisation - Guide Diagnostic Complet

## Fonction et Rôle

Détend le fluide frigorigène avant l'évaporateur

**Actions principales:** detendre, reguler, abaisser la pression

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- evaporateur qui givre anormalement
- refroidissement irregulier chaud puis froid
- sifflement ou bruit de detente audible
- compresseur qui cycle en permanence
- odeur de gaz refrigerant dans l habitacle
- clim qui fonctionne puis s arrete brusquement

## Procédure de Diagnostic

Pour diagnostiquer un problème de détendeur de climatisation:

1. **Inspection visuelle** - Examiner l'état du détendeur de climatisation
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bouteille-deshydratante
- commande-de-ventilation
- compresseur-de-climatisation
- condenseur-de-climatisation
- evaporateur-de-climatisation
- filtre-d-habitacle

## Critères de Compatibilité

Pour commander le bon détendeur de climatisation, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidit le moteur"

## FAQ

**Détendeur clim OE ou adaptable ?**
Les détendeurs OES (Valeo, Denso) garantissent un débit calibré. Un détendeur mal calibré peut provoquer un givrage de l'évaporateur.

**Comment savoir si le détendeur est HS ?**
Clim qui givre puis s'arrête, refroidissement irrégulier (chaud/froid), sifflement au niveau du détendeur, évaporateur partiellement givré.

**Tous les combien changer le détendeur ?**
Pas de périodicité. Pièce rarement en panne sauf obstruction par impuretés. Changez-le si diagnostic confirmé.

**Peut-on changer le détendeur soi-même ?**
Possible mais nécessite la récupération du gaz et une recharge. L'accès est souvent difficile (boîtier de ventilation).

**Quelle erreur éviter avec le détendeur ?**
Ne pas confondre un détendeur bouché avec un manque de gaz. Vérifier la pression HP et BP avant remplacement.


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
