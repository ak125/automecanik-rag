---
category: distribution
slug: galet-enrouleur-de-courroie-de-distribution
title: Galet enrouleur de courroie de distribution
pg_id: 313
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
  role: Guider la courroie de distribution dans son parcours
  must_be_true:
  - guider
  - enrouler
  - positionner
  must_not_contain:
  - freinage
  - climatisation
  - turbo
  - injection
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - courroie-de-distribution
  - kit-de-distribution
  - galet-tendeur-de-courroie-de-distribution
  - pompe-a-eau
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
  - ❌ "synchronisation parfaite"
  cost_range:
    min: 20
    max: 60
    currency: EUR
    unit: galet seul
    source: catalogue automecanik
  quality_tiers:
  - tier: Qualité Origine (OE)
    description: Galets enrouleurs de distribution livrés en première monte. Roulement haute précision conçu pour résister
      aux contraintes thermiques et mécaniques du circuit de distribution.
  - tier: Équivalent Qualité Origine
    description: Galets produits aux mêmes spécifications dimensionnelles et de charge que les pièces OE. Roulement scellé,
      poulie usinée avec précision.
  - tier: Adaptable Économique
    description: Galets de remplacement aux dimensions compatibles. Conviennent pour un usage courant. Contrôler diamètres
      et épaisseur avant montage.
  brands:
    premium:
    - Gates
    - Continental/Contitech
    standard:
    - Dayco
    - SKF
    - INA
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Bruit de roulement au ralenti
    severity: confort
  - id: S2
    label: Sifflement cote distribution
    severity: confort
  - id: S3
    label: Traces d usure anormale sur la courroie
    severity: confort
  - id: S4
    label: Galet qui tourne difficilement a la main
    severity: confort
  - id: S5
    label: Jeu radial ou axial dans le galet
    severity: confort
  - id: S6
    label: Bruit metallique leger
    severity: confort
  - id: S7
    label: Courroie qui se deporte sur le cote
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - remplacement preventif recommande
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'kilometrage eleve ou usure visible : remplacement preventif recommande'
  depose_steps:
  - Deposer les caches et protections pour acceder au circuit de distribution
  - Reperer les calages de distribution (piger vilebrequin et arbre a cames)
  - Detendre le galet tendeur pour liberer la courroie de distribution
  - Devisser la fixation centrale du galet enrouleur (vis unique, cle de 13 ou 15)
  - Installer le nouveau galet, serrer au couple preconise (25-35 Nm)
  - Remettre la courroie en respectant le sens et les reperes de calage
  - Tourner le moteur manuellement sur 2 tours pour verifier le calage
  quick_checks:
  - Bruit de roulement au ralenti ?
  - 'Observer : sifflement cote distribution ?'
  - 'Observer : traces d usure anormale sur la courroie ?'
  - 'Observer : galet qui tourne difficilement a la main ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Bruit de roulement au ralenti
  - Sifflement cote distribution
  - Traces d usure anormale sur la courroie
  - Galet qui tourne difficilement a la main
  - Jeu radial ou axial dans le galet
  - Bruit metallique leger
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '313'
  intro_title: A quoi sert Galet enrouleur de courroie de distribution ?
  risk_title: Pourquoi remplacer Galet enrouleur de courroie de distribution a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
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
  - question: Quelle différence avec le galet tendeur ?
    answer: L'enrouleur guide la courroie, le tendeur la maintient en tension. Les deux sont nécessaires et se changent ensemble.
  - question: Comment vérifier l'état du galet ?
    answer: 'Faites-le tourner à la main : il doit tourner librement, sans bruit ni à-coups. Vérifiez qu''il n''y a pas de
      jeu.'
  - question: Peut-on réutiliser un galet en bon état ?
    answer: Déconseillé. Les roulements s'usent avec le temps même s'ils semblent bons. Le coût du galet est faible par rapport
      au risque.
  - question: Quelles sont les erreurs fréquentes à éviter ?
    answer: Juger le galet "bon" sur son apparence. Oublier de le changer avec la courroie. Monter un galet générique de mauvaise
      qualité.
  - question: Comment faire un diagnostic rapide ?
    answer: Galet qui gratte/grince à la main → remplacement. Jeu dans le roulement → remplacement. Courroie qui s'use d'un
      côté → galet suspect.
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
doc_id: ce9a9b7f-f3c1-52f8-84bd-f48ab15a3f72
content_hash: sha256:245de33f7c942533
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
  area: Face laterale du moteur, derriere le carter de distribution
  access: Depose courroie accessoire + carter distribution
  adjacent_parts:
  - courroie
  - galets
  - pompe a eau
  - poulie
