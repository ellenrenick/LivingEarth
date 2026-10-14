"""Question bank for the HS-LS3-2 CSA: Inherited Instructions (unit 2.2).

45-minute test, 30 points. Edit, then run `python3 ../build_unit.py HS-LS3-2`.
Boundary: no phases of meiosis; no biochemical mechanism of specific steps.
"""

TITLE = "HS-LS3-2 Assessment: Inherited Instructions"
STANDARD = "HS-LS3-2"
QUIZ_ID = "hs_ls3_2_inherited_instructions"
FILE_PREFIX = "HS-LS3-2"
MAX_ATTEMPTS = 1
TIME_MINUTES = 45
KEY_POSITIONS = [0, 2, 3, 1, 0, 3, 2, 1]

DESCRIPTION = (
    "<p><strong>Living Earth (Biology) &ndash; HS-LS3-2</strong></p>"
    "<p>Make and defend a claim based on evidence that inheritable genetic variations may result "
    "from (1) new genetic combinations through meiosis, (2) viable errors occurring during "
    "replication, and/or (3) mutations caused by environmental factors.</p>"
    "<p>Part 1: Vocabulary matching &middot; Part 2: Multiple choice &middot; Part 3: Free response</p>"
)

MATCHING = {
    "title": "Part 1: Vocabulary Matching",
    "points": 6,
    "prompt": "<p>Match each term with its best definition. Some definitions will not be used.</p>",
    "pairs": [
        ("Genetic variation", "Differences in genes among the individuals of a population"),
        ("Allele", "One of the different versions of the same gene"),
        ("Sex cell (gamete)", "A cell, such as an egg or a sperm, that carries half of a parent's genetic information"),
        ("Meiosis", "The kind of cell division that makes sex cells with half the genetic information of the parent cell"),
        ("Fertilization", "The joining of a sperm and an egg to form a new cell with genetic information from both parents"),
        ("Mutation", "A change in the base sequence of DNA"),
    ],
    "distractors": [
        "The kind of cell division that makes two identical body cells for growth and repair",
        "A trait that a person learns or gains during life, such as a scar",
    ],
}

