"""Student-facing slide content for the 8-day unit 2.1 (Siamese cats). Rendered by make_slides.py.

Each deck is a list of slides: {"title", "bullets" (optional), "table" (optional {"header", "rows"}), "note" (optional small line)}.
"""

TEMP_TABLE = {"header": ["Body part", "Skin temp (°C)", "Fur color"],
              "rows": [["Back", "36", "Cream"], ["Belly", "36", "Cream"], ["Upper leg", "34", "Cream"], ["Ear", "28", "Dark brown"],
                       ["Nose / face", "30", "Dark brown"], ["Paw", "28", "Dark brown"], ["Tail tip", "27", "Dark brown"]]}
LITTER_TABLE = {"header": ["Litter", "Mother", "Father", "Siamese-pattern kittens", "Solid kittens"],
                "rows": [["1", "Siamese", "Siamese", "5", "0"], ["2", "Siamese", "Siamese", "4", "0"], ["3", "Siamese", "Solid", "0", "6"],
                         ["4", "Solid", "Solid", "1", "4"], ["5", "Solid", "Solid", "2", "3"], ["6", "Siamese", "Solid", "3", "2"], ["7", "Solid", "Solid", "1", "5"]]}
CODE_TABLE = {"header": ["DNA triplet", "Amino acid", "DNA triplet", "Amino acid"],
              "rows": [["ATG", "Met", "AGA", "Arg"], ["GGA", "Gly", "CTG", "Leu"], ["TTT", "Phe", "GAC", "Asp"]]}

