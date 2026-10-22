"""Unit 2.2 Inherited Instructions (HS-LS3-2), 2026-27: 11 class days, Mon Nov 9 to Tue Dec 1.

The department workbook (Living_Earth_Linked_Workbook 26-27, tab "2.2 Inherited") plans 15 days. The LE Planner has 11 class
days between Nov 9 and Dec 1 (Nov 11 Veterans Day and Nov 23-27 Fall Break are off), so this version compresses the way Unit
2.1 did (13 days to 8): every priority target gets one class period, the supporting standard LS3-3 is taught through the four
resources already linked in the planner (Genetics Notes and Monster Genetics), the unit ends with the CSA on Dec 1, and the
Nov 20 "Catch Up Day" is kept as the review and Mastery Path day.

Every lesson follows CLAUDE.md (pace and style, modeled on Unit 1.3 Short Lessons A and B): about 30 minutes of student work
including the CFA (20 to 40 in all), short activities, one worked example, a small data table with real numbers, a sentence
frame and a scrambled word bank on every fill-in, one slide per notebook section in notebook order, and the CFA last, from
memory. Day 11 (CSA) uses the full period.

Everything here is data. build.py turns it into slides, Canvas pages, CFAs, and the CSA.
"""

import random

UNIT = "Unit 2.2"
UNIT_NAME = "Inherited Instructions"
STANDARD = "HS-LS3-2"
MYSTERY = "The Puppy Puzzle"
DRIVING_Q = "How can puppies from the same parents be similar to their parents, but not exactly the same as them or each other?"
PE = ("Make and defend a claim based on evidence that inheritable genetic variations may result from (1) new genetic "
      "combinations through meiosis, (2) viable errors occurring during replication, and/or (3) mutations caused by "
      "environmental factors.")
BOUNDARY = "No phases of meiosis; no biochemical mechanism of specific steps."

# Workbook (Living Earth Standards and Learning Targets 26-27, Targets tab). (id, short name, DOK, "I can", tier)
TARGETS = [
    ("LS3-2.1", "Three sources of variation", 1, "I can name three ways new genetic variation arises.", "Priority"),
    ("LS3-2.2", "Sex cells and fertilization", 2,
     "I can describe how making sex cells and fertilization mix alleles into new combinations.", "Priority"),
    ("LS3-2.3", "Copying errors and mutations", 2,
     "I can explain how copying errors and things like UV light change genes, and when that change is inherited.", "Priority"),
    ("LS3-2.4", "Read data, make a claim", 3,
     "I can read data and make a claim, backed by that data, about what caused a genetic variation.", "Priority"),
    ("LS3-2.5", "Defend the claim", 3,
     "I can defend my claim against another explanation using the evidence.", "Priority"),
    ("LS3-3.1", "Punnett squares", 1,
     "I can use a Punnett square to show the possible allele combinations from a cross.", "Supporting"),
    ("LS3-3.2", "Chances and real counts", 2,
     "I can calculate the chance of each trait and compare it with real counts.", "Supporting"),
    ("LS3-3.3", "Traits in a population", 3,
     "I can use probability to explain how traits vary and spread in a population, including effects of environment.",
     "Supporting"),
]
TARGET = {t[0]: t for t in TARGETS}
PRIORITY = [t[0] for t in TARGETS if t[4] == "Priority"]


def scramble(words):
    """Word bank order: never answer order (fixed seed, so reruns match). No word keeps its answer-order spot when the bank
    has different words, and in banks of 4 or more no two answer-order neighbours stay side by side."""
    words, original = list(words), list(words)
    if len(set(words)) < 2:
        return words
    rng = random.Random(" ".join(words))

    def ordered(w):
        return any(a == b for a, b in zip(w, original)) or (len(w) > 3 and any(
            original.index(x) + 1 == original.index(y) for x, y in zip(w, w[1:])))
    for _ in range(500):
        if not ordered(words):
            break
        rng.shuffle(words)
    return words


B = "____"

# ---------------------------------------------------------------------------
# Data tables (real numbers; a simplified class data set modeled on real patterns)
# ---------------------------------------------------------------------------
LITTER = (["", "Fur color", "Ear shape", "Pattern"],
          [["Mom", "Black", "Floppy", "Spotted"], ["Dad", "Brown", "Pointed", "Solid"],
           ["Puppy A", "Black", "Floppy", "Solid"], ["Puppy B", "Brown", "Pointed", "Spotted"],
           ["Puppy C", "Black", "Pointed", "Spotted"], ["Puppy D", "Brown", "Floppy", "Solid"]])
CARDS = (["Offspring", "Fur color (P1 + P2)", "Ear shape (P1 + P2)", "Pattern (P1 + P2)"],
         [["1 (done for you)", "Black + White", "Floppy + Pointed", "Spotted + Solid"], ["2", "", "", ""], ["3", "", "", ""]])
COAT = (["Alleles the cat has", "Coat color"], [["BB", "Black (done for you)"], ["Bb", ""], ["bb", ""]])
PEAS = (["Genotype", "Phenotype"], [["TT", "Tall (done for you)"], ["Tt", ""], ["tt", ""]])
ZYG = (["Genotype", "Homozygous or heterozygous?"],
       [["TT", "Homozygous (done for you)"], ["Tt", ""], ["tt", ""], ["Rr", ""]])
PUNNETT_TT = (["", "T", "t"], [["T", "TT", "Tt"], ["t", "Tt", "tt"]])
MONSTER = (["Trait", "Allele 1 (heads)", "Allele 2 (tails)"],
           [["Eyes", "Two small eyes (E)", "One large eye (e)"], ["Eye color", "Red (R)", "White (r)"],
            ["Skin color", "Green (G)", "Blue (g)"]])
MALE = (["Trait", "Genotype", "Phenotype"],
        [["Eyes", "ee", "One large eye (done for you)"], ["Eye color", "", "White"], ["Skin color", "Gg", ""],
         ["Tail shape", "", "Straight"], ["Tail color", "Pp", ""]])
PUNNETT_GG = (["", "G", "g"], [["G", "GG", "Gg"], ["g", "Gg", "gg"]])
CLASS_COUNTS = (["Baby's skin color", "Punnett prediction", "Class count (sample)", "Class percent"],
                [["Green", "75%", "22 of 30", "73%"], ["Blue", "25%", "8 of 30", "27%"]])
UV = (["Hours of UV light", "Mutations per 1,000 skin cells"],
      [["0 (none)", "2"], ["1", "9"], ["2", "21"], ["4", "40"]])
CASES = (["Case", "Where the DNA changed", "Inherited?"],
         [["A", "UV hits a skin cell", "No (done)"],
          ["B", "Copy error in a sperm-making cell", ""],
          ["C", "Copy error in a muscle cell", ""],
          ["D", "X-rays hit an egg-making cell", ""],
          ["E", "Smoke chemical hits a lung cell", ""]])
LITTER_ALLELES = (["", "Alleles for fur color (B = black, b = brown)"],
                  [["Mom", "B and b"], ["Dad", "B and b"], ["Puppies", "4 black (BB or Bb), 2 brown (bb)"]])
DNA_FAMILY = (["", "Allele 1", "Allele 2"], [["Mom", "CAT", "CAT"], ["Dad", "CAT", "CGT"], ["Puppy", "CAT", "CCT"]])
XRAY = (["Group of mice", "X-ray dose", "New mutations per 1,000 sperm cells"],
        [["A", "none", "3"], ["B", "low", "12"], ["C", "high", "25"]])
KENNELS = (["Kennel", "Puppies checked", "Puppies with a new coat pattern (in neither parent)"],
           [["A (chemical in the water)", "1,000", "14"], ["B (clean water)", "1,000", "3"]])
