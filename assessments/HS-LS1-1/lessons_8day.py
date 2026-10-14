"""Lesson pages for the 8-day version of unit 2.1, built around the anchoring phenomenon of Siamese cats.

Why are a Siamese cat's ears, face, paws, and tail dark when the rest of its body is cream, and why is a Siamese
kitten born white? Answer: the cat inherits two copies of a changed version of the gene for a pigment-making protein
(tyrosinase). One DNA base change swaps one amino acid, so the protein stops working at warm body temperatures and works
only in cooler skin (ears, nose, paws, tail tip). Same DNA, same gene, one amino acid different, a different result.

Science notes: the Siamese (colorpoint) pattern is linked to a single-base change in the tyrosinase (TYR) gene
that swaps one amino acid (reported as glycine to arginine; sources number the residue differently). It is inherited as a
recessive trait. Class temperatures, litter data, and DNA letters are simplified illustrations.
Sources: Lyons et al. 2005 (Siamese and Burmese tyrosinase alleles); Acromelanism (Wikipedia).
"""

CODE_TABLE = ("<table border=\"1\" cellpadding=\"6\"><tr><th>DNA triplet</th><th>Amino acid</th><th>DNA triplet</th><th>Amino acid</th></tr>"
              "<tr><td>ATG</td><td>Met</td><td>AGA</td><td>Arg</td></tr><tr><td>GGA</td><td>Gly</td><td>CTG</td><td>Leu</td></tr>"
              "<tr><td>TTT</td><td>Phe</td><td>GAC</td><td>Asp</td></tr></table>")

CODE_TABLE_D4 = ("<table border=\"1\" cellpadding=\"6\"><tr><th>DNA triplet</th><th>Amino acid</th><th>DNA triplet</th><th>Amino acid</th></tr>"
                 "<tr><td>GGA</td><td>Gly</td><td>AGA</td><td>Arg</td></tr><tr><td>GAG</td><td>Glu</td><td>GTG</td><td>Val</td></tr>"
                 "<tr><td>GAA</td><td>Glu</td><td>CTG</td><td>Leu</td></tr><tr><td>CCG</td><td>Pro</td><td>&nbsp;</td><td>&nbsp;</td></tr></table>")

TEMPS = ("<table border=\"1\" cellpadding=\"6\"><tr><th>Body part of an adult Siamese cat</th><th>Skin temperature (&deg;C)</th><th>Fur color</th></tr>"
         "<tr><td>Back (trunk)</td><td>36</td><td>Cream</td></tr><tr><td>Belly</td><td>36</td><td>Cream</td></tr>"
         "<tr><td>Upper leg</td><td>34</td><td>Cream</td></tr><tr><td>Ear</td><td>28</td><td>Dark brown</td></tr>"
         "<tr><td>Nose and face mask</td><td>30</td><td>Dark brown</td></tr><tr><td>Paw</td><td>28</td><td>Dark brown</td></tr>"
         "<tr><td>Tail tip</td><td>27</td><td>Dark brown</td></tr></table>"
         "<p><em>Simplified class data set. Real temperatures vary.</em></p>")

LITTERS = ("<table border=\"1\" cellpadding=\"6\"><tr><th>Litter</th><th>Mother</th><th>Father</th><th>Dark-pointed (Siamese pattern) kittens</th><th>Solid-colored kittens</th></tr>"
           "<tr><td>1</td><td>Siamese pattern</td><td>Siamese pattern</td><td>5</td><td>0</td></tr>"
           "<tr><td>2</td><td>Siamese pattern</td><td>Siamese pattern</td><td>4</td><td>0</td></tr>"
           "<tr><td>3</td><td>Siamese pattern</td><td>Solid</td><td>0</td><td>6</td></tr>"
           "<tr><td>4</td><td>Solid</td><td>Solid</td><td>1</td><td>4</td></tr>"
           "<tr><td>5</td><td>Solid</td><td>Solid</td><td>2</td><td>3</td></tr>"
           "<tr><td>6</td><td>Siamese pattern</td><td>Solid</td><td>3</td><td>2</td></tr>"
           "<tr><td>7</td><td>Solid</td><td>Solid</td><td>1</td><td>5</td></tr></table>"
           "<p><em>Simplified class data set modeled on real litter patterns.</em></p>")

TEACHER = "<p style=\"background:#fff3cd;padding:6px\"><strong>TEACHER PAGE.</strong> Includes answers. Do not share with students.</p>"

