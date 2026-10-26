"""Build Unit 2.2 (HS-LS3-2) in a Canvas course: student pages, CFAs, Mastery Path reviews, the CSA, and teacher pages.

Everything is created unpublished, and the script is safe to rerun (anything whose title exists is updated, not duplicated).
Pattern follows HS-LS1-1/next_year/build.py. Sandbox only: the course id must be 330720.

  python3 canvas.py 330720 decks.json
"""

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent / "HS-LS1-6"))
import cfas as Q  # noqa: E402
import content as U  # noqa: E402
import newquiz_upload as N  # noqa: E402
import reviews as R  # noqa: E402

SANDBOX = "330720"
B_CUTOFF = 0.675  # below a B (fewer than 4 of 5) opens the review
BOX = "background:#eef5fb;border-left:5px solid #1e5fbf;padding:10px 14px;margin:12px 0"
TBOX = "background:#fff4e8;border-left:5px solid #ff8a1f;padding:10px 14px;margin:12px 0"
BANK = "border:1px solid #999;padding:6px"
SLIDES = "https://docs.google.com/presentation/d/{}/edit"


def html_table(head, rows):
    th = "<tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr>"
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table border="1" cellpadding="6" style="border-collapse:collapse"><tbody>{th}{tr}</tbody></table>'


def bank_line(s):
    if not s.get("bank"):
        return ""
    note = f" {s['bank_note']}" if s.get("bank_note") else ""
    return "Word bank: " + " · ".join(U.scramble(s["bank"])) + note


def slides_embed(deck_id, title):
    url = SLIDES.format(deck_id)
    return (f'<h2>Today\'s slides</h2><p><iframe title="{title}" src="{url.replace("/edit", "/embed?start=false&loop=false&delayms=3000")}" '
            'width="960" height="569" style="max-width:100%;border:0" allowfullscreen="allowfullscreen"></iframe></p>'
            f'<p><a href="{url.replace("/edit", "/present")}" target="_blank" rel="noopener">Open the slides full screen</a></p>')


def section_html(s):
    out = "".join(f"<p>{x}</p>" for x in s["body"])
    if s.get("table"):
        out += html_table(*s["table"])
    if s.get("frame"):
        out += (f"<p><strong>In your notebook, under “{s['nb']}”:</strong></p>" if s.get("nb") else "") + "<ul>" + "".join(
            f"<li>{x}</li>" for x in s["frame"]) + "</ul>"
    elif s.get("nb"):
        out += f"<p><em>In your notebook, under “{s['nb']}”.</em></p>"
    if s.get("bank"):
        label, rest = bank_line(s).split(": ", 1)
        out += f'<p style="{BANK}"><strong>{label}:</strong> {rest}</p>'
    return out


def student_html(d, deck_id):
    label = "Learning target" if len(d["targets"]) == 1 else "Learning targets"
    tl = "".join(f"<li><strong>{t}:</strong> {U.TARGET[t][3]}</li>" for t in d["targets"])
    mins = U.minutes(d)
    can = "".join(f"<li>{x}</li>" for x in d["can"])
    out = [f'<div style="{BOX}"><p><strong>Day {d["day"]} · {d["date"]}</strong> · {U.UNIT}: {U.UNIT_NAME} ({U.STANDARD}) · {U.MYSTERY}</p>'
           f"<p><strong>Driving question:</strong> {U.DRIVING_Q}</p><p><strong>Focus question:</strong> {d['focus']}</p>"
           f"<p><strong>{label}:</strong></p><ul>{tl}</ul><p><strong>I can:</strong></p><ul>{can}</ul>"
           + (f"<p>About {mins} minutes. {d['ready']}.</p>" if mins else "") + "</div>",
           slides_embed(deck_id, f"Day {d['day']}: {d['title']}")]
    nb = [s for s in d["sections"] if s.get("nb")]
    if nb:
        rows = "".join(f"<li><strong>{s['nb']}:</strong> {s['nbnote']}</li>" for s in nb)
        out.append(f'<h2>Notebook setup</h2><div style="{BOX}"><p><strong>Before the lesson:</strong> title a new page '
                   f"<strong>Day {d['day']}: {d['title']}</strong> and make a heading for each part, in order:</p><ol>{rows}</ol>"
                   "<p><em>Your notebook is your answer sheet for this lesson.</em></p></div>")
    for n, s in enumerate(d["sections"], 1):
        out.append(f"<hr><h2>Part {n}: {s['title']}</h2>{section_html(s)}")
    if d["cfa"]:
        out.append(f"<hr><h2>Part {len(d['sections']) + 1}: Show what you know: CFA {d['cfa']}</h2>"
                   f"<p>Take <strong>{Q.CFA_TITLE[d['cfa']]}</strong> on Canvas (5 questions), on your own and from memory. "
                   "If you score below a B (fewer than 4 of 5), a review for this target will open for you.</p>")
    out.append("<hr><p><strong>If you were absent:</strong> go through today's slides above, complete the notebook "
               "page, and take any CFA listed on this page.</p>")
    return "\n".join(out)


