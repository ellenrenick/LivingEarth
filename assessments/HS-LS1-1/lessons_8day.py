"""Lesson pages for the 8-day version of unit 2.1, built around the anchoring phenomenon of six-toed (polydactyl) cats.

Each day has items created in Canvas in order: teacher plans and student pages (type "page") and the lab
sheet (type "assignment"). Everything is created unpublished. The CFA for the day is added by canvas_unit.py.

Science notes (verified): in Hemingway and other polydactyl cats, the extra toes are linked to a single-base
change in the ZRS, a stretch of DNA that acts like a switch for the SHH gene. The change makes the SHH
signal protein in an extra place in the developing paw. The trait is inherited as a dominant, but it does not always
show (incomplete penetrance, variable expression). The base sequences used in class are illustrations, not the real sequence.
"""

CODE_TABLE = ("<table border=\"1\" cellpadding=\"6\"><tr><th>DNA triplet</th><th>Amino acid</th><th>DNA triplet</th><th>Amino acid</th></tr>"
              "<tr><td>ATG</td><td>Met</td><td>GAG</td><td>Glu</td></tr><tr><td>CTG</td><td>Leu</td><td>GTG</td><td>Val</td></tr>"
              "<tr><td>TTT</td><td>Phe</td><td>GAC</td><td>Asp</td></tr><tr><td>CCT</td><td>Pro</td><td>GGC</td><td>Gly</td></tr></table>")

LITTERS = ("<table border=\"1\" cellpadding=\"6\"><tr><th>Litter</th><th>Mother</th><th>Father</th><th>Six-toed kittens</th><th>Five-toed kittens</th></tr>"
           "<tr><td>1</td><td>Six-toed</td><td>Five-toed</td><td>3</td><td>3</td></tr>"
           "<tr><td>2</td><td>Five-toed</td><td>Six-toed</td><td>2</td><td>3</td></tr>"
           "<tr><td>3</td><td>Five-toed</td><td>Five-toed</td><td>0</td><td>5</td></tr>"
           "<tr><td>4</td><td>Six-toed</td><td>Six-toed</td><td>5</td><td>2</td></tr>"
           "<tr><td>5</td><td>Six-toed</td><td>Five-toed</td><td>3</td><td>2</td></tr>"
           "<tr><td>6</td><td>Five-toed</td><td>Five-toed</td><td>0</td><td>4</td></tr>"
           "<tr><td>7</td><td>Five-toed</td><td>Six-toed</td><td>3</td><td>3</td></tr></table>"
           "<p><em>Simplified class data set modeled on real litter patterns. &ldquo;Six-toed&rdquo; means extra toes on at least one paw.</em></p>")

TEACHER = "<p style=\"background:#fff3cd;padding:6px\"><strong>TEACHER PAGE.</strong> Includes answers. Do not share with students.</p>"

