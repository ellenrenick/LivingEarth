"""Unit 2.1 CSA ("HS-LS1-1 Assessment: DNA to Proteins (CSA)", sandbox) on the 26-27 learning targets.

- instructions list the 5 LS1-1 targets (student "I can" wording) and say which items are teacher-graded; 40 minutes;
- each item's title names its target, so the teacher can read results by target;
- on every multiple-choice item where the key was the single longest choice, two wrong choices are lengthened
  (same meaning, wrong for the same reason) so length gives nothing away.
No answer key, choice id, point value, or item order changes; every item is read back and checked.

  python3 csa21_new_lts.py 330720 13936912
"""

import copy
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "HS-LS1-6"))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "HS-LS1-6" / "lessons"))
import newquiz_upload as N  # noqa: E402
import new_lts as T  # noqa: E402

TITLES = {
    1: "Part 1: Vocabulary Matching · LS1-1.1, LS1-1.2",
    2: "MC 1 · LS1-1.1 (DOK 2)", 3: "MC 2 · LS1-1.2 (DOK 2)", 4: "MC 3 · LS1-1.3 (DOK 2)", 5: "MC 4 · LS1-1.2 (DOK 2)",
    6: "MC 5 · LS1-1.4 (DOK 3)", 7: "MC 6 · LS1-1.1 (DOK 2)", 8: "MC 7 · LS1-1.5 (DOK 3)", 9: "MC 8 · LS1-1.3 (DOK 3)",
    10: "Free response 1 · LS1-1.5, with LS1-1.2 and 1.3 (DOK 3)", 11: "Free response 2 · LS1-1.4 (DOK 3)",
}
BLUEPRINT = {  # target: question numbers as students see them
    "LS1-1.1": "1 (matching), 2, 7", "LS1-1.2": "1 (matching), 3, 5", "LS1-1.3": "4, 9",
    "LS1-1.4": "6, 11", "LS1-1.5": "8, 10",
}
CHOICES = {
    2: [("A single straight strand made of amino acids joined together",
         "A single straight strand made of amino acids joined together end to end, with no sugars, phosphates, or bases anywhere in the model"),
        ("Two strands twisted together, each made only of sugar molecules",
         "Two strands twisted together, each made only of sugar molecules, with no phosphates or bases attached anywhere along either strand")],
    4: [("All three amino acids change, because one base change affects the whole chain.",
         "All three amino acids change, because one base change affects the whole chain, so every amino acid in the protein is now different from before."),
        ("No protein is built, because every change in DNA stops protein building.",
         "No protein is built, because every change in DNA stops protein building, so the cell can no longer make this protein at all after the change.")],
    5: [("The amino acids are copied, and the copies are read to build DNA.",
         "The amino acids are copied, and the copies are read to build DNA, so the recipe book stands for the amino acids and the dish stands for the DNA."),
        ("The whole DNA molecule leaves the nucleus and is taken apart to make a protein.",
         "The whole DNA molecule leaves the nucleus and is taken apart to make a protein, so the recipe book itself is used up each time a dish is made.")],
    6: [("Type Y lost gene 1 and Type X lost gene 3, so they cannot make the other proteins.",
         "Type Y lost gene 1 and Type X lost gene 3, so they cannot make the other proteins, which is the only reason each type of cell makes its own different set of proteins."),
        ("Type X and Type Y must have different DNA, because they make different proteins.",
         "Type X and Type Y must have different DNA, because they make different proteins, and two cells can only ever make different proteins if their genes are different.")],
    7: [("Proteins determine the base sequence of DNA, and DNA carries out jobs for the cell.",
         "Proteins determine the base sequence of DNA, and DNA carries out jobs for the cell, so the instructions flow from the proteins into the DNA molecule."),
        ("DNA carries out most jobs in a cell, and proteins store the instructions for DNA.",
         "DNA carries out most jobs in a cell, and proteins store the instructions for DNA, so proteins act as the cell's instruction book and DNA does the work.")],
    8: [("The protein changed first, and that caused the DNA to change.",
         "The protein changed first, and that caused the DNA to change, so the base change in Group 2 came after the protein stopped working well."),
        ("The symptoms are caused by the protein, not by the DNA, because DNA has no effect on proteins.",
         "The symptoms are caused by the protein, not by the DNA, because DNA has no effect on proteins, so the base change in Group 2 has nothing to do with them.")],
    9: [("The claim is supported, because all three changes affect the protein.",
         "The claim is supported, because all three changes affect the protein, so every single-base change in a gene must always stop the protein from working."),
        ("The claim is supported, because change C stops the protein.",
         "The claim is supported, because change C stops the protein, and one example where the protein stops working is enough to show that the claim is true.")],
}


