# 论文详注

每篇一张卡片：年份、标签、链接、摘要、要点。

中文摘要是对 arXiv **实抓英文摘要**的忠实转述，不是另写未发表论文。

本版 **276 / 276** 取得英文原文；无「摘要暂缺」。

## 本页目录

- [阅读说明](#阅读说明)
- [年份一览](#年份一览)
- [2026 年（45 篇）](#2026-年)
- [2025 年（69 篇）](#2025-年)
- [2024 年（63 篇）](#2024-年)
- [2023 年（76 篇）](#2023-年)
- [2022 年（18 篇）](#2022-年)
- [2021 年（1 篇）](#2021-年)
- [2020 年（1 篇）](#2020-年)
- [2019 年（1 篇）](#2019-年)
- [2018 年（2 篇）](#2018-年)

## 阅读说明

- 英文原文与机器字段：[`papers_detailed.jsonl`](papers_detailed.jsonl)。
- 标题速查（按年列表）：[`PAPERS.md`](PAPERS.md)。
- 摘要来源：arXiv API（[`export.arxiv.org`](http://export.arxiv.org/api/query)）
  或 abs 页（`https://arxiv.org/abs/<id>`）。
- 抓取失败会写 **摘要暂缺**，并保留已核验链接。
- 要点只依据该摘要：方法、贡献、与 Agent / `WM` × `VLA` / `VLN` / `VLM` 的关系。
  不编造摘要中未出现的实验数字。

## 年份一览

| 年份 | 篇数 | 编号 | 跳转 |
| ---: | ---: | --- | --- |
| 2026 | 45 | 1–45 | [↓ 2026 年](#2026-年) |
| 2025 | 69 | 46–114 | [↓ 2025 年](#2025-年) |
| 2024 | 63 | 115–177 | [↓ 2024 年](#2024-年) |
| 2023 | 76 | 178–253 | [↓ 2023 年](#2023-年) |
| 2022 | 18 | 254–271 | [↓ 2022 年](#2022-年) |
| 2021 | 1 | 272 | [↓ 2021 年](#2021-年) |
| 2020 | 1 | 273 | [↓ 2020 年](#2020-年) |
| 2019 | 1 | 274 | [↓ 2019 年](#2019-年) |
| 2018 | 2 | 275–276 | [↓ 2018 年](#2018-年) |

## 2026 年

共 45 篇。先扫目录，再下翻卡片。

- [1. A Comprehensive Survey and Systematic Real-World Evaluation of Embodied Vision-and-Language Navigation](#p-1)  `VLN`
- [2. AdaVLA: Adaptive Step Flow Matching for Training-free Acceleration of Vision-Language-Action Models](#p-2)  `intersection`
- [3. Addressing the Orchestration Gap in Generalist Robots via Physical Agency](#p-3)  `agent-robot`
- [4. AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight](#p-4)  `intersection`
- [5. AgenticNav: Zero-Shot Vision-and-Language Navigation as a Tool-Calling Harness](#p-5)  `intersection`
- [6. AirForesight: Current-to-Future Spatial Map Imagination with Cross-Space Planning Consistency for UAV-VLN](#p-6)  `VLN`
- [7. CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](#p-7)  `agent-robot` · `llm-agent`
- [8. Causal World Modeling for Robot Control](#p-8)  `world_model`
- [9. Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning](#p-9)  `world_model` · `VLA` · `intersection`
- [10. DDP-WM: Disentangled Dynamics Prediction for Efficient World Models](#p-10)  `world_model`
- [11. DreamFly: Causal Memory and Receding-Horizon Diffusion Planning for Aerial Vision-Language Navigation](#p-11)  `VLN`
- [12. EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](#p-12)  `agent-robot` · `VLA`
- [13. Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention](#p-13)  `world_model`
- [14. Fast-WAM: Do World Action Models Need Test-time Future Imagination?](#p-14)  `world_model`
- [15. From Semantic Grounding to Decision Optimization: A Unified Framework for Long-Horizon UAV Vision-Language Navigation](#p-15)  `VLN`
- [16. GeniWorld: A Generalizable Interactive World Model for Robotic Manipulation via Visual Actions](#p-16)  `world_model`
- [17. Grounding Generated Videos in Feasible Plans via World Models](#p-17)  `world_model`
- [18. H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model](#p-18)  `world_model`
- [19. HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments](#p-19)  `VLN`
- [20. If, Then, Otherwise: Diagnosing Conditional Branching in Vision-Language Navigation](#p-20)  `VLN`
- [21. LLawCo: Learning Laws of Cooperation for Modeling Embodied Multi-Agent Behavior](#p-21)  `agent-robot`
- [22. LookStep: Efficient Vision-Language Navigation with Linguistic Foresight and Event Driven Memory](#p-22)  `VLN`
- [23. MetaWorld: Skill Transfer and Composition in a Hierarchical World Model for Grounding High-Level Instructions](#p-23)  `world_model`
- [24. MobileVLA-R1 2.0: RL-Enhanced Reasoning for Mobile Robot Control](#p-24)  `agent-robot` · `VLA` · `VLN`
- [25. OSCAR: Omni-Embodiment Action-Conditioned World Model for Robotics](#p-25)  `world_model`
- [26. PGN: Design and Implementation of a Vision-Language Navigation System Based on Pangu Multimodal Foundation Model](#p-26)  `intersection`
- [27. PlayWorld: Learning Robot World Models from Autonomous Play](#p-27)  `world_model`
- [28. PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation](#p-28)  `world_model`
- [29. RACO: Reliability-Aware Coarse-Goal Optimization for Inspection-Oriented UAV Vision-Language Navigation](#p-29)  `VLN`
- [30. RecoverFly: A Failure-Aware Reinforcement Learning Post-Training Framework for Aerial Vision-Language Navigation](#p-30)  `VLN`
- [31. Revisiting Topological Graphs for Macro Action based Closed-loop Reinforcement Learning of Vision Language Navigation in Continuous Environment](#p-31)  `VLN`
- [32. RynnBrain: Open Embodied Foundation Models](#p-32)  `VLA` · `VLM`
- [33. Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control](#p-33)  `agent-robot` · `VLA`
- [34. TANGO: Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Language-Action Model](#p-34)  `VLN`
- [35. TiPToP: A Modular Open-Vocabulary Robot Manipulation System That Plans](#p-35)  `agent-robot`
- [36. Verification of the Implicit World Model in a Generative Model via Adversarial Sequences](#p-36)  `world_model`
- [37. VLA-Precision: Asymmetric Co-Bootstrapping for Efficient Real-World Online RL of Vision-Language-Action Models](#p-37)  `VLA`
- [38. What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents](#p-38)  `agent-robot` · `VLA`
- [39. World Action Models are Zero-shot Policies](#p-39)  `world_model` · `VLA` · `intersection`
- [40. World Model for Robot Learning: A Comprehensive Survey](#p-40)  `VLM` · `world_model`
- [41. World Models for Robotic Manipulation: A Survey](#p-41)  `intersection` · `world_model`
- [42. World-Gymnast: Training Robots with Reinforcement Learning in a World Model](#p-42)  `world_model`
- [43. World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis](#p-43)  `world_model` · `VLA` · `intersection`
- [44. π₀.₇: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](#p-44)  `VLA`
- [45. τ₀-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation](#p-45)  `intersection`

<a id="p-1"></a>

### 1. A Comprehensive Survey and Systematic Real-World Evaluation of Embodied Vision-and-Language Navigation

- **年份：** 2026
- **标签：** `VLN`
- **链接：** [arXiv:2607.09792](https://arxiv.org/abs/2607.09792)

**摘要：** 导航是自主系统的基础能力，但多数方法依赖结构化模型与强先验，开放不确定环境中鲁棒性不足。`VLN` 以数据驱动融合自然语言理解与视觉感知，系统分类与实机验证仍有限。本综述沿动作范式（层次化与单体）和模型范式（判别与生成）组织前沿方法并分析优劣，并在实体机器人上对代表性 `VLN` 配置做真实评测。十个多样真实场景显示仿真与实机差距显著：单体仅 RGB 方法仿真成功率 61%、实机 22%，层次化框架实机达 51%。最后指出感知、决策与控制的关键挑战。

**要点：**

- **方法：** 沿层次化/单体动作范式与判别/生成模型范式系统综述 `VLN`，并在实体机器人上评测代表性配置。
- **贡献：** 揭示所测配置下仿真与实机成功率差距，层次化框架实机更稳健，并归纳感知、决策与控制挑战。
- **关系：** 面向 `VLN` 方法谱系与实机鸿沟，为后续结合 `World Model` 或 `VLA` 的导航提供评测参照。

---

<a id="p-2"></a>

### 2. AdaVLA: Adaptive Step Flow Matching for Training-free Acceleration of Vision-Language-Action Models

- **年份：** 2026
- **标签：** `intersection`
- **链接：** [arXiv:2608.29208](https://arxiv.org/abs/2608.29208)

**摘要：** 建立在 `VLM` 之上的 `VLA` 借助互联网规模知识与多模态推理提升机器人能力，但计算开销制约端侧部署与实时响应。现有加速常需微调或训练数据，且多只降低 `VLM` 推理成本，未处理 flow matching 中的迭代 ODE 求解。本文提出 AdaVLA：面向 flow-matching `VLA` 的在线、免训练自适应框架，由轨迹曲率度量动作生成置信度，动态减少推理步并自适应调整 MLP 剪枝比，无需训练数据。在 LIBERO 与 Jetson AGX Orin 上，对 π₀.₅ 与 X-VLA 分别获得 1.87× 与 2.24× 加速且成功率几乎不降，并以 SmolVLA 在真实任务上验证鲁棒性。

**要点：**

- **方法：** 免训练在线框架，用 flow matching 轨迹曲率度量置信度，动态减步并自适应 MLP 剪枝。
- **贡献：** 在 LIBERO 与 Jetson 上加速 π₀.₅ 与 X-VLA 且成功率几乎不降，并以 SmolVLA 验证真实任务鲁棒性。
- **关系：** 加速基于 `VLM` 的 flow-matching `VLA` 端侧推理，文中未涉及 `World Model` 实验。

---

<a id="p-3"></a>

### 3. Addressing the Orchestration Gap in Generalist Robots via Physical Agency

- **年份：** 2026
- **标签：** `agent-robot`
- **链接：** [arXiv:2607.21725](https://arxiv.org/abs/2607.21725)

**摘要：** Physical Agency 指出通才机器人的编排缺口：仅有冻结 `VLA` 不够，需要规划、执行、验证与恢复的闭环物理智能体。系统把 TiPToP 等当作可调用工具，强调 Agent 层与策略层分离。

**要点：**

- **方法：** 以物理智能体编排规划、执行、验证与恢复，调用冻结技能后端。
- **贡献：** 明确「编排缺口」并给出与平坦 `VLA` 对照的 Agent 架构。
- **关系：** 2026 年 Agent 控制机器人的纲领性系统文。

---

<a id="p-4"></a>

### 4. AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight

- **年份：** 2026
- **标签：** `intersection`
- **链接：** [arXiv:2607.14997](https://arxiv.org/abs/2607.14997)

**摘要：** 语言条件四旋翼飞行需锚定语义目标、预判自运动的视觉后果，并输出平滑可执行的控制参考。现有空中 `VLN` 与 `VLA` 多用离散动作、高层航点或瞬时速度，对动作如何改变未来观测监督不足。本文提出 AeroAct：以动作为中心的 world-action model，适配预训练视频扩散 Transformer，由自我中心视觉历史、本体感觉与语言预测局部轨迹-动作块；训练用未来第一人称帧作稠密后果监督，部署时直接解码动作而不生成未来视频。配合 DiffAero 管线、手持采集与自引导时序一致性，闭环仿真与实机表明时序视觉上下文提升跟踪与搜索，且策略可在实体四旋翼上执行。

**要点：**

- **方法：** 将预训练视频扩散 Transformer 适配为动作中心 WAM，训练用未来第一人称帧作后果监督，部署只解码动作。
- **贡献：** 构建对齐的视-状态-语言-动作数据与自引导时序一致性，闭环仿真与实机显示跟踪/搜索提升且可上四旋翼。
- **关系：** 把 `World Model` 与空中 `VLN`/`VLA` 结合，用未来观测监督动作如何改变第一人称视野。

---

<a id="p-5"></a>

### 5. AgenticNav: Zero-Shot Vision-and-Language Navigation as a Tool-Calling Harness

- **年份：** 2026
- **标签：** `intersection`
- **链接：** [arXiv:2606.10577](https://arxiv.org/abs/2606.10577)

**摘要：** 零样本连续环境 `VLN`（`VLN-CE`）已可借助大型 `VLM` 实现，但现有方法常依赖学得的航点预测器，限制动作空间且未有效利用深度；记忆则堆积冗长无关历史或检索跨回合经验，削弱零样本设定。本文提出 AgenticNav：将零样本 `VLN-CE` 重思为 `VLM` 与环境的 agentic 接口，把动作、深度与记忆暴露为可调用工具——在 RGB 中直接选目标像素并转为运动，按需查询像素深度，并以紧凑地图加回忆工具选择性回顾过去观测。在 R2R-CE 上以相同 `VLM` 骨干取得零样本 SOTA，实机验证泛化；消融表明动作工具优于传统航点预测器，深度工具与 agentic 记忆亦有贡献。

**要点：**

- **方法：** 将零样本 `VLN-CE` 视为 `VLM` 与环境的工具调用接口，暴露动作、深度与记忆三类可调用工具。
- **贡献：** 同骨干下取得 R2R-CE 零样本 SOTA，实机显示泛化；消融表明动作工具优于航点预测器。
- **关系：** 用 `VLM` 做零样本 `VLN` 工具调用，文中未涉及 `World Model` 实验。

---

<a id="p-6"></a>

### 6. AirForesight: Current-to-Future Spatial Map Imagination with Cross-Space Planning Consistency for UAV-VLN

- **年份：** 2026
- **标签：** `VLN`
- **链接：** [arXiv:2608.12835](https://arxiv.org/abs/2608.12835)

**摘要：** UAV-VLN 要求智能体遵循语言指令、从稀疏多视图推断空间结构，并在复杂室外执行可行 3D 运动。现有方法多将视觉-语言直接映射为动作，显式场景锚定与面向未来的空间推理不足。本文提出 AirForesight：先从多视图学习结构化当前地图，并以当前地图重建与未来轨迹预测联合监督；在结构化因果注意力下将当前空间知识传播到未来地图推理，聚合后预测下一 3D 航点。跨空间规划一致性损失促使地图空间预测轨迹与由真值航点位移得到的专家动作方向一致。OpenUAV 与 AerialVLN-S 实验及消融支持该框架的有效性与稳定性。

**要点：**

- **方法：** 学习当前地图表示并以重建与未来轨迹联合监督，经因果注意力传播到未来地图再预测下一 3D 航点。
- **贡献：** 跨空间规划一致性损失对齐地图轨迹与专家方向，OpenUAV 与 AerialVLN-S 实验及消融支持有效性。
- **关系：** 为 UAV-VLN 引入当前到未来的空间地图想象，属面向未来的场景推理而非独立 `World Model` 实验。

---

<a id="p-7"></a>

### 7. CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation

- **年份：** 2026
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2603.22435](https://arxiv.org/abs/2603.22435)

**摘要：** CaP-X 提供评测与改进机器人操作编码智能体的框架，直接继承 Code as Policies 一线，用基准衡量「写策略代码的 Agent」在操作上的能力与改进空间。

**要点：**

- **方法：** 为机器人操作编码 Agent 建立评测与改进框架。
- **贡献：** 把 Code as Policies 推进到可比较的基准与改进循环。
- **关系：** 2026 年代码即策略 Agent 评测，补全 2022 地标之后的缺口。

---

<a id="p-8"></a>

### 8. Causal World Modeling for Robot Control

- **年份：** 2026
- **标签：** `world_model`
- **链接：** [arXiv:2601.21998](https://arxiv.org/abs/2601.21998)

**摘要：** Causal World Modeling for Robot Control 强调因果世界建模以服务机器人控制，针对相关但不一定可干预的预测问题，把因果结构引入动作条件预测。

**要点：**

- **方法：** 以因果结构约束机器人控制用的世界模型。
- **贡献：** 把因果建模接到动作条件预测与控制。
- **关系：** 控制导向 `World Model`。

---

<a id="p-9"></a>

### 9. Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning

- **年份：** 2026
- **标签：** `world_model` · `VLA` · `intersection`
- **链接：** [arXiv:2601.16163](https://arxiv.org/abs/2601.16163)

**摘要：** Cosmos Policy 把视频世界模型微调为视觉运动控制与规划策略，展示 Cosmos 预测模型如何变成可部署的控制 / 规划器。

**要点：**

- **方法：** 微调视频世界模型以同时做控制与规划。
- **贡献：** 打通 Cosmos 类 WFM 到策略的路径。
- **关系：** `World Model` 直接变成策略，可被 Agent 调用。

---

<a id="p-10"></a>

### 10. DDP-WM: Disentangled Dynamics Prediction for Efficient World Models

- **年份：** 2026
- **标签：** `world_model`
- **链接：** [arXiv:2602.01780](https://arxiv.org/abs/2602.01780)

**摘要：** `World Model` 对自主机器人规划至关重要，但现有稠密 Transformer 模型计算开销大，难以实时部署。本文提出以解耦动力学预测为核心的 DDP-WM：假设观测场景中潜在状态演化可分解为物理交互驱动的稀疏主动力学与上下文驱动的背景更新。架构结合高效历史处理与动态定位以隔离主动力学，并用交叉注意力更新背景，优化资源分配并为规划器提供平滑优化景观。实验覆盖导航、精细桌面操作及可变形或多体交互；在 Push-T 上相对稠密 SOTA 约 9 倍推理加速，MPC 成功率由 90% 升至 98%。

**要点：**

- **方法：** 将潜状态演化解耦为稀疏主动力学与背景更新，结合历史处理、动态定位与交叉注意力。
- **贡献：** 在导航、桌面操作及可变形/多体任务上兼顾效率与性能，Push-T 上显著加速并提高 MPC 成功率。
- **关系：** 纯 `World Model` 效率工作，服务规划与导航等任务，文中未涉及 `VLA`/`VLM`。

---

<a id="p-11"></a>

### 11. DreamFly: Causal Memory and Receding-Horizon Diffusion Planning for Aerial Vision-Language Navigation

- **年份：** 2026
- **标签：** `VLN`
- **链接：** [arXiv:2608.12308](https://arxiv.org/abs/2608.12308)

**摘要：** 空中 `VLN` 要求智能体随时间整合视觉证据、规划未来动作，并在部分可观测下判断是否到达目标。将 `VLA` 适配到空中导航仍受历史上下文有限、规划时域短与隐式终止不可靠制约。本文提出基于 Dream-VLA 的扩散框架 DreamFly：以因果对齐历史记忆仅用当前决策步之前的观测增强视觉表示；将导航表述为滚动时域扩散规划，预测 K 步动作块但只执行第一步再重规划；LiteStop 从初始全掩码状态的动作 logits 直接估计停止概率。OpenFly 上 test-seen/unseen 的 SR 为 32.04%/29.46%、SPL 为 28.22%/23.54%，优于对比方法且导航误差最低。

**要点：**

- **方法：** 在 Dream-VLA 上引入因果历史记忆、滚动时域扩散规划（预测 K 步执行 1 步）及 LiteStop 显式终止。
- **贡献：** OpenFly seen/unseen 上 SR 与 SPL 优于对比方法，且导航误差最低。
- **关系：** 将 `VLA` 范式适配空中 `VLN`，用扩散规划未来动作结构，文中未单独做 `World Model` 实验。

---

<a id="p-12"></a>

### 12. EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents

- **年份：** 2026
- **标签：** `agent-robot` · `VLA`
- **链接：** [arXiv:2609.01281](https://arxiv.org/abs/2609.01281)

**摘要：** EmbodiedSkills 把技能决策当作执行提案：运行时检查前提、执行有界 `VLA`、事后验证，并用固定可执行技能接口连接规划、执行与恢复。在 RoboTwin 2.0 与 LIBERO 上，任务适应的低层 `VLA` 平均成功率分别达 86.20% 与 97.40%；记忆依赖的 RMBench 仍仅 12.5%，暴露 Agent 记忆挑战。

**要点：**

- **方法：** 统一技能接口做提案—前提检查—`VLA` 执行—结果验证与恢复。
- **贡献：** 在 RoboTwin / LIBERO 上给出强执行层，并暴露记忆任务缺口。
- **关系：** 可训练 Agent 层把 `VLA` 变成闭环技能系统。

---

<a id="p-13"></a>

### 13. Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention

- **年份：** 2026
- **标签：** `world_model`
- **链接：** [arXiv:2602.01801](https://arxiv.org/abs/2602.01801)

**摘要：** 自回归视频扩散支持流式生成，通向长视频合成、视频 `World Model` 与交互神经游戏引擎，但推理时 KV cache 增长推高延迟与显存，限制时序上下文并损害长程一致性。作者识别跨帧近重复缓存键、缓慢演化查询/键造成的冗余注意力，以及长提示交叉注意力中每帧仅少数 token 重要。据此提出免训练框架 FAST-AR：TempCache 按时间对应压缩 KV cache；AnnCA 用 ANN 选择帧相关提示 token 加速交叉注意力；AnnSA 将自注意力限制到语义匹配的键。可与现有自回归扩散骨干及 `World Model` 兼容，端到端加速达 5–10 倍，视觉质量近乎不变，长 rollout 吞吐稳定且峰值显存近乎恒定。

**要点：**

- **方法：** 免训练 FAST-AR 以 TempCache、AnnCA 与 AnnSA 压缩缓存并稀疏化自/交叉注意力。
- **贡献：** 兼容现有自回归扩散骨干与 `World Model`，长 rollout 近恒定显存与稳定吞吐，加速约 5–10 倍且质量近乎不变。
- **关系：** 加速视频 `World Model` 与自回归扩散推理，文中未涉及 `VLA`/`VLN`。

---

<a id="p-14"></a>

### 14. Fast-WAM: Do World Action Models Need Test-time Future Imagination?

- **年份：** 2026
- **标签：** `world_model`
- **链接：** [arXiv:2603.16666](https://arxiv.org/abs/2603.16666)

**摘要：** Fast-WAM 追问世界—动作模型是否必须在测试时做未来想象：研究能否在保持性能下跳过昂贵 rollout，以服务实时控制。

**要点：**

- **方法：** 分析测试时未来想象对世界—动作模型的必要性。
- **贡献：** 为实时 WAM 部署提供是否展开想象的实证。
- **关系：** `WM` 推理成本，影响 Agent 能否在线调用想象。

---

<a id="p-15"></a>

### 15. From Semantic Grounding to Decision Optimization: A Unified Framework for Long-Horizon UAV Vision-Language Navigation

- **年份：** 2026
- **标签：** `VLN`
- **链接：** [arXiv:2608.09564](https://arxiv.org/abs/2608.09564)

**摘要：** UAV-VLN 使空中智能体根据自我中心视觉观测，在开放 3D 环境中遵循自然语言指令。现有方法存在指令相关地标锚定弱、长时程历史利用不足、局部陷阱或重复探索下决策不稳等耦合问题。本文提出统一语义到决策框架：先将物体级语义与相对空间线索注入当前观测；再以相关性感知策略重加权完整历史缓冲，并将高相关帧转为结构化地标提示；最后以拓扑感知决策结合局部最优认知与组相对策略优化，奖励覆盖进度、目标、语义与路径合规。在 AerialVLN 与 OpenFly 上达到文中所述 SOTA。

**要点：**

- **方法：** 指令锚定语义增强、相关性感知历史聚合与拓扑感知组相对策略优化组成统一语义到决策框架。
- **贡献：** 在 AerialVLN 与 OpenFly 上达到文中所述 SOTA。
- **关系：** 面向长时程 UAV-VLN 的语义接地与决策优化，文中未涉及 `World Model` 或 `VLA`。

---

<a id="p-16"></a>

### 16. GeniWorld: A Generalizable Interactive World Model for Robotic Manipulation via Visual Actions

- **年份：** 2026
- **标签：** `world_model`
- **链接：** [arXiv:2608.06332](https://arxiv.org/abs/2608.06332)

**摘要：** 通用机器人策略在复杂未见环境中鲁棒性仍有限，多样真实环境中扩展学习与评测成本高。动作条件 `World Model` 常动作可控性不足且 OOD 泛化差。本文提出 GeniWorld：基于预训练视频生成模型，用 URDF 渲染将数值动作转为视觉动作表示，实现空间锚定控制，并显式解耦本体运动学与环境动力学以减轻场景过拟合。自回归视频预测结合高频运动学控制，可与策略及人类遥操作闭环交互。即便仅在有限固定场景数据上训练，域内与对高度随机未见环境的零样本泛化均较强；还可作为策略评测器，并在有限真实演示下生成多样操作轨迹以提升下游策略。

**要点：**

- **方法：** 用 URDF 渲染将数值动作转为视觉动作，解耦本体运动学与环境动力学，并以自回归视频预测做闭环交互。
- **贡献：** 有限固定场景训练下仍有强域内与零样本泛化，可用作策略评测器并生成轨迹提升下游策略。
- **关系：** 交互式机器人 `World Model`，服务策略评测与改进，文中未涉及 `VLN`/`VLM`。

---

<a id="p-17"></a>

### 17. Grounding Generated Videos in Feasible Plans via World Models

- **年份：** 2026
- **标签：** `world_model`
- **链接：** [arXiv:2602.01960](https://arxiv.org/abs/2602.01960)

**摘要：** 大规模视频生成模型展现零样本视觉规划能力，但生成计划常违反时间一致性与物理约束，映射为可执行动作时失败。本文提出 GVP-WM：用学得的动作条件 `World Model` 将视频计划锚定为可行动作序列。测试时先由初始与目标观测生成视频计划，再经视频引导的潜空间配置将其投影到动力学可行的潜轨迹流形。锚定被表述为目标条件潜空间轨迹优化，在 `World Model` 动力学下联合优化潜状态与动作，并保持与视频计划的语义对齐。实验表明该方法能从违反物理约束的零样本图像到视频及运动模糊视频中恢复可行长时程计划，覆盖导航与操作仿真。

**要点：**

- **方法：** 测试时先生成视频计划，再经视频引导潜空间配置，在 `World Model` 动力学下联合优化潜状态与动作。
- **贡献：** 能从违反物理约束的零样本视频计划中恢复可行长时程动作，覆盖导航与操作仿真。
- **关系：** 用 `World Model` 把视频生成规划锚定到可行动作，属 `WM` 规划，文中未涉及 `VLA`/`VLM`。

---

<a id="p-18"></a>

### 18. H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model

- **年份：** 2026
- **标签：** `world_model`
- **链接：** [arXiv:2602.11291](https://arxiv.org/abs/2602.11291)

**摘要：** `World Model` 因能预测未来状态转移而成为机器人规划与控制的核心。现有方法常强调视频生成或自然语言预测，难以锚定到机器人动作且长时程误差累积；经典任务与运动规划在逻辑空间建模转移，可执行且长时程稳健，但通常独立于视觉感知。本文提出层次化 `World Model`（H-WM），在统一框架中联合预测逻辑与视觉状态转移：高层逻辑 `World Model` 与低层视觉 `World Model` 结合，以层次化输出为长时程任务提供稳定中间引导，减轻误差累积。在多种 `VLA` 控制策略上的实验表明其引导有效且具一般性。

**要点：**

- **方法：** 统一框架联合预测逻辑与视觉状态转移，高层逻辑 `World Model` 与低层视觉 `World Model` 分层输出中间引导。
- **贡献：** 为长时程任务提供稳定中间引导以减轻误差累积，并在多种 `VLA` 控制策略上验证引导有效。
- **关系：** 层次化 `World Model` 直接指导多种 `VLA` 策略执行。

---

<a id="p-19"></a>

### 19. HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments

- **年份：** 2026
- **标签：** `VLN`
- **链接：** [arXiv:2608.12860](https://arxiv.org/abs/2608.12860)

**摘要：** 人形机器人 `VLN` 面临双足运动的物理约束、跨平台形态差异，以及运动引起的相机动态对自我中心观测的扭曲，现有基准未能充分覆盖。本文提出基于 NVIDIA Isaac Sim 的 HumanoidVLN：跨多样人形本体的物理接地仿真器与基准，演示四种机器人，并以强化学习运动策略加可互换的 PD 或 MPC 路径跟踪器构成层次化控制栈。环境来自艺术家场景与 3D Gaussian Splatting 重建；指令由多智能体管线加人工核验生成 933 条碰撞感知参考回合。四模型四本体上 JanusVLN 平均成功率最高；DualVLN 与 Unitree G1 的 sim-to-real 试点显示导航误差高度相关。

**要点：**

- **方法：** 在 Isaac Sim 上构建跨人形本体的物理接地 `VLN` 仿真与基准，层次化结合强化学习运动策略与 PD/MPC 跟踪。
- **贡献：** 提供可扩展本体、环境与经核验的指令回合，并报告跨模型/本体结果及初步 sim-to-real 相关性。
- **关系：** 为人形 `VLN` 提供物理接地评测床，兼容多种 `VLN` 模型，文中未涉及 `World Model`。

---

<a id="p-20"></a>

### 20. If, Then, Otherwise: Diagnosing Conditional Branching in Vision-Language Navigation

- **年份：** 2026
- **标签：** `VLN`
- **链接：** [arXiv:2608.17318](https://arxiv.org/abs/2608.17318)

**摘要：** `VLN` 智能体常按路线式指令走向固定目标来评测，但真实指令往往依赖环境观测：若条件成立则走一条路径，否则走另一条。现有评测对条件分支执行控制有限，难以区分感知、锚定、导航或逻辑决策失败。本文提出 CondVLN：基于可验证 3D 场景图谓词程序化生成条件指令，并控制分支深度、依赖链、空间组成、证据可观测性与指令时域，覆盖 AI2-THOR、Matterport3D、Gibson 与 ReplicaCAD 上逾 11500 条指令，以分支选择准确率与条件成功率诊断。四种 SOTA 智能体可看似合理导航却选错与场景条件不一致的分支；将条件锚定与导航执行分离的轻量神经符号模型使性能约提升 2 倍。

**要点：**

- **方法：** 基于可验证 3D 场景图谓词程序化生成条件指令，并用分支选择准确率与条件成功率诊断。
- **贡献：** 显示 SOTA `VLN` 智能体可看似合理导航却选错分支；神经符号分支选择将条件锚定与执行分离并提升性能。
- **关系：** 诊断 `VLN` 条件逻辑能力，文中未涉及 `World Model` 或 `VLA`。

---

<a id="p-21"></a>

### 21. LLawCo: Learning Laws of Cooperation for Modeling Embodied Multi-Agent Behavior

- **年份：** 2026
- **标签：** `agent-robot`
- **链接：** [arXiv:2606.28182](https://arxiv.org/abs/2606.28182)

**摘要：** 分散、部分可观测环境中，LLM 智能体常与伙伴或环境状态不对齐。LLawCo 让智能体反思失败、提炼「必要时说话」「等待伙伴」等高层次合作法则，再经监督微调写入思维链。作者构建基于 PARTNR 的大规模对话合作基准 PARTNR-Dialog；相对开源通信智能体，四类 LLM 骨干上 PARTNR-Dialog 平均成功率高 4.5%，TDW-MAT 高 6.8%。

**要点：**

- **方法：** 从失败中提炼合作法则并监督微调写入思维链，使推理对齐伙伴与任务。
- **贡献：** 提出 PARTNR-Dialog，并在该基准与 TDW-MAT 上提高合作效率与成功。
- **关系：** 多智能体具身合作 Agent，对齐通信与行为。

---

<a id="p-22"></a>

### 22. LookStep: Efficient Vision-Language Navigation with Linguistic Foresight and Event Driven Memory

- **年份：** 2026
- **标签：** `VLN`
- **链接：** [arXiv:2609.02350](https://arxiv.org/abs/2609.02350)

**摘要：** `VLN` 要求具身智能体在未见环境中遵循自然语言指令。近期进展多由 MLLM 驱动，但现有方法仅监督专家下一步动作，需大量数据，并依赖认知地图、累积历史帧或外部 3D 工具维持状态，计算与记忆开销高。本文提出 LookStep：统一端到端结合语言中心未来状态建模与事件驱动滚动记忆，用语言标签为每个候选动作生成粗粒度导航进度与未来状态，并自主决定是否将观测写入带语义角色的有界滚动记忆。在 `VLN-CE` 上，相同训练设定下优于现有方法，R2R-CE Val-Unseen 成功率为 49.7%，记忆效率更高、数据用量更少。

**要点：**

- **方法：** 以语言标签建模候选动作的粗粒度未来状态，并用事件驱动有界滚动记忆按语义角色写入观测。
- **贡献：** 相同训练设定下在 `VLN-CE` 上优于现有方法，R2R-CE 未见验证集成功率更高且更省记忆与数据。
- **关系：** 面向高效 `VLN` 与 MLLM，用语言中心未来状态建模，非独立 `World Model` 实验。

---

<a id="p-23"></a>

### 23. MetaWorld: Skill Transfer and Composition in a Hierarchical World Model for Grounding High-Level Instructions

- **年份：** 2026
- **标签：** `world_model`
- **链接：** [arXiv:2601.17507](https://arxiv.org/abs/2601.17507)

**摘要：** 人形机器人 loco-manipulation 受语义-物理鸿沟制约：强化学习样本效率低、模仿学习泛化差、`VLM` 存在物理不一致。本文提出层次化 `World Model` MetaWorld，通过专家策略迁移整合语义规划与物理控制：任务解耦为 `VLM` 驱动的语义层与在紧凑状态空间运行的潜动力学模型；动态专家选择与运动先验融合利用预训练多专家策略库作为可迁移知识，经两阶段框架在线适应。`VLM` 将指令映射为可执行技能，绕过符号接地。Humanoid-Bench 上在任务完成与运动连贯性上优于基于 `World Model` 的强化学习。

**要点：**

- **方法：** 层次化 `World Model` 将任务解耦为 `VLM` 语义层与紧凑潜动力学，并以动态专家选择与运动先验融合做在线适应。
- **贡献：** 用 `VLM` 将指令映射为可执行技能，Humanoid-Bench 上优于基于 `World Model` 的强化学习。
- **关系：** 层次化 `World Model` 接地高层指令，并以 `VLM` 作语义接口（非 `VLA`/`VLN` 实验）。

---

<a id="p-24"></a>

### 24. MobileVLA-R1 2.0: RL-Enhanced Reasoning for Mobile Robot Control

- **年份：** 2026
- **标签：** `agent-robot` · `VLA` · `VLN`
- **链接：** [arXiv:2609.06251](https://arxiv.org/abs/2609.06251)

**摘要：** MobileVLA-R1 2.0 用监督思维链与强化学习对齐推理到动作，再经推理条件动作解码器输出移动机器人任务级目标。在 `VLN-CE`、四足与 Unitree Go2/G1 真机上，相对 MobileVLA-R1 平均成功率提升，并改善长时程指令跟随。

**要点：**

- **方法：** 思维链对齐 + RL 增强推理，再解码为移动操作 / 导航动作。
- **贡献：** `VLN-CE` 与 G1 真机移动操作相对前作提升。
- **关系：** 推理 Agent × 移动 `VLA` / `VLN`。

---

<a id="p-25"></a>

### 25. OSCAR: Omni-Embodiment Action-Conditioned World Model for Robotics

- **年份：** 2026
- **标签：** `world_model`
- **链接：** [arXiv:2606.04463](https://arxiv.org/abs/2606.04463)

**摘要：** 本文提出 OSCAR：精确的动作条件视频 `World Model`，可跨不同机器人本体泛化并用于策略评测。现有视频 `World Model` 面临训练数据场景多样性不足、动作跟随不准、跨本体泛化差。作者以大规模标准化管线整理、过滤并去重机器人与自我中心人类数据，并以 2D 运动学骨架渲染作为可泛化到不同机械臂甚至人手的统一条件表示，在单块 GH200 上微调 Cosmos-Predict2.5-2B。相对更大模型或更多 GPU 的基线，动作跟随、外观质量与运动一致性显著提升；部署于 RoboArena 时，虚拟策略评测与真实评测显著相关。

**要点：**

- **方法：** 标准化大规模数据管线加 2D 运动学骨架渲染作为跨本体统一动作条件，微调视频 `World Model`。
- **贡献：** 提升动作跟随、外观与运动一致性，并在 RoboArena 上显示虚拟策略评测与真实评测相关。
- **关系：** 跨本体动作条件 `World Model`，用于机器人策略评测，文中未涉及 `VLA`/`VLN`。

---

<a id="p-26"></a>

### 26. PGN: Design and Implementation of a Vision-Language Navigation System Based on Pangu Multimodal Foundation Model

- **年份：** 2026
- **标签：** `intersection`
- **链接：** [arXiv:2607.17806](https://arxiv.org/abs/2607.17806)

**摘要：** `VLN` 要求智能体解释自然语言指令，并根据时序视觉观测预测动作。将多模态大语言模型适配到 `VLN` 需要视觉-语言对齐、紧凑时序输入、动作空间锚定及目标硬件上的稳定训练。本文提出基于 OpenPangu-7B 的离线动作预测系统 PGN：先以 Q-Former 与两层 MLP 对齐冻结的 EVA-ViT-G/14 与语言骨干，再以五观测窗口、随 epoch 变化的时序采样及先推理后动作格式适配专家轨迹，并更新结构 token 嵌入与 LoRA。在八张昇腾 910B 上以混合精度与 DeepSpeed ZeRO-2 训练。500 条留出专家轨迹的教师强制开环评测中，V9 的 NAM 为 62.29%、NER 为 100%，衡量离线专家动作对齐而非闭环导航成功。

**要点：**

- **方法：** 先用 Q-Former 与 MLP 对齐视觉编码器与 OpenPangu-7B，再以窗口观测、时序采样与 LoRA 适配专家导航轨迹。
- **贡献：** 在昇腾上完成离线动作预测训练，开环专家对齐指标按报告给出，并明确尚非闭环成功评测。
- **关系：** 将多模态基础模型适配 `VLN` 动作预测，文中未涉及 `World Model`。

---

<a id="p-27"></a>

### 27. PlayWorld: Learning Robot World Models from Autonomous Play

- **年份：** 2026
- **标签：** `world_model`
- **链接：** [arXiv:2603.09030](https://arxiv.org/abs/2603.09030)

**摘要：** 动作条件视频模型有望构建可直接从数据改进的通用机器人仿真器，但即便在大规模机器人数据上训练，现有 SOTA 视频模型仍难以预测操作所需的物理一致机器人-物体交互。本文提出 PlayWorld：从交互经验训练高保真视频世界仿真器的简单、可扩展、全自主管线，据称首次完全从无监督机器人自博弈学习，从而可扩展采集并捕捉长尾物理交互。多样操作任务上，其对接触丰富交互的预测优于在人类采集数据上训练的 `World Model`；细粒度失败预测与策略评测相对人类数据最高提升 40%；并支持在 `World Model` 中做强化学习，实机部署成功率提升 65%。

**要点：**

- **方法：** 全自主无监督机器人自博弈采集交互经验，训练动作条件视频世界仿真器。
- **贡献：** 接触丰富交互预测优于人类演示训练的 `World Model`，并改善失败预测、策略评测及在世界模型中的强化学习。
- **关系：** 纯 `World Model` 数据与仿真管线，服务操作策略，文中未涉及 `VLA`/`VLN`/`VLM`。

---

<a id="p-28"></a>

### 28. PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation

- **年份：** 2026
- **标签：** `world_model`
- **链接：** [arXiv:2601.03782](https://arxiv.org/abs/2601.03782)

**摘要：** 人类能从一瞥与设想的身体动作预判 3D 世界如何响应。本文提出大型预训练 3D `World Model` PointWorld：在共享 3D 空间中以 3D 点流统一状态与动作，给定一两张 RGB-D 与低层动作指令序列，预测响应这些动作的逐像素 3D 位移，从而直接条件于机器人几何并跨本体整合学习。训练数据覆盖真实与仿真开放世界操作，约 200 万条轨迹、500 小时，涵盖单臂 Franka 与双臂人形。大规模实证研究提炼骨干、动作表示与目标等设计原则。实时（0.1s）推理可嵌入 MPC；单一预训练检查点使真实 Franka 在无演示、无后训练、仅一张野外图像下完成刚体推、可变形与铰接物操作及工具使用。

**要点：**

- **方法：** 以 3D 点流在共享空间统一状态与动作，由少量 RGB-D 与低层指令预测逐像素 3D 位移。
- **贡献：** 大规模跨本体数据与系统设计研究支持实时嵌入 MPC，单检查点无演示即可在野外图像上完成多种真实操作。
- **关系：** 大规模 3D `World Model` 服务操作与 MPC，文中未涉及 `VLA`/`VLN`/`VLM`。

---

<a id="p-29"></a>

### 29. RACO: Reliability-Aware Coarse-Goal Optimization for Inspection-Oriented UAV Vision-Language Navigation

- **年份：** 2026
- **标签：** `VLN`
- **链接：** [arXiv:2608.22678](https://arxiv.org/abs/2608.22678)

**摘要：** UAV-VLN 常以到达目标评测，但面向巡检的部署要求智能体停在有效巡检区域内，并避免对视觉或语义相似干扰物的错误确认。现有粗到细策略常把局部精化前的粗目标当作可靠，而其可能漂移到似是而非的物体区域。本文提出由 CityNav/CityRefer 导出的 LG-UVI，扩展目标物体、困难干扰物、类型感知巡检区域及到达与确认诊断。RACO 将粗目标视为运行时假设，用物体级候选锚点在第一阶段前及阶段边界检查并纠正粗定位，并以尺度自适应终端精化处理近失。统一在线评测下，相对复现的 HETT 基线在 validation-unseen 与 test-unseen 上 SR 分别提高 9.53 与 7.98 个百分点，并改善巡检到达、降低错误核验风险。

**要点：**

- **方法：** 将粗目标视为运行时假设，用物体级锚点校验纠正，并以尺度自适应终端精化处理近失。
- **贡献：** 提出 LG-UVI 巡检评测设定；相对 HETT 提升未见分割 SR 并改善巡检到达、降低错误核验。
- **关系：** 面向巡检型 UAV-VLN 的粗目标可靠性，文中未涉及 `World Model` 或 `VLA`。

---

<a id="p-30"></a>

### 30. RecoverFly: A Failure-Aware Reinforcement Learning Post-Training Framework for Aerial Vision-Language Navigation

- **年份：** 2026
- **标签：** `VLN`
- **链接：** [arXiv:2608.09467](https://arxiv.org/abs/2608.09467)

**摘要：** 无人飞行器视觉语言导航（UAV-VLN）需将视觉观测与语言指令转化为复杂环境中的可靠飞行动作。端到端 UAV-VLA 虽减少对分模块感知、规划与控制的依赖，但行为克隆对闭环纠错监督有限。强化学习又受样本效率、长尾场景与策略分布偏移制约。RecoverFly 作为面向失败的 RL 后训练框架，对语法约束的自回归飞行动作做 token 级强化学习，重访未解决失败以加强纠错与样本利用，并以两阶段长尾课程与参考策略正则提升场景适应、保留已学能力。在 TravelUAV 的 seen、unseen-map、unseen-object 上取得最佳，相对 AerialVLA 成功率提升 3.12 至 8.37 个百分点，总 rollout 预算约为训练集规模的 30%。

**要点：**

- **方法：** RecoverFly 以 token 级强化学习、失败重访、两阶段长尾课程与参考策略正则对端到端 UAV-VLA 做后训练。
- **贡献：** 在 TravelUAV 的 seen、unseen-map、unseen-object 上取得最佳，并以约 30% 训练集规模的 rollout 相对 AerialVLA 提升成功率。
- **关系：** 面向 UAV-VLN 的闭环纠错与泛化，摘要未涉及 `World Model`。

---

<a id="p-31"></a>

### 31. Revisiting Topological Graphs for Macro Action based Closed-loop Reinforcement Learning of Vision Language Navigation in Continuous Environment

- **年份：** 2026
- **标签：** `VLN`
- **链接：** [arXiv:2609.03906](https://arxiv.org/abs/2609.03906)

**摘要：** 连续环境视觉语言导航（`VLN-CE`）要求智能体在未见环境中跟随自然语言指令。现有模仿学习在闭环中困难：行为克隆存在分布偏移，DAgger 在轨迹偏离后专家动作变得含糊。直接在微动作空间做强化学习则因奖励稀疏而不够样本高效。本文将 `VLN-CE` 重构为分层马尔可夫决策过程，用拓扑图将环境抽象为前沿节点上的宏动作，并以无需训练的低层控制器作为状态转移，以便压缩决策时域、使闭环强化学习可行。进而提出动作感知价值头，在动态前沿动作空间下评估状态价值，支撑基于图的 PPO。在 R2R-CE 与 RxR-CE 上取得当时最优。

**要点：**

- **方法：** 将 `VLN-CE` 建模为分层 MDP，在拓扑图前沿节点上做宏动作，并以动作感知价值头支撑图上 PPO。
- **贡献：** 压缩决策时域使闭环强化学习可行，并在 R2R-CE 与 RxR-CE 上取得当时最优。
- **关系：** 服务连续环境 `VLN` 的闭环强化学习，摘要未涉及 `World Model`。

---

<a id="p-32"></a>

### 32. RynnBrain: Open Embodied Foundation Models

- **年份：** 2026
- **标签：** `VLA` · `VLM`
- **链接：** [arXiv:2602.14979](https://arxiv.org/abs/2602.14979)

**摘要：** 具身社区缺少在真实时空动力学中统一感知、推理与规划的物理接地基础模型。RynnBrain 是开源时空基础模型，强化自我中心理解、时空定位、物理接地推理与物理感知规划；提供 2B / 8B / 30B-A3B MoE 及导航、规划、`VLA` 与空间推理等后训练变体。在 20 个具身与 8 个通用视觉基准上明显优于既有具身基础模型，并可用作可高效适应的预训练骨干。

**要点：**

- **方法：** 统一框架强化自我中心理解、时空定位、物理推理与规划，并提供多尺度与后训练变体。
- **贡献：** 在 20+8 个基准上优于既有具身基础模型，且可高效适配导航 / 规划 / `VLA`。
- **关系：** 开放具身 `VLM` 底座，后训练含 `VLA`，可供 Agent 调用。

---

<a id="p-33"></a>

### 33. Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control

- **年份：** 2026
- **标签：** `agent-robot` · `VLA`
- **链接：** [arXiv:2602.13193](https://arxiv.org/abs/2602.13193)

**摘要：** 层次化系统里 `VLM` 与 `VLA` 之间若只有自然语言任务指令，高层推理很难转向低层行为。Steerable Policies 在子任务、运动与接地像素坐标等多抽象层级的合成命令上训练 `VLA`。用学得的高层具身推理器或即插即用 `VLM`（上下文学习推理命令抽象）来控制该策略时，真机操作在泛化与长时程上优于先前具身推理 `VLA` 与 `VLM` 层次基线。

**要点：**

- **方法：** 在多抽象层级合成命令上训练可转向 `VLA`，并由 `VLM` / 具身推理器控制。
- **贡献：** 真机泛化与长时程上优于先前层次化 `VLM`–`VLA` 基线。
- **关系：** 层次化 Agent 的可转向 `VLA` 接口。

---

<a id="p-34"></a>

### 34. TANGO: Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Language-Action Model

- **年份：** 2026
- **标签：** `VLN`
- **链接：** [arXiv:2609.09158](https://arxiv.org/abs/2609.09158)

**摘要：** 本文研究人形机器人在杂乱室内的导航。不同于二维路径规划，杂乱场景中的人形穿越需要几何感知的全身适应，包括协调手臂放置、躯干调整与步态调制。TANGO 是首个面向语言条件人形穿越的全身视觉语言导航框架：由自然语言指令与自我中心 RGB 直接预测 29-DoF 关节空间动作。训练完全在仿真中进行，借助全局路径规划、运动学全身运动生成、障碍感知运动编辑与强化学习跟踪合成无碰撞行为。仿真中取得视觉语言导航最优，并在需协商障碍的场景上优于强模块化基线；在 Unitree G1 上零样本部署，无需真实导航数据即可实现语言引导穿越。

**要点：**

- **方法：** TANGO 由语言与自我中心 RGB 直接预测 29-DoF 关节动作，并在仿真中用规划、运动生成、障碍编辑与强化学习跟踪合成监督。
- **贡献：** 仿真中取得视觉语言导航最优并优于模块化基线，且在 Unitree G1 上零样本部署到真实杂乱场景。
- **关系：** 为人形 `VLN` 提供全身视觉语言动作策略，摘要未涉及 `World Model`。

---

<a id="p-35"></a>

### 35. TiPToP: A Modular Open-Vocabulary Robot Manipulation System That Plans

- **年份：** 2026
- **标签：** `agent-robot`
- **链接：** [arXiv:2603.09971](https://arxiv.org/abs/2603.09971)

**摘要：** TiPToP 是模块化开放词汇操作规划系统：把开放词汇接地与经典任务—运动规划组合，并作为可调用后端供更高层物理 Agent 使用。Physical Agency 一文将其当作冻结工具而非整系统。

**要点：**

- **方法：** 开放词汇感知与经典 TAMP 模块化组合。
- **贡献：** 提供可被 Agent 调用的规划后端。
- **关系：** 规划工具 Agent 后端，衔接语言与运动规划。

---

<a id="p-36"></a>

### 36. Verification of the Implicit World Model in a Generative Model via Adversarial Sequences

- **年份：** 2026
- **标签：** `world_model`
- **链接：** [arXiv:2602.05903](https://arxiv.org/abs/2602.05903)

**摘要：** 生成式序列模型通常在自然或形式语言样本上训练，关键问题是基于样本的训练能否捕捉这些语言的真实结构，即所谓 `world model`。理论表明至多可期望健全性——生成合法序列，但不一定覆盖全部。本文以国际象棋为对象，用对抗序列生成检验模型是否健全：对手构造合法序列以迫使模型预测非法着法，并分析失败模式与训练选择。在随机与高质量对局、多种配方的大量象棋模型上评估，发现无一健全，但部分技术与数据选择能显著改善健全性。棋盘状态探测还表明，多数模型中提取的棋盘状态对下一 token 预测并无因果作用。

**要点：**

- **方法：** 以国际象棋为规则明确的 `world model`，用对抗序列生成迫使模型预测非法着法以检验健全性。
- **贡献：** 所评象棋序列模型均不健全，但部分训练配方与数据选择能显著改善健全性；棋盘探测多无因果作用。
- **关系：** 检验生成模型是否内隐习得 `world model`，属 `World Model` 验证，不涉及 `VLA`/`VLN`/`VLM`。

---

<a id="p-37"></a>

### 37. VLA-Precision: Asymmetric Co-Bootstrapping for Efficient Real-World Online RL of Vision-Language-Action Models

- **年份：** 2026
- **标签：** `VLA`
- **链接：** [arXiv:2609.04355](https://arxiv.org/abs/2609.04355)

**摘要：** `VLA`-Precision 用非对称共引导做高效真机在线强化学习，缓解不可靠价值信号与大 `VLA` 吞吐瓶颈。在四类九项高精度化学任务、四种本体上，平均成功率 98.3%，并报告显著吞吐提升。

**要点：**

- **方法：** 非对称共引导在线 RL + 流式闭环架构微调大 `VLA`。
- **贡献：** 高精度真机任务高成功，并大幅提高在线吞吐。
- **关系：** `VLA` 在线改进；可被精度敏感 Agent 当低层。

---

<a id="p-38"></a>

### 38. What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents

- **年份：** 2026
- **标签：** `agent-robot` · `VLA`
- **链接：** [arXiv:2606.10267](https://arxiv.org/abs/2606.10267)

**摘要：** 该文系统研究层次化 `VLA` Agent：高层 `VLM` 规划器分解任务，低层 `VLA` 执行。在统一 options 框架下比较规划器、控制器、切换与记忆设计，并在仿真与真实 ALOHA 上表明原则化层次显著优于平坦 `VLA` 或朴素层次。

**要点：**

- **方法：** 在 options 框架下系统消融 Hi-VLA 的规划器、控制器与接口。
- **贡献：** 给出可执行的层次化 `VLA` Agent 设计原则，并在真机验证。
- **关系：** Agent 控制机器人的 2026 年系统研究，直接对照 `VLA`。

---

<a id="p-39"></a>

### 39. World Action Models are Zero-shot Policies

- **年份：** 2026
- **标签：** `world_model` · `VLA` · `intersection`
- **链接：** [arXiv:2602.15922](https://arxiv.org/abs/2602.15922)

**摘要：** World Action Models are Zero-shot Policies 主张世界—动作模型本身即可作为零样本策略：在学得的动作条件动力学上直接解码控制，而无需单独策略头。

**要点：**

- **方法：** 把世界—动作模型直接当作零样本策略。
- **贡献：** 模糊 `WM` 与策略的界限，强调动作条件预测即可控制。
- **关系：** `WM` 即策略，高层 Agent 仍可提供目标。

---

<a id="p-40"></a>

### 40. World Model for Robot Learning: A Comprehensive Survey

- **年份：** 2026
- **标签：** `VLM` · `world_model`
- **链接：** [arXiv:2605.00080](https://arxiv.org/abs/2605.00080)

**摘要：** `World Model` 是动作条件下环境如何演化的预测表示，已成为机器人学习的核心，支撑策略学习、规划、仿真、评估与数据生成，并随基础模型与大规模视频生成迅速发展。文献在架构、功能角色与具身应用上仍较分散。本文从机器人学习视角综述：考察 `World Model` 如何与策略耦合、如何作为强化学习与评估的学习仿真器，以及机器人视频 `World Model` 如何从想象生成走向可控、结构化与基础模型尺度；并连接到导航与自动驾驶，总结数据集、基准与评估协议。综述澄清范式与应用，指出挑战与未来方向，并将持续更新配套 GitHub 仓库。

**要点：**

- **方法：** 从机器人学习视角系统综述 `World Model`，覆盖与策略耦合、学习仿真器及视频 `World Model` 的发展脉络。
- **贡献：** 澄清关键范式与应用，总结导航与自动驾驶相关数据与评估，并维护持续更新的资源库。
- **关系：** 为 `World Model` 与机器人策略、导航交叉提供综述框架，本身不提出新实验。

---

<a id="p-41"></a>

### 41. World Models for Robotic Manipulation: A Survey

- **年份：** 2026
- **标签：** `intersection` · `world_model`
- **链接：** [arXiv:2606.00113](https://arxiv.org/abs/2606.00113)

**摘要：** 机器人操作依赖在执行前预判动作如何改变物体、接触与场景几何。学习到的 `World Model` 预测干预下的任务相关未来，但该术语已涵盖潜在动力学、动作条件视频生成、三维与四维场景预测、物理仿真器及 `VLA` 内部预测模块。本文以预测何种表示、如何连接动作、何时用于学习流水线组织综述，将 `World Model` 定义为动作条件预测系统，并与感知、逆模型、策略、奖励与价值函数区分。归纳五类表示与功能分类，覆盖预训练、后训练与推理适应，回顾 34 个操作数据集并综合评估协议。综述表明 `World Model` 正演变为预测基础设施，并指出接触建模、幻觉控制、动作对齐与闭环评测等挑战。

**要点：**

- **方法：** 按未来表示、动作连接与使用时机三问综述操作域 `World Model`，并将其定义为动作条件预测系统。
- **贡献：** 归纳五类表示与功能分类，回顾 34 个操作数据集并综合评估协议，指出接触、幻觉、对齐与闭环评测挑战。
- **关系：** 明确涵盖 `VLA` 内部预测模块，说明 `World Model` 如何作为操作学习的预测基础设施。

---

<a id="p-42"></a>

### 42. World-Gymnast: Training Robots with Reinforcement Learning in a World Model

- **年份：** 2026
- **标签：** `world_model`
- **链接：** [arXiv:2602.02454](https://arxiv.org/abs/2602.02454)

**摘要：** 与物理世界交互的成本制约机器人学习：监督微调受专家数据量限制，软件仿真器则有操作域的仿真到真实差距。本文提出 World-Gymnast：在动作条件视频 `World Model` 中展开 `VLA` 策略，并用 `VLM` 对轨迹打分以做强化学习微调。在 Bridge 机器人上，相对监督微调最高约 18 倍、相对软件仿真器最高约 2 倍。还展示在多样语言指令与新场景上训练、在新场景做测试时训练，以及在线迭代改进 `World Model` 与策略。结果表明，在云端学习 `World Model` 并训练策略或有助于弥合仅能完成演示与可在家庭中工作的机器人之间的差距。

**要点：**

- **方法：** World-Gymnast 在动作条件视频 `World Model` 中对 `VLA` 做强化学习微调，并用 `VLM` 奖励轨迹。
- **贡献：** 在 Bridge 上相对监督微调与软件仿真器提升真实机器人表现，并展示多样指令、新场景与在线迭代改进。
- **关系：** 将 `World Model` 作为 `VLA` 的强化学习训练场，并以 `VLM` 提供奖励，属 `WM`×`VLA`/`VLM` 交叉。

---

<a id="p-43"></a>

### 43. World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis

- **年份：** 2026
- **标签：** `world_model` · `VLA` · `intersection`
- **链接：** [arXiv:2606.05979](https://arxiv.org/abs/2606.05979)

**摘要：** World-Language-Action（WLA）用自回归 Transformer 统一世界建模、语言推理与动作合成：高层意图以文本子任务形式引导动力学与动作，相对纯 `VLA` 更能利用无动作标注的跨本体视频。原型在仿真与真机多任务、长时程上报告强成功。

**要点：**

- **方法：** 自回归骨干统一下一状态预测、语言子任务与动作合成。
- **贡献：** 提出 WLA 家族，连接 `WM`、语言推理与控制。
- **关系：** 显式交叉 `World Model`、语言 Agent 与 `VLA`。

---

<a id="p-44"></a>

### 44. π₀.₇: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities

- **年份：** 2026
- **标签：** `VLA`
- **链接：** [arXiv:2604.15483](https://arxiv.org/abs/2604.15483)

**摘要：** π₀.₇ 是可转向的通才机器人基础模型，强调涌现能力与更丰富的命令结构，供层次化控制与具身推理使用。

**要点：**

- **方法：** 可转向通才机器人基础模型，承接层次化命令。
- **贡献：** 展示 π 系列在转向与涌现能力上的后续。
- **关系：** `VLA` 底座，为 Agent 编排提供可转向接口。

---

<a id="p-45"></a>

### 45. τ₀-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation

- **年份：** 2026
- **标签：** `intersection`
- **链接：** [arXiv:2608.16885](https://arxiv.org/abs/2608.16885)

**摘要：** 长时程机器人操作既要可靠执行单项技能，也要在延展任务中连贯编排。多数层次化 `VLA` 仅用单次前向完成决策，难以把额外算力投向困难或关键选择。本文提出 τ₀-VLA：将高层子任务生成表述为可随算力扩展的推理，并由 `World Model` 引导测试时计算。高层策略利用执行记忆生成子任务，必要时搜索备选后再提交；低层策略在多种本体上执行。模型在 40115 小时异构真实数据上多模态共训。域内与分布偏移下，增加测试时计算显著提升下一子任务预测精度，并转化为长时程操作闭环成功率提高。

**要点：**

- **方法：** 以 `World Model` 引导测试时计算，将层次化 `VLA` 的高层子任务生成作为可扩展推理，必要时搜索备选后再提交。
- **贡献：** 异构真实数据多模态共训后，增加测试时计算提升下一子任务预测，并转化为长时程操作闭环成功。
- **关系：** 直接交叉 `World Model` 与层次化 `VLA`，用世界模型指导测试时决策而非单次前向。

---

## 2025 年

共 69 篇。先扫目录，再下翻卡片。

- [46. A Comprehensive Survey on World Models for Embodied AI](#p-46)  `world_model`
- [47. A Survey on Efficient Vision-Language-Action Models](#p-47)  `VLA`
- [48. AdaWM: Adaptive World Model based Planning for Autonomous Driving](#p-48)  `world_model`
- [49. AdaWorld: Learning Adaptable World Models with Latent Actions](#p-49)  `world_model`
- [50. An Anatomy of Vision-Language-Action Models: From Modules to Milestones and Challenges](#p-50)  `VLA`
- [51. Back to the Features: DINO as a Foundation for Video World Models](#p-51)  `world_model`
- [52. Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos](#p-52)  `VLA`
- [53. BitVLA: 1-bit Vision-Language-Action Models for Robotics Manipulation](#p-53)  `VLA`
- [54. BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models](#p-54)  `VLA`
- [55. ChatVLA: Unified Multimodal Understanding and Robot Control with Vision-Language-Action Model](#p-55)  `VLA`
- [56. CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification](#p-56)  `intersection`
- [57. Cosmos World Foundation Model Platform for Physical AI](#p-57)  `world_model`
- [58. Ctrl-World: A Controllable Generative World Model for Robot Manipulation](#p-58)  `VLM` · `world_model`
- [59. EdgeVLA: Efficient Vision-Language-Action Models](#p-59)  `intersection`
- [60. Emergent World Representations in OpenVLA](#p-60)  `intersection`
- [61. Empowering Multi-Robot Cooperation via Sequential World Models](#p-61)  `VLM`
- [62. Epona: Autoregressive Diffusion World Model for Autonomous Driving](#p-62)  `world_model`
- [63. EvoVLA: Self-Evolving Vision-Language-Action Model](#p-63)  `VLA`
- [64. Explainable Adversarial-Robust Vision-Language-Action Model for Robotic Manipulation](#p-64)  `VLA`
- [65. FAST: Efficient Action Tokenization for Vision-Language-Action Models](#p-65)  `VLA`
- [66. FCRF: Flexible Constructivism Reflection for Long-Horizon Robotic Task Planning with Large Language Models](#p-66)  `agent-robot` · `llm-agent`
- [67. Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](#p-67)  `intersection`
- [68. FlowDreamer: A RGB-D World Model with Flow-based Motion Representations for Robot Manipulation](#p-68)  `world_model`
- [69. Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models](#p-69)  `intersection`
- [70. GAIA-2: A Controllable Multi-View Generative World Model for Autonomous Driving](#p-70)  `world_model`
- [71. Gemini Robotics: Bringing AI into the Physical World](#p-71)  `VLA` · `VLM`
- [72. GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](#p-72)  `VLA`
- [73. GWM: Towards Scalable Gaussian World Models for Robotic Manipulation](#p-73)  `VLM` · `world_model`
- [74. Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](#p-74)  `agent-robot` · `VLA`
- [75. Improving Transformer World Models for Data-Efficient RL](#p-75)  `world_model`
- [76. Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling](#p-76)  `VLM` · `world_model`
- [77. InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation](#p-77)  `intersection`
- [78. Kinodynamic Motion Planning for Mobile Robot Navigation across Inconsistent World Models](#p-78)  `VLM`
- [79. LaDi-WM: A Latent Diffusion-based World Model for Predictive Manipulation](#p-79)  `world_model`
- [80. LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction](#p-80)  `VLA`
- [81. LLM+MAP: Bimanual Robot Task Planning using Large Language Models and Planning Domain Definition Language](#p-81)  `agent-robot` · `llm-agent`
- [82. Logic-Guided Socially-aware Robot Navigation World Model](#p-82)  `VLM`
- [83. LUMOS: Language-Conditioned Imitation Learning with World Models](#p-83)  `world_model`
- [84. mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs](#p-84)  `VLA` · `world_model` · `intersection`
- [85. MineWorld: a Real-Time and Open-Source Interactive World Model on Minecraft](#p-85)  `world_model`
- [86. Motus: A Unified Latent Action World Model](#p-86)  `world_model` · `VLA` · `intersection`
- [87. Optimus-2: Multimodal Minecraft Agent with Goal-Observation-Action Conditioned Policy](#p-87)  `agent-robot`
- [88. Phoenix: A Motion-based Self-Reflection Framework for Fine-grained Robotic Action Correction](#p-88)  `agent-robot` · `llm-agent`
- [89. Pure Vision Language Action (VLA) Models: A Comprehensive Survey](#p-89)  `VLA`
- [90. REFLEX: Metacognitive Reasoning for Reflective Zero-Shot Robotic Planning with Large Language Models](#p-90)  `agent-robot` · `llm-agent`
- [91. RLVR-World: Training World Models with Reinforcement Learning](#p-91)  `world_model`
- [92. RoboFlamingo-Plus: Fusion of Depth and RGB Perception with Vision-Language Models for Enhanced Robotic Manipulation](#p-92)  `VLM`
- [93. RoboHorizon: An LLM-Assisted Multi-View World Model for Long-Horizon Robotic Manipulation](#p-93)  `VLM` · `world_model`
- [94. RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models](#p-94)  `agent-robot` · `VLA`
- [95. Robot Learning from a Physical World Model](#p-95)  `VLM`
- [96. Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics](#p-96)  `world_model`
- [97. RobotxR1: Enabling Embodied Robotic Intelligence on Large Language Models through Closed-Loop Reinforcement Learning](#p-97)  `agent-robot` · `llm-agent`
- [98. Safe LLM-Controlled Robots with Formal Guarantees via Reachability Analysis](#p-98)  `agent-robot` · `llm-agent`
- [99. Safety Guardrails for LLM-Enabled Robots](#p-99)  `agent-robot` · `llm-agent`
- [100. SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](#p-100)  `VLA`
- [101. SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model](#p-101)  `VLA`
- [102. Survey on Vision-Language-Action Models](#p-102)  `VLA`
- [103. TesserAct: Learning 4D Embodied World Models](#p-103)  `world_model`
- [104. Unified Vision-Language-Action Model](#p-104)  `VLA`
- [105. Universal Actions for Enhanced Embodied Foundation Models](#p-105)  `VLA`
- [106. UniVLA: Learning to Act Anywhere with Task-centric Latent Actions](#p-106)  `VLA`
- [107. V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](#p-107)  `world_model`
- [108. Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges](#p-108)  `intersection`
- [109. Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications](#p-109)  `VLA`
- [110. Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning](#p-110)  `intersection`
- [111. VOTE: Vision-Language-Action Optimization with Trajectory Ensemble Voting](#p-111)  `VLA`
- [112. WorldVLA: Towards Autoregressive Action World Model](#p-112)  `world_model`
- [113. X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model](#p-113)  `VLA`
- [114. π₀.₅: a Vision-Language-Action Model with Open-World Generalization](#p-114)  `VLA`

<a id="p-46"></a>

### 46. A Comprehensive Survey on World Models for Embodied AI

- **年份：** 2025
- **标签：** `world_model`
- **链接：** [arXiv:2510.16732](https://arxiv.org/abs/2510.16732)

**摘要：** 具身智能需要智能体感知、行动并预判动作如何改变未来世界状态。`World Model` 作为捕捉环境动力学的内部仿真器，支持前向与反事实展开。本综述提出具身人工智能中 `World Model` 的统一框架：形式化问题与学习目标，并沿功能（决策耦合相对通用）、时间建模（序列仿真推断相对全局差分预测）、空间表示（全局潜向量、token 特征序列、空间潜网格、分解渲染）三轴分类。系统整理机器人、自动驾驶与通用视频的数据与指标，并定量比较前沿模型。开放挑战包括统一数据稀缺、需超越像素保真的物理一致性评估、性能与实时控制算力权衡，以及长时程一致性与误差累积。

**要点：**

- **方法：** 提出具身人工智能 `World Model` 的统一框架，沿功能、时间建模与空间表示三轴分类。
- **贡献：** 整理跨领域数据与指标并定量比较前沿模型，提炼物理一致性评估、实时算力与长时程误差等挑战。
- **关系：** 属 `World Model` 综述，摘要未涉及 `VLA`/`VLN`/`VLM` 新实验。

---

<a id="p-47"></a>

### 47. A Survey on Efficient Vision-Language-Action Models

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2510.24795](https://arxiv.org/abs/2510.24795)

**摘要：** 视觉语言动作模型（`VLA`）旨在连接数字知识与物理交互，但基础 `VLA` 受大规模架构的高昂算力与数据需求制约。近期工作关注提升效率，却缺少统一框架。本综述首次沿模型—训练—数据全流水线全面评述高效 `VLA`，将技术归为三柱：高效模型设计（架构与压缩）、高效训练（降低学习算力）、高效数据采集（缓解机器人数据获取与利用瓶颈）。在此框架下批判性回顾前沿方法，总结代表性应用、关键挑战与未来路线图，并维护持续更新的项目页。

**要点：**

- **方法：** 沿模型—训练—数据全流水线综述高效 `VLA`，归为高效模型设计、高效训练与高效数据采集三柱。
- **贡献：** 整合分散的效率进展，总结应用、挑战与路线图，并维护持续更新的项目页。
- **关系：** 服务 `VLA` 部署与训练效率，摘要未涉及 `World Model`。

---

<a id="p-48"></a>

### 48. AdaWM: Adaptive World Model based Planning for Autonomous Driving

- **年份：** 2025
- **标签：** `world_model`
- **链接：** [arXiv:2501.13072](https://arxiv.org/abs/2501.13072)

**摘要：** 基于 `World Model` 的强化学习为自动驾驶提供先学潜在动力学再用其训练规划策略的路径。预训练—微调常用于加速，但在新任务在线交互中朴素初始化可能导致性能剧降。作者识别两大根因：规划策略不匹配与动力学模型不匹配，均源于分布偏移，且微调策略的选择至关重要。据此提出 AdaWM：先量化不匹配以指导微调，再以低秩更新按需对齐策略或模型。在具有挑战性的 CARLA 驾驶任务上，AdaWM 显著改善微调，使规划更稳健高效。

**要点：**

- **方法：** AdaWM 先量化规划策略与动力学模型的不匹配，再以低秩更新按需微调策略或 `World Model`。
- **贡献：** 在 CARLA 驾驶任务上显著改善预训练后的在线微调，使规划更稳健高效。
- **关系：** 属自动驾驶中的 `World Model` 规划，摘要未涉及 `VLA`/`VLN`/`VLM`。

---

<a id="p-49"></a>

### 49. AdaWorld: Learning Adaptable World Models with Latent Actions

- **年份：** 2025
- **标签：** `world_model`
- **链接：** [arXiv:2503.18938](https://arxiv.org/abs/2503.18938)

**摘要：** `World Model` 旨在学习受动作控制的未来预测，对智能体发展至关重要。多数现有方法依赖大量动作标注与昂贵训练，难以通过有限交互适应动作异构的新环境。AdaWorld 在预训练中纳入动作信息：以自监督从视频提取潜在动作，捕捉帧间最关键转移，并训练条件于这些潜在动作的自回归 `World Model`。该范式使模型高度可适应，即便交互与微调有限也能高效迁移并学习新动作。跨多种环境的实验表明，AdaWorld 在仿真质量与视觉规划上均更优。

**要点：**

- **方法：** AdaWorld 自监督从视频提取潜在动作，并训练条件于潜在动作的自回归 `World Model`。
- **贡献：** 在有限交互与微调下实现新环境、异构动作的高效适应，并提升仿真质量与视觉规划。
- **关系：** 属可适应 `World Model`，摘要未涉及 `VLA`/`VLN`/`VLM`。

---

<a id="p-50"></a>

### 50. An Anatomy of Vision-Language-Action Models: From Modules to Milestones and Challenges

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2512.11362](https://arxiv.org/abs/2512.11362)

**摘要：** 视觉语言动作（`VLA`）模型使机器人理解指令并与物理世界交互，模型与数据迅速增长。本综述按研究者学习路径组织：从任意 `VLA` 的基本模块，经关键里程碑，再深入近期前沿的核心挑战。主要贡献是拆解五大挑战：表示、执行、泛化、安全、数据集与评估，对应通才智能体从感知—动作环、跨本体与环境扩展，到可信部署并由数据基础设施支撑的路线。对每一挑战回顾现有方法并指出未来机会，兼作新手指南与资深路线图，并维护持续更新的项目页。

**要点：**

- **方法：** 按模块、里程碑与挑战组织 `VLA` 综述，并拆解表示、执行、泛化、安全、数据集与评估五大问题。
- **贡献：** 为通才智能体从感知—动作环到可信部署提供结构化路线图，并维护持续更新的项目页。
- **关系：** 服务 `VLA` 研究导航，摘要未涉及 `World Model`。

---

<a id="p-51"></a>

### 51. Back to the Features: DINO as a Foundation for Video World Models

- **年份：** 2025
- **标签：** `world_model`
- **链接：** [arXiv:2507.19468](https://arxiv.org/abs/2507.19468)

**摘要：** 本文提出 DINO-world，一个在 DINOv2 潜空间中预测未来帧的强通用视频 `World Model`。它借助预训练图像编码器，并在大规模未策展视频上训练未来预测器，从而学习驾驶、室内场景到仿真环境等多样场景的时间动力学。DINO-world 在分割与深度预测等视频预测基准上优于先前模型，并展现对直觉物理的较强理解。还可在观测—动作轨迹上微调预测器；得到的动作条件 `World Model` 能在潜空间仿真候选轨迹以用于规划。

**要点：**

- **方法：** DINO-world 在 DINOv2 潜空间预测未来帧，并可在观测—动作轨迹上微调为动作条件 `World Model`。
- **贡献：** 在分割与深度等视频预测基准上优于先前模型，并展现直觉物理理解与潜空间规划能力。
- **关系：** 属视频 `World Model` 与规划，摘要未涉及 `VLA`/`VLN`/`VLM`。

---

<a id="p-52"></a>

### 52. Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2507.15597](https://arxiv.org/abs/2507.15597)

**摘要：** Being-H0 从大规模人类视频做视觉—语言—动作预训练，把自我中心人类行为迁到机器人策略，降低对机器人轨迹的依赖。

**要点：**

- **方法：** 大规模人类视频上的 `VLA` 预训练。
- **贡献：** 用人类视频补充机器人数据以预训练控制。
- **关系：** 人类视频 × `VLA`，含隐式动作 / 世界预测。

---

<a id="p-53"></a>

### 53. BitVLA: 1-bit Vision-Language-Action Models for Robotics Manipulation

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2506.07530](https://arxiv.org/abs/2506.07530)

**摘要：** 在边缘设备部署强大 `VLA` 受其巨大规模限制。本文从部署导向出发，通过模型设计与优化追求效率，而非仅依赖事后压缩。BitVLA 是面向机器人操作的原生 1-bit `VLA`，全部参数为三元取值 {-1,0,1}，基于公开的 1-bit 大语言模型 BitNet b1.58 2B4T。为降低视觉骨干显存，提出 Quantize-then-Distill：将全精度视觉编码器压缩为 1.58-bit 权重，并由全精度教师引导表示对齐。在仿真基准与真实任务上匹配全精度 OpenVLA-OFT，同时模型显存降低 11.0 倍、端到端延迟降低 4.4 倍。

**要点：**

- **方法：** BitVLA 以原生 1-bit 三元参数训练操作策略，并用 Quantize-then-Distill 压缩视觉编码器。
- **贡献：** 在仿真与真实任务上匹配 OpenVLA-OFT，同时显存降低 11.0 倍、端到端延迟降低 4.4 倍。
- **关系：** 面向边缘部署的高效 `VLA`，摘要未涉及 `World Model`。

---

<a id="p-54"></a>

### 54. BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2512.11769](https://arxiv.org/abs/2512.11769)

**摘要：** `VLA` 能实现出色的零样本操作，但其推理栈对网页演示或消费级 GPU 上的高频控制往往过重。BLURR 是可插入现有 `VLA` 控制器的轻量推理包装，无需重训或更改检查点。以 pi-zero 为实例，它保留原观测接口，并结合指令前缀键值缓存、混合精度与单步展开调度以降低逐步计算。在基于 SimplerEnv 的评估中，成功率与原控制器相当，同时显著降低有效浮点运算与墙钟延迟。作者还构建可实时切换控制器与推理选项的交互网页演示，凸显其在紧计算预算下部署现代 `VLA` 的实用性。

**要点：**

- **方法：** BLURR 作为免重训推理包装，结合指令前缀键值缓存、混合精度与单步展开加速现有 `VLA`。
- **贡献：** 在 SimplerEnv 上保持相当成功率并降低浮点运算与延迟，并提供可交互网页演示。
- **关系：** 服务 `VLA` 低资源推理部署，摘要未涉及 `World Model`。

---

<a id="p-55"></a>

### 55. ChatVLA: Unified Multimodal Understanding and Robot Control with Vision-Language-Action Model

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2502.14420](https://arxiv.org/abs/2502.14420)

**摘要：** 人类具有感知、理解并与物理世界交互的统一认知。对现有 `VLA` 训练范式的分析揭示两大挑战：虚假遗忘（机器人训练覆盖视觉—文本对齐）与任务干扰（控制与理解联合训练时相互损害）。ChatVLA 采用分阶段对齐训练，在掌握控制后再增量融入多模态数据，并以 Mixture-of-Experts 降低任务干扰。它在视觉问答上具竞争力，多模态理解基准显著优于当时 `VLA` 方法：MMMU 约为六倍，MMStar 为 47.2%，且设计比 ECoT 更省参数；并在 25 项真实操作任务上优于 OpenVLA 等。

**要点：**

- **方法：** ChatVLA 用分阶段对齐训练与 Mixture-of-Experts 缓解虚假遗忘与控制—理解任务干扰。
- **贡献：** 多模态理解显著优于当时 `VLA` 方法，并在 25 项真实操作任务上优于 OpenVLA 等。
- **关系：** 统一 `VLA` 的多模态理解与机器人控制，摘要未涉及 `World Model`。

---

<a id="p-56"></a>

### 56. CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification

- **年份：** 2025
- **标签：** `intersection`
- **链接：** [arXiv:2508.21046](https://arxiv.org/abs/2508.21046)

**摘要：** 基于预训练 `VLM` 的 `VLA` 需要大量后训练，算力开销限制可扩展性。CogVLA 以指令驱动路由与稀疏化提升效率与性能，采用三阶段架构：EFA-Routing 将指令注入视觉编码器，聚合压缩双流视觉标记；LFP-Routing 向语言模型引入动作意图并剪除无关视觉接地标记；CAtten 结合因果视觉—语言注意力与双向动作并行解码。在 LIBERO 与真实机器人任务上分别取得 97.4% 与 70.0% 成功率，相对 OpenVLA 训练成本降低 2.5 倍、推理延迟降低 2.8 倍。

**要点：**

- **方法：** CogVLA 以 EFA-Routing、LFP-Routing 与 CAtten 做指令驱动路由与稀疏化。
- **贡献：** 在 LIBERO 与真实任务上分别取得 97.4% 与 70.0% 成功率，相对 OpenVLA 降低训练成本与推理延迟。
- **关系：** 在预训练 `VLM` 上构建更高效 `VLA`，摘要未涉及 `World Model`。

---

<a id="p-57"></a>

### 57. Cosmos World Foundation Model Platform for Physical AI

- **年份：** 2025
- **标签：** `world_model`
- **链接：** [arXiv:2501.03575](https://arxiv.org/abs/2501.03575)

**摘要：** NVIDIA Cosmos 世界基础模型平台面向物理人工智能，提供可微调的视频世界模型、数据与工具。本包 OSS 已收录 cosmos / predict 仓库，此处补平台论文卡片。

**要点：**

- **方法：** 开放世界基础模型平台，支持视频预测与物理 AI 微调。
- **贡献：** 为机器人与驾驶等提供可微调的世界模型基础设施。
- **关系：** `World Model` 平台；可被策略或 Agent 当想象器调用。

---

<a id="p-58"></a>

### 58. Ctrl-World: A Controllable Generative World Model for Robot Manipulation

- **年份：** 2025
- **标签：** `VLM` · `world_model`
- **链接：** [arXiv:2510.10125](https://arxiv.org/abs/2510.10125)

**摘要：** 通才机器人策略已能执行广泛操作技能，但评估并改进其对陌生物体与指令的能力仍难：真实展开与带专家标注的纠错数据都缓慢昂贵。`World Model` 可在想象空间中展开策略，但需支持多视角预测、细粒度动作控制与长时程一致交互。本文提出可控多视角 `World Model`：以位姿条件记忆检索保持长时程一致性，并以帧级动作条件实现精确控制。在 DROID（95k 条轨迹、564 个场景）上训练，可在新场景与新相机位下生成逾 20 秒时空一致轨迹。无需真实展开即可准确排序策略表现；在想象中合成成功轨迹做监督微调，使策略成功率提升 44.7%。

**要点：**

- **方法：** Ctrl-World 以位姿条件记忆检索与帧级动作条件构建可控多视角 `World Model`。
- **贡献：** 在 DROID 上生成逾 20 秒一致轨迹，无需真实展开即可排序策略，并用想象成功轨迹将成功率提升 44.7%。
- **关系：** 用 `World Model` 评估并改进通才机器人策略的指令跟随，摘要未另做 `VLA`/`VLN`/`VLM` 实验。

---

<a id="p-59"></a>

### 59. EdgeVLA: Efficient Vision-Language-Action Models

- **年份：** 2025
- **标签：** `intersection`
- **链接：** [arXiv:2507.14049](https://arxiv.org/abs/2507.14049)

**摘要：** `VLM` 有望缓解机器人数据稀缺并支撑可泛化视觉运动策略，但如 OpenVLA 等大规模模型难以部署在资源受限的移动操作平台。Edge `VLA`（EVLA）旨在显著提升 `VLA` 推理速度，在保持表示能力的同时实现边缘设备实时性能。两点创新：取消末端执行器位置预测的自回归要求，推理加速约 7 倍；利用小语言模型（SLM），以更低算力获得与更大模型相当的训练表现。早期结果显示 EVLA 训练特性与 OpenVLA 相当，同时推理速度与显存效率有实质提升。

**要点：**

- **方法：** EVLA 取消末端位置预测的自回归约束，并改用小语言模型以加速 `VLA` 推理。
- **贡献：** 相对自回归设置推理约加速 7 倍，早期结果显示训练特性与 OpenVLA 相当且更省显存。
- **关系：** 把 `VLM`/`VLA` 压到边缘实时控制，摘要未涉及 `World Model`。

---

<a id="p-60"></a>

### 60. Emergent World Representations in OpenVLA

- **年份：** 2025
- **标签：** `intersection`
- **链接：** [arXiv:2509.24559](https://arxiv.org/abs/2509.24559)

**摘要：** 以策略强化学习训练的 `VLA` 能编码复杂行为而不显式建模环境动力学，但其是否隐式学习 `World Model` 仍不清楚。本文对状态表示做嵌入算术，以探测 OpenVLA 是否包含状态转移的潜在知识：测量连续环境状态嵌入之差，并检验该转移向量能否从中间激活中恢复。在各层激活上训练线性与非线性探针，发现对状态转移的预测能力在统计上显著超过嵌入基线，表明 OpenVLA 编码了内部 `World Model` 而非探针本身学会转移。更早检查点显示该 `World Model` 随训练进展出现。并概述用稀疏自编码器分析该模型的流水线。

**要点：**

- **方法：** 对 OpenVLA 状态嵌入做算术，并用线性与非线性探针从中间激活恢复状态转移向量。
- **贡献：** 探针预测显著超过嵌入基线，表明 OpenVLA 编码内部 `World Model`，且该能力随训练出现。
- **关系：** 直接检验 `VLA` 是否涌现 `World Model`，属 `WM`×`VLA` 交叉。

---

<a id="p-61"></a>

### 61. Empowering Multi-Robot Cooperation via Sequential World Models

- **年份：** 2025
- **标签：** `VLM`
- **链接：** [arXiv:2509.13095](https://arxiv.org/abs/2509.13095)

**摘要：** 基于模型的强化学习因样本效率与规划能力在机器人中取得成功，但扩展到物理多机器人合作因联合动力学复杂而困难。Sequential `World Model`（SeqWM）将序列范式引入多机器人 MBRL：用独立的自回归智能体级 `World Model` 表示联合动力学，每个智能体基于前驱预测生成未来轨迹并规划动作，从而降低建模复杂度并通过显式意图共享促进合作。在 Bi-DexHands 与 Multi-Quadruped 上优于当时基于模型与无模型基线，并展现预测适应、时间对齐与角色分工；还已部署到实体四足机器人。

**要点：**

- **方法：** SeqWM 用独立自回归的智能体级 `World Model` 表示联合动力学，并按前驱预测顺序规划。
- **贡献：** 在 Bi-DexHands 与 Multi-Quadruped 上优于当时基线，展现预测适应、时间对齐与角色分工，并部署到实体四足。
- **关系：** 将序列化 `World Model` 用于多机器人合作，摘要未涉及 `VLA`/`VLN`/`VLM`。

---

<a id="p-62"></a>

### 62. Epona: Autoregressive Diffusion World Model for Autonomous Driving

- **年份：** 2025
- **标签：** `world_model`
- **链接：** [arXiv:2506.24113](https://arxiv.org/abs/2506.24113)

**摘要：** 扩散模型在视频生成上视觉质量出色，适合自动驾驶 `World Model`，但现有视频扩散 `World Model` 难以灵活长度、长时程预测并整合轨迹规划，因其对固定长度帧序列做全局联合分布建模。Epona 是自回归扩散 `World Model`：解耦时空分解将时间动力学与细粒度未来世界生成分开，模块化轨迹与视频预测将运动规划与视觉建模端到端结合。架构支持高分辨率长时生成，并以链式前向训练缓解自回归误差累积。实验显示弗雷歇视频距离改进 7.4%、预测时长更长，并作为实时运动规划器在 NAVSIM 上优于强端到端规划器。

**要点：**

- **方法：** Epona 以解耦时空分解与模块化轨迹—视频预测构建自回归扩散 `World Model`，并用链式前向训练抑制误差累积。
- **贡献：** 弗雷歇视频距离改进 7.4% 且预测更长，并作为实时运动规划器在 NAVSIM 上优于强端到端规划器。
- **关系：** 属自动驾驶视频 `World Model` 与规划，摘要未涉及 `VLA`/`VLN`/`VLM`。

---

<a id="p-63"></a>

### 63. EvoVLA: Self-Evolving Vision-Language-Action Model

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2511.16166](https://arxiv.org/abs/2511.16166)

**摘要：** 长时程操作对 `VLA` 仍难，现有模型常出现阶段幻觉，借粗糙评估捷径虚报进度。EvoVLA 含 SAR（三联对比与 Gemini 难负例）、POE（以物体-夹爪相对位姿驱动好奇）及选择性上下文保留与门控融合的长时程记忆。Discoverse-L 上平均成功率较 OpenVLA-OFT 高 10.2 个百分点达 69.2%，样本效率约 1.5 倍，阶段幻觉由 38.5% 降至 14.8%；真机四任务平均 54.6%。

**要点：**

- **方法：** 自监督 `VLA`，含 SAR 三联对比奖励、基于位姿的物体探索与长时程门控记忆。
- **贡献：** 缓解阶段幻觉，仿真与真机长时程操作成功率均高于 OpenVLA-OFT。
- **关系：** 面向 `VLA` 长时程操作与阶段幻觉，摘要未涉及世界模型或 `VLN`。

---

<a id="p-64"></a>

### 64. Explainable Adversarial-Robust Vision-Language-Action Model for Robotic Manipulation

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2512.11865](https://arxiv.org/abs/2512.11865)

**摘要：** 智慧农业常用 RGB 相机与机械臂，但对色调、光照与噪声等光度扰动敏感，对抗攻击下易失灵。本文基于 OpenVLA-OFT 提出可解释、对抗鲁棒的 `VLA`，并集成 Evidence-3 模块检测光度扰动，用自然语言说明成因与影响。实验显示相对基线，当前动作 L1 损失降 21.7%、后续动作 L1 损失降 18.4%，提升对抗条件下的动作预测精度与可解释性。

**要点：**

- **方法：** 基于 OpenVLA-OFT 的可解释对抗鲁棒 `VLA`，用 Evidence-3 检测光度扰动并生成自然语言解释。
- **贡献：** 对抗条件下当前/后续动作 L1 损失分别下降 21.7% 与 18.4%，兼具预测精度与可解释性。
- **关系：** 强化 `VLA` 在光度对抗扰动下的稳健动作预测，摘要未涉及世界模型或 `VLN`。

---

<a id="p-65"></a>

### 65. FAST: Efficient Action Tokenization for Vision-Language-Action Models

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2501.09747](https://arxiv.org/abs/2501.09747)

**摘要：** FAST 提出高效的 `VLA` 动作分词，降低动作序列的 token 数与训练 / 推理成本，成为后续开源 `VLA` 栈的常见组件。

**要点：**

- **方法：** 为 `VLA` 设计更高效的动作分词。
- **贡献：** 在保持控制质量下降低 token 与计算开销。
- **关系：** `VLA` 基础设施，服务策略而非规划 Agent。

---

<a id="p-66"></a>

### 66. FCRF: Flexible Constructivism Reflection for Long-Horizon Robotic Task Planning with Large Language Models

- **年份：** 2025
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2507.14975](https://arxiv.org/abs/2507.14975)

**摘要：** FCRF 提出灵活建构主义反思，用于 LLM 长时程家用任务规划的自主纠错。针对既有自我反思机制僵硬，借鉴人类认知适应，使长时程家务执行更可靠。

**要点：**

- **方法：** 灵活建构主义反思以自主纠正长时程任务规划错误。
- **贡献：** 针对家用机器人提高长时程执行可靠性。
- **关系：** 家用长时程反思 Agent。

---

<a id="p-67"></a>

### 67. Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

- **年份：** 2025
- **标签：** `intersection`
- **链接：** [arXiv:2502.19645](https://arxiv.org/abs/2502.19645)

**摘要：** 近期 `VLA` 依托预训练视觉语言模型与多样机器人数据，具备执行与语义泛化能力，但对新机身常需微调且策略不清。本文以 OpenVLA 比较动作解码、表示与目标，提出并行解码、动作分块、连续动作与 L1 回归的 OFT。LIBERO 上平均成功率由 76.5% 提至 97.1%，吞吐约 26 倍；真机双臂 ALOHA 上优于默认配方的 π0、RDT-1B 及从零训练的 Diffusion Policy 与 ACT，最高约 15 个百分点。

**要点：**

- **方法：** 以 OpenVLA 研究微调设计，提出并行解码、动作分块、连续动作与 L1 回归的 OFT 配方。
- **贡献：** LIBERO 平均成功率由 76.5% 升至 97.1%、吞吐约 26 倍，真机双臂任务优于多种 `VLA` 与模仿策略。
- **关系：** 在预训练 `VLM` 底座上改进 `VLA` 微调与动作解码，摘要未做世界模型或 `VLN` 实验。

---

<a id="p-68"></a>

### 68. FlowDreamer: A RGB-D World Model with Flow-based Motion Representations for Robot Manipulation

- **年份：** 2025
- **标签：** `world_model`
- **链接：** [arXiv:2505.10075](https://arxiv.org/abs/2505.10075)

**摘要：** 本文研究面向机器人操作、以历史帧与动作为条件预测未来观测的 RGB-D 世界模型。不同于把动力学隐含在单一渲染模型中，FlowDreamer 用三维场景流作显式运动表示：先以 U-Net 由历史帧与动作预测场景流，再用扩散模型据此生成未来帧，并端到端训练。在四个涵盖视频预测与视觉规划的基准上，相对其他 RGB-D 世界模型，语义相似高 7%、像素质量高 11%、操作成功率高 6%。

**要点：**

- **方法：** FlowDreamer 以 U-Net 预测三维场景流，再用扩散模型生成未来 RGB-D 帧并端到端训练。
- **贡献：** 在四个视频预测与视觉规划基准上，语义、像素与操作成功率均优于其他 RGB-D 世界模型。
- **关系：** 属面向操作的 RGB-D 世界模型，摘要未涉及 `VLA`/`VLN`/`VLM` 实验。

---

<a id="p-69"></a>

### 69. Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models

- **年份：** 2025
- **标签：** `intersection`
- **链接：** [arXiv:2509.23655](https://arxiv.org/abs/2509.23655)

**摘要：** `VLA` 常复用预训练 `VLM` 输出机器人动作，但视觉输入的 tokenization 计算代价过高。本文提出 Oat-VLA，即面向物体与智能体的分词，把归纳偏置对准场景物体及智能体自身视觉信息，从而把视觉 token 压到极少而不牺牲性能。LIBERO 上收敛至少比 OpenVLA 快一倍，并在多样真机抓放任务上优于 OpenVLA。

**要点：**

- **方法：** Oat-VLA 采用物体—智能体中心的视觉 tokenization，把归纳偏置对准场景物体与智能体自身视觉。
- **贡献：** 将视觉 token 压至极少而不损性能，LIBERO 收敛至少快一倍，真机抓放优于 OpenVLA。
- **关系：** 用物体中心分词降低 `VLM`→`VLA` 适配成本，摘要未涉及世界模型或 `VLN`。

---

<a id="p-70"></a>

### 70. GAIA-2: A Controllable Multi-View Generative World Model for Autonomous Driving

- **年份：** 2025
- **标签：** `world_model`
- **链接：** [arXiv:2503.20523](https://arxiv.org/abs/2503.20523)

**摘要：** GAIA-2 是可控多视角生成式驾驶世界模型，为 GAIA-1 后续。官方权重仍未开放；社区仅有架构级复现。本包补上论文卡片以对照缺口表。

**要点：**

- **方法：** 可控多视角生成式世界模型预测驾驶未来。
- **贡献：** 扩展 GAIA-1 的多视角与可控性。
- **关系：** 驾驶 `World Model`；官方 OSS 仍缺。

---

<a id="p-71"></a>

### 71. Gemini Robotics: Bringing AI into the Physical World

- **年份：** 2025
- **标签：** `VLA` · `VLM`
- **链接：** [arXiv:2503.20020](https://arxiv.org/abs/2503.20020)

**摘要：** Gemini Robotics 把 Gemini 类多模态模型带入物理世界，训练双系统视觉—语言—动作能力，用于真实机器人操作与推理。作为工业闭源 / API 向地标，它常被层次化 Agent 论文当作低层后端。

**要点：**

- **方法：** 把大规模多模态模型适配为物理世界中的双系统机器人模型。
- **贡献：** 展示工业级 `VLM`/`VLA` 进入真机操作。
- **关系：** `VLM`×`VLA` 工业地标；Agent 论文常将其当冻结控制器。

---

<a id="p-72"></a>

### 72. GR00T N1: An Open Foundation Model for Generalist Humanoid Robots

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2503.14734](https://arxiv.org/abs/2503.14734)

**摘要：** 通才机器人需要灵活身体与智能「心智」。GR00T N1 是开放的人形 `VLA`：系统 2 的视觉—语言模块解释环境与指令，系统 1 的扩散 Transformer 实时生成流畅动作，两端到端联合训练。数据混合真机轨迹、人类视频与合成数据。仿真多本体上优于模仿学习基线，并在 Fourier GR-1 人形上做语言条件双臂操作，数据效率高。

**要点：**

- **方法：** 双系统 `VLA`——`VLM` 解释环境，扩散 Transformer 生成实时动作，端到端共训。
- **贡献：** 开放人形基础模型，仿真超模仿基线，并在 Fourier GR-1 上做语言双臂操作。
- **关系：** 人形 `VLA` 底座，高层可被 Agent 编排。

---

<a id="p-73"></a>

### 73. GWM: Towards Scalable Gaussian World Models for Robotic Manipulation

- **年份：** 2025
- **标签：** `VLM` · `world_model`
- **链接：** [arXiv:2508.17600](https://arxiv.org/abs/2508.17600)

**摘要：** 在学得世界模型中训策略可减少真机交互，但图像世界模型即使经大规模视频预训练也缺稳健几何。Gaussian `World Model`（GWM）在动作下推断高斯基元传播以重建未来，核心为潜空间 DiT 与三维变分自编码器，并用 Gaussian Splatting 做场景级重建。它可通过自监督未来预测增强模仿表征，也可作神经仿真器支持基于模型的强化学习；仿真与真机显示其能按多样动作精确预测未来，并据此训出明显更优的策略。

**要点：**

- **方法：** GWM 用潜空间 DiT 与三维 VAE 推断高斯基元在动作下的传播，并以 Gaussian Splatting 重建未来场景。
- **贡献：** 既可自监督增强模仿表征，也可作神经仿真器做基于模型的强化学习，仿真与真机策略优于当时最优。
- **关系：** 三维高斯世界模型服务操作策略训练，摘要未报告 `VLA`/`VLN`/`VLM` 实验。

---

<a id="p-74"></a>

### 74. Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models

- **年份：** 2025
- **标签：** `agent-robot` · `VLA`
- **链接：** [arXiv:2502.19417](https://arxiv.org/abs/2502.19417)

**摘要：** Hi Robot 用层次化视觉—语言—动作模型做开放指令跟随：高层 `VLM` 把复杂指令分解为子任务，低层策略执行。它明确把「听懂并更努力思考」接到机器人控制，是层次化 Agent × `VLA` 的代表。

**要点：**

- **方法：** 层次化 `VLM` 规划器 + 低层 `VLA`/策略执行开放指令。
- **贡献：** 提高复杂、开放式指令跟随。
- **关系：** 层次化 Agent 编排 `VLA`，直接交叉两条线。

---

<a id="p-75"></a>

### 75. Improving Transformer World Models for Data-Efficient RL

- **年份：** 2025
- **标签：** `world_model`
- **链接：** [arXiv:2502.01591](https://arxiv.org/abs/2502.01591)

**摘要：** 本文改进 Transformer 世界模型：Dyna with warmup（模型够好后才用想象数据）、码字固定的最近邻图像块 tokenizer，与联合推理下一时刻全部 token 的 block teacher forcing。Craftax-classic 上 100 万步达 69.66%，超过 DreamerV3 的 53.2% 并首次超过人类 65.0%；亦在 Craftax-full、MinAtar 与三款双人游戏上初步验证。

**要点：**

- **方法：** 改进 Transformer 世界模型：Dyna warmup、固定码字的最近邻图像块 tokenizer 与 block teacher forcing。
- **贡献：** Craftax-classic 上 100 万步达 69.66%，超过 DreamerV3 与人类水平，并在多环境展示通用性。
- **关系：** 专注 Transformer 世界模型与数据高效强化学习，摘要未涉及 `VLA`/`VLN`/`VLM`。

---

<a id="p-76"></a>

### 76. Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling

- **年份：** 2025
- **标签：** `VLM` · `world_model`
- **链接：** [arXiv:2502.00622](https://arxiv.org/abs/2502.00622)

**摘要：** 本文提出 Generative Predictive Control（GPC）：推理期增强预训练行为克隆策略而无需再训练。部署时为冻结的扩散策略配备动作条件世界模型（在专家演示与随机探索上训练），预测提议动作的后果，并以轻量在线规划做前瞻排序与精炼。在多样操作任务、状态/视觉设定以及仿真与真机中，GPC 持续优于标准行为克隆，并与其他推理期适应基线相当或更好。

**要点：**

- **方法：** GPC 在推理期用动作条件世界模型对冻结扩散策略的提议做前瞻排序与精炼，无需再训练。
- **贡献：** 在仿真与真机的状态/视觉操作任务上持续优于标准行为克隆，并可比其他推理期适应基线。
- **关系：** 以世界模型在测试时增强生成式策略；摘要未将方法表述为 `VLA`/`VLN`/`VLM` 实验。

---

<a id="p-77"></a>

### 77. InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation

- **年份：** 2025
- **标签：** `intersection`
- **链接：** [arXiv:2507.17520](https://arxiv.org/abs/2507.17520)

**摘要：** 现有 `VLA` 常在推理与精确动作间取舍，并灾难性遗忘预训练视觉语言能力。InstructVLA 保留大型 `VLM` 灵活推理，并以具身推理取得领先操作。`VLA`-IT 用混合专家适配在 `VLM` 语料与约 65 万条数据上联合优化。SimplerEnv 较 SpatialVLA 高 33%；80 任务指令基准上较微调 OpenVLA 高 96%、较 GPT-4o 辅助动作专家高 29%；多模态任务亦超基线 `VLM`，并可用文本推理做推理期扩展。

**要点：**

- **方法：** InstructVLA 以 `VLA`-IT 与混合专家适配，在 `VLM` 语料与约 65 万条数据上联合优化具身推理与动作。
- **贡献：** SimplerEnv 与 80 任务指令基准上大幅优于 SpatialVLA、微调 OpenVLA 等，并保留多模态能力与推理期扩展。
- **关系：** 在 `VLM` 推理与 `VLA` 操纵间搭桥，摘要未涉及世界模型或 `VLN`。

---

<a id="p-78"></a>

### 78. Kinodynamic Motion Planning for Mobile Robot Navigation across Inconsistent World Models

- **年份：** 2025
- **标签：** `VLM`
- **链接：** [arXiv:2509.26339](https://arxiv.org/abs/2509.26339)

**摘要：** 无先验地图的移动机器人须靠传感器建世界模型，障碍判定常不一致，代价图在障碍与自由空间间翻转。VEH 要求轨迹在历史世界模型中皆安全；另有按改道惩罚调节点代价的 PEH、GEH、GEGRH：PEH 在分歧点做子搜索，后两者推迟到进入目标区，GEGRH 再按分歧节点修订图。PEH/GEH 虽更乐观但规划超 1 秒；越野场上 GEGRH 比 VEH 代价更低、平均更快，比单假设搜索更保守、耗时略增。

**要点：**

- **方法：** 在历史不一致世界模型上规划，比较 VEH、PEH、GEH 与进入目标区后再子搜索并修订图的 GEGRH。
- **贡献：** GEGRH 在越野场上比 VEH 轨迹代价更低、平均规划更快，比单假设搜索更保守且耗时仅略增。
- **关系：** 针对移动机器人不一致世界模型下的运动规划，摘要未涉及 `VLA`/`VLN`/`VLM` 实验。

---

<a id="p-79"></a>

### 79. LaDi-WM: A Latent Diffusion-based World Model for Predictive Manipulation

- **年份：** 2025
- **标签：** `world_model`
- **链接：** [arXiv:2505.11528](https://arxiv.org/abs/2505.11528)

**摘要：** 预测操纵可借未来状态提升策略，但世界模型生成高质量像素级交互仍难。LaDi-WM 用扩散在潜空间预测未来状态，依托与预训练 Visual Foundation Models 对齐的表征：DINO 几何特征与 CLIP 语义特征。作者发现预测潜空间演化比直接预测像素更易学、更可泛化。其上设计扩散策略，迭代融入预报状态以精炼动作。LIBERO-LONG 上策略提升 27.9%，真机约 20%，并展现真机泛化。

**要点：**

- **方法：** LaDi-WM 用扩散预测与 VFM 对齐的潜空间演化（DINO 几何、CLIP 语义），再以预报状态迭代精炼扩散策略。
- **贡献：** LIBERO-LONG 策略提升 27.9%、真机约 20%，并报告世界模型与策略的真机泛化。
- **关系：** 潜空间扩散世界模型服务预测操纵，摘要用 CLIP/DINO 作 VFM，未做 `VLA`/`VLN` 实验。

---

<a id="p-80"></a>

### 80. LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2506.13751](https://arxiv.org/abs/2506.13751)

**摘要：** LeVERB 做人形全身控制的潜在视觉—语言指令：把语言接到全身运动潜空间，而非仅机械臂 `VLA`。

**要点：**

- **方法：** 以潜在视觉—语言指令条件化人形全身控制。
- **贡献：** 把 `VLA` 接口扩展到全身运动。
- **关系：** 人形 `VLA` / 语言条件控制。

---

<a id="p-81"></a>

### 81. LLM+MAP: Bimanual Robot Task Planning using Large Language Models and Planning Domain Definition Language

- **年份：** 2025
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2503.17309](https://arxiv.org/abs/2503.17309)

**摘要：** LLM+MAP 用大语言模型与 PDDL 做双臂长时程任务规划：既有工作多重双手技能，本文补上长时程任务层，用上下文学习与规划域定义协调双手时空。

**要点：**

- **方法：** LLM + PDDL（MAP）做双臂长时程任务规划。
- **贡献：** 把双臂研究从技能层提升到任务规划层。
- **关系：** 双臂符号规划 Agent。

---

<a id="p-82"></a>

### 82. Logic-Guided Socially-aware Robot Navigation World Model

- **年份：** 2025
- **标签：** `VLM`
- **链接：** [arXiv:2510.23509](https://arxiv.org/abs/2510.23509)

**摘要：** 社交机器人导航日益依赖大语言模型做推理与路径规划，但仅靠 LLM 在动态人群中常不安全、缺物理接地与逻辑一致性。NaviWM 将 LLM 推理与结构化世界模型及逻辑驱动思维链结合：时空世界模型刻画智能体位置、速度与活动；演绎模块引导多步逻辑推断，使决策满足个人空间、避碰与时序等约束。社交规范编码为一阶逻辑以便解释与验证。实验显示成功率提升、社交违规减少，尤其在拥挤环境。

**要点：**

- **方法：** NaviWM 以时空世界模型刻画智能体状态，并用一阶逻辑与演绎思维链约束 LLM 导航推理。
- **贡献：** 在定义约束下提升成功率、减少社交违规，尤其在拥挤环境，推理可解释可验证。
- **关系：** 把世界模型与 LLM 形式推理用于社交导航，摘要未做 `VLA` 或标准 `VLN` 基准实验。

---

<a id="p-83"></a>

### 83. LUMOS: Language-Conditioned Imitation Learning with World Models

- **年份：** 2025
- **标签：** `world_model`
- **链接：** [arXiv:2503.10370](https://arxiv.org/abs/2503.10370)

**摘要：** LUMOS 是语言条件多任务模仿学习框架：在学得世界模型潜空间中经长时程 rollout 练习技能，并零样本迁到真机。潜空间 on-policy 学习可缓解离线模仿的策略诱导分布偏移。它从非结构化玩耍数据学习，事后语言标注不足 1%，测试时仍可用语言指挥。训练结合潜空间规划、图像与语言事后目标重标注，并优化潜空间多步内在奖励。CALVIN 链式多任务上优于可比方法；据称是首次在离线世界模型中学习真机语言条件连续视觉运动控制。

**要点：**

- **方法：** LUMOS 在世界模型潜空间中 on-policy 练习技能，结合潜空间规划与图像/语言事后目标重标注。
- **贡献：** 少语言标注的玩耍数据即可语言指挥，CALVIN 链式多任务优于可比方法，并零样本迁到真机。
- **关系：** 语言条件模仿与离线世界模型结合，属 `WM`×语言控制交叉，摘要未称 `VLA`/`VLN`。

---

<a id="p-84"></a>

### 84. mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs

- **年份：** 2025
- **标签：** `VLA` · `world_model` · `intersection`
- **链接：** [arXiv:2512.15692](https://arxiv.org/abs/2512.15692)

**摘要：** mimic-video 提出视频—动作模型（VAM），主张在 `VLA` 之外用视频—动作联合建模获得更可泛化的机器人控制。

**要点：**

- **方法：** 视频—动作模型联合建模未来视频与控制。
- **贡献：** 探索超越标准 `VLA` 的视频动作通才。
- **关系：** 视频 `World Model` 与动作策略统一。

---

<a id="p-85"></a>

### 85. MineWorld: a Real-Time and Open-Source Interactive World Model on Minecraft

- **年份：** 2025
- **标签：** `world_model`
- **链接：** [arXiv:2504.08388](https://arxiv.org/abs/2504.08388)

**摘要：** 世界建模对智能体与人交互、在动态环境中运作至关重要。MineWorld 是 Minecraft 上的实时可交互世界模型，由视觉—动作自回归 Transformer 驱动：用图像与动作 tokenizer 把场景和动作编成离散 token 并交错拼接，以下一 token 预测同时学习状态与动作条件。推理并行解码每帧空间冗余 token，不同规模可达每秒 4 至 7 帧。评测兼顾视觉质量与动作遵从，并显著优于当时开源扩散世界模型。

**要点：**

- **方法：** MineWorld 用视觉—动作自回归 Transformer 交错建模离散场景与动作 token，并以并行解码实时生成。
- **贡献：** 提出兼顾视觉质量与动作遵从的指标，实时可达每秒 4–7 帧，并显著优于开源扩散世界模型。
- **关系：** Minecraft 交互式世界模型，摘要仅评估 `WM`，未涉及 `VLA`/`VLN`/`VLM`。

---

<a id="p-86"></a>

### 86. Motus: A Unified Latent Action World Model

- **年份：** 2025
- **标签：** `world_model` · `VLA` · `intersection`
- **链接：** [arXiv:2512.13030](https://arxiv.org/abs/2512.13030)

**摘要：** Motus 提出统一的潜在动作世界模型，把动作与未来预测放在同一潜空间，衔接世界建模与策略。

**要点：**

- **方法：** 统一潜在动作空间中的世界模型。
- **贡献：** 把动作表征与动力学预测接到同一模型。
- **关系：** 潜在动作 `World Model` × `VLA`。

---

<a id="p-87"></a>

### 87. Optimus-2: Multimodal Minecraft Agent with Goal-Observation-Action Conditioned Policy

- **年份：** 2025
- **标签：** `agent-robot`
- **链接：** [arXiv:2502.19902](https://arxiv.org/abs/2502.19902)

**摘要：** Optimus-2 是多模态 Minecraft 智能体：MLLM 做高层规划，Goal-Observation-Action 条件策略（GOAP）做低层控制，并发布约 3000 万对的 MGOA 数据。在原子、长时程与开放指令任务上优于先前 Minecraft Agent。

**要点：**

- **方法：** MLLM 规划 + 目标—观察—动作条件低层策略，并构建 MGOA 数据。
- **贡献：** 在多样 Minecraft 任务上提升，并开源数据构建方法。
- **关系：** 2025 年开放式具身 Agent，层次类似 Hi Robot。

---

<a id="p-88"></a>

### 88. Phoenix: A Motion-based Self-Reflection Framework for Fine-grained Robotic Action Correction

- **年份：** 2025
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2504.14588](https://arxiv.org/abs/2504.14588)

**摘要：** Phoenix 用基于运动的自我反思，把多模态模型的语义反思翻译成细粒度动作纠正。针对「知道失败了但不知如何改动作」的鸿沟，用运动指令连接语义反思与控制修正。

**要点：**

- **方法：** 运动自我反思框架把语义失败分析落到细粒度动作纠正。
- **贡献：** 弥合 MLLM 反思与可执行动作修正之间的缺口。
- **关系：** 细粒度纠正 Agent，可配合 `VLA`。

---

<a id="p-89"></a>

### 89. Pure Vision Language Action (VLA) Models: A Comprehensive Survey

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2509.19012](https://arxiv.org/abs/2509.19012)

**摘要：** Vision-Language-Action（`VLA`）把 `VLM` 从被动序列生成转为复杂动态环境中的主动操作与决策智能体。本综述梳理先进 `VLA` 方法，给出分类并系统回顾：按自回归、扩散、强化学习、混合与专用等范式分析动机、策略与实现，并介绍基础数据集、基准与仿真平台。在当前图景上讨论挑战与未来方向。综合三百余项近期研究，勾勒可扩展、通用 `VLA` 与可泛化机器人的机遇与难点。

**要点：**

- **方法：** 综述将 `VLA` 分为自回归、扩散、强化学习、混合与专用等范式，并梳理数据、基准与仿真平台。
- **贡献：** 综合三百余项研究给出分类图景，并讨论可扩展、通用 `VLA` 与可泛化机器人的挑战与方向。
- **关系：** 系统梳理 `VLA` 及其 `VLM` 根基，摘要未单独展开世界模型或 `VLN` 专论。

---

<a id="p-90"></a>

### 90. REFLEX: Metacognitive Reasoning for Reflective Zero-Shot Robotic Planning with Large Language Models

- **年份：** 2025
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2505.14899](https://arxiv.org/abs/2505.14899)

**摘要：** REFLEX 赋予 LLM 元认知推理，做反思式零样本机器人规划：不停留在静态提示行为，而用类似人类的元认知与创造性解题提升复杂任务上的零 / 少样本规划。

**要点：**

- **方法：** 元认知推理支持反思式零样本机器人规划。
- **贡献：** 把 LLM 从静态提示行为推进到可反思规划。
- **关系：** 元认知规划 Agent。

---

<a id="p-91"></a>

### 91. RLVR-World: Training World Models with Reinforcement Learning

- **年份：** 2025
- **标签：** `world_model`
- **链接：** [arXiv:2505.13934](https://arxiv.org/abs/2505.13934)

**摘要：** 世界模型按动作预测状态转移，但最大似然等标准目标常与精度、感知质量等任务指标不对齐。RLVR-World 用带可验证奖励的强化学习（RLVR）直接按这些指标优化世界模型：虽把建模写成对分词序列的自回归预测，却以解码后预测的指标作可验证奖励。在语言与视频世界模型上，覆盖文本游戏、网页导航与机器人操作，均获显著提升。作者认为 RLVR 可作为生成模型更广泛的后训练范式。

**要点：**

- **方法：** RLVR-World 将世界模型作分词序列自回归，但以解码预测的可验证指标为奖励做强化学习后训练。
- **贡献：** 在语言与视频世界模型上提升文本游戏、网页导航与机器人操作等域的任务指标。
- **关系：** 用 RLVR 对齐世界模型与任务度量；网页导航等为 `WM` 评测域，摘要未做 `VLA`/`VLM` 实验。

---

<a id="p-92"></a>

### 92. RoboFlamingo-Plus: Fusion of Depth and RGB Perception with Vision-Language Models for Enhanced Robotic Manipulation

- **年份：** 2025
- **标签：** `VLM`
- **链接：** [arXiv:2503.19510](https://arxiv.org/abs/2503.19510)

**摘要：** 机器人走向复杂多模态操作时，融合先进 `VLM` 是关键，但在三维环境中融合深度与 RGB、并按语言指令执行仍困难。RoboFlamingo-Plus 在 RoboFlamingo 上引入深度：用预训练 Vision Transformer 与重采样融合 RGB 与深度并对齐语言；以预训练 resampler 提取深度特征，再用交叉注意力整合。从而更好理解三维环境并完成语言引导任务。实验显示操作性能较现有方法提升约 10%–20%。

**要点：**

- **方法：** RoboFlamingo-Plus 用预训练 ViT 与 resampler 融合 RGB 与深度，并以交叉注意力对齐语言。
- **贡献：** 在语言引导操作上较现有方法提升约 10%–20%，增强三维环境理解。
- **关系：** 改进 `VLM` 感知融合以服务机器人操作，摘要未涉及世界模型或 `VLN`。

---

<a id="p-93"></a>

### 93. RoboHorizon: An LLM-Assisted Multi-View World Model for Long-Horizon Robotic Manipulation

- **年份：** 2025
- **标签：** `VLM` · `world_model`
- **链接：** [arXiv:2501.06605](https://arxiv.org/abs/2501.06605)

**摘要：** 长时程操作中表示与策略学习困难，基于模型的视觉强化学习仍受稀疏奖励与复杂视觉困扰。本文提出 RSPA 流程与 RoboHorizon：预训练 LLM 按语言指令为多阶段子任务生成稠密奖励；关键帧发现接入多视角掩码自编码器；再构建机器人世界模型，用强化学习规划执行。RLBench 4 个短时程任务成功率高 23.35%，6 个长时程加 FurnitureBench 3 个装配任务高 29.23%。

**要点：**

- **方法：** RoboHorizon 用 LLM 生成多阶段稠密奖励，在多视角 MAE 中发现关键帧，并构建世界模型供强化学习规划。
- **贡献：** 提出 RSPA 流程，在 RLBench 短/长时程及 FurnitureBench 装配上成功率明显高于视觉模型强化学习基线。
- **关系：** LLM 辅助多视角世界模型做长时程操作，摘要未将方法表述为 `VLA`/`VLN`。

---

<a id="p-94"></a>

### 94. RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models

- **年份：** 2025
- **标签：** `agent-robot` · `VLA`
- **链接：** [arXiv:2506.17811](https://arxiv.org/abs/2506.17811)

**摘要：** RoboMonkey 扩展 `VLA` 的测试时采样与验证：对候选动作做缩放采样并由验证器筛选，把 Agent 式 test-time compute 接到策略。层次化编排论文常引用它作为验证模块。

**要点：**

- **方法：** 测试时对 `VLA` 动作候选做大规模采样与验证。
- **贡献：** 用推理期计算提升 `VLA` 可靠性。
- **关系：** Agent 式测试时计算 × `VLA`。

---

<a id="p-95"></a>

### 95. Robot Learning from a Physical World Model

- **年份：** 2025
- **标签：** `VLM`
- **链接：** [arXiv:2511.07416](https://arxiv.org/abs/2511.07416)

**摘要：** PhysWorld 让机器人从视频生成中经物理世界建模学习。近期视频生成模型可由语言与图像合成逼真演示，但把像素运动直接重定向到机器人常忽略物理、导致操作不准。给定单图与任务指令，方法生成任务条件视频并重建底层物理世界，再以物体中心残差强化学习把视频运动落到物理可执行动作。该协同无需真机数据采集，实现零样本可泛化操作；多样真机任务上操作精度较先前方法显著提升。

**要点：**

- **方法：** PhysWorld 由语言与图像生成任务视频并重建物理世界，再用物体中心残差强化学习落到可执行动作。
- **贡献：** 无需真机数据采集即可把视频运动转为物理轨迹，多样真机任务上操作精度优于先前方法。
- **关系：** 物理世界模型对接语言条件视频生成以学操作，摘要未报告 `VLA`/`VLN`/`VLM` 实验。

---

<a id="p-96"></a>

### 96. Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics

- **年份：** 2025
- **标签：** `world_model`
- **链接：** [arXiv:2501.10100](https://arxiv.org/abs/2501.10100)

**摘要：** 学习稳健可泛化的世界模型对真实环境中高效可扩展机器人控制至关重要。本文提出刻画复杂、部分可观测且随机动力学的世界模型框架，采用双自回归机制与自监督训练，在不依赖领域特定归纳偏置的情况下获得可靠长时程预测，以适应多样机器人任务。进一步给出策略优化框架，在想象环境中高效训练并部署到真实系统。工作针对长时程预测、误差累积与仿真到现实迁移，为自适应高效机器人系统提供可扩展路径。

**要点：**

- **方法：** 双自回归与自监督训练学习部分可观测随机动力学，并在世界模型想象中优化策略再部署真机。
- **贡献：** 在无领域特定归纳偏置下做长时程预测，面向误差累积与仿真到现实迁移给出可扩展框架。
- **关系：** 纯世界模型与基于模型的策略优化，摘要未涉及 `VLA`/`VLN`/`VLM`。

---

<a id="p-97"></a>

### 97. RobotxR1: Enabling Embodied Robotic Intelligence on Large Language Models through Closed-Loop Reinforcement Learning

- **年份：** 2025
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2505.03238](https://arxiv.org/abs/2505.03238)

**摘要：** RobotxR1 把 R1-zero 思路扩到机器人：用闭环强化学习让小参数量 LLM 在机载、非持续云连接条件下具备具身智能，平衡能力与算力 / 内存约束。

**要点：**

- **方法：** 闭环 RL 将低参数 LLM 适配为机载具身智能。
- **贡献：** 面向无持续云连接的机载语言控制。
- **关系：** 机载语言 Agent，补云端 GPT 编排的缺口。

---

<a id="p-98"></a>

### 98. Safe LLM-Controlled Robots with Formal Guarantees via Reachability Analysis

- **年份：** 2025
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2503.03911](https://arxiv.org/abs/2503.03911)

**摘要：** LLM 零样本增强人机交互，但其概率性缺形式保证。本文用可达性分析为 LLM 控制的机器人提供形式化安全保证，针对不可预测环境中的安全关键部署。

**要点：**

- **方法：** 以可达性分析为 LLM 控机器人提供形式保证。
- **贡献：** 把传统模型验证接到概率性语言控制器。
- **关系：** 安全形式化 × 语言 Agent。

---

<a id="p-99"></a>

### 99. Safety Guardrails for LLM-Enabled Robots

- **年份：** 2025
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2503.07885](https://arxiv.org/abs/2503.07885)

**摘要：** 讨论 LLM 机器人的安全护栏：覆盖幻觉等平均错误与对抗越狱，指出传统机器人安全不管 LLM 的上下文脆弱性，需要针对语言控制栈的护栏。

**要点：**

- **方法：** 为 LLM 使能的机器人设计针对幻觉与越狱的安全护栏。
- **贡献：** 区分传统机器人安全与语言上下文脆弱性。
- **关系：** Agent 安全护栏。

---

<a id="p-100"></a>

### 100. SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2506.01844](https://arxiv.org/abs/2506.01844)

**摘要：** 预训练 `VLM` 蕴含丰富视觉与语言知识，常被改造成 `VLA`，但现有模型动辄数十亿参数，训练贵、难部署，且多依赖学术工业数据、忽视社区廉价平台数据。SmolVLA 是小型、高效、社区驱动的 `VLA`，大幅降低训练与推理成本且保持竞争力，可在单 GPU 训练、消费级 GPU 甚至 CPU 部署。异步推理栈将感知与动作预测与执行解耦，以分块动作提高控制频率。紧凑体量下性能可比大约 10 倍的 `VLA`；并在仿真与真机基准上评估、公开代码与数据。

**要点：**

- **方法：** SmolVLA 将 `VLM` 做成小型社区驱动 `VLA`，并以异步推理栈把感知/预测与动作执行解耦。
- **贡献：** 单 GPU 可训、消费级设备可部署，性能可比大约 10 倍的 `VLA`，并公开代码、权重与数据。
- **关系：** 降低 `VLM`→`VLA` 的训练与部署成本，摘要未涉及世界模型或 `VLN`。

---

<a id="p-101"></a>

### 101. SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2501.15830](https://arxiv.org/abs/2501.15830)

**摘要：** SpatialVLA 在 110 万真实回合上训练空间增强 `VLA`，用自我中心位置编码与自适应空间网格注入 3D 信息。RSS 2025，开源已核验，零样本与新本体适应表现强，推理 token 更少。

**要点：**

- **方法：** 自我中心位置编码与自适应空间网格增强 `VLA` 的 3D 空间理解。
- **贡献：** 大规模真实数据上取得强零样本与高效推理。
- **关系：** 空间 `VLA` 策略，可作层次化 Agent 的低层控制器。

---

<a id="p-102"></a>

### 102. Survey on Vision-Language-Action Models

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2502.06851](https://arxiv.org/abs/2502.06851)

**摘要：** 本文是由大语言模型生成的 `VLA` 综述，概括方法、发现与未来方向，仅作演示，不代表原创研究，意在展示 AI 辅助文献综述的可能。随着 AI 生成内容增多，准确性、可靠性与综合质量仍是挑战。作者计划构建 AI 辅助综述的结构化框架，改进引用准确性、来源可信度与语境理解，并讨论 LLM 用于学术写作的潜力与局限，作为系统化利用 AI 做文献综合的初步探索。

**要点：**

- **方法：** 用大语言模型自动生成 `VLA` 文献综述，概括方法、发现与未来方向，仅作演示。
- **贡献：** 展示 AI 辅助综述的可能，并指出准确性、引用与综合质量等挑战及后续框架设想。
- **关系：** 主题为 `VLA` 综述，但摘要声明非原创研究，不可当作已核验的 `VLA` 实验或结论。

---

<a id="p-103"></a>

### 103. TesserAct: Learning 4D Embodied World Models

- **年份：** 2025
- **标签：** `world_model`
- **链接：** [arXiv:2504.20995](https://arxiv.org/abs/2504.20995)

**摘要：** 本文提出学习新颖的4D 具身世界模型，根据具身智能体动作预测三维场景随时间的动态演化并保持时空一致性。方法是在 RGB-DN（RGB、深度与法向）视频上训练：先用现成模型为机器人操作视频补充深度与法向，再微调视频生成模型联合预测每帧 RGB-DN，最后将生成结果直接转为高质量4D 场景。该方法保证具身预测的时空连贯，支持新视角合成，并促进显著优于先前视频世界模型的策略学习。

**要点：**

- **方法：** 用现成模型为操作视频补充深度与法向，微调视频生成模型联合预测 RGB-DN 并转为4D 场景。
- **贡献：** 实现具身场景的时空一致4D 预测与新视角合成，并促进优于先前视频世界模型的策略学习。
- **关系：** 面向具身动作条件的4D `World Model`，服务场景演化与策略学习（主要为 `WM`）。

---

<a id="p-104"></a>

### 104. Unified Vision-Language-Action Model

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2506.19850](https://arxiv.org/abs/2506.19850)

**摘要：** Unified Vision-Language-Action Model 研究统一架构同时做视觉—语言理解与动作生成，减少「理解模型 + 动作头」的割裂。

**要点：**

- **方法：** 统一模型同时承担视觉语言理解与动作合成。
- **贡献：** 探索理解与控制共享骨干的 `VLA`。
- **关系：** 统一 `VLA`，高层推理可服务 Agent。

---

<a id="p-105"></a>

### 105. Universal Actions for Enhanced Embodied Foundation Models

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2501.10105](https://arxiv.org/abs/2501.10105)

**摘要：** Universal Actions 研究跨本体具身基础模型的通用动作表示，使不同机器人共享动作接口，增强通才 `VLA` 的跨本体迁移。

**要点：**

- **方法：** 设计跨本体共享的通用动作表示。
- **贡献：** 提升具身基础模型的跨机器人迁移。
- **关系：** `VLA` 动作接口，便于高层 Agent 调用统一技能。

---

<a id="p-106"></a>

### 106. UniVLA: Learning to Act Anywhere with Task-centric Latent Actions

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2505.06111](https://arxiv.org/abs/2505.06111)

**摘要：** UniVLA 学习任务中心的潜在动作，使策略可在不同本体与场景「随处行动」，用潜在动作统一跨环境控制。

**要点：**

- **方法：** 任务中心潜在动作表示，统一跨场景 `VLA`。
- **贡献：** 提高跨本体 / 跨场景行动能力。
- **关系：** 潜在动作 `VLA`，接近动作条件世界表征。

---

<a id="p-107"></a>

### 107. V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

- **年份：** 2025
- **标签：** `world_model`
- **链接：** [arXiv:2506.09985](https://arxiv.org/abs/2506.09985)

**摘要：** 本文探索自监督路径：结合互联网规模视频与少量机器人轨迹，构建能理解、预测并规划物理世界的模型。先在逾百万小时网络视频上预训练无动作的联合嵌入预测架构 `V-JEPA` 2，再与大语言模型对齐以提升视频问答。随后用 Droid 中少于62 小时无标注机器人视频后训练潜在动作条件世界模型 `V-JEPA` 2-AC，并在两实验室 Franka 机械臂上按图像目标零样本完成抓放，无需这些环境的数据或任务特定训练与奖励。

**要点：**

- **方法：** 先在大规模网络视频预训练 `V-JEPA` 2，再后训练潜在动作条件世界模型 `V-JEPA` 2-AC。
- **贡献：** 在运动理解与动作预期上表现突出，并可零样本部署到未见环境的 Franka 机械臂完成抓放规划。
- **关系：** 表明网络视频加少量机器人交互即可得到可规划的 `World Model`（主要为 `WM`）。

---

<a id="p-108"></a>

### 108. Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges

- **年份：** 2025
- **标签：** `intersection`
- **链接：** [arXiv:2505.04769](https://arxiv.org/abs/2505.04769)

**摘要：** 本文对 `VLA` 模型作基础综述，按五个主题梳理进展：从跨模态架构到融合 `VLM`、动作规划器与分层控制器的通才智能体，并以文献综述框架覆盖近三年80 余个模型。讨论架构创新、高效训练与实时推理加速，以及自动驾驶、医疗工业机器人、精准农业、人形机器人与增强现实等应用，分析智能体自适应与跨本体规划等挑战，并展望 `VLA`、`VLM` 与智能体式 AI 融合以强化社会对齐、自适应的通用具身智能体。

**要点：**

- **方法：** 以严格文献综述框架覆盖近三年80 余个 `VLA` 模型，按五个主题组织。
- **贡献：** 系统梳理 `VLA` 概念演进、架构与训练、应用与挑战，并给出与 `VLM` 及智能体式 AI 融合的路线图。
- **关系：** 为 `VLA` 与 `VLM` 交叉提供概念与应用全景，未涉及 `World Model` 实验。

---

<a id="p-109"></a>

### 109. Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2510.07077](https://arxiv.org/abs/2510.07077)

**摘要：** 在利用 LLM 与 `VLM` 推进机器人学的背景下，`VLA` 通过规模化统一视觉、语言与动作数据，旨在学习可跨任务、物体、本体与环境泛化的策略，从而以极少或无需任务数据解决新下游任务。本文提供涵盖软硬件的全栈综述，覆盖策略与架构演进、组成模块、模态处理与学习范式，并回顾常用机器人平台、数据采集、公开数据集、数据增强与评测基准，为将 `VLA` 部署到真实机器人系统提供实践指引。

**要点：**

- **方法：** 对 `VLA` 作涵盖软硬件的全栈综述，系统梳理架构、模态处理与学习范式。
- **贡献：** 同时回顾机器人平台、数据采集、公开数据集、增强方法与评测基准，面向真实部署。
- **关系：** 聚焦 `VLA` 如何把 `VLM` 能力落到可泛化机器人策略，未涉及 `World Model` 实验。

---

<a id="p-110"></a>

### 110. Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning

- **年份：** 2025
- **标签：** `intersection`
- **链接：** [arXiv:2510.11027](https://arxiv.org/abs/2510.11027)

**摘要：** 针对上游 `VLM` 具身推理与下游 `VLA` 策略学习之间的缺口，本文提出 Vlaser——具备协同具身推理能力的 `VLA`，作为融合高层推理与低层控制的基础视觉语言模型。基于高质量 Vlaser-6M 数据集，在空间推理、具身定位、具身问答与任务规划等基准上取得领先。并系统考察不同 `VLM` 初始化对监督式 `VLA` 微调的影响，以缓解互联网预训练与具身策略数据之间的域偏移；据此在 WidowX 上达到领先、在 Google Robot 上具有竞争力。

**要点：**

- **方法：** 构建融合高层推理与低层控制的基础 `VLM`/`VLA`，并基于 Vlaser-6M 训练。
- **贡献：** 在多项具身推理基准领先，并揭示 `VLM` 初始化如何缓解监督 `VLA` 微调中的域偏移。
- **关系：** 直接衔接 `VLM` 推理与 `VLA` 策略学习，服务具身控制（非 `World Model` 实验）。

---

<a id="p-111"></a>

### 111. VOTE: Vision-Language-Action Optimization with Trajectory Ensemble Voting

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2507.05116](https://arxiv.org/abs/2507.05116)

**摘要：** 针对当前 `VLA` 生成大量 token 导致推理延迟与训练成本高、且生成动作利用不足的问题，本文提出训练框架，以高并行方式微调 `VLA` 生成显著更少的动作 token。并引入基于投票的集成推理，融合当前与历史动作预测以提升动作利用率。结果显示相对先进 `VLA` 有更高成功率，推理较 OpenVLA 快39 倍，边缘平台吞吐46 Hz，具备实际部署性。

**要点：**

- **方法：** 微调 `VLA` 以高并行生成更少动作 token，并用投票集成融合当前与历史动作预测。
- **贡献：** 相对先进 `VLA` 提高成功率并显著降低推理延迟，可在边缘平台部署。
- **关系：** 针对 `VLA` 推理效率与动作利用，未涉及 `World Model` 或 `VLN` 实验。

---

<a id="p-112"></a>

### 112. WorldVLA: Towards Autoregressive Action World Model

- **年份：** 2025
- **标签：** `world_model`
- **链接：** [arXiv:2506.21539](https://arxiv.org/abs/2506.21539)

**摘要：** 本文提出 WorldVLA，将 `VLA` 与世界模型统一为自回归动作世界模型：世界模型依动作与图像理解预测未来图像以学习环境物理，动作模型依图像观测生成动作并反哺视觉理解与生成，二者相互增强。针对自回归动作序列误差传播导致性能下降，提出在生成当前动作时选择性掩蔽先前动作的注意力掩码策略，显著改善动作块生成。

**要点：**

- **方法：** 在单一自回归框架中联合世界模型的未来图像预测与 `VLA` 式动作生成，并用注意力掩码抑制历史动作干扰。
- **贡献：** 表明世界模型与动作模型相互增强，掩码策略可缓解自回归动作块中的误差传播。
- **关系：** 明确把 `World Model` 与 `VLA` 统一，用未来视觉预测改进动作生成。

---

<a id="p-113"></a>

### 113. X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2510.10274](https://arxiv.org/abs/2510.10274)

**摘要：** X-VLA 用软提示 Transformer 做可扩展跨本体视觉—语言—动作模型，以提示而非重训适应新本体。

**要点：**

- **方法：** 软提示 Transformer 实现跨本体可扩展 `VLA`。
- **贡献：** 降低新本体适应成本。
- **关系：** 跨本体 `VLA`，便于 Agent 层切换技能后端。

---

<a id="p-114"></a>

### 114. π₀.₅: a Vision-Language-Action Model with Open-World Generalization

- **年份：** 2025
- **标签：** `VLA`
- **链接：** [arXiv:2504.16054](https://arxiv.org/abs/2504.16054)

**摘要：** π₀.₅ 是 Physical Intelligence 的视觉—语言—动作模型，强调开放世界泛化。作为 π₀ 后续，它被层次化 Agent 与 OpenPI 栈广泛当作低层通才策略。

**要点：**

- **方法：** 在 π₀ 流匹配 `VLA` 上提升开放世界泛化。
- **贡献：** 成为 2025 年通才机器人策略的常用底座。
- **关系：** `VLA` 底座，常被 Agent 编排层调用。

---

## 2024 年

共 63 篇。先扫目录，再下翻卡片。

- [115. 3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations](#p-115)  `VLM`
- [116. 3D-VLA: A 3D Vision-Language-Action Generative World Model](#p-116)  `VLA` · `world_model` · `intersection`
- [117. A Survey on Robotics with Foundation Models: toward Embodied AI](#p-117)  `llm-agent` · `VLA`
- [118. A Survey on Vision-Language-Action Models for Embodied AI](#p-118)  `VLA`
- [119. Adaptive Mobile Manipulation for Articulated Objects In the Open World](#p-119)  `agent-robot`
- [120. AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents](#p-120)  `agent-robot` · `llm-agent` · `VLM`
- [121. AVID: Adapting Video Diffusion Models to World Models](#p-121)  `world_model`
- [122. Bringing the RT-1-X Foundation Model to a SCARA robot](#p-122)  `VLM`
- [123. CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision](#p-123)  `intersection`
- [124. Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection](#p-124)  `agent-robot` · `llm-agent` · `VLM`
- [125. CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation](#p-125)  `VLA`
- [126. COHERENT: Collaboration of Heterogeneous Multi-Robot System with Large Language Models](#p-126)  `agent-robot` · `llm-agent`
- [127. DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models](#p-127)  `agent-robot` · `llm-agent`
- [128. Diffusion for World Modeling: Visual Details Matter in Atari](#p-128)  `world_model`
- [129. Diffusion Models Are Real-Time Game Engines](#p-129)  `world_model`
- [130. DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](#p-130)  `world_model`
- [131. DrivingGPT: Unifying Driving World Modeling and Planning with Multi-modal Autoregressive Transformers](#p-131)  `world_model`
- [132. DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](#p-132)  `VLA`
- [133. Embodied AI in Mobile Robots: Coverage Path Planning with Large Language Models](#p-133)  `agent-robot` · `llm-agent`
- [134. Enhancing End-to-End Autonomous Driving with Latent World Model](#p-134)  `world_model`
- [135. Genie: Generative Interactive Environments](#p-135)  `world_model`
- [136. GR-2: A Generative Video-Language-Action Model with Web-Scale Knowledge for Robot Manipulation](#p-136)  `VLA`
- [137. Imagination Policy: Using Generative Point Cloud Models for Learning Manipulation Policies](#p-137)  `world_model`
- [138. IRASim: A Fine-Grained World Model for Robot Manipulation](#p-138)  `world_model`
- [139. Jailbreaking LLM-Controlled Robots](#p-139)  `agent-robot` · `llm-agent`
- [140. Large Language Models for Orchestrating Bimanual Robots](#p-140)  `agent-robot` · `llm-agent`
- [141. Latent Action Pretraining from Videos](#p-141)  `VLA`
- [142. LLaRA: Supercharging Robot Learning Data for Vision-Language Policy](#p-142)  `VLA`
- [143. LLM-Driven Robots Risk Enacting Discrimination, Violence, and Unlawful Actions](#p-143)  `agent-robot` · `llm-agent`
- [144. LLM-Personalize: Aligning LLM Planners with Human Preferences via Reinforced Self-Training for Housekeeping Robots](#p-144)  `llm-agent` · `agent-robot`
- [145. LLM3:Large Language Model-based Task and Motion Planning with Motion Failure Reasoning](#p-145)  `agent-robot` · `llm-agent`
- [146. MALMM: Multi-Agent Large Language Models for Zero-Shot Robotics Manipulation](#p-146)  `agent-robot` · `llm-agent`
- [147. MapGPT: Map-Guided Prompting with Adaptive Path Planning for Vision-and-Language Navigation](#p-147)  `VLN`
- [148. Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation](#p-148)  `VLM`
- [149. Multi-Modal Grounded Planning and Efficient Replanning For Learning Embodied Agents with A Few Examples](#p-149)  `agent-robot` · `llm-agent`
- [150. NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models](#p-150)  `VLN`
- [151. NaVILA: Legged Robot Vision-Language-Action Model for Navigation](#p-151)  `VLA` · `VLN`
- [152. Octo: An Open-Source Generalist Robot Policy](#p-152)  `VLA`
- [153. OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics](#p-153)  `agent-robot` · `VLM`
- [154. On the Vulnerability of LLM/VLM-Controlled Robotics](#p-154)  `agent-robot` · `llm-agent` · `VLM`
- [155. OpenVLA: An Open-Source Vision-Language-Action Model](#p-155)  `VLA`
- [156. Pandora: Towards General World Model with Natural Language Actions and Video States](#p-156)  `world_model`
- [157. Physically Embodied Gaussian Splatting: A Realtime Correctable World Model for Robotics](#p-157)  `world_model`
- [158. Plan-Seq-Learn: Language Model Guided RL for Solving Long Horizon Robotics Tasks](#p-158)  `agent-robot` · `llm-agent`
- [159. RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation](#p-159)  `VLA`
- [160. ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation](#p-160)  `agent-robot` · `llm-agent` · `VLM`
- [161. RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots](#p-161)  `VLA`
- [162. RoboCodeX: Multimodal Code Generation for Robotic Behavior Synthesis](#p-162)  `agent-robot` · `llm-agent`
- [163. RoboDreamer: Learning Compositional World Models for Robot Imagination](#p-163)  `world_model`
- [164. Robotic Control via Embodied Chain-of-Thought Reasoning](#p-164)  `agent-robot` · `VLA`
- [165. SELP: Generating Safe and Efficient Task Plans for Robot Agents with Large Language Models](#p-165)  `agent-robot` · `llm-agent`
- [166. ShowUI: One Vision-Language-Action Model for GUI Visual Agent](#p-166)  `VLA`
- [167. SPINE: Online Semantic Planning for Missions with Incomplete Natural Language Specifications in Unstructured Environments](#p-167)  `agent-robot` · `llm-agent`
- [168. TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation](#p-168)  `intersection`
- [169. TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies](#p-169)  `VLA`
- [170. Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations](#p-170)  `world_model` · `VLA` · `intersection`
- [171. Vision-and-Language Navigation Today and Tomorrow: A Survey in the Era of Foundation Models](#p-171)  `VLN`
- [172. What Matters in Building Vision-Language-Action Models for Generalist Robots](#p-172)  `VLA`
- [173. Wonderful Team: Zero-Shot Physical Task Planning with Visual LLMs](#p-173)  `agent-robot` · `llm-agent`
- [174. World Model-based Perception for Visual Legged Locomotion](#p-174)  `world_model`
- [175. WorldDreamer: Towards General World Models for Video Generation via Predicting Masked Tokens](#p-175)  `world_model`
- [176. X-MOBILITY: End-To-End Generalizable Navigation via World Modeling](#p-176)  `world_model`
- [177. π₀: A Vision-Language-Action Flow Model for General Robot Control](#p-177)  `VLA`

<a id="p-115"></a>

### 115. 3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations

- **年份：** 2024
- **标签：** `VLM`
- **链接：** [arXiv:2403.03954](https://arxiv.org/abs/2403.03954)

**摘要：** 模仿学习能高效传授灵巧技能，但稳健可泛化通常需大量示范。本文提出3D Diffusion Policy（DP3），将紧凑三维视觉表征纳入扩散策略：由稀疏点云经高效点编码器提取。在72 项仿真任务中，多数仅用10 条示范即可完成并相对基线提升24.2%；4 项真实任务各40 条示范成功率达85%，并在空间、视角、外观与实例上表现良好泛化，且较少违反安全约束。评估强调三维表征对真实机器人学习的关键作用。

**要点：**

- **方法：** 用高效点编码器从稀疏点云提取紧凑3D 表征，并融入作为条件动作生成模型的扩散策略。
- **贡献：** 在少量示范下提升仿真与真实操作成功率，并改善空间、视角、外观与实例泛化及安全性。
- **关系：** 为视觉运动策略提供3D 表征，服务 `VLM` 相关具身控制，非 `World Model` 实验。

---

<a id="p-116"></a>

### 116. 3D-VLA: A 3D Vision-Language-Action Generative World Model

- **年份：** 2024
- **标签：** `VLA` · `world_model` · `intersection`
- **链接：** [arXiv:2403.09631](https://arxiv.org/abs/2403.09631)

**摘要：** 3D-VLA 提出三维视觉—语言—动作生成式世界模型，在 3D 场景中把语言、感知与动作交互统一建模。它补全本包 OSS 已收录、论文卡片此前缺失的 `WM`×`VLA` 交叉地标。

**要点：**

- **方法：** 三维生成式世界模型统一语言、场景与动作交互。
- **贡献：** 为具身交互提供 3D 条件的生成式 `WM`/`VLA`。
- **关系：** 直接交叉 3D `World Model` 与 `VLA`。

---

<a id="p-117"></a>

### 117. A Survey on Robotics with Foundation Models: toward Embodied AI

- **年份：** 2024
- **标签：** `llm-agent` · `VLA`
- **链接：** [arXiv:2402.02385](https://arxiv.org/abs/2402.02385)

**摘要：** 机器人与基础模型综述，面向具身人工智能，梳理语言、视觉与动作基础模型如何进入机器人栈，并讨论评测与安全。

**要点：**

- **方法：** 综述基础模型驱动的机器人 / 具身 AI。
- **贡献：** 提供 2024 年前后的具身基础模型地图。
- **关系：** 交叉综述。

---

<a id="p-118"></a>

### 118. A Survey on Vision-Language-Action Models for Embodied AI

- **年份：** 2024
- **标签：** `VLA`
- **链接：** [arXiv:2405.14093](https://arxiv.org/abs/2405.14093)

**摘要：** 具身 AI 因控制智能体在物理世界执行任务而被视为 AGI 基石。在 LLM 与 `VLM` 成功之上，`VLA` 应运而生以生成动作、完成语言条件机器人任务。本文给出面向具身 AI 的首份 `VLA` 综述，将研究分为三条主线：`VLA` 各组成模块、擅长预测低层动作的 `VLA` 控制策略，以及把长时程任务分解为子任务序列的高层规划器。并汇总数据集、仿真器与基准，讨论挑战与未来方向。

**要点：**

- **方法：** 对具身 AI 中的 `VLA` 作分类综述，按组件、低层控制策略与高层任务规划三条主线组织。
- **贡献：** 系统梳理相关数据集、仿真器与基准，并讨论挑战与未来方向。
- **关系：** 阐明 `VLA` 如何衔接 `VLM` 与具身动作，未涉及 `World Model` 实验。

---

<a id="p-119"></a>

### 119. Adaptive Mobile Manipulation for Articulated Objects In the Open World

- **年份：** 2024
- **标签：** `agent-robot`
- **链接：** [arXiv:2401.14403](https://arxiv.org/abs/2401.14403)

**摘要：** 实验室内的移动操作常止于抓—移—放。本文提出开放世界移动操作系统，全栈处理真实门、柜、抽屉与冰箱等铰接物：先用少量数据行为克隆，再在分布外物体上在线练习。配套约 2 万美元的低成本移动操作平台。在卡内基梅隆校园 4 栋楼、20 个铰接物上，每物不足 1 小时在线学习即可把成功率从行为克隆的 50% 提高到 95%。

**要点：**

- **方法：** 少量行为克隆后再对未见铰接物做在线自适应，并给出低成本移动操作硬件。
- **贡献：** 校园 4 栋楼 20 个铰接物上，在线学习约 1 小时内成功率由 50% 升至 95%。
- **关系：** 开放世界移动操作技能，可被家用语言 Agent 当铰接物原语调用。

---

<a id="p-120"></a>

### 120. AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents

- **年份：** 2024
- **标签：** `agent-robot` · `llm-agent` · `VLM`
- **链接：** [arXiv:2401.12963](https://arxiv.org/abs/2401.12963)

**摘要：** AutoRT 用 `VLM` 做场景理解、用 LLM 提出多样指令，并借助「机器人宪法」过滤不安全任务，从而在未见场景以极少人工监督部署机器人车队。系统在 4 栋楼、20 余台机器人上收集 7.7 万真实回合，展示 LLM 控制机器人在真实环境中自主提出目标并采集数据。

**要点：**

- **方法：** `VLM` 接地场景 + LLM 提案指令 + 机器人宪法安全过滤，编排车队采集。
- **贡献：** 7 个月收集 7.7 万真实回合，指令更多样并更对齐人的偏好。
- **关系：** 大规模 Agent 编排真机车队，服务后续 `VLA` 数据。

---

<a id="p-121"></a>

### 121. AVID: Adapting Video Diffusion Models to World Models

- **年份：** 2024
- **标签：** `world_model`
- **链接：** [arXiv:2410.12822](https://arxiv.org/abs/2410.12822)

**摘要：** 决策任务中带动作标注的数据稀缺。AVID 在无法获取预训练参数的前提下，将预训练视频扩散模型适配为动作条件世界模型：在少量领域动作标注视频上训练适配器，用学习到的掩码修改中间输出以生成准确的动作条件视频。在电子游戏与真实机器人数据上优于现有扩散模型适配基线，表明若使用得当，预训练视频模型可成为具身 AI 的有力工具。

**要点：**

- **方法：** 不访问预训练参数，用适配器与学习掩码把视频扩散模型改为动作条件世界模型。
- **贡献：** 在电子游戏与真实机器人数据上优于扩散适配基线，显示预训练视频模型可服务决策。
- **关系：** 把视频生成模型变为可模拟动作后果的 `World Model`，服务具身决策（主要为 `WM`）。

---

<a id="p-122"></a>

### 122. Bringing the RT-1-X Foundation Model to a SCARA robot

- **年份：** 2024
- **标签：** `VLM`
- **链接：** [arXiv:2409.03299](https://arxiv.org/abs/2409.03299)

**摘要：** 传统机器人需为每项任务、环境与形态收集专用数据。本研究考察 RT-1-X 机器人基础模型对训练中未见的 UMI-RTX SCARA 机器人的泛化。初始实验显示其无法零样本泛化到该未见机型；但经示范微调后，机器人可学会基础模型中已有、却针对另一机型学习的拾取任务。当面对基础模型包含、微调数据未出现的物体时，仅技能迁移，物体特定知识并未迁移。

**要点：**

- **方法：** 将 RT-1-X 部署到未见的 SCARA 机型，并比较零样本与示范微调。
- **贡献：** 发现零样本无法泛化到新机型，微调可迁移拾取技能，但物体特定知识未随技能一并迁移。
- **关系：** 检验视觉语言动作基础模型跨本体泛化，属 `VLM`/机器人基础模型，非 `World Model` 实验。

---

<a id="p-123"></a>

### 123. CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision

- **年份：** 2024
- **标签：** `intersection`
- **链接：** [arXiv:2411.00508](https://arxiv.org/abs/2411.00508)

**摘要：** 自然语言可作为易用的机器人学习接口。本文研究非专家用自然语言监督采集数据，并直接据此训练策略。提出采集与增强框架，以及 CLIP-RT 这一 `VLA`：适配预训练 CLIP，用对比模仿学习预测基于语言的运动原语；在 Open X-Embodiment 上训练并在框架采集的域内数据上微调。真实评估中以约1B 参数平均成功率高出 OpenVLA 24%；仿真 LIBERO 平均成功率93.1%，推理吞吐163 Hz。

**要点：**

- **方法：** 用自然语言监督采集并增强示范，再以对比模仿学习让 CLIP 预测语言运动原语。
- **贡献：** 在真实操作中以更少参数优于 OpenVLA，并在 LIBERO 上取得高成功率与高吞吐。
- **关系：** 将预训练视觉语言模型 CLIP 转化为语言条件 `VLA` 策略，非 `World Model` 实验。

---

<a id="p-124"></a>

### 124. Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection

- **年份：** 2024
- **标签：** `agent-robot` · `llm-agent` · `VLM`
- **链接：** [arXiv:2412.04455](https://arxiv.org/abs/2412.04455)

**摘要：** Code-as-Monitor（CaM）用 `VLM` 做开集失败的反应式与预防式检测：以约束感知的视觉编程同时在失败后识别，并在可预见失败前预防，服务闭环机器人。

**要点：**

- **方法：** `VLM` 视觉编程生成约束监视器，兼顾反应与预防。
- **贡献：** 开集失败检测同时覆盖已发生与可预见失败。
- **关系：** 代码监视 Agent + `VLM`。

---

<a id="p-125"></a>

### 125. CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation

- **年份：** 2024
- **标签：** `VLA`
- **链接：** [arXiv:2411.19650](https://arxiv.org/abs/2411.19650)

**摘要：** CogACT 在 OpenVLA 一类骨干上增加扩散动作模块，以协同认知（`VLM`）与动作生成。它代表「`VLM` 骨干 + 专门动作头」的 `VLA` 设计，常被 SpatialVLA 等后续引用。

**要点：**

- **方法：** 在 `VLM`/`VLA` 骨干上附加扩散动作模块以协同认知与控制。
- **贡献：** 提升操作中认知理解与动作生成的配合。
- **关系：** `VLA` 架构工作，非工具调用 Agent。

---

<a id="p-126"></a>

### 126. COHERENT: Collaboration of Heterogeneous Multi-Robot System with Large Language Models

- **年份：** 2024
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2409.15146](https://arxiv.org/abs/2409.15146)

**摘要：** 既有 LLM 任务规划多针对单机或同构简单任务。COHERENT 面向四旋翼、机器狗与机械臂等异构团队：中央分配器提出分解方案并分配子任务，各执行器选择可行动作并回报自我反思，经提案—执行—反馈—调整（PEFA）循环直至完成。配套 100 个长时程异构任务基准，成功率与执行效率大幅超过先前方法。

**要点：**

- **方法：** PEFA 循环由中央 LLM 分解分配，异构执行器反馈并调整计划。
- **贡献：** 覆盖四旋翼 / 机器狗 / 机械臂，并发布 100 任务基准，成功与效率明显提升。
- **关系：** 异构多智能体规划 Agent，补充 RoCo / SMART-LLM。

---

<a id="p-127"></a>

### 127. DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models

- **年份：** 2024
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2411.09022](https://arxiv.org/abs/2411.09022)

**摘要：** DART-LLM 做依赖感知的多机器人任务分解与执行：相对 RoCo 的固定机械臂与 SMART-LLM 的非实时代码输出，它显式建模任务依赖并支持更实时的 LLM 推理执行，面向移动多机器人。

**要点：**

- **方法：** LLM 做依赖感知的任务分解，并闭环执行多机器人计划。
- **贡献：** 相对 RoCo / SMART-LLM 更强调依赖与实时执行。
- **关系：** 多智能体规划 Agent。

---

<a id="p-128"></a>

### 128. Diffusion for World Modeling: Visual Details Matter in Atari

- **年份：** 2024
- **标签：** `world_model`
- **链接：** [arXiv:2405.12399](https://arxiv.org/abs/2405.12399)

**摘要：** DIAMOND（Diffusion for World Modeling）表明视觉细节对 Atari 世界模型很重要：用扩散模型作世界模型并在想象中训练 RL 智能体。本包 OSS 已收录其仓库，此处补论文卡片。

**要点：**

- **方法：** 以扩散模型作为世界模型，在想象中训练智能体。
- **贡献：** 强调像素级视觉细节对 Atari `WM` 的作用。
- **关系：** 扩散 `World Model` RL，非语言 Agent。

---

<a id="p-129"></a>

### 129. Diffusion Models Are Real-Time Game Engines

- **年份：** 2024
- **标签：** `world_model`
- **链接：** [arXiv:2408.14837](https://arxiv.org/abs/2408.14837)

**摘要：** GameNGen 表明扩散模型可作实时游戏引擎：在动作条件下交互生成游戏画面，展示交互视频世界模型的实时性。官方可训练栈仍未核验开放，与本包缺口说明一致。

**要点：**

- **方法：** 动作条件扩散实时生成交互游戏帧。
- **贡献：** 展示扩散世界模型作为实时神经游戏引擎的可行性。
- **关系：** 交互视频 `World Model` 地标；官方 OSS 仍缺。

---

<a id="p-130"></a>

### 130. DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning

- **年份：** 2024
- **标签：** `world_model`
- **链接：** [arXiv:2411.04983](https://arxiv.org/abs/2411.04983)

**摘要：** 本文认为世界模型应能在离线轨迹上训练、支持测试时行为优化并做任务无关推理。DINO-WM 不重建视觉世界，而是利用 DINOv2 预训练的空间 patch 特征，通过预测未来 patch 特征从离线行为轨迹学习视觉动态，并将目标特征作为预测对象，经动作序列优化达成观测目标。在六个环境上无需专家示范、奖励建模或预训练逆模型即可零样本规划，在任意迷宫、不同形状物体的推操作及多粒子场景上优于先前工作。

**要点：**

- **方法：** 在 DINOv2 的空间 patch 特征上预测未来特征，离线学习视觉动态并以动作序列优化达成目标。
- **贡献：** 无需专家示范、奖励或逆模型，即可在多样环境上做测试时零样本规划。
- **关系：** 提出任务无关的视觉 `World Model` 规划框架（主要为 `WM`）。

---

<a id="p-131"></a>

### 131. DrivingGPT: Unifying Driving World Modeling and Planning with Multi-modal Autoregressive Transformers

- **年份：** 2024
- **标签：** `world_model`
- **链接：** [arXiv:2412.18607](https://arxiv.org/abs/2412.18607)

**摘要：** 现有驾驶世界模型多依赖视频扩散，擅长视觉生成但难灵活纳入动作等模态。本文把驾驶仿真与轨迹规划统一为序列建模：提出由交错图像与动作 token 构成的多模态驾驶语言，并以标准下一 token 预测训练 DrivingGPT，联合学习世界建模与规划。该方法在动作条件视频生成与端到端规划上表现突出，并在大规模 nuPlan 与 NAVSIM 基准上优于强基线。

**要点：**

- **方法：** 用交错图像与动作 token 的多模态驾驶语言，以自回归 Transformer 做下一 token 预测。
- **贡献：** 在同一模型中联合动作条件视频生成与端到端规划，并在 nuPlan 与 NAVSIM 上优于强基线。
- **关系：** 将 `World Model` 仿真与规划统一为多模态序列建模（主要为驾驶 `WM`）。

---

<a id="p-132"></a>

### 132. DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset

- **年份：** 2024
- **标签：** `VLA`
- **链接：** [arXiv:2403.12945](https://arxiv.org/abs/2403.12945)

**摘要：** DROID 是大规模野外机器人操作数据集，覆盖多样场景与任务，为通用 `VLA` 与世界模型微调提供真实轨迹。Ctrl-World 等后续工作即在其上训练。

**要点：**

- **方法：** 采集大规模野外真实操作轨迹并公开。
- **贡献：** 为通才策略与视频 `World Model` 提供场景多样的真实数据。
- **关系：** `VLA` / `WM` 数据底座，本身不是 Agent 算法。

---

<a id="p-133"></a>

### 133. Embodied AI in Mobile Robots: Coverage Path Planning with Large Language Models

- **年份：** 2024
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2407.02220](https://arxiv.org/abs/2407.02220)

**摘要：** 提出面向移动智能体的 LLM 具身路径规划框架，分层解决高层覆盖路径规划与低层控制：提示 LLM 做覆盖规划，再交给低层执行，用于移动机器人巡检 / 覆盖。

**要点：**

- **方法：** 多层架构用提示 LLM 做覆盖路径规划并接下层控制。
- **贡献：** 把语言规划接到移动覆盖任务。
- **关系：** 移动规划 Agent，近 `VLN` 但强调覆盖。

---

<a id="p-134"></a>

### 134. Enhancing End-to-End Autonomous Driving with Latent World Model

- **年份：** 2024
- **标签：** `world_model`
- **链接：** [arXiv:2406.08481](https://arxiv.org/abs/2406.08481)

**摘要：** 端到端规划器直接使用原始传感器数据，可比传统规划器提取更丰富场景特征并减少信息损失。受自监督表征学习启发，本文提出潜在世界模型 LAW：根据当前场景特征与自车轨迹预测未来场景特征。该自监督任务可无缝接入无感知与基于感知的框架，改善场景特征学习并优化轨迹预测。LAW 在 nuScenes、NAVSIM 与 CARLA 等开环与闭环基准上取得领先性能。

**要点：**

- **方法：** 用潜在世界模型根据当前特征与自车轨迹自监督预测未来场景特征。
- **贡献：** 可接入有或无感知的端到端驾驶框架，并在 nuScenes、NAVSIM 与 CARLA 上取得领先。
- **关系：** 以 Latent `World Model` 增强端到端自动驾驶的场景表征与轨迹预测（主要为 `WM`）。

---

<a id="p-135"></a>

### 135. Genie: Generative Interactive Environments

- **年份：** 2024
- **标签：** `world_model`
- **链接：** [arXiv:2402.15391](https://arxiv.org/abs/2402.15391)

**摘要：** 本文提出 Genie，首个从无标注互联网视频以无监督方式训练的生成式交互环境。可通过文本、合成图、照片甚至草图提示，生成丰富的可动作控制虚拟世界。约11B 参数，由时空视频分词器、自回归动力学模型与可扩展的潜在动作模型组成，被视为基础世界模型。即便训练无真实动作标签，用户仍可逐帧在生成环境中行动；学到的潜在动作空间还可让智能体模仿未见视频中的行为。

**要点：**

- **方法：** 以无标注网络视频无监督训练视频分词器、自回归动力学模型与潜在动作模型。
- **贡献：** 无需真实动作标签即可生成可控制交互世界，并支持从未见视频模仿行为。
- **关系：** 提出可提示、可交互的基础 `World Model`（主要为 `WM`）。

---

<a id="p-136"></a>

### 136. GR-2: A Generative Video-Language-Action Model with Web-Scale Knowledge for Robot Manipulation

- **年份：** 2024
- **标签：** `VLA`
- **链接：** [arXiv:2410.06158](https://arxiv.org/abs/2410.06158)

**摘要：** GR-2 是带网络规模知识的生成式视频—语言—动作模型，用于机器人操作。相对 GR-1，它扩大视频—语言—动作生成能力，作为闭源 / 实验室通才 `VLA` 的重要后续。

**要点：**

- **方法：** 生成式视频—语言—动作模型，融合网络规模视频知识。
- **贡献：** 扩展 GR-1 的操作通才与视频预测能力。
- **关系：** 生成式 `VLA`，含视频世界预测色彩。

---

<a id="p-137"></a>

### 137. Imagination Policy: Using Generative Point Cloud Models for Learning Manipulation Policies

- **年份：** 2024
- **标签：** `world_model`
- **链接：** [arXiv:2406.11740](https://arxiv.org/abs/2406.11740)

**摘要：** Imagination Policy 用生成式点云模型学习操作策略：在想象的三维未来上规划或条件生成动作。它把点云世界预测接到策略，属于 3D `World Model` 服务操作的一条线。

**要点：**

- **方法：** 生成式点云世界预测用于学习操作策略。
- **贡献：** 把三维想象接到操作策略学习。
- **关系：** 3D `World Model` × 操作策略。

---

<a id="p-138"></a>

### 138. IRASim: A Fine-Grained World Model for Robot Manipulation

- **年份：** 2024
- **标签：** `world_model`
- **链接：** [arXiv:2406.14540](https://arxiv.org/abs/2406.14540)

**摘要：** 针对精细机器人—物体交互难以对齐动作与各帧的问题，IRASim 依据历史观测与动作轨迹生成细粒度交互视频：在扩散 Transformer 各块中加入帧级动作条件模块以强化动作—帧对齐。生成质量优于基线并随规模提升；策略评估与真实仿真器高度相关；测试时基于该模型规划可提升策略（Push-T 的 IoU 由0.637 至0.961）；并可用键盘或 VR 控制数据集中的虚拟机械臂。

**要点：**

- **方法：** 用扩散 Transformer 及帧级动作条件模块，按历史观测与动作轨迹生成交互视频。
- **贡献：** 提升细粒度视频质量，策略评估与仿真器相关，模型规划可改进策略并支持交互控制。
- **关系：** 面向机器人操作的细粒度 `World Model`，用于仿真评估与基于模型的规划（主要为 `WM`）。

---

<a id="p-139"></a>

### 139. Jailbreaking LLM-Controlled Robots

- **年份：** 2024
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2410.13691](https://arxiv.org/abs/2410.13691)

**摘要：** 研究越狱攻击 LLM 控制的机器人：把对独立 LLM 的越狱扩展到操作、行走与自动驾驶等身体系统，展示恶意提示如何绕过护栏并诱发有害机器人行为。

**要点：**

- **方法：** 把 LLM 越狱攻击迁移到受 LLM 控制的机器人。
- **贡献：** 实证语言护栏在身体执行上可被绕过。
- **关系：** Agent 安全地标，`VLA` 纯策略不覆盖此类提示攻击。

---

<a id="p-140"></a>

### 140. Large Language Models for Orchestrating Bimanual Robots

- **年份：** 2024
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2404.02018](https://arxiv.org/abs/2404.02018)

**摘要：** 研究用大语言模型编排双臂机器人：在空间与时间上协调双手动作，用语言规划器分配双臂角色与顺序，而不是只学单臂技能。

**要点：**

- **方法：** LLM 编排双臂的时空协调与角色分配。
- **贡献：** 把语言规划从单臂扩展到双臂协调。
- **关系：** 双臂编排 Agent。

---

<a id="p-141"></a>

### 141. Latent Action Pretraining from Videos

- **年份：** 2024
- **标签：** `VLA`
- **链接：** [arXiv:2410.11758](https://arxiv.org/abs/2410.11758)

**摘要：** LAPA（Latent Action Pretraining from Videos）从无动作标注视频中预训练潜在动作，再迁到机器人 `VLA`，降低对大规模动作标注的依赖。

**要点：**

- **方法：** 从视频学习潜在动作表示，再用于 `VLA` 预训练。
- **贡献：** 减少对动作标注轨迹的依赖。
- **关系：** 视频潜在动作 × `VLA`，接近世界 / 动作表征学习。

---

<a id="p-142"></a>

### 142. LLaRA: Supercharging Robot Learning Data for Vision-Language Policy

- **年份：** 2024
- **标签：** `VLA`
- **链接：** [arXiv:2406.20095](https://arxiv.org/abs/2406.20095)

**摘要：** 将预训练 `VLM` 直接用于机器人控制在示范有限时仍困难。LLaRA 把机器人动作策略表述为视觉—文本对话，以便高效把预训练 `VLM` 转化为 `VLA`。首先由已有行为克隆数据自动生成对话式指令微调数据，使动作与图像像素坐标对齐；再以自监督定义六项辅助任务增强数据，无需额外动作标注。少量此类数据微调后即可产生有意义的控制决策，并在多项仿真与真实任务上取得领先，同时保留大语言模型的泛化能力。

**要点：**

- **方法：** 将动作策略写成视觉—文本对话，由行为克隆数据自动构建指令微调并辅以六项自监督任务。
- **贡献：** 在有限示范下把预训练 `VLM` 转为有效 `VLA`，仿真与真实任务上领先并保留泛化。
- **关系：** 用视觉指令微调把 `VLM` 转化为 `VLA` 策略，非 `World Model` 实验。

---

<a id="p-143"></a>

### 143. LLM-Driven Robots Risk Enacting Discrimination, Violence, and Unlawful Actions

- **年份：** 2024
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2406.08824](https://arxiv.org/abs/2406.08824)

**摘要：** 指出 LLM 驱动的机器人可能执行歧视、暴力与违法动作：即便有常识能力，未加约束的语言控制也会把有害文本变成身体伤害。工作强调部署前的规范与过滤。

**要点：**

- **方法：** 分析 LLM 控机器人在歧视、暴力与违法指令上的风险。
- **贡献：** 把社会与法律风险连接到身体执行。
- **关系：** Agent 安全与规范，AutoRT「宪法」的对照文献。

---

<a id="p-144"></a>

### 144. LLM-Personalize: Aligning LLM Planners with Human Preferences via Reinforced Self-Training for Housekeeping Robots

- **年份：** 2024
- **标签：** `llm-agent` · `agent-robot`
- **链接：** [arXiv:2404.14285](https://arxiv.org/abs/2404.14285)

**摘要：** LLM-Personalize 用强化自我训练把 LLM 规划器对齐到人的偏好，使家用或个性化任务计划更符合特定用户，而不是通用常识计划。

**要点：**

- **方法：** 强化自我训练对齐 LLM 规划器与用户偏好。
- **贡献：** 个性化语言规划，而非单一通用计划。
- **关系：** 个性化规划 Agent，近 TidyBot。

---

<a id="p-145"></a>

### 145. LLM3:Large Language Model-based Task and Motion Planning with Motion Failure Reasoning

- **年份：** 2024
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2403.11552](https://arxiv.org/abs/2403.11552)

**摘要：** LLM3 把大语言模型用于任务与运动规划，并纳入运动失败推理：当运动规划失败时用语言推理调整任务计划，形成 TAMP 闭环。

**要点：**

- **方法：** LLM-TAMP 并在运动失败时做语言推理再规划。
- **贡献：** 把运动失败反馈写回任务层。
- **关系：** TAMP Agent。

---

<a id="p-146"></a>

### 146. MALMM: Multi-Agent Large Language Models for Zero-Shot Robotics Manipulation

- **年份：** 2024
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2411.17636](https://arxiv.org/abs/2411.17636)

**摘要：** MALMM 用多智能体大语言模型做零样本机器人操作：针对单次生成长时程计划的幻觉与不适应，用多角色 Agent 分工规划与修正，提高零样本操作规划。

**要点：**

- **方法：** 多智能体 LLM 分工以降低长时程单次计划幻觉。
- **贡献：** 提高零样本操作规划的适应性。
- **关系：** 多智能体操作 Agent。

---

<a id="p-147"></a>

### 147. MapGPT: Map-Guided Prompting with Adaptive Path Planning for Vision-and-Language Navigation

- **年份：** 2024
- **标签：** `VLN`
- **链接：** [arXiv:2401.07314](https://arxiv.org/abs/2401.07314)

**摘要：** 现有零样本 `VLN` 智能体仅提示 GPT-4 在局部环境中选择位置，缺少有效全局视图。MapGPT 引入在线语言形式地图以促进全局探索：将含节点信息与拓扑关系的在线地图写入提示，帮助 GPT 理解空间；并据此提出自适应规划，使智能体基于地图逐步进行多步路径规划、系统探索候选节点或子目标。该方法适用于 GPT-4 与 GPT-4V，在 R2R 与 REVERIE 上同时取得领先零样本性能（成功率约分别提升10%与12%）。

**要点：**

- **方法：** 将在线语言地图（节点与拓扑）写入提示，并做基于地图的自适应多步路径规划。
- **贡献：** 在 GPT-4 与 GPT-4V 上于 R2R 与 REVERIE 取得领先零样本 `VLN` 性能，并显现全局思考能力。
- **关系：** 用 `VLM`/GPT 做地图引导的零样本 `VLN`，未涉及 `World Model` 实验。

---

<a id="p-148"></a>

### 148. Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation

- **年份：** 2024
- **标签：** `VLM`
- **链接：** [arXiv:2401.02117](https://arxiv.org/abs/2401.02117)

**摘要：** 人类示范模仿学习多集中于桌面操作，缺乏通用任务所需的移动性与灵巧性。本文提出低成本全身遥操作系统 Mobile ALOHA，为 ALOHA 增加移动底盘与全身遥操作接口以采集双臂移动操作数据。用监督行为克隆并与已有静态 ALOHA 数据共同训练可提升移动操作；每任务50 条示范时，共训练最高可将成功率提高90%，使系统自主完成炒虾上菜、开双门橱柜存放重锅、呼叫并进入电梯、用水龙头轻冲锅等任务。

**要点：**

- **方法：** 用低成本全身遥操作系统采集双臂移动操作数据，并与静态 ALOHA 数据做监督行为克隆共训练。
- **贡献：** 每任务约50 条示范即可自主完成炒虾上菜、存锅、乘电梯与冲洗锅等复杂移动操作。
- **关系：** 为视觉运动策略提供全身移动操作数据与模仿学习范式，非 `World Model` 实验。

---

<a id="p-149"></a>

### 149. Multi-Modal Grounded Planning and Efficient Replanning For Learning Embodied Agents with A Few Examples

- **年份：** 2024
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2412.17288](https://arxiv.org/abs/2412.17288)

**摘要：** 用少量例子学习具身智能体的多模态接地规划与高效重规划：减少对大量自由语言标注的依赖，在步骤细化时结合多模态接地并在失败后高效重规划。

**要点：**

- **方法：** 少样本多模态接地规划，并做高效重规划。
- **贡献：** 降低复杂任务规划对大规模语言标注的需求。
- **关系：** 少样本接地规划 Agent。

---

<a id="p-150"></a>

### 150. NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models

- **年份：** 2024
- **标签：** `VLN`
- **链接：** [arXiv:2407.12366](https://arxiv.org/abs/2407.12366)

**摘要：** 借助 LLM 进展，用其做指令跟随的机器人导航受到关注，但接入 `VLN` 时智能体表现常明显落后于专用模型，且语言的解释与交流能力未被充分利用。本文在冻结 LLM 中对齐视觉内容以使其理解观测，并将 LLM 与导航策略网络结合，以同时做出有效动作预测与语言化导航推理，从而弥合 `VLN` 专用模型与基于 LLM 的导航范式。方法具有数据效率，并缩小了语言模型智能体与先进 `VLN` 专用模型之间的差距。

**要点：**

- **方法：** 在冻结 LLM 中对齐视觉内容，并将 LLM 与导航策略网络结合以同时预测动作与生成导航推理。
- **贡献：** 提高数据效率，缩小语言模型导航智能体与先进 `VLN` 专用模型的性能差距。
- **关系：** 把 `VLM`/LLM 的语言推理接入 `VLN` 策略，未涉及 `World Model` 实验。

---

<a id="p-151"></a>

### 151. NaVILA: Legged Robot Vision-Language-Action Model for Navigation

- **年份：** 2024
- **标签：** `VLA` · `VLN`
- **链接：** [arXiv:2412.04453](https://arxiv.org/abs/2412.04453)

**摘要：** NaVILA 是腿式机器人的视觉—语言—动作导航模型：高层产生语言导航命令，低层实时运动策略执行。它把 `VLA` 接到四足 / 腿式导航，RSS 2025，开源已核验。

**要点：**

- **方法：** 腿式 `VLA` 输出语言导航命令，再由实时运动策略执行。
- **贡献：** 将 `VLA` 范式扩展到腿式导航。
- **关系：** `VLA` × `VLN`，层次化语言接口类似 Agent 编排。

---

<a id="p-152"></a>

### 152. Octo: An Open-Source Generalist Robot Policy

- **年份：** 2024
- **标签：** `VLA`
- **链接：** [arXiv:2405.12213](https://arxiv.org/abs/2405.12213)

**摘要：** 多样化机器人数据上预训练的大策略，有望仅用少量域内数据微调并广泛泛化，但须适配多样传感器、动作空间与平台。本文提出开源通才操作策略 Octo：基于 Transformer，在 Open X-Embodiment 的 80 万条轨迹上训练，可用语言或目标图像指令，并在消费级 GPU 上数小时内微调到新感知与动作空间。跨 9 个平台实验显示其可作为有效初始化，并做了架构与数据消融。

**要点：**

- **方法：** 基于 Transformer 的通才策略，在 Open X-Embodiment 的 80 万条轨迹上训练，支持语言与目标图像指令，并可微调至新传感器与动作空间。
- **贡献：** 开源通才操作策略，消费级 GPU 数小时即可适配新本体，并在 9 个平台上验证，辅以架构与数据消融。
- **关系：** 面向 `VLA` 的开源初始化与跨平台微调范式，文中未涉及 `World Model` 实验。

---

<a id="p-153"></a>

### 153. OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics

- **年份：** 2024
- **标签：** `agent-robot` · `VLM`
- **链接：** [arXiv:2401.12202](https://arxiv.org/abs/2401.12202)

**摘要：** OK-Robot 问：把开放知识模型（开放词汇检测、语言条件导航与抓取）拼成家用拾取—放置系统，真正重要的是什么。它给出模块化零样本框架，在真实家庭中做语言条件拾放，并分析各模块对成败的贡献。开源仓库已核验。

**要点：**

- **方法：** 模块化组合开放词汇感知、语言导航与抓取，做零样本家用拾放。
- **贡献：** 在真实家庭评测并分析「开放知识集成」的关键因素。
- **关系：** 模块化 Agent / `VLM` 技能编排，而非单一 `VLA`。

---

<a id="p-154"></a>

### 154. On the Vulnerability of LLM/VLM-Controlled Robotics

- **年份：** 2024
- **标签：** `agent-robot` · `llm-agent` · `VLM`
- **链接：** [arXiv:2402.10340](https://arxiv.org/abs/2402.10340)

**摘要：** 分析 LLM / `VLM` 控制机器人的脆弱性：提示攻击、错误接地与不安全输出如何变成危险身体动作，指出语言控制栈与纯策略 `VLA` 不同的攻击面。

**要点：**

- **方法：** 分析 LLM/`VLM` 控机器人的安全脆弱性。
- **贡献：** 把模型安全问题连接到身体执行风险。
- **关系：** Agent 安全，区别于纯 `VLA` 策略风险。

---

<a id="p-155"></a>

### 155. OpenVLA: An Open-Source Vision-Language-Action Model

- **年份：** 2024
- **标签：** `VLA`
- **链接：** [arXiv:2406.09246](https://arxiv.org/abs/2406.09246)

**摘要：** 在互联网视觉-语言数据与多样机器人演示上预训练的策略可微调为稳健 `VLA`，但既有模型多不开放且缺少高效微调。本文提出 70 亿参数开源 `VLA` OpenVLA，在 97 万条真实演示上训练，以 Llama 2 结合融合 DINOv2 与 SigLIP 的视觉编码器。其在 29 项任务与多本体上比闭源 RT-2-X 绝对成功率高 16.5%、参数约少 7 倍，微调后亦优于 Diffusion Policy，并可用低秩适配与量化部署。

**要点：**

- **方法：** Llama 2 加 DINOv2 与 SigLIP 融合视觉编码器，在 97 万条真实机器人演示上训练 70 亿参数开源 `VLA`。
- **贡献：** 开放权重与微调工具；在 29 项任务上比 RT-2-X 高 16.5%，微调后比 Diffusion Policy 高 20.4%，并可用低秩适配与量化部署。
- **关系：** 提供可复现的开源 `VLA` 底座与高效微调路径，文中未涉及 `World Model` 或 `VLN` 实验。

---

<a id="p-156"></a>

### 156. Pandora: Towards General World Model with Natural Language Actions and Video States

- **年份：** 2024
- **标签：** `world_model`
- **链接：** [arXiv:2406.09455](https://arxiv.org/abs/2406.09455)

**摘要：** `World Model` 按动作模拟未来状态，支撑交互内容与长程推理。现有 LLM 受限于语言模态，视频模型又缺可交互动作控制。本文提出 Pandora：混合自回归-扩散模型，以生成视频模拟世界状态，并用自由文本动作实时控制。经大规模预训练与指令微调获得跨域性、一致性与可控性；集成预训练 70 亿 LLM 与视频模型，仅需轻量微调，并展示室内外、自然/城市、人/机器人、2D/3D 等多样输出。

**要点：**

- **方法：** 混合自回归-扩散，集成预训练 LLM 与视频模型，用自由文本动作控制生成视频以模拟世界状态。
- **贡献：** 以轻量微调实现跨域、一致且可控的视频世界模拟，并展示多样场景输出。
- **关系：** 属语言动作条件的通用 `World Model`，为接地长程推理奠基，文中未做 `VLA`/`VLN` 实验。

---

<a id="p-157"></a>

### 157. Physically Embodied Gaussian Splatting: A Realtime Correctable World Model for Robotics

- **年份：** 2024
- **标签：** `world_model`
- **链接：** [arXiv:2406.10788](https://arxiv.org/abs/2406.10788)

**摘要：** 机器人稳健理解并交互物理世界，需要同时刻画几何、物理与视觉的综合表示。本文提出双路 Gaussian-Particle 表示：粒子刻画几何并可配合粒子物理预测合理未来；其上附着 3D Gaussian，经 splatting 渲染视觉状态。对比预测与观测图像产生视觉力，在遵守物理约束下校正粒子。系统以 3 台相机 30Hz 实时运行，并在 2D/3D 跟踪与光度重建上验证。

**要点：**

- **方法：** 粒子几何加物理预测，附着 3D Gaussian 渲染；用预测与观测图像之差产生视觉力以在线校正。
- **贡献：** 可预测未来并在线视觉校正的统一表示，3 相机 30Hz 实时，验证于跟踪与光度重建。
- **关系：** 面向机器人的可校正实时 `World Model`，文中未涉及 `VLA`/`VLN`/`VLM`。

---

<a id="p-158"></a>

### 158. Plan-Seq-Learn: Language Model Guided RL for Solving Long Horizon Robotics Tasks

- **年份：** 2024
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2405.01534](https://arxiv.org/abs/2405.01534)

**摘要：** Plan-Seq-Learn 用语言模型引导强化学习求解长时程机器人任务：LLM 提供计划或子目标序列，RL 在子目标上学习，从而结合语言分解与技能学习。

**要点：**

- **方法：** 语言计划分解 + 序列上的强化学习。
- **贡献：** 提高长时程机器人任务上的 RL 样本效率。
- **关系：** 规划 Agent 指导 RL，非纯 `VLA`。

---

<a id="p-159"></a>

### 159. RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation

- **年份：** 2024
- **标签：** `VLA`
- **链接：** [arXiv:2410.07864](https://arxiv.org/abs/2410.07864)

**摘要：** RDT-1B 是面向双臂操作的十亿级扩散基础模型，用扩散动作头学习双臂协调。它补全 OpenVLA / π₀ 之外的双臂扩散 `VLA` 一线。

**要点：**

- **方法：** 十亿参数扩散基础模型生成双臂动作。
- **贡献：** 为双臂操作提供开源取向的扩散 `VLA`。
- **关系：** 双臂 `VLA` 策略，非规划 Agent。

---

<a id="p-160"></a>

### 160. ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation

- **年份：** 2024
- **标签：** `agent-robot` · `llm-agent` · `VLM`
- **链接：** [arXiv:2409.01652](https://arxiv.org/abs/2409.01652)

**摘要：** ReKep 用关系关键点约束表示操作：约束是把环境中 3D 关键点映射为代价的 Python 函数，再分层优化得到 SE(3) 末端轨迹。`VLM` 与大视觉模型可从语言与 RGB-D 自动生成 ReKep，从而在移动单臂与双臂平台上无任务数据地完成多阶段、野外与双臂行为。

**要点：**

- **方法：** `VLM` 生成 Python 关系关键点约束，优化器求解实时 SE(3) 动作。
- **贡献：** 无任务数据与环境模型即可做多阶段、双臂与野外操作。
- **关系：** 代码约束 Agent + `VLM`，而非端到端 `VLA`。

---

<a id="p-161"></a>

### 161. RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots

- **年份：** 2024
- **标签：** `VLA`
- **链接：** [arXiv:2406.02523](https://arxiv.org/abs/2406.02523)

**摘要：** RoboCasa 提供面向通才机器人的大规模日常任务仿真，支持语言条件家务操作数据生成与评测，常被 `VLA` 与层次化 Agent 用作仿真床。

**要点：**

- **方法：** 大规模日常家务仿真以支持通才机器人学习。
- **贡献：** 为语言条件操作提供可扩展仿真与任务集。
- **关系：** `VLA` / Agent 仿真基础设施。

---

<a id="p-162"></a>

### 162. RoboCodeX: Multimodal Code Generation for Robotic Behavior Synthesis

- **年份：** 2024
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2402.16117](https://arxiv.org/abs/2402.16117)

**摘要：** RoboCodeX 做机器人行为合成的多模态代码生成：从视觉与语言生成可执行行为代码，扩展 Code as Policies 到更强的多模态程序合成。

**要点：**

- **方法：** 多模态代码生成以合成机器人行为程序。
- **贡献：** 把代码即策略扩展到更强的视—语言程序合成。
- **关系：** 代码即策略 Agent。

---

<a id="p-163"></a>

### 163. RoboDreamer: Learning Compositional World Models for Robot Imagination

- **年份：** 2024
- **标签：** `world_model`
- **链接：** [arXiv:2404.12377](https://arxiv.org/abs/2404.12377)

**摘要：** 文本到视频模型可用于机器人决策中的未来动作想象与环境仿真，但泛化受限，难以合成训练时未见过的物体与动作组合。本文提出 RoboDreamer，通过分解视频生成学习组合式 `World Model`：将指令解析为低层原语并分别条件生成。该分解使新指令可写成已见成分的组合，并支持语言与目标图像的多模态目标。方法能在 RT-X 上对未见目标合成视频计划，在仿真中成功执行，并优于单体基线。

**要点：**

- **方法：** 将语言指令解析为低层原语并分解视频生成，支持语言与目标图像的多模态条件。
- **贡献：** 组合式 `World Model` 可对未见物体-动作组合合成计划，在 RT-X 与仿真执行上优于单体基线。
- **关系：** 以组合视频 `World Model` 服务机器人想象与计划，文中未构建 `VLA`/`VLN` 策略。

---

<a id="p-164"></a>

### 164. Robotic Control via Embodied Chain-of-Thought Reasoning

- **年份：** 2024
- **标签：** `agent-robot` · `VLA`
- **链接：** [arXiv:2407.08693](https://arxiv.org/abs/2407.08693)

**摘要：** Embodied Chain-of-Thought（ECoT）让机器人策略在输出动作前生成接地的推理轨迹，把 `VLA` 的端到端控制与 Agent 式思维链结合。实验表明具身推理痕迹可提高复杂指令跟随与可解释性。

**要点：**

- **方法：** 在 `VLA` 中插入具身思维链，先推理再输出动作。
- **贡献：** 提升复杂指令跟随，并使决策更可解释。
- **关系：** 把 ReAct 式推理接入 `VLA` 控制回路。

---

<a id="p-165"></a>

### 165. SELP: Generating Safe and Efficient Task Plans for Robot Agents with Large Language Models

- **年份：** 2024
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2409.19471](https://arxiv.org/abs/2409.19471)

**摘要：** SELP 为机器人智能体生成安全且高效的任务计划。关键是等价投票、约束解码与领域微调，使复杂命令与长时程任务仍遵守用户约束，而不是只追求表面可执行。

**要点：**

- **方法：** 等价投票、约束解码与领域微调以生成安全高效计划。
- **贡献：** 提高长时程语言计划对用户约束的遵守。
- **关系：** 安全规划 Agent。

---

<a id="p-166"></a>

### 166. ShowUI: One Vision-Language-Action Model for GUI Visual Agent

- **年份：** 2024
- **标签：** `VLA`
- **链接：** [arXiv:2411.17465](https://arxiv.org/abs/2411.17465)

**摘要：** 构建 GUI 助手可提升效率，但多数智能体依赖闭源 API 与 HTML 等文本元信息，难以如人感知界面视觉。本文提出数字世界 `VLA` 模型 ShowUI：以 UI 引导视觉 token 选择把截图建模为连通图并剔除冗余；交错视觉-语言-动作流统一导航历史与多轮查询-动作；以及经策展重采样的小规模高质量 GUI 数据。20 亿参数模型用 25.6 万数据达 75.1% 零样本截图接地，并减少 33% 冗余 token、加速 1.4 倍。

**要点：**

- **方法：** UI 引导视觉 token 选择、交错 `VLA` 流与经策展重采样的小规模高质量 GUI 指令数据。
- **贡献：** 20 亿参数模型达 75.1% 零样本截图接地，减少 33% 冗余视觉 token 并加速 1.4 倍，导航实验含 Mind2Web、AITW 与 MiniWob。
- **关系：** 将 `VLA` 拓展到 GUI 视觉智能体与界面导航，文中未涉及 `World Model`。

---

<a id="p-167"></a>

### 167. SPINE: Online Semantic Planning for Missions with Incomplete Natural Language Specifications in Unstructured Environments

- **年份：** 2024
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2410.03035](https://arxiv.org/abs/2410.03035)

**摘要：** SPINE 做在线语义规划，处理非结构化环境中不完整的自然语言任务：无法预建地图时，机器人边建图边推断任务细节，而不是要求任务被完全指定。

**要点：**

- **方法：** 在线建图 + 语义规划以补全不完整自然语言任务。
- **贡献：** 把任务规划从「任务已完全指定」推广到野外不完整指令。
- **关系：** 在线语义规划 Agent，接导航。

---

<a id="p-168"></a>

### 168. TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation

- **年份：** 2024
- **标签：** `intersection`
- **链接：** [arXiv:2409.12514](https://arxiv.org/abs/2409.12514)

**摘要：** `VLA` 在视觉运动控制与指令理解上潜力显著，但推理慢且需大量机器人数据预训练。本文提出紧凑 `VLA` 家族 TinyVLA：推理更快、数据更高效，且无需预训练阶段。以稳健高速多模态模型初始化骨干，微调时接入扩散策略解码器以输出精确动作。仿真与真机评估显示其速度与数据效率显著优于 OpenVLA，性能相当或更好，并在语言、新物体、未见位置、外观、背景与环境变化上泛化强。

**要点：**

- **方法：** 以高速多模态模型初始化骨干，微调时接入扩散策略解码器，无需机器人数据预训练阶段。
- **贡献：** 推理更快、数据更省，仿真与真机上速度与数据效率优于 OpenVLA，泛化相当或更好。
- **关系：** 给出可部署的紧凑 `VLA` 路径，并利用预训练多模态（`VLM` 类）骨干；文中未涉及 `World Model`。

---

<a id="p-169"></a>

### 169. TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies

- **年份：** 2024
- **标签：** `VLA`
- **链接：** [arXiv:2412.10345](https://arxiv.org/abs/2412.10345)

**摘要：** TraceVLA 用视觉轨迹提示增强通才机器人策略的时空意识：在观测上叠加或提示运动痕迹，帮助 `VLA` 理解「怎么动」。

**要点：**

- **方法：** 以视觉轨迹提示增强 `VLA` 的时空感知。
- **贡献：** 提升通才策略对运动过程的意识与操作表现。
- **关系：** `VLA` 输入设计，非规划 Agent。

---

<a id="p-170"></a>

### 170. Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations

- **年份：** 2024
- **标签：** `world_model` · `VLA` · `intersection`
- **链接：** [arXiv:2412.14803](https://arxiv.org/abs/2412.14803)

**摘要：** Video Prediction Policy 用预测性视觉表征训练通才机器人策略：先预测未来视频，再据此生成动作，把视频世界预测接到 `VLA` 式控制。

**要点：**

- **方法：** 以视频预测表征作为通才操作策略的条件。
- **贡献：** 把预测性视觉接到一般操作策略。
- **关系：** `World Model` 式视频预测 × `VLA` 策略。

---

<a id="p-171"></a>

### 171. Vision-and-Language Navigation Today and Tomorrow: A Survey in the Era of Foundation Models

- **年份：** 2024
- **标签：** `VLN`
- **链接：** [arXiv:2407.07035](https://arxiv.org/abs/2407.07035)

**摘要：** 视觉-语言导航（`VLN`）近年受到关注，方法不断涌现；基础模型的成就也重塑了该领域的挑战与路径。本综述提供自上而下的评述，采用具身规划与推理的原则性框架，并强调利用基础模型应对 `VLN` 挑战的现有方法与未来机遇。作者希望一方面里程碑式梳理进展、探讨基础模型的潜在角色，另一方面把 `VLN` 中的不同挑战与解决方案组织给基础模型研究者参考。

**要点：**

- **方法：** 以具身规划与推理为原则框架，自上而下综述基础模型时代的 `VLN` 方法与机遇。
- **贡献：** 梳理 `VLN` 进展与挑战，并向基础模型研究者组织问题与方案。
- **关系：** 定位基础模型（含 `VLM`）如何服务 `VLN`；综述本身不做 `World Model` 或 `VLA` 新实验。

---

<a id="p-172"></a>

### 172. What Matters in Building Vision-Language-Action Models for Generalist Robots

- **年份：** 2024
- **标签：** `VLA`
- **链接：** [arXiv:2412.14058](https://arxiv.org/abs/2412.14058)

**摘要：** 如何把动作注入基础 `VLM` 以构建 `VLA`，关键因素仍不清。本文回答三问：选何种骨干、如何组织 `VLA` 架构、何时加入跨本体数据。据此提出少手工设计的 RoboVLMs 家族，在三个仿真任务与真机上达新 SOTA。实验覆盖 8 个以上 `VLM` 骨干、4 种策略架构与 600 余组设计，并开源灵活框架与配方。

**要点：**

- **方法：** 系统消融 `VLM` 骨干、`VLA` 架构与跨本体数据时机，并给出 RoboVLMs。
- **贡献：** 600 余组实验形成设计指南，仿真与真机达新 SOTA，框架开源。
- **关系：** `VLA` 设计实验，为层次化 Agent 选择低层策略提供依据。

---

<a id="p-173"></a>

### 173. Wonderful Team: Zero-Shot Physical Task Planning with Visual LLMs

- **年份：** 2024
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2407.19094](https://arxiv.org/abs/2407.19094)

**摘要：** Wonderful Team 是多智能体视觉大模型框架，做零样本高层物理任务规划：给定新环境图像与任务描述，输出完成任务所需动作序列，而无需该环境的先验训练。

**要点：**

- **方法：** 多 VLLM 智能体零样本由场景图像生成高层动作序列。
- **贡献：** 新环境无需训练即可做物理任务规划。
- **关系：** 多智能体视觉规划 Agent。

---

<a id="p-174"></a>

### 174. World Model-based Perception for Visual Legged Locomotion

- **年份：** 2024
- **标签：** `world_model`
- **链接：** [arXiv:2409.16784](https://arxiv.org/abs/2409.16784)

**摘要：** 腿式多样地形运动需要本体感觉与视觉的精确感知，但直接从高维视觉学习往往数据低效。教师-学生模仿因信息差距难以最优。本文提出基于 `World Model` 的感知（WMP）：先建环境模型再学策略。尽管完全在仿真中训练，该模型仍能准确预测真实轨迹。仿真与真机实验表明其在可通过性与鲁棒性上优于现有基线。

**要点：**

- **方法：** 先学环境 `World Model`，再基于其预测学习腿式运动策略，而非教师-学生模仿。
- **贡献：** 仿真训练的 `World Model` 可预测真实轨迹，仿真与真机上可通过性与鲁棒性优于基线。
- **关系：** 展示视觉腿式运动中的 `World Model` 感知，文中未涉及 `VLA`/`VLN`/`VLM`。

---

<a id="p-175"></a>

### 175. WorldDreamer: Towards General World Models for Video Generation via Predicting Masked Tokens

- **年份：** 2024
- **标签：** `world_model`
- **链接：** [arXiv:2401.09985](https://arxiv.org/abs/2401.09985)

**摘要：** `World Model` 对预测世界动力学、生成视频至关重要，但现有模型多限于游戏或驾驶。本文提出 WorldDreamer，将世界建模视为无监督视觉序列建模：把视觉映射为离散 token 并预测被掩码者，同时引入多模态提示。实验表明其能在自然场景与驾驶等情境生成视频，并胜任文本到视频、图像到视频与视频编辑。

**要点：**

- **方法：** 将视觉映射为离散 token 并预测掩码 token，辅以多模态提示，做无监督视觉序列式世界建模。
- **贡献：** 面向一般世界物理与运动的视频 `World Model`，支持文/图生视频与视频编辑。
- **关系：** 属通用视频 `World Model`，文中未做 `VLA`/`VLN` 控制实验。

---

<a id="p-176"></a>

### 176. X-MOBILITY: End-To-End Generalizable Navigation via World Modeling

- **年份：** 2024
- **标签：** `world_model`
- **链接：** [arXiv:2410.17491](https://arxiv.org/abs/2410.17491)

**摘要：** 挑战环境下的通用导航仍困难：经典方法需大量调参，学习方法又难泛化到分布外。本文提出端到端可泛化导航模型 X-Mobility：用带潜空间的自回归 `World Model` 刻画动力学；多样多头解码器学习与导航相关的丰富状态；并将世界建模与动作策略解耦，从而融合离/在策略数据。实验表明其超越现有导航方法，并具备零样本 Sim2Real 与跨本体潜力。

**要点：**

- **方法：** 潜空间自回归 `World Model`、多头解码器丰富状态，并将世界建模与动作策略解耦以融合离/在策略数据。
- **贡献：** 端到端可泛化导航，实验上超越现有方法，并展示零样本 Sim2Real 与跨本体潜力。
- **关系：** 以 `World Model` 支撑可泛化导航，文中未构建语言条件 `VLA`/`VLN`。

---

<a id="p-177"></a>

### 177. π₀: A Vision-Language-Action Flow Model for General Robot Control

- **年份：** 2024
- **标签：** `VLA`
- **链接：** [arXiv:2410.24164](https://arxiv.org/abs/2410.24164)

**摘要：** 本文讨论通才机器人策略（机器人基础模型）如何应对数据、泛化与鲁棒性障碍，并提出基于预训练 `VLM` 的流匹配架构以继承互联网规模语义知识。该模型在单臂、双臂与移动操作等多类灵巧机器人平台的大规模多样数据上训练，评估其预训练后的零样本任务能力、对人及高层 `VLM` 策略语言指令的跟随，以及经微调获取新技能的能力，任务涵盖叠衣服、清理桌面与组装纸箱等。

**要点：**

- **方法：** 在预训练 `VLM` 之上构建流匹配架构，并用多平台灵巧机器人多样数据训练。
- **贡献：** 展示零样本执行、跟随语言或高层 `VLM` 指令，以及微调习得叠衣服、清理桌面等新技能。
- **关系：** 以 `VLM` 为语义底座的通用机器人 `VLA` 控制，未涉及 `World Model` 实验。

---

## 2023 年

共 76 篇。先扫目录，再下翻卡片。

- [178. AdaPlanner: Adaptive Planning from Feedback with Language Models](#p-178)  `llm-agent` · `agent-robot`
- [179. An Embodied Generalist Agent in 3D World](#p-179)  `agent-robot` · `VLA` · `VLM` · `llm-agent`
- [180. Bridging Language and Action: A Survey of Language-Conditioned Robot Manipulation](#p-180)  `intersection`
- [181. Building Cooperative Embodied Agents Modularly with Large Language Models](#p-181)  `agent-robot` · `llm-agent`
- [182. Chat with the Environment: Interactive Multimodal Perception Using Large Language Models](#p-182)  `agent-robot` · `llm-agent` · `VLM`
- [183. ChatGPT Empowered Long-Step Robot Control in Various Environments: A Case Application](#p-183)  `agent-robot` · `llm-agent`
- [184. ChatGPT for Robotics: Design Principles and Model Abilities](#p-184)  `agent-robot` · `llm-agent`
- [185. CLIN: A Continually Learning Language Agent for Rapid Task Adaptation and Generalization](#p-185)  `llm-agent` · `agent-robot`
- [186. Collaborating with language models for embodied reasoning](#p-186)  `llm-agent` · `agent-robot`
- [187. CoPAL: Corrective Planning of Robot Actions with Large Language Models](#p-187)  `agent-robot` · `llm-agent`
- [188. Copilot4D: Learning Unsupervised World Models for Autonomous Driving via Discrete Diffusion](#p-188)  `world_model`
- [189. Creative Agents: Empowering Agents with Imagination for Creative Tasks](#p-189)  `agent-robot`
- [190. Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents](#p-190)  `agent-robot` · `llm-agent`
- [191. Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](#p-191)  `VLM`
- [192. DoReMi: Grounding Language Model by Detecting and Recovering from Plan-Execution Misalignment](#p-192)  `agent-robot` · `llm-agent`
- [193. DriveDreamer: Towards Real-world-driven World Models for Autonomous Driving](#p-193)  `world_model`
- [194. EmbodiedGPT: Vision-Language Pre-Training via Embodied Chain of Thought](#p-194)  `agent-robot` · `VLM` · `llm-agent`
- [195. Eureka: Human-Level Reward Design via Coding Large Language Models](#p-195)  `agent-robot` · `llm-agent`
- [196. Foundation Models in Robotics: Applications, Challenges, and the Future](#p-196)  `llm-agent` · `VLM`
- [197. GAIA-1: A Generative World Model for Autonomous Driving](#p-197)  `world_model`
- [198. Ghost in the Minecraft: Generally Capable Agents for Open-World Environments via Large Language Models with Text-based Knowledge and Memory](#p-198)  `agent-robot` · `llm-agent`
- [199. Grounded Decoding: Guiding Text Generation with Grounded Models for Embodied Agents](#p-199)  `agent-robot` · `llm-agent`
- [200. Grounding Large Language Models in Interactive Environments with Online Reinforcement Learning](#p-200)  `llm-agent` · `agent-robot`
- [201. HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face](#p-201)  `llm-agent`
- [202. Instruct2Act: Mapping Multi-modality Instructions to Robotic Actions with Large Language Model](#p-202)  `agent-robot` · `llm-agent`
- [203. JARVIS-1: Open-World Multi-task Agents with Memory-Augmented Multimodal Language Models](#p-203)  `agent-robot` · `llm-agent`
- [204. Language to Rewards for Robotic Skill Synthesis](#p-204)  `agent-robot` · `llm-agent`
- [205. Large Language Models as Commonsense Knowledge for Large-Scale Task Planning](#p-205)  `llm-agent` · `agent-robot`
- [206. Large Language Models as Generalizable Policies for Embodied Tasks](#p-206)  `llm-agent` · `agent-robot`
- [207. Large Language Models for Robotics: A Survey](#p-207)  `VLM`
- [208. Learning Interactive Real-World Simulators](#p-208)  `world_model`
- [209. LGMCTS: Language-Guided Monte-Carlo Tree Search for Executable Semantic Object Rearrangement](#p-209)  `agent-robot` · `llm-agent`
- [210. LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](#p-210)  `VLA`
- [211. LLM as A Robotic Brain: Unifying Egocentric Memory and Control](#p-211)  `agent-robot` · `llm-agent`
- [212. LLM+P: Empowering Large Language Models with Optimal Planning Proficiency](#p-212)  `llm-agent`
- [213. LLM-BRAIn: AI-driven Fast Generation of Robot Behaviour Tree based on Large Language Model](#p-213)  `agent-robot` · `llm-agent`
- [214. LLM-State: Open World State Representation for Long-horizon Task Planning with Large Language Model](#p-214)  `agent-robot` · `llm-agent`
- [215. Look Before You Leap: Unveiling the Power of GPT-4V in Robotic Vision-Language Planning](#p-215)  `agent-robot` · `llm-agent` · `VLM`
- [216. March in Chat: Interactive Prompting for Remote Embodied Referring Expression](#p-216)  `VLN` · `llm-agent`
- [217. Mastering Diverse Domains through World Models](#p-217)  `VLM` · `world_model`
- [218. NavGPT: Explicit Reasoning in Vision-and-Language Navigation with Large Language Models](#p-218)  `VLN`
- [219. Navigation with Large Language Models: Semantic Guesswork as a Heuristic for Planning](#p-219)  `VLN`
- [220. OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving](#p-220)  `world_model`
- [221. Octopus: Embodied Vision-Language Programmer from Environmental Feedback](#p-221)  `agent-robot` · `llm-agent` · `VLM`
- [222. Open X-Embodiment: Robotic Learning Datasets and RT-X Models](#p-222)  `intersection`
- [223. PaLM-E: An Embodied Multimodal Language Model](#p-223)  `VLM`
- [224. Prompt a Robot to Walk with Large Language Models](#p-224)  `agent-robot` · `llm-agent`
- [225. Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions](#p-225)  `VLM`
- [226. REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction](#p-226)  `agent-robot` · `llm-agent`
- [227. Reflexion: Language Agents with Verbal Reinforcement Learning](#p-227)  `llm-agent`
- [228. RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation](#p-228)  `VLM`
- [229. RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation](#p-229)  `agent-robot` · `llm-agent`
- [230. RoboGPT: an intelligent agent of making embodied long-term decisions for daily instruction tasks](#p-230)  `agent-robot` · `llm-agent`
- [231. RoCo: Dialectic Multi-Robot Collaboration with Large Language Models](#p-231)  `agent-robot` · `llm-agent`
- [232. RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](#p-232)  `VLA`
- [233. RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches](#p-233)  `VLA`
- [234. SayCanPay: Heuristic Planning with Large Language Models using Learnable Domain Knowledge](#p-234)  `agent-robot` · `llm-agent`
- [235. SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning](#p-235)  `VLM`
- [236. Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture](#p-236)  `world_model`
- [237. Skill Reinforcement Learning and Planning for Open-World Long-Horizon Tasks](#p-237)  `agent-robot` · `llm-agent`
- [238. SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models](#p-238)  `agent-robot` · `llm-agent`
- [239. Statler: State-Maintaining Language Models for Embodied Reasoning](#p-239)  `agent-robot` · `llm-agent`
- [240. STEVE-1: A Generative Model for Text-to-Behavior in Minecraft](#p-240)  `agent-robot` · `llm-agent`
- [241. STORM: Efficient Stochastic Transformer based World Models for Reinforcement Learning](#p-241)  `world_model`
- [242. Task and Motion Planning with Large Language Models for Object Rearrangement](#p-242)  `agent-robot` · `llm-agent`
- [243. Text2Motion: From Natural Language Instructions to Feasible Plans](#p-243)  `agent-robot` · `llm-agent`
- [244. TidyBot: Personalized Robot Assistance with Large Language Models](#p-244)  `agent-robot` · `llm-agent`
- [245. Toward General-Purpose Robots via Foundation Models: A Survey and Meta-Analysis](#p-245)  `llm-agent` · `VLA`
- [246. Towards Learning a Generalist Model for Embodied Navigation](#p-246)  `VLN`
- [247. Transformer-based World Models Are Happy With 100k Interactions](#p-247)  `world_model`
- [248. Translating Natural Language to Planning Goals with Large-Language Models](#p-248)  `llm-agent`
- [249. Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation](#p-249)  `VLA`
- [250. ViNT: A Foundation Model for Visual Navigation](#p-250)  `VLN`
- [251. Vision-Language Foundation Models as Effective Robot Imitators](#p-251)  `intersection`
- [252. VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](#p-252)  `agent-robot` · `llm-agent`
- [253. Voyager: An Open-Ended Embodied Agent with Large Language Models](#p-253)  `agent-robot` · `llm-agent`

<a id="p-178"></a>

### 178. AdaPlanner: Adaptive Planning from Feedback with Language Models

- **年份：** 2023
- **标签：** `llm-agent` · `agent-robot`
- **链接：** [arXiv:2305.16653](https://arxiv.org/abs/2305.16653)

**摘要：** 多数 LLM 智能体要么贪心无规划，要么静态计划不适应反馈，随问题变复杂而退化。AdaPlanner 根据环境反馈自适应改写计划，使顺序决策在更长时程上保持可修正。

**要点：**

- **方法：** 由环境反馈自适应改写语言模型计划。
- **贡献：** 缓解静态计划在长时程上的退化。
- **关系：** ReAct 式自适应规划 Agent。

---

<a id="p-179"></a>

### 179. An Embodied Generalist Agent in 3D World

- **年份：** 2023
- **标签：** `agent-robot` · `VLA` · `VLM` · `llm-agent`
- **链接：** [arXiv:2311.12871](https://arxiv.org/abs/2311.12871)

**摘要：** 现有通用模型多依赖二维图像，对三维输入与三维世界中定义的任务（接地、具身推理与行动）能力有限。LEO 是面向三维世界的具身多模态通才智能体，统一任务接口、架构与目标，分两阶段训练：三维视觉—语言对齐，再做三维视觉—语言—动作（`VLA`）指令微调。作者收集物体级与场景级大规模数据，并用 LLM 辅助管线生成高质量三维视觉—语言数据。实验覆盖三维描述、问答、具身推理、导航与操作；消融与缩放分析为后续具身通才提供参照。代码与数据见项目页。

**要点：**

- **方法：** 两阶段训练——3D 视觉—语言对齐 + 3D `VLA` 指令微调；统一接口，并以 LLM 辅助生成 3D VL 数据。
- **贡献：** 在三维描述、问答、具身推理、导航与操作上展示通才能力，并给出消融与缩放分析。
- **关系：** 研究员包标为具身 LLM Agent；同时是 3D `VLM` / `VLA` 通才。

---

<a id="p-180"></a>

### 180. Bridging Language and Action: A Survey of Language-Conditioned Robot Manipulation

- **年份：** 2023
- **标签：** `intersection`
- **链接：** [arXiv:2312.10807](https://arxiv.org/abs/2312.10807)

**摘要：** 语言条件机器人操作旨在让机器人理解并执行自然语言指令，以实现人机沟通与协作；该交叉领域融合场景理解、语言处理与策略学习。本综述系统梳理近期进展，按语言接入方式分类：语言用于状态评估、作为策略条件、用于认知规划与推理，以及统一视觉-语言-动作模型。进一步从动作粒度、数据与监督、系统成本与延迟、环境与评测、任务规格五轴分析现有技术，并归纳关键争论。最后讨论开放挑战与未来方向，聚焦提升泛化与应对安全问题。

**要点：**

- **方法：** 按语言接入方式分类并沿五轴分析语言条件操作方法，含统一 `VLA`。
- **贡献：** 系统综述进展、争论与开放挑战，并指向泛化与安全。
- **关系：** 把统一 `VLA` 作为语言接入的一类；综述本身不提出新的 `World Model` 实验。

---

<a id="p-181"></a>

### 181. Building Cooperative Embodied Agents Modularly with Large Language Models

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2307.02485](https://arxiv.org/abs/2307.02485)

**摘要：** CoELA 针对分散控制、原始感知、有代价通信与多目标任务，把 LLM 嵌入感知、记忆、通信、规划与执行五个模块。在 C-WAH 与 TDW-MAT 上，GPT-4 驱动的 CoELA 超过强规划基线并出现有效通信；对 LLaMA-2 微调的 CoLLAMA 也取得可行表现，人机协作中自然语言通信更获信任。

**要点：**

- **方法：** 模块化认知架构把 LLM 用于通信与规划，形成合作具身语言智能体。
- **贡献：** 分散多智体合作超过规划基线，并展示人机自然语言协作。
- **关系：** 多智能体机器人 / 具身合作 Agent 地标。

---

<a id="p-182"></a>

### 182. Chat with the Environment: Interactive Multimodal Perception Using Large Language Models

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent` · `VLM`
- **链接：** [arXiv:2303.08268](https://arxiv.org/abs/2303.08268)

**摘要：** 少样本 LLM 规划强，但把多模态感知与连续动作接地仍难。本文让机器人与环境「对话」：用交互式多模态感知把传感结果写成语言，再交给 LLM 推理，从而在复杂世界中闭环交互。

**要点：**

- **方法：** 交互式多模态感知把观测转为语言，与 LLM 对话式规划。
- **贡献：** 缓解 LLM 在连续感知—动作上的接地困难。
- **关系：** `VLM` 感知 + 语言 Agent 控制。

---

<a id="p-183"></a>

### 183. ChatGPT Empowered Long-Step Robot Control in Various Environments: A Case Application

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2304.03893](https://arxiv.org/abs/2304.03893)

**摘要：** 案例研究展示少样本 ChatGPT 把自然语言转为可执行机器人动作序列，并给出易定制、易接入执行系统、可迁移多环境的提示设计，同时尽量降低 ChatGPT 幻觉对控制的影响。

**要点：**

- **方法：** 定制少样本提示，将指令译为可接入执行系统的动作序列。
- **贡献：** 给出跨环境长步骤机器人控制的工程案例。
- **关系：** 代码 / 动作序列 Agent，近 ChatGPT for Robotics。

---

<a id="p-184"></a>

### 184. ChatGPT for Robotics: Design Principles and Model Abilities

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2306.17582](https://arxiv.org/abs/2306.17582)

**摘要：** ChatGPT for Robotics 总结用对话式 LLM 设计机器人应用的原则：提示中暴露高层 API、用语言做任务分解与代码生成，并在多种机器人平台上演示。论文讨论模型能力、安全与人机协作，是工业界早期「对话 Agent 控制机器人」的系统设计报告。

**要点：**

- **方法：** 以高层 API 提示 ChatGPT 做任务分解与控制代码生成。
- **贡献：** 给出跨平台机器人对话应用的设计原则与能力观察。
- **关系：** 对话 Agent 控制机器人的工程地标，非 `VLA` 权重模型。

---

<a id="p-185"></a>

### 185. CLIN: A Continually Learning Language Agent for Rapid Task Adaptation and Generalization

- **年份：** 2023
- **标签：** `llm-agent` · `agent-robot`
- **链接：** [arXiv:2310.10134](https://arxiv.org/abs/2310.10134)

**摘要：** CLIN 是持续学习的语言智能体，强调快速任务适应与泛化：在新任务上用语言记忆积累经验，而不必每次从零提示，从而加速适应。

**要点：**

- **方法：** 持续学习语言智能体积累任务经验以快速适应。
- **贡献：** 提高语言 Agent 在新任务上的适应与泛化。
- **关系：** 持续学习规划 Agent。

---

<a id="p-186"></a>

### 186. Collaborating with language models for embodied reasoning

- **年份：** 2023
- **标签：** `llm-agent` · `agent-robot`
- **链接：** [arXiv:2302.00763](https://arxiv.org/abs/2302.00763)

**摘要：** 复杂模糊环境中的推理是强化学习难点：强 RL 智能体数据饥渴且难泛化，而大规模语言模型推理与适应强。本文研究与语言模型协作做具身推理，把 LLM 常识接到交互环境中的决策。

**要点：**

- **方法：** 让语言模型与具身智能体协作完成环境中的推理。
- **贡献：** 探索用 LLM 补 RL 在新环境、新任务上的泛化。
- **关系：** 具身推理 Agent，非 `VLA` 策略。

---

<a id="p-187"></a>

### 187. CoPAL: Corrective Planning of Robot Actions with Large Language Models

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2310.07263](https://arxiv.org/abs/2310.07263)

**摘要：** CoPAL 用大语言模型做机器人动作的纠正规划：在执行偏差或失败后重新生成修正计划，强调纠正而非一次性开环计划。

**要点：**

- **方法：** LLM 对机器人动作做纠正式再规划。
- **贡献：** 把失败后的纠正规划显式化。
- **关系：** 纠正规划 Agent。

---

<a id="p-188"></a>

### 188. Copilot4D: Learning Unsupervised World Models for Autonomous Driving via Discrete Diffusion

- **年份：** 2023
- **标签：** `world_model`
- **链接：** [arXiv:2311.01017](https://arxiv.org/abs/2311.01017)

**摘要：** 无监督 `World Model` 可教智能体理解世界，但自动驾驶上规模化慢于 GPT。瓶颈是复杂非结构化观测与可扩展生成模型。本文提出 Copilot4D：VQVAE 离散化观测后以离散扩散预测未来，并把 Masked Generative Image Transformer 改写为可并行去噪。点云上 NuScenes、KITTI Odometry 与 Argoverse2 的 1s Chamfer 距离降逾 65%、3s 降逾 50%。

**要点：**

- **方法：** VQVAE 将观测离散化，再以改进的离散扩散（由 Masked Generative Image Transformer 改写）并行预测未来。
- **贡献：** 点云 `World Model` 在三个驾驶数据集上显著降低短时 Chamfer 距离。
- **关系：** 为自动驾驶提供可扩展无监督 `World Model`，文中未涉及 `VLA`/`VLN`/`VLM`。

---

<a id="p-189"></a>

### 189. Creative Agents: Empowering Agents with Imagination for Creative Tasks

- **年份：** 2023
- **标签：** `agent-robot`
- **链接：** [arXiv:2312.02519](https://arxiv.org/abs/2312.02519)

**摘要：** Creative Agents 研究开放式创造任务：用想象器把抽象语言变成具体目标（文本或扩散视觉想象），再由行为克隆或代码基础模型执行。在 Minecraft 生存模式中，智能体可按自由语言建造多样建筑，并用 GPT-4V 评估开放创造。

**要点：**

- **方法：** 想象器（LLM 或扩散）生成任务结果，再交给控制策略或代码模型。
- **贡献：** 据称首次在生存模式完成多样建筑创造，并开源评测。
- **关系：** 开放式创造 Agent；视觉想象接近 `World Model` 用途。

---

<a id="p-190"></a>

### 190. Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2302.01560](https://arxiv.org/abs/2302.01560)

**摘要：** 开放世界多任务规划面临长时程推理与计划不可执行的难题。DEPS（Describe, Explain, Plan and Select）用交互式规划：描述当前处境、解释失败、生成计划并选择可执行技能。在 Minecraft 中，该方法显著提高长时程任务完成率，成为 Voyager 之前的开放世界规划 Agent 代表。

**要点：**

- **方法：** 描述—解释—规划—选择的交互式 LLM 规划，把失败反馈写入下一轮。
- **贡献：** 在 Minecraft 长时程多任务上提高计划可执行性与完成率。
- **关系：** 开放世界规划 Agent，技能选择接口可接到控制器而非 `VLA`。

---

<a id="p-191"></a>

### 191. Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

- **年份：** 2023
- **标签：** `VLM`
- **链接：** [arXiv:2303.04137](https://arxiv.org/abs/2303.04137)

**摘要：** 本文提出 Diffusion Policy，将机器人视觉运动策略表示为条件去噪扩散过程。在 4 个基准的 12 项任务上平均优于现有方法 46.9%。它学习动作分布分数函数梯度，推理时经随机 Langevin 动力学逐步优化，能处理多模态与高维动作并训练稳定。为用于真机，还引入滚动时域控制、视觉条件与时间序列扩散 Transformer。

**要点：**

- **方法：** 将视觉运动策略建模为条件去噪扩散，结合滚动时域控制、视觉条件与时间序列扩散 Transformer。
- **贡献：** 在 12 项操作任务上平均优于现有方法 46.9%，并具备多模态、高维动作与训练稳定优势。
- **关系：** 属视觉条件动作生成，可服务视觉运动策略；文中未涉及 `World Model` 或 `VLN`，亦未自称 `VLA`。

---

<a id="p-192"></a>

### 192. DoReMi: Grounding Language Model by Detecting and Recovering from Plan-Execution Misalignment

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2307.00329](https://arxiv.org/abs/2307.00329)

**摘要：** DoReMi 通过检测并恢复计划—执行错位来接地语言模型：当执行偏离计划时触发恢复，而不是继续开环执行错误计划，从而提高语言计划在机器人上的可靠性。

**要点：**

- **方法：** 检测计划与执行的错位并触发恢复以接地 LLM。
- **贡献：** 降低开环语言计划在真机上的漂移。
- **关系：** 闭环接地 Agent。

---

<a id="p-193"></a>

### 193. DriveDreamer: Towards Real-world-driven World Models for Autonomous Driving

- **年份：** 2023
- **标签：** `world_model`
- **链接：** [arXiv:2309.09777](https://arxiv.org/abs/2309.09777)

**摘要：** `World Model` 在自动驾驶中因能理解环境而受关注，但既有研究多聚焦游戏或仿真。本文提出完全源于真实驾驶的 DriveDreamer：用扩散模型构建复杂环境表示，并两阶段训练——先理解结构化交通约束，再预测未来状态。这是首个基于真实驾驶场景的 `World Model`。在 nuScenes 上验证其能精确可控地生成忠实于交通结构的视频，并生成现实合理的驾驶策略。

**要点：**

- **方法：** 以扩散模型表征复杂驾驶环境，两阶段先学交通约束再预测未来状态，数据全部来自真实驾驶。
- **贡献：** 首个完全源于真实驾驶场景的 `World Model`，在 nuScenes 上实现可控视频生成与合理驾驶策略。
- **关系：** 属真实驾驶 `World Model`，文中未涉及 `VLA`/`VLN`/`VLM`。

---

<a id="p-194"></a>

### 194. EmbodiedGPT: Vision-Language Pre-Training via Embodied Chain of Thought

- **年份：** 2023
- **标签：** `agent-robot` · `VLM` · `llm-agent`
- **链接：** [arXiv:2305.15021](https://arxiv.org/abs/2305.15021)

**摘要：** EmbodiedGPT 是面向具身人工智能的端到端多模态基础模型，用具身思维链做视觉—语言预训练，使智能体具备多模态理解与规划执行能力。模型在具身规划、视觉问答与操作相关基准上提升，展示把 `VLM` 预训练接到动作序列的路径。

**要点：**

- **方法：** 以具身思维链做视觉—语言预训练，端到端赋能规划与执行。
- **贡献：** 在具身规划、VQA 与操作相关任务上提升多模态基础能力。
- **关系：** `VLM` Agent 预训练，通向规划式控制而非纯 `World Model`。

---

<a id="p-195"></a>

### 195. Eureka: Human-Level Reward Design via Coding Large Language Models

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2310.12931](https://arxiv.org/abs/2310.12931)

**摘要：** Eureka 用编码 LLM 做人类水平的奖励设计：在仿真中进化可执行奖励函数，覆盖 29 个机器人任务，并达到与人类奖励相当或更好的表现。它把「写奖励代码」作为 Agent 技能，用于训练低层控制器，开源代码已核验。

**要点：**

- **方法：** 编码 LLM 进化可执行奖励函数，在仿真中训练机器人技能。
- **贡献：** 在 29 个任务上达到人类水平奖励设计。
- **关系：** 奖励代码 Agent 间接控制机器人学习，非在线 `VLA`。

---

<a id="p-196"></a>

### 196. Foundation Models in Robotics: Applications, Challenges, and the Future

- **年份：** 2023
- **标签：** `llm-agent` · `VLM`
- **链接：** [arXiv:2312.07843](https://arxiv.org/abs/2312.07843)

**摘要：** 综述机器人中的基础模型：应用、挑战与未来，覆盖语言、视觉与控制接口，为 Agent / `VLA` / `VLM` 交叉提供早期全景。

**要点：**

- **方法：** 综述基础模型在机器人中的应用与挑战。
- **贡献：** 梳理早期基础模型机器人路线与开放问题。
- **关系：** 交叉综述，本身无新控制实验。

---

<a id="p-197"></a>

### 197. GAIA-1: A Generative World Model for Autonomous Driving

- **年份：** 2023
- **标签：** `world_model`
- **链接：** [arXiv:2309.17080](https://arxiv.org/abs/2309.17080)

**摘要：** GAIA-1 是面向自动驾驶的生成式世界模型，用视频、文本与动作预测未来驾驶场景。它展示基础模型尺度的驾驶世界模拟，但官方代码与权重未开放，是本包诚实标注的闭源 `World Model` 地标。

**要点：**

- **方法：** 以视频、文本与动作为条件的生成式驾驶世界模型。
- **贡献：** 展示可提示、可动作条件的驾驶未来预测。
- **关系：** 驾驶 `World Model` 地标；官方栈未开放。

---

<a id="p-198"></a>

### 198. Ghost in the Minecraft: Generally Capable Agents for Open-World Environments via Large Language Models with Text-based Knowledge and Memory

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2305.17144](https://arxiv.org/abs/2305.17144)

**摘要：** Ghost in the Minecraft（GITM）针对开放世界一般能力，而非单一「获得钻石」。它用 LLM 做层次化规划与结构化文本接口，把 Minecraft 交互表示为可推理的文本世界，从而在广泛任务上取得一般能力。相对目标单一的智能体，GITM 更强调开放任务覆盖与规划—执行分解。

**要点：**

- **方法：** 以 LLM 层次化规划与结构化文本接口操作 Minecraft。
- **贡献：** 面向开放世界一般能力，而非单一钻石目标。
- **关系：** 与 Voyager 并列的开放式 Agent，文本接口控制具身环境。

---

<a id="p-199"></a>

### 199. Grounded Decoding: Guiding Text Generation with Grounded Models for Embodied Agents

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2303.00855](https://arxiv.org/abs/2303.00855)

**摘要：** LLM 缺物理经验、难解析非语言观测、也不知奖励与安全约束。Grounded Decoding 在解码时用接地模型引导文本生成，使具身智能体的语言计划遵守感知、奖励与安全，而不是纯自由生成。

**要点：**

- **方法：** 解码阶段用接地模型约束 LLM 文本生成。
- **贡献：** 把互联网知识接到具身约束下的可执行语言。
- **关系：** SayCan 一线的接地生成 Agent。

---

<a id="p-200"></a>

### 200. Grounding Large Language Models in Interactive Environments with Online Reinforcement Learning

- **年份：** 2023
- **标签：** `llm-agent` · `agent-robot`
- **链接：** [arXiv:2302.02662](https://arxiv.org/abs/2302.02662)

**摘要：** LLM 对世界物理的抽象知识可用于决策，但与环境对齐不足会限制功能能力。GLAM 通过在线强化学习做功能接地，使智能体在交互中对齐语言模型知识与环境，提升可执行能力。

**要点：**

- **方法：** 用在线强化学习对 LLM 做功能接地（GLAM）。
- **贡献：** 缩小语言模型知识与交互环境之间的错位。
- **关系：** 接地规划 Agent，非学得 `World Model`。

---

<a id="p-201"></a>

### 201. HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face

- **年份：** 2023
- **标签：** `llm-agent`
- **链接：** [arXiv:2303.17580](https://arxiv.org/abs/2303.17580)

**摘要：** HuggingGPT 用 ChatGPT 作控制器，调度 Hugging Face 上的专家模型完成跨域跨模态任务：LLM 负责任务规划、模型选择、参数生成与结果汇总。该工作展示工具使用 Agent 如何把语言计划接到可调用技能库，为机器人 tool-use 提供非具身对照。

**要点：**

- **方法：** 以 LLM 规划并调度外部专家模型，完成跨模态任务。
- **贡献：** 展示工具使用 Agent 的规划—选模型—执行—汇总回路。
- **关系：** 工具使用规划 Agent 地标，本身不是机器人或 `VLA` 实验。

---

<a id="p-202"></a>

### 202. Instruct2Act: Mapping Multi-modality Instructions to Robotic Actions with Large Language Model

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2305.11176](https://arxiv.org/abs/2305.11176)

**摘要：** Instruct2Act 用 LLM 把多模态指令映射为机器人顺序动作：生成调用 SAM、CLIP 等感知工具与操作原语的 Python 程序。框架保留专家技能接口，同时利用 LLM 的零样本多模态推理，在表格操作等任务上实现灵活的指令跟随。

**要点：**

- **方法：** LLM 生成调用 SAM/CLIP 与操作原语的程序，映射多模态指令。
- **贡献：** 在保留专家技能的同时实现灵活的零样本指令跟随。
- **关系：** 代码即策略 + 视觉工具使用的机器人 Agent。

---

<a id="p-203"></a>

### 203. JARVIS-1: Open-World Multi-task Agents with Memory-Augmented Multimodal Language Models

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2311.05997](https://arxiv.org/abs/2311.05997)

**摘要：** JARVIS-1 是开放世界多任务 Minecraft 智能体：多模态语言模型把视觉与指令映射为计划，再交给目标条件控制器，并用多模态记忆结合预训练知识与生存经验。它可完成 200 余项任务，短时程近乎完美；在获得钻石镐上可靠性约为先前 SOTA 的 5 倍。

**要点：**

- **方法：** 多模态 LLM 规划 + 目标条件控制 + 多模态记忆。
- **贡献：** 覆盖 200+ 任务，钻石镐任务可靠性约 5 倍于先前 SOTA。
- **关系：** Voyager 之后的多模态开放式 Agent。

---

<a id="p-204"></a>

### 204. Language to Rewards for Robotic Skill Synthesis

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2306.08647](https://arxiv.org/abs/2306.08647)

**摘要：** Language to Rewards 让用户用自然语言描述想要的机器人技能，LLM 生成奖励代码，再在仿真中用强化学习优化低层控制器。该「语言→奖励程序→RL」回路可合成新的运动技能，展示代码生成 Agent 对控制器训练的间接控制。

**要点：**

- **方法：** LLM 把语言技能描述编译为奖励程序，再用强化学习训练控制器。
- **贡献：** 用语言合成新运动技能，形成可迭代的奖励设计回路。
- **关系：** 代码 / 奖励设计 Agent，控制的是训练目标而非在线 `VLA`。

---

<a id="p-205"></a>

### 205. Large Language Models as Commonsense Knowledge for Large-Scale Task Planning

- **年份：** 2023
- **标签：** `llm-agent` · `agent-robot`
- **链接：** [arXiv:2305.14078](https://arxiv.org/abs/2305.14078)

**摘要：** 大规模任务规划极难。本文表明 LLM 既可当策略，也可提供常识世界模型，二者可在蒙特卡洛树搜索中结合以扩展规划规模。相对直接把 LLM 当策略，搜索式组合更能放大常识。

**要点：**

- **方法：** 把 LLM 常识世界模型与策略嵌入 MCTS 做大规模任务规划。
- **贡献：** 展示 LLM 可作为可搜索的常识模型而不只是贪心策略。
- **关系：** LLM 当符号世界模型 + 规划 Agent。

---

<a id="p-206"></a>

### 206. Large Language Models as Generalizable Policies for Embodied Tasks

- **年份：** 2023
- **标签：** `llm-agent` · `agent-robot`
- **链接：** [arXiv:2310.17722](https://arxiv.org/abs/2310.17722)

**摘要：** 本文将大语言模型作为具身任务的可泛化策略：不只生成文本计划，而把 LLM 直接或经适配当作跨任务的决策策略，探索语言先验在具身策略中的迁移。

**要点：**

- **方法：** 把 LLM 当作可泛化的具身任务策略。
- **贡献：** 检验语言先验作为跨任务策略的能力。
- **关系：** LLM 策略 / Agent，介于规划与策略之间。

---

<a id="p-207"></a>

### 207. Large Language Models for Robotics: A Survey

- **年份：** 2023
- **标签：** `VLM`
- **链接：** [arXiv:2311.07226](https://arxiv.org/abs/2311.07226)

**摘要：** 人类借多模态反馈学习并控制复杂操作的能力可称为灵巧智能。随着 LLM 迅速发展，其在机器人中的应用日益受关注。本综述总结 LLM 对机器人控制、感知、决策与规划的影响；回顾背景、收益与近期模型，梳理感知、决策、控制、交互及跨模块协调技术，并指出近期挑战。作者认为基于 LLM 的机器人是通往具身智能最有前景亦最具挑战的路径之一。

**要点：**

- **方法：** 综述 LLM 在机器人感知、决策、控制、交互与跨模块协调中的技术与模型。
- **贡献：** 梳理背景、收益、应用与近期挑战，并将基于 LLM 的机器人定位为具身智能的重要路径。
- **关系：** 讨论语言基础模型如何服务机器人感知与规划（与 `VLM` 相关）；综述本身不做 `World Model` 新实验。

---

<a id="p-208"></a>

### 208. Learning Interactive Real-World Simulators

- **年份：** 2023
- **标签：** `world_model`
- **链接：** [arXiv:2310.06114](https://arxiv.org/abs/2310.06114)

**摘要：** 生成模型已变革文本、图像与视频创作；下一里程碑或是按人类与机器人动作模拟真实体验。本文探索通过生成建模学习通用真实交互模拟器 UniSim：编排在物体、动作密度与运动多样性上各有所长的自然数据，即可由静态场景模拟高层指令与低层控制的视觉结果。用其训练的高层视觉-语言策略与低层强化学习策略，均可纯仿真训练后零样本部署到现实。

**要点：**

- **方法：** 编排多源自然数据，以生成建模学习可响应高层指令与低层控制的通用真实交互模拟器 UniSim。
- **贡献：** 仿真中训练的视觉-语言策略与强化学习策略可零样本部署到现实，视频描述等任务也可受益。
- **关系：** 交互式 `World Model` 可训练视觉-语言策略；文中未构建完整 `VLA`/`VLN` 系统。

---

<a id="p-209"></a>

### 209. LGMCTS: Language-Guided Monte-Carlo Tree Search for Executable Semantic Object Rearrangement

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2309.15821](https://arxiv.org/abs/2309.15821)

**摘要：** LGMCTS 用语言引导蒙特卡洛树搜索，做可执行的语义物体重排：在搜索中纳入语言语义，使重排计划既可执行又符合指令语义。

**要点：**

- **方法：** 语言引导的 MCTS 搜索可执行语义重排。
- **贡献：** 把指令语义写入搜索而非只做一次 LLM 展开。
- **关系：** 搜索式规划 Agent。

---

<a id="p-210"></a>

### 210. LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning

- **年份：** 2023
- **标签：** `VLA`
- **链接：** [arXiv:2306.03310](https://arxiv.org/abs/2306.03310)

**摘要：** LIBERO 提供面向终身机器人学习的知识迁移基准，覆盖程序性、目标与操作知识的前向迁移。它包含仿真操作任务套件与评测协议，成为后续 `VLA` 与层次化 Agent 的常用操作评测床。

**要点：**

- **方法：** 构建区分程序性 / 目标 / 操作知识迁移的终身操作基准。
- **贡献：** 为通用操作策略与层次化 Agent 提供可比较的仿真评测。
- **关系：** `VLA` 与 Agent 编排常用评测床，本身不是新控制算法。

---

<a id="p-211"></a>

### 211. LLM as A Robotic Brain: Unifying Egocentric Memory and Control

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2304.09349](https://arxiv.org/abs/2304.09349)

**摘要：** 具身系统的记忆与控制通常分框架建模。LLM-Brain 用大语言模型统一自我中心记忆与控制，作为可泛化的机器人「大脑」，在交互中同时保持情景记忆并输出控制决策。

**要点：**

- **方法：** 单一 LLM 框架统一自我中心记忆与控制。
- **贡献：** 提出可泛化的机器人大脑式记忆—控制接口。
- **关系：** 记忆型规划 Agent，符号记忆而非 Dreamer 式 `WM`。

---

<a id="p-212"></a>

### 212. LLM+P: Empowering Large Language Models with Optimal Planning Proficiency

- **年份：** 2023
- **标签：** `llm-agent`
- **链接：** [arXiv:2304.11477](https://arxiv.org/abs/2304.11477)

**摘要：** LLM 零样本问答强，但长时程规划不可靠；经典规划器在问题形式化后很强。LLM+P 让 LLM 把语言指令译为 PDDL，再调用最优规划器求解，最后把计划译回自然语言。该方法在规划基准上显著优于仅用 LLM 的计划，为机器人符号规划 Agent 提供可组合接口。

**要点：**

- **方法：** LLM 将指令译为 PDDL，经典规划器求最优计划后再译回语言。
- **贡献：** 在规划基准上明显优于纯 LLM 计划。
- **关系：** 规划 Agent 与符号规划器的工具使用组合，可接到机器人任务规划。

---

<a id="p-213"></a>

### 213. LLM-BRAIn: AI-driven Fast Generation of Robot Behaviour Tree based on Large Language Model

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2305.19352](https://arxiv.org/abs/2305.19352)

**摘要：** LLM-BRAIn 从 Alpaca 7B 微调，把操作员文本命令转为机器人行为树。训练使用约 8500 条指令跟随示范，实现由语言快速生成可执行 BT，便于接入传统机器人执行栈。

**要点：**

- **方法：** 微调 LLM 由文本生成机器人行为树。
- **贡献：** 把自然语言命令接到工业常用的 BT 执行表示。
- **关系：** 语言→行为树 Agent，非 `VLA`。

---

<a id="p-214"></a>

### 214. LLM-State: Open World State Representation for Long-horizon Task Planning with Large Language Model

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2311.17406](https://arxiv.org/abs/2311.17406)

**摘要：** LLM-State 为开放世界长时程规划维护语言模型可读的状态表示，使规划器在开放世界中跟踪物体与关系，而不是只依赖对话历史。

**要点：**

- **方法：** 用 LLM 维护开放世界状态表示以支持长时程规划。
- **贡献：** 显式状态减轻开放世界规划的遗忘与不一致。
- **关系：** 近 Statler 的符号状态 Agent。

---

<a id="p-215"></a>

### 215. Look Before You Leap: Unveiling the Power of GPT-4V in Robotic Vision-Language Planning

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent` · `VLM`
- **链接：** [arXiv:2311.17842](https://arxiv.org/abs/2311.17842)

**摘要：** Look Before You Leap 展示 GPT-4V 在机器人视觉—语言规划中的能力：先看再跳，用多模态模型在行动前做视觉推理与计划，减少盲目执行。

**要点：**

- **方法：** 用 GPT-4V 在行动前做视觉—语言规划。
- **贡献：** 验证多模态 LLM 作为机器人视觉规划器。
- **关系：** `VLM` 规划 Agent。

---

<a id="p-216"></a>

### 216. March in Chat: Interactive Prompting for Remote Embodied Referring Expression

- **年份：** 2023
- **标签：** `VLN` · `llm-agent`
- **链接：** [arXiv:2308.10141](https://arxiv.org/abs/2308.10141)

**摘要：** March in Chat 研究远程具身指代表达（REVERIE 一类）：用交互式提示让 LLM 在对话中逐步明确导航与指代目标。方法把语言交互接到具身导航，展示对话 Agent 如何服务 `VLN` 式远程指令。

**要点：**

- **方法：** 交互式对话提示逐步澄清远程具身指代与导航目标。
- **贡献：** 把对话式 LLM 接到远程具身指代表达任务。
- **关系：** 对话 Agent 服务 `VLN` / 指代导航，文中非 `World Model`。

---

<a id="p-217"></a>

### 217. Mastering Diverse Domains through World Models

- **年份：** 2023
- **标签：** `VLM` · `world_model`
- **链接：** [arXiv:2301.04104](https://arxiv.org/abs/2301.04104)

**摘要：** 研发能在广泛任务上求解的通用算法是人工智能的基本挑战。现有强化学习迁到新域需大量调参。本文提出 DreamerV3：以单一配置在逾 150 项任务上优于专用方法。它学习环境模型并通过想象未来改进行为，以归一化、平衡与变换保证跨域稳定。开箱即用时，它是首个无人类数据或课程即从零在 Minecraft 中采集钻石的算法。

**要点：**

- **方法：** 学习环境 `World Model` 并在想象中改进策略，以归一化、平衡与变换保证跨域稳定，单一配置通用。
- **贡献：** 以同一配置在逾 150 项任务上优于专用方法，并首次无人类数据从零在 Minecraft 中采集钻石。
- **关系：** 展示可跨域的 `World Model` 强化学习；文中未做 `VLA`/`VLN`/`VLM` 实验。

---

<a id="p-218"></a>

### 218. NavGPT: Explicit Reasoning in Vision-and-Language Navigation with Large Language Models

- **年份：** 2023
- **标签：** `VLN`
- **链接：** [arXiv:2305.16986](https://arxiv.org/abs/2305.16986)

**摘要：** 大规模 LLM 如 ChatGPT 与 GPT-4 涌现显著推理能力。本文提出纯 LLM 指令跟随导航智能体 NavGPT，对 `VLN` 做零样本序列动作预测。每步输入观测文本、导航历史与可探索方向以推理并决策。实验表明其能分解子目标、整合常识、识别地标、跟踪进度并调整计划，还能生成导航指令与俯视轨迹。零样本 R2R 仍不及训练模型；作者建议为 LLM 适配多模态输入，并把显式推理用于学习型模型。

**要点：**

- **方法：** 纯 LLM 导航智能体，每步用观测文本、历史与可探索方向做零样本 `VLN` 序列动作预测。
- **贡献：** 展示可分解子目标、用地标与常识规划并调整计划；还能生成指令与俯视轨迹，但零样本 R2R 仍不及训练模型。
- **关系：** 把 LLM 显式推理引入 `VLN`；文中未涉及 `World Model`。

---

<a id="p-219"></a>

### 219. Navigation with Large Language Models: Semantic Guesswork as a Heuristic for Planning

- **年份：** 2023
- **标签：** `VLN`
- **链接：** [arXiv:2310.10103](https://arxiv.org/abs/2310.10103)

**摘要：** 陌生环境导航对机器人很难：建图规划往往需要漫长探索。人类可借助语义迅速导航，但直接用未接地的语言模型指挥可能任意错误。本文提出 Language Frontier Guide（LFG），把语言模型的“语义猜测”作为拓扑或度量地图规划的搜索启发式，以偏置新颖真实环境中的探索。在真实环境与仿真基准上评估，优于无信息探索及其他使用语言模型的方式。

**要点：**

- **方法：** 将语言模型的语义猜测作为拓扑或度量地图规划的搜索启发式，以偏置陌生环境探索（LFG）。
- **贡献：** 在真实环境与仿真基准上优于无信息探索及其他使用语言模型的方式。
- **关系：** 用语言模型语义启发式服务导航规划，属 `VLN`/语言导航；文中未涉及 `World Model` 或 `VLA`。

---

<a id="p-220"></a>

### 220. OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving

- **年份：** 2023
- **标签：** `world_model`
- **链接：** [arXiv:2311.16038](https://arxiv.org/abs/2311.16038)

**摘要：** 理解三维场景演化对自动驾驶决策至关重要，但预测物体框难以刻画细粒度信息。本文提出在三维占据空间学习 `World Model` 的 OccWorld，同时预测自车运动与周围场景演化。三维占据更精细、更易获取，且可适配视觉与 LiDAR。先学重建式场景分词器得到离散 token，再用类 GPT 的时空生成 Transformer 解码未来占据与自车轨迹。在 nuScenes 上能有效建模场景演化，且无实例与地图监督时规划仍有竞争力。

**要点：**

- **方法：** 三维占据上学习重建式场景分词器，再用类 GPT 的时空生成 Transformer 预测未来占据与自车轨迹。
- **贡献：** 同时预测自车与场景演化；nuScenes 上有效建模场景演化，且无实例/地图监督时规划仍有竞争力。
- **关系：** 三维占据 `World Model` 服务驾驶预测与规划，文中未涉及 `VLA`/`VLN`/`VLM`。

---

<a id="p-221"></a>

### 221. Octopus: Embodied Vision-Language Programmer from Environmental Feedback

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent` · `VLM`
- **链接：** [arXiv:2310.08588](https://arxiv.org/abs/2310.08588)

**摘要：** Octopus 是具身视觉—语言程序员：根据环境反馈生成程序，把视觉观察与语言指令编译为可执行代码，并在反馈下改写，属于代码即策略的视觉闭环版本。

**要点：**

- **方法：** 视觉—语言程序员根据环境反馈生成并改写控制程序。
- **贡献：** 把 Code as Policies 接到视觉反馈闭环。
- **关系：** 代码即策略 Agent + `VLM`。

---

<a id="p-222"></a>

### 222. Open X-Embodiment: Robotic Learning Datasets and RT-X Models

- **年份：** 2023
- **标签：** `intersection`
- **链接：** [arXiv:2310.08864](https://arxiv.org/abs/2310.08864)

**摘要：** 在多样化数据上训练的高容量模型已在 NLP 与视觉中成为统一预训练骨干。机器人学习能否同样整合？传统方法为每个应用、机器人甚至环境单独训练。本文提供标准化格式的数据集与模型以探索通才跨机器人策略。通过 21 家机构协作，汇集 22 种机器人数据，涵盖 527 项技能（160266 个任务）。高容量模型 RT-X 表现出正向迁移，能借助其他平台经验提升多机器人能力。

**要点：**

- **方法：** 汇集 22 种机器人、标准化格式的大规模操作数据，并训练高容量跨机器人策略 RT-X。
- **贡献：** 提供可共享的跨本体数据集与模型，实验显示正向迁移并提升多机器人能力。
- **关系：** 为跨本体视觉-语言条件操作策略提供共享数据与模型底座；文中未涉及 `World Model`。

---

<a id="p-223"></a>

### 223. PaLM-E: An Embodied Multimodal Language Model

- **年份：** 2023
- **标签：** `VLM`
- **链接：** [arXiv:2303.03378](https://arxiv.org/abs/2303.03378)

**摘要：** 提出具身语言模型，将真实世界连续传感模态直接纳入语言模型，以建立词语与感知之间的联系。输入为交织视觉、连续状态估计与文本编码的多模态句子，并与预训练大语言模型端到端训练，用于序列机器人操作规划、视觉问答与描述。评估显示单一大型具身多模态模型 PaLM-E 可处理多种观测模态与多种本体上的具身推理，并在互联网规模语言、视觉与视觉—语言联合训练中呈现正向迁移；最大的 PaLM-E-562B 还是视觉—语言通才，在 OK-VQA 上达先进水平并随规模保留通用语言能力。

**要点：**

- **方法：** 将视觉、连续状态估计与文本编码交织为多模态句子，并与预训练大语言模型端到端训练具身语言模型。
- **贡献：** 单一大型具身多模态模型 PaLM-E 可跨模态与本体做具身推理，联合训练呈现正向迁移，且大规模模型兼具视觉—语言通才能力。
- **关系：** 为 `VLM` 提供把连续感知直接接入语言模型的具身路径，对后续 `VLA` 的视觉—语言落地具有奠基意义；本文并非 `World Model` 研究。

---

<a id="p-224"></a>

### 224. Prompt a Robot to Walk with Large Language Models

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2309.09969](https://arxiv.org/abs/2309.09969)

**摘要：** 本文研究用大语言模型提示机器人行走：把语言接到步态 / 运动控制接口，展示 LLM 不仅能做操作规划，也能参与运动控制层面的指令跟随。

**要点：**

- **方法：** 用 LLM 提示生成或选择行走相关控制。
- **贡献：** 把语言 Agent 从操作规划扩展到行走。
- **关系：** 语言条件运动 Agent，非腿式 `VLA` 权重模型。

---

<a id="p-225"></a>

### 225. Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions

- **年份：** 2023
- **标签：** `VLM`
- **链接：** [arXiv:2309.10150](https://arxiv.org/abs/2309.10150)

**摘要：** 提出可扩展的强化学习方法，从大型离线数据集训练多任务策略，并可同时利用人类演示与自主采集数据。该方法用 Transformer 作为经离线时序差分备份训练的 Q 函数的可扩展表示，故称 Q-Transformer。通过离散化各动作维度、将每一维 Q 值表示为独立 token，从而把高容量序列建模用于 Q 学习。若干设计决策使离线强化学习表现良好；在大规模多样的真实机器人操作任务集上，Q-Transformer 优于先前离线强化学习算法与模仿学习方法。

**要点：**

- **方法：** 用 Transformer 表示经离线时序差分备份训练的 Q 函数，并将各动作维离散化为独立 token 以做序列化 Q 学习。
- **贡献：** 给出可同时利用演示与自主数据的可扩展离线强化学习，并在多样真实操作任务上优于先前离线强化学习与模仿学习。
- **关系：** 为多任务机器人策略提供可扩展的 Transformer Q 学习骨干，可与 `VLA` 式控制衔接；本文并不研究 `World Model` 或 `VLN`。

---

<a id="p-226"></a>

### 226. REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2306.15724](https://arxiv.org/abs/2306.15724)

**摘要：** 自动检测并分析失败对可解释稳健机器人至关重要。REFLECT 查询 LLM，把机器人经验总结为失败解释并生成纠正，从而用语言反思闭环改进后续执行。

**要点：**

- **方法：** 用 LLM 总结机器人经验以解释失败并生成纠正。
- **贡献：** 把失败解释变成可执行的纠正回路。
- **关系：** 反思 / 恢复 Agent，近 Reflexion 的真机版。

---

<a id="p-227"></a>

### 227. Reflexion: Language Agents with Verbal Reinforcement Learning

- **年份：** 2023
- **标签：** `llm-agent`
- **链接：** [arXiv:2303.11366](https://arxiv.org/abs/2303.11366)

**摘要：** 语言智能体难以像传统强化学习那样从试错中快速学习。Reflexion 用语言形式的强化：智能体把环境反馈转成语言反思并写入情景记忆，供后续试验使用，而无需更新模型权重。在决策、编程与推理任务上显著提升，成为机器人自我纠错 Agent 的常用组件。

**要点：**

- **方法：** 以语言反思作言语强化学习，写入记忆供后续试验，不更新权重。
- **贡献：** 在决策、编程与推理任务上显著提升试错学习效率。
- **关系：** 规划 / 工具使用 Agent 地标，机器人闭环常复用其反思回路。

---

<a id="p-228"></a>

### 228. RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation

- **年份：** 2023
- **标签：** `VLM`
- **链接：** [arXiv:2306.11706](https://arxiv.org/abs/2306.11706)

**摘要：** 提出多本体、多任务的机器人操作通才智能体 RoboCat：它是视觉目标条件的 decision transformer，可消费带动作标注的视觉经验，覆盖仿真与真实机械臂上多种观测与动作的运动控制技能。可零样本泛化到新任务与新机器人，也可仅用目标任务的 100–1000 条样本进行适配；训练好的模型还能生成数据供后续训练迭代，构成自主改进循环的基本构件。在仿真与三种真实本体上的大规模评估表明，随着训练数据增长与多样化，RoboCat 出现跨任务迁移迹象，并对新任务的适配更为高效。

**要点：**

- **方法：** 构建视觉目标条件的 decision transformer，消费跨仿真与真实、多种观测与动作的带标注视觉经验。
- **贡献：** 展示对新任务与新本体的零样本及少样本适配，并可用模型自身生成数据形成自主改进循环。
- **关系：** 作为多本体多任务通才操作智能体，为 `VLA` 式视觉—动作泛化提供经验；本文并非 `World Model` 或 `VLN` 研究。

---

<a id="p-229"></a>

### 229. RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2311.01455](https://arxiv.org/abs/2311.01455)

**摘要：** RoboGen 是生成式机器人智能体：自动提出任务、生成仿真场景与训练监督，再选择强化学习、运动规划或轨迹优化来学技能。提出—生成—学习循环可反复查询，产生无限多样的技能演示，覆盖刚体、软体与腿式运动。

**要点：**

- **方法：** 基础模型自动提出任务、生成场景与监督，再选择学习算法练技能。
- **贡献：** 以生成式仿真规模化机器人技能学习，减少人工设计。
- **关系：** 生成式 Agent 控制「学什么、在哪学」，而非部署期 `VLA`。

---

<a id="p-230"></a>

### 230. RoboGPT: an intelligent agent of making embodied long-term decisions for daily instruction tasks

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2311.15649](https://arxiv.org/abs/2311.15649)

**摘要：** RoboGPT 做日常指令的具身长期决策智能体：把家居式长时程指令分解为可执行决策序列，强调日常任务上的长期决策而非单步技能。

**要点：**

- **方法：** 以 LLM 智能体做日常指令的长期具身决策。
- **贡献：** 面向家居长时程指令跟随。
- **关系：** 家用长期决策 Agent。

---

<a id="p-231"></a>

### 231. RoCo: Dialectic Multi-Robot Collaboration with Large Language Models

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2307.04738](https://arxiv.org/abs/2307.04738)

**摘要：** RoCo 让多机器人用 LLM 对话协商高层策略，再生成子任务与任务空间航点，交给多臂运动规划器。环境碰撞等反馈被写回提示以改进计划。配套 RoCoBench 覆盖六类协作场景；仿真成功率高，真机还可接入人机对话协作。

**要点：**

- **方法：** 多机器人 LLM 对话 + 航点生成 + 多臂运动规划，并闭环反馈。
- **贡献：** 提出 RoCoBench，仿真与真机展示可解释的多机器人协作。
- **关系：** 多智能体机器人协作 Agent，规划层为 LLM 而非 `VLA`。

---

<a id="p-232"></a>

### 232. RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control

- **年份：** 2023
- **标签：** `VLA`
- **链接：** [arXiv:2307.15818](https://arxiv.org/abs/2307.15818)

**摘要：** 研究如何将互联网规模数据上训练的视觉—语言模型直接纳入端到端机器人控制，以提升泛化并带来涌现的语义推理。将先进视觉—语言模型在机器人轨迹与互联网规模视觉—语言任务上共同微调；为统一格式，把动作表示为文本 token 并像自然语言 token 一样纳入训练集。此类模型称为视觉—语言—动作模型（`VLA`），其实例为 RT-2。广泛评估表明可得到有效机器人策略，并使 RT-2 获得对新物体更好泛化、理解机器人数据中未见指令以及初步推理等涌现能力；结合思维链还可进行多阶段语义推理。

**要点：**

- **方法：** 将先进视觉—语言模型在机器人轨迹与互联网规模视觉—语言任务上共同微调，并把动作表示为文本 token。
- **贡献：** 实例化 `VLA` 模型 RT-2，展示有效机器人策略及来自互联网训练的泛化、指令理解与思维链多阶段推理等涌现能力。
- **关系：** 是将 `VLM` 知识迁入端到端控制的代表性 `VLA` 工作；本文并不研究 `World Model` 或 `VLN`。

---

<a id="p-233"></a>

### 233. RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches

- **年份：** 2023
- **标签：** `VLA`
- **链接：** [arXiv:2311.01977](https://arxiv.org/abs/2311.01977)

**摘要：** RT-Trajectory 用事后轨迹草图作为任务泛化的条件：把期望的末端轨迹画成或生成为草图，再训练策略跟随。相对纯语言条件，轨迹草图提供更密的时空指导，提高对新任务与新物体的泛化。

**要点：**

- **方法：** 以事后轨迹草图条件训练机器人策略，补充语言指令。
- **贡献：** 提高对未见任务的轨迹级泛化。
- **关系：** 语言 / 轨迹条件策略，属 `VLA` 数据条件而非规划 Agent。

---

<a id="p-234"></a>

### 234. SayCanPay: Heuristic Planning with Large Language Models using Learnable Domain Knowledge

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2308.12682](https://arxiv.org/abs/2308.12682)

**摘要：** SayCanPay 在 SayCan 上加入可学习领域知识的启发式支付 / 评分，用 LLM 提议技能，用可学习启发式评估长期代价或价值，从而改进启发式规划。

**要点：**

- **方法：** LLM 提议技能，可学习启发式（Pay）评估并选择。
- **贡献：** 在 SayCan 式规划中引入可学习领域评分。
- **关系：** SayCan 家族规划 Agent。

---

<a id="p-235"></a>

### 235. SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning

- **年份：** 2023
- **标签：** `VLM`
- **链接：** [arXiv:2307.06135](https://arxiv.org/abs/2307.06135)

**摘要：** 针对在广阔的多楼层、多房间环境中落地规划这一机器人难题，提出 SayPlan：利用三维场景图（3DSG）表示，实现可扩展的基于大语言模型的大规模任务规划。为保证可扩展性，利用 3DSG 的层次性让 LLM 从压缩小图中对任务相关子图做语义搜索，结合经典路径规划以缩短规划视界，并引入迭代重规划流水线，用场景图仿真器反馈修正不可行动作。在最多三层、三十六房间、一百四十项资产与物体的两大环境上评估，表明可将抽象自然语言指令落地为移动操作机器人可执行的大规模长时程任务计划。

**要点：**

- **方法：** 以层次化三维场景图支撑 LLM 语义搜索，结合经典路径规划与基于场景图仿真反馈的迭代重规划。
- **贡献：** 在多楼层、多房间大环境中将抽象自然语言指令落地为移动操作机器人可执行的长时程任务计划。
- **关系：** 为 `VLM`/LLM 机器人规划提供可扩展的三维场景图落地；本文并不研究 `World Model`，亦非 `VLN` 导航基准工作。

---

<a id="p-236"></a>

### 236. Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture

- **年份：** 2023
- **标签：** `world_model`
- **链接：** [arXiv:2301.08243](https://arxiv.org/abs/2301.08243)

**摘要：** 展示一种不依赖手工数据增强即可学习高语义图像表示的方法。提出基于图像的联合嵌入预测架构 I-JEPA，这是一种从图像做自监督学习的非生成式方法：由单一上下文块预测同一图像中多个目标块的表示。引导其产生语义表示的核心设计是掩码策略——需采样足够大尺度的目标块，并使用足够信息、空间分布充分的上下文块。经验上，与 Vision Transformer 结合时 I-JEPA 具有高可扩展性：例如在 ImageNet 上训练 ViT-Huge/14，可在线性分类、物体计数与深度预测等广泛下游任务上取得较强表现。

**要点：**

- **方法：** 提出非生成式自监督架构 I-JEPA，由单一上下文块预测同图中多目标块表示，并以掩码策略导向语义表征。
- **贡献：** 无需手工数据增强即可学习高语义图像表示，与 Vision Transformer 结合具有可扩展性并在多种下游任务上表现较强。
- **关系：** 属于预测式表征学习，为 `World Model` 提供联合嵌入预测思路；本文并不研究 `VLA`、`VLN` 或 `VLM` 具身控制。

---

<a id="p-237"></a>

### 237. Skill Reinforcement Learning and Planning for Open-World Long-Horizon Tasks

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2303.16563](https://arxiv.org/abs/2303.16563)

**摘要：** 开放世界无演示的长时程强化学习极低效。本文在 Minecraft 上把多任务学习拆成技能强化学习与技能上的规划，先学基本技能再规划组合，以完成开放世界长时程任务。

**要点：**

- **方法：** 先 RL 学基本技能，再在技能上规划开放世界长任务。
- **贡献：** 无人类演示下提高 Minecraft 多任务效率。
- **关系：** 技能库 Agent，与 Voyager / DEPS 同属开放世界线。

---

<a id="p-238"></a>

### 238. SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2309.10062](https://arxiv.org/abs/2309.10062)

**摘要：** SMART-LLM 用少样本程序化提示完成多机器人任务分解、联盟形成与任务分配，把高层指令转为多机器人计划。作者构建按复杂度分档的基准，并在仿真与真机上验证计划生成。相对每机器人一个 LLM 的对话方案，它用中央 LLM 简化异构团队协调。

**要点：**

- **方法：** 中央 LLM 经分解—联盟—分配三阶段生成多机器人任务计划。
- **贡献：** 提出多机器人规划基准，并在仿真与真机上验证。
- **关系：** 多智能体任务规划 Agent，不训练 `VLA`。

---

<a id="p-239"></a>

### 239. Statler: State-Maintaining Language Models for Embodied Reasoning

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2306.17840](https://arxiv.org/abs/2306.17840)

**摘要：** Statler 让 LLM 维护对不可观测世界状态的估计，并在动作后更新该状态，再据此条件生成下一步。相对 Code as Policies 等仅依赖对话历史的方法，显式状态读写显著提高若干机器人规划任务的成功，并更利于长时程扩展。

**要点：**

- **方法：** 世界状态读—写双 LLM，在显式状态估计上条件生成动作。
- **贡献：** 在多项机器人规划上优于 Code as Policies 等强基线。
- **关系：** 用语言模型维护符号世界状态，属 Agent 规划而非学得 `World Model`。

---

<a id="p-240"></a>

### 240. STEVE-1: A Generative Model for Text-to-Behavior in Minecraft

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2306.00937](https://arxiv.org/abs/2306.00937)

**摘要：** STEVE-1 把 VPT 行为基础模型按 unCLIP 思路做指令微调：先在 MineCLIP 潜空间对齐指令，再训练文本先验，从而用自监督行为克隆与事后重标注降低文本标注成本（约 60 美元算力）。它用原始像素与键鼠低层控制跟随短时程开放指令，在早期游戏评测中稳健完成 13 项中的 12 项。

**要点：**

- **方法：** 在 MineCLIP 潜空间指令微调 VPT，并训练文本先验。
- **贡献：** 低成本实现 Minecraft 短时程开放指令跟随，12/13 项任务稳健完成。
- **关系：** 开放式具身控制 Agent，低层策略可与 LLM 规划器组合。

---

<a id="p-241"></a>

### 241. STORM: Efficient Stochastic Transformer based World Models for Reinforcement Learning

- **年份：** 2023
- **标签：** `world_model`
- **链接：** [arXiv:2310.09615](https://arxiv.org/abs/2310.09615)

**摘要：** STORM 用随机 Transformer 世界模型做样本高效强化学习：在潜空间对随机动力学建模，并在想象中训练策略。作为 Transformer `World Model` 一线（与 IRIS / TWM 并列），它补全本包此前仅有仓库、缺少论文卡片的缺口。

**要点：**

- **方法：** 随机 Transformer 世界模型在潜空间建模动力学并想象训练策略。
- **贡献：** 为样本高效 RL 提供 Transformer `WM` 代表方法。
- **关系：** 纯 `World Model` RL，摘要未做 `VLA`/`VLN`。

---

<a id="p-242"></a>

### 242. Task and Motion Planning with Large Language Models for Object Rearrangement

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2303.06247](https://arxiv.org/abs/2303.06247)

**摘要：** 服务机器人多物体重排需要常识，但 LLM 并不天然编码合理物理布局。本文把 LLM 接到任务与运动规划，使物体重排既符合常识又满足几何可行，用于桌面 / 服务操作。

**要点：**

- **方法：** LLM 常识与任务—运动规划结合做物体重排。
- **贡献：** 在常识布局与几何可行之间搭桥。
- **关系：** TAMP + 语言 Agent。

---

<a id="p-243"></a>

### 243. Text2Motion: From Natural Language Instructions to Feasible Plans

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2303.12153](https://arxiv.org/abs/2303.12153)

**摘要：** Text2Motion 把自然语言指令转为几何可行的任务—运动计划。框架用少样本 LLM 构造符号目标与技能序列，再用运动规划验证几何可行性；不可行则反馈重规划。相对纯 LLM 计划，它能完成需要长时程几何推理的顺序操作，并在仿真操作任务上提高成功。

**要点：**

- **方法：** LLM 符号规划与运动规划可行性检验交替，失败则反馈重规划。
- **贡献：** 把语言指令落到几何可行的长时程操作计划。
- **关系：** 规划 Agent 与经典运动规划耦合，不是端到端 `VLA`。

---

<a id="p-244"></a>

### 244. TidyBot: Personalized Robot Assistance with Large Language Models

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2305.05658](https://arxiv.org/abs/2305.05658)

**摘要：** 家居整理需要把用户偏好泛化到新场景。TidyBot 用 LLM 从少量示例中总结「东西放哪」的偏好，再结合预训练感知与抓放技能在真实房间整理。系统可个性化放置规则，并在真实家庭环境中完成拾取—放置，展示语言 Agent 对真机家务的控制。

**要点：**

- **方法：** 用 LLM 从少量示例归纳放置偏好，再调用感知与抓放技能。
- **贡献：** 在真实房间实现可个性化的整理辅助。
- **关系：** 家用机器人 Agent，语言规划 + 技能原语，而非端到端 `VLA`。

---

<a id="p-245"></a>

### 245. Toward General-Purpose Robots via Foundation Models: A Survey and Meta-Analysis

- **年份：** 2023
- **标签：** `llm-agent` · `VLA`
- **链接：** [arXiv:2312.08782](https://arxiv.org/abs/2312.08782)

**摘要：** 面向通用机器人的基础模型综述与元分析，比较不同基础模型路线通向通才机器人的证据与缺口，补充 `VLA` / Agent 设计选择。

**要点：**

- **方法：** 对通才机器人基础模型文献做综述与元分析。
- **贡献：** 归纳通向通用机器人的证据强度与缺口。
- **关系：** 通才机器人综述，覆盖 Agent 与 `VLA`。

---

<a id="p-246"></a>

### 246. Towards Learning a Generalist Model for Embodied Navigation

- **年份：** 2023
- **标签：** `VLN`
- **链接：** [arXiv:2312.02010](https://arxiv.org/abs/2312.02010)

**摘要：** 先前具身导航工作多针对特定任务智能体，对未见场景泛化不足。提出首个具身导航通才模型 NaviLLM：通过引入基于 schema 的指令将大语言模型适配到具身导航，把多种任务灵活转为生成问题从而统一任务，并融合多数据集训练以具备具身导航所需的广泛能力。实验表明该统一模型在 CVDN、SOON 与 ScanQA 上达到先进水平，其中 CVDN 的目标进度较先前先进方法显著高出 29%；对未见任务如具身问答与三维描述也表现出强泛化。

**要点：**

- **方法：** 用基于 schema 的指令将多种具身导航任务统一为生成问题，并融合多数据源训练大语言模型。
- **贡献：** 提出首个具身导航通才模型 NaviLLM，在 CVDN、SOON 与 ScanQA 上达先进水平，并对未见任务表现强泛化。
- **关系：** 直接推进基于 LLM 的 `VLN` 通才智能体；本文并不研究 `World Model`，亦非操作向 `VLA`。

---

<a id="p-247"></a>

### 247. Transformer-based World Models Are Happy With 100k Interactions

- **年份：** 2023
- **标签：** `world_model`
- **链接：** [arXiv:2303.07109](https://arxiv.org/abs/2303.07109)

**摘要：** 深度网络在强化学习中常过于依赖数据。为构建样本高效的 `World Model`，以自回归方式将 Transformer 用于真实回合：不仅将紧凑隐状态与已采取动作，也将经历或预测的奖励输入 Transformer，使其可灵活关注三种模态的不同时间步。该 Transformer 可直接访问先前状态，而非经由压缩循环状态观察它们；采用 Transformer-XL 架构以在保持计算效率的同时学习长期依赖。基于 Transformer 的 `World Model`（TWM）生成有意义的新经验以训练策略，在 Atari 100k 基准上优于先前无模型与基于模型的强化学习算法。

**要点：**

- **方法：** 以自回归 Transformer-XL 同时建模隐状态、动作与奖励，使 `World Model` 可直接回看历史而非依赖压缩循环状态。
- **贡献：** 所提 TWM 能生成有意义的新经验以训练策略，并在 Atari 100k 上优于先前无模型与基于模型的算法。
- **关系：** 属于样本高效 Transformer `World Model` 工作，并未涉及 `VLA`、`VLN` 或 `VLM`。

---

<a id="p-248"></a>

### 248. Translating Natural Language to Planning Goals with Large-Language Models

- **年份：** 2023
- **标签：** `llm-agent`
- **链接：** [arXiv:2302.05128](https://arxiv.org/abs/2302.05128)

**摘要：** LLM 在 NLP 上强，但准确推理与求解规划问题仍弱。本文研究如何把自然语言译为规划目标，使经典规划器可用，从而服务机器人任务。结论强调翻译目标比让 LLM 直接当规划器更可靠。

**要点：**

- **方法：** 把自然语言翻译为规划目标，再交给规划器。
- **贡献：** 指出 LLM 直接规划的不可靠，并给出目标翻译路径。
- **关系：** 与 LLM+P 同类的符号规划接口。

---

<a id="p-249"></a>

### 249. Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation

- **年份：** 2023
- **标签：** `VLA`
- **链接：** [arXiv:2312.13139](https://arxiv.org/abs/2312.13139)

**摘要：** 该文（GR-1）把大规模视频生成预训练用于视觉机器人操作：模型同时预测未来图像与动作，将互联网视频知识迁到操作策略。作为视频—语言—动作生成式通才的早期代表，它衔接后续 GR-2。

**要点：**

- **方法：** 大规模视频生成预训练后，联合预测未来帧与机器人动作。
- **贡献：** 把网络视频知识迁到视觉操作通才策略。
- **关系：** 生成式 `VLA` / 视频预测策略，含隐式世界预测。

---

<a id="p-250"></a>

### 250. ViNT: A Foundation Model for Visual Navigation

- **年份：** 2023
- **标签：** `VLN`
- **链接：** [arXiv:2306.14846](https://arxiv.org/abs/2306.14846)

**摘要：** 提出视觉导航 Transformer（ViNT），旨在将通才预训练模型的成功带到基于视觉的机器人导航。以可适用于任意导航数据集的通用到达目标进行训练，并用灵活的 Transformer 架构学习导航可供性，以高效适配多种下游导航任务。在涵盖数百小时、多种机器人平台的现有导航数据集上训练，呈现正向迁移并优于在单一数据集上训练的专家模型。可用基于扩散的子目标提案探索新环境，并在配备远程启发式时求解公里级导航；亦可用类似 prompt-tuning 的技术，将目标编码器替换为嵌入同一目标 token 空间的其他任务模态（如 GPS 航点或路由指令）。

**要点：**

- **方法：** 以通用到达目标训练灵活的 Transformer，学习导航可供性，并可用类似 prompt-tuning 的方式替换目标编码器。
- **贡献：** 跨多平台导航数据呈现正向迁移，可结合扩散子目标探索新环境，并在远程启发式辅助下求解公里级导航。
- **关系：** 为视觉导航提供基础模型，直接服务 `VLN`/移动机器人；本文并不研究 `World Model` 或操作向 `VLA`。

---

<a id="p-251"></a>

### 251. Vision-Language Foundation Models as Effective Robot Imitators

- **年份：** 2023
- **标签：** `intersection`
- **链接：** [arXiv:2311.01378](https://arxiv.org/abs/2311.01378)

**摘要：** 寻求以简单微调机器人数据的方式利用现有视觉—语言模型。提出基于开源 `VLM` OpenFlamingo 的视觉—语言操作框架 RoboFlamingo：用预训练 `VLM` 做单步视觉—语言理解，以显式策略头建模序列历史信息，并仅在语言条件操作数据集上用模仿学习轻度微调。该分解使其便于开环控制及在低性能平台部署。在所测基准上大幅超过当时先进水平，表明可将 `VLM` 有效适配到机器人控制；广泛实验还揭示不同预训练 `VLM` 在操作任务上的若干行为差异。

**要点：**

- **方法：** 在 OpenFlamingo 上分解为预训练 `VLM` 的单步理解与显式策略头，并仅用模仿学习对语言条件操作数据轻度微调。
- **贡献：** 以简单微调将开源 `VLM` 适配为有竞争力的机器人操作策略，并便于开环控制与低性能平台部署。
- **关系：** 展示把现成 `VLM` 转为语言条件操作策略的交叉路径，贴近 `VLA` 控制；本文并不研究 `World Model` 或 `VLN`。

---

<a id="p-252"></a>

### 252. VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2307.05973](https://arxiv.org/abs/2307.05973)

**摘要：** VoxPoser 用语言模型合成可组合的三维价值图，表示操作约束与目标，再用运动规划在价值图上求解轨迹。系统无需任务演示，即可在真实与仿真中完成多样语言条件操作，并组合空间约束。它把语言推理接到三维几何，是代码 / 价值图 Agent 控制机械臂的代表。

**要点：**

- **方法：** LLM 合成可组合 3D 价值图，运动规划在其上求解操作轨迹。
- **贡献：** 无任务演示即可完成多样语言条件真实操作。
- **关系：** 语言 Agent 通过 3D 价值图控制机器人，非端到端 `VLA`。

---

<a id="p-253"></a>

### 253. Voyager: An Open-Ended Embodied Agent with Large Language Models

- **年份：** 2023
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2305.16291](https://arxiv.org/abs/2305.16291)

**摘要：** Voyager 是 Minecraft 中首个由 LLM 驱动的终身学习具身智能体：自动课程最大化探索，可增长的技能库存储可执行代码，迭代提示融入环境反馈、执行错误与自验证。它不微调模型参数，仅黑盒查询 GPT-4。相对先前方法，获得更多独特物品、旅行更远，科技树里程碑最快约 15.3 倍，并可将技能库迁移到新世界。

**要点：**

- **方法：** 自动课程 + 可执行技能库 + 带反馈的迭代代码提示，黑盒调用 GPT-4。
- **贡献：** 开放式 Minecraft 终身学习，物品、行程与科技树进度显著领先，技能可迁移。
- **关系：** 开放式具身 Agent 地标，代码技能库控制「机器人式」游戏本体。

---

## 2022 年

共 18 篇。先扫目录，再下翻卡片。

- [254. CAPE: Corrective Actions from Precondition Errors using Large Language Models](#p-254)  `agent-robot` · `llm-agent`
- [255. Code as Policies: Language Model Programs for Embodied Control](#p-255)  `agent-robot` · `llm-agent`
- [256. DayDreamer: World Models for Physical Robot Learning](#p-256)  `world_model`
- [257. Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](#p-257)  `VLM`
- [258. Inner Monologue: Embodied Reasoning through Planning with Language Models](#p-258)  `VLM`
- [259. Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents](#p-259)  `agent-robot` · `llm-agent`
- [260. LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models](#p-260)  `agent-robot` · `llm-agent`
- [261. LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action](#p-261)  `agent-robot` · `VLN` · `llm-agent`
- [262. MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge](#p-262)  `agent-robot` · `llm-agent`
- [263. Open-vocabulary Queryable Scene Representations for Real World Planning](#p-263)  `agent-robot` · `llm-agent`
- [264. ProgPrompt: Generating Situated Robot Task Plans using Large Language Models](#p-264)  `agent-robot` · `llm-agent`
- [265. ReAct: Synergizing Reasoning and Acting in Language Models](#p-265)  `llm-agent`
- [266. Robot Task Planning and Situation Handling in Open Worlds](#p-266)  `agent-robot` · `llm-agent`
- [267. RT-1: Robotics Transformer for Real-World Control at Scale](#p-267)  `VLA`
- [268. Socratic Models: Composing Zero-Shot Multimodal Reasoning with Language](#p-268)  `agent-robot` · `llm-agent` · `VLM`
- [269. TransDreamer: Reinforcement Learning with Transformer World Models](#p-269)  `world_model`
- [270. Transformers are Sample-Efficient World Models](#p-270)  `world_model`
- [271. VIMA: General Robot Manipulation with Multimodal Prompts](#p-271)  `VLM`

<a id="p-254"></a>

### 254. CAPE: Corrective Actions from Precondition Errors using Large Language Models

- **年份：** 2022
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2211.09935](https://arxiv.org/abs/2211.09935)

**摘要：** 既有 LLM 规划失败时往往只是重试同一动作。CAPE 针对前提错误提出纠正动作，用语言模型分析失败原因并生成能解除前提的修正，从而在规划执行中恢复，而不是盲目重试。

**要点：**

- **方法：** 由前提错误触发 LLM 生成纠正动作，而非简单重试。
- **贡献：** 提高执行失败后的可恢复性。
- **关系：** ReAct 式失败恢复的规划 Agent。

---

<a id="p-255"></a>

### 255. Code as Policies: Language Model Programs for Embodied Control

- **年份：** 2022
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2209.07753](https://arxiv.org/abs/2209.07753)

**摘要：** Code as Policies 把会写代码的 LLM 重用于生成机器人策略程序：策略代码可表达反馈回路、调用感知与控制原语，并引用 NumPy 等库做几何推理。通过少样本「指令注释 + 策略代码」提示与层次化代码生成（递归定义未定义函数），模型可写出反应式与航点式策略，并在多台真机上演示。层次化代码生成还将 HumanEval 求解率提升至 39.8%。

**要点：**

- **方法：** 以层次化代码生成把自然语言指令编译为可执行策略程序（LMP）。
- **贡献：** 在真机上实现反应式与航点策略，并提升 HumanEval 求解率。
- **关系：** Agent 控制机器人的代码即策略地标，后续 ProgPrompt / VoxPoser 沿此线。

---

<a id="p-256"></a>

### 256. DayDreamer: World Models for Physical Robot Learning

- **年份：** 2022
- **标签：** `world_model`
- **链接：** [arXiv:2206.14176](https://arxiv.org/abs/2206.14176)

**摘要：** 深度强化学习需大量试错，限制了其在物理世界的部署；仿真学习又难以捕捉真实复杂性且行为难以适应变化。Dreamer 通过在所学 `World Model` 内规划，从少量交互学习。本文将 Dreamer 用于四台机器人，在真实世界在线直接学习、无需仿真器：四足机器人约一小时从零学会翻身、站立与行走且无需复位，受推后约十分钟适应；两台机械臂从相机图像与稀疏奖励学习多物体抓放并接近人类水平；轮式机器人仅从图像导航到目标并自动消解朝向歧义。各实验使用相同超参数，表明 Dreamer 可在真实世界在线学习。

**要点：**

- **方法：** 将 Dreamer 的 `World Model` 想象规划直接用于真实机器人在线学习，全程不依赖仿真器。
- **贡献：** 在四足、机械臂与轮式等四台真实机器人上，用同一组超参数从图像实现快速在线技能学习与适应。
- **关系：** 是把 `World Model` 用于物理机器人学习的实证；本文并不研究 `VLA`、`VLN` 或 `VLM`。

---

<a id="p-257"></a>

### 257. Do As I Can, Not As I Say: Grounding Language in Robotic Affordances

- **年份：** 2022
- **标签：** `VLM`
- **链接：** [arXiv:2204.01691](https://arxiv.org/abs/2204.01691)

**摘要：** 大语言模型编码了丰富的世界语义知识，但缺乏真实世界经验，难以在给定本体中做决策。提出用预训练技能提供真实世界落地，约束模型提出既可行又符合情境的自然语言动作：机器人充当语言模型的“手与眼”，语言模型提供任务的高层语义知识。低层技能与大语言模型结合，由技能相关的价值函数将关于复杂、长时程指令程序的知识连接到具体物理环境。在多项真实机器人任务上评估，表明需要真实世界落地，且该方法能使移动操作机器人完成长时程、抽象的自然语言指令。

**要点：**

- **方法：** 用预训练技能及其价值函数约束大语言模型，使其只提出可行且符合情境的自然语言动作。
- **贡献：** 将语言模型的高层程序知识落地到具体物理环境，使移动操作机器人能完成长时程抽象自然语言指令。
- **关系：** 为 `VLM`/LLM 机器人决策提供可供性落地范式；本文并不研究 `World Model`，亦非端到端 `VLA`。

---

<a id="p-258"></a>

### 258. Inner Monologue: Embodied Reasoning through Planning with Language Models

- **年份：** 2022
- **标签：** `VLM`
- **链接：** [arXiv:2207.05608](https://arxiv.org/abs/2207.05608)

**摘要：** 具身规划不仅要决定做什么技能，还要考虑如何与何时执行，且答案随智能体自身选择而变化。本文研究在具身情境中使用的大语言模型能在多大程度上、无需额外训练地，对以自然语言提供的反馈进行推理。提出利用环境反馈形成内心独白，从而更丰富地处理并规划机器人控制场景。考察成功检测、场景描述与人类交互等多种反馈来源。发现闭环语言反馈在三个领域显著提高高层指令完成率，包括仿真与真实桌面重排任务，以及真实厨房环境中的长时程移动操作任务。

**要点：**

- **方法：** 在无需额外训练的条件下，让大语言模型利用自然语言环境反馈形成内心独白并做闭环规划。
- **贡献：** 表明成功检测、场景描述与人类交互等闭环语言反馈可显著提高仿真与真实机器人任务的高层指令完成率。
- **关系：** 为 `VLM`/LLM 具身推理提供闭环语言反馈机制；本文并不研究 `World Model` 或 `VLN` 导航基准。

---

<a id="p-259"></a>

### 259. Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents

- **年份：** 2022
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2201.07207](https://arxiv.org/abs/2201.07207)

**摘要：** 本文探讨能否把大语言模型学到的世界知识落地为可执行步骤，例如把「做早餐」映射为「打开冰箱」。作者评估若干提示方法，发现预训练 LLM 的计划常不可执行。他们提出可容许动作翻译，把自由生成计划映射到环境中可用动作，从而显著提高可执行性。该工作是后续 SayCan、Inner Monologue 与 Code as Policies 等机器人 Agent 的规划前驱。

**要点：**

- **方法：** 用可容许动作翻译把 LLM 自由计划映射到环境可行动作。
- **贡献：** 系统评估零样本 LLM 规划的可执行性缺口，并给出可落地的动作映射。
- **关系：** 语言规划 Agent 地标，本身不是 `VLA` 或 `World Model`。

---

<a id="p-260"></a>

### 260. LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models

- **年份：** 2022
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2212.04088](https://arxiv.org/abs/2212.04088)

**摘要：** LLM-Planner 把大语言模型用作具身智能体的少样本规划器：在视觉感知环境中跟随自然语言指令。为降低数据成本，它用 LLM 生成高层子目标，再与学得的低层策略结合，并可在执行中根据观察重新规划。在 ALFRED 等基准上，少样本设定下即可达到有竞争力的成功率。

**要点：**

- **方法：** LLM 少样本生成子目标并与低层策略结合，支持执行中重规划。
- **贡献：** 在 ALFRED 等具身指令任务上以少样本取得有竞争力的成功。
- **关系：** 规划 Agent 控制具身执行，属语言规划而非端到端 `VLA`。

---

<a id="p-261"></a>

### 261. LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action

- **年份：** 2022
- **标签：** `agent-robot` · `VLN` · `llm-agent`
- **链接：** [arXiv:2207.04429](https://arxiv.org/abs/2207.04429)

**摘要：** 视觉导航目标常用图像指定，接口不自然。LM-Nav 组合预训练语言模型、视觉—语言模型与视觉导航模型：LLM 把自由语言指令分解为地标列表，`VLM` 在拓扑图上接地这些地标，导航模型再执行。系统在真实户外环境中用语言指令导航，且无需语言标注的导航轨迹。

**要点：**

- **方法：** LLM 分解指令、`VLM` 接地地标、视觉导航模型执行，三者均用预训练。
- **贡献：** 在真实户外用自由语言导航，无需语言标注轨迹。
- **关系：** 语言 Agent 控制导航，属 `VLN` 与模块化 `VLM` 交叉。

---

<a id="p-262"></a>

### 262. MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge

- **年份：** 2022
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2206.08853](https://arxiv.org/abs/2206.08853)

**摘要：** 开放世界智能体需要多样任务环境、大规模多模态知识与可扩展架构。MineDojo 在 Minecraft 上提供数千开放任务与互联网规模的视频、教程、维基与论坛知识库，并训练 MineCLIP 作为语言条件稠密奖励。该平台成为 Voyager、STEVE-1 与 GITM 等开放式具身 Agent 的共同底座。

**要点：**

- **方法：** 以 Minecraft 开放任务套件加互联网知识库，并训练 MineCLIP 语言条件奖励。
- **贡献：** 为开放式具身智能体提供可扩展环境与多模态知识基础设施。
- **关系：** 开放式 Agent 平台，不是 `World Model` 或 `VLA` 策略本身。

---

<a id="p-263"></a>

### 263. Open-vocabulary Queryable Scene Representations for Real World Planning

- **年份：** 2022
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2209.09874](https://arxiv.org/abs/2209.09874)

**摘要：** LLM 规划常缺场景接地。NLMap 提供开放词汇、可查询的场景表示，采集并整合环境上下文，使语言规划器能对真实场景提问并生成可执行计划。系统把开放词汇感知接到任务规划，服务真实世界机器人。

**要点：**

- **方法：** 构建开放词汇可查询场景图 NLMap，供 LLM 规划器检索上下文。
- **贡献：** 缓解语言计划与真实场景脱节，支持实机规划。
- **关系：** 场景表示服务规划 Agent，补 SayCan 式接地。

---

<a id="p-264"></a>

### 264. ProgPrompt: Generating Situated Robot Task Plans using Large Language Models

- **年份：** 2022
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2209.11302](https://arxiv.org/abs/2209.11302)

**摘要：** 任务规划通常需要大量领域知识。ProgPrompt 用程序化提示让 LLM 直接生成情境化机器人任务计划：提示包含环境状态、可用动作与示例，使生成计划可在真实与仿真机器人上执行。相对仅打分下一步的方法，直接生成动作序列更易利用 LLM 的程序结构，并在桌面操作任务上提高成功率。

**要点：**

- **方法：** 用包含状态与可用动作的程序化提示，让 LLM 生成可执行任务计划。
- **贡献：** 在仿真与真机桌面任务上提高计划可执行性与成功率。
- **关系：** 与 Code as Policies 并列的规划 Agent，强调情境化程序提示。

---

<a id="p-265"></a>

### 265. ReAct: Synergizing Reasoning and Acting in Language Models

- **年份：** 2022
- **标签：** `llm-agent`
- **链接：** [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)

**摘要：** LLM 的推理（思维链）与行动（生成动作计划）此前多被分开研究。ReAct 交错生成推理轨迹与任务动作，使模型能规划、跟踪与更新行动，并处理异常。在问答与决策基准上，ReAct 优于仅推理或仅行动的基线，并减少幻觉。该范式被广泛接到机器人闭环（Inner Monologue、Voyager、`VLN` 工具调用）。

**要点：**

- **方法：** 交错生成推理轨迹与动作，形成思考—行动闭环。
- **贡献：** 在问答与决策任务上优于单模态基线，并降低幻觉。
- **关系：** 通用 LLM Agent 地标，机器人 ReAct 式闭环的直接前驱（非 `VLA` 实验）。

---

<a id="p-266"></a>

### 266. Robot Task Planning and Situation Handling in Open Worlds

- **年份：** 2022
- **标签：** `agent-robot` · `llm-agent`
- **链接：** [arXiv:2210.01287](https://arxiv.org/abs/2210.01287)

**摘要：** 经典任务规划假设封闭世界与完备知识，真实开放世界常出现未预见情形。本文提出开放世界任务规划与情境处理，使机器人在知识不全时仍能补全情境并继续执行，而不是让规划器完备性崩溃。

**要点：**

- **方法：** 为开放世界补充情境处理，使任务规划在未预见情况下可恢复。
- **贡献：** 把封闭世界规划器接到真实开放环境。
- **关系：** 开放世界规划 Agent，非端到端 `VLA`。

---

<a id="p-267"></a>

### 267. RT-1: Robotics Transformer for Real-World Control at Scale

- **年份：** 2022
- **标签：** `VLA`
- **链接：** [arXiv:2212.06817](https://arxiv.org/abs/2212.06817)

**摘要：** 通过从大型、多样、任务无关数据集迁移知识，现代机器学习模型可以零样本或仅用少量任务数据高水平完成下游任务；该能力已在视觉、语言与语音中得到展示，但在难以采集真实数据的机器人领域仍有待证明。本文认为通用机器人模型成功的关键在于开放式、任务无关训练，以及能吸收多样机器人数据的高容量架构。提出名为 Robotics Transformer 的模型类，展现有前景的可扩展模型性质，并基于真实机器人执行真实任务的大规模数据采集，研究不同模型类随数据规模、模型规模与数据多样性而泛化的能力。

**要点：**

- **方法：** 以开放式、任务无关训练结合高容量 Robotics Transformer 架构，吸收大规模多样真实机器人数据。
- **贡献：** 提出具有可扩展性质的 Robotics Transformer，并系统考察数据规模、模型规模与数据多样性对泛化的影响。
- **关系：** 是大规模真实机器人控制 Transformer 的先导，直接孕育后续 `VLA`；本文并不研究 `World Model` 或 `VLN`。

---

<a id="p-268"></a>

### 268. Socratic Models: Composing Zero-Shot Multimodal Reasoning with Language

- **年份：** 2022
- **标签：** `agent-robot` · `llm-agent` · `VLM`
- **链接：** [arXiv:2204.00598](https://arxiv.org/abs/2204.00598)

**摘要：** 不同基础模型能力域仅部分重叠：`VLM` 擅长图像—语言，LLM 擅长互联网文本推理。Socratic Models 用语言作信息瓶颈，把多个预训练多模态模块组合成零样本多模态推理系统，而无需微调。该组合可做图像描述、问答与多模态辅助，并在机器人演示中把视觉检测接到 LLM 规划再调用语言条件策略。

**要点：**

- **方法：** 以语言为瓶颈组合多个冻结基础模型，做零样本多模态推理。
- **贡献：** 无需微调即可完成描述、问答与机器人模块化规划演示。
- **关系：** 模块化 `VLM`+LLM Agent 范式，后续 Code as Policies / SayCan 栈常沿用。

---

<a id="p-269"></a>

### 269. TransDreamer: Reinforcement Learning with Transformer World Models

- **年份：** 2022
- **标签：** `world_model`
- **链接：** [arXiv:2202.09481](https://arxiv.org/abs/2202.09481)

**摘要：** Dreamer 智能体具备基于模型强化学习的样本效率、可复用知识与安全规划等益处，但其 `World Model` 与策略网络继承了循环神经网络的局限。本文提出基于 Transformer 的模型强化学习智能体 TransDreamer：先引入用 Transformer 做动力学预测的 `World Model`——Transformer State-Space Model；再与基于 Transformer 的策略网络共享该 `World Model`，从而在训练基于 Transformer 的强化学习智能体时获得稳定性。实验将其用于需要长程记忆访问以进行基于记忆推理的二维视觉强化学习与三维第一人称视觉强化学习任务，并表明该模型在这些复杂任务上优于 Dreamer。

**要点：**

- **方法：** 提出 Transformer State-Space Model 做动力学预测，并与基于 Transformer 的策略网络共享该 `World Model`。
- **贡献：** 在需要长程记忆推理的二维与三维第一人称视觉强化学习任务上，TransDreamer 优于 Dreamer。
- **关系：** 属于用 Transformer 增强 `World Model` 的工作，并未涉及 `VLA`、`VLN` 或 `VLM`。

---

<a id="p-270"></a>

### 270. Transformers are Sample-Efficient World Models

- **年份：** 2022
- **标签：** `world_model`
- **链接：** [arXiv:2209.00588](https://arxiv.org/abs/2209.00588)

**摘要：** 深度强化学习智能体样本效率低，限制了现实应用。许多基于模型的方法试图解决这一问题，在 `World Model` 的想象中学习是突出途径之一，但 `World Model` 必须在较长时间上保持准确。受 Transformer 在序列建模中成功的启发，提出数据高效智能体 IRIS，在由离散自编码器和自回归 Transformer 组成的 `World Model` 中学习。在 Atari 100k 基准上仅相当于约两小时游戏时间，平均人类归一化得分为 1.046，在二十六款游戏中的十款超过人类，为无前瞻搜索方法树立新的先进水平。

**要点：**

- **方法：** 用离散自编码器与自回归 Transformer 构成 `World Model`，并在其想象中训练数据高效智能体 IRIS。
- **贡献：** 在 Atari 100k 上以约两小时等价交互取得 1.046 的平均人类归一化得分，为无前瞻搜索方法达到新的先进水平。
- **关系：** 属于样本高效 Transformer `World Model` 工作，并未涉及 `VLA`、`VLN` 或 `VLM`。

---

<a id="p-271"></a>

### 271. VIMA: General Robot Manipulation with Multimodal Prompts

- **年份：** 2022
- **标签：** `VLM`
- **链接：** [arXiv:2210.03094](https://arxiv.org/abs/2210.03094)

**摘要：** 基于提示的学习使通才语言模型可由输入提示执行指定任务，但机器人中的任务指定形式多样，常被视为不同任务并由专用模型处理。本文表明广泛的机器人操作任务可用交织文本与视觉 token 的多模态提示来表达，并构建包含数千个程序生成桌面任务、六十万余条专家轨迹与四级系统泛化评估协议的新仿真基准。设计基于 Transformer 的机器人智能体 VIMA，处理这些提示并自回归输出电机动作，兼具模型可扩展性与数据效率；在最难的零样本泛化设定下，同等数据时任务成功率最高可达其他设计的 2.9 倍，以 10 倍更少数据仍优于最佳竞争变体 2.7 倍。

**要点：**

- **方法：** 用交织文本与视觉 token 的多模态提示指定操作任务，并由 Transformer 智能体 VIMA 自回归输出电机动作。
- **贡献：** 发布含大量专家轨迹与四级泛化评估的仿真基准，并显示 VIMA 在零样本泛化与数据效率上优于替代设计。
- **关系：** 以多模态提示统一操作任务规格，衔接 `VLM` 与机器人动作；本文并不研究 `World Model` 或 `VLN`。

---

## 2021 年

共 1 篇。先扫目录，再下翻卡片。

- [272. CLIPort: What and Where Pathways for Robotic Manipulation](#p-272)  `agent-robot` · `VLM`

<a id="p-272"></a>

### 272. CLIPort: What and Where Pathways for Robotic Manipulation

- **年份：** 2021
- **标签：** `agent-robot` · `VLM`
- **链接：** [arXiv:2109.12098](https://arxiv.org/abs/2109.12098)

**摘要：** 精确操作与抽象概念推理难以兼得：端到端网络空间推理强但难泛化到新目标，而 CLIP 等语义模型缺空间精度。CLIPort 把语言条件的 CLIP 语义（what）与 Transporter 的空间操作（where）两条通路结合，用两个流式网络实现表格堆叠等语言条件操作。在未见物体、属性与未见语言上均能零样本泛化，并在多任务语言条件表格操作上设立强基线。

**要点：**

- **方法：** 以 CLIP 语义通路与 Transporter 空间通路双流实现语言条件操作。
- **贡献：** 在未见物体与未见语言上零样本泛化，并给出多任务表格操作强基线。
- **关系：** 早期语言条件操作智能体，用 `VLM` 语义接地动作，尚非端到端 `VLA`。

---

## 2020 年

共 1 篇。先扫目录，再下翻卡片。

- [273. Mastering Atari with Discrete World Models](#p-273)  `world_model`

<a id="p-273"></a>

### 273. Mastering Atari with Discrete World Models

- **年份：** 2020
- **标签：** `world_model`
- **链接：** [arXiv:2010.02193](https://arxiv.org/abs/2010.02193)

**摘要：** `World Model` 促进从经验泛化，并允许从想象结果学习行为以提高样本效率。从图像学习 `World Model` 对部分任务已可行，但足够准确地建模 Atari 游戏以导出成功行为长期仍是开放挑战。提出 DreamerV2：在强大 `World Model` 的紧凑潜空间中纯从预测学习行为；该 `World Model` 使用离散表示并与策略分开训练。它是首个通过在单独训练的 `World Model` 内学习行为、在五十五项 Atari 基准上达到人类水平的智能体；同等计算预算与墙上时间下达到 2 亿帧并超过 IQN 与 Rainbow 的最终表现。亦适用于连续动作，从像素学习复杂人形机器人的准确 `World Model` 并解决站立与行走。

**要点：**

- **方法：** 单独训练使用离散表示的 `World Model`，并在其紧凑潜空间的预测中纯学习行为。
- **贡献：** DreamerV2 首次在五十五项 Atari 任务上通过分离训练的 `World Model` 达到人类水平，并可用于像素输入的连续控制。
- **关系：** 是离散潜空间 `World Model` 的关键进展，并未涉及 `VLA`、`VLN` 或 `VLM`。

---

## 2019 年

共 1 篇。先扫目录，再下翻卡片。

- [274. Dream to Control: Learning Behaviors by Latent Imagination](#p-274)  `world_model`

<a id="p-274"></a>

### 274. Dream to Control: Learning Behaviors by Latent Imagination

- **年份：** 2019
- **标签：** `world_model`
- **链接：** [arXiv:1912.01603](https://arxiv.org/abs/1912.01603)

**摘要：** 所学 `World Model` 总结智能体经验以促进学习复杂行为。尽管通过深度学习从高维感官输入学习 `World Model` 正变得可行，从中导出行为仍有多种潜在途径。提出 Dreamer：纯通过潜空间想象从图像解决长时程任务的强化学习智能体。在所学 `World Model` 的紧凑状态空间中想象轨迹，并将所学状态价值的解析梯度沿轨迹反向传播，从而高效学习行为。在二十项具有挑战性的视觉控制任务上，Dreamer 在数据效率、计算时间与最终性能上超过现有方法。

**要点：**

- **方法：** 在所学 `World Model` 的紧凑状态空间中想象轨迹，并将状态价值的解析梯度沿想象轨迹反向传播以学习行为。
- **贡献：** Dreamer 可纯从图像通过潜空间想象解决长时程任务，并在二十项视觉控制任务上于效率与性能上超过现有方法。
- **关系：** 奠定在潜空间想象中学习控制的 `World Model` 范式，并未涉及 `VLA`、`VLN` 或 `VLM`。

---

## 2018 年

共 2 篇。先扫目录，再下翻卡片。

- [275. Learning Latent Dynamics for Planning from Pixels](#p-275)  `world_model`
- [276. World Models](#p-276)  `world_model`

<a id="p-275"></a>

### 275. Learning Latent Dynamics for Planning from Pixels

- **年份：** 2018
- **标签：** `world_model`
- **链接：** [arXiv:1811.04551](https://arxiv.org/abs/1811.04551)

**摘要：** 规划在已知环境动力学的控制任务中非常成功；要在未知环境中利用规划，智能体需从与世界的交互中学习动力学。学习对规划足够准确的动力学模型长期具有挑战，尤其在基于图像的领域。提出纯基于模型的智能体 Deep Planning Network（PlaNet）：从图像学习环境动力学，并在潜空间中通过快速在线规划选择动作。为准确预测多步超前奖励，采用兼具确定性与随机转移分量的潜动力学模型，并提出名为 latent overshooting 的多步变分推断目标。仅用像素观测即可解决含接触动力学、部分可观测与稀疏奖励的连续控制任务，所用回合更少且最终性能接近有时高于强无模型算法。

**要点：**

- **方法：** 用兼具确定性与随机转移的潜动力学模型，并以 latent overshooting 多步变分目标从图像学习，再在潜空间在线规划。
- **贡献：** PlaNet 仅用像素即可解决更难的接触、部分可观测与稀疏奖励连续控制，且样本效率优于或接近强无模型算法。
- **关系：** 是从像素学习潜动力学并做规划的早期 `World Model` 工作，并未涉及 `VLA`、`VLN` 或 `VLM`。

---

<a id="p-276"></a>

### 276. World Models

- **年份：** 2018
- **标签：** `world_model`
- **链接：** [arXiv:1803.10122](https://arxiv.org/abs/1803.10122)

**摘要：** 本文探索为流行的强化学习环境构建生成式神经网络模型。所提出的 `World Model` 能够以无监督方式快速训练，从而学习到环境在空间与时间维度上的压缩表示。通过将从该 `World Model` 中提取的特征作为智能体的输入，可以训练出非常紧凑且简单的策略来完成所需任务。甚至可以让智能体完全在由其自身 `World Model` 所生成的幻觉梦境内部接受训练，随后再把所得策略迁移回实际环境中执行。论文还提供了交互式版本。

**要点：**

- **方法：** 以无监督方式快速训练生成式神经网络 `World Model`，学习环境的压缩空间与时间表示。
- **贡献：** 可用 `World Model` 特征训练紧凑策略，甚至完全在其生成的梦境中训练智能体再将策略迁回真实环境。
- **关系：** 提出在 `World Model` 梦境中学习策略的经典范式，并未涉及 `VLA`、`VLN` 或 `VLM`。

---
