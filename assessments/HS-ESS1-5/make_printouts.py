"""Builds the two Unit 3.1 print PDFs, modeled on the Unit 2.2 set:
  Unit31_Student_Notebook.pdf  - the notebook setup: a left and a right page per day (title, focus question, headings, lines, glue-in and draw boxes)
  Unit31_Printables.pdf        - the cut-apart glue-ins (tables students would otherwise copy), black ink only

Usage: python3 make_printouts.py OUTDIR
"""
import glob, html, os, subprocess, sys, urllib.request
from pathlib import Path
import lessons as L

FONTS = Path(os.environ.get("ESS_FONT_DIR", "/tmp/ess_fonts"))
FONT_URLS = {"Boogaloo": "https://fonts.gstatic.com/s/boogaloo/v25/kmK-Zq45GAvOdnaW6x1F.ttf",
             "Handlee": "https://fonts.gstatic.com/s/handlee/v20/-F6xfjBsISg9aMakDmo.ttf",
             "Lato": "https://fonts.gstatic.com/s/lato/v25/S6uyw4BMUTPHvxk.ttf",
             "LatoBold": "https://fonts.gstatic.com/s/lato/v25/S6u9w4BMUTPHh6UVew8.ttf"}

def fonts_css():
    FONTS.mkdir(parents=True, exist_ok=True)
    for n, u in FONT_URLS.items():
        p = FONTS / f"{n}.ttf"
        if not p.exists(): urllib.request.urlretrieve(u, p)
    f = lambda fam, n, w="normal": f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file://{FONTS}/{n}.ttf');}}"
    return f("Boogaloo", "Boogaloo") + f("Handlee", "Handlee") + f("Lato", "Lato") + f("Lato", "LatoBold", "bold")

CSS = """
@page { size: letter; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; font-family: Lato, Arial, sans-serif; font-size: 10.5pt; color: #111; }
.page { width: 8.5in; height: 11in; padding: 0.9in 0.78in; page-break-after: always; position: relative; overflow: hidden; }
.frame { border: 1px dashed #777; height: 100%; padding: 14px 24px; overflow: hidden; }
.top { display: flex; justify-content: space-between; font-size: 8pt; letter-spacing: .4px; color: #666; text-transform: uppercase; }
.name { margin-top: 3px; font-size: 10.5pt; }
h1 { font-family: Boogaloo; font-weight: normal; font-size: 27pt; line-height: 1.12; margin: 6px 0 2px; }
h1.cont { font-size: 18pt; margin-top: 4px; }
.focus { margin: 2px 0 6px; }
h2 { font-family: Handlee; font-weight: normal; font-size: 15pt; margin: 12px 0 4px; }
.line { border-bottom: 1px solid #aaa; height: 32px; }
.box { border: 1px solid #777; padding: 5px 7px; font-size: 8.5pt; color: #555; }
.sheet { font-size: 10.5pt; margin: 4px 0; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #777; padding: 3px 6px; font-size: 8.5pt; text-align: left; vertical-align: top; }
th { border-bottom: 2px solid #111; background: none; }
td.w { height: 28px; } td.t { height: 46px; } td.s { height: 20px; }
.cut { border: 1px dashed #777; padding: 8px 14px 10px; margin: 0 0 14px; break-inside: avoid; }
.cut .hd { font-size: 8pt; letter-spacing: .4px; color: #666; text-transform: uppercase; }
.cut .hd b { font-family: Boogaloo; font-weight: normal; font-size: 13pt; letter-spacing: 0; color: #111; text-transform: none; margin-left: 6px; }
.cut .ins { border: 1px solid #777; padding: 3px 7px; margin: 4px 0; font-size: 9pt; }
.cut h3 { font-family: Handlee; font-weight: normal; font-size: 11.5pt; margin: 6px 0 2px; }
.cut p { margin: 3px 0; font-size: 9pt; }
.cut ol { margin: 3px 0 3px 18px; padding: 0; font-size: 9pt; } .cut li { margin: 2px 0; }
.cover h1 { font-size: 15pt; margin: 0; } .cover p { font-size: 10pt; margin: 3px 0 6px; }
.cover td, .cover th { font-size: 10pt; padding: 5px 7px; }
"""