HYDRANGEA = (["Soil pH", "Flower color (same DNA)"], [["5.0", "Blue"], ["6.0", "Purple"], ["7.0", "Pink"]])
GARDEN = (["Flower color", "Plants (all from one parent plant)"], [["Blue", "42"], ["Purple", "33"], ["Pink", "25"]])

# A section is one notebook heading = one slide, in notebook order.
#   nb: notebook heading · nbnote: one line for the notebook setup slide · label/who: slide kicker · minutes · title
#   body: lines · table: (head, rows) · frame: fill-in lines (each blank is ____) · bank: the answers' words (scrambled when shown)
#   teacher: what you do
# Day kinds: lesson (about 30 min with the CFA), review (the Nov 20 catch-up day), csa (full period).
DAYS = [
    dict(
        day=1, date="Mon Nov 9", kind="lesson", title="The Puppy Puzzle", targets=["LS3-2.1"], cfa=None,
        focus="How can puppies from the same parents be alike, but not identical?",
        ready="Have ready: your notebook and a pencil",
        can=["notice what is alike and different in a litter of puppies", "make a first model of how traits pass to offspring",
             "name three possible reasons offspring differ from their parents"],
        plan=["Notice and wonder", "Compare the traits", "My first model", "Three possible explanations", "Key idea",
              "Exit ticket"],
        sections=[
            dict(nb="Notice and wonder", nbnote="Two notices and two wonders about the puppies.", label="WARM-UP",
                 who="ON YOUR OWN", minutes=5, layout="warmup", title="What do you notice? What do you wonder?",
                 body=["Look at the puppies and their parents. Draw an arrow on a photo to one shared trait and one "
                       "different trait."],
                 frame=[f"I notice {B}.", f"I wonder {B}."],
                 teacher="Show your puppy photos (or the data on the next slide). Two notices and two wonders each; take "
                         "3 aloud. Steer toward: alike in some traits, different in others."),
            dict(nb="Compare the traits", nbnote="Table: who each puppy looks like.", label="EVIDENCE", who="WITH A PARTNER",
                 minutes=5, title="Compare the traits", table=LITTER,
                 body=["Worked example: Puppy A has black fur and floppy ears like Mom, and a solid pattern like Dad."],
                 frame=[f"Every puppy has some traits like Mom and some like {B}.", f"No two puppies have the same {B} of traits."],
                 bank=["Dad", "combination"],
                 teacher="Partners check Puppies B, C, D. Debrief: every puppy matches one parent for each trait, but each "
                         "puppy has a different mix. If you use your own photos, swap the table for what you see."),
            dict(nb="My first model", nbnote="A model of how traits get from parents to puppies.", label="MY FIRST MODEL",
                 who="ON YOUR OWN", minutes=8, title="The problem and my first model",
                 body=["Copy the problem: The puppies share some traits, but they are not identical. How can offspring "
                       "inherit traits from their parents and still be different from one another?",
                       "Draw: Parent 1, Parent 2, and two offspring. Use arrows to show information moving from the "
                       "parents to the offspring. Label one shared trait and one different trait.",
                       "It's OK to guess. We fix this model on Day 10."],
                 teacher="Do not correct models. Students revise them on Days 2 and 10."),
            dict(nb="Three possible explanations", nbnote="Three small sketch boxes.", label="SKETCHNOTES",
                 who="WITH A PARTNER", minutes=8, title="Three possible explanations",
                 body=["1. Information gets mixed: offspring may get different combinations of information from their parents.",
                       "2. Information changes: it may sometimes change when it is copied.",
                       "3. The environment has an effect: sunlight, temperature, or food may affect how an animal looks."],
                 frame=[f"For each box, draw it, then write one thing you notice in the puppy data and one question you have."],
                 teacher="About 2 to 3 minutes per box. Idea 3 gets sharper later: some environmental effects change only how "
                         "an animal looks (not inherited); others, like UV light, can change the DNA itself (a mutation)."),
            dict(nb="Key idea", nbnote="Copy the key idea and finish the arrow chain.", label="KEY IDEA", who="ON YOUR OWN",
                 minutes=4, title="Key idea",
                 body=["Copy: Offspring resemble their parents because they receive information from them. They may differ "
                       "because the information can be combined in different ways or may sometimes change."],
                 frame=[f"Parents → {B} → Offspring → similarities and {B}"], bank=["information", "differences"],
                 teacher="Key: information; differences."),
            dict(nb="Exit ticket", nbnote="One reason siblings can be different.", label="EXIT TICKET", who="ON YOUR OWN",
                 minutes=3, title="Why can siblings be different?",
                 body=["Pick one of the three ideas."],
                 frame=[f"One explanation for why siblings can be different is {B}.", f"The evidence from the puppies is {B}."],
                 bank=["the information is combined in different ways", "the information changes",
                       "the environment has an effect"], bank_note="(for the first blank; the second is in your own words)",
                 teacher="Collect. No CFA today: LS3-2.1 is on Day 2, after students have seen the idea of mixing."),
        ],
        key=["Notice and wonder: any observation and question about shared and different traits.",
             "Compare: Dad; combination.", "First model: look for two parents, information arrows, and offspring. Do not correct yet.",
             "Three explanations: any evidence and question for each box.", "Key idea: information; differences.",
             "Exit ticket: any one of the three ideas, with evidence from the puppy data."],
        notes=["The puppy photos are yours (the Nov 9 Genetic Variation Introduction Notes doc). The trait table is a stand-in, so the "
               "lesson works without photos.",
               "This lesson is the 57-minute \"Why Aren't Offspring Identical to Their Parents\" doc, trimmed to about 33 minutes: "
               "notice and wonder and compare traits are shortened, the problem and first model are combined, and the three "
               "sketch boxes are quick.",
               "No CFA today. The three ideas are the three sources of variation in LS3-2.1 (new combinations, copying errors, "
               "and mutations from the environment). Do not name them yet."],
    ),
    dict(
        day=2, date="Tue Nov 10", kind="lesson", title="Mixing Information", targets=["LS3-2.1"], cfa="LS3-2.1",
        focus="If offspring get information from the same two parents, why might each get a different combination?",
        ready="Have ready: your notebook, a pencil, and your group's information cards",
        can=["use cards to model how offspring get a mix of information from two parents",
             "name three sources of new genetic variation", "revise my model with what the cards show"],
        plan=["Warm-up", "Make possible offspring", "Analyze the pattern", "Revise our model", "Three sources of variation",
              "CFA LS3-2.1"],
        sections=[
            dict(nb="Warm-up", nbnote="Finish the three ideas from Day 1.", label="WARM-UP", who="ON YOUR OWN", minutes=3,
                 layout="warmup", title="What we thought last lesson",
                 body=["Today's question: If offspring get information from the same two parents, why might each get a "
                       "different combination?"],
                 frame=[f"Idea 1: information is {B} in different ways. Idea 2: information {B}. Idea 3: the {B} has an effect."],
                 bank=["combined", "changes", "environment"],
                 teacher="Key: combined; changes; environment. Copy the day's question into the notebook."),
            dict(nb="Make possible offspring", nbnote="Card table: 3 offspring.", label="CARD ACTIVITY", who="IN A GROUP",
                 minutes=12, title="Use the cards to make offspring", table=CARDS,
                 body=["Sort the cards into 6 piles: fur color, ear shape, and pattern for Parent 1, and the same 3 for Parent 2. "
                       "Shuffle each pile and take one card from every pile. Record it, put the cards back, and repeat.",
                       "Offspring 1 is done for you. Make Offspring 2 and 3."],
                 teacher="Each pile is one parent's information for one trait. Keep the six piles separate. You are not "
                         "deciding what each puppy looks like, only which combination of information it could get. Use your "
                         "own card set from the Combination of Genetics doc."),
            dict(nb="Analyze the pattern", nbnote="Finish three sentences about the pattern.", label="ANALYZE", who="ON YOUR OWN",
                 minutes=5, title="What pattern do you see?",
                 body=["Look at your 3 offspring."],
                 frame=[f"Every offspring got information from {B} parents.", f"Each offspring got a {B} combination of cards.",
                        f"Different combinations can lead to different {B}."],
                 bank=["both", "different", "traits"],
                 teacher="Key: both; different; traits. Ask: does mixing explain every difference we saw? (It leads to Day 7.)"),
            dict(nb="Revise our model", nbnote="Revise your Day 1 model.", label="REVISE MY MODEL", who="ON YOUR OWN",
                 minutes=5, title="Revise your Day 1 model",
                 body=["Show: Parent 1, Parent 2, information from each parent, the information being combined, two possible "
                       "offspring, one similarity, and one difference."],
                 frame=[f"Offspring resemble their parents because they receive {B} from both. Offspring may differ because {B}."],
                 bank=["information", "the combination is different"],
                 teacher="Look for information from both parents joining. Do not introduce the word allele yet; Day 3 does."),
            dict(nb="Three sources of variation", nbnote="Name the three sources.", label="MINI-LESSON", who="WHOLE CLASS",
                 minutes=5, title="Three sources of new variation",
                 body=["Scientists name three ways new genetic variation arises:",
                       "1. New combinations of alleles: sex cells carry one version of each gene, and fertilization puts two "
                       "together. That is what the cards modeled.",
                       "2. Copying errors: DNA is copied before cells divide, and a rare error can slip through.",
                       "3. Mutations from the environment: UV light and some chemicals can damage DNA."],
                 frame=[f"1. New {B} of alleles. 2. {B} when DNA is copied. 3. Mutations caused by the {B}."],
                 bank=["combinations", "errors", "environment"],
                 teacher="Key: combinations; errors; environment. A mutation is a change in DNA. Day 1's idea 3 is only the "
                         "environment affecting how an animal looks. Here the environment changes the DNA itself."),
        ],
        key=["Warm-up: combined; changes; environment.",
             "Offspring: any 2 offspring, each with one card per pile from each parent.",
             "Analyze: both; different; traits.", "Revise: information; the combination is different.",
             "Three sources: combinations; errors; environment."],
        notes=["Trimmed from the 57-minute \"What Information Does an Offspring Receive\" doc: the card activity runs 12 minutes "
               "with 3 offspring (the doc has 4), the analysis is three sentences, and the model revision is 5 minutes.",
               "If the card piles are small, combine the group's piles so each pile has at least 2 different cards.",
               "CFA LS3-2.1 closes the lesson. Below 4 of 5 opens the review (Mastery Path)."],
    ),
    dict(
        day=3, date="Thu Nov 12", kind="lesson", title="Genetics Notes, Part 1: Genes and Alleles", targets=["LS3-3.1"],
        cfa=None, focus="What are genes and alleles, and what do dominant and recessive mean?",
        ready="Have ready: your notebook and a pencil",
        can=["connect chromosomes, DNA, genes, proteins, and traits", "explain what an allele is",
             "tell a dominant allele from a recessive allele"],
        plan=["Warm-up", "Heredity", "Chromosomes", "Genes make proteins make traits", "How tigers get their stripes", "Alleles",
              "Dominant vs. recessive", "Black or brown cats", "Exit ticket"],
        sections=[
            dict(nb="Warm-up", nbnote="Finish the chain from Unit 2.1.", label="WARM-UP", who="ON YOUR OWN", minutes=3,
                 layout="warmup", title="From chromosome to trait",
                 body=["Recall Unit 2.1."],
                 frame=[f"A {B} is one long DNA molecule. A {B} is a section of DNA that codes for one protein, and proteins "
                        f"help produce a {B}."],
                 bank=["chromosome", "gene", "trait"],
                 teacher="Key: chromosome; gene; trait. Buyout day: these slides run themselves, so a sub can lead the day."),
            dict(nb="Heredity", nbnote="Guided notes: heredity and traits.", label="NOTES", who="ON YOUR OWN", minutes=2,
                 title="Heredity",
                 body=["Genetics is the study of heredity. Heredity is the passing of traits (or characteristics) from parents to "
                       "offspring.",
                       "For example, a tiger's stripes may be wide or narrow."],
                 frame=[f"Genetics is the study of {B}. Heredity is the passing of {B} from {B} to {B}. The width of a tiger's "
                        f"stripes is a trait {B} from its parents."],
                 bank=["heredity", "traits", "parents", "offspring", "inherited"],
                 teacher="Key: heredity; traits; parents; offspring; inherited. From slide 3 of the Genetics Notes deck."),
            dict(nb="Chromosomes", nbnote="Guided notes: chromosomes come in pairs.", label="NOTES", who="ON YOUR OWN", minutes=3,
                 title="Chromosomes", text_w=4.35,
                 img=dict(ids=["g1ebb2efc9c9_2_96"], x=5.2, y=2.35, w=4.1),
                 body=["Look at the graphic: a cell, its nucleus, and its chromosomes."],
                 frame=[f"Inside each nucleus of a cell are thread-like structures called {B}. Chromosomes come in {B}. "
                        f"You usually have {B} copies of each chromosome, one from each parent."],
                 bank=["chromosomes", "pairs", "two"],
                 teacher="Key: chromosomes; pairs; two. From slide 4 of the Genetics Notes deck (same cell and chromosome graphic)."),
            dict(nb="Genes make proteins make traits", nbnote="Guided notes: DNA, gene, protein, trait.", label="NOTES",
                 who="ON YOUR OWN", minutes=3, title="How are traits determined?", text_w=4.4, text_x=4.9,
                 img=dict(ids=["g1ebb2efc9c9_2_105"], x=0.7, y=2.15, w=3.95),
                 body=["Trace the graphic: chromosome, DNA, gene."],
                 frame=[f"{B}, also known as the molecule of life, is found within chromosomes. A {B} is a short segment of DNA. "
                        f"Genes contain instructions that make {B}, which determine {B}."],
                 bank=["DNA", "gene", "proteins", "traits"],
                 teacher="Key: DNA; gene; proteins; traits. From slide 5 of the Genetics Notes deck (same graphic)."),
            dict(nb="Genes make proteins make traits", nbnote="Guided notes: the chain for a tiger.", label="NOTES",
                 who="ON YOUR OWN", minutes=3, title="How tigers get their stripes",
                 img=dict(ids=["g1ebb2efc9c9_2_112", "g1ebb2efc9c9_2_113", "g1ebb2efc9c9_2_114", "g1ebb2efc9c9_2_115",
                               "g1ebb2efc9c9_2_116"], x=1.85, y=2.95, w=6.3),
                 body=[],
                 frame=[f"Genes found within a tiger's {B} produce {B} that determine the width of a tiger's {B}."],
                 bank=["DNA", "proteins", "stripes"],
                 teacher="Key: DNA; proteins; stripes. From slide 6 of the Genetics Notes deck (same five graphics)."),
            dict(nb="Alleles", nbnote="Guided notes and a chromosome sketch.", label="NOTES", who="ON YOUR OWN", minutes=4,
                 title="Alleles", text_w=7.3, text_x=2.2,
                 img=dict(ids=["g1ebb2efc9c9_2_128"], x=0.95, y=1.9, w=0.83),
                 body=["In your notebook, color each set of alleles on the chromosome pair a different color."],
                 frame=[f"Individuals inherit {B} forms of each {B}, one from each parent. The different variations of a gene are "
                        f"known as {B}. Alleles are represented with lowercase and uppercase {B}."],
                 bank=["two", "gene", "alleles", "letters"],
                 teacher="Key: two; gene; alleles; letters. From slide 8 of the Genetics Notes deck (same chromosome pair). "
                         "Students color the matching A/a, B/b pairs."),
            dict(nb="Dominant vs. recessive", nbnote="Guided notes: two columns.", label="NOTES", who="ON YOUR OWN", minutes=5,
                 title="Dominant vs. recessive", layout="domrec",
                 img=dict(banner="g1ebb2efc9c9_2_215", dom=["g1ebb2efc9c9_2_221", "g1ebb2efc9c9_2_222"],
                          rec=["g1ebb2efc9c9_2_231", "g1ebb2efc9c9_2_232"]),
                 body=["Alleles can be dominant or recessive."],
                 frame=[f"Dominant: {B} expressed when present. Shown as {B} letters.",
                        f"Recessive: expressed if {B} copies are present. Shown as {B} letters."],
                 bank=["always", "capital", "two", "lowercase"],
                 teacher="Key: always; capital; two; lowercase. From slides 10 to 12 of the Genetics Notes deck (same banner and "
                         "A = DOMINANT, a = recessive graphics)."),
            dict(nb="Black or brown cats", nbnote="Color the cat heads: BB, Bb, bb.", label="NOTES", who="ON YOUR OWN",
                 minutes=4, title="Black or brown cats?",
                 img=dict(ids=["g1ebb2efc9c9_2_239"], x=2.55, y=3.9, w=4.9),
                 body=["A black coat (B) is dominant to a brown coat (b) in cats. A cat needs only one B to be black. A cat needs "
                       "two b alleles to be brown.",
                       "In your notebook, color each cat head to show its color."],
                 frame=[f"A cat with Bb is {B} because {B} is dominant. A cat needs {B} copies of b to be brown."],
                 bank=["black", "B", "two"],
                 teacher="Key: BB black; Bb black; bb brown. Frame: black; B; two. From slide 13 of the Genetics Notes deck "
                         "(same BB, Bb, bb cat heads)."),
            dict(nb="Exit ticket", nbnote="One sentence on dominant and recessive.", label="EXIT TICKET", who="ON YOUR OWN",
                 minutes=3, title="Dominant or recessive?",
                 body=["Finish both sentences."],
                 frame=[f"An allele that shows up when only one copy is present is {B}. A recessive trait shows only when {B} "
                        "copies are present."],
                 bank=["dominant", "two"], teacher="Key: dominant; two."),
        ],
        key=["Warm-up: chromosome; gene; trait.", "Heredity: heredity; traits; parents; offspring; inherited.",
             "Chromosomes: chromosomes; pairs; two.", "Genes: DNA; gene; proteins; traits.",
             "Tiger stripes: DNA; proteins; stripes.", "Alleles: two; gene; alleles; letters.",
             "Dominant vs. recessive: always; capital; two; lowercase.", "Black or brown cats: BB black, Bb black, bb brown; "
             "black; B; two.", "Exit ticket: dominant; two."],
        notes=["Planner: Thu Nov 12 is a buyout day, so this is a notes day that a sub can run. The slides follow the \"26-27 "
               "GeneticsHereditySlideshow\" Genetics Notes (the first half): same wording, same fill-in words, and the same graphics "
               "(cell and chromosomes; chromosome, DNA, gene; the tiger-stripe chain; the allele chromosome pair; A = DOMINANT and "
               "a = recessive; the cat heads). Each fill-in has a scrambled word bank.",
               "No CFA today. LS3-3 is a supporting standard: taught and practiced, not on the CSA.",
               "Link: Genetics Notes slides, https://docs.google.com/presentation/d/1zLmg_vu7MzxnbCe4xbBWE76xxyEMa8TrHC_Iuja29UM/edit"],
    ),
    dict(
        day=4, date="Fri Nov 13", kind="lesson", title="Genetics Notes, Part 2: Genotype, Phenotype, and Punnett Squares",
        targets=["LS3-3.1"], cfa=None, focus="How can a Punnett square show the possible allele combinations?",
        ready="Have ready: your notebook and a pencil",
        can=["tell a genotype from a phenotype", "tell homozygous from heterozygous", "fill in a Punnett square for a cross"],
        plan=["Warm-up", "Genotypes", "Phenotypes", "From genotype to phenotype", "Homozygous and heterozygous", "Punnett squares",
              "Practice", "Exit ticket"],
        sections=[
            dict(nb="Warm-up", nbnote="Dominant and recessive letters.", label="WARM-UP", who="ON YOUR OWN", minutes=3,
                 layout="warmup", title="Capital or lowercase?",
                 body=["Recall Day 3."],
                 frame=[f"A dominant allele is written with a {B} letter. A recessive allele is written with a {B} letter."],
                 bank=["capital", "lowercase"], teacher="Key: capital; lowercase."),
            dict(nb="Genotype and phenotype", nbnote="Guided notes: what a genotype is.", label="NOTES", who="ON YOUR OWN", minutes=2,
                 title="Genotypes", big="BB    Bb    bb",
                 note="Note: always write the dominant (capital) letter first when writing genotypes.", body=[],
                 frame=[f"The genotype is the {B} makeup of an individual. In other words, it is the pair of {B} an individual "
                        "inherits from their parents."],
                 bank=["genetic", "alleles"],
                 teacher="Key: genetic; alleles. From slides 15 and 16 of the Genetics Notes deck (same wording and the BB, Bb, bb "
                         "examples)."),
            dict(nb="Genotype and phenotype", nbnote="Guided notes and two eyes to color.", label="NOTES", who="ON YOUR OWN", minutes=3,
                 title="Phenotypes",
                 img=dict(ids=["g1ebb2efc9c9_2_277", "g1ebb2efc9c9_2_278"], x=1.9, y=3.0, w=6.2), body=[],
                 frame=[f"The phenotype is the observable {B} or characteristics determined by the genotype. For example, {B} is "
                        "a phenotype."],
                 bank=["traits", "eye color"],
                 teacher="Key: traits; eye color. Students color the two eyes in their notebook (blue and brown). From slides 17 "
                         "and 18 of the Genetics Notes deck (same eye graphics)."),
            dict(nb="Genotype and phenotype", nbnote="Table: genotype to phenotype.", label="NOTES", who="ON YOUR OWN", minutes=3,
                 title="From genotype to phenotype", table=PEAS,
                 body=["In pea plants, T (tall) is dominant to t (short). TT is done for you."],
                 frame=[f"Tt is {B} because T is dominant. tt is {B}."], bank=["tall", "short"],
                 teacher="Key: Tt tall; tt short. Frame: tall; short."),
            dict(nb="Homozygous and heterozygous", nbnote="Guided notes and six genotypes to color.", label="NOTES",
                 who="ON YOUR OWN", minutes=4, title="Homozygous and heterozygous",
                 img=dict(ids=["g1ebb2efc9c9_2_289"], x=1.5, y=3.95, w=7.0),
                 body=["Genotypes can be homozygous or heterozygous.",
                       "In your notebook, color the homozygous genotypes green and the heterozygous genotypes orange."],
                 frame=[f"If the individual inherits two of the {B} allele, it is {B} (or purebred). If it inherits two {B} "
                        f"alleles, it is {B} (or hybrid)."],
                 bank=["same", "homozygous", "different", "heterozygous"],
                 teacher="Key: same; homozygous; different; heterozygous. Green (homozygous): CC, dd, AA. Orange (heterozygous): "
                         "Ee, Gg, Hh. From slide 19 of the Genetics Notes deck (same six genotypes)."),
            dict(nb="Punnett squares", nbnote="Copy the steps and the worked example.", label="MINI-LESSON", who="WHOLE CLASS",
                 minutes=8, title="Punnett squares", table=PUNNETT_TT,
                 body=["A Punnett square shows every possible combination of alleles from two parents.",
                       "1. Write one parent's two alleles across the top. 2. Write the other parent's down the side. "
                       "3. Fill each box with the allele from its column and the allele from its row.",
                       "Worked example: Tt × Tt gives TT, Tt, Tt, tt. That is 3 tall to 1 short."],
                 frame=[f"Each box in a Punnett square shows one possible {B} of alleles."], bank=["combination"],
                 teacher="Draw the square on the board while students copy it. Key: combination. Tell them: the letters on the "
                         "top and side are the alleles in each parent's sex cells (Day 6 explains why)."),
            dict(nb="Practice", nbnote="Two crosses of your own.", label="PRACTICE", who="WITH A PARTNER", minutes=6,
                 title="Try two crosses",
                 body=["Cross 1: Tt × tt.    Cross 2: TT × Tt."],
                 frame=[f"Cross 1: {B} of the 4 boxes are tall and {B} are short.", f"Cross 2: {B} of the 4 boxes are tall."],
                 bank=["2", "4"], bank_note="(use a number more than once)",
                 teacher="Key: Cross 1: Tt, Tt, tt, tt: 2 tall, 2 short. Cross 2: TT, TT, Tt, Tt: 4 tall."),
            dict(nb="Exit ticket", nbnote="One more cross.", label="EXIT TICKET", who="ON YOUR OWN", minutes=3,
                 title="How many are short?", body=["Tt × Tt."],
                 frame=[f"In a Tt × Tt cross, {B} out of 4 boxes show a short plant (tt)."], bank=["1", "2", "3"],
                 teacher="Key: 1."),
        ],
        key=["Warm-up: capital; lowercase.", "Genotypes: genetic; alleles.", "Phenotypes: traits; eye color.",
             "Pea plants: Tt tall, tt short; tall; short.",
             "Zygosity: same; homozygous; different; heterozygous. Green CC, dd, AA; orange Ee, Gg, Hh.", "Punnett: combination.",
             "Practice: 2, 2, 4.", "Exit ticket: 1."],
        notes=["Planner: Fri Nov 13, Finish Genetics Notes. Covers the second half of the notes (genotype, phenotype, homozygous, "
               "heterozygous) and adds the Punnett square mini-lesson that Monster Genetics needs.",
               "No CFA today. Supporting standard, not on the CSA."],
    ),
    dict(
        day=5, date="Mon Nov 16", kind="lesson", title="Monster Genetics, Part 1: Flip a Coin, Build a Monster",
        targets=["LS3-3.1"], cfa=None, focus="How can two coin flips build a monster's genotype?",
        ready="Have ready: your notebook, a pencil, a coin, and the Monster Genetics sheet",
        can=["use coin flips to model the two alleles an offspring inherits", "write a genotype and its phenotype",
             "fill in a missing genotype or phenotype"],
        plan=["Warm-up", "How the lab works", "Build the female monster", "Fill in the male monster", "Compare",
              "Exit ticket"],
        sections=[
            dict(nb="Warm-up", nbnote="Which allele does a sex cell get?", label="WARM-UP", who="ON YOUR OWN", minutes=3,
                 layout="warmup", title="One parent, one allele",
                 body=["A parent has the alleles Bb. A sex cell gets only one of them. Today a coin flip stands for which allele "
                       "gets passed on."],
                 frame=[f"Each sex cell gets {B} allele. A coin flip can choose between B and {B}."], bank=["one", "b"],
                 teacher="Key: one; b."),
            dict(nb="How the lab works", nbnote="Copy the rule and the worked example.", label="MINI-LESSON", who="WHOLE CLASS",
                 minutes=4, title="Part 1: how the lab works", table=MONSTER,
                 body=["Flip a coin twice for each trait. Heads = Allele 1 (capital letter). Tails = Allele 2 (lowercase).",
                       "Worked example, Eyes: heads, tails gives Ee. E is dominant, so the monster has two small eyes."],
                 teacher="Do two flips together on the board. Remind: one capital letter is enough to show the dominant trait."),
            dict(nb="Build the female monster", nbnote="Table 1 on your Monster Genetics sheet.", label="LAB", who="WITH A PARTNER",
                 minutes=12, title="Part 1: build the female monster",
                 body=["Fill in Table 1 on your Monster Genetics sheet for all 12 traits: flip twice, write the genotype, then "
                       "write the phenotype.",
                       "One partner flips and the other records. Switch after 6 traits."],
                 teacher="Sheet: \"Corrected_Monster Genetics (Mendellian genetics only)\" (the Nov 16 planner link). Circulate for "
                         "dominant and recessive mix-ups."),
            dict(nb="Fill in the male monster", nbnote="Table 2: finish the male monster.", label="LAB", who="WITH A PARTNER",
                 minutes=8, title="Part 2: fill in the male monster", table=MALE,
                 body=["Use the dominant rule to finish Table 2 for all 12 traits. Example: Gg is green, because G is dominant. "
                       "Straight tail is cc, because straight is recessive."],
                 teacher="Key (all 12): ee one large eye; rr white; Gg green; cc straight; Pp purple; TT has a tail; ss round "
                         "teeth; Ff four toes; ww white horn; YY pointy ears; nn two ears; Ll long claws."),
            dict(nb="Compare", nbnote="Compare monsters and predict.", label="COMPARE", who="WITH A PARTNER", minutes=5,
                 title="Why are our monsters different?",
                 body=["Compare your female monster with your partner's. Both came from coin flips.",
                       "Predict: when she mates with the male, what is the chance their baby has one large eye? Write your guess. "
                       "We check it tomorrow."],
                 frame=[f"Our monsters are different because the flips gave different {B} of alleles."], bank=["combinations"],
                 teacher="Key: combinations. Do not teach the percent yet."),
            dict(nb="Exit ticket", nbnote="What did the coin flip stand for?", label="EXIT TICKET", who="ON YOUR OWN", minutes=3,
                 title="What did a coin flip stand for?", body=["Finish both sentences."],
                 frame=[f"Each coin flip stood for the {B} a sex cell passes on. Two flips gave the monster's {B}."],
                 bank=["allele", "genotype"], teacher="Key: allele; genotype."),
        ],
        key=["Warm-up: one; b.", "How the lab works: Eyes Ee, two small eyes.",
             "Table 1: any genotypes; each phenotype must match the dominant rule (check 3 rows).",
             "Table 2: ee one large eye; rr white; Gg green; cc straight; Pp purple; TT has a tail; ss round; Ff four toes; ww white; "
             "YY pointy; nn two ears; Ll long.", "Compare: combinations.", "Exit ticket: allele; genotype."],
        notes=["Planner: Mon Nov 16, Monster Genetics. Parts 1 and 2 of the sheet today; Part 3 (Punnett squares) tomorrow.",
               "Tail color and tail shape only show if the monster has a tail (T). Point this out if a student's female has tt.",
               "No CFA today. Supporting standard, not on the CSA."],
    ),
    dict(
        day=6, date="Tue Nov 17", kind="lesson", title="Monster Genetics, Part 2: Predict the Baby",
        targets=["LS3-2.2", "LS3-3.2"], cfa="LS3-2.2",
        focus="How do sex cells and fertilization mix alleles, and how can we predict the baby?",
        ready="Have ready: your notebook, a pencil, a coin, and the Monster Genetics sheet",
        can=["describe how sex cells and fertilization mix alleles", "use Punnett squares to find the chance of each trait",
             "compare a prediction with real counts"],
        plan=["Warm-up", "Sex cells and fertilization", "Punnett squares for the baby", "Percent chance", "Class data",
              "CFA LS3-2.2"],
        sections=[
            dict(nb="Warm-up", nbnote="What a Gg parent passes on.", label="WARM-UP", who="ON YOUR OWN", minutes=3,
                 layout="warmup", title="One parent, two kinds of sex cells",
                 body=["A parent has the genotype Gg. Her body cells carry two alleles. Her sex cells carry only one."],
                 frame=[f"A Gg parent makes sex cells with {B} or {B}."], bank=["G", "g"], teacher="Key: G; g (either order)."),
            dict(nb="Sex cells and fertilization", nbnote="Copy the key ideas and finish the frame.", label="MINI-LESSON",
                 who="WHOLE CLASS", minutes=5, title="Sex cells and fertilization",
                 body=["Body cells have two alleles of each gene.",
                       "Meiosis is the cell division that makes sex cells (eggs and sperm). Each sex cell gets only one allele "
                       "of each gene, chosen at random, like a coin flip.",
                       "At fertilization, a sperm and an egg join. The offspring gets one allele from each parent: a new combination."],
                 frame=[f"Each sex cell carries {B} allele of each gene. Fertilization joins two {B} to make a new {B} of alleles."],
                 bank=["one", "sex cells", "combination"],
                 teacher="Key: one; sex cells; combination. No phases of meiosis. Link to yesterday: a coin flip was a sex cell's allele."),
            dict(nb="Punnett squares for the baby", nbnote="Six Punnett squares on your sheet.", label="LAB", who="WITH A PARTNER",
                 minutes=10, title="Part 3: Punnett squares for the baby monster", table=PUNNETT_GG,
                 body=["Make a Punnett square for 6 traits: Eyes, Skin color, Teeth, Feet, Horn color, and Claws. Use your "
                       "female's genotype (Table 1) and the male's (Table 2).",
                       "Worked example together: Skin color, female Gg × male Gg."],
                 frame=[f"The letters on the top and side of a square are the {B} in each parent's sex cells."], bank=["alleles"],
                 teacher="Required: Eyes (ee), Skin color (Gg), Teeth (ss), Feet (Ff), Horn color (ww), Claws (Ll). The other 6 "
                         "squares are \"if time.\" Key: alleles."),
            dict(nb="Percent chance", nbnote="Percent chance for your six traits.", label="PERCENT CHANCE", who="ON YOUR OWN",
                 minutes=5, title="From boxes to percent",
                 body=["Each box is 1 of 4, or 25%.",
                       "Worked example: Gg × Gg gives GG, Gg, Gg, gg. Three of 4 boxes are green and 1 is blue.",
                       "Fill in the percent-chance table on your sheet for your 6 traits."],
                 frame=[f"In a Gg × Gg cross, {B}% of the boxes are green and {B}% are blue."], bank=["75", "25"],
                 teacher="Key: 75; 25. Eyes (male ee): a female EE gives 0% one large eye, Ee gives 50%, and ee gives 100%. Check a few."),
            dict(nb="Class data", nbnote="Compare the prediction with the class count.", label="REAL COUNTS", who="WHOLE CLASS",
                 minutes=6, title="Real counts: Gg × Gg", table=CLASS_COUNTS,
                 body=["Everyone makes one baby: flip a coin for Mom (heads = G, tails = g) and a coin for Dad. Add your baby "
                       "to the class tally. The table shows a sample class."],
                 frame=[f"The Punnett square predicted {B}% green. The class got about {B}% green. The numbers are close but "
                        f"not exact because every flip is {B}."],
                 bank=["75", "73", "random"],
                 teacher="Replace the sample with your class's tally (the sample is 22 green and 8 blue out of 30). Key: 75; "
                         "73 (or your class's number); random. Real counts rarely match the prediction exactly."),
        ],
        key=["Warm-up: G; g.", "Sex cells: one; sex cells; combination.",
             "Punnett squares: use the male's genotypes. Gg × Gg: GG, Gg, Gg, gg. alleles.",
             "Percent chance: 75; 25.", "Class data: 75; 73; random."],
        notes=["Planner: Tue Nov 17, Finish Monster Genetics. Part 3 is trimmed to 6 required squares (the sheet has 12), so the "
               "lesson fits with a mini-lesson, class data, and the CFA.",
               "CFA LS3-2.2 closes the lesson. LS3-3.2 (chances and real counts) is taught here and is not assessed.",
               "Below 4 of 5 on the CFA opens the review."],
    ),
    dict(
        day=7, date="Wed Nov 18", kind="lesson", title="When Copying Goes Wrong", targets=["LS3-2.3"], cfa="LS3-2.3",
        focus="How do copying errors and UV light change genes, and when are the changes inherited?",
        ready="Have ready: your notebook and a pencil",
        can=["explain how copying errors and UV light can change DNA", "read data showing UV light causes more mutations",
             "decide when a mutation is passed on to the next generation"],
        plan=["Warm-up", "How do mutations happen?", "UV and mutations", "Who passes it on?", "Explain it", "CFA LS3-2.3"],
        sections=[
            dict(nb="Warm-up", nbnote="Finish two sentences about mutations.", label="WARM-UP", who="ON YOUR OWN", minutes=3,
                 layout="warmup", title="Back to one letter",
                 body=["In Unit 2.1, one DNA letter changed (GAG to GTG) and one amino acid changed (Glu to Val)."],
                 frame=[f"A mutation is a {B} in the DNA sequence. A mutation can change an {B} in a protein."],
                 bank=["change", "amino acid"], teacher="Key: change; amino acid."),
            dict(nb="How do mutations happen?", nbnote="Copy the key ideas and finish the frame.", label="MINI-LESSON",
                 who="WHOLE CLASS", minutes=6, title="How do mutations happen?",
                 body=["Before a cell divides, it copies all its DNA: about 6 billion letters in a human cell.",
                       "Cells proofread, so most copying errors are fixed. A rare error that stays is a mutation.",
                       "The environment causes mutations too. UV light, X-rays, and some chemicals damage DNA.",
                       "A mutation the organism survives is viable. It can become a new variation."],
                 frame=[f"A {B} error that is not fixed becomes a mutation. UV light and some {B} can also damage DNA."],
                 bank=["copying", "chemicals"], teacher="Key: copying; chemicals."),
            dict(nb="UV and mutations", nbnote="Table: UV light and mutations.", label="EVIDENCE", who="WITH A PARTNER",
                 minutes=5, title="UV light and mutations", table=UV,
                 body=["Worked example: with 0 hours of UV, there are 2 mutations per 1,000 skin cells. Those come from copying "
                       "errors."],
                 frame=[f"With more UV light, there are {B} mutations. The 2 mutations with no UV came from {B} errors."],
                 bank=["more", "copying"], teacher="Key: more; copying. The table is a class data set modeled on real experiments."),
            dict(nb="Who passes it on?", nbnote="Table: five cases.", label="SORT", who="WITH A PARTNER", minutes=9,
                 title="Who passes it on?", table=CASES,
                 body=["Could the next generation inherit each change? Case A is done for you."],
                 frame=[f"Why: a change in a {B} cell is not passed on. A change in a cell that makes {B} can be."],
                 bank=["body", "eggs or sperm"],
                 teacher="Key: A No; B Yes; C No; D Yes; E No. In animals, only changes in cells that make eggs or sperm are inherited."),
            dict(nb="Explain it", nbnote="Two sentences.", label="EXPLAIN IT", who="ON YOUR OWN", minutes=4,
                 title="How can UV light change a gene?", body=["Finish both sentences."],
                 frame=[f"UV light can change a gene by {B} its DNA.", f"The change is inherited only if it happens in a cell that makes {B}."],
                 bank=["damaging", "eggs or sperm"], teacher="Key: damaging; eggs or sperm."),
        ],
        key=["Warm-up: change; amino acid.", "Mini-lesson: copying; chemicals.", "UV: more; copying.",
             "Cases: A No; B Yes; C No; D Yes; E No.", "Explain it: damaging; eggs or sperm."],
        notes=["Connects to Unit 2.1 (LS1-1.3, a one-letter change). The boundary applies: no biochemical mechanism of specific "
               "steps, so do not teach the enzymes of copying or repair.",
               "In humans and other animals, a mutation is inherited only if it is in a cell that makes eggs or sperm. A sunburn "
               "mutation in skin is not passed on.",
               "CFA LS3-2.3 closes the lesson. Below 4 of 5 opens the review."],
    ),
    dict(
        day=8, date="Thu Nov 19", kind="lesson", title="Where Did This Variation Come From?", targets=["LS3-2.4"], cfa="LS3-2.4",
        focus="How can data show where a genetic variation came from?",
        ready="Have ready: your notebook and a pencil",
        can=["list a clue in the data for each source of variation", "read family and experiment data",
             "write a claim backed by evidence and reasoning"],
        plan=["Clues for each source", "Case 1: the puppy litter", "Case 2: a new base", "Case 3: X-rays and mice",
              "Write your claim", "CFA LS3-2.4"],
        sections=[
            dict(nb="Clues for each source", nbnote="Three clue sentences.", label="WARM-UP", who="ON YOUR OWN", minutes=5,
                 title="Clues in the data",
                 body=["Use these clues all lesson: what does the data look like for each source?"],
                 frame=[f"New combination: every allele in the offspring was {B} in a parent.",
                        f"Copying error: a {B} allele that neither parent has, and no extra exposure.",
                        f"Environmental mutation: {B} mutations in the group that was exposed."],
                 bank=["already", "new", "more"],
                 teacher="Key: already; new; more. Keep this table up while students work the cases."),
            dict(nb="Case 1: the puppy litter", nbnote="Worked example with claim, evidence, reasoning.", label="WORKED EXAMPLE",
                 who="WHOLE CLASS", minutes=5, title="Case 1: the puppy litter", table=LITTER_ALLELES,
                 body=["Claim: These puppies came from a new combination of alleles.",
                       "Evidence: Both parents are Bb. The brown puppies are bb, so each got a b from each parent.",
                       "Reasoning: No new allele appeared. The puppies have only alleles the parents already had, in new pairs."],
                 teacher="Read it aloud and point at each piece of data."),
            dict(nb="Case 2: a new base", nbnote="Table and two sentences.", label="CASE 2", who="WITH A PARTNER", minutes=6,
                 title="Case 2: a new base", table=DNA_FAMILY,
                 body=["The table shows a coat-color gene. Each puppy gets one allele from each parent."],
                 frame=[f"The puppy's CCT allele is {B} because neither parent has it. The most likely source is a {B}, not a new "
                        "combination."],
                 bank=["new", "mutation"],
                 teacher="Key: new; mutation. This data cannot separate a copying error from an environmental mutation. Ask what "
                         "data would (Case 3)."),
            dict(nb="Case 3: X-rays and mice", nbnote="Table and two sentences.", label="CASE 3", who="WITH A PARTNER", minutes=6,
                 title="Case 3: X-rays and mice", table=XRAY,
                 body=["Scientists exposed mice to X-rays and counted new mutations in sperm cells."],
                 frame=[f"The group with a high X-ray dose had {B} mutations. The group with no X-rays had {B}.",
                        f"The extra mutations came from {B}."],
                 bank=["25", "3", "the X-rays"],
                 teacher="Key: 25; 3; the X-rays (an environmental mutation). The 3 per 1,000 baseline is copying errors."),
            dict(nb="Write your claim", nbnote="Claim, evidence, reasoning.", label="CER", who="ON YOUR OWN", minutes=5,
                 title="Write your claim for Case 3",
                 body=["Use the table from Case 3."],
                 frame=[f"Claim: The extra mutations came from {B}.",
                        f"Evidence: The high-dose group had {B} mutations per 1,000 sperm cells, but the group with no X-rays had {B}.",
                        f"Reasoning: If copying errors alone caused every mutation, the groups would have {B} numbers."],
                 bank=["an environmental mutation", "25", "3", "similar"],
                 teacher="Key: an environmental mutation; 25; 3; similar. Collect two samples."),
        ],
        key=["Clues: already; new; more.", "Case 1: read aloud.", "Case 2: new; mutation.", "Case 3: 25; 3; the X-rays.",
             "CER: an environmental mutation; 25; 3; similar."],
        notes=["LS3-2.4 asks students to read data and make a claim supported by that data. Claim, evidence, and reasoning are the "
               "frame used in Unit 1.3.",
               "The data are classroom models patterned on real experiments (mutation rates rise with radiation dose).",
               "CFA LS3-2.4 closes the lesson. Below 4 of 5 opens the review."],
    ),
    dict(
        day=9, date="Fri Nov 20 (2-hour early out)", kind="review", title="Catch-Up Day: Reviews and Make-Up Work",
        targets=["LS3-2.1", "LS3-2.2", "LS3-2.3", "LS3-2.4"], cfa=None,
        focus="What do I still need to work on before the next lesson?",
        ready="Have ready: your notebook, a pencil, and a Chromebook",
        can=["check my CFA scores", "make up missing work and start my CFA reviews",
             "see how the environment can change how a trait shows up"],
        plan=["Check my CFAs", "Reviews and make-up work", "Enrichment: environment and traits", "Self-check"],
        sections=[
            dict(nb="Check my CFAs", nbnote="Four CFA scores.", label="CHECK-IN", who="EVERYONE", minutes=3,
                 title="Check your CFA scores",
                 body=["Open Canvas and look at your CFA scores for LS3-2.1, LS3-2.2, LS3-2.3, and LS3-2.4.",
                       "Below a B (fewer than 4 of 5)? A review for that target opened for you."],
                 teacher="Everyone does this first."),
            dict(nb="Reviews and make-up work", nbnote="Your to-do list.", label="WORK TIME", who="ON YOUR OWN + SMALL GROUPS",
                 minutes=13, title="Make up missing work, then do reviews",
                 body=["In this order: 1. Missing work: any missing CFA and unfinished Monster Genetics pages. 2. Your CFA "
                       "reviews, lowest target first, if you have time. You will have more review time on Monday.",
                       "Your teacher will pull small groups."],
                 teacher="Shortened periods today (30 minutes). The point is catching up on work. Reviews are fine if a student has "
                         "time, but the main review block is Monday (Day 10). Students with nothing to do go to the enrichment."),
            dict(nb="Enrichment: environment and traits", nbnote="Table and two sentences.", label="ENRICHMENT",
                 who="NO REVIEWS, OR ALL DONE", minutes=8, title="The same DNA, different colors", table=HYDRANGEA,
                 body=["A gardener grew copies of one hydrangea plant (the same DNA) in soils of different pH.",
                       "In a garden of 100 plants from one parent, the soil varies: 42 plants are blue, 33 purple, and 25 pink."],
                 frame=[f"The plants have the same {B}. Flower color varied because the {B} changed how the gene works."],
                 bank=["DNA", "soil"],
                 teacher="LS3-3.3, supporting (not on the CSA). Key: DNA; soil. The environment changed how the trait showed up, "
                         "not the DNA, so the color is not inherited. This is idea 3 from Day 1."),
            dict(nb="Self-check", nbnote="Rate yourself 1 to 4.", label="SELF-CHECK", who="EVERYONE", minutes=3,
                 title="Rate yourself on each target",
                 body=["Rate each target 1 to 4 in your notebook (4 = I could teach it).",
                       "LS3-2.1 three sources · LS3-2.2 sex cells and fertilization · LS3-2.3 copying errors and UV · LS3-2.4 "
                       "read data and make a claim",
                       "Monday (Nov 30): reviews and the wrap-up of the puppy puzzle. Then the CSA on Dec 1."],
                 teacher="Collect the ratings to choose small groups for the Monday review block (Nov 30)."),
        ],
        key=["Enrichment: DNA; soil."],
        notes=["Planner: Fri Nov 20 is a 2-hour early out (30-minute classes) and a Catch Up Day. Use it to get caught up on missing "
               "work. CFA reviews (Mastery Paths) for LS3-2.1 to 2.4 can start here, but the main review block is Monday, Nov 30 "
               "(Day 10).",
               "There is no new CFA. LS3-3.3 is the supporting standard for the enrichment; it is not on the CSA."],
    ),
    dict(
        day=10, date="Mon Nov 30", kind="lesson", title="Defend Your Claim and Back to the Puppies", targets=["LS3-2.5"],
        cfa="LS3-2.5", focus="How do I defend my claim against another explanation?",
        ready="Have ready: your notebook (with your Day 1 model), a pencil, and a Chromebook",
        can=["defend a claim against another explanation using data", "fix my Day 1 model with all three sources of variation",
             "explain the puppy puzzle with evidence"],
        plan=["Reviews and make-up work", "How to defend a claim", "The new coat pattern", "Fix my Day 1 model",
              "Write It: the puppy puzzle", "CFA LS3-2.5"],
        sections=[
            dict(nb="Reviews and make-up work", nbnote="Your to-do list.", label="WORK TIME", who="ON YOUR OWN + SMALL GROUPS",
                 minutes=18, title="Do your reviews",
                 body=["Open Canvas. In this order: 1. Any CFA review that opened for you, lowest target first (LS3-2.1 to "
                       "LS3-2.4). 2. Any missing CFA or Monster Genetics pages.",
                       "The CSA is tomorrow, and a review is the best way to get ready for it. Stop at the end of the work time: "
                       "the puppy puzzle wrap-up starts next."],
                 teacher="This is the main review block (Day 9 was a short catch-up day). Pull small groups by lowest target. Call "
                         "time at 18 minutes."),
            dict(nb="How to defend a claim", nbnote="Three steps and a worked example.", label="MINI-LESSON", who="WHOLE CLASS",
                 minutes=3, title="How to defend a claim",
                 body=["A counterclaim is another explanation. To defend your claim: 1. Restate it. 2. Cite the data that "
                       "supports it. 3. Show why the other explanation does not fit the data.",
                       "Worked example (Day 8, Case 3): Claim: X-rays caused the extra mutations. Counterclaim: copying errors "
                       "caused them. Defense: copying errors happen in every group, and the no-X-ray group had only 3 while the "
                       "high-dose group had 25, so copying errors cannot explain the extra 22."],
                 frame=[f"A counterclaim is {B} explanation. To defend my claim I show why the {B} does not fit the data."],
                 bank=["another", "counterclaim"], teacher="Key: another; counterclaim."),
            dict(nb="The new coat pattern", nbnote="Table and a defense.", label="CASE", who="WITH A PARTNER", minutes=3,
                 title="The new coat pattern", table=KENNELS,
                 body=["Claim: A chemical in Kennel A's water caused the new coat patterns.",
                       "Counterclaim: \"New patterns are just copying errors. Copying errors happen in every dog.\""],
                 frame=[f"Evidence: Kennel A had {B} new patterns per 1,000 puppies. Kennel B had {B}.",
                        f"Defense: Copying errors happen in {B} kennels, so they cannot explain the {B} extra patterns."],
                 bank=["14", "3", "both", "11"],
                 teacher="Key: 14; 3; both; 11. Good defenses also say copying errors may explain Kennel B's 3, so both sources can "
                         "be at work (the standard says \"and/or\")."),
            dict(nb="Fix my Day 1 model", nbnote="Redraw with all three sources.", label="MYSTERY SOLVED", who="ON YOUR OWN",
                 minutes=3, title="Fix your Day 1 model",
                 body=["Redraw your Day 1 model. Check off each part as you add it:",
                       "☐ new combinations (sex cells and fertilization)  ☐ copying errors  ☐ mutations from the environment",
                       "☐ a note that only changes in eggs or sperm are inherited  ☐ the puppy traits"],
                 teacher="Walk the room with the checklist."),
            dict(nb="Write It: the puppy puzzle", nbnote="Claim, evidence, reasoning.", label="WRITE IT", who="ON YOUR OWN",
                 minutes=3, title="Why are the puppies alike but not identical?",
                 body=["Write one explanation for the puzzle."],
                 frame=[f"Claim: Puppies from the same parents are alike but not identical because of {B}.",
                        f"Evidence: In the card activity, each offspring got a different {B} of alleles.",
                        f"Reasoning: Sex cells and fertilization make new combinations. Copying errors and {B} can also change DNA, "
                        f"and a change is inherited only if it is in {B}."],
                 bank=["new combinations of alleles", "combination", "environmental mutations", "eggs or sperm"],
                 teacher="This is the unit's phenomenon explanation. Collect it."),
        ],
        key=["Defend: another; counterclaim.", "Coat pattern: 14; 3; both; 11.",
             "Fix my model: all three sources plus the sex-cell note.",
             "Write It: claim: new combinations of alleles (plus copying errors and mutations); evidence: combination; reasoning: "
             "combination; environmental mutations; eggs or sperm."],
        notes=["Monday is the main review block (Day 9, the early-out catch-up day, was short). The phenomenon wrap-up is kept short: 12 "
               "minutes of activities, then the 6-minute CFA LS3-2.5. Below 4 of 5 opens the review.",
               "The CSA is tomorrow (Dec 1). Tell students which CFA reviews to finish tonight."],
    ),
    dict(
        day=11, date="Tue Dec 1", kind="csa", title="Unit 2.2 CSA", targets=PRIORITY, cfa=None,
        focus="Show what you know: inherited instructions",
        ready="Have ready: a Chromebook and a pencil (scratch paper is fine)",
        can=["show what I know on all 5 priority targets", "read the data and tables in the questions",
             "write two explanations with evidence"],
        plan=["Log in and open the CSA", "Read each question carefully", "Use the tables in the questions",
              "Two written responses", "Check every answer", "Submit"],
        sections=[
            dict(nb=None, label="BEFORE YOU BEGIN", who="EVERYONE", minutes=0, title="Before you begin",
                 body=["Work alone. Put everything away except what your teacher allows.",
                       "Read each question carefully. Data tables are inside the questions that need them.",
                       "Part 1 is multiple choice, true or false, and select-all. Part 2 is two written responses: use claim, "
                       "evidence, and reasoning.",
                       "Answer every question; do not leave blanks."],
                 teacher="Read the slide aloud. Students open Canvas when you say go."),
            dict(nb=None, label="CSA", who="FULL PERIOD · ON YOUR OWN", minutes=40, title="Show what you know: Unit 2.2 CSA",
                 body=["Open Canvas: Unit 2.2 CSA: Inherited Instructions (HS-LS3-2).",
                       "13 questions on the 5 priority targets. Two are written responses your teacher grades.",
                       "Work on your own. Check every answer, then submit."],
                 teacher="Allow the full period."),
            dict(nb=None, label="REMINDERS", who="EVERYONE", minutes=0, title="Reminders",
                 body=["Do your best on every question.", "If you finish early, check your written responses.",
                       "Submit, then read quietly until the bell."],
                 teacher="Post this slide after students start."),
        ],
    ),
]
DAY = {d["day"]: d for d in DAYS}


def minutes(d):
    """Total student minutes, notebook setup (2) and the CFA (6) included."""
    if d["kind"] == "csa":
        return None
    m = 2 + sum(s["minutes"] + s.get("minutes_frame", 0) for s in d["sections"])
    return m + (6 if d["cfa"] else 0)


for _d in DAYS:
    _m = minutes(_d)
    for _s in _d["sections"]:
        _s["layout_kind"] = _s.get("layout") or ("table" if _s.get("table") else "list")
    if _d["kind"] == "lesson":
        assert 20 <= _m <= 40 and 5 <= len(_d["plan"]) <= 10, (_d["day"], _m, len(_d["plan"]))
    if _d["kind"] == "review":
        assert _m <= 40, _m
