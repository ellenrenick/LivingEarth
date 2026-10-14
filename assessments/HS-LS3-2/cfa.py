"""CFAs for HS-LS3-2 (unit 2.2): one short exit-ticket check per priority learning target.

Each CFA is worth 6 points. MC items list the correct choice FIRST (the builder shuffles).
Teaching note: no phases of meiosis and no biochemical mechanisms.
"""

STANDARD = "HS-LS3-2"
UNIT = "2.2"
UNIT_TITLE = "Inherited Instructions"

CFAS = [
    {
        "id": "LS3-2.1", "dok": 1,
        "lt": "I can name three ways new genetic variation arises.",
        "items": [
            {"prompt": "<p>Which list names three sources of new genetic variation?</p>",
             "choices": ["New combinations from meiosis and fertilization, copying errors, and mutations from the environment",
                         "Exercise, diet, and sleep", "Learning, practice, and memory", "Sunlight, water, and soil only"],
             "feedback": "Variation arises from new combinations of alleles, errors when DNA is copied, and mutations caused by the environment."},
            {"prompt": "<p>A change in the base sequence of DNA is called a</p>",
             "choices": ["mutation", "gamete", "tissue", "protein"],
             "feedback": "A mutation is a change in DNA."},
            {"prompt": "<p>UV light and certain chemicals can cause variation by</p>",
             "choices": ["causing mutations in DNA", "making new sex cells", "copying DNA without errors", "deleting all genes"],
             "feedback": "UV light and chemicals are environmental factors that can cause mutations."},
        ],
    },
    {
        "id": "LS3-2.2", "dok": 2,
        "lt": "I can describe how making sex cells and fertilization mix alleles into new combinations.",
        "items": [
            {"prompt": "<p>How many alleles of a gene does each sex cell carry?</p>",
             "choices": ["One", "Two", "Four", "None"],
             "feedback": "Each sex cell carries one allele of each gene, so a child gets one from each parent."},
            {"prompt": "<p>Two parents each have alleles B and b. Which offspring combinations are possible?</p>",
             "choices": ["BB, Bb, or bb", "Only Bb", "Only BB", "BBB"],
             "feedback": "Each parent gives B or b, so offspring can be BB, Bb, or bb."},
            {"prompt": "<p>In 1 or 2 sentences, explain how meiosis and fertilization make a new combination of alleles in a child.</p>",
             "points": 2,
             "criteria": [(2, "Says each sex cell gets one allele of each gene, and fertilization joins two sex cells to make a new combination."),
                          (1, "Mentions sex cells or fertilization but not how alleles combine."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Meiosis gives each sex cell one allele of each gene. When a sperm and egg join in fertilization, the child gets a new combination of alleles from both parents."},
        ],
    },
    {
        "id": "LS3-2.3", "dok": 2,
        "lt": "I can explain how copying errors and things like UV light change genes, and when that change is inherited.",
        "items": [
            {"prompt": "<p>A mutation is passed to the next generation only if it occurs in</p>",
             "choices": ["a cell that makes sex cells", "any skin cell", "any muscle cell", "a cell outside the body"],
             "feedback": "Only changes in cells that become sex cells are inherited."},
            {"prompt": "<p>A cell makes a copy of its DNA before it divides. Sometimes the copy is not exact. What is this called?</p>",
             "choices": ["A copying error that can cause a mutation", "Fertilization", "A new species", "A tissue"],
             "feedback": "Errors during copying are a source of mutations."},
            {"prompt": "<p>Explain in 2 sentences how UV light can change a gene, and whether that change is always passed to children.</p>",
             "points": 2,
             "criteria": [(2, "Says UV light can change the DNA (a mutation) and the change is inherited only if it is in a cell that makes sex cells."),
                          (1, "Says UV can change DNA but not when it is inherited, or the reverse."),
                          (0, "Blank or incorrect.")],
             "exemplar": "UV light can damage DNA and cause a mutation. The change is passed to children only if it happens in a cell that makes eggs or sperm."},
        ],
    },
    {
        "id": "LS3-2.4", "dok": 2,
        "lt": "I can read data as evidence for where a genetic variation came from.",
        "items": [
            {"prompt": "<table border=\"1\" cellpadding=\"4\"><tr><th></th><th>Gene sequence</th></tr><tr><td>Mother</td><td>CAT and CAT</td></tr><tr><td>Father</td><td>CAT and CGT</td></tr><tr><td>Child</td><td>CAT and CCT</td></tr></table><p>Where did the CCT most likely come from?</p>",
             "choices": ["A mutation, because neither parent has CCT", "The mother, who has CCT", "The father, who has CCT", "Fertilization alone"],
             "feedback": "Neither parent has CCT, so it was a new change in the DNA."},
            {"prompt": "<p>A child has two alleles that were both present in the parents. This variation is best explained by</p>",
             "choices": ["a new combination of alleles from meiosis and fertilization", "a copying error", "a mutation from UV light", "a mutation from the child's diet"],
             "feedback": "If both alleles were already in the parents, the child has a new combination."},
            {"prompt": "<p>Describe one piece of data that would show a variation is a <strong>new mutation</strong> rather than a new combination.</p>",
             "points": 2,
             "criteria": [(2, "Describes a base or allele found in the child but in neither parent, or a variation not seen in family records."),
                          (1, "Gives an idea that does not clearly separate the two causes."),
                          (0, "Blank or incorrect.")],
             "exemplar": "A DNA sequence in the child that is not found in either parent, or a trait that never appeared in the family records."},
        ],
    },
    {
        "id": "LS3-2.5", "dok": 3,
        "lt": "I can make a claim, backed by data, about what caused a genetic variation.",
        "items": [
            {"prompt": "<table border=\"1\" cellpadding=\"4\"><tr><th>Group of fruit flies</th><th>Offspring with a new eye color (out of 1,000)</th></tr><tr><td>Normal conditions</td><td>3</td></tr><tr><td>Exposed to X-rays</td><td>55</td></tr></table><p>Which claim is best supported?</p>",
             "choices": ["X-rays caused mutations that were inherited by the offspring.", "X-rays changed the eye color after the flies were born.",
                         "Eye color is not affected by DNA.", "Nothing caused the difference."],
             "feedback": "More offspring had the new trait after exposure, so X-rays raised the mutation rate."},
            {"prompt": "<p>A claim about the cause of variation should be supported by</p>",
             "choices": ["data that are measured and compared", "what seems most likely", "what most people believe", "only one example"],
             "feedback": "A claim needs evidence from data."},
            {"prompt": "<p>Using the table above, write a claim and two pieces of data.</p>",
             "points": 2,
             "criteria": [(2, "States that X-rays caused the increase and cites both numbers (3 and 55)."),
                          (1, "States the claim with one number, or two numbers without a claim."),
                          (0, "Blank or incorrect.")],
             "exemplar": "X-rays caused mutations. Only 3 of 1,000 offspring had the new eye color in normal conditions, but 55 of 1,000 did after X-rays."},
        ],
    },
    {
        "id": "LS3-2.6", "dok": 3,
        "lt": "I can defend my claim against another explanation using the evidence.",
        "items": [
            {"prompt": "<p>A student claims a plant's new flower color is caused by the soil. Seeds from that plant, grown in different soil, still have the new color. What does this show?</p>",
             "choices": ["The color is probably inherited, not caused by the soil.", "The soil caused the color.", "The seeds are not alive.", "Flower color cannot be inherited."],
             "feedback": "The trait stayed when the soil changed, so it is inherited."},
            {"prompt": "<p>To defend a claim against another explanation, you should</p>",
             "choices": ["use evidence that fits your claim and does not fit the other explanation", "repeat your claim louder", "ignore the other explanation", "change your claim without evidence"],
             "feedback": "A defense uses evidence to show why one explanation fits better."},
            {"prompt": "<p>Another student says a trait in the beetles was caused by pollution, but the trait appears at the same rate in clean ponds. In 1 or 2 sentences, use that evidence to defend a different explanation.</p>",
             "points": 2,
             "criteria": [(2, "Uses the same rate in clean ponds to show pollution did not cause it, and offers an inherited explanation."),
                          (1, "Rejects the pollution claim without the evidence, or gives the evidence without a new explanation."),
                          (0, "Blank or incorrect.")],
             "exemplar": "If pollution caused the trait, it would be more common in polluted ponds. Since it appears at the same rate in clean ponds, it is more likely an inherited new combination of alleles."},
        ],
    },
]
