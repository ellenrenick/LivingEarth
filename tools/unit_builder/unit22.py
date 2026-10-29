# -*- coding: utf-8 -*-
"""Unit 2.2 Inherited Instructions (HS-LS3-2): content for printables, notebook, key, teacher plans."""
from lib import *

T = {
    '2.1': 'LS3-2.1: I can name three ways new genetic variation arises.',
    '2.2': 'LS3-2.2: I can describe how making sex cells and fertilization mix alleles into new combinations.',
    '2.3': 'LS3-2.3: I can explain how copying errors and things like UV light change genes, and when that change is inherited.',
    '2.4': 'LS3-2.4: I can read data and make a claim, backed by that data, about what caused a genetic variation.',
    '2.5': 'LS3-2.5: I can defend my claim against another explanation using the evidence.',
    '3.1': 'LS3-3.1 (supporting): I can use a Punnett square to show the possible allele combinations from a cross.',
    '3.2': 'LS3-3.2 (supporting): I can calculate the chance of each trait and compare it with real counts.',
}
ILLUS = 'Illustrative data: simplified numbers made up for class, not from a study.'


def tb(header, rows, cols=None, rowh=None):
    return ('table', {'header': header, 'rows': rows, 'cols': cols, 'rowh': rowh})


def item(lesson, title, kicker, use, copies, body, key):
    return dict(lesson=lesson, title=title, kicker=kicker, use=use, copies=copies, body=body, key=key)


items = []

# ---------- Lesson 1 ----------
items.append(item(1, 'Puppy litter data', 'Compare the traits', 'Glue under "Compare the traits" in the notebook', 'One per student',
    [('p', 'Two parents had four puppies. Look at the traits. Circle every trait a puppy shares with Mom. Underline every trait a puppy shares with Dad.'),
     tb(['', 'Fur color', 'Ear shape', 'Pattern'],
        [['Mom', 'Black', 'Floppy', 'Spotted'], ['Dad', 'Brown', 'Pointed', 'Solid'],
         ['Puppy A', 'Black', 'Floppy', 'Solid'], ['Puppy B', 'Brown', 'Floppy', 'Spotted'],
         ['Puppy C', 'Black', 'Pointed', 'Spotted'], ['Puppy D', 'Brown', 'Floppy', 'Solid']], [1.2, 1.6, 1.6, 1.6]),
     ('h', 'Finish the sentences'),
     ('p', 'Every puppy has some traits like Mom and some like ______________.'),
     ('p', 'No two puppies have the same ______________ of traits.'),
     ('p', 'Word bank: combination · Dad'),
     ('note', ILLUS)],
    [('p', 'Puppy A: black and floppy are like Mom; solid is like Dad. Puppy B: floppy and spotted are like Mom; brown is like Dad. Puppy C: black and spotted are like Mom; pointed is like Dad. Puppy D: floppy is like Mom; brown and solid are like Dad.'),
     ('p', 'Every puppy has some traits like Mom and some like <b>Dad</b>. No two puppies have the same <b>combination</b> of traits (all four rows differ).')]))

# ---------- Lesson 2 ----------
items.append(item(2, 'Allele cards: Parent 1 and Parent 2', 'Make possible offspring', 'Cut apart; each group sorts the cards into 6 piles', 'One per group of 3 to 4',
    [('p', 'Each parent has two versions of each of 3 genes. Cut out all 12 cards. Sort them into 6 piles: Parent 1 fur color, Parent 1 ear shape, Parent 1 pattern, and the same 3 for Parent 2. Shuffle each pile. Take one card from every pile to make one offspring. Record it, put the cards back, and repeat.'),
     ('h', 'Parent 1'),
     ('cards', ['P1 · Fur color: Black', 'P1 · Fur color: Brown', 'P1 · Ear shape: Floppy', 'P1 · Ear shape: Pointed', 'P1 · Pattern: Solid', 'P1 · Pattern: Spotted'], 3, 0.78),
     ('h', 'Parent 2'),
     ('cards', ['P2 · Fur color: Black', 'P2 · Fur color: Brown', 'P2 · Ear shape: Floppy', 'P2 · Ear shape: Pointed', 'P2 · Pattern: Solid', 'P2 · Pattern: Spotted'], 3, 0.78),
     ('note', 'The cards model sex cells: each parent passes on one version of each gene. ' + ILLUS)],
    [('p', 'There is no single correct card draw. Any draw that takes exactly one card from each of the 6 piles is correct. The 6 piles: P1 fur, P1 ears, P1 pattern, P2 fur, P2 ears, P2 pattern. Each pile has 2 cards.')]))
items.append(item(2, 'Card table: 3 offspring', 'Make possible offspring', 'Glue under "Make possible offspring" in the notebook', 'One per student',
    [('p', 'Offspring 1 is done for you. Make Offspring 2 and 3 with the cards. Write the card you drew from each pile.'),
     tb(['Offspring', 'Fur: from P1', 'Fur: from P2', 'Ears: from P1', 'Ears: from P2', 'Pattern: from P1', 'Pattern: from P2'],
        [['1', 'Black', 'Brown', 'Floppy', 'Pointed', 'Solid', 'Solid'], ['2', '', '', '', '', '', ''], ['3', '', '', '', '', '', '']],
        [1, 1.1, 1.1, 1.1, 1.1, 1.2, 1.2], rowh=0.55),
     ('h', 'Which offspring look alike? Explain in one sentence.'), ('lines', 3)],
    [('p', 'Offspring 2 and 3 vary by draw. Check that each has one card from each of the 6 piles and that the two offspring are not identical. If a group draws two identical offspring, have them draw again: it is possible, but unlikely.'),
     ('p', 'Sample sentence: Offspring 2 and 3 are different because each got a different combination of cards.')]))

# ---------- Lesson 4 ----------
items.append(item(4, 'Genotype to phenotype: pea plants', 'Genotype and phenotype', 'Glue under "Genotype and phenotype" in the notebook', 'One per student',
    [('p', 'In pea plants, T (tall) is dominant to t (short). TT is done for you. Fill in the table.'),
     tb(['Genotype', 'Phenotype (what it looks like)', 'Homozygous or heterozygous?'],
        [['TT', 'Tall', 'Homozygous'], ['Tt', '', ''], ['tt', '', '']], [1, 2, 2], rowh=0.45),
     ('p', 'Tt is ______________ because T is dominant. tt is ______________.'),
     ('p', 'Word bank: short · tall'),
     ('h', 'Practice: write the genotype'),
     tb(['Description', 'Genotype'],
        [['Two copies of the dominant allele', ''], ['One dominant and one recessive allele', ''], ['Short plant', '']], [3, 2], rowh=0.4),
     ('note', 'Pea plant height is the classic Mendel trait (Gregor Mendel, 1866).')],
    [tb(['Genotype', 'Phenotype', 'Homozygous or heterozygous?'], [['TT', 'Tall', 'Homozygous'], ['Tt', 'Tall', 'Heterozygous'], ['tt', 'Short', 'Homozygous']], [1, 2, 2]),
     ('p', 'Tt is <b>tall</b> because T is dominant. tt is <b>short</b>.'),
     ('p', 'Practice: TT; Tt; tt.')]))
