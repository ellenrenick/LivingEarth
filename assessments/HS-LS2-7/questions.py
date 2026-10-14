"""Question bank for the HS-LS2-7 CSA: Solutions for Sustainability (unit 4.4).

45-minute test, 30 points. Edit, then run `python3 ../build_unit.py HS-LS2-7`.
CSA items stop at DOK 3 (the department rates LS2-7.4 and LS2-7.5 at DOK 4).
"""

TITLE = "HS-LS2-7 Assessment: Solutions for Sustainability"
STANDARD = "HS-LS2-7"
QUIZ_ID = "hs_ls2_7_solutions_for_sustainability"
FILE_PREFIX = "HS-LS2-7"
MAX_ATTEMPTS = 1
TIME_MINUTES = 45
KEY_POSITIONS = [1, 3, 0, 2, 3, 0, 2, 1]

DESCRIPTION = (
    "<p><strong>Living Earth (Biology) &ndash; HS-LS2-7</strong></p>"
    "<p>Design, evaluate, and refine a solution for reducing the impacts of human activities on the "
    "environment and biodiversity.</p>"
    "<p>Part 1: Vocabulary matching &middot; Part 2: Multiple choice &middot; Part 3: Free response</p>"
)

MATCHING = {
    "title": "Part 1: Vocabulary Matching",
    "points": 6,
    "prompt": "<p>Match each term with its best definition. Some definitions will not be used.</p>",
    "pairs": [
        ("Deforestation", "The clearing of large areas of forest, often for farming, building, or lumber"),
        ("Pollution", "A harmful substance added to air, water, or soil"),
        ("Invasive species", "A species brought into an area where it did not live before and that harms the ecosystem"),
        ("Criteria", "The goals a solution must meet to be successful"),
        ("Constraints", "The limits a solution must stay within, such as cost, time, or materials"),
        ("Trade-off", "Giving up some of one benefit to gain another when comparing solutions"),
    ],
    "distractors": [
        "The variety of different species in an ecosystem",
        "The largest population an environment can support",
    ],
}

