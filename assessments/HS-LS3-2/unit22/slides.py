"""Google Slides requests for the Unit 2.2 decks: blue theme with orange accents, laid out like the Unit 2.1 decks.

Each deck: title slide, notebook setup (slide 2), learning targets (slide 3), one slide per notebook section in notebook order,
then the CFA (exit ticket) slide. Every deck is a Drive copy of one template deck; this module writes (1) the requests that build
the template (once) and (2) the small batch of requests that turns a copy into a day's deck.

  python3 slides.py template > template_requests.json     # build the template (into a blank deck)
  python3 slides.py deck 4 > deck4_requests.json           # fill a copy of the template for Day 4

The notebook setup slide (slide 2) is then replaced by nbslide.py (a Unit 2.1-style notebook spread). Day 3 is built by
`imgdeck` (original Genetics Notes graphics, see image_slide below) instead of `deck`.

Page: 10 x 5.625 in (9144000 x 5143500 EMU). Font: Lexend (as in Unit 2.1). Colors are RGB 0-1 for the API.
"""

import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cfas as Q  # noqa: E402
import content as U  # noqa: E402

EMU = 914400
FONT = "Lexend"


def rgb(h):
    h = h.lstrip("#")
    return {"red": round(int(h[0:2], 16) / 255, 4), "green": round(int(h[2:4], 16) / 255, 4), "blue": round(int(h[4:6], 16) / 255, 4)}


NAVY = rgb("0B2D5C")      # title slide background, kicker pills
BLUE = rgb("1E5FBF")      # titles, bars, table headers
LIGHT = rgb("EAF2FC")     # content slide background
ORANGE = rgb("FF8A1F")    # accent
ORANGE_LIGHT = rgb("FFE7CC")
INK = rgb("10264A")       # body text
MUTED = rgb("4A6A9E")     # footer
PALE = rgb("CFE0FA")      # footer on the title slide
WHITE = rgb("FFFFFF")


def e(x):
    return int(round(x * EMU))


def props(page, x, y, w, h):
    return {"pageObjectId": page,
            "size": {"width": {"magnitude": e(w), "unit": "EMU"}, "height": {"magnitude": e(h), "unit": "EMU"}},
            "transform": {"scaleX": 1, "scaleY": 1, "translateX": e(x), "translateY": e(y), "unit": "EMU"}}


def shape(oid, page, kind, x, y, w, h, fill=None, line=None, line_pt=1.0, text=None, size=14, bold=False, color=INK,
          align="START", valign="TOP", space_below=0):
    """createShape + fill/outline + optional styled text. fill/line are rgb dicts or None (not rendered)."""
    r = [{"createShape": {"objectId": oid, "shapeType": kind, "elementProperties": props(page, x, y, w, h)}}]
    if kind == "TEXT_BOX" and not fill and not line and valign == "TOP":
        if text is not None:
            r += set_text(oid, text, size, bold, color, align, space_below)
        return r
    sp, fields = {}, []
    if fill:
        sp["shapeBackgroundFill"] = {"solidFill": {"color": {"rgbColor": fill}}}
        fields.append("shapeBackgroundFill.solidFill.color")
    else:
        sp["shapeBackgroundFill"] = {"propertyState": "NOT_RENDERED"}
        fields.append("shapeBackgroundFill.propertyState")
    if line:
        sp["outline"] = {"outlineFill": {"solidFill": {"color": {"rgbColor": line}}}, "weight": {"magnitude": line_pt, "unit": "PT"}}
        fields += ["outline.outlineFill.solidFill.color", "outline.weight"]
    else:
        sp["outline"] = {"propertyState": "NOT_RENDERED"}
        fields.append("outline.propertyState")
    sp["contentAlignment"] = valign if valign != "TOP" else "TOP"
    fields.append("contentAlignment")
    r.append({"updateShapeProperties": {"objectId": oid, "shapeProperties": sp, "fields": ",".join(fields)}})
    if text is not None:
        r += set_text(oid, text, size, bold, color, align, space_below)
    return r


def set_text(oid, text, size, bold=False, color=INK, align="START", space_below=0):
    r = [{"insertText": {"objectId": oid, "insertionIndex": 0, "text": text}},
         {"updateTextStyle": {"objectId": oid, "textRange": {"type": "ALL"}, "style": {
             "fontFamily": FONT, "fontSize": {"magnitude": size, "unit": "PT"}, "bold": bold,
             "foregroundColor": {"opaqueColor": {"rgbColor": color}}}, "fields": "fontFamily,fontSize,bold,foregroundColor"}},
         ]
    if align != "START" or space_below:
        r.append({"updateParagraphStyle": {"objectId": oid, "textRange": {"type": "ALL"}, "style": {
            "alignment": align, "spaceBelow": {"magnitude": space_below, "unit": "PT"}}, "fields": "alignment,spaceBelow"}})
    return r


def background(page, color):
    return {"updatePageProperties": {"objectId": page, "pageProperties": {"pageBackgroundFill": {"solidFill": {"color": {"rgbColor": color}}}},
                                     "fields": "pageBackgroundFill.solidFill.color"}}


def new_slide(oid, index):
    return {"createSlide": {"objectId": oid, "insertionIndex": index, "slideLayoutReference": {"predefinedLayout": "BLANK"}}}


# ---------------------------------------------------------------------------
# Template (built once): geometry in inches
# ---------------------------------------------------------------------------
BODY_W, BODY_H = 8.64, 3.1
BODY_X, BODY_Y = 0.68, 1.88
FRAME_H = 1.0


