"""Question bank for the HS-LS1-2 CSA: Organization in Organisms (unit 1.1).

45-minute test, 30 points. Edit this file, then run `python3 ../build_unit.py HS-LS1-2`.
Boundary: no interactions or functions at the molecular or chemical-reaction level.
"""

TITLE = "HS-LS1-2 Assessment: Organization in Organisms"
STANDARD = "HS-LS1-2"
QUIZ_ID = "hs_ls1_2_organization"
FILE_PREFIX = "HS-LS1-2"
MAX_ATTEMPTS = 1
TIME_MINUTES = 45
KEY_POSITIONS = [1, 3, 0, 2, 1, 0, 3, 2]

DESCRIPTION = (
    "<p><strong>Living Earth (Biology) &ndash; HS-LS1-2</strong></p>"
    "<p>Develop and use a model to illustrate the hierarchical organization of "
    "interacting systems that provide specific functions within multicellular organisms.</p>"
    "<p>Part 1: Vocabulary matching &middot; Part 2: Multiple choice &middot; Part 3: Free response</p>"
)

MATCHING = {
    "title": "Part 1: Vocabulary Matching",
    "points": 6,
    "prompt": "<p>Match each term with its best definition. Some definitions will not be used.</p>",
    "pairs": [
        ("Cell", "The basic unit of structure and function in all living things"),
        ("Tissue", "A group of similar cells that work together to do a specific job"),
        ("Organ", "A structure made of different tissues that work together to perform a specific function"),
        ("Organ system", "A group of organs that work together to carry out a major function for the body"),
        ("Organism", "A complete living thing, made of one cell or of many organ systems working together"),
        ("Structure and function", "The idea that the shape and makeup of a part fit the job that part does"),
    ],
    "distractors": [
        "The process by which one cell divides to make two new cells",
        "All the living things of one kind that live in the same area",
    ],
}

