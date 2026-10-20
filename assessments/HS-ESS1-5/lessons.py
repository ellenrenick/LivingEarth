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
SITE_TABLE = table(["Site", "Type", "Latitude", "Longitude", "Boundary type (you decide)"],
                   [[s, t, la, lo, "<br>"] for s, t, la, lo in SITES])
BOUNDARIES = table(["Boundary", "Plates move…", "Example", "Landforms"], [
    ["Divergent", "apart", "Mid-Atlantic Ridge", "mid-ocean ridges, rift valleys"],
    ["Convergent", "toward each other", "Andes and the Peru-Chile Trench; Japan", "trenches, volcanic arcs, mountain ranges"],
    ["Transform", "sliding past each other", "San Andreas Fault", "faults and earthquakes"],
])

DAY1 = dict(
    title="Where Did the Old Ocean Floor Go?",
    focus="How old is the ocean floor compared with the continents, and how do moving plates make and destroy it?",
    targets=["ESS1-5.1"],
    notebook=[
        "Title: <strong>D1 Where Did the Old Ocean Floor Go?</strong>. Start your table of contents.",
        "Fill in the warm-up guesses, the I notice / I wonder table, and your first claim and model.",
        "Start your <strong>Unit CER</strong> on a new page. Write the question <em>Why is the seafloor so much younger than the continents?</em>, your first claim, and a 3-column evidence log (Day · Evidence · What it shows). You will add a row every day.",
        "Tape your plotted world map into your notebook and record the pattern answers.",
        "Start your <strong>Frayer cards</strong> for the 10 vocabulary words (list in Part 6). Finish them by Day 4.",
    ],
    parts=[
        ("Warm-up: guess", "<p>Earth is about 4.5 billion years old. Write down a guess for (a) the age of the <strong>oldest ocean floor</strong> and (b) the age of the <strong>oldest rock or mineral on the continents</strong>. Give one reason for each.</p>"),
        ("The phenomenon", "<p>Scientists have measured the age of rock from the ocean floor and from the continents. Here are some of the results.</p>"
            "<h3>Ocean floor</h3>" + OCEAN_AGES + "<p><em>Ages are rounded.</em></p><h3>Continents and life</h3>" + LAND_AGES +
            "<p><strong>Notice and wonder:</strong> write what you notice and what you wonder.</p>" + blank_table(["I notice…", "I wonder…"], 1)),
        ("The mystery and your first claim", "<p>Almost all of Earth's history is missing from the ocean floor. <strong>Why is the seafloor so much younger than the continents?</strong></p>"
            "<ol><li>Draw a quick model: a cross-section of an ocean with two continents on either side. Show where you think ocean floor might come from and where it might go.</li>"
            "<li>Write your first claim for the Unit CER. It is fine if it is wrong; we will revise it.</li></ol>"),
        ("Plot the pattern", "<p>Earth's rigid outer layer, the <strong>lithosphere</strong>, is broken into <strong>plates</strong> that move a few centimeters a year. Earthquakes and volcanoes mark where plates meet. Plot these sites on a world map (a different symbol for each type), then use a map of the plates to decide which kind of plate boundary is nearest to each site.</p>" + SITE_TABLE +
            ol(["Describe the pattern of your points. Do they appear at random or along lines?",
                "One site does not fit the pattern. Which one? What could explain it?"])),
        ("Three boundaries and the crust conveyor belt", "<p>Plates meet in three ways.</p>" + BOUNDARIES +
            "<p>At a <strong>mid-ocean ridge</strong> (a divergent boundary), plates pull apart, magma rises, and <strong>new ocean crust</strong> forms. At a <strong>subduction zone</strong> (a convergent boundary), an old ocean plate sinks into the mantle at a <strong>trench</strong> and the crust is destroyed.</p>"
            + ol(["On your model from Part 3, add the ridge, the trench, and arrows for plate motion. Where is crust made? Where is it destroyed?",
                  "Change your first claim if you want to. Which new words would you add?"])),
        ("Vocabulary preview and exit ticket", "<p>You will use these 10 words all unit. With a partner, make a Frayer card for the two words your teacher assigns. Finish all 10 by Day 4.</p>" +
            ol(["lithosphere (plate)", "plate boundary (divergent, convergent, transform)", "mid-ocean ridge", "subduction", "trench",
                "magnetic reversal", "craton (a continent's ancient core)", "radiometric dating", "half-life", "impact crater"]) +
            "<p><strong>Exit ticket:</strong> Write one thing you could measure or observe that would test your claim.</p>"),
    ],
)

# ===================================================================== DAY 2
SPREAD = table(["Distance from ridge (km)", "Crust age (million years)", "Sediment thickness (m)"], [
    ["0", "0", "about 0"], ["500", "20", "about 50"], ["1,000", "40", "about 150"], ["1,500", "60", "about 250"],
    ["2,000", "80", "about 350"], ["2,500", "100", "about 450"], ["3,000", "120", "about 550"],
])
NA_AGES = table(["Region of North America", "Direction and distance from the central core (km)", "Age of the crust"], [
    ["Canadian Shield (the central core)", "0", "about 2.7 billion years"],
    ["Grenville Province (Great Lakes to Quebec)", "east, about 1,200", "about 1.1 billion years"],
    ["Appalachian Mountains", "east, about 2,000", "about 400 million years"],
    ["Rocky Mountain region", "west, about 1,800", "about 150 million years"],
    ["Pacific Coast Ranges", "west, about 2,800", "about 50 million years"],
])