def chrome(page, kick_w=3.6):
    """Kicker pill, emoji circle, title, bar, white card, footer: the shared look of every content slide."""
    r = [background(page, LIGHT)]
    r += shape(f"{page}_card", page, "ROUND_RECTANGLE", 0.5, 1.75, 9.0, 3.35, fill=WHITE)
    r += shape(f"{page}_kick", page, "ROUND_RECTANGLE", 0.5, 0.27, kick_w, 0.36, fill=NAVY, text="{{KICK}}", size=12, bold=True,
               color=ORANGE, valign="MIDDLE", align="CENTER")
    r += shape(f"{page}_emo", page, "ELLIPSE", 8.75, 0.12, 0.75, 0.75, fill=ORANGE, line=NAVY, line_pt=2.25, text="{{EMO}}", size=22,
               color=NAVY, align="CENTER", valign="MIDDLE")
    r += shape(f"{page}_title", page, "TEXT_BOX", 0.5, 0.72, 8.1, 0.7, text="{{TITLE}}", size=30, bold=True, color=BLUE, valign="BOTTOM")
    r += shape(f"{page}_bar", page, "ROUND_RECTANGLE", 0.5, 1.55, 1.5, 0.07, fill=ORANGE)
    r += shape(f"{page}_foot", page, "TEXT_BOX", 0.5, 5.2, 9.0, 0.3, text="{{FOOT}}", size=11, bold=True, color=MUTED)
    return r


def template_requests():
    r = []
    # title slide
    t = "tpl_title"
    r.append(new_slide(t, 0))
    r.append(background(t, NAVY))
    r += shape(f"{t}_kick", t, "ROUND_RECTANGLE", 0.5, 0.72, 4.6, 0.36, fill=ORANGE, text="{{KICK}}", size=12, bold=True, color=NAVY,
               valign="MIDDLE", align="CENTER")
    r += shape(f"{t}_nb", t, "TEXT_BOX", 5.45, 0.66, 4.0, 0.46, text="Notebook pages: ________", size=14, bold=True, color=WHITE, align="END")
    r += shape(f"{t}_title", t, "TEXT_BOX", 0.5, 1.3, 6.55, 1.55, text="{{TITLE}}", size=38, bold=True, color=ORANGE, valign="MIDDLE")
    r += shape(f"{t}_bar", t, "ROUND_RECTANGLE", 0.5, 3.0, 1.7, 0.08, fill=ORANGE)
    r += shape(f"{t}_sub", t, "TEXT_BOX", 0.5, 3.2, 9.0, 1.75, text="{{SUB}}", size=22, color=WHITE)
    r += shape(f"{t}_emo", t, "ELLIPSE", 7.45, 1.35, 1.9, 1.9, fill=ORANGE, line=WHITE, line_pt=4, text="{{EMO}}", size=66, color=NAVY,
               align="CENTER", valign="MIDDLE")
    r += shape(f"{t}_foot", t, "TEXT_BOX", 0.5, 5.2, 9.0, 0.3, text="{{FOOT}}", size=11, bold=True, color=PALE)

    # notebook setup (white page): title, focus question, up to 8 section cards in two columns
    n = "tpl_nb"
    r.append(new_slide(n, 1))
    r.append(background(n, WHITE))
    r += shape(f"{n}_top", n, "RECTANGLE", 0, 0, 10, 0.12, fill=ORANGE)
    r += shape(f"{n}_title", n, "TEXT_BOX", 0.35, 0.2, 9.3, 0.5, text="{{TITLE}}", size=20, bold=True, color=NAVY)
    r += shape(f"{n}_focus", n, "TEXT_BOX", 0.35, 0.7, 9.3, 0.5, text="{{FOCUS}}", size=12, bold=True, color=BLUE)
    for i in range(8):
        col, row = i // 4, i % 4
        x, y = 0.35 + col * 4.85, 1.3 + row * 1.02
        r += shape(f"{n}_c{i + 1}", n, "ROUND_RECTANGLE", x, y, 4.5, 0.92, fill=LIGHT, line=BLUE, line_pt=1,
                   text="{{H%d}}\n{{D%d}}" % (i + 1, i + 1), size=10, color=MUTED, space_below=2)
        # heading line bold and larger
        r.append({"updateTextStyle": {"objectId": f"{n}_c{i + 1}", "textRange": {"type": "FIXED_RANGE", "startIndex": 0, "endIndex": len("{{H%d}}" % (i + 1))},
                                      "style": {"fontSize": {"magnitude": 13, "unit": "PT"}, "bold": True,
                                                "foregroundColor": {"opaqueColor": {"rgbColor": NAVY}}},
                                      "fields": "fontSize,bold,foregroundColor"}})

    # learning targets
    g = "tpl_targets"
    r.append(new_slide(g, 2))
    r += chrome(g, kick_w=5.4)
    r += shape(f"{g}_body", g, "TEXT_BOX", BODY_X, 1.82, BODY_W, 3.25, text="{{BODY}}", size=12, color=INK, space_below=5)

    # content slide: body and (for tables) frame boxes; list slides delete the frame box
    c = "tpl_content"
    r.append(new_slide(c, 3))
    r += chrome(c)
    r += shape(f"{c}_body", c, "TEXT_BOX", BODY_X, BODY_Y, BODY_W, BODY_H, text="{{BODY}}", size=16, color=INK, space_below=6)
    r += shape(f"{c}_frame", c, "TEXT_BOX", BODY_X, BODY_Y + 2.0, BODY_W, FRAME_H, text="{{FRAME}}", size=14, color=INK, space_below=4)
    return r


# ---------------------------------------------------------------------------
# Text fitting
# ---------------------------------------------------------------------------
def lines_needed(text, width_in, pt):
    cpl = max(8, int(width_in * 72 / (0.60 * pt)))
    return sum(max(1, math.ceil(len(p) / cpl)) for p in text.split("\n"))


def text_h(text, width_in, pt, space_after_pt=6):
    n_par = len(text.split("\n"))
    return lines_needed(text, width_in, pt) * pt * 1.3 / 72 + n_par * space_after_pt / 72 + 0.12


