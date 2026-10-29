# -*- coding: utf-8 -*-
"""Unit 3.2 Age of the Earth (HS-ESS1-5), rebuilt to the 26-27 workbook pacing: 12 days, 10 lessons
(lessons 7 and 8 each span two days)."""
from lib import *

T = {
    '5.1': 'ESS1-5.1: I can describe Earth\'s outer layer as moving plates, name three kinds of plate boundaries, and describe where ocean crust is made and where it sinks back down.',
    '5.2': 'ESS1-5.2: I can read a rock-age map and describe the pattern in the ages.',
    '5.3': 'ESS1-5.3: I can explain why ocean crust is young and why continents are oldest at their ancient cores.',
    '5.4': 'ESS1-5.4: I can judge how strong the evidence is that the crust has moved and is still moving.',
    '5.5': 'ESS1-5.5: I can judge how well plate tectonics explains the ages of rocks, using evidence.',
    '6.1': 'ESS1-6.1 (supporting): I can list the evidence scientists use to learn about early Earth.',
    '6.2': 'ESS1-6.2 (supporting): I can explain why meteorites and moon rocks tell Earth\'s age better than Earth rocks do.',
    '6.3': 'ESS1-6.3 (supporting): I can use evidence from rocks, meteorites, and other planets to tell how Earth formed.',
}
ILLUS = 'Illustrative data: simplified numbers for class, not from a single study.'
SRC_AGES = ('Sources: ocean-floor ages, Müller et al. (2008), Science 319:1357-1362, "Age, spreading rates, and spreading asymmetry of the world\'s ocean crust" (oldest ocean floor about 180 million years; '
            'rounded); oldest mineral (zircon), Wilde et al. (2001), Nature 409:175-178 (about 4.4 billion years, Jack Hills, Western Australia); oldest known rock, Bowring and Williams (1999), '
            'Contributions to Mineralogy and Petrology 134:3-16 (Acasta Gneiss, Canada, about 4.0 billion years); oldest fossils, Allwood et al. (2006), Nature 441:714-718 (about 3.5 billion years, Western Australia).')


def tb(header, rows, cols=None, rowh=None):
    return ('table', {'header': header, 'rows': rows, 'cols': cols, 'rowh': rowh})


def item(lesson, title, kicker, use, copies, body, key):
    return dict(lesson=lesson, title=title, kicker=kicker, use=use, copies=copies, body=body, key=key)


items = []
# ================= Lesson 1: Launch =================
items.append(item(1, 'Pre-check (not graded)', 'Pre-assessment', 'Glue under "Pre-check" in the notebook; keep to compare at the end of the unit', 'One per student',
    [('p', 'Answer in your notebook. It is OK to guess. We will come back to these at the end of the unit.'),
     ('p', '1. About how old is Earth? ______________________'),
     ('p', '2. What is the oldest rock or mineral that has been found on Earth, about how old is it, and where was it found? ______________________'),
     ('p', '3. Is the ocean floor older, younger, or about the same age as the continents? What is your reason? ______________________'),
     ('lines', 3),
     ('p', '4. What do you think the Earth\'s outer layer is made of, and does it ever move? ______________________'),
     ('lines', 2),
     ('p', '5. How could scientists tell how old a rock is? ______________________'), ('lines', 2)],
    [('p', 'Ungraded. Likely answers: 1) about 4.5 billion years; 2) answers vary; the oldest minerals are zircons about 4.4 billion years old (Western Australia) and the oldest rock is about 4.0 billion years old (Canada); 3) the ocean floor is younger, but many students will guess it is older; 4) tectonic plates of rock that move slowly; 5) radioactive (radiometric) dating, or by its layers and fossils. Compare at the end of the unit.')]))
items.append(item(1, 'Hook data: ocean floor and continent ages', 'Hook data', 'Glue under "Hook data" in the notebook (D1-D)', 'One per student',
    [('h', 'The ocean floor'),
     tb(['Place on the ocean floor', 'Age of the rock'],
        [['Right at the Mid-Atlantic Ridge', '0 (forming now)'], ['Middle of the Atlantic, 2,000 km from the ridge', 'about 80 million years'],
         ['Atlantic floor next to eastern North America', 'about 180 million years'], ['Western Pacific, east of Japan', 'about 180 million years']], [4.5, 2.6], 0.34),
     ('p', 'Ages are rounded. Earth is about 4,500 million years old.'),
     ('h', 'The continents and life'),
     tb(['Continental material', 'Where', 'Age'],
        [['Oldest mineral (zircon)', 'Western Australia', 'about 4.4 billion years'], ['Oldest known rock', 'Canada', 'about 4.0 billion years'], ['Oldest fossils', 'Western Australia', 'about 3.5 billion years']], [3, 2.3, 2.6], 0.34),
     ('h', 'I notice: ______________________________________________'), ('lines', 2),
     ('h', 'I wonder: ______________________________________________'), ('lines', 2),
     ('note', SRC_AGES)],
    [('p', 'Notice: the youngest ocean floor is at the ridge and the oldest ocean floor is only about 180 million years old, while continental rock is billions of years old and fossils go back 3.5 billion years. Wonder: Why is the ocean floor so young? Where did the older ocean floor go? Student wording varies.')]))
items.append(item(1, 'Unit CER page', 'Unit CER', 'Glue into the notebook (U-1); add rows all unit', 'One per student',
    [('p', 'Write your first claim today. It is fine if it is wrong. Revise it every few lessons and add evidence to the log.'),
     ('h', 'First claim (Lesson 1): Why is the seafloor so much younger than the continents?'), ('lines', 2),
     tb(['Evidence (what I saw, with a number)', 'Lesson', 'Kind (map, graph, data, model, fossil)', 'What it shows'], [['', '', '', '']] * 8, [3, 0.8, 2, 2.6], 0.42),
     ('h', 'Revised claim (Lesson 8)'), ('lines', 3)],
    [('p', 'Rows fill in over the unit. Example rows: Ocean floor ages increase away from the ridge (map, Lesson 3). Oldest ocean floor about 180 million years (data, Lesson 1). Magnetic stripes are mirror images across a ridge (model, Lesson 7). GPS and Hawaii give similar motion rates (data, Lesson 7).')]))
items.append(item(1, 'World map and site list', 'Plot the pattern', 'Glue under "Plot the pattern" in the notebook (D1-A)', 'One per student',
    [('p', 'Lab A. Each partner plots 5 sites. Use a red dot for a volcano and a blue X for an earthquake. The lines are 30° apart. Do the points make lines, or are they random? Circle the one site that does not fit.'),
     ('draw', lambda w: map_drawing(w)),
     tb(['Site', 'Type', 'Latitude, longitude'],
        [['Mount St. Helens, Washington, USA', 'volcano', '46.2° N, 122.2° W'], ['Mount Fuji, Japan', 'volcano', '35.4° N, 138.7° E'], ['Popocatépetl, Mexico', 'volcano', '19.0° N, 98.6° W'],
         ['Hekla, Iceland', 'volcano', '64.0° N, 19.7° W'], ['Erta Ale, Ethiopia', 'volcano', '13.6° N, 40.7° E'], ['Tohoku, Japan (2011, magnitude 9.1)', 'earthquake', '38.3° N, 142.4° E'],
         ['Maule, Chile (2010, magnitude 8.8)', 'earthquake', '35.9° S, 72.7° W'], ['Haiti (2010, magnitude 7.0)', 'earthquake', '18.4° N, 72.5° W'], ['Turkey (2023, magnitude 7.8)', 'earthquake', '37.2° N, 37.0° E'],
         ['Kīlauea, Hawaiʻi, USA', 'volcano', '19.4° N, 155.3° W']], [4.2, 1.2, 2], 0.26),
     ('p', 'The points make ______ . They match the edges of the ______ .'),
     ('note', 'Coordinates: Smithsonian Global Volcanism Program and the USGS Earthquake Hazards Program catalogs (rounded). Continent outlines are a simplified schematic map, not for measuring distances.')],
    [('p', 'Pattern: the points make belts (lines) that match the edges of the tectonic plates. Mount St. Helens, Fuji, Popocatépetl, Tohoku and Maule lie on the Pacific "Ring of Fire"; Hekla lies on the Mid-Atlantic Ridge; Erta Ale on the East African Rift; Haiti on the Caribbean plate boundary; Turkey on the Anatolian fault boundary. Kīlauea (Hawaiʻi) is the site that does not fit: it is in the middle of the Pacific plate over a hot spot, not at a boundary.'),
     ('draw', lambda w: map_drawing(w, sites=None))]))
