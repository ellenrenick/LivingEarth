"""Unit 2.2 (HS-LS3-2): one CFA per priority target (5 one-point auto-graded questions each, the Unit 1.3 model) and the CSA on the
Unit 1.3 blueprint: a DOK 1-2 target gets 3 auto-graded questions, a DOK 3 target gets 1 multiple-choice question plus 1
four-point written response that the teacher grades. 5 targets -> 13 questions, 19 raw points; the 26-27 CSA items were then merged in: 17 questions,
26 raw points (one extra written response), graded out of 4.

Item format is unit13_bank's: "choice" (answer = index of the key, written first; the key is moved by KEY_POSITIONS on upload),
"multi" (answer = list of indexes, all or nothing), "tf", "essay" (4-point rubric).
Boundary: no phases of meiosis, no biochemical mechanism of specific steps. Nothing here asks for the names of enzymes or
repair mechanisms.
"""


def c(prompt, choices, fb):
    return {"type": "choice", "prompt": prompt, "choices": choices, "answer": 0, "feedback": fb}


def multi(prompt, choices, answer, fb):
    return {"type": "multi", "prompt": prompt, "choices": choices, "answer": answer, "feedback": fb}


def match(prompt, pairs, fb, distractors=()):
    return {"type": "match", "prompt": prompt, "pairs": pairs, "distractors": list(distractors), "feedback": fb}


def tf(prompt, answer, fb):
    return {"type": "tf", "prompt": prompt, "answer": answer, "feedback": fb}


def tbl(head, rows):
    th = "<tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr>"
    tr = "".join("<tr>" + "".join(f"<td>{x}</td>" for x in r) + "</tr>" for r in rows)
    return f'<table border="1" cellpadding="6"><tbody>{th}{tr}</tbody></table>'


PUNNETT_GG = tbl(["", "G", "g"], [["G", "GG", "Gg"], ["g", "Gg", "gg"]])
FF_FAMILY = tbl(["", "Alleles for coat color"], [["Mom", "F and f"], ["Dad", "F and f"], ["Puppy", "f and f"]])
DNA_FAMILY = tbl(["", "Allele 1", "Allele 2"], [["Mom", "CAT", "CAT"], ["Dad", "CAT", "CGT"], ["Puppy", "CAT", "CCT"]])
XRAY = tbl(["Group of mice", "X-ray dose", "New mutations per 1,000 sperm cells"],
           [["A", "none", "3"], ["B", "low", "12"], ["C", "high", "25"]])
CHEM_NONE = tbl(["Group", "Exposed to the chemical?", "New mutations per 1,000 cells"],
                [["1", "Yes", "5"], ["2", "No", "5"]])
KENNELS = tbl(["Kennel", "Puppies checked", "Puppies with a new coat pattern (in neither parent)"],
              [["A (chemical in the water)", "1,000", "14"], ["B (clean water)", "1,000", "3"]])
SNAIL = tbl(["Trait", "Snail 1 (parent)", "Snail 2 (parent)", "Baby snail"],
            [["Shell stripe gene, allele 1", "S", "S", "S"], ["Shell stripe gene, allele 2", "s", "S", "S"]])
UV_TEXT = tbl(["Hours of UV light", "Mutations per 1,000 skin cells"], [["0", "2"], ["2", "21"], ["4", "40"]])
HAMSTER = tbl(["Hamster", "Alleles for fur length (L = long, l = short)"],
              [["Mother", "L and l"], ["Father", "L and l"], ["Pup 1", "L and L"], ["Pup 2", "L and l"], ["Pup 3", "l and l"]])
RADIATION = tbl(["Group of fruit flies", "Radiation dose", "New mutations per 1,000 egg cells"],
                [["1", "none", "4"], ["2", "low", "15"], ["3", "high", "31"]])

