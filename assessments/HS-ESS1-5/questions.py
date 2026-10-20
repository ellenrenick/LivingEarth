"""Question bank for Unit 3.1 Age of the Earth (HS-ESS1-5, supporting HS-ESS1-6).

Targets follow the team workbook "Renick Living Earth Standards and Learning Targets (26-27)",
Targets tab: ESS1-5.1 to 5.5 (priority, assessed on the CSA) and ESS1-6.1 to 6.3 (supporting,
taught but never assessed: no CFAs, no reviews, not on the CSA).

Item types (New Quizzes):
  choice   one correct answer           {"type","body","choices","answer": index, "feedback"}
  multi    select all that apply        {"type","body","choices","answer": [indexes], "feedback"}
  tf       true / false                 {"type","body","answer": bool, "feedback"}
  essay    teacher graded, 4 pts        {"type","body","rubric","feedback"}

Every body is HTML. CFAs are 5 auto-graded items each so the Mastery Path can open
the review automatically. The CSA has 16 items on the five priority targets, two of them essays.
"""

# Learning targets: code -> (short name, student "I can" line from the workbook)
TARGETS = {
    "ESS1-5.1": ("Plates, boundaries, and crust",
                 "I can describe Earth's outer layer as moving plates, name three kinds of plate boundaries, and describe where ocean crust is made and where it sinks back down."),
    "ESS1-5.2": ("Reading rock ages",
                 "I can read a rock-age map and describe the pattern in the ages."),
    "ESS1-5.3": ("Why ocean crust is young and continents are old",
                 "I can explain why ocean crust is young and why continents are oldest at their ancient cores."),
    "ESS1-5.4": ("Evidence for moving crust",
                 "I can judge how strong the evidence is that the crust has moved and is still moving."),
    "ESS1-5.5": ("How well plate tectonics explains rock ages",
                 "I can judge how well plate tectonics explains the ages of rocks, using evidence."),
    "ESS1-6.1": ("Evidence for early Earth",
                 "I can list the evidence scientists use to learn about early Earth."),
    "ESS1-6.2": ("Why meteorites and moon rocks give the age",
                 "I can explain why meteorites and moon rocks tell Earth's age better than Earth rocks do."),
    "ESS1-6.3": ("Telling the story of Earth's formation",
                 "I can use evidence from rocks, meteorites, and other planets to tell how Earth formed."),
}

# Full learning-target wording, tier, and DOK from the workbook (for teacher pages and keys)
TARGET_FULL = {
    "ESS1-5.1": ("Priority", 1, "Describe Earth's outer layer (lithosphere) as moving plates that carry continental or oceanic crust, name the three kinds of plate boundary, and describe how new oceanic crust forms at mid-ocean ridges and is destroyed at subduction zones."),
    "ESS1-5.2": ("Priority", 2, "Read a map or graph of rock ages and describe the pattern: oceanic crust is older farther from a ridge, and continental crust is oldest near an ancient core."),
    "ESS1-5.3": ("Priority", 2, "Explain why oceanic crust is young compared with the oldest continental rocks, and why continental crust is youngest far from its ancient core, using how each kind of crust forms, grows, and is recycled."),
    "ESS1-5.4": ("Priority", 3, "Evaluate evidence, such as rock ages, magnetic striping, and measured plate motion, for past and current movements of continental and oceanic crust."),
    "ESS1-5.5": ("Priority", 3, "Evaluate how well the theory of plate tectonics explains the ages of crustal rocks, using evidence from both oceanic and continental crust."),
    "ESS1-6.1": ("Supporting", 1, "Describe the evidence for Earth's early history: radiometric ages of meteorites, moon rocks, and Earth's oldest minerals, and the impact-crater record."),
    "ESS1-6.2": ("Supporting", 2, "Explain why the age of the solar system, about 4.6 billion years, comes mostly from meteorites and moon rocks rather than from Earth's own rocks."),
    "ESS1-6.3": ("Supporting", 3, "Apply scientific reasoning and evidence from ancient Earth materials, meteorites, and other planetary surfaces to construct an account of Earth's formation and early history."),
}

CFA_DAY = {  # where each CFA is taken (the start of the class after the lesson; Day 7 is the cushion day)
    "ESS1-5.1": 2, "ESS1-5.2": 3, "ESS1-5.3": 5, "ESS1-5.4": 6, "ESS1-5.5": 7,
}

SEAFLOOR_TABLE = ('<table border="1" cellpadding="4"><tbody><tr><th>Distance from ridge (km)</th><th>Crust age (million years)</th></tr>'
                  '<tr><td>0</td><td>0</td></tr><tr><td>500</td><td>20</td></tr><tr><td>1,000</td><td>40</td></tr><tr><td>1,500</td><td>60</td></tr></tbody></table>')
NA_TABLE = ('<table border="1" cellpadding="4"><tbody><tr><th>Region of North America</th><th>Distance from the central core (km)</th><th>Age of the crust</th></tr>'
            '<tr><td>Canadian Shield (the central core)</td><td>0</td><td>about 2.7 billion years</td></tr>'
            '<tr><td>Grenville Province (Great Lakes to Quebec)</td><td>about 1,200</td><td>about 1.1 billion years</td></tr>'
            '<tr><td>Appalachian Mountains</td><td>about 2,000</td><td>about 400 million years</td></tr></tbody></table>'
            '<p><em>Simplified from geologic maps.</em></p>')