installation:
  difficulty: difficile (pro recommande)
  time: 3h a 6h
  tools:
  - kit calage distribution
  - cle dynamometrique
  - extracteur poulie
  prerequisite: Moteur cale au PMH, ne pas tourner le moteur sans courroie
---

# Galet enrouleur de courroie de distribution - Guide Diagnostic Complet

## Fonction et Rôle

Guider la courroie de distribution dans son parcours

**Actions principales:** guider, enrouler, positionner

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit metallique leger**
  bruit metallique leger

### 🟢 Autres Symptômes

- bruit de roulement au ralenti
- sifflement cote distribution
- traces d usure anormale sur la courroie
- galet qui tourne difficilement a la main
- jeu radial ou axial dans le galet
- courroie qui se deporte sur le cote

## Procédure de Diagnostic

Pour diagnostiquer un problème de galet enrouleur de courroie de distribution:

1. **Inspection visuelle** - Examiner l'état du galet enrouleur de courroie de distribution
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-de-distribution

## Critères de Compatibilité

Pour commander le bon galet enrouleur de courroie de distribution, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "synchronisation parfaite"

## FAQ

**Quelle différence avec le galet tendeur ?**
L'enrouleur guide la courroie, le tendeur la maintient en tension. Les deux sont nécessaires et se changent ensemble.

**Comment vérifier l'état du galet ?**
Faites-le tourner à la main : il doit tourner librement, sans bruit ni à-coups. Vérifiez qu'il n'y a pas de jeu.

**Peut-on réutiliser un galet en bon état ?**
Déconseillé. Les roulements s'usent avec le temps même s'ils semblent bons. Le coût du galet est faible par rapport au risque.

**Quelles sont les erreurs fréquentes à éviter ?**
Juger le galet "bon" sur son apparence. Oublier de le changer avec la courroie. Monter un galet générique de mauvaise qualité.

**Comment faire un diagnostic rapide ?**
Galet qui gratte/grince à la main → remplacement. Jeu dans le roulement → remplacement. Courroie qui s'use d'un côté → galet suspect.


## Symptomes supplementaires

<!-- materialized-from-db diagnostic/distribution-courroie.md 2026-01-08 -->
### Diagnostic - Distribution et courroie

# Distribution et courroie - Diagnostic complet

## Symptomes courants

### Bruit de claquement moteur
- **Quand** : Au ralenti ou a l'acceleration
- **Caracteristique** : Claquement rythmique, lie au regime moteur

### Sifflement au demarrage
- **Quand** : A froid, disparait a chaud
- **Caracteristique** : Son aigu type courroie patinante

### Perte de puissance
- **Quand** : En acceleration
- **Caracteristique** : Moteur qui "tire" moins

### Temoin moteur allume
- **Quand** : Aleatoire
- **Caracteristique** : Voyant orange fixe

## Causes possibles et solutions

### 1. Courroie de distribution usee
- **Probabilite** : 40%
- **Verification** : Age/kilometrage, aspect visuel (fissures, effilochage)
- **Solution** : Remplacement kit distribution complet
- **Pieces** : Kit distribution (courroie, galets, pompe a eau)
- **Urgence** : CRITIQUE - Risque casse moteur

### 2. Galet tendeur defaillant
- **Probabilite** : 25%
- **Verification** : Jeu excessif, bruit de roulement
- **Solution** : Remplacement galet(s)
- **Pieces** : Galet tendeur, galet enrouleur
- **Urgence** : Haute

### 3. Pompe a eau HS
- **Probabilite** : 20%
- **Verification** : Fuite liquide de refroidissement, jeu axial
- **Solution** : Remplacement pompe a eau
- **Pieces** : Pompe a eau
- **Urgence** : Haute

### 4. Courroie accessoires usee
- **Probabilite** : 15%
- **Verification** : Fissures, patinage
- **Solution** : Remplacement courroie accessoires
- **Pieces** : Courroie poly-V, galet tendeur accessoires
- **Urgence** : Moyenne

## Intervalles de remplacement

| Type moteur | Intervalle | Kilometrage |
|-------------|------------|-------------|
| Essence | 5 ans | 100 000 km |
| Diesel | 5 ans | 120 000 km |
| HDI/TDI | 4 ans | 160 000 km |

## Recommandations

- **Remplacement preventif** : Respecter les preconisations constructeur
- **Kit complet** : Toujours remplacer courroie + galets + pompe a eau ensemble
- **Marques** : Privilegier Gates, Continental, SKF
- **Huile** : Verifier absence de fuites d'huile sur la courroie
