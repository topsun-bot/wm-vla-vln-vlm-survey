import { useState } from "react";
import { localizeFamily } from "../data/taxonomy.js";
import { paperCardCopy } from "../i18n.js";

const TAG_COLORS = {
  world_model: ["var(--accent-ink)", "var(--accent-soft)"],
  VLA: ["var(--blue)", "var(--blue-soft)"],
  VLN: ["var(--teal)", "var(--teal-soft)"],
  VLM: ["var(--purple)", "var(--purple-soft)"],
  "agent-robot": ["var(--amber)", "var(--amber-soft)"],
  "llm-agent": ["var(--gold)", "var(--gold-soft)"],
  intersection: ["var(--purple)", "var(--purple-soft)"],
};

function formatAuthors(authors, lang, copy) {
  if (!authors.length) return copy.authorsUnknown;
  if (authors.length <= 4) return authors.join(", ");
  if (lang === "zh") return `${authors.slice(0, 3).join(", ")} 等（${copy.authors(authors.length)}）`;
  return `${authors.slice(0, 3).join(", ")}, et al. (${copy.authors(authors.length)})`;
}

export default function PaperCard({ paper, lang }) {
  const [showAbstract, setShowAbstract] = useState(false);
  const [showProfile, setShowProfile] = useState(false);
  const copy = paperCardCopy[lang];
  const abstract = lang === "zh" ? paper.abstractZh || paper.abstract : paper.abstract;

  return (
    <article className="paper-card">
      <div className="paper-top">
        <span className="paper-nick">{paper.nickname}</span>
        <span className="paper-meta">
          <span>{paper.year}</span>
          <span>{paper.venue || copy.venueUnknown}</span>
          <span>arXiv:{paper.id}</span>
        </span>
      </div>
      <h3 className="paper-title">
        <a href={paper.arxiv} target="_blank" rel="noreferrer">{paper.title}</a>
      </h3>
      <p className="paper-authors">{formatAuthors(paper.authors, lang, copy)}</p>
      <div className="paper-tags">
        {paper.tags.map((tag) => {
          const [ink, bg] = TAG_COLORS[tag] ?? [];
          return (
            <span key={tag} className="tag" style={{ "--tag-ink": ink, "--tag-bg": bg }}>
              {localizeFamily(tag, lang)}
            </span>
          );
        })}
      </div>
      <div className="paper-links">
        <a href={paper.arxiv} target="_blank" rel="noreferrer">arXiv</a>
        <a href={paper.pdf} target="_blank" rel="noreferrer">PDF</a>
        <button className="abstract-toggle" type="button" onClick={() => setShowAbstract((value) => !value)}>
          {showAbstract ? copy.hideAbstract : copy.showAbstract}
        </button>
        <button
          className="abstract-toggle"
          type="button"
          aria-expanded={showProfile}
          onClick={() => setShowProfile((value) => !value)}
        >
          {showProfile ? copy.hideProfile : copy.showProfile}
        </button>
      </div>
      {showAbstract && <p className="paper-abstract">{abstract}</p>}
      {showProfile && (
        <section className="taxonomy-profile" aria-label={copy.profileLabel}>
          <div className="taxonomy-profile-row">
            <strong>{copy.source}</strong>
            <div>{paper.sources.map((source) => <span key={source}>{source}</span>)}</div>
          </div>
          {paper.highlightsZh.length > 0 && (
            <div className="taxonomy-profile-row">
              <strong>{copy.highlights}</strong>
              <div>
                {(lang === "zh" ? paper.highlightsZh : paper.highlightsZh).map((item) => (
                  <span key={item}>{item}</span>
                ))}
              </div>
            </div>
          )}
        </section>
      )}
    </article>
  );
}
