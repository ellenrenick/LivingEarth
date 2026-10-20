"""Unit 2.1 printables (ink saver): one PDF of everything students glue in, annotate, or use on paper, and a student
notebook setup for the whole unit in the same format as the Unit 1.3 notebook (print_notebook.py).

The notebook pages match each deck's notebook slide (slide 2): a vocabulary table on the left page; SketchNotes,
Sensemaking, and the exit ticket on the right. Day 3 (lab) and Day 8 (CSA) have no notebook slide.

  python3 print_unit21.py            # writes Unit21_Printables.pdf and Unit21_Student_Notebook.pdf next to this file
"""

import html
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "HS-LS1-6" / "lessons"))
import print_notebook as PN  # noqa: E402
import revise_40min as R  # noqa: E402

# ---------------------------------------------------------------------------
# Student notebook (read from the notebook slides, Oct 2026)
# ---------------------------------------------------------------------------
VOCAB_HEAD = ["Word", "Definition (my words)", "This reminds me of… (connections)", "Example", "Drawing"]
VOCAB_W = [0.91, 0.99, 0.98, 0.77, 0.62]
NOTEBOOK = [  # (day, title, focus, words, sketch heading, sketch prompt, sensemaking heading, sensemaking prompt)
    (1, "The Siamese Cat Mystery", "Why are a Siamese cat's ears, paws, and tail dark?", ["DNA", "gene", "protein"],
     "SketchNotes: DNA to Proteins", "Draw DNA, a gene, and a protein with a short label and a simple icon for each. No full sentences.",
     "Sensemaking: The Siamese Cat Path", "Draw the cat. Add one idea about why its ears, paws, and tail are dark. Keep adding after each lesson."),
    (2, "What Is DNA Made Of?", "What is DNA made of?", ["nucleotide", "base", "double helix"],
     "SketchNotes: DNA Structure", "Sketch the DNA ladder. Label the backbone and the four bases (A, T, C, G). Use color, not sentences.",
     "Sensemaking: The Siamese Cat Path", "Add what you learned about DNA's structure to your cat drawing."),
    (4, "What Can One Letter Do?", "Does every change in DNA matter?", ["base", "amino acid", "protein"],
     "SketchNotes: Bases to Amino Acids", "Show how a 3-base code picks an amino acid and how amino acids link into a protein.",
     "Sensemaking: The Siamese Cat Path", "Add how one changed base could change a protein, then keep adding after each lesson."),
    (5, "Same DNA, Different Jobs", "Why are only some parts of a Siamese cat dark?", ["gene", "protein", "job"],
     "SketchNotes: Same DNA, Different Jobs", "Draw two cells with the same DNA but different proteins and different jobs.",
     "Sensemaking: The Siamese Cat Path", "Add why only the ears, paws, and tail are dark."),
    (6, "Case Data", "How can one DNA letter change the body?", ["claim", "evidence", "reasoning"],
     "SketchNotes: Claim, Evidence, Reasoning", "Write your claim, list or draw the data that backs it, then the reasoning that links them.",
     "Sensemaking: The Case Path", "Add how one DNA change can change the body."),
    (7, "Review and Back to the Cat", "Why are a Siamese cat's points dark?", ["DNA", "gene", "protein", "amino acid"],
     "SketchNotes: DNA to Trait", "Sketch the whole path from DNA to gene to protein to what you see.",
     "Sensemaking: The Siamese Cat Path", "Finish your cat path with every step from DNA to dark fur."),
]


def notebook_html():
    sheets = []
    for day, title, focus, words, h1, d1, h2, d2 in NOTEBOOK:
        d = {"title": title, "focus": focus}
        row_h = 5.9 / (len(words) * PN.K)  # rows fill the left page
        left = [("h", "Vocabulary"), ("table", VOCAB_HEAD, [[w, "", "", "", ""] for w in words], VOCAB_W, 9, row_h)]
        right = [("h", h1), ("box", 1.75, d1), ("h", h2), ("box", 1.6, d2), ("h", "Exit Ticket"), ("lines", 3)]
        label = f"Day {day} · Vocabulary and SketchNotes"
        sheets.append(PN.page(d, label, "Left", left, student=True, unit="Unit 2.1"))
        sheets.append(PN.page(d, label, "Right", right, student=True, unit="Unit 2.1"))
    return wrap(PN.CSS, sheets)


