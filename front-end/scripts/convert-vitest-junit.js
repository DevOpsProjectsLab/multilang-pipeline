import fs from "fs";
import { parse } from "path";

const reportPath = "report-node.json";
const outputPath = "report-node.xml";

if (!fs.existsSync(reportPath)) {
  console.error("Vitest JSON report not found.");
  process.exit(1);
}

const json = JSON.parse(fs.readFileSync(reportPath, "utf-8"));
let xml = `<?xml version="1.0" encoding="UTF-8"?>\n<testsuites name="vitest">\n`;

for (const suite of json.testResults || []) {
  const suiteName = parse(suite.name).base;
  xml += `  <testsuite name="${suiteName}" tests="${suite.assertionResults.length}">\n`;
  for (const test of suite.assertionResults) {
    const durationSec = (test.duration ?? 0) / 1000
    xml += `    <testcase classname="${suiteName}" name="${test.title}" time="${durationSec.toFixed(3)}">\n`
    if (test.status !== "passed") {
      const msg = test.failureMessages?.join("\n") || test.status;
      xml += `      <failure message="${test.status}">${msg}</failure>\n`;
    }
    xml += `    </testcase>\n`;
  }

  xml += `  </testsuite>\n`;
}

xml += `</testsuites>`;

fs.writeFileSync(outputPath, xml);
console.log(`Generated ${outputPath}`);
