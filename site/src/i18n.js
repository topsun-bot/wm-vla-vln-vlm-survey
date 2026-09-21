export const appCopy = {
  en: {
    pageTitle: "World Model × VLA / VLN / VLM — Survey",
    pageDescription:
      "A verified, filterable index of World Model × VLA / VLN / VLM papers and open-source stacks for robotics and embodied AI.",
    themeToggle: "Toggle theme",
    light: "Light",
    dark: "Dark",
    language: "Language",
    english: "English",
    chinese: "Chinese",
    heroTitleBefore: "A verified map of ",
    heroTitleEmphasis: "World Model × VLA / VLN / VLM",
    heroTitleAfter: " research",
    heroBody:
      "Papers and open-source stacks at the intersection of world models, vision-language-action, navigation, and multimodal models for robots — plus agent-controlled robots. Every abstract was fetched from arXiv; no invented citations.",
    guideEyebrow: "START HERE",
    guideLink: "Read the composition crosswalk",
    tabs: {
      guide: "Crosswalk",
      papers: "Papers",
      oss: "Open source",
      graph: "Composition graph",
      resources: "Resources",
    },
    footerBefore: "Maintained as part of ",
    footerAfter:
      ". Abstracts from arXiv API or abs pages. Open-source rows are survey-day snapshots. Contributions welcome — open a PR with a verified arXiv or GitHub URL.",
  },
  zh: {
    pageTitle: "World Model × VLA / VLN / VLM — 调研索引",
    pageDescription: "面向机器人与具身智能的世界模型 × VLA / VLN / VLM 已核验论文与开源栈索引。",
    themeToggle: "切换主题",
    light: "浅色",
    dark: "深色",
    language: "语言",
    english: "英文",
    chinese: "中文",
    heroTitleBefore: "",
    heroTitleEmphasis: "World Model × VLA / VLN / VLM",
    heroTitleAfter: " 已核验调研图谱",
    heroBody:
      "收录世界模型、视觉—语言—动作、导航与多模态模型在机器人上的交叉论文与开源栈，并补上 Agent 控制机器人。摘要均来自 arXiv，不编造引用。",
    guideEyebrow: "从这里开始",
    guideLink: "阅读组合交叉对照",
    tabs: {
      guide: "交叉对照",
      papers: "论文",
      oss: "开源",
      graph: "组合图谱",
      resources: "资源",
    },
    footerBefore: "本网站由 ",
    footerAfter:
      " 项目维护。摘要来自 arXiv API 或 abs 页。开源表为调研日快照。欢迎提交带已核验 arXiv 或 GitHub 链接的 PR。",
  },
};

export const papersCopy = {
  en: {
    noPapers: "No papers found",
    noPapersHint: "Try removing one of the filters or widening the year range.",
    reset: "Reset all filters",
  },
  zh: {
    noPapers: "没有符合条件的论文",
    noPapersHint: "可以尝试减少筛选条件，或扩大年份范围。",
    reset: "重置全部筛选",
  },
};

export const filterCopy = {
  en: {
    filterPapers: "Filter papers",
    resultCount: (visible, total) => ({ before: "", visible, middle: " of ", total, after: " papers" }),
    all: "All",
    includes: "Includes",
    note: "Note",
    explain: (label) => `Explain ${label}`,
    definitions: (label) => `${label} definitions`,
    onlyValue: "Only value in the current collection",
    minimum: (label) => `${label} minimum`,
    maximum: (label) => `${label} maximum`,
    numericRange: "Numeric range",
    publicationYear: "Publication year",
    citations: "Stars",
    logic: "OR within rows",
    logicAnd: "AND across rows",
    reset: "Reset all filters",
    searchPlaceholder: "Search within filtered papers by title, author, abstract, or arXiv ID",
    sortPapers: "Sort papers",
    sort: "Sort",
    newest: "Newest",
    mostCited: "Title",
    numericHelp: {
      summary: "Continuous filter for publication year recorded in the survey pack.",
      items: [
        { term: "Publication year", description: "Keep papers whose recorded year falls in the selected interval." },
      ],
      note: "This collection does not store citation counts, so there is no citation slider.",
    },
  },
  zh: {
    filterPapers: "筛选论文",
    resultCount: (visible, total) => ({ before: "共 ", visible, middle: " / ", total, after: " 篇论文" }),
    all: "全部",
    includes: "包含",
    note: "说明",
    explain: (label) => `查看“${label}”的定义`,
    definitions: (label) => `${label}的定义`,
    onlyValue: "当前合集只有这一个取值",
    minimum: (label) => `${label}下限`,
    maximum: (label) => `${label}上限`,
    numericRange: "数值范围",
    publicationYear: "发表年份",
    citations: "Star 数",
    logic: "同一行内按“或”筛选",
    logicAnd: "不同行之间按“且”筛选",
    reset: "重置全部筛选",
    searchPlaceholder: "在筛选结果中搜索标题、作者、摘要或 arXiv ID",
    sortPapers: "论文排序",
    sort: "排序",
    newest: "最新发表",
    mostCited: "标题",
    numericHelp: {
      summary: "按调研包中记录的发表年份连续筛选。",
      items: [
        { term: "发表年份", description: "只保留记录年份落在所选区间内的论文。" },
      ],
      note: "本包没有存储引用次数，因此没有引用滑块。",
    },
  },
};

