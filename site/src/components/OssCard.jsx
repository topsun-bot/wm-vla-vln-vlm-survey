import { useState } from "react";
import { ossCardCopy } from "../i18n.js";

export default function OssCard({ repo, lang }) {
  const [showProfile, setShowProfile] = useState(false);
  const copy = ossCardCopy[lang];

  return (
    <article className="paper-card method-card system-card">
      <div className="paper-top">
        <span className="paper-nick">{repo.nickname}</span>
        <span className="method-status is-system">{repo.family}</span>
        <span className="paper-meta">
          <span>{copy.stars(repo.stars)}</span>
          <span>{repo.license}</span>
        </span>
      </div>
      <h3 className="paper-title">
        <a href={repo.url} target="_blank" rel="noreferrer">{repo.title}</a>
      </h3>
      <p className="paper-authors system-maintainers">
        <strong>{copy.maintainers}</strong> {repo.org}
      </p>
      <p className="method-summary">{repo.notes}</p>
      <div className="paper-links">
        <a href={repo.url} target="_blank" rel="noreferrer">GitHub</a>
        {repo.relatedPapers.map((arxivId) => (
          <a key={arxivId} href={`https://arxiv.org/abs/${arxivId}`} target="_blank" rel="noreferrer">
            {arxivId}
          </a>
        ))}
        <button
          className="abstract-toggle"
          type="button"
          aria-expanded={showProfile}
          onClick={() => setShowProfile((value) => !value)}
        >
          {showProfile ? copy.hideProfile : copy.showProfile}
        </button>
      </div>
      {showProfile && (
        <section className="taxonomy-profile" aria-label={copy.profileLabel}>
          <div className="taxonomy-profile-row">
            <strong>{copy.family}</strong>
            <div><span>{repo.family}</span></div>
          </div>
          <div className="taxonomy-profile-row">
            <strong>{copy.license}</strong>
            <div><span>{repo.license}</span></div>
          </div>
          <div className="taxonomy-profile-row">
            <strong>{copy.modality}</strong>
            <div><span>{repo.modality}</span></div>
          </div>
          <div className="taxonomy-profile-row">
            <strong>{copy.activity}</strong>
            <div><span>{repo.lastActivity}</span></div>
          </div>
          <div className="taxonomy-profile-row">
            <strong>{copy.related}</strong>
            <div>
              {repo.relatedPapers.length
                ? repo.relatedPapers.map((arxivId) => <span key={arxivId}>{arxivId}</span>)
                : <span>{copy.noRelated}</span>}
            </div>
          </div>
        </section>
      )}
    </article>
  );
}