MULTIPLE_CHOICE = [
    {
        "title": "MC 1 - Why siblings differ",
        "dok": 2,
        "prompt": (
            "<p>Two brothers have the same mother and father, yet one has curly hair and one has straight hair. "
            "Both parents have wavy hair and carry one allele for curly hair and one for straight hair.</p>"
            "<p>Which statement <strong>best</strong> explains how the brothers got different hair types?</p>"
        ),
        "choices": [
            "Each parent's sex cells carry a different mix of the parent's alleles, and fertilization joins two sex cells at random, making a different new combination in each brother.",
            "Each brother's hair was changed by a mutation caused by the environment after he was born.",
            "Each brother copied his hair type from the other children at school.",
            "The parents' genes changed to match the first child.",
        ],
        "answer": 0,
        "feedback": "Meiosis gives each sex cell a different mix of alleles, and fertilization combines two of them. This creates new genetic combinations, even in brothers with the same parents.",
    },
    {
        "title": "MC 2 - Sunburn and the next generation",
        "dok": 3,
        "prompt": (
            "<p>A hiker gets a bad sunburn. Ultraviolet (UV) light causes a mutation in some of her skin cells. "
            "A friend says, &ldquo;She will pass that mutation to her children.&rdquo;</p>"
            "<p>Which response is <strong>best</strong>?</p>"
        ),
        "choices": [
            "Not necessarily: a mutation in a skin cell is not passed on, but a mutation in a cell that makes eggs or sperm could be passed to a child.",
            "Yes: all mutations in any cell are passed to children.",
            "No: UV light cannot cause mutations.",
            "Yes: skin cells make the sex cells.",
        ],
        "answer": 0,
        "feedback": "UV light can cause mutations, but only changes in cells that become sex cells can be inherited by children.",
    },
    {
        "title": "MC 3 - New changes in children",
        "dok": 3,
        "prompt": (
            "<p>Scientists sequence the DNA of three children and both of their parents. They find base changes in each child "
            "that are <strong>not</strong> found in either parent:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Child</th><th>New base changes not found in either parent</th></tr>"
            "<tr><td>1</td><td>58</td></tr>"
            "<tr><td>2</td><td>63</td></tr>"
            "<tr><td>3</td><td>70</td></tr>"
            "</table>"
            "<p>Which conclusion is <strong>best supported</strong> by these data?</p>"
        ),
        "choices": [
            "Every child gets a small number of brand-new changes that arise when DNA is copied, so mistakes in copying are one source of variation.",
            "The children's DNA is identical to their parents' DNA.",
            "The new changes must all have been caused by the children's diet.",
            "The new changes show that the parents' genes disappear after one generation.",
        ],
        "answer": 0,
        "feedback": "Changes found in the children but in neither parent must have arisen during copying of DNA. Errors in replication create new variations.",
    },
    {
        "title": "MC 4 - Where did the variation come from?",
        "dok": 2,
        "prompt": (
            "<p>A gene has these versions. Parent 1 has the sequences <strong>GAG</strong> and <strong>GAG</strong>. "
            "Parent 2 has <strong>GAG</strong> and <strong>GTG</strong>. Their two children have:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Child</th><th>Gene sequences</th></tr>"
            "<tr><td>A</td><td>GAG and GTG</td></tr>"
            "<tr><td>B</td><td>GAG and GCG</td></tr>"
            "</table>"
            "<p>Which statement <strong>best</strong> explains the variation in the children?</p>"
        ),
        "choices": [
            "Child A's combination came from alleles that were already in the parents; Child B's GCG is a new variation, because neither parent has it, so it came from a mutation.",
            "Both children's combinations came from alleles that were already in the parents.",
            "Both children's variations are new mutations, because they differ from Parent 1.",
            "Child B's GCG came from Parent 2, because Parent 2 has a T in the sequence.",
        ],
        "answer": 0,
        "feedback": "GAG and GTG both appear in the parents, so Child A's pair is a new combination. GCG appears in neither parent, so it must have come from a change in the DNA.",
    },
    {
        "title": "MC 5 - Seeds exposed to UV light",
        "dok": 3,
        "prompt": (
            "<p>A scientist grows 1,000 seedlings from each of two groups of seeds under the same conditions. "
            "Group 1 seeds are from plants kept in normal light. Group 2 seeds are from plants exposed to strong UV light "
            "while their flowers were forming. She counts seedlings with a new leaf color not seen in the parent plants.</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Group</th><th>Seedlings with the new leaf color (out of 1,000)</th></tr>"
            "<tr><td>1 (normal light)</td><td>2</td></tr>"
            "<tr><td>2 (strong UV light)</td><td>41</td></tr>"
            "</table>"
            "<p>Which conclusion is <strong>best supported</strong>?</p>"
        ),
        "choices": [
            "UV light caused mutations in the cells that made the seeds, and those mutations were inherited by the seedlings.",
            "UV light turns normal leaves a new color only after the seedlings grow.",
            "The new leaf color is caused by the soil, because the soil was the same.",
            "Mutations can only occur in normal light.",
        ],
        "answer": 0,
        "feedback": "The seeds were exposed before the seedlings grew, and all seedlings were grown under the same conditions, so the difference is inherited. UV light raised the number of mutations.",
    },
    {
        "title": "MC 6 - Making sex cells",
        "dok": 2,
        "prompt": (
            "<p>A plant has two alleles for flower color: <strong>R</strong> and <strong>r</strong>. Another plant "
            "has the same two alleles. A student wants to explain how their seeds can have different color combinations.</p>"
            "<p>Which statement <strong>best</strong> describes how meiosis and fertilization create new combinations?</p>"
        ),
        "choices": [
            "Meiosis puts one of each parent's alleles into each sex cell, so sex cells can carry R or r, and fertilization can join any two of them to make RR, Rr, or rr.",
            "Meiosis copies all of the parent's alleles into every sex cell, so every seed is identical.",
            "Fertilization changes the alleles in the sex cells before they join.",
            "Meiosis makes new alleles that did not exist in either parent.",
        ],
        "answer": 0,
        "feedback": "Each sex cell gets one allele. Fertilization joins two sex cells, so offspring can be RR, Rr, or rr. This mixes existing alleles into new combinations.",
    },
    {
        "title": "MC 7 - Defend the claim",
        "dok": 3,
        "prompt": (
            "<p>A rare spotted pattern appears in some beetles. Student 1 claims it is caused by a mutation from pond pollution. "
            "Student 2 claims it is a new combination of alleles that were already in the beetle population. "
            "The class gathers this evidence:</p>"
            "<ul>"
            "<li>Beetles with the pattern appear at about the same rate (3 in 100) in polluted and clean ponds.</li>"
            "<li>Both parents of every spotted beetle carry one allele for the pattern.</li>"
            "</ul>"
            "<p>Which statement <strong>best</strong> defends the correct claim with this evidence?</p>"
        ),
        "choices": [
            "Student 2 is better supported: the pattern appears just as often without pollution, and the parents both carry the allele, so it fits new combinations of existing alleles.",
            "Student 1 is better supported: the pattern appears in polluted ponds, so pollution caused it.",
            "Both students are wrong, because patterns cannot be inherited.",
            "Student 1 is better supported: all rare traits are caused by mutations.",
        ],
        "answer": 0,
        "feedback": "If pollution caused the pattern, polluted ponds would have more spotted beetles. The same rate in clean ponds and the parents' alleles point to inherited combinations.",
    },
    {
        "title": "MC 8 - Correcting a misconception",
        "dok": 2,
        "prompt": (
            "<p>A student writes, &ldquo;All mutations are harmful, and every mutation is passed on to children.&rdquo;</p>"
            "<p>Which revision is <strong>most accurate</strong>?</p>"
        ),
        "choices": [
            "Mutations can be harmful, helpful, or have no effect, and only mutations in cells that make sex cells can be passed on to children.",
            "Mutations are never harmful, and all of them are passed on to children.",
            "Mutations only occur in the environment, never in DNA.",
            "Mutations are always helpful, so they are always passed on.",
        ],
        "answer": 0,
        "feedback": "Mutations have varied effects. They are inherited only when they occur in cells that become sex cells.",
    },
]

