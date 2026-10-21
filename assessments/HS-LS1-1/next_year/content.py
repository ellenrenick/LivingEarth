"""Unit 2.1 DNA to Proteins (HS-LS1-1), next-year version: 8 days (department workbook, Units tab), every lesson
modeled on Unit 1.3 Short Lessons A and B (CLAUDE.md: pace and style).

Each lesson day is about 30 minutes of student work including its CFA: short activities (2 to 8 minutes), a 5-minute
mini-lesson, one worked example, a small data table with real numbers, a sentence frame and a scrambled word bank on
every fill-in, one slide per notebook section in notebook order, and the CFA last, from memory. Day 3 (gummy DNA lab)
and Day 8 (CSA) use the full period; Day 7 (review) is the Unit 1.3 Day 9 pattern: a self-check for everyone, the
mystery wrap-up for everyone, then CFA reviews or (no reviews) an enrichment.

Everything here is data. build.py turns it into slides, Canvas pages, CFAs, and the CSA.
"""

import random

UNIT = "Unit 2.1"
UNIT_NAME = "DNA to Proteins"
STANDARD = "HS-LS1-1"
MYSTERY = "The Siamese Cat Mystery"
DRIVING_Q = "Why are a Siamese cat's ears, face, paws, and tail dark, while its body is cream?"
PE = ("Construct an explanation based on evidence for how the structure of DNA determines the structure of proteins, "
      "which carry out the essential functions of life through systems of specialized cells.")

# Workbook (Living Earth Standards and Learning Targets 26-27), Targets tab. (id, short name, DOK, "I can", tier)
TARGETS = [
    ("LS1-1.1", "DNA structure and instructions", 1,
     "I can describe DNA as a double helix built from nucleotides, each with a sugar, a phosphate, and a base, and state "
     "that DNA holds the instructions for building proteins.", "Priority"),
    ("LS1-1.2", "Copy and read a gene", 2,
     "I can describe how a gene's message is copied and read to build a chain of amino acids.", "Priority"),
    ("LS1-1.3", "One base change", 2, "I can explain how changing one DNA base can change a protein and what it does.",
     "Priority"),
    ("LS1-1.4", "Same DNA, different jobs", 3, "I can explain how DNA, through proteins, gives different cells their different jobs.",
     "Priority"),
    ("LS1-1.5", "Case data", 3, "I can use case data, like sickle cell, to explain how a DNA change affects the body.",
     "Priority"),
    ("LS3-1.1", "Chromosomes, DNA, and genes", 1, "I can describe how chromosomes, DNA, and genes are related.", "Supporting"),
    ("LS3-1.2", "Chromosomes from each parent", 2, "I can explain how a child gets half of its chromosomes from each parent.",
     "Supporting"),
    ("LS3-1.3", "Ask questions about traits", 2,
     "I can ask questions that clarify how DNA and chromosomes carry the instructions for traits passed to offspring.",
     "Supporting"),
]
TARGET = {t[0]: t for t in TARGETS}
PRIORITY = [t[0] for t in TARGETS if t[4] == "Priority"]


def scramble(words):
    """Word bank order: never answer order (fixed seed, so reruns match). No word keeps its answer-order spot, and in
    banks of 4 or more no two answer-order neighbours stay side by side."""
    words, original = list(words), list(words)
    rng = random.Random(" ".join(words))

    def ordered(w):
        return any(a == b for a, b in zip(w, original)) or (len(w) > 3 and any(
            original.index(x) + 1 == original.index(y) for x, y in zip(w, w[1:])))
    while len(words) > 1 and ordered(words):
        rng.shuffle(words)
    return words


B = "____"
TEMPS = (["Body part", "Skin temperature (°C)", "Fur color"],
         [["Ear", "28", "Dark brown"], ["Face (mask)", "30", "Dark brown"], ["Paw", "28", "Dark brown"],
          ["Tail tip", "27", "Dark brown"], ["Upper leg", "34", "Cream"], ["Back", "36", "Cream"]])
LITTERS = (["Litter", "Mother", "Father", "Siamese kittens", "Solid kittens"],
           [["1", "Siamese", "Siamese", "5", "0"], ["2", "Siamese", "Siamese", "4", "0"],
            ["3", "Solid", "Solid", "1", "4"], ["4", "Solid", "Solid", "2", "3"]])
BASES = (["Organism", "A (%)", "T (%)", "G (%)", "C (%)"],
         [["Human", "30.9", "29.4", "19.9", "19.8"], ["Wheat", "27.3", "27.1", "22.7", "22.8"],
          ["E. coli (bacteria)", "24.7", "23.6", "26.0", "25.7"]])
CODE = "Code table: GGA = Gly · AGA = Arg · GAG = Glu · GAA = Glu · GTG = Val · CTG = Leu · CCG = Pro"
CARDS = (["Card", "What changed in the DNA", "1, 2, or 3?", "Reason"],
         [["A", "GGA becomes AGA (the Siamese cat)", "", ""],
          ["B", "GAG becomes GAA", "3 (done for you)", "The amino acid stays the same: Glu and Glu."],
          ["C", "CTG becomes CCG", "", ""],
          ["D", "A letter changes where there is no gene and no switch", "", ""],
          ["E", "A letter changes in a gene's switch, so the gene never turns on", "", ""],
          ["F", "GAG becomes GTG (a human gene)", "", ""]])
