---
category: accessoires
slug: retroviseur-exterieur
title: Rétroviseur extérieur
pg_id: 50
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-01'
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
  role: Permet la vision arrière et latérale
  must_be_true:
  - reflechir
  - montrer
  - permettre la vision
  must_not_contain:
  - injection
  - freinage
  - distribution
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - reflechir
  - montrer
  - permettre la vision
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
  - ❌ "meilleure visibilité garantie"
  cost_range:
    min: 50
    max: 200
    currency: EUR
    unit: coque complète
    source: catalogue automecanik
  brands:
    premium:
    - Magna Mirrors
    - Ficosa
    - SMR
    standard:
    - Hagus/DAPA
    - ALKAR
    - TYC
    budget:
    - VAN WEZEL
    - PRASCO
    - BLIC
  quality_tiers:
  - tier: Origine constructeur (OE/OES)
    description: Retroviseur identique a la premiere monte. Toutes les fonctions d'origine preservees (rabattage electrique,
      chauffant, camera, repetiteur).
  - tier: Equivalent OE (qualite premiere monte)
    description: Retroviseur de qualite equivalente. Fonctions principales conservees (reglage electrique, chauffant). Finition
      correcte.
  - tier: Adaptable (qualite atelier courant)
    description: Retroviseur compatible. Verifier la presence des fonctions requises (chauffant, repetiteur, rabattage) avant
      commande.
diagnostic:
  symptoms:
  - id: S1
    label: Miroir casse fissure ou decolle
    severity: confort
  - id: S2
    label: Coque de retroviseur cassee choc accrochage
    severity: confort
  - id: S3
    label: Reglage electrique inoperant ou lent
    severity: confort
  - id: S4
    label: Degivrage du miroir qui ne fonctionne plus
    severity: confort
  - id: S5
    label: Retroviseur rabattable bloque ou qui vibre
    severity: immobilisation
  - id: S6
    label: Repetiteur de clignotant integre grille
    severity: confort
  - id: S7
    label: Miroir fissure ebreche deformant image
    severity: confort
  - id: S8
    label: Bruit claquement vibration retroviseur vent
    severity: confort
  - id: S9
    label: Odeur plastique brule moteur electrique
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - verifier equilibrage et fixations
  quick_checks:
  - 'Observer : miroir casse fissure ou decolle ?'
  - 'Observer : coque de retroviseur cassee choc accrochage ?'
  - 'Observer : reglage electrique inoperant ou lent ?'
  - 'Observer : degivrage du miroir qui ne fonctionne plus ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Miroir casse fissure ou decolle
  - Coque de retroviseur cassee choc accrochage
  - Reglage electrique inoperant ou lent
  - Degivrage du miroir qui ne fonctionne plus
  - Retroviseur rabattable bloque ou qui vibre
  - Repetiteur de clignotant integre grille
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '50'
  intro_title: A quoi sert Rétroviseur extérieur ?
  risk_title: Pourquoi remplacer Rétroviseur extérieur a temps ?
  risk_explanation: '**Pièce HS** - Le rétroviseur extérieur peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le rétroviseur extérieur peut être hors service et nécessiter un remplacement'
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: Rétroviseur OE ou adaptable ?
    answer: Les rétroviseurs adaptables (Hagus, ALKAR, VAN WEZEL) sont de qualité correcte pour un usage courant. Pour un
      rétro avec nombreuses fonctions (rabattable, chauffant, caméra), l'OE est plus fiable.
  - question: Comment savoir si mon rétroviseur est HS ?
    answer: Miroir cassé ou décollé, coque fissurée, réglage électrique inopérant, dégivrage qui ne fonctionne plus, rabattage
      bloqué, répétiteur grillé.
  - question: Tous les combien changer le rétroviseur ?
    answer: Pas de périodicité. Le rétroviseur se change uniquement si cassé (choc, vandalisme) ou si le mécanisme électrique
      est défaillant.
  - question: Peut-on changer un rétroviseur soi-même ?
    answer: 'Oui. Pour le miroir seul : déclipser l''ancien, clipser le nouveau. Pour la coque complète : déposer le cache
      intérieur de portière, débrancher, dévisser. 15-45 min.'
  - question: Quelle erreur éviter avec le rétroviseur ?
    answer: Forcer sur un rétroviseur rabattable électrique bloqué. Le mécanisme interne est fragile et se casse facilement.
      Vérifiez d'abord le fusible et le connecteur.
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
doc_id: 6ef9fa0a-b808-5455-94f4-2aab050d1292
content_hash: sha256:8dfdef4372d8cc7d
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

# Rétroviseur extérieur - Guide Diagnostic Complet

## Fonction et Rôle

Permet la vision arrière et latérale

**Actions principales:** reflechir, montrer, permettre la vision

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Retroviseur rabattable bloque ou qui vibre**
  retroviseur rabattable bloque ou qui vibre

### 🟠 Symptômes de Dégâts Potentiels

- **Miroir casse fissure ou decolle**
  miroir casse fissure ou decolle
- **Coque de retroviseur cassee choc accrochage**
  coque de retroviseur cassee choc accrochage
- **Bruit claquement vibration retroviseur vent**
  bruit claquement vibration retroviseur vent

### 🟢 Autres Symptômes

- reglage electrique inoperant ou lent
- degivrage du miroir qui ne fonctionne plus
- repetiteur de clignotant integre grille
- miroir fissure ebreche deformant image
- odeur plastique brule moteur electrique

## Procédure de Diagnostic

Pour diagnostiquer un problème de rétroviseur extérieur:

1. **Inspection visuelle** - Examiner l'état du rétroviseur extérieur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le rétroviseur extérieur peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- bouton-de-retroviseur

## Critères de Compatibilité

Pour commander le bon rétroviseur extérieur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleure visibilité garantie"

## FAQ

**Rétroviseur OE ou adaptable ?**
Les rétroviseurs adaptables (Hagus, ALKAR, VAN WEZEL) sont de qualité correcte pour un usage courant. Pour un rétro avec nombreuses fonctions (rabattable, chauffant, caméra), l'OE est plus fiable.

**Comment savoir si mon rétroviseur est HS ?**
Miroir cassé ou décollé, coque fissurée, réglage électrique inopérant, dégivrage qui ne fonctionne plus, rabattage bloqué, répétiteur grillé.

**Tous les combien changer le rétroviseur ?**
Pas de périodicité. Le rétroviseur se change uniquement si cassé (choc, vandalisme) ou si le mécanisme électrique est défaillant.

**Peut-on changer un rétroviseur soi-même ?**
Oui. Pour le miroir seul : déclipser l'ancien, clipser le nouveau. Pour la coque complète : déposer le cache intérieur de portière, débrancher, dévisser. 15-45 min.

**Quelle erreur éviter avec le rétroviseur ?**
Forcer sur un rétroviseur rabattable électrique bloqué. Le mécanisme interne est fragile et se casse facilement. Vérifiez d'abord le fusible et le connecteur.
