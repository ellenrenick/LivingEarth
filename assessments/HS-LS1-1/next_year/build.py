"""Build the next-year Unit 2.1 (content.py, cfas.py): Google Slides requests, and the Canvas module in a course.

Each lesson deck is a Drive copy of the Unit 1.3 Lesson 2 deck (same look and object ids as Short Lessons A and B),
rewritten here: title, notebook setup (slide 2), learning targets (slide 3), goals, one slide per notebook section,
then the CFA slide. Day 3 is a Drive copy of the 2026-27 gummy lab deck, unchanged.

  python3 build.py slides 4 > reqs.json     # Slides batchUpdate requests for Day 4's deck (a fresh Lesson 2 copy)
  python3 build.py canvas 333216 decks.json # module, pages, CFAs, reviews, Mastery Paths, CSA (safe to rerun)
  python3 build.py doc > assessments.md     # every CFA and the CSA, with keys, as markdown

decks.json maps day number to the deck's Drive id, e.g. {"1": "1abc...", "3": "1xyz..."}.
"""

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "HS-LS1-6"))
sys.path.insert(0, str(HERE.parent.parent / "HS-LS1-6" / "lessons"))
import classic_to_newquiz as C  # noqa: E402
import deck_requests as D  # noqa: E402
import newquiz_upload as N  # noqa: E402
import notebook_slides as NB  # noqa: E402
import cfas as Q  # noqa: E402
import content as U  # noqa: E402

EMU = 914400
LAYOUT = "h287605ecd2867468_0_216"
CFA_SLIDE = ("cfa_LS1_6_1", ["cfa_LS1_6_1_k", "cfa_LS1_6_1_t", "cfa_LS1_6_1_b", "SLIDES_API1306876476_0"])
INK = {"red": 0.137, "green": 0.224, "blue": 0.173}
MUTED = {"red": 0.43, "green": 0.46, "blue": 0.43}
TAN = {"red": 0.9098, "green": 0.8627, "blue": 0.7765}
TODAY = {"red": 1.0, "green": 0.84, "blue": 0.4}
WHITE = {"red": 1, "green": 1, "blue": 1}
LAB_DECK_2026 = "1xQ8vInixkGQ-GSjPvgjxy1tU0Km0WUFePmGom_Vc_Jw"
B_CUTOFF = 0.675  # below a B (fewer than 4 of 5) opens the review, as in Unit 1.3


# ---------------------------------------------------------------------------
# Text shared by slides and Canvas
# ---------------------------------------------------------------------------
def kicker(s):
    m = s["minutes"]
    if s.get("minutes_frame"):
        return f"{s['label']} · {m} MIN, THEN {s['minutes_frame']} MIN IN YOUR NOTEBOOK"
    return f"{s['label']} · {m} MIN · {s['who']}" if m else f"{s['label']} · {s['who']}"


def bank_line(s):
    if not s.get("bank"):
        return ""
    note = f" {s['bank_note']}" if s.get("bank_note") else ""
    return f"{s.get('bank_label', 'Word bank')}: " + " · ".join(U.scramble(s["bank"])) + note


def notebook_line(s):
    return f"In your notebook, under “{s['nb']}”:" if s.get("nb") else ""


def slide_body(s, with_intro=True):
    lines = list(s["body"]) if with_intro else []
    if s.get("frame"):
        lines += [notebook_line(s)] if s.get("nb") else []
        lines += s["frame"]
    elif s.get("nb") and s["layout_kind"] != "table":
        lines.append(f"(In your notebook, under “{s['nb']}”.)")
    if s.get("bank"):
        lines.append(bank_line(s))
    return "\n".join(x for x in lines if x)


def layout_kind(s):
    return s.get("layout") or ("table" if s.get("table") else "list")


for _d in U.DAYS:
    for _s in _d.get("sections", []):
        _s["layout_kind"] = layout_kind(_s)


def deck_title(d):
    return f"Unit 2.1 (2027-28) Day {d['day']} Slides: {d['title']}"


# ---------------------------------------------------------------------------
# Slides
# ---------------------------------------------------------------------------
def text_h(text, pt, w=8.9):
    """Rough height (in) of wrapped text: average glyph is half the point size wide."""
    import math
    cpl = w * 72 / (0.5 * pt)
    return sum(max(1, math.ceil(len(x) / cpl)) for x in text.split("\n")) * pt * 1.25 / 72


def emu(x):
    return int(x * EMU)


