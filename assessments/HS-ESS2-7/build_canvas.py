"""Build Unit 3.1 (Changing Earth, Changing Life, HS-ESS2-7) in a Canvas course.

Usage: CANVAS_TOKEN=... python3 build_canvas.py https://kernhigh.instructure.com 330720
Everything is created unpublished. Running it twice creates a second copy.
Created ids are written to created_ids.json (so a partial run can be cleaned up).
"""
import json
import os
import ssl
import sys
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

import assess
import days

HERE = Path(__file__).parent
CA = "/root/.ccr/ca-bundle.crt"
CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()
base, course = sys.argv[1].rstrip("/"), sys.argv[2]
tok = os.environ["CANVAS_TOKEN"]
GROUP = None  # filled from the course's Unit 3.2 CFA group below
UNIT = "Unit 3.1"
MODULE_NAME = "Unit 3.1 Earth and Life HS-ESS2-7"
created = {"pages": [], "assignments": [], "quizzes": [], "rules": [], "module": None}


def api(method, path, body=None):
    req = urllib.request.Request(base + path, data=json.dumps(body).encode() if body is not None else None, method=method)
    req.add_header("Authorization", "Bearer " + tok)
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, context=CTX) as r:
        return json.loads(r.read() or "null")


C = f"/api/v1/courses/{course}"
Q = f"/api/quiz/v1/courses/{course}/quizzes"
SETTINGS = {"calculator_type": "none", "filter_ip_address": False, "filters": {}, "one_at_a_time_type": "none", "allow_backtracking": True,
            "shuffle_answers": False, "shuffle_questions": False, "require_student_access_code": False, "student_access_code": None,
            "has_time_limit": False, "session_time_limit_in_seconds": 0, "multiple_attempts": {}, "result_view_settings": {}}


def page(title, body):
    p = api("POST", C + "/pages", {"wiki_page": {"title": title, "body": body, "published": False}})
    created["pages"].append(p["url"])
    return p


def assignment(name, description, points=4):
    a = api("POST", C + "/assignments", {"assignment": {"name": name, "description": description, "points_possible": points, "published": False,
            "submission_types": ["online_text_entry", "online_upload"], "assignment_group_id": GROUP}})
    created["assignments"].append(a["id"])
    return a


def quiz(title, instructions):
    q = api("POST", Q, {"quiz": {"title": title, "instructions": instructions, "points_possible": 4, "assignment_group_id": str(GROUP), "quiz_settings": SETTINGS}})
    created["quizzes"].append(q["id"])
    return q


def add_item(qid, pos, pts, entry):
    return api("POST", f"{Q}/{qid}/items", {"item": {"position": pos, "points_possible": pts, "entry_type": "Item", "entry": dict(entry, calculator_type="none")}})


def choice_item(qid, pos, pts, title, stem, opts, correct, feedback):
    ids = [str(uuid.uuid4()) for _ in opts]
    multi = isinstance(correct, list)
    entry = {"title": title, "item_body": f"<p>{stem}</p>", "interaction_type_slug": "multi-answer" if multi else "choice",
             "interaction_data": {"choices": [{"id": i, "position": n + 1, "item_body": f"<p>{o}</p>"} for n, (i, o) in enumerate(zip(ids, opts))]},
             "properties": {"shuffle_rules": {"choices": {"to_lock": [], "shuffled": False}}} if multi else {"shuffle_rules": {"choices": {"to_lock": [], "shuffled": False}}, "vary_points_by_answer": False},
             "scoring_data": {"value": [ids[i] for i in correct] if multi else ids[correct]},
             "scoring_algorithm": "AllOrNothing" if multi else "Equivalence", "feedback": {"neutral": f"<p>{feedback}</p>"}}
    return add_item(qid, pos, pts, entry)


def matching_item(qid, pos, pts, title, stem, pairs, extra):
    qids = [str(uuid.uuid4()) for _ in pairs]
    entry = {"title": title, "item_body": stem, "interaction_type_slug": "matching",
             "interaction_data": {"answers": [p[1] for p in pairs] + extra, "questions": [{"id": i, "item_body": p[0]} for i, p in zip(qids, pairs)]},
             "properties": {"shuffle_rules": {"questions": {"shuffled": False}}},
             "scoring_data": {"value": {i: p[1] for i, p in zip(qids, pairs)},
                              "edit_data": {"matches": [{"answer_body": p[1], "question_id": i, "question_body": p[0]} for i, p in zip(qids, pairs)], "distractors": extra}},
             "scoring_algorithm": "PartialDeep"}
    return add_item(qid, pos, pts, entry)


def essay_item(qid, pos, pts, title, body, scoring):
    entry = {"title": title, "item_body": f"<p>{body}</p>", "interaction_type_slug": "essay",
             "interaction_data": {"rce": True, "essay": None, "word_count": True, "file_upload": False, "spell_check": True, "word_limit_enabled": False},
             "properties": {"word_limit": False, "spell_check": False, "word_limit_max": 0, "word_limit_min": 0, "show_word_count": False, "rich_content_editor": False},
             "scoring_data": {"value": scoring}, "scoring_algorithm": "None"}
    return add_item(qid, pos, pts, entry)


