"""Question bank for the HS-LS1-6 practice test (about 20 minutes).

Uses new scenarios that parallel the summative test without repeating its
items. Run `python3 build.py` after editing.
"""

TITLE = "HS-LS1-6 Practice Test: From Sugar to Building Blocks"
QUIZ_ID = "hs_ls1_6_practice"
FILE_PREFIX = "HS-LS1-6_practice"
MAX_ATTEMPTS = "unlimited"
TIME_MINUTES = 20
# Where the correct answer lands for each MC item (0 = A), balanced across letters.
KEY_POSITIONS = [2, 0, 3, 1, 3, 0]

# ---------------------------------------------------------------------------
# Part 1: Vocabulary matching (about 3 minutes)
# ---------------------------------------------------------------------------
MATCHING = {
    "title": "Part 1: Vocabulary Matching",
    "points": 6,
    "prompt": (
        "<p>Match each term with its best definition. Some definitions will "
        "not be used.</p>"
    ),
    "pairs": [
        ("Atom",
         "The smallest unit of an element that still has the properties of that element"),
        ("Element",
         "A pure substance made of only one kind of atom, such as carbon, nitrogen, or sulfur"),
        ("Glucose",
         "A sugar made of carbon, hydrogen, and oxygen that stores energy and supplies atoms for building other molecules"),
        ("Amino acid",
         "A building block of proteins that contains carbon, hydrogen, oxygen, and nitrogen"),
        ("Protein",
         "A large carbon-based molecule made of amino acids linked together in a specific order"),
        ("Photosynthesis",
         "The process that uses light energy to build sugar from carbon dioxide and water"),
    ],
    "distractors": [
        "A gas that plants release into the air during photosynthesis",
        "The energy stored in sunlight before it reaches a leaf",
    ],
}

