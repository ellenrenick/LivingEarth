"""Question bank for the HS-LS1-1 CSA: DNA to Proteins (unit 2.1).

45-minute test, 30 points. Edit, then run `python3 ../build_unit.py HS-LS1-1`.
Boundary: no specific cell or tissue types, whole body systems, specific protein
structures and functions, or the biochemistry of protein synthesis. No mRNA/tRNA items.
"""

TITLE = "HS-LS1-1 Assessment: DNA to Proteins"
STANDARD = "HS-LS1-1"
QUIZ_ID = "hs_ls1_1_dna_to_proteins"
FILE_PREFIX = "HS-LS1-1"
MAX_ATTEMPTS = 1
TIME_MINUTES = 45
KEY_POSITIONS = [3, 1, 0, 2, 0, 3, 1, 2]

DESCRIPTION = (
    "<p><strong>Living Earth (Biology) &ndash; HS-LS1-1</strong></p>"
    "<p>Construct an explanation based on evidence for how the structure of DNA determines "
    "the structure of proteins, which carry out the essential functions of life through "
    "systems of specialized cells.</p>"
    "<p>Part 1: Vocabulary matching &middot; Part 2: Multiple choice &middot; Part 3: Free response</p>"
)

CODE_TABLE = (
    "<table border=\"1\" cellpadding=\"4\">"
    "<tr><th>DNA triplet</th><th>Amino acid</th><th>DNA triplet</th><th>Amino acid</th></tr>"
    "<tr><td>ATG</td><td>Met</td><td>GAG</td><td>Glu</td></tr>"
    "<tr><td>CTG</td><td>Leu</td><td>GTG</td><td>Val</td></tr>"
    "<tr><td>TTT</td><td>Phe</td><td>GAC</td><td>Asp</td></tr>"
    "<tr><td>CCT</td><td>Pro</td><td>GGC</td><td>Gly</td></tr>"
    "</table>"
)

MATCHING = {
    "title": "Part 1: Vocabulary Matching",
    "points": 6,
    "prompt": "<p>Match each term with its best definition. Some definitions will not be used.</p>",
    "pairs": [
        ("DNA", "The molecule in a cell that stores the instructions for building proteins, shaped like a twisted ladder"),
        ("Nucleotide", "One of the repeating building blocks of DNA, made of a sugar, a phosphate, and a base"),
        ("Gene", "A section of DNA that holds the instructions for one protein"),
        ("Base sequence", "The order of the bases (A, T, C, G) along a strand of DNA"),
        ("Amino acid", "One of the small building blocks that are linked in a chain to make a protein"),
        ("Protein", "A large molecule made of a chain of amino acids that carries out jobs for the cell"),
    ],
    "distractors": [
        "A group of similar cells that work together to do a specific job",
        "The process by which a cell divides to make two new cells",
    ],
}

