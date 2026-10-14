"""Question bank for the HS-ESS3-1 CSA: Earth Shaping Humanity (unit 4.3).

45-minute test, 30 points. Edit, then run `python3 ../build_unit.py HS-ESS3-1`.
"""

TITLE = "HS-ESS3-1 Assessment: Earth Shaping Humanity"
STANDARD = "HS-ESS3-1"
QUIZ_ID = "hs_ess3_1_earth_shaping_humanity"
FILE_PREFIX = "HS-ESS3-1"
MAX_ATTEMPTS = 1
TIME_MINUTES = 45
KEY_POSITIONS = [3, 1, 0, 2, 1, 3, 0, 2]

DESCRIPTION = (
    "<p><strong>Living Earth (Biology) &ndash; HS-ESS3-1</strong></p>"
    "<p>Construct an explanation based on evidence for how the availability of natural resources, "
    "occurrence of natural hazards, and changes in climate have influenced human activity.</p>"
    "<p>Part 1: Vocabulary matching &middot; Part 2: Multiple choice &middot; Part 3: Free response</p>"
)

MATCHING = {
    "title": "Part 1: Vocabulary Matching",
    "points": 6,
    "prompt": "<p>Match each term with its best definition. Some definitions will not be used.</p>",
    "pairs": [
        ("Natural resource", "A material from Earth that people use, such as fresh water, fertile soil, minerals, or fossil fuels"),
        ("Natural hazard", "A natural event, such as an earthquake, flood, or hurricane, that can harm people and property"),
        ("Fertile soil", "Soil rich in the nutrients that plants need to grow well"),
        ("Climate", "The typical weather pattern of a region over many years"),
        ("Migration", "The movement of people from one place to live in another"),
        ("Sea level rise", "The increase in the average height of the ocean's surface over time"),
    ],
    "distractors": [
        "The daily change in the temperature and rainfall of a place",
        "A rule that limits how many people can live in a city",
    ],
}

