// Resources already present in this repository. Do not invent external books or courses.

export const documents = [
  {
    title: "Paper index",
    titleZh: "论文索引",
    description: "Year-grouped title list with tags and arXiv links (PAPERS.md).",
    descriptionZh: "按年排列的标题索引，含标签与 arXiv 链接（PAPERS.md）。",
    url: "https://github.com/topsun-bot/wm-vla-vln-vlm-survey/blob/main/PAPERS.md",
    by: "PAPERS.md",
  },
  {
    title: "Paper cards",
    titleZh: "论文详注",
    description: "Per-paper fetched abstract plus Chinese paraphrase and notes (PAPERS_DETAIL.md).",
    descriptionZh: "逐篇实抓摘要、中文转述与要点（PAPERS_DETAIL.md）。",
    url: "https://github.com/topsun-bot/wm-vla-vln-vlm-survey/blob/main/PAPERS_DETAIL.md",
    by: "PAPERS_DETAIL.md",
  },
  {
    title: "English crosswalk",
    titleZh: "英文交叉对照",
    description: "Definitions, stack sketch, OSS honesty notes, and ODM integration notes.",
    descriptionZh: "定义、组合草图、开源诚实说明与 ODM 接入笔记。",
    url: "https://github.com/topsun-bot/wm-vla-vln-vlm-survey/blob/main/CROSSWALK.md",
    by: "CROSSWALK.md",
  },
  {
    title: "Chinese crosswalk",
    titleZh: "中文交叉对照",
    description: "Parallel Chinese companion to the English crosswalk, including the agent-robot contrast table.",
    descriptionZh: "英文对照的中文并行文档，含 Agent 控制机器人对照表。",
    url: "https://github.com/topsun-bot/wm-vla-vln-vlm-survey/blob/main/CROSSWALK.zh.md",
    by: "CROSSWALK.zh.md",
  },
  {
    title: "OSS comparison",
    titleZh: "开源对照表",
    description: "42 verified repositories with license, stars snapshot, modality, and related arXiv IDs.",
    descriptionZh: "42 个已核验仓库：许可、star 快照、模态与相关 arXiv ID。",
    url: "https://github.com/topsun-bot/wm-vla-vln-vlm-survey/blob/main/oss_repos.md",
    by: "oss_repos.md",
  },
  {
    title: "Org forks",
    titleZh: "组织 fork",
    description: "Upstreams already forked to topsun-bot (OpenVLA, Octo, DreamerV3, VLN-CE, and others).",
    descriptionZh: "已 fork 到 topsun-bot 的上游（OpenVLA、Octo、DreamerV3、VLN-CE 等）。",
    url: "https://github.com/topsun-bot/wm-vla-vln-vlm-survey/blob/main/forks_created.md",
    by: "forks_created.md",
  },
];

export const dataFiles = [
  {
    title: "papers_merged.jsonl",
    description: "Merged verified paper records: sources, tags, fetched abstracts.",
    descriptionZh: "合并后的已核验论文记录：来源、标签、实抓摘要。",
    url: "https://github.com/topsun-bot/wm-vla-vln-vlm-survey/blob/main/papers_merged.jsonl",
    by: "Machine-readable",
    byZh: "机器可读",
  },
  {
    title: "papers_detailed.jsonl",
    description: "Detail-page rows: English abstract, Chinese paraphrase, highlights.",
    descriptionZh: "详注行：英文摘要、中文转述、要点。",
    url: "https://github.com/topsun-bot/wm-vla-vln-vlm-survey/blob/main/papers_detailed.jsonl",
    by: "Machine-readable",
    byZh: "机器可读",
  },
  {
    title: "oss_repos.jsonl",
    description: "One JSON object per verified repository, including related_papers.",
    descriptionZh: "每个已核验仓库一行，含 related_papers。",
    url: "https://github.com/topsun-bot/wm-vla-vln-vlm-survey/blob/main/oss_repos.jsonl",
    by: "Machine-readable",
    byZh: "机器可读",
  },
  {
    title: "research/agent_robotics/",
    description: "Researcher-verified agent-robotics pack (list, metadata, agent crosswalk).",
    descriptionZh: "研究员核验的 Agent 控制机器人包（清单、元数据、Agent 对照）。",
    url: "https://github.com/topsun-bot/wm-vla-vln-vlm-survey/tree/main/research/agent_robotics",
    by: "Research pack",
    byZh: "研究包",
  },
];

