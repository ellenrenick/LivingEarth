"""Builds the Unit 3.1 print PDFs, modeled on the Unit 2.2 set:
  Unit31_Student_Notebook.pdf          notebook setup: a left and a right page per day
  Unit31_Printables.pdf                cut-apart glue-ins (black ink)
  Unit31_Printables_Teacher_Key.pdf    the same pieces with answers, plus the lesson answer notes
  Unit31_Teacher_Notebook.pdf          the notebook pages filled in, with each glue-in in place

Each notebook "Glue in" box is sized from the measured height of its printable piece (same width, same height),
so a cut piece fits its box exactly.

Usage: python3 make_printouts.py OUTDIR
"""
import glob, html, json, os, re, subprocess, sys, urllib.request
from pathlib import Path
import lessons as L

FONTS = Path(os.environ.get("ESS_FONT_DIR", "/tmp/ess_fonts"))
FONT_URLS = {"Boogaloo": "https://fonts.gstatic.com/s/boogaloo/v25/kmK-Zq45GAvOdnaW6x1F.ttf",
             "Handlee": "https://fonts.gstatic.com/s/handlee/v20/-F6xfjBsISg9aMakDmo.ttf",
             "Lato": "https://fonts.gstatic.com/s/lato/v25/S6uyw4BMUTPHvxk.ttf",
             "LatoBold": "https://fonts.gstatic.com/s/lato/v25/S6u9w4BMUTPHh6UVew8.ttf"}
BOX_W = "6.44in"   # width of a notebook glue-in box and of a printable piece
CHROME = sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome"))[0]

def fonts_css():
    FONTS.mkdir(parents=True, exist_ok=True)
    for n, u in FONT_URLS.items():
        p = FONTS / f"{n}.ttf"
        if not p.exists(): urllib.request.urlretrieve(u, p)
    f = lambda fam, n, w="normal": f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file://{FONTS}/{n}.ttf');}}"
    return f("Boogaloo", "Boogaloo") + f("Handlee", "Handlee") + f("Lato", "Lato") + f("Lato", "LatoBold", "bold")

CSS = """
* { box-sizing: border-box; }
body { margin: 0; font-family: Lato, Arial, sans-serif; font-size: 10.5pt; color: #111; }
.page { width: 8.5in; height: 11in; padding: 0.9in 0.78in; page-break-after: always; position: relative; overflow: hidden; }
.frame { border: 1px dashed #777; height: 100%; padding: 14px 24px; overflow: hidden; }
.top { display: flex; justify-content: space-between; font-size: 8pt; letter-spacing: .4px; color: #666; text-transform: uppercase; }
.name { margin-top: 3px; font-size: 10.5pt; }
h1 { font-family: Boogaloo; font-weight: normal; font-size: 27pt; line-height: 1.12; margin: 6px 0 2px; }
h1.cont { font-size: 18pt; margin-top: 4px; }
.focus { margin: 2px 0 6px; }
h2 { font-family: Handlee; font-weight: normal; font-size: 15pt; margin: 7px 0 3px; }
.line { border-bottom: 1px solid #aaa; height: 32px; }
.ruled { background: repeating-linear-gradient(to bottom, transparent 0, transparent 31px, #aaa 31px, #aaa 32px); line-height: 32px; font-family: Handlee; font-size: 11pt; }
.box { border: 1px solid #777; padding: 5px 7px; font-size: 8.5pt; color: #555; }
.box .a { display: block; margin-top: 3px; }
.sheet { font-size: 10.5pt; margin: 4px 0; }
.a { font-family: Handlee; font-weight: bold; font-size: 9.5pt; color: #111; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #777; padding: 3px 6px; font-size: 8.5pt; text-align: left; vertical-align: top; }
th { border-bottom: 2px solid #111; }
td.w { height: 26px; } td.t { height: 42px; } td.s { height: 19px; }
.cut { width: BOXW; border: 1px dashed #777; padding: 8px 14px 10px; margin: 0 0 12px; break-inside: avoid; }
.cut .hd { font-size: 8pt; letter-spacing: .4px; color: #666; text-transform: uppercase; }
.cut .hd b { font-family: Boogaloo; font-weight: normal; font-size: 13pt; letter-spacing: 0; color: #111; text-transform: none; margin-left: 6px; }
.cut .ins { border: 1px solid #777; padding: 3px 7px; margin: 4px 0; font-size: 9pt; }
.cut p { margin: 3px 0; font-size: 9pt; }
.cut ol { margin: 3px 0 3px 18px; padding: 0; font-size: 9pt; } .cut li { margin: 2px 0; }
.cut .line { height: 24px; }
.cover { margin-bottom: 12px; } .cover h1 { font-size: 15pt; margin: 0; } .cover p { font-size: 10pt; margin: 3px 0 6px; }
.cover td, .cover th { font-size: 10pt; padding: 5px 7px; }
.knote { margin: 0 0 12px; width: BOXW; } .knote h2 { font-size: 13pt; margin: 8px 0 3px; } .knote li { font-size: 9.5pt; margin: 2px 0; }
""".replace("BOXW", BOX_W)