DAY1_PLAN = TEACHER + """
<h2>Day 1: Launch with the six-toed cats</h2>
<table border="1" cellpadding="6"><tr><th>Targets</th><td>LS1-1.2 (priority): DNA holds the instructions for building proteins. LS3-1 (supporting, light): chromosomes, DNA, and genes; one set from each parent.</td></tr>
<tr><th>Goal</th><td>Students notice and wonder about six-toed cats, find a pattern in inheritance, and start an initial model of what is in the cells.</td></tr>
<tr><th>Materials</th><td>A projected photo of a polydactyl (six-toed) cat paw (search &ldquo;polydactyl cat paw&rdquo;); the student page below; optional: a ball of yarn to show &ldquo;long strand, many genes.&rdquo;</td></tr>
<tr><th>CFA</th><td>LS1-1.2 (6 minutes, last 6 minutes of class)</td></tr></table>
<h3>Plan (45 minutes)</h3>
<ol>
<li><strong>Notice and wonder (6 min).</strong> Project the photo. Tell students a typical cat has 18 toes (5 on each front paw, 4 on each back paw). Students count the toes in the photo and write 2 noticings and 2 wonderings on the student page. Collect wonderings on the board. Steer toward: <em>Why do some cats have extra toes? Is it passed from parents? What is different inside the cat?</em></li>
<li><strong>The Hemingway cats (6 min).</strong> Read aloud: Ernest Hemingway's home in Key West, Florida, is now a museum with about 50 to 60 cats living on the property. About half of them have extra toes, often 6 on a paw. They are descendants of a six-toed cat that a ship captain gave Hemingway in the 1930s. Ask: <em>Where could a trait like that come from?</em> (Accept: eaten, caught, injury, born with it, parents.)</li>
<li><strong>Look for patterns in data (10 min).</strong> Students study the litter table on the student page in pairs and answer Questions 1 to 4. Debrief: six-toed &times; five-toed litters are about half six-toed (11 of 22), five-toed &times; five-toed litters have none (0 of 9), six-toed &times; six-toed litters have most six-toed (5 of 7). Both mothers and fathers pass the trait. So the trait is inherited, but what is actually passed on?</li>
<li><strong>Mini-lesson: what is passed on (12 min).</strong> Use the Key Ideas box on the student page. Write on the board: <em>DNA &rarr; gene &rarr; protein &rarr; job in the cell.</em> A kitten gets one set of chromosomes (each a very long DNA molecule, with many genes) from its mother and one from its father (LS3-1, light). A <strong>gene</strong> is a section of DNA with the instructions for one protein. <strong>Proteins</strong> do the jobs of the cell. Teaser: the cats' extra toes come from a one-letter difference in their DNA. We will find out how a tiny DNA difference can build a bigger paw.</li>
<li><strong>Practice (5 min).</strong> Students answer Questions 5 to 7.</li>
<li><strong>Initial model (3 min).</strong> Students sketch Question 8, their first model of what is in a cat's cells that leads to extra toes. Keep it; they revise it on Day 7.</li>
<li><strong>CFA LS1-1.2 (6 min).</strong> Canvas quiz, exit ticket.</li>
</ol>
<h3>Answer key for the student page</h3>
<ol>
<li>Six-toed &times; five-toed litters: 11 of 22 kittens are six-toed (half). Five-toed &times; five-toed: none of 9. Six-toed &times; six-toed: 5 of 7.</li>
<li>Yes, six-toed parents have six-toed kittens, and five-toed parents have only five-toed kittens, so the trait is passed from parent to kitten.</li>
<li>Both. Litters with a six-toed mother (1, 5) and with a six-toed father (2, 7) both have six-toed kittens.</li>
<li>It is not caused by diet or a disease the kittens caught, because five-toed parents do not have six-toed kittens, and six-toed parents' kittens are born with it. Something inherited is the best explanation.</li>
<li>DNA.</li>
<li>A gene; a protein.</li>
<li>One set from the mother and one set from the father.</li>
<li>Look for: DNA or genes inside the cells, passed from both parents, that build the extra toe. Do not correct yet.</li>
</ol>
<h3>Notes</h3>
<ul><li>Some sources differ on the founding cat's name (Snow White or Snowball). Leave the name out unless students ask.</li>
<li>The trait is inherited as a dominant, but it does not always show, so a few litters in real populations break the pattern. The class data set is simplified.</li></ul>
"""

DAY1_STUDENT = """
<h2>Day 1: Why do some cats have extra toes?</h2>
<h3>Notice and wonder</h3>
<p>A typical cat has 18 toes: 5 on each front paw and 4 on each back paw. Look at the photo of a six-toed cat.</p>
<p>I notice: __________________________ &nbsp; I notice: __________________________</p>
<p>I wonder: __________________________ &nbsp; I wonder: __________________________</p>
<h3>The Hemingway cats</h3>
<p>Ernest Hemingway's house in Key West, Florida, is now a museum. About 50 to 60 cats live there, and about half of them have extra toes. They are descended from a six-toed cat given to Hemingway in the 1930s.</p>
<h3>Data: litters of kittens</h3>
""" + LITTERS + """
<ol>
<li>Describe the pattern for each type of pair: six-toed &times; five-toed, five-toed &times; five-toed, and six-toed &times; six-toed.</li>
<li>Is the trait passed from parents to kittens? What is your evidence?</li>
<li>Does the trait come from the mother, the father, or both? What is your evidence?</li>
<li>Could the extra toes be caused by what the kittens ate or a disease they caught? Why or why not?</li>
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
<li>The molecule that stores the instructions in the cells of a cat is ______.</li>
<li>A section of DNA with the instructions for one protein is a ______. Its product, which does jobs for the cell, is a ______.</li>
<li>How many sets of chromosomes does a kitten get from each parent?</li>
<li><strong>Initial model.</strong> Draw and label a model of what is inside a cat's cells that leads to extra toes. Use arrows. We will revise it on Day 7.</li>
</ol>
"""

