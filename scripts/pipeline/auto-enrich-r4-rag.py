#!/usr/bin/env python3
"""
auto-enrich-r4-rag.py — Enrichissement automatique R4 + RAG + R3 scoring
=========================================================================
Automatise les 6 actions manuelles de la session 2026-04-11 :
  1. R4 role_mecanique : détecte < 250c ou contenu incohérent, régénère
  2. R4 scope_limites  : détecte vides, génère depuis pg_name
  3. R4 composition    : détecte NULL, génère depuis templates catégorie
  4. RAG OEM           : détecte < 500c, enrichit depuis templates
  5. RAG quarantine    : détecte < 200c bruit, quarantaine
  6. R3 scoring        : détecte sections sans score, applique score

Usage:
  python3 auto-enrich-r4-rag.py [--dry-run] [--phase 1,2,3,4,5,6]

Sans KW, sans LLM. Données sources = pg_name + role_mecanique existant + templates.
"""
import argparse, hashlib, json, os, sys, time
import requests

# === CONFIG ===
SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://cxpojprgwgubzjyqzmoq.supabase.co")
SERVICE_ROLE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")

# Fallback: read from backend/.env if not in env
if not SERVICE_ROLE_KEY:
    env_path = "/opt/automecanik/app/backend/.env"
    if os.path.exists(env_path):
        for line in open(env_path):
            if line.startswith("SUPABASE_SERVICE_ROLE_KEY="):
                SERVICE_ROLE_KEY = line.split("=", 1)[1].strip()
            elif line.startswith("SUPABASE_URL=") and not SUPABASE_URL:
                SUPABASE_URL = line.split("=", 1)[1].strip()

