import { useMemo, useState } from "react";
import { papers } from "../data/papers.js";
import { filterDimensions, localizeFilterDimensions } from "../data/taxonomy.js";
import FilterBar from "./FilterBar.jsx";
import PaperCard from "./PaperCard.jsx";
import { papersCopy } from "../i18n.js";

const INITIAL_SELECTIONS = Object.fromEntries(filterDimensions.map(({ id }) => [id, []]));
const YEARS = papers.map((paper) => paper.year);
const YEAR_BOUNDS = [Math.min(...YEARS), Math.max(...YEARS)];

function paperFacets(paper) {
  return { family: paper.tags, source: paper.sources };
}

const indexedPapers = papers.map((paper) => ({ ...paper, facets: paperFacets(paper) }));

export default function PapersTab({ lang }) {
  const [selections, setSelections] = useState(INITIAL_SELECTIONS);
  const [yearRange, setYearRange] = useState(YEAR_BOUNDS);
  const [query, setQuery] = useState("");
  const [sortBy, setSortBy] = useState("date");
  const dimensions = useMemo(() => localizeFilterDimensions(filterDimensions, lang), [lang]);
  const copy = papersCopy[lang];

  const facetCounts = useMemo(() => Object.fromEntries(dimensions.map((dimension) => [
    dimension.id,
    Object.fromEntries(dimension.options.map((option) => [
      option.value,
      indexedPapers.filter((paper) => paper.facets[dimension.id].includes(option.value)).length,
    ])),
  ])), [dimensions]);

  const visible = useMemo(() => {
    const normalizedQuery = query.trim().toLowerCase();
    return indexedPapers
      .filter((paper) => filterDimensions.every(({ id }) =>
        selections[id].length === 0 || selections[id].some((value) => paper.facets[id].includes(value))))
      .filter((paper) => paper.year >= yearRange[0] && paper.year <= yearRange[1])
      .filter((paper) => {
        if (!normalizedQuery) return true;
        return [
          paper.id,
          paper.title,
          paper.nickname,
          paper.abstract,
          paper.abstractZh,
          paper.venue,
          ...paper.authors,
          ...paper.tags,
        ].join(" ").toLowerCase().includes(normalizedQuery);
      })
      .sort((a, b) => sortBy === "title"
        ? a.title.localeCompare(b.title)
        : b.year - a.year || a.title.localeCompare(b.title));
  }, [selections, yearRange, query, sortBy]);

  const toggleOption = (dimensionId, optionValue) => setSelections((current) => ({
    ...current,
    [dimensionId]: current[dimensionId].includes(optionValue)
      ? current[dimensionId].filter((value) => value !== optionValue)
      : [...current[dimensionId], optionValue],
  }));

  const clearDimension = (dimensionId) => setSelections((current) => ({ ...current, [dimensionId]: [] }));
  const clearFilters = () => {
    setSelections(INITIAL_SELECTIONS);
    setYearRange(YEAR_BOUNDS);
    setQuery("");
  };

  return (
    <>
      <FilterBar
        dimensions={dimensions}
        selections={selections}
        facetCounts={facetCounts}
        onToggle={toggleOption}
        onClearDimension={clearDimension}
        yearBounds={YEAR_BOUNDS}
        yearRange={yearRange}
        onYearRangeChange={setYearRange}
        citationBounds={null}
        citationRange={null}
        onCitationRangeChange={() => {}}
        query={query}
        onQueryChange={setQuery}
        sortBy={sortBy}
        onSortChange={setSortBy}
        resultCount={visible.length}
        totalCount={papers.length}
        onClear={clearFilters}
        lang={lang}
        sortOptions={[
          { value: "date", label: lang === "zh" ? "最新发表" : "Newest" },
          { value: "title", label: lang === "zh" ? "标题" : "Title" },
        ]}
      />
      {visible.length === 0 ? (
        <div className="empty-state">
          <b>{copy.noPapers}</b>
          <span>{copy.noPapersHint}</span>
          <button onClick={clearFilters}>{copy.reset}</button>
        </div>
      ) : (
        <div className="paper-list">
          {visible.map((paper) => <PaperCard key={paper.id} paper={paper} lang={lang} />)}
        </div>
      )}
    </>
  );
}
