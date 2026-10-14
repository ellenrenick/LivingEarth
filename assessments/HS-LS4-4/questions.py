"""Question bank for the HS-LS4-4 CSA: Evolution by Selection (unit 3.4).

45-minute test, 30 points. Edit, then run `python3 ../build_unit.py HS-LS4-4`.
"""

TITLE = "HS-LS4-4 Assessment: Evolution by Selection"
STANDARD = "HS-LS4-4"
QUIZ_ID = "hs_ls4_4_evolution_by_selection"
FILE_PREFIX = "HS-LS4-4"
MAX_ATTEMPTS = 1
TIME_MINUTES = 45
KEY_POSITIONS = [2, 0, 3, 1, 0, 3, 1, 2]

DESCRIPTION = (
    "<p><strong>Living Earth (Biology) &ndash; HS-LS4-4</strong></p>"
    "<p>Construct an explanation based on evidence for how natural selection leads to adaptation of populations.</p>"
    "<p>Part 1: Vocabulary matching &middot; Part 2: Multiple choice &middot; Part 3: Free response</p>"
)

MATCHING = {
    "title": "Part 1: Vocabulary Matching",
    "points": 6,
    "prompt": "<p>Match each term with its best definition. Some definitions will not be used.</p>",
    "pairs": [
        ("Natural selection", "The process in which individuals with helpful inherited traits are more likely to survive and reproduce"),
        ("Adaptation", "An inherited trait that helps an organism survive and reproduce in its environment"),
        ("Population", "A group of individuals of the same species living in the same area"),
        ("Biotic factor", "A living part of an environment, such as a predator, a food plant, or a competitor"),
        ("Abiotic factor", "A nonliving part of an environment, such as temperature, light, or acidity"),
        ("Allele frequency", "How common a version of a gene is in a population"),
    ],
    "distractors": [
        "A change in one individual's body caused by how it is used during its life",
        "A change in the base sequence of DNA caused by UV light",
    ],
}

