"""Unit review for HS-LS4-4 (unit 3.4). Done on the review day, built around the CFAs (no practice test)."""

STANDARD = "HS-LS4-4"
UNIT_TITLE = "Evolution by Selection"
GOAL = ("Explain, using data, how natural selection changes which inherited traits are common in a population, "
        "making the population better suited to its environment.")

KEY_IDEAS = [
    "<strong>Natural selection</strong> is when individuals with helpful inherited traits are more likely to survive and reproduce. An <strong>adaptation</strong> is such a trait.",
    "<strong>It needs three things:</strong> variation in a trait, the trait is inherited, and some versions help survival or reproduction more than others.",
    "<strong>Populations evolve, not individuals.</strong> Traits gained during a lifetime (like stretched necks) are not passed on.",
    "<strong>Biotic factors</strong> are living (predators, food, competitors). <strong>Abiotic factors</strong> are nonliving (temperature, acidity, light, rainfall).",
    "<strong>Data show evolution as a shift</strong> in how common a trait is (its allele frequency or percent) over generations.",
    "<strong>If the environment changes, different traits are favored.</strong> The population becomes better suited to the new conditions.",
]

VOCAB = {
    "bank": ["natural selection", "adaptation", "population", "biotic factor", "abiotic factor", "allele frequency"],
    "blanks": [
        ("The process in which individuals with helpful inherited traits survive and reproduce more is ____________.", "natural selection"),
        ("An inherited trait that helps an organism survive and reproduce is an ____________.", "adaptation"),
        ("A group of individuals of one species living in the same area is a ____________.", "population"),
        ("A predator is a living, or ____________, part of the environment.", "biotic factor"),
        ("Temperature and acidity are nonliving, or ____________.", "abiotic factors"),
        ("How common a version of a gene is in a population is its ____________.", "allele frequency"),
    ],
}

SECTIONS = [
    {"id": "A", "title": "Key terms in action", "lts": ["LS4-4.1"],
     "intro": "<p>Sort factors and use the words correctly.</p>",
     "items": [
         ("Label each as biotic or abiotic: a predator, ocean acidity, a food plant, temperature, a competing species.", "Biotic: predator, food plant, competing species. Abiotic: ocean acidity, temperature."),
         ("What is an adaptation?", "An inherited trait that helps an organism survive and reproduce in its environment."),
         ("Define natural selection in your own words.", "Individuals with helpful inherited traits survive and reproduce more, so those traits become more common."),
     ]},
    {"id": "B", "title": "How selection causes a population to evolve", "lts": ["LS4-4.2"],
     "intro": "<p>Work through what selection needs.</p>",
     "items": [
         ("List the three things natural selection needs.", "Variation in a trait, the trait is inherited, and differences in survival or reproduction."),
         ("A student says giraffes stretched their necks and passed the longer neck on. Revise using natural selection.", "Giraffes varied in neck length. Those with longer, inherited necks reached more food, survived, and had more offspring, so long necks became common."),
         ("Bacteria: 1% survive an antibiotic at first; after a week 95% do. Explain.", "Bacteria that already had the trait survived and reproduced, so it became common."),
     ]},
    {"id": "C", "title": "Using data to show a shift", "lts": ["LS4-4.3"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Generation</th><th>0</th><th>5</th><th>10</th><th>15</th></tr><tr><td>Mice with thick fur (%)</td><td>10</td><td>25</td><td>55</td><td>80</td></tr></table>",
     "items": [
         ("Describe the shift in numbers.", "Thick fur rose from 10% in generation 0 to 80% in generation 15."),
         ("What was the average change per 5 generations?", "(80 - 10) / 3 = about 23 percentage points per 5 generations."),
         ("Winters are getting colder. Explain the shift.", "Thick-furred mice survived the cold and reproduced more, so the inherited trait became common."),
     ]},
    {"id": "D", "title": "Better suited to the environment", "lts": ["LS4-4.4"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Area</th><th>Dark fur (%)</th><th>Light fur (%)</th></tr><tr><td>Dark lava rock</td><td>90</td><td>10</td></tr><tr><td>Light sand</td><td>8</td><td>92</td></tr></table><p>Owls hunt by sight. Fur color is inherited.</p>",
     "items": [
         ("Explain the pattern in each area.", "Owls caught mice that stood out, so mice matching their background survived and reproduced more in each area."),
         ("How is each population better suited to its environment?", "Its common fur color matches the ground, so it is better hidden."),
         ("Predict what happens if the lava rock is covered by light sand over many generations.", "Dark mice would stand out and be eaten more, so light fur would become more common."),
     ]},
]

WRITE = {
    "prompt": ("<p>Wild mustard plants grow in a region with growing droughts. Flowering time is inherited.</p>"
               "<table border=\"1\" cellpadding=\"6\"><tr><th></th><th>Early-flowering plants</th><th>Late-flowering plants</th></tr>"
               "<tr><td>Plants that set seed before the dry season (%)</td><td>80</td><td>20</td></tr></table>"
               "<table border=\"1\" cellpadding=\"6\"><tr><th>Year</th><th>0</th><th>3</th><th>6</th></tr><tr><td>Early-flowering plants in the population (%)</td><td>10</td><td>35</td><td>70</td></tr></table>"
               "<p>Write an explanation: <strong>Claim</strong>, <strong>Evidence</strong> (at least two numbers), and <strong>Reasoning</strong> (name the abiotic factor, say why the trait is an adaptation, and explain how the population changed). Then predict what happens if rainfall returns to normal.</p>"),
    "checklist": ["States that early flowering became more common through natural selection",
                  "Uses at least two numbers (80% versus 20%; 10% to 70%)",
                  "Names drought (rainfall) as the abiotic factor",
                  "Explains variation, inheritance, and differences in seed-setting",
                  "Predicts that the advantage would weaken if rainfall returned"],
    "exemplar": ("Natural selection made early flowering more common. 80% of early-flowering plants set seed before the dry season compared with 20% of late-flowering plants, and the early-flowering share of the population rose from 10% to 70% in 6 years. "
                 "Drought, an abiotic factor, killed plants that had not set seed yet. Flowering time varies and is inherited, so early plants left more offspring that inherited early flowering, which makes it an adaptation. "
                 "If rainfall returned to normal, late flowering would no longer be a disadvantage, so the share of early-flowering plants would stop rising."),
}
