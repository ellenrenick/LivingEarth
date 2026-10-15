"""Rebuild classic Canvas quizzes as New Quizzes (rule: every CFA and CSA is a New Quiz).

For each classic quiz id given:
- creates a New Quiz with the same title, instructions, assignment group, dates, and
  questions (multiple choice, multiple answer, true/false, essay, matching), graded out
  of the same points. Text-only section headers ("Part 2: ...") are dropped, since the
  questions are shuffled;
- applies the CFA/CSA settings (shuffle questions and answers, results hidden);
- puts it in the classic quiz's module spot(s) and moves any Mastery Path rule over;
- renames the classic quiz "OLD classic: ..." and leaves it unpublished (nothing is deleted).

Question points keep the classic ratios (the smallest question = 1 point).
Safe to run again: a quiz whose New Quiz already exists is skipped.

  python3 classic_to_newquiz.py https://kernhigh.instructure.com 330720 1570433 1570434 ...
"""

import sys
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "lessons"))
import newquiz_upload as N  # noqa: E402
from canvas_lessons_upload import get_all  # noqa: E402

OLD_PREFIX = "OLD classic: "


def ans_html(a):
    return a.get("html") or a.get("text") or ""


def entry(q, title, body):
    t = q["question_type"]
    fb = q.get("neutral_comments_html") or q.get("neutral_comments") or ""
    feedback = {}
    if t in ("multiple_choice_question", "multiple_answers_question", "true_false_question"):
        answers = q["answers"]
        if t == "true_false_question":
            correct = next(a for a in answers if a["weight"] > 0)
            e = {"interaction_type_slug": "true-false",
                 "interaction_data": {"true_choice": "True", "false_choice": "False"},
                 "properties": {}, "scoring_data": {"value": ans_html(correct).strip().lower() == "true"},
                 "scoring_algorithm": "Equivalence"}
        else:
            ids = [str(uuid.uuid4()) for _ in answers]
            right = [i for i, a in zip(ids, answers) if a["weight"] > 0]
            multi = t == "multiple_answers_question"
            e = {"interaction_type_slug": "multi-answer" if multi else "choice",
                 "interaction_data": {"choices": [{"id": i, "position": p, "item_body": N.html(ans_html(a))}
                                                  for p, (i, a) in enumerate(zip(ids, answers), 1)]},
                 "properties": {"shuffle_rules": {"choices": {"to_lock": [], "shuffled": True}}},
                 "scoring_data": {"value": right if multi else right[0]},
                 "scoring_algorithm": "AllOrNothing" if multi else "Equivalence"}
            if not multi:
                e["properties"]["vary_points_by_answer"] = False
        if fb:
            feedback = {"neutral": fb}
    elif t == "essay_question":
        # The classic rubric lives in the grader notes, never in student-facing feedback.
        e = {"interaction_type_slug": "essay",
             "interaction_data": {"rce": True, "essay": None, "word_count": True, "file_upload": False,
                                  "spell_check": True, "word_limit_enabled": False},
             "properties": {"word_limit": False, "spell_check": False, "word_limit_max": 0,
                            "word_limit_min": 0, "show_word_count": False, "rich_content_editor": False},
             "scoring_data": {"value": fb}, "scoring_algorithm": "None"}
    elif t == "matching_question":
        pairs = [(a.get("left") or ans_html(a), a.get("right", "")) for a in q["answers"]]
        distractors = [d for d in (q.get("matching_answer_incorrect_matches") or "").split("\n") if d.strip()]
        qids = [str(uuid.uuid4()) for _ in pairs]
        answers = [r for _, r in pairs] + distractors
        e = {"interaction_type_slug": "matching",
             "interaction_data": {"answers": answers,
                                  "questions": [{"id": i, "item_body": left} for i, (left, _) in zip(qids, pairs)]},
             "properties": {"shuffle_rules": {"questions": {"shuffled": False}}},
             "scoring_data": {"value": {i: right for i, (_, right) in zip(qids, pairs)},
                              "edit_data": {"matches": [{"answer_body": right, "question_id": i, "question_body": left}
                                                        for i, (left, right) in zip(qids, pairs)],
                                            "distractors": distractors}},
             "scoring_algorithm": "PartialDeep"}
    else:
        raise SystemExit(f"Unsupported question type {t} in '{title}'")
    return {"title": title, "item_body": body, "calculator_type": "none", "feedback": feedback, **e}