items.append(item(1, 'Frayer card', 'Vocabulary', 'Make one for each of the 8 vocabulary words as they come up; finish by Lesson 9', '8 per student',
    [tb(['Definition (my words)', 'Characteristics'], [['', ''], ['', ''], ['', '']], [3.5, 3.5], 0.9),
     ('p', 'WORD: ____________________________'),
     tb(['Examples', 'Non-examples'], [['', ''], ['', ''], ['', '']], [3.5, 3.5], 0.9),
     ('note', 'Words: lithosphere (plate), plate boundary, mid-ocean ridge, subduction, trench, magnetic reversal, craton, impact crater.')],
    [('p', 'Definitions: lithosphere (plate): Earth\'s rigid outer layer broken into moving plates. Plate boundary: where two plates meet. Mid-ocean ridge: where plates move apart and new ocean crust forms. Subduction: one plate sinks beneath another. Trench: deep groove where a plate sinks. Magnetic reversal: Earth\'s magnetic field flips direction; recorded in ocean-floor rock. Craton: a continent\'s ancient core. Impact crater: bowl-shaped hole made by a space rock.')]))

# ================= Lesson 2: Plate boundaries =================
items.append(item(2, 'Boundary table', 'Plate boundary models', 'Glue under "Plate boundary models" in the notebook (D1-B)', 'One per student',
    [('p', 'Model each boundary with clay (about 5 minutes each). Sketch each model in your notebook and label the arrows. Then fill in the table.'),
     tb(['Boundary', 'What the plates did', 'What formed', 'Real example'], [['Divergent', '', '', ''], ['Convergent', '', '', ''], ['Transform', '', '', '']], [1.2, 2, 2, 2], 0.8),
     ('p', 'Where is ocean crust made? ________________________   Where is it destroyed? ________________________'),
     ('h', 'Boundary sketches (label the arrows)'),
     ('box', 1.4, 'Divergent'), ('box', 1.4, 'Convergent (trench, volcanoes)'), ('box', 1.4, 'Transform'),
     ('note', 'Examples are standard textbook cases (Mid-Atlantic Ridge, Andes and Japan trenches, San Andreas Fault).')],
    [tb(['Boundary', 'What the plates did', 'What formed', 'Real example'],
        [['Divergent', 'Moved apart', 'Mid-ocean ridge; new ocean crust', 'Mid-Atlantic Ridge; East African Rift'], ['Convergent', 'Moved together; one plate slid under the other', 'Trench, volcanoes, mountains', 'Andes (Nazca under South America); Japan trench'],
         ['Transform', 'Slid past each other', 'Fault; earthquakes', 'San Andreas Fault, California']], [1.2, 2, 2, 2.4]),
     ('p', 'Ocean crust is made at a mid-ocean ridge (divergent boundary) and destroyed at a trench (convergent boundary, subduction).')]))
items.append(item(2, 'Plate boundary word wall: 8 vocabulary cards', 'Vocabulary', 'Cut apart; pairs match word, definition and picture', 'One set per pair',
    [('cards', ['lithosphere (plate) · Earth\'s rigid outer layer', 'plate boundary · where two plates meet', 'mid-ocean ridge · plates move apart; new crust', 'subduction · one plate sinks under another',
                'trench · deep groove at a sinking plate', 'magnetic reversal · the magnetic field flips', 'craton · a continent\'s ancient core', 'impact crater · hole made by a space rock'], 2, 0.9),
     ('p', 'Word on the left of each card, definition on the right. Cut on the dashed lines and shuffle. Match words to definitions, then sketch a picture for each word.')],
    [('p', 'Cards already pair each word with its definition; for the matching game, cut each card in half. Check definitions against the Frayer card key (Lesson 1).')]))

# ================= Lesson 3: Rock ages =================
items.append(item(3, 'Seafloor ages: table, color key and 13-box strip', 'Seafloor ages', 'Glue under "Seafloor ages" and "Color the seafloor" (D2-A, D2-B)', 'One per student',
    [('p', 'Lab A. Draw a row of 13 boxes: the middle box is the RIDGE, and the others are 500, 1,000 ... 3,000 km on each side. Color each box with the key.'),
     tb(['Distance from ridge (km)', 'Crust age (million years)', 'Color'],
        [['0', '0', 'red'], ['500', '20', 'orange'], ['1,000', '40', 'yellow'], ['1,500', '60', 'green'], ['2,000', '80', 'blue'], ['2,500', '100', 'purple'], ['3,000', '120', 'dark purple']], [3, 3, 2], 0.3),
     ('p', 'The strip (write the distance in each box, then color):'),
     tb(None, [[''] * 13], [1] * 13, 0.5),
     ('p', 'Where is the youngest color? The oldest? How do the left and right sides compare? As you move away from the ridge, the crust gets ______ .'),
     ('note', 'The spreading rate (2.5 cm per year, or 25 km per million years) is close to the Atlantic half-rate; see Müller et al. (2008), Science 319:1357-1362. Values are simplified.')],
    [('p', 'Left and right sides are mirror images: youngest at the ridge (red), oldest farthest away (dark purple). As you move away from the ridge, the crust gets older. Strip colors: red, orange, yellow, green, blue, purple, dark purple, purple, blue, green, yellow, orange, red (symmetric about the ridge).')]))
items.append(item(3, 'Graph grid: age versus distance', 'Graph', 'Glue under "Graph: age vs. distance" (D2-C)', 'One per student',
    [('p', 'Lab B. x-axis: distance from the ridge (0 to 3,000 km). y-axis: age (0 to 120 million years). Plot the 7 points from the table and connect them.'),
     ('draw', lambda w: graph_drawing(w, 250, 3000, 120, 500, 20, 'Distance from ridge (km)', 'Age (million years)')),
     ('p', 'Pick two points. Rate = distance ÷ time (500 km in 20 million years). Show your work: ______________________'),
     ('p', 'Rate: ______ km per million years = ______ cm per year (1 km per million years = 0.1 cm per year). About how fast do fingernails grow? ____________'),
     ('p', 'Use your line to predict the age of crust 3,500 km from the ridge: ______ million years.')],
    [('p', 'Points are (0,0), (500,20), (1000,40), (1500,60), (2000,80), (2500,100), (3000,120): a straight line. Rate = 500 km ÷ 20 million years = 25 km per million years = 2.5 cm per year. Fingernails grow about 3 to 4 cm per year (a few cm), similar to plate speed. At 3,500 km: 3,500 ÷ 25 = 140 million years.')]))
items.append(item(3, 'North America ages: table and 5-box strip', 'Color North America', 'Glue under "Color North America" (D2-D)', 'One per student',
    [('p', 'Lab C. Draw a row of 5 boxes from west to east. Write the region names in order. Oldest region: dark brown. Youngest: light yellow. Pick colors in between.'),
     tb(['Region', 'From the core', 'Age of the crust'],
        [['Pacific Coast Ranges', 'west, 2,800 km', 'about 50 million years'], ['Rocky Mountain region', 'west, 1,800 km', 'about 150 million years'], ['Canadian Shield (core)', '0', 'about 2.7 billion years'],
         ['Grenville Province', 'east, 1,200 km', 'about 1.1 billion years'], ['Appalachian Mountains', 'east, 2,000 km', 'about 400 million years']], [3, 2, 2.6], 0.3),
     tb(None, [[''] * 5], [1] * 5, 0.5),
     ('p', 'Where is the oldest crust? How does the age change as you move away from it? ______________________'),
     ('note', 'Ages simplified from the Geologic Map of North America (Reed et al. 2005, Geological Society of America DNAG), and the "ancient core" idea from Hoffman (1988), Annual Review of Earth and Planetary Sciences 16:543-603. Distances are approximate.')],
    [('p', 'West to east order: Pacific Coast Ranges (50 Ma, light yellow), Rocky Mountain region (150 Ma), Canadian Shield (2.7 Ga, dark brown), Grenville Province (1.1 Ga), Appalachians (400 Ma). The oldest crust is the Canadian Shield core. Age decreases as you move away from the core in both directions (tree-ring pattern). Note the strip order west to east is not oldest to youngest: young, medium, oldest, old, medium.')]))

