#!/usr/bin/env python3
"""Standalone RAG reindex script with anchored chunking and canonical layer."""

import os
import sys
import re
import gc
import uuid
import yaml
import hashlib
import argparse
import logging
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Any, Generator, Tuple

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.services.gamme_page_contract import build_and_validate_gamme_page_contract
from app.config import get_settings
from orchestrator.processors.role_classifier import classify_chunk

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

_settings = get_settings()
DEFAULT_KNOWLEDGE_PATH = _settings.knowledge_path
DEFAULT_WEAVIATE_URL = _settings.weaviate_url
DEFAULT_WEAVIATE_GRPC_PORT = _settings.weaviate_grpc_port
DEFAULT_COLLECTION = "KB_Knowledge"
DEFAULT_BATCH_SIZE = int(os.environ.get("REINDEX_BATCH_SIZE", "10"))
FASTEMBED_MODEL = _settings.fastembed_model
ALLOWED_ENVIRONMENTS = frozenset(["dev", "development", "ci", "staging", "test"])

TARGET_MAX_TOKENS = _settings.reindex_target_max_tokens
CANONICAL_MIN_TOKENS = 100
CANONICAL_MAX_TOKENS = 250

ALLOWED_INTENTS = {
    "define", "choose", "do", "maintain", "compare", "cost", "policy", "troubleshoot", "fitment"
}
ALLOWED_TRUTH_LEVELS = {"L1", "L2", "L3", "L4"}
ALLOWED_VERIFICATION_STATUS = {"verified", "unverified", "disputed"}
ALLOWED_DOMAINS = {"general", "freinage", "moteur", "climatisation", "suspension", "transmission", "electrique", "eclairage", "refroidissement", "filtration", "embrayage", "distribution", "echappement", "direction", "carrosserie", "demarrage", "essuyage", "allumage", "vehicule", "catalog"}

COLLECTION_BY_FAMILY = {
    "catalog": "KB_Catalog",
    "diagnostic": "KB_Diagnostic",
    "knowledge": "KB_Knowledge",
}

SOURCE_TYPE_TO_DEFAULT_INTENT = {
    "diagnostic": "troubleshoot",
    "gamme": "choose",
    "faq": "define",
    "guide": "do",
    "vehicle": "fitment",
    "policy": "policy",
    "knowledge": "define",
    "canonical": "define",
}

DIR_TO_SOURCE_TYPE = {
    "diagnostic": "diagnostic", "diagnostics": "diagnostic",
    "gamme": "gamme", "gammes": "gamme", "catalog": "gamme",
    "faq": "faq", "faqs": "faq",
    "guide": "guide", "guides": "guide",
    "vehicle": "vehicle", "vehicles": "vehicle",
    "policy": "policy", "policies": "policy", "knowledge": "knowledge", "canonical": "canonical",
}

# V3 gamme template: H2 heading (lowercase) -> per-chunk intent override
V3_H2_INTENT_MAP = {
    "reference technique": "define",
    "diagnostic": "troubleshoot",
    "guide d achat": "choose",
    "entretien": "maintain",
}


def is_v3_gamme(metadata: Dict[str, Any], content: str) -> bool:
    """Detect if a gamme file uses the V3 template (4 canonical H2 sections)."""
    if str(metadata.get("source_type", "")).lower() != "gamme":
        return False
    content_lower = content.lower()
    return all(f"## {h}" in content_lower for h in V3_H2_INTENT_MAP)

DOMAIN_KEYWORDS = {
    "freinage": ["frein", "disque", "plaquette", "etrier", "mastervac", "abs"],
    "moteur": ["moteur", "huile", "courroie", "distribution", "bougie", "injecteur", "turbo"],
    "climatisation": ["clim", "condenseur", "compresseur", "habitacle"],
    "suspension": ["amortisseur", "suspension", "triangle", "rotule", "silentbloc"],
    "transmission": ["embrayage", "boite", "cardan", "transmission"],
    "electrique": ["batterie", "alternateur", "demarreur", "capteur", "faisceau"],
}

ENTITY_PATTERNS = [
    r"\b[Bb]osch\b",
    r"\b[Aa][Tt][Ee]\b",
    r"\b[Vv][Ii][Nn]\b",
    r"\b[A-Z]{2,6}\d{2,6}[A-Z0-9-]*\b",
]

TRUTH_TO_DOC_WEIGHT = {"L1": 1.0, "L2": 0.85, "L3": 0.65, "L4": 0.45}

PDF_PAGE_MARKER_RE = re.compile(r"\[\[PDF_PAGE:(\d+)\]\]")
BBOX_MARKER_RE = re.compile(r"\[\[BBOX:(\d+),(\d+),(\d+),(\d+)\]\]")
VIDEO_TS_MARKER_RE = re.compile(r"\[\[VIDEO_TS:([0-9:.]+)-([0-9:.]+)\]\]")


def resolve_doc_family(source_type: str) -> str:
    if source_type in {"image", "video", "audio", "media"}:
        return "media"
    if source_type in {"faq", "policy", "support"}:
        return "knowledge"
    if source_type in {"gamme", "catalog"}:
        return "catalog"
    if source_type == "diagnostic":
        return "diagnostic"
    if source_type == "canonical":
        return "knowledge"
    return "knowledge"


def route_collection_for_family(doc_family: str) -> str:
    fam = (doc_family or "").strip().lower()
    if fam in COLLECTION_BY_FAMILY:
        return COLLECTION_BY_FAMILY[fam]
    return "KB_Knowledge"


def enforce_build_plane():
    env = os.environ.get("ENV", "").lower()
    if env not in ALLOWED_ENVIRONMENTS:
        logger.error(f"KILL SWITCH: ENV={env} not in allowed list {ALLOWED_ENVIRONMENTS}")
        sys.exit(1)
    logger.info(f"BUILD plane confirmed (ENV={env})")


