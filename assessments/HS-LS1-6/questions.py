"""Question bank for the HS-LS1-6 assessment: From Sugar to Building Blocks.

Edit this file, then run `python3 build.py` to regenerate the Canvas QTI
package and the teacher copy.
"""

TITLE = "HS-LS1-6 Assessment: From Sugar to Building Blocks"

DESCRIPTION = (
    "<p><strong>Living Earth (Biology) &ndash; HS-LS1-6</strong></p>"
    "<p>Construct and revise an explanation based on evidence for how carbon, "
    "hydrogen, and oxygen from sugar molecules may combine with other elements "
    "to form amino acids and/or other large carbon-based molecules.</p>"
    "<p>Part 1: Vocabulary matching &middot; Part 2: Multiple choice (scenarios) "
    "&middot; Part 3: Free response</p>"
)

# ---------------------------------------------------------------------------
# Part 1: Vocabulary matching (1 point per pair)
# ---------------------------------------------------------------------------
MATCHING = {
    "title": "Part 1: Vocabulary Matching",
    "points": 8,
    "prompt": (
        "<p>Match each term with its best definition. Some definitions will "
        "not be used.</p>"
    ),
    "pairs": [
        ("Glucose",
         "A simple sugar made only of carbon, hydrogen, and oxygen that plants build during photosynthesis"),
        ("Amino acid",
         "A small carbon-based building block that contains nitrogen and links with others to form proteins"),
        ("Protein",
         "A large molecule made of long chains of amino acids folded into a specific shape"),
        ("Monomer",
         "A small molecule that can bond with others like it to build a larger molecule"),
        ("Polymer",
         "A large molecule made of many repeating smaller units bonded together"),
        ("Element",
         "A pure substance made of only one kind of atom, such as carbon or nitrogen"),
        ("Photosynthesis",
         "The process plants use to capture light energy and build sugar from carbon dioxide and water"),
        ("Conservation of matter",
         "The idea that atoms are rearranged, not created or destroyed, when molecules are built or broken down"),
    ],
    "distractors": [
        "The process cells use to break down sugar and release stored energy",
        "A mineral that plants absorb from the soil and use as their main source of carbon",
    ],
}

