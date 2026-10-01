"""Unit 1.3 Sugar to Structures (HS-LS1-6): the 10-day lesson sequence.

Each day becomes a student Canvas page and an unpublished teacher page, laid out
like Earth Science Unit 3. The lessons are the Giant Pumpkin Mystery lessons
(slides and handouts in Drive, Unit 1.3 Sugar to Structures folder), plus a new
Day 2 (vocabulary and SketchNotes), a practice test and review day, and a CSA day.
Each CFA sits at the end of the lesson that teaches its target.

  Day 1   Lesson 1  The Giant Pumpkin Mystery (phenomenon, unit CER starts)
  Day 2   new       Vocabulary and SketchNotes
  Day 3   Lesson 2  What Are Living Things Made Of?        CFA LS1-6.1
  Day 4   Lesson 3  Building Sugar from Air and Water      CFA LS1-6.2
  Day 5   Lesson 4  From Sugar to Amino Acids              CFA LS1-6.3
  Day 6   Lesson 5  Small Pieces, Big Molecules            CFA LS1-6.4
  Day 7   Lesson 6  What's the Evidence?                   CFA LS1-6.5
  Day 8   Lesson 7  Solving the Pumpkin Mystery            CFA LS1-6.6 (unit CER finished)
  Day 9   new       Practice Test and Review
  Day 10  new       Unit 1.3 CSA
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import unit13_bank as U  # noqa: E402

DRIVING_Q = "How does a plant build its body, and what is it built from?"
SLIDES = "https://docs.google.com/presentation/d/{}/edit"
FILE = "https://drive.google.com/file/d/{}/view"
FOLDER = "https://drive.google.com/drive/folders/1yvFf77Y0j9kt4Do091Hh39gqWNj5G00x"
BOX = "background:#eef5fb;border-left:5px solid #2b6cb0;padding:10px 14px;margin:12px 0"
TBOX = "background:#fff7e6;border-left:5px solid #c05621;padding:10px 14px;margin:12px 0"
TABLE = '<table border="1" cellpadding="6" style="border-collapse:collapse"><tbody>{}</tbody></table>'


def table(header, *rows):
    th = "<tr>" + "".join(f"<th>{h}</th>" for h in header) + "</tr>"
    return TABLE.format(th + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows))


def ol(*items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


CER_LOG = ("<strong>Unit CER evidence log:</strong> add one row: the day, one piece of evidence from today, "
           "and what it shows about where the pumpkin's matter comes from.")

DAYS = [
    # ------------------------------------------------------------------ Day 1
    dict(
        day=1, title="The Giant Pumpkin Mystery", lesson="Lesson 1", targets=["LS1-6.1"],
        focus="Where does a pumpkin's mass come from?",
        slides=("Lesson 1: The Giant Pumpkin Mystery", SLIDES.format("17tM_2j5SNPC2nMr5QKLGKWgArevjOlpIHWCArKJetF8")),
        handout=FILE.format("1Ai4IWRnVIQkW1X5ias4d5ZZWz-4jFsIf"),
        notebook=[
            "Title: <strong>D1 The Giant Pumpkin Mystery</strong>. Add it to your table of contents.",
            "Fill in the phenomenon page from the slides: I notice / I wonder, your initial model, the source ranking, and the element table.",
            "Start your <strong>Unit CER</strong> on a new page. Write the question <em>Where does a giant pumpkin's mass come from?</em>, "
            "your first claim, and a 3-column evidence log (Day · Evidence · What it shows). You'll add a row every day.",
        ],
        sections=[
            ("The phenomenon", "<p>A giant pumpkin seed weighs less than 1 gram. About four months later, the pumpkin can weigh more than "
             "1,200 kg, about as much as a small car. About 90% of a fresh pumpkin is water. The other 10%, about 120 kg, is sugars, "
             "fiber, proteins, fats, and other molecules. Where did all that matter come from?</p>"),
            ("Your initial model", "<p>Draw the pumpkin plant with its leaves, roots, soil, and the air around it. Use arrows to show where you "
             "think its matter came from. Rank the six sources (soil, water, air, sunlight, fertilizer, the seed) from 1 (most mass) to 6 (least).</p>"),
            ("Test the sources with element data", "<p>A dry pumpkin is 45% carbon, 42% oxygen, 6% hydrogen, and 3% nitrogen. Soil is mostly "
             "oxygen, silicon, and aluminum. Use the tables to decide which sources could supply the pumpkin's elements, then re-rank.</p>"),
            ("Driving question board", f"<p><strong>{DRIVING_Q}</strong> Write 2–3 questions you'd need to answer. Post each on a sticky note.</p>"),
            ("Exit ticket: your first claim", "<p>Which source do you now think provides most of the pumpkin's mass? Why? "
             "Copy this as the first claim in your Unit CER.</p>"),
        ],
        cfa=None,
        teacher=dict(
            glance="Launch. Students meet the phenomenon, draw an initial model, test sources against element data, and build the driving "
                   "question board. The unit CER (Where does a giant pumpkin's mass come from?) starts today and is finished on Day 8.",
            materials="Lesson 1 slides; notebooks (or the Lesson 1 handout); sticky notes; chart paper for the driving question board.",
            agenda=[("0–5", "The phenomenon: I notice / I wonder"), ("5–15", "Initial model and source ranking"),
                    ("15–22", "Share in groups; class poll"), ("22–35", "Element data (Tables 1–4)"),
                    ("35–42", "Driving question board; set up the Unit CER page"), ("42–45", "Exit ticket = first claim")],
            notes=[
                "No CFA today. The exit ticket becomes each student's first claim on the Unit CER page.",
                "Keep the class poll results and the driving question board; students revisit both on Days 8 and 9.",
                "Nitrogen gas (N₂) is 78% of air, but plants can't use N₂ directly. If students list air as the nitrogen source, "
                "note it and come back to it on Day 5 (soil nitrogen).",
            ],
            key=ul("Most of the dry pumpkin: carbon (45%) and oxygen (42%).",
                   "Silicon is less than 1% and aluminum almost 0% of the pumpkin, but 28% and 8% of soil, so soil can't be the main source.",
                   "Sources: C from air (CO₂), a little in soil · H from water · O from air (CO₂, O₂), water, and soil · N from soil (and air, which plants can't use directly).",
                   "50 kg of carbon from 0.04% CO₂: leaves take in huge volumes of air, all day, for months.",
                   "Expected re-ranking: air and water move to the top; soil, fertilizer, and the seed drop; sunlight is energy, not matter."),
            supports="Sentence frames are on the slides and handout. Pair students for the element-data questions.",
        ),
    ),
    # ------------------------------------------------------------------ Day 2
    dict(
        day=2, title="Vocabulary and SketchNotes", lesson="New", targets=["LS1-6.1", "LS1-6.2", "LS1-6.3"],
        focus="What words and big ideas will we need to solve the pumpkin mystery?",
        slides=("Day 2 Vocabulary and SketchNotes", SLIDES.format("1SakPKw-q29gXMRUfa0g7DF0myjJ3qIO-bjUgRttQLR8")),
        handout=None,
        notebook=[
            "Title: <strong>D2 Vocabulary</strong>. Add it to your table of contents.",
            "Make 10 Frayer models, 2 per page (5 pages): definition in your own words, facts, examples, non-examples. Draw at least one example for each word.",
            "Title the next page <strong>D2 SketchNotes: Sugar to Structures</strong>. Fill ½ to 1 page with the 5 big ideas as short phrases and icons.",
            "Title the next page <strong>The Pumpkin Path</strong> (sensemaking). Draw the plant, its sources, and arrows. You'll add to this page after every lesson.",
        ],
        sections=[
            ("Do Now", "<p>Rate each word from 1 (never heard it) to 4 (I could teach it).</p>"),
            ("Frayer models: 10 words", table(
                ["Word", "Definition"],
                ["Atom", "The smallest piece of an element that still acts like that element"],
                ["Element", "A pure substance made of only one kind of atom (C, H, O, N, …)"],
                ["Molecule", "Two or more atoms bonded together, like CO₂ or H₂O"],
                ["Conservation of matter", "Atoms are rearranged, never created, destroyed, or changed into other elements"],
                ["Photosynthesis", "Plants use light energy to build sugar from CO₂ and water, releasing O₂"],
                ["Glucose", "A sugar (C₆H₁₂O₆) that stores energy and supplies atoms for building"],
                ["Amino acid", "A building block of proteins; it has C, H, O, and N"],
                ["Protein", "A large molecule made of amino acids linked in a specific order"],
                ["Monomer", "A small molecule that can link with others like it"],
                ["Polymer", "A large molecule made of many linked monomers"])),
            ("SketchNotes: the 5 big ideas", ol(
                "Living things are made mostly of C, H, and O, plus a little N, P, and S.",
                "Atoms are rearranged into new molecules. They are never created or destroyed.",
                "Plants build sugar from CO₂ and water. Light is the energy, not the matter.",
                "Atoms from sugar join with nitrogen from the soil to build amino acids, which link into proteins.",
                "Animals eat, break molecules down, and rebuild the atoms into their own molecules.")),
            ("Sensemaking: the Pumpkin Path", "<p>Draw the pumpkin plant with the air, water, soil, and sunlight. Use solid arrows for matter "
             "and dashed arrows for energy. Label where sugar is built and where nitrogen comes in. After each lesson, add one new idea or piece of evidence.</p>"),
            ("Exit ticket", "<p>Use 3 vocabulary words to answer: Where do you think most of the pumpkin's matter comes from? Underline the 3 words.</p>"),
        ],
        cfa=None,
        teacher=dict(
            glance="Vocabulary and SketchNotes day, front-loading the 10 words and 5 big ideas the lessons build on. The SketchNotes are a preview; "
                   "the Pumpkin Path sensemaking page grows after each lesson and becomes a study tool on Day 9.",
            materials="Day 2 slides; notebooks; colored pencils. Optional: a printed word list for students who need it.",
            agenda=[("0–3", "Do Now: rate the 10 words"), ("3–8", "Model one Frayer (atom) together"),
                    ("8–25", "Frayer models for all 10 words"), ("25–35", "SketchNotes: 5 big ideas"),
                    ("35–42", "Sensemaking: the Pumpkin Path"), ("42–45", "Exit ticket")],
            notes=[
                "Same 10 words as the vocabulary on the old CSA matching section, so this also covers the vocabulary piece of the unit.",
                "To save time, let students write the given definition first and reword it later; examples and non-examples matter more.",
                "Collect the Do Now ratings and compare them with the Day 9 self-ratings.",
            ],
            key=ul("Good non-examples: atom (a cell, sunlight) · element (water, a molecule made of two elements) · molecule (a single atom, light) · "
                   "photosynthesis (cellular respiration, absorbing water) · glucose (protein, fertilizer) · amino acid (glucose, a whole protein) · "
                   "protein (a single amino acid, starch) · monomer (a polymer such as starch) · polymer (one glucose or one amino acid)."),
            supports="Provide the word list with definitions for students with IEPs/504s or English learners; they still complete examples, non-examples, and sketches.",
        ),
    ),
    # ------------------------------------------------------------------ Day 3
    dict(
        day=3, title="What Are Living Things Made Of?", lesson="Lesson 2", targets=["LS1-6.1", "LS1-6.2"],
        focus="Which elements make up the molecules of life, and where could a plant get them?",
        slides=("Lesson 2: What Are Living Things Made Of?", SLIDES.format("1xD36Y-QqwdvhmE8EQXBZGkN-qBNUNDJlT91reKUuRwM")),
        handout=FILE.format("1Yr8aG_aEqOTw2zAsyiwfNEAljeeKXjez"),
        notebook=[
            "Title: <strong>D3 What Are Living Things Made Of?</strong> Add it to your table of contents.",
            "Record the sealed-bag demo table, the formula counts, the molecule card sort, and the atom accounting rule.",
            CER_LOG,
        ],
        sections=[
            ("Warm-up", "<p>Is a carbon atom in a pumpkin different from a carbon atom in the air? Explain.</p>"),
            ("Sealed-bag demo", "<p>Record the mass before and after tipping the cup, then after opening the bag. "
             "<strong>Conservation of matter:</strong> atoms are rearranged into new molecules. They are never created, destroyed, or changed into a different element.</p>"),
            ("Reading formulas", "<p>C₆H₁₂O₆ has 6 carbon, 12 hydrogen, and 6 oxygen atoms. Count the atoms in CO₂, H₂O, and C₆H₁₂O₆.</p>"),
            ("Molecule card sort", "<p>Count the atoms on each of the 11 cards, sort them by which elements they contain, and decide which molecules a plant "
             "could build from only CO₂ and water.</p>"),
            ("The atom accounting rule", "<p>As a class, write one rule for deciding whether a plant can build a molecule. Copy it into your notebook.</p>"),
        ],
        cfa="LS1-6.1",
        teacher=dict(
            glance="Atoms and elements. The sealed-bag demo grounds conservation of matter; the card sort shows that sugar's elements (C, H, O) can't "
                   "build anything with N or P. CFA LS1-6.1 closes the lesson.",
            materials="Lesson 2 slides and handout (cards on the last page, 1 set per group); sealed-bag demo (zip bag, cup, baking soda, vinegar, balance) "
                      "or the sealed-bag demo video in the Unit 1.3 Drive folder; Chromebooks for the CFA.",
            agenda=[("0–5", "Warm-up"), ("5–11", "Sealed-bag demo"), ("11–15", "Reading formulas"),
                    ("15–31", "Molecule card sort (count, sort, apply)"), ("31–36", "Atom accounting rule"),
                    ("36–39", "Exit ticket (glucose vs. histidine)"), ("39–45", "CFA LS1-6.1 (slide at the end of the deck)")],
            notes=[
                "Minutes are trimmed from the original 45-minute plan to fit the 6-minute CFA. If time runs short, do the exit ticket orally.",
                "Students below a B on the CFA get the LS1-6.1 review on Canvas automatically (Mastery Path).",
            ],
            key=ul(
                "Sealed bag: mass stays the same while sealed (no atoms leave); drops after opening because CO₂ gas escapes. No atoms are destroyed.",
                "CO₂: 1 C, 2 O · H₂O: 2 H, 1 O · C₆H₁₂O₆: 6 C, 12 H, 6 O.",
                "Cards: glucose and fructose C₆H₁₂O₆ · sucrose C₁₂H₂₂O₁₁ · cellulose unit C₆H₁₀O₅ · oleic acid C₁₈H₃₄O₂ · beta-carotene C₄₀H₅₆ · "
                "valine C₅H₁₁NO₂ · lysine C₆H₁₄N₂O₂ · tryptophan C₁₁H₁₂N₂O₂ · AMP C₁₀H₁₄N₅O₇P · chlorophyll a C₅₅H₇₂MgN₄O₅.",
                "Groups: C, H, O only (cards 1–5) · C and H only (6) · C, H, O, N (7–9) · C, H, O, N, P (10) · C, H, O, N, Mg (11).",
                "From only CO₂ and H₂O: cards 1–6. Need other elements: 7–9 (N), 10 (N, P), 11 (N, Mg), from the soil.",
                "Carbon can't turn into nitrogen: atoms are never changed into other elements (the bag's mass shows atoms are conserved).",
                "Exit ticket: disagree. Histidine has 3 N; glucose has 0 N. Atoms can't be created, so the N must come from the soil.",
            ),
            supports="Assign each group member specific cards to count. Sentence frames on the slides and handout.",
        ),
    ),
    # ------------------------------------------------------------------ Day 4
    dict(
        day=4, title="Building Sugar from Air and Water", lesson="Lesson 3", targets=["LS1-6.2"],
        focus="Where do the atoms in sugar come from, and what does light do?",
        slides=("Lesson 3: Building Sugar from Air and Water", SLIDES.format("1eJKaJgqK0YgDJ3YA_qJKm99gpPedl4CcBoXNR-K9ZqQ")),
        handout=FILE.format("1VNnbigr9yBPgX-adcan2KsGvfiRvp9JQ"),
        notebook=[
            "Title: <strong>D4 Building Sugar from Air and Water</strong>. Add it to your table of contents.",
            "Record the leaf-chamber data answers, the bead-model Before/After table, and the energy-or-matter sort.",
            "Save your 2 glucose bead models in your labeled bag for Day 5.",
            CER_LOG,
        ],
        sections=[
            ("Warm-up", "<p>Is sunlight matter? Could sunlight become part of the pumpkin?</p>"),
            ("A pumpkin leaf in a sealed chamber", "<p>In the light, CO₂ dropped from 420 to 300 ppm in 20 minutes. In the dark, it rose from 420 to 470 ppm. "
             "Where did the carbon go in the light?</p>"),
            ("Photosynthesis: the big idea", "<p>Carbon dioxide and water supply the <strong>atoms</strong>. Light supplies the <strong>energy</strong> to rearrange them "
             "into glucose; oxygen gas is released.</p>"),
            ("Build sugar with beads", "<p>Build 6 CO₂ and 6 H₂O, count, then rebuild the same beads into 1 glucose and 6 O₂ while the LIGHT ENERGY card is out. "
             "Count again. Build a second glucose and save both.</p>"),
            ("Energy or matter?", "<p>Sort sunlight, CO₂, water, glucose, oxygen gas, heat, nitrogen in fertilizer, and chlorophyll.</p>"),
        ],
        cfa="LS1-6.2",
        teacher=dict(
            glance="Photosynthesis as atom rearrangement. Leaf-chamber data, then a bead model with before/after atom counts (conservation), then matter vs. "
                   "energy. CFA LS1-6.2 closes the lesson.",
            materials="Lesson 3 slides and handout; beads (black, white, red), pipe cleaners, labeled bags, LIGHT ENERGY cards; Chromebooks.",
            agenda=[("0–4", "Warm-up"), ("4–10", "Leaf-chamber data"), ("10–14", "Photosynthesis: the big idea"),
                    ("14–32", "Bead model, rounds 1 and 2"), ("32–36", "Energy or matter?"),
                    ("36–39", "Exit ticket"), ("39–45", "CFA LS1-6.2")],
            notes=["Make sure every pair bags 2 glucose models; Day 5 depends on them. Keep spares for absent students.",
                   "The CFA includes atom counting (photosynthesis oxygen count; two glucose joining and releasing water). The bead table is good practice for it."],
            key=ul("Light: CO₂ fell 420 → 300 ppm (120 ppm in 20 min). Dark: rose 420 → 470 ppm (cellular respiration).",
                   "The carbon went into sugar (glucose) in the leaf. Light had to be present.",
                   "Beads before = after: 6 black (C), 12 white (H), 18 red (O), 36 total.",
                   "C came from CO₂, H from water, the extra O left as O₂. The light card never became beads: it stands for energy.",
                   "Matter: CO₂, water, glucose, oxygen gas, nitrogen in fertilizer, chlorophyll. Energy: sunlight, heat.",
                   "Exit ticket: CO₂ and water supply the atoms; light supplies the energy; sunlight does not become part of the sugar."),
            supports="Pre-count bead bags for pairs who need it. Let students point to bead colors as they explain.",
        ),
    ),
    # ------------------------------------------------------------------ Day 5
    dict(
        day=5, title="From Sugar to Amino Acids", lesson="Lesson 4", targets=["LS1-6.3", "LS1-6.4"],
        focus="How can a plant turn sugar into amino acids?",
        slides=("Lesson 4: From Sugar to Amino Acids", SLIDES.format("1uMGH58CJ-PGAOWvFJJOtj08df_M0AtiBVRFrrxXCGYU")),
        handout=FILE.format("1qff5is2qHqgSV6771int-volqu3GDN8k"),
        notebook=[
            "Title: <strong>D5 From Sugar to Amino Acids</strong>. Add it to your table of contents.",
            "Record the bead lab table (Start, Added from soil, Total available, In valine, In threonine, Recycle tray, Total at end) and draw the atoms you end up with.",
            CER_LOG,
        ],
        sections=[
            ("Warm-up", "<p>Glucose is C₆H₁₂O₆. Valine is C₅H₁₁NO₂. Could you build valine using only the beads in your glucose bag?</p>"),
            ("The amino acid recipe", "<p>Every amino acid has the same backbone (2 C, 4 H, 2 O, 1 N) plus a side chain that makes it unique.</p>"),
            ("Bead lab", "<p>Take apart your 2 glucose models. Build valine and threonine, taking blue (nitrogen) beads from the soil cup only when you need them. "
             "Unused beads go in the recycle tray. Count everything.</p>"),
            ("Atom accounting", "<p>Which colors came from glucose, and which from the soil? Does \"Total available\" match \"Total at end\"?</p>"),
        ],
        cfa="LS1-6.3",
        teacher=dict(
            glance="Sugar plus nitrogen makes amino acids. Students rebuild Day 4's glucose beads into valine and threonine, adding nitrogen from the soil cup. CFA LS1-6.3 closes the lesson.",
            materials="Lesson 4 slides and handout; students' glucose bags from Day 4; blue beads (soil cup); recycle trays; spare glucose models; Chromebooks.",
            agenda=[("0–4", "Warm-up"), ("4–10", "The amino acid recipe"), ("10–29", "Bead lab"),
                    ("29–36", "Atom accounting and discussion"), ("36–39", "Exit ticket (is fertilizer plant food?)"), ("39–45", "CFA LS1-6.3")],
            notes=["The lysine challenge is for early finishers only.",
                   "The fertilizer exit ticket sets up the Day 8 grower explanation; keep the answers."],
            key=ul("Start (2 glucose): 12 C, 24 H, 12 O, 0 N = 48. Added from soil: 2 N. Total available: 50.",
                   "Valine C₅H₁₁NO₂ (19 beads); threonine C₄H₉NO₃ (17 beads). Recycle tray: 3 C, 4 H, 7 O = 14. Total at end: 50.",
                   "Lysine challenge: extra glucose + tray = 9 C, 16 H, 13 O; lysine (C₆H₁₄N₂O₂) needs 2 blue beads; left over 3 C, 2 H, 11 O.",
                   "Black, white, red came from glucose; blue came from the soil cup. No amino acid can be built from glucose alone because every one needs N.",
                   "No-nitrogen pumpkin: can still make sugar; can't make amino acids or proteins; sugar would build up.",
                   "Exit ticket: fertilizer isn't food (no sugar, no energy). It supplies elements like N and P that the plant combines with atoms from its own sugar."),
            supports="Give pairs a filled-in Start row. Color-coded bead key on the table.",
        ),
    ),
    # ------------------------------------------------------------------ Day 6
    dict(
        day=6, title="Small Pieces, Big Molecules", lesson="Lesson 5", targets=["LS1-6.4", "LS1-6.2"],
        focus="How do amino acids become proteins, and what happens to them when an animal eats?",
        slides=("Lesson 5: Small Pieces, Big Molecules (pptx)", FILE.format("1bCiFgSB37Z9wspFwRZTgaGJC0iR37q0M")),
        handout=FILE.format("1vCEnX0TvmkAm6seT2VDEmlomYGl637Yj"),
        notebook=[
            "Title: <strong>D6 Small Pieces, Big Molecules</strong>. Add it to your table of contents.",
            "Record the monomer/polymer table, both paper-clip count tables, and the 6-step carbon trace.",
            CER_LOG,
        ],
        sections=[
            ("Warm-up", "<p>A pumpkin makes thousands of proteins from only about 20 kinds of amino acids. How?</p>"),
            ("Monomers and polymers", "<p>A <strong>monomer</strong> is a small molecule that links with others; a <strong>polymer</strong> is many linked monomers.</p>"),
            ("Paper-clip proteins", "<p>Build a 12-clip pumpkin seed protein in order. Then digest it (unhook every clip) and rebuild the clips into a human hair protein.</p>"),
            ("Trace a carbon atom from the air into your hair", "<p>Air → leaf → amino acid → pumpkin seed protein → your blood → your hair. Say what molecule the carbon is in at each step.</p>"),
            ("Show what you know: CFA LS1-6.4", "<p>Take <strong>Unit 1.3 CFA LS1-6.4: Trace atoms with a model</strong> on Canvas (5 questions). "
             "If you score below a B, a review page for this target will open for you.</p>"),
        ],
        cfa="LS1-6.4",
        teacher=dict(
            glance="Monomers to polymers, and digest-and-rebuild. Students trace a carbon atom from the air into their own hair. CFA LS1-6.4 closes the lesson.",
            materials="Lesson 5 slides (pptx in Drive) and handout; colored paper clips (5 colors) per pair; a \"cafeteria\" cup of extra clips; Chromebooks.",
            agenda=[("0–4", "Warm-up"), ("4–10", "Monomers and polymers"), ("10–19", "Activity A: build a pumpkin seed protein"),
                    ("19–31", "Activity B: eat, digest, and rebuild"), ("31–37", "Trace a carbon atom"),
                    ("37–39", "Exit ticket (\"you are what you eat\")"), ("39–45", "CFA LS1-6.4")],
            notes=["This deck has no Google Slides version yet, so the CFA isn't on a slide. Announce it from this page, or add a CFA slide after you convert the deck.",
                   "Keep the starch/cellulose rows about elements, not about classifying macromolecules (outside the HS-LS1-6 boundary)."],
            key=ul("Monomer/polymer: amino acid → protein · glucose → starch (energy storage) · glucose → cellulose (cell walls) · nucleotide → DNA/RNA. "
                   "Starch and cellulose: C, H, O. Proteins: C, H, O, N (some S).",
                   "Pumpkin protein V–L–T–K–Q–L–L–V–T–Q–K–L: V 2, L 4, T 2, K 2, Q 2. Order matters: a different order is a different protein.",
                   "Hair protein K–Q–Q–L–V–Q–T–T–L–Q–V–K: V 2, L 2, T 2, K 2, Q 4 → L +2 extra, Q −2 short (take from the cafeteria cup).",
                   "Trace: CO₂ → glucose (photosynthesis, light energy) → amino acid (with nitrogen from the soil) → seed protein (specific order) → "
                   "amino acid in blood (digested) → hair protein (rebuilt in a new order). Extra amino acids are broken down; their atoms are not destroyed.",
                   "Exit ticket: right that the atoms came from the seed; wrong that the seed protein is in your hair. It was broken down and rebuilt in a new order."),
            supports="Post the clip color key at each table. Partners alternate building and checking the sequence.",
        ),
    ),
    # ------------------------------------------------------------------ Day 7
    dict(
        day=7, title="What's the Evidence?", lesson="Lesson 6", targets=["LS1-6.5"],
        focus="What evidence do scientists have for how plants build their molecules?",
        slides=("Lesson 6: What's the Evidence? (pptx)", FILE.format("13x4a21FJcHhXzfqfl6rtNMw57F4frh49")),
        handout=FILE.format("1sxD7Lttp_p1Q7yeqIV17SXu-OV6kXn7X"),
        notebook=[
            "Title: <strong>D7 What's the Evidence?</strong> Add it to your table of contents.",
            "Record your expert notes, the home-group evidence table (4 stations), and your CER exit ticket.",
            CER_LOG + " Today, add the strongest piece of evidence from the jigsaw.",
        ],
        sections=[
            ("Expert groups", "<p>Station 1: following labeled carbon · Station 2: tomatoes without nitrogen · Station 3: squash, fungi, and phosphorus · "
             "Station 4: crops with extra CO₂. Analyze your station's data and answer the expert questions.</p>"),
            ("Home groups", "<p>Each expert has 3 minutes: what they did, what they found, what it shows. Everyone fills in the evidence table.</p>"),
            ("Which station supports which claim?", ol(
                "A. The carbon in a plant's molecules comes from CO₂ in the air and goes into sugar first.",
                "B. Atoms from sugar are used to build amino acids and other carbon-based molecules.",
                "C. To build amino acids, DNA, and other molecules, plants need elements sugar doesn't have, like N and P, from the soil.",
                "D. A plant needs both sugar and soil elements to grow. Whichever is in short supply limits growth.")),
            ("Exit ticket: CER", "<p>Using Station 2, why were the tomato plants without nitrogen so much smaller, even though they had more sugar?</p>"),
            ("Show what you know: CFA LS1-6.5", "<p>Take <strong>Unit 1.3 CFA LS1-6.5: Explain with evidence</strong> on Canvas (5 questions). "
             "If you score below a B, a review page for this target will open for you.</p>"),
        ],
        cfa="LS1-6.5",
        teacher=dict(
            glance="Jigsaw on four real data sets, then a short CER scored with the same 4-point rubric as the CSA. CFA LS1-6.5 closes the lesson.",
            materials="Lesson 6 slides (pptx) and handout; station data cards (last pages of the handout/deck); Chromebooks.",
            agenda=[("0–3", "How the jigsaw works"), ("3–16", "Expert groups"), ("16–30", "Home groups"),
                    ("30–35", "Match evidence to claims"), ("35–39", "Exit ticket: short CER"), ("39–45", "CFA LS1-6.5")],
            notes=["Expert and home-group time are each trimmed by 1–2 minutes from the original plan to fit the CFA.",
                   "Score the CER exit ticket with the 4-point rubric; it previews the CSA's written response (Q14).",
                   "No Google Slides version of this deck yet, so the CFA isn't on a slide. Announce it from this page."],
            key=ul("Station 1: labeled C appears first in a 3-carbon molecule, then sugars, then amino acids, then starch/proteins/fats; the carbon in proteins comes from CO₂ via sugar; atoms keep their identity. Claims A, B.",
                   "Station 2: still photosynthesizing (sugar 25 vs. 12 mg/g); lower without N: height 11 vs. 32 cm, amino acids 2 vs. 9, protein 10 vs. 40, dry mass 2.4 vs. 7.5 g; sugar built up because it couldn't be combined with N; chlorophyll contains N, so leaves are pale. Claims B, C, D.",
                   "Station 3: fungus gets sugar (carbon) from the plant; plant gets phosphorus (3.0 vs. 1.2 mg/g; dry mass 9.0 vs. 4.0 g); P is needed for DNA, RNA, membranes, ATP; less sugar with fungi because the plant used more for growth and sent some to the fungus; carbon traces back to CO₂. Claims C, D (and A, B).",
                   "Station 4: extra CO₂ raised growth 18 points with plenty of N but only 5 with low N; more CO₂ → more sugar; low N limits turning sugar into proteins; much of a plant's mass comes from CO₂. Claims A, D."),
            supports="Assign station roles by readiness (Station 2 is the most direct). Sentence frames on the slides.",
        ),
    ),
    # ------------------------------------------------------------------ Day 8
    dict(
        day=8, title="Solving the Pumpkin Mystery", lesson="Lesson 7", targets=["LS1-6.5", "LS1-6.6"],
        focus="What is the pumpkin made of, and how did it get built?",
        slides=("Lesson 7: Solving the Pumpkin Mystery (pptx)", FILE.format("1LJ1QOxwElYP00TDNnBghfjYlW5_K3c90")),
        handout=FILE.format("1yRUJCpK1hiP8DKsd9oxKwkJz5PFDngp-"),
        notebook=[
            "Title: <strong>D8 Solving the Pumpkin Mystery</strong>. Add it to your table of contents.",
            "Revise your Day 1 model in a different color and fill in Then I thought / Now I think / Because.",
            "<strong>Finish your Unit CER:</strong> your explanation for the grower is your final claim, evidence, and reasoning. Use your evidence log.",
        ],
        sections=[
            ("Warm-up", "<p>Look at your Day 1 model. What is one thing you now think is wrong or missing? What evidence changed your mind?</p>"),
            ("Class consensus model", "<p>Build the model together: what goes into the leaf, what the leaf builds, what comes from the soil, what the plant builds from sugar plus soil elements, and the evidence for each arrow.</p>"),
            ("Explain it to the grower", "<p>The pumpkin's 110 kg of dry matter is about 45% carbon, the soil barely changed, and the fertilizer has no carbon. "
             "Write a scientific explanation for the grower using the checklist.</p>"),
            ("Peer scoring", "<p>Swap with a partner, check off the checklist, score 1–4 with the rubric, and write one Glow and one Grow.</p>"),
            ("Show what you know: CFA LS1-6.6", "<p>Take <strong>Unit 1.3 CFA LS1-6.6: Revise an explanation</strong> on Canvas (5 questions). "
             "If you score below a B, a review page for this target will open for you.</p>"),
        ],
        cfa="LS1-6.6",
        teacher=dict(
            glance="Revise the Day 1 model and finish the unit CER as an explanation for the grower, peer-scored with the CSA rubric. CFA LS1-6.6 closes the lesson.",
            materials="Lesson 7 slides (pptx) and handout; students' Day 1 models; different-colored pens; Chromebooks.",
            agenda=[("0–4", "Warm-up"), ("4–11", "Class consensus model"), ("11–17", "Revise your model"),
                    ("17–29", "Explain it to the grower (unit CER)"), ("29–37", "Peer scoring"),
                    ("37–39", "Wrap-up: before the practice test, can you…"), ("39–45", "CFA LS1-6.6")],
            notes=["Collect the grower explanations as the unit CER grade (4-point rubric).",
                   "No Google Slides version of this deck yet, so the CFA isn't on a slide. Announce it from this page."],
            key="<p><strong>Exemplar (score 4):</strong> Your pumpkin is made mostly from carbon dioxide from the air and water, not from the soil or fertilizer. "
                "The soil level barely changed, yet the dry pumpkin has about 50 kg of carbon, and the fertilizer has no carbon at all. In class, labeled carbon "
                "from CO₂ showed up first in sugar and later in proteins. The leaves use light energy to build sugar from CO₂ and water; sugar contains only "
                "carbon, hydrogen, and oxygen. The plant then rearranges those atoms and combines them with nitrogen from the soil and fertilizer to build amino "
                "acids, proteins, and other molecules. The \"plant food\" isn't food: it supplies elements like nitrogen and phosphorus. Sunlight supplied the "
                "energy to build sugar, but it didn't become part of the pumpkin because light is energy, not matter.</p>",
            supports="Sentence frames on the slides and handout. Students may use their evidence log and Pumpkin Path page.",
        ),
    ),
    # ------------------------------------------------------------------ Day 9
    dict(
        day=9, title="Practice Test and Review", lesson="Review", targets=[t[0] for t in U.TARGETS],
        focus="Can I explain how a pumpkin builds its body from sugar?",
        slides=("Day 9 Practice Test and Review", SLIDES.format("1yKhzC3fnl-McGFuwPbjTfEk3VI_Vff_qkEfvcL3ExYA")),
        handout=None,
        notebook=[
            "Title: <strong>D9 Review</strong>. Add it to your table of contents.",
            "Rate yourself 1–4 on all 6 targets.",
            "For each review station, write one thing you learned or fixed.",
            f"Answer the driving question in 2–3 sentences: <em>{DRIVING_Q}</em> Use at least 4 vocabulary words.",
        ],
        sections=[
            ("Do Now: rate yourself", "<p>Rate yourself 1–4 on each Unit 1.3 target. Circle the one you'll focus on today.</p>"),
            ("Practice test", "<p>Take the <strong>Unit 1.3 Practice Test: Sugar to Structures (HS-LS1-6)</strong> on Canvas. It looks just like the CSA: "
             "16 questions, including 2 written answers. After your teacher grades it, a review (below a B) or an extension (A or B) opens for you.</p>"),
            ("Review stations", ol(
                "<strong>Station A · Atoms and elements (LS1-6.1, 6.2):</strong> recount 4 molecule cards and check the photosynthesis atom count.",
                "<strong>Station B · Sugar plus nitrogen (LS1-6.3):</strong> build glycine from a glucose bead model and the soil cup; count what's left.",
                "<strong>Station C · Trace the atoms (LS1-6.4):</strong> put the 8 carbon-path cards in order, from the air to your hair.",
                "<strong>Station D · Evidence and revision (LS1-6.5, 6.6):</strong> score two sample answers with the 4-point rubric, then fix the weaker one.")),
            ("Driving question, revisited", f"<p><strong>{DRIVING_Q}</strong> Answer it in your notebook using at least 4 vocabulary words.</p>"),
        ],
        cfa=None,
        teacher=dict(
            glance="Practice test in the CSA's format, then review stations chosen from CFA results. The practice test's Mastery Path opens the review "
                   "(below a B) or the extension (A or B) once the two written answers (P14, P16) are graded.",
            materials="Day 9 slides; Chromebooks; Station A: 4 molecule cards from Lesson 2 + the photosynthesis equation; Station B: glucose bead models, "
                      "blue beads; Station C: the 8 carbon-path cards below (cut apart); Station D: the two sample answers below and the 4-point rubric.",
            agenda=[("0–3", "Self-rating"), ("3–28", "Practice test (grade P14 and P16 during stations)"),
                    ("28–31", "Choose your stations (lowest CFA target first)"), ("31–37", "Station round 1"),
                    ("37–43", "Station round 2"), ("43–45", "Driving question revisited")],
            notes=["Mastery Paths wait for the full practice-test score, so grade the two written answers today if you can.",
                   "If grading can't finish today, students start their review or extension on Day 10 after the CSA.",
                   "Students who finished early can open any CFA review that opened for them."],
            key=(
                "<p><strong>Station A:</strong> photosynthesis 6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂: C 6/6, H 12/12, O 18/18.</p>"
                "<p><strong>Station B:</strong> glycine C₂H₅NO₂ from one glucose (6 C, 12 H, 6 O): add 1 blue bead; left over 4 C, 7 H, 4 O.</p>"
                "<p><strong>Station C cards (correct order):</strong> 1. CO₂ in the air · 2. A pumpkin leaf takes in CO₂ · 3. Light energy powers photosynthesis; the carbon is built into glucose · "
                "4. Atoms from glucose combine with nitrogen from the soil to make an amino acid · 5. Amino acids link in a specific order into a seed protein · "
                "6. You eat the seed; digestion breaks the protein into amino acids · 7. Your blood carries the amino acids to your cells · "
                "8. Your cells link them in a new order into hair protein.</p>"
                "<p><strong>Station D sample answers</strong> (question: why is a plant with more sugar but no nitrogen smaller?)<br>"
                "Sample 1 (scores 2): \"The plant needs nitrogen to grow. The data shows it was smaller.\" Missing: data with numbers, and why nitrogen matters (sugar has only C, H, O; amino acids need N).<br>"
                "Sample 2 (scores 4): \"The no-nitrogen plant made more sugar (25 vs. 12 mg/g) but less protein (10 vs. 40 mg/g) and less dry mass (2.4 vs. 7.5 g). "
                "Sugar has only carbon, hydrogen, and oxygen. To build amino acids and proteins, the plant has to combine atoms from sugar with nitrogen. Without nitrogen, "
                "the sugar couldn't be used, so it built up and the plant couldn't make new cells.\"</p>"),
            supports="Send students to the station for their lowest CFA target first. Allow notebooks and the Pumpkin Path page at stations (not on the practice test).",
        ),
    ),
    # ------------------------------------------------------------------ Day 10
    dict(
        day=10, title="Unit 1.3 CSA", lesson="CSA", targets=[t[0] for t in U.TARGETS],
        focus="How do atoms from sugar become the structures of living things?",
        slides=("Day 10 Unit 1.3 CSA", SLIDES.format("1jVo_CDFD9Cz6mf4n6Q3llg3l6LiBdm60L5xXxhWonfk")),
        handout=None,
        notebook=["After the test: title <strong>D10 CSA reflection</strong>. Rate yourself on all 6 targets one last time. Which target improved the most since Day 1?"],
        sections=[
            ("Before you start", "<p>Clear your desk except your Chromebook, a pencil, and scratch paper. Read every question twice. "
             "Questions 14 and 16 need written answers: use claim, evidence, and reasoning.</p>"),
            ("Unit 1.3 CSA", "<p>Open <strong>Unit 1.3 CSA: Sugar to Structures (HS-LS1-6)</strong> on Canvas. 16 questions, 22 points.</p>"),
            ("When you finish", "<p>Do your notebook reflection. Then work quietly on your review or extension assignment from the practice test.</p>"),
        ],
        cfa=None,
        teacher=dict(
            glance="Common summative assessment: 16 questions (3 per DOK 1–2 target; 1 multiple choice + 1 written response per DOK 3 target), 22 points.",
            materials="Day 10 slides; Chromebooks; scratch paper.",
            agenda=[("0–3", "Settle in; directions"), ("3–43", "Unit 1.3 CSA"), ("43–45", "Notebook reflection; review or extension work")],
            notes=["Grade Q14 and Q16 with the rubric in each question's grading notes (SpeedGrader).",
                   "Students who score below proficient on a target can redo that target's CFA review before reassessment."],
            key="<p>CSA answer key, rubrics, and outcome alignment: <em>assessments/HS-LS1-6/Unit1.3_teacher_key.md</em> in the course repo.</p>",
            supports="Accommodations per IEP/504 (extended time, read-aloud). Scratch paper for atom counts and bead sketches.",
        ),
    ),
]


def page_title(d):
    return f"Unit 1.3 Day {d['day']}: {d['title']}"


def targets_html(tids):
    return "".join(f"<li><strong>{t}</strong> {U.TARGET[t][3]}</li>" for t in tids)


def student_html(d):
    label = "Learning target" if len(d["targets"]) == 1 else "Learning targets"
    lesson = f" ({d['lesson']} of the Giant Pumpkin Mystery)" if d["lesson"].startswith("Lesson") else ""
    out = [f'<div style="{BOX}"><p><strong>Day {d["day"]}</strong>{lesson} · Unit 1.3: Sugar to Structures (HS-LS1-6)</p>'
           f"<p><strong>Driving question:</strong> {DRIVING_Q}</p><p><strong>Focus question:</strong> {d['focus']}</p>"
           f"<p><strong>{label}:</strong></p><ul>{targets_html(d['targets'])}</ul></div>",
           f'<h2>Notebook setup</h2><div style="{BOX}">' + ol(*d["notebook"]) +
           "<p><em>Your notebook is your answer sheet for this lesson. Keep it neat; your teacher will check it.</em></p></div>"]
    sections = list(d["sections"])
    if d["cfa"] and not any(h.startswith("Show what you know") for h, _ in sections):
        tid = d["cfa"]
        sections.append((f"Show what you know: CFA {tid}",
                         f"<p>Take <strong>Unit 1.3 CFA {tid}: {U.TARGET[tid][1]}</strong> on Canvas (5 questions). "
                         "If you score below a B, a review page for this target will open for you.</p>"))
    for n, (h, body) in enumerate(sections, 1):
        out.append(f"<hr><h2>Part {n}: {h}</h2>{body}")
    out.append("<hr><p><strong>If you were absent:</strong> view today's slides with your teacher's link or ask for a copy, complete the notebook "
               "pages above, and take any CFA listed on this page.</p>")
    return "\n".join(out)


def teacher_html(d, student_url=None):
    t = d["teacher"]
    link = f' · <a href="{student_url}">Student page</a>' if student_url else ""
    cfa = f" · CFA {d['cfa']}" if d["cfa"] else ""
    rows = "".join(f"<tr><td>{m}</td><td>{a}</td></tr>" for m, a in t["agenda"])
    links = [f'<a href="{d["slides"][1]}">{d["slides"][0]}</a>']
    if d["handout"]:
        links.append(f'<a href="{d["handout"]}">Student handout (docx)</a>')
    links.append(f'<a href="{FOLDER}">Unit 1.3 Drive folder</a>')
    return "\n".join([
        f'<div style="{TBOX}"><p><strong>Teacher page · keep unpublished.</strong> Students never see this page.</p>'
        f"<p><strong>Day {d['day']}</strong> · {d['lesson']} · Targets: {', '.join(d['targets'])}{cfa}{link}</p></div>",
        f"<h2>At a glance</h2><p>{t['glance']}</p>",
        "<h2>Slides and materials</h2><p>" + " · ".join(links) + f"</p><p>{t['materials']}</p>",
        f'<h2>Agenda (45 minutes)</h2><table border="1" cellpadding="6" style="border-collapse:collapse"><tbody><tr><th>Min</th><th>What happens</th></tr>{rows}</tbody></table>',
        "<h2>Teaching notes</h2>" + ul(*t["notes"]),
        "<h2>Answer key</h2>" + t["key"],
        f"<h2>Supports</h2><p>{t['supports']}</p>",
    ])


if __name__ == "__main__":
    for d in DAYS:
        print(page_title(d), "|", d["cfa"])
