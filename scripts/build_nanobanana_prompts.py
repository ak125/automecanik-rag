#!/usr/bin/env python3
"""Build safe NanoBanana image prompts from selected storyboard shots."""

import argparse
import csv
from pathlib import Path


SEGMENT_STYLE = {
    "intro": "plan large propre, ambiance atelier moderne, éclairage doux",
    "overview": "vue d'ensemble claire, infographie technique, fond neutre",
    "diagnostic": "focus composant automobile, détail net, style didactique",
    "procedure": "étape pratique en atelier, angle caméra 3/4, rendu réaliste",
    "repair": "gros plan outil + pièce, guidance visuelle, composition claire",
    "reference": "style manuel technique modernisé, pictogrammes lisibles",
    "main": "illustration technique automobile, style professionnel",
}


def read_rows(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def build_prompt(row: dict) -> str:
    segment = row.get("segment", "main")
    style = SEGMENT_STYLE.get(segment, SEGMENT_STYLE["main"])
    doc_title = row.get("doc_title", "système automobile")
    page = row.get("page", "?")

    return (
        "Créer une illustration originale pour une vidéo de mécanique automobile, "
        "sans logo, sans marque, sans texte protégé, sans reprise exacte d'une image existante. "
        f"Sujet: {doc_title}, section page {page}. "
        f"Style: {style}. "
        "Rendu 16:9, haute définition, lisible sur mobile, palette industrielle (gris, bleu, orange)."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate NanoBanana-safe prompts CSV")
    parser.add_argument("--input", required=True, help="shots_selected.csv path")
    parser.add_argument("--output", required=True, help="output nanobanana_prompts.csv path")
    args = parser.parse_args()

    rows = read_rows(Path(args.input))
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8", newline="") as f:
        fieldnames = [
            "shot_id",
            "doc_slug",
            "page",
            "segment",
            "priority",
            "image_file",
            "nanobanana_prompt",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "shot_id": row.get("shot_id", ""),
                    "doc_slug": row.get("doc_slug", ""),
                    "page": row.get("page", ""),
                    "segment": row.get("segment", ""),
                    "priority": row.get("priority", ""),
                    "image_file": row.get("image_file", ""),
                    "nanobanana_prompt": build_prompt(row),
                }
            )

    print(f"generated={len(rows)} output={out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
