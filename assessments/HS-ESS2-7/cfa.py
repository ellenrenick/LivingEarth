"""CFAs for HS-ESS2-7 (unit 3.2): one short exit-ticket check per priority learning target.

Each CFA is worth 6 points. MC items list the correct choice FIRST (the builder shuffles).
ESS2-7.5 is DOK 4 (depth work); its CFA stops at DOK 3 like the CSA.
"""

STANDARD = "HS-ESS2-7"
UNIT = "3.2"
UNIT_TITLE = "Changing Earth, Changing Life"

CFAS = [
    {
        "id": "ESS2-7.1", "dok": 1,
        "lt": "I can name examples of how Earth has changed and how life has changed.",
        "items": [
            {"prompt": "<p>Which is an example of how <strong>Earth</strong> has changed over time?</p>",
             "choices": ["The atmosphere gained oxygen.", "A frog laid eggs.", "A student read a book.", "A tree grew a new leaf."],
             "feedback": "The atmosphere gaining oxygen is a change in Earth's systems."},
            {"prompt": "<p>Which is an example of how <strong>life</strong> has changed over time?</p>",
             "choices": ["Large animals evolved after oxygen increased.", "The Sun rose in the east.", "A river changed course in one flood.", "Rock cooled and hardened."],
             "feedback": "The evolution of animals is a change in life."},
            {"prompt": "<p>Photosynthetic microbes have been on Earth for billions of years. They are part of which Earth system?</p>",
             "choices": ["Biosphere", "Atmosphere", "Geosphere only", "Hydrosphere only"],
             "feedback": "Living things make up the biosphere."},
        ],
    },
    {
        "id": "ESS2-7.2", "dok": 2,
        "lt": "I can describe one way Earth changed life and one way life changed Earth.",
        "items": [
            {"prompt": "<p>Which is an example of <strong>life changing Earth</strong>?</p>",
             "choices": ["Photosynthetic microbes added oxygen to the atmosphere.", "A volcano erupted.", "Ice formed at the poles.", "A meteor hit the planet."],
             "feedback": "Photosynthesis by living things changed the atmosphere."},
            {"prompt": "<p>Which is an example of <strong>Earth changing life</strong>?</p>",
             "choices": ["An ice age changed where plants and animals could live.", "Plants made soil.", "Corals built a reef.", "Microbes made oxygen."],
             "feedback": "An ice age is an Earth change that affected life."},
            {"prompt": "<p>Describe one way life changed Earth and one way Earth changed life (1 or 2 sentences).</p>",
             "points": 2,
             "criteria": [(2, "Gives one correct way in each direction."),
                          (1, "Gives one correct way in only one direction."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Life changed Earth when photosynthetic microbes added oxygen to the air. Earth changed life when a colder climate caused many species to die out."},
        ],
    },
    {
        "id": "ESS2-7.3", "dok": 3,
        "lt": "I can explain how events in Earth's history changed life, and how life in turn changed Earth.",
        "items": [
            {"prompt": "<p>Which is a correct chain of cause and effect?</p>",
             "choices": ["Microbes added oxygen &rarr; the atmosphere changed &rarr; oxygen-using animals evolved.", "Animals evolved &rarr; oxygen was removed &rarr; microbes appeared.",
                         "Oxygen appeared &rarr; microbes disappeared &rarr; the atmosphere stayed the same.", "Rocks formed &rarr; microbes stopped living."],
             "feedback": "Life changed the atmosphere, and the new atmosphere made new life possible."},
            {"prompt": "<p>After a big asteroid hit Earth, many large animals died out. Small mammals later became many new species. Which explanation is best?</p>",
             "choices": ["The impact changed the climate, which caused extinctions, and survivors evolved to fill open habitats.", "The mammals caused the impact.",
                         "The extinction had no connection to the impact.", "The climate stayed the same."],
             "feedback": "An Earth event changed conditions and changed life."},
            {"prompt": "<p>In 2 or 3 sentences, explain how an event in Earth's history changed life <em>and</em> how that change in life then changed Earth.</p>",
             "points": 2,
             "criteria": [(2, "Describes an Earth event that changed life and a change in life that then changed Earth, linked in sequence."),
                          (1, "Describes only one direction, or the two directions are not linked."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Early Earth had little oxygen, which allowed microbes to flourish. Their photosynthesis then added oxygen to the air, changing the atmosphere so oxygen-using life could evolve."},
        ],
    },
    {
        "id": "ESS2-7.4", "dok": 3,
        "lt": "I can write an argument, with evidence, that Earth and life changed each other.",
        "items": [
            {"prompt": "<table border=\"1\" cellpadding=\"4\"><tr><th>Site</th><th>Plants present?</th><th>Soil depth (cm)</th></tr><tr><td>A</td><td>No</td><td>0</td></tr><tr><td>B</td><td>Yes</td><td>20</td></tr></table><p>Which claim does the data best support?</p>",
             "choices": ["Plants help form soil.", "Soil forms only without plants.", "Plants and soil are unrelated.", "Soil makes plants disappear."],
             "feedback": "Soil is deeper where plants live."},
            {"prompt": "<p>A strong argument includes</p>",
             "choices": ["a claim, evidence, and reasoning that links them", "only an opinion", "only evidence with no claim", "a claim with no evidence"],
             "feedback": "Arguments need a claim, evidence, and reasoning."},
            {"prompt": "<p>Use the table above to write a claim, one piece of evidence, and one sentence of reasoning.</p>",
             "points": 2,
             "criteria": [(2, "Has a claim, accurate evidence from the table, and reasoning that links them."),
                          (1, "Has two of the three parts, or the reasoning does not connect."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Claim: Plants help form soil. Evidence: Site B has plants and 20 cm of soil, but Site A has none and 0 cm. Reasoning: Plants break down rock and add material, so soil builds up where they live."},
        ],
    },
    {
        "id": "ESS2-7.5", "dok": 3,
        "lt": "I can combine several kinds of evidence into one strong argument about Earth and life.",
        "items": [
            {"prompt": "<p>Which set of evidence gives the <strong>strongest</strong> argument that life changed the atmosphere?</p>",
             "choices": ["Fossils of oxygen-making microbes, rock chemistry showing oxygen rising, and rusted iron layers", "A single fossil", "A story with no data", "The color of the sky today"],
             "feedback": "Strong arguments combine independent kinds of evidence."},
            {"prompt": "<p>When two kinds of evidence agree, the conclusion is usually</p>",
             "choices": ["stronger", "weaker", "unrelated", "impossible"],
             "feedback": "Independent evidence that agrees strengthens a conclusion."},
            {"prompt": "<p>Name two different kinds of evidence (such as fossils, rock chemistry, or climate records) and say what each tells you about Earth and life changing together.</p>",
             "points": 2,
             "criteria": [(2, "Names two kinds of evidence and states what each shows."),
                          (1, "Names two kinds without saying what they show, or states what one shows."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Fossils show what kinds of life lived at a time, and rock chemistry shows what the atmosphere was like. Together they show life and the atmosphere changed together."},
        ],
    },
    {
        "id": "ESS2-7.6", "dok": 3,
        "lt": "I can argue from evidence that Earth's systems and life have changed together over time.",
        "items": [
            {"prompt": "<p>Which statement is best supported by the evidence that Earth and life have changed together?</p>",
             "choices": ["Changes in the atmosphere, rocks, and living things happened at related times and affected each other.", "Earth and life are unrelated.",
                         "Life changed but Earth did not.", "Earth changed but life did not."],
             "feedback": "The record shows related, two-way changes."},
            {"prompt": "<p>A feedback in which life builds soil, and soil supports more life, shows that</p>",
             "choices": ["life and Earth can change each other repeatedly", "soil never changes", "life does not affect the ground", "feedbacks do not exist"],
             "feedback": "Feedbacks show Earth and life changing each other."},
            {"prompt": "<p>Write 2 or 3 sentences arguing that Earth's systems and life changed together. Use one example and one piece of evidence.</p>",
             "points": 2,
             "criteria": [(2, "Claim plus an accurate example and evidence showing change in both Earth and life."),
                          (1, "Claim and an example without evidence, or evidence for only one side."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Earth and life changed together. Photosynthetic microbes added oxygen to the air, and rock layers show rust forming worldwide as oxygen rose. Later, animals that need oxygen evolved."},
        ],
    },
]
