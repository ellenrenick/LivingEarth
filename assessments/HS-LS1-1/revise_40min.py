"""Unit 2.1 (Siamese cat): 40-minute versions of Days 1, 2, 4, 5, 6, and 7 for low-level freshman classes.

Every day now fits 40 minutes, including the 6-minute CFA: fewer questions, sentence frames and word banks,
one worked example done together, no cutting. Each deck gets one simple notebook setup slide (slide 2).
Day 3 (gummy DNA lab) and Day 8 (CSA) are not touched.

  python3 revise_40min.py canvas 330720     # student assignments + teacher pages (keeps the slides embed)
  python3 revise_40min.py slides 1          # print the Google Slides batchUpdate requests for one day's deck
"""

import json
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "HS-LS1-6"))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "HS-LS1-6" / "lessons"))
import newquiz_upload as N  # noqa: E402

TEACHER = "<p style=\"background:#fff3cd;padding:6px\"><strong>TEACHER PAGE.</strong> Includes answers. Do not share with students.</p>"
SCORING = ("<h3>How this is scored (4 points)</h3><ul><li>4: complete and accurate</li><li>3: mostly complete, a few errors</li>"
           "<li>2: partly complete or several errors</li><li>1: started</li></ul>")
VERSION = "<p><em>40-minute version (revised Oct 2026 for freshman pacing).</em></p>"


def tbl(rows, head=True):
    out = []
    for i, r in enumerate(rows):
        tag = "th" if head and i == 0 else "td"
        out.append("<tr>" + "".join(f"<{tag}>{c}</{tag}>" for c in r) + "</tr>")
    return "<table border=\"1\" cellpadding=\"6\"><tbody>" + "".join(out) + "</tbody></table>"


def bank(words):
    return f"<p style=\"border:1px solid #999;padding:6px\"><strong>Word bank:</strong> {' &middot; '.join(words)}</p>"


TEMPS = tbl([["Body part of an adult Siamese cat", "Skin temperature (&deg;C)", "Fur color"],
             ["Back (trunk)", "36", "Cream"], ["Belly", "36", "Cream"], ["Upper leg", "34", "Cream"],
             ["Ear", "28", "Dark brown"], ["Nose and face mask", "30", "Dark brown"], ["Paw", "28", "Dark brown"],
             ["Tail tip", "27", "Dark brown"]]) + "<p><em>Simplified class data set. Real temperatures vary.</em></p>"
LITTERS = tbl([["Litter", "Mother", "Father", "Dark-pointed (Siamese pattern) kittens", "Solid-colored kittens"],
               ["1", "Siamese pattern", "Siamese pattern", "5", "0"], ["2", "Siamese pattern", "Siamese pattern", "4", "0"],
               ["3", "Solid", "Solid", "1", "4"], ["4", "Solid", "Solid", "2", "3"]]) + \
    "<p><em>Simplified class data set modeled on real litter patterns.</em></p>"
CODE_D4 = tbl([["DNA triplet", "Amino acid", "DNA triplet", "Amino acid"], ["GGA", "Gly", "AGA", "Arg"],
               ["GAG", "Glu", "GTG", "Val"], ["GAA", "Glu", "CTG", "Leu"], ["CCG", "Pro", "&nbsp;", "&nbsp;"]])
CELLS = tbl([["Cell type", "Genes in the cell", "Proteins made", "Job"], ["P", "1, 2, 3, 4", "1 and 2", "Carries signals"],
             ["Q", "1, 2, 3, 4", "3 and 4", "Squeezes to move the body"]])
WORKS = tbl([["Body part", "Skin temperature (&deg;C)", "Cooler than 33 &deg;C? Protein works? (yes or no)", "Fur color (dark or cream)"],
             ["Ear", "28", "<em>yes (we do this one together)</em>", "<em>dark</em>"], ["Nose", "30", "", ""], ["Paw", "28", "", ""],
             ["Tail tip", "27", "", ""], ["Upper leg", "34", "", ""], ["Back", "36", "", ""], ["Belly", "36", "", ""]])
CASE1 = tbl([["", "Solid cat", "Siamese cat"], ["Gene for the pigment-making protein", "Usual sequence", "One letter different"],
             ["Amino acid chain", "Usual chain", "One amino acid different"],
             ["Where the protein works", "At every body temperature", "Only in skin cooler than about 33 &deg;C"],
             ["Fur color", "Dark all over", "Dark ears, nose, paws, tail; cream body"],
             ["Temperature of ear / back", "28 / 36 &deg;C", "28 / 36 &deg;C"]])
