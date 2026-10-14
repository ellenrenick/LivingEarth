"""Question bank for the HS-LS2-5 CSA: Energy Through Carbon (unit 1.2).

45-minute test, 30 points. Edit, then run `python3 ../build_unit.py HS-LS2-5`.
Boundary: no specific chemical steps of photosynthesis and respiration.
"""

TITLE = "HS-LS2-5 Assessment: Energy Through Carbon"
STANDARD = "HS-LS2-5"
QUIZ_ID = "hs_ls2_5_energy_through_carbon"
FILE_PREFIX = "HS-LS2-5"
MAX_ATTEMPTS = 1
TIME_MINUTES = 45
KEY_POSITIONS = [2, 0, 3, 1, 3, 0, 1, 2]

DESCRIPTION = (
    "<p><strong>Living Earth (Biology) &ndash; HS-LS2-5</strong></p>"
    "<p>Develop a model to illustrate the role of photosynthesis and cellular respiration "
    "in the cycling of carbon among the biosphere, atmosphere, hydrosphere, and geosphere.</p>"
    "<p>Part 1: Vocabulary matching &middot; Part 2: Multiple choice &middot; Part 3: Free response</p>"
)

MATCHING = {
    "title": "Part 1: Vocabulary Matching",
    "points": 6,
    "prompt": "<p>Match each term with its best definition. Some definitions will not be used.</p>",
    "pairs": [
        ("Biosphere", "All the living things on Earth and the places they live"),
        ("Atmosphere", "The layer of gases that surrounds Earth, including carbon dioxide"),
        ("Hydrosphere", "All the water on Earth, including oceans, lakes, rivers, and groundwater"),
        ("Geosphere", "The solid Earth, including rocks, soil, and fossil fuels"),
        ("Photosynthesis", "The process that uses light energy to build sugar from carbon dioxide and water"),
        ("Cellular respiration", "The process cells use to release the energy stored in sugar, giving off carbon dioxide"),
    ],
    "distractors": [
        "The process in which a cell divides to make two new cells",
        "The movement of heat from a warm object to a cooler one",
    ],
}