MULTIPLE_CHOICE = [
    {
        "title": "MC 1 - Forest loss and birds",
        "dok": 2,
        "prompt": (
            "<p>Scientists compare four regions of a rainforest with different amounts of forest left:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Region</th><th>W</th><th>X</th><th>Y</th><th>Z</th></tr>"
            "<tr><td>Forest remaining (%)</td><td>100</td><td>70</td><td>40</td><td>20</td></tr>"
            "<tr><td>Bird species</td><td>80</td><td>62</td><td>35</td><td>15</td></tr>"
            "</table>"
            "<p>Which statement <strong>best</strong> explains how human activity affects biodiversity?</p>"
        ),
        "choices": [
            "As people clear more forest, habitat is lost, and fewer bird species can survive, so biodiversity decreases.",
            "Clearing forest increases bird species because more land is open.",
            "Forest loss has no effect on the number of bird species.",
            "Bird species decrease only because birds migrate for fun.",
        ],
        "answer": 0,
        "feedback": "As forest remaining fell from 100% to 20%, species fell from 80 to 15, showing habitat loss reduces biodiversity.",
    },
    {
        "title": "MC 2 - Fertilizer and a dead zone",
        "dok": 2,
        "prompt": (
            "<p>Farms along a river use a lot of fertilizer. Rain washes extra fertilizer into the river and out to a bay. "
            "Algae in the bay grow very fast, then die and are broken down by bacteria that use up the oxygen in the water. Fish and crabs leave or die.</p>"
            "<p>Which sequence <strong>best</strong> shows how a human activity harmed the ecosystem?</p>"
        ),
        "choices": [
            "Fertilizer runoff &rarr; extra nutrients in the water &rarr; algae growth &rarr; low oxygen &rarr; fish and crabs die",
            "Fewer fish &rarr; more algae &rarr; more fertilizer",
            "Less oxygen &rarr; fertilizer runoff &rarr; farms",
            "Algae growth &rarr; fertilizer made &rarr; farms stop",
        ],
        "answer": 0,
        "feedback": "The extra nutrients from fertilizer set off a chain of events that removed oxygen and harmed animals.",
    },
    {
        "title": "MC 3 - A dam on a river",
        "dok": 2,
        "prompt": (
            "<p>Salmon swim from the ocean up a river to lay eggs. A dam is built across the river with no fish passage. "
            "Scientists count salmon each year:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Year</th><th>Before dam</th><th>5 years after</th><th>10 years after</th></tr>"
            "<tr><td>Salmon upstream of the dam</td><td>5,000</td><td>1,200</td><td>200</td></tr>"
            "</table>"
            "<p>Which statement is <strong>best supported</strong> by the data?</p>"
        ),
        "choices": [
            "The dam blocked the salmon's migration, so the number of salmon upstream dropped sharply.",
            "The dam increased the number of salmon upstream.",
            "The dam had no effect on salmon.",
            "Salmon moved upstream faster after the dam.",
        ],
        "answer": 0,
        "feedback": "Salmon fell from 5,000 to 200 after the dam. A structure that blocks movement can reduce populations.",
    },
    {
        "title": "MC 4 - An invasive predator",
        "dok": 2,
        "prompt": (
            "<p>Lionfish from another ocean were released into the Caribbean Sea. They eat many small reef fish and have no natural predators there. "
            "Surveys show:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Reef</th><th>Lionfish present?</th><th>Young native fish per 100 m<sup>2</sup></th></tr>"
            "<tr><td>1</td><td>No</td><td>120</td></tr>"
            "<tr><td>2</td><td>Yes</td><td>35</td></tr>"
            "</table>"
            "<p>Which conclusion is <strong>best supported</strong>?</p>"
        ),
        "choices": [
            "The invasive lionfish reduced the number of native young fish by feeding on them.",
            "Lionfish help native fish grow.",
            "Lionfish have no effect on reef communities.",
            "Reef 2 has more native fish than Reef 1.",
        ],
        "answer": 0,
        "feedback": "Young native fish are far fewer on the reef with lionfish (35 versus 120), which fits an invasive predator.",
    },
    {
        "title": "MC 5 - Which design meets the goals?",
        "dok": 3,
        "prompt": (
            "<p>A town wants to reduce fertilizer runoff into a stream. Its criteria are: (1) reduce nitrogen in the stream by at least 50%, and "
            "(2) cost no more than $100,000. Three solutions are proposed:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Solution</th><th>Nitrogen reduced (%)</th><th>Cost</th></tr>"
            "<tr><td>A: Plant wide strips of grass and trees along the stream</td><td>60</td><td>$70,000</td></tr>"
            "<tr><td>B: Build a water treatment plant for the stream</td><td>90</td><td>$3,000,000</td></tr>"
            "<tr><td>C: Put up signs asking farmers to use less fertilizer</td><td>10</td><td>$2,000</td></tr>"
            "</table>"
            "<p>Which solution <strong>best</strong> meets both criteria, and why?</p>"
        ),
        "choices": [
            "Solution A, because it reduces nitrogen by 60% (at least 50%) and costs $70,000 (under $100,000).",
            "Solution B, because it reduces nitrogen the most.",
            "Solution C, because it costs the least.",
            "None, because every solution must reduce nitrogen by 100%.",
        ],
        "answer": 0,
        "feedback": "Only Solution A meets both criteria. B is too expensive and C does not reduce enough nitrogen.",
    },
    {
        "title": "MC 6 - Weighing trade-offs",
        "dok": 3,
        "prompt": (
            "<p>A highway cuts through a habitat, and many animals are killed on the road. A wildlife agency compares solutions. "
            "Its criteria are: reduce road deaths by at least 70% and let animals cross to find food and mates.</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Solution</th><th>Road deaths reduced (%)</th><th>Animals can cross?</th><th>Cost</th></tr>"
            "<tr><td>A: Overpasses with plants</td><td>80</td><td>Yes</td><td>$2,000,000</td></tr>"
            "<tr><td>B: Warning signs</td><td>10</td><td>Yes</td><td>$20,000</td></tr>"
            "<tr><td>C: A tall fence along the whole highway</td><td>75</td><td>No</td><td>$500,000</td></tr>"
            "</table>"
            "<p>Which statement <strong>best</strong> evaluates the solutions?</p>"
        ),
        "choices": [
            "Only A meets both criteria; its trade-off is a high cost, but it protects animals and lets them move.",
            "C is best because it is cheaper than A and reduces deaths by 75%, so crossing does not matter.",
            "B is best because it costs the least and meets the criteria.",
            "All three solutions meet the criteria equally.",
        ],
        "answer": 0,
        "feedback": "A is the only solution that both cuts deaths by at least 70% and lets animals cross. Cost is its trade-off.",
    },
    {
        "title": "MC 7 - Refining a solution",
        "dok": 3,
        "prompt": (
            "<p>A city tests rain gardens (planted basins that soak up rainwater) in three neighborhoods to reduce polluted runoff:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Neighborhood</th><th>Soil type</th><th>Runoff reduced (%)</th></tr>"
            "<tr><td>1</td><td>Sandy</td><td>45</td></tr>"
            "<tr><td>2</td><td>Sandy</td><td>40</td></tr>"
            "<tr><td>3</td><td>Heavy clay</td><td>12</td></tr>"
            "</table>"
            "<p>Which refinement is <strong>best supported</strong> by the test data?</p>"
        ),
        "choices": [
            "Change the design for clay soil, for example by adding drainage or mixing in sand, and then test it again.",
            "Stop using rain gardens in all neighborhoods.",
            "Build the same design in clay soil because the data are not important.",
            "Test only in sandy soil and ignore Neighborhood 3.",
        ],
        "answer": 0,
        "feedback": "The solution worked in sandy soil but not clay. The data point to a specific change to try and then retest.",
    },
    {
        "title": "MC 8 - Defending a plan",
        "dok": 3,
        "prompt": (
            "<p>A group proposes restoring wetlands to filter polluted water. Which statement is the <strong>strongest</strong> defense of the plan?</p>"
        ),
        "choices": [
            "Test sites show wetlands removed 65% of nitrogen at a cost of $40 per kilogram, which is below the alternatives; the plan needs land, so we will use public land first.",
            "Wetlands are natural, so they are the best solution.",
            "Everyone likes wetlands, so the plan will work.",
            "The plan should be accepted because it was proposed first.",
        ],
        "answer": 0,
        "feedback": "A strong defense uses evidence (percent removed, cost), compares it with alternatives, and addresses a limit (land).",
    },
]

