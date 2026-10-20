"""Unit 2.1 teacher notebook answer key: the student notebook setup (print_unit21.py) filled in the way it should look
by the end of the unit. Vocabulary rows are filled, glue-in boxes say what the glued sheet should show, exit tickets
have a model answer, and every sketch is a black outline drawing that can be colored in. Ink saver: white background,
outlines only.

  python3 print_unit21_teacher_notebook.py      # writes Unit21_Teacher_Notebook_Key.pdf next to this file
"""

import html
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "HS-LS1-6" / "lessons"))
import print_notebook as PN  # noqa: E402
import print_unit21 as P  # noqa: E402

K = PN.K
INK = "#222"
S = f'stroke="{INK}" stroke-width="2" fill="#fff"'
T = 'font-family="Calibri, Carlito, Arial, sans-serif" fill="#222"'


def svg(w, h, body):
    return f'<svg viewBox="0 0 {w} {h}" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">{body}</svg>'


def label(x, y, text, size=13, anchor="start", bold=False):
    b = ' font-weight="700"' if bold else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}"{b} {T}>{html.escape(text)}</text>'


def arrow(x1, y1, x2, y2):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="2"/>'
            f'<polygon points="{x2},{y2} {x2 - 8},{y2 - 5} {x2 - 8},{y2 + 5}" fill="{INK}"/>')


# ---------------------------------------------------------------------------
# Drawings (outline only, to color in)
# ---------------------------------------------------------------------------
def helix(x, y, w, h, rungs=6, letters=None, bracket=None):
    """A simple DNA ladder (two wavy backbones, rectangle rungs to color)."""
    out, step = [], w / rungs
    top = " ".join(f"{x + i * step / 2:.1f},{y + (h * 0.15 if (i // 2) % 2 == 0 else 0):.1f}" for i in range(rungs * 2 + 1))
    bot = " ".join(f"{x + i * step / 2:.1f},{y + h - (h * 0.15 if (i // 2) % 2 == 0 else 0):.1f}" for i in range(rungs * 2 + 1))
    out.append(f'<polyline points="{top}" fill="none" stroke="{INK}" stroke-width="4"/>')
    out.append(f'<polyline points="{bot}" fill="none" stroke="{INK}" stroke-width="4"/>')
    for i in range(rungs):
        rx = x + step * (i + 0.5) - 6
        out.append(f'<rect x="{rx:.1f}" y="{y + h * 0.22:.1f}" width="12" height="{h * 0.27:.1f}" {S}/>')
        out.append(f'<rect x="{rx:.1f}" y="{y + h * 0.51:.1f}" width="12" height="{h * 0.27:.1f}" {S}/>')
        if letters:
            a, b = letters[i]
            out.append(label(rx + 6, y + h * 0.42, a, 11, "middle", True) + label(rx + 6, y + h * 0.71, b, 11, "middle", True))
    if bracket:
        i0, i1 = bracket
        bx0, bx1 = x + step * i0, x + step * i1
        out.append(f'<path d="M{bx0},{y - 6} v-8 H{bx1} v8" fill="none" stroke="{INK}" stroke-width="2"/>')
        out.append(label((bx0 + bx1) / 2, y - 20, "gene", 13, "middle", True))
    return "".join(out)


def protein_blob(cx, cy, r):
    pts = []
    import math
    for k in range(9):
        a = k / 9 * 6.283
        rr = r * (0.75 + 0.25 * ((k * 37) % 5) / 4)
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    beads = "".join(f'<circle cx="{cx - r * .55 + j * r * .28:.1f}" cy="{cy + (8 if j % 2 else -8):.1f}" r="{r * .14:.1f}" {S}/>'
                    for j in range(5))
    return f'<polygon points="{" ".join(pts)}" {S} stroke-linejoin="round"/>' + beads