MULTIPLE_CHOICE = [
    {
        "title": "MC 1 - Where is the carbon stored?",
        "dok": 2,
        "prompt": (
            "<p>Scientists estimate how much carbon is stored in four places:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Where the carbon is stored</th><th>Sphere</th><th>Carbon (billions of metric tons)</th></tr>"
            "<tr><td>Carbon dioxide in the air</td><td>Atmosphere</td><td>870</td></tr>"
            "<tr><td>Plants, animals, and soil</td><td>Biosphere</td><td>2,200</td></tr>"
            "<tr><td>Dissolved in the deep ocean</td><td>Hydrosphere</td><td>38,000</td></tr>"
            "<tr><td>Coal, oil, and gas</td><td>Geosphere</td><td>4,000</td></tr>"
            "</table>"
            "<p>Which statement is <strong>best supported</strong> by the table?</p>"
        ),
        "choices": [
            "Carbon is stored in all four spheres, and the deep ocean stores far more than the atmosphere does.",
            "Almost all of Earth's carbon is stored in the atmosphere.",
            "Carbon is stored only in living things and in the ocean.",
            "The geosphere stores more carbon than the other three spheres combined.",
        ],
        "answer": 0,
        "feedback": "The table lists carbon in each of the four spheres. The hydrosphere (38,000) holds the most, and the atmosphere (870) the least.",
    },
    {
        "title": "MC 2 - A forest fire",
        "dok": 2,
        "prompt": (
            "<p>A wildfire burns a large forest. Smoke carrying carbon dioxide rises into the sky.</p>"
            "<p>Which statement <strong>best</strong> describes how carbon moved?</p>"
        ),
        "choices": [
            "Burning moved carbon from the trees (biosphere) into the air (atmosphere), a process other than photosynthesis or respiration.",
            "Photosynthesis moved carbon from the trees into the air.",
            "Cellular respiration moved carbon from the air into the trees.",
            "Carbon was destroyed by the fire, so no carbon went into the air.",
        ],
        "answer": 0,
        "feedback": "Burning (combustion) releases the carbon stored in trees as carbon dioxide. Carbon is moved, not destroyed.",
    },
    {
        "title": "MC 3 - Plant in a sealed jar",
        "dok": 2,
        "prompt": (
            "<p>A student seals a green plant in a clear jar with a carbon dioxide (CO<sub>2</sub>) sensor. "
            "She records the CO<sub>2</sub> level in bright light and then in the dark.</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Condition</th><th>CO<sub>2</sub> at start (ppm)</th><th>CO<sub>2</sub> after 2 hours (ppm)</th></tr>"
            "<tr><td>Bright light</td><td>800</td><td>520</td></tr>"
            "<tr><td>Dark</td><td>800</td><td>950</td></tr>"
            "</table>"
            "<p>Which explanation <strong>best</strong> accounts for the data?</p>"
        ),
        "choices": [
            "In the light, photosynthesis took in more CO2 than the plant's respiration gave off, so CO2 fell; in the dark only respiration continued, so CO2 rose.",
            "In the light, the plant stopped respiring, and in the dark it started respiring.",
            "In the dark, photosynthesis made CO2, so the level rose.",
            "The plant made new carbon atoms in the light and destroyed carbon atoms in the dark.",
        ],
        "answer": 0,
        "feedback": "Plants carry out photosynthesis (only in light) and cellular respiration (all the time). CO2 falls when photosynthesis outpaces respiration and rises when only respiration is happening.",
    },
    {
        "title": "MC 4 - The path of one carbon atom",
        "dok": 2,
        "prompt": (
            "<p>A carbon atom is part of a carbon dioxide molecule in the air. It is taken in by a leaf and built "
            "into sugar. The leaf falls into a river, is carried to a lake, and sinks to the bottom. Over millions "
            "of years, it is buried and becomes part of rock.</p>"
            "<p>Which path <strong>correctly</strong> traces this carbon atom?</p>"
        ),
        "choices": [
            "Atmosphere (CO2) &rarr; biosphere (sugar in a leaf, by photosynthesis) &rarr; hydrosphere (river and lake water) &rarr; geosphere (buried in rock)",
            "Geosphere &rarr; hydrosphere &rarr; biosphere &rarr; atmosphere",
            "Atmosphere &rarr; geosphere &rarr; biosphere &rarr; hydrosphere",
            "Biosphere (leaf) &rarr; atmosphere &rarr; geosphere, with no use of the hydrosphere",
        ],
        "answer": 0,
        "feedback": "Photosynthesis moved the carbon from the air into a leaf. Water carried the leaf, and burial over time moved the carbon into the geosphere.",
    },
    {
        "title": "MC 5 - Clearing a forest",
        "dok": 3,
        "prompt": (
            "<p>A simple model of the carbon cycle shows these arrows: atmosphere &rarr; plants (photosynthesis); "
            "plants and animals &rarr; atmosphere (cellular respiration); atmosphere &harr; ocean (CO<sub>2</sub> dissolves in "
            "and leaves the water).</p>"
            "<p>A large forest is cleared and replaced with a parking lot. Using the model, which prediction "
            "is <strong>best supported</strong>?</p>"
        ),
        "choices": [
            "Less carbon will be taken out of the air by photosynthesis, so more carbon will stay in the atmosphere, and the ocean may take in more of it.",
            "More carbon will be taken out of the air, because fewer plants means less respiration.",
            "The amount of carbon in the atmosphere will not change, because carbon is destroyed when trees are removed.",
            "The ocean will release all its carbon, because forests and oceans are the same sphere.",
        ],
        "answer": 0,
        "feedback": "Removing the forest removes the arrow that moves carbon out of the air. When one part of the model changes, carbon builds up elsewhere.",
    },
    {
        "title": "MC 6 - The seasonal CO2 wave",
        "dok": 3,
        "prompt": (
            "<p>A weather station in the Northern Hemisphere records carbon dioxide in the air through one year.</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Month</th><th>March</th><th>May</th><th>July</th><th>September</th><th>November</th></tr>"
            "<tr><td>CO<sub>2</sub> (ppm)</td><td>423</td><td>425</td><td>422</td><td>418</td><td>421</td></tr>"
            "</table>"
            "<p>Which explanation for the drop from May to September is <strong>best supported</strong>?</p>"
        ),
        "choices": [
            "In the Northern Hemisphere's spring and summer, plants grow and their photosynthesis takes in more CO2 than is returned by respiration, so CO2 in the air falls.",
            "In the summer, plants stop respiring, so no CO2 is added to the air.",
            "In the summer, photosynthesis makes carbon, which raises the CO2 level.",
            "The drop is caused by the ocean, because the ocean is the only sphere that takes in CO2.",
        ],
        "answer": 0,
        "feedback": "In the growing season, photosynthesis removes more CO2 from the air than respiration returns. When plants slow down in fall, CO2 rises again.",
    },
    {
        "title": "MC 7 - Do plants respire?",
        "dok": 2,
        "prompt": (
            "<p>A student says, &ldquo;Plants only do photosynthesis. Cellular respiration is something "
            "that only animals do.&rdquo;</p>"
            "<p>Which piece of evidence <strong>best refutes</strong> this claim?</p>"
        ),
        "choices": [
            "A plant kept in the dark gives off CO2, which shows its cells are doing cellular respiration.",
            "A plant in the light takes in CO2.",
            "Animals give off CO2 when they breathe out.",
            "A plant needs water and light to make sugar.",
        ],
        "answer": 0,
        "feedback": "In the dark there is no photosynthesis, yet the plant still gives off CO2. Plant cells release the energy in sugar by cellular respiration, just as animal cells do.",
    },
    {
        "title": "MC 8 - Completing a student's model",
        "dok": 3,
        "prompt": (
            "<p>A student's model of the carbon cycle has only two arrows: photosynthesis moves carbon from the "
            "atmosphere into plants, and respiration moves carbon from plants back to the atmosphere.</p>"
            "<p>Which addition would make the model <strong>most complete</strong> as a model of the carbon cycle among the four spheres?</p>"
        ),
        "choices": [
            "Add the ocean and rocks, with arrows for carbon dissolving in water, dead organisms being buried over time, and burning of fossil fuels.",
            "Add more arrows between plants and the atmosphere so the arrows are bolder.",
            "Add the Sun as a source of carbon atoms.",
            "Remove the plants, because carbon moves only through the air.",
        ],
        "answer": 0,
        "feedback": "A model of the carbon cycle should include all four spheres and the other processes that move carbon, such as dissolving, burial, and burning. The Sun supplies energy, not carbon.",
    },
]

