#!/usr/bin/env python3
"""Generate short and long French voice-over variants from selected shots."""

import argparse
import csv
from pathlib import Path


def read_rows(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def to_int(v: str) -> int:
    try:
        return int(v)
    except Exception:
        return 0


def build_short(rows: list[dict]) -> str:
    # Keep top 8 by score, preserve chronology.
    top = sorted(rows, key=lambda r: -to_int(r.get("visual_score", "0")))[:8]
    top = sorted(top, key=lambda r: (to_int(r.get("page", "0")), to_int(r.get("index_on_page", "0"))))

    out = []
    out.append("# Voix Off FR - Version Courte (60s)")
    out.append("")
    out.append("Aujourd'hui, on résume l'essentiel du diagnostic et de la réparation freinage en mode pratique.")
    out.append("")
    for r in top:
        out.append(
            f"- Plan page {r.get('page','?')}: point clé visuel, contrôle rapide, décision d'action atelier."
        )
    out.append("")
    out.append("Conclusion: un diagnostic structuré et des contrôles visuels précis améliorent sécurité et fiabilité.")
    out.append("")
    return "\n".join(out)


def build_long(rows: list[dict]) -> str:
    # Keep all selected rows ordered by doc then page.
    ordered = sorted(
        rows,
        key=lambda r: (r.get("doc_slug", ""), to_int(r.get("page", "0")), to_int(r.get("index_on_page", "0"))),
    )

    out = []
    out.append("# Voix Off FR - Version Longue (4 min)")
    out.append("")
    out.append(
        "Dans cette vidéo, on suit un fil complet: contexte, diagnostic, puis procédure de réparation, "
        "avec des repères visuels concrets pour l'atelier."
    )
    out.append("")

    current_doc = None
    for r in ordered:
        doc = r.get("doc_title", "Document technique")
        seg = r.get("segment", "main")
        page = r.get("page", "?")

        if doc != current_doc:
            current_doc = doc
            out.append(f"## Module: {doc}")
            out.append("On isole les informations utiles et on garde une logique d'intervention simple.")
            out.append("")

        out.append(
            f"- Segment {seg}, page {page}: observation visuelle, vérification méthodique, "
            "et recommandation d'action selon l'état du composant."
        )

    out.append("")
    out.append(
        "Conclusion: appliquer une méthode stable, du contrôle initial à la validation finale, "
        "réduit les erreurs et améliore la qualité des réparations."
    )
    out.append("")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build short+long French voice-over scripts")
    parser.add_argument("--input", required=True, help="shots_selected.csv path")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    rows = read_rows(Path(args.input))
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    short_path = out_dir / "voiceover_short_60s.txt"
    long_path = out_dir / "voiceover_long_4min.txt"

    short_path.write_text(build_short(rows), encoding="utf-8")
    long_path.write_text(build_long(rows), encoding="utf-8")

    print(f"generated_short={short_path}")
    print(f"generated_long={long_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