DAY2_PLAN = TEACHER + """
<h2>Day 2: What is DNA made of?</h2>
<table border="1" cellpadding="6"><tr><th>Target</th><td>LS1-1.1 (priority): DNA is a double helix built from nucleotides, each with a sugar, a phosphate, and a base.</td></tr>
<tr><th>Goal</th><td>Students describe DNA's structure and base pairing, and see that the message is the order of the bases. Prepares for the lab on Day 3.</td></tr>
<tr><th>Materials</th><td>Student page; colored pencils; scissors and tape or glue (for the nucleotide cut-out); the base pairing card strips printed from the student page.</td></tr>
<tr><th>CFA</th><td>LS1-1.1 (6 minutes)</td></tr></table>
<h3>Plan (45 minutes)</h3>
<ol>
<li><strong>Warm-up (5 min).</strong> Ask: <em>Yesterday we said DNA holds the instructions for the extra toes. What do you think DNA looks like?</em> Students sketch for 1 minute, then share.</li>
<li><strong>Mini-lesson (12 min).</strong> Draw and build up on the board: one nucleotide (a pentagon for sugar, a circle for phosphate, a rectangle for the base); a strand of nucleotides joined sugar to phosphate (the backbone); the four bases A, T, C, G; the second strand; pairing rules A with T, C with G; the twist into a double helix. Key point: <strong>the order of the bases is the message.</strong> A cat has billions of bases in its DNA; a gene is a stretch of them.</li>
<li><strong>Activity: build it on paper (14 min).</strong> Students complete Parts A to C on the student page: cut out and label a nucleotide, write the partner strand for three sequences using the pairing rules, and answer the questions.</li>
<li><strong>Connect to the cats (4 min).</strong> Show the illustration on the student page: two cats' DNA in the same place, differing by one letter. Ask: <em>Could one letter make a six-toed cat?</em> We find out on Day 4. State clearly that the sequences are an illustration, not the real ones.</li>
<li><strong>CFA LS1-1.1 (6 min).</strong></li>
</ol>
<h3>Answer key for the student page</h3>
<ul>
<li>Part A: sugar (pentagon), phosphate (circle), base (rectangle) are the three parts of a nucleotide. The sugar and phosphate form the backbone of each strand.</li>
<li>Part B: (1) A T G C C T &rarr; T A C G G A. (2) T T T G A C &rarr; A A A C T G. (3) C T G G A G &rarr; G A C C T C.</li>
<li>Part C: 1. A double helix (twisted ladder). 2. The backbone: sugar and phosphate; the rungs: pairs of bases. 3. A pairs with T; C pairs with G. 4. The order of the bases. 5. Illustration answer: they differ at one position (the fifth letter, G versus A).</li>
</ul>
"""

DAY2_STUDENT = """
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
<p>Use the pairing rules (A with T, C with G).</p>
<ol>
<li>A T G C C T &rarr; ______________</li>
<li>T T T G A C &rarr; ______________</li>
<li>C T G G A G &rarr; ______________</li>
</ol>
<h3>Part C: Questions</h3>
<ol>
<li>What shape is DNA?</li>
<li>What makes up the sides of the ladder? What makes up the rungs?</li>
<li>Which bases pair together?</li>
<li>What makes one gene different from another?</li>
<li><strong>Illustration only.</strong> Here is the same stretch of DNA from two cats (these letters are made up to show the idea, not the real sequence):<br>
Five-toed cat: &hellip; A C G G <u>G</u> T C A &hellip;<br>
Six-toed cat: &nbsp;&hellip; A C G G <u>A</u> T C A &hellip;<br>
How many letters differ? Where?</li>
</ol>
"""

LAB_STUDENT = """
<h2>Gummy DNA Lab: Build, Copy, and Read a Gene</h2>
<p><strong>Name:</strong> ______________ &nbsp; <strong>Partner:</strong> ______________</p>
<p><strong>Question:</strong> How does a cell's copy of a gene become a chain of amino acids, and what happens if one letter of DNA changes?</p>
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
<p>This is the strand of your gene that the cell uses as a template. Using toothpicks, attach the bases to one licorice strand in order from left to right:</p>
<p><strong>T A C &nbsp; C T C &nbsp; G A C &nbsp; A A A</strong></p>
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
<li>Pull the two strands apart. Keep the template strand. Build a <em>new</em> strand by pairing with the template (A with T, C with G). This new strand is the <strong>copy</strong>. Write its sequence: ___ ___ ___ ___</li>
<li>Read the copy three letters at a time with the code table. Write the amino acid chain: ______ &ndash; ______ &ndash; ______ &ndash; ______</li>
<li>Put the amino acid chain in order on the plate using one bead or paper tag per amino acid. This chain would fold to make a protein.</li>
<li>Explain the path in your own words, starting with the DNA: ______________________________________________</li>
</ol>
<h3>Part D: Change one letter (7 min)</h3>
<ol>
<li>On your template strand, replace the 5th base (the T in the second triplet, C&#8203;T&#8203;C) with an A (swap a yellow gummy for a red one). The template now reads <strong>TAC CAC GAC AAA</strong>.</li>
<li>Build the new copy by pairing with the changed template. Sequence: ___ ___ ___ ___</li>
<li>Read it with the code table: ______ &ndash; ______ &ndash; ______ &ndash; ______</li>
<li>Compare with Part C. How many amino acids changed? Which one?</li>
<li>Predict: Could a protein built from this changed chain work differently? Explain.</li>
</ol>
<h3>Connect to the cats</h3>
<ol>
<li>In the six-toed cats, a one-letter change in DNA is found in a stretch of DNA near a gene. In the model you changed one letter inside a gene. In your own words, what did your one-letter change do to the protein in the model?</li>
<li>Name two ways your gummy model is different from real DNA (for example, size, what it is made of).</li>
</ol>
<h3>Clean up</h3>
<p>Put toothpicks and candy in the trash or the labeled container. Wipe your table. Wash your hands.</p>
"""