# ================= Lesson 4: Clues to early Earth =================
items.append(item(4, '45 cm Earth timeline: event table and three strips', 'Earth timeline', 'Glue under "45 cm Earth timeline" (D3-B); cut and tape the strips end to end', 'One per student',
    [('p', 'Lab B. Left end: Earth forms. Right end: today. Scale: 1 cm = 100 million years. Position = (4,500 minus age in millions of years) ÷ 100. Cut the three 15-cm strips along the dashed lines and tape them end to end. Mark and label each event.'),
     tb(['Event', 'Age (million years ago)', 'Position (cm)'],
        [['Earth forms', '4,500', '0'], ['Oldest mineral (zircon)', '4,400', '1'], ['Oldest known rock', '4,000', ''], ['Oldest fossils', '3,500', ''], ['Oldest ocean floor', '200', ''], ['Today', '0', '45']], [3.6, 2.4, 1.6], 0.3),
     ('cards', ['Strip 1: 0 to 15 cm (1 cm per box)', 'Strip 2: 15 to 30 cm', 'Strip 3: 30 to 45 cm'], 1, 0.55),
     ('p', 'Questions: How much of the 45 cm is covered by ocean floor that still exists? ______   Why is the oldest Earth rock younger than Earth? ______________________   Why are there no fossils that old in the ocean floor? ______________________'),
     ('note', SRC_AGES)],
    [('p', 'Positions: oldest rock (4,500 − 4,000) ÷ 100 = 5 cm; oldest fossils 10 cm; oldest ocean floor 43 cm; today 45 cm. Only the last 2 cm of the 45 cm (200 million years) is covered by ocean floor that still exists. The oldest Earth rock is younger than Earth because early rock was melted, buried, or eroded and recycled by plate motion. There are no fossils that old in the ocean floor because the old ocean floor has been subducted and recycled.')]))
items.append(item(4, 'Early Earth evidence log', 'Evidence for early Earth', 'Glue under "Evidence list" in the notebook', 'One per student',
    [('p', 'List the evidence scientists use to learn about early Earth. Use today\'s timeline and your Lesson 4 reading (Lesson 8.2 Life\'s Early History, pp. 219-225).'),
     tb(['Evidence', 'Where it is found', 'Age', 'What it tells us'], [['', '', '', '']] * 6, [2.2, 1.8, 1.4, 2.4], 0.5),
     ('p', 'Why can\'t we use only Earth rocks to learn about the very first few hundred million years? ______________________'), ('lines', 2)],
    [('p', 'Evidence list examples: zircon crystals (Western Australia, 4.4 billion years, solid crust existed); Acasta Gneiss (Canada, 4.0 billion years, oldest known rock); stromatolites and microfossils (Western Australia, 3.5 billion years, life existed); meteorites (4.56 billion years, solar system age); moon rocks (up to about 4.4 billion years, early crust). Earth rocks alone fail because plate tectonics, melting and erosion have destroyed the earliest rock; the oldest known rock is younger than Earth.')]))

# ================= Lesson 5: Meteorites and moon rocks =================
items.append(item(5, 'Crater counts: record sheet', 'Crater counter', 'Glue under "Crater counts" in the notebook (D3-A)', 'One per student',
    [('p', 'Simulation A. Watch four time steps on the slides: 1, 2, 3, and 4 billion years. At each step count the craters on the Moon and on Earth. Record both numbers.'),
     tb(['Time step', 'Moon craters', 'Earth craters'], [['1 billion years', '', ''], ['2 billion years', '', ''], ['3 billion years', '', ''], ['4 billion years', '', '']], [3, 2.4, 2.4], 0.45),
     ('p', '1. Which surface looks older? How can you tell? ______________________'), ('lines', 2),
     ('p', '2. Earth was hit as often as the Moon. Why does Earth show so few craters? ______________________'), ('lines', 2),
     ('p', '3. A surface has a lot of craters. Is it old or young? Why? ______________________'), ('lines', 2),
     ('note', ILLUS + ' The Moon has no plate tectonics and almost no weathering, so craters stay; Earth\'s craters are erased by erosion, lava and plate motion.')],
    [('p', 'Counts depend on the simulation slides: the Moon\'s total rises at each step (craters pile up); Earth\'s stays low (lava, erosion and plate motion clear craters). 1) The Moon: more craters, so older (more time to collect them). 2) Earth\'s craters are erased by weathering, erosion, volcanoes and moving plates; the Moon has none of these. 3) A surface with many craters is old; few craters means a young or resurfaced surface.')]))
items.append(item(5, 'Half-life model: decay record', 'Half-life model', 'Quick lab (textbook p. 215); glue under "Half-life" in the notebook', 'One per pair',
    [('p', 'Model decay with 100 pennies in a shoebox. Shake the box and pour the pennies out. Remove the pennies that landed heads (they have "decayed"). Count and record the pennies left. Repeat six times. Each shake is one half-life.'),
     tb(['Shake (half-lives)', 'Pennies left (atoms not decayed)', 'Predicted (halve each time)'], [['0', '100', '100'], ['1', '', '50'], ['2', '', '25'], ['3', '', ''], ['4', '', ''], ['5', '', ''], ['6', '', '']], [2.2, 3, 2.6], 0.32),
     ('draw', lambda w: graph_drawing(w, 190, 6, 100, 1, 20, 'Shakes (half-lives)', 'Pennies left')),
     ('p', 'If a half-life is 700 million years, how old is a rock that has 25% of its original parent atoms left? ______________________'),
     ('p', 'Why do scientists date meteorites and moon rocks, not Earth\'s earliest rocks, to find the age of the solar system? ______________________'),
     ('note', 'A coin-flip model of radioactive decay (a standard classroom model). Uranium-lead dating of meteorites gives about 4.57 billion years: Connelly et al. (2012), Science 338:651-655. Moon highland (ferroan anorthosite) rock about 4.36 billion years: Borg et al. (2011), Nature 477:70-72.')],
    [('p', 'Real counts vary but roughly halve each shake: about 50, 25, 12, 6, 3, 2 (predicted column: 50, 25, 12.5, 6.25, 3.1, 1.6). 25% left = two half-lives: 2 × 700 million = 1,400 million years (1.4 billion years). Meteorites and moon rocks have been hardly changed since they formed, so they keep the original record; Earth\'s earliest rocks have been recycled by plate tectonics and weathering.')]))

# ================= Lesson 6: Young ocean / old continents =================
items.append(item(6, 'Guided notes: the life of ocean crust and how continents grow', 'Guided notes', 'Glue under "Guided notes" in the notebook (D4-A)', 'One per student',
    [('h', 'The life of ocean crust'),
     ('p', 'Ocean crust is made at a ______________ and moves away about 25 km per million years.'),
     ('p', 'Travel 3,000 km: 3,000 ÷ 25 = ______ million years.'),
     ('p', 'In 200 million years it travels 200 × 25 = ______ km. Then it reaches a trench and sinks.'),
     ('p', 'No ocean floor is older than about ______ million years.'),
     ('h', 'Density and continents'),
     ('p', 'Ocean crust: about 3.0 g/cm³. Continental crust: about 2.7 g/cm³. The ______________ plate sinks (subduction).'),
     ('p', 'Each continent has an ancient core. Volcanic arcs and pieces of crust are added to its edge, like tree rings. The edge is ______________ than the core.'),
     ('note', 'Densities are typical values (oceanic crust 2.9 to 3.0 g/cm³; continental crust about 2.7 g/cm³). The cooler, older ocean plate is denser than the mantle below it, which is why it can sink.')],
    [('p', 'Ridge; 120 million years; 5,000 km; 200 million years (about 180 to 200); ocean (denser) plate sinks; the edge is younger than the core.')]))
items.append(item(6, 'Density lab table', 'Sink or float', 'Glue under "Density lab table" in the notebook (D4-B)', 'One per student',
    [('p', 'Lab. Predict: which block sinks, and which floats? Measure the mass of each block and l × w × h for the volume. Density = mass ÷ volume. Water is 1.0 g/cm³.'),
     tb(['Block', 'Mass (g)', 'Volume (cm³)', 'Density (g/cm³)', 'Sinks or floats?'], [['Wood (continent)', '', '', '', ''], ['Clay (old, cold ocean plate)', '', '', '', '']], [2.6, 1.1, 1.3, 1.4, 1.5], 0.5),
     ('p', 'Which block is like the ocean plate? ______  What does the denser block do when they meet? ______________  What stands in for the mantle? ______________'),
     ('h', 'Draw what you saw'), ('box', 1.8, 'Push the blocks toward each other on water. Sketch the side view.')],
    [('p', 'Values depend on the blocks. Expected: wood density less than 1.0 (floats, like continental crust); clay density greater than 1.0 (sinks, like old dense ocean crust). The clay (ocean-plate) block dives under the wood (continent) block when pushed together; the water stands in for the mantle.')]))