CASE2 = tbl([["Person", "Gene", "Protein", "Symptoms"], ["1", "Normal", "Works", "None"],
             ["2", "One base changed", "One amino acid different; works poorly", "Yes"]])
KITTENS = tbl([["", "Kitten raised warm", "Kitten raised cool"], ["Ear skin temperature (&deg;C)", "34", "26"],
               ["Ear fur color", "Light tan", "Dark brown"], ["Back skin temperature (&deg;C)", "36", "35"],
               ["Back fur color", "Cream", "Cream"]])
B = "______"

# Simple notebook setup: four lines to copy. (title, target, key words, question)
NOTEBOOK = {
    1: ("Day 1: The Siamese cat mystery", "DNA holds the instructions for building proteins.", "DNA, gene, protein",
        "Why are a Siamese cat's ears, paws, and tail dark?"),
    2: ("Day 2: What is DNA made of?", "DNA is a double helix made of nucleotides.", "nucleotide, base, double helix",
        "What is DNA made of?"),
    4: ("Day 4: What can one letter do?", "Changing one DNA base can change a protein.", "base, amino acid, protein",
        "Does every change in DNA matter?"),
    5: ("Day 5: Same DNA, different jobs", "DNA, through proteins, gives cells different jobs.", "gene, protein, job",
        "Why are only some parts of a Siamese cat dark?"),
    6: ("Day 6: Case data", "Use data to explain how a DNA change affects the body.", "claim, evidence, reasoning",
        "How can one DNA letter change the body?"),
    7: ("Day 7: Review and back to the cat", "Explain the Siamese cat from DNA to fur.", "DNA, gene, protein, amino acid",
        "Why are a Siamese cat's points dark?"),
}


def notebook_lines(day):
    title, target, words, q = NOTEBOOK[day]
    return [f"{title}   (date)", f"Target: {target}", f"Key words: {words}", f"Question: {q}"]


def notebook_html(day):
    return ("<p style=\"border:2px solid #2e7d32;padding:6px\"><strong>Notebook setup (2 min).</strong> Copy these 4 lines:<br>"
            + "<br>".join(notebook_lines(day)) + "</p>")


