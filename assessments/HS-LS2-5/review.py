"""Unit review for HS-LS2-5 (unit 1.2). Done on the review day, built around the CFAs (no practice test)."""

STANDARD = "HS-LS2-5"
UNIT_TITLE = "Energy Through Carbon"
GOAL = ("Use a model to show how photosynthesis and cellular respiration, along with other processes, "
        "cycle carbon among the biosphere, atmosphere, hydrosphere, and geosphere.")

KEY_IDEAS = [
    "<strong>Four spheres store carbon:</strong> the atmosphere (CO<sub>2</sub> in the air), biosphere (living things), hydrosphere (dissolved in water), and geosphere (rocks, soil, fossil fuels).",
    "<strong>Photosynthesis</strong> uses light energy to move carbon from CO<sub>2</sub> in the atmosphere (or water) into sugar in living things.",
    "<strong>Cellular respiration</strong> releases the energy stored in sugar and returns carbon to the atmosphere as CO<sub>2</sub>. Plants and animals both do it, all the time.",
    "<strong>Other processes move carbon too:</strong> burning, decay, burial in rock, and CO<sub>2</sub> dissolving in or leaving the ocean.",
    "<strong>Carbon is conserved.</strong> It changes places and forms but is never created or destroyed. Light is energy, not carbon.",
    "<strong>If one part of the cycle changes, carbon builds up or drops elsewhere.</strong> Use the arrows in a model to predict where.",
]

VOCAB = {
    "bank": ["biosphere", "atmosphere", "hydrosphere", "geosphere", "photosynthesis", "cellular respiration"],
    "blanks": [
        ("All living things on Earth make up the ____________.", "biosphere"),
        ("The layer of gases around Earth, which holds CO<sub>2</sub>, is the ____________.", "atmosphere"),
        ("The oceans, lakes, rivers, and groundwater make up the ____________.", "hydrosphere"),
        ("Rocks, soil, and fossil fuels are part of the ____________.", "geosphere"),
        ("Plants use light energy to build sugar from CO<sub>2</sub> and water in ____________.", "photosynthesis"),
        ("Cells release the energy in sugar and give off CO<sub>2</sub> in ____________.", "cellular respiration"),
    ],
}

