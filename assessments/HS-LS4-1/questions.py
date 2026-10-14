"""Question bank for the HS-LS4-1 CSA: Patterns of the Past (unit 3.3).

45-minute test, 30 points. Edit, then run `python3 ../build_unit.py HS-LS4-1`.
"""

TITLE = "HS-LS4-1 Assessment: Patterns of the Past"
STANDARD = "HS-LS4-1"
QUIZ_ID = "hs_ls4_1_patterns_of_the_past"
FILE_PREFIX = "HS-LS4-1"
MAX_ATTEMPTS = 1
TIME_MINUTES = 45
KEY_POSITIONS = [3, 1, 0, 2, 1, 3, 0, 2]

DESCRIPTION = (
    "<p><strong>Living Earth (Biology) &ndash; HS-LS4-1</strong></p>"
    "<p>Communicate scientific information that common ancestry and biological evolution are "
    "supported by multiple lines of empirical evidence.</p>"
    "<p>Part 1: Vocabulary matching &middot; Part 2: Multiple choice &middot; Part 3: Free response</p>"
)

MATCHING = {
    "title": "Part 1: Vocabulary Matching",
    "points": 6,
    "prompt": "<p>Match each term with its best definition. Some definitions will not be used.</p>",
    "pairs": [
        ("Common ancestry", "The idea that different species descend from earlier species they share"),
        ("Evolution", "Change in the inherited traits of a population over many generations"),
        ("Homologous structures", "Body parts in different species that have a similar structure because they come from a common ancestor"),
        ("Vestigial structure", "A body part that has lost most or all of its original function"),
        ("Fossil record", "The history of life shown by fossils found in layers of rock, from oldest to youngest"),
        ("Embryonic development", "The early stages of growth of an organism before it is born or hatched"),
    ],
    "distractors": [
        "Body parts with similar functions that did not come from a common ancestor",
        "A change in an individual's body caused by use during its lifetime",
    ],
}

