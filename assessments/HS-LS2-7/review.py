"""Unit review for HS-LS2-7 (unit 4.4). Done on the review day, built around the CFAs (no practice test).

LS2-7.4 and LS2-7.5 are DOK 4 (depth work); the CSA stops at DOK 3, and so does this review.
"""

STANDARD = "HS-LS2-7"
UNIT_TITLE = "Solutions for Sustainability"
GOAL = ("Design, evaluate, and refine a solution that reduces a human impact on the environment and biodiversity, "
        "and defend it with evidence.")

KEY_IDEAS = [
    "<strong>Human activities affect ecosystems:</strong> deforestation removes habitat, pollution harms organisms, dams block migration, and invasive species can crowd out natives.",
    "<strong>Start a design with evidence.</strong> Use data to find the biggest cause of a problem and target it.",
    "<strong>Criteria</strong> are the goals a solution must meet. <strong>Constraints</strong> are the limits, such as cost and time.",
    "<strong>Trade-offs:</strong> a solution can gain something and cost something. Compare gains and costs with numbers.",
    "<strong>Refine with feedback and new data.</strong> If a test shows a weakness, change the design and test it again.",
    "<strong>A strong defense</strong> uses evidence about how well the solution works and what it costs, and honestly names a limit.",
]

VOCAB = {
    "bank": ["deforestation", "pollution", "invasive species", "criteria", "constraints", "trade-off"],
    "blanks": [
        ("The clearing of large areas of forest is ____________.", "deforestation"),
        ("A harmful substance added to air, water, or soil is ____________.", "pollution"),
        ("A species brought into a new area where it harms the ecosystem is an ____________.", "invasive species"),
        ("The goals a solution must meet are its ____________.", "criteria"),
        ("The limits a solution must stay within, such as cost, are its ____________.", "constraints"),
        ("Giving up some of one benefit to gain another is a ____________.", "trade-off"),
    ],
}

SECTIONS = [
    {"id": "A", "title": "How human activities affect ecosystems", "lts": ["LS2-7.1"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Forest remaining (%)</th><th>100</th><th>60</th><th>30</th></tr><tr><td>Bird species</td><td>70</td><td>48</td><td>20</td></tr></table>",
     "items": [
         ("What do the data show about deforestation and biodiversity?", "As forest was cleared from 100% to 30%, bird species fell from 70 to 20."),
         ("Explain in a chain how fertilizer runoff can kill fish.", "Fertilizer runoff adds nutrients, algae grow too much, the algae die and decompose and use up oxygen, and fish die."),
         ("A dam blocks salmon from swimming upstream. Predict the effect on the salmon population upstream.", "It falls sharply because salmon cannot reach their spawning areas."),
     ]},
    {"id": "B", "title": "Designing a solution with evidence", "lts": ["LS2-7.2"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Source of trash in a stream</th><th>Share (%)</th></tr><tr><td>Storm drains</td><td>55</td></tr><tr><td>Littering at the park</td><td>25</td></tr><tr><td>Boat docks</td><td>20</td></tr></table>",
     "items": [
         ("Which source should the design target first? Why?", "Storm drains, because they are the largest source (55%)."),
         ("Describe a solution for the largest source.", "Install trash screens in storm drains."),
         ("Name one criterion and one constraint for your design.", "Criterion: reduce trash by at least 50%. Constraint: cost no more than $100,000 per year."),
     ]},
    {"id": "C", "title": "Judging gains and costs", "lts": ["LS2-7.3"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Solution</th><th>Trash reduced (%)</th><th>Cost per year</th></tr><tr><td>A: Screens on storm drains</td><td>45</td><td>$50,000</td></tr><tr><td>B: Cleanup days and bins at the park</td><td>20</td><td>$15,000</td></tr><tr><td>C: Bins and fines at docks</td><td>12</td><td>$10,000</td></tr><tr><td>D: Street sweeping</td><td>25</td><td>$120,000</td></tr></table><p>Criteria: reduce trash by at least 50% and spend no more than $100,000 per year.</p>",
     "items": [
         ("Does A alone meet the criteria? Explain.", "No. It meets the cost but reduces only 45%, below 50%."),
         ("Find a combination that meets both criteria and show the totals.", "A + B: 65% for $65,000. A + C: 57% for $60,000. A + B + C: 77% for $75,000."),
         ("Why is D a poor choice?", "It costs $120,000, over the budget, and reduces only 25%."),
         ("Name a trade-off of your combination.", "Example: A + B costs more than A alone but cuts trash much more."),
     ]},
    {"id": "D", "title": "Refining and defending", "lts": ["LS2-7.4", "LS2-7.5"],
     "intro": "<p>After a year, trash fell by only 40%.</p>",
     "items": [
         ("Suggest a change to improve the design and how you would test it.", "Add more screens or add a solution for another source, then measure trash again next year and compare with the 50% goal."),
         ("A classmate says your plan costs too much. Write a reply with evidence.", "Example: The plan cuts trash by 65% for $65,000, under the $100,000 limit, which is cheaper per percent than street sweeping."),
         ("Name one limit of your solution and how you would address it.", "Example: Screens need cleaning, so schedule monthly maintenance."),
     ]},
]

WRITE = {
    "prompt": ("<p>Fertilizer runoff gives a bay too many nutrients and causes algae blooms. Scientists find the sources and list solutions:</p>"
               "<table border=\"1\" cellpadding=\"6\"><tr><th>Source</th><th>Share of nitrogen (%)</th></tr><tr><td>Farms</td><td>45</td></tr><tr><td>Lawns</td><td>35</td></tr><tr><td>Sewage leaks</td><td>20</td></tr></table>"
               "<table border=\"1\" cellpadding=\"6\"><tr><th>Solution</th><th>Cuts nitrogen by</th><th>Cost per year</th></tr>"
               "<tr><td>A: Grass and tree strips along farm streams</td><td>22%</td><td>$50,000</td></tr>"
               "<tr><td>B: Restore wetlands at the river mouth</td><td>18%</td><td>$80,000</td></tr>"
               "<tr><td>C: Ban lawn fertilizer in summer</td><td>14%</td><td>$8,000</td></tr>"
               "<tr><td>D: Repair the sewage system</td><td>15%</td><td>$220,000</td></tr></table>"
               "<p>Criteria: cut nitrogen by at least 40% and spend no more than $180,000 per year.</p>"
               "<p>Write a plan: <strong>Design</strong> (a combination with totals), <strong>Evaluate</strong> (trade-offs and why you left one out), and <strong>Refine</strong> (what to change if nitrogen falls only 30% after a year, and how to test it).</p>"),
    "checklist": ["Chooses a combination that meets both criteria and shows the totals",
                  "Compares costs and reductions (for example, cost per percent)",
                  "Explains why at least one option was left out (D is over budget)",
                  "Names a specific change tied to the feedback",
                  "Says how to test the change and compare with the 40% goal"],
    "exemplar": ("I choose A, B, and C: 22% + 18% + 14% = 54% reduction, and $50,000 + $80,000 + $8,000 = $138,000 per year, which meets both criteria. "
                 "A targets farms, the largest source (45%); C is the cheapest per percent (about $570 per percent) and B costs more per percent (about $4,400) but adds protection, which is a trade-off. I left out D because at $220,000 it is over the budget by itself. "
                 "If nitrogen fell only 30%, I would add strips along more farm streams, since farms are the biggest source, and test it by measuring nitrogen in the bay next summer and comparing it with the 40% goal."),
}
