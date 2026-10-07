"""Unit 1.3 Sugar to Structures (HS-LS1-6): outcomes, CFAs, practice test, and CSA.

Laid out like Earth Science Unit 3 (Forces Beneath Our Feet):
- One outcome per learning target (4-point scale, mastery at 3, highest score).
- One CFA per learning target: 5 one-point auto-graded questions.
- Practice test and CSA are parallel forms. A DOK 1-2 target gets 3 one-point
  auto-graded questions. A DOK 3 target gets 1 one-point multiple-choice
  question plus 1 four-point written response that the teacher grades.
  6 targets -> 16 questions, 22 points.

The CSA reuses the items in questions.py, and the practice test reuses
practice_questions.py where an item fits a target. Run
`python3 newquiz_upload.py` to put everything in Canvas (New Quizzes).

Item types: "choice" (answer = index of the key), "multi" (answer = list of
indexes, all-or-nothing), "tf" (answer = True/False), "essay" (4 points).
For "choice" items the key is written first and moved into place by
KEY_POSITIONS when uploaded.
"""

import practice_questions as P
import questions as S

UNIT = "Unit 1.3"
UNIT_NAME = "Sugar to Structures"
STANDARD = "HS-LS1-6"
GROUP_TITLE = "HS-LS1-6 · Unit 1.3: Sugar to Structures"
GROUP_DESCRIPTION = (
    "<p>Construct and revise an explanation based on evidence for how carbon, hydrogen, "
    "and oxygen from sugar molecules may combine with other elements to form amino acids "
    "and/or other large carbon-based molecules.</p>"
)

# Learning targets from "Living Earth Standards and Learning Targets (26-27)", Targets tab.
# (id, short name, DOK, student "I can" line)
TARGETS = [
    ("LS1-6.1", "Elements in sugar and large molecules", 1,
     "I can name the three elements that make up most of sugar and the body's large molecules."),
    ("LS1-6.2", "Taking in and rearranging matter", 2,
     "I can describe how living things take in matter and rearrange its atoms, with no atoms lost."),
    ("LS1-6.3", "Sugar atoms plus other elements", 2,
     "I can explain how atoms from sugar join with other elements, like nitrogen, to build larger molecules."),
    ("LS1-6.4", "Trace atoms with a model", 2,
     "I can use a model to trace atoms from sugar into a larger molecule."),
    ("LS1-6.5", "Explain with evidence", 3,
     "I can use evidence to explain how atoms from sugar combine with other elements to build large carbon-based molecules."),
    ("LS1-6.6", "Revise an explanation", 3,
     "I can revise my explanation when new evidence comes in."),
]
TARGET = {t[0]: t for t in TARGETS}

# Outcome ratings copied from Earth Science Unit 3.
RATINGS = [
    ("Mastered", 4), ("Proficient", 3), ("Approaching", 2),
    ("Not yet meeting", 1), ("Insufficient evidence", 0),
]
MASTERY_POINTS = 3
GRADE_POINTS = 4  # every Unit 1.3 assignment and quiz is graded out of 4 in Canvas

# Where the key lands for each "choice" item (0 = A), cycled per quiz.
KEY_POSITIONS = [1, 3, 0, 2, 2, 0, 3, 1]


def _from_bank(item, lt, feedback=True):
    """Turn a questions.py / practice_questions.py MC item into a bank item."""
    return {
        "lt": lt, "type": "choice", "prompt": item["prompt"],
        "choices": item["choices"], "answer": item["answer"],
        "feedback": item["feedback"] if feedback else "",
    }


def _essay_from_bank(item, lt):
    return {
        "lt": lt, "type": "essay", "prompt": item["prompt"],
        "rubric": item["rubric"], "grading_notes": item["grading_notes"],
        "exemplar": item["exemplar"],
    }


def _find(bank, prefix):
    for it in bank.MULTIPLE_CHOICE + bank.FREE_RESPONSE:
        if it["title"].startswith(prefix):
            return it
    raise KeyError(prefix)


