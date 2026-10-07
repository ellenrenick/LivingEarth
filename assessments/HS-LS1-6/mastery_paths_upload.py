"""Add the Unit 1.3 (HS-LS1-6) Mastery Paths to Canvas, like Earth Science Unit 3.

Run after newquiz_upload.py. It:
- refreshes the CFA, practice test, and CSA instructions from newquiz_upload.py;
- creates the 6 CFA reviews, the practice test review, and the extension
  (4-point complete/incomplete, visible only to students the Mastery Path sends there);
- sets the Mastery Path rules: CFA below 67.5% -> that target's review;
  practice test below 67.5% -> review, 67.5% and up -> extension;
- puts the module in order: each CFA followed by its review, then the practice
  test, review, extension, and CSA.

Anything that already exists is reused, so it is safe to run again.

Usage:
  CANVAS_TOKEN=... python3 mastery_paths_upload.py https://kernhigh.instructure.com 330720 1634113
"""

import os
import sys

import newquiz_upload as N
import unit13_bank as U
import unit13_reviews as R

B_CUTOFF = 0.675  # a B on the 4-point scale (2.7 out of 4)


def assignments_by_name(api):
    out, page = {}, 1
    while True:
        batch = api.v1("GET", f"/assignments?per_page=100&page={page}")
        if not batch:
            return out
        out.update({a["name"]: a for a in batch})
        page += 1


def ensure_review(api, existing, title, html, group_id):
    if title in existing:
        print(f"Review exists: {title}")
        return existing[title]
    a = api.v1("POST", "/assignments", {"assignment": {
        "name": title,
        "description": html,
        "points_possible": U.GRADE_POINTS,
        "grading_type": "pass_fail",
        "submission_types": ["online_text_entry", "online_upload"],
        "only_visible_to_overrides": True,
        "assignment_group_id": group_id,
        "published": False,
    }})
    print(f"Review: {title}")
    return a


def ensure_rule(api, rules, trigger_id, below=None, above=None):
    """below/above: assignment id unlocked under / at-or-over the B cutoff."""
    def sets(aid):
        return [{"assignment_set_associations": [{"assignment_id": aid}]}] if aid else []
    body = {"trigger_assignment_id": trigger_id, "scoring_ranges": [
        {"lower_bound": B_CUTOFF, "upper_bound": None, "position": 1, "assignment_sets": sets(above)},
        {"lower_bound": 0.0, "upper_bound": B_CUTOFF, "position": 2, "assignment_sets": sets(below)},
    ]}
    old = next((r for r in rules if r["trigger_assignment_id"] == trigger_id), None)
    if old:
        api.v1("PUT", f"/mastery_paths/rules/{old['id']}", body)
    else:
        api.v1("POST", "/mastery_paths/rules", body)


def main(base, course, module_id):
    api = N.Canvas(base, course, os.environ.get("CANVAS_TOKEN", ""))
    groups = api.v1("GET", "/assignment_groups?per_page=50")
    group = next((g for g in groups if g["name"] == "Assignments"), groups[0])

    # Quizzes and their instructions.
    quizzes = {q["title"]: q for q in api.nq("GET", "/quizzes?per_page=50")}
    order = []
    for title, instr, _items in N.all_quizzes():
        q = quizzes[title]
        api.nq("PATCH", f"/quizzes/{q['id']}", {"quiz": {"instructions": instr}})
        order.append(int(q["id"]))
    cfa_ids, practice_id, csa_id = order[:6], order[6], order[7]

    # Review and extension assignments.
    existing = assignments_by_name(api)
    reviews = [ensure_review(api, existing, R.REVIEW_TITLE[t[0]], R.REVIEWS[t[0]], group["id"])["id"] for t in U.TARGETS]
    p_review = ensure_review(api, existing, R.PRACTICE_REVIEW_TITLE, R.PRACTICE_REVIEW, group["id"])["id"]
    ext = ensure_review(api, existing, R.EXTENSION_TITLE, R.EXTENSION, group["id"])["id"]

    # Mastery Path rules.
    rules = api.v1("GET", "/mastery_paths/rules")
    for cfa, rev in zip(cfa_ids, reviews):
        ensure_rule(api, rules, cfa, below=rev)
    ensure_rule(api, rules, practice_id, below=p_review, above=ext)
    print("Mastery Path rules set: 6 CFAs, practice test")

    # Module order: anything else first (lessons), then the assessment sequence.
    wanted = [x for pair in zip(cfa_ids, reviews) for x in pair] + [practice_id, p_review, ext, csa_id]
    items = api.v1("GET", f"/modules/{module_id}/items?per_page=100")
    by_content = {i.get("content_id"): i for i in items}
    for aid in wanted:
        if aid not in by_content:
            by_content[aid] = api.v1("POST", f"/modules/{module_id}/items",
                                     {"module_item": {"type": "Assignment", "content_id": aid}})
    others = [i for i in items if i.get("content_id") not in wanted]
    for pos, item in enumerate(others + [by_content[a] for a in wanted], 1):
        api.v1("PUT", f"/modules/{module_id}/items/{item['id']}", {"module_item": {"position": pos}})
    print(f"Module ordered: {len(others)} existing items, then {len(wanted)} assessment items")


if __name__ == "__main__":
    main(*sys.argv[1:4])
