"""Build Slides batchUpdate requests for the Day 2, Day 9, and Day 10 decks.

Each deck is a Drive copy of the Lesson 2 Google Slides deck, so it keeps that
deck's look. Slides are duplicated from Lesson 2's layouts and their text is
rewritten; the unused Lesson 2 slides are deleted.

  python3 deck_requests.py day2 > day2.json
"""

import json
import sys

P = "h287605ecd2867468_0_"
TITLE, GOALS = P + "109", P + "117"
# Source layouts in the Lesson 2 deck: slide id -> (kicker, title, body, footer)
WARMUP = (P + "130", [P + "131", P + "132", P + "133", P + "134"])   # kicker, title, one paragraph, footer
LIST = (P + "184", [P + "185", P + "186", P + "187", P + "188"])     # kicker, title, numbered list, footer
KEY = (P + "149", [P + "150", P + "151", P + "152", P + "153"])      # kicker, big statement, second statement, footer
ORIGINALS = [P + n for n in ("217", "130", "138", "303", "149", "157", "171", "184", "192", "203")]


def text(oid, s):
    return [{"deleteText": {"objectId": oid, "textRange": {"type": "ALL"}}},
            {"insertText": {"objectId": oid, "insertionIndex": 0, "text": s}}]


def cell(table, row, s):
    loc = {"rowIndex": row, "columnIndex": 0}
    return [{"deleteText": {"objectId": table, "cellLocation": loc, "textRange": {"type": "ALL"}}},
            {"insertText": {"objectId": table, "cellLocation": loc, "insertionIndex": 0, "text": s}}]


def deck(prefix, kicker, title, focus, ready, can, plan, footer, slides):
    reqs = []
    reqs += text(P + "110", kicker) + text(P + "111", title)
    reqs += [{"deleteText": {"objectId": P + "112", "textRange": {"type": "FROM_START_INDEX", "startIndex": 15}}},
             {"insertText": {"objectId": P + "112", "insertionIndex": 15, "text": " " + focus}}]
    reqs += text(P + "113", ready)
    reqs += text(P + "121", "\n".join(can)) + text(P + "126", footer)
    assert len(plan) == 6
    for i, row in enumerate(plan, 1):
        reqs += cell(P + "125", i, row)
    order = [TITLE, GOALS]
    for n, (layout, parts) in enumerate(slides, 3):
        src, els = {"warmup": WARMUP, "list": LIST, "key": KEY}[layout]
        sid = f"{prefix}_s{n:02d}"
        ids = {src: sid, **{e: f"{sid}_e{i}" for i, e in enumerate(els)}}
        reqs.append({"duplicateObject": {"objectId": src, "objectIds": ids}})
        for i, s in enumerate(list(parts) + [footer]):
            reqs += text(f"{sid}_e{i}", s)
        order.append(sid)
    reqs += [{"deleteObject": {"objectId": o}} for o in ORIGINALS]
    # Duplicates land after their source; move each slide into place one at a time.
    reqs += [{"updateSlidesPosition": {"slideObjectIds": [sid], "insertionIndex": i}} for i, sid in enumerate(order)]
    return reqs