DATES = {1: "Wed Dec 2", 2: "Thu Dec 3", 3: "Fri Dec 4", 4: "Tue Dec 8", 5: "Wed Dec 9", 6: "Fri Dec 11", 7: "Tue Dec 15"}
B = "______"
def e(s): return html.escape(s)

# ---------------------------------------------------------------- tables
def cell(c, cls, k):
    if isinstance(c, tuple): c = c[1] if k else c[0]; ans = k and bool(c)
    else: ans = False
    return f"<td class='{cls}'>" + (f"<span class='a'>{e(c)}</span>" if ans else e(c)) + "</td>"

def tbl(head, rows, cls="w", k=False):
    th = "".join(f"<th>{e(c)}</th>" for c in head)
    return f"<table><tr>{th}</tr>" + "".join("<tr>" + "".join(cell(c, cls, k) for c in r) + "</tr>" for r in rows) + "</table>"

def rows_of(name):
    out = []
    for r in re.findall(r"<tr>(.*?)</tr>", getattr(L, name), re.S):
        out.append([re.sub(r"<[^>]+>", "", c).replace("&divide;", "÷").replace("&times;", "×").strip() for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", r, re.S)])
    return out[0], out[1:]

def lt(name, cls="s", k=False, extra=None, fill=None):
    head, rows = rows_of(name)
    if extra: head = head + extra; rows = [r + [""] * len(extra) for r in rows]
    for (ri, ci), v in (fill or {}).items(): rows[ri][ci] = v
    return tbl(head, rows, cls, k)

def ruled(n, text, k, h=24):
    if k: return f"<div class='ruled' style='height:{n*h}px;line-height:{h}px;background-size:100% {h}px;background-image:repeating-linear-gradient(to bottom,transparent 0,transparent {h-1}px,#aaa {h-1}px,#aaa {h}px)'>{e(text)}</div>"
    return f"<div class='line' style='height:{h}px'></div>" * n

def olist(items): return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"

def blank(k, ans): return f"<span class='a'>{e(ans)}</span>" if k else B

# ---------------------------------------------------------------- printable pieces
def pieces(k):
    P = []
    def add(id_, day, mode, title, ins, body, copies="1 per student"): P.append((id_, day, mode, title, ins, body, copies))
    A = lambda s: ("", s)   # blank for students, answer for the key
    claim1 = "The seafloor is young because it keeps getting renewed."
    rows = [["1", "The oldest ocean floor is about 200 million years old. Continental rock is up to 4.4 billion years old.", "The seafloor is much younger than the continents."],
            [A("2"), A("Ocean crust is 0 million years old at the ridge and 120 million years old 3,000 km away (2.5 cm per year)."), A("Age increases with distance from the ridge.")],
            [A("2"), A("North American crust is about 2.7 billion years old at its core and about 400 million years old in the Appalachians."), A("Continents have old cores and younger edges.")],
            [A("3"), A("Meteorites are about 4.56 billion years old; the oldest Earth rock is about 4.0 billion."), A("Earth's early record is missing.")],
            [A("4"), A("Ocean crust is about 3.0 g/cm³; continental crust is about 2.7 g/cm³."), A("The denser ocean plate sinks; continents survive.")],
            [A("5"), A("Kauaʻi moved about 10 cm per year; GPS says 7 to 8 cm per year."), A("Two independent methods agree.")],
            [A("6"), A("The oldest ocean floor is only about 200 million years old."), A("Ocean crust is recycled.")],
            ["", "", ""]]
    add("U-1", 1, "Write on it", "Unit CER page: question, claim, evidence log", "Your first claim goes under the question. Add a row each day. Row 1 is done for you. Glue this on its own new page.",
        "<p><b>Question:</b> Why is the seafloor so much younger than the continents?</p><p><b>My first claim (Day 1):</b></p>" + ruled(2, claim1 + " (Baseline: accept any attempt.)", k) +
        tbl(["Day", "Evidence (use a number)", "What it shows"], rows, "w", k) + "<p><b>My claim after Day 6:</b></p>" +
        ruled(2, "Plate tectonics explains the ages very well: ocean crust is made at ridges and recycled at trenches, while less-dense continents survive and grow.", k))
    fz = {"plate boundary (divergent, convergent, transform)": ("Where two plates meet: they move apart, together, or past each other.", "sketch: three arrow pairs", "San Andreas Fault"),
          "mid-ocean ridge": ("Underwater mountain chain where new ocean crust forms.", "sketch: ridge with arrows", "Mid-Atlantic Ridge"),
          "subduction": ("One plate sinks beneath another.", "sketch: slab diving down", "Nazca plate under South America"),
          "trench": ("A deep groove where a plate sinks.", "sketch: V-shaped groove", "Mariana Trench"),
          "magnetic reversal": ("Earth's magnetic field flips direction; the crust records it as stripes.", "sketch: mirror stripes", "Stripes on each side of a ridge"),
          "craton (a continent's ancient core)": ("The ancient core of a continent.", "sketch: bullseye of ages", "Canadian Shield"),
          "impact crater": ("A bowl-shaped dent made when a rock hits a surface.", "sketch: crater", "Moon highlands")}
    add("U-2", 1, "Write on it", "Frayer card sheet (homework)", "For each word write a definition in your own words, draw a quick picture, and give an example. Row 1 is done for you. Finish by Day 7.",
        tbl(["Word", "Definition in my own words", "Picture", "Example"], [["lithosphere (plate)", "A rigid slab of Earth's outer layer that moves.", "", "The Pacific plate"]] +
            [[w, A(fz[w][0]), A(fz[w][1]), A(fz[w][2])] for w in L.VOCAB[1:]], "t", k))
    add("D1-D", 1, "Reference", "Hook data: ocean floor and continent ages", "", lt("OCEAN_AGES") + "<br>" + lt("LAND_AGES"))
    h, r = rows_of("SITE_TABLE")
    add("D1-A", 1, "Write on it", "Site list for the plotted map", "Plot each site on your world map: a red dot for a volcano, a blue X for an earthquake. Each partner plots five. Check Plotted when done. Mount St. Helens is done for you.",
        tbl(h + ["Plotted"], [x + ["✓" if i == 0 else A("✓")] for i, x in enumerate(r)], "s", k) +
        f"<p>The points make {blank(k, 'lines')} . They match the edges of the {blank(k, 'plates')} .</p>" + ("<p><span class='a'>Kīlauea is a hot spot inside a plate: circle it as the one that does not fit.</span></p>" if k else ""), "1 per pair")
    add("D1-B", 1, "Write on it", "Plate boundary table", "Fill in the table after you make each clay model. Divergent is done for you.",
        tbl(["Boundary", "What the plates did", "What formed", "Real example"], [["Divergent", "Moved apart", "New crust at a mid-ocean ridge", "Mid-Atlantic Ridge"],
            ["Convergent", A("Pushed together; the ocean slab slid under"), A("A trench and volcanoes (subduction)"), A("Pacific coast of South America")],
            ["Transform", A("Slid past each other"), A("A broken line; earthquakes"), A("San Andreas Fault")]], "t", k))
    add("D2-A", 2, "Reference", "Seafloor ages and color key", "", lt("SPREAD") + "<br>" + lt("SEAFLOOR_KEY"))
    cols = ["dark purple", "purple", "blue", "green", "yellow", "orange", "red", "orange", "yellow", "green", "blue", "purple", "dark purple"]
    add("D2-B", 2, "Write on it", "Seafloor strip", "Color each box using the key on D2-A. The ridge is done for you.",
        tbl(["3,000 km", "2,500", "2,000", "1,500", "1,000", "500", "RIDGE", "500", "1,000", "1,500", "2,000", "2,500", "3,000 km"], [[("", c) if i != 6 else "red" for i, c in enumerate(cols)]], "t", k) +
        f"<p>As you move away from the ridge, the crust gets {blank(k, 'older')} .</p>")
    grid = [[str(a), "●" if a == 0 else ("", "●") if k or True else ""] for a in range(120, -1, -20)]
    g = []
    for a in range(120, -1, -20):
        row = [str(a)]
        for ci in range(7):
            on = (a == ci * 20)
            row.append("●" if (a == 0 and ci == 0) else (("", "●") if on else ""))
        g.append(row)
    add("D2-C", 2, "Write on it", "Graph grid: age vs. distance", "Mark a dot in the box where the distance column meets the age row. Connect the dots. The first dot (0 km, 0 years) is done for you.",
        tbl(["Age (million years)", "0 km", "500", "1,000", "1,500", "2,000", "2,500", "3,000 km"], g, "s", k) +
        f"<p>Rate = distance ÷ time = {blank(k, '25')} km per million years = {blank(k, '2.5')} cm per year. Age at 3,500 km: {blank(k, '140')} million years.</p>")
    add("D2-D", 2, "Reference and write on it", "North America crust ages and strip", "Color the oldest region dark brown and the youngest light yellow. Choose three colors in between. The Canadian Shield is done for you.",
        lt("NA_AGES") + "<br>" + tbl(["Pacific Coast Ranges (west)", "Rocky Mountains", "Canadian Shield (core)", "Grenville Province", "Appalachians (east)"], [[A("light yellow"), A("yellow"), "dark brown", A("brown"), A("tan")]], "t", k))
    add("D3-A", 3, "Write on it", "Crater counts", "Count the craters at each time step in the simulation. Row 1 is done for you. Then answer the questions.",
        tbl(["Time step", "Moon craters", "Earth craters"], [["1 billion years", "6", "5"], ["2 billion years", A("12"), A("4")], ["3 billion years", A("18"), A("6")], ["4 billion years", A("24"), A("5")]], "w", k) +
        "<p>Which surface looks older? How can you tell?</p>" + ruled(1, "The Moon: it has many craters that stay.", k) +
        "<p>Why does Earth show so few craters?</p>" + ruled(1, "Erosion, volcanoes, and moving plates erase them.", k) +
        "<p>A surface has a lot of craters. Is it old or young? Why?</p>" + ruled(1, "Old: craters pile up over time.", k))
    add("D3-B", 3, "Reference and write on it", "Timeline table and old materials", "Scale: 1 cm = 100 million years. Position = (4,500 − age in millions of years) ÷ 100. Two rows are done for you.",
        lt("TIMELINE", "s", k, None, {(2, 2): ("", "5"), (3, 2): ("", "10"), (4, 2): ("", "43")}) + "<br>" + lt("OLD"))
    add("D4-A", 4, "Write on it", "Guided notes", "Fill in the blanks as your teacher goes. Blank 1 is done for you.",
        olist(["Old ocean crust is made at a <b>mid-ocean ridge</b> and moves away about 2.5 cm a year (25 km per million years).",
               f"A piece of crust travels 3,000 km. Time = 3,000 ÷ 25 = {blank(k, '120')} million years. In 200 million years it travels 200 × 25 = {blank(k, '5,000')} km, so it reaches a trench and sinks. No ocean floor is older than about {blank(k, '200')} million years.",
               f"Ocean crust has a density of about <b>3.0 g/cm³</b>. Continental crust is about <b>2.7 g/cm³</b>. The {blank(k, 'ocean')} plate sinks (<i>subduction</i>).",
               f"Each continent has an ancient core. Volcanic arcs and pieces of crust are added to its edge over time, like rings on a tree. The edge is {blank(k, 'younger')} than the core."]))
    add("D4-B", 4, "Write on it", "Density table", "Water has a density of 1.0 g/cm³. Density = mass ÷ volume.",
        tbl(["Block", "Mass (g)", "Volume (cm³)", "Density (g/cm³) = mass ÷ volume", "Sinks or floats?"],
            [["Wood block (stand-in for a continent)", A("40"), A("64"), A("0.6"), A("floats")], ["Clay block (stand-in for an old, cold ocean plate)", A("128"), A("64"), A("2.0"), A("sinks")]], "t", k) +
        f"<p>Which block is denser? {blank(k, 'clay')} What does the denser one do when they meet? {blank(k, 'dives under')}</p>" + ("<p><span class='a'>Sample values; real numbers depend on your blocks.</span></p>" if k else ""))
    box = "☑" if k else "☐"
    add("D4-C", 4, "Write on it", "SketchNotes checklist", "Check each box when it is in your SketchNotes. Turn in a photo on Canvas: Lesson 4: SketchNotes.",
        tbl(["", "Half page of notes", "", "Cross-section drawing"], [[box, "Where ocean crust is made", box, "Ridge and plate moving away"], [box, "How it moves and sinks", box, "Trench and volcanic arc"],
            [box, "How continents grow from a core", box, "Continent with an ancient core and a younger edge"], [box, "Density numbers", box, "Density labels and a carbon arrow"]], "s", k))
    add("D5-A", 5, "Reference", "Magnetic stripe bands", "Color both strips with this table (2 cm = 1 million years). Start at the end you will push through first.", lt("STRIP_TABLE"))
    add("D5-B", 5, "Reference and write on it", "Hawaii and GPS", "1 km per million years = 0.1 cm per year. GPS today: about 7 to 8 cm per year. The first rate is worked for you.",
        lt("HAWAII") + f"<p>Kīlauea to Kauaʻi: 500 ÷ 5 = <b>100</b> km per million years = <b>10</b> cm per year (done for you).</p>"
        f"<p>Kīlauea to Midway: {blank(k, '2,500')} ÷ {blank(k, '28')} = {blank(k, 'about 90')} km per million years = {blank(k, 'about 9')} cm per year.</p>")
    add("D5-C", 5, "Reference", "Fossil table", "", lt("FOSSILS"))
    add("D5-D", 5, "Write on it", "Evaluate the evidence", "Rate strength from 1 (weak) to 4 (very strong). Row 1 is started for you.",
        tbl(["Line of evidence", "Measured numbers?", "Past or present motion?", "Independent of the others?", "Strength (1–4)"],
            [["Rock ages across a ridge", "Yes", "Past", A("Yes"), A("4")], ["Magnetic stripes", A("Yes"), A("Past"), A("Yes"), A("4")], ["GPS and Hawaiian island ages", A("Yes"), A("Present and past"), A("Yes"), A("4")], ["Matching fossils and rocks", A("No"), A("Past"), A("Partly"), A("2 to 3")]], "t", k))
    add("D6-E", 6, "Write on it", "Three buckets", "Put each row of your Unit CER log in a bucket. One example is done for you.",
        tbl(["The seafloor is young because…", "The continents are old because…", "The early record is missing because…"],
            [["The oldest ocean floor is only about 200 million years old (done for you).", "", ""], [A("Crust is 0 at the ridge and 120 million years at 3,000 km."), A("The Canadian Shield is about 2.7 billion years old."), A("Plate tectonics and erosion recycled it.")],
             [A("Ocean plates sink at trenches."), A("Continents are less dense, so they stay on top."), A("Scientists use meteorites and moon rocks.")]], "w", k))
    add("D6-A", 6, "Reference", "Part A sentence frames", "", re.sub(r"<ul>", "<ol>", re.sub(r"</ul>", "</ol>", L.CER_FRAMES)))
    add("D6-D", 6, "Write on it", "Peer feedback", "Trade papers. Give one star (something strong) and one step (one thing to improve).",
        tbl(["Partner's name", "One star", "One step"], [[A("Sam"), A("You used the number 2.5 cm per year."), A("Say what the evidence cannot show.")]], "t", k))
    add("D6-B", 6, "Write on it", "Evidence cards", "Cut the cards apart. Put them in order from oldest to newest on a paper strip and glue them down. Card 1 is placed for you.",
        tbl(["Order", "Evidence card", "What it shows"], [[("1" if i == 0 else ("", str(i + 1))), c, w] for i, (c, w) in enumerate((r_[0], r_[1]) for r_ in rows_of("EVIDENCE_CARDS")[1])], "s", k))
    add("D6-C", 6, "Write on it", "Part B story frames", "Use your ordered evidence cards. Frame 1 is done for you.",
        olist(["About <b>4.56</b> billion years ago, <b>the solar system formed</b>. The evidence is <b>meteorites</b>.",
               f"About {blank(k, '4.4')} billion years ago, {blank(k, 'solid crust and zircon minerals formed')}. The evidence is {blank(k, 'moon rocks and zircons')}.",
               f"About {blank(k, '3.5')} billion years ago, {blank(k, 'life existed')}. The evidence is {blank(k, 'stromatolite fossils')}.",
               f"Earth's earliest record is missing because {blank(k, 'plate tectonics and erosion recycled it')}."]))
    add("D7-A", 7, "Write on it", "Self-rating chart", "Rate each target from 1 (I need help) to 4 (I could teach it). Use your CFA scores to check.",
        tbl(["Target", "My rating (1–4)", "My CFA score", "What I will do today"], [[f"{c}: {t}", A("(personal)"), A("(personal)"), A("(personal)")] for c, t in L.TARGET_TEXT.items() if c.startswith("ESS1-5")], "t", k))
    return P

def piece_html(p, k):
    id_, day, mode, title, ins, body, _ = p
    ins_html = f"<div class='ins'>{ins}</div>" if ins else ""
    return f"<div class='cut' data-id='{id_}'><div class='hd'>Unit 3.1 · Day {day} · Glue in · {mode} <b>{e(title)}</b></div>{ins_html}{body}</div>"

# ---------------------------------------------------------------- chrome helpers
def dump(body, css_extra, script):
    tmp = Path("/tmp/ess_measure.html")
    tmp.write_text(f"<!doctype html><meta charset='utf-8'><style>{fonts_css()}{CSS}{css_extra}</style><body>{body}<pre id='o'></pre><script>{script}</script></body>")
    out = subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--allow-file-access-from-files", "--virtual-time-budget=8000", "--dump-dom", f"file://{tmp}"], check=True, capture_output=True, text=True).stdout
    return json.loads(html.unescape(re.search(r"<pre id=\"o\">(.*?)</pre>", out, re.S).group(1)))

def measure():
    body = "".join(piece_html(p, k) for k in (False, True) for p in pieces(k))
    js = "document.fonts.ready.then(()=>{const h={};document.querySelectorAll('.cut[data-id]').forEach(e=>{h[e.dataset.id]=Math.max(h[e.dataset.id]||0,Math.ceil(e.getBoundingClientRect().height))});document.getElementById('o').textContent=JSON.stringify(h)})"
    return dump(body, "", js)

def overflow(body):
    js = "document.fonts.ready.then(()=>{const r=[];document.querySelectorAll('.frame').forEach((f,i)=>{r.push([i+1,f.scrollHeight-f.clientHeight])});document.getElementById('o').textContent=JSON.stringify(r)})"
    return dump(body, "@page{size:letter;margin:0}", js)

def pdf(body, out, margin="0"):
    out = Path(out); h = out.with_suffix(".html")
    h.write_text(f"<!doctype html><meta charset='utf-8'><style>@page{{size:letter;margin:{margin}}}{fonts_css()}{CSS}</style><body>{body}</body>")
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--allow-file-access-from-files", f"--print-to-pdf={out}", "--no-pdf-header-footer", f"file://{h}"], check=True, capture_output=True)
    h.unlink()

# ---------------------------------------------------------------- notebook
VOCAB = {1: ["lithosphere (plate)", "plate boundary", "mid-ocean ridge", "subduction", "trench"], 2: ["craton"], 3: ["impact crater"], 5: ["magnetic reversal"]}
DEF = {"lithosphere (plate)": ("A rigid slab of Earth's outer layer that moves.", "The Pacific plate"), "plate boundary": ("Where two plates meet.", "San Andreas Fault"),
       "mid-ocean ridge": ("Where new ocean crust forms.", "Mid-Atlantic Ridge"), "subduction": ("One plate sinks under another.", "Nazca plate"), "trench": ("Deep groove where a plate sinks.", "Mariana Trench"),
       "craton": ("A continent's ancient core.", "Canadian Shield"), "impact crater": ("A dent made by a rock hitting a surface.", "Moon highlands"), "magnetic reversal": ("The magnetic field flips; crust records it.", "Mirror stripes")}

def glue_h(text, H, h):
    m = re.match(r"([UD]\d?-?[A-Z0-9]+)\b", text)
    return H.get(m.group(1)) if m and m.group(1) in H else h

def block(b, H, P, k):
    kind = b[0]
    if kind == "lines": return f"<h2>{e(b[1])}</h2>" + ruled(b[2], b[3], k, 32)
    if kind == "note": return f"<div class='sheet' style='margin-top:10px'>{e(b[1])}</div>"
    if kind == "glue":
        text, h = b[2], b[3]
        m = re.match(r"([UD]\d?-?[A-Z0-9]+)\b", text)
        pid = m.group(1) if m else None
        if pid in H:
            if k:
                p = next(x for x in P if x[0] == pid)
                inner = piece_html(p, True).replace("class='cut'", f"class='cut' style='margin:0;height:{H[pid]}px'")
                return (f"<h2>{e(b[1])}</h2>" if b[1] else "") + inner
            return (f"<h2>{e(b[1])}</h2>" if b[1] else "<div style='height:6px'></div>") + f"<div class='box' style='height:{H[pid]}px;width:{BOX_W}'>Glue in: {e(text)}</div>"
        return f"<h2>{e(b[1])}</h2><div class='box' style='height:{h}px'>{e('Glue in: ' + text)}</div>" if not k else f"<h2>{e(b[1])}</h2><div class='box' style='height:{h}px'>{e('Glue in: ' + text)}<span class='a'>{e(b[4]) if len(b) > 4 else ''}</span></div>"
    if kind == "draw": return f"<h2>{e(b[1])}</h2><div class='box' style='height:{b[3]}px'>{e(b[2])}" + (f"<span class='a'>Sample: {e(b[4])}</span>" if k and len(b) > 4 else "") + "</div>"
    if kind == "vocab":
        rows = [[w, ("", DEF[w][0]), ("", DEF[w][1])] for w in b[1]]
        return "<h2>Vocabulary</h2>" + tbl(["Word", "Definition (my words)", "This reminds me of… (connections)"], rows, "w", k)
    if kind == "vocab8":
        rows = [[w, ("", "✓"), ("", DEF.get(w.split(" (")[0], ("", ""))[1])] for w in L.VOCAB]
        return "<h2>Vocabulary check</h2>" + tbl(["Word", "I can explain it to a partner (✓)", "My example"], rows, "s", k)

LEFT = {
 1: [("glue", "Hook data", "D1-D Ocean floor and continent ages", 250), ("lines", "Notice and wonder", 3, "I notice the ocean floor is much younger than the continents. I wonder where the old ocean floor went."), ("vocab", VOCAB[1])],
 2: [("lines", "Warm-up", 1, "The Brazil sample is older. It is far from the ridge, and crust gets older away from the ridge."), ("glue", "Seafloor ages", "D2-A Seafloor ages and color key", 250), ("glue", None, "D2-B 13-box strip", 105), ("vocab", VOCAB[2])],
 3: [("lines", "Warm-up", 2, "Use atoms that change at a steady rate, like a clock, to date rocks."), ("vocab", VOCAB[3]), ("glue", "Crater counts", "D3-A Crater counts and three questions", 330)],
 4: [("lines", "Warm-up", 2, "It sinks back into the mantle at a trench (subduction)."), ("glue", "Guided notes", "D4-A Guided notes", 340), ("glue", "Sink or float", "D4-B Density table", 150)],
 5: [("lines", "Warm-up", 2, "Past: rock ages, stripes, and fossils. Today: GPS and the Hawaiian islands."), ("vocab", VOCAB[5]), ("glue", "Magnetic stripes", "D5-A Magnetic stripe band table", 170),
     ("draw", "Tape in your paper stripes", "Tape the stripes here. Label the youngest and oldest crust.", 170, "mirror-image red and blue stripes on both sides of the slit; youngest at the center")],
 6: [("glue", "Sort your evidence", "D6-E Three buckets", 140), ("glue", "Part A: argument", "D6-A Part A sentence frames", 290),
     ("lines", "Write your argument", 5, "Plate tectonics explains the ages very well. The seafloor is youngest at the ridge (0) and no older than about 200 million years, while continents have crust up to 4.4 billion years old. Ocean plates are denser, so they sink at trenches, while continents survive. One limit: no early ocean floor is left, so we also use meteorites.")],
 7: [("glue", "Self-rating chart", "D7-A Self-rating chart", 330), ("lines", "Work plan", 4, "Retake CFA 5.5. Do the review for ESS1-5.3. Then the enrichment board.")],
}
RIGHT = {
 1: [("note", "Unit CER: glue U-1 on its own new page and write your first claim."), ("glue", "Plot the pattern", "your plotted world map. Keep the site list (D1-A) beside it.", 100, "Sample: points in lines along the Pacific rim and the mid-Atlantic"),
     ("lines", "Pattern sentence", 1, "The points make lines. They match the edges of the plates."), ("draw", "Plate boundary models", "Sketch divergent, convergent, and transform. Label the arrows.", 90, "arrows apart with a ridge; a blue slab under a tan block with a trench; arrows sliding past each other"),
     ("glue", "Boundary table", "D1-B Plate boundary table", 150), ("lines", "Exit ticket", 3, "Ocean crust is made at mid-ocean ridges and sinks back down at trenches (subduction).")],
 2: [("glue", "Graph: age vs. distance", "D2-C Graph grid", 270), ("glue", "Color North America", "D2-D North America ages and 5-box strip", 280), ("note", "Add two rows to your Unit CER page (U-1): the ocean pattern and the continent pattern.")],
 3: [("glue", "45 cm Earth timeline", "D3-B Timeline table and old materials", 330), ("draw", "Your timeline strip", "Tape your 45 cm strip here and label each event.", 110, "strip marked at 0, 1, 5, 10, 43, and 45 cm"),
     ("lines", "Exit ticket", 3, "Meteorites and moon rocks have barely changed, so they keep the early record; Earth's early rocks were recycled."), ("note", "Add a row to your Unit CER page (U-1) about meteorites, moon rocks, or zircons.")],
 4: [("glue", "SketchNotes checklist", "D4-C SketchNotes checklist", 150), ("draw", "SketchNotes: notes", "Half a page: the life of ocean crust and how continents grow.", 170, "crust is made at a ridge, moves about 2.5 cm a year, and sinks at a trench in under 200 million years; continents grow outward from an ancient core"),
     ("draw", "Sensemaking: cross-section", "Draw a ridge, moving plate, trench, volcanic arc, and a continent with a younger edge. Label the densities and add a carbon arrow.", 270, "ridge, plate arrows, trench, volcanic arc, continent with a younger edge, 3.0 and 2.7 g/cm³ labels, carbon arrow down and back up"),
     ("note", "Add a row to your Unit CER page (U-1) about density or continental growth.")],
 5: [("glue", "Hawaii and GPS", "D5-B Hawaii and GPS table", 200), ("draw", "Pangaea puzzle", "Tape your best fit here.", 70, "South America fits Africa; Mesosaurus and Glossopteris marked on both"),
     ("glue", None, "D5-C Fossil table", 90), ("glue", "Evaluate the evidence", "D5-D Evaluate-the-evidence table", 150)],
 6: [("glue", "Peer feedback", "D6-D Star and step", 110), ("glue", "Part B: Earth's story", "D6-B Evidence cards, in order from oldest to newest", 240), ("glue", "Story frames", "D6-C Part B story frames", 170),
     ("note", "Mark every row of your Unit CER page (U-1) that you used today.")],
 7: [("vocab8",), ("lines", "Before the CSA, I will study", 5, "My lowest targets. I will reread my notebook, redo the CFA questions I missed, and review the vocabulary.")],
}

def nb_page(d, side, H, P, k):
    title, focus = L.DAYS[d]["title"], L.DAYS[d]["focus"]
    left = side == "L"
    head = f"<div class='top'><span>Unit 3.1 · Day {d} · {DATES[d]}</span><span>{'Teacher ' if k else ''}{'Left' if left else 'Right'} page</span></div><div class='name'>Name ______________________________ Period ______ Date ____________</div>"
    t = f"<h1>{e(title)}</h1><div class='focus'><b>Focus question:</b> {e(focus)}</div>" if left else f"<h1 class='cont'>{e(title)} (continued)</h1>"
    body = "".join(block(b, H, P, k) for b in (LEFT if left else RIGHT)[d])
    return f"<div class='page'><div class='frame'>{head}{t}{body}</div></div>"

def notebook(H, k):
    P = pieces(True)
    return "".join(nb_page(d, s, H, P, k) for d in range(1, 8) for s in "LR")

# ---------------------------------------------------------------- printables and key
def cover(k):
    P = pieces(k)
    rows = "".join(f"<tr><td>Day {d}</td><td>{e(t)}</td><td>Glue in · {m.lower()}</td><td>{c}</td></tr>" for _, d, m, t, _, _, c in P)
    name = "Teacher Key" if k else "Printables"
    intro = ("Answers for every printable, plus the answer notes from each lesson. Student versions are in Unit31_Printables.pdf." if k else
             "Every table students only copy or fill in is printed here, so they do not spend class time drawing it. Cut each piece on the dashed line and glue it into the matching \"Glue in\" box on that day's notebook setup page (Unit31_Student_Notebook.pdf). Each piece is the same size as its box. Print on white paper, black ink only.")
    return (f"<div class='cut cover'><h1>Unit 3.1 {name}: Age of the Earth</h1><p>{intro}</p><table><tr><th>Day</th><th>Printable</th><th>Use</th><th>Copies</th></tr>{rows}</table>"
            "<p>Day 8 (CSA) needs nothing glued in. Not printed here: the world map with latitude and longitude lines (Day 1), the continent cut-outs for the Pangaea puzzle (Day 5), and the 45 cm adding-machine tape strips (Day 3).</p></div>")

def key_notes():
    out = ""
    for d in range(1, 8):
        items = "".join(f"<li>{re.sub(r'<[^>]+>', '', x)}</li>" for x in L.TEACHER[d].get("key", []))
        out += f"<div class='knote'><h2>Day {d}: {e(L.DAYS[d]['title'])}</h2><ul>{items}</ul></div>"
    return out

def printables(k):
    return cover(k) + "".join(piece_html(p, k) for p in pieces(k)) + (key_notes() if k else "")

if __name__ == "__main__":
    o = Path(sys.argv[1]); o.mkdir(parents=True, exist_ok=True)
    H = measure(); print("piece heights (px):", H)
    for k, name in ((False, "Student_Notebook"), (True, "Teacher_Notebook")):
        body = notebook(H, k)
        bad = [x for x in overflow(body) if x[1] > 0]
        if bad: print("OVERFLOW", name, bad)
        pdf(body, o / f"Unit31_{name}.pdf")
    pdf(printables(False), o / "Unit31_Printables.pdf", "0.5in 1.03in")
    pdf(printables(True), o / "Unit31_Printables_Teacher_Key.pdf", "0.5in 1.03in")
    print("done")
