#!/usr/bin/env python3
"""Generate a French voice-over script from selected storyboard shots."""

import argparse
import csv
from collections import defaultdict
from pathlib import Path


SEGMENT_INTRO = {
    "intro": "Dans cette séquence, on pose le contexte et les symptômes principaux.",
    "overview": "Ici, on présente une vue d'ensemble du système et de son rôle.",
    "diagnostic": "On passe maintenant à la phase de diagnostic méthodique.",
    "procedure": "On déroule ensuite la procédure étape par étape.",
    "repair": "Ici, on se concentre sur les actions de réparation concrètes.",
    "reference": "Cette partie sert de référence technique rapide.",
    "main": "On poursuit avec les points techniques essentiels.",
}


def load_rows(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def line_for_row(row: dict) -> str:
    page = row.get("page", "?")
    segment = row.get("segment", "main")
    doc_title = row.get("doc_title", "document technique")
    return (
        f"Plan page {page}. {SEGMENT_INTRO.get(segment, SEGMENT_INTRO['main'])} "
        f"On illustre ce point à partir du document « {doc_title} »."
    )


def build_script(rows: list[dict]) -> str:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        grouped[r.get("doc_slug", "document")].append(r)

    out = []
    out.append("# Script Voix Off FR")
    out.append("")
    out.append("## Intro générale")
    out.append(
        "Aujourd'hui, on explore les points clés du freinage et des procédures atelier, "
        "avec un focus sur le diagnostic visuel et les bonnes pratiques de réparation."
    )
    out.append("")

    for slug, shot_rows in grouped.items():
        title = shot_rows[0].get("doc_title", slug)
        out.append(f"## Module: {title}")

        # Order by page then index_on_page when available.
        shot_rows.sort(
            key=lambda r: (
                int(r.get("page", "0") or 0),
                int(r.get("index_on_page", "0") or 0),
            )
        )

        previous_segment = None
        for row in shot_rows:
            seg = row.get("segment", "main")
            if seg != previous_segment:
                out.append("")
                out.append(f"### Segment {seg}")
                previous_segment = seg
            out.append(f"- {line_for_row(row)}")

        out.append("")
        out.append("Transition: on résume les points critiques puis on passe à la partie suivante.")
        out.append("")

    out.append("## Conclusion")
    out.append(
        "En résumé, un diagnostic structuré, des contrôles visuels précis et des étapes de réparation "
        "claires permettent d'améliorer la fiabilité et la sécurité du freinage."
    )
    out.append("")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build French voice-over script from shots CSV")
    parser.add_argument("--input", required=True, help="shots_selected.csv path")
    parser.add_argument("--output", required=True, help="voiceover output .txt path")
    args = parser.parse_args()

    rows = load_rows(Path(args.input))
    script = build_script(rows)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(script, encoding="utf-8")
    print(f"generated={len(rows)} output={output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
