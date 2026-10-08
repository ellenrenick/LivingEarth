"""Question bank for Unit 3.1 Age of the Earth (HS-ESS1-5, supporting HS-ESS1-6).

Item types (New Quizzes):
  choice   one correct answer           {"type","body","choices","answer": index, "feedback"}
  multi    select all that apply        {"type","body","choices","answer": [indexes], "feedback"}
  tf       true / false                 {"type","body","answer": bool, "feedback"}
  essay    teacher graded, 4 pts        {"type","body","rubric","feedback"}

Every body is HTML. CFAs are 5 auto-graded items each so the Mastery Path can open
the review automatically. The CSA mirrors the Unit 1.3 CSA layout (16 items, two essays).
"""

# Learning targets: code -> (short name, full target)
TARGETS = {
    "ESS1-5.1": ("Evidence for continental drift",
                 "I can describe evidence for continental drift: matching fossils, matching rock types and mountain ranges, glacial evidence, and how the continents fit together."),
    "ESS1-5.2": ("Seafloor spreading and the age pattern",
                 "I can describe the pattern of seafloor rock ages, sediment thickness, and magnetic stripes, and explain how seafloor spreading makes new crust at mid-ocean ridges."),
    "ESS1-5.3": ("Plate boundaries and subduction",
                 "I can identify the three plate boundary types and explain why ocean crust sinks at subduction zones while less-dense continental crust survives."),
    "ESS1-6.1": ("Radiometric dating and Earth's oldest rocks",
                 "I can explain how radiometric dating uses half-life to find the age of a rock, and why Earth's oldest rocks are younger than meteorites."),
    "ESS1-5.4": ("Argue why the seafloor is young and the continents are old",
                 "I can argue from evidence why ocean-floor rock is young and continental rock is old."),
}

CFA_DAY = {  # where each CFA is taken (Day 7 is the cushion day for any that slip)
    "ESS1-5.1": 2, "ESS1-5.2": 3, "ESS1-5.3": 5, "ESS1-6.1": 6, "ESS1-5.4": 6,
}