def convert(api, qid, nq_titles, rules):
    q = api.v1("GET", f"/quizzes/{qid}")
    title = q["title"].removeprefix(OLD_PREFIX)
    if title in nq_titles:
        print(f"Skip (New Quiz exists): {title}")
        return
    asg = api.v1("GET", f"/assignments/{q['assignment_id']}")
    questions = get_all(api, f"/quizzes/{qid}/questions")
    scored = [x for x in questions if x["question_type"] != "text_only_question"]
    unit = min(x["points_possible"] for x in scored if x["points_possible"] > 0)

    nq = api.nq("POST", "/quizzes", {"quiz": {
        "title": title, "instructions": q.get("description") or "",
        "assignment_group_id": q["assignment_group_id"], "grading_type": "points", "published": False,
        "due_at": asg.get("due_at"), "unlock_at": asg.get("unlock_at"), "lock_at": asg.get("lock_at"),
        "quiz_settings": {"has_time_limit": False, "one_at_a_time_type": "none", "allow_backtracking": True,
                          **N.CFA_CSA_SETTINGS}}})
    pos, raw = 0, 0
    for x in questions:
        if x["question_type"] == "text_only_question":
            continue
        pos += 1
        pts = max(1, round(x["points_possible"] / unit))
        raw += pts
        api.nq("POST", f"/quizzes/{nq['id']}/items", {"item": {
            "position": pos, "points_possible": pts, "entry_type": "Item",
            "entry": entry(x, x.get("question_name") or f"Question {pos}", x["question_text"])}})
    api.nq("PATCH", f"/quizzes/{nq['id']}", {"quiz": {"points_possible": q["points_possible"] or asg["points_possible"]}})
    new_id = int(nq["id"])  # a New Quiz's id is its assignment id
    print(f"New Quiz: {title} ({pos} questions, {raw} raw pts, graded out of {asg['points_possible']}) id={new_id}")

    # Module spots.
    for m in get_all(api, "/modules"):
        for it in get_all(api, f"/modules/{m['id']}/items"):
            if it["type"] == "Quiz" and it.get("content_id") == qid:
                api.v1("POST", f"/modules/{m['id']}/items", {"module_item": {
                    "type": "Assignment", "content_id": new_id, "position": it["position"], "indent": it.get("indent", 0)}})
                api.v1("DELETE", f"/modules/{m['id']}/items/{it['id']}")
                print(f"  module '{m['name']}': replaced at position {it['position']}")

    # Mastery Path rule.
    old = next((r for r in rules if r["trigger_assignment_id"] == q["assignment_id"]), None)
    if old:
        ranges = [{"lower_bound": s["lower_bound"], "upper_bound": s["upper_bound"], "position": s["position"],
                   "assignment_sets": [{"assignment_set_associations": [
                       {"assignment_id": a["assignment_id"]} for a in st.get("assignment_set_associations", [])]}
                       for st in s.get("assignment_sets", [])]}
                  for s in old["scoring_ranges"]]
        api.v1("POST", "/mastery_paths/rules", {"trigger_assignment_id": new_id, "scoring_ranges": ranges})
        api.v1("DELETE", f"/mastery_paths/rules/{old['id']}")
        print("  Mastery Path rule moved to the New Quiz")

    api.v1("PUT", f"/quizzes/{qid}", {"quiz": {"title": OLD_PREFIX + title, "published": False}})


def main(base, course, *ids):
    api = N.Canvas(base, course, "")
    nq_titles = set()
    page = 1
    while True:
        r = api.nq("GET", f"/quizzes?per_page=50&page={page}")
        nq_titles |= {x["title"] for x in r}
        if len(r) < 50:
            break
        page += 1
    rules = api.v1("GET", "/mastery_paths/rules?include[]=all")
    for qid in ids:
        convert(api, int(qid), nq_titles, rules)


if __name__ == "__main__":
    main(*sys.argv[1:])
