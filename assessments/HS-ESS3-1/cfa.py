"""CFAs for HS-ESS3-1 (unit 4.3): one short exit-ticket check per priority learning target.

Each CFA is worth 6 points. MC items list the correct choice FIRST (the builder shuffles).
"""

STANDARD = "HS-ESS3-1"
UNIT = "4.3"
UNIT_TITLE = "Earth Shaping Humanity"

CFAS = [
    {
        "id": "ESS3-1.1", "dok": 1,
        "lt": "I can name the resources, hazards, and climate factors that shape where people live.",
        "items": [
            {"prompt": "<p>Which is a natural <strong>resource</strong>?</p>",
             "choices": ["Fresh water", "An earthquake", "A hurricane", "A flood warning"],
             "feedback": "Fresh water is a resource people use."},
            {"prompt": "<p>Which is a natural <strong>hazard</strong>?</p>",
             "choices": ["A volcanic eruption", "Fertile soil", "A river", "Iron ore"],
             "feedback": "Volcanic eruptions can harm people."},
            {"prompt": "<p>Which change in <strong>climate</strong> can affect where people live?</p>",
             "choices": ["Rising sea level", "A new school", "A road", "A market"],
             "feedback": "Rising seas can flood coasts and push people to move."},
        ],
    },
    {
        "id": "ESS3-1.2", "dok": 2,
        "lt": "I can describe how resources like water and fertile soil are spread unevenly.",
        "items": [
            {"prompt": "<p>Resources such as fresh water are</p>",
             "choices": ["spread unevenly across Earth", "spread evenly everywhere", "found only in deserts", "not needed by people"],
             "feedback": "Resources are concentrated in some places."},
            {"prompt": "<p>Why do large river deltas often have many farms?</p>",
             "choices": ["Rivers deposit fertile soil and bring fresh water.", "They have no water.", "The soil is poor.", "They are always dry."],
             "feedback": "Deltas have fertile soil and water."},
            {"prompt": "<p>Region A has 8,000 and Region B has 400 cubic meters of fresh water per person each year. Describe in 1 sentence how this affects where people can live and farm.</p>",
             "points": 2,
             "criteria": [(2, "Says the water is uneven and Region B has less water for farming or cities, citing the numbers."),
                          (1, "Says the water is uneven without the effect on people."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Region B has only 400 cubic meters per person compared with 8,000 in Region A, so it can support less farming and fewer people."},
        ],
    },
    {
        "id": "ESS3-1.3", "dok": 2,
        "lt": "I can describe how hazards like earthquakes and floods affect where and how people live.",
        "items": [
            {"prompt": "<p>People who live in an earthquake zone often</p>",
             "choices": ["build earthquake-resistant buildings", "avoid all buildings", "never use the land", "ignore the hazard completely"],
             "feedback": "People adapt by building safer structures."},
            {"prompt": "<p>Why might people choose to live on a flood plain?</p>",
             "choices": ["The fertile soil and nearby water outweigh the flood risk for them.", "There are no floods.", "It is the highest land.", "The soil is poor."],
             "feedback": "People weigh benefits against risks."},
            {"prompt": "<p>Describe one way a hazard (such as a flood or earthquake) changes where or how people live.</p>",
             "points": 2,
             "criteria": [(2, "Describes a specific change, such as moving, building differently, or avoiding the hazard zone, and links it to the hazard."),
                          (1, "Names an effect without linking it to the hazard."),
                          (0, "Blank or incorrect.")],
             "exemplar": "In earthquake zones, people build with stronger materials, and after floods some people move to higher ground."},
        ],
    },
    {
        "id": "ESS3-1.4", "dok": 2,
        "lt": "I can explain how climate change can move people and change what they grow.",
        "items": [
            {"prompt": "<p>If a region becomes much drier, farmers may</p>",
             "choices": ["switch to crops that need less water or move away", "grow more water-loving crops", "stop eating", "not change anything"],
             "feedback": "Climate changes push farmers to adapt or leave."},
            {"prompt": "<p>Sea level rise can push people to leave coastal areas because</p>",
             "choices": ["more land floods more often", "oceans shrink", "the land rises", "storms stop"],
             "feedback": "Higher seas flood low-lying land."},
            {"prompt": "<p>Explain in 1 or 2 sentences how a hotter, drier climate could change what a region grows and where people live.</p>",
             "points": 2,
             "criteria": [(2, "Links the climate change to crops and to people moving or staying."),
                          (1, "Gives one of the two."),
                          (0, "Blank or incorrect.")],
             "exemplar": "A hotter, drier climate means farmers must grow crops that need less water, and some people may move to places with more water."},
        ],
    },
    {
        "id": "ESS3-1.5", "dok": 2,
        "lt": "I can read maps and data that connect resources, hazards, or climate to human activity.",
        "items": [
            {"prompt": "<table border=\"1\" cellpadding=\"4\"><tr><th>City</th><th>Distance to river (km)</th><th>Population (millions)</th></tr><tr><td>A</td><td>1</td><td>5</td></tr><tr><td>B</td><td>80</td><td>0.3</td></tr></table><p>What does the table suggest?</p>",
             "choices": ["Cities near a river tend to be larger.", "Cities far from rivers are larger.", "Distance does not matter.", "Both have equal populations."],
             "feedback": "The city by the river has more people."},
            {"prompt": "<p>A map shows most large cities along coasts and rivers. This suggests</p>",
             "choices": ["people settle where water and transport are available", "people avoid water", "cities are placed at random", "rivers cause cities to disappear"],
             "feedback": "Water and trade routes support settlement."},
            {"prompt": "<p>Use the table above to write one sentence connecting a resource to human activity. Include a number.</p>",
             "points": 2,
             "criteria": [(2, "Connects the river resource to the larger population with a number."),
                          (1, "Connects without a number."),
                          (0, "Blank or incorrect.")],
             "exemplar": "City A is 1 km from a river and has 5 million people, while City B is 80 km away and has only 0.3 million."},
        ],
    },
    {
        "id": "ESS3-1.6", "dok": 3,
        "lt": "I can use evidence to explain how resources, hazards, and climate have shaped human activity.",
        "items": [
            {"prompt": "<p>Which statement best uses evidence to explain why a city grew near a volcano?</p>",
             "choices": ["Volcanic ash made the soil fertile, so farming supported many people despite the eruption hazard.", "Volcanoes never erupt.", "Nobody lives near volcanoes.", "People enjoy danger."],
             "feedback": "The benefit of fertile soil outweighs the hazard for many people."},
            {"prompt": "<p>A drought cut a river's flow in half and the town lost half its farms. What does this show?</p>",
             "choices": ["A change in climate and resources can change human activity.", "Rivers do not matter.", "Farms never depend on water.", "The town did not change."],
             "feedback": "Less water led to fewer farms."},
            {"prompt": "<p>Choose a place (real or from class). In 2 or 3 sentences, use one resource, one hazard, and one climate factor to explain how people live there.</p>",
             "points": 2,
             "criteria": [(2, "Names all three accurately and links each to what people do."),
                          (1, "Names two, or names three without linking."),
                          (0, "Blank or incorrect.")],
             "exemplar": "In a river delta, fertile soil and water (resources) let people farm. Floods (a hazard) happen yearly, so people build raised homes, and sea level rise (a climate change) may force some to move."},
        ],
    },
]