STUDENT = {
    1: ("Day 1: Why are a Siamese cat's ears, paws, and tail dark?", f"""
<h3>Notice and wonder</h3>
<p>Look at the photos of an adult Siamese cat and a newborn Siamese kitten.</p>
<p>I notice: __________________________</p>
<p>I wonder: __________________________</p>
<h3>Data 1: Temperature and color</h3>
{TEMPS}
<ol>
<li>Circle: Dark fur is on the body parts that are <strong>(warmer / cooler)</strong>. Cream fur is on the parts that are <strong>(warmer / cooler)</strong>.</li>
<li>A kitten is born almost white. Finish the sentence: A kitten is born white because before birth its whole body was {B} (warm / cool).</li>
</ol>
<h3>Data 2: Litters of kittens</h3>
{LITTERS}
<ol start="3">
<li>Circle: Two Siamese-pattern parents had kittens that were <strong>(all / some / no)</strong> Siamese pattern.</li>
<li>Circle: Two solid parents <strong>(can / cannot)</strong> have a Siamese-pattern kitten. So a kitten gets genes from <strong>(one parent / both parents)</strong>.</li>
</ol>
<h3>Key ideas</h3>
<ul><li>DNA in every cell stores instructions.</li><li>A gene is a section of DNA with the instructions for one protein.</li>
<li>Proteins do jobs for the cell.</li><li>A kitten gets one set of chromosomes (long DNA molecules with many genes) from each parent.</li></ul>
{bank(["DNA", "gene", "protein"])}
<ol start="5">
<li>The molecule that stores the instructions in a cat's cells is {B}.</li>
<li>A section of DNA with the instructions for one protein is a {B}. It makes a {B}, which does a job for the cell.</li>
<li><strong>Initial model (quick sketch).</strong> Draw a cell from a Siamese cat's ear. Label: <em>DNA, gene, protein, dark fur</em>. Use arrows. We will fix it on Day 7.</li>
</ol>"""),
    2: ("Day 2: What is DNA made of?", f"""
<h3>Key ideas</h3>
<ul><li>DNA is a double helix, like a twisted ladder.</li>
<li>It is built from nucleotides. Each nucleotide has a sugar, a phosphate, and a base.</li>
<li>The sugars and phosphates make the sides (the backbone). The bases make the rungs.</li>
<li>There are four bases: A, T, C, G. A pairs with T. C pairs with G.</li><li>The order of the bases is the message.</li></ul>
<h3>Part A: One nucleotide (we draw it together)</h3>
<p>Draw a pentagon (sugar), a circle (phosphate), and a rectangle (base). Label each part.</p>
<h3>Part B: Write the partner strand</h3>
<p><strong>Rule:</strong> A &harr; T and C &harr; G. Example: A T G &rarr; T A C</p>
<p>1. A T G C C T &rarr; ______________</p>
<p>2. T T T G A C &rarr; ______________</p>
<h3>Part C: Fill in the blanks</h3>
{bank(["double helix", "sugar and phosphate", "bases", "T", "G", "order of the bases"])}
<ol>
<li>DNA's shape is a {B}.</li>
<li>The sides of the ladder are made of {B}. The rungs are pairs of {B}.</li>
<li>A pairs with {B}. C pairs with {B}.</li>
<li>One gene is different from another because of the {B}.</li>
<li>A short stretch of a gene in two cats (made-up letters that show the idea):<br>
Solid cat: &nbsp; A T G G G A C T G T T T<br>Siamese cat: A T G A G A C T G T T T<br>
Circle the letter that is different. How many letters are different? {B}</li>
</ol>"""),
    4: ("Day 4: What can one letter do?", f"""
<h3>Key ideas</h3>
<p>A one-letter change in DNA can do one of three things:</p>
<ol><li>Change an amino acid in the chain (the protein may work differently).</li>
<li>Change whether a protein is made (a change in the switch next to a gene).</li>
<li>Change nothing noticeable.</li></ol>
<p><strong>Not every change matters.</strong></p>
<h3>Code table</h3>
{CODE_D4}
<h3>Sort the cards (no cutting)</h3>
<p>Write 1, 2, or 3 for each card. Pick a reason from the reason bank. Card B is done for you.</p>
{bank(["The amino acid changes from ___ to ___.", "The amino acid stays the same.", "The protein is not made.", "No gene is involved."]).replace("Word bank", "Reason bank")}
{tbl([["Card", "What changed", "Category (1, 2, or 3)", "Reason"],
      ["A", "In a Siamese cat, one letter changes in the gene for a pigment-making protein: GGA becomes AGA.", "", ""],
      ["B", "A gene's triplet changes from GAG to GAA.", "<em>3</em>", "<em>The amino acid stays the same (Glu and Glu).</em>"],
      ["C", "A gene's triplet changes from CTG to CCG.", "", ""],
      ["D", "One letter changes in a stretch of DNA that has no gene and no switch.", "", ""],
      ["E", "One letter changes in the switch next to a gene, so the gene is never turned on.", "", ""],
      ["F", "In a human gene, GAG becomes GTG.", "", ""]])}
<ol>
<li>A student says, &ldquo;Every change in DNA changes how a cell works.&rdquo; Circle: <strong>(agree / disagree)</strong>. Card {B} shows this because {B}.</li>
<li>Siamese cat (card A): Gly changes to {B}. The protein now works only where the skin is <strong>(warm / cool)</strong>, so the fur is dark on the {B}.</li>
</ol>"""),
    5: ("Day 5: Same DNA, different jobs", f"""
<h3>Key ideas</h3>
<ul><li>Every cell has the same DNA, including all the genes.</li>
<li>Each kind of cell uses a different set of genes, makes different proteins, and so has a different job.</li></ul>
<h3>Part A: Two kinds of cells</h3>
{CELLS}
<ol><li>Circle: P and Q have <strong>(the same / different)</strong> DNA. They have different jobs because they use different {B} and make different {B}.</li></ol>
<h3>Part B: Where does the changed protein work?</h3>
<p>In a Siamese cat, the pigment-making protein has one amino acid changed. It works only in skin <strong>cooler than about 33 &deg;C</strong> (a simplified number).</p>
{WORKS}
{bank(["DNA", "gene", "protein", "cool", "dark", "pigment-making"])}
<ol start="2">
<li>Every cell has the pigment gene, but only {B} cells make the pigment protein.</li>
<li><strong>Explain.</strong> Every cell in a Siamese cat has the same {B}. Only pigment-making cells use the {B} for the pigment-making {B}. The changed protein works only where the skin is {B}, so the ears, nose, paws, and tail are {B}.</li>
</ol>"""),
    6: ("Day 6: Case data", f"""
<h3>Case 1: Siamese and solid cats</h3>
{CASE1}
{bank(["gene", "amino acid", "in cool skin", "ears, nose, paws, and tail"])}
<ol><li>One letter in the {B} changes &rarr; one {B} in the protein is different &rarr; the protein works only {B} &rarr; pigment is made only on the {B}.</li></ol>
<h3>Case 2: A human gene</h3>
{CASE2}
{bank(["gene", "amino acid", "protein", "symptoms"])}
<ol start="2">
<li>One base in the {B} changes &rarr; one {B} in the chain is different &rarr; the {B} works poorly &rarr; {B}.</li>
<li><strong>Compare.</strong> In both cases, one letter in the DNA changes, one {B} changes, and the protein works {B}.</li>
<li><strong>Write (use the frame).</strong><br>
Claim: The Siamese cat's dark points are caused by {B}.<br>
Evidence: The ear is ___ &deg;C and its fur is ____. The back is ___ &deg;C and its fur is ____.<br>
Reasoning: The changed letter in the gene changes one {B}. Because of this, the protein works only in {B} skin, so pigment is made only on the {B}.</li>
</ol>"""),
    7: ("Day 7: Review and back to the cat", f"""
<h3>Part 1: Review (15 min)</h3>
<p>Your goal on every CFA is at least a 3. If you scored below a 3, a review assignment opened for that target in your Mastery Path; do it first. List the reviews you did: ______________</p>
<h3>Vocabulary (everyone)</h3>
{bank(["DNA", "nucleotide", "gene", "base sequence", "amino acid", "protein"])}
<ol>
<li>The molecule that stores the instructions for building proteins is ____________.</li>
<li>One building block of DNA, with a sugar, a phosphate, and a base, is a ____________.</li>
<li>A section of DNA with the instructions for one protein is a ____________.</li>
<li>The order of A, T, C, and G along a strand of DNA is its ____________.</li>
<li>A chain of ____________ is folded to make a protein.</li>
<li>A ____________ does jobs for the cell, such as moving materials or building structures.</li>
</ol>
<h3>Part 2: Fix your Day 1 model (8 min)</h3>
<p>Redraw your model. Check off each part as you add it:</p>
<p>&#9744; DNA with the gene &nbsp; &#9744; the one-letter change &nbsp; &#9744; the amino acid chain with one amino acid different &nbsp; &#9744; the protein working only in cool skin &nbsp; &#9744; the dark points</p>
<p>Upload a photo or describe your drawing in words.</p>
<h3>Part 3: Write It (14 min)</h3>
<p>Two Siamese kittens are raised from birth, one in a warm room and one in a cool room. At 12 weeks the scientists record:</p>
{KITTENS}
<p><strong>Use the frame.</strong></p>
<p>Claim: The cool-room kitten's ears are darker because {B}.</p>
<p>Evidence: The cool-room kitten's ear is ___ &deg;C and ________. The warm-room kitten's ear is ___ &deg;C and ________.</p>
<p>Reasoning: Both kittens have the same changed {B}. One changed DNA letter changes one {B} in the pigment-making {B}. That protein works only in skin cooler than about 33 &deg;C, so {B}.</p>"""),
}


