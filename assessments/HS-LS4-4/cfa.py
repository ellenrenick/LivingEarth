"""CFAs for HS-LS4-4 (unit 3.4): one short exit-ticket check per priority learning target.

Each CFA is worth 6 points. MC items list the correct choice FIRST (the builder shuffles).
"""

STANDARD = "HS-LS4-4"
UNIT = "3.4"
UNIT_TITLE = "Evolution by Selection"

CFAS = [
    {
        "id": "LS4-4.1", "dok": 1,
        "lt": "I can define natural selection, adaptation, population, biotic, and abiotic.",
        "items": [
            {"prompt": "<p>An inherited trait that helps an organism survive and reproduce in its environment is a(n)</p>",
             "choices": ["adaptation", "population", "abiotic factor", "habit"],
             "feedback": "An adaptation is an inherited trait that helps survival and reproduction."},
            {"prompt": "<p>Which is an <strong>abiotic</strong> factor?</p>",
             "choices": ["Temperature", "A predator", "A food plant", "A competitor"],
             "feedback": "Abiotic means nonliving; temperature is nonliving."},
            {"prompt": "<p>Natural selection is the process in which</p>",
             "choices": ["individuals with helpful inherited traits survive and reproduce more", "individuals change themselves to fit the environment", "all individuals survive equally", "the environment never affects living things"],
             "feedback": "Natural selection favors individuals with helpful inherited traits."},
        ],
    },
    {
        "id": "LS4-4.2", "dok": 2,
        "lt": "I can describe how natural selection causes a population to evolve.",
        "items": [
            {"prompt": "<p>Which order best describes natural selection?</p>",
             "choices": ["Variation exists; some individuals survive and reproduce more; their traits become more common", "Individuals try to change; they change; they pass it on",
                         "All individuals are identical; some die; the rest change", "The environment changes; every individual changes at once"],
             "feedback": "Selection acts on existing variation and changes which traits are common."},
            {"prompt": "<p>Natural selection changes</p>",
             "choices": ["the traits that are common in a population over generations", "the DNA of a single organism during its life", "the age of the organism", "nothing"],
             "feedback": "Populations evolve, not individuals."},
            {"prompt": "<p>In 2 or 3 sentences, describe how natural selection causes a population to evolve. Use the words <em>variation</em> and <em>inherited</em>.</p>",
             "points": 2,
             "criteria": [(2, "Describes variation, differences in survival and reproduction, and that the helpful inherited trait becomes more common."),
                          (1, "Describes some parts but leaves out variation or inheritance."),
                          (0, "Blank or says individuals change themselves.")],
             "exemplar": "Individuals in a population vary in an inherited trait. Those with a helpful version survive and reproduce more, so more offspring inherit it, and the trait becomes more common."},
        ],
    },
    {
        "id": "LS4-4.3", "dok": 2,
        "lt": "I can use data to show that a population's traits shifted because of natural selection.",
        "items": [
            {"prompt": "<table border=\"1\" cellpadding=\"4\"><tr><th>Generation</th><th>0</th><th>5</th><th>10</th></tr><tr><td>Beetles that are green (%)</td><td>20</td><td>50</td><td>85</td></tr></table><p>What does the data show?</p>",
             "choices": ["The green trait is becoming more common over generations.", "Beetles are changing from green to brown.", "The population is not changing.", "Green beetles are leaving the area."],
             "feedback": "The percentage of green beetles rises each generation."},
            {"prompt": "<p>Green beetles survive 80% a year and brown beetles 30% a year in a grassy field. Which explains the shift in the table above?</p>",
             "choices": ["Birds see the brown beetles more easily, so green beetles survive and reproduce more.", "Beetles turn green when they eat grass.", "Green beetles are bigger.", "The data are random."],
             "feedback": "Higher survival of green beetles explains why the trait became more common."},
            {"prompt": "<p>Use the numbers from the table to describe, in 1 or 2 sentences, how the population's traits shifted.</p>",
             "points": 2,
             "criteria": [(2, "Cites at least two numbers and states the direction of the shift."),
                          (1, "States the direction without numbers, or one number."),
                          (0, "Blank or incorrect.")],
             "exemplar": "The percent of green beetles rose from 20% in generation 0 to 85% in generation 10, so the green trait became much more common."},
        ],
    },
    {
        "id": "LS4-4.4", "dok": 3,
        "lt": "I can use evidence to explain how natural selection makes a population better suited to its environment.",
        "items": [
            {"prompt": "<p>A cold winter kills most lizards with thin skin. Thick-skinned lizards survive and breed. Which statement is best?</p>",
             "choices": ["The population becomes better suited to the cold because thick skin is inherited and becomes more common.", "Each lizard grows thicker skin during the winter.",
                         "The population is worse off.", "The winter changed the lizards' DNA."],
             "feedback": "Selection increases helpful inherited traits in the population."},
            {"prompt": "<p>Which evidence best shows a population became better suited to a changed environment?</p>",
             "choices": ["A higher percent of individuals have a trait that improves survival in the new conditions.", "The number of individuals stays the same.", "One individual changes.", "The environment is the same."],
             "feedback": "A rising percentage of individuals with a helpful trait shows better suitedness."},
            {"prompt": "<p>Use evidence from this question to explain in 2 or 3 sentences how selection made the lizard population better suited to the cold: <em>Before the winter, 10% of lizards had thick skin; after 10 winters, 75% did.</em></p>",
             "points": 2,
             "criteria": [(2, "Uses the numbers and links survival of thick-skinned lizards to the trait becoming common in the population."),
                          (1, "Uses numbers or the explanation, but not both."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Thick-skinned lizards survived the cold and had more offspring that inherited the trait. Over 10 winters the share with thick skin grew from 10% to 75%, so the population became better suited to the cold."},
        ],
    },
]
