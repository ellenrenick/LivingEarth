"""Unit 1.3 restructure (Oct 19): two 30-minute lessons replace Lessons 5, 6, and 7.

Mon Oct 19 Day 4 vocab + SketchNotes · Tue Oct 20 Short Lesson A (LS1-6.4) · Wed Oct 21 Short Lesson B
(LS1-6.5, LS1-6.6) · Thu Oct 22 review + Pumpkin Mystery wrap-up · Fri Oct 23 CSA.

Each deck is a Drive copy of the Lesson 2 deck (same look, same object ids), rewritten
with deck_requests.deck(), plus a notebook set-up slide (slide 2), a learning-targets
slide (slide 3), and the CFA slide(s) at the end.

  python3 short_lessons.py deck A      # Slides batchUpdate requests for Short Lesson A
  python3 short_lessons.py html B      # student Canvas page for Short Lesson B
  python3 short_lessons.py live-a-slides x   # add the 2 notebook slides to the live Short Lesson A deck
"""

import copy
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import deck_requests as D  # noqa: E402
import notebook_slides as NB  # noqa: E402
import targets_slide as T  # noqa: E402
import unit13_bank as U  # noqa: E402
import unit13_lessons as L  # noqa: E402

LAYOUT = "h287605ecd2867468_0_216"
CFA_SLIDE = ("cfa_LS1_6_1", ["cfa_LS1_6_1_k", "cfa_LS1_6_1_t", "cfa_LS1_6_1_b", "SLIDES_API1306876476_0"])
STEPS = [["1", "In a ____ molecule in the air", "A pumpkin leaf takes it in."],
         ["2", "In a ____ molecule in the leaf", "Built during ____ using ____ energy"],
         ["3", "In an ____", "Combined with ____ from the soil"],
         ["4", "In a pumpkin seed ____", "Linked in a specific ____"],
         ["5", "In an amino acid in your blood", "You ate the seed and ____ it."],
         ["6", "In your hair protein", "Your cells ____ them in a new order."]]
# Word bank for the Short Lesson A blanks (the 6-step trace, then the valine line on the notebook page).
# Scrambled on purpose: never list the words in answer order.
WORD_BANK_A = ["digested", "light", "protein", "carbon dioxide (CO₂)", "link", "amino acid", "order", "glucose",
               "nitrogen", "photosynthesis"]
# Notebook right page, Short Lesson A: what goes under each heading (slides after the warm-up and the mini-lesson).
SUGAR_N_A = ("Glucose C₆H₁₂O₆ + N from the soil → valine C₅H₁₁NO₂\n"
             "From sugar: C, H, and O. From the soil: N (nitrogen).\n"
             "Write it in your notebook under “Sugar + nitrogen.”\n"
             "On the 2 lines, finish: A plant can't make amino acids from sugar alone because sugar has no ____. "
             "The plant gets it from the ____.")
SMALL_PIECES_A = ("Fill in one line each in your notebook under “Small pieces, big molecules”:\n"
                  "1. Small pieces called ____ (monomers) link to make big molecules called ____ (polymers).\n"
                  "2. The ____ of the amino acids makes each protein different.\n"
                  "3. Digestion breaks proteins back into ____.\n"
                  "4. Atoms are ____, never created, destroyed, or changed.\n"
                  "Word bank: rearranged · proteins · order · amino acids")
# Short Lesson B sentence frames. Word banks are scrambled (never in answer order).
CER_FRAME_B = ("Claim: The tomatoes without nitrogen were smaller because ____.\n"
               "Evidence: With no nitrogen, height was ___ cm (vs. ___ cm) and protein was ___ mg/g (vs. ___ mg/g).\n"
               "Reasoning: Sugar has only C, H, and O. To build ____ and proteins, a plant combines sugar's atoms with ____. "
               "With no nitrogen, the plant could not build ____, so it could not grow. The sugar it made was not used, so it ____.\n"
               "Word bank: proteins · built up · amino acids · they had no nitrogen to make proteins · nitrogen")
REVISE_FRAME_B = "Frame: Then I thought the mass came from ____. Now I think it comes from ____. Because ____."
REVISE_BANK_B = "Word bank: the tomato data · CO₂ from the air · the soil · the Leaf Atom Lab · water · the leaf chamber"
UNSURE_B = ("In your notebook, under “One thing I'm still not sure about,” write 1 question you still have.\n"
            "Start with: I'm still not sure how / why / whether ____.\n"
            "Example: I'm still not sure whether a plant could grow with no soil at all.")
