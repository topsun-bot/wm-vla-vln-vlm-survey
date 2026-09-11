# 交叉对照（中文）

`World Model` × `VLM` × `VLA` × `VLN` 的短对照，面向机器人 / ODM 栈。不编造引用。

英文原文：[`CROSSWALK.md`](CROSSWALK.md)。

## 本页目录

- [定义](#定义)
- [如何组合](#如何组合)
- [开源缺口](#开源缺口)
- [工程接入](#工程接入)
- [本包指针](#本包指针)

## 定义

- **`World Model`（`WM`，世界模型）：** 学习到的（常为潜空间）动力学，在动作条件下预测未来状态 / 观测 / 奖励。用于想象、规划或策略训练，而不必每一步都滚真实环境。
- **`VLM`（Vision-Language Model）：** 把图像 / 视频与语言互映射的多模态基础模型（描述、VQA、接地）。提供感知与语义接口；**本身通常不是**动作策略。
- **`VLA`（Vision-Language-Action）：** 把视觉 + 语言指令映射到机器人动作（连续控制或动作 token）的策略 / 基础模型。开源例子：OpenVLA、Octo。
- **`VLN`（Vision-and-Language Navigation）：** 在视觉环境中跟随自然语言路线指令的智能体（离散拓扑图或连续 Habitat 风格）。例子：`VLN-CE`、NavGPT、MapGPT。
- **交叉（`intersection`）：** 显式把 `WM` 想象接到 `VLA` / `VLN`，或在语言条件控制 / 导航里使用世界模型式预测。

## 如何组合

- **感知 → 潜空间：** `VLM` / 视觉编码器把 RGB(D) 压成 token 或 latent，再交给 `WM` 或策略。
- **潜空间动力学：** `WM` 在动作条件下预测下一 latent（或像素 / 占据 / 3D）——Dreamer 式 RSSM、Transformer `WM`、扩散 / 视频 `WM`、JEPA 预测器、占据 `WM`（如 OccWorld 一线）。
- **语言接地：** 指令或目标经 `VLM` 嵌入、LLM 规划器，或语言条件的 `WM` 动作进入（如 Pandora 式语言动作；LUMOS 式语言条件模仿 + `WM`）。
- **动作 / 导航头：**
  - 操作 → `VLA` 策略（直接），或 `WM` 想象 + 规划器 / actor-critic。
  - 导航 → `VLN` 策略 / 在地图上的 LLM tool-calling，或基于 `WM` 的预测导航（如 X-MOBILITY 一类）。
- **典型栈：** 传感器 → `VLM` / 编码器 →（可选：`WM` 做 what-if）→ `VLA` / `VLN` 或 MPC → 底层控制器。
- **数据路径：** 大规模轨迹（Open X-Embodiment）训 `VLA`；视频 / 交互数据训 `WM`；`VLN` 用指令—路径数据（R2R / RxR / `VLN-CE`）。

## 开源缺口

依据 [`oss_repos.md`](oss_repos.md) 的诚实说明：

- **GAIA-1/2（Wayve）：** 官方代码 / 权重**未开放**；社区 `lucidrains/gaia2-pytorch` 只是架构级 WIP。
- **Genie（DeepMind）：** 官方**未开放**；开源复现 `flairox/jafar`、`p-doom/jasmine` 近似 Genie 式 tokenizer / LAM / 动力学。
- **UniSim：** 未找到可交互的官方世界模型代码（仅研究页；`google/unisim` 无关）。
- **GameNGen：** **无核验官方 OSS**；本调研中最接近的交互视频 `WM` 开源是 Oasis / DIAMOND。

**确实开放且有用的：** DreamerV3 / DayDreamer，IRIS / DIAMOND / Oasis，NVIDIA Cosmos predict 栈，`V-JEPA` 2，3D-VLA / RoboDreamer，OpenVLA / Octo / Open X-Embodiment，`VLN-CE` / NavGPT / MapGPT。

优先核验 `LICENSE` 与近期提交；若干有用仓库仍无许可证文件（OSS 表中已标注）。已 fork 到 `topsun-bot` 的上游见 [`forks_created.md`](forks_created.md)。

## 工程接入

- **先选策略还是模型：** 现在就要可部署的语言 → 动作，走 OpenVLA / Octo；需要想象 / 离线仿真 / 样本效率，走 DreamerV3 / Cosmos-predict / 扩散 `WM`。
- **论文 ≠ 可跑栈：** Genie / GAIA / UniSim / GameNGen 是地标论文，不是即插即用依赖——按重实现成本或闭源 API 做计划。
- **潜空间 vs 像素 `WM`：** RSSM / JEPA 更便宜，适合控制回路；像素 / 视频扩散 `WM` 更适合可视化与数据生成，机载 ODM 更重。
- **3D / 占据 `WM`：** OccWorld、Gaussian `WM`、3D-VLA 比纯 Atari 式视频 `WM` 更贴合偏建图的 ODM。
- **语言接口：** 用 `VLM` 做接地 / 指令解析；不要把完整 LLM 塞进 100 Hz 回路——缓存目标，`WM` / `VLA` 中频运行，底层做跟踪。
- **评测：** 真机或连续 `VLN-CE` 指标与 Atari / Minecraft `WM` 分数分开报；数字不能直接迁移。
- **许可：** 原版 `V-JEPA` 为 CC-BY-NC；`V-JEPA` 2 为 MIT。MineRL 为 NC-SA。商用前请核对。
- **数据：** Open X-Embodiment 是许多 `VLA` 的共享底座；`WM` 常需要动作条件视频，往往要在机上采集（DayDreamer 的教训）。
- **安全：** `WM` 想象可能提出物理上不成立的未来——用约束 / 残差真机微调把门，再信任开环展开。
- **ODM 建图：** 把 `WM` 的占据 / Gaussian 预测当作滤波器的*先验*，不是真值；与真实传感器融合。

## 本包指针

| 内容 | 文档 |
| --- | --- |
| 标题索引 | [`PAPERS.md`](PAPERS.md) / [`papers_merged.jsonl`](papers_merged.jsonl) |
| 逐篇卡片 | [`PAPERS_DETAIL.md`](PAPERS_DETAIL.md) / [`papers_detailed.jsonl`](papers_detailed.jsonl) |
| OSS 对照 | [`oss_repos.md`](oss_repos.md) / [`oss_repos.jsonl`](oss_repos.jsonl) |
| Fork 清单 | [`forks_created.md`](forks_created.md) |
| 方法与缺口 | [`README.md`](README.md) |