FREE_RESPONSE = [
    {
        "title": "FR 1 - Two mouse stories",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>A lab keeps careful family records for its mice. Two unusual events happened:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th></th><th>Event 1</th><th>Event 2</th></tr>"
            "<tr><td>What happened</td><td>Two brown mice had a white pup.</td><td>A mouse was born with a new curly-fur trait.</td></tr>"
            "<tr><td>Family records</td><td>White fur appeared in the pup's grandfather. Both parents' DNA includes one allele for white fur.</td><td>No curly fur in the previous 12 generations. The mother had been exposed to strong radiation while pregnant.</td></tr>"
            "<tr><td>DNA test</td><td>The pup has two copies of the white-fur allele.</td><td>The curly mouse has a base change in a fur gene that neither parent has.</td></tr>"
            "</table>"
            "<p>Write a scientific explanation using <strong>Claim, Evidence, and Reasoning</strong>:</p>"
            "<ol>"
            "<li><strong>Claim:</strong> State the most likely source of the variation in each event.</li>"
            "<li><strong>Evidence:</strong> Use at least <strong>two</strong> pieces of data from the table (at least one for each event).</li>"
            "<li><strong>Reasoning:</strong> Explain how each source produces a variation that can be inherited. Include why the radiation in Event 2 matters.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Correct claims for both events: Event 1 is a new combination of existing alleles (meiosis and fertilization); Event 2 is a mutation, likely caused by radiation. "
             "At least two accurate data points that cover both events. "
             "Reasoning explains that sex cells carry one allele each and fertilization joined two white-fur alleles, and that radiation can change DNA bases in cells that make sex cells so the change is inherited."),
            (3, "Proficient",
             "Correct claims for both events and two accurate data points. "
             "Reasoning explains one event fully and the other briefly, or leaves out why the change is inherited."),
            (2, "Developing",
             "One claim correct or both partly correct. One data point or data used inaccurately. "
             "Reasoning is vague (for example, \"it was genetic\") without a mechanism."),
            (1, "Beginning",
             "Claims missing or wrong. Little or no data. Reasoning shows a major misconception (for example, the mouse chose to change its fur)."),
        ],
        "grading_notes": [
            "Event 1 data: the grandfather had white fur; both parents carry one white allele; the pup has two copies. Event 2 data: no curly fur in 12 generations; base change that neither parent has; mother exposed to radiation.",
            "Accept a copying error as a possible additional cause for Event 2; the radiation is the best-supported cause.",
            "Do not require phases of meiosis or any chemical mechanism; they are outside the HS-LS3-2 assessment boundary.",
            "Common misconceptions: the white pup came from a mutation; the mother's radiation exposure changed the pup's fur after birth.",
        ],
        "exemplar": (
            "Event 1 is most likely a new combination of alleles that were already in the family, and Event 2 is most likely a mutation caused by radiation. "
            "In Event 1, white fur appeared in the pup's grandfather and both parents carry one white allele, and the pup has two copies of it. In Event 2, there was no curly fur in 12 generations and the curly mouse has a base change that neither parent has. "
            "During meiosis each sex cell gets only one allele, and when a sperm and egg that both carry the white allele join in fertilization, the pup gets two copies, so white fur shows. "
            "Radiation can change the bases in DNA, and the mother's exposure likely caused a mutation in a cell that became a sex cell, so the change was passed to the pup and is inherited."
        ),
    },
    {
        "title": "FR 2 - Is the flower color inherited?",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>A gardener finds one plant with bright orange flowers. All the other plants in the garden have yellow flowers. "
            "Student A says, &ldquo;The soil in that spot changed the flower color, so it is not genetic.&rdquo; "
            "Student B says, &ldquo;A mutation in the seed that grew into this plant caused the orange color, so it is genetic.&rdquo;</p>"
            "<p>The gardener collects seeds and grows them in the same soil as the yellow plants:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Seeds from</th><th>Seeds planted</th><th>Plants with orange flowers</th></tr>"
            "<tr><td>The orange plant</td><td>100</td><td>48</td></tr>"
            "<tr><td>Yellow plants</td><td>100</td><td>0</td></tr>"
            "</table>"
            "<ol>"
            "<li><strong>Claim:</strong> Which student is better supported? </li>"
            "<li><strong>Evidence:</strong> Use at least two pieces of data to defend your claim.</li>"
            "<li><strong>Reasoning:</strong> Explain why the data rule out the other explanation. Then name one cause that could have produced the mutation, and explain why the mutation had to be in a cell that makes seeds for the orange color to be inherited.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Claims Student B (inherited variation). Cites at least two accurate data points (48 of 100 seeds from the orange plant produce orange flowers versus 0 of 100 from yellow plants, all grown in the same soil). "
             "Explains that if soil caused the color, seeds from the orange plant would grow into yellow plants in the same soil. "
             "Names a plausible cause (a copying error or an environmental factor such as UV light or chemicals) and explains that only a mutation in cells that make seeds (sex cells) is passed to offspring."),
            (3, "Proficient",
             "Correct claim and two accurate data points. Rules out the soil explanation, but the cause of the mutation or why it must be in a sex-cell-producing cell is brief or missing."),
            (2, "Developing",
             "Correct claim with one data point, or a correct claim with inaccurate data use. The reasoning does not rule out the other explanation."),
            (1, "Beginning",
             "Claim missing or wrong (supports Student A). Little or no data. Reasoning shows a major misconception."),
        ],
        "grading_notes": [
            "The key data contrast: 48 of 100 versus 0 of 100 orange plants, in the same soil.",
            "The reasoning for ruling out Student A: the same soil produced orange plants from the orange plant's seeds and yellow plants from the yellow plants' seeds, so the difference came from the seeds.",
            "Accept any plausible cause of the mutation: a copying error when cells divided, UV light, chemicals, or radiation.",
            "Do not require chemical or molecular mechanisms; they are outside the HS-LS3-2 assessment boundary.",
        ],
        "exemplar": (
            "Student B is better supported. When the gardener planted 100 seeds from the orange plant in the same soil as the yellow plants, 48 grew into orange-flowered plants, while 0 of the 100 seeds from yellow plants did. "
            "If the soil had changed the color, seeds from the orange plant would have grown into yellow plants in this soil, so the color is inherited. "
            "A mutation in the plant's DNA could have been caused by a copying error or by UV light. For the color to be passed on, the mutation had to be in a cell that makes seeds, because only the genetic information in sex cells and seeds is passed to the next generation."
        ),
    },
]
