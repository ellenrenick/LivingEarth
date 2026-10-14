"""Create a unit in a Canvas course through the API: overview page, CFA quizzes, review page, CSA, and a module.

Usage: python3 canvas_unit.py <STD> <course id> [--plan plan_8day]
Everything is created unpublished. Running it again creates duplicates (it stops if the module name exists).
Uses CANVAS_TOKEN if set; otherwise relies on the environment proxy to supply credentials.
"""

import importlib.util
import json
import os
import re
import ssl
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "HS-LS1-6"))
import build  # noqa: E402
import build_unit  # noqa: E402

BASE = "https://kernhigh.instructure.com"
CA = "/root/.ccr/ca-bundle.crt"
CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()
MC_POINTS = 2


class Canvas:
    def __init__(self, course):
        self.root = f"{BASE}/api/v1/courses/{course}"
        self.token = os.environ.get("CANVAS_TOKEN")

    def call(self, method, path, body=None):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(self.root + path, data=data, method=method)
        if self.token:
            req.add_header("Authorization", f"Bearer {self.token}")
        req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req, context=CTX) as r:
            return json.loads(r.read() or "null")


def load(path, name):
    return build_unit.load(path, name)


def mc_q(name, prompt, choices, answer, feedback, points=MC_POINTS):
    return {"question_name": name, "question_type": "multiple_choice_question", "question_text": prompt,
            "points_possible": points, "neutral_comments_html": f"<p>{feedback}</p>",
            "answers": [{"answer_html": c, "answer_weight": 100 if i == answer else 0} for i, c in enumerate(choices)]}


def essay_q(name, prompt, points, feedback_html):
    return {"question_name": name, "question_type": "essay_question", "question_text": prompt,
            "points_possible": points, "neutral_comments_html": feedback_html}


def header_q(title):
    return {"question_name": title, "question_type": "text_only_question", "question_text": f"<h3>{title}</h3>"}


def add_questions(api, quiz_id, questions):
    for pos, q in enumerate(questions, 1):
        api.call("POST", f"/quizzes/{quiz_id}/questions", {"question": {**q, "position": pos}})


def make_quiz(api, title, description, questions, quiz_type="assignment", time_limit=None):
    quiz = {"title": title, "description": description, "shuffle_answers": False, "published": False,
            "quiz_type": quiz_type, "allowed_attempts": 1}
    if time_limit:
        quiz["time_limit"] = time_limit
    made = api.call("POST", "/quizzes", {"quiz": quiz})
    add_questions(api, made["id"], questions)
    return made


def csa_questions(q):
    mc = build.shuffled_mc(q)
    qs = [header_q(q.MATCHING["title"]), {
        "question_name": q.MATCHING["title"], "question_type": "matching_question", "question_text": q.MATCHING["prompt"],
        "points_possible": q.MATCHING["points"],
        "answers": [{"answer_match_left": t, "answer_match_right": d, "answer_weight": 100} for t, d in q.MATCHING["pairs"]],
        "matching_answer_incorrect_matches": "\n".join(q.MATCHING["distractors"])}, header_q("Part 2: Multiple Choice")]
    qs += [mc_q(f"MC {i} (DOK {it['dok']})", it["prompt"], it["choices"], it["answer"], it["feedback"]) for i, it in enumerate(mc, 1)]
    qs.append(header_q("Part 3: Free Response"))
    for i, it in enumerate(q.FREE_RESPONSE, 1):
        rows = "".join(f"<tr><td><strong>{s}</strong></td><td>{l}</td><td>{d}</td></tr>" for s, l, d in it["rubric"])
        notes = "".join(f"<li>{n}</li>" for n in it["grading_notes"])
        fb = ("<p><strong>4-point scoring rubric</strong></p><table border=\"1\" cellpadding=\"4\"><tr><th>Score</th><th>Level</th><th>Descriptor</th></tr>"
              f"{rows}<tr><td><strong>0</strong></td><td>No response</td><td>Blank or off-topic.</td></tr></table>"
              f"<p><strong>Grading notes</strong></p><ul>{notes}</ul><p><strong>Exemplar (score 4):</strong> {it['exemplar']}</p>")
        qs.append(essay_q(f"Free response {i} (DOK {it['dok']})", it["prompt"], it["points"], fb))
    return qs


def cfa_questions(cfa):
    qs = []
    for n, it in enumerate(build_unit.cfa_items(cfa), 1):
        if "choices" in it:
            qs.append(mc_q(f"Q{n}", it["prompt"], it["choices"], it["answer"], it["feedback"]))
        else:
            rows = "".join(f"<tr><td><strong>{s}</strong></td><td>{d}</td></tr>" for s, d in it["criteria"])
            fb = f"<p><strong>Scoring</strong></p><table border=\"1\" cellpadding=\"4\"><tr><th>Score</th><th>Criteria</th></tr>{rows}</table><p><strong>Model answer:</strong> {it['exemplar']}</p>"
            qs.append(essay_q(f"Q{n}", it["prompt"], it["points"], fb))
    return qs