DECKS = {
    "Day 1: Launch with the Siamese cat": [
        {"title": "Day 1: Why are a Siamese cat's ears, paws, and tail dark?", "bullets": ["Unit 2.1: DNA to Proteins", "Today's target: DNA holds the instructions for building proteins (LS1-1.2)"], "note": "Illustrations in this unit are simplified."},
        {"title": "Notice and wonder", "bullets": ["Look at the photos of an adult Siamese cat and a newborn Siamese kitten.", "Write 2 things you notice.", "Write 2 things you wonder.", "Where is the cat dark? Where is it cream? What about the kitten?"]},
        {"title": "Data 1: Temperature and fur color", "table": TEMP_TABLE, "note": "Simplified class data. What pattern do you see? (Question 1)"},
        {"title": "Think about it", "bullets": ["A kitten is born almost white. The dark parts show up in the first weeks.", "Use the temperature data to suggest why (Question 2).", "A newborn is warm all over before birth."]},
        {"title": "Data 2: Litters of kittens", "table": LITTER_TABLE, "note": "Simplified class data. Describe each type of pair (Questions 3 and 4)."},
        {"title": "Key ideas", "bullets": ["DNA in every cell stores instructions.", "A gene is a section of DNA with the instructions for one protein.", "Proteins do jobs for the cell.", "A kitten gets one set of chromosomes (long DNA molecules with many genes) from each parent."]},
        {"title": "Big question for the unit", "bullets": ["How can a difference in DNA change which parts of a cat are dark?", "Draw your initial model (Question 8): what is inside the cat's cells that leads to dark ears, paws, and tail?", "We will revise it on Day 7."]},
        {"title": "Exit ticket: CFA LS1-1.2", "bullets": ["6 minutes, on your own.", "Then finish the Day 1 assignment in Canvas."]},
    ],
    "Day 2: What is DNA made of?": [
        {"title": "Day 2: What is DNA made of?", "bullets": ["Today's target: describe DNA as a double helix built from nucleotides (LS1-1.1)"]},
        {"title": "Warm-up", "bullets": ["Yesterday: a gene in the cat's cells holds instructions for a protein.", "Sketch what you think DNA looks like (1 minute).", "Share with a partner."]},
        {"title": "DNA is a double helix", "bullets": ["Two strands twisted like a ladder.", "Built from nucleotides.", "Each nucleotide: a sugar, a phosphate, and a base.", "Sugars and phosphates make the sides (the backbone). Bases make the rungs."]},
        {"title": "Base pairing", "bullets": ["Four bases: A, T, C, G.", "A pairs with T.", "C pairs with G.", "The order of the bases is the message."], "table": {"header": ["Strand 1", "A", "T", "G", "C"], "rows": [["Partner", "T", "A", "C", "G"]]}},
        {"title": "Your turn", "bullets": ["Part A: draw and label one nucleotide (pentagon, circle, rectangle).", "Part B: write the partner strand for three sequences.", "Part C: answer the questions."]},
        {"title": "One letter apart", "bullets": ["Solid cat:   A T G G G A C T G T T T", "Siamese cat: A T G A G A C T G T T T", "Illustration only (made-up letters). Where do they differ?", "Could one letter change which parts of a cat are dark? We find out on Days 3 and 4."]},
        {"title": "Exit ticket: CFA LS1-1.1", "bullets": ["6 minutes, on your own.", "Then finish the Day 2 assignment in Canvas."]},
    ],
    "Day 3: LAB, build, copy, and read a gene (gummy DNA)": [
        {"title": "Day 3 LAB: Build, copy, and read a gene", "bullets": ["Today's target: a gene's message is copied, and the copy is read to build a chain of amino acids (LS1-1.3)"]},
        {"title": "The idea: copy, then read", "bullets": ["DNA stays safe in the nucleus.", "The cell COPIES the gene's message from the template strand.", "The COPY is read three letters at a time.", "Each triplet gives one amino acid. The amino acids make a chain."]},
        {"title": "Base key and code table", "bullets": ["Red = A   Yellow = T   Green = C   Orange = G"], "table": CODE_TABLE},
        {"title": "Safety", "bullets": ["Do not eat lab materials until your teacher says you may.", "Toothpicks are sharp.", "Tell your teacher about any food allergy.", "Clean up your table and wash your hands."]},
        {"title": "Part A and B (14 min)", "bullets": ["A: build the template strand  T A C  C C T  G A C  A A A", "B: build the partner strand (A with T, C with G) and make the ladder.", "Have your teacher check the ladder."]},
        {"title": "Part C (10 min)", "bullets": ["Pull the strands apart. Keep the template.", "Build the COPY by pairing with the template.", "Read the copy three letters at a time with the code table.", "Write the amino acid chain."]},
        {"title": "Part D (7 min): change one letter", "bullets": ["Change the 4th base of the template: it becomes T A C  T C T  G A C  A A A", "Build the new copy and read it.", "How many amino acids changed? Which one?", "Predict: could this protein work differently?"]},
        {"title": "Wrap up", "bullets": ["Connect questions: what did one letter do? How is the model different from real DNA?", "Clean up.", "Exit ticket: CFA LS1-1.3 (6 minutes)."]},
    ],
    "Day 4: What can one letter do?": [
        {"title": "Day 4: What can one letter do?", "bullets": ["Today's target: changing one DNA base can change a protein and what it does (LS1-1.4)"]},
        {"title": "Warm-up: recap Part D", "bullets": ["When one letter changed in the lab, how many amino acids changed?", "Base order sets amino acid order."]},
        {"title": "Three things a one-letter change can do", "bullets": ["1. Change one amino acid in the chain (the protein may work differently).", "2. Change whether or when a protein is made (a change in a switch next to a gene).", "3. Change nothing noticeable (same amino acid, or no gene or switch involved).", "Not every change matters."]},
        {"title": "Code table for the card sort", "table": {"header": ["DNA triplet", "Amino acid", "DNA triplet", "Amino acid"], "rows": [["GGA", "Gly", "AGA", "Arg"], ["GAG", "Glu", "GTG", "Val"], ["GAA", "Glu", "CTG", "Leu"], ["CCG", "Pro", "", ""]]}},
        {"title": "Card sort (15 min)", "bullets": ["Sort cards A to F into three categories and write your reason on each.", "A: Siamese cat, GGA becomes AGA     B: GAG becomes GAA", "C: CTG becomes CCG     D: change in DNA with no gene or switch", "E: change that turns a gene off for good     F: human gene, GAG becomes GTG"]},
        {"title": "The Siamese cat", "bullets": ["Card A is the real change: one amino acid in the pigment-making protein is different.", "The protein still forms, but it stops working at warm body temperatures.", "It works only in the cooler ears, nose, paws, and tail tip.", "How does this explain the dark points and the white newborn?"]},
        {"title": "Exit ticket: CFA LS1-1.4", "bullets": ["6 minutes, on your own.", "Then finish the Day 4 assignment in Canvas."]},
    ],
    "Day 5: Same DNA, different jobs": [
        {"title": "Day 5: Same DNA, different jobs", "bullets": ["Today's target: DNA, through proteins, gives different cells their different jobs (LS1-1.5)"]},
        {"title": "Warm-up", "bullets": ["Your skin cells and your nerve cells have the same DNA.", "Why are they so different?"]},
        {"title": "Key ideas", "bullets": ["Every cell has the same DNA, including all the genes.", "Each kind of cell uses a different set of genes.", "The proteins a cell makes decide its job.", "In a cat, only pigment-making cells use the gene for the pigment-making protein."]},
        {"title": "Part A: two kinds of cells", "table": {"header": ["Cell", "Genes in cell", "Proteins made", "Job"], "rows": [["P", "1, 2, 3, 4", "1 and 2", "Carries signals"], ["Q", "1, 2, 3, 4", "3 and 4", "Squeezes to move the body"]]}, "note": "Same DNA? Why different jobs?"},
        {"title": "Part B: cells in a Siamese cat's ear", "bullets": ["Which cells have the gene for the pigment-making protein?", "Which cells make the protein?", "Fill in the table: pigment-making cell, skin cell, nerve cell."]},
        {"title": "Part C: where does the changed protein work?", "bullets": ["One amino acid is different. The protein works only in skin cooler than about 33 °C (a simplified number).", "Use the temperatures to fill in each body part: protein works? Fur dark or cream?"], "table": {"header": ["Body part", "Skin temp (°C)"], "rows": [["Ear", "28"], ["Nose", "30"], ["Paw", "28"], ["Tail tip", "27"], ["Upper leg", "34"], ["Back", "36"], ["Belly", "36"]]}},
        {"title": "Explain it", "bullets": ["Use the words DNA, gene, protein, and job to explain why a Siamese cat has dark points.", "Then: Exit ticket CFA LS1-1.5 (6 minutes)."]},
    ],
    "Day 6: Case data": [
        {"title": "Day 6: Case data", "bullets": ["Today's target: use case data to explain how a DNA change affects the body (LS1-1.6)"]},
        {"title": "Warm-up: the chain for the cat", "bullets": ["One-letter DNA change", "to one different amino acid", "to a protein that works only in cool skin", "to dark points"]},
        {"title": "Case 1: Siamese and solid cats", "table": {"header": ["", "Solid cat", "Siamese cat"], "rows": [["Gene", "Usual sequence", "One letter different"], ["Amino acid chain", "Usual chain", "One amino acid different"], ["Where protein works", "At every temperature", "Only below about 33 °C"], ["Fur color", "Dark all over", "Dark points, cream body"]]}},
        {"title": "Case 2: a human gene", "table": {"header": ["Person", "Gene", "Protein", "Symptoms"], "rows": [["1", "Normal", "Works", "None"], ["2", "One base changed", "One amino acid different; works poorly", "Yes"]]}},
        {"title": "Compare the cases", "bullets": ["How are they alike? How are they different?", "Why does a change in DNA change what a protein can do?", "What do the Day 1 litter data tell you about the changed gene in Case 1?"]},
        {"title": "Write: claim, evidence, reasoning", "bullets": ["Claim: what caused the Siamese cat's dark points?", "Evidence: at least two numbers from the data.", "Reasoning: how does a one-letter DNA change lead to dark color only on the cooler body parts?"]},
        {"title": "Exit ticket: CFA LS1-1.6", "bullets": ["6 minutes, on your own.", "Then finish the Day 6 assignment in Canvas."]},
    ],
    "Day 7: Review and back to the cat": [
        {"title": "Day 7: Review and back to the cat", "bullets": ["Today: fix what you missed, revise your model, and explain the phenomenon."]},
        {"title": "Find your focus (5 min)", "bullets": ["Look at your six CFA scores in Canvas.", "Scored below a 3 on a CFA? Do the matching section of the Review page.", "Everyone does Vocabulary and Write It."]},
        {"title": "Review work time (20 min)", "bullets": ["Open the Review page in Canvas.", "Do Vocabulary, then the sections for the CFAs you need.", "Check your answers on the key your teacher shares."]},
        {"title": "Revise your Day 1 model (8 min)", "bullets": ["Show: DNA with the gene.", "Show: the one-letter change.", "Show: the copy-then-read path and the amino acid chain with one amino acid different.", "Show: the protein working only in cool skin, and the dark points."]},
        {"title": "Write It: two Siamese kittens", "table": {"header": ["", "Raised warm", "Raised cool"], "rows": [["Ear skin temp (°C)", "34", "26"], ["Ear fur color", "Light tan", "Dark brown"], ["Back skin temp (°C)", "36", "35"], ["Back fur color", "Cream", "Cream"]]}, "note": "Why are the cool-room kitten's ears darker?"},
        {"title": "Write It: your explanation", "bullets": ["Claim: why are the cool-room kitten's ears darker?", "Evidence: at least two numbers.", "Reasoning: DNA, gene, protein, and what the amino acid change does.", "Submit in Canvas."]},
    ],
    "Day 8: CSA": [
        {"title": "Day 8: Unit Assessment (CSA)", "bullets": ["HS-LS1-1: DNA to Proteins", "45 minutes"]},
        {"title": "Before you begin", "bullets": ["Work alone. Put everything away except what your teacher allows.", "Read each question carefully. Use the code table when it is given.", "Part 1: matching. Part 2: multiple choice. Part 3: free response.", "Free response: use claim, evidence, and reasoning where asked."]},
        {"title": "Reminders", "bullets": ["Do your best on every question.", "Answer every question; do not leave blanks.", "If you finish early, check your free responses.", "Next class: we will review the free-response examples and revisit the Siamese cat."]},
    ],
}