items.append(item(4, 'Punnett squares: steps and worked example', 'Punnett squares', 'Glue under "Punnett squares" in the notebook', 'One per student',
    [('h', 'Steps'),
     ('p', '1. Write one parent\'s two alleles across the top.   2. Write the other parent\'s two alleles down the side.   3. Fill each box with the allele from its column and the allele from its row.'),
     ('h', 'Worked example: Tt × Tt'),
     ('punnett', {'title': 'Tt × Tt', 'top': ['T', 't'], 'side': ['T', 't'], 'cells': [['TT', 'Tt'], ['Tt', 'tt']]}),
     ('p', 'Results: TT, Tt, Tt, tt. That is 3 tall to 1 short.'),
     ('h', 'Your turn'),
     ('punnett', {'title': 'Tt × tt', 'top': ['T', 't'], 'side': ['t', 't']}),
     ('punnett', {'title': 'TT × Tt', 'top': ['T', 'T'], 'side': ['T', 't']}),
     ('p', 'Each box in a Punnett square shows one possible ______________ of alleles.   Word bank: combination')],
    [('punnett', {'title': 'Tt × tt', 'top': ['T', 't'], 'side': ['t', 't'], 'cells': [['Tt', 'tt'], ['Tt', 'tt']]}),
     ('punnett', {'title': 'TT × Tt', 'top': ['T', 'T'], 'side': ['T', 't'], 'cells': [['TT', 'TT'], ['Tt', 'Tt']]}),
     ('p', 'Tt × tt: 2 of 4 tall, 2 of 4 short. TT × Tt: 4 of 4 tall (2 TT, 2 Tt). Each box shows one possible <b>combination</b> of alleles.')]))

# ---------- Lesson 5 ----------
MON = [('Eyes', 'E', 'two small eyes', 'e', 'one large eye'), ('Skin color', 'G', 'green', 'g', 'blue'),
       ('Teeth', 'T', 'pointed', 't', 'flat'), ('Feet', 'F', 'webbed', 'f', 'round'),
       ('Horn color', 'H', 'red', 'h', 'yellow'), ('Claws', 'K', 'long', 'k', 'short'),
       ('Tail', 'C', 'curly', 'c', 'straight'), ('Ears', 'A', 'round', 'a', 'pointed'),
       ('Hair', 'P', 'hairy', 'p', 'bald'), ('Wings', 'W', 'wings', 'w', 'no wings'),
       ('Spots', 'S', 'spotted', 's', 'plain'), ('Body size', 'B', 'large', 'b', 'small')]
MALE = ['Ee', 'Gg', 'tt', 'Ff', 'hh', 'Kk', 'cc', 'AA', 'Pp', 'ww', 'Ss', 'bb']


def pheno(g, row):
    return row[2] if any(ch.isupper() for ch in g) else row[4]


items.append(item(5, 'Monster Genetics: the coin rule and Table 2', 'How the lab works', 'Glue under "How the lab works"; keep for Lesson 6', 'One per student',
    [('h', 'The coin rule'),
     ('p', 'Flip a coin twice for each trait. Heads = Allele 1 (the capital letter). Tails = Allele 2 (the lowercase letter). Two flips make the genotype. If there is at least one capital letter, the dominant trait shows.'),
     ('p', 'Worked example, Eyes: heads, tails gives Ee. E is dominant, so the monster has two small eyes.'),
     ('h', 'Table 2: the male monster (genotypes are given)'),
     tb(['Trait', 'Dominant (capital)', 'Recessive (lowercase)', 'Male genotype', 'Male phenotype'],
        [[r[0], '%s = %s' % (r[1], r[2]), '%s = %s' % (r[3], r[4]), MALE[i], ''] for i, r in enumerate(MON)], [1.2, 1.7, 1.7, 1.1, 1.5], rowh=0.3),
     ('note', 'Monster traits and rules are made up for class.')],
    [tb(['Trait', 'Male genotype', 'Male phenotype'], [[r[0], MALE[i], pheno(MALE[i], r)] for i, r in enumerate(MON)], [2, 1.5, 2])]))
items.append(item(5, 'Monster Genetics sheet: Table 1, the female monster', 'Build the female monster', 'Lab sheet for the coin-flip build', 'One per pair',
    [('p', 'One partner flips and the other records. Switch after 6 traits. Flip twice per trait, write the genotype, then write the phenotype using the dominant rule from your Table 2 key.'),
     tb(['Trait', 'Flip 1', 'Flip 2', 'Genotype', 'Phenotype'], [[r[0], '', '', '', ''] for r in MON], [1.5, 1, 1, 1.4, 2.2], rowh=0.3),
     ('p', 'Compare: our monster is different from our partner pair\'s because the flips gave different ______________ of alleles.   Word bank: combinations'),
     ('p', 'Predict: when she mates with the male, what is the chance their baby has one large eye? My guess: ______________')],
    [('p', 'Results vary by flips. Check each row: Heads+Heads = capital capital (e.g., EE); Heads+Tails or Tails+Heads = capital + lowercase, written capital first (Ee); Tails+Tails = lowercase lowercase (ee). Dominant phenotype shows if there is a capital letter.'),
     ('p', 'Prediction check: for Eyes, a female Ee × male Ee gives a 25% chance of ee (one large eye); a female EE gives 0%; a female ee × male Ee gives 50%. This is done in Lesson 6.')]))

# ---------- Lesson 6 ----------
items.append(item(6, 'Punnett square: skin color and eyes', 'Punnett squares for the baby', 'Glue under "Punnett squares for the baby"', 'One per student',
    [('h', 'Worked example together: Skin color, Gg × Gg'),
     ('punnett', {'title': 'Gg × Gg', 'top': ['G', 'g'], 'side': ['G', 'g'], 'cells': [['GG', 'Gg'], ['Gg', 'gg']]}),
     ('p', 'Each box is 1 of 4, or 25%. Gg × Gg gives GG, Gg, Gg, gg. Three of 4 boxes are green and 1 is blue.'),
     ('h', 'Now use your own monsters\' genotypes (Table 1 and Table 2). Eyes:'),
     ('punnett', {'title': 'Eyes: ____ × ____', 'top': ['', ''], 'side': ['', '']}),
     ('p', 'The letters on the top and side of a square are the ______________ in each parent\'s sex cells.   Word bank: alleles'),
     ('h', 'Percent chance table (6 traits)'),
     tb(['Trait', 'Female × Male', 'Boxes with the dominant trait', 'Percent chance (dominant)', 'Percent chance (recessive)'],
        [[t, '', '', '', ''] for t in ['Eyes', 'Skin color', 'Teeth', 'Feet', 'Horn color', 'Claws']], [1.2, 1.4, 1.8, 1.6, 1.6], rowh=0.3)],
    [('punnett', {'title': 'Gg × Gg', 'top': ['G', 'g'], 'side': ['G', 'g'], 'cells': [['GG', 'Gg'], ['Gg', 'gg']]}),
     ('p', 'The letters on the top and side are the <b>alleles</b> in each parent\'s sex cells. Gg × Gg: 75% green, 25% blue.'),
     ('p', 'Student squares depend on their coin flips. Check: each box = 25%; percent dominant = (boxes with a capital letter) × 25. Male genotypes for the six traits: Eyes Ee, Skin color Gg, Teeth tt, Feet Ff, Horn color hh, Claws Kk. Example: female Gg × male Gg for skin color: 3 dominant boxes = 75%. Female Tt × male tt for teeth: 2 of 4 dominant = 50%.'),
     ('p', 'Quick key if the female is Ee × Ee (male Ee): 3 of 4 dominant (75%), 25% one large eye.')]))