TOMATO = [["Height (cm)", "32", "11"], ["Sugar in leaves (mg/g)", "12", "25"],
          ["Protein in leaves (mg/g)", "40", "10"], ["Dry mass (g)", "7.5", "2.4"]]

NOTE_SUGAR_N = ("<p><strong>In your notebook, under “Sugar + nitrogen”:</strong> write which of valine's atoms come from sugar "
                "and which from the soil. Then finish: <em>A plant can't make amino acids from sugar alone because sugar has no "
                "____. The plant gets it from the ____.</em></p>")
NOTE_SMALL = ("<p><strong>In your notebook, under “Small pieces, big molecules”:</strong> fill in these 4 lines.</p><ol>"
              "<li>Small pieces called ____ (monomers) link to make big molecules called ____ (polymers).</li>"
              "<li>The ____ of the amino acids makes each protein different.</li>"
              "<li>Digestion breaks proteins back into ____.</li>"
              "<li>Atoms are ____, never created, destroyed, or changed.</li></ol>"
              "<p style=\"border:1px solid #999;padding:6px\"><strong>Word bank:</strong> rearranged · proteins · order · amino acids</p>")

NOTE_CER_B = ("<p><strong>Use the frame:</strong></p><ul>"
              "<li>Claim: The tomatoes without nitrogen were smaller because ____.</li>"
              "<li>Evidence: With no nitrogen, height was ___ cm (vs. ___ cm) and protein was ___ mg/g (vs. ___ mg/g).</li>"
              "<li>Reasoning: Sugar has only C, H, and O. To build ____ and proteins, a plant combines sugar's atoms with ____. "
              "With no nitrogen, the plant could not build ____, so it could not grow. The sugar it made was not used, so it ____.</li></ul>"
              "<p style=\"border:1px solid #999;padding:6px\"><strong>Word bank:</strong> proteins · built up · amino acids · "
              "they had no nitrogen to make proteins · nitrogen</p>")
NOTE_REVISE_B = ("<p><strong>Frame:</strong> Then I thought the mass came from ____. Now I think it comes from ____. Because ____.</p>"
                 "<p style=\"border:1px solid #999;padding:6px\"><strong>Word bank:</strong> the tomato data · CO₂ from the air · "
                 "the soil · the Leaf Atom Lab · water · the leaf chamber</p>")
NOTE_UNSURE_B = ("<p>In your notebook, write 1 question you still have. Start with: <em>I'm still not sure how / why / whether "
                 "____.</em></p>")

