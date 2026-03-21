#!/usr/bin/env python3
"""One-shot fix: correct misclassified image gammes based on source_url content analysis."""

import os
import re
import sys
from pathlib import Path

KNOWLEDGE_PATH = os.getenv("KNOWLEDGE_PATH", "/opt/automecanik/rag/knowledge")
IMG_DIR = os.path.join(KNOWLEDGE_PATH, "_raw", "web-images")

# ─── URL path → gamme mapping rules ───
# Order matters: first match wins. More specific patterns first.
URL_GAMME_RULES: list[tuple[str, str]] = [
    # Hutchinson
    ("hutchinson.com/fr/solutions/courroie-poly-v", "courroie-d-accessoire"),
    ("hutchinson.com/fr/solutions/poulie-decoupleuse", "poulie-d-alternateur"),
    ("hutchinson.com/fr/solutions/ligne-de-refroidissement", "durite-de-refroidissement"),
    ("hutchinson.com/fr/solutions/capteurs", "capteur-abs"),
    ("hutchinson.com/fr/solutions/biellette", "biellette-de-barre-stabilisatrice"),
    ("hutchinson.com/fr/solutions/articulation", "silent-bloc"),

    # Brembo — specific product pages
    ("bremboparts.com", "plaquettes", "plaquette-de-frein"),
    ("bremboparts.com", "brake-pads", "plaquette-de-frein"),
    ("bremboparts.com", "brake.pad", "plaquette-de-frein"),
    ("bremboparts.com", "disque", "disque-de-frein"),
    ("bremboparts.com", "discs", "disque-de-frein"),
    ("bremboparts.com", "machoire", "machoires-de-frein"),
    ("bremboparts.com", "m%C3%A2choire", "machoires-de-frein"),
    ("bremboparts.com", "tambour", "tambour-de-frein"),
    ("bremboparts.com", "etrier", "etrier-de-frein"),
    ("bremboparts.com", "%C3%A9trier", "etrier-de-frein"),
    ("bremboparts.com", "liquide-de-frein", "liquide-de-frein"),
    ("bremboparts.com", "brake-fluid", "liquide-de-frein"),
    ("bremboparts.com", "cylindre", "maitre-cylindre-de-frein"),
    ("bremboparts.com", "greenance-kit", "disque-de-frein"),
    ("bremboparts.com", "co-cast", "disque-de-frein"),
    ("bremboparts.com", "gt-disque", "disque-de-frein"),
    ("bremboparts.com", "kit-gt", "etrier-de-frein"),
    ("bremboparts.com", "kit-upgrade-gt", "etrier-de-frein"),
    ("bremboparts.com", "carbon-ceramic", "disque-de-frein"),
    # Brembo fallback: most Brembo content is about disc brakes
    ("bremboparts.com", "disque-de-frein"),

    # ATE — specific product pages
    ("ate-freinage.fr/produits/capteurs", "capteur-abs"),
    ("ate-freinage.fr/produits/freins-a-tambour", "machoires-de-frein"),
    ("ate-freinage.fr/produits/liquides", "liquide-de-frein"),
    ("ate-freinage.fr/produits/pieces-dembrayage", "embrayage"),
    ("ate-freinage.fr/produits/pieces-hydrauliques/correcteur", "cylindre-de-roue"),
    ("ate-freinage.fr/produits/pieces-hydrauliques/cylindres-de-roue", "cylindre-de-roue"),
    ("ate-freinage.fr/produits/pieces-hydrauliques/etriers", "etrier-de-frein"),
    ("ate-freinage.fr/produits/pieces-hydrauliques/flexibles", "flexible-de-frein"),
    ("ate-freinage.fr/produits/pieces-hydrauliques/frein-de-parking", "etrier-de-frein"),
    ("ate-freinage.fr/produits/pieces-hydrauliques/maitres-cylindres", "maitre-cylindre-de-frein"),
    ("ate-freinage.fr/produits/pieces-hydrauliques/mk60", "capteur-abs"),
    ("ate-freinage.fr/produits/pieces-hydrauliques/reconditionnement", "etrier-de-frein"),
    ("ate-freinage.fr/produits/pieces-hydrauliques/servofreins", "maitre-cylindre-de-frein"),
    ("ate-freinage.fr/blog/montage-des-plaquettes", "plaquette-de-frein"),
    ("ate-freinage.fr/catalogues", "plaquette-de-frein"),

    # Textar
    ("textar.com/fr/capteurs-abs", "capteur-abs"),
    ("textar.com/fr/gamme-de-disques", "disque-de-frein"),
    ("textar.com/fr/liquide-de-frein", "liquide-de-frein"),
    ("textar.com/fr/machoires", "machoires-de-frein"),
    ("textar.com/fr/plaquettes", "plaquette-de-frein"),
    ("textar.com/fr/produits-dentretien", "liquide-de-frein"),
    ("textar.com/fr/tambours", "tambour-de-frein"),

    # Delphi
    ("delphiautoparts.com", "allumage", "bobine-d-allumage"),
    ("delphiautoparts.com", "biellette-stabilisatrice", "biellette-de-barre-stabilisatrice"),
    ("delphiautoparts.com", "bras-de-suspension", "bras-de-suspension"),
    ("delphiautoparts.com", "caoutchouc-sur-m", "silent-bloc"),
    ("delphiautoparts.com", "rotules", "rotule-de-direction"),
    ("delphiautoparts.com", "disques-de-frein", "disque-de-frein"),
    ("delphiautoparts.com", "plaquettes", "plaquette-de-frein"),
    ("delphiautoparts.com", "sabots", "machoires-de-frein"),
    ("delphiautoparts.com", "tambours", "tambour-de-frein"),
    ("delphiautoparts.com", "machoires", "machoires-de-frein"),
    ("delphiautoparts.com", "m%C3%A2choires", "machoires-de-frein"),
    ("delphiautoparts.com", "maitres-cylindres", "maitre-cylindre-de-frein"),
    ("delphiautoparts.com", "cylindres-de-roue", "cylindre-de-roue"),
    ("delphiautoparts.com", "ma%C3%AEtres-cylindres", "maitre-cylindre-de-frein"),
    ("delphiautoparts.com", "liquide-de-frein", "liquide-de-frein"),
    ("delphiautoparts.com", "direction-et-suspension", "rotule-de-direction"),
    ("delphiautoparts.com", "freinage", "plaquette-de-frein"),
    ("delphiautoparts.com", "pompes-%C3%A0-carburant", "injecteur"),
    ("delphiautoparts.com", "modules-et-pompes", "injecteur"),
    ("delphiautoparts.com", "vis-de-fixation", "disque-de-frein"),
    ("delphiautoparts.com", "purger", "injecteur"),

    # DENSO
    ("denso-am.eu/fr/products/balais-dessuie-glace", "balais-d-essuie-glace"),
    ("denso-am.eu/fr/products/climatisation", "compresseur-de-climatisation"),
    ("denso-am.eu", "ac-compressor-oil", "compresseur-de-climatisation"),
    ("denso-am.eu", "ac-compressor", "compresseur-de-climatisation"),
    ("denso-am.eu", "condenseur", "condenseur-de-climatisation"),
    ("denso-am.eu", "evaporateur", "condenseur-de-climatisation"),
    ("denso-am.eu", "intercooler", "radiateur-de-refroidissement"),
    ("denso-am.eu", "noyaux-de-chauffage", "radiateur-de-refroidissement"),
    ("denso-am.eu", "pressostats", "compresseur-de-climatisation"),
    ("denso-am.eu", "radiateurs", "radiateur-de-refroidissement"),
    ("denso-am.eu", "secheurs", "condenseur-de-climatisation"),
    ("denso-am.eu", "soupapes", "compresseur-de-climatisation"),
    ("denso-am.eu", "thermostats", "thermostat"),
    ("denso-am.eu", "ventilateurs", "condenseur-de-climatisation"),
    ("denso-am.eu", "actionneurs", "compresseur-de-climatisation"),
    ("denso-am.eu", "moto-ventilateurs", "condenseur-de-climatisation"),

    # MANN-FILTER
    ("mann-filter.com", "filtre-air", "filtre-a-air"),
    ("mann-filter.com", "filtre-carburant", "filtre-a-carburant"),
    ("mann-filter.com", "filtre-huile", "filtre-a-huile"),

    # Purflux
    ("purflux.com", "filtres-a-air", "filtre-a-air"),

    # WIX
    ("wixfilters.com", "filtres-a-carburant", "filtre-a-carburant"),

    # FRAM
    ("fram.com", "oil-filter", "filtre-a-huile"),
    ("fram.com", "change-your-oil", "filtre-a-huile"),

    # Auto media
    ("autoplus.fr", "filtre-a-air", "filtre-a-air"),
    ("autoplus.fr", "etrier-de-frein", "etrier-de-frein"),
    ("la-voiture.fr", "plaquettes-frein", "plaquette-de-frein"),
    ("blog.vivacar.fr/plaquettes-de-frein", "plaquette-de-frein"),
    ("fiches-auto.fr", "direction-assistee", "direction-cremaillere"),
    ("fiches-auto.fr", "plaquettes", "plaquette-de-frein"),
    ("caradisiac.com", "disque-de-frein"),
    ("profauto.fr/nettoyant-frein", "plaquette-de-frein"),
    ("gpa26.com", "etrier-de-frein", "etrier-de-frein"),
    ("gpa26.com", "alternateur", "poulie-d-alternateur"),
    ("capcar.fr", "filtre-a-air", "filtre-a-air"),
    ("user-manual.renault.com", "thermostat"),
    ("provence-outillage.fr", "balai-essuie-glace", "balais-d-essuie-glace"),
]