DAY1_PLAN = TEACHER + """
<h2>Day 1: Launch with the Siamese cat</h2>
<table border="1" cellpadding="6"><tr><th>Targets</th><td>LS1-1.2 (priority): DNA holds the instructions for building proteins. LS3-1 (supporting, light): one set of chromosomes and genes from each parent.</td></tr>
<tr><th>Goal</th><td>Students notice and wonder about a Siamese cat's colors, find patterns in temperature and inheritance data, and start an initial model of what is in the cells.</td></tr>
<tr><th>Materials</th><td>A projected photo of an adult Siamese cat and of a white newborn Siamese kitten (search &ldquo;Siamese kitten newborn white&rdquo; and &ldquo;Siamese cat&rdquo;); the student page.</td></tr>
<tr><th>CFA</th><td>LS1-1.2 (last 6 minutes)</td></tr></table>
<h3>Plan (45 minutes)</h3>
<ol>
<li><strong>Notice and wonder (7 min).</strong> Show the adult Siamese: dark ears, face mask, paws, and tail; cream body. Then show the newborn kitten: nearly all white. Students write 2 noticings and 2 wonderings. Collect on the board. Steer toward: <em>Why are only the ears, face, paws, and tail dark? Why is the kitten born white? What is different inside a Siamese cat?</em></li>
<li><strong>Look for patterns: temperature (8 min).</strong> Students study the temperature table and answer Questions 1 and 2. Debrief: dark fur goes with the cooler body parts (27 to 30 degrees), cream fur with warmer parts (34 to 36). A newborn kitten was warm all over in the womb, so it is born white and darkens as its extremities cool.</li>
<li><strong>Look for patterns: inheritance (8 min).</strong> Students study the litter table and answer Questions 3 and 4. Debrief: two Siamese-pattern parents have only Siamese-pattern kittens; two solid parents can still have Siamese-pattern kittens; a Siamese-pattern &times; solid pair can have all solid kittens. The pattern is inherited, and a kitten gets something from <em>both</em> parents.</li>
<li><strong>Mini-lesson: what is passed on (10 min).</strong> Key Ideas on the student page. Board: <em>DNA &rarr; gene &rarr; protein &rarr; job in the cell.</em> A kitten gets one set of chromosomes (each a very long DNA molecule with many genes) from each parent (LS3-1, light). A gene is a section of DNA with the instructions for one protein, and proteins do the jobs of the cell. Question to carry through the unit: <em>How can a difference in DNA change which parts of a cat are dark?</em></li>
<li><strong>Practice and initial model (6 min).</strong> Students answer Questions 5 to 7 and sketch Question 8, a first model. They revise it on Day 7.</li>
<li><strong>CFA LS1-1.2 (6 min).</strong></li>
</ol>
<h3>Answer key for the student page</h3>
<ol>
<li>The dark parts (ear 28, nose 30, paw 28, tail 27) are the coolest; the cream parts (36, 36, 34) are the warmest. Dark fur goes with cooler skin.</li>
<li>A newborn is warm all over, so it is born white. As the ears, paws, and tail cool after birth, they darken.</li>
<li>Siamese &times; Siamese: all kittens (9 of 9) are Siamese pattern. Siamese &times; solid: either no Siamese-pattern kittens (litter 3) or some (litter 6). Solid &times; solid: some litters have a few Siamese-pattern kittens (4 of 5 solid litters here: 1, 2, 1 of 5, 5, 6 kittens).</li>
<li>Yes: the pattern appears only in kittens whose parents are related to the pattern, and two Siamese-pattern parents always have Siamese-pattern kittens. It is inherited, and it can be hidden for a generation (solid parents can have Siamese-pattern kittens). Both parents contribute.</li>
<li>DNA.</li>
<li>A gene; a protein.</li>
<li>Look for: DNA or a gene in the cells, passed from both parents, that affects something made in the fur (pigment) and is affected by temperature. Do not correct yet.</li>
</ol>
<h3>Notes</h3>
<ul><li>The Siamese pattern is a recessive trait: a kitten needs a changed copy of the gene from both parents. Do not name recessive/dominant yet unless students ask; the key idea is &ldquo;from both parents.&rdquo;</li>
<li>Solid parents who have Siamese-pattern kittens each carry one changed copy that is hidden. That is expected here.</li></ul>
"""

DAY1_STUDENT = """{{SLIDES}}
<h2>Day 1: Why are a Siamese cat's ears, paws, and tail dark?</h2>
<h3>Notice and wonder</h3>
<p>Look at the photos of an adult Siamese cat and a newborn Siamese kitten.</p>
<p>I notice: __________________________ &nbsp; I notice: __________________________</p>
<p>I wonder: __________________________ &nbsp; I wonder: __________________________</p>
<h3>Data 1: Temperature and color</h3>
""" + TEMPS + """
<ol>
<li>What pattern do you see between skin temperature and fur color?</li>
<li>A Siamese kitten is born almost white, and the dark parts appear in the first weeks. Use the data to suggest why.</li>
</ol>
<h3>Data 2: Litters of kittens</h3>
""" + LITTERS + """
<ol start="3">
<li>Describe the pattern for each type of pair: Siamese &times; Siamese, Siamese &times; solid, and solid &times; solid.</li>
<li>Is the Siamese pattern passed from parents to kittens? What is your evidence? Does a kitten need something from one parent or from both?</li>
</ol>
<h3>Key ideas</h3>
<ul>
<li><strong>DNA</strong> in every cell stores instructions.</li>
<li>A <strong>gene</strong> is a section of DNA with the instructions for one <strong>protein</strong>.</li>
<li><strong>Proteins</strong> do jobs for the cell.</li>
<li>A kitten gets one set of chromosomes (long DNA molecules with many genes) from each parent.</li>
</ul>
<h3>Practice</h3>
<ol start="5">
<li>The molecule that stores the instructions in a cat's cells is ______.</li>
<li>A section of DNA with the instructions for one protein is a ______. Its product, which does a job for the cell, is a ______.</li>
<li>How many sets of chromosomes does a kitten get from each parent?</li>
<li><strong>Initial model.</strong> Draw and label a model of what is inside a Siamese cat's cells that leads to dark ears, paws, and tail. Use arrows. We will revise it on Day 7.</li>
</ol>
"""

DAY2_PLAN = TEACHER + """
<h2>Day 2: What is DNA made of?</h2>
<table border="1" cellpadding="6"><tr><th>Target</th><td>LS1-1.1 (priority): DNA is a double helix built from nucleotides, each with a sugar, a phosphate, and a base.</td></tr>
<tr><th>Goal</th><td>Students describe DNA's structure and base pairing, and see that the message is the order of the bases. Prepares for the lab on Day 3.</td></tr>
<tr><th>Materials</th><td>Student page; colored pencils; scissors and tape or glue.</td></tr>
<tr><th>CFA</th><td>LS1-1.1 (6 minutes)</td></tr></table>
<h3>Plan (45 minutes)</h3>
<ol>
<li><strong>Warm-up (5 min).</strong> Ask: <em>Yesterday we said a gene in the cat's cells holds instructions for a protein that has something to do with dark fur. What do you think DNA looks like?</em> Students sketch for 1 minute, then share.</li>
<li><strong>Mini-lesson (12 min).</strong> Build up on the board: one nucleotide (a pentagon for the sugar, a circle for the phosphate, a rectangle for the base); a strand of nucleotides joined sugar to phosphate (the backbone); the four bases A, T, C, G; the second strand; pairing A with T and C with G; the twist into a double helix. Key point: <strong>the order of the bases is the message.</strong> A cat's DNA has billions of bases; a gene is a stretch of them.</li>
<li><strong>Activity: build it on paper (14 min).</strong> Students complete Parts A to C on the student page: draw and label a nucleotide, write the partner strand for three sequences, and answer the questions.</li>
<li><strong>Connect to the cats (4 min).</strong> Show the illustration in Part C: the same short stretch of a gene from a solid cat and a Siamese cat, differing by one letter. Ask: <em>Could one letter change which parts of a cat are dark?</em> We find out on Days 3 and 4. State clearly that the letters are an illustration.</li>
<li><strong>CFA LS1-1.1 (6 min).</strong></li>
</ol>
<h3>Answer key for the student page</h3>
<ul>
<li>Part A: sugar (pentagon), phosphate (circle), base (rectangle). The sugar and phosphate form the backbone.</li>
<li>Part B: (1) A T G C C T &rarr; T A C G G A. (2) T T T G A C &rarr; A A A C T G. (3) C T G G G A &rarr; G A C C C T.</li>
<li>Part C: 1. Double helix (twisted ladder). 2. Sides: sugar and phosphate; rungs: pairs of bases. 3. A with T; C with G. 4. The order of the bases. 5. They differ at one letter: the first letter of the second triplet (G in the solid cat, A in the Siamese cat).</li>
</ul>
"""