CFAS = {
    # ------------------------------------------------------------------ ESS1-5.1
    "ESS1-5.1": [
        {"type": "choice",
         "body": "<p>Which statement best describes Earth's lithosphere (the crust and rigid upper mantle)?</p>",
         "choices": ["It is one solid shell that does not move.",
                     "It is broken into rigid plates that move slowly over the softer mantle, carrying continents and ocean floor.",
                     "It is a layer of liquid rock beneath the crust.",
                     "It includes only the continents above sea level."],
         "answer": 1,
         "feedback": "<p>The lithosphere is broken into plates. They move a few centimeters a year over the softer mantle below and carry continental crust, oceanic crust, or both.</p>"},
        {"type": "choice",
         "body": "<p>Which row correctly matches each plate boundary with the way the plates move?</p>",
         "choices": ["Divergent: plates move apart. Convergent: plates move toward each other. Transform: plates slide past each other.",
                     "Divergent: plates move toward each other. Convergent: plates move apart. Transform: plates slide past each other.",
                     "Divergent: plates slide past each other. Convergent: plates move apart. Transform: plates move toward each other.",
                     "Divergent: plates move apart. Convergent: plates slide past each other. Transform: plates move toward each other."],
         "answer": 0,
         "feedback": "<p>Diverge means to move apart, converge means to come together, and a transform boundary is where plates slide past each other, like the San Andreas Fault.</p>"},
        {"type": "multi",
         "body": "<p>Select the <strong>TWO</strong> features that form where plates move <strong>toward</strong> each other.</p>",
         "choices": ["Deep-sea trench", "Mid-ocean ridge", "Line of volcanoes on land next to a trench", "San Andreas Fault", "Rift valley"],
         "answer": [0, 2],
         "feedback": "<p>Trenches and volcanic arcs form at convergent boundaries where one plate sinks beneath another. Mid-ocean ridges and rift valleys form where plates pull apart, and the San Andreas Fault is a transform boundary.</p>"},
        {"type": "choice",
         "body": "<p>Where is new oceanic crust made?</p>",
         "choices": ["At deep-sea trenches, where plates collide",
                     "At mid-ocean ridges, where magma rises as plates move apart",
                     "At transform faults, where plates slide past each other",
                     "In the middle of continents"],
         "answer": 1,
         "feedback": "<p>When plates pull apart at a mid-ocean ridge, magma rises into the gap and hardens into new ocean crust.</p>"},
        {"type": "choice",
         "body": "<p>A deep trench runs along the coast of Chile, where the Nazca plate meets South America. What happens to the ocean crust there?</p>",
         "choices": ["It sinks beneath South America and returns to the mantle.",
                     "It is pushed up to make a new mid-ocean ridge.",
                     "It slides sideways along a fault and stays at the surface.",
                     "It turns into continental crust."],
         "answer": 0,
         "feedback": "<p>At a trench, the ocean plate sinks into the mantle. This is called subduction, and it is how ocean crust is destroyed.</p>"},
    ],
    # ------------------------------------------------------------------ ESS1-5.2
    "ESS1-5.2": [
        {"type": "choice",
         "body": "<p>Scientists measured the age of seafloor crust along a line across a mid-ocean ridge:</p>" + SEAFLOOR_TABLE + "<p>Which statement describes the pattern in the data?</p>",
         "choices": ["Crust gets older at a steady rate as distance from the ridge increases.",
                     "Crust is the same age everywhere.",
                     "Crust gets younger as distance from the ridge increases.",
                     "Crust is oldest at the ridge."],
         "answer": 0,
         "feedback": "<p>The age is 0 at the ridge and increases by 20 million years for every 500 km, a steady increase with distance.</p>"},
        {"type": "choice",
         "body": "<p>A map of the Atlantic Ocean is colored by the age of the seafloor. A band of the youngest color runs down the center of the ocean, and the oldest colors are next to the continents. What does the band of youngest crust show?</p>",
         "choices": ["Where the ocean is deepest",
                     "Where new crust is forming, at the mid-ocean ridge",
                     "Where the continents used to touch",
                     "Where ocean crust is sinking into the mantle"],
         "answer": 1,
         "feedback": "<p>The youngest crust is found where new crust forms, at the ridge. Ages then increase in both directions away from it.</p>"},
        {"type": "choice",
         "body": "<p>Using the same pattern (0 million years at the ridge, 20 million years at 500 km, and so on), about how old is crust 2,500 km from the ridge?</p>",
         "choices": ["50 million years", "100 million years", "250 million years", "500 million years"],
         "answer": 1,
         "feedback": "<p>The crust gains 20 million years every 500 km, which is 25 km per million years. 2,500 &divide; 25 = 100 million years.</p>"},
        {"type": "choice",
         "body": "<p>Geologists mapped the age of North America's continental crust:</p>" + NA_TABLE + "<p>Which statement describes the pattern?</p>",
         "choices": ["Continental crust is oldest near the central core and gets younger farther away.",
                     "Continental crust is youngest near the central core and gets older farther away.",
                     "Continental crust is the same age everywhere.",
                     "Continental crust is oldest at the Atlantic coast."],
         "answer": 0,
         "feedback": "<p>The ancient core in the Canadian Shield is about 2.7 billion years old. The crust gets younger moving outward to the Grenville Province and the Appalachians.</p>"},
        {"type": "tf",
         "body": "<p>True or false: On a map of North America's crust, the oldest rocks are found at the edges of the continent and the youngest are in the middle.</p>",
         "answer": False,
         "feedback": "<p>False. It is the other way around: the oldest rocks are in the central core and the crust gets younger toward the edges.</p>"},
    ],
    # ------------------------------------------------------------------ ESS1-5.3
    "ESS1-5.3": [
        {"type": "choice",
         "body": "<p>The oldest ocean floor is about 200 million years old, but some continental rock is about 4 billion years old. Which explanation fits best?</p>",
         "choices": ["Ocean crust is made at ridges and destroyed at subduction zones, so it is always replaced, while continental crust stays at the surface.",
                     "The ocean formed after the continents did, so all ocean rock is young.",
                     "Waves and currents wear away ocean rock faster than rain wears away continental rock.",
                     "Continental crust is made at mid-ocean ridges, and ocean crust is not."],
         "answer": 0,
         "feedback": "<p>Ocean floor is a conveyor belt: it is made at ridges and recycled at trenches within about 200 million years. Continental crust is not recycled that way, so it can last billions of years.</p>"},
        {"type": "choice",
         "body": "<p>An old ocean plate (average density about 3.0 g/cm&sup3;) collides with a continental plate (average density about 2.7 g/cm&sup3;). What happens, and why?</p>",
         "choices": ["The continental plate sinks because it is thicker.",
                     "The ocean plate sinks beneath the continent because it is denser.",
                     "Neither plate sinks because they have similar densities.",
                     "Both plates sink at the same rate."],
         "answer": 1,
         "feedback": "<p>The denser plate sinks beneath the less-dense plate. Old, cold ocean plates are denser than continental crust, so they subduct.</p>"},
        {"type": "choice",
         "body": "<p>Continental crust is rarely pulled down into the mantle. Which statement explains why some continental crust is billions of years old?</p>",
         "choices": ["Continental crust is less dense, so it is buoyant and stays at the surface instead of sinking at subduction zones.",
                     "Continental crust is never worn down by weathering and erosion.",
                     "Continental crust is made of the same material as the mantle.",
                     "Continental crust is made at the same ridges as ocean crust."],
         "answer": 0,
         "feedback": "<p>Continental crust is thick and less dense, so it floats and survives. Ocean plates are denser, so they are recycled.</p>"},
        {"type": "choice",
         "body": "<p>In North America, the continental crust is oldest in the central core and youngest near the edges. Which explanation fits best?</p>",
         "choices": ["Over time, volcanic island chains and pieces of crust were added to the edges of the continent, so the newest material is at the outside.",
                     "The edges of the continent were made first and the center formed last.",
                     "The crust at the center was recycled at subduction zones, so it is the youngest.",
                     "New crust forms at the center of the continent, like a mid-ocean ridge."],
         "answer": 0,
         "feedback": "<p>Continents grow outward, like tree rings. Volcanic arcs and pieces of crust collide with the edge and are added to it, so crust gets younger moving away from the ancient core.</p>"},
        {"type": "choice",
         "body": "<p>Which sequence describes the life of a piece of ocean crust?</p>",
         "choices": ["It is made at a ridge, moves away as part of a plate, cools and becomes denser, and sinks at a trench.",
                     "It is made at a trench, moves toward a ridge, and sinks at the ridge.",
                     "It is made at a ridge and stays in the same place for billions of years.",
                     "It is made in the middle of a continent and moves toward the coast."],
         "answer": 0,
         "feedback": "<p>New crust forms at a ridge and moves away as the plate spreads. As it ages it cools and gets denser, and at a trench it sinks back into the mantle.</p>"},
    ],
    # ------------------------------------------------------------------ ESS1-5.4
    "ESS1-5.4": [
        {"type": "choice",
         "body": "<p>Scientists have three kinds of evidence about moving crust: (A) the same fossils on separated continents, (B) mirror-image magnetic stripes on the two sides of a ridge, and (C) GPS and satellite measurements of plates moving a few centimeters a year. Which is the best evidence that plates are moving <strong>right now</strong>?</p>",
         "choices": ["A, because fossils are millions of years old", "B, because magnetic stripes were made in the past", "C, because it is a direct measurement of present motion", "None of them, because only one kind of evidence is ever strong"],
         "answer": 2,
         "feedback": "<p>GPS and satellite data measure the motion of the plates today. Fossils and magnetic stripes record past movement.</p>"},
        {"type": "choice",
         "body": "<p>A student says, &ldquo;The same fossil found on two continents proves that the continents moved apart.&rdquo; Which response is the best evaluation?</p>",
         "choices": ["The student is right; fossils are the only evidence needed.",
                     "Matching fossils show the lands were once connected, but they say little about how or when they moved. The case is stronger when rock ages, magnetic stripes, and measured motion agree.",
                     "The student is wrong; fossils say nothing about the continents.",
                     "Fossils cannot be evidence because they are too old."],
         "answer": 1,
         "feedback": "<p>Fossils are good evidence that lands were once joined, but a single line of evidence has limits. Several independent lines that agree make a much stronger case.</p>"},
        {"type": "multi",
         "body": "<p>Select the <strong>TWO</strong> observations that together show new seafloor forms at a ridge and spreads away from it.</p>",
         "choices": ["Crust gets older with distance from the ridge.", "Magnetic stripes on one side of the ridge are a mirror image of those on the other.", "Earthquakes occur in Japan.", "The deepest part of the ocean is in the Pacific.", "Whales live in every ocean."],
         "answer": [0, 1],
         "feedback": "<p>A steady increase in age away from the ridge and symmetrical magnetic stripes are the two observations that match crust forming at the ridge and moving apart in both directions.</p>"},
        {"type": "choice",
         "body": "<p>GPS stations on opposite sides of the Mid-Atlantic Ridge in Iceland are moving apart by about 2 cm per year. Rock ages and magnetic stripes give a spreading rate of about 2.5 cm per year. What does this agreement tell you?</p>",
         "choices": ["The evidence is weak because the two numbers are different.",
                     "Two independent methods give nearly the same rate, which makes the conclusion that the seafloor is spreading more trustworthy.",
                     "The GPS data must be wrong because rock ages are more accurate.",
                     "Spreading stopped millions of years ago."],
         "answer": 1,
         "feedback": "<p>When two independent methods, one measuring today and one using rocks formed over millions of years, give nearly the same rate, the evidence is stronger.</p>"},
        {"type": "choice",
         "body": "<p>Which new finding would most <strong>weaken</strong> the idea that ocean crust forms at ridges and spreads away from them?</p>",
         "choices": ["Crust at the ridge is 100 million years old and crust gets younger farther away.",
                     "Crust at the ridge is brand new and gets older farther away.",
                     "Magnetic stripes are mirror images on both sides of the ridge.",
                     "GPS stations on either side of the ridge are moving apart."],
         "answer": 0,
         "feedback": "<p>If the crust at the ridge were old and got younger moving away, it would contradict the idea that the ridge is where new crust forms. The other findings support the idea.</p>"},
    ],
    # ------------------------------------------------------------------ ESS1-5.5
    "ESS1-5.5": [
        {"type": "choice",
         "body": "<p>Which statement best completes the reasoning?</p><p><em>Plate tectonics explains why the ocean floor is under 200 million years old and continental rock can be billions of years old, because&hellip;</em></p>",
         "choices": ["ocean plates are continuously made at ridges and recycled at subduction zones, while buoyant continental crust is not.",
                     "the ocean did not exist until 200 million years ago.",
                     "ocean rock erodes faster than continental rock.",
                     "scientists have not found the older ocean rocks yet."],
         "answer": 0,
         "feedback": "<p>The theory explains both ages with one process: ocean crust is made and destroyed on a short cycle, while continental crust is too buoyant to be destroyed.</p>"},
        {"type": "multi",
         "body": "<p>Select the <strong>TWO</strong> observations about the ages of rocks that plate tectonics explains well.</p>",
         "choices": ["Ocean crust gets steadily older away from mid-ocean ridges and none is older than about 200 million years.",
                     "Some continental rock is billions of years old, much older than the ocean floor.",
                     "The ocean floor is older than the continents.",
                     "All crust on Earth is the same age."],
         "answer": [0, 1],
         "feedback": "<p>Plate tectonics explains the age pattern of the ocean floor (made at ridges, destroyed at trenches) and the much greater age of continental crust (too buoyant to sink).</p>"},
        {"type": "choice",
         "body": "<p>A student argues: &ldquo;The ocean floor is young because waves and currents wear it away, so the old rock is eroded.&rdquo; Which evidence best shows this explanation does not fit?</p>",
         "choices": ["Sediment is thickest on the oldest seafloor, so old crust is still there and is not worn away.",
                     "Waves are strongest near the coast.",
                     "The ocean has tides.",
                     "Some fish live in the deep ocean."],
         "answer": 0,
         "feedback": "<p>If old seafloor were eroded away, it would have little sediment. Instead it has the thickest sediment, and the ages follow a regular pattern away from the ridge. The old ocean floor is recycled at trenches, not worn away.</p>"},
        {"type": "choice",
         "body": "<p>When you judge how well plate tectonics explains the ages of rocks, which is the best <strong>limitation</strong> to point out?</p>",
         "choices": ["No ocean floor older than about 200 million years survives, so the theory cannot be tested against ocean rock from early in Earth's history; continental rocks supply that evidence.",
                     "Rocks do not have ages.",
                     "Plate tectonics only explains the ages of ocean rock, not continental rock.",
                     "Plate tectonics has never been supported by any measurement."],
         "answer": 0,
         "feedback": "<p>A strong evaluation notes where the evidence stops. Older ocean crust has been destroyed, so for early Earth scientists rely on continental rocks and other evidence.</p>"},
        {"type": "choice",
         "body": "<p>The oldest widely accepted fossils, about 3.5 billion years old, are found in continental rock in Western Australia. No fossils that old have been found in ocean-floor rock. How does this fit plate tectonics?</p>",
         "choices": ["Ocean floor that old has been recycled at subduction zones, so it no longer exists; the early record survives in continental rock.",
                     "Life did not exist in the oceans until 200 million years ago.",
                     "Fossils cannot form in rock made at mid-ocean ridges.",
                     "Scientists have not drilled the ocean floor yet."],
         "answer": 0,
         "feedback": "<p>The ocean floor does not last long enough to hold the first three billion years of life's history. That record is in the continents, which survive much longer.</p>"},
    ],
}

