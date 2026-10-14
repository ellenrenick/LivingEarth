"""Question bank for the HS-LS2-4 CSA: Cycles of Life (unit 4.1).

45-minute test, 30 points. Edit, then run `python3 ../build_unit.py HS-LS2-4`.
Boundary: proportional reasoning only to describe the cycling of matter and flow of energy.
"""

TITLE = "HS-LS2-4 Assessment: Cycles of Life"
STANDARD = "HS-LS2-4"
QUIZ_ID = "hs_ls2_4_cycles_of_life"
FILE_PREFIX = "HS-LS2-4"
MAX_ATTEMPTS = 1
TIME_MINUTES = 45
KEY_POSITIONS = [1, 3, 0, 2, 3, 0, 2, 1]

DESCRIPTION = (
    "<p><strong>Living Earth (Biology) &ndash; HS-LS2-4</strong></p>"
    "<p>Use mathematical representations to support claims for the cycling of matter and flow of "
    "energy among organisms in an ecosystem.</p>"
    "<p>Part 1: Vocabulary matching &middot; Part 2: Multiple choice &middot; Part 3: Free response</p>"
)

MATCHING = {
    "title": "Part 1: Vocabulary Matching",
    "points": 6,
    "prompt": "<p>Match each term with its best definition. Some definitions will not be used.</p>",
    "pairs": [
        ("Producer", "An organism that makes its own food from sunlight or chemicals, such as a plant or alga"),
        ("Consumer", "An organism that gets energy by eating other organisms"),
        ("Decomposer", "An organism that breaks down dead organisms and wastes and returns matter to the environment"),
        ("Trophic level", "A feeding level in a food chain or food web"),
        ("Biomass", "The total mass of living material, or the energy stored in it, at a trophic level"),
        ("Food web", "A diagram of the many feeding connections among organisms in an ecosystem"),
    ],
    "distractors": [
        "The number of different species in an ecosystem",
        "The nonliving parts of an environment, such as temperature and water",
    ],
}

