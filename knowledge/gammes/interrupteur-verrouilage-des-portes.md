---
category: accessoires
slug: interrupteur-verrouilage-des-portes
title: Interrupteur verrouilage des portes
pg_id: 864
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-04-04'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:materialize-db-to-md
  last_enriched_at: '2026-04-04'
  v5_migrated_at: '2026-03-29'
domain:
  role: Commande le verrouillage/déverrouillage centralisé des portes
  must_be_true:
  - commander
  - activer
  - verrouiller
  must_not_contain:
  - serrure
  - cle
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - commander
  - activer
  - verrouiller
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
  - ❌ "securite garantie"
  cost_range:
    min: 50
    max: 300
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Qualité Origine (OE)
    description: Interrupteurs de verrouillage centralisé fournis en première monte. Contact fiable, intégration parfaite
      dans le panneau de porte, rétroéclairage conforme.
  - tier: Équivalent Qualité Origine
    description: Interrupteurs fabriqués aux mêmes dimensions et avec le même brochage que l'OE. Toucher et course du bouton
      conformes.
  - tier: Adaptable Économique
    description: Interrupteurs de remplacement compatibles. Vérifier le nombre de broches, le type de clip et la position
      gauche/droite avant commande.
  brands:
    premium:
    - Stabilus
    - Valeo
    standard:
    - Febi
    - Meyle
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Centralisation qui ne repond plus
    severity: confort
  - id: S2
    label: Une porte ne se verrouille pas
    severity: confort
  - id: S3
    label: Verrouillage deverrouillage intempestif
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : centralisation qui ne repond plus'
  quick_checks:
  - 'Observer : centralisation qui ne repond plus ?'
  - 'Observer : une porte ne se verrouille pas ?'
  - 'Observer : verrouillage deverrouillage intempestif ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Centralisation qui ne repond plus
  - Porte ne se verrouille pas
  - Verrouillage deverrouillage intempestif
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '864'
  intro_title: A quoi sert Interrupteur verrouilage des portes ?
  risk_title: Pourquoi remplacer Interrupteur verrouilage des portes a temps ?
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
  - question: Comment choisir Interrupteur verrouilage des portes compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Interrupteur verrouilage des portes ?
    answer: En cas de centralisation qui ne repond plus ou de degradation mesurable, il faut controler rapidement avant panne
      secondaire.
  - question: Puis-je monter Interrupteur verrouilage des portes sans verification atelier ?
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
doc_id: 850f99dd-668d-5add-9078-edc32fc72376
content_hash: sha256:6a67daf5e38a04e3
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
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-04'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: plein
    source_ref: corpus RAG web OEM
  - type: électrique
    source_ref: corpus RAG web OEM
  technical_notes:
    norme_iso_9995: ISO 9995
    val_18_a: 18 a
    val_3_a: 3 a
    val_5_v: 5 V
    val_60__: 60 %
    val_90__: 90 %
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'L''interrupteur de verrouillage des portes est le commutateur électrique intégré dans la porte du conducteur (et parfois
    du passager avant) qui permet de commander le système de centralisation du véhicule. Une simple pression sur ce bouton
    envoie un signal électrique au boîtier de centralisation (UCH, BSI ou module de confort selon les constructeurs), qui
    active simultanément les actuateurs de toutes les portes pour verrouiller ou déverrouiller l''ensemble des serrures.Ce
    composant est au cœur du système de fermeture centralisée. Il traduit une commande manuelle (pression sur le bouton) en
    signal électrique qui déclenche l''action des moteurs de centralisation présents dans chaque porte. Sur les véhicules
    modernes, ce signal transite souvent par un bus de communication (LIN ou CAN) vers le boîtier de confort avant d''être
    redistribué aux actuateurs. Sur les architectures plus anciennes, le signal est directement câblé entre l''interrupteur
    et les relais de centralisation.La serrure de chaque porte et le moteur de centralisation sont les composants directement
    pilotés par ce système. Une défaillance de l''interrupteur ne bloque pas physiquement les serrures : celles-ci restent
    actionnables manuellement ou par la télécommande. En revanche, la commande centrale depuis l''habitacle n''est plus disponible,
    ce qui peut être source d''inconfort et d''insécurité.'
  S2: 'L''interrupteur de verrouillage est un composant à contact mécanique soumis à de nombreuses sollicitations quotidiennes.
    Son usure est progressive et se manifeste de plusieurs façons :- Centralisation qui ne répond plus : appuyer sur le bouton
    de verrouillage n''entraîne aucune réaction des serrures. Les portes ne se verrouillent ni ne se déverrouillent depuis
    l''interrupteur de la porte, même si la télécommande fonctionne encore.- Une porte ne se verrouille pas : seule une porte
    ou un groupe de portes ne répond pas à la commande. Cela peut venir de l''interrupteur de la porte concernée ou d''un
    moteur de centralisation défaillant sur cette porte.- Verrouillage ou déverrouillage intempestif : les serrures se déclenchent
    sans action sur le bouton, parfois de façon répétée. Un contact électrique intermittent dans l''interrupteur usé peut
    générer des faux signaux vers le boîtier de confort.- Bouton qui reste enfoncé ou dur à actionner : le mécanisme interne
    du bouton est grippé ou le ressort de rappel est cassé. Le bouton ne revient plus à sa position initiale après la pression.-
    Fonctionnement aléatoire selon la température : l''interrupteur fonctionne par temps chaud mais plus par temps froid,
    ou inversement. Ce comportement indique un contact électrique fragilisé qui perd sa conduction sous l''effet des variations
    thermiques.- Voyant de diagnostic ou message d''alerte au tableau de bord : sur les véhicules récents avec boîtier de
    confort (BSI/UCH), un court- circuit ou une absence de signal sur la ligne de l''interrupteur peut générer un code défaut
    et allumer un voyant.'
  S3: 'L''interrupteur de verrouillage des portes est intégré dans un panneau de commandes de porte qui regroupe souvent plusieurs
    fonctions (vitres, rétroviseurs, centralisation). Il existe en pièce individuelle ou en combiné avec d''autres commandes
    selon le véhicule. Voici les critères de sélection :- Marque et modèle du véhicule : les boutons de porte sont spécifiques
    à chaque constructeur et souvent à chaque génération de modèle. La forme, la couleur et les fixations varient.- Côté de
    montage (conducteur ou passager) : l''interrupteur de verrouillage principal est souvent sur le panneau de porte côté
    conducteur. Certains véhicules en ont également côté passager. Indiquer le côté lors de la commande.- Centralisation qui
    ne répond plus : avant de commander l''interrupteur, tester le fonctionnement via la télécommande. Si la télécommande
    fonctionne, le système de centralisation est intact et la panne vient bien de l''interrupteur ou de son câblage.- Couleur
    et finition : sur certains véhicules, l''interrupteur est disponible en plusieurs teintes pour correspondre au coloris
    de l''intérieur (noir, gris, beige). Vérifier la teinte d''origine.- Pièce individuelle ou bloc de commandes de porte
    complet : selon les disponibilités et le coût, il peut être plus économique de remplacer uniquement le bouton défaillant
    ou le bloc complet. Vérifier la disponibilité de la pièce individuelle.- Référence OEM ou numéro de pièce constructeur
    : noter la référence OEM gravée sur la pièce déposée ou la récupérer dans la documentation technique du véhicule. Les
    équipementiers (Hella, TRW, Febi) proposent des références équivalentes.- Verrouillage déverrouillage intempestif : si
    ce symptôme est présent, vérifier d''abord le câblage de la porte (soufflet de passage de câbles entre la porte et le
    montant, qui se craque avec le temps) avant de remplacer l''interrupteur.Pour aller plus loin : consultez notre guide
    d''achat interrupteur verrouilage des portes — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 'Le remplacement de l''interrupteur de verrouillage des portes implique d''accéder au panneau de commandes de
    porte. Cette opération nécessite dans la plupart des cas de déposer le panneau de porte ou le cache du bloc de commandes.
    La procédure varie selon les véhicules mais suit les grandes étapes suivantes :- Déconnecter la batterie : couper l''alimentation
    électrique avant toute intervention sur un composant électronique. Débrancher la borne négative et attendre 2 minutes
    pour que les capacités des boîtiers électroniques se déchargent.- Déposer le panneau de porte ou le cache du bloc de commandes
    : selon les véhicules, le bloc de commandes est clipsé dans un logement du panneau de porte ou fait partie du panneau
    lui- même. Utiliser un outil démonte-garniture pour extraire le cache sans l''abîmer. Repérer et retirer les vis dissimulées
    sous des cache-vis ou dans des cavités.- Accéder au connecteur du bloc de commandes : une fois le cache retiré, localiser
    le connecteur électrique qui alimente le bloc. Il est généralement maintenu par un clip de déverrouillage. Appuyer sur
    le clip et tirer le connecteur doucement.- Extraire l''interrupteur défaillant : certains interrupteurs sont clipsés dans
    le bloc et s''extraient en appuyant sur des pattes de maintien depuis l''arrière. D''autres sont remplacés avec le bloc
    complet.- Comparer les pièces : vérifier que la nouvelle pièce est identique à l''ancienne (géométrie, nombre de broches,
    sens du connecteur) avant de l''installer.- Installer le nouvel interrupteur : clipser le nouvel interrupteur dans son
    logement jusqu''au clic de verrouillage. S''assurer que les pattes de maintien sont correctement engagées.- Rebrancher
    le connecteur électrique : pousser le connecteur jusqu''au clic de verrouillage. Vérifier que le verrouillage mécanique
    est actif en tirant doucement sur le connecteur.- Rebrancher la batterie et tester : reconnecter la borne négative, démarrer
    le véhicule et tester le bouton de verrouillage avant de reposer le cache définitivement.'
  S4_REPOSE: 'Après avoir remplacé l''interrupteur de verrouillage des portes, la repose du panneau de commandes de porte
    et les tests de fonctionnement doivent être faits méticuleusement avant de refermer la porte. - Reconnexion du connecteur
    électrique : avant tout remontage, tester l''interrupteur en connectant son connecteur et en actionnant le bouton, batterie
    reconnectée. Si le verrouillage central ne répond pas à ce stade, l''interrupteur est défectueux ou le câblage est à vérifier
    — inutile de tout remonter pour découvrir une panne persistante. - Mise en place de l''interrupteur dans son logement
    : insérer l''interrupteur dans son clip ou son cadre de fixation. Sur la plupart des véhicules, il s''enclipse dans le
    panneau de commandes par pression frontale. Vérifier que les languettes d''encliquetage sont bien engagées — l''interrupteur
    ne doit pas bouger une fois en place. - Remontage du bloc de commandes : remettre en place le bloc de commandes (vitres,
    rétroviseurs, verrouillage) dans sa position d''origine dans l''accoudoir ou la garniture de porte. Vérifier l''alignement
    avant de clipper ou visser. - Remontage du panneau de porte : replacer la garniture de porte en alignant les clips périphériques,
    puis enfoncer fermement sur tout le pourtour. Revisser les vis de fixation (cadre de poignée intérieure, angle inférieur
    selon le véhicule). Ne pas oublier de repasser le câble ou la tringle de déverrouillage intérieur si elle avait été décrochée.
    - Reconnexion de la lèche-vitre et des conduits de câbles : vérifier que la lèche-vitre est correctement positionnée dans
    sa rainure et que les câbles électriques (vitre, rétroviseur, verrouillage) ne sont pas pincés entre la porte et la garniture.
    - Tests fonctionnels complets : actionner le verrouillage et le déverrouillage depuis le bouton remonté, depuis la télécommande
    et depuis les autres portes. Vérifier également que les autres fonctions du bloc de commandes (vitre, rétroviseur) n''ont
    pas été perturbées par l''intervention.'
  S5: 'Le remplacement d''un interrupteur de porte est une opération de carrosserie électrique accessible, mais quelques erreurs
    peuvent compliquer inutilement la réparation ou l''empêcher de fonctionner :- Ne pas vérifier le câblage du soufflet de
    porte avant de conclure à une panne d''interrupteur : le câblage qui traverse le soufflet entre le montant et la porte
    subit des flexions répétées à chaque ouverture de porte. Après plusieurs années, les fils intérieurs se cassent tout en
    conservant une gaine externe intacte. Ce type de panne simule parfaitement une défaillance d''interrupteur. Inspecter
    ou tester la continuité du câblage avant toute commande de pièce.- Forcer sur les clips de maintien du cache de porte
    : les caches de porte sont maintenus par des clips plastique fragiles. Forcer avec un outil inadapté casse ces clips et
    rend le cache instable après repose. Utiliser un outil démonte- garniture plat et large pour répartir la force.- Omettre
    de débrancher la batterie : sur les véhicules modernes, les boîtiers de confort (BSI/UCH) sont très sensibles aux courts-circuits.
    Un tournevis qui court-circuite accidentellement deux broches du connecteur peut effacer la mémoire du boîtier ou déclencher
    un verrouillage des organes de confort.- Confondre l''interrupteur de verrouillage et le moteur de centralisation : si
    une seule porte ne se verrouille pas depuis l''interrupteur mais répond à la télécommande, la panne est dans le moteur
    de centralisation de cette porte, pas dans l''interrupteur de commande. Vérifier quel composant est en cause avant de
    commander.- Oublier d''effacer les codes défaut après la réparation : si le boîtier de confort a enregistré un code défaut
    à cause de l''interrupteur défaillant, il faut l''effacer à la valise OBD pour que le voyant s''éteigne et que le système
    retrouve son fonctionnement normal.'
  S6: 'Après le montage du nouvel interrupteur et avant de reposer définitivement les caches de porte, effectuer les vérifications
    suivantes pour valider le bon fonctionnement :- Tester le verrouillage et le déverrouillage central depuis le bouton :
    actionner le bouton dans les deux sens et vérifier que toutes les portes se verrouillent et se déverrouillent simultanément.
    Si une porte ne répond pas, le problème vient du moteur de centralisation de cette porte et non de l''interrupteur.- Comparer
    avec le fonctionnement de la télécommande : le comportement de la centralisation depuis le bouton doit être identique
    à celui déclenché par la télécommande.- Vérifier l''absence de commandes intempestives : laisser le véhicule stationné
    moteur allumé pendant 5 minutes en observant que les serrures ne se déclenchent pas de façon aléatoire.- Effectuer une
    lecture de diagnostic si un voyant était allumé : brancher une valise OBD, effacer les codes défaut présents et vérifier
    que le voyant ne revient pas après un cycle de démarrage.- Contrôler la fixation du cache de porte : vérifier que tous
    les clips de maintien sont engagés et que le cache ne vibre pas lors d''une frappe douce du poing. Un cache mal clipssé
    génère des bruits parasites en roulage.- Tester la résistance de la porte aux vibrations : effectuer un trajet court pour
    vérifier l''absence de bruit de caisse ou de claquement dans la porte après la repose du cache.'
  S7: 'La panne de verrouillage centralisé peut impliquer plusieurs composants de la chaîne électrique. Avant de commander
    l''interrupteur, vérifier que les pièces suivantes ne sont pas en cause. - Serrure de porte : si une seule porte ne se
    verrouille pas malgré un interrupteur fonctionnel, la serrure de cette porte ou son moteur de centralisation est défaillant
    — pas l''interrupteur. Tester la centralisation depuis la télécommande pour localiser la panne. - Moteur de centralisation
    : chaque porte dispose d''un moteur électrique qui actionne la serrure. Un moteur qui clique mais ne verrouille plus est
    usé et doit être remplacé. Ce composant est indépendant de l''interrupteur. - Boîtier BSI / UCH : le calculateur de confort
    (BSI, UCH selon la marque) gère la centralisation. Une défaillance de ce boîtier peut simuler une panne d''interrupteur.
    Tester la centralisation depuis la télécommande ou l''appli constructeur avant de conclure. - Soufflet de passage de porte
    : le câblage électrique entre la caisse et la porte passe par un soufflet en caoutchouc. Si ce soufflet est fissuré ou
    que les fils sont cassés à l''intérieur, la panne peut affecter plusieurs fonctions de porte simultanément (vitre, verrouillage,
    rétroviseur). - Télécommande / Plip : si le verrouillage depuis le bouton de porte fonctionne mais pas depuis la télécommande,
    la pile de la télécommande est épuisée ou le plip est à re-synchroniser — pas de remplacement d''interrupteur nécessaire
    dans ce cas.'
  S8: 'La télécommande fonctionne mais pas le bouton de porte : est-ce toujours l''interrupteur ?Pas forcément. Si la télécommande
    fonctionne, le système de centralisation (moteurs, câblage, boîtier de commande) est intact. La panne est alors localisée
    entre le bouton de porte et le boîtier de centralisation. Cela peut être l''interrupteur lui-même, son connecteur ou le
    câblage dans le soufflet de passage entre la porte et le montant de carrosserie. Tester la continuité du câblage avec
    un multimètre avant de commander l''interrupteur.Peut-on remplacer uniquement le bouton ou faut-il changer tout le bloc
    de commandes de porte ?Cela dépend du véhicule. Sur certains modèles, le bouton de verrouillage est une pièce indépendante
    clipsée dans le bloc de commandes, remplaçable séparément. Sur d''autres, il est intégré dans un combiné de commandes
    de porte (lève-vitres, rétroviseurs, centralisation) qui se remplace en bloc. Identifier la référence de la pièce déposée
    pour déterminer si une pièce séparée existe.Le soufflet de porte peut-il vraiment casser les fils du câblage ?Oui, c''est
    un mode de défaillance très courant sur les véhicules de plus de 7 ans. Le câblage dans le soufflet subit des milliers
    de flexions lors des ouvertures et fermetures de porte. Les fils fins à l''intérieur se fatiguent et finissent par rompre,
    parfois sans trace visible sur la gaine externe. Ce type de panne crée des défaillances intermittentes difficiles à reproduire.Faut-il
    réinitialiser quelque chose après le remplacement de l''interrupteur ?Sur la plupart des véhicules, non. Le remplacement
    d''un simple interrupteur mécanique ne nécessite pas de procédure de réinitialisation. En revanche, si un code défaut
    avait été généré dans le boîtier de confort, il faut l''effacer manuellement à la valise OBD. Certains véhicules nécessitent
    également de réinitialiser le boîtier de confort après déconnexion de la batterie (fenêtre de toit ouvrant, initialisation
    des lève-vitres) : consulter la procédure spécifique au modèle.'
  META: Centralisation qui ne répond plus, porte qui ne se verrouille pas ou déclenchements intempestifs ? Diagnostiquez l'interrupteur
    de verrouillage des portes.
---

# Interrupteur verrouilage des portes - Guide Diagnostic Complet

## Fonction et Rôle

Commande le verrouillage/déverrouillage centralisé des portes

**Actions principales:** commander, activer, verrouiller

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- centralisation qui ne repond plus
- une porte ne se verrouille pas
- verrouillage deverrouillage intempestif

## Procédure de Diagnostic

Pour diagnostiquer un problème de interrupteur verrouilage des portes:

1. **Inspection visuelle** - Examiner l'état du interrupteur verrouilage des portes
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

- serrure
- moteur centralisation

## Critères de Compatibilité

Pour commander le bon interrupteur verrouilage des portes, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"

## FAQ

**Comment choisir Interrupteur verrouilage des portes compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Interrupteur verrouilage des portes ?**
En cas de centralisation qui ne repond plus ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Interrupteur verrouilage des portes sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
