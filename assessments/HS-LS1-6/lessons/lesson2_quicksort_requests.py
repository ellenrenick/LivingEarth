"""Slides requests: swap Lesson 2's 11-card sort for the 10-minute "Who needs the soil?" part.

Rewrites the Part 3 slides (watch the video, then a 4-molecule quick sort), the
agenda row, the discussion slide, and the Part 3 side of the notebook slide.

  python3 lesson2_quicksort_requests.py     # prints the JSON request list
"""

import json

EMU = 914400
P = "h287605ecd2867468_0_"
NB = P + "217"
TAN = {"red": 0.9098039, "green": 0.8627451, "blue": 0.7764706}
MOLECULES = [("Glucose", "C₆H₁₂O₆"), ("Oleic acid", "C₁₈H₃₄O₂"), ("Valine", "C₅H₁₁NO₂"), ("AMP", "C₁₀H₁₄N₅O₇P"),
             ("Challenge: chlorophyll a", "C₅₅H₇₂MgN₄O₅")]
RULE = "A plant can build ________ from only CO₂ and water. To build ________, it also needs ________ from the ________."

TEXT = {
    P + "172": "PART 3 · 10 MIN · WITH A PARTNER",
    P + "173": "Who needs the soil?",
    P + "175": "STEP 1 · WATCH · 3 MIN",
    P + "176": "Video: Plants Need More Than C, H, and O\n"
               "Listen for: which big molecules need elements besides C, H, and O?\n"
               "Pause when the video says “Your turn.”",
    P + "178": "STEP 2 · QUICK SORT · 5 MIN",
    P + "179": "For each molecule, name its type of big molecule.\n"
               "Could a plant build it from only CO₂ + water? Y or N.\n"
               "List any extra element(s) it needs from the soil.",
    P + "185": "STEP 2 · QUICK SORT · 5 MIN",
    P + "186": "What can a plant build from only CO₂ + water?",
    P + "187": "\n".join(f"{n}  {f}" for n, f in MOLECULES)
               + "\nWhy can't the plant just turn extra carbon atoms into nitrogen? (Think: the sealed bag.)",
    P + "193": "DISCUSSION · 4 MIN · WHOLE CLASS",
    P + "195": "Share your quick sort. Which molecules needed the soil, and for which elements?\n"
               "As a class, finish the atom accounting rule.\n"
               "Copy the rule into your notebook.",
    P + "198": "Rule: " + RULE,
    P + "297": "Part 3: Who needs the soil?",
}


def requests():
    reqs = []
    for oid, text in TEXT.items():
        reqs.append({"deleteText": {"objectId": oid, "textRange": {"type": "ALL"}}})
        reqs.append({"insertText": {"objectId": oid, "insertionIndex": 0, "text": text}})
    reqs.append({"replaceAllText": {"containsText": {"text": "Molecule card sort", "matchCase": True},
                                    "replaceText": "Who needs the soil? (video + quick sort)",
                                    "pageObjectIds": [P + "117"]}})

    # Notebook slide, right page: new quick-sort table and rule frame in place of the two card-sort tables.
    reqs += [{"deleteObject": {"objectId": P + "300"}}, {"deleteObject": {"objectId": P + "302"}}]
    tbl = "nb_l2_quicksort"
    head = ["Molecule", "Formula", "Type of big molecule", "CO₂ + H₂O only?", "Extra element(s)"]
    widths = [1.15, 0.95, 0.95, 0.6, 0.6]
    rows = [head] + [[n, f, "", "", ""] for n, f in MOLECULES]
    reqs.append({"createTable": {"objectId": tbl, "rows": len(rows), "columns": len(head), "elementProperties": {
        "pageObjectId": NB, "transform": {"scaleX": 1, "scaleY": 1, "translateX": 4655925, "translateY": 925862, "unit": "EMU"},
        "size": {"width": {"magnitude": int(sum(widths) * EMU), "unit": "EMU"},
                 "height": {"magnitude": int(0.3 * len(rows) * EMU), "unit": "EMU"}}}}})
    for c, w in enumerate(widths):
        reqs.append({"updateTableColumnProperties": {"objectId": tbl, "columnIndices": [c],
                     "tableColumnProperties": {"columnWidth": {"magnitude": int(w * EMU), "unit": "EMU"}},
                     "fields": "columnWidth"}})
    for r, row in enumerate(rows):
        for c, s in enumerate(row):
            if not s:
                continue
            loc = {"rowIndex": r, "columnIndex": c}
            reqs.append({"insertText": {"objectId": tbl, "cellLocation": loc, "insertionIndex": 0, "text": s}})
            reqs.append({"updateTextStyle": {"objectId": tbl, "cellLocation": loc, "textRange": {"type": "ALL"},
                         "style": {"fontSize": {"magnitude": 9, "unit": "PT"}, "bold": r == 0},
                         "fields": "fontSize,bold"}})
    reqs.append({"updateTableCellProperties": {"objectId": tbl,
                 "tableRange": {"location": {"rowIndex": 0, "columnIndex": 0}, "rowSpan": 1, "columnSpan": len(head)},
                 "tableCellProperties": {"tableCellBackgroundFill": {"solidFill": {"color": {"rgbColor": TAN}}}},
                 "fields": "tableCellBackgroundFill.solidFill.color"}})
    reqs.append({"updateTableRowProperties": {"objectId": tbl, "rowIndices": list(range(1, len(rows))),
                 "tableRowProperties": {"minRowHeight": {"magnitude": int(0.34 * EMU), "unit": "EMU"}},
                 "fields": "minRowHeight"}})

    rule = "nb_l2_rule"
    reqs.append({"createShape": {"objectId": rule, "shapeType": "TEXT_BOX", "elementProperties": {
        "pageObjectId": NB, "transform": {"scaleX": 1, "scaleY": 1, "translateX": 4655925, "translateY": int(3.25 * EMU), "unit": "EMU"},
        "size": {"width": {"magnitude": int(4.25 * EMU), "unit": "EMU"}, "height": {"magnitude": int(0.7 * EMU), "unit": "EMU"}}}}})
    label = "Atom accounting rule: "
    reqs.append({"insertText": {"objectId": rule, "insertionIndex": 0, "text": label + RULE}})
    reqs.append({"updateTextStyle": {"objectId": rule, "textRange": {"type": "ALL"},
                 "style": {"fontFamily": "Calibri", "fontSize": {"magnitude": 10, "unit": "PT"}, "bold": False},
                 "fields": "fontFamily,fontSize,bold"}})
    reqs.append({"updateTextStyle": {"objectId": rule, "textRange": {"type": "FIXED_RANGE", "startIndex": 0, "endIndex": len(label)},
                 "style": {"bold": True}, "fields": "bold"}})
    return reqs


if __name__ == "__main__":
    print(json.dumps(requests(), ensure_ascii=False, separators=(",", ":")))