items.append(item(6, 'Prediction vs. class count', 'Class data', 'Glue under "Class data"', 'One per student',
    [('p', 'Everyone makes one baby: flip a coin for Mom (heads = G, tails = g) and a coin for Dad. Add your baby to the class tally.'),
     tb(['Skin color', 'Punnett prediction', 'Sample class (30 babies)', 'Percent in the sample', 'Our class count'],
        [['Green (GG or Gg)', '75%', '22', '73%', ''], ['Blue (gg)', '25%', '8', '27%', '']], [1.6, 1.4, 1.7, 1.5, 1.4], rowh=0.45),
     ('p', 'The Punnett square predicted ______% green. The sample class got about ______% green. The numbers are close but not exact because every flip is ______________.   Word bank: 73 · random · 75'),
     ('h', 'Compare your own class tally with the prediction. Percent green in our class: ______%'),
     ('note', ILLUS + ' The sample class is a made-up result of 30 flips.')],
    [('p', 'The Punnett square predicted <b>75</b>% green. The sample class got about <b>73</b>% green. The numbers are close but not exact because every flip is <b>random</b>.'),
     ('p', 'Class tally will vary. Expect values near 75% green for larger classes; small samples can differ by 10 or more points. This is the point: probability predicts a pattern, not each baby.')]))

# ---------- Lesson 7 ----------
items.append(item(7, 'Four kinds of mutations', 'Four kinds of mutations', 'Fill in during the notes; glue in or keep with the notebook', 'One per student',
    [('p', 'DNA is read in groups of three bases called codons. Each codon calls for one amino acid or a stop. Original message (mRNA): AUG GAA CAC UGG. Amino acids: Met - Glu - His - Trp.'),
     tb(['Kind', 'What changes', 'Example (mRNA)', 'Effect on the protein'],
        [['Silent', 'One base changes, but the new codon calls for the same ____(1)____', 'GAA → GAG (Glu → Glu)', 'No ____(2)____ on the protein'],
         ['Missense', 'One base changes and the codon calls for a ____(3)____ amino acid', 'GAA → GUA (Glu → Val)', 'One amino acid is different; the protein may work differently'],
         ['Nonsense', 'A codon becomes a ____(4)____ codon', 'UGG → UGA (Trp → stop)', 'Protein-building ____(5)____ early, so the protein is too short'],
         ['Frameshift', 'A base is added or deleted, so every codon after it is ____(6)____', 'AUG GAA CAC UGG → AUG AAC ACU GG...', 'Most amino acids after the change are different']],
        [1.1, 2.8, 2.2, 2.6]),
     ('p', 'Word bank: amino acid · effect · different · stop · terminates · shifted'),
     ('note', 'Codon assignments are from the standard genetic code (e.g., NCBI, "The Genetic Codes"). The example message is made up for class.')],
    [tb(['Blank', 'Answer'], [['1', 'amino acid'], ['2', 'effect'], ['3', 'different'], ['4', 'stop'], ['5', 'terminates'], ['6', 'shifted']], [1, 3]),
     ('p', 'Codon check: GAA and GAG both code for glutamic acid (Glu); GUA codes for valine (Val); UGG codes for tryptophan (Trp); UGA is a stop codon. Frameshift: deleting the first G in GAA shifts the reading frame (AUG AAC ACU GG...).')]))
items.append(item(7, 'UV light and mutations', 'UV and mutations', 'Glue under "UV and mutations"', 'One per student',
    [('p', 'Skin cells were exposed to different amounts of UV light. Scientists counted new mutations per 1,000 skin cells. Worked example: with 0 hours of UV there are 2 mutations per 1,000 cells. Those come from copying errors.'),
     tb(['UV exposure (hours)', 'Mutations per 1,000 skin cells'], [['0', '2'], ['1', '6'], ['2', '11'], ['4', '23']], [2, 2], rowh=0.35),
     ('h', 'Graph it: put UV hours on the x-axis and mutations on the y-axis.'),
     ('box', 1.9, 'Graph area'),
     ('p', 'With more UV light, there are ______ mutations. The 2 mutations with no UV came from ______________ errors.   Word bank: copying · more'),
     ('note', ILLUS + ' Pattern modeled on the known effect of UV light on DNA damage in skin cells.')],
    [('p', 'With more UV light, there are <b>more</b> mutations. The 2 mutations with no UV came from <b>copying</b> errors. Points: (0, 2), (1, 6), (2, 11), (4, 23): the line rises, so more UV goes with more mutations.'),
     ('p', 'About 21 of the 23 mutations at 4 hours (23 minus the 2 baseline) are above the no-UV level, so UV likely caused most of them.')]))
items.append(item(7, 'Who passes it on? Five cases', 'Who passes it on?', 'Glue under "Who passes it on?"', 'One per student',
    [('p', 'Could the next generation inherit each change? Case A is done for you.'),
     tb(['Case', 'Where did the change happen?', 'Could the next generation inherit it? (Yes or No)', 'Why'],
        [['A', 'A skin cell gets a UV mutation and becomes a mole.', 'No', 'It is a body cell, not an egg or sperm.'],
         ['B', 'A copying error happens in a cell that makes sperm.', '', ''],
         ['C', 'UV light mutates a skin cell of a dog.', '', ''],
         ['D', 'A mutation occurs in an egg cell before fertilization.', '', ''],
         ['E', 'A chemical mutates a liver cell.', '', '']], [0.5, 3.2, 2.0, 2.3], rowh=0.6),
     ('p', 'Why: a change in a ______ cell is not passed on. A change in a cell that makes ______ can be.   Word bank: eggs or sperm · body'),
     ('h', 'Explain it: How can UV light change a gene, and when is the change inherited?'), ('lines', 3)],
    [tb(['Case', 'Inherit?', 'Why'], [['A', 'No', 'Body (skin) cell'], ['B', 'Yes', 'The cell makes sperm, so the change can be in the sperm that fertilizes an egg'],
                                    ['C', 'No', 'Skin is a body cell'], ['D', 'Yes', 'The change is in the egg, so it can be passed to offspring'],
                                    ['E', 'No', 'Liver is a body cell']], [0.7, 1, 4]),
     ('p', 'A change in a <b>body</b> cell is not passed on. A change in a cell that makes <b>eggs or sperm</b> can be.'),
     ('p', 'Sample explanation: UV light damages DNA, which can change a gene. The change is inherited only if it happens in a cell that makes eggs or sperm.')]))

# ---------- Lesson 8 ----------
items.append(item(8, 'Case data: three cases', 'Case data', 'Glue under "Case 1" (and refer back for Cases 2 and 3)', 'One per student',
    [('h', 'Case 1: the puppy litter'),
     ('p', 'Both parents are Bb. B is black, b is brown. The litter has 3 black puppies and 1 brown puppy. The brown puppy is bb.'),
     ('h', 'Case 2: a new base (coat-color gene)'),
     tb(['', 'Allele 1', 'Allele 2'], [['Parent 1', 'CCA', 'CCG'], ['Parent 2', 'CCA', 'CCC'], ['Puppy', 'CCA', 'CCT']], [1.5, 1.5, 1.5]),
     ('p', 'Each puppy gets one allele from each parent. The letters show a short stretch of DNA in the coat-color gene.'),
     ('h', 'Case 3: X-rays and mice'),
     tb(['X-ray dose', 'New mutations per 1,000 sperm cells'], [['None', '3'], ['Low', '9'], ['High', '25']], [2, 3], rowh=0.32),
     ('p', 'Scientists exposed male mice to X-rays and counted new mutations in sperm cells.'),
     ('note', ILLUS + ' Background: radiation raises mutation rates in mouse sperm cells (e.g., W. L. Russell\'s mouse studies, Oak Ridge National Laboratory, 1950s). The numbers here are not from a specific study.')],
    [('p', 'Case 1: <b>New combination.</b> Both parents are Bb, so no new allele appeared; the brown puppy is bb because it got a b from each parent.'),
     ('p', 'Case 2: <b>Mutation (copying error).</b> The puppy\'s CCT allele is new because neither parent has it. The most likely source is a copying error (no extra exposure is described), not a new combination.'),
     ('p', 'Case 3: <b>Environmental mutation.</b> High dose had 25 mutations per 1,000 sperm cells, no X-rays had 3. The extra mutations came from the X-rays. If copying errors alone caused every mutation, the groups would have similar numbers.'),
     ('p', 'CER model for Case 3: Claim: The extra mutations came from an environmental mutation (the X-rays). Evidence: The high-dose group had 25 mutations per 1,000 sperm cells, but the group with no X-rays had 3. Reasoning: If copying errors alone caused every mutation, the groups would have similar numbers.')]))