DAY2 = dict(
    title="Reading Rock Ages",
    focus="What patterns do the ages of ocean crust and continental crust follow?",
    targets=["ESS1-5.2"],
    notebook=[
        "Title: <strong>D2 Reading Rock Ages</strong>. Add it to your table of contents.",
        "Record your prediction, your age-versus-distance graph with the rate calculation, and your notes on the two age maps.",
        "<strong>Unit CER evidence log:</strong> add one row with a specific number from today's data.",
    ],
    parts=[
        ("Start with a CFA: ESS1-5.1", cfa_part(["ESS1-5.1"])),
        ("Warm-up: predict", "<p>A ship pulls up seafloor rock right at the Mid-Atlantic Ridge and another sample near the coast of Brazil. Which rock is older? Explain your prediction.</p>"),
        ("The ocean data", "<p>Scientists measured the age and the sediment thickness of the seafloor at sites along a line across the Mid-Atlantic Ridge. (These numbers are simplified from a spreading rate of about 2.5 cm per year.)</p>" + SPREAD +
            ol(["Graph <strong>crust age</strong> (y-axis) against <strong>distance from the ridge</strong> (x-axis). Describe the pattern in one sentence.",
                "Calculate the rate: distance &divide; time. (Convert: 1 km per million years = 0.1 cm per year.) Compare it with something that grows at about that speed.",
                "Predict the age of crust 3,500 km from the ridge.",
                "Graph <strong>sediment thickness</strong> against distance. Why would older crust have thicker sediment? (Hint: what falls to the seafloor from the ocean above, including the shells of dead plankton?)"])),
        ("Read the seafloor age map", "<p>Your teacher will project a map of the age of the ocean floor, with a color for each age.</p>" +
            ol(["Find the band of the youngest color. What is it, and where does it run?",
                "Describe how the colors change as you move away from it on <em>each</em> side. How do the two sides compare?",
                "Find the oldest color on the map. About how old is it? Where is it found?"])),
        ("The pattern on the continents", "<p>Continents have a rock-age pattern too. Each continent has an ancient <strong>core</strong>, called a <strong>craton</strong>. In North America it is the Canadian Shield. Here are the ages of the crust along a line through the continent. (Simplified from geologic maps.)</p>" + NA_AGES +
            ol(["Where is the oldest crust? How does the age change as you move away from it, in each direction?",
                "Sketch a graph of age against distance from the core. Does the pattern look the same east and west?",
                "Add this to your Unit CER log: one row for the ocean pattern and one for the continent pattern."])),
        ("Tomorrow", "<p>Tomorrow starts with <strong>Unit 3.1 CFA ESS1-5.2: Reading rock ages</strong> (5 questions). Study your graph and your two pattern statements tonight.</p>"),
    ],
)

# ===================================================================== DAY 3
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
TIMELINE = table(["Event", "Age (millions of years ago)", "Position on the 45 m timeline"], [
    ["Earth forms", "4,500", "0 m"],
    ["Oldest mineral on Earth (zircon)", "4,400", "1 m"],
    ["Oldest known rock", "4,000", "<br>"],
    ["Oldest fossils", "3,500", "<br>"],
    ["Oldest ocean floor", "200", "<br>"],
    ["Today", "0", "45 m"],
])
CRATERS = table(["Surface", "What it looks like", "Age from rocks or models"], [
    ["Moon highlands", "Covered with overlapping craters", "about 4.4 billion years or more"],
    ["Moon dark plains (maria)", "Far fewer craters; smooth lava plains", "about 3.2 to 3.9 billion years"],
    ["Mars southern highlands", "Heavily cratered", "about 3.7 billion years or more"],
    ["Earth (all land and ocean)", "About 190 impact craters known in total; most are eroded or buried", "Earth's surface is renewed constantly"],
])