def props(page, x, y, w, h):
    return {"pageObjectId": page, "size": {"width": {"magnitude": emu(w), "unit": "EMU"},
                                           "height": {"magnitude": emu(h), "unit": "EMU"}},
            "transform": {"scaleX": 1, "scaleY": 1, "translateX": emu(x), "translateY": emu(y), "unit": "EMU"}}


def style(size, bold=False, color=INK, font="Calibri"):
    return {"fontFamily": font, "fontSize": {"magnitude": size, "unit": "PT"}, "bold": bold,
            "foregroundColor": {"opaqueColor": {"rgbColor": color}}}


def textbox(oid, page, x, y, w, h, text, size, bold=False, color=INK):
    return [{"createShape": {"objectId": oid, "shapeType": "TEXT_BOX", "elementProperties": props(page, x, y, w, h)}},
            {"insertText": {"objectId": oid, "insertionIndex": 0, "text": text}},
            {"updateTextStyle": {"objectId": oid, "textRange": {"type": "ALL"}, "style": style(size, bold, color),
                                 "fields": "fontFamily,fontSize,bold,foregroundColor"}}]


def font_size(oid, size):
    return {"updateTextStyle": {"objectId": oid, "textRange": {"type": "ALL"},
                                "style": {"fontSize": {"magnitude": size, "unit": "PT"}}, "fields": "fontSize"}}


def box_to(oid, y, h):
    """Move/resize a template text box (3,000,000 EMU square, scaled) to y..y+h inches, full content width."""
    return {"updatePageElementTransform": {"objectId": oid, "applyMode": "ABSOLUTE", "transform": {
        "scaleX": 2.7209, "scaleY": round(emu(h) / 3000000, 4), "translateX": 609600, "translateY": emu(y), "unit": "EMU"}}}


def col_widths(head, rows, width):
    raw = [max(6, max(len(str(r[c])) for r in [head] + rows)) for c in range(len(head))]
    widths = [max(0.7, width * w / sum(raw)) for w in raw]
    return [w * width / sum(widths) for w in widths]


def table_h(head, rows, width, fs, row):
    """Rough rendered height (in): rows grow when a cell wraps."""
    import math
    ws = col_widths(head, rows, width)
    return sum(max(row, max(math.ceil(len(str(c)) / max(1, w * 72 / (0.5 * fs) - 2)) for c, w in zip(r, ws)) * fs * 1.25 / 72 + 0.1)
               for r in [head] + rows)


def table(oid, page, x, y, head, rows, width, fs=11, row=0.27):
    nr, nc = len(rows) + 1, len(head)
    widths = col_widths(head, rows, width)
    reqs = [{"createTable": {"objectId": oid, "rows": nr, "columns": nc, "elementProperties": props(page, x, y, width, row * nr)}}]
    for c, w in enumerate(widths):
        reqs.append({"updateTableColumnProperties": {"objectId": oid, "columnIndices": [c], "tableColumnProperties": {
            "columnWidth": {"magnitude": emu(w), "unit": "EMU"}}, "fields": "columnWidth"}})
    for r, line in enumerate([head] + rows):
        for c, txt in enumerate(line):
            if not txt:
                continue
            loc = {"rowIndex": r, "columnIndex": c}
            reqs.append({"insertText": {"objectId": oid, "cellLocation": loc, "insertionIndex": 0, "text": str(txt)}})
            st = {"fontSize": {"magnitude": fs, "unit": "PT"}, "bold": r == 0}
            reqs.append({"updateTextStyle": {"objectId": oid, "cellLocation": loc, "textRange": {"type": "ALL"},
                                             "style": st, "fields": "fontSize,bold"}})
    for r, color in [(0, TAN)]:
        reqs.append({"updateTableCellProperties": {"objectId": oid, "tableRange": {
            "location": {"rowIndex": r, "columnIndex": 0}, "rowSpan": 1, "columnSpan": nc},
            "tableCellProperties": {"tableCellBackgroundFill": {"solidFill": {"color": {"rgbColor": color}}}},
            "fields": "tableCellBackgroundFill.solidFill.color"}})
    reqs.append({"updateTableRowProperties": {"objectId": oid, "rowIndices": list(range(nr)), "tableRowProperties": {
        "minRowHeight": {"magnitude": emu(row), "unit": "EMU"}}, "fields": "minRowHeight"}})
    return reqs