MULTIPLE_CHOICE = [
    {
        "title": "MC 1 - Mushrooms on a log",
        "dok": 2,
        "prompt": (
            "<p>A fallen log in a forest is covered with mushrooms. Over several years the log crumbles into soil, and nearby trees grow faster.</p>"
            "<p>Which statement <strong>best</strong> describes the role of the mushrooms?</p>"
        ),
        "choices": [
            "They are decomposers that break down the dead wood and return matter to the soil, where producers can use it again.",
            "They are producers that make the log from sunlight.",
            "They are consumers that destroy the matter in the log.",
            "They are producers that give the trees energy from the Sun.",
        ],
        "answer": 0,
        "feedback": "Decomposers break down dead organisms and return matter to the environment so it can cycle.",
    },
    {
        "title": "MC 2 - Cycle or flow?",
        "dok": 2,
        "prompt": (
            "<p>A student says, &ldquo;In an ecosystem, matter and energy both cycle around in circles.&rdquo;</p>"
            "<p>Which revision is <strong>most accurate</strong>?</p>"
        ),
        "choices": [
            "Matter, such as carbon, is reused and cycles through the ecosystem, but energy flows one way: it comes in as sunlight and leaves as heat.",
            "Energy cycles and matter flows in one direction.",
            "Neither matter nor energy moves through an ecosystem.",
            "Both matter and energy leave the Earth at every trophic level.",
        ],
        "answer": 0,
        "feedback": "Atoms are conserved and reused. Energy is transferred and eventually lost as heat, so ecosystems need a constant supply of new energy from the Sun.",
    },
    {
        "title": "MC 3 - Reading an energy pyramid",
        "dok": 2,
        "prompt": (
            "<p>An energy pyramid for a grassland shows the energy stored in each trophic level in one year:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Trophic level</th><th>Energy stored (kJ per year)</th></tr>"
            "<tr><td>Producers (grass)</td><td>10,000</td></tr>"
            "<tr><td>Primary consumers (grasshoppers)</td><td>1,000</td></tr>"
            "<tr><td>Secondary consumers (frogs)</td><td>100</td></tr>"
            "<tr><td>Tertiary consumers (snakes)</td><td>10</td></tr>"
            "</table>"
            "<p>Which statement is <strong>best supported</strong> by the pyramid?</p>"
        ),
        "choices": [
            "About 10% of the energy at each level is stored in the next level; most of the rest is used by the organisms or lost as heat.",
            "About 90% of the energy at each level is passed to the next level.",
            "All the energy at each level is passed up unchanged.",
            "The snakes receive more energy than the grasshoppers.",
        ],
        "answer": 0,
        "feedback": "1,000 out of 10,000, 100 out of 1,000, and 10 out of 100 are each 10%. The rest powers life processes or is lost as heat.",
    },
    {
        "title": "MC 4 - Applying the 10% rule",
        "dok": 2,
        "prompt": (
            "<p>A meadow's grass stores 50,000 kcal of energy in a year. The food chain is: grass &rarr; grasshopper &rarr; frog &rarr; snake. "
            "Assume about 10% of the energy at each level is stored in the next.</p>"
            "<p>About how much energy is stored in the <strong>snake</strong> level?</p>"
        ),
        "choices": [
            "About 50 kcal",
            "About 500 kcal",
            "About 5,000 kcal",
            "About 5 kcal",
        ],
        "answer": 0,
        "feedback": "50,000 &times; 0.10 = 5,000 (grasshoppers); &times; 0.10 = 500 (frogs); &times; 0.10 = 50 (snakes).",
    },
    {
        "title": "MC 5 - Real data vs. the 10% rule",
        "dok": 3,
        "prompt": (
            "<p>Scientists measure the energy stored in each trophic level of a lake in one year:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Trophic level</th><th>Energy stored (kJ)</th></tr>"
            "<tr><td>Producers</td><td>8,000</td></tr>"
            "<tr><td>Primary consumers</td><td>900</td></tr>"
            "<tr><td>Secondary consumers</td><td>85</td></tr>"
            "<tr><td>Tertiary consumers</td><td>7</td></tr>"
            "</table>"
            "<p>Which statement <strong>best</strong> uses the data?</p>"
        ),
        "choices": [
            "The energy passed to each level is roughly 8% to 11% of the level below, which is close to the 10% rule, so most energy is not passed on and few levels can be supported.",
            "The energy passed on at each level is exactly 10% every time.",
            "Tertiary consumers store more energy than producers.",
            "The data show energy is created at each level.",
        ],
        "answer": 0,
        "feedback": "900 / 8,000 is about 11%, 85 / 900 about 9%, and 7 / 85 about 8%. Real ecosystems pass on roughly 10%, not exactly 10%.",
    },
    {
        "title": "MC 6 - Counting carbon",
        "dok": 3,
        "prompt": (
            "<p>Scientists track carbon (in units) in a closed ecosystem across one year:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Where the carbon is</th><th>Start of year</th><th>End of year</th></tr>"
            "<tr><td>Air</td><td>3,000</td><td>2,900</td></tr>"
            "<tr><td>Producers</td><td>1,500</td><td>1,560</td></tr>"
            "<tr><td>Consumers</td><td>100</td><td>110</td></tr>"
            "<tr><td>Soil and decomposers</td><td>400</td><td>430</td></tr>"
            "</table>"
            "<p>Which statement <strong>best</strong> uses the numbers to support a claim about matter?</p>"
        ),
        "choices": [
            "The total is 5,000 units at the start and at the end, which supports the claim that carbon is conserved as it moves among the air, organisms, and soil.",
            "The total went down, which shows carbon was destroyed.",
            "The air gained carbon, which shows carbon was created by producers.",
            "The producers lost carbon, which shows they stopped growing.",
        ],
        "answer": 0,
        "feedback": "3,000 + 1,500 + 100 + 400 = 5,000 and 2,900 + 1,560 + 110 + 430 = 5,000. Carbon moved from the air into organisms and soil, but the total stayed the same.",
    },
    {
        "title": "MC 7 - Do decomposers recycle energy?",
        "dok": 2,
        "prompt": (
            "<p>A student claims, &ldquo;Decomposers recycle energy back to the producers, so an ecosystem does not need the Sun.&rdquo;</p>"
            "<p>Which statement <strong>best</strong> evaluates the claim?</p>"
        ),
        "choices": [
            "The claim is not correct: decomposers return matter to the soil, but energy is lost as heat at every level, so producers need new energy from the Sun.",
            "The claim is correct: energy can be recycled forever.",
            "The claim is correct: producers get their energy from decomposers.",
            "The claim is not correct because decomposers do not exist.",
        ],
        "answer": 0,
        "feedback": "Matter is recycled, but energy is not. It is lost as heat, so ecosystems need a constant source of energy.",
    },
    {
        "title": "MC 8 - How many hawks can the meadow support?",
        "dok": 3,
        "prompt": (
            "<p>A meadow's producers store 200,000 kJ per year. The food chain is: producers &rarr; mice &rarr; snakes &rarr; hawks. "
            "About 10% of the energy at each level is stored in the next level. One hawk needs about 40 kJ of stored energy per year from this food chain.</p>"
            "<p>About how many hawks can the meadow support, and why?</p>"
        ),
        "choices": [
            "About 5 hawks, because the hawk level stores about 200 kJ (200,000 &times; 0.1 &times; 0.1 &times; 0.1), and 200 &divide; 40 = 5.",
            "About 500 hawks, because the hawk level stores 20,000 kJ.",
            "About 50 hawks, because the hawk level stores 2,000 kJ.",
            "About 5,000 hawks, because hawks eat producers directly.",
        ],
        "answer": 0,
        "feedback": "200,000 kJ becomes 20,000 (mice), 2,000 (snakes), and 200 (hawks). Dividing 200 by 40 kJ per hawk gives about 5 hawks.",
    },
]

