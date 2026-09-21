import { dataFiles, documents, gaps, scripts } from "../data/resources.js";
import { localizedValue, resourcesCopy } from "../i18n.js";

function ResourceCard({ title, by, description, url }) {
  return (
    <div className="resource-card">
      <h3>
        {url ? <a href={url} target="_blank" rel="noreferrer">{title}</a> : title}
      </h3>
      <p>{description}</p>
      <span className="resource-by">{by}</span>
    </div>
  );
}

export default function ResourcesTab({ lang }) {
  const copy = resourcesCopy[lang];
  const sections = [
    [copy.docs, documents],
    [copy.data, dataFiles],
    [copy.gaps, gaps],
    [copy.scripts, scripts],
  ];

  return (
    <>
      {sections.map(([heading, items]) => (
        <section className="resource-section" key={heading}>
          <h2>{heading}</h2>
          <div className="resource-grid">
            {items.map((item) => (
              <ResourceCard
                key={item.title}
                title={localizedValue(item, "title", lang)}
                by={localizedValue(item, "by", lang)}
                description={localizedValue(item, "description", lang)}
                url={item.url}
              />
            ))}
          </div>
        </section>
      ))}
    </>
  );
}