# ---------------------------------------------------------------------------
# Printables
# ---------------------------------------------------------------------------
CSS = PN.CSS + """
.sheet.halves { display: flex; flex-direction: column; gap: .25in; padding: .4in .75in; }
.half { width: 7in; height: 4.95in; border: 1.5px dashed #999; padding: .18in .22in; overflow: hidden; }
.full { width: 7in; min-height: 9.6in; border: 1.5px dashed #999; padding: .2in .25in; }
.sheet.long { height: auto; padding: .45in .75in; }
.half h3, .full h3 { font-family: Handlee, cursive; font-size: 13pt; margin: .06in 0 .02in; }
.half p, .full p, .half li, .full li { font-size: 10.5pt; margin: .03in 0; }
.half table, .full table { font-size: 10pt; table-layout: auto; }
.half th, .full th { border-bottom: 2px solid #444; }
.tag { font-size: 8.5pt; color: #666; letter-spacing: .05em; text-transform: uppercase; }
.do { font-size: 10pt; border: 1px solid #888; padding: 3px 6px; margin: .05in 0; }
.labsheet { width: 7in; } .labsheet h3 { font-family: Handlee, cursive; font-size: 13pt; margin: .08in 0 .02in; } .labsheet p, .labsheet li { font-size: 11pt; margin: .04in 0; }
.title2 { font-family: Boogaloo, sans-serif; font-size: 19pt; margin: 0; }
.contents td, .contents th { font-size: 10.5pt; padding: 4px 6px; }
"""


def ink(s):
    """Strip the page colors from the Canvas HTML (ink saver)."""
    return (s.replace('style="border:1px solid #999;padding:6px"', 'class="do"')
             .replace('style="border:2px solid #2e7d32;padding:6px"', 'class="do"')
             .replace(' border="1" cellpadding="6"', ""))


def half(day, title, use, body):
    return (f'<div class="half"><div class="tag">Unit 2.1 · Day {day} · {html.escape(use)}</div>'
            f'<p class="title2">{html.escape(title)}</p>{ink(body)}</div>')


PIECES = [  # (day, title, use, copies, body)
    (1, "Siamese cat data", "Glue in · annotate", "1 per student",
     "<p class=\"do\">Circle the 4 dark body parts. Write W next to the warm parts and C next to the cool parts.</p>"
     "<h3>Data 1: Temperature and fur color</h3>" + R.TEMPS + "<h3>Data 2: Litters of kittens</h3>" + R.LITTERS),
    (1, "Reading: DNA, genes, and chromosomes", "Glue in · annotate", "1 per student",
     "<p class=\"do\">Annotate: underline each key word the first time you see it (DNA, gene, protein, chromosome). "
     "Draw an arrow from DNA to gene to protein. Put a ? next to one thing you still wonder.</p>"
     "<p>Every cell in a cat stores instructions in <strong>DNA</strong>. A <strong>gene</strong> is a section of DNA with the "
     "instructions for one <strong>protein</strong>. Proteins do the jobs of the cell, like making the dark pigment in fur.</p>"
     "<p>DNA is packed into <strong>chromosomes</strong>. A chromosome is one long DNA molecule packed with proteins, and it "
     "holds many genes. A kitten gets one set of chromosomes, and so one set of genes, from each parent. That is why two "
     "solid-colored parents can still have a Siamese kitten: each parent can pass on a changed copy of the gene.</p>"
     "<p><strong>Big question:</strong> How can a difference in DNA change which parts of a cat are dark?</p>"),
    (2, "Reading: What is DNA made of?", "Glue in · annotate", "1 per student",
     "<p class=\"do\">Annotate: draw the shape next to each part (pentagon = sugar, circle = phosphate, rectangle = base). "
     "Box the base-pairing rule.</p>"
     "<p>DNA is a <strong>double helix</strong>, shaped like a twisted ladder. It is built from <strong>nucleotides</strong>. "
     "Each nucleotide has three parts: a <strong>sugar</strong>, a <strong>phosphate</strong>, and a <strong>base</strong>.</p>"
     "<p>The sugars and phosphates make the sides of the ladder (the backbone). The bases make the rungs. There are four "
     "bases: A, T, C, and G. <strong>A pairs with T. C pairs with G.</strong></p>"
     "<p>The order of the bases is the message. A cat's DNA has billions of bases, and a gene is one stretch of them.</p>"
     "<p>Solid cat: &nbsp; A T G G G A C T G T T T<br>Siamese cat: A T G A G A C T G T T T &nbsp; "
     "<em>(made-up letters that show the idea)</em></p>"),
    (3, "Base key and code table", "Lab table card", "1 per pair",
     "<p class=\"do\">Keep this card on your lab tray. Read the copy three letters at a time.</p>"
     "<p>Red = A &nbsp; Yellow = T &nbsp; Green = C &nbsp; Orange = G</p>"
     "<table><tbody><tr><th>DNA triplet</th><th>Amino acid</th><th>DNA triplet</th><th>Amino acid</th></tr>"
     "<tr><td>ATG</td><td>Met</td><td>AGA</td><td>Arg</td></tr><tr><td>GGA</td><td>Gly</td><td>CTG</td><td>Leu</td></tr>"
     "<tr><td>TTT</td><td>Phe</td><td>GAC</td><td>Asp</td></tr></tbody></table>"
     "<p><strong>Pairing rule:</strong> A with T, C with G.</p>"),
    (4, "Card sort: what can one letter do?", "Glue in · write on it", "1 per student",
     "<p class=\"do\">For each card, write 1, 2, or 3 and a reason. Card B is done for you. "
     "1 = changes an amino acid · 2 = changes whether the protein is made · 3 = no noticeable change</p>"
     + R.CODE_D4 + R.bank(["The amino acid changes from ___ to ___.", "The amino acid stays the same.", "The protein is not made.",
                          "No gene is involved."]).replace("Word bank", "Reason bank")
     + R.tbl([["Card", "What changed", "1, 2, or 3", "Reason"],
              ["A", "Siamese cat: GGA becomes AGA in the pigment gene.", "", ""],
              ["B", "GAG becomes GAA.", "3", "The amino acid stays the same."],
              ["C", "CTG becomes CCG.", "", ""],
              ["D", "A change in DNA with no gene and no switch.", "", ""],
              ["E", "A change in a gene's switch, so the gene is never turned on.", "", ""],
              ["F", "Human gene: GAG becomes GTG.", "", ""]])),
    (5, "Same DNA, different jobs", "Glue in · write on it", "1 per student",
     "<p class=\"do\">Highlight what is the same in cells P and Q. Then fill in the temperature table. We do the ear together.</p>"
     "<h3>Two kinds of cells</h3>" + R.CELLS + "<h3>Where does the changed protein work? (cooler than 33 °C)</h3>" + R.WORKS),
    (6, "Case data", "Glue in · annotate", "1 per student",
     "<p class=\"do\">In each case, circle the DNA change, underline the protein change, and box the effect on the body.</p>"
     "<h3>Case 1: Siamese and solid cats</h3>" + R.CASE1 + "<h3>Case 2: A human gene</h3>" + R.CASE2),
    (7, "Write It: two Siamese kittens", "Glue in · annotate", "1 per student",
     "<p class=\"do\">Circle the two numbers you will use as evidence. Then check off each part of your model as you add it.</p>"
     "<p>Two Siamese kittens are raised from birth, one in a warm room and one in a cool room. At 12 weeks:</p>" + R.KITTENS +
     "<h3>Model checklist</h3><p>☐ DNA with the gene &nbsp; ☐ the one-letter change &nbsp; ☐ the amino acid chain with one "
     "amino acid different &nbsp; ☐ the protein working only in cool skin &nbsp; ☐ the dark points</p>"),
]