items.append(item(6, 'SketchNotes checklist', 'SketchNotes', 'Glue above your half page of notes (D4-C)', 'One per student',
    [('p', 'Half page of notes: the life of ocean crust and how continents grow. One page of sensemaking: a cross-section. Check each part you drew.'),
     tb(['Part of the cross-section', 'Done?'], [['Ridge (new crust)', ''], ['Plate moving away from the ridge', ''], ['Trench', ''], ['Volcanic arc', ''], ['Continent with an ancient core and a younger edge', ''],
                                                ['Density labels (3.0 and 2.7 g/cm³)', ''], ['Arrow for plankton-shell carbon riding the plate down', '']], [6, 1.4], 0.32),
     ('p', 'Turn in a photo on Canvas: Lesson 6: SketchNotes.')],
    [('p', 'Check that the sketch includes every listed part and that the denser ocean plate is under the continental plate at the trench.')]))

# ================= Lesson 7: Evidence for moving crust (2 days) =================
items.append(item(7, 'Magnetic stripes: band table and paper strips', 'Magnetic stripes', 'Day 1. Glue under "Magnetic stripes" (D5-A); cut and fold the strips', 'One per pair',
    [('p', 'Lab A (2 cm = 1 million years). Color the two strips with the table. Start at the end you push first (the oldest crust). Cut a slit in a folded sheet of paper (the ridge). Put the strips back to back, push them up through the slit and pull them apart. Tape the result in your notebook. Label the youngest and oldest crust.'),
     tb(['Band', 'Color', 'Length', 'Age it represents'],
        [['1', 'Reversed (blue)', '3.4 cm', 'about 3.6 to 5.3 million years'], ['2', 'Normal (red)', '2.0 cm', 'about 2.6 to 3.6 million years'], ['3', 'Reversed (blue)', '3.6 cm', 'about 0.8 to 2.6 million years'], ['4', 'Normal (red)', '1.6 cm', '0 to 0.8 million years (youngest)']], [0.8, 2, 1.2, 3.6], 0.3),
     ('cards', ['Strip A (cut out; color bands 1 to 4, 10.6 cm total)', 'Strip B (cut out; color the same bands)'], 1, 0.5),
     ('p', 'What does a pair of mirror-image stripe patterns tell you about how the crust formed? ______________________'),
     ('note', 'Polarity timescale (Gilbert reversed, Gauss normal, Matuyama reversed, Brunhes normal): Gradstein et al. (2012), The Geologic Time Scale 2012; first recognized in ocean-floor data by Vine and Matthews (1963), Nature 199:947-949. Band lengths use 2 cm = 1 million years and are rounded.')],
    [('p', 'The two sides are mirror images: new crust forms at the ridge, records the field direction, and splits so each half moves away. This is evidence for seafloor spreading in the past (each band is an age). Strip colors: 1 blue, 2 red, 3 blue, 4 red from the outside in, mirrored on the other side.')]))
items.append(item(7, 'Hawaii and GPS: measured motion', 'Hawaii and GPS', 'Day 1. Glue under "Hawaii and GPS" (D5-B)', 'One per student',
    [('p', 'Lab B. Rate = distance ÷ time. 1 km per million years = 0.1 cm per year. Find the rate for Kauai and for Midway. GPS stations show about 7 to 8 cm per year. What do you notice?'),
     tb(['Island', 'Distance from Kīlauea (km)', 'Age (million years)', 'Rate (cm per year)'], [['Kīlauea', '0', '0', '(starting point)'], ['Kauaʻi', 'about 500', 'about 5', ''], ['Midway Atoll', 'about 2,500', 'about 28', '']], [2, 2.2, 1.8, 1.8], 0.45),
     ('p', 'What do you notice about the rates and about GPS? ______________________'), ('lines', 2),
     ('note', 'Island ages and distances rounded from the U.S. Geological Survey, "The Hawaiian-Emperor chain" and Clague and Dalrymple (1987), USGS Professional Paper 1350. GPS motion of the Pacific plate about 7 to 8 cm per year (NASA/JPL and UNAVCO GPS velocity solutions; rounded).')],
    [('p', 'Kauaʻi: 500 km ÷ 5 million years = 100 km per million years = 10 cm per year. Midway: 2,500 ÷ 28 = about 89 km per million years = about 9 cm per year. The rates (9 to 10 cm per year) are close to GPS (7 to 8 cm per year): independent methods (rock ages and satellites) agree that the Pacific plate moves several cm per year, so past and present motion are similar.')]))
items.append(item(7, 'Pangaea puzzle: continent cutouts and fossil table', 'Pangaea puzzle', 'Day 2. Cut out the continents; glue the fossil table under "Pangaea puzzle" (D5-C)', 'One per pair',
    [('p', 'Lab C. Cut out the dashed continents. Fit them together like a puzzle and tape the best fit in your notebook. Mark where each fossil lived.'),
     ('draw', lambda w: puzzle_drawing(w)),
     tb(['Fossil', 'What it was', 'Found in'],
        [['Mesosaurus', 'freshwater reptile', 'South America and southern Africa'], ['Glossopteris', 'seed fern (heavy seeds)', 'South America, Africa, India, Australia, Antarctica'], ['Lystrosaurus', 'land animal', 'Africa, India, Antarctica']], [1.6, 2.2, 3.8], 0.34),
     ('p', 'Mesosaurus lived in fresh water and Glossopteris had heavy seeds. Why does that matter? ______________________   What can fossils NOT tell you that GPS can? ______________________'),
     ('note', 'Continent outlines are simplified schematic shapes and are not to scale. Fossil distributions: classic evidence summarized in Wegener (1915/1929) and in standard textbooks.')],
    [('p', 'Best fit: South America nests into Africa; India, Antarctica and Australia sit near southern Africa. Mesosaurus could not swim across an ocean (fresh water) and heavy Glossopteris seeds could not blow across an ocean, so the continents must have been joined. Fossils show past positions but not current motion; GPS measures present-day motion.')]))
items.append(item(7, 'Evaluate the evidence table', 'Evaluate the evidence', 'Day 2. Glue under "Evaluate the evidence" (D5-D)', 'One per student',
    [('p', 'Rate each line of evidence for how strongly it supports moving crust (1 = weak, 4 = very strong).'),
     tb(['Line of evidence', 'Measured?', 'Past or present?', 'Independent?', 'Strength (1 to 4)'],
        [['Rock ages across a ridge', '', '', '', ''], ['Magnetic stripes', '', '', '', ''], ['GPS and Hawaii', '', '', '', ''], ['Fossils and rocks', '', '', '', '']], [2.6, 1.2, 1.4, 1.3, 1.3], 0.5),
     ('p', 'Which is strongest for current motion? ______  For past motion? ______  Why does agreement of two independent methods help? ______________________'), ('lines', 2)],
    [tb(['Evidence', 'Measured?', 'Past or present?', 'Independent?', 'Strength'],
        [['Rock ages across a ridge', 'Yes (radiometric ages)', 'Past', 'Yes', '4'], ['Magnetic stripes', 'Yes (magnetometers)', 'Past', 'Yes', '4'], ['GPS and Hawaii', 'Yes (GPS and rock ages)', 'Present (and past with Hawaii)', 'Yes', '4'], ['Fossils and rocks', 'Partly (fossil location)', 'Past', 'Yes', '3']], [2.2, 1.6, 1.8, 1.1, 1]),
     ('p', 'Strongest for current motion: GPS. For past motion: rock ages and magnetic stripes (measured, mirror-image, repeatable). Two independent methods that agree are very unlikely to both be wrong. Accept reasoned ratings of 3 or 4 with justification.')]))

# ================= Lesson 8: Evaluate the theory (2 days) =================
items.append(item(8, 'Three buckets: sort your evidence', 'Sort your evidence', 'Day 1. Glue under "Sort your evidence" (D6-E)', 'One per student',
    [('p', 'Put each row of your Unit CER log in a bucket. Then look back at your Lesson 1 claim: what would you change now?'),
     tb(['The seafloor is young because...', 'The continents are old because...', 'The early record is missing because...'], [['', '', '']], [1, 1, 1], 2.4),
     ('p', 'What I would change in my Lesson 1 claim: ______________________'), ('lines', 2)],
    [('p', 'Seafloor young: it forms at ridges and is subducted at trenches within about 200 million years (ages increase from the ridge; density). Continents old: continental crust is less dense and does not subduct; continents grow outward from ancient cores. Early record missing: plate recycling, melting and erosion destroyed the earliest rocks; only meteorites and moon rocks keep that record.')]))
