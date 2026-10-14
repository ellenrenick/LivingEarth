"""Unit review for HS-LS2-4 (unit 4.1). Done on the review day, built around the CFAs (no practice test).

Boundary: proportional reasoning only.
"""

STANDARD = "HS-LS2-4"
UNIT_TITLE = "Cycles of Life"
GOAL = ("Use math to support claims about how matter cycles and energy flows among organisms in an ecosystem.")

KEY_IDEAS = [
    "<strong>Producers</strong> make their own food from sunlight, <strong>consumers</strong> eat other organisms, and <strong>decomposers</strong> break down dead matter and return it to the soil and air.",
    "<strong>Matter cycles.</strong> Atoms such as carbon are reused again and again. They are conserved.",
    "<strong>Energy flows one way.</strong> It enters as sunlight and leaves as heat. Ecosystems need a constant supply of new energy.",
    "<strong>The 10% rule:</strong> about 10% of the energy at one trophic level is stored in the next. The rest is used for life processes or lost as heat.",
    "<strong>To find the percent passed on:</strong> divide the energy in the next level by the energy in the level below, then multiply by 100.",
    "<strong>To show matter is conserved,</strong> add up all the parts. The total stays the same even when the parts change.",
]

VOCAB = {
    "bank": ["producer", "consumer", "decomposer", "trophic level", "biomass", "food web"],
    "blanks": [
        ("An organism that makes its own food from sunlight is a ____________.", "producer"),
        ("An organism that gets energy by eating others is a ____________.", "consumer"),
        ("An organism that breaks down dead matter and returns it to the environment is a ____________.", "decomposer"),
        ("A feeding level in a food chain is a ____________.", "trophic level"),
        ("The total mass of living material at a level is its ____________.", "biomass"),
        ("A diagram of many feeding connections is a ____________.", "food web"),
    ],
}

SECTIONS = [
    {"id": "A", "title": "Roles in an ecosystem", "lts": ["LS2-4.1"],
     "intro": "<p>Name the role of each organism.</p>",
     "items": [
         ("Grass, a rabbit, a hawk, and a mushroom on a dead log: label each as producer, consumer, or decomposer.", "Grass: producer. Rabbit: consumer. Hawk: consumer. Mushroom: decomposer."),
         ("What would happen to the matter in dead leaves if there were no decomposers?", "It would stay locked in the dead matter and not return to the soil and air for producers to reuse."),
     ]},
    {"id": "B", "title": "Matter cycles, energy flows", "lts": ["LS2-4.2"],
     "intro": "<p>Compare how matter and energy move.</p>",
     "items": [
         ("Complete: Matter is ____________ and energy ____________ through a food web.", "Recycled (cycles); flows one way and leaves as heat."),
         ("Where does the energy for almost all ecosystems come from?", "The Sun."),
         ("A student says decomposers recycle energy back to producers. Correct this.", "Decomposers return matter, not energy. Energy is lost as heat, so producers need new energy from the Sun."),
     ]},
    {"id": "C", "title": "Energy pyramids and the 10% rule", "lts": ["LS2-4.3", "LS2-4.4"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Trophic level</th><th>Energy stored (kJ per year)</th></tr><tr><td>Producers</td><td>20,000</td></tr><tr><td>Primary consumers</td><td>2,000</td></tr><tr><td>Secondary consumers</td><td>200</td></tr><tr><td>Tertiary consumers</td><td>20</td></tr></table>",
     "items": [
         ("What percent of the energy passes from each level to the next?", "10% each time (2,000/20,000, 200/2,000, 20/200)."),
         ("Where does the other 90% go?", "It is used for life processes such as moving and growing, or lost as heat."),
         ("Grass stores 8,000 kJ. How much is stored in the next two levels using the 10% rule?", "800 kJ, then 80 kJ."),
         ("A level stores 500 kJ and the next level stores 45 kJ. What percent was passed on?", "45 / 500 = 0.09 = 9%."),
         ("Why do food chains rarely have more than four or five levels?", "So little energy is left at the top (only about 10% per step) that it cannot support more levels."),
     ]},
    {"id": "D", "title": "Matter is conserved", "lts": ["LS2-4.5"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Carbon (units)</th><th>Air</th><th>Plants</th><th>Animals</th><th>Soil</th></tr><tr><td>Start</td><td>600</td><td>250</td><td>50</td><td>100</td></tr><tr><td>End</td><td>570</td><td>270</td><td>55</td><td>105</td></tr></table>",
     "items": [
         ("Find the total carbon at the start and at the end.", "1,000 at the start and 1,000 at the end."),
         ("What do the totals show about matter?", "Matter (carbon) is conserved; it moved among the air, plants, animals, and soil but was not created or destroyed."),
         ("Air has 500, plants 300, soil 200. Later air has 470 and soil 215. How many units are in the plants if carbon is conserved?", "Total 1,000. Plants = 1,000 - 470 - 215 = 315."),
     ]},
    {"id": "E", "title": "Supporting a claim with math", "lts": ["LS2-4.6"],
     "intro": "<p>A claim is stronger when numbers support it.</p>",
     "items": [
         ("A meadow's producers store 100,000 kJ. A hawk needs 25 kJ per year from a chain producers &rarr; mice &rarr; snakes &rarr; hawks. How many hawks can it support?", "100,000 &times; 0.1 &times; 0.1 &times; 0.1 = 100 kJ at the hawk level; 100 / 25 = 4 hawks."),
         ("Write a claim about energy in a food chain and support it with a calculation.", "Claim: Energy decreases at each level. If producers store 30,000 kJ, the next level stores about 3,000 kJ and the next about 300 kJ."),
     ]},
]

WRITE = {
    "prompt": ("<p>A class builds a sealed jar ecosystem (water, algae, snails, bacteria in the mud) and keeps it in a sunny window. They estimate carbon (in units):</p>"
               "<table border=\"1\" cellpadding=\"6\"><tr><th>Where the carbon is</th><th>Day 0</th><th>Day 20</th></tr>"
               "<tr><td>CO<sub>2</sub> in the water and air</td><td>70</td><td>58</td></tr>"
               "<tr><td>Algae (producers)</td><td>20</td><td>29</td></tr>"
               "<tr><td>Snails (consumers)</td><td>4</td><td>5</td></tr>"
               "<tr><td>Bacteria and mud (decomposers and dead matter)</td><td>6</td><td>8</td></tr></table>"
               "<p>Write an explanation: <strong>Claim</strong>, <strong>Evidence</strong> (calculate the totals), and <strong>Reasoning</strong> (the role of each group in moving the carbon, and what happens if the jar is kept in the dark).</p>"),
    "checklist": ["Calculates the totals (100 on day 0 and 100 on day 20) and says matter is conserved",
                  "Explains that carbon moved among the parts but was not created or destroyed",
                  "Explains the roles of producers, consumers, and decomposers",
                  "Says energy must keep entering as light",
                  "Predicts that in the dark the producers stop growing and the ecosystem fails, though the carbon is still there"],
    "exemplar": ("The total carbon is 70 + 20 + 4 + 6 = 100 units on day 0 and 58 + 29 + 5 + 8 = 100 units on day 20, so matter is conserved: carbon moved from the air and water into the algae, snails, and mud, but none was lost or made. "
                 "The algae are producers that take in CO<sub>2</sub> and build their bodies using light, the snails are consumers that eat the algae, and the bacteria are decomposers that break down dead matter and return carbon to the water. "
                 "In the dark, the algae could not capture energy, so they would stop growing and the other organisms would run out of food. The carbon would still be in the jar, but energy has to keep flowing in to run the cycle."),
}
