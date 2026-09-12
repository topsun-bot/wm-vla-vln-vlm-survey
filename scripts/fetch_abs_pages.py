#!/usr/bin/env python3
"""Fetch real abstracts from arXiv abs HTML. Never invent text."""

from __future__ import annotations

import html as htmlmod
import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

USER_AGENT = "wm-vla-vln-vlm-survey/1.0 (documentation pack; +https://github.com/topsun-bot/wm-vla-vln-vlm-survey)"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "scripts" / "_fetched_candidates.json"

IDS = [
    "2109.12098",
    "2201.07207",
    "2206.08853",
    "2207.04429",
    "2207.10716",
    "2209.07753",
    "2209.11302",
    "2210.03629",
    "2212.04088",
    "2302.01560",
    "2302.11550",
    "2303.11366",
    "2303.12153",
    "2304.10750",
    "2305.05658",
    "2305.14954",
    "2305.15021",
    "2305.16291",
    "2305.17144",
    "2306.03310",
    "2306.08647",
    "2306.13195",
    "2306.17582",
    "2307.02485",
    "2307.04738",
    "2307.05973",
    "2308.10141",
    "2309.10062",
    "2309.12306",
    "2309.17080",
    "2310.09615",
    "2310.12931",
    "2311.01455",
    "2311.01977",
    "2311.05997",
    "2311.12871",
    "2312.05244",
    "2401.12202",
    "2401.12963",
    "2403.09631",
    "2403.12945",
    "2405.12399",
    "2406.02523",
    "2407.08693",
    "2408.14837",
    "2409.01652",
    "2409.15146",
    "2410.06158",
    "2410.07864",
    "2411.09022",
    "2411.19650",
    "2412.04453",
    "2412.10345",
    "2412.14058",
    "2412.14803",
    "2501.03575",
    "2501.09747",
    "2501.10105",
    "2501.15830",
    "2502.19417",
    "2503.14734",
    "2503.20020",
    "2503.20523",
    "2504.16054",
    "2505.06111",
    "2506.17811",
    "2506.18088",
    "2506.19850",
    "2507.15597",
    "2510.10274",
    "2512.13030",
    "2512.15692",
    "2601.16163",
    "2601.21998",
    "2602.13193",
    "2602.14979",
    "2602.15922",
    "2603.01229",
    "2603.09971",
    "2603.16666",
    "2603.22435",
    "2604.15483",
    "2606.05979",
    "2606.10267",
    "2606.28182",
    "2607.21725",
    "2609.01281",
    "2609.04355",
    "2609.06251",
    "2401.14403",
    "2403.17364",
    "2404.11457",
    "2405.01483",
    "2406.11740",
    "2303.17580",
    "2603.10448",
    "2604.05014",
    # extra 2025–2026 agent / VLA / WM likely
    "2506.09985",  # already
    "2410.24164",  # already
    "2603.02115",  # Robometer
    "2510.03827",  # LIBERO-PRO
    "2506.13751",
    "2504.08634",
    "2402.19469",
    "2308.12966",
    "2401.14434",
    "2410.11758",
    "2503.03828",
    "2501.04693",
    "2608.06332",  # already
    "2609.09158",  # already
]


def load_existing() -> set[str]:
    ids = set()
    with (ROOT / "papers_merged.jsonl").open() as f:
        for line in f:
            rec = json.loads(line)
            aid = rec.get("arxiv_id") or ""
            if aid:
                ids.add(aid.split("v")[0] if "v" in aid[4:] else aid)
    return ids


def strip_tags(chunk: str) -> str:
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
    return htmlmod.unescape("".join(text))


