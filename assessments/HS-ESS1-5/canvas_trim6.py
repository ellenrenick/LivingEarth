"""One-off: remove the ESS1-6 CFAs/reviews from the sandbox and refresh the page bodies that mention them."""
import json, os
import canvas_upload as U, lessons as L
base, course = "https://kernhigh.instructure.com", "330720"
cv = U.Canvas(base, course, os.environ.get("CANVAS_TOKEN", ""))
ids = json.loads(U.IDS_FILE.read_text())
for k in ("cfa", "review"):
    for code in [c for c in ids[k] if c.startswith("ESS1-6")]:
        cv.delete_quiet(f"/assignments/{ids[k].pop(code)}")
        print("deleted", k, code)
ids["assignments"] = [a for a in ids.get("assignments", []) if a in set(ids["cfa"].values()) | set(ids["review"].values()) | {ids["csa"]} | set(ids["extra_assignments"].values())]
root = f"{base}/courses/{course}/pages"
for day in (3, 4, 6, 7):
    d = L.DAYS[day]
    sp = cv.v1("GET", f"/pages/{ids['pages'][f'student{day}']}")
    cv.v1("PUT", f"/pages/{ids['pages'][f'student{day}']}", {"wiki_page": {"body": L.student_html(day, d["title"], d["focus"], d["targets"], d["notebook"], d["parts"])}})
    t = L.TEACHER[day]
    cv.v1("PUT", f"/pages/{ids['pages'][f'teacher{day}']}", {"wiki_page": {"body": L.teacher_html(day, d["title"], d["targets"], f"{root}/{sp['url']}", t["glance"], t["materials"], t["agenda"], t["notes"], t["key"], t["supports"])}})
    print("updated day", day)
U.IDS_FILE.write_text(json.dumps(ids, indent=1))
