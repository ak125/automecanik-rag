---
category: climatisation
slug: condenseur-de-climatisation
title: Condenseur de climatisation
pg_id: 448
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
  role: Dissipe la chaleur du fluide frigorigene comprime - Distinct du radiateur moteur
  must_be_true:
  - dissiper la chaleur
  must_not_contain:
  - radiateur moteur
  - refroidissement
  - eau
  - liquide
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - compresseur-de-climatisation
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
  - ❌ "refroidit le moteur"
  cost_range:
    min: 42
    max: 195
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Pièce OE (Origine Équipement)
    description: Condenseur identique à l origine. Surface d échange et revêtement conformes aux spécifications constructeur.
  - tier: Équivalent OE (fournisseurs de rang 1)
    description: Fabricants spécialisés dans les échangeurs thermiques automobiles. Qualité garantie, prix compétitif.
  - tier: Condenseur générique
    description: Peut présenter moins d ailettes qu un condenseur OE, réduisant l efficacité de refroidissement du circuit.
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
    label: Climatisation moins efficace qu avant
    severity: confort
  - id: S2
    label: Recharges de gaz frequentes necessaires
    severity: confort
  - id: S3
    label: Traces d huile verdatre sur le condenseur
    severity: confort
  - id: S4
    label: Condenseur visiblement deforme ou perce
    severity: confort
  - id: S5
    label: Odeur de gaz refrigerant a l avant
    severity: confort
  - id: S6
    label: Choc frontal recent meme leger
    severity: confort
  - id: S7
    label: Bruit ventilateur condenseur tourne permanence
    severity: confort
  - id: S8
    label: Climatisation inefficace temps chaud embouteillages
    severity: confort
  - id: S9
    label: Plus controle circuit climatisation preventif
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  depose_steps: []
  quick_checks:
  - 'Observer : climatisation moins efficace qu avant ?'
  - 'Observer : recharges de gaz frequentes necessaires ?'
  - 'Observer : traces d huile verdatre sur le condenseur ?'
  - 'Observer : condenseur visiblement deforme ou perce ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Climatisation moins efficace qu avant
  - Recharges de gaz frequentes necessaires
  - Traces d huile verdatre sur le condenseur
  - Condenseur visiblement deforme ou perce
  - Odeur de gaz refrigerant a l avant
  - Choc frontal recent meme leger
  good_practices:
  - Faire tourner la climatisation 10 min par semaine meme en hiver
  - Remplacement du filtre d habitacle chaque annee
  - Recharge de gaz par un professionnel equipe (circuit sous pression)
  - Controle d etancheite si baisse de performance
rendering:
  pgId: '448'
  intro_title: A quoi sert Condenseur de climatisation ?
  risk_title: Pourquoi remplacer Condenseur de climatisation a temps ?
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
  - question: Condenseur clim OE ou adaptable ?
    answer: Les condenseurs OES (Nissens, Valeo, NRF) garantissent un rendement optimal. Les adaptables peuvent avoir moins
      d'ailettes et refroidir moins bien.
  - question: Comment savoir si mon condenseur fuit ?
    answer: Clim qui perd en efficacité progressivement, traces d'huile sur le condenseur, test UV positif, recharges fréquentes
      nécessaires.
  - question: Tous les combien changer le condenseur ?
    answer: Pas de périodicité. À remplacer si percé ou corrodé. Vérifier après tout choc frontal.
  - question: Peut-on réparer un condenseur percé ?
    answer: Non recommandé. Une soudure tiendra rarement sous la pression du circuit (15-20 bars). Remplacement obligatoire.
  - question: Quelle erreur éviter avec le condenseur ?
    answer: Ne pas monter un condenseur sans rincer le circuit si l'ancien a projeté des débris. Vérifier l'état des supports.
  quality:
    score: 60
    source: script:rag-upgrade-v4
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
doc_id: 63f68560-0a53-568e-b1a1-52405665bae0
content_hash: sha256:998f58edb314f9df
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

# Condenseur de climatisation - Guide Diagnostic Complet

## Fonction et Rôle

Dissipe la chaleur du fluide frigorigene comprime - Distinct du radiateur moteur

**Actions principales:** dissiper la chaleur

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- climatisation moins efficace qu avant
- recharges de gaz frequentes necessaires
- traces d huile verdatre sur le condenseur
- condenseur visiblement deforme ou perce
- odeur de gaz refrigerant a l avant
- choc frontal recent meme leger

## Procédure de Diagnostic

Pour diagnostiquer un problème de condenseur de climatisation:

1. **Inspection visuelle** - Examiner l'état du condenseur de climatisation
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
- detendeur-de-climatisation
- evaporateur-de-climatisation
- filtre-d-habitacle
- pulseur-d-air-d-habitacle

## Critères de Compatibilité

Pour commander le bon condenseur de climatisation, vous devez connaître:

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

**Condenseur clim OE ou adaptable ?**
Les condenseurs OES (Nissens, Valeo, NRF) garantissent un rendement optimal. Les adaptables peuvent avoir moins d'ailettes et refroidir moins bien.

**Comment savoir si mon condenseur fuit ?**
Clim qui perd en efficacité progressivement, traces d'huile sur le condenseur, test UV positif, recharges fréquentes nécessaires.

**Tous les combien changer le condenseur ?**
Pas de périodicité. À remplacer si percé ou corrodé. Vérifier après tout choc frontal.

**Peut-on réparer un condenseur percé ?**
Non recommandé. Une soudure tiendra rarement sous la pression du circuit (15-20 bars). Remplacement obligatoire.

**Quelle erreur éviter avec le condenseur ?**
Ne pas monter un condenseur sans rincer le circuit si l'ancien a projeté des débris. Vérifier l'état des supports.


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
