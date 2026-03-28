#!/usr/bin/env python3
"""
Nettoyage P1 des web chunks RAG (web/ + web-catalog/).

3 passes :
  Pass 1: Déclasser en L4 les fichiers vides ou tiny (<=5 lignes body, <200 chars)
  Pass 2: Nettoyer le boilerplate HTML/nav des fichiers utiles
  Pass 3: Ajouter doc_id + content_hash + lang aux fichiers restants L2/L3

Usage:
  python3 clean-web-chunks.py --dry-run                  # Compter seulement
  python3 clean-web-chunks.py --dry-run --dir web        # Seulement web/
  python3 clean-web-chunks.py --dry-run --dir web-catalog
  python3 clean-web-chunks.py --all                       # Exécuter sur web/ + web-catalog/
"""

import argparse
import hashlib
import os
import re
import sys
import time
import uuid
import yaml

# ── Config ──────────────────────────────────────────────────────────────────

RAG_ROOT = '/opt/automecanik/rag/knowledge'
DIRS = ['web', 'web-catalog']
LOG_DIR = '/opt/automecanik/rag/scripts/logs'
LOGFILE = os.path.join(LOG_DIR, 'clean-web-chunks.log')

DOC_ID_NAMESPACE = uuid.UUID('a1b2c3d4-e5f6-7890-abcd-ef1234567890')

# Boilerplate patterns to strip (case-insensitive line matching)
BOILERPLATE_LINE_PATTERNS = [
    re.compile(r'^\s*-?\s*Skip to main content', re.I),
    re.compile(r'^\s*-?\s*Skip to menu', re.I),
    re.compile(r'^\s*-?\s*Skip to footer', re.I),
    re.compile(r'^\s*-?\s*Partager sur\s*$', re.I),
    re.compile(r'^\s*-?\s*Accepter les cookies', re.I),
    re.compile(r'^\s*-?\s*Politique de confidentialité\s*$', re.I),
    re.compile(r'^\s*-?\s*Mentions légales\s*$', re.I),
    re.compile(r'^\s*-?\s*CGV\s*$', re.I),
    re.compile(r'^\s*-?\s*CGU\s*$', re.I),
    re.compile(r'^\s*-?\s*Tous droits réservés', re.I),
    re.compile(r'^\s*-?\s*©\s*\d{4}', re.I),
    re.compile(r'^\s*-?\s*Copyright\s', re.I),
    re.compile(r'^\s*-?\s*S\'inscrire à la newsletter', re.I),
    re.compile(r'^\s*-?\s*Inscrivez-vous à notre newsletter', re.I),
    re.compile(r'^\s*-?\s*Nous contacter\s*$', re.I),
]

# Combined line pattern: nav menu items (bullet lists of site sections)
NAV_MENU_PATTERNS = [
    re.compile(r'^\s*-\s*(ENTRETIEN AUTO|RÉPARATION AUTO|Révision voiture|'
               r'Changement liquide de frein|Changement amortisseurs|'
               r'Changement de batterie voiture|Changement alternateur|'
               r'Changement courroie accessoires|Décalaminage moteur|'
               r'Régénération forcée FAP|Parallélisme)\s*$', re.I),
    re.compile(r'^\s*-\s*(Vidange|Courroie de distribution|Plaquettes de frein|'
               r'Embrayage)\s*$', re.I),
    # Generic site nav: short bullet items that are clearly menu links
    re.compile(r'^\s*-\s*(Accueil|Contact|À propos|Blog|Catalogue|'
               r'Mon compte|Se connecter|Créer un compte|'
               r'Mon panier|Votre panier)\s*$', re.I),
]

# Full-line boilerplate to strip from beginning of body
HEADER_BOILERPLATE = re.compile(
    r'^-\s*Skip to main content\s*Skip to menu\s*Skip to footer\s*Partager sur\s*',
    re.I
)

