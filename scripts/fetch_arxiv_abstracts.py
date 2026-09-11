#!/usr/bin/env python3
"""Fetch real arXiv abstracts for papers_merged.jsonl. Never invent text."""

from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

NS = {"a": "http://www.w3.org/2005/Atom"}
API = "http://export.arxiv.org/api/query"
ABS_HTML = "https://arxiv.org/abs/{id}"
USER_AGENT = "wm-vla-vln-vlm-survey/1.0 (documentation pack; +https://github.com/topsun-bot/wm-vla-vln-vlm-survey)"


def load_ids(path: Path) -> list[str]:
    ids = []
    with path.open() as f:
        for line in f:
            rec = json.loads(line)
            aid = rec.get("arxiv_id")
            if aid:
                ids.append(aid)
    return ids


def fetch_api_batch(ids: list[str]) -> dict[str, dict]:
    q = urllib.parse.urlencode(
        {"id_list": ",".join(ids), "start": 0, "max_results": len(ids)}
    )
    url = f"{API}?{q}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        raw = resp.read()
    root = ET.fromstring(raw)
    out: dict[str, dict] = {}
    for entry in root.findall("a:entry", NS):
        id_el = entry.find("a:id", NS)
        title_el = entry.find("a:title", NS)
        summary_el = entry.find("a:summary", NS)
        published_el = entry.find("a:published", NS)
        if id_el is None or summary_el is None:
            continue
        abs_url = (id_el.text or "").strip()
        # http://arxiv.org/abs/2406.09246v2
        aid = abs_url.rsplit("/", 1)[-1]
        aid_nov = aid.split("v")[0] if "v" in aid[4:] else aid
        authors = []
        for a in entry.findall("a:author", NS):
            name = a.find("a:name", NS)
            if name is not None and name.text:
                authors.append(name.text.strip())
        abstract = " ".join((summary_el.text or "").split())
        title = " ".join((title_el.text or "").split()) if title_el is not None else ""
        out[aid_nov] = {
            "arxiv_id": aid_nov,
            "arxiv_id_versioned": aid,
            "title_arxiv": title,
            "abstract": abstract,
            "authors": authors,
            "published": (published_el.text or "").strip() if published_el is not None else "",
            "source": "arxiv_api",
        }
    return out


def fetch_abs_page(arxiv_id: str) -> dict | None:
    url = ABS_HTML.format(id=arxiv_id)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except Exception:
        return None
    # arXiv abs pages include <blockquote class="abstract mathjax">
    marker = 'class="abstract'
    i = html.find(marker)
    if i < 0:
        return None
    start = html.find(">", i)
    if start < 0:
        return None
    end = html.find("</blockquote>", start)
    if end < 0:
        return None
    chunk = html[start + 1 : end]
    # strip tags
    text = []
    in_tag = False
    for ch in chunk:
        if ch == "<":
            in_tag = True
            continue
        if ch == ">":
            in_tag = False
            continue
        if not in_tag:
            text.append(ch)
    abstract = " ".join("".join(text).replace("Abstract:", "").split())
    if len(abstract) < 40:
        return None
    return {
        "arxiv_id": arxiv_id,
        "arxiv_id_versioned": arxiv_id,
        "title_arxiv": "",
        "abstract": abstract,
        "authors": [],
        "published": "",
        "source": "arxiv_abs_html",
    }


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    papers = root / "papers_merged.jsonl"
    ids = load_ids(papers)
    print(f"loaded {len(ids)} ids", flush=True)

    fetched: dict[str, dict] = {}
    batch_size = 20
    for i in range(0, len(ids), batch_size):
        batch = ids[i : i + batch_size]
        print(f"API batch {i // batch_size + 1}: {batch[0]}..{batch[-1]}", flush=True)
        try:
            part = fetch_api_batch(batch)
            fetched.update(part)
            print(f"  got {len(part)}/{len(batch)}", flush=True)
        except Exception as e:
            print(f"  API failed: {e}", flush=True)
        time.sleep(3.2)

    missing = [x for x in ids if x not in fetched or not fetched[x].get("abstract")]
    print(f"missing after API: {len(missing)}", flush=True)
    for aid in missing:
        print(f"abs-page fallback {aid}", flush=True)
        rec = fetch_abs_page(aid)
        if rec:
            fetched[aid] = rec
            print(f"  ok ({len(rec['abstract'])} chars)", flush=True)
        else:
            print("  FAIL", flush=True)
        time.sleep(1.2)

    out_path = root / "papers_abstracts.json"
    payload = {
        "fetched_utc_note": "real arXiv text only; empty abstract means fetch failed",
        "n_requested": len(ids),
        "n_with_abstract": sum(1 for i in ids if fetched.get(i, {}).get("abstract")),
        "records": {i: fetched.get(i, {"arxiv_id": i, "abstract": "", "source": "missing"}) for i in ids},
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {out_path} n_with_abstract={payload['n_with_abstract']}/{len(ids)}")


if __name__ == "__main__":
    main()