LAB_TEACHER = TEACHER + """
<h2>Day 3 Teacher Key: Gummy DNA Lab</h2>
<table border="1" cellpadding="6"><tr><th>Targets</th><td>LS1-1.3 (priority): a gene's message is copied and the copy is read to build a chain of amino acids. Applies LS1-1.1 (DNA structure).</td></tr>
<tr><th>Prep (15 min before class)</th><td>For each pair: 2 licorice strands (6 to 8 inches, such as Twizzlers or Red Vines), 24 candy bases (6 each of four colors, plus a few spare), a handful of toothpicks, a paper plate. Print the lab sheet and the code table. Fruit-snack or gummy candies work; if you cannot use food (gelatin, allergies, or policy), use colored beads and pipe cleaners or paper circles taped to paper strips.</td></tr>
<tr><th>CFA</th><td>LS1-1.3 (6 minutes; give it first if the lab runs long and finish Part D at the start of Day 4)</td></tr></table>
<h3>Timing (45 minutes)</h3>
<ol><li>Intro and safety (5 min): the copy-then-read idea; show a pre-built strand.</li><li>Part A (6 min).</li><li>Part B (8 min).</li><li>Part C (10 min).</li><li>Part D (5 min).</li><li>Clean up and CFA (11 min). Move quickly through Part D if short on time.</li></ol>
<h3>Answer key</h3>
<ul>
<li><strong>Part A</strong> (colors in order): yellow, red, green, green, yellow, green, orange, red, green, red, red, red.</li>
<li><strong>Part B</strong> partner strand: A T G &nbsp; G A G &nbsp; C T G &nbsp; T T T. Coding strand = the partner strand (it matches the copy the cell makes). Check the ladder: A with T, C with G.</li>
<li><strong>Part C</strong>: the copy (pairing with the template) is <strong>A T G G A G C T G T T T</strong>. Chain: <strong>Met &ndash; Glu &ndash; Leu &ndash; Phe</strong>. Explanation: the gene's message is copied from the template strand, and the copy is read three letters at a time to link amino acids in order.</li>
<li><strong>Part D</strong>: the changed template TAC CAC GAC AAA gives the copy ATG GTG CTG TTT, which reads <strong>Met &ndash; Val &ndash; Leu &ndash; Phe</strong>. One amino acid changed (the second, Glu to Val). Yes, a different chain can fold into a protein that works differently.</li>
<li><strong>Connect</strong>: (1) One amino acid in the chain changed, so the protein could work differently. (2) Accept: candy versus molecules, the model is huge compared to real DNA, real DNA has sugar and phosphate in every nucleotide and twists differently, real genes are thousands of bases long.</li>
</ul>
<h3>Teaching notes</h3>
<ul>
<li>Teach copy-then-read only. Do not teach mRNA, tRNA, or ribosome mechanics (outside the assessment boundary). Say &ldquo;the cell copies the gene's message.&rdquo;</li>
<li>Common mistakes: matching A with C or G; reading the template strand directly instead of the copy; reading in the wrong grouping (always groups of three from the start).</li>
<li>Grade the lab sheet out of 12 for completion and accuracy: Part A 1, Part B 2, Part C 4, Part D 3, Connect 2.</li>
<li>Honest limit of the model: in the cats, the one-letter change is not inside the gene's amino acid code; Day 4 explains this difference.</li>
</ul>
"""

DAY3_PLAN = TEACHER + """
<h2>Day 3: Lab day, Build, Copy, and Read a Gene (gummy DNA)</h2>
<p>This is the one hands-on lab and the one day on how a gene's message is copied and read. See the <strong>Teacher Key and Prep</strong> page for materials, timing, and answers, and the <strong>Lab Sheet</strong> assignment for students.</p>
<ol><li>Intro (5): <em>On Day 1 we asked what is in a cat's cells that makes extra toes. Today we build a gene and watch how its message is copied and read.</em></li>
<li>Lab, Parts A to D (about 29 min).</li>
<li>CFA LS1-1.3 (6 min) and clean up.</li></ol>
"""

