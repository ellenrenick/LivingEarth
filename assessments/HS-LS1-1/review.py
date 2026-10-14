"""Unit review for HS-LS1-1 (unit 2.1). Done on the review day, built around the CFAs (no practice test).

Boundary: no mRNA/tRNA mechanics, no specific cell types, no protein structure items.
"""

STANDARD = "HS-LS1-1"
UNIT_TITLE = "DNA to Proteins"
GOAL = ("Explain, using evidence, how the base sequence of DNA determines the amino acid sequence of proteins, "
        "and how proteins give different cells their different jobs.")

CODE = ("<table border=\"1\" cellpadding=\"6\"><tr><th>DNA triplet</th><th>Amino acid</th><th>DNA triplet</th><th>Amino acid</th></tr>"
        "<tr><td>ATG</td><td>Met</td><td>GAG</td><td>Glu</td></tr><tr><td>CTG</td><td>Leu</td><td>GTG</td><td>Val</td></tr>"
        "<tr><td>TTT</td><td>Phe</td><td>GAC</td><td>Asp</td></tr><tr><td>CCT</td><td>Pro</td><td>GGC</td><td>Gly</td></tr></table>")

KEY_IDEAS = [
    "<strong>DNA is a double helix made of nucleotides.</strong> Each nucleotide has a sugar, a phosphate, and a base (A, T, C, or G).",
    "<strong>A gene is a section of DNA</strong> with the instructions for one protein.",
    "<strong>Copy, then read.</strong> A gene's message is copied, and the copy is read to link amino acids in order into a chain. The DNA itself stays protected.",
    "<strong>The order of bases sets the order of amino acids,</strong> and the amino acid chain makes the protein.",
    "<strong>One base change can change one amino acid,</strong> which can change how a protein works. Not every change matters.",
    "<strong>All your cells have the same DNA,</strong> but each kind of cell uses different genes, makes different proteins, and so has a different job.",
]

VOCAB = {
    "bank": ["DNA", "nucleotide", "gene", "base sequence", "amino acid", "protein"],
    "blanks": [
        ("The molecule that stores the instructions for building proteins is ____________.", "DNA"),
        ("One building block of DNA, with a sugar, a phosphate, and a base, is a ____________.", "nucleotide"),
        ("A section of DNA with the instructions for one protein is a ____________.", "gene"),
        ("The order of A, T, C, and G along a strand of DNA is its ____________.", "base sequence"),
        ("A chain of ____________ is folded to make a protein.", "amino acids"),
        ("A ____________ does jobs for the cell, such as moving materials or building structures.", "protein"),
    ],
}

