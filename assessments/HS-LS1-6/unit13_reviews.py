"""Unit 1.3 (HS-LS1-6) Mastery Path assignments, laid out like Earth Science Unit 3.

- REVIEWS[target]: opens when a student scores below a B (under 67.5%) on that CFA.
- PRACTICE_REVIEW: opens when a student scores below 67.5% on the practice test.
- EXTENSION: opens when a student scores 67.5% or higher on the practice test.

Each is a 10-point complete/incomplete assignment (text entry or upload) that
only students sent to it by the Mastery Path can see.
"""

import unit13_bank as U

BOX = '<div style="background:#eef5fb;border-left:4px solid #2b6cb0;padding:10px 14px;margin:12px 0"><p><strong>Learning target {tid}:</strong> {ican}</p></div>'
TABLE = '<table border="1" cellpadding="6" style="border-collapse:collapse"><tbody>{}</tbody></table>'


def table(header, *rows):
    th = "<tr>" + "".join(f"<th>{h}</th>" for h in header) + "</tr>"
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return TABLE.format(th + trs)


def try_it(q, a):
    return f"<p><strong>Try it:</strong> {q}</p><details><summary>Check your answer</summary><p>{a}</p></details>"


def review(tid, sections, submit):
    _, _, _, ican = U.TARGET[tid]
    body = [BOX.format(tid=tid, ican=ican),
            "<p>Your CFA score was below a B, so this page walks you back through the target. "
            f"Read each section, try the checks, then answer the {len(submit)} questions at the bottom.</p>",
            "<p><strong>Use:</strong> your Unit 1.3 notes and Lesson 1: The Giant Pumpkin Mystery.</p>"]
    for n, (title, html) in enumerate(sections, 1):
        body.append(f"<h3>{n}. {title}</h3>{html}")
    body.append("<h3>Show what you know (submit these)</h3><ol>" + "".join(f"<li>{s}</li>" for s in submit) + "</ol>")
    return "\n".join(body)


GLUCOSE = "C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>"
PHOTO = "6 CO<sub>2</sub> + 6 H<sub>2</sub>O &rarr; C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + 6 O<sub>2</sub>"

