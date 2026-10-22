"""Notebook setup slide for Unit 2.2 decks, same layout as Unit 2.1's (HS-LS1-6/lessons/notebook_slides.py): a two-page notebook
spread on notebook paper, Boogaloo title, Calibri focus question, Handlee headings, ruled answer lines, small tables, dashed boxes.
Blue headings and orange dashed boxes for the Unit 2.2 theme. One block per notebook section, in notebook order.

  python3 nbslide.py N      # Slides requests that replace slide 2 (tpl_nb) of Day N's deck with the new notebook slide
"""

import json
import sys

import content as U

EMU = 914400
BG = "http://res.publicdomainfiles.com/pdf_view/83/13939457415622.png"
BLUE = {"red": 0.1176, "green": 0.3725, "blue": 0.749}
ORANGE = {"red": 1.0, "green": 0.5412, "blue": 0.1216}
HEAD = {"red": 0.0431, "green": 0.1765, "blue": 0.3608}
HDR = {"red": 0.8118, "green": 0.8784, "blue": 0.9804}
GREY = {"red": 0.42, "green": 0.46, "blue": 0.55}
BLACK = {"red": 0, "green": 0, "blue": 0}
WHITE = {"red": 1, "green": 1, "blue": 1}
LEFT_X, RIGHT_X, PAGE_W = 0.22, 5.09, 4.45
BOTTOM = 5.2
LEFT_TOP, RIGHT_TOP = 1.02, 0.62

SKETCH = ("sketch", "draw", "model", "glue")
# Days whose sections need a hand-made block (nb heading -> blocks after the heading)
OVERRIDE = {
    (9, "Check my CFAs"): [("table", ["Target", "My CFA score", "Review?"],
                            [["LS3-2.1", "", ""], ["LS3-2.2", "", ""], ["LS3-2.3", "", ""], ["LS3-2.4", "", ""]], [1.1, 1.65, 1.7], 9, 0.27)],
    (9, "Reviews and make-up work"): [("lines", 3)],
    (9, "Self-check"): [("table", ["Target", "Rating 1 to 4"],
                         [["LS3-2.1 three sources", ""], ["LS3-2.2 sex cells and fertilization", ""],
                          ["LS3-2.3 copying errors and UV", ""], ["LS3-2.4 read data, make a claim", ""]], [2.9, 1.55], 9, 0.27)],
    (1, "My first model"): [("box", 1.25, "Draw: Parent 1, Parent 2, and two offspring. Use arrows to show information moving from "
                                          "the parents to the offspring. Label one shared trait and one different trait.")],
    (1, "Three possible explanations"): [("box", 0.8, "Three small sketch boxes: one idea in each.")],
    (10, "Fix my Day 1 model"): [("box", 1.2, "Redraw your Day 1 model. Add: new combinations, copying errors, mutations from the "
                                              "environment, and which changes are inherited.")],
    (5, "Build the female monster"): [("text", "Use Table 1 on your Monster Genetics sheet."), ("lines", 1)],
    (5, "Fill in the male monster"): [("text", "Use Table 2 on your Monster Genetics sheet."), ("lines", 1)],
    (6, "Punnett squares for the baby"): [("box", 0.95, "Draw the Punnett square for Skin color, Gg × Gg. Then make 5 more for "
                                                      "your traits (on your sheet).")],
    (4, "Punnett squares"): [("box", 0.95, "Draw a 2 × 2 Punnett square for Tt × Tt. Write the alleles on the top and the side.")],
    (4, "Genotype and phenotype"): [("lines", 2), ("box", 0.95, "Make a table: Genotype and Phenotype for TT, Tt, tt (TT is tall).\nThen draw two eyes. Color one blue and one brown.")],
    (4, "Homozygous and heterozygous"): [("box", 0.7, "Write CC, Ee, Gg, dd, AA, Hh. Color the homozygous ones green and the heterozygous ones orange."),
                                         ("lines", 1)],
    (3, "Genes make proteins make traits"): [("lines", 4)],
    (3, "Alleles"): [("box", 0.95, "Sketch a pair of chromosomes. Color each set of alleles a different color."), ("lines", 1)],
    (3, "Black or brown cats"): [("box", 0.7, "Draw three cat heads: BB, Bb, bb. Color each one to show its coat."), ("lines", 1)],
}


def row_h(fs, min_h):
    return max(min_h or 0, 0.11 + fs * 0.0175)


def block_h(b):
    k = b[0]
    if k == "h":
        return 0.34
    if k == "lines":
        return 0.22 * b[1] + 0.06
    if k == "text":
        return 0.3
    if k == "box":
        return b[1] + 0.08
    if k == "table":
        _, head, rows, widths, fs, min_h = b
        return row_h(fs, None) + len(rows) * row_h(fs, min_h) + 0.1
    raise ValueError(k)


def widths_for(head, rows):
    raw = [max(5, max(len(str(r[c])) for r in [head] + rows)) for c in range(len(head))]
    raw = [min(r, 22) for r in raw]
    ws = [PAGE_W - 0.05] * 0
    tot = sum(raw)
    return [round((PAGE_W - 0.1) * r / tot, 2) for r in raw]


