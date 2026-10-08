"""Create the Unit 3.1 (HS-ESS1-5) CFAs, CSA, and Mastery Path reviews in a Canvas course.

Builds New Quizzes through the Canvas quiz API, review assignments through the
assignments API, Mastery Path rules (review opens when a CFA score is below 3 of 4),
and a day-by-day module. Everything is created unpublished.

Usage:
  CANVAS_TOKEN=... python3 canvas_upload.py https://kernhigh.instructure.com 330720 --dry-run
  CANVAS_TOKEN=... python3 canvas_upload.py https://kernhigh.instructure.com 330720
  CANVAS_TOKEN=... python3 canvas_upload.py https://kernhigh.instructure.com 330720 --cleanup

Created IDs are written to canvas_ids.json so --cleanup can remove them.
Running the upload twice creates duplicates.
"""

import json
import os
import ssl
import sys
import uuid
import urllib.error
import urllib.request
from pathlib import Path

import questions as Q

HERE = Path(__file__).parent
IDS_FILE = HERE / "canvas_ids.json"
CA = "/root/.ccr/ca-bundle.crt"
CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()

UNIT = "Unit 3.1"
MODULE_NAME = "Unit 3.1 Age of the Earth HS-ESS1-5"
ASSIGNMENT_POINTS = 4.0          # same 4-point scale as the Unit 1.3 quizzes
MASTERY_CUTOFF = 0.75            # below 3 of 4 (fewer than 4 of 5 correct) opens the review
CSA_TITLE = f"{UNIT} CSA: Age of the Earth (HS-ESS1-5)"

DAYS = {
    1: "Where Did the Old Ocean Floor Go?",
    2: "The Fossil Puzzle",
    3: "Making New Crust",
    4: "Where Crust Goes, and Where It Stays",
    5: "Reading Deep Time",
    6: "Build the Argument",
    7: "Cushion, Practice Test and Review",
    8: "Unit 3.1 CSA",
}


class Canvas:
    def __init__(self, base, course, token, dry=False):
        self.base = base.rstrip("/")
        self.course = course
        self.token = token
        self.dry = dry

    def call(self, method, path, body=None):
        if self.dry:
            return {"id": 0}
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(self.base + path, data=data, method=method)
        if self.token:  # in the cloud sandbox the proxy injects the credential instead
            req.add_header("Authorization", f"Bearer {self.token}")
        req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, context=CTX) as r:
                return json.loads(r.read() or "null")
        except urllib.error.HTTPError as e:
            raise SystemExit(f"{method} {path} -> {e.code}: {e.read().decode()[:600]}")

    def v1(self, method, path, body=None):
        return self.call(method, f"/api/v1/courses/{self.course}{path}", body)

    def quiz(self, method, path, body=None):
        return self.call(method, f"/api/quiz/v1/courses/{self.course}{path}", body)


# ------------------------------------------------------------------ item payloads
def entry(title, item):
    """Convert one question-bank item to a New Quizzes item entry."""
    kind = item["type"]
    base = {"title": title, "item_body": item["body"], "calculator_type": "none"}
    fb = {"neutral": item["feedback"]} if item.get("feedback") else {}
    shuffle = {"shuffle_rules": {"choices": {"to_lock": [], "shuffled": False}}}
    if kind in ("choice", "multi"):
        ids = [str(uuid.uuid4()) for _ in item["choices"]]
        base["interaction_data"] = {"choices": [
            {"id": i, "position": n + 1, "item_body": f"<p>{c}</p>"}
            for n, (i, c) in enumerate(zip(ids, item["choices"]))]}
        if kind == "choice":
            base.update(interaction_type_slug="choice", properties={**shuffle, "vary_points_by_answer": False},
                        scoring_data={"value": ids[item["answer"]]}, scoring_algorithm="Equivalence")
        else:
            base.update(interaction_type_slug="multi-answer", properties=shuffle,
                        scoring_data={"value": [ids[n] for n in item["answer"]]}, scoring_algorithm="AllOrNothing")
    elif kind == "tf":
        base.update(interaction_type_slug="true-false", properties={},
                    interaction_data={"true_choice": "True", "false_choice": "False"},
                    scoring_data={"value": item["answer"]}, scoring_algorithm="Equivalence")
    elif kind == "essay":
        base.update(interaction_type_slug="essay",
                    interaction_data={"rce": True, "essay": None, "word_count": True, "file_upload": False,
                                      "spell_check": True, "word_limit_enabled": False},
                    properties={"word_limit": False, "spell_check": False, "word_limit_max": 0,
                                "word_limit_min": 0, "show_word_count": False, "rich_content_editor": False},
                    scoring_data={"value": item["rubric"]}, scoring_algorithm="None")
    else:
        raise ValueError(kind)
    if fb:
        base["feedback"] = fb
    return base


