import { useMemo, useState } from "react";
import { oss } from "../data/oss.js";
import FilterBar from "./FilterBar.jsx";
import OssCard from "./OssCard.jsx";
import { ossCopy, ossFilterCopy } from "../i18n.js";

function licenseBucket(license) {
  if (license.startsWith("MIT")) return "MIT";
  if (license.startsWith("Apache")) return "Apache";
  if (license.includes("GPL")) return "GPL";
  if (license.includes("CC-BY")) return "CC";
  if (license.includes("OpenMDW")) return "OpenMDW";
  return "Unstated / other";
}

const families = [...new Set(oss.map((repo) => repo.family))].sort();
const filterDimensions = [
  {
    id: "family",
    label: "Family",
    help: {
      summary: "Repository families already recorded in oss_repos.jsonl.",
      items: families.map((family) => ({
        term: family,
        description: `Repositories tagged ${family} in the verified OSS table.`,
      })),
      note: "Family labels are copied from the jsonl; they are not inferred on the site.",
    },
    options: families.map((family) => ({ value: family, label: family })),
  },
  {
    id: "license",
    label: "License",
    help: {
      summary: "License buckets derived from the LICENSE text recorded on survey day.",
      items: [
        { term: "MIT", description: "MIT license recorded." },
        { term: "Apache", description: "Apache-2.0 recorded." },
        { term: "GPL", description: "GPL-family license recorded." },
        { term: "CC", description: "Creative Commons license recorded (often non-commercial)." },
        { term: "OpenMDW", description: "NVIDIA OpenMDW recorded." },
        { term: "Unstated / other", description: "No LICENSE found, or a license outside the buckets above." },
      ],
      note: "Recheck the upstream LICENSE before commercial use.",
    },
    options: ["MIT", "Apache", "GPL", "CC", "OpenMDW", "Unstated / other"].map((value) => ({ value, label: value })),
  },
];

const INITIAL_SELECTIONS = Object.fromEntries(filterDimensions.map(({ id }) => [id, []]));
const STARS = oss.map((repo) => repo.stars);
const STAR_BOUNDS = [Math.min(...STARS), Math.max(...STARS)];
const indexed = oss.map((repo) => ({
  ...repo,
  facets: { family: [repo.family], license: [licenseBucket(repo.license)] },
}));

function localizeOssDimensions(lang) {
  if (lang !== "zh") return filterDimensions;
  return filterDimensions.map((dimension) => (
    dimension.id === "family"
      ? {
        ...dimension,
        label: "家族",
        help: {
          summary: "oss_repos.jsonl 中已记录的仓库家族。",
          items: families.map((family) => ({
            term: family,
            description: `已核验开源表中标记为 ${family} 的仓库。`,
          })),
          note: "家族标签直接复制 jsonl，不在站点上推断。",
        },
      }
      : {
        ...dimension,
        label: "许可",
        help: {
          summary: "按调研日记录的 LICENSE 文本分桶。",
          items: [
            { term: "MIT", description: "记录为 MIT。" },
            { term: "Apache", description: "记录为 Apache-2.0。" },
            { term: "GPL", description: "记录为 GPL 系。" },
            { term: "CC", description: "记录为 Creative Commons（常含非商用）。" },
            { term: "OpenMDW", description: "记录为 NVIDIA OpenMDW。" },
            { term: "Unstated / other", description: "未找到 LICENSE，或不在上述分桶。" },
          ],
          note: "商用前请再核对本仓库上游 LICENSE。",
        },
      }
  ));
}

export default function OssTab({ lang }) {
  const [selections, setSelections] = useState(INITIAL_SELECTIONS);
  const [starRange, setStarRange] = useState(STAR_BOUNDS);
  const [query, setQuery] = useState("");
  const [sortBy, setSortBy] = useState("citations");
  const dimensions = useMemo(() => localizeOssDimensions(lang), [lang]);
  const copy = ossCopy[lang];
  const filterText = ossFilterCopy[lang];

  const facetCounts = useMemo(() => Object.fromEntries(filterDimensions.map((dimension) => [
    dimension.id,
    Object.fromEntries(dimension.options.map((option) => [
      option.value,
      indexed.filter((repo) => repo.facets[dimension.id].includes(option.value)).length,
    ])),
  ])), []);

  const visible = useMemo(() => {
    const normalizedQuery = query.trim().toLowerCase();
    return indexed
      .filter((repo) => filterDimensions.every(({ id }) =>
        selections[id].length === 0 || selections[id].some((value) => repo.facets[id].includes(value))))
      .filter((repo) => repo.stars >= starRange[0] && repo.stars <= starRange[1])
      .filter((repo) => {
        if (!normalizedQuery) return true;
        return [
          repo.id,
          repo.name,
          repo.org,
          repo.notes,
          repo.license,
          repo.family,
          repo.modality,
          ...repo.relatedPapers,
        ].join(" ").toLowerCase().includes(normalizedQuery);
      })
      .sort((a, b) => sortBy === "citations"
        ? b.stars - a.stars || a.name.localeCompare(b.name)
        : a.name.localeCompare(b.name));
  }, [selections, starRange, query, sortBy]);

  const toggleOption = (dimensionId, optionValue) => setSelections((current) => ({
    ...current,
    [dimensionId]: current[dimensionId].includes(optionValue)
      ? current[dimensionId].filter((value) => value !== optionValue)
      : [...current[dimensionId], optionValue],
  }));

  const clearDimension = (dimensionId) => setSelections((current) => ({ ...current, [dimensionId]: [] }));
  const clearFilters = () => {
    setSelections(INITIAL_SELECTIONS);
    setStarRange(STAR_BOUNDS);
    setQuery("");
  };

  return (
    <section className="methods-index">
      <FilterBar
        dimensions={dimensions}
        selections={selections}
        facetCounts={facetCounts}
        onToggle={toggleOption}
        onClearDimension={clearDimension}
        yearBounds={null}
        yearRange={null}
        onYearRangeChange={() => {}}
        citationBounds={STAR_BOUNDS}
        citationRange={starRange}
        onCitationRangeChange={setStarRange}
        query={query}
        onQueryChange={setQuery}
        sortBy={sortBy}
        onSortChange={setSortBy}
        resultCount={visible.length}
        totalCount={oss.length}
        onClear={clearFilters}
        lang={lang}
        copyOverride={filterText}
        sortOptions={[
          { value: "citations", label: filterText.mostCited },
          { value: "date", label: filterText.newest },
        ]}
      />
      {visible.length === 0 ? (
        <div className="empty-state">
          <b>{copy.noRepos}</b>
          <span>{copy.noReposHint}</span>
          <button onClick={clearFilters}>{copy.reset}</button>
        </div>
      ) : (
        <div className="paper-list method-list">
          {visible.map((repo) => <OssCard key={repo.id} repo={repo} lang={lang} />)}
        </div>
      )}
    </section>
  );
}
