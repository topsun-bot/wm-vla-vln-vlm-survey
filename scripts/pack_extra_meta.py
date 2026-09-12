"""Chinese paraphrases for researcher-pack papers not already in KEEP.

English abstracts from arXiv abs pages only.
"""

PACK_EXTRA = {
    "2209.09874": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "LLM 规划常缺场景接地。NLMap 提供开放词汇、可查询的场景表示，采集并整合环境上下文，使语言规划器能对真实场景提问并生成可执行计划。系统把开放词汇感知接到任务规划，服务真实世界机器人。",
        "highlights_zh": [
            "方法：构建开放词汇可查询场景图 NLMap，供 LLM 规划器检索上下文。",
            "贡献：缓解语言计划与真实场景脱节，支持实机规划。",
            "与 Agent / WM×VLA/VLN/VLM：场景表示服务规划 Agent，补 SayCan 式接地。",
        ],
    },
    "2210.01287": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "经典任务规划假设封闭世界与完备知识，真实开放世界常出现未预见情形。本文提出开放世界任务规划与情境处理，使机器人在知识不全时仍能补全情境并继续执行，而不是让规划器完备性崩溃。",
        "highlights_zh": [
            "方法：为开放世界补充情境处理，使任务规划在未预见情况下可恢复。",
            "贡献：把封闭世界规划器接到真实开放环境。",
            "与 Agent / WM×VLA/VLN/VLM：开放世界规划 Agent，非端到端 VLA。",
        ],
    },
    "2211.09935": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "既有 LLM 规划失败时往往只是重试同一动作。CAPE 针对前提错误提出纠正动作，用语言模型分析失败原因并生成能解除前提的修正，从而在规划执行中恢复，而不是盲目重试。",
        "highlights_zh": [
            "方法：由前提错误触发 LLM 生成纠正动作，而非简单重试。",
            "贡献：提高执行失败后的可恢复性。",
            "与 Agent / WM×VLA/VLN/VLM：ReAct 式失败恢复的规划 Agent。",
        ],
    },
    "2302.00763": {
        "tags": ["llm-agent", "agent-robot"],
        "sources": ["agent_robot"],
        "abstract_zh": "复杂模糊环境中的推理是强化学习难点：强 RL 智能体数据饥渴且难泛化，而大规模语言模型推理与适应强。本文研究与语言模型协作做具身推理，把 LLM 常识接到交互环境中的决策。",
        "highlights_zh": [
            "方法：让语言模型与具身智能体协作完成环境中的推理。",
            "贡献：探索用 LLM 补 RL 在新环境、新任务上的泛化。",
            "与 Agent / WM×VLA/VLN/VLM：具身推理 Agent，非 VLA 策略。",
        ],
    },
    "2302.02662": {
        "tags": ["llm-agent", "agent-robot"],
        "sources": ["agent_robot"],
        "abstract_zh": "LLM 对世界物理的抽象知识可用于决策，但与环境对齐不足会限制功能能力。GLAM 通过在线强化学习做功能接地，使智能体在交互中对齐语言模型知识与环境，提升可执行能力。",
        "highlights_zh": [
            "方法：用在线强化学习对 LLM 做功能接地（GLAM）。",
            "贡献：缩小语言模型知识与交互环境之间的错位。",
            "与 Agent / WM×VLA/VLN/VLM：接地规划 Agent，非学得 World Model。",
        ],
    },
    "2302.05128": {
        "tags": ["llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "LLM 在 NLP 上强，但准确推理与求解规划问题仍弱。本文研究如何把自然语言译为规划目标，使经典规划器可用，从而服务机器人任务。结论强调翻译目标比让 LLM 直接当规划器更可靠。",
        "highlights_zh": [
            "方法：把自然语言翻译为规划目标，再交给规划器。",
            "贡献：指出 LLM 直接规划的不可靠，并给出目标翻译路径。",
            "与 Agent / WM×VLA/VLN/VLM：与 LLM+P 同类的符号规划接口。",
        ],
    },
    "2303.00855": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "LLM 缺物理经验、难解析非语言观测、也不知奖励与安全约束。Grounded Decoding 在解码时用接地模型引导文本生成，使具身智能体的语言计划遵守感知、奖励与安全，而不是纯自由生成。",
        "highlights_zh": [
            "方法：解码阶段用接地模型约束 LLM 文本生成。",
            "贡献：把互联网知识接到具身约束下的可执行语言。",
            "与 Agent / WM×VLA/VLN/VLM：SayCan 一线的接地生成 Agent。",
        ],
    },
    "2303.06247": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "服务机器人多物体重排需要常识，但 LLM 并不天然编码合理物理布局。本文把 LLM 接到任务与运动规划，使物体重排既符合常识又满足几何可行，用于桌面 / 服务操作。",
        "highlights_zh": [
            "方法：LLM 常识与任务—运动规划结合做物体重排。",
            "贡献：在常识布局与几何可行之间搭桥。",
            "与 Agent / WM×VLA/VLN/VLM：TAMP + 语言 Agent。",
        ],
    },
    "2303.08268": {
        "tags": ["agent-robot", "llm-agent", "VLM"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "少样本 LLM 规划强，但把多模态感知与连续动作接地仍难。本文让机器人与环境「对话」：用交互式多模态感知把传感结果写成语言，再交给 LLM 推理，从而在复杂世界中闭环交互。",
        "highlights_zh": [
            "方法：交互式多模态感知把观测转为语言，与 LLM 对话式规划。",
            "贡献：缓解 LLM 在连续感知—动作上的接地困难。",
            "与 Agent / WM×VLA/VLN/VLM：VLM 感知 + 语言 Agent 控制。",
        ],
    },
    "2303.16563": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "开放世界无演示的长时程强化学习极低效。本文在 Minecraft 上把多任务学习拆成技能强化学习与技能上的规划，先学基本技能再规划组合，以完成开放世界长时程任务。",
        "highlights_zh": [
            "方法：先 RL 学基本技能，再在技能上规划开放世界长任务。",
            "贡献：无人类演示下提高 Minecraft 多任务效率。",
            "与 Agent / WM×VLA/VLN/VLM：技能库 Agent，与 Voyager / DEPS 同属开放世界线。",
        ],
    },
    "2304.03893": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "案例研究展示少样本 ChatGPT 把自然语言转为可执行机器人动作序列，并给出易定制、易接入执行系统、可迁移多环境的提示设计，同时尽量降低 ChatGPT 幻觉对控制的影响。",
        "highlights_zh": [
            "方法：定制少样本提示，将指令译为可接入执行系统的动作序列。",
            "贡献：给出跨环境长步骤机器人控制的工程案例。",
            "与 Agent / WM×VLA/VLN/VLM：代码 / 动作序列 Agent，近 ChatGPT for Robotics。",
        ],
    },
    "2304.09349": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "具身系统的记忆与控制通常分框架建模。LLM-Brain 用大语言模型统一自我中心记忆与控制，作为可泛化的机器人「大脑」，在交互中同时保持情景记忆并输出控制决策。",
        "highlights_zh": [
            "方法：单一 LLM 框架统一自我中心记忆与控制。",
            "贡献：提出可泛化的机器人大脑式记忆—控制接口。",
            "与 Agent / WM×VLA/VLN/VLM：记忆型规划 Agent，符号记忆而非 Dreamer 式 WM。",
        ],
    },
    "2305.14078": {
        "tags": ["llm-agent", "agent-robot"],
        "sources": ["agent_robot"],
        "abstract_zh": "大规模任务规划极难。本文表明 LLM 既可当策略，也可提供常识世界模型，二者可在蒙特卡洛树搜索中结合以扩展规划规模。相对直接把 LLM 当策略，搜索式组合更能放大常识。",
        "highlights_zh": [
            "方法：把 LLM 常识世界模型与策略嵌入 MCTS 做大规模任务规划。",
            "贡献：展示 LLM 可作为可搜索的常识模型而不只是贪心策略。",
            "与 Agent / WM×VLA/VLN/VLM：LLM 当符号世界模型 + 规划 Agent。",
        ],
    },
    "2305.16653": {
        "tags": ["llm-agent", "agent-robot"],
        "sources": ["agent_robot"],
        "abstract_zh": "多数 LLM 智能体要么贪心无规划，要么静态计划不适应反馈，随问题变复杂而退化。AdaPlanner 根据环境反馈自适应改写计划，使顺序决策在更长时程上保持可修正。",
        "highlights_zh": [
            "方法：由环境反馈自适应改写语言模型计划。",
            "贡献：缓解静态计划在长时程上的退化。",
            "与 Agent / WM×VLA/VLN/VLM：ReAct 式自适应规划 Agent。",
        ],
    },
    "2305.19352": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "LLM-BRAIn 从 Alpaca 7B 微调，把操作员文本命令转为机器人行为树。训练使用约 8500 条指令跟随示范，实现由语言快速生成可执行 BT，便于接入传统机器人执行栈。",
        "highlights_zh": [
            "方法：微调 LLM 由文本生成机器人行为树。",
            "贡献：把自然语言命令接到工业常用的 BT 执行表示。",
            "与 Agent / WM×VLA/VLN/VLM：语言→行为树 Agent，非 VLA。",
        ],
    },
    "2306.15724": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "自动检测并分析失败对可解释稳健机器人至关重要。REFLECT 查询 LLM，把机器人经验总结为失败解释并生成纠正，从而用语言反思闭环改进后续执行。",
        "highlights_zh": [
            "方法：用 LLM 总结机器人经验以解释失败并生成纠正。",
            "贡献：把失败解释变成可执行的纠正回路。",
            "与 Agent / WM×VLA/VLN/VLM：反思 / 恢复 Agent，近 Reflexion 的真机版。",
        ],
    },
    "2307.00329": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "DoReMi 通过检测并恢复计划—执行错位来接地语言模型：当执行偏离计划时触发恢复，而不是继续开环执行错误计划，从而提高语言计划在机器人上的可靠性。",
        "highlights_zh": [
            "方法：检测计划与执行的错位并触发恢复以接地 LLM。",
            "贡献：降低开环语言计划在真机上的漂移。",
            "与 Agent / WM×VLA/VLN/VLM：闭环接地 Agent。",
        ],
    },
    "2308.12682": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "SayCanPay 在 SayCan 上加入可学习领域知识的启发式支付 / 评分，用 LLM 提议技能，用可学习启发式评估长期代价或价值，从而改进启发式规划。",
        "highlights_zh": [
            "方法：LLM 提议技能，可学习启发式（Pay）评估并选择。",
            "贡献：在 SayCan 式规划中引入可学习领域评分。",
            "与 Agent / WM×VLA/VLN/VLM：SayCan 家族规划 Agent。",
        ],
    },
    "2309.09969": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "本文研究用大语言模型提示机器人行走：把语言接到步态 / 运动控制接口，展示 LLM 不仅能做操作规划，也能参与运动控制层面的指令跟随。",
        "highlights_zh": [
            "方法：用 LLM 提示生成或选择行走相关控制。",
            "贡献：把语言 Agent 从操作规划扩展到行走。",
            "与 Agent / WM×VLA/VLN/VLM：语言条件运动 Agent，非腿式 VLA 权重模型。",
        ],
    },
    "2309.15821": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "LGMCTS 用语言引导蒙特卡洛树搜索，做可执行的语义物体重排：在搜索中纳入语言语义，使重排计划既可执行又符合指令语义。",
        "highlights_zh": [
            "方法：语言引导的 MCTS 搜索可执行语义重排。",
            "贡献：把指令语义写入搜索而非只做一次 LLM 展开。",
            "与 Agent / WM×VLA/VLN/VLM：搜索式规划 Agent。",
        ],
    },
    "2310.07263": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "CoPAL 用大语言模型做机器人动作的纠正规划：在执行偏差或失败后重新生成修正计划，强调纠正而非一次性开环计划。",
        "highlights_zh": [
            "方法：LLM 对机器人动作做纠正式再规划。",
            "贡献：把失败后的纠正规划显式化。",
            "与 Agent / WM×VLA/VLN/VLM：纠正规划 Agent。",
        ],
    },
    "2310.08588": {
        "tags": ["agent-robot", "llm-agent", "VLM"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "Octopus 是具身视觉—语言程序员：根据环境反馈生成程序，把视觉观察与语言指令编译为可执行代码，并在反馈下改写，属于代码即策略的视觉闭环版本。",
        "highlights_zh": [
            "方法：视觉—语言程序员根据环境反馈生成并改写控制程序。",
            "贡献：把 Code as Policies 接到视觉反馈闭环。",
            "与 Agent / WM×VLA/VLN/VLM：代码即策略 Agent + VLM。",
        ],
    },
    "2310.10134": {
        "tags": ["llm-agent", "agent-robot"],
        "sources": ["agent_robot"],
        "abstract_zh": "CLIN 是持续学习的语言智能体，强调快速任务适应与泛化：在新任务上用语言记忆积累经验，而不必每次从零提示，从而加速适应。",
        "highlights_zh": [
            "方法：持续学习语言智能体积累任务经验以快速适应。",
            "贡献：提高语言 Agent 在新任务上的适应与泛化。",
            "与 Agent / WM×VLA/VLN/VLM：持续学习规划 Agent。",
        ],
    },
    "2310.17722": {
        "tags": ["llm-agent", "agent-robot"],
        "sources": ["agent_robot"],
        "abstract_zh": "本文将大语言模型作为具身任务的可泛化策略：不只生成文本计划，而把 LLM 直接或经适配当作跨任务的决策策略，探索语言先验在具身策略中的迁移。",
        "highlights_zh": [
            "方法：把 LLM 当作可泛化的具身任务策略。",
            "贡献：检验语言先验作为跨任务策略的能力。",
            "与 Agent / WM×VLA/VLN/VLM：LLM 策略 / Agent，介于规划与策略之间。",
        ],
    },
    "2311.15649": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "RoboGPT 做日常指令的具身长期决策智能体：把家居式长时程指令分解为可执行决策序列，强调日常任务上的长期决策而非单步技能。",
        "highlights_zh": [
            "方法：以 LLM 智能体做日常指令的长期具身决策。",
            "贡献：面向家居长时程指令跟随。",
            "与 Agent / WM×VLA/VLN/VLM：家用长期决策 Agent。",
        ],
    },
    "2311.17406": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "LLM-State 为开放世界长时程规划维护语言模型可读的状态表示，使规划器在开放世界中跟踪物体与关系，而不是只依赖对话历史。",
        "highlights_zh": [
            "方法：用 LLM 维护开放世界状态表示以支持长时程规划。",
            "贡献：显式状态减轻开放世界规划的遗忘与不一致。",
            "与 Agent / WM×VLA/VLN/VLM：近 Statler 的符号状态 Agent。",
        ],
    },
    "2311.17842": {
        "tags": ["agent-robot", "llm-agent", "VLM"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "Look Before You Leap 展示 GPT-4V 在机器人视觉—语言规划中的能力：先看再跳，用多模态模型在行动前做视觉推理与计划，减少盲目执行。",
        "highlights_zh": [
            "方法：用 GPT-4V 在行动前做视觉—语言规划。",
            "贡献：验证多模态 LLM 作为机器人视觉规划器。",
            "与 Agent / WM×VLA/VLN/VLM：VLM 规划 Agent。",
        ],
    },
    "2312.07843": {
        "tags": ["llm-agent", "VLM"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "综述机器人中的基础模型：应用、挑战与未来，覆盖语言、视觉与控制接口，为 Agent / VLA / VLM 交叉提供早期全景。",
        "highlights_zh": [
            "方法：综述基础模型在机器人中的应用与挑战。",
            "贡献：梳理早期基础模型机器人路线与开放问题。",
            "与 Agent / WM×VLA/VLN/VLM：交叉综述，本身无新控制实验。",
        ],
    },
    "2312.08782": {
        "tags": ["llm-agent", "VLA"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "面向通用机器人的基础模型综述与元分析，比较不同基础模型路线通向通才机器人的证据与缺口，补充 VLA / Agent 设计选择。",
        "highlights_zh": [
            "方法：对通才机器人基础模型文献做综述与元分析。",
            "贡献：归纳通向通用机器人的证据强度与缺口。",
            "与 Agent / WM×VLA/VLN/VLM：通才机器人综述，覆盖 Agent 与 VLA。",
        ],
    },
    "2402.02385": {
        "tags": ["llm-agent", "VLA"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "机器人与基础模型综述，面向具身人工智能，梳理语言、视觉与动作基础模型如何进入机器人栈，并讨论评测与安全。",
        "highlights_zh": [
            "方法：综述基础模型驱动的机器人 / 具身 AI。",
            "贡献：提供 2024 年前后的具身基础模型地图。",
            "与 Agent / WM×VLA/VLN/VLM：交叉综述。",
        ],
    },
    "2402.10340": {
        "tags": ["agent-robot", "llm-agent", "VLM"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "分析 LLM / VLM 控制机器人的脆弱性：提示攻击、错误接地与不安全输出如何变成危险身体动作，指出语言控制栈与纯策略 VLA 不同的攻击面。",
        "highlights_zh": [
            "方法：分析 LLM/VLM 控机器人的安全脆弱性。",
            "贡献：把模型安全问题连接到身体执行风险。",
            "与 Agent / WM×VLA/VLN/VLM：Agent 安全，区别于纯 VLA 策略风险。",
        ],
    },
    "2402.16117": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "RoboCodeX 做机器人行为合成的多模态代码生成：从视觉与语言生成可执行行为代码，扩展 Code as Policies 到更强的多模态程序合成。",
        "highlights_zh": [
            "方法：多模态代码生成以合成机器人行为程序。",
            "贡献：把代码即策略扩展到更强的视—语言程序合成。",
            "与 Agent / WM×VLA/VLN/VLM：代码即策略 Agent。",
        ],
    },
    "2403.11552": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "LLM3 把大语言模型用于任务与运动规划，并纳入运动失败推理：当运动规划失败时用语言推理调整任务计划，形成 TAMP 闭环。",
        "highlights_zh": [
            "方法：LLM-TAMP 并在运动失败时做语言推理再规划。",
            "贡献：把运动失败反馈写回任务层。",
            "与 Agent / WM×VLA/VLN/VLM：TAMP Agent。",
        ],
    },
    "2404.02018": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "研究用大语言模型编排双臂机器人：在空间与时间上协调双手动作，用语言规划器分配双臂角色与顺序，而不是只学单臂技能。",
        "highlights_zh": [
            "方法：LLM 编排双臂的时空协调与角色分配。",
            "贡献：把语言规划从单臂扩展到双臂协调。",
            "与 Agent / WM×VLA/VLN/VLM：双臂编排 Agent。",
        ],
    },
    "2404.14285": {
        "tags": ["llm-agent", "agent-robot"],
        "sources": ["agent_robot"],
        "abstract_zh": "LLM-Personalize 用强化自我训练把 LLM 规划器对齐到人的偏好，使家用或个性化任务计划更符合特定用户，而不是通用常识计划。",
        "highlights_zh": [
            "方法：强化自我训练对齐 LLM 规划器与用户偏好。",
            "贡献：个性化语言规划，而非单一通用计划。",
            "与 Agent / WM×VLA/VLN/VLM：个性化规划 Agent，近 TidyBot。",
        ],
    },
    "2405.01534": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "Plan-Seq-Learn 用语言模型引导强化学习求解长时程机器人任务：LLM 提供计划或子目标序列，RL 在子目标上学习，从而结合语言分解与技能学习。",
        "highlights_zh": [
            "方法：语言计划分解 + 序列上的强化学习。",
            "贡献：提高长时程机器人任务上的 RL 样本效率。",
            "与 Agent / WM×VLA/VLN/VLM：规划 Agent 指导 RL，非纯 VLA。",
        ],
    },
    "2406.08824": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "指出 LLM 驱动的机器人可能执行歧视、暴力与违法动作：即便有常识能力，未加约束的语言控制也会把有害文本变成身体伤害。工作强调部署前的规范与过滤。",
        "highlights_zh": [
            "方法：分析 LLM 控机器人在歧视、暴力与违法指令上的风险。",
            "贡献：把社会与法律风险连接到身体执行。",
            "与 Agent / WM×VLA/VLN/VLM：Agent 安全与规范，AutoRT「宪法」的对照文献。",
        ],
    },
    "2407.02220": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "提出面向移动智能体的 LLM 具身路径规划框架，分层解决高层覆盖路径规划与低层控制：提示 LLM 做覆盖规划，再交给低层执行，用于移动机器人巡检 / 覆盖。",
        "highlights_zh": [
            "方法：多层架构用提示 LLM 做覆盖路径规划并接下层控制。",
            "贡献：把语言规划接到移动覆盖任务。",
            "与 Agent / WM×VLA/VLN/VLM：移动规划 Agent，近 VLN 但强调覆盖。",
        ],
    },
    "2407.19094": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "Wonderful Team 是多智能体视觉大模型框架，做零样本高层物理任务规划：给定新环境图像与任务描述，输出完成任务所需动作序列，而无需该环境的先验训练。",
        "highlights_zh": [
            "方法：多 VLLM 智能体零样本由场景图像生成高层动作序列。",
            "贡献：新环境无需训练即可做物理任务规划。",
            "与 Agent / WM×VLA/VLN/VLM：多智能体视觉规划 Agent。",
        ],
    },
    "2409.19471": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "SELP 为机器人智能体生成安全且高效的任务计划。关键是等价投票、约束解码与领域微调，使复杂命令与长时程任务仍遵守用户约束，而不是只追求表面可执行。",
        "highlights_zh": [
            "方法：等价投票、约束解码与领域微调以生成安全高效计划。",
            "贡献：提高长时程语言计划对用户约束的遵守。",
            "与 Agent / WM×VLA/VLN/VLM：安全规划 Agent。",
        ],
    },
    "2410.03035": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "SPINE 做在线语义规划，处理非结构化环境中不完整的自然语言任务：无法预建地图时，机器人边建图边推断任务细节，而不是要求任务被完全指定。",
        "highlights_zh": [
            "方法：在线建图 + 语义规划以补全不完整自然语言任务。",
            "贡献：把任务规划从「任务已完全指定」推广到野外不完整指令。",
            "与 Agent / WM×VLA/VLN/VLM：在线语义规划 Agent，接导航。",
        ],
    },
    "2410.13691": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "研究越狱攻击 LLM 控制的机器人：把对独立 LLM 的越狱扩展到操作、行走与自动驾驶等身体系统，展示恶意提示如何绕过护栏并诱发有害机器人行为。",
        "highlights_zh": [
            "方法：把 LLM 越狱攻击迁移到受 LLM 控制的机器人。",
            "贡献：实证语言护栏在身体执行上可被绕过。",
            "与 Agent / WM×VLA/VLN/VLM：Agent 安全地标，VLA 纯策略不覆盖此类提示攻击。",
        ],
    },
    "2411.17636": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "MALMM 用多智能体大语言模型做零样本机器人操作：针对单次生成长时程计划的幻觉与不适应，用多角色 Agent 分工规划与修正，提高零样本操作规划。",
        "highlights_zh": [
            "方法：多智能体 LLM 分工以降低长时程单次计划幻觉。",
            "贡献：提高零样本操作规划的适应性。",
            "与 Agent / WM×VLA/VLN/VLM：多智能体操作 Agent。",
        ],
    },
    "2412.04455": {
        "tags": ["agent-robot", "llm-agent", "VLM"],
        "sources": ["agent_robot", "vla_vln_vlm"],
        "abstract_zh": "Code-as-Monitor（CaM）用 VLM 做开集失败的反应式与预防式检测：以约束感知的视觉编程同时在失败后识别，并在可预见失败前预防，服务闭环机器人。",
        "highlights_zh": [
            "方法：VLM 视觉编程生成约束监视器，兼顾反应与预防。",
            "贡献：开集失败检测同时覆盖已发生与可预见失败。",
            "与 Agent / WM×VLA/VLN/VLM：代码监视 Agent + VLM。",
        ],
    },
    "2412.17288": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "用少量例子学习具身智能体的多模态接地规划与高效重规划：减少对大量自由语言标注的依赖，在步骤细化时结合多模态接地并在失败后高效重规划。",
        "highlights_zh": [
            "方法：少样本多模态接地规划，并做高效重规划。",
            "贡献：降低复杂任务规划对大规模语言标注的需求。",
            "与 Agent / WM×VLA/VLN/VLM：少样本接地规划 Agent。",
        ],
    },
    "2503.03911": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "LLM 零样本增强人机交互，但其概率性缺形式保证。本文用可达性分析为 LLM 控制的机器人提供形式化安全保证，针对不可预测环境中的安全关键部署。",
        "highlights_zh": [
            "方法：以可达性分析为 LLM 控机器人提供形式保证。",
            "贡献：把传统模型验证接到概率性语言控制器。",
            "与 Agent / WM×VLA/VLN/VLM：安全形式化 × 语言 Agent。",
        ],
    },
    "2503.07885": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "讨论 LLM 机器人的安全护栏：覆盖幻觉等平均错误与对抗越狱，指出传统机器人安全不管 LLM 的上下文脆弱性，需要针对语言控制栈的护栏。",
        "highlights_zh": [
            "方法：为 LLM 使能的机器人设计针对幻觉与越狱的安全护栏。",
            "贡献：区分传统机器人安全与语言上下文脆弱性。",
            "与 Agent / WM×VLA/VLN/VLM：Agent 安全护栏。",
        ],
    },
    "2503.17309": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "LLM+MAP 用大语言模型与 PDDL 做双臂长时程任务规划：既有工作多重双手技能，本文补上长时程任务层，用上下文学习与规划域定义协调双手时空。",
        "highlights_zh": [
            "方法：LLM + PDDL（MAP）做双臂长时程任务规划。",
            "贡献：把双臂研究从技能层提升到任务规划层。",
            "与 Agent / WM×VLA/VLN/VLM：双臂符号规划 Agent。",
        ],
    },
    "2504.14588": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "Phoenix 用基于运动的自我反思，把多模态模型的语义反思翻译成细粒度动作纠正。针对「知道失败了但不知如何改动作」的鸿沟，用运动指令连接语义反思与控制修正。",
        "highlights_zh": [
            "方法：运动自我反思框架把语义失败分析落到细粒度动作纠正。",
            "贡献：弥合 MLLM 反思与可执行动作修正之间的缺口。",
            "与 Agent / WM×VLA/VLN/VLM：细粒度纠正 Agent，可配合 VLA。",
        ],
    },
    "2505.03238": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "RobotxR1 把 R1-zero 思路扩到机器人：用闭环强化学习让小参数量 LLM 在机载、非持续云连接条件下具备具身智能，平衡能力与算力 / 内存约束。",
        "highlights_zh": [
            "方法：闭环 RL 将低参数 LLM 适配为机载具身智能。",
            "贡献：面向无持续云连接的机载语言控制。",
            "与 Agent / WM×VLA/VLN/VLM：机载语言 Agent，补云端 GPT 编排的缺口。",
        ],
    },
    "2505.14899": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "REFLEX 赋予 LLM 元认知推理，做反思式零样本机器人规划：不停留在静态提示行为，而用类似人类的元认知与创造性解题提升复杂任务上的零 / 少样本规划。",
        "highlights_zh": [
            "方法：元认知推理支持反思式零样本机器人规划。",
            "贡献：把 LLM 从静态提示行为推进到可反思规划。",
            "与 Agent / WM×VLA/VLN/VLM：元认知规划 Agent。",
        ],
    },
    "2507.14975": {
        "tags": ["agent-robot", "llm-agent"],
        "sources": ["agent_robot"],
        "abstract_zh": "FCRF 提出灵活建构主义反思，用于 LLM 长时程家用任务规划的自主纠错。针对既有自我反思机制僵硬，借鉴人类认知适应，使长时程家务执行更可靠。",
        "highlights_zh": [
            "方法：灵活建构主义反思以自主纠正长时程任务规划错误。",
            "贡献：针对家用机器人提高长时程执行可靠性。",
            "与 Agent / WM×VLA/VLN/VLM：家用长时程反思 Agent。",
        ],
    },
}