FREE_RESPONSE = [
    {
        "title": "FR 1 - Energy in a pond",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>Scientists measure the energy stored in each trophic level of a pond in one year:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Trophic level</th><th>Energy stored (kJ per year)</th></tr>"
            "<tr><td>Producers (algae and plants)</td><td>20,000</td></tr>"
            "<tr><td>Primary consumers (insects, snails)</td><td>2,200</td></tr>"
            "<tr><td>Secondary consumers (small fish)</td><td>190</td></tr>"
            "<tr><td>Tertiary consumers (large fish)</td><td>21</td></tr>"
            "</table>"
            "<p>Write an explanation using <strong>Claim, Evidence, and Reasoning</strong>:</p>"
            "<ol>"
            "<li><strong>Claim:</strong> Make a claim about how energy moves through the pond's trophic levels.</li>"
            "<li><strong>Evidence:</strong> Calculate the percent of energy passed from <strong>at least two</strong> levels to the next (show your work), and use your results.</li>"
            "<li><strong>Reasoning:</strong> Explain where the rest of the energy goes, why a pond cannot support many levels of consumers, and how this is different from the way matter moves in the pond.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Claim that only a small fraction of energy (about 10%) passes to each next level, so energy decreases at higher levels. "
             "At least two correct calculations shown (2,200 / 20,000 = 11%; 190 / 2,200 = about 9%; 21 / 190 = about 11%). "
             "Explains that the rest is used for life processes and lost as heat, so there is too little energy to support many levels. "
             "Contrasts energy (flows one way and is lost as heat) with matter (cycled by decomposers and reused)."),
            (3, "Proficient",
             "Correct claim and two correct calculations. Explains where the energy goes and why levels are limited, but the contrast with matter is brief or missing."),
            (2, "Developing",
             "Claim is partly correct. One calculation, or calculations with errors. Reasoning is vague about where the energy goes."),
            (1, "Beginning",
             "Claim wrong or missing. No usable calculations. Shows a major misconception (for example, all the energy is passed on)."),
        ],
        "grading_notes": [
            "Correct values: 2,200/20,000 = 11%; 190/2,200 = about 8.6% (accept 9%); 21/190 = about 11%.",
            "Look for: used for life processes (movement, growth, keeping warm), lost as heat, not all of an organism is eaten.",
            "Matter contrast: atoms such as carbon are reused and cycled by decomposers, but energy is not recycled.",
            "Do not require anything beyond proportional reasoning; it is the assessment boundary.",
        ],
        "exemplar": (
            "Only about 10% of the energy at each level of the pond is passed on to the next level, so the energy available decreases quickly at higher levels. "
            "From producers to primary consumers, 2,200 / 20,000 = 11%, and from secondary to tertiary consumers, 21 / 190 = about 11%; the step between primary and secondary consumers is 190 / 2,200 = about 9%. "
            "The rest of the energy at each level is used by the organisms for life processes such as moving and growing, and is lost as heat, so by the fourth level there is very little left, which limits the number of levels a pond can support. "
            "Matter is different: the atoms in dead organisms are broken down by decomposers and returned to the water and soil, where producers use them again, so matter cycles while energy flows through and is lost."
        ),
    },
    {
        "title": "FR 2 - A sealed ecosystem",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>A class builds a sealed jar ecosystem with water, algae, snails, and bacteria in the mud. The jar sits in a sunny window. "
            "They estimate the carbon (in units) in each part at the start and after 30 days:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Where the carbon is</th><th>Day 0</th><th>Day 30</th></tr>"
            "<tr><td>Carbon dioxide in the water and air in the jar</td><td>60</td><td>48</td></tr>"
            "<tr><td>Algae (producers)</td><td>25</td><td>33</td></tr>"
            "<tr><td>Snails (consumers)</td><td>5</td><td>6</td></tr>"
            "<tr><td>Bacteria and mud (decomposers and dead matter)</td><td>10</td><td>13</td></tr>"
            "</table>"
            "<ol>"
            "<li><strong>Calculate</strong> the total carbon at day 0 and day 30 and state what the totals show about matter.</li>"
            "<li><strong>Explain</strong> the role of the producers, consumers, and decomposers in moving the carbon.</li>"
            "<li><strong>Predict</strong> what would happen to the ecosystem if the jar were moved to a dark closet for several weeks, and explain using the ideas of matter and energy.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Correct totals (100 and 100) and states that matter is conserved: the carbon moved among parts but the total did not change. "
             "Explains correctly that producers take carbon dioxide into their bodies, consumers eat producers, and decomposers break down dead matter and return carbon to the cycle. "
             "Predicts that producers would stop growing and the ecosystem would fail, because without light there is no new energy entering, although the matter in the jar would still be there."),
            (3, "Proficient",
             "Correct totals and conclusion. Roles are correct but one is thin. Prediction is correct but the matter-versus-energy link is brief."),
            (2, "Developing",
             "One total is miscalculated, or the conclusion is vague. Roles are incomplete. Prediction is vague."),
            (1, "Beginning",
             "No usable calculation, or concludes that matter is lost or created. Shows a major misconception."),
        ],
        "grading_notes": [
            "Totals: day 0 is 60 + 25 + 5 + 10 = 100; day 30 is 48 + 33 + 6 + 13 = 100.",
            "The conclusion should say the total did not change, so matter (carbon) is conserved and cycles within the jar.",
            "Prediction: producers can no longer capture energy from light, so the food web has no energy source; matter is not lost, but the flow of energy needed to run the cycle stops.",
            "Do not require anything beyond proportional reasoning; it is the assessment boundary.",
        ],
        "exemplar": (
            "The total carbon is 60 + 25 + 5 + 10 = 100 units on day 0 and 48 + 33 + 6 + 13 = 100 units on day 30. The total did not change, so matter is conserved: the carbon moved from the air and water into the algae, snails, and mud, but none was lost or created. "
            "The algae are producers that take in carbon dioxide and use light to build their bodies. The snails are consumers that eat algae. The bacteria are decomposers that break down dead matter and return carbon to the water so it can be used again. "
            "If the jar were moved to a dark closet, the algae could not capture energy, so they would stop growing and the other organisms would run out of food, and the ecosystem would fail. The carbon would still be in the jar, but energy has to keep flowing in from light to power the cycle."
        ),
    },
]
