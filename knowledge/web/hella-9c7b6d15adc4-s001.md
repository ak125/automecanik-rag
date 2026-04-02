---
title: "Capteur vilebrequin PMH — types inductif/Hall, diagnostic (HELLA)"
source_type: guide
category: knowledge
truth_level: L3
source_url: "https://www.hella.com/techworld/fr/technique/capteurs-et-actionneurs/capteur-de-vilebrequin-capteur-pmh/"
ingested_at: "2026-03-29T22:48:07Z"
ingested_by: batch-web-ingest-phase5
mapped_gammes:
- capteur-vilebrequin
- capteur-impulsion
---

# Capteur vilebrequin (PMH) — Guide technique

## Types
- **Inductif (2 broches)** : signal sinusoidal, resistance 200-1000 ohms
- **Hall (3 broches)** : signal rectangulaire, necessite alimentation 5V

## Valeurs de diagnostic
| Parametre | Specification |
|---|---|
| Resistance inductif | 200 - 1000 ohms |
| Isolement masse | >30 Mohms |
| Signal Hall | rectangulaire |
| Signal inductif | sinusoidal |

ATTENTION : ne pas mesurer la resistance sur un capteur Hall — risque de destruction par la tension de test.

## Symptomes de defaillance
- Rates d'allumage, calages moteur, difficultes de demarrage, codes defaut stockes

## Diagnostic
1. Lecture memoire defaut
2. Inspection connecteurs (corrosion)
3. Mesure resistance (inductif uniquement)
4. Verification entrefer capteur/cible
5. Oscilloscope : signal sinusoidal ou rectangulaire selon type
