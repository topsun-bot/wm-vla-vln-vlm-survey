import { guide } from "../data/guide.js";
import { guideCopy, localizedValue } from "../i18n.js";

export default function GuideTab({ lang }) {
  const copy = guideCopy[lang];
  return (
    <section className="blog-index" aria-label={copy.title}>
      <p className="graph-eyebrow">{copy.eyebrow}</p>
      <h2>{copy.title}</h2>
      <p>{copy.lead}</p>

      <div className="resource-grid" style={{ marginTop: "1.5rem" }}>
        {guide.definitions.map((item) => (
          <article className="resource-card" key={item.term}>
            <h3>{localizedValue(item, "term", lang)}</h3>
            <p>{localizedValue(item, "body", lang)}</p>
          </article>
        ))}
      </div>

      <section className="resource-section">
        <h2>{lang === "zh" ? "如何组合" : "How they compose"}</h2>
        <div className="resource-grid">
          {guide.compose.map((item) => (
            <article className="resource-card" key={item.title}>
              <h3>{localizedValue(item, "title", lang)}</h3>
              <p>{localizedValue(item, "body", lang)}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="resource-section">
        <h2>{lang === "zh" ? "不要混的三点" : "Do not mix these"}</h2>
        <div className="resource-grid">
          {guide.doNotMix.map((item) => (
            <article className="resource-card" key={item.title}>
              <h3>{localizedValue(item, "title", lang)}</h3>
              <p>{localizedValue(item, "body", lang)}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="resource-section">
        <h2>{lang === "zh" ? "对照" : "Contrast"}</h2>
        <div className="paper-card">
          <div className="taxonomy-profile" aria-label={lang === "zh" ? "家族对照" : "Family contrast"}>
            {(lang === "zh" ? guide.contrast.rowsZh : guide.contrast.rows).map((row, index) => (
              <div className="taxonomy-profile-row" key={row[0]}>
                <strong>{row[0]}</strong>
                <div>
                  {(lang === "zh" ? guide.contrast.headersZh : guide.contrast.headers).slice(1).map((header, column) => (
                    <span key={`${index}-${header}`}>{header}: {row[column + 1]}</span>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>
    </section>
  );
}
