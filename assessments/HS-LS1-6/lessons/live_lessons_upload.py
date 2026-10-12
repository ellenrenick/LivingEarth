"""Put Unit 1.3 into the live Living Earth course with each lesson as an assignment.

The live course (342850) got the unit by course copy, so its CFAs, reviews, and CSA
already exist. This script:
- makes one assignment per lesson day (Days 1-9), set up like the existing
  "Lesson 1: The Giant Pumpkin Mystery" assignment: 4 points, no submission,
  same assignment group, unpublished. The description is the day's student page.
  If a day's page in the live course was edited by hand (newer than the copy),
  that page's body is used instead of the generated one;
- lays out the Unit 1.3 module in the current day order (Oct 9 makeup day,
  no practice test), keeping any items it doesn't know about at the end;
- takes the old lesson pages, the practice test, its review, and the extension
  out of the module (they stay in the course, unpublished).

Nothing is published or deleted. Safe to run again.

  python3 live_lessons_upload.py https://kernhigh.instructure.com 342850 1640554
"""

import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import newquiz_upload as N  # noqa: E402
import unit13_bank as U  # noqa: E402
import unit13_reviews as R  # noqa: E402
import unit13_lessons as L  # noqa: E402
from canvas_lessons_upload import get_all, order_module  # noqa: E402

LESSON1 = "Lesson 1: The Giant Pumpkin Mystery"
# Hand-edited page in the live course to use for a day, by page url.
HAND_EDITED = {2: "lesson-2-what-are-living-things-made-of"}
MAKEUP_HEADER_PREFIX = "💥Today's Work💥"


def assignment_name(d):
    if d["lesson"].startswith("Lesson"):
        return f"{d['lesson']}: {d['title']}"
    return f"Unit 1.3 Day {d['day']}: {d['title']}"


def main(base, course, module_id):
    api = N.Canvas(base, course, "")
    assignments = {a["name"]: a for a in get_all(api, "/assignments")}
    template = assignments[LESSON1]
    quizzes = {q["title"]: int(q["id"]) for q in api.nq("GET", "/quizzes?per_page=50")}

    lesson_ids = {1: template["id"]}
    for d in L.DAYS:
        if d["day"] in (1, 10):  # Day 1 exists; Day 10 is the CSA itself
            continue
        body = L.student_html(d)
        if d["day"] in HAND_EDITED:
            body = api.v1("GET", f"/pages/{urllib.parse.quote(HAND_EDITED[d['day']])}")["body"]
        name = assignment_name(d)
        fields = {"name": name, "description": body, "points_possible": U.GRADE_POINTS,
                  "grading_type": template["grading_type"], "submission_types": template["submission_types"],
                  "assignment_group_id": template["assignment_group_id"]}
        if name in assignments:
            a = api.v1("PUT", f"/assignments/{assignments[name]['id']}", {"assignment": fields})
            print(f"Updated: {name}")
        else:
            a = api.v1("POST", "/assignments", {"assignment": {**fields, "published": False}})
            print(f"Created: {name}")
        lesson_ids[d["day"]] = a["id"]

    # Module layout.
    items = get_all(api, f"/modules/{module_id}/items")
    makeup = next((it for it in items if it["type"] == "SubHeader" and it["title"].startswith(MAKEUP_HEADER_PREFIX)), None)
    day10_page = next((it for it in items if it["type"] == "Page" and "day-10" in (it.get("page_url") or "")), None)
    retired = {quizzes.get(f"{U.UNIT} Practice Test: {U.UNIT_NAME} ({U.STANDARD})"),
               assignments.get(R.PRACTICE_REVIEW_TITLE, {}).get("id"), assignments.get(R.EXTENSION_TITLE, {}).get("id")}
    for it in items:
        old_header = it["type"] == "SubHeader" and it["title"].startswith("Day ")
        old_page = it["type"] == "Page" and it is not day10_page
        if old_header or old_page or (it["type"] in ("Assignment", "Quiz") and it.get("content_id") in retired):
            api.v1("DELETE", f"/modules/{module_id}/items/{it['id']}")
            print(f"Removed from module: {it['title']}")

    cfa_title = {t[0]: f"{U.UNIT} CFA {t[0]}: {t[1]}" for t in U.TARGETS}
    wanted = []
    for d in L.DAYS:
        wanted.append(("SubHeader", f"Day {d['day']} · {d['title']}"))
        if d["day"] in lesson_ids:
            wanted.append(("Assignment", lesson_ids[d["day"]]))
        if d["cfa"]:
            wanted.append(("Assignment", quizzes[cfa_title[d["cfa"]]]))
            wanted.append(("Assignment", assignments[R.REVIEW_TITLE[d["cfa"]]]["id"]))
        if d["day"] == 10:
            if day10_page:
                wanted.append(("Page", day10_page["page_url"], ""))
            wanted.append(("Assignment", quizzes[f"{U.UNIT} CSA: {U.UNIT_NAME} ({U.STANDARD})"]))
        if d["day"] == 1 and makeup:  # Fri Oct 9 makeup day sits between Day 1 and Day 2
            wanted.append(("SubHeader", makeup["title"]))
    n, rest = order_module(api, module_id, wanted)
    print(f"Unit module ordered: {n} items by day, {rest} other items after them")


if __name__ == "__main__":
    main(*sys.argv[1:4])