REVIEWS = {
    "LS1-6.1": review("LS1-6.1", [
        ("What is sugar made of?",
         f"<p>A chemical formula tells you which atoms are in a molecule and how many of each. Glucose is {GLUCOSE}.</p>"
         + table(["Letter", "Element", "Atoms in glucose"], ["C", "Carbon", "6"], ["H", "Hydrogen", "12"], ["O", "Oxygen", "6"])
         + "<p><strong>Memory trick:</strong> sugar is just <em>CHO</em>.</p>"
         + try_it("How many atoms in total are in one glucose molecule?", "6 + 12 + 6 = 24 atoms.")),
        ("The big molecules are mostly the same three elements",
         "<p>The large carbon-based molecules a living thing builds are made mostly of carbon, hydrogen, and oxygen too, which is why sugar is such a good starting material. Remember the dry pumpkin from Lesson 1:</p>"
         + table(["Carbon", "Oxygen", "Hydrogen", "Nitrogen", "Everything else"], ["45%", "42%", "6%", "3%", "about 4%"])
         + try_it("Which three elements make up about 93% of the dry pumpkin?", "Carbon, oxygen, and hydrogen (45 + 42 + 6 = 93%), the same three elements that are in sugar.")),
        ("What sugar can't supply",
         "<p>Some molecules need small amounts of other elements. Amino acids (the building blocks of proteins) all contain <strong>nitrogen</strong>, and a few contain <strong>sulfur</strong>. DNA contains nitrogen and <strong>phosphorus</strong>. Sugar has none of these, so plants take them in from the soil, and animals get them from their food.</p>"
         + try_it("The amino acid cysteine is C<sub>3</sub>H<sub>7</sub>NO<sub>2</sub>S. Which of its elements can't come from sugar?", "Nitrogen (N) and sulfur (S).")),
    ], [
        "Name the three elements that make up sugar.",
        "Name one element in amino acids that sugar does not have. Where does a plant get it?",
        "The dry pumpkin is 45% carbon, 42% oxygen, 6% hydrogen, and 3% nitrogen. Explain how these numbers show that the pumpkin is built mostly from the same elements as sugar.",
    ]),

    "LS1-6.2": review("LS1-6.2", [
        ("Living things take in matter",
         "<p>To grow and repair themselves, living things need building materials, which means matter (atoms). Plants take in carbon dioxide from the air, water, and minerals from the soil. Animals take in matter by eating. Their bodies break food molecules down and rebuild the atoms into their own molecules.</p>"
         + try_it("A goat eats hay and grows new hair. Where did the atoms in the new hair come from?", "From molecules in the hay. The goat broke them down and rearranged the atoms into its own molecules.")),
        ("Atoms are rearranged, never created or destroyed",
         f"<p>In a chemical reaction the atoms trade partners, but every atom is still there. Count the atoms in photosynthesis: {PHOTO}</p>"
         + table(["Element", "Left side (reactants)", "Right side (products)"],
                 ["Carbon", "6 (in 6 CO<sub>2</sub>)", "6 (in glucose)"],
                 ["Hydrogen", "12 (in 6 H<sub>2</sub>O)", "12 (in glucose)"],
                 ["Oxygen", "12 + 6 = 18", "6 + 12 = 18"])
         + try_it("Why do the numbers match on both sides?", "Atoms are only rearranged into new molecules. None are made or lost.")),
        ("Building bigger molecules releases water",
         "<p>When a cell joins two small molecules, it often removes a water molecule:</p>"
         "<p>C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> &rarr; C<sub>12</sub>H<sub>22</sub>O<sub>11</sub> + H<sub>2</sub>O</p>"
         "<p>Left: 12 C, 24 H, 12 O. Right: 12 C, 22 + 2 = 24 H, 11 + 1 = 12 O. The \"missing\" atoms are in the water. Because no atoms are lost, the total mass stays the same.</p>"
         + try_it("A sealed jar of yeast and sugar water has a mass of 300.0 g. The yeast grow for 3 days. What is the mass now?", "Still 300.0 g. Nothing entered or left the jar, and the atoms were only rearranged.")),
    ], [
        "Describe where an animal gets the matter it uses to grow, and what happens to that matter inside its body.",
        f"Copy and fill in an atom-count table (carbon, hydrogen, oxygen; left side and right side) for {PHOTO}.",
        "Explain why the total mass doesn't change when a cell builds a large molecule from smaller ones.",
    ]),

    "LS1-6.3": review("LS1-6.3", [
        ("From simple molecules to complex ones",
         "<p>Cells use chemical reactions to rearrange the atoms of simple molecules, like sugar, into larger and more complex products. Atoms from sugar become the carbon \"backbone\" of many other molecules.</p>"
         + try_it("Is building a protein from amino acids making something simpler or more complex?", "More complex. Many small amino acids are joined into one large protein.")),
        ("Adding nitrogen",
         "<p>Compare glucose with the amino acid glycine:</p>"
         + table(["Molecule", "C", "H", "O", "N"], ["Glucose (sugar)", "6", "12", "6", "0"], ["Glycine (amino acid)", "2", "5", "2", "1"])
         + "<p>Sugar can supply the C, H, and O, but not the N. Plants take in nitrogen as nitrate from the soil. Animals get it from the proteins in their food.</p>"
         + try_it("Alanine is C<sub>3</sub>H<sub>7</sub>NO<sub>2</sub>. Which atom must come from somewhere other than sugar?", "The nitrogen (N).")),
        ("When an element is missing",
         "<p>If a plant is missing nitrogen, it can still make sugar (photosynthesis only needs CO<sub>2</sub>, water, and light). But it can't turn that sugar into amino acids and proteins, so it stays small and its sugar builds up. The same is true for sulfur (some amino acids) and phosphorus (DNA).</p>"
         + try_it("A plant grows in soil with no sulfur. Name something it can't make.", "The amino acids that contain sulfur, such as cysteine, and the proteins that need them.")),
    ], [
        "In your own words, explain how a plant builds an amino acid using sugar. Name the other element it needs.",
        "Glycine is C<sub>2</sub>H<sub>5</sub>NO<sub>2</sub>. Which atom in glycine can't come from glucose, and where would a plant get it?",
        "A farmer's corn makes plenty of sugar but stays small in nitrogen-poor soil. Explain why.",
    ]),

    "LS1-6.4": review("LS1-6.4", [
        ("Bead models",
         "<p>In a bead model, black = carbon, white = hydrogen, red = oxygen, and blue = nitrogen. Taking a model apart and rebuilding the same beads into a new molecule shows atoms being <strong>rearranged</strong>. If the new molecule needs a color the old one didn't have, you have to add beads from outside, just like a plant takes nitrogen from the soil.</p>"
         + try_it("You take apart a glucose model to build glycine (C<sub>2</sub>H<sub>5</sub>NO<sub>2</sub>). Which color must you add?", "Blue (nitrogen). Glucose has no nitrogen.")),
        ("Tracers",
         "<p>Scientists can give a plant CO<sub>2</sub> made with \"labeled\" carbon and track where it goes. The labeled carbon shows up in this order: CO<sub>2</sub> &rarr; sugar &rarr; amino acids &rarr; proteins. This shows the atoms in proteins came from sugar first.</p>"
         + try_it("Put these in the order the labeled carbon would reach them: protein, CO<sub>2</sub>, amino acids, sugar.", "CO<sub>2</sub> &rarr; sugar &rarr; amino acids &rarr; protein.")),
        ("Matter arrows vs. energy arrows",
         "<p>When you trace atoms, follow <strong>matter</strong>: CO<sub>2</sub>, water, sugar, nitrogen, amino acids, proteins. Light and heat are <strong>energy</strong>, not atoms. Food chain trace: CO<sub>2</sub> in air &rarr; sugar in grass &rarr; grass proteins and other molecules &rarr; eaten and broken down by a cow &rarr; rebuilt into cow muscle protein.</p>"
         + try_it("Does the arrow \"sunlight &rarr; leaf\" trace matter or energy?", "Energy. Sunlight has no atoms.")),
    ], [
        "Trace a carbon atom from the air into a cow's muscle protein. Include at least 4 steps.",
        "A glucose bead model has 6 black, 12 white, and 6 red beads. You use them to build 2 glycine models (each C<sub>2</sub>H<sub>5</sub>NO<sub>2</sub>). Which beads are left over, and which beads must you add?",
        "Explain why a tracer experiment is good evidence that atoms from sugar end up in proteins.",
    ]),

    "LS1-6.5": review("LS1-6.5", [
        ("Claim, Evidence, Reasoning",
         "<p>A scientific explanation has three parts:</p><ul>"
         "<li><strong>Claim:</strong> one sentence that answers the question.</li>"
         "<li><strong>Evidence:</strong> specific data, with numbers, that support the claim.</li>"
         "<li><strong>Reasoning:</strong> the science idea that explains <em>why</em> the evidence supports the claim.</li></ul>"
         "<p>Sentence frames: <em>I claim that ___. The data show ___ (numbers). This supports my claim because ___.</em></p>"
         + try_it("Which part answers the question \"why does the evidence matter?\"", "The reasoning.")),
        ("Strong evidence uses numbers",
         table(["Tomato group", "Sugar in leaves (mg/g)", "Protein in leaves (mg/g)"], ["Normal nitrogen", "12", "30"], ["Low nitrogen", "25", "8"])
         + "<p>Weak evidence: \"The low-nitrogen plants looked bad.\" Strong evidence: \"Protein dropped from 30 to 8 mg/g, but sugar went <em>up</em> from 12 to 25 mg/g.\"</p>"
         + try_it("What does the sugar data tell you about photosynthesis in the low-nitrogen plants?", "Photosynthesis still worked. They made plenty of sugar.")),
        ("Reasoning connects atoms to the evidence",
         "<p>For this standard, strong reasoning usually includes: (1) sugar contains only carbon, hydrogen, and oxygen; (2) cells rearrange atoms from sugar and combine them with other elements, such as nitrogen, to build amino acids and proteins; (3) atoms can't be created, so a missing element limits what can be built.</p>"
         + try_it("What is missing from this reasoning: \"The plant needs nitrogen to grow.\"?", "Why it needs nitrogen: sugar has no nitrogen, and amino acids and proteins need it, so the plant can't build them from sugar alone.")),
    ], [
        "Use this data on bean plants: <strong>with nitrogen</strong>: sugar 14 mg/g, protein 35 mg/g, dry mass 6.0 g. <strong>No nitrogen</strong>: sugar 27 mg/g, protein 9 mg/g, dry mass 2.1 g. Write a <strong>claim</strong>: why are the no-nitrogen plants smaller, even though they have more sugar?",
        "Give <strong>evidence</strong> for your claim, using at least two pairs of numbers from the data.",
        "Write your <strong>reasoning</strong>. Explain how carbon, hydrogen, and oxygen from sugar combine with nitrogen, and why the sugar built up in the no-nitrogen plants.",
    ]),

    "LS1-6.6": review("LS1-6.6", [
        ("Why scientists revise",
         "<p>Scientific explanations change when new evidence doesn't fit. To revise:</p><ol>"
         "<li>Read the new evidence. What does it show?</li>"
         "<li>Check each part of the explanation. Which parts does the evidence <em>support</em>? Which does it <em>contradict</em>?</li>"
         "<li>Keep what is supported. Rewrite what is contradicted, and cite the evidence.</li></ol>"
         + try_it("Should you throw out an entire explanation if one part is wrong?", "No. Keep the parts the evidence supports and revise only the part it contradicts.")),
        ("Example: where does a tree's mass come from?",
         "<p><strong>First explanation:</strong> \"A tree gets its mass from the soil.\"<br><strong>New evidence:</strong> A willow tree gained 74 kg in 5 years, but its soil lost only 0.06 kg.<br><strong>Revised:</strong> \"Most of a tree's mass comes from carbon dioxide and water, which it builds into sugar and then other molecules. The soil supplies only small amounts of elements like nitrogen.\"</p>"
         + try_it("Which part of the first explanation did the soil data contradict?", "That most of the mass comes from the soil. The soil lost almost nothing.")),
        ("Using peer feedback",
         "<p>Peer feedback is evidence too. If a classmate says, \"Your explanation says the cat stores fish protein unchanged, but cat protein has a different amino acid order,\" the fix is: the cat <em>breaks down</em> the fish protein into amino acids and <em>rebuilds</em> them in a new order.</p>"
         + try_it("What words show that a molecule was not stored unchanged?", "Broken down, rearranged, rebuilt.")),
    ], [
        "A student wrote: \"A fish's muscle protein comes straight from the algae protein it eats, unchanged.\" New evidence: (a) Labeled carbon from CO<sub>2</sub> went into algae sugar, then algae protein, then fish muscle protein. (b) Fish muscle protein has a very different amino acid order from any algae protein. Which part of the student's explanation is <strong>supported</strong>? Cite the evidence.",
        "Which part is <strong>not supported</strong>? Cite the evidence.",
        "Write a revised explanation that traces carbon from CO<sub>2</sub> into the fish's muscle protein. Include sugar and nitrogen.",
    ]),
}

