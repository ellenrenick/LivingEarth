"""Unit 2.2 printables (ink saver): everything students glue into their notebooks, a teacher answer key, and the student
notebook setup for the whole unit, in the same format as Unit 2.1 (HS-LS1-1/print_unit21.py).

A table whose information students only copy from a slide, or that they fill in, is a glue-in: it is printed here so
nobody spends class time drawing it. Each glue-in is 6.3 in wide and sized to fit the dashed "Glue in" box on that day's
notebook page (the page in Unit22_Student_Notebook.pdf and the notebook slide are laid out from the same blocks).

  python3 printables.py   # writes Unit22_Printables.pdf, Unit22_Printables_Teacher_Key.pdf, Unit22_Student_Notebook.pdf in ..

PIECES is also read by nbslide.py (the notebook slides) and slides.py (the "glue in" line on each content slide).
"""

import html
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent
sys.path.insert(0, str(HERE.parent.parent / "HS-LS1-6" / "lessons"))
sys.path.insert(0, str(HERE.parent.parent / "HS-LS1-1"))
import content as U  # noqa: E402

K = 1.45  # slide inches -> printed inches (the same factor the notebook printouts use)


def T(head, rows, ans=(), h=0.3, widths=None):
    """HTML table. Blank cells get a writing height; cells in `ans` (row, col) are shown as answers."""
    cols = "".join(f'<col style="width:{w}%">' for w in widths) if widths else ""
    th = "".join(f"<th>{c}</th>" for c in head)
    trs = ""
    for r, row in enumerate(rows):
        tds = ""
        for c, v in enumerate(row):
            if (r, c) in ans:
                v = f'<span class="ans">{ans[(r, c)] if isinstance(ans, dict) else v}</span>'
            tds += f'<td style="height:{h}in">{v or "&nbsp;"}</td>'
        trs += f"<tr>{tds}</tr>"
    return f'<table style="width:100%"><colgroup>{cols}</colgroup><tr>{th}</tr>{trs}</table>'


def do(s):
    return f'<p class="do">{s}</p>'