MULTIPLE_CHOICE = [
    {
        "title": "MC 1 - Early civilizations",
        "dok": 2,
        "prompt": (
            "<p>Some of the earliest large civilizations began in river valleys:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Civilization</th><th>River</th><th>What the river provided</th></tr>"
            "<tr><td>Ancient Egypt</td><td>Nile</td><td>Fresh water; yearly floods left rich silt on the fields</td></tr>"
            "<tr><td>Mesopotamia</td><td>Tigris and Euphrates</td><td>Fresh water; fertile soil; routes for travel</td></tr>"
            "<tr><td>Indus Valley</td><td>Indus</td><td>Fresh water; fertile floodplain; routes for travel</td></tr>"
            "</table>"
            "<p>Which statement is <strong>best supported</strong> by the table?</p>"
        ),
        "choices": [
            "People settled where natural resources such as fresh water and fertile soil were available, which let them grow food and form large communities.",
            "People settled by rivers only because they enjoyed the view.",
            "Rivers did not affect where people lived.",
            "Large civilizations formed in places with no fresh water.",
        ],
        "answer": 0,
        "feedback": "Fresh water and fertile soil allowed farming, which supported large populations in river valleys.",
    },
    {
        "title": "MC 2 - Uneven water",
        "dok": 2,
        "prompt": (
            "<p>The table shows the fresh water available per person per year in three regions:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Region</th><th>Fresh water per person (cubic meters per year)</th></tr>"
            "<tr><td>A</td><td>15,000</td></tr>"
            "<tr><td>B</td><td>1,200</td></tr>"
            "<tr><td>C</td><td>300</td></tr>"
            "</table>"
            "<p>Which statement <strong>best</strong> describes the pattern and its likely effect on human activity?</p>"
        ),
        "choices": [
            "Fresh water is spread unevenly, so Region C will have a harder time growing food and supporting large cities than Region A.",
            "Fresh water is spread evenly, so every region can farm in the same way.",
            "Region C has the most water, so it can support the largest population.",
            "Water supply does not affect where people live.",
        ],
        "answer": 0,
        "feedback": "Region A has about 50 times as much water per person as Region C. Limited water limits farming and city size.",
    },
    {
        "title": "MC 3 - Living near a fault",
        "dok": 2,
        "prompt": (
            "<p>Millions of people live in cities near active earthquake faults, such as along the coast of California and Japan. "
            "These areas also have major ports, flat land, and fertile soil nearby.</p>"
            "<p>Which statement <strong>best</strong> explains why many people live in these areas despite the hazard?</p>"
        ),
        "choices": [
            "The benefits of resources such as harbors and fertile land are large, and people reduce the risk with measures such as earthquake-resistant buildings.",
            "People do not know earthquakes are possible there.",
            "Earthquakes only happen where nobody lives.",
            "Natural hazards have no effect on how people build.",
        ],
        "answer": 0,
        "feedback": "People weigh the benefits of a place against its hazards and adapt, for example with building codes.",
    },
    {
        "title": "MC 4 - A flood plain",
        "dok": 2,
        "prompt": (
            "<p>Farmers on a flood plain grow three times more rice per acre than farmers in the hills. Every few years, floods damage homes in the flood plain. "
            "The floods also leave a layer of nutrient-rich mud on the fields.</p>"
            "<p>Which statement <strong>best</strong> describes the flood plain?</p>"
        ),
        "choices": [
            "Flooding is both a hazard and a source of a resource, because it harms homes but also renews the fertile soil.",
            "Flooding is only a hazard and has no benefit.",
            "Flooding is only a resource and never causes harm.",
            "The fertile soil is not related to flooding.",
        ],
        "answer": 0,
        "feedback": "Floods can damage property, yet they also deposit nutrients that make the land fertile.",
    },
    {
        "title": "MC 5 - Changing climate, changing crops",
        "dok": 3,
        "prompt": (
            "<p>Over 30 years, a farming region records the following:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Year</th><th>1990</th><th>2000</th><th>2010</th><th>2020</th></tr>"
            "<tr><td>Yearly rainfall (mm)</td><td>700</td><td>650</td><td>580</td><td>520</td></tr>"
            "<tr><td>Wheat yield (tons per hectare)</td><td>3.2</td><td>3.0</td><td>2.5</td><td>2.0</td></tr>"
            "</table>"
            "<p>Which prediction is <strong>best supported</strong> by the data?</p>"
        ),
        "choices": [
            "If the trend continues, farmers may switch to crops that need less water or may leave the area, because less rain is lowering wheat yields.",
            "Wheat yields will rise because rainfall is falling.",
            "Rainfall has no connection to crop yields.",
            "Farmers will grow more wheat each year, since yield has been steady.",
        ],
        "answer": 0,
        "feedback": "As rainfall fell from 700 to 520 mm, yields fell from 3.2 to 2.0. Continuing the trend would push farmers to change crops or move.",
    },
    {
        "title": "MC 6 - Rising seas",
        "dok": 3,
        "prompt": (
            "<p>A low coastal city records how many days each year the streets flood at high tide while the sea level rises:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Year</th><th>2000</th><th>2010</th><th>2020</th></tr>"
            "<tr><td>Flood days per year</td><td>5</td><td>12</td><td>30</td></tr>"
            "</table>"
            "<p>Which statement <strong>best</strong> explains how this change in climate may influence human activity?</p>"
        ),
        "choices": [
            "As floods become more frequent, people may build sea walls, raise buildings, or move to higher ground, so where and how people live will change.",
            "Rising seas will not affect where people choose to live.",
            "The number of flood days is falling, so more people will move to the coast.",
            "Sea level rise only affects fish and has no effect on people.",
        ],
        "answer": 0,
        "feedback": "More frequent flooding increases cost and risk, which pushes people to adapt or relocate.",
    },
    {
        "title": "MC 7 - Reading city data",
        "dok": 2,
        "prompt": (
            "<p>A table gives information about four cities:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>City</th><th>Distance to nearest river or coast (km)</th><th>Yearly rainfall (mm)</th><th>Population (millions)</th></tr>"
            "<tr><td>P</td><td>2</td><td>900</td><td>6.0</td></tr>"
            "<tr><td>Q</td><td>5</td><td>800</td><td>4.5</td></tr>"
            "<tr><td>R</td><td>120</td><td>150</td><td>0.2</td></tr>"
            "<tr><td>S</td><td>90</td><td>200</td><td>0.4</td></tr>"
            "</table>"
            "<p>Which pattern is <strong>best supported</strong> by the data?</p>"
        ),
        "choices": [
            "The larger cities are close to a river or coast and have more rainfall, which suggests water access supports bigger populations.",
            "The larger cities are far from water and have little rainfall.",
            "Distance to water has no relationship to population.",
            "Every city has the same population.",
        ],
        "answer": 0,
        "feedback": "Cities P and Q have both the nearest water and the most rainfall, and the two largest populations.",
    },
    {
        "title": "MC 8 - Is safety the only reason?",
        "dok": 3,
        "prompt": (
            "<p>A student claims, &ldquo;People always choose to live in the safest places.&rdquo; Three pieces of evidence are given:</p>"
            "<ul>"
            "<li>Millions of people farm on the slopes of active volcanoes, where volcanic ash makes the soil very fertile.</li>"
            "<li>Large cities exist on hurricane-prone coasts that have busy ports.</li>"
            "<li>Many people live on river flood plains that flood every few years but have good farmland.</li>"
            "</ul>"
            "<p>Which statement <strong>best</strong> evaluates the claim?</p>"
        ),
        "choices": [
            "The claim is not supported: people often choose places with hazards when natural resources such as fertile soil and ports give strong benefits.",
            "The claim is supported: all of these places are safe.",
            "The claim is supported: natural hazards do not exist in these places.",
            "The claim cannot be tested with evidence.",
        ],
        "answer": 0,
        "feedback": "In all three examples, people accept hazards to use the resources of the place.",
    },
]

