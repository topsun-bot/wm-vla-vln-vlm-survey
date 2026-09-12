# World Model × VLA / VLN / VLM 调研索引

> 维护：[`topsun-bot/wm-vla-vln-vlm-survey`](https://github.com/topsun-bot/wm-vla-vln-vlm-survey)（默认分支 `main`）

面向机器人与具身智能的可核验文献包。收录 `World Model`（世界模型）与 `VLA` / `VLN` / `VLM` 交叉处的论文、开源仓库与组合关系；本版补上 **Agent 控制机器人**（LLM / VLM 规划、代码即策略、工具调用、多智能体编排）。

论文仍属原作者；本仓库只索引已核验链接与实抓摘要，不声称复现了每篇实验。

**论文 276 · 开源 42 · 摘要 276/276 实抓**

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

- **文献：** 真正落到机器人 / 具身 AI 的世界模型与视觉—语言—动作、导航、多模态工作，以及 **Agent 控制机器人**（规划 / 代码 / 工具 / 多机编排）。
- **开源：** 标明能跑的仓库，并对 `GAIA` / `Genie` / `UniSim` / `GameNGen` 保持诚实。
- **组合：** 一条短草图——感知 → 潜空间动力学 → 语言接地 → 动作 / 导航；Agent 层负责分解、验证与恢复，低层可以是 `VLA` 或技能原语。
- **详注：** 每篇有从 arXiv **实抓**的摘要（中文转述）与要点，见 [`PAPERS_DETAIL.md`](PAPERS_DETAIL.md)。

## 一览

| 指标 | 数值 |
| --- | ---: |
| 已核验论文（去重） | **276** |
| 相对仓库原 131 篇 | **+145**（自检索 +93，再并入研究员包去重后 +52） |
| 已核验开源仓库 | **42** |
| 检索 / 合并（UTC） | 2026-09-12T03:10:00Z |
| 其中 Agent 控制机器人（`agent-robot`） | **94** |
| 其中 LLM / 工具使用地标（`llm-agent`） | **88** |
| 年份 | 2018–2026（2023: 76 · 2024: 63 · 2025: 69 · 2026: 45） |
| 抽样链接 | 本版抽检 6/6 HTTP 200（arXiv + GitHub）；上版 10/10 |
| 摘要 | **276 / 276** 来自 arXiv API 或 abs 页同一官方文本；失败标「摘要暂缺」 |

## 怎么读

1. 先读 [`CROSSWALK.zh.md`](CROSSWALK.zh.md) 的定义、「感知 → 动力学 → 语言 → 动作」草图，以及 **Agent 控制机器人** 与 `WM` / `VLA` / `VLN` / `VLM` 的对照。
2. 用 [`PAPERS.md`](PAPERS.md) 按年份扫标题（标签含 `agent-robot` / `llm-agent` 的即 Agent 线）；需要摘要时打开 [`PAPERS_DETAIL.md`](PAPERS_DETAIL.md) 对应编号。
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
| [`oss_repos.md`](oss_repos.md) | 42 个已核验仓库对照 |
| [`oss_repos.jsonl`](oss_repos.jsonl) | OSS 机器可读行 |
| [`forks_created.md`](forks_created.md) | 已 fork 到 `topsun-bot` 的上游 |

### 复现

| 文档 | 用途 |
| --- | --- |
| [`scripts/fetch_arxiv_abstracts.py`](scripts/fetch_arxiv_abstracts.py) | 从 arXiv 抓摘要（不编造；API 限流回退 abs 页） |
| [`scripts/render_zh_docs.py`](scripts/render_zh_docs.py) | 由 jsonl 重排 `PAPERS.md` / `PAPERS_DETAIL.md` |
| [`scripts/new_papers_meta.py`](scripts/new_papers_meta.py) | 本轮自检索 +93 篇的中文转述与标签 |
| [`scripts/pack_extra_meta.py`](scripts/pack_extra_meta.py) | 研究员包去重后 +52 篇的中文转述与标签 |
| [`research/agent_robotics/`](research/agent_robotics/) | 研究员核验包原文（79 篇清单 + 查询元数据 + Agent 对照） |

开源对照覆盖 Dreamer 家族、Transformer / 扩散世界模型、Cosmos、JEPA、3D-VLA、OpenVLA / Octo / OpenPI / GR00T、VLN 栈、Minecraft 周边，以及 VoxPoser / Eureka / RoCo / OK-Robot / CoELA 等 Agent 控制栈。家族覆盖与排除项写在 [`oss_repos.md`](oss_repos.md)。

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
- 收录优先机器人、具身、视频预测 `WM`、`VLA` / `VLN` / `VLM`，以及会输出可执行动作 / 技能 / 代码的 Agent；纯 NLP 聊天与和控无关的「世界模型」比喻已排除。ReAct / Reflexion / HuggingGPT 等仅作为被机器人闭环广泛引用的规划 / 工具使用地标保留。
- OSS 表中的 star 与「最近活动」是调研日快照，依赖前请再查。
- 这是**索引 + 交叉对照**，不是「我们跑过每篇实验」。

细节见 [`oss_repos.md`](oss_repos.md) 的 Family coverage / Exclusions，以及 [`CROSSWALK.zh.md`](CROSSWALK.zh.md)。

## 方法

1. **输入：** 世界模型表 + `VLA` / `VLN` / `VLM` 表 + **Agent 控制机器人** 地标 / 检索命中；条目事先经 arXiv API 和 / 或 abs 页核验。
2. **去重：** 主键为 arXiv ID（去掉 `vN`）；否则用规范化标题。
3. **标签：** `world_model` 来自 WM 表；`VLA` / `VLN` / `VLM` / `intersection` 来自 VLA 表；`agent-robot` / `llm-agent` 来自 Agent 扩表；多源取并集。
4. **扩表（2026-09-12）：** 在 131 篇基础上分两段合并。（1）自检索 Agent / 代码即策略 / 开放式具身 / 多智能体，以及尚未收录的 `WM` / `VLA` / `VLN` 地标，**+93**。（2）优先并入 `research/agent-robotics-pack` 的 79 篇核验清单，去重后 **+52**。合计 **276**。禁止编造 ID。错误 ID 碰撞（如误把无关论文当成 STEVE-1）已丢弃。
5. **摘要：** [arXiv API](http://export.arxiv.org/api/query) 的 `id_list` 批量拉取；限流则回退 `https://arxiv.org/abs/<id>`。只收录抓到的原文；失败标「摘要暂缺」。中文是对该原文的转述。本版扩表时 API 曾 429，新条目摘要来自 abs 页同一官方文本。
6. **抽样：** 合并后的论文 URL 曾用 `curl -sI` 抽检。

本版用过的检索（节选，非穷尽）：`ti:"Code as Policies"`、`ti:Voyager AND all:Minecraft`、`ti:VoxPoser`、`ti:AutoRT`、`ti:CoELA`、`ti:GR00T`、`ti:"Gemini Robotics"`、`all:"LLM agent" AND all:robot AND cat:cs.RO`、`all:"embodied agent" AND all:"language model"`、`ti:"Vision-Language-Action"`（2025–2026）、`ti:"world model" AND all:robot`（2026），以及已知地标 `id_list`（SayCan / Inner Monologue 已在旧包中，未重复计入）。研究员包查询见 [`research/agent_robotics/agent_meta.json`](research/agent_robotics/agent_meta.json)：`LLM agent robotics`、`code as policies robot`、`embodied agent LLM`、`tool use robot LLM`、`ReAct robot planning`、`multi-agent LLM robot`、`Voyager GITM MineDojo`、`Instruct2Act SayPlan RoboGPT` 等。

本快照**不包含**原始 `build_pack.py` 或 `verify_sample.log`。重建摘要：

```bash
python3 scripts/fetch_arxiv_abstracts.py
python3 scripts/render_zh_docs.py
```

## 标签

一篇可带多个标签。计数见 [`PAPERS.md`](PAPERS.md)。

| 标签 | 含义 | 篇数 |
| --- | --- | ---: |
| `agent-robot` | Agent 控制机器人 / 具身编排 | 94 |
| `llm-agent` | LLM / 工具使用 / 规划智能体 | 88 |
| `world_model` | 世界模型主线 | 74 |
| `VLA` | 视觉—语言—动作策略 | 63 |
| `VLM` | 视觉—语言模型 / 具身多模态 | 38 |
| `intersection` | 跨家族 / 桥接（如 `WM` 引导的 `VLA`） | 26 |
| `VLN` | 视觉—语言导航 | 22 |

## 许可

本包中的调研文字用于仓库文档。各论文与开源项目保留各自许可。

尤其注意非商业许可：历史上的 `V-JEPA` 为 CC-BY-NC；MineRL 为 CC-BY-NC-SA。`V-JEPA` 2 为 MIT，商用前仍须核对上游 `LICENSE`。
