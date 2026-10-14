"""Unit review for HS-LS1-6 (unit 1.3). Done on the review day, built around the CFAs (no practice test).

Department note: never ask students to identify or classify a macromolecule, and never say amino acids
or proteins are only C, H, and O.
"""

STANDARD = "HS-LS1-6"
UNIT_TITLE = "Sugar to Structures"
GOAL = ("Explain, using evidence, how carbon, hydrogen, and oxygen from sugar combine with other elements "
        "to build amino acids and other large carbon-based molecules, and revise your explanation when new evidence comes in.")

KEY_IDEAS = [
    "<strong>Sugar is made of only carbon, hydrogen, and oxygen.</strong> Plants build sugar from CO<sub>2</sub> and water using light energy. Light is energy, not matter.",
    "<strong>Amino acids also contain nitrogen</strong> (some contain sulfur). Nitrogen and sulfur are not in sugar, so they come from somewhere else, such as the soil.",
    "<strong>Atoms are conserved.</strong> They are rearranged, never created, destroyed, or changed into another element.",
    "<strong>Atoms from sugar are rearranged and combined with other elements</strong> to build larger molecules.",
    "<strong>Matter moves through food chains.</strong> An animal breaks food down and rebuilds its atoms into its own molecules.",
    "<strong>Scientists revise explanations</strong> when new evidence does not fit.",
]

VOCAB = {
    "bank": ["atom", "element", "glucose", "amino acid", "photosynthesis", "conservation of matter"],
    "blanks": [
        ("During ____________, a plant uses light energy to build sugar from carbon dioxide and water.", "photosynthesis"),
        ("The sugar a plant makes, ____________, contains only carbon, hydrogen, and oxygen.", "glucose"),
        ("Carbon and nitrogen are each an ____________, a pure substance made of only one kind of ____________.", "element; atom"),
        ("An ____________ is a small building block of proteins that contains nitrogen.", "amino acid"),
        ("The idea that atoms are rearranged but never created or destroyed is called ____________.", "conservation of matter"),
    ],
}