def fit(text, width_in, height_in, sizes=(22, 20, 18, 16, 15, 14, 13, 12, 11), space=6):
    for s in sizes:
        if text_h(text, width_in, s, space) <= height_in:
            return s
    return sizes[-1]


# ---------------------------------------------------------------------------
# Section text
# ---------------------------------------------------------------------------
def bank_line(s):
    if not s.get("bank"):
        return ""
    note = f" {s['bank_note']}" if s.get("bank_note") else ""
    return "Word bank: " + " · ".join(U.scramble(s["bank"])) + note


def kicker(s):
    m = s["minutes"] + s.get("minutes_frame", 0)
    return f"{s['label']} · {m} MIN · {s['who']}" if m else f"{s['label']} · {s['who']}"


EMOJI = {"WARM-UP": "🔄", "MINI-LESSON": "💡", "NOTES": "📝", "EVIDENCE": "📊", "LAB": "🧪", "CARD ACTIVITY": "🃏",
         "MY FIRST MODEL": "✏️", "SKETCHNOTES": "🎨", "KEY IDEA": "🔑", "EXIT TICKET": "🎟️", "ANALYZE": "🔍",
         "REVISE MY MODEL": "✏️", "PRACTICE": "🎯", "COMPARE": "⚖️", "PERCENT CHANCE": "🧮", "REAL COUNTS": "🎲", "SORT": "🗂️",
         "EXPLAIN IT": "💬", "WORKED EXAMPLE": "🔎", "CASE 2": "📂", "CASE 3": "📂", "CASE": "📂", "CER": "✍️", "CHECK-IN": "✅",
         "WORK TIME": "⏳", "ENRICHMENT": "🌱", "SELF-CHECK": "🌟", "MYSTERY SOLVED": "🧩", "WRITE IT": "✍️", "CSA": "📝"}

LABEL_STARTS = ("Worked example", "Worked example (Day 8, Case 3)", "Claim:", "Evidence:", "Reasoning:", "Defense:", "Counterclaim",
                "Today's question:", "Word bank:", "Offspring 1", "Cross 1", "Cross 2", "Idea 1", "Step 1", "In your notebook")


def bold_ranges(text):
    """(start, end) of each line's label (up to its first colon) for lines that start with a known label."""
    out, pos = [], 0
    for line in text.split("\n"):
        for lab in LABEL_STARTS:
            if line.startswith(lab):
                k = line.find(":")
                out.append((pos, pos + (k + 1 if k > 0 else len(lab))))
                break
        pos += len(line) + 1
    return out


def style_ranges(oid, ranges, color=None):
    out = []
    for a, b in ranges:
        st, fl = {"bold": True}, "bold"
        if color:
            st["foregroundColor"] = {"opaqueColor": {"rgbColor": color}}
            fl += ",foregroundColor"
        out.append({"updateTextStyle": {"objectId": oid, "textRange": {"type": "FIXED_RANGE", "startIndex": a, "endIndex": b},
                                        "style": st, "fields": fl}})
    return out


def section_texts(s):
    """(intro text, frame text) for a section: the body lines; then the notebook line, fill-ins, and word bank."""
    intro = "\n".join(s["body"])
    frame = list(s.get("frame") or [])
    if frame and s.get("nb"):
        frame = [f"In your notebook, under “{s['nb']}”:"] + frame
    elif s.get("nb") and not s.get("table") and not frame:
        intro += f"\n(In your notebook, under “{s['nb']}”.)"
    b = bank_line(s)
    if b:
        frame.append(b)
    return intro, "\n".join(frame)


# ---------------------------------------------------------------------------
# Tables
# ---------------------------------------------------------------------------
def col_widths(head, rows, width):
    raw = [max(5, max(len(str(r[c])) for r in [head] + rows)) for c in range(len(head))]
    ws = [max(0.9, width * w / sum(raw)) for w in raw]
    return [w * width / sum(ws) for w in ws]


def table_h(head, rows, width, fs, row):
    ws = col_widths(head, rows, width)
    total = 0
    for r in [head] + rows:
        n = max(max(1, math.ceil(len(str(c)) / max(1, int(w * 72 / (0.60 * fs) - 1)))) for c, w in zip(r, ws))
        total += max(row, n * fs * 1.25 / 72 + 0.2)
    return total


def table_requests(oid, page, x, y, head, rows, width, fs, row):
    nr, nc = len(rows) + 1, len(head)
    ws = col_widths(head, rows, width)
    r = [{"createTable": {"objectId": oid, "rows": nr, "columns": nc, "elementProperties": props(page, x, y, width, row * nr)}}]
    for ci, w in enumerate(ws):
        r.append({"updateTableColumnProperties": {"objectId": oid, "columnIndices": [ci], "tableColumnProperties": {
            "columnWidth": {"magnitude": e(w), "unit": "EMU"}}, "fields": "columnWidth"}})
    for ri, line in enumerate([head] + rows):
        for ci, txt in enumerate(line):
            if not txt:
                continue
            loc = {"rowIndex": ri, "columnIndex": ci}
            r.append({"insertText": {"objectId": oid, "cellLocation": loc, "insertionIndex": 0, "text": str(txt)}})
            color = WHITE if ri == 0 else INK
            r.append({"updateTextStyle": {"objectId": oid, "cellLocation": loc, "textRange": {"type": "ALL"}, "style": {
                "fontFamily": FONT, "fontSize": {"magnitude": fs, "unit": "PT"}, "bold": ri == 0 or ci == 0,
                "foregroundColor": {"opaqueColor": {"rgbColor": color}}}, "fields": "fontFamily,fontSize,bold,foregroundColor"}})
    r.append({"updateTableCellProperties": {"objectId": oid, "tableRange": {"location": {"rowIndex": 0, "columnIndex": 0}, "rowSpan": 1, "columnSpan": nc},
                                           "tableCellProperties": {"tableCellBackgroundFill": {"solidFill": {"color": {"rgbColor": BLUE}}}},
                                           "fields": "tableCellBackgroundFill.solidFill.color"}})
    if nr > 1:
        r.append({"updateTableCellProperties": {"objectId": oid, "tableRange": {"location": {"rowIndex": 1, "columnIndex": 0}, "rowSpan": nr - 1, "columnSpan": nc},
                                               "tableCellProperties": {"tableCellBackgroundFill": {"solidFill": {"color": {"rgbColor": WHITE}}}},
                                               "fields": "tableCellBackgroundFill.solidFill.color"}})
    r.append({"updateTableRowProperties": {"objectId": oid, "rowIndices": list(range(nr)), "tableRowProperties": {
        "minRowHeight": {"magnitude": e(row), "unit": "EMU"}}, "fields": "minRowHeight"}})
    return r