CFAS = {
    # ------------------------------------------------------------------ ESS1-5.1
    "ESS1-5.1": [
        {"type": "choice",
         "body": "<p><em>Mesosaurus</em> was a small freshwater reptile that lived about 280 million years ago. Its fossils are found only in eastern South America and southwestern Africa, two places now separated by the salty Atlantic Ocean. Which explanation is best supported by this evidence?</p>",
         "choices": ["Mesosaurus swam across the Atlantic Ocean to lay its eggs.",
                     "South America and Africa were joined when Mesosaurus lived.",
                     "Strong winds carried Mesosaurus eggs across the ocean.",
                     "Mesosaurus fossils moved across the seafloor on ocean currents."],
         "answer": 1,
         "feedback": "<p>Mesosaurus lived in fresh water and could not cross a salt-water ocean. Finding the same fossils on both sides is best explained by the two continents being joined at the time.</p>"},
        {"type": "multi",
         "body": "<p>Select the <strong>THREE</strong> observations that are evidence the continents were once joined.</p>",
         "choices": ["Rock layers and mountain belts on the two sides of the Atlantic match in type and age.",
                     "Fossils of <em>Glossopteris</em> (a seed fern) are found on South America, Africa, India, Australia, and Antarctica.",
                     "Every continent has rivers that flow to the sea.",
                     "The edges of the continental shelves of South America and Africa fit together like puzzle pieces.",
                     "Whales are found in every ocean."],
         "answer": [0, 1, 3],
         "feedback": "<p>Matching rocks and mountain belts, matching fossils on separated continents, and the fit of the continental shelves all point to continents that were once joined. Rivers and whales are found everywhere and say nothing about the continents' past positions.</p>"},
        {"type": "tf",
         "body": "<p>True or false: When Alfred Wegener proposed continental drift in 1912, most scientists accepted it right away because he had explained the force that moves the continents.</p>",
         "answer": False,
         "feedback": "<p>False. Wegener had strong evidence that the continents were once joined, but he could not explain what force could move them, so many scientists rejected the idea for decades.</p>"},
        {"type": "choice",
         "body": "<p>Scratches left by glaciers, from the same ice age, are found in rock in southern Africa, India, Australia, South America, and Antarctica. Most of these places are warm today. Which explanation fits best?</p>",
         "choices": ["Earth was colder everywhere for one day, and ice covered every continent.",
                     "The continents were joined in one landmass near the south pole, and a connected ice sheet covered it.",
                     "Glaciers slid across the oceans from one continent to another.",
                     "Volcanoes on each continent made the ice."],
         "answer": 1,
         "feedback": "<p>When the southern continents are fitted together, the directions of the glacial scratches line up as if one ice sheet made them. The continents later moved apart to their warmer positions.</p>"},
        {"type": "choice",
         "body": "<p>Scientists fit the continents together using the edge of the continental shelf, not the coastline. Why?</p>",
         "choices": ["Coastlines are always straight, so they cannot be fitted.",
                     "The coastline changes with sea level and erosion, but the shelf edge is closer to the true edge of the continent.",
                     "Continental shelves are made of ocean crust.",
                     "The shelf edge is the part of the continent that is always the oldest."],
         "answer": 1,
         "feedback": "<p>Sea level and erosion keep changing the coastline. The edge of the continental shelf is a better marker of where the continental crust actually ends, so the fit is better.</p>"},
    ],
    # ------------------------------------------------------------------ ESS1-5.2
    "ESS1-5.2": [
        {"type": "choice",
         "body": "<p>Scientists drill into the seafloor along a line across the Mid-Atlantic Ridge. Crust at the ridge crest is brand new (0 years old). Crust 1,000 km from the ridge is 40 million years old. About how fast has the seafloor moved away from the ridge?</p>",
         "choices": ["About 0.25 cm per year", "About 2.5 cm per year", "About 25 cm per year", "About 40 cm per year"],
         "answer": 1,
         "feedback": "<p>1,000 km in 40 million years is 25 km per million years. That is 2.5 cm per year, about as fast as a fingernail grows.</p>"},
        {"type": "choice",
         "body": "<p>Ships towing magnetic sensors find stripes of rock with normal and reversed magnetism. The pattern on one side of a mid-ocean ridge is a mirror image of the pattern on the other side. What is the best explanation?</p>",
         "choices": ["Magma rises at the ridge, records Earth's magnetic field as it hardens, and then the new crust splits and moves apart in both directions.",
                     "The ocean floor on each side was made at different times and then pushed together.",
                     "Magnetic stripes form when seawater reacts with sediment.",
                     "Earth's magnetic field only reversed on one side of the ocean."],
         "answer": 0,
         "feedback": "<p>Rock that forms at the ridge records the direction of Earth's magnetic field at that time. As the new rock splits and moves away on both sides, the same sequence of reversals is carried in both directions, giving mirror-image stripes.</p>"},
        {"type": "choice",
         "body": "<p>At the same spreading rate (2.5 cm per year, or 25 km per million years), how old is seafloor crust that is 3,000 km from the ridge?</p>",
         "choices": ["About 12 million years", "About 75 million years", "About 120 million years", "About 300 million years"],
         "answer": 2,
         "feedback": "<p>3,000 km divided by 25 km per million years is 120 million years.</p>"},
        {"type": "tf",
         "body": "<p>True or false: Seafloor sediment is thickest right at the ridge crest and gets thinner farther away.</p>",
         "answer": False,
         "feedback": "<p>False. New crust at the ridge has had no time to collect sediment. Older crust farther away has had millions of years for the shells of dead plankton and fine particles to settle, so the layer gets thicker with distance.</p>"},
        {"type": "choice",
         "body": "<p>Communities of tube worms, clams, and bacteria live around hydrothermal vents along the crest of mid-ocean ridges. They are not found on older seafloor far from the ridge. What best explains this pattern?</p>",
         "choices": ["Vent animals can only live in the deepest part of the ocean.",
                     "Vents need heat from fresh magma near the surface, which only exists where crust is new; as crust moves away and cools, the vents stop.",
                     "Older seafloor is too thickly covered with sediment for any animal to live there.",
                     "Vent communities move across the seafloor to follow the sunlight."],
         "answer": 1,
         "feedback": "<p>Vent water is heated by magma near the ridge. The bacteria use chemicals from that water for energy (chemosynthesis) and feed the rest of the community. As the crust moves away from the ridge it cools, the vents shut off, and the community dies.</p>"},
    ],
    # ------------------------------------------------------------------ ESS1-5.3
    "ESS1-5.3": [
        {"type": "choice",
         "body": "<p>Along the west coast of South America, the Nazca plate (ocean) sinks beneath the South American plate (continent). A deep trench forms offshore, and a chain of volcanoes (the Andes) rises on land. What type of plate boundary is this?</p>",
         "choices": ["Divergent", "Convergent", "Transform", "Mid-ocean ridge"],
         "answer": 1,
         "feedback": "<p>Two plates moving toward each other is a convergent boundary. When one plate sinks beneath another it is called subduction, and it makes a trench and volcanoes.</p>"},
        {"type": "multi",
         "body": "<p>Select the <strong>TWO</strong> landforms that form where two plates move <strong>apart</strong>.</p>",
         "choices": ["Mid-ocean ridge", "Deep-sea trench", "Rift valley (such as in East Africa)", "Chain of volcanic islands above a subduction zone"],
         "answer": [0, 2],
         "feedback": "<p>Where plates pull apart (a divergent boundary), new crust forms in mid-ocean ridges, and on land the crust can split to form rift valleys. Trenches and volcanic island arcs form at convergent boundaries.</p>"},
        {"type": "choice",
         "body": "<p>An ocean plate (average density about 3.0 g/cm&sup3;) collides with a continental plate (average density about 2.7 g/cm&sup3;). Which statement is correct?</p>",
         "choices": ["The continental plate sinks because it is thicker.",
                     "The ocean plate sinks because it is denser.",
                     "Neither plate can sink because they have similar density.",
                     "Both plates sink at the same rate."],
         "answer": 1,
         "feedback": "<p>The denser plate sinks beneath the less-dense one. Old, cold ocean plates are denser than continental plates, so the ocean plate subducts.</p>"},
        {"type": "tf",
         "body": "<p>True or false: Most continental crust is not pulled down into the mantle at subduction zones because it is less dense and more buoyant than ocean plates.</p>",
         "answer": True,
         "feedback": "<p>True. Continental crust is thick and less dense, so it floats at the surface. This is why continental rock can survive for billions of years while ocean floor is recycled.</p>"},
        {"type": "choice",
         "body": "<p>Seafloor sediment includes calcium carbonate shells from dead plankton, which contain carbon. What happens to some of this carbon at a subduction zone?</p>",
         "choices": ["It is carried down into the mantle with the sinking plate, and some returns to the air as carbon dioxide from volcanoes.",
                     "It stays on the surface because sediment is too light to sink.",
                     "It turns into oxygen as the plate sinks.",
                     "It is destroyed, so the atoms no longer exist."],
         "answer": 0,
         "feedback": "<p>Atoms are not destroyed. Sediment and its carbon ride the sinking plate into the mantle, and some of the carbon comes back to the atmosphere as CO&#8322; when volcanoes erupt. This links plate tectonics to the carbon cycle.</p>"},
    ],
    # ------------------------------------------------------------------ ESS1-6.1
    "ESS1-6.1": [
        {"type": "choice",
         "body": "<p>A rock formed with 80 atoms of a radioactive parent isotope. After 3 half-lives, how many parent atoms remain?</p>",
         "choices": ["40", "20", "10", "0"],
         "answer": 2,
         "feedback": "<p>80 &rarr; 40 (1 half-life) &rarr; 20 (2) &rarr; 10 (3). After 3 half-lives, 1/8 of the original remains.</p>"},
        {"type": "choice",
         "body": "<p>An archaeologist finds a wooden tool believed to be about 8,000 years old. Which dating method can she use, and why?</p>",
         "choices": ["Uranium-238, because it has the longest half-life.",
                     "Carbon-14, because wood was once living and the tool is far younger than 50,000 years.",
                     "Uranium-235, because it works on all organic material.",
                     "None; wood cannot be dated by radioactive decay."],
         "answer": 1,
         "feedback": "<p>Living things take in carbon-14. After death it decays with a half-life of 5,730 years, so it works for once-living material up to about 50,000 years old. Uranium isotopes decay too slowly to date something this young.</p>"},
        {"type": "choice",
         "body": "<p>Scientists often date zircon crystals in igneous rock using uranium. Zircon takes uranium into its structure when it forms but leaves out lead. Why does this make zircon a good &ldquo;clock&rdquo;?</p>",
         "choices": ["Any lead found in the zircon must have come from the decay of uranium since the crystal formed.",
                     "Zircon is the hardest mineral, so it cannot be scratched.",
                     "Zircon always contains exactly the same amount of uranium.",
                     "Lead stops uranium from decaying."],
         "answer": 0,
         "feedback": "<p>Because the crystal started with uranium and no lead, the ratio of lead to uranium shows how much decay, and so how much time, has passed since the crystal formed.</p>"},
        {"type": "tf",
         "body": "<p>True or false: Carbon-14 dating can be used to find the age of a 3.5-billion-year-old rock fossil.</p>",
         "answer": False,
         "feedback": "<p>False. Carbon-14 has a half-life of 5,730 years, so after about 50,000 years too little is left to measure. Rocks billions of years old are dated with isotopes that decay far more slowly, such as uranium.</p>"},
        {"type": "choice",
         "body": "<p>The oldest known meteorites are about 4.56 billion years old. The oldest known Earth rocks are about 4.0 billion years old. Why are meteorites older than any rock found on Earth?</p>",
         "choices": ["Meteorites formed before the solar system.",
                     "Earth's earliest rocks were destroyed or recycled by plate tectonics and erosion, but meteorites have changed very little since they formed.",
                     "Radioactive decay is faster on Earth than in space.",
                     "Earth formed after the meteorites, so Earth is younger than they are."],
         "answer": 1,
         "feedback": "<p>Earth's active surface recycled its earliest rock. Meteorites formed with the solar system and have stayed nearly unchanged, so they preserve its age, which is also the best estimate for Earth's age.</p>"},
    ],
    # ------------------------------------------------------------------ ESS1-5.4
    "ESS1-5.4": [
        {"type": "choice",
         "body": "<p>The question is: <em>Why is the ocean floor so much younger than the continents?</em> Which claim answers the question best?</p>",
         "choices": ["The ocean floor is young.",
                     "The ocean is young.",
                     "The ocean floor is made of basalt.",
                     "The ocean floor is young because it is made at ridges and recycled at subduction zones, while less-dense continental crust is not recycled."],
         "answer": 3,
         "feedback": "<p>A strong claim answers the question completely and names the cause. The other choices restate the observation, are incorrect, or do not answer the question.</p>"},
        {"type": "multi",
         "body": "<p>Select the <strong>TWO</strong> statements that are <strong>evidence</strong> (data or observations), not reasoning.</p>",
         "choices": ["Crust 2,000 km from the Mid-Atlantic Ridge is about 80 million years old.",
                     "Because crust is made at the ridge, it must be older farther away.",
                     "The oldest minerals found in continental rock are about 4.4 billion years old.",
                     "Continents are less dense, so they do not sink."],
         "answer": [0, 2],
         "feedback": "<p>Evidence is a measurement or observation: a specific age or distance. The other two statements explain why the data look the way they do, which is reasoning.</p>"},
        {"type": "choice",
         "body": "<p>Which piece of evidence best supports the claim that new ocean crust forms at mid-ocean ridges?</p>",
         "choices": ["The ocean is very large.",
                     "Seafloor ages are 0 at the ridge crest and increase evenly in both directions, with mirror-image magnetic stripes.",
                     "Some islands are made of volcanic rock.",
                     "Fish live in all parts of the ocean."],
         "answer": 1,
         "feedback": "<p>The best evidence is a specific pattern that the claim predicts: youngest rock at the ridge, ages increasing symmetrically away from it, and matching stripes on both sides.</p>"},
        {"type": "choice",
         "body": "<p>Which sentence is the best <strong>reasoning</strong> to connect the evidence to the claim that continental rock is older than ocean-floor rock?</p>",
         "choices": ["Continental rock is found on land.",
                     "Because ocean plates are denser, they sink at subduction zones and are destroyed, but continental crust is too buoyant to sink, so it stays at the surface for billions of years.",
                     "Many scientists agree that continents are old.",
                     "The oldest rock is the most interesting to study."],
         "answer": 1,
         "feedback": "<p>Reasoning links the evidence to the claim with a scientific process. Here it is the density difference and what it does at subduction zones.</p>"},
        {"type": "choice",
         "body": "<p>A student argues: &ldquo;The ocean floor is young because waves and currents wear it away, so old rock is eroded.&rdquo; Which evidence best shows this is incorrect?</p>",
         "choices": ["Sediment is thickest on the oldest seafloor, so old crust is still there and has not been worn away.",
                     "Waves are strongest near the coast.",
                     "Some fish live deep in the ocean.",
                     "The ocean has tides."],
         "answer": 0,
         "feedback": "<p>If old seafloor were being eroded away, it would have little sediment. Instead sediment gets thicker with age, and the ages follow a regular pattern from the ridge. The old ocean floor is recycled at subduction zones, not worn away.</p>"},
    ],
}