DAY3 = dict(
    title="Reading Deep Time and Early Earth",
    focus="How do scientists find ages in the billions of years, and why do meteorites and moon rocks tell Earth's age better than Earth rocks do?",
    targets=["ESS1-6.1", "ESS1-6.2"],
    notebook=[
        "Title: <strong>D3 Reading Deep Time</strong>. Add it to your table of contents.",
        "Record your half-life data table, graph, and answers.",
        "Complete the timeline table and the crater table.",
        "<strong>Unit CER evidence log:</strong> add one row about the age of meteorites, moon rocks, or Earth's oldest minerals.",
    ],
    parts=[
        ("Start with a CFA: ESS1-5.2", cfa_part(["ESS1-5.2"])),
        ("Hook and definitions", "<p>The oldest ocean floor is only about 200 million years old, yet scientists say Earth is about 4.5 billion years old. How could anyone know that? Write one idea.</p>"
            "<p>Some atoms are <strong>unstable</strong>: they change into a different kind of atom at a steady rate. This is <strong>radioactive decay</strong>. The <strong>half-life</strong> is the time for half of the unstable (parent) atoms in a sample to decay into stable (daughter) atoms. Scientists use this as a clock: <strong>radiometric dating</strong>.</p>"),
        ("Half-life lab", ol(["Put 50 coins (or candies with a marked side) in a cup. Each coin is an atom of the parent isotope.",
                              "Shake the cup, spill the coins, and remove every coin that landed <strong>marked side up</strong>. These atoms have &ldquo;decayed.&rdquo; Count and record the coins left.",
                              "Put the remaining coins back and repeat for 6 rounds, or until none are left."]) + HALF_TABLE +
            ol(["Graph <strong>parent atoms left</strong> against <strong>round</strong>. Describe the shape.",
                "About what fraction remains after each round? What is each round equal to?",
                "If each round were one half-life of carbon-14 (5,730 years), how old would a sample be with 1/8 of its carbon-14 left?"])),
        ("Which clock for which sample?", CLOCKS +
            "<p>Zircon crystals take uranium into their structure when they form but leave out lead, so any lead inside came from decay. Pick the best method for each and explain in a few words:</p>" +
            ol(["A 9,000-year-old wooden spear", "A zircon crystal in a 3-billion-year-old granite", "A 20,000-year-old mammoth tusk"])),
        ("The oldest materials and a 45-meter timeline", OLD +
            "<p>Imagine Earth's whole history along a 45 m hallway: <strong>1 m = 100 million years</strong>. Earth forms at 0 m and today is at 45 m. Position = (4,500 − age in millions of years) ÷ 100.</p>" + TIMELINE +
            "<p>Fill in the missing positions. How much of the 45 m is covered by <strong>ocean floor that still exists</strong>?</p>"),
        ("The impact-crater record", "<p>Meteorites and asteroids have hit every rock planet and moon. A surface that has been exposed longer collects more craters.</p>" + CRATERS +
            ol(["Which surface is oldest? How do you know?",
                "Earth was hit as often as the Moon. Why does Earth show so few craters? Use plate tectonics, erosion, and weathering.",
                "Which kind of place is the best archive of the early solar system: Earth or the Moon? Explain."])),
        ("Why meteorites and moon rocks?", ol(["Why is the oldest Earth rock (4.0 billion years) younger than Earth itself?",
                                              "Why do scientists use meteorites and moon rocks, not Earth rocks, to find the age of the solar system (about 4.6 billion years)?",
                                              "The oldest fossils are in continental rock. Why are there no fossils that old in the ocean floor?"]) +
            "<p>Tomorrow you will use density to explain why ocean crust sinks. Review your half-life data and the oldest-materials table tonight.</p>"),
    ],
)

# ===================================================================== DAY 4
DAY4 = dict(
    title="Why the Ocean Is Young and the Continents Old",
    focus="How is ocean crust made, grown, and recycled, and how do continents grow and survive?",
    targets=["ESS1-5.3"],
    notebook=[
        "Title: <strong>D4 Why the Ocean Is Young, the Continents Old</strong>. Add it to your table of contents.",
        "Record your density answers and the crust-conveyor calculation.",
        "Make your <strong>SketchNotes</strong>: a half page of notes and one page of sensemaking (a cross-section showing a ridge, a trench, and a growing continent).",
        "<strong>Unit CER evidence log:</strong> add one row about density or continental growth.",
        "Finish your Frayer cards for all 10 words as homework.",
    ],
    parts=[
        ("Warm-up", "<p>You know the ocean floor is under 200 million years old. Where does the old ocean crust go, and what must be different about the continents?</p>"),
        ("Why does some crust sink?", "<p>At a <strong>convergent</strong> boundary where an ocean plate meets a continent, the ocean plate bends and sinks into the mantle. This is <strong>subduction</strong>, and it makes a deep <strong>trench</strong> and a line of volcanoes on land.</p>" +
            table(["Material", "Average density (g/cm³)"], [["Ocean crust (basalt)", "about 3.0"], ["Continental crust (granite)", "about 2.7"]]) +
            "<p>Old ocean plates are cold, so they are denser than the hot mantle rock beneath them.</p>"
            + ol(["When an ocean plate meets a continental plate, which one sinks? Why?",
                  "What happens when two continental plates collide (such as India and Asia)? Use the density data to explain why mountains rise instead of a trench forming.",
                  "Continents stay at the surface for billions of years; the ocean floor is recycled in about 200 million years. Use density to explain both."])),
        ("The life of ocean crust", "<p>Crust made at a ridge moves away at about 2.5 cm per year and sinks at a trench.</p>" +
            ol(["A piece of crust is made at the Mid-Atlantic Ridge and travels 3,000 km. How long does the trip take at 25 km per million years? (Show your work.)",
                "The oldest ocean floor is about 200 million years old. About how far (km) can crust travel in that time at the same rate?",
                "Explain why no ocean floor is older than that, even though the ocean basins have existed for much longer."])),
        ("How continents grow", "<p>Continental crust is not made at ridges and not recycled the way ocean crust is. Each continent has an ancient <strong>core</strong>. Over hundreds of millions of years, volcanic island arcs and pieces of crust crash into its edge and are added to it, so the continent grows outward like rings on a tree. Look again at your North America table from Day 2.</p>" +
            ol(["Why is the crust at the edge of a continent younger than the crust at its core?",
                "Draw a cross-section of a continent with an ancient core, a younger belt next to it, and a subduction zone at the edge. Show where new material is added.",
                "Compare the life of ocean crust (made, moves, destroyed) with the life of continental crust (core, growth, survival). Write two sentences."])),
        ("What rides the plate down?", "<p>The ocean floor is covered in sediment, including the shells of dead plankton, which contain carbon. When a plate subducts, some of this sediment goes down with it. Some of the carbon returns to the air as carbon dioxide when volcanoes erupt. Connect to Unit 1.2: is carbon lost? Explain.</p>"),
        ("SketchNotes", "<p><strong>Half page of notes:</strong> the life of ocean crust (made, moves, sinks) and how continents grow. <strong>One page of sensemaking:</strong> draw a cross-section with a ridge, an ocean plate moving away, a trench, a volcanic arc, and a continent with an ancient core and a younger edge. Label density and add an arrow showing where a plankton shell's carbon goes.</p>"
            "<p>Take a photo of your SketchNotes and turn them in on Canvas: <strong>Lesson 4: SketchNotes</strong>.</p>"
            "<p>Tomorrow starts with <strong>CFA ESS1-5.3: Why ocean crust is young and continents are old</strong> (5 questions). Study your SketchNotes tonight.</p>"),
    ],
)

