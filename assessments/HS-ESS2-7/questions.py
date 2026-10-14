"""Question bank for the HS-ESS2-7 CSA: Changing Earth, Changing Life (unit 3.2).

45-minute test, 30 points. Edit, then run `python3 ../build_unit.py HS-ESS2-7`.
Boundary: no comprehensive understanding of how the biosphere interacts with all of Earth's systems.
CSA items stop at DOK 3 (the department rates ESS2-7.5 at DOK 4).
"""

TITLE = "HS-ESS2-7 Assessment: Changing Earth, Changing Life"
STANDARD = "HS-ESS2-7"
QUIZ_ID = "hs_ess2_7_changing_earth_changing_life"
FILE_PREFIX = "HS-ESS2-7"
MAX_ATTEMPTS = 1
TIME_MINUTES = 45
KEY_POSITIONS = [2, 0, 3, 1, 0, 2, 3, 1]

DESCRIPTION = (
    "<p><strong>Living Earth (Biology) &ndash; HS-ESS2-7</strong></p>"
    "<p>Construct an argument based on evidence about the simultaneous coevolution of Earth's "
    "systems and life on Earth.</p>"
    "<p>Part 1: Vocabulary matching &middot; Part 2: Multiple choice &middot; Part 3: Free response</p>"
)

MATCHING = {
    "title": "Part 1: Vocabulary Matching",
    "points": 6,
    "prompt": "<p>Match each term with its best definition. Some definitions will not be used.</p>",
    "pairs": [
        ("Biosphere", "All the living things on Earth and the places they live"),
        ("Atmosphere", "The layer of gases that surrounds Earth"),
        ("Weathering", "The breaking down of rock into smaller pieces by water, air, ice, or living things"),
        ("Feedback", "A change in a system that causes further changes that speed up or slow down the original change"),
        ("Fossil", "The preserved remains or traces of a living thing from long ago"),
        ("Coevolution of Earth and life", "The idea that Earth's systems and living things change each other over time"),
    ],
    "distractors": [
        "The movement of rock and soil from one place to another by water or wind",
        "The group of organisms of one kind that live in the same area",
    ],
}

