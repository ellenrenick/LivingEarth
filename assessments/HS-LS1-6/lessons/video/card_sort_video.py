"""Build "Part 3: Molecule Card Sort" (Lesson 2 support video) as an MP4.

Walks through the card sort: count three example cards, sort by which elements a
molecule contains, then decide what a plant can build from only CO2 and water.
It models the method without giving away every card's group.

  python3 card_sort_video.py out.mp4
"""

import sys
import tempfile
from pathlib import Path

import atom_counting_video as V

V.COLORS.update({"P": (230, 125, 20), "Mg": (40, 150, 80)})
V.NAMES.update({"P": "phosphorus", "Mg": "magnesium"})
W, H, INK, MUTED, HILITE = V.W, V.H, V.INK, V.MUTED, V.HILITE
GOOD, BAD = (46, 125, 50), (190, 50, 50)
KICKER = "LESSON 2 · PART 3 · MOLECULE CARD SORT"

SUCROSE = [("C", 12), ("H", 22), ("O", 11)]
VALINE = [("C", 5), ("H", 11), ("N", 1), ("O", 2)]
AMP = [("C", 10), ("H", 14), ("N", 5), ("O", 7), ("P", 1)]
GLUCOSE = [("C", 6), ("H", 12), ("O", 6)]
GROUPS = [("C, H, O only", "CHO"), ("C and H only", "CH"), ("C, H, O, N", "CHON"),
          ("C, H, O, N, P", "CHONP"), ("C, H, O, N, Mg", "CHONMg")]


def chip(d, x, y, w, h, text, fill, color=INK, size=30):
    d.rounded_rectangle([x, y, x + w, y + h], radius=16, fill=fill, outline=(160, 150, 130), width=2)
    d.text((x + w / 2, y + h / 2), text, font=V.font(size, True), fill=color, anchor="mm")


