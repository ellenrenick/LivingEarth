"""Unit 2.1 printables (ink saver): one PDF of everything students glue in, annotate, or use on paper, and a student
notebook setup for the whole unit in the same format as the Unit 1.3 notebook (print_notebook.py).

The notebook pages match each deck's notebook slide (slide 2): a vocabulary table on the left page; SketchNotes,
Sensemaking, and the exit ticket on the right. Day 3 (lab) and Day 8 (CSA) have no notebook slide.

  python3 print_unit21.py   # writes Unit21_Printables.pdf, Unit21_Printables_Teacher_Key.pdf, Unit21_Student_Notebook.pdf here

Each glue-in is sized to fit the "Glue in" box on that day's notebook page (6.3 x 4.2 in; the Day 1 reading is a
6.3 x 2.6 in strip on the Day 1 right page).
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
        glue = {side: (label, h) for side, label, h in GLUE_INTO.get(day, [])}
        # Vocabulary rows share what the glue-in box leaves on the left page.
        row_h = (1.8 if "Left" in glue else 5.9) / (len(words) * PN.K)
        left = [("h", "Vocabulary"), ("table", VOCAB_HEAD, [[w, "", "", "", ""] for w in words], VOCAB_W, 9, row_h)]
        if "Left" in glue:
            label, h = glue["Left"]
            left += [("h", f"Glue in: {label}"), ("box", (h + 0.12) / PN.K, f"Glue the Day {day} “{label}” half-sheet here.")]
        if "Right" in glue:
            label, h = glue["Right"]
            right = [("h", h1), ("box", 1.0, d1), ("h", h2), ("box", 0.95, d2), ("h", "Exit Ticket"), ("lines", 2),
                     ("h", f"Glue in: {label}"), ("box", (h + 0.12) / PN.K, f"Glue the Day {day} “{label}” strip here.")]
        else:
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
.half { width: 6.3in; height: 4.2in; border: 1.5px dashed #999; padding: .1in .16in; overflow: hidden; }
.half.strip { height: 2.6in; }
.half .tight table { font-size: 8pt; margin: 0; } .half .tight td, .half .tight th { padding: 0 4px; } .half .tight p { font-size: 8pt; margin: 0; } .half .tight h3 { margin: .02in 0 0; }
.half td, .half th { padding: 1px 4px; }
.full { width: 7in; min-height: 9.6in; border: 1.5px dashed #999; padding: .2in .25in; }
.sheet.long { height: auto; padding: .45in .75in; }
.half h3, .full h3 { font-family: Handlee, cursive; font-size: 11.5pt; margin: .04in 0 .01in; }
.full h3 { font-size: 13pt; }
.half p, .half li { font-size: 9.5pt; margin: .02in 0; }
.full p, .full li { font-size: 10.5pt; margin: .03in 0; }
.half table { font-size: 9pt; table-layout: auto; margin: .01in 0 .03in; }
.full table { font-size: 10pt; table-layout: auto; }
.half .title2 { font-size: 15pt; }
.half .do { font-size: 9pt; padding: 2px 5px; margin: .03in 0; }
.key { border: 2px solid #444; padding: 6px 10px; margin: .1in 0; font-size: 10.5pt; }
.key b.k { letter-spacing: .06em; }
.ans { font-style: italic; font-weight: 700; }
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


def half(day, title, use, body, cls="half"):
    return (f'<div class="{cls}"><div class="tag">Unit 2.1 · Day {day} · {html.escape(use)}</div>'
            f'<p class="title2">{html.escape(title)}</p>{ink(body)}</div>')


PIECES = [  # (day, title, use, copies, body)
    (1, "Siamese cat data", "Glue in · annotate", "1 per student",
     "<p class=\"do\">Circle the 4 dark body parts. Write W next to the warm parts and C next to the cool parts.</p>"
     "<div class=\"tight\"><h3>Data 1: Temperature and fur color</h3>" + R.TEMPS + "<h3>Data 2: Litters of kittens</h3>" + R.LITTERS + "</div>"),
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


STRIPS = {1}  # the Day 1 reading is a short strip (6.3 x 2.6 in); every other glue-in is 6.3 x 4.2 in
# Where each glue-in goes in the notebook setup: day -> [(page side, label, height in inches)]
GLUE_INTO = {1: [("Left", "Siamese cat data", 4.2), ("Right", "Reading: DNA, genes, and chromosomes", 2.6)],
             2: [("Left", "Reading: What is DNA made of?", 4.2)], 4: [("Left", "Card sort", 4.2)],
             5: [("Left", "Same DNA, different jobs", 4.2)], 6: [("Left", "Case data", 4.2)],
             7: [("Left", "Write It: two Siamese kittens", 4.2)]}


def lab_sheet():
    s = (HERE / "lab_sheet.html").read_text()
    return f'<section class="sheet long"><div class="labsheet"><div class="tag">Unit 2.1 · Day 3 · Lab sheet · 1 per pair</div>{ink(s)}</div></section>'


def printables_html():
    rows = "".join(f"<tr><td>Day {d}</td><td>{html.escape(t)}</td><td>{html.escape(u)}</td><td>{html.escape(c)}</td></tr>"
                   for d, t, u, c, _ in PIECES)
    rows += "<tr><td>Day 3</td><td>Gummy DNA lab sheet</td><td>Lab sheet (full page)</td><td>1 per pair</td></tr>"
    cover = ('<section class="sheet"><div class="full"><p class="title2">Unit 2.1 Printables: DNA to Proteins</p>'
             "<p>Everything students glue in, annotate, or use on paper, in day order. Cut each sheet on the dashed line and "
             "glue it into the matching “Glue in” box on that day's notebook setup page (Unit21_Student_Notebook.pdf). "
             "Print on white paper, black ink only. Answers: Unit21_Printables_Teacher_Key.pdf.</p>"
             '<table class="contents"><tbody><tr><th>Day</th><th>Printable</th><th>Use</th><th>Copies</th></tr>'
             f"{rows}</tbody></table>"
             "<p>Days 2 and 8 need nothing else on paper. The notebook setups for each lesson are in "
             "Unit21_Student_Notebook.pdf.</p></div></section>")
    halves = [half(d, t, u, b, "half strip" if i in STRIPS else "half") for i, (d, t, u, c, b) in enumerate(PIECES)]
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


# ---------------------------------------------------------------------------
# Teacher answer key (one printable per page, answers in a bordered box; filled tables where students write in cells)
# ---------------------------------------------------------------------------
A = lambda t: f'<span class="ans">{t}</span>'
CARDS_KEY = R.tbl([["Card", "What changed", "1, 2, or 3", "Reason"],
                   ["A", "Siamese cat: GGA becomes AGA in the pigment gene.", A("1"), A("The amino acid changes from Gly to Arg.")],
                   ["B", "GAG becomes GAA.", "3", "The amino acid stays the same."],
                   ["C", "CTG becomes CCG.", A("1"), A("The amino acid changes from Leu to Pro.")],
                   ["D", "A change in DNA with no gene and no switch.", A("3"), A("No gene is involved.")],
                   ["E", "A change in a gene's switch, so the gene is never turned on.", A("2"), A("The protein is not made.")],
                   ["F", "Human gene: GAG becomes GTG.", A("1"), A("The amino acid changes from Glu to Val (as in sickle cell).")]])
WORKS_KEY = R.tbl([["Body part", "Skin temperature (&deg;C)", "Cooler than 33 &deg;C? Protein works?", "Fur color"]]
                  + [[b, t, A("yes") if int(t) < 33 else A("no"), A("dark") if int(t) < 33 else A("cream")]
                     for b, t in (("Ear", "28"), ("Nose", "30"), ("Paw", "28"), ("Tail tip", "27"), ("Upper leg", "34"),
                                  ("Back", "36"), ("Belly", "36"))])
KEYS = [  # same order as PIECES
    ("<b>Circle:</b> ear (28 &deg;C), nose and face mask (30), paw (28), tail tip (27): all dark brown, all marked <b>C</b> (cool). "
     "Back (36), belly (36), upper leg (34): cream, marked <b>W</b> (warm).<br><b>Litters:</b> two Siamese-pattern parents had only "
     "Siamese-pattern kittens (5 of 5 and 4 of 4). Two solid parents can still have Siamese kittens (litters 3 and 4: 1 and 2), "
     "so a kitten gets genes from both parents.", None),
    ("<b>Underline:</b> DNA, gene, protein, chromosome (first use of each). <b>Arrow:</b> DNA &rarr; gene &rarr; protein (&rarr; job, "
     "such as pigment). <b>?:</b> any honest question; good ones ask how two solid parents can have a Siamese kitten, or what the "
     "changed gene does.", None),
    ("<b>Shapes:</b> pentagon next to sugar, circle next to phosphate, rectangle next to base. <b>Box:</b> “A pairs with T. C pairs "
     "with G.” The two cat sequences differ at one letter: the 4th (G in the solid cat, A in the Siamese cat).", None),
    ("Reference card; nothing to fill in. Lab answers are on the lab sheet key page.", None),
    ("Card B is the worked example. Category 1 = A, C, F; category 2 = E; category 3 = B, D.", CARDS_KEY),
    ("<b>Highlight:</b> both cells have genes 1, 2, 3, 4 (the same DNA). They make different proteins (1 and 2 vs. 3 and 4), "
     "so they have different jobs.", WORKS_KEY),
    ("<b>Case 1:</b> circle “One letter different”; underline “One amino acid different”; box “Dark ears, nose, paws, tail; cream "
     "body” (protein works only in skin cooler than about 33 &deg;C). <b>Case 2:</b> circle “One base changed”; underline “One "
     "amino acid different; works poorly”; box “Yes” (symptoms).", None),
    ("<b>Circle:</b> ear 26 &deg;C, dark brown (cool room) and ear 34 &deg;C, light tan (warm room). Backs 36 and 35 &deg;C are "
     "cream in both. <b>Model checklist:</b> all 5 boxes should be checked on the revised model.", None),
]
LAB_KEY = ("<ul><li><b>Part A</b> colors in order: yellow, red, green, green, green, yellow, orange, red, green, red, red, red.</li>"
           "<li><b>Part B</b> partner strand: A T G G G A C T G T T T. The partner strand carries the coding letters; it matches the "
           "copy the cell makes from the template.</li>"
           "<li><b>Part C</b> copy: A T G G G A C T G T T T. Chain: <b>Met – Gly – Leu – Phe</b>. The gene's message is copied from "
           "the template strand, and the copy is read three letters at a time to link amino acids in order.</li>"
           "<li><b>Part D</b>: the changed template TAC TCT GAC AAA gives the copy ATG AGA CTG TTT: <b>Met – Arg – Leu – Phe</b>. "
           "One amino acid changed (the second, Gly to Arg). Yes, a different chain can make a protein that works differently.</li>"
           "<li><b>Connect</b>: (1) one amino acid in the chain changed, so the protein could work differently (in the Siamese cat it "
           "stops working at warm temperatures). (2) Accept: candy, not molecules; far bigger than real DNA; real genes are "
           "thousands of bases long; real strands twist into a helix.</li>"
           "<li><b>Scoring:</b> out of 12 (Part A 1, Part B 2, Part C 4, Part D 3, Connect 2), divided by 3 for the 4-point score.</li></ul>")


def key_html():
    sheets = ['<section class="sheet"><div class="full"><p class="title2">Unit 2.1 Printables: Teacher Answer Key</p>'
              "<p>One printable per page, in the same order as the student printables. Answers are in the bordered KEY box; "
              "where students write in a table, the table is shown filled in (answers in bold italic).</p></div></section>"]
    for (d, t, u, c, body), (note, filled) in zip(PIECES, KEYS):
        shown = body
        if filled:  # replace the student table (the last table on the sheet) with the filled one
            i = shown.rfind("<table")
            shown = shown[:i] + filled
        sheets.append(f'<section class="sheet"><div class="full"><div class="tag">Unit 2.1 · Day {d} · {html.escape(u)} · KEY</div>'
                      f'<p class="title2">{html.escape(t)}</p>{ink(shown)}<div class="key"><b class="k">KEY</b> {note}</div></div></section>')
    sheets.append('<section class="sheet"><div class="full"><div class="tag">Unit 2.1 · Day 3 · Lab sheet · KEY</div>'
                  f'<p class="title2">Gummy DNA Lab: Build, Copy, and Read a Gene</p><div class="key"><b class="k">KEY</b>{LAB_KEY}</div>'
                  "</div></section>")
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
    to_pdf(key_html(), HERE / "Unit21_Printables_Teacher_Key.pdf")