FREE_RESPONSE = [
    {
        "title": "FR 1 - Algae in Harbor Bay",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>Harbor Bay has summer algae blooms that kill fish. Scientists find the sources of the extra nitrogen and list possible solutions:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Source of nitrogen</th><th>Share of the total (%)</th></tr>"
            "<tr><td>Farm fertilizer runoff</td><td>50</td></tr>"
            "<tr><td>Lawn fertilizer runoff</td><td>30</td></tr>"
            "<tr><td>Leaking sewage systems</td><td>20</td></tr>"
            "</table>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Possible solution</th><th>Cuts nitrogen in the bay by</th><th>Cost per year</th></tr>"
            "<tr><td>A: Plant strips of grass and trees along farm streams</td><td>25%</td><td>$60,000</td></tr>"
            "<tr><td>B: Restore wetlands at the river mouth</td><td>20%</td><td>$90,000</td></tr>"
            "<tr><td>C: Ban lawn fertilizer in summer</td><td>12%</td><td>$10,000</td></tr>"
            "<tr><td>D: Repair the sewage system</td><td>18%</td><td>$250,000</td></tr>"
            "</table>"
            "<p>The town's criteria are: cut nitrogen by at least 40% in total, and spend no more than $200,000 per year.</p>"
            "<ol>"
            "<li><strong>Design:</strong> Choose a combination of solutions that meets both criteria. Show the total reduction and total cost.</li>"
            "<li><strong>Evaluate:</strong> Explain the trade-offs of your design, using data, and explain why you did not choose at least one of the other solutions.</li>"
            "<li><strong>Refine:</strong> After one year, nitrogen fell by only 30%. Suggest one change to improve your design, and explain how you would test whether it works.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Selects a combination that meets both criteria with correct totals (for example, A + B + C = 57% for $160,000; or A + C + B; A + B = 45% for $150,000). "
             "Explains trade-offs with data (for example, wetlands cost more per percent than lawn ban) and justifies leaving out another solution (for example, D exceeds the budget). "
             "The refinement is a specific change connected to the feedback (for example, add buffer strips along more streams or increase enforcement of the ban) and a clear test plan (measure nitrogen again and compare with the goal)."),
            (3, "Proficient",
             "Combination meets both criteria with correct totals. Trade-offs and the rejected option are explained, but the refinement or the test plan is thin."),
            (2, "Developing",
             "Combination misses one criterion or has a math error. Trade-offs are vague. Refinement is general."),
            (1, "Beginning",
             "No combination chosen, or it ignores the criteria. Little or no data."),
        ],
        "grading_notes": [
            "Accept any combination with a total of at least 40% reduction and at most $200,000 per year. Valid examples: A + B (45%, $150,000); A + C + B (57%, $160,000); A + B + C (57%, $160,000); A + C + D is not valid (exceeds budget).",
            "Because farm runoff is 50% of the source, a solution that targets farms should be considered, but any reasoned choice that meets the criteria is acceptable.",
            "Refinement example: add more buffer strips or increase the share of farms covered; test by measuring nitrogen again next summer and comparing it with the 40% goal.",
        ],
        "exemplar": (
            "I would choose Solutions A, B, and C. Together they cut nitrogen by 25% + 20% + 12% = 57%, which is above the 40% goal, and cost $60,000 + $90,000 + $10,000 = $160,000 per year, which is under the $200,000 limit. "
            "A targets the largest source, farms, at a modest cost. B costs more per percent cut ($4,500 per percent compared with $2,400 for A and about $830 for C), which is a trade-off, but it adds protection. I did not choose D because at $250,000 it is over the budget by itself. "
            "If nitrogen fell by only 30% after a year, I would add buffer strips along more farm streams, since farms are the biggest source, and test the change by measuring nitrogen in the bay again next summer and comparing it with the 40% goal."
        ),
    },
    {
        "title": "FR 2 - Paying to protect the forest",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>A conservation group tests a solution in two villages next to a rainforest: farmers are paid each year if they do not clear new forest. "
            "After three years:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th></th><th>Village A</th><th>Village B</th></tr>"
            "<tr><td>Forest cleared per year before the plan (%)</td><td>4.0</td><td>4.0</td></tr>"
            "<tr><td>Forest cleared per year after the plan (%)</td><td>1.0</td><td>3.5</td></tr>"
            "<tr><td>Payments arrived on time?</td><td>Yes</td><td>No (often 6 months late)</td></tr>"
            "<tr><td>Cost per village per year</td><td>$80,000</td><td>$80,000</td></tr>"
            "</table>"
            "<ol>"
            "<li><strong>Evaluate:</strong> Judge whether the solution works. Use at least two pieces of data and name one gain and one cost.</li>"
            "<li><strong>Refine:</strong> Use the data to propose one change that would improve the solution, and explain why it should help.</li>"
            "<li><strong>Defend:</strong> Write two sentences defending the improved solution to a skeptical village leader, using evidence.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Judges that the solution can work when payments are reliable (clearing fell from 4.0% to 1.0% in Village A, but only to 3.5% in Village B). "
             "Names a gain (less forest loss and habitat for biodiversity) and a cost ($80,000 per year per village). "
             "Proposes a specific change tied to the data (guarantee on-time payments) and explains why it should help. "
             "Defense uses evidence and addresses the leader's concern (for example, 75% less clearing for $80,000 a year when paid on time)."),
            (3, "Proficient",
             "Judges correctly with two data points, a gain, and a cost. Refinement is tied to the data, but the defense is brief or lacks evidence."),
            (2, "Developing",
             "Judgment is partly correct. One data point. Refinement is general, or the defense is an opinion."),
            (1, "Beginning",
             "Judgment is wrong or missing. Little or no data. Refinement and defense are missing."),
        ],
        "grading_notes": [
            "Key data: 4.0 to 1.0 in Village A (a 75% drop) versus 4.0 to 3.5 in Village B (a 12.5% drop); late payments in Village B.",
            "Gain: protects forest and habitat. Cost: $80,000 per village per year. Accept additional gains and costs.",
            "Accept any refinement tied to the data (on-time payments, monitoring, education), but the best is to guarantee on-time payments.",
            "Common misconception: that the solution failed in Village B for no reason; the difference in payments is the clue.",
        ],
        "exemplar": (
            "The solution works when it is carried out well: forest clearing dropped from 4.0% to 1.0% per year in Village A, where payments arrived on time, but only from 4.0% to 3.5% in Village B, where payments were often six months late. "
            "A gain is that less forest is cleared, which protects habitat for many species. A cost is $80,000 per village each year. "
            "To improve the plan, I would make sure payments arrive on time, because the village with on-time payments cut clearing by 75% and the one with late payments hardly changed. "
            "To the village leader I would say: where farmers were paid on time, forest loss fell by three-quarters for $80,000 a year, so with reliable payments your village can protect its forest and its income."
        ),
    },
]