REVIEW_TITLE = {tid: f"{U.UNIT} Review {tid}: {name} (Mastery Path)" for tid, name, _, _ in U.TARGETS}

PRACTICE_REVIEW_TITLE = f"{U.UNIT} Review: Back to the Building Blocks (Mastery Path)"
PRACTICE_REVIEW = "\n".join([
    "<p><strong>Why you got this:</strong> Your practice test score was below a B (under 2.7 out of 4, or 67.5%). "
    "This review goes back over each Unit 1.3 learning target, one at a time. Work through all 6 parts, then type your answers in the submission box (number them 1-6). "
    "You can use your notes and Lesson 1: The Giant Pumpkin Mystery.</p>",

    "<h3>Part 1 · LS1-6.1: Elements in sugar and large molecules</h3>"
    f"<p><strong>Key idea:</strong> Sugar ({GLUCOSE}) is made of <strong>carbon, hydrogen, and oxygen</strong>. The large carbon-based molecules in living things are mostly these same three elements. Amino acids also need <strong>nitrogen</strong> (and some need sulfur), which sugar doesn't have.</p>"
    "<p><strong>Task 1:</strong> Copy and fill in this table.</p>"
    + table(["Molecule", "Contains C, H, and O? (yes/no)", "Contains nitrogen? (yes/no)"], ["Glucose (sugar)", "", ""], ["Glycine (amino acid)", "", ""]),

    "<h3>Part 2 · LS1-6.2: Taking in and rearranging matter</h3>"
    "<p><strong>Key idea:</strong> Living things take in matter (plants: CO<sub>2</sub>, water, minerals; animals: food) and rearrange the atoms through chemical reactions. Atoms are never created or destroyed, so the number of each kind of atom is the same before and after.</p>"
    f"<p><strong>Task 2:</strong> For {PHOTO}, count the oxygen atoms on the left and on the right. Show your math.</p>",

    "<h3>Part 3 · LS1-6.3: Sugar atoms plus other elements</h3>"
    "<p><strong>Key idea:</strong> Cells build complex molecules by combining atoms from sugar with other elements. A plant without nitrogen can still make sugar, but it can't build amino acids and proteins.</p>"
    "<p><strong>Task 3:</strong> Finish this sentence: \"Sugar supplies the ______, ______, and ______ atoms for an amino acid, but the ______ has to come from ______.\"</p>",

    "<h3>Part 4 · LS1-6.4: Trace atoms with a model</h3>"
    "<p><strong>Key idea:</strong> Bead models and tracer experiments let you follow atoms. Follow matter, not energy: light and heat are not atoms.</p>"
    "<p><strong>Task 4:</strong> Put these steps in order (write the letters) to trace a carbon atom into a fish:<br>"
    "A. The fish breaks the algae molecules down.<br>B. Algae take in carbon dioxide from the water.<br>C. The atoms are rebuilt into the fish's own proteins.<br>"
    "D. The algae build the carbon into sugar.<br>E. The algae use sugar and nitrogen to make amino acids and proteins, and a fish eats the algae.</p>",

    "<h3>Part 5 · LS1-6.5: Explain with evidence</h3>"
    "<p><strong>Key idea:</strong> A strong explanation has a <strong>claim</strong>, <strong>evidence</strong> with numbers, and <strong>reasoning</strong> that uses the science idea.</p>"
    + table(["Lettuce", "Sugar (mg/g)", "Protein (mg/g)", "Head mass (g)"], ["With nitrogen", "15", "38", "310"], ["No nitrogen", "28", "7", "95"])
    + "<p><strong>Task 5:</strong> Write a claim, two pieces of evidence (with numbers), and your reasoning: why is the no-nitrogen lettuce smaller even though it has more sugar?</p>",

    "<h3>Part 6 · LS1-6.6: Revise an explanation</h3>"
    "<p><strong>Key idea:</strong> When new evidence doesn't fit, keep what's supported and rewrite what isn't.</p>"
    "<p><strong>Task 6:</strong> A student wrote, \"Fertilizer is plant food that gives plants energy.\" New evidence: fertilizer contains nitrogen and phosphorus but no sugar, and plants given fertilizer but kept in the dark died. Write a revised explanation.</p>",

    "<p><em>When you finish, tell your teacher. You'll get a short re-check before the CSA.</em></p>",
])