def squeeze(bl):
    out = []
    for b in bl:
        if b[0] == "table":
            _, head, rows, w, fs, mh = b
            out.append(("table", head, rows[:3], w, fs, 0.21))
        elif b[0] == "lines":
            out.append(("lines", min(b[1], 2)))
        elif b[0] == "box":
            out.append(("box", min(b[1], 0.75), b[2]))
        else:
            out.append(b)
    return out


def blocks_for(day, s):
    nb = s["nb"]
    if (day, nb) in OVERRIDE:
        return [("h", nb)] + OVERRIDE[(day, nb)]
    out = [("h", nb)]
    note = s.get("nbnote", "")
    if s.get("table"):
        head, rows = s["table"]
        rows = [[r[0]] + [""] * (len(r) - 1) if str(r[0]) not in ("",) else [""] * len(r) for r in rows][:5]
        rows = [r for r in rows]
        w = widths_for(head, rows)
        out.append(("table", head, rows, w, 9 if len(head) <= 3 else 8, 0.25))
        if s.get("frame"):
            out.append(("lines", 1))
        return out
    if any(k in note.lower() for k in SKETCH):
        out.append(("box", 0.95, note))
        return out
    n = len(s.get("frame") or [])
    out.append(("lines", 2 if n <= 1 else 3))
    return out


def layout(day):
    d = U.DAY[day]
    secs = []
    for s in d["sections"]:
        if s.get("nb") and not (secs and secs[-1]["nb"] == s["nb"]):  # a slide that continues the last notebook section adds no block
            secs.append(s)
    allb = [blocks_for(day, s) for s in secs]
    cap_l, cap_r = BOTTOM - LEFT_TOP, BOTTOM - RIGHT_TOP

    def split(allb):
        hs = [sum(block_h(b) for b in bl) for bl in allb]
        best = None
        for k in range(len(allb) + 1):
            lh, rh = sum(hs[:k]), sum(hs[k:])
            if lh > cap_l:
                break
            score = max(lh + 0.4, rh)  # the left page also holds the focus question, so it starts lower
            if best is None or score < best[0]:
                best = (score, k)
        k = best[1]
        return [b for bl in allb[:k] for b in bl], [b for bl in allb[k:] for b in bl]
    left, right = split(allb)
    if sum(block_h(b) for b in right) > cap_r:
        left, right = split([squeeze(bl) for bl in allb])
    return left, right