CELLS = (["Cell", "Genes it has", "Gene it uses", "Protein it makes", "Job"],
         [["Skin cell", "keratin, pigment, myosin", "keratin", "keratin", "makes tough, waterproof skin"],
          ["Pigment cell", "keratin, pigment, myosin", "pigment", "pigment-making protein", "colors fur and skin"],
          ["Muscle cell", "keratin, pigment, myosin", "myosin", "myosin", "squeezes to move the body"]])
MAP = (["Body part", "Skin (°C)", "Cooler than 33 °C?", "Protein works?", "Fur color"],
       [["Ear", "28", "yes", "yes", "dark (done for you)"], ["Face", "30", "", "", ""], ["Paw", "28", "", "", ""],
        ["Tail tip", "27", "", "", ""], ["Upper leg", "34", "", "", ""], ["Back", "36", "", "", ""]])
SICKLE = (["Measurement", "Typical", "Sickle cell disease"],
          [["DNA triplet 6 of the hemoglobin gene", "GAG", "GTG (done for you)"],
           ["Amino acid 6 of 146", "Glu", "Val"],
           ["Red blood cell shape", "Round and bendy", "Sickle-shaped and stiff"],
           ["Red blood cell life span", "About 120 days", "About 10 to 20 days"],
           ["Hemoglobin in the blood (g/dL)", "About 12 to 17", "About 6 to 10"]])
KITTENS = (["", "Kitten raised warm", "Kitten raised cool"],
           [["Ear skin temperature (°C)", "34", "26"], ["Ear fur color", "Light tan", "Dark brown"],
            ["Back skin temperature (°C)", "36", "35"], ["Back fur color", "Cream", "Cream"]])

