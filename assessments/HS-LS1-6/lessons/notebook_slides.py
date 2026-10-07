"""Notebook set-up example slides, modeled on slide 2 of the Lesson 2 deck.

Each slide is a two-page notebook spread (left page, right page) on the same
notebook-paper background, with the same fonts: Boogaloo title, Handlee section
headings, Calibri focus question and tables (tan header row), and lined answer
boxes. Students copy the layout into their notebooks before the lesson.

Layouts are written in Lesson 2 page units (10 x 5.625 in) and scaled to each
deck's page size. The slide goes in as slide 2, right after the title slide.

  python3 notebook_slides.py L5      # prints the batchUpdate requests
"""

import json
import sys

EMU = 914400
BG = "http://res.publicdomainfiles.com/pdf_view/83/13939457415622.png"
HEAD_COLOR = {"red": 0.13725491, "green": 0.22352941, "blue": 0.17254902}
TAN = {"red": 0.9098039, "green": 0.8627451, "blue": 0.7764706}
LEFT_X, RIGHT_X, PAGE_W = 0.22, 5.09, 4.45
BOTTOM = 5.2

CER_LOG = "Unit CER evidence log (back of notebook): add today's row."

DECKS = {
    "L5": dict(
        id="1tF7urG91FWcNfaae2WjjEmJLZPPd1_C2BmPdBm1regM", scale=12192000 / 9144000,
        title="Small Pieces, Big Molecules",
        focus="How do amino acids become proteins, and what happens to them when an animal eats?",
        left=[("h", "Warm-up"), ("lines", 2),
              ("h", "Part 1: Monomers and polymers"),
              ("table", ["Monomer (small)", "Polymer (large)", "Job in a pumpkin"],
               [["Amino acid", "", ""], ["Glucose", "Starch", ""], ["Glucose", "", "Tough cell walls"], ["Nucleotide", "", ""]],
               [1.3, 1.3, 1.85], 9, None),
              ("text", "Starch and cellulose contain: ______   Proteins contain: ______"),
              ("h", "Part 2A: Build a pumpkin seed protein"),
              ("table", ["Amino acid", "V", "L", "T", "K", "Q"], [["How many?", "", "", "", "", ""]],
               [1.45, 0.6, 0.6, 0.6, 0.6, 0.6], 9, None)],
        right=[("h", "Part 2B: Eat, digest, and rebuild"),
               ("table", ["Amino acid", "V", "L", "T", "K", "Q"],
                [["Hair protein needs", "", "", "", "", ""], ["Short or extra (+/−)", "", "", "", "", ""]],
                [1.45, 0.6, 0.6, 0.6, 0.6, 0.6], 9, None),
               ("text", "Same protein as the pumpkin's? ____  Where did its atoms come from? ____"),
               ("h", "Part 3: Trace a carbon atom"),
               ("table", ["Step", "Where is the carbon atom?", "What happens to it?"],
                [["1", "In a ____ molecule in the air", "A pumpkin leaf takes it in."],
                 ["2", "In a ____ molecule in the leaf", "Built during ____ using ____ energy"],
                 ["3", "In an ____", "Combined with ____ from the soil"],
                 ["4", "In a pumpkin seed ____", "Linked in a specific ____"],
                 ["5", "In an amino acid in your blood", "You ate the seed and ____ it."],
                 ["6", "In your hair protein", "Your cells ____ them in a new order."]],
                [0.4, 2.0, 2.05], 7, None),
               ("h", "Exit ticket"), ("lines", 2)],
    ),
    "L6": dict(
        id="1Uip06UmGWFJnyU8avQuP3ko_bnp3yRbCBXrCxBCDRYI", scale=12192000 / 9144000,
        title="What's the Evidence?",
        focus="What evidence do scientists have for how plants build their molecules?",
        left=[("text", "Home group #: ______      My station #: ______"),
              ("h", "Part 1: Expert notes (my station)"),
              ("table", ["Question", "My answer"],
               [["1", ""], ["2", ""], ["3", ""], ["4", ""], ["5 (Station 3 only)", ""]],
               [1.25, 3.2], 9, 0.36),
              ("h", "The most important thing my station shows:"), ("lines", 2)],
        right=[("h", "Part 2: Home group evidence table"),
               ("table", ["Station", "What they did", "Key data (numbers)", "What it shows", "Claim(s)"],
                [["1. Labeled carbon", "", "", "", ""], ["2. Tomatoes, no N", "", "", "", ""],
                 ["3. Squash + fungi", "", "", "", ""], ["4. Extra CO₂", "", "", "", ""]],
                [0.95, 0.95, 0.95, 0.95, 0.65], 7, 0.42),
               ("h", "Exit ticket: CER (Station 2)"),
               ("table", ["Part", "My answer"], [["Claim", ""], ["Evidence (2 numbers)", ""], ["Reasoning", ""]],
                [1.3, 3.15], 9, 0.34),
               ("text", CER_LOG)],
    ),
    "L7": dict(
        id="1t8Lrk0jHV10WnJJ9fgdSycAylj6la1xpOCUN383YD74", scale=12192000 / 9144000,
        title="Solving the Pumpkin Mystery",
        focus="What is the pumpkin made of, and how did it get built?",
        left=[("h", "Warm-up"), ("lines", 2),
              ("h", "Part 1: Class consensus model"),
              ("box", 1.25, "Draw: what goes into the leaf · what the leaf builds · what comes from the soil · "
                            "what the plant builds from sugar + soil elements. Label each arrow with its evidence."),
              ("h", "Part 2: Revise my Day 1 model"),
              ("table", ["Then I thought…", "Now I think…", "Because (evidence)…"], [["", "", ""], ["", "", ""]],
               [1.48, 1.48, 1.49], 9, 0.32)],
        right=[("h", "Part 3: Explain it to the grower (Unit CER)"),
               ("table", ["Checklist", "My explanation"],
                [["Claim: what the pumpkin is made of", ""], ["Evidence: 2 pieces of grower data", ""],
                 ["Evidence: 1 piece from class", ""], ["Reasoning: sugar from CO₂ + water, then + N", ""],
                 ["Correct the grower: soil and plant food", ""], ["Energy vs. matter: sunlight", ""]],
                [1.65, 2.8], 8, 0.4),
               ("h", "Part 4: Peer scoring"),
               ("table", ["Scored by", "Score (1–4)", "Glow", "Grow"], [["", "", "", ""]],
                [1.0, 0.85, 1.3, 1.3], 8, 0.34)],
    ),
    "D5": dict(
        id="1SakPKw-q29gXMRUfa0g7DF0myjJ3qIO-bjUgRttQLR8", scale=1.0,
        title="Vocabulary and SketchNotes",
        focus="What words and big ideas will we need to solve the pumpkin mystery?",
        left=[("h", "Frayer chart: 10 words"),
              ("table", ["Word", "Definition (my words)", "Facts", "Example (draw)", "Non-example"],
               [["Atom"] + [""] * 4, ["Element"] + [""] * 4, ["Molecule"] + [""] * 4,
                ["Conservation of matter"] + [""] * 4, ["Photosynthesis"] + [""] * 4, ["Glucose"] + [""] * 4,
                ["Amino acid"] + [""] * 4, ["Protein"] + [""] * 4, ["Monomer"] + [""] * 4, ["Polymer"] + [""] * 4],
               [0.95, 1.25, 0.8, 0.8, 0.65], 7, 0.3)],
        right=[("h", "SketchNotes: Sugar to Structures"),
               ("box", 1.9, "The 5 big ideas: a short phrase + a simple icon for each. One color for matter, another for energy. No full sentences."),
               ("h", "Sensemaking: the Pumpkin Path"),
               ("box", 1.75, "Draw the pumpkin plant with air, water, soil, and sunlight. Solid arrows = matter, dashed arrows = energy. "
                             "Add one idea from each of Days 1–4, then keep adding after each lesson.")],
    ),
    "D9": dict(
        id="1yKhzC3fnl-McGFuwPbjTfEk3VI_Vff_qkEfvcL3ExYA", scale=1.0,
        title="Review: Sugar to Structures",
        focus="Can I explain how a pumpkin builds its body from sugar?",
        left=[("h", "Self-rating (1–4)"),
              ("table", ["Target", "Do Now", "After stations"],
               [["LS1-6.1 Elements in sugar and large molecules", "", ""], ["LS1-6.2 Taking in and rearranging matter", "", ""],
                ["LS1-6.3 Sugar atoms plus other elements", "", ""], ["LS1-6.4 Trace atoms with a model", "", ""],
                ["LS1-6.5 Explain with evidence", "", ""], ["LS1-6.6 Revise an explanation", "", ""]],
               [2.95, 0.7, 0.8], 8, None),
              ("h", "Review stations"),
              ("table", ["Station", "One thing I learned or fixed"],
               [["A · Atoms and elements", ""], ["B · Sugar plus nitrogen", ""], ["C · Trace the atoms", ""],
                ["D · Evidence and revision", ""]],
               [1.55, 2.9], 8, 0.3)],
        right=[("h", "Driving question"),
               ("text", "How does a plant build its body, and what is it built from? Use at least 4 vocabulary words."),
               ("lines", 4),
               ("h", "Practice test reflection"),
               ("text", "My lowest target: ______   My plan before the CSA: ______"),
               ("lines", 3)],
    ),
    "D10": dict(
        id="1jVo_CDFD9Cz6mf4n6Q3llg3l6LiBdm60L5xXxhWonfk", scale=1.0,
        title="CSA Reflection",
        focus="How do atoms from sugar become the structures of living things?",
        left=[("h", "After the CSA: rate yourself (1–4)"),
              ("table", ["Target", "Day 9", "Today"],
               [["LS1-6.1 Elements in sugar and large molecules", "", ""], ["LS1-6.2 Taking in and rearranging matter", "", ""],
                ["LS1-6.3 Sugar atoms plus other elements", "", ""], ["LS1-6.4 Trace atoms with a model", "", ""],
                ["LS1-6.5 Explain with evidence", "", ""], ["LS1-6.6 Revise an explanation", "", ""]],
               [3.15, 0.65, 0.65], 8, None),
              ("h", "Which target improved the most since Day 1? Why?"), ("lines", 3)],
        right=[],
    ),
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


class Builder:
    def __init__(self, deck):
        self.d = DECKS[deck]
        self.k = self.d["scale"]
        self.pre = f"nb_{deck.lower()}"
        self.sid = self.pre + "_slide"
        self.layout = {"predefinedLayout": "BLANK"}
        self.n = 0
        self.reqs = []

    def oid(self):
        self.n += 1
        return f"{self.pre}_{self.n:02d}"

    def props(self, x, y, w, h):
        k = self.k
        return {"pageObjectId": self.sid,
                "size": {"width": {"magnitude": int(w * k * EMU), "unit": "EMU"},
                         "height": {"magnitude": int(h * k * EMU), "unit": "EMU"}},
                "transform": {"scaleX": 1, "scaleY": 1, "translateX": int(x * k * EMU),
                              "translateY": int(y * k * EMU), "unit": "EMU"}}

    def style(self, oid, font, size, bold=False, color=None, cell=None):
        st = {"fontFamily": font, "fontSize": {"magnitude": round(size * self.k, 1), "unit": "PT"}, "bold": bold}
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
        return oid

    def table(self, x, y, head, rows, widths, fs, min_h):
        oid = self.oid()
        nr, nc = len(rows) + 1, len(head)
        self.reqs.append({"createTable": {"objectId": oid, "rows": nr, "columns": nc,
                                          "elementProperties": self.props(x, y, sum(widths), 0.3 * nr)}})
        for c, w in enumerate(widths):
            self.reqs.append({"updateTableColumnProperties": {"objectId": oid, "columnIndices": [c],
                              "tableColumnProperties": {"columnWidth": {"magnitude": int(w * self.k * EMU), "unit": "EMU"}},
                              "fields": "columnWidth"}})
        for r, line in enumerate([head] + rows):
            for c, txt in enumerate(line):
                cell = {"rowIndex": r, "columnIndex": c}
                if txt:
                    self.reqs.append({"insertText": {"objectId": oid, "cellLocation": cell, "insertionIndex": 0, "text": txt}})
                    self.style(oid, "Calibri", fs, bold=(r == 0 or c == 0 and bool(txt)), cell=cell)
        self.reqs.append({"updateTableCellProperties": {"objectId": oid,
                          "tableRange": {"location": {"rowIndex": 0, "columnIndex": 0}, "rowSpan": 1, "columnSpan": nc},
                          "tableCellProperties": {"tableCellBackgroundFill": {"solidFill": {"color": {"rgbColor": TAN}}}},
                          "fields": "tableCellBackgroundFill.solidFill.color"}})
        self.reqs.append({"updateTableCellProperties": {"objectId": oid,
                          "tableRange": {"location": {"rowIndex": 1, "columnIndex": 0}, "rowSpan": nr - 1, "columnSpan": nc},
                          "tableCellProperties": {"tableCellBackgroundFill": {"solidFill": {"color": {"rgbColor": {"red": 1, "green": 1, "blue": 1}}}}},
                          "fields": "tableCellBackgroundFill.solidFill.color"}})
        self.reqs.append({"updateTableRowProperties": {"objectId": oid, "rowIndices": list(range(nr)),
                          "tableRowProperties": {"minRowHeight": {"magnitude": int(row_h(fs, None) * self.k * EMU), "unit": "EMU"}},
                          "fields": "minRowHeight"}})
        if min_h:
            self.reqs.append({"updateTableRowProperties": {"objectId": oid, "rowIndices": list(range(1, nr)),
                              "tableRowProperties": {"minRowHeight": {"magnitude": int(min_h * self.k * EMU), "unit": "EMU"}},
                              "fields": "minRowHeight"}})

    def box(self, x, y, w, h, label):
        oid = self.oid()
        self.reqs.append({"createShape": {"objectId": oid, "shapeType": "ROUND_RECTANGLE", "elementProperties": self.props(x, y, w, h)}})
        self.reqs.append({"updateShapeProperties": {"objectId": oid, "shapeProperties": {
            "shapeBackgroundFill": {"propertyState": "NOT_RENDERED"},
            "outline": {"outlineFill": {"solidFill": {"color": {"rgbColor": HEAD_COLOR}}},
                        "weight": {"magnitude": 1, "unit": "PT"}, "dashStyle": "DASH"},
            "contentAlignment": "TOP"}, "fields": "shapeBackgroundFill.propertyState,outline,contentAlignment"}})
        self.reqs.append({"insertText": {"objectId": oid, "insertionIndex": 0, "text": label}})
        self.style(oid, "Calibri", 9, color={"red": 0.42, "green": 0.46, "blue": 0.43})

    def page(self, x, y, blocks):
        for b in blocks:
            k = b[0]
            if k == "h":
                self.textbox(x - 0.04, y, PAGE_W, 0.34, b[1], "Handlee", 14, True, HEAD_COLOR)
            elif k == "lines":
                self.textbox(x + 0.05, y, PAGE_W - 0.1, 0.22 * b[1], "\n".join([" "] * b[1]), "Arial", 12, bullets=True)
            elif k == "text":
                self.textbox(x, y, PAGE_W, 0.3, b[1], "Calibri", 10)
            elif k == "box":
                self.box(x + 0.02, y, PAGE_W - 0.08, b[1], b[2])
            elif k == "table":
                self.table(x + 0.03, y, *b[1:])
            y += block_h(b)
        if y > BOTTOM + 0.05:
            print(f"WARNING: page content ends at {y:.2f} in (page bottom {BOTTOM})", file=sys.stderr)
        return y

    def build(self):
        d = self.d
        self.reqs.append({"createSlide": {"objectId": self.sid, "insertionIndex": 1,
                                          "slideLayoutReference": self.layout}})
        bg = self.oid()
        self.reqs.append({"createImage": {"objectId": bg, "url": BG, "elementProperties": self.props(0, 0.06, 10.0, 5.47)}})
        self.textbox(0.55, 0.12, 8.89, 0.5, d["title"], "Boogaloo", 24, True, {"red": 0, "green": 0, "blue": 0}, align="CENTER")
        self.textbox(LEFT_X - 0.02, 0.55, 4.6, 0.45, "Focus question: " + d["focus"], "Calibri", 11, True)
        self.page(LEFT_X, 1.02, d["left"])
        self.page(RIGHT_X, 0.62, d["right"])
        return self.reqs


if __name__ == "__main__":
    b = Builder(sys.argv[1])
    # Optional layout id: some decks' masters have no predefined BLANK layout.
    if len(sys.argv) > 2:
        b.layout = {"layoutId": sys.argv[2]}
    print(json.dumps(b.build(), ensure_ascii=False))