LESSONS = {
    "A": dict(
        day=7, date="Tue Oct 20", title="Trace the Atoms", lesson="Short Lesson A", targets=["LS1-6.3", "LS1-6.4"], cfas=["LS1-6.3", "LS1-6.4"],
        deck="1Y7UTZP3ErFgW0IE67TNt1cxsOOAXuqLlS6TsBvYlxoI",
        focus="How do atoms from sugar and the soil end up in a protein in your hair?",
        ready="Have ready: your notebook, a pencil, and a Chromebook",
        can=["explain how a plant combines atoms from sugar with nitrogen from the soil to build amino acids",
             "use a model to trace a carbon atom from the air into a protein",
             "show that atoms are rearranged, never changed"],
        plan=["Warm-up", "Mini-lesson: sugar + nitrogen → amino acids", "Trace a carbon atom", "Check the path",
              "CFA LS1-6.3", "CFA LS1-6.4"],
        slides=[
            ("warmup", ["WARM-UP · 3 MIN · ON YOUR OWN", "Glucose or the soil?",
                        "Glucose is C₆H₁₂O₆. Valine (an amino acid) is C₅H₁₁NO₂. Which atoms in valine could come from glucose? "
                        "Which must come from somewhere else?"]),
            ("list", ["SUGAR + NITROGEN · 2 MIN · IN YOUR NOTEBOOK", "Check the warm-up: where do valine's atoms come from?",
                      SUGAR_N_A]),
            ("list", ["MINI-LESSON · 5 MIN", "Sugar + nitrogen → amino acids → proteins",
                      "Glucose has only C, H, and O. To build an amino acid, the plant combines atoms from sugar with nitrogen from the soil.\n"
                      "Every amino acid has the same backbone (2 C, 4 H, 2 O, 1 N) plus a side chain that makes it unique.\n"
                      "Amino acids (monomers) link in a specific order to make proteins (polymers).\n"
                      "When you eat, digestion breaks proteins back into amino acids. Your cells link them into your own proteins.\n"
                      "The atoms are rearranged. They are never created, destroyed, or changed."]),
            ("list", ["SMALL PIECES, BIG MOLECULES · 2 MIN · IN YOUR NOTEBOOK", "Small pieces, big molecules", SMALL_PIECES_A]),
            ("list", ["TRACE A CARBON ATOM · 8 MIN · WITH A PARTNER", "From the air to your hair",
                      "1. In a ____ molecule in the air. A pumpkin leaf takes it in.\n"
                      "2. In a ____ molecule in the leaf. Built during ____ using ____ energy.\n"
                      "3. In an ____. Combined with ____ from the soil.\n"
                      "4. In a pumpkin seed ____. Linked in a specific ____.\n"
                      "5. In an amino acid in your blood. You ate the seed and ____ it.\n"
                      "6. In your hair protein. Your cells ____ them in a new order."]),
            ("key", ["CHECK THE PATH · 1 MIN",
                     "CO₂ → glucose → amino acid → seed protein → amino acid in your blood → your hair protein",
                     "It is the same carbon atom the whole way. Light supplied the energy. The soil supplied the nitrogen."]),
        ],
        notebook=dict(
            # Same order as the slides: warm-up, sugar + nitrogen, small pieces (mini-lesson), then the trace.
            left=[("h", "Warm-up"), ("lines", 2),
                  ("h", "Sugar + nitrogen"),
                  ("text", "Glucose C₆H₁₂O₆ + N from the soil → valine C₅H₁₁NO₂. From sugar: ____  From soil: ____  (C, H, O or N?)"),
                  ("lines", 2),
                  ("h", "Small pieces, big molecules"), ("lines", 4)],
            right=[("h", "Trace a carbon atom"),
                   ("table", ["Step", "Where is the carbon atom?", "What happens to it?"], STEPS, [0.45, 2.0, 2.0], 7, None)]),
        sections=[
            ("Warm-up", "<p>Glucose is C₆H₁₂O₆. Valine (an amino acid) is C₅H₁₁NO₂. Which atoms in valine could come from glucose? "
             "Which must come from somewhere else?</p>" + NOTE_SUGAR_N),
            ("Sugar + nitrogen → amino acids → proteins", "<p>Glucose has only C, H, and O. To build an amino acid, a plant "
             "combines atoms from sugar with nitrogen from the soil. Amino acids (monomers) link in a specific order into proteins "
             "(polymers). When you eat, digestion breaks proteins back into amino acids, and your cells link them into your own "
             "proteins. The atoms are rearranged, never changed.</p>" + NOTE_SMALL),
            ("Trace a carbon atom", "<p>With a partner, fill in the 6-step table in your notebook: follow one carbon atom from CO₂ "
             "in the air to a protein in your hair.</p>"
             "<p style=\"border:1px solid #999;padding:6px\"><strong>Word bank:</strong> " + " · ".join(WORD_BANK_A) + "</p>"),
        ],
    ),
    "B": dict(
        day=8, date="Wed Oct 21", title="Evidence and Revision", lesson="Short Lesson B", targets=["LS1-6.5", "LS1-6.6"],
        cfas=["LS1-6.5", "LS1-6.6"], deck="1jlKZanJduvVKbdG4zJk80E2SaIftkEAnk4VSwyN3I_A",
        focus="What does the evidence say, and how has my thinking changed?",
        ready="Have ready: your notebook (with your Day 1 model), a pencil, and a Chromebook",
        can=["use data to explain why a plant with plenty of sugar still needs nitrogen",
             "write a CER with two numbers as evidence",
             "revise my Day 1 model using evidence"],
        plan=["Read the tomato data", "CER: why so small?", "How it's scored", "Revise my Day 1 model",
              "CFA LS1-6.5", "CFA LS1-6.6"],
        slides=[
            ("list", ["EVIDENCE · 2 MIN · WHOLE CLASS", "Tomatoes without nitrogen",
                      "Same light, water, CO₂, and temperature. One group got no nitrogen. After 4 weeks (all nutrients vs. no nitrogen):\n"
                      "Height: 32 cm vs. 11 cm\n"
                      "Sugar in leaves: 12 vs. 25 mg/g\n"
                      "Protein in leaves: 40 vs. 10 mg/g\n"
                      "Dry mass: 7.5 g vs. 2.4 g"]),
            ("warmup", ["CER · 10 MIN · ON YOUR OWN",
                        "Why were the tomatoes without nitrogen so much smaller, even though they had more sugar?",
                        CER_FRAME_B]),
            ("list", ["HOW IT'S SCORED", "The 4-point rubric",
                      "4: Correct claim, 2 accurate numbers compared, explains that sugar's atoms are combined with nitrogen to build "
                      "amino acids and proteins, and why sugar built up.\n"
                      "3: Correct claim and 2 numbers; leaves out one piece of the reasoning.\n"
                      "2: Partly correct claim; one number or numbers used wrongly; vague reasoning.\n"
                      "1: Incorrect claim or a misconception (“nitrogen is needed for photosynthesis”); little or no data."]),
            ("list", ["REVISE · 6 MIN · ON YOUR OWN", "Then I thought… Now I think…",
                      "Find your Day 1 model of where the pumpkin's mass comes from.\n"
                      "Make 3 columns: Then I thought… / Now I think… / Because (evidence)…\n"
                      "Fill in 2 rows. Use evidence from the leaf chamber, the Leaf Atom Lab, or the tomato data.\n"
                      "Stuck? Start with the soil: does most of the pumpkin's mass really come from the soil?\n"
                      + REVISE_FRAME_B + "\n" + REVISE_BANK_B]),
            ("list", ["STILL WONDERING · 1 MIN · ON YOUR OWN", "One thing I'm still not sure about", UNSURE_B]),
        ],
        notebook=dict(
            left=[("h", "Evidence: tomatoes without nitrogen"),
                  ("table", ["Measurement", "All nutrients", "No nitrogen"], TOMATO, [2.05, 1.2, 1.2], 9, None),
                  ("h", "CER: why so small?"),
                  ("table", ["Part", "My answer"], [["Claim", ""], ["Evidence (2 numbers)", ""], ["Reasoning", ""]],
                   [1.3, 3.15], 9, 0.42)],
            right=[("h", "Revise my Day 1 model"),
                   ("table", ["Then I thought…", "Now I think…", "Because (evidence)…"], [["", "", ""], ["", "", ""]],
                    [1.48, 1.48, 1.49], 9, 1.0),
                   ("h", "One thing I'm still not sure about"), ("lines", 2)]),
        sections=[
            ("Evidence: tomatoes without nitrogen", "<p>Students grew tomatoes with the same light, water, CO₂, and temperature. "
             "One group got no nitrogen. After 4 weeks:</p>"
             + L.table(["Measurement", "All nutrients", "No nitrogen"], *TOMATO)),
            ("CER: why so small?", "<p>Why were the tomatoes without nitrogen so much smaller, even though they had more sugar? "
             "Write a claim, 2 numbers as evidence, and reasoning about the atoms in sugar and in proteins.</p>" + NOTE_CER_B),
            ("Revise my Day 1 model", "<p>Reread your Day 1 model. Fill in 2 rows: Then I thought… / Now I think… / "
             "Because (evidence)…</p>" + NOTE_REVISE_B),
            ("One thing I'm still not sure about", NOTE_UNSURE_B),
        ],
    ),
}