SECTIONS = [
    {"id": "A", "title": "Spheres and other carbon-moving processes", "lts": ["LS2-5.1", "LS2-5.2"],
     "intro": "<p>Name where carbon is stored and the processes, besides photosynthesis and respiration, that move it.</p>",
     "items": [
         ("In which sphere is the carbon in each: (a) coal, (b) CO<sub>2</sub> gas in the air, (c) a maple tree, (d) CO<sub>2</sub> dissolved in the ocean?", "(a) geosphere, (b) atmosphere, (c) biosphere, (d) hydrosphere."),
         ("Complete the table: for each process, give the sphere carbon moves from and to. <em>Burning gasoline; burial of dead sea creatures under mud; decay of fallen leaves; CO<sub>2</sub> dissolving into the ocean.</em>", "Burning gasoline: geosphere to atmosphere. Burial: biosphere to geosphere. Decay: biosphere to atmosphere and soil (geosphere). Dissolving: atmosphere to hydrosphere."),
         ("True or false: When wood burns, the carbon in it is destroyed. Explain.", "False. Carbon is conserved. It moves from the wood (biosphere) into the air as CO<sub>2</sub>."),
     ]},
    {"id": "B", "title": "Photosynthesis and cellular respiration", "lts": ["LS2-5.3"],
     "intro": "<p>A plant in a sealed jar with a CO<sub>2</sub> sensor: bright light, CO<sub>2</sub> fell from 800 to 520 ppm in 2 hours. In the dark, CO<sub>2</sub> rose from 800 to 950 ppm.</p>",
     "items": [
         ("Explain the drop in CO<sub>2</sub> in the light.", "Photosynthesis took in more CO<sub>2</sub> than the plant's respiration gave off, moving carbon from the air into sugar."),
         ("Explain the rise in the dark.", "There is no photosynthesis in the dark, but the plant's cells still do cellular respiration, which gives off CO<sub>2</sub>."),
         ("Fill in: Photosynthesis moves carbon from the ____________ to the ____________. Cellular respiration moves it from the ____________ back to the ____________.", "Atmosphere, biosphere (living things); biosphere, atmosphere."),
         ("A student says only animals do cellular respiration. What evidence shows she is wrong?", "A plant in the dark gives off CO<sub>2</sub>, which shows plant cells do cellular respiration too."),
     ]},
    {"id": "C", "title": "Trace a carbon atom", "lts": ["LS2-5.4"],
     "intro": "<p>A carbon atom is in a CO<sub>2</sub> molecule in the air. It enters a grass leaf, is eaten by a cow, and the cow dies and is buried and slowly becomes part of the rock.</p>",
     "items": [
         ("List the sphere at each step, in order.", "Atmosphere, biosphere (grass), biosphere (cow), geosphere (buried and in rock)."),
         ("Name the process that moves the atom at each step.", "Photosynthesis (air to grass), eating (grass to cow), burial (cow to rock)."),
         ("Write your own path for one carbon atom through at least three different spheres, naming each process.", "Example: atmosphere to biosphere by photosynthesis; biosphere to hydrosphere as a leaf is washed into a lake; hydrosphere to geosphere by burial at the bottom of the lake. Any correct path through three spheres is acceptable."),
     ]},
    {"id": "D", "title": "Using and building a model", "lts": ["LS2-5.5", "LS2-5.6"],
     "intro": "<p>A model of the carbon cycle needs all four spheres, arrows that show which way carbon moves, and labels for each process.</p>",
     "items": [
         ("Build a model in words and arrows. Include all four spheres, photosynthesis, cellular respiration, and at least one more process.", "Atmosphere to biosphere (photosynthesis); biosphere to atmosphere (respiration); atmosphere to and from hydrosphere (dissolving); biosphere to geosphere (burial); geosphere to atmosphere (burning fossil fuels)."),
         ("Predict: Ocean algae die off in a warming sea. Use your model to say what happens to carbon in the atmosphere.", "Less photosynthesis in the ocean removes less CO<sub>2</sub>, so more carbon stays in the atmosphere."),
         ("Predict: Fewer dead plants and animals are buried each year. What changes in the geosphere and the atmosphere?", "Less carbon moves into the geosphere, so more stays cycling through living things and the air, and atmospheric CO<sub>2</sub> may rise."),
         ("A model shows only an arrow from the air to plants and one from plants to the air. List two things that would make it more complete.", "Add the ocean and rocks (hydrosphere, geosphere) and processes like dissolving, burial, and burning."),
     ]},
]

WRITE = {
    "prompt": ("<p>A farmer plows up an old grassland and plants corn. Scientists measure:</p>"
               "<table border=\"1\" cellpadding=\"6\"><tr><th>Years after plowing</th><th>0</th><th>5</th><th>10</th></tr>"
               "<tr><td>Carbon stored in the soil (tons per hectare)</td><td>80</td><td>62</td><td>51</td></tr>"
               "<tr><td>Carbon released to the air each year (tons per hectare)</td><td>0</td><td>4.1</td><td>3.2</td></tr></table>"
               "<p>Write an explanation: <strong>Claim</strong> (what happened to the soil carbon), <strong>Evidence</strong> (at least two numbers), and <strong>Reasoning</strong> (name the spheres and the process, and say what would happen if the field were replanted with grass).</p>"),
    "checklist": ["States that carbon moved from the soil (geosphere) into the atmosphere",
                  "Uses at least two numbers from the table",
                  "Names the spheres involved and the process (decay and respiration by soil organisms)",
                  "Says carbon is moved, not destroyed",
                  "Predicts that replanting grass would take carbon back into plants and soil through photosynthesis"],
    "exemplar": ("The plowing moved carbon from the soil into the air. The carbon stored in the soil fell from 80 to 51 tons per hectare in 10 years, while the soil released 4.1 tons per hectare to the air in year 5. "
                 "Plowing exposes the soil, so decomposers break down dead plant matter faster and give off CO<sub>2</sub> by cellular respiration, moving carbon from the geosphere to the atmosphere. The carbon was not destroyed; it changed spheres. "
                 "If grass were replanted, photosynthesis would take CO<sub>2</sub> back out of the air into plants and, over time, into the soil."),
}