def teacher_html(d, deck_id):
    mins = U.minutes(d)
    rows = [("2", "Notebook setup: title the page and make the section headings.")] if any(s.get("nb") for s in d["sections"]) else []
    rows += [(str(s["minutes"] + s.get("minutes_frame", 0)) if s.get("minutes") else "", f"<strong>{s['title']}.</strong> {s['teacher']}")
             for s in d["sections"]]
    if d["cfa"]:
        rows.append(("6", f"<strong>CFA {d['cfa']}</strong>, on their own and from memory. Below a B opens the review."))
    total = f" ({mins} minutes)" if mins else ""
    return "\n".join([
        f'<div style="{TBOX}"><p><strong>Teacher page · keep unpublished.</strong> Students never see this page.</p>'
        f"<p><strong>Day {d['day']} · {d['date']}: {d['title']}</strong> · Targets: {', '.join(d['targets'])}"
        + (f" · CFA {d['cfa']}" if d["cfa"] else "") + "</p></div>",
        f'<p><a href="{SLIDES.format(deck_id)}">Slides</a></p>',
        f"<h2>Agenda{total}</h2>{html_table(['Min', 'What happens'], rows)}",
        "<h2>Answer key</h2><ol>" + "".join(f"<li>{k}</li>" for k in d.get("key", [])) + "</ol>",
        "<h2>Notes</h2><ul>" + "".join(f"<li>{n}</li>" for n in d.get("notes", [])) + "</ul>"])


def overview_html(decks):
    rows = [[t[0], t[4], t[3], str(t[2])] for t in U.TARGETS if t[4] == "Priority"]
    days = []
    for d in U.DAYS:
        m = U.minutes(d)
        days.append([f"Day {d['day']} · {d['date']}", f'<a href="{SLIDES.format(decks[str(d["day"])])}">{d["title"]}</a>',
                     ", ".join(d["targets"]), f"CFA {d['cfa']}" if d["cfa"] else "none", f"{m} min" if m else "full period"])
    return (f"<h2>{U.UNIT}: {U.UNIT_NAME} ({U.STANDARD}) · Nov 9 to Dec 1, 2026 (11 class days)</h2>"
            "<p><em>Built from the department workbook (LS3-2.1 to 2.5 priority, LS3-3.1 to 3.3 supporting) in the Unit 2.1 "
            "format: a daily deck, about 30 minutes of student work including the CFA, and a Mastery Path review below a B. "
            "Nov 11 (Veterans Day) and Nov 23 to 27 (Fall Break) are off, so the workbook's 15 days are compressed to 11.</em></p>"
            f"<h3>Anchoring phenomenon</h3><p>{U.DRIVING_Q}</p><h3>Learning targets</h3>"
            + html_table(["Target", "Tier", "I can", "DOK"], rows)
            + "<h3>Day by day</h3>" + html_table(["Day", "Lesson", "Targets", "CFA", "Time"], days)
            + "<p>CFAs: 5 questions each, below a B (fewer than 4 of 5) opens that target's review (Mastery Path). "
              "The CSA has 17 questions (26 raw points, graded out of 4).</p>")


def get_all(api, path):
    out, page = [], 1
    while True:
        sep = "&" if "?" in path else "?"
        batch = api.v1("GET", f"{path}{sep}per_page=100&page={page}")
        if not batch:
            return out
        out += batch
        page += 1


# (day label, old title, date text) -> (day label, new title, date text)
RENAMED_DAYS = [(("Day 9", "Catch-Up Day: Reviews and Make-Up Work", "Fri Nov 20 (2-hour early out)"),
                 ("Day 9", "Back to the Puppies and Make-Up Work", "Fri Nov 20 (2-hour early out)")),
                (("Day 10", "Defend Your Claim and Back to the Puppies", "Mon Nov 30"),
                 ("Day 10", "Review Day: Prepare for the CSA", "Mon Nov 30"))]


