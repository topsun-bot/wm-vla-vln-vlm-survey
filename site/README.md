# World Model × VLA / VLN / VLM — Landing Page

React + Vite single-page site for this survey, deployed to GitHub Pages.

## Develop

```bash
cd site
npm install
npm run dev
```

The explorer reads generated files in `src/data/`. Rebuild them from the repo jsonl (never invent entries):

```bash
node scripts/build-site-data.mjs
```

## Build

```bash
npm run build    # outputs to site/dist
```

GitHub Actions publishes `site/dist` to Pages. After the first successful workflow, enable Pages in the repo settings:

**Settings → Pages → Source: GitHub Actions**

Then set the repo homepage (About) to:

`https://topsun-bot.github.io/wm-vla-vln-vlm-survey/`

## Data

- `src/data/papers.js` — generated from `papers_merged.jsonl` / `papers_detailed.jsonl`
- `src/data/oss.js` — generated from `oss_repos.jsonl`
- `src/data/compositionGraph.js` — verified OSS `related_papers` edges only
- `src/data/taxonomy.js` — filter dimensions for the existing tags
- `src/data/resources.js` / `guide.js` — CROSSWALK definitions, OSS gaps, and repo documents