DAY2_STUDENT = """{{SLIDES}}
<h2>Day 2: What is DNA made of?</h2>
<h3>Key ideas</h3>
<ul>
<li>DNA is a <strong>double helix</strong>, like a twisted ladder.</li>
<li>It is built from <strong>nucleotides</strong>. Each nucleotide has a <strong>sugar</strong>, a <strong>phosphate</strong>, and a <strong>base</strong>.</li>
<li>The sugars and phosphates make the sides (the backbone). The bases make the rungs.</li>
<li>There are four bases: <strong>A, T, C, G</strong>. A pairs with T. C pairs with G.</li>
<li><strong>The order of the bases is the message.</strong></li>
</ul>
<h3>Part A: One nucleotide</h3>
<p>Draw one nucleotide: a pentagon (sugar), a circle (phosphate), and a rectangle (base). Label each part and color the base.</p>
<h3>Part B: Write the partner strand</h3>
<ol>
<li>A T G C C T &rarr; ______________</li>
<li>T T T G A C &rarr; ______________</li>
<li>C T G G G A &rarr; ______________</li>
</ol>
<h3>Part C: Questions</h3>
<ol>
<li>What shape is DNA?</li>
<li>What makes up the sides of the ladder? What makes up the rungs?</li>
<li>Which bases pair together?</li>
<li>What makes one gene different from another?</li>
<li><strong>Illustration only.</strong> A short stretch of a gene in two cats (made-up letters that show the idea):<br>
Solid cat: &nbsp;&nbsp;A T G <u>G</u> G A C T G T T T<br>
Siamese cat: A T G <u>A</u> G A C T G T T T<br>
How many letters differ? Where?</li>
</ol>
"""

LAB_STUDENT = """{{SLIDES}}
<h2>Gummy DNA Lab: Build, Copy, and Read a Gene</h2>
<p><strong>Name:</strong> ______________ &nbsp; <strong>Partner:</strong> ______________</p>
<p><strong>Question:</strong> How does a cell's copy of a gene become a chain of amino acids, and what happens if one letter of DNA changes?</p>
<p>You will build a short model of the start of a cat's gene for a pigment-making protein. (The letters are an illustration, not the real gene.)</p>
<h3>Materials (per pair)</h3>
<ul>
<li>2 licorice strands (the backbone; the sugars and phosphates)</li>
<li>Candy &ldquo;bases&rdquo;: 6 red (A), 6 yellow (T), 6 green (C), 6 orange (G) gummies, plus 2 extra of each color</li>
<li>Toothpicks (to attach bases to the backbone and to hold pairs together)</li>
<li>Paper plate or tray, this sheet, the code table</li>
</ul>
<p><strong>Safety:</strong> Keep materials clean. Do not eat the lab materials until your teacher says you may. Toothpicks are sharp. Tell your teacher about any food allergy. If candy is not used, use colored beads or paper circles.</p>
<h3>Base key and code table</h3>
<p>Red = A &nbsp; Yellow = T &nbsp; Green = C &nbsp; Orange = G</p>
""" + CODE_TABLE + """
<h3>Part A: Build the template strand (6 min)</h3>
<p>This is the strand of the gene that the cell uses as a template. Attach the bases to one licorice strand in order from left to right:</p>
<p><strong>T A C &nbsp; C C T &nbsp; G A C &nbsp; A A A</strong></p>
<p>Write the color order you built: ______________________________________________</p>
<h3>Part B: Build the partner strand and make the ladder (8 min)</h3>
<p>Build the partner strand on the second licorice strand by pairing each base (A with T, C with G). Write the partner sequence you built:</p>
<p>_ _ _ &nbsp; _ _ _ &nbsp; _ _ _ &nbsp; _ _ _</p>
<ol>
<li>Join the two strands with toothpicks between pairs. Gently twist the ladder. Have your teacher check it before you continue. &#9744; Checked</li>
<li>Which strand carries the &ldquo;coding&rdquo; letters (the same as the cell's message copy)? How do you know?</li>
</ol>
<h3>Part C: Copy the message, then read it (10 min)</h3>
<p>The cell does not use the DNA directly to make a protein. It <strong>copies the gene's message</strong> from the template strand, and then the <strong>copy is read</strong> to link amino acids. The DNA stays safe.</p>
<ol>
<li>Pull the two strands apart. Keep the template strand. Build a <em>new</em> strand by pairing with the template. This is the <strong>copy</strong>. Write its sequence: ___ ___ ___ ___</li>
<li>Read the copy three letters at a time with the code table. Write the amino acid chain: ______ &ndash; ______ &ndash; ______ &ndash; ______</li>
<li>Line up one bead or paper tag per amino acid on the plate in order. This chain would fold to make a protein.</li>
<li>Explain the path in your own words, starting with the DNA: ______________________________________________</li>
</ol>
<h3>Part D: Change one letter (7 min)</h3>
<ol>
<li>On your template strand, replace the 4th base (the first C of the second triplet) with a T (swap a green gummy for a yellow one). The template now reads <strong>TAC TCT GAC AAA</strong>.</li>
<li>Build the new copy by pairing with the changed template. Sequence: ___ ___ ___ ___</li>
<li>Read it with the code table: ______ &ndash; ______ &ndash; ______ &ndash; ______</li>
<li>Compare with Part C. How many amino acids changed? Which one?</li>
<li>Predict: Could a protein built from this changed chain work differently? Explain.</li>
</ol>
<h3>Connect to the Siamese cat</h3>
<ol>
<li>In a Siamese cat, a one-letter change in the gene for a pigment-making protein swaps one amino acid. In your own words, what did your one-letter change do to the chain in the model?</li>
<li>Name two ways your gummy model is different from real DNA.</li>
</ol>
<h3>Clean up</h3>
<p>Put toothpicks and candy in the trash or the labeled container. Wipe your table. Wash your hands.</p>
"""

