"""Question bank for the HS-LS2-2 CSA: Patterns in Populations (unit 4.2).

45-minute test, 30 points. Edit, then run `python3 ../build_unit.py HS-LS2-2`.
Boundary: provided data only.
"""

TITLE = "HS-LS2-2 Assessment: Patterns in Populations"
STANDARD = "HS-LS2-2"
QUIZ_ID = "hs_ls2_2_patterns_in_populations"
FILE_PREFIX = "HS-LS2-2"
MAX_ATTEMPTS = 1
TIME_MINUTES = 45
KEY_POSITIONS = [0, 2, 3, 1, 2, 0, 3, 1]

DESCRIPTION = (
    "<p><strong>Living Earth (Biology) &ndash; HS-LS2-2</strong></p>"
    "<p>Use mathematical representations to support and revise explanations based on evidence about "
    "factors affecting biodiversity and populations in ecosystems of different scales.</p>"
    "<p>Part 1: Vocabulary matching &middot; Part 2: Multiple choice &middot; Part 3: Free response</p>"
)

MATCHING = {
    "title": "Part 1: Vocabulary Matching",
    "points": 6,
    "prompt": "<p>Match each term with its best definition. Some definitions will not be used.</p>",
    "pairs": [
        ("Population", "All the individuals of one species living in the same area at the same time"),
        ("Biodiversity", "The variety of different species in an ecosystem"),
        ("Limiting factor", "A resource or condition that keeps a population from growing larger"),
        ("Mean (average)", "The sum of all the values divided by how many values there are"),
        ("Rate of change", "How much a quantity changes per unit of time"),
        ("Trend", "The general direction that data move over time, such as rising, falling, or staying level"),
    ],
    "distractors": [
        "The largest population an environment can support for a long time",
        "A nonliving part of an environment, such as temperature or water",
    ],
}