MULTIPLE_CHOICE = [
    {
        "title": "MC 1 - Limb bones",
        "dok": 2,
        "prompt": (
            "<p>The forelimb of a human, a cat, a bat, and a whale is used for very different jobs (grasping, walking, flying, swimming). "
            "Yet each forelimb has the same basic pattern of bones: one upper arm bone, two lower arm bones, wrist bones, and finger bones.</p>"
            "<p>Which statement <strong>best</strong> explains this similarity?</p>"
        ),
        "choices": [
            "These species inherited the same basic limb structure from a common ancestor, and it was modified for different uses.",
            "The same bone pattern is the only possible design for any limb.",
            "Each species grew the same bones by copying each other.",
            "The bones are similar by chance and have no connection to ancestry.",
        ],
        "answer": 0,
        "feedback": "Homologous structures share a common basic pattern because they were inherited from a common ancestor and modified over time.",
    },
    {
        "title": "MC 2 - DNA similarity",
        "dok": 2,
        "prompt": (
            "<p>Scientists compare a section of DNA from several species with the same section in humans (approximate values):</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Species</th><th>DNA identical to humans</th></tr>"
            "<tr><td>Chimpanzee</td><td>99%</td></tr>"
            "<tr><td>Mouse</td><td>85%</td></tr>"
            "<tr><td>Chicken</td><td>65%</td></tr>"
            "<tr><td>Fruit fly</td><td>45%</td></tr>"
            "</table>"
            "<p>Which conclusion is <strong>best supported</strong> by the data?</p>"
        ),
        "choices": [
            "Species that are more closely related to humans share more of their DNA, which supports common ancestry.",
            "Chickens are more closely related to humans than chimpanzees are.",
            "DNA similarity has no connection to how species are related.",
            "Fruit flies are made of the same DNA as humans.",
        ],
        "answer": 0,
        "feedback": "The closer the relationship, the more recent the common ancestor and the more similar the DNA. That pattern supports common ancestry.",
    },
    {
        "title": "MC 3 - Early embryos",
        "dok": 2,
        "prompt": (
            "<p>Early embryos of a fish, a chicken, and a human each have a tail and a set of small pouches in the neck region. "
            "In the fish, the pouches develop into gills. In the chicken and human, they develop into other structures, not gills.</p>"
            "<p>Which interpretation is <strong>best</strong>?</p>"
        ),
        "choices": [
            "The shared early features are best explained by inheritance from a common ancestor.",
            "Humans were once fish as adults.",
            "The embryos are the same species.",
            "The early features are unrelated to ancestry.",
        ],
        "answer": 0,
        "feedback": "Similar early development in different species is evidence of shared ancestry, though adults can differ.",
    },
    {
        "title": "MC 4 - Tiny hip bones in a whale",
        "dok": 2,
        "prompt": (
            "<p>Whales swim with flippers and a tail and have no hind legs. However, many whales have small hip bones "
            "that are not attached to the backbone and are not used for walking.</p>"
            "<p>Which statement <strong>best</strong> explains why these bones are evidence for evolution?</p>"
        ),
        "choices": [
            "They are vestigial structures left over from ancestors that walked on four legs.",
            "They help the whale walk on land.",
            "They prove that whales will grow legs in the future.",
            "They have no explanation.",
        ],
        "answer": 0,
        "feedback": "A vestigial structure has lost most of its function and is best explained as inherited from an ancestor that used it.",
    },
    {
        "title": "MC 5 - A sequence of fossils",
        "dok": 3,
        "prompt": (
            "<p>Scientists find three fossils in rock layers of different ages:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Fossil</th><th>Age (millions of years)</th><th>Traits</th></tr>"
            "<tr><td>A</td><td>385</td><td>Fish with fins and gills</td></tr>"
            "<tr><td>B</td><td>375</td><td>Fish with flat head, neck, gills, and wrist-like bones inside the fins</td></tr>"
            "<tr><td>C</td><td>365</td><td>Animal with limbs with digits, a neck, and gills</td></tr>"
            "</table>"
            "<p>Which conclusion is <strong>best supported</strong> by the fossil sequence?</p>"
        ),
        "choices": [
            "The traits changed gradually over time, which supports evolution from fish toward animals with limbs.",
            "All three animals lived at the same time.",
            "Fossil C is the ancestor of Fossil A.",
            "The fossils show that fish and limbed animals are unrelated.",
        ],
        "answer": 0,
        "feedback": "Older to younger, the fossils show intermediate steps in traits, which supports evolution over time.",
    },
    {
        "title": "MC 6 - Which lines of evidence?",
        "dok": 3,
        "prompt": (
            "<p>A student claims whales and hippos share a common ancestor. She has several observations. "
            "Which set gives the <strong>strongest</strong> support for the claim?</p>"
        ),
        "choices": [
            "DNA of whales is more similar to hippos than to fish, a fossil of an early whale had legs, and whale embryos form small limb buds that later disappear.",
            "Whales and hippos both live in or near water.",
            "Both whales and hippos are large.",
            "A single picture of a whale next to a hippo.",
        ],
        "answer": 0,
        "feedback": "Strong support uses several independent lines of evidence (DNA, fossils, and embryos) that agree.",
    },
    {
        "title": "MC 7 - Reading shared traits",
        "dok": 3,
        "prompt": (
            "<p>A table shows which traits four animals have (X = has the trait):</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Trait</th><th>Fish</th><th>Frog</th><th>Lizard</th><th>Mouse</th></tr>"
            "<tr><td>Backbone</td><td>X</td><td>X</td><td>X</td><td>X</td></tr>"
            "<tr><td>Four limbs</td><td></td><td>X</td><td>X</td><td>X</td></tr>"
            "<tr><td>Egg with a waterproof membrane (amniotic egg)</td><td></td><td></td><td>X</td><td>X</td></tr>"
            "<tr><td>Hair</td><td></td><td></td><td></td><td>X</td></tr>"
            "</table>"
            "<p>Which conclusion about relationships is <strong>best supported</strong>?</p>"
        ),
        "choices": [
            "The mouse and lizard share more traits than the mouse and frog, so the mouse and lizard likely share a more recent common ancestor.",
            "The frog and the mouse share a more recent ancestor than the mouse and the lizard.",
            "The fish is the most closely related to the mouse, because they both have a backbone.",
            "The traits show that these four animals are not related.",
        ],
        "answer": 0,
        "feedback": "More shared traits point to a more recent common ancestor. The mouse and lizard share an extra trait with each other that the frog lacks.",
    },
    {
        "title": "MC 8 - A misconception",
        "dok": 2,
        "prompt": (
            "<p>A student says, &ldquo;Humans evolved from chimpanzees, so there should be no chimpanzees today.&rdquo;</p>"
            "<p>Which revision is <strong>most accurate</strong>?</p>"
        ),
        "choices": [
            "Humans and chimpanzees both descended from a common ancestor that lived millions of years ago, and both lines continued to evolve.",
            "Chimpanzees are the ancestors of humans and then disappeared.",
            "Humans and chimpanzees are unrelated.",
            "Humans evolved from gorillas, not chimpanzees.",
        ],
        "answer": 0,
        "feedback": "Related species share a common ancestor; one living species does not evolve into another living species.",
    },
]

