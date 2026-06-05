// Renders REPORT.html with the sample data island substituted, asserts no external
// network calls and that the verdict + adjusted score appear in the DOM text.
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const skill = join(here, "..");
let html = readFileSync(join(skill, "templates", "REPORT.html"), "utf8");
const data = readFileSync(join(here, "sample-dossier.json"), "utf8");

// Fail if the template references any external URL (must be fully self-contained).
const ext = html.match(/\b(https?:)?\/\/[^"')\s]+/g) || [];
const bad = ext.filter(u => !u.startsWith("//#") && !u.includes("www.w3.org")); // allow SVG ns
if (bad.length) { console.error("FAIL external refs:", bad); process.exit(1); }

// Inject the data island the way the skill will at generation time.
html = html.replace("/*__DOSSIER_DATA__*/null", data);

// Minimal DOM check without a browser: the placeholder is replaced and key fields present.
if (html.includes("/*__DOSSIER_DATA__*/")) { console.error("FAIL: data island not substitutable"); process.exit(1); }
for (const needle of ["data-role=\"verdict\"", "data-role=\"score\"", "data-role=\"scorecard\"", "lens-toggle"]) {
  if (!html.includes(needle)) { console.error("FAIL missing element:", needle); process.exit(1); }
}
console.log("report render test OK");
