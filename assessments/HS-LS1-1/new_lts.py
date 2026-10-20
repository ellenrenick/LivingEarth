"""Unit 2.1 (sandbox): move to the 26-27 learning targets in "Renick Living Earth Standards and Learning Targets (26-27)".

LS1-1 goes from 6 targets to 5:
  new LS1-1.1 = old 1.1 (DNA structure) + old 1.2 (DNA holds the instructions)
  new LS1-1.2 = old 1.3 (copy, then read)      new LS1-1.3 = old 1.4 (one base change)
  new LS1-1.4 = old 1.5 (same DNA, different jobs)   new LS1-1.5 = old 1.6 (case data)
LS3-1.1-1.3 (supporting, not on the CSA) are taught on Day 1.

What this does (safe to run again):
- updates the course outcomes LS1-1.1 to 1.5 to the workbook text; LS1-1.6 is retitled as retired;
- merges CFA LS1-1.2's questions into CFA LS1-1.1 (Day 2), renames old CFA LS1-1.2 "OLD ..." and takes it,
  its review, and its Mastery Path rule out of use; renames CFAs and reviews 1.3-1.6 to 1.2-1.5;
- rewrites the unit overview page and renumbers the Day 3 lab pages.
Student assignments and teacher plans for Days 1, 2, 4-7 come from revise_40min.py (run it after this).

  python3 new_lts.py 330720
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "HS-LS1-6"))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "HS-LS1-6" / "lessons"))
import newquiz_upload as N  # noqa: E402
from canvas_lessons_upload import get_all  # noqa: E402

MODULE = 1644096
TARGETS = {  # id: (workbook learning target, DOK, student "I can")
    "LS1-1.1": ("Students can describe DNA as a double helix made of nucleotides containing sugar, phosphate, and nitrogen bases, "
                "and state that DNA contains the genetic instructions for building proteins.", 1,
                "I can describe DNA as a double helix built from nucleotides, each with a sugar, a phosphate, and a base, and state "
                "that DNA holds the instructions for building proteins."),
    "LS1-1.2": ("Students can describe the role of mRNA and tRNA in the transcription and translation processes.", 2,
                "I can describe how a gene's message is copied and read to build a chain of amino acids."),
    "LS1-1.3": ("Students can explain that a single base change can alter a protein and possibly change its function.", 2,
                "I can explain how changing one DNA base can change a protein and what it does."),
    "LS1-1.4": ("Students connect the idea that DNA codes for proteins and that these proteins contribute to the specialized "
                "functions of different cells.", 3, "I can explain how DNA, through proteins, gives different cells their different jobs."),
    "LS1-1.5": ("Students use data from case studies or simulations to analyze the impacts of protein defects (e.g., sickle cell "
                "anemia or cystic fibrosis).", 3, "I can use case data, like sickle cell, to explain how a DNA change affects the body."),
}
OUTCOME_IDS = {"LS1-1.1": 35599, "LS1-1.2": 35600, "LS1-1.3": 35601, "LS1-1.4": 35602, "LS1-1.5": 35603}
RETIRED_OUTCOME = 35604  # old LS1-1.6
# CFA quiz ids and review assignment ids, keyed by NEW target.
CFA = {"LS1-1.1": 13936905, "LS1-1.2": 13936908, "LS1-1.3": 13936909, "LS1-1.4": 13936910, "LS1-1.5": 13936911}
REVIEW = {"LS1-1.1": 13935171, "LS1-1.2": 13935173, "LS1-1.3": 13935174, "LS1-1.4": 13935175, "LS1-1.5": 13935176}
OLD_CFA_12, OLD_REVIEW_12 = 13936907, 13935172
OLD = "OLD (merged into LS1-1.1): "

OVERVIEW_SLUG = "unit-2-dot-1-dna-to-proteins-8-day-version-siamese-cats-overview-and-day-by-day-plan-7"
DAY3 = ("day-3-teacher-plan-gummy-dna-lab-7", "day-3-teacher-key-and-prep-gummy-dna-lab-7")

OVERVIEW = """<h2>Unit 2.1: DNA to Proteins (8-day version: Siamese Cats)</h2>
<p><em>Learning targets updated Oct 2026 to the department workbook (26-27). 40-minute class periods.</em></p>
<h3>Anchoring phenomenon</h3><p>Why are a Siamese cat's ears, face, paws, and tail dark while the rest of its body is cream, and why is a Siamese kitten born white? Over the unit, students find the pattern is inherited and tied to cooler skin, learn how DNA stores a gene and how the gene's message is copied and read to build a chain of amino acids, and trace how a one-letter DNA change swaps one amino acid so the pigment-making protein works only in cool skin.</p>
<h3>Learning targets</h3>
<table border="1" cellpadding="6"><tbody><tr><th>Target</th><th>I can</th><th>DOK</th><th>Taught</th><th>CFA</th></tr>
<tr><td>LS1-1.1 (priority)</td><td>describe DNA as a double helix built from nucleotides, each with a sugar, a phosphate, and a base, and state that DNA holds the instructions for building proteins.</td><td>1</td><td>Days 1 and 2</td><td>Day 2</td></tr>
<tr><td>LS1-1.2 (priority)</td><td>describe how a gene's message is copied and read to build a chain of amino acids.</td><td>2</td><td>Day 3 (lab)</td><td>Day 3</td></tr>
<tr><td>LS1-1.3 (priority)</td><td>explain how changing one DNA base can change a protein and what it does.</td><td>2</td><td>Day 4</td><td>Day 4</td></tr>
<tr><td>LS1-1.4 (priority)</td><td>explain how DNA, through proteins, gives different cells their different jobs.</td><td>3</td><td>Day 5</td><td>Day 5</td></tr>
<tr><td>LS1-1.5 (priority)</td><td>use case data, like sickle cell, to explain how a DNA change affects the body.</td><td>3</td><td>Day 6</td><td>Day 6</td></tr>
<tr><td>LS3-1.1 (supporting)</td><td>describe how chromosomes, DNA, and genes are related.</td><td>1</td><td>Day 1</td><td>none (not on the CSA)</td></tr>
<tr><td>LS3-1.2 (supporting)</td><td>explain how a child gets half of its chromosomes from each parent.</td><td>2</td><td>Day 1</td><td>none (not on the CSA)</td></tr>
<tr><td>LS3-1.3 (supporting)</td><td>ask questions that clarify how DNA and chromosomes carry the instructions for traits passed to offspring.</td><td>2</td><td>Day 1 (and the wonder questions all unit)</td><td>none (not on the CSA)</td></tr>
</tbody></table>
<p>The CSA never asks about mRNA or tRNA mechanics (LS1-1.2 teaches copy-then-read only) or about a specific protein's structure (LS1-1.5 uses the case as evidence).</p>
<h3>Day by day</h3>
<table border="1" cellpadding="6"><tbody><tr><th>Day</th><th>Focus</th><th>Targets</th><th>CFA</th></tr>
<tr><td>Day 1</td><td>Notice and wonder about a Siamese cat; temperature and litter data show the pattern is inherited and tied to cool skin. DNA holds the instructions for proteins; chromosome, DNA, and gene; one set of chromosomes from each parent; students write their own questions.</td><td>LS1-1.1 (second half), LS3-1.1, LS3-1.2, LS3-1.3</td><td>none</td></tr>
<tr><td>Day 2</td><td>DNA is a double helix of nucleotides (sugar, phosphate, base); base pairing; the order of bases is the message.</td><td>LS1-1.1</td><td>CFA LS1-1.1 (covers Days 1 and 2)</td></tr>
<tr><td>Day 3</td><td>Lab: build a gene out of gummy candy, copy its message, read the copy to build an amino acid chain; change one letter and compare.</td><td>LS1-1.2</td><td>CFA LS1-1.2</td></tr>
<tr><td>Day 4</td><td>One-letter DNA changes can change an amino acid (the Siamese cat), change whether a protein is made, or change nothing.</td><td>LS1-1.3</td><td>CFA LS1-1.3</td></tr>
<tr><td>Day 5</td><td>All cells have the same DNA but use different genes; map where the changed protein works by skin temperature.</td><td>LS1-1.4</td><td>CFA LS1-1.4</td></tr>
<tr><td>Day 6</td><td>Trace a DNA change to a protein to an effect on the body in two cases (the Siamese cat and a human gene change).</td><td>LS1-1.5</td><td>CFA LS1-1.5</td></tr>
<tr><td>Day 7</td><td>Mastery Path reviews for any CFA below a 3 (trigger: below 2.67); fix the Day 1 model; Write It about warm-raised and cool-raised kittens.</td><td>all</td><td>none</td></tr>
<tr><td>Day 8</td><td>CSA: HS-LS1-1, DNA to Proteins.</td><td>LS1-1.1 to LS1-1.5</td><td>none</td></tr>
</tbody></table>
<p>A CFA is a short exit ticket (about 6 minutes, 4 points). Students aim for at least a 3. In Canvas, a score below 2.67 opens the review assignment for that target through its Mastery Path (2.67 rounds up to a 3); students never see the decimal. There are 5 CFAs.</p>"""


def outcome_desc(tid):
    text, dok, _ = TARGETS[tid]
    return f"{text} [DOK {dok}; Priority (on the unit test); Unit 2.1]"


def review_name(tid):
    ican = TARGETS[tid][2].removeprefix("I can ").rstrip(".")
    return f"Review {tid}: {ican[0].upper() + ican[1:]} (Mastery Path)"


def main(course):
    api = N.Canvas("https://kernhigh.instructure.com", course, "")

    # 1. Outcomes.
    for tid, oid in OUTCOME_IDS.items():
        api.call("PUT", f"/api/v1/outcomes/{oid}", {"title": tid, "display_name": TARGETS[tid][2], "description": outcome_desc(tid)})
    api.call("PUT", f"/api/v1/outcomes/{RETIRED_OUTCOME}", {
        "title": "LS1-1.6 (retired 26-27)", "display_name": "Retired: now LS1-1.5",
        "description": "Retired in 26-27. The case-data target is now LS1-1.5."})
    print("Outcomes: LS1-1.1 to 1.5 updated; LS1-1.6 retired")

    # 2. Merge CFA LS1-1.2 into CFA LS1-1.1.
    old12 = api.nq("GET", f"/quizzes/{OLD_CFA_12}")
    if not old12["title"].startswith(OLD):
        target = sorted(api.nq("GET", f"/quizzes/{CFA['LS1-1.1']}/items"), key=lambda i: i["position"])
        pos = len(target)
        for it in sorted(api.nq("GET", f"/quizzes/{OLD_CFA_12}/items"), key=lambda i: i["position"]):
            pos += 1
            api.nq("POST", f"/quizzes/{CFA['LS1-1.1']}/items", {"item": {
                "position": pos, "points_possible": it["points_possible"], "entry_type": "Item", "entry": it["entry"]}})
        api.nq("PATCH", f"/quizzes/{CFA['LS1-1.1']}", {"quiz": {"points_possible": 4}})
        api.nq("PATCH", f"/quizzes/{OLD_CFA_12}", {"quiz": {"title": OLD + old12["title"]}})
        print(f"CFA LS1-1.1: added {pos - len(target)} questions from CFA LS1-1.2 ({pos} questions, graded out of 4)")
    rv = api.v1("GET", f"/assignments/{OLD_REVIEW_12}")
    if not rv["name"].startswith(OLD):
        api.v1("PUT", f"/assignments/{OLD_REVIEW_12}", {"assignment": {"name": OLD + rv["name"], "published": False}})
    rules = api.v1("GET", "/mastery_paths/rules?include[]=all")
    for r in rules:
        if r["trigger_assignment_id"] == OLD_CFA_12:
            api.v1("DELETE", f"/mastery_paths/rules/{r['id']}")
            print("Mastery Path rule for old CFA LS1-1.2 removed")
    for it in get_all(api, f"/modules/{MODULE}/items"):
        if it.get("content_id") in (OLD_CFA_12, OLD_REVIEW_12):
            api.v1("DELETE", f"/modules/{MODULE}/items/{it['id']}")
            print(f"Module: removed {it['title']}")

    # 3. Rename CFAs and reviews to the new numbers; update the target box on each review.
    for tid, qid in CFA.items():
        q = api.nq("GET", f"/quizzes/{qid}")
        if q["title"] != f"CFA {tid}":
            api.nq("PATCH", f"/quizzes/{qid}", {"quiz": {"title": f"CFA {tid}"}})
            print(f"{q['title']} -> CFA {tid}")
    for tid, aid in REVIEW.items():
        a = api.v1("GET", f"/assignments/{aid}")
        d = re.sub(r"<strong>Learning target LS1-1\.\d:</strong> [^<]*",
                   f"<strong>Learning target {tid}:</strong> {TARGETS[tid][2]}", a["description"] or "", count=1)
        api.v1("PUT", f"/assignments/{aid}", {"assignment": {"name": review_name(tid), "description": d}})
        print(f"{a['name'][:40]}... -> {review_name(tid)}")

    # 4. Module item titles follow their content.
    for it in get_all(api, f"/modules/{MODULE}/items"):
        if it["type"] != "Assignment":
            continue
        name = api.v1("GET", f"/assignments/{it['content_id']}")["name"]
        if it["title"] != name:
            api.v1("PUT", f"/modules/{MODULE}/items/{it['id']}", {"module_item": {"title": name}})

    # 5. Overview and Day 3 pages.
    api.v1("PUT", f"/pages/{OVERVIEW_SLUG}", {"wiki_page": {"body": OVERVIEW}})
    for slug in DAY3:
        body = api.v1("GET", f"/pages/{slug}")["body"]
        new = body.replace("LS1-1.3", "LS1-1.2")
        if new != body:
            api.v1("PUT", f"/pages/{slug}", {"wiki_page": {"body": new}})
    print("Overview rewritten; Day 3 pages renumbered (LS1-1.3 -> LS1-1.2)")


if __name__ == "__main__":
    main(sys.argv[1])