def estimate_tokens(text: str) -> int:
    # Pragmatic heuristic for FR markdown without external tokenizer.
    return max(1, int(len(re.findall(r"\S+", text)) * 1.3))


def parse_frontmatter(content: str) -> Dict[str, Any]:
    if not content.startswith("---"):
        return {}
    try:
        end_idx = content.find("---", 3)
        if end_idx == -1:
            return {}
        return yaml.safe_load(content[3:end_idx].strip()) or {}
    except Exception:
        return {}


def strip_frontmatter(content: str) -> str:
    if not content.startswith("---"):
        return content.strip()
    end_idx = content.find("\n---", 3)
    if end_idx == -1:
        return content.strip()
    return content[end_idx + 4:].lstrip("\n").strip()

def resolve_source_type(metadata: Dict[str, Any], rel_path: str) -> str:
    st = metadata.get("source_type")
    if st:
        return str(st)
    et = metadata.get("entity_type")
    if et and et != "unknown":
        return str(et)
    parts = rel_path.split("/")
    if parts:
        return DIR_TO_SOURCE_TYPE.get(parts[0].lower(), "general")
    return "general"


def infer_intent_rules(text: str, source_type: str) -> str:
    t = text.lower()
    if any(k in t for k in ["sympt", "panne", "diagnostic", "bruit", "vibration", "voyant"]):
        return "troubleshoot"
    if any(k in t for k in ["compatibil", "vin", "immatriculation", "vehicule"]):
        return "fitment"
    if any(k in t for k in ["livraison", "retour", "garantie", "remboursement", "cgv"]):
        return "policy"
    if any(k in t for k in ["prix", "tarif", "cout", "promo"]):
        return "cost"
    if any(k in t for k in ["comment", "tutoriel", "etape", "installer", "remplacer"]):
        return "do"
    if any(k in t for k in ["entretien", "maintenance", "intervalle"]):
        return "maintain"
    if any(k in t for k in ["difference", "versus", "compar"]):
        return "compare"
    if any(k in t for k in ["definition", "c'est quoi", "que signifie"]):
        return "define"
    return SOURCE_TYPE_TO_DEFAULT_INTENT.get(source_type, "define")


def normalize_intent(metadata: Dict[str, Any], source_type: str, content: str) -> str:
    raw = str(metadata.get("intent", "")).strip().lower()
    if raw in ALLOWED_INTENTS:
        return raw
    return infer_intent_rules(content, source_type)


def infer_domain_rules(text: str) -> str:
    t = text.lower()
    scores: Dict[str, int] = {}
    for domain, keywords in DOMAIN_KEYWORDS.items():
        scores[domain] = sum(1 for kw in keywords if kw in t)
    best_domain, best_score = max(scores.items(), key=lambda kv: kv[1])
    return best_domain if best_score > 0 else "general"


def normalize_domain(metadata: Dict[str, Any], content: str) -> str:
    raw = metadata.get("domain", "")
    if isinstance(raw, dict):
        # v4 frontmatter: domain is an object with role/must_be_true/etc.
        # The technical domain is in 'category', not 'domain.role' (which is the mechanical description)
        domain = ""
    else:
        domain = str(raw).strip().lower()
    # Fallback to category field (canonical domain for gamme files)
    if not domain or domain not in ALLOWED_DOMAINS:
        cat = str(metadata.get("category", "")).strip().lower()
        if cat in ALLOWED_DOMAINS:
            domain = cat
        # Try extracting from category like "catalog/gamme" -> use parent domain
        elif "/" in cat:
            parent = cat.split("/")[0]
            if parent in ALLOWED_DOMAINS:
                domain = parent
    if domain and domain in ALLOWED_DOMAINS:
        return domain
    return infer_domain_rules(content)


def normalize_entities(metadata: Dict[str, Any], content: str) -> List[str]:
    value = metadata.get("entities")
    if isinstance(value, list):
        existing = [str(v).strip() for v in value if str(v).strip()]
    elif isinstance(value, str):
        existing = [v.strip() for v in value.split(",") if v.strip()]
    else:
        existing = []

    if existing:
        return existing

    found = []
    for pattern in ENTITY_PATTERNS:
        found.extend(re.findall(pattern, content))

    deduped = []
    seen = set()
    for e in found:
        norm = e.strip()
        if norm and norm not in seen:
            seen.add(norm)
            deduped.append(norm)
    return deduped[:20]


def extract_anchors(markdown: str) -> List[str]:
    anchors = []
    for line in markdown.splitlines():
        if line.startswith("## ") or line.startswith("### "):
            heading = re.sub(r"\s+", " ", line.lstrip("#").strip())
            if heading:
                anchors.append(heading)
    seen = set()
    out = []
    for a in anchors:
        if a not in seen:
            seen.add(a)
            out.append(a)
    return out


def normalize_verification_status(metadata: Dict[str, Any], truth_level: str) -> str:
    raw = str(metadata.get("verification_status", "")).strip().lower()
    if raw in {"verified", "unverified", "disputed"}:
        return raw
    return "verified" if truth_level in {"L1", "L2"} else "unverified"


def normalize_doc_weight(metadata: Dict[str, Any], truth_level: str) -> float:
    value = metadata.get("doc_weight")
    if isinstance(value, (float, int)):
        return max(0.0, min(1.0, float(value)))
    return TRUTH_TO_DOC_WEIGHT.get(truth_level, 0.7)


def normalize_updated_at(metadata: Dict[str, Any], path: Path) -> str:
    raw = metadata.get("updated_at")
    if isinstance(raw, str) and raw.strip():
        return raw.strip()
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).isoformat()