DAY4_PLAN = TEACHER + """
<h2>Day 4: What can one letter do?</h2>
<table border="1" cellpadding="6"><tr><th>Target</th><td>LS1-1.4 (priority): changing one DNA base can change a protein and what it does.</td></tr>
<tr><th>Goal</th><td>Students sort one-letter DNA changes by their effect, see that not every change matters, and place the cats' change in a category.</td></tr>
<tr><th>Materials</th><td>Student page and card strips (cut into 6 cards per group); gummy models from Day 3 if kept.</td></tr>
<tr><th>CFA</th><td>LS1-1.4 (6 minutes)</td></tr></table>
<h3>Plan (45 minutes)</h3>
<ol>
<li><strong>Warm-up (5 min).</strong> Finish Part D from the lab: how many amino acids changed when one letter changed? Recap: base order sets amino acid order.</li>
<li><strong>Mini-lesson (10 min).</strong> A one-letter change can do one of three things: (1) change an amino acid in the chain, which can change how the protein works; (2) change where or when the gene is used, because the DNA near a gene contains switches that turn it on and off; (3) change nothing noticeable (the amino acid is the same, or the change is in a stretch with no role). Not every change matters.</li>
<li><strong>Card sort (15 min).</strong> Groups sort the six cards into the three categories and justify each (student page).</li>
<li><strong>The cats (8 min).</strong> The extra toes are linked to a one-letter change in a switch for a gene called SHH. The cat's SHH protein itself is normal; the change makes the protein in an extra place while the paw forms. Which category? (Category 2.) Preview Day 5.</li>
<li><strong>CFA LS1-1.4 (6 min).</strong></li>
</ol>
<h3>Answer key for the card sort</h3>
<ul>
<li>Card A (GAG &rarr; GTG, Glu &rarr; Val): Category 1.</li>
<li>Card B (GAG &rarr; GAA, Glu &rarr; Glu): Category 3 (same amino acid).</li>
<li>Card C (cat: one letter in the switch region for SHH): Category 2.</li>
<li>Card D (CTG &rarr; CCG, Leu &rarr; Pro): Category 1.</li>
<li>Card E (a one-letter change in a stretch of DNA with no gene or switch): Category 3.</li>
<li>Card F (a letter change that turns a gene's switch off, so the protein is not made): Category 2.</li>
<li>Claim check: &ldquo;Every change in DNA changes how a cell works.&rdquo; Not supported: cards B and E show no effect.</li>
</ul>
<h3>Notes</h3>
<ul><li>GAA also codes for Glu, so card B is a real &ldquo;same amino acid&rdquo; change. CCG codes for Pro.</li>
<li>Simplification to say out loud: the cats' change is outside the part of the gene that sets the amino acid order. It is a good example of a DNA letter changing what a cell does through a protein, which is the Day 5 and 6 idea.</li></ul>
"""

DAY4_STUDENT = """
<h2>Day 4: What can one letter do?</h2>
<h3>Key ideas</h3>
<ul>
<li>A one-letter change in DNA can (1) change an amino acid in the chain, (2) change where or when a gene is used (a switch changes), or (3) change nothing noticeable.</li>
<li>Not every change matters.</li>
</ul>
<h3>Card sort</h3>
<p>Cut out the cards. Sort them into three groups and write your reason on each. Use the code table. Also: GAA = Glu, CCG = Pro.</p>
""" + CODE_TABLE + """
<table border="1" cellpadding="6">
<tr><th>Card</th><th>What changed</th></tr>
<tr><td>A</td><td>A gene's triplet changes from GAG to GTG.</td></tr>
<tr><td>B</td><td>A gene's triplet changes from GAG to GAA.</td></tr>
<tr><td>C</td><td>In a cat, one letter changes in a switch for the SHH gene. The SHH protein itself is normal, but it is now made in an extra place in the developing paw.</td></tr>
<tr><td>D</td><td>A gene's triplet changes from CTG to CCG.</td></tr>
<tr><td>E</td><td>One letter changes in a stretch of DNA that has no gene and no switch.</td></tr>
<tr><td>F</td><td>One letter changes in a switch so the gene can no longer be turned on, and its protein is not made.</td></tr>
</table>
<p><strong>Category 1:</strong> changes an amino acid in the chain. <strong>Category 2:</strong> changes where, when, or whether the gene is used. <strong>Category 3:</strong> no noticeable change.</p>
<ol>
<li>Write the cards in each category and your reasons.</li>
<li>A student says, &ldquo;Every change in DNA changes how a cell works.&rdquo; Use the cards to respond.</li>
<li>Which category does the cats' extra-toe change belong to? Explain.</li>
</ol>
"""

