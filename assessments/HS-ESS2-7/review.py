"""Unit review for HS-ESS2-7 (unit 3.2). Done on the review day, built around the CFAs (no practice test).

ESS2-7.5 is DOK 4 depth work; its section here stays at DOK 3 like the CSA.
"""

STANDARD = "HS-ESS2-7"
UNIT_TITLE = "Changing Earth, Changing Life"
GOAL = ("Argue from evidence that Earth's systems and life have changed each other, and have changed together, over time.")

KEY_IDEAS = [
    "<strong>Earth changes life.</strong> Ice ages, impacts, and changes in the atmosphere have caused extinctions and opened new habitats.",
    "<strong>Life changes Earth.</strong> Photosynthetic microbes added oxygen to the atmosphere. Plants and microbes build soil. Corals build reefs that change coasts.",
    "<strong>The changes link up in chains.</strong> Life added oxygen, oxygen changed rocks and weathering, and the new atmosphere made oxygen-using animals possible.",
    "<strong>A feedback is a loop.</strong> Life builds soil, soil supports more life, and more life builds more soil.",
    "<strong>Evidence comes from several records:</strong> fossils (life), rock chemistry and rusted iron layers (atmosphere and oceans), and climate records.",
    "<strong>A strong argument combines several kinds of evidence</strong> into one story with a clear claim and reasoning.",
]

VOCAB = {
    "bank": ["biosphere", "atmosphere", "weathering", "feedback", "fossil", "coevolution"],
    "blanks": [
        ("All the living things on Earth make up the ____________.", "biosphere"),
        ("The gases around Earth make up the ____________.", "atmosphere"),
        ("The breaking down of rock by water, air, ice, or living things is ____________.", "weathering"),
        ("A change that causes further changes that speed up or slow the original change is a ____________.", "feedback"),
        ("The preserved remains of a living thing from long ago is a ____________.", "fossil"),
        ("The idea that Earth's systems and life change each other over time is the ____________ of Earth and life.", "coevolution"),
    ],
}