# ---------------------------------------------------------------------------
# Part 2: Multiple choice (2 points each). "answer" is the index of the key.
# ---------------------------------------------------------------------------
MULTIPLE_CHOICE = [
    {
        "title": "MC 1 - Nitrogen-poor cornfield",
        "dok": 2,
        "prompt": (
            "<p>A farmer plants corn in a field where the soil is very low in "
            "nitrogen. The plants get plenty of sunlight, water, and carbon "
            "dioxide. Their leaves are able to carry out photosynthesis, but "
            "the plants stay small and produce very little new tissue.</p>"
            "<p>Which explanation <strong>best</strong> accounts for the "
            "stunted growth?</p>"
        ),
        "choices": [
            "The plants can make sugar, but sugar contains only carbon, hydrogen, and oxygen, so without nitrogen they cannot build enough amino acids and proteins for new cells.",
            "Without nitrogen the plants cannot carry out photosynthesis, so they have no sugar to use for growth.",
            "Nitrogen in the soil is the main source of the carbon atoms that plants use to build the stems, leaves, and proteins of new tissue.",
            "The plants absorb amino acids directly from the soil, and this soil has run out of amino acids.",
        ],
        "answer": 0,
        "feedback": "Sugar supplies carbon, hydrogen, and oxygen, but amino acids also need nitrogen. The plants can photosynthesize but lack the nitrogen needed to turn sugar-derived atoms into amino acids and proteins.",
    },
    {
        "title": "MC 2 - Tracing labeled carbon",
        "dok": 2,
        "prompt": (
            "<p>Scientists place a bean plant in a sealed chamber containing "
            "carbon dioxide made with a special &ldquo;labeled&rdquo; form of "
            "carbon that can be tracked. They collect samples over time:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Time after exposure</th><th>Where the labeled carbon was found</th></tr>"
            "<tr><td>10 minutes</td><td>Sugar molecules in the leaves</td></tr>"
            "<tr><td>2 days</td><td>Sugar in leaves; amino acids in stems and leaves</td></tr>"
            "<tr><td>2 weeks</td><td>Proteins in leaves, fats and proteins in developing seeds</td></tr>"
            "</table>"
            "<p>Which conclusion is <strong>best supported</strong> by this evidence?</p>"
        ),
        "choices": [
            "Carbon atoms from the air were first built into sugar, and then atoms from that sugar were used to build other carbon-based molecules in the plant.",
            "The plant's proteins and fats were absorbed from the soil, and the labeled carbon only stayed in the sugar.",
            "The labeled carbon atoms were changed into nitrogen atoms so they could become part of amino acids.",
            "The plant created new carbon atoms in its seeds because seeds need more carbon than leaves.",
        ],
        "answer": 0,
        "feedback": "The timing shows the labeled carbon appearing in sugar first, then in amino acids, proteins, and fats. Atoms are rearranged, not created or changed into other elements.",
    },
    {
        "title": "MC 3 - Comparing molecular models",
        "dok": 2,
        "prompt": (
            "<p>A student compares models of three molecules found in a plant cell:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Molecule</th><th>Carbon (C)</th><th>Hydrogen (H)</th><th>Oxygen (O)</th><th>Nitrogen (N)</th><th>Sulfur (S)</th></tr>"
            "<tr><td>Glucose (a sugar)</td><td>6</td><td>12</td><td>6</td><td>0</td><td>0</td></tr>"
            "<tr><td>Glycine (an amino acid)</td><td>2</td><td>5</td><td>2</td><td>1</td><td>0</td></tr>"
            "<tr><td>Cysteine (an amino acid)</td><td>3</td><td>7</td><td>2</td><td>1</td><td>1</td></tr>"
            "</table>"
            "<p>The student claims, &ldquo;A plant can build every amino acid "
            "using only the atoms in glucose.&rdquo; Which evidence from the "
            "table <strong>best refutes</strong> this claim?</p>"
        ),
        "choices": [
            "Both amino acids contain nitrogen, and cysteine also contains sulfur, but glucose contains neither element.",
            "Glucose has more carbon atoms than either amino acid.",
            "All three molecules contain carbon, hydrogen, and oxygen.",
            "Glycine has fewer hydrogen atoms than glucose.",
        ],
        "answer": 0,
        "feedback": "Atoms cannot be created. Because glucose has no nitrogen or sulfur, those elements must come from another source (such as the soil) before amino acids can be built.",
    },
    {
        "title": "MC 4 - Hydroponic bean experiment",
        "dok": 3,
        "prompt": (
            "<p>A class grows bean plants hydroponically (in water, with no "
            "soil). All plants get the same light, temperature, and carbon "
            "dioxide. After 3 weeks they record the data below.</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Group</th><th>Nutrient solution</th><th>Sugar in leaves (mg/g)</th><th>Protein in leaves (mg/g)</th><th>Dry mass gained (g)</th></tr>"
            "<tr><td>A</td><td>Contains nitrate (a nitrogen source)</td><td>18</td><td>42</td><td>6.1</td></tr>"
            "<tr><td>B</td><td>Same as A, but no nitrogen</td><td>31</td><td>9</td><td>1.8</td></tr>"
            "</table>"
            "<p>Which explanation <strong>best</strong> uses the evidence to "
            "account for the differences between the groups?</p>"
        ),
        "choices": [
            "Both groups made sugar, but only Group A could combine atoms from sugar with nitrogen to build amino acids and proteins; Group B's unused sugar built up while growth stayed low.",
            "Group B made more sugar, so it should have grown more; the results must be caused by an error in measuring mass.",
            "Group A grew more because nitrate is a sugar that gave the plants extra energy for photosynthesis.",
            "Group B had less protein because the extra sugar in its leaves broke down the proteins it already had.",
        ],
        "answer": 0,
        "feedback": "Group B still photosynthesized (sugar is high) but lacked nitrogen, so sugar could not be converted into amino acids and proteins. Sugar piled up and new tissue (mass) was limited.",
    },
    {
        "title": "MC 5 - Bead model kit",
        "dok": 2,
        "prompt": (
            "<p>A student uses a bead kit to model molecules: black beads = "
            "carbon, white = hydrogen, red = oxygen, blue = nitrogen. She "
            "builds a model of one glucose molecule, then takes it apart to "
            "try to build amino acid models from the same beads.</p>"
            "<p>Which statement <strong>best</strong> describes what her model "
            "shows?</p>"
        ),
        "choices": [
            "She can reuse the black, white, and red beads, but she must add blue beads from outside the glucose model because amino acids contain nitrogen.",
            "She can build amino acids from only the glucose beads because atoms can change from one element into another.",
            "She must throw away the glucose beads and start over because atoms from sugar cannot be reused in other molecules.",
            "She can build amino acids from the glucose beads alone, and any leftover beads will disappear because they are no longer part of a molecule.",
        ],
        "answer": 0,
        "feedback": "The model shows conservation of matter: atoms from sugar are rearranged and reused, but a nitrogen source must be added because sugar has no nitrogen.",
    },
    {
        "title": "MC 6 - From grass to cow muscle",
        "dok": 3,
        "prompt": (
            "<p>A dairy cow eats only grass and drinks water. Over one year, "
            "the cow gains 150 kg of body mass, much of it as muscle protein.</p>"
            "<p>Which pathway <strong>best</strong> traces where most of the "
            "carbon atoms in the cow's new muscle protein originally came from?</p>"
        ),
        "choices": [
            "Carbon dioxide in the air &rarr; sugar made by grass during photosynthesis &rarr; molecules in grass eaten by the cow &rarr; broken down and rearranged into the cow's own amino acids and proteins",
            "Water the cow drinks &rarr; absorbed into the blood &rarr; converted into carbon inside the cow's muscle cells",
            "Minerals in the soil &rarr; absorbed by grass roots &rarr; stored unchanged in grass &rarr; stored unchanged in the cow's muscle",
            "Sunlight absorbed by the cow's skin &rarr; changed into carbon atoms &rarr; built into proteins",
        ],
        "answer": 0,
        "feedback": "The carbon originally came from CO2 fixed into sugar by the grass. The cow digests grass molecules and rearranges those atoms (plus nitrogen from grass proteins) into its own proteins. Water has no carbon, and light is energy, not matter.",
    },
    {
        "title": "MC 7 - Plant cell simulation",
        "dok": 3,
        "prompt": (
            "<p>In a computer simulation of a leaf cell, a student can change "
            "the light level while keeping nitrogen, water, and carbon dioxide "
            "the same. She records these results:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Light level</th><th>Sugar produced (units)</th><th>Amino acids produced (units)</th><th>Fats produced (units)</th></tr>"
            "<tr><td>High</td><td>100</td><td>40</td><td>20</td></tr>"
            "<tr><td>Medium</td><td>60</td><td>24</td><td>12</td></tr>"
            "<tr><td>Low</td><td>20</td><td>8</td><td>4</td></tr>"
            "</table>"
            "<p>Nitrogen was always available. Which explanation <strong>best</strong> "
            "accounts for why amino acid and fat production dropped as light decreased?</p>"
        ),
        "choices": [
            "Less light meant less sugar, and sugar supplies the carbon, hydrogen, and oxygen atoms the cell needs to build amino acids and fats.",
            "Light directly builds amino acids and fats, so less light means fewer of these molecules regardless of sugar.",
            "The cell used up all its nitrogen at low light, so it could not build amino acids.",
            "At low light, amino acids and fats were broken down to make more sugar.",
        ],
        "answer": 0,
        "feedback": "Nitrogen was held constant, so the limiting factor was sugar. Amino acids and fats both decreased in step with sugar because sugar provides the C, H, and O atoms used to build them.",
    },
    {
        "title": "MC 8 - Where does a tree's mass come from?",
        "dok": 2,
        "prompt": (
            "<p>A tiny acorn grows into an oak tree with a mass of several "
            "thousand kilograms. When scientists measure the soil in the pot "
            "of a young oak over 5 years, the soil loses less than 1 kg.</p>"
            "<p>Which statement <strong>best</strong> explains where most of "
            "the matter in the tree's wood, leaves, and proteins came from?</p>"
        ),
        "choices": [
            "Most came from carbon dioxide in the air and water, which the tree built into sugar and then rearranged into other large carbon-based molecules; small amounts of elements like nitrogen came from the soil.",
            "Most came from the soil, because roots absorb nutrients and minerals that are built directly into wood, leaves, and proteins as the tree grows.",
            "Most came from sunlight, which the leaves absorb and convert directly into the solid matter that makes up wood, leaves, and proteins.",
            "Most came from the acorn, which contained all of the atoms the tree would need and then expanded as the tree absorbed water.",
        ],
        "answer": 0,
        "feedback": "The soil barely changed, so it cannot be the main source. Carbon (from CO2) plus hydrogen and oxygen (from water and CO2) are built into sugar and then into other molecules. Soil supplies smaller amounts of elements like nitrogen and phosphorus.",
    },
    {
        "title": "MC 9 - Algae in a phosphorus-poor lake",
        "dok": 3,
        "prompt": (
            "<p>Two lakes receive the same amount of sunlight and have similar "
            "temperatures. Lake 1 receives runoff containing phosphorus and "
            "nitrogen from nearby farms; Lake 2 does not. Algae in both lakes "
            "carry out photosynthesis, but algae populations grow much faster "
            "in Lake 1.</p>"
            "<p>Which explanation is <strong>best supported</strong>?</p>"
        ),
        "choices": [
            "Algae in both lakes can make sugar, but only algae in Lake 1 have enough phosphorus and nitrogen to combine with atoms from sugar to build the large molecules needed for new cells.",
            "Algae in Lake 2 cannot carry out photosynthesis without phosphorus, so they make no sugar at all.",
            "Phosphorus and nitrogen give the Lake 1 algae extra carbon atoms to build sugar.",
            "Algae in Lake 2 are using their sugar to make phosphorus, which slows their growth.",
        ],
        "answer": 0,
        "feedback": "Both lakes have the light and CO2 needed to make sugar. Building new cells also requires elements like nitrogen and phosphorus that sugar does not contain, so the lake with those elements supports faster growth.",
    },
    {
        "title": "MC 10 - Revising an explanation",
        "dok": 3,
        "prompt": (
            "<p>At the start of a unit, a student wrote this explanation:</p>"
            "<blockquote>&ldquo;Plants make all of their molecules out of "
            "sunlight.&rdquo;</blockquote>"
            "<p>Since then, the class has analyzed (1) a tracer experiment "
            "showing carbon from CO<sub>2</sub> ends up in plant proteins, "
            "(2) data showing plants without nitrogen make sugar but little "
            "protein, and (3) bead models showing atoms are rearranged but "
            "never created.</p>"
            "<p>Which revision <strong>best</strong> incorporates all of this evidence?</p>"
        ),
        "choices": [
            "Plants use light energy to build sugar from CO2 and water; atoms from that sugar are rearranged and combined with elements like nitrogen from the soil to make amino acids, proteins, and other carbon-based molecules.",
            "Plants use light energy to make sugar from CO2 and water, and sugar is then stored unchanged as the only building material in every plant cell.",
            "Plants absorb proteins and other large carbon-based molecules from the soil through their roots and use light energy to store them in their cells.",
            "Plants change sunlight into new carbon atoms, and then combine those new carbon atoms with nitrogen from the soil to make amino acids and proteins.",
        ],
        "answer": 0,
        "feedback": "The best revision separates energy (light) from matter (atoms from CO2, water, and soil) and explains that sugar's atoms are rearranged and combined with other elements such as nitrogen.",
    },
]