def header(rows):
    return tbl([[f"<strong>{k}</strong>", v] for k, v in rows], head=False).replace("<td><strong>", "<th>").replace("</strong></td>", "</th>")


def plan(steps):
    total = sum(m for _, m, _ in steps)
    assert total == 40, total
    return "<h3>Plan (40 minutes)</h3><ol>" + "".join(
        f"<li><strong>{name} ({m} min).</strong> {text}</li>" for name, m, text in steps) + "</ol>"


def key(items, title="Answer key for the student page"):
    return f"<h3>{title}</h3><ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def notes(items):
    return "<h3>Notes</h3><ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


NB = "Students copy the 4-line notebook setup slide (title and date, target, key words, question)."

TEACHER_PAGES = {
    1: "<h2>Day 1: Launch with the Siamese cat</h2>" + header([
        ("Targets", "LS1-1.2 (priority): DNA holds the instructions for building proteins. LS3-1 (supporting, light): genes come from both parents."),
        ("Goal", "Students notice and wonder about a Siamese cat's colors, find patterns in two data tables, and sketch a first model."),
        ("Materials", "A projected photo of an adult Siamese cat and of a white newborn Siamese kitten; the student page."),
        ("CFA", "LS1-1.2 (last 6 minutes)")]) + plan([
        ("Notebook setup and notice/wonder", 7, NB + " Then show the adult Siamese and the white newborn. Each student writes 1 notice and 1 wonder; take 3 or 4 aloud. Steer toward: <em>Why are only the ears, face, paws, and tail dark?</em>"),
        ("Temperature data", 7, "Read the table together. Students circle Question 1 and finish the Question 2 sentence. Debrief: dark fur goes with cool parts (27 to 30), cream with warm parts (34 to 36); a newborn was warm all over, so it is born white."),
        ("Litter data", 6, "Four litters only. Students circle Questions 3 and 4. Debrief: two solid parents can still have a Siamese kitten, so a kitten gets something from both parents."),
        ("Key ideas", 8, "Read the Key Ideas aloud. Board: <em>DNA &rarr; gene &rarr; protein &rarr; job</em>. Do Questions 5 and 6 together with the word bank. Big question: <em>How can a difference in DNA change which parts of a cat are dark?</em>"),
        ("Initial model", 6, "Quick sketch, Question 7, with the four labels given. Do not correct; it is revised on Day 7."),
        ("CFA LS1-1.2", 6, "")]) + key([
        "Cooler; warmer.", "Warm.", "All.", "Can; both parents.", "DNA.", "Gene; protein.",
        "Look for: DNA or a gene in the cell, a protein, and dark fur, joined by arrows. Do not correct yet."]) + notes([
        "Cut from the 45-minute version: the second notice and wonder, the open-ended pattern questions (now circle or finish-the-sentence), three of the seven litters (the Siamese &times; solid pairs), and the chromosome-count question.",
        "The Siamese pattern is recessive: a kitten needs a changed copy of the gene from both parents. Do not name recessive/dominant unless students ask."]),
    2: "<h2>Day 2: What is DNA made of?</h2>" + header([
        ("Target", "LS1-1.1 (priority): DNA is a double helix built from nucleotides, each with a sugar, a phosphate, and a base."),
        ("Goal", "Students describe DNA's structure and base pairing, and see that the message is the order of the bases. Prepares for the lab on Day 3."),
        ("Materials", "Student page; colored pencils."), ("CFA", "LS1-1.1 (6 minutes)")]) + plan([
        ("Notebook setup and warm-up", 4, NB + " Then: sketch what you think DNA looks like (1 minute)."),
        ("Mini-lesson and Part A", 8, "Draw it on the board while students draw Part A with you: nucleotide (pentagon sugar, circle phosphate, rectangle base), a strand, the four bases, the second strand, A&ndash;T and C&ndash;G, the twist. Key point: the order of the bases is the message."),
        ("Part B: partner strands", 8, "Do the example A T G &rarr; T A C together. Students write the partner strand for two sequences. Check with a partner."),
        ("Part C: fill in the blanks", 8, "Questions 1 to 4 with the word bank."),
        ("Connect to the cats", 6, "Question 5: the same short stretch of a gene in a solid and a Siamese cat, one letter different. Ask: Could one letter change which parts of a cat are dark? We find out on Days 3 and 4. The letters are an illustration."),
        ("CFA LS1-1.1", 6, "")]) + key([
        "Part A: sugar (pentagon), phosphate (circle), base (rectangle).",
        "Part B: (1) T A C G G A. (2) A A A C T G.",
        "Part C: 1. double helix. 2. sugar and phosphate; bases. 3. T; G. 4. order of the bases. 5. One letter (the 4th: G in the solid cat, A in the Siamese cat)."]) + notes([
        "Cut from the 45-minute version: the third partner strand, open-ended Part C questions (now fill-in-the-blank), and the scissors and tape. The 12-minute lecture and the separate drawing time are merged so students draw along."]),
    4: "<h2>Day 4: What can one letter do?</h2>" + header([
        ("Target", "LS1-1.4 (priority): changing one DNA base can change a protein and what it does."),
        ("Goal", "Students sort one-letter DNA changes by their effect, see that not every change matters, and connect an amino acid change to the Siamese cat."),
        ("Materials", "Student page (no cutting: the cards are a table)."), ("CFA", "LS1-1.4 (6 minutes)")]) + plan([
        ("Notebook setup and warm-up", 4, NB + " Recap from the lab: base order sets amino acid order."),
        ("Mini-lesson", 7, "The three things a one-letter change can do. Then model card B with the code table: GAG and GAA both make Glu, so category 3."),
        ("Card sort", 15, "Partners write 1, 2, or 3 and a reason from the reason bank for cards A, C, D, E, F. Circulate; check card E (category 2) and card D (category 3), the two that use no code table."),
        ("The Siamese cat", 8, "Reveal: card A is the real Siamese change. The pigment-making protein has one different amino acid; it stops working at warm body temperatures and works only in the cooler ears, nose, paws, and tail tip. Students finish Questions 1 and 2."),
        ("CFA LS1-1.4", 6, "")]) + key([
        "Card A (GGA &rarr; AGA, Gly &rarr; Arg): 1, the amino acid changes.",
        "Card B (GAG &rarr; GAA, Glu &rarr; Glu): 3, the amino acid stays the same (done for students).",
        "Card C (CTG &rarr; CCG, Leu &rarr; Pro): 1.",
        "Card D (no gene, no switch): 3, no gene is involved.",
        "Card E (switch, gene never turned on): 2, the protein is not made.",
        "Card F (GAG &rarr; GTG, Glu &rarr; Val, as in sickle cell): 1.",
        "Question 1: disagree; card B or D, because the amino acid stays the same or no gene is involved.",
        "Question 2: Arg; cool; ears, nose, paws, and tail (the cool parts)."], "Answer key") + notes([
        "Cut from the 45-minute version: cutting out the cards, sorting all six from scratch (card B is now the worked example), and the open-ended reasons (now a reason bank).",
        "Keep the protein story at the level of the standard: a different amino acid changes how the protein works."]),
    5: "<h2>Day 5: Same DNA, different jobs</h2>" + header([
        ("Target", "LS1-1.5 (priority): DNA, through proteins, gives different cells their different jobs."),
        ("Goal", "Students explain that all cells have the same genes but use different ones, and use the Siamese cat to explain why only some parts of the body are dark."),
        ("Materials", "Student page."), ("CFA", "LS1-1.5 (6 minutes)")]) + plan([
        ("Notebook setup and warm-up", 4, NB + " Ask: Your skin cells and nerve cells have the same DNA. Why are they so different?"),
        ("Mini-lesson", 7, "Every cell has all the genes, but each kind of cell uses a different set. The proteins a cell makes decide its job. In a cat, only pigment-making cells use the gene for the pigment-making protein."),
        ("Part A", 6, "Students read the cell P and Q table and finish Question 1."),
        ("Part B", 8, "Do the ear row together (28 is cooler than 33, so yes, dark). Students finish the table."),
        ("Explain it", 9, "Questions 2 and 3 with the word bank. Read two answers aloud."),
        ("CFA LS1-1.5", 6, "")]) + key([
        "Part A, Question 1: the same; genes; proteins.",
        "Part B table: ear, nose, paw, tail tip: yes, dark. Upper leg, back, belly: no, cream.",
        "Question 2: pigment-making.",
        "Question 3: DNA; gene; protein; cool; dark."], "Answer key") + notes([
        "Cut from the 45-minute version: the Part B table of skin, nerve, and pigment cells (its idea is now Question 2) and the open-ended questions (now a frame with a word bank).",
        "The 33-degree line is a simplified class number. The idea to keep: the changed protein works in cool skin and not in warm skin."]),
    6: "<h2>Day 6: Case data, from a DNA change to the body</h2>" + header([
        ("Target", "LS1-1.6 (priority): use case data, like sickle cell, to explain how a DNA change affects the body."),
        ("Goal", "Students trace a DNA change through a protein to the body in two cases and write a claim-evidence-reasoning explanation with a frame."),
        ("Materials", "Student page."), ("CFA", "LS1-1.6 (6 minutes)")]) + plan([
        ("Notebook setup and warm-up", 4, NB + " Say the cat chain together: one-letter DNA change &rarr; one different amino acid &rarr; protein works only in cool skin &rarr; dark points."),
        ("Case 1 together", 8, "Read the table aloud. Fill in the Question 1 chain together."),
        ("Case 2 with a partner", 8, "Partners fill in the Question 2 chain with the word bank."),
        ("Compare", 4, "Question 3, one sentence."),
        ("Write", 10, "Question 4: claim, evidence, reasoning with the frame. Share two samples."),
        ("CFA LS1-1.6", 6, "")]) + key([
        "Question 1: gene; amino acid; in cool skin; ears, nose, paws, and tail.",
        "Question 2: gene; amino acid; protein; symptoms.",
        "Question 3: amino acid; differently (or poorly).",
        "Question 4: Claim: a one-letter change in the gene for the pigment-making protein. Evidence: the ear is 28 &deg;C and dark; the back is 36 &deg;C and cream. Reasoning: amino acid; cool; cooler body parts (ears, nose, paws, and tail)."], "Answer key") + notes([
        "Cut from the 45-minute version: the separate alike/different questions, the &ldquo;why does a DNA change matter&rdquo; and litter-data questions, and the open CER (now a frame). Case 1 is done as a class."]),
    7: "<h2>Day 7: Review and return to the Siamese cat</h2>" + header([
        ("Goal", "Reteach from CFA results; students fix their Day 1 model and write the final explanation of the phenomenon with a frame."),
        ("Materials", "Students' Day 1 models and CFA scores; the Mastery Path review assignments.")]) + plan([
        ("Find your focus", 3, "Students look at their six CFA scores. A score below 2.67 opens that target's review through the Mastery Path."),
        ("Review and vocabulary", 15, "Students do the reviews that opened, then the Vocabulary. Pull a small group if several students are below a 3 on the same CFA."),
        ("Fix the model", 8, "Students redraw their Day 1 model using the checklist."),
        ("Write It", 14, "Students write the claim-evidence-reasoning explanation with the frame and submit.")]) + key([
        "DNA", "nucleotide", "gene", "base sequence", "amino acids", "protein"], "Vocabulary answers") + """
<h3>Write It model answer</h3>
<p>Claim: The cool-room kitten's ears are darker because they are cooler, and the changed protein works in cool skin. Evidence: the cool-room kitten's ear is 26 &deg;C and dark brown; the warm-room kitten's ear is 34 &deg;C and light tan. Reasoning: Both kittens have the same changed <strong>gene</strong>. One changed DNA letter changes one <strong>amino acid</strong> in the pigment-making <strong>protein</strong>. That protein works only in skin cooler than about 33 &deg;C, so <strong>pigment is made in the cool-room kitten's ears and not much in the warm-room kitten's ears</strong>.</p>
<h3>Scoring (4 points)</h3>
<ul><li>4: correct claim, two accurate data points, all frame blanks correct.</li><li>3: correct claim and data, one blank thin.</li>
<li>2: partly correct claim, one data point.</li><li>1: wrong claim or misconception (for example, the cat changes color on purpose).</li></ul>""" + notes([
        "Cut from the 45-minute version: 5 minutes of review time and 2 of focus time. The model revision is now a checklist and Write It is now a frame."]),
}