def plain(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip()


def key_of(e):
    return json.dumps({"slug": e["interaction_type_slug"], "scoring": e.get("scoring_data"),
                       "choice_ids": [c["id"] for c in (e.get("interaction_data") or {}).get("choices", [])]}, sort_keys=True)


def instructions(old):
    i = old.find("<p><strong>Living Earth")
    slides = old[:i] if i >= 0 else ""
    targets = "".join(f"<li><strong>{t}:</strong> {T.TARGETS[t][2]}</li>" for t in T.TARGETS)
    return (slides + "<p><strong>Living Earth (Biology) – HS-LS1-1</strong></p>"
            "<p>Construct an explanation based on evidence for how the structure of DNA determines the structure of proteins, "
            "which carry out the essential functions of life through systems of specialized cells.</p>"
            f"<p><strong>Learning targets on this test:</strong></p><ul>{targets}</ul>"
            "<p>Part 1: Vocabulary matching (Question 1) · Part 2: Multiple choice (Questions 2 to 9) · "
            "Part 3: Free response (Questions 10 and 11). Questions 10 and 11 are written responses your teacher will grade.</p>"
            "<p>A code table is included in every question that needs one. 40 minutes, 4 points.</p>")


def edit(e, pos):
    e = copy.deepcopy(e)
    e["title"] = TITLES[pos]
    for old, new in CHOICES.get(pos, []):
        hits = [c for c in e["interaction_data"]["choices"] if plain(c["item_body"]) == old]
        assert len(hits) == 1, (pos, old)
        hits[0]["item_body"] = f"<p>{new}</p>"
    if pos in CHOICES:
        right = e["scoring_data"]["value"]
        lens = {c["id"]: len(plain(c["item_body"])) for c in e["interaction_data"]["choices"]}
        assert sum(1 for i, n in lens.items() if i != right and n >= lens[right]) >= 2, (pos, lens)
    return e


def main(course, quiz_id):
    api = N.Canvas("https://kernhigh.instructure.com", course, "")
    q = api.nq("GET", f"/quizzes/{quiz_id}")
    api.nq("PATCH", f"/quizzes/{quiz_id}", {"quiz": {"instructions": instructions(q.get("instructions") or "")}})
    items = sorted(api.nq("GET", f"/quizzes/{quiz_id}/items"), key=lambda i: i["position"])
    before = {i["id"]: (key_of(i["entry"]), i["points_possible"]) for i in items}
    for it in items:
        pos = it["position"]
        try:
            e = edit(it["entry"], pos)
        except AssertionError:  # already lengthened on an earlier run
            e = copy.deepcopy(it["entry"])
            e["title"] = TITLES[pos]
        if e != it["entry"]:
            api.nq("PATCH", f"/quizzes/{quiz_id}/items/{it['id']}", {"item": {"entry": e}})
            print(f"Q{pos}: {TITLES[pos]}")
    longest = 0
    for it in sorted(api.nq("GET", f"/quizzes/{quiz_id}/items"), key=lambda i: i["position"]):
        k, pts = before[it["id"]]
        assert key_of(it["entry"]) == k and it["points_possible"] == pts, it["position"]
        e = it["entry"]
        if e["interaction_type_slug"] == "choice":
            lens = {c["id"]: len(plain(c["item_body"])) for c in e["interaction_data"]["choices"]}
            r = e["scoring_data"]["value"]
            longest += lens[r] == max(lens.values()) and list(lens.values()).count(lens[r]) == 1
    print(f"All {len(before)} keys and point values unchanged. Key is the single longest choice on {longest} of 8 MC items.")


if __name__ == "__main__":
    main(*sys.argv[1:3])