BASE = 3000000  # Slides stores every shape at a 3,000,000 EMU square base size and scales it


def move(oid, base_w, base_h, x, y, w, h):
    """Place a shape at x, y (in) with width w and height h (in). base_w/base_h are unused: the API's base is 3,000,000 EMU."""
    return {"updatePageElementTransform": {"objectId": oid, "applyMode": "ABSOLUTE", "transform": {
        "scaleX": round(e(w) / BASE, 5), "scaleY": round(e(h) / BASE, 5), "translateX": e(x), "translateY": e(y), "unit": "EMU"}}}


def replace(page, token, text):
    return {"replaceAllText": {"containsText": {"text": "{{%s}}" % token, "matchCase": True}, "replaceText": text, "pageObjectIds": [page]}}


# ---------------------------------------------------------------------------
# One day's deck: requests that turn a copy of the template into the deck
# ---------------------------------------------------------------------------
def kick_width(text, pt=12):
    return min(8.0, max(2.2, len(text) * pt * 0.66 / 72 + 0.5))


def deck(day):
    d = U.DAY[day]
    foot = f"Unit 2.2 · Day {day} · {d['title']}"
    p = f"u{day}"
    reqs, order, warn = [], ["tpl_title", "tpl_nb", "tpl_targets"], []

    # --- title slide
    t = "tpl_title"
    sub = (f"Today's target ({d['targets'][0]}): {U.TARGET[d['targets'][0]][3]}" if len(d["targets"]) == 1 and d["kind"] != "review"
           else f"Today's focus: {d['focus']}")
    if d["kind"] == "csa":
        sub = "HS-LS3-2: Inherited Instructions · 40 minutes"
    reqs += [replace(t, "KICK", f"UNIT 2.2 · INHERITED INSTRUCTIONS · {U.STANDARD}"), replace(t, "TITLE", f"Day {day}: {d['title']}"),
             replace(t, "SUB", sub), replace(t, "EMO", "🐶" if day < 11 else "📝"), replace(t, "FOOT", foot)]
    reqs.append(move(f"{t}_kick", 4.6, 0.36, 0.5, 0.72, kick_width(f"UNIT 2.2 · INHERITED INSTRUCTIONS · {U.STANDARD}"), 0.36))
    tfs = 36 if lines_needed(f"Day {day}: {d['title']}", 6.3, 38) <= 3 else 30
    reqs.append({"updateTextStyle": {"objectId": f"{t}_title", "textRange": {"type": "ALL"}, "style": {"fontSize": {"magnitude": tfs, "unit": "PT"}}, "fields": "fontSize"}})
    sfs = fit(sub, 8.8, 1.7, (24, 22, 20, 18))
    reqs.append({"updateTextStyle": {"objectId": f"{t}_sub", "textRange": {"type": "ALL"}, "style": {"fontSize": {"magnitude": sfs, "unit": "PT"}}, "fields": "fontSize"}})

    # --- notebook setup (none for the CSA)
    n = "tpl_nb"
    if d["kind"] == "csa":
        order.remove("tpl_nb")
        reqs.append({"deleteObject": {"objectId": n}})
    cards = [(s["nb"], s["nbnote"]) for s in d["sections"] if s.get("nb")]
    if d["cfa"]:
        cards.append((f"CFA {d['cfa']}", "On Canvas, from memory. No notebook page."))
    assert len(cards) <= 8, (day, len(cards))
    if d["kind"] != "csa":
        reqs += [replace(n, "TITLE", f"Day {day}: {d['title']}"), replace(n, "FOCUS", f"Focus question: {d['focus']}")]
        for i in range(8):
            if i < len(cards):
                reqs += [replace(n, f"H{i + 1}", cards[i][0]), replace(n, f"D{i + 1}", cards[i][1])]
            else:
                reqs.append({"deleteObject": {"objectId": f"{n}_c{i + 1}"}})
    # --- learning targets
    g = "tpl_targets"
    today = set(d["targets"])
    shown = [t_ for t_ in U.TARGETS if t_[4] == "Priority" or t_[0] in today]  # supporting targets only on their own lessons
    lines = [f"{'★ ' if t_[0] in today else ''}{t_[0]}{' (supporting)' if t_[4] == 'Supporting' else ''}: {t_[3]}" for t_ in shown]
    body = "\n".join(lines)
    reqs += [replace(g, "KICK", f"UNIT 2.2 · {U.STANDARD} · LEARNING TARGETS"), replace(g, "TITLE", "Learning targets"),
             replace(g, "EMO", "🎯"), replace(g, "FOOT", foot), replace(g, "BODY", body)]
    reqs.append(move(f"{g}_kick", 3.6, 0.36, 0.5, 0.27, kick_width(f"UNIT 2.2 · {U.STANDARD} · LEARNING TARGETS"), 0.36))
    start = 0
    for line, t_ in zip(lines, shown):
        if t_[0] in today:
            reqs.append({"updateTextStyle": {"objectId": f"{g}_body", "textRange": {"type": "FIXED_RANGE", "startIndex": start, "endIndex": start + len(line)},
                                             "style": {"bold": True, "foregroundColor": {"opaqueColor": {"rgbColor": BLUE}}}, "fields": "bold,foregroundColor"}})
        start += len(line) + 1
    gfs = fit(body, BODY_W, 3.2, (13, 12, 11), space=5)
    reqs.append({"updateTextStyle": {"objectId": f"{g}_body", "textRange": {"type": "ALL"}, "style": {"fontSize": {"magnitude": gfs, "unit": "PT"}}, "fields": "fontSize"}})

    # --- content slides: one per section, then the CFA slide
    items = []
    for s in d["sections"]:
        items.append(("section", s))
    if d["cfa"]:
        items.append(("cfa", None))
    dup = []
    for k, (kind, s) in enumerate(items, 1):
        sid = f"{p}_s{k:02d}"
        order.append(sid)
        dup.append(sid)
        body_id, frame_id, card_id = f"{sid}_body", f"{sid}_frame", f"{sid}_card"
        reqs.append({"duplicateObject": {"objectId": "tpl_content", "objectIds": {
            "tpl_content": sid, "tpl_content_body": body_id, "tpl_content_frame": frame_id,
            "tpl_content_kick": f"{sid}_kick", "tpl_content_title": f"{sid}_title"}}})
        if kind == "cfa":
            tid = d["cfa"]
            kick, title, emo = "EXIT TICKET · 6 MIN · ON YOUR OWN, FROM MEMORY", f"Exit ticket: CFA {tid}", "🎟️"
            intro = (f"Open Canvas: {Q.CFA_TITLE[tid]} (5 questions).\nTarget: {U.TARGET[tid][3]}\n"
                     "Below a B (fewer than 4 of 5)? A review for this target opens for you.")
            frame = ""
            tbl = None
        else:
            kick, title, emo = kicker(s), s["title"], EMOJI.get(s["label"], "📘")
            intro, frame = section_texts(s)
            tbl = s.get("table")
        reqs += [replace(sid, "KICK", kick), replace(sid, "TITLE", title), replace(sid, "EMO", emo), replace(sid, "FOOT", foot)]
        reqs.append(move(f"{sid}_kick", 3.6, 0.36, 0.5, 0.27, kick_width(kick), 0.36))
        tfs = 30 if lines_needed(title, 8.1, 30) == 1 else 24
        if lines_needed(title, 8.1, tfs) > 1:
            tfs = 20
            if lines_needed(title, 8.1, tfs) > 1:
                warn.append(f"day {day} slide {k}: long title '{title}'")
        reqs.append({"updateTextStyle": {"objectId": f"{sid}_title", "textRange": {"type": "ALL"}, "style": {"fontSize": {"magnitude": tfs, "unit": "PT"}}, "fields": "fontSize"}})
        if tbl is None:
            if frame:
                intro_full = intro + "\n" + frame
            else:
                intro_full = intro
            fs = fit(intro_full, BODY_W, BODY_H)
            reqs += [replace(sid, "BODY", intro_full), {"deleteObject": {"objectId": frame_id}},
                     {"updateTextStyle": {"objectId": body_id, "textRange": {"type": "ALL"}, "style": {"fontSize": {"magnitude": fs, "unit": "PT"}}, "fields": "fontSize"}}]
            reqs += style_ranges(body_id, bold_ranges(intro_full))
            if "Word bank:" in intro_full:
                a = intro_full.index("Word bank:")
                reqs += style_ranges(body_id, [(a, a + len("Word bank:"))], color=ORANGE)
        else:
            head, rows = tbl
            ifs = fit(intro, BODY_W, 1.3, (14, 13, 12), space=4)
            ih = text_h(intro, BODY_W, ifs, 4)
            tfs_ = 12 if len(rows) <= 3 else 11 if len(rows) <= 5 else 10
            row = 0.2
            y_tab = BODY_Y + ih
            avail = 5.15 - y_tab
            th_full = table_h(head, rows, BODY_W, tfs_, row)
            frs = 12
            need_below = text_h(frame, BODY_W, frs, 3) if frame else 0
            if not frame or th_full + 0.1 + need_below <= avail:
                tw, fx, fy, fw, fh = BODY_W, BODY_X, y_tab + th_full + 0.1, BODY_W, max(0.4, avail - th_full - 0.1)
                th = th_full
            else:  # table on the left, sentence frame on the right
                tw = 5.2 if len(head) <= 4 else 5.6
                th = table_h(head, rows, tw, tfs_, row)
                fx, fy, fw, fh = BODY_X + tw + 0.2, y_tab, BODY_W - tw - 0.2, avail
                frs = fit(frame, fw, fh, (12, 11, 10.5, 10), space=3)
                if th > avail + 0.05 or text_h(frame, fw, frs, 3) > fh + 0.05:
                    warn.append(f"day {day} slide {k} ({title}): table {th:.2f}/{avail:.2f}in, frame {text_h(frame, fw, frs, 3):.2f}/{fh:.2f}in")
            reqs += [replace(sid, "BODY", intro), replace(sid, "FRAME", frame)]
            reqs.append(move(body_id, BODY_W, BODY_H, BODY_X, BODY_Y, BODY_W, max(0.4, ih)))
            reqs.append({"updateTextStyle": {"objectId": body_id, "textRange": {"type": "ALL"}, "style": {"fontSize": {"magnitude": ifs, "unit": "PT"}}, "fields": "fontSize"}})
            reqs += style_ranges(body_id, bold_ranges(intro))
            reqs += table_requests(f"{sid}_tbl", sid, BODY_X, y_tab, head, rows, tw, tfs_, row)
            if frame:
                reqs.append(move(frame_id, BODY_W, FRAME_H, fx, fy, fw, fh))
                reqs.append({"updateTextStyle": {"objectId": frame_id, "textRange": {"type": "ALL"}, "style": {"fontSize": {"magnitude": frs, "unit": "PT"}}, "fields": "fontSize"}})
                reqs += style_ranges(frame_id, bold_ranges(frame))
                if "Word bank:" in frame:
                    a_ = frame.index("Word bank:")
                    reqs += style_ranges(frame_id, [(a_, a_ + len("Word bank:"))], color=ORANGE)
            else:
                reqs.append({"deleteObject": {"objectId": frame_id}})
    # delete the template content slide, then put the slides in order (one move each)
    reqs.append({"deleteObject": {"objectId": "tpl_content"}})
    for i, sid in enumerate(order):
        reqs.append({"updateSlidesPosition": {"slideObjectIds": [sid], "insertionIndex": i}})
    return reqs, warn