def lab_sheet():
    s = (HERE / "lab_sheet.html").read_text()
    return f'<section class="sheet long"><div class="labsheet"><div class="tag">Unit 2.1 · Day 3 · Lab sheet · 1 per pair</div>{ink(s)}</div></section>'


def printables_html():
    rows = "".join(f"<tr><td>Day {d}</td><td>{html.escape(t)}</td><td>{html.escape(u)}</td><td>{html.escape(c)}</td></tr>"
                   for d, t, u, c, _ in PIECES)
    rows += "<tr><td>Day 3</td><td>Gummy DNA lab sheet</td><td>Lab sheet (full page)</td><td>1 per pair</td></tr>"
    cover = ('<section class="sheet"><div class="full"><p class="title2">Unit 2.1 Printables: DNA to Proteins</p>'
             "<p>Everything students glue in, annotate, or use on paper, in day order. Each half-sheet is sized to cut on the "
             "dashed line and glue into a composition notebook. Print on white paper, black ink only.</p>"
             '<table class="contents"><tbody><tr><th>Day</th><th>Printable</th><th>Use</th><th>Copies</th></tr>'
             f"{rows}</tbody></table>"
             "<p>Days 2 and 8 need nothing else on paper. The notebook setups for each lesson are in "
             "Unit21_Student_Notebook.pdf.</p></div></section>")
    halves = [half(d, t, u, b) for d, t, u, c, b in PIECES]
    sheets = [cover]
    # Day order with the lab sheet after the Day 3 card.
    day3 = next(i for i, p in enumerate(PIECES) if p[0] == 3)
    before, after = halves[:day3 + 1], halves[day3 + 1:]
    for grp in (before, after):
        for i in range(0, len(grp), 2):
            sheets.append('<section class="sheet halves">' + "".join(grp[i:i + 2]) + "</section>")
        if grp is before:
            sheets.append(lab_sheet())
    return wrap(CSS, sheets)


def wrap(css, sheets):
    fonts = "".join(f"@font-face {{ font-family: {f}; src: url('{(PN.FONTS / (f + '.woff2')).as_uri()}'); }}\n"
                    for f in ("Boogaloo", "Handlee"))
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{fonts}{css}</style></head><body>{"".join(sheets)}</body></html>'


def to_pdf(doc, out):
    tmp = Path(tempfile.mkdtemp()) / "page.html"
    tmp.write_text(doc)
    subprocess.run(["/opt/pw-browsers/chromium", "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    "--virtual-time-budget=10000", f"--print-to-pdf={out}", tmp.as_uri()], check=True, stderr=subprocess.DEVNULL)
    print(out)


if __name__ == "__main__":
    to_pdf(printables_html(), HERE / "Unit21_Printables.pdf")
    to_pdf(notebook_html(), HERE / "Unit21_Student_Notebook.pdf")
