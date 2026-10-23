"""One-off: refresh the eight student and teacher pages and the Lesson 1 assignment after the labs-first rework."""
import json, os
import canvas_upload as U, lessons as L
base, course = "https://kernhigh.instructure.com", "330720"
cv = U.Canvas(base, course, os.environ.get("CANVAS_TOKEN", ""))
ids = json.loads(U.IDS_FILE.read_text())
root = f"{base}/courses/{course}/pages"
for day in range(1, 9):
    d = L.DAYS[day]
    sp = cv.v1("GET", f"/pages/{ids['pages'][f'student{day}']}")
    cv.v1("PUT", f"/pages/{ids['pages'][f'student{day}']}", {"wiki_page": {"body": L.student_html(day, d["title"], d["focus"], d["targets"], d["notebook"], d["parts"])}})
    t = L.TEACHER[day]
    cv.v1("PUT", f"/pages/{ids['pages'][f'teacher{day}']}", {"wiki_page": {"body": L.teacher_html(day, d["title"], d["targets"], f"{root}/{sp['url']}", t["glance"], t["materials"], t["agenda"], t["notes"], t["key"], t["supports"])}})
    print("updated day", day)
cv.v1("PUT", f"/assignments/{ids['extra_assignments']['lesson1']}", {"assignment": {"description": L.LESSON1_ASSIGN[1]}})
print("updated lesson1 assignment")
