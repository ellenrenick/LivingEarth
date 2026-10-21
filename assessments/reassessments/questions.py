"""Question banks for the Unit 1.1, 1.2, and 1.3 reassessments (CP Living Earth).

Each reassessment mirrors the structure and point values of its original
assessment, but uses new scenarios, plainer wording, short sentences,
vocabulary support, and sentence starters on written responses. Every
reassessment is worth 4.0 points.

Item types:
  choice    one correct answer ("answer" is the index into "choices")
  multi     select all that apply ("answers" is a list of indexes)
  truefalse "answer" is True or False
  matching  "pairs" are (left, right); "distractors" are unused right-hand answers
  essay     "rubric" and "exemplar" are shown to the grader only

Run `python3 upload_canvas.py <course id>` to build them in Canvas, or
`python3 build_key.py` to regenerate teacher_key.md.
"""

# ---------------------------------------------------------------------------
# Unit 1.1 Reassessment: From Cells to Organisms (HS-LS1-2)
# Original: 4 MC, 2 matching, 2 model MC, scenario (select 2 + explain). 4.0 pts.
# ---------------------------------------------------------------------------
_MODEL_1_1 = (
    "<p><strong>Model:</strong></p>"
    "<p>Air &rarr; Lungs (respiratory system) &rarr; Oxygen goes into the blood &rarr; "
    "Heart and blood vessels (circulatory system) &rarr; Muscle cells</p>"
)

_SCENARIO_1_1 = (
    "<p><strong>Scenario:</strong> A soccer player sees the ball roll toward her. "
    "She runs to the ball and kicks it.</p>"
)