DATES = {1: "Wed Dec 2", 2: "Thu Dec 3", 3: "Fri Dec 4", 4: "Tue Dec 8", 5: "Wed Dec 9", 6: "Fri Dec 11", 7: "Tue Dec 15"}
VOCAB = {1: ["lithosphere (plate)", "plate boundary", "mid-ocean ridge", "subduction", "trench"], 2: ["craton"], 3: ["impact crater"], 5: ["magnetic reversal"]}
B = "______"

def e(s): return html.escape(s)

def tbl(head, rows, cls="w", first_cols=0):
    th = "".join(f"<th>{e(c)}</th>" for c in head)
    out = ""
    for r in rows:
        out += "<tr>" + "".join(f"<td class='{cls}'>{e(c)}</td>" for c in r) + "</tr>"
    return f"<table><tr>{th}</tr>{out}</table>"

# ---------------------------------------------------------------- notebook
def block(b):
    k = b[0]
    if k == "lines": return f"<h2>{e(b[1])}</h2>" + "<div class='line'></div>" * b[2]
    if k == "text": return f"<h2>{e(b[1])}</h2><div class='sheet'>{e(b[2])}</div>" + "<div class='line'></div>" * b[3]
    if k == "glue": return f"<h2>{e(b[1])}</h2><div class='box' style='height:{b[3]}px'>Glue in: {e(b[2])}</div>"
    if k == "draw": return f"<h2>{e(b[1])}</h2><div class='box' style='height:{b[3]}px'>{e(b[2])}</div>"
    if k == "note": return f"<div class='sheet' style='margin-top:10px'>{e(b[1])}</div>"
    if k == "vocab":
        rows = [[w, "", ""] for w in b[1]]
        return "<h2>Vocabulary</h2>" + tbl(["Word", "Definition (my words)", "This reminds me of… (connections)"], rows)
    if k == "vocab8":
        rows = [[w, "", ""] for w in L.VOCAB]
        return "<h2>Vocabulary check</h2>" + tbl(["Word", "I can explain it to a partner (✓)", "My example"], rows, "s")