# ===================================================================== DAY 5
HAWAII = table(["Volcano or island", "Distance northwest of Kīlauea (km)", "Age of its oldest rock (million years)"], [
    ["Kīlauea (Hawaiʻi Island, active now)", "0", "0"],
    ["Oʻahu", "about 400", "about 4"],
    ["Kauaʻi", "about 500", "about 5"],
    ["Midway Atoll", "about 2,500", "about 28"],
])
FOSSILS = table(["Organism", "What it was", "Found in", "Age"], [
    ["<em>Glossopteris</em>", "seed fern (heavy seeds)", "South America, Africa, India, Australia, Antarctica", "about 250–300 million years"],
    ["<em>Mesosaurus</em>", "freshwater reptile", "South America, southern Africa", "about 280 million years"],
    ["<em>Lystrosaurus</em>", "land animal", "Africa, India, Antarctica", "about 250 million years"],
])
EVIDENCE_EVAL = table(["Line of evidence", "Measured or quantitative?", "Shows past or present motion?", "Independent of the others?", "Strength (1–4)"], [
    ["Rock ages across a ridge", "<br>", "<br>", "<br>", "<br>"],
    ["Magnetic stripes", "<br>", "<br>", "<br>", "<br>"],
    ["GPS and Hawaiian island ages", "<br>", "<br>", "<br>", "<br>"],
    ["Matching fossils and rocks", "<br>", "<br>", "<br>", "<br>"],
])

DAY5 = dict(
    title="Evidence for Moving Crust",
    focus="How strong is the evidence that the crust has moved and is still moving?",
    targets=["ESS1-5.4"],
    notebook=[
        "Title: <strong>D5 Evidence for Moving Crust</strong>. Add it to your table of contents.",
        "Tape your finished paper stripes into your notebook and answer the stripe questions.",
        "Record the Hawaiian-chain calculation and the evidence-evaluation table.",
        "<strong>Unit CER evidence log:</strong> add one row about the strongest evidence you saw today.",
    ],
    parts=[
        ("Start with a CFA: ESS1-5.3", cfa_part(["ESS1-5.3"])),
        ("Warm-up", "<p>How could a scientist show that a continent or the seafloor moved millions of years ago? How could they show that it is moving <em>today</em>? List two ideas for each.</p>"),
        ("Evidence A: magnetic stripes (paper model)", "<p>As lava hardens at a ridge, tiny magnetic minerals line up with Earth's magnetic field. Earth's field has flipped many times, so the new crust records <strong>stripes</strong> of normal and reversed magnetism. This is a <strong>magnetic reversal</strong> record.</p>"
            "<p><strong>Make the strips:</strong> Cut two identical paper strips, each 12 cm long. Starting from the end you will push through the slit first (this becomes the <em>oldest</em> crust), color these bands (2 cm = 1 million years):</p>" +
            table(["Band (from the end you push first)", "Color", "Length", "Age it represents"], [
                ["1", "Reversed (blue)", "3.4 cm", "about 3.6–5.3 million years"],
                ["2", "Normal (red)", "2.0 cm", "about 2.6–3.6 million years"],
                ["3", "Reversed (blue)", "3.6 cm", "about 0.8–2.6 million years"],
                ["4", "Normal (red)", "1.6 cm", "0–0.8 million years (youngest)"]]) +
            ol(["Cut a slit in a folded sheet of paper. This slit is the <strong>mid-ocean ridge</strong>.",
                "Put the two strips back to back and push them up through the slit from underneath. Pull them slowly apart, one to each side.",
                "Draw what you see. Where is the youngest crust? The oldest? Are the two sides the same?"]) +
            "<p><strong>Explain:</strong> What does a pair of mirror-image stripe patterns tell you about how the crust formed?</p>"),
        ("Evidence B: measured motion", "<p>Satellites and GPS stations measure plate motion directly: about 2 cm per year apart across the Mid-Atlantic Ridge in Iceland, and about 7 to 8 cm per year for the Pacific plate near Hawaii. The Hawaiian Islands are a chain of volcanoes made as the Pacific plate moves over a fixed hot spot under the Big Island. (Rounded values.)</p>" + HAWAII +
            ol(["Calculate the rate of the Pacific plate from Kauaʻi: distance &divide; time. (1 km per million years = 0.1 cm per year.) Do the same for Midway.",
                "Compare your rates with the GPS value of 7 to 8 cm per year. What do you notice?",
                "Predict where the next Hawaiian island will form. Explain."])),
        ("Evidence C: matching fossils and rocks (past motion)", "<p>In 1912 Alfred Wegener proposed that the continents were once joined, partly because the same fossils turn up on separated continents.</p>" + FOSSILS +
            "<p>Rock layers and mountain belts also match across oceans (the Appalachians and the mountains of Scotland), and ice-age scratches line up when the southern continents are fitted together. Wegener could not explain what force moved the continents, so many scientists doubted him until seafloor spreading was found.</p>"
            + ol(["<em>Mesosaurus</em> lived in fresh water and <em>Glossopteris</em> had heavy seeds. Why are they good evidence that lands were once joined?",
                  "What can this evidence not tell you that GPS can?"])),
        ("Evaluate the evidence", "<p>Fill in the table for each line of evidence (use yes/no, past/present, and a strength rating from 1 = weak to 4 = very strong).</p>" + EVIDENCE_EVAL +
            ol(["Which line of evidence is strongest for <em>current</em> motion? For <em>past</em> motion? Explain each in one sentence.",
                "GPS gives about 2 cm per year in Iceland and rock ages give about 2.5 cm per year. Why does the agreement of two independent methods make the case stronger?",
                "Name one new finding that would weaken the idea that the seafloor spreads from ridges."]) +
            "<p>Tomorrow starts with <strong>CFA ESS1-5.4: Evidence for moving crust</strong> (5 questions). Study your evaluation table tonight.</p>"),
    ],
)