def fetch_abs(arxiv_id: str) -> dict | None:
    url = f"https://arxiv.org/abs/{arxiv_id}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=40) as resp:
            final = resp.geturl()
            html = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return {"arxiv_id": arxiv_id, "error": f"HTTP {e.code}"}
    except Exception as e:
        return {"arxiv_id": arxiv_id, "error": str(e)}

    if "Article identifier is empty or does not match expected pattern" in html:
        return {"arxiv_id": arxiv_id, "error": "invalid_id"}
    if "not been identified" in html.lower() and "abstract" not in html.lower():
        return {"arxiv_id": arxiv_id, "error": "not_found"}

    marker = 'class="abstract'
    i = html.find(marker)
    if i < 0:
        return {"arxiv_id": arxiv_id, "error": "no_abstract_block"}
    start = html.find(">", i)
    end = html.find("</blockquote>", start)
    if start < 0 or end < 0:
        return {"arxiv_id": arxiv_id, "error": "abstract_parse"}
    abstract = " ".join(strip_tags(html[start + 1 : end]).replace("Abstract:", "").split())
    if len(abstract) < 40:
        return {"arxiv_id": arxiv_id, "error": "abstract_too_short"}

    title = ""
    tm = re.search(r'<h1 class="title[^"]*">\s*<span class="descriptor">Title:</span>\s*(.*?)</h1>', html, re.S)
    if tm:
        title = " ".join(strip_tags(tm.group(1)).split())
    if not title:
        tm = re.search(r"<title>(.*?)</title>", html, re.S)
        if tm:
            title = " ".join(strip_tags(tm.group(1)).split())
            title = re.sub(r"^\[.*?\]\s*", "", title)

    authors = []
    am = re.search(r'<div class="authors">(.*?)</div>', html, re.S)
    if am:
        names = re.findall(r"<a[^>]*>(.*?)</a>", am.group(1))
        authors = [" ".join(strip_tags(n).split()) for n in names if strip_tags(n).strip()]

    published = ""
    dm = re.search(r'<div class="dateline">(.*?)</div>', html, re.S)
    dateline = " ".join(strip_tags(dm.group(1)).split()) if dm else ""
    ym = re.search(r"(\d{1,2} \w+ \d{4})", dateline)
    if ym:
        published = ym.group(1)
    # also citation_date
    cm = re.search(r'name="citation_date" content="([^"]+)"', html)
    if cm:
        published = cm.group(1)

    comment = ""
    cmt = re.search(r'<td class="tablecell comments">(.*?)</td>', html, re.S)
    if cmt:
        comment = " ".join(strip_tags(cmt.group(1)).split())

    cats = re.findall(r'<span class="primary-subject">(.*?)</span>', html)
    cats += re.findall(r'class="subject"[^>]*>([^<]+)', html)

    year = None
    if published:
        y = re.search(r"(20\d{2})", published)
        if y:
            year = int(y.group(1))
    if year is None:
        year = 2000 + int(arxiv_id[:2])

    return {
        "arxiv_id": arxiv_id,
        "arxiv_id_versioned": arxiv_id,
        "title": title,
        "abstract": abstract,
        "authors": authors,
        "published": published,
        "year": year,
        "comment": comment,
        "categories": cats,
        "url": f"https://arxiv.org/abs/{arxiv_id}",
        "source": "arxiv_abs_html",
        "final_url": final,
    }


def main() -> None:
    existing = load_existing()
    print(f"existing {len(existing)}", flush=True)
    found = {}
    errors = []
    # resume
    if OUT.exists():
        try:
            prev = json.loads(OUT.read_text())
            for r in prev.get("new", []):
                found[r["arxiv_id"]] = r
            print(f"resumed {len(found)}", flush=True)
        except Exception:
            pass

    ids = []
    seen = set()
    for x in IDS:
        if x not in seen:
            ids.append(x)
            seen.add(x)

    for n, aid in enumerate(ids, 1):
        if aid in existing:
            print(f"[{n}/{len(ids)}] skip existing {aid}", flush=True)
            continue
        if aid in found and found[aid].get("abstract"):
            print(f"[{n}/{len(ids)}] cached {aid}", flush=True)
            continue
        print(f"[{n}/{len(ids)}] abs {aid}", flush=True)
        rec = fetch_abs(aid)
        if rec and rec.get("abstract"):
            found[aid] = rec
            print(f"  ok {rec.get('year')} {rec['title'][:90]}", flush=True)
        else:
            errors.append(rec or {"arxiv_id": aid, "error": "none"})
            print(f"  FAIL {rec}", flush=True)
        # checkpoint
        new = [found[k] for k in found if k not in existing]
        payload = {
            "existing_n": len(existing),
            "new_n": len(new),
            "errors": errors,
            "new": sorted(new, key=lambda r: (r.get("year") or 0, r.get("title") or ""), reverse=True),
        }
        OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        time.sleep(1.6)

    print(f"DONE new={len(found)} errors={len(errors)} -> {OUT}", flush=True)


if __name__ == "__main__":
    main()