def cfa_title(tid):
    return f"Unit 1.3 CFA {tid}: {U.TARGET[tid][1]}"


def cfa_slide_text(tid, minutes):
    return [f"CFA · {minutes} MIN · ON YOUR OWN, FROM MEMORY", f"Show what you know: CFA {tid}",
            f"Open Canvas: {cfa_title(tid)} (5 questions).\n"
            f"Target: {U.TARGET[tid][3]}\n"
            "Below a B (fewer than 4 of 5)? A review page for this target opens for you on Canvas."]


def word_bank_box(page):
    """A bordered word-bank box under the 6-step trace."""
    oid = f"{page}_wb"
    return [{"createShape": {"objectId": oid, "shapeType": "TEXT_BOX", "elementProperties": {
                "pageObjectId": page, "size": {"width": {"magnitude": 8162700, "unit": "EMU"},
                                                   "height": {"magnitude": 1100000, "unit": "EMU"}},
                "transform": {"scaleX": 1, "scaleY": 1, "translateX": 609600, "translateY": 3200000, "unit": "EMU"}}}},
            {"insertText": {"objectId": oid, "text": "Word bank: " + "  ·  ".join(WORD_BANK_A)}},
            {"updateTextStyle": {"objectId": oid, "style": {"fontSize": {"magnitude": 16, "unit": "PT"}}, "fields": "fontSize"}},
            {"updateTextStyle": {"objectId": oid, "textRange": {"type": "FIXED_RANGE", "startIndex": 0, "endIndex": 10},
                                 "style": {"bold": True}, "fields": "bold"}},
            {"updateShapeProperties": {"objectId": oid, "shapeProperties": {"outline": {
                "outlineFill": {"solidFill": {"color": {"rgbColor": {"red": 0.4, "green": 0.4, "blue": 0.4}}}},
                "weight": {"magnitude": 1.5, "unit": "PT"}}}, "fields": "outline"}}]