# ---------------------------------------------------------------------- CSA (16 items)
# Tags are the learning target each item is assessed against.
CSA = [
    # ESS1-5.1
    ("ESS1-5.1", {"type": "choice",
     "body": "<p><em>Glossopteris</em> was a seed fern whose seeds were large and heavy. Fossils of <em>Glossopteris</em> that are about 270 million years old are found in South America, Africa, India, Australia, and Antarctica. Which explanation is best supported?</p>",
     "choices": ["The seeds were carried across the oceans by wind.",
                 "The landmasses were joined as one supercontinent when the plant lived.",
                 "Glossopteris evolved separately on every continent in the same way.",
                 "The plant grew in the ocean and washed ashore."],
     "answer": 1,
     "feedback": "<p>Heavy seeds cannot cross thousands of kilometers of ocean. Matching fossils of the same age on separated continents are best explained by the continents being joined.</p>"}),
    ("ESS1-5.1", {"type": "multi",
     "body": "<p>Select the <strong>THREE</strong> observations that are evidence that Africa, India, Antarctica, and South America were once joined.</p>",
     "choices": ["Fossils of <em>Lystrosaurus</em>, a land animal about 250 million years old, are found in Africa, India, and Antarctica.",
                 "Glacial scratches from the same ice age line up in direction when the continents are fitted together.",
                 "Rock layers of the same type and age are found in the matching places across the fitted continents.",
                 "Earthquakes occur in Japan.",
                 "The Atlantic Ocean is saltier than the Indian Ocean."],
     "answer": [0, 1, 2],
     "feedback": "<p>Matching land fossils, glacial scratches that line up, and matching rock layers are all evidence for a joined landmass. Earthquakes in Japan and ocean salt do not bear on the past positions of the continents.</p>"}),
    ("ESS1-5.1", {"type": "tf",
     "body": "<p>True or false: One reason many scientists rejected Wegener's idea of continental drift was that he could not explain what force could move continents.</p>",
     "answer": True,
     "feedback": "<p>True. The evidence for joined continents was strong, but without a mechanism the idea was not accepted until seafloor spreading was discovered.</p>"}),
    # ESS1-5.2
    ("ESS1-5.2", {"type": "choice",
     "body": "<p>A research ship samples the seafloor along a line away from a mid-ocean ridge:</p><table border=\"1\" cellpadding=\"4\"><tbody><tr><th>Site</th><th>Distance from ridge (km)</th><th>Crust age (million years)</th></tr><tr><td>A</td><td>0</td><td>0</td></tr><tr><td>B</td><td>750</td><td>30</td></tr><tr><td>C</td><td>1,750</td><td>?</td></tr></tbody></table><p>If the seafloor keeps spreading at the same rate, what is the age of Site C?</p>",
     "choices": ["About 35 million years", "About 70 million years", "About 130 million years", "About 175 million years"],
     "answer": 1,
     "feedback": "<p>Rate = 750 km / 30 million years = 25 km per million years. 1,750 km / 25 = 70 million years.</p>"}),
    ("ESS1-5.2", {"type": "choice",
     "body": "<p>Which observation best supports the idea that new crust forms at a mid-ocean ridge and moves away in both directions?</p>",
     "choices": ["The stripe pattern of magnetic reversals on one side of the ridge is a mirror image of the pattern on the other side.",
                 "The ridge is the highest mountain range on the seafloor.",
                 "Both sides of the ridge are covered with the same thickness of sediment near the crest.",
                 "Hot water comes out of the seafloor at the ridge."],
     "answer": 0,
     "feedback": "<p>Mirror-image magnetic stripes show that crust formed at the same time on both sides of the ridge and then split apart. The other observations are true but do not show symmetric spreading.</p>"}),
    ("ESS1-5.2", {"type": "choice",
     "body": "<p>Scientists drill sediment cores at three sites on the same side of a mid-ocean ridge:</p><table border=\"1\" cellpadding=\"4\"><tbody><tr><th>Site</th><th>Distance from ridge (km)</th><th>Sediment thickness (m)</th></tr><tr><td>X</td><td>100</td><td>about 20</td></tr><tr><td>Y</td><td>1,200</td><td>about 180</td></tr><tr><td>Z</td><td>2,400</td><td>about 420</td></tr></tbody></table><p>Which explanation fits the data best?</p>",
     "choices": ["Older crust has had more time to collect the shells of dead plankton and other particles.",
                 "Plankton live only in the middle of the ocean.",
                 "Sediment is pushed up from the mantle at the ridge.",
                 "Waves bring more sediment to the middle of the ocean than to the ridge."],
     "answer": 0,
     "feedback": "<p>Sediment slowly settles onto the seafloor. The farther from the ridge, the older the crust and the longer it has been collecting sediment.</p>"}),
    # ESS1-5.3
    ("ESS1-5.3", {"type": "choice",
     "body": "<p>A map shows a deep trench off the coast of a continent, with a line of active volcanoes on land running parallel to the coast. Earthquakes occur at increasing depths moving inland. What does this pattern show?</p>",
     "choices": ["A divergent boundary where new crust is forming.",
                 "A convergent boundary where an ocean plate is sinking beneath the continent.",
                 "A transform boundary where plates slide past each other.",
                 "A hot spot in the middle of a plate."],
     "answer": 1,
     "feedback": "<p>A trench, a volcanic arc, and earthquakes that get deeper inland are the signature of subduction at a convergent boundary.</p>"}),
    ("ESS1-5.3", {"type": "choice",
     "body": "<p>Two plates collide. Plate A is old ocean crust with an average density of about 3.0 g/cm&sup3;. Plate B is continental crust with an average density of about 2.7 g/cm&sup3;. What will happen, and why?</p>",
     "choices": ["Plate B will sink because it is thicker.",
                 "Plate A will sink beneath Plate B because it is denser.",
                 "Both plates will rise to form a mountain range because they have similar densities.",
                 "Neither plate will move, because plates are not affected by density."],
     "answer": 1,
     "feedback": "<p>The denser plate sinks beneath the less-dense one. Old ocean crust is cold and dense, so it subducts.</p>"}),
    ("ESS1-5.3", {"type": "choice",
     "body": "<p>Some continental rocks are nearly 4 billion years old, but no ocean floor is older than about 200 million years. Which statement best explains why continental crust survives longer?</p>",
     "choices": ["Continental crust is less dense, so it resists sinking at subduction zones.",
                 "Continental crust forms at the same ridges as ocean crust.",
                 "Continental crust is never weathered or eroded.",
                 "Continental crust is made of the same material as the mantle."],
     "answer": 0,
     "feedback": "<p>Continental crust is thick and less dense, so it stays at the surface while denser ocean crust is recycled into the mantle.</p>"}),
    # ESS1-6.1
    ("ESS1-6.1", {"type": "choice",
     "body": "<p>A radioactive isotope has a half-life of 100 million years. A rock sample contains 1/8 of the original amount of this isotope. About how old is the rock?</p>",
     "choices": ["100 million years", "300 million years", "800 million years", "1.2 billion years"],
     "answer": 1,
     "feedback": "<p>1/8 means 3 half-lives have passed (1/2 &rarr; 1/4 &rarr; 1/8). 3 &times; 100 million = 300 million years.</p>"}),
    ("ESS1-6.1", {"type": "choice",
     "body": "<p>Which pair correctly matches a sample to the dating method that fits it?</p>",
     "choices": ["A 12,000-year-old piece of charcoal from a campfire &mdash; carbon-14",
                 "A 12,000-year-old piece of charcoal from a campfire &mdash; uranium-238",
                 "A 4-billion-year-old zircon crystal in granite &mdash; carbon-14",
                 "A 4-billion-year-old zircon crystal in granite &mdash; none; it is too old to date"],
     "answer": 0,
     "feedback": "<p>Charcoal was once living wood and is young enough for carbon-14. Billion-year-old zircon is dated with uranium decaying to lead.</p>"}),
    ("ESS1-6.1", {"type": "choice",
     "body": "<p>The oldest known minerals on Earth (zircon crystals) are about 4.4 billion years old. The oldest known meteorites are about 4.56 billion years old. Which conclusion is best supported by this evidence?</p>",
     "choices": ["Earth formed about 4.5 billion years ago, and most of its earliest rock has since been destroyed or recycled.",
                 "Earth is only 4.4 billion years old.",
                 "Meteorites formed on Earth and were thrown into space.",
                 "Earth has no rocks older than 4.4 billion years because none formed before then."],
     "answer": 0,
     "feedback": "<p>Meteorites preserve the age of the solar system, about 4.56 billion years. Earth's oldest surviving minerals are slightly younger because Earth's early crust was recycled.</p>"}),
    # ESS1-5.4
    ("ESS1-5.4", {"type": "choice",
     "body": "<p>Which statement completes the reasoning best?</p><p><em>Continental rock can be billions of years old but ocean-floor rock is less than 200 million years old because&hellip;</em></p>",
     "choices": ["ocean plates are continuously made at ridges and recycled at subduction zones, while buoyant continental crust is not.",
                 "the ocean was not on Earth until 200 million years ago.",
                 "ocean rock erodes faster than continental rock.",
                 "scientists have not found the older ocean rocks yet."],
     "answer": 0,
     "feedback": "<p>The ocean floor is a conveyor belt: created at ridges, destroyed at subduction zones. Continental crust is too buoyant to be recycled that way.</p>"}),
    ("ESS1-5.4", {"type": "essay",
     "body": "<p>A student says, &ldquo;The ocean floor is young because the ocean is young.&rdquo; Use the data below to write a scientific argument that explains why the ocean floor is so much younger than the continents.</p>"
             "<p><strong>Data</strong></p>"
             "<table border=\"1\" cellpadding=\"4\"><tbody><tr><th>Distance from Mid-Atlantic Ridge (km)</th><th>Crust age (million years)</th></tr>"
             "<tr><td>0</td><td>0</td></tr><tr><td>1,000</td><td>40</td></tr><tr><td>2,000</td><td>80</td></tr><tr><td>3,000</td><td>120</td></tr></tbody></table>"
             "<ul><li>The oldest ocean floor on Earth is about 200 million years old.</li>"
             "<li>The oldest minerals found in continental rock are about 4.4 billion years old.</li>"
             "<li>Ocean crust is denser (about 3.0 g/cm&sup3;) than continental crust (about 2.7 g/cm&sup3;).</li>"
             "<li>Ocean plates sink into the mantle at trenches.</li></ul>"
             "<ol><li><strong>Claim:</strong> Answer the question: why is the ocean floor so much younger than the continents?</li>"
             "<li><strong>Evidence:</strong> Use at least <strong>two</strong> specific pieces of data.</li>"
             "<li><strong>Reasoning:</strong> Explain how the evidence supports your claim using what you know about seafloor spreading and subduction.</li>"
             "<li><strong>Counterclaim:</strong> Explain why the student's idea that &ldquo;the ocean is young&rdquo; does not fit the evidence.</li></ol>",
     "rubric": (
         "Rubric (4 pts) - 4: Advanced. Accurate claim that ocean floor is young because it is continually made at ridges and destroyed (recycled) at subduction zones, while less-dense continental crust is not recycled. Cites at least two accurate data points (for example, crust age increases with distance from the ridge from 0 to 120 million years, or the oldest ocean floor is about 200 million years versus continental minerals about 4.4 billion years). Reasoning connects the evidence to the process (new crust at ridges moves away; dense ocean plates sink at trenches; buoyant continents stay at the surface). Counterclaim is addressed: the ocean itself is older than its floor, and the floor is replaced. "
         "3: Proficient. Accurate claim, at least two accurate data points, reasoning present but missing one piece (for example, density or the role of subduction), counterclaim brief or missing. "
         "2: Developing. Claim is partly correct (for example, 'the seafloor is recycled') without a cause. One data point, or inaccurate use of data. Reasoning is vague or restates the evidence. "
         "1: Beginning. Claim is wrong or missing (for example, 'the ocean is young' or 'the seafloor is eroded away'). Little or no data. Major misconception. "
         "0: blank or off-topic. "
         "Grading notes: - Look for: 'made at ridges', 'sinks/subducts at trenches', 'recycled', 'continents are less dense/buoyant'. - Key data: ages increase 40 million years per 1,000 km (about 2.5 cm per year); oldest ocean floor about 200 million years; continental minerals about 4.4 billion years. - Common misconception: ocean floor is 'eroded away' (sediment gets thicker on older crust, so it is not eroded). - Common misconception: the continents are 'older' because they formed first and the ocean formed later. - Sample 4-point response: The ocean floor is much younger than the continents because it is constantly being made at mid-ocean ridges and recycled back into the mantle at subduction zones, but continental crust is too buoyant to sink. The data show the crust is 0 million years old at the ridge and 120 million years old 3,000 km away, so new rock is made at the ridge and moves outward, and the oldest ocean floor is only about 200 million years old. In contrast, continental rock contains minerals 4.4 billion years old. Since ocean crust is denser (3.0 g/cm3) than continental crust (2.7 g/cm3), it sinks at trenches, and the ocean floor is destroyed within a few hundred million years while the continents survive. The student's claim that the ocean is young does not fit, since the ocean basins are old but their floor is constantly replaced."),
     "feedback": ""}),
    ("ESS1-5.4", {"type": "choice",
     "body": "<p>The oldest widely accepted fossils, about 3.5 billion years old, are found in continental rock in Western Australia. No fossils of that age have been found in ocean-floor rock. What is the best explanation?</p>",
     "choices": ["Ocean floor that old has been recycled at subduction zones, so it no longer exists.",
                 "Life did not exist in the oceans until 200 million years ago.",
                 "Fossils cannot form in rock made at mid-ocean ridges.",
                 "Scientists have not drilled the ocean floor yet."],
     "answer": 0,
     "feedback": "<p>The ocean floor does not last long enough to hold the first 3 billion years of life's history. The early fossil record comes from continental rock, which survives much longer.</p>"}),
    ("ESS1-6.1", {"type": "essay",
     "body": "<p>A student writes: &ldquo;Scientists cannot know how old Earth is, because the oldest rock found on Earth is only about 4 billion years old.&rdquo;</p>"
             "<p>Revise this explanation so it is correct and complete. Use these facts:</p>"
             "<ul><li>The oldest known Earth rocks are about 4.0 billion years old, and the oldest minerals (zircons) are about 4.4 billion years old.</li>"
             "<li>The oldest meteorites are about 4.56 billion years old.</li>"
             "<li>Plate tectonics recycles ocean crust, and erosion wears down rock at Earth's surface.</li>"
             "<li>Radiometric dating uses the half-lives of unstable isotopes.</li></ul>"
             "<p>In your revision, explain (1) why the oldest Earth rocks are not the same age as Earth, (2) what meteorites tell us and why, and (3) how scientists find these ages.</p>",
     "rubric": (
         "Rubric (4 pts) - 4: Advanced. Revision states that Earth is about 4.5 to 4.6 billion years old and that the oldest rocks do not give Earth's age because Earth's earliest rocks were destroyed or recycled by plate tectonics and erosion. Explains that meteorites formed with the solar system and have changed little, so their age (about 4.56 billion years) is the best estimate for Earth. Explains that radiometric dating uses the steady decay (half-life) of isotopes such as uranium to lead. Uses at least two of the given facts accurately. "
         "3: Proficient. Correct conclusion with two of the three required ideas explained clearly (recycling, meteorites, radiometric dating). "
         "2: Developing. Partly correct (for example, mentions meteorites or recycling, but not why) or the conclusion is vague. May confuse the oldest rock with Earth's age. "
         "1: Beginning. Repeats the student's misconception or gives an incorrect conclusion (for example, 'Earth is 4 billion years old because that is the oldest rock'). "
         "0: blank or off-topic. "
         "Grading notes: - Look for: 'recycled/destroyed by plate tectonics', 'meteorites changed little', 'half-life', 'uranium', 'about 4.5 billion'. - Common misconception: dating methods work by 'reading rings' or 'counting layers' for all rocks. - Common misconception: radiometric dating changes with temperature or pressure (it does not; decay rates are steady). - Sample 4-point response: Scientists can know Earth's age even though the oldest Earth rocks are only about 4 billion years old, because Earth's earliest rocks were destroyed or recycled by plate tectonics and erosion. Meteorites formed at the same time as the solar system and have changed very little since, so their ages, about 4.56 billion years, show when Earth formed. Scientists find these ages with radiometric dating, which measures how much of an unstable isotope like uranium has decayed to lead, using its steady half-life. So Earth is about 4.5 billion years old."),
     "feedback": ""}),
]

