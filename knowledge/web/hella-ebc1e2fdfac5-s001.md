---
title: "Bobine d allumage — fonctionnement, types, diagnostic et remplacement (HELLA TechWorld)"
source_type: guide
category: knowledge
truth_level: L3
source_url: "https://www.hella.com/techworld/fr/technique/electricite-et-electronique/bobine-allumage-depannage/"
ingested_at: "2026-03-29T22:38:47Z"
ingested_by: manual-web-ingest-phase5
mapped_gammes:
---

# Bobine d allumage — Guide technique

## Fonctionnement
La bobine d allumage fonctionne comme un transformateur : elle convertit la basse tension batterie (12V) en haute tension (jusqu a 40 000V) pour declencher l etincelle aux bougies.

## Composants internes
- Noyau de fer feuillete (renforce le champ magnetique)
- Enroulement primaire : fil cuivre 0,6-0,9 mm, resistance 0,2-3,0 ohms
- Enroulement secondaire : fil cuivre 0,05-0,1 mm, 50 000+ spires, resistance 5-20 kohms
- Rapport de transformation : 1:100

## Types de bobines
- **Type A — Bobine cylindrique conventionnelle** : 3 bornes (15, 1, 4), systeme a distributeur
- **Type B — Bobine double sortie** : 2 sorties secondaires, alimente 2 cylindres simultanement
- **Type C — Bobine quad sortie** : 2 enroulements primaires, remplace 2 bobines doubles
- **Type D — Bobine crayon (direct-on-plug)** : 1 primaire + 1 secondaire par cylindre, montee directement sur la bougie

## Specifications de resistance
| Type allumage | Primaire (ohms) | Secondaire (kohms) |
|---|---|---|
| Transistorise | 0,5 - 2,0 | 8 - 19 |
| Electronique/cartographique | 0,5 - 2,0 | 8 - 19 |
| Full electronic | 0,3 - 1,0 | 8 - 15 |

## Causes de defaillance
- Courts-circuits internes par vieillissement et surchauffe
- Tension d alimentation insuffisante (temps de charge primaire reduit)
- Dommages mecaniques (morsures de rongeurs, infiltration d huile)
- Infiltration d humidite (sel hivernal, lavage moteur)
- Resistance de contact (corrosion des connecteurs)

## Diagnostic
1. **Inspection visuelle** : fissures, fuites de pate de remplissage, cablage corrode
2. **Mesure de resistance primaire** : ohmmetre entre bornes 1 et 2 (comparer aux specs constructeur)
3. **Mesure de resistance secondaire** : entre bornes haute tension
4. **Tension d alimentation** : minimum 10,5V a la borne 2 contact mis (ex: 11,93V = OK)
5. **Signal primaire** : oscilloscope bornes 1 et 2, demarreur actif sans injection

## Remplacement
1. Debrancher le connecteur
2. Retirer le cable haute tension si applicable
3. Deboulonner la bobine de la culasse — eviter les mouvements rotatifs
4. Verifier la proprete du puits de bougie (huile/eau = probleme de joint)
5. Remonter la bobine neuve verticalement, serrer, rebrancher
6. Effacer les codes defaut, essai route avec diagnostic

## Securite
Les travaux sur les systemes d allumage electroniques peuvent provoquer des blessures graves. Personnel qualifie uniquement.