items.append(item(8, 'Part A sentence frames and data bank', 'Part A: argument', 'Day 1. Glue under "Part A: argument" (D6-A)', 'One per student',
    [('p', 'Claim: Plate tectonics explains the ages (very well / partly / poorly) because ______________________.'),
     ('p', 'Ocean evidence: The seafloor is youngest at the ______ and gets older with ______ ; the oldest ocean floor is about ______ million years old.'),
     ('p', 'Continent evidence: Continental crust as old as ______ exists. In North America the crust gets ______ toward the edges.'),
     ('p', 'Reasoning: Because ocean plates are ______ than continental crust, they ______ at subduction zones, while continents ______ .'),
     ('p', 'Limit: One thing this evidence cannot show is ______ . OR: Someone might say ______ . That does not fit the evidence because ______ .'),
     ('h', 'Data you may use'),
     ('p', 'Crust age: 0 to 120 million years across 3,000 km (2.5 cm per year). Oldest ocean floor: about 200 million years. Oldest continental mineral: about 4.4 billion years. North America: 2.7 billion years at the core, 400 million years in the Appalachians. Ocean crust 3.0 g/cm³. Continental crust 2.7 g/cm³. GPS 2 cm per year (spreading rate) and rock ages 2.5 cm per year. Oldest fossils 3.5 billion years, in continental rock.'),
     ('note', 'Values are the unit data from Lessons 1 to 7 (see sources on those sheets).')],
    [('p', 'Sample: Claim: Plate tectonics explains the ages very well because ocean crust is young where it forms and recycled at trenches, and continents survive. Ocean evidence: The seafloor is youngest at the ridge and gets older with distance; the oldest ocean floor is about 200 million years old. Continent evidence: Continental crust as old as 4.4 billion years exists. In North America the crust gets younger toward the edges. Reasoning: Because ocean plates are denser than continental crust, they sink at subduction zones, while continents stay at the surface. Limit: this evidence cannot show how the earliest crust formed (before 4 billion years); or: someone might say ocean floor is young because Earth was smaller then; the 4.4 billion-year zircons and meteorites do not fit that.')]))
items.append(item(8, 'Star and step peer feedback', 'Peer feedback', 'Day 1. Glue under "Peer feedback" (D6-D)', 'One per student',
    [('p', 'Trade papers. Check the four questions, then write one star and one step.'),
     tb(['Check', 'Yes / not yet'], [['Does the claim say how well and give a cause?', ''], ['Is the evidence specific, from ocean and continents?', ''], ['Does the reasoning say why the evidence supports the claim?', ''], ['Is a limit or counterclaim addressed?', '']], [5.6, 1.8], 0.38),
     ('p', 'Star (something strong): ______________________'), ('lines', 2), ('p', 'Step (something to add or fix): ______________________'), ('lines', 2)],
    [('p', 'Student feedback varies. Look for specific stars (a number used, a clear reason) and one concrete step (add a number; explain why density matters; add a limit).')]))
items.append(item(8, 'Earth\'s story: evidence cards and frames', 'Part B: Earth\'s story', 'Day 2. Cut out the cards; glue under "Part B" (D6-B, D6-C)', 'One per student',
    [('p', 'Cut out the six evidence cards. Put them in order from oldest to newest on a paper strip and glue them down. Then write the story with the frames.'),
     ('cards', ['Meteorites: 4.56 billion years · The solar system formed.', 'Moon highlands: up to 4.4 billion years · Solid crust existed early.', 'Earth\'s oldest zircons: 4.4 billion years · Solid crust on Earth by then.',
                'Oldest Earth rock: 4.0 billion years · Rock survives in the continents.', 'Oldest fossils: 3.5 billion years · Life existed by then.', 'Oldest ocean floor: 200 million years · Ocean crust is recycled.'], 2, 0.85),
     ('p', 'Story frames: About ___ billion years ago, ___ happened. The evidence is ___ .'), ('lines', 4),
     ('p', 'Why is Earth\'s earliest record missing? ______________________'), ('lines', 2),
     ('note', 'Sources: Connelly et al. (2012), Science 338:651-655 (meteorites, 4.567 billion years); Borg et al. (2011), Nature 477:70-72 (moon highlands); Wilde et al. (2001), Nature 409:175-178 (zircons); Bowring and Williams (1999) (oldest rock); Allwood et al. (2006), Nature 441:714-718 (fossils); Müller et al. (2008), Science 319:1357-1362 (ocean floor). Ages rounded.')],
    [('p', 'Order oldest to newest: meteorites 4.56 Ga; moon highlands 4.4 Ga and Earth zircons 4.4 Ga (tie); oldest Earth rock 4.0 Ga; oldest fossils 3.5 Ga; oldest ocean floor 0.2 Ga. Story sample: About 4.56 billion years ago the solar system formed (meteorites). About 4.4 billion years ago solid crust existed (zircons, moon highlands). By 4.0 billion years rock survived in continents, and by 3.5 billion years life existed. Earth\'s earliest record is missing because plate recycling, melting and erosion destroyed it; the ocean floor is recycled in under 200 million years.')]))

# ================= Lesson 9: Review =================
items.append(item(9, 'Self-rating chart and work plan', 'Review day', 'Glue under "Self-rating chart" in the notebook (D7-A)', 'One per student',
    [('p', 'Rate yourself 1 to 4 (1 = I need help, 4 = I could teach it). Then list what you will do today: unfinished CFA, review, or enrichment.'),
     tb(['Target', 'Rating (1 to 4)', 'CFA score'],
        [['ESS1-5.1  Plates, boundaries, and crust', '', ''], ['ESS1-5.2  Reading rock ages', '', ''], ['ESS1-5.3  Why ocean crust is young and continents are old', '', ''], ['ESS1-5.4  Evidence for moving crust', '', ''],
         ['ESS1-5.5  How well plate tectonics explains rock ages', '', ''], ['ESS1-6.1  Evidence for early Earth', '', ''], ['ESS1-6.2  Why meteorites and moon rocks give the age', '', ''], ['ESS1-6.3  Telling the story of Earth\'s formation', '', '']], [4.6, 1.4, 1.2], 0.34),
     ('h', 'My work plan for today'), ('lines', 4)],
    [('p', 'Student responses vary. Look for honest ratings, completed CFAs, and a specific plan that starts with the lowest target. ESS1-6 targets support ESS1-5.3 and 5.5 and are not on the CSA.')]))
items.append(item(9, 'Review stations: five station cards', 'Review stations', 'Cut apart; early finishers rotate through the stations', 'One set per station table',
    [('p', 'Station tasks, one for each priority target. Do the task in your notebook, then check with the answer card at the station.'),
     ('cards', ['Station 1 · ESS1-5.1: Sketch a ridge, a trench and a transform fault. Label where ocean crust is made and where it sinks.',
                'Station 2 · ESS1-5.2: Crust at 1,500 km from a ridge is 60 million years old; at 2,500 km it is 100 million. Describe the pattern and the rate in cm per year.',
                'Station 3 · ESS1-5.3: Explain in two sentences why ocean floor is under 200 million years old but continents hold 4 billion-year-old rock.',
                'Station 4 · ESS1-5.4: Rank magnetic stripes, GPS, and fossils for how strongly they show crust moves. Give one reason for the top rank.',
                'Station 5 · ESS1-5.5: Write a claim that plate tectonics explains rock ages, with two numbers as evidence and one limit.'], 1, 1.0),
     ('note', 'Data are from the unit; no new sources.')],
    [('p', 'Station 1: ridge = divergent (new crust); trench = convergent (subduction); transform = sliding, earthquakes. Station 2: ages increase away from the ridge; (2,500 − 1,500) km ÷ (100 − 60) million years = 25 km per million years = 2.5 cm per year. Station 3: Ocean crust is made at ridges and sinks at trenches within about 200 million years; continental crust is less dense, does not sink, and keeps ancient cores. Station 4: GPS strongest for current motion; stripes and ages strongest for past motion. Station 5: see the Lesson 8 Part A key.')]))

# ---------- Lessons ----------
L = []


def lesson(n, title, focus, tl, objective, agenda, moves, misc, check, diff, nb, warmup, exit_, days, materials=None, key_nb=None):
    L.append(dict(n=n, title=title, focus=focus, target_labels=([T[k] for k in tl] or ['Launch day: preview all unit targets (ESS1-5.1 to ESS1-5.5)']), objective=objective, agenda=agenda, moves=moves, misc=misc,
                  check=check, diff=diff, nb=nb, warmup=warmup, exit=exit_, days=days, materials=materials or [], key_nb=key_nb, tl=tl))