export const paperCardCopy = {
  en: {
    authors: (count) => `${count} authors`,
    authorsUnknown: "Authors not recorded in the pack",
    venueUnknown: "Venue not recorded",
    showAbstract: "Show abstract ▾",
    hideAbstract: "Hide abstract ▴",
    showProfile: "Show survey notes ▾",
    hideProfile: "Hide survey notes ▴",
    profileLabel: "Survey notes from the pack",
    highlights: "Notes",
    source: "Pack source",
  },
  zh: {
    authors: (count) => `共 ${count} 位作者`,
    authorsUnknown: "本包未记录作者",
    venueUnknown: "未记录会议 / 期刊",
    showAbstract: "展开摘要 ▾",
    hideAbstract: "收起摘要 ▴",
    showProfile: "展开调研要点 ▾",
    hideProfile: "收起调研要点 ▴",
    profileLabel: "本包中的调研要点",
    highlights: "要点",
    source: "来源表",
  },
};

export const ossCopy = {
  en: {
    noRepos: "No repositories found",
    noReposHint: "Try removing one of the filters.",
    reset: "Reset all filters",
  },
  zh: {
    noRepos: "没有符合条件的仓库",
    noReposHint: "可以尝试减少筛选条件。",
    reset: "重置全部筛选",
  },
};

export const ossFilterCopy = {
  en: {
    filterPapers: "Filter open-source stacks",
    resultCount: (visible, total) => ({ before: "", visible, middle: " of ", total, after: " repositories" }),
    all: "All",
    includes: "Includes",
    note: "Note",
    explain: (label) => `Explain ${label}`,
    definitions: (label) => `${label} definitions`,
    onlyValue: "Only value in the current collection",
    minimum: (label) => `${label} minimum`,
    maximum: (label) => `${label} maximum`,
    numericRange: "Star snapshot",
    publicationYear: "Year",
    citations: "Stars (survey day)",
    logic: "OR within rows",
    logicAnd: "AND across rows",
    reset: "Reset all filters",
    searchPlaceholder: "Search repositories by name, org, notes, license, or related arXiv ID",
    sortPapers: "Repository sorting",
    sort: "Sort",
    newest: "Name",
    mostCited: "Most stars",
    numericHelp: {
      summary: "Star counts are snapshots from the survey date, not live GitHub values.",
      items: [
        { term: "Stars (survey day)", description: "Keep repositories whose recorded star count falls in the selected interval." },
      ],
      note: "Recheck GitHub before depending on activity or popularity.",
    },
  },
  zh: {
    filterPapers: "筛选开源栈",
    resultCount: (visible, total) => ({ before: "共 ", visible, middle: " / ", total, after: " 个仓库" }),
    all: "全部",
    includes: "包含",
    note: "说明",
    explain: (label) => `查看“${label}”的定义`,
    definitions: (label) => `${label}的定义`,
    onlyValue: "当前合集只有这一个取值",
    minimum: (label) => `${label}下限`,
    maximum: (label) => `${label}上限`,
    numericRange: "Star 快照",
    publicationYear: "年份",
    citations: "Star 数（调研日）",
    logic: "同一行内按“或”筛选",
    logicAnd: "不同行之间按“且”筛选",
    reset: "重置全部筛选",
    searchPlaceholder: "按名称、组织、说明、许可或相关 arXiv ID 搜索仓库",
    sortPapers: "仓库排序",
    sort: "排序",
    newest: "名称",
    mostCited: "Star 最多",
    numericHelp: {
      summary: "Star 数是调研日快照，不是实时 GitHub 数据。",
      items: [
        { term: "Star 数（调研日）", description: "只保留记录 star 数落在所选区间内的仓库。" },
      ],
      note: "依赖活跃度或热度前请再查 GitHub。",
    },
  },
};

export const ossCardCopy = {
  en: {
    maintainers: "Organization",
    stars: (count) => `${count} stars`,
    related: "Related papers",
    noRelated: "No arXiv IDs recorded for this repository",
    showProfile: "Show repository profile ▾",
    hideProfile: "Hide repository profile ▴",
    profileLabel: "Verified OSS profile",
    license: "License",
    modality: "Primary modality",
    activity: "Last activity hint",
    family: "Family",
  },
  zh: {
    maintainers: "组织",
    stars: (count) => `${count} stars`,
    related: "相关论文",
    noRelated: "本仓库未记录 arXiv ID",
    showProfile: "展开仓库档案 ▾",
    hideProfile: "收起仓库档案 ▴",
    profileLabel: "已核验开源档案",
    license: "许可",
    modality: "主要模态",
    activity: "最近活动提示",
    family: "家族",
  },
};

