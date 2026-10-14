"""CFAs for HS-LS4-1 (unit 3.3): one short exit-ticket check per priority learning target.

LS4-1.1 is a pre-assessment prompt used on launch day, not a target, so it has no CFA.
Each CFA is worth 6 points. MC items list the correct choice FIRST (the builder shuffles).
"""

STANDARD = "HS-LS4-1"
UNIT = "3.3"
UNIT_TITLE = "Patterns of the Past"

CFAS = [
    {
        "id": "LS4-1.2", "dok": 2,
        "lt": "I can describe the kinds of evidence that support common ancestry: DNA, body structures, and embryos.",
        "items": [
            {"prompt": "<p>Which list names three kinds of evidence for common ancestry?</p>",
             "choices": ["DNA similarity, shared body structures, and early embryo development", "Color, size, and name", "Where animals live, what they eat, and how loud they are", "Age, weight, and speed"],
             "feedback": "DNA, body structures, and embryos are three lines of evidence for common ancestry."},
            {"prompt": "<p>The forelimbs of a human, a bat, and a whale have the same basic bones. This is evidence for common ancestry because</p>",
             "choices": ["the structure was inherited from a common ancestor and modified for different uses", "the animals live in the same place", "bones are always the same", "all animals can fly"],
             "feedback": "Homologous structures come from a common ancestor."},
            {"prompt": "<p>Choose one kind of evidence (DNA, body structures, or embryos) and explain in 1 or 2 sentences how it supports common ancestry.</p>",
             "points": 2,
             "criteria": [(2, "Names one kind and correctly explains how it shows shared ancestry."),
                          (1, "Names a kind but the explanation is vague."),
                          (0, "Blank or incorrect.")],
             "exemplar": "DNA similarity: species that are more closely related have DNA that is more alike, because they share a more recent common ancestor."},
        ],
    },
    {
        "id": "LS4-1.3", "dok": 3,
        "lt": "I can explain to others how several lines of evidence support common ancestry.",
        "items": [
            {"prompt": "<p>Why is it stronger to use <strong>several</strong> lines of evidence for common ancestry than one?</p>",
             "choices": ["Independent kinds of evidence that agree make the conclusion more reliable.", "One line of evidence is always enough.",
                         "More evidence makes the conclusion less certain.", "Different lines always disagree."],
             "feedback": "Independent evidence that agrees strengthens a conclusion."},
            {"prompt": "<p>A student says, &ldquo;Dolphins and sharks look alike, so they share a recent ancestor.&rdquo; Which additional evidence would best test this?</p>",
             "choices": ["Comparing their DNA and their embryos", "Counting their fins", "Measuring how fast they swim", "Asking which one is bigger"],
             "feedback": "DNA and embryos are independent evidence beyond outward appearance."},
            {"prompt": "<p>Explain to a friend in 2 or 3 sentences how DNA and body structures together support the idea that two species share a common ancestor.</p>",
             "points": 2,
             "criteria": [(2, "Explains what each line shows and that together they strengthen the conclusion."),
                          (1, "Explains one line, or mentions both without explaining."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Related species have similar DNA and similar bone structures because they inherited them from a common ancestor. When both kinds of evidence point to the same relationship, we can be more sure."},
        ],
    },
    {
        "id": "LS4-1.4", "dok": 2,
        "lt": "I can describe the kinds of evidence that support evolution, like the fossil record.",
        "items": [
            {"prompt": "<p>The fossil record is evidence for evolution because it shows</p>",
             "choices": ["changes in living things across rock layers of different ages", "that all fossils are the same age", "that fossils are living", "that rocks cause evolution"],
             "feedback": "Fossils in older and younger layers show change over time."},
            {"prompt": "<p>A tiny leftover hip bone in a snake is an example of a</p>",
             "choices": ["vestigial structure", "fossil", "mutation", "homologous organ system"],
             "feedback": "Vestigial structures are leftovers from ancestors."},
            {"prompt": "<p>Name two kinds of evidence that support evolution and say what each shows (1 or 2 sentences).</p>",
             "points": 2,
             "criteria": [(2, "Names two kinds (fossils, DNA, anatomy, embryos) and states what each shows."),
                          (1, "Names two kinds without saying what they show, or explains one."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Fossils show how living things changed over time in layers of rock. DNA comparisons show how closely related species are."},
        ],
    },
    {
        "id": "LS4-1.5", "dok": 3,
        "lt": "I can explain to others how several lines of evidence support evolution.",
        "items": [
            {"prompt": "<p>Which set of evidence gives the strongest support for evolution?</p>",
             "choices": ["A fossil sequence, DNA similarity, and shared body structures", "A single fossil", "A story without data", "A guess"],
             "feedback": "Several independent lines of evidence give the strongest support."},
            {"prompt": "<p>A fossil sequence shows a gradual change in toe number. What would DNA from the same animals be expected to show if evolution is correct?</p>",
             "choices": ["More similar DNA in animals that are closer in the sequence", "No similarity at all", "Identical DNA in all of them", "No DNA"],
             "feedback": "If the fossils are related, closer relatives should have more similar DNA."},
            {"prompt": "<p>Explain to a younger student in 2 or 3 sentences why scientists accept evolution, using at least two kinds of evidence.</p>",
             "points": 2,
             "criteria": [(2, "Uses two kinds of evidence accurately and explains that they support evolution together."),
                          (1, "Uses one kind well, or two without explanation."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Fossils show living things changing over time in rock layers, and DNA shows closer relatives have more similar genes. Since different kinds of evidence agree, scientists are confident that evolution happened."},
        ],
    },
]