CREAM = {"red": 0.96, "green": 0.91, "blue": 0.8}
DARK = {"red": 0.32, "green": 0.21, "blue": 0.15}
KITTEN = {"red": 1.0, "green": 0.98, "blue": 0.95}
LINE = {"red": 0.45, "green": 0.4, "blue": 0.35}


def cat(prefix, page, x, y, k, adult):
    """A side-view cat drawn with shapes. Adult: cream body, dark ears, face, paws, tail. Kitten: white all over."""
    body = CREAM if adult else KITTEN
    point = DARK if adult else KITTEN
    parts = [  # (shape, x, y, w, h, color)
        ("ELLIPSE", 2.15, 0.85, 1.0, 0.2, point),                                        # tail
        ("RECTANGLE", 0.5, 1.25, 0.22, 0.45, body), ("RECTANGLE", 1.75, 1.25, 0.22, 0.45, body),   # legs
        ("ELLIPSE", 0.45, 1.62, 0.32, 0.16, point), ("ELLIPSE", 1.7, 1.62, 0.32, 0.16, point),     # paws
        ("ELLIPSE", 0.2, 0.6, 2.2, 0.85, body),                                          # body
        ("TRIANGLE", -0.38, -0.02, 0.3, 0.38, point), ("TRIANGLE", 0.02, -0.02, 0.3, 0.38, point),  # ears
        ("ELLIPSE", -0.45, 0.2, 0.85, 0.8, body),                                        # head
    ] + ([("ELLIPSE", -0.3, 0.45, 0.55, 0.5, point)] if adult else [])                  # face mask
    reqs = []
    for n, (shape, dx, dy, w, h, color) in enumerate(parts):
        oid = f"{prefix}_{n:02d}"
        reqs.append({"createShape": {"objectId": oid, "shapeType": shape,
                                     "elementProperties": props(page, x + dx * k, y + dy * k, w * k, h * k)}})
        reqs.append({"updateShapeProperties": {"objectId": oid, "shapeProperties": {
            "shapeBackgroundFill": {"solidFill": {"color": {"rgbColor": color}}},
            "outline": {"outlineFill": {"solidFill": {"color": {"rgbColor": LINE}}}, "weight": {"magnitude": 0.75, "unit": "PT"}}},
            "fields": "shapeBackgroundFill.solidFill.color,outline"}})
    return reqs


def targets_slide(d, sid):
    """Learning targets slide (slide 3): every Unit 2.1 target, today's marked ★ and in bold."""
    today = set(d["targets"])
    reqs = [{"createSlide": {"objectId": sid, "insertionIndex": 3, "slideLayoutReference": {"layoutId": LAYOUT}}}]
    reqs += textbox(f"{sid}_k", sid, 0.5, 0.25, 9.0, 0.3, f"UNIT 2.1 · DNA TO PROTEINS · {U.STANDARD}", 11, True, MUTED)
    reqs += textbox(f"{sid}_t", sid, 0.5, 0.5, 9.0, 0.5, "Learning targets", 26, True)
    sub = ("Today: all five priority targets (★)." if today == set(U.PRIORITY) else
           "Today: " + ", ".join(d["targets"]) + " (★)")
    reqs += textbox(f"{sid}_s", sid, 0.5, 0.98, 9.0, 0.3, sub, 12)
    lines = [f"{'★ ' if t[0] in today else ''}{t[0]}{' (supporting)' if t[4] == 'Supporting' else ''}: {t[3]}"
             for t in U.TARGETS]
    text = "\n".join(lines)
    reqs += textbox(f"{sid}_g", sid, 0.5, 1.35, 9.0, 3.7, text, 12)
    start = 0
    for line, t in zip(lines, U.TARGETS):
        if t[0] in today:
            reqs.append({"updateTextStyle": {"objectId": f"{sid}_g", "textRange": {
                "type": "FIXED_RANGE", "startIndex": start, "endIndex": start + len(line)}, "style": {"bold": True}, "fields": "bold"}})
        start += len(line) + 1
    reqs.append({"updateParagraphStyle": {"objectId": f"{sid}_g", "textRange": {"type": "ALL"},
                                          "style": {"spaceBelow": {"magnitude": 6, "unit": "PT"}}, "fields": "spaceBelow"}})
    reqs.append({"updateSlidesPosition": {"slideObjectIds": [sid], "insertionIndex": 2}})
    return reqs


