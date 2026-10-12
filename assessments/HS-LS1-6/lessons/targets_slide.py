"""Requests that add a "Learning targets" slide to a Unit 1.3 deck.

The slide lists all six unit targets (ID, I-can statement) and highlights the
day's target(s) with a TODAY tag. It is inserted as slide 3, right after the
notebook set-up example (slide 2), so the Canvas pages' "slide 2" note still holds.

  python3 targets_slide.py <day>      # prints the JSON request list
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import unit13_bank as U  # noqa: E402
import unit13_lessons as L  # noqa: E402

EMU = 914400
INK = {"red": 0.137, "green": 0.224, "blue": 0.173}
MUTED = {"red": 0.43, "green": 0.46, "blue": 0.43}
TAN = {"red": 0.9098, "green": 0.8627, "blue": 0.7765}
TODAY = {"red": 1.0, "green": 0.84, "blue": 0.4}
WHITE = {"red": 1, "green": 1, "blue": 1}

# day -> (layout id for a content slide, scale: 1 for 10 in wide decks, 4/3 for 13.33 in)
DECKS = {
    1: ("h1bb456a1bbc0def0_0_244", 1), 2: ("h287605ecd2867468_0_216", 1), 3: ("h5a55907624f9106e_0_258", 1),
    4: ("h287605ecd2867468_0_216", 1), 5: ("h146d7118798b7cf1_0_230", 1), 6: ("p18", 4 / 3),
    7: ("p12", 4 / 3), 8: ("p14", 4 / 3), 9: ("h287605ecd2867468_0_216", 1), 10: ("h287605ecd2867468_0_216", 1),
}


def deck_id(d):
    return re.search(r"/d/([\w-]+)/", d["slides"][1]).group(1)


def requests(day):
    d = next(x for x in L.DAYS if x["day"] == day)
    layout, k = DECKS[day]
    sid = f"lt_d{day}_slide"
    n = [0]

    def oid():
        n[0] += 1
        return f"lt_d{day}_{n[0]:02d}"

    def props(x, y, w, h):
        return {"pageObjectId": sid,
                "size": {"width": {"magnitude": int(w * k * EMU), "unit": "EMU"},
                         "height": {"magnitude": int(h * k * EMU), "unit": "EMU"}},
                "transform": {"scaleX": 1, "scaleY": 1, "translateX": int(x * k * EMU),
                              "translateY": int(y * k * EMU), "unit": "EMU"}}

    def style(size, bold, color):
        return {"fontFamily": "Calibri", "fontSize": {"magnitude": round(size * k, 1), "unit": "PT"},
                "bold": bold, "foregroundColor": {"opaqueColor": {"rgbColor": color}}}

    # Create after the "Today" slide (3rd slide), whose master owns the layout, then move it to slide 3.
    reqs = [{"createSlide": {"objectId": sid, "insertionIndex": 3, "slideLayoutReference": {"layoutId": layout}}}]

    def text(x, y, w, h, s, size, bold, color):
        o = oid()
        reqs.extend([
            {"createShape": {"objectId": o, "shapeType": "TEXT_BOX", "elementProperties": props(x, y, w, h)}},
            {"insertText": {"objectId": o, "insertionIndex": 0, "text": s}},
            {"updateTextStyle": {"objectId": o, "textRange": {"type": "ALL"}, "style": style(size, bold, color),
                                 "fields": "fontFamily,fontSize,bold,foregroundColor"}},
        ])

    today = set(d["targets"])
    all_today = len(today) == len(U.TARGETS)
    text(0.5, 0.28, 9.0, 0.3, "UNIT 1.3 · SUGAR TO STRUCTURES · HS-LS1-6", 11, True, MUTED)
    text(0.5, 0.52, 9.0, 0.55, "Learning targets", 28, True, INK)
    sub = ("Today: all six targets." if all_today else
           "Today's target" + ("s" if len(today) > 1 else "") + ": " + ", ".join(t for t in d["targets"]) + " (highlighted)")
    text(0.5, 1.07, 9.0, 0.3, sub, 13, False, INK)

    tbl = oid()
    rows = len(U.TARGETS) + 1
    reqs.append({"createTable": {"objectId": tbl, "rows": rows, "columns": 3, "elementProperties": props(0.5, 1.45, 9.0, 3.5)}})
    for c, w in enumerate((1.0, 7.0, 1.0)):
        reqs.append({"updateTableColumnProperties": {"objectId": tbl, "columnIndices": [c],
                     "tableColumnProperties": {"columnWidth": {"magnitude": int(w * k * EMU), "unit": "EMU"}},
                     "fields": "columnWidth"}})

    def cell(r, c, s, size, bold):
        loc = {"rowIndex": r, "columnIndex": c}
        reqs.append({"insertText": {"objectId": tbl, "cellLocation": loc, "insertionIndex": 0, "text": s}})
        reqs.append({"updateTextStyle": {"objectId": tbl, "cellLocation": loc, "textRange": {"type": "ALL"},
                     "style": style(size, bold, INK), "fields": "fontFamily,fontSize,bold,foregroundColor"}})

    def fill(r, color):
        reqs.append({"updateTableCellProperties": {"objectId": tbl,
                     "tableRange": {"location": {"rowIndex": r, "columnIndex": 0}, "rowSpan": 1, "columnSpan": 3},
                     "tableCellProperties": {"tableCellBackgroundFill": {"solidFill": {"color": {"rgbColor": color}}}},
                     "fields": "tableCellBackgroundFill.solidFill.color"}})

    for c, s in enumerate(("Target", "I can…", "")):
        if s:
            cell(0, c, s, 13, True)
    fill(0, TAN)
    for r, (tid, _name, _dok, ican) in enumerate(U.TARGETS, 1):
        on = tid in today
        cell(r, 0, tid, 13, True)
        cell(r, 1, ican, 13, on)
        if on:
            cell(r, 2, "★ TODAY", 12, True)
        fill(r, TODAY if on else WHITE)
    reqs.append({"updateTableRowProperties": {"objectId": tbl, "rowIndices": list(range(rows)),
                 "tableRowProperties": {"minRowHeight": {"magnitude": int(0.44 * k * EMU), "unit": "EMU"}},
                 "fields": "minRowHeight"}})
    footer = f"Day {d['day']} · {d['title']}" if not d["lesson"].startswith("Lesson") else f"{d['lesson']} · {d['title']}"
    text(0.5, 5.18, 9.0, 0.3, footer, 10, False, MUTED)
    reqs.append({"updateSlidesPosition": {"slideObjectIds": [sid], "insertionIndex": 2}})
    return deck_id(d), reqs


if __name__ == "__main__":
    pid, reqs = requests(int(sys.argv[1]))
    print(pid)
    print(json.dumps(reqs, ensure_ascii=False, separators=(",", ":")))
