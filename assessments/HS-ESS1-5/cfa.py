"""CFAs for HS-ESS1-5 (unit 3.1): one short exit-ticket check per priority learning target.

Each CFA is worth 6 points. MC items list the correct choice FIRST (the builder shuffles).
"""

STANDARD = "HS-ESS1-5"
UNIT = "3.1"
UNIT_TITLE = "Age of the Earth"

CFAS = [
    {
        "id": "ESS1-5.1", "dok": 1,
        "lt": "I can describe Earth's outer layer as moving plates and name three kinds of plate boundaries.",
        "items": [
            {"prompt": "<p>Earth's outer layer is broken into large pieces that slowly move. These pieces are called</p>",
             "choices": ["tectonic plates", "continents only", "mantle plumes", "faults"],
             "feedback": "Earth's rigid outer layer is divided into tectonic plates."},
            {"prompt": "<p>Which list names the three kinds of plate boundaries?</p>",
             "choices": ["Divergent, convergent, and transform", "Divergent, magnetic, and volcanic", "Convergent, solid, and liquid", "Transform, island, and crater"],
             "feedback": "The three kinds are divergent, convergent, and transform."},
            {"prompt": "<p>At a transform boundary, two plates</p>",
             "choices": ["slide past each other", "move apart", "move together and one sinks", "stop moving"],
             "feedback": "Plates slide past each other at transform boundaries."},
        ],
    },
    {
        "id": "ESS1-5.2", "dok": 1,
        "lt": "I can describe where ocean crust is made and where it sinks back down.",
        "items": [
            {"prompt": "<p>New ocean crust is made at</p>",
             "choices": ["mid-ocean ridges", "subduction zones", "continental cores", "transform boundaries"],
             "feedback": "New ocean crust forms at mid-ocean ridges."},
            {"prompt": "<p>Ocean crust sinks back into the mantle at</p>",
             "choices": ["subduction zones", "mid-ocean ridges", "the middle of continents", "transform boundaries"],
             "feedback": "Ocean crust is recycled at subduction zones."},
            {"prompt": "<p>Where plates move apart, what happens?</p>",
             "choices": ["Hot rock rises and hardens to make new crust.", "Crust is destroyed.", "Plates stop moving.", "Mountains are always formed."],
             "feedback": "At divergent boundaries, new crust forms."},
        ],
    },
    {
        "id": "ESS1-5.3", "dok": 2,
        "lt": "I can read a rock-age map and describe the pattern in the ages.",
        "items": [
            {"prompt": "<table border=\"1\" cellpadding=\"4\"><tr><th>Distance from ridge (km)</th><th>0</th><th>500</th><th>1,000</th></tr><tr><td>Age of rock (million years)</td><td>0</td><td>25</td><td>50</td></tr></table><p>Which pattern does the table show?</p>",
             "choices": ["Rock gets older as distance from the ridge increases.", "Rock gets younger as distance increases.", "All the rock is the same age.", "The ages have no pattern."],
             "feedback": "Age increases with distance from the ridge."},
            {"prompt": "<p>On a rock-age map of the seafloor, the youngest rocks are found</p>",
             "choices": ["at the mid-ocean ridge", "next to continents", "at subduction zones", "in the deepest trenches"],
             "feedback": "The youngest crust is at the ridge where it forms."},
            {"prompt": "<p>Describe in 1 or 2 sentences the pattern of rock ages on both sides of a mid-ocean ridge.</p>",
             "points": 2,
             "criteria": [(2, "Says ages increase with distance from the ridge on both sides (symmetrical)."),
                          (1, "Says ages increase with distance but not that both sides match."),
                          (0, "Blank or incorrect.")],
             "exemplar": "The rock is youngest at the ridge and gets older with distance on both sides, in a matching pattern."},
        ],
    },
    {
        "id": "ESS1-5.4", "dok": 2,
        "lt": "I can explain why ocean crust is young and why continents are oldest at their ancient cores.",
        "items": [
            {"prompt": "<p>Why is the oldest ocean crust much younger than the oldest continental rock?</p>",
             "choices": ["Ocean crust keeps being made and recycled at subduction zones.", "Ocean crust formed last.", "Continents are made of ocean crust.", "Ocean crust is not affected by plate motion."],
             "feedback": "Ocean crust is continually recycled, so none survives for billions of years."},
            {"prompt": "<p>Why is the center (core) of a continent older than its edges?</p>",
             "choices": ["Crust was added around an ancient core over time.", "The core formed after the edges.", "All parts formed at the same time.", "The edges are older because they are on the coast."],
             "feedback": "Continents grew outward as newer crust was added to older cores."},
            {"prompt": "<p>In 2 sentences, explain why ocean crust is young compared with continental crust.</p>",
             "points": 2,
             "criteria": [(2, "Says ocean crust is made at ridges and destroyed at subduction zones, so it is recycled, while continental crust is not easily recycled."),
                          (1, "Says ocean crust is recycled but does not contrast with continents."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Ocean crust is made at ridges and sinks back into the mantle at subduction zones, so it is always being renewed. Continental crust is less dense and is not recycled as easily, so some of it stays for billions of years."},
        ],
    },
    {
        "id": "ESS1-5.5", "dok": 3,
        "lt": "I can judge how strong the evidence is that the crust has moved and is still moving.",
        "items": [
            {"prompt": "<p>Which evidence shows that plates are moving <strong>right now</strong>?</p>",
             "choices": ["GPS measurements of stations moving a few centimeters per year", "Fossils found on two continents", "The age of the oldest continental rock", "The shape of coastlines"],
             "feedback": "GPS shows present-day motion."},
            {"prompt": "<p>Which statement best judges the strength of the evidence for plate motion?</p>",
             "choices": ["It is strong because several independent lines of evidence agree.", "It is weak because only one fossil was found.", "It is strong because everyone believes it.", "It is weak because nothing can be measured."],
             "feedback": "Strong conclusions are supported by multiple independent lines of evidence."},
            {"prompt": "<p>Name two kinds of evidence for plate motion and say whether each shows <em>past</em> or <em>current</em> movement.</p>",
             "points": 2,
             "criteria": [(2, "Names two kinds and correctly says past or current for each (for example, GPS: current; seafloor ages or fossils: past)."),
                          (1, "Names two kinds but gets past or current wrong for one, or names only one correctly."),
                          (0, "Blank or incorrect.")],
             "exemplar": "GPS measurements show current movement. Seafloor rock ages that increase away from a ridge show past movement."},
        ],
    },
    {
        "id": "ESS1-5.6", "dok": 3,
        "lt": "I can judge how well plate tectonics explains the ages of rocks, using evidence.",
        "items": [
            {"prompt": "<p>Which observation is <strong>best explained</strong> by plate tectonics?</p>",
             "choices": ["Ocean rock is youngest at ridges and older farther away.", "Rock is made of minerals.", "The Sun shines on Earth.", "Rock can be heavy."],
             "feedback": "Plate tectonics predicts the age pattern on the seafloor."},
            {"prompt": "<p>A theory is considered a strong explanation when it</p>",
             "choices": ["explains many observations and matches data", "is old", "is believed by one person", "has never been tested"],
             "feedback": "Good theories explain many observations and agree with data."},
            {"prompt": "<p>Give one observation about the age of rocks that plate tectonics explains well, and say how it explains it (1 or 2 sentences).</p>",
             "points": 2,
             "criteria": [(2, "Names a correct observation and gives the plate-tectonic explanation."),
                          (1, "Names an observation or an explanation, but not both."),
                          (0, "Blank or incorrect.")],
             "exemplar": "Ocean rocks are all fairly young, because ocean crust is made at ridges and sinks back into the mantle at subduction zones."},
        ],
    },
]
