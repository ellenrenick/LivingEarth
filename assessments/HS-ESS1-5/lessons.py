"""Student pages, teacher pages, and extra assignments for Unit 3.1 Age of the Earth.

Content only. canvas_lessons.py turns these into Canvas pages and a module.
All numbers are real or simplified from real values; simplified ones are labeled.

Day map (targets from the team workbook):
  1 Where Did the Old Ocean Floor Go?          ESS1-5.1  (launch, plates and boundaries)
  2 Reading Rock Ages                          ESS1-5.2  (CFA 5.1 opens the day)
  3 Reading Deep Time and Early Earth          ESS1-6.1, ESS1-6.2  (CFA 5.2 opens the day; ESS1-6 has no CFAs)
  4 Why the Ocean Is Young, the Continents Old ESS1-5.3  (no CFA opens the day)
  5 Evidence for Moving Crust                  ESS1-5.4  (CFA 5.3 opens the day)
  6 Evaluate the Theory, Tell Earth's Story    ESS1-5.5, ESS1-6.3  (CFA 5.4 opens the day)
  7 Review Day (CFA 5.5 if not yet taken)
  8 Unit 3.1 CSA (priority targets ESS1-5.1 to 5.5 only)
"""

import questions as Q

UNIT_TITLE = "Unit 3.1: Age of the Earth (HS-ESS1-5, HS-ESS1-6)"
DRIVING = "Earth is 4.5 billion years old, so why is the ocean floor so young, and where did the rest of Earth's early record go?"

TARGET_TEXT = {c: t for c, (_, t) in Q.TARGETS.items()}

BOX = "background:#eef5fb;border-left:5px solid #2b6cb0;padding:10px 14px;margin:12px 0"
TBOX = "background:#fff7e6;border-left:5px solid #c05621;padding:10px 14px;margin:12px 0"
TBL = 'border="1" cellpadding="6" style="border-collapse:collapse"'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f"<table {TBL}><tbody><tr>{h}</tr>{r}</tbody></table>"