# ---------------------------------------------------------------------- CSA (16 items)
# Priority targets only (ESS1-5.1 to ESS1-5.5): supporting targets are taught and practiced but never on the CSA.
CSA = [
    # ESS1-5.1  (Q1-Q3)
    ("ESS1-5.1", {"type": "choice",
     "body": "<p>Which sequence correctly describes the path of a piece of ocean crust?</p>",
     "choices": ["It forms at a mid-ocean ridge, moves away on a plate, and sinks into the mantle at a trench.",
                 "It forms at a trench, moves across the ocean, and ends at a ridge.",
                 "It forms at a ridge and stays there for billions of years.",
                 "It forms at a transform fault and moves onto a continent."],
     "answer": 0,
     "feedback": "<p>Ocean crust is made at ridges where plates pull apart and destroyed at trenches where one plate sinks beneath another.</p>"}),
    ("ESS1-5.1", {"type": "choice",
     "body": "<p>Which pair correctly matches a plate boundary type with a real example?</p>",
     "choices": ["Divergent: the Mid-Atlantic Ridge. Convergent: the Andes and the Peru-Chile Trench. Transform: the San Andreas Fault.",
                 "Divergent: the San Andreas Fault. Convergent: the Mid-Atlantic Ridge. Transform: the Andes.",
                 "Divergent: the Andes. Convergent: the San Andreas Fault. Transform: the Mid-Atlantic Ridge.",
                 "Divergent: the Peru-Chile Trench. Convergent: the San Andreas Fault. Transform: the Mid-Atlantic Ridge."],
     "answer": 0,
     "feedback": "<p>The Mid-Atlantic Ridge is where plates move apart, the Andes and the trench are where the Nazca plate sinks beneath South America, and the San Andreas Fault is where plates slide past each other.</p>"}),
    ("ESS1-5.1", {"type": "tf",
     "body": "<p>True or false: Earth's lithosphere is broken into moving plates, and a single plate can carry both continental crust and oceanic crust.</p>",
     "answer": True,
     "feedback": "<p>True. The North American plate, for example, carries a continent and part of the Atlantic seafloor.</p>"}),
    # ESS1-5.2  (Q4-Q6)
    ("ESS1-5.2", {"type": "choice",
     "body": "<p>A research ship samples the seafloor along a line away from a mid-ocean ridge:</p><table border=\"1\" cellpadding=\"4\"><tbody><tr><th>Site</th><th>Distance from ridge (km)</th><th>Crust age (million years)</th></tr><tr><td>A</td><td>0</td><td>0</td></tr><tr><td>B</td><td>750</td><td>30</td></tr><tr><td>C</td><td>1,750</td><td>?</td></tr></tbody></table><p>If the pattern continues at the same rate, what is the age of Site C?</p>",
     "choices": ["About 35 million years", "About 70 million years", "About 130 million years", "About 175 million years"],
     "answer": 1,
     "feedback": "<p>The rate is 750 km in 30 million years, or 25 km per million years. 1,750 &divide; 25 = 70 million years.</p>"}),
    ("ESS1-5.2", {"type": "choice",
     "body": "<p>A map of seafloor ages in the Atlantic shows bands of color. Which description matches the pattern a ridge produces?</p>",
     "choices": ["The youngest band is along the ridge, and bands get older in both directions away from it, matching on the two sides.",
                 "The youngest bands are next to the continents, and the oldest is along the ridge.",
                 "The ages are scattered with no pattern.",
                 "The youngest band is on one side of the ocean and the oldest is on the other."],
     "answer": 0,
     "feedback": "<p>New crust forms at the ridge and spreads both ways, so the youngest band is at the ridge and the ages are symmetrical on the two sides.</p>"}),
    ("ESS1-5.2", {"type": "choice",
     "body": "<p>A table shows the age of North America's continental crust:</p>" + NA_TABLE + "<p>Which statement describes the pattern?</p>",
     "choices": ["The crust is oldest near the central core and gets younger toward the outer regions.",
                 "The crust is youngest near the central core and gets older toward the outer regions.",
                 "The crust is the same age everywhere.",
                 "The crust is oldest at the Appalachian Mountains."],
     "answer": 0,
     "feedback": "<p>Ages decrease from about 2.7 billion years at the core to about 400 million years at the Appalachians.</p>"}),
    # ESS1-5.3  (Q7-Q9)
    ("ESS1-5.3", {"type": "choice",
     "body": "<p>Two plates collide. Plate A is old ocean crust with an average density of about 3.0 g/cm&sup3;. Plate B is continental crust with an average density of about 2.7 g/cm&sup3;. What will happen, and why?</p>",
     "choices": ["Plate B will sink because it is thicker.",
                 "Plate A will sink beneath Plate B because it is denser.",
                 "Both plates will rise to form a mountain range because they have similar densities.",
                 "Neither plate will move, because density does not affect plates."],
     "answer": 1,
     "feedback": "<p>The denser plate sinks beneath the less-dense one. Old ocean crust is cold and dense, so it subducts.</p>"}),
    ("ESS1-5.3", {"type": "choice",
     "body": "<p>North America's continental crust is oldest in the central core and gets younger toward the edges. Which explanation fits best?</p>",
     "choices": ["Pieces of crust and volcanic arcs were added to the edges of the continent over time, so the newest material is farthest from the core.",
                 "The edges of the continent formed first and the center formed last.",
                 "The center was recycled at subduction zones, so it is the youngest part.",
                 "New crust forms at the center of the continent, like a mid-ocean ridge."],
     "answer": 0,
     "feedback": "<p>Continents grow outward as new material is added at their margins, like rings on a tree.</p>"}),
    ("ESS1-5.3", {"type": "choice",
     "body": "<p>Some continental rock is nearly 4 billion years old, but no ocean floor is older than about 200 million years. Which statement best explains why?</p>",
     "choices": ["Ocean crust is made at ridges and recycled at trenches, and continental crust is too buoyant to sink, so it stays at the surface.",
                 "Ocean crust formed later than the continents.",
                 "Continental crust is never weathered or eroded.",
                 "Ocean crust is made of the same material as the mantle."],
     "answer": 0,
     "feedback": "<p>The ocean floor is on a short recycling cycle. Less-dense continental crust resists sinking and survives.</p>"}),
    # ESS1-5.4  (Q10-Q12)
    ("ESS1-5.4", {"type": "choice",
     "body": "<p>The Hawaiian Islands form a chain as the Pacific plate moves over a fixed hot spot. Kilauea, on the Big Island, is active now. Kauai is about 500 km northwest of Kilauea, and its oldest rock is about 5 million years old. GPS stations on the Pacific plate near Hawaii measure about 7 to 8 cm per year of motion. How does the rate from the island ages compare, and what does it suggest?</p>",
     "choices": ["The island ages give about 10 cm per year, close to the GPS rate, so two independent methods agree that the plate is moving.",
                 "The island ages give about 1 cm per year, so the methods disagree and the plate is not moving.",
                 "The island ages give about 100 cm per year, which proves the GPS data are wrong.",
                 "The island ages cannot be used to find a rate."],
     "answer": 0,
     "feedback": "<p>500 km in 5 million years is 100 km per million years, or about 10 cm per year. That is close to the GPS rate, so a measurement of the present and a record of the past agree, which strengthens the evidence.</p>"}),
    ("ESS1-5.4", {"type": "multi",
     "body": "<p>Select the <strong>TWO</strong> lines of evidence that are independent of each other (they use different kinds of data) and both support seafloor spreading.</p>",
     "choices": ["Ages of seafloor rock increase with distance from the ridge.", "Mirror-image magnetic stripes on the two sides of a ridge.", "Two copies of the same age table, one in a textbook and one on a website.", "The coastline of Africa looks like a puzzle piece.", "Earthquakes occur in Japan."],
     "answer": [0, 1],
     "feedback": "<p>Rock ages come from radiometric dating, and magnetic stripes come from the magnetic field recorded in the rock. They are different kinds of data pointing to the same conclusion. Two copies of the same table are not independent.</p>"}),
    ("ESS1-5.4", {"type": "essay",
     "body": "<p>Scientists claim that the seafloor spreads away from mid-ocean ridges. Here are three lines of evidence:</p>"
             "<ol><li><strong>Rock ages:</strong> Seafloor crust is 0 million years old at the ridge and 40 million years old 1,000 km away, 80 million 2,000 km away, and 120 million 3,000 km away.</li>"
             "<li><strong>Magnetic stripes:</strong> Stripes of normal and reversed magnetism on one side of the ridge are a mirror image of the stripes on the other side.</li>"
             "<li><strong>Measured motion:</strong> GPS stations on opposite sides of the Mid-Atlantic Ridge in Iceland move apart about 2 cm per year, compared with about 2.5 cm per year from the rock ages.</li></ol>"
             "<p>Write an evaluation of this evidence. (1) State which line of evidence you think is the strongest and why. (2) Explain how the lines of evidence work together. (3) Describe one limitation of the evidence or one new finding that would weaken the claim.</p>",
     "rubric": (
         "Rubric (4 pts) - 4: Advanced. Chooses a line of evidence and justifies it with a specific reason (for example, GPS is a direct measurement of present motion, or the rock-age pattern is quantitative and checkable). Explains that the lines are independent yet agree (rock ages give 2.5 cm per year, GPS about 2 cm per year, stripes are symmetric), which strengthens the claim. Describes a valid limitation or a finding that would weaken the claim (for example, only a short record of GPS data, or crust at the ridge being old). "
         "3: Proficient. Judges the evidence with a reason and notes that the lines agree, but one of the three parts is general or missing. "
         "2: Developing. Lists or restates the evidence with little evaluation; limited or generic reasoning about strength. "
         "1: Beginning. Little evaluation, or an incorrect idea about what the evidence shows. "
         "0: blank or off-topic. "
         "Grading notes: - Look for: 'independent', 'agree', 'direct measurement', 'quantitative', 'limitation', 'would weaken'. - Common misconception: more of the same data is stronger evidence (independent lines are stronger). - Common misconception: older evidence is weaker. - Sample 4-point response: The strongest evidence is the measured GPS motion because it directly shows the plates moving apart today. The rock ages show crust gets older at a steady 2.5 cm per year, and the mirror-image stripes show crust forms at the ridge and splits both ways. These three lines of evidence use different kinds of data, yet they agree, which makes the claim much stronger. A limitation is that GPS has only been measured for a few decades, so we have to rely on rock ages and stripes to show what happened millions of years ago. If crust at the ridge were found to be old, that would weaken the claim."),
     "feedback": ""}),
    # ESS1-5.5  (Q13-Q16)
    ("ESS1-5.5", {"type": "choice",
     "body": "<p>Which statement completes the reasoning best?</p><p><em>Plate tectonics explains the ages of oceanic and continental rock because&hellip;</em></p>",
     "choices": ["ocean plates are continuously made at ridges and recycled at subduction zones, while buoyant continental crust is not.",
                 "the ocean was not on Earth until 200 million years ago.",
                 "ocean rock erodes faster than continental rock.",
                 "scientists have not found the older ocean rocks yet."],
     "answer": 0,
     "feedback": "<p>One process, new crust at ridges and destruction at trenches, accounts for the young, regular ages of the ocean floor and for the old continents.</p>"}),
    ("ESS1-5.5", {"type": "multi",
     "body": "<p>Select the <strong>TWO</strong> observations that support the theory of plate tectonics as an explanation for the ages of crustal rocks.</p>",
     "choices": ["Ocean crust ages increase steadily away from ridges and none is older than about 200 million years.",
                 "North American crust is oldest at its central core and younger toward its edges, where material was added by past plate interactions.",
                 "The ocean floor is older than the continents.",
                 "Rock ages are the same on every continent."],
     "answer": [0, 1],
     "feedback": "<p>Both patterns are explained by plate processes: crust made and destroyed on the ocean floor, and continents growing outward from an ancient core.</p>"}),
    ("ESS1-5.5", {"type": "choice",
     "body": "<p>The oldest widely accepted fossils, about 3.5 billion years old, are in continental rock in Western Australia. No ocean-floor rock is that old. Which statement best evaluates what this shows about plate tectonics?</p>",
     "choices": ["It is consistent with the theory: ocean floor that old has been recycled at subduction zones, so the early record survives only in continental rock.",
                 "It disproves the theory because ocean rock should hold fossils.",
                 "It shows life began only in Australia.",
                 "It has nothing to do with the ages of rocks."],
     "answer": 0,
     "feedback": "<p>The theory predicts that ocean floor older than about 200 million years has been destroyed, and the lack of old ocean rock matches that prediction.</p>"}),
    ("ESS1-5.5", {"type": "essay",
     "body": "<p>A student says, &ldquo;Plate tectonics is just one idea. It does not really explain why the ocean floor is so much younger than the continents.&rdquo; Evaluate how well the theory of plate tectonics explains the ages of Earth's crustal rocks, using the data below.</p>"
             "<p><strong>Data</strong></p>"
             "<table border=\"1\" cellpadding=\"4\"><tbody><tr><th>Distance from Mid-Atlantic Ridge (km)</th><th>Crust age (million years)</th></tr>"
             "<tr><td>0</td><td>0</td></tr><tr><td>1,000</td><td>40</td></tr><tr><td>2,000</td><td>80</td></tr><tr><td>3,000</td><td>120</td></tr></tbody></table>"
             "<ul><li>The oldest ocean floor on Earth is about 200 million years old.</li>"
             "<li>The oldest minerals found in continental rock are about 4.4 billion years old.</li>"
             "<li>In North America, crust is about 2.7 billion years old at the central core and about 400 million years old in the Appalachian Mountains.</li>"
             "<li>Ocean crust is denser (about 3.0 g/cm&sup3;) than continental crust (about 2.7 g/cm&sup3;), and ocean plates sink into the mantle at trenches.</li></ul>"
             "<ol><li><strong>Claim:</strong> How well does plate tectonics explain the ages of crustal rocks?</li>"
             "<li><strong>Evidence:</strong> Use at least <strong>two</strong> specific pieces of data, including at least one from oceanic crust and one from continental crust.</li>"
             "<li><strong>Reasoning:</strong> Explain how the evidence supports your claim.</li>"
             "<li><strong>Limit or counterclaim:</strong> Describe one thing the theory cannot show with this evidence, or answer the student's statement.</li></ol>",
     "rubric": (
         "Rubric (4 pts) - 4: Advanced. Accurate claim that plate tectonics explains the ages well, because the ocean floor is continually made at ridges and recycled at subduction zones while less-dense continental crust survives and grows outward. Cites at least two accurate data points including both ocean and continental crust (for example, ages increase 40 million years per 1,000 km from the ridge or the oldest ocean floor is about 200 million years, and continental minerals about 4.4 billion years or North American crust from 2.7 billion years at the core to about 400 million years at the Appalachians). Reasoning connects the evidence to the process (new crust at ridges, dense ocean plates sinking at trenches, buoyant continents staying and growing at their edges). Notes a limit or answers the student (for example, no ocean floor older than about 200 million years remains, so early Earth must be studied in continental rock). "
         "3: Proficient. Accurate claim, at least two accurate data points with both ocean and continental crust, reasoning present but missing one piece, limit or counterclaim brief or missing. "
         "2: Developing. Claim is partly correct without a cause, or data come from only one kind of crust. Reasoning is vague or restates the evidence. "
         "1: Beginning. Claim is incorrect or missing (for example, 'the ocean is young' or 'the seafloor is eroded away'). Little or no data. Major misconception. "
         "0: blank or off-topic. "
         "Grading notes: - Look for: 'made at ridges', 'sinks/subducts at trenches', 'recycled', 'continents are less dense/buoyant', 'added to the edges'. - Key data: ages increase 40 million years per 1,000 km (about 2.5 cm per year); oldest ocean floor about 200 million years; continental minerals about 4.4 billion years; North American core about 2.7 billion years. - Common misconception: ocean floor is 'eroded away' (sediment is thicker on older crust). - Common misconception: the ocean is young. - Sample 4-point response: Plate tectonics explains the ages of crustal rocks very well. The data show crust is 0 million years old at the ridge and 120 million years old 3,000 km away, so ocean crust is made at ridges and moves away, and the oldest ocean floor is only about 200 million years old because ocean plates are denser than continental crust (3.0 versus 2.7 g/cm3) and sink at trenches. In contrast, continental crust contains minerals up to 4.4 billion years old and in North America gets younger from 2.7 billion years at the core to about 400 million years in the Appalachians, which shows the continent grew outward and is too buoyant to be recycled. One limit is that no ocean floor older than about 200 million years survives, so the early history of Earth has to be studied in continental rock. The ocean is not young; its floor is just constantly replaced."),
     "feedback": ""}),
]

