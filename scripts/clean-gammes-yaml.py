#!/usr/bin/env python3
"""
Nettoyage P0 des fichiers gammes RAG.

5 passes séquentielles :
  Pass 1: Nettoyer les dumps web bruts du YAML (diagnostic.symptoms, depose_steps, selection.criteria/anti_mistakes)
  Pass 2: Ajouter doc_id (UUID5) + content_hash (SHA256) + lang
  Pass 3: Promouvoir rendering.faq dans le corps MD (section ## FAQ)
  Pass 4: Promouvoir maintenance dans le corps MD (section ## Entretien et Intervalles)
  Pass 5: Promouvoir variants dans le corps MD (section ## Types et Variantes)

Usage:
  python3 clean-gammes-yaml.py --dry-run                                    # Compter seulement
  python3 clean-gammes-yaml.py --dry-run --only filtre-a-huile,disque-de-frein
  python3 clean-gammes-yaml.py --only filtre-a-huile,plaquette-de-frein     # 2 fichiers
  python3 clean-gammes-yaml.py --all                                         # 232 fichiers
"""

import argparse
import hashlib
import os
import re
import shutil
import sys
import time
import uuid
import yaml

# ── Config ──────────────────────────────────────────────────────────────────

GAMMES_DIR = '/opt/automecanik/rag/knowledge/gammes'
BACKUP_DIR = os.path.join(GAMMES_DIR, '.backup-pre-clean')
EVIDENCE_DIR = '/opt/automecanik/rag/knowledge/_raw/evidence'
LOG_DIR = '/opt/automecanik/rag/scripts/logs'
LOGFILE = os.path.join(LOG_DIR, 'clean-gammes.log')

# UUID namespace for doc_id generation (stable, never changes)
DOC_ID_NAMESPACE = uuid.UUID('a1b2c3d4-e5f6-7890-abcd-ef1234567890')

# Threshold: strings longer than this in YAML lists are likely dumps
DUMP_THRESHOLD = 200

# Pattern to detect source references in dump strings
SOURCE_PATTERN = re.compile(r'\(Source:\s*web')

# ── Logging ─────────────────────────────────────────────────────────────────

def log(msg):
    ts = time.strftime('%Y-%m-%d %H:%M:%S')
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    os.makedirs(LOG_DIR, exist_ok=True)
    with open(LOGFILE, 'a') as f:
        f.write(line + '\n')


# ── File I/O ────────────────────────────────────────────────────────────────

