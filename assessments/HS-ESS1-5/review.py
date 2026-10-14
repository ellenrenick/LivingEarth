"""Unit review for HS-ESS1-5 (unit 3.1). Done on the review day, built around the CFAs (no practice test)."""

STANDARD = "HS-ESS1-5"
UNIT_TITLE = "Age of the Earth"
GOAL = ("Evaluate evidence for past and present movements of continental and oceanic crust, and judge how well "
        "the theory of plate tectonics explains the ages of crustal rocks.")

KEY_IDEAS = [
    "<strong>Earth's outer layer is broken into tectonic plates</strong> that slowly move. Plate boundaries are <em>divergent</em> (move apart), <em>convergent</em> (move together), or <em>transform</em> (slide past).",
    "<strong>Ocean crust is made at mid-ocean ridges</strong> (divergent boundaries) and <strong>destroyed at subduction zones</strong> (convergent boundaries), where it sinks into the mantle.",
    "<strong>Seafloor rock gets older with distance from a ridge,</strong> on both sides. This pattern shows the seafloor spreads.",
    "<strong>Ocean crust is young</strong> (under about 200 million years old) because it is constantly recycled. <strong>Continental crust is older</strong> (up to about 4,000 million years) because it is less dense and is not recycled as easily.",
    "<strong>Continents grew outward</strong> from ancient cores as plate collisions added newer crust around the edges.",
    "<strong>Strong evidence comes from several independent lines</strong> that agree: GPS (now), seafloor ages and magnetic stripes (past), and matching fossils and rocks (past).",
]

VOCAB = {
    "bank": ["tectonic plate", "mid-ocean ridge", "subduction zone", "divergent boundary", "convergent boundary", "transform boundary"],
    "blanks": [
        ("A large, rigid piece of Earth's outer layer that slowly moves is a ____________.", "tectonic plate"),
        ("New ocean crust forms at a ____________.", "mid-ocean ridge"),
        ("Where one plate sinks beneath another and is recycled is a ____________.", "subduction zone"),
        ("Two plates moving apart form a ____________.", "divergent boundary"),
        ("Two plates moving toward each other form a ____________.", "convergent boundary"),
        ("Two plates sliding past each other form a ____________.", "transform boundary"),
    ],
}