def canvas(course, decks_file):
    assert str(course) == SANDBOX, "sandbox course only"
    decks = json.loads(Path(decks_file).read_text())
    api = N.Canvas("https://kernhigh.instructure.com", course, "")
    group = next(g for g in api.v1("GET", "/assignment_groups") if g["name"] == "Assignments")["id"]
    mods = {m["name"]: m for m in get_all(api, "/modules")}

    def module(name):
        if name not in mods:
            mods[name] = api.v1("POST", "/modules", {"module": {"name": name, "published": False}})
        return mods[name]["id"]

    student_mod = module(f"{U.UNIT}: {U.UNIT_NAME} {U.STANDARD}")
    teacher_mod = module(f"{U.UNIT} TEACHER PAGES (keep unpublished)")
    asg = {a["name"]: a for a in get_all(api, "/assignments")}
    quizzes = {q["title"]: q for q in api.nq("GET", "/quizzes?per_page=100")}
    pages = {p["title"]: p for p in get_all(api, "/pages")}

    def assignment(name, html, points=4, review=False):
        body = {"name": name, "description": html, "points_possible": points, "assignment_group_id": group,
                "submission_types": ["online_text_entry", "online_upload"], "published": False}
        if review:
            body.update(grading_type="pass_fail", only_visible_to_overrides=True)
        if name in asg:
            return api.v1("PUT", f"/assignments/{asg[name]['id']}", {"assignment": body})
        asg[name] = api.v1("POST", "/assignments", {"assignment": body})
        return asg[name]

    def page(title, html):
        if title in pages:
            return api.v1("PUT", f"/pages/{pages[title]['url']}", {"wiki_page": {"body": html}})
        pages[title] = api.v1("POST", "/pages", {"wiki_page": {"title": title, "body": html, "published": False}})
        return pages[title]

    def cfa(tid):
        title = Q.CFA_TITLE[tid]
        instr = (N.CFA_NOTE + f"<p><strong>Learning target {tid}:</strong> {U.TARGET[tid][3]}</p>"
                 "<p>5 questions. If you score below a B (fewer than 4 of 5 correct), a review for this target will open for you.</p>")
        if title in quizzes:
            api.nq("PATCH", f"/quizzes/{quizzes[title]['id']}", {"quiz": {"instructions": instr, "quiz_settings": N.CFA_CSA_SETTINGS}})
            return quizzes[title]
        items = [(f"{tid}.{n} · {tid}", it) for n, it in enumerate(Q.CFAS[tid], 1)]
        quizzes[title] = N.make_quiz(api, title, instr, items, group)
        return quizzes[title]

    def csa():
        title = Q.CSA_TITLE
        targets = "".join(f"<li><strong>{t}:</strong> {U.TARGET[t][3]}</li>" for t in U.PRIORITY)
        instr = (f"<p><strong>Living Earth (Biology) – {U.STANDARD}</strong></p><p>{U.PE}</p>"
                 f"<p><strong>Learning targets on this test:</strong></p><ul>{targets}</ul>"
                 "<p>17 questions. Three are written responses your teacher will grade. Work on your own; you have the full period.</p>")
        items = [(f"Q{n} · {t}", it) for n, (t, it) in enumerate(Q.CSA, 1)]
        if title in quizzes:  # rebuild the items in place so the module item and planner links stay valid
            qid = quizzes[title]["id"]
            for old in api.nq("GET", f"/quizzes/{qid}/items") or []:
                api.nq("DELETE", f"/quizzes/{qid}/items/{old['id']}")
            n_choice = 0
            for pos, (qtitle, it) in enumerate(items, 1):
                api.nq("POST", f"/quizzes/{qid}/items", {"item": {"position": pos, "points_possible": 4 if it["type"] == "essay" else 1,
                                                                 "entry_type": "Item", "entry": N.entry(it, qtitle, n_choice)}})
                n_choice += it["type"] == "choice"
            api.nq("PATCH", f"/quizzes/{qid}", {"quiz": {"instructions": instr, "quiz_settings": N.CFA_CSA_SETTINGS}})
            return quizzes[title]
        quizzes[title] = N.make_quiz(api, title, instr, items, group)
        return quizzes[title]

    # Days 9 and 10 swapped jobs: rename the existing Canvas objects in place so the planner's module-item links keep working
    for old_t, new_t in RENAMED_DAYS:
        for pre in ("Student Assignment", "Teacher Plan"):
            o, n_ = f"{old_t[0]} {pre}: {old_t[1]}", f"{new_t[0]} {pre}: {new_t[1]}"
            if o in asg and n_ not in asg:
                asg[n_] = api.v1("PUT", f"/assignments/{asg[o]['id']}", {"assignment": {"name": n_}})
                del asg[o]
            if o in pages and n_ not in pages:
                pages[n_] = api.v1("PUT", f"/pages/{pages[o]['url']}", {"wiki_page": {"title": n_}})
                del pages[o]
        o = f"{old_t[0]} · {old_t[2]}: {old_t[1]}"
        n_ = f"{new_t[0]} · {new_t[2]}: {new_t[1]}"
        for it in get_all(api, f"/modules/{student_mod}/items"):
            if it["type"] == "SubHeader" and it["title"] == o:
                api.v1("PUT", f"/modules/{student_mod}/items/{it['id']}", {"module_item": {"title": n_}})
    rules = api.v1("GET", "/mastery_paths/rules")
    wanted_names = set()
    order, teacher_order = [], []  # (kind, title or content id, indent) / page urls
    for d in U.DAYS:
        day, deck_id = d["day"], decks[str(d["day"])]
        order.append(("SubHeader", f"Day {day} · {d['date']}: {d['title']}", 0))
        if d["kind"] == "csa":
            order.append(("Assignment", int(csa()["id"]), 1))
        else:
            a = assignment(f"Day {day} Student Assignment: {d['title']}", student_html(d, deck_id))
            order.append(("Assignment", a["id"], 1))
        teacher_order.append(page(f"Day {day} Teacher Plan: {d['title']}", teacher_html(d, deck_id))["url"])
        if d["cfa"]:
            q = cfa(d["cfa"])
            wanted_names |= {Q.CFA_TITLE[d["cfa"]], f"{U.UNIT} Review {d['cfa']}: {U.TARGET[d['cfa']][1]} (Mastery Path)"}
            rev = assignment(f"{U.UNIT} Review {d['cfa']}: {U.TARGET[d['cfa']][1]} (Mastery Path)", R.REVIEWS[d["cfa"]], review=True)
            order += [("Assignment", int(q["id"]), 1), ("Assignment", rev["id"], 2)]
            body = {"trigger_assignment_id": int(q["id"]), "scoring_ranges": [
                {"lower_bound": B_CUTOFF, "upper_bound": None, "position": 1, "assignment_sets": []},
                {"lower_bound": 0.0, "upper_bound": B_CUTOFF, "position": 2,
                 "assignment_sets": [{"assignment_set_associations": [{"assignment_id": rev["id"]}]}]}]}
            old = next((x for x in rules if x["trigger_assignment_id"] == int(q["id"])), None)
            api.v1("PUT" if old else "POST", f"/mastery_paths/rules/{old['id']}" if old else "/mastery_paths/rules", body)
    teacher_order.insert(0, page(f"{U.UNIT} Overview and day-by-day plan", overview_html(decks))["url"])

    def place(mod, wanted):
        have = get_all(api, f"/modules/{mod}/items")
        for pos, (kind, ref, indent) in enumerate(wanted, 1):
            if kind == "SubHeader":
                it = next((i for i in have if i["type"] == "SubHeader" and i["title"] == ref), None)
                body = {"type": "SubHeader", "title": ref}
            elif kind == "Page":
                it = next((i for i in have if i.get("page_url") == ref), None)
                body = {"type": "Page", "page_url": ref}
            else:
                it = next((i for i in have if i.get("content_id") == ref and i["type"] in ("Assignment", "Quiz")), None)
                body = {"type": "Assignment", "content_id": ref}
            if it:
                api.v1("PUT", f"/modules/{mod}/items/{it['id']}", {"module_item": {"position": pos, "indent": indent}})
            else:
                api.v1("POST", f"/modules/{mod}/items", {"module_item": {**body, "position": pos, "indent": indent}})

    # retire CFAs and reviews that the plan no longer has (sandbox only; the course assert is above)
    stale = [a for n, a in asg.items() if n.startswith(f"{U.UNIT} Review ") and n not in wanted_names]
    stale += [q for t, q in quizzes.items() if t.startswith(f"{U.UNIT} CFA ") and t not in wanted_names]
    for a in stale:
        for rule in [x for x in rules if x["trigger_assignment_id"] == int(a["id"])]:
            api.v1("DELETE", f"/mastery_paths/rules/{rule['id']}")
        api.v1("DELETE", f"/assignments/{int(a['id'])}")
        print("retired", a.get("name") or a.get("title"))
    asg = {n: a for n, a in asg.items() if a not in stale}
    quizzes = {t: q for t, q in quizzes.items() if q not in stale}
    place(student_mod, order)
    place(teacher_mod, [("Page", u, 0) for u in teacher_order])
    print(f"Module {student_mod}: {len(order)} items; teacher module {teacher_mod}: {len(teacher_order)} pages")
    return {"module": student_mod, "teacher_module": teacher_mod,
            "assignments": {n: a["id"] for n, a in asg.items()}, "quizzes": {t: int(q["id"]) for t, q in quizzes.items()},
            "pages": {t: p["url"] for t, p in pages.items()}}


if __name__ == "__main__":
    if sys.argv[1] == "preview":
        d = U.DAY[int(sys.argv[2])]
        print(student_html(d, "DECK"))
    else:
        print(json.dumps(canvas(sys.argv[1], sys.argv[2]), indent=1))