SECTIONS = [
    {"id": "A", "title": "Elements in sugar and other molecules", "lts": ["LS1-6.1"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Molecule</th><th>C</th><th>H</th><th>O</th><th>N</th><th>S</th></tr><tr><td>Glucose (sugar)</td><td>6</td><td>12</td><td>6</td><td>0</td><td>0</td></tr><tr><td>Serine (amino acid)</td><td>3</td><td>7</td><td>3</td><td>1</td><td>0</td></tr><tr><td>Methionine (amino acid)</td><td>5</td><td>11</td><td>2</td><td>1</td><td>1</td></tr></table>",
     "items": [
         ("Which three elements make up sugar?", "Carbon, hydrogen, and oxygen."),
         ("Which element(s) does each amino acid in the table have that sugar does not?", "Serine has nitrogen. Methionine has nitrogen and sulfur."),
         ("Where would a plant get nitrogen and sulfur?", "From the soil (taken in by the roots), including from fertilizer."),
     ]},
    {"id": "B", "title": "Atoms are conserved", "lts": ["LS1-6.2"],
     "intro": "<p>Use the idea of conservation of matter.</p>",
     "items": [
         ("A student takes apart a bead model of glucose and uses the beads to build other molecules. What must be true about the number of each color of bead before and after?", "The number of each color stays the same. Beads (atoms) are rearranged and none are created or lost."),
         ("A classmate says, &ldquo;The plant can turn some carbon into nitrogen.&rdquo; Explain why this is wrong.", "Atoms are conserved and cannot change from one element to another. Nitrogen has to come from an outside source."),
         ("True or false: Most of a tree's mass comes from the soil. Explain.", "False. Most comes from CO<sub>2</sub> in the air and water, rearranged into sugar and other molecules. The soil supplies small amounts of elements like nitrogen."),
     ]},
    {"id": "C", "title": "Combining atoms from sugar with other elements", "lts": ["LS1-6.3", "LS1-6.4"],
     "intro": "<p>Bead model: black = carbon, white = hydrogen, red = oxygen, blue = nitrogen.</p>",
     "items": [
         ("You want to build an amino acid from a glucose model. Which beads can you reuse and which must you add?", "Reuse black, white, and red (C, H, O). Add blue (nitrogen) beads, because glucose has no nitrogen."),
         ("You have red and white beads left over. What does that show?", "Not every atom from sugar goes into the amino acid. The leftover atoms are conserved and can be used in other molecules."),
         ("A rabbit eats clover. Trace one carbon atom from the air to the rabbit's muscle.", "CO<sub>2</sub> in the air, built into sugar by the clover (photosynthesis), rearranged with nitrogen into the clover's amino acids and proteins, eaten by the rabbit, broken down, and rebuilt into the rabbit's own proteins."),
     ]},
    {"id": "D", "title": "Using evidence and revising", "lts": ["LS1-6.5", "LS1-6.6"],
     "intro": "<table border=\"1\" cellpadding=\"6\"><tr><th>Plant group</th><th>Nitrogen added?</th><th>Sugar (mg/g)</th><th>Protein (mg/g)</th></tr><tr><td>A</td><td>Yes</td><td>14</td><td>40</td></tr><tr><td>B</td><td>No</td><td>30</td><td>8</td></tr></table>",
     "items": [
         ("What does the table show about Group B? Use numbers.", "Group B made more sugar (30 vs. 14 mg/g) but much less protein (8 vs. 40 mg/g)."),
         ("Explain why Group B has so much sugar but so little protein.", "Without nitrogen, Group B cannot combine atoms from sugar with nitrogen to build amino acids and proteins, so sugar builds up."),
         ("A student wrote, &ldquo;Plants make all their molecules from sunlight.&rdquo; New evidence: labeled carbon from CO<sub>2</sub> ends up in plant proteins. Revise her explanation.", "Plants use light energy to build sugar from CO<sub>2</sub> and water; atoms from that sugar are rearranged and combined with elements like nitrogen from the soil to build proteins. Light is energy, not matter."),
         ("Another student says plants without nitrogen cannot do photosynthesis. Use the table to revise her statement.", "Group B has high sugar, so it still does photosynthesis. Nitrogen is needed to build proteins, not to make sugar."),
     ]},
]

WRITE = {
    "prompt": ("<p>A farmer grows two fields of wheat. Both get the same light, water, and CO<sub>2</sub>. Field 1 has sulfur-rich soil. Field 2 has sulfur-poor soil.</p>"
               "<table border=\"1\" cellpadding=\"6\"><tr><th></th><th>Field 1</th><th>Field 2</th></tr>"
               "<tr><td>Sugar in leaves (mg/g)</td><td>16</td><td>27</td></tr>"
               "<tr><td>Protein in grain (percent)</td><td>13</td><td>6</td></tr>"
               "<tr><td>Grain yield (tons per hectare)</td><td>7.5</td><td>3.1</td></tr></table>"
               "<p>Write an explanation: <strong>Claim</strong>, <strong>Evidence</strong> (at least two numbers), and <strong>Reasoning</strong> (how atoms from sugar combine with other elements to build the molecules needed to grow). Then predict what happens if sulfur is added to Field 2.</p>"),
    "checklist": ["States that the lack of sulfur limited building proteins even though sugar was made",
                  "Uses at least two numbers (sugar and protein or yield)",
                  "Says sugar has only C, H, and O, and sulfur has to come from the soil",
                  "Says atoms from sugar are rearranged and combined with sulfur (and other elements) to build the molecules for growth",
                  "Explains why sugar built up and predicts sugar drops and protein and yield rise after adding sulfur"],
    "exemplar": ("Field 2 grew less because it lacked sulfur, so it could not turn its sugar into the proteins needed to grow. Field 2 had more sugar (27 vs. 16 mg/g) but less protein (6% vs. 13%) and a lower yield (3.1 vs. 7.5 tons per hectare). "
                 "Sugar contains only carbon, hydrogen, and oxygen. To build some amino acids, the plant combines atoms from sugar with sulfur and nitrogen from the soil. Without sulfur, Field 2's sugar could not be used, so it built up. "
                 "If sulfur were added, the sugar would be used to build amino acids and proteins, so sugar would drop and protein and yield would rise."),
}
