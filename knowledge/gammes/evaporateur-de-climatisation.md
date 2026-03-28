---
category: climatisation
slug: evaporateur-de-climatisation
title: Evaporateur de climatisation
pg_id: 471
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
  last_enriched_by: script:rag-fill-remaining-gaps
  last_enriched_at: '2026-03-28'
domain:
  role: Absorbe la chaleur de l'air habitacle pour produire du froid - Circuit habitacle uniquement
  must_be_true:
  - absorber la chaleur
  must_not_contain:
  - moteur
  - refroidissement
  - radiateur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - compresseur-de-climatisation
  - condenseur-de-climatisation
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
    min: 100
    max: 400
    currency: EUR
    unit: l'unite
    source: estimation categorie
  quality_tiers:
  - tier: Pièce OE (Origine Équipement)
    description: Évaporateur identique à l origine. Surface d échange optimale, traitement anti-corrosion conforme. Compatible
      raccords et boîtier de soufflage d origine.
  - tier: Équivalent OE (spécialistes échangeurs thermiques)
    description: 'Fabricants d échangeurs de rang 1 fournissant les constructeurs. Deux grandes familles techniques : évaporateur
      type MS (ailette intérieure entre plaques, circuit complexe) et tubes multivoies.'
  - tier: Générique compatible
    description: Peut convenir si les dimensions et raccords sont strictement conformes. Vérifier la surface d échange et
      le traitement anti-corrosion.
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
    label: Climatisation inefficace malgre recharge recente
    severity: confort
  - id: S2
    label: Odeur de moisi ou d humidite a la ventilation
    severity: confort
  - id: S3
    label: Buee persistante sur le pare-brise en mode clim
    severity: confort
  - id: S4
    label: Flaque d eau anormale sous le tableau de bord
    severity: confort
  - id: S5
    label: Bruit gargouillement boitier ventilation
    severity: confort
  - id: S6
    label: Mauvaises odeurs des l enclenchement de la clim
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : climatisation inefficace malgre recharge recente'
  depose_steps: []
  quick_checks:
  - 'Observer : climatisation inefficace malgre recharge recente ?'
  - Odeur de moisi ou d humidite a la ventilation ?
  - 'Observer : buee persistante sur le pare-brise en mode clim ?'
  - 'Observer : flaque d eau anormale sous le tableau de bord ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Climatisation inefficace malgre recharge recente
  - Odeur de moisi ou d humidite a la ventilation
  - Buee persistante sur le pare-brise en mode clim
  - Flaque d eau anormale sous le tableau de bord
  - Bruit gargouillement boitier ventilation
  - Mauvaises odeurs des l enclenchement de la clim
  good_practices:
  - Faire tourner la climatisation 10 min par semaine meme en hiver
  - Remplacement du filtre d habitacle chaque annee
  - Recharge de gaz par un professionnel equipe (circuit sous pression)
  - Controle d etancheite si baisse de performance
rendering:
  pgId: '471'
  intro_title: A quoi sert Evaporateur de climatisation ?
  risk_title: Pourquoi remplacer Evaporateur de climatisation a temps ?
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
  - question: Evaporateur clim OE ou adaptable ?
    answer: Les évaporateurs OES (Valeo, Denso, Nissens) garantissent une surface d'échange optimale. Les adaptables moins
      chers peuvent être moins efficaces.
  - question: Comment savoir si mon évaporateur fuit ?
    answer: Clim qui ne refroidit plus, buée sur le pare-brise en mode clim, odeur d'humidité ou de moisi, flaque d'eau sous
      le tableau de bord.
  - question: Tous les combien changer l'évaporateur ?
    answer: Pas de périodicité. Durée de vie 10 à 15 ans. Nettoyage antibactérien annuel recommandé pour éviter l'encrassement.
  - question: Peut-on nettoyer l'évaporateur sans le démonter ?
    answer: Oui, avec un nettoyant mousse via les conduits de ventilation. Efficace pour les mauvaises odeurs mais pas pour
      les fuites.
  - question: Quelle erreur éviter avec l'évaporateur ?
    answer: Ne pas négliger les mauvaises odeurs (moisissures sur l'évaporateur). Remplacer aussi le filtre d'habitacle encrassé.
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
doc_id: 190aa91d-7f5a-5adb-af09-ec5e39aae00d
content_hash: sha256:a54b85a18dcd4fbe
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

# Evaporateur de climatisation - Guide Diagnostic Complet

## Fonction et Rôle

Absorbe la chaleur de l'air habitacle pour produire du froid - Circuit habitacle uniquement

**Actions principales:** absorber la chaleur

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- climatisation inefficace malgre recharge recente
- odeur de moisi ou d humidite a la ventilation
- buee persistante sur le pare-brise en mode clim
- flaque d eau anormale sous le tableau de bord
- bruit gargouillement boitier ventilation
- mauvaises odeurs des l enclenchement de la clim

## Procédure de Diagnostic

Pour diagnostiquer un problème de evaporateur de climatisation:

1. **Inspection visuelle** - Examiner l'état du evaporateur de climatisation
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

- compresseur-de-climatisation
- condenseur-de-climatisation
- detendeur-de-climatisation
- filtre-d-habitacle
- pulseur-d-air-d-habitacle

## Critères de Compatibilité

Pour commander le bon evaporateur de climatisation, vous devez connaître:

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

**Evaporateur clim OE ou adaptable ?**
Les évaporateurs OES (Valeo, Denso, Nissens) garantissent une surface d'échange optimale. Les adaptables moins chers peuvent être moins efficaces.

**Comment savoir si mon évaporateur fuit ?**
Clim qui ne refroidit plus, buée sur le pare-brise en mode clim, odeur d'humidité ou de moisi, flaque d'eau sous le tableau de bord.

**Tous les combien changer l'évaporateur ?**
Pas de périodicité. Durée de vie 10 à 15 ans. Nettoyage antibactérien annuel recommandé pour éviter l'encrassement.

**Peut-on nettoyer l'évaporateur sans le démonter ?**
Oui, avec un nettoyant mousse via les conduits de ventilation. Efficace pour les mauvaises odeurs mais pas pour les fuites.

**Quelle erreur éviter avec l'évaporateur ?**
Ne pas négliger les mauvaises odeurs (moisissures sur l'évaporateur). Remplacer aussi le filtre d'habitacle encrassé.


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
