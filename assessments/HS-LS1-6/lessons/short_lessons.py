"""Unit 1.3 restructure (Oct 19): two 30-minute lessons replace Lessons 5, 6, and 7.

Mon Oct 19 Lesson 4 · Tue Oct 20 Short Lesson A (LS1-6.4) · Wed Oct 21 Short Lesson B
(LS1-6.5, LS1-6.6) · Thu Oct 22 review + Pumpkin Mystery wrap-up · Fri Oct 23 CSA.

Each deck is a Drive copy of the Lesson 2 deck (same look, same object ids), rewritten
with deck_requests.deck(), plus a notebook set-up slide (slide 2), a learning-targets
slide (slide 3), and the CFA slide(s) at the end.

  python3 short_lessons.py deck A      # Slides batchUpdate requests for Short Lesson A
  python3 short_lessons.py html B      # student Canvas page for Short Lesson B
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
TOMATO = [["Height (cm)", "32", "11"], ["Sugar in leaves (mg/g)", "12", "25"],
          ["Protein in leaves (mg/g)", "40", "10"], ["Dry mass (g)", "7.5", "2.4"]]

LESSONS = {
    "A": dict(
        day=7, date="Tue Oct 20", title="Trace the Atoms", lesson="Short Lesson A", targets=["LS1-6.4"], cfas=["LS1-6.4"],
        deck="1Y7UTZP3ErFgW0IE67TNt1cxsOOAXuqLlS6TsBvYlxoI",
        focus="How does a carbon atom from the air end up in your hair?",
        ready="Have ready: your notebook, a pencil, and a Chromebook",
        can=["use a model to trace a carbon atom from the air into a protein",
             "explain how small molecules link into big ones and come apart when we eat",
             "show that atoms are rearranged, never changed"],
        plan=["Warm-up", "Mini-lesson: small pieces, big molecules", "Trace a carbon atom", "Check the path",
              "Exit sentence", "CFA LS1-6.4"],
        slides=[
            ("warmup", ["WARM-UP · 3 MIN · ON YOUR OWN", "Glucose or the soil?",
                        "Glucose is C₆H₁₂O₆. Valine (an amino acid) is C₅H₁₁NO₂. Which atoms in valine could come from glucose? "
                        "Which must come from somewhere else?"]),
            ("list", ["MINI-LESSON · 5 MIN", "Small pieces, big molecules",
                      "Monomers are small molecules that link into long chains called polymers.\n"
                      "Amino acids link in a specific order to make proteins. Glucose links to make starch and cellulose.\n"
                      "When you eat, digestion breaks proteins back into amino acids.\n"
                      "Your cells link those amino acids in a new order to build your own proteins.\n"
                      "The atoms are rearranged. They are never created, destroyed, or changed."]),
            ("list", ["TRACE A CARBON ATOM · 12 MIN · WITH A PARTNER", "From the air to your hair",
                      "1. In a ____ molecule in the air. A pumpkin leaf takes it in.\n"
                      "2. In a ____ molecule in the leaf. Built during ____ using ____ energy.\n"
                      "3. In an ____. Combined with ____ from the soil.\n"
                      "4. In a pumpkin seed ____. Linked in a specific ____.\n"
                      "5. In an amino acid in your blood. You ate the seed and ____ it.\n"
                      "6. In your hair protein. Your cells ____ them in a new order."]),
            ("key", ["CHECK THE PATH · 2 MIN",
                     "CO₂ → glucose → amino acid → seed protein → amino acid in your blood → your hair protein",
                     "It is the same carbon atom the whole way. Light supplied the energy. The soil supplied the nitrogen."]),
            ("warmup", ["EXIT SENTENCE · 2 MIN · ON YOUR OWN", "Finish the sentence in your notebook",
                        "A carbon atom in my hair was once in ____ in the air, then in ____ in a leaf, then ____."]),
        ],
        notebook=dict(
            left=[("h", "Warm-up"), ("lines", 2),
                  ("h", "Trace a carbon atom"),
                  ("table", ["Step", "Where is the carbon atom?", "What happens to it?"], STEPS, [0.45, 2.0, 2.0], 7, None)],
            right=[("h", "Small pieces, big molecules"), ("lines", 4),
                   ("h", "Exit sentence"),
                   ("text", "A carbon atom in my hair was once in ____ in the air, then ____"), ("lines", 2)]),
        sections=[
            ("Warm-up", "<p>Glucose is C₆H₁₂O₆. Valine (an amino acid) is C₅H₁₁NO₂. Which atoms in valine could come from glucose? "
             "Which must come from somewhere else?</p>"),
            ("Small pieces, big molecules", "<p>Small molecules (monomers) link into big ones (polymers): amino acids → proteins, "
             "glucose → starch and cellulose. When you eat, digestion breaks proteins back into amino acids, and your cells link them "
             "into your own proteins. The atoms are rearranged, never changed.</p>"),
            ("Trace a carbon atom", "<p>With a partner, fill in the 6-step table in your notebook: follow one carbon atom from CO₂ "
             "in the air to a protein in your hair.</p>"),
            ("Exit sentence", "<p>A carbon atom in my hair was once in ____ in the air, then in ____ in a leaf, then ____.</p>"),
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
                        "Claim: answer in one sentence. Evidence: use 2 numbers from the data. Reasoning: sugar has only C, H, and O. "
                        "What else does a plant need to build proteins, and why did the sugar build up?"]),
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
                      "Stuck? Start with the soil: does most of the pumpkin's mass really come from the soil?"]),
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
             "Write a claim, 2 numbers as evidence, and reasoning about the atoms in sugar and in proteins.</p>"),
            ("Revise my Day 1 model", "<p>Reread your Day 1 model. Fill in 2 rows: Then I thought… / Now I think… / "
             "Because (evidence)…</p>"),
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
    print(json.dumps(deck(key), ensure_ascii=False) if what == "deck" else student_html(key))