FREE_RESPONSE = [
    {
        "title": "FR 1 - Life in a river delta",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>A river delta is low, flat land where a river meets the sea. Scientists compare a delta region with a nearby highland region:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th></th><th>Delta</th><th>Highlands</th></tr>"
            "<tr><td>People per km<sup>2</sup></td><td>1,100</td><td>90</td></tr>"
            "<tr><td>Rice harvested (tons per hectare)</td><td>4.5</td><td>1.5</td></tr>"
            "<tr><td>Days with flooding each year</td><td>35</td><td>2</td></tr>"
            "<tr><td>Fresh water from river and groundwater (relative)</td><td>High</td><td>Low</td></tr>"
            "</table>"
            "<p>Sea level near the delta is rising about 4 mm each year.</p>"
            "<p>Write an explanation using <strong>Claim, Evidence, and Reasoning</strong>:</p>"
            "<ol>"
            "<li><strong>Claim:</strong> Explain why many more people live in the delta than in the highlands.</li>"
            "<li><strong>Evidence:</strong> Use at least <strong>two</strong> pieces of data.</li>"
            "<li><strong>Reasoning:</strong> Identify one natural resource, one natural hazard, and one climate change in the data. Explain how each may influence human activity in the delta in the future.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Accurate claim that the delta's resources (fertile land, fresh water) outweigh its flood hazard for many people. "
             "At least two accurate data points (1,100 versus 90 people per km&sup2;; 4.5 versus 1.5 tons of rice). "
             "Correctly identifies a resource (fresh water or fertile soil), a hazard (flooding), and a climate change (sea level rise). "
             "Explains an influence for each (food supply supports population; people build defenses or adapt crops to floods; rising seas may force people to relocate or change what they grow)."),
            (3, "Proficient",
             "Accurate claim and two data points. Identifies all three factors but explains the influence of only two, or the explanations are brief."),
            (2, "Developing",
             "Claim partly correct. One data point. Identifies one or two factors and gives little explanation."),
            (1, "Beginning",
             "Claim wrong or missing. Little or no data. Shows a major misconception (for example, people live in the delta because it has no hazards)."),
        ],
        "grading_notes": [
            "Resource: fresh water, fertile soil, or rice harvests. Hazard: flooding (35 days per year). Climate change: sea level rise (4 mm per year).",
            "Accept any reasonable future influence: relocation, building sea walls, salt-tolerant crops, raising houses, migration inland.",
            "Common misconception: hazards always make people leave an area.",
        ],
        "exemplar": (
            "Many more people live in the delta because its natural resources make food and water easy to get. The delta has 1,100 people per km&sup2; compared with 90 in the highlands, and it produces 4.5 tons of rice per hectare compared with 1.5, so it can feed far more people. "
            "The fresh water and fertile soil are resources that support farming. The flooding, 35 days per year, is a hazard, but it also renews the soil and people accept it because of the benefits. "
            "Sea level rise of 4 mm per year is a climate change that could make flooding worse, so people may build sea walls, grow salt-tolerant crops, or move inland over time."
        ),
    },
    {
        "title": "FR 2 - The story of Valley Town",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>Valley Town was founded in 1900 next to a river in a dry region. Here is a record of the town:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Year</th><th>1900</th><th>1950</th><th>2000</th><th>2020</th></tr>"
            "<tr><td>River flow (cubic meters per second)</td><td>90</td><td>85</td><td>60</td><td>40</td></tr>"
            "<tr><td>Population</td><td>5,000</td><td>30,000</td><td>120,000</td><td>100,000</td></tr>"
            "<tr><td>Main crop</td><td>Rice</td><td>Rice</td><td>Cotton</td><td>Drought-tolerant sorghum</td></tr>"
            "<tr><td>Years with damaging floods</td><td>4 in 10</td><td>3 in 10 (levees built)</td><td>1 in 10</td><td>0 in 10</td></tr>"
            "</table>"
            "<p>Write an explanation using <strong>Claim, Evidence, and Reasoning</strong>:</p>"
            "<ol>"
            "<li><strong>Claim:</strong> Explain how resources, hazards, and a changing climate shaped the town's history.</li>"
            "<li><strong>Evidence:</strong> Use at least <strong>three</strong> pieces of data from the table.</li>"
            "<li><strong>Reasoning:</strong> Explain why the town grew until 2000 and why the population then fell. Predict one thing the town might do next.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Accurate claim covering all three: the river as a resource that let the town grow, floods as a hazard that people reduced with levees, and a drying climate that lowered river flow, changed crops, and reduced the population. "
             "Cites at least three accurate data points from different rows. "
             "Explains that growth followed water and farming while flow was high, and that after 2000 less water forced changes (new crops, people leaving). "
             "Gives a reasonable prediction tied to the data (more drought-tolerant crops, water conservation, further decline in population)."),
            (3, "Proficient",
             "Accurate claim, three data points, and a reasonable explanation, but one of the three factors is missing or the prediction is weak."),
            (2, "Developing",
             "Claim partly correct. One or two data points. Explanation focuses on only one factor."),
            (1, "Beginning",
             "Claim wrong or missing. Little or no data. Shows a major misconception."),
        ],
        "grading_notes": [
            "Resource: river water. Hazard: floods, reduced by levees. Climate change: river flow falling from 90 to 40 suggests a drier climate.",
            "Accept any reasonable prediction that matches the data: more water conservation, new crops, population keeps falling, or moving to a different source of water.",
            "Common misconception: people leave only because of hazards, not because of resource decline.",
        ],
        "exemplar": (
            "Valley Town was shaped by a river resource, a flood hazard, and a drying climate. In 1900 the river flowed at 90 cubic meters per second, which supported rice farming, and the population grew from 5,000 in 1900 to 120,000 in 2000. "
            "Floods were a hazard (damaging floods in 4 years of 10), so people built levees and by 2000 floods happened in only 1 year in 10. "
            "By 2020 the river flow had fallen to 40, a sign of a drier climate, so farmers switched from rice and cotton to drought-tolerant sorghum, and the population fell to 100,000 as people left. "
            "The town may next use less water, grow even more drought-tolerant crops, or lose more people unless it finds a new water source."
        ),
    },
]
