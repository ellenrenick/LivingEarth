"""Requests that write the Unit 1.3 days into the LE Planner 2026-2027 October calendar.

October table g3f07a7a478a_0_97 (5 columns, Mon-Fri). Unit 1.3 runs Thu Oct 8 to
Thu Oct 22 (Fri Oct 9 is a makeup work day); Unit 2.1 starts Fri Oct 23. Oct 14 and Oct 16 are sub days. Each cell gets the day's lesson (linked
to its slides), its teacher page, and its CFA or test (linked to Canvas). Text
goes at the start of the cell, so anything already there stays after it.

  python3 planner_requests.py
"""

import json

import unit13_lessons as L

TABLE = "g3f07a7a478a_0_97"
CANVAS = "https://kernhigh.instructure.com/courses/330720"
# Unit 1.3 day -> (row, column) in the October table
CELLS = {1: (2, 3), 2: (4, 0), 3: (4, 1), 4: (4, 2), 5: (4, 3), 6: (4, 4),
         7: (6, 0), 8: (6, 1), 9: (6, 2), 10: (6, 3)}
MAKEUP = (2, 4)  # Fri Oct 9
MAKEUP_TEXT = "Makeup work day (no Unit 1.3 lesson)"
# Oct 14 and Oct 16 are sub days: the notebook-only vocabulary day and the evidence jigsaw.
SHORT = {1: "Phenomena + CER intro: The Giant Pumpkin Mystery", 5: "From Sugar to Amino Acids (bead lab)",
         4: "SUB DAY: Vocab (Frayer) + SketchNotes", 6: "SUB DAY: What's the Evidence? (jigsaw)",
         8: "Solving the Pumpkin Mystery (finish CER)", 9: "Interventions: assigned CFA reviews + review stations",
         10: "HS-LS1-6 Sugar to Structures Summative assessment (CSA)"}
CFA_IDS = {"LS1-6.1": 13882514, "LS1-6.2": 13882515, "LS1-6.3": 13882517,
           "LS1-6.4": 13882519, "LS1-6.5": 13882520, "LS1-6.6": 13882521}
CSA = 13882523


def lines(d):
    n = d["day"]
    slug = "teacher-" + {1: "unit-1-dot-3-day-1-the-giant-pumpkin-mystery"}.get(n, "")
    out = [(f"Day {n}: {SHORT.get(n, d['title'])}", d["slides"][1])]
    out.append(("Lesson plan (Canvas)", None))  # url filled in by caller
    if d["cfa"]:
        out.append((f"CFA {d['cfa']}", f"{CANVAS}/assignments/{CFA_IDS[d['cfa']]}"))
    if n == 9:
        out.append(("CFA reviews (Mastery Paths)", f"{CANVAS}/modules"))
    if n == 10:
        out.append(("Unit 1.3 CSA", f"{CANVAS}/assignments/{CSA}"))
    return out


def requests(teacher_slugs):
    loc = {"rowIndex": MAKEUP[0], "columnIndex": MAKEUP[1]}
    reqs = [{"insertText": {"objectId": TABLE, "cellLocation": loc, "insertionIndex": 0, "text": MAKEUP_TEXT + "\n"}},
            {"updateTextStyle": {"objectId": TABLE, "cellLocation": loc,
             "textRange": {"type": "FIXED_RANGE", "startIndex": 0, "endIndex": len(MAKEUP_TEXT) + 1},
             "style": {"bold": True, "fontSize": {"magnitude": 10, "unit": "PT"}, "link": None},
             "fields": "bold,fontSize,link"}}]
    for d in L.DAYS:
        r, c = CELLS[d["day"]]
        loc = {"rowIndex": r, "columnIndex": c}
        ls = lines(d)
        ls[1] = (ls[1][0], f"{CANVAS}/pages/{teacher_slugs[d['day']]}")
        text = "".join(t + "\n" for t, _ in ls)
        reqs.append({"insertText": {"objectId": TABLE, "cellLocation": loc, "insertionIndex": 0, "text": text}})
        reqs.append({"updateTextStyle": {"objectId": TABLE, "cellLocation": loc,
                     "textRange": {"type": "FIXED_RANGE", "startIndex": 0, "endIndex": len(text)},
                     "style": {"bold": True, "fontSize": {"magnitude": 10, "unit": "PT"}},
                     "fields": "bold,fontSize"}})
        i = 0
        for t, url in ls:
            if url:
                reqs.append({"updateTextStyle": {"objectId": TABLE, "cellLocation": loc,
                             "textRange": {"type": "FIXED_RANGE", "startIndex": i, "endIndex": i + len(t)},
                             "style": {"link": {"url": url}}, "fields": "link"}})
            i += len(t) + 1
    return reqs


if __name__ == "__main__":
    slugs = {d["day"]: "teacher-" + L.page_title(d).lower() for d in L.DAYS}
    import re
    slugs = {k: re.sub(r"[^a-z0-9]+", "-", v.replace(".", " dot ").replace("'", "")).strip("-") for k, v in slugs.items()}
    print(json.dumps(requests(slugs), ensure_ascii=False))
