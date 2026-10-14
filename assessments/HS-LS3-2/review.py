"""Unit review for HS-LS3-2 (unit 2.2). Done on the review day, built around the CFAs (no practice test).

Boundary: no phases of meiosis; no biochemical mechanisms.
"""

STANDARD = "HS-LS3-2"
UNIT_TITLE = "Inherited Instructions"
GOAL = ("Make and defend a claim, based on evidence, that inheritable genetic variation comes from new combinations "
        "of alleles, copying errors, and mutations caused by the environment.")

KEY_IDEAS = [
    "<strong>Genetic variation</strong> is differences in genes among the individuals of a population.",
    "<strong>New combinations:</strong> each sex cell gets one allele of each gene, and fertilization joins two sex cells at random. Siblings get different mixes of the same alleles.",
    "<strong>Copying errors:</strong> when DNA is copied, a mistake can change a base. Each child has some new changes that neither parent has.",
    "<strong>Environmental mutations:</strong> UV light, radiation, and some chemicals can change DNA.",
    "<strong>A mutation is passed on only if it is in a cell that makes sex cells.</strong> A mutation in a skin cell is not inherited.",
    "<strong>To decide the source of a variation, use data:</strong> if both alleles were already in the parents it is a new combination; if the sequence is in neither parent it is a mutation.",
]

VOCAB = {
    "bank": ["genetic variation", "allele", "sex cell", "meiosis", "fertilization", "mutation"],
    "blanks": [
        ("Differences in genes among the individuals of a population are called ____________.", "genetic variation"),
        ("One version of a gene is an ____________.", "allele"),
        ("An egg or a sperm is a ____________.", "sex cell"),
        ("The kind of cell division that makes sex cells is ____________.", "meiosis"),
        ("The joining of a sperm and an egg is ____________.", "fertilization"),
        ("A change in the base sequence of DNA is a ____________.", "mutation"),
    ],
}

SECTIONS = [
    {"id": "A", "title": "Three sources of variation", "lts": ["LS3-2.1"],
     "intro": "<p>Sort each situation into: <em>new combination of alleles</em>, <em>copying error</em>, or <em>environmental mutation</em>.</p>",
     "items": [
         ("Two brown-eyed parents have a child with blue eyes, and both parents carry the blue allele.", "New combination of alleles."),
         ("A base in a child's DNA is not found in either parent, and no unusual exposure is known.", "Copying error (a mutation arising when DNA was copied)."),
         ("Seeds from plants exposed to strong UV light grow into more plants with an odd leaf color than normal.", "Environmental mutation (UV light)."),
         ("List the three sources of new genetic variation.", "New combinations from meiosis and fertilization, copying errors, and mutations caused by the environment."),
     ]},
    {"id": "B", "title": "Mixing alleles", "lts": ["LS3-2.2"],
     "intro": "<p>Each parent has alleles <strong>R</strong> and <strong>r</strong>.</p>",
     "items": [
         ("How many alleles of a gene does each sex cell carry? Which can each parent's sex cells carry?", "One. Each can carry R or r."),
         ("What offspring combinations are possible?", "RR, Rr, or rr."),
         ("Explain in 2 sentences how meiosis and fertilization make brothers with the same parents different from each other.", "Each sex cell gets a different mix of the parent's alleles, and fertilization joins two sex cells at random, so each brother gets a different new combination."),
     ]},
    {"id": "C", "title": "Mutations and inheritance", "lts": ["LS3-2.3"],
     "intro": "<p>Think about which cells a mutation happens in.</p>",
     "items": [
         ("A hiker's skin cells are mutated by UV light. Will her children inherit the mutation? Explain.", "No, not from skin cells. Only mutations in cells that make sex cells are passed to children."),
         ("A mutation happens in a cell that will become an egg. Could a child inherit it?", "Yes, because the change is in a sex cell."),
         ("Scientists find about 60 base changes in each child that neither parent has. What does this show?", "Copying errors produce new variation in every generation."),
         ("True or false: All mutations are harmful. Explain.", "False. Mutations can be harmful, helpful, or have no effect."),
     ]},
    {"id": "D", "title": "Reading data as evidence", "lts": ["LS3-2.4"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th></th><th>Gene sequences</th></tr><tr><td>Mother</td><td>CAT and CAT</td></tr><tr><td>Father</td><td>CAT and CGT</td></tr><tr><td>Child 1</td><td>CAT and CGT</td></tr><tr><td>Child 2</td><td>CAT and CCT</td></tr></table>",
     "items": [
         ("Where did Child 1's pair come from?", "A new combination of alleles already in the parents."),
         ("Where did Child 2's CCT come from? How do you know?", "A mutation, because neither parent has CCT."),
         ("What data would show a variation is a mutation and not a new combination?", "A sequence in the child that is in neither parent, or a trait that never appeared in the family records."),
     ]},
    {"id": "E", "title": "Make and defend a claim", "lts": ["LS3-2.5", "LS3-2.6"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Group of fruit flies</th><th>Offspring with a new eye color (out of 1,000)</th></tr><tr><td>Normal conditions</td><td>3</td></tr><tr><td>Exposed to X-rays</td><td>55</td></tr></table>",
     "items": [
         ("Write a claim about the cause of the new eye color, using two numbers.", "X-rays caused mutations that were inherited: 55 of 1,000 offspring had the new color after X-rays compared with 3 of 1,000 in normal conditions."),
         ("A classmate says the eye color came from the food the flies ate. What evidence would you need to defend your claim against this?", "Both groups ate the same food, so food cannot explain the difference; only the X-rays differed."),
         ("Beetles with a spotted pattern appear at the same rate in clean and polluted ponds, and both parents of each carry the allele. Defend the claim that it is an inherited new combination, not a mutation from pollution.", "If pollution caused it, polluted ponds would have more spotted beetles. The same rate in clean ponds and parents who both carry the allele fit a new combination of existing alleles."),
     ]},
]

WRITE = {
    "prompt": ("<p>A lab keeps records of its frogs. A tadpole is born with a new orange spot pattern. The records show:</p>"
               "<table border=\"1\" cellpadding=\"6\"><tr><th></th><th>Data</th></tr>"
               "<tr><td>Orange spots in earlier generations</td><td>None in the previous 15 generations</td></tr>"
               "<tr><td>The tadpole's DNA</td><td>A base change in a color gene that neither parent has</td></tr>"
               "<tr><td>Parents' exposure</td><td>The mother's eggs were kept in water with a chemical known to damage DNA</td></tr></table>"
               "<p>Write an explanation: <strong>Claim</strong> (the most likely source of the variation), <strong>Evidence</strong> (at least two data points), and <strong>Reasoning</strong> (how this source makes a variation that can be inherited). Then say why it is <em>not</em> a new combination of alleles.</p>"),
    "checklist": ["Claims a mutation, most likely caused by the chemical",
                  "Uses at least two data points (none in 15 generations; base change in neither parent; chemical exposure)",
                  "Explains that the change was in a cell that makes sex cells so it could be inherited",
                  "Explains why a new combination of existing alleles does not fit (neither parent has the sequence)",
                  "Does not use phases of meiosis or chemistry details"],
    "exemplar": ("The orange spots are most likely a mutation caused by the chemical. Orange spots never appeared in the previous 15 generations, the tadpole has a base change that neither parent has, and the mother's eggs were exposed to a chemical that damages DNA. "
                 "The chemical changed the DNA in a cell that became an egg, so the change was passed to the tadpole. It is not a new combination of alleles, because a new combination only mixes alleles the parents already have, and neither parent has this one."),
}
