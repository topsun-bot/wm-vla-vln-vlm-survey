// Crosswalk copy condensed from CROSSWALK.md / CROSSWALK.zh.md.
// Do not add papers, links, or claims that are not already in those files.

export const guide = {
  definitions: [
    {
      term: "World Model (WM)",
      termZh: "World Model（WM，世界模型）",
      body: "Learned (often latent) dynamics that predict future states / observations / rewards conditioned on actions — used for imagination, planning, or policy training without always rolling the real environment.",
      bodyZh: "学习到的（常为潜空间）动力学，在动作条件下预测未来状态 / 观测 / 奖励。用于想象、规划或策略训练，而不必每一步都滚真实环境。",
    },
    {
      term: "VLM",
      termZh: "VLM（Vision-Language Model）",
      body: "Multimodal foundation model mapping images/video ↔ language (caption, VQA, grounding). Perception + semantic interface; typically not an action policy by itself.",
      bodyZh: "把图像 / 视频与语言互映射的多模态基础模型（描述、VQA、接地）。提供感知与语义接口；本身通常不是动作策略。",
    },
    {
      term: "VLA",
      termZh: "VLA（Vision-Language-Action）",
      body: "Policy / foundation model that maps vision + language instructions → robot actions (often continuous control or action tokens). OSS examples in this pack: OpenVLA, Octo.",
      bodyZh: "把视觉 + 语言指令映射到机器人动作（连续控制或动作 token）的策略 / 基础模型。本包开源例子：OpenVLA、Octo。",
    },
    {
      term: "VLN",
      termZh: "VLN（Vision-and-Language Navigation）",
      body: "Agents that follow natural-language route instructions in visual environments (discrete graph or continuous Habitat-style). Examples: VLN-CE, NavGPT, MapGPT.",
      bodyZh: "在视觉环境中跟随自然语言路线指令的智能体（离散拓扑图或连续 Habitat 风格）。例子：VLN-CE、NavGPT、MapGPT。",
    },
    {
      term: "Intersection",
      termZh: "交叉（intersection）",
      body: "Works that explicitly couple WM imagination with VLA/VLN, or use WM-style prediction inside language-conditioned control / navigation.",
      bodyZh: "显式把 WM 想象接到 VLA / VLN，或在语言条件控制 / 导航里使用世界模型式预测。",
    },
    {
      term: "Agent-controlling-robots",
      termZh: "Agent 控制机器人",
      body: "LLM/VLM runtime that orchestrates perception, planning, tools, code, or skills to drive a robot. Outputs are often subgoals, Python policies, tool calls, or dispatch to a frozen VLA — not a single action-token forward pass.",
      bodyZh: "用 LLM / VLM 编排感知、规划、工具、代码或技能，再驱动机器人。输出常常是子目标、Python 策略、API 调用或对冻结 VLA 的调度，而不是单一前向的动作 token。",
    },
  ],
  compose: [
    {
      title: "Perception → latent",
      titleZh: "感知 → 潜空间",
      body: "VLM / vision encoder compresses RGB(D) into tokens or latents that a WM or policy consumes.",
      bodyZh: "VLM / 视觉编码器把 RGB(D) 压成 token 或 latent，再交给 WM 或策略。",
    },
    {
      title: "Latent dynamics",
      titleZh: "潜空间动力学",
      body: "WM predicts next latents (or pixels / occupancy / 3D) given actions — Dreamer-style RSSM, transformer WMs, diffusion/video WMs, JEPA predictors, occupancy WMs.",
      bodyZh: "WM 在动作条件下预测下一 latent（或像素 / 占据 / 3D）——Dreamer 式 RSSM、Transformer WM、扩散 / 视频 WM、JEPA 预测器、占据 WM。",
    },
    {
      title: "Language grounding",
      titleZh: "语言接地",
      body: "Instructions enter via VLM embeddings, LLM planners, or language-conditioned WM actions.",
      bodyZh: "指令或目标经 VLM 嵌入、LLM 规划器，或语言条件的 WM 动作进入。",
    },
    {
      title: "Action / navigation head",
      titleZh: "动作 / 导航头",
      body: "Manipulation → VLA policy or WM imagination + planner. Navigation → VLN policy / LLM tool-calling over maps or WM-based predictive nav.",
      bodyZh: "操作 → VLA 策略，或 WM 想象 + 规划器。导航 → VLN 策略 / 在地图上的 LLM tool-calling，或基于 WM 的预测导航。",
    },
    {
      title: "Typical stack",
      titleZh: "典型栈",
      body: "Sensors → VLM/encoder → (optional WM rollouts) → VLA/VLN or MPC → low-level controller. For long-horizon verify/recover, insert an agent loop at mid-rate.",
      bodyZh: "传感器 → VLM / 编码器 →（可选 WM 做 what-if）→ VLA / VLN 或 MPC → 底层控制器。需要长时程验证与恢复时，在中频插入 Agent 环。",
    },
  ],
  contrast: {
    headers: ["Contrast", "Agent-robot", "VLA", "World Model", "VLN", "VLM"],
    headersZh: ["对照", "Agent 控制机器人", "VLA", "World Model", "VLN", "VLM"],
    rows: [
      ["Main output", "Subgoals, programs, tool calls, verify / recover", "Action tokens or continuous chunks", "Future state / observation / reward", "Nav actions or waypoints", "Caption, grounding, VQA"],
      ["Loop", "Explicit plan → act → feedback → replan", "Implicit inside the policy", "Roll out in imagination, then actor / MPC", "Stepwise edges or continuous control", "Usually does not control"],
    ],
    rowsZh: [
      ["主输出", "子目标、程序、工具调用、验证 / 恢复", "动作 token 或连续动作块", "未来状态 / 观测 / 奖励", "导航动作或航点", "描述、接地、VQA"],
      ["闭环", "显式：计划 → 执行 → 反馈 → 再计划", "隐式，在策略里", "在想象里滚动，再交给 actor / MPC", "逐步选边或连续控制", "通常不直接控"],
    ],
  },
  doNotMix: [
    {
      title: "Having a VLA is not having an agent",
      titleZh: "有 VLA 不等于有 Agent",
      body: "A single forward pass of OpenVLA is a policy. EmbodiedSkills / Physical Agency wrap a policy in propose–verify–recover.",
      bodyZh: "单次前向的 OpenVLA 是策略；EmbodiedSkills / Physical Agency 才把策略包进提案—验证—恢复。",
    },
    {
      title: "Having an LLM is not robot control",
      titleZh: "有 LLM 不等于会控机器人",
      body: "HuggingGPT / ReAct are tool-use precursors; whether they drive a body depends on executable actions or a real / embodied environment in the abstract.",
      bodyZh: "HuggingGPT / ReAct 是工具使用前驱；是否接到本体要看摘要是否出现可执行动作或真机 / 具身环境。",
    },
    {
      title: "Symbolic world state is not a Dreamer WM",
      titleZh: "符号世界状态不是 Dreamer 的 WM",
      body: "Statler-style prompted state read/write is not learned action-conditioned dynamics.",
      bodyZh: "Statler 的提示符号状态读写，不是学得的动作条件动力学。",
    },
  ],
};
