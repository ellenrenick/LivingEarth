"""Live course: put the Oct 19 restructure (short_lessons.py) into the Unit 1.3 module.

- creates "Short Lesson A: Trace the Atoms" and "Short Lesson B: Evidence and Revision"
  (4 pts, file upload, same group as Lesson 1, unpublished), due 3 days after their day,
  locked Dec 11;
- renames the Day 6-8 headers and lays the module out: Day 6 = the Day 4 vocab lesson,
  Day 7 = Short A + CFA/review 6.4, Day 8 = Short B + CFA/review 6.5 and 6.6;
- takes the Lesson 5, 6, and 7 assignments out of the module (they stay in the course,
  publish state untouched);
- adds the 15-minute Great Pumpkin Mystery wrap-up to the top of the Day 9 assignment.

Items it doesn't know about (your own pages and headers) keep their place. Safe to run again.

  python3 live_restructure.py 342850 1640554
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import newquiz_upload as N  # noqa: E402
import short_lessons as S  # noqa: E402
import unit13_bank as U  # noqa: E402
from canvas_lessons_upload import get_all  # noqa: E402

LESSON1 = "Lesson 1: The Giant Pumpkin Mystery"
DUE = {"A": "2026-10-23T23:59:00-07:00", "B": "2026-10-24T23:59:00-07:00"}  # planner day + 3
LOCK = "2026-12-11T23:59:00-08:00"
HEADERS = {6: "Day 6 · Vocabulary and SketchNotes (Day 4 lesson)", 7: "Day 7 · Short Lesson A: Trace the Atoms",
           8: "Day 8 · Short Lesson B: Evidence and Revision"}
RETIRED = ("Lesson 6: What's the Evidence?", "Lesson 5: Small Pieces, Big Molecules", "Lesson 7: Solving the Pumpkin Mystery")
WRAP_MARK = "Great Pumpkin Mystery wrap-up"
WRAP = (f'<h2>Start here: {WRAP_MARK} (15 min)</h2>'
        "<ol><li><strong>Re-rank (3 min):</strong> find your Day 1 ranking of where the pumpkin's mass comes from "
        "(soil, water, air, sunlight, fertilizer, the seed) and fill in the “after data” row.</li>"
        "<li><strong>Mystery solved (7 min):</strong> in 3–5 sentences, answer <em>Where does a giant pumpkin's mass come from?</em> "
        "Include where the C, H, and O come from, what the soil adds, what light does, how the atoms become sugar and then proteins, "
        "and whether fertilizer is food.</li>"
        "<li><strong>Share (5 min):</strong> as a class, agree on one answer and copy it into your notebook.</li></ol>"
        "<p>Then work on your assigned CFA reviews and the review stations below.</p>")


def main(course, module_id):
    api = N.Canvas("https://kernhigh.instructure.com", course, "")
    assignments = {a["name"]: a for a in get_all(api, "/assignments")}
    template = assignments[LESSON1]

    new = {}
    for key in ("A", "B"):
        s = S.LESSONS[key]
        name = f"{s['lesson']}: {s['title']}"
        fields = {"name": name, "description": S.student_html(key), "points_possible": U.GRADE_POINTS,
                  "grading_type": template["grading_type"], "submission_types": ["online_upload"],
                  "assignment_group_id": template["assignment_group_id"], "due_at": DUE[key], "lock_at": LOCK}
        if name in assignments:
            a = api.v1("PUT", f"/assignments/{assignments[name]['id']}", {"assignment": fields})
            print(f"Updated: {name}")
        else:
            a = api.v1("POST", "/assignments", {"assignment": {**fields, "published": False}})
            print(f"Created: {name} (unpublished)")
        new[key] = a["id"]

    items = get_all(api, f"/modules/{module_id}/items")

    def header(day):
        return next(it for it in items if it["type"] == "SubHeader" and it["title"].startswith(f"Day {day} "))

    for day, title in HEADERS.items():
        it = header(day)
        if it["title"] != title:
            api.v1("PUT", f"/modules/{module_id}/items/{it['id']}", {"module_item": {"title": title}})
            print(f"Header: {it['title']} -> {title}")
            it["title"] = title

    retired = {assignments[n]["id"] for n in RETIRED if n in assignments}
    for it in list(items):
        if it["type"] == "Assignment" and it.get("content_id") in retired:
            api.v1("DELETE", f"/modules/{module_id}/items/{it['id']}")
            items.remove(it)
            print(f"Removed from module: {it['title']}")

    def asg(aid):
        found = next((it for it in items if it["type"] == "Assignment" and it.get("content_id") == aid), None)
        if found is None:
            found = api.v1("POST", f"/modules/{module_id}/items", {"module_item": {"type": "Assignment", "content_id": aid}})
            items.append(found)
        return found

    cfa = {t[0]: int(next(a["id"] for n, a in assignments.items() if n.startswith(f"Unit 1.3 CFA {t[0]}"))) for t in U.TARGETS}
    rev = {t[0]: int(next(a["id"] for n, a in assignments.items() if n.startswith(f"Unit 1.3 Review {t[0]}"))) for t in U.TARGETS}

    # New layout for Days 6-8; everything else keeps its relative order.
    block = [header(6), header(7), asg(new["A"]), asg(cfa["LS1-6.4"]), asg(rev["LS1-6.4"]),
             header(8), asg(new["B"]), asg(cfa["LS1-6.5"]), asg(rev["LS1-6.5"]), asg(cfa["LS1-6.6"]), asg(rev["LS1-6.6"])]
    ids = {it["id"] for it in block}
    items.sort(key=lambda it: it["position"])
    # Keep whatever sat between the Day 6 header and the Day 7 header (e.g. "Today's Work") right after Day 6.
    start = items.index(next(it for it in items if it["id"] == block[0]["id"]))
    tail = [it for it in items[start + 1:] if it["id"] not in ids]
    stay_with_6 = []
    for it in tail:
        if it["type"] == "SubHeader" and it["title"].startswith("Day "):
            break
        stay_with_6.append(it)
    before = [it for it in items[:start] if it["id"] not in ids]
    after = [it for it in tail if it not in stay_with_6]
    ordered = before + [block[0]] + stay_with_6 + block[1:] + after
    for pos, it in enumerate(ordered, 1):
        if it.get("position") != pos:
            api.v1("PUT", f"/modules/{module_id}/items/{it['id']}", {"module_item": {"position": pos}})
    print(f"Module ordered: {len(ordered)} items")

    day9 = assignments.get("Unit 1.3 Day 9: Interventions and Review")
    if day9 and WRAP_MARK not in (day9["description"] or ""):
        d = day9["description"] or ""
        i = d.find("<hr><h2>Part 1")
        d = d[:i] + "<hr>" + WRAP + "\n" + d[i:] if i >= 0 else WRAP + d
        api.v1("PUT", f"/assignments/{day9['id']}", {"assignment": {"description": d}})
        print("Day 9: added the Great Pumpkin Mystery wrap-up")


if __name__ == "__main__":
    main(*sys.argv[1:3])