def parse_md(filepath):
    """Parse a .md file into (frontmatter_dict, body_string, raw_content)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        raw = f.read()

    if not raw.startswith('---'):
        return None, raw, raw

    parts = raw.split('---', 2)
    if len(parts) < 3:
        return None, raw, raw

    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        log(f"  YAML parse error: {e}")
        return None, raw, raw

    body = parts[2]
    return meta, body, raw


def write_md(filepath, meta, body):
    """Write frontmatter + body back to .md file."""
    yaml_str = yaml.dump(meta, default_flow_style=False, allow_unicode=True,
                         sort_keys=False, width=120)
    content = f"---\n{yaml_str}---\n{body}"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    # Validate: re-parse to ensure YAML is still valid
    with open(filepath, 'r', encoding='utf-8') as f:
        check = f.read()
    check_parts = check.split('---', 2)
    if len(check_parts) >= 3:
        yaml.safe_load(check_parts[1])  # raises if broken


def backup_file(filepath, slug):
    """Copy file to backup dir before modification."""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    dest = os.path.join(BACKUP_DIR, f"{slug}.md")
    if not os.path.exists(dest):
        shutil.copy2(filepath, dest)


# ── Pass 1: Clean YAML dumps ───────────────────────────────────────────────

def is_dump(item):
    """Detect if a YAML list item is a web dump (string > threshold with Source ref)."""
    if not isinstance(item, str):
        return False
    if len(item) < DUMP_THRESHOLD:
        return False
    # Strong signal: contains (Source: web/...)
    if SOURCE_PATTERN.search(item):
        return True
    # Also catch: starts with markdown heading (# or ##) and is long
    if len(item) > 300 and re.match(r'^#{1,3}\s', item.strip()):
        return True
    return False


def clean_list(items):
    """Remove dump items from a YAML list. Returns (cleaned, extracted)."""
    if not isinstance(items, list):
        return items, []
    cleaned = []
    extracted = []
    for item in items:
        if is_dump(item):
            extracted.append(item)
        else:
            cleaned.append(item)
    return cleaned, extracted


def pass1_clean_dumps(meta, slug):
    """Clean dump strings from diagnostic.symptoms, depose_steps, selection.criteria, anti_mistakes.
    Returns (modified_meta, evidence_dict, stats)."""
    evidence = {}
    stats = {'removed': 0}

    # Fields to clean: nested paths
    targets = [
        ('diagnostic', 'symptoms'),
        ('diagnostic', 'depose_steps'),
        ('diagnostic', 'causes'),
        ('selection', 'criteria'),
        ('selection', 'anti_mistakes'),
        ('selection', 'checklist'),
    ]

    for parent_key, child_key in targets:
        parent = meta.get(parent_key)
        if not isinstance(parent, dict):
            continue
        items = parent.get(child_key)
        if not isinstance(items, list):
            continue

        cleaned, extracted = clean_list(items)
        if extracted:
            evidence_key = f"{parent_key}.{child_key}"
            evidence[evidence_key] = extracted
            stats['removed'] += len(extracted)
            parent[child_key] = cleaned

    # Also check rendering.faq for dumps (seen in plaquette-de-frein)
    rendering = meta.get('rendering')
    if isinstance(rendering, dict):
        faq = rendering.get('faq')
        if isinstance(faq, list):
            cleaned_faq = []
            extracted_faq = []
            for item in faq:
                if isinstance(item, str) and is_dump(item):
                    extracted_faq.append(item)
                elif isinstance(item, dict):
                    # Check if answer is a dump
                    answer = item.get('answer', '')
                    if isinstance(answer, str) and is_dump(answer):
                        extracted_faq.append(item)
                    else:
                        cleaned_faq.append(item)
                else:
                    cleaned_faq.append(item)
            if extracted_faq:
                evidence['rendering.faq'] = extracted_faq
                stats['removed'] += len(extracted_faq)
                rendering['faq'] = cleaned_faq

    return meta, evidence, stats


def save_evidence(slug, evidence):
    """Save extracted dump evidence to _raw/evidence/{slug}.yml."""
    if not evidence:
        return
    os.makedirs(EVIDENCE_DIR, exist_ok=True)
    filepath = os.path.join(EVIDENCE_DIR, f"{slug}.yml")
    with open(filepath, 'w', encoding='utf-8') as f:
        yaml.dump(evidence, f, default_flow_style=False, allow_unicode=True,
                  sort_keys=False, width=200)


# ── Pass 2: Add doc_id, content_hash, lang ──────────────────────────────────

def generate_doc_id(source_type, slug):
    """Generate deterministic UUID5 from source_type:slug."""
    name = f"{source_type}:{slug}"
    return str(uuid.uuid5(DOC_ID_NAMESPACE, name))


def compute_content_hash(body):
    """SHA256 of the body content (everything after frontmatter)."""
    return f"sha256:{hashlib.sha256(body.strip().encode('utf-8')).hexdigest()[:16]}"


def pass2_add_ids(meta, body):
    """Add doc_id, content_hash, lang to frontmatter."""
    stats = {'added': 0}

    source_type = meta.get('source_type', 'gamme')
    slug = meta.get('slug', '')

    if not meta.get('doc_id'):
        meta['doc_id'] = generate_doc_id(source_type, slug)
        stats['added'] += 1

    meta['content_hash'] = compute_content_hash(body)
    stats['added'] += 1

    if not meta.get('lang'):
        meta['lang'] = 'fr'
        stats['added'] += 1

    return meta, stats


# ── Pass 3: Promote FAQ to body ─────────────────────────────────────────────

def pass3_promote_faq(meta, body):
    """Promote rendering.faq items into a ## FAQ section in the body."""
    stats = {'promoted': 0}

    if '## FAQ' in body:
        return body, stats  # Already has FAQ section

    rendering = meta.get('rendering')
    if not isinstance(rendering, dict):
        return body, stats

    faq_items = rendering.get('faq')
    if not isinstance(faq_items, list) or not faq_items:
        return body, stats

    lines = ['\n## FAQ\n']
    for item in faq_items:
        if isinstance(item, dict):
            q = item.get('question', '').strip()
            a = item.get('answer', '').strip()
            if q and a:
                lines.append(f"**{q}**")
                lines.append(f"{a}\n")
                stats['promoted'] += 1

    if stats['promoted'] > 0:
        body = body.rstrip() + '\n' + '\n'.join(lines)

    return body, stats


# ── Pass 4: Promote maintenance to body ──────────────────────────────────────