DAY5_PLAN = TEACHER + """
<h2>Day 5: Same DNA, different jobs</h2>
<table border="1" cellpadding="6"><tr><th>Target</th><td>LS1-1.5 (priority): DNA, through proteins, gives different cells their different jobs.</td></tr>
<tr><th>Goal</th><td>Students explain that all cells have the same genes but use different ones, and use this to explain how a switch change can build an extra toe.</td></tr>
<tr><th>Materials</th><td>Student page; two colors of pencil.</td></tr>
<tr><th>CFA</th><td>LS1-1.5 (6 minutes)</td></tr></table>
<h3>Plan (45 minutes)</h3>
<ol>
<li><strong>Warm-up (5 min).</strong> Ask: <em>Your skin cells and your nerve cells have the same DNA. Why are they so different?</em> Collect ideas.</li>
<li><strong>Mini-lesson (10 min).</strong> Every cell has all the genes, but each kind of cell uses a different set. The proteins a cell makes decide its job. A gene's switches decide when and where it is used.</li>
<li><strong>Activity: map the developing paw (17 min).</strong> Students color the paw-bud diagram: the paw forms as a small bud with six zones from front (thumb side) to back (pinky side). Every zone has the SHH gene. In a five-toed cat, the SHH signal protein is made only in zone 6 (the back edge) and helps set up the toes. In a six-toed cat, the changed switch also turns on SHH in zone 1 (the front edge). Students complete the table and questions.</li>
<li><strong>Explain it (7 min).</strong> Students write the Question 4 explanation using &ldquo;same DNA, different genes used, different proteins, different jobs.&rdquo;</li>
<li><strong>CFA LS1-1.5 (6 min).</strong></li>
</ol>
<h3>Answer key</h3>
<ul>
<li>Table: all six zones have the SHH gene in both cats. SHH is made in zone 6 only (five-toed cat); in zones 6 and 1 (six-toed cat).</li>
<li>Q1: Yes, the same DNA, including the SHH gene, in every zone. Q2: Zone 6 (five-toed); zones 1 and 6 (six-toed). Q3: The extra SHH signal in zone 1 changes what the cells there do, so an extra toe forms.</li>
<li>Q4 model answer: Every cell in the paw has the same DNA, including the SHH gene. In a five-toed cat only the back-edge cells use it. In a six-toed cat a changed switch also turns it on in the front-edge cells, so those cells make the SHH protein and an extra toe forms.</li>
<li>Cell types P and Q: same genes 1 to 4; P uses 1 and 2, Q uses 3 and 4; different proteins, so different jobs.</li>
</ul>
<h3>Notes</h3>
<ul><li>Keep to the level in the standard: protein signals and cell jobs. Do not go into the chemistry of how SHH works.</li>
<li>Real extra toes in these cats are on the front (thumb) side of the paw, matching the extra SHH zone.</li></ul>
"""

DAY5_STUDENT = """
<h2>Day 5: Same DNA, different jobs</h2>
<h3>Key ideas</h3>
<ul>
<li>Every cell has the same DNA, including all the genes.</li>
<li>Each kind of cell uses a different set of genes, makes different proteins, and so has a different job.</li>
<li>Switches in the DNA decide when and where a gene is used.</li>
</ul>
<h3>Part A: Two kinds of cells</h3>
<table border="1" cellpadding="6"><tr><th>Cell type</th><th>Genes in the cell</th><th>Proteins made</th><th>Job</th></tr>
<tr><td>P</td><td>1, 2, 3, 4</td><td>1 and 2</td><td>Carries signals</td></tr>
<tr><td>Q</td><td>1, 2, 3, 4</td><td>3 and 4</td><td>Squeezes to move the body</td></tr></table>
<p>Do P and Q have the same DNA? How do you know? Why do they have different jobs?</p>
<h3>Part B: The developing paw</h3>
<p>A kitten's paw forms as a small bud with six zones, from the front (thumb) side, zone 1, to the back (pinky) side, zone 6. Every zone has the SHH gene. Complete the table.</p>
<table border="1" cellpadding="6"><tr><th>Zone</th><th>1 (front)</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6 (back)</th></tr>
<tr><td>Has the SHH gene? (both cats)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>SHH protein made, five-toed cat (mark X)</td><td></td><td></td><td></td><td></td><td></td><td>X</td></tr>
<tr><td>SHH protein made, six-toed cat (mark X)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>
<p>For a six-toed cat, a one-letter change in the SHH switch turns the gene on in zone 1 as well as zone 6.</p>
<ol>
<li>Do all the zones have the same DNA?</li>
<li>In which zones is the SHH protein made in a five-toed cat? In a six-toed cat?</li>
<li>What does the extra SHH protein in zone 1 change?</li>
<li><strong>Explain.</strong> Use the words DNA, gene, protein, and job to explain how a one-letter change in a switch can lead to an extra toe.</li>
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
<li><strong>Warm-up (5 min).</strong> Students list the chain from Day 5 for the cat: DNA switch change &rarr; SHH made in an extra place &rarr; extra toe.</li>
<li><strong>Case 1: the cats (12 min).</strong> Students complete the chain and the data table on the student page.</li>
<li><strong>Case 2: a human protein-coding case (12 min).</strong> A single base change in a gene changes one amino acid and the protein works poorly. Students complete the chain and compare the two cases.</li>
<li><strong>Write (10 min).</strong> Students write a claim-evidence-reasoning explanation (Question 6). Share two samples.</li>
<li><strong>CFA LS1-1.6 (6 min).</strong></li>
</ol>
<h3>Answer key</h3>
<ul>
<li>Case 1 chain: one-letter change in the SHH switch &rarr; the switch turns SHH on in an extra zone &rarr; SHH protein is made in the front edge of the paw &rarr; an extra toe forms. Case 1 data: five-toed cats have the SHH protein only in zone 6 (1 zone) and 18 toes; six-toed cats have it in zones 1 and 6 (2 zones) and 20 or more toes.</li>
<li>Case 2 chain: one base in a gene changes &rarr; one amino acid in the chain is different &rarr; the protein works poorly &rarr; symptoms in the body.</li>
<li>Compare: both start with a one-letter DNA change and end with an effect on the body through a protein. In Case 1 the protein is normal but made in the wrong place; in Case 2 the protein itself is different.</li>
<li>Q5: The data show it is inherited from a parent (matches Day 1) and that a DNA change can be the cause.</li>
<li>Q6 model answer: A one-letter change in the DNA switch for the SHH gene caused the extra toe. The data show that SHH protein is made in 2 zones of the developing paw in six-toed cats compared with 1 zone in five-toed cats, and six-toed cats have 20 or more toes compared with 18. The switch change makes cells in the front edge of the paw use the SHH gene, so they make the SHH protein, which changes what those cells do and builds an extra toe.</li>
</ul>
<h3>Notes</h3>
<ul><li>The data in Case 1 are simplified for class. The condition is inherited as a dominant trait that does not always show, so a five-toed cat can carry the change; mention this as an extension.</li></ul>
"""

