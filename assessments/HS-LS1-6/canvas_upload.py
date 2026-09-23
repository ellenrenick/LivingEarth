"""Create the HS-LS1-6 quizzes, review page, and lesson handout pages in a Canvas course.

Uses the Canvas REST API (Classic Quizzes), so no file upload is needed.
Everything is created unpublished. Running it again creates duplicates, so use
--only to create just the parts you don't have yet.

Usage:
  CANVAS_TOKEN=... python3 canvas_upload.py https://kernhigh.instructure.com 330720
  CANVAS_TOKEN=... python3 canvas_upload.py https://kernhigh.instructure.com 330720 --only lessons
  python3 canvas_upload.py https://kernhigh.instructure.com 330720 --dry-run

--only takes a comma-separated list of: quizzes, review, lessons (default: all three).
--dry-run lists what would be created without contacting Canvas.
"""

import json
import os
import re
import ssl
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import argparse

import build
import practice_questions
import questions

HERE = Path(__file__).parent
HANDOUTS = HERE.parent.parent / "lessons" / "HS-LS1-6" / "handouts"
PARTS = ("quizzes", "review", "lessons")
CA = "/root/.ccr/ca-bundle.crt"
CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()

# Per-bank quiz settings.
SETTINGS = {
    questions: {"quiz_type": "assignment", "allowed_attempts": 1},
    practice_questions: {"quiz_type": "practice_quiz", "allowed_attempts": -1, "time_limit": 20},
}


class Canvas:
    def __init__(self, base, course, token):
        self.root = f"{base.rstrip('/')}/api/v1/courses/{course}"
        self.token = token

    def call(self, method, path, body=None):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(self.root + path, data=data, method=method)
        req.add_header("Authorization", f"Bearer {self.token}")
        req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req, context=CTX) as r:
            return json.loads(r.read() or "null")


def header(title, html):
    return {"question_name": title, "question_type": "text_only_question", "question_text": html}


def matching(m):
    return {
        "question_name": m["title"],
        "question_type": "matching_question",
        "question_text": m["prompt"],
        "points_possible": m["points"],
        "answers": [
            {"answer_match_left": term, "answer_match_right": definition, "answer_weight": 100}
            for term, definition in m["pairs"]
        ],
        "matching_answer_incorrect_matches": "\n".join(m["distractors"]),
    }


def multiple_choice(n, item):
    return {
        "question_name": f"MC {n} (DOK {item['dok']})",
        "question_type": "multiple_choice_question",
        "question_text": item["prompt"],
        "points_possible": build.MC_POINTS,
        "neutral_comments_html": f"<p>{item['feedback']}</p>",
        "answers": [
            {"answer_html": choice, "answer_weight": 100 if i == item["answer"] else 0}
            for i, choice in enumerate(item["choices"])
        ],
    }


def essay(n, item):
    rows = "".join(
        f"<tr><td><strong>{s}</strong></td><td>{lvl}</td><td>{d}</td></tr>" for s, lvl, d in item["rubric"]
    )
    notes = "".join(f"<li>{x}</li>" for x in item["grading_notes"])
    fb = (
        "<p><strong>4-point scoring rubric</strong></p>"
        '<table border="1" cellpadding="4"><tr><th>Score</th><th>Level</th><th>Descriptor</th></tr>'
        f"{rows}<tr><td><strong>0</strong></td><td>No response</td><td>Blank or off-topic.</td></tr></table>"
        f"<p><strong>Grading notes</strong></p><ul>{notes}</ul>"
        f"<p><strong>Exemplar (score 4):</strong> {item['exemplar']}</p>"
    )
    return {
        "question_name": f"Free response {n} (DOK {item['dok']})",
        "question_type": "essay_question",
        "question_text": item["prompt"],
        "points_possible": item["points"],
        "neutral_comments_html": fb,
    }


def upload_quiz(api, bank):
    mc = build.shuffled_mc(bank)
    quiz = api.call("POST", "/quizzes", {"quiz": {
        "title": bank.TITLE,
        "description": getattr(bank, "DESCRIPTION", "") or f"<p>Suggested time: {bank.TIME_MINUTES} minutes.</p>",
        "shuffle_answers": False,
        "published": False,
        **SETTINGS[bank],
    }})
    qs = [header(bank.MATCHING["title"], "<h3>" + bank.MATCHING["title"] + "</h3>"), matching(bank.MATCHING),
          header("Part 2", "<h3>Part 2: Multiple Choice</h3>")]
    qs += [multiple_choice(i, it) for i, it in enumerate(mc, 1)]
    qs += [header("Part 3", "<h3>Part 3: Free Response</h3>")]
    qs += [essay(i, it) for i, it in enumerate(bank.FREE_RESPONSE, 1)]
    for pos, q in enumerate(qs, 1):
        api.call("POST", f"/quizzes/{quiz['id']}/questions", {"question": {**q, "position": pos}})
    quiz = api.call("GET", f"/quizzes/{quiz['id']}")
    print(f"Quiz: {quiz['title']} ({quiz['points_possible']} pts, {quiz['question_count']} items) {quiz['html_url']}")


def page_body(path):
    """Return the part of an HTML file between <body> and </body>, without comments."""
    src = path.read_text(encoding="utf-8")
    body = re.search(r"<body>(.*)</body>", src, re.S).group(1)
    return re.sub(r"<!--.*?-->", "", body, flags=re.S).strip()


def page_title(path):
    return re.search(r"<title>(.*?)</title>", path.read_text(encoding="utf-8"), re.S).group(1).strip()


def upload_page(api, title, body):
    if api is None:
        print(f"Would create page: {title} ({len(body):,} characters)")
        return
    page = api.call("POST", "/pages", {"wiki_page": {"title": title, "body": body, "published": False}})
    print(f"Page: {page['title']} {page['html_url']}")


def upload_review(api):
    upload_page(api, "HS-LS1-6 Review: From Sugar to Building Blocks", page_body(HERE / "HS-LS1-6_review.html"))


def upload_lessons(api):
    # lesson_1_handout.html ... lesson_7_handout.html, created in lesson order.
    for path in sorted(HANDOUTS.glob("lesson_*_handout.html")):
        upload_page(api, f"HS-LS1-6 {page_title(path)}", page_body(path))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Create the HS-LS1-6 materials in a Canvas course.")
    ap.add_argument("base", help="Canvas URL, e.g. https://kernhigh.instructure.com")
    ap.add_argument("course", help="Canvas course id")
    ap.add_argument("--only", default=",".join(PARTS), help="comma-separated: quizzes, review, lessons")
    ap.add_argument("--dry-run", action="store_true", help="list what would be created without contacting Canvas")
    args = ap.parse_args()
    parts = [p.strip() for p in args.only.split(",") if p.strip()]
    bad = [p for p in parts if p not in PARTS]
    if bad:
        sys.exit(f"Unknown part(s) for --only: {', '.join(bad)}. Choose from: {', '.join(PARTS)}")

    api = None if args.dry_run else Canvas(args.base, args.course, os.environ["CANVAS_TOKEN"])
    if "quizzes" in parts:
        for bank in (questions, practice_questions):
            if api is None:
                print(f"Would create quiz: {bank.TITLE}")
            else:
                upload_quiz(api, bank)
    if "review" in parts:
        upload_review(api)
    if "lessons" in parts:
        upload_lessons(api)