def pass4_promote_maintenance(meta, body):
    """Promote maintenance.interval into a ## Entretien et Intervalles section."""
    stats = {'promoted': 0}

    if '## Entretien' in body:
        return body, stats

    maint = meta.get('maintenance')
    if not isinstance(maint, dict):
        return body, stats

    interval = maint.get('interval')
    if not interval:
        return body, stats

    lines = ['\n## Entretien et Intervalles\n']

    # interval can be a dict or a string
    if isinstance(interval, dict):
        value = interval.get('value', '')
        note = interval.get('note', '')
        timing = maint.get('timing_years', '') or interval.get('timing_years', '')
        if value:
            lines.append(f"- **Intervalle** : {value}")
        if note:
            lines.append(f"- {note}")
        if timing:
            lines.append(f"- **Timing** : {timing}")
    elif isinstance(interval, str):
        lines.append(f"- {interval}")
        timing = maint.get('timing', '') or maint.get('timing_years', '')
        if timing:
            lines.append(f"- **Timing** : {timing}")

    rule = maint.get('rule', '')
    if rule:
        lines.append(f"- **Règle** : {rule}")

    stats['promoted'] = 1

    # Insert after ## Procédure de Diagnostic (or append)
    insert_marker = '## Causes Probables'
    if insert_marker in body:
        idx = body.index(insert_marker)
        body = body[:idx] + '\n'.join(lines) + '\n\n' + body[idx:]
    else:
        body = body.rstrip() + '\n' + '\n'.join(lines)

    return body, stats


# ── Pass 5: Promote variants to body ────────────────────────────────────────

def pass5_promote_variants(meta, body):
    """Promote variants list into a ## Types et Variantes section."""
    stats = {'promoted': 0}

    if '## Types et Variantes' in body:
        return body, stats

    variants = meta.get('variants')
    if not isinstance(variants, list) or not variants:
        return body, stats

    lines = ['\n## Types et Variantes\n']

    for v in variants:
        if not isinstance(v, dict):
            continue
        name = v.get('name', '').strip()
        if not name:
            continue

        lines.append(f"### {name}")

        aliases = v.get('aliases', [])
        if aliases and isinstance(aliases, list):
            lines.append(f"Aussi appelé : {', '.join(str(a) for a in aliases)}.")

        visual = v.get('visual_differences', v.get('visual', ''))
        if isinstance(visual, list):
            for vd in visual:
                lines.append(f"- {vd}")
        elif isinstance(visual, str) and visual:
            lines.append(f"- {visual}")

        functional = v.get('functional_differences', v.get('functional', ''))
        if isinstance(functional, list):
            for fd in functional:
                lines.append(f"- {fd}")
        elif isinstance(functional, str) and functional:
            lines.append(f"- {functional}")

        lines.append('')
        stats['promoted'] += 1

    if stats['promoted'] > 0:
        # Insert after ## Fonction et Rôle (or append)
        # Look for the next H2 after Fonction
        marker_pattern = re.compile(r'(## Fonction et Rôle.*?)(\n## )', re.DOTALL)
        match = marker_pattern.search(body)
        if match:
            insert_pos = match.end(1)
            body = body[:insert_pos] + '\n' + '\n'.join(lines) + body[insert_pos:]
        else:
            body = body.rstrip() + '\n' + '\n'.join(lines)

    return body, stats


# ── Main ────────────────────────────────────────────────────────────────────

def process_file(filepath, slug, dry_run=False):
    """Process one gamme .md file through all 5 passes."""
    meta, body, raw = parse_md(filepath)
    if meta is None:
        log(f"  SKIP {slug} — no valid frontmatter")
        return {'skipped': True}

    result = {
        'slug': slug,
        'lines_before': raw.count('\n'),
        'pass1_removed': 0,
        'pass2_added': 0,
        'pass3_faq': 0,
        'pass4_maint': 0,
        'pass5_variants': 0,
    }

    # Pass 1: Clean dumps
    meta, evidence, p1_stats = pass1_clean_dumps(meta, slug)
    result['pass1_removed'] = p1_stats['removed']

    # Pass 2: Add IDs
    meta, p2_stats = pass2_add_ids(meta, body)
    result['pass2_added'] = p2_stats['added']

    # Pass 3: Promote FAQ
    body, p3_stats = pass3_promote_faq(meta, body)
    result['pass3_faq'] = p3_stats['promoted']

    # Pass 4: Promote maintenance
    body, p4_stats = pass4_promote_maintenance(meta, body)
    result['pass4_maint'] = p4_stats['promoted']

    # Pass 5: Promote variants
    body, p5_stats = pass5_promote_variants(meta, body)
    result['pass5_variants'] = p5_stats['promoted']

    # Recompute content_hash after body modifications
    meta['content_hash'] = compute_content_hash(body)

    if dry_run:
        # Count lines after
        yaml_str = yaml.dump(meta, default_flow_style=False, allow_unicode=True,
                             sort_keys=False, width=120)
        after_content = f"---\n{yaml_str}---\n{body}"
        result['lines_after'] = after_content.count('\n')
        return result

    # Backup
    backup_file(filepath, slug)

    # Save evidence
    if evidence:
        save_evidence(slug, evidence)

    # Write
    write_md(filepath, meta, body)

    # Count lines after
    with open(filepath, 'r', encoding='utf-8') as f:
        result['lines_after'] = f.read().count('\n')

    return result


