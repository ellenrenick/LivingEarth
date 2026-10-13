"""Printable teacher-notebook set-ups for Unit 1.3 (one PDF, two pages per lesson).

Each lesson's notebook slide (slide 2 of its deck) is a two-page spread. Here the
left half becomes one printed page and the right half the next, sized to cut out
and glue into a composition notebook (dashed cut line, 7 x 9.25 in). Ink saver:
white background everywhere, no filled table headers, only thin gray lines.

Layouts come from notebook_slides.DECKS (Lessons 5-7, Days 4 and 10) plus the
entries below, which were read from the live slides (Lessons 1-4, Day 9).

  python3 print_notebook.py [out.pdf]              # teacher copy
  python3 print_notebook.py --student [out.pdf]    # student copy: adds a name / period / date line
"""

import html
import subprocess
import sys
import tempfile
from pathlib import Path

import notebook_slides as NB

S = NB.DECKS
FONTS = Path(__file__).resolve().parent / "fonts"  # Google Fonts (OFL)
LESSONS = {
    "L1": dict(
        title="Phenomena: The Giant Pumpkin Mystery",
        focus="Where does a pumpkin's mass come from?",
        left=[("table", ["I notice…", "I wonder…"], [["", ""]], [2.2, 2.2], 10, 1.0),
              ("h", "Part 1: My initial model"), ("box", 1.6, "Draw where you think the pumpkin's mass comes from."),
              ("table", ["Source", "Soil", "Water", "Air", "Sunlight", "Fertilizer", "The seed"],
               [["My rank (before data)"] + [""] * 6, ["My rank (after data)"] + [""] * 6],
               [1.2, 0.5, 0.5, 0.45, 0.6, 0.65, 0.55], 8, 0.36)],
        right=[("h", "Part 2: What are these things made of?"), ("lines", 3),
               ("table", ["Element in the pumpkin", "Possible source(s)"],
                [["Carbon (C)", ""], ["Hydrogen (H)", ""], ["Oxygen (O)", ""], ["Nitrogen (N)", ""]], [1.15, 3.3], 9, 0.3),
               ("numbered", [4, 5]),
               ("h", "Part 3: Our questions"), ("lines", 3),
               ("h", "Exit ticket"), ("lines", 2)],
    ),
    "L2": dict(
        title="What Are Living Things Made Of?",
        focus="Which elements make up the molecules of life, and where could a plant get them?",
        left=[("h", "Warm-up"), ("lines", 2),
              ("h", "Part 1: The sealed-bag demo"),
              ("table", ["Step", "Mass (g)"],
               [["Sealed bag, before tipping the cup", ""], ["My prediction after tipping (up, down, or same?)", ""],
                ["Sealed bag, after tipping the cup", ""], ["After opening the bag", ""]], [3.4, 1.05], 9, 0.3),
              ("lines", 2),
              ("h", "Part 2: Reading a formula"),
              ("table", ["Formula", "C", "H", "O", "N", "Other"],
               [["CO₂ (carbon dioxide)"] + [""] * 5, ["H₂O (water)"] + [""] * 5, ["C₆H₁₂O₆ (glucose)"] + [""] * 5],
               [1.75, 0.45, 0.45, 0.45, 0.45, 0.9], 9, 0.3)],
        right=[("h", "Part 3: Who needs the soil?"),
               ("text", "Watch: Plants Need More Than C, H, and O (3 min). Then fill in the quick sort with a partner."),
               ("table", ["Molecule", "Formula", "Type of big molecule", "CO₂ + H₂O only? (Y/N)", "Extra element(s) from soil"],
                [["Glucose", "C₆H₁₂O₆", "", "", ""], ["Oleic acid", "C₁₈H₃₄O₂", "", "", ""], ["Valine", "C₅H₁₁NO₂", "", "", ""],
                 ["AMP", "C₁₀H₁₄N₅O₇P", "", "", ""], ["Challenge: chlorophyll a", "C₅₅H₇₂MgN₄O₅", "", "", ""]],
                [1.15, 1.0, 0.95, 0.65, 0.7], 9, 0.42),
               ("h", "Atom accounting rule"),
               ("text", "A plant can build ____________ from only CO₂ and water. To build ____________, "
                        "it also needs ____________ from the ____________."),
               ("h", "Exit ticket"), ("lines", 4)],
    ),
    "L3": dict(
        title="Building Sugar from Air and Water",
        focus="Where do the atoms in sugar come from, and what does light do?",
        left=[("h", "Warm-up"), ("lines", 2),
              ("h", "Part 1: A pumpkin leaf in a sealed chamber"), ("lines", 4),
              ("h", "Part 2: Build sugar with beads"),
              ("table", ["", "Black (C)", "White (H)", "Red (O)", "Total beads"],
               [["Before (6 CO₂ + 6 H₂O)", "", "", "", ""], ["After (1 glucose + 6 O₂)", "", "", "", ""]],
               [1.65, 0.68, 0.68, 0.68, 0.76], 9, 0.36),
              ("lines", 4)],
        right=[("h", "Part 3: Energy or matter?"),
               ("table", ["Item", "M or E", "Item", "M or E"],
                [["Sunlight", "", "Oxygen gas", ""], ["Carbon dioxide", "", "Heat given off by a leaf", ""],
                 ["Water", "", "Nitrogen in fertilizer", ""], ["Glucose", "", "Chlorophyll", ""]],
                [1.1, 0.8, 1.75, 0.8], 9, 0.32),
               ("h", "Exit ticket"), ("lines", 5)],
    ),
    "L4": dict(
        title="From Sugar to Amino Acids",
        focus="How can a plant turn sugar into amino acids?",
        left=[("h", "Warm-up"), ("lines", 2),
              ("h", "Part 1: The amino acid recipe"), ("box", 1.2, ""),
              ("h", "Part 2: Build amino acids"), ("box", 1.2, ""), ("lines", 2)],
        right=[("h", "Part 3: Make sense of the model"), ("box", 3.0, ""), ("lines", 5)],
    ),
    "D9": dict(
        title="Review: Sugar to Structures",
        focus="Which targets do I still need to work on before the CSA?",
        left=S["D9"]["left"],
        right=[("h", "Driving question"),
               ("text", "How does a plant build its body, and what is it built from? Use at least 4 vocabulary words."),
               ("lines", 4),
               ("h", "My assigned CFA reviews"),
               ("text", "Reviews open for me: ______   Done (check off): ______"),
               ("lines", 3)],
    ),
}
ORDER = [("L1", "Day 1 · Lesson 1"), ("L2", "Day 2 · Lesson 2"), ("L3", "Day 3 · Lesson 3"), ("D5", "Day 4 · Vocabulary"),
         ("L4", "Day 5 · Lesson 4"), ("L6", "Day 6 · Lesson 6"), ("L5", "Day 7 · Lesson 5"), ("L7", "Day 8 · Lesson 7"),
         ("D9", "Day 9 · Interventions and Review"), ("D10", "Day 10 · CSA")]