def deck(key):
    s = LESSONS[key]
    footer = f"{s['lesson']} · {s['title']}"
    reqs = D.deck(f"s{key.lower()}", f"HS-LS1-6 · THE GIANT PUMPKIN MYSTERY · {s['lesson'].upper()}", s["title"], s["focus"],
                  s["ready"], s["can"], s["plan"], footer, s["slides"])
    reqs.append({"deleteObject": {"objectId": "lt_d2_slide"}})
    # CFA slide(s), last. The first reuses the Lesson 2 CFA slide; any second one is a duplicate.
    src, els = CFA_SLIDE
    minutes = 6
    for n, tid in enumerate(s["cfas"]):
        sid = src if n == 0 else f"s{key.lower()}_cfa{n}"
        ids = {e: e if n == 0 else f"{sid}_e{i}" for i, e in enumerate(els)}
        if n:
            reqs.insert(0, {"duplicateObject": {"objectId": src, "objectIds": {src: sid, **ids}}})
        for e, t in zip(els, cfa_slide_text(tid, minutes) + [footer]):
            reqs += D.text(ids[e], t)
        reqs.append({"updateSlidesPosition": {"slideObjectIds": [sid], "insertionIndex": 2 + len(s["slides"]) + n}})

    if key == "A":
        trace = next(n for n, (_, parts) in enumerate(s["slides"], 3) if parts[0].startswith("TRACE"))
        reqs += word_bank_box(f"sa_s{trace:02d}")

    # Notebook set-up example, slide 2.
    NB.DECKS[key] = dict(id=s["deck"], scale=1.0, title=s["title"], focus=s["focus"], **s["notebook"])
    b = NB.Builder(key)
    b.layout = {"layoutId": LAYOUT}
    reqs += b.build()

    # Learning-targets slide, slide 3.
    fake = dict(day=100 + s["day"], targets=s["targets"], title=s["title"], lesson=s["lesson"],
                slides=("", L.SLIDES.format(s["deck"])))
    L.DAYS.append(fake)
    T.DECKS[fake["day"]] = (LAYOUT, 1)
    _, treqs = T.requests(fake["day"])
    L.DAYS.remove(fake)
    treqs = json.dumps(treqs, ensure_ascii=False).replace(f"lt_d{fake['day']}_", f"lt_s{key.lower()}_")
    reqs += json.loads(treqs.replace(f"Day {fake['day']} · ", f"{s['lesson']} · "))
    return reqs


def live_short_a_slides():
    """Add the two notebook slides to the live Short Lesson A deck (built before they existed) by duplicating
    its mini-lesson slide sa_s04: "Sugar + nitrogen" after the warm-up, "Small pieces, big molecules" after
    the mini-lesson. Slide order then: ..., warm-up, sugar + nitrogen, mini-lesson, small pieces, trace, ..."""
    footer = "Short Lesson A · Trace the Atoms"
    new = [(sid, parts) for sid, (_, parts) in zip(("sa_s03n", None, "sa_s04n"), LESSONS["A"]["slides"][1:4]) if sid]
    reqs = []
    for sid, parts in new:
        reqs.append({"duplicateObject": {"objectId": "sa_s04", "objectIds": {"sa_s04": sid, **{
            f"sa_s04_e{i}": f"{sid}_e{i}" for i in range(4)}}}})
        for i, t in enumerate(list(parts) + [footer]):
            reqs += D.text(f"{sid}_e{i}", t)
    # Title, notebook, targets, goals, warm-up (index 4), then:
    for i, sid in enumerate(["sa_s03n", "sa_s04", "sa_s04n"], 5):
        reqs.append({"updateSlidesPosition": {"slideObjectIds": [sid], "insertionIndex": i}})
    return reqs