export const gaps = [
  {
    title: "GAIA-1/2 (Wayve)",
    description: "Official code/weights are not open. Community lucidrains/gaia2-pytorch is architecture-level WIP only.",
    descriptionZh: "官方代码 / 权重未开放。社区 lucidrains/gaia2-pytorch 只是架构级 WIP。",
    url: "https://github.com/lucidrains/gaia2-pytorch",
    by: "oss_repos.md honesty notes",
  },
  {
    title: "Genie (DeepMind)",
    description: "Official stack is not open. Open reproductions in this pack: flairox/jafar and p-doom/jasmine.",
    descriptionZh: "官方栈未开放。本包开源复现：flairox/jafar 与 p-doom/jasmine。",
    url: "https://github.com/flairox/jafar",
    by: "oss_repos.md honesty notes",
  },
  {
    title: "UniSim",
    description: "Interactive UniSim world-model code was not found open (research page; google/unisim is unrelated).",
    descriptionZh: "未找到可交互的官方世界模型代码（研究页；google/unisim 是无关仓库）。",
    url: "https://github.com/topsun-bot/wm-vla-vln-vlm-survey/blob/main/oss_repos.md",
    by: "oss_repos.md honesty notes",
  },
  {
    title: "GameNGen",
    description: "No verified official OSS. Closest interactive video-WM OSS in this survey: Oasis / DIAMOND.",
    descriptionZh: "无核验过的官方 OSS。本调研中最接近的交互视频 WM 开源是 Oasis / DIAMOND。",
    url: "https://github.com/eloialonso/diamond",
    by: "oss_repos.md honesty notes",
  },
];

export const scripts = [
  {
    title: "scripts/fetch_arxiv_abstracts.py",
    description: "Fetch abstracts from the arXiv API; fall back to the abs page. Does not invent text.",
    descriptionZh: "从 arXiv API 抓摘要，限流则回退 abs 页。不编造文本。",
    url: "https://github.com/topsun-bot/wm-vla-vln-vlm-survey/blob/main/scripts/fetch_arxiv_abstracts.py",
    by: "Rebuild",
    byZh: "重建",
  },
  {
    title: "scripts/render_zh_docs.py",
    description: "Regenerate PAPERS.md / PAPERS_DETAIL.md from papers_detailed.jsonl.",
    descriptionZh: "由 papers_detailed.jsonl 重排 PAPERS.md / PAPERS_DETAIL.md。",
    url: "https://github.com/topsun-bot/wm-vla-vln-vlm-survey/blob/main/scripts/render_zh_docs.py",
    by: "Rebuild",
    byZh: "重建",
  },
  {
    title: "scripts/build-site-data.mjs",
    description: "Convert jsonl records into site/src/data papers, OSS, and composition-graph modules.",
    descriptionZh: "把 jsonl 记录转成站点 papers / OSS / 组合图谱模块。",
    url: "https://github.com/topsun-bot/wm-vla-vln-vlm-survey/blob/main/scripts/build-site-data.mjs",
    by: "Site",
    byZh: "站点",
  },
  {
    title: "scripts/generate-readme.mjs",
    description: "Fill README counts and taxonomy lists from the generated site data.",
    descriptionZh: "用生成的站点数据填写 README 计数与分类列表。",
    url: "https://github.com/topsun-bot/wm-vla-vln-vlm-survey/blob/main/scripts/generate-readme.mjs",
    by: "Site",
    byZh: "站点",
  },
];
