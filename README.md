# World Model × VLA / VLN / VLM — Survey Pack

> **Maintained under [`topsun-bot/wm-vla-vln-vlm-survey`](https://github.com/topsun-bot/wm-vla-vln-vlm-survey).**  
> Related OSS forks: see [`forks_created.md`](forks_created.md). Upstream research papers remain third-party; we only index verified links.


Drop-in documentation pack for a topsun / robotics repo: verified papers, OSS landscape, and a short composition crosswalk.

## Purpose

- Give engineers a **single verified index** of world-model and vision-language-action / navigation / model literature that actually intersects robotics and embodied AI.
- Surface **what is open-source vs closed** (GAIA / Genie / UniSim / GameNGen honesty).
- Provide a tight **composition sketch** (perception → latent dynamics → language grounding → action/nav) for ODM / robot stacks.

## Stats

| Metric | Value |
| --- | ---: |
| Unique verified papers | **131** |
| Verified OSS repos | **31** |
| Retrieval / pack build (UTC) | **2026-09-11T15:31:03Z** |
| Spot-check (sample URLs) | 10/10 HTTP 200 |

## Contents

| File | Role |
| --- | --- |
| [`PAPERS.md`](PAPERS.md) | Markdown table of **all** unique papers (columns: #, Title, Year, Tags, arXiv/DOI, URL) |
| [`papers_merged.jsonl`](papers_merged.jsonl) | Machine-readable merged records (sources + tags) |
| [`CROSSWALK.md`](CROSSWALK.md) | Definitions, composition, OSS gaps, ODM integration notes |
| [`oss_repos.md`](oss_repos.md) | Verified open-source comparison table (31 repos) |
| [`oss_repos.jsonl`](oss_repos.jsonl) | Machine-readable OSS rows |
| [`build_pack.py`](build_pack.py) | Reproducible merge / expand / verify script |
| [`verify_sample.log`](verify_sample.log) | `curl -sI` spot-check log |

### OSS table

See **[`oss_repos.md`](oss_repos.md)** for the full comparison (Dreamer family, transformer/diffusion WMs, Cosmos, JEPA, 3D-VLA, OpenVLA/Octo, VLN stacks, Minecraft adjacent). Family coverage and **honest exclusions** (GAIA official, Genie official, UniSim interactive code, GameNGen official) are documented there.

## Methodology

1. **Inputs**: `papers_world_models.jsonl` (world-model survey) + `papers_vla_vln_vlm.jsonl` (VLA/VLN/VLM survey) — each entry previously verified via arXiv API and/or abs-page fetch.
2. **Merge / dedupe**: primary key = arXiv ID with version suffix `vN` stripped; fallback = normalized title.
3. **Tags**: `world_model` from WM list; `VLA` / `VLN` / `VLM` / `intersection` from VLA list; multi-source papers keep union of tags.
4. **Expansion (only if unique < 100)**: additional HTTPS arXiv API queries for niches (video-prediction WM, occupancy WM, 3D scene WM, language-conditioned WM); **each candidate abs page verified** before insert. **Zero fabricated IDs.**
5. **Spot-check**: random sample of merged paper URLs probed with `curl -sI`; results in `verify_sample.log`.

### Expansion queries used this build

- Expansion skipped: already 131 >= 100

## Honest gaps

- Landmark **closed** systems without verified official OSS in this pack: **GAIA-1/2**, **Genie**, **UniSim** (interactive), **GameNGen**.
- Some listed community reproductions are WIP / incomplete relative to the papers.
- Paper lists prioritize robotics / embodied / video-prediction WMs and VLA/VLN/VLM; pure NLP VLMs and unrelated “world model” metaphors were rejected during source collection (`meta.json` rejected samples).
- Star counts and “last activity” in OSS table are snapshots as of survey date — re-check before depending on a repo.
- This pack is an index + crosswalk, **not** a claim of having re-run every paper’s experiments.

## Rebuild

```bash
python3 build_pack.py
```

Requires network access for optional expansion and URL spot-checks.

## License note

Survey text in this pack is for documentation use in your repo. Individual papers and OSS projects retain their own licenses — especially watch NC licenses (historical V-JEPA, MineRL).