# ===================================================================== DAY 6
CER_FRAMES = ul([
    "<strong>Claim:</strong> Plate tectonics explains the ages of Earth's crustal rocks (very well / partly / poorly) because ______.",
    "<strong>Evidence 1 (ocean):</strong> The seafloor age data show ______ (give a number or a pattern).",
    "<strong>Evidence 2 (ocean):</strong> The oldest ocean floor is only about ______ million years old because ______.",
    "<strong>Evidence 3 (continents):</strong> Continental crust as old as ______ exists, and in North America the crust gets ______ toward the edges.",
    "<strong>Reasoning:</strong> Because ocean plates are ______ than continental crust, they ______ at subduction zones, while continents ______.",
    "<strong>Limit or counterclaim:</strong> One thing this evidence cannot show is ______. OR: Someone might say the ocean floor is young because ______. This does not fit the evidence because ______.",
])
CER_CHECK = ul(["The claim says how well the theory explains the ages and gives a cause.",
                "Each piece of evidence is specific (a number or a named pattern), and both ocean and continental crust are used.",
                "At least two different kinds of evidence are used.",
                "The reasoning explains <em>why</em> the evidence supports the claim.",
                "A limit or a counterclaim is addressed with evidence."])
STORY_FRAMES = ul([
    "About ______ billion years ago, ______ happened. The evidence is ______.",
    "About ______ billion years ago, ______ happened. The evidence is ______.",
    "About ______ billion years ago, ______ happened. The evidence is ______.",
    "Earth's earliest record is missing because ______. Scientists fill the gap with evidence from ______.",
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
        "Sort your evidence into the three buckets in Part 2.",
    ],
    parts=[
        ("Start with a CFA: ESS1-5.4", cfa_part(["ESS1-5.4"])),
        ("Sort your evidence", "<p>Look at your evidence log. Sort each row into a bucket:</p>" +
            table(["The seafloor is young because…", "The continents are old because…", "The early record is missing because…"], [["<br><br><br>", "<br><br><br>", "<br><br><br>"]]) +
            "<p>Look back at your Day 1 claim. What would you change now?</p>"),
        ("Evaluate the theory (ESS1-5.5)", "<p>Answer: <strong>How well does the theory of plate tectonics explain the ages of Earth's crustal rocks?</strong> Use the sentence frames. Strong writers use all of them; you may add more.</p>" + CER_FRAMES +
            "<p><strong>Data you may use:</strong> seafloor age and distance from the ridge (Day 2 table); oldest ocean floor about 200 million years; oldest continental mineral about 4.4 billion years; North American crust from about 2.7 billion years at the core to about 400 million years in the Appalachians; ocean crust about 3.0 g/cm³ and continental crust about 2.7 g/cm³; GPS and rock-age spreading rates (2 and 2.5 cm per year); oldest fossils about 3.5 billion years in continental rock.</p>"
            "<p>Submit your finished argument on Canvas: <strong>Unit 3.1 CER</strong> (Part A).</p>"),
        ("Peer feedback", "<p>Trade with a partner. Check the list below and write one &ldquo;star&rdquo; (something strong) and one &ldquo;step&rdquo; (something to improve). Then revise your own.</p>" + CER_CHECK),
        ("Tell Earth's story (ESS1-6.3)", "<p>Use the evidence cards to build a short account of how Earth formed and what happened in its early history.</p>" + EVIDENCE_CARDS +
            "<p>Write your account with these frames (Part B of <strong>Unit 3.1 CER</strong> on Canvas):</p>" + STORY_FRAMES),
        ("Take the last CFA", "<p>Take <strong>Unit 3.1 CFA ESS1-5.5: How well plate tectonics explains rock ages</strong> (5 questions) at the start of your next class or on the work day, as your teacher tells you. If you score below 3 out of 4, a review for that target will open for you.</p>"),
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
            "<strong>Everyone:</strong> finish your Frayer cards and make sure your Unit CER evidence log and your CER are complete.",
        ])),
        ("Vocabulary self-check", "<p>Cover the definitions on your Frayer cards. Explain each word aloud to a partner without reading: lithosphere, plate boundary, mid-ocean ridge, subduction, trench, magnetic reversal, craton, radiometric dating, half-life, impact crater.</p>"),
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
    "<p>Complete the Day 1 notebook pages from the lesson page: warm-up guesses, I notice / I wonder, your first claim and initial model, your plotted world map with the pattern answers, and your first Frayer cards. Your teacher will check your notebook.</p>")
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