def cfa_text(tid):
    return ["CFA · 6 MIN · ON YOUR OWN, FROM MEMORY", f"Show what you know: CFA {tid}",
            f"Open Canvas: {Q.CFA_TITLE[tid]} (5 questions).\nTarget: {U.TARGET[tid][3]}\n"
            "Below a B (fewer than 4 of 5)? A review for this target opens for you on Canvas."]


def deck(day):
    d = U.DAY[day]
    p = f"u{day}"
    footer = f"Day {day} · {d['title']}"
    slides = []
    for s in d["sections"]:
        kind = s["layout_kind"]
        tmpl = "warmup" if kind in ("warmup", "cats") else "list"
        text = "\n".join(s["body"]) if kind in ("table", "cats") else slide_body(s)
        slides.append((tmpl, [kicker(s), s["title"], text]))
    reqs = D.deck(p, f"{U.STANDARD} · {U.MYSTERY.upper()} · DAY {day}", d["title"], d["focus"], d["ready"], d["can"],
                  d["plan"], footer, slides)
    for n, s in enumerate(d["sections"], 3):
        sid = f"{p}_s{n:02d}"
        body = f"{sid}_e2"
        kind = s["layout_kind"]
        if kind == "list":
            lines = slide_body(s).count("\n") + 1
            reqs += [box_to(body, 1.48, 3.62), font_size(body, 12 if lines > 8 else 13 if lines > 6 else 15)]
        elif kind == "warmup":
            reqs += [box_to(body, 1.85, 3.2), font_size(body, 15)]
        elif kind == "table":
            head, rows = s["table"]
            intro_h = text_h("\n".join(s["body"]), 13) + 0.12
            reqs += [box_to(body, 1.48, intro_h), font_size(body, 13)]
            ty = 1.48 + intro_h + 0.04
            rh = 0.27 if len(rows) <= 6 else 0.25
            reqs += table(f"{sid}_tb", sid, 0.67, ty, head, rows, 8.9, fs=11 if len(rows) <= 5 else 10, row=rh)
            rest = slide_body(s, with_intro=False)
            if rest:
                fy = ty + table_h(head, rows, 8.9, 11 if len(rows) <= 5 else 10, rh) + 0.12
                fs = 12 if fy + text_h(rest, 12) <= 5.0 else 11
                reqs += textbox(f"{sid}_fr", sid, 0.67, fy, 8.9, max(0.4, 5.05 - fy), rest, fs)
        elif kind == "cats":
            reqs += [box_to(body, 1.45, 0.4), font_size(body, 14)]
            reqs += cat(f"{sid}_ad", sid, 1.4, 2.05, 0.75, True) + cat(f"{sid}_kt", sid, 6.3, 2.5, 0.5, False)
            reqs += textbox(f"{sid}_la", sid, 1.0, 3.4, 2.6, 0.3, "Adult Siamese cat", 12, True)
            reqs += textbox(f"{sid}_lk", sid, 5.9, 3.4, 2.6, 0.3, "Newborn Siamese kitten", 12, True)
            reqs += textbox(f"{sid}_fr", sid, 0.67, 3.8, 8.9, 0.85, slide_body(s, with_intro=False), 14)
    reqs.append({"deleteObject": {"objectId": "lt_d2_slide"}})
    src, els = CFA_SLIDE
    if d["cfa"]:
        for e, t in zip(els, cfa_text(d["cfa"]) + [footer]):
            reqs += D.text(e, t)
        reqs.append({"updateSlidesPosition": {"slideObjectIds": [src], "insertionIndex": 2 + len(slides)}})
    else:
        reqs.append({"deleteObject": {"objectId": src}})
    if d.get("notebook"):
        key = f"U21D{day}"
        NB.DECKS[key] = dict(id="", scale=1.0, title=f"Day {day}: {d['title']}", focus=d["focus"], **d["notebook"])
        b = NB.Builder(key)
        b.layout = {"layoutId": LAYOUT}
        reqs += b.build()
    reqs += targets_slide(d, f"lt_u{day}")
    return reqs


# ---------------------------------------------------------------------------
# Canvas
# ---------------------------------------------------------------------------
BOX = "background:#eef5fb;border-left:5px solid #2b6cb0;padding:10px 14px;margin:12px 0"
TBOX = "background:#fff7e6;border-left:5px solid #c05621;padding:10px 14px;margin:12px 0"
BANK = "border:1px solid #999;padding:6px"
SLIDES = "https://docs.google.com/presentation/d/{}/edit"