MULTIPLE_CHOICE = [
    {
        "title": "MC 1 - Where did the oxygen come from?",
        "dok": 2,
        "prompt": (
            "<p>Scientists compile this timeline from rocks and fossils:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Billions of years ago</th><th>Evidence in the rock record</th></tr>"
            "<tr><td>3.5</td><td>Fossils of tiny microbes that carried out photosynthesis; oxygen in the air is almost zero</td></tr>"
            "<tr><td>2.4 to 1.8</td><td>Layers of rusted iron in rocks around the world; oxygen starts to build up in the air</td></tr>"
            "<tr><td>0.6</td><td>First large animals, which need oxygen</td></tr>"
            "</table>"
            "<p>Which statement is <strong>best supported</strong> by the timeline?</p>"
        ),
        "choices": [
            "Photosynthetic microbes released oxygen that changed the atmosphere, and the oxygen later made it possible for large animals to evolve.",
            "Large animals produced the oxygen in the air, which then allowed microbes to evolve.",
            "The atmosphere changed on its own, and life had no effect on it.",
            "Oxygen was always plentiful, so life did not change the atmosphere.",
        ],
        "answer": 0,
        "feedback": "Photosynthetic life changed the atmosphere by adding oxygen, and the new atmosphere made later forms of life possible.",
    },
    {
        "title": "MC 2 - Oxygen and rocks",
        "dok": 2,
        "prompt": (
            "<p>After photosynthetic microbes added oxygen to the air, the oxygen reacted with rock at Earth's surface, "
            "making the rock break down faster. Weathering released more nutrients to the oceans, where more life could grow.</p>"
            "<p>Which sequence <strong>best</strong> shows how life and Earth's systems changed each other?</p>"
        ),
        "choices": [
            "Life changed the atmosphere &rarr; the changed atmosphere increased weathering of rock &rarr; more nutrients in the oceans supported more life",
            "More weathering &rarr; less oxygen &rarr; fewer microbes",
            "Weathering of rock &rarr; microbes appeared &rarr; the atmosphere had no change",
            "Rocks stopped weathering &rarr; the oceans lost nutrients &rarr; life changed the atmosphere",
        ],
        "answer": 0,
        "feedback": "Each step affects the next: life changed the atmosphere, the atmosphere changed rock weathering, and weathering changed the nutrients available to life.",
    },
    {
        "title": "MC 3 - Soil on bare rock",
        "dok": 2,
        "prompt": (
            "<p>A scientist measures soil depth in three places that started as bare rock:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Site</th><th>Living things present</th><th>Soil depth (cm)</th></tr>"
            "<tr><td>1</td><td>None</td><td>0</td></tr>"
            "<tr><td>2</td><td>Microbes and lichens</td><td>2</td></tr>"
            "<tr><td>3</td><td>Mosses, shrubs, and trees</td><td>35</td></tr>"
            "</table>"
            "<p>Which conclusion is <strong>best supported</strong> by the data?</p>"
        ),
        "choices": [
            "Living things help break down rock and add material that forms soil, and soil in turn supports more kinds of life.",
            "Soil forms only where there is no life.",
            "Soil depth has no connection to the living things at a site.",
            "Trees grew first and the soil then disappeared.",
        ],
        "answer": 0,
        "feedback": "Where life is present, more soil has formed. Soil lets larger plants grow, which in turn adds more soil.",
    },
    {
        "title": "MC 4 - A coral reef coast",
        "dok": 3,
        "prompt": (
            "<p>Scientists compare two coastlines in the same ocean. One has a coral reef offshore; the other does not.</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th></th><th>With reef</th><th>Without reef</th></tr>"
            "<tr><td>Average wave height at the shore (m)</td><td>0.3</td><td>1.2</td></tr>"
            "<tr><td>Shoreline erosion (cm per year)</td><td>0.5</td><td>6</td></tr>"
            "<tr><td>Number of fish species living nearby</td><td>220</td><td>15</td></tr>"
            "</table>"
            "<p>Which claim is <strong>best supported</strong> by the data?</p>"
        ),
        "choices": [
            "Corals changed how waves reach the shore and how fast the shoreline erodes, and the reef created habitat for many new forms of life.",
            "Coral reefs have no effect on waves or erosion.",
            "Erosion creates the reef, and the reef is not alive.",
            "Fish create the waves, which then protect the coral.",
        ],
        "answer": 0,
        "feedback": "Living corals built a reef that reduced wave energy and erosion. The reef also became a habitat for many species.",
    },
    {
        "title": "MC 5 - An asteroid impact",
        "dok": 2,
        "prompt": (
            "<p>About 66 million years ago, a large asteroid struck Earth. Dust and smoke blocked sunlight for years and "
            "the climate cooled. Fossils show that many large animals, including the dinosaurs, died out. Small mammals survived "
            "and later became many new kinds of mammals.</p>"
            "<p>Which statement <strong>best</strong> shows how an Earth event changed life?</p>"
        ),
        "choices": [
            "The impact changed the atmosphere and climate, which caused many species to die out, and the survivors then evolved to fill new roles.",
            "The animals changed the climate by dying out.",
            "The asteroid created new species directly from rock.",
            "The climate did not change, so the extinction had another cause.",
        ],
        "answer": 0,
        "feedback": "An Earth event (the impact) changed conditions so many species died out. Survivors evolved to fill the open habitats.",
    },
    {
        "title": "MC 6 - Evaluating a student's claim",
        "dok": 2,
        "prompt": (
            "<p>A student writes, &ldquo;Earth changes life, but life never changes Earth.&rdquo;</p>"
            "<p>Which piece of evidence <strong>best refutes</strong> the second part of this claim?</p>"
        ),
        "choices": [
            "The oxygen in today's atmosphere was added by photosynthetic organisms over billions of years.",
            "Volcanic eruptions put gas and ash into the air.",
            "Ice ages change where animals can live.",
            "Rock can be broken down by freezing and thawing water.",
        ],
        "answer": 0,
        "feedback": "The other examples are Earth processes acting on life or rock. Oxygen from photosynthetic life shows life changing Earth's atmosphere.",
    },
    {
        "title": "MC 7 - Which evidence fits together?",
        "dok": 3,
        "prompt": (
            "<p>A group of students wants to argue that Earth's systems and life changed together over time. "
            "They have four kinds of evidence: <em>(a)</em> rusted iron layers in rocks that formed after 2.4 billion years ago, "
            "<em>(b)</em> fossils of microbes that made oxygen, <em>(c)</em> gas trapped in ancient rocks showing oxygen rising, "
            "and <em>(d)</em> fossils of large animals that appear after oxygen was plentiful.</p>"
            "<p>Which argument is <strong>strongest</strong>?</p>"
        ),
        "choices": [
            "Combining all four: life added oxygen to the air (b, c), the oxygen changed rocks (a), and the changed air made large animals possible (d), so Earth and life changed together.",
            "Using only (a), because rust is easier to see than fossils.",
            "Using only (d), because animals are more interesting than microbes.",
            "Using none of them, because evidence from long ago cannot be trusted.",
        ],
        "answer": 0,
        "feedback": "The strongest arguments combine several kinds of evidence that fit together into one story.",
    },
    {
        "title": "MC 8 - A growing feedback",
        "dok": 3,
        "prompt": (
            "<p>On bare ground, lichens and microbes break down rock and add organic material that becomes thin soil. "
            "Thin soil lets mosses and grasses grow. These plants add more organic material and hold the soil in place.</p>"
            "<p>Which statement <strong>best</strong> describes the pattern?</p>"
        ),
        "choices": [
            "A feedback in which life makes soil, and the soil supports more life, which makes still more soil.",
            "A pattern in which soil causes life but life never affects soil.",
            "A pattern in which the plants and microbes slow down the formation of soil.",
            "A pattern with no connection between living things and soil.",
        ],
        "answer": 0,
        "feedback": "Life builds soil, soil supports more life, and more life builds more soil. That loop is a feedback.",
    },
]