# Minimum useful body: >5 non-empty lines and >200 chars
MIN_USEFUL_LINES = 5
MIN_USEFUL_CHARS = 200


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
    with open(filepath, 'r', encoding='utf-8') as f:
        raw = f.read()
    if not raw.startswith('---'):
        return None, raw, raw
    parts = raw.split('---', 2)
    if len(parts) < 3:
        return None, raw, raw
    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None, raw, raw
    return meta, parts[2], raw


def write_md(filepath, meta, body):
    yaml_str = yaml.dump(meta, default_flow_style=False, allow_unicode=True,
                         sort_keys=False, width=120)
    content = f"---\n{yaml_str}---\n{body}"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    # Validate
    with open(filepath, 'r', encoding='utf-8') as f:
        check = f.read()
    parts = check.split('---', 2)
    if len(parts) >= 3:
        yaml.safe_load(parts[1])


# ── Pass 1: Classify & downgrade ────────────────────────────────────────────

def classify_body(body):
    """Classify body content quality. Returns 'empty', 'tiny', or 'useful'."""
    stripped = body.strip()
    lines = [l for l in stripped.split('\n') if l.strip()]

    if len(lines) <= 1:
        return 'empty'
    if len(lines) <= MIN_USEFUL_LINES and len(stripped) < MIN_USEFUL_CHARS:
        return 'tiny'
    return 'useful'


# ── Pass 2: Clean boilerplate ───────────────────────────────────────────────

def clean_boilerplate(body):
    """Remove boilerplate lines from body. Returns (cleaned_body, lines_removed)."""
    lines = body.split('\n')
    cleaned = []
    removed = 0

    for line in lines:
        is_bp = False

        # Check boilerplate patterns
        for pattern in BOILERPLATE_LINE_PATTERNS:
            if pattern.search(line):
                is_bp = True
                break

        # Check nav menu patterns
        if not is_bp:
            for pattern in NAV_MENU_PATTERNS:
                if pattern.match(line):
                    is_bp = True
                    break

        if is_bp:
            removed += 1
        else:
            cleaned.append(line)

    # Also clean the combined header boilerplate (single-line dump)
    result = '\n'.join(cleaned)
    match = HEADER_BOILERPLATE.search(result)
    if match:
        result = result[:match.start()] + result[match.end():]
        removed += 1

    # Remove excessive blank lines (>2 consecutive)
    result = re.sub(r'\n{4,}', '\n\n\n', result)

    return result, removed


# ── Pass 3: Add IDs ────────────────────────────────────────────────────────

def add_ids(meta, body, source_type='web'):
    """Add doc_id, content_hash, lang."""
    slug = os.path.splitext(os.path.basename(meta.get('source_uri', '') or ''))[0]
    if not slug:
        slug = meta.get('title', 'unknown')[:60]

    name = f"{source_type}:{slug}"
    if not meta.get('doc_id'):
        meta['doc_id'] = str(uuid.uuid5(DOC_ID_NAMESPACE, name))

    meta['content_hash'] = f"sha256:{hashlib.sha256(body.strip().encode('utf-8')).hexdigest()[:16]}"

    if not meta.get('lang'):
        # Simple heuristic: check for French vs English
        fr_markers = ['le ', 'la ', 'les ', 'un ', 'une ', 'des ', 'du ', 'de ', ' est ', ' sont ']
        en_markers = ['the ', ' is ', ' are ', ' of ', ' and ', ' for ', ' with ']
        fr_score = sum(1 for m in fr_markers if m in body.lower()[:500])
        en_score = sum(1 for m in en_markers if m in body.lower()[:500])
        meta['lang'] = 'fr' if fr_score >= en_score else 'en'

    return meta


# ── Main ────────────────────────────────────────────────────────────────────

