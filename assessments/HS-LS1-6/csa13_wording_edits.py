"""Wording edits to the New Quiz "Unit 1.3 CSA: Sugar to Structures (HS-LS1-6)" (Oct 19 review).

Changes wording only: no answer key, choice id, point value, or item order changes. After patching, every item
is read back and its key (and choice ids) compared with the key before the edit.

  python3 csa13_wording_edits.py https://kernhigh.instructure.com 342850 13902597
"""

import copy
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "lessons"))
import newquiz_upload as N  # noqa: E402

SYMBOL_KEY = ("<p><strong>Symbol key:</strong> C = carbon, H = hydrogen, O = oxygen, N = nitrogen, S = sulfur, P = phosphorus; "
              "CO<sub>2</sub> = carbon dioxide, H<sub>2</sub>O = water, O<sub>2</sub> = oxygen gas.</p>")
TERMS_13 = "<p>mg/g means milligrams in each gram of leaf. Dry mass is the mass left when all the water is dried out.</p>"
TERMS_14 = "<p>mg/g means milligrams in each gram of leaf.</p>"  # Q14 has no dry-mass column

# (old text, new text) replacements in each item's stem, by position.
BODY = {
    4: [("<p>A tiny acorn grows into an oak tree with a mass of several thousand kilograms. When scientists measure the soil in "
         "the pot of a young oak over 5 years, the soil loses less than 1 kg.</p>",
         "<p>A young oak grows in a large pot for 5 years. The tree gains about 70 kg. The soil in the pot loses less than 1 kg.</p>")],
    8: [("<strong>best refutes</strong> this claim?", "<strong>best refutes</strong> (shows the claim is wrong) this claim?")],
    9: [("Lake 1 receives runoff containing", "Lake 1 receives runoff (water that drains off the farms) containing")],
    13: [("</tbody></table><p>Which explanation", "</tbody></table>" + TERMS_13 + "<p>Which explanation")],
    14: [("</tbody></table><p>The grower is confused", "</tbody></table>" + TERMS_14 + "<p>The grower is confused")],
    15: [("<p>Since then, the class has analyzed (1) a tracer experiment showing carbon from CO<sub>2</sub> ends up in plant "
          "proteins, (2) data showing plants without nitrogen make sugar but little protein, and (3) bead models showing atoms "
          "are rearranged but never created.</p>",
          "<p>Since then, the class has analyzed:</p><ol><li>a tracer experiment showing carbon from CO<sub>2</sub> ends up in "
          "plant proteins</li><li>data showing plants without nitrogen make sugar but little protein</li><li>bead models "
          "showing atoms are rearranged but never created</li></ol>")],
    16: [("In a bead-model activity, students broke apart models of corn molecules and rebuilt the same beads into different "
          "molecules. No beads were added or lost, except that blue (nitrogen) beads had to come from the corn's proteins.",
          "Students broke apart bead models of corn proteins and rebuilt the same beads into a chicken protein with a new "
          "order. No beads were added or lost."),
         ("<strong>Evaluate:</strong> Identify", "<strong>Evaluate:</strong> Say whether each part of the claim is right or "
          "wrong and why. Identify"),
         ("<strong>Connect:</strong> Explain how", "<strong>Connect:</strong> Use the bead model to explain where the "
          "chicken's atoms came from. Explain how")],
}

