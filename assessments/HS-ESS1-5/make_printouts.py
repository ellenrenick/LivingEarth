"""Builds the two Unit 3.1 print PDFs (teacher checklist and student notebook printout) with headless Chromium.

Usage: python3 make_printouts.py OUTDIR
"""
import html, re, subprocess, sys, glob
from pathlib import Path
import lessons as L

CSS = """
@page { size: letter; margin: 0.6in; }
body { font-family: 'Nunito Sans', Calibri, Arial, sans-serif; font-size: 11pt; color: #1b2b33; }
h1 { font-size: 20pt; color: #0b2c4a; margin: 0 0 4pt; }
h2 { font-size: 15pt; color: #0b2c4a; border-bottom: 2px solid #d4501a; padding-bottom: 3pt; margin: 0 0 8pt; }
.day { page-break-before: always; }
.day:first-of-type { page-break-before: auto; }
.gi { border: 1.5px dashed #23392c; border-radius: 6px; margin: 0 0 12pt; padding: 0 8pt 8pt; break-inside: avoid; }
.gi h3 { font-size: 11.5pt; background: #fbe9d2; margin: 0 -8pt 6pt; padding: 4pt 8pt; border-radius: 5px 5px 0 0; color: #0b2c4a; }
.gi h3 b { color: #d4501a; }
.gi h3 span { float: right; font-weight: normal; font-size: 9pt; color: #5e7f8f; }
p { margin: 4pt 0; }
table { border-collapse: collapse; width: 100%; margin: 4pt 0 6pt; }
th, td { border: 1px solid #5e7f8f; padding: 4pt 5pt; font-size: 10pt; vertical-align: top; text-align: left; }
th { background: #e8dcc6; }
td.b { height: 30pt; } td.s { height: 18pt; } td.t { height: 56pt; }
ol, ul { margin: 4pt 0 4pt 18pt; padding: 0; } li { margin: 3pt 0; }
.line { border-bottom: 1px solid #333; height: 18pt; margin: 2pt 0; }
.note { font-size: 9.5pt; color: #5e7f8f; }
"""

def esc(s): return html.escape(s)

def table(head, rows, h="b", cls=None):
    """Blank cells ('') get a writing-height class: b = tall, s = short, t = very tall."""
    th = "".join(f"<th>{esc(c)}</th>" for c in head)
    trs = ""
    for r in rows:
        trs += "<tr>" + "".join(f"<td class='{h}'></td>" if c == "" else f"<td>{esc(c)}</td>" for c in r) + "</tr>"
    return f"<table><tr>{th}</tr>{trs}</table>"