class Builder:
    def __init__(self, day, old="tpl_nb"):
        self.day = day
        self.old = old
        self.sid = f"nb{day}_slide"
        self.n = 0
        self.reqs = []

    def oid(self):
        self.n += 1
        return f"nb{self.day}_{self.n:02d}"

    def props(self, x, y, w, h):
        return {"pageObjectId": self.sid,
                "size": {"width": {"magnitude": int(w * EMU), "unit": "EMU"}, "height": {"magnitude": int(h * EMU), "unit": "EMU"}},
                "transform": {"scaleX": 1, "scaleY": 1, "translateX": int(x * EMU), "translateY": int(y * EMU), "unit": "EMU"}}

    def style(self, oid, font, size, bold=False, color=None, cell=None):
        st = {"fontFamily": font, "fontSize": {"magnitude": size, "unit": "PT"}, "bold": bold}
        fields = "fontFamily,fontSize,bold"
        if color:
            st["foregroundColor"] = {"opaqueColor": {"rgbColor": color}}
            fields += ",foregroundColor"
        r = {"objectId": oid, "textRange": {"type": "ALL"}, "style": st, "fields": fields}
        if cell:
            r["cellLocation"] = cell
        self.reqs.append({"updateTextStyle": r})

    def textbox(self, x, y, w, h, text, font, size, bold=False, color=None, align=None, bullets=False):
        oid = self.oid()
        self.reqs.append({"createShape": {"objectId": oid, "shapeType": "TEXT_BOX", "elementProperties": self.props(x, y, w, h)}})
        self.reqs.append({"insertText": {"objectId": oid, "insertionIndex": 0, "text": text}})
        self.style(oid, font, size, bold, color)
        if align:
            self.reqs.append({"updateParagraphStyle": {"objectId": oid, "textRange": {"type": "ALL"},
                                                       "style": {"alignment": align}, "fields": "alignment"}})
        if bullets:
            self.reqs.append({"createParagraphBullets": {"objectId": oid, "textRange": {"type": "ALL"},
                                                         "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE"}})

    def table(self, x, y, head, rows, widths, fs, min_h):
        oid = self.oid()
        nr, nc = len(rows) + 1, len(head)
        self.reqs.append({"createTable": {"objectId": oid, "rows": nr, "columns": nc,
                                          "elementProperties": self.props(x, y, sum(widths), 0.3 * nr)}})
        for c, w in enumerate(widths):
            self.reqs.append({"updateTableColumnProperties": {"objectId": oid, "columnIndices": [c], "tableColumnProperties": {
                "columnWidth": {"magnitude": int(w * EMU), "unit": "EMU"}}, "fields": "columnWidth"}})
        for r, line in enumerate([head] + rows):
            for c, txt in enumerate(line):
                cell = {"rowIndex": r, "columnIndex": c}
                # an empty cell would keep the 18 pt default and stretch its row
                self.reqs.append({"insertText": {"objectId": oid, "cellLocation": cell, "insertionIndex": 0, "text": txt or " "}})
                self.style(oid, "Calibri", fs, bold=bool(txt) and (r == 0 or c == 0), cell=cell)
        self.reqs.append({"updateTableCellProperties": {"objectId": oid, "tableRange": {
            "location": {"rowIndex": 0, "columnIndex": 0}, "rowSpan": 1, "columnSpan": nc},
            "tableCellProperties": {"tableCellBackgroundFill": {"solidFill": {"color": {"rgbColor": HDR}}}},
            "fields": "tableCellBackgroundFill.solidFill.color"}})
        self.reqs.append({"updateTableCellProperties": {"objectId": oid, "tableRange": {
            "location": {"rowIndex": 1, "columnIndex": 0}, "rowSpan": nr - 1, "columnSpan": nc},
            "tableCellProperties": {"tableCellBackgroundFill": {"solidFill": {"color": {"rgbColor": WHITE}}}},
            "fields": "tableCellBackgroundFill.solidFill.color"}})
        self.reqs.append({"updateTableRowProperties": {"objectId": oid, "rowIndices": [0], "tableRowProperties": {
            "minRowHeight": {"magnitude": int(row_h(fs, None) * EMU), "unit": "EMU"}}, "fields": "minRowHeight"}})
        self.reqs.append({"updateTableRowProperties": {"objectId": oid, "rowIndices": list(range(1, nr)), "tableRowProperties": {
            "minRowHeight": {"magnitude": int(row_h(fs, min_h) * EMU), "unit": "EMU"}}, "fields": "minRowHeight"}})

    def box(self, x, y, w, h, label):
        oid = self.oid()
        self.reqs.append({"createShape": {"objectId": oid, "shapeType": "ROUND_RECTANGLE", "elementProperties": self.props(x, y, w, h)}})
        self.reqs.append({"updateShapeProperties": {"objectId": oid, "shapeProperties": {
            "shapeBackgroundFill": {"propertyState": "NOT_RENDERED"},
            "outline": {"outlineFill": {"solidFill": {"color": {"rgbColor": ORANGE}}}, "weight": {"magnitude": 1, "unit": "PT"},
                        "dashStyle": "DASH"}, "contentAlignment": "TOP"},
            "fields": "shapeBackgroundFill.propertyState,outline,contentAlignment"}})
        self.reqs.append({"insertText": {"objectId": oid, "insertionIndex": 0, "text": label}})
        self.style(oid, "Calibri", 9, color=GREY)

    def page(self, x, y, blocks):
        for b in blocks:
            k = b[0]
            if k == "h":
                self.textbox(x - 0.04, y, PAGE_W, 0.34, b[1], "Handlee", 14, True, HEAD)
            elif k == "lines":
                self.textbox(x + 0.05, y, PAGE_W - 0.1, 0.22 * b[1], "\n".join([" "] * b[1]), "Arial", 12, bullets=True)
            elif k == "text":
                self.textbox(x, y, PAGE_W, 0.3, b[1], "Calibri", 10)
            elif k == "box":
                self.box(x + 0.02, y, PAGE_W - 0.08, b[1], b[2])
            elif k == "table":
                self.table(x + 0.03, y, *b[1:])
            y += block_h(b)
        return y

    def build(self):
        d = U.DAY[self.day]
        left, right = layout(self.day)
        self.reqs.append({"deleteObject": {"objectId": self.old}})
        self.reqs.append({"createSlide": {"objectId": self.sid, "insertionIndex": 1,
                                          "slideLayoutReference": {"predefinedLayout": "BLANK"}}})
        bg = self.oid()
        self.reqs.append({"createImage": {"objectId": bg, "url": BG, "elementProperties": self.props(0, 0.06, 10.0, 5.47)}})
        title = f"Day {self.day}: {d['title']}"
        size = 24 if len(title) <= 36 else 19 if len(title) <= 50 else 16
        self.textbox(0.55, 0.12, 8.89, 0.5, title, "Boogaloo", size, True, BLACK, align="CENTER")
        self.textbox(LEFT_X - 0.02, 0.55, 4.6, 0.45, "Focus question: " + d["focus"], "Calibri", 11, True)
        yl = self.page(LEFT_X, LEFT_TOP, left)
        yr = self.page(RIGHT_X, RIGHT_TOP, right)
        warn = [f"day {self.day} {w} page ends {y:.2f} in" for w, y in (("left", yl), ("right", yr)) if y > BOTTOM + 0.05]
        return self.reqs, warn


if __name__ == "__main__":
    reqs, warn = Builder(int(sys.argv[1]), sys.argv[2] if len(sys.argv) > 2 else "tpl_nb").build()
    for w in warn:
        print("WARN", w, file=sys.stderr)
    print(json.dumps(reqs, ensure_ascii=False, separators=(",", ":")))