TEACHER[1] = dict(
    glance="Launch the phenomenon (ocean floor under about 200 million years; continental material up to 4.4 billion), then teach ESS1-5.1: students plot earthquakes and volcanoes to find plate boundaries, name the three boundary types, and add the ridge and trench to their model of where ocean crust is made and destroyed. No CFA today; CFA ESS1-5.1 opens Day 2.",
    materials=["Seafloor age map (NOAA NCEI Age of the Ocean Floor map or any labeled copy) to project", "World map with latitude and longitude (one per student) and a plate boundaries map to project",
               "Frayer template", "Colored pencils", "Notebook paper"],
    agenda=[["0–3", "Warm-up guesses"], ["3–11", "Phenomenon: projected seafloor age map and the two data tables; notice and wonder in pairs"],
            ["11–17", "Mystery, initial model, and first claim"], ["17–32", "Plot earthquakes and volcanoes; find the pattern"],
            ["32–40", "Three boundary types and the crust conveyor belt; revise the model"], ["40–45", "Vocabulary preview (two words per pair) and exit ticket"]],
    notes=["Do not explain why crust is young yet. Collect wrong ideas (&ldquo;the ocean floor erodes away,&rdquo; &ldquo;the ocean is young&rdquo;) and revisit them on Day 6.",
           "A few small remnants of older crust exist in the Mediterranean (up to about 340 million years); they do not change the story and you can mention them if a student asks.",
           "The plotting activity can run as a jigsaw: each group plots five sites and shares. Kīlauea is a deliberate exception (a hot spot inside a plate); it makes a good conversation, not a trick.",
           "The seafloor age map is a projected image; the page includes data tables as a text version."],
    key=["Sites and boundary type: " + "; ".join(f"{k}: {v}" for k, v in SITES_KEY.items()) + ".",
         "Pattern: sites form lines along plate boundaries; the Ring of Fire is the largest.",
         "Boundaries: divergent (move apart; ridges, rift valleys), convergent (move together; trenches, volcanic arcs, mountains), transform (slide past; faults and earthquakes).",
         "Crust is made at mid-ocean ridges (divergent boundaries) and destroyed at trenches (subduction at convergent boundaries).",
         "Sample first claim: The ocean floor is young because it keeps getting renewed (accept any attempt; this is the baseline)."],
    supports="Give a pre-labeled map for students who struggle to plot coordinates. Let students answer orally to a partner before writing.",
)

TEACHER[2] = dict(
    glance="CFA ESS1-5.1 opens the day. Students graph seafloor age against distance, find the spreading rate (about 2.5 cm per year), read a seafloor age map, and find the matching pattern in North American continental crust (oldest at the Canadian Shield core). CFA ESS1-5.2 opens Day 3.",
    materials=["Graph paper or Chromebooks", "Seafloor age map to project (NOAA NCEI)", "A map of North American crust ages (USGS geologic provinces, or the table on the page)", "Chromebooks for the CFA"],
    agenda=[["0–8", "CFA ESS1-5.1"], ["8–12", "Warm-up prediction"], ["12–25", "Ocean data and graph; rate; sediment"], ["25–33", "Read the seafloor age map"], ["33–45", "Continental age pattern; add rows to the CER log"]],
    notes=["Rate arithmetic: 500 km in 20 million years = 25 km per million years = 2.5 cm per year. Convert with 1 km per million years = 0.1 cm per year.",
           "The target is reading and describing the pattern, not explaining it. Save the &lsquo;why&rsquo; for Days 3 to 5.",
           "North America table is simplified from geologic maps (ages when the crust was formed or added). Use the USGS provinces map if you have it.",
           "Data are simplified; if you want an authentic dataset, use NOAA seafloor age and DSDP/IODP sediment data."],
    key=["Prediction: the sample at the ridge is younger; the Brazil sample is older (up to about 120 million years old).",
         "Graph: a straight line through the origin. Slope 500 km per 20 million years = 25 km per million years = 2.5 cm per year (about the speed fingernails grow).",
         "3,500 km from the ridge: 3,500 ÷ 25 = 140 million years.",
         "Sediment gets thicker with age because older crust has had more time to collect clay and the shells of dead plankton.",
         "Age map: the youngest band runs along the ridge; ages increase on both sides and the two sides match; the oldest color (about 180 to 200 million years) is far from the ridges, for example the western Pacific.",
         "Continents: the oldest crust is in the central core (Canadian Shield, about 2.7 billion years); the crust gets younger moving outward both east and west."],
    supports="Provide a partially completed graph. Use a table of expected values so students can compare. Pair students for the age-map reading.",
)