UNIT_1_1 = {
    "key": "1.1",
    "title": "Unit 1.1 Reassessment: From Cells to Organisms (HS-LS1-2)",
    "standard": "HS-LS1-2",
    "instructions": (
        "<p><strong>Unit 1.1 Reassessment (HS-LS1-2)</strong></p>"
        "<p>Show what you know about how the body is organized and how body systems work together. "
        "Read each question slowly. You can read it twice.</p>"
        "<p><strong>Word help:</strong></p>"
        "<ul>"
        "<li><strong>Tissue</strong> = a group of the same kind of cells working together.</li>"
        "<li><strong>Organ</strong> = a body part made of tissues that does one main job (like the heart).</li>"
        "<li><strong>Organ system</strong> = a group of organs that work together to do a big job.</li>"
        "<li><strong>Organism</strong> = a whole living thing.</li>"
        "</ul>"
    ),
    "items": [
        {
            "type": "choice", "points": 0.25, "title": "Level after organ",
            "prompt": "<p><strong>Which level of organization comes directly after organ?</strong></p>",
            "choices": ["Tissue", "Cell", "Organ system", "Organism"],
            "answer": 2,
        },
        {
            "type": "choice", "points": 0.25, "title": "Job of the digestive system",
            "prompt": "<p><strong>What is the main job of the digestive system?</strong></p>",
            "choices": [
                "To send messages to the brain",
                "To move blood around the body",
                "To break down food so the body can use it",
                "To take in oxygen from the air",
            ],
            "answer": 2,
        },
        {
            "type": "choice", "points": 0.25, "title": "Organ in the nervous system",
            "prompt": "<p><strong>Which organ belongs to the nervous system?</strong></p>",
            "choices": ["Brain", "Stomach", "Lung", "Heart"],
            "answer": 0,
        },
        {
            "type": "choice", "points": 0.25, "title": "Muscles and bones",
            "prompt": "<p><strong>Why do the muscular system and the skeletal system work together?</strong></p>",
            "choices": [
                "Bones break down food for the muscles.",
                "Muscles carry oxygen to the bones.",
                "Muscles pull on bones, which moves the body.",
                "Bones send messages to the muscles.",
            ],
            "answer": 2,
        },
        {
            "type": "matching", "points": 0.5, "title": "Match system to job",
            "prompt": "<p><strong>Match each body system to its main job.</strong> One job will not be used.</p>",
            "pairs": [
                ("Respiratory", "Takes in oxygen and gets rid of carbon dioxide"),
                ("Digestive", "Breaks down food so the body can use the nutrients"),
                ("Circulatory", "Carries blood with oxygen and nutrients to the cells"),
                ("Nervous", "Sends messages between the brain and the body"),
                ("Skeletal", "Holds up the body and protects organs"),
            ],
            "distractors": ["Fights germs that make you sick"],
        },
        {
            "type": "matching", "points": 0.5, "title": "Match level to example",
            "prompt": (
                "<p><strong>Match each level of organization to its example.</strong> "
                "One example will not be used.</p>"
            ),
            "pairs": [
                ("Cell", "One heart muscle cell"),
                ("Tissue", "Heart muscle tissue (many heart muscle cells together)"),
                ("Organ", "The heart"),
                ("Organ system", "The circulatory system (heart, blood vessels, and blood)"),
                ("Organism", "A whole person"),
            ],
            "distractors": ["A forest with many plants and animals"],
        },
        {
            "type": "choice", "points": 0.5, "title": "Model: circulatory job",
            "prompt": (
                _MODEL_1_1 +
                "<p><strong>According to the model, what does the circulatory system do?</strong></p>"
            ),
            "choices": [
                "It makes oxygen.",
                "It takes in air from outside the body.",
                "It carries oxygen to the muscle cells.",
                "It makes the muscle cells move.",
            ],
            "answer": 2,
        },
        {
            "type": "choice", "points": 0.5, "title": "Model: lungs stop working well",
            "prompt": (
                _MODEL_1_1 +
                "<p><strong>Which statement best explains what would happen if the lungs "
                "could not take in enough air?</strong></p>"
            ),
            "choices": [
                "Food would not be broken down.",
                "The muscle cells would not get enough oxygen.",
                "The blood would carry extra oxygen.",
                "The bones would grow weaker.",
            ],
            "answer": 1,
        },
        {
            "type": "multi", "points": 0.5, "title": "Scenario: which two systems",
            "prompt": (
                _SCENARIO_1_1 +
                "<p><strong>Which TWO body systems work together most directly so she can "
                "see the ball and kick it?</strong> Pick two.</p>"
            ),
            "choices": ["Nervous", "Digestive", "Muscular", "Respiratory", "Skeletal"],
            "answers": [0, 2],
        },
        {
            "type": "essay", "points": 0.5, "title": "Scenario: explain",
            "prompt": (
                _SCENARIO_1_1 +
                "<p><strong>Explain how the nervous system and the muscular system work together "
                "so she can kick the ball.</strong></p>"
                "<p>Try to use the words <em>message</em>, <em>brain</em>, and <em>muscles</em>.</p>"
                "<p>Sentence starter: <em>First, the nervous system ... Then, the muscular system ...</em></p>"
            ),
            "rubric": (
                "Scoring (0.5 pts): "
                "0.5 = Says that the nervous system sends a message (signal) from the eyes/brain to the muscles, "
                "AND the muscles move the leg (or contract) to kick. "
                "0.25 = Correctly describes the job of only ONE system, or names both systems but does not connect them "
                "(for example, 'the nervous system and muscles both help her kick'). "
                "0 = Blank, off-topic, or names wrong systems. "
                "Grading notes: Accept everyday wording like 'signal' or 'tells the muscles what to do'. "
                "Do not take off points for spelling or for leaving out the word 'contract'. "
                "A common misconception is that muscles decide to move by themselves. The brain sends the message."
            ),
            "exemplar": (
                "First, the nervous system uses her eyes to see the ball, and the brain sends a message to the "
                "muscles in her leg. Then, the muscular system gets the message and the leg muscles pull on her "
                "bones, so her leg swings and kicks the ball. The two systems work together."
            ),
        },
    ],
}