def p2(focus, reading, vocab, warm, ex):
    return dict(focus=focus,
                left=[('Reading: ' + reading, 'Biology: The Living Earth. Annotate: underline new terms, star the main idea.', 1.3, 'lines'),
                      ('Vocabulary', 'Word | my definition | example (' + vocab + ')', 3.0, 'box')],
                right=[('Main idea in my words', '', 1.4, 'lines'), ('Question I still have', '', 1.0, 'lines'),
                       ('Connect it', 'Sketch one idea from the reading that helps explain why the ocean floor is young.', 1.8, 'box')],
                warmup=('Warm-up', warm), exit=('Exit ticket', ex))


lesson(1, 'Where Did the Old Ocean Floor Go?', 'Why is the seafloor so much younger than the continents?', [],
       'Students meet the anchoring phenomenon (a young ocean floor and old continents), write a first claim, plot earthquake and volcano sites to find a pattern, and preview the unit targets.',
       [('5', 'Pre-assessment', 'Ungraded pre-check'), ('8', 'Hook', 'Ocean floor and continent age data; notice and wonder'), ('2', 'First claim', 'Why is the seafloor so much younger?'),
        ('13', 'Lab A', 'Plot earthquakes and volcanoes on the world map'), ('10', 'Preview', 'Read the unit targets; star the hardest'), ('7', 'Wrap-up', 'Exit ticket and Frayer card homework')],
       ['Keep the pre-check ungraded; compare at the end of the unit.', 'Do not correct first claims; students revise them in Lesson 8.', 'Circle the one site that does not fit (Kīlauea) and save that question for Lesson 7.'],
       ['"The ocean floor is as old as the continents."', '"Volcanoes and earthquakes happen at random."'], 'No CFA today; the first CFA is Lesson 2.', 'Reteach: plot only the first 5 sites. Extend: add three more sites from the Smithsonian volcano list.',
       dict(left=[('Pre-check', 'Glue in: Pre-check (not graded)', 1.8, 'glue'), ('Hook data', 'Glue in: Hook data (D1-D). Then write I notice and I wonder.', 2.3, 'glue'), ('Vocabulary', 'Frayer cards: lithosphere (plate), plate boundary, mid-ocean ridge, subduction, trench', 1.5, 'box')],
            right=[('Unit CER page', 'Glue in: Unit CER page (U-1). Write your first claim.', 1.8, 'glue'), ('Plot the pattern', 'Glue in: World map and site list (D1-A). Write the pattern sentence.', 3.4, 'glue')]),
       ('Warm-up', 'Which is older, the ocean floor or the continents? Write a guess and a reason.'), ('Exit ticket', 'What pattern do the dots on your map make?'), [1],
       materials=['Colored pencils (red and blue)', 'Map of earthquakes and volcanoes (printable)'])
lesson(2, 'Three Ways Plates Meet', 'What happens where plates meet, and where is ocean crust made and destroyed?', ['5.1'],
       'Students model divergent, convergent and transform boundaries with clay, record what formed at each, and say where ocean crust is made and where it sinks.',
       [('3', 'Warm-up', 'Recall the map pattern'), ('10', 'Reading notes', 'Lesson 8.1 first chunk (pp. 206-218)'), ('19', 'Lab B', 'Clay plate models and boundary table'), ('5', 'Wrap-up', 'Exit ticket'), ('8', 'CFA', 'CFA ESS1-5.1 in Canvas')],
       ['Have groups rotate the three clay models on a timer.', 'Tie each boundary back to a site from yesterday\'s map.', 'Take CFA ESS1-5.1 at the end of class.'],
       ['"Plates only move apart."', '"Transform boundaries make mountains."'], 'CFA ESS1-5.1 (below 3 of 4 opens a review).', 'Reteach: build one model at a time and name what formed. Extend: predict the boundary type for Himalayas, Iceland, and the San Andreas.',
       dict(left=[('Warm-up', '', 1.0, 'lines'), ('Vocabulary', 'lithosphere, plate boundary, mid-ocean ridge, subduction, trench', 2.0, 'box'), ('Plate boundary models', 'Sketch divergent, convergent, and transform with arrows.', 3.0, 'box')],
            right=[('Boundary table', 'Glue in: Boundary table (D1-B)', 3.0, 'glue'), ('Where is ocean crust made? Where is it destroyed?', '', 1.2, 'lines')],
            part2=p2('How is Earth\'s surface divided into moving plates?', 'Lesson 8.1 Earth\'s Origin (pp. 206-218), first chunk', 'plate, boundary, ridge, trench', 'Skim the headings. What do you predict?', 'One new idea about plates is ____.')),
       ('Warm-up', 'Which pattern did your map dots make? What could explain it?'), ('Exit ticket', 'Where is ocean crust made, and where does it sink back down?'), [2], materials=['Foam or cardboard plates, red, blue and tan clay'])
lesson(3, 'Reading Rock Ages', 'What patterns do the ages of ocean crust and continental crust follow?', ['5.2'],
       'Students color a seafloor age strip, graph age against distance to find a spreading rate, and color a North America age strip.',
       [('3', 'Warm-up', 'Which rock is older?'), ('12', 'Lab A', 'Color the seafloor'), ('9', 'Lab B', 'Graph age against distance'), ('10', 'Lab C', 'Color North America'), ('3', 'Wrap-up', 'Add two rows to the evidence log'), ('8', 'CFA', 'CFA ESS1-5.2 in Canvas')],
       ['Check the graph line before students compute the rate.', 'Ask: what is the unit of the rate, and is it similar to anything students know (fingernails)?'],
       ['Students plot distance on the y-axis.', 'Students think age increases toward the ridge.'], 'CFA ESS1-5.2.', 'Reteach: color the strip and read the color key aloud. Extend: use the rate to find when the Atlantic began to open.',
       dict(left=[('Warm-up', 'Which rock is older: the ridge sample or the Brazil sample? Say why.', 1.0, 'lines'), ('Seafloor ages', 'Glue in: Seafloor ages (D2-A, D2-B)', 3.2, 'glue'), ('Vocabulary', 'craton (a continent\'s ancient core)', 1.0, 'box')],
            right=[('Graph: age vs. distance', 'Glue in: Graph grid (D2-C). Plot 7 points, find the rate, predict the age at 3,500 km.', 3.0, 'glue'), ('Color North America', 'Glue in: North America ages (D2-D). Oldest dark brown, youngest light yellow.', 2.4, 'glue'), ('Unit CER evidence log', 'Add two rows: ocean pattern and continent pattern.', 0.8, 'lines')],
            part2=p2('How do rocks get dated?', 'Lesson 8.1 Earth\'s Origin (pp. 206-218), continued', 'radioactive decay, half-life, craton', 'What does it mean for a rock to have an age?', 'One new idea about dating rocks is ____.')),
       ('Warm-up', 'A ship pulls up seafloor rock at the Mid-Atlantic Ridge and another near the coast of Brazil. Which is older?'), ('Exit ticket', 'Describe the pattern in ocean crust ages in one sentence.'), [3],
       materials=['Colored pencils, graph paper, ruler'])
lesson(4, 'Clues to Early Earth', 'How do scientists learn about early Earth when the oldest ocean floor is only 200 million years old?', ['6.1'],
       'Students build a 45 cm timeline of Earth, find where the oldest evidence falls, and list the evidence scientists use for early Earth.',
       [('3', 'Warm-up', 'How could anyone know Earth is 4.5 billion years old?'), ('5', 'Hook', 'Key ideas about old rocks'), ('13', 'Lab B', '45 cm timeline of Earth'), ('15', 'Evidence list', 'List the evidence for early Earth'), ('9', 'Wrap-up', 'Exit ticket and evidence log')],
       ['Have students measure carefully; many will put 4,000 at 4 cm instead of 5 cm.', 'Ask what is missing between 4.0 and 4.5 billion years.'],
       ['"The oldest rock is the age of Earth."'], 'Evidence list and exit ticket.', 'Reteach: place only the first three events. Extend: add the Acasta Gneiss discovery date.',
       dict(left=[('Warm-up', 'How could anyone know Earth is 4.5 billion years old? Write one idea.', 1.0, 'lines'), ('Vocabulary', 'zircon, radiometric dating, impact crater', 1.2, 'box'), ('45 cm Earth timeline', 'Glue in: 45 cm Earth timeline (D3-B). Tape your 45 cm strip below.', 3.2, 'glue')],
            right=[('Evidence list', 'Glue in: Early Earth evidence log', 3.0, 'glue'), ('Unit CER evidence log', 'Add a row about zircons, rocks, or fossils.', 0.9, 'lines')],
            part2=p2('What does the record of early life tell us about early Earth?', 'Lesson 8.2 Life\'s Early History (pp. 219-225)', 'fossil, stromatolite, zircon', 'What do you already know about the earliest life?', 'One new idea about early Earth is ____.')),
       ('Warm-up', 'How could anyone know Earth is 4.5 billion years old?'), ('Exit ticket', 'List two kinds of evidence used to learn about early Earth.'), [4])