def live_notebook_a():
    """Rebuild the content of the live Short Lesson A notebook slide (keeps the slide, its background, and anything
    added by hand): delete the old nb_a_02.. elements, then recreate them in the new order."""
    s = LESSONS["A"]
    NB.DECKS["A"] = dict(id=s["deck"], scale=1.0, title=s["title"], focus=s["focus"], **s["notebook"])
    reqs = NB.Builder("A").build()
    keep = [r for r in reqs if not ("createSlide" in r or r.get("createImage", {}).get("objectId") == "nb_a_01")]
    old = [f"nb_a_{n:02d}" for n in range(2, 13)]
    return [{"deleteObject": {"objectId": o}} for o in old] + keep


def live_short_b():
    """Live Short Lesson B deck (built before these changes): CER frame + word bank on sb_s04, revise frame + word bank
    on sb_s06, and a new "One thing I'm still not sure about" slide after it (a duplicate of sb_s06)."""
    reqs = D.text("sb_s04_e2", CER_FRAME_B)
    reqs += [{"updateTextStyle": {"objectId": "sb_s04_e2", "textRange": {"type": "ALL"},
                                  "style": {"fontSize": {"magnitude": 14, "unit": "PT"}}, "fields": "fontSize"}},
             # the warm-up body box is short; stretch it down to just above the footer
             {"updatePageElementTransform": {"objectId": "sb_s04_e2", "applyMode": "ABSOLUTE", "transform": {
                 "scaleX": 2.7209, "scaleY": 0.95, "translateX": 609600, "translateY": 1687785, "unit": "EMU"}}}]
    revise = LESSONS["B"]["slides"][3][1][2]
    reqs += D.text("sb_s06_e2", revise)
    reqs += [{"updateTextStyle": {"objectId": "sb_s06_e2", "textRange": {"type": "ALL"},
                                  "style": {"fontSize": {"magnitude": 14, "unit": "PT"}}, "fields": "fontSize"}},
             {"updatePageElementTransform": {"objectId": "sb_s06_e2", "applyMode": "ABSOLUTE", "transform": {
                 "scaleX": 2.7209, "scaleY": 1.0, "translateX": 609600, "translateY": 1352513, "unit": "EMU"}}}]
    sid = "sb_s06n"
    reqs.append({"duplicateObject": {"objectId": "sb_s06", "objectIds": {"sb_s06": sid, **{
        f"sb_s06_e{i}": f"{sid}_e{i}" for i in range(4)}}}})  # lands right after sb_s06
    for i, t in enumerate(LESSONS["B"]["slides"][4][1]):
        reqs += D.text(f"{sid}_e{i}", t)
    reqs += [{"updateTextStyle": {"objectId": f"{sid}_e2", "textRange": {"type": "ALL"},
                                  "style": {"fontSize": {"magnitude": 16, "unit": "PT"}}, "fields": "fontSize"}},
             {"updatePageElementTransform": {"objectId": f"{sid}_e2", "applyMode": "ABSOLUTE", "transform": {
                 "scaleX": 2.7209, "scaleY": 0.4636, "translateX": 609600, "translateY": 1352513, "unit": "EMU"}}}]
    return reqs


def day_dict(key):
    """A unit13_lessons-style day for student_html()."""
    s = LESSONS[key]
    d = dict(day=s["day"], title=s["title"], lesson=s["lesson"], targets=s["targets"], focus=s["focus"],
             slides=(f"{s['lesson']}: {s['title']}", L.SLIDES.format(s["deck"])),
             notebook=[f"Title: <strong>{s['lesson']}: {s['title']}</strong>. Add it to your table of contents.",
                       "Copy the layout on slide 2 and fill it in as you go.", L.CER_LOG],
             sections=copy.deepcopy(s["sections"]), cfa=None)
    for tid in s["cfas"]:
        d["sections"].append((f"Show what you know: CFA {tid}",
                              f"<p>Take <strong>{cfa_title(tid)}</strong> on Canvas (5 questions), on your own and from memory. "
                              "If you score below a B, a review page for this target will open for you.</p>"))
    return d


def student_html(key):
    return L.student_html(day_dict(key))


if __name__ == "__main__":
    what, key = sys.argv[1], sys.argv[2]
    if what == "live-b":
        print(json.dumps(live_short_b(), ensure_ascii=False))
    elif what == "live-a-notebook":
        print(json.dumps(live_notebook_a(), ensure_ascii=False))
    elif what == "live-a-slides":
        print(json.dumps(live_short_a_slides(), ensure_ascii=False))
    else:
        print(json.dumps(deck(key), ensure_ascii=False) if what == "deck" else student_html(key))
