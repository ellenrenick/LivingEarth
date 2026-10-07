"""Put Unit 1.3 (HS-LS1-6) outcomes, CFAs, practice test, and CSA into Canvas.

Creates, all unpublished:
- An outcome group with one outcome per learning target (unit13_bank.TARGETS).
- 6 CFAs, the practice test, and the CSA as New Quizzes, added to the unit's module.

Outcomes are not aligned to questions here; do that in the New Quizzes editor
(each question title starts with its target ID). Anything whose title already
exists is skipped, so the script is safe to run again.

Usage:
  CANVAS_TOKEN=... python3 newquiz_upload.py https://kernhigh.instructure.com 330720 [module_id]
"""

import json
import os
import ssl
import sys
import urllib.request
import uuid

import unit13_bank as U

CA = "/root/.ccr/ca-bundle.crt"
CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()


class Canvas:
    def __init__(self, base, course, token):
        self.base = base.rstrip("/")
        self.course = course
        self.token = token

    def call(self, method, path, body=None):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(self.base + path, data=data, method=method)
        req.add_header("Authorization", f"Bearer {self.token}")
        req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, context=CTX) as r:
                return json.loads(r.read() or "null")
        except urllib.error.HTTPError as e:
            raise SystemExit(f"{method} {path} -> {e.code}: {e.read().decode()[:800]}")

    def v1(self, method, path, body=None):
        return self.call(method, f"/api/v1/courses/{self.course}{path}", body)

    def nq(self, method, path, body=None):
        return self.call(method, f"/api/quiz/v1/courses/{self.course}{path}", body)


# ---------------------------------------------------------------------------
# Outcomes
# ---------------------------------------------------------------------------
def upload_outcomes(api):
    root = api.v1("GET", "/root_outcome_group")
    groups = api.call("GET", f"/api/v1/courses/{api.course}/outcome_groups/{root['id']}/subgroups?per_page=100")
    group = next((g for g in groups if g["title"] == U.GROUP_TITLE), None)
    if group is None:
        group = api.call("POST", f"/api/v1/courses/{api.course}/outcome_groups/{root['id']}/subgroups",
                         {"title": U.GROUP_TITLE, "description": U.GROUP_DESCRIPTION})
    links = api.call("GET", f"/api/v1/courses/{api.course}/outcome_groups/{group['id']}/outcomes?per_page=100")
    have = {l["outcome"]["title"] for l in links}
    for tid, name, _dok, ican in U.TARGETS:
        title = f"{tid}: {name}"
        if title in have:
            print(f"Outcome exists: {title}")
            continue
        api.call("POST", f"/api/v1/courses/{api.course}/outcome_groups/{group['id']}/outcomes", {
            "title": title,
            "display_name": f"{tid} {name}",
            "description": f"<p>{ican}</p>",
            "mastery_points": U.MASTERY_POINTS,
            "ratings": [{"description": d, "points": p} for d, p in U.RATINGS],
            "calculation_method": "highest",
        })
        print(f"Outcome: {title}")


# ---------------------------------------------------------------------------
# New Quizzes items
# ---------------------------------------------------------------------------
def place_key(item, n):
    """Move a choice item's key (written first) to KEY_POSITIONS[n]."""
    choices, ans = list(item["choices"]), item["answer"]
    key = choices.pop(ans)
    pos = U.KEY_POSITIONS[n % len(U.KEY_POSITIONS)]
    choices.insert(pos, key)
    return choices, pos


def html(s):
    return s if s.lstrip().startswith("<") else f"<p>{s}</p>"


def rubric_text(item):
    rows = " ".join(f"{s}: {lvl}. {d}" for s, lvl, d in item["rubric"])
    notes = " ".join(f"- {x}" for x in item["grading_notes"])
    return (f"Rubric (4 pts) - {rows} 0: blank or off-topic. "
            f"Grading notes: {notes} Exemplar (score 4): {item['exemplar']}")


def entry(item, title, n_choice):
    fb = {"neutral": html(item["feedback"])} if item.get("feedback") else {}
    t = item["type"]
    if t in ("choice", "multi"):
        if t == "choice":
            texts, keys = place_key(item, n_choice)
            keys = [keys]
        else:
            texts, keys = item["choices"], item["answer"]
        ids = [str(uuid.uuid4()) for _ in texts]
        e = {
            "interaction_type_slug": "choice" if t == "choice" else "multi-answer",
            "interaction_data": {"choices": [
                {"id": i, "position": p, "item_body": html(c)} for p, (i, c) in enumerate(zip(ids, texts), 1)]},
            "properties": {"shuffle_rules": {"choices": {"to_lock": [], "shuffled": False}}},
            "scoring_data": {"value": ids[keys[0]] if t == "choice" else [ids[k] for k in keys]},
            "scoring_algorithm": "Equivalence" if t == "choice" else "AllOrNothing",
        }
        if t == "choice":
            e["properties"]["vary_points_by_answer"] = False
    elif t == "tf":
        e = {
            "interaction_type_slug": "true-false",
            "interaction_data": {"true_choice": "True", "false_choice": "False"},
            "properties": {},
            "scoring_data": {"value": item["answer"]},
            "scoring_algorithm": "Equivalence",
        }
    elif t == "essay":
        e = {
            "interaction_type_slug": "essay",
            "interaction_data": {"rce": True, "essay": None, "word_count": True, "file_upload": False,
                                 "spell_check": True, "word_limit_enabled": False},
            "properties": {"word_limit": False, "spell_check": False, "word_limit_max": 0,
                           "word_limit_min": 0, "show_word_count": False, "rich_content_editor": False},
            "scoring_data": {"value": rubric_text(item)},
            "scoring_algorithm": "None",
        }
    else:
        raise ValueError(t)
    return {"title": title, "item_body": item["prompt"], "calculator_type": "none", "feedback": fb, **e}