lesson(5, 'Meteorites and Moon Rocks', 'Why do meteorites and moon rocks tell Earth\'s age better than Earth rocks do?', ['6.2', '6.3'],
       'Students use a crater simulation and a half-life model to explain why meteorites and moon rocks keep Earth\'s early record, and begin to tell how Earth formed.',
       [('3', 'Warm-up', 'Why are there so few craters on Earth?'), ('15', 'Simulation A', 'Crater counter: the Moon and Earth, same sky'), ('12', 'Quick lab', 'Half-life model with pennies'), ('9', 'How Earth formed', 'Link meteorites and moon rocks to Earth\'s formation'), ('6', 'Exit ticket', 'Why use meteorites and moon rocks?')],
       ['Run the half-life model in pairs; use Lesson 8.1 p. 215 as a reference. The textbook quick lab sits in the workbook\'s day 3; it moved here where dating matters.', 'Collect class counts for the half-life table.'],
       ['"Meteorites are younger than Earth rocks."', '"Half-life means half the rock is gone after one half-life of the whole sample."'], 'Exit ticket: why meteorites and moon rocks.', 'Reteach: do two shakes together. Extend: compute the age for 12.5% remaining.',
       dict(left=[('Warm-up', 'Earth and the Moon are hit by the same space rocks. Why does Earth show so few craters? Predict.', 1.0, 'lines'), ('Crater counts', 'Glue in: Crater counts (D3-A)', 3.0, 'glue')],
            right=[('Half-life model', 'Glue in: Half-life model: decay record', 3.0, 'glue'), ('How Earth formed', 'Use meteorites, moon rocks, and Earth\'s oldest minerals to tell the story.', 1.5, 'lines'), ('Unit CER evidence log', 'Add a row about meteorites, moon rocks, or zircons.', 0.8, 'lines')],
            part2=p2('How old is the solar system?', 'Lesson 8.1 Earth\'s Origin (pp. 206-218), reread for meteorite and moon rock evidence', 'meteorite, half-life, radiometric dating', 'What is a meteorite?', 'One new idea about the age of the solar system is ____.')),
       ('Warm-up', 'The Moon and Earth are hit by the same space rocks. Why does Earth show so few craters?'), ('Exit ticket', 'Why do scientists use meteorites and moon rocks, not Earth rocks, to find the age of the solar system?'), [5], materials=['100 pennies and a shoebox per pair'])
lesson(6, 'Why the Ocean Is Young and the Continents Old', 'How is ocean crust made, grown, and recycled, and how do continents grow and survive?', ['5.3'],
       'Students use density to explain which plate sinks, explain why ocean crust is young and continents old, and sketch a cross-section of the whole story.',
       [('3', 'Warm-up', 'Where does the old ocean crust go?'), ('7', 'Guided notes', 'The life of ocean crust; density and continents'), ('17', 'Lab', 'Sink or float: the density of plates'), ('15', 'SketchNotes', 'Half page of notes and a cross-section'), ('3', 'CFA', 'CFA ESS1-5.3 in Canvas')],
       ['Collect the density data on the board and compare with 3.0 and 2.7.', 'Require density labels on the cross-section.', 'Take CFA ESS1-5.3 in the last minutes (or at the start of Lesson 7 if time runs short).'],
       ['"Continents are denser than ocean crust."', '"Continents sink and rise like ocean crust."'], 'CFA ESS1-5.3.', 'Reteach: use the three-box sketch (ridge, trench, continent). Extend: compute the rate needed to cross an ocean in 100 million years.',
       dict(left=[('Warm-up', 'Where does the old ocean crust go?', 1.0, 'lines'), ('Guided notes', 'Glue in: Guided notes (D4-A)', 2.3, 'glue'), ('Density lab table', 'Glue in: Density lab table (D4-B)', 2.0, 'glue')],
            right=[('SketchNotes: notes', 'Glue in: SketchNotes checklist (D4-C) above your half page of notes.', 2.0, 'glue'), ('Sensemaking: cross-section', 'Draw: ridge, moving plate, trench, volcanic arc, continent with a younger edge, density labels, carbon arrow.', 3.2, 'box'),
                   ('Unit CER evidence log', 'Add a row about density or continental growth.', 0.8, 'lines')],
            part2=p2('How are continents formed and why do they last?', 'Lesson 8.3 Earth and Life Evolve Together (pp. 226-235)', 'density, subduction, continental crust', 'What do you know about why continents last longer than ocean floor?', 'One new idea about continents is ____.')),
       ('Warm-up', 'You know the ocean floor is under 200 million years old. Where does the old ocean crust go?'), ('Exit ticket', 'Why is ocean crust young and why are continents old?'), [6], materials=['Wood and clay blocks, balance, water tub, ruler'])
lesson(7, 'Evidence for Moving Crust', 'How strong is the evidence that the crust has moved and is still moving?', ['5.4'],
       'Over two days, students use magnetic stripes, Hawaii and GPS, and fossils as evidence of moving crust, and rate how strong each line of evidence is.',
       [('Day 1: 2', 'Warm-up', 'How could you show that the crust moves?'), ('Day 1: 12', 'Lab A', 'Paper model of seafloor spreading'), ('Day 1: 7', 'Lab B', 'Hawaii and GPS: measured motion'), ('Day 1: 5', 'Wrap-up', 'Add evidence log rows'),
        ('Day 2: 3', 'Warm-up', 'Which lines of evidence have we used?'), ('Day 2: 9', 'Lab C', 'Pangaea puzzle and fossils'), ('Day 2: 6', 'Evaluate the evidence', 'Rate each line of evidence 1 to 4'), ('Day 2: 8', 'CFA', 'CFA ESS1-5.4 in Canvas')],
       ['Day 1 ends with the Hawaii data so students carry the rate question into Day 2.', 'Day 2: collect the Pangaea fit before students write the evidence ratings.'],
       ['"Fossils prove the crust is moving today."', '"Magnetic stripes show the plates stopped moving."'], 'CFA ESS1-5.4.', 'Reteach: compare only stripes and GPS. Extend: add the polarity timescale and compute a spreading rate from stripe widths.',
       dict(left=[('Warm-up', 'How could you show the seafloor moved long ago? How could you show it is moving today?', 1.0, 'lines'), ('Vocabulary', 'magnetic reversal', 1.0, 'box'), ('Magnetic stripes', 'Glue in: Magnetic stripes (D5-A). Tape your paper stripes below it. Label youngest and oldest.', 2.6, 'glue'), ('Hawaii and GPS', 'Glue in: Hawaii and GPS (D5-B). Fill in both rates.', 1.8, 'glue')],
            right=[('Pangaea puzzle', 'Glue in: Pangaea puzzle (D5-C). Tape your best fit above it.', 2.8, 'glue'), ('Evaluate the evidence', 'Glue in: Evaluate the evidence (D5-D), strength 1 to 4.', 2.4, 'glue')],
            part2=p2('What evidence did scientists use to propose that continents move?', 'Lesson 8.3 Earth and Life Evolve Together (pp. 226-235), second read; Analyzing Data, Extinction Through Time (p. 231)', 'magnetic reversal, fossil evidence, spreading', 'What is your best evidence so far that crust moves?', 'One new idea about the evidence is ____.')),
       ('Warm-up', 'How could you show that the crust moves?'), ('Exit ticket', 'Which line of evidence is strongest for past motion? For current motion? Why?'), [7, 8], materials=['Scissors, red and blue pencils, ruler, tape, folded paper'])