DAY6_STUDENT = """
<h2>Day 6: Case data</h2>
<h3>Case 1: Six-toed cats</h3>
<table border="1" cellpadding="6"><tr><th></th><th>Five-toed cat</th><th>Six-toed cat</th></tr>
<tr><td>DNA of the SHH switch</td><td>Usual sequence</td><td>One letter different</td></tr>
<tr><td>Zones of the developing paw that make SHH protein</td><td>1 zone (back edge)</td><td>2 zones (front and back edges)</td></tr>
<tr><td>Toes (typical)</td><td>18</td><td>20 or more</td></tr></table>
<p>Fill in the chain: One-letter change in the ______ &rarr; ______ is made in an extra zone &rarr; ______ forms.</p>
<h3>Case 2: A change inside a gene (human)</h3>
<table border="1" cellpadding="6"><tr><th>Person</th><th>Gene</th><th>Protein</th><th>Symptoms</th></tr>
<tr><td>1</td><td>Normal</td><td>Works</td><td>None</td></tr>
<tr><td>2</td><td>One base changed</td><td>One amino acid different; works poorly</td><td>Yes</td></tr></table>
<p>Fill in the chain: One base in the ______ changes &rarr; one ______ in the chain is different &rarr; the ______ works poorly &rarr; ______.</p>
<ol>
<li>How are the two cases alike?</li>
<li>How are they different?</li>
<li>Why does the extra SHH protein need DNA, a gene, and a protein to build an extra toe?</li>
<li>In Case 2, why does a different amino acid cause symptoms?</li>
<li>What does the Day 1 litter data tell you about Case 1?</li>
<li><strong>Write.</strong> Claim: What caused the extra toe in the six-toed cat? Evidence: use at least two numbers from Case 1. Reasoning: explain how a one-letter DNA change leads to a protein made in an extra place and an extra toe.</li>
</ol>
"""

DAY7_PLAN = TEACHER + """
<h2>Day 7: Review and return to the six-toed cats</h2>
<table border="1" cellpadding="6"><tr><th>Goal</th><td>Reteach from CFA results; students revise their Day 1 model and write the final explanation of the phenomenon.</td></tr>
<tr><th>Materials</th><td>The Review page (Canvas), students' Day 1 models and CFA scores.</td></tr></table>
<h3>Plan (45 minutes)</h3>
<ol>
<li><strong>Find your focus (5 min).</strong> Students look at their six CFA scores. Below 4 of 6 on a CFA means do the matching Review section. Pull a small group for reteaching if several students are below 4 on the same CFA.</li>
<li><strong>Review sections (20 min).</strong> Students do Vocabulary and the sections for any CFA below 4 (Review page). Teacher circulates; answers are on the Review key.</li>
<li><strong>Revise the model (8 min).</strong> Students redraw their Day 1 model with: DNA with a gene and a switch, a one-letter change, the copy-then-read path, the protein made in an extra place, and the extra toe.</li>
<li><strong>Write It: the cats (12 min).</strong> Students write a claim-evidence-reasoning explanation of how a one-letter DNA change in a six-toed cat can lead to an extra toe (use the data from Day 6).</li>
</ol>
<h3>Model answer for Write It</h3>
<p>Claim: A one-letter change in the DNA switch of the SHH gene caused the extra toe. Evidence: six-toed cats make the SHH protein in 2 zones of the developing paw compared with 1 zone in five-toed cats, and they have 20 or more toes compared with 18; the trait passes from six-toed parents to kittens (11 of 22 kittens from six-toed &times; five-toed pairs). Reasoning: DNA stores the instructions. The cell copies the gene's message, and the copy is read to build a protein. A switch next to the gene decides where the gene is used. The one-letter change turns the SHH gene on in an extra place, so cells at the front of the paw make the SHH protein, which changes what those cells do and builds an extra toe.</p>
<h3>Scoring (4 points)</h3>
<ul><li>4: correct claim, two or more accurate data points, complete reasoning (DNA, gene, protein, job).</li><li>3: correct claim and data, one piece of the reasoning thin.</li><li>2: partly correct claim, one data point, vague reasoning.</li><li>1: wrong claim or misconception (for example, the cat chose to grow an extra toe).</li></ul>
"""