def match_gamme(source_url: str) -> str | None:
    """Find the correct gamme for a source URL using rule matching."""
    url_lower = source_url.lower()
    for rule in URL_GAMME_RULES:
        if len(rule) == 2:
            # (url_pattern, gamme)
            pattern, gamme = rule
            if pattern.lower() in url_lower:
                return gamme
        elif len(rule) == 3:
            # (domain, keyword, gamme) — domain AND keyword must match
            domain, keyword, gamme = rule
            if domain.lower() in url_lower and keyword.lower() in url_lower:
                return gamme
    return None


def main():
    dry_run = "--apply" not in sys.argv

    sidecars = []
    for f in sorted(os.listdir(IMG_DIR)):
        if not f.endswith(".prompt.md"):
            continue
        filepath = os.path.join(IMG_DIR, f)
        try:
            content = Path(filepath).read_text(encoding="utf-8")
            url_match = re.search(r'source_url:\s*"([^"]+)"', content)
            gamme_match = re.search(r'gamme:\s*(?:"([^"]+)"|null)', content)
            source_url = url_match.group(1) if url_match else ""
            current_gamme = gamme_match.group(1) if gamme_match and gamme_match.group(1) else None
            sidecars.append({
                "file": f,
                "path": filepath,
                "source_url": source_url,
                "current_gamme": current_gamme,
                "content": content,
            })
        except Exception:
            continue

    print(f"Scanned {len(sidecars)} sidecars")

    fixed = 0
    unchanged = 0
    no_match = 0
    fixes_log = []

    for sc in sidecars:
        correct = match_gamme(sc["source_url"])
        if correct is None:
            no_match += 1
            continue
        if sc["current_gamme"] == correct:
            unchanged += 1
            continue

        old = sc["current_gamme"] or "null"
        fixes_log.append(f"  {sc['file']}: {old} -> {correct}")

        if not dry_run:
            content = sc["content"]
            updated = re.sub(
                r'gamme:\s*(?:null|"[^"]*")',
                f'gamme: "{correct}"',
                content,
            )
            if updated != content:
                Path(sc["path"]).write_text(updated, encoding="utf-8")
        fixed += 1

    print(f"\nResults:")
    print(f"  Fixed: {fixed}")
    print(f"  Already correct: {unchanged}")
    print(f"  No rule matched: {no_match}")

    if fixes_log:
        print(f"\nChanges ({'APPLIED' if not dry_run else 'DRY-RUN'}):")
        for line in fixes_log[:100]:
            print(line)
        if len(fixes_log) > 100:
            print(f"  ... and {len(fixes_log) - 100} more")

    if dry_run and fixed > 0:
        print(f"\n[DRY-RUN] Use --apply to write {fixed} fixes.")


if __name__ == "__main__":
    main()