# ---------------------------------------------------------------------------
# Slides with graphics from the original Genetics Notes deck (Day 3). Slides is built from scratch (no template copy).
# Image urls are expiring docs.google.com/slides-images-rt links: read them from the original deck just before use.
# ---------------------------------------------------------------------------
ORIG_DECK = "1zLmg_vu7MzxnbCe4xbBWE76xxyEMa8TrHC_Iuja29UM"
# object id in the original deck -> (x, y, w, h) in its 20 x 11.25 in page
ORIG = {
    "g1ebb2efc9c9_2_96": (6.37, 6.89, 7.15, 3.8), "g1ebb2efc9c9_2_105": (0.22, 3.46, 8.02, 5.22),
    "g1ebb2efc9c9_2_112": (0.62, 4.92, 3.42, 5.63), "g1ebb2efc9c9_2_113": (2.95, 4.86, 4.55, 5.75),
    "g1ebb2efc9c9_2_114": (7.67, 4.91, 2.22, 3.26), "g1ebb2efc9c9_2_115": (9.64, 4.93, 5.29, 5.95),
    "g1ebb2efc9c9_2_116": (15.3, 4.88, 3.95, 5.37), "g1ebb2efc9c9_2_128": (1.41, 2.63, 2.17, 8.11),
    "g1ebb2efc9c9_2_215": (0.1, 1.17, 20.0, 3.09), "g1ebb2efc9c9_2_221": (3.84, 6.69, 2.98, 3.5),
    "g1ebb2efc9c9_2_222": (6.95, 7.06, 9.6, 2.19), "g1ebb2efc9c9_2_231": (3.84, 6.69, 2.98, 3.5),
    "g1ebb2efc9c9_2_232": (6.95, 7.06, 9.6, 2.19), "g1ebb2efc9c9_2_239": (7.56, 8.18, 10.15, 2.37),
    "g1ebb2efc9c9_2_277": (1.62, 4.54, 8.02, 5.62), "g1ebb2efc9c9_2_278": (10.12, 4.54, 8.1, 5.62),
    "g1ebb2efc9c9_2_289": (3.05, 8.3, 13.89, 1.98),
}


