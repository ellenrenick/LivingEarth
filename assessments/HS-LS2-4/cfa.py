"""CFAs for HS-LS2-4 (unit 4.1): one short exit-ticket check per priority learning target.

Each CFA is worth 6 points. MC items list the correct choice FIRST (the builder shuffles).
Assessment boundary: proportional reasoning only.
"""

STANDARD = "HS-LS2-4"
UNIT = "4.1"
UNIT_TITLE = "Cycles of Life"

CFAS = [
    {
        "id": "LS2-4.1", "dok": 1,
        "lt": "I can name producers, consumers, and decomposers and the role of each.",
        "items": [
            {"prompt": "<p>Which organism is a <strong>producer</strong>?</p>",
             "choices": ["A tree", "A deer", "A mushroom", "A hawk"],
             "feedback": "Producers make their own food from sunlight."},
            {"prompt": "<p>A decomposer</p>",
             "choices": ["breaks down dead organisms and returns matter to the environment", "makes food from sunlight", "hunts living animals", "stores energy as heat"],
             "feedback": "Decomposers recycle matter from dead organisms."},
            {"prompt": "<p>A consumer gets energy by</p>",
             "choices": ["eating other organisms", "absorbing sunlight", "making sugar from carbon dioxide", "breaking down rocks"],
             "feedback": "Consumers eat other organisms."},
        ],
    },
    {
        "id": "LS2-4.2", "dok": 2,
        "lt": "I can describe how matter cycles and energy flows through a food web.",
        "items": [
            {"prompt": "<p>Which statement is true?</p>",
             "choices": ["Matter cycles through an ecosystem, and energy flows through it and leaves as heat.", "Energy cycles and matter flows out.", "Neither matter nor energy moves.", "Matter is used up and energy is recycled."],
             "feedback": "Matter cycles; energy flows one way."},
            {"prompt": "<p>Where does the energy for almost all ecosystems come from?</p>",
             "choices": ["The Sun", "Decomposers", "Rocks", "The ocean floor only"],
             "feedback": "Producers capture the Sun's energy and it flows to consumers."},
            {"prompt": "<p>Describe in 1 or 2 sentences how energy and matter move differently through a food web.</p>",
             "points": 2,
             "criteria": [(2, "Says matter is reused/cycled and energy flows one way and is lost as heat."),
                          (1, "Describes one of them correctly."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Matter, such as carbon, is passed along and returned to the soil and air by decomposers. Energy flows one way from the Sun through the food web and is lost as heat."},
        ],
    },
    {
        "id": "LS2-4.3", "dok": 3,
        "lt": "I can interpret energy pyramids and matter diagrams, including the 10 percent rule.",
        "items": [
            {"prompt": "<p>In an energy pyramid, why is each level smaller than the one below it?</p>",
             "choices": ["Most of the energy is used by organisms or lost as heat, so only about 10% passes on.", "Organisms at higher levels do not need energy.", "Energy is created at the bottom.", "Higher levels eat all of the level below."],
             "feedback": "About 10% of the energy is passed to the next level."},
            {"prompt": "<table border=\"1\" cellpadding=\"4\"><tr><th>Level</th><th>Energy (kJ)</th></tr><tr><td>Producers</td><td>5,000</td></tr><tr><td>Primary consumers</td><td>500</td></tr><tr><td>Secondary consumers</td><td>50</td></tr></table><p>What does the pyramid show about the secondary consumers compared with producers?</p>",
             "choices": ["They receive about 1% as much energy.", "They receive the same energy.", "They receive 10 times as much.", "They receive no energy."],
             "feedback": "50 / 5,000 = 1%."},
            {"prompt": "<p>A diagram shows carbon moving from air to a plant to a rabbit to a fox to decomposers and back to the air. In 1 or 2 sentences, explain what this diagram shows about matter.</p>",
             "points": 2,
             "criteria": [(2, "Says the same carbon atoms are passed along and returned, so matter cycles."),
                          (1, "Says carbon moves but not that it returns or is conserved."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Carbon atoms are passed from the air to the plant to animals, and decomposers return them to the air, so matter cycles and is reused."},
        ],
    },
    {
        "id": "LS2-4.4", "dok": 2,
        "lt": "I can use numbers to show how much energy passes from one level to the next.",
        "items": [
            {"prompt": "<p>Grass stores 2,000 kJ. About how much energy is stored in the primary consumers that eat the grass (10% rule)?</p>",
             "choices": ["200 kJ", "20 kJ", "1,800 kJ", "2,000 kJ"],
             "feedback": "10% of 2,000 is 200."},
            {"prompt": "<p>A level stores 1,000 kJ and the next level stores 80 kJ. What percent of the energy was passed on?</p>",
             "choices": ["8%", "80%", "0.8%", "12.5%"],
             "feedback": "80 / 1,000 = 0.08 = 8%."},
            {"prompt": "<p>Producers store 40,000 kJ. Show the energy stored in the next <strong>two</strong> levels using the 10% rule. Write the numbers and a one-sentence conclusion.</p>",
             "points": 2,
             "criteria": [(2, "Shows 4,000 and 400 kJ and concludes that energy drops by about 90% at each level."),
                          (1, "One value correct, or values with no conclusion."),
                          (0, "Blank or incorrect.")],
             "exemplar": "40,000 x 0.10 = 4,000 kJ in the next level, and 4,000 x 0.10 = 400 kJ in the level after. Most of the energy is not passed on at each step."},
        ],
    },
    {
        "id": "LS2-4.5", "dok": 3,
        "lt": "I can use numbers to show that matter is conserved as it cycles.",
        "items": [
            {"prompt": "<table border=\"1\" cellpadding=\"4\"><tr><th></th><th>Air</th><th>Plants</th><th>Soil</th></tr><tr><td>Start (carbon units)</td><td>50</td><td>30</td><td>20</td></tr><tr><td>End (carbon units)</td><td>40</td><td>38</td><td>22</td></tr></table><p>Which conclusion fits the numbers?</p>",
             "choices": ["The total is 100 at the start and the end, so carbon is conserved.", "Carbon was created in the plants.", "Carbon was destroyed in the air.", "The totals are different."],
             "feedback": "50 + 30 + 20 = 100 and 40 + 38 + 22 = 100."},
            {"prompt": "<p>If matter is conserved in a closed ecosystem, the total amount of an element in all parts should</p>",
             "choices": ["stay the same", "increase over time", "decrease over time", "be zero"],
             "feedback": "Matter is not created or destroyed."},
            {"prompt": "<p>Air has 70 units of carbon, producers 20, and soil 10. Later, air has 62 and soil 12. How many units must the producers now have if matter is conserved? Show your math.</p>",
             "points": 2,
             "criteria": [(2, "Total 100; 100 - 62 - 12 = 26; answers 26 with work."),
                          (1, "Correct method with an arithmetic error, or 26 with no work."),
                          (0, "Blank or incorrect.")],
             "exemplar": "The total is 70 + 20 + 10 = 100. Now air has 62 and soil 12, so producers have 100 - 62 - 12 = 26 units."},
        ],
    },
    {
        "id": "LS2-4.6", "dok": 3,
        "lt": "I can use math to support a claim about how matter cycles and energy flows.",
        "items": [
            {"prompt": "<p>Which statement is a claim supported by math?</p>",
             "choices": ["Only about 10% of energy passes to the next level, since 500 kJ of 5,000 kJ was passed on.", "Energy seems to be passed on.", "Most energy probably goes somewhere.", "Ecosystems are important."],
             "feedback": "A claim supported by math cites numbers."},
            {"prompt": "<p>A food chain has producers at 10,000 kJ. A student claims the top consumer level can get 5,000 kJ. Which response is best?</p>",
             "choices": ["The claim is not supported: with the 10% rule each level has much less, so three levels up would have about 10 kJ.", "The claim is supported.", "The claim is supported because top levels get the most energy.", "The 10% rule does not apply."],
             "feedback": "10,000 x 0.1 x 0.1 x 0.1 = 10 kJ."},
            {"prompt": "<p>Make a claim about energy in a food chain and support it with a calculation (2 or 3 sentences).</p>",
             "points": 2,
             "criteria": [(2, "States a claim and supports it with a correct calculation."),
                          (1, "Claim without a calculation, or a calculation without a claim."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Claim: Energy decreases at each level. If producers store 20,000 kJ, the next level stores about 2,000 kJ, and the one after about 200 kJ, since about 10% passes on each time."},
        ],
    },
]