def build_pieces():
    """Glue-ins. day + nb is the notebook heading whose "Glue in" box holds the piece; also = later headings that use it.
    h is the printed height in inches of the piece (and of its box on the notebook page)."""
    P = []

    def add(day, nb, title, use, h, body, note="", key=None, copies="1 per student", also=()):
        P.append(dict(day=day, nb=nb, title=title, use=use, h=h, body=body, note=note, key=key, copies=copies, also=tuple(also)))

    def h3(s):
        return f"<h3>{s}</h3>"

    # Day 1
    litter = U.LITTER
    rows1 = [[r[0], r[1] + (" (M)" if r[0] == "Puppy A" else ""), r[2] + (" (M)" if r[0] == "Puppy A" else ""),
              r[3] + (" (D)" if r[0] == "Puppy A" else "")] for r in litter[1]]
    add(1, "Compare the traits", "Puppy litter data", "Glue in · write on it", 2.5,
        do("Next to each puppy trait, write M if it matches Mom or D if it matches Dad. Puppy A is done for you.")
        + T(litter[0], rows1, h=0.22),
        "Puppy A: M, M, D (done). Puppy B: fur D, ears D, pattern M. Puppy C: fur M, ears D, pattern M. Puppy D: fur D, ears M, "
        "pattern D. Every puppy matches one parent for each trait, but each has a different mix.", T(litter[0], rows1, h=0.22))
    # Day 2
    add(2, "Make possible offspring", "Card table: 3 offspring", "Glue in · write on it", 2.0,
        do("Draw one card from each of the six piles. Write what you drew, then put the cards back. Offspring 1 is done for you.")
        + T(U.CARDS[0], U.CARDS[1], h=0.3),
        "Answers vary: each offspring combines one card per pile (one fur color from each parent, and so on).")
    # Day 4
    add(4, "Genotype and phenotype", "Genotype to phenotype: pea plants", "Glue in · write on it", 1.7,
        do("T (tall) is dominant to t (short). TT is done for you. Fill in the phenotype for Tt and tt.") + T(*U.PEAS, h=0.28),
        "Tt: tall. tt: short.",
        T(U.PEAS[0], [["TT", "Tall (done for you)"], ["Tt", "Tall"], ["tt", "Short"]], ans={(1, 1): "Tall", (2, 1): "Short"}, h=0.28))
    add(4, "Punnett squares", "Punnett squares: steps and worked example", "Glue in · copy of the board", 2.0,
        "<p><b>1.</b> Write one parent's two alleles across the top. <b>2.</b> Write the other parent's two alleles down the side. "
        "<b>3.</b> Fill each box with the allele from its column and the allele from its row.</p>"
        "<p><b>Worked example: Tt × Tt</b></p>"
        + T(["", "T", "t"], [["T", "TT", "Tt"], ["t", "Tt", "tt"]], h=0.3, widths=[20, 40, 40])
        + "<p>Result: TT, Tt, Tt, tt. That is <b>3 tall to 1 short</b>.</p>"
        "<p>Each box in a Punnett square shows one possible ____ of alleles.</p>",
        "Answer: combination. Students keep this sheet for Days 4 and 6.")
    # Day 5
    male = U.MALE
    add(5, "How the lab works", "Monster Genetics: the coin rule and Table 2", "Glue in · reference and write on it", 3.9,
        do("Flip a coin twice for each trait. Heads = Allele 1 (capital letter). Tails = Allele 2 (lowercase). Example, Eyes: heads, tails "
           "gives <b>Ee</b>. E is dominant, so the monster has two small eyes.") + T(*U.MONSTER, h=0.24)
        + h3("Table 2: finish the male monster (row 1 is done for you; the other traits are on your Monster Genetics sheet)")
        + T(*male, h=0.26),
        "Table 2 answers: Eye color rr; Skin color green; Tail shape cc; Tail color purple.",
        T(U.MONSTER[0], U.MONSTER[1], h=0.24) + T(male[0], [["Eyes", "ee", "One large eye (done for you)"], ["Eye color", "rr", "White"],
           ["Skin color", "Gg", "Green"], ["Tail shape", "cc", "Straight"], ["Tail color", "Pp", "Purple"]],
          ans={(1, 1): "rr", (2, 2): "Green", (3, 1): "cc", (4, 2): "Purple"}, h=0.26),
        also=["Fill in the male monster"])
    # Day 6
    add(6, "Punnett squares for the baby", "Punnett square: skin color and eyes", "Glue in · write on it", 2.2,
        do("Skin color: Gg × Gg (together). Then Eyes on your own.")
        + T(["", "G", "g"], [["G", "GG", "Gg"], ["g", "Gg", "gg"]], h=0.24, widths=[20, 40, 40])
        + h3("Eyes: ___ × ___") + T(["", "", ""], [["", "", ""], ["", "", ""]], h=0.2, widths=[20, 40, 40]),
        "Eyes: ee × ee gives ee in all four boxes (100% one large eye).",
        T(["", "G", "g"], [["G", "GG", "Gg"], ["g", "Gg", "gg"]], h=0.24, widths=[20, 40, 40])
        + h3("Eyes: ee × ee") + T(["", "e", "e"], [["e", "ee", "ee"], ["e", "ee", "ee"]], h=0.24, widths=[20, 40, 40]))
    add(6, "Class data", "Prediction vs. class count", "Glue in · reference", 1.0,
        T(*U.CLASS_COUNTS, h=0.26), "Reference table (sample class). Use your class's tally if you like.")
    # Day 7
    add(7, "UV and mutations", "UV light and mutations", "Glue in · reference", 1.4,
        T(*U.UV, h=0.18), "Circle the 4-hour row (40 mutations per 1,000 cells).")
    add(7, "Who passes it on?", "Who passes it on? Five cases", "Glue in · write on it", 2.2,
        do("Could the next generation inherit it? Write Yes or No.") + T(*U.CASES, h=0.2),
        "A No; B Yes; C No; D Yes; E No.",
        T(U.CASES[0], [["A", "UV hits a skin cell", "No (done)"], ["B", "Copy error in a sperm-making cell", "Yes"],
                      ["C", "Copy error in a muscle cell", "No"], ["D", "X-rays hit an egg-making cell", "Yes"],
                      ["E", "Smoke chemical hits a lung cell", "No"]], ans={(1, 2): "Yes", (2, 2): "No", (3, 2): "Yes", (4, 2): "No"},
          h=0.26))
    # Day 8
    add(8, "Case 1: the puppy litter", "Case data: three cases", "Glue in · reference", 3.9,
        h3("Case 1: puppy litter") + T(*U.LITTER_ALLELES, h=0.22) + h3("Case 2: DNA of a puppy and its parents")
        + T(*U.DNA_FAMILY, h=0.22) + h3("Case 3: X-rays and mice") + T(*U.XRAY, h=0.22),
        "Reference tables. Case 2: the puppy's CCT is in neither parent (a mutation). Case 3: none = 3 (copying errors), high = 25, so the "
        "X-rays added about 22.", also=["Case 2: a new base", "Case 3: X-rays and mice"])
    # Day 9
    add(9, "The new coat pattern", "The new coat pattern: two kennels", "Glue in · reference", 1.4,
        T(*U.KENNELS, h=0.26), "Reference table. 14 − 3 = 11 extra new patterns per 1,000 puppies in Kennel A.")
    # Day 10
    add(10, "Check my CFAs", "My target tracker", "Glue in · write on it", 2.4,
        do("Write your CFA score out of 5. Below a B (fewer than 4 of 5)? Write Yes under Review. At the end of class, rate each "
           "target 1 to 4 (4 = I could teach it).")
        + T(["Target", "CFA score (of 5)", "Review?", "Rating (1 to 4)"],
            [["LS3-2.1 three sources", "", "", ""], ["LS3-2.2 sex cells and fertilization", "", "", ""],
             ["LS3-2.3 copying errors and UV", "", "", ""], ["LS3-2.4 read data, make a claim", "", "", ""]], h=0.28,
            widths=[40, 20, 16, 24]),
        "Student scores and ratings; nothing to key.", also=["Self-check"])
    add(10, "Enrichment: environment and traits", "Hydrangea soil data", "Glue in · reference", 1.4, T(*U.HYDRANGEA, h=0.24),
        "Reference table (optional enrichment).")
    return P