FREE_RESPONSE = [
    {
        "title": "FR 1 - A sign for the museum",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>A museum wants a sign for visitors explaining that whales are related to land mammals. The scientists give you this evidence:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Line of evidence</th><th>Finding</th></tr>"
            "<tr><td>Anatomy</td><td>A whale flipper has the same bone pattern as a human arm (upper arm, two lower bones, wrist, fingers).</td></tr>"
            "<tr><td>Vestigial structure</td><td>Some whales have small leftover hip bones that are not used for walking.</td></tr>"
            "<tr><td>DNA</td><td>Whale DNA is more similar to the DNA of hippos and other hoofed mammals than to fish DNA.</td></tr>"
            "<tr><td>Fossils</td><td>A 50-million-year-old whale ancestor had four legs and lived near water.</td></tr>"
            "<tr><td>Embryos</td><td>Whale embryos form small hind limb buds that later stop growing.</td></tr>"
            "</table>"
            "<p>Write the text for the sign (4 to 6 sentences) that communicates to non-scientists:</p>"
            "<ol>"
            "<li><strong>Claim:</strong> Whales share a common ancestor with land mammals.</li>"
            "<li><strong>Evidence:</strong> Use at least <strong>three different lines</strong> of evidence from the table.</li>"
            "<li><strong>Reasoning:</strong> Explain what each line of evidence tells us about ancestry, and why using several lines is stronger than using one.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Clear claim in language a visitor can follow. Uses at least three different lines of evidence accurately and with details. "
             "Explains what each line shows (shared structure or DNA, leftover parts or embryo features from ancestors, fossils of ancestors). "
             "Explains that independent lines agree, which makes the conclusion stronger."),
            (3, "Proficient",
             "Clear claim. Three lines of evidence used accurately, or two with strong explanations. Explanation of why several lines are stronger is brief or missing."),
            (2, "Developing",
             "Claim present. Two lines or less. Explanation is vague (lists evidence without saying what it shows)."),
            (1, "Beginning",
             "Claim missing or wrong. One line or none. Shows a major misconception (for example, whales evolved on purpose to live in water)."),
        ],
        "grading_notes": [
            "Accept any three of the five lines. Look for a short, clear sign (4 to 6 sentences) for non-scientists.",
            "Reasoning to look for: homologous structures and similar DNA come from inheritance; vestigial structures and embryo features are leftovers from ancestors; fossils show the ancestor.",
            "Common misconception: individuals change in their lifetime to fit their environment, or evolution happens on purpose.",
        ],
        "exemplar": (
            "Whales are related to land mammals through a common ancestor. A whale's flipper has the same bone pattern as a human arm, and whale DNA is more similar to hoofed mammals like hippos than to fish. "
            "Some whales still have small hip bones and whale embryos grow tiny hind limb buds, which are leftover parts from ancestors that walked on land. "
            "Fossils also show a 50-million-year-old whale ancestor with four legs. "
            "Each kind of evidence points to the same answer, so together they are much stronger than any one alone."
        ),
    },
    {
        "title": "FR 2 - The horse fossils",
        "dok": 3,
        "points": 4,
        "prompt": (
            "<p>Scientists studied fossils of the horse family in rock layers of different ages:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Fossil</th><th>Age (millions of years)</th><th>Height at the shoulder (cm)</th><th>Toes on each foot</th></tr>"
            "<tr><td>Eohippus</td><td>55</td><td>30</td><td>4 (front), 3 (back)</td></tr>"
            "<tr><td>Mesohippus</td><td>35</td><td>60</td><td>3</td></tr>"
            "<tr><td>Merychippus</td><td>15</td><td>100</td><td>3 (one is large)</td></tr>"
            "<tr><td>Modern horse</td><td>0</td><td>150</td><td>1</td></tr>"
            "</table>"
            "<p>Write an explanation using <strong>Claim, Evidence, and Reasoning</strong>:</p>"
            "<ol>"
            "<li><strong>Claim:</strong> Explain what the fossil record shows about the horse family.</li>"
            "<li><strong>Evidence:</strong> Use at least <strong>two</strong> pieces of data from the table.</li>"
            "<li><strong>Reasoning:</strong> Explain how the fossils support evolution and common ancestry. Then describe <strong>one other kind of evidence</strong> (such as DNA or anatomy) that scientists could use to check this conclusion, and what they would expect to find.</li>"
            "</ol>"
        ),
        "rubric": [
            (4, "Advanced",
             "Accurate claim that the horse family changed gradually over time and that modern horses descended from earlier forms. "
             "Cites at least two accurate data points showing a trend (for example, height 30 to 150 cm; toes 4 to 1). "
             "Explains that a sequence of changes across layers of different ages supports evolution and common ancestry. "
             "Describes another line of evidence correctly with the expected finding (for example, DNA of horses and early relatives or other hoofed animals would be similar, and more similar in closer relatives)."),
            (3, "Proficient",
             "Accurate claim and two data points. Reasoning links fossils to evolution, but the other line of evidence is vague or its expected finding is missing."),
            (2, "Developing",
             "Claim partly correct. One data point. Reasoning is vague (\"horses changed\") or does not connect to ancestry."),
            (1, "Beginning",
             "Claim wrong or missing. Little or no data. Shows a major misconception (for example, each horse changed in its own life)."),
        ],
        "grading_notes": [
            "Key trend: height rises from 30 to 150 cm and toes decrease from 4 to 1 as the fossils get younger.",
            "Accept any correct second line of evidence with a sensible expected result: DNA similarity, homologous bones, vestigial toe bones, or embryos.",
            "Do not require the names of genes or any mechanism; the standard asks for a conceptual understanding of the role of each line of evidence.",
            "Common misconception: individual horses grew taller during their lives and passed that on.",
        ],
        "exemplar": (
            "The fossil record shows that the horse family changed gradually over millions of years, and that modern horses descended from smaller ancestors. "
            "Eohippus, 55 million years ago, was only 30 cm tall with 4 toes on its front feet, while the modern horse is 150 cm tall with 1 toe. "
            "Because the older layers hold fossils with more toes that look like earlier forms and the younger layers hold taller horses with fewer toes, the sequence shows evolution, with each type related to the ones before it through common ancestry. "
            "Scientists could check with DNA: if the fossils really are related, DNA from horses and their closest living relatives should be more similar than DNA from distant relatives."
        ),
    },
]
