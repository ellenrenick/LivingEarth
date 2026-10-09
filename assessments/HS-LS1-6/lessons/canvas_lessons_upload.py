"""Put the Unit 1.3 lesson pages into Canvas and lay out the module day by day.

- Creates (or updates) one student page and one teacher page per day, unpublished.
- Teacher pages go in their own module, "Unit 1.3 TEACHER PAGES (keep unpublished)".
- The Unit 1.3 module is reordered: for each day, a "Day N" header, the student
  page, then that day's assignments (CFA and its review, the practice test with
  its review and extension, or the CSA).

Run after newquiz_upload.py and mastery_paths_upload.py. Safe to run again.

  CANVAS_TOKEN=... python3 canvas_lessons_upload.py https://kernhigh.instructure.com 330720 1634113
"""

import os
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import newquiz_upload as N  # noqa: E402
import unit13_bank as U  # noqa: E402
import unit13_reviews as R  # noqa: E402
import unit13_lessons as L  # noqa: E402

TEACHER_MODULE = "Unit 1.3 TEACHER PAGES (keep unpublished)"
LESSON1_ASSIGNMENT = "Lesson 1: The Giant Pumpkin Mystery"


def get_all(api, path):
    out, page = [], 1
    sep = "&" if "?" in path else "?"
    while True:
        batch = api.v1("GET", f"{path}{sep}per_page=100&page={page}")
        if not batch:
            return out
        out += batch
        page += 1


def upsert_page(api, pages, title, body):
    if title in pages:
        url = pages[title]["url"]
        page = api.v1("PUT", f"/pages/{urllib.parse.quote(url)}", {"wiki_page": {"body": body}})
    else:
        page = api.v1("POST", "/pages", {"wiki_page": {"title": title, "body": body, "published": False}})
        pages[title] = page
    return page


def ensure_module(api, name, position=None):
    mods = get_all(api, "/modules")
    m = next((m for m in mods if m["name"] == name), None)
    if m is None:
        body = {"module": {"name": name, "published": False}}
        if position:
            body["module"]["position"] = position
        m = api.v1("POST", "/modules", body)
    return m


def order_module(api, module_id, wanted):
    """wanted: list of ("SubHeader", title) | ("Page", page_url, title) | ("Assignment", id).
    Creates any missing items, then sets positions in order. Other items keep their place at the end."""
    items = get_all(api, f"/modules/{module_id}/items")

    def find(w):
        for it in items:
            if w[0] == "SubHeader" and it["type"] == "SubHeader" and it["title"] == w[1]:
                return it
            if w[0] == "Page" and it["type"] == "Page" and it.get("page_url") == w[1]:
                return it
            if w[0] == "Assignment" and it["type"] == "Assignment" and it.get("content_id") == w[1]:
                return it
        return None

    ordered = []
    for w in wanted:
        it = find(w)
        if it is None:
            body = {"type": w[0]}
            if w[0] == "SubHeader":
                body["title"] = w[1]
            elif w[0] == "Page":
                body["page_url"] = w[1]
            else:
                body["content_id"] = w[1]
            it = api.v1("POST", f"/modules/{module_id}/items", {"module_item": body})
            items.append(it)
        ordered.append(it)
    rest = [it for it in items if it["id"] not in {o["id"] for o in ordered}]
    for pos, it in enumerate(ordered + rest, 1):
        api.v1("PUT", f"/modules/{module_id}/items/{it['id']}", {"module_item": {"position": pos}})
    return len(ordered), len(rest)


def main(base, course, module_id):
    api = N.Canvas(base, course, os.environ.get("CANVAS_TOKEN", ""))
    pages = {p["title"]: p for p in get_all(api, "/pages")}
    assignments = {a["name"]: a["id"] for a in get_all(api, "/assignments")}
    quizzes = {q["title"]: int(q["id"]) for q in api.nq("GET", "/quizzes?per_page=50")}

    student, teacher = {}, {}
    for d in L.DAYS:
        title = L.page_title(d)
        student[d["day"]] = upsert_page(api, pages, title, L.student_html(d))
    for d in L.DAYS:
        surl = f"{base.rstrip('/')}/courses/{course}/pages/{student[d['day']]['url']}"
        teacher[d["day"]] = upsert_page(api, pages, "TEACHER: " + L.page_title(d), L.teacher_html(d, surl))
    print(f"Pages: {len(student)} student, {len(teacher)} teacher")

    # Teacher module (unpublished), right after the unit module.
    unit = api.v1("GET", f"/modules/{module_id}")
    tmod = ensure_module(api, TEACHER_MODULE, position=unit["position"] + 1)
    order_module(api, tmod["id"], [("Page", teacher[d["day"]]["url"], "") for d in L.DAYS])

    # Unit module, day by day.
    cfa_title = {t[0]: f"{U.UNIT} CFA {t[0]}: {t[1]}" for t in U.TARGETS}
    wanted = []
    for d in L.DAYS:
        wanted.append(("SubHeader", f"Day {d['day']} · {d['title']}"))
        wanted.append(("Page", student[d["day"]]["url"], ""))
        if d["day"] == 1 and LESSON1_ASSIGNMENT in assignments:
            wanted.append(("Assignment", assignments[LESSON1_ASSIGNMENT]))
        if d["cfa"]:
            wanted.append(("Assignment", quizzes[cfa_title[d["cfa"]]]))
            wanted.append(("Assignment", assignments[R.REVIEW_TITLE[d["cfa"]]]))
        # Day 9 has no practice test (removed Oct 2026): students do the CFA reviews above.
        if d["day"] == 10:
            wanted.append(("Assignment", quizzes[f"{U.UNIT} CSA: {U.UNIT_NAME} ({U.STANDARD})"]))
    # The practice test, its review, and the extension are no longer part of the unit.
    retired = {quizzes.get(f"{U.UNIT} Practice Test: {U.UNIT_NAME} ({U.STANDARD})"),
               assignments.get(R.PRACTICE_REVIEW_TITLE), assignments.get(R.EXTENSION_TITLE)}
    for it in get_all(api, f"/modules/{module_id}/items"):
        if it["type"] in ("Assignment", "Quiz") and it.get("content_id") in retired:
            api.v1("DELETE", f"/modules/{module_id}/items/{it['id']}")
            print(f"Removed from module: {it['title']}")
    n, rest = order_module(api, module_id, wanted)
    print(f"Unit module ordered: {n} items by day, {rest} other items after them")


if __name__ == "__main__":
    main(*sys.argv[1:4])