# ---------------------------------------------------------------------------
# Part 3: Free response (DOK 3, 6 points each)
# ---------------------------------------------------------------------------
FREE_RESPONSE = [
    {
        "title": "FR 1 - Yellow lettuce in the greenhouse",
        "dok": 3,
        "points": 6,
        "prompt": (
            "<p>A greenhouse grower raises two batches of lettuce. Both get "
            "the same light, water, carbon dioxide, and temperature. Batch 1 "
            "receives a nitrogen fertilizer; Batch 2 does not. After 4 weeks "
            "she measures the plants:</p>"
            "<table border=\"1\" cellpadding=\"4\">"
            "<tr><th>Measurement</th><th>Batch 1 (nitrogen)</th><th>Batch 2 (no nitrogen)</th></tr>"
            "<tr><td>Leaf color</td><td>Dark green</td><td>Pale yellow</td></tr>"
            "<tr><td>Average head mass (g)</td><td>310</td><td>95</td></tr>"
            "<tr><td>Sugar in leaves (mg/g)</td><td>15</td><td>28</td></tr>"
            "<tr><td>Protein in leaves (mg/g)</td><td>38</td><td>7</td></tr>"
            "</table>"
            "<p>The grower is confused: &ldquo;Batch 2 has <em>more</em> sugar. "
            "If plants use sugar to grow, why is it so much smaller?&rdquo;</p>"
            "<p>Write a scientific explanation for the grower using "
            "<strong>Claim, Evidence, and Reasoning</strong>:</p>"
            "<ol>"
            "<li><strong>Claim:</strong> Explain why Batch 2 is smaller even though it has more sugar.</li>"
            "<li><strong>Evidence:</strong> Use at least <strong>two</strong> specific pieces of data from the table.</li>"
            "<li><strong>Reasoning:</strong> Explain how the carbon, hydrogen, and oxygen in sugar combine with other elements to build the molecules a plant needs to grow. Include why the sugar built up in Batch 2.</li>"
            "<li><strong>Prediction:</strong> Predict what would happen to the sugar and protein levels in Batch 2 if the grower began adding nitrogen fertilizer, and explain why.</li>"
            "</ol>"
        ),
        "rubric": [
            ("Claim (1 pt)", "States that Batch 2 lacked nitrogen, so it could not turn its sugar into amino acids/proteins needed to build new tissue."),
            ("Evidence (2 pts)", "Cites at least two accurate data points (e.g., protein 38 vs. 7 mg/g; mass 310 vs. 95 g; sugar 15 vs. 28 mg/g; yellow vs. green leaves). 1 pt per relevant data point, max 2."),
            ("Reasoning (2 pts)", "1 pt: Sugar contains only C, H, and O; amino acids/proteins also need nitrogen, which must come from the soil/fertilizer. 1 pt: Atoms from sugar are rearranged and combined with nitrogen to build amino acids (and other large carbon-based molecules); without nitrogen, sugar is not used and accumulates."),
            ("Prediction (1 pt)", "Predicts sugar will decrease and protein (and mass) will increase, because sugar's atoms will now be combined with nitrogen to build amino acids/proteins."),
        ],
        "exemplar": (
            "Batch 2 is smaller because it did not have nitrogen, so it could not use its sugar to build proteins for new cells. "
            "Batch 2 had only 7 mg/g of protein compared to 38 mg/g in Batch 1, and its heads were only 95 g compared to 310 g, even though it had more sugar (28 vs. 15 mg/g). "
            "Photosynthesis makes sugar, which only contains carbon, hydrogen, and oxygen. To build amino acids, the plant rearranges atoms from sugar and combines them with nitrogen from the soil or fertilizer. "
            "The amino acids link into proteins that build new cells. Without nitrogen, Batch 2 kept making sugar but could not convert it, so the sugar built up while growth stayed low. "
            "If nitrogen is added, I predict sugar levels will drop and protein and mass will rise, because the stored sugar will be used with the new nitrogen to make amino acids and proteins."
        ),
    },
    {
        "title": "FR 2 - Revise the chicken explanation",
        "dok": 3,
        "points": 6,
        "prompt": (
            "<p>A student wrote this explanation about a chicken that eats only corn:</p>"
            "<blockquote>&ldquo;The chicken's muscle proteins come straight from "
            "the corn. The chicken eats corn protein and stores it in its "
            "muscles without changing it.&rdquo;</blockquote>"
            "<p>Scientists then collected the following evidence:</p>"
            "<ul>"
            "<li><strong>Tracer study:</strong> Corn plants were grown with labeled carbon dioxide. The labeled carbon showed up first in corn <em>sugar</em>, then in corn starch and corn proteins. After a chicken ate the corn, the labeled carbon appeared in the chicken's muscle proteins.</li>"
            "<li><strong>Protein comparison:</strong> The order of amino acids in chicken muscle protein is very different from the order in any corn protein.</li>"
            "<li><strong>Model:</strong> In a bead-model activity, students broke apart models of corn molecules and rebuilt the same beads into different molecules. No beads were added or lost, except that blue (nitrogen) beads had to come from the corn's proteins.</li>"
            "</ul>"
            "<p>Using this evidence:</p>"
            "<ol>"
            "<li><strong>Evaluate:</strong> Identify which part of the student's explanation is supported and which part is <em>not</em> supported. Cite evidence for each.</li>"
            "<li><strong>Revise:</strong> Write an improved explanation that traces carbon atoms from the <em>air</em> to the <em>chicken's muscle</em>. Your explanation must describe how carbon, hydrogen, and oxygen from sugar combine with other elements (such as nitrogen) to form amino acids and proteins.</li>"
            "<li><strong>Connect:</strong> Explain how the bead model supports the idea that matter is conserved during this process.</li>"
            "</ol>"
        ),
        "rubric": [
            ("Evaluate (2 pts)", "1 pt: Supported part - the atoms in chicken protein do come from the corn (tracer carbon moved from corn to chicken muscle). 1 pt: Unsupported part - the protein is not stored unchanged; chicken protein has a different amino acid order, so the corn molecules were broken down and rebuilt."),
            ("Revise (3 pts)", "1 pt: Traces carbon from CO2 in air into corn sugar by photosynthesis. 1 pt: Explains that C, H, and O from sugar combine with nitrogen (from soil in corn; from eaten protein in the chicken) to form amino acids. 1 pt: Explains the chicken breaks down corn molecules and rearranges the atoms/amino acids into its own new proteins."),
            ("Connect (1 pt)", "Explains that the bead model shows atoms are rearranged into new molecules without being created or destroyed, so the same atoms move from air to corn to chicken."),
        ],
        "exemplar": (
            "The student is partly right: the atoms in the chicken's muscle protein do come from the corn, because the labeled carbon traveled from the corn into the chicken's muscle. "
            "But the chicken does not store corn protein unchanged, because the amino acid order in chicken protein is very different from any corn protein. "
            "Revised explanation: The corn takes in carbon dioxide from the air and uses light energy to build sugar during photosynthesis. The corn then rearranges the carbon, hydrogen, and oxygen atoms from sugar and combines them with nitrogen from the soil to make amino acids, which link into corn proteins (and it also makes starch). "
            "When the chicken eats the corn, it breaks those molecules down into smaller pieces like amino acids and sugars. The chicken's cells then rearrange those atoms and build its own amino acid chains in a new order, making chicken muscle protein. "
            "The bead model supports this because the same beads were taken apart and rebuilt into different molecules with none added or lost, showing atoms are conserved - they are only rearranged."
        ),
    },
]