# ---------- Lesson 9 ----------
items.append(item(9, 'The new coat pattern: two kennels', 'The new coat pattern', 'Glue under "The new coat pattern"', 'One per student',
    [('p', 'Claim: A chemical in Kennel A\'s water caused the new coat patterns.'),
     ('p', 'Counterclaim: "New patterns are just copying errors. Copying errors happen in every dog."'),
     tb(['Kennel', 'New coat patterns per 1,000 puppies'], [['A (chemical in the water)', '14'], ['B (clean water)', '3']], [3, 3], rowh=0.4),
     ('p', 'Evidence: Kennel A had ______ new patterns per 1,000 puppies. Kennel B had ______.'),
     ('p', 'Defense: Copying errors happen in ______ kennels, so they cannot explain the ______ extra patterns.   Word bank: 11 · both · 3 · 14'),
     ('h', 'Your turn: restate the claim, cite the data, and show why the other explanation does not fit.'), ('lines', 4),
     ('note', ILLUS)],
    [('p', 'Evidence: Kennel A had <b>14</b> new patterns per 1,000 puppies. Kennel B had <b>3</b>. Defense: Copying errors happen in <b>both</b> kennels, so they cannot explain the <b>11</b> extra patterns.'),
     ('p', 'Sample defense: I claim a chemical in Kennel A\'s water caused the new patterns. Kennel A had 14 per 1,000 and Kennel B had 3. Copying errors happen in both kennels, so they only explain about 3 patterns; they cannot explain the 11 extra in Kennel A.')]))

# ---------- Lesson 10 ----------
items.append(item(10, 'My target tracker', 'Check my CFAs', 'Glue under "Check my CFAs"', 'One per student',
    [('p', 'Open Canvas. Write your CFA score for each target. Below a B (fewer than 4 of 5)? Do the review for that target. Then rate yourself 1 to 4 (4 = I can teach it).'),
     tb(['Target', 'CFA score', 'Review done?', 'Self-rating (1 to 4)'],
        [[T['2.1'], '', '', ''], [T['2.2'], '', '', ''], [T['2.3'], '', '', ''], [T['2.4'], '', '', ''], [T['2.5'], '', '', '']], [4.2, 1.1, 1.3, 1.5], rowh=0.55),
     ('h', 'Which target will I practice first, and how?'), ('lines', 3)],
    [('p', 'Student responses vary. Look for: lowest target chosen first, a specific plan (review in Canvas, flashcards, redo the case data), and honest self-ratings.')]))
items.append(item(10, 'Hydrangea soil data', 'Enrichment: environment and traits', 'Glue under "Enrichment: environment and traits"', 'One per student (enrichment)',
    [('p', 'A gardener grew copies of one hydrangea plant (the same DNA) in soils of different pH. In a garden of 100 plants from one parent, the soil varies:'),
     tb(['Soil', 'Flower color', 'Plants'], [['More acidic soil', 'Blue', '42'], ['Close to neutral soil', 'Purple', '33'], ['Less acidic (alkaline) soil', 'Pink', '25']], [3, 2, 1.5], rowh=0.35),
     ('p', 'The plants have the same ______________. Flower color varied because the ______________ changed how the gene works.   Word bank: soil · DNA'),
     ('h', 'Is flower color here an inherited mutation? Explain with one piece of evidence.'), ('lines', 3),
     ('note', 'Science background: hydrangea sepal color depends on how much aluminum the plant can take up, which depends on soil pH (more acidic soil gives blue flowers; see Royal Horticultural Society plant advice on changing hydrangea flower colour). The plant counts are illustrative, made up for class.')],
    [('p', 'The plants have the same <b>DNA</b>. Flower color varied because the <b>soil</b> changed how the gene works.'),
     ('p', 'Not an inherited mutation: the plants are clones with the same DNA, and color changes with soil, so the environment affected how the trait was expressed. A mutation would change the DNA sequence and stay the same in any soil.')]))

# ---------- Lessons ----------
L = []


def lesson(n, title, focus, tl, objective, agenda, moves, misc, check, diff, nb, warmup, exit_, materials=None, key_nb=None):
    L.append(dict(n=n, title=title, focus=focus, target_labels=[T[k] for k in tl], objective=objective, agenda=agenda,
                  moves=moves, misc=misc, check=check, diff=diff, nb=nb, warmup=warmup, exit=exit_,
                  materials=materials or [], key_nb=key_nb))


def rd(label, hint, h=1.0):
    return (label, hint, h, 'lines')


lesson(1, 'The Puppy Puzzle', 'How can puppies from the same parents be alike, but not identical?', ['2.1'],
       'Students notice shared and different traits in a litter and make a first model of how information passes from parents to offspring.',
       [('5', 'Warm-up', 'Notice and wonder about the puppies and parents'), ('5', 'Evidence', 'Compare the traits (puppy litter data)'),
        ('8', 'My first model', 'Draw Parent 1, Parent 2, and two offspring with arrows'), ('8', 'Sketchnotes', 'Three possible explanations'),
        ('4', 'Key idea', 'Copy the key idea'), ('3', 'Exit ticket', 'Pick one explanation and one piece of evidence')],
       ['Do not correct the first model. It is revised on Lessons 2 and 9.', 'Name the three ideas (mixed, changed, environment) without ranking them; students test them all unit.'],
       ['"Offspring are exact copies of one parent."', '"The environment is the only reason siblings differ."'],
       'Exit ticket: one explanation and the puppy evidence that points to it.', 'Reteach: use only the three traits in the table. Extend: ask which explanation could not be checked from this table.',
       dict(left=[('Notice and wonder', 'I notice ... I wonder ...', 1.0, 'lines'), ('Compare the traits', 'Glue in: Puppy litter data', 2.3, 'glue'),
                  ('My first model', 'Draw Parent 1, Parent 2, and two offspring. Use arrows to show information moving from the parents to the offspring. Label one shared trait and one different trait.', 2.1, 'box')],
            right=[('Three possible explanations', 'Three small sketch boxes: one idea in each (information mixed, information changes, environment has an effect).', 2.4, 'box'),
                   ('Key idea', 'Parents → ____ → Offspring → similarities and ____', 1.0, 'lines')]),
       ('Warm-up', 'What do you notice about the puppies and their parents? What do you wonder?'), ('Exit ticket', 'One explanation for why siblings can be different is ____. The evidence from the puppies is ____.'),
       materials=['Puppy photos or the litter table on the slides'])
