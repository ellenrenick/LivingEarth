"""Build the Unit 3.1 student pages, teacher pages, extra assignments, and modules in Canvas.

Run canvas_upload.py first (it builds the CFAs, CSA, reviews, and Mastery Path rules and writes
canvas_ids.json). This script then replaces that script's simple module with a full day-by-day
module that has the student pages and extra assignments, and adds an unpublished teacher module.

Usage:
  python3 canvas_lessons.py https://kernhigh.instructure.com 330720 --dry-run
  python3 canvas_lessons.py https://kernhigh.instructure.com 330720
  python3 canvas_lessons.py https://kernhigh.instructure.com 330720 --cleanup   # removes pages, extra assignments, teacher module

Everything is unpublished. The Enrichment assignment is also hidden from all students until you
assign it to specific students.
"""

import json
import os
import sys

import canvas_upload as U
import lessons as L
import questions as Q

IDS = U.IDS_FILE
SUBMIT = {"upload": ["online_upload"], "text": ["online_text_entry", "online_upload"], "none": ["none"]}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if len(args) != 2:
        raise SystemExit(__doc__)
    base, course = args
    cv = U.Canvas(base, course, os.environ.get("CANVAS_TOKEN", ""), dry="--dry-run" in flags)
    ids = json.loads(IDS.read_text())

    if "--cleanup" in flags:
        for pid in ids.get("pages", {}).values():
            cv.v1("DELETE", f"/pages/{pid}")
        for aid in ids.get("extra_assignments", {}).values():
            cv.v1("DELETE", f"/assignments/{aid}")
        if ids.get("teacher_module"):
            cv.v1("DELETE", f"/modules/{ids['teacher_module']}")
        for k in ("pages", "extra_assignments", "teacher_module"):
            ids.pop(k, None)
        IDS.write_text(json.dumps(ids, indent=1))
        print("Removed pages, extra assignments, and the teacher module.")
        return

    group = next((g["id"] for g in cv.v1("GET", "/assignment_groups") if g["name"] == "Assignments"), 0) if not cv.dry else 0
    root = f"{base.rstrip('/')}/courses/{course}/pages"

    # ---- pages
    student, teacher = {}, {}
    page_ids = {}
    for day, d in L.DAYS.items():
        body = L.student_html(day, d["title"], d["focus"], d["targets"], d["notebook"], d["parts"])
        p = cv.v1("POST", "/pages", {"wiki_page": {"title": f"Unit 3.1 Day {day}: {d['title']}", "body": body,
                                                 "published": False, "editing_roles": "teachers"}})
        student[day] = p.get("url", "")
        page_ids[f"student{day}"] = p.get("page_id", 0)
        print("Student page", day, student[day])
    for day, d in L.DAYS.items():
        t = L.TEACHER[day]
        body = L.teacher_html(day, d["title"], d["targets"], f"{root}/{student[day]}", t["glance"], t["materials"],
                              t["agenda"], t["notes"], t["key"], t["supports"])
        p = cv.v1("POST", "/pages", {"wiki_page": {"title": f"TEACHER: Unit 3.1 Day {day}: {d['title']}", "body": body,
                                                 "published": False, "editing_roles": "teachers"}})
        teacher[day] = p.get("url", "")
        page_ids[f"teacher{day}"] = p.get("page_id", 0)
        print("Teacher page", day, teacher[day])

    # ---- extra assignments
    def assignment(key, spec, submit, hidden=False):
        name, desc = spec
        a = cv.v1("POST", "/assignments", {"assignment": {
            "name": name, "description": desc, "points_possible": U.ASSIGNMENT_POINTS, "grading_type": "points",
            "submission_types": SUBMIT[submit], "assignment_group_id": group, "published": False}})
        if hidden:
            cv.v1("PUT", f"/assignments/{a['id']}", {"assignment": {"only_visible_to_overrides": True}})
        print("Assignment", key, a["id"])
        return a["id"]

    extra = {
        "lesson1": assignment("lesson1", L.LESSON1_ASSIGN, "none"),
        "lesson4": assignment("lesson4", L.LESSON4_ASSIGN, "upload"),
        "cer": assignment("cer", L.CER_ASSIGN, "text"),
        "enrichment": assignment("enrichment", L.ENRICH, "text", hidden=True),
    }

    # ---- student module (replaces the simple one made by canvas_upload.py)
    if ids.get("module") and not cv.dry:
        cv.v1("DELETE", f"/modules/{ids['module']}")
    mod = cv.v1("POST", "/modules", {"module": {"name": U.MODULE_NAME}})
    cfa, rev = ids["cfa"], ids["review"]

    def item(**kw):
        cv.v1("POST", f"/modules/{mod['id']}/items", {"module_item": kw})

    def sub(day):
        item(title=f"Day {day} · {L.DAYS[day]['title']}", type="SubHeader")

    def page(day):
        item(title=f"Unit 3.1 Day {day}: {L.DAYS[day]['title']}", type="Page", page_url=student[day])

    def asg(aid):
        item(type="Assignment", content_id=aid)

    plan = {1: [extra["lesson1"]],
            2: [cfa["ESS1-5.1"], rev["ESS1-5.1"]],
            3: [cfa["ESS1-5.2"], rev["ESS1-5.2"]],
            4: [extra["lesson4"]],
            5: [cfa["ESS1-5.3"], rev["ESS1-5.3"]],
            6: [cfa["ESS1-6.1"], rev["ESS1-6.1"], extra["cer"], cfa["ESS1-5.4"], rev["ESS1-5.4"]],
            7: [extra["enrichment"]],
            8: [ids["csa"]]}
    for day in L.DAYS:
        sub(day)
        page(day)
        for aid in plan[day]:
            asg(aid)

    # ---- teacher module
    tmod = cv.v1("POST", "/modules", {"module": {"name": "Unit 3.1 TEACHER PAGES (keep unpublished)"}})
    for day in L.DAYS:
        cv.v1("POST", f"/modules/{tmod['id']}/items", {"module_item": {
            "title": f"TEACHER: Unit 3.1 Day {day}: {L.DAYS[day]['title']}", "type": "Page", "page_url": teacher[day]}})

    if not cv.dry:
        ids.update(module=mod["id"], teacher_module=tmod["id"], pages=page_ids, extra_assignments=extra)
        ids["assignments"] = sorted(set(ids["assignments"]) | set(extra.values()))
        IDS.write_text(json.dumps(ids, indent=1))
    print("Done." if not cv.dry else "Dry run only.")


if __name__ == "__main__":
    main()
