"""Hand-written Chinese paraphrases for newly added, arXiv-verified papers.

English abstracts come only from arXiv abs/API fetches. Do not invent IDs or abstracts.
"""

# tags: world_model | VLA | VLN | VLM | intersection | agent-robot | llm-agent
# sources: agent_robot | world_model | vla_vln_vlm

KEEP = {
    "2109.12098": {
        "tags": ["agent-robot", "VLM"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "精确操作与抽象概念推理难以兼得：端到端网络空间推理强但难泛化到新目标，而 CLIP 等语义模型缺空间精度。CLIPort 把语言条件的 CLIP 语义（what）与 Transporter 的空间操作（where）两条通路结合，用两个流式网络实现表格堆叠等语言条件操作。在未见物体、属性与未见语言上均能零样本泛化，并在多任务语言条件表格操作上设立强基线。",
        "highlights_zh": [
            "方法：以 CLIP 语义通路与 Transporter 空间通路双流实现语言条件操作。",
            "贡献：在未见物体与未见语言上零样本泛化，并给出多任务表格操作强基线。",
            "与 Agent / WM×VLA/VLN/VLM：早期语言条件操作智能体，用 VLM 语义接地动作，尚非端到端 VLA。",
        ],
    },
    "2201.07207": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "本文探讨能否把大语言模型学到的世界知识落地为可执行步骤，例如把「做早餐」映射为「打开冰箱」。作者评估若干提示方法，发现预训练 LLM 的计划常不可执行。他们提出可容许动作翻译，把自由生成计划映射到环境中可用动作，从而显著提高可执行性。该工作是后续 SayCan、Inner Monologue 与 Code as Policies 等机器人 Agent 的规划前驱。",
        "highlights_zh": [
            "方法：用可容许动作翻译把 LLM 自由计划映射到环境可行动作。",
            "贡献：系统评估零样本 LLM 规划的可执行性缺口，并给出可落地的动作映射。",
            "与 Agent / WM×VLA/VLN/VLM：语言规划 Agent 地标，本身不是 VLA 或 World Model。",
        ],
    },
    "2204.00598": {
        "tags": ["agent-robot", "llm-agent", "VLM"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "不同基础模型能力域仅部分重叠：VLM 擅长图像—语言，LLM 擅长互联网文本推理。Socratic Models 用语言作信息瓶颈，把多个预训练多模态模块组合成零样本多模态推理系统，而无需微调。该组合可做图像描述、问答与多模态辅助，并在机器人演示中把视觉检测接到 LLM 规划再调用语言条件策略。",
        "highlights_zh": [
            "方法：以语言为瓶颈组合多个冻结基础模型，做零样本多模态推理。",
            "贡献：无需微调即可完成描述、问答与机器人模块化规划演示。",
            "与 Agent / WM×VLA/VLN/VLM：模块化 VLM+LLM Agent 范式，后续 Code as Policies / SayCan 栈常沿用。",
        ],
    },
    "2206.08853": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "开放世界智能体需要多样任务环境、大规模多模态知识与可扩展架构。MineDojo 在 Minecraft 上提供数千开放任务与互联网规模的视频、教程、维基与论坛知识库，并训练 MineCLIP 作为语言条件稠密奖励。该平台成为 Voyager、STEVE-1 与 GITM 等开放式具身 Agent 的共同底座。",
        "highlights_zh": [
            "方法：以 Minecraft 开放任务套件加互联网知识库，并训练 MineCLIP 语言条件奖励。",
            "贡献：为开放式具身智能体提供可扩展环境与多模态知识基础设施。",
            "与 Agent / WM×VLA/VLN/VLM：开放式 Agent 平台，不是 World Model 或 VLA 策略本身。",
        ],
    },
    "2207.04429": {
        "tags": ["agent-robot", "llm-agent", "VLN"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "视觉导航目标常用图像指定，接口不自然。LM-Nav 组合预训练语言模型、视觉—语言模型与视觉导航模型：LLM 把自由语言指令分解为地标列表，VLM 在拓扑图上接地这些地标，导航模型再执行。系统在真实户外环境中用语言指令导航，且无需语言标注的导航轨迹。",
        "highlights_zh": [
            "方法：LLM 分解指令、VLM 接地地标、视觉导航模型执行，三者均用预训练。",
            "贡献：在真实户外用自由语言导航，无需语言标注轨迹。",
            "与 Agent / WM×VLA/VLN/VLM：语言 Agent 控制导航，属 VLN 与模块化 VLM 交叉。",
        ],
    },
    "2209.07753": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "Code as Policies 把会写代码的 LLM 重用于生成机器人策略程序：策略代码可表达反馈回路、调用感知与控制原语，并引用 NumPy 等库做几何推理。通过少样本「指令注释 + 策略代码」提示与层次化代码生成（递归定义未定义函数），模型可写出反应式与航点式策略，并在多台真机上演示。层次化代码生成还将 HumanEval 求解率提升至 39.8%。",
        "highlights_zh": [
            "方法：以层次化代码生成把自然语言指令编译为可执行策略程序（LMP）。",
            "贡献：在真机上实现反应式与航点策略，并提升 HumanEval 求解率。",
            "与 Agent / WM×VLA/VLN/VLM：Agent 控制机器人的代码即策略地标，后续 ProgPrompt / VoxPoser 沿此线。",
        ],
    },
    "2209.11302": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "任务规划通常需要大量领域知识。ProgPrompt 用程序化提示让 LLM 直接生成情境化机器人任务计划：提示包含环境状态、可用动作与示例，使生成计划可在真实与仿真机器人上执行。相对仅打分下一步的方法，直接生成动作序列更易利用 LLM 的程序结构，并在桌面操作任务上提高成功率。",
        "highlights_zh": [
            "方法：用包含状态与可用动作的程序化提示，让 LLM 生成可执行任务计划。",
            "贡献：在仿真与真机桌面任务上提高计划可执行性与成功率。",
            "与 Agent / WM×VLA/VLN/VLM：与 Code as Policies 并列的规划 Agent，强调情境化程序提示。",
        ],
    },
    "2210.03629": {
        "tags": ["llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "LLM 的推理（思维链）与行动（生成动作计划）此前多被分开研究。ReAct 交错生成推理轨迹与任务动作，使模型能规划、跟踪与更新行动，并处理异常。在问答与决策基准上，ReAct 优于仅推理或仅行动的基线，并减少幻觉。该范式被广泛接到机器人闭环（Inner Monologue、Voyager、VLN 工具调用）。",
        "highlights_zh": [
            "方法：交错生成推理轨迹与动作，形成思考—行动闭环。",
            "贡献：在问答与决策任务上优于单模态基线，并降低幻觉。",
            "与 Agent / WM×VLA/VLN/VLM：通用 LLM Agent 地标，机器人 ReAct 式闭环的直接前驱（非 VLA 实验）。",
        ],
    },
    "2212.04088": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "LLM-Planner 把大语言模型用作具身智能体的少样本规划器：在视觉感知环境中跟随自然语言指令。为降低数据成本，它用 LLM 生成高层子目标，再与学得的低层策略结合，并可在执行中根据观察重新规划。在 ALFRED 等基准上，少样本设定下即可达到有竞争力的成功率。",
        "highlights_zh": [
            "方法：LLM 少样本生成子目标并与低层策略结合，支持执行中重规划。",
            "贡献：在 ALFRED 等具身指令任务上以少样本取得有竞争力的成功。",
            "与 Agent / WM×VLA/VLN/VLM：规划 Agent 控制具身执行，属语言规划而非端到端 VLA。",
        ],
    },
    "2302.01560": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "开放世界多任务规划面临长时程推理与计划不可执行的难题。DEPS（Describe, Explain, Plan and Select）用交互式规划：描述当前处境、解释失败、生成计划并选择可执行技能。在 Minecraft 中，该方法显著提高长时程任务完成率，成为 Voyager 之前的开放世界规划 Agent 代表。",
        "highlights_zh": [
            "方法：描述—解释—规划—选择的交互式 LLM 规划，把失败反馈写入下一轮。",
            "贡献：在 Minecraft 长时程多任务上提高计划可执行性与完成率。",
            "与 Agent / WM×VLA/VLN/VLM：开放世界规划 Agent，技能选择接口可接到控制器而非 VLA。",
        ],
    },
    "2303.11366": {
        "tags": ["llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "语言智能体难以像传统强化学习那样从试错中快速学习。Reflexion 用语言形式的强化：智能体把环境反馈转成语言反思并写入情景记忆，供后续试验使用，而无需更新模型权重。在决策、编程与推理任务上显著提升，成为机器人自我纠错 Agent 的常用组件。",
        "highlights_zh": [
            "方法：以语言反思作言语强化学习，写入记忆供后续试验，不更新权重。",
            "贡献：在决策、编程与推理任务上显著提升试错学习效率。",
            "与 Agent / WM×VLA/VLN/VLM：规划 / 工具使用 Agent 地标，机器人闭环常复用其反思回路。",
        ],
    },
    "2303.12153": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "Text2Motion 把自然语言指令转为几何可行的任务—运动计划。框架用少样本 LLM 构造符号目标与技能序列，再用运动规划验证几何可行性；不可行则反馈重规划。相对纯 LLM 计划，它能完成需要长时程几何推理的顺序操作，并在仿真操作任务上提高成功。",
        "highlights_zh": [
            "方法：LLM 符号规划与运动规划可行性检验交替，失败则反馈重规划。",
            "贡献：把语言指令落到几何可行的长时程操作计划。",
            "与 Agent / WM×VLA/VLN/VLM：规划 Agent 与经典运动规划耦合，不是端到端 VLA。",
        ],
    },
    "2303.17580": {
        "tags": ["llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "HuggingGPT 用 ChatGPT 作控制器，调度 Hugging Face 上的专家模型完成跨域跨模态任务：LLM 负责任务规划、模型选择、参数生成与结果汇总。该工作展示工具使用 Agent 如何把语言计划接到可调用技能库，为机器人 tool-use 提供非具身对照。",
        "highlights_zh": [
            "方法：以 LLM 规划并调度外部专家模型，完成跨模态任务。",
            "贡献：展示工具使用 Agent 的规划—选模型—执行—汇总回路。",
            "与 Agent / WM×VLA/VLN/VLM：工具使用规划 Agent 地标，本身不是机器人或 VLA 实验。",
        ],
    },
    "2304.11477": {
        "tags": ["llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "LLM 零样本问答强，但长时程规划不可靠；经典规划器在问题形式化后很强。LLM+P 让 LLM 把语言指令译为 PDDL，再调用最优规划器求解，最后把计划译回自然语言。该方法在规划基准上显著优于仅用 LLM 的计划，为机器人符号规划 Agent 提供可组合接口。",
        "highlights_zh": [
            "方法：LLM 将指令译为 PDDL，经典规划器求最优计划后再译回语言。",
            "贡献：在规划基准上明显优于纯 LLM 计划。",
            "与 Agent / WM×VLA/VLN/VLM：规划 Agent 与符号规划器的工具使用组合，可接到机器人任务规划。",
        ],
    },
    "2305.05658": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "家居整理需要把用户偏好泛化到新场景。TidyBot 用 LLM 从少量示例中总结「东西放哪」的偏好，再结合预训练感知与抓放技能在真实房间整理。系统可个性化放置规则，并在真实家庭环境中完成拾取—放置，展示语言 Agent 对真机家务的控制。",
        "highlights_zh": [
            "方法：用 LLM 从少量示例归纳放置偏好，再调用感知与抓放技能。",
            "贡献：在真实房间实现可个性化的整理辅助。",
            "与 Agent / WM×VLA/VLN/VLM：家用机器人 Agent，语言规划 + 技能原语，而非端到端 VLA。",
        ],
    },
    "2305.11176": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "Instruct2Act 用 LLM 把多模态指令映射为机器人顺序动作：生成调用 SAM、CLIP 等感知工具与操作原语的 Python 程序。框架保留专家技能接口，同时利用 LLM 的零样本多模态推理，在表格操作等任务上实现灵活的指令跟随。",
        "highlights_zh": [
            "方法：LLM 生成调用 SAM/CLIP 与操作原语的程序，映射多模态指令。",
            "贡献：在保留专家技能的同时实现灵活的零样本指令跟随。",
            "与 Agent / WM×VLA/VLN/VLM：代码即策略 + 视觉工具使用的机器人 Agent。",
        ],
    },
    "2305.15021": {
        "tags": ["agent-robot", "llm-agent", "VLM"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "EmbodiedGPT 是面向具身人工智能的端到端多模态基础模型，用具身思维链做视觉—语言预训练，使智能体具备多模态理解与规划执行能力。模型在具身规划、视觉问答与操作相关基准上提升，展示把 VLM 预训练接到动作序列的路径。",
        "highlights_zh": [
            "方法：以具身思维链做视觉—语言预训练，端到端赋能规划与执行。",
            "贡献：在具身规划、VQA 与操作相关任务上提升多模态基础能力。",
            "与 Agent / WM×VLA/VLN/VLM：VLM Agent 预训练，通向规划式控制而非纯 World Model。",
        ],
    },
    "2305.16291": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "Voyager 是 Minecraft 中首个由 LLM 驱动的终身学习具身智能体：自动课程最大化探索，可增长的技能库存储可执行代码，迭代提示融入环境反馈、执行错误与自验证。它不微调模型参数，仅黑盒查询 GPT-4。相对先前方法，获得更多独特物品、旅行更远，科技树里程碑最快约 15.3 倍，并可将技能库迁移到新世界。",
        "highlights_zh": [
            "方法：自动课程 + 可执行技能库 + 带反馈的迭代代码提示，黑盒调用 GPT-4。",
            "贡献：开放式 Minecraft 终身学习，物品、行程与科技树进度显著领先，技能可迁移。",
            "与 Agent / WM×VLA/VLN/VLM：开放式具身 Agent 地标，代码技能库控制「机器人式」游戏本体。",
        ],
    },
    "2305.17144": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "Ghost in the Minecraft（GITM）针对开放世界一般能力，而非单一「获得钻石」。它用 LLM 做层次化规划与结构化文本接口，把 Minecraft 交互表示为可推理的文本世界，从而在广泛任务上取得一般能力。相对目标单一的智能体，GITM 更强调开放任务覆盖与规划—执行分解。",
        "highlights_zh": [
            "方法：以 LLM 层次化规划与结构化文本接口操作 Minecraft。",
            "贡献：面向开放世界一般能力，而非单一钻石目标。",
            "与 Agent / WM×VLA/VLN/VLM：与 Voyager 并列的开放式 Agent，文本接口控制具身环境。",
        ],
    },
    "2306.00937": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "STEVE-1 把 VPT 行为基础模型按 unCLIP 思路做指令微调：先在 MineCLIP 潜空间对齐指令，再训练文本先验，从而用自监督行为克隆与事后重标注降低文本标注成本（约 60 美元算力）。它用原始像素与键鼠低层控制跟随短时程开放指令，在早期游戏评测中稳健完成 13 项中的 12 项。",
        "highlights_zh": [
            "方法：在 MineCLIP 潜空间指令微调 VPT，并训练文本先验。",
            "贡献：低成本实现 Minecraft 短时程开放指令跟随，12/13 项任务稳健完成。",
            "与 Agent / WM×VLA/VLN/VLM：开放式具身控制 Agent，低层策略可与 LLM 规划器组合。",
        ],
    },
    "2306.03310": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "LIBERO 提供面向终身机器人学习的知识迁移基准，覆盖程序性、目标与操作知识的前向迁移。它包含仿真操作任务套件与评测协议，成为后续 VLA 与层次化 Agent 的常用操作评测床。",
        "highlights_zh": [
            "方法：构建区分程序性 / 目标 / 操作知识迁移的终身操作基准。",
            "贡献：为通用操作策略与层次化 Agent 提供可比较的仿真评测。",
            "与 Agent / WM×VLA/VLN/VLM：VLA 与 Agent 编排常用评测床，本身不是新控制算法。",
        ],
    },
    "2306.08647": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "Language to Rewards 让用户用自然语言描述想要的机器人技能，LLM 生成奖励代码，再在仿真中用强化学习优化低层控制器。该「语言→奖励程序→RL」回路可合成新的运动技能，展示代码生成 Agent 对控制器训练的间接控制。",
        "highlights_zh": [
            "方法：LLM 把语言技能描述编译为奖励程序，再用强化学习训练控制器。",
            "贡献：用语言合成新运动技能，形成可迭代的奖励设计回路。",
            "与 Agent / WM×VLA/VLN/VLM：代码 / 奖励设计 Agent，控制的是训练目标而非在线 VLA。",
        ],
    },
    "2306.17582": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "ChatGPT for Robotics 总结用对话式 LLM 设计机器人应用的原则：提示中暴露高层 API、用语言做任务分解与代码生成，并在多种机器人平台上演示。论文讨论模型能力、安全与人机协作，是工业界早期「对话 Agent 控制机器人」的系统设计报告。",
        "highlights_zh": [
            "方法：以高层 API 提示 ChatGPT 做任务分解与控制代码生成。",
            "贡献：给出跨平台机器人对话应用的设计原则与能力观察。",
            "与 Agent / WM×VLA/VLN/VLM：对话 Agent 控制机器人的工程地标，非 VLA 权重模型。",
        ],
    },
    "2306.17840": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "Statler 让 LLM 维护对不可观测世界状态的估计，并在动作后更新该状态，再据此条件生成下一步。相对 Code as Policies 等仅依赖对话历史的方法，显式状态读写显著提高若干机器人规划任务的成功，并更利于长时程扩展。",
        "highlights_zh": [
            "方法：世界状态读—写双 LLM，在显式状态估计上条件生成动作。",
            "贡献：在多项机器人规划上优于 Code as Policies 等强基线。",
            "与 Agent / WM×VLA/VLN/VLM：用语言模型维护符号世界状态，属 Agent 规划而非学得 World Model。",
        ],
    },
    "2307.02485": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "CoELA 针对分散控制、原始感知、有代价通信与多目标任务，把 LLM 嵌入感知、记忆、通信、规划与执行五个模块。在 C-WAH 与 TDW-MAT 上，GPT-4 驱动的 CoELA 超过强规划基线并出现有效通信；对 LLaMA-2 微调的 CoLLAMA 也取得可行表现，人机协作中自然语言通信更获信任。",
        "highlights_zh": [
            "方法：模块化认知架构把 LLM 用于通信与规划，形成合作具身语言智能体。",
            "贡献：分散多智体合作超过规划基线，并展示人机自然语言协作。",
            "与 Agent / WM×VLA/VLN/VLM：多智能体机器人 / 具身合作 Agent 地标。",
        ],
    },
    "2307.04738": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "RoCo 让多机器人用 LLM 对话协商高层策略，再生成子任务与任务空间航点，交给多臂运动规划器。环境碰撞等反馈被写回提示以改进计划。配套 RoCoBench 覆盖六类协作场景；仿真成功率高，真机还可接入人机对话协作。",
        "highlights_zh": [
            "方法：多机器人 LLM 对话 + 航点生成 + 多臂运动规划，并闭环反馈。",
            "贡献：提出 RoCoBench，仿真与真机展示可解释的多机器人协作。",
            "与 Agent / WM×VLA/VLN/VLM：多智能体机器人协作 Agent，规划层为 LLM 而非 VLA。",
        ],
    },
    "2307.05973": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "VoxPoser 用语言模型合成可组合的三维价值图，表示操作约束与目标，再用运动规划在价值图上求解轨迹。系统无需任务演示，即可在真实与仿真中完成多样语言条件操作，并组合空间约束。它把语言推理接到三维几何，是代码 / 价值图 Agent 控制机械臂的代表。",
        "highlights_zh": [
            "方法：LLM 合成可组合 3D 价值图，运动规划在其上求解操作轨迹。",
            "贡献：无任务演示即可完成多样语言条件真实操作。",
            "与 Agent / WM×VLA/VLN/VLM：语言 Agent 通过 3D 价值图控制机器人，非端到端 VLA。",
        ],
    },
    "2308.10141": {
        "tags": ["VLN", "llm-agent"],
        "sources": ["vla_vln_vlm", "agent_robot"],
        "abstract_zh": "March in Chat 研究远程具身指代表达（REVERIE 一类）：用交互式提示让 LLM 在对话中逐步明确导航与指代目标。方法把语言交互接到具身导航，展示对话 Agent 如何服务 VLN 式远程指令。",
        "highlights_zh": [
            "方法：交互式对话提示逐步澄清远程具身指代与导航目标。",
            "贡献：把对话式 LLM 接到远程具身指代表达任务。",
            "与 Agent / WM×VLA/VLN/VLM：对话 Agent 服务 VLN / 指代导航，文中非 World Model。",
        ],
    },
    "2309.10062": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "SMART-LLM 用少样本程序化提示完成多机器人任务分解、联盟形成与任务分配，把高层指令转为多机器人计划。作者构建按复杂度分档的基准，并在仿真与真机上验证计划生成。相对每机器人一个 LLM 的对话方案，它用中央 LLM 简化异构团队协调。",
        "highlights_zh": [
            "方法：中央 LLM 经分解—联盟—分配三阶段生成多机器人任务计划。",
            "贡献：提出多机器人规划基准，并在仿真与真机上验证。",
            "与 Agent / WM×VLA/VLN/VLM：多智能体任务规划 Agent，不训练 VLA。",
        ],
    },
    "2309.17080": {
        "tags": ["world_model"],
        "sources": ["world_model"],
        "abstract_zh": "GAIA-1 是面向自动驾驶的生成式世界模型，用视频、文本与动作预测未来驾驶场景。它展示基础模型尺度的驾驶世界模拟，但官方代码与权重未开放，是本包诚实标注的闭源 World Model 地标。",
        "highlights_zh": [
            "方法：以视频、文本与动作为条件的生成式驾驶世界模型。",
            "贡献：展示可提示、可动作条件的驾驶未来预测。",
            "与 Agent / WM×VLA/VLN/VLM：驾驶 World Model 地标；官方栈未开放。",
        ],
    },
    "2310.09615": {
        "tags": ["world_model"],
        "sources": ["world_model"],
        "abstract_zh": "STORM 用随机 Transformer 世界模型做样本高效强化学习：在潜空间对随机动力学建模，并在想象中训练策略。作为 Transformer World Model 一线（与 IRIS / TWM 并列），它补全本包此前仅有仓库、缺少论文卡片的缺口。",
        "highlights_zh": [
            "方法：随机 Transformer 世界模型在潜空间建模动力学并想象训练策略。",
            "贡献：为样本高效 RL 提供 Transformer WM 代表方法。",
            "与 Agent / WM×VLA/VLN/VLM：纯 World Model RL，摘要未做 VLA/VLN。",
        ],
    },
    "2310.12931": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "Eureka 用编码 LLM 做人类水平的奖励设计：在仿真中进化可执行奖励函数，覆盖 29 个机器人任务，并达到与人类奖励相当或更好的表现。它把「写奖励代码」作为 Agent 技能，用于训练低层控制器，开源代码已核验。",
        "highlights_zh": [
            "方法：编码 LLM 进化可执行奖励函数，在仿真中训练机器人技能。",
            "贡献：在 29 个任务上达到人类水平奖励设计。",
            "与 Agent / WM×VLA/VLN/VLM：奖励代码 Agent 间接控制机器人学习，非在线 VLA。",
        ],
    },
    "2311.01455": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "RoboGen 是生成式机器人智能体：自动提出任务、生成仿真场景与训练监督，再选择强化学习、运动规划或轨迹优化来学技能。提出—生成—学习循环可反复查询，产生无限多样的技能演示，覆盖刚体、软体与腿式运动。",
        "highlights_zh": [
            "方法：基础模型自动提出任务、生成场景与监督，再选择学习算法练技能。",
            "贡献：以生成式仿真规模化机器人技能学习，减少人工设计。",
            "与 Agent / WM×VLA/VLN/VLM：生成式 Agent 控制「学什么、在哪学」，而非部署期 VLA。",
        ],
    },
    "2311.01977": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "RT-Trajectory 用事后轨迹草图作为任务泛化的条件：把期望的末端轨迹画成或生成为草图，再训练策略跟随。相对纯语言条件，轨迹草图提供更密的时空指导，提高对新任务与新物体的泛化。",
        "highlights_zh": [
            "方法：以事后轨迹草图条件训练机器人策略，补充语言指令。",
            "贡献：提高对未见任务的轨迹级泛化。",
            "与 Agent / WM×VLA/VLN/VLM：语言 / 轨迹条件策略，属 VLA 数据条件而非规划 Agent。",
        ],
    },
    "2311.05997": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "JARVIS-1 是开放世界多任务 Minecraft 智能体：多模态语言模型把视觉与指令映射为计划，再交给目标条件控制器，并用多模态记忆结合预训练知识与生存经验。它可完成 200 余项任务，短时程近乎完美；在获得钻石镐上可靠性约为先前 SOTA 的 5 倍。",
        "highlights_zh": [
            "方法：多模态 LLM 规划 + 目标条件控制 + 多模态记忆。",
            "贡献：覆盖 200+ 任务，钻石镐任务可靠性约 5 倍于先前 SOTA。",
            "与 Agent / WM×VLA/VLN/VLM：Voyager 之后的多模态开放式 Agent。",
        ],
    },
    "2311.12871": {
        "tags": ["agent-robot", "llm-agent", "VLA", "VLM"],
        "sources": ["agent_robot", "vla_vln_vlm", "researcher_pack"],
        "abstract_zh": "现有通用模型多依赖二维图像，对三维输入与三维世界中定义的任务（接地、具身推理与行动）能力有限。LEO 是面向三维世界的具身多模态通才智能体，统一任务接口、架构与目标，分两阶段训练：三维视觉—语言对齐，再做三维视觉—语言—动作（VLA）指令微调。作者收集物体级与场景级大规模数据，并用 LLM 辅助管线生成高质量三维视觉—语言数据。实验覆盖三维描述、问答、具身推理、导航与操作；消融与缩放分析为后续具身通才提供参照。代码与数据见项目页。",
        "highlights_zh": [
            "方法：两阶段训练——3D 视觉—语言对齐 + 3D VLA 指令微调；统一接口，并以 LLM 辅助生成 3D VL 数据。",
            "贡献：在三维描述、问答、具身推理、导航与操作上展示通才能力，并给出消融与缩放分析。",
            "与 Agent / WM×VLA/VLN/VLM：研究员包标为具身 LLM Agent；同时是 3D VLM / VLA 通才。",
        ],
    },
    "2312.02519": {
        "tags": ["agent-robot"],
        "sources": ["agent_robot"],
        "abstract_zh": "Creative Agents 研究开放式创造任务：用想象器把抽象语言变成具体目标（文本或扩散视觉想象），再由行为克隆或代码基础模型执行。在 Minecraft 生存模式中，智能体可按自由语言建造多样建筑，并用 GPT-4V 评估开放创造。",
        "highlights_zh": [
            "方法：想象器（LLM 或扩散）生成任务结果，再交给控制策略或代码模型。",
            "贡献：据称首次在生存模式完成多样建筑创造，并开源评测。",
            "与 Agent / WM×VLA/VLN/VLM：开放式创造 Agent；视觉想象接近 World Model 用途。",
        ],
    },
    "2312.13139": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "该文（GR-1）把大规模视频生成预训练用于视觉机器人操作：模型同时预测未来图像与动作，将互联网视频知识迁到操作策略。作为视频—语言—动作生成式通才的早期代表，它衔接后续 GR-2。",
        "highlights_zh": [
            "方法：大规模视频生成预训练后，联合预测未来帧与机器人动作。",
            "贡献：把网络视频知识迁到视觉操作通才策略。",
            "与 Agent / WM×VLA/VLN/VLM：生成式 VLA / 视频预测策略，含隐式世界预测。",
        ],
    },
    "2401.12202": {
        "tags": ["agent-robot", "VLM"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "OK-Robot 问：把开放知识模型（开放词汇检测、语言条件导航与抓取）拼成家用拾取—放置系统，真正重要的是什么。它给出模块化零样本框架，在真实家庭中做语言条件拾放，并分析各模块对成败的贡献。开源仓库已核验。",
        "highlights_zh": [
            "方法：模块化组合开放词汇感知、语言导航与抓取，做零样本家用拾放。",
            "贡献：在真实家庭评测并分析「开放知识集成」的关键因素。",
            "与 Agent / WM×VLA/VLN/VLM：模块化 Agent / VLM 技能编排，而非单一 VLA。",
        ],
    },
    "2401.12963": {
        "tags": ["agent-robot", "llm-agent", "VLM"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "AutoRT 用 VLM 做场景理解、用 LLM 提出多样指令，并借助「机器人宪法」过滤不安全任务，从而在未见场景以极少人工监督部署机器人车队。系统在 4 栋楼、20 余台机器人上收集 7.7 万真实回合，展示 LLM 控制机器人在真实环境中自主提出目标并采集数据。",
        "highlights_zh": [
            "方法：VLM 接地场景 + LLM 提案指令 + 机器人宪法安全过滤，编排车队采集。",
            "贡献：7 个月收集 7.7 万真实回合，指令更多样并更对齐人的偏好。",
            "与 Agent / WM×VLA/VLN/VLM：大规模 Agent 编排真机车队，服务后续 VLA 数据。",
        ],
    },
    "2401.14403": {
        "tags": ["agent-robot"],
        "sources": ["agent_robot"],
        "abstract_zh": "实验室内的移动操作常止于抓—移—放。本文提出开放世界移动操作系统，全栈处理真实门、柜、抽屉与冰箱等铰接物：先用少量数据行为克隆，再在分布外物体上在线练习。配套约 2 万美元的低成本移动操作平台。在卡内基梅隆校园 4 栋楼、20 个铰接物上，每物不足 1 小时在线学习即可把成功率从行为克隆的 50% 提高到 95%。",
        "highlights_zh": [
            "方法：少量行为克隆后再对未见铰接物做在线自适应，并给出低成本移动操作硬件。",
            "贡献：校园 4 栋楼 20 个铰接物上，在线学习约 1 小时内成功率由 50% 升至 95%。",
            "与 Agent / WM×VLA/VLN/VLM：开放世界移动操作技能，可被家用语言 Agent 当铰接物原语调用。",
        ],
    },
    "2403.09631": {
        "tags": ["VLA", "world_model", "intersection"],
        "sources": ["world_model", "vla_vln_vlm"],
        "abstract_zh": "3D-VLA 提出三维视觉—语言—动作生成式世界模型，在 3D 场景中把语言、感知与动作交互统一建模。它补全本包 OSS 已收录、论文卡片此前缺失的 WM×VLA 交叉地标。",
        "highlights_zh": [
            "方法：三维生成式世界模型统一语言、场景与动作交互。",
            "贡献：为具身交互提供 3D 条件的生成式 WM/VLA。",
            "与 Agent / WM×VLA/VLN/VLM：直接交叉 3D World Model 与 VLA。",
        ],
    },
    "2403.12945": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "DROID 是大规模野外机器人操作数据集，覆盖多样场景与任务，为通用 VLA 与世界模型微调提供真实轨迹。Ctrl-World 等后续工作即在其上训练。",
        "highlights_zh": [
            "方法：采集大规模野外真实操作轨迹并公开。",
            "贡献：为通才策略与视频 World Model 提供场景多样的真实数据。",
            "与 Agent / WM×VLA/VLN/VLM：VLA / WM 数据底座，本身不是 Agent 算法。",
        ],
    },
    "2405.12399": {
        "tags": ["world_model"],
        "sources": ["world_model"],
        "abstract_zh": "DIAMOND（Diffusion for World Modeling）表明视觉细节对 Atari 世界模型很重要：用扩散模型作世界模型并在想象中训练 RL 智能体。本包 OSS 已收录其仓库，此处补论文卡片。",
        "highlights_zh": [
            "方法：以扩散模型作为世界模型，在想象中训练智能体。",
            "贡献：强调像素级视觉细节对 Atari WM 的作用。",
            "与 Agent / WM×VLA/VLN/VLM：扩散 World Model RL，非语言 Agent。",
        ],
    },
    "2406.02523": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "RoboCasa 提供面向通才机器人的大规模日常任务仿真，支持语言条件家务操作数据生成与评测，常被 VLA 与层次化 Agent 用作仿真床。",
        "highlights_zh": [
            "方法：大规模日常家务仿真以支持通才机器人学习。",
            "贡献：为语言条件操作提供可扩展仿真与任务集。",
            "与 Agent / WM×VLA/VLN/VLM：VLA / Agent 仿真基础设施。",
        ],
    },
    "2406.11740": {
        "tags": ["world_model"],
        "sources": ["world_model"],
        "abstract_zh": "Imagination Policy 用生成式点云模型学习操作策略：在想象的三维未来上规划或条件生成动作。它把点云世界预测接到策略，属于 3D World Model 服务操作的一条线。",
        "highlights_zh": [
            "方法：生成式点云世界预测用于学习操作策略。",
            "贡献：把三维想象接到操作策略学习。",
            "与 Agent / WM×VLA/VLN/VLM：3D World Model × 操作策略。",
        ],
    },
    "2407.08693": {
        "tags": ["agent-robot", "VLA"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "Embodied Chain-of-Thought（ECoT）让机器人策略在输出动作前生成接地的推理轨迹，把 VLA 的端到端控制与 Agent 式思维链结合。实验表明具身推理痕迹可提高复杂指令跟随与可解释性。",
        "highlights_zh": [
            "方法：在 VLA 中插入具身思维链，先推理再输出动作。",
            "贡献：提升复杂指令跟随，并使决策更可解释。",
            "与 Agent / WM×VLA/VLN/VLM：把 ReAct 式推理接入 VLA 控制回路。",
        ],
    },
    "2408.14837": {
        "tags": ["world_model"],
        "sources": ["world_model"],
        "abstract_zh": "GameNGen 表明扩散模型可作实时游戏引擎：在动作条件下交互生成游戏画面，展示交互视频世界模型的实时性。官方可训练栈仍未核验开放，与本包缺口说明一致。",
        "highlights_zh": [
            "方法：动作条件扩散实时生成交互游戏帧。",
            "贡献：展示扩散世界模型作为实时神经游戏引擎的可行性。",
            "与 Agent / WM×VLA/VLN/VLM：交互视频 World Model 地标；官方 OSS 仍缺。",
        ],
    },
    "2409.01652": {
        "tags": ["agent-robot", "llm-agent", "VLM"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "ReKep 用关系关键点约束表示操作：约束是把环境中 3D 关键点映射为代价的 Python 函数，再分层优化得到 SE(3) 末端轨迹。VLM 与大视觉模型可从语言与 RGB-D 自动生成 ReKep，从而在移动单臂与双臂平台上无任务数据地完成多阶段、野外与双臂行为。",
        "highlights_zh": [
            "方法：VLM 生成 Python 关系关键点约束，优化器求解实时 SE(3) 动作。",
            "贡献：无任务数据与环境模型即可做多阶段、双臂与野外操作。",
            "与 Agent / WM×VLA/VLN/VLM：代码约束 Agent + VLM，而非端到端 VLA。",
        ],
    },
    "2409.15146": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "既有 LLM 任务规划多针对单机或同构简单任务。COHERENT 面向四旋翼、机器狗与机械臂等异构团队：中央分配器提出分解方案并分配子任务，各执行器选择可行动作并回报自我反思，经提案—执行—反馈—调整（PEFA）循环直至完成。配套 100 个长时程异构任务基准，成功率与执行效率大幅超过先前方法。",
        "highlights_zh": [
            "方法：PEFA 循环由中央 LLM 分解分配，异构执行器反馈并调整计划。",
            "贡献：覆盖四旋翼 / 机器狗 / 机械臂，并发布 100 任务基准，成功与效率明显提升。",
            "与 Agent / WM×VLA/VLN/VLM：异构多智能体规划 Agent，补充 RoCo / SMART-LLM。",
        ],
    },
    "2410.06158": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "GR-2 是带网络规模知识的生成式视频—语言—动作模型，用于机器人操作。相对 GR-1，它扩大视频—语言—动作生成能力，作为闭源 / 实验室通才 VLA 的重要后续。",
        "highlights_zh": [
            "方法：生成式视频—语言—动作模型，融合网络规模视频知识。",
            "贡献：扩展 GR-1 的操作通才与视频预测能力。",
            "与 Agent / WM×VLA/VLN/VLM：生成式 VLA，含视频世界预测色彩。",
        ],
    },
    "2410.07864": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "RDT-1B 是面向双臂操作的十亿级扩散基础模型，用扩散动作头学习双臂协调。它补全 OpenVLA / π₀ 之外的双臂扩散 VLA 一线。",
        "highlights_zh": [
            "方法：十亿参数扩散基础模型生成双臂动作。",
            "贡献：为双臂操作提供开源取向的扩散 VLA。",
            "与 Agent / WM×VLA/VLN/VLM：双臂 VLA 策略，非规划 Agent。",
        ],
    },
    "2410.11758": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "LAPA（Latent Action Pretraining from Videos）从无动作标注视频中预训练潜在动作，再迁到机器人 VLA，降低对大规模动作标注的依赖。",
        "highlights_zh": [
            "方法：从视频学习潜在动作表示，再用于 VLA 预训练。",
            "贡献：减少对动作标注轨迹的依赖。",
            "与 Agent / WM×VLA/VLN/VLM：视频潜在动作 × VLA，接近世界 / 动作表征学习。",
        ],
    },
    "2411.09022": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "DART-LLM 做依赖感知的多机器人任务分解与执行：相对 RoCo 的固定机械臂与 SMART-LLM 的非实时代码输出，它显式建模任务依赖并支持更实时的 LLM 推理执行，面向移动多机器人。",
        "highlights_zh": [
            "方法：LLM 做依赖感知的任务分解，并闭环执行多机器人计划。",
            "贡献：相对 RoCo / SMART-LLM 更强调依赖与实时执行。",
            "与 Agent / WM×VLA/VLN/VLM：多智能体规划 Agent。",
        ],
    },
    "2411.19650": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "CogACT 在 OpenVLA 一类骨干上增加扩散动作模块，以协同认知（VLM）与动作生成。它代表「VLM 骨干 + 专门动作头」的 VLA 设计，常被 SpatialVLA 等后续引用。",
        "highlights_zh": [
            "方法：在 VLM/VLA 骨干上附加扩散动作模块以协同认知与控制。",
            "贡献：提升操作中认知理解与动作生成的配合。",
            "与 Agent / WM×VLA/VLN/VLM：VLA 架构工作，非工具调用 Agent。",
        ],
    },
    "2412.04453": {
        "tags": ["VLA", "VLN"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "NaVILA 是腿式机器人的视觉—语言—动作导航模型：高层产生语言导航命令，低层实时运动策略执行。它把 VLA 接到四足 / 腿式导航，RSS 2025，开源已核验。",
        "highlights_zh": [
            "方法：腿式 VLA 输出语言导航命令，再由实时运动策略执行。",
            "贡献：将 VLA 范式扩展到腿式导航。",
            "与 Agent / WM×VLA/VLN/VLM：VLA × VLN，层次化语言接口类似 Agent 编排。",
        ],
    },
    "2412.10345": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "TraceVLA 用视觉轨迹提示增强通才机器人策略的时空意识：在观测上叠加或提示运动痕迹，帮助 VLA 理解「怎么动」。",
        "highlights_zh": [
            "方法：以视觉轨迹提示增强 VLA 的时空感知。",
            "贡献：提升通才策略对运动过程的意识与操作表现。",
            "与 Agent / WM×VLA/VLN/VLM：VLA 输入设计，非规划 Agent。",
        ],
    },
    "2412.14058": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "如何把动作注入基础 VLM 以构建 VLA，关键因素仍不清。本文回答三问：选何种骨干、如何组织 VLA 架构、何时加入跨本体数据。据此提出少手工设计的 RoboVLMs 家族，在三个仿真任务与真机上达新 SOTA。实验覆盖 8 个以上 VLM 骨干、4 种策略架构与 600 余组设计，并开源灵活框架与配方。",
        "highlights_zh": [
            "方法：系统消融 VLM 骨干、VLA 架构与跨本体数据时机，并给出 RoboVLMs。",
            "贡献：600 余组实验形成设计指南，仿真与真机达新 SOTA，框架开源。",
            "与 Agent / WM×VLA/VLN/VLM：VLA 设计实验，为层次化 Agent 选择低层策略提供依据。",
        ],
    },
    "2412.14803": {
        "tags": ["world_model", "VLA", "intersection"],
        "sources": ["world_model", "vla_vln_vlm"],
        "abstract_zh": "Video Prediction Policy 用预测性视觉表征训练通才机器人策略：先预测未来视频，再据此生成动作，把视频世界预测接到 VLA 式控制。",
        "highlights_zh": [
            "方法：以视频预测表征作为通才操作策略的条件。",
            "贡献：把预测性视觉接到一般操作策略。",
            "与 Agent / WM×VLA/VLN/VLM：World Model 式视频预测 × VLA 策略。",
        ],
    },
    "2501.03575": {
        "tags": ["world_model"],
        "sources": ["world_model"],
        "abstract_zh": "NVIDIA Cosmos 世界基础模型平台面向物理人工智能，提供可微调的视频世界模型、数据与工具。本包 OSS 已收录 cosmos / predict 仓库，此处补平台论文卡片。",
        "highlights_zh": [
            "方法：开放世界基础模型平台，支持视频预测与物理 AI 微调。",
            "贡献：为机器人与驾驶等提供可微调的世界模型基础设施。",
            "与 Agent / WM×VLA/VLN/VLM：World Model 平台；可被策略或 Agent 当想象器调用。",
        ],
    },
    "2501.09747": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "FAST 提出高效的 VLA 动作分词，降低动作序列的 token 数与训练 / 推理成本，成为后续开源 VLA 栈的常见组件。",
        "highlights_zh": [
            "方法：为 VLA 设计更高效的动作分词。",
            "贡献：在保持控制质量下降低 token 与计算开销。",
            "与 Agent / WM×VLA/VLN/VLM：VLA 基础设施，服务策略而非规划 Agent。",
        ],
    },
    "2501.10105": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "Universal Actions 研究跨本体具身基础模型的通用动作表示，使不同机器人共享动作接口，增强通才 VLA 的跨本体迁移。",
        "highlights_zh": [
            "方法：设计跨本体共享的通用动作表示。",
            "贡献：提升具身基础模型的跨机器人迁移。",
            "与 Agent / WM×VLA/VLN/VLM：VLA 动作接口，便于高层 Agent 调用统一技能。",
        ],
    },
    "2501.15830": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "SpatialVLA 在 110 万真实回合上训练空间增强 VLA，用自我中心位置编码与自适应空间网格注入 3D 信息。RSS 2025，开源已核验，零样本与新本体适应表现强，推理 token 更少。",
        "highlights_zh": [
            "方法：自我中心位置编码与自适应空间网格增强 VLA 的 3D 空间理解。",
            "贡献：大规模真实数据上取得强零样本与高效推理。",
            "与 Agent / WM×VLA/VLN/VLM：空间 VLA 策略，可作层次化 Agent 的低层控制器。",
        ],
    },
    "2502.19417": {
        "tags": ["agent-robot", "VLA"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "Hi Robot 用层次化视觉—语言—动作模型做开放指令跟随：高层 VLM 把复杂指令分解为子任务，低层策略执行。它明确把「听懂并更努力思考」接到机器人控制，是层次化 Agent × VLA 的代表。",
        "highlights_zh": [
            "方法：层次化 VLM 规划器 + 低层 VLA/策略执行开放指令。",
            "贡献：提高复杂、开放式指令跟随。",
            "与 Agent / WM×VLA/VLN/VLM：层次化 Agent 编排 VLA，直接交叉两条线。",
        ],
    },
    "2502.19902": {
        "tags": ["agent-robot"],
        "sources": ["agent_robot"],
        "abstract_zh": "Optimus-2 是多模态 Minecraft 智能体：MLLM 做高层规划，Goal-Observation-Action 条件策略（GOAP）做低层控制，并发布约 3000 万对的 MGOA 数据。在原子、长时程与开放指令任务上优于先前 Minecraft Agent。",
        "highlights_zh": [
            "方法：MLLM 规划 + 目标—观察—动作条件低层策略，并构建 MGOA 数据。",
            "贡献：在多样 Minecraft 任务上提升，并开源数据构建方法。",
            "与 Agent / WM×VLA/VLN/VLM：2025 年开放式具身 Agent，层次类似 Hi Robot。",
        ],
    },
    "2503.14734": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "通才机器人需要灵活身体与智能「心智」。GR00T N1 是开放的人形 VLA：系统 2 的视觉—语言模块解释环境与指令，系统 1 的扩散 Transformer 实时生成流畅动作，两端到端联合训练。数据混合真机轨迹、人类视频与合成数据。仿真多本体上优于模仿学习基线，并在 Fourier GR-1 人形上做语言条件双臂操作，数据效率高。",
        "highlights_zh": [
            "方法：双系统 VLA——VLM 解释环境，扩散 Transformer 生成实时动作，端到端共训。",
            "贡献：开放人形基础模型，仿真超模仿基线，并在 Fourier GR-1 上做语言双臂操作。",
            "与 Agent / WM×VLA/VLN/VLM：人形 VLA 底座，高层可被 Agent 编排。",
        ],
    },
    "2503.20020": {
        "tags": ["VLA", "VLM"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "Gemini Robotics 把 Gemini 类多模态模型带入物理世界，训练双系统视觉—语言—动作能力，用于真实机器人操作与推理。作为工业闭源 / API 向地标，它常被层次化 Agent 论文当作低层后端。",
        "highlights_zh": [
            "方法：把大规模多模态模型适配为物理世界中的双系统机器人模型。",
            "贡献：展示工业级 VLM/VLA 进入真机操作。",
            "与 Agent / WM×VLA/VLN/VLM：VLM×VLA 工业地标；Agent 论文常将其当冻结控制器。",
        ],
    },
    "2503.20523": {
        "tags": ["world_model"],
        "sources": ["world_model"],
        "abstract_zh": "GAIA-2 是可控多视角生成式驾驶世界模型，为 GAIA-1 后续。官方权重仍未开放；社区仅有架构级复现。本包补上论文卡片以对照缺口表。",
        "highlights_zh": [
            "方法：可控多视角生成式世界模型预测驾驶未来。",
            "贡献：扩展 GAIA-1 的多视角与可控性。",
            "与 Agent / WM×VLA/VLN/VLM：驾驶 World Model；官方 OSS 仍缺。",
        ],
    },
    "2504.16054": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "π₀.₅ 是 Physical Intelligence 的视觉—语言—动作模型，强调开放世界泛化。作为 π₀ 后续，它被层次化 Agent 与 OpenPI 栈广泛当作低层通才策略。",
        "highlights_zh": [
            "方法：在 π₀ 流匹配 VLA 上提升开放世界泛化。",
            "贡献：成为 2025 年通才机器人策略的常用底座。",
            "与 Agent / WM×VLA/VLN/VLM：VLA 底座，常被 Agent 编排层调用。",
        ],
    },
    "2505.06111": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "UniVLA 学习任务中心的潜在动作，使策略可在不同本体与场景「随处行动」，用潜在动作统一跨环境控制。",
        "highlights_zh": [
            "方法：任务中心潜在动作表示，统一跨场景 VLA。",
            "贡献：提高跨本体 / 跨场景行动能力。",
            "与 Agent / WM×VLA/VLN/VLM：潜在动作 VLA，接近动作条件世界表征。",
        ],
    },
    "2506.13751": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "LeVERB 做人形全身控制的潜在视觉—语言指令：把语言接到全身运动潜空间，而非仅机械臂 VLA。",
        "highlights_zh": [
            "方法：以潜在视觉—语言指令条件化人形全身控制。",
            "贡献：把 VLA 接口扩展到全身运动。",
            "与 Agent / WM×VLA/VLN/VLM：人形 VLA / 语言条件控制。",
        ],
    },
    "2506.17811": {
        "tags": ["agent-robot", "VLA"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "RoboMonkey 扩展 VLA 的测试时采样与验证：对候选动作做缩放采样并由验证器筛选，把 Agent 式 test-time compute 接到策略。层次化编排论文常引用它作为验证模块。",
        "highlights_zh": [
            "方法：测试时对 VLA 动作候选做大规模采样与验证。",
            "贡献：用推理期计算提升 VLA 可靠性。",
            "与 Agent / WM×VLA/VLN/VLM：Agent 式测试时计算 × VLA。",
        ],
    },
    "2506.19850": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "Unified Vision-Language-Action Model 研究统一架构同时做视觉—语言理解与动作生成，减少「理解模型 + 动作头」的割裂。",
        "highlights_zh": [
            "方法：统一模型同时承担视觉语言理解与动作合成。",
            "贡献：探索理解与控制共享骨干的 VLA。",
            "与 Agent / WM×VLA/VLN/VLM：统一 VLA，高层推理可服务 Agent。",
        ],
    },
    "2507.15597": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "Being-H0 从大规模人类视频做视觉—语言—动作预训练，把自我中心人类行为迁到机器人策略，降低对机器人轨迹的依赖。",
        "highlights_zh": [
            "方法：大规模人类视频上的 VLA 预训练。",
            "贡献：用人类视频补充机器人数据以预训练控制。",
            "与 Agent / WM×VLA/VLN/VLM：人类视频 × VLA，含隐式动作 / 世界预测。",
        ],
    },
    "2510.10274": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "X-VLA 用软提示 Transformer 做可扩展跨本体视觉—语言—动作模型，以提示而非重训适应新本体。",
        "highlights_zh": [
            "方法：软提示 Transformer 实现跨本体可扩展 VLA。",
            "贡献：降低新本体适应成本。",
            "与 Agent / WM×VLA/VLN/VLM：跨本体 VLA，便于 Agent 层切换技能后端。",
        ],
    },
    "2512.13030": {
        "tags": ["world_model", "VLA", "intersection"],
        "sources": ["world_model", "vla_vln_vlm"],
        "abstract_zh": "Motus 提出统一的潜在动作世界模型，把动作与未来预测放在同一潜空间，衔接世界建模与策略。",
        "highlights_zh": [
            "方法：统一潜在动作空间中的世界模型。",
            "贡献：把动作表征与动力学预测接到同一模型。",
            "与 Agent / WM×VLA/VLN/VLM：潜在动作 World Model × VLA。",
        ],
    },
    "2512.15692": {
        "tags": ["VLA", "world_model", "intersection"],
        "sources": ["world_model", "vla_vln_vlm"],
        "abstract_zh": "mimic-video 提出视频—动作模型（VAM），主张在 VLA 之外用视频—动作联合建模获得更可泛化的机器人控制。",
        "highlights_zh": [
            "方法：视频—动作模型联合建模未来视频与控制。",
            "贡献：探索超越标准 VLA 的视频动作通才。",
            "与 Agent / WM×VLA/VLN/VLM：视频 World Model 与动作策略统一。",
        ],
    },
    "2601.16163": {
        "tags": ["world_model", "VLA", "intersection"],
        "sources": ["world_model", "vla_vln_vlm"],
        "abstract_zh": "Cosmos Policy 把视频世界模型微调为视觉运动控制与规划策略，展示 Cosmos 预测模型如何变成可部署的控制 / 规划器。",
        "highlights_zh": [
            "方法：微调视频世界模型以同时做控制与规划。",
            "贡献：打通 Cosmos 类 WFM 到策略的路径。",
            "与 Agent / WM×VLA/VLN/VLM：World Model 直接变成策略，可被 Agent 调用。",
        ],
    },
    "2601.21998": {
        "tags": ["world_model"],
        "sources": ["world_model"],
        "abstract_zh": "Causal World Modeling for Robot Control 强调因果世界建模以服务机器人控制，针对相关但不一定可干预的预测问题，把因果结构引入动作条件预测。",
        "highlights_zh": [
            "方法：以因果结构约束机器人控制用的世界模型。",
            "贡献：把因果建模接到动作条件预测与控制。",
            "与 Agent / WM×VLA/VLN/VLM：控制导向 World Model。",
        ],
    },
    "2602.13193": {
        "tags": ["agent-robot", "VLA"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "层次化系统里 VLM 与 VLA 之间若只有自然语言任务指令，高层推理很难转向低层行为。Steerable Policies 在子任务、运动与接地像素坐标等多抽象层级的合成命令上训练 VLA。用学得的高层具身推理器或即插即用 VLM（上下文学习推理命令抽象）来控制该策略时，真机操作在泛化与长时程上优于先前具身推理 VLA 与 VLM 层次基线。",
        "highlights_zh": [
            "方法：在多抽象层级合成命令上训练可转向 VLA，并由 VLM / 具身推理器控制。",
            "贡献：真机泛化与长时程上优于先前层次化 VLM–VLA 基线。",
            "与 Agent / WM×VLA/VLN/VLM：层次化 Agent 的可转向 VLA 接口。",
        ],
    },
    "2602.14979": {
        "tags": ["VLA", "VLM"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "具身社区缺少在真实时空动力学中统一感知、推理与规划的物理接地基础模型。RynnBrain 是开源时空基础模型，强化自我中心理解、时空定位、物理接地推理与物理感知规划；提供 2B / 8B / 30B-A3B MoE 及导航、规划、VLA 与空间推理等后训练变体。在 20 个具身与 8 个通用视觉基准上明显优于既有具身基础模型，并可用作可高效适应的预训练骨干。",
        "highlights_zh": [
            "方法：统一框架强化自我中心理解、时空定位、物理推理与规划，并提供多尺度与后训练变体。",
            "贡献：在 20+8 个基准上优于既有具身基础模型，且可高效适配导航 / 规划 / VLA。",
            "与 Agent / WM×VLA/VLN/VLM：开放具身 VLM 底座，后训练含 VLA，可供 Agent 调用。",
        ],
    },
    "2602.15922": {
        "tags": ["world_model", "VLA", "intersection"],
        "sources": ["world_model", "vla_vln_vlm"],
        "abstract_zh": "World Action Models are Zero-shot Policies 主张世界—动作模型本身即可作为零样本策略：在学得的动作条件动力学上直接解码控制，而无需单独策略头。",
        "highlights_zh": [
            "方法：把世界—动作模型直接当作零样本策略。",
            "贡献：模糊 WM 与策略的界限，强调动作条件预测即可控制。",
            "与 Agent / WM×VLA/VLN/VLM：WM 即策略，高层 Agent 仍可提供目标。",
        ],
    },
    "2603.09971": {
        "tags": ["agent-robot"],
        "sources": ["agent_robot"],
        "abstract_zh": "TiPToP 是模块化开放词汇操作规划系统：把开放词汇接地与经典任务—运动规划组合，并作为可调用后端供更高层物理 Agent 使用。Physical Agency 一文将其当作冻结工具而非整系统。",
        "highlights_zh": [
            "方法：开放词汇感知与经典 TAMP 模块化组合。",
            "贡献：提供可被 Agent 调用的规划后端。",
            "与 Agent / WM×VLA/VLN/VLM：规划工具 Agent 后端，衔接语言与运动规划。",
        ],
    },
    "2603.16666": {
        "tags": ["world_model"],
        "sources": ["world_model"],
        "abstract_zh": "Fast-WAM 追问世界—动作模型是否必须在测试时做未来想象：研究能否在保持性能下跳过昂贵 rollout，以服务实时控制。",
        "highlights_zh": [
            "方法：分析测试时未来想象对世界—动作模型的必要性。",
            "贡献：为实时 WAM 部署提供是否展开想象的实证。",
            "与 Agent / WM×VLA/VLN/VLM：WM 推理成本，影响 Agent 能否在线调用想象。",
        ],
    },
    "2603.22435": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "CaP-X 提供评测与改进机器人操作编码智能体的框架，直接继承 Code as Policies 一线，用基准衡量「写策略代码的 Agent」在操作上的能力与改进空间。",
        "highlights_zh": [
            "方法：为机器人操作编码 Agent 建立评测与改进框架。",
            "贡献：把 Code as Policies 推进到可比较的基准与改进循环。",
            "与 Agent / WM×VLA/VLN/VLM：2026 年代码即策略 Agent 评测，补全 2022 地标之后的缺口。",
        ],
    },
    "2604.15483": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "π₀.₇ 是可转向的通才机器人基础模型，强调涌现能力与更丰富的命令结构，供层次化控制与具身推理使用。",
        "highlights_zh": [
            "方法：可转向通才机器人基础模型，承接层次化命令。",
            "贡献：展示 π 系列在转向与涌现能力上的后续。",
            "与 Agent / WM×VLA/VLN/VLM：VLA 底座，为 Agent 编排提供可转向接口。",
        ],
    },
    "2606.05979": {
        "tags": ["world_model", "VLA", "intersection"],
        "sources": ["world_model", "vla_vln_vlm"],
        "abstract_zh": "World-Language-Action（WLA）用自回归 Transformer 统一世界建模、语言推理与动作合成：高层意图以文本子任务形式引导动力学与动作，相对纯 VLA 更能利用无动作标注的跨本体视频。原型在仿真与真机多任务、长时程上报告强成功。",
        "highlights_zh": [
            "方法：自回归骨干统一下一状态预测、语言子任务与动作合成。",
            "贡献：提出 WLA 家族，连接 WM、语言推理与控制。",
            "与 Agent / WM×VLA/VLN/VLM：显式交叉 World Model、语言 Agent 与 VLA。",
        ],
    },
    "2606.10267": {
        "tags": ["agent-robot", "VLA"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "该文系统研究层次化 VLA Agent：高层 VLM 规划器分解任务，低层 VLA 执行。在统一 options 框架下比较规划器、控制器、切换与记忆设计，并在仿真与真实 ALOHA 上表明原则化层次显著优于平坦 VLA 或朴素层次。",
        "highlights_zh": [
            "方法：在 options 框架下系统消融 Hi-VLA 的规划器、控制器与接口。",
            "贡献：给出可执行的层次化 VLA Agent 设计原则，并在真机验证。",
            "与 Agent / WM×VLA/VLN/VLM：Agent 控制机器人的 2026 年系统研究，直接对照 VLA。",
        ],
    },
    "2606.28182": {
        "tags": ["agent-robot"],
        "sources": ["agent_robot"],
        "abstract_zh": "分散、部分可观测环境中，LLM 智能体常与伙伴或环境状态不对齐。LLawCo 让智能体反思失败、提炼「必要时说话」「等待伙伴」等高层次合作法则，再经监督微调写入思维链。作者构建基于 PARTNR 的大规模对话合作基准 PARTNR-Dialog；相对开源通信智能体，四类 LLM 骨干上 PARTNR-Dialog 平均成功率高 4.5%，TDW-MAT 高 6.8%。",
        "highlights_zh": [
            "方法：从失败中提炼合作法则并监督微调写入思维链，使推理对齐伙伴与任务。",
            "贡献：提出 PARTNR-Dialog，并在该基准与 TDW-MAT 上提高合作效率与成功。",
            "与 Agent / WM×VLA/VLN/VLM：多智能体具身合作 Agent，对齐通信与行为。",
        ],
    },
    "2607.21725": {
        "tags": ["agent-robot"],
        "sources": ["agent_robot"],
        "abstract_zh": "Physical Agency 指出通才机器人的编排缺口：仅有冻结 VLA 不够，需要规划、执行、验证与恢复的闭环物理智能体。系统把 TiPToP 等当作可调用工具，强调 Agent 层与策略层分离。",
        "highlights_zh": [
            "方法：以物理智能体编排规划、执行、验证与恢复，调用冻结技能后端。",
            "贡献：明确「编排缺口」并给出与平坦 VLA 对照的 Agent 架构。",
            "与 Agent / WM×VLA/VLN/VLM：2026 年 Agent 控制机器人的纲领性系统文。",
        ],
    },
    "2609.01281": {
        "tags": ["agent-robot", "VLA"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "EmbodiedSkills 把技能决策当作执行提案：运行时检查前提、执行有界 VLA、事后验证，并用固定可执行技能接口连接规划、执行与恢复。在 RoboTwin 2.0 与 LIBERO 上，任务适应的低层 VLA 平均成功率分别达 86.20% 与 97.40%；记忆依赖的 RMBench 仍仅 12.5%，暴露 Agent 记忆挑战。",
        "highlights_zh": [
            "方法：统一技能接口做提案—前提检查—VLA 执行—结果验证与恢复。",
            "贡献：在 RoboTwin / LIBERO 上给出强执行层，并暴露记忆任务缺口。",
            "与 Agent / WM×VLA/VLN/VLM：可训练 Agent 层把 VLA 变成闭环技能系统。",
        ],
    },
    "2609.04355": {
        "tags": ["VLA"],
        "sources": ["vla_vln_vlm"],
        "abstract_zh": "VLA-Precision 用非对称共引导做高效真机在线强化学习，缓解不可靠价值信号与大 VLA 吞吐瓶颈。在四类九项高精度化学任务、四种本体上，平均成功率 98.3%，并报告显著吞吐提升。",
        "highlights_zh": [
            "方法：非对称共引导在线 RL + 流式闭环架构微调大 VLA。",
            "贡献：高精度真机任务高成功，并大幅提高在线吞吐。",
            "与 Agent / WM×VLA/VLN/VLM：VLA 在线改进；可被精度敏感 Agent 当低层。",
        ],
    },
    "2609.06251": {
        "tags": ["agent-robot", "VLA", "VLN"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "MobileVLA-R1 2.0 用监督思维链与强化学习对齐推理到动作，再经推理条件动作解码器输出移动机器人任务级目标。在 VLN-CE、四足与 Unitree Go2/G1 真机上，相对 MobileVLA-R1 平均成功率提升，并改善长时程指令跟随。",
        "highlights_zh": [
            "方法：思维链对齐 + RL 增强推理，再解码为移动操作 / 导航动作。",
            "贡献：VLN-CE 与 G1 真机移动操作相对前作提升。",
            "与 Agent / WM×VLA/VLN/VLM：推理 Agent × 移动 VLA / VLN。",
        ],
    },
}