MULTIPLE_CHOICE = [
    {
        "title": "MC 1 - Modeling DNA",
        "dok": 2,
        "prompt": (
            "<p>A student builds a model of DNA from paper and pipe cleaners. Which set of features "
            "must her model show to represent DNA <strong>correctly</strong>?</p>"
        ),
        "choices": [
            "Two strands twisted into a double helix, built from repeating nucleotides, each with a sugar, a phosphate, and a base",
            "A single straight strand made of amino acids joined together",
            "Two strands twisted together, each made only of sugar molecules",
            "A ball-shaped molecule made of phosphate groups with no bases",
        ],
        "answer": 0,
        "feedback": "DNA is a double helix built from nucleotides. Each nucleotide has a sugar, a phosphate, and a base. Amino acids make up proteins, not DNA.",
    },
    {
        "title": "MC 2 - Reading a gene",
        "dok": 2,
        "prompt": (
            "<p>The code table below shows the amino acid that each DNA triplet (three bases in a row) calls for.</p>"
            + CODE_TABLE +
            "<p>A gene has the base sequence <strong>ATG CTG TTT CCT</strong>. Which chain of amino acids "
            "will be built from this gene?</p>"
        ),
        "choices": [
            "Met &ndash; Leu &ndash; Phe &ndash; Pro",
            "Met &ndash; Phe &ndash; Leu &ndash; Pro",
            "Pro &ndash; Phe &ndash; Leu &ndash; Met",
            "Met &ndash; Leu &ndash; Phe &ndash; Gly",
        ],
        "answer": 0,
        "feedback": "The triplets are read in order from the start: ATG = Met, CTG = Leu, TTT = Phe, CCT = Pro. The base sequence sets the amino acid order.",
    },
    {
        "title": "MC 3 - One base changes",
        "dok": 2,
        "prompt": (
            "<p>Use the code table.</p>"
            + CODE_TABLE +
            "<p>A gene normally reads <strong>ATG GAG GAC</strong>. In one person, a single base changes and the gene "
            "reads <strong>ATG GTG GAC</strong>. Which statement <strong>best</strong> describes the effect?</p>"
        ),
        "choices": [
            "The second amino acid in the chain changes from Glu to Val, so the protein that is built is different and may work differently.",
            "The protein is exactly the same, because only one base changed.",
            "No protein is built, because every change in DNA stops protein building.",
            "All three amino acids change, because one base change affects the whole chain.",
        ],
        "answer": 0,
        "feedback": "GAG calls for Glu and GTG calls for Val. One changed base changed one amino acid. A different amino acid chain can fold or work differently.",
    },
    {
        "title": "MC 4 - Copy, then read",
        "dok": 2,
        "prompt": (
            "<p>A student compares a cell to a kitchen. The recipe book is kept safe on a shelf and never leaves "
            "it. The cook makes a copy of one recipe, takes the copy to the counter, and follows it to make a dish.</p>"
            "<p>Which statement <strong>best</strong> matches this to how a cell uses a gene?</p>"
        ),
        "choices": [
            "The gene's message is copied, and the copy is read to link amino acids into a protein; the DNA itself stays protected in the nucleus.",
            "The whole DNA molecule leaves the nucleus and is taken apart to make a protein.",
            "The protein is copied into new DNA, which is then read.",
            "The amino acids are copied, and the copies are read to build DNA.",
        ],
        "answer": 0,
        "feedback": "A gene's message is copied and the copy is read to build the amino acid chain. This keeps the original DNA safe.",
    },
    {
        "title": "MC 5 - Same DNA, different jobs",
        "dok": 3,
        "prompt": (
            "<p>A biologist studies two types of cells from the same person. Each type of cell contains genes 1, 2, and 3. "
            "She measures which proteins each type of cell makes:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Cell type</th><th>Genes in the cell</th><th>Proteins the cell makes</th></tr>"
            "<tr><td>Type X</td><td>1, 2, 3</td><td>Protein 1, Protein 2</td></tr>"
            "<tr><td>Type Y</td><td>1, 2, 3</td><td>Protein 2, Protein 3</td></tr>"
            "</table>"
            "<p>Which explanation <strong>best</strong> accounts for the data?</p>"
        ),
        "choices": [
            "Both types of cells have all the genes, but each type uses a different set of genes to build proteins, so each type has different proteins that do different jobs.",
            "Type Y lost gene 1 and Type X lost gene 3, so they cannot make the other proteins.",
            "Proteins in a cell are made without using DNA, so DNA does not affect cell jobs.",
            "Type X and Type Y must have different DNA, because they make different proteins.",
        ],
        "answer": 0,
        "feedback": "Every cell has the same genes, but cells use different genes. The proteins a cell makes give it its specialized job.",
    },
    {
        "title": "MC 6 - Which statement is correct?",
        "dok": 2,
        "prompt": (
            "<p>Which statement <strong>best</strong> describes the relationship among DNA, proteins, and the "
            "functions of a cell?</p>"
        ),
        "choices": [
            "DNA holds the instructions; those instructions determine the amino acid order of proteins, and the proteins carry out jobs for the cell.",
            "DNA carries out most jobs in a cell, and proteins store the instructions for DNA.",
            "Proteins determine the base sequence of DNA, and DNA carries out jobs for the cell.",
            "DNA and proteins are the same molecule found in two different places.",
        ],
        "answer": 0,
        "feedback": "DNA stores instructions, the base sequence determines the amino acid sequence, and proteins do the work of the cell.",
    },
    {
        "title": "MC 7 - A case study",
        "dok": 3,
        "prompt": (
            "<p>Doctors study a condition caused by a single base change in one gene. They test three groups of people:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Group</th><th>Gene version in the DNA</th><th>Protein made</th><th>Health effect</th></tr>"
            "<tr><td>1</td><td>Normal</td><td>Works normally</td><td>No symptoms</td></tr>"
            "<tr><td>2</td><td>Single base changed</td><td>One amino acid is different; the protein works poorly</td><td>Serious symptoms</td></tr>"
            "<tr><td>3</td><td>Normal</td><td>Works normally</td><td>No symptoms</td></tr>"
            "</table>"
            "<p>Which conclusion is <strong>best supported</strong> by the data?</p>"
        ),
        "choices": [
            "A change in the DNA changed the amino acid chain, which changed how the protein works, and that affected the body.",
            "The symptoms are caused by the protein, not by the DNA, because DNA has no effect on proteins.",
            "Any change in a person's DNA causes symptoms.",
            "The protein changed first, and that caused the DNA to change.",
        ],
        "answer": 0,
        "feedback": "The data link DNA to protein to body effect: the changed DNA built a different protein, which did not work well, and the person had symptoms.",
    },
    {
        "title": "MC 8 - Does every change matter?",
        "dok": 3,
        "prompt": (
            "<p>A student claims, &ldquo;Whenever a base in a gene changes, the cell's protein will stop working.&rdquo; "
            "A scientist records three different single-base changes in the same gene:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Change</th><th>Amino acid chain</th><th>Protein works?</th></tr>"
            "<tr><td>A</td><td>Same as the normal chain</td><td>Yes</td></tr>"
            "<tr><td>B</td><td>One amino acid is different</td><td>Yes</td></tr>"
            "<tr><td>C</td><td>One amino acid is different</td><td>No</td></tr>"
            "</table>"
            "<p>Which statement <strong>best</strong> evaluates the student's claim?</p>"
        ),
        "choices": [
            "The claim is not supported: a base change can leave the protein unchanged or change it only slightly, and only some changes stop it from working.",
            "The claim is supported, because all three changes affect the protein.",
            "The claim is supported, because change C stops the protein.",
            "The data cannot be used, because DNA never changes the protein.",
        ],
        "answer": 0,
        "feedback": "Changes A and B left the protein working, so a base change does not always stop it. What matters is whether the amino acid chain changes and how.",
    },
]