# ---------------------------------------------------------------------------
# Slides: one simple notebook setup slide (slide 2) plus text edits to match the 40-minute plan.
# ---------------------------------------------------------------------------

SLIDE_TEXT = {
    1: {"day1_s2_b": ["Look at the photos of an adult Siamese cat and a newborn Siamese kitten.", "Write 1 thing you notice.",
                      "Write 1 thing you wonder.", "Where is the cat dark? Where is it cream?"],
        "day1_s3_n": ["Circle: dark fur is on the (warmer / cooler) parts. (Question 1)"],
        "day1_s4_b": ["A kitten is born almost white. The dark parts show up in the first weeks.", "Before birth, a kitten is warm all over.",
                      "Finish the sentence (Question 2)."],
        "day1_s5_n": ["Circle your answers to Questions 3 and 4. Simplified class data."],
        "day1_s7_b": ["How can a difference in DNA change which parts of a cat are dark?",
                      "Quick sketch (Question 7): a cell from the cat's ear. Label DNA, gene, protein, dark fur. Use arrows.",
                      "We will fix it on Day 7."]},
    2: {"day2_s5_b": ["Part A: draw one nucleotide with me.", "Part B: write the partner strand for two sequences. A-T, C-G.",
                      "Part C: fill in the blanks with the word bank."],
        "day2_s6_b": ["Solid cat:   A T G G G A C T G T T T", "Siamese cat: A T G A G A C T G T T T",
                      "Illustration only (made-up letters). Circle the letter that is different (Question 5).",
                      "Could one letter change which parts of a cat are dark? We find out on Days 3 and 4."]},
    4: {"day4_s5_t": ["Card sort: no cutting (15 min)"],
        "day4_s5_b": ["Write 1, 2, or 3 for each card and pick a reason from the reason bank.",
                      "Card B is done for you: GAG and GAA both make Glu, so it is a 3.",
                      "A: Siamese cat, GGA becomes AGA     C: CTG becomes CCG",
                      "D: change in DNA with no gene or switch     E: change that turns a gene off for good     F: human gene, GAG becomes GTG"]},
    5: {"day5_s4_n": ["Same DNA? Why different jobs? (Question 1)"],
        "day5_s6_t": ["Part B: where does the protein work?"],
        "day5_s6_b": ["One amino acid is different. The protein works only in skin cooler than about 33 °C (a simplified number).",
                      "We do the ear together. Then fill in each body part: protein works? Fur dark or cream?"],
        "day5_s7_b": ["Use the word bank to finish the frame (Questions 2 and 3).",
                      "Same DNA → only pigment cells use the gene → the protein works only in cool skin → dark points.",
                      "Then: Exit ticket CFA LS1-1.5 (6 minutes)."]},
    6: {"day6_s5_b": ["In both cases: one letter in the DNA changes → one ____ changes → the protein works ____.",
                      "(Question 3, one sentence)"],
        "day6_s6_b": ["Claim: The dark points are caused by ____.", "Evidence: The ear is __ °C and __. The back is __ °C and __.",
                      "Reasoning: one letter → one amino acid → the protein works only in __ skin → pigment only on the __."]},
    7: {"day7_s2_t": ["Find your focus (3 min)"],
        "day7_s3_t": ["Review work time (15 min)"],
        "day7_s4_b": ["Check off each part as you add it:", "DNA with the gene, and the one-letter change",
                      "The amino acid chain with one amino acid different", "The protein working only in cool skin, and the dark points"],
        "day7_s6_b": ["Claim: The cool-room kitten's ears are darker because ____.",
                      "Evidence: The cool-room ear is __ °C and __. The warm-room ear is __ °C and __.",
                      "Reasoning: same changed gene → one amino acid different → the protein works only in skin cooler than 33 °C → ____.",
                      "Submit in Canvas."]},
}
DELETE_SLIDES = {5: ["day5_s5"]}  # Day 5 Part B (skin, nerve, pigment cells) is cut