lesson(2, 'Mixing Information', 'If offspring get information from the same two parents, why might each get a different combination?', ['2.1'],
       'Students use allele cards to model how sex cells and fertilization produce different combinations, then name the three sources of new variation.',
       [('3', 'Warm-up', 'Review the three ideas from Lesson 1'), ('12', 'Card activity', 'Sort cards into 6 piles; make offspring 2 and 3'),
        ('5', 'Analyze', 'Pattern in the offspring'), ('5', 'Revise model', 'Revise the Day 1 model'), ('5', 'Mini-lesson', 'Three sources of new variation'),
        ('6', 'Exit ticket', 'CFA LS3-2.1 in Canvas')],
       ['Walk the room during the card activity; ask "Which card came from which parent?"', 'Connect the cards to sex cells and fertilization; save meiosis details for Lesson 6.'],
       ['Students think each parent gives half of every trait blended together.', 'Students think a copying error is the same as a new combination.'],
       'CFA LS3-2.1: name the three sources of new genetic variation (below a B opens a review).', 'Reteach: read the three sources aloud and match each to a picture. Extend: predict how many different offspring 6 cards could make (2 × 2 × 2 per parent, 64 total).',
       dict(left=[('Make possible offspring', 'Glue in: Card table: 3 offspring', 2.4, 'glue'), ('Analyze the pattern', 'Every offspring got information from ____ parents. Each offspring got a ____ combination of cards. Different combinations can lead to different ____.', 1.4, 'lines')],
            right=[('Revise our model', 'Revise your Day 1 model: Parent 1, Parent 2, information from each parent, the information being combined, two possible offspring, one similarity, one difference.', 2.6, 'box'),
                   ('Three sources of variation', '1. New ____ of alleles. 2. ____ when DNA is copied. 3. Mutations caused by the ____.', 1.3, 'lines')],
            part2=dict(focus='What does the reading say about genes and variation?',
                       left=[('Reading: Lesson 13.1 Genes and Variation (pp. 370–374)', 'Biology: The Living Earth. Annotate: underline new terms, star the main idea.', 1.3, 'lines'),
                             ('Vocabulary', 'Word | my definition | example (allele, variation, gene pool)', 3.0, 'box')],
                       right=[('Main idea in my words', '', 1.4, 'lines'), ('Question I still have', '', 1.0, 'lines'),
                              ('Connect to the puppies', 'Sketch one way the reading explains why puppies from the same parents differ.', 1.8, 'box')],
                       warmup=('Warm-up', 'Skim the headings. What do you predict the reading is about?'), exit=('Exit ticket', 'One new idea from the reading is ____.'))),
       ('Warm-up', 'Idea 1: information is ____ in different ways. Idea 2: information ____. Idea 3: the ____ has an effect.'), ('Exit ticket', 'Name the three sources of new genetic variation.'),
       materials=['Allele cards (one set per group)', 'Scissors'])
lesson(3, 'Genetics Notes, Part 1: Genes and Alleles', 'What are genes and alleles, and what do dominant and recessive mean?', ['3.1'],
       'Students take guided notes on heredity, chromosomes, genes, alleles, and dominant/recessive, and connect them to black and brown cats.',
       [('3', 'Warm-up', 'Recall chromosome, gene, trait from Unit 2.1'), ('2', 'Notes', 'Heredity'), ('3', 'Notes', 'Chromosomes'),
        ('3+3', 'Notes', 'How traits are determined; how tigers get their stripes'), ('4', 'Notes', 'Alleles'), ('5', 'Notes', 'Dominant vs. recessive'),
        ('4', 'Notes', 'Black or brown cats'), ('3', 'Exit ticket', 'Dominant or recessive?')],
       ['Pause after each note slide for the fill-in. All answers come from the word bank on the slide.', 'Have students color-code allele pairs on the sketch; it pays off in Lessons 4 to 6.'],
       ['"Dominant means more common." Dominant means it shows when present, not that it is common.', '"Recessive alleles disappear."'],
       'Exit ticket: dominant allele definition and what recessive needs (two copies).', 'Reteach: use B and b with cat heads. Extend: ask what genotype a black cat with a brown parent must have.',
       dict(left=[('Heredity', '', 0.8, 'lines'), ('Chromosomes', '', 0.8, 'lines'), ('Genes make proteins make traits', '', 1.3, 'lines'),
                  ('Alleles', 'Sketch a pair of chromosomes. Color each set of alleles a different color.', 1.8, 'box')],
            right=[('Dominant vs. recessive', '', 1.3, 'lines'), ('Black or brown cats', 'Draw three cat heads: BB, Bb, bb. Color each one to show its coat.', 1.8, 'box')],
            part2=dict(focus='How did Mendel figure out dominant and recessive traits?',
                       left=[('Reading: Lesson 10.1 The Work of Gregor Mendel (pp. 286–290)', 'Biology: The Living Earth. Annotate: underline new terms, star the main idea.', 1.3, 'lines'),
                             ('Vocabulary', 'Word | my definition | example (heredity, allele, dominant, recessive)', 3.2, 'box')],
                       right=[('Main idea in my words', '', 1.4, 'lines'), ('Question I still have', '', 1.0, 'lines'),
                              ('Connect to the cats', 'Sketch how Mendel\'s results could explain a black cat with a brown parent.', 1.8, 'box')],
                       warmup=('Warm-up', 'What do you already know about Gregor Mendel?'), exit=('Exit ticket', 'One thing Mendel showed is ____.'))),
       ('Warm-up', 'A ____ is one long DNA molecule. A ____ is a section of DNA that codes for one protein, and proteins help produce a ____.'), ('Exit ticket', 'An allele that shows up when only one copy is present is ____. A recessive trait shows only when ____ copies are present.'))
lesson(4, 'Genetics Notes, Part 2: Genotype, Phenotype, and Punnett Squares', 'How can a Punnett square show the possible allele combinations?', ['3.1'],
       'Students distinguish genotype and phenotype, homozygous and heterozygous, and use Punnett squares to show possible allele combinations.',
       [('3', 'Warm-up', 'Capital or lowercase?'), ('2+3', 'Notes', 'Genotypes and phenotypes'), ('4', 'Notes', 'Homozygous and heterozygous'),
        ('8', 'Mini-lesson', 'Punnett squares with worked example'), ('6', 'Practice', 'Two crosses'), ('3', 'Exit ticket', 'How many are short?')],
       ['Model the three Punnett steps aloud with Tt × Tt, then release.', 'Insist on writing the capital letter first in genotypes.'],
       ['Students put both parents\' alleles on the same side of the square.', 'Students read 3:1 as "three plants and one plant" instead of a probability.'],
       'Exit ticket: in Tt × Tt, 1 of 4 boxes is short (tt).', 'Reteach: give a filled square and ask for the cross. Extend: Tt × Tt for two traits.',
       dict(left=[('Genotype and phenotype', 'Glue in: Genotype to phenotype: pea plants. Draw two eyes: color one blue and one brown.', 2.2, 'glue'),
                  ('Homozygous and heterozygous', 'Write CC, Ee, Gg, dd, AA, Hh. Color the homozygous ones green and the heterozygous ones orange. Then write the missing words.', 1.6, 'box')],
            right=[('Punnett squares', 'Glue in: Punnett squares: steps and worked example', 2.3, 'glue'), ('Practice', 'Cross 1: Tt × tt. Cross 2: TT × Tt. ____ of the 4 boxes are tall and ____ are short.', 1.6, 'box')],
            part2=dict(focus='How do Mendel\'s principles apply to many traits?',
                       left=[('Reading: Lesson 10.2 Applying Mendel\'s Principles (pp. 291–296)', 'Biology: The Living Earth. Annotate: underline new terms, star the main idea.', 1.3, 'lines'),
                             ('Vocabulary', 'Word | my definition | example (genotype, phenotype, homozygous, heterozygous, probability)', 3.2, 'box')],
                       right=[('Main idea in my words', '', 1.4, 'lines'), ('Question I still have', '', 1.0, 'lines'),
                              ('Try it', 'Use a Punnett square from the reading to check one result.', 1.8, 'box')],
                       warmup=('Warm-up', 'What is the difference between genotype and phenotype? Guess.'), exit=('Exit ticket', 'One way Punnett squares help is ____.'))),
       ('Warm-up', 'A dominant allele is written with a ____ letter. A recessive allele is written with a ____ letter.'), ('Exit ticket', 'In a Tt × Tt cross, ____ out of 4 boxes show a short plant (tt).'),
       materials=['Colored pencils'])