LAB_TEACHER = TEACHER + """
<h2>Day 3 Teacher Key: Gummy DNA Lab</h2>
<table border="1" cellpadding="6"><tr><th>Targets</th><td>LS1-1.3 (priority): a gene's message is copied and the copy is read to build a chain of amino acids. Applies LS1-1.1 (DNA structure).</td></tr>
<tr><th>Prep (15 min before class)</th><td>For each pair: 2 licorice strands (6 to 8 inches, such as Twizzlers or Red Vines), 24 candy bases (6 each of four colors, plus a few spare), a handful of toothpicks, a paper plate. Print the lab sheet and code table. If you cannot use food (gelatin, allergies, or policy), use colored beads and pipe cleaners or paper circles taped to paper strips.</td></tr>
<tr><th>CFA</th><td>LS1-1.3 (6 minutes; if the lab runs long, give the CFA first and finish Part D at the start of Day 4)</td></tr></table>
<h3>Timing (45 minutes)</h3>
<ol><li>Intro and safety (5 min): the copy-then-read idea; show a pre-built strand.</li><li>Part A (6 min).</li><li>Part B (8 min).</li><li>Part C (10 min).</li><li>Part D (5 min).</li><li>Clean up and CFA (11 min).</li></ol>
<h3>Answer key</h3>
<ul>
<li><strong>Part A</strong> (colors in order): yellow, red, green, green, green, yellow, orange, red, green, red, red, red.</li>
<li><strong>Part B</strong> partner strand: A T G &nbsp; G G A &nbsp; C T G &nbsp; T T T. The partner strand has the coding letters; it matches the copy the cell makes from the template. Check each pair: A with T, C with G.</li>
<li><strong>Part C</strong>: the copy (pairing with the template) is <strong>A T G G G A C T G T T T</strong>. Chain: <strong>Met &ndash; Gly &ndash; Leu &ndash; Phe</strong>. Explanation: the gene's message is copied from the template strand, and the copy is read three letters at a time to link amino acids in order.</li>
<li><strong>Part D</strong>: the changed template TAC TCT GAC AAA gives the copy ATG AGA CTG TTT, which reads <strong>Met &ndash; Arg &ndash; Leu &ndash; Phe</strong>. One amino acid changed (the second, Gly to Arg). Yes, a different chain can fold into a protein that works differently.</li>
<li><strong>Connect</strong>: (1) One amino acid in the chain changed, so the protein could work differently (in the Siamese cat, it stops working at warm temperatures). (2) Accept: candy versus molecules; the model is huge compared with real DNA; real nucleotides each have a sugar and phosphate and the strands twist; real genes are thousands of bases long.</li>
</ul>
<h3>Teaching notes</h3>
<ul>
<li>Teach copy-then-read only. Do not teach mRNA, tRNA, or ribosome mechanics (outside the assessment boundary). Say &ldquo;the cell copies the gene's message.&rdquo;</li>
<li>Common mistakes: matching A with C or G; reading the template directly; not reading in groups of three from the start.</li>
<li>Grade out of 12 (Part A 1, Part B 2, Part C 4, Part D 3, Connect 2), then divide by 3 to enter the 4-point score in Canvas.</li>
</ul>
"""

DAY3_PLAN = TEACHER + """
<h2>Day 3: Lab day, Build, Copy, and Read a Gene (gummy DNA)</h2>
<p>This is the one hands-on lab and the one day on how a gene's message is copied and read. See the <strong>Teacher Key and Prep</strong> page for materials, timing, and answers, and the <strong>Lab Sheet</strong> assignment for students.</p>
<ol><li>Intro (5): <em>Yesterday we saw a one-letter difference between a solid cat's gene and a Siamese cat's gene. Today we build a gene, watch how its message is copied and read, and change one letter ourselves.</em></li>
<li>Lab, Parts A to D (about 29 min).</li>
<li>CFA LS1-1.3 (6 min) and clean up.</li></ol>
"""

