"""Live course Unit 1.3: file-upload submissions, due 3 days after the planner day (11:59 pm), lock Dec 11 11:59 pm.

Quizzes (CFAs, CSA) keep their quiz submission; only their dates change. Publish state is never touched.

  python3 live_dates.py 342850 1640554 [first_day]   # only Day >= first_day
"""

import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import newquiz_upload as N  # noqa: E402
from canvas_lessons_upload import get_all  # noqa: E402

# Planner date for each module "Day N" header (Fri Oct 9 makeup day has no unit day).
# Days 6-10 follow the Oct 19 restructure (short_lessons.py): Day 6 = Lesson 4 continued (Mon Oct 19),
# Short Lesson A Tue Oct 20, Short Lesson B Wed Oct 21, review Thu Oct 22, CSA Fri Oct 23.
PLANNER = {1: date(2026, 10, 8), 2: date(2026, 10, 12), 3: date(2026, 10, 13), 4: date(2026, 10, 14),
           5: date(2026, 10, 15), 6: date(2026, 10, 19), 7: date(2026, 10, 20), 8: date(2026, 10, 21),
           9: date(2026, 10, 22), 10: date(2026, 10, 23)}
LOCK = "2026-12-11T23:59:00-08:00"  # PST
DUE_OFFSET = "-07:00"  # PDT through Nov 1


def main(course, module_id, first_day="1"):
    api = N.Canvas("https://kernhigh.instructure.com", course, "")
    day = None
    for it in get_all(api, f"/modules/{module_id}/items"):
        if it["type"] == "SubHeader" and it["title"].startswith("Day "):
            day = int(it["title"].split()[1])
            continue
        if it["type"] != "Assignment" or day is None or day < int(first_day):
            continue
        due = PLANNER[day] + timedelta(days=3)
        body = {"due_at": f"{due.isoformat()}T23:59:00{DUE_OFFSET}", "lock_at": LOCK}
        a = api.v1("GET", f"/assignments/{it['content_id']}")
        if "external_tool" not in a["submission_types"]:
            body["submission_types"] = ["online_upload"]
        a = api.v1("PUT", f"/assignments/{it['content_id']}", {"assignment": body})
        print(f"Day {day}  due {a['due_at']}  lock {a['lock_at']}  {','.join(a['submission_types'])}  "
              f"{'PUBLISHED' if a['published'] else 'unpublished'}  {a['name']}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