def main():
    global GROUP
    GROUP = api("GET", f"{C}/assignments?search_term=" + urllib.parse.quote("Unit 3.2 CFA"))[0]["assignment_group_id"]
    mods = api("GET", C + "/modules?per_page=100")
    target = next(m for m in mods if m["name"].startswith("Unit 3.2"))
    # ---- student pages, then teacher pages (they link to the student pages)
    spages, tpages = {}, {}
    for d in days.DAYS:
        n = d["n"]
        s = d["s"]
        body = days.student(n, d["title"], d["targets"], s["driving"], s["focus"], s["reading"], s["nb"], s["parts"], s["wrap"])
        spages[n] = page(f"{UNIT} Day {n}: {d['title']}", body)
        print("page", spages[n]["title"])
    for d in days.DAYS:
        n, t = d["n"], d["t"]
        tg = ", ".join(f"ESS2-{k}" for k in d["targets"])
        url = f"{base}/courses/{course}/pages/{spages[n]['url']}"
        tpages[n] = page(f"TEACHER: {UNIT} Day {n}: {d['title']}", days.teacher(n, url, tg, t["glance"], t["materials"], t["agenda"], t["notes"], t["key"], t["supports"]))
    # ---- assignments
    lesson1 = assignment("Lesson 1: Rusty Stripes", assess.LESSON1)
    cer = assignment(f"{UNIT} CER: Earth and life changed each other", assess.CER)
    sketch = assignment("Lesson 7: SketchNotes: Earth's systems and life", assess.SKETCH)
    enrich = assignment(f"{UNIT} Enrichment: Choice Board", assess.ENRICH)
    reviews, cfas = {}, {}
    for k, cf in assess.CFAS.items():
        reviews[k] = assignment(f"{UNIT} Review ESS2-{k}: {cf['title']} (Mastery Path)", assess.review_html(k))
        q = quiz(f"{UNIT} CFA ESS2-{k}: {cf['title']}",
                 f"<p>Learning target ESS2-{k}: {days.TARGETS[k]}</p><p>5 questions. If you score below a 3 out of 4 (fewer than 4 of 5 correct), a review for this target will open for you.</p>")
        for pos, (stem, opts, correct, fb) in enumerate(cf["items"], 1):
            choice_item(q["id"], pos, 1.0, f"ESS2-{k}.{pos} · ESS2-{k} · {cf['title']}", stem, opts, correct, fb)
        cfas[k] = q
        print("cfa", k, q["id"])
    # ---- CSA
    csa = quiz(f"{UNIT} CSA: Changing Earth, Changing Life (HS-ESS2-7)",
               "<p>Common summative assessment for Unit 3.1. 16 questions on learning targets ESS2-7.1 to ESS2-7.6 (30 points): 6 matching terms, 8 multiple-choice questions, and 2 written responses that your teacher will grade. You have 45 minutes.</p>")
    pos = 1
    matching_item(csa["id"], pos, 6.0, "Q1 · Vocabulary", "<p><strong>Match each term to its meaning.</strong> Two meanings will not be used.</p>", assess.CSA_MATCH, assess.CSA_EXTRA)
    for i, (k, stem, opts, correct, fb) in enumerate(assess.CSA_MC, 1):
        pos += 1
        choice_item(csa["id"], pos, 2.0, f"Q{pos} · ESS2-{k}", stem, opts, correct, fb)
    for k, body, scoring in (assess.FR1, assess.FR2):
        pos += 1
        essay_item(csa["id"], pos, 4.0, f"Q{pos} · ESS2-{k} (teacher-graded)", body, scoring)
    print("csa", csa["id"])
    # ---- mastery path rules (below 75% opens the review)
    for k in assess.CFAS:
        r = api("POST", C + "/mastery_paths/rules", {"trigger_assignment_id": int(cfas[k]["id"]), "scoring_ranges": [
            {"lower_bound": 0.75, "upper_bound": None, "assignment_sets": [{"assignment_set_associations": []}]},
            {"lower_bound": 0.0, "upper_bound": 0.75, "assignment_sets": [{"assignment_set_associations": [{"assignment_id": int(reviews[k]["id"]), "position": 1}]}]}]})
        created["rules"].append(r.get("id") if isinstance(r, dict) else None)
        print("rule", k)
    # ---- module
    mod = api("POST", C + "/modules", {"module": {"name": MODULE_NAME, "position": target["position"]}})
    created["module"] = mod["id"]

    def item(kind, title, **kw):
        body = {"title": title, "type": kind, "indent": 0}
        body.update(kw)
        api("POST", f"{C}/modules/{mod['id']}/items", {"module_item": body})

    def asg(a):
        item("Assignment", a["name"], content_id=a["id"], indent=1)

    def pg(p):
        item("Page", p["title"], page_url=p["url"], indent=1)

    for d in days.DAYS:
        n = d["n"]
        item("SubHeader", f"Day {n} · {d['short']}")
        pg(spages[n])
        if n == 1:
            asg(lesson1)
        if n == 5:
            asg(cer)
        if n == 7:
            asg(sketch)
        if d.get("cfa"):
            k = d["cfa"]
            asg({"id": cfas[k]["id"], "name": cfas[k]["title"]})
            asg(reviews[k])
        if n == 9:
            asg(enrich)
        if n == 10:
            asg({"id": csa["id"], "name": csa["title"]})
    item("SubHeader", f"💥{UNIT} TEACHER PAGES (keep unpublished)💥")
    for d in days.DAYS:
        pg(tpages[d["n"]])
    (HERE / "created_ids.json").write_text(json.dumps(created, indent=1))
    print("module", mod["id"], MODULE_NAME)


if __name__ == "__main__":
    try:
        main()
    finally:
        (HERE / "created_ids.json").write_text(json.dumps(created, indent=1))