lesson(5, 'Monster Genetics, Part 1: Flip a Coin, Build a Monster', 'How can two coin flips build a monster\'s genotype?', ['3.1'],
       'Students use coin flips to model which allele a sex cell passes on and build a monster genotype and phenotype.',
       [('3', 'Warm-up', 'One parent, one allele'), ('4', 'Mini-lesson', 'How the lab works (coin rule)'), ('12', 'Lab', 'Build the female monster (Table 1)'),
        ('8', 'Lab', 'Fill in the male monster (Table 2)'), ('5', 'Compare', 'Why are our monsters different?'), ('3', 'Exit ticket', 'What did a coin flip stand for?')],
       ['Model one trait with the whole class before pairs start.', 'Collect one coin per pair at the end.'],
       ['Students think the flip decides the trait; it decides the allele.', 'Students forget the dominant rule when writing phenotype.'],
       'Exit ticket: coin flip = allele passed on; two flips = genotype.', 'Reteach: do the first three traits together. Extend: ask what coin could model a sex-linked trait (not required).',
       dict(left=[('How the lab works', 'Glue in: Monster Genetics: the coin rule and Table 2', 2.6, 'glue'), ('Build the female monster', 'Use Table 1 on your Monster Genetics sheet.', 2.0, 'box')],
            right=[('Fill in the male monster', 'Use Table 2 (glued in at left) and your Monster Genetics sheet.', 1.8, 'box'), ('Compare', 'Our monsters are different because the flips gave different ____ of alleles.', 1.2, 'lines')]),
       ('Warm-up', 'Each sex cell gets ____ allele. A coin flip can choose between B and ____.'), ('Exit ticket', 'Each coin flip stood for the ____ a sex cell passes on. Two flips gave the monster\'s ____.'),
       materials=['One coin per pair'])
lesson(6, 'Monster Genetics, Part 2: Predict the Baby', 'How do sex cells and fertilization mix alleles, and how can we predict the baby?', ['2.2', '3.2'],
       'Students explain how meiosis and fertilization produce new allele combinations, predict the baby with Punnett squares, and compare predictions with class counts.',
       [('3', 'Warm-up', 'One parent, two kinds of sex cells'), ('5', 'Mini-lesson', 'Sex cells and fertilization'), ('10', 'Lab', 'Punnett squares for the baby monster'),
        ('5', 'Percent chance', 'From boxes to percent'), ('6', 'Real counts', 'Class tally vs. prediction'), ('6', 'Exit ticket', 'CFA LS3-2.2 in Canvas')],
       ['Do not teach the phases of meiosis (boundary). Focus on crossing over and independent assortment as sources of mixing.', 'Collect the class tally on the board; reveal the prediction only after the tally.'],
       ['"A 3:1 result means every group of 4 has exactly 3 dominant."', 'Students mix up sex cells (one allele) and body cells (two alleles).'],
       'CFA LS3-2.2: describe how making sex cells and fertilization mix alleles into new combinations.', 'Reteach: redraw a Gg parent making G and g sex cells. Extend: compute the chance for two traits at once (multiplication).',
       dict(left=[('Sex cells and fertilization', 'Meiosis makes ____ with one allele of each gene. Crossing over happens when paired chromosomes ____ pieces of DNA. Fertilization joins two sex cells to make a new ____ of alleles.', 1.6, 'lines'),
                  ('Punnett squares for the baby', 'Glue in: Punnett square: skin color and eyes', 2.4, 'glue')],
            right=[('Percent chance', 'In a Gg × Gg cross, ____% of the boxes are green and ____% are blue.', 1.2, 'lines'), ('Class data', 'Glue in: Prediction vs. class count', 2.4, 'glue')],
            part2=dict(focus='How does meiosis make sex cells?',
                       left=[('Reading: Lesson 10.3 Meiosis (pp. 301–307)', 'Biology: The Living Earth. Skip the phases of meiosis. Annotate: underline new terms, star the main idea.', 1.3, 'lines'),
                             ('Vocabulary', 'Word | my definition | example (meiosis, gamete, crossing over, independent assortment)', 3.2, 'box')],
                       right=[('Main idea in my words', '', 1.4, 'lines'), ('Question I still have', '', 1.0, 'lines'),
                              ('Sketch it', 'Sketch a pair of chromosomes swapping one piece (crossing over).', 1.8, 'box')],
                       warmup=('Warm-up', 'How many alleles of a gene are in an egg cell? Guess.'), exit=('Exit ticket', 'Meiosis mixes alleles because ____.'))),
       ('Warm-up', 'A Gg parent makes sex cells with ____ or ____.'), ('Exit ticket', 'Describe how sex cells and fertilization make new allele combinations.'),
       materials=['Monster Genetics sheets from Lesson 5', 'One coin per pair'])
lesson(7, 'When Copying Goes Wrong', 'How do copying errors and UV light change genes, and when are the changes inherited?', ['2.3'],
       'Students explain how copying errors and environmental damage cause mutations, identify four kinds of mutations, and decide which changes can be inherited.',
       [('3', 'Warm-up', 'Back to one letter (GAG to GTG)'), ('6', 'Mini-lesson', 'How do mutations happen?'), ('5', 'Notes', 'Four kinds of mutations'),
        ('5', 'Evidence', 'UV light and mutations'), ('7', 'Sort', 'Who passes it on? Five cases'), ('3', 'Explain it', 'How can UV light change a gene?'), ('6', 'Exit ticket', 'CFA LS3-2.3 in Canvas')],
       ['Keep the mutation-type notes light: students need the idea, not the biochemistry (boundary).', 'Ask "Is that cell a body cell or does it make eggs or sperm?" for each case.'],
       ['"All mutations are harmful."', '"Any mutation can be inherited."'],
       'CFA LS3-2.3: how copying errors and UV change genes and when that change is inherited.', 'Reteach: use only Cases A to C. Extend: why can a skin-cell mutation still harm the person but not their children?',
       dict(left=[('How do mutations happen?', 'A ____ error that is not fixed becomes a mutation. UV light and some ____ can also damage DNA.', 1.1, 'lines'),
                  ('Four kinds of mutations', 'Glue in: Four kinds of mutations', 2.6, 'glue'), ('UV and mutations', 'Glue in: UV light and mutations', 1.9, 'glue')],
            right=[('Who passes it on?', 'Glue in: Who passes it on? Five cases', 2.6, 'glue'), ('Explain it', 'UV light can change a gene by ____ its DNA. The change is inherited only if it happens in a cell that makes ____.', 1.3, 'lines')],
            part2=dict(focus='How is DNA copied, and what can go wrong?',
                       left=[('Reading: Lesson 11.3 DNA Replication (pp. 328–331) and Lesson 12.4 Mutations (pp. 357–361)', 'Biology: The Living Earth. Annotate: underline new terms, star the main idea.', 1.5, 'lines'),
                             ('Vocabulary', 'Word | my definition | example (replication, mutation, proofreading, mutagen)', 3.0, 'box')],
                       right=[('Main idea in my words', '', 1.4, 'lines'), ('Question I still have', '', 1.0, 'lines'),
                              ('Connect to the puppies', 'Sketch where a copying error could enter the puppy story.', 1.8, 'box')],
                       warmup=('Warm-up', 'What is DNA replication? Guess.'), exit=('Exit ticket', 'Cells proofread DNA because ____.'))),
       ('Warm-up', 'A mutation is a ____ in the DNA sequence. A mutation can change an ____ in a protein.'), ('Exit ticket', 'Explain one way a mutation can happen and one reason a mutation might not be inherited.'))