export const graphCopy = {
  en: {
    verifiedNetwork: "Verified paper ↔ OSS links",
    title: "Composition graph",
    intro:
      "Edges come only from oss_repos.jsonl related_papers fields. They are survey-recorded paper IDs for a repository, not a citation graph and not inferred from titles.",
    visiblePapers: "nodes",
    verifiedEdges: "verified links",
    controls: "Graph zoom controls",
    zoomIn: "Zoom in",
    zoomOut: "Zoom out",
    resetView: "Reset graph view",
    hint: "Drag to pan · scroll or pinch to zoom",
    networkLabel: (papers, edges) =>
      `Composition network with ${papers} nodes and ${edges} verified paper–repository links`,
    citations: "stars / papers",
    older: "Older / paper",
    newer: "Newer / OSS",
    nodeSize: "Node size = recorded stars (OSS) or 1 (paper)",
    cites: "repository records paper",
    noEdges: "No verified paper–repository links are available.",
    globalCitations: "recorded stars",
    citedByCorpus: "linked from OSS",
    referencesInCorpus: "linked papers",
    references: "Related papers",
    citedBy: "Related repositories",
    noReferences: "This node has no recorded related paper in the pack.",
    noCitations: "No verified repository in the pack points to this paper.",
    originalPdf: "OSS record",
    semanticScholar: "OSS record",
    openArxiv: "Open paper on arXiv ↗",
    openPaper: "Open repository ↗",
    provenanceLead:
      "Every edge is copied from a verified OSS row’s related_papers list. None are generated from keywords, topic similarity, or model inference.",
    snapshot: "Survey snapshot:",
  },
  zh: {
    verifiedNetwork: "已核验的论文 ↔ 开源链接",
    title: "组合图谱",
    intro:
      "边只来自 oss_repos.jsonl 的 related_papers 字段，是调研记录的仓库—论文对应，不是引用图谱，也不根据标题推断。",
    visiblePapers: "个节点",
    verifiedEdges: "条已核验链接",
    controls: "图谱缩放控制",
    zoomIn: "放大",
    zoomOut: "缩小",
    resetView: "重置图谱视图",
    hint: "拖动平移 · 滚轮或双指缩放",
    networkLabel: (papers, edges) =>
      `包含 ${papers} 个节点和 ${edges} 条已核验论文—仓库链接的图谱`,
    citations: "stars / 论文",
    older: "较早 / 论文",
    newer: "较新 / 开源",
    nodeSize: "节点大小：开源为记录 star 数，论文为 1",
    cites: "仓库记录该论文",
    noEdges: "当前没有已核验的论文—仓库链接。",
    globalCitations: "记录 star 数",
    citedByCorpus: "被开源记录",
    referencesInCorpus: "关联论文",
    references: "相关论文",
    citedBy: "相关仓库",
    noReferences: "该节点在本包中没有记录相关论文。",
    noCitations: "本包中没有已核验仓库指向这篇论文。",
    originalPdf: "开源记录",
    semanticScholar: "开源记录",
    openArxiv: "在 arXiv 查看论文 ↗",
    openPaper: "打开仓库 ↗",
    provenanceLead:
      "每一条边都复制自已核验开源行的 related_papers，不包含根据关键词、主题相似度或模型推断生成的关系。",
    snapshot: "调研快照：",
  },
};

export const graphExplorerCopy = {
  en: {
    title: "Composition graph explorer",
    searchLabel: "Find a node",
    searchPlaceholder: "Search title, repository, org, or arXiv ID",
    noResults: "No matching node found.",
  },
  zh: {
    title: "组合图谱浏览器",
    searchLabel: "查找节点",
    searchPlaceholder: "搜索标题、仓库、组织或 arXiv ID",
    noResults: "没有匹配的节点。",
  },
};

export const resourcesCopy = {
  en: {
    docs: "Survey documents",
    data: "Machine-readable data",
    gaps: "Open-source gaps",
    scripts: "Rebuild scripts",
    links: (title) => `${title} links`,
  },
  zh: {
    docs: "调研文档",
    data: "机器可读数据",
    gaps: "开源缺口",
    scripts: "重建脚本",
    links: (title) => `${title}相关链接`,
  },
};

export const guideCopy = {
  en: {
    eyebrow: "Composition",
    title: "How the families fit together",
    lead: "Short definitions and a stack sketch from the survey crosswalk. Papers remain the authors’; this pack only indexes verified links and fetched abstracts.",
  },
  zh: {
    eyebrow: "组合",
    title: "这些家族如何接在一起",
    lead: "来自交叉对照的短定义与栈草图。论文仍属原作者；本包只索引已核验链接与实抓摘要。",
  },
};

export function getInitialLanguage() {
  try {
    const saved = localStorage.getItem("wm-survey-lang");
    if (saved === "en" || saved === "zh") return saved;
  } catch {}
  return navigator.language?.toLowerCase().startsWith("zh") ? "zh" : "en";
}

export function localizedValue(item, field, lang) {
  return lang === "zh" ? item[`${field}Zh`] ?? item[field] : item[field];
}