def render(title, spec):
    img, d = V.frame(title, kicker=KICKER)
    kind = spec.get("kind")
    if kind == "intro":
        for i, (step, txt) in enumerate([("1  COUNT", "Count the atoms on each card"),
                                         ("2  SORT", "Group cards by which elements they have"),
                                         ("3  APPLY", "What can a plant build from CO₂ + water?")]):
            y = 190 + i * 140
            chip(d, 120, y, 300, 100, step, (232, 220, 198), size=36)
            d.text((460, y + 50), txt, font=V.font(34, True), fill=INK, anchor="lm")
    elif kind == "table":
        cols = ["Card", "C", "H", "O", "N", "Other"]
        xs = [140, 420, 560, 700, 840, 980]
        for x, c in zip(xs, cols):
            chip(d, x - 10, 200, 130 if c != "Card" else 250, 60, c, (232, 220, 198), size=28)
        for r in range(4):
            d.rectangle([130, 270 + r * 70, 1120, 330 + r * 70], outline=(180, 170, 150), width=2)
        d.text((W / 2, 600), "Split the 11 cards in your group. Check each other's counts.", font=V.font(30, True), fill=INK, anchor="mm")
    elif kind == "count":
        V.draw_formula(d, spec["parts"], 160, hi=spec.get("hi"))
        if spec.get("counts"):
            V.draw_tally(d, spec["counts"], 390, total=True)
            n = sum(c for _, c in spec["counts"])
            if n <= 32:
                V.draw_beads(d, spec["counts"], 530, r=16 if n > 16 else 26)
    elif kind == "same":
        V.draw_formula(d, GLUCOSE, 150, size=90)
        V.draw_formula(d, SUCROSE, 330, size=90)
        chip(d, 340, 540, 600, 80, "Same elements: C, H, O  →  same group", HILITE, size=32)
    elif kind == "different":
        V.draw_formula(d, GLUCOSE, 150, size=90)
        V.draw_formula(d, VALINE, 330, size=90, hi=2)
        chip(d, 290, 540, 700, 80, "Valine has N  →  a different group", HILITE, size=32)
    elif kind == "groups":
        for i, (name, _) in enumerate(GROUPS):
            x = 90 + (i % 3) * 380
            y = 200 + (i // 3) * 170
            chip(d, x, y, 340, 120, name, (232, 220, 198) if not spec.get("judge") else
                 ((214, 236, 214) if name in ("C, H, O only", "C and H only") else (246, 218, 214)), size=32)
            if spec.get("judge"):
                ok = name in ("C, H, O only", "C and H only")
                d.text((x + 170, y + 150), "✓ CO₂ + H₂O" if ok else "✗ needs soil", font=V.font(26, True),
                       fill=GOOD if ok else BAD, anchor="mm")
        if not spec.get("judge"):
            d.text((W / 2, 610), "Pause the video and sort your 11 cards into these groups.", font=V.font(30, True), fill=INK, anchor="mm")
    elif kind == "inputs":
        V.draw_formula(d, [("C", 1), ("O", 2)], 170, size=100)
        V.draw_formula(d, [("H", 2), ("O", 1)], 320, size=100)
        chip(d, 290, 540, 700, 80, "Only C, H, and O come in", HILITE, size=34)
    elif kind == "nochange":
        d.text((W / 2, 260), "C  →  N ?", font=V.font(150, True), fill=INK, anchor="mm")
        d.line([480, 340, 800, 180], fill=BAD, width=14)
        d.text((W / 2, 470), "Atoms are rearranged, never changed into another element.", font=V.font(32, True), fill=INK, anchor="mm")
        d.text((W / 2, 530), "The sealed bag: mass stayed the same because the atoms stayed the same.", font=V.font(26), fill=MUTED, anchor="mm")
    elif kind == "rule":
        lines = ["A plant can build a molecule from only CO₂ and water",
                 "if the molecule contains only ____________.",
                 "If it also has ____________,",
                 "the plant needs ____________ from the ____________."]
        for i, t in enumerate(lines):
            d.text((110, 190 + i * 85), t, font=V.font(36, True), fill=INK)
        d.text((110, 560), "Write your class's rule in your notebook.", font=V.font(30), fill=MUTED)
    elif kind == "summary":
        for i, t in enumerate(["1. Count: subscripts tell how many; no number means 1.",
                               "2. Sort by WHICH elements, not how many atoms.",
                               "3. CO₂ + water give only C, H, O.",
                               "4. N, P, and Mg must come from the soil."]):
            d.text((120, 210 + i * 90), t, font=V.font(38, True), fill=INK)
    return img


def count_scenes(name, parts, say):
    total = sum(n for _, n in parts)
    words = ", ".join(f"{n} {V.NAMES[s]}" for s, n in parts)
    return [(f"Card: {name}", dict(kind="count", parts=parts), say),
            (f"Card: {name}", dict(kind="count", parts=parts, counts=parts),
             f"So {name} has {words}. That is {total} atoms.")]


SCENES = (
    [("Molecule Card Sort", dict(kind="intro"),
      "Part 3, the molecule card sort. You will count the atoms on each card, sort the cards by which elements they contain, "
      "and then decide which molecules a plant could build from only carbon dioxide and water."),
     ("Step 1: Count", dict(kind="table"),
      "Step 1, count. Split the 11 cards among your group. For each card, write how many carbon, hydrogen, oxygen, and nitrogen atoms it has, "
      "and any other elements. Then check each other's counts. Let's try three cards together.")]
    + count_scenes("sucrose", SUCROSE, "Sucrose is table sugar. The formula is C 12, H 22, O 11.")
    + count_scenes("valine", VALINE, "Valine is an amino acid. C 5, H 11, N, O 2. Remember, N with no number means 1 nitrogen.")
    + count_scenes("AMP", AMP, "AMP is a piece of DNA and RNA. C 10, H 14, N 5, O 7, P. "
                   "P is phosphorus, and with no number it means 1 phosphorus atom.")
    + [("Step 2: Sort by which elements", dict(kind="same"),
        "Step 2, sort. Group the cards by which elements they contain, not by how many atoms. Glucose and sucrose have different numbers, "
        "but they both have only carbon, hydrogen, and oxygen. So they go in the same group."),
       ("Step 2: Sort by which elements", dict(kind="different"),
        "Valine has nitrogen. Glucose does not. So valine goes in a different group."),
       ("Your turn: sort into groups", dict(kind="groups"),
        "Your cards will fit into five groups. C, H, O only. C and H only. C, H, O, and N. C, H, O, N, and P. And C, H, O, N, and magnesium. "
        "Pause the video now and sort your 11 cards. Give each group a name and record it in your table."),
       ("Step 3: Apply", dict(kind="inputs"),
        "Step 3, apply. A plant takes in carbon dioxide and water. Carbon dioxide has carbon and oxygen. Water has hydrogen and oxygen. "
        "So the only atoms coming in are carbon, hydrogen, and oxygen."),
       ("Step 3: Which can the plant build?", dict(kind="groups", judge=True),
        "That means a plant can build the C, H, O molecules and the C and H molecules from only carbon dioxide and water. "
        "Any molecule with nitrogen, phosphorus, or magnesium needs those atoms from another source. For a plant, that source is the soil."),
       ("Can carbon turn into nitrogen?", dict(kind="nochange"),
        "Could the plant just turn some extra carbon atoms into nitrogen? No. Remember the sealed bag. "
        "Atoms are rearranged into new molecules, but they are never created, destroyed, or changed into a different element."),
       ("The atom accounting rule", dict(kind="rule"),
        "Now write the atom accounting rule with your class. A plant can build a molecule from only carbon dioxide and water if the molecule "
        "contains only blank. If it also has blank, the plant needs blank from the blank."),
       ("Remember", dict(kind="summary"),
        "Remember. Count the atoms using the subscripts. Sort by which elements, not how many. Carbon dioxide and water only give carbon, "
        "hydrogen, and oxygen. Nitrogen, phosphorus, and magnesium have to come from the soil.")]
)


def main(out):
    V.SCENES[:] = SCENES
    V.render = render
    V.main(out)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "card_sort_lesson2.mp4")
