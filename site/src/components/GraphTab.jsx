import { useMemo, useRef, useState } from "react";
import { compositionNodes, compositionEdges, compositionGraphMeta } from "../data/compositionGraph.js";
import { graphCopy, graphExplorerCopy } from "../i18n.js";
import CitationGraph from "./CitationGraph.jsx";

function searchableText(node) {
  return [node.id, node.nickname, node.title, ...(node.authors ?? [])].join(" ").toLowerCase();
}

export default function GraphTab({ lang }) {
  const [query, setQuery] = useState("");
  const [resultsOpen, setResultsOpen] = useState(false);
  const [activeResult, setActiveResult] = useState(0);
  const [focusRequest, setFocusRequest] = useState(null);
  const focusSequence = useRef(0);
  const copy = graphExplorerCopy[lang];
  const graphText = graphCopy[lang];

  const matches = useMemo(() => {
    const normalized = query.trim().toLowerCase();
    if (!normalized) return [];
    return compositionNodes.filter((node) => searchableText(node).includes(normalized)).slice(0, 8);
  }, [query]);

  const focusNode = (node) => {
    focusSequence.current += 1;
    setQuery(node.nickname);
    setResultsOpen(false);
    setActiveResult(0);
    setFocusRequest({ id: node.id, sequence: focusSequence.current });
  };

  return (
    <section className="graph-explorer" aria-label={copy.title}>
      <div className="graph-explorer-toolbar">
      <label className="search-field graph-search graph-node-search">
        <span className="search-icon" aria-hidden="true">⌕</span>
        <input
          type="search"
          placeholder={copy.searchPlaceholder}
          value={query}
          aria-label={copy.searchLabel}
          onChange={(event) => {
            setQuery(event.target.value);
            setResultsOpen(true);
            setActiveResult(0);
          }}
          onFocus={() => setResultsOpen(true)}
        />
      </label>
      {resultsOpen && query.trim() && (
        <div className="graph-search-results" role="listbox">
          {matches.length === 0 ? (
            <p>{copy.noResults}</p>
          ) : matches.map((node, index) => (
            <button
              key={node.id}
              type="button"
              className={index === activeResult ? "is-active" : ""}
              onClick={() => focusNode(node)}
            >
              <span>{node.nickname}</span>
              <small>{node.kind === "oss" ? node.title : node.id.replace("paper:", "arXiv:")}</small>
            </button>
          ))}
        </div>
      )}
      </div>
      <CitationGraph
        papers={compositionNodes}
        lang={lang}
        edges={compositionEdges}
        meta={compositionGraphMeta}
        copyOverride={graphText}
        nodeWeight={(node) => node.kind === "oss" ? node.citations : 1}
        primaryMetric={(node) => node.kind === "oss" ? node.citations : node.year || "—"}
        primaryMetricLabel={lang === "zh" ? "Star / 年份" : "Stars / year"}
        focusRequest={focusRequest}
      />
    </section>
  );
}