MULTIPLE_CHOICE = [
    {
        "title": "MC 1 - Comparing two forests",
        "dok": 2,
        "prompt": (
            "<p>Scientists count the number of species in two forests that are the same size:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Forest</th><th>Number of tree species</th><th>Number of individual trees</th></tr>"
            "<tr><td>North</td><td>12</td><td>1,000</td></tr>"
            "<tr><td>South</td><td>45</td><td>1,000</td></tr>"
            "</table>"
            "<p>Which statement is <strong>best supported</strong> by the data?</p>"
        ),
        "choices": [
            "The South forest has higher biodiversity because it has more species, even though both forests have the same number of trees.",
            "The North forest has higher biodiversity because its trees are larger.",
            "Both forests have the same biodiversity because they have the same number of trees.",
            "The South forest has fewer species than the North forest.",
        ],
        "answer": 0,
        "feedback": "Biodiversity is the variety of species. The South forest has more species with the same number of individuals.",
    },
    {
        "title": "MC 2 - A deer population",
        "dok": 2,
        "prompt": (
            "<p>A wildlife agency counts the deer in a park each year:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Year</th><th>2019</th><th>2020</th><th>2021</th><th>2022</th><th>2023</th></tr>"
            "<tr><td>Deer</td><td>420</td><td>380</td><td>340</td><td>300</td><td>260</td></tr>"
            "</table>"
            "<p>Which statement <strong>best</strong> describes the trend?</p>"
        ),
        "choices": [
            "The deer population decreased steadily by about 40 deer each year.",
            "The deer population increased steadily by about 40 deer each year.",
            "The deer population stayed the same.",
            "The deer population increased, then decreased.",
        ],
        "answer": 0,
        "feedback": "Each year the count dropped by 40 (420 to 380 to 340 to 300 to 260), a steady decrease.",
    },
    {
        "title": "MC 3 - Finding the mean",
        "dok": 2,
        "prompt": (
            "<p>A student counts the frogs in a pond on five evenings: 14, 18, 15, 20, and 18.</p>"
            "<p>What is the <strong>mean</strong> number of frogs per evening?</p>"
        ),
        "choices": [
            "17",
            "15",
            "20",
            "85",
        ],
        "answer": 0,
        "feedback": "14 + 18 + 15 + 20 + 18 = 85, and 85 &divide; 5 = 17.",
    },
    {
        "title": "MC 4 - Which grows faster?",
        "dok": 2,
        "prompt": (
            "<p>Two fish populations are measured over 4 years:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Population</th><th>Start</th><th>After 4 years</th></tr>"
            "<tr><td>Lake A trout</td><td>200</td><td>280</td></tr>"
            "<tr><td>Lake B trout</td><td>1,000</td><td>1,060</td></tr>"
            "</table>"
            "<p>Which statement <strong>correctly</strong> compares the rates of change?</p>"
        ),
        "choices": [
            "Lake A grew by 20 fish per year and Lake B grew by 15 fish per year, so Lake A grew faster.",
            "Lake B grew faster because it ended with more fish.",
            "Both grew at the same rate.",
            "Lake A grew by 80 fish per year and Lake B by 60 fish per year.",
        ],
        "answer": 0,
        "feedback": "Lake A: (280 - 200) / 4 = 20 per year. Lake B: (1,060 - 1,000) / 4 = 15 per year.",
    },
    {
        "title": "MC 5 - Ecosystems of different sizes",
        "dok": 3,
        "prompt": (
            "<p>Scientists compare two ecosystems of different sizes:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Ecosystem</th><th>Area (km<sup>2</sup>)</th><th>Number of species</th></tr>"
            "<tr><td>Small pond</td><td>0.5</td><td>40</td></tr>"
            "<tr><td>Large lake</td><td>5</td><td>90</td></tr>"
            "</table>"
            "<p>Which statement <strong>best</strong> uses math to compare the biodiversity of the two ecosystems?</p>"
        ),
        "choices": [
            "The pond has about 80 species per km&sup2; and the lake has about 18 species per km&sup2;, so the pond has more species for its size, even though the lake has more species in total.",
            "The lake is more diverse for every measure because it has 90 species.",
            "The pond is less diverse because it is smaller.",
            "Area has nothing to do with comparing biodiversity.",
        ],
        "answer": 0,
        "feedback": "40 / 0.5 = 80 species per km&sup2; 90 / 5 = 18 species per km&sup2;. Dividing by area makes ecosystems of different sizes comparable.",
    },
    {
        "title": "MC 6 - Fertilizer runoff",
        "dok": 3,
        "prompt": (
            "<p>Scientists measure the phosphorus from farm runoff and the number of fish species in four lakes of similar size:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Lake</th><th>W</th><th>X</th><th>Y</th><th>Z</th></tr>"
            "<tr><td>Phosphorus (parts per billion)</td><td>5</td><td>10</td><td>20</td><td>40</td></tr>"
            "<tr><td>Fish species</td><td>22</td><td>18</td><td>11</td><td>5</td></tr>"
            "</table>"
            "<p>Which conclusion is <strong>best supported</strong> by the data?</p>"
        ),
        "choices": [
            "Fish biodiversity decreased as phosphorus increased, from 22 species at 5 ppb to 5 species at 40 ppb.",
            "Fish biodiversity increased as phosphorus increased.",
            "Phosphorus had no connection to the number of fish species.",
            "Lake Z had the highest biodiversity.",
        ],
        "answer": 0,
        "feedback": "As phosphorus rose from 5 to 40 ppb, species fell from 22 to 5, a negative trend.",
    },
    {
        "title": "MC 7 - New data change the story",
        "dok": 3,
        "prompt": (
            "<p>A student claims, &ldquo;Frogs are disappearing because of the noise from a new road.&rdquo; "
            "New data are collected from 20 ponds:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Pond group</th><th>Road nearby?</th><th>Pesticide runoff?</th><th>Change in frog population</th></tr>"
            "<tr><td>5 ponds</td><td>Yes</td><td>No</td><td>-3%</td></tr>"
            "<tr><td>5 ponds</td><td>Yes</td><td>Yes</td><td>-62%</td></tr>"
            "<tr><td>5 ponds</td><td>No</td><td>Yes</td><td>-58%</td></tr>"
            "<tr><td>5 ponds</td><td>No</td><td>No</td><td>+1%</td></tr>"
            "</table>"
            "<p>Which revision of the explanation is <strong>best supported</strong>?</p>"
        ),
        "choices": [
            "Frog populations dropped by about 60% in ponds with pesticide runoff whether or not a road was nearby, so pesticide runoff, not road noise, is the main factor.",
            "Road noise alone causes a 62% drop in frogs.",
            "Neither the road nor pesticide runoff affects frogs.",
            "The road and pesticides both cause exactly the same drop in frogs.",
        ],
        "answer": 0,
        "feedback": "Ponds with a road but no pesticides barely changed (-3%), while ponds with pesticides dropped 58% to 62% with or without a road.",
    },
    {
        "title": "MC 8 - Is the growth really steady?",
        "dok": 3,
        "prompt": (
            "<p>A student reads this table of a growing population and says, &ldquo;The population is growing steadily because it increases every year.&rdquo;</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Year</th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th></tr>"
            "<tr><td>Population</td><td>100</td><td>180</td><td>240</td><td>280</td><td>300</td></tr>"
            "</table>"
            "<p>Which revision <strong>best</strong> uses the rate of change?</p>"
        ),
        "choices": [
            "The population is always increasing, but the yearly increase is getting smaller (+80, +60, +40, +20), so growth is slowing.",
            "The population increases by the same amount each year.",
            "The population is decreasing because the numbers are getting closer together.",
            "The population is increasing faster each year.",
        ],
        "answer": 0,
        "feedback": "The yearly changes are 80, 60, 40, and 20, so the population grows, but more slowly each year.",
    },
]

