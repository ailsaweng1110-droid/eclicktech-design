#!/usr/bin/env node
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const CORE_FILE = path.join(ROOT, "tokens.json");
const BRANDS_DIR = path.join(ROOT, "brands");
const DIST_DIR = path.join(ROOT, "dist");

function isObject(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

function deepMerge(base, override) {
  if (!isObject(base) || !isObject(override)) {
    return override;
  }

  const output = { ...base };
  for (const key of Object.keys(override)) {
    const baseValue = base[key];
    const overrideValue = override[key];
    if (isObject(baseValue) && isObject(overrideValue)) {
      output[key] = deepMerge(baseValue, overrideValue);
    } else {
      output[key] = overrideValue;
    }
  }
  return output;
}

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function writeJson(filePath, data) {
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2) + "\n", "utf8");
}

function build() {
  if (!fs.existsSync(CORE_FILE)) {
    throw new Error(`Core file not found: ${CORE_FILE}`);
  }
  if (!fs.existsSync(BRANDS_DIR)) {
    throw new Error(`Brands directory not found: ${BRANDS_DIR}`);
  }

  const coreTokens = readJson(CORE_FILE);
  fs.mkdirSync(DIST_DIR, { recursive: true });

  const brandFiles = fs
    .readdirSync(BRANDS_DIR)
    .filter((file) => file.endsWith(".json"))
    .sort();

  for (const fileName of brandFiles) {
    const filePath = path.join(BRANDS_DIR, fileName);
    const brandConfig = readJson(filePath);
    const brandName = brandConfig.brand || path.basename(fileName, ".json");
    const overrides = brandConfig.overrides || {};

    const merged = deepMerge(coreTokens, overrides);
    const output = {
      $meta: {
        brand: brandName,
        source: "tokens.json + brands/<brand>.json",
        generatedAt: new Date().toISOString()
      },
      ...merged
    };

    const outFile = path.join(DIST_DIR, `${brandName}.tokens.json`);
    writeJson(outFile, output);
    process.stdout.write(`Built ${path.relative(ROOT, outFile)}\n`);
  }
}

build();
