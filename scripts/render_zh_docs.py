#!/usr/bin/env python3
"""Render PAPERS.md + PAPERS_DETAIL.md from papers_detailed.jsonl (layout only)."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Standalone terms only — do not split OpenVLA / τ₀-VLA / UAV-VLN.
_BOUND = r"(?<![A-Za-z0-9_\-`])"
_END = r"(?![A-Za-z0-9_`])"
_TERM_PATTERNS = [
    (re.compile(rf"{_BOUND}World Models{_END}"), "`World Models`"),
    (re.compile(rf"{_BOUND}World Model{_END}"), "`World Model`"),
    (re.compile(rf"{_BOUND}world models{_END}"), "`world models`"),
    (re.compile(rf"{_BOUND}world model{_END}"), "`world model`"),
    (re.compile(rf"{_BOUND}VLN-CE{_END}"), "`VLN-CE`"),
    (re.compile(rf"{_BOUND}V-JEPA{_END}"), "`V-JEPA`"),
    (re.compile(rf"{_BOUND}VLA{_END}"), "`VLA`"),
    (re.compile(rf"{_BOUND}VLN{_END}"), "`VLN`"),
    (re.compile(rf"{_BOUND}VLM{_END}"), "`VLM`"),
    (re.compile(rf"{_BOUND}WM{_END}"), "`WM`"),
]


def display_title(title: str) -> str:
    """Avoid $math$ in GitHub headings; keep Unicode subscripts."""
    t = title.replace("$τ_0$", "τ₀").replace("$π_0$", "π₀")
    t = t.replace("$\\tau_0$", "τ₀").replace("$\\pi_0$", "π₀")
    return t


def backtick_terms(text: str) -> str:
    out = text
    for pat, repl in _TERM_PATTERNS:
        out = pat.sub(repl, out)
    return out


def cjk_en_space(text: str) -> str:
    """Insert a space between CJK and Latin / code spans; keep ：；、。！？."""
    s = backtick_terms(text)
    s = re.sub(r"([\u4e00-\u9fff])(`)", r"\1 \2", s)
    s = re.sub(r"(`)([\u4e00-\u9fff])", r"\1 \2", s)
    s = re.sub(r"([\u4e00-\u9fff])([A-Za-z])", r"\1 \2", s)
    s = re.sub(r"([A-Za-z0-9])([\u4e00-\u9fff])", r"\1 \2", s)
    s = re.sub(r" {2,}", " ", s)
    return s


def split_highlight(item: str) -> tuple[str, str]:
    if "：" in item:
        label, body = item.split("：", 1)
    elif ":" in item:
        label, body = item.split(":", 1)
    else:
        return "要点", item.strip()
    label = label.strip()
    if label.startswith("与"):
        label = "关系"
    elif label == "方法":
        label = "方法"
    elif label == "贡献":
        label = "贡献"
    return label, body.strip()


def load_rows() -> list[dict]:
    path = ROOT / "papers_detailed.jsonl"
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def render_papers_md(rows: list[dict]) -> str:
    by_year: dict[int, list[dict]] = defaultdict(list)
    for r in rows:
        by_year[int(r["year"])].append(r)

    years = sorted(by_year, reverse=True)
    lines: list[str] = []
    lines += [
        "# 论文索引",
        "",
        "已核验、去重后的 **131** 篇速查页。",
        "",
        "摘要与要点见 [`PAPERS_DETAIL.md`](PAPERS_DETAIL.md)。",
        "英文原文见 [`papers_detailed.jsonl`](papers_detailed.jsonl)。",
        "",
        "主键为 arXiv ID（去掉版本后缀 `vN`），否则用规范化标题。",
        "本页按年份列出标题，不把 131 行摘要塞进宽表。",
        "",
        "## 本页目录",
        "",
        "- [年份一览](#年份一览)",
        "- [按年份浏览](#按年份浏览)",
        "- [标签](#标签)",
        "",
        "## 年份一览",
        "",
        "| 年份 | 篇数 | 跳转 |",
        "| ---: | ---: | --- |",
    ]
    for y in years:
        lines.append(f"| {y} | {len(by_year[y])} | [↓ {y} 年](#{y}-年) |")
    lines += [
        "",
        "## 按年份浏览",
        "",
    ]
    for y in years:
        chunk = by_year[y]
        lines += [
            f"### {y} 年",
            "",
            f"共 {len(chunk)} 篇。",
            "",
        ]
        for r in chunk:
            title = display_title(r["title"])
            tags = " · ".join(f"`{t}`" for t in r["tags"])
            lines.append(
                f"{r['n']}. [{title}](PAPERS_DETAIL.md#p-{r['n']})  "
                f"{tags} · [`{r['arxiv_id']}`]({r['url']})"
            )
        lines.append("")

    lines += [
        "## 标签",
        "",
        "| 标签 | 含义 | 篇数 |",
        "| --- | --- | ---: |",
        "| `world_model` | 世界模型主线 | 58 |",
        "| `VLM` | 视觉—语言模型 / 具身多模态 | 23 |",
        "| `VLA` | 视觉—语言—动作策略 | 20 |",
        "| `intersection` | 跨家族 / 桥接 | 19 |",
        "| `VLN` | 视觉—语言导航 | 18 |",
        "",
        "一篇可带多个标签。细分标签（如 `video_prediction_wm`）仅扩表时出现；本包未扩表。",
        "",
    ]
    return "\n".join(lines)


def render_detail_md(rows: list[dict]) -> str:
    by_year: dict[int, list[dict]] = defaultdict(list)
    for r in rows:
        by_year[int(r["year"])].append(r)
    years = sorted(by_year, reverse=True)
    n_missing = sum(1 for r in rows if r.get("abstract_missing") or not r.get("abstract_en"))

    lines: list[str] = []
    lines += [
        "# 论文详注",
        "",
        "每篇一张卡片：年份、标签、链接、摘要、要点。",
        "",
        "中文摘要是对 arXiv **实抓英文摘要**的忠实转述，不是另写未发表论文。",
        "",
        f"本版 **{len(rows)} / {len(rows)}** 取得英文原文"
        + ("；无「摘要暂缺」。" if n_missing == 0 else f"；其中 {n_missing} 篇标「摘要暂缺」。"),
        "",
        "## 本页目录",
        "",
        "- [阅读说明](#阅读说明)",
        "- [年份一览](#年份一览)",
    ]
    for y in years:
        lines.append(f"- [{y} 年（{len(by_year[y])} 篇）](#{y}-年)")
    lines += [
        "",
        "## 阅读说明",
        "",
        "- 英文原文与机器字段：[`papers_detailed.jsonl`](papers_detailed.jsonl)。",
        "- 标题速查（按年列表）：[`PAPERS.md`](PAPERS.md)。",
        "- 摘要来源：arXiv API（[`export.arxiv.org`](http://export.arxiv.org/api/query)）",
        "  或 abs 页（`https://arxiv.org/abs/<id>`）。",
        "- 抓取失败会写 **摘要暂缺**，并保留已核验链接。",
        "- 要点只依据该摘要：方法、贡献、与 `WM` × `VLA` / `VLN` / `VLM` 的关系。",
        "  不编造摘要中未出现的实验数字。",
        "",
        "## 年份一览",
        "",
        "| 年份 | 篇数 | 编号 | 跳转 |",
        "| ---: | ---: | --- | --- |",
    ]
    for y in years:
        ns = [r["n"] for r in by_year[y]]
        span = f"{min(ns)}–{max(ns)}" if len(ns) > 1 else str(ns[0])
        lines.append(f"| {y} | {len(ns)} | {span} | [↓ {y} 年](#{y}-年) |")
    lines.append("")

    for y in years:
        chunk = by_year[y]
        lines += [
            f"## {y} 年",
            "",
            f"共 {len(chunk)} 篇。先扫目录，再下翻卡片。",
            "",
        ]
        for r in chunk:
            title = display_title(r["title"])
            tags = " · ".join(f"`{t}`" for t in r["tags"])
            lines.append(f"- [{r['n']}. {title}](#p-{r['n']})  {tags}")
        lines.append("")

        for i, r in enumerate(chunk):
            title = display_title(r["title"])
            tags = " · ".join(f"`{t}`" for t in r["tags"])
            missing = r.get("abstract_missing") or not r.get("abstract_en")
            abstract = "摘要暂缺。未能从 arXiv 取得摘要，请打开上方已核验链接。"
            if not missing:
                abstract = cjk_en_space(r["abstract_zh"].strip())

            lines += [
                f'<a id="p-{r["n"]}"></a>',
                "",
                f"### {r['n']}. {title}",
                "",
                f"- **年份：** {r['year']}",
                f"- **标签：** {tags}",
                f"- **链接：** [arXiv:{r['arxiv_id']}]({r['url']})",
                "",
                f"**摘要：** {abstract}",
                "",
                "**要点：**",
                "",
            ]
            for h in r["highlights_zh"]:
                lab, body = split_highlight(h)
                lines.append(f"- **{lab}：** {cjk_en_space(body)}")
            lines.append("")
            lines.append("---")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    rows = load_rows()
    if len(rows) != 131:
        raise SystemExit(f"expected 131 rows, got {len(rows)}")
    (ROOT / "PAPERS.md").write_text(render_papers_md(rows), encoding="utf-8")
    (ROOT / "PAPERS_DETAIL.md").write_text(render_detail_md(rows), encoding="utf-8")
    print(f"rendered {len(rows)} papers → PAPERS.md + PAPERS_DETAIL.md")


if __name__ == "__main__":
    main()