def blank_table(head, nrows):
    return table(head, [["<br><br>"] * len(head) for _ in range(nrows)])


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ol(items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def student_html(day, day_title, focus, targets, notebook, parts, absent_extra=""):
    tl = "".join(f"<li><strong>{c}</strong> {TARGET_TEXT[c]}</li>" for c in targets) if targets else "<li>Launch day: you will work toward all eight unit targets.</li>"
    out = [
        f'<div style="{BOX}"><p><strong>Day {day}</strong> · {UNIT_TITLE}</p>'
        f"<p><strong>Driving question:</strong> {DRIVING}</p>"
        f"<p><strong>Focus question:</strong> {focus}</p><p><strong>Learning target{'s' if len(targets) > 1 else ''}:</strong></p><ul>{tl}</ul></div>",
        "<h2>Notebook setup</h2>"
        f'<div style="{BOX}"><p><strong>Before the lesson:</strong></p>{ol(notebook)}'
        "<p><em>Your notebook is your answer sheet for this lesson. Keep it neat; your teacher will check it.</em></p></div>",
    ]
    for i, (title, body) in enumerate(parts, 1):
        out.append(f"<hr><h2>Part {i}: {title}</h2>{body}")
    out.append("<hr><p><strong>If you were absent:</strong> complete the notebook pages above using this page, and take any CFA listed on it. "
               f"Your teacher will tell you which materials to borrow.{absent_extra}</p>")
    return "\n".join(out)


def teacher_html(day, day_title, targets, student_url, glance, materials, agenda, notes, key, supports):
    t = ", ".join(targets) if targets else "launch"
    out = [
        f'<div style="{TBOX}"><p><strong>Teacher page · keep unpublished.</strong> Students never see this page.</p>'
        f'<p><strong>Day {day}</strong> · Targets: {t} · <a href="{student_url}">Student page</a></p></div>',
        f"<h2>At a glance</h2><p>{glance}</p>",
        f"<h2>Materials</h2>{ul(materials)}",
        "<h2>Agenda (45 minutes)</h2>" + table(["Min", "What happens"], agenda),
        f"<h2>Teaching notes</h2>{ul(notes)}",
        f"<h2>Answer key</h2>{ul(key)}",
        f"<h2>Supports</h2><p>{supports}</p>",
    ]
    return "\n".join(out)


def cfa_part(codes, when="now"):
    """The 'Start with a CFA' block used at the top of Days 2 to 6."""
    names = "".join(f"<li><strong>Unit 3.1 CFA {c}: {Q.TARGETS[c][0]}</strong></li>" for c in codes)
    many = "each CFA" if len(codes) > 1 else "the CFA"
    return (f"<p>Take {'these CFAs' if len(codes) > 1 else 'this CFA'} on Canvas {when} (5 questions each):</p><ul>{names}</ul>"
            f"<p>If you score below 3 out of 4 on {many} (fewer than 4 of 5 correct), a review for that target will open for you.</p>")


def lab(title, mins, materials, steps, after=""):
    """A lab block: materials line, short numbered steps, then questions or a record table."""
    return (f"<p><strong>{title} · {mins} min · with your group</strong></p>"
            f"<p><strong>Materials:</strong> {materials}</p>{ol(steps)}{after}")


VOCAB = ["lithosphere (plate)", "plate boundary (divergent, convergent, transform)", "mid-ocean ridge", "subduction", "trench",
         "magnetic reversal", "craton (a continent's ancient core)", "impact crater"]
VOCAB_NOTE = ("<p><strong>Vocabulary (homework):</strong> make a Frayer card for each of the 8 words as they come up. Finish them by Day 7. "
              "Keep each card short: a picture, a definition in your own words, and one example.</p>")

# ===================================================================== DAY 1
OCEAN_AGES = table(["Place on the ocean floor", "Age of the rock"], [
    ["Right at the Mid-Atlantic Ridge", "0 (forming now)"],
    ["Middle of the Atlantic, about 2,000 km from the ridge", "about 80 million years"],
    ["Atlantic seafloor next to the east coast of North America", "about 180 million years"],
    ["Right at the East Pacific Rise", "0 (forming now)"],
    ["Western Pacific, east of Japan (the oldest on Earth)", "about 180 million years"],
])
LAND_AGES = table(["Continental material", "Where", "Age"], [
    ["Oldest mineral (a zircon crystal)", "Jack Hills, Western Australia", "about 4.4 billion years"],
    ["Oldest known rock (Acasta Gneiss)", "Northwest Territories, Canada", "about 4.0 billion years"],
    ["Very old rock (Isua belt)", "Greenland", "about 3.8 billion years"],
    ["Oldest widely accepted fossils (stromatolites)", "Western Australia", "about 3.5 billion years"],
])

SITES = [
    ("Mount St. Helens, Washington, USA", "volcano", "46.2° N", "122.2° W"),
    ("Mount Fuji, Japan", "volcano", "35.4° N", "138.7° E"),
    ("Popocatépetl, Mexico", "volcano", "19.0° N", "98.6° W"),
    ("Hekla, Iceland", "volcano", "64.0° N", "19.7° W"),
    ("Erta Ale, Ethiopia", "volcano", "13.6° N", "40.7° E"),
    ("Tohoku, Japan (2011, magnitude 9.1)", "earthquake", "38.3° N", "142.4° E"),
    ("Maule, Chile (2010, magnitude 8.8)", "earthquake", "35.9° S", "72.7° W"),
    ("Haiti (2010, magnitude 7.0)", "earthquake", "18.4° N", "72.5° W"),
    ("Turkey (2023, magnitude 7.8)", "earthquake", "37.2° N", "37.0° E"),
    ("Kīlauea, Hawaiʻi, USA", "volcano", "19.4° N", "155.3° W"),
]
SITES_KEY = {
    "Mount St. Helens": "convergent (Juan de Fuca plate subducting under North America)",
    "Mount Fuji": "convergent (subduction)",
    "Popocatépetl": "convergent (Cocos plate subducting under North America)",
    "Hekla": "divergent (Mid-Atlantic Ridge on land, with a hot spot)",
    "Erta Ale": "divergent (Afar rift)",
    "Tohoku": "convergent (Pacific plate subducting under Japan)",
    "Maule": "convergent (Nazca plate subducting under South America)",
    "Haiti": "transform (strike-slip fault)",
    "Turkey": "transform (East Anatolian Fault)",
    "Kīlauea": "NOT at a plate boundary: a hot spot in the middle of the Pacific plate",
}
SITE_TABLE = table(["Site", "Type", "Latitude", "Longitude"], [[s, t, la, lo] for s, t, la, lo in SITES])
BOUNDARY_RECORD = table(["Boundary", "What the plates did", "What formed", "Real example"], [
    ["Divergent", "<br><br>", "<br><br>", "<br>"], ["Convergent", "<br><br>", "<br><br>", "<br>"], ["Transform", "<br><br>", "<br><br>", "<br>"]])

DAY1 = dict(
    title="Where Did the Old Ocean Floor Go?",
    focus="How old is the ocean floor compared with the continents, and how do moving plates make and destroy it?",
    targets=["ESS1-5.1"],
    notebook=[
        "Title: <strong>D1 Where Did the Old Ocean Floor Go?</strong>. Start your table of contents.",
        "Draw a 2-column I notice / I wonder table.",
        "Start your <strong>Unit CER</strong> on a new page: the question <em>Why is the seafloor so much younger than the continents?</em>, your first claim, and a 3-column evidence log (Day · Evidence · What it shows). You will add a row every day.",
        "Leave room for your plotted world map and a 3-row boundary table.",
    ],
    parts=[
        ("Hook: the mystery (8 min)", "<p>Earth is about 4.5 billion years old. Scientists measured the age of rock on the ocean floor and on the continents.</p>"
            "<h3>Ocean floor</h3>" + OCEAN_AGES + "<h3>Continents and life</h3>" + LAND_AGES +
            "<ol><li>Write what you <strong>notice</strong> and what you <strong>wonder</strong> in your table.</li>"
            "<li>Write your first claim for the Unit CER in one sentence: <strong>Why is the seafloor so much younger than the continents?</strong> It is fine if it is wrong; we will revise it.</li></ol>"),
        ("Lab A: Plot the pattern (13 min)", lab("Plot earthquakes and volcanoes", 13,
            "a world map with latitude and longitude, 2 colored pencils, the plate boundaries map on the slide",
            ["Plot each site with a <strong>red dot</strong> for a volcano and a <strong>blue X</strong> for an earthquake. Share the work: each partner plots five.",
             "Look at your finished map. Do the points land in lines or at random?",
             "One site does not fit the pattern. Circle it. (It is a hot spot in the middle of a plate.)"],
            SITE_TABLE + "<p><strong>Check:</strong> The points make ______ . They match the edges of the ______ .</p>")),
        ("Lab B: Plate boundary models (19 min)", lab("Model the three boundaries with clay", 19,
            "2 pieces of foam sheet or cardboard (the plates), red, blue, and tan modeling clay, a paper towel",
            ["<strong>Divergent:</strong> Put the two plates edge to edge. Press a ridge of red clay into the gap. Slowly pull the plates apart and add more red clay in the gap. Sketch it and label the arrows. New crust forms at a <strong>mid-ocean ridge</strong>.",
             "<strong>Convergent:</strong> Put a blue clay slab (ocean crust) on the end of one plate and a tan clay block (continent) on the other. Push the plates together. Watch the blue slab slide under. Sketch it. The deep groove is a <strong>trench</strong> and the sinking is <strong>subduction</strong>. Push a bit of red clay up behind the block to show volcanoes.",
             "<strong>Transform:</strong> Lay a line of tan clay across both plates. Slide the plates past each other. Sketch the broken line. Earthquakes happen here.",
             "Fill in the table below with your group."],
            BOUNDARY_RECORD + "<p><strong>Think:</strong> Where is ocean crust <em>made</em>? Where is it <em>destroyed</em>?</p>")),
        ("Wrap-up (5 min)", "<ol><li>Look at your first claim. Add the words <strong>ridge</strong> and <strong>trench</strong> to it if they help.</li>"
            "<li><strong>Exit ticket:</strong> Where is ocean crust made, and where does it sink back down?</li></ol>" + VOCAB_NOTE),
    ],
)

# ===================================================================== DAY 2
SPREAD = table(["Distance from ridge (km)", "Crust age (million years)"], [
    ["0", "0"], ["500", "20"], ["1,000", "40"], ["1,500", "60"], ["2,000", "80"], ["2,500", "100"], ["3,000", "120"],
])
SEAFLOOR_KEY = table(["Age (million years)", "Color"], [
    ["0", "red"], ["20", "orange"], ["40", "yellow"], ["60", "green"], ["80", "blue"], ["100", "purple"], ["120", "dark purple"]])
NA_AGES = table(["Region of North America", "Direction and distance from the central core (km)", "Age of the crust"], [
    ["Pacific Coast Ranges", "west, about 2,800", "about 50 million years"],
    ["Rocky Mountain region", "west, about 1,800", "about 150 million years"],
    ["Canadian Shield (the central core)", "0", "about 2.7 billion years"],
    ["Grenville Province (Great Lakes to Quebec)", "east, about 1,200", "about 1.1 billion years"],
    ["Appalachian Mountains", "east, about 2,000", "about 400 million years"],
])

DAY2 = dict(
    title="Reading Rock Ages",
    focus="What patterns do the ages of ocean crust and continental crust follow?",
    targets=["ESS1-5.2"],
    notebook=[
        "Title: <strong>D2 Reading Rock Ages</strong>. Add it to your table of contents.",
        "Leave room for a row of 13 boxes, a small graph, and a row of 5 boxes.",
        "<strong>Unit CER evidence log:</strong> you will add two rows today.",
    ],
    parts=[
        ("Start with a CFA: ESS1-5.1 (8 min)", cfa_part(["ESS1-5.1"])),
        ("Warm-up (3 min)", "<p>A ship pulls up seafloor rock right at the Mid-Atlantic Ridge and another sample near the coast of Brazil. Which rock is older? Say why.</p>"),
        ("Lab A: Color the seafloor (12 min)", lab("Color a map of the seafloor", 12,
            "colored pencils, a ruler",
            ["Draw a row of <strong>13 boxes</strong> across your page. Label the middle box <strong>RIDGE</strong>. Label the boxes to the left and right 500, 1,000, 1,500, 2,000, 2,500, and 3,000 km.",
             "The age in each box is the age from the table below. Color each box with the color key. The two sides match.",
             ],
            SPREAD + SEAFLOOR_KEY +
            ol(["Where is the youngest color? Where is the oldest color?",
                "How do the colors on the left compare with the colors on the right?",
                "Write one sentence that tells the pattern: As you move away from the ridge, the crust gets ______ ."]))),
        ("Lab B: Graph the pattern (9 min)", lab("Graph age against distance", 9,
            "graph paper, a ruler, a pencil",
            ["Put <strong>distance from the ridge</strong> on the x-axis (0 to 3,000 km) and <strong>crust age</strong> on the y-axis (0 to 120 million years). Plot the 7 points and connect them.",
             "Pick two points on your line. Rate = distance &divide; time. (500 km in 20 million years is 25 km per million years. 1 km per million years = 0.1 cm per year.)",
             ],
            ol(["What is the rate in cm per year? Compare it with something that grows about that fast (fingernails).",
                "Use your line to predict the age of crust 3,500 km from the ridge."]))),
        ("Lab C: Color North America (10 min)", lab("Color the continent by age", 10,
            "colored pencils",
            ["Draw a row of <strong>5 boxes</strong> from west to east. Write the region names from the table in order.",
             "Color the oldest region <strong>dark brown</strong>. Color the youngest region <strong>light yellow</strong>. Choose three in-between colors for the others.",
             ],
            NA_AGES +
            ol(["Where is the oldest crust? How does the age change as you move away from it, east and west?",
                "How is this pattern like the pattern in the ocean, and how is it different?"]))),
        ("Wrap-up (3 min)", "<p>Add <strong>two rows</strong> to your Unit CER evidence log: one for the ocean pattern and one for the continent pattern. Use a number from today.</p>"
            "<p>Tomorrow starts with <strong>Unit 3.1 CFA ESS1-5.2: Reading rock ages</strong> (5 questions). Study your colored boxes and graph.</p>"),
    ],
)

# ===================================================================== DAY 3
OLD = table(["Material", "Where", "Age"], [
    ["Meteorite fragments (Canyon Diablo)", "Arizona, USA", "about 4.56 billion years"],
    ["Moon rocks from the lunar highlands", "Brought back by Apollo", "up to about 4.4 billion years"],
    ["Oldest Earth mineral (zircon)", "Jack Hills, Australia", "about 4.4 billion years"],
    ["Oldest known Earth rock (Acasta Gneiss)", "Canada", "about 4.0 billion years"],
    ["Oldest widely accepted fossils (stromatolites)", "Western Australia", "about 3.5 billion years"],
    ["Oldest ocean floor", "Western Pacific and Atlantic margins", "about 180–200 million years"],
])
TIMELINE = table(["Event", "Age (millions of years ago)", "Position on the 45 cm strip (cm)"], [
    ["Earth forms (left end)", "4,500", "0"],
    ["Oldest mineral on Earth (zircon)", "4,400", "1"],
    ["Oldest known rock", "4,000", "<br>"],
    ["Oldest fossils", "3,500", "<br>"],
    ["Oldest ocean floor", "200", "<br>"],
    ["Today (right end)", "0", "45"],
])
CRATER_RECORD = table(["Test", "Drop height", "Crater width (cm)"], [
    ["Small marble", "30 cm", "<br>"], ["Small marble", "60 cm", "<br>"], ["Large marble", "30 cm", "<br>"], ["Large marble", "60 cm", "<br>"]])

DAY3 = dict(
    title="Reading Deep Time and Early Earth",
    focus="How do scientists know how old Earth is, and why do meteorites and moon rocks tell Earth's age better than Earth rocks do?",
    targets=["ESS1-6.1", "ESS1-6.2"],
    notebook=[
        "Title: <strong>D3 Reading Deep Time</strong>. Add it to your table of contents.",
        "Leave room for a 4-row crater table, two drawings of a crater tray, and the timeline table.",
        "<strong>Unit CER evidence log:</strong> you will add one row about the age of meteorites, moon rocks, or Earth's oldest minerals.",
    ],
    parts=[
        ("Start with a CFA: ESS1-5.2 (8 min)", cfa_part(["ESS1-5.2"])),
        ("Hook and key ideas (5 min)", "<p>The oldest ocean floor is only about 200 million years old, but scientists say Earth is about 4.5 billion years old. How could anyone know?</p>"
            "<ul><li>Scientists find the age of rock using atoms that change at a steady rate, like a clock. This is called <strong>radiometric dating</strong>.</li>"
            "<li>The oldest rock found on Earth is about <strong>4.0 billion</strong> years old, which is <em>younger</em> than Earth itself. Earth's first rocks were destroyed or recycled.</li>"
            "<li><strong>Meteorites</strong> (pieces of asteroids) and <strong>moon rocks</strong> have hardly changed. They keep the early record.</li></ul>"
            "<p>Write one reason scientists use meteorites and moon rocks to find the age of the solar system.</p>"),
        ("Lab A: Make craters (15 min)", lab("Impact crater lab", 15,
            "a tray with a layer of flour topped with a little cocoa powder, 2 marbles (small and large), a ruler, newspaper under the tray, safety goggles",
            ["Smooth the flour. Drop the small marble from 30 cm. Measure the crater width. Repeat from 60 cm, then do the same with the large marble. Record the widths.",
             "<strong>Old surface:</strong> Without smoothing, drop both marbles 4 times each from random heights. Sketch what the tray looks like.",
             "<strong>Young surface:</strong> Smooth the tray (this is lava or erosion renewing the surface). Drop each marble once. Sketch it."],
            CRATER_RECORD +
            ol(["Which tray looks older? How can you tell?",
                "The Moon highlands are covered with craters, but Earth has only about 190 known craters. Earth was hit just as often. Why does Earth show so few?"]))),
        ("Lab B: Build a 45 cm timeline of Earth (13 min)", lab("Earth timeline strip", 13,
            "a 45 cm strip of adding-machine tape (or paper), a ruler, a pencil, colored pencils",
            ["Mark the left end <strong>Earth forms</strong> and the right end <strong>today</strong>. Scale: <strong>1 cm = 100 million years</strong>.",
             "Use position = (4,500 &minus; age in millions of years) &divide; 100. Fill in the table.",
             "Mark and label each event on your strip. Color the part of the strip covered by the ocean floor that is still here."],
            TIMELINE + OLD +
            ol(["How much of the 45 cm is covered by ocean floor that still exists?",
                "Why is the oldest Earth rock younger than Earth?",
                "The oldest fossils are in continental rock. Why are there no fossils that old in the ocean floor?"]))),
        ("Wrap-up (4 min)", "<p>Add a row to your Unit CER evidence log about the age of meteorites, moon rocks, or Earth's oldest minerals.</p>"
            "<p><strong>Exit ticket:</strong> Why do scientists use meteorites and moon rocks, not Earth rocks, to find the age of the solar system?</p>"),
    ],
)

# ===================================================================== DAY 4
DENSITY_RECORD = table(["Block", "Mass (g)", "Volume (cm³)", "Density (g/cm³) = mass ÷ volume", "Sinks or floats?"], [
    ["Wood block (stand-in for a continent)", "<br>", "<br>", "<br>", "<br>"], ["Clay block (stand-in for an old, cold ocean plate)", "<br>", "<br>", "<br>", "<br>"]])

DAY4 = dict(
    title="Why the Ocean Is Young and the Continents Old",
    focus="How is ocean crust made, grown, and recycled, and how do continents grow and survive?",
    targets=["ESS1-5.3"],
    notebook=[
        "Title: <strong>D4 Why the Ocean Is Young, the Continents Old</strong>. Add it to your table of contents.",
        "Leave room for guided notes (half a page), a density table, and a full page for SketchNotes.",
        "<strong>Unit CER evidence log:</strong> add one row about density or continental growth.",
    ],
    parts=[
        ("Warm-up (3 min)", "<p>You know the ocean floor is under 200 million years old. Where does the old ocean crust go?</p>"),
        ("Guided notes (7 min)", "<p>Fill in the blanks as your teacher shows each idea.</p>"
            + ol(["Old ocean crust is made at a ______ and moves away about 2.5 cm a year (25 km per million years).",
                  "A piece of crust travels 3,000 km. Time = 3,000 &divide; 25 = ______ million years. In 200 million years it travels 200 &times; 25 = ______ km, so it reaches a trench and sinks. No ocean floor is older than about ______ million years.",
                  "Ocean crust has a density of about <strong>3.0 g/cm³</strong>. Continental crust is about <strong>2.7 g/cm³</strong>. The ______ plate sinks (<em>subduction</em>).",
                  "Each continent has an ancient core. Volcanic arcs and pieces of crust are added to its edge over time, like rings on a tree. The edge is ______ than the core."])),
        ("Lab: Sink or float (17 min)", lab("Density of plates", 17,
            "a clear tub of water (the &ldquo;mantle&rdquo;), a wood block, a clay block, a balance, a ruler, paper towels",
            ["<strong>Predict:</strong> Which block will sink? Which will float? Write it down.",
             "Measure the mass of each block with the balance. Measure the length, width, and height and find the volume (l &times; w &times; h).",
             "Calculate density = mass &divide; volume. Water has a density of 1.0 g/cm³.",
             "Place each block on the water. Record what happened. Then push the two blocks toward each other under the water and watch which one dives under the other.",
             "Draw what you saw in your notebook."],
            DENSITY_RECORD +
            ol(["Which block is denser? Which one sank?",
                "In this model, which block is like the ocean plate and which is like the continent? What does the denser one do when they meet?",
                "Model limits: both real crusts are denser than water. What stands in for the mantle in this model?"]))),
        ("SketchNotes (15 min)", "<p><strong>Half page of notes:</strong> the life of ocean crust (made, moves, sinks) and how continents grow. <strong>One page of sensemaking:</strong> draw a cross-section with a ridge, an ocean plate moving away, a trench, a volcanic arc, and a continent with an ancient core and a younger edge. Label density and add an arrow showing where a plankton shell's carbon goes (it rides the plate down; some returns as CO₂ from volcanoes).</p>"
            "<p>Take a photo of your SketchNotes and turn them in on Canvas: <strong>Lesson 4: SketchNotes</strong>.</p>"),
        ("Wrap-up (3 min)", "<p>Add a row to your Unit CER evidence log about density or continental growth.</p>"
            "<p>Tomorrow starts with <strong>CFA ESS1-5.3: Why ocean crust is young and continents are old</strong> (5 questions). Study your SketchNotes tonight.</p>"),
    ],
)

# ===================================================================== DAY 5
HAWAII = table(["Volcano or island", "Distance northwest of Kīlauea (km)", "Age of its oldest rock (million years)"], [
    ["Kīlauea (Hawaiʻi Island, active now)", "0", "0"],
    ["Kauaʻi", "about 500", "about 5"],
    ["Midway Atoll", "about 2,500", "about 28"],
])
FOSSILS = table(["Organism", "What it was", "Found in"], [
    ["<em>Mesosaurus</em>", "freshwater reptile", "South America and southern Africa"],
    ["<em>Glossopteris</em>", "seed fern (heavy seeds)", "South America, Africa, India, Australia, Antarctica"],
    ["<em>Lystrosaurus</em>", "land animal", "Africa, India, Antarctica"],
])
EVIDENCE_EVAL = table(["Line of evidence", "Measured numbers?", "Past or present motion?", "Independent of the others?", "Strength (1–4)"], [
    ["Rock ages across a ridge", "<br>", "<br>", "<br>", "<br>"],
    ["Magnetic stripes", "<br>", "<br>", "<br>", "<br>"],
    ["GPS and Hawaiian island ages", "<br>", "<br>", "<br>", "<br>"],
    ["Matching fossils and rocks", "<br>", "<br>", "<br>", "<br>"],
])
STRIP_TABLE = table(["Band (from the end you push first)", "Color", "Length", "Age it represents"], [
    ["1", "Reversed (blue)", "3.4 cm", "about 3.6–5.3 million years"],
    ["2", "Normal (red)", "2.0 cm", "about 2.6–3.6 million years"],
    ["3", "Reversed (blue)", "3.6 cm", "about 0.8–2.6 million years"],
    ["4", "Normal (red)", "1.6 cm", "0–0.8 million years (youngest)"]])

DAY5 = dict(
    title="Evidence for Moving Crust",
    focus="How strong is the evidence that the crust has moved and is still moving?",
    targets=["ESS1-5.4"],
    notebook=[
        "Title: <strong>D5 Evidence for Moving Crust</strong>. Add it to your table of contents.",
        "Leave room to tape in your paper stripes, a small calculation, a puzzle sketch, and the evidence table.",
        "<strong>Unit CER evidence log:</strong> add one row about the strongest evidence you saw today.",
    ],
    parts=[
        ("Start with a CFA: ESS1-5.3 (8 min)", cfa_part(["ESS1-5.3"])),
        ("Warm-up (2 min)", "<p>How could a scientist show that the seafloor moved long ago? How could they show it is moving <em>today</em>? Write one idea for each.</p>"),
        ("Lab A: Magnetic stripes (12 min)", lab("Paper model of seafloor spreading", 12,
            "two strips of paper (12 cm), red and blue pencils, scissors, a folded sheet of paper",
            ["Color both strips with the table below (2 cm = 1 million years). Start at the end you will push through first. This is the <em>oldest</em> crust.",
             "Cut a slit in the folded paper. The slit is the <strong>mid-ocean ridge</strong>.",
             "Put the strips back to back and push them up through the slit. Pull them slowly apart, one to each side.",
             "Tape the result in your notebook and label the youngest and the oldest crust."],
            STRIP_TABLE +
            ol(["What does a pair of mirror-image stripe patterns tell you about how the crust formed?",
                "Earth's magnetic field has flipped many times. How does the crust record the flips? (This is a <strong>magnetic reversal</strong> record.)"]))),
        ("Lab B: Measured motion (7 min)", lab("Hawaii and GPS", 7,
            "a calculator or your notebook",
            ["GPS stations measure plate motion directly: about 7 to 8 cm per year for the Pacific plate near Hawaii, and about 2 cm per year across the ridge in Iceland.",
             "The Hawaiian Islands formed as the Pacific plate moved over a hot spot. Use the table. Rate = distance &divide; time. (1 km per million years = 0.1 cm per year.)"],
            HAWAII +
            ol(["Find the rate from Kīlauea to Kauaʻi: 500 km &divide; 5 million years = ______ km per million years = ______ cm per year.",
                "Find the rate to Midway. Compare both rates with the GPS value. What do you notice?"]))),
        ("Lab C: Fit the continents (9 min)", lab("Pangaea puzzle", 9,
            "cut-out continent shapes (South America, Africa, India, Australia, Antarctica) or the Pangaea puzzle handout, scissors, tape",
            ["Fit the continents together like a puzzle. Tape the best fit into your notebook.",
             "Mark where each fossil lived, using the table. The fossils form a line across the joined continents."],
            FOSSILS +
            ol(["<em>Mesosaurus</em> lived in fresh water and <em>Glossopteris</em> had heavy seeds. Why are they good evidence that the lands were once joined?",
                "What can fossils <strong>not</strong> tell you that GPS can?"]))),
        ("Evaluate the evidence (6 min)", "<p>Fill in the table (yes/no, past/present, and a strength rating from 1 = weak to 4 = very strong).</p>" + EVIDENCE_EVAL +
            ol(["Which line is strongest for <em>current</em> motion? For <em>past</em> motion?",
                "Why does it make the case stronger when two independent methods (GPS and rock ages) agree?"]) +
            "<p>Tomorrow starts with <strong>CFA ESS1-5.4: Evidence for moving crust</strong> (5 questions). Study your evaluation table tonight.</p>"),
    ],
)

# ===================================================================== DAY 6
CER_FRAMES = ul([
    "<strong>Claim:</strong> Plate tectonics explains the ages of Earth's crustal rocks (very well / partly / poorly) because ______.",
    "<strong>Ocean evidence:</strong> The seafloor is youngest at the ______ and gets older with ______; the oldest ocean floor is only about ______ million years old.",
    "<strong>Continent evidence:</strong> Continental crust as old as ______ exists, and in North America the crust gets ______ toward the edges.",
    "<strong>Reasoning:</strong> Because ocean plates are ______ than continental crust, they ______ at subduction zones, while continents ______.",
    "<strong>Limit or counterclaim:</strong> One thing this evidence cannot show is ______. OR: Someone might say the ocean floor is young because ______. This does not fit the evidence because ______.",
])
CER_CHECK = ul(["The claim says how well the theory explains the ages and gives a cause.",
                "The evidence is specific (a number or a named pattern) and uses both ocean and continental crust.",
                "The reasoning explains <em>why</em> the evidence supports the claim.",
                "A limit or a counterclaim is addressed with evidence."])
STORY_FRAMES = ul([
    "About ______ billion years ago, ______ happened. The evidence is ______.",
    "About ______ billion years ago, ______ happened. The evidence is ______.",
    "About ______ billion years ago, ______ happened. The evidence is ______.",
    "Earth's earliest record is missing because ______.",
])
EVIDENCE_CARDS = table(["Evidence card", "What it shows"], [
    ["Meteorites: about 4.56 billion years", "The solar system formed about 4.56 billion years ago."],
    ["Moon highland rocks: up to about 4.4 billion years; heavily cratered", "Solid crust existed early; the early solar system had many impacts."],
    ["Earth's oldest zircons: about 4.4 billion years", "Solid crust and minerals had formed on Earth by then."],
    ["Oldest Earth rock (Acasta Gneiss): about 4.0 billion years", "Rock has survived for 4 billion years in the continents."],
    ["Oldest fossils (stromatolites): about 3.5 billion years", "Life existed by then."],
    ["Oldest ocean floor: about 200 million years", "Ocean crust is recycled; the early record is not on the ocean floor."],
])

DAY6 = dict(
    title="Evaluate the Theory, Tell Earth's Story",
    focus="How well does plate tectonics explain the ages of crustal rocks, and what story do ancient materials tell about Earth's formation?",
    targets=["ESS1-5.5", "ESS1-6.3"],
    notebook=[
        "Title: <strong>D6 Evaluate the Theory, Tell Earth's Story</strong>. Add it to your table of contents.",
        "Have your <strong>Unit CER evidence log</strong> open. You will use every row.",
        "Draw a 3-column bucket table (see Part 2).",
    ],
    parts=[
        ("Start with a CFA: ESS1-5.4 (8 min)", cfa_part(["ESS1-5.4"])),
        ("Sort your evidence (3 min)", "<p>Look at your evidence log. Sort each row into a bucket:</p>" +
            table(["The seafloor is young because…", "The continents are old because…", "The early record is missing because…"], [["<br><br>", "<br><br>", "<br><br>"]]) +
            "<p>Look back at your Day 1 claim. What would you change now?</p>"),
        ("Part A: Evaluate the theory, ESS1-5.5 (14 min)", "<p>Answer: <strong>How well does the theory of plate tectonics explain the ages of Earth's crustal rocks?</strong> Use the five sentence frames.</p>" + CER_FRAMES +
            "<p><strong>Data you may use:</strong> crust age goes from 0 to 120 million years across 3,000 km (2.5 cm per year); the oldest ocean floor is about 200 million years; the oldest continental mineral is about 4.4 billion years; North American crust is about 2.7 billion years at the core and about 400 million years in the Appalachians; ocean crust is about 3.0 g/cm³ and continental crust about 2.7 g/cm³; GPS and rock-age rates (2 and 2.5 cm per year).</p>"
            "<p>Submit your finished argument on Canvas: <strong>Unit 3.1 CER</strong> (Part A).</p>"),
        ("Peer feedback (5 min)", "<p>Trade with a partner. Check the list and write one &ldquo;star&rdquo; (something strong) and one &ldquo;step&rdquo; (something to improve). Then fix your own.</p>" + CER_CHECK),
        ("Part B: Earth's story card sort, ESS1-6.3 (12 min)", lab("Order the evidence", 12,
            "6 evidence cards (cut from the table), scissors, glue, a strip of paper",
            ["Cut out the six evidence cards.",
             "Put them in order from oldest to newest on a paper strip and glue them down.",
             "Under your strip, write the story with the frames (Part B of <strong>Unit 3.1 CER</strong> on Canvas)."],
            EVIDENCE_CARDS + STORY_FRAMES)),
        ("Wrap-up (3 min)", "<p>Take <strong>Unit 3.1 CFA ESS1-5.5: How well plate tectonics explains rock ages</strong> (5 questions) at the start of your next class or on the work day, as your teacher tells you. If you score below 3 out of 4, a review for that target will open for you.</p>"),
    ],
)

# ===================================================================== DAY 7
DAY7 = dict(
    title="Review Day",
    focus="Which targets do I still need to work on before the CSA?",
    targets=list(Q.TARGETS),
    notebook=[
        "Title: <strong>D7 Review Day</strong>. Add it to your table of contents.",
        "Copy the self-rating chart in Part 1 and fill it in.",
    ],
    parts=[
        ("Rate yourself", "<p>Rate each target from 1 (I need help) to 4 (I could teach it). Use your CFA scores to check your rating.</p>" +
            table(["Target", "My rating (1–4)", "My CFA score"], [[f"<strong>{c}</strong> {t}", "<br>", "<br>"] for c, t in TARGET_TEXT.items()])),
        ("Do the work that matches your scores", ol([
            "<strong>If you have not taken a CFA yet,</strong> take it now. This includes <strong>CFA ESS1-5.5</strong>. The CFAs are in this module on Canvas.",
            "<strong>If a Mastery Path review opened for you,</strong> complete it now (they are in this module). Study your notebook first, then answer the 3 written questions.",
            "<strong>If you do not have any reviews open,</strong> your teacher may assign you the Enrichment choice board. Check Canvas, or ask.",
            "<strong>Everyone:</strong> finish your 8 Frayer cards and make sure your Unit CER evidence log and your CER are complete.",
        ])),
        ("Vocabulary self-check", "<p>Cover the definitions on your Frayer cards. Explain each word aloud to a partner without reading: lithosphere, plate boundary, mid-ocean ridge, subduction, trench, magnetic reversal, craton, impact crater.</p>"),
        ("About the CSA", "<p>The <strong>Unit 3.1 CSA</strong> covers the five priority targets, <strong>ESS1-5.1 to ESS1-5.5</strong>. The three ESS1-6 targets are taught to support ESS1-5.3 and ESS1-5.5, but they have no CFAs and are not tested on the CSA. Study your notebook, your CFA results, and your reviews.</p>"),
    ],
)

# ===================================================================== DAY 8
DAY8 = dict(
    title="Unit 3.1 CSA",
    focus="Show what you know about the ages of Earth's crust.",
    targets=[c for c in Q.TARGETS if c.startswith("ESS1-5")],
    notebook=["Bring a pencil. You do not need your notebook for the CSA."],
    parts=[
        ("About the CSA", "<p>The Common Summative Assessment has <strong>16 questions</strong> on the five priority targets, ESS1-5.1 to ESS1-5.5: 14 multiple-choice, select-all, and true/false questions, and 2 written responses (an evaluation of evidence for seafloor spreading, and an evaluation of how well plate tectonics explains rock ages using data). Read each question carefully and use the data provided.</p>"),
        ("Take the CSA", "<p>Open <strong>Unit 3.1 CSA: Age of the Earth (HS-ESS1-5)</strong> on Canvas when your teacher says to begin.</p>"),
        ("When you finish", "<p>Check your written answers. Then work quietly on any missing Canvas work. If your score on a target is below a 3, you will have a chance to reassess after an intervention.</p>"),
    ],
)

# ===================================================================== extra assignments
LESSON1_ASSIGN = ("Lesson 1: Where Did the Old Ocean Floor Go?",
    "<p><strong>Focus question:</strong> How old is the ocean floor compared with the continents, and how do moving plates make and destroy it?</p>"
    "<p>Complete the Day 1 notebook pages from the lesson page: your I notice / I wonder table, your first claim, your plotted world map with the pattern answer, and your boundary sketches and table. Your teacher will check your notebook.</p>")
LESSON4_ASSIGN = ("Lesson 4: SketchNotes",
    "<p><strong>Focus question:</strong> How is ocean crust made, grown, and recycled, and how do continents grow and survive?</p>"
    "<p>Take a photo of your Day 4 SketchNotes (half page of notes and one page of sensemaking with a labeled cross-section) and upload it here.</p>"
    "<table border=\"1\" cellpadding=\"6\" style=\"border-collapse:collapse\"><tbody><tr><th>4</th><td>Notes describe the life of ocean crust and how continents grow. The cross-section correctly shows the ridge, a plate moving away, the trench, the volcanic arc, a continent with an ancient core and a younger edge, density labels, and an arrow for carbon.</td></tr>"
    "<tr><th>3</th><td>All parts are present with one small error or missing label.</td></tr>"
    "<tr><th>2</th><td>Some parts are missing or incorrect.</td></tr><tr><th>1</th><td>Few parts, or major errors.</td></tr></tbody></table>")
CER_ASSIGN = ("Unit 3.1 CER: How well does plate tectonics explain the ages of Earth's rocks?",
    "<p><strong>Part A question:</strong> How well does the theory of plate tectonics explain the ages of Earth's crustal rocks?</p>"
    "<p>Write your argument using the sentence frames from the Day 6 page. Use evidence from both ocean crust and continental crust. Type it in the text box or upload your notebook page.</p>" + CER_FRAMES +
    "<p><strong>Part B (ESS1-6.3):</strong> Tell the story of Earth's formation using the evidence cards and these frames.</p>" + STORY_FRAMES +
    "<h3>Scoring (4 points)</h3>" +
    table(["Score", "What it looks like"], [
        ["4", "Part A: a complete, accurate claim about how well plate tectonics explains the ages; at least two specific pieces of evidence including both ocean and continental crust; reasoning that connects the evidence to the process (made at ridges, destroyed at subduction zones, continents too buoyant to sink and growing at their edges); a limit or counterclaim is addressed. Part B: three or more events in order with ages and evidence, and an explanation of the missing record."],
        ["3", "Accurate claim; two specific pieces of evidence; reasoning present but incomplete or generic. Part B has events in order with evidence for two."],
        ["2", "Claim and one piece of evidence, or two vague pieces; reasoning missing or restates the evidence. Part B is incomplete."],
        ["1", "Claim only, or the claim and evidence are partly incorrect."],
        ["0", "Blank or off-task."]]))

ENRICH = ("Unit 3.1 Enrichment: Choice Board",
    f'<div style="{BOX}"><p><strong>Unit 3.1 Enrichment</strong> · {UNIT_TITLE}</p>'
    "<p>You showed that you understand the targets. Now take your thinking further. <strong>Choose ONE</strong> of the four options. Your product should use at least two numbers or facts from this unit.</p></div>"
    "<h2>Option 1: Life at the Ridge (biology)</h2>"
    "<p>Hydrothermal vent communities live where the crust is brand new, with no sunlight.</p>"
    + ol(["Draw and label a food web for a vent community: hydrothermal fluid, chemosynthetic bacteria, tube worms, and one predator.",
          "Compare chemosynthesis with photosynthesis in a Venn diagram (energy source, where it happens, what the organism makes).",
          "At 2.5 cm per year, how long does it take new crust to move 1 km from the ridge? (Show the calculation.) Individual vents often last only years to decades. What does that tell you about why vent animals have to keep finding new vents?"]) +
    "<h2>Option 2: The Missing Record</h2>"
    "<p>Make a poster or slide that shows why the first 3 billion years of life are in continental rock and not in the ocean floor.</p>"
    + ol(["Draw a scaled timeline (1 cm = 100 million years) with Earth's formation, the oldest zircon, the oldest rock, the oldest fossils, and the oldest ocean floor. Label the positions.",
          "Explain, in 3 sentences, what happened to the ocean floor that formed before 200 million years ago.",
          "Suggest what part of the fossil record might be biased because of this."]) +
    "<h2>Option 3: Iceland, a Divergent Boundary on Land</h2>"
    "<p>Iceland sits on the Mid-Atlantic Ridge. The North American and Eurasian plates there move apart at about 2 cm per year.</p>"
    + ol(["Calculate how far apart the plates will move in 1 million years, in kilometers. In 50 years, in centimeters.",
          "Explain why Iceland has volcanoes and rift valleys instead of a deep trench.",
          "Predict how the ages of rock in Iceland change from the center of the island toward the coasts, and explain why."]) +
    "<h2>Option 4: A Planet Without Plate Tectonics</h2>"
    "<p>Mars appears not to have plate tectonics. Large parts of its southern highlands are heavily cratered and are thought to be about 3.7 billion years old or more.</p>"
    + ol(["Predict how the age of Mars's crust compares with the age of Earth's ocean floor. Explain using what you know about recycling of crust.",
          "Explain why scientists use rocks and craters from other planets and meteorites to learn about Earth's early history (ESS1-6).",
          "Write a short argument: &ldquo;Plate tectonics is the reason the ocean floor is young.&rdquo; What evidence from Earth and from Mars supports this claim?"]) +
    "<h2>How you will be scored (4 points)</h2>" +
    table(["Score", "What it looks like"], [
        ["4", "All parts are complete and accurate; uses at least two specific numbers or facts from the unit; reasoning is clear and goes beyond what we did in class."],
        ["3", "Mostly complete and accurate; one number or fact; reasoning is present."],
        ["2", "Some parts missing or inaccurate; little use of data."],
        ["1", "Little completed or major errors."]]))


# ===================================================================== teacher pages
TEACHER = {}
READING = "Reading support: the slides carry the directions in short steps; read each step aloud before students start. Students may answer orally to a partner first."

TEACHER[1] = dict(
    glance="Launch the phenomenon in 8 minutes (ocean floor under about 200 million years; continental material up to 4.4 billion), then two hands-on labs teach ESS1-5.1: students plot earthquakes and volcanoes to find plate boundaries (13 min), then model the three boundary types with clay (19 min). About 32 of 45 minutes are lab. No CFA today; CFA ESS1-5.1 opens Day 2.",
    materials=["Seafloor age map (NOAA NCEI Age of the Ocean Floor map or any labeled copy) to project", "World map with latitude and longitude (one per student) and a plate boundaries map to project",
               "Lab B per group of 3 to 4: 2 pieces of foam sheet or cardboard (about 10 × 15 cm), red, blue, and tan modeling clay, a paper towel",
               "Colored pencils (red and blue)", "Notebook paper"],
    agenda=[["0–8", "Hook: two age tables, notice and wonder, first claim (one sentence)"], ["8–21", "Lab A: plot the 10 sites and find the pattern (each partner plots five)"],
            ["21–40", "Lab B: clay models of divergent, convergent, and transform boundaries; sketch each and fill in the table"], ["40–45", "Wrap-up: revise the claim, exit ticket, hand out the vocabulary homework"]],
    notes=["Do not explain why crust is young yet. Collect wrong ideas (&ldquo;the ocean floor erodes away,&rdquo; &ldquo;the ocean is young&rdquo;) and revisit them on Day 6.",
           "A few small remnants of older crust exist in the Mediterranean (up to about 340 million years); they do not change the story and you can mention them if a student asks.",
           "Kīlauea is a deliberate exception (a hot spot inside a plate); it makes a good conversation, not a trick.",
           "Lab B pacing: about 5 minutes per boundary, then 4 minutes to fill in the table. Demonstrate the convergent model first because the sliding-under motion is the hardest to see.",
           "Vocabulary is now 8 words as homework Frayer cards (not class time): lithosphere, plate boundary, mid-ocean ridge, subduction, trench, magnetic reversal, craton, impact crater.",
           READING],
    key=["Sites and boundary type: " + "; ".join(f"{k}: {v}" for k, v in SITES_KEY.items()) + ".",
         "Pattern: sites form lines along plate boundaries; the Ring of Fire is the largest.",
         "Clay models: divergent — plates move apart, new crust forms at a mid-ocean ridge; convergent — the denser ocean slab slides under the continent, a trench forms, volcanoes rise; transform — plates slide past each other, the line breaks, earthquakes.",
         "Crust is made at mid-ocean ridges (divergent boundaries) and destroyed at trenches (subduction at convergent boundaries).",
         "Sample first claim: The ocean floor is young because it keeps getting renewed (accept any attempt; this is the baseline)."],
    supports="Give a pre-labeled map for students who struggle to plot coordinates. Pre-roll the clay. Let students answer orally to a partner before writing.",
)

TEACHER[2] = dict(
    glance="CFA ESS1-5.1 opens the day (8 min). Three short, hands-on map and graph labs follow: students color-code a seafloor strip by age (12 min), graph age against distance and find the rate (9 min), and color-code a strip of North America to find the matching pattern (10 min). CFA ESS1-5.2 opens Day 3.",
    materials=["Colored pencils", "Graph paper", "Rulers", "Seafloor age map to project (NOAA NCEI)", "A map of North American crust ages (USGS geologic provinces) to project (optional)", "Chromebooks for the CFA"],
    agenda=[["0–8", "CFA ESS1-5.1"], ["8–11", "Warm-up prediction"], ["11–23", "Lab A: color the seafloor strip"], ["23–32", "Lab B: graph age against distance; find the rate"],
            ["32–42", "Lab C: color the North America strip"], ["42–45", "Wrap-up: two evidence-log rows; preview the CFA"]],
    notes=["Rate arithmetic: 500 km in 20 million years = 25 km per million years = 2.5 cm per year. Convert with 1 km per million years = 0.1 cm per year.",
           "The target is reading and describing the pattern, not explaining it. Save the &lsquo;why&rsquo; for Days 3 to 5.",
           "North America table is simplified from geologic maps (ages when the crust was formed or added). Use the USGS provinces map if you have it.",
           "Hand out the graph with the axes already drawn and labeled if you want to save 2 minutes.",
           READING],
    key=["Prediction: the sample at the ridge is younger; the Brazil sample is older (up to about 120 million years old).",
         "Strip colors: red 0, orange 20, yellow 40, green 60, blue 80, purple 100, dark purple 120. The youngest color is at the ridge; the oldest is at the outer boxes; the left and right sides match.",
         "Pattern sentence: As you move away from the ridge, the crust gets older.",
         "Graph: a straight line through the origin. Slope 500 km per 20 million years = 25 km per million years = 2.5 cm per year (about the speed fingernails grow).",
         "3,500 km from the ridge: 3,500 ÷ 25 = 140 million years.",
         "Continents: the oldest crust is in the central core (Canadian Shield, about 2.7 billion years); the crust gets younger moving outward both east and west. Like the ocean, age changes with distance from a center; unlike the ocean, the ages are billions of years and the pattern is not the same on both sides."],
    supports="Provide a partially completed graph. Use a table of expected values so students can compare. Pair students for the strip coloring.",
)

TEACHER[3] = dict(
    glance="CFA ESS1-5.2 opens the day (8 min), then a 5-minute hook. Students run an impact-crater lab (15 min) and build a 45 cm timeline of Earth (13 min) to see why meteorites and moon rocks give the age of the solar system and why Earth's own early record is missing. About 28 of 45 minutes are lab.",
    materials=["Per group: a shallow tray or box lid with about 2 cm of flour topped with a thin layer of cocoa powder, 2 marbles (one small, one large), a ruler, newspaper under the tray, safety goggles",
               "Per pair: a 45 cm strip of adding-machine tape or paper, a ruler, colored pencils", "Images of the Moon and Mars surfaces (optional)", "Chromebooks for the CFA"],
    agenda=[["0–8", "CFA ESS1-5.2"], ["8–13", "Hook and key ideas (radiometric dating as a steady clock; why the oldest Earth rock is younger than Earth)"], ["13–28", "Lab A: impact craters"],
            ["28–41", "Lab B: 45 cm timeline of Earth"], ["41–45", "Wrap-up: evidence-log row and exit ticket"]],
    notes=["The half-life lab was removed to save time and reading. Radiometric dating is told in one sentence (a steady atomic clock); students are not asked to calculate with it. The CFAs and CSA do not use half-life.",
           "Lab A pacing: 5 minutes for the size and height tests, 5 for the old surface, 5 for the young surface. Do the flour work on newspaper; marbles can be dropped in a box lid to keep the mess small.",
           "Timeline positions use 1 cm = 100 million years, so Earth is 45 cm long and all of the surviving ocean floor fits in the last 2 cm. Meteorites (4.56 billion years) are about as old as the left end.",
           "ESS1-6 is a supporting standard, taught here to feed ESS1-5.3 and ESS1-5.5. ESS1-6 has no CFAs or reviews and is not on the CSA.",
           "Crater counts: the Moon has no plate tectonics and almost no weathering, so craters last. Earth has about 190 known craters because erosion, volcanism, and plate tectonics erase them.",
           READING],
    key=["Crater lab: higher drops and bigger marbles make wider craters. The tray with many overlapping craters (not smoothed) looks older; the smoothed tray with 2 craters looks young.",
         "Earth shows few craters because plate tectonics, erosion, weathering, and volcanism erase them; the Moon highlands are oldest (most craters) and are the better archive of the early solar system.",
         "Timeline positions: oldest rock (4,000) = 5 cm; oldest fossils (3,500) = 10 cm; oldest ocean floor (200) = 43 cm. All existing ocean floor is in the last 2 cm of the 45 cm strip.",
         "The oldest Earth rocks are younger than Earth because Earth's earliest rocks were destroyed or recycled by plate tectonics and erosion.",
         "Meteorites formed with the solar system and have changed little, so their ages (about 4.56 billion years) are the best estimate; the Moon is geologically quiet and kept its early rocks.",
         "Fossils that old are in continental rock; ocean floor of that age has been subducted."],
    supports="Pre-cut the timeline strips and mark the ends. Give a partially filled timeline table. Let students describe the craters orally before sketching.",
)

TEACHER[4] = dict(
    glance="Students take 7 minutes of guided notes (the life of ocean crust, density, how continents grow), then run a 17-minute sink-or-float density lab, then make SketchNotes (15 min) for the Lesson 4 assignment. No CFA opens the day. CFA ESS1-5.3 opens Day 5.",
    materials=["Per group: a clear tub of water, a wood block, a clay block, a balance, a ruler, paper towels", "SketchNotes paper", "Chromebooks"],
    agenda=[["0–3", "Warm-up"], ["3–10", "Guided notes (fill-in-the-blank, shown on the slides)"], ["10–27", "Lab: sink or float (density of plates)"], ["27–42", "SketchNotes"], ["42–45", "Wrap-up: evidence-log row; preview tomorrow's CFA"]],
    notes=["Density wording: ocean crust alone is slightly less dense than the mantle; the old, cold ocean plate is denser than the hot mantle below and sinks. The lab uses water as the stand-in for the mantle, a wood block as the continent, and a clay block as an old, cold plate. Both real crusts are denser than water, so say that out loud as a model limit.",
           "Lab pacing: 3 minutes to measure, 3 to calculate, 5 to place and push the blocks, 6 to answer the questions. Have the blocks pre-cut into rectangles so the volume is easy.",
           "Continental growth is simplified: arcs and pieces of crust (terranes) collide with and are added to the margin; the continent is also eroded and parts are recycled, but most of it stays.",
           "The carbon link is one arrow on the SketchNotes (plankton-shell carbon rides the plate down and some returns as CO₂), not a separate discussion.",
           READING],
    key=["Guided notes: ridge; 3,000 ÷ 25 = 120 million years; 200 × 25 = 5,000 km; about 200 million years; the ocean (denser) plate sinks; the edge is younger than the core.",
         "Lab: the clay block is denser (greater than 1 g/cm³) and sinks; the wood block is less dense and floats. The ocean plate is like the clay, the continent is like the wood. When they meet, the denser one dives under. Water stands in for the mantle.",
         "Two continental plates collide: both are buoyant, so neither subducts; the crust crumples upward into mountains (such as the Himalaya).",
         "Continents survive because they are less dense; the ocean floor is recycled at trenches, so its age rarely exceeds about 200 million years.",
         "Edge crust is younger because volcanic arcs and pieces of crust were added to the edge of the continent later.",
         "Ocean crust: made at a ridge, moves, is destroyed in under 200 million years. Continental crust: ancient core, grows outward, survives for billions of years.",
         "Carbon is not lost: plankton shells carry carbon down; some returns to the air as CO₂ from volcanoes; the rest stays in the mantle for a long time."],
    supports="Provide a SketchNotes template with the sinking plate outlined. Provide the guided-notes sheet pre-printed. Let students dictate the comparison sentences.",
)

TEACHER[5] = dict(
    glance="CFA ESS1-5.3 opens the day (8 min). Students then run three short hands-on labs on the evidence for moving crust: a paper magnetic-stripe model (12 min), a measured-motion calculation using Hawaii and GPS (7 min), and a Pangaea fossil puzzle (9 min). They finish by evaluating the strength of each line of evidence (6 min). CFA ESS1-5.4 opens Day 6.",
    materials=["Paper, scissors, red and blue pencils, rulers; 2 strips per pair (12 cm each); a folded sheet for the slit", "Cut-out continent shapes for each pair (any 'Pangaea puzzle' handout; the Gizmo Building Pangaea is an alternate)", "Tape", "Chromebooks for the CFA"],
    agenda=[["0–8", "CFA ESS1-5.3"], ["8–10", "Warm-up"], ["10–22", "Lab A: magnetic-stripe paper model"], ["22–29", "Lab B: Hawaii and GPS rates"], ["29–38", "Lab C: Pangaea puzzle with fossils"],
            ["38–44", "Evaluate the evidence table"], ["44–45", "Preview tomorrow's CFA"]],
    notes=["For low readers, pre-color the strips or give them pre-printed strips so Lab A is about the pull-apart, not the coloring.",
           "Strips must start with the oldest band at the end that goes through the slit first, so the youngest band appears at the center last.",
           "Hawaiian chain numbers are rounded: Kauaʻi about 500 km and 5 million years, Midway about 2,500 km and 28 million years. The rates come out near 9 to 10 cm per year; GPS gives about 7 to 8 cm per year. That is close but not identical, which is a good moment to talk about rounded data.",
           "ESS1-5.4 is DOK 3: students judge strength. Push for criteria (measured, independent, predictions hold, limits named), not just opinions.",
           "Oʻahu was removed from the Hawaii table to shorten the calculation. The two islands left give the rate.",
           READING],
    key=["Stripes are mirror images because crust forms at the ridge, records the magnetic field, then splits and moves apart both ways.",
         "Hawaii: Kauaʻi 500 km ÷ 5 million years = 100 km per million years = 10 cm per year. Midway 2,500 ÷ 28 ≈ 90 km per million years ≈ 9 cm per year. Similar to GPS (7 to 8 cm per year).",
         "Mesosaurus (freshwater) and Glossopteris (heavy seeds) could not cross oceans, so the lands were once joined. Fossils cannot give the rate or show present motion.",
         "Evaluation table (sample): rock ages — quantitative, past, independent, 4; stripes — quantitative, past, independent, 4; GPS and Hawaii — measured, present (GPS) and past (island ages), independent, 4; fossils and rocks — qualitative, past, partly independent, 2 to 3.",
         "Current motion: GPS. Past motion: rock ages and stripes agree, plus fossils.",
         "Two independent methods agree on a rate, which is hard to explain by chance, so the conclusion is more trustworthy.",
         "A weakening finding: crust at the ridge being old and getting younger away from it."],
    supports="Pre-cut strips and continents. Give the evaluation table with one row completed. Pair students for the models.",
)

TEACHER[6] = dict(
    glance="CFA ESS1-5.4 opens the day (8 min). Students sort their evidence log (3 min), write an evaluation of how well plate tectonics explains the ages of crustal rocks with five sentence frames (Part A, 14 min), give peer feedback (5 min), and order six evidence cards on a strip to tell Earth's story (Part B, 12 min). CFA ESS1-5.5 follows on the work day or at the start of Day 7.",
    materials=["Students' Unit CER evidence logs", "Sentence frames, evidence cards, and the peer feedback checklist (on the page)", "Scissors, glue, paper strips", "Chromebooks"],
    agenda=[["0–8", "CFA ESS1-5.4"], ["8–11", "Sort evidence into three buckets; revisit the Day 1 claim"], ["11–25", "Part A: draft the evaluation with five frames"],
            ["25–30", "Peer feedback and revision"], ["30–42", "Part B: evidence-card sort and the Earth story"], ["42–45", "Wrap-up: preview CFA ESS1-5.5"]],
    notes=["Revisit the Day 1 misconceptions. Ask students who changed their claim to say what changed their mind.",
           "Score the CER with the 4-point rubric on the assignment. Students who score below a 3 can revise during the work day, Day 7, or the reassessment window.",
           "ESS1-5.5 asks for an evaluation, not just an explanation. A strong response says how well and names a limit (no ocean crust older than about 200 million years remains).",
           "Part B (ESS1-6.3) is supporting and has no CFA; it is not on the CSA. Do not let it crowd out Part A. If time is short, students can do the card sort and write only two frames.",
           READING],
    key=["Sample strong claim: Plate tectonics explains the ages of Earth's crustal rocks very well because ocean crust is made at ridges and recycled at subduction zones, while less-dense continental crust survives and grows outward.",
         "Evidence examples: crust age increases from 0 to 120 million years across 3,000 km (2.5 cm per year); the oldest ocean floor is about 200 million years; continental minerals are up to about 4.4 billion years; North American crust is about 2.7 billion years at its core and about 400 million years in the Appalachians.",
         "Reasoning: dense ocean plates sink at trenches while buoyant continents stay at the surface and grow at their edges.",
         "Limit: no ocean floor older than about 200 million years remains, so early Earth must be studied in continental rock and in meteorites. Counterclaim: the ocean floor erodes away — sediment is thicker on older crust, so old crust is not worn away; it is subducted.",
         "Part B card order (oldest to newest): meteorites 4.56 billion; moon highlands up to 4.4 billion; zircons 4.4 billion; Acasta Gneiss 4.0 billion; stromatolites 3.5 billion; oldest ocean floor 200 million. The early record is missing because plate tectonics and erosion recycled it, so scientists use meteorites, the Moon, and other planets."],
    supports="Provide a completed example for the first frame. Allow students to dictate or use speech-to-text. Pre-cut the evidence cards.",
)

TEACHER[7] = dict(
    glance="Review day and cushion. Students rate themselves on all eight targets, take any CFA they have not taken (including ESS1-5.5), and complete the Mastery Path reviews that opened. Students with no reviews open can be assigned the Enrichment choice board (you assign it manually).",
    materials=["Students' notebooks, Frayer cards, and CFA scores", "Chromebooks", "Optional: Blooket or quiz game for students who finish"],
    agenda=[["0–5", "Self-rating chart"], ["5–38", "Work time: unfinished CFAs, Mastery Path reviews, or Enrichment"], ["38–43", "Vocabulary self-check with a partner"], ["43–45", "Preview the CSA"]],
    notes=["Review assignments open automatically when a CFA score is below 3 of 4. Check the Gradebook for students with a CFA but no review yet.",
           "To assign the Enrichment piece: open Unit 3.1 Enrichment: Choice Board, use Assign To for the students you choose, and publish it. It is hidden from everyone else.",
           "The CSA covers ESS1-5.1 to ESS1-5.5 only. Tell students that ESS1-6 practice supports ESS1-5.3 and ESS1-5.5 but is not tested.",
           "The Frayer cards (8 words) are homework from Day 1; use the first minutes of work time for students to finish them.",
           "There is no practice test in this unit; the CFAs and reviews serve as practice for the CSA."],
    key=["Self-rating chart is personal. Compare it with CFA scores and discuss any mismatch.",
         "Review answers are in the teacher key (HS-ESS1-5_teacher_key.md in the repo).",
         "Enrichment answers: see the notes on the Enrichment assignment; for Option 1, 1 km ÷ 2.5 cm per year = 40,000 years; for Option 3, 2 cm/yr × 1 million years = 20 km, and 100 cm in 50 years; for Option 4, Mars's crust is older because it is not recycled."],
    supports="Pull a small group for any target where several students scored below 3. Pair students who have completed reviews with those who need more practice.",
)

TEACHER[8] = dict(
    glance="CSA day. 16 questions on the five priority targets, 14 auto-graded and two written responses (Q12 evaluate the evidence and Q16 evaluate plate tectonics) graded with the 4-point rubrics in the quiz.",
    materials=["Chromebooks with Canvas open", "Pencils"],
    agenda=[["0–3", "Directions"], ["3–43", "CSA"], ["43–45", "Collect Chromebooks; early finishers work quietly"]],
    notes=["Grade Q12 and Q16 in SpeedGrader; the rubric and sample answers are in each question's scoring data.",
           "Targets and CSA questions: ESS1-5.1 (Q1–3), ESS1-5.2 (Q4–6), ESS1-5.3 (Q7–9), ESS1-5.4 (Q10–12), ESS1-5.5 (Q13–16). Supporting ESS1-6 targets are not on the CSA.",
           "For students below a 3 on a target, assign the matching Mastery Path review as intervention, then reassess."],
    key=["See HS-ESS1-5_teacher_key.md for answers to every CSA question and the full rubrics."],
    supports="Provide extended time, read aloud, or a quiet room as outlined in IEP/504 plans.",
)

DAYS = {1: DAY1, 2: DAY2, 3: DAY3, 4: DAY4, 5: DAY5, 6: DAY6, 7: DAY7, 8: DAY8}