def normalize_created_at(metadata: Dict[str, Any], path: Path) -> str:
    raw = metadata.get("created_at")
    if isinstance(raw, str) and raw.strip():
        return raw.strip()
    return datetime.fromtimestamp(path.stat().st_ctime, tz=timezone.utc).isoformat()




def chunk_document_anchored(doc: Dict[str, Any]) -> List[Tuple[str, str]]:
    """Chunk document content by headings.

    Delegates splitting to TokenAwareChunker (FAQ, procedure, merge-aware).
    Returns list of (chunk_text, parent_h2) tuples for downstream enrichment.
    """
    from orchestrator.processors.chunker import TokenAwareChunker

    chunker = TokenAwareChunker(
        chunk_size=TARGET_MAX_TOKENS,
        chunk_overlap=50,
        min_chunk_size=50,  # Low threshold: original code never dropped small sections
    )
    raw_chunks = chunker.chunk(doc["content"])

    if not raw_chunks:
        return []

    # Derive parent_h2 from heading metadata (track last H2 seen)
    result: List[Tuple[str, str]] = []
    last_h2 = ""
    for chunk in raw_chunks:
        heading = chunk.get("heading") or ""
        level = chunk.get("heading_level")
        if level == 2:
            last_h2 = heading
        text = chunk["content"].strip()
        if text:
            result.append((text, last_h2))

    return result


def build_canonical_snippet(text: str) -> str:
    words = re.findall(r"\S+", text)
    if not words:
        return ""
    # Approximate 100-250 tokens -> ~80-190 words
    min_words = 80
    max_words = 190
    selected = words[:max_words]
    if len(selected) < min_words:
        return ""
    snippet = " ".join(selected)
    return snippet.strip()


def iter_documents(knowledge_path: str, max_files: int = 0) -> Generator[Dict[str, Any], None, None]:
    path = Path(knowledge_path)
    if not path.exists():
        logger.error(f"Knowledge path not found: {knowledge_path}")
        return

    yielded = 0
    ignored_dirs = {"_trash", "_raw", "__pycache__", "_quarantine"}
    for md_file in path.rglob("*.md"):
        if md_file.name == "README.md" or ".backup" in str(md_file):
            continue
        rel_parts = md_file.relative_to(path).parts
        if any(part in ignored_dirs for part in rel_parts):
            continue
        try:
            content_raw = md_file.read_text(encoding="utf-8")
            relative_path = str(md_file.relative_to(path))
            metadata = parse_frontmatter(content_raw)
            content = strip_frontmatter(content_raw)
            source_type = resolve_source_type(metadata, relative_path)
            truth_level = str(metadata.get("truth_level", "L2"))

            intent = normalize_intent(metadata, source_type, content)
            domain = normalize_domain(metadata, content)
            entities = normalize_entities(metadata, content)

            # Extract gamme_slug for per-gamme role_map config (v2.5)
            gamme_slug = None
            if source_type.lower() == "gamme":
                gamme_slug = str(metadata.get("slug", "")).strip() or md_file.stem

            gamme_page_contract = None
            gamme_contract_errors: List[str] = []
            gamme_contract_warnings: List[str] = []
            if source_type.lower() == "gamme":
                contract_result = build_and_validate_gamme_page_contract(
                    metadata=metadata,
                    content=content,
                    source_path=relative_path,
                )
                gamme_page_contract = contract_result.get("contract")
                gamme_contract_errors = contract_result.get("errors", [])
                gamme_contract_warnings = contract_result.get("warnings", [])
                for warning in gamme_contract_warnings:
                    logger.warning("gamme_contract warning %s: %s", relative_path, warning)

            yield {
                "_raw_metadata": metadata,
                "source_path": relative_path,
                "content": content,
                "title": str(metadata.get("title", md_file.stem)),
                "truth_level": truth_level,
                "source_type": source_type,
                "doc_family": resolve_doc_family(source_type),
                "intent": intent,
                "domain": domain,
                "entities": entities,
                "anchors": extract_anchors(content),
                "verification_status": normalize_verification_status(metadata, truth_level),
                "doc_weight": normalize_doc_weight(metadata, truth_level),
                "is_canonical": bool(metadata.get("is_canonical", False)),
                "canonical_weight": float(metadata.get("canonical_weight", 1.0) or 1.0),
                "created_at": normalize_created_at(metadata, md_file),
                "updated_at": normalize_updated_at(metadata, md_file),
                "category": str(metadata.get("category", source_type)),
                "language": str(metadata.get("language", "fr")),
                "confidence_score": float(metadata.get("confidence_score", 0.0) or 0.0),
                "last_verified_date": str(metadata.get("last_verified_date", "")),
                "verified_by": str(metadata.get("verified_by", "")),
                "source_uri_base": str(metadata.get("source_uri", "")).strip() or f"md://{relative_path}",
                "source_ref_base": str(metadata.get("source_ref", "")).strip(),
                "gamme_page_contract": gamme_page_contract,
                "gamme_contract_errors": gamme_contract_errors,
                "gamme_contract_warnings": gamme_contract_warnings,
                "gamme_contract_score": int(((gamme_page_contract or {}).get("quality", {}) or {}).get("score", 0)),
                "gamme_contract_flags": list((((gamme_page_contract or {}).get("quality", {}) or {}).get("flags", []) or [])),
                "gamme_slug": gamme_slug,
            }
            yielded += 1
            if max_files > 0 and yielded >= max_files:
                logger.info(f"Reached max_files={max_files}, stopping early")
                return
        except Exception as e:
            logger.error(f"Failed to read {md_file}: {e}")


def extract_pdf_pages(text: str) -> List[int]:
    pages = [int(m.group(1)) for m in PDF_PAGE_MARKER_RE.finditer(text)]
    if not pages:
        return []
    return sorted(set(pages))