def group_box(ids, x, y, w):
    """Height of a group of original images scaled to total width w, and each image's (x, y, w, h) on the new slide."""
    bx = min(ORIG[i][0] for i in ids)
    by = min(ORIG[i][1] for i in ids)
    bw = max(ORIG[i][0] + ORIG[i][2] for i in ids) - bx
    bh = max(ORIG[i][1] + ORIG[i][3] for i in ids) - by
    k = w / bw
    return bh * k, [(i, x + (ORIG[i][0] - bx) * k, y + (ORIG[i][1] - by) * k, ORIG[i][2] * k, ORIG[i][3] * k) for i in ids]


def picture(oid, page, url, x, y, w, h):
    return [{"createImage": {"objectId": oid, "url": url, "elementProperties": props(page, x, y, w, h)}}]


CHROME_PARTS = ("card", "kick", "emo", "title", "bar", "foot")


def image_slide(day, k, s, index, urls):
    """One section slide with original graphics. Returns (slide id, requests, warnings)."""
    d = U.DAY[day]
    foot = f"Unit 2.2 · Day {day} · {d['title']}"
    sid = f"u{day}g_s{k:02d}"
    warn = []
    kick, title, emo = kicker(s), s["title"], EMOJI.get(s["label"], "📘")
    tpl = f"u{day}g_tpl"
    r = [{"duplicateObject": {"objectId": tpl, "objectIds": {tpl: sid, **{f"{tpl}_{p}": f"{sid}_{p}" for p in CHROME_PARTS}}}}]
    r += [replace(sid, "KICK", kick), replace(sid, "TITLE", title), replace(sid, "EMO", emo), replace(sid, "FOOT", foot),
          move(f"{sid}_kick", 3.6, 0.36, 0.5, 0.27, kick_width(kick), 0.36)]
    tfs = 30 if lines_needed(title, 8.1, 30) == 1 else 24
    r.append({"updateTextStyle": {"objectId": f"{sid}_title", "textRange": {"type": "ALL"}, "style": {"fontSize": {"magnitude": tfs, "unit": "PT"}}, "fields": "fontSize"}})
    img = s.get("img") or {}
    n = 0

    def put(ids, x, y, w):
        nonlocal n
        h, items = group_box(ids, x, y, w)
        for i, ix, iy, iw, ih in items:
            n += 1
            r.extend(picture(f"{sid}_img{n}", sid, urls[i], ix, iy, iw, ih))
        return h

    if s.get("layout") == "domrec":
        put([img["banner"]], 2.4, 1.82, 5.2)
        top = 2.75
        bank = bank_line(s)
        lines = s["frame"]
        for col, (txt, ids, x) in enumerate([(lines[0], img["dom"], 0.68), (lines[1], img["rec"], 5.12)]):
            oid = f"{sid}_col{col + 1}"
            r += shape(oid, sid, "TEXT_BOX", x, top, 4.2, 0.85, text=txt, size=12, color=INK, space_below=3)
            end = txt.index(":") + 1
            r += style_ranges(oid, [(0, end)], color=BLUE)
            put(ids, x + 0.2, top + 0.9, 3.7)
        oid = f"{sid}_bank"
        txt = f"In your notebook, under “{s['nb']}”. {bank}"
        r += shape(oid, sid, "TEXT_BOX", 0.68, 4.62, 8.64, 0.45, text=txt, size=11, color=INK)
        a = txt.index("Word bank:")
        r += style_ranges(oid, [(a, a + len("Word bank:"))], color=ORANGE)
        return sid, r, warn

    if s.get("table") and not img:  # intro on top, table on the left, notebook line + sentence frame + word bank on the right
        head, rows = s["table"]
        intro, frame = section_texts(s)
        r += shape(f"{sid}_intro", sid, "TEXT_BOX", BODY_X, BODY_Y, BODY_W, 0.8, text=intro, size=14, color=INK, space_below=4)
        r += table_requests(f"{sid}_tbl", sid, BODY_X, 2.85, head, rows, 4.3, 12, 0.32)
        r += shape(f"{sid}_text", sid, "TEXT_BOX", 5.3, 2.8, 4.0, 2.2, text=frame, size=12, color=INK, space_below=4)
        a = frame.index("Word bank:")
        r += style_ranges(f"{sid}_text", bold_ranges(frame) + [(0, frame.index(":") + 1)] + [(a, a + len("Word bank:"))])
        r += style_ranges(f"{sid}_text", [(a, a + len("Word bank:"))], color=ORANGE)
        return sid, r, warn
    h = 0
    if img:
        h = put(img["ids"], img["x"], img["y"], img["w"])
        if img["y"] + h > 5.1:
            warn.append(f"day {day} {title}: picture ends at {img['y'] + h:.2f} in")
    intro, frame = section_texts(s)
    text = "\n".join(t for t in (intro, frame) if t)
    tx, tw = s.get("text_x", BODY_X), s.get("text_w", BODY_W)
    th = 3.2 if not img or tw < BODY_W or img["y"] < 2.8 else img["y"] - BODY_Y - 0.05
    if s.get("big"):
        th = 1.25
    fs = fit(text, tw, th, (16, 15, 14, 13, 12, 11), space=5)
    if text_h(text, tw, fs, 5) > th:
        warn.append(f"day {day} {title}: text {text_h(text, tw, fs, 5):.2f}/{th:.2f} in at {fs} pt")
    oid = f"{sid}_text"
    r += shape(oid, sid, "TEXT_BOX", tx, BODY_Y, tw, th, text=text, size=fs, color=INK, space_below=5)
    if s.get("big"):
        r += shape(f"{sid}_big", sid, "TEXT_BOX", BODY_X, 3.15, BODY_W, 1.0, text=s["big"], size=44, bold=True, color=BLUE, align="CENTER")
        r += shape(f"{sid}_note", sid, "TEXT_BOX", BODY_X, 4.25, BODY_W, 0.6, text=s["note"], size=13, color=MUTED, align="CENTER")
    r += style_ranges(oid, bold_ranges(text))
    if "Word bank:" in text:
        a = text.index("Word bank:")
        r += style_ranges(oid, [(a, a + len("Word bank:"))], color=ORANGE)
    return sid, r, warn