CFAS = {
    "LS3-2.1": [
        c("<p>Which list names three ways new genetic variation can arise?</p>",
          ["New combinations of alleles, copying errors in DNA, and mutations from the environment",
           "Eating new foods, exercising more often, and learning new skills over many years",
           "Photosynthesis, cellular respiration, and the movement of carbon through all ecosystems",
           "Changes in the weather, changes in the soil, and changes in how much food there is"],
          "The three sources are new combinations of alleles (sex cells and fertilization), errors when DNA is copied, and "
          "mutations caused by the environment."),
        c("<p>What is a mutation?</p>",
          ["A change in the order of the bases in the DNA of a cell",
           "A new combination of alleles made when an egg and a sperm join",
           "A protein that copies the DNA before a cell divides into two cells",
           "A trait that shows when an offspring has two recessive alleles"],
          "A mutation is a change in the DNA sequence."),
        tf("<p>True or false: UV light and some chemicals can cause mutations by damaging DNA.</p>", True,
           "True. UV light, X-rays, and some chemicals are environmental factors that can damage DNA and cause mutations."),
        c("<p>Two parents each have the alleles B and b. Which source of variation best explains why their puppies can be BB, "
          "Bb, or bb?</p>",
          ["New combinations of alleles when sex cells join at fertilization",
           "Copying errors that happen in every cell of the developing puppy",
           "Mutations caused by UV light shining on the puppies after birth",
           "The puppies' food and water changing their DNA as they grow"],
          "Each parent passes on one allele, so the puppies get different combinations of the alleles the parents already have."),
        multi("<p>Select the <strong>TWO</strong> sources of new genetic variation.</p>",
              ["Errors made when DNA is copied before a cell divides", "Mutations caused by UV light or chemicals",
               "Exercise and a healthy diet during a puppy's whole life", "Learning new tricks from other dogs in the kennel"],
              [0, 1], "Copying errors and mutations from the environment change the DNA. Exercise and learning do not."),
    ],
    "LS3-2.2": [
        c("<p>How many alleles of one gene does each sex cell (egg or sperm) carry?</p>",
          ["One allele of each gene, chosen at random from the two the parent has",
           "Two alleles of each gene, one from each of the parent's own parents",
           "Four alleles of each gene, two from the mother and two from the father",
           "No alleles, because sex cells do not have any genes inside of them"],
          "Each sex cell carries one allele of each gene. A child gets one from each parent, so it has two."),
        c("<p>A parent has the alleles Gg. Which sex cells can this parent make?</p>",
          ["Some sex cells with G and some sex cells with g",
           "Only sex cells that carry both G and g together at once",
           "Only sex cells with the dominant allele, which is the G allele",
           "Only sex cells that carry two copies, either two G or two g"],
          "Each sex cell gets just one of the parent's two alleles, so about half carry G and half carry g."),
        c(f"<p>Two Gg parents are crossed.</p>{PUNNETT_GG}<p>How many of the 4 boxes show the genotype gg?</p>",
          ["1 of the 4 boxes", "2 of the 4 boxes", "3 of the 4 boxes", "0 of the 4 boxes"],
          "Only one box has a g from the top and a g from the side, so 1 of 4 boxes is gg."),
        c("<p>What happens at fertilization?</p>",
          ["A sperm and an egg join, so the offspring gets one allele from each parent",
           "A body cell copies all of its DNA, so the offspring gets two copies of the same allele",
           "An egg splits in two, so the offspring gets both of its alleles from its mother only",
           "A mutation changes the alleles, so the offspring gets alleles that neither parent had"],
          "Fertilization joins two sex cells. The offspring gets one allele from each parent: a new combination."),
        c("<p>Two siblings have the same parents. One is BB and the other is Bb. What best explains this?</p>",
          ["Each sibling got a different combination of alleles from the same two parents",
           "One sibling's DNA mutated, because siblings can never have different genotypes",
           "Siblings with the same parents always get the same alleles, so a record is wrong",
           "The environment changed one sibling's alleles after that sibling was born"],
          "Sex cells carry one allele at random, so each fertilization can make a different combination."),
    ],
    "LS3-2.3": [
        c("<p>A cell copies its DNA before it divides, and one letter is copied wrong. What is this?</p>",
          ["A copying error that can become a mutation",
           "A new combination of alleles from fertilization",
           "A change that is always caused by the environment",
           "A normal change that never affects the DNA at all"],
          "An error made when DNA is copied that is not fixed becomes a mutation."),
        tf("<p>True or false: A mutation in a person's skin cell can be passed on to their children.</p>", False,
           "False. Only mutations in cells that make eggs or sperm can be passed to the next generation."),
        c("<p>In an animal, which mutation can be inherited by its offspring?</p>",
          ["A mutation in a cell that makes eggs or sperm", "A mutation in a muscle cell of its leg",
           "A mutation in a skin cell caused by a sunburn", "A mutation in a lung cell caused by smoke"],
          "Only changes in cells that become eggs or sperm are inherited."),
        c("<p>A lifeguard has many UV-damaged skin cells. Why won't her children inherit these mutations?</p>",
          ["The mutations are in skin cells, which do not become eggs or sperm",
           "UV light never changes the DNA of any cell in the whole human body",
           "Mutations are only passed on from fathers to children, never from mothers",
           "Mutations in skin cells are always repaired before they can ever matter"],
          "A mutation is inherited only when it is in a cell that makes eggs or sperm."),
        c("<p>A one-letter mutation changes one amino acid in a protein. Why might this matter?</p>",
          ["A different amino acid can make the protein work differently",
           "The protein is no longer made by any of the cells of the body",
           "Every other gene in the cell changes in the same way at once",
           "The mutation is copied into every cell of the body right away"],
          "Base order sets amino acid order, and a different amino acid can change how a protein works (Unit 2.1)."),
    ],
    "LS3-2.4": [
        c(f"<p>A coat-color gene has the alleles F and f.</p>{FF_FAMILY}<p>Which claim is best supported by the data?</p>",
          ["The puppy's alleles came from a new combination, because f was already in both parents",
           "The puppy's alleles came from a mutation, because the puppy differs from both parents",
           "The puppy's alleles came from UV light, because the puppy looks different from its parents",
           "The puppy's alleles came from a copying error, because the puppy has two of the same allele"],
          "Both parents carry f, so the puppy ff is a new pairing of alleles the parents already had."),
        c(f"<p>A coat-color gene:</p>{DNA_FAMILY}<p>Which claim is best supported by the data?</p>",
          ["The CCT allele came from a mutation, because neither parent has a CCT allele",
           "The CCT allele came from fertilization, because the puppy gets one allele from each parent",
           "The CCT allele came from the dad, because the dad has a CGT allele in his DNA",
           "The CCT allele is not new, because the mom has the CAT allele on both copies"],
          "Neither parent has CCT, so it is a new allele: a mutation."),
        c(f"<p>Scientists exposed mice to X-rays.</p>{XRAY}<p>Which claim is best supported by the data?</p>",
          ["X-rays increased the number of mutations, because the counts rise as the dose rises",
           "X-rays had no effect on mutations, because the group with no X-rays also had mutations",
           "Copying errors caused every mutation, because all three groups had some mutations",
           "The low dose caused more mutations than the high dose, because the low dose came first"],
          "The mutation count goes up with the dose. The no-X-ray group shows the baseline from copying errors."),
        c("<p>Which new data would best show that a new allele came from an environmental mutagen and not from a copying "
          "error?</p>",
          ["Mutation counts for a group exposed to the mutagen and a group that was not exposed",
           "The total number of puppies in each litter that the parents had over several years",
           "The coat colors of the puppies' grandparents on both sides of the whole family tree",
           "The number of alleles that each sex cell of the parents carries for the same gene"],
          "Comparing an exposed group with an unexposed group shows whether the exposure changed the number of mutations."),
        c(f"<p>Scientists compared mutation counts.</p>{CHEM_NONE}<p>A student claims the chemical caused mutations. "
          "Which statement best evaluates the claim?</p>",
          ["The data do not support the claim, because both groups had the same number of mutations",
           "The data support the claim, because the exposed group had some mutations in its own cells",
           "The data support the claim, because chemicals always change the DNA of every cell in the body",
           "The data cannot be used, because there are two groups to compare in the table"],
          "If the chemical caused mutations, the exposed group would have more. Both groups had 5."),
    ],
}