lesson(8, 'Where Did This Variation Come From?', 'How can data show where a genetic variation came from?', ['2.4'],
       'Students read three cases, identify the source of variation in each from the data, and write a claim, evidence, and reasoning.',
       [('5', 'Warm-up', 'Clues for each source'), ('5', 'Worked example', 'Case 1: the puppy litter'), ('6', 'Case 2', 'A new base'), ('6', 'Case 3', 'X-rays and mice'),
        ('5', 'CER', 'Write your claim for Case 3'), ('6', 'Exit ticket', 'CFA LS3-2.4 in Canvas')],
       ['Make "what would the data look like?" the routine question for each source.', 'Require numbers in the evidence sentence.'],
       ['Students call any difference a mutation without checking whether the parents already had the allele.', 'Students cite a result without comparing it with the group that was not exposed.'],
       'CFA LS3-2.4: claim and evidence from a data table.', 'Reteach: give the claim and have students pick the evidence. Extend: ask for the reasoning that rules out copying errors alone.',
       dict(left=[('Clues for each source', 'New combination: every allele in the offspring was ____ in a parent. Copying error: a ____ allele that neither parent has. Environmental mutation: ____ mutations in the group that was exposed.', 1.3, 'lines'),
                  ('Case 1: the puppy litter', 'Glue in: Case data: three cases', 2.4, 'glue'), ('Case 2: a new base', 'Use "Case data: three cases". The puppy\'s CCT allele is ____ because neither parent has it. The most likely source is a ____.', 1.3, 'lines')],
            right=[('Case 3: X-rays and mice', 'Use "Case data: three cases". The high-dose group had ____ mutations. The group with no X-rays had ____. The extra mutations came from ____.', 1.3, 'lines'),
                   ('Write your claim', 'Claim: ... Evidence: ... Reasoning: ...', 2.4, 'lines')]),
       ('Warm-up', 'Which kind of clue would point to a new combination, a copying error, and an environmental mutation?'), ('Exit ticket', 'Name the source of variation in one case and the evidence.'))
lesson(9, 'Defend Your Claim and Back to the Puppies', 'How do I defend my claim against another explanation?', ['2.5'],
       'Students defend a claim against a counterclaim using data, revise the Day 1 model, and explain the puppy puzzle in writing.',
       [('4', 'Mini-lesson', 'How to defend a claim'), ('4', 'Case', 'The new coat pattern: two kennels'), ('4', 'Mystery solved', 'Fix your Day 1 model'),
        ('3', 'Write It', 'Why are the puppies alike but not identical?'), ('20', 'Work time', 'Make up missing work')],
       ['Use the Case 3 CER from Lesson 8 as the worked defense.', 'Pull small groups during make-up time for students below a B on any CFA.'],
       ['Students restate the claim but never address the counterclaim.', 'Students defend with opinion instead of numbers.'],
       'Write It: claim, evidence, and reasoning for the puppy puzzle, using the card activity and the three sources.', 'Reteach: use the three-step frame (restate, cite, show why the other explanation fails). Extend: write a second counterclaim and defend against it.',
       dict(left=[('How to defend a claim', 'A counterclaim is ____ explanation. To defend my claim I show why the ____ does not fit the data.', 1.1, 'lines'),
                  ('The new coat pattern', 'Glue in: The new coat pattern: two kennels', 2.6, 'glue'), ('Fix my Day 1 model', 'Redraw your Day 1 model. Add: new combinations, copying errors, mutations from the environment, and which changes are inherited.', 2.0, 'box')],
            right=[('Write It: the puppy puzzle', 'Claim ... Evidence ... Reasoning ...', 2.2, 'lines'), ('Make up missing work', '', 1.6, 'lines')]),
       ('Warm-up', 'Which three sources of variation have we studied? Name one piece of evidence for each.'), ('Exit ticket', 'Write one counterclaim and one piece of data that defends against it.'))
lesson(10, 'Review Day: Prepare for the CSA', 'Which CFA reviews will best get me ready for the CSA?', ['2.1', '2.2', '2.3', '2.4', '2.5'],
       'Students check CFA scores, complete the Canvas reviews they need, and rate themselves on each target.',
       [('4', 'Check-in', 'Check your CFA scores'), ('34', 'Work time', 'Do your reviews'), ('7', 'Enrichment', 'Hydrangea soil data (if all reviews done)')],
       ['Pull small groups by target; start with the lowest class-wide CFA.', 'Remind students the CSA is next class.'],
       ['Students skip reviews because they feel confident.', 'Students redo the enrichment instead of the review.'],
       'Target tracker with CFA scores, reviews done, and self-ratings.', 'Reteach: pull a small group on the weakest target. Extend: hydrangea enrichment (same DNA, different colors).',
       dict(left=[('Check my CFAs', 'Glue in: My target tracker', 2.6, 'glue'), ('My reviews', 'List each review you did and one thing you fixed.', 1.8, 'lines')],
            right=[('Enrichment: environment and traits', 'Glue in: Hydrangea soil data', 2.6, 'glue'), ('Self-check', 'Rate each target 1 to 4 on your tracker.', 1.2, 'lines')]),
       ('Warm-up', 'List the five unit targets in your own words.'), ('Exit ticket', 'The target I will study most tonight is ____ because ____.'))
lesson(11, 'CSA', 'Can I show I have met the targets for this unit?', ['2.1', '2.2', '2.3', '2.4', '2.5'],
       'Students show mastery of the five priority targets on the CSA.',
       [('2', 'Directions', 'Before you begin'), ('36', 'CSA', 'Unit 2.2 CSA in Canvas (13 questions)'), ('2', 'Reminders', 'Check written responses; read quietly')],
       ['Collect all materials. Allow notes only as the teacher permits.', 'After the CSA, students fill in the notebook reflection page.'],
       ['Students rush the written responses.'], 'CSA scores by target.', 'Reassess below-mastery targets after reteach.',
       dict(left=[('What I learned about inherited instructions', 'After the CSA: three things I understand better now.', 3.0, 'lines'), ('The puppy puzzle one more time', 'Explain the puppy puzzle with the three sources of variation.', 3.0, 'lines')],
            right=[]),
       ('Warm-up', 'Before the CSA, I feel ____ about ____.'), ('Exit ticket', 'The one idea I want to remember from this unit is ____.'))


