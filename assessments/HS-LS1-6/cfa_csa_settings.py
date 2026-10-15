"""Apply the CFA/CSA New Quiz settings to every CFA and CSA in a course.

Settings (newquiz_upload.CFA_CSA_SETTINGS): shuffle questions, shuffle answers, and
hide results with every "show" option under it off. A quiz counts as a CFA or CSA
when its title says CFA or CSA, or it is in the "Assessment" assignment group;
practice tests, bootcamp, and lab-safety tests are left alone.

  python3 cfa_csa_settings.py https://kernhigh.instructure.com 342850 [--dry-run]
"""

import re
import sys

import newquiz_upload as N

# CSAs whose titles don't say CSA (and may sit outside the Assessment group in the sandbox).
CSA_TITLES = {"Unit 1.1: From Cells to Organisms", "Cell Energy & Carbon HS-LS2-5"}
SKIP = re.compile(r"practice|bootcamp|lab safety|^OLD", re.I)


def targets(api):
    groups = {g["id"]: g["name"] for g in api.v1("GET", "/assignment_groups?per_page=100")}
    out, page = [], 1
    while True:
        r = api.nq("GET", f"/quizzes?per_page=50&page={page}")
        for q in r:
            group = groups.get(int(q.get("assignment_group_id") or 0), "")
            if SKIP.search(q["title"]):
                continue
            if re.search(r"\bCF?A\b|\bCSA\b", q["title"]) or group.lower().startswith("assessment") \
                    or q["title"].strip() in CSA_TITLES:
                out.append(q)
        if len(r) < 50:
            return out
        page += 1


def main(base, course, *flags):
    api = N.Canvas(base, course, "")
    for q in targets(api):
        if "--dry-run" in flags:
            print("would set:", q["id"], q["title"])
            continue
        r = api.nq("PATCH", f"/quizzes/{q['id']}", {"quiz": {"quiz_settings": N.CFA_CSA_SETTINGS}})
        s = r["quiz_settings"]
        ok = s["shuffle_questions"] and s["shuffle_answers"] and s["result_view_settings"].get("result_view_restricted")
        print("set" if ok else "CHECK", q["id"], q["title"])


if __name__ == "__main__":
    main(*sys.argv[1:])