# ---------------------------------------------------------------------------
# Unit 1.2 Reassessment: Cell Energy & Carbon (HS-LS2-5)
# Original: vocab matching, 2 MC (photosynthesis, respiration), scenario,
# 2 model matching. 4.0 pts.
# ---------------------------------------------------------------------------
_MODEL_1_2 = (
    "<p><strong>Carbon cycle model.</strong> CO<sub>2</sub> = carbon dioxide. Each arrow shows carbon moving.</p>"
    '<table border="1" cellpadding="6" style="border-collapse: collapse;">'
    "<tr><th>Arrow</th><th>Carbon moves from ...</th><th>... to</th><th>What you see</th></tr>"
    "<tr><td><strong>A</strong></td><td>CO<sub>2</sub> in the air</td><td>A tree</td>"
    "<td>CO<sub>2</sub> goes into the tree's leaves. The tree uses sunlight and builds sugar.</td></tr>"
    "<tr><td><strong>B</strong></td><td>A tree</td><td>CO<sub>2</sub> in the air</td>"
    "<td>The tree's cells break down sugar to get energy. CO<sub>2</sub> comes out.</td></tr>"
    "<tr><td><strong>C</strong></td><td>Coal (a fossil fuel)</td><td>CO<sub>2</sub> in the air</td>"
    "<td>A power plant burns coal. CO<sub>2</sub> goes up the smokestack.</td></tr>"
    "</table>"
)