def cat(x, y, s=1.0, notes=()):
    """A sitting Siamese cat outline. Points (face mask, ears, paws, tail) are separate shapes to color dark."""
    g = (f'<g transform="translate({x},{y}) scale({s})">'
         f'<path d="M60,200 C20,200 20,110 70,95 C100,88 130,95 140,130 C150,170 140,200 110,200 Z" {S}/>'  # body
         f'<path d="M135,185 C175,190 190,150 170,120 C160,105 175,95 182,105" fill="none" stroke="{INK}" stroke-width="2"/>'
         f'<path d="M168,118 C176,104 186,98 192,106 C188,112 180,116 172,124 Z" {S}/>'  # tail tip
         f'<circle cx="95" cy="70" r="42" {S}/>'  # head
         f'<polygon points="60,48 62,10 88,36" {S}/><polygon points="102,36 128,10 130,48" {S}/>'  # ears
         f'<path d="M75,62 C80,90 110,90 115,62 C108,80 82,80 75,62 Z" {S}/>'  # face mask
         f'<ellipse cx="80" cy="56" rx="5" ry="3" {S}/><ellipse cx="110" cy="56" rx="5" ry="3" {S}/>'
         f'<ellipse cx="70" cy="202" rx="18" ry="9" {S}/><ellipse cx="112" cy="202" rx="18" ry="9" {S}/>'  # paws
         "</g>")
    out = [g]
    for (tx, ty, px, py, text) in notes:
        out.append(f'<line x1="{tx}" y1="{ty}" x2="{x + px * s}" y2="{y + py * s}" stroke="{INK}" stroke-width="1" stroke-dasharray="3 3"/>')
        out.append(label(tx + 4, ty + 4, text, 12))
    return "".join(out)


def nucleotide(x, y, sc=1.0):
    return (f'<g transform="translate({x},{y}) scale({sc})"><circle cx="10" cy="20" r="10" {S}/>'
            f'<polygon points="30,8 46,2 58,14 52,32 34,32" {S}/><rect x="58" y="12" width="34" height="16" {S}/>'
            f'<line x1="20" y1="20" x2="32" y2="18" stroke="{INK}" stroke-width="2"/></g>')


def bead_chain(x, y, n, r=9, mark=None):
    out = []
    for i in range(n):
        cx = x + i * (2 * r + 6)
        if i:
            out.append(f'<line x1="{cx - r - 6}" y1="{y}" x2="{cx - r}" y2="{y}" stroke="{INK}" stroke-width="2"/>')
        thick = ' style="stroke-width:4"' if i == mark else ""
        out.append(f'<circle cx="{cx}" cy="{y}" r="{r}" {S}{thick}/>')
    return "".join(out)


def cell(x, y, w, h, dna=True, prot="circle", job=""):
    out = [f'<ellipse cx="{x + w / 2}" cy="{y + h / 2}" rx="{w / 2}" ry="{h / 2}" {S}/>',
           f'<circle cx="{x + w * .35}" cy="{y + h * .45}" r="{h * .2}" {S}/>']
    if dna:
        out.append(f'<path d="M{x + w * .28},{y + h * .38} q6,8 12,0 q6,-8 12,0 q6,8 12,0" fill="none" stroke="{INK}" stroke-width="2"/>')
    for k in range(3):
        px, py = x + w * (.62 + .1 * (k % 2)), y + h * (.3 + .2 * k)
        if prot == "circle":
            out.append(f'<circle cx="{px}" cy="{py}" r="7" {S}/>')
        else:
            out.append(f'<rect x="{px - 7}" y="{py - 7}" width="14" height="14" {S}/>')
    out.append(label(x + w / 2, y + h + 16, job, 12, "middle"))
    return "".join(out)


def thermometer(x, y):
    return (f'<rect x="{x}" y="{y}" width="14" height="80" rx="7" {S}/><circle cx="{x + 7}" cy="{y + 88}" r="12" {S}/>'
            f'<line x1="{x + 16}" y1="{y + 30}" x2="{x + 26}" y2="{y + 30}" stroke="{INK}" stroke-width="2"/>'
            + label(x + 30, y + 34, "33 °C", 11))


def flow(x, y, boxes, w=120, h=46, gap=26):
    out = []
    for i, t in enumerate(boxes):
        bx = x + i * (w + gap)
        out.append(f'<rect x="{bx}" y="{y}" width="{w}" height="{h}" rx="6" {S}/>')
        lines = t.split("|")
        for j, ln in enumerate(lines):
            out.append(label(bx + w / 2, y + h / 2 + 4 + (j - (len(lines) - 1) / 2) * 14, ln, 12, "middle"))
        if i:
            out.append(arrow(bx - gap + 2, y + h / 2, bx - 3, y + h / 2))
    return "".join(out)