lesson(8, 'Evaluate the Theory, Tell Earth\'s Story', 'How well does plate tectonics explain the ages of crustal rocks, and what story do ancient materials tell about Earth\'s formation?', ['5.5', '6.3'],
       'Over two days, students sort their evidence, write a claim-evidence-reasoning evaluation of plate tectonics, peer-review it, and order six evidence cards to tell Earth\'s story.',
       [('Day 1: 3', 'Sort your evidence', 'Put each row of the evidence log in a bucket'), ('Day 1: 14', 'Part A', 'Write the argument with frames'), ('Day 1: 5', 'Peer feedback', 'Star and step'), ('Day 1: 23', 'Revise and submit', 'Fix one thing; submit Unit 3.2 CER (Part A)'),
        ('Day 2: 4', 'Warm-up', 'Revisit your Lesson 1 claim'), ('Day 2: 12', 'Part B', 'Order six evidence cards; Earth\'s story'), ('Day 2: 8', 'Wrap-up', 'Why is Earth\'s earliest record missing?'), ('Day 2: 8', 'CFA', 'CFA ESS1-5.5 in Canvas')],
       ['Day 1 is the argument-writing day: require a limit or counterclaim.', 'Day 2: have partners explain their card order to another pair before gluing.'],
       ['"Plate tectonics explains the oldest rocks too."', 'Claims with no numbers.'], 'CFA ESS1-5.5.', 'Reteach: give the frames only for Ocean evidence. Extend: write a second counterclaim.',
       dict(left=[('Sort your evidence', 'Glue in: Three buckets (D6-E). Sort the rows of your U-1 log.', 2.0, 'glue'), ('Part A: argument', 'Glue in: Part A sentence frames and data bank (D6-A). Write your claim, evidence, reasoning, and limit beside them.', 3.2, 'glue'), ('Peer feedback', 'Glue in: Star and step (D6-D).', 1.6, 'glue')],
            right=[('Part B: Earth\'s story', 'Glue in: Evidence cards (D6-B) in order, oldest to newest. Then write the story with the frames (D6-C).', 4.0, 'glue'), ('Unit CER evidence log', 'Mark every row you used today (U-1). Revise your Lesson 1 claim.', 1.4, 'lines')]),
       ('Warm-up', 'Look back at your Lesson 1 claim. What would you change now?'), ('Exit ticket', 'Why is Earth\'s earliest record missing?'), [9, 10], materials=['Scissors, glue, evidence log'])
lesson(9, 'Review Day', 'Which targets do I still need to work on before the CSA?', ['5.1', '5.2', '5.3', '5.4', '5.5'],
       'Students rate themselves on each target, work on the Canvas reviews or review stations their scores call for, and preview the CSA.',
       [('5', 'Rate yourself', '1 to 4 on each target'), ('33', 'Work time', 'Reviews, review stations, or enrichment matched to CFA scores'), ('5', 'Vocabulary self-check', 'Explain the 8 words to a partner'), ('2', 'CSA preview', 'What to study')],
       ['Pull small groups by lowest target; have early finishers use the review stations.', 'Remind students the ESS1-6 targets are not on the CSA.'],
       ['Students skip reviews because they feel confident.'], 'Self-rating chart and review work.', 'Reteach: group on ESS1-5.4 and 5.5. Extend: enrichment choice board.',
       dict(left=[('Self-rating chart', 'Glue in: Self-rating chart and work plan (D7-A)', 3.8, 'glue'), ('Work plan', 'List what you will do today.', 1.4, 'lines')],
            right=[('Review stations', 'Notes from any review station you used.', 3.0, 'lines'), ('Vocabulary check', 'Explain each of the 8 words to a partner without reading.', 2.0, 'lines')]),
       ('Warm-up', 'Which target do you feel least sure about? Why?'), ('Exit ticket', 'The target I will study tonight is ____.'), [11], materials=['Review stations (printable)'])
lesson(10, 'CSA', 'What do you know about the ages of Earth\'s crust?', ['5.1', '5.2', '5.3', '5.4', '5.5'],
       'Students show mastery of the five priority targets on the CSA.',
       [('2', 'Directions', 'Before you begin'), ('41', 'CSA', 'Unit 3.2 CSA in Canvas (12 questions)'), ('2', 'When you finish', 'Check Q10 and Q12; read quietly')],
       ['Clear desks; pencil only.', 'After the CSA, students fill in the notebook reflection page.'], ['Students rush the written responses.'], 'CSA scores by target.', 'Reassess below-mastery targets after reteach.',
       dict(left=[('What I learned about the ages of Earth\'s crust', 'Three things I understand better now.', 2.8, 'lines'), ('Where did the old ocean floor go?', 'Explain it with plates, density, and evidence.', 3.2, 'lines')], right=[]),
       ('Warm-up', 'Before the CSA, I feel ____ about ____.'), ('Exit ticket', 'The one idea I want to remember from this unit is ____.'), [12])

KEYNB = {
    1: ['Warm-up: students guess; the ocean floor is younger. Exit ticket: the dots make belts (lines) that match plate edges.', 'Vocabulary: see the Frayer card key.'],
    2: ['Exit ticket: ocean crust is made at a mid-ocean ridge (divergent boundary) and sinks at a trench (convergent boundary).'],
    3: ['Warm-up: the Brazil sample is older (farther from the ridge). Exit ticket: ocean crust gets older with distance from the ridge; youngest at the ridge.'],
    4: ['Warm-up: students may say radioactive dating; accept reasoned ideas. Exit ticket: zircons, oldest rock, oldest fossils, meteorites, moon rocks.'],
    5: ['Warm-up: Earth erases craters by erosion, lava, and moving plates. Exit ticket: meteorites and moon rocks have hardly changed since they formed, so they keep the early record; Earth rocks were recycled.'],
    6: ['Warm-up: it sinks at trenches (subduction) and is recycled. Exit ticket: ocean crust is young because it is made at ridges and recycled at trenches (denser plate sinks); continents are old because they are less dense and stay on the surface, growing from an ancient core.'],
    7: ['Exit ticket: strongest for past motion: rock ages across a ridge and magnetic stripes; for current motion: GPS.'],
    8: ['Warm-up: students revise; look for plates, density, and evidence in the revised claim. Exit ticket: plate recycling, melting and erosion destroyed the early record; only meteorites and moon rocks keep it.'],
    9: ['Student responses vary.'], 10: ['Reflection: look for plates, density, subduction, and evidence (ages, stripes, GPS).'],
}
for l in L:
    l['key_nb'] = [('p', t) for t in KEYNB.get(l['n'], [])]

unit = dict(id='3.2', name='Age of the Earth', std_short='HS-ESS1-5 Age of the Earth',
            std_line='Standard: HS-ESS1-5. Evaluate evidence of the past and current movements of continental and oceanic crust and the theory of plate tectonics to explain the ages of crustal rocks. Targets are labeled ESS1-5.1 to ESS1-5.5 (priority) and ESS1-6.1 to ESS1-6.3 (supporting). Pacing follows the 26-27 workbook: 12 days across 10 lessons (Lessons 7 and 8 each take two days).',
            lessons=L, items=sorted(items, key=lambda i: i['lesson']),
            caveats=['Real data (ocean-floor ages, zircon, oldest rock, fossils, meteorites, polarity timescale, Hawaii) are rounded and cited on each item. Scientists revise ranges as new evidence arrives.',
                     'Spreading rates, the age-versus-distance table (2.5 cm per year) and the North America ages are simplified for class (see item notes).',
                     'The world map and continent cut-outs are simplified schematic outlines, not accurate coastlines. Do not use them to measure distance or area.',
                     'Penny half-life results vary. Expect counts to halve on average, not exactly.',
                     'The crater-count simulation counts depend on the slide images; the key gives the expected pattern.',
                     'Q10 and Q12 on the CSA are the two written responses. They use the same claim, evidence, reasoning, and limit frames as Lesson 8.'],
            match=dict(heading='Matching table: evidence to the story it tells', intro='Use this table to check Lesson 7 and Lesson 8 answers: match each line of evidence to what it shows.',
                       table=dict(header=['Evidence', 'Kind', 'What it shows'],
                                  rows=[['Ocean-floor ages increase away from a ridge', 'Rock ages (map, graph)', 'Ocean crust is made at ridges and moves away'], ['Mirror-image magnetic stripes on both sides of a ridge', 'Magnetic data (model)', 'Seafloor spreading in the past'],
                                        ['Hawaii: island ages increase along the chain; GPS about 7 to 8 cm per year', 'Rock ages and GPS', 'The Pacific plate moves now and moved in the past'], ['Same fossils on separated continents', 'Fossils', 'Continents were once joined'],
                                        ['Oldest ocean floor is about 200 million years old', 'Rock ages', 'Ocean crust is recycled by subduction'], ['Oldest continental rock is about 4.0 billion years old; zircons 4.4', 'Rock ages', 'Continents survive; early record is partial'],
                                        ['Meteorites 4.56 billion years; moon highlands up to 4.4', 'Radiometric ages', 'Earth and the solar system formed about 4.5 billion years ago']],
                                  cols=[3.4, 1.8, 3.2])))

if __name__ == '__main__':
    import sys
    out = sys.argv[1]
    build_printables(unit, out + '/Unit3.2_Printables.pdf')
    build_notebook(unit, out + '/Unit3.2_Student_Notebook.pdf')
    build_key(unit, out + '/Unit3.2_Printables_Teacher_Key.pdf')
    print('built')