SECTIONS = [
    {"id": "A", "title": "Earth changes life and life changes Earth", "lts": ["ESS2-7.1", "ESS2-7.2"],
     "intro": "<p>Label each example as <em>Earth changed life</em> or <em>life changed Earth</em>.</p>",
     "items": [
         ("Photosynthetic microbes added oxygen to the atmosphere.", "Life changed Earth."),
         ("An ice age made large parts of the land too cold for many plants.", "Earth changed life."),
         ("An asteroid impact darkened the sky and many animals died out.", "Earth changed life."),
         ("Plants and lichens broke down rock and formed soil.", "Life changed Earth."),
         ("Give one example of each direction in your own words.", "Example: life changed Earth when corals built reefs that changed erosion; Earth changed life when a colder climate caused extinctions."),
     ]},
    {"id": "B", "title": "Chains of cause and effect", "lts": ["ESS2-7.3"],
     "intro": "<p>Put the events in order and explain the links.</p>",
     "items": [
         ("Order: (a) oxygen-using animals appear, (b) microbes release oxygen, (c) oxygen builds up in the air and rusts iron in rocks.", "(b), (c), (a)."),
         ("Which steps show life changing Earth, and which show Earth changing life?", "(b) and (c) are life changing Earth's atmosphere and rocks. (a) is the changed Earth making new life possible."),
         ("An asteroid impact cooled the climate and many animals died out. Small mammals later became many new kinds. Explain the two-way story.", "An Earth event changed the climate and life; survivors then evolved to fill open habitats."),
     ]},
    {"id": "C", "title": "Writing an argument", "lts": ["ESS2-7.4"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Site</th><th>Living things present</th><th>Soil depth (cm)</th></tr><tr><td>1</td><td>None</td><td>0</td></tr><tr><td>2</td><td>Microbes and lichens</td><td>2</td></tr><tr><td>3</td><td>Mosses, shrubs, and trees</td><td>35</td></tr></table>",
     "items": [
         ("Write a claim the data support.", "Living things help form soil, and more life goes with deeper soil."),
         ("Cite two numbers as evidence.", "Site 1 has no life and 0 cm of soil; Site 3 has trees and 35 cm."),
         ("Write the reasoning that links the evidence to the claim.", "Microbes, lichens, and plants break down rock and add organic material that builds soil."),
     ]},
    {"id": "D", "title": "Combining evidence", "lts": ["ESS2-7.5"],
     "intro": "<p>Four kinds of evidence: (a) rusted iron layers in rocks, (b) fossils of oxygen-making microbes, (c) gas trapped in ancient rocks showing rising oxygen, (d) fossils of large animals that appear later.</p>",
     "items": [
         ("Which kinds of evidence show life changed the atmosphere? Which show the changed atmosphere changed life?", "(b) and (c) show life changing the atmosphere (with (a) showing its effect on rocks). (d) shows the new atmosphere making large animals possible."),
         ("Write a combined argument in 3 sentences using at least three of the four.", "Microbes that made oxygen existed (b), oxygen rose in the air (c) and rusted iron in rocks (a), and later large animals that need oxygen appeared (d), so Earth and life changed together."),
         ("Extension: What might the fossil record look like if oxygen had never risen? Explain.", "Likely no large animals, only small or one-celled life, because oxygen-using life needs oxygen."),
     ]},
    {"id": "E", "title": "Feedbacks and the whole story", "lts": ["ESS2-7.6"],
     "intro": "<p>Use feedback loops and several examples to argue that Earth and life changed together.</p>",
     "items": [
         ("Describe a feedback between life and soil.", "Life builds soil, soil supports more life, and more life builds more soil."),
         ("A coral reef changes waves and erosion and also creates habitat. Explain why this is two-way.", "Corals (life) changed the coast (Earth), and the changed coast created habitat for more life."),
         ("Write 2 sentences arguing Earth and life changed together, using one example.", "Photosynthetic microbes added oxygen to the air, which changed rocks and later made animals possible. Each change shaped the next, so the two changed together."),
     ]},
]

WRITE = {
    "prompt": ("<p>Scientists studied a period when the first forests spread across land:</p>"
               "<table border=\"1\" cellpadding=\"6\"><tr><th>Million years ago</th><th>500</th><th>400</th><th>350</th></tr>"
               "<tr><td>Land plants</td><td>None</td><td>Small plants</td><td>Large forests</td></tr>"
               "<tr><td>Thickness of soil on land (relative)</td><td>1</td><td>4</td><td>10</td></tr>"
               "<tr><td>Carbon dioxide in the air (ppm)</td><td>4,000</td><td>2,000</td><td>800</td></tr></table>"
               "<p>Write an argument: <strong>Claim</strong> (how life and Earth changed each other), <strong>Evidence</strong> (at least three numbers), and <strong>Reasoning</strong> (a chain of cause and effect, with one way life changed Earth and one way the changed Earth could affect life).</p>"),
    "checklist": ["States that the spread of land plants and changes in soil and atmosphere went together",
                  "Uses at least three numbers from the table",
                  "Explains life changing Earth (plants building soil and changing the atmosphere)",
                  "Explains Earth changing life (more soil and a changed climate let more kinds of life live on land)",
                  "Links the steps in a chain and avoids saying more than the data show"],
    "exemplar": ("Life and Earth changed together as land plants spread. Land plants went from none to large forests, soil thickness rose from 1 to 10, and carbon dioxide in the air fell from 4,000 to 800 ppm. "
                 "Plants and their roots break down rock and add organic material, which builds soil, and the data show CO<sub>2</sub> falling as plants spread, so life changed the atmosphere and the land. "
                 "The thicker soil and changed air then changed conditions for life, letting more kinds of plants and animals live on land, which in turn built even more soil."),
}