PIECES = build_pieces()
BY = {(p["day"], p["nb"]): p for p in PIECES}
SECOND = {(p["day"], n): p for p in PIECES for n in p["also"]}


def glue_for(day, nb):
    return BY.get((day, nb))


def glue_second(day, nb):
    """The piece a later heading uses (it is glued in under an earlier heading), or None."""
    return SECOND.get((day, nb))


def glue_box_h(piece):
    """Height of the dashed Glue in box on the notebook page, in slide inches."""
    return round((piece["h"] + 0.12) / K, 2)


# ---------------------------------------------------------------------------
# Documents
# ---------------------------------------------------------------------------
CSS22 = """
.sheet.halves { padding: .35in .75in; gap: .2in; }
.half { padding: .06in .14in; }
.half .tag { display: inline; font-size: 8pt; }
.half .title2 { display: inline; font-size: 12pt; margin-left: .08in; }
.half h3 { font-size: 10pt; margin: .05in 0 .01in; }
.half p.do { margin: .04in 0; font-size: 8.5pt; }
.half table { font-size: 8.5pt; margin: .01in 0 .02in; }
.half td, .half th { padding: 0 4px; }
.half p { font-size: 8.5pt; margin: .03in 0; }
"""


def _p21():
    import print_unit21 as P21  # CSS, wrap, to_pdf (Unit 2.1 printables, same look)
    return P21


