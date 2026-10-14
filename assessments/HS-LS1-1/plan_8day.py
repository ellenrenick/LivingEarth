"""Modified 8-day version of unit 2.1 (DNA to Proteins) for 2026-27, built on the Siamese cat phenomenon.

The full unit is 13 days (see pacing.json). This version keeps every priority target and its CFA, gives each
one class period, folds the supporting standard into one light day, and ends with a review day and the CSA.
Lessons are in lessons_8day.py.
"""

STANDARD = "HS-LS1-1"
MODULE_NAME = "Unit 2.1: DNA to Proteins (8-day version: Siamese Cats)"
PHENOMENON = ("Why are a Siamese cat's ears, face, paws, and tail dark while the rest of its body is cream, and why is a Siamese kitten born white? "
              "Over the unit, students find the pattern is inherited and tied to cooler skin, learn how DNA stores a gene and how the gene's message is copied and read "
              "to build a chain of amino acids, and trace how a one-letter DNA change swaps one amino acid so the pigment-making protein works only in cool skin.")

# (title, focus, standard, [CFA ids], note). Titles match the keys of LESSONS in lessons_8day.py.
DAYS = [
    ("Day 1: Launch with the Siamese cat", "Notice and wonder about a Siamese cat; temperature and litter data show the pattern is inherited and tied to cool skin. LS1-1.2: DNA holds the instructions for building proteins; a gene codes for one protein. Supporting (light): LS3-1, one set of chromosomes from each parent.", "LS1-1, LS3-1", ["LS1-1.2"],
     "Initial model of what is in a cat's cells that leads to dark ears, paws, and tail."),
    ("Day 2: What is DNA made of?", "LS1-1.1: DNA is a double helix of nucleotides (sugar, phosphate, base); base pairing; the order of bases is the message.", "LS1-1", ["LS1-1.1"], "Paper model of a nucleotide and base pairing."),
    ("Day 3: LAB, build, copy, and read a gene (gummy DNA)", "LS1-1.3: hands-on lab. Build a gene out of gummy candy, copy its message, and read the copy to build an amino acid chain; change one letter (Gly to Arg) and compare.", "LS1-1", ["LS1-1.3"],
     "Teach copy-then-read only; no mRNA or tRNA mechanics. Lab sheet is a 12-point assignment."),
    ("Day 4: What can one letter do?", "LS1-1.4: one-letter DNA changes can change an amino acid (the Siamese cat), change whether or when a protein is made, or change nothing.", "LS1-1", ["LS1-1.4"], "Card sort."),
    ("Day 5: Same DNA, different jobs", "LS1-1.5: all cells have the same DNA but use different genes; only pigment-making cells use the pigment gene; map where the changed protein works by skin temperature.", "LS1-1", ["LS1-1.5"], ""),
    ("Day 6: Case data", "LS1-1.6: trace a DNA change to a protein to an effect on the body in two cases (the Siamese cat and a human gene change).", "LS1-1", ["LS1-1.6"], ""),
    ("Day 7: Review and back to the cat", "Mastery Path reviews for any CFA below a 3 (trigger: below 2.67); revise the Day 1 model; Write It about warm-raised and cool-raised Siamese kittens.", "LS1-1", [], ""),
    ("Day 8: CSA", "CSA: priority targets for HS-LS1-1 (45 minutes, 30 points).", "LS1-1", [], "Allow the full 45 minutes."),
]

CHANGES = [
    "Each priority target gets one class period. LS1-1.3, 1.5, and 1.6 get one day instead of two (build and apply together, then the CFA).",
    "The supporting standard LS3-1 is taught lightly as part of Day 1 instead of its own day.",
    "The launch is combined with LS1-1.2 on Day 1; the phenomenon (Siamese cats) runs through every day and returns in Write It on Day 7.",
    "Nothing on the CSA is removed. All six CFAs and the review are unchanged.",
]