def slide_requests(day):
    p = f"day{day}_nb"
    reqs = [{"createSlide": {"objectId": p, "insertionIndex": 1, "slideLayoutReference": {"layoutId": "p4"},
                             "placeholderIdMappings": [{"layoutPlaceholder": {"type": "TITLE", "index": 0}, "objectId": f"{p}_t"},
                                                       {"layoutPlaceholder": {"type": "BODY", "index": 0}, "objectId": f"{p}_b"}]}},
            {"insertText": {"objectId": f"{p}_t", "text": "Notebook setup (2 min)"}},
            {"insertText": {"objectId": f"{p}_b", "text": "\n".join(notebook_lines(day))}}]
    for oid, lines in SLIDE_TEXT.get(day, {}).items():
        reqs += [{"deleteText": {"objectId": oid, "textRange": {"type": "ALL"}}},
                 {"insertText": {"objectId": oid, "text": "\n".join(lines)}}]
    if day == 1:
        # Litter table: keep litters 1, 2, 4, 5 (drop the Siamese x solid litters 3 and 6, and litter 7), renumber 1 to 4.
        for row in (7, 6, 3):
            reqs.append({"deleteTableRow": {"tableObjectId": "day1_s5_g", "cellLocation": {"rowIndex": row, "columnIndex": 0}}})
        for row, n in ((3, "3"), (4, "4")):
            loc = {"rowIndex": row, "columnIndex": 0}
            reqs += [{"deleteText": {"objectId": "day1_s5_g", "cellLocation": loc, "textRange": {"type": "ALL"}}},
                     {"insertText": {"objectId": "day1_s5_g", "cellLocation": loc, "text": n}}]
    for sid in DELETE_SLIDES.get(day, []):
        reqs.append({"deleteObject": {"objectId": sid}})
    return reqs