# Small vocabulary icons (outline, colorable).
ICON = {
    "DNA": svg(110, 60, helix(8, 10, 94, 40, 4)),
    "gene": svg(110, 70, helix(8, 26, 94, 36, 4, bracket=(1, 3))),
    "protein": svg(80, 70, protein_blob(40, 36, 28)),
    "nucleotide": svg(100, 40, nucleotide(4, 2)),
    "base": svg(110, 60, f'<rect x="8" y="10" width="40" height="20" {S}/>{label(28, 25, "A", 12, "middle", True)}'
                 f'<rect x="56" y="10" width="40" height="20" {S}/>{label(76, 25, "T", 12, "middle", True)}'
                 f'<line x1="48" y1="20" x2="56" y2="20" stroke="{INK}" stroke-width="2"/>'
                 + label(52, 50, "A pairs with T", 10, "middle")),
    "double helix": svg(110, 60, helix(8, 10, 94, 40, 5)),
    "amino acid": svg(110, 40, bead_chain(14, 20, 4, mark=1)),
    "job": svg(110, 70, cell(10, 6, 90, 46, job="")),
    "claim": svg(110, 50, f'<rect x="8" y="8" width="94" height="34" rx="6" {S}/>{label(55, 30, "The answer", 12, "middle")}'),
    "evidence": svg(110, 50, f'<rect x="8" y="8" width="94" height="34" {S}/>{label(55, 30, "28 °C → dark", 12, "middle")}'),
    "reasoning": svg(110, 50, f'{label(8, 22, "because…", 12)}' + arrow(8, 34, 100, 34)),
}