def overview_html(plan, cfa_titles):
    rows = "".join(f"<tr><td>{d[0].split(':')[0]}</td><td>{d[1]}</td><td>{d[2]}</td><td>{', '.join('CFA ' + c for c in d[3]) or '&mdash;'}</td><td>{d[4]}</td></tr>" for d in plan.DAYS)
    changes = "".join(f"<li>{c}</li>" for c in plan.CHANGES)
    phen = f"<h3>Anchoring phenomenon</h3><p>{plan.PHENOMENON}</p>" if hasattr(plan, "PHENOMENON") else ""
    return (f"<h2>{plan.MODULE_NAME}</h2>{phen}<p>Eight 45-minute class periods. Every priority learning target and its CFA is kept; the supporting standard is taught lightly and is not on the CSA.</p>"
            f"<table border=\"1\" cellpadding=\"6\"><tr><th>Day</th><th>Focus</th><th>Standards</th><th>CFA</th><th>Notes</th></tr>{rows}</table>"
            f"<h3>How this differs from the full 13-day unit</h3><ul>{changes}</ul>"
            "<p>A CFA is a short exit ticket (about 6 minutes, 6 points). Mastery is 4 of 6. Students who score below 4 use the matching section of the Review on Day 7.</p>")


def main():
    std, course = sys.argv[1], sys.argv[2]
    plan_name = sys.argv[sys.argv.index("--plan") + 1] if "--plan" in sys.argv else None
    unit_dir = ROOT / std
    q = load(unit_dir / "questions.py", f"q_{std}")
    cfa_mod = load(unit_dir / "cfa.py", f"c_{std}")
    plan = load(unit_dir / f"{plan_name}.py", "plan")
    api = Canvas(course)
    if any(m["name"] == plan.MODULE_NAME for m in api.call("GET", "/modules?per_page=100")):
        sys.exit(f"Module '{plan.MODULE_NAME}' already exists in course {course}; delete it first.")
    cfas = {c["id"]: c for c in cfa_mod.CFAS}

    overview = api.call("POST", "/pages", {"wiki_page": {"title": f"{plan.MODULE_NAME}: Overview and Day-by-Day Plan", "body": overview_html(plan, None), "published": False}})
    review_src = (unit_dir / f"{std}_review.html").read_text(encoding="utf-8")
    review_body = re.sub(r"<!--.*?-->", "", re.search(r"<body>(.*)</body>", review_src, re.S).group(1), flags=re.S).strip()
    review = api.call("POST", "/pages", {"wiki_page": {"title": f"{std} Review: {cfa_mod.UNIT_TITLE}", "body": review_body, "published": False}})
    cfa_quiz = {}
    for cid, c in cfas.items():
        desc = f"<p>Exit ticket (about 6 minutes, 6 points). Learning target: {c['lt']}</p>"
        cfa_quiz[cid] = make_quiz(api, f"CFA {cid}", desc, cfa_questions(c))
        print("CFA", cid, cfa_quiz[cid]["html_url"])
    csa = make_quiz(api, q.TITLE + " (CSA)", q.DESCRIPTION + "<p>45 minutes, 30 points.</p>", csa_questions(q), time_limit=45)
    print("CSA", csa["html_url"])

    mod = api.call("POST", "/modules", {"module": {"name": plan.MODULE_NAME, "published": False}})
    pos = 0

    def item(**kw):
        nonlocal pos
        pos += 1
        api.call("POST", f"/modules/{mod['id']}/items", {"module_item": {"position": pos, **kw}})

    item(title="Overview and day-by-day plan", type="Page", page_url=overview["url"])
    lessons = load(unit_dir / "lessons_8day.py", "lessons") if (unit_dir / "lessons_8day.py").exists() else None
    if lessons:
        mp = api.call("POST", "/pages", {"wiki_page": {"title": "Unit materials and prep (teacher)", "body": lessons.MATERIALS_PAGE, "published": False}})
        item(title="Unit materials and prep (teacher)", type="Page", page_url=mp["url"])
    for title, focus, _std, cfa_ids, _note in plan.DAYS:
        item(title=title, type="SubHeader")
        for it in (lessons.LESSONS.get(title, []) if lessons else []):
            if it[0] == "page":
                pg = api.call("POST", "/pages", {"wiki_page": {"title": it[1], "body": it[2], "published": False}})
                item(title=it[1], type="Page", page_url=pg["url"], indent=1)
            else:
                asg = api.call("POST", "/assignments", {"assignment": {"name": it[1], "description": it[2], "points_possible": it[3],
                                                                         "submission_types": ["online_text_entry"], "published": False}})
                item(title=it[1], type="Assignment", content_id=asg["id"], indent=1)
        for cid in cfa_ids:
            item(title=f"CFA {cid}", type="Quiz", content_id=cfa_quiz[cid]["id"], indent=1)
        if title.startswith("Day 7"):
            item(title=f"{std} Review", type="Page", page_url=review["url"], indent=1)
        if title.startswith("Day 8"):
            item(title=q.TITLE + " (CSA)", type="Quiz", content_id=csa["id"], indent=1)
    print("Module", mod["id"], f"{BASE}/courses/{course}/modules")


if __name__ == "__main__":
    main()
