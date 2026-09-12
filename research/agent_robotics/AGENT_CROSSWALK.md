# Agent Control vs VLA vs World Model — Crosswalk / 对照说明

Scope: conceptual differences and how they compose. No fabricated citations.

## English
- **Agent control (LLM agent)**: LLM as planner/reasoner/tool-caller; outputs plans, code, API calls, or dialog; often closed-loop with language feedback (success detectors, scene text, replanning).
- **VLA (Vision-Language-Action)**: end-to-end (or near end-to-end) policy mapping images(+language) → low-level actions/tokens; learned from robot demos; usually not an explicit multi-step tool agent.
- **World model**: learned dynamics/predictor of future observations or latents; used for imagination, planning, or data generation; may not include an LLM controller.
- **Composition A — LLM agent + skills/VLA**: SayCan-style / AutoRT-style: LLM selects or sequences skills; each skill may be a VLA/policy primitive.
- **Composition B — Code-as-policy**: LLM writes executable programs that call perception/control APIs (CaP, ProgPrompt, Instruct2Act, Octopus).
- **Composition C — Agent + world model**: agent proposes actions; world model simulates outcomes for scoring/replanning (optional; not required for LLM agents).
- **Composition D — Multi-agent LLM robots**: multiple LLM roles (planner/coder/supervisor) or multiple robot agents dialog (RoCo, SMART-LLM, MALMM).
- **ReAct-style loop**: Thought → Act(tool/API) → Observe → replan; central to many embodied LLM agents (Voyager, AdaPlanner, DoReMi, REFLECT).
- **Grounding difference**: agents ground via affordance value functions, scene graphs, code interpreters, or VLM captions; VLAs ground via imitation in action space.
- **Failure handling**: agent papers emphasize language reflection/replanning; VLAs emphasize more data / better policy; world models emphasize better imagined rollouts.
- **Data needs**: LLM agents often zero/few-shot with frozen LLMs; VLAs need large robot trajectory sets; world models need video/interaction data.
- **Latency/control**: agents usually low-frequency high-level; VLAs can be high-frequency control; world models sit in planning/imagination loop.
- **Embodied sandbox agents** (MineDojo/Voyager/GITM/JARVIS): same agent pattern in simulated open worlds; transfer ideas (skill libraries, curricula) to real robots carefully.
- **Safety angle**: LLM-controlled robots add prompt/jailbreak and unlawful-instruction risks distinct from pure policy VLAs.

## 中文
- **Agent 控制**：LLM 做规划/推理/工具调用，输出计划、代码或 API；常配合语言反馈闭环重规划。
- **VLA**：视觉(+语言)→动作的端到端策略，多依赖机器人示范数据，通常没有显式多步工具智能体。
- **World Model**：学习动态/未来预测，用于想象、规划或造数据；本身不必含 LLM 控制器。
- **组合方式**：Agent 编排技能/VLA；Code-as-policy 写可执行程序；Agent+世界模型做推演评估；多 Agent/多机器人分工对话。
- **频率分层**：Agent 偏低频高层决策；VLA 可高频控制；世界模型服务规划/想象环。
- **失败处理**：Agent 侧重语言反思与重规划；VLA 侧重数据与策略；世界模型侧重更准的想象 rollout。
- **安全**：LLM 控机器人额外面临提示注入/越狱与违规指令风险，与纯策略 VLA 不完全相同。
