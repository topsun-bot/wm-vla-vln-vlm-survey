import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { papers } from "../site/src/data/papers.js";
import { oss } from "../site/src/data/oss.js";
import { FAMILY_OPTIONS } from "../site/src/data/taxonomy.js";
import { catalogData, renderCatalog, renderReadme, replaceSection } from "./generate-readme.mjs";

test("every paper and repository keeps its verified HTTPS source", () => {
  const { papers: paperRows, oss: ossRows } = catalogData();
  for (const paper of papers) {
    assert.equal(paperRows.find(({ id }) => id === paper.id).arxiv, paper.arxiv);
    assert.match(paper.arxiv, /^https:\/\/arxiv\.org\//);
  }
  for (const repo of oss) {
    assert.equal(ossRows.find(({ id }) => id === repo.id).url, repo.url);
    assert.match(repo.url, /^https:\/\/github\.com\//);
  }
});

test("every paper appears once per matching family group", () => {
  const catalog = renderCatalog();
  const papersSection = catalog.split("## Open-source landscape")[0];
  for (const paper of papers) {
    const count = paper.tags.filter((tag) => FAMILY_OPTIONS.some((option) => option.value === tag)).length;
    assert.equal(papersSection.split(`](${paper.arxiv})`).length - 1, count, paper.title);
  }
});

test("generated sections preserve hand-written content and are idempotent", async () => {
  const markdown = await readFile(new URL("../README.md", import.meta.url), "utf8");
  const generated = renderReadme(markdown);
  const strip = (text) => text.replace(/(<!-- BEGIN GENERATED (\w+) -->)[\s\S]*?(<!-- END GENERATED \2 -->)/g, "$1$3");
  assert.equal(strip(generated), strip(markdown));
  assert.equal(renderReadme(generated), generated);
});

test("missing, repeated, or reversed markers fail instead of overwriting prose", () => {
  const start = "<!-- BEGIN GENERATED COUNTS -->";
  const end = "<!-- END GENERATED COUNTS -->";
  for (const markdown of ["", start, `${start}${start}${end}`, `${start}${end}${end}`, `${end}${start}`]) {
    assert.throws(() => replaceSection(markdown, "COUNTS", "new"));
  }
});

test("all generated data rows have the expected number of table cells", () => {
  let columns;
  for (const line of renderCatalog().split("\n")) {
    if (!line.startsWith("|")) {
      columns = undefined;
      continue;
    }
    const count = line.split("|").length;
    if (columns === undefined) columns = count;
    assert.equal(count, columns, line);
  }
});