def strip_pdf_page_markers(text: str) -> str:
    cleaned = PDF_PAGE_MARKER_RE.sub("", text)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def extract_bbox_ref(text: str) -> str:
    m = BBOX_MARKER_RE.search(text)
    if not m:
        return ""
    return f"{m.group(1)},{m.group(2)},{m.group(3)},{m.group(4)}"


def strip_bbox_markers(text: str) -> str:
    cleaned = BBOX_MARKER_RE.sub("", text)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def parse_hms_to_seconds(value: str) -> int:
    txt = (value or "").strip()
    if not txt:
        return 0
    main = txt.split(".", 1)[0]
    parts = main.split(":")
    try:
        if len(parts) == 3:
            h, m, s = parts
            return int(h) * 3600 + int(m) * 60 + int(s)
        if len(parts) == 2:
            m, s = parts
            return int(m) * 60 + int(s)
        return int(parts[0])
    except Exception:
        return 0


def format_hms(seconds: int) -> str:
    sec = max(0, int(seconds))
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def extract_video_ts_range(text: str) -> tuple[str, str] | None:
    matches = VIDEO_TS_MARKER_RE.findall(text or "")
    if not matches:
        return None
    starts = [parse_hms_to_seconds(m[0]) for m in matches]
    ends = [parse_hms_to_seconds(m[1]) for m in matches]
    if not starts or not ends:
        return None
    return format_hms(min(starts)), format_hms(max(ends))


def strip_video_ts_markers(text: str) -> str:
    cleaned = VIDEO_TS_MARKER_RE.sub("", text)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def format_source_uri(doc: Dict[str, Any], chunk_index: int, page_numbers: List[int]) -> str:
    base = str(doc.get("source_uri_base", "") or "").strip()
    if "#" in base:
        return base
    if base.startswith("db:"):
        return base
    if base.startswith("pdf://") and page_numbers:
        start = page_numbers[0]
        end = page_numbers[-1]
        if start == end:
            return f"{base}#p{start}"
        return f"{base}#p{start}-p{end}"
    if base.startswith("image://"):
        return f"{base}#chunk-{chunk_index}"
    if base:
        return f"{base}#chunk-{chunk_index}"
    return f"md://{doc['source_path']}#chunk-{chunk_index}"


def format_source_ref(doc: Dict[str, Any], chunk_index: int, page_numbers: List[int]) -> str:
    base = str(doc.get("source_uri_base", "") or "").strip()
    custom_ref = str(doc.get("source_ref_base", "") or "").strip()
    if custom_ref:
        return custom_ref if custom_ref.startswith("#") else f"#{custom_ref}"
    if "#" in base:
        return "#" + base.split("#", 1)[1]
    if base.startswith("pdf://") and page_numbers:
        start = page_numbers[0]
        end = page_numbers[-1]
        if start == end:
            return f"#p{start}"
        return f"#p{start}-p{end}"
    if base.startswith(("video://", "audio://")):
        return f"#t=chunk-{chunk_index}"
    if base.startswith("image://"):
        return f"#chunk-{chunk_index}"
    if base.startswith("db://"):
        return f"#row={chunk_index}"
    return f"#chunk-{chunk_index}"


def compute_evidence_grade(truth_level: str, verification_status: str, doc_weight: float) -> str:
    if verification_status == "verified" and truth_level in {"L1", "L2"} and doc_weight >= 0.85:
        return "A"
    if truth_level in {"L1", "L2", "L3"} and doc_weight >= 0.6:
        return "B"
    return "C"


def resolve_namespace(source_type: str) -> str:
    st = (source_type or "").lower()
    if st in {"image", "video", "audio", "media"}:
        return "knowledge:media"
    return f"knowledge:{st or 'general'}"


def build_chunk_record(doc: Dict[str, Any], chunk_text: str, chunk_index: int, parent_id: str, canonical: bool, page_numbers: List[int] | None = None, chunk_intent: str | None = None, heading: str | None = None, chunk_type: str = "text") -> Dict[str, Any]:
    suffix = "canonical" if canonical else "body"
    page_numbers = page_numbers or []
    bbox_ref = extract_bbox_ref(chunk_text)
    video_ts_range = extract_video_ts_range(chunk_text)
    clean_chunk = strip_bbox_markers(strip_pdf_page_markers(strip_video_ts_markers(chunk_text)))
    chunk_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{doc['source_path']}:{suffix}:{chunk_index}"))
    content_hash = hashlib.sha256(clean_chunk.encode("utf-8")).hexdigest()

    truth_level = "L4" if canonical else doc["truth_level"]
    verification_status = doc["verification_status"] if not canonical else "verified"
    doc_weight = 1.0 if canonical else doc["doc_weight"]
    source_uri = format_source_uri(doc, chunk_index, page_numbers)
    source_ref = format_source_ref(doc, chunk_index, page_numbers)
    if bbox_ref:
        source_ref = f"#bbox={bbox_ref}"
        base = str(doc.get("source_uri_base", "") or "").strip()
        if base.startswith("image://"):
            source_uri = f"{base}#bbox={bbox_ref}"
    elif video_ts_range:
        start, end = video_ts_range
        source_ref = f"#t={start}-{end}"
        base = str(doc.get("source_uri_base", "") or "").strip()
        if base:
            source_uri = f"{base}#t={start}-{end}"
    evidence_grade = compute_evidence_grade(truth_level, verification_status, doc_weight)
    canonical_weight = float(doc.get("canonical_weight", 1.0) or 1.0) if canonical else 0.0

    # Role classification (v2.5: config-driven, per-gamme aware)
    role_data = classify_chunk(heading=heading, chunk_type=chunk_type, content=clean_chunk, source_type=doc["source_type"], gamme_slug=doc.get("gamme_slug"))

    # Phase 3: derive page_contract_id from primary_role
    _ROLE_TO_CONTRACT = {
        "R1_ROUTER": "PageContractR1@1.0",
        "R3_GUIDE": "PageContractR3@1.0",
        "R3_CONSEILS": "PageContractR3@1.0",
        "R4_REFERENCE": "PageContractR4@1.0",
        "R5_DIAGNOSTIC": "PageContractR5@1.0",
    }
    page_contract_id = _ROLE_TO_CONTRACT.get(role_data.get("primary_role", ""), "")

    # Phase 3: media_slots_hint — MVP: only for table_rows and faq
    _chunk_kind = role_data.get("chunk_kind", "other")
    media_slots_hint = ""
    if _chunk_kind == "table_rows":
        media_slots_hint = '{"type":"table","variant":"specs_table"}'
    elif _chunk_kind == "faq":
        media_slots_hint = '{"type":"faq","variant":"faq_block"}'

    return {
        "uuid": chunk_id,
        "chunk_id": chunk_id,
        "parent_id": parent_id,
        "source_path": doc["source_path"],
        "source_uri": source_uri,
        "source_ref": source_ref,
        "title": doc["title"],
        "content": clean_chunk,
        "anchors": doc["anchors"],
        "intent": chunk_intent if chunk_intent and chunk_intent in ALLOWED_INTENTS else doc["intent"],
        "domain": doc["domain"],
        "entities": doc["entities"],
        "truth_level": truth_level,
        "verification_status": verification_status,
        "doc_weight": doc_weight,
        "evidence_grade": evidence_grade,
        "is_canonical": canonical,
        "canonical_weight": canonical_weight,
        "chunk_index": chunk_index,
        "created_at": doc["created_at"],
        "updated_at": doc["updated_at"],
        "content_hash": content_hash,
        "source_type": doc["source_type"],
        "doc_family": doc["doc_family"],
        "namespace": resolve_namespace(doc["source_type"]),
        "category": doc["category"],
        "language": doc["language"],
        "confidence_score": doc["confidence_score"],
        "last_verified_date": doc["last_verified_date"],
        "verified_by": doc["verified_by"],
        **role_data,
        "page_contract_id": page_contract_id,
        "media_slots_hint": media_slots_hint,
    }


