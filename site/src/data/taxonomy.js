// Filter dimensions derived from tags already present in papers_merged.jsonl.
// Values within a row combine with OR; rows combine with AND.

export const FAMILY_OPTIONS = [
  {
    value: "world_model",
    label: "World Model",
    labelZh: "世界模型",
    description: "Learned (often latent) dynamics that predict future states, observations, or rewards given actions.",
    descriptionZh: "学习到的（常为潜空间）动力学，在动作条件下预测未来状态、观测或奖励。",
  },
  {
    value: "VLA",
    label: "VLA",
    labelZh: "VLA",
    description: "Vision-language-action policies that map vision plus language instructions to robot actions.",
    descriptionZh: "把视觉与语言指令映射到机器人动作的视觉—语言—动作策略。",
  },
  {
    value: "VLN",
    label: "VLN",
    labelZh: "VLN",
    description: "Vision-and-language navigation agents that follow natural-language route instructions.",
    descriptionZh: "在视觉环境中跟随自然语言路线指令的视觉—语言导航智能体。",
  },
  {
    value: "VLM",
    label: "VLM",
    labelZh: "VLM",
    description: "Vision-language models used as perception or semantic interfaces, typically not action policies by themselves.",
    descriptionZh: "作为感知或语义接口的视觉—语言模型，通常本身不是动作策略。",
  },
  {
    value: "agent-robot",
    label: "Agent-robot",
    labelZh: "Agent 控制机器人",
    description: "LLM / VLM runtimes that orchestrate perception, planning, tools, code, or skills to drive a robot or embodied body.",
    descriptionZh: "用 LLM / VLM 编排感知、规划、工具、代码或技能，再驱动机器人或具身本体。",
  },
  {
    value: "llm-agent",
    label: "LLM-agent",
    labelZh: "LLM 智能体",
    description: "Planning / tool-use landmarks widely cited by robot loops (for example ReAct-style agents).",
    descriptionZh: "被机器人闭环广泛引用的规划 / 工具使用地标（如 ReAct 一类）。",
  },
  {
    value: "intersection",
    label: "Intersection",
    labelZh: "交叉",
    description: "Works that couple world-model imagination with VLA / VLN, or use world-model-style prediction inside language-conditioned control.",
    descriptionZh: "显式把世界模型想象接到 VLA / VLN，或在语言条件控制中使用世界模型式预测。",
  },
];

export const SOURCE_OPTIONS = [
  {
    value: "world_model",
    label: "World-model table",
    labelZh: "世界模型表",
    description: "Entered from the world-model verification table.",
    descriptionZh: "来自世界模型核验表。",
  },
  {
    value: "vla_vln_vlm",
    label: "VLA / VLN / VLM table",
    labelZh: "VLA / VLN / VLM 表",
    description: "Entered from the VLA / VLN / VLM verification table.",
    descriptionZh: "来自 VLA / VLN / VLM 核验表。",
  },
  {
    value: "agent_robot",
    label: "Agent-robot table",
    labelZh: "Agent 控制机器人表",
    description: "Entered from the agent-controls-robot expansion.",
    descriptionZh: "来自 Agent 控制机器人扩表。",
  },
  {
    value: "researcher_pack",
    label: "Researcher pack",
    labelZh: "研究员核验包",
    description: "Merged from the researcher-verified agent-robotics pack after de-duplication.",
    descriptionZh: "来自研究员核验包，去重后并入。",
  },
];

export const filterDimensions = [
  {
    id: "family",
    label: "Family",
    help: {
      summary: "Survey tags already stored on each verified paper. A paper can carry more than one tag.",
      items: FAMILY_OPTIONS.map((option) => ({
        term: option.label,
        description: option.description,
      })),
      note: "These labels come from papers_merged.jsonl. Selecting several values in this row keeps papers that match any of them.",
    },
    options: FAMILY_OPTIONS.map(({ value, label }) => ({ value, label })),
  },
  {
    id: "source",
    label: "Pack source",
    help: {
      summary: "Which verification table introduced the paper. Multi-source papers keep the union.",
      items: SOURCE_OPTIONS.map((option) => ({
        term: option.label,
        description: option.description,
      })),
      note: "Source fields are copied from the jsonl record; they are not inferred from the title.",
    },
    options: SOURCE_OPTIONS.map(({ value, label }) => ({ value, label })),
  },
];

export const familyLabelsZh = Object.fromEntries(FAMILY_OPTIONS.map((option) => [option.value, option.labelZh]));
export const sourceLabelsZh = Object.fromEntries(SOURCE_OPTIONS.map((option) => [option.value, option.labelZh]));

export function localizeFilterDimensions(dimensions, lang) {
  if (lang !== "zh") return dimensions;
  return dimensions.map((dimension) => {
    const labels = dimension.id === "family" ? familyLabelsZh : sourceLabelsZh;
    const helpItems = dimension.id === "family" ? FAMILY_OPTIONS : SOURCE_OPTIONS;
    return {
      ...dimension,
      label: dimension.id === "family" ? "家族" : "来源表",
      help: {
        summary: dimension.id === "family"
          ? "每篇已核验论文上已有的调研标签。一篇可以带多个标签。"
          : "论文最初进入本包时的核验表。多源条目保留并集。",
        items: helpItems.map((option) => ({
          term: option.labelZh,
          description: option.descriptionZh,
        })),
        note: dimension.id === "family"
          ? "标签来自 papers_merged.jsonl。同一行内多选按“或”保留。"
          : "来源字段直接复制 jsonl 记录，不根据标题推断。",
      },
      options: dimension.options.map((option) => ({
        ...option,
        label: labels[option.value] ?? option.label,
      })),
    };
  });
}

export function localizeFamily(value, lang) {
  if (lang !== "zh") {
    return FAMILY_OPTIONS.find((option) => option.value === value)?.label ?? value;
  }
  return familyLabelsZh[value] ?? value;
}
