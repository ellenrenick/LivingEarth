"""CFAs for HS-LS2-7 (unit 4.4): one short exit-ticket check per priority learning target.

Each CFA is worth 6 points. MC items list the correct choice FIRST (the builder shuffles).
LS2-7.4 and LS2-7.5 are rated DOK 4 by the department (depth work); their CFAs are written at DOK 3.
"""

STANDARD = "HS-LS2-7"
UNIT = "4.4"
UNIT_TITLE = "Solutions for Sustainability"

CFAS = [
    {
        "id": "LS2-7.1", "dok": 2,
        "lt": "I can explain how human activities like pollution and deforestation affect ecosystems and biodiversity.",
        "items": [
            {"prompt": "<p>How does deforestation usually affect biodiversity?</p>",
             "choices": ["It removes habitat, so fewer species can live there.", "It increases habitat for all species.", "It has no effect.", "It makes new species appear immediately."],
             "feedback": "Clearing forest removes habitat."},
            {"prompt": "<p>Fertilizer washing into a lake causes algae to grow too much. What happens next?</p>",
             "choices": ["The algae die and decompose, using up oxygen so fish may die.", "More oxygen is made and fish multiply.", "Nothing changes.", "The lake becomes clearer."],
             "feedback": "Decomposing algae use up oxygen."},
            {"prompt": "<p>Explain in 1 or 2 sentences how one human activity (such as pollution, a dam, or an invasive species) affects an ecosystem.</p>",
             "points": 2,
             "criteria": [(2, "Names an activity and a specific effect on the ecosystem or biodiversity."),
                          (1, "Names an activity or an effect, but they are not connected."),
                          (0, "Blank or incorrect.")],
             "exemplar": "A dam blocks salmon from swimming upstream to lay eggs, so the number of salmon drops."},
        ],
    },
    {
        "id": "LS2-7.2", "dok": 3,
        "lt": "I can design a solution, based on evidence, that reduces a human impact on the environment.",
        "items": [
            {"prompt": "<p>Which is the best first step in designing a solution to reduce a human impact?</p>",
             "choices": ["Use data to identify the biggest cause of the problem.", "Pick the cheapest idea.", "Pick the idea you like best.", "Ignore the data."],
             "feedback": "Designs should be based on evidence about the cause."},
            {"prompt": "<p>Farm runoff causes 60% of a lake's pollution and lawns cause 10%. Which design is most likely to help most?</p>",
             "choices": ["Reduce runoff from farms.", "Reduce runoff from lawns only.", "Do nothing.", "Add more fertilizer."],
             "feedback": "Targeting the biggest cause gives the biggest benefit."},
            {"prompt": "<p>A river has too much trash from storm drains. Describe a solution and the evidence you would use to choose it (2 sentences).</p>",
             "points": 2,
             "criteria": [(2, "Describes a solution that addresses the cause and cites the kind of evidence (data) that supports it."),
                          (1, "Describes a solution without evidence."),
                          (0, "Blank or incorrect.")],
             "exemplar": "I would put trash screens in storm drains, because counts show most trash enters the river through them."},
        ],
    },
    {
        "id": "LS2-7.3", "dok": 3,
        "lt": "I can judge whether a solution will work, and what it gains and costs.",
        "items": [
            {"prompt": "<p>A solution cuts pollution by 60% and costs $50,000. The goal is a 50% cut for under $100,000. What is the best judgment?</p>",
             "choices": ["It meets the goals.", "It does not meet either goal.", "It meets the cost but not the pollution goal.", "It meets the pollution goal but not the cost."],
             "feedback": "60% is at least 50%, and $50,000 is under $100,000."},
            {"prompt": "<p>A solution gives up some jobs but protects a forest. This is an example of a</p>",
             "choices": ["trade-off", "criterion", "constraint", "hypothesis"],
             "feedback": "A trade-off gives up one thing to gain another."},
            {"prompt": "<p>Solution A cuts pollution by 70% at $200,000. Solution B cuts it by 40% at $20,000. The goal is at least 50%. Which meets the goal, and what is its cost? (1 or 2 sentences)</p>",
             "points": 2,
             "criteria": [(2, "Chooses A and names the cost ($200,000) or the trade-off."),
                          (1, "Chooses A with no reasoning, or reasons without a choice."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Solution A meets the 50% goal, but it costs $200,000, which is the trade-off."},
        ],
    },
    {
        "id": "LS2-7.4", "dok": 4,
        "lt": "I can use feedback and new evidence to improve my solution.",
        "items": [
            {"prompt": "<p>A test shows a solution worked in two of three towns. What should the designers do?</p>",
             "choices": ["Find out why it failed in the third town and change the design.", "Stop all work.", "Ignore the third town.", "Repeat exactly the same design."],
             "feedback": "Evidence from a test should guide improvements."},
            {"prompt": "<p>Reviewers say your solution is too expensive. Which response is best?</p>",
             "choices": ["Look for a cheaper way to meet the same goal and test it.", "Ignore the feedback.", "Say the reviewers are wrong.", "Make the solution more expensive."],
             "feedback": "Feedback should be used to improve the design."},
            {"prompt": "<p>A new data set shows your solution works poorly in the dry season. Describe one change you would make and how you would check it (1 or 2 sentences).</p>",
             "points": 2,
             "criteria": [(2, "Describes a specific change tied to the new data and a way to check it."),
                          (1, "Gives a change without a way to check, or a vague change."),
                          (0, "Blank or incorrect.")],
             "exemplar": "I would add a way to store water for the dry season and then measure the results next dry season."},
        ],
    },
    {
        "id": "LS2-7.5", "dok": 4,
        "lt": "I can present and defend my solution with evidence.",
        "items": [
            {"prompt": "<p>Which is the strongest way to defend a solution?</p>",
             "choices": ["Use data about how well it works and its cost, and address a limit.", "Say it is the best.", "Say everyone likes it.", "Say it is natural."],
             "feedback": "Evidence and honesty about limits make a strong defense."},
            {"prompt": "<p>A classmate says your solution is too costly. Which reply uses evidence?</p>",
             "choices": ["It costs $40,000 and removes 70% of the pollution, which is cheaper per percent than the other options.", "It is a good idea.", "Costs do not matter.", "I do not have an answer."],
             "feedback": "Specific numbers support the defense."},
            {"prompt": "<p>In 2 sentences, defend a solution to reduce plastic in a stream. Use at least one piece of evidence.</p>",
             "points": 2,
             "criteria": [(2, "States the solution and supports it with evidence."),
                          (1, "States the solution without evidence."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Putting trash screens on storm drains will keep plastic out of the stream. In a test, screens caught 80% of the trash before it reached the stream."},
        ],
    },
]
