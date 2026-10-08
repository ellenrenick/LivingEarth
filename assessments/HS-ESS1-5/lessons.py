"""Student pages, teacher pages, and extra assignments for Unit 3.1 Age of the Earth.

Content only. canvas_lessons.py turns these into Canvas pages and a module.
All numbers are real or simplified from real values; simplified ones are labeled.
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
    tl = "".join(f"<li><strong>{c}</strong> {TARGET_TEXT[c]}</li>" for c in targets) if targets else "<li>Launch day: you will work toward all five unit targets.</li>"
    out = [
        f'<div style="{BOX}"><p><strong>Day {day}</strong> · {UNIT_TITLE}</p>'
        f"<p><strong>Driving question:</strong> {DRIVING}</p>"
        f"<p><strong>Focus question:</strong> {focus}</p><p><strong>Learning target:</strong></p><ul>{tl}</ul></div>",
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
TIMELINE = table(["Event", "Age (millions of years ago)", "Position on the 45 m timeline"], [
    ["Earth forms", "4,500", "0 m"],
    ["Oldest mineral on Earth (zircon)", "4,400", "1 m"],
    ["Oldest known rock", "4,000", "<br>"],
    ["Oldest fossils", "3,500", "<br>"],
    ["Oldest ocean floor", "200", "<br>"],
    ["Today", "0", "45 m"],
])

DAY1 = dict(
    title="Where Did the Old Ocean Floor Go?",
    focus="How old is the ocean floor compared with the continents, and what does that tell us?",
    targets=[],
    notebook=[
        "Title: <strong>D1 Where Did the Old Ocean Floor Go?</strong>. Start your table of contents.",
        "Fill in the warm-up guesses, the I notice / I wonder table, and the timeline table.",
        "Start your <strong>Unit CER</strong> on a new page. Write the question <em>Why is the seafloor so much younger than the continents?</em>, your first claim, and a 3-column evidence log (Day · Evidence · What it shows). You will add a row every day.",
        "Start your <strong>Frayer cards</strong> for the 10 vocabulary words (list in Part 5). Finish them by Day 4.",
    ],
    parts=[
        ("Warm-up: guess", "<p>Earth is about 4.5 billion years old. Write down a guess for (a) the age of the <strong>oldest ocean floor</strong> and (b) the age of the <strong>oldest rock or mineral on the continents</strong>. Give one reason for each.</p>"),
        ("The phenomenon", "<p>Scientists have measured the age of rock from the ocean floor and from the continents. Here are some of the results.</p>"
            "<h3>Ocean floor</h3>" + OCEAN_AGES + "<p><em>Ages are rounded.</em></p><h3>Continents and life</h3>" + LAND_AGES +
            "<p><strong>Notice and wonder:</strong> write what you notice and what you wonder.</p>" + blank_table(["I notice…", "I wonder…"], 1)),
        ("Scale it: a 45-meter timeline", "<p>Imagine Earth's whole history stretched along a 45 m hallway: <strong>1 m = 100 million years</strong>. Earth forms at 0 m and today is at 45 m. Position = (4,500 − age in millions of years) ÷ 100.</p>" + TIMELINE +
            "<p>Fill in the missing positions. Then answer: how much of the 45 m is covered by <strong>ocean floor that still exists</strong>? Where on the timeline did life first leave fossils?</p>"),
        ("The mystery and your first claim", "<p>Almost all of Earth's history is missing from the ocean floor. <strong>Why is the seafloor so much younger than the continents?</strong></p>"
            "<ol><li>Draw a quick model: a cross-section of an ocean with two continents on either side. Show where you think ocean floor might come from and where it might go.</li>"
            "<li>Write your first claim for the Unit CER. It is fine if it is wrong; we will revise it.</li></ol>"),
        ("Vocabulary preview", "<p>You will use these 10 words all unit. With a partner, make a Frayer card for the two words your teacher assigns. Finish all 10 by Day 4.</p>" +
            ol(["continental drift", "seafloor spreading", "mid-ocean ridge", "subduction", "trench", "magnetic reversal",
                "plate boundary (divergent, convergent, transform)", "radiometric dating", "half-life", "fossil record"])),
        ("Exit ticket", "<p>Write one thing you could measure or observe that would test your claim.</p>"),
    ],
)

# ===================================================================== DAY 2
FOSSILS = table(["Organism", "What it was", "Found in", "Age"], [
    ["<em>Glossopteris</em>", "seed fern (a plant with heavy seeds)", "South America, Africa, India, Australia, Antarctica", "about 250–300 million years"],
    ["<em>Mesosaurus</em>", "freshwater reptile", "South America, southern Africa", "about 280 million years"],
    ["<em>Lystrosaurus</em>", "land animal (about the size of a pig)", "Africa, India, Antarctica", "about 250 million years"],
    ["<em>Cynognathus</em>", "land animal, relative of mammals", "South America, southern Africa", "about 240 million years"],
])
MATCHES = table(["Evidence", "What scientists found", "What it suggests"], [
    ["Rock layers", "The same sequence of rock types and fossils on the southern continents.", "<br>"],
    ["Mountain belts", "The Appalachians (North America) match mountains in Scotland and Scandinavia in rock type and age.", "<br>"],
    ["Glacial scratches", "Scratches from the same ice age in southern Africa, India, Australia, South America, and Antarctica.", "<br>"],
    ["Shelf fit", "The edges of the continental shelves, not the coastlines, fit together best.", "<br>"],
])

DAY2 = dict(
    title="The Fossil Puzzle",
    focus="What evidence shows that the continents were once joined?",
    targets=["ESS1-5.1"],
    notebook=[
        "Title: <strong>D2 The Fossil Puzzle</strong>. Add it to your table of contents.",
        "Record your warm-up answer, the fossil range map, and the evidence table.",
        "Tape or glue your continent puzzle into your notebook.",
        "<strong>Unit CER evidence log:</strong> add one row: the day, one piece of evidence from today, and what it shows about why the ocean floor is so young.",
    ],
    parts=[
        ("Warm-up", "<p><em>Mesosaurus</em>, a small reptile that lived in <strong>fresh water</strong>, left fossils in both Brazil and South Africa. Could it have swum across the Atlantic? Explain.</p>"),
        ("Wegener's idea", "<p>In 1912, Alfred Wegener proposed that all the continents were once joined in one supercontinent, <strong>Pangaea</strong>, and have slowly drifted apart. This is called <strong>continental drift</strong>. Today you test his idea with evidence.</p>"),
        ("Fossil puzzle lab", "<p>Your teacher will give you a map of the southern continents.</p>" +
            ol(["Cut out South America, Africa, India, Antarctica, and Australia along the <strong>edge of the continental shelf</strong> (the dashed line), not the coastline.",
                "Fit the pieces together so the shelf edges match. Tape them down.",
                "Use a different color for each fossil in the table below. Shade the places where each fossil has been found.",
                "Describe what you see: do the colored areas form a continuous pattern?"]) + FOSSILS +
            "<p><strong>Biology question:</strong> The seeds of <em>Glossopteris</em> were large and heavy, and <em>Mesosaurus</em> lived only in fresh water. Which explanation fits better: &ldquo;they crossed a gap&rdquo; or &ldquo;there was no gap&rdquo;? Use two pieces of evidence.</p>"),
        ("More evidence", "<p>Complete the last column. What does each piece of evidence suggest?</p>" + MATCHES),
        ("Wegener's weakness", "<p>Wegener could not explain what force could move continents. Why did that make many scientists reject his idea for decades? What kind of evidence would they have needed?</p>"),
        ("Show what you know: CFA ESS1-5.1", "<p>Take <strong>Unit 3.1 CFA ESS1-5.1: Evidence for continental drift</strong> on Canvas (5 questions). If you score below 3 out of 4 (fewer than 4 of 5 correct), a review for this target will open for you.</p>"),
    ],
)

# ===================================================================== DAY 3
SPREAD = table(["Distance from ridge (km)", "Crust age (million years)", "Sediment thickness (m)"], [
    ["0", "0", "about 0"], ["500", "20", "about 50"], ["1,000", "40", "about 150"], ["1,500", "60", "about 250"],
    ["2,000", "80", "about 350"], ["2,500", "100", "about 450"], ["3,000", "120", "about 550"],
])

DAY3 = dict(
    title="Making New Crust",
    focus="How is new ocean floor made, and what pattern does it leave behind?",
    targets=["ESS1-5.2"],
    notebook=[
        "Title: <strong>D3 Making New Crust</strong>. Add it to your table of contents.",
        "Record your prediction, your age-versus-distance graph with the rate calculation, and your magnetic-stripe model drawing.",
        "Tape your finished paper stripes into your notebook.",
        "<strong>Unit CER evidence log:</strong> add one row with a specific number from today's data.",
    ],
    parts=[
        ("Warm-up: predict", "<p>A ship pulls up seafloor rock right at the Mid-Atlantic Ridge and another sample near the coast of Brazil. Which rock is older? Explain your prediction.</p>"),
        ("The data", "<p>Scientists measured the age and the sediment thickness of the seafloor at sites along a line across the Mid-Atlantic Ridge. (These numbers are simplified from a spreading rate of about 2.5 cm per year.)</p>" + SPREAD +
            ol(["Graph <strong>crust age</strong> (y-axis) against <strong>distance from the ridge</strong> (x-axis). Describe the pattern.",
                "Calculate the rate: distance &divide; time. (Convert: 1 km per million years = 0.1 cm per year.) How fast is the seafloor moving? Compare it with something that grows at about that speed.",
                "Predict the age of crust 3,500 km from the ridge.",
                "Graph <strong>sediment thickness</strong> against distance. Why would older crust have thicker sediment? (Hint: what falls to the seafloor from the ocean above, including the shells of dead plankton?)"])),
        ("Paper magnetic-stripe model", "<p>As lava hardens at a ridge, tiny magnetic minerals line up with Earth's magnetic field. Earth's field has flipped many times, so the new crust records <strong>stripes</strong> of normal and reversed magnetism. This is a <strong>magnetic reversal</strong> record.</p>"
            "<p><strong>Make the strips:</strong> Cut two identical paper strips, each 12 cm long. Starting from the end you will push through the slit first (this becomes the <em>oldest</em> crust), color these bands (2 cm = 1 million years):</p>" +
            table(["Band (from the end you push first)", "Color", "Length", "Age it represents"], [
                ["1", "Reversed (blue)", "3.4 cm", "about 3.6–5.3 million years"],
                ["2", "Normal (red)", "2.0 cm", "about 2.6–3.6 million years"],
                ["3", "Reversed (blue)", "3.6 cm", "about 0.8–2.6 million years"],
                ["4", "Normal (red)", "1.6 cm", "0–0.8 million years (youngest)"]]) +
            ol(["Cut a slit in a folded sheet of paper. This slit is the <strong>mid-ocean ridge</strong>.",
                "Put the two strips back to back and push them up through the slit from underneath. Pull them slowly apart, one to each side.",
                "Draw what you see. Where is the youngest crust? The oldest? Are the two sides the same?"]) +
            "<p><strong>Explain:</strong> Why are the stripes on the two sides of a ridge mirror images?</p>"),
        ("Life on new crust", "<p>Along the ridge, hot water heated by magma rises through the seafloor at <strong>hydrothermal vents</strong>. Far from sunlight, bacteria use chemicals in the vent water (such as hydrogen sulfide) as an energy source in a process called <strong>chemosynthesis</strong>. Tube worms, clams, and shrimp live with these bacteria. Individual vents last years to decades. Vent fields depend on heat from magma beneath the ridge; crust that has moved far from the ridge has left that heat behind.</p>"
            "<p>Why are vent communities found at the ridge but not on the old seafloor far away? Use the age pattern in your answer.</p>"),
        ("Show what you know: CFA ESS1-5.2", "<p>Take <strong>Unit 3.1 CFA ESS1-5.2: Seafloor spreading and the age pattern</strong> on Canvas (5 questions). If you score below 3 out of 4 (fewer than 4 of 5 correct), a review for this target will open for you.</p>"),
    ],
)

# ===================================================================== DAY 4
SITES = [
    ("Mount St. Helens, Washington, USA", "volcano", "46.2° N", "122.2° W"),
    ("Mount Fuji, Japan", "volcano", "35.4° N", "138.7° E"),
    ("Mount Pinatubo, Philippines", "volcano", "15.1° N", "120.4° E"),
    ("Popocatépetl, Mexico", "volcano", "19.0° N", "98.6° W"),
    ("Hekla, Iceland", "volcano", "64.0° N", "19.7° W"),
    ("Erta Ale, Ethiopia", "volcano", "13.6° N", "40.7° E"),
    ("Tohoku, Japan (2011, magnitude 9.1)", "earthquake", "38.3° N", "142.4° E"),
    ("Maule, Chile (2010, magnitude 8.8)", "earthquake", "35.9° S", "72.7° W"),
    ("Sumatra, Indonesia (2004, magnitude 9.1)", "earthquake", "3.3° N", "96.0° E"),
    ("Haiti (2010, magnitude 7.0)", "earthquake", "18.4° N", "72.5° W"),
    ("Turkey (2023, magnitude 7.8)", "earthquake", "37.2° N", "37.0° E"),
    ("Nepal (2015, magnitude 7.8)", "earthquake", "28.2° N", "84.7° E"),
    ("Kīlauea, Hawaiʻi, USA", "volcano", "19.4° N", "155.3° W"),
]
SITES_KEY = {
    "Mount St. Helens": "convergent (Juan de Fuca plate subducting under North America)",
    "Mount Fuji": "convergent (subduction)",
    "Mount Pinatubo": "convergent (subduction)",
    "Popocatépetl": "convergent (Cocos plate subducting under North America)",
    "Hekla": "divergent (Mid-Atlantic Ridge on land, with a hot spot)",
    "Erta Ale": "divergent (Afar rift)",
    "Tohoku": "convergent (Pacific plate subducting under Japan)",
    "Maule": "convergent (Nazca plate subducting under South America)",
    "Sumatra": "convergent (subduction)",
    "Haiti": "transform (strike-slip fault)",
    "Turkey": "transform (East Anatolian Fault)",
    "Nepal": "convergent (continent-continent collision, no subduction of continental crust)",
    "Kīlauea": "NOT at a plate boundary: a hot spot in the middle of the Pacific plate",
}
SITE_TABLE = table(["Site", "Type", "Latitude", "Longitude", "Boundary type (you decide)"],
                   [[s, t, la, lo, "<br>"] for s, t, la, lo in SITES])

DAY4 = dict(
    title="Where Crust Goes, and Where It Stays",
    focus="If new crust is made at ridges, where does old ocean crust go, and why do the continents stay?",
    targets=["ESS1-5.3"],
    notebook=[
        "Title: <strong>D4 Where Crust Goes</strong>. Add it to your table of contents.",
        "Tape your plotted world map into your notebook and record your answers to the pattern questions.",
        "Make your <strong>SketchNotes</strong>: a half page of notes and one page of sensemaking (a labeled subduction zone cross-section).",
        "<strong>Unit CER evidence log:</strong> add one row about density or subduction.",
        "Finish your Frayer cards for all 10 words as homework.",
    ],
    parts=[
        ("Warm-up", "<p>Earth is not getting bigger, but new ocean crust is made at ridges all the time. Where could the old crust go?</p>"),
        ("Plot the pattern", "<p>Plot these earthquakes and volcanoes on a world map (use a different symbol for each type). Then use a map of the plates to decide which kind of plate boundary is nearest to each site.</p>" + SITE_TABLE +
            ol(["Describe the pattern of your points. Do they appear at random or along lines?",
                "Name the three boundary types (divergent, convergent, transform) and write what the plates do at each.",
                "One site does not fit the pattern. Which one? What could explain it?"])),
        ("Why does some crust sink?", "<p>At a <strong>convergent</strong> boundary where an ocean plate meets a continent, the ocean plate bends and sinks into the mantle. This is <strong>subduction</strong>, and it makes a deep <strong>trench</strong> and a line of volcanoes on land.</p>" +
            table(["Material", "Average density (g/cm³)"], [["Ocean crust (basalt)", "about 3.0"], ["Continental crust (granite)", "about 2.7"]]) +
            "<p>Old ocean plates are cold, so they are denser than the hot mantle rock beneath them.</p>"
            + ol(["When an ocean plate meets a continental plate, which one sinks? Why?",
                  "What happens when two continental plates collide (such as India and Asia)? Use the density data to explain why mountains rise instead of a trench forming.",
                  "Continents stay at the surface for billions of years; the ocean floor is recycled in about 200 million years. Use density to explain both."])),
        ("What rides the plate down?", "<p>The ocean floor is covered in sediment, including the shells of dead plankton, which contain carbon. When a plate subducts, some of this sediment goes down with it. Some of the carbon returns to the air as carbon dioxide when volcanoes erupt.</p>"
            "<p>Connect to Unit 1.2: describe how this movement of carbon is part of the carbon cycle. Is carbon lost? Explain.</p>"),
        ("SketchNotes", "<p><strong>Half page of notes:</strong> the three boundary types, with a landform for each. <strong>One page of sensemaking:</strong> draw a cross-section of a subduction zone with the trench, the sinking plate, the volcanic arc, and an arrow showing where a plankton shell's carbon goes. Label density.</p>"
            "<p>Take a photo of your SketchNotes and turn them in on Canvas: <strong>Lesson 4: SketchNotes</strong>.</p>"),
        ("Tomorrow", "<p>Your CFA for this target, <strong>Unit 3.1 CFA ESS1-5.3: Plate boundaries and subduction</strong>, is at the start of tomorrow's class (5 questions). Study your SketchNotes tonight.</p>"),
    ],
)

# ===================================================================== DAY 5
HALF_TABLE = table(["Round", "Parent atoms left", "Fraction of the original"], [[str(n), "<br>", "<br>"] for n in range(0, 7)])
OLD = table(["Material", "Where", "Age"], [
    ["Meteorite fragments (Canyon Diablo)", "Arizona, USA", "about 4.56 billion years"],
    ["Moon rocks from the lunar highlands", "Brought back by Apollo", "up to about 4.4 billion years"],
    ["Oldest Earth mineral (zircon)", "Jack Hills, Australia", "about 4.4 billion years"],
    ["Oldest known Earth rock (Acasta Gneiss)", "Canada", "about 4.0 billion years"],
    ["Oldest widely accepted fossils (stromatolites)", "Western Australia", "about 3.5 billion years"],
    ["Oldest ocean floor", "Western Pacific and Atlantic margins", "about 180–200 million years"],
])
CLOCKS = table(["Method", "Parent → daughter", "Half-life", "Good for"], [
    ["Carbon-14", "C-14 → N-14", "5,730 years", "Once-living things (wood, bone, shell) younger than about 50,000 years"],
    ["Uranium-235", "U-235 → Pb-207", "about 704 million years", "Zircon crystals in igneous rock; meteorites"],
    ["Uranium-238", "U-238 → Pb-206", "about 4.47 billion years", "Zircon crystals in igneous rock; meteorites"],
])

DAY5 = dict(
    title="Reading Deep Time",
    focus="How do scientists find the age of a rock, and why are the oldest Earth rocks younger than Earth?",
    targets=["ESS1-6.1"],
    notebook=[
        "Title: <strong>D5 Reading Deep Time</strong>. Add it to your table of contents.",
        "Record your half-life data table, graph, and answers.",
        "Complete the clock-matching table and the timeline question.",
        "<strong>Unit CER evidence log:</strong> add one row about the age of continental material or of meteorites.",
    ],
    parts=[
        ("Start with a CFA: ESS1-5.3", "<p>Take <strong>Unit 3.1 CFA ESS1-5.3: Plate boundaries and subduction</strong> on Canvas now (5 questions). If you score below 3 out of 4, a review for this target will open for you.</p>"),
        ("Hook", "<p>The oldest ocean floor is only about 200 million years old, yet scientists say Earth is about 4.5 billion years old. How could anyone know that? Write one idea.</p>"
            "<p>Some atoms are <strong>unstable</strong>: they change into a different kind of atom at a steady rate. This is <strong>radioactive decay</strong>. The <strong>half-life</strong> is the time for half of the unstable (parent) atoms in a sample to decay into stable (daughter) atoms. Scientists use this as a clock: <strong>radiometric dating</strong>.</p>"),
        ("Half-life lab", ol(["Put 50 coins (or candies with a marked side) in a cup. Each coin is an atom of the parent isotope.",
                              "Shake the cup, spill the coins, and remove every coin that landed <strong>marked side up</strong>. These atoms have &ldquo;decayed.&rdquo; Count and record the coins left.",
                              "Put the remaining coins back in the cup and repeat for 6 rounds, or until none are left.",
                              "Combine your data with another pair if you have time."]) + HALF_TABLE +
            ol(["Graph <strong>parent atoms left</strong> against <strong>round</strong>. Describe the shape.",
                "About what fraction remains after each round? What is each round equal to?",
                "If each round were one half-life of carbon-14 (5,730 years), how old would a sample be with 1/8 of its carbon-14 left?",
                "Can you predict when one particular coin will &ldquo;decay&rdquo;? Can you predict what happens to 50? Why does it matter for dating rocks that there are billions of atoms?"])),
        ("Which clock for which sample?", CLOCKS +
            "<p>Zircon crystals take uranium into their structure when they form but leave out lead, so any lead inside came from decay. Match each sample to the best method and explain:</p>" +
            ol(["A 9,000-year-old wooden spear",
                "A zircon crystal in a 3-billion-year-old granite",
                "A 3.5-billion-year-old fossil stromatolite in rock",
                "A 20,000-year-old mammoth tusk"])),
        ("The oldest materials", OLD +
            "<p>Plate tectonics and erosion recycled Earth's earliest rocks. Meteorites formed with the solar system and have changed very little.</p>"
            + ol(["Why is the oldest Earth rock (4.0 billion years) younger than Earth itself?",
                  "Why do scientists use meteorites to estimate Earth's age?",
                  "The oldest fossils are in continental rock. Why are there no fossils that old in the ocean floor?"])),
        ("Tomorrow", "<p>Your CFA for this target, <strong>Unit 3.1 CFA ESS1-6.1: Radiometric dating and Earth's oldest rocks</strong>, is at the start of tomorrow's class (5 questions). Study your half-life data and the clock table.</p>"),
    ],
)

# ===================================================================== DAY 6
CER_FRAMES = ul([
    "<strong>Claim:</strong> The ocean floor is much younger than the continents because ______.",
    "<strong>Evidence 1 (pattern):</strong> The seafloor age data show ______.",
    "<strong>Evidence 2 (numbers):</strong> At a rate of about ______, rock ______ km from the ridge is about ______ million years old.",
    "<strong>Evidence 3 (continents):</strong> Continental rocks and minerals as old as ______ exist because ______.",
    "<strong>Reasoning:</strong> Because ocean plates are ______ than continental crust, they ______ at subduction zones, so ______.",
    "<strong>Counterclaim:</strong> Someone might say the ocean floor is young because ______. This does not fit the evidence because ______.",
])
CER_CHECK = ul(["The claim answers the question completely and names the cause.",
                "Each piece of evidence is specific (a number or a named pattern).",
                "At least two different kinds of evidence are used.",
                "The reasoning explains <em>why</em> the evidence supports the claim.",
                "A counterclaim is answered with evidence."])

DAY6 = dict(
    title="Build the Argument",
    focus="How do I use evidence and reasoning to answer the unit question?",
    targets=["ESS1-6.1", "ESS1-5.4"],
    notebook=[
        "Title: <strong>D6 Build the Argument</strong>. Add it to your table of contents.",
        "Have your <strong>Unit CER evidence log</strong> open. You will use every row.",
        "Sort your evidence into the three buckets in Part 2.",
    ],
    parts=[
        ("Start with a CFA: ESS1-6.1", "<p>Take <strong>Unit 3.1 CFA ESS1-6.1: Radiometric dating and Earth's oldest rocks</strong> on Canvas now (5 questions). If you score below 3 out of 4, a review for this target will open for you.</p>"),
        ("Sort your evidence", "<p>Look at your evidence log. Sort each row into a bucket:</p>" +
            table(["The seafloor is young because…", "The continents are old because…", "The early record is missing because…"], [["<br><br><br>", "<br><br><br>", "<br><br><br>"]]) +
            "<p>Look back at your Day 1 claim. What would you change now?</p>"),
        ("Write your argument", "<p>Answer the unit question: <strong>Why is the seafloor so much younger than the continents?</strong> Use the sentence frames. Strong writers use all of them; you may add more.</p>" + CER_FRAMES +
            "<p><strong>Data you may use:</strong> seafloor age and distance from the ridge (Day 3 table); oldest ocean floor about 200 million years; oldest continental mineral about 4.4 billion years; ocean crust about 3.0 g/cm³ and continental crust about 2.7 g/cm³; oldest fossils about 3.5 billion years in continental rock; meteorites about 4.56 billion years.</p>"
            "<p>Submit your finished argument on Canvas: <strong>Unit 3.1 CER</strong>.</p>"),
        ("Peer feedback", "<p>Trade with a partner. Check the list below and write one &ldquo;star&rdquo; (something strong) and one &ldquo;step&rdquo; (something to improve). Then revise your own.</p>" + CER_CHECK),
        ("Show what you know: CFA ESS1-5.4", "<p>Take <strong>Unit 3.1 CFA ESS1-5.4: Argue why the seafloor is young and the continents are old</strong> on Canvas (5 questions). If you score below 3 out of 4, a review for this target will open for you.</p>"),
    ],
)

# ===================================================================== DAY 7
DAY7 = dict(
    title="Review Day",
    focus="Which targets do I still need to work on before the CSA tomorrow?",
    targets=list(Q.TARGETS),
    notebook=[
        "Title: <strong>D7 Review Day</strong>. Add it to your table of contents.",
        "Copy the self-rating chart in Part 1 and fill it in.",
    ],
    parts=[
        ("Rate yourself", "<p>Rate each target from 1 (I need help) to 4 (I could teach it). Use your CFA scores to check your rating.</p>" +
            table(["Target", "My rating (1–4)", "My CFA score"], [[f"<strong>{c}</strong> {t}", "<br>", "<br>"] for c, t in TARGET_TEXT.items()])),
        ("Do the work that matches your scores", ol([
            "<strong>If you have not taken a CFA yet,</strong> take it now. The CFAs are in this module on Canvas.",
            "<strong>If a Mastery Path review opened for you,</strong> complete it now (they are in this module). Study your notebook first, then answer the 3 written questions.",
            "<strong>If you do not have any reviews open,</strong> your teacher may assign you the Enrichment choice board. Check Canvas, or ask.",
            "<strong>Everyone:</strong> finish your Frayer cards and make sure your Unit CER evidence log is complete.",
        ])),
        ("Vocabulary self-check", "<p>Cover the definitions on your Frayer cards. Explain each word aloud to a partner without reading: continental drift, seafloor spreading, mid-ocean ridge, subduction, trench, magnetic reversal, plate boundary, radiometric dating, half-life, fossil record.</p>"),
        ("Tomorrow", "<p>Tomorrow is the <strong>Unit 3.1 CSA</strong>. Study your notebook, your CFA results, and your reviews tonight.</p>"),
    ],
)

# ===================================================================== DAY 8
DAY8 = dict(
    title="Unit 3.1 CSA",
    focus="Show what you know about the age of Earth's crust.",
    targets=list(Q.TARGETS),
    notebook=["Bring a pencil. You do not need your notebook for the CSA."],
    parts=[
        ("About the CSA", "<p>The Common Summative Assessment has <strong>16 questions</strong> on all five targets: 14 multiple-choice, select-all, and true/false questions, and 2 written responses (a claim-evidence-reasoning argument using data, and a revision of an explanation). Read each question carefully and use the data provided.</p>"),
        ("Take the CSA", "<p>Open <strong>Unit 3.1 CSA: Age of the Earth (HS-ESS1-5)</strong> on Canvas when your teacher says to begin.</p>"),
        ("When you finish", "<p>Check your written answers. Then work quietly on any missing Canvas work. If your score on a target is below a 3, you will have a chance to reassess after an intervention.</p>"),
    ],
)

# ===================================================================== extra assignments
LESSON1_ASSIGN = ("Lesson 1: Where Did the Old Ocean Floor Go?",
    "<p><strong>Focus question:</strong> How old is the ocean floor compared with the continents?</p>"
    "<p>Complete the Day 1 notebook pages from the lesson page: warm-up guesses, I notice / I wonder, the 45-meter timeline, your first claim and initial model, and your first Frayer cards. Your teacher will check your notebook.</p>")
LESSON4_ASSIGN = ("Lesson 4: SketchNotes",
    "<p><strong>Focus question:</strong> If new crust is made at ridges, where does old ocean crust go, and why do the continents stay?</p>"
    "<p>Take a photo of your Day 4 SketchNotes (half page of notes and one page of sensemaking with a labeled subduction zone) and upload it here.</p>"
    "<table border=\"1\" cellpadding=\"6\" style=\"border-collapse:collapse\"><tbody><tr><th>4</th><td>Notes name all three boundary types with a landform for each. The cross-section correctly shows the trench, sinking plate, volcanic arc, and density labels, and an arrow for carbon.</td></tr>"
    "<tr><th>3</th><td>All parts are present with one small error or missing label.</td></tr>"
    "<tr><th>2</th><td>Some parts are missing or incorrect.</td></tr><tr><th>1</th><td>Few parts, or major errors.</td></tr></tbody></table>")
CER_ASSIGN = ("Unit 3.1 CER: Why is the seafloor so much younger than the continents?",
    "<p><strong>Question:</strong> Why is the seafloor so much younger than the continents?</p>"
    "<p>Write your argument using the sentence frames from the Day 6 page. Type it in the text box or upload your notebook page.</p>" + CER_FRAMES +
    "<h3>Scoring (4 points)</h3>" +
    table(["Score", "What it looks like"], [
        ["4", "Complete, accurate claim; at least two specific pieces of evidence from different lines (the age pattern, the density difference, or the oldest continental rock); reasoning that connects the evidence to the process (made at ridges, destroyed at subduction zones, continents too buoyant to sink); a counterclaim is addressed."],
        ["3", "Accurate claim; two specific pieces of evidence; reasoning present but incomplete or generic."],
        ["2", "Claim and one piece of evidence, or two vague pieces; reasoning missing or restates the evidence."],
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
def teacher_for(day, **kw):
    return kw

TEACHER = {}

TEACHER[1] = dict(
    glance="Launch the phenomenon: ocean floor is under about 200 million years old; continental material is up to 4.4 billion. Students guess, notice and wonder, scale the numbers on a 45 m timeline, write a first claim, and preview vocabulary. No CFA.",
    materials=["Seafloor age map (NOAA NCEI Age of the Ocean Floor map or any labeled copy) to project", "Meter stick, string, or a 45 m hallway (optional; the table works too)",
               "Frayer template", "Chromebooks", "Notebook paper"],
    agenda=[["0–5", "Warm-up guesses"], ["5–15", "Phenomenon: projected seafloor age map and the two data tables; notice and wonder in pairs"],
            ["15–25", "45-meter timeline: fill in the table; walk it if you have a hallway"], ["25–35", "Mystery and first claim; initial model"],
            ["35–43", "Vocabulary preview; assign two words per pair for Frayer cards"], ["43–45", "Exit ticket"]],
    notes=["Do not explain plate tectonics today. Collect wrong ideas (&ldquo;the ocean floor erodes away,&rdquo; &ldquo;the ocean is young&rdquo;) and revisit them on Day 6.",
           "A few small remnants of older crust exist in the Mediterranean (up to about 340 million years); they do not change the story and you can mention them if a student asks.",
           "The seafloor age map is a projected image; the page includes data tables as a text version."],
    key=["Timeline positions: oldest rock (4,000) = 5 m; oldest fossils (3,500) = 10 m; oldest ocean floor (200) = 43 m. All existing ocean floor is in the last 2 m of the 45 m timeline.",
         "Life first left fossils at about the 10 m mark, 3.3 billion years before the oldest surviving ocean floor.",
         "Sample first claim: The ocean floor is young because it keeps getting renewed (accept any attempt; this is the baseline)."],
    supports="Pre-fill the first row of the timeline for students who need it. Provide a number line instead of a hallway. Let students answer orally to a partner before writing.",
)

TEACHER[2] = dict(
    glance="Students test Wegener's idea with a continent puzzle and four fossil ranges, then evaluate three more lines of evidence. CFA ESS1-5.1 closes the lesson.",
    materials=["Printed map of the southern continents on a Pangaea-style layout with the continental shelf edge dashed (print one per pair; any Gondwana map works)", "Scissors, tape, colored pencils", "Chromebooks for the CFA"],
    agenda=[["0–4", "Warm-up (Mesosaurus)"], ["4–12", "Wegener's idea; model the fit with one pair on the projector"], ["12–35", "Fossil puzzle lab"],
            ["35–39", "More evidence table and Wegener's weakness"], ["39–45", "CFA ESS1-5.1"]],
    notes=["Cutting along the shelf edge matters: coastlines do not fit as well. Have a few pre-cut sets for students who struggle with fine motor tasks.",
           "Several students will say Mesosaurus swam. Ask what water it lived in.",
           "Keep the mechanism question open; Day 3 answers it."],
    key=["Warm-up: no; it lived in fresh water and could not cross a salt-water ocean, so the continents were probably joined.",
         "Evidence table: matching rock layers, mountain belts, and glacial scratches suggest the continents were joined; the shelf fit suggests they fit like puzzle pieces.",
         "Biology question: &ldquo;there was no gap.&rdquo; Heavy seeds and a freshwater animal could not cross an ocean; the same fossils appear in the same ages on separated continents.",
         "Wegener's weakness: he had no mechanism for what moves continents; scientists needed evidence of a process (seafloor spreading, found in the 1950s and 60s)."],
    supports="Provide the fossil colors already assigned. Let students point to the map and explain orally.",
)

TEACHER[3] = dict(
    glance="Students graph seafloor age against distance, find the rate (about 2.5 cm per year), model magnetic stripes with paper strips, and connect new crust to hydrothermal vent life and sediment thickness. CFA ESS1-5.2 closes the lesson.",
    materials=["Graph paper or Chromebooks", "Paper, scissors, red and blue pencils, rulers; 2 strips per pair (12 cm each)", "Photos or a short video of hydrothermal vents (optional)"],
    agenda=[["0–5", "Warm-up prediction"], ["5–15", "Age/sediment data and graph; rate calculation"], ["15–32", "Paper magnetic-stripe model"],
            ["32–37", "Vents and chemosynthesis"], ["37–40", "Sediment thickness"], ["40–45", "CFA ESS1-5.2"]],
    notes=["Strips must start with the oldest band at the end that goes through the slit first, so the youngest band appears at the center last.",
           "Vent timing: individual vents last years to decades; vent fields persist near the ridge axis where magma heat exists. At 2.5 cm per year crust takes tens of thousands of years to move 1 km. Keep the idea as &ldquo;vent communities need the heat found near the ridge.&rdquo;",
           "Data are simplified; if you want an authentic dataset, use NOAA seafloor age and DSDP/IODP sediment data."],
    key=["Prediction: the sample at the ridge is younger; the Brazil sample is older (up to about 120 million years old).",
         "Graph: a straight line through the origin. Slope 500 km per 20 million years = 25 km per million years = 2.5 cm per year (about the speed fingernails grow).",
         "3,500 km from the ridge: 3,500 ÷ 25 = 140 million years.",
         "Sediment gets thicker with age because older crust has had more time to collect clay and the shells of dead plankton.",
         "Stripes are mirror images because crust forms at the ridge, records the magnetic field, then splits and moves apart both ways.",
         "Vents occur at the ridge because that is where magma heats seawater; older crust has moved away from that heat."],
    supports="Pre-cut strips. Give a partially completed graph. Pair students for the model so one can pull and one can draw.",
)

TEACHER[4] = dict(
    glance="Students plot earthquakes and volcanoes, find the plate boundary pattern, use density to explain subduction and why continents survive, and connect plankton-shell carbon to the carbon cycle. SketchNotes. The CFA for this target is the next day's opener.",
    materials=["World map with latitude and longitude (one per student) and a plate boundaries map to project", "SketchNotes paper", "Optional density demo: oil and water, or clay of different densities"],
    agenda=[["0–4", "Warm-up"], ["4–20", "Plot and classify earthquake and volcano sites"], ["20–30", "Density and subduction"], ["30–34", "Carbon link"],
            ["34–44", "SketchNotes"], ["44–45", "Preview tomorrow's CFA"]],
    notes=["The CFA is intentionally placed at the start of Day 5 as spaced retrieval; Day 4 is already full.",
           "Density wording: ocean crust alone is slightly less dense than mantle; the old, cold ocean plate is denser than the hot mantle below it and sinks. Compare plate against plate (ocean plate versus continental plate) with students.",
           "Kīlauea is a deliberate exception (a hot spot inside a plate). It makes a good conversation, not a trick."],
    key=["Sites and boundary type: " + "; ".join(f"{k}: {v}" for k, v in SITES_KEY.items()) + ".",
         "Pattern: sites form lines along plate boundaries; the Ring of Fire is the largest.",
         "Boundaries: divergent (move apart; ridges and rift valleys), convergent (move together; trenches, volcanic arcs, mountains), transform (slide past; faults and earthquakes).",
         "The ocean plate sinks because it is denser.",
         "Two continental plates collide: both are buoyant, so neither subducts; the crust crumples upward into mountains (such as the Himalaya).",
         "Continents survive because they are less dense; the ocean floor is recycled at trenches, so its age rarely exceeds about 200 million years.",
         "Carbon is not lost: plankton shells carry carbon down; some returns to the air as CO₂ from volcanoes; the rest stays in the mantle for a long time."],
    supports="Give a pre-labeled map for students who struggle to plot coordinates. Provide a SketchNotes template with the sinking plate outlined.",
)

TEACHER[5] = dict(
    glance="Day starts with CFA ESS1-5.3. Then students do the half-life lab, match samples to radiometric dating methods, and compare the oldest Earth materials with meteorites and moon rocks. CFA ESS1-6.1 is tomorrow's opener.",
    materials=["50 coins (or candies with one marked side) and a cup per pair", "Graph paper or Chromebooks", "Chromebooks for the CFA"],
    agenda=[["0–8", "CFA ESS1-5.3"], ["8–12", "Hook and definitions"], ["12–30", "Half-life lab"], ["30–37", "Which clock?"], ["37–45", "Oldest materials and the missing record"]],
    notes=["Collect the coins at the end of the lab. A student can use dice or a spreadsheet for 'decay' if coins are short.",
           "Radiometric dating: zircon includes uranium but excludes lead when it forms, so any lead is from decay.",
           "ESS1-6 is a supporting standard; keep the focus on the idea that Earth's early rocks are gone but meteorites and the Moon preserve evidence."],
    key=["Expected counts (about): 50, 25, 12, 6, 3, 1. Each round about halves the sample; fractions 1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/64.",
         "Each round equals one half-life. A sample with 1/8 left is 3 half-lives old = 3 × 5,730 = 17,190 years.",
         "You cannot predict one coin, but the half-and-half pattern is reliable for very large numbers of atoms.",
         "Matching: the wooden spear — carbon-14; the 3-billion-year-old zircon — uranium-lead; the stromatolite in rock — uranium-lead on zircon in nearby igneous rock (carbon-14 is too short); the mammoth tusk — carbon-14.",
         "The oldest Earth rocks are younger than Earth because Earth's earliest rocks were destroyed or recycled by plate tectonics and erosion.",
         "Meteorites formed with the solar system and have changed little, so their ages (about 4.56 billion years) are the best estimate for Earth's age.",
         "Fossils that old are in continental rock; ocean floor of that age has been subducted."],
    supports="Provide a pre-drawn graph axis. Use a table of expected values for students to compare. Let students role-play the coin decay in a group.",
)

TEACHER[6] = dict(
    glance="CFA ESS1-6.1 opens the day. Students sort their evidence log, write the unit argument with sentence frames, give peer feedback, and finish with CFA ESS1-5.4. They submit the CER on Canvas.",
    materials=["Students' Unit CER evidence logs", "Sentence frames (on the page)", "Peer feedback checklist (on the page)", "Chromebooks"],
    agenda=[["0–8", "CFA ESS1-6.1"], ["8–13", "Sort evidence into three buckets; revisit the Day 1 claim"], ["13–27", "Draft the CER with frames"],
            ["27–38", "Peer feedback and revision"], ["38–45", "CFA ESS1-5.4"]],
    notes=["Revisit the Day 1 misconceptions. Ask students who changed their claim to say what changed their mind.",
           "Score the CER with the 4-point rubric on the assignment. Students who score below a 3 can revise during Day 7 or the reassessment window.",
           "Day 7's review and enrichment depend on these CFA scores."],
    key=["Sample strong claim: The ocean floor is much younger than the continents because it is continually made at mid-ocean ridges and recycled at subduction zones, while less-dense continental crust is too buoyant to be recycled.",
         "Evidence examples: crust age increases from 0 to 120 million years across 3,000 km (2.5 cm per year); the oldest ocean floor is about 200 million years; continental minerals are up to about 4.4 billion years; sediment is thicker on older crust.",
         "Reasoning: dense ocean plates sink at trenches while buoyant continents stay at the surface.",
         "Counterclaim: the ocean floor is young because it erodes away — sediment is thicker on older crust, so old crust is not worn away; it is subducted.",
         "Part 2 bucket sort: seafloor is young — made at ridges, recycled at trenches; continents are old — buoyant, not subducted; early record missing — recycled by plate tectonics and erosion."],
    supports="Provide a completed example for the first frame. Allow students to dictate or use speech-to-text.",
)

TEACHER[7] = dict(
    glance="Review day and cushion. Students rate themselves, take any CFA they have not taken, and complete the Mastery Path reviews that opened. Students with no reviews open can be assigned the Enrichment choice board (you assign it manually).",
    materials=["Students' notebooks, Frayer cards, and CFA scores", "Chromebooks", "Optional: Blooket or quiz game for students who finish"],
    agenda=[["0–5", "Self-rating chart"], ["5–38", "Work time: unfinished CFAs, Mastery Path reviews, or Enrichment"], ["38–43", "Vocabulary self-check with a partner"], ["43–45", "Preview CSA"]],
    notes=["Review assignments open automatically when a CFA score is below 3 of 4. Check the Gradebook for students with a CFA but no review yet.",
           "To assign the Enrichment piece: open Unit 3.1 Enrichment: Choice Board, use Assign To for the students you choose, and publish it. It is hidden from everyone else.",
           "There is no practice test in this unit; the CFAs and reviews serve as practice for the CSA."],
    key=["Self-rating chart is personal. Compare it with CFA scores and discuss any mismatch.",
         "Review answers are in the teacher key (HS-ESS1-5_teacher_key.md in the repo).",
         "Enrichment answers: see the notes on the Enrichment assignment; for Option 1, 1 km ÷ 2.5 cm per year = 40,000 years; for Option 3, 2 cm/yr × 1 million years = 20 km, and 100 cm in 50 years; for Option 4, Mars's crust is older because it is not recycled."],
    supports="Pull a small group for any target where several students scored below 3. Pair students who have completed reviews with those who need more practice.",
)

TEACHER[8] = dict(
    glance="CSA day. 16 questions, 14 auto-graded and two written responses (Q14 CER and Q16 revision) graded with the 4-point rubrics in the quiz.",
    materials=["Chromebooks with Canvas open", "Pencils"],
    agenda=[["0–3", "Directions"], ["3–43", "CSA"], ["43–45", "Collect Chromebooks; early finishers work quietly"]],
    notes=["Grade Q14 and Q16 in SpeedGrader; the rubric and sample answers are in each question's scoring data.",
           "Targets and CSA questions: ESS1-5.1 (Q1–3), ESS1-5.2 (Q4–6), ESS1-5.3 (Q7–9), ESS1-6.1 (Q10–12, Q16), ESS1-5.4 (Q13–15).",
           "For students below a 3 on a target, assign the matching Mastery Path review as intervention, then reassess."],
    key=["See HS-ESS1-5_teacher_key.md for answers to every CSA question and the full rubrics."],
    supports="Provide extended time, read aloud, or a quiet room as outlined in IEP/504 plans.",
)

DAYS = {1: DAY1, 2: DAY2, 3: DAY3, 4: DAY4, 5: DAY5, 6: DAY6, 7: DAY7, 8: DAY8}