# ===========================================================================
# CFAs: one per learning target, 5 one-point questions each.
# ===========================================================================
CFAS = {
    "LS1-6.1": [
        {"type": "choice",
         "prompt": "<p>A glucose (sugar) molecule is C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>. Which three elements make up glucose?</p>",
         "choices": ["Carbon, hydrogen, and oxygen", "Carbon, nitrogen, and oxygen",
                     "Calcium, hydrogen, and oxygen", "Carbon, helium, and oxygen"],
         "answer": 0,
         "feedback": "C stands for carbon, H for hydrogen, and O for oxygen. Glucose has 6 carbon, 12 hydrogen, and 6 oxygen atoms."},
        {"type": "choice",
         "prompt": "<p>Which list best describes the elements that make up the proteins in your muscles?</p>",
         "choices": ["Mostly carbon, hydrogen, and oxygen, plus nitrogen (and sometimes sulfur)",
                     "Mostly iron, calcium, and sodium",
                     "Only carbon",
                     "Only hydrogen and oxygen"],
         "answer": 0,
         "feedback": "Like sugar, proteins are built mostly from carbon, hydrogen, and oxygen. Their amino acids also contain nitrogen, and a few contain sulfur."},
        {"type": "multi",
         "prompt": "<p>A cell uses atoms from sugar to build larger carbon-based molecules. Select the <strong>THREE</strong> elements that sugar supplies.</p>",
         "choices": ["Carbon", "Nitrogen", "Hydrogen", "Phosphorus", "Oxygen", "Sodium"],
         "answer": [0, 2, 4],
         "feedback": "Sugar is made of carbon, hydrogen, and oxygen. Nitrogen and phosphorus have to come from somewhere else, such as the soil or food."},
        {"type": "tf",
         "prompt": "<p>True or false: Amino acids contain nitrogen, an element that sugar does not have.</p>",
         "answer": True,
         "feedback": "True. Every amino acid has nitrogen. Sugar has none, so the nitrogen has to come from another source."},
        {"type": "choice",
         "prompt": "<p>Which element is found in <strong>every</strong> large carbon-based molecule in a cell?</p>",
         "choices": ["Carbon", "Nitrogen", "Sulfur", "Phosphorus"],
         "answer": 0,
         "feedback": "They are called carbon-based molecules because every one of them is built on carbon. Only some also contain nitrogen, sulfur, or phosphorus."},
    ],
    "LS1-6.2": [
        {"type": "choice",
         "prompt": "<p>A rabbit eats only clover and grows larger. Where does the matter in the rabbit's new body tissue come from?</p>",
         "choices": ["Molecules in the clover, which the rabbit breaks down and rebuilds into its own molecules",
                     "Sunlight that the rabbit absorbs through its fur",
                     "New atoms that the rabbit's cells make as it grows",
                     "Heat that the rabbit's body releases"],
         "answer": 0,
         "feedback": "Animals take in matter as food. They break food molecules down and rearrange the atoms into their own molecules. Sunlight and heat are energy, not matter, and cells can't make new atoms."},
        {"type": "choice",
         "prompt": "<p>Photosynthesis can be written as:</p><p>6 CO<sub>2</sub> + 6 H<sub>2</sub>O &rarr; C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + 6 O<sub>2</sub></p><p>How many oxygen atoms are on each side?</p>",
         "choices": ["18 on the left and 18 on the right", "12 on the left and 18 on the right",
                     "18 on the left and 6 on the right", "6 on the left and 6 on the right"],
         "answer": 0,
         "feedback": "Left: 6 CO2 has 12 O and 6 H2O has 6 O, so 18. Right: glucose has 6 O and 6 O2 has 12 O, so 18. The atoms are rearranged, not lost."},
        {"type": "choice",
         "prompt": "<p>Two glucose molecules join to make a larger sugar:</p><p>C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> &rarr; C<sub>12</sub>H<sub>22</sub>O<sub>11</sub> + H<sub>2</sub>O</p><p>The two glucose molecules have 24 hydrogen atoms, but the larger sugar has only 22. What happened to the other 2 hydrogen atoms?</p>",
         "choices": ["They became part of the water molecule that was released.",
                     "They were destroyed when the two sugars joined.",
                     "They changed into oxygen atoms.",
                     "They turned into energy."],
         "answer": 0,
         "feedback": "When the two sugars join, a water molecule (H2O) is released. It holds the 2 hydrogen atoms and 1 oxygen atom. Count both products and every atom is still there."},
        {"type": "tf",
         "prompt": "<p>True or false: When a cell links amino acids together to build a protein, the total number of each kind of atom stays the same, because atoms are only rearranged.</p>",
         "answer": True,
         "feedback": "True. In a chemical reaction atoms are rearranged into new molecules. None are created or destroyed, so the total mass stays the same."},
        {"type": "choice",
         "prompt": "<p>A student puts yeast, sugar, and water in a jar and seals it tightly. The jar and its contents have a mass of 250.0 g. Two days later the yeast has grown into many new cells. Nothing has gone into or out of the jar.</p><p>What mass should the sealed jar have now?</p>",
         "choices": ["250.0 g, because the atoms were rearranged into new molecules, not created or destroyed",
                     "Less than 250.0 g, because the yeast used up the sugar",
                     "More than 250.0 g, because the yeast made new cells",
                     "It is impossible to predict, because living things do not follow conservation of matter"],
         "answer": 0,
         "feedback": "The yeast rearranged atoms from the sugar into new molecules, but no atoms left or entered the sealed jar, so the mass stays at 250.0 g."},
    ],
    "LS1-6.3": [
        {"type": "choice",
         "prompt": "<p>Glucose is C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>. The amino acid glycine is C<sub>2</sub>H<sub>5</sub>NO<sub>2</sub>.</p><p>A cell builds glycine using atoms from glucose. Which element must the cell get from somewhere else?</p>",
         "choices": ["Nitrogen", "Carbon", "Hydrogen", "Oxygen"],
         "answer": 0,
         "feedback": "Glycine has one N (nitrogen). Glucose has no nitrogen, so the cell has to get it from another source."},
        {"type": "choice",
         "prompt": "<p>The amino acid cysteine is C<sub>3</sub>H<sub>7</sub>NO<sub>2</sub>S. Which elements in cysteine <strong>cannot</strong> come from sugar?</p>",
         "choices": ["Nitrogen and sulfur", "Carbon and oxygen", "Hydrogen only", "None of them. Sugar supplies every element in cysteine."],
         "answer": 0,
         "feedback": "Sugar supplies C, H, and O. The N (nitrogen) and S (sulfur) in cysteine have to come from other sources, like compounds in the soil."},
        {"type": "choice",
         "prompt": "<p>Plant roots take in nitrate, a compound that contains nitrogen, from the soil. What does the plant do with this nitrogen?</p>",
         "choices": ["It combines the nitrogen with carbon, hydrogen, and oxygen atoms from sugar to build amino acids.",
                     "It uses the nitrogen to make sugar during photosynthesis.",
                     "It breaks the nitrogen down to release energy for growth.",
                     "It stores the nitrogen unchanged in its leaves."],
         "answer": 0,
         "feedback": "Sugar is made from CO2 and water and has no nitrogen. The plant joins the nitrogen with atoms from sugar to build amino acids, which it then links into proteins."},
        {"type": "multi",
         "prompt": "<p>Select the <strong>TWO</strong> statements that describe how a cell builds a large molecule, such as a protein, from smaller molecules.</p>",
         "choices": ["Smaller molecules are bonded together into a longer chain.",
                     "New carbon atoms are made to hold the chain together.",
                     "The atoms are rearranged, and none are created or destroyed.",
                     "Energy is turned into new atoms that become part of the molecule.",
                     "The smaller molecules melt into a single large atom."],
         "answer": [0, 2],
         "feedback": "Building a large molecule bonds smaller ones together. The atoms are rearranged, but none are made or destroyed, and energy doesn't turn into atoms."},
        {"type": "tf",
         "prompt": "<p>True or false: A plant growing in soil with no phosphorus can still make sugar, but it can't build molecules that need phosphorus, such as DNA.</p>",
         "answer": True,
         "feedback": "True. Photosynthesis only needs CO2, water, and light, so the plant can still make sugar. Sugar has no phosphorus, so the plant can't build molecules that need it."},
    ],
    "LS1-6.4": [
        {"type": "choice",
         "prompt": "<p>In a bead model, black = carbon, white = hydrogen, red = oxygen, and blue = nitrogen. A student takes apart a glucose model (6 black, 12 white, 6 red) and uses the beads to build amino acid models. Each amino acid model needs 1 blue bead.</p><p>What must the student do?</p>",
         "choices": ["Add blue beads from a separate pile, which stands for nitrogen from the soil",
                     "Paint some black beads blue, since carbon can turn into nitrogen",
                     "Build the amino acids without blue beads, since they aren't really needed",
                     "Throw away the glucose beads, since atoms from sugar can't be reused"],
         "answer": 0,
         "feedback": "The glucose beads can be reused, which models atoms being rearranged. Glucose has no nitrogen, so blue beads have to come from outside the model, like nitrogen from the soil."},
        {"type": "choice",
         "prompt": "<p>Scientists give a plant carbon dioxide with \"labeled\" carbon atoms they can track. In what order would they expect to find the labeled carbon?</p>",
         "choices": ["Carbon dioxide &rarr; sugar &rarr; amino acids &rarr; proteins",
                     "Proteins &rarr; amino acids &rarr; sugar &rarr; carbon dioxide",
                     "Carbon dioxide &rarr; proteins &rarr; sugar &rarr; amino acids",
                     "Sugar &rarr; carbon dioxide &rarr; proteins &rarr; amino acids"],
         "answer": 0,
         "feedback": "Photosynthesis builds the carbon from CO2 into sugar first. The plant then uses atoms from sugar, plus nitrogen, to build amino acids, and links the amino acids into proteins."},
        {"type": "choice",
         "prompt": "<p>A student's model of a rabbit eating grass has four arrows. Which arrow traces <strong>atoms</strong> (matter), not energy?</p>",
         "choices": ["Carbon dioxide in the air &rarr; sugar in grass leaves",
                     "Sunlight &rarr; grass leaves",
                     "Rabbit muscles &rarr; heat given off to the air",
                     "Sunlight &rarr; warmth of the rabbit's fur"],
         "answer": 0,
         "feedback": "Carbon atoms from CO2 are built into sugar, so that arrow traces matter. Sunlight and heat are energy, not atoms."},
        {"type": "choice",
         "prompt": "<p>In a leaf-cell simulation, a student sets nitrogen to <strong>zero</strong> and keeps light, water, and carbon dioxide high. What should the simulation show?</p>",
         "choices": ["The cell keeps making sugar, but it can't make amino acids.",
                     "The cell stops making sugar, because photosynthesis needs nitrogen.",
                     "The cell makes amino acids from sugar alone.",
                     "The atoms in the cell start to disappear."],
         "answer": 0,
         "feedback": "Photosynthesis only needs light, CO2, and water, so sugar is still made. Amino acids need nitrogen, so with no nitrogen the cell can't make them."},
        {"type": "choice",
         "prompt": "<p>A student builds 2 models of the amino acid glycine (C<sub>2</sub>H<sub>5</sub>NO<sub>2</sub>). To link them, the student removes one water molecule (H<sub>2</sub>O) from the models.</p><p>How many hydrogen atoms (white beads) are in the linked model?</p>",
         "choices": ["8", "10", "9", "12"],
         "answer": 0,
         "feedback": "2 glycine models have 2 × 5 = 10 hydrogen atoms. The water removed holds 2 of them, so 10 − 2 = 8 are left in the linked model. The 2 removed atoms are still in the water molecule."},
    ],
    "LS1-6.5": [
        {"type": "choice",
         "prompt": "<p><strong>Claim:</strong> Atoms from sugar end up in a plant's proteins.</p><p>Which evidence <strong>best</strong> supports this claim?</p>",
         "choices": ["Labeled carbon that first showed up in the plant's sugar later showed up in its proteins.",
                     "Plants need sunlight to grow.",
                     "Proteins are found in a plant's seeds and leaves.",
                     "Plants are green because they contain chlorophyll."],
         "answer": 0,
         "feedback": "Only the tracer evidence follows atoms from sugar into proteins. The other statements are true, but they don't connect sugar to proteins."},
        {"type": "choice",
         "prompt": "<p>Tomato plants are grown with the same light, water, and carbon dioxide. After 4 weeks:</p>"
                   "<table border=\"1\" cellpadding=\"4\"><tr><th>Group</th><th>Sugar in leaves (mg/g)</th><th>Protein in leaves (mg/g)</th></tr>"
                   "<tr><td>Normal nitrogen</td><td>12</td><td>30</td></tr><tr><td>Low nitrogen</td><td>25</td><td>8</td></tr></table>"
                   "<p>Which explanation <strong>best</strong> uses the data?</p>",
         "choices": ["The low-nitrogen plants still made plenty of sugar (25 mg/g), but without nitrogen they couldn't combine its atoms into amino acids, so their protein stayed low (8 mg/g).",
                     "The low-nitrogen plants couldn't do photosynthesis, so they had no sugar to build protein.",
                     "Nitrogen turns into sugar, so the normal-nitrogen plants should have had more sugar.",
                     "The low-nitrogen plants had low protein because the extra sugar destroyed their proteins."],
         "answer": 0,
         "feedback": "The sugar data show photosynthesis still worked. Protein was low because nitrogen, which sugar lacks, was missing, so the sugar piled up unused."},
        {"type": "choice",
         "prompt": "<p><strong>Claim:</strong> Corn needs both sugar and nitrogen to grow.<br><strong>Evidence:</strong> Corn grown with no nitrogen stayed small, even though its leaves were full of sugar.</p><p>Which sentence is the <strong>best reasoning</strong> to connect the evidence to the claim?</p>",
         "choices": ["Sugar supplies carbon, hydrogen, and oxygen, but amino acids also need nitrogen, and atoms can't be created, so without nitrogen the corn can't build the proteins it needs for new cells.",
                     "Corn is a plant, and all plants need fertilizer.",
                     "Nitrogen is the most common gas in the air.",
                     "The corn made sugar, so it should have grown normally."],
         "answer": 0,
         "feedback": "Good reasoning uses a science idea to explain why the evidence supports the claim. Here that means atoms from sugar plus nitrogen form amino acids, and atoms can't be made from nothing."},
        {"type": "multi",
         "prompt": "<p>Yeast are grown in sugar water. Flask A also has ammonium (a nitrogen source). Flask B does not. After 2 days, the yeast population in Flask A grew 10 times larger. Flask B barely grew, and most of its sugar was still there.</p><p>Select the <strong>TWO</strong> statements the evidence supports.</p>",
         "choices": ["The yeast needed nitrogen as well as sugar to build new cells.",
                     "Ammonium was the yeast's main source of carbon.",
                     "Sugar alone couldn't supply all the atoms needed to build new yeast cells.",
                     "The yeast in Flask B turned their sugar into nitrogen.",
                     "Yeast don't need sugar to grow."],
         "answer": [0, 2],
         "feedback": "Flask B had plenty of sugar but no nitrogen, and it barely grew, so sugar alone isn't enough. Cells can't turn sugar into nitrogen, and the carbon comes from the sugar."},
        {"type": "choice",
         "prompt": "<p>Which statement is the <strong>best</strong> scientific explanation of how a bean plant builds protein?</p>",
         "choices": ["The plant uses light energy to build sugar from carbon dioxide and water. It then rearranges the carbon, hydrogen, and oxygen atoms from that sugar and combines them with nitrogen from the soil to make amino acids, which link into proteins.",
                     "The plant absorbs proteins from the soil through its roots and stores them in its seeds.",
                     "The plant turns sunlight into protein in its leaves.",
                     "The plant makes sugar, and the sugar becomes protein without needing any other elements."],
         "answer": 0,
         "feedback": "A complete explanation follows the atoms (CO2 and water to sugar, then sugar plus nitrogen to amino acids and protein) and keeps light energy separate from matter."},
    ],
    "LS1-6.6": [
        {"type": "choice",
         "prompt": "<p>A student's first explanation: \"A tree gets its mass from the soil.\"</p><p><strong>New evidence:</strong> In a 5-year experiment, a willow tree in a pot gained 74 kg, but the soil in the pot lost only 0.06 kg.</p><p>Which revision <strong>best</strong> fits the new evidence?</p>",
         "choices": ["Most of the tree's mass came from carbon dioxide and water, built into sugar and then other molecules. The soil supplied only small amounts of elements like nitrogen.",
                     "The tree's mass came from the soil, so the scale must have been wrong.",
                     "The tree's mass came from sunlight, which turned into wood.",
                     "The tree's mass came only from the water it absorbed."],
         "answer": 0,
         "feedback": "The soil lost almost nothing, so the explanation has to change. Carbon from CO2, plus hydrogen and oxygen from water, is built into sugar and then into the tree's other molecules."},
        {"type": "choice",
         "prompt": "<p>A student's first explanation: \"Sugar alone is enough to build all of a plant's molecules.\"</p><p><strong>New evidence:</strong> Plants grown in a solution with no nitrogen make plenty of sugar but very little protein.</p><p>How should the student revise the explanation?</p>",
         "choices": ["Add that building amino acids and proteins also takes nitrogen from another source, such as the soil.",
                     "Remove sugar from the explanation, because plants don't use sugar to build molecules.",
                     "Add that nitrogen is used to make sugar.",
                     "Make no change, because the plants still made sugar."],
         "answer": 0,
         "feedback": "The evidence shows sugar alone isn't enough to make protein. The revision should keep sugar as the source of C, H, and O and add nitrogen as a second source."},
        {"type": "choice",
         "prompt": "<p>A student wrote: \"A cat stores the fish protein it eats in its own muscles.\" A peer reviewer replies: \"But cat muscle protein has a different order of amino acids than any fish protein.\"</p><p>Which revision <strong>best</strong> responds to the peer review?</p>",
         "choices": ["The cat breaks the fish proteins down into amino acids and rebuilds them, in a new order, into its own proteins.",
                     "The cat makes its amino acids from sunlight, not from the fish.",
                     "Keep the explanation, because peer reviewers are often wrong.",
                     "The fish protein slowly changes into cat protein without being broken down."],
         "answer": 0,
         "feedback": "A different amino acid order means the protein wasn't stored unchanged. The cat breaks it down and rearranges the parts into its own proteins."},
        {"type": "tf",
         "prompt": "<p>True or false: A student's explanation says, \"When a plant builds proteins, atoms from sugar are used up and disappear.\" A bead model in which no beads are ever added or lost supports keeping this explanation.</p>",
         "answer": False,
         "feedback": "False. The bead model shows that atoms are rearranged, not lost. The explanation should be revised to say that atoms from sugar are rearranged into new molecules."},
        {"type": "multi",
         "prompt": "<p>A student's first explanation: \"A seedling grows using only the matter stored in its seed.\"</p><p><strong>New evidence:</strong> Seedlings grown in light gained dry mass after their leaves opened. Seedlings grown in the dark lost dry mass.</p><p>Select the <strong>TWO</strong> revisions the evidence supports.</p>",
         "choices": ["In the dark, seedlings had to build their new parts from matter stored in the seed.",
                     "Light is turned directly into new plant matter.",
                     "In the light, seedlings also built new sugar from carbon dioxide and water, which added new matter.",
                     "Seedlings in the dark destroyed some of their atoms.",
                     "Water alone explains the gain in dry mass."],
         "answer": [0, 2],
         "feedback": "Dry mass leaves out water. In the dark, the seedlings could only rearrange stored matter, and some was used for energy. In the light, they added new matter by building sugar from CO2. Light is energy, and atoms aren't destroyed."},
    ],
}