UNIT_1_2 = {
    "key": "1.2",
    "title": "Unit 1.2 Reassessment: Cell Energy & Carbon (HS-LS2-5)",
    "standard": "HS-LS2-5",
    "instructions": (
        "<p><strong>Unit 1.2 Reassessment (HS-LS2-5)</strong></p>"
        "<p>Show what you know about how carbon moves through Earth's systems, and about how "
        "photosynthesis and cellular respiration are part of that path. Read each question slowly.</p>"
        "<p><strong>Word help:</strong> CO<sub>2</sub> = carbon dioxide. A fossil fuel (like coal or oil) "
        "is made from living things that died a very long time ago.</p>"
    ),
    "items": [
        {
            "type": "matching", "points": 1.0, "title": "Vocabulary",
            "prompt": "<p><strong>Match each word to its meaning.</strong> Two meanings will not be used.</p>",
            "pairs": [
                ("Atmosphere", "The air around Earth. It holds carbon as carbon dioxide gas."),
                ("Hydrosphere", "All of the water on Earth, such as oceans, lakes, and rivers"),
                ("Biosphere", "All of the living things on Earth, like plants and animals"),
                ("Geosphere", "The solid parts of Earth, like rock, soil, and fossil fuels"),
                ("Carbon cycle", "The path carbon takes as it moves between air, water, living things, and rock"),
                ("Photosynthesis", "Plants use sunlight to turn carbon dioxide and water into sugar"),
                ("Cellular respiration", "Cells break down sugar to get energy and give off carbon dioxide"),
                ("Combustion", "Burning something, like wood or gasoline, which gives off carbon dioxide"),
            ],
            "distractors": [
                "Liquid water changes into a gas",
                "The part of a plant that takes in water from the soil",
            ],
        },
        {
            "type": "choice", "points": 0.5, "title": "Photosynthesis in a pond",
            "prompt": (
                "<p>A pond is full of algae (tiny plant-like living things). On a very sunny day the algae "
                "do more photosynthesis.</p>"
                "<p><strong>Which change should a carbon cycle model show?</strong></p>"
            ),
            "choices": [
                "More carbon moves from the algae into the rock under the pond.",
                "More carbon moves from the air and water into the algae.",
                "Less carbon moves from the air and water into the algae.",
                "No carbon moves, because algae do not use carbon.",
            ],
            "answer": 1,
        },
        {
            "type": "choice", "points": 0.5, "title": "Cellular respiration in a forest",
            "prompt": (
                "<p>On a warm day, the animals in a forest are very active. Their cells do more cellular "
                "respiration.</p>"
                "<p><strong>Which sentence best tells how this changes the carbon cycle?</strong></p>"
            ),
            "choices": [
                "Carbon dioxide turns into sugar inside the animals.",
                "Less carbon moves into the air.",
                "More carbon moves from living things into the air as carbon dioxide.",
                "Carbon stays in the animals as sugar and never leaves.",
            ],
            "answer": 2,
        },
        {
            "type": "choice", "points": 1.0, "title": "Fallen trees scenario",
            "prompt": (
                "<p>A big storm knocks over many trees in a forest. The dead trees lie on the ground. "
                "Over the next few years, fungi and bacteria break the dead trees down. New young trees "
                "start to grow.</p>"
                "<p>A student says: <em>&ldquo;The carbon in the dead trees is gone forever.&rdquo;</em></p>"
                "<p><strong>Which answer best explains whether the student is correct?</strong> Choose 1.</p>"
            ),
            "choices": [
                "The student is correct, because the carbon in a dead tree is destroyed.",
                "The student is not correct. The carbon changes into energy and leaves Earth.",
                "The student is not correct. Fungi and bacteria break down the trees and give off CO<sub>2</sub> to the air. New trees take in that CO<sub>2</sub> by photosynthesis.",
                "The student is not correct, because the carbon stays inside the dead trees and never moves.",
            ],
            "answer": 2,
        },
        {
            "type": "matching", "points": 0.5, "title": "Model: match arrow to process",
            "prompt": (
                _MODEL_1_2 +
                "<p><strong>Match each arrow in the model to the process it shows.</strong> "
                "Two processes will not be used.</p>"
            ),
            "pairs": [
                ("Arrow A", "Photosynthesis"),
                ("Arrow B", "Cellular respiration"),
                ("Arrow C", "Combustion"),
            ],
            "distractors": ["Decomposition", "Evaporation"],
        },
        {
            "type": "matching", "points": 0.5, "title": "Match arrow to spheres",
            "prompt": (
                "<p>Each sentence below tells about carbon moving. "
                "<strong>Match each sentence to the two spheres the carbon moves between.</strong> "
                "Two choices will not be used.</p>"
            ),
            "pairs": [
                ("CO2 gas from the air dissolves into the ocean.", "atmosphere to hydrosphere"),
                ("Seaweed in the ocean takes in CO2 that is dissolved in the water.", "hydrosphere to biosphere"),
                ("Coal from underground is burned and CO2 goes into the air.", "geosphere to atmosphere"),
            ],
            "distractors": ["biosphere to biosphere", "atmosphere to geosphere"],
        },
    ],
}