SECTIONS = [
    {"id": "A", "title": "DNA and genes", "lts": ["LS1-1.1", "LS1-1.2"],
     "intro": "<p>Describe DNA and what it does.</p>",
     "items": [
         ("What shape is DNA, and what are the three parts of a nucleotide?", "A double helix (twisted ladder). A nucleotide has a sugar, a phosphate, and a base."),
         ("Name the four bases.", "A, T, C, and G."),
         ("What do the instructions in a gene tell the cell to build?", "A protein."),
         ("True or false: Proteins hold the instructions and DNA does the jobs. Explain.", "False. DNA holds the instructions, and proteins do the jobs for the cell."),
     ]},
    {"id": "B", "title": "From gene to amino acid chain", "lts": ["LS1-1.3"],
     "intro": "<p>Use the code table.</p>" + CODE,
     "items": [
         ("Think of a recipe book (DNA) that stays on a shelf. A cook copies one recipe and follows the copy. Match each part to the cell: recipe book, one recipe, the copy, the dish.", "DNA; a gene; the copy of the gene's message; the protein."),
         ("Put in order: (a) amino acids are linked in order, (b) the copy is read, (c) the gene's message is copied.", "(c), then (b), then (a)."),
         ("A gene reads ATG CTG TTT CCT. What amino acid chain is built?", "Met, Leu, Phe, Pro."),
         ("A gene reads ATG GGC GAC. Write the chain.", "Met, Gly, Asp."),
     ]},
    {"id": "C", "title": "What a base change can do", "lts": ["LS1-1.4"],
     "intro": "<p>Use the code table.</p>" + CODE,
     "items": [
         ("A gene reads ATG GAG CTG. A base changes so it reads ATG GTG CTG. Write both amino acid chains.", "Original: Met, Glu, Leu. Changed: Met, Val, Leu."),
         ("How many amino acids changed? Could this change how the protein works? Explain.", "One amino acid changed (Glu to Val). A chain with a different amino acid can make a protein that works differently."),
         ("A student says, &ldquo;Any change in a gene always stops the protein from working.&rdquo; Use this evidence to respond: change A leaves the chain the same, change B alters one amino acid and the protein still works, change C alters one amino acid and the protein does not work.", "Not every change matters. A and B did not stop the protein. What matters is whether the amino acid chain changes and how."),
     ]},
    {"id": "D", "title": "Same DNA, different jobs", "lts": ["LS1-1.5"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Cell type</th><th>Genes in the cell</th><th>Proteins made</th><th>Job</th></tr><tr><td>P</td><td>1, 2, 3, 4</td><td>1 and 2</td><td>Carries signals</td></tr><tr><td>Q</td><td>1, 2, 3, 4</td><td>3 and 4</td><td>Squeezes to move the body</td></tr></table>",
     "items": [
         ("Do the two cell types have the same DNA? How do you know?", "Yes. Both have genes 1 to 4."),
         ("Why do they make different proteins?", "Each cell type uses a different set of genes."),
         ("Explain how DNA, through proteins, gives cell types P and Q different jobs.", "Cell P uses genes 1 and 2 to build proteins 1 and 2 that carry signals; Cell Q uses genes 3 and 4 to build proteins 3 and 4 that squeeze. The proteins carry out each cell's job."),
         ("Predict: gene 3 has a change that stops Protein 3 from working. What happens to Cell Q's job?", "Cell Q cannot do its job well, because it depends on Protein 3."),
     ]},
    {"id": "E", "title": "A case study", "lts": ["LS1-1.6"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Person</th><th>Gene</th><th>Protein</th><th>Symptoms</th></tr><tr><td>1</td><td>Normal</td><td>Works</td><td>None</td></tr><tr><td>2</td><td>One base changed</td><td>One amino acid different; works poorly</td><td>Yes</td></tr></table>",
     "items": [
         ("Put these in order: (a) symptoms, (b) a base in the gene changes, (c) the protein works poorly, (d) a different amino acid in the chain.", "(b), (d), (c), (a)."),
         ("Use the table to explain how Person 2's DNA change led to symptoms.", "A single base change altered one amino acid, so the protein works poorly; because the protein does not do its job, the person has symptoms."),
     ]},
]

WRITE = {
    "prompt": ("<p>A gene helps cells take in iron. Doctors compare two people.</p>" + CODE.replace("<table", "<table", 1) +
               "<table border=\"1\" cellpadding=\"6\"><tr><th></th><th>Person 1</th><th>Person 2</th></tr>"
               "<tr><td>Gene base sequence</td><td>ATG GAG GAC CTG</td><td>ATG GTG GAC CTG</td></tr>"
               "<tr><td>Protein works?</td><td>Yes</td><td>No (cells take in too little iron)</td></tr></table>"
               "<p>Write an explanation: <strong>Claim</strong> (how the DNA difference caused the problem), <strong>Evidence</strong> (at least two data points), and <strong>Reasoning</strong> (copy then read, the amino acid chain, and how a different protein changes what a cell can do).</p>"),
    "checklist": ["States that one base change led to a different amino acid and a protein that does not work",
                  "Uses at least two pieces of data (GAG versus GTG; Glu versus Val; works versus does not)",
                  "Describes copy-then-read from the gene to an amino acid chain",
                  "Links the base sequence to the amino acid order",
                  "Explains that a protein that does not work means the cell cannot do its job"],
    "exemplar": ("One base in the gene changed, which changed one amino acid, so the protein no longer works. Person 1's gene reads ATG GAG GAC CTG and Person 2's reads ATG GTG GAC CTG, so GAG (Glu) is GTG (Val) in Person 2, and the protein does not work. "
                 "A cell copies the message of a gene and reads the copy to link amino acids in order, so the base sequence sets the amino acid order. A chain with a different amino acid can make a protein that works differently. "
                 "Since this protein cannot help the cell take in iron, the cell cannot do its job."),
}