# ---------------------------------------------------------------------- Review (Mastery Path) assignments
# Each: study sections (title, html, check, answer) plus 3 questions the student answers in a text box.
T = 'border="1" cellpadding="6" style="border-collapse:collapse"'
REVIEWS = {
    "ESS1-5.1": {
        "use": "your Day 1 notes (plates and boundaries) and your plotted world map",
        "sections": [
            ("1. Moving plates",
             "<p>Earth's rigid outer layer, the <strong>lithosphere</strong> (the crust and the stiff top of the mantle), is broken into <strong>plates</strong>. The plates move a few centimeters a year, about as fast as fingernails grow, over the softer mantle below. A plate can carry <strong>continental crust</strong>, <strong>oceanic crust</strong>, or both.</p>",
             "<strong>Try it:</strong> What kinds of crust can a plate carry?",
             "Continental crust, oceanic crust, or both."),
            ("2. Three kinds of plate boundaries",
             f"<table {T}><tbody><tr><th>Boundary</th><th>Plates move&hellip;</th><th>Example</th><th>Landforms</th></tr>"
             "<tr><td>Divergent</td><td>apart</td><td>Mid-Atlantic Ridge</td><td>mid-ocean ridges, rift valleys</td></tr>"
             "<tr><td>Convergent</td><td>toward each other</td><td>Andes, Japan Trench</td><td>trenches, volcanic arcs, mountain ranges</td></tr>"
             "<tr><td>Transform</td><td>sliding past each other</td><td>San Andreas Fault</td><td>faults and earthquakes</td></tr></tbody></table>",
             "<strong>Try it:</strong> Which boundary type is the Mid-Atlantic Ridge?",
             "Divergent."),
            ("3. The crust conveyor belt",
             "<p>At a <strong>mid-ocean ridge</strong> the plates pull apart, magma rises, and <strong>new ocean crust</strong> forms. The crust moves away from the ridge as part of its plate. At a <strong>subduction zone</strong> the old, cold, dense ocean plate sinks into the mantle at a <strong>trench</strong>, and the crust is destroyed.</p>",
             "<strong>Try it:</strong> Where is ocean crust made, and where is it destroyed?",
             "Made at mid-ocean ridges (divergent boundaries); destroyed at subduction zones (convergent boundaries) marked by trenches."),
        ],
        "questions": [
            "Name the three kinds of plate boundaries and describe how the plates move at each.",
            "Explain where new ocean crust is made and how it forms.",
            "Explain what happens to ocean crust at a subduction zone and name the landform that marks it.",
        ],
        "answers": [
            "Divergent: plates move apart. Convergent: plates move toward each other. Transform: plates slide past each other.",
            "At mid-ocean ridges (divergent boundaries): plates pull apart, magma rises into the gap, and it hardens into new ocean crust.",
            "The old ocean plate sinks beneath another plate into the mantle and is recycled; a deep-sea trench marks the spot.",
        ],
    },
    "ESS1-5.2": {
        "use": "your Day 2 notes (Reading Rock Ages), your age-versus-distance graph, and the North America age table",
        "sections": [
            ("1. The pattern in the ocean",
             "<p>Seafloor crust is youngest at the ridge and gets older in both directions as you move away.</p>"
             f"<table {T}><tbody><tr><th>Distance from ridge (km)</th><th>Age (million years)</th></tr><tr><td>0</td><td>0</td></tr><tr><td>500</td><td>20</td></tr><tr><td>1,000</td><td>40</td></tr><tr><td>2,000</td><td>80</td></tr></tbody></table>"
             "<p><strong>Rate = distance &divide; time.</strong> 500 km &divide; 20 million years = 25 km per million years = <strong>2.5 cm per year</strong>.</p>",
             "<strong>Try it:</strong> How old is crust 3,000 km from the ridge at this rate?",
             "3,000 &divide; 25 = 120 million years."),
            ("2. Reading an age map",
             "<p>On a map of seafloor age, colors show age. Look for the band of the youngest color: that is the ridge, where new crust forms. Bands on one side of the ridge match the bands on the other side, and they get older with distance. The oldest ocean floor, found far from the ridges, is only about 200 million years old.</p>",
             "<strong>Try it:</strong> What would a ridge look like on an age map?",
             "A line of the youngest color, with bands that get older in both directions and match on the two sides."),
            ("3. The pattern on the continents",
             "<p>Continents have an ancient core. In North America it is the Canadian Shield, about 2.7 billion years old. Moving outward the crust gets younger.</p>"
             f"<table {T}><tbody><tr><th>Region</th><th>Distance from core (km)</th><th>Age</th></tr><tr><td>Canadian Shield (core)</td><td>0</td><td>about 2.7 billion years</td></tr><tr><td>Grenville Province</td><td>about 1,200</td><td>about 1.1 billion years</td></tr><tr><td>Appalachian Mountains</td><td>about 2,000</td><td>about 400 million years</td></tr></tbody></table>",
             "<strong>Try it:</strong> Where is the oldest continental crust, and how does the age change moving outward?",
             "In the central core (the Canadian Shield); the crust gets younger toward the outside."),
        ],
        "questions": [
            "Crust 2,500 km from a ridge is 100 million years old. Calculate the spreading rate in km per million years and in cm per year. How old would crust 4,000 km away be?",
            "Describe the pattern of seafloor ages on the two sides of a mid-ocean ridge.",
            "Describe the pattern of continental crust ages in North America, starting from the Canadian Shield.",
        ],
        "answers": [
            "2,500 km / 100 million years = 25 km per million years = 2.5 cm per year. 4,000 km / 25 = 160 million years.",
            "The youngest crust is at the ridge, and ages increase with distance on both sides, matching on the two sides.",
            "The crust is oldest in the central core (about 2.7 billion years) and gets younger moving outward (about 1.1 billion years, then about 400 million years in the Appalachians).",
        ],
    },
    "ESS1-5.3": {
        "use": "your Day 4 notes and SketchNotes (Why the Ocean Is Young and the Continents Old)",
        "sections": [
            ("1. The life of ocean crust",
             "<p>Ocean crust is made at a ridge, moves away as its plate spreads, and cools. Cold ocean plates are <strong>denser</strong> (the crust is about 3.0 g/cm&sup3;, and the cold rock under it adds to the weight). At a trench the old plate sinks into the mantle. The whole trip takes about 200 million years or less, which is why no ocean floor is older.</p>",
             "<strong>Try it:</strong> Why is no ocean floor older than about 200 million years?",
             "Ocean crust is recycled at subduction zones within about 200 million years."),
            ("2. Why continents stay",
             "<p>Continental crust is thicker and <strong>less dense</strong> (about 2.7 g/cm&sup3;). When an ocean plate meets a continent, the denser ocean plate sinks and the continent floats. Continental crust is rarely pulled down, so some of it can survive for billions of years.</p>",
             "<strong>Try it:</strong> An ocean plate meets a continental plate. Which one sinks?",
             "The ocean plate, because it is denser."),
            ("3. How continents grow",
             "<p>Every continent has an ancient <strong>core</strong>. Over time, volcanic arcs, island chains, and pieces of crust crash into the edge and are added to it, so the continent grows outward like rings on a tree. That is why the crust gets younger away from the core.</p>",
             "<strong>Try it:</strong> Why is the crust at the edge of a continent younger than at its core?",
             "New material was added to the edges later, so the newest crust is at the outside."),
        ],
        "questions": [
            "Explain why the ocean floor is under 200 million years old while some continental rock is billions of years old.",
            "Explain why continental crust is oldest at its core and youngest at its edges.",
            "An ocean plate meets a continental plate. Say which sinks, and use density to explain why.",
        ],
        "answers": [
            "Ocean crust is made at ridges and recycled at subduction zones, so it is replaced in about 200 million years; continental crust is less dense, so it is not recycled and can last billions of years.",
            "The continent grew outward from an ancient core as volcanic arcs and pieces of crust were added at the edges, so the newest crust is farthest from the core.",
            "The ocean plate sinks because it is denser (about 3.0 versus 2.7 g/cm3), so it goes beneath the less-dense continental plate.",
        ],
    },
    "ESS1-5.4": {
        "use": "your Day 5 notes (Evidence for Moving Crust), your paper magnetic-stripe model, and your evidence cards",
        "sections": [
            ("1. Four lines of evidence",
             f"<table {T}><tbody><tr><th>Evidence</th><th>What scientists found</th><th>What it shows</th></tr>"
             "<tr><td>Rock ages</td><td>Seafloor crust is 0 at the ridge and gets older with distance (2.5 cm per year).</td><td>Crust forms at the ridge and spreads out.</td></tr>"
             "<tr><td>Magnetic stripes</td><td>Mirror-image stripes of normal and reversed magnetism on both sides of a ridge.</td><td>Crust forms at the ridge and splits both ways.</td></tr>"
             "<tr><td>Measured motion</td><td>GPS and satellites measure plates moving a few cm per year; the Hawaiian chain gets older to the northwest.</td><td>Plates are moving now, and moved in the past at similar rates.</td></tr>"
             "<tr><td>Matching fossils and rocks</td><td>The same fossils, rock layers, and mountain belts on separated continents.</td><td>The continents were once joined.</td></tr></tbody></table>",
             "<strong>Try it:</strong> Which line of evidence directly measures motion happening today?",
             "GPS and satellite measurements."),
            ("2. What makes evidence strong?",
             "<ul><li><strong>Measured or quantitative:</strong> numbers you can check.</li><li><strong>Independent lines agree:</strong> different kinds of data lead to the same rate or conclusion.</li><li><strong>Predictions hold up:</strong> the idea correctly predicts what scientists find.</li><li><strong>Limits are named:</strong> a good evaluation says what the evidence cannot show.</li></ul>",
             "<strong>Try it:</strong> GPS says about 2 cm per year; rock ages say about 2.5 cm per year. Why does this make the evidence stronger?",
             "Two independent methods give nearly the same rate, so the conclusion is more trustworthy."),
        ],
        "questions": [
            "Which line of evidence best shows that plates are moving right now? Explain why.",
            "Name two independent lines of evidence for seafloor spreading and explain why it matters that they agree.",
            "A student says, &ldquo;Matching fossils prove the continents moved.&rdquo; Evaluate this claim in two sentences.",
        ],
        "answers": [
            "GPS and satellite measurements, because they directly measure present motion.",
            "Any two of rock ages, magnetic stripes, measured motion. They use different kinds of data, so when they agree the conclusion is much more trustworthy.",
            "Matching fossils show the lands were once connected, but they do not show how or when they moved. The case is stronger when rock ages, magnetic stripes, and measured motion agree.",
        ],
    },
    "ESS1-5.5": {
        "use": "your Day 6 draft evaluation and your Unit CER evidence log",
        "sections": [
            ("1. The parts of an evaluation",
             f"<table {T}><tbody><tr><th>Part</th><th>What it is</th><th>Example</th></tr>"
             "<tr><td>Claim</td><td>How well the theory explains the ages</td><td>Plate tectonics explains the ages of both ocean and continental rock very well.</td></tr>"
             "<tr><td>Evidence</td><td>Specific data from ocean and continental crust</td><td>Crust is 0 million years old at the ridge and 120 million years old 3,000 km away. North American crust is 2.7 billion years old at its core and about 400 million years old in the Appalachians.</td></tr>"
             "<tr><td>Reasoning</td><td>The process that links evidence to claim</td><td>Dense ocean plates sink at trenches while buoyant continents stay and grow at their edges.</td></tr>"
             "<tr><td>Limit or counterclaim</td><td>What the evidence cannot show, or another idea and why it fails</td><td>No ocean floor older than about 200 million years remains. &ldquo;The ocean floor is worn away&rdquo; fails because older crust has thicker sediment.</td></tr></tbody></table>",
             "<strong>Try it:</strong> Is &ldquo;plate tectonics explains rock ages&rdquo; a complete claim? Why or why not?",
             "No. It does not say how well or why; add the evidence and the process."),
            ("2. Your evidence menu",
             "<ul><li>Ocean crust age increases with distance from the ridge (2.5 cm per year).</li><li>Oldest ocean floor is about 200 million years.</li><li>Oldest continental minerals are about 4.4 billion years.</li><li>North American crust is oldest at the core (2.7 billion years) and younger at the edges.</li><li>Ocean crust (3.0 g/cm&sup3;) is denser than continental crust (2.7 g/cm&sup3;).</li><li>The oldest fossils (3.5 billion years) are in continental rock.</li></ul>",
             "<strong>Try it:</strong> Is &ldquo;ocean plates sink because they are denser&rdquo; evidence or reasoning?",
             "Reasoning. It explains why the data look the way they do. Evidence is a measurement or observation."),
        ],
        "questions": [
            "Rewrite this weak claim so it says how well and why: &ldquo;Plate tectonics explains rock ages.&rdquo;",
            "List two pieces of specific evidence, one from the ocean floor and one from the continents.",
            "Write one sentence of reasoning that links your evidence to your claim, and one limit of the evidence.",
        ],
        "answers": [
            "Plate tectonics explains the ages of rocks very well because the ocean floor is made at ridges and recycled at subduction zones, while buoyant continental crust survives and grows outward.",
            "Ocean: ages increase from 0 to 120 million years over 3,000 km, or the oldest ocean floor is about 200 million years. Continent: minerals up to 4.4 billion years, or North American crust from 2.7 billion years at the core to 400 million years in the Appalachians.",
            "Because ocean plates are denser, they sink at trenches and are destroyed, while less-dense continents stay at the surface. Limit: no ocean floor older than about 200 million years remains, so early Earth must be studied in continental rock.",
        ],
    },
}


# ---------------------------------------------------------------------- answer-order shuffle
# Fixed seed so Canvas and the teacher key always agree. Keeps the correct answers from
# clustering in the first positions of the choice lists.
def _shuffle_choices(items, seed):
    import random
    rng = random.Random(seed)
    for it in items:
        if it["type"] not in ("choice", "multi"):
            continue
        order = list(range(len(it["choices"])))
        rng.shuffle(order)
        it["choices"] = [it["choices"][i] for i in order]
        if it["type"] == "choice":
            it["answer"] = order.index(it["answer"])
        else:
            it["answer"] = sorted(order.index(a) for a in it["answer"])


for _i, (_code, _items) in enumerate(CFAS.items()):
    _shuffle_choices(_items, 310 + _i)
_shuffle_choices([i for _, i in CSA], 399)