def html_table(head, rows):
    th = "<tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr>"
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table border="1" cellpadding="6" style="border-collapse:collapse"><tbody>{th}{tr}</tbody></table>'


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
        out += (f"<p><strong>{notebook_line(s)}</strong></p>" if s.get("nb") else "") + "<ul>" + "".join(
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
    out = [f'<div style="{BOX}"><p><strong>Day {d["day"]}</strong> · {U.UNIT}: {U.UNIT_NAME} ({U.STANDARD}) · {U.MYSTERY}</p>'
           f"<p><strong>Driving question:</strong> {U.DRIVING_Q}</p><p><strong>Focus question:</strong> {d['focus']}</p>"
           f"<p><strong>{label}:</strong></p><ul>{tl}</ul>"
           + (f"<p>About {mins} minutes.</p>" if mins else "") + "</div>",
           slides_embed(deck_id, f"Day {d['day']}: {d['title']}")]
    if d.get("notebook"):
        out.append(f'<h2>Notebook setup</h2><div style="{BOX}"><p><strong>Before the lesson:</strong> title a new page '
                   f"<strong>Day {d['day']}: {d['title']}</strong> and copy the layout on slide 2. Fill it in as you go, "
                   "in the same order as the slides.</p><p><em>Your notebook is your answer sheet for this lesson.</em></p></div>")
    parts = [s for s in d["sections"]]
    for n, s in enumerate(parts, 1):
        out.append(f"<hr><h2>Part {n}: {s['title']}</h2>{section_html(s)}")
    if d["day"] in U.ANIMATIONS:
        name, url = U.ANIMATIONS[d["day"]]
        out.append(f'<p style="{BANK}"><strong>Review animation:</strong> <a href="{url}" target="_blank" rel="noopener">{name}</a> '
                   "(use it to review before the CFA, or at home).</p>")
    if d["cfa"]:
        out.append(f"<hr><h2>Part {len(parts) + 1}: Show what you know: CFA {d['cfa']}</h2>"
                   f"<p>Take <strong>{Q.CFA_TITLE[d['cfa']]}</strong> on Canvas (5 questions), on your own and from memory. "
                   "If you score below a B (fewer than 4 of 5), a review for this target will open for you.</p>")
    out.append("<hr><p><strong>If you were absent:</strong> go through today's slides above, complete the notebook "
               "page, and take any CFA listed on this page.</p>")
    return "\n".join(out)


def teacher_html(d, deck_id, links):
    mins = U.minutes(d)
    rows = [("2", "Notebook setup: students copy slide 2.")] if d.get("notebook") else []
    rows += [(str(s["minutes"] + s.get("minutes_frame", 0)) if s["minutes"] else "", f"<strong>{s['title']}.</strong> {s['teacher']}")
             for s in d["sections"]]
    if d["cfa"]:
        rows.append(("6", f"<strong>CFA {d['cfa']}</strong>, on their own and from memory. Below a B opens the review."))
    agenda = html_table(["Min", "What happens"], rows)
    total = f" ({mins} minutes)" if mins else ""
    return "\n".join([
        f'<div style="{TBOX}"><p><strong>Teacher page · keep unpublished.</strong> Students never see this page.</p>'
        f"<p><strong>Day {d['day']}: {d['title']}</strong> · Targets: {', '.join(d['targets'])}"
        + (f" · CFA {d['cfa']}" if d["cfa"] else "") + "</p></div>",
        f'<p><a href="{SLIDES.format(deck_id)}">Slides</a>' + "".join(f" · {l}" for l in links) + "</p>",
        f"<h2>Agenda{total}</h2>{agenda}",
        "<h2>Answer key</h2><ol>" + "".join(f"<li>{k}</li>" for k in d.get("key", [])) + "</ol>",
        "<h2>Notes</h2><ul>" + "".join(f"<li>{n}</li>" for n in d.get("notes", [])) + "</ul>"])


def overview_html(decks):
    rows = [[t[0], t[4], t[3], str(t[2])] for t in U.TARGETS]
    days = []
    for d in U.DAYS:
        m = U.minutes(d)
        days.append([f"Day {d['day']}", f'<a href="{SLIDES.format(decks[str(d["day"])])}">{d["title"]}</a>',
                     ", ".join(d["targets"]), f"CFA {d['cfa']}" if d["cfa"] else "none",
                     f"{m} min" if m else "full period"])
    return (f"<h2>{U.UNIT}: {U.UNIT_NAME} ({U.STANDARD}) · next-year version (8 days)</h2>"
            "<p><em>Built for 2027-28 from the department workbook (8 days; LS1-1.1 to 1.5 priority, LS3-1.1 to 1.3 "
            "supporting). Every lesson follows the Unit 1.3 Short Lesson A/B pace and style: about 30 minutes of student "
            "work including the CFA.</em></p>"
            f"<h3>Anchoring phenomenon</h3><p>{U.DRIVING_Q}</p><h3>Learning targets</h3>"
            + html_table(["Target", "Tier", "I can", "DOK"], rows)
            + "<h3>Day by day</h3>" + html_table(["Day", "Lesson", "Targets", "CFA", "Time"], days)
            + "<p>Day 3 (gummy DNA lab) is unchanged from 2026-27. CFAs: 5 questions each, below a B (fewer than 4 of 5) "
              "opens that target's review (Mastery Path). The CSA has 13 questions (19 raw points, graded out of 4).</p>")


def get_all(api, path):
    out, page = [], 1
    while True:
        sep = "&" if "?" in path else "?"
        batch = api.v1("GET", f"{path}{sep}per_page=100&page={page}")
        if not batch:
            return out
        out += batch
        page += 1


def canvas(course, decks_file):
    decks = json.loads(Path(decks_file).read_text())
    api = N.Canvas("https://kernhigh.instructure.com", course, "")
    group = next(g for g in api.v1("GET", "/assignment_groups") if g["name"] == "Assignments")["id"]
    src = json.loads((HERE / "source_2026.json").read_text())
    mods = {m["name"]: m for m in get_all(api, "/modules")}

    def module(name):
        if name not in mods:
            mods[name] = api.v1("POST", "/modules", {"module": {"name": name, "published": False}})
        return mods[name]["id"]

    student_mod = module(f"{U.UNIT}: {U.UNIT_NAME} {U.STANDARD} (next year)")
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
        title = f"{U.UNIT} CSA: {U.UNIT_NAME} ({U.STANDARD})"
        targets = "".join(f"<li><strong>{t}:</strong> {U.TARGET[t][3]}</li>" for t in U.PRIORITY)
        instr = (f"<p><strong>Living Earth (Biology) – {U.STANDARD}</strong></p><p>{U.PE}</p>"
                 f"<p><strong>Learning targets on this test:</strong></p><ul>{targets}</ul>"
                 "<p>13 questions. Two are written responses your teacher will grade. A code table is included in every "
                 "question that needs one. Work on your own; you have the full period.</p>")
        if title in quizzes:
            return quizzes[title]
        quiz = api.nq("POST", "/quizzes", {"quiz": {
            "title": title, "instructions": instr, "assignment_group_id": group, "grading_type": "points", "published": False,
            "quiz_settings": {"has_time_limit": False, "one_at_a_time_type": "none", "allow_backtracking": True,
                              **N.CFA_CSA_SETTINGS}}})
        raw, n_choice = 0, 0
        for pos, (qt, it, kind) in enumerate(Q.csa_items(), 1):
            if kind == "classic":
                e = C.entry(it, qt, it["question_text"])
                pts = 4 if it["question_type"] == "essay_question" else 1
            else:
                e = N.entry(it, qt, n_choice)
                n_choice += it["type"] == "choice"
                pts = 1
            raw += pts
            api.nq("POST", f"/quizzes/{quiz['id']}/items", {"item": {"position": pos, "points_possible": pts,
                                                                    "entry_type": "Item", "entry": e}})
        api.nq("PATCH", f"/quizzes/{quiz['id']}", {"quiz": {"points_possible": 4}})
        print(f"CSA: {title} ({pos} questions, {raw} raw points, graded out of 4) id={quiz['id']}")
        quizzes[title] = quiz
        return quiz

    rules = api.v1("GET", "/mastery_paths/rules")
    order = []  # (kind, title or content id, indent)
    teacher_order = []
    review_text = ("Your goal on every CFA is at least a B (4 of 5). Your CFA score was below a B, so this review opened "
                   "for you. Work through the questions, check your answers, then submit your answers.")
    for d in U.DAYS:
        day, deck_id = d["day"], decks[str(d["day"])]
        order.append(("SubHeader", f"Day {day}: {d['title']}", 0))
        if d["kind"] == "lab":
            lab = src["lab"]["description"].replace(LAB_DECK_2026, deck_id)
            a = assignment(f"Day 3: {src['lab']['name']}", lab, points=4)
            order.append(("Assignment", a["id"], 1))
            for t in ("Day 3 Teacher Plan: Gummy DNA Lab", "Day 3 Teacher Key and Prep: Gummy DNA Lab"):
                body = src[t]["body"].replace(LAB_DECK_2026, deck_id)
                teacher_order.append(page(f"{t} (next year)", body)["url"])
        elif d["kind"] == "csa":
            q = csa()
            order.append(("Assignment", int(q["id"]), 1))
        else:
            a = assignment(f"Day {day} Student Assignment: {d['title']}", student_html(d, deck_id))
            order.append(("Assignment", a["id"], 1))
        if d["kind"] != "lab":
            links = [f'<a href="{U.ANIMATIONS[day][1]}">Review animation: {U.ANIMATIONS[day][0]}</a>'] if day in U.ANIMATIONS else []
            teacher_order.append(page(f"Day {day} Teacher Plan: {d['title']} (next year)", teacher_html(d, deck_id, links))["url"])
        if d["cfa"]:
            q = cfa(d["cfa"])
            r = src[f"Review {d['cfa']}"]
            desc = re.sub(r"Your goal on every CFA is at least a 3\..*?then submit your answers\.", review_text, r["description"],
                          flags=re.S)
            rev = assignment(f"{U.UNIT} Review {d['cfa']}: {U.TARGET[d['cfa']][1]} (Mastery Path)", desc, review=True)
            order += [("Assignment", int(q["id"]), 1), ("Assignment", rev["id"], 2)]
            body = {"trigger_assignment_id": int(q["id"]), "scoring_ranges": [
                {"lower_bound": B_CUTOFF, "upper_bound": None, "position": 1, "assignment_sets": []},
                {"lower_bound": 0.0, "upper_bound": B_CUTOFF, "position": 2,
                 "assignment_sets": [{"assignment_set_associations": [{"assignment_id": rev["id"]}]}]}]}
            old = next((x for x in rules if x["trigger_assignment_id"] == int(q["id"])), None)
            api.v1("PUT" if old else "POST", f"/mastery_paths/rules/{old['id']}" if old else "/mastery_paths/rules", body)
    teacher_order.insert(0, page(f"{U.UNIT} Overview and day-by-day plan (next year)", overview_html(decks))["url"])

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

    place(student_mod, order)
    place(teacher_mod, [("Page", u, 0) for u in teacher_order])
    print(f"Module {student_mod}: {len(order)} items; teacher module {teacher_mod}: {len(teacher_order)} pages")
    return {"module": student_mod, "teacher_module": teacher_mod,
            "assignments": {n: a["id"] for n, a in asg.items()}, "quizzes": {t: int(q["id"]) for t, q in quizzes.items()},
            "pages": {t: p["url"] for t, p in pages.items()}}


def refresh_cfas(course):
    """Rewrite every CFA item from cfas.py in place (same quiz, same positions, keys moved by KEY_POSITIONS)."""
    api = N.Canvas("https://kernhigh.instructure.com", course, "")
    quizzes = {q["title"]: q for q in api.nq("GET", "/quizzes?per_page=100")}
    for tid, bank in Q.CFAS.items():
        qid = quizzes[Q.CFA_TITLE[tid]]["id"]
        items = sorted(api.nq("GET", f"/quizzes/{qid}/items"), key=lambda i: i["position"])
        n_choice = 0
        for it, (n, b) in zip(items, enumerate(bank, 1)):
            e = N.entry(b, f"{tid}.{n} · {tid}", n_choice)
            n_choice += b["type"] == "choice"
            api.nq("PATCH", f"/quizzes/{qid}/items/{it['id']}", {"item": {"entry": e}})
        print(f"Refreshed {Q.CFA_TITLE[tid]} ({len(items)} items)")


# ---------------------------------------------------------------------------
# Assessments as markdown (for the assessments doc)
# ---------------------------------------------------------------------------
def _md(s):
    s = re.sub(r"<table.*?</table>", lambda m: "\n\n" + _md_table(m.group(0)) + "\n\n", s, flags=re.S)
    s = re.sub(r"</?(strong|b)>", "**", s)
    s = re.sub(r"</?em>", "*", s)
    s = re.sub(r"<li>", "\n- ", s)
    s = re.sub(r"</p>\s*<p>", "\n\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"[ \t]+", " ", s.replace("&rarr;", "→").replace("&nbsp;", " ")).strip()


def _md_table(t):
    rows = re.findall(r"<tr>(.*?)</tr>", t, flags=re.S)
    cells = [[re.sub(r"<[^>]+>", "", c).strip() for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", r, flags=re.S)] for r in rows]
    out = ["| " + " | ".join(cells[0]) + " |", "| " + " | ".join("---" for _ in cells[0]) + " |"]
    return "\n".join(out + ["| " + " | ".join(r) + " |" for r in cells[1:]])


def doc():
    L = "ABCDEFGH"
    out = []
    for tid, items in Q.CFAS.items():
        out.append(f"## {Q.CFA_TITLE[tid]}\n\n**Target:** {U.TARGET[tid][3]} 5 questions, 1 point each. Below a B "
                   "(fewer than 4 of 5) opens the review.\n")
        key = []
        for n, it in enumerate(items, 1):
            out.append(f"### Question {n}\n\n{_md(it['prompt'])}\n")
            if it["type"] == "choice":
                ch, pos = N.place_key(it, n - 1)
                out.append("\n".join(f"- {L[i]}. {_md(x)}" for i, x in enumerate(ch)) + "\n")
                key.append(f"| {n} | {L[pos]} | {it['feedback']} |")
            else:
                key.append(f"| {n} | {'True' if it['answer'] else 'False'} | {it['feedback']} |")
        out.append("### Answer key\n\n| Question | Answer | Why |\n| --- | --- | --- |\n" + "\n".join(key) + "\n")
    return "\n".join(out)


def csa_doc():
    L = "ABCDEFGH"
    out = ["## Unit 2.1 CSA: DNA to Proteins (HS-LS1-1)\n\n13 questions, 19 raw points, graded out of 4. Canvas shuffles "
           "questions and answer choices; letters here follow this doc's order.\n"]
    key = []
    for n, (title, it, kind) in enumerate(Q.csa_items(), 1):
        tid = title.split(" · ")[1].split(" ")[0]
        if kind == "bank":
            out.append(f"### Question {n} ({tid})\n\n{_md(it['prompt'])}\n")
            if it["type"] == "choice":
                out.append("\n".join(f"- {L[i]}. {_md(c)}" for i, c in enumerate(it["choices"])) + "\n")
                key.append(f"| {n} | {tid} | A |")
            else:
                key.append(f"| {n} | {tid} | {'True' if it['answer'] else 'False'} |")
            continue
        t = it["question_type"]
        pts = " (4 points, teacher-graded)" if t == "essay_question" else ""
        out.append(f"### Question {n} ({tid}){pts}\n\n{_md(it['question_text'])}\n")
        if t == "multiple_choice_question":
            ans = it["answers"]
            out.append("\n".join(f"- {L[i]}. {_md(a.get('html') or a.get('text'))}" for i, a in enumerate(ans)) + "\n")
            key.append(f"| {n} | {tid} | {L[next(i for i, a in enumerate(ans) if a['weight'] > 0)]} |")
        elif t == "matching_question":
            out.append("\n".join(f"- {a['left']}" for a in it["answers"]) + "\n\nDefinitions to choose from:\n\n" +
                       "\n".join(f"- {a['right']}" for a in it["answers"]) + "\n" +
                       "".join(f"- {d}\n" for d in (it.get("matching_answer_incorrect_matches") or "").split("\n") if d.strip()))
            key.append(f"| {n} | {tid} | " + "; ".join(f"{a['left']}: {a['right']}" for a in it["answers"]) + " |")
        else:
            key.append(f"| {n} | {tid} | Rubric below |")
    out.append("### Answer key\n\n| Question | Target | Answer |\n| --- | --- | --- |\n" + "\n".join(key) + "\n")
    for n, (title, it, kind) in enumerate(Q.csa_items(), 1):
        if kind == "classic" and it["question_type"] == "essay_question":
            out.append(f"### Question {n} rubric\n\n{_md(it['neutral_comments_html'])}\n")
    return "\n".join(out)


if __name__ == "__main__":
    what = sys.argv[1]
    if what == "slides":
        print(json.dumps(deck(int(sys.argv[2])), ensure_ascii=False, separators=(",", ":")))
    elif what == "canvas":
        print(json.dumps(canvas(sys.argv[2], sys.argv[3]), indent=1))
    elif what == "refresh-cfas":
        refresh_cfas(sys.argv[2])
    elif what == "doc":
        print(doc())
    elif what == "csa-doc":
        print(csa_doc())
    elif what == "preview":
        d = U.DAY[int(sys.argv[2])]
        print(student_html(d, "DECK"))