K = 1.45  # slide inches -> printed inches (4.45 in half-slide -> about 6.45 in)

CSS = """
@page { size: letter; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; background: #fff; color: #222; font-family: Calibri, Carlito, Arial, sans-serif; }
.sheet { width: 8.5in; height: 11in; padding: 0.875in 0.75in; page-break-after: always; }
.sheet:last-child { page-break-after: auto; }
.cut { width: 7in; height: 9.25in; border: 1.5px dashed #999; padding: 0.25in; display: flex; flex-direction: column; }
.meta { display: flex; justify-content: space-between; font-size: 9pt; color: #777; letter-spacing: .04em; text-transform: uppercase; }
h1 { font-family: Boogaloo, sans-serif; font-weight: 400; font-size: 26pt; margin: .04in 0 .02in; color: #222; }
.focus { font-size: 12pt; margin: 0 0 .06in; }
h2 { font-family: Handlee, cursive; font-size: 15pt; margin: .1in 0 .03in; }
table { border-collapse: collapse; width: 100%; table-layout: fixed; margin: .02in 0 .06in; }
th, td { border: 1px solid #888; padding: 2px 5px; text-align: left; vertical-align: top; }
th { font-weight: 700; border-bottom: 2px solid #444; }
.lines div { border-bottom: 1px solid #aaa; height: .32in; }
.box { border: 1px solid #888; padding: 4px 6px; font-size: 9.5pt; color: #666; margin: .02in 0 .06in; }
.text { font-size: 11pt; margin: .04in 0; }
.cut > * { flex: 0 0 auto; }
.cut > .grow { flex: 1 1 0; min-height: 0; overflow: hidden; }
.lines.grow { display: flex; flex-direction: column; }
.lines.grow div { flex: 0 0 .34in; }
.name { font-size: 11pt; margin: .08in 0 0; }
.foot { font-size: 8.5pt; color: #888; margin-top: .06in; }
"""