MULTIPLE_CHOICE = [
    {
        "title": "MC 1 - Bacteria and an antibiotic",
        "dok": 2,
        "prompt": (
            "<p>A hospital treats a bacteria population with an antibiotic each day. At the start, 1% of the bacteria "
            "carry an inherited trait that lets them survive the drug. The percent of bacteria with the trait is measured:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Day</th><th>0</th><th>2</th><th>4</th><th>6</th></tr>"
            "<tr><td>Bacteria with the survival trait (%)</td><td>1</td><td>8</td><td>40</td><td>95</td></tr>"
            "</table>"
            "<p>Which explanation <strong>best</strong> accounts for the change?</p>"
        ),
        "choices": [
            "Bacteria that already had the trait survived the drug and reproduced more, so the trait became more common in the population.",
            "Each bacterium changed itself so it could survive the drug.",
            "The drug caused all of the bacteria to develop the trait at once.",
            "Bacteria without the trait learned to copy bacteria with it.",
        ],
        "answer": 0,
        "feedback": "The trait was already present in a few bacteria. The drug acted as a selective pressure, so those bacteria reproduced more and the trait spread.",
    },
    {
        "title": "MC 2 - Drought and beak size",
        "dok": 2,
        "prompt": (
            "<p>After a drought, birds on an island can find only large, hard seeds. Before the drought, the average beak depth was 9.2 mm. "
            "Afterward, the average beak depth of the survivors' offspring was 10.1 mm. Beak depth is an inherited trait.</p>"
            "<p>Which statement <strong>best</strong> describes how the population evolved?</p>"
        ),
        "choices": [
            "Birds with deeper beaks could crack the hard seeds, survived, and had more offspring, so deeper beaks became more common.",
            "Each bird stretched its beak during the drought and passed on the longer beak.",
            "The seeds changed the birds' DNA so that all birds had deeper beaks.",
            "Birds with shallow beaks gained deeper beaks to survive.",
        ],
        "answer": 0,
        "feedback": "Variation already existed in beak size. The drought favored deeper beaks, which are inherited, so they became more common.",
    },
    {
        "title": "MC 3 - What is needed for selection?",
        "dok": 2,
        "prompt": (
            "<p>Which set of conditions <strong>must all</strong> be present for natural selection to change a population?</p>"
        ),
        "choices": [
            "The individuals vary in a trait, the trait is inherited, and individuals with some versions of the trait survive and reproduce more than others.",
            "All individuals are identical, the trait is learned, and every individual survives.",
            "The trait appears only after an individual has used it, and it is not inherited.",
            "The environment never changes, and every individual has the same number of offspring.",
        ],
        "answer": 0,
        "feedback": "Natural selection requires variation, inheritance, and differences in survival or reproduction.",
    },
    {
        "title": "MC 4 - Acidic water",
        "dok": 3,
        "prompt": (
            "<p>Scientists study a population of sea snails over 20 years as the ocean water becomes more acidic. Shell thickness is inherited.</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Year</th><th>0</th><th>10</th><th>20</th></tr>"
            "<tr><td>Water pH (lower is more acidic)</td><td>8.1</td><td>7.9</td><td>7.8</td></tr>"
            "<tr><td>Snails with thick shells (%)</td><td>12</td><td>35</td><td>70</td></tr>"
            "</table>"
            "<p>Which conclusion is <strong>best supported</strong>?</p>"
        ),
        "choices": [
            "As the water became more acidic, snails with thick shells survived and reproduced more, so thick shells became more common; acidity is an abiotic factor that drove the change.",
            "Individual snails grew thicker shells because they wanted to.",
            "Acidity is a biotic factor that made the snails relatives.",
            "The shell thickness shows that the snails left the area.",
        ],
        "answer": 0,
        "feedback": "The data show a trait that helps in the changed environment becoming more common. Acidity is a nonliving, abiotic factor.",
    },
    {
        "title": "MC 5 - A new predator",
        "dok": 2,
        "prompt": (
            "<p>Foxes are introduced to an island with rabbits. Rabbits vary in how fast they can run, and running speed is inherited. "
            "Ten years later, the average speed of the rabbit population is higher.</p>"
            "<p>Which statement <strong>best</strong> identifies the factor and the effect?</p>"
        ),
        "choices": [
            "The fox is a biotic factor; faster rabbits escaped more often and had more offspring, so fast running became more common.",
            "The fox is an abiotic factor; each rabbit trained itself to run faster.",
            "The fox is an abiotic factor; the island's temperature changed the rabbit DNA.",
            "The fox is a biotic factor that made all rabbits run faster instantly.",
        ],
        "answer": 0,
        "feedback": "A predator is a living, or biotic, factor. It selects for faster rabbits, which then leave more offspring.",
    },
    {
        "title": "MC 6 - A common misconception",
        "dok": 2,
        "prompt": (
            "<p>A student writes, &ldquo;Giraffes have long necks because their ancestors stretched their necks to reach high leaves, "
            "and then passed longer necks to their young.&rdquo;</p>"
            "<p>Which revision <strong>best</strong> explains the long necks using natural selection?</p>"
        ),
        "choices": [
            "Giraffes in the past varied in neck length, and those with longer, inherited necks reached more food, survived, and had more offspring, so long necks became common.",
            "Giraffes decided to grow long necks to survive.",
            "Stretching during life changes DNA so that offspring are born with longer necks.",
            "No explanation is possible.",
        ],
        "answer": 0,
        "feedback": "Traits gained during an individual's life are not passed on. Selection acts on inherited variation that already exists.",
    },
    {
        "title": "MC 7 - Allele frequency",
        "dok": 3,
        "prompt": (
            "<p>A population of mice lives where winters are growing colder. A fur allele <strong>A</strong> gives thicker fur. "
            "Scientists measure how common allele A is over time:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Generation</th><th>0</th><th>5</th><th>10</th><th>15</th></tr>"
            "<tr><td>Allele A frequency</td><td>0.10</td><td>0.25</td><td>0.55</td><td>0.80</td></tr>"
            "</table>"
            "<p>Which explanation is <strong>best supported</strong> by the data?</p>"
        ),
        "choices": [
            "Mice with allele A were more likely to survive the colder winters and reproduce, so the allele became more common and the population became better suited to the cold.",
            "Allele A was created in each mouse because it was cold.",
            "Allele A became common because mice with it chose to have more offspring.",
            "The population did not change because allele A was already present.",
        ],
        "answer": 0,
        "feedback": "The steady rise in the frequency of allele A shows selection for a trait that helps in a colder climate.",
    },
    {
        "title": "MC 8 - Two soil colors",
        "dok": 3,
        "prompt": (
            "<p>Small mice live on two areas separated by a wide river. One area is dark volcanic rock and one is light sand. Owls hunt "
            "the mice by sight. Fur color is inherited. Scientists count mice with each color:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Area</th><th>Dark fur (%)</th><th>Light fur (%)</th></tr>"
            "<tr><td>Dark volcanic rock</td><td>90</td><td>10</td></tr>"
            "<tr><td>Light sand</td><td>8</td><td>92</td></tr>"
            "</table>"
            "<p>Which explanation is <strong>best</strong> supported?</p>"
        ),
        "choices": [
            "Owls caught the mice that were easy to see against the ground, so mice that matched their background survived and reproduced more in each area; the river kept the two populations separate.",
            "The mice change fur color to match whichever ground they walk on.",
            "Owls made the fur dark by hunting.",
            "The river created dark and light fur in the mice.",
        ],
        "answer": 0,
        "feedback": "Predators remove the mice that stand out, so in each area the matching color becomes common. The barrier keeps the populations from mixing.",
    },
]