# ---------------------------------------------------------------------- Review (Mastery Path) assignments
# Each: study sections (title, html, optional check) plus 3 questions the student answers in a text box.
REVIEWS = {
    "ESS1-5.1": {
        "use": "your Day 2 notes (The Fossil Puzzle) and your continent puzzle map",
        "sections": [
            ("1. Wegener's big idea",
             "<p>In 1912, Alfred Wegener proposed that all the continents were once joined in one supercontinent, which scientists later named <strong>Pangaea</strong> (&ldquo;all land&rdquo;). Over millions of years the continents drifted apart to their present positions. This is called <strong>continental drift</strong>.</p>",
             "<strong>Try it:</strong> Wegener could not explain what force moves continents. Why did that make many scientists doubt him?",
             "They wanted a cause. Without a force that could move continents, the evidence was not enough for most scientists at the time."),
            ("2. Four lines of evidence",
             "<table border=\"1\" cellpadding=\"6\" style=\"border-collapse:collapse\"><tbody><tr><th>Evidence</th><th>What scientists found</th><th>What it suggests</th></tr>"
             "<tr><td>Fit</td><td>The edges of the continental shelves (not the coastlines) of South America and Africa fit together.</td><td>They were once one piece.</td></tr>"
             "<tr><td>Fossils</td><td>The same land plants and animals (<em>Glossopteris</em>, <em>Mesosaurus</em>, <em>Lystrosaurus</em>, <em>Cynognathus</em>) in the same layers on separated continents.</td><td>The land was connected; they could not cross oceans.</td></tr>"
             "<tr><td>Rocks and mountains</td><td>Rock layers and mountain belts (such as the Appalachians and the Scottish Highlands) match across the Atlantic.</td><td>They formed side by side.</td></tr>"
             "<tr><td>Glaciers</td><td>Ice-age scratches in warm places today line up when the southern continents are fitted together.</td><td>One ice sheet covered the joined landmass.</td></tr></tbody></table>",
             "<strong>Try it:</strong> <em>Mesosaurus</em> lived in fresh water. Why does it make a better clue than a flying bird?",
             "A freshwater reptile could not cross a salt-water ocean, so its fossils on both continents point to a land connection. A bird could fly across."),
        ],
        "questions": [
            "A fossil fern is found in Antarctica and India. Name two other pieces of evidence you would look for to test whether those lands were once joined.",
            "Explain, using the Mesosaurus example, why a fossil on two separated continents can be evidence that they were once joined.",
            "Why did Wegener's idea need more than fossils to be accepted?",
        ],
        "answers": [
            "Any two: matching rock layers, matching mountain belts, glacial scratches that line up, or continental shelf fit.",
            "Mesosaurus lived in fresh water and could not cross the salt-water Atlantic, so finding it on both continents means the continents were joined when it lived.",
            "He could not explain what force moves continents; scientists needed a mechanism, which came from seafloor spreading.",
        ],
    },
    "ESS1-5.2": {
        "use": "your Day 3 notes (Making New Crust), your age-versus-distance graph, and your paper magnetic-stripe model",
        "sections": [
            ("1. The age pattern",
             "<p>At a <strong>mid-ocean ridge</strong>, magma rises and hardens into new ocean crust. The crust splits and moves away on both sides. This is <strong>seafloor spreading</strong>.</p>"
             "<table border=\"1\" cellpadding=\"6\" style=\"border-collapse:collapse\"><tbody><tr><th>Distance from ridge (km)</th><th>Age (million years)</th></tr><tr><td>0</td><td>0</td></tr><tr><td>500</td><td>20</td></tr><tr><td>1,000</td><td>40</td></tr><tr><td>2,000</td><td>80</td></tr></tbody></table>"
             "<p><strong>Rate = distance &divide; time.</strong> 500 km &divide; 20 million years = 25 km per million years = <strong>2.5 cm per year</strong>.</p>",
             "<strong>Try it:</strong> How old is crust 3,000 km from the ridge at this rate?",
             "3,000 &divide; 25 = 120 million years."),
            ("2. Magnetic stripes",
             "<p>As lava hardens, tiny magnetic minerals line up with Earth's magnetic field. Earth's field has reversed many times, so the crust records <strong>stripes</strong> of normal and reversed magnetism. Because the crust splits and moves both ways, the stripes on one side are a <strong>mirror image</strong> of the other side.</p>",
             "<strong>Try it:</strong> What would the stripes look like if crust formed on only one side of the ridge?",
             "They would not be mirror images; the pattern would appear only on one side."),
            ("3. Sediment and life",
             "<p>Sediment (clay and the shells of dead plankton) slowly settles onto the seafloor, so older crust has more sediment. At the ridge, hot water from vents feeds communities of bacteria and tube worms by <strong>chemosynthesis</strong>. When crust moves away and cools, the vents stop and the community dies.</p>",
             "<strong>Try it:</strong> Why is there almost no sediment at the ridge crest?",
             "The crust there is brand new; it has had no time to collect sediment."),
        ],
        "questions": [
            "Crust 2,500 km from a ridge is 100 million years old. Calculate the spreading rate in km per million years, and in cm per year.",
            "Explain why magnetic stripes on both sides of a ridge are mirror images.",
            "Describe how sediment thickness changes with distance from the ridge and explain why.",
        ],
        "answers": [
            "2,500 km / 100 million years = 25 km per million years = 2.5 cm per year.",
            "Crust forms at the ridge recording the magnetic field, then splits and moves away in both directions, so the same sequence of reversals is carried to both sides.",
            "It gets thicker farther from the ridge because older crust has had more time to collect sediment.",
        ],
    },
    "ESS1-5.3": {
        "use": "your Day 4 notes and SketchNotes (Where Crust Goes, and Where It Stays) and your quake and volcano map",
        "sections": [
            ("1. Three kinds of plate boundaries",
             "<table border=\"1\" cellpadding=\"6\" style=\"border-collapse:collapse\"><tbody><tr><th>Boundary</th><th>Plates move&hellip;</th><th>Landforms</th></tr>"
             "<tr><td>Divergent</td><td>apart</td><td>mid-ocean ridges, rift valleys</td></tr>"
             "<tr><td>Convergent</td><td>toward each other</td><td>trenches, volcanic arcs, mountain ranges</td></tr>"
             "<tr><td>Transform</td><td>sliding past</td><td>faults and earthquakes (such as the San Andreas)</td></tr></tbody></table>",
             "<strong>Try it:</strong> Which boundary makes new crust?",
             "Divergent."),
            ("2. Why some crust sinks and some stays",
             "<p>At a convergent boundary, the <strong>denser</strong> plate sinks beneath the less-dense plate. This is <strong>subduction</strong>. Old ocean plates are cold and dense (about 3.0 g/cm&sup3; for the crust), so they sink. Continental crust is thicker and less dense (about 2.7 g/cm&sup3;), so it floats and is rarely pulled down. That is why continental rock can survive for billions of years while the ocean floor is recycled.</p>",
             "<strong>Try it:</strong> A continental plate meets an ocean plate. Which one subducts?",
             "The ocean plate, because it is denser."),
            ("3. What rides the plate down",
             "<p>Ocean plates carry a layer of sediment, including carbon in the shells of dead plankton. Some of it reaches the mantle, and some carbon returns to the air as CO&#8322; from volcanoes. Atoms are recycled, not destroyed.</p>",
             "<strong>Try it:</strong> Name one place the carbon from a plankton shell may end up after subduction.",
             "In the mantle, or back in the atmosphere as CO&#8322; from a volcano."),
        ],
        "questions": [
            "A trench and a chain of volcanoes form where an ocean plate meets a continent. Name the boundary type and explain which plate sinks and why.",
            "Explain why continental crust is rarely subducted.",
            "Describe how subduction connects plate tectonics to the carbon cycle.",
        ],
        "answers": [
            "Convergent boundary; the ocean plate sinks because it is denser than continental crust.",
            "It is thick and less dense (more buoyant) than ocean plates, so it floats instead of sinking.",
            "Plankton shells in seafloor sediment hold carbon; subduction carries it into the mantle, and some returns to the air as CO2 from volcanoes.",
        ],
    },
    "ESS1-6.1": {
        "use": "your Day 5 notes (Reading Deep Time) and your half-life lab graph",
        "sections": [
            ("1. Half-life",
             "<p>Some atoms are unstable and decay into different atoms at a steady rate. The <strong>half-life</strong> is the time for half of the parent atoms to decay.</p>"
             "<table border=\"1\" cellpadding=\"6\" style=\"border-collapse:collapse\"><tbody><tr><th>Half-lives passed</th><th>Fraction of parent left</th></tr><tr><td>0</td><td>1</td></tr><tr><td>1</td><td>1/2</td></tr><tr><td>2</td><td>1/4</td></tr><tr><td>3</td><td>1/8</td></tr></tbody></table>",
             "<strong>Try it:</strong> A sample has 1/16 of its parent atoms left. How many half-lives have passed?",
             "4 (1/2, 1/4, 1/8, 1/16)."),
            ("2. Which clock for which sample?",
             "<table border=\"1\" cellpadding=\"6\" style=\"border-collapse:collapse\"><tbody><tr><th>Method</th><th>Half-life</th><th>Good for</th></tr>"
             "<tr><td>Carbon-14</td><td>5,730 years</td><td>Once-living things (wood, bone, shell) younger than about 50,000 years</td></tr>"
             "<tr><td>Uranium-238 to lead-206</td><td>about 4.47 billion years</td><td>Zircon crystals in igneous rock and meteorites; very old samples</td></tr>"
             "<tr><td>Uranium-235 to lead-207</td><td>about 704 million years</td><td>Zircon crystals in igneous rock and meteorites</td></tr></tbody></table>"
             "<p>Zircon takes uranium into its structure when it forms but leaves out lead, so any lead inside came from decay.</p>",
             "<strong>Try it:</strong> Why can't you use carbon-14 on a billion-year-old rock?",
             "Its half-life is too short; after about 50,000 years almost none is left to measure."),
            ("3. Earth's oldest rocks versus meteorites",
             "<p>Oldest zircon crystals: about 4.4 billion years. Oldest known rocks: about 4.0 billion years. Oldest meteorites: about 4.56 billion years. Plate tectonics and erosion recycled Earth's earliest rocks. Meteorites formed with the solar system and changed little, so they give the best estimate for Earth's age: about 4.5 billion years.</p>",
             "<strong>Try it:</strong> Why does the oldest Earth rock not give the age of Earth?",
             "Earth's earliest rocks have been destroyed or recycled, so the oldest survivors are younger than Earth."),
        ],
        "questions": [
            "A rock formed with 160 atoms of a parent isotope. How many parent atoms are left after 4 half-lives? Show your work.",
            "A bone from a campsite is 9,000 years old, and a zircon crystal in granite is 3 billion years old. Which dating method (carbon-14 or uranium-lead) fits each? Explain why.",
            "Explain why meteorites give a better estimate of Earth's age than the oldest rock found on Earth.",
        ],
        "answers": [
            "160 -> 80 -> 40 -> 20 -> 10. 10 atoms remain.",
            "Bone: carbon-14, because it was once living and is younger than 50,000 years. Zircon: uranium-lead, because it is billions of years old and carbon-14 would be gone.",
            "Earth's earliest rocks were recycled by plate tectonics and erosion, so none survive from Earth's formation; meteorites changed little since they formed with the solar system.",
        ],
    },
    "ESS1-5.4": {
        "use": "your unit CER evidence log and your Day 6 draft argument",
        "sections": [
            ("1. The parts of an argument",
             "<table border=\"1\" cellpadding=\"6\" style=\"border-collapse:collapse\"><tbody><tr><th>Part</th><th>What it is</th><th>Example</th></tr>"
             "<tr><td>Claim</td><td>A complete answer to the question</td><td>The ocean floor is young because it is made at ridges and recycled at subduction zones, while continental crust is too buoyant to be recycled.</td></tr>"
             "<tr><td>Evidence</td><td>Specific data or observations</td><td>Crust is 0 million years old at the ridge and 120 million years old 3,000 km away.</td></tr>"
             "<tr><td>Reasoning</td><td>The science that links evidence to claim</td><td>Dense ocean plates sink at trenches, but less-dense continents float.</td></tr>"
             "<tr><td>Counterclaim</td><td>Another idea and why the evidence does not support it</td><td>&ldquo;The ocean floor is worn away&rdquo; does not fit, since sediment is thicker on older crust.</td></tr></tbody></table>",
             "<strong>Try it:</strong> Is &ldquo;the ocean floor is young&rdquo; a complete claim? Why or why not?",
             "No. It restates the observation and does not give the cause."),
            ("2. Your evidence menu",
             "<ul><li>Crust age increases with distance from the ridge (2.5 cm per year).</li><li>Mirror-image magnetic stripes.</li><li>Sediment is thicker on older crust.</li><li>Oldest ocean floor is about 200 million years; continental minerals about 4.4 billion.</li><li>Ocean crust is denser than continental crust.</li><li>The oldest fossils (about 3.5 billion years) are in continental rock.</li></ul>",
             "<strong>Try it:</strong> Is &ldquo;ocean plates sink because they are denser&rdquo; evidence or reasoning?",
             "Reasoning. It explains why the data look the way they do. Evidence is a measurement or observation, like an age or a distance."),
        ],
        "questions": [
            "Rewrite this weak claim so it fully answers the question: &ldquo;The seafloor is young because it is new rock.&rdquo;",
            "List two pieces of specific evidence for your claim, using numbers or patterns.",
            "Write one sentence of reasoning that links your evidence to your claim.",
        ],
        "answers": [
            "The seafloor is young because new rock is made at mid-ocean ridges and old ocean plates sink into the mantle at subduction zones, while buoyant continental crust stays at the surface.",
            "Any two: ages increase with distance from the ridge (0 to 120 million years across 3,000 km); mirror-image magnetic stripes; sediment thicker on older crust; oldest ocean floor about 200 million years versus continents up to 4.4 billion.",
            "Because ocean plates are denser than continental crust, they sink at trenches and are destroyed, so the ocean floor is always replaced while the continents survive.",
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