DAY4_PLAN = TEACHER + """
<h2>Day 4: What can one letter do?</h2>
<table border="1" cellpadding="6"><tr><th>Target</th><td>LS1-1.4 (priority): changing one DNA base can change a protein and what it does.</td></tr>
<tr><th>Goal</th><td>Students sort one-letter DNA changes by their effect, see that not every change matters, and connect an amino acid change to a protein that works differently, as in the Siamese cat.</td></tr>
<tr><th>Materials</th><td>Student page and card strips (six cards per group); gummy models from Day 3 if kept.</td></tr>
<tr><th>CFA</th><td>LS1-1.4 (6 minutes)</td></tr></table>
<h3>Plan (45 minutes)</h3>
<ol>
<li><strong>Warm-up (5 min).</strong> Finish Part D of the lab: how many amino acids changed when one letter changed? Recap: base order sets amino acid order.</li>
<li><strong>Mini-lesson (10 min).</strong> A one-letter change can do one of three things: (1) change one amino acid in the chain, which can change how the protein works; (2) change whether or when the protein is made, if the change is in a switch next to the gene; (3) change nothing noticeable (the amino acid is the same, or the change is in a stretch with no role). Not every change matters.</li>
<li><strong>Card sort (15 min).</strong> Groups sort the six cards into the three categories and justify each (student page).</li>
<li><strong>The Siamese cat (8 min).</strong> Reveal: card A is the real Siamese change. The cat's pigment-making protein has one different amino acid. That protein still forms, but the change makes it stop working at warm body temperatures. It works only in the cooler ears, nose, paws, and tail tip. Ask: <em>How does this explain the dark points and the white newborn?</em> (A newborn kitten is warm everywhere, so no pigment is made; as the extremities cool, the protein works there and pigment appears.)</li>
<li><strong>CFA LS1-1.4 (6 min).</strong></li>
</ol>
<h3>Answer key for the card sort</h3>
<ul>
<li>Card A (Siamese: GGA &rarr; AGA, Gly &rarr; Arg): Category 1.</li>
<li>Card B (GAG &rarr; GAA, Glu &rarr; Glu): Category 3 (same amino acid).</li>
<li>Card C (CTG &rarr; CCG, Leu &rarr; Pro): Category 1.</li>
<li>Card D (a one-letter change in a stretch of DNA with no gene and no switch): Category 3.</li>
<li>Card E (a one-letter change in a switch so the gene can never be turned on and its protein is not made): Category 2.</li>
<li>Card F (a human gene: GAG &rarr; GTG, Glu &rarr; Val, as in sickle cell): Category 1.</li>
<li>Claim check: &ldquo;Every change in DNA changes how a cell works.&rdquo; Not supported: cards B and D show no effect.</li>
</ul>
<h3>Notes</h3>
<ul><li>GAA also codes for Glu, and CCG codes for Pro, so cards B and C are real.</li>
<li>Keep the protein story at the level of the standard: a different amino acid changes how the protein works. Do not go into protein folding or chemistry.</li></ul>
"""

DAY4_STUDENT = """{{SLIDES}}
<h2>Day 4: What can one letter do?</h2>
<h3>Key ideas</h3>
<ul>
<li>A one-letter change in DNA can (1) change an amino acid in the chain, (2) change whether or when a protein is made, or (3) change nothing noticeable.</li>
<li>A different amino acid can make a protein work differently.</li>
<li>Not every change matters.</li>
</ul>
<h3>Card sort</h3>
<p>Cut out the cards. Sort them into three groups and write your reason on each. Use the code table.</p>
""" + CODE_TABLE_D4 + """
<table border="1" cellpadding="6">
<tr><th>Card</th><th>What changed</th></tr>
<tr><td>A</td><td>In a Siamese cat, one letter changes in the gene for a pigment-making protein: GGA becomes AGA.</td></tr>
<tr><td>B</td><td>A gene's triplet changes from GAG to GAA.</td></tr>
<tr><td>C</td><td>A gene's triplet changes from CTG to CCG.</td></tr>
<tr><td>D</td><td>One letter changes in a stretch of DNA that has no gene and no switch.</td></tr>
<tr><td>E</td><td>One letter changes in a switch next to a gene so the gene can never be turned on, and its protein is not made.</td></tr>
<tr><td>F</td><td>In a human gene, GAG becomes GTG.</td></tr>
</table>
<p><strong>Category 1:</strong> changes an amino acid in the chain. <strong>Category 2:</strong> changes whether or when the protein is made. <strong>Category 3:</strong> no noticeable change.</p>
<ol>
<li>Write the cards in each category and your reasons.</li>
<li>A student says, &ldquo;Every change in DNA changes how a cell works.&rdquo; Use the cards to respond.</li>
<li>Siamese cat: card A changes one amino acid. Predict what could happen to the protein and to the fur color. (Hint: think about temperature.)</li>
</ol>
"""

DAY5_PLAN = TEACHER + """
<h2>Day 5: Same DNA, different jobs</h2>
<table border="1" cellpadding="6"><tr><th>Target</th><td>LS1-1.5 (priority): DNA, through proteins, gives different cells their different jobs.</td></tr>
<tr><th>Goal</th><td>Students explain that all cells have the same genes but use different ones, and use the Siamese cat to explain why only some parts of the body show dark color.</td></tr>
<tr><th>Materials</th><td>Student page; two colors of pencil.</td></tr>
<tr><th>CFA</th><td>LS1-1.5 (6 minutes)</td></tr></table>
<h3>Plan (45 minutes)</h3>
<ol>
<li><strong>Warm-up (5 min).</strong> Ask: <em>Your skin cells and your nerve cells have the same DNA. Why are they so different?</em> Collect ideas.</li>
<li><strong>Mini-lesson (10 min).</strong> Every cell has all the genes, but each kind of cell uses a different set. The proteins a cell makes decide its job. In a cat, only pigment-making cells use the gene for the pigment-making protein.</li>
<li><strong>Activity A: cell types (6 min).</strong> Students complete Part A (cell types P and Q).</li>
<li><strong>Activity B: map the Siamese cat (14 min).</strong> Students complete the tables in Parts B and C: which cells use the gene, and where the changed protein works.</li>
<li><strong>Explain it (4 min).</strong> Students write the Question 4 explanation.</li>
<li><strong>CFA LS1-1.5 (6 min).</strong></li>
</ol>
<h3>Answer key</h3>
<ul>
<li>Part A: same DNA (genes 1 to 4 in both). P uses genes 1 and 2, Q uses genes 3 and 4. Different genes used means different proteins, so different jobs.</li>
<li>Part B table: all cell types have the pigment gene. Only pigment-making cells make the pigment protein (X). Skin cells and nerve cells do not.</li>
<li>Part C table: the changed protein works only where the skin is cooler than about 33 degrees (simplified): ear 28 works, nose 30 works, paw 28 works, tail tip 27 works, back 36 does not, belly 36 does not, upper leg 34 does not. Pigment (dark) where it works; cream where it does not.</li>
<li>Q1 Yes, every cell has the gene. Q2 Only pigment cells make the protein. Q3 It works only in cool skin, so only the ears, nose, paws, and tail are dark. Q4 model answer: All of a Siamese cat's cells have the same DNA, including the gene for the pigment-making protein. Only pigment-making cells use the gene. Because the protein has one amino acid changed, it works only in cool skin, so pigment is made only in the ears, nose, paws, and tail.</li>
</ul>
<h3>Notes</h3>
<ul><li>The 33-degree line is a simplified class number. The idea to keep: the changed protein works in cool skin and not in warm skin.</li>
<li>Do not go into the chemistry of pigment production. Stay at: protein works, so pigment is made.</li></ul>
"""