CFA_TITLE = {t: f"Unit 2.2 CFA {t}: {n}" for t, n in
             [("LS3-2.1", "Three sources of variation"), ("LS3-2.2", "Sex cells and fertilization"),
              ("LS3-2.3", "Copying errors and mutations"), ("LS3-2.4", "Read data, make a claim")]}

# ---------------------------------------------------------------------------
# CSA: 17 questions (26 raw points). Includes the items from the old 26-27 HS-LS3-2 CSA (docs 1EmaRdAk3v...), rewritten with
# similar-length choices. Nothing repeats a CFA question.
# ---------------------------------------------------------------------------
CSA = [
    # LS3-2.1 (DOK 1): 3 auto-graded
    ("LS3-2.1", c("<p>A scientist studies why the pups in a hamster litter have different traits. Which list names three sources "
                  "of new genetic variation?</p>",
                  ["New combinations of alleles, copying errors in DNA, and mutations caused by X-rays",
                   "Growth in the pups' bodies, healthy food for the mother, and a warm, safe place for the nest",
                   "Photosynthesis in plants, the carbon cycle in the soil, and heat energy leaving the cage",
                   "Changes in the cage temperature, changes in the pups' weight, and changes in the length of their fur"],
                  "New combinations of alleles, copying errors, and mutations from the environment are the three sources.")),
    ("LS3-2.1", match("<p>Match each vocabulary word to its definition.</p>",
                      [("Mutation", "A change in the DNA sequence"),
                       ("Chromosome", "A DNA structure that holds many genes"),
                       ("Sex cell (gamete)", "An egg cell or a sperm cell"),
                       ("Meiosis", "Cell division that makes sex cells with mixed genes"),
                       ("Crossing over", "Chromosomes swap pieces while sex cells form")],
                      "Mutation = change in DNA. Chromosome = DNA structure with many genes. Sex cell = egg or sperm. Meiosis = "
                      "division that makes sex cells. Crossing over = chromosomes swap segments.",
                      ["A copy of a gene found in a body cell"])),
    ("LS3-2.1", match("<p>Match each source of variation to the correct description.</p>",
                      [("Crossing over", "Chromosomes exchange pieces of DNA"),
                       ("Independent assortment", "Chromosomes are sorted into sex cells at random"),
                       ("DNA copying error", "A mistake is made while DNA is copied"),
                       ("Environmental mutation", "Radiation or chemicals change the DNA")],
                      "Crossing over and independent assortment mix the genes in sex cells. A copying error happens when DNA is "
                      "copied. An environmental mutation is caused by something outside the cell, like radiation.",
                      ["New foods switch on genes in every cell"])),
    ("LS3-2.1", c("<p>Which statement best explains why siblings can inherit different traits from the same parents?</p>",
                  ["Each sex cell carries a different mix of the parents' genes",
                   "Each sibling receives the same set of chromosomes from both parents",
                   "Each sibling's DNA is rewritten by the environment before birth",
                   "Each sibling gets a mutation in every gene that a parent has"],
                  "Meiosis and fertilization make a different mix of genes for each sibling.")),
    ("LS3-2.1", multi("<p>Select the <strong>TWO</strong> environmental factors that can cause mutations by damaging DNA.</p>",
                      ["UV light from the sun", "Certain chemicals in smoke", "A diet with plenty of protein",
                       "Regular exercise every day"], [0, 1],
                      "UV light and some chemicals damage DNA. Diet and exercise do not.")),
    # LS3-2.2 (DOK 2): 3 auto-graded
    ("LS3-2.2", c(f"<p>Two Gg parents are crossed.</p>{PUNNETT_GG}<p>What is the chance that an offspring is Gg?</p>",
                  ["50% (2 of the 4 boxes)", "25% (1 of the 4 boxes)", "75% (3 of the 4 boxes)", "100% (all 4 boxes)"],
                  "Two boxes show Gg, so the chance is 2 of 4, or 50%.")),
    ("LS3-2.2", c("<p>Which statement best describes how sex cells mix alleles?</p>",
                  ["Each sex cell gets one allele of each gene, and fertilization joins two sex cells into a new combination",
                   "Each sex cell gets both alleles of each gene, and fertilization removes one allele from each sex cell",
                   "Each sex cell makes new alleles of its own, and fertilization copies those alleles into the offspring",
                   "Each sex cell gets all the alleles of its parent, and fertilization mixes them together in all of the body cells"],
                  "One allele per gene in each sex cell, and two sex cells join at fertilization.")),
    ("LS3-2.2", c(tbl(["", "Alleles for shell stripes (S = stripes, s = none)"],
                      [["Snail 1", "S and s"], ["Snail 2", "S and S"]])
                  + "<p>These two snails are the parents. Which offspring genotypes are possible?</p>",
                  ["SS or Ss only, because Snail 2 can only pass on S",
                   "ss only, because Snail 1 is the parent that passes on s",
                   "Ss only, because each parent passes on a different allele",
                   "SS, Ss, or ss, because both parents can pass on S or s"],
                  "Snail 2 can only pass on S. Snail 1 passes on S or s. The offspring are SS or Ss.")),
    # LS3-2.3 (DOK 2): 3 auto-graded
    ("LS3-2.3", c("<p>Which event can lead to a mutation that is passed on to the next generation?</p>",
                  ["A copying error in a cell that makes sperm", "A copying error in a skin cell of the face",
                   "UV damage to a skin cell on the shoulder", "A chemical changing DNA in a cell of the liver"],
                  "Only changes in cells that make eggs or sperm are inherited.")),
    ("LS3-2.3", c(UV_TEXT + "<p>Scientists exposed skin cells to UV light. Which statement does the data best support?</p>",
                  ["UV light causes mutations, and more UV light causes more mutations",
                   "UV light does not cause mutations, because the 0-hour group had some",
                   "Copying errors cause all mutations, because every group had mutations",
                   "Mutations caused by UV light are always passed on to children"],
                  "The mutation count rises with UV exposure, so UV light causes mutations. The data say nothing about "
                  "inheritance.")),
    ("LS3-2.3", tf("<p>True or false: A mutation caused by a chemical in smoke in a person's lung cell will be inherited by "
                   "their children.</p>", False,
                   "False. A lung cell does not become an egg or sperm.")),
    # LS3-2.4 (DOK 3): 1 MC + 1 written response
    ("LS3-2.4", c(HAMSTER + "<p>Which claim is best supported by the data?</p>",
                  ["The pups' alleles came from new combinations, because every allele was already in the parents",
                   "The pups' alleles came from mutations, because Pup 1 and Pup 3 differ from both of the parents",
                   "The pups' alleles came from X-rays, because Pup 2 is the only one like the parents",
                   "The pups' alleles came from copying errors, because Pup 3 has two copies of the same allele"],
                  "L and l are both in the parents. The pups show new pairings of those alleles.")),
    ("LS3-2.4", c("<p>In a population of plants near a nuclear power plant, scientists find a few plants with twisted stems "
                  "and spotted leaves. DNA tests show changes in their genes that were not present in earlier generations.</p>"
                  "<p>Which explanation best supports how these new traits could have appeared?</p>",
                  ["Radiation near the plant likely caused DNA mutations, which led to the new traits",
                   "The traits appeared at random during meiosis because the plants were exposed to heat",
                   "The changes came from normal aging in the plants, so they will not be passed on",
                   "Chemicals in the soil changed the plants' RNA but not their DNA, causing the traits"],
                  "The genes changed and were not in earlier generations, and the plants grew near radiation, so radiation-caused "
                  "mutations fit best.")),
    ("LS3-2.4", {
        "type": "essay",
        "prompt": f"<p>Scientists exposed fruit flies to radiation and counted new mutations in the cells that make eggs.</p>{RADIATION}"
                  "<p>Write a claim about what caused the new mutations. Support your claim with <strong>two pieces of "
                  "evidence</strong> from the table, and explain your <strong>reasoning</strong> (how the evidence supports the claim "
                  "and what the no-radiation group shows).</p>",
        "rubric": [
            (4, "Advanced", "Claim: radiation caused (most of) the new mutations. Evidence: cites at least two numbers (for example 4 with no "
                            "radiation, 15 with a low dose, 31 with a high dose) and notes the count rises with the dose. Reasoning: explains the "
                            "no-radiation group shows the baseline from copying errors, and the extra mutations rise with the dose."),
            (3, "Proficient", "Claim is correct. Cites at least one number from the table. Reasoning links the data to the claim but does "
                              "not explain the baseline or the rise with dose."),
            (2, "Developing", "Claim is correct but evidence is vague (no numbers) or reasoning is missing."),
            (1, "Beginning", "Names a source of variation without using the table, or the claim does not match the data."),
        ],
        "grading_notes": ["Accept \"copying errors cause the baseline of 4\" as a strong addition.",
                          "A claim that only says \"radiation\" with no mention of the dose rising is a 2 or 3.",
                          "Do not require the word \"baseline.\" Look for the idea that the no-radiation group shows what copying "
                          "errors alone do."],
        "exemplar": "Claim: The radiation caused the extra mutations. Evidence: The flies with no radiation had 4 new mutations per 1,000 "
                    "egg cells, but the high-dose flies had 31, and the low-dose flies had 15. Reasoning: The no-radiation group shows "
                    "the mutations that copying errors make on their own. The count went up as the dose went up, so the radiation is what "
                    "caused the extra mutations.",
    }),
    # LS3-2.5 (DOK 3): 1 MC + 1 written response
    ("LS3-2.5", c("<p>A student is studying why siblings can look very different. The student writes: “Siblings have different "
                  "traits because sometimes meiosis doesn't copy genes correctly, which creates mistakes in the DNA.”</p>"
                  "<p>Meiosis makes egg and sperm cells by mixing chromosomes from each parent through crossing over and "
                  "independent assortment. Which evaluation best explains the strengths or weaknesses of the student's claim?</p>",
                  ["The claim is partly incorrect, because meiosis mixes genes into new combinations, not DNA mistakes",
                   "The claim is correct, because meiosis always causes mutations and mutations make siblings look different",
                   "The claim is supported, because copying mistakes in meiosis are the main cause of inherited variation",
                   "The claim is wrong, because traits are controlled only by the environment and are not set by the DNA"],
                  "Meiosis mixes genes into new combinations. That mixing, not DNA mistakes, is the main reason siblings differ.")),
    ("LS3-2.5", {
        "type": "essay",
        "prompt": f"<p>A farmer finds a calf with a new coat pattern that neither parent has. The farmer claims a chemical in the pasture's "
                  f"water caused a mutation. A veterinarian says it was a <strong>copying error</strong>, which happens in every herd.</p>"
                  f"{tbl(['Herd', 'Calves checked', 'Calves with a new coat pattern'], [['Pasture with the chemical in its water', '2,000', '6'], ['Barn with clean water', '2,000', '5']])}"
                  "<p>Use the data and what you know about inheritance to <strong>defend the better explanation</strong>. Include (1) numbers "
                  "from the table, (2) why the veterinarian's explanation fits the data better, and (3) in which kind of cell the change "
                  "had to happen for the calf to have a pattern that neither parent has, and why.</p>",
        "rubric": [
            (4, "Advanced", "Defends the veterinarian's explanation with all three parts: cites the numbers (6 vs 5 per 2,000, almost the same, "
                            "so the chemical added few if any mutations); explains that copying errors happen at a similar low rate in both "
                            "herds; and explains the change had to be in a cell that makes eggs or sperm, because only those changes are "
                            "inherited."),
            (3, "Proficient", "Defends the veterinarian's explanation, cites the numbers, and gives two of the three parts correctly."),
            (2, "Developing", "Picks the veterinarian but the evidence or reasoning is vague, or only one part is correct."),
            (1, "Beginning", "Picks a side without using the data or the inheritance idea, or picks the farmer's claim with no support."),
        ],
        "grading_notes": ["The pattern is new in the calf and neither parent has it, so the change must have been in a cell that makes eggs "
                          "or sperm in one of the parents. A change in any other body cell could not be passed on.",
                          "Accept \"6 and 5 are almost the same\" for the data point. Do not require the word \"baseline.\"",
                          "Give credit for noting the data cannot rule out that a few of the 6 came from the chemical, because the "
                          "difference is small."],
        "exemplar": "The veterinarian's explanation fits better. The pasture with the chemical had 6 calves with a new pattern out of 2,000, and "
                    "the barn with clean water had 5 out of 2,000. That is almost the same, so the chemical did not add many mutations. Copying "
                    "errors happen in every herd at a similar low rate, which fits both numbers. For a calf to have a pattern that neither "
                    "parent has, the change had to happen in a cell that makes eggs or sperm, because only those changes are inherited.",
    }),
    ("LS3-2.5", {
        "type": "essay",
        "prompt": "<p>In families, children do not always look the same as their parents. What leads to variation (differences) "
                  "within a family?</p><p>Make a <strong>claim</strong> explaining how inheritable genetic variation occurs. Use "
                  "<strong>evidence from at least two different sources</strong> of genetic variation to support your claim. Then "
                  "<strong>explain</strong> how your evidence supports your claim.</p>",
        "rubric": [
            (4, "Advanced", "Clear claim that inherited variation comes from changes in the genetic information passed to offspring. Uses "
                            "at least two sources (new combinations of alleles, copying errors, environmental mutations) with a specific "
                            "example for each, and explains why each example would be inherited (it is in a cell that makes eggs or sperm)."),
            (3, "Proficient", "Correct claim with two sources named and one example explained; reasoning is partly complete."),
            (2, "Developing", "Names one source, or names two without examples or reasoning."),
            (1, "Beginning", "Mentions variation or mutations in general with no source tied to inheritance."),
        ],
        "grading_notes": ["Accept alleles mixing at fertilization, crossing over, or independent assortment as one source.",
                          "Accept DNA copying errors and radiation, chemicals, or UV as sources.",
                          "Reasoning must say why the change is inherited, not only that it happens."],
        "exemplar": "Claim: Genetic variation in a family comes from new combinations of alleles and from mutations. Evidence: Each parent "
                    "makes sex cells with a different mix of alleles, so two siblings get different pairs, like one puppy that is Bb and a "
                    "sibling that is bb. Mutations also add new alleles: an error when DNA is copied, or radiation, can change a gene. "
                    "Reasoning: A mixed combination is inherited because it is in the egg and sperm that join at fertilization, and a "
                    "mutation is inherited only if it happens in a cell that makes eggs or sperm. Both sources change the information "
                    "children receive, so children differ from their parents.",
    }),
]

CSA_TITLE = "Unit 2.2 CSA: Inherited Instructions (HS-LS3-2)"