def chunk_document(doc: Dict[str, Any]) -> List[Dict[str, Any]]:
    chunks: List[Dict[str, Any]] = []
    parent_id = str(uuid.uuid5(uuid.NAMESPACE_URL, doc["source_path"]))

    # Detect V3 gamme template for per-chunk intent
    raw_metadata = doc.get("_raw_metadata") or {}
    v3 = is_v3_gamme(raw_metadata, doc["content"])

    body_chunks = chunk_document_anchored(doc)  # List[(text, parent_h2)]
    chunk_index = 0
    for part_text, parent_h2 in body_chunks:
        page_numbers = extract_pdf_pages(part_text)
        clean_part = strip_pdf_page_markers(part_text)
        if not clean_part:
            continue
        # Resolve per-chunk intent from parent H2 (V3 only)
        chunk_intent = None
        if v3 and parent_h2:
            chunk_intent = V3_H2_INTENT_MAP.get(parent_h2.strip().lower())
        chunks.append(build_chunk_record(doc, clean_part, chunk_index, parent_id, canonical=False, page_numbers=page_numbers, chunk_intent=chunk_intent, heading=parent_h2))
        chunk_index += 1

    # Canonical layer: only from explicit canonical corpus/docs.
    if doc.get("is_canonical") or doc.get("source_type") == "canonical":
        canonical_added = 0
        for body_text, _ in body_chunks:
            page_numbers = extract_pdf_pages(body_text)
            canonical = build_canonical_snippet(strip_pdf_page_markers(body_text))
            if not canonical:
                continue
            tok = estimate_tokens(canonical)
            if tok < CANONICAL_MIN_TOKENS or tok > CANONICAL_MAX_TOKENS:
                continue
            chunks.append(build_chunk_record(doc, canonical, chunk_index, parent_id, canonical=True, page_numbers=page_numbers))
            chunk_index += 1
            canonical_added += 1

        if canonical_added == 0:
            fallback = build_canonical_snippet(strip_pdf_page_markers(doc["content"]))
            if fallback:
                tok = estimate_tokens(fallback)
                if CANONICAL_MIN_TOKENS <= tok <= CANONICAL_MAX_TOKENS:
                    chunks.append(build_chunk_record(doc, fallback, chunk_index, parent_id, canonical=True, page_numbers=extract_pdf_pages(doc["content"])))

    return chunks


def build_embedding_input(chunk: Dict[str, Any]) -> str:
    """
    Build embedding text from chunk body + structural hints.
    Important for retrieval quality: include title and anchors with the content.
    """
    title = str(chunk.get("title", "") or "").strip()
    anchors = chunk.get("anchors", []) or []
    if not isinstance(anchors, list):
        anchors = []
    anchors_text = " | ".join(str(a).strip() for a in anchors if str(a).strip())
    content = str(chunk.get("content", "") or "").strip()

    parts = []
    if title:
        parts.append(f"Title: {title}")
    if anchors_text:
        parts.append(f"Anchors: {anchors_text}")
    if content:
        parts.append(content)
    return "\n".join(parts).strip()


def get_weaviate_client(weaviate_url: str):
    import weaviate

    url_clean = weaviate_url.replace("http://", "").replace("https://", "")
    parts = url_clean.split(":")
    host = parts[0]
    port = int(parts[1]) if len(parts) > 1 else 8080

    return weaviate.connect_to_custom(
        http_host=host,
        http_port=port,
        http_secure=False,
        grpc_host=host,
        grpc_port=DEFAULT_WEAVIATE_GRPC_PORT,
        grpc_secure=False,
    )