FREE_RESPONSE = [
    {
        "title": "FR 1 - A tree-planting project",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>A city plants thousands of trees on an empty lot. Scientists measure the carbon stored in the "
            "trees and the carbon dioxide level just above the lot at noon in July.</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Years after planting</th><th>0</th><th>3</th><th>6</th><th>10</th></tr>"
            "<tr><td>Carbon stored in trees (metric tons)</td><td>0</td><td>150</td><td>520</td><td>1,100</td></tr>"
            "<tr><td>CO<sub>2</sub> above the lot (ppm)</td><td>428</td><td>425</td><td>421</td><td>414</td></tr>"
            "</table>"
            "<p>Write an explanation using <strong>Claim, Evidence, and Reasoning</strong>:</p>"
            "<ol>"
            "<li><strong>Claim:</strong> Explain how the trees changed where carbon is stored.</li>"
            "<li><strong>Evidence:</strong> Use at least <strong>two</strong> pieces of data from the table.</li>"
            "<li><strong>Reasoning:</strong> Name the process that moved the carbon and trace one carbon atom through at least <strong>three</strong> spheres, from the air to a place where it could be stored for a long time. Then explain what role cellular respiration plays for the trees.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Accurate claim that the trees moved carbon from the atmosphere into the biosphere. "
             "Cites at least two accurate data points and links them (carbon in trees rises while CO2 above the lot falls). "
             "Names photosynthesis as the process and traces one atom through at least three spheres correctly (for example, atmosphere to biosphere, to geosphere or hydrosphere by decay, burial, or runoff). "
             "Explains that trees also do cellular respiration, returning some carbon to the atmosphere, so the net change is still storage."),
            (3, "Proficient",
             "Accurate claim and two accurate data points. "
             "Names photosynthesis and traces through three spheres, or describes the role of respiration, but one piece is thin or missing."),
            (2, "Developing",
             "Claim is partly correct (for example, \"trees take in CO2\") without linking to storage. "
             "One data point or inaccurate data use. Path has fewer than three spheres, or confuses photosynthesis and respiration."),
            (1, "Beginning",
             "Claim is wrong or missing. Little or no data. Reasoning shows a major misconception (for example, trees make carbon or photosynthesis releases CO2 to the air)."),
        ],
        "grading_notes": [
            "Key data: carbon stored 0 to 1,100 tons; CO2 428 to 414 ppm. Both support photosynthesis moving carbon from the air into the trees.",
            "Accept any correct three-sphere path, such as atmosphere to biosphere (tree) to geosphere (soil or buried wood) or to hydrosphere (runoff).",
            "Do not require the chemical equations or steps of photosynthesis or respiration; they are outside the HS-LS2-5 assessment boundary.",
            "Common misconceptions: trees \"make\" carbon; photosynthesis gives off CO2; plants do not respire.",
        ],
        "exemplar": (
            "The trees moved carbon out of the atmosphere and stored it in the biosphere. The carbon stored in the trees rose from 0 to 1,100 tons in 10 years while the CO2 above the lot fell from 428 to 414 ppm. "
            "Through photosynthesis, the trees take in CO2 from the air and use light energy to build sugar, so carbon moves from the atmosphere into the biosphere. "
            "One carbon atom could go from the air into a leaf, then the leaf falls and is carried by runoff into a stream (hydrosphere) or is buried in soil (geosphere), where it can stay stored a long time. "
            "The trees also do cellular respiration, which releases some carbon back to the air as CO2, but photosynthesis takes in more than respiration returns, so the trees store carbon overall."
        ),
    },
    {
        "title": "FR 2 - Model a wildfire",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>Use words and arrows (such as &ldquo;A &rarr; B&rdquo;) to describe a <strong>model</strong> of the carbon cycle "
            "for a forest and the ocean next to it. Your model must:</p>"
            "<ol>"
            "<li>Include all four spheres (biosphere, atmosphere, hydrosphere, geosphere).</li>"
            "<li>Include <strong>photosynthesis</strong> and <strong>cellular respiration</strong>, and label what each does to carbon (which sphere carbon moves from and to).</li>"
            "<li>Include at least <strong>one more process</strong> that moves carbon (for example, burning, decay, burial, or dissolving in water).</li>"
            "</ol>"
            "<p>Then use your model to <strong>predict</strong> what happens to the other parts of the model when a large wildfire burns most of the forest. Explain your prediction.</p>"
        ),
        "rubric": [
            (4, "Advanced",
             "The model includes all four spheres, with correctly directed arrows for photosynthesis (atmosphere to biosphere) and cellular respiration (biosphere to atmosphere), plus at least one more correct process. "
             "The prediction follows from the model: burning moves carbon from the biosphere to the atmosphere, less photosynthesis removes less carbon later, more CO2 stays in the air, and the ocean may take in more. "
             "The explanation links each effect to an arrow in the model."),
            (3, "Proficient",
             "The model includes all four spheres and both processes with correct directions. "
             "The prediction is correct but only partly linked to the model, or one effect is missing."),
            (2, "Developing",
             "The model has only two or three spheres, or one of the arrows is reversed. "
             "The prediction is vague or not connected to the model."),
            (1, "Beginning",
             "The model lists spheres or processes without arrows or shows a major misconception. The prediction is missing or incorrect."),
        ],
        "grading_notes": [
            "Directions to check: photosynthesis moves carbon from atmosphere to biosphere; cellular respiration moves it from biosphere to atmosphere.",
            "Accept any correct additional process: burning, decay, burial, dissolving in or release from water, runoff, or eruption.",
            "The prediction should name at least two effects of the fire: more CO2 in the air right away and less photosynthesis afterward.",
            "Do not require chemical equations or steps; they are outside the HS-LS2-5 assessment boundary.",
        ],
        "exemplar": (
            "Model: Atmosphere (CO2) -> biosphere (trees), by photosynthesis. Biosphere -> atmosphere, by cellular respiration. Atmosphere <-> hydrosphere (ocean), as CO2 dissolves in and leaves the water. "
            "Biosphere -> geosphere, as dead trees are buried and slowly become soil or fossil fuel. Biosphere -> atmosphere, by burning. "
            "Prediction: A wildfire burns the trees, so burning moves a large amount of carbon from the biosphere to the atmosphere. "
            "With fewer trees, less photosynthesis happens, so less CO2 is removed from the air in the following years, and more carbon stays in the atmosphere. "
            "The ocean may take in more of the extra CO2, so the hydrosphere may hold more carbon, and less will be buried in the geosphere because there are fewer dead plants."
        ),
    },
]