# ===========================================================================
# Practice test (parallel to the CSA). 16 questions, 22 points.
# ===========================================================================
PRACTICE = [
    # LS1-6.1 (DOK 1): 3 one-point questions
    {"lt": "LS1-6.1", "type": "choice",
     "prompt": "<p>Table sugar (sucrose) is C<sub>12</sub>H<sub>22</sub>O<sub>11</sub>. Which elements does it contain?</p>",
     "choices": ["Carbon, hydrogen, and oxygen", "Carbon, hydrogen, oxygen, and nitrogen",
                 "Calcium, hydrogen, and oxygen", "Carbon and oxygen only"],
     "answer": 0,
     "feedback": "C = carbon, H = hydrogen, O = oxygen. Sugars are made of these three elements."},
    {"lt": "LS1-6.1", "type": "multi",
     "prompt": "<p>Select the <strong>TWO</strong> elements found in some amino acids that sugar does <strong>not</strong> supply.</p>",
     "choices": ["Carbon", "Nitrogen", "Oxygen", "Sulfur", "Hydrogen"],
     "answer": [1, 3],
     "feedback": "All amino acids contain nitrogen, and a few contain sulfur. Sugar has only carbon, hydrogen, and oxygen."},
    {"lt": "LS1-6.1", "type": "tf",
     "prompt": "<p>True or false: Most of the atoms in the large carbon-based molecules of your body are carbon, hydrogen, and oxygen.</p>",
     "answer": True,
     "feedback": "True. Carbon, hydrogen, and oxygen make up most of these molecules. Nitrogen, sulfur, and phosphorus are there in smaller amounts."},
    # LS1-6.2 (DOK 2): 3 one-point questions
    {"lt": "LS1-6.2", "type": "choice",
     "prompt": "<p>A caterpillar eats milkweed leaves and grows to many times its starting mass. Where do the atoms in the caterpillar's new body tissue come from?</p>",
     "choices": ["Molecules in the leaves, which the caterpillar breaks down and rearranges into its own molecules",
                 "Sunlight that the caterpillar absorbs while it feeds",
                 "New atoms that the caterpillar's cells create",
                 "The air the caterpillar breathes, which turns directly into body tissue"],
     "answer": 0,
     "feedback": "The caterpillar takes in matter as food. It breaks the leaf molecules down and rearranges their atoms into its own molecules. No atoms are created."},
    {"lt": "LS1-6.2", "type": "choice",
     "prompt": "<p>Two glucose molecules join to make a larger sugar. Fill in the missing product:</p><p>C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> &rarr; C<sub>12</sub>H<sub>22</sub>O<sub>11</sub> + ____</p>",
     "choices": ["H<sub>2</sub>O", "O<sub>2</sub>", "CO<sub>2</sub>", "H<sub>2</sub>"],
     "answer": 0,
     "feedback": "Left side: C12 H24 O12. The larger sugar has C12 H22 O11, so 2 H and 1 O are missing. Together those make H2O."},
    {"lt": "LS1-6.2", "type": "tf",
     "prompt": "<p>True or false: When a plant builds starch from sugar, some of the carbon atoms are destroyed.</p>",
     "answer": False,
     "feedback": "False. Chemical reactions rearrange atoms. They don't create or destroy them."},
    # LS1-6.3 (DOK 2): 3 one-point questions
    {**_from_bank(_find(P, "PMC 1"), "LS1-6.3")},
    {**_from_bank(_find(P, "PMC 2"), "LS1-6.3")},
    {"lt": "LS1-6.3", "type": "multi",
     "prompt": "<p>Select the <strong>TWO</strong> things a plant cell must have to build amino acids.</p>",
     "choices": ["Carbon, hydrogen, and oxygen atoms from sugar", "Sunlight, which turns directly into amino acids",
                 "A source of nitrogen, such as nitrate from the soil", "New carbon atoms made by the cell", "Heat from the soil"],
     "answer": [0, 2],
     "feedback": "Amino acids are built from atoms from sugar plus nitrogen. Light is the energy used to make sugar. It doesn't become matter."},
    # LS1-6.4 (DOK 2): 3 one-point questions
    {**_from_bank(_find(P, "PMC 4"), "LS1-6.4")},
    {**_from_bank(_find(P, "PMC 5"), "LS1-6.4")},
    {"lt": "LS1-6.4", "type": "choice",
     "prompt": "<p>In a bead model, black = carbon, white = hydrogen, red = oxygen, and blue = nitrogen. A student takes apart one glucose model (6 black, 12 white, 6 red) and wants to build <strong>2</strong> models of the amino acid alanine. Each alanine is C<sub>3</sub>H<sub>7</sub>NO<sub>2</sub>.</p><p>Which beads must the student add from <strong>outside</strong> the glucose model?</p>",
     "choices": ["2 blue beads and 2 white beads", "6 black beads", "No beads. Glucose has everything needed.", "2 red beads"],
     "answer": 0,
     "feedback": "Two alanine need 6 C, 14 H, 2 N, and 4 O. Glucose gives 6 C, 12 H, and 6 O, so the student must add 2 N (blue) and 2 more H (white). There will be 2 red beads left over."},
    # LS1-6.5 (DOK 3): 1 multiple choice + 1 written response
    {**_from_bank(_find(P, "PMC 3"), "LS1-6.5")},
    {**_essay_from_bank(_find(P, "PFR 1"), "LS1-6.5")},
    # LS1-6.6 (DOK 3): 1 multiple choice + 1 written response
    {"lt": "LS1-6.6", "type": "choice",
     "prompt": "<p>A student's first explanation: \"Fertilizer is plant food. It gives plants the energy they need to grow.\"</p>"
               "<p>New evidence:</p><ul><li>Plants given fertilizer but kept in the dark died.</li>"
               "<li>The fertilizer label lists nitrogen, phosphorus, and potassium, and no sugar.</li>"
               "<li>Labeled nitrogen from the fertilizer later showed up in the plants' proteins.</li></ul>"
               "<p>Which revision <strong>best</strong> fits all of the evidence?</p>",
     "choices": ["Fertilizer supplies elements like nitrogen, which plants combine with atoms from the sugar they make using light energy to build amino acids, proteins, and other molecules.",
                 "Fertilizer gives plants energy, but only when it's light outside.",
                 "Fertilizer contains sugar that the plant builds into proteins.",
                 "Fertilizer turns into light energy inside the plant."],
     "answer": 0,
     "feedback": "The plants died in the dark, so fertilizer isn't their energy source. Fertilizer has no sugar, so it isn't food. The tracer shows its nitrogen ends up in proteins. Fertilizer supplies building elements, and light powers sugar-making."},
    {"lt": "LS1-6.6", "type": "essay",
     "prompt": "<p>In Lesson 1, a student explained the giant pumpkin like this:</p>"
               "<blockquote>\"The pumpkin gets most of its solid matter from the soil. The roots suck up soil and build it into the pumpkin.\"</blockquote>"
               "<p>New evidence:</p><ul>"
               "<li><strong>Soil data:</strong> A grower weighed the dry soil in a pumpkin bed before and after a season. The soil lost about 1 kg. The pumpkin's dry mass (with the water removed) was about 60 kg.</li>"
               "<li><strong>Tracer study:</strong> Pumpkin plants were given carbon dioxide with labeled carbon. The labeled carbon showed up first in leaf sugar, then in the pumpkin's starch and proteins.</li>"
               "<li><strong>Fertilizer test:</strong> Pumpkin plants with no nitrogen fertilizer still made sugar in their leaves, but they grew small, pale fruit with very little protein.</li></ul>"
               "<p>Using this evidence:</p><ol>"
               "<li><strong>Evaluate:</strong> Identify what is <em>not</em> supported in the student's explanation, and what part of it the soil <em>does</em> contribute. Cite evidence for each.</li>"
               "<li><strong>Revise:</strong> Write an improved explanation that traces carbon atoms from the <em>air</em> into the <em>pumpkin's proteins</em>. Describe how carbon, hydrogen, and oxygen from sugar combine with other elements (such as nitrogen) to form amino acids and proteins.</li>"
               "<li><strong>Connect:</strong> Explain how your revised explanation shows that matter is conserved.</li></ol>",
     "rubric": [
         (4, "Advanced",
          "Correctly evaluates both parts with evidence: the soil lost about 1 kg against about 60 kg of pumpkin dry mass, which refutes \"most matter from soil,\" and the fertilizer test shows the soil supplies nitrogen. "
          "The revision traces carbon completely: CO2 from the air goes into leaf sugar through photosynthesis. Atoms from sugar combine with nitrogen from the soil to form amino acids, which link into proteins. "
          "Clearly explains conservation: atoms are rearranged, and none are created or destroyed."),
         (3, "Proficient",
          "Evaluates both parts, with evidence for at least one. The revision includes CO2 to sugar to amino acids and protein, and includes nitrogen, but one step is thin. "
          "Mentions conservation briefly."),
         (2, "Developing",
          "Evaluates only one part. The revision skips sugar or nitrogen, or still says most matter comes from soil. Conservation is vague or missing."),
         (1, "Beginning",
          "Repeats the original explanation or shows a major misconception (for example, sunlight becomes matter). Little or no evidence."),
     ],
     "grading_notes": [
         "Key data contrast: about 1 kg soil lost vs. about 60 kg pumpkin dry mass. The soil can't be the main source.",
         "The soil DOES contribute small amounts of elements like nitrogen. The fertilizer test is the evidence for this.",
         "Common misconception: sunlight becomes the pumpkin's mass. Light is the energy used to build sugar, not the matter.",
         "Don't take off points for leaving out chemical reaction details or names of macromolecule types. Both are outside the HS-LS1-6 assessment boundary.",
     ],
     "exemplar": (
         "The student is wrong that most of the pumpkin's matter comes from the soil: the soil lost only about 1 kg, but the pumpkin's dry mass was about 60 kg. "
         "The soil does supply nitrogen, because plants without nitrogen fertilizer made sugar but grew small fruit with little protein. "
         "Revised: The pumpkin plant takes in carbon dioxide from the air and uses light energy to build sugar in its leaves, as the tracer showed. "
         "The plant rearranges the carbon, hydrogen, and oxygen atoms from that sugar and combines them with nitrogen from the soil to make amino acids, which link into proteins in the pumpkin. "
         "Matter is conserved because the atoms in the pumpkin all came from CO2, water, and the soil. They were only rearranged into new molecules, never created."
     )},
]

