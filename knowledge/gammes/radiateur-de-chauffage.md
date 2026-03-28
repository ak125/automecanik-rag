---
category: refroidissement
slug: radiateur-de-chauffage
title: Radiateur de chauffage
pg_id: 467
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
  role: Transferer la chaleur du liquide de refroidissement vers l'habitacle pour le confort des passagers. NE REFROIDIT PAS
    LE MOTEUR!
  must_be_true:
  - chauffer
  - transferer
  - diffuser
  must_not_contain:
  - refroidissement moteur
  - ventilateur moteur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - radiateur-de-refroidissement
  - pompe-a-eau
  - thermostat
  - durite-de-refroidissement
  - vase-d-expansion
  - ventilateur-de-refroidissement
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
    max: 200
    currency: EUR
    unit: radiateur
    source: catalogue automecanik
  brands:
    premium:
    - Valeo
    - Behr/Mahle
    - Denso
    standard:
    - Nissens
    - NRF
    - Hella
    budget:
    - Thermotec
    - Frigair
    - AVA
  quality_tiers:
  - tier: Origine constructeur (OE/OES)
    description: Radiateur de chauffage identique a la premiere monte. Echange thermique optimal, dimensions et raccords conformes.
  - tier: Equivalent OE (qualite premiere monte)
    description: Radiateur de chauffage de qualite equivalente, teste en pression. Dimensions et raccords verifies.
  - tier: Adaptable (qualite atelier courant)
    description: Radiateur compatible. Verifier les dimensions exactes et le type de raccords avant commande.
diagnostic:
  symptoms:
  - id: S1
    label: Buee grasse persistante sur le pare-brise
    severity: confort
  - id: S2
    label: Odeur sucree de liquide dans l habitacle
    severity: confort
  - id: S3
    label: Moquette humide cote passager avant
    severity: confort
  - id: S4
    label: Chauffage qui ne chauffe plus ou peu
    severity: confort
  - id: S5
    label: Gargouillement dans le tableau de bord
    severity: confort
  - id: S6
    label: Plus de 15 ans ou fuite averee
    severity: confort
  causes:
  - identifier origine fuite et verifier joints
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  - 'Usure ou defaillance causant : buee grasse persistante sur le pare-brise'
  quick_checks:
  - 'Observer : buee grasse persistante sur le pare-brise ?'
  - Odeur sucree de liquide dans l habitacle ?
  - 'Observer : moquette humide cote passager avant ?'
  - 'Observer : chauffage qui ne chauffe plus ou peu ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Buee grasse persistante sur le pare-brise
  - Odeur sucree de liquide dans l habitacle
  - Moquette humide cote passager avant
  - Chauffage qui ne chauffe plus ou peu
  - Gargouillement dans le tableau de bord
  - Plus de 15 ans ou fuite averee
  good_practices:
  - Controle du niveau de liquide de refroidissement a froid chaque mois
  - Remplacement du liquide selon preconisation constructeur (2-5 ans)
  - Verification des durites et colliers a chaque revision
  - Purge du circuit apres toute intervention sur le refroidissement
rendering:
  pgId: '467'
  intro_title: A quoi sert Radiateur de chauffage ?
  risk_title: Pourquoi remplacer Radiateur de chauffage a temps ?
  risk_explanation: '**Défaillance progressive** - Usure normale due à l''utilisation'
  risk_consequences:
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
  - question: Radiateur chauffage OE ou adaptable ?
    answer: Les radiateurs OES (Valeo, Behr, Nissens) garantissent un échange thermique optimal. Les adaptables peuvent convenir
      mais vérifiez les dimensions exactes.
  - question: Comment savoir si mon radiateur de chauffage fuit ?
    answer: Buée grasse sur le pare-brise, odeur sucrée dans l'habitacle, moquette humide côté passager, niveau de liquide
      qui baisse.
  - question: Tous les combien changer le radiateur de chauffage ?
    answer: Pas de périodicité. Durée de vie 10 à 15 ans. À remplacer uniquement en cas de fuite ou d'obstruction.
  - question: Peut-on changer le radiateur de chauffage soi-même ?
    answer: Difficile. Accès complexe nécessitant souvent la dépose du tableau de bord. Intervention réservée aux bricoleurs
      expérimentés.
  - question: Quelle erreur éviter avec le radiateur de chauffage ?
    answer: Ne pas négliger une petite fuite qui s'aggravera. Rincer le circuit avant montage pour éviter d'obstruer le nouveau
      radiateur.
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
doc_id: 9b8b5373-18bb-5759-ba64-8786d636438a
content_hash: sha256:b2f969a6f5990300
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
  area: Face avant du vehicule (radiateur) et bloc moteur
  access: Par le dessus (capot) ou face avant
  adjacent_parts:
  - radiateur
  - durites
  - pompe a eau
  - thermostat
installation:
  difficulty: moyen
  time: 30min a 2h
  tools:
  - tournevis
  - pince de serrage
  - bac de recuperation
  prerequisite: Moteur froid, circuit vidange avant depose
---

# Radiateur de chauffage - Guide Diagnostic Complet

## Fonction et Rôle

Transferer la chaleur du liquide de refroidissement vers l'habitacle pour le confort des passagers. NE REFROIDIT PAS LE MOTEUR!

**Actions principales:** chauffer, transferer, diffuser, rechauffer l'habitacle

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- buee grasse persistante sur le pare-brise
- odeur sucree de liquide dans l habitacle
- moquette humide cote passager avant
- chauffage qui ne chauffe plus ou peu
- gargouillement dans le tableau de bord
- plus de 15 ans ou fuite averee

## Procédure de Diagnostic

Pour diagnostiquer un problème de radiateur de chauffage:

1. **Inspection visuelle** - Examiner l'état du radiateur de chauffage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- commande-de-ventilation
- filtre-d-habitacle
- pulseur-d-air-d-habitacle
- radiateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon radiateur de chauffage, vous devez connaître:

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

**Radiateur chauffage OE ou adaptable ?**
Les radiateurs OES (Valeo, Behr, Nissens) garantissent un échange thermique optimal. Les adaptables peuvent convenir mais vérifiez les dimensions exactes.

**Comment savoir si mon radiateur de chauffage fuit ?**
Buée grasse sur le pare-brise, odeur sucrée dans l'habitacle, moquette humide côté passager, niveau de liquide qui baisse.

**Tous les combien changer le radiateur de chauffage ?**
Pas de périodicité. Durée de vie 10 à 15 ans. À remplacer uniquement en cas de fuite ou d'obstruction.

**Peut-on changer le radiateur de chauffage soi-même ?**
Difficile. Accès complexe nécessitant souvent la dépose du tableau de bord. Intervention réservée aux bricoleurs expérimentés.

**Quelle erreur éviter avec le radiateur de chauffage ?**
Ne pas négliger une petite fuite qui s'aggravera. Rincer le circuit avant montage pour éviter d'obstruer le nouveau radiateur.


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
