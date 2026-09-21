import { readFile, writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { papers, paperCounts } from "../site/src/data/papers.js";
import { oss } from "../site/src/data/oss.js";
import { FAMILY_OPTIONS } from "../site/src/data/taxonomy.js";

const readmePath = fileURLToPath(new URL("../README.md", import.meta.url));
const SITE = "https://topsun-bot.github.io/wm-vla-vln-vlm-survey/";
const escape = (value) => String(value).replaceAll("&", "&amp;").replaceAll("<", "&lt;")
  .replaceAll(">", "&gt;").replaceAll("|", "&#124;").replaceAll("[", "&#91;")
  .replaceAll("]", "&#93;").replaceAll("*", "&#42;").replaceAll("_", "&#95;")
  .replaceAll("\n", " ");
const link = (title, url) => `[${escape(title)}](${url})`;
const table = (headers, rows) => [
  `| ${headers.join(" | ")} |`,
  `| ${headers.map(() => ":---").join(" | ")} |`,
  ...rows.map((row) => `| ${row.join(" | ")} |`),
].join("\n");

export function catalogData() {
  const ids = new Set();
  for (const paper of papers) {
    if (ids.has(paper.id)) throw new Error(`Duplicate paper: ${paper.id}`);
    ids.add(paper.id);
    if (!paper.title || !paper.arxiv) throw new Error(`Incomplete paper: ${paper.id}`);
    if (!paper.arxiv.startsWith("https://")) throw new Error(`Missing HTTPS source: ${paper.id}`);
  }
  for (const repo of oss) {
    if (!repo.url.startsWith("https://github.com/")) throw new Error(`Missing GitHub URL: ${repo.id}`);
  }
  return { papers, oss, counts: paperCounts };
}

export function renderCounts() {
  const { counts } = catalogData();
  const tagBits = FAMILY_OPTIONS
    .map((option) => `${counts.tags[option.value] ?? 0} ${option.label}`)
    .join(" · ");
  return `**${counts.papers} papers · ${counts.oss} OSS repos · ${counts.abstracts}/${counts.papers} fetched abstracts**

Tag coverage: **${tagBits}**`;
}

export function renderCatalog() {
  const { papers: paperRows, oss: ossRows } = catalogData();
  const sections = [
    "## Papers",
    `[Compare all dimensions on the website →](${SITE})`,
    "Grouped by the survey tags already stored on each record. A paper can appear under more than one tag. Ordered by year, newest first, then title.",
  ];

  for (const option of FAMILY_OPTIONS) {
    sections.push(`### ${option.label}`);
    sections.push(option.description);
    const group = paperRows
      .filter((paper) => paper.tags.includes(option.value))
      .sort((a, b) => b.year - a.year || a.title.localeCompare(b.title));
    if (!group.length) {
      sections.push("No entries in this tag.");
      continue;
    }
    sections.push(table(
      ["Paper", "Year", "Tags"],
      group.map((paper) => [
        link(paper.title, paper.arxiv),
        String(paper.year),
        paper.tags.map((tag) => escape(FAMILY_OPTIONS.find((item) => item.value === tag)?.label ?? tag)).join(" · "),
      ]),
    ));
  }

  sections.push("## Open-source landscape");
  sections.push(`[Compare repositories on the website →](${SITE}#oss)`);
  sections.push("Grouped by the family field recorded in `oss_repos.jsonl`. Star counts are survey-day snapshots.");

  const families = [...new Set(ossRows.map((repo) => repo.family))].sort();
  for (const family of families) {
    sections.push(`### ${family}`);
    const group = ossRows
      .filter((repo) => repo.family === family)
      .sort((a, b) => b.stars - a.stars || a.name.localeCompare(b.name));
    sections.push(table(
      ["Repository", "License", "Stars", "Related papers"],
      group.map((repo) => [
        link(`${repo.org}/${repo.name}`, repo.url),
        escape(repo.license),
        String(repo.stars),
        repo.relatedPapers.length
          ? repo.relatedPapers.map((id) => `[${id}](https://arxiv.org/abs/${id})`).join(" · ")
          : "—",
      ]),
    ));
  }

  return sections.join("\n\n");
}

export function replaceSection(markdown, name, content) {
  const start = `<!-- BEGIN GENERATED ${name} -->`;
  const end = `<!-- END GENERATED ${name} -->`;
  if (markdown.split(start).length !== 2 || markdown.split(end).length !== 2) {
    throw new Error(`Expected exactly one ${name} marker pair`);
  }
  const a = markdown.indexOf(start) + start.length;
  const b = markdown.indexOf(end);
  if (a > b) throw new Error(`Reversed ${name} markers`);
  return `${markdown.slice(0, a)}\n\n${content}\n\n${markdown.slice(b)}`;
}

export function renderReadme(markdown) {
  return replaceSection(replaceSection(markdown, "COUNTS", renderCounts()), "CATALOG", renderCatalog());
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  if (process.argv.slice(2).some((arg) => arg !== "--check")) {
    throw new Error("Usage: node scripts/generate-readme.mjs [--check]");
  }
  const current = await readFile(readmePath, "utf8");
  const generated = renderReadme(current);
  if (process.argv.includes("--check")) {
    if (generated !== current) {
      console.error("README catalog is stale. Run: node scripts/generate-readme.mjs");
      process.exitCode = 1;
    } else {
      console.log("README catalog and counts match the site data.");
    }
  } else if (current !== generated) {
    await writeFile(readmePath, generated);
    console.log("Updated README catalog and counts from the site data.");
  } else {
    console.log("README is already up to date.");
  }
}
