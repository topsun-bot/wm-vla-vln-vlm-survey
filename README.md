# World Model × VLA / VLN / VLM 调研索引

> 维护：[`topsun-bot/wm-vla-vln-vlm-survey`](https://github.com/topsun-bot/wm-vla-vln-vlm-survey)（默认分支 `main`）

面向机器人与具身智能的可核验文献包。收录 `World Model`（世界模型）与 `VLA` / `VLN` / `VLM` 交叉处的论文、开源仓库与组合关系。

论文仍属原作者；本仓库只索引已核验链接与实抓摘要，不声称复现了每篇实验。

**论文 131 · 开源 31 · 摘要 131/131 实抓**

从这里开始：[`论文详注`](PAPERS_DETAIL.md) · [`交叉对照`](CROSSWALK.zh.md) · [`开源表`](oss_repos.md) · [`组织 fork`](forks_created.md)

## 本页目录

- [目的](#目的)
- [一览](#一览)
- [怎么读](#怎么读)
- [文档地图](#文档地图)
- [开源缺口](#开源缺口)
- [方法](#方法)
- [标签](#标签)
- [许可](#许可)

## 目的

给工程师一份单一、可核对的入口，而不是再堆一张标题表。

- **文献：** 真正落到机器人 / 具身 AI 的世界模型与视觉—语言—动作、导航、多模态工作。
- **开源：** 标明能跑的仓库，并对 `GAIA` / `Genie` / `UniSim` / `GameNGen` 保持诚实。
- **组合：** 一条短草图——感知 → 潜空间动力学 → 语言接地 → 动作 / 导航——便于接到 ODM 或机器人栈。
- **详注：** 每篇有从 arXiv **实抓**的摘要（中文转述）与要点，见 [`PAPERS_DETAIL.md`](PAPERS_DETAIL.md)。

## 一览

| 指标 | 数值 |
| --- | ---: |
| 已核验论文（去重） | **131** |
| 已核验开源仓库 | **31** |
| 检索 / 合并（UTC） | 2026-09-11T15:31:03Z |
| 抽样链接 | 10/10 HTTP 200 |
| 摘要 | arXiv API 或 abs 页；失败标「摘要暂缺」 |

## 怎么读

1. 先读 [`CROSSWALK.zh.md`](CROSSWALK.zh.md) 的定义与「感知 → 动力学 → 语言 → 动作」草图。
2. 用 [`PAPERS.md`](PAPERS.md) 按年份扫标题；需要摘要时打开 [`PAPERS_DETAIL.md`](PAPERS_DETAIL.md) 对应编号。
3. 要落地代码时对照 [`oss_repos.md`](oss_repos.md)，并看 [`forks_created.md`](forks_created.md) 是否已有 `topsun-bot` fork。
4. 写脚本请读 jsonl，不要解析 Markdown。

## 文档地图

### 论文

| 文档 | 用途 |
| --- | --- |
| [`PAPERS.md`](PAPERS.md) | 按年列表的标题索引（编号、标签、链接） |
| [`PAPERS_DETAIL.md`](PAPERS_DETAIL.md) | 逐篇卡片：摘要 + 方法 / 贡献 / 关系 |
| [`papers_merged.jsonl`](papers_merged.jsonl) | 合并记录（来源、标签、摘要字段） |
| [`papers_detailed.jsonl`](papers_detailed.jsonl) | 详注用机器可读行（英文原文 + 中文转述） |

### 对照与开源

| 文档 | 用途 |
| --- | --- |
| [`CROSSWALK.zh.md`](CROSSWALK.zh.md) | 中文：定义、组合、缺口、ODM 笔记 |
| [`CROSSWALK.md`](CROSSWALK.md) | 英文对照（并行保留） |
| [`oss_repos.md`](oss_repos.md) | 31 个已核验仓库对照 |
| [`oss_repos.jsonl`](oss_repos.jsonl) | OSS 机器可读行 |
| [`forks_created.md`](forks_created.md) | 已 fork 到 `topsun-bot` 的上游 |

### 复现

| 文档 | 用途 |
| --- | --- |
| [`scripts/fetch_arxiv_abstracts.py`](scripts/fetch_arxiv_abstracts.py) | 从 arXiv 抓摘要（不编造） |
| [`scripts/render_zh_docs.py`](scripts/render_zh_docs.py) | 由 jsonl 重排 `PAPERS.md` / `PAPERS_DETAIL.md` |

开源对照覆盖 Dreamer 家族、Transformer / 扩散世界模型、Cosmos、JEPA、3D-VLA、OpenVLA / Octo、VLN 栈与 Minecraft 周边。家族覆盖与排除项写在 [`oss_repos.md`](oss_repos.md)。

已 fork 的上游包括 OpenVLA、Octo、DreamerV3、V-JEPA 2、Cosmos-Predict、VLN-CE、Open X-Embodiment 等，见 [`forks_created.md`](forks_created.md)。

## 开源缺口

下列标志性系统在本包中**没有**核验到与论文匹配的官方可训练 / 可推理栈（权重 + 代码）：

| 系统 | 本调研中的现状 |
| --- | --- |
| **GAIA-1/2**（Wayve） | 官方代码 / 权重未开放；社区仅有架构级 WIP：`lucidrains/gaia2-pytorch` |
| **Genie**（DeepMind） | 官方未开放；开源复现近似：`flairox/jafar`、`p-doom/jasmine` |
| **UniSim** | 未找到可交互的官方世界模型代码（研究页；`google/unisim` 是无关仓库） |
| **GameNGen** | 无核验过的官方 OSS；最接近的交互视频 `WM` 开源是 Oasis / DIAMOND |

还须记住：

- 部分社区复现相对论文仍是 WIP / 不完整。
- 收录优先机器人、具身、视频预测 `WM` 与 `VLA` / `VLN` / `VLM`；纯 NLP 的 `VLM` 以及与控制无关的「世界模型」比喻已排除。
- OSS 表中的 star 与「最近活动」是调研日快照，依赖前请再查。
- 这是**索引 + 交叉对照**，不是「我们跑过每篇实验」。

细节见 [`oss_repos.md`](oss_repos.md) 的 Family coverage / Exclusions，以及 [`CROSSWALK.zh.md`](CROSSWALK.zh.md)。

## 方法

1. **输入：** 世界模型表 + `VLA` / `VLN` / `VLM` 表；条目事先经 arXiv API 和 / 或 abs 页核验。
2. **去重：** 主键为 arXiv ID（去掉 `vN`）；否则用规范化标题。
3. **标签：** `world_model` 来自 WM 表；`VLA` / `VLN` / `VLM` / `intersection` 来自 VLA 表；多源取并集。
4. **扩表：** 仅当去重后不足 100 篇才追加检索。本包已有 131 篇，**未再扩表**。禁止编造 ID。
5. **摘要：** [arXiv API](http://export.arxiv.org/api/query) 的 `id_list` 批量拉取；限流则回退 `https://arxiv.org/abs/<id>`。只收录抓到的原文；失败标「摘要暂缺」。中文是对该原文的转述。
6. **抽样：** 合并后的论文 URL 曾用 `curl -sI` 抽检。

本快照**不包含**原始 `build_pack.py` 或 `verify_sample.log`。重建摘要：

```bash
python3 scripts/fetch_arxiv_abstracts.py
python3 scripts/render_zh_docs.py
```

## 标签

一篇可带多个标签。计数见 [`PAPERS.md`](PAPERS.md)。

| 标签 | 含义 | 篇数 |
| --- | --- | ---: |
| `world_model` | 世界模型主线 | 58 |
| `VLM` | 视觉—语言模型 / 具身多模态 | 23 |
| `VLA` | 视觉—语言—动作策略 | 20 |
| `intersection` | 跨家族 / 桥接（如 `WM` 引导的 `VLA`） | 19 |
| `VLN` | 视觉—语言导航 | 18 |

## 许可

本包中的调研文字用于仓库文档。各论文与开源项目保留各自许可。

尤其注意非商业许可：历史上的 `V-JEPA` 为 CC-BY-NC；MineRL 为 CC-BY-NC-SA。`V-JEPA` 2 为 MIT，商用前仍须核对上游 `LICENSE`。