# ---------------------------------------------------------------------------
# Filled pages
# ---------------------------------------------------------------------------
DAYS = {
    1: dict(
        vocab=[("DNA", "The molecule in every cell that stores the instructions for building proteins.", "A recipe book.", "The DNA in every cell of the cat."),
               ("gene", "A section of DNA with the instructions for one protein.", "One recipe in the book.", "The gene for the pigment-making protein."),
               ("protein", "A molecule built from amino acids that does a job for the cell.", "A worker or a machine.", "The protein that makes dark pigment.")],
        sketch=svg(620, 130, helix(30, 40, 220, 60, 6, bracket=(2, 4)) + arrow(265, 70, 330, 70) + protein_blob(385, 70, 38)
                   + arrow(435, 70, 495, 70) + cat(500, 8, 0.45)
                   + label(140, 122, "DNA", 15, "middle", True) + label(385, 122, "protein", 15, "middle", True)
                   + label(555, 122, "dark fur", 15, "middle", True)),
        sense=svg(620, 125, cat(20, 4, 0.55, notes=[(170, 14, 75, 20, "Ears 28 °C: dark"), (170, 36, 95, 75, "Face 30 °C: dark"),
                                                   (170, 58, 180, 110, "Tail tip 27 °C: dark"), (170, 80, 70, 202, "Paws 28 °C: dark"),
                                                   (170, 102, 100, 150, "Body 34–36 °C: cream")])
                  + label(360, 40, "Color the points dark.", 14, bold=True)
                  + label(360, 62, "Newborn kittens are white:", 13) + label(360, 80, "warm all over before birth.", 13)),
        exit="Dark fur grows on the cool parts of the cat (ears, face, paws, tail; 27–30 °C). The pattern is inherited from both "
             "parents, so it starts in the DNA: DNA → gene → protein → dark fur.",
        glue={"Left": "Circled ear (28), face (30), paw (28), tail tip (27) = C; back (36), belly (36), upper leg (34) = W. "
                      "Litters 1–2: Siamese × Siamese = all Siamese. Litters 3–4: solid parents had Siamese kittens, so genes come from both parents.",
              "Right": "Underlined DNA, gene, protein, chromosome. Arrow DNA → gene → protein. ? example: How can two solid parents have a Siamese kitten?"},
    ),
    2: dict(
        vocab=[("nucleotide", "One building block of DNA: a sugar, a phosphate, and a base.", "A link in a chain.", "One A nucleotide."),
               ("base", "The part of a nucleotide that is a letter: A, T, C, or G. A pairs with T, C with G.", "Letters of an alphabet.", "A–T, C–G."),
               ("double helix", "DNA's shape: two strands twisted like a ladder.", "A twisted ladder or spiral staircase.", "A DNA molecule.")],
        sketch=svg(620, 230, helix(40, 40, 420, 130, 6, letters=[("A", "T"), ("T", "A"), ("C", "G"), ("G", "C"), ("A", "T"), ("G", "C")])
                   + label(470, 50, "backbone: sugar + phosphate", 13, bold=True) + label(470, 110, "rungs: base pairs", 13, bold=True)
                   + label(470, 130, "A–T, C–G (4 colors)", 12) + nucleotide(470, 160, 1.2) + label(470, 215, "1 nucleotide", 12)),
        sense=svg(620, 230, cat(20, 10, 0.95) + f'<circle cx="390" cy="105" r="88" {S}/>' + helix(325, 75, 130, 50, 4)
                  + f'<line x1="140" y1="70" x2="304" y2="90" stroke="{INK}" stroke-width="1" stroke-dasharray="3 3"/>'
                  + label(300, 215, "Inside every cell: DNA. The order of the bases is the message.", 12)
                  + label(320, 160, "Siamese gene: one letter different", 12)),
        exit="DNA is a double helix made of nucleotides. Each nucleotide has a sugar, a phosphate, and a base. A pairs with T and "
             "C pairs with G. The order of the bases is the message.",
        glue={"Left": "Pentagon by sugar, circle by phosphate, rectangle by base. Boxed: A pairs with T. C pairs with G. "
                      "The cat sequences differ at the 4th letter (G vs. A)."},
    ),
    4: dict(
        vocab=[("base", "A DNA letter. Three bases in a row code for one amino acid.", "Three letters spell a word.", "GGA codes for Gly."),
               ("amino acid", "A small building block linked in a chain to make a protein.", "Beads on a necklace.", "Gly, Arg, Glu."),
               ("protein", "A folded chain of amino acids that does a job.", "A machine built from parts.", "The pigment-making protein.")],
        sketch=svg(620, 230, label(20, 40, "GGA → Gly", 16, bold=True) + label(20, 70, "AGA → Arg", 16, bold=True)
                   + label(20, 100, "(one letter changed)", 12) + bead_chain(200, 50, 6, mark=2) + label(200, 90, "amino acids link in order", 12)
                   + arrow(330, 120, 380, 160) + protein_blob(450, 160, 50) + label(450, 225, "protein (folds)", 13, "middle")),
        sense=svg(620, 230, cat(20, 10, 0.95, notes=[(260, 40, 75, 20, "GGA → AGA: Gly → Arg"),
                                                    (260, 90, 95, 75, "Pigment protein works only in cool skin"),
                                                    (260, 140, 180, 110, "Cool points → dark")])),
        exit="Not every change matters. One letter can change an amino acid (Siamese: Gly → Arg), stop a protein from being made, "
             "or change nothing (GAG and GAA both make Glu).",
        glue={"Left": "A = 1 (Gly → Arg); B = 3 (done); C = 1 (Leu → Pro); D = 3 (no gene); E = 2 (protein not made); F = 1 (Glu → Val)."},
    ),
    5: dict(
        vocab=[("gene", "A section of DNA for one protein. Every cell has every gene.", "Every student has the same textbook.", "The pigment gene is in every cat cell."),
               ("protein", "What a gene codes for. The proteins a cell makes decide its job.", "Tools in a toolbox.", "Pigment protein in pigment cells."),
               ("job", "The work a cell does, decided by the proteins it makes.", "A job at school.", "Nerve cells carry signals.")],
        sketch=svg(620, 230, cell(30, 30, 230, 130, prot="circle", job="Cell P: proteins 1, 2 → carries signals")
                   + cell(340, 30, 230, 130, prot="square", job="Cell Q: proteins 3, 4 → squeezes")
                   + label(310, 20, "same DNA (genes 1–4)", 14, "middle", True)),
        sense=svg(620, 230, cat(20, 10, 0.95, notes=[(270, 40, 75, 20, "Every cell has the pigment gene"),
                                                    (270, 80, 95, 75, "Only pigment cells use it"),
                                                    (270, 120, 180, 110, "Works below 33 °C → dark"),
                                                    (270, 160, 100, 150, "Body 34–36 °C → cream")]) + thermometer(560, 110)),
        exit="Only the cool parts are dark. Every cell has the pigment gene, but only pigment cells use it, and the changed "
             "protein works only below about 33 °C, so pigment is made only in the ears, nose, paws, and tail.",
        glue={"Left": "Highlighted: genes 1, 2, 3, 4 in both cells. Table: ear, nose, paw, tail tip = yes, dark; "
                      "upper leg, back, belly = no, cream."},
    ),
    6: dict(
        vocab=[("claim", "A one-sentence answer to the question.", "Your answer on a test.", "A one-letter change caused the dark points."),
               ("evidence", "Data, with numbers, that supports the claim.", "Proof.", "The ear is 28 °C and dark."),
               ("reasoning", "The science idea that links the evidence to the claim.", "Explaining why.", "One letter → one amino acid → protein works only in cool skin.")],
        sketch=svg(620, 230, flow(20, 20, ["Claim", "Evidence", "Reasoning"], w=170, h=50, gap=30)
                   + label(20, 110, "Claim: a one-letter change in the pigment gene.", 13)
                   + label(20, 135, "Evidence: ear 28 °C dark; back 36 °C cream.", 13)
                   + label(20, 160, "Reasoning: one amino acid changes, so the protein", 13)
                   + label(20, 180, "works only in cool skin; pigment only on cool parts.", 13)),
        sense=svg(620, 230, flow(10, 30, ["DNA change", "amino acid|change", "protein works|differently", "body|effect"], w=130, h=56, gap=22)
                  + label(10, 130, "Cat: one letter → Gly to Arg → works only in cool skin → dark points", 13)
                  + label(10, 160, "Case 2: one base → one amino acid → works poorly → symptoms", 13)),
        exit="One DNA letter changes one amino acid. The protein then works differently or poorly, and that changes the body "
             "(dark points in the cat, symptoms in Case 2).",
        glue={"Left": "Circled: “One letter different” / “One base changed.” Underlined: “One amino acid different.” "
                      "Boxed: dark points (cat) and “Yes” symptoms (Case 2)."},
    ),
    7: dict(
        vocab=[("DNA", "Stores the instructions for proteins.", "A recipe book.", "In every cell."),
               ("gene", "A section of DNA for one protein.", "One recipe.", "Pigment gene."),
               ("protein", "A chain of amino acids that does a job.", "A worker.", "Pigment protein."),
               ("amino acid", "A protein building block, set by 3 bases.", "A bead.", "Gly, Arg.")],
        sketch=svg(620, 230, helix(10, 70, 120, 60, 4) + arrow(140, 100, 175, 100) + helix(185, 70, 90, 60, 3, bracket=(0, 3))
                   + arrow(285, 100, 320, 100) + protein_blob(370, 100, 40) + arrow(420, 100, 455, 100) + cat(455, 20, 0.5)
                   + label(70, 165, "DNA", 14, "middle", True) + label(230, 165, "gene", 14, "middle", True)
                   + label(370, 165, "protein", 14, "middle", True) + label(510, 165, "trait", 14, "middle", True)),
        sense=svg(620, 230, cat(20, 10, 0.95, notes=[(260, 30, 75, 20, "DNA: same gene in every cell"),
                                                    (260, 65, 95, 75, "One letter changed (GGA → AGA)"),
                                                    (260, 100, 180, 110, "One amino acid: Gly → Arg"),
                                                    (260, 135, 70, 202, "Protein works only below 33 °C"),
                                                    (260, 170, 100, 150, "Cool points dark; warm body cream")])),
        exit="A Siamese cat's points are dark because one changed DNA letter swaps one amino acid in the pigment-making protein. "
             "That protein works only in skin cooler than about 33 °C, so pigment is made only on the cool ears, face, paws, and tail.",
        glue={"Left": "Circled: cool-room ear 26 °C, dark brown; warm-room ear 34 °C, light tan. All 5 model checkboxes checked."},
    ),
}