# ---------------------------------------------------------------------------
# Unit 1.3 Reassessment: Sugar to Structures (HS-LS1-6)
# Original: 14 MC / TF items across LS1-6.1 to 6.6 plus 2 four-point essays.
# Reassessment: 8 MC / TF (0.25 each) plus 2 scaffolded written responses (1.0 each).
# ---------------------------------------------------------------------------
UNIT_1_3 = {
    "key": "1.3",
    "title": "Unit 1.3 Reassessment: Sugar to Structures (HS-LS1-6)",
    "standard": "HS-LS1-6",
    "instructions": (
        "<p><strong>Unit 1.3 Reassessment (HS-LS1-6)</strong></p>"
        "<p>Show what you know about how plants use the atoms in sugar, and atoms from other elements, to build "
        "the large molecules they need. There are 8 multiple choice questions and 2 written responses. "
        "The written responses have sentence starters to help you.</p>"
        "<p><strong>Symbol key:</strong> C = carbon, H = hydrogen, O = oxygen, N = nitrogen; "
        "CO<sub>2</sub> = carbon dioxide, H<sub>2</sub>O = water.</p>"
        "<p><strong>Word help:</strong></p>"
        "<ul>"
        "<li><strong>Element</strong> = one kind of atom, like carbon or nitrogen.</li>"
        "<li><strong>Amino acid</strong> = a small building block. Many amino acids join to make a protein.</li>"
        "<li><strong>Rearranged</strong> = moved into a new order. The atoms are the same atoms.</li>"
        "</ul>"
    ),
    "items": [
        {
            "type": "choice", "points": 0.25, "title": "LS1-6.1 Elements from sugar",
            "prompt": (
                "<p>An amino acid has carbon, hydrogen, oxygen, and nitrogen atoms.</p>"
                "<p><strong>Which of these elements can come from the sugar a plant makes?</strong></p>"
            ),
            "choices": [
                "Nitrogen only",
                "Oxygen and nitrogen only",
                "Carbon, hydrogen, and oxygen",
                "All four elements",
            ],
            "answer": 2,
        },
        {
            "type": "truefalse", "points": 0.25, "title": "LS1-6.1 What sugar is made of",
            "prompt": "<p><strong>True or false:</strong> Sugar is made of only carbon, hydrogen, and oxygen atoms.</p>",
            "answer": True,
        },
        {
            "type": "choice", "points": 0.25, "title": "LS1-6.2 Where does the matter come from",
            "prompt": (
                "<p>A pumpkin plant grows from a tiny seed into a big vine that weighs 20 kg. "
                "The soil in its pot loses almost no mass.</p>"
                "<p><strong>Where did most of the matter in the pumpkin vine come from?</strong></p>"
            ),
            "choices": [
                "From sunlight, which turned into solid matter",
                "From the soil, which the roots took in",
                "From carbon dioxide in the air and from water, which the plant built into sugar and other molecules",
                "From the seed, which already had all the matter the vine needed",
            ],
            "answer": 2,
        },
        {
            "type": "choice", "points": 0.25, "title": "LS1-6.2 Bead model, count the atoms",
            "prompt": (
                "<p>A student uses beads to model a sugar molecule: 6 black beads (carbon), 12 white beads "
                "(hydrogen), and 6 red beads (oxygen). She takes the sugar model apart. Then she uses the "
                "beads to build new molecules.</p>"
                "<p><strong>How many black (carbon) beads can she use in the new molecules?</strong></p>"
            ),
            "choices": [
                "0 black beads, because carbon disappears when a molecule is taken apart",
                "3 black beads, because half of the carbon is lost",
                "12 black beads, because new carbon is made when beads are rearranged",
                "6 black beads, because atoms are rearranged, not destroyed",
            ],
            "answer": 3,
        },
        {
            "type": "choice", "points": 0.25, "title": "LS1-6.3 Plants with no nitrogen",
            "prompt": (
                "<p>Bean plants get plenty of light, water, and carbon dioxide, but their soil has no nitrogen. "
                "The plants make sugar, but they stay very small.</p>"
                "<p><strong>Which explanation is best?</strong></p>"
            ),
            "choices": [
                "Sugar has no nitrogen, so the plants cannot build the amino acids and proteins they need for new cells.",
                "Without nitrogen the plants cannot make any sugar at all.",
                "Nitrogen is the main source of carbon atoms in plants.",
                "The plants are small because they used up all of their sugar for energy.",
            ],
            "answer": 0,
        },
        {
            "type": "choice", "points": 0.25, "title": "LS1-6.3 Table evidence",
            "prompt": (
                "<p>A student counts the atoms in two molecules:</p>"
                '<table border="1" cellpadding="6" style="border-collapse: collapse;">'
                "<tr><th>Molecule</th><th>Carbon (C)</th><th>Hydrogen (H)</th><th>Oxygen (O)</th><th>Nitrogen (N)</th></tr>"
                "<tr><td>Glucose (a sugar)</td><td>6</td><td>12</td><td>6</td><td>0</td></tr>"
                "<tr><td>Alanine (an amino acid)</td><td>3</td><td>7</td><td>2</td><td>1</td></tr>"
                "</table>"
                "<p>The student says: <em>&ldquo;A plant can build alanine using only atoms from glucose.&rdquo;</em></p>"
                "<p><strong>Which evidence from the table shows the claim is wrong?</strong></p>"
            ),
            "choices": [
                "Glucose has more hydrogen atoms than alanine.",
                "Alanine has 1 nitrogen atom, and glucose has no nitrogen atoms.",
                "Both molecules have carbon, hydrogen, and oxygen.",
                "Glucose has 6 carbon atoms, and alanine has 3.",
            ],
            "answer": 1,
        },
        {
            "type": "choice", "points": 0.25, "title": "LS1-6.4 Trace the atoms",
            "prompt": (
                "<p>Scientists give a plant carbon dioxide that has &ldquo;tagged&rdquo; carbon. The tag lets "
                "them follow the carbon atoms. They find the tagged carbon here:</p>"
                '<table border="1" cellpadding="6" style="border-collapse: collapse;">'
                "<tr><th>Time</th><th>Where the tagged carbon was found</th></tr>"
                "<tr><td>10 minutes</td><td>Sugar in the leaves</td></tr>"
                "<tr><td>2 days</td><td>Sugar in the leaves; amino acids in the stems and leaves</td></tr>"
                "<tr><td>2 weeks</td><td>Proteins in the leaves and in the seeds</td></tr>"
                "</table>"
                "<p><strong>Which conclusion is best supported by this evidence?</strong></p>"
            ),
            "choices": [
                "The plant made new carbon atoms inside its seeds.",
                "Carbon from the air was built into sugar. Then atoms from that sugar were used to build amino acids and proteins.",
                "The plant took in proteins from the soil, and the tagged carbon stayed in the sugar.",
                "The tagged carbon changed into nitrogen so it could join the amino acids.",
            ],
            "answer": 1,
        },
        {
            "type": "choice", "points": 0.25, "title": "LS1-6.6 Revise an explanation",
            "prompt": (
                "<p>At the start of the unit, a student wrote: <em>&ldquo;Plants make their proteins out of "
                "sunlight.&rdquo;</em></p>"
                "<p>Since then, the class learned these things:</p>"
                "<ul>"
                "<li>Tagged carbon from CO<sub>2</sub> ended up in plant proteins.</li>"
                "<li>Plants with no nitrogen make sugar but very little protein.</li>"
                "<li>Bead models show atoms are rearranged, but never made from nothing.</li>"
                "</ul>"
                "<p><strong>Which revision best uses all of this evidence?</strong></p>"
            ),
            "choices": [
                "Plants take proteins from the soil and store them in their cells.",
                "Plants turn sunlight into new carbon atoms, and then add nitrogen to make proteins.",
                "Plants use light energy to make sugar from CO<sub>2</sub> and water. Atoms from the sugar are rearranged and combined with nitrogen from the soil to make amino acids and proteins.",
                "Plants use light energy to make sugar. The sugar is the only building material in the plant, so no other elements are needed.",
            ],
            "answer": 2,
        },
        {
            "type": "essay", "points": 1.0, "title": "LS1-6.5 Explain with evidence (CER)",
            "prompt": (
                "<p>A gardener grows two groups of tomato plants. Both groups get the same light, water, "
                "carbon dioxide, and temperature. Group 1 gets nitrogen fertilizer. Group 2 does not. "
                "After 4 weeks she measures the plants:</p>"
                '<table border="1" cellpadding="6" style="border-collapse: collapse;">'
                "<tr><th>Measurement</th><th>Group 1 (nitrogen)</th><th>Group 2 (no nitrogen)</th></tr>"
                "<tr><td>Leaf color</td><td>Dark green</td><td>Pale yellow</td></tr>"
                "<tr><td>Plant mass (g)</td><td>250</td><td>80</td></tr>"
                "<tr><td>Sugar in leaves (mg/g)</td><td>14</td><td>26</td></tr>"
                "<tr><td>Protein in leaves (mg/g)</td><td>35</td><td>8</td></tr>"
                "</table>"
                "<p>mg/g means milligrams in each gram of leaf.</p>"
                "<p>The gardener asks: <em>&ldquo;Group 2 has MORE sugar. If plants use sugar to grow, why are "
                "they so much smaller?&rdquo;</em></p>"
                "<p><strong>Write an explanation with a Claim, Evidence, and Reasoning.</strong></p>"
                "<p><strong>Claim:</strong> Why is Group 2 smaller even though it has more sugar?<br>"
                "<em>Sentence starter: Group 2 is smaller because ...</em></p>"
                "<p><strong>Evidence:</strong> Use at least TWO numbers from the table.<br>"
                "<em>Sentence starter: In the table, Group 2 has ... but Group 1 has ...</em></p>"
                "<p><strong>Reasoning:</strong> Explain how the carbon, hydrogen, and oxygen atoms in sugar "
                "combine with another element to build what the plant needs to grow. Also say why the sugar "
                "built up in Group 2.<br>"
                "<em>Sentence starter: Sugar has only ... To make proteins, the plant must add ... "
                "The sugar built up because ...</em></p>"
            ),
            "rubric": (
                "Rubric (4 levels; Canvas points = 1.0 for level 4, 0.75 for level 3, 0.5 for level 2, 0.25 for level 1, 0 for blank). "
                "Level 4, Advanced: Accurate claim that the missing nitrogen kept Group 2 from turning its sugar into amino acids and proteins. "
                "Cites at least two accurate data points and contrasts them (for example, sugar is higher but protein and mass are lower). "
                "Reasoning says sugar has only C, H, and O, and that atoms from sugar are rearranged and combined with nitrogen to make amino acids and proteins. "
                "Explains why the sugar built up (it could not be used without nitrogen). "
                "Level 3, Proficient: Accurate claim and at least two accurate data points. Reasoning connects sugar plus nitrogen to proteins but leaves out one piece "
                "(for example, that sugar has no nitrogen, or why sugar built up). "
                "Level 2, Developing: Claim is partly correct (for example, 'it needs nitrogen to grow') without linking nitrogen to using sugar. "
                "Uses only one data point, or uses data inaccurately. Reasoning is vague. "
                "Level 1, Beginning: Claim is wrong or missing (for example, 'nitrogen is needed for photosynthesis' or 'more sugar should mean a bigger plant'). "
                "Little or no data. Reasoning is missing or shows a major misconception (for example, atoms are created, or sunlight becomes matter). "
                "0: Blank or off-topic. "
                "Grading notes: Group 2 made MORE sugar (26 vs. 14 mg/g), so photosynthesis still worked. Nitrogen limited protein (8 vs. 35 mg/g) and growth (80 vs. 250 g). "
                "Common misconception: 'Without nitrogen the plant can't do photosynthesis.' The sugar data contradict this, so the claim cannot earn a 3 or 4. "
                "Common misconception: fertilizer is 'plant food' that gives energy or carbon. Fertilizer supplies elements like nitrogen, not sugar. "
                "Do not take off points for leaving out chemical reaction details or names of large molecule types. Both are outside the HS-LS1-6 assessment boundary."
            ),
            "exemplar": (
                "Group 2 is smaller because it did not have nitrogen, so it could not use its sugar to build proteins for new cells. "
                "In the table, Group 2 has 8 mg/g of protein but Group 1 has 35 mg/g, and Group 2 has a mass of only 80 g compared with 250 g. "
                "Group 2 actually has more sugar (26 vs. 14 mg/g), so photosynthesis still worked. "
                "Sugar has only carbon, hydrogen, and oxygen. To make amino acids and proteins, the plant must rearrange the atoms from sugar and combine them with nitrogen from the soil. "
                "Group 2 had no nitrogen, so its sugar could not be used and it piled up."
            ),
        },
        {
            "type": "essay", "points": 1.0, "title": "LS1-6.6 Revise an explanation",
            "prompt": (
                "<p>A student wrote this explanation:</p>"
                "<p><em>&ldquo;A pea plant makes the protein in its seeds out of nutrients from the soil. "
                "The soil gives the plant its protein.&rdquo;</em></p>"
                "<p>Scientists collected this evidence:</p>"
                "<ul>"
                "<li><strong>Weighing:</strong> A pea plant gained 40 g over the summer. The soil lost less than 1 g.</li>"
                "<li><strong>Tagged carbon:</strong> Pea plants were given CO<sub>2</sub> with tagged carbon. "
                "The tag showed up first in the plant's sugar, then in amino acids, then in the protein in the seeds.</li>"
                "<li><strong>No nitrogen:</strong> Pea plants grown without nitrogen made sugar but very little protein.</li>"
                "</ul>"
                "<p><strong>Use the evidence to answer both parts.</strong></p>"
                "<p><strong>Part 1: Evaluate.</strong> Which part of the student's explanation is NOT supported "
                "by the evidence? Use the evidence to say why.<br>"
                "<em>Sentence starter: The student is wrong that ... because the evidence shows ...</em></p>"
                "<p><strong>Part 2: Revise.</strong> Write a better explanation. Trace the carbon atoms from the "
                "air to the protein in the seeds. Say what the atoms from sugar combine with, and where that "
                "other element comes from.<br>"
                "<em>Sentence starter: The plant takes in CO<sub>2</sub> from the ... The plant uses light to make ... "
                "Then the atoms from sugar are rearranged and combine with ... to make ...</em></p>"
            ),
            "rubric": (
                "Rubric (4 levels; Canvas points = 1.0 for level 4, 0.75 for level 3, 0.5 for level 2, 0.25 for level 1, 0 for blank). "
                "Level 4, Advanced: Part 1 says the idea that the soil gives the plant its protein (or most of its matter) is NOT supported, and cites evidence "
                "(the soil lost almost no mass while the plant gained 40 g, and/or the tagged carbon came from CO2). "
                "Part 2 traces carbon completely: CO2 from the air goes into sugar by photosynthesis. Atoms from sugar are rearranged and combine with nitrogen "
                "to make amino acids and then proteins. Says the nitrogen comes from the soil. "
                "Level 3, Proficient: Part 1 is correct with evidence. Part 2 traces carbon from air to sugar to protein and includes nitrogen, "
                "but is missing one piece (for example, does not say the nitrogen comes from the soil, or does not say the atoms are rearranged). "
                "Level 2, Developing: Identifies the unsupported idea but gives weak or no evidence, OR the revision skips the sugar step or the nitrogen. "
                "Level 1, Beginning: Repeats the original idea or shows a major misconception (carbon from soil, plant makes new atoms, sunlight becomes protein). No traceable path for the carbon. "
                "0: Blank or off-topic. "
                "Grading notes: The student is PARTLY right: nitrogen does come from the soil. A strong answer keeps that part and fixes the rest. "
                "Look for the words 'air', 'CO2', 'sugar', 'rearranged' or 'combined', and 'nitrogen'. "
                "Do not take off points for leaving out chemical reaction details or names of large molecule types. Both are outside the HS-LS1-6 assessment boundary."
            ),
            "exemplar": (
                "Part 1: The student is wrong that the soil gives the plant its protein, because the plant gained 40 g and the soil lost less than 1 g. "
                "The tagged carbon came from the CO2 in the air, not from the soil. "
                "Part 2: The plant takes in CO2 from the air. The plant uses light to make sugar from CO2 and water. "
                "Then the atoms from the sugar (carbon, hydrogen, and oxygen) are rearranged and combine with nitrogen from the soil to make amino acids. "
                "The amino acids join to make the proteins in the seeds. The soil gives the nitrogen, but the carbon in the protein came from the air."
            ),
        },
    ],
}

REASSESSMENTS = [UNIT_1_1, UNIT_1_2, UNIT_1_3]