LEFT = {
 1: [("glue", "Hook data", "D1-D Ocean floor and continent ages", 250), ("lines", "Notice and wonder", 3), ("vocab", VOCAB[1])],
 2: [("lines", "Warm-up", 2), ("glue", "Seafloor ages", "D2-A Seafloor ages and color key", 250), ("glue", "Color the seafloor", "D2-B 13-box strip", 105), ("vocab", VOCAB[2])],
 3: [("lines", "Warm-up", 2), ("vocab", VOCAB[3]), ("glue", "Crater counts", "D3-A Crater counts and three questions", 330)],
 4: [("lines", "Warm-up", 2), ("glue", "Guided notes", "D4-A Guided notes", 340), ("glue", "Sink or float", "D4-B Density table", 150)],
 5: [("lines", "Warm-up", 2), ("vocab", VOCAB[5]), ("glue", "Magnetic stripes", "D5-A Magnetic stripe band table", 170), ("draw", "Tape in your paper stripes", "Tape the stripes here. Label the youngest and oldest crust.", 170)],
 6: [("glue", "Sort your evidence", "D6-E Three buckets", 140), ("glue", "Part A: argument", "D6-A Part A sentence frames", 290), ("lines", "Write your argument", 5)],
 7: [("glue", "Self-rating chart", "D7-A Self-rating chart", 330), ("lines", "Work plan", 4)],
}
RIGHT = {
 1: [("note", "Unit CER: glue U-1 on its own new page and write your first claim."), ("glue", "Plot the pattern", "your plotted world map. Keep the site list (D1-A) beside it.", 140), ("lines", "Pattern sentence", 1),
     ("draw", "Plate boundary models", "Sketch divergent, convergent, and transform. Label the arrows.", 110), ("glue", "Boundary table", "D1-B Plate boundary table", 150), ("lines", "Exit ticket", 3)],
 2: [("glue", "Graph: age vs. distance", "D2-C Graph grid", 270), ("lines", "Rate and prediction", 2), ("glue", "Color North America", "D2-D North America ages and 5-box strip", 280), ("note", "Add two rows to your Unit CER page (U-1): the ocean pattern and the continent pattern.")],
 3: [("glue", "45 cm Earth timeline", "D3-B Timeline table and old materials", 330), ("draw", "Your timeline strip", "Tape your 45 cm strip here and label each event.", 110), ("lines", "Exit ticket", 3), ("note", "Add a row to your Unit CER page (U-1) about meteorites, moon rocks, or zircons.")],
 4: [("glue", "SketchNotes checklist", "D4-C SketchNotes checklist", 150), ("draw", "SketchNotes: notes", "Half a page: the life of ocean crust and how continents grow.", 190), ("draw", "Sensemaking: cross-section", "Draw a ridge, moving plate, trench, volcanic arc, and a continent with a younger edge. Label the densities and add a carbon arrow.", 290), ("note", "Add a row to your Unit CER page (U-1) about density or continental growth.")],
 5: [("glue", "Hawaii and GPS", "D5-B Hawaii and GPS table", 200), ("draw", "Pangaea puzzle", "Tape your best fit here.", 100), ("glue", "Fossils", "D5-C Fossil table", 90), ("glue", "Evaluate the evidence", "D5-D Evaluate-the-evidence table", 150)],
 6: [("glue", "Peer feedback", "D6-D Star and step", 110), ("glue", "Part B: Earth's story", "D6-B Evidence cards, in order from oldest to newest", 240), ("glue", "Story frames", "D6-C Part B story frames", 170), ("note", "Mark every row of your Unit CER page (U-1) that you used today.")],
 7: [("vocab8",), ("lines", "Before the CSA, I will study", 5)],
}

def nb_page(d, side):
    title, focus = L.DAYS[d]["title"], L.DAYS[d]["focus"]
    left = side == "L"
    head = f"<div class='top'><span>Unit 3.1 · Day {d} · {DATES[d]}</span><span>{'Left' if left else 'Right'} page</span></div><div class='name'>Name ______________________________ Period ______ Date ____________</div>"
    t = f"<h1>{e(title)}</h1><div class='focus'><b>Focus question:</b> {e(focus)}</div>" if left else f"<h1 class='cont'>{e(title)} (continued)</h1>"
    body = "".join(block(b) for b in (LEFT if left else RIGHT)[d])
    return f"<div class='page'><div class='frame'>{head}{t}{body}</div></div>"

def notebook():
    return "".join(nb_page(d, s) for d in range(1, 8) for s in "LR")

# ---------------------------------------------------------------- printables
import re