def build_gold_properties():
    from weaviate.classes.config import Property, DataType
    return [
        Property(name="chunk_id", data_type=DataType.TEXT),
        Property(name="parent_id", data_type=DataType.TEXT),
        Property(name="source_path", data_type=DataType.TEXT),
        Property(name="source_uri", data_type=DataType.TEXT),
        Property(name="source_ref", data_type=DataType.TEXT),
        Property(name="title", data_type=DataType.TEXT),
        Property(name="content", data_type=DataType.TEXT),
        Property(name="anchors", data_type=DataType.TEXT_ARRAY),
        Property(name="intent", data_type=DataType.TEXT),
        Property(name="domain", data_type=DataType.TEXT),
        Property(name="entities", data_type=DataType.TEXT_ARRAY),
        Property(name="truth_level", data_type=DataType.TEXT),
        Property(name="verification_status", data_type=DataType.TEXT),
        Property(name="doc_weight", data_type=DataType.NUMBER),
        Property(name="evidence_grade", data_type=DataType.TEXT),
        Property(name="is_canonical", data_type=DataType.BOOL),
        Property(name="canonical_weight", data_type=DataType.NUMBER),
        Property(name="chunk_index", data_type=DataType.INT),
        Property(name="created_at", data_type=DataType.TEXT),
        Property(name="updated_at", data_type=DataType.TEXT),
        Property(name="content_hash", data_type=DataType.TEXT),
        Property(name="source_type", data_type=DataType.TEXT),
        Property(name="doc_family", data_type=DataType.TEXT),
        Property(name="namespace", data_type=DataType.TEXT),
        Property(name="category", data_type=DataType.TEXT),
        Property(name="language", data_type=DataType.TEXT),
        Property(name="confidence_score", data_type=DataType.NUMBER),
        Property(name="last_verified_date", data_type=DataType.TEXT),
        Property(name="verified_by", data_type=DataType.TEXT),
    ]


def ensure_collection(client, collection_name: str):
    from weaviate.classes.config import Configure
    if client.collections.exists(collection_name):
        return
    client.collections.create(
        name=collection_name,
        properties=build_gold_properties(),
        vectorizer_config=Configure.Vectorizer.none(),
    )
    logger.info(f"Created missing collection: {collection_name}")


def clear_collection(weaviate_url: str, collection_name: str):
    logger.info(f"Clearing collection {collection_name}...")
    from weaviate.classes.config import Configure

    client = get_weaviate_client(weaviate_url)
    if client.collections.exists(collection_name):
        client.collections.delete(collection_name)
        logger.info(f"Deleted collection {collection_name}")

    client.collections.create(
        name=collection_name,
        properties=build_gold_properties(),
        vectorizer_config=Configure.Vectorizer.none(),
    )

    logger.info(f"Recreated collection {collection_name}")
    client.close()


def append_quarantine(quarantine_log: str, payload: Dict[str, Any]) -> None:
    try:
        qpath = Path(quarantine_log)
        qpath.parent.mkdir(parents=True, exist_ok=True)
        with qpath.open("a", encoding="utf-8") as f:
            f.write(json_dump_line(payload))
    except Exception as exc:  # noqa: BLE001
        logger.error(f"Failed to write quarantine log: {exc}")


def json_dump_line(payload: Dict[str, Any]) -> str:
    import json
    return json.dumps(payload, ensure_ascii=True) + "\n"


def validate_doc(doc: Dict[str, Any], strict_routing: bool) -> List[str]:
    errors: List[str] = []
    if not str(doc.get("title", "")).strip():
        errors.append("missing title")
    if not str(doc.get("content", "")).strip():
        errors.append("missing content")
    if not str(doc.get("source_path", "")).strip():
        errors.append("missing source_path")
    if not str(doc.get("source_uri_base", "")).strip():
        errors.append("missing source_uri")

    intent = str(doc.get("intent", "")).strip().lower()
    if intent not in ALLOWED_INTENTS:
        errors.append(f"invalid intent={intent}")

    domain_raw = doc.get("domain", "")
    domain = str(domain_raw.get("role", "")).strip().lower() if isinstance(domain_raw, dict) else str(domain_raw).strip().lower()
    if domain not in ALLOWED_DOMAINS:
        errors.append(f"invalid domain={domain}")

    tl = str(doc.get("truth_level", "")).strip().upper()
    if tl not in ALLOWED_TRUTH_LEVELS:
        errors.append(f"invalid truth_level={tl}")

    vs = str(doc.get("verification_status", "")).strip().lower()
    if vs not in ALLOWED_VERIFICATION_STATUS:
        errors.append(f"invalid verification_status={vs}")

    source_type = str(doc.get("source_type", "")).strip().lower()
    if source_type == "gamme":
        contract = doc.get("gamme_page_contract")
        if not isinstance(contract, dict):
            errors.append("missing gamme_page_contract")
        else:
            quality = contract.get("quality") if isinstance(contract.get("quality"), dict) else {}
            if quality.get("version") != "GammeContentContract.v1":
                errors.append(
                    f"invalid gamme_page_contract.quality.version={quality.get('version')}"
                )
            score = quality.get("score")
            if not isinstance(score, int):
                errors.append("invalid gamme_page_contract.quality.score")
            elif score < 40:
                errors.append(f"low gamme_page_contract.quality.score={score}")

            flags = quality.get("flags")
            if flags is not None and not isinstance(flags, list):
                errors.append("invalid gamme_page_contract.quality.flags")

        contract_errors = doc.get("gamme_contract_errors")
        if isinstance(contract_errors, list):
            for contract_error in contract_errors:
                ce = str(contract_error).strip()
                if ce:
                    errors.append(f"gamme_contract: {ce}")

    if strict_routing:
        fam = str(doc.get("doc_family", "")).strip().lower()
        if fam not in COLLECTION_BY_FAMILY:
            errors.append(f"invalid doc_family={fam}")

    return errors