CSS = PN.CSS + """
.kv td { font-size: 8.5pt; line-height: 1.15; }
.kv td svg { display: block; max-height: .42in; }
.fill svg { display: block; }
.fill { border: 1px solid #888; padding: 2px 4px; margin: .02in 0 .06in; font-size: 9.5pt; overflow: hidden; }
.glue { border: 1.5px dashed #777; padding: 6px 8px; font-size: 10pt; margin: .02in 0 .06in; overflow: hidden; }
.glue b { display: block; font-size: 9pt; color: #555; letter-spacing: .04em; text-transform: uppercase; }
.ex { border-bottom: 1px solid #aaa; font-size: 11pt; line-height: .32in; font-style: italic; }
.keytag { font-weight: 700; letter-spacing: .08em; }
"""


def vocab_table(rows, row_h):
    head = "".join(f"<th>{html.escape(h)}</th>" for h in P.VOCAB_HEAD)
    cols = "".join(f'<col style="width:{w / sum(P.VOCAB_W) * 100:.1f}%">' for w in P.VOCAB_W)
    body = "".join(f'<tr><td style="height:{row_h:.2f}in"><b>{html.escape(w)}</b></td><td>{html.escape(d)}</td><td>{html.escape(c)}</td>'
                   f'<td>{html.escape(e)}</td><td style="padding:1px">{ICON.get(w, "")}</td></tr>' for w, d, c, e in rows)
    return f'<table class="kv"><colgroup>{cols}</colgroup><tr>{head}</tr>{body}</table>'