# ---------------------------------------------------------------------------
# Part 2: Multiple choice (about 9 minutes). "answer" is the index of the key.
# ---------------------------------------------------------------------------
MULTIPLE_CHOICE = [
    {
        "title": "PMC 1 - Soybean root nodules",
        "dok": 2,
        "prompt": (
            "<p>Soybean plants can have small bumps on their roots called "
            "nodules. Bacteria living in the nodules take nitrogen from the "
            "air and give it to the plant. A farmer grows soybeans in "
            "nitrogen-poor soil. Plants <em>with</em> nodules produce beans "
            "high in protein. Plants <em>without</em> nodules photosynthesize "
            "normally but produce beans low in protein.</p>"
            "<p>Which explanation <strong>best</strong> accounts for this difference?</p>"
        ),
        "choices": [
            "The nodules supply nitrogen, which the plant combines with carbon, hydrogen, and oxygen from its sugar to build amino acids and proteins.",
            "The nodules supply extra sugar, so plants with nodules have more energy to do photosynthesis.",
            "The bacteria in the nodules make proteins and pass them directly into the beans, unchanged.",
            "Plants without nodules cannot make sugar, so they have no carbon for building proteins.",
        ],
        "answer": 0,
        "feedback": "Both groups made sugar (photosynthesis was normal). The nodules supply nitrogen, an element sugar doesn't have, so only plants with nodules could turn their sugar's atoms into lots of amino acids and proteins.",
    },
    {
        "title": "PMC 2 - Counting atoms in alanine",
        "dok": 2,
        "prompt": (
            "<p>A student compares two molecules found in a grass plant:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Molecule</th><th>C</th><th>H</th><th>O</th><th>N</th></tr>"
            "<tr><td>Glucose (a sugar)</td><td>6</td><td>12</td><td>6</td><td>0</td></tr>"
            "<tr><td>Alanine (an amino acid)</td><td>3</td><td>7</td><td>2</td><td>1</td></tr>"
            "</table>"
            "<p>Which conclusion is <strong>best supported</strong> by the table?</p>"
        ),
        "choices": [
            "The carbon, hydrogen, and oxygen in alanine can come from glucose, but the nitrogen must come from another source, such as the soil.",
            "Alanine is made by breaking glucose in half, since it has about half as many atoms.",
            "Glucose must contain hidden nitrogen atoms that are released when alanine is made.",
            "The plant can make alanine from glucose alone because both molecules contain carbon.",
        ],
        "answer": 0,
        "feedback": "Glucose supplies C, H, and O. It has zero nitrogen, and atoms cannot be created, so the nitrogen in alanine has to come from somewhere else, like nitrogen compounds in the soil.",
    },
    {
        "title": "PMC 3 - Wheat in sulfur-poor soil",
        "dok": 3,
        "prompt": (
            "<p>Two amino acids, cysteine and methionine, contain sulfur. The "
            "other amino acids a wheat plant makes do not. Scientists grow "
            "wheat in two fields that differ only in sulfur:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Field</th><th>Sugar in leaves</th><th>Amino acids without sulfur</th><th>Cysteine and methionine</th></tr>"
            "<tr><td>Normal sulfur</td><td>Normal</td><td>Normal</td><td>Normal</td></tr>"
            "<tr><td>Low sulfur</td><td>Normal</td><td>Normal</td><td>Very low</td></tr>"
            "</table>"
            "<p>Which explanation <strong>best</strong> fits all of the data?</p>"
        ),
        "choices": [
            "Sugar supplies the carbon, hydrogen, and oxygen for all amino acids, but cysteine and methionine also need sulfur from the soil, so only those two were limited.",
            "Low sulfur slowed photosynthesis, so the plants made less of every amino acid.",
            "Sulfur is the source of carbon for cysteine and methionine, so without sulfur there was no carbon to build them.",
            "The plants in low-sulfur soil turned some of their sugar into sulfur, which used up the sugar needed for amino acids.",
        ],
        "answer": 0,
        "feedback": "Sugar and the sulfur-free amino acids were normal, so photosynthesis and building from sugar still worked. Only the sulfur-containing amino acids dropped, because sulfur is an element sugar can't supply.",
    },
    {
        "title": "PMC 4 - Fish eating algae",
        "dok": 2,
        "prompt": (
            "<p>In a pond, small fish eat only algae. Algae carry out "
            "photosynthesis using carbon dioxide dissolved in the water.</p>"
            "<p>Which pathway <strong>best</strong> describes where the carbon "
            "atoms in the fish's muscle proteins came from?</p>"
        ),
        "choices": [
            "Carbon dioxide in the water &rarr; sugar made by algae &rarr; other molecules in the algae &rarr; eaten, broken down, and rebuilt into the fish's own proteins",
            "Water molecules &rarr; absorbed through the fish's gills &rarr; changed into carbon in the fish's muscle",
            "Sunlight &rarr; absorbed by the fish's scales &rarr; converted into carbon atoms in muscle protein",
            "Algae proteins &rarr; eaten by the fish &rarr; stored unchanged in the fish's muscles",
        ],
        "answer": 0,
        "feedback": "The carbon started as CO2, was built into sugar by the algae, then into other algae molecules. The fish broke those down and rearranged the atoms into its own proteins. Water has no carbon, light is energy (not matter), and proteins are not stored unchanged.",
    },
    {
        "title": "PMC 5 - Choosing evidence for a model",
        "dok": 3,
        "prompt": (
            "<p>Two students drew models of how a plant gets the materials to build protein:</p>"
            "<ul>"
            "<li><strong>Model X:</strong> Sunlight and soil &rarr; protein</li>"
            "<li><strong>Model Y:</strong> Carbon dioxide + water (using light energy) &rarr; sugar; "
            "sugar + nitrogen from soil &rarr; amino acids &rarr; protein</li>"
            "</ul>"
            "<p>Which piece of evidence would <strong>best</strong> support Model Y over Model X?</p>"
        ),
        "choices": [
            "When a plant is given carbon dioxide with labeled carbon, the labeled carbon shows up first in sugar and later in the plant's proteins.",
            "Plants grown in brighter light usually have greener leaves than plants grown in dim light.",
            "Plants absorb water and dissolved minerals from the soil through their roots.",
            "Proteins are found in many parts of a plant, including leaves, stems, and seeds.",
        ],
        "answer": 0,
        "feedback": "Only the tracer evidence shows the path of atoms: carbon from CO2 goes into sugar first and then into protein, which is what Model Y shows. The other choices are true, but they don't separate the two models.",
    },
    {
        "title": "PMC 6 - Seedlings in the dark and light",
        "dok": 3,
        "prompt": (
            "<p>Students sprout bean seeds. Half grow in the dark and half in "
            "the light. They measure the <em>dry mass</em> (mass without "
            "water) of each group:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Day</th><th>Dry mass, dark (g)</th><th>Dry mass, light (g)</th></tr>"
            "<tr><td>0</td><td>0.50</td><td>0.50</td></tr>"
            "<tr><td>7</td><td>0.42</td><td>0.45</td></tr>"
            "<tr><td>14</td><td>0.35</td><td>0.70</td></tr>"
            "</table>"
            "<p>Both groups grew new roots and stems with new proteins. Which "
            "explanation <strong>best</strong> fits the data?</p>"
        ),
        "choices": [
            "Seedlings in the dark could only rearrange atoms from molecules already stored in the seed, while seedlings in the light, once their leaves opened, also built new sugar from carbon dioxide and used it to make more molecules.",
            "Seedlings in the light gained mass because sunlight was turned directly into new plant matter.",
            "Seedlings in the dark lost mass because atoms in the seed were destroyed as they grew.",
            "Both groups should have gained the same mass because they received the same water, so the data must contain an error.",
        ],
        "answer": 0,
        "feedback": "Without light, the seedlings could only rebuild the matter stored in the seed, and some was used up for energy, so dry mass fell. After day 7 the light-grown seedlings made new sugar from CO2, adding new atoms they could build into other molecules, so dry mass rose.",
    },
]