DECKS = {
    "day2": lambda: deck(
        "d2", "HS-LS1-6 · THE GIANT PUMPKIN MYSTERY · DAY 2", "Vocabulary and SketchNotes",
        "What words and big ideas will we need to solve the pumpkin mystery?",
        "Have ready: your notebook, a pencil, and colored pencils",
        ["define 10 unit words in my own words, with examples and non-examples",
         "summarize the unit's 5 big ideas as sketchnotes",
         "connect the big ideas to the giant pumpkin"],
        ["Do Now", "How a Frayer model works", "Frayer models: 10 words", "SketchNotes: 5 big ideas",
         "Sensemaking: the Pumpkin Path", "Exit ticket"],
        "Day 2 · Vocabulary and SketchNotes",
        [
            ("warmup", ["DO NOW · 3 MIN · ON YOUR OWN", "Which of these words do you already know?",
                        "In your notebook, rate each word from 1 (never heard it) to 4 (I could teach it): atom, element, molecule, "
                        "conservation of matter, photosynthesis, glucose, amino acid, protein, monomer, polymer."]),
            ("list", ["VOCABULARY · 5 MIN · WATCH, THEN SET UP", "How to build a Frayer model",
                      "Draw a box with 4 squares and an oval in the middle. Write the word in the oval.\n"
                      "Top left: the definition in your own words.\n"
                      "Top right: facts or characteristics.\n"
                      "Bottom left: examples. Draw at least one.\n"
                      "Bottom right: non-examples (things it is NOT)."]),
            ("key", ["EXAMPLE · ATOM",
                     "Atom: the smallest piece of an element that still acts like that element.",
                     "Facts: atoms are rearranged in reactions, never created or destroyed. Examples: a carbon atom, an oxygen atom. "
                     "Non-examples: a cell, sunlight, a CO₂ molecule (that's 3 atoms)."]),
            ("list", ["FRAYER MODELS · 17 MIN · IN YOUR NOTEBOOK", "Words 1–5: what living things are made of",
                      "Atom: the smallest piece of an element that still acts like that element\n"
                      "Element: a pure substance made of only one kind of atom (C, H, O, N, …)\n"
                      "Molecule: two or more atoms bonded together, like CO₂ or H₂O\n"
                      "Conservation of matter: atoms are rearranged, never created, destroyed, or changed into other elements\n"
                      "Photosynthesis: plants use light energy to build sugar from CO₂ and water, releasing O₂"]),
            ("list", ["FRAYER MODELS · IN YOUR NOTEBOOK", "Words 6–10: how a plant builds its body",
                      "Glucose: a sugar (C₆H₁₂O₆) that stores energy and supplies atoms for building\n"
                      "Amino acid: a building block of proteins; it has C, H, O, and N\n"
                      "Protein: a large molecule made of amino acids linked in a specific order\n"
                      "Monomer: a small molecule that can link with others like it\n"
                      "Polymer: a large molecule made of many linked monomers"]),
            ("list", ["SKETCHNOTES · 10 MIN · ½ TO 1 PAGE", "SketchNotes: pictures plus a few words",
                      "Title the page: Sugar to Structures.\n"
                      "For each big idea, write a short phrase and draw a simple icon.\n"
                      "Connect ideas with arrows. Use one color for matter and another for energy.\n"
                      "No full sentences. If you can draw it, draw it."]),
            ("list", ["SKETCHNOTES · BIG IDEAS 1–3", "The five big ideas, part 1",
                      "Living things are made mostly of C, H, and O, plus a little N, P, and S. (Dry pumpkin: 45% C, 42% O, 6% H, 3% N.)\n"
                      "Atoms are rearranged into new molecules. They are never created or destroyed.\n"
                      "Plants build sugar from CO₂ and water. Light is the energy, not the matter."]),
            ("list", ["SKETCHNOTES · BIG IDEAS 4–5", "The five big ideas, part 2",
                      "Atoms from sugar join with nitrogen from the soil to build amino acids, which link into proteins.\n"
                      "Animals eat, break molecules down, and rebuild the atoms into their own molecules."]),
            ("list", ["SENSEMAKING · 7 MIN · NEXT NOTEBOOK PAGE", "The Pumpkin Path",
                      "Draw the pumpkin plant with the air, water, soil, and sunlight around it.\n"
                      "Draw a solid arrow for each source of matter and a dashed arrow for energy.\n"
                      "Label where sugar is built and where nitrogen comes in.\n"
                      "Leave room: after each lesson, add one new idea or piece of evidence to this page."]),
            ("warmup", ["EXIT TICKET · 3 MIN · ON YOUR OWN", "Use 3 vocabulary words to answer:",
                        "Where do you think most of the pumpkin's matter comes from? Underline the 3 words you used."]),
        ]),
    "day9": lambda: deck(
        "d9", "HS-LS1-6 · THE GIANT PUMPKIN MYSTERY · DAY 9", "Practice Test and Review",
        "Can I explain how a pumpkin builds its body from sugar?",
        "Have ready: your Chromebook, your notebook, and a pencil",
        ["show what I know on a practice test that looks like the CSA",
         "find my weakest target and fix it at a review station",
         "answer the driving question with evidence"],
        ["Self-rating", "Practice test", "Choose your stations", "Review station, round 1", "Review station, round 2",
         "Driving question"],
        "Day 9 · Practice Test and Review",
        [
            ("list", ["DO NOW · 3 MIN · ON YOUR OWN", "Rate yourself 1–4 on each target",
                      "LS1-6.1 Elements in sugar and large molecules\n"
                      "LS1-6.2 Taking in and rearranging matter\n"
                      "LS1-6.3 Sugar atoms plus other elements\n"
                      "LS1-6.4 Trace atoms with a model\n"
                      "LS1-6.5 Explain with evidence\n"
                      "LS1-6.6 Revise an explanation"]),
            ("warmup", ["PRACTICE TEST · 25 MIN · ON YOUR OWN", "Take the Unit 1.3 Practice Test on Canvas",
                        "16 questions, just like the CSA. Questions 14 and 16 are written answers: use claim, evidence, and reasoning. "
                        "After your teacher grades it, a review (below a B) or an extension (A or B) opens for you."]),
            ("list", ["REVIEW STATIONS · 2 ROUNDS OF 6 MIN", "Start at the station for your lowest target",
                      "Station A · Atoms and elements (LS1-6.1, 6.2): recount the molecule cards and check the photosynthesis atom count.\n"
                      "Station B · Sugar plus nitrogen (LS1-6.3): build an amino acid from glucose beads and the soil cup.\n"
                      "Station C · Trace the atoms (LS1-6.4): put the carbon-path cards in order, from the air to your hair.\n"
                      "Station D · Evidence and revision (LS1-6.5, 6.6): score two sample answers with the rubric, then fix one.\n"
                      "Finished? Open any CFA review that opened for you on Canvas."]),
            ("key", ["DRIVING QUESTION · 2 MIN",
                     "How does a plant build its body, and what is it built from?",
                     "Answer it in 2–3 sentences in your notebook. Use at least 4 vocabulary words."]),
        ]),
    "day10": lambda: deck(
        "d10", "HS-LS1-6 · THE GIANT PUMPKIN MYSTERY · DAY 10", "Unit 1.3 CSA",
        "How do atoms from sugar become the structures of living things?",
        "Have ready: your Chromebook, a pencil, and scratch paper",
        ["show what I know about all six Unit 1.3 targets",
         "use claim, evidence, and reasoning in my written answers",
         "reflect on how my understanding grew since Day 1"],
        ["Settle in", "Before you start", "Unit 1.3 CSA (about 40 minutes)", "Check your answers", "Notebook reflection", "Review or extension work"],
        "Day 10 · Unit 1.3 CSA",
        [
            ("list", ["BEFORE YOU START", "Set up for success",
                      "Clear your desk except your Chromebook, a pencil, and scratch paper.\n"
                      "Read every question twice.\n"
                      "Questions 14 and 16 are written answers: use claim, evidence, and reasoning.\n"
                      "You may sketch bead models or atom counts on scratch paper."]),
            ("warmup", ["UNIT 1.3 CSA · ON CANVAS", "Open Unit 1.3 CSA: Sugar to Structures (HS-LS1-6)",
                        "16 questions · 22 points. Take your time and check your work before you submit."]),
            ("list", ["WHEN YOU FINISH", "Reflect, then keep learning",
                      "In your notebook, re-rate yourself 1–4 on all six targets. Which one improved most since Day 1?\n"
                      "Then work quietly on your review or extension assignment from the practice test."]),
        ]),
}

if __name__ == "__main__":
    print(json.dumps(DECKS[sys.argv[1]](), ensure_ascii=False))
