"""Unit review for HS-LS1-2 (unit 1.1). Done on the review day, built around the CFAs (no practice test)."""

STANDARD = "HS-LS1-2"
UNIT_TITLE = "Organization in Organisms"
GOAL = ("Use a model to show how cells, tissues, organs, and organ systems are organized in a multicellular "
        "organism, and how interacting systems provide the functions the organism needs.")

KEY_IDEAS = [
    "<strong>Cells are the basic unit of life.</strong> Every living thing is made of one or more cells. A bacterium is one cell; a human has trillions.",
    "<strong>Levels of organization, smallest to largest:</strong> cell, tissue, organ, organ system, organism. Each level is built from the level below it.",
    "<strong>A tissue</strong> is a group of similar cells doing one job. <strong>An organ</strong> is made of several different tissues working together. <strong>An organ system</strong> is a group of organs working together.",
    "<strong>Structure fits function.</strong> The shape and makeup of a part helps it do its job, like the many folds of the small intestine or the thin walls of the air sacs in the lungs.",
    "<strong>Systems depend on each other.</strong> Movement needs the nervous, muscular, and skeletal systems. Delivering oxygen needs the respiratory and circulatory systems.",
    "<strong>A change at one level affects the levels above it.</strong> If a tissue in an artery is damaged, the artery, the circulatory system, and the organs it serves are affected.",
]

VOCAB = {
    "bank": ["cell", "tissue", "organ", "organ system", "organism", "structure and function"],
    "blanks": [
        ("The basic unit of structure and function in all living things is the ____________.", "cell"),
        ("A group of similar cells that work together to do one job is a ____________.", "tissue"),
        ("The stomach is made of several different tissues working together, so it is an ____________.", "organ"),
        ("The stomach, intestines, and liver work together to digest food, so together they are an ____________.", "organ system"),
        ("A whole living thing, made of one cell or many organ systems, is an ____________.", "organism"),
        ("The idea that a part's shape fits the job it does is called ____________.", "structure and function"),
    ],
}

