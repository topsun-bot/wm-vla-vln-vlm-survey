#!/usr/bin/env python3
"""Merge newly verified papers into jsonl sources. English abstracts are fetched, never invented."""

from __future__ import annotations

import json
from pathlib import Path

from new_papers_meta import KEEP
from pack_extra_meta import PACK_EXTRA

KEEP = {**KEEP, **PACK_EXTRA}

ROOT = Path(__file__).resolve().parents[1]


def authors_short(authors: list[str]) -> str:
    if not authors:
        return ""
    if len(authors) <= 3:
        return ", ".join(authors)
    return ", ".join(authors[:3]) + " et al."


def title_sort_key(title: str) -> str:
    return title.replace("$", "").lower()


def main() -> None:
    by_id: dict = {}
    for name in ("_fetched_candidates.json", "_pack_extra.json"):
        p = ROOT / "scripts" / name
        if not p.exists():
            continue
        blob = json.loads(p.read_text())
        for r in blob.get("new", []):
            by_id[r["arxiv_id"]] = r

    existing = []
    with (ROOT / "papers_merged.jsonl").open() as f:
        for line in f:
            if line.strip():
                existing.append(json.loads(line))
    existing_ids = {r["arxiv_id"].split("v")[0] if "v" in r["arxiv_id"][4:] else r["arxiv_id"] for r in existing}

    new_rows = []
    missing = []
    for aid, meta in KEEP.items():
        if aid in existing_ids:
            continue
        src = by_id.get(aid)
        if not src or not src.get("abstract"):
            missing.append(aid)
            continue
        year = int(src.get("year") or (2000 + int(aid[:2])))
        rec = {
            "title": src["title"],
            "year": year,
            "arxiv_id": aid,
            "url": f"https://arxiv.org/abs/{aid}",
            "venue": src.get("comment") or "",
            "authors_short": authors_short(src.get("authors") or []),
            "verified": True,
            "sources": meta["sources"],
            "tags": meta["tags"],
            "abstract_en": src["abstract"],
            "abstract_source": src.get("source") or "arxiv_abs_html",
            "abstract_zh": meta["abstract_zh"],
            "highlights_zh": meta["highlights_zh"],
        }
        new_rows.append(rec)

    if missing:
        raise SystemExit(f"missing fetched abstracts: {missing}")

    all_merged = existing + new_rows
    all_merged.sort(key=lambda r: (-int(r["year"]), title_sort_key(r["title"])))

    merged_path = ROOT / "papers_merged.jsonl"
    with merged_path.open("w") as f:
        for rec in all_merged:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    detailed_path = ROOT / "papers_detailed.jsonl"
    with detailed_path.open("w") as f:
        for i, rec in enumerate(all_merged, 1):
            d = {
                "n": i,
                "title": rec["title"],
                "year": rec["year"],
                "tags": rec["tags"],
                "arxiv_id": rec["arxiv_id"],
                "url": rec["url"],
                "authors_short": rec.get("authors_short") or None,
                "venue": rec.get("venue") or "",
                "abstract_en": rec["abstract_en"],
                "abstract_source": rec.get("abstract_source") or "arxiv_abs_html",
                "abstract_zh": rec["abstract_zh"],
                "highlights_zh": rec["highlights_zh"],
                "abstract_missing": not bool(rec.get("abstract_en")),
            }
            f.write(json.dumps(d, ensure_ascii=False) + "\n")

    from collections import Counter

    years = Counter(r["year"] for r in all_merged)
    tags = Counter(t for r in all_merged for t in r["tags"])
    print(f"wrote {len(all_merged)} papers (+{len(new_rows)})")
    print("years", dict(sorted(years.items())))
    print("tags", dict(tags))


if __name__ == "__main__":
    main()