# A section is one notebook heading = one slide, in notebook order.
#   nb: notebook heading · label/who: slide kicker · minutes · title · body: lines · table: (head, rows)
#   frame: fill-in lines (each blank is ____) · bank: the answers' words (scrambled when shown) · teacher: what you do
# Day kinds: lesson (about 30 min with the CFA), lab and csa (full period), review (Unit 1.3 Day 9 pattern).
DAYS = [
    dict(
        day=1, kind="lesson", title=MYSTERY, targets=["LS3-1.1", "LS3-1.2", "LS3-1.3"], cfa=None,
        focus="Why are a Siamese cat's ears, face, paws, and tail dark?",
        ready="Have ready: your notebook and a pencil",
        can=["use data to find a pattern in a Siamese cat's colors", "describe how chromosomes, DNA, and genes are related",
             "ask a question about how traits pass from parents to kittens"],
        plan=["Notice and wonder", "Skin temperature data", "DNA, genes, and chromosomes", "Litter data", "My first model",
              "Ask a question"],
        sections=[
            dict(nb="Notice and wonder", label="WARM-UP", who="ON YOUR OWN", minutes=3, layout="cats",
                 title="What do you notice? What do you wonder?",
                 body=["An adult Siamese cat is cream with dark ears, face, paws, and tail. A Siamese kitten is born almost all white."],
                 frame=[f"I notice {B}.", f"I wonder {B}."], bank=None,
                 teacher="Show the two cats (photos too, if you have them). Each student writes 1 notice and 1 wonder; take 3 "
                         "aloud. Steer toward: why only the ears, face, paws, and tail?"),
            dict(nb="Skin temperature and fur", label="EVIDENCE 1", who="WITH A PARTNER", minutes=6,
                 title="Skin temperature and fur color", table=TEMPS,
                 body=["Worked example (together): the ear is 28 °C, a cool spot, and its fur is dark."],
                 frame=[f"Dark fur grows where the skin is {B}. Cream fur grows where the skin is {B}.",
                        f"A kitten is born white because inside its mother it was {B} all over."],
                 bank=["cool", "warm"], bank_note="(use a word more than once)",
                 teacher="Do the ear row aloud. Partners finish the frame. Debrief: dark at 27 to 30 °C, cream at 34 to 36 °C. "
                         "A newborn was warm all over inside its mother, so it is born white."),
            dict(nb="Chromosomes, DNA, and genes", label="MINI-LESSON", who="WHOLE CLASS", minutes=5,
                 title="DNA, genes, and chromosomes",
                 body=["Every cell has DNA: the instructions for building proteins.",
                       "A chromosome is one long DNA molecule packed with proteins. A cat has 38 chromosomes in each body cell.",
                       "A gene is a section of DNA that codes for one protein. Proteins do the cell's jobs, like making dark pigment.",
                       "A kitten gets one set of 19 chromosomes from its mother and one set of 19 from its father."],
                 frame=[f"A {B} is one long DNA molecule. A {B} is a section of DNA that codes for one {B}.",
                        f"A kitten gets {B} chromosomes from its mother and {B} from its father."],
                 bank=["chromosome", "gene", "protein", "19"], bank_note="(19 is used twice)", minutes_frame=3,
                 teacher="Board: chromosome → DNA → gene → protein → trait. Students finish the frame (3 min)."),
            dict(nb="Litters of kittens", label="EVIDENCE 2", who="WITH A PARTNER", minutes=5,
                 title="Litters of kittens", table=LITTERS,
                 body=["Worked example: Litter 1 has two Siamese parents, and all 5 kittens are Siamese."],
                 frame=[f"Two solid parents {B} have a Siamese kitten. So each kitten gets genes from {B}."],
                 bank=["can", "both parents"],
                 teacher="Litters 3 and 4 are the surprise: solid parents, Siamese kittens. A kitten gets a set of "
                         "chromosomes from each parent. Don't name recessive yet."),
            dict(nb="My first model", label="MY FIRST MODEL", who="ON YOUR OWN", minutes=4,
                 title="Sketch a cell from the cat's ear",
                 body=["In the box, draw a cell from a Siamese cat's ear.",
                       "Label: chromosome, DNA, gene, protein, dark fur. Use arrows to show what leads to what.",
                       "It's OK to guess. We fix this model on Day 7."],
                 teacher="Do not correct the models; students revise them on Day 7."),
            dict(nb="My question", label="ASK A QUESTION", who="ON YOUR OWN", minutes=2,
                 title="What do you still want to know?",
                 body=["Write 1 question about how DNA and chromosomes pass the Siamese pattern from parents to kittens.",
                       "Example: How can two solid parents have a Siamese kitten?"],
                 frame=[f"How / Why / What {B}?"], bank=None,
                 teacher="Collect 3 questions to answer during the unit (LS3-1.3)."),
        ],
        notebook=dict(
            left=[("h", "Notice and wonder"), ("text", "I notice ____"), ("text", "I wonder ____"),
                  ("h", "Skin temperature and fur"), ("lines", 3), ("h", "Chromosomes, DNA, and genes"), ("lines", 3)],
            right=[("h", "Litters of kittens"), ("lines", 2), ("h", "My first model"),
                   ("box", 1.7, "Sketch a cell from the cat's ear. Label: chromosome, DNA, gene, protein, dark fur."),
                   ("h", "My question"), ("lines", 2)]),
        key=["Skin temperature: cool; warm; warm.", "Chromosomes: chromosome; gene; protein; 19; 19.",
             "Litters: can; both parents.",
             "First model: look for DNA or a gene in a cell, a protein, and dark fur joined by arrows. Do not correct yet.",
             "Question: any How, Why, or What question about DNA, chromosomes, or genes passing the pattern on."],
        notes=["No CFA today: LS3-1 targets are supporting targets, taught but not on the CSA. CFA LS1-1.1 is on Day 2.",
               "The Siamese pattern is recessive: a kitten needs a changed copy of the gene from both parents. Don't name "
               "recessive or dominant unless students ask.",
               "The temperatures and litters are a simplified class data set modeled on real patterns."],
    ),
    dict(
        day=2, kind="lesson", title="DNA: The Twisted Ladder", targets=["LS1-1.1"], cfa="LS1-1.1",
        focus="What is DNA made of, and where is its message?",
        ready="Have ready: your notebook, a pencil, and a Chromebook",
        can=["describe DNA as a double helix made of nucleotides", "use real data to show that A pairs with T and C with G",
             "explain that the order of the bases is the message"],
        plan=["Warm-up", "Mini-lesson: the double helix", "Real base counts", "Partner strands", "The message", "CFA LS1-1.1"],
        sections=[
            dict(nb="Warm-up", label="WARM-UP", who="ON YOUR OWN", minutes=3, layout="warmup",
                 title="What does DNA look like?",
                 body=["Sketch what you think DNA looks like."],
                 frame=[f"A gene is a section of {B} that codes for one {B}. (Day 1)"], bank=["DNA", "protein"],
                 teacher="Take 2 sketches. Most will draw a twisted ladder; ask what the rungs are made of."),
            dict(nb="One nucleotide", label="MINI-LESSON", who="DRAW WITH ME", minutes=5, title="DNA is a double helix",
                 body=["DNA is a double helix: two strands twisted like a ladder.",
                       "It is built from nucleotides. Each nucleotide has a sugar, a phosphate, and a base.",
                       "Sugars and phosphates make the sides. Pairs of bases make the rungs.",
                       "Four bases: A, T, C, G. A pairs with T. C pairs with G.",
                       "The order of the bases is the message: the instructions for building a protein.",
                       "Draw with me: a pentagon (sugar), a circle (phosphate), a rectangle (base). Label each part."],
                 frame=[f"A nucleotide has a {B}, a {B}, and a {B}."], bank=["sugar", "phosphate", "base"],
                 teacher="Draw on the board while students draw one nucleotide in the box. Then two nucleotides paired."),
            dict(nb="Real base counts", label="EVIDENCE", who="WITH A PARTNER", minutes=5,
                 title="Real base counts (Chargaff, 1950s)", table=BASES,
                 body=["Percent of each base in the DNA. Worked example: in humans, A (30.9%) and T (29.4%) are almost equal."],
                 frame=[f"In every organism, A is about equal to {B}, and G is about equal to {B}.",
                        f"This is evidence that the bases come in {B}."],
                 bank=["T", "C", "pairs"],
                 teacher="Erwin Chargaff measured these in the late 1940s and 1950s. The near-equal pairs were a clue for "
                         "Watson, Crick, and Franklin's double helix. Numbers are not exactly equal because of measuring error."),
            dict(nb="Partner strands", label="PARTNER STRANDS", who="WITH A PARTNER", minutes=6,
                 title="Write the matching strand",
                 body=["Rule: A ↔ T and C ↔ G.", "Worked example (together): A T G → T A C"],
                 frame=[f"1. A T G C C T → {B}", f"2. T T T G A C → {B}", f"3. G G A C T G → {B}"], bank=None,
                 teacher="Do the example aloud. Partners write and check each other."),
            dict(nb="The message", label="THE MESSAGE", who="ON YOUR OWN", minutes=3, title="One letter different",
                 body=["Solid cat:     A T G G G A C T G", "Siamese cat:  A T G A G A C T G",
                       "(Made-up letters that show the idea.) Circle the letter that is different."],
                 frame=[f"The {B} of the bases is the message. One different letter could change the {B} the cell builds."],
                 bank=["order", "protein"],
                 teacher="Ask: could one letter change which parts of a cat are dark? We find out on Days 3 and 4."),
        ],
        notebook=dict(
            left=[("h", "Warm-up"), ("box", 0.85, "Sketch: what DNA looks like"), ("text", "A gene is a section of ____ that codes for one ____."),
                  ("h", "One nucleotide"), ("box", 0.9, "Draw and label: sugar, phosphate, base"), ("lines", 1)],
            right=[("h", "Real base counts"), ("lines", 2), ("h", "Partner strands"), ("text", "Example: A T G → T A C"),
                   ("lines", 3), ("h", "The message"), ("lines", 2)]),
        key=["Warm-up: DNA; protein.", "One nucleotide: sugar, phosphate, base (any order), drawn as a pentagon, circle, rectangle.",
             "Base counts: T; C; pairs.", "Partner strands: (1) T A C G G A; (2) A A A C T G; (3) C C T G A C.",
             "The message: the 4th letter (G in the solid cat, A in the Siamese cat); order; protein."],
        notes=["Chargaff data: Wikipedia, Chargaff's rules (human thymus, wheat germ, E. coli)."],
    ),
    dict(
        day=3, kind="lab", title="Gummy DNA Lab: Build, Copy, and Read a Gene", targets=["LS1-1.2"], cfa="LS1-1.2",
        focus="How does a cell's copy of a gene become a chain of amino acids?",
        note="Unchanged from 2026-27 (lab sheet, deck, and teacher key copied as they are); the CFA is the new 5-question CFA."),
    dict(
        day=4, kind="lesson", title="One Letter Can Matter", targets=["LS1-1.3"], cfa="LS1-1.3",
        focus="Does every change in DNA change the protein?",
        ready="Have ready: your notebook, a pencil, and a Chromebook",
        can=["sort one-letter DNA changes by what they do", "use a code table to find a changed amino acid",
             "explain the Siamese cat's one-letter change"],
        plan=["Warm-up: from the lab", "Three things one letter can do", "Card sort", "The Siamese cat", "Claim check",
              "CFA LS1-1.3"],
        sections=[
            dict(nb="Warm-up", label="WARM-UP", who="FROM THE LAB", minutes=3, layout="warmup",
                 title="What did our one-letter change do?",
                 body=["In the gummy lab, one changed letter turned GGA into AGA.", CODE],
                 frame=[f"GGA codes for {B}. AGA codes for {B}. So one {B} in the chain changed."],
                 bank=["Gly", "Arg", "amino acid"], teacher="Recap the lab: base order sets amino acid order."),
            dict(nb="Three things one letter can do", label="MINI-LESSON", who="WHOLE CLASS", minutes=5,
                 title="Three things one letter can do",
                 body=["DNA is read 3 bases at a time. 64 triplets code for only 20 amino acids, so some triplets mean the same one.",
                       "1. Change one amino acid: the protein may work differently.",
                       "2. Change the switch next to a gene: the protein is not made.",
                       "3. Change nothing: the same amino acid, or no gene there."],
                 frame=[f"A one-letter change can change one {B}, turn a gene {B}, or change {B}."],
                 bank=["amino acid", "off", "nothing"],
                 teacher="Model card B with the code table: GAG and GAA both make Glu, so it is a 3."),
            dict(nb="Card sort", label="CARD SORT", who="WITH A PARTNER", minutes=8, title="Sort each change: 1, 2, or 3",
                 table=CARDS, body=[CODE],
                 frame=["Write 1, 2, or 3 and a reason for cards A, C, D, E, and F."],
                 bank=["The amino acid changes from ___ to ___.", "The protein is not made.", "No gene is involved.",
                       "The amino acid stays the same."], bank_label="Reason bank",
                 teacher="Circulate. Check E (category 2) and D (category 3), the two that use no code table."),
            dict(nb="The Siamese cat", label="THE SIAMESE CAT", who="IN YOUR NOTEBOOK", minutes=4,
                 title="Card A is the real Siamese change",
                 body=["In Siamese cats, one letter in the gene for a pigment-making protein (tyrosinase) is different. "
                       "It swaps Gly for Arg.",
                       "The changed protein stops working in warm skin. It works only in skin cooler than about 33 °C."],
                 frame=[f"Gly changes to {B}. The protein works only where the skin is {B}, so the fur is dark on the {B}."],
                 bank=["Arg", "cool", "ears, face, paws, and tail"],
                 teacher="Reveal that card A is the real change (Lyons et al., 2005). Keep it at: a different amino acid "
                         "changes how the protein works."),
            dict(nb="Claim check", label="CLAIM CHECK", who="ON YOUR OWN", minutes=3, title="Does every DNA change matter?",
                 body=["A student says: “Every change in DNA changes how a cell works.”"],
                 frame=[f"I {B} with the student. Card {B} shows this, because {B}."],
                 bank=["disagree", "B", "the amino acid stays the same"],
                 teacher="Card D (no gene is involved) is also a correct answer."),
        ],
        notebook=dict(
            left=[("h", "Warm-up"), ("lines", 2), ("h", "Three things one letter can do"), ("lines", 3)],
            right=[("h", "Card sort"),
                   ("table", ["Card", "1, 2, or 3?", "Reason"],
                    [["A", "", ""], ["B", "3", "Same amino acid (Glu, Glu)"], ["C", "", ""], ["D", "", ""], ["E", "", ""],
                     ["F", "", ""]], [0.6, 1.0, 2.8], 9, None),
                   ("h", "The Siamese cat"), ("lines", 2), ("h", "Claim check"), ("lines", 2)]),
        key=["Warm-up: Gly; Arg; amino acid.", "Three things: amino acid; off; nothing.",
             "Card A (GGA → AGA): 1, Gly to Arg. Card B: 3 (done). Card C (CTG → CCG): 1, Leu to Pro. Card D: 3, no gene is "
             "involved. Card E: 2, the protein is not made. Card F (GAG → GTG): 1, Glu to Val (the sickle cell change).",
             "The Siamese cat: Arg; cool; ears, face, paws, and tail.",
             "Claim check: disagree; B (or D); the amino acid stays the same (or no gene is involved)."],
        notes=["The Siamese change is reported as glycine to arginine in tyrosinase (TYR); sources number the residue "
               "differently. The 33 °C line is a simplified class number."],
    ),
    dict(
        day=5, kind="lesson", title="Same DNA, Different Jobs", targets=["LS1-1.4"], cfa="LS1-1.4",
        focus="If every cell has the same DNA, why do cells do different jobs?",
        ready="Have ready: your notebook, a pencil, and a Chromebook",
        can=["explain that cells use different genes from the same DNA", "connect the genes a cell uses to its proteins and its job",
             "use temperature data to explain where a Siamese cat is dark"],
        plan=["Warm-up", "Cells use different genes", "Three cells, one set of genes", "Where does the protein work?",
              "Explain it", "CFA LS1-1.4"],
        sections=[
            dict(nb="Warm-up", label="WARM-UP", who="ON YOUR OWN", minutes=3, layout="warmup",
                 title="Same DNA, different cells",
                 body=["Your skin cells and your muscle cells have the same DNA. So why do they look and act so different?"],
                 frame=[f"I think they are different because {B}."], bank=None,
                 teacher="Take 3 ideas. Keep the ones about different instructions being used."),
            dict(nb="Key idea", label="MINI-LESSON", who="WHOLE CLASS", minutes=5, title="Cells use different genes",
                 body=["Almost every cell in your body has the same DNA, with about 20,000 genes.",
                       "Each kind of cell (you have about 200 kinds) uses only some of its genes.",
                       "The genes a cell uses decide which proteins it makes. The proteins decide its job.",
                       "Cells that share a job form tissues, and tissues work together in body systems."],
                 frame=[f"Every cell has the same {B}, but each kind of cell uses different {B}."],
                 bank=["DNA", "genes"], teacher="Draw: same DNA → different genes used → different proteins → different jobs."),
            dict(nb="Three cells, one set of genes", label="EVIDENCE", who="WITH A PARTNER", minutes=5,
                 title="Three cells, one set of genes", table=CELLS,
                 body=["Worked example: the skin cell has all three genes but uses the keratin gene, so it makes keratin."],
                 frame=[f"All three cells have the {B} genes. Each cell uses a different {B}, so it makes a different {B} "
                        f"and does a different {B}."],
                 bank=["same", "gene", "protein", "job"],
                 teacher="Keratin is the main protein of skin, hair, and nails; myosin helps muscle cells squeeze."),
            dict(nb="Where does the protein work?", label="DATA", who="WITH A PARTNER", minutes=6,
                 title="Where does the changed protein work?", table=MAP,
                 body=["The Siamese cat's changed protein works only in skin cooler than about 33 °C. The ear is done for you."],
                 frame=["Fill in each row of the table in your notebook."], bank=None,
                 teacher="Students copy the table (ear row given) and fill in the rest."),
            dict(nb="Explain it", label="EXPLAIN IT", who="ON YOUR OWN", minutes=4, title="Why only the points are dark",
                 body=["Use the word bank to finish the frame."],
                 frame=[f"Every cell in a Siamese cat has the same {B}. Only pigment cells use the {B} for the pigment-making {B}.",
                        f"The changed protein works only where the skin is {B}, so the ears, face, paws, and tail are {B}."],
                 bank=["DNA", "gene", "protein", "cool", "dark"], teacher="Read two answers aloud."),
        ],
        notebook=dict(
            left=[("h", "Warm-up"), ("lines", 2), ("h", "Key idea"), ("lines", 2), ("h", "Three cells, one set of genes"),
                  ("lines", 3)],
            right=[("h", "Where does the protein work?"),
                   ("table", ["Body part", "°C", "Below 33?", "Works?", "Fur"],
                    [["Ear", "28", "yes", "yes", "dark"], ["Face", "30", "", "", ""], ["Paw", "28", "", "", ""],
                     ["Tail tip", "27", "", "", ""], ["Upper leg", "34", "", "", ""], ["Back", "36", "", "", ""]],
                    [1.0, 0.55, 0.95, 0.85, 1.05], 9, None),
                   ("h", "Explain it"), ("lines", 3)]),
        key=["Warm-up: any idea about cells using different instructions.", "Key idea: DNA; genes.",
             "Three cells: same; gene; protein; job.",
             "Where it works: face, paw, tail tip: yes, yes, dark. Upper leg and back: no, no, cream.",
             "Explain it: DNA; gene; protein; cool; dark."],
        notes=["About 20,000 protein-coding genes and about 200 cell types are the usual textbook figures for humans.",
               "Boundary: do not test the names of cell types, tissues, or body systems; they are examples here."],
    ),
    dict(
        day=6, kind="lesson", title="Sickle Cell: From Gene to Body", targets=["LS1-1.5"], cfa="LS1-1.5",
        focus="How can one DNA letter change a person's whole body?",
        ready="Have ready: your notebook, a pencil, and a Chromebook",
        can=["trace a DNA change to a protein to the body", "use two numbers from case data as evidence",
             "compare the Siamese cat and sickle cell"],
        plan=["Warm-up", "Hemoglobin and sickle cell", "Case data", "Compare the cat and the person", "CER", "CFA LS1-1.5"],
        sections=[
            dict(nb="Warm-up", label="WARM-UP", who="ON YOUR OWN", minutes=3, layout="warmup",
                 title="The Siamese cat chain",
                 body=["Finish the chain from Days 4 and 5."],
                 frame=[f"One letter in the {B} changes → one {B} in the protein is different → the protein works only in "
                        f"{B} skin → dark fur on the points."],
                 bank=["gene", "amino acid", "cool"], teacher="Say the chain together."),
            dict(nb="Key idea", label="MINI-LESSON", who="WHOLE CLASS", minutes=5, title="Hemoglobin and sickle cell",
                 body=["Red blood cells are packed with hemoglobin, a protein that carries oxygen.",
                       "In sickle cell disease, one base in the hemoglobin gene changes: GAG becomes GTG.",
                       "That swaps one amino acid: Glu becomes Val (number 6 of 146).",
                       "When oxygen is low, the changed hemoglobin sticks together, and red blood cells bend into stiff sickles.",
                       "Sickle cells clog small blood vessels and break down early."],
                 frame=[f"Sickle cell starts with one changed {B} in the {B} gene."], bank=["base", "hemoglobin"],
                 teacher="Sickle cell disease affects about 100,000 people in the U.S. (CDC). Keep the protein at the level of "
                         "'works differently'; its structure is outside the boundary."),
            dict(nb="Case data: the chain", label="CASE DATA", who="WITH A PARTNER", minutes=7,
                 title="Typical vs. sickle cell disease", table=SICKLE,
                 body=["The DNA row is done for you: GAG becomes GTG."],
                 frame=[f"One base in the {B} changes → one {B} is different → the {B} sticks together and cells sickle → "
                        f"cells last {B} days instead of 120 → less {B} reaches the body."],
                 bank=["gene", "amino acid", "hemoglobin", "10 to 20", "oxygen"],
                 teacher="Partners fill in the chain. Check the numbers: 120 vs. 10 to 20 days; 12 to 17 vs. 6 to 10 g/dL."),
            dict(nb="Compare", label="COMPARE", who="ON YOUR OWN", minutes=3, title="The cat and the person",
                 body=["Siamese cat: one letter → Gly becomes Arg → protein works only in cool skin → dark points.",
                       "Sickle cell: one letter → Glu becomes Val → hemoglobin sticks together → sickled cells, tiredness, pain."],
                 frame=[f"In both cases, one letter in the DNA changes, one {B} changes, and the protein works {B}."],
                 bank=["amino acid", "differently"], teacher="One sentence each."),
            dict(nb="CER", label="CER", who="ON YOUR OWN", minutes=6, title="Why do people with sickle cell feel tired?",
                 body=["Write a claim, two pairs of numbers as evidence, and reasoning from gene to body."],
                 frame=[f"Claim: People with sickle cell disease feel tired because {B}.",
                        "Evidence: Their red blood cells last ___ days (vs. ___), and their hemoglobin is ___ g/dL (vs. ___).",
                        f"Reasoning: One base change in the hemoglobin {B} swaps one {B}. The changed {B} sticks together, so "
                        f"red blood cells sickle and break down early. Fewer red blood cells carry less {B}."],
                 bank=["their red blood cells carry less oxygen", "gene", "amino acid", "hemoglobin", "oxygen"],
                 teacher="Share two samples. Look for both pairs of numbers."),
        ],
        notebook=dict(
            left=[("h", "Warm-up"), ("lines", 2), ("h", "Key idea"), ("lines", 1), ("h", "Case data: the chain"), ("lines", 4)],
            right=[("h", "Compare"), ("lines", 2), ("h", "CER"),
                   ("table", ["Part", "My answer"], [["Claim", ""], ["Evidence (4 numbers)", ""], ["Reasoning", ""]],
                    [1.3, 3.15], 9, 0.55)]),
        key=["Warm-up: gene; amino acid; cool.", "Key idea: base; hemoglobin.",
             "Case data chain: gene; amino acid; hemoglobin; 10 to 20; oxygen.", "Compare: amino acid; differently.",
             "CER: claim: their red blood cells carry less oxygen (fewer red blood cells, because they sickle and break down). "
             "Evidence: about 10 to 20 days vs. about 120 days; about 6 to 10 g/dL vs. about 12 to 17 g/dL. Reasoning: gene; "
             "amino acid; hemoglobin; oxygen."],
        notes=["Hemoglobin ranges are typical adult ranges (about 12 to 17 g/dL); people with sickle cell anemia usually "
               "run about 6 to 10 g/dL. Red blood cell life span: about 120 days vs. 10 to 20 days (NIH NHLBI)."],
    ),
    dict(
        day=7, kind="review", title="Mystery Solved: The Siamese Cat", targets=PRIORITY, cfa=None,
        focus="Can I explain the Siamese cat from DNA to fur?",
        ready="Have ready: your notebook (with your Day 1 model), a pencil, and a Chromebook",
        can=["rate myself on every target", "fix my Day 1 model with what I learned",
             "explain the warm-room and cool-room kittens with evidence"],
        plan=["Self-check", "Mystery solved: fix my model", "Mystery solved: explain", "CFA reviews (if any opened)",
              "Enrichment (no reviews, or done)", "Driving question"],
        sections=[
            dict(nb="Self-check", label="SELF-CHECK", who="EVERYONE", minutes=4, title="Rate yourself on each target",
                 body=["Rate each target 1 to 4 in your notebook (4 = I could teach it).",
                       "LS1-1.1 DNA structure · LS1-1.2 Copy and read · LS1-1.3 One base change · LS1-1.4 Same DNA, "
                       "different jobs · LS1-1.5 Case data",
                       "Then check your 5 CFA scores. Below a B? A review for that target opened for you on Canvas."],
                 teacher="Everyone does this first."),
            dict(nb="Fix my Day 1 model", label="MYSTERY SOLVED", who="EVERYONE", minutes=7,
                 title="Fix your Day 1 model",
                 body=["Redraw your Day 1 model. Check off each part as you add it:",
                       "☐ DNA with the gene  ☐ the one-letter change  ☐ the changed amino acid",
                       "☐ the protein that works only in cool skin  ☐ the dark points"],
                 teacher="Walk the room with the checklist."),
            dict(nb="Explain: warm room or cool room?", label="MYSTERY SOLVED", who="EVERYONE", minutes=8,
                 title="Warm room or cool room?", table=KITTENS,
                 body=["Two Siamese kittens were raised from birth, one in a warm room, one in a cool room. At 12 weeks:"],
                 frame=[f"Claim: The cool-room kitten's ears are darker because {B}.",
                        "Evidence: The cool-room ear is ___ °C and ____. The warm-room ear is ___ °C and ____.",
                        f"Reasoning: Both kittens have the same changed {B}. It changes one {B} in the pigment-making {B}, "
                        "which works only in skin cooler than about 33 °C."],
                 bank=["their ears are cool enough for the protein to work", "gene", "amino acid", "protein"],
                 teacher="This is the unit's phenomenon explanation. Collect it."),
            dict(nb="Reviews or enrichment", label="CFA REVIEWS", who="ON YOUR OWN + SMALL GROUPS", minutes=15,
                 title="Do your CFA reviews",
                 body=["Scored below a B on a CFA? A review for that target opened for you on Canvas.",
                       "Do your reviews, lowest target first. Your teacher will pull small groups.",
                       "No reviews open, or all done? Do the enrichment on the next slide."],
                 teacher="Pull small groups by the lowest target. Students with no reviews go to the enrichment."),
            dict(nb="Reviews or enrichment", label="ENRICHMENT", who="NO REVIEWS, OR ALL DONE", minutes=0, same_nb=True,
                 title="The ice-pack rabbit",
                 body=["Himalayan rabbits have the same kind of temperature-sensitive pigment protein: white bodies, dark ears, "
                       "nose, feet, and tail.",
                       "In a classic experiment, scientists shaved a patch of white fur on a rabbit's back and kept it cold with an "
                       "ice pack while the fur grew back. The new fur grew in dark."],
                 frame=[f"1. Without the ice pack, the fur would grow back {B}, because the skin there is {B}.",
                        f"2. The rabbit's DNA {B}. The same {B} makes the same protein, but the protein works only in cold skin.",
                        "3. Siamese cats that live in cold places are often darker all over. Explain why in 1 or 2 sentences."],
                 bank=["white", "warm", "did not change", "gene"],
                 teacher="Key: white; warm; did not change; gene. Q3: more of their skin is cool enough for the protein to work."),
            dict(nb="Driving question", label="DRIVING QUESTION", who="EVERYONE", minutes=2,
                 title="Why are a Siamese cat's points dark?",
                 body=["Tell your partner in one sentence. Use DNA, gene, amino acid, protein, and cool.", "Tomorrow: the CSA."],
                 teacher="Cold-call 2 pairs."),
        ],
        notebook=dict(
            left=[("h", "Self-check"),
                  ("table", ["Target", "Me (1–4)"], [["LS1-1.1 DNA structure", ""], ["LS1-1.2 Copy and read a gene", ""],
                                                     ["LS1-1.3 One base change", ""], ["LS1-1.4 Same DNA, different jobs", ""],
                                                     ["LS1-1.5 Case data", ""]], [3.35, 1.0], 9, None),
                  ("h", "Fix my Day 1 model"), ("box", 1.2, "Redraw: gene, one-letter change, amino acid, protein, dark points")],
            right=[("h", "Explain: warm room or cool room?"),
                   ("table", ["Part", "My answer"], [["Claim", ""], ["Evidence", ""], ["Reasoning", ""]], [1.3, 3.15], 9, 0.5),
                   ("h", "Reviews or enrichment"), ("lines", 3), ("h", "Driving question"), ("lines", 1)]),
        key=["Explain: claim: their ears are cool enough for the protein to work (cool-room ear 26 °C, dark brown; warm-room "
             "ear 34 °C, light tan). Reasoning: gene; amino acid; protein.",
             "Enrichment: white; warm; did not change; gene. Q3: in a cold place more of the cat's skin drops below about "
             "33 °C, so the protein works in more places."],
        notes=["Day 7 follows Unit 1.3 Day 9: the self-check and the mystery wrap-up are for everyone; then CFA reviews, or the "
               "enrichment for students with no reviews. No stations."],
    ),
    dict(
        day=8, kind="csa", title="Unit 2.1 CSA", targets=PRIORITY, cfa=None,
        focus="Show what you know: DNA to proteins",
        ready="Have ready: a Chromebook and a pencil (scratch paper is fine)",
        can=["show what I know on all 5 priority targets", "use code tables and data in the questions",
             "write two explanations with evidence"],
        plan=["Log in and open the CSA", "Read each question carefully", "Use the code tables in the questions",
              "Two written responses", "Check every answer", "Submit"],
        sections=[
            dict(nb=None, label="CSA", who="FULL PERIOD · ON YOUR OWN", minutes=40,
                 title="Show what you know: Unit 2.1 CSA",
                 body=["Open Canvas: Unit 2.1 CSA: DNA to Proteins (HS-LS1-1).",
                       "13 questions on the 5 priority targets. Two are written responses your teacher grades.",
                       "Code tables are inside the questions that need them.",
                       "Work on your own. Check every answer, then submit."],
                 teacher="Allow the full period."),
        ],
    ),
]
ANIMATIONS = {  # review animations (claude.ai artifacts; share them from the page before students open them)
    4: ("Siamese Points", "https://claude.ai/artifact/8F5kotkRbVVn6i8hqHJHen"),
    5: ("Siamese Points", "https://claude.ai/artifact/8F5kotkRbVVn6i8hqHJHen"),
    6: ("Sickle Cell Chain", "https://claude.ai/artifact/1Vik4KtWpZtyBsD5YgefaV"),
}
DAY = {d["day"]: d for d in DAYS}


def minutes(d):
    """Total student minutes, notebook setup (2) and the CFA (6) included."""
    if d["kind"] in ("lab", "csa"):
        return None
    m = 2 + sum(s["minutes"] + s.get("minutes_frame", 0) for s in d["sections"])
    return m + (6 if d["cfa"] else 0)


for _d in DAYS:
    _m = minutes(_d)
    if _d["kind"] == "lesson":
        assert 20 <= _m <= 40 and len(_d["plan"]) == 6, (_d["day"], _m)
    if _d["kind"] == "review":
        assert _m <= 40, _m