MULTIPLE_CHOICE = [
    {
        "title": "MC 1 - Slide of the stomach lining",
        "dok": 2,
        "prompt": (
            "<p>A student looks at a microscope slide of the inner lining of a stomach. "
            "She sees many similar cells packed side by side in a sheet, and they all "
            "make and release the same digestive fluid.</p>"
            "<p>Which level of organization does this sheet of cells <strong>best</strong> represent?</p>"
        ),
        "choices": [
            "A tissue, because it is a group of similar cells working together to do one job",
            "An organ, because it is made of many cells",
            "An organ system, because it releases a fluid for digestion",
            "An organism, because it is alive and carries out a function",
        ],
        "answer": 0,
        "feedback": "A group of similar cells that work together at one job is a tissue. An organ needs several different tissues.",
    },
    {
        "title": "MC 2 - Building up from cells",
        "dok": 2,
        "prompt": (
            "<p>A teacher gives students these parts of a human body: <em>small intestine</em>, "
            "<em>digestive system</em>, <em>muscle cell</em>, <em>smooth muscle tissue</em>, "
            "<em>human</em>.</p>"
            "<p>Which list puts them in order from the <strong>smallest</strong> level to the "
            "<strong>largest</strong> level?</p>"
        ),
        "choices": [
            "Muscle cell, smooth muscle tissue, small intestine, digestive system, human",
            "Smooth muscle tissue, muscle cell, small intestine, digestive system, human",
            "Muscle cell, small intestine, smooth muscle tissue, human, digestive system",
            "Human, digestive system, small intestine, smooth muscle tissue, muscle cell",
        ],
        "answer": 0,
        "feedback": "Cells build tissues, tissues build organs, organs build organ systems, and organ systems build the organism.",
    },
    {
        "title": "MC 3 - What kind of structure is the heart?",
        "dok": 2,
        "prompt": (
            "<p>The heart contains cardiac muscle tissue that squeezes, connective tissue that "
            "holds it together, and nervous tissue that helps control the beat. Together these "
            "tissues pump blood through the body.</p>"
            "<p>Which statement <strong>best</strong> describes how the levels of organization "
            "are related in this example?</p>"
        ),
        "choices": [
            "The heart is an organ because several different tissues work together to do one job, and it is one part of the circulatory system.",
            "The heart is a tissue because it is made of cells, and the circulatory system is made of many hearts.",
            "The heart is an organ system because it has more than one kind of tissue.",
            "The heart is a single giant cell that contains muscle, connective, and nervous parts.",
        ],
        "answer": 0,
        "feedback": "An organ is made of different tissues working together. The heart is one organ in the circulatory system.",
    },
    {
        "title": "MC 4 - Folds in the small intestine",
        "dok": 2,
        "prompt": (
            "<p>The inner wall of the small intestine is covered with millions of tiny finger-like "
            "folds. The folds make the wall's surface area very large. Digested food passes "
            "through the wall into the blood.</p>"
            "<p>Which claim <strong>best</strong> connects the structure to the function?</p>"
        ),
        "choices": [
            "The folds give the wall a large surface, so more digested food can pass into the blood at one time.",
            "The folds make the small intestine shorter, so food moves through it faster.",
            "The folds are decorations; the wall would work the same way if it were smooth.",
            "The folds make the small intestine part of the respiratory system instead of the digestive system.",
        ],
        "answer": 0,
        "feedback": "Structure fits function: a larger surface area lets more nutrients be taken in. The small intestine stays in the digestive system.",
    },
    {
        "title": "MC 5 - A sprint across the field",
        "dok": 3,
        "prompt": (
            "<p>A soccer player sprints for the ball. Within seconds, her breathing speeds up, her "
            "heart beats faster, and her leg muscles contract again and again.</p>"
            "<p>Which explanation <strong>best</strong> describes how organ systems interact?</p>"
        ),
        "choices": [
            "The nervous system senses the need for more effort and signals the others; the respiratory system takes in more air, and the circulatory system moves blood faster to carry that air to the working muscles.",
            "The muscular system works alone; the respiratory and circulatory systems keep the same pace because they do not depend on the muscles.",
            "The circulatory system makes the muscles contract, and the nervous system moves blood to the lungs.",
            "The respiratory system pushes blood around the body, so the heart is not needed during a sprint.",
        ],
        "answer": 0,
        "feedback": "Systems depend on each other. The nervous system coordinates, the respiratory system brings in air, and the circulatory system delivers it to the muscular system.",
    },
    {
        "title": "MC 6 - Evidence from three organisms",
        "dok": 2,
        "prompt": (
            "<p>A class collects information about four organisms:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Organism</th><th>Number of cells</th><th>Takes in food</th><th>Grows</th><th>Reproduces</th></tr>"
            "<tr><td>Bacterium</td><td>1</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>"
            "<tr><td>Yeast</td><td>1</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>"
            "<tr><td>Oak tree</td><td>Billions</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>"
            "<tr><td>Human</td><td>Trillions</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>"
            "</table>"
            "<p>Which conclusion is <strong>best supported</strong> by this table?</p>"
        ),
        "choices": [
            "Every organism listed is made of at least one cell, and one cell can carry out the functions of life by itself.",
            "Only organisms with many cells can take in food, grow, and reproduce.",
            "Organisms with more cells always grow faster than organisms with fewer cells.",
            "Single-celled organisms are not living because they have no tissues.",
        ],
        "answer": 0,
        "feedback": "All four organisms carry out the functions of life, including the two with only one cell. The cell is the basic unit of life.",
    },
    {
        "title": "MC 7 - A damaged artery",
        "dok": 3,
        "prompt": (
            "<p>The wall of an artery has elastic tissue that stretches and springs back and smooth "
            "muscle tissue that narrows or widens the artery. Together they help the artery "
            "regulate how much blood reaches each part of the body.</p>"
            "<p>A patient's artery has lost most of its elastic tissue. Which prediction is "
            "<strong>best supported</strong> by what you know about levels of organization?</p>"
        ),
        "choices": [
            "The artery will have trouble regulating blood flow, so the circulatory system will deliver blood less effectively to the organs that depend on it.",
            "Nothing will change, because an organ does not depend on its tissues to do its job.",
            "The artery will become part of the nervous system, which will take over regulating blood flow.",
            "Only the single cells in the artery wall will be affected; the circulatory system will work the same way.",
        ],
        "answer": 0,
        "feedback": "An organ works because its tissues work together. Damage to one tissue affects the organ, and a damaged organ affects the system and the organs that depend on it.",
    },
    {
        "title": "MC 8 - Revising a student's model",
        "dok": 3,
        "prompt": (
            "<p>A student drew a model of the levels of organization and wrote this explanation:</p>"
            "<blockquote>&ldquo;An organism is made of organ systems. Organ systems are made of "
            "tissues. Tissues are made of organs. Organs are made of cells.&rdquo;</blockquote>"
            "<p>Which revision <strong>correctly</strong> fixes the model?</p>"
        ),
        "choices": [
            "An organism is made of organ systems, organ systems are made of organs, organs are made of tissues, and tissues are made of cells.",
            "An organism is made of cells, cells are made of tissues, tissues are made of organs, and organs are made of organ systems.",
            "An organism is made of organs, organs are made of organ systems, organ systems are made of tissues, and tissues are made of cells.",
            "No change is needed, because the levels can be listed in any order.",
        ],
        "answer": 0,
        "feedback": "Each level is built from the level below it: cells, then tissues, organs, organ systems, and the organism.",
    },
]

