"""CFAs for HS-LS1-1 (unit 2.1): one short exit-ticket check per priority learning target.

Each CFA is worth 6 points (LS1-1.1 has 6 multiple-choice items covering both the structure of DNA and its role as instructions). MC items list the correct choice FIRST (the builder shuffles).
Teaching notes: no mRNA/tRNA mechanics; no specific cell types; no protein structure items.
"""

STANDARD = "HS-LS1-1"
UNIT = "2.1"
UNIT_TITLE = "DNA to Proteins"

CODE = ("<table border=\"1\" cellpadding=\"4\"><tr><th>DNA triplet</th><th>Amino acid</th></tr>"
        "<tr><td>ATG</td><td>Met</td></tr><tr><td>GAG</td><td>Glu</td></tr><tr><td>GTG</td><td>Val</td></tr>"
        "<tr><td>CTG</td><td>Leu</td></tr><tr><td>TTT</td><td>Phe</td></tr></table>")

CFAS = [
    {
        "id": "LS1-1.1", "dok": 1,
        "lt": "I can describe DNA as a double helix built from nucleotides, each with a sugar, a phosphate, and a base, and state that DNA holds the instructions for building proteins.",
        "items": [
            {"prompt": "<p>What shape is a DNA molecule?</p>",
             "choices": ["A double helix (a twisted ladder)", "A single straight chain", "A flat sheet", "A ball"],
             "feedback": "DNA is a double helix made of two strands."},
            {"prompt": "<p>What are the three parts of one nucleotide?</p>",
             "choices": ["A sugar, a phosphate, and a base", "An amino acid, a sugar, and a protein", "A gene, a base, and a cell", "Two bases and a protein"],
             "feedback": "Each nucleotide has a sugar, a phosphate, and a base."},
            {"prompt": "<p>The letters A, T, C, and G stand for the four</p>",
             "choices": ["bases in DNA", "kinds of amino acid", "kinds of protein", "kinds of cell"],
             "feedback": "A, T, C, and G are the four bases found in DNA."},
            {"prompt": "<p>DNA stores the instructions for building</p>",
             "choices": ["proteins", "sugars", "water", "light"],
             "feedback": "DNA holds the instructions for building proteins."},
            {"prompt": "<p>A section of DNA with the instructions for one protein is called a</p>",
             "choices": ["gene", "cell", "nucleotide", "tissue"],
             "feedback": "A gene is the section of DNA that holds the instructions for one protein."},
            {"prompt": "<p>Which statement is true?</p>",
             "choices": ["DNA holds instructions, and proteins do jobs for the cell.", "Proteins hold instructions, and DNA does jobs for the cell.",
                         "DNA and proteins are the same thing.", "Neither DNA nor proteins are found in cells."],
             "feedback": "DNA stores instructions and proteins carry out jobs."},
        ],
    },
    {
        "id": "LS1-1.2", "dok": 2,
        "lt": "I can describe how a gene's message is copied and read to build a chain of amino acids.",
        "items": [
            {"prompt": "<p>Which sequence best describes how a cell uses a gene?</p>",
             "choices": ["The gene's message is copied; the copy is read to link amino acids in order.", "The amino acids are copied; the copy is read to build DNA.",
                         "The DNA leaves the cell; the cell reads it outside.", "The protein is copied to make a gene."],
             "feedback": "A gene's message is copied and the copy is read to build a chain of amino acids."},
            {"prompt": "<p>What is built when a gene's copy is read?</p>",
             "choices": ["A chain of amino acids", "A new DNA molecule", "A sugar", "A new cell"],
             "feedback": "Reading the copy links amino acids into a chain."},
            {"prompt": "<p>In 1 or 2 sentences, describe how a gene's message becomes a chain of amino acids. Use the words <em>copy</em> and <em>read</em>.</p>",
             "points": 2,
             "criteria": [(2, "Says the gene's message is copied and the copy is read to link amino acids in order."),
                          (1, "Mentions copying or reading, or that the gene codes for amino acids, but not both."),
                          (0, "Blank or incorrect.")],
             "exemplar": "The message in a gene is copied. The copy is read in order, and amino acids are linked in that order to make a chain."},
        ],
    },
    {
        "id": "LS1-1.3", "dok": 2,
        "lt": "I can explain how changing one DNA base can change a protein and what it does.",
        "items": [
            {"prompt": CODE + "<p>A gene reads ATG GAG CTG. A base change makes it read ATG GTG CTG. What changes in the amino acid chain?</p>",
             "choices": ["Glu becomes Val", "Met becomes Leu", "Leu becomes Phe", "Nothing changes"],
             "feedback": "GAG calls for Glu and GTG calls for Val."},
            {"prompt": "<p>Why can a single base change make a protein work differently?</p>",
             "choices": ["It can change an amino acid in the chain, and a different chain can make a protein that works differently.",
                         "It always removes the gene from the cell.", "It turns the protein into DNA.", "It does not matter because every base is the same."],
             "feedback": "A changed base can mean a different amino acid, which can change how the protein works."},
            {"prompt": "<p>Explain in 1 or 2 sentences how a change in one base of a gene could change what a protein does.</p>",
             "points": 2,
             "criteria": [(2, "Links base change to a different amino acid and to a protein that works differently."),
                          (1, "Says the protein might change, but does not mention the amino acid."),
                          (0, "Blank or incorrect.")],
             "exemplar": "A changed base can change the amino acid that is added to the chain. A chain with a different amino acid can make a protein that works differently."},
        ],
    },
    {
        "id": "LS1-1.4", "dok": 3,
        "lt": "I can explain how DNA, through proteins, gives different cells their different jobs.",
        "items": [
            {"prompt": "<p>Two cells in the same person have the same genes but make different proteins. What explains this?</p>",
             "choices": ["Each cell uses a different set of its genes.", "Each cell has different DNA.", "Proteins are not made from genes.", "Only one of the cells has DNA."],
             "feedback": "All cells have the same genes, but they use different genes."},
            {"prompt": "<p>Cell type A makes Protein 1 and Cell type B makes Protein 2. Both have genes 1 and 2. Which statement is best supported?</p>",
             "choices": ["Cell A uses gene 1 and Cell B uses gene 2, so they have different jobs.", "Cell A has only gene 1.", "Cell B has no DNA.", "The cells must do the same job."],
             "feedback": "Using different genes leads to different proteins and jobs."},
            {"prompt": "<p>In 2 or 3 sentences, explain how two cells with the same DNA can have different jobs.</p>",
             "points": 2,
             "criteria": [(2, "Says the cells use different genes, build different proteins, and the proteins carry out the different jobs."),
                          (1, "Says the cells use different genes or make different proteins, but does not connect to jobs."),
                          (0, "Blank, or says the cells have different DNA.")],
             "exemplar": "Both cells have the same DNA, but each uses different genes. Using different genes means each builds different proteins, and those proteins do the cell's job."},
        ],
    },
    {
        "id": "LS1-1.5", "dok": 3,
        "lt": "I can use case data, like sickle cell, to explain how a DNA change affects the body.",
        "items": [
            {"prompt": "<table border=\"1\" cellpadding=\"4\"><tr><th>Person</th><th>Gene</th><th>Protein</th><th>Symptoms</th></tr><tr><td>1</td><td>Normal</td><td>Works</td><td>None</td></tr><tr><td>2</td><td>One base changed</td><td>Works poorly</td><td>Yes</td></tr></table><p>Which conclusion is best supported?</p>",
             "choices": ["The DNA change led to a protein that works poorly, and that caused symptoms.", "The symptoms caused the DNA to change.",
                         "The protein has no link to the symptoms.", "DNA changes never matter."],
             "feedback": "The data connect the DNA change to the protein and to the symptoms."},
            {"prompt": "<p>Which sequence correctly shows how a DNA change can affect the body?</p>",
             "choices": ["DNA change &rarr; different amino acid chain &rarr; protein works differently &rarr; effect on the body",
                         "Effect on the body &rarr; protein change &rarr; DNA change", "Protein change &rarr; DNA change &rarr; amino acid change",
                         "DNA change &rarr; no change in any protein"],
             "feedback": "DNA determines the protein, and the protein affects the body."},
            {"prompt": "<p>Use the table above to write 2 sentences connecting the DNA change in Person 2 to their symptoms.</p>",
             "points": 2,
             "criteria": [(2, "Connects DNA change to protein change to symptoms, using data."),
                          (1, "Gives part of the chain only."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Person 2 has a changed base in the gene, so the protein is built differently and works poorly. Because the protein does not do its job well, the person has symptoms."},
        ],
    },
]