KEYNB = {
 1: ['Notice and wonder: answers vary (e.g., I notice every puppy has some traits like Mom and some like Dad; I wonder why no two are the same).',
     'Three possible explanations: (1) information is mixed in different combinations, (2) information changes when it is copied, (3) the environment has an effect.',
     'Key idea: Parents \u2192 <b>information</b> \u2192 Offspring \u2192 similarities and <b>differences</b>.',
     'Exit ticket: e.g., One explanation is that the information is combined in different ways. The evidence is that no two puppies have the same combination of traits.'],
 2: ['Warm-up: Idea 1: information is <b>combined</b> in different ways. Idea 2: information <b>changes</b>. Idea 3: the <b>environment</b> has an effect.',
     'Analyze the pattern: Every offspring got information from <b>both</b> parents. Each offspring got a <b>different</b> combination of cards. Different combinations can lead to different <b>traits</b>.',
     'Revise our model: Offspring resemble their parents because they receive <b>information</b> from both. Offspring may differ because <b>the combination is different</b>.',
     'Three sources of variation: 1. New <b>combinations</b> of alleles. 2. <b>Errors</b> when DNA is copied. 3. Mutations caused by the <b>environment</b>.'],
 3: ['Warm-up: A <b>chromosome</b> is one long DNA molecule. A <b>gene</b> is a section of DNA that codes for one protein, and proteins help produce a <b>trait</b>.',
     'Heredity: Genetics is the study of <b>heredity</b>. Heredity is the passing of <b>traits</b> from <b>parents</b> to <b>offspring</b>. The width of a tiger\'s stripes is a trait <b>inherited</b> from its parents.',
     'Chromosomes: thread-like structures called <b>chromosomes</b>; they come in <b>pairs</b>; you usually have <b>two</b> copies of each, one from each parent.',
     'Genes make proteins make traits: <b>DNA</b> is found within chromosomes. A <b>gene</b> is a short segment of DNA. Genes contain instructions that make <b>proteins</b>, which determine <b>traits</b>. A tiger\'s <b>DNA</b> produces <b>proteins</b> that determine the width of its <b>stripes</b>.',
     'Alleles: individuals inherit <b>two</b> forms of each <b>gene</b>, one from each parent. The variations are <b>alleles</b>, written with lowercase and uppercase <b>letters</b>.',
     'Dominant vs. recessive: Dominant: <b>always</b> expressed when present; <b>capital</b> letters. Recessive: expressed if <b>two</b> copies are present; <b>lowercase</b> letters.',
     'Black or brown cats: A cat with Bb is <b>black</b> because <b>B</b> is dominant. A cat needs <b>two</b> copies of b to be brown.',
     'Exit ticket: dominant; two.'],
 4: ['Warm-up: dominant = <b>capital</b>; recessive = <b>lowercase</b>.',
     'Genotype and phenotype: the genotype is the <b>genetic</b> makeup (pair of <b>alleles</b>). The phenotype is the observable <b>traits</b>; for example <b>eye color</b>.',
     'Homozygous and heterozygous: two of the <b>same</b> allele = <b>homozygous</b> (purebred); two <b>different</b> alleles = <b>heterozygous</b> (hybrid). Green: CC, dd, AA. Orange: Ee, Gg, Hh.',
     'Practice: Cross 1 (Tt \u00d7 tt): 2 of 4 tall and 2 short. Cross 2 (TT \u00d7 Tt): 4 of 4 tall (the slide asks for how many are tall; accept 4).',
     'Exit ticket: In Tt \u00d7 Tt, <b>1</b> out of 4 boxes show a short plant (tt).'],
 5: ['Warm-up: Each sex cell gets <b>one</b> allele. A coin flip can choose between B and <b>b</b>.',
     'Compare: Our monsters are different because the flips gave different <b>combinations</b> of alleles.',
     'Exit ticket: Each coin flip stood for the <b>allele</b> a sex cell passes on. Two flips gave the monster\'s <b>genotype</b>.'],
 6: ['Warm-up: A Gg parent makes sex cells with <b>G</b> or <b>g</b>.',
     'Sex cells and fertilization: Meiosis makes <b>sex cells</b> with one allele of each gene. Crossing over happens when paired chromosomes <b>swap</b> pieces of DNA. Fertilization joins two sex cells to make a new <b>combination</b> of alleles.',
     'Percent chance: In a Gg \u00d7 Gg cross, <b>75</b>% of the boxes are green and <b>25</b>% are blue.',
     'Class data: predicted <b>75</b>% green; class got about <b>73</b>%; close but not exact because every flip is <b>random</b>.'],
 7: ['Warm-up: A mutation is a <b>change</b> in the DNA sequence. A mutation can change an <b>amino acid</b> in a protein.',
     'How do mutations happen: A <b>copying</b> error that is not fixed becomes a mutation. UV light and some <b>chemicals</b> can also damage DNA.',
     'Explain it: UV light can change a gene by <b>damaging</b> its DNA. The change is inherited only if it happens in a cell that makes <b>eggs or sperm</b>.'],
 8: ['Clues: New combination: every allele in the offspring was <b>already</b> in a parent. Copying error: a <b>new</b> allele that neither parent has, and no extra exposure. Environmental mutation: <b>more</b> mutations in the group that was exposed.',
     'Case 2: The puppy\'s CCT allele is <b>new</b> because neither parent has it. The most likely source is a <b>mutation</b>, not a new combination.',
     'Case 3: The high-dose group had <b>25</b> mutations. The group with no X-rays had <b>3</b>. The extra mutations came from <b>the X-rays</b>.',
     'CER: Claim: The extra mutations came from <b>an environmental mutation</b>. Evidence: The high-dose group had <b>25</b> mutations per 1,000 sperm cells, but the group with no X-rays had <b>3</b>. Reasoning: If copying errors alone caused every mutation, the groups would have <b>similar</b> numbers.'],
 9: ['How to defend a claim: A counterclaim is <b>another</b> explanation. To defend my claim I show why the <b>counterclaim</b> does not fit the data.',
     'The new coat pattern: see the printable key.',
     'Write It: Claim: Puppies from the same parents are alike but not identical because of <b>new combinations of alleles</b>. Evidence: In the card activity, each offspring got a different <b>combination</b> of alleles. Reasoning: Sex cells and fertilization make new combinations. Copying errors and <b>environmental mutations</b> can also change DNA, and a change is inherited only if it is in <b>eggs or sperm</b>.'],
 10: ['Student responses vary: look for honest CFA scores, completed reviews, and a specific plan.'],
 11: ['Reflection: student responses vary. Look for the three sources of variation (new combinations, copying errors, environmental mutations) and that only changes in eggs or sperm are inherited.'],
}
for l in L:
    l['key_nb'] = [('p', t) for t in KEYNB.get(l['n'], [])]

unit = dict(id='2.2', name='Inherited Instructions', std_short='HS-LS3-2 Inherited Instructions',
            std_line='Standard: HS-LS3-2. Make and defend a claim based on evidence that inheritable genetic variations may result from (1) new genetic combinations through meiosis, (2) viable errors occurring during replication, and/or (3) mutations caused by environmental factors. Targets are labeled LS3-2.1 to LS3-2.5 (priority) and LS3-3.1, LS3-3.2 (supporting).',
            lessons=L, items=sorted(items, key=lambda i: i['lesson']),
            caveats=['All numbers and counts in the printables are illustrative, made up for class unless a source is cited on the item. They are not measurements from a study.',
                     'Coin-flip, card, and Monster Genetics results vary by group. Sample answers show the method and the expected pattern, not one right draw.',
                     'Codons and amino acids in the mutation printable follow the standard genetic code. The example message is made up.',
                     'The class sample (22 green of 30 = 73%) is a made-up result. Real class tallies of 25 to 30 can differ from 75% by 10 or more points.'],
            match=dict(intro='Use this table to check Lesson 8 and Lesson 9 answers. Match each data pattern to its likely source of variation.',
                       table=dict(header=['Data pattern', 'Likely source of variation', 'Why'],
                                  rows=[['Both parents are Bb; brown puppy is bb', 'New combination of alleles', 'The puppy has only alleles the parents already had.'],
                                        ['Puppy has an allele (CCT) that neither parent has; no extra exposure', 'Copying error', 'A new allele with no exposure points to an error during copying.'],
                                        ['25 mutations per 1,000 sperm cells after high X-ray dose vs. 3 with no X-rays', 'Environmental mutation', 'The exposed group had far more mutations than the unexposed group.'],
                                        ['Kennel A: 14 new patterns; Kennel B: 3', 'Environmental mutation (chemical in water)', 'Copying errors happen in both kennels; the extra 11 need another cause.'],
                                        ['Same plant DNA, flower color varies with soil', 'Environment affecting gene expression (not a mutation)', 'DNA is the same; the trait changed with soil.']],
                                  cols=[3, 2.2, 3.4])))

if __name__ == '__main__':
    import sys
    out = sys.argv[1]
    build_printables(unit, out + '/Unit2.2_Printables.pdf')
    build_notebook(unit, out + '/Unit2.2_Student_Notebook.pdf')
    build_key(unit, out + '/Unit2.2_Printables_Teacher_Key.pdf')
    print('built')