FREE_RESPONSE = [
    {
        "title": "FR 1 - Water for a tall tree",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>A plant biologist studies two young maple trees of the same age. Both get the same "
            "light and soil water. Tree B had part of its root system damaged by a fungus.</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Measurement after 4 weeks</th><th>Tree A (healthy roots)</th><th>Tree B (damaged roots)</th></tr>"
            "<tr><td>Water taken up each day (mL)</td><td>240</td><td>70</td></tr>"
            "<tr><td>Leaves that are wilted (%)</td><td>5</td><td>60</td></tr>"
            "<tr><td>New height growth (cm)</td><td>12</td><td>2</td></tr>"
            "</table>"
            "<p>Write an explanation using <strong>Claim, Evidence, and Reasoning</strong>:</p>"
            "<ol>"
            "<li><strong>Claim:</strong> Explain why damage to the roots affected the whole tree.</li>"
            "<li><strong>Evidence:</strong> Use at least <strong>two</strong> pieces of data from the table.</li>"
            "<li><strong>Reasoning:</strong> Explain how the levels of organization (cells, tissues, organs, organ systems) and the interacting systems of a plant (the root system and the shoot system of stems and leaves) provide the function of water delivery. Include one way a structure fits its function.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Accurate claim that damage to one organ system (roots) reduced a function the whole organism depends on. "
             "Cites at least two accurate data points and links them (less water taken up, so more wilting and less growth). "
             "Reasoning builds the hierarchy correctly (cells form tissues, tissues form organs such as roots and leaves, organs form systems such as the root system and shoot system) and explains that the systems depend on each other to deliver water. "
             "Gives a correct structure-function example (for example, root hairs give a large surface for taking in water, or tube-like tissue carries water upward)."),
            (3, "Proficient",
             "Accurate claim and two accurate data points. "
             "Reasoning names the levels or the interacting systems correctly but leaves out one piece (for example, no structure-function example or the levels are named without showing how each builds on the one below)."),
            (2, "Developing",
             "Claim is partly correct (for example, \"the roots matter\") without linking to the whole tree. "
             "One data point, or data used inaccurately. Reasoning is vague or lists levels in the wrong order."),
            (1, "Beginning",
             "Claim is wrong or missing. Little or no data. Reasoning is missing or shows a major misconception (for example, treats a tissue as larger than an organ)."),
        ],
        "grading_notes": [
            "Look for: roots take in water; the water is carried up to the leaves; the root system and shoot system depend on each other; a damaged part lowers the function of the whole organism.",
            "Key data: water uptake 240 vs. 70 mL, wilted leaves 5% vs. 60%, growth 12 vs. 2 cm.",
            "Accept any correct structure-function example (root hairs, tube-like water-carrying tissue, flat leaf shape). Do not require the words xylem or phloem.",
            "Do not require anything at the molecular or chemical level; it is outside the HS-LS1-2 assessment boundary. Do not take points off for leaving it out.",
            "Common misconception: a tissue is bigger than an organ, or an organ system is a single organ.",
        ],
        "exemplar": (
            "Damage to the roots affected the whole tree because the roots are the organ system that takes in the water the rest of the tree needs. "
            "Tree B took up only 70 mL of water a day compared with 240 mL for Tree A, and 60% of its leaves were wilted compared with 5%, so it grew only 2 cm instead of 12 cm. "
            "In a plant, cells make up tissues, such as the tissue that carries water. Different tissues make up organs, such as roots, stems, and leaves, and the organs work as systems. "
            "The root system takes in water, and the shoot system uses that water in the leaves, so each depends on the other. "
            "A root's structure fits its function: root hairs give it a large surface for taking in water. When the roots are damaged, less water reaches the leaves and the whole organism suffers."
        ),
    },
    {
        "title": "FR 2 - Pulling away from a hot pan",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>A student touches a hot pan and pulls her hand away before she even says &ldquo;ouch.&rdquo; "
            "Her reaction needed several organ systems working together.</p>"
            "<p>Describe a <strong>model</strong> (use words and arrows, such as &ldquo;A &rarr; B&rdquo;) that explains this response. Your model must:</p>"
            "<ol>"
            "<li>Name at least <strong>three</strong> organ systems and say what each one does in the reaction.</li>"
            "<li>Show, with arrows, how the systems interact in order, starting with the hot pan.</li>"
            "<li>Show the levels of organization for <strong>one</strong> of the systems by naming a cell, a tissue, an organ, and the organ system it belongs to.</li>"
            "<li>Explain how one structure in your model fits the function it performs.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Names at least three systems (for example, nervous, muscular, skeletal) with a correct role for each. "
             "The arrows show a correct order (stimulus, nerve signal to the brain or spinal cord, signal to muscles, bones move). "
             "Gives a complete, correct hierarchy for one system (cell, tissue, organ, organ system). "
             "Gives a correct structure-function explanation (for example, long nerve cells carry signals quickly, or muscle tissue shortens to pull on bone)."),
            (3, "Proficient",
             "Three systems with correct roles and a correct order, and a mostly correct hierarchy. "
             "The structure-function statement is brief or only partly explained."),
            (2, "Developing",
             "Only two systems, or three named with unclear roles. The order of the arrows is partly wrong. "
             "The hierarchy is incomplete or has an error. Structure-function is missing."),
            (1, "Beginning",
             "Lists body parts without showing how they interact, or shows a major misconception. The hierarchy is missing or wrong."),
        ],
        "grading_notes": [
            "Accept any three real systems that fit the response (nervous, muscular, skeletal, circulatory). The nervous system and muscular system are the expected core.",
            "The hierarchy must climb in order: a cell (such as a nerve cell or muscle cell), the tissue it belongs to, an organ (such as the brain or a muscle), and the organ system.",
            "Do not require anything at the molecular or chemical level (such as how nerve signals are made); it is outside the HS-LS1-2 assessment boundary.",
            "Common misconception: the brain is a system, or a tissue is made of organs.",
        ],
        "exemplar": (
            "Hot pan (stimulus) -> sensory nerve cells in the skin (nervous system detects the heat) -> signal travels along nerves to the spinal cord and brain (nervous system) -> signal travels to the arm muscles (nervous system to muscular system) -> arm muscles contract and pull on the bones (muscular system and skeletal system) -> the hand moves away. "
            "In the muscular system, a muscle cell is part of muscle tissue, muscle tissue is part of an organ such as the biceps, and the biceps is part of the muscular system. "
            "Structure fits function: muscle tissue can shorten, so it can pull on a bone to move the arm, and nerve cells are long, so they carry signals quickly from the skin to the spinal cord."
        ),
    },
]
