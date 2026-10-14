"""CFAs for HS-LS2-2 (unit 4.2): one short exit-ticket check per priority learning target.

Each CFA is worth 6 points. MC items list the correct choice FIRST (the builder shuffles).
Assessment boundary: provided data only.
"""

STANDARD = "HS-LS2-2"
UNIT = "4.2"
UNIT_TITLE = "Patterns in Populations"

CFAS = [
    {
        "id": "LS2-2.1", "dok": 1,
        "lt": "I can define population and biodiversity and name factors that change them.",
        "items": [
            {"prompt": "<p>A population is</p>",
             "choices": ["all the individuals of one species in the same area", "all the species in an area", "all the living and nonliving things in an area", "a group of different species"],
             "feedback": "A population is one species in one area."},
            {"prompt": "<p>Biodiversity is the</p>",
             "choices": ["variety of different species in an ecosystem", "number of individuals of one species", "size of an ecosystem", "amount of rainfall"],
             "feedback": "Biodiversity is the variety of species."},
            {"prompt": "<p>Which is a factor that can change a population or biodiversity?</p>",
             "choices": ["A new predator, pollution, or loss of habitat", "The color of a rock", "The name of a lake", "A student's opinion"],
             "feedback": "Predators, pollution, and habitat loss are examples of factors that change populations."},
        ],
    },
    {
        "id": "LS2-2.2", "dok": 2,
        "lt": "I can read graphs and tables of population or biodiversity data.",
        "items": [
            {"prompt": "<table border=\"1\" cellpadding=\"4\"><tr><th>Year</th><th>1</th><th>2</th><th>3</th></tr><tr><td>Frogs</td><td>50</td><td>70</td><td>90</td></tr></table><p>How many frogs were counted in year 2?</p>",
             "choices": ["70", "50", "90", "20"],
             "feedback": "The table gives 70 frogs in year 2."},
            {"prompt": "<p>The table above shows that the number of frogs</p>",
             "choices": ["increased each year", "decreased each year", "stayed the same", "was random"],
             "feedback": "50, 70, 90 is an increase."},
            {"prompt": "<p>Describe in 1 sentence what the data in the table show, using numbers.</p>",
             "points": 2,
             "criteria": [(2, "States the direction of change with at least two values."),
                          (1, "States the direction without numbers."),
                          (0, "Blank or incorrect.")],
             "exemplar": "The frog population increased from 50 in year 1 to 90 in year 3."},
        ],
    },
    {
        "id": "LS2-2.3", "dok": 2,
        "lt": "I can find averages, rates of change, and trends in population data.",
        "items": [
            {"prompt": "<p>What is the mean of 10, 14, 12, and 16?</p>",
             "choices": ["13", "12", "16", "52"],
             "feedback": "(10 + 14 + 12 + 16) / 4 = 13."},
            {"prompt": "<p>A population grew from 200 to 260 in 3 years. What is the rate of change?</p>",
             "choices": ["20 per year", "60 per year", "3 per year", "260 per year"],
             "feedback": "(260 - 200) / 3 = 20 per year."},
            {"prompt": "<p>Data: 80, 70, 60, 50, 40. Name the trend and give the average change per time period.</p>",
             "points": 2,
             "criteria": [(2, "Decreasing trend; change of -10 per period."),
                          (1, "Trend or change correct, not both."),
                          (0, "Blank or incorrect.")],
             "exemplar": "The trend is decreasing, by 10 each time period."},
        ],
    },
    {
        "id": "LS2-2.4", "dok": 2,
        "lt": "I can use math to compare populations and biodiversity across ecosystems of different sizes.",
        "items": [
            {"prompt": "<p>Park A has 30 species in 3 km<sup>2</sup>. Park B has 50 species in 10 km<sup>2</sup>. Which has more species per km<sup>2</sup>?</p>",
             "choices": ["Park A: 10 per km<sup>2</sup> versus 5", "Park B: 5 versus 10", "They are equal", "Cannot be compared"],
             "feedback": "30 / 3 = 10; 50 / 10 = 5."},
            {"prompt": "<p>Why divide by area when comparing two ecosystems of different sizes?</p>",
             "choices": ["So the comparison is fair for the size of each ecosystem", "To make numbers bigger", "Because area does not matter", "To find the mean"],
             "feedback": "Dividing by area gives a fair comparison."},
            {"prompt": "<p>Pond P has 15 fish in 0.5 km<sup>2</sup>. Pond Q has 36 fish in 3 km<sup>2</sup>. Show which pond has more fish per km<sup>2</sup>.</p>",
             "points": 2,
             "criteria": [(2, "Pond P: 30 per km<sup>2</sup>; Pond Q: 12 per km<sup>2</sup>; concludes P has more."),
                          (1, "One value correct, or correct method with an arithmetic error."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Pond P: 15 / 0.5 = 30 per km<sup>2</sup>. Pond Q: 36 / 3 = 12 per km<sup>2</sup>. Pond P has more fish for its size."},
        ],
    },
    {
        "id": "LS2-2.5", "dok": 3,
        "lt": "I can use math as evidence to explain how a factor affects a population or biodiversity.",
        "items": [
            {"prompt": "<table border=\"1\" cellpadding=\"4\"><tr><th>Pollution level</th><th>Low</th><th>Medium</th><th>High</th></tr><tr><td>Insect species</td><td>40</td><td>25</td><td>10</td></tr></table><p>Which statement uses the data correctly?</p>",
             "choices": ["Insect species fell from 40 to 10 as pollution rose, a 75% decrease.", "Insect species increased with pollution.", "Pollution had no effect.", "Insect species fell by 10%."],
             "feedback": "(40 - 10) / 40 = 75%."},
            {"prompt": "<p>A claim that a factor affects a population is strongest when</p>",
             "choices": ["numbers show a change that goes with the factor", "people believe it", "it sounds reasonable", "only one example is given"],
             "feedback": "Numbers that change with a factor are good evidence."},
            {"prompt": "<p>Use the table above: write one sentence explaining how pollution affects biodiversity and include a calculation.</p>",
             "points": 2,
             "criteria": [(2, "States that higher pollution lowers species and shows a correct calculation."),
                          (1, "States the relationship without a calculation, or a calculation without the explanation."),
                          (0, "Blank or incorrect.")],
             "exemplar": "As pollution rises, insect biodiversity falls: from 40 to 10 species, which is a 75% drop."},
        ],
    },
    {
        "id": "LS2-2.6", "dok": 3,
        "lt": "I can use new data to revise my explanation of what affects a population or biodiversity.",
        "items": [
            {"prompt": "<p>A student says deer decreased because of cold winters. New data show deer also decreased in mild winters, but only where hunting was allowed. What should she do?</p>",
             "choices": ["Revise her explanation to include hunting.", "Ignore the new data.", "Keep her explanation unchanged.", "Say the data are wrong."],
             "feedback": "Explanations should change when new data do not fit."},
            {"prompt": "<p>Which revised explanation best fits the new data above?</p>",
             "choices": ["Deer decreased mainly where hunting was allowed, in both cold and mild winters.", "Deer decreased only because of cold winters.", "Deer did not decrease.", "Hunting increased the deer population."],
             "feedback": "The new data point to hunting."},
            {"prompt": "<p>Your first explanation: &ldquo;Fish decreased because of a drought.&rdquo; New data: fish also decreased 70% in lakes with no drought but with a new invasive predator. Revise your explanation in 1 or 2 sentences.</p>",
             "points": 2,
             "criteria": [(2, "Revises to include the predator, using the new data."),
                          (1, "Mentions the predator but keeps the old explanation unchanged, or revises without using the data."),
                          (0, "Blank or no revision.")],
             "exemplar": "Fish decreased because of the invasive predator as well as drought: lakes with no drought but with the predator still lost 70% of their fish."},
        ],
    },
]