SECTIONS = [
    {"id": "A", "title": "Plates and boundaries", "lts": ["ESS1-5.1", "ESS1-5.2"],
     "intro": "<p>Name the boundary and say whether crust is made, destroyed, or neither.</p>",
     "items": [
         ("Plates move apart and hot rock rises to fill the gap under the ocean.", "Divergent boundary; new crust is made."),
         ("A dense ocean plate bends and sinks beneath a continental plate.", "Convergent boundary (subduction zone); ocean crust is destroyed."),
         ("Two plates slide past each other with large earthquakes but no new crust.", "Transform boundary; crust is neither made nor destroyed."),
         ("Where is ocean crust made, and where does it sink back into the mantle?", "It is made at mid-ocean ridges and sinks at subduction zones."),
     ]},
    {"id": "B", "title": "Reading rock-age data", "lts": ["ESS1-5.3"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Distance from ridge (km)</th><th>0</th><th>300</th><th>600</th><th>1,200</th></tr><tr><td>Rock age (million years)</td><td>0</td><td>15</td><td>30</td><td>60</td></tr></table>",
     "items": [
         ("Describe the pattern in the ages.", "Rock gets older as distance from the ridge increases."),
         ("What process does the pattern show?", "New crust forms at the ridge and spreads outward over time."),
         ("The spreading rate: 600 km in 30 million years. Calculate the rate in km per million years and predict the age 900 km away.", "600 / 30 = 20 km per million years. At 900 km: 900 / 20 = 45 million years."),
         ("What pattern would you expect on the other side of the ridge?", "A matching pattern: ages increase with distance on both sides."),
     ]},
    {"id": "C", "title": "Why ocean crust is young and continents are old", "lts": ["ESS1-5.4"],
     "intro": "<p>The oldest ocean crust is about 180 million years old. The oldest continental rocks are about 4,000 million years old.</p>",
     "items": [
         ("Explain why the oldest ocean crust is so much younger.", "It is continually made at ridges and recycled into the mantle at subduction zones."),
         ("Why can continental crust be so much older?", "It is less dense and is not recycled as easily."),
         ("A continent's rocks are 3,500 million years old at the core and 400 million years old at the edge. What does this show about how the continent formed?", "It grew outward from an ancient core as plate interactions added newer crust at the edges."),
     ]},
    {"id": "D", "title": "How strong is the evidence?", "lts": ["ESS1-5.5"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Evidence</th><th>What was found</th></tr><tr><td>GPS</td><td>Stations on different plates move a few cm per year</td></tr><tr><td>Seafloor ages</td><td>Older with distance from ridges, on both sides</td></tr><tr><td>Fossils</td><td>The same land reptile in South America and Africa</td></tr></table>",
     "items": [
         ("For each line of evidence, say whether it shows past or current movement.", "GPS: current. Seafloor ages: past. Fossils: past."),
         ("Why is it stronger to use all three lines than only one?", "They are independent and all point to the same conclusion."),
         ("Name one limit of one line of evidence.", "Example: GPS covers only a few decades; fossils alone could be explained by animals crossing a land bridge."),
     ]},
    {"id": "E", "title": "Judging the theory", "lts": ["ESS1-5.6"],
     "intro": "<p>Decide how well plate tectonics explains each observation.</p>",
     "items": [
         ("Seafloor rock is youngest at ridges and symmetrical on both sides. Does plate tectonics explain it? How?", "Yes. New crust forms at the ridge and spreads both ways."),
         ("The oldest ocean floor is about 180 million years old but Earth is 4,600 million years old. Explain.", "Ocean crust is recycled at subduction zones, so older ocean floor has been destroyed."),
         ("Name one question the theory does not answer by itself.", "Example: how the first continental crust formed, or how plate motion began."),
         ("Rate the theory as a strong, medium, or weak explanation of rock ages, and give two reasons.", "Strong: it explains very different ages with one set of processes, and it matches many independent measurements."),
     ]},
]

WRITE = {
    "prompt": ("<p>A student claims, &ldquo;The continents have always been where they are today.&rdquo; Use this evidence:</p>"
               "<table border=\"1\" cellpadding=\"6\"><tr><th>Evidence</th><th>What was found</th></tr>"
               "<tr><td>A. Mountain belts</td><td>The same type of mountain belt, with matching rock ages, runs through eastern North America and Scotland, which are now separated by an ocean.</td></tr>"
               "<tr><td>B. GPS</td><td>Greenland is moving away from Europe at about 2 cm per year.</td></tr>"
               "<tr><td>C. Seafloor ages</td><td>0 million years old at the Mid-Atlantic Ridge and 100 million years old 2,000 km away, on both sides.</td></tr></table>"
               "<p>Write an evaluation: <strong>Claim</strong>, <strong>Evidence</strong> (at least two lines), and <strong>Reasoning</strong> (what each line shows about past or current movement, how strong the evidence is overall, and one limit).</p>"),
    "checklist": ["Rejects the claim that the continents have not moved",
                  "Uses at least two lines of evidence with specific details",
                  "Says whether each line shows past or current movement",
                  "Judges that the evidence is strong because independent lines agree",
                  "Names a reasonable limit of one line of evidence"],
    "exemplar": ("The claim is not supported; the continents have moved in the past and are moving now. Greenland is moving away from Europe at about 2 cm per year, which shows current motion. The seafloor is 0 million years old at the Mid-Atlantic Ridge and 100 million years old 2,000 km away on both sides, which shows new crust formed at the ridge and spread apart over time. "
                 "A matching mountain belt in North America and Scotland suggests they were once joined. The evidence is strong because three independent kinds agree. One limit is that GPS covers only a short time, so alone it cannot show what happened millions of years ago."),
}