# ---------------------------------------------------------------------------
# Part 3: Free response (about 8 minutes)
# ---------------------------------------------------------------------------
FREE_RESPONSE = [
    {
        "title": "PFR 1 - How much nitrogen for basil?",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>A student grows basil hydroponically with four different "
            "amounts of nitrogen. Everything else (light, water, CO<sub>2</sub>, "
            "temperature) is the same. After 4 weeks:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Nitrogen added (mg/L)</th><th>Protein in leaves (mg/g)</th><th>Sugar in leaves (mg/g)</th><th>Dry mass (g)</th></tr>"
            "<tr><td>0</td><td>6</td><td>30</td><td>2.0</td></tr>"
            "<tr><td>50</td><td>22</td><td>21</td><td>5.5</td></tr>"
            "<tr><td>100</td><td>35</td><td>14</td><td>8.2</td></tr>"
            "<tr><td>200</td><td>36</td><td>13</td><td>8.4</td></tr>"
            "</table>"
            "<p>Answer in a short paragraph:</p>"
            "<ol>"
            "<li>Use data to describe what happens to protein and sugar as nitrogen goes from 0 to 100 mg/L.</li>"
            "<li>Explain <strong>why</strong> the sugar goes down as protein goes up. Describe how the carbon, hydrogen, and oxygen from sugar combine with nitrogen.</li>"
            "<li>Doubling nitrogen from 100 to 200 mg/L barely changes anything. Suggest one reason why, using the idea that the plant needs <em>both</em> sugar and nitrogen.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Accurately describes both trends with data (for example, protein rises from 6 to 35 mg/g while sugar falls from 30 to 14 mg/g). "
             "Explains that atoms from sugar (C, H, O) are rearranged and combined with nitrogen to build amino acids and proteins, so sugar is used up as protein is made. "
             "Gives a reasonable explanation for the leveling off: sugar is now the limiting material (the plant is using nearly all it makes), so more nitrogen can't help without more sugar (for example, more light or CO2)."),
            (3, "Proficient",
             "Describes both trends with at least one accurate data pair. "
             "Links sugar and nitrogen to protein, but the explanation of atoms being combined or rearranged is brief. "
             "Gives a reason for the leveling off that mentions sugar or another limit, but doesn't fully connect it."),
            (2, "Developing",
             "Describes only one trend, or describes trends without data. "
             "States that nitrogen helps make protein but doesn't explain why sugar decreases. "
             "Leveling-off explanation is missing or unrelated (for example, \"the plant was full\")."),
            (1, "Beginning",
             "Data are missing or misread. Reasoning is missing or shows a major misconception (for example, nitrogen makes sugar, or nitrogen gives the plant energy)."),
        ],
        "grading_notes": [
            "Part 3 is the stretch. A response can earn a 3 with a partial leveling-off explanation if Parts 1 and 2 are strong.",
            "Accept any reasonable limit for Part 3 (sugar supply, light, or CO2), but a 4 needs the connection that protein needs both sugar and nitrogen.",
            "Common misconception: \"nitrogen turns into sugar\" or \"nitrogen gives energy.\" Nitrogen is a building material that sugar lacks.",
            "Don't take off points for leaving out chemical reaction details or names of macromolecule types. Both are outside the HS-LS1-6 assessment boundary.",
        ],
        "exemplar": (
            "As nitrogen increases from 0 to 100 mg/L, protein goes up from 6 to 35 mg/g, but sugar goes down from 30 to 14 mg/g. "
            "Sugar goes down because the plant uses it to build protein. Sugar only has carbon, hydrogen, and oxygen, so the plant rearranges those atoms and combines them with nitrogen to make amino acids, which link into proteins. "
            "More nitrogen means more sugar gets turned into protein. From 100 to 200 mg/L almost nothing changes because the plant is already using almost all of its sugar. "
            "Now sugar is the limit, not nitrogen, so the plant would need more light or CO2 to make more sugar before extra nitrogen could help."
        ),
    },
]