TEACHER[3] = dict(
    glance="CFA ESS1-5.2 opens the day. Students do the half-life lab, pick the right dating method for a sample, compare the oldest Earth materials with meteorites and moon rocks on a 45 m timeline, read the impact-crater record, and explain why meteorites and moon rocks give the age of the solar system.",
    materials=["50 coins (or candies with one marked side) and a cup per pair", "Graph paper or Chromebooks", "Images of the Moon and Mars surfaces (optional)", "Chromebooks for the CFA"],
    agenda=[["0–7", "CFA ESS1-5.2"], ["7–10", "Hook and definitions"], ["10–22", "Half-life lab"], ["22–26", "Which clock?"], ["26–34", "Oldest materials and the 45 m timeline"],
            ["34–40", "Impact-crater record"], ["40–45", "Why meteorites and moon rocks; preview tomorrow"]],
    notes=["Collect the coins at the end of the lab. A student can use dice or a spreadsheet for 'decay' if coins are short.",
           "Radiometric dating: zircon includes uranium but excludes lead when it forms, so any lead is from decay.",
           "ESS1-6 is a supporting standard, taught here to feed ESS1-5.3 and ESS1-5.5. ESS1-6 has no CFAs or reviews and is not on the CSA.",
           "Crater counts: the Moon has no plate tectonics and almost no weathering, so craters last. Earth has about 190 known craters because erosion, volcanism, and plate tectonics erase them."],
    key=["Expected counts (about): 50, 25, 12, 6, 3, 1. Each round about halves the sample; fractions 1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/64.",
         "Each round equals one half-life. A sample with 1/8 left is 3 half-lives old = 3 × 5,730 = 17,190 years.",
         "Matching: the wooden spear — carbon-14; the 3-billion-year-old zircon — uranium-lead; the mammoth tusk — carbon-14.",
         "Timeline positions: oldest rock (4,000) = 5 m; oldest fossils (3,500) = 10 m; oldest ocean floor (200) = 43 m. All existing ocean floor is in the last 2 m of the 45 m timeline.",
         "Craters: the Moon highlands are oldest (most craters). Earth shows few because plate tectonics, erosion, and weathering erase them. The Moon is the better archive of the early solar system.",
         "The oldest Earth rocks are younger than Earth because Earth's earliest rocks were destroyed or recycled by plate tectonics and erosion.",
         "Meteorites formed with the solar system and have changed little, so their ages (about 4.56 billion years) are the best estimate; the Moon is geologically quiet and kept its early rocks.",
         "Fossils that old are in continental rock; ocean floor of that age has been subducted."],
    supports="Provide a pre-drawn graph axis. Let students role-play the coin decay in a group. Give a partially filled crater table.",
)

TEACHER[4] = dict(
    glance="Students use density to explain subduction, trace the life of ocean crust, learn how continents grow outward from an ancient core, connect plankton-shell carbon to the carbon cycle, and make SketchNotes. CFA ESS1-5.3 opens Day 5.",
    materials=["SketchNotes paper", "Optional density demo: oil and water, or clay of different densities", "Chromebooks"],
    agenda=[["0–2", "Warm-up"], ["2–12", "Density and subduction"], ["12–18", "Life of ocean crust"], ["18–28", "How continents grow"],
            ["28–32", "Carbon link"], ["32–45", "SketchNotes; preview tomorrow's CFA"]],
    notes=["Density wording: ocean crust alone is slightly less dense than mantle; the old, cold ocean plate is denser than the hot mantle below and sinks. Compare plate against plate (ocean plate versus continental plate) with students.",
           "Continental growth is simplified: arcs and pieces of crust (terranes) collide with and are added to the margin; the continent is also eroded and parts are recycled, but most of it stays.",
           "There is no CFA today, so use the extra time for SketchNotes. CFA ESS1-5.3 opens Day 5."],
    key=["The ocean plate sinks because it is denser (3.0 versus 2.7 g/cm³).",
         "Two continental plates collide: both are buoyant, so neither subducts; the crust crumples upward into mountains (such as the Himalaya).",
         "Continents survive because they are less dense; the ocean floor is recycled at trenches, so its age rarely exceeds about 200 million years.",
         "3,000 km ÷ 25 km per million years = 120 million years. In 200 million years crust travels 200 × 25 = 5,000 km.",
         "Edge crust is younger because volcanic arcs and pieces of crust were added to the edge of the continent later.",
         "Ocean crust: made at a ridge, moves, is destroyed in under 200 million years. Continental crust: ancient core, grows outward, survives for billions of years.",
         "Carbon is not lost: plankton shells carry carbon down; some returns to the air as CO₂ from volcanoes; the rest stays in the mantle for a long time."],
    supports="Provide a SketchNotes template with the sinking plate outlined. Let students dictate the comparison sentences.",
)