DAY5_STUDENT = """{{SLIDES}}
<h2>Day 5: Same DNA, different jobs</h2>
<h3>Key ideas</h3>
<ul>
<li>Every cell has the same DNA, including all the genes.</li>
<li>Each kind of cell uses a different set of genes, makes different proteins, and so has a different job.</li>
</ul>
<h3>Part A: Two kinds of cells</h3>
<table border="1" cellpadding="6"><tr><th>Cell type</th><th>Genes in the cell</th><th>Proteins made</th><th>Job</th></tr>
<tr><td>P</td><td>1, 2, 3, 4</td><td>1 and 2</td><td>Carries signals</td></tr>
<tr><td>Q</td><td>1, 2, 3, 4</td><td>3 and 4</td><td>Squeezes to move the body</td></tr></table>
<p>Do P and Q have the same DNA? How do you know? Why do they have different jobs?</p>
<h3>Part B: Cells in a Siamese cat's ear</h3>
<table border="1" cellpadding="6"><tr><th>Cell type</th><th>Has the gene for the pigment-making protein?</th><th>Makes the pigment-making protein? (X)</th><th>Job</th></tr>
<tr><td>Pigment-making cell</td><td></td><td></td><td>Makes dark color in fur</td></tr>
<tr><td>Skin cell</td><td></td><td></td><td>Covers and protects</td></tr>
<tr><td>Nerve cell</td><td></td><td></td><td>Carries signals</td></tr></table>
<h3>Part C: Where does the changed protein work?</h3>
<p>In a Siamese cat, the pigment-making protein has one amino acid changed. It works only in skin cooler than about 33 &deg;C (a simplified number). Complete the table using the temperatures.</p>
<table border="1" cellpadding="6"><tr><th>Body part</th><th>Skin temperature (&deg;C)</th><th>Does the protein work? (yes or no)</th><th>Fur color (dark or cream)</th></tr>
<tr><td>Ear</td><td>28</td><td></td><td></td></tr><tr><td>Nose</td><td>30</td><td></td><td></td></tr>
<tr><td>Paw</td><td>28</td><td></td><td></td></tr><tr><td>Tail tip</td><td>27</td><td></td><td></td></tr>
<tr><td>Upper leg</td><td>34</td><td></td><td></td></tr><tr><td>Back</td><td>36</td><td></td><td></td></tr><tr><td>Belly</td><td>36</td><td></td><td></td></tr></table>
<ol>
<li>Do all of the cat's cells have the gene for the pigment-making protein?</li>
<li>Which cells make the protein?</li>
<li>Why are only the ears, nose, paws, and tail dark?</li>
<li><strong>Explain.</strong> Use the words DNA, gene, protein, and job to explain why a Siamese cat has dark points.</li>
</ol>
"""

DAY6_PLAN = TEACHER + """
<h2>Day 6: Case data, from a DNA change to the body</h2>
<table border="1" cellpadding="6"><tr><th>Target</th><td>LS1-1.6 (priority): use case data, like sickle cell, to explain how a DNA change affects the body.</td></tr>
<tr><th>Goal</th><td>Students trace a DNA change through a protein to an effect on the body using two cases, and write a claim-evidence-reasoning explanation.</td></tr>
<tr><th>Materials</th><td>Student page.</td></tr>
<tr><th>CFA</th><td>LS1-1.6 (6 minutes)</td></tr></table>
<h3>Plan (45 minutes)</h3>
<ol>
<li><strong>Warm-up (5 min).</strong> Students list the chain from Days 4 and 5 for the cat: one-letter DNA change &rarr; one different amino acid &rarr; protein works only in cool skin &rarr; dark points.</li>
<li><strong>Case 1: the Siamese cat (12 min).</strong> Students complete the chain and the data table.</li>
<li><strong>Case 2: a human gene change (12 min).</strong> A single base change in a human gene changes one amino acid and the protein works poorly. Students complete the chain and compare the cases.</li>
<li><strong>Write (10 min).</strong> Students write a claim-evidence-reasoning explanation (Question 6). Share two samples.</li>
<li><strong>CFA LS1-1.6 (6 min).</strong></li>
</ol>
<h3>Answer key</h3>
<ul>
<li>Case 1 chain: one letter in the gene changes &rarr; one amino acid in the protein is different &rarr; the protein works only below about 33 &deg;C &rarr; pigment is made only in the cool ears, nose, paws, and tail.</li>
<li>Case 1 data: solid cat: normal gene, protein works at every temperature, color everywhere. Siamese cat: one amino acid different, protein works only in cool skin, color only on points.</li>
<li>Case 2 chain: one base in the gene changes &rarr; one amino acid in the chain is different &rarr; the protein works poorly &rarr; symptoms in the body.</li>
<li>Q1 Alike: one DNA letter changes, one amino acid changes, the protein works differently, and the body is affected. Q2 Different: in the cat the protein works at some temperatures and not others; in Case 2 it works poorly overall. Q3 DNA stores the gene, the gene codes for the protein, and the protein does the job, so a change in DNA changes what the protein can do. Q4 A different amino acid changes how the protein works, so it cannot do its job well. Q5 The litter data show the changed gene is inherited from both parents.</li>
<li>Q6 model answer: A one-letter change in the gene for a pigment-making protein caused the dark points. The data show the Siamese cat's protein works only in skin cooler than about 33 degrees, and the ears (28 degrees), nose (30), paws (28), and tail tip (27) are dark while the back (36) and belly (36) are cream. The changed letter swaps one amino acid, so the protein works only in cool skin and pigment is made only in the cooler body parts.</li>
</ul>
"""