def box(h_in, inner):
    return f'<div class="fill" style="height:{h_in:.2f}in">{inner}</div>'


def glue_box(h_in, title, text):
    return f'<div class="glue" style="height:{h_in:.2f}in"><b>Glued in: {html.escape(title)}</b>{html.escape(text)}</div>'


def sheet(label, side, inner, title, focus=None):
    head = f'<div class="meta"><span>Unit 2.1 · {html.escape(label)} · <span class="keytag">TEACHER KEY</span></span><span>{side} page</span></div>'
    if side == "Left":
        head += f'<h1>{html.escape(title)}</h1><p class="focus"><b>Focus question:</b> {html.escape(focus)}</p>'
    else:
        head += f'<h1 style="font-size:18pt">{html.escape(title)} (continued)</h1>'
    return f'<section class="sheet"><div class="cut">{head}{inner}</div></section>'


def build():
    sheets = []
    for day, title, focus, words, h1, d1, h2, d2 in P.NOTEBOOK:
        k = DAYS[day]
        glue = {side: (lab, h) for side, lab, h in P.GLUE_INTO.get(day, [])}
        label = f"Day {day} · Vocabulary and SketchNotes"
        row_h = (1.8 if "Left" in glue else 5.9) / len(words)
        left = "<h2>Vocabulary</h2>" + vocab_table(k["vocab"], row_h)
        if "Left" in glue:
            lab, h = glue["Left"]
            left += f"<h2>Glue in: {html.escape(lab)}</h2>" + glue_box(h + 0.12, lab, k["glue"]["Left"])
        if "Right" in glue:
            sk, se, ex_lines = 1.0 * K, 0.95 * K, 2
        else:
            sk, se, ex_lines = 1.75 * K, 1.6 * K, 3
        right = (f"<h2>{html.escape(h1)}</h2>" + box(sk, k["sketch"]) + f"<h2>{html.escape(h2)}</h2>" + box(se, k["sense"])
                 + "<h2>Exit Ticket</h2>" + f'<div class="ex">{html.escape(k["exit"])}</div>')
        if "Right" in glue:
            lab, h = glue["Right"]
            right += f"<h2>Glue in: {html.escape(lab)}</h2>" + glue_box(h + 0.12, lab, k["glue"]["Right"])
        sheets.append(sheet(label, "Left", left, title, focus))
        sheets.append(sheet(label, "Right", right, title))
    return P.wrap(CSS, sheets)


if __name__ == "__main__":
    P.to_pdf(build(), HERE / "Unit21_Teacher_Notebook_Key.pdf")