def main():
    parser = argparse.ArgumentParser(description='Nettoyage P0 des gammes RAG')
    parser.add_argument('--dry-run', action='store_true', help='Compter seulement, ne rien modifier')
    parser.add_argument('--only', type=str, help='Slugs séparés par virgule (ex: filtre-a-huile,plaquette-de-frein)')
    parser.add_argument('--all', action='store_true', help='Traiter les 232 fichiers')
    args = parser.parse_args()

    if not args.dry_run and not args.only and not args.all:
        parser.print_help()
        print("\n⚠️  Spécifier --dry-run, --only ou --all")
        sys.exit(1)

    mode = 'DRY-RUN' if args.dry_run else 'EXECUTE'
    log(f"\n{'='*60}")
    log(f"=== Nettoyage P0 gammes RAG — {mode} ===")
    log(f"{'='*60}")

    # Collect files
    all_files = sorted([f for f in os.listdir(GAMMES_DIR) if f.endswith('.md')])

    if args.only:
        slugs = [s.strip() for s in args.only.split(',')]
        files = [f"{s}.md" for s in slugs if f"{s}.md" in all_files]
        missing = [s for s in slugs if f"{s}.md" not in all_files]
        if missing:
            log(f"  WARNING: fichiers manquants: {missing}")
    else:
        files = all_files

    log(f"  Fichiers: {len(files)} / {len(all_files)}")
    log(f"  Mode: {mode}")

    # Process
    totals = {
        'processed': 0,
        'skipped': 0,
        'pass1_removed': 0,
        'pass2_added': 0,
        'pass3_faq': 0,
        'pass4_maint': 0,
        'pass5_variants': 0,
        'lines_saved': 0,
    }

    for filename in files:
        slug = filename.replace('.md', '')
        filepath = os.path.join(GAMMES_DIR, filename)

        result = process_file(filepath, slug, dry_run=args.dry_run)

        if result.get('skipped'):
            totals['skipped'] += 1
            continue

        totals['processed'] += 1
        totals['pass1_removed'] += result['pass1_removed']
        totals['pass2_added'] += result['pass2_added']
        totals['pass3_faq'] += result['pass3_faq']
        totals['pass4_maint'] += result['pass4_maint']
        totals['pass5_variants'] += result['pass5_variants']

        lines_before = result.get('lines_before', 0)
        lines_after = result.get('lines_after', lines_before)
        delta = lines_before - lines_after
        totals['lines_saved'] += delta

        if result['pass1_removed'] > 0 or result['pass3_faq'] > 0:
            log(f"  {slug}: dumps={result['pass1_removed']}, faq={result['pass3_faq']}, "
                f"maint={result['pass4_maint']}, variants={result['pass5_variants']}, "
                f"lines {lines_before}→{lines_after} ({'-' if delta > 0 else '+'}{abs(delta)})")

    # Summary
    log(f"\n{'='*60}")
    log(f"=== BILAN ===")
    log(f"  Fichiers traités: {totals['processed']} ({totals['skipped']} skippés)")
    log(f"  Pass 1 — Dumps supprimés: {totals['pass1_removed']}")
    log(f"  Pass 2 — IDs ajoutés: {totals['pass2_added']}")
    log(f"  Pass 3 — FAQ promues: {totals['pass3_faq']}")
    log(f"  Pass 4 — Maintenance promues: {totals['pass4_maint']}")
    log(f"  Pass 5 — Variantes promues: {totals['pass5_variants']}")
    log(f"  Lignes économisées: {totals['lines_saved']}")
    log(f"{'='*60}")


if __name__ == '__main__':
    main()