def validate_chunk(chunk: Dict[str, Any]) -> List[str]:
    required = [
        "chunk_id", "parent_id", "source_path", "source_uri", "title", "content",
        "intent", "domain", "truth_level", "verification_status", "doc_weight",
        "chunk_index", "updated_at", "content_hash", "doc_family",
    ]
    errors: List[str] = []
    for field in required:
        value = chunk.get(field)
        if value is None or (isinstance(value, str) and not value.strip()):
            errors.append(f"missing {field}")
    if str(chunk.get("intent", "")).strip().lower() not in ALLOWED_INTENTS:
        errors.append(f"invalid intent={chunk.get('intent')}")
    chunk_domain_raw = chunk.get("domain", "")
    chunk_domain = str(chunk_domain_raw.get("role", "")).strip().lower() if isinstance(chunk_domain_raw, dict) else str(chunk_domain_raw).strip().lower()
    if chunk_domain not in ALLOWED_DOMAINS:
        errors.append(f"invalid domain={chunk_domain}")
    if str(chunk.get("truth_level", "")).strip().upper() not in ALLOWED_TRUTH_LEVELS:
        errors.append(f"invalid truth_level={chunk.get('truth_level')}")
    if str(chunk.get("verification_status", "")).strip().lower() not in ALLOWED_VERIFICATION_STATUS:
        errors.append(f"invalid verification_status={chunk.get('verification_status')}")
    fam = str(chunk.get("doc_family", "")).strip().lower()
    if fam not in COLLECTION_BY_FAMILY:
        errors.append(f"invalid doc_family={fam}")
    return errors


def apply_cpu_strict_mode():
    os.environ["OMP_NUM_THREADS"] = os.environ.get("OMP_NUM_THREADS", "1")
    os.environ["OPENBLAS_NUM_THREADS"] = os.environ.get("OPENBLAS_NUM_THREADS", "1")
    os.environ["MKL_NUM_THREADS"] = os.environ.get("MKL_NUM_THREADS", "1")
    os.environ["NUMEXPR_NUM_THREADS"] = os.environ.get("NUMEXPR_NUM_THREADS", "1")
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    logger.info("CPU strict mode enabled: single-thread numerical/tokenizer execution")


def index_streaming_true(
    knowledge_path: str,
    weaviate_url: str,
    collection_name: str,
    batch_size: int,
    max_files: int = 0,
    strict_routing: bool = False,
    quarantine_log: str = "/tmp/rag_quarantine.jsonl",
    prefer_insert_first: bool = True,
) -> tuple:
    from fastembed import TextEmbedding

    logger.info(f"Loading FastEmbed model: {FASTEMBED_MODEL}")
    model = TextEmbedding(model_name=FASTEMBED_MODEL)
    logger.info("FastEmbed model loaded")

    logger.info("Connecting to Weaviate...")
    client = get_weaviate_client(weaviate_url)
    collections_cache: Dict[str, Any] = {}
    if strict_routing:
        for cname in COLLECTION_BY_FAMILY.values():
            ensure_collection(client, cname)
            collections_cache[cname] = client.collections.get(cname)
    else:
        if collection_name == "AUTO":
            collection_name = DEFAULT_COLLECTION
        ensure_collection(client, collection_name)
        collections_cache[collection_name] = client.collections.get(collection_name)

    doc_count = 0
    chunk_count = 0
    indexed_count = 0
    blocked_docs = 0
    blocked_chunks = 0

    prefer_insert_first = bool(prefer_insert_first)

    def _is_missing_object_error(exc: Exception) -> bool:
        msg = str(exc).lower()
        return "no object with id" in msg or "status code: 404" in msg

    def _is_already_exists_error(exc: Exception) -> bool:
        msg = str(exc).lower()
        return (
            "already exists" in msg
            or "already in use" in msg
            or "status code: 422" in msg
            or "unprocessable" in msg
        )

    def upsert(collection, chunk: dict, embedding) -> None:
        nonlocal prefer_insert_first
        props = {k: v for k, v in chunk.items() if k != "uuid"}
        vec = embedding.tolist()

        # Adaptive strategy:
        # - Fresh/clear runs: insert-first is fastest (no PUT miss -> 500).
        # - Incremental runs: fallback to replace-first once duplicates are detected.
        if prefer_insert_first:
            try:
                collection.data.insert(
                    properties=props,
                    vector=vec,
                    uuid=chunk["uuid"],
                )
                return
            except Exception as exc:  # noqa: BLE001
                if not _is_already_exists_error(exc):
                    raise
                prefer_insert_first = False
                collection.data.replace(
                    uuid=chunk["uuid"],
                    properties=props,
                    vector=vec,
                )
                return

        try:
            collection.data.replace(
                uuid=chunk["uuid"],
                properties=props,
                vector=vec,
            )
        except Exception as exc:  # noqa: BLE001
            if not _is_missing_object_error(exc):
                raise
            prefer_insert_first = True
            collection.data.insert(
                properties=props,
                vector=vec,
                uuid=chunk["uuid"],
            )

    for doc in iter_documents(knowledge_path, max_files=max_files):
        doc_count += 1
        doc_errors = validate_doc(doc, strict_routing=strict_routing)
        if doc_errors:
            blocked_docs += 1
            append_quarantine(quarantine_log, {
                "type": "doc",
                "source_path": doc.get("source_path"),
                "errors": doc_errors,
                "ts": datetime.now(timezone.utc).isoformat(),
            })
            continue

        target_name = route_collection_for_family(str(doc.get("doc_family", ""))) if strict_routing else collection_name
        if target_name not in collections_cache:
            ensure_collection(client, target_name)
            collections_cache[target_name] = client.collections.get(target_name)
        target_collection = collections_cache[target_name]

        chunks = chunk_document(doc)
        chunk_count += len(chunks)
        if not chunks:
            continue

        for i in range(0, len(chunks), batch_size):
            batch_chunks = chunks[i:i + batch_size]
            texts = [build_embedding_input(c) for c in batch_chunks]
            embeddings = list(model.embed(texts, batch_size=batch_size))

            # Dynamic batch mode can stall indefinitely in low-memory (batch_size=1)
            # with some Weaviate versions; use direct inserts in that mode.
            if batch_size <= 1:
                for chunk, embedding in zip(batch_chunks, embeddings):
                    chunk_errors = validate_chunk(chunk)
                    if chunk_errors:
                        blocked_chunks += 1
                        append_quarantine(quarantine_log, {
                            "type": "chunk",
                            "source_path": chunk.get("source_path"),
                            "chunk_id": chunk.get("chunk_id"),
                            "errors": chunk_errors,
                            "ts": datetime.now(timezone.utc).isoformat(),
                        })
                        continue
                    upsert(target_collection, chunk, embedding)
                    indexed_count += 1
            else:
                with target_collection.batch.dynamic() as batch_obj:
                    for chunk, embedding in zip(batch_chunks, embeddings):
                        chunk_errors = validate_chunk(chunk)
                        if chunk_errors:
                            blocked_chunks += 1
                            append_quarantine(quarantine_log, {
                                "type": "chunk",
                                "source_path": chunk.get("source_path"),
                                "chunk_id": chunk.get("chunk_id"),
                                "errors": chunk_errors,
                                "ts": datetime.now(timezone.utc).isoformat(),
                            })
                            continue
                        batch_obj.add_object(
                            properties={k: v for k, v in chunk.items() if k != "uuid"},
                            vector=embedding.tolist(),
                            uuid=chunk["uuid"],
                        )
                        indexed_count += 1
            del embeddings

        del doc, chunks
        gc.collect()

        if doc_count % 25 == 0:
            logger.info(
                f"Progress: {doc_count} docs, {chunk_count} chunks, {indexed_count} indexed, "
                f"{blocked_docs} blocked docs, {blocked_chunks} blocked chunks"
            )

    client.close()
    return doc_count, chunk_count, indexed_count, blocked_docs, blocked_chunks