EXTENSION_TITLE = f"{U.UNIT} Extension: Algae for Fuel or Food? (Mastery Path)"
EXTENSION = "\n".join([
    "<p><strong>Why you got this:</strong> You scored an A or B on the practice test (2.7 out of 4, or 67.5%, and up). "
    "Now use what you know about how sugar's atoms become other molecules to judge a real engineering idea: growing <strong>algae</strong> for fuel or for food. "
    "Type your answers in the submission box (number them 1-4), or upload a document.</p>",

    "<h3>Background: algae farms</h3>"
    "<p>Tiny algae grow in tanks of water using sunlight and carbon dioxide. Companies grow them for two reasons. Algae <strong>oil</strong> can be made into biofuel to replace gasoline or diesel. Algae <strong>protein</strong> can be used as food for people or animal feed. Engineers noticed something strange: when algae run out of nitrogen, they stop growing fast but start packing their cells with oil.</p>"
    "<p>Sample data from a 10-day growth test (based on lab studies):</p>"
    + table(["Tank", "Nitrogen in water", "Algae dry mass (g per liter)", "Protein (% of dry mass)", "Oil (% of dry mass)"],
            ["A", "Plenty all 10 days", "2.0", "50%", "15%"],
            ["B", "Used up by day 3", "1.0", "15%", "45%"]),

    "<h3>1. Trace (LS1-6.4)</h3>"
    "<p>Trace a carbon atom from the carbon dioxide bubbled into the tank to (a) a molecule of algae oil and (b) a molecule of algae protein. Label which steps need nitrogen.</p>",

    "<h3>2. Calculate (LS1-6.1, LS1-6.3)</h3>"
    "<p>Calculate the grams of protein and the grams of oil per liter in each tank (dry mass × percent). Show your math. "
    "Then explain why Tank B could still make plenty of oil without nitrogen but couldn't make much protein. (Hint: algae oil is made almost entirely of carbon, hydrogen, and oxygen.)</p>",

    "<h3>3. Argue (LS1-6.5)</h3>"
    "<p>Write a claim-evidence-reasoning (CER) paragraph answering: <em>Why did the algae in Tank B grow only half as much as the algae in Tank A?</em> Use data from the table and explain how atoms from sugar combine with other elements.</p>",

    "<h3>4. Evaluate and revise (LS1-6.6, ETS1-3)</h3>"
    "<p>An engineer says, \"Starving algae of nitrogen is always the best plan, because it makes the most oil.\" Use your numbers from Part 2 to evaluate this claim. Which tank produced more oil per liter? "
    "Then revise the engineer's statement into a better recommendation. Consider whether the goal is fuel or food, the cost of nitrogen fertilizer, and the trade-offs.</p>",

    "<p><em>Scoring: complete and thoughtful answers to all 4 parts = complete.</em></p>",
])