# (old choice text, new choice text) by position. Lengthened wrong choices keep their meaning and stay wrong for the
# same reason; Q2 only gets a clear subject.
CHOICES = {
    2: [("All of them contain carbon.", "Sugar and the large carbon-based molecules all contain carbon."),
        ("Most of the atoms in them are iron and calcium.",
         "Most of the atoms in sugar and the large carbon-based molecules are iron and calcium.")],
    4: [("Most came from the soil, because roots absorb nutrients and minerals that are built directly into wood, leaves, "
         "and proteins as the tree grows.",
         "Most came from the soil, because roots absorb nutrients and minerals that are built directly into wood, leaves, "
         "and proteins as the tree grows, so the tree's mass comes mainly from what its roots take out of the soil."),
        ("Most came from sunlight, which the leaves absorb and convert directly into the solid matter that makes up wood, "
         "leaves, and proteins.",
         "Most came from sunlight, which the leaves absorb and convert directly into the solid matter that makes up wood, "
         "leaves, and proteins, so the more light energy the tree takes in, the more of its mass is made of that light.")],
    7: [("Without nitrogen the plants cannot carry out photosynthesis, so they have no sugar to use for growth.",
         "Without nitrogen the plants cannot carry out photosynthesis, so they have no sugar to use for growth, and with "
         "no sugar they cannot build any new stems, leaves, or other tissue."),
        ("Nitrogen in the soil is the main source of the carbon atoms that plants use to build the stems, leaves, and "
         "proteins of new tissue.",
         "Nitrogen in the soil is the main source of the carbon atoms that plants use to build the stems, leaves, and "
         "proteins of new tissue, so with little nitrogen the plants run short of carbon.")],
    8: [("Glucose has more carbon atoms than either amino acid.",
         "Glucose has more carbon atoms than either amino acid: 6 carbon atoms, compared with 2 in glycine and 3 in cysteine."),
        ("All three molecules contain carbon, hydrogen, and oxygen.",
         "All three molecules contain carbon, hydrogen, and oxygen, the same three elements that make up the glucose molecule.")],
    9: [("Algae in Lake 2 cannot carry out photosynthesis without phosphorus, so they make no sugar at all.",
         "Algae in Lake 2 cannot carry out photosynthesis without phosphorus, so they make no sugar at all, and with no "
         "sugar they have nothing to build new cells from, so their population cannot grow."),
        ("Phosphorus and nitrogen give the Lake 1 algae extra carbon atoms to build sugar.",
         "Phosphorus and nitrogen give the Lake 1 algae extra carbon atoms to build sugar, so the Lake 1 algae can make "
         "more sugar than the Lake 2 algae do and can grow much faster as a result.")],
    13: [("Group B made more sugar, so it should have grown more; the results must be caused by an error in measuring mass.",
          "Group B made more sugar, so it should have grown more; the results must be caused by an error in measuring mass, "
          "because a plant with more sugar in its leaves should always gain more dry mass."),
         ("Group A grew more because nitrate is a sugar that gave the plants extra energy for photosynthesis.",
          "Group A grew more because nitrate is a sugar that gave the plants extra energy for photosynthesis, so Group A "
          "had more energy to build new tissue and gain dry mass than Group B did.")],
    15: [("Plants use light energy to make sugar from CO2 and water, and sugar is then stored unchanged as the only building "
          "material in every plant cell.",
          "Plants use light energy to make sugar from CO2 and water, and sugar is then stored unchanged as the only building "
          "material in every plant cell, so no other elements are needed to make any of the plant's other molecules."),
         ("Plants change sunlight into new carbon atoms, and then combine those new carbon atoms with nitrogen from the soil "
          "to make amino acids and proteins.",
          "Plants change sunlight into new carbon atoms, and then combine those new carbon atoms with nitrogen from the soil "
          "to make amino acids and proteins, so the carbon in a plant comes from the light and not from the air.")],
}
BALANCE = (4, 7, 8, 9, 13, 15)


def plain(s):
    return re.sub(r"<[^>]+>", "", s or "")


def key_of(e):
    return json.dumps({"slug": e["interaction_type_slug"], "scoring": e.get("scoring_data"),
                       "choice_ids": [c["id"] for c in (e.get("interaction_data") or {}).get("choices", [])]}, sort_keys=True)


def edit(entry, pos):
    e = copy.deepcopy(entry)
    for old, new in BODY.get(pos, []):
        assert e["item_body"].count(old) == 1, (pos, old[:50])
        e["item_body"] = e["item_body"].replace(old, new)
    for old, new in CHOICES.get(pos, []):
        hits = [c for c in e["interaction_data"]["choices"] if plain(c["item_body"]) == old]
        assert len(hits) == 1, (pos, old[:50])
        hits[0]["item_body"] = f"<p>{new}</p>"
    if pos in BALANCE:
        right = e["scoring_data"]["value"]
        lens = {c["id"]: len(plain(c["item_body"])) for c in e["interaction_data"]["choices"]}
        longer = [i for i, n in lens.items() if i != right and n >= lens[right]]
        assert len(longer) >= 2, (pos, lens, right)
    return e


def main(base, course, quiz_id):
    api = N.Canvas(base, course, "")
    quiz = api.nq("GET", f"/quizzes/{quiz_id}")
    if "Symbol key" not in (quiz.get("instructions") or ""):
        api.nq("PATCH", f"/quizzes/{quiz_id}", {"quiz": {"instructions": (quiz.get("instructions") or "") + SYMBOL_KEY}})
        print("Instructions: added the symbol key")
    items = sorted(api.nq("GET", f"/quizzes/{quiz_id}/items"), key=lambda i: i["position"])
    before = {i["id"]: (key_of(i["entry"]), i["points_possible"]) for i in items}
    edited = []
    for it in items:
        pos = it["position"]
        if pos not in BODY and pos not in CHOICES:
            continue
        if "Symbol key" in it["entry"]["item_body"]:
            continue
        try:
            e = edit(it["entry"], pos)
        except AssertionError as err:
            print(f"Q{pos}: skipped (already edited or text not found: {err})")
            continue
        api.nq("PATCH", f"/quizzes/{quiz_id}/items/{it['id']}", {"item": {"entry": e}})
        edited.append(pos)
        print(f"Q{pos}: edited")
    after = sorted(api.nq("GET", f"/quizzes/{quiz_id}/items"), key=lambda i: i["position"])
    for it in after:
        k, pts = before[it["id"]]
        same = key_of(it["entry"]) == k and it["points_possible"] == pts
        print(f"Q{it['position']}: key and points unchanged = {same}")
        assert same
    print("Edited:", edited)


if __name__ == "__main__":
    main(*sys.argv[1:4])