def make_quiz(api, title, instructions, items, group_id):
    """items: list of (title, bank item). Returns the quiz."""
    quiz = api.nq("POST", "/quizzes", {"quiz": {
        "title": title,
        "instructions": instructions,
        "assignment_group_id": group_id,
        "grading_type": "points",
        "published": False,
        "quiz_settings": {"shuffle_answers": False, "shuffle_questions": False,
                          "has_time_limit": False, "one_at_a_time_type": "none", "allow_backtracking": True},
    }})
    n_choice = 0
    for pos, (qtitle, it) in enumerate(items, 1):
        pts = 4 if it["type"] == "essay" else 1
        api.nq("POST", f"/quizzes/{quiz['id']}/items", {"item": {
            "position": pos, "points_possible": pts, "entry_type": "Item",
            "entry": entry(it, qtitle, n_choice)}})
        if it["type"] == "choice":
            n_choice += 1
    total = sum(4 if it["type"] == "essay" else 1 for _, it in items)
    # Every Unit 1.3 grade is out of 4 (the 4-point scale); Canvas scales the raw score.
    api.nq("PATCH", f"/quizzes/{quiz['id']}", {"quiz": {"points_possible": U.GRADE_POINTS}})
    print(f"Quiz: {title} ({len(items)} questions, {total} raw pts, graded out of {U.GRADE_POINTS}) id={quiz['id']}")
    return quiz


def essay_numbers(items):
    return [i for i, (_, it) in enumerate(items, 1) if it["type"] == "essay"]


def lt_items(prefix, bank):
    out = []
    for n, it in enumerate(bank, 1):
        name = U.TARGET[it["lt"]][1]
        suffix = " (teacher-graded)" if it["type"] == "essay" else ""
        out.append((f"{prefix}{n} · {it['lt']} · {name}{suffix}", it))
    return out


def all_quizzes():
    """(title, instructions, items) for every quiz, in module order."""
    out = []
    for tid, name, _dok, ican in U.TARGETS:
        items = [(f"{tid}.{n} · {tid} · {name}", {**it, "lt": tid}) for n, it in enumerate(U.CFAS[tid], 1)]
        out.append((
            f"{U.UNIT} CFA {tid}: {name}",
            f"<p><strong>Learning target {tid}:</strong> {ican}</p>"
            "<p>5 questions. If you score below a B (under 67.5%, or fewer than 4 of 5 correct), "
            "a review for this target will open for you.</p>",
            items))
    ids = ", ".join(t[0] for t in U.TARGETS)
    for prefix, bank, label, lead in (
        ("P", U.PRACTICE, "Practice Test", "Practice for the Unit 1.3 CSA."),
        ("Q", U.CSA, "CSA", "Common summative assessment for Unit 1.3."),
    ):
        unlock = (" Your score unlocks your next assignment: a review (below a B, under 67.5%) "
                  "or an extension (A or B, 67.5% or higher).") if prefix == "P" else ""
        items = lt_items(prefix, bank)
        ess = essay_numbers(items)
        out.append((
            f"{U.UNIT} {label}: {U.UNIT_NAME} ({U.STANDARD})",
            f"<p>{lead} {len(items)} questions on learning targets {ids}. "
            f"Questions {ess[0]} and {ess[1]} are written responses your teacher will grade.{unlock}</p>",
            items))
    return out


def upload_quizzes(api, module_id=None):
    groups = api.v1("GET", "/assignment_groups?per_page=50")
    group = next((g for g in groups if g["name"] == "Assignments"), groups[0])
    existing = {q["title"] for q in api.nq("GET", "/quizzes?per_page=50")}
    for title, instr, items in all_quizzes():
        if title in existing:
            print(f"Quiz exists, skipped: {title}")
            continue
        quiz = make_quiz(api, title, instr, items, group["id"])
        if module_id:
            api.v1("POST", f"/modules/{module_id}/items",
                   {"module_item": {"type": "Assignment", "content_id": int(quiz["id"])}})


if __name__ == "__main__":
    base, course = sys.argv[1], sys.argv[2]
    module = sys.argv[3] if len(sys.argv) > 3 else None
    api = Canvas(base, course, os.environ.get("CANVAS_TOKEN", ""))
    upload_outcomes(api)
    upload_quizzes(api, module)
