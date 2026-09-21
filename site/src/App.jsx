import { useEffect, useState } from "react";
import GuideTab from "./components/GuideTab.jsx";
import PapersTab from "./components/PapersTab.jsx";
import OssTab from "./components/OssTab.jsx";
import GraphTab from "./components/GraphTab.jsx";
import ResourcesTab from "./components/ResourcesTab.jsx";
import { appCopy, getInitialLanguage } from "./i18n.js";

const REPO_URL = "https://github.com/topsun-bot/wm-vla-vln-vlm-survey";
const TAB_HASHES = {
  guide: "#guide",
  resources: "#resources",
  oss: "#oss",
  graph: "#graph",
  papers: "",
};

function tabFromHash() {
  if (window.location.hash.startsWith("#guide") || window.location.hash.startsWith("#blog")) return "guide";
  if (window.location.hash === "#resources") return "resources";
  if (window.location.hash.startsWith("#graph") || window.location.hash === "#oss-graph") return "graph";
  if (window.location.hash.startsWith("#oss") || window.location.hash.startsWith("#methods")) return "oss";
  return "papers";
}

function useTheme() {
  const [theme, setTheme] = useState(
    () => document.documentElement.getAttribute("data-theme") ?? "light",
  );
  useEffect(() => {
    document.documentElement.setAttribute("data-theme", theme);
    try {
      localStorage.setItem("wm-survey-theme", theme);
    } catch {}
  }, [theme]);
  return [theme, () => setTheme((current) => (current === "dark" ? "light" : "dark"))];
}

function useLanguage() {
  const [lang, setLang] = useState(getInitialLanguage);
  useEffect(() => {
    document.documentElement.setAttribute("data-lang", lang);
    document.documentElement.setAttribute("lang", lang === "zh" ? "zh-Hans" : "en");
    try {
      localStorage.setItem("wm-survey-lang", lang);
    } catch {}
  }, [lang]);
  return [lang, setLang];
}

export default function App() {
  const [tab, setTab] = useState(tabFromHash);
  const [theme, toggleTheme] = useTheme();
  const [lang, setLang] = useLanguage();
  const copy = appCopy[lang];

  useEffect(() => {
    document.title = copy.pageTitle;
    document.querySelector('meta[name="description"]')?.setAttribute("content", copy.pageDescription);
  }, [copy]);

  useEffect(() => {
    const syncTab = () => setTab(tabFromHash());
    window.addEventListener("hashchange", syncTab);
    return () => window.removeEventListener("hashchange", syncTab);
  }, []);

  const selectTab = (nextTab) => {
    const nextHash = TAB_HASHES[nextTab];
    const nextUrl = nextHash || `${window.location.pathname}${window.location.search}`;
    window.history.replaceState(null, "", nextUrl);
    window.dispatchEvent(new Event("hashchange"));
    setTab(nextTab);
  };

  return (
    <>
      <header className="site-header">
        <div className="header-inner">
          <a className="brand" href="#">
            <span className="brand-full">World Model × VLA / VLN / VLM</span>
            <span className="brand-short">WM × VLA</span>
          </a>
          <div className="header-actions">
            <div className="lang-segment" role="group" aria-label={copy.language}>
              {["en", "zh"].map((option) => (
                <button
                  type="button"
                  className={`lang-choice${lang === option ? " is-active" : ""}`}
                  aria-label={option === "en" ? copy.english : copy.chinese}
                  aria-pressed={lang === option}
                  onClick={() => setLang(option)}
                  key={option}
                >
                  {option.toUpperCase()}
                </button>
              ))}
            </div>
            <button className="icon-btn" onClick={toggleTheme} aria-label={copy.themeToggle}>
              {theme === "dark" ? "☀" : "☾"}
              <span className="icon-btn-label">{theme === "dark" ? copy.light : copy.dark}</span>
            </button>
            <a className="icon-btn" href={REPO_URL} target="_blank" rel="noreferrer">
              <span className="icon-btn-label">GitHub</span> ↗
            </a>
          </div>
        </div>
      </header>

      <section className="hero">
        <div className="container">
          <h1>
            {copy.heroTitleBefore}<em>{copy.heroTitleEmphasis}</em>{copy.heroTitleAfter}
          </h1>
          <p>{copy.heroBody}</p>
          <a
            className="hero-guide-link"
            href="#guide"
            onClick={() => window.setTimeout(
              () => document.getElementById("panel-guide")?.scrollIntoView({ behavior: "smooth" }),
              0,
            )}
          >
            <span>{copy.guideEyebrow}</span>
            {copy.guideLink}
            <b aria-hidden="true">→</b>
          </a>
        </div>
      </section>

      <main className="container">
        <nav className="tabs" role="tablist">
          {[
            ["guide", copy.tabs.guide],
            ["papers", copy.tabs.papers],
            ["oss", copy.tabs.oss],
            ["graph", copy.tabs.graph],
            ["resources", copy.tabs.resources],
          ].map(([id, label]) => (
            <button
              key={id}
              className={`tab${tab === id ? " is-active" : ""}`}
              role="tab"
              id={`tab-${id}`}
              aria-controls={`panel-${id}`}
              aria-selected={tab === id}
              onClick={() => selectTab(id)}
            >
              {label}
            </button>
          ))}
        </nav>
        <div id={`panel-${tab}`} role="tabpanel" aria-labelledby={`tab-${tab}`}>
          {tab === "guide"
            ? <GuideTab lang={lang} />
            : tab === "papers"
              ? <PapersTab lang={lang} />
              : tab === "oss"
                ? <OssTab lang={lang} />
                : tab === "graph"
                  ? <GraphTab lang={lang} />
                  : <ResourcesTab lang={lang} />}
        </div>
      </main>

      <footer className="site-footer">
        <div className="container">
          {copy.footerBefore}<a href={REPO_URL}>wm-vla-vln-vlm-survey</a>{copy.footerAfter}
        </div>
      </footer>
    </>
  );
}