def rebuild_with_images(day, urls, old_ids, only=None, start=3):
    """Requests that replace the section slides (everything after the learning-targets slide) of a built deck."""
    d = U.DAY[day]
    tpl = f"u{day}g_tpl"
    reqs, warn = [{"deleteObject": {"objectId": o}} for o in old_ids], []
    wanted = [s for k, s in enumerate(d["sections"], 1) if not only or k in only]
    use_tpl = any(not s.get("strip") for s in wanted)
    if use_tpl:
        reqs += [new_slide(tpl, start)] + chrome(tpl)
    sids = []
    for k, s in enumerate(d["sections"], 1):
        if only and k not in only:
            continue
        sid, rr, w = (mutation_slide if s.get("strip") else image_slide)(day, k, s, start, urls)
        reqs += rr
        warn += w
        sids.append(sid)
    if use_tpl:
        reqs.append({"deleteObject": {"objectId": tpl}})
    reqs += [{"updateSlidesPosition": {"slideObjectIds": [sid], "insertionIndex": start + i}} for i, sid in enumerate(sids)]
    return reqs, warn



# ---------------------------------------------------------------------------
# Day 7: the "Effects of Mutations" page from the original Genetics Notes deck. The deck shows it cropped; the API cannot crop, so
# the whole page is placed enlarged and everything around the window is covered with page-colored rectangles.
# ---------------------------------------------------------------------------
MUT_NATURAL = (22.17, 21.52)          # natural size (in, at the original deck's scale) of the page image
MUT_L, MUT_R = 0.06423206, 0.07243377  # horizontal crop used by the original slides 21 to 25
# original slides: displayed rect (x, y, w, h in the 20 in page), top and bottom crop, and each blank box (x, y, w, h)
MUT_SLIDES = {
    22: dict(rect=(0.428, 3.82, 19.14, 3.226), top=0.40058172, bottom=0.44948876,
             boxes=[(11.24, 4.86, 1.82, 0.58), (6.95, 5.33, 2.83, 0.58), (12.25, 5.81, 1.66, 0.58)]),   # effect, amino acid, codons
    23: dict(rect=(0.428, 3.549, 19.14, 3.689), top=0.52881366, bottom=0.29972738, boxes=[(9.74, 5.62, 2.63, 0.58)]),   # different
    24: dict(rect=(0.428, 3.549, 19.14, 3.689), top=0.67410797, bottom=0.15443309,
             boxes=[(2.25, 5.28, 1.32, 0.58), (1.46, 5.89, 2.66, 0.58)]),                                 # mRNA, backwards
    25: dict(rect=(0.428, 3.549, 19.14, 3.689), top=0.8077873, bottom=0.020762578,
             boxes=[(15.59, 4.62, 1.32, 0.58), (10.91, 5.13, 2.93, 0.58)]),                               # stop, terminates
}