def process_file(filepath, dry_run=False):
    """Process one web chunk file."""
    meta, body, raw = parse_md(filepath)
    if meta is None:
        return {'status': 'skip', 'reason': 'no_frontmatter'}

    result = {
        'status': 'ok',
        'lines_before': raw.count('\n'),
        'downgraded': False,
        'bp_removed': 0,
        'ids_added': False,
    }

    # Pass 1: Classify
    quality = classify_body(body)
    current_level = meta.get('truth_level', 'L2')

    if quality in ('empty', 'tiny') and current_level in ('L2', 'L3'):
        meta['truth_level'] = 'L4'
        meta['downgrade_reason'] = f'body_{quality}'
        result['downgraded'] = True

    # Pass 2: Clean boilerplate (only for non-downgraded files)
    if not result['downgraded']:
        body, bp_removed = clean_boilerplate(body)
        result['bp_removed'] = bp_removed

        # Re-check after cleaning: might now be tiny
        post_quality = classify_body(body)
        if post_quality in ('empty', 'tiny') and current_level in ('L2', 'L3'):
            meta['truth_level'] = 'L4'
            meta['downgrade_reason'] = f'body_{post_quality}_after_clean'
            result['downgraded'] = True

    # Pass 3: Add IDs
    source_type = 'web-catalog' if 'web-catalog' in filepath else 'web'
    meta = add_ids(meta, body, source_type)
    result['ids_added'] = True

    if not dry_run:
        write_md(filepath, meta, body)

    with open(filepath, 'r', encoding='utf-8') as f:
        result['lines_after'] = f.read().count('\n') if not dry_run else result['lines_before']

    return result


def main():
    parser = argparse.ArgumentParser(description='Nettoyage P1 des web chunks RAG')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--dir', type=str, help='Répertoire cible (web ou web-catalog)')
    parser.add_argument('--all', action='store_true')
    args = parser.parse_args()

    if not args.dry_run and not args.all:
        parser.print_help()
        print("\n⚠️  Spécifier --dry-run ou --all")
        sys.exit(1)

    mode = 'DRY-RUN' if args.dry_run else 'EXECUTE'
    target_dirs = [args.dir] if args.dir else DIRS

    log(f"\n{'='*60}")
    log(f"=== Nettoyage P1 web chunks — {mode} ===")
    log(f"{'='*60}")

    totals = {
        'processed': 0, 'skipped': 0,
        'downgraded': 0, 'bp_removed': 0,
        'useful_remaining': 0,
    }

    for dirname in target_dirs:
        dirpath = os.path.join(RAG_ROOT, dirname)
        if not os.path.isdir(dirpath):
            log(f"  SKIP {dirname} — not found")
            continue

        files = sorted([f for f in os.listdir(dirpath) if f.endswith('.md')])
        log(f"\n  --- {dirname}/ ({len(files)} fichiers) ---")

        dir_downgraded = 0
        dir_bp = 0
        dir_useful = 0

        for filename in files:
            filepath = os.path.join(dirpath, filename)
            result = process_file(filepath, dry_run=args.dry_run)

            if result['status'] == 'skip':
                totals['skipped'] += 1
                continue

            totals['processed'] += 1

            if result['downgraded']:
                totals['downgraded'] += 1
                dir_downgraded += 1
            else:
                totals['useful_remaining'] += 1
                dir_useful += 1

            totals['bp_removed'] += result['bp_removed']
            dir_bp += result['bp_removed']

        log(f"    Downgraded→L4: {dir_downgraded}, Boilerplate lines removed: {dir_bp}, Useful remaining: {dir_useful}")

    log(f"\n{'='*60}")
    log(f"=== BILAN ===")
    log(f"  Fichiers traités: {totals['processed']} ({totals['skipped']} skippés)")
    log(f"  Downgraded → L4: {totals['downgraded']}")
    log(f"  Boilerplate lines removed: {totals['bp_removed']}")
    log(f"  Useful remaining (L2/L3): {totals['useful_remaining']}")
    log(f"{'='*60}")


if __name__ == '__main__':
    main()
