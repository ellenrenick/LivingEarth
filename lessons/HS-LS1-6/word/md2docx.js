// Convert the HS-LS1-6 teacher plans (Markdown) into Word documents.
// Handles the Markdown subset the plans use: headings, paragraphs, bullet and
// numbered lists (one nested level), tables, blockquotes, rules, bold, italic,
// code, links, and <sub>/<sup>.
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  ShadingType, BorderStyle, HeadingLevel, AlignmentType, LevelFormat, Footer,
  PageNumber, PageBreak, TableLayoutType,
} = require("docx");

const SRC = process.argv[2];
const OUT = process.argv[3];
const TABLE_W = 9360; // 6.5" text width on Letter with 1" margins
const BORDER = { style: BorderStyle.SINGLE, size: 4, color: "999999" };
const BORDERS = { top: BORDER, bottom: BORDER, left: BORDER, right: BORDER };

// ---------- inline ----------
const INLINE = /(\*\*.+?\*\*|\*[^*\s][^*]*?\*|`[^`]+`|\[[^\]]+\]\([^)]+\)|<sub>.*?<\/sub>|<sup>.*?<\/sup>)/g;

function runs(text, fmt = {}) {
  const out = [];
  for (const part of text.split(INLINE)) {
    if (!part) continue;
    let m;
    if ((m = part.match(/^\*\*(.+)\*\*$/))) out.push(...runs(m[1], { ...fmt, bold: true }));
    else if ((m = part.match(/^\*([^*].*)\*$/))) out.push(...runs(m[1], { ...fmt, italics: true }));
    else if ((m = part.match(/^`(.+)`$/))) out.push(new TextRun({ text: m[1], ...fmt, font: "Consolas", size: 20 }));
    else if ((m = part.match(/^\[([^\]]+)\]\(([^)]+)\)$/))) out.push(...runs(m[1], fmt));
    else if ((m = part.match(/^<sub>(.*)<\/sub>$/))) out.push(...runs(m[1], { ...fmt, subScript: true }));
    else if ((m = part.match(/^<sup>(.*)<\/sup>$/))) out.push(...runs(m[1], { ...fmt, superScript: true }));
    else out.push(new TextRun({ text: part.replace(/&minus;/g, "−"), ...fmt }));
  }
  return out;
}

// Lines joined with hard breaks where the Markdown line ended in two spaces.
function paraRuns(lines) {
  const out = [];
  lines.forEach((l, i) => {
    if (i > 0) out.push(new TextRun({ text: "", break: 1 }));
    out.push(...runs(l.trim()));
  });
  return out;
}

// ---------- tables ----------
function splitRow(line) {
  return line.trim().replace(/^\|/, "").replace(/\|$/, "").split("|").map((c) => c.trim());
}

function table(lines) {
  const rows = lines.filter((l) => !/^\|\s*:?-{3,}/.test(l.trim())).map(splitRow);
  const n = Math.max(...rows.map((r) => r.length));
  // Column widths proportional to content length, with a floor so short columns stay readable.
  const plain = (s) => s.replace(/<[^>]+>|\*|`/g, "");
  const weight = [...Array(n)].map((_, c) =>
    Math.max(6, Math.min(60, Math.max(...rows.map((r) => plain(r[c] || "").length)))));
  const total = weight.reduce((a, b) => a + b, 0);
  const widths = weight.map((w) => Math.floor((w / total) * TABLE_W));
  widths[n - 1] += TABLE_W - widths.reduce((a, b) => a + b, 0);
  return new Table({
    width: { size: TABLE_W, type: WidthType.DXA },
    columnWidths: widths,
    layout: TableLayoutType.FIXED,
    rows: rows.map((r, ri) => new TableRow({
      ...(ri === 0 ? { tableHeader: true } : {}),
      cantSplit: true,
      children: widths.map((w, c) => new TableCell({
        width: { size: w, type: WidthType.DXA },
        borders: BORDERS,
        shading: ri === 0 ? { type: ShadingType.CLEAR, color: "auto", fill: "E8EEF4" } : undefined,
        margins: { top: 60, bottom: 60, left: 100, right: 100 },
        children: [new Paragraph({
          spacing: { after: 0 },
          children: runs(r[c] || "", ri === 0 ? { bold: true } : {}),
        })],
      })),
    })),
  });
}

// ---------- blocks ----------
let listInstance = 0;