DAY6_STUDENT = """{{SLIDES}}
<h2>Day 6: Case data</h2>
<h3>Case 1: Siamese and solid cats</h3>
<table border="1" cellpadding="6"><tr><th></th><th>Solid cat</th><th>Siamese cat</th></tr>
<tr><td>Gene for the pigment-making protein</td><td>Usual sequence</td><td>One letter different</td></tr>
<tr><td>Amino acid chain</td><td>Usual chain</td><td>One amino acid different</td></tr>
<tr><td>Where the protein works</td><td>At every body temperature</td><td>Only in skin cooler than about 33 &deg;C</td></tr>
<tr><td>Fur color</td><td>Dark all over</td><td>Dark ears, nose, paws, tail; cream body</td></tr>
<tr><td>Temperature of ear / back</td><td>28 / 36 &deg;C</td><td>28 / 36 &deg;C</td></tr></table>
<p>Fill in the chain: One letter in the ______ changes &rarr; one ______ in the protein is different &rarr; the protein works only ______ &rarr; pigment is made only on the ______.</p>
<h3>Case 2: A human gene</h3>
<table border="1" cellpadding="6"><tr><th>Person</th><th>Gene</th><th>Protein</th><th>Symptoms</th></tr>
<tr><td>1</td><td>Normal</td><td>Works</td><td>None</td></tr>
<tr><td>2</td><td>One base changed</td><td>One amino acid different; works poorly</td><td>Yes</td></tr></table>
<p>Fill in the chain: One base in the ______ changes &rarr; one ______ in the chain is different &rarr; the ______ works poorly &rarr; ______.</p>
<ol>
<li>How are the two cases alike?</li>
<li>How are they different?</li>
<li>Why does a change in DNA change what a protein can do?</li>
<li>In Case 2, why does a different amino acid cause symptoms?</li>
<li>What do the Day 1 litter data tell you about the changed gene in Case 1?</li>
<li><strong>Write.</strong> Claim: What caused the Siamese cat's dark points? Evidence: use at least two numbers from the data. Reasoning: explain how a one-letter DNA change leads to dark color only on the cooler body parts.</li>
</ol>
"""

DAY7_PLAN = TEACHER + """
<h2>Day 7: Review and return to the Siamese cat</h2>
<table border="1" cellpadding="6"><tr><th>Goal</th><td>Reteach from CFA results; students revise their Day 1 model and write the final explanation of the phenomenon.</td></tr>
<tr><th>Materials</th><td>The Review page (Canvas), students' Day 1 models and CFA scores.</td></tr></table>
<h3>Plan (45 minutes)</h3>
<ol>
<li><strong>Find your focus (5 min).</strong> Students look at their six CFA scores. Below about 67 percent (under 2.7 of 4 points) on a CFA means do the matching Review section. Pull a small group for reteaching if several students are below that mark on the same CFA.</li>
<li><strong>Review sections (20 min).</strong> Students do Vocabulary and the sections for any CFA below 4 (Review page). Answers are on the Review key.</li>
<li><strong>Revise the model (8 min).</strong> Students redraw their Day 1 model with: DNA with the gene, the one-letter change, the copy-then-read path, the amino acid chain with one amino acid different, the protein working only in cool skin, and dark points.</li>
<li><strong>Write It: the Siamese kitten (12 min).</strong> Students write a claim-evidence-reasoning explanation using the data below.</li>
</ol>
<h3>Write It prompt (give to students)</h3>
<p>Two Siamese kittens are raised from birth, one in a warm room and one in a cool room. At 12 weeks the scientists record:</p>
<table border="1" cellpadding="6"><tr><th></th><th>Kitten raised warm</th><th>Kitten raised cool</th></tr>
<tr><td>Ear skin temperature (&deg;C)</td><td>34</td><td>26</td></tr><tr><td>Ear fur color</td><td>Light tan</td><td>Dark brown</td></tr>
<tr><td>Back skin temperature (&deg;C)</td><td>36</td><td>35</td></tr><tr><td>Back fur color</td><td>Cream</td><td>Cream</td></tr></table>
<p>Write an explanation: <strong>Claim</strong> (why the cool-room kitten's ears are darker), <strong>Evidence</strong> (at least two numbers), and <strong>Reasoning</strong> (DNA, gene, protein, and what the amino acid change does).</p>
<h3>Model answer</h3>
<p>Claim: The ears of the cool-room kitten are darker because they are cooler, and the changed pigment-making protein works in cooler skin. Evidence: the cool-room kitten's ear is 26 degrees and dark brown, while the warm-room kitten's ear is 34 degrees and light tan; the backs are 35 and 36 degrees and both cream. Reasoning: Both kittens have the same changed gene, in which one DNA letter swaps one amino acid. The gene is copied and the copy is read to build the protein, and the changed protein works only in skin cooler than about 33 degrees. The cool-room kitten's ears are cooler, so the protein works there and pigment is made. The warm-room kitten's ears are warmer, so the protein works less and little pigment is made. The backs are warm in both, so they stay cream.</p>
<h3>Scoring (4 points)</h3>
<ul><li>4: correct claim, two or more accurate data points, complete reasoning (DNA, gene, protein, temperature).</li><li>3: correct claim and data, one piece of the reasoning thin.</li><li>2: partly correct claim, one data point, vague reasoning.</li><li>1: wrong claim or misconception (for example, the cat changes color on purpose).</li></ul>
"""