FREE_RESPONSE = [
    {
        "title": "FR 1 - A gene and a health condition",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>A gene makes a protein that helps a cell move water. Doctors compare the DNA of a healthy "
            "person and a person with a condition that affects breathing.</p>"
            + CODE_TABLE +
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th></th><th>Healthy person</th><th>Person with the condition</th></tr>"
            "<tr><td>Base sequence of the gene</td><td>ATG CTG GAG GAC</td><td>ATG CTG GTG GAC</td></tr>"
            "<tr><td>Protein works?</td><td>Yes</td><td>No (too little water moves)</td></tr>"
            "</table>"
            "<p>Write an explanation using <strong>Claim, Evidence, and Reasoning</strong>:</p>"
            "<ol>"
            "<li><strong>Claim:</strong> Explain how the DNA difference caused the condition.</li>"
            "<li><strong>Evidence:</strong> Use at least <strong>two</strong> pieces of data from the tables.</li>"
            "<li><strong>Reasoning:</strong> Explain how the base sequence of a gene is copied and read to build an amino acid chain, how the change affects that chain, and how a different protein can change what a cell can do.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Accurate claim that the single base change altered the amino acid chain, producing a protein that does not work, which led to the condition. "
             "Cites at least two accurate data points (the sequences differ at one triplet, GAG versus GTG; the amino acid changes from Glu to Val; the protein does not work). "
             "Reasoning describes copy-then-read from gene to amino acid chain, links the base sequence to the amino acid order, and explains that a different chain can make a protein that works differently so the cell cannot do its job."),
            (3, "Proficient",
             "Accurate claim and two accurate data points. "
             "Reasoning links the base change to a different amino acid and to a protein that works differently, but leaves out one piece (for example, copy-then-read, or how the protein affects the cell)."),
            (2, "Developing",
             "Claim is partly correct (for example, \"the DNA is different\") without linking to the protein. "
             "One data point or inaccurate use of data. Reasoning is vague."),
            (1, "Beginning",
             "Claim is wrong or missing. Little or no data. Reasoning shows a major misconception (for example, the protein changes the DNA)."),
        ],
        "grading_notes": [
            "Key data: GAG (Glu) in the healthy gene versus GTG (Val) in the other; all other triplets are the same; the protein works in one and not in the other.",
            "Look for the idea of copy-then-read, and a link such as base sequence determines amino acid order, which determines the protein.",
            "Do not require the names mRNA, tRNA, ribosome, or any steps of protein synthesis; they are outside the HS-LS1-1 assessment boundary.",
            "Do not require the 3-D shape of the protein or its exact function; both are outside the boundary.",
            "Common misconception: a protein can change DNA, or DNA does the work of the cell.",
        ],
        "exemplar": (
            "The condition happens because one base in the gene changed, which changed one amino acid in the protein so that it no longer works. "
            "The healthy gene reads ATG CTG GAG GAC and the other reads ATG CTG GTG GAC; the third triplet changed from GAG, which calls for Glu, to GTG, which calls for Val, and the protein no longer works. "
            "A cell copies the message of a gene and reads the copy to link amino acids in order, so the base sequence sets the amino acid order. "
            "When one amino acid is different, the chain can build a protein that works differently. Here the protein cannot move enough water, so the cell cannot do its job and the person has symptoms."
        ),
    },
    {
        "title": "FR 2 - Same DNA, different cells",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>A student says, &ldquo;If all my cells have the same DNA, then all my cells must do the same job.&rdquo; "
            "A teacher shows her this data about two types of cells from one person:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th></th><th>Cell type P</th><th>Cell type Q</th></tr>"
            "<tr><td>Genes in the cell (DNA)</td><td>Genes 1, 2, 3, 4</td><td>Genes 1, 2, 3, 4</td></tr>"
            "<tr><td>Proteins the cell makes</td><td>Proteins 1 and 2</td><td>Proteins 3 and 4</td></tr>"
            "<tr><td>Main job</td><td>Carries signals</td><td>Squeezes to move the body</td></tr>"
            "</table>"
            "<ol>"
            "<li><strong>Evaluate</strong> the student's statement using at least two pieces of data.</li>"
            "<li><strong>Explain</strong> how the DNA, through proteins, gives these two types of cells different jobs.</li>"
            "<li><strong>Predict</strong> what would happen to the job of Cell type Q if the gene for Protein 3 had a base change that stopped Protein 3 from working. Explain your prediction.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Evaluates the statement correctly: the first part is supported (same genes) but the conclusion is not (different jobs), citing at least two data points. "
             "Explains that the cells use different genes, so they build different proteins that carry out different jobs. "
             "Predicts that Cell type Q would not do its job well or would lose it, linking the changed gene to the changed protein and then to the job."),
            (3, "Proficient",
             "Evaluates correctly with two data points. Explains that different genes lead to different proteins and jobs. "
             "Prediction is correct but the link from gene to protein to job is thin."),
            (2, "Developing",
             "Partially evaluates (for example, says the student is wrong without evidence). "
             "Explanation says cells have different DNA, or says different proteins without linking to the genes used. Prediction is vague."),
            (1, "Beginning",
             "Repeats the student's statement or shows a major misconception (for example, each cell has different DNA). Little evidence."),
        ],
        "grading_notes": [
            "Key data: both cells have genes 1 to 4; P makes proteins 1 and 2, Q makes proteins 3 and 4; the jobs differ.",
            "The idea to look for: same DNA, different genes used, different proteins, different jobs.",
            "Do not require names of real cell types, tissues, or body systems; they are outside the HS-LS1-1 assessment boundary.",
            "Common misconception: cells that do different jobs have different DNA.",
        ],
        "exemplar": (
            "The student is right that the cells have the same DNA, since both have genes 1, 2, 3, and 4, but she is wrong that they must do the same job. "
            "Cell type P makes Proteins 1 and 2 and carries signals, while Cell type Q makes Proteins 3 and 4 and squeezes to move the body. "
            "Each cell uses a different set of genes, so each builds different proteins, and the proteins carry out each cell's job. "
            "If the gene for Protein 3 had a base change that stopped Protein 3 from working, Cell type Q would not be able to do its job well, because the changed gene would make a protein that does not work and Q depends on that protein."
        ),
    },
]