def parse(h):
    rows = re.findall(r"<tr>(.*?)</tr>", h, re.S)
    out = []
    for r in rows:
        out.append([re.sub(r"<br\s*/?>", "", re.sub(r"<[^>]+>", "", c)).strip().replace("&divide;", "÷").replace("&times;", "×") for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", r, re.S)])
    return out

def lt(name, h="b"):
    r = parse(getattr(L, name)); return table(r[0], r[1:], h)

def gi(id_, title, where, body):
    return f"<div class='gi'><h3><b>{id_}</b> {esc(title)}<span>{esc(where)}</span></h3>{body}</div>"

def lines(n=2): return "<div class='line'></div>" * n
def olist(items): return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"
def day(title, parts): return f"<section class='day'><h2>{esc(title)}</h2>{''.join(parts)}</section>"
BL = "______"

def student():
    d = []
    d.append(day("Unit pages", [
        gi("U-1", "Unit CER page (glue in Day 1, add a row every day)", "New page",
           "<p><b>Question:</b> Why is the seafloor so much younger than the continents?</p><p><b>My first claim (Day 1):</b></p>" + lines(2) +
           table(["Day", "Evidence (use a number)", "What it shows"], [["", "", ""]] * 8) + "<p><b>My claim after Day 6:</b></p>" + lines(2)),
        gi("U-2", "Frayer card sheet (homework, finish by Day 7)", "Keep in notebook",
           "<p class='note'>For each word write a short definition in your own words, draw a quick picture, and give one example.</p>" +
           table(["Word", "Definition in my own words", "Picture", "Example"], [[w, "", "", ""] for w in L.VOCAB], "t")),
    ]))
    d.append(day("Day 1: Where Did the Old Ocean Floor Go?", [
        gi("D1-D", "Hook data", "Left page, above I notice and I wonder", lt("OCEAN_AGES") + lt("LAND_AGES")),
        gi("D1-A", "Site list for the plotted map", "Left page, beside your world map",
           "<p>Plot each site with a <b>red dot</b> for a volcano and a <b>blue X</b> for an earthquake. Each partner plots five.</p>" + lt("SITE_TABLE") +
           f"<p>The points make {BL} . They match the edges of the {BL} .</p>"),
        gi("D1-B", "Plate boundary table", "Right page, below your clay-model sketches", lt("BOUNDARY_RECORD", "t") + f"<p>Where is ocean crust made? {BL}{BL} Where is it destroyed? {BL}{BL}</p>"),
    ]))
    d.append(day("Day 2: Reading Rock Ages", [
        gi("D2-A", "Seafloor ages and color key", "Left page", lt("SPREAD") + lt("SEAFLOOR_KEY")),
        gi("D2-B", "Seafloor strip: color each box using D2-A", "Left page",
           table(["3,000 km", "2,500", "2,000", "1,500", "1,000", "500", "RIDGE", "500", "1,000", "1,500", "2,000", "2,500", "3,000 km"], [[""] * 13], "t") + f"<p>As you move away from the ridge, the crust gets {BL} .</p>"),
        gi("D2-C", "Graph grid: age vs. distance", "Right page",
           "<p class='note'>Mark a dot in the box where the distance column meets the age row. Connect the dots.</p>" +
           table(["Age (million yrs)", "0 km", "500", "1,000", "1,500", "2,000", "2,500", "3,000 km"], [[str(a)] + [""] * 7 for a in range(120, -1, -20)], "s") +
           f"<p>Rate = distance ÷ time = {BL} km per million years = {BL} cm per year. Age at 3,500 km: {BL} million years.</p>"),
        gi("D2-D", "North America crust ages and strip", "Right page", lt("NA_AGES") +
           "<p>Color the oldest region dark brown and the youngest light yellow. Choose three colors in between.</p>" +
           table(["Pacific Coast Ranges (west)", "Rocky Mountains", "Canadian Shield (core)", "Grenville Province", "Appalachians (east)"], [[""] * 5], "t")),
    ]))
    d.append(day("Day 3: Reading Deep Time and Early Earth", [
        gi("D3-A", "Crater counts (from the crater-counter simulation)", "Left page", lt("CRATER_RECORD") +
           f"<p>Which surface looks older? How can you tell?</p>{lines(1)}<p>Why does Earth show so few craters?</p>{lines(1)}<p>A surface has a lot of craters. Is it old or young? Why?</p>{lines(1)}"),
        gi("D3-B", "Timeline table and old materials", "Right page, with your 45 cm strip",
           "<p class='note'>Scale: 1 cm = 100 million years. Position = (4,500 − age in millions of years) ÷ 100.</p>" + lt("TIMELINE", "s") + lt("OLD")),
    ]))
    d.append(day("Day 4: Why the Ocean Is Young and the Continents Old", [
        gi("D4-A", "Guided notes (fill in as your teacher goes)", "Left page", olist([
            f"Old ocean crust is made at a {BL} and moves away about 2.5 cm a year (25 km per million years).",
            f"A piece of crust travels 3,000 km. Time = 3,000 ÷ 25 = {BL} million years. In 200 million years it travels 200 × 25 = {BL} km, so it reaches a trench and sinks. No ocean floor is older than about {BL} million years.",
            f"Ocean crust has a density of about <b>3.0 g/cm³</b>. Continental crust is about <b>2.7 g/cm³</b>. The {BL} plate sinks (<i>subduction</i>).",
            f"Each continent has an ancient core. Volcanic arcs and pieces of crust are added to its edge over time, like rings on a tree. The edge is {BL} than the core."])),
        gi("D4-B", "Density table", "Left page, for the sink-or-float lab", lt("DENSITY_RECORD", "t") + f"<p>Water has a density of 1.0 g/cm³. Which block is denser? {BL}{BL} What does the denser one do when they meet? {BL}{BL}</p>"),
        gi("D4-C", "SketchNotes checklist", "Right page, above your notes and drawing",
           "<p class='note'>Turn in a photo of your SketchNotes on Canvas: Lesson 4: SketchNotes.</p>" +
           table(["Check", "Half page of notes", "Check", "Cross-section drawing"], [["☐", "Where ocean crust is made", "☐", "Ridge and plate moving away"], ["☐", "How it moves and sinks", "☐", "Trench and volcanic arc"], ["☐", "How continents grow from a core", "☐", "Continent with an ancient core and a younger edge"], ["☐", "Density numbers", "☐", "Density labels and a carbon arrow"]], "s")),
    ]))
    d.append(day("Day 5: Evidence for Moving Crust", [
        gi("D5-A", "Magnetic stripe bands", "Left page, for the paper strip model", "<p class='note'>Color both strips with this table (2 cm = 1 million years). Start at the end you will push through first.</p>" + lt("STRIP_TABLE")),
        gi("D5-B", "Hawaii and GPS", "Right page", lt("HAWAII") + "<p>GPS today: about 7 to 8 cm per year (Pacific plate near Hawaii). 1 km per million years = 0.1 cm per year.</p>" +
           f"<p>Kīlauea to Kauaʻi: 500 ÷ 5 = {BL} km per million years = {BL} cm per year.</p><p>Kīlauea to Midway: {BL} ÷ {BL} = {BL} km per million years = {BL} cm per year.</p>"),
        gi("D5-C", "Fossil table", "Right page, with your Pangaea puzzle", lt("FOSSILS")),
        gi("D5-D", "Evaluate the evidence", "Right page", "<p class='note'>Rate strength from 1 (weak) to 4 (very strong).</p>" + lt("EVIDENCE_EVAL", "t")),
    ]))
    d.append(day("Day 6: Evaluate the Theory, Tell Earth's Story", [
        gi("D6-E", "Three buckets", "Left page, sort your evidence log rows",
           table(["The seafloor is young because…", "The continents are old because…", "The early record is missing because…"], [["", "", ""]], "t")),
        gi("D6-A", "Part A sentence frames", "Left page", re.sub(r"<[^>]*>", lambda m: m.group(0), L.CER_FRAMES)),
        gi("D6-D", "Peer feedback", "Right page", table(["Partner's name", "One star (something strong)", "One step (one thing to improve)"], [["", "", ""]], "t")),
        gi("D6-B", "Evidence cards: cut apart, order oldest to newest, glue on a strip", "Right page", lt("EVIDENCE_CARDS", "s")),
        gi("D6-C", "Part B story frames", "Right page, under your evidence cards", L.STORY_FRAMES),
    ]))
    d.append(day("Day 7: Review Day", [
        gi("D7-A", "Self-rating chart", "Left page",
           "<p class='note'>Rate each target from 1 (I need help) to 4 (I could teach it). Use your CFA scores to check your rating.</p>" +
           table(["Target", "My rating (1–4)", "My CFA score", "What I will do today"], [[f"{c}: {t}", "", "", ""] for c, t in L.TARGET_TEXT.items() if c.startswith("ESS1-5")], "t")),
    ]))
    return "<h1>Unit 3.1 Student Notebook Printout</h1><p class='note'>Print a day at a time, one copy per student. Cut along each title bar and glue where the notebook setup slide shows the box.</p>" + "".join(d)

CHECK = [
 ("U-1","1","Unit CER page: question, claim, evidence log","New page","32","Trim; students add a row each day"),
 ("U-2","1","Frayer card sheet (8 words)","Homework; keep in notebook","32","Hand out Day 1"),
 ("D1-D","1","Hook data: ocean-floor and continent ages","Left","32","Cut the two tables apart"),
 ("D1-A","1","Site list for plotting","Left, beside the map","16","Per pair; not glued"),
 ("D1-B","1","Plate boundary table","Right","32","Trim"),
 ("D2-A","2","Seafloor ages table and color key","Left","32","Trim"),
 ("D2-B","2","13-box seafloor strip","Left","32","Trim"),
 ("D2-C","2","Graph grid: age vs. distance","Right","32","Trim"),
 ("D2-D","2","North America ages table and 5-box strip","Right","32","Trim"),
 ("D3-A","3","Crater counts and three questions","Left","32","Trim"),
 ("D3-B","3","Timeline table and old materials table","Right","32","Trim; strip itself is adding-machine tape"),
 ("D4-A","4","Guided notes with blanks","Left","32","Trim"),
 ("D4-B","4","Density table","Left","32","Trim"),
 ("D4-C","4","SketchNotes checklist","Right","32","Trim"),
 ("D5-A","5","Magnetic stripe band table","Left","32","Trim"),
 ("D5-B","5","Hawaii and GPS table with rate blanks","Right","32","Trim"),
 ("D5-C","5","Fossil table","Right","32","Trim"),
 ("D5-D","5","Evaluate-the-evidence table","Right","32","Trim"),
 ("D6-E","6","Three buckets for sorting evidence","Left","32","Trim"),
 ("D6-A","6","Part A sentence frames","Left","32","Trim"),
 ("D6-D","6","Peer feedback (star and step)","Right","32","Trim"),
 ("D6-B","6","Six evidence cards","Right","32","Students cut apart and sort"),
 ("D6-C","6","Part B story frames","Right","32","Trim"),
 ("D7-A","7","Self-rating chart for the five priority targets","Left","32","Trim"),
]
EXTERNAL = [
 ("World map with latitude and longitude lines","1","32","Students plot on it and tape it into the notebook (D1-A box)"),
 ("Plate boundaries map","1","Project","Shown on the slide"),
 ("Continent cut-outs for the Pangaea puzzle (South America, Africa, India, Australia, Antarctica)","5","8 sets or 1 per pair","Pre-cut; the Building Pangaea Gizmo is an optional alternate"),
 ("45 cm strips of adding-machine tape","3","16","Plain paper strips also work"),
 ("12 cm paper strips, 2 per student, and a folded sheet with a slit","5","32","For the magnetic-stripe model"),
 ("Plain paper for SketchNotes","4","32","A half page of notes and a full page of drawing"),
]
def teacher():
    t = "<h1>Unit 3.1 Printables and Glue-Ins Needed</h1>"
    t += "<p>All pages are in the <b>Unit 3.1 Student Notebook Printout</b>, grouped by day. Every ID matches the dashed \"glue in\" box on that day's notebook setup slide and the orange tag on the lesson slide. Copies assume 32 students.</p>"
    t += "<h2>Print checklist</h2>" + table(["ID", "Day", "Printable", "Notebook page", "Copies", "Prep"], [list(r) for r in CHECK], "s")
    t += "<h2 style='margin-top:14pt'>Not in the student printout</h2>" + table(["Item", "Day", "Copies", "Note"], [list(r) for r in EXTERNAL], "s")
    t += "<p class='note'>Lab supplies (clay, balances, tubs, blocks) are in the Lab Materials and Set-Ups doc. The Day 3 crater lab is now a slide simulation, so it needs no print or supplies.</p>"
    t += "<h2 style='margin-top:14pt'>Prep and glue-in routine</h2>" + olist([
        "Print one day at a time from the student printout, 32 copies each (or print the whole unit once if you copy double-sided).",
        "Trim each glue-in at its heading. Sort the pieces into one labeled tray per ID so students can pick up what the slide names.",
        "At the start of each lab day, the notebook setup slide shows which dashed box each ID goes in. Students glue first, then start the lab.",
        "Use glue sticks for small pieces and tape for the map (D1-A) and the Pangaea puzzle (D5-C).",
        "Glue-in time target: under 2 minutes. If a class runs behind, hand out only the pieces for the first lab and the rest during transitions.",
        "Students fill in blank rows with pencil. Ask them to keep the tables on the slide as a check, not to copy them."])
    return t

def pdf(body, out):
    out = Path(out); h = out.with_suffix(".html")
    h.write_text(f"<!doctype html><meta charset='utf-8'><style>{CSS}</style><body>{body}</body>")
    exe = sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome"))[0]
    subprocess.run([exe, "--headless", "--no-sandbox", "--disable-gpu", f"--print-to-pdf={out}", "--no-pdf-header-footer", f"file://{h}"], check=True, capture_output=True)
    h.unlink()

if __name__ == "__main__":
    o = Path(sys.argv[1]); o.mkdir(parents=True, exist_ok=True)
    pdf(student(), o / "Unit_3.1_Student_Notebook_Printout.pdf")
    pdf(teacher(), o / "Unit_3.1_Printables_and_Glue-Ins_Needed.pdf")
    print("done")