def item_payload(position, points, title, item):
    return {"item": {"position": position, "points_possible": points, "entry_type": "Item",
                     "entry": entry(title, item)}}


def build_quiz(cv, title, instructions, items, group):
    """Create a New Quiz and add its items. items: list of (title, bank_item)."""
    quiz = cv.quiz("POST", "/quizzes", {"quiz": {
        "title": title, "instructions": instructions, "points_possible": ASSIGNMENT_POINTS,
        "assignment_group_id": group, "published": False,
        "quiz_settings": {"shuffle_answers": False, "shuffle_questions": False, "allow_backtracking": True}}})
    qid = quiz["id"]
    for n, (name, item) in enumerate(items, 1):
        points = 4.0 if item["type"] == "essay" else 1.0
        cv.quiz("POST", f"/quizzes/{qid}/items", item_payload(n, points, name, item))
    return qid


# ------------------------------------------------------------------ review page
def review_html(code, review):
    name, target = Q.TARGETS[code]
    parts = [
        '<div style="background:#eef5fb;border-left:4px solid #2b6cb0;padding:10px 14px;margin:12px 0">'
        f"<p><strong>Learning target {code}:</strong> {target}</p></div>",
        "<p>Your CFA score was below a 3 out of 4, so this page walks you back through the target. "
        "Read each section, try the checks, then answer the 3 questions at the bottom.</p>",
        f"<p><strong>Use:</strong> {review['use']}.</p>",
    ]
    for title, body, check, answer in review["sections"]:
        parts.append(f"<h3>{title}</h3>{body}<p>{check}</p>"
                     f"<details><summary>Check your answer</summary><p>{answer}</p></details>")
    qs = "".join(f"<li>{q}</li>" for q in review["questions"])
    parts.append("<h3>Show what you know</h3><p>Answer all 3 questions in the text box or upload a photo of your "
                 f"written answers. Use complete sentences.</p><ol>{qs}</ol>")
    return "\n".join(parts)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if len(args) != 2:
        raise SystemExit(__doc__)
    base, course = args
    token = os.environ.get("CANVAS_TOKEN", "")
    cv = Canvas(base, course, token, dry="--dry-run" in flags)

    if "--cleanup" in flags:
        ids = json.loads(IDS_FILE.read_text())
        for aid in ids["assignments"]:
            cv.v1("DELETE", f"/assignments/{aid}")
        if ids.get("module"):
            cv.v1("DELETE", f"/modules/{ids['module']}")
        IDS_FILE.unlink()
        print("Deleted", len(ids["assignments"]), "assignments and the module.")
        return

    group = cv.v1("GET", "/assignment_groups")
    group = next((g["id"] for g in group if g["name"] == "Assignments"), None) if not cv.dry else 0
    created = {"assignments": [], "module": None}
    cfa, review, rules = {}, {}, {}

    # CFAs
    for code, items in Q.CFAS.items():
        name = Q.TARGETS[code][0]
        title = f"{UNIT} CFA {code}: {name}"
        instr = (f"<p><strong>Learning target {code}:</strong> {Q.TARGETS[code][1]}</p>"
                 "<p>5 questions. If you score below a 3 out of 4 (fewer than 4 of 5 correct), "
                 "a review for this target will open for you.</p>")
        bank = [(f"{code}.{n} · {code} · {name}", it) for n, it in enumerate(items, 1)]
        cfa[code] = int(build_quiz(cv, title, instr, bank, group))
        created["assignments"].append(cfa[code])
        print("CFA", code, cfa[code])

    # CSA
    csa_items = [(f"Q{n} · {code} · {Q.TARGETS[code][0]}" + (" (teacher-graded)" if it["type"] == "essay" else ""), it)
                 for n, (code, it) in enumerate(Q.CSA, 1)]
    codes = sorted({c for c, _ in Q.CSA})
    essays = [str(n) for n, (_, it) in enumerate(Q.CSA, 1) if it["type"] == "essay"]
    csa_instr = (f"<p>Common summative assessment for {UNIT}. {len(Q.CSA)} questions on learning targets "
                 f"{', '.join(codes)}. Questions {' and '.join(essays)} are written responses your teacher will grade.</p>")
    csa = int(build_quiz(cv, CSA_TITLE, csa_instr, csa_items, group))
    created["assignments"].append(csa)
    print("CSA", csa)

    # Reviews
    for code, rv in Q.REVIEWS.items():
        name = Q.TARGETS[code][0]
        a = cv.v1("POST", "/assignments", {"assignment": {
            "name": f"{UNIT} Review {code}: {name} (Mastery Path)",
            "description": review_html(code, rv), "points_possible": ASSIGNMENT_POINTS,
            "grading_type": "pass_fail", "submission_types": ["online_text_entry", "online_upload"],
            "assignment_group_id": group, "published": False}})
        review[code] = a["id"]
        created["assignments"].append(a["id"])
        print("Review", code, a["id"])

    # Mastery Path rules: review opens when the CFA score is below the cutoff
    for code in Q.CFAS:
        cv.v1("POST", "/mastery_paths/rules", {
            "trigger_assignment_id": cfa[code],
            "scoring_ranges": [
                {"lower_bound": MASTERY_CUTOFF, "upper_bound": None, "assignment_sets": [{"assignment_set_associations": []}]},
                {"lower_bound": 0.0, "upper_bound": MASTERY_CUTOFF, "assignment_sets": [
                    {"assignment_set_associations": [{"assignment_id": review[code]}]}]}]})
        # Hide the review from everyone except students the rule releases it to
        cv.v1("PUT", f"/assignments/{review[code]}", {"assignment": {"only_visible_to_overrides": True}})
        print("Mastery Path rule", code)

    # Module, day by day
    mod = cv.v1("POST", "/modules", {"module": {"name": MODULE_NAME}})
    created["module"] = mod["id"]
    by_day = {}
    for code, day in Q.CFA_DAY.items():
        by_day.setdefault(day, []).append(code)
    for day, label in DAYS.items():
        cv.v1("POST", f"/modules/{mod['id']}/items", {"module_item": {"title": f"Day {day} · {label}", "type": "SubHeader"}})
        for code in by_day.get(day, []):
            for aid in (cfa[code], review[code]):
                cv.v1("POST", f"/modules/{mod['id']}/items", {"module_item": {"type": "Assignment", "content_id": aid}})
        if day == 8:
            cv.v1("POST", f"/modules/{mod['id']}/items", {"module_item": {"type": "Assignment", "content_id": csa}})
    if not cv.dry:
        IDS_FILE.write_text(json.dumps({**created, "cfa": cfa, "review": review, "csa": csa}, indent=1))
    print("Done." if not cv.dry else "Dry run only; nothing created.")


if __name__ == "__main__":
    main()