DAY7_STUDENT = """{{SLIDES}}
<h2>Day 7: Review and back to the cat</h2>
<h3>Part 1: Review</h3>
<p>Open the HS-LS1-1 Review page. Do Vocabulary and the section for any CFA where you scored below about 67 percent. List the sections you did: ______________</p>
<h3>Part 2: Revise your Day 1 model</h3>
<p>Redraw your model of what is inside a Siamese cat's cells. Show: DNA with the gene, the one-letter change, the copy-then-read path, the amino acid chain with one amino acid different, the protein working only in cool skin, and the dark points. Upload a photo or describe your drawing in words.</p>
<h3>Part 3: Write It</h3>
<p>Two Siamese kittens are raised from birth, one in a warm room and one in a cool room. At 12 weeks the scientists record:</p>
<table border="1" cellpadding="6"><tr><th></th><th>Kitten raised warm</th><th>Kitten raised cool</th></tr>
<tr><td>Ear skin temperature (&deg;C)</td><td>34</td><td>26</td></tr><tr><td>Ear fur color</td><td>Light tan</td><td>Dark brown</td></tr>
<tr><td>Back skin temperature (&deg;C)</td><td>36</td><td>35</td></tr><tr><td>Back fur color</td><td>Cream</td><td>Cream</td></tr></table>
<p>Write an explanation. <strong>Claim:</strong> why are the cool-room kitten's ears darker? <strong>Evidence:</strong> use at least two numbers. <strong>Reasoning:</strong> use DNA, gene, protein, and what the amino acid change does.</p>
"""

DAY8_PLAN = TEACHER + """
<h2>Day 8: CSA</h2>
<ul>
<li>CSA: HS-LS1-1, DNA to Proteins. 4 points in Canvas (30 raw points scaled down): 6 vocabulary matches, 8 multiple choice, 2 free response. Allow the full 45 minutes.</li>
<li>The code table is included in the questions that need it. Calculators are not needed.</li>
<li>The free-response items are scored with the 4-point rubrics in the Canvas question comments.</li>
<li>After the test (next class): return the CSA, review the two free-response exemplars, and ask students to compare them with their own answers. Revisit the Siamese cat: <em>What would you add to your Day 1 model now?</em></li>
</ul>
"""

MATERIALS_PAGE = TEACHER + """
<h2>Unit materials and prep</h2>
<table border="1" cellpadding="6">
<tr><th>Day</th><th>You need</th></tr>
<tr><td>1</td><td>Projected photos of an adult Siamese cat and a white newborn Siamese kitten; student page (print or share the Canvas page)</td></tr>
<tr><td>2</td><td>Student page, colored pencils, scissors, tape or glue</td></tr>
<tr><td>3 (lab)</td><td>Per pair: 2 licorice strands, 24 candy bases in four colors (6 each, plus a few spare), toothpicks, paper plate, printed lab sheet and code table. Allergy-free or non-food alternatives: colored beads and pipe cleaners, or colored paper circles.</td></tr>
<tr><td>4</td><td>Student page (card sort), printed on card stock if you want reusable cards</td></tr>
<tr><td>5</td><td>Student page, two colors of pencil</td></tr>
<tr><td>6</td><td>Student page</td></tr>
<tr><td>7</td><td>Review page, Day 1 models, CFA scores</td></tr>
<tr><td>8</td><td>CSA (Canvas quiz, 45-minute limit)</td></tr></table>
<h3>Science background (for you)</h3>
<ul>
<li>The Siamese (colorpoint) pattern is linked to a single-base change in the tyrosinase gene (TYR), which makes a pigment-producing protein. The change swaps one amino acid (reported as glycine to arginine; sources number the residue differently). The changed protein works only in cooler skin, so pigment is made only on the ears, face, paws, and tail. A newborn kitten is warm all over in the womb, so it is born pale. Cats in cooler places end up darker. Source: Lyons et al., 2005.</li>
<li>The pattern is a recessive trait: a kitten needs two changed copies, one from each parent. Class litter data, temperatures, and the DNA letters are simplified illustrations. The 33-degree threshold is a simplified class number.</li>
<li>Assessment boundary: no identification of specific cell or tissue types, whole body systems, specific protein structures and functions, or the biochemistry of protein synthesis. The cat is the context; the CSA does not require knowing anything about cats. Do not go into how the protein makes pigment or how it folds.</li>
</ul>
"""

SCORING = "<h3>How this is scored (4 points)</h3><ul><li>4: complete and accurate</li><li>3: mostly complete, a few errors</li><li>2: partly complete or several errors</li><li>1: started</li></ul>"

LESSONS = {
    "Day 1: Launch with the Siamese cat": [("page", "Day 1 Teacher Plan: Launch", DAY1_PLAN), ("assignment", "Day 1 Student Assignment: Why are a Siamese cat's ears, paws, and tail dark?", DAY1_STUDENT + SCORING, 4)],
    "Day 2: What is DNA made of?": [("page", "Day 2 Teacher Plan: DNA structure", DAY2_PLAN), ("assignment", "Day 2 Student Assignment: What is DNA made of?", DAY2_STUDENT + SCORING, 4)],
    "Day 3: LAB, build, copy, and read a gene (gummy DNA)": [("page", "Day 3 Teacher Plan: Gummy DNA Lab", DAY3_PLAN), ("page", "Day 3 Teacher Key and Prep: Gummy DNA Lab", LAB_TEACHER), ("assignment", "Gummy DNA Lab Sheet", LAB_STUDENT + SCORING, 4)],
    "Day 4: What can one letter do?": [("page", "Day 4 Teacher Plan: One-letter changes", DAY4_PLAN), ("assignment", "Day 4 Student Assignment: What can one letter do?", DAY4_STUDENT + SCORING, 4)],
    "Day 5: Same DNA, different jobs": [("page", "Day 5 Teacher Plan: Same DNA, different jobs", DAY5_PLAN), ("assignment", "Day 5 Student Assignment: Same DNA, different jobs", DAY5_STUDENT + SCORING, 4)],
    "Day 6: Case data": [("page", "Day 6 Teacher Plan: Case data", DAY6_PLAN), ("assignment", "Day 6 Student Assignment: Case data", DAY6_STUDENT + SCORING, 4)],
    "Day 7: Review and back to the cat": [("page", "Day 7 Teacher Plan: Review and Write It", DAY7_PLAN), ("assignment", "Day 7 Student Assignment: Review, revise your model, and Write It", DAY7_STUDENT + SCORING, 4)],
    "Day 8: CSA": [("page", "Day 8 Teacher Plan: CSA", DAY8_PLAN)],
}
