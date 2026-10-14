"""Modified 8-day version of unit 2.1 (DNA to Proteins) for 2026-27.

The full unit is 13 days (see pacing.json). This version keeps every priority target and its CFA, gives each
one class period, folds the supporting standard into one light day, and ends with a review day and the CSA.
"""

STANDARD = "HS-LS1-1"
MODULE_NAME = "Unit 2.1: DNA to Proteins (8-day version)"

# (title, focus, standard, [CFA ids], note)
DAYS = [
    ("Day 1: Launch and DNA structure", "Launch: anchoring phenomenon and pre-assessment. LS1-1.1: DNA is a double helix of nucleotides (sugar, phosphate, base).", "LS1-1", ["LS1-1.1"],
     "About 15 minutes for the launch, 20 for DNA structure, 6 for the CFA."),
    ("Day 2: DNA holds the instructions (and LS3-1, light)", "LS1-1.2: DNA holds the instructions for building proteins; a gene codes for one protein. Supporting (light): LS3-1.1 to LS3-1.3, how chromosomes, DNA, and genes are related and passed from parents.", "LS1-1, LS3-1", ["LS1-1.2"],
     "Supporting standard LS3-1 is taught and practiced only; it is not on the CSA. Keep it to about 15 minutes."),
    ("Day 3: Copy, then read", "LS1-1.3: a gene's message is copied and the copy is read to build a chain of amino acids. Use the code table.", "LS1-1", ["LS1-1.3"],
     "Teach copy-then-read only; no mRNA or tRNA mechanics."),
    ("Day 4: One base change", "LS1-1.4: changing one DNA base can change one amino acid, and so how a protein works. Not every change matters.", "LS1-1", ["LS1-1.4"], ""),
    ("Day 5: Same DNA, different jobs", "LS1-1.5: the same DNA gives different cells different proteins and jobs, because cells use different genes.", "LS1-1", ["LS1-1.5"],
     "Use the gene and protein table for two cell types as the class work."),
    ("Day 6: Case data", "LS1-1.6: use case data (for example, sickle cell) to trace a DNA change to a different protein to an effect on the body.", "LS1-1", ["LS1-1.6"],
     "Use a data table of normal and changed genes as the class work."),
    ("Day 7: Review", "Review and reteach. Students do the review sections for any CFA under 4 of 6, plus Vocabulary and Write It.", "LS1-1", [], ""),
    ("Day 8: CSA", "CSA: priority targets for HS-LS1-1 (45 minutes, 30 points).", "LS1-1", [], "Allow the full 45 minutes."),
]

CHANGES = [
    "Each priority target gets one class period. LS1-1.3, 1.5, and 1.6 get one day instead of two (build and apply together, then the CFA).",
    "The supporting standard LS3-1 is one light day (part of Day 2) instead of its own day.",
    "The launch is combined with LS1-1.1 on Day 1.",
    "Nothing on the CSA is removed. All six CFAs and the review are unchanged.",
]
