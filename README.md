# World Model × VLA / VLN / VLM 调研索引

> **维护仓库：** [`topsun-bot/wm-vla-vln-vlm-survey`](https://github.com/topsun-bot/wm-vla-vln-vlm-survey)（默认分支 `main`）。  
> 相关开源 fork 清单见 [`forks_created.md`](forks_created.md)。论文本身仍属原作者；本仓库只收录**已核验**的链接与摘要，不声称复现了每篇实验。

面向机器人 / 具身智能工程的可落地文献包：把 World Model（世界模型）与 VLA / VLN / VLM 交叉处的论文、开源仓库和组合关系收成一份可核对的索引。

## 目的

- 给工程师一份**单一、可核验**的索引：世界模型与视觉—语言—动作 / 导航 / 多模态模型中，真正落到机器人与具身 AI 的文献。
- 标明**开源 vs 闭源**：对 GAIA、Genie、UniSim、GameNGen 等标志性工作保持诚实，不把论文当成可直接依赖的代码。
- 给出一条短的**组合草图**（感知 → 潜空间动力学 → 语言接地 → 动作/导航），便于接到 ODM / 机器人栈。
- 每篇论文不只列标题：在 [`PAPERS_DETAIL.md`](PAPERS_DETAIL.md) 中提供从 arXiv **实抓**的摘要（中文转述）与要点。

## 统计

| 指标 | 数值 |
| --- | ---: |
| 已核验论文（去重后） | **131** |
| 已核验开源仓库 | **31** |
| 检索 / 合并时间（UTC） | **2026-09-11T15:31:03Z** |
| 抽样链接探测 | 10/10 HTTP 200 |
| 摘要来源 | arXiv API 或 abs 页面；失败则标「摘要暂缺」 |

## 目录与链接

| 文件 | 作用 |
| --- | --- |
| [`PAPERS.md`](PAPERS.md) | 全部 131 篇的标题表（编号、标题、年份、标签、arXiv/DOI、URL） |
| [`PAPERS_DETAIL.md`](PAPERS_DETAIL.md) | **逐篇详注**：标题 / 年份 / 标签 / 链接 + 中文摘要 + 要点（方法、贡献、与 WM×VLA/VLN/VLM 的关系） |
| [`papers_merged.jsonl`](papers_merged.jsonl) | 机器可读合并记录（来源 + 标签） |
| [`papers_detailed.jsonl`](papers_detailed.jsonl) | 机器可读详注（英文摘要原文 + 中文转述 + 要点） |
| [`CROSSWALK.md`](CROSSWALK.md) | 英文：定义、组合关系、OSS 缺口、ODM 接入笔记 |
| [`CROSSWALK.zh.md`](CROSSWALK.zh.md) | 中文对照版（与英文并行保留） |
| [`oss_repos.md`](oss_repos.md) | 已核验开源对照表（31 个仓库） |
| [`oss_repos.jsonl`](oss_repos.jsonl) | 机器可读 OSS 行 |
| [`forks_created.md`](forks_created.md) | 已 fork 到 `topsun-bot` 的上游清单 |
| [`scripts/fetch_arxiv_abstracts.py`](scripts/fetch_arxiv_abstracts.py) | 从 arXiv API / abs 页抓取摘要（不编造） |

### 开源表

完整对照见 **[`oss_repos.md`](oss_repos.md)**（Dreamer 家族、Transformer/扩散世界模型、Cosmos、JEPA、3D-VLA、OpenVLA/Octo、VLN 栈、Minecraft 周边）。家族覆盖与**诚实排除项**写在该页。

已 fork 到本组织的上游见 **[`forks_created.md`](forks_created.md)**（OpenVLA、Octo、DreamerV3、V-JEPA 2、Cosmos-Predict、VLN-CE、Open X-Embodiment 等）。

## 方法论

1. **输入**：世界模型文献表 + VLA/VLN/VLM 文献表；条目事先经 arXiv API 和/或 abs 页核验。
2. **合并去重**：主键为 arXiv ID（去掉版本后缀 `vN`）；否则用规范化标题。
3. **标签**：`world_model` 来自 WM 表；`VLA` / `VLN` / `VLM` / `intersection` 来自 VLA 表；多源论文取标签并集。
4. **扩表规则**：仅当去重后不足 100 篇才追加检索；**本包已有 131 篇，未再扩表**。禁止编造 ID。
5. **摘要**：用 [arXiv API](http://export.arxiv.org/api/query) 的 `id_list` 批量拉取；遇限流则回退到 `https://arxiv.org/abs/<id>` 页面解析。只收录抓到的原文；失败标「摘要暂缺」，并保留已核验链接。中文摘要是对**该原文**的忠实转述，不是另写一篇未发表论文。
6. **抽样**：合并后的论文 URL 曾用 `curl -sI` 抽检。

本快照**不包含**原始构建脚本 `build_pack.py` 或 `verify_sample.log`；重建摘要可用 `python3 scripts/fetch_arxiv_abstracts.py`。

## 诚实的开源缺口

下列标志性系统在本包中**没有**核验到与论文匹配的官方可训练 / 可推理开源栈（权重 + 代码）：

| 系统 | 现状（本调研） |
| --- | --- |
| **GAIA-1/2**（Wayve） | 官方代码/权重未开放；社区仅有架构级 WIP：`lucidrains/gaia2-pytorch` |
| **Genie**（DeepMind） | 官方未开放；开源复现近似：`flairox/jafar`、`p-doom/jasmine` |
| **UniSim** | 未找到可交互的官方世界模型代码（研究页；`google/unisim` 是无关仓库） |
| **GameNGen** | 无核验过的官方 OSS；本调研中最接近的交互视频 WM 开源是 Oasis / DIAMOND |

此外：

- 部分社区复现相对论文仍是 WIP / 不完整。
- 收录优先机器人 / 具身 / 视频预测 WM 与 VLA/VLN/VLM；纯 NLP 的 VLM 以及与控制无关的「世界模型」比喻在收集阶段已排除。
- OSS 表中的 star 数与「最近活动」是调研日快照，依赖前请再查。
- 这是**索引 + 交叉对照**，不是「我们跑过每篇实验」的声明。

细节见 [`oss_repos.md`](oss_repos.md) 的 Family coverage / Exclusions，以及 [`CROSSWALK.zh.md`](CROSSWALK.zh.md)。

## 标签说明

论文可带多个标签（见 [`PAPERS.md`](PAPERS.md) 计数）：

| 标签 | 含义 | 篇数（约） |
| --- | --- | ---: |
| `world_model` | 世界模型主线 | 58 |
| `VLM` | 视觉—语言模型 / 具身多模态 | 23 |
| `VLA` | 视觉—语言—动作策略 | 20 |
| `intersection` | 跨家族 / 桥接（如 WM 引导的 VLA、语言条件 WM） | 19 |
| `VLN` | 视觉—语言导航 | 18 |

## 如何读这个包

1. 先看 [`CROSSWALK.zh.md`](CROSSWALK.zh.md) 里的定义与「感知 → 动力学 → 语言 → 动作」草图。
2. 用 [`PAPERS.md`](PAPERS.md) 扫标题；需要摘要与贡献时打开 [`PAPERS_DETAIL.md`](PAPERS_DETAIL.md) 对应编号。
3. 要落地代码时对照 [`oss_repos.md`](oss_repos.md)，并核对 [`forks_created.md`](forks_created.md) 是否已有 `topsun-bot` fork。
4. 自动化请读 jsonl，不要解析 Markdown 表格。

## 许可说明

本包中的调研文字用于仓库文档。各论文与开源项目保留各自许可——尤其注意非商业许可（历史上的 V-JEPA 为 CC-BY-NC；MineRL 为 CC-BY-NC-SA）。V-JEPA 2 为 MIT，商用前仍须核对上游 LICENSE。