# ===========================================================================
# CSA (built from questions.py). 16 questions, 22 points. No feedback shown.
# ===========================================================================
CSA = [
    # LS1-6.1 (DOK 1)
    {"lt": "LS1-6.1", "type": "choice",
     "prompt": "<p>A protein in a bean seed contains carbon, hydrogen, oxygen, nitrogen, and sulfur. Which of these elements could have come from the sugar the bean plant made?</p>",
     "choices": ["Carbon, hydrogen, and oxygen", "Nitrogen and sulfur", "All five elements", "Carbon only"],
     "answer": 0, "feedback": ""},
    {"lt": "LS1-6.1", "type": "multi",
     "prompt": "<p>Select the <strong>TWO</strong> true statements about the elements in sugar and in large carbon-based molecules.</p>",
     "choices": ["Sugar contains nitrogen.", "All of them contain carbon.",
                 "Most of the atoms in them are iron and calcium.",
                 "Amino acids contain nitrogen as well as carbon, hydrogen, and oxygen.",
                 "Sugar contains sulfur."],
     "answer": [1, 3], "feedback": ""},
    {"lt": "LS1-6.1", "type": "tf",
     "prompt": "<p>True or false: Glucose (C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>) contains carbon, hydrogen, oxygen, and nitrogen.</p>",
     "answer": False, "feedback": ""},
    # LS1-6.2 (DOK 2)
    {**_from_bank(_find(S, "MC 8"), "LS1-6.2", feedback=False)},
    {"lt": "LS1-6.2", "type": "choice",
     "prompt": "<p>Photosynthesis can be written as:</p><p>6 CO<sub>2</sub> + 6 H<sub>2</sub>O &rarr; C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + 6 O<sub>2</sub></p><p>How many <strong>carbon</strong> atoms are on each side?</p>",
     "choices": ["6 on the left and 6 on the right", "6 on the left and 12 on the right",
                 "12 on the left and 6 on the right", "1 on the left and 6 on the right"],
     "answer": 0, "feedback": ""},
    {"lt": "LS1-6.2", "type": "tf",
     "prompt": "<p>True or false: When a cow digests grass and builds its own muscle, the atoms from the grass are rearranged, not destroyed.</p>",
     "answer": True, "feedback": ""},
    # LS1-6.3 (DOK 2)
    {**_from_bank(_find(S, "MC 1"), "LS1-6.3", feedback=False)},
    {**_from_bank(_find(S, "MC 3"), "LS1-6.3", feedback=False)},
    {**_from_bank(_find(S, "MC 9"), "LS1-6.3", feedback=False)},
    # LS1-6.4 (DOK 2)
    {**_from_bank(_find(S, "MC 2"), "LS1-6.4", feedback=False)},
    {**_from_bank(_find(S, "MC 7"), "LS1-6.4", feedback=False)},
    {**_from_bank(_find(S, "MC 5"), "LS1-6.4", feedback=False)},
    # LS1-6.5 (DOK 3)
    {**_from_bank(_find(S, "MC 4"), "LS1-6.5", feedback=False)},
    {**_essay_from_bank(_find(S, "FR 1"), "LS1-6.5")},
    # LS1-6.6 (DOK 3)
    {**_from_bank(_find(S, "MC 10"), "LS1-6.6", feedback=False)},
    {**_essay_from_bank(_find(S, "FR 2"), "LS1-6.6")},
]