FREE_RESPONSE = [
    {
        "title": "FR 1 - The drought and the finches",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>On a small island, a drought killed most of the plants that make small, soft seeds. Only large, hard seeds were left. "
            "Scientists measured the birds that lived on the island before and after the drought. Beak depth is inherited.</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Beak depth of a bird</th><th>Birds that survived the drought (%)</th></tr>"
            "<tr><td>Less than 9 mm</td><td>15</td></tr>"
            "<tr><td>9 to 10 mm</td><td>45</td></tr>"
            "<tr><td>More than 10 mm</td><td>85</td></tr>"
            "</table>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th></th><th>Before drought</th><th>Offspring born after drought</th></tr>"
            "<tr><td>Average beak depth (mm)</td><td>9.2</td><td>10.1</td></tr>"
            "</table>"
            "<p>Write an explanation using <strong>Claim, Evidence, and Reasoning</strong>:</p>"
            "<ol>"
            "<li><strong>Claim:</strong> Explain how natural selection led to a change in this population.</li>"
            "<li><strong>Evidence:</strong> Use at least <strong>two</strong> pieces of data.</li>"
            "<li><strong>Reasoning:</strong> Name the abiotic factor and the food (biotic) factor that created the selection, and explain why the offspring born after the drought had a different average beak depth than their parents' generation.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Accurate claim that deeper beaks gave birds an advantage during the drought, so the population's average beak depth shifted. "
             "Cites at least two accurate data points (for example, 85% versus 15% survival; 9.2 to 10.1 mm). "
             "Names the drought as the abiotic factor and the large, hard seeds as the biotic factor. "
             "Explains the full process: variation existed, deeper beaks are inherited, deeper-beaked birds survived and reproduced more, so more offspring had deeper beaks."),
            (3, "Proficient",
             "Accurate claim and two accurate data points. Reasoning names a factor and links survival to the trait, but leaves out inheritance or variation."),
            (2, "Developing",
             "Claim is partly correct. One data point. Reasoning is vague (\"birds adapted\") without a mechanism."),
            (1, "Beginning",
             "Claim is wrong or missing. Little or no data. Reasoning shows a major misconception (for example, birds changed their beaks to survive)."),
        ],
        "grading_notes": [
            "Key data: survival 15% (under 9 mm), 45% (9 to 10 mm), 85% (over 10 mm); average beak depth 9.2 to 10.1 mm.",
            "Abiotic factor: drought (lack of rain). Biotic factor: the kind of food (seeds) available; accept competition as an additional biotic factor.",
            "Require the idea that the trait is inherited: survivors' offspring have deeper beaks.",
            "Common misconception: individual birds' beaks grew deeper because they needed to.",
        ],
        "exemplar": (
            "Natural selection caused the population to change so that deeper beaks became more common. Only 15% of birds with beaks under 9 mm survived the drought, but 85% of birds with beaks over 10 mm survived, and the average beak depth rose from 9.2 mm to 10.1 mm in the next generation. "
            "The drought, an abiotic factor, killed the plants with small soft seeds, so the only food left was large, hard seeds, a biotic factor. "
            "Birds already varied in beak depth, and beak depth is inherited. Birds with deeper beaks could crack the hard seeds, so they survived and had more offspring. "
            "Their offspring inherited deeper beaks, so the average beak depth of the population shifted."
        ),
    },
    {
        "title": "FR 2 - Salamanders and a new fish",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>A pond has a population of salamanders that vary in color pattern. Some are speckled and blend in with the mud. "
            "Others are bright orange. Color pattern is inherited. A fish that hunts by sight is added to the pond. "
            "Scientists record the following:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Generation</th><th>0 (before fish)</th><th>5</th><th>10</th><th>15</th></tr>"
            "<tr><td>Speckled salamanders (%)</td><td>20</td><td>40</td><td>70</td><td>88</td></tr>"
            "</table>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th></th><th>Speckled</th><th>Bright orange</th></tr>"
            "<tr><td>Survive each year (%)</td><td>70</td><td>20</td></tr>"
            "</table>"
            "<ol>"
            "<li><strong>Explain</strong> the change in the population using at least two pieces of data and the word <em>adaptation</em>.</li>"
            "<li><strong>Identify</strong> the biotic factor and describe how it caused the change.</li>"
            "<li><strong>Predict</strong> what would happen to the percentages over many generations if the fish were removed, and explain why.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Accurate explanation using at least two data points (20% to 88% speckled; 70% versus 20% survival). Uses adaptation correctly (speckled pattern is an inherited trait that helps survival). "
             "Identifies the fish as the biotic factor, explaining that it removed the bright salamanders that were easy to see. "
             "Predicts that without the fish the advantage would weaken and the percentage of speckled salamanders would stop rising or slowly shift, because bright orange salamanders would no longer be at a disadvantage."),
            (3, "Proficient",
             "Accurate explanation with two data points and the biotic factor identified. The prediction is correct but the reason is brief."),
            (2, "Developing",
             "One data point, or the factor is not clearly identified. Prediction is missing or unsupported."),
            (1, "Beginning",
             "Explanation wrong or missing. Little or no data. Shows a major misconception (for example, salamanders changed color to hide)."),
        ],
        "grading_notes": [
            "Key data: speckled 20%, 40%, 70%, 88% over generations; survival 70% versus 20%.",
            "Accept a prediction that the speckled percentage levels off or slowly declines, as long as the reason is that the fish no longer removes bright salamanders.",
            "Common misconception: the salamanders changed their color because of the fish.",
        ],
        "exemplar": (
            "The salamander population evolved so that the speckled color pattern became more common. The percent of speckled salamanders rose from 20% to 88% in 15 generations, and speckled salamanders survived each year at 70% compared with only 20% for bright orange ones. "
            "The speckled pattern is an adaptation because it is an inherited trait that helps the salamanders blend in with the mud and survive. "
            "The fish is the biotic factor: it hunts by sight, so it ate the bright orange salamanders more often, and the speckled ones lived to have more offspring that inherited the pattern. "
            "If the fish were removed, the bright orange color would no longer be a disadvantage, so the percentage of speckled salamanders would stop rising and could slowly change, because survival would no longer depend on color."
        ),
    },
]