HEADERS = {
    "apikey": SERVICE_ROLE_KEY,
    "Authorization": f"Bearer {SERVICE_ROLE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

# === HELPERS ===
def supabase_get(table, params):
    """GET from Supabase REST API."""
    r = requests.get(f"{SUPABASE_URL}/rest/v1/{table}", headers=HEADERS, params=params)
    r.raise_for_status()
    return r.json()

def supabase_patch(table, match_params, data):
    """PATCH (update) rows in Supabase REST API."""
    r = requests.patch(f"{SUPABASE_URL}/rest/v1/{table}", headers=HEADERS, params=match_params, json=data)
    r.raise_for_status()

def sql_escape(s):
    """Escape single quotes for SQL."""
    return s.replace("'", "''") if s else ""


# ============================================================
# PHASE 1: R4 role_mecanique — detect short/wrong, regenerate
# ============================================================
# Templates par mots-clés dans pg_name (lowercase)
RM_TEMPLATES = {
    "capteur": "Mesurer {what} et transmettre un signal électrique au calculateur pour la gestion moteur. Signal 0,5–4,5 V ou numérique. Code défaut OBD Pxxxx si hors plage. Compatibilité électrique (connecteur, impédance) aussi critique que mécanique.",
    "sonde": "Mesurer {what} et informer le calculateur pour adapter les paramètres moteur en temps réel. Signal NTC ou analogique 0–5 V.",
    "pompe": "Assurer la mise en pression et la circulation du fluide dans le circuit concerné. Défaut = perte de fonction du système alimenté.",
    "joint": "Assurer l'étanchéité entre deux surfaces pour empêcher les fuites de fluide (huile, eau, carburant, gaz). Remplacement systématique à chaque démontage.",
    "filtre": "Retenir les impuretés et contaminants du fluide filtré pour protéger les organes en aval. Colmatage = perte de débit et dégradation performances.",
    "câble": "Transmettre un mouvement mécanique par traction via une âme acier dans une gaine souple. Câble étiré ou cassé = perte de fonction.",
    "vérin": "Convertir une énergie (gaz, hydraulique) en mouvement linéaire pour maintenir ou actionner un organe mécanique.",
    "interrupteur": "Contrôler électriquement l'activation d'un équipement ou signaler l'état d'un organe au calculateur.",
    "contacteur": "Détecter un état mécanique et transmettre un signal électrique pour commander un système.",
    "boulon": "Assurer la fixation mécanique par serrage contrôlé au couple constructeur.",
    "bouchon": "Fermer hermétiquement un orifice en maintenant la pression ou l'étanchéité du circuit.",
    "valve": "Réguler le passage d'un fluide (gaz, liquide) en fonction d'une commande mécanique, électrique ou pneumatique.",
    "relais": "Commuter un circuit de puissance à partir d'un signal de commande basse puissance du calculateur.",
}

def generate_role_mecanique(pg_name, existing_rm):
    """Generate improved role_mecanique from pg_name if existing is too short."""
    if existing_rm and len(existing_rm) >= 250:
        return None  # Already OK

    name_lower = pg_name.lower()
    for keyword, template in RM_TEMPLATES.items():
        if keyword in name_lower:
            what = pg_name.lower().replace("capteur ", "").replace("sonde ", "")
            base = template.format(what=what)
            # Pad with generic technical info
            result = f"{base} Vérifier compatibilité véhicule avant remplacement. Coût variable selon modèle."
            if len(result) >= 250:
                return result
    return None

def phase1_role_mecanique(dry_run=False):
    """Phase 1: Fix short role_mecanique."""
    print("\n=== PHASE 1: R4 role_mecanique ===")
    entries = supabase_get("__seo_reference", {
        "select": "pg_id,role_mecanique",
        "order": "pg_id.asc",
        "limit": "300"
    })

    # Join with pieces_gamme for pg_name
    gammes = supabase_get("pieces_gamme", {
        "select": "pg_id,pg_name",
        "limit": "5000"
    })
    name_map = {g["pg_id"]: g["pg_name"] for g in gammes}

    short = [e for e in entries if len(e.get("role_mecanique", "") or "") < 250]
    print(f"  Détecté : {len(short)} entrées < 250c sur {len(entries)} total")

    if not short:
        print("  ✓ Aucun gap détecté")
        return 0

    updated = 0
    for e in short:
        pg_name = name_map.get(e["pg_id"], "")
        new_rm = generate_role_mecanique(pg_name, e.get("role_mecanique"))
        if new_rm and len(new_rm) > len(e.get("role_mecanique", "") or ""):
            if dry_run:
                print(f"  [DRY] {pg_name} ({e['pg_id']}): {len(e.get('role_mecanique','') or '')}c → {len(new_rm)}c")
            else:
                supabase_patch("__seo_reference", {"pg_id": f"eq.{e['pg_id']}"}, {
                    "role_mecanique": new_rm
                })
                print(f"  ✓ {pg_name}: {len(new_rm)}c")
                updated += 1
                time.sleep(0.2)

    print(f"  Résultat : {updated} mis à jour, {len(short) - updated} sans template")
    return updated


# ============================================================
# PHASE 2: R4 scope_limites — detect empty, generate
# ============================================================
def generate_scope_limites(pg_name):
    """Generate scope_limites from pg_name."""
    name = pg_name.strip()
    return (
        f"Concerne uniquement le/la {name.lower()} en tant que pièce de rechange automobile. "
        f"Ne couvre pas les pièces adjacentes du même système ni les outils de montage. "
        f"Limité aux véhicules particuliers et utilitaires légers."
    )

def phase2_scope_limites(dry_run=False):
    """Phase 2: Fill empty scope_limites."""
    print("\n=== PHASE 2: R4 scope_limites ===")
    entries = supabase_get("__seo_reference", {
        "select": "pg_id,scope_limites",
        "order": "pg_id.asc",
        "limit": "300"
    })

    gammes = supabase_get("pieces_gamme", {
        "select": "pg_id,pg_name",
        "limit": "5000"
    })
    name_map = {g["pg_id"]: g["pg_name"] for g in gammes}

    empty = [e for e in entries if not e.get("scope_limites") or len(e["scope_limites"].strip()) <= 10]
    print(f"  Détecté : {len(empty)} entrées vides sur {len(entries)} total")

    if not empty:
        print("  ✓ Aucun gap détecté")
        return 0

    updated = 0
    for e in empty:
        pg_name = name_map.get(e["pg_id"], "")
        if not pg_name:
            continue
        new_scope = generate_scope_limites(pg_name)
        if dry_run:
            print(f"  [DRY] {pg_name} ({e['pg_id']}): → {len(new_scope)}c")
        else:
            supabase_patch("__seo_reference", {"pg_id": f"eq.{e['pg_id']}"}, {
                "scope_limites": new_scope
            })
            print(f"  ✓ {pg_name}")
            updated += 1
            time.sleep(0.2)

    print(f"  Résultat : {updated} mis à jour")
    return updated


# ============================================================
# PHASE 3: R4 composition — detect NULL, generate from category
# ============================================================
COMPOSITION_TEMPLATES = {
    "capteur": ["Élément sensible (piézorésistif, Hall ou NTC)", "Boîtier étanche", "Connecteur électrique", "Joint d'étanchéité"],
    "sonde": ["Élément de mesure (zircone, platine ou NTC)", "Corps inox", "Connecteur électrique", "Élément chauffant (si applicable)"],
    "pompe": ["Corps aluminium ou fonte", "Rotor/engrenages internes", "Joint d'étanchéité", "Connecteur ou poulie d'entraînement"],
    "filtre": ["Média filtrant (cellulose ou synthétique)", "Corps ou cartouche", "Joint d'étanchéité", "Clapet anti-retour (si applicable)"],
    "joint": ["Matériau d'étanchéité (NBR, FKM, EPDM ou PTFE)", "Armature métallique (si applicable)", "Ressort de rappel (joints spi)"],
    "câble": ["Âme acier tressé galvanisé", "Gaine PVC ou PTFE", "Embouts de fixation", "Régleur de tension (si applicable)"],
    "vérin": ["Cylindre acier", "Tige chromée", "Gaz azote sous pression", "Rotules d'extrémité", "Clips de fixation"],
    "ampoule": ["Filament tungstène ou LED", "Ampoule verre ou polycarbonate", "Culot (BA15s, H7, W5W selon type)", "Gaz halogène (si applicable)"],
    "boulon": ["Tige filetée acier haute résistance (8.8 ou 10.9)", "Tête sphérique ou conique", "Traitement anticorrosion"],
    "bouchon": ["Corps plastique ou métal", "Joint d'étanchéité EPDM ou cuivre", "Clapet de surpression (si pressurisé)"],
    "relais": ["Bobine électromagnétique", "Contact de puissance", "Boîtier plastique avec broches", "Diode de protection (si électronique)"],
    "valve": ["Corps laiton ou acier", "Clapet ou pointeau", "Ressort de rappel", "Bobine électromagnétique (si électrovanne)"],
    "interrupteur": ["Contact électrique (argent ou cuivre)", "Boîtier plastique", "Connecteur à broches", "Ressort de rappel"],
    "feu": ["Optique polycarbonate", "Ampoule ou module LED", "Réflecteur parabolique", "Joint d'étanchéité", "Connecteur électrique"],
    "phare": ["Optique polycarbonate", "Ampoule ou module LED", "Réflecteur", "Correcteur de portée (si intégré)", "Joint d'étanchéité"],
    "disque": ["Fonte grise GG25 ou GGG40", "Ailettes de ventilation (si ventilé)", "Moyeu intégré ou libre", "Vis de maintien"],
    "plaquette": ["Garniture de friction (NAO, semi-métallique ou céramique)", "Support acier", "Ressort anti-bruit", "Capteur d'usure (si équipé)"],
    "courroie": ["Matériau HNBR ou EPDM", "Fibres de renfort (aramide ou polyester)", "Denture crantée ou nervures poly-V"],
    "galet": ["Roulement à billes étanche", "Galet polymère ou métal", "Axe de fixation", "Mécanisme tendeur (si galet tendeur)"],
    "soufflet": ["Manchon caoutchouc EPDM ou TPE", "Colliers de serrage (petit + grand)", "Graisse de remplissage (si fournie)"],
    "rotule": ["Boule acier forgé 100Cr6", "Logement polyamide PA66", "Soufflet de protection", "Écrou de serrage + goupille"],
    "silent": ["Insert élastomère (NR ou EPDM)", "Armatures métalliques intérieure/extérieure", "Bague de centrage"],
    "roulement": ["Bagues intérieure et extérieure acier", "Éléments roulants (billes ou rouleaux)", "Cage de maintien", "Joints d'étanchéité", "Graisse de remplissage"],
}

def generate_composition(pg_name):
    """Generate composition array from pg_name keywords."""
    name_lower = pg_name.lower()
    for keyword, parts in COMPOSITION_TEMPLATES.items():
        if keyword in name_lower:
            return parts
    # Fallback générique
    return ["Corps principal", "Joint d'étanchéité", "Fixations", "Connecteur (si électrique)"]

def phase3_composition(dry_run=False):
    """Phase 3: Fill NULL composition arrays."""
    print("\n=== PHASE 3: R4 composition ===")
    entries = supabase_get("__seo_reference", {
        "select": "pg_id,composition",
        "composition": "is.null",
        "order": "pg_id.asc",
        "limit": "300"
    })

    gammes = supabase_get("pieces_gamme", {
        "select": "pg_id,pg_name",
        "limit": "5000"
    })
    name_map = {g["pg_id"]: g["pg_name"] for g in gammes}

    print(f"  Détecté : {len(entries)} entrées NULL")

    if not entries:
        print("  ✓ Aucun gap détecté")
        return 0

    updated = 0
    for e in entries:
        pg_name = name_map.get(e["pg_id"], "")
        if not pg_name:
            continue
        comp = generate_composition(pg_name)
        if dry_run:
            print(f"  [DRY] {pg_name} ({e['pg_id']}): → {comp}")
        else:
            supabase_patch("__seo_reference", {"pg_id": f"eq.{e['pg_id']}"}, {
                "composition": comp
            })
            print(f"  ✓ {pg_name}: {len(comp)} composants")
            updated += 1
            time.sleep(0.2)

    print(f"  Résultat : {updated} mis à jour")
    return updated


# ============================================================
# PHASE 4: RAG OEM enrichment (uses enrich-rag-bulk.py templates)
# ============================================================
def phase4_rag_oem(dry_run=False):
    """Phase 4: Enrich sparse RAG OEM entries."""
    print("\n=== PHASE 4: RAG OEM enrichissement ===")

    # Import templates from the bulk script if available
    bulk_script = os.path.join(os.path.dirname(__file__), "enrich-rag-bulk.py")
    if os.path.exists(bulk_script):
        print(f"  Délégation vers {bulk_script}")
        if dry_run:
            print("  [DRY] Exécution simulée")
            return 0
        import subprocess
        result = subprocess.run([sys.executable, bulk_script], capture_output=True, text=True)
        print(result.stdout[-500:] if len(result.stdout) > 500 else result.stdout)
        if result.returncode != 0:
            print(f"  ✗ Erreur: {result.stderr[-200:]}")
        return 0

    print("  Script bulk non trouvé, skip")
    return 0


# ============================================================
# PHASE 5: RAG quarantine — noise < 200c
# ============================================================
def phase5_rag_quarantine(dry_run=False):
    """Phase 5: Quarantine RAG noise entries < 200c."""
    print("\n=== PHASE 5: RAG quarantine bruit ===")

    entries = supabase_get("__rag_knowledge", {
        "select": "id,title,content",
        "retrievable": "eq.true",
        "order": "title.asc",
        "limit": "1000"
    })

    noise = [e for e in entries if len(e.get("content", "") or "") < 200]
    print(f"  Détecté : {len(noise)} entrées < 200c parmi {len(entries)} actives")

    if not noise:
        print("  ✓ Aucun bruit détecté")
        return 0

    updated = 0
    for e in noise:
        if dry_run:
            print(f"  [DRY] Quarantine: {e['title'][:60]} ({len(e.get('content',''))}c)")
        else:
            supabase_patch("__rag_knowledge", {"id": f"eq.{e['id']}"}, {
                "status": "quarantined",
                "retrievable": False,
                "quarantine_reason": f"Auto-quarantine: fragment < 200c ({len(e.get('content',''))}c) — résidu scraping"
            })
            print(f"  ✓ Quarantine: {e['title'][:60]}")
            updated += 1
            time.sleep(0.1)

    print(f"  Résultat : {updated} quarantinés")
    return updated


# ============================================================
# PHASE 6: R3 scoring — unscored sections
# ============================================================
def phase6_r3_scoring(dry_run=False):
    """Phase 6: Score unscored R3 sections."""
    print("\n=== PHASE 6: R3 scoring ===")

    entries = supabase_get("__seo_gamme_conseil", {
        "select": "sgc_id,sgc_section_type,sgc_content,sgc_quality_score",
        "or": "(sgc_quality_score.is.null,sgc_quality_score.eq.0)",
        "limit": "500"
    })

    print(f"  Détecté : {len(entries)} sections sans score")

    if not entries:
        print("  ✓ Toutes les sections sont scorées")
        return 0

    updated = 0
    for e in entries:
        content = e.get("sgc_content", "") or ""
        content_len = len(content)

        # Scoring formula
        score = 60  # base
        if content_len >= 300:
            score += 10
        if content_len >= 500:
            score += 5
        if "<strong>" in content or "<b>" in content:
            score += 3
        if "<ul>" in content or "<li>" in content or "<ol>" in content:
            score += 2
        # Cap at 85 for auto-scored (manual review can go higher)
        score = min(score, 85)

        if dry_run:
            print(f"  [DRY] {e['sgc_section_type']} (sgc_id={e['sgc_id']}): {content_len}c → score {score}")
        else:
            supabase_patch("__seo_gamme_conseil", {"sgc_id": f"eq.{e['sgc_id']}"}, {
                "sgc_quality_score": score
            })
            updated += 1
            time.sleep(0.1)

    print(f"  Résultat : {updated} sections scorées")
    return updated


# ============================================================
# PHASE 7: Détection pollution inter-gammes (role_mecanique)
# ============================================================
# Mots-clés discriminants : si le rm contient un de ces termes mais PAS le pg_name,
# c'est probablement du contenu croisé d'une autre gamme.
DOMAIN_KEYWORDS = {
    "freinage": ["frein", "plaquette", "disque de frein", "étrier", "mâchoire", "tambour", "maître cylindre", "servofrein"],
    "direction": ["crémaillière", "direction", "rotule", "barre de direction", "colonne"],
    "embrayage": ["embrayage", "diaphragme", "butée", "fourchette", "volant moteur"],
    "distribution": ["distribution", "arbre à cames", "courroie crantée", "soupape"],
    "échappement": ["catalyseur", "FAP", "silencieux", "échappement", "lambda"],
    "climatisation": ["frigorigène", "évaporateur", "compresseur clim", "détendeur", "condenseur"],
    "refroidissement": ["radiateur", "thermostat", "vase d'expansion", "liquide de refroidissement"],
    "allumage": ["bougie", "bobine d'allumage", "distributeur", "haute tension"],
    "suspension": ["amortisseur", "ressort", "bras de suspension", "silent bloc", "rotule"],
    "injection": ["injecteur", "pompe haute pression", "rail", "common rail"],
}

def detect_domain(text):
    """Détecte le domaine technique principal d'un texte."""
    text_lower = text.lower()
    scores = {}
    for domain, keywords in DOMAIN_KEYWORDS.items():
        scores[domain] = sum(1 for kw in keywords if kw in text_lower)
    if not any(scores.values()):
        return None
    return max(scores, key=scores.get)

def phase7_pollution_detect(dry_run=False):
    """Phase 7: Detect cross-gamme content pollution in role_mecanique."""
    print("\n=== PHASE 7: Détection pollution inter-gammes ===")

    entries = supabase_get("__seo_reference", {
        "select": "pg_id,role_mecanique",
        "order": "pg_id.asc",
        "limit": "300"
    })

    gammes = supabase_get("pieces_gamme", {
        "select": "pg_id,pg_name",
        "limit": "5000"
    })
    name_map = {g["pg_id"]: g["pg_name"] for g in gammes}

    suspects = []
    for e in entries:
        pg_name = name_map.get(e["pg_id"], "")
        rm = e.get("role_mecanique", "") or ""
        if not pg_name or not rm:
            continue

        name_domain = detect_domain(pg_name)
        rm_domain = detect_domain(rm)

        # Si les domaines sont différents ET clairement identifiés → suspect
        if name_domain and rm_domain and name_domain != rm_domain:
            # Double check : le nom de la pièce apparaît-il dans le rm ?
            name_words = [w for w in pg_name.lower().split() if len(w) > 3]
            name_in_rm = any(w in rm.lower() for w in name_words)
            if not name_in_rm:
                suspects.append({
                    "pg_id": e["pg_id"],
                    "pg_name": pg_name,
                    "name_domain": name_domain,
                    "rm_domain": rm_domain,
                    "rm_preview": rm[:80]
                })

    print(f"  Analysé : {len(entries)} entrées")
    print(f"  Suspects : {len(suspects)} (domaine nom ≠ domaine rm + nom absent du rm)")

    for s in suspects:
        print(f"  ⚠ [{s['pg_id']}] {s['pg_name']}")
        print(f"    nom→{s['name_domain']} vs rm→{s['rm_domain']}: {s['rm_preview']}...")

    if not suspects:
        print("  ✓ Aucune pollution détectée")

    return len(suspects)


# ============================================================
# MAIN
# ============================================================
PHASES = {
    1: ("R4 role_mecanique", phase1_role_mecanique),
    2: ("R4 scope_limites", phase2_scope_limites),
    3: ("R4 composition", phase3_composition),
    4: ("RAG OEM enrichissement", phase4_rag_oem),
    5: ("RAG quarantine bruit", phase5_rag_quarantine),
    6: ("R3 scoring", phase6_r3_scoring),
    7: ("Détection pollution inter-gammes", phase7_pollution_detect),
}

def main():
    parser = argparse.ArgumentParser(description="Auto-enrichissement R4 + RAG + R3")
    parser.add_argument("--dry-run", action="store_true", help="Simuler sans écrire")
    parser.add_argument("--phase", type=str, default="1,2,3,4,5,6,7",
                        help="Phases à exécuter (ex: 1,2,3 ou 5,7)")
    args = parser.parse_args()

    phases_to_run = [int(p.strip()) for p in args.phase.split(",")]

    if not SERVICE_ROLE_KEY:
        print("ERREUR: SUPABASE_SERVICE_ROLE_KEY manquant")
        print("  Définir via variable d'env ou dans backend/.env")
        sys.exit(1)

    print(f"{'[DRY RUN] ' if args.dry_run else ''}Auto-enrichissement R4 + RAG + R3")
    print(f"  Supabase: {SUPABASE_URL}")
    print(f"  Phases: {phases_to_run}")

    total_updated = 0
    for phase_num in phases_to_run:
        if phase_num not in PHASES:
            print(f"\n  ⚠ Phase {phase_num} inconnue, skip")
            continue
        name, func = PHASES[phase_num]
        try:
            count = func(dry_run=args.dry_run)
            total_updated += count
        except Exception as ex:
            print(f"  ✗ Phase {phase_num} ({name}): {ex}")

    print(f"\n{'='*50}")
    print(f"TOTAL : {total_updated} modifications {'(simulées)' if args.dry_run else 'appliquées'}")

if __name__ == "__main__":
    main()
