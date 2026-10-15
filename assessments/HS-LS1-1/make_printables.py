"""Printable materials for the 8-day unit 2.1 (Siamese cats).

Writes printables/Unit_2.1_Printables.pdf (every worksheet, tape-in table, and cut-out card) and
printables/Unit_2.1_Student_Notebook.pdf (one open-notebook spread per lesson, laid out like the notebook set up slide
in the unit 1.3 lesson decks: title across the top, focus question, Warm-up, Parts 1-3, numbered lines).
Usage: python3 make_printables.py   (needs Chromium, set CHROME to override)
"""
import os
import subprocess
from pathlib import Path

import lessons_8day as L

OUT = Path(__file__).parent / "printables"
CHROME = os.environ.get("CHROME", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")


# ---- student notebook: one lesson = two portrait pages (LEFT PAGE / RIGHT PAGE), same layout as the unit 1.3 student notebook ----
def lines(n):
    return '<div class="ln">' + "<div></div>" * n + "</div>"


def box(h, hint=""):
    return f'<div class="bx" style="height:{h}in">{f"<span>{hint}</span>" if hint else ""}</div>'


def tbl(head, rows, widths=None, rh=0.42, bold_first=False):
    w = "".join(f'<col style="width:{x}%">' for x in widths) if widths else ""
    th = "".join(f"<th>{h}</th>" for h in head)
    body = "".join("<tr style=\"height:%sin\">" % rh + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="gt"><colgroup>{w}</colgroup><tr>{th}</tr>{body}</table>'


def p(text):
    return f'<p class="tx">{text}</p>'


def hh(text):
    return f'<div class="hd">{text}</div>'


BLANK = ["&nbsp;"] * 1
NOTEBOOK = [
    {"day": 1, "title": "Phenomena: The Siamese Cat Mystery", "fq": "How can a difference in DNA change which parts of a cat are dark?",
     "left": [tbl(["I notice…", "I wonder…"], [[""]], [50, 50], rh=1.55), hh("Part 1: My initial model"), box(2.9, "Draw what is inside a Siamese cat's cells that leads to dark ears, paws, and tail."),
              hh("Part 2: Key ideas"), lines(4)],
     "right": [hh("Part 3: Temperature and fur color"), tbl(["Body part", "Skin temp (°C)", "Fur color"], [[x, "", ""] for x in ["Back", "Belly", "Upper leg", "Ear", "Nose and face", "Paw", "Tail tip"]], [40, 30, 30], rh=0.32),
               p("Pattern: dark fur goes with ______________ skin."), hh("Part 4: Litters of kittens"),
               tbl(["Parents", "What kittens did they have?"], [["Siamese × Siamese", ""], ["Siamese × solid", ""], ["Solid × solid", ""]], [32, 68], rh=0.5),
               hh("Exit ticket"), lines(4)]},
    {"day": 2, "title": "What Is DNA Made Of?", "fq": "What is DNA built from, and what is the message?",
     "left": [hh("Warm-up"), box(1.5, "Sketch what you think DNA looks like."), hh("Part 1: One nucleotide"), box(2.2, "Draw and label the sugar, phosphate, and base."),
              hh("Part 2: Words to know"), tbl(["Word", "In my words"], [["double helix", ""], ["nucleotide", ""], ["backbone", ""], ["base pair", ""]], [30, 70], rh=0.5)],
     "right": [hh("Part 3: Partner strands"), tbl(["Strand", "Partner strand"], [["A T G C C T", ""], ["T T T G A C", ""], ["C T G G G A", ""]], [40, 60], rh=0.5),
               p("The order of the bases is the ______________________."), hh("Part 4: One letter apart"),
               p("Solid cat: A T G <u>G</u> G A C T G T T T<br>Siamese cat: A T G <u>A</u> G A C T G T T T"), p("How many letters differ? Where?"), lines(3),
               hh("Exit ticket"), lines(5)]},
    {"day": 3, "title": "Build, Copy, and Read a Gene", "fq": "How does a gene's message become a chain of amino acids?",
     "left": [hh("Warm-up"), p("In my own words, what does “copy, then read” mean?"), lines(3), hh("Part 1: Lab record"),
              tbl(["Step", "What I built (letters or colors)"], [["A: Template strand", ""], ["B: Partner strand", ""], ["C: The copy", ""], ["C: Amino acid chain", ""]], [34, 66], rh=0.62),
              p("Which strand carries the “coding” letters? How do you know?"), lines(3)],
     "right": [hh("Part 2: Change one letter"), tbl(["Step", "What I found"], [["Changed template", ""], ["New copy", ""], ["New amino acid chain", ""]], [34, 66], rh=0.6),
               p("How many amino acids changed? Which one?"), lines(2), hh("Part 3: Connect to the cat"),
               p("What did one letter do to the chain? Name two ways the gummy model is different from real DNA."), lines(4), hh("Exit ticket"), lines(4)]},
    {"day": 4, "title": "What Can One Letter Do?", "fq": "What can a one-letter change in DNA do?",
     "left": [hh("Warm-up"), lines(2), hh("Part 1: Three things a one-letter change can do"),
              tbl(["Category", "What it means", "Cards"], [["1", "Changes an amino acid in the chain", ""], ["2", "Changes whether or when the protein is made", ""], ["3", "No noticeable change", ""]], [14, 56, 30], rh=0.62),
              hh("Part 2: Card sort"), tbl(["Card", "Category", "My reason"], [[x, "", ""] for x in "ABCDEF"], [12, 18, 70], rh=0.5)],
     "right": [hh("Part 3: The Siamese cat"), tbl(["DNA", "Amino acid", "Protein", "Fur"], [[""]], [25, 25, 25, 25], rh=0.9),
               p("How does this explain the dark points and the white newborn?"), lines(4),
               p("Claim check: “Every change in DNA changes how a cell works.” Use the cards to respond."), lines(4), hh("Exit ticket"), lines(5)]},
    {"day": 5, "title": "Same DNA, Different Jobs", "fq": "If all cells have the same DNA, why do cells have different jobs?",
     "left": [hh("Warm-up"), lines(2), hh("Part 1: Two kinds of cells"),
              tbl(["Cell", "Genes in cell", "Proteins made", "Job"], [["P", "1, 2, 3, 4", "1 and 2", "Carries signals"], ["Q", "1, 2, 3, 4", "3 and 4", "Squeezes to move the body"]], [12, 24, 24, 40], rh=0.5),
              p("Same DNA? Why different jobs?"), lines(3), hh("Part 2: Cells in a Siamese cat's ear"),
              tbl(["Cell type", "Has the gene?", "Makes protein X?", "Job"], [["Pigment-making cell", "", "", "Makes dark color"], ["Skin cell", "", "", "Covers and protects"], ["Nerve cell", "", "", "Carries signals"]], [28, 20, 22, 30], rh=0.55)],
     "right": [hh("Part 3: Where does the changed protein work?"), p("Works only in skin cooler than about 33 °C (a simplified number)."),
               tbl(["Body part", "Skin temp (°C)", "Protein works?", "Fur color"], [[a, b, "", ""] for a, b in [("Ear", 28), ("Nose", 30), ("Paw", 28), ("Tail tip", 27), ("Upper leg", 34), ("Back", 36), ("Belly", 36)]], [28, 24, 24, 24], rh=0.34),
               p("Explain it with the words DNA, gene, protein, and job."), lines(5), hh("Exit ticket"), lines(4)]},
    {"day": 6, "title": "Case Data", "fq": "How does a DNA change lead to an effect on the body?",
     "left": [hh("Warm-up"), p("The chain for the cat: one-letter DNA change → ______ → ______ → ______"), lines(2), hh("Part 1: Case 1, Siamese and solid cats"),
              tbl(["", "Solid cat", "Siamese cat"], [["Gene", "", ""], ["Amino acid chain", "", ""], ["Where the protein works", "", ""], ["Fur color", "", ""]], [30, 35, 35], rh=0.55),
              hh("Part 2: Case 2, a human gene"), tbl(["Person", "Gene", "Protein", "Symptoms"], [["1", "", "", ""], ["2", "", "", ""]], [14, 24, 36, 26], rh=0.55),
              p("The chain for Case 2: ______ → ______ → ______ → ______")],
     "right": [hh("Part 3: Compare the cases"), tbl(["How they are alike", "How they are different"], [[""]], [50, 50], rh=1.5),
               hh("Part 4: Claim, evidence, reasoning"), p("<b>Claim:</b> what caused the Siamese cat's dark points?"), lines(2), p("<b>Evidence:</b> at least two numbers from the data."), lines(2),
               p("<b>Reasoning:</b> how does a one-letter DNA change lead to dark color only on the cooler body parts?"), lines(4), hh("Exit ticket"), lines(3)]},
    {"day": 7, "title": "Review and Back to the Cat", "fq": "How can I explain the Siamese cat with DNA, genes, and proteins?",
     "left": [hh("Warm-up: My CFA scores"), tbl(["CFA", "My score", "Review done?"], [[x, "", ""] for x in ["LS1-1.1", "LS1-1.2", "LS1-1.3", "LS1-1.4", "LS1-1.5", "LS1-1.6"]], [30, 30, 40], rh=0.38),
              hh("Part 1: Vocabulary"), tbl(["Word", "In my words"], [[x, ""] for x in ["DNA", "nucleotide", "gene", "base sequence", "amino acid", "protein"]], [28, 72], rh=0.5)],
     "right": [hh("Part 2: My revised model"), box(2.7, "Show the gene, the one-letter change, the copy-then-read path, the amino acid chain, the protein, and the dark points."),
               hh("Part 3: Write It, two Siamese kittens"), p("Why are the cool-room kitten's ears darker?"), lines(9)]},
    {"day": 8, "title": "Unit Assessment and Reflection", "fq": "What do I know about how DNA leads to traits?",
     "left": [hh("Warm-up: Before the test"), p("Three things I am sure about:"), lines(4), hh("Part 1: Back to the cat"), box(2.9, "What I would add to my Day 1 model now."),
              hh("Part 2: Looking back at my CFAs"), tbl(["CFA", "My score", "What helped me"], [[x, "", ""] for x in ["LS1-1.1", "LS1-1.2", "LS1-1.3"]], [24, 22, 54], rh=0.4)],
     "right": [tbl(["CFA", "My score", "What helped me"], [[x, "", ""] for x in ["LS1-1.4", "LS1-1.5", "LS1-1.6"]], [24, 22, 54], rh=0.4),
               hh("Part 3: What I will do next time"), lines(6), hh("Exit ticket"), p("One question I still have about DNA and proteins:"), lines(4)]},
]

CSS_COMMON = """
@page { size: letter %s; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Liberation Sans', Arial, sans-serif; color: #1c1c1c; }
table { border-collapse: collapse; } td, th { border: 1px solid #555; padding: 4px 8px; font-size: 11pt; }
th { background: #eef2f7; }
"""

NB_CSS = CSS_COMMON % "portrait" + """
.sheet { width: 8.5in; height: 11in; padding: 0.8in 0.78in; page-break-after: always; }
.frame { width: 100%; height: 100%; border: 1px dashed #888; padding: 0.28in 0.28in 0.1in; overflow: hidden; }
.top { display: flex; justify-content: space-between; font-size: 8.5pt; color: #777; letter-spacing: 0.4px; }
.nm { font-size: 10.5pt; margin-top: 3px; }
.ti { font-family: 'Inter Display','Inter',sans-serif; font-weight: 800; font-size: 22pt; margin-top: 6px; line-height: 1.1; } .ti.sm { font-size: 17pt; }
.fqq { font-size: 10.5pt; margin: 2px 0 6px; }
.hd { font-family: 'Inter',sans-serif; font-weight: 600; font-size: 13pt; margin: 12px 0 6px; }
.tx { font-size: 10pt; margin: 4px 0; line-height: 1.35; }
.gt { width: 100%; border: 1px solid #777; margin: 3px 0; } .gt th { text-align: left; font-size: 10.5pt; background: none; border: 1px solid #777; border-bottom: 2px solid #333; padding: 3px 6px; }
.gt td { border: 1px solid #aaa; vertical-align: top; font-size: 10pt; padding: 3px 6px; }
.bx { border: 1px solid #777; margin: 4px 0; padding: 4px 8px; } .bx span { font-size: 9pt; color: #777; }
.ln div { border-bottom: 1px solid #aaa; height: 0.31in; }
"""

PR_CSS = CSS_COMMON % "portrait" + """
.pg { width: 8.5in; height: 11in; padding: 0.55in 0.6in; page-break-after: always; position: relative; }
h1 { font-size: 22pt; margin: 0 0 4px; color: #1f3a5f; } h2 { font-size: 15pt; margin: 12px 0 6px; color: #1f3a5f; } h3 { font-size: 12.5pt; margin: 10px 0 4px; }
.day { display: inline-block; background: #1f3a5f; color: #fff; padding: 2px 10px; border-radius: 3px; font-size: 10pt; margin-bottom: 6px; }
p, li { font-size: 11pt; line-height: 1.4; } .note { font-size: 9.5pt; color: #666; font-style: italic; }
.cut { border: 2px dashed #888; padding: 10px 14px; margin: 10px 0; border-radius: 6px; } .cut .lab { font-size: 9pt; color: #888; margin: -22px 0 6px; background: #fff; display: inline-block; padding: 0 6px; position: relative; top: -2px; }
.cards { display: grid; grid-template-columns: 1fr 1fr; gap: 0; } .card { border: 2px dashed #888; padding: 14px; height: 2.1in; } .card b { font-size: 24pt; color: #1f3a5f; display: block; } .card p { font-size: 12.5pt; margin: 4px 0; }
.mat td { width: 0.55in; height: 0.6in; text-align: center; font-size: 14pt; } .mat { margin: 6px 0 14px; }
.cat { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; } .cat div { border: 2px solid #555; height: 2.3in; padding: 6px; font-size: 11pt; } 
.lines div { border-bottom: 1px solid #666; height: 0.32in; }
.box { border: 2px solid #555; padding: 8px; min-height: 1.6in; margin: 6px 0; }
"""


def notebook_page(n):
    out = []
    for side, label, cont in (("left", "LEFT PAGE", ""), ("right", "RIGHT PAGE", " (continued)")):
        title = f'<div class="ti{" sm" if cont else ""}">{n["title"]}{cont}</div>'
        fq = '' if cont else f'<div class="fqq"><b>Focus question:</b> {n["fq"]}</div>'
        out.append(f'<div class="sheet"><div class="frame"><div class="top"><span>UNIT 2.1 &middot; DAY {n["day"]} &middot; LESSON {n["day"]}</span><span>{label}</span></div>'
                   f'<div class="nm">Name ______________________________ Period ______ Date ____________</div>{title}{fq}{"".join(n[side])}</div></div>')
    return "".join(out)


def clean(html):
    return html.replace("{{SLIDES}}", "").replace("{{VOCAB}}", "").replace("{{VOCAB_KEY}}", "")


def printables_html():
    P = []
    pg = lambda body: P.append(f'<div class="pg">{body}</div>')
    pg('<h1>Unit 2.1 Printables</h1><p><b>DNA to Proteins (HS-LS1-1) &middot; 8-day version: Siamese Cats</b></p>'
       '<table><tr><th>Day</th><th>Print</th><th>Copies</th></tr>'
       '<tr><td>1</td><td>Day 1 worksheet (data tables and questions)</td><td>1 per student</td></tr>'
       '<tr><td>2</td><td>Day 2 worksheet</td><td>1 per student</td></tr>'
       '<tr><td>3</td><td>Gummy DNA lab sheet; strand mat and base key; code table</td><td>1 per student; 1 mat set per pair</td></tr>'
       '<tr><td>4</td><td>Code table and card sort (cards A to F, three category mats)</td><td>1 set per group</td></tr>'
       '<tr><td>5</td><td>Day 5 worksheet</td><td>1 per student</td></tr>'
       '<tr><td>6</td><td>Day 6 case data worksheet</td><td>1 per student</td></tr>'
       '<tr><td>7</td><td>Vocabulary and Write It page</td><td>1 per student</td></tr>'
       '<tr><td>All</td><td>Student notebook spreads (separate file: Unit_2.1_Student_Notebook.pdf)</td><td>1 per lesson, or have students copy the layout</td></tr></table>'
       '<h2>Lab materials checklist (Day 3, per pair)</h2><ul><li>2 licorice strands (6 to 8 inches)</li><li>24 candy bases: 6 red (A), 6 yellow (T), 6 green (C), 6 orange (G), plus a few spare</li>'
       '<li>Toothpicks, a paper plate, the printed lab sheet and code table</li><li>No food? Use colored beads and pipe cleaners, or colored paper circles</li></ul>'
       '<p class="note">Tape-in tables are sized to fit half of a notebook page. Cut on the dashed lines.</p>')
    # Day 1
    pg('<span class="day">Day 1</span>' + clean(L.DAY1_STUDENT).split("<h3>Key ideas</h3>")[0].replace("<h3>Data 1", '<h3>Data 1') + "")
    pg('<span class="day">Day 1</span><h1>Tape-in tables</h1><p class="note">Cut out and tape into your notebook.</p>'
       '<div class="cut"><div class="lab">Data 1: Temperature and fur color</div>' + L.TEMPS + '</div>'
       '<div class="cut"><div class="lab">Data 2: Litters of kittens</div>' + L.LITTERS + '</div>'
       '<div class="cut"><div class="lab">Key ideas</div><ul><li><b>DNA</b> in every cell stores instructions.</li><li>A <b>gene</b> is a section of DNA with the instructions for one <b>protein</b>.</li>'
       '<li><b>Proteins</b> do jobs for the cell.</li><li>A kitten gets one set of chromosomes from each parent.</li></ul></div>')
    pg('<span class="day">Day 1</span>' + "<h3>Key ideas and practice</h3>" + clean(L.DAY1_STUDENT).split("<h3>Key ideas</h3>")[1].replace("<h3>Practice</h3>", "<h3>Practice</h3>"))
    # Day 2
    pg('<span class="day">Day 2</span>' + clean(L.DAY2_STUDENT))
    # Day 3
    pg('<span class="day">Day 3</span>' + clean(L.LAB_STUDENT).split("<h3>Part C")[0])
    pg('<span class="day">Day 3</span>' + "<h3>Part C" + clean(L.LAB_STUDENT).split("<h3>Part C")[1])
    mat = '<table class="mat"><tr>' + "".join("<td></td>" for _ in range(12)) + "</tr></table>"
    pg('<span class="day">Day 3</span><h1>Gummy DNA mats</h1><p class="note">Slide the licorice strand along the mat. One base per box, three boxes per amino acid.</p>'
       '<div class="cut"><div class="lab">Base key</div><p><b>Red = A &nbsp; Yellow = T &nbsp; Green = C &nbsp; Orange = G</b></p></div>'
       '<div class="cut"><div class="lab">Part A and B: template strand (T A C &nbsp;C C T &nbsp;G A C &nbsp;A A A) and partner strand</div><p>Template</p>' + mat + '<p>Partner</p>' + mat + '</div>'
       '<div class="cut"><div class="lab">Part C: the copy</div>' + mat + '<p>Amino acids: ______ &ndash; ______ &ndash; ______ &ndash; ______</p></div>'
       '<div class="cut"><div class="lab">Part D: changed template (T A C &nbsp;T C T &nbsp;G A C &nbsp;A A A) and its copy</div>' + mat + mat + '<p>Amino acids: ______ &ndash; ______ &ndash; ______ &ndash; ______</p></div>'
       '<div class="cut"><div class="lab">Code table (tape in)</div>' + L.CODE_TABLE + '</div>')
    # Day 4
    cards = [("A", "In a Siamese cat, one letter changes in the gene for a pigment-making protein: GGA becomes AGA."), ("B", "A gene's triplet changes from GAG to GAA."),
             ("C", "A gene's triplet changes from CTG to CCG."), ("D", "One letter changes in a stretch of DNA that has no gene and no switch."),
             ("E", "One letter changes in a switch next to a gene so the gene can never be turned on, and its protein is not made."), ("F", "In a human gene, GAG becomes GTG.")]
    pg('<span class="day">Day 4</span><h1>Card sort</h1><p class="note">Cut on the dashed lines. Sort into three categories and write your reason on the back.</p><div class="cards">'
       + "".join(f"<div class='card'><b>{k}</b><p>{t}</p></div>" for k, t in cards) + '</div>')
    pg('<span class="day">Day 4</span><h1>Category mats and code table</h1><div class="cat"><div><b>Category 1</b><br>Changes an amino acid in the chain</div><div><b>Category 2</b><br>Changes whether or when the protein is made</div>'
       '<div><b>Category 3</b><br>No noticeable change</div></div><h3>Code table</h3>' + L.CODE_TABLE_D4 + '<h3>Questions</h3><ol><li>Write the cards in each category and your reasons.</li>'
       '<li>A student says, "Every change in DNA changes how a cell works." Use the cards to respond.</li><li>Card A changes one amino acid. Predict what could happen to the protein and to the fur color. (Hint: think about temperature.)</li></ol><div class="lines">'
       + "<div></div>" * 6 + "</div>")
    # Day 5, 6
    pg('<span class="day">Day 5</span>' + clean(L.DAY5_STUDENT))
    pg('<span class="day">Day 6</span>' + clean(L.DAY6_STUDENT))
    # Day 7
    pg('<span class="day">Day 7</span><h1>Vocabulary and Write It</h1><h3>Vocabulary</h3><p><b>Word bank:</b> DNA, nucleotide, gene, base sequence, amino acid, protein</p><ol>'
       '<li>The molecule that stores the instructions for building proteins is ____________.</li><li>One building block of DNA, with a sugar, a phosphate, and a base, is a ____________.</li>'
       '<li>A section of DNA with the instructions for one protein is a ____________.</li><li>The order of A, T, C, and G along a strand of DNA is its ____________.</li>'
       '<li>A chain of ____________ is folded to make a protein.</li><li>A ____________ does jobs for the cell.</li></ol>'
       '<h3>Write It: two Siamese kittens</h3><table><tr><th></th><th>Kitten raised warm</th><th>Kitten raised cool</th></tr><tr><td>Ear skin temperature (&deg;C)</td><td>34</td><td>26</td></tr>'
       '<tr><td>Ear fur color</td><td>Light tan</td><td>Dark brown</td></tr><tr><td>Back skin temperature (&deg;C)</td><td>36</td><td>35</td></tr><tr><td>Back fur color</td><td>Cream</td><td>Cream</td></tr></table>'
       '<p><b>Claim:</b> why are the cool-room kitten\'s ears darker? <b>Evidence:</b> at least two numbers. <b>Reasoning:</b> DNA, gene, protein, and what the amino acid change does.</p>'
       '<div class="lines">' + "<div></div>" * 12 + "</div>")
    return f'<html><head><meta charset="utf-8"><style>{PR_CSS}</style></head><body>{"".join(P)}</body></html>'


def to_pdf(html, name):
    OUT.mkdir(exist_ok=True)
    src = OUT / f"{name}.html"
    src.write_text(html, encoding="utf-8")
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", f"--print-to-pdf={OUT / (name + '.pdf')}", "--no-pdf-header-footer", src.as_uri()],
                   check=True, capture_output=True)
    src.unlink()


def main():
    nb = "".join(notebook_page(n) for n in NOTEBOOK)
    to_pdf(f'<html><head><meta charset="utf-8"><style>{NB_CSS}</style></head><body>{nb}</body></html>', "Unit_2.1_Student_Notebook")
    to_pdf(printables_html(), "Unit_2.1_Printables")
    print("done")


if __name__ == "__main__":
    main()