FREE_RESPONSE = [
    {
        "title": "FR 1 - The oxygen story",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>Use this evidence from the rock and fossil records:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Billions of years ago</th><th>Evidence</th></tr>"
            "<tr><td>3.5</td><td>Fossils of microbes that carried out photosynthesis. Almost no oxygen in the air.</td></tr>"
            "<tr><td>2.4</td><td>Oxygen starts to build up in the atmosphere.</td></tr>"
            "<tr><td>2.4 to 1.8</td><td>Rusted iron layers form worldwide. Rocks at the surface weather faster.</td></tr>"
            "<tr><td>0.6</td><td>First large animals, which need oxygen to live.</td></tr>"
            "</table>"
            "<p>Write an argument using <strong>Claim, Evidence, and Reasoning</strong>:</p>"
            "<ol>"
            "<li><strong>Claim:</strong> Argue that Earth's systems and life changed each other over time.</li>"
            "<li><strong>Evidence:</strong> Use at least <strong>three</strong> pieces of evidence from the table.</li>"
            "<li><strong>Reasoning:</strong> Explain one way life changed Earth and one way the changed Earth changed life. Connect them in a chain of cause and effect.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Clear claim that Earth and life changed each other. Cites at least three accurate pieces of evidence from different rows. "
             "Reasoning gives a complete two-way chain: photosynthetic life added oxygen to the atmosphere (life changed Earth); oxygen increased weathering and made oxygen-using animals possible (Earth changed life). "
             "Shows how the steps connect in time."),
            (3, "Proficient",
             "Clear claim and at least two accurate pieces of evidence. Reasoning gives both directions but one link in the chain is thin."),
            (2, "Developing",
             "Claim is partly correct. One or two pieces of evidence used with little explanation. Reasoning shows only one direction (life changed Earth or Earth changed life)."),
            (1, "Beginning",
             "Claim is wrong or missing. Little or no evidence. Shows a major misconception (for example, animals made the oxygen)."),
        ],
        "grading_notes": [
            "Two-way answer: life to Earth (photosynthesis adds oxygen to the air) and Earth to life (more oxygen allows large animals, and faster weathering supplied nutrients).",
            "Accept any three accurate rows as evidence. Rewards linking the dates.",
            "Do not require a complete account of how the biosphere interacts with every system; it is outside the HS-ESS2-7 assessment boundary.",
            "Common misconception: oxygen was always in the air, or animals produced the oxygen.",
        ],
        "exemplar": (
            "Earth's systems and life changed each other. Fossils show photosynthetic microbes existed 3.5 billion years ago when the air had almost no oxygen, and then oxygen started to build up 2.4 billion years ago. "
            "The oxygen also reacted with rock, forming rusted iron layers worldwide and making surface rocks weather faster. Finally, the first large animals appeared 0.6 billion years ago, and they need oxygen. "
            "Life changed Earth because the microbes' photosynthesis added oxygen to the atmosphere. Earth then changed life, because the new atmosphere made it possible for oxygen-using animals to live, and faster weathering released more nutrients. "
            "So the change in the atmosphere is the link between early microbes and later animals."
        ),
    },
    {
        "title": "FR 2 - A new volcanic island",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>A volcano builds a new island of bare rock. Scientists visit it over several hundred years:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Years since eruption</th><th>0</th><th>20</th><th>100</th><th>300</th></tr>"
            "<tr><td>Soil depth (cm)</td><td>0</td><td>1</td><td>12</td><td>40</td></tr>"
            "<tr><td>Kinds of plants and microbes</td><td>0</td><td>5</td><td>40</td><td>120</td></tr>"
            "<tr><td>Rock broken down each year (relative)</td><td>1</td><td>2</td><td>5</td><td>9</td></tr>"
            "</table>"
            "<ol>"
            "<li><strong>Argue</strong> that life and the island's rock and soil changed together over time, using at least two pieces of data.</li>"
            "<li><strong>Explain</strong> how one change makes another change more likely (a feedback).</li>"
            "<li><strong>Predict</strong> what would happen to the soil if most of the plants were removed, and explain why.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Argues that life and the island changed together, citing at least two accurate data points that rise together. "
             "Explains a complete feedback (life breaks down rock and adds material, forming soil; soil supports more life; more life forms more soil). "
             "Predicts correctly that soil would thin or wash away and explains that the plants held and added to the soil."),
            (3, "Proficient",
             "Argues correctly with two data points and explains the feedback, but the prediction is brief or not fully explained."),
            (2, "Developing",
             "Cites one data point, or the feedback is stated without a connection between life and soil. Prediction is vague."),
            (1, "Beginning",
             "Claim is wrong or missing. Little or no data. Shows a major misconception (for example, soil causes the volcano)."),
        ],
        "grading_notes": [
            "Key data: soil 0 to 40 cm; kinds of life 0 to 120; rock breakdown 1 to 9 over 300 years.",
            "Accept any correct feedback: life forms soil, soil supports more life, and more life forms more soil.",
            "Prediction: removing plants reduces new soil and leaves it open to erosion; accept thinning or wash-away with a reason.",
            "Do not require a comprehensive account of how the biosphere interacts with all of Earth's systems; it is outside the HS-ESS2-7 assessment boundary.",
        ],
        "exemplar": (
            "Life and the island changed together. Over 300 years, the soil deepened from 0 to 40 cm while the kinds of plants and microbes rose from 0 to 120, and the rock broken down each year rose from 1 to 9. "
            "This is a feedback: microbes and lichens break down rock and add material that makes thin soil, the soil lets more plants grow, and the larger plants add more material and break down more rock, so even more soil forms. "
            "If most plants were removed, the soil would thin or wash away, because plants add new material to the soil and their roots hold it in place, so soil would form more slowly and erode faster."
        ),
    },
]