SECTIONS = [
    {"id": "A", "title": "Levels and cells", "lts": ["LS1-2.1", "LS1-2.2"],
     "intro": "<p>Use the levels of organization and the idea that all living things are made of cells.</p>",
     "items": [
         ("Put these in order from smallest to largest: <em>organ system, cell, organism, tissue, organ</em>.", "Cell, tissue, organ, organ system, organism."),
         ("Name the level of organization for each: (a) a sheet of similar lining cells in the stomach, (b) the stomach, (c) the digestive system, (d) a single bacterium.", "(a) tissue, (b) organ, (c) organ system, (d) organism (a one-celled organism)."),
         ("True or false: Every living thing has organs. Explain.", "False. Many organisms, like bacteria, are one cell with no tissues or organs. Every living thing is made of at least one cell."),
         ("Why is the cell called the basic unit of life?", "It is the smallest unit that can carry out the functions of life, and all living things are made of cells."),
     ]},
    {"id": "B", "title": "Building up from the level below", "lts": ["LS1-2.3"],
     "intro": "<p>Each level is built from the level below it.</p>",
     "items": [
         ("Complete the chain for the muscular system: muscle cell &rarr; ____________ &rarr; biceps (an ____________) &rarr; ____________ &rarr; human (an ____________).", "Muscle cell, muscle tissue, biceps (organ), muscular system, human (organism)."),
         ("The heart has muscle tissue, connective tissue, and nervous tissue. Why is the heart an organ and not a tissue?", "An organ is made of several different tissues that work together to do one job. The heart has three kinds of tissue, so it is an organ."),
         ("A student says, &ldquo;A tissue is made of organs.&rdquo; Correct the statement.", "A tissue is made of cells. Organs are made of tissues."),
     ]},
    {"id": "C", "title": "Structure, function, and working together", "lts": ["LS1-2.4"],
     "intro": "<p>Match each structure to its function, then think about how systems depend on each other.</p><table border=\"1\" cellpadding=\"6\"><tr><th>Structure</th><th>Where</th></tr><tr><td>Millions of tiny folds</td><td>Inner wall of the small intestine</td></tr><tr><td>Very thin walls</td><td>Air sacs of the lungs</td></tr><tr><td>Hair-like extensions</td><td>Cells on plant roots</td></tr><tr><td>Very long cells</td><td>Nerves that carry signals</td></tr></table>",
     "items": [
         ("For each structure in the table, explain how it fits the job it does.", "Folds give the intestine a large surface to take in digested food. Thin walls let oxygen pass quickly into the blood. Root hairs give a large surface for taking in water. Long nerve cells carry signals quickly over long distances."),
         ("During a sprint, breathing and heartbeat speed up. Explain how the respiratory and circulatory systems work together.", "The respiratory system takes in more oxygen, and the circulatory system moves blood faster to carry that oxygen to the working muscles."),
         ("Predict what happens to the muscular system if the circulatory system slows down. Explain.", "The muscles get less oxygen and tire quickly, because the circulatory system delivers oxygen to them. One system's failure affects the others."),
         ("An artery has lost most of its elastic tissue. Trace the effect from the tissue up to the organism.", "The artery (organ) cannot regulate blood flow well, so the circulatory system delivers blood less effectively, and the organs that depend on it work poorly, which affects the whole person."),
     ]},
    {"id": "D", "title": "Using and building models", "lts": ["LS1-2.5", "LS1-2.6"],
     "intro": "<p>A model shows parts and how they connect, with arrows. A model of levels shows each level built from the one below.</p>",
     "items": [
         ("Make a flow model with arrows for catching a ball. Include the nervous, muscular, and skeletal systems.", "Eyes see ball and nerves send signals (nervous system) &rarr; brain sends signals to arm muscles (nervous to muscular) &rarr; muscles contract and pull on bones (muscular and skeletal) &rarr; hand closes on ball."),
         ("A student's model is: <em>brain &rarr; leg muscles &rarr; legs move</em>. What is missing, and why does it matter?", "The skeletal system. Muscles move the body by pulling on bones, so a complete model needs the bones."),
         ("Plan your own model of how the body digests food and delivers it to the cells. List three parts and the arrows between them.", "Example: stomach and small intestine (digestive system) break down food and pass nutrients into the blood &rarr; circulatory system carries them &rarr; cells of the body use them. Any three real parts with correct arrows are acceptable."),
         ("Add the levels of organization to your model: name a cell, a tissue, an organ, and the system for one part.", "Example: small intestine lining cell, lining tissue, small intestine (organ), digestive system."),
     ]},
]

WRITE = {
    "prompt": ("<p>A person with damaged lungs gets tired very quickly when climbing stairs. Doctors measure:</p>"
               "<table border=\"1\" cellpadding=\"6\"><tr><th></th><th>Healthy</th><th>Damaged lungs</th></tr>"
               "<tr><td>Oxygen reaching the blood (percent of normal)</td><td>100</td><td>60</td></tr>"
               "<tr><td>Heart rate on the stairs (beats per minute)</td><td>110</td><td>150</td></tr>"
               "<tr><td>Time before the leg muscles tire (minutes)</td><td>12</td><td>3</td></tr></table>"
               "<p>Write an explanation: <strong>Claim</strong> (how the lung damage affects other systems), <strong>Evidence</strong> (at least two data points), and <strong>Reasoning</strong> (how the respiratory, circulatory, and muscular systems interact, and how the structure of the lungs fits their job).</p>"),
    "checklist": ["States a claim that damage to one organ system affects other systems and the whole person",
                  "Uses at least two numbers from the table",
                  "Names at least three organ systems and what each does",
                  "Shows how the systems depend on each other (arrows or sentences)",
                  "Explains one structure-function fit (for example, thin walls of the air sacs)"],
    "exemplar": ("The damaged lungs lower the oxygen that reaches the body, which makes the heart and muscles work harder and tire sooner. Only 60% of the normal oxygen reaches the blood, the heart rate on the stairs rises from 110 to 150, and the leg muscles tire after 3 minutes instead of 12. "
                 "The respiratory system takes in oxygen, the circulatory system carries it to the muscular system, and the heart beats faster to make up for the lower oxygen. The air sacs of healthy lungs have thin walls that let oxygen pass quickly into the blood, but damaged air sacs cannot, so the whole chain suffers."),
}