def piece_html(p, key=False):
    P21 = _p21()
    body = p["key"] if (key and p["key"]) else p["body"]
    tag = f'Unit 2.2 · Day {p["day"]} · {html.escape(p["use"])}' + (" · KEY" if key else "")
    return (f'<div class="half" style="height:{p["h"]}in"><div class="tag">{tag}</div>'
            f'<p class="title2">{html.escape(p["title"])}</p>{P21.ink(body)}</div>')


def printables_html():
    P21 = _p21()
    rows = "".join(f'<tr><td>Day {p["day"]}</td><td>{html.escape(p["title"])}</td><td>{html.escape(p["use"])}</td>'
                   f'<td>{html.escape(p["copies"])}</td></tr>' for p in PIECES)
    cover = ('<section class="sheet"><div class="full"><p class="title2">Unit 2.2 Printables: Inherited Instructions</p>'
             "<p>Every table students only copy or fill in is printed here, so they do not spend class time drawing it. Cut each piece on "
             "the dashed line and glue it into the matching “Glue in” box on that day's notebook setup page "
             "(Unit22_Student_Notebook.pdf). Print on white paper, black ink only. Answers: Unit22_Printables_Teacher_Key.pdf.</p>"
             '<table class="contents"><tbody><tr><th>Day</th><th>Printable</th><th>Use</th><th>Copies</th></tr>'
             f"{rows}</tbody></table>"
             "<p>Days 3 and 11 need nothing glued in (Day 3 notes are copied into the notebook; Day 11 is the CSA).</p></div></section>")
    sheets, cur, used = [cover], [], 0.0
    for p in PIECES:
        need = p["h"] + 0.5 + 0.25
        if used + need > 10.2 and cur:
            sheets.append('<section class="sheet halves">' + "".join(cur) + "</section>")
            cur, used = [], 0.0
        cur.append(piece_html(p))
        used += need
    if cur:
        sheets.append('<section class="sheet halves">' + "".join(cur) + "</section>")
    return P21.wrap(P21.CSS + CSS22, sheets)


def key_html():
    P21 = _p21()
    sheets = ['<section class="sheet"><div class="full"><p class="title2">Unit 2.2 Printables: Teacher Answer Key</p>'
              "<p>Same order as the student printables. Where students write in a table, the table is filled in (answers in bold italic). "
              "Reference tables have nothing to fill in.</p></div></section>"]
    cur, used = [], 0.0
    for p in PIECES:
        block = (piece_html(p, key=True) + f'<div class="key"><b class="k">KEY</b> {p["note"]}</div>')
        need = p["h"] + 0.9 + 0.2
        if used + need > 10.2 and cur:
            sheets.append('<section class="sheet halves">' + "".join(cur) + "</section>")
            cur, used = [], 0.0
        cur.append(block)
        used += need
    if cur:
        sheets.append('<section class="sheet halves">' + "".join(cur) + "</section>")
    return P21.wrap(P21.CSS + CSS22 + ".sheet.halves { gap: .1in; }", sheets)


def notebook_html():
    import nbslide
    import print_notebook as PN
    P21 = _p21()
    sheets = []
    for d in U.DAYS:
        if d["kind"] == "csa":
            continue
        left, right = nbslide.layout(d["day"])
        label = f"Day {d['day']} · {d['date'].split(' (')[0]}"
        sheets.append(PN.page(d, label, "Left", left, student=True, unit="Unit 2.2"))
        sheets.append(PN.page(d, label, "Right", right, student=True, unit="Unit 2.2"))
    return P21.wrap(PN.CSS, sheets)


if __name__ == "__main__":
    P21 = _p21()
    P21.to_pdf(printables_html(), OUT / "Unit22_Printables.pdf")
    P21.to_pdf(key_html(), OUT / "Unit22_Printables_Teacher_Key.pdf")
    P21.to_pdf(notebook_html(), OUT / "Unit22_Student_Notebook.pdf")