TEACHER[5] = dict(
    glance="CFA ESS1-5.3 opens the day. Students rotate through evidence for moving crust: a paper magnetic-stripe model, measured motion (GPS and the Hawaiian island chain), and fossil and rock matches. They evaluate the strength of each line of evidence with a table. CFA ESS1-5.4 opens Day 6.",
    materials=["Paper, scissors, red and blue pencils, rulers; 2 strips per pair (12 cm each)", "Map of the Hawaiian chain (optional)", "Fossil range cards (optional)", "Chromebooks for the CFA"],
    agenda=[["0–7", "CFA ESS1-5.3"], ["7–10", "Warm-up"], ["10–20", "Evidence A: paper magnetic-stripe model"], ["20–28", "Evidence B: measured motion"], ["28–33", "Evidence C: fossils and rocks"],
            ["33–44", "Evaluate the evidence"], ["44–45", "Preview tomorrow's CFA"]],
    notes=["Strips must start with the oldest band at the end that goes through the slit first, so the youngest band appears at the center last.",
           "Hawaiian chain numbers are rounded: Oʻahu about 400 km and 4 million years, Kauaʻi about 500 km and 5 million years, Midway about 2,500 km and 28 million years. The rates come out near 9 to 10 cm per year; GPS gives about 7 to 8 cm per year. That is close but not identical, which is a good moment to talk about rounded data.",
           "ESS1-5.4 is DOK 3: students judge strength. Push for criteria (measured, independent, predictions hold, limits named), not just opinions.",
           "Keep the vocabulary on the evidence: rock ages, stripes, measured motion."],
    key=["Stripes are mirror images because crust forms at the ridge, records the magnetic field, then splits and moves apart both ways.",
         "Hawaii: Kauaʻi 500 km ÷ 5 million years = 100 km per million years = 10 cm per year. Midway 2,500 ÷ 28 ≈ 90 km per million years ≈ 9 cm per year. Similar to GPS (7 to 8 cm per year); the next island forms southeast of Hawaiʻi Island (Lōʻihi seamount).",
         "Mesosaurus (freshwater) and Glossopteris (heavy seeds) could not cross oceans, so the lands were once joined. Fossils cannot give the rate or show present motion.",
         "Evaluation table (sample): rock ages — quantitative, past, independent, 4; stripes — quantitative, past, independent, 4; GPS and Hawaii — measured, present (GPS) and past (island ages), independent, 4; fossils and rocks — qualitative, past, partly independent, 2 to 3.",
         "Current motion: GPS. Past motion: rock ages and stripes agree, plus fossils.",
         "Two independent methods agree on a rate, which is hard to explain by chance, so the conclusion is more trustworthy.",
         "A weakening finding: crust at the ridge being old and getting younger away from it."],
    supports="Pre-cut strips. Give the evaluation table with one row completed. Pair students for the model.",
)

TEACHER[6] = dict(
    glance="CFA ESS1-5.4 opens the day. Students sort their evidence log, write an evaluation of how well plate tectonics explains the ages of crustal rocks (Part A), give peer feedback, and build a short account of Earth's formation from evidence cards (Part B). CFA ESS1-5.5 follows on the work day or at the start of Day 7.",
    materials=["Students' Unit CER evidence logs", "Sentence frames and evidence cards (on the page)", "Peer feedback checklist (on the page)", "Chromebooks"],
    agenda=[["0–7", "CFA ESS1-5.4"], ["7–11", "Sort evidence into three buckets; revisit the Day 1 claim"], ["11–24", "Draft the evaluation (Part A) with frames"],
            ["24–31", "Peer feedback and revision"], ["31–42", "Tell Earth's story (Part B)"], ["42–45", "Preview CFA ESS1-5.5"]],
    notes=["Revisit the Day 1 misconceptions. Ask students who changed their claim to say what changed their mind.",
           "Score the CER with the 4-point rubric on the assignment. Students who score below a 3 can revise during the work day, Day 7, or the reassessment window.",
           "ESS1-5.5 asks for an evaluation, not just an explanation. A strong response says how well and names a limit (no ocean crust older than about 200 million years remains).",
           "Part B (ESS1-6.3) is supporting and has no CFA; it is not on the CSA. Do not let it crowd out Part A."],
    key=["Sample strong claim: Plate tectonics explains the ages of Earth's crustal rocks very well because ocean crust is made at ridges and recycled at subduction zones, while less-dense continental crust survives and grows outward.",
         "Evidence examples: crust age increases from 0 to 120 million years across 3,000 km (2.5 cm per year); the oldest ocean floor is about 200 million years; continental minerals are up to about 4.4 billion years; North American crust is about 2.7 billion years at its core and about 400 million years in the Appalachians.",
         "Reasoning: dense ocean plates sink at trenches while buoyant continents stay at the surface and grow at their edges.",
         "Limit: no ocean floor older than about 200 million years remains, so early Earth must be studied in continental rock and in meteorites. Counterclaim: the ocean floor erodes away — sediment is thicker on older crust, so old crust is not worn away; it is subducted.",
         "Part B sample: 4.56 billion years ago the solar system formed (meteorites); about 4.4 billion years ago solid crust existed (zircons, moon rocks); about 3.5 billion years ago life existed (stromatolites). The early record is missing because plate tectonics and erosion recycled it, so scientists use meteorites, the Moon, and other planets."],
    supports="Provide a completed example for the first frame. Allow students to dictate or use speech-to-text.",
)

TEACHER[7] = dict(
    glance="Review day and cushion. Students rate themselves on all eight targets, take any CFA they have not taken (including ESS1-5.5), and complete the Mastery Path reviews that opened. Students with no reviews open can be assigned the Enrichment choice board (you assign it manually).",
    materials=["Students' notebooks, Frayer cards, and CFA scores", "Chromebooks", "Optional: Blooket or quiz game for students who finish"],
    agenda=[["0–5", "Self-rating chart"], ["5–38", "Work time: unfinished CFAs, Mastery Path reviews, or Enrichment"], ["38–43", "Vocabulary self-check with a partner"], ["43–45", "Preview the CSA"]],
    notes=["Review assignments open automatically when a CFA score is below 3 of 4. Check the Gradebook for students with a CFA but no review yet.",
           "To assign the Enrichment piece: open Unit 3.1 Enrichment: Choice Board, use Assign To for the students you choose, and publish it. It is hidden from everyone else.",
           "The CSA covers ESS1-5.1 to ESS1-5.5 only. Tell students that ESS1-6 practice supports ESS1-5.3 and ESS1-5.5 but is not tested.",
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