FREE_RESPONSE = [
    {
        "title": "FR 1 - Rats on islands",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>Scientists count the bird species on four islands. Two islands have invasive rats that eat bird eggs; two do not.</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Island</th><th>Area (km<sup>2</sup>)</th><th>Rats present?</th><th>Bird species</th></tr>"
            "<tr><td>A</td><td>2</td><td>No</td><td>24</td></tr>"
            "<tr><td>B</td><td>10</td><td>No</td><td>60</td></tr>"
            "<tr><td>C</td><td>2</td><td>Yes</td><td>9</td></tr>"
            "<tr><td>D</td><td>10</td><td>Yes</td><td>28</td></tr>"
            "</table>"
            "<p>Write an explanation using <strong>Claim, Evidence, and Reasoning</strong>:</p>"
            "<ol>"
            "<li><strong>Claim:</strong> Explain how the presence of rats affects bird biodiversity.</li>"
            "<li><strong>Evidence:</strong> Calculate the number of species per km<sup>2</sup> for <strong>all four</strong> islands (show your work) and compare islands of the same size.</li>"
            "<li><strong>Reasoning:</strong> Explain why dividing by area is needed to compare islands of different sizes, and give one reason that rats reduce the number of bird species.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Claim that rats reduce bird biodiversity. All four calculations correct and shown (A: 12, B: 6, C: 4.5, D: 2.8 species per km&sup2;). "
             "Compares same-sized islands (A with C, and B with D) and states the size of the difference (about 60% fewer species per km&sup2; with rats). "
             "Explains that dividing by area makes different-sized islands comparable, and gives a plausible mechanism (rats eat eggs, so fewer birds survive and some species disappear)."),
            (3, "Proficient",
             "Claim and at least three correct calculations. Compares same-sized islands. Reasoning is correct but the mechanism or the purpose of dividing by area is brief."),
            (2, "Developing",
             "Claim is partly correct. One or two calculations, or errors in calculations. Compares totals without area or gives a vague reason."),
            (1, "Beginning",
             "Claim wrong or missing. No usable calculations. Shows a major misconception."),
        ],
        "grading_notes": [
            "Correct values: A = 24 / 2 = 12; B = 60 / 10 = 6; C = 9 / 2 = 4.5; D = 28 / 10 = 2.8 species per km&sup2;.",
            "Same-sized comparisons: A to C (12 vs. 4.5) and B to D (6 vs. 2.8). Rats lower the value by roughly 60% in both cases.",
            "Accept any plausible mechanism: rats eat eggs and chicks, birds cannot reproduce, species die out.",
            "Using only the provided data is the assessment boundary. Do not require anything beyond it.",
        ],
        "exemplar": (
            "Rats reduce bird biodiversity. The islands have different areas, so I divided species by area: A has 24 / 2 = 12 species per km&sup2;, B has 60 / 10 = 6, C has 9 / 2 = 4.5, and D has 28 / 10 = 2.8. "
            "Island C has rats and A does not, and both are 2 km&sup2;, so the rats lowered the value from 12 to 4.5. Island D has rats and B does not, and both are 10 km&sup2;, so the value dropped from 6 to 2.8. In both pairs rats cut biodiversity by about 60%. "
            "Dividing by area makes islands of different sizes fair to compare, because a larger island is expected to hold more species just because it is bigger. "
            "Rats eat bird eggs and chicks, so fewer young birds survive, and some species cannot reproduce enough to stay on the island."
        ),
    },
    {
        "title": "FR 2 - Kelp, otters, and urchins",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>A student reads a report about a coastal kelp forest and writes this explanation: &ldquo;The kelp forest is growing because the ocean is getting colder.&rdquo; "
            "The first data set seems to support her:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Year</th><th>2000</th><th>2005</th><th>2010</th><th>2015</th></tr>"
            "<tr><td>Kelp forest area (km<sup>2</sup>)</td><td>10</td><td>15</td><td>28</td><td>40</td></tr>"
            "<tr><td>Water temperature (&deg;C)</td><td>15.0</td><td>14.9</td><td>14.8</td><td>14.8</td></tr>"
            "</table>"
            "<p>Then the student finds new data from the same coast:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Year</th><th>2000</th><th>2005</th><th>2010</th><th>2015</th></tr>"
            "<tr><td>Sea otters (number)</td><td>50</td><td>120</td><td>300</td><td>520</td></tr>"
            "<tr><td>Sea urchins (per m<sup>2</sup>; they eat kelp)</td><td>60</td><td>42</td><td>15</td><td>4</td></tr>"
            "</table>"
            "<ol>"
            "<li><strong>Evaluate</strong> the student's first explanation by calculating the average rate of change of kelp area and of temperature from 2000 to 2015.</li>"
            "<li><strong>Revise</strong> the explanation using the new data. Include one calculation from the new data.</li>"
            "<li><strong>Predict</strong> what would happen to the kelp forest if the number of sea otters fell sharply, and explain why.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Correct rates: kelp (40 - 10) / 15 = +2 km&sup2; per year; temperature (14.8 - 15.0) / 15 = about -0.013 &deg;C per year, so the temperature barely changed and cannot explain a fourfold increase in kelp. "
             "Revision uses the new data: otters rose and urchins (which eat kelp) fell, so kelp recovered; includes a correct calculation (for example, urchins dropped from 60 to 4 per m&sup2;, about 93% fewer; otters rose about 10 times). "
             "Prediction: fewer otters would let urchins increase and eat more kelp, so the kelp forest would shrink."),
            (3, "Proficient",
             "Correct rate calculations and a revision supported by new data. The calculation from the new data is correct, but the prediction is brief."),
            (2, "Developing",
             "One rate correct or both partly correct. Revision names otters or urchins without using numbers. Prediction vague."),
            (1, "Beginning",
             "No usable calculations, or the explanation is not revised. Shows a major misconception."),
        ],
        "grading_notes": [
            "Kelp: (40 - 10) / 15 = 2 km&sup2; per year. Temperature: (14.8 - 15.0) / 15 = about -0.013 &deg;C per year (a very small change).",
            "Accept any valid calculation from the new data: urchins fell by 56 per m&sup2; (about 93%); otters rose by 470 (about ten-fold).",
            "The intended chain: otters eat urchins, urchins eat kelp, so more otters leads to fewer urchins and more kelp.",
            "Using only the provided data is the assessment boundary.",
        ],
        "exemplar": (
            "The kelp forest area grew at an average of (40 - 10) / 15 = 2 km&sup2; per year, while the water temperature changed by only (14.8 - 15.0) / 15 = about -0.01 &deg;C per year. "
            "The temperature barely changed, so it cannot explain a four-fold increase in kelp. "
            "The new data suggest a better explanation: the number of sea otters rose from 50 to 520 while the urchins that eat kelp dropped from 60 to 4 per m&sup2;, about 93% fewer, so otters eating urchins protected the kelp, and the kelp forest grew. "
            "If the sea otters fell sharply, the urchin numbers would rise and eat more kelp, so the kelp forest would shrink."
        ),
    },
]
