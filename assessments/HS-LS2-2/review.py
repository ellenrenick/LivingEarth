"""Unit review for HS-LS2-2 (unit 4.2). Done on the review day, built around the CFAs (no practice test).

Boundary: provided data only.
"""

STANDARD = "HS-LS2-2"
UNIT_TITLE = "Patterns in Populations"
GOAL = ("Use math on provided data to explain how factors affect populations and biodiversity, and revise "
        "explanations when new data come in.")

KEY_IDEAS = [
    "<strong>A population</strong> is one species in one area. <strong>Biodiversity</strong> is the variety of species in an ecosystem.",
    "<strong>Factors that change them</strong> include predators, pollution, habitat loss, invasive species, and food supply.",
    "<strong>Mean (average):</strong> add the values and divide by how many there are. <strong>Rate of change:</strong> (end value - start value) &divide; time.",
    "<strong>A trend</strong> is the general direction of the data: rising, falling, or level.",
    "<strong>To compare ecosystems of different sizes,</strong> divide by area (for example, species per km<sup>2</sup>).",
    "<strong>New data can change an explanation.</strong> Compare groups that differ in only one factor to see which factor matters.",
]

VOCAB = {
    "bank": ["population", "biodiversity", "limiting factor", "mean", "rate of change", "trend"],
    "blanks": [
        ("All the individuals of one species in an area are a ____________.", "population"),
        ("The variety of species in an ecosystem is its ____________.", "biodiversity"),
        ("A resource or condition that keeps a population from growing larger is a ____________.", "limiting factor"),
        ("The sum of the values divided by how many there are is the ____________.", "mean"),
        ("How much a quantity changes per unit of time is its ____________.", "rate of change"),
        ("The general direction of data over time is the ____________.", "trend"),
    ],
}

SECTIONS = [
    {"id": "A", "title": "Population, biodiversity, and the factors that change them", "lts": ["LS2-2.1"],
     "intro": "<p>Use the vocabulary correctly.</p>",
     "items": [
         ("A forest has 30 oak trees and 40 species of insects. Which number describes a population and which describes biodiversity?", "30 oaks is a population; 40 insect species relates to biodiversity."),
         ("Name three factors that can change a population or biodiversity.", "Examples: a new predator, pollution, habitat loss, an invasive species."),
     ]},
    {"id": "B", "title": "Reading tables and graphs", "lts": ["LS2-2.2"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Year</th><th>2020</th><th>2021</th><th>2022</th><th>2023</th></tr><tr><td>Frogs counted</td><td>90</td><td>120</td><td>150</td><td>150</td></tr></table>",
     "items": [
         ("How many frogs were counted in 2021?", "120."),
         ("Describe the trend.", "The population increased from 2020 to 2022 and then leveled off in 2023."),
     ]},
    {"id": "C", "title": "Mean, rate of change, and trend", "lts": ["LS2-2.3"],
     "intro": "<p>Use the frog data above for some questions.</p>",
     "items": [
         ("Find the mean number of frogs for the four years.", "(90 + 120 + 150 + 150) / 4 = 127.5."),
         ("Find the rate of change from 2020 to 2022.", "(150 - 90) / 2 = 30 frogs per year."),
         ("Lake A trout went from 200 to 280 in 4 years. Lake B trout went from 1,000 to 1,060 in 4 years. Which grew faster?", "Lake A at 20 per year; Lake B grew 15 per year."),
     ]},
    {"id": "D", "title": "Comparing ecosystems of different sizes", "lts": ["LS2-2.4"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Ecosystem</th><th>Area (km<sup>2</sup>)</th><th>Species</th></tr><tr><td>Pond</td><td>0.5</td><td>40</td></tr><tr><td>Lake</td><td>5</td><td>90</td></tr></table>",
     "items": [
         ("Calculate species per km<sup>2</sup> for each.", "Pond: 40 / 0.5 = 80. Lake: 90 / 5 = 18."),
         ("Which has higher biodiversity for its size?", "The pond (80 versus 18 species per km<sup>2</sup>), even though the lake has more species in total."),
         ("Why divide by area?", "So ecosystems of different sizes can be compared fairly."),
     ]},
    {"id": "E", "title": "Math as evidence, and revising", "lts": ["LS2-2.5", "LS2-2.6"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Pond group</th><th>Road nearby?</th><th>Pesticide runoff?</th><th>Change in frog population</th></tr><tr><td>1</td><td>Yes</td><td>No</td><td>-3%</td></tr><tr><td>2</td><td>Yes</td><td>Yes</td><td>-62%</td></tr><tr><td>3</td><td>No</td><td>Yes</td><td>-58%</td></tr><tr><td>4</td><td>No</td><td>No</td><td>+1%</td></tr></table>",
     "items": [
         ("A student first claims, &ldquo;Frogs are disappearing because of road noise.&rdquo; Which groups let you test this?", "Groups 1 and 4 (road versus no road, with no pesticide) and groups 2 and 3."),
         ("What do the numbers show about road noise alone? About pesticide runoff?", "Road alone: -3%, very small. Pesticide runoff: about -60% with or without a road."),
         ("Revise the explanation using the data.", "Frog populations dropped about 60% in ponds with pesticide runoff, with or without a road, so pesticide runoff is the main factor."),
     ]},
]

WRITE = {
    "prompt": ("<p>Four islands of different sizes have bird species. Two have invasive cats.</p>"
               "<table border=\"1\" cellpadding=\"6\"><tr><th>Island</th><th>Area (km<sup>2</sup>)</th><th>Cats present?</th><th>Bird species</th></tr>"
               "<tr><td>W</td><td>4</td><td>No</td><td>32</td></tr><tr><td>X</td><td>20</td><td>No</td><td>80</td></tr>"
               "<tr><td>Y</td><td>4</td><td>Yes</td><td>12</td></tr><tr><td>Z</td><td>20</td><td>Yes</td><td>36</td></tr></table>"
               "<p>Write an explanation: <strong>Claim</strong> (how cats affect bird biodiversity), <strong>Evidence</strong> (calculate species per km<sup>2</sup> for all four islands and compare islands of the same size), and <strong>Reasoning</strong> (why you divide by area, and one reason cats reduce species).</p>"),
    "checklist": ["States that cats reduce bird biodiversity",
                  "Shows the four calculations (W 8, X 4, Y 3, Z 1.8 species per km<sup>2</sup>)",
                  "Compares islands of the same size (W with Y, X with Z)",
                  "Explains that dividing by area makes different-sized islands comparable",
                  "Gives a reason, such as cats eating birds and eggs"],
    "exemplar": ("Invasive cats reduce bird biodiversity. W has 32 / 4 = 8 species per km<sup>2</sup>, X has 80 / 20 = 4, Y has 12 / 4 = 3, and Z has 36 / 20 = 1.8. "
                 "Comparing same-sized islands, W (no cats) has 8 and Y (cats) has 3, and X (no cats) has 4 and Z (cats) has 1.8, so cats lower biodiversity by more than half. "
                 "I divided by area because a larger island is expected to have more species just from its size. Cats eat birds and their eggs, so some species cannot reproduce enough to stay on the island."),
}