def block(b):
    k = b[0]
    if k == "h":
        return f"<h2>{html.escape(b[1])}</h2>"
    if k == "lines":
        return '<div class="lines">' + "<div></div>" * b[1] + "</div>"
    if k == "numbered":
        return '<div class="lines">' + "".join(f"<div>{n}.</div>" for n in b[1]) + "</div>"
    if k == "text":
        return f'<p class="text">{html.escape(b[1])}</p>'
    if k == "box":
        return f'<div class="box" style="height:{b[1] * K:.2f}in">{html.escape(b[2])}</div>'
    if k == "table":
        _, head, rows, widths, fs, min_h = b
        tot = sum(widths)
        cols = "".join(f'<col style="width:{w / tot * 100:.1f}%">' for w in widths)
        fs_p = min(fs * 1.3, 12)
        h = max(min_h or 0, 0.11 + fs * 0.0175) * K
        th = "".join(f"<th>{html.escape(c)}</th>" for c in head)
        trs = "".join("<tr>" + "".join(f'<td style="height:{h:.2f}in">{html.escape(c)}</td>' for c in r) + "</tr>"
                      for r in rows)
        return f'<table style="font-size:{fs_p:.1f}pt"><colgroup>{cols}</colgroup><tr>{th}</tr>{trs}</table>'
    raise ValueError(k)


def page(d, label, side, blocks, student=False):
    parts = [b for b in blocks]
    # Let the last write-in area stretch to the bottom of the page.
    body = [block(b) for b in parts]
    if parts and parts[-1][0] == "lines":
        n = max(parts[-1][1], 2)
        body[-1] = '<div class="lines grow">' + "<div></div>" * (n + 12) + "</div>"
    else:
        body.append('<div class="grow"></div>')
    head = f'<div class="meta"><span>Unit 1.3 · {html.escape(label)}</span><span>{side} page</span></div>'
    if student:
        head += '<div class="name">Name ______________________________   Period ______   Date ____________</div>'
    if side == "Left":
        head += f'<h1>{html.escape(d["title"])}</h1><p class="focus"><b>Focus question:</b> {html.escape(d["focus"])}</p>'
    else:
        head += f'<h1 style="font-size:18pt">{html.escape(d["title"])} (continued)</h1>'
    return f'<section class="sheet"><div class="cut">{head}{"".join(body)}</div></section>'


def build_html(student=False):
    sheets = []
    for key, label in ORDER:
        d = LESSONS.get(key) or S[key]
        sheets.append(page(d, label, "Left", d["left"], student))
        if d["right"]:
            sheets.append(page(d, label, "Right", d["right"], student))
    fonts = "".join(f"@font-face {{ font-family: {f}; src: url('{(FONTS / (f + '.woff2')).as_uri()}'); }}\n"
                    for f in ("Boogaloo", "Handlee"))
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{fonts}{CSS}</style></head><body>{"".join(sheets)}</body></html>'


def main(out, student=False):
    tmp = Path(tempfile.mkdtemp()) / "notebook.html"
    tmp.write_text(build_html(student))
    subprocess.run(["/opt/pw-browsers/chromium", "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    "--virtual-time-budget=10000", f"--print-to-pdf={Path(out).resolve()}", tmp.as_uri()],
                   check=True, stderr=subprocess.DEVNULL)
    print(out)


if __name__ == "__main__":
    student = "--student" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--student"]
    main(args[0] if args else ("unit13_student_notebook.pdf" if student else "unit13_teacher_notebook.pdf"), student)