def rows_of(name):
    out = []
    for r in re.findall(r"<tr>(.*?)</tr>", getattr(L, name), re.S):
        out.append([re.sub(r"<[^>]+>", "", c).replace("&divide;", "÷").replace("&times;", "×").strip() for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", r, re.S)])
    return out[0], out[1:]

def lt(name, cls="s", extra=None, done=None):
    head, rows = rows_of(name)
    if extra: head = head + extra; rows = [r + [""] * len(extra) for r in rows]
    if done:
        for (ri, ci), v in done.items(): rows[ri][ci] = v
    return tbl(head, rows, cls)

def lines(n): return "<div class='line' style='height:26px'></div>" * n

def piece(day, mode, title, ins, body):
    ins_html = f"<div class='ins'>{ins}</div>" if ins else ""
    return f"<div class='cut'><div class='hd'>Unit 3.1 · Day {day} · Glue in · {mode} <b>{e(title)}</b></div>{ins_html}{body}</div>"

def olist(items): return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"

def pieces():
    P = []
    def add(id_, day, mode, title, ins, body, copies="1 per student"): P.append((id_, day, mode, title, ins, body, copies))
    add("U-1", 1, "Write on it", "Unit CER page: question, claim, evidence log", "Your first claim goes under the question. Add a row each day. Row 1 is done for you. Glue this on its own new page.",
        "<p><b>Question:</b> Why is the seafloor so much younger than the continents?</p><p><b>My first claim (Day 1):</b></p>" + lines(2) +
        tbl(["Day", "Evidence (use a number)", "What it shows"], [["1", "The oldest ocean floor is about 200 million years old. Continental rock is up to 4.4 billion years old.", "The seafloor is much younger than the continents."]] + [["", "", ""]] * 7) + "<p><b>My claim after Day 6:</b></p>" + lines(2))
    add("U-2", 1, "Write on it", "Frayer card sheet (homework)", "For each word write a definition in your own words, draw a quick picture, and give an example. Row 1 is done for you. Finish by Day 7.",
        tbl(["Word", "Definition in my own words", "Picture", "Example"], [["lithosphere (plate)", "A rigid slab of Earth's outer layer that moves.", "", "The Pacific plate"]] + [[w, "", "", ""] for w in L.VOCAB[1:]], "t"))
    add("D1-D", 1, "Reference", "Hook data: ocean floor and continent ages", "", lt("OCEAN_AGES") + "<br>" + lt("LAND_AGES"))
    add("D1-A", 1, "Write on it", "Site list for the plotted map", "Plot each site on your world map: a red dot for a volcano, a blue X for an earthquake. Each partner plots five. Check Plotted when done. Mount St. Helens is done for you.",
        lt("SITE_TABLE", "s", ["Plotted"], {(0, 4): "✓"}), "1 per pair")
    add("D1-B", 1, "Write on it", "Plate boundary table", "Fill in the table after you make each clay model. Divergent is done for you.",
        tbl(["Boundary", "What the plates did", "What formed", "Real example"], [["Divergent", "Moved apart", "New crust at a mid-ocean ridge", "Mid-Atlantic Ridge"], ["Convergent", "", "", ""], ["Transform", "", "", ""]], "t"))
    add("D2-A", 2, "Reference", "Seafloor ages and color key", "", lt("SPREAD") + "<br>" + lt("SEAFLOOR_KEY"))
    add("D2-B", 2, "Write on it", "Seafloor strip", "Color each box using the key on D2-A. The ridge is done for you.",
        tbl(["3,000 km", "2,500", "2,000", "1,500", "1,000", "500", "RIDGE", "500", "1,000", "1,500", "2,000", "2,500", "3,000 km"], [[""] * 6 + ["red"] + [""] * 6], "t") + f"<p>As you move away from the ridge, the crust gets {B} .</p>")
    add("D2-C", 2, "Write on it", "Graph grid: age vs. distance", "Mark a dot in the box where the distance column meets the age row. Connect the dots. The first dot (0 km, 0 years) is done for you.",
        tbl(["Age (million years)", "0 km", "500", "1,000", "1,500", "2,000", "2,500", "3,000 km"], [[str(a), "●" if a == 0 else "", "", "", "", "", "", ""] for a in range(120, -1, -20)], "s") +
        f"<p>Rate = distance ÷ time = {B} km per million years = {B} cm per year. Age at 3,500 km: {B} million years.</p>")
    add("D2-D", 2, "Reference and write on it", "North America crust ages and strip", "Color the oldest region dark brown and the youngest light yellow. Choose three colors in between. The Canadian Shield is done for you.",
        lt("NA_AGES") + "<br>" + tbl(["Pacific Coast Ranges (west)", "Rocky Mountains", "Canadian Shield (core)", "Grenville Province", "Appalachians (east)"], [["", "", "dark brown", "", ""]], "t"))
    add("D3-A", 3, "Write on it", "Crater counts", "Count the craters at each time step in the simulation. Row 1 is done for you. Then answer the questions.",
        tbl(["Time step", "Moon craters", "Earth craters"], [["1 billion years", "6", "5"], ["2 billion years", "", ""], ["3 billion years", "", ""], ["4 billion years", "", ""]], "w") +
        "<p>Which surface looks older? How can you tell?</p>" + lines(1) + "<p>Why does Earth show so few craters?</p>" + lines(1) + "<p>A surface has a lot of craters. Is it old or young? Why?</p>" + lines(1))
    add("D3-B", 3, "Reference and write on it", "Timeline table and old materials", "Scale: 1 cm = 100 million years. Position = (4,500 − age in millions of years) ÷ 100. Two rows are done for you.",
        lt("TIMELINE") + "<br>" + lt("OLD"))
    add("D4-A", 4, "Write on it", "Guided notes", "Fill in the blanks as your teacher goes. Blank 1 is done for you.",
        olist([f"Old ocean crust is made at a <b>mid-ocean ridge</b> and moves away about 2.5 cm a year (25 km per million years).",
               f"A piece of crust travels 3,000 km. Time = 3,000 ÷ 25 = {B} million years. In 200 million years it travels 200 × 25 = {B} km, so it reaches a trench and sinks. No ocean floor is older than about {B} million years.",
               f"Ocean crust has a density of about <b>3.0 g/cm³</b>. Continental crust is about <b>2.7 g/cm³</b>. The {B} plate sinks (<i>subduction</i>).",
               f"Each continent has an ancient core. Volcanic arcs and pieces of crust are added to its edge over time, like rings on a tree. The edge is {B} than the core."]))
    add("D4-B", 4, "Write on it", "Density table", "Water has a density of 1.0 g/cm³. Density = mass ÷ volume.",
        lt("DENSITY_RECORD", "t") + f"<p>Which block is denser? {B}{B} What does the denser one do when they meet? {B}{B}</p>")
    add("D4-C", 4, "Write on it", "SketchNotes checklist", "Check each box when it is in your SketchNotes. Turn in a photo on Canvas: Lesson 4: SketchNotes.",
        tbl(["", "Half page of notes", "", "Cross-section drawing"], [["☐", "Where ocean crust is made", "☐", "Ridge and plate moving away"], ["☐", "How it moves and sinks", "☐", "Trench and volcanic arc"], ["☐", "How continents grow from a core", "☐", "Continent with an ancient core and a younger edge"], ["☐", "Density numbers", "☐", "Density labels and a carbon arrow"]], "s"))
    add("D5-A", 5, "Reference", "Magnetic stripe bands", "Color both strips with this table (2 cm = 1 million years). Start at the end you will push through first.", lt("STRIP_TABLE"))
    add("D5-B", 5, "Reference and write on it", "Hawaii and GPS", "1 km per million years = 0.1 cm per year. GPS today: about 7 to 8 cm per year. The first rate is worked for you.",
        lt("HAWAII") + f"<p>Kīlauea to Kauaʻi: 500 ÷ 5 = <b>100</b> km per million years = <b>10</b> cm per year (done for you).</p><p>Kīlauea to Midway: {B} ÷ {B} = {B} km per million years = {B} cm per year.</p>")
    add("D5-C", 5, "Reference", "Fossil table", "", lt("FOSSILS"))
    add("D5-D", 5, "Write on it", "Evaluate the evidence", "Rate strength from 1 (weak) to 4 (very strong). Row 1 is started for you.",
        lt("EVIDENCE_EVAL", "t", None, {(0, 1): "Yes", (0, 2): "Past"}))
    add("D6-E", 6, "Write on it", "Three buckets", "Put each row of your Unit CER log in a bucket. One example is done for you.",
        tbl(["The seafloor is young because…", "The continents are old because…", "The early record is missing because…"], [["The oldest ocean floor is only about 200 million years old (done for you).", "", ""], ["", "", ""], ["", "", ""]], "w"))
    add("D6-A", 6, "Reference", "Part A sentence frames", "", re.sub(r"<ul>", "<ol>", re.sub(r"</ul>", "</ol>", L.CER_FRAMES)))
    add("D6-D", 6, "Write on it", "Peer feedback", "Trade papers. Give one star (something strong) and one step (one thing to improve).",
        tbl(["Partner's name", "One star", "One step"], [["", "", ""]], "t"))
    add("D6-B", 6, "Write on it", "Evidence cards", "Cut the cards apart. Put them in order from oldest to newest on a paper strip and glue them down. Card 1 is placed for you.",
        tbl(["Evidence card", "What it shows"], [[c, w] for c, w in [(r[0], r[1]) for r in rows_of("EVIDENCE_CARDS")[1]]], "s"))
    add("D6-C", 6, "Write on it", "Part B story frames", "Use your ordered evidence cards. Frame 1 is done for you.",
        olist([f"About <b>4.56</b> billion years ago, <b>the solar system formed</b>. The evidence is <b>meteorites</b>.", f"About {B} billion years ago, {B} happened. The evidence is {B}.", f"About {B} billion years ago, {B} happened. The evidence is {B}.", f"Earth's earliest record is missing because {B}."]))
    add("D7-A", 7, "Write on it", "Self-rating chart", "Rate each target from 1 (I need help) to 4 (I could teach it). Use your CFA scores to check.",
        tbl(["Target", "My rating (1–4)", "My CFA score", "What I will do today"], [[f"{c}: {t}", "", "", ""] for c, t in L.TARGET_TEXT.items() if c.startswith("ESS1-5")], "t"))
    return P

def printables():
    P = pieces()
    rows = "".join(f"<tr><td>Day {d}</td><td>{e(t)}</td><td>Glue in · {m.lower()}</td><td>{c}</td></tr>" for _, d, m, t, _, _, c in P)
    cover = ("<div class='cut cover'><h1>Unit 3.1 Printables: Age of the Earth</h1><p>Every table students only copy or fill in is printed here, so they do not spend class time drawing it. "
             "Cut each piece on the dashed line and glue it into the matching \"Glue in\" box on that day's notebook setup page (Unit31_Student_Notebook.pdf). Print on white paper, black ink only.</p>"
             f"<table><tr><th>Day</th><th>Printable</th><th>Use</th><th>Copies</th></tr>{rows}</table>"
             "<p>Day 8 (CSA) needs nothing glued in. Things not printed here: the world map with latitude and longitude lines (Day 1), the continent cut-outs for the Pangaea puzzle (Day 5), and the 45 cm adding-machine tape strips (Day 3).</p></div>")
    body = "".join(piece(d, m, t, i, b) for _, d, m, t, i, b, _ in P)
    return cover + body

def pdf(body, out):
    out = Path(out); h = out.with_suffix(".html")
    h.write_text(f"<!doctype html><meta charset='utf-8'><style>{fonts_css()}{CSS}</style><body>{body}</body>")
    exe = sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome"))[0]
    subprocess.run([exe, "--headless", "--no-sandbox", "--disable-gpu", "--allow-file-access-from-files", f"--print-to-pdf={out}", "--no-pdf-header-footer", f"file://{h}"], check=True, capture_output=True)
    h.unlink()

if __name__ == "__main__":
    o = Path(sys.argv[1]); o.mkdir(parents=True, exist_ok=True)
    pdf(notebook(), o / "Unit31_Student_Notebook.pdf")
    pdf(printables(), o / "Unit31_Printables.pdf")
    print("done")
