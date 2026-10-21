"""Create the reassessments as New Quizzes in a Canvas course, in a "Reassessments" module at the top.

Everything is created unpublished. Quiz settings match the Unit 1.1 / 1.3 assessments
(shuffled questions and answers, results hidden from students).

Usage:
  CANVAS_TOKEN=... python3 upload_canvas.py https://kernhigh.instructure.com 330720
"""

import json
import os
import ssl
import sys
import urllib.request
import uuid

import questions

CA = "/root/.ccr/ca-bundle.crt"
CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()

MODULE_NAME = "Reassessments"
ASSIGNMENT_GROUP = "Assignments"  # same group the Unit 1.1 and 1.3 assessments use

QUIZ_SETTINGS = {
    "calculator_type": "none",
    "shuffle_answers": True,
    "shuffle_questions": True,
    "allow_backtracking": True,
    "result_view_settings": {
        "result_view_restricted": True,
        "display_items": False,
        "display_item_response": False,
        "display_item_response_correctness": False,
        "display_item_correct_answer": False,
        "display_item_feedback": False,
        "display_points_awarded": False,
        "display_points_possible": False,
    },
}


class Canvas:
    def __init__(self, base, course, token=None):
        self.base = base.rstrip("/")
        self.course = course
        self.token = token

    def call(self, method, path, body=None):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(self.base + path, data=data, method=method)
        if self.token:  # on the cloud sandbox the proxy injects the token for this host
            req.add_header("Authorization", f"Bearer {self.token}")
        req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req, context=CTX) as r:
            return json.loads(r.read() or "null")

    def classic(self, method, path, body=None):
        return self.call(method, f"/api/v1/courses/{self.course}{path}", body)

    def new_quiz(self, method, path, body=None):
        return self.call(method, f"/api/quiz/v1/courses/{self.course}{path}", body)


def _id():
    return str(uuid.uuid4())


def choice_item(item):
    ids = [_id() for _ in item["choices"]]
    return "choice", {
        "choices": [
            {"id": i, "position": n, "item_body": f"<p>{c}</p>"}
            for n, (i, c) in enumerate(zip(ids, item["choices"]), 1)
        ],
    }, {"value": ids[item["answer"]]}, "Equivalence"


def multi_item(item):
    ids = [_id() for _ in item["choices"]]
    return "multi-answer", {
        "choices": [
            {"id": i, "position": n, "item_body": f"<p>{c}</p>"}
            for n, (i, c) in enumerate(zip(ids, item["choices"]), 1)
        ],
    }, {"value": [ids[a] for a in item["answers"]]}, "PartialScore"


def truefalse_item(item):
    return "true-false", {"true_choice": "True", "false_choice": "False"}, {"value": item["answer"]}, "Equivalence"


def matching_item(item):
    qids = [_id() for _ in item["pairs"]]
    answers = [right for _, right in item["pairs"]] + list(item["distractors"])
    value = {qid: right for qid, (_, right) in zip(qids, item["pairs"])}
    return "matching", {
        "answers": answers,
        "questions": [{"id": qid, "item_body": left} for qid, (left, _) in zip(qids, item["pairs"])],
    }, {
        "value": value,
        "edit_data": {
            "matches": [
                {"answer_body": right, "question_id": qid, "question_body": left}
                for qid, (left, right) in zip(qids, item["pairs"])
            ],
            "distractors": list(item["distractors"]),
        },
    }, "PartialDeep"


def essay_item(item):
    grader_note = f"{item['rubric']} Exemplar (full credit): {item['exemplar']}"
    return "essay", {
        "rce": True, "essay": None, "word_count": True, "file_upload": False, "spell_check": True,
        "word_limit_enabled": False,
    }, {"value": grader_note}, "None"


BUILDERS = {
    "choice": choice_item,
    "multi": multi_item,
    "truefalse": truefalse_item,
    "matching": matching_item,
    "essay": essay_item,
}


def add_item(api, quiz_id, position, item):
    slug, interaction_data, scoring_data, algorithm = BUILDERS[item["type"]](item)
    api.new_quiz("POST", f"/quizzes/{quiz_id}/items", {"item": {
        "position": position,
        "points_possible": item["points"],
        "entry_type": "Item",
        "entry": {
            "title": item["title"],
            "item_body": item["prompt"],
            "calculator_type": "none",
            "interaction_type_slug": slug,
            "interaction_data": interaction_data,
            "scoring_data": scoring_data,
            "scoring_algorithm": algorithm,
            "properties": {},
        },
    }})


def existing_titles(api):
    found, page = set(), 1
    while True:
        batch = api.classic("GET", f"/assignments?per_page=100&page={page}")
        if not batch:
            return found
        found |= {a["name"] for a in batch}
        page += 1


def group_id(api):
    for g in api.classic("GET", "/assignment_groups?per_page=100"):
        if g["name"] == ASSIGNMENT_GROUP:
            return g["id"]
    return None


def upload(api, bank, group):
    total = round(sum(i["points"] for i in bank["items"]), 2)
    quiz = api.new_quiz("POST", "/quizzes", {"quiz": {
        "title": bank["title"],
        "instructions": bank["instructions"],
        "points_possible": total,
        "quiz_settings": QUIZ_SETTINGS,
    }})
    quiz_id = quiz["id"]
    for pos, item in enumerate(bank["items"], 1):
        add_item(api, quiz_id, pos, item)
    if group:
        api.classic("PUT", f"/assignments/{quiz_id}", {"assignment": {"assignment_group_id": group}})
    print(f"{bank['title']}: assignment {quiz_id}, {len(bank['items'])} items, {total} pts")
    return quiz_id


def main(base, course):
    api = Canvas(base, course, os.environ.get("CANVAS_TOKEN"))
    taken = existing_titles(api)
    clashes = [b["title"] for b in questions.REASSESSMENTS if b["title"] in taken]
    if clashes:
        sys.exit(f"Already in the course (delete them first to rebuild): {clashes}")
    group = group_id(api)
    ids = [(b["title"], upload(api, b, group)) for b in questions.REASSESSMENTS]
    module = api.classic("POST", "/modules", {"module": {"name": MODULE_NAME, "position": 1, "published": False}})
    for title, quiz_id in ids:
        api.classic("POST", f"/modules/{module['id']}/items", {"module_item": {
            "title": title, "type": "Assignment", "content_id": quiz_id,
        }})
    print(f"Module '{MODULE_NAME}' ({module['id']}) created at position 1 with {len(ids)} items.")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
