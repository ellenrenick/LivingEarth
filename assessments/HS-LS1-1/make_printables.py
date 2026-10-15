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

NOTEBOOK = [
    # (day label, title, focus question, [left sections: warm-up, part 1, part 2], part 3, tape-in notes {section index: text})
    ("Day 1", "The Siamese Cat Mystery", "How can a difference in DNA change which parts of a cat are dark?",
     ["Warm-up: Notice and wonder", "Part 1: Data 1, temperature and fur color", "Part 2: Data 2, litters of kittens"],
     "Part 3: Key ideas and my first model", {1: "tape the temperature table here", 2: "tape the litter table here"}),
    ("Day 2", "What Is DNA Made Of?", "What is DNA built from, and what is the message?",
     ["Warm-up: What does DNA look like?", "Part 1: One nucleotide", "Part 2: Base pairing, write the partner strands"],
     "Part 3: One letter apart", {}),
    ("Day 3", "Build, Copy, and Read a Gene", "How does a gene's message become a chain of amino acids?",
     ["Warm-up: Copy, then read", "Part 1: Base key and code table", "Part 2: Lab, build the gene, copy it, read it"],
     "Part 3: Change one letter, then connect to the cat", {1: "tape the code table here"}),
    ("Day 4", "What Can One Letter Do?", "What can a one-letter change in DNA do?",
     ["Warm-up: What changed in Part D?", "Part 1: Three things a one-letter change can do", "Part 2: Card sort, cards A to F"],
     "Part 3: The Siamese cat, one amino acid different", {2: "glue the sorted cards here"}),
    ("Day 5", "Same DNA, Different Jobs", "If all cells have the same DNA, why do cells have different jobs?",
     ["Warm-up: Skin cells and nerve cells", "Part 1: Two kinds of cells", "Part 2: Cells in a Siamese cat's ear"],
     "Part 3: Where does the changed protein work?", {1: "tape the cell table here"}),
    ("Day 6", "Case Data", "How does a DNA change lead to an effect on the body?",
     ["Warm-up: The chain for the cat", "Part 1: Case 1, Siamese and solid cats", "Part 2: Case 2, a human gene"],
     "Part 3: Claim, evidence, reasoning", {1: "tape the case table here"}),
    ("Day 7", "Review and Back to the Cat", "How can I explain the Siamese cat with DNA, genes, and proteins?",
     ["Warm-up: My CFA scores and my reviews", "Part 1: Vocabulary", "Part 2: My revised model"],
     "Part 3: Write It, two Siamese kittens", {}),
    ("Day 8", "Unit Assessment and Reflection", "What do I know about how DNA leads to traits?",
     ["Warm-up: Before the test", "Part 1: Back to the cat, what I would add", "Part 2: Looking back at my CFAs"],
     "Part 3: What I will do next time", {}),
]

CSS_COMMON = """
@page { size: letter %s; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Liberation Sans', Arial, sans-serif; color: #1c1c1c; }
table { border-collapse: collapse; } td, th { border: 1px solid #555; padding: 4px 8px; font-size: 11pt; }
th { background: #eef2f7; }
"""

NB_CSS = CSS_COMMON % "landscape" + """
.sheet { width: 11in; height: 8.5in; padding: 0.22in; page-break-after: always; position: relative; }
.nb { width: 100%; height: 100%; border: 7px solid #d8a98b; border-radius: 0.55in; background: #fffdf9; position: relative; overflow: hidden; }
.spine { position: absolute; left: 50%; top: 0; bottom: 0; border-left: 2px solid #222; }
.page { position: absolute; top: 0; bottom: 0; width: 50%; padding: 0.12in 0.35in 0.1in 0.38in;
  background-image: repeating-linear-gradient(to bottom, transparent 0, transparent 0.285in, #9aa6e6 0.285in, #9aa6e6 0.3in); background-position: 0 0.52in; }
.page.l { left: 0; } .page.r { left: 50%; }
.title { position: absolute; left: 0; right: 0; top: 0.08in; text-align: center; font-family: 'Inter Display','Inter',sans-serif; font-weight: 900; font-size: 30pt; letter-spacing: 0.5px; z-index: 3; }
.tag { position: absolute; top: 0.12in; font-size: 9pt; color: #777; z-index: 3; }
.fq { background: #00e5ff; display: inline-block; padding: 0 5px; font-size: 11pt; line-height: 0.3in; margin-top: 0.55in; }
.sec { margin-top: 0; }
.h { display: inline-block; font-family: 'Inter',sans-serif; font-weight: 600; font-size: 13pt; color: #24402f; border-bottom: 2px solid #24402f; background: #fffdf9; line-height: 0.27in; padding: 0 4px; }
.tape { position: absolute; right: 0.4in; border: 1.5px dashed #999; background: rgba(255,255,255,0.8); color: #888; font-size: 8.5pt; font-style: italic; padding: 2px 10px; }
.nums { position: absolute; left: 0.35in; right: 0.35in; bottom: 0.12in; }
.nums div { height: 0.3in; line-height: 0.3in; font-size: 10pt; color: #555; position: relative; }
.nums div span { display: inline-block; width: 0.3in; } .nums div i { position: absolute; left: 0.3in; right: 0; bottom: 0.03in; border-bottom: 1px solid #5560b8; }
.nums .cap { font-size: 8.5pt; font-style: italic; color: #777; height: 0.22in; line-height: 0.22in; background: #fffdf9; display: inline-block; padding: 0 4px; }
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


def notebook_page(day, title, fq, left, part3, tapes):
    def sec(i, text, h_in):
        tape = f'<div class="tape" style="margin-top:-0.02in">{tapes[i]}</div>' if i in tapes else ""
        return f'<div class="sec" style="height:{h_in}in"><span class="h">{text}</span>{tape}</div>'
    leftp = (f'<div class="page l"><span class="fq"><b>Focus question:</b> {fq}</span>'
             f'{sec(0, left[0], 1.15)}{sec(1, left[1], 2.0)}{sec(2, left[2], 2.4)}'
             '<div class="nums"><div class="cap">Questions I still have</div><div><span>1.</span><i></i></div><div><span>2.</span><i></i></div></div></div>')
    rows = "".join(f"<div><span>{i}.</span><i></i></div>" for i in range(1, 6))
    rightp = (f'<div class="page r"><div style="height:0.55in"></div><span class="h">{part3}</span>'
              f'<div class="nums" style="bottom:0.12in"><div class="cap">Five things I learned today</div>{rows}</div></div>')
    return (f'<div class="sheet"><div class="nb"><div class="title">{title}</div><div class="tag" style="left:0.4in">Unit 2.1 &middot; {day}</div>'
            f'<div class="tag" style="right:0.4in">Name ____________  Period ___</div>{leftp}{rightp}<div class="spine"></div></div></div>')


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
    nb = "".join(notebook_page(*n) for n in NOTEBOOK)
    to_pdf(f'<html><head><meta charset="utf-8"><style>{NB_CSS}</style></head><body>{nb}</body></html>', "Unit_2.1_Student_Notebook")
    to_pdf(printables_html(), "Unit_2.1_Printables")
    print("done")


if __name__ == "__main__":
    main()
