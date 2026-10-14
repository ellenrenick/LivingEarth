"""Unit review for HS-LS4-1 (unit 3.3). Done on the review day, built around the CFAs (no practice test).

LS4-1.1 is a pre-assessment prompt used on launch day, so it has no CFA or review section.
"""

STANDARD = "HS-LS4-1"
UNIT_TITLE = "Patterns of the Past"
GOAL = ("Communicate, using several independent lines of evidence, that living things share common ancestors "
        "and have evolved over time.")

KEY_IDEAS = [
    "<strong>Common ancestry</strong> means different species descend from earlier species they share. <strong>Evolution</strong> is a change in the inherited traits of a population over many generations.",
    "<strong>DNA similarity:</strong> the more closely related two species are, the more of their DNA is alike.",
    "<strong>Body structures:</strong> <em>homologous</em> structures (like the bones in a human arm and a whale flipper) share a pattern inherited from a common ancestor. <em>Vestigial</em> structures are leftovers from ancestors.",
    "<strong>Embryos:</strong> related species have similar early development, even when adults look different.",
    "<strong>The fossil record</strong> shows living things changing across rock layers of different ages, including intermediate forms.",
    "<strong>Several independent lines of evidence that agree</strong> make the strongest case. Species evolve from shared ancestors, not from each other.",
]

VOCAB = {
    "bank": ["common ancestry", "evolution", "homologous structures", "vestigial structure", "fossil record", "embryonic development"],
    "blanks": [
        ("The idea that different species descend from earlier species they share is ____________.", "common ancestry"),
        ("Change in the inherited traits of a population over many generations is ____________.", "evolution"),
        ("The same basic bone pattern in a human arm and a whale flipper is an example of ____________.", "homologous structures"),
        ("A body part that has lost most of its function, like a whale's tiny hip bones, is a ____________.", "vestigial structure"),
        ("The history of life shown by fossils in rock layers is the ____________.", "fossil record"),
        ("The early stages of growth before birth or hatching are ____________.", "embryonic development"),
    ],
}

SECTIONS = [
    {"id": "A", "title": "Kinds of evidence for common ancestry", "lts": ["LS4-1.2"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Species</th><th>DNA identical to humans (approximate)</th></tr><tr><td>Chimpanzee</td><td>99%</td></tr><tr><td>Mouse</td><td>85%</td></tr><tr><td>Chicken</td><td>65%</td></tr></table>",
     "items": [
         ("Name three kinds of evidence for common ancestry.", "DNA similarity, shared body structures, and early embryo development."),
         ("What does the DNA table suggest about how closely each species is related to humans?", "The chimpanzee is most closely related, then the mouse, then the chicken, because more similar DNA means a more recent common ancestor."),
         ("The forelimbs of a human, bat, and whale have the same basic bones but different uses. What does this show?", "The structure was inherited from a common ancestor and modified for different uses."),
         ("Fish, chicken, and human embryos all have a tail and neck pouches early on. What does this suggest?", "They inherited these early features from a common ancestor."),
     ]},
    {"id": "B", "title": "Explaining several lines together", "lts": ["LS4-1.3"],
     "intro": "<p>Whale DNA is more like hippo DNA than fish DNA. A fossil whale ancestor had four legs. Whale embryos form hind limb buds that stop growing.</p>",
     "items": [
         ("What does each of the three observations tell you about whale ancestry?", "DNA: closer to land mammals. Fossil: the ancestor walked on land. Embryo buds: leftovers from legged ancestors."),
         ("Why is it stronger to use all three than only one?", "They are independent lines of evidence that agree, so the conclusion is more reliable."),
         ("Dolphins and sharks look alike. Why is that not good evidence that they share a recent ancestor? What would you check?", "Looks alone can be misleading. Check DNA, embryos, and skeleton."),
         ("Write 2 sentences explaining common ancestry to a friend using two lines of evidence.", "Example: Related species have similar DNA and similar bones, because they inherited them from a common ancestor. When both agree, we can be more sure."),
     ]},
    {"id": "C", "title": "Evidence for evolution", "lts": ["LS4-1.4"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Fossil</th><th>Age (million years)</th><th>Traits</th></tr><tr><td>A</td><td>385</td><td>Fish with fins and gills</td></tr><tr><td>B</td><td>375</td><td>Fish with a neck and wrist-like fin bones</td></tr><tr><td>C</td><td>365</td><td>Animal with limbs with digits</td></tr></table>",
     "items": [
         ("What does the fossil sequence show?", "Traits changed gradually over time, with intermediate forms."),
         ("What kind of structure is a snake's tiny leftover hip bone?", "A vestigial structure, a leftover from ancestors that had legs."),
         ("Name two kinds of evidence that support evolution.", "Fossil record and DNA similarity (or homologous structures, vestigial structures, embryos)."),
     ]},
    {"id": "D", "title": "Putting it together", "lts": ["LS4-1.5"],
     "intro": "<p>Use several lines of evidence to explain evolution.</p>",
     "items": [
         ("A student says, &ldquo;Humans evolved from chimpanzees, so there should be no chimpanzees.&rdquo; Revise.", "Humans and chimpanzees descended from a common ancestor millions of years ago. Both lines kept evolving."),
         ("If a fossil sequence shows a gradual change in toe number, what would DNA from the same animals be expected to show?", "Closer relatives in the sequence would have more similar DNA."),
         ("Explain to a younger student why scientists accept evolution, using two lines of evidence.", "Fossils show living things changing over time, and DNA shows closer relatives have more similar genes. Because different evidence agrees, scientists are confident."),
     ]},
]

WRITE = {
    "prompt": ("<p>A museum wants a sign explaining that birds are related to dinosaurs. Use this evidence:</p>"
               "<table border=\"1\" cellpadding=\"6\"><tr><th>Line of evidence</th><th>Finding</th></tr>"
               "<tr><td>Fossils</td><td>Fossils 150 to 125 million years old show dinosaurs with feathers and wings, and early birds with teeth and bony tails.</td></tr>"
               "<tr><td>Anatomy</td><td>A bird's wing has the same bone pattern as the forelimb of a meat-eating dinosaur.</td></tr>"
               "<tr><td>Nests</td><td>Fossil nests show some dinosaurs sat on eggs, as birds do.</td></tr>"
               "<tr><td>DNA</td><td>Birds' DNA is more similar to crocodiles' than to lizards'.</td></tr></table>"
               "<p>Write the sign (4 to 6 sentences) for non-scientists: a <strong>claim</strong>, at least <strong>three different lines</strong> of evidence, and <strong>reasoning</strong> about what each shows and why using several lines is stronger.</p>"),
    "checklist": ["States the claim in plain language that birds share a common ancestor with dinosaurs",
                  "Uses at least three different lines of evidence from the table",
                  "Explains what each line shows about ancestry",
                  "Explains why several independent lines are stronger than one",
                  "Does not say individuals changed on purpose or in their lifetimes"],
    "exemplar": ("Birds are living relatives of dinosaurs and share a common ancestor with them. Fossils show dinosaurs with feathers and wings and early birds with teeth and bony tails, which are intermediate forms. A bird's wing has the same bone pattern as the forelimb of a meat-eating dinosaur, and fossil nests show some dinosaurs sat on eggs the way birds do. "
                 "Bird DNA is also more similar to crocodile DNA than to lizard DNA. Each kind of evidence points to the same answer, so together they are much stronger than any one alone."),
}