def dry_run(knowledge_path: str, max_files: int = 0) -> tuple:
    doc_count = 0
    chunk_count = 0
    sample_docs = []

    for doc in iter_documents(knowledge_path, max_files=max_files):
        doc_count += 1
        chunks = chunk_document(doc)
        chunk_count += len(chunks)

        if doc_count <= 10:
            sample_docs.append(doc["source_path"])

        del doc, chunks
        gc.collect()

    return doc_count, chunk_count, sample_docs


def main():
    parser = argparse.ArgumentParser(description="Reindex RAG documents to Weaviate (FastEmbed)")
    parser.add_argument("--path", default=DEFAULT_KNOWLEDGE_PATH)
    parser.add_argument("--weaviate-url", default=os.environ.get("WEAVIATE_URL", DEFAULT_WEAVIATE_URL))
    parser.add_argument("--collection", default=os.environ.get("COLLECTION_NAME", DEFAULT_COLLECTION))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--clear", action="store_true")
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    parser.add_argument("--max-files", type=int, default=0)
    parser.add_argument("--cpu-strict", action="store_true")
    parser.add_argument("--strict-routing", action="store_true", default=os.environ.get("STRICT_ROUTING", "0") == "1")
    parser.add_argument("--quarantine-log", default=os.environ.get("REINDEX_QUARANTINE_LOG", "/tmp/rag_quarantine.jsonl"))
    args = parser.parse_args()

    enforce_build_plane()
    if args.cpu_strict:
        apply_cpu_strict_mode()

    start_time = datetime.utcnow()

    logger.info("=" * 60)
    logger.info("RAG REINDEX SCRIPT (ULTRA INGESTION)")
    logger.info("=" * 60)
    logger.info(f"Knowledge path: {args.path}")
    logger.info(f"Collection: {args.collection}")
    logger.info(f"Batch size: {args.batch_size}")
    logger.info(f"Max files: {args.max_files if args.max_files > 0 else 'unlimited'}")
    logger.info(f"Dry run: {args.dry_run}")
    logger.info(f"Clear: {args.clear}")
    logger.info(f"Strict routing: {args.strict_routing}")
    logger.info(f"Quarantine log: {args.quarantine_log}")
    logger.info("=" * 60)

    if args.dry_run:
        doc_count, chunk_count, sample_docs = dry_run(args.path, max_files=args.max_files)
        logger.info("[DRY RUN] Would index:")
        for doc_path in sample_docs:
            logger.info(f"  - {doc_path}")
        if doc_count > 10:
            logger.info(f"  ... and {doc_count - 10} more")
        logger.info(f"Total: {doc_count} documents, {chunk_count} chunks")
        return

    if args.clear:
        if args.strict_routing:
            for cname in COLLECTION_BY_FAMILY.values():
                clear_collection(args.weaviate_url, cname)
        else:
            clear_collection(args.weaviate_url, args.collection)

    doc_count, chunk_count, indexed_count, blocked_docs, blocked_chunks = index_streaming_true(
        args.path,
        args.weaviate_url,
        args.collection,
        args.batch_size,
        args.max_files,
        strict_routing=args.strict_routing,
        quarantine_log=args.quarantine_log,
        prefer_insert_first=args.clear,
    )

    duration = (datetime.utcnow() - start_time).total_seconds()
    logger.info("=" * 60)
    logger.info("REINDEX COMPLETE")
    logger.info(f"Documents: {doc_count}")
    logger.info(f"Chunks: {chunk_count}")
    logger.info(f"Indexed: {indexed_count}")
    logger.info(f"Blocked docs: {blocked_docs}")
    logger.info(f"Blocked chunks: {blocked_chunks}")
    logger.info(f"Duration: {duration:.2f}s")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