DAY8_PLAN = TEACHER + """
<h2>Day 8: CSA</h2>
<ul>
<li>CSA: HS-LS1-1, DNA to Proteins. 30 points: 6 vocabulary matches, 8 multiple choice, 2 free response. Allow the full 45 minutes.</li>
<li>Provide the code table on the test (it is in the questions). Calculators are not needed.</li>
<li>The free-response items are scored with the 4-point rubrics in the Canvas question comments.</li>
<li>After the test (next class): return the CSA, review the two free-response exemplars, and ask students to compare them with their own answers. Revisit the six-toed cats: <em>What would you add to your Day 1 model now?</em></li>
</ul>
"""

MATERIALS_PAGE = TEACHER + """
<h2>Unit materials and prep</h2>
<table border="1" cellpadding="6">
<tr><th>Day</th><th>You need</th></tr>
<tr><td>1</td><td>Projected photo of a polydactyl cat paw; printed student page (or share the Canvas page)</td></tr>
<tr><td>2</td><td>Student page, colored pencils, scissors, tape or glue</td></tr>
<tr><td>3 (lab)</td><td>Per pair: 2 licorice strands, 24 candy bases in four colors (6 each, plus a few spare), toothpicks, paper plate, printed lab sheet and code table. Allergy-free or non-food alternatives: colored beads and pipe cleaners, or colored paper circles.</td></tr>
<tr><td>4</td><td>Student page (card sort), printed on card stock if you want reusable cards</td></tr>
<tr><td>5</td><td>Student page, two colors of pencil</td></tr>
<tr><td>6</td><td>Student page</td></tr>
<tr><td>7</td><td>Review page, Day 1 models, CFA scores</td></tr>
<tr><td>8</td><td>CSA (Canvas quiz, 45-minute limit)</td></tr></table>
<h3>Science background (for you)</h3>
<ul>
<li>In Hemingway cats and other polydactyl cats, extra toes are linked to a single-base substitution in the ZRS, a regulatory stretch of DNA that works like a switch for the SHH gene. The change turns SHH on in an extra place (the front edge of the developing paw), which leads to extra toes. The SHH protein itself is not changed. Source: Lettice et al., 2008, <em>Human Molecular Genetics</em>.</li>
<li>The trait is inherited as an autosomal dominant but does not always show (incomplete penetrance, varying expression). Class data and the sequences shown are simplified illustrations.</li>
<li>The Hemingway Home museum in Key West houses about 50 to 60 cats; sources say about half have extra toes. Sources disagree on the name of the founding cat.</li>
<li>Assessment boundary: no identification of specific cell or tissue types, whole body systems, specific protein structures and functions, or the biochemistry of protein synthesis. The cats are used as a context; the CSA does not require knowing anything about cats.</li>
</ul>
"""

# Order of items per day: (type, title, html, [points])
LESSONS = {
    "Day 1: Launch with the six-toed cats": [("page", "Day 1 Teacher Plan: Launch", DAY1_PLAN), ("page", "Day 1 Student Page: Why do some cats have extra toes?", DAY1_STUDENT)],
    "Day 2: What is DNA made of?": [("page", "Day 2 Teacher Plan: DNA structure", DAY2_PLAN), ("page", "Day 2 Student Page: What is DNA made of?", DAY2_STUDENT)],
    "Day 3: LAB, build, copy, and read a gene (gummy DNA)": [("page", "Day 3 Teacher Plan: Gummy DNA Lab", DAY3_PLAN), ("page", "Day 3 Teacher Key and Prep: Gummy DNA Lab", LAB_TEACHER), ("assignment", "Gummy DNA Lab Sheet", LAB_STUDENT, 12)],
    "Day 4: What can one letter do?": [("page", "Day 4 Teacher Plan: One-letter changes", DAY4_PLAN), ("page", "Day 4 Student Page: What can one letter do?", DAY4_STUDENT)],
    "Day 5: Same DNA, different jobs": [("page", "Day 5 Teacher Plan: Same DNA, different jobs", DAY5_PLAN), ("page", "Day 5 Student Page: Same DNA, different jobs", DAY5_STUDENT)],
    "Day 6: Case data": [("page", "Day 6 Teacher Plan: Case data", DAY6_PLAN), ("page", "Day 6 Student Page: Case data", DAY6_STUDENT)],
    "Day 7: Review and back to the cats": [("page", "Day 7 Teacher Plan: Review and Write It", DAY7_PLAN)],
    "Day 8: CSA": [("page", "Day 8 Teacher Plan: CSA", DAY8_PLAN)],
}