DAYS = {1: 13935178, 2: 13935179, 4: 13935182, 5: 13935183, 6: 13935184, 7: 13935185}
TEACHER_SLUGS = {1: "day-1-teacher-plan-launch-7", 2: "day-2-teacher-plan-dna-structure-7",
                 4: "day-4-teacher-plan-one-letter-changes-7", 5: "day-5-teacher-plan-same-dna-different-jobs-7",
                 6: "day-6-teacher-plan-case-data-7", 7: "day-7-teacher-plan-review-and-write-it-7"}


def student_html(day, old):
    # Keep the slides embed at the top of the current description.
    i = old.find("<h2>Day ")
    slides = old[:i] if i >= 0 else ""
    title, body = STUDENT[day]
    return f"{slides}<h2>{title}</h2>\n{notebook_html(day)}\n{body}\n{SCORING}"


def canvas(course):
    api = N.Canvas("https://kernhigh.instructure.com", course, "")
    for day, aid in DAYS.items():
        a = api.v1("GET", f"/assignments/{aid}")
        api.v1("PUT", f"/assignments/{aid}", {"assignment": {"description": student_html(day, a["description"] or "")}})
        print(f"Student assignment Day {day}: {a['name']}")
        slug = urllib.parse.quote(TEACHER_SLUGS[day])
        api.v1("PUT", f"/pages/{slug}", {"wiki_page": {"body": TEACHER + VERSION + TEACHER_PAGES[day]}})
        print(f"Teacher page Day {day}: {TEACHER_SLUGS[day]}")


if __name__ == "__main__":
    if sys.argv[1] == "slides":
        print(json.dumps(slide_requests(int(sys.argv[2])), ensure_ascii=False))
    elif sys.argv[1] == "canvas":
        canvas(sys.argv[2])
    elif sys.argv[1] == "preview":
        S = Path(sys.argv[2])
        for d in DAYS:
            (S / f"new_day{d}_student.html").write_text(student_html(d, (S / f"day{d}_student.html").read_text()))
            (S / f"new_day{d}_teacher.html").write_text(TEACHER + VERSION + TEACHER_PAGES[d])
        print("preview written")
