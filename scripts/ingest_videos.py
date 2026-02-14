#!/usr/bin/env python3
"""Ingest local videos or video URLs into knowledge corpus.

Pipeline:
- raw immutable archive under knowledge/_raw/videos
- ASR transcript with timestamps (whisper CLI when available, fallback to subtitles for URLs)
- keyframe extraction (ffmpeg) + OCR on frames (tesseract)
- normalized markdown docs with [[VIDEO_TS:HH:MM:SS-HH:MM:SS]] markers
- optional technical passage promotion into canonical docs
"""

import argparse
import hashlib
import json
import logging
import math
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from PIL import Image

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.config import get_settings  # noqa: E402
from app.services.knowledge_service import get_knowledge_service  # noqa: E402


logger = logging.getLogger(__name__)
VIDEO_EXTS = {".mp4", ".mov", ".mkv", ".webm", ".m4v", ".avi"}
TECHNICAL_TERMS = {
    "diagnostic",
    "procedure",
    "etape",
    "couple",
    "torque",
    "frein",
    "brake",
    "sensor",
    "capteur",
    "maintenance",
    "calibration",
    "ecu",
    "abs",
    "ebs",
    "norme",
    "reglage",
}


def setup_logging(verbose: bool = False) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def command_exists(name: str) -> bool:
    return shutil.which(name) is not None


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha1_text(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()


def sanitize_title(value: str) -> str:
    clean = "".join(ch if ch.isalnum() or ch in {" ", "-", "_"} else " " for ch in value)
    clean = " ".join(clean.replace("_", " ").replace("-", " ").split())
    return clean.strip() or "untitled video"


def parse_hms_to_seconds(value: str) -> float:
    txt = (value or "").strip().replace(",", ".")
    if not txt:
        return 0.0
    parts = txt.split(":")
    try:
        if len(parts) == 3:
            return float(parts[0]) * 3600 + float(parts[1]) * 60 + float(parts[2])
        if len(parts) == 2:
            return float(parts[0]) * 60 + float(parts[1])
        return float(parts[0])
    except Exception:
        return 0.0


def format_hms(seconds: float) -> str:
    sec = max(0, int(seconds))
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def archive_raw_video(
    video_path: Path,
    source_label: str,
    knowledge_root: Path,
    source_url: str = "",
) -> tuple[Path, str]:
    digest = sha256_file(video_path)
    raw_dir = knowledge_root / "_raw" / "videos"
    raw_dir.mkdir(parents=True, exist_ok=True)

    ext = video_path.suffix.lower() or ".bin"
    raw_video = raw_dir / f"{digest}{ext}"
    if not raw_video.exists():
        shutil.copy2(video_path, raw_video)

    sidecar = raw_dir / f"{digest}.json"
    if not sidecar.exists():
        metadata = {
            "sha256": digest,
            "source_label": source_label,
            "source_url": source_url,
            "ingested_at": datetime.now(timezone.utc).isoformat(),
            "size_bytes": video_path.stat().st_size,
        }
        sidecar.write_text(json.dumps(metadata, ensure_ascii=True, indent=2), encoding="utf-8")
    return raw_video, digest


def run_cmd(cmd: list[str], timeout: int = 300) -> tuple[int, str, str]:
    try:
        proc = subprocess.run(
            cmd,
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return proc.returncode, proc.stdout or "", proc.stderr or ""
    except Exception as exc:  # noqa: BLE001
        return 1, "", str(exc)


def list_local_videos(input_path: Path) -> list[Path]:
    if input_path.is_file() and input_path.suffix.lower() in VIDEO_EXTS:
        return [input_path]
    if input_path.is_dir():
        return sorted(
            p for p in input_path.rglob("*")
            if p.is_file() and p.suffix.lower() in VIDEO_EXTS
        )
    return []


def parse_vtt_file(path: Path) -> list[dict[str, Any]]:
    segments: list[dict[str, Any]] = []
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if "-->" not in line:
            i += 1
            continue
        start_raw, end_raw = [x.strip() for x in line.split("-->", 1)]
        start = parse_hms_to_seconds(start_raw.split(" ")[0])
        end = parse_hms_to_seconds(end_raw.split(" ")[0])
        i += 1
        text_lines = []
        while i < len(lines) and lines[i].strip():
            txt = lines[i].strip()
            if txt.startswith(("WEBVTT", "NOTE")):
                break
            text_lines.append(txt)
            i += 1
        text = " ".join(text_lines).strip()
        if text and end > start:
            segments.append({"start": start, "end": end, "text": text})
        i += 1
    return segments


def extract_subtitle_segments(url: str, tmp_dir: Path) -> list[dict[str, Any]]:
    if not command_exists("yt-dlp"):
        return []

    out_tpl = str(tmp_dir / "video.%(ext)s")
    cmd = [
        "yt-dlp",
        "--skip-download",
        "--no-playlist",
        "--write-auto-sub",
        "--write-sub",
        "--sub-langs",
        "fr,en,fr-FR,en-US",
        "--sub-format",
        "vtt",
        "-o",
        out_tpl,
        url,
    ]
    code, _, err = run_cmd(cmd, timeout=240)
    if code != 0:
        logger.warning(f"Subtitle extraction failed for URL {url}: {err.strip()[:200]}")
        return []

    vtts = sorted(tmp_dir.glob("*.vtt"))
    for vtt in vtts:
        segs = parse_vtt_file(vtt)
        if segs:
            return segs
    return []


def download_video_url(url: str, tmp_dir: Path) -> tuple[Path | None, str]:
    """Download URL when possible; return (video_path, source_uri)."""
    url_hash = sha1_text(url)[:12]
    source_uri = f"video://url/{url_hash}"
    if not command_exists("yt-dlp"):
        return None, source_uri

    out_tpl = str(tmp_dir / "video.%(ext)s")
    cmd = [
        "yt-dlp",
        "--no-playlist",
        "-f",
        "mp4/best[ext=mp4]/best",
        "-o",
        out_tpl,
        url,
    ]
    code, _, err = run_cmd(cmd, timeout=900)
    if code != 0:
        logger.warning(f"Video download failed for URL {url}: {err.strip()[:200]}")
        return None, source_uri

    candidates = sorted(tmp_dir.glob("video.*"))
    for cand in candidates:
        if cand.suffix.lower() in VIDEO_EXTS:
            return cand, source_uri
    return None, source_uri


def whisper_segments(video_path: Path, tmp_dir: Path, language: str) -> list[dict[str, Any]]:
    if not command_exists("whisper"):
        return []

    cmd = [
        "whisper",
        str(video_path),
        "--task",
        "transcribe",
        "--language",
        language,
        "--output_format",
        "json",
        "--output_dir",
        str(tmp_dir),
        "--fp16",
        "False",
    ]
    code, _, err = run_cmd(cmd, timeout=7200)
    if code != 0:
        logger.warning(f"Whisper ASR failed for {video_path.name}: {err.strip()[:240]}")
        return []

    json_path = tmp_dir / f"{video_path.stem}.json"
    if not json_path.exists():
        return []
    try:
        payload = json.loads(json_path.read_text(encoding="utf-8"))
    except Exception:
        return []

    segs = []
    for s in payload.get("segments", []) or []:
        start = float(s.get("start", 0.0) or 0.0)
        end = float(s.get("end", 0.0) or 0.0)
        text = str(s.get("text", "")).strip()
        if end > start and text:
            segs.append({"start": start, "end": end, "text": text})
    return segs


def normalize_segments(
    segments: list[dict[str, Any]],
    min_sec: int,
    max_sec: int,
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for seg in segments:
        start = float(seg.get("start", 0.0) or 0.0)
        end = float(seg.get("end", 0.0) or 0.0)
        text = str(seg.get("text", "")).strip()
        if not text or end <= start:
            continue
        duration = end - start
        if duration <= max_sec:
            out.append({"start": start, "end": end, "text": text})
            continue

        splits = int(math.ceil(duration / max_sec))
        words = text.split()
        chunk_size = max(1, len(words) // splits)
        for i in range(splits):
            s = start + (duration * i / splits)
            e = start + (duration * (i + 1) / splits)
            chunk_words = words[i * chunk_size:] if i == splits - 1 else words[i * chunk_size:(i + 1) * chunk_size]
            chunk_text = " ".join(chunk_words).strip()
            if chunk_text:
                out.append({"start": s, "end": e, "text": chunk_text})

    # merge very short adjacent segments when possible
    merged: list[dict[str, Any]] = []
    for seg in out:
        if not merged:
            merged.append(seg)
            continue
        prev = merged[-1]
        prev_dur = prev["end"] - prev["start"]
        cur_dur = seg["end"] - seg["start"]
        if prev_dur < min_sec and (prev["end"] - prev["start"] + cur_dur) <= max_sec:
            prev["end"] = seg["end"]
            prev["text"] = (prev["text"] + " " + seg["text"]).strip()
        else:
            merged.append(seg)
    return merged


def extract_ocr_blocks(image_path: Path) -> list[dict[str, Any]]:
    if not command_exists("tesseract"):
        return []
    code, out, _ = run_cmd(
        ["tesseract", str(image_path), "stdout", "-l", "fra+eng", "tsv"],
        timeout=120,
    )
    if code != 0 or not out.strip():
        return []

    blocks: dict[int, list[tuple[int, int, int, int, str]]] = {}
    for row in out.splitlines()[1:]:
        cols = row.split("\t")
        if len(cols) < 12:
            continue
        try:
            level = int(float(cols[0]))
            block_num = int(float(cols[2]))
            left = int(float(cols[6]))
            top = int(float(cols[7]))
            width = int(float(cols[8]))
            height = int(float(cols[9]))
            conf = int(float(cols[10]))
        except Exception:
            continue
        text = (cols[11] or "").strip()
        if level != 5 or conf < 0 or not text:
            continue
        blocks.setdefault(block_num, []).append((left, top, left + width, top + height, text))

    out_blocks = []
    for _, words in sorted(blocks.items(), key=lambda kv: kv[0]):
        text = " ".join(w[4] for w in words).strip()
        if not text:
            continue
        x1 = min(w[0] for w in words)
        y1 = min(w[1] for w in words)
        x2 = max(w[2] for w in words)
        y2 = max(w[3] for w in words)
        out_blocks.append({"text": text, "bbox": [x1, y1, x2, y2]})
    return out_blocks


def extract_keyframes(video_path: Path, tmp_dir: Path, interval_sec: int) -> list[dict[str, Any]]:
    if not command_exists("ffmpeg"):
        return []
    frames_dir = tmp_dir / "frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    pattern = str(frames_dir / "frame_%06d.jpg")
    fps_expr = f"fps=1/{max(1, interval_sec)}"
    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "error",
        "-i",
        str(video_path),
        "-vf",
        fps_expr,
        pattern,
    ]
    code, _, err = run_cmd(cmd, timeout=1800)
    if code != 0:
        logger.warning(f"Keyframe extraction failed for {video_path.name}: {err.strip()[:200]}")
        return []

    frames = []
    for idx, frame in enumerate(sorted(frames_dir.glob("frame_*.jpg")), start=1):
        start = (idx - 1) * interval_sec
        end = start + interval_sec
        ocr_blocks = extract_ocr_blocks(frame)
        sample = ""
        if ocr_blocks:
            sample = (ocr_blocks[0].get("text", "") or "")[:300].strip()
        try:
            with Image.open(frame) as img:
                width, height = img.size
        except Exception:
            width, height = 0, 0
        frames.append(
            {
                "index": idx,
                "start": start,
                "end": end,
                "ocr_blocks": ocr_blocks,
                "ocr_sample": sample,
                "width": width,
                "height": height,
            }
        )
    return frames


def render_transcript_markdown(segments: list[dict[str, Any]], source_url: str) -> str:
    lines = ["## Transcript"]
    if source_url:
        lines.append(f"Source URL: {source_url}")
        lines.append("")
    if not segments:
        lines.append("- No ASR transcript available.")
        return "\n".join(lines).strip()

    for i, seg in enumerate(segments, start=1):
        start = format_hms(seg["start"])
        end = format_hms(seg["end"])
        lines.append(f"### Segment {i:03d} [[VIDEO_TS:{start}-{end}]]")
        lines.append(seg["text"].strip())
        lines.append("")
    return "\n".join(lines).strip()


def render_keyframes_markdown(frames: list[dict[str, Any]], source_url: str) -> str:
    lines = ["## Keyframes OCR"]
    if source_url:
        lines.append(f"Source URL: {source_url}")
        lines.append("")
    if not frames:
        lines.append("- No keyframes extracted.")
        return "\n".join(lines).strip()

    for frame in frames:
        start = format_hms(frame["start"])
        end = format_hms(frame["end"])
        lines.append(f"### Frame {frame['index']:03d} [[VIDEO_TS:{start}-{end}]]")
        lines.append(f"Resolution: {frame['width']}x{frame['height']}")
        if frame["ocr_blocks"]:
            for j, block in enumerate(frame["ocr_blocks"], start=1):
                bbox = block.get("bbox", [0, 0, 0, 0])
                lines.append(f"- OCR {j} [[BBOX:{bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]}]]: {block.get('text', '').strip()}")
        else:
            lines.append("- OCR: none")
        lines.append("")
    return "\n".join(lines).strip()


def render_canonical_markdown(segments: list[dict[str, Any]], source_url: str) -> str:
    selected = []
    for seg in segments:
        text = seg.get("text", "").strip()
        if len(text) < 40:
            continue
        low = text.lower()
        if not any(term in low for term in TECHNICAL_TERMS):
            continue
        selected.append(seg)
        if len(selected) >= 24:
            break

    if not selected:
        return ""

    lines = ["## Canonical Technical Excerpts"]
    if source_url:
        lines.append(f"Source URL: {source_url}")
        lines.append("")
    for i, seg in enumerate(selected, start=1):
        start = format_hms(seg["start"])
        end = format_hms(seg["end"])
        lines.append(f"### Excerpt {i:03d} [[VIDEO_TS:{start}-{end}]]")
        lines.append(seg["text"].strip())
        lines.append("")
    return "\n".join(lines).strip()


def collect_urls(args: argparse.Namespace) -> list[str]:
    urls = []
    for u in args.url or []:
        u = (u or "").strip()
        if u:
            urls.append(u)
    if args.urls_file:
        path = Path(args.urls_file).resolve()
        if path.exists():
            for line in path.read_text(encoding="utf-8").splitlines():
                txt = line.strip()
                if txt and not txt.startswith("#"):
                    urls.append(txt)
    dedup = []
    seen = set()
    for u in urls:
        if u not in seen:
            seen.add(u)
            dedup.append(u)
    return dedup


def run(args: argparse.Namespace) -> int:
    settings = get_settings()
    if not settings.can_write() and not args.dry_run:
        logger.error("Write operations are blocked in this environment (set ENV=dev/ci/staging).")
        return 1

    local_videos: list[Path] = []
    if args.input:
        input_path = Path(args.input).resolve()
        local_videos = list_local_videos(input_path)
        if args.input and not local_videos and not input_path.exists():
            logger.error(f"Input path not found: {input_path}")
            return 1

    url_list = collect_urls(args)
    if not local_videos and not url_list:
        logger.warning("No local videos or URLs provided.")
        return 0

    service = get_knowledge_service()
    knowledge_root = Path(service.knowledge_path)
    created = 0
    failed = 0

    logger.info(f"Found local videos={len(local_videos)}, urls={len(url_list)}")

    # Local video ingestion
    for video_path in local_videos:
        rel = video_path.name if not args.input else str(video_path.relative_to(Path(args.input).resolve()))
        source_uri = f"video://{Path(rel).as_posix()}"
        title_base = sanitize_title(video_path.stem)

        with tempfile.TemporaryDirectory(prefix="vid_ingest_") as tdir:
            tmp_dir = Path(tdir)
            try:
                if args.dry_run:
                    raw_sha = sha256_file(video_path)
                else:
                    _, raw_sha = archive_raw_video(video_path, rel, knowledge_root)

                segs = whisper_segments(video_path, tmp_dir, args.language)
                segs = normalize_segments(segs, args.segment_min_sec, args.segment_max_sec)

                frames = extract_keyframes(video_path, tmp_dir, args.frame_interval_sec)
                transcript_md = render_transcript_markdown(segs, source_url="")
                keyframes_md = render_keyframes_markdown(frames, source_url="")
                canonical_md = render_canonical_markdown(segs, source_url="")

                if args.dry_run:
                    logger.info(
                        f"[DRY-RUN] local={rel} asr_segments={len(segs)} "
                        f"keyframes={len(frames)} raw_sha256={raw_sha}"
                    )
                    continue

                doc_t = service.create_document(
                    title=f"{title_base} video transcript",
                    content=transcript_md,
                    source_type="video",
                    category="media",
                    truth_level=args.truth_level,
                    source_uri=source_uri,
                )
                if not doc_t:
                    failed += 1
                    logger.error(f"Failed transcript doc for {rel}")
                    continue
                created += 1

                doc_k = service.create_document(
                    title=f"{title_base} video keyframes",
                    content=keyframes_md,
                    source_type="video",
                    category="media",
                    truth_level=args.truth_level,
                    source_uri=source_uri,
                )
                if doc_k:
                    created += 1

                if canonical_md:
                    doc_c = service.create_document(
                        title=f"{title_base} video technical canonical",
                        content=canonical_md,
                        source_type="canonical",
                        category="knowledge",
                        truth_level=args.canonical_truth_level,
                        source_uri=source_uri,
                    )
                    if doc_c:
                        created += 1

                logger.info(
                    f"Ingested local video {rel} -> asr_segments={len(segs)} "
                    f"keyframes={len(frames)} raw_sha256={raw_sha}"
                )
            except Exception as exc:  # noqa: BLE001
                failed += 1
                logger.error(f"Failed local video {rel}: {exc}")

    # URL video ingestion
    for url in url_list:
        url_hash = sha1_text(url)[:12]
        title_base = f"video url {url_hash}"
        with tempfile.TemporaryDirectory(prefix="vid_url_ingest_") as tdir:
            tmp_dir = Path(tdir)
            try:
                video_path, source_uri = download_video_url(url, tmp_dir)
                subtitle_segs = extract_subtitle_segments(url, tmp_dir)
                asr_segs = whisper_segments(video_path, tmp_dir, args.language) if video_path else []
                segs = asr_segs or subtitle_segs
                segs = normalize_segments(segs, args.segment_min_sec, args.segment_max_sec)

                frames = extract_keyframes(video_path, tmp_dir, args.frame_interval_sec) if video_path else []
                transcript_md = render_transcript_markdown(segs, source_url=url)
                keyframes_md = render_keyframes_markdown(frames, source_url=url)
                canonical_md = render_canonical_markdown(segs, source_url=url)

                raw_sha = ""
                if video_path:
                    raw_sha = sha256_file(video_path)
                    if not args.dry_run:
                        _, raw_sha = archive_raw_video(video_path, source_uri, knowledge_root, source_url=url)

                if args.dry_run:
                    logger.info(
                        f"[DRY-RUN] url={url} downloaded={'yes' if video_path else 'no'} "
                        f"asr_segments={len(segs)} keyframes={len(frames)} raw_sha256={raw_sha or 'n/a'}"
                    )
                    continue

                doc_t = service.create_document(
                    title=f"{title_base} video transcript",
                    content=transcript_md,
                    source_type="video",
                    category="media",
                    truth_level=args.truth_level,
                    source_uri=source_uri,
                )
                if not doc_t:
                    failed += 1
                    logger.error(f"Failed transcript doc for URL {url}")
                    continue
                created += 1

                doc_k = service.create_document(
                    title=f"{title_base} video keyframes",
                    content=keyframes_md,
                    source_type="video",
                    category="media",
                    truth_level=args.truth_level,
                    source_uri=source_uri,
                )
                if doc_k:
                    created += 1

                if canonical_md:
                    doc_c = service.create_document(
                        title=f"{title_base} video technical canonical",
                        content=canonical_md,
                        source_type="canonical",
                        category="knowledge",
                        truth_level=args.canonical_truth_level,
                        source_uri=source_uri,
                    )
                    if doc_c:
                        created += 1

                logger.info(
                    f"Ingested URL video {url} -> downloaded={'yes' if video_path else 'no'} "
                    f"segments={len(segs)} keyframes={len(frames)} raw_sha256={raw_sha or 'n/a'}"
                )
            except Exception as exc:  # noqa: BLE001
                failed += 1
                logger.error(f"Failed URL video {url}: {exc}")

    logger.info(f"Done. created={created}, failed={failed}")
    return 0 if failed == 0 else 2


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest videos into RAG knowledge corpus")
    parser.add_argument("--input", help="Video file or directory")
    parser.add_argument("--url", action="append", help="Video URL (repeatable, e.g. YouTube)")
    parser.add_argument("--urls-file", help="Text file with one video URL per line")
    parser.add_argument(
        "--truth-level",
        default="L3",
        choices=["L1", "L2", "L3", "L4"],
        help="Truth level for media docs",
    )
    parser.add_argument(
        "--canonical-truth-level",
        default="L2",
        choices=["L1", "L2", "L3", "L4"],
        help="Truth level for promoted canonical docs",
    )
    parser.add_argument("--language", default="fr", help="ASR language hint for whisper")
    parser.add_argument("--frame-interval-sec", type=int, default=8, help="Keyframe sampling interval")
    parser.add_argument("--segment-min-sec", type=int, default=10, help="Minimum transcript segment duration")
    parser.add_argument("--segment-max-sec", type=int, default=30, help="Maximum transcript segment duration")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose logs")
    args = parser.parse_args()

    setup_logging(args.verbose)
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