function convert(md) {
  const lines = md.replace(/\r/g, "").split("\n");
  const out = [];
  let i = 0;
  let para = [];
  let lastListLevel = -1;
  let numberedInstance = [null, null];

  const flush = () => {
    if (para.length) out.push(new Paragraph({ children: paraRuns(para), spacing: { after: 120 } }));
    para = [];
  };
  const endList = () => { lastListLevel = -1; numberedInstance = [null, null]; };

  while (i < lines.length) {
    const line = lines[i];
    const t = line.trim();
    let m;
    if (!t) { flush(); i++; continue; }

    if ((m = line.match(/^(#{1,4})\s+(.*)$/))) {
      flush(); endList();
      const level = [HeadingLevel.TITLE, HeadingLevel.HEADING_1, HeadingLevel.HEADING_2, HeadingLevel.HEADING_3][m[1].length - 1];
      out.push(new Paragraph({ heading: level, children: runs(m[2]) }));
      i++; continue;
    }
    if (/^-{3,}$/.test(t)) {
      flush(); endList();
      out.push(new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "BBBBBB", space: 1 } }, spacing: { after: 160 } }));
      i++; continue;
    }
    if (t.startsWith("|")) {
      flush(); endList();
      const block = [];
      while (i < lines.length && lines[i].trim().startsWith("|")) block.push(lines[i++]);
      out.push(table(block));
      out.push(new Paragraph({ spacing: { after: 60 } }));
      continue;
    }
    if (t.startsWith(">")) {
      flush(); endList();
      const block = [];
      while (i < lines.length && lines[i].trim().startsWith(">")) block.push(lines[i++].trim().replace(/^>\s?/, ""));
      out.push(new Paragraph({
        children: paraRuns(block),
        indent: { left: 540 },
        border: { left: { style: BorderStyle.SINGLE, size: 18, color: "7A9CC6", space: 10 } },
        spacing: { after: 160 },
      }));
      continue;
    }
    if ((m = line.match(/^(\s*)([-*]|\d+\.)\s+(.*)$/))) {
      flush();
      const level = m[1].length >= 2 ? 1 : 0;
      const numbered = /\d/.test(m[2]);
      if (level === 0 && lastListLevel === -1) numberedInstance = [null, null];
      if (level === 1 && lastListLevel === 0) numberedInstance[1] = null;
      let numbering;
      if (numbered) {
        if (numberedInstance[level] === null) numberedInstance[level] = ++listInstance;
        numbering = { reference: "numbers", level, instance: numberedInstance[level] };
      } else {
        numbering = { reference: "bullets", level };
      }
      lastListLevel = level;
      // Lazy continuation lines belong to the same item.
      const body = [m[3]];
      i++;
      while (i < lines.length && lines[i].trim() && !/^\s*([-*]|\d+\.)\s+/.test(lines[i]) &&
             !/^(#|\||>)/.test(lines[i].trim()) && !/^\s{2,}/.test(lines[i])) body.push(lines[i++]);
      out.push(new Paragraph({ numbering, children: paraRuns(body), spacing: { after: 80 } }));
      continue;
    }
    if (/^\s{2,}\S/.test(line) && lastListLevel >= 0) {
      // Indented paragraph inside a list item.
      flush();
      out.push(new Paragraph({ children: paraRuns([t]), indent: { left: 720 }, spacing: { after: 80 } }));
      i++; continue;
    }
    endList();
    para.push(line);
    if (!/ {2}$/.test(line)) { /* soft wrap: keep collecting */ }
    i++;
  }
  flush();
  return out;
}

function numberingConfig() {
  const lvl = (level, format, text) => ({
    level, format, text, alignment: AlignmentType.LEFT,
    style: { paragraph: { indent: { left: 720 * (level + 1), hanging: 360 } } },
  });
  return {
    config: [
      { reference: "bullets", levels: [lvl(0, LevelFormat.BULLET, "•"), lvl(1, LevelFormat.BULLET, "◦")] },
      { reference: "numbers", levels: [lvl(0, LevelFormat.DECIMAL, "%1."), lvl(1, LevelFormat.LOWER_LETTER, "%2.")] },
    ],
  };
}

function buildDoc(sections) {
  return new Document({
    creator: "Living Earth",
    title: sections[0].title,
    styles: {
      default: { document: { run: { font: "Calibri", size: 22 } } },
      paragraphStyles: [
        { id: "Title", name: "Title", basedOn: "Normal", next: "Normal", run: { size: 40, bold: true, color: "1F3864" }, paragraph: { spacing: { after: 200 } } },
        { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 30, bold: true, color: "1F3864" }, paragraph: { spacing: { before: 280, after: 120 }, keepNext: true, outlineLevel: 0 } },
        { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 25, bold: true, color: "2E5A88" }, paragraph: { spacing: { before: 220, after: 100 }, keepNext: true, outlineLevel: 1 } },
        { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 23, bold: true, color: "2E5A88" }, paragraph: { spacing: { before: 160, after: 80 }, keepNext: true, outlineLevel: 2 } },
      ],
    },
    numbering: numberingConfig(),
    sections: sections.map((s) => ({
      properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } },
      footers: {
        default: new Footer({
          children: [new Paragraph({
            alignment: AlignmentType.RIGHT,
            children: [new TextRun({ text: `${s.footer}   |   Page `, size: 18, color: "666666" }),
                       new TextRun({ children: [PageNumber.CURRENT], size: 18, color: "666666" })],
          })],
        }),
      },
      children: s.children,
    })),
  });
}

function section(file) {
  const md = fs.readFileSync(file, "utf8");
  const title = md.match(/^#\s+(.*)$/m)[1];
  const short = title.startsWith("Lesson") ? `HS-LS1-6 ${title.split(":")[0]}` : "HS-LS1-6 Unit Overview";
  return { title, footer: short, children: convert(md) };
}

// Usage: node md2docx.js <file.md|dir> <out.docx|outdir>
const files = fs.statSync(SRC).isDirectory()
  ? ["README.md", ...fs.readdirSync(SRC).filter((f) => /^lesson_\d_.*\.md$/.test(f)).sort()].map((f) => path.join(SRC, f))
  : [SRC];

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  for (const f of files) {
    const base = path.basename(f) === "README.md" ? "HS-LS1-6_unit_overview" : path.basename(f, ".md");
    listInstance = 0;
    fs.writeFileSync(path.join(OUT, base + ".docx"), await Packer.toBuffer(buildDoc([section(f)])));
    console.log("wrote", base + ".docx");
  }
  // Everything in one document, each plan starting on a new page (new section).
  listInstance = 0;
  const all = files.map(section);
  fs.writeFileSync(path.join(OUT, "HS-LS1-6_all_teacher_plans.docx"), await Packer.toBuffer(buildDoc(all)));
  console.log("wrote HS-LS1-6_all_teacher_plans.docx");
})();
