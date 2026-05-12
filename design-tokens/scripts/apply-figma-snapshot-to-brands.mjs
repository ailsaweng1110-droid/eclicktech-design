#!/usr/bin/env node
/**
 * Merges scripts/figma-variable-snapshot.json into brands/*.json
 * - Light: semantic + layout + typography from snapshot "Brand"
 * - Dark: brand + status colors from "Brand / Dark"; neutral.* kept when Figma is still #000000 placeholder
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const SNAPSHOT = path.join(__dirname, "figma-variable-snapshot.json");
const BRANDS_DIR = path.join(ROOT, "brands");

function figPathToSemanticKey(figPath) {
  if (!figPath.startsWith("color/")) return null;
  let s = figPath.split("/").join(".");
  s = s.replace(/\.info-bg$/, ".info.bg");
  return s;
}

function figPathToLayoutKey(figPath) {
  if (figPath.startsWith("space/") || figPath.startsWith("radius/")) return figPath;
  return null;
}

function figPathToTypographyKey(figPath) {
  if (!figPath.startsWith("font/")) return null;
  return figPath.split("/").join(".");
}

function roundFloat(v) {
  if (typeof v !== "number") return v;
  if (Math.abs(v - Math.round(v)) < 1e-6) return Math.round(v);
  return Math.round(v * 10000) / 10000;
}

function buildLightParts(flat) {
  const semantic = {};
  const layout = {};
  const typography = {};
  for (const [figPath, val] of Object.entries(flat)) {
    const sem = figPathToSemanticKey(figPath);
    if (sem) {
      semantic[sem] = { value: val, type: "color" };
      continue;
    }
    const lay = figPathToLayoutKey(figPath);
    if (lay) {
      layout[lay] = { value: roundFloat(val), type: "float" };
      continue;
    }
    const typ = figPathToTypographyKey(figPath);
    if (typ) {
      const isString = typeof val === "string";
      typography[typ] = {
        value: isString ? val : roundFloat(val),
        type: isString ? "string" : "float",
      };
    }
  }
  return { semantic, layout, typography };
}

function mergeDarkSemantic(prevSemantic, darkFlat) {
  const out = { ...prevSemantic };
  for (const [figPath, val] of Object.entries(darkFlat)) {
    const sem = figPathToSemanticKey(figPath);
    if (!sem) continue;
    const isNeutralPlaceholder =
      sem.startsWith("color.neutral.") &&
      typeof val === "string" &&
      val.toLowerCase() === "#000000";
    if (isNeutralPlaceholder && prevSemantic[sem]) continue;
    out[sem] = { value: val, type: "color" };
  }
  return out;
}

function main() {
  const snap = JSON.parse(fs.readFileSync(SNAPSHOT, "utf8"));
  const brandNames = ["eclicktech", "cyberklick", "yeahmobi", "zmaticoo"];

  for (const brand of brandNames) {
    const filePath = path.join(BRANDS_DIR, `${brand}.json`);
    const data = JSON.parse(fs.readFileSync(filePath, "utf8"));
    const flatLight = snap.Brand[brand];
    const flatDark = snap["Brand / Dark"][brand];
    if (!flatLight || !flatDark) throw new Error(`Missing snapshot for ${brand}`);

    const { semantic, layout, typography } = buildLightParts(flatLight);

    if (!data.overrides) data.overrides = {};
    if (!data.overrides.light) data.overrides.light = {};
    data.overrides.light.semantic = semantic;
    data.overrides.layout = layout;
    data.overrides.typography = typography;

    if (!data.overrides.dark) data.overrides.dark = {};
    const prevSem = data.overrides.dark.semantic || {};
    data.overrides.dark.semantic = mergeDarkSemantic(prevSem, flatDark);

    fs.writeFileSync(filePath, JSON.stringify(data, null, 2) + "\n", "utf8");
    process.stdout.write(`Updated brands/${brand}.json\n`);
  }
}

main();