def mut_frac(slide, x, y):
    """Position (x, y in the original slide) as fractions (u, v) of the whole page image."""
    m = MUT_SLIDES[slide]
    ox, oy, ow, oh = m["rect"]
    u = MUT_L + (x - ox) / ow * (1 - MUT_L - MUT_R)
    v = m["top"] + (y - oy) / oh * (1 - m["top"] - m["bottom"])
    return u, v


def mutation_slide(day, k, s, index, urls):
    """Section slide showing a window of the Effects of Mutations page with numbered blank boxes. Returns (id, requests, warnings)."""
    d = U.DAY[day]
    foot = f"Unit 2.2 · Day {day} · {d['title']}"
    sid = f"u{day}g_s{k:02d}"
    spec = s["strip"]
    wins = spec["slides"]
    v0 = MUT_SLIDES[wins[0]]["top"]
    v1 = 1 - MUT_SLIDES[wins[-1]]["bottom"]
    X, Y, Wd = 1.3, 1.85, 7.4
    kk = Wd / (MUT_NATURAL[0] * (1 - MUT_L - MUT_R))
    nw, nh = MUT_NATURAL[0] * kk, MUT_NATURAL[1] * kk
    Hd = (v1 - v0) * nh
    kick, title, emo = kicker(s), s["title"], EMOJI.get(s["label"], "📘")
    items = chrome(sid)
    r = [new_slide(sid, index), items[0]]
    r += shape(f"{sid}_card", sid, "RECTANGLE", 0.5, 1.75, 9.0, 3.35, fill=WHITE)
    r += picture(f"{sid}_img", sid, urls[spec["url_id"]], X - MUT_L * nw, Y - v0 * nh, nw, nh)
    n = 0

    def cover(x, y, w, h, color):
        nonlocal n
        n += 1
        return shape(f"{sid}_cv{n}", sid, "RECTANGLE", x, y, w, h, fill=color)

    for x, y, w, h in [(0, 0, 10, 1.75), (0, 5.1, 10, 0.525), (0, 1.75, 0.5, 3.35), (9.5, 1.75, 0.5, 3.35)]:
        r += cover(x, y, w, h, LIGHT)
    for x, y, w, h in [(0.5, 1.75, 9.0, Y - 1.75), (0.5, Y, X - 0.5, Hd), (X + Wd, Y, 9.5 - X - Wd, Hd), (0.5, Y + Hd, 9.0, 5.1 - Y - Hd)]:
        r += cover(x, y, w, h, WHITE)
    num = 0
    for sl in wins:
        for bx, by, bw, bh in MUT_SLIDES[sl]["boxes"]:
            u, v = mut_frac(sl, bx, by)
            u2, _ = mut_frac(sl, bx + bw, by)
            _, v2 = mut_frac(sl, bx, by + bh)
            num += 1
            oid = f"{sid}_bx{num}"
            r += shape(oid, sid, "ROUND_RECTANGLE", X + (u - MUT_L) / (1 - MUT_L - MUT_R) * Wd, Y + (v - v0) * nh,
                       (u2 - u) / (1 - MUT_L - MUT_R) * Wd, (v2 - v) * nh, fill=ORANGE, text=str(num), size=10, bold=True, color=NAVY,
                       align="CENTER", valign="MIDDLE")
    parts = [x for x in items[3:] if True]  # kick, emo, title, bar, foot (the card's two requests are items[1:3])
    r += parts
    r += [replace(sid, "KICK", kick), replace(sid, "TITLE", title), replace(sid, "EMO", emo), replace(sid, "FOOT", foot),
          move(f"{sid}_kick", 3.6, 0.36, 0.5, 0.27, kick_width(kick), 0.36)]
    tfs = 30 if lines_needed(title, 8.1, 30) == 1 else 24
    if lines_needed(title, 8.1, tfs) > 1:
        tfs = 20
    r.append({"updateTextStyle": {"objectId": f"{sid}_title", "textRange": {"type": "ALL"}, "style": {"fontSize": {"magnitude": tfs, "unit": "PT"}}, "fields": "fontSize"}})
    txt = f"In your notebook, under “{s['nb']}”: write the missing words 1 to {num}.  {bank_line(s)}"
    oid = f"{sid}_text"
    r += shape(oid, sid, "TEXT_BOX", 0.68, Y + Hd + 0.05, 8.64, 0.6, text=txt, size=11, color=INK)
    a = txt.index("Word bank:")
    r += style_ranges(oid, [(0, txt.index(":") + 1), (a, a + len("Word bank:"))])
    r += style_ranges(oid, [(a, a + len("Word bank:"))], color=ORANGE)
    warn = [] if Y + Hd + 0.65 <= 5.12 else [f"day {day} {title}: text ends at {Y + Hd + 0.65:.2f} in"]
    return sid, r, warn

if __name__ == "__main__":
    what = sys.argv[1]
    if what == "template":
        print(json.dumps(template_requests(), ensure_ascii=False, separators=(",", ":")))
    elif what == "imgdeck":  # python3 slides.py imgdeck DAY urls.json old_id,old_id,...
        only = {int(x) for x in sys.argv[5].split(",")} if len(sys.argv) > 5 else None  # optional: section numbers to build
        start = int(sys.argv[6]) if len(sys.argv) > 6 else 3  # optional: slide index for the first new slide
        r, w = rebuild_with_images(int(sys.argv[2]), json.load(open(sys.argv[3])), sys.argv[4].split(",") if sys.argv[4] else [], only, start)
        for x in w:
            print("WARN", x, file=sys.stderr)
        print(json.dumps(r, ensure_ascii=False, separators=(",", ":")))
    elif what == "deck":
        r, w = deck(int(sys.argv[2]))
        for x in w:
            print("WARN", x, file=sys.stderr)
        print(json.dumps(r, ensure_ascii=False, separators=(",", ":")))
